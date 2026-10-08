#!/usr/bin/env python3
"""Validate marketplace entries under data/.

Usage:
  scripts/validate.py                 validate every entry in data/
  scripts/validate.py --changed FILE  validate only entries touched by a diff
  scripts/validate.py --entry data/skills/foo   validate only that entry

--changed expects `git diff --name-status -M` output (plain names from
`--name-only` are also accepted). An entry is validated when any touched
path adds or modifies content in it; deletions alone only validate the
entry if a directory still remains (full removal is allowed, partial
removal fails the missing-file checks).
"""

import argparse
import re
import sys
from pathlib import Path

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

DATA_ROOT = Path("data")
ENTRY_KINDS = {"skills": "SKILL.md", "agents": "PROMPT.md"}
ENTRY_FILES = {
    "skills": ("README.md", "SKILL.md"),
    "agents": ("README.md", "PROMPT.md"),
}
AGENT_ALLOWED = {"README.md", "PROMPT.md", "profile.png"}

# Entoli's frontmatter parser (lib/domain/frontmatter.dart) verbatim: it is
# a strict regex subset of YAML, so validating against full YAML would pass
# files Entoli reads differently.
_SCALAR_RE = re.compile(r"^([A-Za-z0-9_.-]+):[ \t]*(.*)$")
_INDENTED_SCALAR_RE = re.compile(r"^[ \t]+([A-Za-z0-9_.-]+):[ \t]*(.*)$")


def parse_frontmatter(source: str) -> tuple[dict[str, str], dict[str, str], bool]:
    """Port of Entoli's Frontmatter.parse.

    Returns (scalars, metadata, has_block): the top-level keys, the indented
    `metadata:` map, and whether a frontmatter block was found. Values are
    exactly what Entoli reads — entries the port drops (wrong indent, nested
    deeper, interrupted block) are dropped for Entoli too.
    """
    text = source.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, {}, False
    close = text.find("\n---", 3)
    if close < 0:
        return {}, {}, False

    scalars: dict[str, str] = {}
    metadata: dict[str, str] = {}
    in_metadata = False
    metadata_indent: int | None = None
    for line in text[4 : close + 1].split("\n"):
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
    version = metadata.get("version")
    if version is not None and not SEMVER_RE.fullmatch(version):
        errors.append(
            f"{path}: metadata 'version' must be a SemVer string like "
            f"'1.2.0' (got {version!r})"
        )
    tags = metadata.get("tags")
    if tags is not None:
        if tags.startswith("[") and tags.endswith("]"):
            errors.append(
                f'{path}: metadata "tags" must be a comma-separated string, '
                f"not a YAML list (got {tags!r})"
            )
        else:
            parts = [t.strip() for t in tags.split(",") if t.strip()]
            if not parts:
                errors.append(f"{path}: metadata 'tags' is empty")
            if len(parts) != len(set(parts)):
                errors.append(f"{path}: metadata 'tags' contains duplicates: {parts}")
    return errors


def check_entry_frontmatter(path: Path, kind: str, slug: str, text: str) -> list[str]:
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
            if key not in ("description", "metadata"):
                errors.append(
                    f'{path}: unexpected frontmatter key "{key}" (an agent '
                    f"carries only description and metadata)"
                )
        if "name" in scalars:
            errors.append(
                f"{path}: an agent's name is its file name; do not set a "
                f"'name' frontmatter key"
            )

    errors.extend(_check_meta_fields(path, metadata))
    return errors


def check_utf8(path: Path) -> list[str]:
    try:
        path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [f"{path}: not valid UTF-8"]
    except OSError as exc:
        return [f"{path}: cannot read: {exc}"]
    return []


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
    if not magic.startswith(PNG_MAGIC):
        return [f"{path}: not a valid PNG file (bad magic bytes)"]
    return []


def check_agent_extras(base: Path) -> list[str]:
    return [
        f"{p}: file is not part of the agent schema (expected only "
        f"{', '.join(sorted(AGENT_ALLOWED))})"
        for p in sorted(base.iterdir())
        if p.name not in AGENT_ALLOWED
    ]


