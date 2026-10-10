# Software Security Review

An agent that behaves like the security engineer on pre-launch review:
it writes every feature's threats down before the feature ships.

It walks the stated trust boundaries through STRIDE, ranks threats by
likelihood times impact for this feature specifically, and maps each to
the mitigations already present — the remaining gaps become the
mitigation checklist. Unknowns stay unknown: a classification or flow
you have not described comes back as the question for your team.

## What you get

- The threat list: boundary, STRIDE category, description, existing
  mitigation, remaining gap, severity.
- A mitigation checklist ordered to build first, each item tied to the
  threat it closes.
- The unknowns list: what the model assumed, and what to answer first.

## Configuring

Describe the feature, its flows in and out, and the data
classifications (public, internal, PII, credentials). It cannot scan
or reproduce anything; threats are reasoned from the material you
provide, not tested.
