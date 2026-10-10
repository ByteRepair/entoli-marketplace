# Fashion Collection Planner

An agent that behaves like a fashion label's merchandiser: it turns
last season's numbers and this season's targets into a line plan the
design team can execute and sales can sell.

Working about two seasons ahead of the delivery calendar (SS/FW, plus
resort and pre-fall, with market weeks between), it sizes each category
against what actually sold at which price tier, keeps the carryover
that still sells, and flags the months where the plan would break the
budget.

## What you get

- A line plan: categories with style counts, price tiers, and the
  newness versus carryover split.
- Open-to-buy notes by month with the assumptions behind them.
- A line-review memo: the architecture paragraph, the cut list with
  reasons, the add list with the holes they fill, and the open
  questions for design and sales.

## Configuring

Name the delivery season, attach last season's sell-through, and set
the targets in the launching message. Without the sell-through it plans
from the brief alone and marks the plan "unvalidated by history".
