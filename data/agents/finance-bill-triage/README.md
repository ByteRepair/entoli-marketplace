# Finance Bill Triage

An agent that behaves like a small business's AP clerk: it decides
nothing about pay, but nothing wrong reaches the payment run.

It three-way matches bills against purchase orders and receipts, flags
duplicates and new or changed bank details, suggests coding, and drafts
the payment-run memo the approver can agree or disagree with line by
line. Vendor bank details are always a human verification flag — the
agent never touches them.

## What you get

- An exception report: one line per item, with the issue and the check
  to run.
- Coding suggestions against your chart of accounts.
- The payment-run memo: total, per-vendor list, terms, holds with
  reasons.
- Vendor follow-up drafts, plus the year-end 1099/W-9 sweep table when
  you say this is the run.

## Configuring

Provide the bills export, the PO and receipt records where they exist,
and the approval rules; name the payment run date. No payments are
ever initiated by the agent.
