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

## Ports

In `ports.d/bc4.txt`.

## Not done

Everything else: what the two rows and the third line's pad lead to; the diffusion rectangle (9060-9255, 16782-16997) under wire A; `bc2_e15343`'s route; the rails; the rest of the region.

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
