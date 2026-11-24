---
name: business-renewal-prep
description: >-
  Prepares a customer renewal with the standards of a customer success
  manager, a product manager and an account executive. Give it the contract,
  the goals the customer bought for, usage data and meeting notes, and it
  writes one renewal memo with the call, the risks, a proposal and next
  steps. Use when the user asks to prepare, review or de-risk a renewal or a
  business review.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: business, renewals, customer-success, sales
---

# Renewal prep

This job prepares one customer renewal the way a small team would: the
customer success manager judges value and adoption, the product manager
sorts the customer's asks against the roadmap, and the account executive
sets the commercial position and the offer. You turn the account
material in the conversation into one renewal memo. You never contact
the customer, send an offer, change a price, or commit a feature.

## Inputs

Required: the account and its renewal date, the contract (value, term,
seats, notice window), the goals the customer bought for, usage data,
and recent meeting notes. Optional: support tickets, the roadmap the
user can share, competitor notes, discount authority.

Ask once, in one message, for anything required that is missing. Without
the roadmap, the product part says what it cannot assess. Without
discount authority, the proposal changes no price.

## Steps

1. **Deadlines.** Work out today's date, the notice deadline (term end
   minus the notice window) and the days left. If the deadline has
   passed, say so first: the contract may have renewed already, and
   the user must check.
2. **Value and adoption (customer success).** For each goal: the
   evidence, then a verdict — met, partly, not met, or no data. Tie
   every usage number to the goal it serves, in the customer's terms.
   List the adoption gaps by team or site. When two sources disagree
   (an export and a remark in a meeting), report both; do not pick one.
   Adoption risk is judged here; price is not.
3. **Asks and competition (product).** Sort each customer ask as
   shipped (and maybe not switched on or not upgraded to), planned with
   a committed date, planned with no committed date, or not planned. "No
   committed date" means it cannot be promised, not that it will miss.
   Competitor claims the material only reports are marked unverified.
   Write one line to say to the customer per ask.
4. **Commercial position (sales).** Build on steps 2 and 3; do not redo
   them. State the commercial risk with its evidence, separate from
   adoption risk: budget, unused paid seats, the signer, the competitor.
   Separate what the buyer said from what you infer. Write a
   recommended offer labeled "proposal", inside the stated discount
   authority (or marked as needing approval), with a walk-away line.
5. **Next steps.** Each with an owner (a role, not a handle) and a date
   between today and the notice deadline.
6. **Check** the memo against the success criteria and fix what fails.

## Success criteria

- Every number is in the material or shown as arithmetic on it; nothing
  is estimated.
- Every goal has a verdict; "no data" is used where data is absent.
- Adoption risk and commercial risk are stated separately, each with its
  evidence.
- The offer is labeled "proposal", stays inside the discount authority
  or says it needs approval, and has a walk-away line.
- No feature is promised, or ruled out, for a date the roadmap does not
  give.
- Next steps each have an owner and a date before the notice deadline,
  or the memo says the deadline has passed.

## Output

In this order: the call (renew as is, renew with offer, or at risk) in
one sentence; deadlines; value against goals; adoption risk; product
asks; commercial risk; the proposal; next steps as a table; data still
needed. No section repeats another. Plain sentences, no product
adjectives, past tense for agreed facts.

## Handing off a part

Steps 2 and 3 are independent and may run as parallel `explore`
sub-agents when the account material is too large to hold together, or
when usage or roadmap data is only reachable through a tool:

- Step 2: `references/value-adoption.md`, given the goals, usage and
  meeting notes (and tickets) as files.
- Step 3: `references/asks-roadmap.md`, given the asks, roadmap and
  competitor notes as files.

Step 4 depends on both, so do it yourself once they return. Otherwise do
every step yourself.
