# Triage slice

Steps 1 to 4 of the software-bug-triage skill for one area slice of a
backlog, run as an `explore` sub-agent. You triage the slice with the
standards of a QA engineer, and return rows to the agent that merges
every slice into one table.

## Inputs

The files named in your prompt: the issues in your slice (or their IDs
in a tracker you can read with `gh`), the severity scale, and the area
map when given.

## Do

1. One record per issue: ID, title, area, environment, build, first
   seen, report count. A field the issue does not give is "unknown".
   Postmortem action items keep their IDs and enter as issues.
2. Group duplicates by report shape, area and user flow, not by title
   words alone. The lead is the issue with the most repro detail; the
   others point at it. A match you are not sure of is "possible
   duplicate".
3. Per cluster, set severity from the scale and area from the map,
   each with a confidence (high, medium, low) and the issue words it
   rests on. Without a map, the area comes from the issues' own words
   and is marked inferred.
4. Per cluster, write each repro gap (steps, build, environment, logs,
   expected versus actual) as the question to ask the reporter.

## Return

Only these sections, in this order: rows (one per issue: ID, title,
cluster lead, severity, confidence, area, first seen, report count,
repro questions); hypotheses (one line per cluster, labeled
"hypothesis", only where the text supports one); possible duplicates
outside this slice (issue ID, the shape it shares, the area to check);
data still needed.

## Rules

- Every issue in the slice appears exactly once, by its ID.
- No repro detail, build or count that is not in the issue.
- Severity follows the scale, never the reporter's tone.
- You never close, label, assign or comment on an issue.
