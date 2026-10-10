# Finance Collections Clerk

An agent that behaves like a small business's collections clerk: it
keeps money moving without burning relationships.

It ranks open receivables by amount and days past due, picks each
customer's dunning rung from your contact history rather than aging
alone, and drafts the email that rung calls for — polite early,
specific and firm mid-ladder, formal-notice prep at 90+. Disputed
accounts stay off the automatic path. It drafts; you send.

## What you get

- A ranked queue table: customer, total past due, oldest invoice,
  rung, last contact, action.
- One draft email per customer, escalating with the rung, subject line
  included.
- Cash-application suggestions from any payment records you supply.
- A resolve-first list for disputed accounts.

## Configuring

Provide the AR aging export and your recent contact history. State
your ladder if you have one (the standard spacing is the due date,
then 15, 30, 60, 90+) and how hard to push this week. Nothing is
credited, written off, or sent by the agent.
