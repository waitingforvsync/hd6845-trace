---
name: trace6845
description: Take the next package of the HD6845S die trace from the master list, claim it, trace it by the project's rules, review it independently in rounds until a round finds nothing that changes a connection, merge it into main and hand off to the coordinator. Run by a collaborator with write access, in the repository's main checkout.
argument-hint: "[PREFIX]  (optional: the package to take; default the first free one in the queue)"
disable-model-invocation: true
model: claude-fable-5-2
---

# /trace6845: one package, end to end

This command runs on Claude Fable 5.2 (`model:` above), and its reviewer agents must be started
with `model: "fable"`: the project traces with Fable 5.2 only (user, 2026-11-17), and the merge
gate checks it.

You are a tracer on the HD6845S die trace. This command takes one package from the
master list and carries it through to main. Work through the steps in order. Do not skip
the review or the merge gate. If a step fails in a way these instructions do not cover,
stop, push what you have to your branch, and report to the user. Do not improvise around
the rules.

The rules you work under are in `CLAUDE.md` (already loaded), `notes/workflow.md` and
`notes/tracing-guide.md`. Where this file and those disagree, those win; tell the user.

## 0. Preconditions (stop if any fails)

- You are in the repository's main checkout, not a worktree, and `tools/claim.py list`
  runs. A remote points at `waitingforvsync/hd6845-trace` and you can push to it (write
  access; ask the owner if not).
- `cache/metal.npy`, `cache/acid.npy`, `cache/acid1b.npy` exist (else `tools/prepare.py`
  then `tools/align.py`, which take a while) and `.venv/bin/python` imports shapely,
  opencv, skimage, networkx, scipy.

## 1. Pull, then read

```
git switch main && git pull --ff-only
```

Then read, in full: `notes/workflow.md`, `notes/tracing-guide.md`, `notes/layers.md`, the
latest entry of `notes/journal.md`, `notes/operation.md`, and `notes/work-packages.md`.
Run `tools/claim.py list`.

## 2. Choose the package

**If you already hold a claim** (`tools/claim.py list` shows you as Who), continue that package:
its notes' Not done list is where to start, and steps 3 and 4 resume your claim and worktree.
This is the normal case in a loop. Otherwise, if the user gave a PREFIX, take that; if not, the first row of the **Queue** in
`notes/work-packages.md` that:

- is not claimed (`tools/claim.py list`), and whose region does not overlap a claim whose
  status is not "merged";
- is tracing work: skip `rename` and `verification`, which are the coordinator's;
- for a row of several parts (`tl1`-`tl6` "in six parts"): the lowest-numbered free part.
  Divide the row's region into that many equal strips across its longer side unless the
  row says otherwise; your region is your strip;
- for a `(continue)` row or a `partial` package: the existing prefix, files and notes. Start
  from the notes' "Not done" list. Do not survey again.

Say which package you chose and why, in one line, and go on. Do not ask.

## 3. Claim it, before any tracing

```
tools/claim.py take PREFIX --region "x0-x1 x y0-y1" --what "one line: what you will trace"
```

It pulls main again and refuses a taken prefix or an overlapping region; for a package you
already hold it just says so. If it refuses, go back to step 2. Never edit `claims/` by hand.

## 4. Your own working tree and branch

```
tools/newwork.sh PREFIX
```

It reuses your worktree and branch if you have them (the next round of a loop), with main merged
in. Then work **only** in the directory it prints (`../hd6845-trace-PREFIX`). Run every
command there, and run tools through `tools/t.sh PREFIX tool.py ...`.

## 5. Trace

Follow `notes/tracing-guide.md` exactly: try the known cells first, survey once, then
the loop of trace a piece, overlay, extract, write the notes, ship:

```
tools/ship.sh "Subject" trace/PREFIX.txt notes/blocks/PREFIX.md floorplan.d/PREFIX.txt ports.d/PREFIX.txt
```

- **Before drawing anything, write the survey and a draft of the geometry to disk**:
  `cache/scratch/PREFIX/survey.md` (what is where, with coordinates; each measurement with the
  command that gave it) and, per piece, `cache/scratch/PREFIX/draft-PIECE.txt` (trace-file
  lines, corrected there until the overlay fits, then moved into `trace/PREFIX.txt`). They are
  not committed. If your context is compacted in mid-piece, you resume by reading those two
  files and the notes; without them you survey again.
- Measure with the shared text tools before you render: `tools/px.py` (colour profiles),
  `tools/textmap.py` (a rectangle as text maps), `tools/opendiff.py` (large open diffusions),
  all in section 2 of the guide.
- **Ports**: every wire that leaves the piece goes in the notes' Ports table and, one per
  line, in `ports.d/PREFIX.txt` (guide, section 8). `tools/ports.py --near X,Y` shows what
  other packages have at a place; `tools/ports.py --prefix PREFIX` what yours meet.

