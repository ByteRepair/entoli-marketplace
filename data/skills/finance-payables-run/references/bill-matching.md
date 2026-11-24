# Bill matching

Step 2 of the finance-payables-run skill, run as an `explore`
sub-agent, one per block of vendors. You match one block of bills with
the standards of an accounts payable clerk, and return it to the agent
preparing the payment run.

## Inputs

The files named in your prompt: the bills in scope for your vendors
(vendor, bill number, date, amount, due date), and the PO and receipt
records for the same vendors. Pasted invoices when given.

## Do

1. For each bill with a PO, compare bill, PO and receipt on vendor,
   quantity, price and total.
2. Mark each bill: matched; PO mismatch (name the field and show both
   figures); no receipt (not ready to pay); or no PO.
3. Name the bills you could not check because a record is missing, and
   which record.

## Return

Only this table, one line per bill in your block and no bill twice
(vendor, bill number, amount, PO, receipt, result, the figures that
differ), then a line with the bill count and total for the block, then
data still needed.

## Rules

- Every figure is in the files, as written; nothing is estimated or
  rounded.
- A difference is reported with both figures, never resolved or
  averaged.
- Match only: no duplicate, approval, coding or pay-or-hold judgments.
- You never pay a bill, schedule a payment or change vendor details.
