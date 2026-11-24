# Software Dependency Upgrade

A skill that plans a dependency upgrade with the standards of a platform
engineer, in one pass: the version bump gets a plan before anyone types a
command.

## What you get

- The breaking-change table: each change, the call sites it touches in
  your code, and a fix sketch.
- Changes with no matching call site, listed for confirmation rather
  than dropped.
- An ordered checklist, one action per step, with a verification after
  each stage, and a test focus list for this upgrade's risks.

## Configuring

Name the dependency, the current and target versions, and paste or link
the migration guide. When the agent can read the repository it finds the
call sites itself; otherwise paste the affected files or a lockfile
diff. Say whether the upgrade lands as one wave (the default) or staged
per service. It never runs the upgrade, commits or pushes.
