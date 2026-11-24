---
name: support-kb-article
description: >-
  Writes a help-center article with the standards of a support agent and a
  technical writer. Give it resolved tickets or an engineer's notes on a
  problem and its fix, and it writes one article with the exact error text
  customers search for, numbered steps and screenshot placeholders. Use when
  the user asks to turn a fix, a resolved ticket or internal notes into a
  help article.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: support, knowledge-base, documentation
---

# Help-center article

This job writes one help-center article the way a support team would:
the support agent knows what customers see and type when they hit the
problem, and the technical writer turns the fix into steps anyone can
follow. You turn the resolved tickets or engineer's notes in the
conversation into one article ready for review. You never publish the
article or change an existing one.

## Inputs

Required: the problem and its fix, from resolved tickets or an
engineer's notes. Optional: the product's plans or versions the fix
applies to, the help center's style guide or a sample article, existing
articles on the same topic, the product's UI labels.

Ask once, in one message, for anything required that is missing.
Without a style guide, use second person, present tense, short steps.
Without UI labels, use the labels in the material and mark each one to
confirm.

## Steps

1. **Search terms (support agent).** Collect the exact error messages,
   codes and symptom phrases customers used in the tickets, copied
   character for character. These go in the title, the first lines and
   the "Error messages" section.
2. **Audience and scope.** State who the article is for (plan, platform,
   version) and who it is not for. If the fix differs by platform, write
   one section per platform.
3. **Cause.** Explain the cause in two or three sentences a customer can
   follow. Leave out internal system names, ticket numbers, staff names
   and anything the notes mark as internal.
4. **Steps (technical writer).** Number the steps, one action each,
   using the product's UI labels in bold. Add a placeholder
   "[Screenshot: what it shows]" where a customer would need to see the
   screen. Say what the customer should see when each key step works.
5. **If it still fails.** Give what to try next, then how to contact
   support and what to include (the error text, the time, the account
   email).
6. **Related.** List existing articles on the topic and say whether this
   one replaces, extends or overlaps them.
7. **Check** the article against the success criteria and fix what
   fails.

## Success criteria

- The title and the first two lines contain the customer's own error
  text or symptom words.
- Every error message is quoted exactly as in the material.
- Each step has one action, and the steps follow the fix in the
  material without adding any.
- No internal names, ticket numbers or staff names appear.
- Every UI label is from the material or marked to confirm.

## Output

In this order: the title; a one-paragraph summary; "Applies to"; the
cause; the steps; "Error messages" (quoted); "If it still fails";
related articles; notes for the reviewer (labels to confirm, gaps in
the fix); data still needed. Under 600 words for the article itself.
Plain words, no product adjectives.

## Handing off a part

Do every step yourself: one article from one fix holds in one context.
If the resolved tickets are too many to read with the rest, step 1 may
go to a sub-agent with the tickets only, to return the exact error
texts and symptom phrases.
