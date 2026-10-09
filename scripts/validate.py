#!/usr/bin/env python3
"""Quick standalone entry checks under data/ (and ext/ with network).

Usage:
  scripts/validate.py                 validate every entry in data/ + ext/
  scripts/validate.py --changed FILE  validate only entries touched by a diff
  scripts/validate.py --entry data/skills/foo   validate only that entry
  scripts/validate.py --data-root DIR           validate a different tree

--changed expects `git diff --name-status -M` output (plain names from
`--name-only` are also accepted). An entry is validated when any touched
path adds or modifies content in it; deletions alone only validate the
entry if a directory still remains (full removal is allowed, partial
removal fails the missing-file checks).

Entries under ext/<section>/<slug>/ are remote: their index.toml points at
content in another GitHub repository (see fetch_remote.py), which this
script fetches and checks with the same frontmatter rules as data/
entries. That needs network access, so only this tier validates ext/ —
entoli's Dart CLI has none. The ext root sits beside the data root
(data/ -> ext/; a non-default --data-root looks for ext/ beside it).

Checks are file presence, slug shape, UTF-8, PNG magic, and a Python
mirror of entoli's frontmatter parser and Agent Skills spec rules — same
two tiers: strict YAML (PyYAML; system-installed locally and on CI
runners) then the legacy regex fallback. CI's source of truth is entoli's
own Dart CLI (tool/validate_marketplace.dart in the entoli repo), which
tool/frontmatter_diff_test.dart pins both tiers to agree with; this
script is the quick local pass with no Dart toolchain required.
"""

import argparse
import re
import sys
from pathlib import Path, PurePosixPath

# The Agent Skills spec keys Entoli's validator enforces on SKILL.md
# frontmatter (lib/data/prompts/skill_validate.dart). Constants match Entoli
# so CI fails exactly the skills Entoli would refuse.
SPEC_KEYS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
NAME_MAX = 64
DESCRIPTION_MAX = 1024
COMPATIBILITY_MAX = 500

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

ENTRY_ROOTS = ("data", "ext")
ROOTS: dict[str, Path] = {"data": Path("data"), "ext": Path("ext")}
DATA_ROOT = ROOTS["data"]
EXT_ROOT = ROOTS["ext"]
SOURCES_ROOT = Path("sources")
ENTRY_KINDS = {"skills": "SKILL.md", "agents": "PROMPT.md"}
ENTRY_FILES = {
    "skills": ("README.md", "SKILL.md"),
    "agents": ("README.md", "PROMPT.md"),
}
AGENT_ALLOWED = {"README.md", "PROMPT.md", "profile.png"}
not_part_of_agent_schema = (
    f"file is not part of the agent schema (expected only "
    f"{', '.join(sorted(AGENT_ALLOWED))})"
)

# Entoli's frontmatter parser (lib/domain/frontmatter.dart) as two tiers:
# strict YAML first (the `yaml` package there; PyYAML here, which entoli's
# grammar matches for the shapes entries write), then the legacy regex
# subset as fallback for content that is not valid YAML (unquoted ": " in
# values). Ports mirror entoli tier for tier, and
# tool/frontmatter_diff_test.dart keeps them in lockstep.
import yaml  # PyYAML; system-installed locally and on GitHub runners

_SCALAR_RE = re.compile(r"^([A-Za-z0-9_.-]+):[ \t]*(.*)$")
_INDENTED_SCALAR_RE = re.compile(r"^[ \t]+([A-Za-z0-9_.-]+):[ \t]*(.*)$")


