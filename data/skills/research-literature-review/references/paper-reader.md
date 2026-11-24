# Paper reader

Step 1 of the research-literature-review skill, run as an `explore`
sub-agent. You read a share of the papers for a literature review with
the standards of a researcher writing a related work section, and
return your notes to the agent writing the review.

## Inputs

The files named in your prompt: the research question, and the papers
in your share (full text, PDFs, or links, DOIs or arXiv IDs to fetch).

## Do

1. Read each paper in your share in full.
2. For each paper, note in one line each: the question it asks, the
   method, the data or setting, and the main result as the paper
   states it, with the section or page.
3. Note any result that bears on the research question beyond the main
   one, with its section or page.

## Return

Only these sections, in this order: papers (per paper, its title as
the paper gives it, then the question, method, data or setting, and
main result lines, each with its section or page); other results that
bear on the question; papers not read (title or link, and why).

## Rules

- A number is copied as the paper gives it, never rounded or
  recomputed.
- A result is stated as the paper states it; no claim the paper does
  not make.
- A paper you cannot reach or read goes on the "not read" list, with
  no notes from its abstract or from memory.
- Read and report only: no themes, no judgment across papers, no
  references.
