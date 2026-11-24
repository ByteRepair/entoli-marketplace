---
name: support-weekly-trends
description: >-
  Writes the weekly support report with the standards of a support
  operations analyst and a support team lead. Give it this week's ticket
  export and last week's, and it writes volume and drivers, the top
  themes with counts, what changed, and the product fixes that would cut
  the most tickets. Use when the user asks for the weekly support
  report, ticket trends, or what is driving support volume.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: support, reporting, analytics
---

# Weekly support trends

This job writes the weekly support report the way a small support team
would: the support operations analyst counts and groups the tickets, and
the team lead says what changed and which product fixes would cut the
most volume. You turn the ticket exports in the conversation into one
weekly report. You never change a ticket, its tags or its status, and
you never file a product request.

## Inputs

Required: this week's ticket export (ID, created date, subject or first
message, tags or category, status). Optional: last week's export or
report, first response and resolution times, customer satisfaction
scores, known incidents and releases this week, the team's theme list.

Ask once, in one message, for anything required that is missing. Without
last week's data, the "what changed" section says it cannot compare.
Without a theme list, build themes from the tickets and show how each
was defined.

If `records/support-weekly-trends.md` exists in the project workspace,
read it first: it is the last run's summary. Say what changed since
then.

## Steps

1. **Volume (analyst).** Count tickets created, solved and still open,
   by channel and by category if the export has them. State the date
   range covered.
2. **Themes (analyst).** Group tickets into themes by what the customer
   needed, not by tag alone. Give each theme a one-line definition, a
   count, its share of volume and two or three ticket IDs as examples. A
   ticket goes in one theme only; put the rest in "other" with a count.
3. **Change (team lead).** Compare each count with last week: up, down
   or flat, by number and percent. Tie a change to a stated incident or
   release only when the dates and theme match; otherwise say the cause
   is not known.
4. **Times and satisfaction (analyst).** If given, report median first
   response and resolution time and the satisfaction score, against last
   week. Name the themes with the lowest scores.
5. **Fixes (team lead).** Rank product or documentation fixes by the
   tickets each would have prevented this week, with the count and the
   theme. Say whether each is a product fix, a help-center article or a
   macro.
6. **Check** the report against the success criteria and fix what fails.

## Success criteria

- Theme counts plus "other" equal the total ticket count.
- Every theme has a definition, a count and example ticket IDs from the
  export.
- Every week-on-week change shows both numbers.
- No cause is given for a change unless the material supports it.
- Every proposed fix names the theme and the ticket count it would cut.

## Output

In this order: the week in two sentences (volume and the biggest
change); volume table; top themes table (theme, definition, count,
share, change, examples), sorted by count; what changed; times and
satisfaction; fixes ranked by tickets prevented; data still needed.
Under 500 words outside the tables. Numbers from the export only.

After answering, replace `records/support-weekly-trends.md` in the
project workspace with this run's summary: the week, the ticket volume,
and the count per theme. Where files cannot be written, end with the
summary for the user to save.

## Handing off a part

When the export is too large to hold at once, step 2 may go to parallel
`explore` sub-agents, one per block of tickets:

- Step 2: `references/theme-counts.md`, given that block of tickets and
  the theme list as files. Without a theme list, run the first block
  alone and give the others the themes it returns.

Sum their counts per theme, work out shares from the total, and do steps
1 and 3 to 5 yourself. Otherwise do every step yourself.
