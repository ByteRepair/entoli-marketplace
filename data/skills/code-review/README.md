# Code Review

Reviews pull request diffs for bugs, security issues, and style problems, and
leaves focused inline comments.

Code Review runs when a reviewer requests it. For each hunk it examines the
change in the context of the whole file, then reports only findings it can tie
to a concrete line: crash risks, injection paths, race conditions, missing
error handling, and violations of the repository's own conventions.

## How it behaves in review

- Reads contributing guides and linter configs first, so "style" findings
  match your rules, not a generic checklist.
- Groups its comments: one comment per issue, prefixed `bug:`, `security:`,
  or `style:`.
- Skips hunks that are pure formatting or generated code, unless the hunk
  breaks the generator's contract.
- Marks low-confidence guesses as questions instead of assertions, and stays
  silent when it has nothing worth saying.

## Install

Reference the skill from entoli and ask it to review a diff. It needs read
access to the repository and permission to post comments.

## Files

- `SKILL.md` — the skill definition loaded by entoli.
- `references/` — sample review comments for calibration.
