---
name: marketing-performance-readout
description: >-
  Writes a campaign or channel performance readout with the standards of
  a marketing analyst and a channel manager. Give it the metrics exports
  and the targets (or the campaign brief), and it writes the readout:
  results against targets, what drove them, and what to stop, keep and
  start, with no causal claim the data cannot support. Use when the user
  asks to read out, review or explain marketing results.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: marketing, analytics, reporting
---

# Performance readout

This job reads out one campaign or one period of channel results: the
marketing analyst checks the numbers against the targets and says what
the data can and cannot show, and the channel manager turns that into
what to stop, keep and start. You turn the exports in the conversation
into one readout. You work only from that material. You never change a
budget, pause a campaign or edit a target.

## Inputs

Required: the metrics exports (by channel, campaign or ad, with dates)
and the targets, or the campaign brief that states them. Optional: spend
by channel, the prior period or a baseline, notes on changes made during
the run (new creative, budget moves, outages), and the business goal.

Ask once, in one message, for anything required that is missing. Without
targets, report results against the prior period and say no target was
given. Without spend, no cost metric is reported.

If `records/marketing-performance-readout.md` exists in the project
workspace, read it first: it is the last run's summary. Say what changed
since then.

## Steps

1. **Clean the data (analyst).** State the date range and the source of
   each number. Where exports disagree (an ad platform and analytics),
   report both and say which the readout uses. Flag gaps in dates.
2. **Results against targets (analyst).** Each target: the result, the
   gap in number and percent, and the verdict (hit, missed, or no data).
   Show the arithmetic for derived numbers (cost per result, conversion
   rate).
3. **What drove it (analyst).** Name the channels, campaigns or ads that
   made up most of the result or the gap, with their share. Say
   "coincided with" for a change and a result in the same period; say
   "caused" only when a test with a control shows it. Small samples are
   flagged with the count.
4. **Stop, keep, start (channel manager).** Each line ties to a number
   from steps 2 and 3. A "start" with no data behind it is labeled a
   test to run, with what it would measure.
5. **Check** the readout against the success criteria and fix what
   fails.

## Success criteria

- Every number is in an export or shown as arithmetic on one.
- Every target has a verdict: hit, missed, or no data.
- No "caused", "drove" or "because" claim rests on timing alone.
- Where sources disagree, both numbers are shown.
- Every stop, keep and start line cites a number or is labeled a test.
- No budget change is stated as done; changes are recommendations.

## Output

In this order: the headline in one sentence (met, partly met, or missed,
against what); results against targets as a table (metric, target,
result, gap, verdict); what drove the result; stop, keep, start; caveats
on the data; data still needed. Under one page. Plain sentences, past
tense for results.

After answering, replace `records/marketing-performance-readout.md` in
the project workspace with this run's summary: the period and each
channel's results against its targets. Where files cannot be written,
end with the summary for the user to save.

## Handing off a part

When exports for many channels are too large to hold together, steps 1
and 2 may run as parallel `explore` sub-agents, one per channel:

- Steps 1 and 2: `references/channel-results.md`, given that channel's
  exports and its targets (and its spend and prior period) as files.

Steps 3 and 4 compare across channels, so do them yourself once the
results return. Otherwise do every step yourself.
