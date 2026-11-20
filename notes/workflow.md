# How work is shared

For everyone who traces: the coordinating session, agents it starts, and remote
collaborators and their agents. Read this before taking any work, then
`notes/tracing-guide.md` before tracing anything.

**`/trace6845`** (a Claude Code command in this repository, `.claude/skills/trace6845/`)
runs all of the steps below for one package: pull, choose, claim, trace, review in
a full review then fix checks until a round finds nothing that changes a connection (at most
three rounds), merge through the gate, hand off. Collaborators with
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
  `ports.d/PREFIX.txt` (your ports, one per line: tracing guide, section 8),
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

Follow `notes/tracing-guide.md`: survey (written to `cache/scratch/PREFIX/` before anything
is drawn), trace a piece, overlay, extract, write it down, ship:

```
tools/ship.sh "Subject: what was traced" trace/PREFIX.txt notes/blocks/PREFIX.md floorplan.d/PREFIX.txt ports.d/PREFIX.txt
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
checks it against the photos. The first round is a full review; later rounds are fix checks,
which look only at what changed since the previous round and at what it touches, so that the
review stays affordable (a full round costs about as much as a tracing run). At most three
rounds: a package that still has confirmed findings that change a connection after the third
is not ready to merge. For an agent, each round is one fresh agent started for the
purpose (the one exception to "do not start sub-agents" in the tracing guide). It is what
caught the two worst errors of the first contributor round, both of them a bundle that
steps one track where it had been drawn straight.

**Small pieces are reviewed together.** A full review has a large fixed cost (the reviewer
reads the guide and calibrates its eye on the colours before it looks at anything): one
reviewer used about 250,000 tokens on a three-transistor NOR. So when the pieces are small
cells of the same build (the same kind of gate in one column or row, read by the same
method), trace two or three of them and put them through one full review: **at most three
pieces and about a dozen transistors in one review**. Each piece is still shipped to the
branch as it is finished; only the review and the merge wait. The one brief lists every
piece: its region, its claims, and its own suspicions. Do not batch a piece that is of a
different build, that another piece's reading depends on (review the first before building
on it), or that is large enough to fill a review by itself; and do not hold finished
pieces back at the end of a session to fill a batch.

Brief the reviewer with:

- the region, `trace/PREFIX.txt`, `notes/blocks/PREFIX.md`, `notes/tracing-guide.md` and
  `notes/layers.md`;
- the list of what the package claims: each join, each gate's equation, each route (for a
  batch, piece by piece);
- **what is most likely to be wrong**, to steer its effort: a bridged or swapped track at
  a jog or staircase, a hop drawn straight, a junction judged at low zoom, a contact
  taken from colour alone, a cell copy that differs from its master;
- the instruction to look for errors, not to confirm: read each junction that decides a
  connection at 4x or more in two shots, measure where the eye could be wrong (profiles with
  `tools/px.py`, text maps with `tools/textmap.py`, the metal test, `tools/unsure.py`), and
  report what it could not check, and for each finding whether it changes a connection;
- the practical lines, which every tracer otherwise adds by hand: the shell's directory
  resets after every command, so each command starts with `cd <worktree> &&`; images go in
  this round's own folder, `cache/scratch/PREFIX/review-N/` with N the next number not yet
  used there, by passing `--out cache/scratch/PREFIX/review-N/NAME.png` (a bare `--out NAME.png`
  lands in `cache/scratch/PREFIX/` among the tracer's images; a name with a folder in it is
  taken relative to the working tree); not to read the notes' Review section (earlier
  reviewers' conclusions); not to start agents of its own; no web, and no other
  reverse-engineering of the 6845.

The reviewer does not edit the trace. It reports findings with coordinates. The tracer
checks each, fixes what is confirmed, ships the fixes, and adds a **Review** section to the
block notes: date, reviewer, what was checked and at what zoom, what was found and changed,
what was not checked. A finding that a method used on earlier blocks can mislead goes into
the pull request (step 7) as a proposed Re-read item; that is how the list stays honest.

**Only findings that change a connection count against the three rounds.** A package was
once kept out of main by a third round whose findings were a rail's width, a diffusion's
width and a direction in a comment. The rule since 2026-11-17:

- A finding **changes a connection** if fixing it changes which nets are joined or apart,
  which net any transistor's gate or channel end is on, whether a transistor or a contact
  exists, any recovered equation, or where a wire leaves the package (a port's place or
  side). Everything else is **geometry only**: a width, a length, an edge a few pixels off,
  the path of a wire between the same two ends, a comment.
- A geometry-only finding is fixed and recorded like any other. It does not use up a round
  and does not by itself call for a further fix check, **provided the tracer shows that the
  extraction's connections are the same before and after the fix**:

  ```
  tools/t.sh PREFIX sameconn.py <commit before the fixes>     # the package alone
  .venv/bin/python tools/sameconn.py <commit before the fixes>   # every trace file
  ```

  Both must end `connections identical` (`tools/sameconn.py` compares the nets' names, every
  transistor's three nets and the equations, and ignores sizes and positions; its docstring
  says what it cannot see). Record both commands and their last lines in the Review section.
  If either says `CONNECTIONS DIFFER`, the fix changed a connection: it is treated as one,
  and goes to a fix check.
- A round is written into the Review section with one of these last lines, which the merge
  gate reads:
  - `Round N: no findings.`: nothing confirmed (nothing found, or every finding refuted
    with evidence);
  - `Round N: no findings that change a connection.`: confirmed findings, all geometry only,
    all fixed, with the `connections identical` proof recorded. This closes the review like a
    clean round;
  - anything else (say `Round N: two findings, fixed.`): a connection changed. The next round
    is a fix check of those fixes, and of the geometry-only fixes made with them.
- The limit stays: if round 3 has a confirmed finding that changes a connection, the package
  is not merged.

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
.venv/bin/python tools/mergecheck.py PREFIX    # on its own, not piped; until its last line is PASS
git push origin HEAD:main                      # a separate command, after you have read PASS
                                               # rejected? main moved: merge again, gate again
```

