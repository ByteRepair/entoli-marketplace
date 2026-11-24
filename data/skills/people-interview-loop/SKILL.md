---
name: people-interview-loop
description: >-
  Designs a structured interview loop with the standards of a recruiter and
  a hiring manager. Give it the role's requirements and the interviewers
  with their rounds and time, and it writes one kit per interviewer with
  competency-mapped questions, an anchored scorecard and the debrief agenda.
  Use when the user is setting up or fixing the interviews for a role.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: people, hiring, interviews
---

# Interview loop

This job builds the materials for one structured hiring loop, the way a
small team would: the hiring manager says what the role needs, and the
recruiter turns that into a loop that asks each thing once, the same
way for every candidate. You turn the role's requirements and the
interviewer list in the conversation into kits, a scorecard and a
debrief agenda. You never score or rank a candidate, make a hiring
decision, or contact anyone.

## Inputs

Required: the role (a job description or bullets) with must-haves and
nice-to-haves, the interviewers on the loop, the number of rounds, and
the time each round gets. Optional: the competencies the team uses, the
company's values, a take-home or work sample already in use.

Ask once, in one message, for anything required that is missing.
Without named competencies, propose four to six from the must-haves and
mark them "draft". This job does not write the job description; it
works from what the user gives.

## Steps

1. **Competencies (hiring manager).** List the competencies the loop
   tests, each tied to a must-have. Nice-to-haves get a competency only
   if a round has time left.
2. **Map the loop (recruiter).** Give each competency to exactly one
   interviewer, so nothing is asked twice. Keep inside the stated
   rounds and time; if it does not fit, drop the lowest nice-to-have
   and say so.
3. **Questions.** For each competency, two or three behavioral
   questions ("Tell me about a time...") with the follow-ups planned in.
   No hypothetical trick questions, no questions about age, family,
   health, religion, origin or other protected traits.
4. **Scorecard.** One dimension per competency, anchored at 1, 3 and 5
   with observable behavior ("at 3: does X with help"), not adjectives.
   Add the evidence line the interviewer fills in before the debrief.
5. **Debrief agenda.** Evidence first, then votes; time per
   interviewer; the decision questions the panel answers.
6. **Check** the materials against the success criteria and fix what
   fails.

## Success criteria

- Every competency maps to a must-have and to exactly one interviewer.
- The loop fits the stated rounds and time.
- Every question is behavioral and has at least one planned follow-up.
- Every scorecard anchor describes behavior someone could observe.
- No question touches a protected trait.
- The debrief takes evidence before votes.

## Output

In this order: the loop map (round, interviewer, competency, time) as a
table; one kit per interviewer, one page each (round, competency,
opening, questions with follow-ups, the shared off-limits list); the
scorecard; the debrief agenda; data still needed. Neutral, repeatable
wording: the same questions asked the same way each time.

## Handing off a part

For a loop with many interviewers, step 3 for each competency is
independent and may run as parallel sub-agents, each briefed with its
competency, the must-have behind it and the round's time. Do steps 1, 2,
4 and 5 yourself. Otherwise do every step yourself.
