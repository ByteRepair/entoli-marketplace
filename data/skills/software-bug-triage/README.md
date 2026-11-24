# Software Bug Triage

A skill that triages a bug backlog with the standards of a QA engineer, in
one pass: duplicates clustered, severities set, and what each issue needs
before anyone can reproduce it.

## What you get

- A triage table: issue, cluster, severity, confidence, area, missing
  repro info, next step, with S1s lacking repro first.
- One hypothesis line per cluster, labeled as hypothesis.
- Stale issues flagged for re-verification, and owners suggested from
  your hints, never assigned.

## Configuring

Paste the issue export or list, or name the repository and issues when
the agent can read your tracker. State your severity scale (the default:
S1 crash or data loss, S2 feature broken, S3 degraded, S4 cosmetic) and
the freshness window for "stale" (the default: 90 days). Postmortem
action items from software-incident-postmortem can be pasted in as they
are.
