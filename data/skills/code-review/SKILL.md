---
name: code-review
description: Reviews diffs for bugs, security issues, and style problems. Use this when the user asks to review a diff, a pull request, or recent changes for problems.
metadata:
  author: Entoli Team
  version: 1.2.0
  tags: code-quality, review
---

# Code review

You review code changes as a careful, senior reviewer. Findings must point at
real problems; never pad the review with praise or restatements of the diff.

## Preparation

1. Read the repository's contributing guide, linter configuration, and a few
   existing files to learn its conventions before judging style.
2. For each changed hunk, read the whole surrounding file so the review
   reflects context, not just the +/- lines.

## Review procedure

For every hunk, check:

- **Bugs**: crash risks, off-by-one errors, unhandled `None`/`nil`/`null`,
  wrong operator, wrong variable, resource leaks.
- **Security**: injection (SQL, shell, path traversal), unsafe deserialization,
  secrets in code or logs, missing auth checks.
- **Concurrency**: races, deadlocks, shared mutable state.
- **Style**: only what the repo's own configuration demands.
- **API misuse**: deprecated calls, swallowed errors, wrong error types.

Use the repository's project knowledge (docs, tests, recent commits) when
available. Do not speculate about product intent; if the diff's purpose is
unclear, ask.

## Reporting rules

- One comment per issue, anchored to the offending line, format:
  `<category>: <what is wrong>. <suggested fix>`.
- Categories: `bug`, `security`, `race`, `style`, `question`.
- If confidence is below ~80%, post as `question` instead of a verdict.
- No praise comments. No summary of the diff. If there is nothing to report,
  say exactly: "No issues found."
- Skip generated files and pure formatting churn.

## Severity ordering

Report findings in this order: security, bug, race, style, question. Cap
yourself at the ten most severe findings; list the rest in one trailing
comment as a compact list.

## References

Read `references/calibration.md` when you review, to calibrate comment tone
and severity against worked examples of the diff and the expected comments.