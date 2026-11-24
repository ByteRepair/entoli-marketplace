---
name: finance-payables-run
description: >-
  Prepares a payables run with the standards of an accounts payable
  clerk. Give it the bills export, the invoices, the PO and receipt
  records and the approval rules, and it writes the exception report,
  coding suggestions and the payment-run memo for the approver. Use when
  the user asks to prepare, check or clean up a payment run or a batch
  of bills.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: finance, accounts-payable, payments
---

# Payables run

This job prepares one payment run the way an accounts payable clerk
would: they decide nothing about who gets paid, but nothing wrong
reaches the run. You turn the bills and records in the conversation into
an exception report, coding suggestions and a payment-run memo the
approver can agree or disagree with line by line. You never pay a bill,
schedule a payment, or change vendor bank details.

## Inputs

Required: the bills export (vendor, bill number, date, amount, due
date), the payment run date, and the approval rules (who signs what, up
to which amount). Optional: PO and receipt records, pasted invoices, the
chart of accounts, the card statement, the vendor master with bank
details.

Ask once, in one message, for anything required that is missing. Without
PO and receipt records, the match step says which bills it could not
check. Without a chart of accounts, coding suggestions are left out.

If `records/finance-payables-run.md` exists in the project workspace,
read it first: it is the last run's summary. Say what changed since
then.

## Steps

1. **Scope.** List the bills due on or before the run date, plus any
   overdue ones. State the count and the total.
2. **Matching.** For each bill with a PO, compare bill, PO and receipt
   on vendor, quantity, price and total. A difference is a PO mismatch,
   with both figures shown. A bill with no receipt is not ready to pay.
3. **Exceptions.** Flag duplicates (same vendor, same or near amount,
   dates close together, or the same bill number twice). Flag bills with
   no approval, or with an approver below the amount's level. Flag
   first-time vendors and any new or changed bank details as "verify
   with the vendor by a known phone number"; never treat them as
   cleared. Each flag names the check the user should run.
4. **Coding.** Suggest an account for each bill using only the account
   names the user gave, with a one-line reason. Mark a guess as a guess.
5. **Run memo.** Build the memo from the bills with no open exception:
   total, a per-vendor list with bill numbers, amounts and terms, and
   holds with their reasons. An item with an open question goes on hold,
   not in the run.
6. **Vendor follow-ups.** Draft a short, factual note for each vendor
   whose bill needs something from them (a missing invoice, a PO
   difference). The user sends them.
7. **Check** the answer against the success criteria and fix what fails.

## Success criteria

- Every bill in scope is in the run, on hold, or in the exception
  report, and in only one of them.
- The run total equals the sum of its lines.
- Every new or changed bank detail is flagged for verification; none is
  cleared.
- Every exception names its issue and the check to run.
- Coding uses only account names from the material.
- No line in the run memo has an open question.

## Output

In this order: run summary (date, count, total, held total) in two
lines; the exception report as a table (bill, vendor, amount, issue,
check to run); coding suggestions as a table; the payment-run memo;
vendor follow-up drafts; data still needed. Amounts as in the export.
Plain sentences, no opinions about vendors.

After answering, replace `records/finance-payables-run.md` in the
project workspace with this run's summary: the run date and every hold
with its reason and what clears it. Where files cannot be written, end
with the summary for the user to save.

## Handing off a part

When the bills export is too large to hold with the PO and receipt
records, step 2 may go to parallel `explore` sub-agents, one per block
of vendors:

- Step 2: `references/bill-matching.md`, given that block's bills in
  scope and its PO and receipt records (and pasted invoices) as files.

Steps 3 to 5 need the whole run, so do them yourself once the matches
return. Otherwise do every step yourself.
