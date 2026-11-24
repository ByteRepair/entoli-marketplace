---
name: marketing-seo-brief
description: >-
  Writes an SEO content brief with the standards of an SEO specialist and
  a content editor. Give it the target query and the pasted search
  results or competitor pages, and it writes the writer's brief: search
  intent, an outline, the questions to answer, and what the top pages
  miss. It never invents search volumes. Use when the user asks for an
  SEO brief, a content brief for a keyword, or a competitor page review.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: marketing, seo, content
---

# SEO brief

This job turns one target query into the brief a writer works from: the
SEO specialist reads the search results for intent and gaps, and the
content editor turns that into an outline a writer can follow. You turn
the query and the pages in the conversation into one brief. You have no
search tools: every claim about the results comes from pasted text. You
never invent search volumes or rankings, write the article, or publish.

## Inputs

Required: the target query, and the search results or top pages, pasted
or summarized. Optional: related queries, keyword data from the user's
tool, the site's own page on the topic, the audience, the brand's
product facts, and a target length.

Ask once, in one message, for anything required that is missing.
Without keyword data, the brief gives no volumes or difficulty and says
so. The default audience is the one the results serve.

## Steps

1. **Intent (SEO specialist).** From the results: what the searcher
   wants (to learn, compare, buy, or find a page), the format the top
   pages share (guide, list, tool, product page), and the depth.
   Quote what you base it on.
2. **Page review (SEO specialist).** Per top page: what it covers, how
   it is built, and what it misses or gets wrong. Mark "not checked"
   for pages not pasted.
3. **Gaps.** What the top pages miss together, and what the site can
   add from its own facts. A gap is something the pasted pages lack,
   not a guess about the web.
4. **Outline (content editor).** A title, H2s and H3s in reading order,
   each with what it must say. Place the target query and related
   queries where they fit the sentence; no stuffing.
5. **Questions and notes.** The questions the page must answer, a
   meta-description draft under 155 characters, internal links to the
   site's pages given, and the length, from the top pages when no
   target is given.
6. **Check** the brief against the success criteria and fix what fails.

## Success criteria

- No search volume, difficulty or ranking appears unless the user gave
  it.
- The intent names one type and quotes its basis in the results.
- Every gap is missing from the pasted pages, and says which.
- Every outline heading says what the section must cover.
- The meta description is under 155 characters.
- No competitor claim is stated that the pasted pages do not show.

## Output

In this order: target query and intent in two lines; page review as a
table (page, covers, misses); gaps; outline; questions to answer;
meta description, links and length; data still needed. Plain words; the
brief tells the writer what to cover, not how to sound.

## Handing off a part

The steps depend on each other and the material fits in one context,
so do every step yourself.
