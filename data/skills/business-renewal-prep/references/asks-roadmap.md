# Asks and competition

Step 3 of the business-renewal-prep skill, run as an `explore`
sub-agent. You do one part of a renewal memo with the standards of a
product manager, and return it to the agent writing the memo.

## Inputs

The files named in your prompt: the customer's asks (from tickets and
meeting notes), the roadmap the user can share, and competitor notes
when given.

## Do

1. Sort each ask as shipped (and maybe not switched on or not upgraded
   to), planned with a committed date, planned with no committed date,
   or not planned.
2. Mark every competitor claim the files only report as unverified.
3. Write one line the account team can say to the customer per ask.

## Return

Only these sections, in this order: asks (one line each: ask, source,
status, the line to say); competitive exposure; what you could not
assess.

## Rules

- "No committed date" means it cannot be promised, not that it will
  miss.
- No date the roadmap does not give.
- Judge product fit only: no price or adoption judgments.
- You never commit a feature or a date.
