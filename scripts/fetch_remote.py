#!/usr/bin/env python3
"""Fetch and check remote marketplace entries declared under ext/.

Each `ext/<section>/<slug>/index.toml` points at content in another GitHub
repository:

    repo = "owner/name"   required: GitHub owner/name
    ref  = "v1.2.0"       optional: tag, branch, or commit SHA; the repo's
                          default branch when omitted (unpinned remote
                          entries drift — CI re-validates the current state)
    path = "skills/x"     required: subtree root inside that repository
    tags = "a, b"         optional: marketplace-side tags, appended to the
                          tags the entry's own frontmatter carries

The path may itself be an entry directory (holding SKILL.md/PROMPT.md,
published as <slug>); every directory below it that holds an entry file is
an entry too, published as <slug>/<relative-path> at any depth. Only
index.toml may sit in an ext directory.

The fetched entry files run through the same frontmatter checks as data/
entries (the slug is the remote directory's own name, agent extras, PNG
magic), so a green check means the marketplace would accept the entry as
if it lived here. The repository's top contributors (the ten with the most
contributions) become the entry's authors, joined with ", ".

Standard library only besides validate (mirrored rules, no extra deps);
GITHUB_TOKEN is used for API calls when set.
"""

import json
import os
import re
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

import tomllib
import validate

API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
MANIFEST_NAME = "index.toml"
MANIFEST_KEYS = ("repo", "ref", "path", "tags")
REPO_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
CONTRIBUTOR_LIMIT = 10
FETCH_WORKERS = 8


@dataclass
class RemoteEntry:
    """One remote entry: its ext identity, source location, fetched files.

    Only `section`, `slug`, `repo`, `ref`, `path`, and `rel` are set by
    hand; key/sub/dir_path derive from `rel` ("" for a single-shape entry).
    """

    section: str  # "skills" | "agents"
    slug: str  # ext/<section>/<slug> holding the manifest
    repo: str
    ref: str | None
    path: str  # manifest path, repository-relative
    rel: str = ""  # entry directory's path under `path`
    files: dict[str, bytes] = field(default_factory=dict)  # name -> bytes

    @property
    def key(self) -> str:
        """The index key: <slug> or <slug>/<relative-path>."""
        return f"{self.slug}/{self.rel}" if self.rel else self.slug

    @property
    def name_slug(self) -> str:
        """The remote directory name — what frontmatter `name` must match."""
        return (
            PurePosixPath(self.rel).name if self.rel else PurePosixPath(self.path).name
        )

    @property
    def dir_path(self) -> str:
        """The entry directory's full path in the remote tree."""
        return f"{self.path}/{self.rel}" if self.rel else self.path


@dataclass
class RemoteResult:
    """Everything fetched for one manifest, plus contributor authorship."""

    slug: str
    section: str
    repo: str
    ref: str | None
    path: str
    tags: str | None
    entries: list[RemoteEntry]
    authors: str | None
    tree: frozenset[str] = frozenset()  # all blob paths at the pinned commit
    excluded: int = 0  # entries dropped for breaking content rules
    exclude_reasons: list[str] = field(default_factory=list)

    def exclusion_warnings(self, where: str) -> list[str]:
        """The non-fatal notices for entries this manifest dropped."""
        if not self.excluded:
            return []
        head = (
            f"{where}: {self.excluded} entr"
            f"{'y' if self.excluded == 1 else 'ies'} excluded — "
            f"upstream content breaks the entry rules:"
        )
        return [head, *(f"    {r}" for r in self.exclude_reasons)]


class FetchError(Exception):
    """A network or API failure; callers turn this into a validation error."""


class ManifestError(Exception):
    """The index.toml is malformed or violates the ext schema."""


# --- fetching -----------------------------------------------------------------


def _request(url: str, token: str | None) -> tuple[int, bytes]:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "entoli-marketplace")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, b""
    except urllib.error.URLError as exc:
        raise FetchError(str(exc.reason)) from exc
    except OSError as exc:
        raise FetchError(str(exc)) from exc


def _get_json(url: str, token: str | None):
    status, body = _request(url, token)
    if status != 200:
        raise FetchError(f"GET {url} -> HTTP {status}")
    try:
        return json.loads(body)
    except ValueError as exc:
        raise FetchError(f"GET {url}: response is not JSON ({exc})") from exc


def _get_bytes(url: str, token: str | None) -> bytes | None:
    status, body = _request(url, token)
    if status == 404:
        return None
    if status != 200:
        raise FetchError(f"GET {url} -> HTTP {status}")
    return body


def github_token() -> str | None:
    return os.environ.get("GITHUB_TOKEN") or None


