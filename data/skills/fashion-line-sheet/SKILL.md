---
name: fashion-line-sheet
description: >-
  Writes a fashion label's wholesale selling papers with the standards of
  showroom sales support. Give it the style list with exact wholesale and
  MSRP, minimums, size runs, colorways and delivery windows, plus meeting
  notes if you want follow-ups, and it writes the line-sheet copy, price
  list, order-form text and buyer follow-up emails. Use when the user
  asks for a line sheet, price list, order form or post-market
  follow-ups.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: fashion, wholesale, sales
---

# Line sheet

This job writes the papers buyers order from between the showroom visit
and the written order, with the standards of the label's wholesale
sales support. You turn a style list into line-sheet copy, a price list,
order-form text and follow-up emails. You write only what the
conversation gives you: no price, minimum or date is invented. You
never set a price and never send an email; the user sends them.

## Inputs

Required: per style, the name, category, exact wholesale and MSRP,
minimum order, size run and colorways; and the cutoff dates and
delivery windows. Optional: a selling description or fabric facts per
style, the audience (market week, standing accounts, trade show), and
meeting notes per buyer for follow-ups.

Ask once, in one message, for anything required that is missing. If the
prices are ranges (a line plan gives tiers, not prices), ask for the
exact price per style; never pick one inside a range. The default
audience is market week. Without meeting notes, write no follow-ups.

## Steps

1. **Style copy.** Three to five lines per style: what it is, fabric
   and care, the fit note, one selling point. Facts, not adjectives:
   "brushed organic cotton fleece", not "luxuriously soft". A fact not
   given is left out, not guessed.
2. **Price list.** One table: style, colorways, wholesale, MSRP, MOQ.
   Check every price matches the style copy and the inputs exactly.
3. **Order papers.** One cutoff and delivery block per delivery window,
   so minimums and cutoffs sit in one place. The order-form text lists
   what the buyer must state: style, colorway, size run, units,
   ship-to, with the cutoff beside it. Check the delivery wording
   against the season calendar the user gave; ask which one when it is
   unclear.
4. **Follow-ups.** One email per buyer or market from the meeting
   notes: a subject line, under 120 words, asking for the written order
   and restating the cutoff.
5. **Check** the papers against the success criteria and fix what fails.

## Success criteria

- Every price, minimum and date matches the inputs exactly; none is a
  pick from a range.
- Each style has three to five lines of copy and no adjective without a
  fact behind it.
- The price list has every style once, with all five columns.
- Each delivery window has one cutoff and delivery block, and the
  order form names the cutoff.
- Each follow-up has a subject, is under 120 words, asks for the
  written order and restates the cutoff.

## Output

In this order: line-sheet copy per style; the price list table; cutoff
and delivery blocks; order-form text; follow-up drafts; data still
needed. These are skimming papers: short lines, no repeated facts. The
style copy is the input product copy can start from.

## Handing off a part

The follow-up emails may go to a sub-agent when there are many buyers,
briefed with step 4, each buyer's notes and the cutoff block. Do the
copy, price list and order papers yourself so the numbers stay in one
place.
