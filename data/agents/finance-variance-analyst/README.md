# Finance Variance Analyst

An agent that behaves like a company's FP&A analyst: it writes the
monthly budget-versus-actual story the owner and board actually read.

It computes the variances, splits them into drivers (price or volume,
one-off or run-rate, timing or real), and writes a flux memo a reader
who never sees the spreadsheet follows. Unexplained variances say so
outright — no driver is invented. It explains the books; it never
restates them.

## What you get

- A variance table sorted by magnitude, material items only, with the
  immaterial remainder summed.
- A flux memo, one paragraph per material variance, each driver either
  evidenced or marked unexplained.
- A watch list: recurring accounts, questions for the controller, and
  the data that would settle them.

## Configuring

Provide the P&L export, the comparison basis (budget, prior year, or
prior forecast), and the events you know happened. Set your
materiality threshold — the default is 10% variance with a stated
absolute floor.
