# HD6845S die trace

Reverse engineering the Hitachi HD6845S CRTC from two die photographs. Read `PLAN.md`
first, then `notes/journal.md` (latest entry) and `notes/ambiguities.md` if they exist.
`notes/operation.md` is the short summary of what is established about how the chip
works (firm / marked / open); the block notes are the deep reference.

## Before you trace anything (everyone: coordinator, agents, remote collaborators)

Several people and agents trace this die at once. The workflow is `notes/workflow.md`;
read it first. **`/trace6845` does all of it for one package** (collaborators with write
access). In short:

1. `git switch main && git pull --ff-only`. Pick a package from the master list
   `notes/work-packages.md` (the coordinator keeps it); check `tools/claim.py list`.
2. **Claim it before doing anything else**: `tools/claim.py take PREFIX --region "..."
   --what "..."` pulls main again, then pushes `claims/PREFIX.md` to main at once, so
   everyone sees it.
3. Work on branch `PREFIX` in a working tree of your own (`tools/newwork.sh PREFIX`),
   touching only your own files (among them `ports.d/PREFIX.txt`, the package's ports, which
   `tools/ports.py` joins up); ship each finished piece with `tools/ship.sh`.
4. Read `notes/tracing-guide.md` before tracing; follow it.
5. **Independent review** against the photos by a fresh reviewer agent: one full review (two
   or three small cells of the same build may share it), then short fix checks of only what
   changed, at most three rounds in all; only findings that change a connection count against
   that limit (geometry-only ones are fixed and shown harmless with `tools/sameconn.py`);
   recorded in the block notes.
6. Merge main into the branch, pass `tools/mergecheck.py PREFIX` (run it unpiped, read `PASS`, and only
   then push, in a separate command: a pipe such as `| tail` hides a failing gate from `&&`), push to main, and hand
   off with `tools/claim.py done` (proposals for the coordinator's files go there, not in
   those files). Without write access: a pull request with the template instead.

## Standing rules from the user

