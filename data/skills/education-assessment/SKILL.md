---
name: education-assessment
description: >-
  Builds a quiz, test or exam with the standards of a subject teacher and an
  exam moderator. Give it the outcomes to assess, the material that was
  covered, the level and the time allowed, and it writes the paper, an
  answer key and a marking rubric, with every question mapped to an outcome.
  Use when the user asks to write, set or check a quiz, test or exam.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: education, assessment, exams, teaching
---

# Assessment

This job builds one assessment the way a teacher and a moderator would:
the subject teacher writes the questions and the answer key, and the
moderator checks that every question is fair, maps to an outcome, tests
only what was covered and that the paper has a sensible spread of
difficulty. You turn the outcomes and material in the conversation into
one paper with its key and rubric. You never give the paper to students
or post it, and you never ask about material that was not covered.

## Inputs

Required: the outcomes to assess (education-course-plan writes them), the material covered (notes, slides,
chapters or a topic list), the level, and the time allowed. Optional:
total marks, the question types wanted, the difficulty spread, past
papers to match, and rules for calculators, notes or word limits.

Ask once, in one message, for anything required that is missing. The
defaults: about one mark per minute; a mix of short-answer and longer
questions, with multiple choice only if the level suits it; a spread
of about 30 percent easy, 50 percent medium and 20 percent hard.

## Steps

1. **Blueprint (moderator).** Make a table of outcomes against marks,
   so each outcome gets marks in proportion to its weight in the
   material. Set the difficulty spread and the question types. Every
   outcome gets at least one question.
2. **Questions (subject teacher).** Write each question from the
   material covered, in plain wording at the level's reading age. Each
   question tests one thing. Mark each with its outcome, difficulty,
   marks and type. For multiple choice, each wrong option is a mistake
   a student could make, not a joke or a giveaway.
3. **Answer key and rubric (subject teacher).** For each question, give
   the model answer. For short answers, list what earns each mark and
   what is accepted. For longer answers, write a rubric with levels and
   what each level looks like, so two markers would give the same mark.
4. **Moderation (moderator).** Check each question against the
   material: if the answer is not in what was covered, cut or rewrite
   it. Check that no question gives away another's answer, that marks
   and time match, and that the difficulty spread is met.
5. **Check** the paper against the success criteria and fix what fails.

## Success criteria

- Every question names one outcome, and every outcome has at least one
  question.
- Every question can be answered from the material covered.
- Marks add up to the stated total, and the paper fits the time.
- The difficulty spread is within 10 points of the target for each
  level.
- Every question has a model answer; every multi-mark question shows
  how its marks are given.
- No question's wording gives away another question's answer.

## Output

Three parts, in this order. The paper: instructions, then the questions
numbered with their marks, ready to print. The answer key and rubric,
by question number. The blueprint: a table of each question's outcome,
difficulty, type and marks, with totals per outcome and per difficulty.
Then data still needed. Keep the answer key apart from the paper so the
paper can be printed on its own.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
