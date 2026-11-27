# bc4: the bottom-centre logic south of `bc2` (9000-11000 x 16300-18550)

Nothing of this region's logic is traced yet. This file starts with the wiring that `bc2`'s work led into.

## Run 1 (2026-11-27), piece `dec`: two decode lines of R8's bits 7,6 to the rows they end on (wiring; no join, no uncertain item)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 14:28 -0600. Views in `cache/scratch/bc4/d/`: `p142`, `p181` (the end pads, 7x,
metal over clean shot), `rowW`, `rowE` (the rows, 3.1x), `jog`, `jog_ov`. Connections unchanged against main
(`tools/sameconn.py`): both nets only grow.

- **`bc2_e15517`** (low for R8 bits 7,6 = 0,1). From `bc2`'s port (9142,16370) the thin metal x 9135-9149 runs
  south (`tools/tl3_thin.py 9133 9150 16360 17200 --thr 176 --min 8`: bars of 8 px only, at y 16473,
  16602, 16777, 16992, down to the pad's ring at y 17149-17166). **Not over plain field all the way** (review
  round 1; the tracer had written so): it crosses two diffusion rectangles, y 16477-16607 (`eof`'s
  `D 8908,16477:9254,16607`) and y 16782-16997 (x 9060 or less to 9255, drawn by no package), tan under the metal
  in the clean shot (190/168/126 against pink 181/116/122); the four bars are their edges. No contact on
  either (no dark stretch between the bars, constant width, flat tan without a hole). It
  **ends on a pad (9141,17171)**: a green hole
  in the middle of a salmon pad (9125-9158, 17155-17188) in the clean shot, ring and bright centre in the metal
  shot, bare ground south of the ring (view `p142`). The pad's poly row y 17160-17180 runs east
  (`tools/tl5_tracks.py rows row 9120 10210 8 17170`: poly from x 9128 to x 9456) under six thin vertical
  metals (x 9185, 9228, 9270, 9312, 9357, 9399) without contact (`h 17170 9150 9460`: no hole; the metals keep
  their width; no branch: `tools/eof_tee.py h 17160 17180 9165 9405`). Small dark dots on the row's edge at each
  crossing in the clean shot (about 8 px, at x 9148, 9190, 9230, 9272, 9315, 9357) are on the row above too
  (y 17120-17140) and have no pad: not holes. Drawn to x 9406 (port). Beyond, at x 9415-9460 against the west
  rail's edge, the row enters a structure that is not read.
- **`bc2_e15690`** (low for bits 7,6 = 1,0). From `bc2`'s port (10138,16300) the thin metal x 10131-10145 runs
  south (`tl3_thin 10130 10146 16290 16575`: no stretch dark in both shots) to a corner at y 16557-16571
  (`tools/px.py col 10160 16545 16595 3 metal,metal1,acid1b`), east to x 10182 and south on x 10174-10189
  (`tl3_thin 10173 10190 16575 17190`: nothing but the pad's ring at y 17147-17165 and y 17175-17190) to its
  **end on a pad (10181,17170)** (ring and bright centre in the metal shot; in the clean shot a mottled dark
  olive hole in the middle of a salmon pad (10163-10198, 17153-17186); bare ground south: view `p181`). The
  pad's poly row y 17159-17180 runs west under five thin vertical metals (x 10138, 10095, 10051, 10008 and
  9958-9972: review round 1) without
  contact (no hole: `h 17170 9930 10170`; no branch) to x 9954 (port). Beyond, at x 9860-9945 beside the east
  rail, it enters a structure that is not read.

So two of the three cursor-skew decode lines run as poly rows towards the two rails of the block below `bc2`,
both at y 17170: `bc2_e15517` towards the west rail (x 9463-9513, which runs on south from `bc2`), `bc2_e15690`
towards the east one. Believed, not read: that they end as gates there (review round 1: row A runs on in the
open to about x 9456, and the clean shot under the west rail at that height is field pink).

The third, `bc2_e15343`, is run 2.

## Run 2 (2026-11-27), piece `dec1`: `bc2_e15343` to its end pad (wiring; no join; 6 `?M`)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 14:46 -0600. Views in `cache/scratch/bc4/b/`: `s1`, `s2` (the metal from y 16370 to
y 17045 in both metal shots and the clean shot, 4x), `corner`, `pad`, overlay `ov_pad`, `end`. Connections and
equations unchanged against main (`tools/sameconn.py`; `bc2_e15343` stays firm: the `?M` lie beyond every drawn
gate of the net).

