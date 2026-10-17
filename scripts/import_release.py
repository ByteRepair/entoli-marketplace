#!/usr/bin/env python3
"""Import the latest skills release of ByteRepair/skills into _release/.

The app's presets stopped bundling the fork's skills; the marketplace
serves them instead, generated at build time: build_site.py runs this as
its first step. A release tag is the pruned and reworded tree, so the
import copies each skill directory verbatim and adds only what a local
entry needs here — a `metadata:` block the released frontmatter does not
carry (author `Entoli`, the tag's version, tags `internal`) and a
README.md. skill-creator is skipped: entoli's presets bundle their own
copy, and a marketplace entry for what the app already ships is a shadow,
not a source.

The stage is wiped and refetched every build and never committed; the
build validates it with everything else.
"""

import re
import shutil
import sys
import tarfile
import tempfile
import textwrap
import urllib.request
from pathlib import Path

import validate

ROOT = Path(__file__).resolve().parent.parent
STAGED_ROOT = ROOT / "_release"
SOURCE_REPO = "ByteRepair/skills"
AUTHOR = "Entoli"

# The one skip: entoli still bundles this as a preset under the same name.
SKIP = {"skill-creator"}


def resolve_tag() -> str:
    # The human latest-release URL is a redirect to /tag/<name>; the tag is
    # read off where the redirect lands. One request, no API, no rate limit.
    with urllib.request.urlopen(
        f"https://github.com/{SOURCE_REPO}/releases/latest"
    ) as response:
        landed = response.geturl()
    match = re.search(r"/releases/tag/(v[\d.]+)$", landed)
    if not match:
        raise SystemExit(f"import_release: {landed} does not name a release tag")
    return match.group(1)


def inject_metadata(source: str, version: str) -> str:
    if "\nmetadata:" in source:
        raise SystemExit(
            "import_release: the released frontmatter carries metadata:, "
            "which this import expected to write itself"
        )
    block = f"metadata:\n  author: {AUTHOR}\n  version: {version}\n  tags: internal\n"
    # The metadata lands just ahead of the closing ---, inside the block.
    lines = source.split("\n")
    close = next((i for i, line in enumerate(lines[1:], 1) if line == "---"), None)
    if close is None:
        raise SystemExit("import_release: a released SKILL.md has no frontmatter")
    lines[close:close] = block.splitlines()
    return "\n".join(lines)


def readme(slug: str, description: str, tag: str) -> str:
    # Wrapped to the prose norm; folding a released description to one
    # paragraph also flattens its trailing blank lines.
    return (
        f"# {slug}\n\n"
        + textwrap.fill(" ".join(description.split()), width=80)
        + "\n\n"
        + f"Imported from the skills release {tag}.\n"
    )


def stage_release() -> int:
    """Fetch, stage, count; raises so a failed fetch serves nothing."""
    tag = resolve_tag()
    url = f"https://github.com/{SOURCE_REPO}/archive/refs/tags/{tag}.tar.gz"
    staged = 0
    with tempfile.TemporaryDirectory() as work:
        archive, _ = urllib.request.urlretrieve(url)
        with tarfile.open(archive, "r:gz") as unpacked:
            unpacked.extractall(work, filter="data")
        # The archive root is <repo>-<tag>; finding skills/ under it keeps
        # the import free of the tarball's layout trivia.
        skills_root = next(
            (Path(work) / name) / "skills"
            for name in Path(work).iterdir()
            if (Path(work) / name / "skills").is_dir()
        )
        if STAGED_ROOT.exists():
            shutil.rmtree(STAGED_ROOT)
        for entry_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
            slug = entry_dir.name
            if slug in SKIP:
                continue
            skill_md = (entry_dir / "SKILL.md").read_text("utf-8")
            scalars, _, has_block = validate.parse_frontmatter(skill_md)
            if not has_block:
                raise SystemExit(
                    f"import_release: {slug}'s SKILL.md has no frontmatter"
                )
            out = STAGED_ROOT / "skills" / slug
            shutil.copytree(entry_dir, out)
            (out / "SKILL.md").write_text(
                inject_metadata(skill_md, version=tag[1:]), "utf-8"
            )
            (out / "README.md").write_text(
                readme(slug, scalars.get("description", ""), tag), "utf-8"
            )
            staged += 1
    print(f"import_release: staged {staged} skills from {tag}")
    return staged


def main() -> int:
    stage_release()
    return 0


if __name__ == "__main__":
    sys.exit(main())
