#!/usr/bin/env python3
"""Collections: the groups the app shows a section's entries under.

Two sources, one record shape. An ext manifest publishing <slug>/<sub>
entries is a collection of those entries (its name and summary from the
manifest). `collections/<section>.toml` names the rest, any entry of the
section by its index key:

    [design]
    name = "Design"                 required, 1-64 chars
    summary = "..."                 optional, 1-160 chars
    members = ["canvas-design"]     required, index keys of the section

An entry sits in one collection at most, and a manifest's own entries are
its collection's alone. The build writes the merged records to
_site/<section>/collections.json as {slug: {name, summary, members}}.

Run on its own it checks the files against what it can see offline: the
data/ and _release/ slugs and the ext manifests' own slugs.
"""

import sys
import tomllib
from pathlib import Path

import validate

ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS_ROOT = ROOT / "collections"
NAME_MAX = 64
SUMMARY_MAX = 160
KEYS = ("name", "summary", "members")


def load(section: str, root: Path = COLLECTIONS_ROOT) -> tuple[dict, list[str]]:
    """The declared collections of [section], or none where there is no file."""
    path = root / f"{section}.toml"
    if not path.exists():
        return {}, []
    where = f"collections/{section}.toml"
    try:
        tables = tomllib.loads(path.read_text("utf-8"))
    except tomllib.TOMLDecodeError as e:
        return {}, [f"{where}: {e}"]
    records: dict[str, dict] = {}
    errors: list[str] = []
    for slug, table in tables.items():
        problems = check_table(f"{where} [{slug}]", slug, table)
        errors.extend(problems)
        if not problems:
            records[slug] = {
                "name": table["name"].strip(),
                "summary": table.get("summary", "").strip(),
                "members": list(table["members"]),
            }
    return records, errors


def check_table(where: str, slug: str, table) -> list[str]:
    """Shape errors in one declared collection."""
    if not isinstance(table, dict):
        return [f"{where}: must be a table"]
    errors = []
    if not validate.SLUG_RE.fullmatch(slug):
        errors.append(f"{where}: the slug must be lowercase-kebab")
    if unknown := sorted(set(table) - set(KEYS)):
        errors.append(f"{where}: unknown key(s) {', '.join(unknown)}")
    name = table.get("name")
    if not isinstance(name, str) or not 1 <= len(name.strip()) <= NAME_MAX:
        errors.append(f'{where}: "name" must be 1-{NAME_MAX} characters')
    if "summary" in table:
        summary = table["summary"]
        if not isinstance(summary, str) or not 1 <= len(summary.strip()) <= SUMMARY_MAX:
            errors.append(f'{where}: "summary" must be 1-{SUMMARY_MAX} characters')
    members = table.get("members")
    if (
        not isinstance(members, list)
        or not members
        or not all(isinstance(m, str) for m in members)
    ):
        errors.append(f'{where}: "members" must be a list of entry keys')
    elif len(members) != len(set(members)):
        errors.append(f'{where}: "members" lists an entry twice')
    return errors


def merge(
    section: str, declared: dict, manifests: dict, keys: set[str]
) -> tuple[dict, list[str]]:
    """The manifests' collections and the declared ones, as one record set.

    [keys] are the section index's keys. A declared member must be one of
    them and in no other collection, a manifest's entries included.
    """
    errors = []
    owner = {
        key: slug for slug, record in manifests.items() for key in record["members"]
    }
    for slug, record in declared.items():
        where = f"collections/{section}.toml [{slug}]"
        if slug in manifests:
            errors.append(f"{where}: ext/{section}/{slug} is already a collection")
        for member in record["members"]:
            if member not in keys:
                errors.append(f"{where}: {member!r} is no entry of {section}")
            elif member in owner:
                errors.append(f"{where}: {member!r} is already in {owner[member]!r}")
            else:
                owner[member] = slug
    return {**manifests, **declared}, errors


def main() -> int:
    errors = []
    for section in validate.ENTRY_KINDS:
        declared, problems = load(section)
        errors.extend(problems)
        keys = {
            slug
            for root in (validate.DATA_ROOT, ROOT / "_release", validate.EXT_ROOT)
            for slug in validate.discover_slugs(section, root)
        }
        # A manifest's sub-entries are unknown offline; the build checks
        # those keys against the fetched index.
        _, problems = merge(section, declared, {}, keys)
        errors.extend(problems)
    for error in errors:
        print(f"  {error}")
    if errors:
        print(f"collections: {len(errors)} error(s)")
        return 1
    print("collections: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
