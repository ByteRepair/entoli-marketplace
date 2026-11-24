# Theme counts

Step 2 of the support-weekly-trends skill, run as an `explore`
sub-agent, one per block of tickets. You group one block with the
standards of a support operations analyst, and return counts the agent
writing the report can add across blocks.

## Inputs

The files named in your prompt: your block of tickets (ID, created
date, subject or first message, tags or category, status), and the
theme list to use. Without a theme list, you are the first block and
build the themes.

## Do

1. Read each ticket for what the customer needed, not by tag alone.
2. Put each ticket in exactly one theme from the list. A ticket that
   fits none goes in "other".
3. If you build the themes, give each a one-line definition that a
   later block can apply without seeing your tickets.
4. Count the tickets in each theme and in "other", and check that the
   counts add up to the tickets in your block.

## Return

Only these sections, in this order: the block's ticket count and date
range; a table, one line per theme including "other" and themes with
zero tickets (theme, definition, count, two or three example ticket
IDs); the IDs in "other" with a few words each; data still needed.

## Rules

- Counts only, no shares or percents: the runner sums blocks first.
- Use the theme names exactly as given, so blocks can be summed; never
  rename, merge or split a given theme.
- Every count and ID is from the files; nothing is estimated.
- Group only: no week-on-week changes, causes or fixes.
- You never change a ticket, its tags or its status, or file a product
  request.