def validate_section_of(path: Path) -> tuple[str, str] | None:
    """Map a (relative) path under data/ to its (section, slug)."""
    prefix = f"{DATA_ROOT}/"
    if not str(path).startswith(prefix):
        return None
    rest = str(path)[len(prefix) :]
    if "/" not in rest:
        return None  # files at data/<section>/ level are not entries
    section, remainder = rest.split("/", 1)
    if section not in ENTRY_KINDS:
        return None
    return section, remainder.split("/", 1)[0]


def discover_slugs(section: str) -> list[str]:
    root = DATA_ROOT / section
    if not root.is_dir():
        return []
    return sorted(p.name for p in root.iterdir() if p.is_dir())


def validate_entry(section: str, slug: str) -> tuple[list[str], list[str]]:
    base = DATA_ROOT / section / slug
    errors: list[str] = []
    warnings: list[str] = []

    if not SLUG_RE.fullmatch(slug):
        errors.append(f"{base}: slug must match {SLUG_RE.pattern}")
    if not base.is_dir():
        errors.append(f"{base}: entry directory does not exist")
        return errors, warnings

    for name in ENTRY_FILES[section]:
        path = base / name
        if not path.is_file():
            errors.append(f"{path}: missing required file")
        elif name.endswith(".md"):
            errors.extend(check_utf8(path))

    entry_md = base / ENTRY_KINDS[section]
    if entry_md.is_file():
        errors.extend(
            check_entry_frontmatter(
                entry_md, section, slug, entry_md.read_text("utf-8")
            )
        )
    if section == "agents":
        errors.extend(check_profile_png(base))
        warnings.extend(check_agent_extras(base))

    return errors, warnings


def collect_slugs_from_diff(diff_text: str) -> dict[str, set[str]]:
    """Extract slugs to validate from name-status (or name-only) diff lines."""
    touched: dict[str, set[str]] = {}
    kept: dict[str, set[str]] = {}
    for line in diff_text.splitlines():
        parts = line.split("\t")
        if not parts or not parts[0]:
            continue
        if len(parts) == 1:  # name-only output
            status, paths = "M", parts
        else:
            status, paths = parts[0][:1], parts[1:]
        if status == "D":
            mapped = validate_section_of(Path(paths[0]))
            if mapped:
                kept.setdefault(mapped[0], set()).add(mapped[1])
            continue
        mapped = validate_section_of(Path(paths[-1]))
        if mapped:
            touched.setdefault(mapped[0], set()).add(mapped[1])
        if status in ("R", "C") and len(paths) > 1:
            mapped = validate_section_of(Path(paths[0]))
            if mapped:
                kept.setdefault(mapped[0], set()).add(mapped[1])

    # Deletion-only slugs stay unvalidated (full removal) unless a
    # directory still exists (partial removal), which the file checks
    # then reject.
    result: dict[str, set[str]] = {}
    for section in ENTRY_KINDS:
        slugs = set(touched.get(section, set()))
        for slug in kept.get(section, set()):
            if (DATA_ROOT / section / slug).is_dir():
                slugs.add(slug)
        result[section] = slugs
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
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
    args = parser.parse_args()

    sections: dict[str, set[str]] = {}
    if args.changed:
        diff = args.changed.read_text(encoding="utf-8", errors="replace")
        sections = collect_slugs_from_diff(diff)
    elif not args.entry:
        sections = {s: set(discover_slugs(s)) for s in ENTRY_KINDS}
    for target in args.entry:
        mapped = validate_section_of(Path(target))
        if mapped is None:
            print(
                f"error: --entry {target!r} is not data/<section>/<slug>",
                file=sys.stderr,
            )
            return 2
        sections.setdefault(mapped[0], set()).add(mapped[1])

    errors: list[str] = []
    warnings: list[str] = []
    checked = 0
    for section in ENTRY_KINDS:
        for slug in sorted(sections.get(section, set())):
            checked += 1
            entry_errors, entry_warnings = validate_entry(section, slug)
            errors.extend(entry_errors)
            warnings.extend(entry_warnings)

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
