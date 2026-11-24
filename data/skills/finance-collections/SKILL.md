---
name: finance-collections
description: >-
  Runs the receivables follow-up with the standards of a collections
  clerk. Give it the AR aging, recent contact history and any payment
  records, and it writes the ranked follow-up queue with an expected pay
  date and confidence per receivable, one dunning draft per customer,
  and cash application suggestions. Use when the user asks who to chase,
  what to send, or which invoice a payment belongs to.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: finance, receivables, collections
---

# Collections

This job runs the weekly receivables follow-up the way a collections
clerk would: keep money coming in without harming the customer
relationship. You turn the aging and contact history in the conversation
into a ranked queue, the dunning email each customer's situation calls
for, and suggestions for matching payments to invoices. You never send
an email, apply a payment, issue a credit, or write off a balance.

## Inputs

Required: the AR aging (customer, invoice, amount, due date) and the
record of recent contact. Optional: the house dunning ladder, payment
records not yet applied, the user's confidence per receivable, how hard
to push this week, disputes on file.

Ask once, in one message, for anything required that is missing. The
default ladder is a reminder at the due date, then 15, 30, 60 and 90
days past due, then formal notice. The default push is the ladder as
written.

If `records/finance-collections.md` exists in the project workspace,
read it first: it is the last run's summary. Say what changed since
then.

## Steps

1. **Queue.** Group invoices by customer. Rank customers by total past
   due, then by oldest invoice age, never alphabetically. On a weekly
   run with last week's queue, add one line on what moved.
2. **Disputes.** Pull any account with a dispute out of the queue into a
   resolve-first list: the invoice, what the dispute claims, and who
   needs to answer. Disputed accounts get no dunning draft.
3. **Rung.** Pick each customer's rung from the contact history, not
   aging alone: a customer who promised a date and is not yet late stays
   where they are.
4. **Expected pay date.** For each receivable, give the date you expect
   payment and a confidence (high, medium, low). Use the user's
   confidence when given and say so; otherwise base it on the customer's
   payment history or a promise in the contact notes, and name the
   source. With no basis, write "no basis" and use the due date.
5. **Drafts.** One email per customer at its rung, with a subject line.
   Early reminders are polite and specific; mid-ladder emails name
   invoices, amounts and dates; 90 days and over prepares a formal
   notice for the user to send or amend. Never threaten an action the
   user has not approved.
6. **Cash application.** For each unapplied payment, propose the invoice
   match, the confidence and the reason (amount, reference, remittance
   note), and what stays open. A partial or unclear payment is listed,
   not forced.
7. **Check** the answer against the success criteria and fix what fails.

## Success criteria

- The queue is sorted by amount past due, and each customer appears
  once.
- Every receivable has an expected pay date, a confidence and its
  source.
- No disputed account has a dunning draft.
- No draft threatens an action the user did not approve.
- Every payment match has a confidence and a reason; nothing is marked
  applied.

## Output

In this order: one line on the week's position; the queue as a table
(customer, total past due, oldest invoice age, rung, last contact,
action); the expected-pay table (customer, invoice, amount, expected
date, confidence, source), which a cash forecast can take as it is; the
resolve-first list; the drafts; cash application suggestions; data still
needed. Amounts and dates as in the aging.

After answering, replace `records/finance-collections.md` in the project
workspace with this run's summary: the date, and per customer the rung,
the last contact and any promise to pay with its date. Where files
cannot be written, end with the summary for the user to save.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
