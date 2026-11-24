---
name: finance-reconciliation
description: >-
  Reconciles one account for one period with the standards of a bookkeeper.
  Give it the bank, card or payout statement export and the ledger export,
  and it writes the match report, the exception list with likely causes, and
  draft correcting journal entries. Use when the user asks to reconcile an
  account or explain why the bank and the books disagree.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: finance, bookkeeping, reconciliation
---

# Reconciliation

This job reconciles one account for one period the way a bookkeeper
would: close the gap between what the bank says and what the books say,
and state any gap left exactly. You turn the statement and ledger
exports in the conversation into a match report, an exception list and
draft journal entries for a person to enter. You never post an entry or
move money.

## Inputs

Required: the account, the period, the statement export and the ledger
or register export for that account. Optional: items the user already
knows about (deposits in transit, pending card charges, known fees),
last period's reconciliation, the chart of accounts.

Ask once, in one message, for anything required that is missing. If the
files cover several periods, ask which one. If a file's columns are
unclear (which column is the amount, the sign convention), ask before
reading it, in the same message.

## Steps

1. **Balances.** State the statement's opening and closing balances and
   the ledger's balance at the same dates.
2. **Known items.** Carry the items the user already named, and open
   items from last period, through first, so they are not reported as
   new.
3. **Matching.** Match statement lines to ledger entries on amount, then
   date, then description. One-to-many and many-to-one cases go to the
   exception list; never force a match.
4. **Exceptions.** Classify each unmatched item as timing, missing entry,
   duplicate, miscoded, or bank error, with the evidence for it. If the
   evidence does not settle it, say "unclear" and name what would.
5. **Journal entries.** Draft one entry per correction: date, accounts
   (debit and credit, named as the user names them), amount, and a memo
   naming the statement line it came from. Timing items get no entry.
6. **Difference.** Show adjusted bank balance against adjusted book
   balance, and state any remaining difference to the cent. A remainder
   is stated, never smoothed or plugged.
7. **Check** the answer against the success criteria and fix what
   fails.

## Success criteria

- Opening balance plus matched and listed items equals the closing
  balance, or the remaining difference is stated exactly.
- Every statement line is matched or on the exception list.
- Every exception has a class and its evidence, or is marked unclear.
- Every journal entry balances and names its source line.
- No journal entry is a plug for an unexplained difference.

## Output

In this order: the result in one line (reconciled, or off by an exact
amount); balances; matched totals; the exception list as a table
(date, description, amount, class, likely cause), one line per item;
draft journal entries; the remaining difference; data still needed.
Account names as the user writes them. Amounts in the statement's
currency and rounding.

## Handing off a part

When the statement and ledger are too large to hold together, step 3
may go to parallel `explore` sub-agents, one per date range:

- Step 3: `references/range-matching.md`, given both exports for that
  range, the column meanings and the known items from step 2 as files.

Do steps 1 and 2 first. Steps 4 to 6 need the whole period, so do them
yourself once the matches return, pairing items left unmatched at the
range edges. Otherwise do every step yourself.
