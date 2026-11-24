---
name: people-survey-readout
description: >-
  Turns employee survey results into a readout with the standards of a
  people analyst and an HR business partner. Give it the scores by
  question, the last survey's scores, group breakdowns and the open
  comments, and it writes the numbers that moved, the themes from the
  comments and proposed actions, while protecting anonymity. Use after
  an engagement or pulse survey closes.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: people, surveys, engagement
---

# Survey readout

This job turns one employee survey into a readout leaders can act on,
the way a small team would: the people analyst finds what changed in the
numbers, and the HR business partner reads the comments, protects the
people who wrote them, and proposes actions. You turn the results in the
conversation into one readout. You never try to identify who wrote a
comment, publish or share the results, or commit to an action.

## Inputs

Required: scores by question (with the scale and the number of answers),
the response rate, and the open comments. Optional: the last survey's
scores, breakdowns by team or group with their answer counts, the
company's benchmark, actions promised after the last survey.

Ask once, in one message, for anything required that is missing. Without
the last survey, the readout shows levels, not changes. The smallest
group shown is five answers unless the user gives a higher company rule.

If `records/people-survey-readout.md` exists in the project workspace,
read it first: it is the last run's summary. Say what changed since
then.

## Steps

1. **Protect anonymity first (HR partner).** Drop any group breakdown
   with fewer answers than the minimum; fold it into the next level up
   and say a group was folded, not which. Never compare groups in a way
   that lets someone work out a small group by subtraction.
2. **What moved (analyst).** For each question, the score and the change
   since last time. Call out the changes of five points or more on a
   100-point scale (or the same share of the scale used) and the lowest
   and highest scores. Note the response rate and its change; low
   response weakens every conclusion.
3. **Themes (HR partner).** Group the comments into themes, with the
   number of comments in each. Link each theme to the scores it
   explains. Paraphrase; quote a comment only if it names no person,
   team, place, project or event that could point to the writer.
4. **Proposed actions.** Two to four, each tied to a theme or a score
   that moved, with a suggested owner (a role) and how the next survey
   will show whether it worked. Note any action promised last time and
   whether the scores suggest it landed.
5. **Check** the readout against the success criteria and fix what
   fails.

## Success criteria

- No group with fewer answers than the minimum is shown.
- No quoted comment contains a detail that could identify its writer.
- Every number is in the results or shown as arithmetic on them.
- Every theme shows how many comments it rests on.
- Every proposed action ties to a theme or a score, and is labeled
  "proposed".
- The response rate is stated.

## Output

In this order: the headline in three sentences; response rate; what
moved, as a table; themes with comment counts; proposed actions; limits
of the data (small groups folded, low response); data still needed.
Plain words, no blame, no guesses about why one group scored lower.

After answering, replace `records/people-survey-readout.md` in the
project workspace with this run's summary: the survey date, the response
rate and the score per question; no comments and no group under the
minimum size. Where files cannot be written, end with the summary for
the user to save.

## Handing off a part

When there are too many comments to hold with the scores, step 3 may go
to an `explore` sub-agent:

- Step 3: `references/comment-themes.md`, given the comments, the
  questions with their scores, and the minimum group size as files. The
  anonymity rules from steps 1 and 3 are in the prompt.

Check its quotes against those rules before using them. Do the other
steps yourself. Otherwise do every step yourself.
