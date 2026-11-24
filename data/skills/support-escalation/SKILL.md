---
name: support-escalation
description: >-
  Writes an engineering escalation from a support ticket with the standards
  of a senior support engineer. Give it the ticket thread and any logs or
  account details, and it writes one escalation with repro steps,
  environment, impact, what was tried and the precise ask, with every
  unknown marked. Use when the user asks to escalate a ticket, file a bug
  from a customer report, or hand a problem to engineering.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: support, escalation, bugs
---

# Escalation

This job writes one engineering escalation the way a senior support
engineer would: give engineering everything they need to act on the
first read, and say plainly what is not known. You turn the ticket
thread and details in the conversation into one escalation ready to
file. You never file the escalation, reply to the customer, or promise
the customer a fix or a date.

## Inputs

Required: the ticket thread, with the customer's messages and support's
replies. Optional: logs, screenshots described in text, account and plan
details, the product version, related tickets, the team's escalation
template or severity scale.

Ask once, in one message, for anything required that is missing.
Without a template, use the sections under Output. Without a severity
scale, use: critical (many customers blocked or data at risk), high
(one customer blocked, no workaround), medium (workaround exists), low
(cosmetic or question).

## Steps

1. **Summary.** One sentence: what fails, for whom, since when.
2. **Repro steps.** Number the steps from the thread that lead to the
   failure, then the expected and the actual result. If support has not
   reproduced it, say so and mark the steps "as reported by the
   customer".
3. **Environment.** Account, plan, platform, browser or app version,
   region, time of the failure with time zone. Write "unknown" for any
   field the thread does not give.
4. **Evidence.** Quote error messages and log lines exactly, with their
   timestamps. Do not paraphrase an error.
5. **Impact.** How many customers or accounts are affected, what they
   cannot do, whether a workaround exists, and any deadline the customer
   gave. Separate what the customer said from what you infer.
6. **Tried.** What support tried and the result of each try, so
   engineering does not repeat it.
7. **Ask.** The precise ask: investigate a cause, fix a bug, restore
   data, confirm expected behavior, or give a workaround. One ask, or a
   numbered list if more than one.
8. **Severity.** Rate it on the scale, with the reason in one line.
9. **Check** the escalation against the success criteria and fix what
   fails.

## Success criteria

- Every environment field has a value from the thread or "unknown".
- Error text is quoted exactly as in the material.
- Repro steps say whether support reproduced them.
- Impact separates what the customer said from what is inferred.
- The ask is a specific action engineering can say yes or no to.
- No customer personal data appears beyond what the ask needs.

## Output

In this order: title (under 80 characters, the symptom and the area);
severity and reason; summary; repro steps with expected and actual;
environment; evidence; impact; what was tried; the ask; unknowns, as a
list of questions and who can answer each (a role); data still needed.
Plain sentences, no blame.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
