# busl: the left bus field

Queue row `busl` of `notes/work-packages.md` (written busL until 2026-11-19): the wiring between the
left array (`larr`, rows end at x 4780) and the central datapath (`cdp3`, `cdp4`, from x 7600).
Claimed region: x 4780-7550, y 10400-15000 (the main part; the northern part 6450-7600 x 6750-10400
is not started). Coordinates are metal-shot pixels; images are in `cache/scratch/busl/`. Wiring only:
no transistor has been found in the field so far.

## Status

Run 1 (richtw1's session, Claude Fable 5.2; 2026-11-19 13:50 to 14:00 +0100). Survey of the whole main
part, and one piece, `h8`, wiring only, no uncertain items:

- **The eight west outputs of the central datapath's register row H reach eight rows of the left
  array** (piece `h8`). Each `cdp3_hw_c#` (# = 7..0; `cdp3`: hw = NOT q1 of the 8-bit register row H)
  is drawn end to end across the field: a poly row west from `cdp3`'s piece at x 7600, a pad, a metal
  track south round one step of a staircase, a pad, and a diffusion row west to the array's edge at
  x 4780. The order is kept: c7 goes to the northernmost row (y 11338), c0 to the southernmost
  (y 14894); seven of the eight rows are 477 px apart, the array's row pitch.

Run 2 (richtw1's session, Claude Fable 5.2; 2026-11-19 14:16 to 14:29 +0100). One piece, `ch1`, wiring
only, no uncertain items:

- **`cdp4`'s eight channel-1 lines are its row C latch inputs, and each reaches a row of the left
  array** (piece `ch1`). For every slice # the poly row `cdp4_bus_s#` (channel 1, x 7600, y 11878 ..
  12182) and the poly row `cdp4_in_s#` (channel 2, x 7600, y 13636 .. 13332: the data input of the
  8-bit latch row C, through the pass transistor gated by `cdp4_ld`) are one net, joined in the field
  by a metal track between poly pads; and the same track has a pad on the east end of one poly row of
  the left array (s7 y 11488, s6 11922, s5 12442, s4 12984, s3 13397, s2 13874, s1 14351). s0's track
  leaves the region south at (5451,15000) and ends 45 px on, on the pad of the next such row
  (y 15042, in `bl0`'s region, not drawn). The two names are gathered by `@alias` in `trace/busl.txt`
  (shown as `cdp4_bus_s#`); the rename is the coordinator's.

Full extraction with run 2: 2,374 nets (eight fewer: the eight joins), 4,290 transistors, 0 errors,
0 warnings. The package by itself: 16 nets, 0 errors, 0 warnings.

Full extraction with run 1: 2,382 nets (unchanged: the eight wires lengthen `cdp3`'s nets), 4,290
transistors, 0 errors, 0 warnings. The package by itself: 8 nets, 0 errors, 0 warnings.

## Inventory

The field (survey: `cache/scratch/busl/survey.md`; views `s0_metal.png`, `s0_acid1b.png`):

- About 55 vertical metal tracks at a pitch of 43.4 px between x 4822 and x 7554, stepping sideways in
  staircases; most run on north of y 10400 and south of y 15000. A wide metal x 4960-5010 runs the
  whole height. Track centres at nine heights: `tools/sel_cut.py h Y 4780 7560 --brief`.
- Horizontal lines of two kinds (told apart in the open column x 5072, `tools/busl_rows.py`,
  `tools/px.py`): **diffusion rows** about 22 px wide (chip-2 metal shot blue 80-87; clean shot cream
  160/128/98 between two dark edge lines) and **poly rows** about 28 px wide (blue 52-57; clean shot
  154/90/61 in the open).
- Poly row bands under the tracks at y 10330-10700, 11850-12150, 12550-12900, 13300-13700, 14050-14300
  (`bc1`'s 13-line bus enters it from the east), 14450-14950.
- Drawn by others inside the region: `trunks` (two lines), `bc1` (the bus, lower right), `tla` (7 items).

Piece `h8` (all eight nets have the same build; `#` = the slice of `cdp3`'s row H):

| Net | Poly row y (x from the pad to 7600) | North pad, contact | Track: upper x, step y, lower x | South pad, contact | Diffusion row y (x 4780 to the pad) |
|---|---|---|---|---|---|
| `cdp3_hw_c7` | 10361 | (6039,10359) | 6039, 11272, 5690 | (5690,11335) | 11338 |
| `cdp3_hw_c6` | 10404 | (5996,10402) | 5996, 11230, 5626 | (5647,11812) | 11815 |
| `cdp3_hw_c5` | 10447 | (5953,10445) | 5953, 11186, 5583 | (5605,12290) | 12291 |
| `cdp3_hw_c4` | 10490 | (5909,10488) | 5909, 11142, 5540 | (5562,12766) | 12768 |
| `cdp3_hw_c3` | 10535 | (5866,10533) | 5866, 11100, 5496 | (5514,13222) | 13247; steps north at x 5432 to y 13220 |
| `cdp3_hw_c2` | 10577 | (5822,10575) | 5822, 11054, 5452 | (5474,13722) | 13725 |
| `cdp3_hw_c1` | 10621 | (5778,10619) | 5778, 11012, 5409 | (5427,14197) | 14202 |
| `cdp3_hw_c0` | 10664 | (5735,10662) | 5735, 10966, 5366 | (5385,14888) | 14894 |

- The poly rows run straight for 1,560-1,870 px under about forty tracks each; no track has a pad
  over them (views `b1_acid1b.png`, `b1_metal.png` at 1.3x).
- The north pads are a staircase of poly pads, each the west end of its row, each with the north end
  of its track on it (`t1.png`).
- Each track leans about 20 px east into its south pad (c7's comes straight down); the track ends
  there (`tools/follow.py --gap 16` from each track both ways; `e1.png`, `e2.png`, overlays `o1.png`,
  `o2.png`, `o3.png`).
- Seven of the tracks cross the diffusion rows of the nets north of their own pad, and the poly rows
  of other nets, without contact: `tools/tl5_tracks.py v X Y0 Y1` down each lower track shows only
  pairs of 8-17 px dark bars (the two edges of each row) and no stretch without metal in both chips;
  the clean shot's short greenish stretches (6-10 px) lie on the south edge of each diffusion row and
  nowhere else.

Piece `ch1` (pads are poly pads with a contact, given by the contact's centre, measured in both
metal shots with `tools/busl_padc.py`; row centres with `tools/busl_rowy.py` in open columns; tracks
with `tools/follow.py --gap 16`; every row is poly, 23-24 px between its edge lines):

| Net | Channel-1 row (to x 7600) | From its west end | Array row (x 4780 to its pad) | Channel-2 row (pad to x 7600) |
|---|---|---|---|---|
| `cdp4_bus_s7` | y 11878, pad (5857,11878) | metal arm west along y 11880 to the track x 5800: a T. The track runs north to the array row's pad and south to the channel-2 row's pad | y 11488, pad (5799,11488) | y 13636, pad (5800,13636) |
| `cdp4_bus_s6` | y 11922: the row itself runs on west to the array (one poly, x 4780 to 7600) | pad in the row at (5757,11922); track x 5757 south | the same row | y 13592, pad (5756,13592) |
| `cdp4_bus_s5` | y 11966, pad (5713,11966) | track x 5713 south, through the array row's pad, to the channel-2 pad | y 12442, pad (5713,12443) | y 13549, pad (5712,13550) |
| `cdp4_bus_s4` | y 12009, pad (5841,12010) | track x 5842 south to a pad (5843,12335); poly south along x 5846 and diagonally south-west to a pad (5668,12681); track x 5669 south through the array row's pad | y 12984, pad (5670,12984) | y 13506, pad (5668,13508) |
| `cdp4_bus_s3` | y 12052, pad (5668,12053) | track x 5668 south, west along y 12622 to x 5627, south, west along y 12860 to x 5540, south to a pad (5537,13157); poly from the pad's top east, south along x 5563, west along y 13266, south along x 5497 into the channel-2 row at (5497,13462) | y 13397; at x 5389 it runs diagonally south-east into the channel-2 row at x 5454 (one poly) | y 13462 |
| `cdp4_bus_s2` | y 12096, to x 6412 | the row turns into a diagonal poly, 770 px south-west under about eighteen tracks, to a pad (5624,12898); track x 5626 south through the channel-2 row's pad to the array row's pad | y 13874, pad (5625,13874) | y 13418, pad (5625,13419) |
| `cdp4_bus_s1` | y 12138, pad (7510,12138) at its west end | track x 7511 south to a pad (7511,12745); poly row y 12745 west to x 5945, diagonal south-west, row y 12941 to a pad (5582,12941); track x 5584 south, west along y 13286 to x 5540, south through the channel-2 row's pad, a diagonal step (y 13900-13944) to x 5496, south, west along y 14353 | y 14351, pad (5407,14351) | y 13375, pad (5538,13375) |
| `cdp4_bus_s0` | y 12182, pad (7554,12183) at its west end | track x 7555 south to a pad (7554,12919); poly west and south along x 7513 (410 px) into the channel-2 row at (7513,13332) | none in the region: from the channel-2 row's pad a track x 5582 south, a diagonal step (y 13900-13943) to x 5539, west along y 14398 to x 5451, south across y 15000; it ends on a pad (5365,15042) of a poly row from the west (view `j6.png`; not drawn, `bl0`'s region) | y 13332, pad (5582,13333) |

What was checked beyond the overlays (`o4.png` .. `o8.png`):

- The T of s7 at (5800,11880): `follow.py` from (5800,12050) north runs through to the pad at y 11484
  and south to y 13612; from the north it turns east into the pad (5857,11878); view `j1.png` (2.4x,
  three shots).
- Tracks that run on through a pad (s5 at (5713,12443), s4 at (5670,12984), s2 at (5625,13419), s1 at
  (5538,13375)): `follow.py` stops at each ring from both sides; views `e3.png`, `j3.png`, `c2w.png`
  show the track at full width on both sides of each pad.
- s3's track corner (5627,12860) is 38 px north of s2's pad (5624,12898) and not on it:
  `tools/textmap.py 5596 12840 5660 12916 3`: the arm's metal ends at y 12861, then a dark edge, then
  bare ground (R 144-160 in both chips) at y 12873-12879, then the pad's ring.
- s3's pad joins the poly that leaves it: `tools/textmap.py 5520 13130 5590 13200 3 --acid`: poly colour
  in the chip-2 stripped shot runs unbroken from the pad along its top (y 13148-13151) into the column
  x 5550-5568 (view `j7.png` at 4x). The poly column's junction with the row at (5497,13462):
  `tools/px.py col 5497 13426 13480 3`, no edge line between them.
- s0's poly column x 7513 lies for 410 px under a metal of another net (a track x 7511 that runs from
  y 8902 to 14284, not followed further): `tools/tl5_tracks.py v 7511 12820 13345` finds no hole and no
  stretch without metal: no contact. The column ends at the row's south edge
  (`tools/px.py col 7513 13290 13372 3`).
- No track has a pad on any of the rows or diagonals it crosses: views `c1a.png`, `c1b.png` (channel
  1), `c2a.png`, `k2.png` (channel 2), `k3.png` (row y 12745), `k5.png`, `k6.png` (the diagonals at
  1.5x), `k1.png`, `w1_*.png` (the array rows); `tools/tl5_tracks.py v` down the five long tracks
  finds green holes only at the pads named above.
- A metal staircase at x 6790-7140 has each step's horizontal run lying on one of channel 2's rows
  for 70-90 px (view `k4.png`). `tools/tl5_tracks.py h` along each run finds no green hole; the one
  low reading (y 13375, x 6853-6886, red minus green 15-25) is a yellowish patch of the clean shot,
  and the chip-2 stripped shot shows poly colour there with no hole
  (`tools/textmap.py 6820 13355 6915 13397 3 --acid`). No contact (Ambiguity 4).

## Logic

Wiring only. Traced: the eight joins above (no uncertain item on any). From `cdp3`'s notes:
`cdp3_hw_c#` = NOT q1 of the row H register bit of slice c#, so **the left array's rows at y 11338 ..
14894 each take one bit of register row H, inverted**. Believed, not traced: these eight rows are
eight of the fourteen rows of the memory address counter, and row H is the low byte of a 14-bit
address register (R13, the display start, or R15, the cursor; `regs` is the queue row that decides).
What the rows do with the bit is `larr`'s untraced part (x 3900-4720).

Piece `ch1`. Traced (no uncertain item on any of the eight nets): for each slice # of `cdp4`,
`cdp4_bus_s#` = `cdp4_in_s#`: the channel-1 line (which `cdp4` follows east to a contact under a track
that goes up into its row R1) is the data input of the row C latch bit of the same slice
(`cdp4_lc_s#_a` through the pass transistor gated by `cdp4_ld`), and the same net ends on a poly row
of the left array (s7..s1 at y 11488, 11922, 12442, 12984, 13397, 13874, 14351; s0 on the row at
y 15042 just south of the region, seen and not drawn). Nothing in the field drives these nets. Not
traced: which end drives (the array's rows, or `cdp4`'s row R1 upper, both untraced where these lines
arrive). Believed: the array's rows drive, i.e. eight bits of the memory address counter are what row C
latches on `cdp4_ld` and what row R1 takes from channel 1.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `cdp3_hw_c7` .. `cdp3_hw_c0` | P | x 7600, y 10361, 10404, 10447, 10490, 10535, 10577, 10621, 10664 (18 px wide) | in | `cdp3`'s channel G west pieces, drawn there from x 7600 |
| `cdp4_bus_s7` .. `cdp4_bus_s0` | P | x 7600, y 11878, 11922, 11966, 12009, 12052, 12096, 12138, 12182 (20 px wide) | not known | `cdp4`'s channel-1 lines, drawn there from x 7600 |
| `cdp4_bus_s7` .. `cdp4_bus_s0` (`cdp4`'s name: `cdp4_in_s#`) | P | x 7600, y 13636, 13592, 13549, 13506, 13462, 13418, 13375, 13332 | not known | `cdp4`'s channel-2 west pieces, the row C latch inputs |
| `cdp4_bus_s7` .. `cdp4_bus_s1` | P | x 4780, y 11488, 11922, 12442, 12984, 13397, 13874, 14351 | not known | poly rows on west into the left array (`larr` draws nothing east of x 3900) |
| `cdp4_bus_s0` | M | (5451,15000), 16 px wide | not known | the track goes on 45 px to a pad (5365,15042) on a poly row from the west (`bl0`) |
| `cdp3_hw_c7` .. `cdp3_hw_c0` | D | x 4780, y 11338, 11815, 12291, 12768, 13247, 13725, 14202, 14894 (20 px wide) | in (driven in `cdp3`) | on west into the left array's rows; `larr` draws nothing east of x 3900 |

## Ambiguities

1. **Red patches on the poly rows in the clean shot** (for instance (6340-6385,10353),
   (6095-6140,10530), (6160-6200,10660); each one track wide). Readings: a contact or a channel
   under that track; or a colour difference of chip 1's stripped shot only. Assumed the second:
   neither chip-2 shot shows anything there (the track keeps its width, no ring, no pad; `q1.png`
   at 3.2x, three shots), and a crossing field without pads carries no taps (guide, trap 15).
   Would settle it: nothing more in these photos; the patches' pattern over the whole band could be
   listed and compared with where the tracks' own contacts are.
2. **The rows' layer.** Taken as diffusion from the colours above; a poly row would make no
   difference to any connection here (nothing crosses the rows but metal).

3. **The poly L round c3's south pad** (the pad (5514,13222); a poly runs east along y 13258-13272
   and north along x 5545-5560, at minimum spacing from the pad's south and east edges). The round-1
   reviewer could not resolve the two outlines at 6x in the clean shot. Read by the tracer in the
   chip-2 shots at 5x (`c3s.png`): the pad's outline is closed and a pale strip 3-4 px wide lies
   between it and the poly's outline on both sides; `tools/px.py col 5515 13236 13276 2`: pad to
   y 13244, dark to 13258, poly (chip-2 stripped shot 157/116/63) from 13260. Taken as apart; there is
   no buried-contact box. The poly L itself is not drawn (not this piece's).

4. **Metal lying on a poly row without a pad** (the steps of the staircase x 6790-7140 over channel 2's
   rows; the track x 7511 over s0's poly column, y 12920-13332; a track x 5843 that begins 35 px south
   of s4's pad (5843,12335) and lies on s4's poly for about 100 px). Readings: a contact somewhere
   along the overlap; or none. Assumed none: no pad, no ring, no green hole in the clean shot on any
   (measurements under piece `ch1` above; guide, trap 13). A contact would join one of these eight
   nets to another track's net.
5. **Red and yellowish patches on the poly rows and diagonals in the clean shot** (channel 2 at
   x 6600-6900, the diagonals at (5700,12610), (6250,12250)): as Ambiguity 1, colour only; the chip-2
   shots show nothing there.
6. **Which end drives `cdp4_bus_s#`**: not decidable in the field (it holds no transistor). Settled by
   `larr`'s rows east of x 3900 and `cdp4`'s row R1 upper.

## Review

**Round 1: full review** (2026-11-19 14:05 +0100; a fresh Fable 5.2 reviewer agent; commit 59157c2; piece `h8`).
Told to suspect: the track staircase's order, the north pad staircase, the poly rows (a step, a
break, a tap, the red patches), each south pad (which track is on it, whether it ends), the lower
tracks' crossings, the diffusion rows (straight, their layer, c3's step), a shift by one row at x 7600.
Checked (25 images in `cache/scratch/busl/review-1/`): both pad staircases and the track staircase at
3.4x in the metal and clean shots, with `tools/follow.py --gap 16` on every track; the poly rows by an
edge-pair measurement every 7 px on the chip-2 metal shot to x 7618 (offset 0 to -2 px, width 23, no
step, no break) and views at 1.6x (no pad on any track); two red patches by `tools/textmap.py --acid`
(colour only); the nine rows at x 7600 (the ninth, y 10317, ends on its own pad near (6730,10315);
the eight drawn are the southern eight); each south pad at 4x in two shots; c3's step in three shots;
the lower tracks by `tools/tl5_tracks.py v`; a diagonal poly under c1 and c2 at (5400-5470,13395-13465)
and a pad (5408,14347) beside c0's track (neither touches); the diffusion rows in three shots (chip-2
metal blue 78-87: diffusion).
Findings: none. Could not check: (a) whether the poly L south and east of c3's pad touches the pad
(would change a connection): read afterwards by the tracer in the chip-2 shots, apart (Ambiguity 3);
(b) the diffusion rows and lower-track crossings were read at 1.4x and by text tools, not at 4x;
(c) `cdp3` has no `ports.d` file, so the join at x 7600 rests on the photos and the rows' y.
Nothing changed in the trace.

Round 1: no findings.

## Not done

- Everything else in the field: about 40 more tracks and the other rows. Next pieces, in the
  order they join things: (1) `cdp4`'s other lines at x 7600, each of which ends on a pad with a track
  (seen, not drawn): `cdp4_sel1` (y 12223, pad about (6735,12213)), `cdp4_sel2` (12481, pad
  (6735,12470)), `cdp4_sel3` (12530, pad (6690,12515)), `cdp4_sel4` (12788, pad (6735,12775)),
  `cdp4_rst` (12874, pad (7465,12872), track x 7465 south), `cdp4_ld` (12962, pad (7555,12985), track
  x 7556 south), `cdp4_ld8b` (11837, not looked at); the metal L from x 7465 that turns south at
  x 7511 (y 12830; the long track x 7511 from y 8902 to 14284, west along y 13940 to x 7404, to
  y 14284); the track that begins at (5843,12375) from an arm from the east; (2) the top band's ninth row (y 10317, `cdp3_gate_f`) and
  the three poly rows at the top left (y 10560, 10686, 10736); (3) the staircases at x 5100-5700,
  y 10600-10960 west of piece `h8`'s; (4) the bands at y 11850-12150 and below.
- s0's last 45 px: the track from (5451,15000) to the pad (5365,15042) and the poly row west of it
  (`bl0`, or this package if its region is extended to y 15060).
- The diffusion rows and the poly rows west of x 4780 (`larr` (continue)).
- The northern part (6450-7600 x 6750-10400).
- `trunks`' two lines in the field: taps not checked (R4).
