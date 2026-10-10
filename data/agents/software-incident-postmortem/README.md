# Software Incident Postmortem

An agent that behaves like the on-call engineer after a resolved
incident: it writes down what happened while it is fresh.

Postmortems live or die by the record they are built from. This agent
reads your pasted timeline, alert log, and chat trail, deduplicates the
noise, and writes the blameless postmortem — events and conditions,
never names. Gaps in the record become an explicit list, and vague
remediations are sharpened into trackable tasks. It never mitigates or
deploys anything.

## What you get

- The postmortem: summary, impact, timeline, contributing factors, what
  went well, what went poorly, action items.
- An explicit missing-data list — the record's gaps, each with what
  filling it would take.
- Action items as trackable tasks with owner roles and priorities.

## Configuring

Paste the alert trail, chat excerpts, and mitigation steps; state the
timezone and whatever impact data you have. A first complete draft
comes back once, ready for one pass before the review.
