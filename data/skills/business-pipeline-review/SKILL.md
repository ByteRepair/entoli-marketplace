---
name: business-pipeline-review
description: >-
  Prepares the weekly pipeline review with the standards of a sales
  manager and a revenue operations analyst. Give it the open-deals
  export from the CRM, the quarter target and the review date, and it
  writes the coverage table, stalled-deal callouts, a forecast draft by
  band and one coaching question per at-risk deal. Use before a pipeline
  review or a forecast call.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: business, sales, forecasting
---

# Pipeline review

This job prepares one pipeline review the way a small team would: the
revenue operations analyst checks the export and does the math, and the
sales manager judges which deals are stuck and what to ask each rep. You
turn the CRM export and the target in the conversation into the review's
contents. You never edit the CRM, submit a forecast, or attend the
meeting.

## Inputs

Required: the open-deals export (stage, amount, close date, last
activity, next step, owner), the quarter target or what is left of it,
and the review date. Optional: closed-won so far, deal notes, the stage
norms (expected days per stage), each rep's quota.

Ask once, in one message, for anything required that is missing. Without
stage norms, use the median age per stage in the export and say so.
Without per-rep quotas, coverage is shown in total only.

If `records/business-pipeline-review.md` exists in the project
workspace, read it first: it is the last run's summary. Say what changed
since then.

## Steps

1. **Check the export (revenue operations).** Use the fields as they
   are. List every missing or malformed field (no close date, amount of
   zero, an owner who is not on the team) as a named gap. Never average
   over a gap or fill it in.
2. **Coverage (revenue operations).** Open pipeline against the
   remaining target, per rep and in total, as plain arithmetic. Add a
   risk-adjusted line that leaves out stalled deals and deals with a
   past close date.
3. **Stalled deals (sales manager).** Find deals with no activity in the
   last 14 days, a stage age well past the norm, or a close date that
   has moved or passed. Check large deals against their stage. Pick the
   five to eight that matter most, each with its age against the norm,
   why it looks stuck, and the question that would unblock it.
4. **Forecast draft (sales manager).** Place deals in commit, best case
   or pipeline, with one line of reason per deal placed. Week one is a
   look ahead; in the last two weeks of the quarter, list the deals to
   pull and where they move.
5. **Coaching questions.** One per at-risk deal, that the rep can answer
   in a sentence from today's facts and act on today.
6. **Check** the review against the success criteria and fix what fails.

## Success criteria

- Every number is in the export or shown as arithmetic on it.
- Each gap in the export is named; none is averaged over.
- There are at most eight stalled-deal callouts, each with an age, a
  reason and an unblocking question.
- Each deal in the forecast has a band and one line of reason.
- Each at-risk deal has exactly one coaching question.
- The review date and the week of the quarter are stated.

## Output

In this order: the headline (coverage and forecast in two sentences);
the coverage table; stalled-deal callouts; the forecast by band; the
coaching questions; export gaps and data still needed. Tables for the
coverage and the forecast, plain sentences for the rest.

After answering, replace `records/business-pipeline-review.md` in the
project workspace with this run's summary: the date, coverage per rep
and in total, the stalled deals, and the forecast by band. Where files
cannot be written, end with the summary for the user to save.

## Handing off a part

When the export is too large to hold with the rest, steps 1 and 2 may go
to an `explore` sub-agent:

- Steps 1 and 2: `references/export-coverage.md`, given the export, the
  remaining target and the review date (and the team list, stage norms
  and quotas) as files. It returns the gap list and the coverage table
  with its arithmetic.

Steps 3 to 5 build on its result, so do them yourself once it returns.
Otherwise do every step yourself.