def _scalar_string(value) -> str:
    """Mirror entoli's _scalarString: resolve YAML scalars the way the yaml
    package delivers them (quotes gone, booleans/numbers at YAML spelling)."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(_scalar_string(v) for v in value) + "]"
    if isinstance(value, dict):
        return (
            "{" + ", ".join(f"{k}: {_scalar_string(v)}" for k, v in value.items()) + "}"
        )
    return str(value)


def _collect_yaml_map(yaml_map: dict) -> tuple[dict[str, str], dict[str, str]]:
    """The scalars and metadata map a parsed YAML mapping yields, mirroring
    entoli's map walk: nested non-metadata blocks dropped, metadata values
    stringified (nested maps inside metadata dropped)."""
    scalars: dict[str, str] = {}
    metadata: dict[str, str] = {}
    for key, value in yaml_map.items():
        if not isinstance(key, str):
            continue
        if key == "metadata" and isinstance(value, dict):
            for mkey, mvalue in value.items():
                if isinstance(mkey, str) and not isinstance(mvalue, dict):
                    metadata[mkey] = _scalar_string(mvalue)
            continue
        if value is None or isinstance(value, (dict, list)):
            continue
        scalars[key] = _scalar_string(value)
    return scalars, metadata


def parse_frontmatter(source: str) -> tuple[dict[str, str], dict[str, str], bool]:
    """Port of Entoli's Frontmatter.parse (YAML first, legacy fallback).

    Returns (scalars, metadata, has_block): the top-level keys, the `metadata:`
    map, and whether a frontmatter block was found. Values are exactly what
    Entoli reads — shapes the strict tier refuses and the legacy tier drops
    are dropped for Entoli too.
    """
    text = source.replace("\r\n", "\n")
    if not text.startswith("---\n") and text != "---":
        return {}, {}, False
    close = text.find("\n---", 3)
    if close < 0:
        return {}, {}, False

    block = text[4:close]
    lines = block.split("\n")

    # Strict tier: everything the yaml grammar accepts (block scalars,
    # comments, quoting).
    try:
        parsed = yaml.safe_load(block)
    except yaml.YAMLError:
        parsed = "not a mapping"
    if isinstance(parsed, dict):
        scalars, metadata = _collect_yaml_map(parsed)
        return scalars, metadata, True

    # Strict retry for tab-indented blocks: tabs are legal YAML content but
    # not legal indentation, so the block indented with tabs the legacy
    # parser read becomes space-indented for the strict try.
    if "\t" in block:
        try:
            parsed = yaml.safe_load(block.replace(_TAB_INDENT_RE, "  "))
        except yaml.YAMLError:
            parsed = "not a mapping"
        if isinstance(parsed, dict):
            scalars, metadata = _collect_yaml_map(parsed)
            return scalars, metadata, True

    # Legacy tier: the verbatim regex subset parse of the whole block.
    scalars, metadata = {}, {}
    in_metadata = False
    metadata_indent: int | None = None
    for line in lines:
        match = _SCALAR_RE.match(line)
        if match is None:
            nested = _INDENTED_SCALAR_RE.match(line)
            if in_metadata and nested is not None:
                indent = len(line) - len(line.lstrip())
                if metadata_indent is None:
                    metadata_indent = indent
                value = nested.group(2).strip()
                if indent == metadata_indent and value:
                    metadata[nested.group(1)] = _unquote(value)
            continue
        key, value = match.group(1), match.group(2)
        if not value:
            in_metadata = key == "metadata"
            continue
        in_metadata = False
        if key == "metadata":
            continue
        scalars[key] = _unquote(value.strip())
    return scalars, metadata, True


_SCALAR_RE = re.compile(r"^([A-Za-z0-9_.-]+):[ \t]*(.*)$")
_INDENTED_SCALAR_RE = re.compile(r"^[ \t]+([A-Za-z0-9_.-]+):[ \t]*(.*)$")
_TAB_INDENT_RE = re.compile(r"^\t+", re.MULTILINE)


def split_tags(tags: str) -> list[str]:
    """The list a `tags:` value publishes: comma-separated, trimmed."""
    return [t.strip() for t in tags.split(",") if t.strip()]


def _unquote(value: str) -> str:
    if len(value) < 2:
        return value
    first = value[0]
    if (first == '"' or first == "'") and value.endswith(first):
        return value[1:-1]
    return value


def _name_problems(path: Path, name: str) -> list[str]:
    problems = []
    if len(name) > NAME_MAX:
        problems.append(f"{path}: name is {len(name)} characters (max {NAME_MAX})")
    elif not SLUG_RE.fullmatch(name):
        problems.append(
            f'{path}: name "{name}" is not lowercase letters, digits and '
            f"hyphens with no doubled or leading/trailing hyphen"
        )
    return problems


def _check_meta_fields(path: Path, metadata: dict[str, str]) -> list[str]:
    """Marketplace fields riding in `metadata:` — what Entoli's parser kept."""
    errors = []
    author = metadata.get("author")
    if author is None or not author.strip():
        errors.append(
            f"{path}: metadata carries no usable 'author' (indented "
            f"author: <name> under metadata:)"
        )
    errors.extend(_check_version_and_tags(path, metadata))
    return errors


