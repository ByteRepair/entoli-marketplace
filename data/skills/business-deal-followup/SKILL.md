---
name: business-deal-followup
description: >-
  Wraps up a sales call with the standards of an account executive and a
  sales manager. Give it the call notes or transcript, the prospect and the
  deal stage, and it writes the follow-up email, an internal deal summary
  with qualification gaps, and dated next steps. Use after a discovery call
  or any later sales meeting.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: business, sales
---

# Deal follow-up

This job wraps up one sales call while the deal is still warm, the way
a small team would: the account executive writes to the buyer, and the
sales manager reads the notes for what the deal still lacks. You turn
the call notes in the conversation into a follow-up email, a deal
summary and next steps. You never send the email, update the CRM, or
put words in the buyer's mouth that the notes do not carry.

## Inputs

Required: the call notes or transcript, the prospect (company and the
people on the call), and whether this was a first discovery call or a
later meeting. Optional: the deal stage as the user sees it, earlier
notes on the deal, the user's product and pricing.

Ask once, in one message, for anything required that is missing.
Without a stated stage, the summary takes it from the notes and says so.
A first call gets a full qualification; a later meeting updates only
what changed.

## Steps

1. **Lift out what the buyer said.** Their problems in their words, the
   budget and who approves it, the timeline, the tools they use now, and
   who is for or against the deal. Quote or closely paraphrase; mark
   anything the user inferred as inferred.
2. **Qualification (sales manager).** For budget, authority, need and
   timeline, mark each as evidenced, hinted or missing, with the line
   from the notes behind it. A gap stays a gap, not a conclusion: an
   unnamed decision maker is "missing", not "probably the CFO". Note
   the risks and whether there is a champion.
3. **Next steps.** Only what the buyer agreed to, in order, each with an
   owner (a role, not a handle) and a date. A buyer commitment with no
   date is "to confirm". Add the user's own follow-ups to close the
   missing items from step 2.
4. **Follow-up email (account executive).** Under 150 words: thanks,
   their problem restated in their terms, the agreed next steps with
   dates, one call to action. It confirms the meeting; it does not
   pitch.
5. **Check** the answer against the success criteria and fix what fails.

## Success criteria

- Every buyer statement in the summary and email is in the notes.
- Budget, authority, need and timeline each have a mark and a source
  line, or "missing".
- Every next step has an owner and a date, or "to confirm".
- No next step is something the buyer did not agree to, unless it is
  marked as the user's own follow-up.
- The email is under 150 words, has one call to action, and has no
  feature pitch.

## Output

In this order: the follow-up email, ready to copy; the deal summary
(the buyer's problem, qualification table, risks, champion status, one
line of activity for the CRM); next steps as a table; data still
needed. Plain sentences, past tense for agreed facts.

## Handing off a part

A long transcript may go to a sub-agent for step 1 when it is too large
to hold with the rest; brief it to return the buyer's statements with
their place in the transcript. Do steps 2 to 4 yourself. Otherwise do
every step yourself.