**`bc2_e15343`** (low for R8 bits 7,6 = 0,0). From `bc2`'s port (9551,16370) the thin metal (centre x 9552-9556,
10-12 px wide: measured on each bright segment) runs south past the gates east of the west rail and **ends on a
pad (9554,17518)**: a green hole (x 9545-9565, y 17508-17525) in the middle of a salmon pad (9530-9575,
17500-17532) in the clean shot; ring y 17497-17508 and y 17524-17536 round a centre in both metal shots
(`tools/px.py col 9552 17470 17560 3 metal,metal1,acid1b`; the centre is dim in chip 2, 99-153, bright in chip 1,
167-180); bare ground south of the ring at y 17538-17548.

- **`tools/follow.py` is wrong here**: it bridges from the pad onto another wire's horizontal metal
  (y 17550-17570, which has its own pad at about (9597,17558)) and reports a route "to y 17568, west to x 9358, north
  to y 17428". That is not this net; `bc2`'s notes and handoffs of runs 11-12 quote it as the follower's and
  should not be read as the wire's route.
- **No contact on the way** (tracer's test, each long dark stretch: the widest bright metal across it is
  14-20 px, never a pad's 34; of 120-140 clean-shot samples under each, 3-17 are hole-like, scattered at edges;
  views `s1`, `s2`: the clean shot under the metal is tan, salmon or pink, with framed "bottle" boxes at
  y 16455-16500 and y 16600-16650 and no hole).
- **`?M` by trap 27** (`tools/tl3_thin.py 9543 9562 16360 17575 --thr 176 --min 8`: dark in both metal shots
  for 14 px or more): y 16383-16418 (36 px), y 16449-16489 (41 px), y 16600-16614 and 16623-16638, y 16711-16747
  (37 px), y 16837-16858 and 16865-16879, y 16989-17026 (38 px). Six `?M` pieces; elsewhere bars of 8-13 px.
  What each lies over (boxes and node edges of gates that no package has drawn) is not read.
- The pad's poly is a column x 9524-9540 along its west side, y 17467-17546 (review round 2; the tracer had it
  leaving south-west only): south a 14 px foot that ends at y 17546 (field under the horizontal metal beyond);
  north to a rounded framed patch (9526-9540, 17466-17482), buried-contact-like, not read: port.

So all three decode lines of R8's bits 7,6 are followed to an end pad: `bc2_e15517` (9141,17171),
`bc2_e15690` (10181,17170), `bc2_e15343` (9554,17518).

### Ambiguities (run 2)

1. **Continuity of `bc2_e15343`'s thin metal over six dark stretches** (the `?M`). For: the metal keeps its line
   and width on both sides of each, and no hole lies under any. Against: the photos cannot show metal on a step
   (trap 27), and two stretches are 41 and 38 px long.