def _check_version_and_tags(path: Path, metadata: dict[str, str]) -> list[str]:
    """The metadata parts that apply to remote entries too (no author rule)."""
    errors = []
    version = metadata.get("version")
    if version is not None and not SEMVER_RE.fullmatch(version):
        errors.append(
            f"{path}: metadata 'version' must be a SemVer string like "
            f"'1.2.0' (got {version!r})"
        )
    tags = metadata.get("tags")
    if tags is not None:
        stripped = tags.strip()
        if stripped.startswith("[") or stripped.endswith("]"):
            errors.append(
                f'{path}: metadata "tags" must be a comma-separated string, '
                f"not a YAML list (got {tags!r})"
            )
        else:
            parts = split_tags(tags)
            if len(parts) != len(set(parts)):
                errors.append(f"{path}: metadata 'tags' contains duplicates: {parts}")
    return errors


def check_entry_frontmatter(
    path: Path, kind: str, slug: str, text: str, require_author: bool = True
) -> list[str]:
    """The frontmatter rules both tiers enforce.

    Remote entries pass require_author=False: their authors are the source
    repository's contributors (fetch_remote), not frontmatter metadata.
    """
    errors = []
    scalars, metadata, has_block = parse_frontmatter(text)
    if not has_block:
        return [f"{path}: no frontmatter block (the file must start with '---')"]

    description = scalars.get("description")
    if description is None or not description.strip():
        errors.append(f"{path}: no description in the frontmatter")

    if kind == "skills":
        for key in scalars:
            if key not in SPEC_KEYS:
                errors.append(
                    f'{path}: unknown frontmatter key "{key}" '
                    f"(allowed: {', '.join(sorted(SPEC_KEYS))})"
                )
        name = scalars.get("name")
        if name is None:
            errors.append(f"{path}: missing 'name' in the frontmatter")
        elif name != slug:
            errors.append(
                f'{path}: frontmatter name "{name}" does not match the folder "{slug}"'
            )
        else:
            errors.extend(_name_problems(path, name))
        if description is not None and len(description) > DESCRIPTION_MAX:
            errors.append(
                f"{path}: description is {len(description)} characters "
                f"(max {DESCRIPTION_MAX})"
            )
        compatibility = scalars.get("compatibility")
        if compatibility is not None and len(compatibility) > COMPATIBILITY_MAX:
            errors.append(
                f"{path}: compatibility is {len(compatibility)} characters "
                f"(max {COMPATIBILITY_MAX})"
            )
    else:
        for key in scalars:
            if key in ("description", "metadata"):
                continue
            if key == "name":
                errors.append(
                    f"{path}: an agent's name is its file name; do not set a "
                    f"'name' frontmatter key"
                )
            else:
                errors.append(
                    f'{path}: unexpected frontmatter key "{key}" (an agent '
                    f"carries only description and metadata)"
                )

    if require_author:
        errors.extend(_check_meta_fields(path, metadata))
    else:
        # Marketplace-only fields stay the source's choice; version is still
        # SemVer-checked when present, tags are still comma-separated.
        errors.extend(_check_version_and_tags(path, metadata))
    return errors


def check_profile_png(base: Path) -> list[str]:
    path = base / "profile.png"
    if not path.exists():
        return []
    if not path.is_file():
        return [f"{path}: expected a regular file"]
    try:
        with path.open("rb") as f:
            magic = f.read(len(PNG_MAGIC))
    except OSError as exc:
        return [f"{path}: cannot read: {exc}"]
    return _png_problems(path, magic)


def _png_problems(label, head: bytes) -> list[str]:
    """The PNG-magic errors for a file's leading bytes (empty when a PNG)."""
    if head.startswith(PNG_MAGIC):
        return []
    return [f"{label}: not a valid PNG file (bad magic bytes)"]


def check_agent_extras(base: Path) -> list[str]:
    """A stray file in an agent directory is what the Dart CLI refuses, so
    it is an error here too — never a warning (tiers must not disagree)."""
    return [
        f"{p}: {not_part_of_agent_schema}"
        for p in sorted(base.iterdir())
        if p.name not in AGENT_ALLOWED
    ]


