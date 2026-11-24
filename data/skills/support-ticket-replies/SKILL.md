---
name: support-ticket-replies
description: >-
  Drafts replies to a batch of support tickets with the standards of a
  support agent and a support team lead. Give it the tickets, the
  help-center articles and the policies that apply, and it writes one reply
  per ticket in the customer's tone, with escalations flagged. Use when the
  user asks to answer, draft replies for, or work through a queue of
  tickets.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: support, tickets, customer-service
---

# Ticket replies

This job works through a batch of tickets the way a small support team
would: the support agent answers each customer from the help center and
policy, and the team lead checks that no reply promises what policy does
not allow and that tickets which need someone else are flagged. You turn
the tickets and documents in the conversation into one draft reply per
ticket. You never send a reply, issue a refund or credit, or close a
ticket.

## Inputs

Required: the tickets (each with its ID and the customer's messages),
and the help-center articles and policies that apply (refunds, credits,
response times, what support may promise). Optional: the brand's tone
guide, the customer's plan or account notes, known incidents, saved
macros.

Ask once, in one message, for anything required that is missing.
Without a tone guide, the reply is plain, warm and short. Without
account notes, the reply makes no claim about the customer's plan.

## Steps

1. **Sort.** For each ticket, write what the customer wants in one line
   and its type (question, bug, billing, account access, complaint,
   other). A ticket with several asks lists them all.
2. **Answer (support agent).** Find the article or policy that answers
   each ask and cite it by title. Give steps in the order the customer
   does them. If nothing in the material answers an ask, say so in the
   reply's notes; do not make up an answer.
3. **Tone (support agent).** Match the customer's register: short for a
   short question, calm and direct for an upset customer, with one line
   that names the problem before the fix. No blame, no jargon, no
   promises about the future.
4. **Policy check (team lead).** Read each draft against the policies.
   Remove any refund, credit, exception or date the policy does not
   allow; replace it with what the policy does allow, or with "I have
   passed this to the team who can decide".
5. **Escalation (team lead).** Flag a ticket for escalation when it
   reports a possible bug, a security or privacy issue, a legal threat,
   a request outside policy, or an account the user cannot verify. Say
   who it should go to, as a role, and why.
6. **Check** the drafts against the success criteria and fix what
   fails.

## Success criteria

- Every ticket has exactly one draft, and every ask in it is answered or
  named as unanswered.
- Every factual claim cites an article or policy from the material.
- No draft promises a refund, credit, exception or date the policies do
  not allow.
- Every flagged ticket names the role it goes to and the reason.
- No draft asks the customer for information they already gave.

## Output

For each ticket, in queue order: ticket ID and type; the draft reply,
ready to paste, under 150 words unless steps need more; sources cited;
an escalation flag if any; notes for the user (asks the material does
not answer). After all tickets: a short table of flagged tickets, then
data still needed.

## Handing off a part

When the batch is too large to hold with the articles and policies,
steps 1 to 4 may go to parallel `explore` sub-agents, one per block of
tickets:

- Steps 1 to 4: `references/reply-drafts.md`, given that block of
  tickets and all the articles and policies (and the tone guide,
  account notes, incidents and macros) as files.

Do step 5 yourself over every draft, and read again against the
policies any draft that mentions a refund, credit, exception or date.
Otherwise do every step yourself.
