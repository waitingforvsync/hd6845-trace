# How work is shared

For everyone who traces: the coordinating session, agents it starts, and remote
collaborators and their agents. Read this before taking any work, then
`notes/tracing-guide.md` before tracing anything.

**`/trace6845`** (a Claude Code command in this repository, `.claude/skills/trace6845/`)
runs all of the steps below for one package: pull, choose, claim, trace, review in
rounds until a round finds nothing, merge through the gate, hand off. Collaborators with
write access use it; the steps below are what it does, and what a human tracer does by
hand.

## Roles

- **The coordinator** (the repository owner's session) keeps the master list of tracing
  tasks, `notes/work-packages.md`, and the shared records: `notes/ambiguities.md`,
  `notes/journal.md`, `floorplan.txt`, `PLAN.md`, `CLAUDE.md`, the shared tools and
  `out/`. It merges finished work into main and does the follow-up there.
- **A tracer** (anyone else, human or agent) takes one package at a time from the master
  list, claims it, traces it on a branch, has it reviewed, and opens a pull request.

The coordinator also traces, and follows the same steps: it claims its own packages too,
so that nobody else starts on them.

## The steps

### 1. Pick a package

From the **Queue** of `notes/work-packages.md` (higher rows first), or a `partial` package
in the wave tables whose notes list what is left, or an item of the Re-read list. Run
`tools/claim.py list` first: a package that is claimed is taken. If what you want to do
is not on the list, ask the coordinator to add it rather than inventing a region.

### 2. Claim it: at once, before any tracing

```
tools/claim.py take PREFIX --region "x0-x1 x y0-y1" --what "one line: what you will do"
```

Run it in the main checkout, on branch main: it first pulls (fast-forward only) and stops
if it cannot, so that you claim against the current list. It then pushes
`claims/PREFIX.md` to main as a commit of its own, within seconds, so every
other collaborator sees the claim on their next fetch. It refuses a prefix that is taken
and a region that overlaps an active claim (see its `--help` for `--overlap-ok`, for
wiring that must cross someone else's region). It needs write access to the repository:
ask the owner.

- PREFIX is the package's prefix from the list (`ral`, `tc2`, ...). Continuing a
  `partial` package uses its existing prefix and files.
- One claim per person (or agent) at a time. Finish, or release, before taking another.
- If you stop without finishing, push what you have (steps 4-5), make the block notes say
  where to resume, and run `tools/claim.py release PREFIX --note "why"`.

### 3. Work on your own branch, in your own working tree

```
tools/newwork.sh PREFIX
```

makes a worktree beside the repository on a new branch `PREFIX` from main, links `cache/`
and `.venv/` into it, and pushes the branch. Work there. Never let two agents share one
working tree. A remote collaborator with a separate clone needs `cache/` built once
(`tools/prepare.py`, then `tools/align.py`) (they write only under `cache/`: `align.py` keeps its fit in
`cache/align.json`; the tracked `trace/align.json` is the coordinator's record, changed only
with `--record`, and the merge gate refuses a branch that changes it) and the Python packages listed in `CLAUDE.md`.

What you may change on your branch:

- your own files: `trace/PREFIX*.txt`, `notes/blocks/PREFIX.md`, `floorplan.d/PREFIX.txt`,
  `tools/PREFIX_*.py`, `cache/scratch/PREFIX/`;
- `notes/signals.md`: rows for your new names, and renames made with `tools/rename.py`;
- `notes/operation.md`, when your block changes what is known about clocks, resets,
  comparators or outputs, with each statement marked as that page says;
- another block's trace file only to fix a clear error that blocks your work, as a commit
  of its own whose message says what was wrong and how you know. Notes of other blocks
  that your work contradicts: do not edit them; list the corrections (step 7).

Not on your branch: the coordinator's files listed under Roles, `out/` (never commit it;
it is rebuilt at merge) and `claims/` (only `tools/claim.py` writes there).

### 4. Trace, and ship every finished piece

Follow `notes/tracing-guide.md`: survey, trace a piece, overlay, extract, write it down,
ship:

```
tools/ship.sh "Subject: what was traced" trace/PREFIX.txt notes/blocks/PREFIX.md floorplan.d/PREFIX.txt
```

`ship.sh` commits exactly the named files and pushes your branch, so your progress is
visible to everyone. Timestamps in your notes: `date '+%Y-%m-%d %H:%M %z'` (local time,
with the offset, so that collaborators in other zones line up). Never guess a date.

### 5. Keep your branch current

Merge main into your branch when main has moved and before opening the pull request
(`git fetch origin && git merge origin/main`), then run the checks of step 7 again.
Do not stack your branch on someone else's unmerged branch. If you need their work,
wait for it to be merged, or ask the coordinator to merge it first.

### 6. Independent review: required before the pull request

When the package is traced and its notes are written, someone who did not trace it
checks it against the photos. For an agent, that is one fresh agent started for the
purpose (the one exception to "do not start sub-agents" in the tracing guide). It is what
caught the two worst errors of the first contributor round, both of them a bundle that
steps one track where it had been drawn straight.

Brief the reviewer with:

- the region, `trace/PREFIX.txt`, `notes/blocks/PREFIX.md`, `notes/tracing-guide.md` and
  `notes/layers.md`;
- the list of what the package claims: each join, each gate's equation, each route;
- **what is most likely to be wrong**, to steer its effort: a bridged or swapped track at
  a jog or staircase, a hop drawn straight, a junction judged at low zoom, a contact
  taken from colour alone, a cell copy that differs from its master;
- the instruction to look for errors, not to confirm: read each junction that decides a
  connection at 4x or more in two shots, measure where the eye could be wrong (profiles,
  the metal test, `tools/unsure.py`), and report what it could not check.

The reviewer does not edit the trace. It writes its images to `cache/scratch/PREFIX/review/`
and reports findings with coordinates. The tracer fixes what is confirmed, ships the
fixes, and adds a **Review** section to the block notes: date, reviewer, what was checked
and at what zoom, what was found and changed, what was not checked. A finding that a
method used on earlier blocks can mislead goes into the pull request (step 7) as a
proposed Re-read item; that is how the list stays honest.

### 7. Merge into main through the gate (or open a pull request)

First write and commit your cost report: `python3 tools/costs.py`, then
`tools/ship.sh "Cost report" costs/*.json`. It reads this machine's Claude Code transcripts and
records only numbers (tokens and API-equivalent dollars by package, model and day). The
dashboard adds the reports up, and the gate reads the models: **tracing here is done with
Claude Fable 5.2**, the project's default model (`.claude/settings.json`), and the gate fails a
package that anything else worked on.

With write access, the package goes into main directly, but only through the gate:

```
git fetch origin && git merge origin/main      # resolve: keep both sides' rows in signals.md / operation.md
.venv/bin/python tools/mergecheck.py PREFIX    # until it prints PASS
git push origin HEAD:main                      # rejected? main moved: merge again, gate again
```

`tools/mergecheck.py` checks that the branch contains main, that only your own files,
the glossary, `operation.md` and (named) fixes to other blocks' traces changed, that
the full extraction has 0 errors and 0 warnings, that every name is in the glossary and
no former name is left, that the notes' Review section ends with a clean round ("Round N:
no findings."), and lists the nets newly joined only through `?` items, each of which must
be written up in your notes. Then hand off:

```
tools/claim.py done PREFIX --merged <commit> --handoff FILE
```

FILE holds what you propose for the coordinator's files (the headings are those of the
pull request template below). The claim stays on main, marked "merged, awaiting
coordinator", with the proposals in it, until the coordinator has applied them.

