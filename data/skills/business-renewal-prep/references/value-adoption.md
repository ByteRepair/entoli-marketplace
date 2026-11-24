# Value and adoption

Step 2 of the business-renewal-prep skill, run as an `explore`
sub-agent. You do one part of a renewal memo with the standards of a
customer success manager, and return it to the agent writing the memo.

## Inputs

The files named in your prompt: the goals the customer bought for, the
usage data, and the meeting notes. Support tickets when given.

## Do

1. For each goal: the evidence from the files, then a verdict — met,
   partly, not met, or no data.
2. Tie every usage number to the goal it serves, in the customer's
   terms (their hours, their metric).
3. List the adoption gaps by team or site, with the numbers behind
   each.
4. When two sources disagree (an export and a remark in a meeting),
   report both and say they disagree.

## Return

Only these sections, in this order: goals (one line each: goal,
evidence, verdict); adoption gaps (one line each); disagreements between
sources; data still needed.

## Rules

- Every number is in the files or shown as arithmetic on them; nothing
  is estimated.
- "No data" where the data is absent, never a guess.
- Judge adoption only: no price, contract or roadmap judgments.
- You never contact the customer.
