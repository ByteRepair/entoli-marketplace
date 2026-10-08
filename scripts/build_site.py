#!/usr/bin/env python3
"""Build the GitHub Pages site into _site/.

- copies data/skills -> _site/skills and data/agents -> _site/agents
- generates _site/skills/index.json and _site/agents/index.json from each
  entry's SKILL.md / PROMPT.md frontmatter, keyed by slug

The build validates everything first (same rules as CI) and refuses to
produce output for invalid data.
"""

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import validate

SITE = ROOT / "_site"
TAGS_DELIM = ","


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
        meta["tags"] = [t.strip() for t in tags.split(TAGS_DELIM) if t.strip()]
    return meta


def build() -> int:
    errors = []
    meta_all = {}
    for section in validate.ENTRY_KINDS:
        meta_all[section] = {}
        for slug in validate.discover_slugs(section):
            entry_errors, _ = validate.validate_entry(section, slug)
            if entry_errors:
                errors.extend(entry_errors)
                continue
            meta_all[section][slug] = entry_meta(section, slug)

    if errors:
        print(f"build failed: {len(errors)} validation error(s):")
        for error in errors:
            print(f"  {error}")
        return 1

    if SITE.exists():
        shutil.rmtree(SITE)
    for section in validate.ENTRY_KINDS:
        (SITE / section).mkdir(parents=True)
        for slug in meta_all[section]:
            src = validate.DATA_ROOT / section / slug
            dst = SITE / section / slug
            if src.is_dir():
                shutil.copytree(src, dst)
        (SITE / section / "index.json").write_text(
            json.dumps(meta_all[section], indent=2, ensure_ascii=False) + "\n",
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