def _api(repo: str, tail: str) -> str:
    return f"{API}/repos/{repo}/{tail}"


def resolve_commit(repo: str, ref: str | None, token: str | None) -> str:
    """The commit SHA for a ref; ref may be absent, a SHA, tag, or branch.

    Returns "HEAD" for an absent ref, which raw.githubusercontent serves at
    the default branch; an unresolved named ref is an error.
    """
    if ref is None:
        return "HEAD"
    if SHA_RE.fullmatch(ref):
        return ref
    data = _get_json(_api(repo, f"commits/{ref}"), token)
    sha = data.get("sha")
    if not isinstance(sha, str) or not SHA_RE.fullmatch(sha):
        raise FetchError(f"ref {ref!r} of {repo} does not resolve (no commit SHA)")
    return sha


def list_tree(repo: str, sha: str, token: str | None) -> set[str]:
    """All blob paths in the repository at sha; truncation is an error."""
    label = "HEAD" if sha == "HEAD" else sha[:12]
    data = _get_json(f"{_api(repo, 'git/trees')}/{sha}?recursive=1", token)
    if data.get("truncated"):
        raise FetchError(f"tree listing of {repo} at {label} was truncated")
    return {item["path"] for item in data.get("tree", []) if item.get("type") == "blob"}


def fetch_contributors(repo: str, token: str | None) -> str | None:
    """The repository's top contributors, space-comma-joined; None when none."""
    data = _get_json(_api(repo, "contributors?per_page=100"), token)
    logins = [
        c["login"]
        for c in data
        if isinstance(c, dict) and isinstance(c.get("login"), str)
    ][:CONTRIBUTOR_LIMIT]
    return ", ".join(logins) or None


# --- manifest parsing and static checks ---------------------------------------


def parse_manifest(text: str, where: str) -> dict[str, str]:
    """The parsed index.toml; every value must be a plain string."""
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        raise ManifestError(f"{where}: invalid TOML: {exc}") from exc
    if not all(isinstance(v, str) for v in data.values()):
        bad = next(k for k, v in data.items() if not isinstance(v, str))
        raise ManifestError(
            f"{where}: {bad} must be a plain string (got {type(data[bad]).__name__})"
        )
    return data


def check_manifest(where: str, manifest: dict[str, str]) -> list[str]:
    """Static manifest errors (no network): keys, shapes, emptiness, tags."""
    errors: list[str] = []
    unknown = sorted(set(manifest) - set(MANIFEST_KEYS))
    if unknown:
        errors.append(
            f"{where}: unknown manifest key(s) {', '.join(unknown)} "
            f"(allowed: {', '.join(MANIFEST_KEYS)})"
        )
    missing = [k for k in ("repo", "path") if not manifest.get(k, "").strip()]
    if missing:
        errors.append(f"{where}: missing required manifest key(s) {', '.join(missing)}")
    if (repo := manifest.get("repo", "").strip()) and not REPO_RE.fullmatch(repo):
        errors.append(f'{where}: manifest "repo" {repo!r} must be an owner/name pair')
    if path := manifest.get("path", "").strip():
        p = PurePosixPath(path)
        if p.is_absolute() or ".." in p.parts or "." in p.parts or not path.strip("/"):
            errors.append(
                f'{where}: manifest "path" {path!r} must be a repository-relative '
                f"directory like skills/x"
            )
    if tags := manifest.get("tags", "").strip():
        parts = validate.split_tags(tags)
        if not parts:
            errors.append(f"{where}: manifest 'tags' is empty")
        elif len(parts) != len(set(parts)):
            errors.append(f'{where}: manifest "tags" contains duplicates: {parts}')
    return errors


# --- entry derivation ---------------------------------------------------------


def derive_entries(
    section: str, slug: str, manifest: dict[str, str], tree: set[str]
) -> list[RemoteEntry]:
    """Derive entries from the tree: every entry directory under the path.

    The manifest path may itself be an entry; every directory below it that
    holds an entry file is an entry too, published as
    <slug>/<relative-path> at any depth.
    """
    entry_file = validate.ENTRY_KINDS[section]
    root = manifest["path"].strip().strip("/")
    top = "" if root in ("", ".") else f"{root}/"

    common = {
        "repo": manifest["repo"].strip(),
        "ref": manifest.get("ref") or None,
        "path": root,
    }
    entries: list[RemoteEntry] = []
    if f"{top}{entry_file}" in tree:
        entries.append(RemoteEntry(section=section, slug=slug, **common))
    rels = {
        p[len(top) :][: -len(f"/{entry_file}")]
        for p in tree
        if p.startswith(top)
        and p.endswith(f"/{entry_file}")
        and len(p) > len(top) + len(entry_file)
    }
    entries.extend(
        RemoteEntry(section=section, slug=slug, rel=rel, **common)
        for rel in sorted(rels)
    )
    if not entries:
        raise ManifestError(f"path {root!r} holds no {entry_file}")
    return entries


