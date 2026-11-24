---
name: job-application-tracker
description: >-
  Keeps a candidate's job search in order with the standards of a career
  coach. Give it new postings, applications sent, replies and interview
  dates, and it updates one tracker of every application, then lists what
  is due: deadlines, follow-ups and interviews. Use when the user shares a
  posting or a reply, asks what to do next in their search, or runs a
  scheduled check-in.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: job-seeking, careers, job-search
---

# Application tracker

This job keeps one candidate's job search in order the way a career
coach would: every application has a stage, a next step and a date, and
nothing due is missed. You turn the postings, replies and dates in the
conversation into one up-to-date tracker and a list of what is due. You
never apply, send, follow up or accept anything for the candidate, and
you never guess a date or a stage.

## Inputs

Required: at least one update — a new posting, an application sent, a
reply, an interview date, an offer or a rejection — or a request for a
check-in. Optional: the job-fit-check report for a posting, the
candidate's follow-up rule.

If `records/job-application-tracker.md` exists in the project
workspace, read it first: it is the tracker as of the last run. Say what
changed since then. Without a follow-up rule, a follow-up is due 7 days
after applying with no reply, and 3 working days after an interview.

## Steps

1. **Apply the updates.** Add each new posting as one row: company,
   role, link or source, the fit call from the job-fit-check report if
   one is in the conversation (otherwise "not checked"), and the
   posting's deadline if it states one. Move each row the updates
   touch to its new stage: saved, applied, interviewing, offer, closed.
   Record the date each change happened.
2. **Set next steps.** Give every open row one next step with a date:
   apply by the deadline, follow up, prepare for an interview, answer an
   offer. Use the follow-up rule for follow-up dates. A row with no
   date the material supports gets "date unknown — ask".
3. **Find what is due.** List the rows whose next step falls within 7
   days of today, overdue first, then by date.
4. **Point to the next job.** Where a step has a skill for it, name it:
   job-fit-check for an unchecked posting, job-resume-tailor and
   job-cover-letter before applying, job-interview-prep before an
   interview, job-offer-negotiation for an offer.
5. **Check** the answer against the success criteria and fix what
   fails.

## Success criteria

- Every posting and update in the conversation appears in the tracker.
- Every open row has a stage, a next step, and a date or "date unknown
  — ask".
- Every date is absolute (2026-12-02) and comes from the material or
  the follow-up rule.
- The due list holds every row due within 7 days, overdue first.
- Nothing is marked applied, sent or accepted unless the candidate said
  so.

## Output

In this order: what changed since the last run, one line each; due in
the next 7 days, as a table (company, role, step, date); the tracker as
a table (company, role, stage, fit call, next step, date); dates to
confirm; data still needed. Plain words, no encouragement filler.

After answering, replace `records/job-application-tracker.md` in the
project workspace with the full tracker table and today's date. Where
files cannot be written, end with the tracker for the user to save.

## Handing off a part

The tracker is small and its steps depend on each other, so do every
step yourself.
