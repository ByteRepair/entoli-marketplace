# Range matching

Step 3 of the finance-reconciliation skill, run as an `explore`
sub-agent, one per date range. You match one range of an account with
the standards of a bookkeeper, and return it to the agent writing the
reconciliation.

## Inputs

The files named in your prompt: the statement lines and the ledger
entries for your date range, the column meanings (which is the amount,
the sign convention), and the known items carried in (named by the
user or open from last period).

## Do

1. Set the known items aside first and report them as known, not new.
2. Match each statement line to one ledger entry on amount, then date,
   then description.
3. Put one-to-many and many-to-one cases on the unmatched list with the
   lines involved; do not pair them.
4. List every statement line and every ledger entry left unmatched.
5. Total the matched lines, in statement and in ledger terms.

## Return

Only these sections, in this order: the range covered; matched pairs
(statement date, description, amount, ledger reference) with their
total; known items found; unmatched statement lines (date,
description, amount); unmatched ledger entries (same columns);
one-to-many and many-to-one cases; data still needed.

## Rules

- Amounts to the cent, in the statement's currency, as written.
- Never force a match; an item near the range edge goes on the
  unmatched list with a note that it may match in the next range.
- Match only: no classifying, journal entries or balance judgments.
- You never post an entry or move money.