# --- content fetching ---------------------------------------------------------


def fetch_entry_files(
    entry: RemoteEntry, sha: str, tree: set[str], token: str | None
) -> None:
    """Fill entry.files from raw.githubusercontent at the pinned commit.

    Fetches the entry file, README.md (optional for remote entries), and
    profile.png for agents when the tree lists it. Any other file stays
    unfetched — skills bundle freely, agents may not (that check runs on
    the tree listing).
    """
    base = f"{RAW}/{entry.repo}/{sha}/{entry.dir_path}"
    wanted = [validate.ENTRY_KINDS[entry.section], "README.md"]
    if entry.section == "agents" and f"{entry.dir_path}/profile.png" in tree:
        wanted.append("profile.png")
    for name in wanted:
        if body := _get_bytes(f"{base}/{name}", token):
            entry.files[name] = body


def _fetch_all_entries(
    entries: list[RemoteEntry], sha: str, tree: set[str], token: str | None
) -> None:
    """Fetch every entry's files, in parallel over a small thread pool."""
    with ThreadPoolExecutor(max_workers=FETCH_WORKERS) as pool:
        futures = [
            pool.submit(fetch_entry_files, entry, sha, tree, token) for entry in entries
        ]
        for future in futures:
            future.result()


def load_manifest(base: Path, where: str) -> tuple[dict[str, str] | None, list[str]]:
    """Read and parse ext/<section>/<slug>/index.toml from disk.

    Returns (manifest, errors); manifest is None when unreadable. Only
    index.toml may sit in the directory — anything else is an error.
    """
    errors: list[str] = []
    manifest_path = base / MANIFEST_NAME
    if not manifest_path.is_file():
        return None, [f"{manifest_path}: missing required manifest"]
    for other in sorted(base.iterdir()):
        if other.name != MANIFEST_NAME:
            errors.append(f"{other}: only {MANIFEST_NAME} may sit in an ext directory")
    try:
        text = manifest_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{manifest_path}: not valid UTF-8")
        return None, errors
    except OSError as exc:
        errors.append(f"{manifest_path}: cannot read: {exc}")
        return None, errors
    try:
        manifest = parse_manifest(text, where)
    except ManifestError as exc:
        errors.append(str(exc))
        return None, errors
    errors.extend(check_manifest(where, manifest))
    return manifest, errors


def fetch_result(
    entry_root: Path, section: str, slug: str
) -> tuple[RemoteResult | None, list[str]]:
    """Validate-and-fetch one ext manifest from disk to a RemoteResult.

    Returns (result, errors); result is None when the manifest or its fetch
    failed — those errors are fatal. Entries that break the content rules
    are excluded on the result (excluded / exclude_reasons) instead: rules
    stay strict, but upstream drift must not break our deploys.
    """
    where = f"{entry_root.name}/{section}/{slug}"
    base = entry_root / section / slug
    errors = list(validate.check_slug_shape(base, slug))
    manifest, manifest_errors = load_manifest(base, where)
    errors.extend(manifest_errors)

    if (Path(validate.DATA_ROOT) / section / slug).is_dir():
        errors.append(f"{where}: slug {slug!r} collides with the local entry")

    if manifest_errors or manifest is None:
        return None, errors

    try:
        token = github_token()
        repo = manifest["repo"].strip()
        ref = manifest.get("ref", "").strip() or None
        sha = resolve_commit(repo, ref, token)
        tree = list_tree(repo, sha, token)
        entries = derive_entries(section, slug, manifest, tree)
        _fetch_all_entries(entries, sha, tree, token)
        result = RemoteResult(
            slug=slug,
            section=section,
            repo=repo,
            ref=ref,
            path=manifest["path"].strip("/"),
            tags=manifest.get("tags", "").strip() or None,
            entries=entries,
            authors=fetch_contributors(repo, token),
            tree=frozenset(tree),
        )
    except FetchError as exc:
        errors.append(f"{where}: fetch failed: {exc}")
        return None, errors
    except ManifestError as exc:
        errors.append(str(exc))
        return None, errors

    surviving = []
    for entry, entry_errors in validate.check_remote_entry(result):
        if entry_errors:
            result.excluded += 1
            result.exclude_reasons.extend(entry_errors)
        else:
            surviving.append(entry)
    if not surviving:
        errors.extend(
            result.exclude_reasons or [f"{where}: no entry passed the content rules"]
        )
        return None, errors
    result.entries = surviving
    return result, errors
