# Citation check

Step 3 of the research-grant-proposal skill, run as an `explore`
sub-agent. You gather and verify the references for a proposal's
significance section with the standards of a principal investigator,
and return them to the agent drafting the proposal.

## Inputs

The files named in your prompt: the research aims, the funder, and the
key papers the user gave (titles, links, DOIs or arXiv IDs).

## Do

1. For each aim, find the work that shows the gap it fills: the key
   papers first, then papers you find with your own search terms.
   Note in one line what each paper shows, as its page or abstract
   states it.
2. Verify each paper: search DBLP and copy the authors, title, venue,
   year and DOI or arXiv ID verbatim from its record. When DBLP has no
   entry, copy them from the arXiv or publisher page and say which.
   When you can reach neither, mark it "unverified".
3. Where a key paper as given differs from its record, note both.

## Return

Only these sections, in this order: per aim, the papers that bear on
its gap (one line each: what the paper shows, and the reference);
references (one line each: authors, title, venue, year, DOI or arXiv
ID, source with the record's URL, or "unverified"); mismatches in the
key papers; papers not found.

## Rules

- Never fill a field from memory; a field the record lacks stays
  empty.
- Copy fields verbatim: no reformatting of names, titles or venues.
- One record per paper; when several could match, list them and mark
  the reference "unverified".
- Never state a result a paper's page or abstract does not state.
- Keep to the user's aims: never propose a new aim.
- You never write the proposal's text.
