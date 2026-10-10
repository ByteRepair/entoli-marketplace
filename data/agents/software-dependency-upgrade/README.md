# Software Dependency Upgrade

An agent that behaves like the platform engineer on upgrade waves: the
version bump gets a plan before anyone types a command.

It maps a release's breaking changes to the call sites they actually
touch, orders the upgrade steps (config and build changes first,
call-site edits grouped by file, behavior changes last), and writes
the test focus list from what those changes put at risk. It cannot run
builds or tests — you execute, and the plan says what to verify after
each stage.

## What you get

- An ordered checklist, one action per step, with a verification after
  each stage.
- The breaking-change table: change, affected call sites, fix sketch.
- Changes with no matching call sites, listed for confirmation rather
  than silently dropped.
- The test focus list for this upgrade's specific risks.

## Configuring

Provide the current and target versions, the migration guide text, and
the affected files or lockfile diff. Say whether the upgrade lands as
one wave or staged per service.
