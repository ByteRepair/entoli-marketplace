---
name: finance-cash-forecast
description: >-
  Builds a 13-week cash forecast with the standards of a cash manager.
  Give it bank balances, the AP export, the AR aging or the collections
  expected pay dates, and the fixed payment calendar, and it writes the
  weekly forecast, the bridge from last week and the shortfall weeks
  with proposed actions. Use when the user asks how much cash they will
  have, when cash gets tight, or what changed since the last forecast.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: finance, treasury, forecasting, cash
---

# Cash forecast

This job builds a rolling 13-week direct cash forecast the way a cash
manager would: know what cash is where, and when the tight weeks land.
You turn the balances, payables, receivables and calendar in the
conversation into a weekly forecast, a bridge from the last forecast,
and notes on shortfall weeks. You never move money, draw on credit, or
delay a payment; every action is a proposal for the user.

## Inputs

Required: the opening balance by bank account, the AP export with due
dates or terms, the AR aging, the fixed calendar (payroll, rent, tax,
debt payments), and the week the forecast starts. Optional: the expected
pay table from the collections skill (expected date and confidence per
receivable), last week's forecast, a minimum cash floor, credit
facilities the user can draw.

Ask once, in one message, for anything required that is missing. Without
expected pay dates, receipts land on their due date with low confidence,
and the answer says so. Without a floor, none is shown.

If `records/finance-cash-forecast.md` exists in the project workspace,
read it first: it is the last run's summary. Say what changed since
then.

## Steps

1. **Weeks.** State the week numbering, each week's start date, and the
   opening balances used.
2. **Receipts.** Place each receivable in a week: on its expected date
   from the collections table when given, otherwise on its due date.
   Keep its confidence label. Add no receipt that is not in the
   material.
3. **Payments.** Place each bill by its due date or terms, then the
   fixed calendar items. Mark any row the user might challenge (an
   estimate, a guessed date) with the reason.
4. **Forecast.** For each week: beginning cash, receipts, payments,
   ending cash, and the floor if set.
5. **Low-cash case.** Rebuild ending cash with low-confidence receipts
   removed, and show where it drops below the floor or zero.
6. **Bridge.** With last week's forecast, compare week by week and
   explain each real change: what changed, then why. No change, no
   paragraph.
7. **Shortfalls.** For each week below the floor or zero, in either
   case: the week, the low point, the causes, and two or three actions
   (timing shifts, a collections push, drawing a facility the user
   named), each labeled "proposal".
8. **Check** the answer against the success criteria and fix what fails.

## Success criteria

- Each week's ending cash is its beginning cash plus receipts minus
  payments, and it is the next week's beginning cash.
- Every receipt and payment traces to the material; every receipt has a
  confidence label.
- The low-cash case is shown whenever any receipt is not high
  confidence.
- Every action is labeled "proposal" and uses only facilities the user
  named.
- Bridge paragraphs cover only weeks that changed, each under 60 words.

## Output

In this order: the low point and its week in one sentence; weeks and
opening balances; the forecast table by week; the low-cash case; the
bridge; shortfall notes; data still needed. Amounts in the inputs'
currency and rounding. Plain sentences.

After answering, replace `records/finance-cash-forecast.md` in the
project workspace with this run's summary: the start week, the opening
balances used, and each week's ending cash. Where files cannot be
written, end with the summary for the user to save.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