**The gate's result decides the push; the command line must not be able to decide otherwise.**
`tools/mergecheck.py` exits non-zero when it fails, but a pipe throws that away: in
`mergecheck.py PREFIX | tail -3 && git push origin HEAD:main` the `&&` tests `tail`, which always
succeeds, so the push goes out with the gate printing FAIL. That happened on 2026-11-20: a commit
with an extraction warning reached main and was there until the next commit fixed it. So:

- Run the gate as a command of its own, unpiped, or with its output sent to a file and then read
  (`.venv/bin/python tools/mergecheck.py PREFIX > gate.txt 2>&1; tail -1 gate.txt; grep -c '^FAIL' gate.txt`).
  It takes a few minutes: give it a long timeout. A gate that outlives the shell's time limit and
  finishes in the background has not passed until you have read its `PASS`.
- Push in a separate command, and only after the last line read `PASS` and no line began `FAIL`.
- The same holds for every step that cannot be taken back: the push to main, `tools/claim.py done`,
  removing the worktree. Never chain one of them with `&&` or `;` after a piped command, or after
  any step whose outcome you have not read (a rejected push followed in the same line by
  `git worktree remove` removed a working tree, also on 2026-11-20).
- A failing gate is never pushed "to be tidied afterwards". If a failing commit does reach main,
  fix it at once with a further commit (no rewrite, no force), pass the gate, push, and say what
  happened in the handoff.

`tools/mergecheck.py` checks that the branch contains main, that only your own files
(`ports.d/PREFIX.txt` among them), the glossary, `operation.md` and (named) fixes to other blocks' traces changed, that
the full extraction has 0 errors and 0 warnings, that every name is in the glossary and
no former name is left, that `ports.d/PREFIX.txt` parses if there is one, that the last
"Round N:" line of the notes' Review section is a clean one ("Round N: no findings.", or
"Round N: no findings that change a connection." with the words "connections identical" in
the section: step 6), and lists the nets newly joined only through `?` items, each of which must
be written up in your notes. Then hand off:

```
tools/claim.py done PREFIX --merged <commit> --handoff FILE [--continue]
```

FILE holds what you propose for the coordinator's files (the headings are those of the
pull request template below). It goes to `handoffs/` on main, and the coordinator applies it
when next on; nothing waits for that. In the same commit your claim is either kept
(`--continue`: you carry on with this package soon, e.g. the next round of a loop) or released
(the package is finished, or you are stopping; the rest is free to take from the notes' Not
done list). A package is often done in several merges this way. Right after a merge and
handoff is the point to compact a long session or start a fresh one: everything is in the
notes, the trace and the handoff, and nothing is half-drawn.

Without write access, or for work that needs discussion first, open a pull request
instead. Run, on your branch, after merging main:

```
.venv/bin/python tools/netlist.py | head -1        # full extraction, no TRACE: 0 errors, 0 warnings
.venv/bin/python tools/signals.py                  # 0 names outside the glossary
.venv/bin/python tools/signals.py --docs           # no former names left
.venv/bin/python tools/unsure.py > /tmp/u_branch.txt   # compare with the same on main
.venv/bin/python tools/ports.py --prefix PREFIX    # your ports parse; look at each meeting it lists
```

Then `gh pr create` against main. The template (`.github/pull_request_template.md`) asks
for: what is traced, the check results, the ports, the review, and what you propose for the
coordinator's files (status line for the master list, Re-read items, ambiguities,
corrections to other blocks' notes). Write those proposals out in full; the coordinator
applies them. One package per pull request.

### 8. The coordinator's follow-up

For each file in `handoffs/` (`tools/claim.py handoffs`; and each pull request, which it
merges first): the coordinator reads the notes and the proposals, spot-checks overlays,
runs `tools/unsure.py`, applies the proposals to the master list, the ambiguity register
and other blocks' notes, trims `floorplan.txt`, rebuilds `out/`, writes the journal, removes
the handoff file and pushes. Claims are not touched: they belong to whoever is working.

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
