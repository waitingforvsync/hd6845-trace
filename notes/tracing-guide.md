# Tracing guide

For anyone (human or agent) tracing a block of the HD6845S die. Read all of it before
starting. It is the distilled experience of the first sessions; most of the traps in
it cost real time to find.

## 1. The job

We are recovering the exact transistor-level circuit of the chip from die photos, as
polygons in plain-text trace files. A tool extracts a transistor netlist from the
polygons and recognises gates. The end product is a schematic exact enough to emulate
undocumented behaviour, so **a wrong connection is worse than a missing one**.

Rules that override everything else:

- Trace what the photos show. Never fill a gap with what a circuit "should" be. If
  you cannot see how something connects, mark it uncertain (`?`) and write it down.
- Do not consult any other reverse-engineering of the 6845 (Lance Ewing's or anyone
  else's), and do not use the web at all. The datasheet (`cache/ds/p-NN.png`, block
  diagram on p-07, register table p-09) and the CPC document (`cache/accc.txt`, large:
  grep it, do not read it whole) describe behaviour; treat them as evidence, not truth.
- Several people and agents trace at once. Claim your package and work on its own branch
  and working tree (`notes/workflow.md`); touch only your own files (section 10).

## 2. Coordinates, photos, tools

All coordinates are pixels of the chip-2 metal photo, origin top-left, x right, y down
(19838 x 21025). Every photo has been resampled into that frame.

| Layer name | What it is | Use it for |
|---|---|---|
| `metal` | chip 2, metal intact | metal wires and their contacts |
| `metal1` | chip 1, metal intact | second opinion on metal; often shows outlines under wide metal better |
| `acid1b` | chip 1, metal stripped, **clean** | the main source for poly and diffusion, also under where metal was |
| `acid` | chip 2, metal stripped | poly in open areas (orange, unmistakable); has interference fringes under wide metal |
| `acid1` | chip 1, metal stripped, some fringes | rarely needed |

Run every tool through the wrapper, which selects your trace file and your scratch
folder (`cache/scratch/BLOCK/`):

```
tools/t.sh BLOCK quad.py X Y W H --scale S [--grid N] [--layers a,b,c,d] [--notrace] --out NAME.png
tools/t.sh BLOCK view.py X Y W H --scale S --layers acid1b [--grid N] [--trace --nofill] [--stack v] --out NAME.png
tools/t.sh BLOCK netlist.py
```

- `quad.py` shows layers of one region side by side: by default `metal` and `acid1b`
  with your trace outlined on the second. `--layers metal,acid,acid1b,acid1b` gives
  four panels when you need the other shots; `--traceall` outlines the trace on every
  panel (useful to check metal). `view.py` shows one layer, or several
  with `--layers a,b --stack v`. `--layers edges` shows only outlines present in
  both chip-2 shots. Three layers go in one row (keep W x S under 430).
- `mosaic.py X Y W H --offsets "0,0 dx,dy ..." --scale S --layer acid1b --out NAME.png`
  shows the same rectangle at several offsets side by side, to compare repeats.
