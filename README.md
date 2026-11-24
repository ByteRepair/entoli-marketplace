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
collections/
  skills.toml       the collections the app groups entries under
  agents.toml       (see Collections)
```

The body of `SKILL.md` holds the instructions entoli loads; the body of
`PROMPT.md` holds the system prompt the agent runs under. Reference bundled
files from the body with relative paths; `references/`, `scripts/`, and
`assets/` are the conventional directories. `profile.png` is served next to the
prompt, where entoli looks for an agent's picture.

## Skills or agents

A job is a skill. An agent is someone the user manages. Pick by this
rule, not by how large the job is.

**Why.** We ran one renewal-prep job 45 times: one agent with the skill,
Athena briefing specialist sub-agents, and Athena with specialists in an
Omada room. The single agent scored as well or better on every measure
(99% of planted traps handled against 97-98%) at a fifth of the cost
(about $0.03 against $0.17 a run), and the only invented facts came from
relaying answers between agents. Published studies agree: with the same
model and the same material, more agents add cost, not quality. They
help when a part needs its own context: too much material for one
prompt, a tool only one part can reach, or large independent parts run
in parallel.

### Make a skill when

- it is a job with an end: a memo, a plan, a draft, a review;
- or several roles' judgment goes into one result. The roles' standards
  are written into the skill's steps; you do not ship agents for them.

A skill whose part needs its own context ships that part's sub-agent
prompt in `references/<part>.md`. The runner gives the part to entoli's
built-in `explore` agent (read-only) or `general` agent (full tools)
with the prompt's path and the input files; it does not need a
marketplace agent.

### Make an agent when

- **It needs something a loaded skill cannot give**: today, nothing
  qualifies, so the marketplace ships no local agents.

None of these needs an agent, so none is a reason for one:

- **A way of working for the whole session** is a skill the user loads
  once: `ponytail` holds until the user turns it off.
- **State across sessions** is a file: a skill keeps it in a record
  (see [Records](#records)).
- **A recurring run** is a trigger: one with no `member` fires into a
  new chat that Athena answers, and its prompt can name the skill.
- **Delegating by handle** is a name to call, not a capability; the
  user runs the skill instead.
- **Different tools per role** would need an agent, but agent
  frontmatter cannot declare tools today. Revisit this rule if it can.

An agent whose rules only matter while one job runs is a skill with
extra cost; write the skill instead.

### Skill shape

Every local work skill (`data/skills/<domain>-<job>/`) is run start to
finish by whoever loads it, in one pass. Its `SKILL.md` body has these
sections:

- **Introduction** (`# Title`, then one paragraph): the job, whose
  standards it applies, what it turns into what, and what it never does
  (send, pay, publish, submit).
- **`## Inputs`**: required and optional. Ask once, in one message, for
  missing required inputs; state the default for everything else.
- **`## Steps`**: numbered, in the order the work is done. A step that
  is one role's part names the role and carries its standards.
- **`## Success criteria`**: a checklist the answer is checked against
  before it is given, testable from the answer alone.
- **`## Output`**: sections, order, limits and style. Empty sections
  are left out; "data still needed" appears once, at the end.
- **`## Handing off a part`**: which steps may go to a sub-agent and
  when. A realistic hand-off names its `references/<part>.md` file, the
  agent (`explore` or `general`), and the input files it expects.
  Otherwise it says to do every step yourself.

A packaged prompt has `# <Part>`, a line naming the skill, the step and
the agent, then `## Inputs` (the files it is given), `## Do` (the step,
self-contained), `## Return` (the exact shape, nothing else) and
`## Rules` (the standards and what it never does). It restates what it
needs rather than pointing back at `SKILL.md`, because the sub-agent
sees nothing else. Use `explore` for parts that only read and report,
`general` only for parts that must write files or run commands.

Imported skills (`_release/`, `ext/`) and design skills such as
`bot-avatar-creator` keep their own structure.

### Records

A skill that runs again and again (weekly, monthly, per tag) keeps a
record: `records/<skill-name>.md` in the project workspace, the last
run's summary. Its `## Inputs` says to read the record first when it
exists and to say what changed since then. Its `## Output` says what the
summary holds and to replace the record with it after answering, or,
where files cannot be written, to end with the summary for the user to
save. A record holds facts the next run compares against, never
personal comments or anything the skill's privacy rules keep out.

### Agent shape

For when an agent qualifies. An agent is named `<domain>-<role>` when
it belongs to a domain, with that domain's skill prefix, so its handle
stays unique when a project installs several domains. Its `PROMPT.md` body has these sections:

