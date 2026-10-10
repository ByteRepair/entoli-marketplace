# Finance Reconciliation Preparer

An agent that behaves like a small business's bookkeeper: it closes the
gap between what the bank says and what the books say.

It matches a statement export against a ledger export (QuickBooks,
Xero, or plain CSV), classifies every exception — timing, missing
entry, duplicate, miscoding, bank error — and drafts the correcting
journal entries for you to enter. It never posts anything anywhere.

## What you get

- A reconciliation report that foots: opening and closing balances,
  matched totals, and the unexplained difference stated exactly.
- An exception list with the likely cause per item.
- Draft journal entries, one per correction, with the source named.

## Configuring

Provide the statement export, the ledger export, and the period, and
say what you already know (deposits in transit, pending cards).
Ambiguous file formats get a question before they get a parse.
