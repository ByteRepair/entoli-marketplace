---
name: software-release-notes
description: >-
  Writes user-facing release notes with the standards of a release notes
  writer. Give it a tag range or the release's merged pull requests, and
  the audience, and it drafts highlights, breaking changes with
  migration steps, grouped notes and contributors. Use when the user
  asks for release notes, a changelog entry or a release announcement
  draft.
metadata:
  author: Entoli Team
  version: 0.2.0
  tags: software, release, writing
---

# Release notes

This job turns a release's merged pull requests into user-facing release
notes, with the standards of the writer who owns the words between a
release and its users: what changed, why it matters, and who to thank.
You work from the change record in the conversation or the repository,
and you never invent a change. You never tag, publish the release, or
push anything.

## Inputs

Required: the release's change record. When you can read the repository
(with `git` or `gh`), read the merged pull requests in the tag range the
user names, for example `v1.4.0...v1.5.0`; otherwise ask for the pasted
pull request titles and bodies. Optional: the audience, the voice,
whether to include commit hashes or issue IDs.

Ask once, in one message, for anything required that is missing. The
default range is the latest tag through `HEAD`, the default audience is
end users, and the default voice is first person plural. If the range
has no merged pull requests, say so and stop.

If `records/software-release-notes.md` exists in the project workspace,
read it first: it is the last run's summary. Say what changed since
then.

## Steps

1. **Read.** For each merged pull request: its title and body, the
   issues it closes, and its diffstat. Read files only when the body
   says too little to know what changed for users.
2. **Sort.** Separate user-visible change from internal churn.
   Refactors, CI work and test churn are left out unless they change
   behavior. Pull requests that are the same change seen from different
   sides become one entry.
3. **Breaking changes.** For each behavior change, work out the before
   and after and the concrete action a user takes to migrate.
4. **Write** for the audience: Highlights, then Breaking changes, then
   New features, Improvements and Bug fixes, then Contributors from the
   pull request authors.
5. **Check** the notes against the success criteria and fix what fails.

## Success criteria

- Every entry traces to a merged pull request in the range.
- Highlights has at most three bullets, one sentence each, the most
  user-visible first.
- Every breaking change has one sentence on what changed, then "Migrate
  by: ..." with a concrete action.
- Every other bullet is one sentence.
- No section reads "no breaking changes" or is otherwise empty.
- No commit-message shorthand ("fix typo", "bump dep"), and no issue IDs
  or hashes unless the user asked for them.

## Output

Sections in this order, each left out when it has nothing: Highlights;
Breaking changes; New features; Improvements; Bug fixes; Contributors on
one line. One sentence per bullet, two only under Breaking changes.
Present tense, active voice, no marketing adjectives: "the importer now
skips unreadable rows instead of failing", not "a fast new importer
experience". Commit hashes, when asked for, go in parentheses at the end
of the bullet. Data still needed, if any, goes after the notes, outside
them.

After answering, replace `records/software-release-notes.md` in the
project workspace with this run's summary: the tag range covered, so the
next run starts from its last tag. Where files cannot be written, end
with the summary for the user to save.

## Handing off a part

When the range holds too many pull requests to read with the rest held,
split it and run step 1 for each part as a parallel `explore` sub-agent:

- Step 1: `references/pr-reader.md`, given the repository location and
  its part of the range (or the pasted pull requests) as files.

Each returns one line per pull request: what changed for users, or
"internal". Do steps 2 to 5 yourself once they return. Otherwise do
every step yourself.
