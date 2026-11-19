---
name: refresh6845
description: Coordinator housekeeping for the HD6845S die trace - rename placeholder signals whose identity the trace now establishes, bring notes/operation.md up to date with the extraction, regenerate out/, and push. Run by the repository owner's coordinating session, on main.
argument-hint: "[--no-renames]  (optional: only operation.md and out/)"
disable-model-invocation: true
---

# /refresh6845: renames, operation.md, out/

This is the coordinator's job (`CLAUDE.md`, "Parallel work and the coordinator"): it
edits files across every block, `notes/operation.md` and `out/`, and writes the journal.
Run it in the main checkout, on main. Do the steps in order. Each step ends in a commit,
so a failure later leaves the earlier steps done and pushed. If a check fails and these
instructions do not say what to do, stop and report. Never push a failing state.

## 0. Start

Never force-push (`--force`, `--force-with-lease`). A rejected push means someone else
pushed first: pull, re-check, push again.


```
git switch main && git pull --ff-only
tools/claim.py list
```

Run `tools/claim.py handoffs`: unprocessed handoffs in `handoffs/` are a separate job
(the coordinator's follow-up), but their notes are input to step 2. Find the last journal
entry titled "Refresh" (`grep -n '^## .*Refresh' notes/journal.md | tail -1`): what was
merged since then is what this run must take in. Read those journal entries, the master
list's `rename` row, `notes/signals.md` (its rules first), `notes/operation.md`, and the
block notes of every package merged since.

## 1. Baseline

```
mkdir -p cache/scratch/refresh
.venv/bin/python tools/netlist.py | head -1                              # must be 0 errors, 0 warnings
.venv/bin/python tools/names.py snapshot cache/scratch/refresh/before.json
.venv/bin/python tools/unsure.py --equations > cache/scratch/refresh/eq_before.txt
```

## 2. Renames (skip with --no-renames)

```
.venv/bin/python tools/names.py candidates
```

Decide each rename yourself. The tool only finds candidates.

**When to rename.** A placeholder (a block prefix and a local name, or an older name kept
as an `@alias`) is renamed when the trace establishes what the signal is:

- a join to a net that already has a functional name, on **firm** geometry
  (`names.py candidates` section 1; never section 2, trap 17 of the tracing guide);
- or an identity the block notes and `notes/operation.md` mark as traced, not believed:
  a register's bits found by its write strobe and the data bus, a counter's bits by
  their joins, a comparator's output by both of its inputs.

- **or two or more names on one net, on firm geometry, whatever kind of names they are** (user,
  2026-11-19: "rename / consolidate any signals which are known to be the same with their proper
  name. I thought that was the point in the rename step"). `names.py candidates` lists only nets
  with a functional name; placeholder-to-placeholder aliases are consolidated too, onto the net's
  canonical name (the first word of its `@alias` lines), so that after a refresh the only `@alias`
  lines left are joins through an uncertain item and cell pin names made from a template. A signal
  on several nets that is known to be one signal (buffered copies) gets names that say what it is
  (`rst_ck`, `rst_rc`, `rst_lat`), not what it was once believed to be.

Leave alone: identities that are "believed", "by position", "from the datasheet" or
marked in `operation.md`; aliases whose glossary row says why both names are kept (for
example a cell's own name for a pin it shares); and supply nets. When in doubt, do not
rename: write in the glossary row what is known, and list the doubt in the journal entry.

**What to call it.** By `notes/signals.md`'s rules, and consistent with the names
already in the glossary: pin names as on the datasheet; register bits `r<reg>_b<bit>_q`
(and `_a`, `_n2` for the latch's nodes, as `r3_b7_*`); write strobes `wr_r<reg>`; counter
bits `hc3`, `rc2`, `sl1`; comparator results `<counter>_eq_r<reg>`; data bus lines by
the names the glossary already uses for that bit. Bit numbers must come from the trace
(the carry direction, the data bus fan-out), never from a guess about layout.

**How.**

- Before renaming an alias onto its canonical name, reword the sentences that name both ("A is B"
  becomes "B is B"): describe the old wire ("the wire `tl5` called w5936 is `tl3_w3982`"). Keep the
  journal's rename records (lines with `->`) as written; put the catch-up `tools/rename.py` commands
  for branches in flight into the journal entry.
- Labels drawn in trace files: `tools/rename.py OLD NEW [OLD NEW ...]`. It renames in
  trace files, notes, plan and floor plan, drops `@alias` lines that become self-aliases,
  and adds rows to "Former names".
- Names made from a cell template (`N ... cdp1_{}_q` with `@inst ... tag=a0`):
  `rename.py` cannot reach them. Change the template so that the tag is the whole stem
  (`{}_q`), and set every `@inst` tag of that cell, **in every file that uses the cell**
  (`grep -n "@inst CELLNAME" trace/*.txt`), to the full stem: the new name where the
  instance is identified (`tag=r8_b5`), the old full stem where it is not
  (`tag=cdp1_c5`), so that unidentified instances keep their names. Then run
  `tools/rename.py` with the concrete old and new names for the notes and the glossary.
- Glossary: a row for every new name, saying what it is and how that is known (moved
  and corrected from the placeholder's row); remove placeholder pattern rows that no
  longer match any net; keep "Former names" (rename.py fills it).
- Do it in batches of related names (one register, one bus). After each batch:

```
.venv/bin/python tools/names.py compare cache/scratch/refresh/before.json   # must end "only names changed"
.venv/bin/python tools/signals.py            # 0 not in the glossary
.venv/bin/python tools/signals.py --docs     # no former names left
```

`compare` lists every net whose names changed. Read the list: every line must be a
rename you meant. If it passes, commit the batch locally (`git add trace notes floorplan.d
floorplan.txt PLAN.md CLAUDE.md && git commit -m "Refresh: rename <batch>"`), not yet
pushed. If it fails (a transistor or a connection differs, or a net lost its names),
undo only this batch (`git checkout -- .` back to the last batch's commit) and find out
why before trying again.

When all batches pass, update the master list's `rename` row (what was renamed, what is
left and why), commit it, and push:

```
git push origin main
```

If the push is rejected, someone merged a package meanwhile: `git pull --rebase origin
main`, then rename anything their package added under an old name (`tools/rename.py`
again), check the extraction, `signals.py` and `signals.py --docs`, and push.

**Tell collaborators.** Branches in flight that use an old name will fail
`tools/mergecheck.py` (former names) until they run `tools/rename.py OLD NEW` after merging
main. `/trace6845` already says so. List the renames in the journal entry (step 5).

## 3. `notes/operation.md`

The page states only what the extraction supports, each statement marked **firm**
(`tools/unsure.py --equations` says the equation survives without every uncertain
item), **marked** (extracted, but resting on a `?` item or an undrawn join; name the
assumption), or **open**. Keep its structure and its plain style.

```
.venv/bin/python tools/unsure.py --equations > cache/scratch/refresh/eq_after.txt
.venv/bin/python tools/netlist.py | head -1
```

- Update the header line (date from `date '+%Y-%m-%d'`, nets, transistors) and the count
  of firm equations.
- Every name on the page is the current name (`signals.py --docs` checks former names).
- Take in each package merged since the last refresh: what it establishes about clocks,
  counters, registers, comparators, the row address, outputs and the step logic. Add or
  change rows; move an item between open, marked and firm only on evidence, and check
  each equation you cite against `eq_after.txt` (FIRM or DEPENDS).
- Compare `eq_before.txt` with `eq_after.txt` for equations that changed status, and make
  the page agree.
- Update "Not established at all" and the closing references (AMB range, Re-read range).
- Do not add anything the extraction does not support. A belief goes in as "believed"
  with its source, or not at all.

Commit and push: `git add notes/operation.md && git commit -m "Refresh: operation.md (<summary>)" && git push origin main`.

## 4. `out/` and your cost report

`python3 tools/costs.py` updates `costs/<your git name>.json` for the dashboard (numbers only).

```
HD_COORD=1 .venv/bin/python tools/build.py
```

It must report 0 errors, 0 warnings and 0 names outside the glossary. Look at the
floor plan (`out/floorplan.jpg`, a crop around blocks changed since the last refresh)
for labels that overlap or blocks drawn in the wrong place. Fix their `floorplan.d`
fragment or `floorplan.txt` and rebuild. Run `tools/coverage.py` and note its three
percentages. Commit and push:

```
git add out floorplan.txt floorplan.d costs && git commit -m "Refresh: out/ rebuilt (<nets> nets, <transistors> transistors)" && git push origin main
```

## 5. Journal and report

Append a journal entry `## YYYY-MM-DD HH:MM  Refresh` (time from `date`): the renames
(old -> new, by batch), what changed in `operation.md`, the extraction and coverage
figures, and anything left unrenamed on purpose, with the reason. Commit and push it
(`HD_COORD=1 tools/ship.sh "Refresh: journal" notes/journal.md`). Then report to the
user in under 250 words.
