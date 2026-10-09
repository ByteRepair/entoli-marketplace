# entoli-marketplace

This repository contains the content served by the entoli marketplace: skills
and agents for entoli clients to discover and install.

Skills follow the [Agent Skills spec](https://agentskills.io/specification) —
entoli implements that spec, and a skill this repo serves must conform to it
(`SKILL.md` frontmatter grammar and caps, `name` matching the directory, top
level limited to the spec's key set). Agents are an entoli content type
modeled on the same convention.

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
ext/
  skills/<slug>/
    index.toml      remote entry manifest (see Remote entries)
  agents/<slug>/
    index.toml      remote entry manifest
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

Slugs under `ext/` follow the same rule; the published key of a sub-entry is
`<slug>/<sub>` (see [Remote entries](#remote-entries)).

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

Rules that follow from the frontmatter grammar (real YAML, as the Agent
Skills spec's examples are written):

- The file must start with `---\n`; the closing `---` must sit on its own line.
- `metadata:` entries are `key: value` lines indented under it at one uniform
  indent; its values are strings.
- `tags` is a comma-separated plain string, not a YAML list.
- Folded (`>-`) and literal (`|`) block scalars, quoting, and comments are
  accepted, so long descriptions may span lines.

Skills additionally: top-level keys are exactly the spec's (`name`,
`description`, `license`, `compatibility`, `metadata`, `allowed-tools`), the
`name` scalar is 1 to 64 lowercase-kebab characters and matches the folder, and
`compatibility` is at most 500 characters when present.

Agents: only `description` and `metadata` at the top level. The agent's name is
its file name, so no `name` key is used.

## Remote entries

A directory under `ext/<section>/<slug>/` holds no entry content — only an
`index.toml` manifest pointing at a living entry in another GitHub repository:

```toml
repo = "anthropics/skills"   # required: owner/name
ref  = "v1.2.0"              # optional: tag, branch, or commit SHA; the
                             # repository's default branch when omitted
path = "skills/algorithmic-art"  # required: subtree root inside the repo
tags = "ai, sdk"             # optional: extra marketplace-side tags
```

The manifest carries location only — no metadata fields: `version` and friends
come from the remote entry's own frontmatter, so nothing in `ext/` can go
stale against its source. `tags` is the one marketplace-side extra; it is
appended to the tags the remote frontmatter carries.

The manifest path matches one of two shapes:

- it is a single entry directory (its `SKILL.md`/`PROMPT.md` directly inside),
  published under the ext slug;
- it is a directory of entry directories one level deep, each published under
  `<slug>/<sub>` where `<sub>` is the remote directory name.

Both shapes at once, or deeper nesting, is rejected. Only `index.toml` may sit
in an ext directory. An ext slug that collides with a `data/<section>/` slug
is rejected.

### Remote entry rules

The remote content is fetched at validation and build time and held to the
same `SKILL.md`/`PROMPT.md` rules as `data/` entries: spec-conformant
frontmatter, `name` matching the remote directory, description limits, agent
file set (`PROMPT.md`, `README.md`, `profile.png` only) and PNG magic. What
differs:

- `metadata.author` is not required — the source repository's contributors
  (the ten with the most contributions) publish as the entry's authors,
  comma-joined.
- `README.md` is optional (no marketplace page is built for remote entries).
- Tags are prefixed with `external`.

An unpinned `ref` drifts with the source repository; validation and deploys
re-check the current state each run, so upstream breakage fails this repo's
CI. Pin a tag or commit SHA to decouple.

## Publishing

`data/skills/` maps to `/skills` and `data/agents/` maps to `/agents` on GitHub
Pages, with file paths preserved: `data/skills/code-review/SKILL.md` is served
at `/skills/code-review/SKILL.md`. Beside these, the build zips each skill
directory into `/skills/<slug>.skill` — the one file an entoli client fetches
to install the whole entry (see [Build outputs](#build-outputs)). Remote
entries publish no content: their manifests map to `/ext/<section>/index.json`
(see below).

### Build outputs

Beside the entries themselves, the build writes:

```text
_site/skills/<slug>.skill        zip of the whole skill directory, one per
                                 skill, served beside the entry's directory
                                 (skills/<slug>.skill, not inside it) — the
                                 file an entoli client fetches to install it,
                                 through the app's .skill import
_site/<section>/index.json       frontmatter of every entry, keyed by slug;
                                 remote entries joined in under their keys
_site/ext/<section>/index.json   every remote entry manifest's location data:
                                 {slug: {repo, ref?, path}}, ref present
                                 only when pinned
```

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

Remote entries join the section index under their key (`<slug>` or
`<slug>/<sub>`) with the same record shape; the differences follow
[Remote entry rules](#remote-entry-rules): `author` is the comma-joined
contributor logins, `name` comes from the remote frontmatter (falling back to
the key), `version` from the frontmatter, and `tags` is `external` plus the
manifest's tags plus the remote frontmatter's own, deduplicated in that order.

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

Every pull request that adds or modifies content under `data/` (local) or
`ext/` (remote manifests) is validated:

1. **Entoli's own CLI — the source of truth for `data/`.** CI checks out the
   entoli repo beside this one and runs
   `dart run entoli/tool/validate_marketplace.dart`, which validates entries
   using the same frontmatter parser and Agent Skills spec checks the app
   applies at import. A green run there is exactly "entoli accepts the entry".
   It has no network access, so it covers `data/` only.
2. **A Python quick pass.** [scripts/validate.py](scripts/validate.py) runs
   the same rules as a port, so contributors without a Dart toolchain get the
   same checks locally. It also validates `ext/`: fetching each manifest's
   remote content over the GitHub API (`GITHUB_TOKEN` is used when set) and
   holding it to the rules in [Remote entry rules](#remote-entry-rules).
   Network failures fail the validation — a green check never means
   unverified remote content.

Beyond the shared rules, each touched skill must have `SKILL.md` and
`README.md`, and each touched agent must have `PROMPT.md` and `README.md`.

On merge to `main`, the site is rebuilt and deployed to GitHub Pages. The
deploy re-runs the same validation (with the ext fetches) and fails on invalid
data.
