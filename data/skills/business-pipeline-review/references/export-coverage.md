# Export and coverage

Steps 1 and 2 of the business-pipeline-review skill, run as an
`explore` sub-agent. You do one part of a pipeline review with the
standards of a revenue operations analyst, and return it to the agent
writing the review.

## Inputs

The files named in your prompt: the open-deals export (stage, amount,
close date, last activity, next step, owner), the remaining quarter
target, and the review date. The team list, the stage norms and each
rep's quota when given.

## Do

1. Use the export's fields as they are. List every missing or
   malformed field as a named gap: deal, field, what is wrong (no close
   date, an amount of zero, an owner not on the team).
2. Add up open pipeline per rep and in total, and set it against the
   remaining target. Show coverage as plain arithmetic (pipeline
   divided by target). Per rep only when quotas are given.
3. Add a risk-adjusted line that leaves out deals with a close date
   before the review date and stalled deals: no activity in the last 14
   days, or a stage age well past the norm. Without stage norms, use
   the median age per stage in the export and say so. List the deals
   left out and why.

## Return

Only these sections, in this order: export gaps (one line each: deal,
field, issue); the coverage table (rep or total, open pipeline,
target, coverage, risk-adjusted pipeline, risk-adjusted coverage), with
the arithmetic under it; deals left out of the risk-adjusted line;
data still needed.

## Rules

- Every number is in the export or shown as arithmetic on it; nothing
  is estimated.
- Never average over a gap or fill it in; a deal with a gap is named,
  and the sum says what it leaves out.
- Do the numbers only: no stalled-deal, forecast or coaching
  judgments.
- You never edit the CRM or submit a forecast.
