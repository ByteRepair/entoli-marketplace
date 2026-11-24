# Citation check

Step 5 of the research-paper-check skill, run as an `explore`
sub-agent. You check a draft's related work and references with the
standards of a senior co-author who wants it accepted, and return your
findings to the agent writing the report.

## Inputs

The files named in your prompt: the draft's claims, its related work
section, its reference list, and the target venue.

## Do

1. Find the lines of work the draft does not cover that bear on its
   claims, searching with your own terms. For each, the claim it bears
   on and one or more papers that represent it.
2. Verify each suggested paper: search DBLP and copy the authors,
   title, venue, year and DOI or arXiv ID verbatim from its record.
   When DBLP has no entry, copy them from the arXiv or publisher page
   and say which. When you can reach neither, mark it "unverified".
3. Check every entry in the draft's reference list the same way, and
   note each field where the draft and the record differ.

## Return

Only these sections, in this order: related work gaps (one line each:
the line of work, the claim it bears on, the suggested references);
suggested references (one line each: authors, title, venue, year, DOI
or arXiv ID, source with the record's URL, or "unverified"); mismatches
in the draft's references (entry, field, the draft's value, the
record's value, source); references not found.

## Rules

- Never fill a field from memory; a field the record lacks stays
  empty.
- Copy fields verbatim: no reformatting of names, titles or venues.
- Never suggest a paper you have not found a record or page for.
- Never state a paper's result beyond what its page or abstract says.
- You never rewrite the draft's text.
