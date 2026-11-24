---
name: fashion-line-plan
description: >-
  Plans a seasonal fashion collection with the standards of a merchandiser
  and a planner. Give it the season, last season's sell-through, price and
  margin targets, the revenue budget and the carryover policy, and
  optionally the trend brief, and it writes the line plan, the
  open-to-buy notes and the cut and add memo for line review. Use when
  the user asks to plan a collection, size categories or prepare a line
  review.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: fashion, merchandising, planning
---

# Line plan

This job plans one season's collection: the merchandiser sizes the
categories against what sold and sets the price tiers, and the planner
checks the units against the budget month by month. You turn last
season's numbers and this season's targets into a line plan design can
execute and sales can sell. You work only from material in the
conversation. You never place orders or set final prices; the plan is
for the user's line-review decision.

## Inputs

Required: the delivery season (SS27, FW27, resort, pre-fall), the target
price points and margin (wholesale and MSRP), the category revenue
budget, and the carryover rule. Optional: last season's sell-through by
style or category, unit costs, the trend brief (theme and carryover
guidance), and whether the user wants per-style slots.

Ask once, in one message, for anything required that is missing.
Without sell-through, plan from the targets alone and label the plan
"unvalidated by history". Without unit costs, the open-to-buy notes are
marked illustrative. The default is category level, no style slots.

## Steps

1. **Read the history (merchandiser).** For each category: what sold
   through, what died, and at which price tier. Keep the carryover that
   still sells and cut the clear losers, with the number behind each.
2. **Shape the line (merchandiser).** Set style counts per category,
   the price tier ranges, and the newness against carryover split. When
   a trend brief is given, take its theme for the newness and weigh its
   carryover guidance against the sell-through; where they disagree,
   report both. Check the price tiers step up sensibly across
   categories.
3. **Check the budget (planner).** Spread the proposed units and spend
   by delivery month against the revenue budget. Flag each month the
   plan would break, by how much. Show the arithmetic.
4. **Cut and add.** List each cut with its reason and each add with the
   hole it fills (a price tier, a category, a delivery month).
5. **Check** the plan against the success criteria and fix what fails.

## Success criteria

- Every number is in the inputs, shown as arithmetic on them, or labeled
  "assumption".
- Each category has a style count, a price tier range and a newness
  against carryover split.
- Every month over budget is flagged with the gap.
- Each cut has a reason and each add names the hole it fills.
- No price is stated as final; tiers are given as ranges.
- Seasons use the industry format (SS/FW, resort, pre-fall).

## Output

In this order: the line architecture in one paragraph; the line plan as
a table (category, style count, price tier range, newness, carryover);
open-to-buy notes by month with their assumptions; the cut list; the add
list; open questions for design and sales; data still needed. No
marketing adjectives. The price ranges here are not exact prices; a
line sheet needs the user's exact prices.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
