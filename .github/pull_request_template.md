<!-- One package per pull request. Steps: notes/workflow.md. -->

## Package

Prefix: `PREFIX` (claim: `claims/PREFIX.md`). Region: x0-x1 x y0-y1.
Branch is based on main at: <!-- commit -->

## What is traced

<!-- transistors and nets added; the main findings, each marked traced / believed;
what is left (the block notes' Not done) -->

## Checks (on this branch, after merging main)

- `tools/netlist.py`: <!-- N nets, N transistors, 0 errors, 0 warnings -->
- `tools/signals.py`: <!-- 0 not in the glossary; open joins: ... -->
- `tools/signals.py --docs`: <!-- no former names left -->
- `tools/unsure.py`, compared with main: <!-- nets newly joined only through ? items, and why each is acceptable -->
- `tools/ports.py --prefix PREFIX`: <!-- ports.d/PREFIX.txt parses, N ports; each meeting with another package it lists, and whether names, layers and directions agree -->

## Independent review

<!-- who reviewed (agent/model or person), what it was told to suspect, what it checked
and at what zoom, what it found, what was changed, what it could not check.
The block notes carry the same as their "Review" section, whose last line is
"Round N: no findings." or, if the last round's findings were geometry only,
"Round N: no findings that change a connection." with both `tools/sameconn.py` results
("connections identical"). Pieces reviewed together in one round: say which. -->

## For the coordinator

- **Status line for `notes/work-packages.md`**: <!-- -->
- **Re-read items** (a method that turned out to mislead, and the earlier blocks affected): <!-- or "none" -->
- **Ambiguities** (new AMB entries in full, or changes to existing ones): <!-- or "none" -->
- **Corrections to other blocks' notes** (file, what it says, what is true, evidence): <!-- or "none" -->
- **Edits to other blocks' trace files** (commit, what was wrong, evidence): <!-- or "none" -->
- **Floor plan**: <!-- coarse blocks in floorplan.txt that floorplan.d/PREFIX.txt replaces -->
