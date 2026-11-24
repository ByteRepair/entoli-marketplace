---
name: research-rebuttal
description: >-
  Drafts the authors' response to reviewers with the standards of a
  corresponding author who has done this many times. Give it the reviews,
  the paper and the venue's rebuttal rules, and it writes a response that
  answers every point, grouped by theme, says what will change in the
  revision, and fits the length limit. Use when the user asks to write a
  rebuttal, author response or response to reviewers.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: research, writing, peer-review
---

# Rebuttal

This job drafts the response to reviewers, with the standards of a
corresponding author: every point answered, specific, polite, and
honest about what will change. You turn the reviews, the paper and the
authors' plans in the conversation into one response within the venue's
limit. You never submit it, never promise a change the authors did not
agree to, and never invent a result or number.

## Inputs

Required: the reviews, the paper (or its relevant sections), and the
venue's rebuttal rules (length limit, format, whether new results are
allowed). Optional: new results the authors have, the changes they
plan, their position on each point, the meta-review. When you can read
the venue's author guidelines, read them; otherwise use what is pasted.

Ask once, in one message, for anything required that is missing. Where
the authors gave no position on a point, draft the most likely answer
and mark it "[authors confirm]".

## Steps

1. **Split.** Break each review into single points, each with an ID
   (R1.1, R1.2, R2.1, ...), quoted short.
2. **Group** the points by theme across reviewers, so a shared concern
   is answered once and every reviewer who raised it is named by ID.
3. **Classify** each point: misread (the paper already answers it),
   valid and will fix, valid but out of scope, or disagree. Use the
   authors' position; never move a point to "will fix" on your own.
4. **Answer.** Each answer points to a section, figure, table or line,
   and says what changes in the revision. New numbers only from results
   the authors gave. A disagreement gives the reason and the evidence,
   not an opinion of the reviewer.
5. **Fit** the limit. Count words or characters as the venue counts
   them. When over, shorten the minor points first, never drop a point.
6. **Check** the response against the success criteria and fix what
   fails.

## Success criteria

- Every point ID from step 1 appears in the response.
- Every "will fix" names the change and where it lands.
- Every number is in the paper or in results the authors gave.
- No change is promised that the authors did not agree to, unless it is
  marked "[authors confirm]".
- The response is within the limit, and its count is stated.
- No sentence judges a reviewer; thanks appear once, at the top.

## Output

The response, in the venue's format, grouped by theme, with the point
IDs it answers at the start of each answer. Then, outside it: a
coverage table (point ID, theme, class, where answered); the planned
revision changes as a list; the items marked "[authors confirm]"; the
count against the limit; data still needed. Plain words, short
sentences.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