- **Introduction** (unheaded opening): who it is, what it turns into
  what, and the action it never takes.
- **`## Workflow`**: numbered steps for how it works on any request,
  with the defaults used when a request is bare and the
  ask-don't-invent rule.
- **`## Expectations`**: the behavior it keeps on every turn, style,
  scope limits, and what it flags instead of inventing.

## Slugs

The directory name under `data/skills/` or `data/agents/` is the entry's slug.
It must be lowercase kebab-case:

```regex
^[a-z0-9]+(-[a-z0-9]+)*$
```

Examples: `software-release-notes`, `fashion-line-plan`, `py2`. The
slug is the entry's
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
name: py2
description: >-
  Converts Python 2 code to modern idioms. Use this when the user asks to
  port a Python 2 file or codebase to Python 3.
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
| `version`     | metadata | no       | valid SemVer string (`x.y.z`)      |
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
name = "Anthropic"           # optional: the collection's name, 1-64 chars
summary = "..."              # optional: the collection's summary, 1-160 chars
```

The manifest carries no entry metadata: `version` and friends come from the
remote entry's own frontmatter, so nothing in `ext/` can go stale against its
source. `tags` is appended to the tags the remote frontmatter carries. `name`
and `summary` describe the collection, not an entry: a manifest whose path
publishes `<slug>/<sub>` entries is shown in the app as one collection under
that name (the slug where `name` is absent). Other entries are grouped in
`collections/` (see [Collections](#collections)).

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
  joined with ", ".
- `README.md` is optional (no marketplace page is built for remote entries).
- Tags are prefixed with `external`.
- `metadata.version` need not be SemVer (the spec leaves metadata values
  free-form). A numeric version is padded to `x.y.z` (`49` → `49.0.0`,
  `v2.1` → `2.1.0`); one with no number publishes without a version.

An unpinned `ref` drifts with the source repository; validation and deploys
re-check the current state each run, so upstream breakage fails this repo's
CI. Pin a tag or commit SHA to decouple.

## Collections

The app lists a section as collections, then the entries in none. An ext
manifest publishing `<slug>/<sub>` entries is a collection of its own entries.
Every other grouping is declared in `collections/<section>.toml`, one table per
collection:

```toml
[design]
name = "Design"                   # required, 1-64 chars
summary = "Art, themes and looks." # optional, 1-160 chars
members = ["canvas-design"]       # required: the section's index keys
```

A member is any entry of the section (local, staged from a release, or a
single-entry ext manifest) by its index key. An entry sits in one collection
at most, a manifest's own entries are its collection's alone, and a declared
slug may not be an ext manifest's. `scripts/collection_files.py` checks the
files against the slugs it can see offline; the build checks every member
against the finished index.

## Skills releases

`_release/skills/` is generated at build time: `build_site.py` runs
`scripts/import_release.py`, which imports the latest release tag of
`ByteRepair/skills` (or the one `--tag vX.Y.Z` names) — each skill
directory copied verbatim, with the `metadata:` block added (author
`Entoli`, the tag's version, tags `internal`) and a README.md, and
`skill-creator` skipped, entoli's presets bundling their own copy. The
stage is wiped and re-fetched every build and never committed.

```sh
python3 scripts/import_release.py
```

## Publishing

`data/skills/` maps to `/skills` and `data/agents/` maps to `/agents` on GitHub
Pages, with file paths preserved: `data/skills/<slug>/SKILL.md` is served
at `/skills/<slug>/SKILL.md`. Beside these, the build zips each skill
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
_site/ext/<section>/index.json   one record per remote entry, keyed by its
                                 published key: {key: {repo, ref?, dir,
                                 files}} — dir is the entry directory's
                                 repository-relative path and files the
                                 blob names under it, resolved by the build
                                 so a client fetches without a listing; ref
                                 present only when pinned
_site/<section>/collections.json every collection, keyed by slug:
                                 {slug: {name, summary, members}} — each
                                 manifest publishing <slug>/<sub> entries
                                 and each collections/<section>.toml table;
                                 members are index keys
```

### index.json

For client discoverability, each section also publishes an `index.json` derived
from the entries' frontmatter, keyed by slug:

```json
{
  "software-release-notes": {
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
the key), `version` from the frontmatter normalised to SemVer, and `tags` is
`external` plus the manifest's tags plus the remote frontmatter's own,
deduplicated in that order.

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
