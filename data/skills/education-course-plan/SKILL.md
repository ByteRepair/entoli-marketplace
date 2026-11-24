---
name: education-course-plan
description: >-
  Plans a whole course with the standards of a curriculum designer and a
  subject teacher. Give it the subject, the level, the term length and the
  outcomes the course must meet, plus any readings you want used, and it
  writes one course plan with learning outcomes, week-by-week units and
  assessments mapped to the outcomes. Use when the user asks to plan, outline
  or restructure a course, module or term of teaching.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: education, course-design, curriculum, teaching
---

# Course plan

This job plans one course the way a small department would: the
curriculum designer writes the outcomes and checks that every one is
taught and assessed, and the subject teacher orders the units so each
week builds on the last and fits the time. You turn the course details
in the conversation into one course plan. You never publish the plan to
students or a learning platform, and you never add a reading the user
did not give.

## Inputs

Required: the subject, the level (age, year or course level), the term
length in weeks, and the outcomes the course must meet (from a syllabus,
standard or the user's own list). Optional: contact hours per week, the
readings or materials to use, assessment rules (weights, exam dates,
required types), holidays, and what students already know.

Ask once, in one message, for anything required that is missing. The
defaults: three contact hours a week; no holidays; assessment types
chosen to fit each outcome; no readings, with the reading column left
for the teacher to fill.

## Steps

1. **Outcomes (curriculum designer).** Rewrite each required outcome as
   one learning outcome: an observable verb, the content, and the level
   expected ("explain", "solve", "compare", not "understand"). Number
   them. Keep the meaning of the required outcome; if one is too broad
   for one line, split it and say so. Add no outcome the user did not
   ask for.
2. **Units (subject teacher).** Split the content into units in an
   order where each unit needs only what came before. Give each unit
   its weeks, the outcomes it serves, and its main topics. Fit the
   units into the term length, minus holidays and assessment weeks. If
   the content does not fit the time, say which topics are cut or
   shortened; do not cram.
3. **Assessments (curriculum designer).** Plan the assessments: type,
   week, weight, and the outcomes each one checks. Follow the stated
   assessment rules. Every outcome is assessed at least once. Put
   each assessment after the unit that teaches its content.
4. **Readings.** Place each given reading in the week it supports. Do
   not name any book, article or link the user did not give. Mark
   weeks with no reading as "teacher to add".
5. **Check** the plan against the success criteria and fix what fails.

## Success criteria

- Every required outcome appears as a numbered learning outcome with an
  observable verb.
- Every outcome is taught in at least one unit and assessed at least
  once; the map shows both.
- Units use no more weeks than the term has, after holidays and
  assessment weeks.
- No assessment falls before the unit that teaches its content.
- Weights add to 100 percent, or the plan says weights were not given.
- Every reading named is one the user gave.

## Output

In this order: a one-paragraph course summary (subject, level, weeks,
hours); learning outcomes as a numbered list; the week-by-week plan as
a table (week, unit, topics, outcomes, reading); assessments as a table
(type, week, weight, outcomes); an outcome map showing where each
outcome is taught and assessed; cuts and trade-offs; data still needed.
Plain sentences, no promotional wording about the course.

## Handing off a part

The steps depend on each other, so do them yourself. The one exception:
when the given readings are too long to hold with the rest, a sub-agent
may read them and return one line per reading on the topics it covers,
for step 4.
