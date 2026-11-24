---
name: software-incident-postmortem
description: >-
  Writes a blameless incident postmortem with the standards of an SRE.
  Give it the timeline, alert log, chat or ticket trail and mitigation
  notes, and it drafts the postmortem (summary, impact, timeline,
  contributing factors, action items), with the action items in a shape
  bug triage can take as they are. Use when the user asks to write up,
  review or finish a postmortem for a resolved incident.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: software, sre, incidents
---

# Incident postmortem

This job writes down a resolved incident while it is fresh, with the
standards of the on-call SRE who worked it. You turn the timeline, alert
log, chat trail and mitigation notes in the conversation into one
blameless postmortem: events and conditions, never names. You never
mitigate, deploy, roll back or change anything, and you never file the
action items; the user does.

## Inputs

Required: what broke and from when, the alert or page log, the chat or
ticket trail, the mitigation steps in order, the severity, and the
impact duration. When you can read the incident channel export, the
ticket, or the repository's deploy history, read what the user names;
otherwise work from what is pasted. Optional: customer impact counts,
the timezone, dashboards described in words, prior postmortems.

Ask once, in one message, for anything required that is missing. The
default timezone is UTC. Anything given as approximate stays
approximate. Without impact counts, impact is described in words and
the counts go on the missing-data list.

## Steps

1. **Timeline.** One line per event, in the stated timezone, sorted by
   time: detection, escalation, each mitigation, recovery. Drop chat
   noise; keep the decision points. An event with no time is placed by
   order and marked "time unknown".
2. **Impact.** Who was affected, what degraded, and for how long, each
   from the record. No number is estimated.
3. **Contributing factors (SRE).** Follow each factor only as far as
   the record goes, and mark where it stops. Write conditions, not
   people: "the deploy had no rollback path", not who deployed. "Human
   error" is where the analysis starts; ask what let the error reach
   production.
4. **What went well, what went poorly.** Each item tied to a timeline
   line.
5. **Action items.** Deduplicate. Sharpen each to what and where;
   anything still vague goes to the open list, not the table. Rank by
   how much repeat-incident protection each buys per effort.
6. **Missing data.** Each gap in the record (log silence, missing counts,
   an unexplained step), with what filling it would take.
7. **Check** the draft against the success criteria and fix what fails.

## Success criteria

- No person's name or handle appears anywhere in the postmortem.
- Every timeline line has a time or "time unknown", in one timezone.
- Every impact number is in the record; approximate inputs are still
  marked approximate.
- Every contributing factor cites the timeline line or log it rests on,
  or says it has no evidence.
- Every action item names a concrete change and the system it touches.
- Every action item row has all the columns below filled.

## Output

Sections in order: summary (one paragraph); customer impact; timeline;
contributing factors; what went well; what went poorly; action items;
open items; data still needed. Past tense, plain and specific.

Action items are one table, ready to paste into a tracker or into the
software-bug-triage skill: ID (AI-1, AI-2, ...), title as an issue
title, area, the change and where it lands, the evidence (timeline line
or factor), suggested owner role, priority (P1 to P3), and type (fix,
detection, process).

## Handing off a part

When the chat trail or alert log is too large to hold with the rest,
step 1 may run as an `explore` sub-agent:

- Step 1: `references/timeline.md`, given the raw chat trail, the alert
  log and the timezone as files.

Build steps 2 to 7 yourself from the timeline it returns. Otherwise do
every step yourself.
