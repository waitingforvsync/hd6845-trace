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

## Run 4 (2026-11-27), piece `e17127`: the gate `bc2_e15690` ends in (3 transistors; 3 uncertain items, one tie)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 15:37 -0600. Region x 9680-10030, y 17000-17265. Views in `cache/scratch/bc4/e/`:
`a_acid1b`, `a_metal` (the gap east of the rail, 5.4x), `ld_acid1b`, `ld_metal`, `ld_acid` (the load side,
6.5x), `east` (the rows' east ends, 7x), overlay `ov_m`.

    bc4_e17127 = NOR(bc4_m17062, bc2_e15690)        (depends on the tie: Ambiguity 2)

The second load of a cursor-skew decode line, and the twin of `bc4_w17127`: the two NORs stand mirror-imaged
about the M rail's line (x 9663.5) and share its VCC land. The format has no mirrored instance, so every shape is
drawn from measurements here.

- **Gate rows** east of the rail (`tools/px.py col 9990 17040 17210 3 metal`): poly at y 17079-17090,
  17121-17130, 17163-17177: the heights of the west unit's rows.
- **The column** x 9884-9917 in the gap east of the rail (x 9810-9858): dark lines at x 9880-9883 (its rail
  side) and x 9916-9922 (its far side, in the open) in both metal shots on every row between the arms
  (`tools/px.py row Y 9856 9960 3 metal,metal1,acid` for Y = 17084, 17105, 17150, 17170), with plain ground
  between them reading diffusion on the stretches (y 17105: blue 77-86, stripped red - green 10-28; weaker at
  y 17150: 2-26, as in the master's lower stretch) and poly on the two gate rows (blue 49-68); west of the first
  line a pocket of field (y 17105, y 17150: stripped red - green -22..8) in which the two rows end with caps at
  x 9866; east of the second line field.
- **Upper arm**: at y 17060 plain from x 9868 to x 9913 with no line at x 9880 (172-175, blue 84-88, stripped
  red - green 17-22), from the land under the rail (`tools/bd2_umap.py 9796 17000 9880 17070 4 4`: tan
  y 17008-17066; contact (9842,17040): hole, ring in both chips).
- **Lower arm**: the land below (tan (9828-9880, 17188-17260), contact (9844,17205)) reaches east under a tab of
  the rail's metal (bright x 9862-9877 at y 17192-17198 in both chips, tan under it to x 9884:
  `tools/bd2_umap.py 9800 17180 9884 17264 4 4`); east of the tab's edge line (x 9880-9886) plain diffusion
  x 9889-9913 (stripped red - green 13-54). The 6 px under that edge line were drawn `?D`; review round 5 read
  them as joined on its own evidence, and they are firm now (Ambiguity 3, closed).
- **Output**: at y 17128 the column's rail side is plain (the strip leaving west), then a frame (x 9889-9901) and
  the box's interior, then poly from x 9925 east: the middle row's end in a framed box (9885-9923, 17114-17140),
  as in the west unit. The row runs east under the thin metal x 9958-9972 (salmon, no hole:
  `tools/tl5_tracks.py h 17127 9930 9995`; no branch) to a pad (10007,17127) (a green hole in a salmon pad, ring
  and bright centre in the metal shot: view `east`); the thin metal x 10008 runs south from it
  (`tools/tl5_tracks.py v 10008 16950 17260`: none between y 17066 and y 17122; metal from the pad south, with
  bars where it crosses the row of `bc2_e15690`). Drawn to y 17150 (port).
- **The upper gate row** runs east under the same thin metal (no hole: `h 17083 9930 9990`; no branch) to a pad
  (10005,17062) (a green hole in a salmon pad (9990-10022, 17045-17090); ring and centre in chip 1's metal shot,
  `padc`), on which a thin metal x 10008 from the north ends (`v 10008`: metal to y 17038, the pad's ring, no
  metal y 17066-17122). Drawn to y 17010 (port): placeholder `bc4_m17062`.
- **The lower gate row is `bc2_e15690`'s row** (run 1; drawn on from x 9954 to its cap at x 9866).
- **Strip and load** (`tools/px.py row 17130 9676 9892 4 metal,acid,acid1b`): west from the column plain
  diffusion across the gap (x 9868-9884), tan under the rail (x 9808-9860; `tools/bd2_umap.py 9796 17106 9870
  17146 3 3`: y 17121-17131), plain diffusion in the open west of the rail (x 9760-9800: blue 70-91, stripped
  red - green 17-29), under a poly block x 9700-9748 (`col 9722 17090 17200 4`: poly y 17102-17190 with edge
  lines at y 17114-17122 and y 17146-17150), to the VCC land under the M rail (tan to x 9684; the land of
  `bc4_w17127`'s load).
- **Tie**: in the open between the block and the rail a diffusion finger runs south from the strip
  (`col 9776 17110 17200 4`: plain, blue 82-88, stripped red - green 12-25, from y 17126 to y 17158) to a framed
  box (about 9762-9795, 17162-17192; interior plain at (9773-9781, 17174-17186)); the block's poly reaches the
  box's frame at x 9757 (`row 17180 9740 9806 3`). **What is inside the box is not resolved: `?`** (Ambiguity 2).
- **Rails**: the wide metal x 9810-9858 is the line of `bc2`'s E rail; `vss` by the gate's build only.

### Ambiguities (runs 3-4)

2. **The tie of `bc4_e17127`'s load** (`?D 9766,17160:9790,17190`, `?P 9745,17174:9790,17189`,
   `?B 9762,17162:9795,17192`): a framed box where the mirror image of the west unit's tie belongs; nothing
   measured contradicts it, its inside is not read. Without it the load's gate has no connection.
3. *(Closed in review round 5: firm.)* **6 px of `bc4_e17127`'s lower arm** (x 9880-9888, y 17188-17202), under the
   edge line of the rail's metal tab.

## Run 5 (2026-11-27), piece `in2`: the two NORs' other inputs to their north ends (wiring; no join, no uncertain item)

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 15:57 -0600. Views in `cache/scratch/bc4/n/`: `w_end`, `e_end` (the end pads, 7x), `w_row`,
`e_row` (the rows, 5x), `cand`. Connections unchanged (`tools/sameconn.py`): both nets only grow.

- **`bc4_m17040`**: the thin metal x 9177-9191 runs north from y 16990 (`tools/tl3_thin.py 9176 9194 16600 17000
  --thr 176 --min 8`: bars of 8-9 px only, at y 16777 and y 16992, the edges of the diffusion rectangle
  y 16782-16997 that it crosses: plain tan under it, no hole; the follower's "contact candidate" (9186,16887) is
  plain bright metal over plain tan with two specks in chip 2 only: view `cand`) and **ends on a pad
  (9184,16647)**: ring, bright centre, ring down the track in both metal shots and a green centre in the clean
  shot (`tools/px.py col 9184 16625 16700 3 metal,metal1,acid1b`), ground north of it. The pad's poly row
  y 16639-16659 runs east (`tools/tl5_tracks.py rows row 9190 9480 6 16649`: poly to x 9412) under the thin
  metals x 9221-9237, 9270, 9313, 9357 (four: review round 6) without contact (no hole: `h 16649 9210 9370`; no
  branch) to x 9372 (port). A 10 px dark spot on the metal at (9183,16926), in both metal shots, is not a contact
  (review round 6: opposite halves of the metal in the two chips, width kept, the clean shot uniform tan).
  Beyond, between x 9375 and the west rail, stands a structure that is not read.
- **`bc4_m17062`**: the thin metal x 10001-10014 runs north from y 17010 over field and, without contact, over a poly row y 16857-16872
  (review round 6; `tl3_thin 10000 10016 16730 17015`: bars of 10-11 px at y 16849 and y 16872, its edges;
  metal bright between them, salmon without a hole) and **ends on a pad (10007,16778)** (the same profile:
  `tools/px.py col 10007 16755 16830 3 ...`; a green centre in a salmon pad (9990-10025, 16762-16792): view
  `e_end`), ground north of it. The pad's poly row y 16767-16788 runs west under the thin metal x 9958-9972
  without contact (no hole: `h 16777 9930 9990`; no branch) to x 9930 (port). Beyond, at x 9870-9920 beside the
  east rail, stands a structure with a framed box that is not read.

**Believed, not read**: each of these rows is the output row of another unit of the same build on its rail (the
west one about 480 px north of `bc4_w17127`, the east one about 350 px north of `bc4_e17127`): in every unit of
this build traced so far the output leaves by the middle row to a pad and a thin metal going south, as here. So
`bc4_w17127` and `bc4_e17127` would each be the second gate of a pair on its rail. Nothing of those units is
drawn.

## Ports

In `ports.d/bc4.txt`.

## Not done

Everything else: what the third line's pad leads to; `bc4_m17062`'s source and `bc4_e17127`'s loads; on the east rail's lands (review round 5): the lower land runs on to y 17270 and beyond with a second contact near (9853,17255) and west at y 17216-17233 to x 9735 against a poly (9725-9820, 17237-17262), another unit's pull-down; the upper land runs west at y 17005-17028 to x 9740; the units that drive `bc4_m17040` (at the west rail, y about 16650) and `bc4_m17062` (at the east rail, y about 16777); `bc4_w17127`'s loads; a poly row y 17246-17263 that crosses under the west rail against the south edge of the land (9458-9502, 17188-17240) (a pull-down on that land: review round 3); a poly block east of the M rail from x 9698 (a mirror-image load on the same VCC land?); the diffusion rectangle (9060-9255, 16782-16997) under wire A; `bc2_e15343`'s route; the rails; the rest of the region.

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

### Round 5 (full review), 2026-11-27: run 4, piece `e17127`

A fresh Claude Fable 5.2 agent, on commit 47a222a, 12 images in `cache/scratch/bc4/review-5/`. Told that the gate
was drawn shape by shape as a mirror image by a tracer who had made several mistakes that day in this kind of
structure (a pass-over drawn as a contact, poly wires ended in the wrong place, transistors missed), and to check
everything: the column and its two edge lines, the arms and lands, the box, the three pads and the two metals on
x 10008 (one metal through both pads, or two?), the crossings, the strip to the western land, the block, the tie.

**No findings.** The equation and its three transistors stand.

- **The lower arm's 6 px: joined** (the reviewer's own evidence): the clean shot is unbroken tan under the tab to
  x 9884-9886 at y 17191-17199, then a dark bar at x 9888-9892, then plain diffusion from x 9890; the same bar
  appears at x 9870-9876 where the upper arm and the strip certainly leave the rail; in chip 1 the line at
  x 9882 is weak here (67-101, like a bare metal edge) against 26-40 on the column's edge above; the arm has no
  other exit. With the tracer's measurements two independent readings: drawn firm now.