def validate_section_of(path: Path) -> tuple[str, str] | None:
    """Map a (relative) path under a root to its (section, slug).

    Roots are the entry trees: data/ (local entries) and ext/ (remote
    entry manifests). Files at <root>/<section>/ level are not entries.
    """
    for root in ENTRY_ROOTS:
        prefix = f"{root}/"
        if not str(path).startswith(prefix):
            continue
        rest = str(path)[len(prefix) :]
        if "/" not in rest:
            return None  # files at <root>/<section>/ level are not entries
        section, remainder = rest.split("/", 1)
        if section not in ENTRY_KINDS:
            return None
        return section, remainder.split("/", 1)[0]
    return None


def discover_slugs(section: str, root: Path) -> list[str]:
    root = root / section
    if not root.is_dir():
        return []
    return sorted(p.name for p in root.iterdir() if p.is_dir())


def check_slug_shape(base: Path, slug: str) -> list[str]:
    if not SLUG_RE.fullmatch(slug):
        return [f"{base}: slug must match {SLUG_RE.pattern}"]
    return []


def validate_entry(section: str, slug: str) -> list[str]:
    """Validate a local entry directory under the data root."""
    base = DATA_ROOT / section / slug
    errors: list[str] = []
    errors.extend(check_slug_shape(base, slug))

    if not base.is_dir():
        errors.append(f"{base}: entry directory does not exist")
        return errors

    for name in ENTRY_FILES[section]:
        path = base / name
        if not path.is_file():
            errors.append(f"{path}: missing required file")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{path}: not valid UTF-8")
            text = None
        except OSError as exc:
            errors.append(f"{path}: cannot read: {exc}")
            text = None
        if name == ENTRY_KINDS[section] and text is not None:
            errors.extend(check_entry_frontmatter(path, section, slug, text))
    if section == "agents":
        errors.extend(check_profile_png(base))
        errors.extend(check_agent_extras(base))

    return errors


def check_remote_entry(result) -> list[tuple]:
    """The fetched remote content, under the same rules as data/ entries.

    Returns (entry, errors) pairs: an entry with errors breaks the content
    rules and is excluded from the marketplace by the caller.
    """
    checked: list[tuple] = []
    sorted_tree = sorted(result.tree)
    for entry in result.entries:
        entry_file = ENTRY_KINDS[entry.section]
        errors: list[str] = []
        raw = entry.files.get(entry_file)
        if raw is None:
            errors.append(
                f"{entry.repo}/{entry.dir_path}: entry file {entry_file} "
                f"was not fetched"
            )
            checked.append((entry, errors))
            continue
        text = raw.decode("utf-8", errors="replace")
        # A virtual path under sources/ — errors read like a tree of the
        # remote content, one directory per published entry.
        virtual = (
            SOURCES_ROOT / entry.section / entry.key.replace("/", "_") / entry_file
        )
        errors.extend(
            check_entry_frontmatter(
                virtual, entry.section, entry.name_slug, text, require_author=False
            )
        )
        if readme := entry.files.get("README.md"):
            try:
                readme.decode("utf-8")
            except UnicodeDecodeError:
                errors.append(f"{virtual.parent / 'README.md'}: not valid UTF-8")

        if entry.section == "agents":
            if (png := entry.files.get("profile.png")) is not None:
                errors.extend(_png_problems(virtual.parent / "profile.png", png))
            # Skill directories bundle freely; an agent may carry only the
            # schema files, checked against the remote tree listing.
            prefix = f"{entry.dir_path}/"
            for p in sorted_tree:
                if not p.startswith(prefix):
                    continue
                top = PurePosixPath(p[len(prefix) :]).parts[0]
                if top not in AGENT_ALLOWED:
                    errors.append(f"{entry.repo}/{p}: {not_part_of_agent_schema}")
        checked.append((entry, errors))
    return checked


def validate_ext_entry(section: str, slug: str) -> tuple:
    """Validate a remote entry manifest; fetches from GitHub (network).

    Returns (result|None, errors): result is the fetched RemoteResult (its
    `excluded` count and `exclude_reasons` carry per-entry exclusions),
    None when the manifest itself failed — those errors are fatal.
    """
    import fetch_remote

    return fetch_remote.fetch_result(EXT_ROOT, section, slug)


