# Ponytail

An agent that codes like the lazy senior developer: it turns a coding
task into the smallest change that fully solves it, plus a reply a busy
human understands in one read.

It is modeled on [ponytail](https://github.com/DietrichGebert/ponytail)
(MIT) by Dietrich Gebert and contributors; the `author` metadata cites
the project's ten top contributors. The core rule it keeps: the best
code is the code never written.

## What you get

- The smallest working diff, found down a ladder: skip what nobody
  asked for, reuse what the codebase already has, prefer the standard
  library, use installed dependencies before adding any, then the
  minimum code that works — finishing every caller, test, and fixture
  the change touches.
- A one-read reply: the change first, then one or two lines on what was
  skipped or not checked and the risk to know.
- Risky logic covered: one small test or self-check per branch, loop,
  parser, or money or security change; `shortcut:` comments for known
  limits; nothing cut at trust boundaries, security, or accessibility.

## Configuring

Name the level in the launching message: lite (build what was asked,
and name the smaller option in one line; you pick), full (the default
rules), or ultra (also push back on anything the need does not
justify). The level holds until "stop ponytail", "normal mode", or
another level name switches it.
