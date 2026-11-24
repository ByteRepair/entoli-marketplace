---
name: people-job-posting
description: >-
  Writes a job description and a job posting with the standards of a
  recruiter and a hiring manager. Give it the hiring manager's notes on the
  role, the team and the location, and it writes an internal job description
  and a public posting with must-haves kept apart from nice-to-haves, in
  plain and inclusive wording, with a salary range only if one is given.
  Use when the user is opening a role or rewriting a posting.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: people, hiring, recruiting
---

# Job posting

This job turns a hiring manager's notes into a role people can read and
apply for, the way a small team would: the hiring manager says what the
work is and what it truly needs, and the recruiter writes it so the
right people apply and no one is put off for no reason. You turn the
notes in the conversation into a job description and a posting. You
never post the role, set the pay, or contact a candidate.

## Inputs

Required: the role title, what the person will do, the team, the
location or remote policy, and the employment type. Optional: the
salary range, the level, benefits, the hiring process, the company
blurb, a posting the user wants to match.

Ask once, in one message, for anything required that is missing.
Without a salary range, the posting has no pay line and the gaps list
says so; never guess one. Without a company blurb, leave a marked
placeholder.

## Steps

1. **The work (hiring manager).** Write what the person will do in the
   first year as four to six concrete outcomes, not a task list. Take
   them from the notes; do not add duties.
2. **Must-haves and nice-to-haves.** Sort every requirement in the
   notes. A must-have is something the person cannot do the job
   without on day one; keep at most five. Move the rest to
   nice-to-haves. Replace year counts with the skill they stand for,
   unless the notes say the count is required.
3. **Wording (recruiter).** Plain words, short sentences, "you" for the
   reader. Remove gendered or age-coded words ("rockstar", "young",
   "digital native"), jargon the reader would not know, and
   requirements that screen out people without a link to the work
   (a degree, a car, lifting) unless the notes say the job needs it.
4. **Pay and terms.** State the salary range exactly as given, with its
   currency and period. State the location, remote policy and
   employment type.
5. **Check** both texts against the success criteria and fix what
   fails.

## Success criteria

- Must-haves and nice-to-haves are in separate lists, with at most five
  must-haves.
- Every duty and requirement is in the notes.
- No gendered or age-coded words, and no requirement without a link to
  the work.
- A salary range appears only if the notes give one, and matches it.
- Location, remote policy and employment type are stated.
- The posting says that people who meet most, not all, of the
  requirements are welcome to apply.

## Output

In this order: the internal job description (purpose, outcomes,
must-haves, nice-to-haves, level, reporting line); the public posting
(a two-sentence opening, what you will do, what you need, nice to have,
pay and terms, how to apply), under 500 words; data still needed. No
marketing adjectives about the company or the role.

## Handing off a part

This job is small enough to do in one pass; do every step yourself. A
sub-agent is only useful when the user asks for postings for several
roles at once, one per role, each briefed with its own notes.
