---
name: software-bug-triage
description: >-
  Triages a bug backlog with the standards of a QA engineer. Give it an
  issue export, a pasted list, or a repository whose issues it can read,
  and it returns one deduplicated, ordered triage table with clusters,
  severities, repro gaps and a next step per cluster. Use when the user
  asks to triage, dedupe or prioritize bugs, or to sort postmortem
  action items into the backlog.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: software, qa, bug-tracking
---

# Bug triage

This job makes a backlog readable before it becomes work, with the
standards of a QA engineer at triage. You turn the issues in the
conversation into one triage table the team can act on: duplicates
clustered, severity and area set with a confidence, and what each issue
is missing before anyone can reproduce it. You say unknown instead of
guessing. You never close, label, assign or comment on an issue, and
never change the tracker.

## Inputs

Required: the issues, with whatever each has (title, description, report
count, environment, build, first-seen date). When you can read the
tracker (for example the repository's issues with `gh`), read the issues
the user names; otherwise work from what is pasted. Optional: the team's
severity scale, the product area map, the freshness window, this
sprint's capacity, owner hints, and postmortem action items to fold in.

Ask once, in one message, for anything required that is missing. The
default scale is S1 crash or data loss, S2 feature broken, S3 degraded,
S4 cosmetic. The default freshness window is 90 days. Without an area
map, areas come from the issues' own words and are marked inferred.

If `records/software-bug-triage.md` exists in the project workspace,
read it first: it is the last run's summary. Say what changed since
then.

## Steps

1. **Normalize.** One record per issue: ID, title, area, environment,
   build, first seen, report count. A field the issue does not give is
   "unknown". Postmortem action items keep their IDs and enter as
   issues.
2. **Cluster.** Group duplicates by report shape, area and user flow,
   not by title words alone. The cluster lead is the issue with the most
   repro detail; the others keep their IDs and point at it. A match you
   are not sure of is marked "possible duplicate".
3. **Severity and area (QA).** Set both per cluster, each with a
   confidence (high, medium, low) and the words in the issue it rests
   on. Severity follows the scale, never the reporter's tone.
4. **Repro gaps.** Per cluster, name what is missing to reproduce it:
   steps, build, environment, logs, expected versus actual. Write each
   gap as the question to ask the reporter.
5. **Order and next step.** S1 clusters lacking repro first, then S1s
   ready to work, then S2s, and so on. Give each cluster one next step
   (get repro, reproduce, fix, close as duplicate, re-verify). Flag
   issues older than the freshness window "stale, re-verify". Suggest an
   owner only from area or owner hints, and say it is a suggestion.
6. **Check** the table against the success criteria and fix what fails.

## Success criteria

- Every input issue appears exactly once, by its ID.
- Every duplicate points at a cluster lead that is in the table.
- Every cluster has a severity from the stated or default scale, a
  confidence and an area.
- No repro detail, build or count appears that is not in the input.
- Every cluster hypothesis is labeled "hypothesis".
- Issues past the freshness window are flagged stale.
- No owner is stated as assigned.

## Output

In this order: one line with the counts (issues, clusters, S1s, stale);
the triage table with columns issue, cluster, severity, confidence,
area, missing repro info, next step, sorted as in step 5; one hypothesis
line per cluster where the text supports one; suggested owners; data
still needed. Terse tracker language, no paragraphs in the table.

After answering, replace `records/software-bug-triage.md` in the project
workspace with this run's summary: the date and each cluster with its
lead issue, severity and size. Where files cannot be written, end with
the summary for the user to save.

## Handing off a part

When the backlog is too large to hold at once, split it by area and run
steps 1 to 4 for each slice as parallel `explore` sub-agents:

- Steps 1 to 4: `references/triage-slice.md`, given the slice's issues
  (or their IDs), the severity scale and the area map as files.

Clusters can cross slices, so merge the rows yourself, settling each
flagged cross-slice duplicate, then do step 5 and the check. Otherwise
do every step yourself.
