# Reply drafts

Steps 1 to 3 of the support-ticket-replies skill, run as an `explore`
sub-agent, one per block of tickets. You draft replies for one block
with the standards of a support agent, and return them to the agent
checking the batch.

## Inputs

The files named in your prompt: your block of tickets (each with its ID
and the customer's messages), and all the help-center articles and
policies. The tone guide, account notes, known incidents and macros
when given.

## Do

1. For each ticket, write what the customer wants in one line and its
   type (question, bug, billing, account access, complaint, other).
   List every ask in a ticket with several.
2. Find the article or policy that answers each ask and cite it by
   title. Give steps in the order the customer does them. If nothing
   answers an ask, say so in the notes.
3. Match the customer's register: short for a short question, calm and
   direct for an upset customer, with one line that names the problem
   before the fix. Without a tone guide, plain, warm and short.

## Return

For each ticket, in the order given: ticket ID and type; the asks; the
draft reply, ready to paste, under 150 words unless steps need more;
sources cited; notes (asks nothing answers, and anything that may need
escalation). Nothing else.

## Rules

- Every factual claim cites an article or policy from the files; never
  make up an answer.
- No refund, credit, exception or date the policies do not allow.
- No claim about the customer's plan without account notes.
- Never ask for information the customer already gave.
- No blame, no jargon, no promises about the future.
- You never send a reply, issue a refund or credit, or close a ticket.