- `tools/railprof.py X0 X1 Y0 Y1 [--horizontal]` prints what lies under a rail as text
  (diffusion, gate, field runs along it, from the clean shot's protected colours): the
  stack structure of a whole gate column in one call. It does not find contacts. Check
  each gate on a view before drawing it.
- `tools/t.sh BLOCK follow.py X Y N|S|E|W [--trace]` follows ONE metal line from a point on
  it (2 px steps, both chips' metal shots, corners and diagonals) and prints corners,
  wide stretches, contact candidates and the end, or the piece as a trace-file `M` line.
  It follows diagonals but does **not report them as corners**: a 44 px diagonal step or a
  400 px diagonal run leaves no line in its output, and its `M` line then draws a straight
  line where there is none. On a long run, sample it: `--max N` in stages (`--max 800`,
  `900`, ...) prints where the line is after N px, which places each step to about 10 px.
  Keep `--gap` at its default: `--gap 50` joined a pad to a rail 40 px away.
- `tools/tla_tracks.py` along a thin metal that horizontal polys cross is **not evidence**
  for the metal: it reports the bright poly crossings as runs and, with a bridging gap,
  joins them into a line that may not exist (or is right by luck). Use the metal shots.
  Use it for every long run; then look at its end, at each staircase it went through and
  at each "wide" stretch (traps 13-15). `tla_tracks.py` profiles a straight track for
  breaks; `tla_contacts.py` lists contact candidates on one; `strips.py --layer class`
  shows 3,000 px of a bus in one image.
- For following bundles of parallel wires, `tools/sel_tracks.py` and `tools/sel_cut.py`
  (written by the agent that traced the select logic; read their docstrings) report
  where metal is present along a track or a cut. **Do not trust them for
  connectivity.** `sel_tracks.py` bridges gaps of about 20 px, so where a bundle steps
  sideways it joins two different nets that share a track: that produced a wrong
  register identification. It also reports breaks at contacts, blemishes and poly
  crossings. `tools/rdp3_jogs.py` finds the jogs. Confirm every track by overlay.
- **Measuring tools that print text** (no image, so they cost almost nothing; shared since
  2026-11-17, when six packages had each written their own). Read each docstring once:
  - `tools/t.sh BLOCK px.py row Y X0 X1 STEP [layers]` (also `col X Y0 Y1 STEP`, and
    `pt X,Y ...`): the colour profile, R G B per sample in any of `metal`, `metal1`, `acid`,
    `acid1`, `acid1b` (or `all`); `--comp NAME` reads a composite. The measurement for a
    junction, a strip, a thin metal, a patch whose class is in doubt (traps 8, 19, 21).
  - `tools/t.sh BLOCK textmap.py X0 Y0 X1 Y1 [STEP] [--acid]`: a rectangle as text maps, one
    character per sample: both metal shots' brightness and the clean shot's red minus green,
    with `--acid` the chip-2 stripped shot's as well. Its docstring says what a contact, a
    break and an edge underneath look like in them (trap 22).
  - `tools/t.sh BLOCK opendiff.py X0 Y0 X1 Y1`: lists the large open diffusions (green in the
    clean shot, red over green in the chip-2 stripped shot) and how much of each your trace
    draws as diffusion (trap 21).
  - `tools/t.sh BLOCK sameconn.py COMMIT`: whether the extraction's connections are the same
    as at an earlier commit, sizes and positions aside (the proof for a geometry-only fix,
    `notes/workflow.md` step 6).
  - `tools/ports.py`: the ports of all packages and which of them meet (section 8).
  The per-block tools these came from stay, because notes cite them: `tc1_px.py`,
  `larr_px.py` (profiles), `tc1_hex.py` (text maps), `tc1_green.py` (open diffusion). Still
  per-block, useful anywhere: `tc1_edge.py` (the runs along a cut where a colour test
  holds: a band's edges), `dbus_localmatch.py` (where a rectangle repeats near a guessed
  offset). Before writing a `tools/BLOCK_*.py` of your own, look for one of these.
- X Y is the top-left corner, W H the size, in die pixels. The tool prints the path of
  the PNG; open it with the Read tool. `--out`: a bare file name (`--out j1.png`) lands in
  your scratch folder `cache/scratch/BLOCK/`; a name with a folder in it is taken as given,
  relative to the working tree (`--out cache/scratch/BLOCK/review-3/j1.png`).
- **Keep every image under about 1400 px a side or it is downscaled when read and the
  zoom is wasted.** quad.py puts two panels side by side: keep W x S under 640.
  view.py with one layer: W x S under 1300.
- Useful scales: 0.5-1 to survey and follow wires, 2.5-3 to trace, 4-6 to settle one
  junction. Beyond 2 there is no new detail, only bigger pixels, but junctions are
  easier to judge.
- To look at someone else's finished trace as a worked example, set TRACE yourself:
  `TRACE=examples/pilot tools/t.sh BLOCK quad.py 14268 14880 380 380 --scale 1.7 --out cal.png`

Before tracing anything, render and study these three calibration views (each shows a
verified trace over the clean shot). Compare the four panels until you can name every
feature:

```
TRACE=examples/pilot tools/t.sh BLOCK quad.py 14268 14880 380 380 --scale 1.7 --out cal1.png   # two gates, open area
TRACE=inrow tools/t.sh BLOCK quad.py 14640 18190 640 400 --scale 1.0 --out cal2.png           # gate chain, loads under a VCC band
TRACE=decode tools/t.sh BLOCK quad.py 14200 13500 470 480 --scale 1.35 --out cal3.png         # NOR array
```

The matching trace files (`trace/examples/pilot.txt`, `trace/inrow.txt`) show how the
geometry is written.

## 3. How the chip is built

Silicon-gate NMOS, one metal layer, depletion loads, buried contacts.

- **Transistor**: poly crossing diffusion. Gate length 20-28 px. Nothing else makes a
  transistor.
- **Static gate**: a VCC contact, a diffusion strip down from it, a *load*, the output
  node, then pull-down transistors to a VSS contact. The load is a poly block over the
  strip whose gate is tied to the *output* side by a buried contact (a small box,
  about 30 x 28 px, with a heavy outline at a corner or end of the load poly). That
  tie is how a load is recognised. Weak loads are long (poly block 70 wide x 100 tall
  over a 27 px strip); strong ones short and wide.
- **NOR** = pull-downs side by side between output and VSS. **NAND / AND-OR-invert** =
  pull-downs in series.
- **Buried contact**: poly joined directly to diffusion, no metal. Outputs often leave
  a gate this way and become the gate poly of the next stage.
- **Metal contact**: metal to diffusion or metal to poly, about 30 px square.
- **Pass transistor**: poly crossing a diffusion that is not on a supply; used for
  latches and multiplexers, usually clocked. Expect dynamic latches (pass transistor
  into an inverter gate) in the datapaths.
- One metal layer, so wires cross by ducking under: contact, a short run in poly or
  diffusion, contact.
- **Supplies**: loads go to VCC, pull-downs to VSS. If you cannot follow a rail to a
  known supply, the orientation of the loads tells you which rail is which. Label
  supply metal `vss` / `vcc`; all pieces with those names are joined automatically.
- Big drivers use multi-finger transistors: columns of contacts alternating with long
  gate strips. Draw each group as one diffusion rectangle and one contact rectangle
  per column; that is accurate enough.

## 4. Reading the photos

What a feature looks like depends on the shot and, in the clean shot, on whether metal
was above it. Full notes with coordinates of examples: `notes/layers.md`.

| Feature | `metal` / `metal1` | `acid` | `acid1b` where metal was above | `acid1b` in the open |
|---|---|---|---|---|
| Metal | bright yellow, grainy | gone | - | - |
| Poly | orange-brown, visible only where no metal covers it | orange, granular | salmon, sharp red outline | dark red-brown, textured |
| Diffusion | plain, dark outline | plain tan, dark outline | flat tan, dark outline | green near the die edge, **pink near the centre** |
| Field | plain | greenish | pink | khaki / olive |
| Metal contact | ring in the metal | pitted box | dark specks on diffusion; on poly a paler patch; measures greenish against its surroundings (a test that caught two false contacts) | - |
| Buried contact | small heavy-outlined box | same | same | same |

Traps, all of them real:

1. **The clean shot's colours drift across the die.** Open diffusion is green in the
   bottom rows, pink in the decode array and mauve in the mid-right array; at the top
   of the central datapath diffusion is light tan with or without metal above it and
   the olive pockets are open field. Calibrate locally: find an unmistakable
   structure near where you work (a VCC contact with its load, a row of contacts) and
   see what colour each layer has there.
2. **Metal protected a margin of about 10 px beyond its edges.** A 25 px gap between two
   metal lines shows in `acid1b` only as a thin dark bar across whatever is underneath,
   or as a narrow olive strip with a dark outline. Those bars and strips are not layout.
   Where such a gap crosses poly it can leave a dark ring that looks like a contact;
   a real contact also shows as a ring in the metal shot.
3. A dark line across a metal wire in the metal shots is the edge of something
   *underneath*, not a break in the metal. Likewise, bright green bands in `acid1b`
   inside the arrays are gaps of open field between metal lines, not features.
4. Tan (diffusion under metal) and khaki (field in the open) are close. Check where the
   metal is before calling a tan area diffusion. A narrow diffusion wire in the open
   may show no colour of its own at all, only a strip about 22 px wide between two
   dark edges. The stripped shots also show an etch-boundary line beside every wide
   rail, which is not a feature.
5. Under wide metal, `acid` shows only fringes. Use `acid1b`, and `metal1` for outlines.
6. Automatic alignment of `acid1b` is within about 1 px in random logic but only
   interpolated inside regular arrays; check it against `metal` at a contact before
   measuring anything.
   Under metal, poly over a channel is distinctly brighter (redder) in `acid1b` than
   poly over field: that is how the decode array was read, and it works elsewhere.
7. **Your eye is unreliable for repeated patterns.** In the decode array, impressions at
   2.7x of which crossings had transistors were wrong where a colour measurement was
   right. For arrays, measure (see `tools/pla_read.py`) and cross-check.
8. Poly often runs directly underneath the metal of a *different* net for hundreds of
   pixels. Metal over poly is a connection only where there is a contact.
   Where a poly line ends next to another feature, zoom to 4-6x before deciding whether
   they touch; and when the decision matters, **measure it**: a colour profile across
   the junction (`tools/px.py`; it was `tools/larr_px.py` then) settled junctions that one
   agent had judged wrongly by eye three times. Most wrong readings so far were junctions judged at too low a zoom.
9. If a region will not give a consistent circuit after two honest passes, stop, record
   exactly what is established (with coordinates) and what is not, and move on.
10. **A wiring channel cannot be read from the metal shot.** Between the metal tracks of a
   channel, and directly under them, poly lines of *other* nets run for hundreds of
   pixels: a track ends on a contact, its net carries on in poly beneath the neighbouring
   track and comes back up to metal three tracks away. The metal shots show none of this
   (trap 8 at full scale). Read every channel in `acid1b`, end to end
   (`strips.py --layer acid1b`, and `classmap.py` where the colours are close), and
   account for every track end: a track that stops has gone somewhere. First seen in
   `mrach` (x 13040-13425), where half the nets change track under the metal.
   **The same holds for every poly hop under a wide metal and every bundle at a block's
   edge: a hop that looks straight at 2x may step one track.** Found 2026-11-17: `r9m`'s two
   hops under the `res_b`/`lpstb_b` metals (x 5078-5127) were drawn straight from a 1.8x view
   and each steps down one track, which had put R9's match on the wrong input of the step
   logic; `bust`'s rows all step one track at `cdp1`'s west edge (x 8215-8345). Read each
   hop at 4x or more in both stripped shots, and check that the number of rows entering
   equals the number leaving at the same order.
11. **"Drawn once, at full length" is a claim about every crossing.** A rail or clock line
   that looks continuous through an array at 1x may be cut at each routing channel and
   re-fed from somewhere else. In the mid-right array the `ck_a` rail, the master clock
   line and line L3 are each three pieces on three nets. Look at such a line at 3x at
   every channel and row-group boundary before drawing it through.
12. **A line that ends in a widened foot ends *on* something.** Look at 6x for the contact
   or the turn before leaving it as a free end.

13. **A metal that lies on a poly line is not joined to it, however long the overlap.**
   The RES line runs exactly on top of another net's poly for 217 px and stops there; its
   real end is a 90 px arm to a contact one bus line over. Before calling two coincident
   lines one net, find the contact: a pad, a ring in the metal shot, the green patch in
   the clean shot. If none of the three is there, they are two nets.
14. **Where a tool says a line ends, look at the end at 5x in the metal shot.** A line ends
   on a contact; if you see none, the line has turned and the tool missed the corner.
15. **Crossing fields without pads carry no taps.** In the fields where poly rows cross a
   metal bus, the clean shot's colour under the metal drifts between salmon and
   yellow-green by the row, so colour alone finds "contacts" at every crossing. A real tap
   there has a widened pad.
16. **A metal that runs up to a pad's ring is not thereby on the pad.** A second line can
   pass a pad at minimum spacing, turn a corner there, and lie on the poly that leaves
   the pad, so that at 3x it looks like the pad's own line going on. Tests: (a) start
   `tools/follow.py` on the pad's *own* metal: it stops at the pad if the other metal is
   separate; (b) profile along the line through the pad centre
   (`tools/tla_tracks.py --half 1 --gap 3`) and compare the dark stretch on that side with
   the ring on the side where the pad's own line arrives (found: 24 px against 10);
   (c) a "T" whose stub ends flush with the edge of the crossing line is a corner.
   Found 2026-11-16 at (7577,5262), after two commits said two nets were one.
   `tools/padjoin.py` lists the contacts where the trace has this shape.
   The follower's default `--gap 24` is itself enough to jump from a pad to a line that
   passes 24 px away (found 2026-11-16 at (7467,4782)): where its output turns a corner
   within 30 px of a pad or contact candidate, check the corner with a brightness profile.

17. **A join the extraction reports is only as good as the geometry on its path.** When
   two named nets become one after new geometry is drawn, the message "carries several
   names" says that the drawing connects them, not that the chip does. If any item on the
   path between the two labels carries a `?`, or was placed "by analogy" or "from one
   view", the join is an assumption and must be written up as one, and the names must not
   be merged with `tools/rename.py` until the uncertain stretch has been read in a second
   shot. Found 2026-11-16: `tc1_i` and `ras_o0_alt1` had been merged across 250 px of
   `?P`, reported as a result, and were two nets.
   `tools/unsure.py` lists every net whose labelled pieces are joined only through `?`
   items; run it before writing up a join.

18. **The text tools are right under metal and wrong in the open.** `tools/classmap.py` and
   `tools/railprof.py` call open poly "dark" and open field "diffusion", and do not tell a
   channel from poly over field there. In an open gap, decide in the chip-2 shots, where
   poly is orange. Found 2026-11-17 in `amr` (re-read item R16).
19. **The metal test misses thin metal.** The follower's test (R > 177, G > 128) does not
   see thin, dim lines (under about 16 px): it reports breaks or no line at all. For those,
   profile along and across the line and compare with a known stretch of the same line.
   Found 2026-11-17 in `rde` (R17).
20. **A contact at low zoom does not say which way a signal goes.** Whether a line drives or
   receives depends on whether its contact lands on a gate poly or on a source or drain.
   Two packages called `amr`'s four outer lines outputs; they are gate inputs. Found
   2026-11-17 (R18).

21. **Bright green in the open is a large diffusion, not field.** In the clean shot a large
   open diffusion (the drain of a big driver) is bright green (118/155/90) and open field is
   khaki-brown (151/138/100); a narrow diffusion wire in the open is not green at all (trap 4).
   `tools/classmap.py` without `--open` paints the green as pale green, its colour for field in
   the open, so a class map shows a drain as empty ground. Decide in the chip-2 stripped shot
   (`acid`): red minus green is 0-4 on field and 13-17 on diffusion (`tools/px.py pt X,Y
   acid1b,acid,metal`; `tools/textmap.py --acid`). `tools/opendiff.py X0 Y0 X1 Y1` lists the
   green areas your trace does not draw as diffusion. This is about areas wider than about
   25 px in the open; the narrow bright green bands between metal lines inside the arrays are
   still field (trap 3). Found 2026-11-17 in `tc1` (run 6, after three runs of reading the
   areas beside the drivers as field; calibration table at the top of `notes/blocks/tc1.md`;
   re-read item R19).
22. **A thin metal goes dark where it passes over a buried contact, and that is not a
   contact.** A metal about 12 px wide is dark for 35-80 px in *both* metal shots where a
   buried-contact box, or a poly's edge running lengthwise, lies under it: it looks like the
   tall ring of a metal contact, and the follower stops there. Seen at every gate of `tc1`'s
   gate columns (its Ambiguities 12, 13, 18); if these were contacts they would short the
   outputs of neighbouring gates together. A real contact of a thin metal has all of: a
   single bright centre about 12 px across inside a dark ring about 40 px across, in both
   metal shots; a green hole inside the pad in the clean shot; the metal widened into a pad.
   The pass-over has none: the clean shot under it is protected tan with no green hole and no
   pits, the metal keeps its width, and the darkness is a lengthwise bar with half-bright
   flanks. Measure with `tools/textmap.py` against a known contact of the same metal nearby
   (its docstring gives two). Do not draw a contact from the darkness alone, and do not take
   the follower's stop there as the line's end (trap 14). Found 2026-11-17 in `tc1`, where run
   2 had taken one for a ring gate's contact (re-read item R20).

**When a trap turns out to affect work already done**, add the affected blocks to the
"Re-read list" in `notes/work-packages.md` in the same commit that records the finding.
A remark in a journal entry or a report is not enough: nobody re-reads those when
choosing the next task.

## 5. The trace file

One file per block: `trace/BLOCK.txt`. The format is documented at the top of
`tools/tracelib.py`; read that docstring. In short, one shape per line:

```
@block myblock
M 14434,14880 y15300 w=52              # metal path: points, then width. xN / yN move one axis
D 14406,14898:14460,15002              # rectangle on the diffusion layer
P [ 100,100 x150 y130 x100 ]           # polygon
C 14423,14920 14422,15050 s=30x34      # contacts, one per point
B 14520,14927:14550,14955              # buried contact
N P 14328,14890 in_a                   # name the net that owns the poly at this point
?P 100,100:120,160                     # uncertain shape (drawn in yellow)
A 100,100:150,150 kind=clamp           # mark a transistor here: clamp, field (both off in
                                       # normal operation) or hold (weak always-on feedback)
@requires inrow                        # load another file (for cells defined there)
```

- Layers: M metal, P poly, D diffusion, C metal contact, B buried contact.
- Poly over diffusion is a channel unless a `B` covers the overlap. Draw diffusion
  *through* under the gate; the extractor splits it.
- A contact joins the metal over it to the poly under it, or else to the diffusion.
- Comment generously: what each group of shapes is. Someone will have to check it.
- **Names.** Label every net you can say something about (`N` lines). Use the name from
  `notes/signals.md` if the net is already there; a functional name if you know what the
  signal is (`h_eq_r0`, `wr_r6`, `rc3_q`); otherwise your block prefix and a local name
  (`bc1_ld_in1`), and add a row to the glossary saying what is known about it. When a
  placeholder is identified, `tools/rename.py OLD NEW` renames it in every trace file and
  note. A wire you believe is net X but have not joined to it is labelled `X_u`.
  `tools/t.sh BLOCK signals.py` lists your names that the glossary does not cover.
- Edge positions are uncertain by about 3 px. Draw shapes that must connect with a
  clear overlap, and shapes that must not with a clear gap (5 px or more). Slivers
  where edges nearly coincide produce warnings.
- Repetition: `@cell NAME tag=T ... @end` defines a cell at its master position;
  `@inst NAME dx,dy [mx=X] [my=Y] [rot=DEG o=x,y] tag=T` places a copy. A label
  containing `{}` gets the tag. **Prefix cell names with your block name.**
- Draw lines that run across many instances (rails, buses, clock lines) once, at full
  length, *outside* the cell; keep in the cell only what belongs to one instance.

## 6. The loop

0. **Try the known cells first.** Before tracing any regular-looking region by hand, run
   `findcell.py` with the master rectangle of every cell already traced, in all
   orientations. On 2026-11-16 three regions (552 transistors) turned out to be copies of
   the counter bit, the counter clock generator and the register/comparator cells. Then
   check each copy's ports on an overlay: a copy can differ from the master by one contact
   on a neighbouring track.
1. **Survey** your region at 0.5-1x in `metal` and `acid1b`. Find the rails, the rows of
   loads, the repeated units, where wires enter and leave. Write a short inventory in
   your notes file before tracing. In the arrays, first run `findcell.py` with the
   master rectangles of cells other blocks have already traced (restricted to your
   region with `--region`, orientations `0,m0,180,m180`): the latch `rdp3_lat`
   (14597 13010 14987 13280, in `trace/rdp3.txt`) and the static register bit
   `cdp1_reg` (8745 3040 9225 3330, in `trace/cdp1.txt`) recur, some upside down, in
   several rows of both datapaths. A row that matches can reuse the cell by
   `@requires`, after checking how its edges differ.
   **Write the survey to disk before drawing anything**: `cache/scratch/BLOCK/survey.md`
   (what is where, with coordinates, each measurement and the command that gave it), and for
   each piece a draft of its geometry, `cache/scratch/BLOCK/draft-PIECE.txt` (trace-file
   lines, not yet in `trace/`), which you correct there until the overlay fits and then move
   into the trace file. Images drop out of your context and a long session is compacted;
   with the survey and the draft on disk, resuming is reading two files. (The inventory in
   the notes is the part of the survey worth keeping; the scratch files are not committed.)
2. **Trace a piece** (one gate group or one cell): view at 2.5-3x with `quad.py`, write
   the shapes.
3. **Overlay**: `quad.py` again (its last panel outlines your trace on the clean shot)
   and `view.py --layers metal --trace --nofill` for the metal. Every outline should
   sit on a real feature. Inside the piece, anything visible that you have *not*
   traced should be something you can name.
4. **Extract**: `tools/t.sh BLOCK netlist.py`. Fix every error. Read the recovered
   gates: does each transistor belong to a sensible structure? A load with no
   pull-down, a gate output that goes nowhere, a transistor with both ends on the same
   net, are usually tracing mistakes. The list "unnamed open nets" must end up empty:
   each net is either driven and used inside your trace, or named as a port.
5. **Write it down** in your notes file while you still have it in view, and **ship it**
   (section 10). Then the next piece.

Finish pieces completely before starting new ones. A block half-covered by verified
pieces is useful; a block fully covered by unchecked geometry is not.

## 7. Repetition and arrays

Most of the die is repeated cells. Trace a cell once.

- `tools/t.sh BLOCK findcell.py x0 y0 x1 y1 --min 0.5 [--region x0,y0:x1,y1] [--orient 0,m0] [--layer metal|acid1b] --cell NAME`
  finds other copies of a rectangle in any of eight orientations and prints `@inst`
  lines. It can lock onto the wrong period of a periodic structure: check every
  placement by overlay.
- `tools/t.sh BLOCK composite.py NAME x0,y0:x1,y1 --offsets "0,0 dx,dy ..."` builds the
  per-pixel median over the copies, which removes dirt, residue and metal grain. View
  it with `--comp NAME` on view.py / quad.py (coordinates stay those of the master).
  Start NAME with your block name (composites share one folder). Above 4x the median
  is blurrier than a single clean shot; use it for dirt, not for fine junctions. In a
  composite the `acid` layer shows poly even under metal, because the fringes average
  out.
- `tools/rdp3_cmp.py` compares instances as text and costs no images.
- `tools/rdp3_sharp.py` (unsharp mask; three agents found it on a median composite at
  3-5x their most useful view), `tools/cdp2_pt.py` (a colour-and-speckle test for
  whether a contact is present, which reversed one by-eye reading) and `tools/cdp1_sr.py` (read the docstrings). The latter makes a
  sub-pixel-aligned median of the copies of a cell at 3-6x. The agent that wrote it says it is what made a register
  cell readable where the plain composite was too blurred.
- `--shift dx,dy` on view.py / quad.py shows another instance in the master's
  coordinates: use it to compare instances.
- `tools/t.sh BLOCK cellcheck.py CELL [--bbox x0,y0:x1,y1] [--layer acid1b]` compares each
  instance's photo with the master's and tints differences. With `--bbox` it compares
  any rectangle, traced or not, at the instance positions: a cheap way to see whether
  untraced neighbours of a cell also repeat. **Instances are not always identical**: the wiring around a
  repeated core often differs (one bit has an extra gate, the end slice differs). Look
  at every instance at least at low zoom before declaring it a copy.
- Datapath slices repeat every 390.3 px horizontally; two other arrays repeat every
  477 px vertically. Use the offsets findcell reports, not multiples of the pitch.
- Tag instances by position (`s0`, `s1`, ... left to right, or top to bottom) unless you
  have established which is bit 0 (for a counter, the carry direction shows it; say
  how you know).
- Agents working on different parts of one array numbered their slices differently.
  So that blocks can be joined, state at the top of your notes how your tags map to
  the array's **columns**, which are defined by the wide VSS rail in each slice:
  central datapath column cN has its VSS rail at x = 7605 + 390.3 N (N = 0..7); right
  datapath column cN has its VSS rail at x = 14175 + 390 N. A row with fewer than
  eight cells occupies only some columns: say which.
- A programmed array (ROM/PLA) is read by measurement: see `tools/pla_read.py` and
  `notes/blocks/decode.md` for the method and its cross-checks.

## 8. Names and ports

- Lower case, digits, underscore. Prefix your local nets and cells with your block
  name (`areg_q0`, `cdp5600_carry_{}`).
- Use a global name only when you have *traced* the connection to something already
  named, or the identity is certain from structure; say which in your notes.
  Global names so far:

| Name | What |
|---|---|
| `vss`, `vcc` | supplies |
| `clk` | the CLK pin node (after its protection resistor) |
| `clk_b` | CLK buffered, same sense as the pin |
| `ck_out` | main internal clock, NOT CLK, heavily buffered |
| `ck_a` | clock phase, high only while CLK is low |
| `ck_b` | clock phase, high only while CLK is high |
| `e_b`, `e_n` | E buffered, and its inverse |
| `rw_a`..`rw_d`, `rs_a`..`rs_d`, `cs_a`..`cs_d` | R/W, RS, CS through 1, 2, 3, 4 inverters (`_a` and `_c` inverted) |
| `res_b`, `lpstb_b` | RES and LPSTB pins, buffered, same sense as the pin |
| `ar0`..`ar4`, `ar0_n`..`ar4_n` | address lines into the decode array (rows) |
| `rsel0`..`rsel17` | register select lines out of the decode array (columns), high when selected |
| `<pin>_drv_in` | the core signal entering an output driver; the pad is its inverse (`ma0`..`ma13`, `ra0`..`ra4`, `hsync`, `vsync`, `disptmg`, `cudisp`) |

- You will meet clock and control lines whose identity you cannot know locally. Give
  them a local name (`BLOCK_phi1`), note where they enter your block, and move on.
- **Ports.** Every wire that crosses your block's boundary goes in a ports table in your
  notes: local name, layer, the coordinate where it crosses, direction if known
  (driven inside / driven from outside), and what you think it is. Draw each such wire
  right up to the boundary and label it. Blocks are joined later through these tables,
  so they matter as much as the gates.
- **The same ports, one per line, go in `ports.d/BLOCK.txt`**, which tools can read
  (expected for new work since 2026-11-17; a block traced before then gets its file when it
  is next opened):

  ```
  # NAME        LAYER  X,Y              DIR  note
  tc1_f         P      8250,3348-3362   out  R3 output; runs on under ns1..ns6 without contact
  ras_straight  M      7220-7240,4450   out  NOT b (W2 lower)
  vss           M      7943-7990,4450   -    the VSS bus turns south
  ```

  NAME is the net's name in the trace; LAYER is `M`, `P` or `D`; X,Y is where the wire
  crosses your boundary or where the drawn wire ends, and either number may be a range
  `A-B` (the wire's extent across the edge); DIR is `in` (driven from outside), `out` (driven
  inside your block), `?` (not known) or `-` (a supply); the rest of the line is a free
  note. `#` starts a comment. One line per place a wire leaves. Only ports with a definite
  place: a wire "seen going on west" stays in the notes until it has a coordinate. Keep the
  file and the notes' table in step: when one changes, change the other in the same commit.
- `tools/ports.py` reads every package's file and reports the ports of different packages
  that lie within 40 px of each other (same name or not, layers, directions), the names two
  packages both use at places that do not meet, and the ports with no partner;
  `tools/ports.py --near X,Y` lists what other packages have near a wire you are following,
  `--prefix BLOCK` only what involves yours. Run it before you name a wire that arrives from
  a neighbour, and before the review: a meeting whose names differ is a join to check in the
  photos (trap 17), not a rename to make from the list.

## 9. What to deliver

1. `trace/BLOCK.txt`: extracts with no errors, no unnamed open nets, uncertain shapes
   marked `?`.
2. `notes/blocks/BLOCK.md`, kept current as you go, with these sections:
   - **Status**: what is traced, what is not, in two or three lines.
   - **Inventory**: the cells / gate groups in the region with coordinates.
   - **Logic**: for each cell or group, the recovered logic in plain equations, the
     latches and what clocks them, and what you believe the function is (keep
     "traced" and "believed" visibly apart).
   - **Ports**: the table from section 8.
   - **Ambiguities**: each with coordinates, the candidate readings, your working
     assumption, and what would settle it.
   - **Review**: the independent review (`notes/workflow.md`, step 6): date, reviewer,
     what it checked and at what zoom, what it found, what changed, what it could not check.
   - **Not done**: anything in your region you did not get to, with coordinates, so the
     next agent can pick it up without re-surveying.
3. `ports.d/BLOCK.txt`: the ports, one per line (section 8).
4. `floorplan.d/BLOCK.txt`: one line per functional piece you have identified, format
   `x0,y0:x1,y1  kind  name | description` with kind one of
   `pad io array pla logic route test power unknown`, prefixed `?` if the function is a
   guess. Example: `7600,5480:10850,5910  array  R1 register (8 bit) | written from the data bus when rsel1; feeds the comparator below`.
   These are drawn over the die photo, so make the names say what the piece *does*.

## 10. Committing, and what not to touch

- Commit and push after every finished piece with
  `tools/ship.sh "Subject line" trace/BLOCK.txt notes/blocks/BLOCK.md floorplan.d/BLOCK.txt ports.d/BLOCK.txt`
  It commits exactly the files you name and refuses a trace file that does not parse.
  Subject in the imperative, under 70 characters, saying what was traced
  ("Address register: latch cell traced and placed five times"); add a body with a
  second `-m`-style paragraph by putting a blank line and text inside the same quoted
  message if there is something a reader of the history should know.
- Work on your package's branch, in a working tree of your own (`tools/newwork.sh
  BLOCK`; `notes/workflow.md`). `ship.sh` pushes that branch; it refuses to commit on
  main. Your work reaches main only through the gate (`tools/mergecheck.py`, workflow
  step 7) after the review rounds, or by pull request. Merging main into your branch is
  fine; do not
  rewrite history that is already pushed (no rebase or reset of pushed commits).
- Yours: `trace/BLOCK*.txt`, `notes/blocks/BLOCK.md`, `floorplan.d/BLOCK.txt`,
  `ports.d/BLOCK.txt`, new tools named `tools/BLOCK_*.py`, your scratch folder; rows for your names in
  `notes/signals.md`, and `notes/operation.md` where your block changes what it says.
- Not yours: `notes/work-packages.md`, `floorplan.txt`, `notes/journal.md`,
  `notes/ambiguities.md`, `PLAN.md`, `CLAUDE.md`, `claims/`, `out/`, the shared tools,
  and other blocks' notes. Do not run `tools/build.py`, `align.py` or `prepare.py`
  except to build your own `cache/`. What you would change in those files goes into your
  pull request (the template has a place for each). If a shared tool is wrong or missing
  something, say so there (and copy it to `tools/BLOCK_x.py` if you need a variant now).
- If you find that an existing trace of a neighbouring block is wrong: record it under
  your notes' Ambiguities with the evidence. Fix it only if it blocks your work and the
  evidence is clear, as a commit of its own whose message says what was wrong and how you
  know, and list it in the pull request.
- Do not start sub-agents, with one exception: the independent reviewer of your
  finished package (`notes/workflow.md`, step 6).

## 11. What is known about the chip

Register and counter widths help recognise datapath rows (from the datasheet; not yet
confirmed in silicon):

| | Width | Function |
|---|---|---|
| R0 | 8 | horizontal total |
| R1 | 8 | horizontal displayed |
| R2 | 8 | horizontal sync position |
| R3 | 4 + 4 | sync widths (horizontal low nibble, vertical high nibble) |
| R4 | 7 | vertical total |
| R5 | 5 | vertical total adjust |
| R6 | 7 | vertical displayed |
| R7 | 7 | vertical sync position |
| R8 | 2 + 2 + 2 | interlace mode (bits 0-1), DISPTMG skew (4-5), cursor skew (6-7) |
| R9 | 5 | maximum raster address |
| R10 | 5 + 2 | cursor start raster, blink mode (bits 5-6) |
| R11 | 5 | cursor end raster |
| R12, R13 | 6, 8 | display start address |
| R14, R15 | 6, 8 | cursor address (readable) |
| R16, R17 | 6, 8 | light pen address (read only) |

Counters expected: horizontal character counter (8 bit), raster counter (5), row
counter (7), vertical adjust counter (5), sync width counters (4 + 4), memory address
counter (14) with a row-start latch (14). Each programmable limit has a comparator.

Already traced (see `notes/blocks/*.md`): the pad ring's output drivers and input
buffers, the clock block (`notes/blocks/clock.md`), the register decode array
(`notes/blocks/decode.md`, with the left-to-right order of the select columns). The
coarse floor plan is `floorplan.txt` (picture: `out/floorplan.jpg`); most of it is
still guesses from shape.

Pads, for orientation: MA0-13 down the left side and along the bottom left, RA0-4 top
right, HSYNC/VSYNC top, DISPTMG/CUDISP bottom, D0-D7 down the right side (D0 at the
top), CLK, R/W, E, RS, CS bottom right, RES and LPSTB top. Table: `notes/pads.md`.

## 12. Pace and context

- **Images are your budget.** You have room for roughly 60 to 80 of them before your
  context is full, and an image costs in proportion to its area: a 1300 x 650 view
  costs half of a 1300 x 1300 one. The first agent on a block spent most of its
  budget surveying and traced one eight-transistor cell. So: survey with a handful of
  large-area, low-zoom views, decide what to trace, then spend on tracing. Read text
  (trace files, netlist reports, notes) freely; it is cheap.
- Old images drop out of your context as new ones arrive. **Write coordinates and
  conclusions into your notes file as soon as you have them.** Do not rely on
  remembering an image.
- Expect one to two views per unique transistor. Decide which junctions matter and
  look at those, rather than paging through the region.
- **If `notes/blocks/BLOCK.md` already exists, you are continuing someone's work.** Read
  it and the existing trace first. Trust what is marked traced and shipped (it
  extracts); re-check what is marked uncertain when you need it; start from the "Not
  done" list. Do not survey again.
- What a brief says "is known" about a block's structure is the coordinator's belief
  from a low-zoom look and may be wrong (one brief's "one unit per bit" was). Check
  it with one view before building on it.
- **When to compact or start a fresh session: right after a merge and handoff.** Everything
  is then in the notes, the trace and the handoff, and nothing is half-drawn. In the middle
  of a piece a compaction loses the images and the reasoning; if one happens anyway, the
  survey and draft in `cache/scratch/BLOCK/` (section 6, step 1) are what you resume from.
- Ship often. If you run out of room, everything shipped so far is safe, and your notes
  tell the next agent where to resume.
- Your final message should be short (under 300 words): what you traced, the main
  findings, what is uncertain, what is not done, and any problem with the tools. The
  detail belongs in the notes file.
