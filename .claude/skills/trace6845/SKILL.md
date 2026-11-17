---
name: trace6845
description: Take the next package of the HD6845S die trace from the master list, claim it, trace it by the project's rules, review it independently in rounds until a round finds nothing, merge it into main and hand off to the coordinator. Run by a collaborator with write access, in the repository's main checkout.
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

If the user gave a PREFIX, take that. Otherwise take the first row of the **Queue** in
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

It pulls main again and refuses a taken prefix or an overlapping region. If it refuses,
go back to step 2. Never edit `claims/` by hand.

## 4. Your own working tree and branch

```
tools/newwork.sh PREFIX
```

Then work **only** in the directory it prints (`../hd6845-trace-PREFIX`). Run every
command there, and run tools through `tools/t.sh PREFIX tool.py ...`.

## 5. Trace

Follow `notes/tracing-guide.md` exactly: try the known cells first, survey once, then
the loop of trace a piece, overlay, extract, write the notes, ship:

```
tools/ship.sh "Subject" trace/PREFIX.txt notes/blocks/PREFIX.md floorplan.d/PREFIX.txt
```

- Files you may change: section 10 of the guide and step 3 of the workflow. The
  coordinator's files (`notes/work-packages.md`, `notes/ambiguities.md`,
  `notes/journal.md`, `floorplan.txt`, `PLAN.md`, `CLAUDE.md`), `out/`, `claims/` and the
  shared tools are not yours. What you would change there goes into the handoff (step 8).
- Timestamps in notes: `date '+%Y-%m-%d %H:%M %z'`.
- Scope: a package can be bigger than one session. Finish whole pieces. When your
  context is getting full, stop starting new pieces: make the notes' Status and Not done
  exact, and go to step 6 with what is finished. Reviewed, finished pieces are worth
  merging; a half-drawn piece is not (leave it out of the trace and describe it in Not
  done).

## 6. Independent review, in rounds, until a round finds nothing

Each round is **one fresh agent** (Agent tool, general-purpose, `model: "fable"`), started for
that round only. Never reuse or continue an earlier reviewer, and never pass it an earlier round's
conclusions. It reads the photos, not your reasoning. Brief it with this, filled in:

> You are reviewing one package of a die trace of the HD6845S against the die photos.
> Repository: `<absolute path of your worktree>`. Read `notes/tracing-guide.md` (all of
> it, especially the traps in section 4) and `notes/layers.md` first. The package is
> `PREFIX`, region `<region>`: its geometry is `trace/PREFIX.txt` and its notes
> `notes/blocks/PREFIX.md`.
>
> What it claims (check each against the photos): `<the list: every join between named
> nets, every gate with its equation, every route with its ends, every cell copy>`.
>
> Most likely to be wrong, so look hardest there: `<e.g. the jog at (x,y); the hop under
> the rail at x ...; junction (x,y), read at 2.5x only; contact (x,y), taken from colour>`.
>
> Your job is to find errors, not to confirm. For every junction or contact that decides
> a connection, look at 4x or more in at least two shots (`metal`, `acid`, `acid1b`;
> `metal1` for outlines) and, where the eye could be wrong, measure: a colour profile
> (`tools/larr_px.py`), the metal test (`tools/follow.py`), `tools/unsure.py`. Check every
> cell copy by overlay. Look for anything visible inside the region that the trace leaves
> out. Run tools as `tools/t.sh PREFIX tool.py ...`; put images in
> `cache/scratch/PREFIX/review-<round>/`. Do not edit any file and do not run git
> commands that change anything.
>
> Report, under 400 words: each finding with its coordinates, what the trace has, what the
> photos show, the evidence (shot, zoom, measurement, image file), and whether it changes
> a connection. Then what you checked and found correct, and what you could not check.
> If you find nothing wrong, say "no findings" plainly.

Then, for each finding:

1. Check it yourself in the photos (reviewers are wrong sometimes too). It is confirmed,
   refuted (say why, with evidence), or undecidable.
2. Fix what is confirmed and ship it. An undecidable one is marked `?` in the trace and
   goes under Ambiguities in the notes.
3. A finding that shows a *method* misleads (a trap) goes into the handoff as a proposed
   Re-read item, with the earlier blocks it may affect.

Record each round in the notes' **Review** section: round number, date, what the
reviewer was told to suspect, what it checked and at what zoom, each finding and its
outcome. Ship the notes.

**Stop when a round reports no findings, or when every finding of the round was refuted
with evidence.** Write that round as `Round N: no findings.` (the merge gate looks for
those words). If round 5 still has confirmed findings, stop: push the branch, leave the
claim, and report to the user. Do not merge.

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
python3 tools/costs.py
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
- **Not done**: as in the notes.

```
tools/claim.py done PREFIX --merged $(git rev-parse HEAD) --handoff cache/scratch/PREFIX/handoff.md
```

## 9. Finish

Remove the worktree's links and the worktree (`rm cache .venv` inside it, then
`git worktree remove <dir>` from the main checkout); the branch stays on the remote.
Report to the user in under 300 words: the package, what was traced, the review rounds
and what they changed, what is uncertain, what is left, and the merge commit.
