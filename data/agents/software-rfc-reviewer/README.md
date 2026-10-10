# Software RFC Reviewer

An agent that behaves like the staff engineer on design review: it
reads a design doc the way a careful senior would, before the team
commits months to it.

It checks the proven shape — context, goals with explicit non-goals,
the proposal with trade-offs, alternatives considered, cross-cutting
concerns, rollout and rollback — interrogates the load-bearing claims,
and finds the cross-team seams the doc does not address. It reviews
designs, not diffs.

## What you get

- Ranked review comments: blocking, then should-fix, then opinion,
  each anchored to a section and stated as the question to answer.
- Missing-section callouts: the section, what it must say, why the
  design without it is not buildable by another team.
- Candidate entries for a thin "alternatives considered" section.
- An explicit "no blocking issues" when the doc actually holds.

## Configuring

Provide the draft plus the constraints it must respect; name the
audience, the review deadline, and which teams it touches.
