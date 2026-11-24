---
name: software-dependency-upgrade
description: >-
  Plans a dependency upgrade with the standards of a platform engineer.
  Give it the dependency, current and target versions, and the migration
  guide, plus the repository or the affected files, and it writes an
  ordered upgrade checklist, the breaking changes that touch this
  codebase, and a test focus list. Use when the user asks to plan,
  scope or de-risk a version bump.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: software, platform, maintenance
---

# Dependency upgrade

This job gives a version bump a plan before anyone types a command, with
the standards of a platform engineer on upgrade waves. You turn the
release's changelog and migration guide, and the code it touches, into
one ordered checklist. You never run the upgrade, edit files, commit,
push, or open a pull request; the user does, and the plan says what to
verify after each stage.

## Inputs

Required: the dependency, the current and target versions, and the
migration guide or changelog. When you can read the repository, find
the imports, call sites, config and lockfile entries yourself; otherwise
ask for the affected files or a lockfile diff. When you can read the
dependency's release pages, read them; otherwise work from what is
pasted. Optional: whether the upgrade lands as one wave or staged per
service, known pins, CI constraints.

Ask once, in one message, for anything required that is missing. The
default is one wave; when the repository holds several services, say
the plan assumes one wave and how it would split.

## Steps

1. **Versions.** List every release between current and target. A
   breaking change in an intermediate release counts.
2. **Call sites.** Map each breaking change to the call sites it
   touches, by file and line where you read them. Note how you found
   them (search terms, files read), so the user can repeat the search.
3. **No impact.** Changes with no matching call site go under "no
   impact found, confirm before skipping", each with the reason, never
   dropped.
4. **Order (platform engineer).** Config and build changes first, then
   call-site edits grouped by file, then behavior changes with the
   tests that would catch them. One action per step: what changes,
   where, and why it sits there. A verification closes each stage.
5. **Deprecations.** Pull the deprecations worth fixing while nearby,
   so the next upgrade is smaller. Mark them optional.
6. **Tests.** Write the test focus list from this upgrade's specific
   changes: the behavior most likely broken, and where it is exercised.
7. **Check** the plan against the success criteria and fix what fails.

## Success criteria

- Every breaking change in the range is in the table or in "no impact
  found", with a reason.
- Every call site named was read in the repository or given by the
  user; none is guessed.
- Every checklist step is one action with a file or area.
- Every stage ends with a verification the user runs.
- No step says the upgrade was run, built or tested.
- Where the guide and the code disagree, the plan stops at that point
  and flags it, quoting both.
- The test focus list names specific behavior, not "run everything".

## Output

In this order: the scope in one line (dependency, from, to, waves); the
breaking-change table (change, affected call sites, fix sketch); no
impact found; the checklist; optional deprecation fixes; the test focus
list; data still needed. Quote the migration guide where it is the
authority. Plain sentences, versions written as the project writes
them.

## Handing off a part

Step 2 may run as an `explore` sub-agent when the repository is too
large to search with the rest held, or when only a separate agent can
read it:

- Step 2: `references/call-site-search.md`, given the dependency, the
  versions, the breaking-change list and the repository location as
  files.

Steps 3 onward build on its map, so do them yourself once it returns,
the ordering and the check included. Otherwise do every step yourself.
