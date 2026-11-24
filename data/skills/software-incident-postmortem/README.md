# Software Incident Postmortem

A skill that writes a blameless postmortem for a resolved incident with the
standards of an SRE, in one pass: events and conditions, never names.

## What you get

- The postmortem: summary, impact, timeline, contributing factors, what
  went well, what went poorly.
- Action items as one table (ID, title, area, change, evidence, owner
  role, priority, type) that pastes into a tracker or into
  software-bug-triage as it is.
- An explicit list of what the record is missing, each gap with what
  filling it would take.

## Configuring

Paste the alert log, chat or ticket trail and mitigation steps, or name
them when the agent can read them. State the severity, the impact
duration and the timezone (the default: UTC). Impact counts make the
impact section exact instead of descriptive.
