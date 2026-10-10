# Fashion Fit Review Scribe

An agent that behaves like the sample room's fit-session scribe: it
turns what everyone said in the fit session into notes that survive the
session.

Raw fit commentary is contradictory, and half of it is design intent
rather than factory instruction. This agent separates the two, turns
accepted comments into per-measurement instructions, and carries
deferred items between rounds so nothing silently drops.

## What you get

- A fit-notes grid: one row per comment — measurement or area, what was
  observed, the instruction, and its status (open, deferred, fixed).
- Factory instructions written exactly like tech-pack comments.
- A revision summary ready to paste into the tech pack.
- A "resolve with the fitter" list for contradicting comments, kept
  verbatim instead of resolved arbitrarily.

## Configuring

Say which sample round the session serves — first proto instructions
differ from PP instructions.
