# AGENTS.md

Guidance for AI coding agents working in this repository. The schema lives
in [README.md](README.md) and is enforced by `scripts/validate.py` — read
both before touching content.

## What this repo is

Marketplace content for entoli: skills and agents under `data/`, published
to GitHub Pages on merge to `main`. Content is the product; `scripts/` and
`.github/` exist to validate and publish it.

Skills follow the [Agent Skills spec](https://agentskills.io/home) —
entoli implements that spec, and this repo must too: spec-conformant
`SKILL.md` frontmatter, `name` matching the directory, and nothing outside
the spec's key set at the top level. Agents are an entoli content type
modeled on the same convention.

## Commands

- Validate everything: `python3 scripts/validate.py`
- Validate one entry: `python3 scripts/validate.py --entry data/skills/<slug>`
- Build the site into `_site/`: `python3 scripts/build_site.py`
- Preview (then open [localhost:8621](http://localhost:8621)):
  `python3 -m http.server 8621 --directory _site`
- Lint Python: `ruff check scripts && ruff format scripts`
- Lint changed markdown: `markdownlint <files>`

## Rules

- Entries are frontmatter-only; there is no index file. Marketplace
  metadata rides under `metadata:`: `author` (required), `version`
  (SemVer), `tags` (comma-separated plain string, not a YAML list).
- Skill `SKILL.md`: `name` must equal the directory slug, top-level keys
  are limited to the Agent Skills spec set, and `metadata:` must be the
  last frontmatter entry.
- Agent `PROMPT.md`: only `description` and `metadata` at the top level;
  never a `name` key — an agent's name is its file name.
- The frontmatter parser in `validate.py` is a verbatim port of entoli's
  `lib/domain/frontmatter.dart` (a strict regex subset of YAML). If that
  file changes upstream, port it again and run
  `dart tool/frontmatter_diff_test.dart` from a checkout with `../entoli`
  present — all cases must agree.
- Python scripts are stdlib-only; CI installs nothing.
- `_site/` is generated output; never commit it.
- CI green must mean entoli accepts the entry: never validate with
  semantics looser than entoli's own parser and spec checks.
