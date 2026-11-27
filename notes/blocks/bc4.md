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
open to about x 9456, and the clean shot under the west rail at that height is field pink). The third, `bc2_e15343`, runs through this region on x 9552 (`tl3_thin 9543 9562 16360 17575`: ten
stretches of 14 px or more dark in both shots, over boxes: not drawn; `tools/follow.py`: to y 17568, west to
x 9358, north to y 17428).

## Ports

In `ports.d/bc4.txt`.

## Not done

Everything else: what the two rows end in; the diffusion rectangle (9060-9255, 16782-16997) under wire A; `bc2_e15343`'s route; the rails; the rest of the region.

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
