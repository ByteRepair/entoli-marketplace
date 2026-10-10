#!/usr/bin/env python3
"""Build the GitHub Pages site into _site/.

- copies data/skills -> _site/skills and data/agents -> _site/agents
- zips each skill into _site/skills/<slug>.skill — the one file an entoli
  client fetches to install the whole directory (SKILL.md and the files
  beside it); parsed by lib/data/prompts/skill_import.dart, which strips the
  top-level folder
- generates _site/skills/index.json and _site/agents/index.json from each
  entry's SKILL.md / PROMPT.md frontmatter, keyed by slug
- resolves ext/<section>/<slug>/index.toml manifests (see fetch_remote.py):
  remote entries join the section index.json — name and description from
  the fetched frontmatter, authors from the source repo's contributors,
  version from the frontmatter, tags = "external", the manifest's tags,
  then the frontmatter's own — and each entry's source location (with its
  full file list, per entry) lands in _site/ext/<section>/index.json.
  Remote content is not mirrored: clients follow the location data.

The build validates everything first (same rules as CI) and refuses to
produce output for invalid data.
"""

import json
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_remote
import validate

SITE = ROOT / "_site"
EXTERNAL_TAG = "external"


def entry_meta(section: str, slug: str) -> dict:
    base = validate.DATA_ROOT / section / slug
    source = (base / validate.ENTRY_KINDS[section]).read_text("utf-8")
    scalars, metadata, _ = validate.parse_frontmatter(source)
    meta = {
        "name": scalars.get("name") or slug,
        "description": scalars.get("description", ""),
        "author": metadata.get("author", ""),
    }
    if version := metadata.get("version"):
        meta["version"] = version
    if tags := metadata.get("tags"):
        meta["tags"] = validate.split_tags(tags)
    return meta


def ext_meta(entry, result) -> dict:
    """One remote entry's index record, in the same shape as a local one."""
    scalars, metadata, _ = validate.parse_frontmatter(
        entry.files[validate.ENTRY_KINDS[entry.section]].decode(
            "utf-8", errors="replace"
        )
    )
    tags = [
        EXTERNAL_TAG,
        *validate.split_tags(result.tags or ""),
        *validate.split_tags(metadata.get("tags", "")),
    ]
    meta = {
        "name": scalars.get("name") or entry.key,
        "description": scalars.get("description", "")[: validate.DESCRIPTION_MAX],
        "author": result.authors or "",
    }
    if version := metadata.get("version"):
        meta["version"] = version
    if tags:
        meta["tags"] = list(dict.fromkeys(tags))
    return meta


def ext_location(result, entry) -> dict:
    """One remote entry's location record in _site/ext/<section>/.

    Clients fetch an entry's files straight from its source repository, so the
    record carries the whole entry directory — its path in the repository and
    every blob under it — resolved by this build rather than derived by the
        client; with the file list a client needs no listings or API calls.
    """
    prefix = f"{entry.dir_path}/"
    location = {
        "repo": result.repo,
        "dir": entry.dir_path,
        "files": [
            path[len(prefix) :]
            for path in sorted(result.tree)
            if path.startswith(prefix)
        ],
    }
    if result.ref:
        location["ref"] = result.ref
    return location


def package_skill(src: Path, dst: Path) -> None:
    """Zip [src] (a skill directory) into [dst] as a `.skill`.

    Entries sit under the slug as one top-level folder, the layout a zip of a
    directory naturally has; entoli's parser takes the shallowest SKILL.md as
    the root and strips the prefix, so the folder name is not load-bearing.
    """
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(src.rglob("*")):
            if path.is_file():
                archive.write(path, arcname=f"{src.name}/{path.relative_to(src)}")


def build() -> int:
    errors = []
    warnings: list[str] = []
    meta_all = {}
    local_slugs: dict[str, list[str]] = {}
    locations: dict[str, dict[str, dict]] = {}

    for section in validate.ENTRY_KINDS:
        meta_all[section] = {}
        local_slugs[section] = []
        for slug in validate.discover_slugs(section, validate.DATA_ROOT):
            entry_errors = validate.validate_entry(section, slug)
            if entry_errors:
                errors.extend(entry_errors)
                continue
            meta_all[section][slug] = entry_meta(section, slug)
            local_slugs[section].append(slug)

        locations[section] = {}
        for slug in validate.discover_slugs(section, validate.EXT_ROOT):
            result, ext_errors = fetch_remote.fetch_result(
                validate.EXT_ROOT, section, slug
            )
            if ext_errors:
                errors.extend(ext_errors)
            if result is None:
                continue
            warnings.extend(result.exclusion_warnings(f"ext/{section}/{slug}"))
            for entry in result.entries:
                meta_all[section][entry.key] = ext_meta(entry, result)
                locations[section][entry.key] = ext_location(result, entry)

    if errors:
        print(f"build failed: {len(errors)} validation error(s):")
        for error in errors:
            print(f"  {error}")
        return 1
    if warnings:
        print("warnings (not fatal):")
        for warning in warnings:
            print(f"  {warning}")

    if SITE.exists():
        shutil.rmtree(SITE)
    for section in validate.ENTRY_KINDS:
        # The section index exists even when the section is empty; the
        # directory must be there before any entry copy or index write.
        (SITE / section).mkdir(parents=True, exist_ok=True)
        for slug in local_slugs[section]:
            src = validate.DATA_ROOT / section / slug
            shutil.copytree(src, SITE / section / slug)
            if section == "skills":
                package_skill(src, SITE / section / f"{slug}.skill")
        (SITE / section / "index.json").write_text(
            json.dumps(meta_all[section], indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    for section in validate.ENTRY_KINDS:
        (SITE / "ext" / section).mkdir(parents=True)
        (SITE / "ext" / section / "index.json").write_text(
            json.dumps(locations[section], indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    total = sum(len(v) for v in meta_all.values())
    print(
        f"built _site/ with {total} entries "
        f"({len(meta_all['skills'])} skills, {len(meta_all['agents'])} agents)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(build())
