---
name: education-study-guide
description: >-
  Builds a personal study plan for a learner with the standards of a study
  skills tutor and a subject tutor. Give it your notes, the syllabus, the
  exam date and how confident you feel on each topic, and it writes a
  day-by-day plan with spaced review, practice questions with answers, and
  your likely weak topics first. Use when a student asks for help to revise,
  study or prepare for an exam.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: education, studying, revision, exams
---

# Study guide

This job builds one study plan for a learner the way two tutors would:
the study skills tutor plans the days with spaced review and real
limits on time, and the subject tutor writes practice questions from
the learner's own notes and puts weak topics first. You turn the notes,
syllabus and self-assessment in the conversation into one study guide
for the learner. You work only from the material given, and you never
do graded work for the learner: practice questions are for practice,
not answers to a set assignment.

## Inputs

Required: the syllabus or topic list, the exam date, and the learner's
notes. Optional: a confidence rating per topic (1 to 5), past papers,
hours free each day, days off, and the exam format.

Ask once, in one message, for anything required that is missing, and
ask for the confidence ratings in the same message. The defaults: two
hours a day, every day; one day off a week; without ratings, every
topic is treated as unknown and the first practice round finds the
weak ones.

## Steps

1. **Time (study skills tutor).** Work out today's date, the days to
   the exam and the hours available. If the time is too short to cover
   every topic, say so first and put the weakest and highest-weighted
   topics first.
2. **Weak topics (subject tutor).** Rank topics by the learner's own
   ratings, then by how much of the syllabus or past papers they take.
   Topics rated 1 or 2, or thin in the notes, are likely weak. Say
   where the notes have gaps against the syllabus.
3. **Schedule (study skills tutor).** Plan day by day. Each topic is
   studied once, then reviewed after about 1, 3 and 7 days, and again
   near the exam. Weak topics get more sessions. Keep sessions to 25 to
   50 minutes with breaks. Leave the last day or two for full practice
   and light review. Do not plan more hours than the learner has.
4. **Practice questions (subject tutor).** For each topic, write three
   to five questions from the notes, from recall to applying the idea,
   in the exam format if given. Give each its answer, with the place in
   the notes it comes from. If the notes do not cover a syllabus topic,
   mark it "not in your notes" instead of writing answers from outside.
5. **Check** the guide against the success criteria and fix what fails.

## Success criteria

- No day has more study hours than the learner has free.
- Every syllabus topic appears in the schedule at least once, or is
  named as cut for time.
- Each topic is reviewed at least twice after first study, or the guide
  says why time did not allow it.
- Weak topics are scheduled before strong ones and get more sessions.
- Every practice question has an answer and a pointer to the notes.
- No answer uses material that is not in the notes.

## Output

In this order: a two-line summary (days left, hours, the three weakest
topics); notes gaps against the syllabus; the schedule as a table
(date, session, topic, new or review); practice questions by topic,
with the answers after all the questions so the learner can test
first; data still needed. Written to the learner as "you", in short
sentences.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
