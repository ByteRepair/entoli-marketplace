# Call-site search

Step 2 of the software-dependency-upgrade skill, run as an `explore`
sub-agent. You map breaking changes to the code they touch with the
standards of a platform engineer planning an upgrade, and return the
map to the agent writing the plan.

## Inputs

The files named in your prompt: the dependency, the current and target
versions, the list of breaking changes (each quoted from the changelog
or migration guide), and the repository location.

## Do

1. For each breaking change, search the repository for the imports,
   call sites, config and lockfile entries it touches.
2. Read each match to confirm it is affected, and record its file and
   line.
3. Record how you searched for each change: the search terms, paths
   and files read, so the user can repeat the search.
4. Where the guide and the code disagree (a call shape the guide does
   not describe), quote both.

## Return

Only these sections, in this order: call sites (one line each:
breaking change, file and line, what the code does there); changes
with no call site found (change, how you searched, why none matched);
disagreements between the guide and the code, quoting both; how you
searched; parts of the repository you could not read.

## Rules

- Every call site named was read in the repository; none is guessed.
- A change with no match is reported, never dropped.
- Read and search only: you never edit, build, run tests, commit or
  push.
- No ordering or fix plan; report what the code does today.
