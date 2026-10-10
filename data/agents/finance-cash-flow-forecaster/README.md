# Finance Cash Flow Forecaster

An agent that behaves like a small company's treasury desk: it always
knows what cash is where and when the tight weeks land.

It builds the rolling 13-week direct cash flow forecast from bank
balances, payables terms, receivables under your collection
confidence, and the fixed calendar (payroll, rent, tax, debt service).
Each update also gets the bridge narrative — what changed since last
week and why. It never moves money or draws credit; shortfall actions
are proposals.

## What you get

- The 13-week forecast table by week, with the opening balances and
  week numbering stated.
- The weekly bridge narrative, real deltas only.
- Shortfall notes: the week, the low point, the causes, and two or
  three tagged proposals.
- The low-cash case shown whenever an inflow is uncertain.

## Configuring

Provide the bank balances, the AP export, the AR aging with your
confidence, and the fixed dates. Say which week the forecast starts
on.