- Files you may change: section 10 of the guide and step 3 of the workflow (your trace,
  notes, floor-plan fragment, `ports.d/PREFIX.txt`, your own tools; the glossary). The
  coordinator's files (`notes/work-packages.md`, `notes/ambiguities.md`,
  `notes/journal.md`, `floorplan.txt`, `PLAN.md`, `CLAUDE.md`), `out/`, `claims/` and the
  shared tools are not yours. What you would change there goes into the handoff (step 8).
- Timestamps in notes: `date '+%Y-%m-%d %H:%M %z'`.
- Scope: a package can be bigger than one session. Finish whole pieces. When your
  context is getting full, stop starting new pieces: make the notes' Status and Not done
  exact, and go to step 6 with what is finished. Reviewed, finished pieces are worth
  merging; a half-drawn piece is not (leave it out of the trace and describe it in Not
  done).
- **Small pieces: review them together.** A full review has a large fixed cost (reading the
  guide, calibrating colours): one reviewer used about 250,000 tokens to check a
  three-transistor NOR. When the pieces are small cells of the same build (the same kind of
  gate in one column or row, read by the same method), trace two or three, shipping each to
  the branch as it is finished, and then go to step 6 once with all of them: **at most three
  pieces and about a dozen transistors in one review**. Do not batch a piece of a different
  build, a piece that the next one's reading depends on, or one big enough to fill a review
  by itself; and never leave finished pieces unreviewed at the end of a session to fill a
  batch.
- **When to compact or start a fresh session**: right after a merge and handoff (step 8),
  when everything is in the notes, the trace and the handoff. Not in the middle of a piece.

## 6. Independent review: one full round, then fix checks

The review is required: it is what catches wrong connections, which cost far more later than a
review costs now. It is kept proportionate: the first round reads the whole package (or the
batch of small pieces, step 5), later rounds read only what changed. At most three rounds, and
only findings that change a connection count against them (below).

Every round is **one fresh agent** (Agent tool, general-purpose, `model: "fable"`), started for
that round only. Never reuse or continue an earlier reviewer, and never pass it your reasoning or
an earlier reviewer's conclusions. Note the commit before each round (`git rev-parse HEAD`).
Each round has its own image folder, `cache/scratch/PREFIX/review-N/`: N is the next number
not yet used in `cache/scratch/PREFIX/` (`ls -d cache/scratch/PREFIX/review-*`), counted
through the whole package, not restarted for each run. Put that number in the brief.

**Round 1: full review.** Brief it with this, filled in (keep its first sentence as it is:
`tools/costs.py` knows a reviewer by it):

> You are reviewing one package of a die trace of the HD6845S against the die photos.
> Repository: `<absolute path of your worktree>`. Read `notes/tracing-guide.md` (all of
> it, especially the traps in section 4) and `notes/layers.md` first. The package is
> `PREFIX`, region `<region>`: its geometry is `trace/PREFIX.txt` and its notes
> `notes/blocks/PREFIX.md`. Do not read the notes' "Review" section: it holds earlier
> reviewers' conclusions, and yours must be your own.
>
> What it claims (check each against the photos): `<the list: every join between named
> nets, every gate with its equation, every route with its ends, every cell copy. For a
> batch of pieces: one such list per piece, headed by the piece's name and region>`.
>
> Most likely to be wrong, so look hardest there: `<e.g. the jog at (x,y); the hop under
> the rail at x ...; junction (x,y), read at 2.5x only; contact (x,y), taken from colour.
> For a batch: per piece>`.
>
> Your job is to find errors, not to confirm. For every junction or contact that decides
> a connection, look at 4x or more in at least two shots (`metal`, `acid`, `acid1b`;
> `metal1` for outlines) and, where the eye could be wrong, measure: a colour profile
> (`tools/px.py`), a text map of both metal shots and the clean shot (`tools/textmap.py`),
> the metal test (`tools/follow.py`), large open diffusions (`tools/opendiff.py`),
> `tools/unsure.py`. Check every cell copy by overlay. Look for anything visible inside the
> region that the trace leaves out.
>
> Practical. The shell's directory resets after every command: start every command with
> `cd <absolute path of your worktree> &&`. Run tools as `tools/t.sh PREFIX tool.py ...`.
> Your images go in `cache/scratch/PREFIX/review-<N>/` and nowhere else: run
> `mkdir -p cache/scratch/PREFIX/review-<N>` first, and pass
> `--out cache/scratch/PREFIX/review-<N>/NAME.png` to every tool that makes an image (a bare
> `--out NAME.png` lands in `cache/scratch/PREFIX/` among the tracer's own images; a name
> with a folder in it is taken relative to the repository). Do not edit any file and do not
> run git commands that change anything. Do not start agents of your own. Do not use the
> web, and do not consult any other reverse-engineering of the 6845.
>
> Budget: about 40 images. Spend them on the listed suspicions and on the junctions that
> decide connections, use the text tools (`tools/px.py`, `tools/textmap.py`,
> `tools/railprof.py`, `tools/follow.py`, the extraction) before rendering, keep crops
> small, and do not re-survey what a view already showed. What you could not check, say so.
>
> Report, under 400 words: each finding with its coordinates, what the trace has, what the
> photos show, the evidence (shot, zoom, measurement, image file), and **whether it changes
> a connection** (which nets are joined, which net a transistor's gate or channel end is
> on, whether a transistor or contact exists, an equation, where a wire leaves the package)
> or is geometry only (a width, an edge, a path between the same ends, a comment). Then
> what you checked and found correct, and what you could not check. If you find nothing
> wrong, say "no findings" plainly.