- **The tie box: a buried contact, nothing against it**: frame 9760-9792 x 17163-17197, interior
  9772-9784 x 17174-17188, plain in both metal shots and chip 2's stripped shot; the finger runs into it from the
  strip with no line at y 17140-17160; the block's poly is orange up to the west frame; the block touches
  nothing else. Whether poly covers the interior cannot be read: it stays `?` (Ambiguity 2).
- Geometry, fixed: the column's edges are x 9882 and x 9920 (W 38); the finger is x 9768-9788, with a field
  pocket (9755-9765, 17150-17165) between it and the block; the upper land's west edge under the rail is x 9826.

Checked and found correct: both column edge lines across both gate rows, open only at the upper arm and the
strip, field in the pockets west and on the ground east; the rows end at the rail's edge (no salmon under the
rail at their heights); the output box with a plain interior and the strip plain to its west (the middle row
ends in it: not a third gate); both pads real contacts (green hole, ring and centre in both chips, pits in chip
2's stripped shot), nothing else leaving either; **x 10008 is two metals** (56 px bare in both chips at
y 17066-17122, the clean shot open there), the south one crossing the lower row with no hole and no widening;
no contact of the thin metal x 9965 on any of the three rows; the strip continuous tan under the rail without
contact and diffusion in the open; no branch on the rows or the block. Could not check: the 10 px between the M
rail's edge (x 9686) and the block (x 9697), dark in every shot (the strip's top edge line runs straight into
the land's); the clean shot in the gap and the tie area (read from the other three shots); the lower row east
of x 9954.

