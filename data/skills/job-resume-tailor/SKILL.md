---
name: job-resume-tailor
description: >-
  Tailors a candidate's resume to one job posting with the standards of a
  resume writer and a recruiter. Give it your resume and the posting, and it
  reorders and rewords your real experience to the posting's terms, uses
  only numbers you gave, and flags the gaps it could not close. Use when the
  user asks to tailor, target, update or rewrite a resume for a specific
  job.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: job-seeking, careers, resume, job-search
---

# Resume tailor

This job tailors one resume to one posting the way a resume writer and
a recruiter would: the recruiter names the terms and requirements the
hiring team will scan for, and the resume writer reorders and rewords
the candidate's real experience to meet them. You turn the resume and
posting in the conversation into one tailored resume and a change list.
You never apply, send or submit anything for the candidate, and you
never invent experience, titles, employers, dates, skills or numbers.

## Inputs

Required: the candidate's resume and the job posting. Optional: the
job-fit-check report from this conversation, extra experience or
numbers the candidate states, a page limit, and a resume format to
keep.

Ask once, in one message, for anything required that is missing. If a
job-fit-check report is in the conversation, use its requirements
table and labels; do not redo the screen. The defaults: one page for
under ten years of experience, two pages otherwise; the resume's
existing section order unless the posting calls for another.

## Steps

1. **Target terms (recruiter).** From the posting (or the fit report),
   list the must-haves, the nice-to-haves, and the exact terms the
   posting uses for skills, tools and duties. Note which ones the
   resume already supports, in any wording.
2. **Select and order (resume writer).** Put the most relevant role
   and bullets first within each section. Move or cut bullets that do
   not serve this posting, within the page limit. Keep every title,
   employer and date exactly as given.
3. **Reword (resume writer).** Rewrite bullets to lead with the action
   and the result, using the posting's terms where the candidate's
   experience truly matches them. Use a number only if the candidate
   gave it; where a bullet would be stronger with a number the
   candidate did not give, mark it "[number?]" for them to fill.
4. **Gaps (recruiter).** List each must-have the resume still does not
   show. Do not cover a gap with wording that implies experience the
   candidate does not have; say what the candidate could add if it is
   true.
5. **Check** the resume against the success criteria and fix what
   fails.

## Success criteria

- Every title, employer and date matches the original resume.
- Every skill, tool and duty in the tailored resume is in the original
  resume or stated by the candidate in the conversation.
- Every number is one the candidate gave; missing ones are "[number?]".
- The resume fits the page limit.
- Each must-have from the posting is either shown in the resume or
  listed as a gap.
- Nothing is sent, applied for or submitted.

## Output

In this order: the tailored resume, ready to paste; a change list (what
moved, what was reworded, what was cut, one line each); the gaps, with
what to add if true; the "[number?]" places to fill; data still
needed. Plain resume style: no first person, no adjectives the
experience does not show.

## Handing off a part

The job is small and its steps depend on each other, so do every step
yourself.
