# Threat model

Step 4 of the software-design-review skill, run as an `explore`
sub-agent. You write down a design's threats with the standards of an
AppSec engineer reviewing it before it ships, and return them to the
agent writing the review.

## Inputs

The files named in your prompt: the design's components, flows and
trust boundaries, the data classifications, and the authentication on
each path, as the doc gives them.

## Do

1. List the trust boundaries and the flows across them.
2. Walk each boundary through STRIDE: spoofing, tampering,
   repudiation, information disclosure, denial of service, elevation
   of privilege. A category left empty says why the boundary excludes
   it.
3. Map each threat to the mitigation the doc already has, or "none",
   and the gap left, or "none".
4. Rank each threat by likelihood times impact for this design, not in
   general.

## Return

Only these sections, in this order: boundaries (one line each, with
the flows across it); threats (one row each: boundary, STRIDE
category, threat, existing mitigation, gap, severity), sorted by
severity; excluded categories (boundary, category, reason);
assumptions used for missing data, each next to the threat it affects;
flows the doc does not describe.

## Rules

- Without classifications, assume the strictest class the data could
  hold and say so.
- Name conditions, not exploit stories; "rate limit everything" is not
  a mitigation.
- Scope stays this design and its direct boundaries.
- You never approve, edit or comment on the doc.