- **Tracing is done with Claude Fable 5.2** (user, 2026-11-17: "insist that only Fable 5.2 is
  used by a collaborator"). `.claude/settings.json` makes it the project's default model,
  `/trace6845` runs on it and starts its reviewers on it, and the merge gate fails a package
  whose cost report (`tools/costs.py`, committed as `costs/<git name>.json`) shows any other
  model doing its work. The coordinator may use another model for coordination
  (`.claude/settings.local.json`).
  Work merged anyway from another model (dp111's Opus pieces, 2026-11-18) stays on main
  but gets a Fable review (re-read item R31); no more such merges (user, 2026-11-18).

- Trace independently. Do not open Lance Ewing's HD6845 reverse-engineering work (on
  GitHub) or any other 6845 netlist/schematic effort until our own trace of the
  relevant block is complete. After that it may be used as confirmation only, never as
  a starting point.
- The datasheet (`datasheets/`), the CPC document (`docs/ACCC1.8-EN.pdf`, which calls
  this chip "CRTC type 0") and beebjit are sources of observed behaviour. None of them
  is assumed to be 100% accurate.
- When something is ambiguous, note it and keep tracing so it can be resolved from
  another direction. If one reading fits the documentation, adopt it cautiously and
  record it as an assumption so it can be rethought if later tracing conflicts.
- Refer to features by pixel coordinates of the metal shot
  (`dieshots/hd6845metal2ndchip.jpg`, 19838 x 21025, origin top-left).
- Name signals from pin names, register numbers and counter numbers.
- **Signal names** (user, 2026-11-16): every label must be meaningful, or be described
  in a table where it cannot be named yet, and every document must use the current
  names. The glossary is `notes/signals.md`: read its rules. A signal is named for what
  it is as soon as that is known, and until then for where it is; when it is identified,
  rename it everywhere with `tools/rename.py OLD NEW` and add it to the glossary's
  tables. `tools/build.py` reports any net name the glossary does not cover: that count
  stays at zero. Names ending in `_u` are open joins and are tasks.
- N-bit comparators and similar may be left as blocks. Derived signals, latches,
  flip-flops and glue gates are wanted in full, especially the end-of-frame state
  machine, the interlace odd/even logic, and whatever makes some registers hold N and
  others N-1.

- **All transistors are to be traced** (user, 2026-11-15): a "visual 6845" (the layout
  in a browser with a switch-level simulation of the extracted netlist running on it)
  is a deliverable once tracing is complete. Schematics may show a comparator as a
  block; the trace and netlist may not leave anything out. See `PLAN.md` M7.
- Schematics (user, 2026-11-15): higher-order structures (N-bit registers, comparators,
  counters) are drawn as blocks, **and** one instance of each kind gets its own
  gate-level sheet. So every block's notes must give the bit cell's gates in full.
- **Re-read rule** (user, 2026-11-15): when tracing shows that a method used on earlier
  blocks can miss or misread things, the affected blocks go on the "Re-read list" in
  `notes/work-packages.md` in the same commit, as tasks with a region and a reason, and
  the lesson goes into the traps of `notes/tracing-guide.md`. A mention in the journal
  or in a report does not count. The list is worked off before simulation (M5).
- The user also wants a floor-plan overlay (`floorplan.txt` -> `out/floorplan.jpg`)
  kept current: rename and tighten a block whenever tracing identifies it.

## Practical

- **Dates** (user, 2026-11-16: "the journal dates are nonsense"): take the date and time
  from `date`, and when something was done from `git log`. Never advance the date by
  guess between pieces of work. Journal headings carry date and time (`## YYYY-MM-DD
  HH:MM  title`).
- **`notes/operation.md`** (user, 2026-11-16): keep it current and readable. It states
  only what the extraction supports, marked firm (`tools/unsure.py --equations` says the
  equation survives without every uncertain item), marked, or open. When a block changes
  what is known about clocks, resets, comparators or outputs, update it in the same
  commit.

- Use `.venv/bin/python` (shapely, opencv, scikit-image, networkx are installed there).
- `cache/` is derived data and is not in git. `tools/prepare.py` then `tools/align.py`
  rebuild it. Every shot is resampled into the frame of the chip-2 metal shot, so all
  tools take the same coordinates for every layer.
- Five shots, as `view.py --layers` names: `metal`, `acid` (chip 2: metal intact,
  metal stripped) and `metal1`, `acid1`, `acid1b` (chip 1, added 2026-11-14).
  **`acid1b` (hd6845acid2.jpg) is the clean one**: no interference fringes, readable
  under where the metal rails were. Use `metal`, `acid` and `acid1b` together. Poly is
  easiest in `acid`; diffusion, contacts and anything under metal in `acid1b`. Its
  colour legend is in `notes/layers.md`.
- Keep large arrays on disk under `cache/`, not in `/tmp`: `/tmp` is RAM-backed here
  and the machine has 12 GB. Scratch renders go in `cache/scratch/`.
- `tools/view.py x y w h --scale 2.5 --grid 50 [--layers metal,acid] [--stack v]
  [--trace] [--nofill] --out FILE` renders a view. Keep each output under about
  1400 px a side or it is downscaled when read. `--trace --nofill` is the clearest
  way to check a trace against the photo.
- `tools/netlist.py` prints the extraction report; `HD_COORD=1 tools/build.py` regenerates `out/` (coordinator only; `--check` prints the report lines and writes nothing).
- Trace file format: docstring of `tools/tracelib.py`. Layer legend and what each
  feature looks like: `notes/layers.md`. Read that before tracing anything.

## Parallel work and the coordinator

How work is shared is `notes/workflow.md` (claims on main, one branch and one working
tree per package, independent review, pull requests). This section is for the
coordinating session, the owner's.

- The coordinator alone edits `notes/work-packages.md` (the master list of tracing
  tasks, which must cover the whole die), `notes/ambiguities.md`, `notes/journal.md`,
  `floorplan.txt`, `PLAN.md`, this file and the shared tools, and alone runs
  `HD_COORD=1 tools/build.py` on main and commits `out/`. It commits on main with
  `HD_COORD=1 tools/ship.sh ...`.
- Its own tracing follows the workflow too: claim the package first (`tools/claim.py
  take`), so that collaborators do not start on it. **While unsupervised it works
  serially** (user, 2026-11-16: "while unsupervised, just work serially, rather than
  trying to do things with multiple agents in parallel"): one package at a time, in the
  priority order of the queue; the one agent it starts per package is the independent
  reviewer, and it waits for it.
- At the start of every session, and when told a package is in: `git pull`, then
  `tools/claim.py handoffs`. For each handoff in `handoffs/` (and each pull request, merged
  first): read the notes and the proposals in the handoff file, spot-check an overlay, run
  the full extraction (no `TRACE`) and `tools/unsure.py`, apply the proposals (master list
  status, Re-read items, ambiguities, other blocks' notes), trim the coarse block in
  `floorplan.txt` that its `floorplan.d` fragment replaces, rebuild `out/`, write the
  journal, `git rm` the handoff, push. Claims are the tracers' own: they keep them while
  they work and release them when they stop; the coordinator releases only a stale one,
  after asking its owner.
- **`/refresh6845`** (`.claude/skills/refresh6845/`): rename placeholders the trace has
  identified (checked with `tools/names.py compare`: only names may change), bring
  `notes/operation.md` up to date, rebuild `out/`, journal. Run it after a batch of merges.
- Keep the master list covering the whole die: after changing it, `tools/coverage.py`
  must show no red (untraced and in no package) except empty field and supply metal. Its stricter line, "untraced and in no Queue row", must also hold only empty field, supply metal and the die marking: a partial package or an untraced spot that no Queue row names is picked by no one (2026-11-19). Stacked pull requests: merge the tips (the first round's notes are in
  the journal, 2026-11-17).
- Every tracer, whoever: `notes/tracing-guide.md`. Tools run through `tools/t.sh PREFIX
  tool.py ...` (sets `TRACE=PREFIX` so other blocks' unfinished files are not loaded).
- `trace/examples/` holds worked examples that are not part of the chip's trace.
