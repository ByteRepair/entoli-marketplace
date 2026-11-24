# Software Design Review

A skill that reviews a design doc or RFC with the standards of a staff
engineer and an AppSec engineer, in one pass: does the design hold, can
another team build it, and what are its threats.

## What you get

- A verdict and ranked comments (blocking, should-fix, opinion), each
  anchored to a section and stated as the question to answer.
- Missing-section callouts and candidate entries for a thin
  "alternatives considered".
- A STRIDE threat list over the doc's trust boundaries and a mitigation
  checklist ordered to build first.

## Configuring

Paste the draft and say what system it shapes and which teams it
touches. The constraints it must respect, the data classifications and
the authentication on each path make both reviews sharper. It reviews
designs, not code.
