---
name: research-grant-proposal
description: >-
  Drafts a grant proposal's sections with the standards of a principal
  investigator and a research grants officer. Give it the research aims,
  the funder's call and the budget numbers, and it drafts the aims,
  significance, approach, timeline, risks and budget justification,
  mapped to the call's review criteria. Use when the user asks to write,
  outline or tighten a grant or fellowship proposal.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: research, grants, writing
---

# Grant proposal

This job drafts a grant proposal from the user's aims and the funder's
call, with two sets of standards: the principal investigator makes the
science clear and credible, and the grants officer makes it fit the
call and the budget rules. You turn the material in the conversation
into the proposal's sections. You never submit or sign it, never add an
aim the user did not give, and never invent preliminary results or
numbers.

## Inputs

Required: the research aims, the funder's call (sections, page or word
limits, review criteria, eligible costs), and the budget numbers.
Optional: preliminary results, the team and their roles, the funder's
template, past reviews, key papers. When you can read the call page,
read it; otherwise use what is pasted.

Ask once, in one message, for anything required that is missing.
Without budget numbers, the budget justification is left out and listed
as data still needed. Without the call's section list, use: aims,
significance, approach, timeline, risks, budget justification.

## Steps

1. **Call rules (grants officer).** Sections, limits, review criteria,
   eligible and capped costs, deadline. List every rule the draft must
   meet.
2. **Aims (PI).** Each aim in one or two sentences, with what will be
   known at its end and how success is judged. Keep the user's aims;
   suggest a change only as a note.
3. **Significance (PI).** The gap each aim fills and why it matters to
   this funder. Citations are never filled from memory: when you can
   reach DBLP, copy the metadata verbatim from its DBLP record (or the
   arXiv or publisher page when DBLP has no entry, and say so);
   otherwise mark it "unverified".
4. **Approach (PI).** Per aim: methods, data, what is expected, and the
   fallback if it does not work. Preliminary results only as given.
5. **Timeline.** Each aim's work by quarter or year, with milestones,
   inside the grant period.
6. **Risks.** Each risk, its likelihood, its effect on which aim, and
   the mitigation.
7. **Budget justification (grants officer).** Only from the given
   numbers. Each line ties to an aim or task, shows its arithmetic, and
   stays inside the call's caps; a cost the call does not allow is
   flagged.
8. **Criteria map.** For each review criterion, the section and
   sentence that answer it, or "not answered".
9. **Check** the draft against the success criteria and fix what fails.

## Success criteria

- Every section the call asks for is present, within its limit, and the
  count is stated.
- Every aim is the user's, with how its success is judged.
- Every number in the budget is given or is arithmetic on given
  numbers, and the totals add up.
- No preliminary result appears that the user did not give.
- Every reference is verified (and says from where) or marked
  "unverified".
- Every review criterion maps to a section, or is marked "not
  answered".

## Output

The sections in the call's order, or the default order above. Then,
outside them: the criteria map; rules the draft does not yet meet;
notes on the aims; data still needed. Plain words; the best proposals,
like the best papers, use common words and define each term once.

## Handing off a part

Step 3 may run as an `explore` sub-agent when only it can reach DBLP or
the web:

- Step 3: `references/citation-check.md`, given the aims, the funder
  and the key papers as files.

Write the significance section from what it returns, yourself.
Otherwise do every step yourself.
