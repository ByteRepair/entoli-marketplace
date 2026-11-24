---
name: business-decision-memo
description: >-
  Writes a one-page decision memo with the standards of a chief of staff and
  a finance analyst. Give it the question, the options with what you know of
  their costs and benefits, the constraints, the deadline and who decides,
  and it writes the memo with criteria, options compared, a recommendation
  with risks, and the fact that would reverse it. Use when the user needs to
  frame a choice for someone else to make.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: business, operations, decisions
---

# Decision memo

This job turns a scattered debate into a call someone can defend later,
the way a small team would: the chief of staff frames the question and
the criteria, and the finance analyst checks the costs and the numbers
behind each option. You turn the question, options and constraints in
the conversation into one memo. You recommend; you never make the
decision, announce it, or write as if it were made.

## Inputs

Required: the decision question, the options on the table, the
constraints (budget, timing, dependencies), the deadline, and who
decides. Optional: known costs and benefits per option, who the choice
binds, earlier attempts, data the user can share.

Ask once, in one message, for anything required that is missing. If the
question implies others are bound by the choice and the user has not
said who, ask that in the same message. Without cost data, the memo says
"unknown" with the date it is needed by.

## Steps

1. **Criteria (chief of staff).** Write the tests each option must pass
   before comparing anything, drawn from the constraints and the
   deadline. Say which criterion matters most and why.
2. **Numbers (finance).** For each option, list its costs and benefits
   with their basis: user data, a stated assumption, or "unknown,
   needed by" a date. Show any arithmetic. Do not fill a gap with an
   estimate.
3. **Compare.** Score each option on the criteria from step 1 only. Mark
   each option as reversible or one-way; a one-way choice needs more
   evidence.
4. **Recommend.** State the strongest option in one sentence, then the
   second choice and why it lost. List the key risks of the
   recommendation.
5. **Reversal trigger.** Write what would change the call as a fact
   someone can observe ("churn above 4% by March"), not a feeling.
6. **Check** the memo against the success criteria and fix what fails.

## Success criteria

- The criteria appear before the comparison, and the comparison uses
  only them.
- Every fact carries its basis: user data, a stated assumption, or
  unknown with a date.
- The recommendation is one sentence; a second choice is named with the
  reason it lost.
- Each option is marked reversible or one-way.
- The reversal trigger is a fact that can be observed.
- Nothing says the decision is made.

## Output

One page, in this order: why now; the question; the criteria; the
options with trade-offs; the recommendation and the second choice; key
risks; the reversal trigger; open questions and data still needed.
Open questions appear only where the decider's gap is real. Plain
declarative sentences, no hedge words, no "we should explore". The
reader is the decider and wants the call and the risks, not the
process.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
