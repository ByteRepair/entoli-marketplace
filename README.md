# entoli-marketplace

This repository contains the content served by the entoli marketplace: skills
and agents for entoli clients to discover and install.

Everything under `data/` is published to GitHub Pages (see
[Publishing](#publishing)). All content is licensed AGPLv3 (see
[LICENSE](LICENSE)); the AGPLv3 grant covers every entry, so entries carry no
license field of their own.

## Layout

```text
data/
  skills/
    <slug>/
      SKILL.md      required: skill definition with metadata frontmatter
      README.md     required: long description for the marketplace page
      ...           optional: any other files/directories the skill needs
  agents/
    <slug>/
      PROMPT.md     required: agent prompt with metadata frontmatter
      README.md     required: long description for the marketplace page
      profile.png   optional: agent avatar (PNG)
```

The body of `SKILL.md` holds the instructions entoli loads; the body of
`PROMPT.md` holds the system prompt the agent runs under. Reference bundled
files from the body with relative paths; `references/`, `scripts/`, and
`assets/` are the conventional directories. `profile.png` is served next to the
prompt, where entoli looks for an agent's picture.

## Slugs

The directory name under `data/skills/` or `data/agents/` is the entry's slug.
It must be lowercase kebab-case:

```regex
^[a-z0-9]+(-[a-z0-9]+)*$
```

Examples: `code-review`, `release-notes`, `py2`. The slug is the entry's
identity in URLs and in `index.json`.

## Frontmatter

`SKILL.md` and `PROMPT.md` open with YAML frontmatter holding the metadata both
entoli and the marketplace read. Skills follow the Agent Skills spec (entoli
enforces it: unknown top-level keys are refused), so marketplace-only fields
live under `metadata:`, the spec's extension point, which entoli reads as a
string-to-string map.

```yaml
---
name: code-review
description: >-
  Reviews diffs for bugs and style problems. Use this when the user asks to
  review a diff or a pull request.
metadata:
  author: Ada Lovelace
  version: 1.2.0
  tags: code-quality, review
---
```

| Field         | Where    | Required | Rules                              |
| ------------- | -------- | -------- | ---------------------------------- |
| `name`        | SKILL.md | skills   | matches the slug                   |
| `description` | scalars  | yes      | non-empty; <=1024 chars for skills |
| `author`      | metadata | yes      | non-empty string                   |
| `version`     | metadata | no       | valid SemVer string                |
| `tags`        | metadata | no       | comma-separated; unique            |

Rules that follow from entoli's parser (a strict regex subset of YAML):

- The file must start with `---\n`; the closing `---` must sit on its own line.
- `metadata:` entries are single `key: value` lines indented under it at one
  uniform indent. Keep `metadata:` as the last frontmatter entry: entoli's
  parser drops a scalar key that follows the nested block.
- `tags` is a comma-separated plain string, not a YAML list; entoli reads
  `[a, b]` as the literal string `[a, b]`.

Skills additionally: top-level keys are exactly the spec's (`name`,
`description`, `license`, `compatibility`, `metadata`, `allowed-tools`), the
`name` scalar is 1 to 64 lowercase-kebab characters and matches the folder, and
`compatibility` is at most 500 characters when present.

Agents: only `description` and `metadata` at the top level. The agent's name is
its file name, so no `name` key is used.

## Publishing

`data/skills/` maps to `/skills` and `data/agents/` maps to `/agents` on GitHub
Pages, with file paths preserved: `data/skills/code-review/SKILL.md` is served
at `/skills/code-review/SKILL.md`.

### index.json

For client discoverability, each section also publishes an `index.json` derived
from the entries' frontmatter, keyed by slug:

```json
{
  "code-review": {
    "name": "...",
    "description": "...",
    "author": "...",
    "version": "...",
    "tags": ["..."]
  }
}
```

Values are taken verbatim from the frontmatter fields described above. `version`
and `tags` are present only when set; `tags` becomes a real JSON list. For
agents, `name` is the slug.

### Previewing locally

Validate and build into `_site/`, then serve it and open
[localhost:8621](http://localhost:8621):

```sh
python3 scripts/validate.py
python3 scripts/build_site.py
python3 -m http.server 8621 --directory _site
```

The preview is the raw content tree, with no HTML index page, since this is what
entoli clients consume.

## Validation

Every pull request that adds or modifies content under `data/` is validated by
[scripts/validate.py](scripts/validate.py):

- Each touched skill has `SKILL.md` and `README.md`, and each touched agent has
  `PROMPT.md` and `README.md`.
- Frontmatter and slugs follow the rules above, checked with the same parser
  semantics entoli uses, so a green check means entoli accepts the entry.

On merge to `main`, the site is rebuilt and deployed to GitHub Pages. The deploy
re-runs the same validation and fails on invalid data.
