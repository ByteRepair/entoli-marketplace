# Finance Close Coordinator

An agent that behaves like a controller's close coordinator: for the
first working days of the month it keeps the month-end close moving and
the package narrative ready.

It tracks the close checklist (transactions cutoff, subledger close,
recurring journals, reconciliations, review reports, package), orders
the outstanding items by dependency, chases what is missing, and drafts
the summary memo. It never posts, locks, or signs — the controller
closes the books.

## What you get

- A status tracker: step, owner, status, blocker.
- The outstanding list with owners, close-day targets, and what
  unblocks each item.
- The summary memo: results in your numbers, movement with reasons,
  exceptions, and what to verify before sign-off.
- The package narrative in plain sentences when you reach packaging.

## Configuring

Give the checklist (yours or the standard flow), what is done so far,
and the period, and say how far into the timetable you are. Every
"done" traces to something you reported.
