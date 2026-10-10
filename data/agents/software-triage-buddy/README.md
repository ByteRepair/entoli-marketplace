# Software Triage Buddy

An agent that behaves like the QA engineer at bug triage: the backlog
becomes readable before it becomes work.

It clusters duplicate reports, assigns severities and areas with a
confidence, and writes down what each issue is missing for
reproduction — the questions that turn "it broke" into a reproducible
ticket. It cannot run software or see your tracker; it says unknown
rather than guessing.

## What you get

- A triage table: issue, cluster, severity, confidence, area, missing
  repro info, suggested next step.
- One hypothesis line per cluster, marked as hypothesis.
- Suggested assignments by area or owner hints, never asserted.
- Stale issues flagged for re-verification instead of trusted.

## Configuring

Paste the issue export or list and state your severity scale (the
default: S1 crash or data loss, S2 feature-broken, S3 degraded, S4
cosmetic) and the freshness window for "stale".
