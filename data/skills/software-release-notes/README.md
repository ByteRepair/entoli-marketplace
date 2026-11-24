# Software Release Notes

A skill that turns a release's merged pull requests into user-facing
release notes, in one pass: what changed, why it matters, and who to
thank, organized by user impact rather than by commit message.

## What you get

- Highlights: at most three bullets, one sentence each, for the changes
  users will notice.
- Breaking changes, each with what changed and "Migrate by: ..." with
  the action to take.
- New features, improvements and bug fixes as grouped bullets, and the
  contributors on one line.

## Configuring

Name the tag range (for example `v1.4.0...v1.5.0`; the default is the
latest tag through `HEAD`) when the agent can read the repository, or
paste the pull request titles and bodies. Put preferences in the same
message: the audience (end users by default, or API consumers, or
both), the voice (first person plural by default), and whether to
include commit hashes.