**Rounds 2 and 3: fix checks.** Only if the previous round had a confirmed finding that
changes a connection. Brief a fresh agent with what changed, not with the whole package (keep
the first sentence here too):

> You are checking corrections to a die trace of the HD6845S against the die photos.
> Repository: `<worktree>`. Read sections 2-4 of `notes/tracing-guide.md` and
> `notes/layers.md`. Do not read the "Review" section of `notes/blocks/PREFIX.md`. The
> geometry changed since commit `<commit before the previous round>`:
> `git diff <commit> -- trace/PREFIX.txt` shows every changed line. The changes were made
> to fix these findings: `<each finding in one line, with coordinates>`.
>
> For each change: is it right in the photos (4x or more, two shots, a measurement where the
> eye could be wrong: `tools/px.py`, `tools/textmap.py`)? Did it disturb anything it touches:
> every junction within about 100 px of a changed item, and every net the extraction now
> joins or splits differently? `tools/t.sh PREFIX sameconn.py <commit>` lists every
> connection that differs between that commit and now (names on one net, each transistor's
> three nets, equations), and `.venv/bin/python tools/sameconn.py <commit>` the same with
> every trace file loaded: each difference must be one the findings intended. Do not
> re-review the rest of the package.
>
> Practical. The shell's directory resets after every command: start every command with
> `cd <worktree> &&`. Run tools as `tools/t.sh PREFIX tool.py ...`. Your images go in
> `cache/scratch/PREFIX/review-<N>/` and nowhere else: `mkdir -p` it first and pass
> `--out cache/scratch/PREFIX/review-<N>/NAME.png` (a bare `--out NAME.png` lands in the
> tracer's folder). Do not edit files or run git commands that change anything. Do not
> start agents of your own. No web, and no other reverse-engineering of the 6845.
>
> Budget: about 15 images. Report under 250 words, and for each finding say whether it
> changes a connection or is geometry only; if nothing is wrong, say "no findings".

Then, for each finding of any round:

1. Check it yourself in the photos (reviewers are wrong sometimes too). It is confirmed,
   refuted (say why, with evidence), or undecidable.
2. Fix what is confirmed and ship it. An undecidable one is marked `?` in the trace and
   goes under Ambiguities in the notes.
3. A finding that shows a *method* misleads (a trap) goes into the handoff as a proposed
   Re-read item, with the earlier blocks it may affect.

**Which findings count.** A confirmed finding **changes a connection** if fixing it changes
which nets are joined or apart, which net a transistor's gate or channel end is on, whether a
transistor or a contact exists, a recovered equation, or where a wire leaves the package (a
port's place or side). Anything else is **geometry only**: a width, a length, an edge a few
pixels off, the path of a wire between the same two ends, a comment. Geometry-only findings
are fixed and recorded, but do not use up a round and do not by themselves need a fix check,
**provided you show the connections are the same before and after your fixes**:

```
tools/t.sh PREFIX sameconn.py <commit before the fixes>
.venv/bin/python tools/sameconn.py <commit before the fixes>
```

Both must end `connections identical`; write both commands and their last lines into the
Review section. If either ends `CONNECTIONS DIFFER`, your fix changed a connection whatever
the finding looked like: treat it as one. (`tools/names.py compare` is not this test: it is
for renames, and fails as soon as any transistor's size or position moves.)

Record each round in the notes' **Review** section: round number, full review or fix check,
date, the pieces it covered, what the reviewer was told to suspect, what it checked and at
what zoom, each finding, whether it changes a connection, and its outcome. End the round's
record with one of these lines, exactly (the merge gate reads the last `Round N:` line of the
section):

- `Round N: no findings.` The round reported nothing, or every finding was refuted with
  evidence. **Stop: the review is done.**
- `Round N: no findings that change a connection.` Confirmed findings, all geometry only, all
  fixed, both `connections identical` lines recorded in the section (the gate looks for those
  words too). **Stop: the review is done.**
- Anything else, for instance `Round N: two findings, fixed.` A connection changed. Go to the
  next round: a fix check of those fixes and of any geometry-only fixes made with them.

Ship the notes. If round 3 still has a confirmed finding that changes a connection, the
package is not ready: stop, push the branch, leave the claim, and report to the user. Do not
merge.

## 7. Merge into main, through the gate

In your worktree:

```
git fetch origin && git merge origin/main
```

Conflicts: in `notes/signals.md` and `notes/operation.md` keep **both** sides' rows. A
union is right for rows that both sides added; a row one side changed or deleted must
end up as that side left it. If main renamed a net that your files still use, run
`tools/rename.py OLD NEW`; it changes only what is still old, which is yours. Ship the
merge resolution (`git commit` to conclude the merge is fine here).

```
.venv/bin/python tools/costs.py
tools/ship.sh "Cost report" costs/*.json
.venv/bin/python tools/mergecheck.py PREFIX
```

`tools/costs.py` writes `costs/<your git name>.json` from this machine's Claude Code
transcripts: token counts and API-equivalent dollars by package, model and day, no text. The
gate reads the models recorded for your package: tracing here is done with **Claude Fable 5.2**,
and the gate fails if anything else did the package's work. Fix and re-run until it prints PASS. Then:

```
git push origin HEAD:main
```

**Run the gate and the push as two separate commands, and read the gate's result between them.**
The gate takes a few minutes (give the command a long timeout) and exits non-zero on failure, but a
pipe hides that: `mergecheck.py PREFIX | tail -3 && git push origin HEAD:main` pushes even when the
gate prints FAIL, because `&&` tests `tail`. Run it unpiped, or to a file that you then read:

```
.venv/bin/python tools/mergecheck.py PREFIX > cache/scratch/PREFIX/gate.txt 2>&1
tail -1 cache/scratch/PREFIX/gate.txt; grep '^FAIL' cache/scratch/PREFIX/gate.txt
```

Push only when the last line is `PASS` and no line begins `FAIL`. If the gate was moved to the
background by a time limit, it has not passed until you have read its `PASS`. Never chain a step
that cannot be taken back (this push, `tools/claim.py done`, removing the worktree) with `&&` or `;`
after a piped command or after a step whose outcome you have not read. A failing gate is not pushed
to be fixed afterwards; if a failing commit reaches main all the same, fix it at once with a further
commit, pass the gate, push, and report it in the handoff (step 8).

If the push is rejected, main has moved: go back to the top of this step. **Never** use
`--force` or `--force-with-lease` on any push, and never push to main other than this way
or through `tools/claim.py`: a rejected push is how the repository keeps two merges from
overwriting each other.

## 8. Hand off to the coordinator

Write `cache/scratch/PREFIX/handoff.md` with these headings, in full:

- **Summary**: what is traced (transistors, nets), the main findings, each marked
  traced or believed.
- **Status line for the master list**: one table cell's worth.
- **Re-read items**: methods that misled, and the earlier blocks affected (or "none").
- **Ambiguities**: new AMB entries in full, or changes to existing ones (or "none").
- **Corrections to other blocks' notes**: file, what it says, what is true, evidence.
- **Edits to other blocks' trace files**: commit, what was wrong, evidence.
- **Floor plan**: the coarse blocks of `floorplan.txt` that `floorplan.d/PREFIX.txt`
  replaces.
- **Ports**: what `tools/ports.py --prefix PREFIX` lists as meeting another package's ports
  (names, layers and directions agreeing or not), or "none meet yet".
- **Not done**: as in the notes.

```
tools/claim.py done PREFIX --merged $(git rev-parse HEAD) --handoff cache/scratch/PREFIX/handoff.md [--continue]
```

This writes the handoff to `handoffs/` on main for the coordinator, who applies it whenever they
are next on; nothing waits for that. In the same commit it either **keeps your claim**
(`--continue`) or **releases it**:

- `--continue` when you will carry on with this package soon: the next round of a loop, or a
  session later today. The package's name stays yours, so nobody starts on it from under you.
- No `--continue` when the package is finished, or you are stopping: the claim is released at
  once and anyone can take the rest from the notes' Not done list.

A kept claim with no commits for 24 hours shows as stale on the dashboard: release it
(`tools/claim.py release PREFIX --note "..."`) if you are not coming back to it.

## 9. Finish

If you released the claim, remove the worktree's links and the worktree (`rm cache .venv` inside
it, then `git worktree remove <dir>` from the main checkout); the branch stays on the remote. Do
this as a command of its own, after you have seen that the push and `tools/claim.py done` went
through: not chained behind them.
If you kept it (`--continue`), keep the worktree for the next round. This is the point to
compact the session or start a fresh one before the next piece.
Report to the user in under 300 words: the package, what was traced, the review rounds
and what they changed, what is uncertain, what is left, and the merge commit.
