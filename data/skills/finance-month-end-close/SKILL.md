---
name: finance-month-end-close
description: >-
  Runs the month-end close with the standards of a close coordinator and
  an FP&A analyst. Give it the close checklist, what is done so far, the
  P&L export and the budget or prior period, and it writes the close
  tracker, the outstanding list with owners, the variance table and the
  flux memo. Use when the user asks where the close stands, what is
  blocking it, or why the month's numbers moved.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: finance, accounting, month-end-close, fp-and-a
---

# Month-end close

This job runs one month's close the way a small finance team would: the
close coordinator keeps the steps moving and the blockers visible, and
the FP&A analyst explains why the numbers moved against the plan. You
turn the checklist, status notes and exports in the conversation into a
close tracker, an outstanding list, a variance table and a flux memo.
You never post an entry, lock a period, sign off the close, or change a
forecast.

## Inputs

Required: the period, the close checklist or the steps done so far, the
status of each step, and the P&L export for the period. Optional: the
comparison basis (budget, prior year or prior forecast), the materiality
threshold, events the user knows about (hires, contracts, price
changes), items carried from last month, the close day today.

Ask once, in one message, for anything required that is missing. Without
a checklist, use the standard order: cutoff, subledger close, recurring
journals, reconciliations, review, reporting. Without a comparison
basis, use the prior month. Materiality defaults to a 10% variance and
an absolute floor the answer states.

If `records/finance-month-end-close.md` exists in the project workspace,
read it first: it is the last run's summary. Say what changed since
then.

## Steps

1. **Tracker (close coordinator).** Give every step a status (done, in
   progress, waiting on a named role, not started), an owner and any
   blocker. "Done" only when the user reported it done. Keep recurring
   and closing entries apart.
2. **Outstanding list (close coordinator).** Order open items by
   dependency: cutoff before subledgers, subledgers before
   reconciliations, reconciliations before review. Each item gets an
   owner, a close-day target and what unblocks it. An unknown status is
   an ask with a day number.
3. **Variances (FP&A analyst).** Compute actual against the basis for
   each line: amount and percent, favorable or unfavorable. Keep only
   material lines; sum the rest in one line.
4. **Drivers (FP&A analyst).** Split each material variance into
   drivers: price or volume, one-off or run-rate, timing or real. Tie a
   driver to a stated event only where it fits. Otherwise write
   "unexplained"; never invent a driver.
5. **Close caveat.** If steps that feed the P&L (accruals,
   reconciliations) are still open, say the variances may move and name
   those steps.
6. **Check** the answer against the success criteria and fix what fails.

## Success criteria

- Every checklist step has a status and an owner; every "done" traces to
  the user's report.
- Every open item has an owner, a close-day target and what unblocks it.
- Variances are actual minus basis, and the material lines plus the
  remainder add up to the P&L total.
- Every material variance has a driver tied to evidence or is marked
  unexplained.
- No one-off month is annualized, and no line is reclassified.

## Output

In this order: close status in one sentence (on track, at risk, or late,
and why); the tracker as a table (step, owner, status, blocker); the
outstanding list as a table; the variance table (line, actual, basis,
variance, percent, favorable or unfavorable), sorted by size; the flux
memo, one short paragraph per material variance a reader can follow
without the spreadsheet; what the controller should check before
sign-off; data still needed. Rounding and units as in the inputs.

After answering, replace `records/finance-month-end-close.md` in the
project workspace with this run's summary: the period, the items carried
open, and each material variance with its driver. Where files cannot be
written, end with the summary for the user to save.

## Handing off a part

Steps 1 and 2 and steps 3 and 4 are independent and may run as parallel
`explore` sub-agents when the checklist material and the P&L detail are
too large to hold together:

- Steps 1 and 2: `references/close-tracker.md`, given the period, the
  checklist and the status notes (and carried items and the close day)
  as files.
- Steps 3 and 4: `references/variance-drivers.md`, given the P&L export
  and the comparison basis (and the materiality threshold and known
  events) as files.

Step 5 needs both, so do it yourself once they return. Otherwise do
every step yourself.
