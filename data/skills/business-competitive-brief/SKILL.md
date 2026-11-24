---
name: business-competitive-brief
description: >-
  Builds a competitor battlecard with the standards of a product manager and
  an account executive. Give it the competitor material as text (pricing
  pages, docs, release notes) and your win/loss and support notes, and it
  writes a one-page battlecard with the positioning trade-offs, where you win
  and lose, objection responses and watch-outs, plus a research list. Use
  when the user asks for a battlecard, a competitor brief or a comparison
  against one competitor.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: business, product, sales, competitive-analysis
---

# Competitive brief

This job builds the battlecard sales reads before a meeting, the way a
small team would: the product manager compares the products on
evidence, and the account executive turns that into answers to what
buyers actually say. The card is quoted all quarter, so every line must
hold up. You turn the competitor material and internal notes in the
conversation into one battlecard and a research list. You have no
browsing: every fact comes from the text given. You never publish the
card, contact a competitor or a buyer, or sign up for a trial.

## Inputs

Required: the competitor's name, their material pasted as text, and
your internal record (win/loss reasons, support themes, objections the
field reported). Optional: the buyer or segment to write for, your own
product's pricing and docs, a known upcoming competitor release.

Ask once, in one message, for anything required that is missing. If
the user names more than one competitor, ask which one; one card covers
one competitor. Without a named segment, write for the buyer the
win/loss notes mention most.

## Steps

1. **Sort the sources.** Label each fact by where it comes from: what
   the competitor states, what buyers reported, what your own data
   shows. A competitor claim that no buyer or data confirms is marked
   unverified.
2. **Positioning (product).** For each strength the competitor claims,
   write their pitch, your counter and the source of the counter. Map
   each to the use case where you win and the one where you lose. Say
   where you lose as plainly as where you win, with the deal or ticket
   behind it.
3. **Objections (sales).** Write a response only for objections seen in
   the material, each in two or three sentences a rep can say out
   loud. Build on step 2; do not add claims it does not support.
4. **Watch-outs.** List what the competitor's release notes or roadmap
   statements suggest is coming, and which counter it would weaken.
5. **Research list.** For each weak spot on the card (an unverified
   claim, a counter with one source), name what to pull next: a buyer
   call, a trial, a pricing check.
6. **Check** the card against the success criteria and fix what fails.

## Success criteria

- Every fact on the card names its source; nothing comes from outside
  the given text.
- Every competitor claim not confirmed by a buyer or your data is
  marked unverified.
- Where you lose is stated, with the evidence behind it, whenever the
  material shows a loss.
- Each objection response answers an objection that appears in the
  material.
- Each research item points at a named weak spot on the card.
- No marketing adjectives for either product.

## Output

In this order: the trade-off table (their pitch, your counter,
source); where you win; where you lose; objection responses;
watch-outs; then, after the card, the research list and data still
needed. The card fits on one page. Plain comparisons, no slogans.

## Handing off a part

When the competitor material is too large to hold with the internal
notes, step 1 for the competitor material may go to a sub-agent that
returns the sorted, sourced claims. Do steps 2 to 5 yourself, since
they weigh both sides together. Otherwise do every step yourself.