Without write access, or for work that needs discussion first, open a pull request
instead. Run, on your branch, after merging main:

```
.venv/bin/python tools/netlist.py | head -1        # full extraction, no TRACE: 0 errors, 0 warnings
.venv/bin/python tools/signals.py                  # 0 names outside the glossary
.venv/bin/python tools/signals.py --docs           # no former names left
.venv/bin/python tools/unsure.py > /tmp/u_branch.txt   # compare with the same on main
```

Then `gh pr create` against main. The template (`.github/pull_request_template.md`) asks
for: what is traced, the check results, the review, and what you propose for the
coordinator's files (status line for the master list, Re-read items, ambiguities,
corrections to other blocks' notes). Write those proposals out in full; the coordinator
applies them. One package per pull request.

### 8. The coordinator's follow-up

For each claim marked "merged, awaiting coordinator" (and each pull request, which it
merges first): the coordinator reads the notes and the proposals, spot-checks overlays,
runs `tools/unsure.py`, applies the proposals to the master list, the ambiguity register
and other blocks' notes, trims `floorplan.txt`, rebuilds `out/`, writes the journal,
pushes, and releases the claim (`tools/claim.py release PREFIX`). A merged claim keeps
its prefix reserved until then, so nobody continues that package from a stale list.

## The master list

`notes/work-packages.md` is the list of all tracing work: the queue, the status of every
package, the Re-read list and the open joins. Only the coordinator edits it. The aim is
that its regions cover the whole die, because every transistor must be traced (`PLAN.md`,
M7); an area of the die that no package covers is a gap in the list, and should be
reported to the coordinator, not traced on the side.

Active claims are not in that file but in `claims/` on main: `tools/claim.py list`, or the
dashboard at https://waitingforvsync.github.io/hd6845-trace/dashboard/ (claims, the master list on the
die, who did each package, progress), which is rebuilt on every push.

## Concurrency

Everything that changes main is a plain (never forced) push, which the server accepts
only if it is a fast-forward of main as it is at that moment: a push built on an older
main is rejected. Every tool and step that pushes to main reacts to a rejection by
fetching again and repeating its checks: `tools/claim.py` (take, release, done) rebuilds
its commit on the new main and re-checks the prefix and the regions; the merge step merges
main again and re-runs `tools/mergecheck.py`. So two claims of one prefix (or two
overlapping regions) cannot both succeed, and no merge reaches main without passing the
gate against exactly the main it lands on. **Never force-push**: it is the one thing that
defeats this, and GitHub's branch protection on main now refuses it (and deletion of main) for
everyone, administrators included; pull requests and status checks are deliberately not
required, because claims and merges push to main directly. `tools/newwork.sh` starts work only on a claim that is yours.

## Why it is done this way

- `tools/claim.py take` pulls main into your checkout first and refuses a prefix the
  master list does not name: you choose from the current list, never a stale one.
- Claims on main, pushed at once: collaborators in different places see who is where
  before they start, and two claims on one prefix cannot both succeed.
- One branch and one working tree per package: nobody's unfinished files break anyone
  else's extraction, and a pull request contains one package.
- The coordinator's files are edited in one place: in the first contributor round almost
  every merge conflict was in `work-packages.md`.
- Independent review: the error rate of tracing from photographs is the main risk of the
  project (`PLAN.md`, section 6), and a second reader from the photos is the cheapest
  check there is.
