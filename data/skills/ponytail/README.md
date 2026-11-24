# Ponytail

The lazy senior developer from
[ponytail](https://github.com/DietrichGebert/ponytail) by Dietrich Gebert
(MIT): the smallest change that fully solves the task, and a reply a busy
human understands in one read. The best code is the code never written.

This is a copy of upstream's `ponytail` skill, kept as it was published,
with `argument-hint` moved under `metadata:` as the Agent Skills spec
requires. It is not kept in sync with upstream.

## What you get

- The smallest working change, found down a ladder: skip what nobody asked
  for, reuse what the codebase has, the standard library, installed
  dependencies, then the minimum code that works.
- Every caller, test and fixture the change touches, finished.
- A reply that ends with what was skipped or not checked, and the risk to
  know.

## Configuring

Run `/ponytail`, optionally with a level: lite (build what was asked
and name the smaller option), full (the default), or ultra (also push back
on anything the need does not justify). It holds for the session until
"stop ponytail" or "normal mode".