def collect_slugs_from_diff(diff_text: str) -> dict[tuple[str, str], set[str]]:
    """Extract touched slugs per (root, section) from diff lines."""
    touched: dict[tuple[str, str], set[str]] = {}
    kept: dict[tuple[str, str], set[str]] = {}
    for line in diff_text.splitlines():
        parts = line.split("\t")
        if not parts or not parts[0]:
            continue
        if len(parts) == 1:  # name-only output
            status, paths = "M", parts
        else:
            status, paths = parts[0][:1], parts[1:]
        if (mapped := validate_section_of(Path(paths[-1]))) and status != "D":
            touched.setdefault((paths[-1].split("/", 1)[0], mapped[0]), set()).add(
                mapped[1]
            )
        if (status == "D" or (status in ("R", "C") and len(paths) > 1)) and (
            mapped := validate_section_of(Path(paths[0]))
        ):
            kept.setdefault((paths[0].split("/", 1)[0], mapped[0]), set()).add(
                mapped[1]
            )

    # Deletion-only slugs stay unvalidated (full removal) unless a
    # directory still exists (partial removal), which the file checks
    # then reject. The tree mapping handles both root-level touches
    # (e.g. a stray data/skills/foo.md file) and root-level deletes of
    # entry trees, which keep nothing.
    result: dict[tuple[str, str], set[str]] = {}
    for root in ENTRY_ROOTS:
        base = ROOTS[root]
        for section in ENTRY_KINDS:
            slugs = set(touched.get((root, section), set()))
            for slug in kept.get((root, section), set()):
                if (base / section / slug).is_dir():
                    slugs.add(slug)
            result[(root, section)] = slugs
    return result


def main_with(argv: list[str]) -> int:
    """main() over an explicit argv (test hook)."""
    return _validate(argv[1:])


def main() -> int:
    return _validate(sys.argv[1:])


def _validate(argv: list[str]) -> int:
    global SOURCES_ROOT, DATA_ROOT, EXT_ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-root",
        type=Path,
        default=DATA_ROOT,
        metavar="DIR",
        help=(
            "the tree holding <data-root>/{skills,agents} (default data/); "
            "ext/ and sources/ live beside it"
        ),
    )
    parser.add_argument(
        "--changed",
        type=Path,
        metavar="FILE",
        help="git diff --name-status output; validate only touched entries",
    )
    parser.add_argument(
        "--entry",
        action="append",
        default=[],
        metavar="DATA/SECTION/SLUG",
        help="validate a specific entry (repeatable)",
    )
    args = parser.parse_args(argv)
    DATA_ROOT = args.data_root
    ROOTS["data"] = args.data_root
    EXT_ROOT = args.data_root.parent / "ext"
    ROOTS["ext"] = EXT_ROOT
    SOURCES_ROOT = args.data_root.parent / "sources"

    sections: dict[tuple[str, str], set[str]] = {}
    if args.changed:
        diff = args.changed.read_text(encoding="utf-8", errors="replace")
        sections = collect_slugs_from_diff(diff)
    elif not args.entry:
        sections = {
            (r, s): set(discover_slugs(s, ROOTS[r]))
            for r in ENTRY_ROOTS
            for s in ENTRY_KINDS
        }
    for target in args.entry:
        mapped = validate_section_of(Path(target))
        if mapped is None:
            print(
                f"error: --entry {target!r} is not [data|ext]/<section>/<slug>",
                file=sys.stderr,
            )
            return 2
        sections.setdefault((Path(target).parts[0], mapped[0]), set()).add(mapped[1])

    errors: list[str] = []
    warnings: list[str] = []
    checked = 0
    for (root, section), slugs in sorted(sections.items()):
        for slug in sorted(slugs):
            checked += 1
            if root == "ext":
                result, ext_errors = validate_ext_entry(section, slug)
                errors.extend(ext_errors)
                if result is not None:
                    warnings.extend(result.exclusion_warnings(f"ext/{section}/{slug}"))
            else:
                errors.extend(validate_entry(section, slug))

    if warnings:
        print("warnings (not fatal):")
        for warning in warnings:
            print(f"  {warning}")
    if errors:
        print(f"validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"  {error}")
        return 1
    print(f"OK: {checked} entr{'y' if checked == 1 else 'ies'} validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
