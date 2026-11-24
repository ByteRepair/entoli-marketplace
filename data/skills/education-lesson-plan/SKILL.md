---
name: education-lesson-plan
description: >-
  Plans a single lesson with the standards of an experienced classroom
  teacher and a learning support teacher. Give it the topic, the level, the
  lesson length and what students already know, and it writes one lesson
  plan with an objective, timed activities, checks for understanding,
  differentiation and a materials list. Use when the user asks to plan,
  prepare or rework one lesson or class session.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: education, lesson-planning, teaching
---

# Lesson plan

This job plans one lesson the way a teacher would with help from a
learning support colleague: the classroom teacher sets the objective
and the timed activities, and the learning support teacher adds the
checks for understanding and the ways in for students who need more
help or more challenge. You turn the lesson details in the conversation
into one lesson plan. You never share the plan with students or post it
anywhere, and you do not plan more than the one lesson asked for.

## Inputs

Required: the topic, the level (age, year or course level), the lesson
length in minutes, and what students already know. Optional: the course
outcome the lesson serves (from education-course-plan), class size, students with known needs (in
general terms, no names needed), the room and equipment, and materials
the teacher already has.

Ask once, in one message, for anything required that is missing. The
defaults: a class of 25 with mixed ability; a standard room with a
board and a projector; no materials beyond what the plan lists for the
teacher to prepare.

## Steps

1. **Objective (classroom teacher).** Write one objective: what students
   will be able to do by the end, with an observable verb. It must be
   reachable in the time from what students already know. If the topic
   is too big for one lesson, narrow it and say what is left for later.
2. **Activities (classroom teacher).** Plan the lesson in timed blocks:
   a start that links to prior knowledge, teaching, guided practice,
   independent practice, and a close. Give each block its minutes, what
   the teacher does and what students do. The minutes add up to the
   lesson length. Keep teacher talk in any one block under 15 minutes.
3. **Checks for understanding (learning support).** Put at least one
   check after teaching and one at the close (an exit question, a
   show of answers, a short task). Write the actual question or task
   and what a correct answer looks like. Say what the teacher does if
   most students get it wrong.
4. **Differentiation (learning support).** For each main activity, give
   one support (for students who struggle) and one stretch (for
   students who finish early). Use the known needs given; do not guess
   at needs that were not described.
5. **Materials.** List every item the activities use, and mark what the
   teacher must make or print.
6. **Check** the plan against the success criteria and fix what fails.

## Success criteria

- There is one objective, with an observable verb.
- Block minutes add up to the lesson length exactly.
- At least two checks for understanding, each with its question and
  the expected answer.
- Each main activity has one support and one stretch.
- Every item used in an activity is in the materials list.
- Nothing in the lesson needs knowledge the stated prior knowledge
  does not cover, or the gap is taught in the lesson.

## Output

In this order: the objective; a one-line link to prior knowledge; the
lesson as a table (minutes, block, teacher does, students do, check);
checks for understanding with expected answers; differentiation; the
materials list; data still needed. Fits on two printed pages. Plain,
direct wording a cover teacher could follow.

## Handing off a part

The lesson is small and its steps depend on each other, so do every
step yourself.