## Run 3 (2026-11-27), piece `n17127`: the gate `bc2_e15517` ends in (3 transistors, no uncertain item)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 15:02 -0600. Region x 9160-9700, y 17020-17250. Views in `cache/scratch/bc4/g/`:
`a_acid1b`, `a_metal`, `a_acid` (the gap west of the rail, 7x), `u_c`, `u_m` (the unit, 4.3x), `ld_acid1b`,
`ld_metal`, `ld_acid` (the load end, 8x), `west` (the rows' west ends, 7x), overlays `ov`, `ov_m`.

    bc4_w17127 = NOR(bc4_m17040, bc2_e15517)                    (firm)

**The first load of a cursor-skew decode line**: the output is low whenever R8's bits 7,6 are not 0,1
(`bc2_e15517` high) or `bc4_m17040` is high.

The unit has the build of `bc2`'s first two on this rail and is drawn as a copy of its cell
(`@inst bc2_wnor 0,2084`). Each part was measured here, not taken from the cell:

- **Gate rows** (`tools/px.py col 9376 17050 17200 3 metal`): poly at y 17077-17090, 17120-17133, 17164-17177:
  2,084 px below unit 1's three rows, each.
- **The column** in the gap between the thin metal x 9399 and the rail: its east edge line at x 9446-9449 in both
  metal shots across the upper row (`tools/px.py row 17090 9404 9466 3 metal,metal1`: 53-64 / 30-39 between
  poly at 128-167), the stretch below it (`row 17105`: 55-75), the stretch above the lower row (`row 17150`:
  57-75) and the lower row (`row 17170`: 57-65); absent on the upper arm (`row 17056`, `17060`: plain 150-174
  from x 9419 to x 9455, stripped red - green 16-27), on the lower arm (`row 17192`: plain 164-172 to x 9455)
  and where the strip leaves (`row 17128`: a frame line at x 9428-9434, plain from x 9440).
- **Lands** under the rail (`tools/bd2_umap.py 9446 17010 9530 17110 4 4`, `9440 17100 9530 17250 3 4`): above,
  y 17030-17068 with a contact (9478,17044); below, y 17188-17240 with a contact (9479,17210) (`padc`: hole,
  ring in both chips, each). Between them the rail lies over field (pink; a dark stripe x 9482-9494 down its
  middle is in the clean shot only, as further north).
- **Output**: the middle row's end in a framed box at the column (as unit 1's); the row runs west under the thin
  metals x 9399, 9357, 9312, 9270, 9228 without contact (`tools/tl5_tracks.py h 17127 9205 9400`: no hole; no
  branch) to a pad (9183,17127) (a green hole in a salmon pad (9165-9210, 17112-17140), ring and bright centre
  in the metal shot: view `west`); a thin metal x 9177-9191 runs south from the pad (`tools/tl3_thin.py 9177
  9193 17135 17480`: the pad's ring, then bars of 8-10 px; none north of the pad). Drawn to y 17200 (port).
- **Strip and load**: tan under the rail at y 17120-17132 (`tools/bd2_umap.py 9450 17106 9530 17146 3 3`),
  plain across the gap (`tools/px.py row 17127 9436 9660 4 metal,acid,acid1b`: blue 87-91, stripped red - green
  18-30), tan under the thin metal x 9545-9560, under a poly block x 9584-9628 (`col 9600 17085 17200 4`: poly
  y 17105-17189 with edge lines at y 17117-17121 and y 17145-17153), onto a land under the M rail
  (`tools/bd2_umap.py 9626 17090 9704 17170 3 4`: tan (9635-9690, 17122-17160); contact centred (9661,17143):
  hole, ring in both chips; review round 3 moved it from (9650,17150)).
- **Tie**: under the thin metal x 9545-9560 the strip's tan runs on south to y 17160, then a framed box
  (y 17162-17190) to which the block's bottom-left reaches (view `ld_acid1b`). **No contact of the thin metal**
  (`bc2_e15343`'s) there: it is not widened (17-19 px bright at y 17150-17158, none over the frame), the clean
  shot is tan without a hole; review round 2 judged this box (9551,17180) a pass-over independently.
- **The lower gate row is `bc2_e15517`'s row** (run 1; drawn on the 6 px to the cell).
- **The upper gate row** runs west under the same five thin metals without contact (`h 17084 9205 9400`: no
  hole; no branch) to x 9200, where it meets a poly column x 9178-9200 that comes from the north
  (`tools/tl5_tracks.py rows col 16980 17100 6 9189`: poly y 17052-17086; orange with an outline on its west
  and south in the metal shot: view `west`). **It ends on a contact pad (9183,17040)** (review round 3; the tracer
  had stopped the poly at y 17055 as a port "from the north"): pad 9166-9200 x 17023-17057, a hole in the clean
  shot and ring with a bright centre in both metal shots (`padc`), on which a thin metal x 9177-9193 from the north
  ends (`tools/tl3_thin.py 9176 9194 16700 17020`: bars of 8-9 px only down to the pad). Drawn to y 16990 (port):
  placeholder `bc4_m17040`.
- **Rails**: the wide metal x 9463-9513 is the west rail of `bc2` (it runs on south from there; its metal between
  y 16335 and y 17020 is not drawn) and the wide metal x 9642-9698 its M rail's line. They are labelled `vss` and
  `vcc` here by the gate's build, as in `bc2`: neither is followed to a supply.

## Ports

In `ports.d/bc4.txt`.

## Not done

Everything else: what `bc2_e15690`'s row and the third line's pad lead to; `bc4_m17040`'s source and `bc4_w17127`'s loads; a poly row y 17246-17263 that crosses under the west rail against the south edge of the land (9458-9502, 17188-17240) (a pull-down on that land: review round 3); a poly block east of the M rail from x 9698 (a mirror-image load on the same VCC land?); the diffusion rectangle (9060-9255, 16782-16997) under wire A; `bc2_e15343`'s route; the rails; the rest of the region.

## Review

### Round 1 (full review), 2026-11-27: run 1, piece `dec`

A fresh Claude Fable 5.2 agent, on commit f32c9a1, 16 images in `cache/scratch/bc4/review-1/`. Told to suspect: the
two end pads (two-part test; anything else leaving them; the metals going on), a contact from either row to a
thin metal above it (the dark dots at the crossings), a contact or branch along the three vertical stretches and
at the jog, the rows (one poly, no branch, no gate), and the joins with `bc2`'s metals.

**No finding changes a connection; no geometry moved.** Three corrections to the notes and comments, made:
wire A does not run over plain field (it crosses two diffusion rectangles without contact: see the run's notes);
row C passes under five thin metals, not four (the fifth at x 9958-9972, no contact: same width at y 17130,
17170, 17195, bright through the row in both chips, salmon without a hole); and "end as gate rows at the two
rails" was not read (now worded as believed).

Checked and found correct: pad A a contact (a green hole 14 px across in a salmon pad, ring with a 10 px bright
centre in both metal shots, the metal ends there, open ground west and south; the pad at (9098,17210) is
separate); pad C a contact (its hole olive, not green; accepted on ring and bright centre in both metal shots
and a pale centre in chip 2's stripped shot like pad A's; the metal ends there, 35 px without metal to a
separate metal at y 17205-17225; nothing leaves east); no contact at any of the eleven crossings (no ring, no
hole, no widening; the large dark marks in the clean shot are open poly in the gaps between the metals; a dark
blemish on the metal x 9228 over row A is in chip 2 only); the rows one poly each, no branch, plain ground
between row A and the row north of it, pink field on both sides under every metal (no gate); the jog one metal
round both corners with no T; wire C's verticals over field throughout; the same metal across (9142,16370) and
(10138,16300). Could not check: anything beyond the two drawn row ends.

Connections (comments only changed; commit f32c9a1 against the tree):

    tools/t.sh bc4 sameconn.py f32c9a1            ->  connections identical
    .venv/bin/python tools/sameconn.py f32c9a1    ->  connections identical

Recorded 2026-11-27 14:41 -0600.

Round 1: no findings that change a connection.

### Round 2 (full review), 2026-11-27: run 2, piece `dec1`

A fresh Claude Fable 5.2 agent, on commit 72500b7, 19 images in `cache/scratch/bc4/review-2/`. Told to test,
hardest first: a contact anywhere on the 1,150 px (two-part test; every dark stretch of 14 px or more and every
pair of bars 10-16 px apart), one metal on one line, the end pad and its separation from the horizontal metal
south of it, the `?M` stretches, the join with `bc2`'s metal.

**No finding changes a drawn connection.** One finding changes the port: the pad's poly leaves NORTH as well as
south: one column x 9524-9540 from y 17467 to y 17546 along the pad's west side (orange in both metal shots with
no edge line across), its south arm a 14 px foot that ends, its north end a rounded framed patch (9526-9540,
17466-17482), buried-contact-like, not read. Drawn now, with the port at its north end. Geometry: at
y 16804-16834 the visible metal is x 9546-9552 (drawn so). Notes: the other wire's pad is at about (9597,17558).

Verdicts: (1) no contact: a green-patch scan of the clean shot under x 9546-9560 from y 16360 to y 17540 finds
only the end pad's hole (12 x 13 px); the bright metal is never wider than 14 px; the closest look-alikes,
(9551,16617) and (9551,17180), are framed boxes of about 26 x 30 with tan interiors, no pit in chip 2's stripped
shot and no widening, like `bc2`'s tie box under this same metal. (2) One metal on one line, x 9546-9561
throughout, no neighbouring metal within 30 px. (3) The end pad a real contact and the metal ends on it: the
strip y 17540-17548 is at bare-ground level in both chips and green in the clean shot; no metal leaves east or
west. (4) The `?M` are right: every stretch of 14 px or more is covered. (5) The same metal as `bc2`'s (overlap
y 16360-16370). Not checked: continuity through the six `?M` (the photos cannot show it); what the column's
north end joins.

Connections before and after the fixes (commit 72500b7 against the fixed tree; the added poly column joins
nothing else):

    tools/t.sh bc4 sameconn.py 72500b7            ->  connections identical
    .venv/bin/python tools/sameconn.py 72500b7    ->  connections identical

Recorded 2026-11-27 14:58 -0600.

Round 2: no findings that change a connection.

### Round 3 (full review), 2026-11-27: run 3, piece `n17127`

A fresh Claude Fable 5.2 agent, on commit 3874460, 19 images in `cache/scratch/bc4/review-3/`. Told that the cell's
master stands and the copy's fit is unchecked; to suspect each shape of the shifted cell, the column and its side
of the edge line, the arms and lands, the middle box, the strip to the VCC land, a contact of the thin metal
x 9552, the block, the crossings, the output pad, the upper row's corner and what lies beyond it, and anything
the cell does not have.

**The gate and its equation stand. One finding changes where a wire ends, fixed:** the upper input's poly column
does not come "from the north" past y 17055: it ends on a contact pad, centre about (9183,17040), on which a thin
metal x 9177-9193 from the north ends (`tools/tl5_tracks.py v 9184 17000 17260`: metal to y 17016, ring
y 17017-17036, bright centre y 17037-17043 in both chips, no metal y 17044-17121, a clean-shot hole at y 17039).
The tracer checked it (`padc`: hole, ring in both chips) and drew the pad, the contact and the metal to y 16990;
the net's placeholder is now `bc4_m17040` (it had a poly-row placeholder before, which never reached main).

Geometry, fixed: the VCC contact is centred about (9661,17143), not (9650,17150); the M rail is x 9638-9686 here.
For the record (in "Not done"): from x 9698 an undrawn poly block (y 17102-17190) carries the same two edge
lines, a mirror-image load, so the VCC land is probably shared eastwards; and a poly row y 17246-17263 crosses
under the west rail directly against the lower land's south edge (tan, salmon, tan down x 9490 with no field
between): a pull-down with that land as its source, not this gate's.

