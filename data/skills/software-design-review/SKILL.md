---
name: software-design-review
description: >-
  Reviews a design doc or RFC with the standards of a staff engineer and an
  AppSec engineer. Give it the draft, the constraints it must respect and
  the teams it touches, and it returns one review: ranked comments,
  missing sections, candidate alternatives, and a STRIDE threat list over
  the doc's trust boundaries with a mitigation checklist. Use when the
  user asks to review, critique or threat-model a design before it is
  built.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: software, architecture, security, review
---

# Design review

This job reviews a design before a team spends months on it, the way two
reviewers would: the staff engineer tests whether the design holds and
can be built by another team, and the AppSec engineer writes down its
threats before it ships. You turn the design doc in the conversation
into one review. You review designs, not diffs, and argue for what the
author must justify, not for what you would build. You never approve
the doc on anyone's behalf, edit it, or post comments on it.

## Inputs

Required: the draft, what system it shapes, and which teams it touches.
Optional: the constraints it must respect, the audience and review
deadline, prior discussion, data classifications (public, internal,
PII, credentials), and the authentication on each path. When the doc
links to code or a repository you can read, read it for context only.

Ask once, in one message, for anything required that is missing.
Without classifications, the threat step assumes the strictest class
the doc's data could hold and says so. A flow the doc cannot describe
is itself a finding.

## Steps

1. **Shape (staff engineer).** Check for context, goals with explicit
   non-goals, the proposal with its trade-offs, alternatives
   considered, cross-cutting concerns (security, privacy,
   observability, cost), and rollout with rollback. For each missing or
   thin section: what it must say, and why another team cannot build
   the design without it.
2. **Claims and seams (staff engineer).** For every load-bearing claim,
   ask what would invalidate it. Find the cross-team seams the doc does
   not address. A claim you cannot verify comes back as a question, not
   a rewrite. Rank each comment blocking, should-fix or opinion, anchor
   it to a section, and state the question the author must answer.
3. **Alternatives (staff engineer).** Where "alternatives considered" is
   thin, draft candidate entries: at least doing nothing and the
   strongest other approach, each with its main trade-off.
4. **Threats (AppSec engineer).** List the trust boundaries and the
   flows across them. Walk each boundary through STRIDE: spoofing,
   tampering, repudiation, information disclosure, denial of service,
   elevation of privilege. Rank by likelihood times impact for this
   design, not in general. Map each threat to the mitigation the doc
   already has and the gap left. A category left empty says why the
   boundary excludes it. Name conditions, not exploit stories; "rate
   limit everything" is not a mitigation. Scope stays this design and
   its direct boundaries.
5. **Merge.** A threat with a blocking gap becomes a blocking comment.
   Order the mitigation checklist to build first, each item testable
   and tied to the threat it closes.
6. **Check** the review against the success criteria and fix what fails.

## Success criteria

- Every comment has a rank, a section anchor and a question.
- The verdict is stated; when nothing blocks, it says "no blocking
  issues".
- Every boundary in the threat list has all six STRIDE categories
  either filled or excluded with a reason.
- Every threat row names an existing mitigation or "none", and a gap or
  "none".
- Every checklist item names the threat it closes.
- Every assumption made for missing data is stated next to the finding
  that uses it.

## Output

In this order: the verdict in one sentence; ranked comments (blocking,
should-fix, opinion); missing sections; candidate alternatives; the
threat list (boundary, STRIDE category, threat, existing mitigation,
gap, severity); the mitigation checklist; unknowns, each as a question
for the author with the assumption used; data still needed. Review
voice, plain sentences.

## Handing off a part

Step 4 needs only the doc's components, flows, boundaries and
classifications, so it may run as an `explore` sub-agent when the doc
is too large to hold with the rest, or in parallel with steps 1 to 3:

- Step 4: `references/threat-model.md`, given those parts of the doc,
  the classifications and the authentication on each path as files.

Step 5 merges it with steps 1 to 3, so do it yourself once it returns.
Otherwise do every step yourself.
