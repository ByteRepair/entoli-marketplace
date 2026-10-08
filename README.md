# entoli-marketplace

This repository contains the content served by the entoli marketplace: skills
and agents for entoli clients to discover and install.

Everything under `data/` is published to GitHub Pages on merge to `main`
(see [Publishing](#publishing)). All content is licensed AGPLv3 (see
[LICENSE](LICENSE)); the AGPLv3 grant covers every entry, so entries carry no
license field of their own.

An entry's metadata lives in the frontmatter of its definition file — the
same frontmatter entoli reads. There is no separate index file.

## Layout

```text
data/
  skills/
    <slug>/
      SKILL.md      required: definition + metadata frontmatter
      README.md     required: long description for the marketplace page
      ...           optional: any other files/directories the skill needs
  agents/
    <slug>/
      PROMPT.md     required: agent prompt + metadata frontmatter
      README.md     required: long description for the marketplace page
      profile.png   optional: agent avatar (PNG)
```

## Slugs

The directory name under `data/skills/` or `data/agents/` is the entry's
slug. It must be lowercase kebab-case:

```regex
^[a-z0-9]+(-[a-z0-9]+)*$
```

Examples: `code-review`, `release-notes`, `py2`. The slug is the entry's
identity in URLs and in `index.json`.

## Frontmatter

`SKILL.md` and `PROMPT.md` open with YAML frontmatter holding the metadata
both entoli and the marketplace read. Skills follow the Agent Skills spec
(entoli enforces it: unknown top-level keys are refused), so marketplace-only
fields live under `metadata:` — the spec's extension point, which entoli
reads as a string-to-string map.

```yaml
---
name: code-review
description: >-
  Reviews diffs for bugs and style problems. Use this when the user
  asks to review a diff or a pull request.
metadata:
  author: Ada Lovelace
  version: 1.2.0
  tags: code-quality, review
---
```

| Field         | Where    | Required | Rules                            |
| ------------- | -------- | -------- | -------------------------------- |
| `name`        | SKILL.md | skills   | equals the slug (spec rule)      |
| `description` | scalars  | yes      | non-empty; <=1024 chars, skills  |
| `author`      | metadata | yes      | non-empty string                 |
| `version`     | metadata | no       | valid SemVer string              |
| `tags`        | metadata | no       | comma-separated; unique          |

Rules that follow from entoli's parser (a strict regex subset of YAML):

- The file must start with `---\n`; the closing `---` must sit on its own
  line.
- `metadata:` entries are single `key: value` lines indented under it, at
  one uniform indent. Keep `metadata:` as the last frontmatter entry — a
  scalar key after the nested block is dropped by entoli's parser.
- `tags` is a comma-separated plain string, not a YAML list: entoli would
  read `[a, b]` as the literal string `[a, b]`.

Skills additionally: top-level keys are exactly the spec's (`name`,
`description`, `license`, `compatibility`, `metadata`, `allowed-tools`), the
`name` scalar is 1–64 lowercase-kebab characters and must match the folder,
and `compatibility` is at most 500 characters when present.

Agents: only `description` and `metadata` at the top level; the agent's name
is its file name, so no `name` key.

## Skills

`data/skills/<slug>/`:

- `SKILL.md` — the skill definition: frontmatter (above) plus the
  instructions entoli loads. Reference bundled files from the body with
  relative paths (`references/…`, `scripts/…`, `assets/…` are the
  conventional directories).
- `README.md` — long description shown on the skill's marketplace page.
- Any additional files or directories the skill ships. They are published
  preserving relative paths.

## Agents

`data/agents/<slug>/`:

- `PROMPT.md` — the agent's prompt: frontmatter (above) plus the system
  prompt it runs under.
- `README.md` — long description shown on the agent's marketplace page.
- `profile.png` — optional agent avatar image (PNG). Served next to the
  prompt, where entoli looks for an agent's picture.

## Publishing

`data/skills/` maps to `/skills` and `data/agents/` maps to `/agents` on
GitHub Pages. File paths are preserved: `data/skills/code-review/SKILL.md`
is served at `/skills/code-review/SKILL.md`.

### index.json

For client discoverability, each section also publishes an `index.json`
derived from the entries' frontmatter, keyed by slug:

```json
{
  "code-review": {
    "name": "code-review",
    "description":
        "Reviews diffs for bugs and style problems. Use this when
        the user asks to review a diff or a pull request.",
    "author": "Ada Lovelace",
    "version": "1.2.0",
    "tags": ["code-quality", "review"]
  }
}
```

`version` and `tags` are present only when set; `tags` becomes a real JSON
list. For agents, `name` is the slug.

## CI

Every pull request that adds or modifies content under `data/` is validated:

- Each touched skill must have `SKILL.md` and `README.md`; each touched
  agent must have `PROMPT.md` and `README.md`.
- Frontmatter must match the rules above — validated with the same parser
  semantics entoli uses, so CI green means entoli accepts the entry.
- Slugs must match the naming rule.

On merge to `main`, the site is built and deployed to GitHub Pages. The
build re-runs the same validation and fails the deploy on invalid data.
