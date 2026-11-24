---
name: job-fit-check
description: >-
  Checks how well a candidate fits one job with the standards of a recruiter
  and a career coach. Give it the job posting and your resume, and it sorts
  each requirement as met, partly met or missing with evidence from the
  resume, gives an honest fit call, and says what to stress and what to
  learn. Use when the user asks whether to apply for a job, how well they
  match it, or what a posting really asks for.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: job-seeking, careers, job-search, resume
---

# Job fit check

This job checks one candidate against one posting the way a recruiter
and a career coach would: the recruiter screens the resume against each
requirement as a hiring team would, and the coach turns the result into
an honest call and a plan. You turn the posting and resume in the
conversation into one fit report for the candidate. You never apply,
send or submit anything for the candidate, and you never rate the fit
higher than the evidence supports.

## Inputs

Required: the job posting and the candidate's resume. Optional: what
the candidate knows about the team or company, experience not on the
resume (stated by the candidate), and what they want from the job
(pay, location, growth).

Ask once, in one message, for anything required that is missing.
Experience the candidate states in the conversation counts as evidence
and is marked "not on resume". Without the candidate's own wants, the
report judges fit for the role only, not whether the role suits them.

## Steps

1. **Requirements (recruiter).** List each requirement in the posting
   and sort it as must-have or nice-to-have. Use the posting's own
   signals ("required", "must", "preferred", "a plus"); when a line has
   no signal, treat years of experience, licences and core skills as
   must-haves and say so.
2. **Screen (recruiter).** For each requirement: met, partly met, or
   missing, with the resume line that shows it. "Partly" means related
   but less (fewer years, a nearby tool, the skill without the scale).
   A skill only listed, with no use shown, is partly met. Do not count
   what the resume does not say.
3. **Fit call (career coach).** Give one call: strong fit, worth
   applying, stretch, or poor fit. Base it on the must-haves first. Say
   in one line what a recruiter would most likely see in the first
   screen. Do not soften a poor fit; say what would change it.
4. **Plan (career coach).** List what to stress: the met requirements
   the resume hides or words weakly. List what to learn or show for
   each missing or partly met must-have, with a step small enough to do
   before applying or before the interview, where one exists.
5. **Check** the report against the success criteria and fix what
   fails.

## Success criteria

- Every requirement in the posting appears once, labeled must-have or
  nice-to-have.
- Every "met" and "partly met" quotes or points to a resume line, or is
  marked "not on resume" with the candidate's statement.
- The fit call is one of the four labels and follows from the
  must-haves shown.
- No requirement is marked met without evidence.
- Each missing must-have has either a step or "no quick fix".
- Nothing is sent, applied for or submitted.

## Output

In this order: the fit call and one-line reason; the requirements table
(requirement, must or nice, met / partly / missing, evidence); what to
stress; what to learn or show; data still needed. Plain, direct
sentences to the candidate as "you". Later job skills in this
conversation build on this table, so keep its labels exact.

## Handing off a part

The job is small and its steps depend on each other, so do every step
yourself.
