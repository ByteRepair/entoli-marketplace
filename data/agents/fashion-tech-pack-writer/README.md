# Fashion Tech Pack Writer

An agent that behaves like a fashion label's technical designer: it
turns design intent into the documents a factory sews from without
asking questions.

Tech packs are the highest-stakes paperwork in an apparel company —
incomplete ones cost extra sample rounds. This agent drafts the pack
sections (BOM, points of measure with tolerances, construction,
grading, care) and writes every fit-round change as a revision entry a
factory can follow.

## What you get

- Complete pack sections in factory-expected order, a tolerance on
  every point of measure.
- A revision log with one entry per change: round, delta, reason.
- Pack reviews that list every gap — with an incomplete pack, "close
  enough" is itself a finding.

## Configuring

Give the style, measurements, materials, and target FOB in the launch
message, and say which round the pack serves. It keeps your imperial or
metric convention exactly as you started.
