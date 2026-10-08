# Release Notes

An agent that turns a release's merged pull requests into user-facing release
notes: what changed, why it matters, and who to thank.

Give the agent a tag range (for example `v1.4.0...v1.5.0`) and it reads the
PRs, the linked issues, and the diffstats, then drafts notes organized by
user impact rather than by commit message. Internal refactors become a line
under maintenance or disappear; behavior changes get a short before/after.

## What you get

- A Highlights section: at most three bullets, one sentence each, for the
  changes users will actually notice.
- Sections grouped by user impact (new features, improvements, bug fixes,
  breaking changes), each entry written for the release's audience.
- A breaking-changes section written carefully: what callers must do about
  it, not just that something changed.
- A contributors section generated from commit authorship.

## Configuring

Put preferences at the front of the message that launches the agent, for
example the audience (end users, API consumers, or both), whether to include
commit hashes, and the notes' voice (first person plural is the default).

## Files

- `PROMPT.md` — the agent's prompt, loaded by entoli.
- `profile.png` — its avatar.