Connections before and after the fixes (commit 47a222a against the fixed tree):

    tools/t.sh bc4 sameconn.py 47a222a            ->  connections identical
    .venv/bin/python tools/sameconn.py 47a222a    ->  connections identical

Recorded 2026-11-27 15:51 -0600.

Round 5: no findings that change a connection.

### Round 6 (full review), 2026-11-27: run 5, piece `in2`

A fresh Claude Fable 5.2 agent, on commit fe6a495, 11 images in `cache/scratch/bc4/review-6/`. Told to test: the two
end pads (two-part test; the metals ending; anything else leaving), a contact on the way (wire W over the
diffusion rectangle; the spot (9186,16887)), each metal one piece and the same as the earlier-drawn part, the
rows (one poly, no contact at the crossings, no branch, not a gate; the drawn ends short of the unread
structures).

**No finding changes a connection.** Notes corrected: row W crosses four thin metals, not three (the fourth at
x 9221-9237, no contact); wire E is not over field all the way (a poly row y 16857-16872 under it, no contact);
a 10 px dark spot on wire W at (9183,16926) is not a contact. Geometry: row E's drawn end moved from x 9925,
which sat on the frame line (x 9918-9926) of the box beyond, to x 9930.

Verdicts: both pads real contacts (a green hole in a salmon pad; ring with a bright centre in both metal shots),
each metal ending there with bare ground north for 50 px or more, nothing else leaving either pad; no contact
on the way ((9186,16887) is a chip-2-only speck); each metal one piece across y 16990 and y 17010, no branch;
each row one poly, no contact at any crossing, no branch, field on both sides; x 9372 is 26 px short of the
change at about x 9398. Not checked: the structures beyond both ports.

Connections before and after (commit fe6a495 against the fixed tree):

    tools/t.sh bc4 sameconn.py fe6a495            ->  connections identical
    .venv/bin/python tools/sameconn.py fe6a495    ->  connections identical

Recorded 2026-11-27 16:05 -0600.

Round 6: no findings that change a connection.
