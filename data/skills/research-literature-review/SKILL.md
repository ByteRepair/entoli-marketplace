---
name: research-literature-review
description: >-
  Writes a structured literature review with the standards of a careful
  researcher. Give it a research question and a set of papers (pasted, or
  links it can reach), and it returns the themes, what is settled, what
  conflicts and what is still open, with every claim tied to a paper and
  every reference checked against DBLP. Use when the user asks to review,
  survey or synthesize the literature on a question.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: research, literature-review, writing
---

# Literature review

This job turns a research question and a set of papers into a review of
what that set says, with the standards of a researcher writing a related
work section or survey. You work from the papers in the conversation or
the ones the user links, read them, and tie every claim to the paper it
comes from. You never cite a paper you have not read, never invent a
result or number, and never fill a reference from memory.

## Inputs

Required: the research question and the papers (full text, PDFs, or
links, DOIs or arXiv IDs you can reach). Optional: the scope (years,
venues, methods), the audience, a length limit, a citation style, and
papers the user wants searched for.

Ask once, in one message, for anything required that is missing. A
paper you cannot reach or read goes on the "not read" list and is never
cited. The default length is about 1,500 words and the default style is
numbered references.

## Steps

1. **Read.** For each paper, note in one line each: the question it
   asks, the method, the data or setting, and the main result as the
   paper states it, with the section or page. A number is copied, never
   rounded or recomputed.
2. **References.** Citations are never filled from memory. When you can
   reach DBLP, copy each paper's authors, title, venue, year and DOI or
   arXiv ID verbatim from its DBLP record; when DBLP has no entry, copy
   them from the arXiv or publisher page and say so. When you can reach
   neither, mark the reference "unverified".
3. **Themes.** Group the papers by the part of the question they answer
   or the approach they take. A paper may sit in more than one theme.
4. **Settled and conflicting.** A finding is "settled" only when two or
   more papers in the set support it and none in the set contradicts
   it. When papers disagree, state each side with its paper and the
   likely reason (data, setting, metric, method) where the papers show
   it; otherwise say the reason is unclear.
5. **Gaps.** What the question needs that no paper in the set answers.
   A gap is a gap in this set; say so, since a paper outside it may
   fill it.
6. **Write** in plain words. The best papers use common words; use a
   complex word only when no simple one exists. Define each term once.
7. **Check** the review against the success criteria and fix what fails.

## Success criteria

- Every claim cites at least one paper from the set.
- Every number matches the paper it cites.
- Every reference is verified from DBLP, verified from arXiv or the
  publisher (and says which), or marked "unverified".
- No paper on the "not read" list is cited.
- Every "settled" finding has two or more supporting papers and none
  against.
- Every conflict names the papers on each side.

## Output

In this order: the question restated in one sentence; themes, each a
short section; what is settled; what conflicts; gaps; the reference
list; papers not read; data still needed. Plain sentences, present tense
for what a paper shows, no praise words ("seminal", "groundbreaking").

## Handing off a part

Step 1 may run as parallel `explore` sub-agents, a share of the papers
each, when the papers are too long to hold together. Step 2 may run as
an `explore` sub-agent when only it can reach DBLP or the web:

- Step 1: `references/paper-reader.md`, given the research question
  and its share of the papers (text or links) as files.
- Step 2: `references/citation-check.md`, given the papers' titles,
  links, DOIs or arXiv IDs from the input, as a file. It needs nothing
  from step 1, so start it in the same message.

Steps 3 to 7 need every paper's notes, so do them yourself once the
parts return. Otherwise do every step yourself.
