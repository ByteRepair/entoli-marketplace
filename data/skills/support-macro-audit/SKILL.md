---
name: support-macro-audit
description: >-
  Audits a library of support macros with the standards of a support team
  lead and a support content editor. Give it the macros, the current
  policies and product notes, and the top ticket themes, and it lists the
  outdated, duplicated, wrong-tone and missing macros with proposed
  rewrites. Use when the user asks to review, clean up or update their
  canned responses or macros.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: support, macros, quality
---

# Macro audit

This job reviews a library of canned responses (macros) the way a
support team would: the team lead checks each macro against current
policy and the product, and the content editor fixes tone and wording
and writes what is missing. You turn the macros, policies and themes in
the conversation into one audit with proposed rewrites. You never edit,
delete or publish a macro in the help desk.

## Inputs

Required: the macros (each with its name and text) and the current
policies and product notes (features, plan names, UI labels, prices,
time frames). Optional: the top ticket themes with counts (as
support-weekly-trends reports them), how often
each macro is used, the brand's tone guide, recent product releases.

Ask once, in one message, for anything required that is missing.
Without themes, the "missing" check is left out and the answer says
so. Without a tone guide, the standard is plain, warm and short, with
no blame and no jargon.

## Steps

1. **Accuracy (team lead).** Check each macro against the policies and
   product notes: wrong prices, plan names, time frames, UI labels,
   links, or features that changed. Quote the wrong text and the source
   that contradicts it. A macro that promises a refund, credit or date
   the policy does not allow is outdated.
2. **Duplicates (team lead).** Find macros that answer the same need.
   Name the one to keep and why (more accurate, more used), and the ones
   to retire.
3. **Tone (content editor).** Flag macros that blame the customer, use
   internal jargon, are cold for a complaint, or are longer than the
   answer needs. Quote the line that fails.
4. **Missing (team lead).** Compare the macros with the top themes. List
   themes with no macro, with their ticket counts.
5. **Rewrites (content editor).** Write a proposed rewrite for every
   macro flagged in steps 1 and 3, and a new draft for each missing
   theme, using only facts from the policies and product notes. Keep
   the help desk's placeholders (such as a customer-name field) as they
   are written.
6. **Check** the audit against the success criteria and fix what
   fails.

## Success criteria

- Every macro has a verdict: keep, rewrite, merge or retire.
- Every "outdated" flag quotes the macro text and the source it
  conflicts with.
- No rewrite states a fact that is not in the policies or product
  notes.
- No rewrite promises what policy does not allow.
- Every missing-macro item names its theme and ticket count.

## Output

In this order: the audit in two sentences (how many to keep, rewrite,
merge, retire, add); the verdict table (macro, verdict, issue, source);
duplicates with the one to keep; proposed rewrites, each with the old
text's problem in one line; new macro drafts for missing themes; data
still needed. Rewrites ready to paste, under 150 words each.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
