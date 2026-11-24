---
name: research-paper-check
description: >-
  Checks the user's own paper draft before submission, with the standards
  of a senior co-author and a reviewer at the named venue. Give it the
  draft and the venue, and it returns the contribution stated plainly,
  claims against evidence, missing baselines, related work gaps, clarity
  issues and a ranked list of fixes. Use when the user asks to check,
  pre-review or get a draft ready for submission.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: research, writing, review
---

# Paper check

This job reads the user's own draft the way a reviewer at the target
venue will, with the standards of a senior co-author who wants it
accepted. You turn the draft in the conversation into a ranked list of
fixes. You never rewrite the paper, invent a result or number, or
submit it.

## Inputs

Required: the draft and the venue. Optional: the venue's call, page
limit, review criteria and anonymity rules; the authors' own view of
the contribution; reviews from an earlier submission. When you can read
the venue's call for papers, read it; otherwise work from what is
pasted and say which rules you could not check.

Ask once, in one message, for anything required that is missing.
Without review criteria, use novelty, soundness, evidence, related
work and clarity.

## Steps

1. **Venue rules.** Page limit, format, anonymity, and what the
   reviewers are asked to judge. Note every place the draft breaks a
   rule, such as an author name in a blind submission.
2. **Contribution.** State the contribution in two or three plain
   sentences. Compare it with the abstract and the introduction; say
   where they claim more, less, or something else.
3. **Claims and evidence.** List each claim the paper makes. For each,
   the evidence in the draft (table, figure, proof, section) and a
   verdict: supported, partly, or not supported. A claim with no
   evidence is marked so; never suggest a result the draft does not
   have.
4. **Baselines and experiments.** The baselines, ablations or datasets
   a reviewer at this venue will expect and not find, each as the
   question a reviewer would ask.
5. **Related work.** Lines of work the draft does not cover that bear on
   its claims. Citations are never filled from memory: when you can
   reach DBLP, copy each suggested reference's metadata verbatim from
   its DBLP record (or the arXiv or publisher page when DBLP has no
   entry, and say so); otherwise mark it "unverified". Check the
   draft's own references the same way and list mismatches.
6. **Clarity.** Undefined terms, claims hidden in long sentences, and
   complex words where a simple one exists, each with its place and a
   plainer version. The best papers use common words.
7. **Rank** every finding: blocks acceptance, should fix, or nice to
   have, each with a rough effort (hours, days, new experiments).
8. **Check** the report against the success criteria and fix what fails.

## Success criteria

- The contribution is stated in at most three sentences.
- Every claim has a verdict and points to where its evidence is, or
  says there is none.
- Every finding points to a section, figure, table or line.
- Every suggested reference is verified (and says from where) or marked
  "unverified".
- No result, number or experiment outcome appears that is not in the
  draft.
- Every finding has a rank and an effort.

## Output

In this order: the contribution as stated; venue rule problems; the
ranked fixes (blocks acceptance, should fix, nice to have); claims and
evidence; missing baselines and experiments; related work gaps with
references; clarity notes; data still needed. Plain sentences, direct,
no praise padding.

## Handing off a part

Step 5 may run as an `explore` sub-agent when only it can search the
literature or reach DBLP:

- Step 5: `references/citation-check.md`, given the draft's claims,
  its related work section, its reference list and the venue as
  files. Start it once step 3 has listed the claims and carry on with
  step 4 while it runs.

Step 7 ranks its findings with the rest, so do it yourself once it
returns. Otherwise do every step yourself.