Checked and found correct: the copy against the master (row profiles at seven heights and side-by-side views:
every cell shape within about 3 px at +2,084); the column (the edge line x 9446-9449 across both gate rows and
both bands, absent on the arms and where the strip leaves; field east of it); both arms continuous tan into
their lands, each land one region with one contact; the box a buried contact, no third gate; the strip unbroken
from x 9442 to the VCC land with no poly and no contact under the rail or the thin metal; the tie a pass-over
(the metal stays 12 px wide, no hole); no contact at any crossing, including the output's metal over the lower
row at (9184,17170); no link between the rows, no branch; the pad (9183,17127) a real contact with the metal
leaving south only; the corner one poly with the upper row, nothing west or south. Could not check: the
column's bands between the gate rows are diffusion by edge lines only (chip 2's stripped colour reads
field-like there, in the master too); the strip under the load block is inferred from the two edge lines; poly
continuity across the 8 px dark lines at x 9408-9414 and at the tie box's frame.

The fix adds a pad, a contact and a metal to one net and renames it, so no "connections identical" line belongs
here; the fix check reads the addition against the photos.

Recorded 2026-11-27 15:17 -0600.

Round 3: one finding that changes a connection (a wire's end: a pad and its metal not drawn), fixed. Fix check next.

### Round 4 (fix check), 2026-11-27: run 3, piece `n17127`

A fresh Claude Fable 5.2 agent, on the changes 3874460..677970d only, 5 images in `cache/scratch/bc4/review-4/`.
Asked: is (9183,17040) a real contact, the pad one poly with the column and the row, the metal ending on it from
the north, nothing else leaving it, and no link to the output's pad 87 px south; the supply contact's centre
and the rail's width; the label's point.

**No findings.** The pad: a ring of about 40 px with a yellow centre in both metal shots, a dark hole mid-pad in
both chip-1 stripped shots (93/82/44 against salmon 182/145/89) and a pit in chip 2's; one poly (salmon to
y 17061, then open poly to the row, orange in both metal shots with no cross line); the metal yellow at
x 9178-9193 from y 17002 to y 17017 and north of y 16990 (the 8 px bar at y 16992-17000 crosses the neighbouring
metals and ground too: an edge underneath), none from y 17044 to y 17121; nothing else leaves the pad; plain
ground between the two pads at y 17098-17104. The supply contact's centre (9660,17142), the land
(9635-9690, 17121-17162) and the metal's edges x 9637 / 9686 as drawn. The label lies on the metal; the
extraction gives `bc4_w17127` = NOR(`bc2_e15517`, `bc4_m17040`). Nothing changed in the trace.

Recorded 2026-11-27 15:26 -0600.

Round 4: no findings.
