# busl: the left bus field

Queue row `busl` of `notes/work-packages.md` (written busL until 2026-11-19): the wiring between the
left array (`larr`, rows end at x 4780) and the central datapath (`cdp3`, `cdp4`, from x 7600).
Claimed region: x 4780-7550, y 10400-15000 (the main part; the northern part 6450-7600 x 6750-10400
is not started). Coordinates are metal-shot pixels; images are in `cache/scratch/busl/`. Wiring only:
no transistor has been found in the field so far. Three pieces are drawn: `h8`, `ch1`, `lc9`.

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

Run 3 (richtw1's session, Claude Fable 5.2; 2026-11-19 16:30 to 16:42 +0100). One piece, `lc9`, wiring
only, no uncertain items:

- **The nine metal lines that leave `lc3` south at y 10400 run down the whole field as one staircase
  bundle and end at its foot on the poly rows of the bottom-centre logic's 13-line bus** (piece `lc9`).
  With `tla`'s metal of `rcs_e4` (the tenth and easternmost line, drawn in `trace/tla.txt`) the lines
  keep their order through two staircases (y 11491-11880 and y 12380-12772) and turn east along
  y 14916-14528, the westernmost lowest. Seven end on a poly pad (x 6320-6409) whose poly row runs east
  under the next thirty tracks: `lc3_e9798` on the row y 14567, `lc2_w9079` on 14611, `lc3_e9756` on
  14654, **`lc3_w9470` (the input of the inverter that drives `lc1_w7170`) on 14697**, `lc2_w8450`
  (the ripple counter's clear) on 14740, **`lc3_w9947` (the ripple counter's clock, `lc2_x6432`) on
  14784**, and `lc2_x6299` on 14914. The rows are drawn to the region's edge at x 7550; they run on
  240-290 px to pads at x about 7790 and 7835, the west ends of `bc1`'s 13 bus metals (seen, not drawn:
  `bc1`'s region). `lc2_x6342` and `lc2_x6387` turn south instead (x 6366, x 6408) and leave the
  region at y 15000. No line has a pad or contact between y 10400 and its end.

Full extraction with run 3: 2,399 nets (unchanged: the nine lines lengthen `lc3`'s and `lc2`'s nets),
4,345 transistors, 0 errors, 0 warnings. The package by itself: 25 nets, 0 errors, 0 warnings.

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
| `cdp4_bus_s0` | y 12182, pad (7554,12183) at its west end | track x 7555 south to a pad (7554,12919); poly west and south along x 7513 (410 px) into the channel-2 row at (7513,13332) | none in the region: from the channel-2 row's pad a track x 5582 south, a diagonal step (y 13916-13959) to x 5539, west along y 14398 to x 5451, south across y 15000; it ends on a pad (5365,15042) of a poly row from the west (view `j6.png`; not drawn, `bl0`'s region) | y 13332, pad (5582,13333) |

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

Piece `lc9` (track centres with `tools/sel_cut.py h Y` at twelve heights and `sel_cut.py v` in the
middle of each horizontal run; every line with `tools/follow.py --gap 16`; pad contacts with
`tools/busl_padc.py` in both metal shots; row centres with `tools/busl_rowy.py`; all metals 12-15 px
wide, drawn 14; all rows poly, 23-24 px between their edge lines):

| Line | Net | x from y 10400 | Step west at y | x | Step west at y | x | East along y | End |
|---|---|---|---|---|---|---|---|---|
| 1 | `lc2_x6299` | 6082 | 11491 | 5908 | 12380 | 5844 | 14916 | pad, contact (6320,14914); poly row y 14914 east |
| 2 | `lc2_x6342` | 6126 | 11534 | 5953 | 12424 | 5888 | 14874 | turns south at x 6366; leaves the region at (6366,15000) |
| 3 | `lc2_x6387` | 6169 | 11577 | 5996 | 12466 | 5932 | 14830 | turns south at x 6408; leaves the region at (6408,15000) (the follower runs on to y 15150) |
| 4 | `lc3_w9947` | 6212 | 11622 | 6040 | 12506 | 5975 | 14787 | pad (6406,14784); row y 14784 |
| 5 | `lc2_w8450` | 6256 | 11664 | 6083 | 12553 | 6018 | 14744 | pad (6365,14741); row y 14740 |
| 6 | `lc3_w9470` | 6299 | 11708 | 6126 | 12596 | 6061 | 14700 | pad (6408,14696); row y 14697 |
| 7 | `lc3_e9756` | 6342 | 11752 | 6169 | 12640 | 6105 | 14656 | pad (6365,14655); row y 14654 |
| 8 | `lc2_w9079` | 6386 | 11794 | 6212 | 12683 | 6148 | 14613 | pad (6409,14612); row y 14611 |
| 9 | `lc3_e9798` | 6429 | 11838 | 6256 | 12726 | 6191 | 14570 | pad (6363,14568); row y 14567 |
| 10 | `rcs_e4` (`trace/tla.txt`, not this piece) | 6472 | 11880 | 6300 | 12772 | 6235 | 14528 | contact (6407,14526); row y 14523 to the pad (7012,14522) |

- Names are `lc3`'s at its south edge (`ports.d/lc3.txt`); line 4's `lc3_w9947` gathers `lc2_x6432`.
  **Line 5 is firmly `lc2_w8907`'s metal** (`lc3`'s name for it; the gates of the ripple counter's clear
  transistors are on that piece); it is `lc2_w8450`, the output of the inverter of `lc1_w7170`, only
  through `lc2`'s uncertain box (`?P 5598,8899:5612,8914`, `?B 5604,8897:5614,8916`, with its
  `@alias lc2_w8450 lc2_w8907`): `tools/unsure.py` lists `lc2_w8450` as two pieces without the uncertain
  items, line 5 on the piece of `lc2_w8907` (Ambiguity 8).
- The staircases are plain right-angle steps over field, nothing underneath (views `l9_s2.png`,
  `l9_s3.png`, overlays `l9_o1.png`, `l9_o2.png` at 1.5x). Two of `ch1`'s diagonal polys cross the second
  staircase.
- No break: `tools/tl5_tracks.py v` down all thirty vertical segments (`cache/scratch/busl/l9_scan.txt`)
  finds no stretch of 18 px or more without metal in both chips, only the 8-17 px edge bars of the rows
  crossed. No pad along any line: every "wide" stretch `tools/follow.py` reports is at a corner. The
  follower loses line 4 at its second step (the diagonal poly of `cdp4_bus_s2` crosses the corner) and
  line 9 at its first corner; each was picked up again beyond ((5975,12560), (6256,11900)) and followed
  both ways.
- The tracks cross, without contact, `cdp3_hw_c#`'s poly rows (y 10361-10664), `cdp4_bus_s#`'s rows
  and diagonals (y 11878-12182, 12290-12480, 12745, 13332-13636) and the undrawn rows of the bands at
  y 12550-12900, 14050-14300 and 14450-14570. Where a track crosses a poly the clean shot is greenish
  for 6-13 px under it at many crossings (red minus green down to -5: (6126,12387), (6342,10577),
  (6169,10446), (6212,10449), `rcs_e4`'s (6472,10490)): tiles at 4x in four shots beside the contact
  (6409,14697) (`l9_c1.png`) show the track at its own width with the row's two edge bars and no ring
  in either metal shot at all five (guide, trap 15).
- The end pads (view `l9_o3.png`, 3.2x, metal and clean shots with the trace): each has the metal
  arriving from the west and one poly leaving east; no metal beyond the ring (`follow.py`: none for
  16 px), field north and south. Lines 2 and 3 cross line 1's row y 14914 on their way south:
  `tools/tl5_tracks.py v 6365 14890 15060` and `v 6408 14845 15060`: two edge bars each, no hole.
- The rows (views `l9_e1.png` at 1.05x, `l9_e2.png`, `l9_e3.png` at 1.5x, clean and metal shots): ten
  poly rows at y 14523, 14567, 14611, 14654, 14697, 14740, 14784, 14827, 14870, 14914, the same y
  within 1 px at x 6450, 6583, 6710, 6884, 6972, 7080, 7146, 7300, 7390 (no step). Seven are this
  piece's. Row 14523 is `rcs_e4`'s as far as the pad (7012,14522), and another net starts on it at the
  pad (7100,14522) (`bc1`'s R10); rows 14827 and 14870 begin at pads (6915,14828) and (6872,14868) of
  two tracks that come from the north (x 6927 and x 6885; no metal south of either pad:
  `tools/tl5_tracks.py v 6915 14850 15000`, `v 6872 14885 15000`; other nets, not drawn). `tools/tl5_tracks.py h Y 6432 7552`
  along each of the seven lists greenish stretches in the clean shot; the eight strongest ((6665,14567),
  40 px long, (6846,14914), (6621,14567), (6715,14697), (6886,14740), (6804,14784), (7533,14784),
  (6502,14784)) as tiles at 3.5x in four shots (`l9_c2.png`): in both metal shots every track crosses
  at its own width, no pad, no ring; the chip-2 stripped shot shows plain poly: colour of chip 1's
  stripped shot only (Ambiguity 5).
- East of x 7550 (seen, `l9_e3.png`; not drawn): the ten rows run on under four more metals to pads
  with contacts in two columns, row 14523 to (7835,14520), 14567 to (7790,14567), 14611 to (7835,14610),
  14654 to (7790,14654), 14697 to (7835,14697), 14740 to (7790,14740), 14784 to (7835,14784), 14827 to
  (7790,14827), 14870 to (7835,14870); row 14914 goes on past x 7860. These are the west ends of
  `bc1`'s thirteen bus metals (`notes/blocks/bc1.md`: y 14354 .. 14873, x 7780-8280).

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

Piece `lc9`. Traced (no uncertain item of this package on any of the nine nets; line 5's name
`lc2_w8450` rests on an uncertain box of `lc2`'s, Ambiguity 8): each line is one metal from
`lc3`'s south edge to its end, with no contact on the way, so nothing in the field drives or loads
them. Seven go on as poly rows toward the bottom-centre logic's bus: **the ripple counter's clock
`lc3_w9947` (row y 14784), `lc3_w9470`, whose inverse is `lc1_w7170` (row y 14697), the counter's
clear `lc2_w8450` = NOT `lc1_w7170` (row y 14740), `lc2_w9079` = NOT `lc3_w9299` (row y 14611),
`lc3_e9756` (14654), `lc3_e9798` (14567) and `lc2_x6299` (14914)**; `rcs_e4` (the step logic's NOR,
`tla`) is the row above them (14523). Two (`lc2_x6342`, `lc2_x6387`) go on south into `bl0`'s ground.
Not traced: what is at the far end of any of them (the rows' pads at x 7790/7835 and the bus metals are
`bc1`'s; `lc3_w9470` and `lc3_e9756`, `lc3_e9798` also have ends east of `lc3` in the northern part).
Believed: the clock of the ripple counter and `lc3_w9470` are driven in the bottom-centre logic, and
`lc2_w8450` and `lc2_w9079`, which have their drivers in the left-centre strips (`lc2_w8450`'s through
`lc2`'s uncertain box), are inputs there.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `cdp3_hw_c7` .. `cdp3_hw_c0` | P | x 7600, y 10361, 10404, 10447, 10490, 10535, 10577, 10621, 10664 (18 px wide) | in | `cdp3`'s channel G west pieces, drawn there from x 7600 |
| `cdp4_bus_s7` .. `cdp4_bus_s0` | P | x 7600, y 11878, 11922, 11966, 12009, 12052, 12096, 12138, 12182 (20 px wide) | not known | `cdp4`'s channel-1 lines, drawn there from x 7600 |
| `cdp4_bus_s7` .. `cdp4_bus_s0` (`cdp4`'s name: `cdp4_in_s#`) | P | x 7600, y 13636, 13592, 13549, 13506, 13462, 13418, 13375, 13332 | not known | `cdp4`'s channel-2 west pieces, the row C latch inputs |
| `cdp4_bus_s7` .. `cdp4_bus_s1` | P | x 4780, y 11488, 11922, 12442, 12984, 13397, 13874, 14351 | not known | poly rows on west into the left array (`larr` draws nothing east of x 3900) |
| `cdp4_bus_s0` | M | (5451,15000), 16 px wide | not known | the track goes on 45 px to a pad (5365,15042) on a poly row from the west (`bl0`) |
| `cdp3_hw_c7` .. `cdp3_hw_c0` | D | x 4780, y 11338, 11815, 12291, 12768, 13247, 13725, 14202, 14894 (20 px wide) | in (driven in `cdp3`) | on west into the left array's rows; `larr` draws nothing east of x 3900 |
| `lc2_x6299`, `lc2_x6342`, `lc2_x6387`, `lc3_w9947`, `lc2_w8450`, `lc3_w9470`, `lc3_e9756`, `lc2_w9079`, `lc3_e9798` | M | y 10400, x 6082, 6126, 6169, 6212, 6256, 6299, 6342, 6386, 6429 (14 px wide) | `lc2_w8450`, `lc2_w9079`: in (driven in `lc2`, `lc3`; for `lc2_w8450` through `lc2`'s uncertain box, Ambiguity 8); the others not known | `lc3`'s nine metals at its south edge (its file ends them at y 10400; it calls the fifth `lc2_w8907`) |
| `lc3_e9798`, `lc2_w9079`, `lc3_e9756`, `lc3_w9470`, `lc2_w8450`, `lc3_w9947`, `lc2_x6299` | P | x 7550, y 14567, 14611, 14654, 14697, 14740, 14784, 14914 (24 px wide) | as above | poly rows on east 240-290 px to pads at x about 7790 / 7835 under `bc1`'s 13-line bus metals (not drawn) |
| `lc2_x6342`, `lc2_x6387` | M | (6366,15000), (6408,15000), 14 px wide | not known | tracks on south into `bl0`'s ground (line 3 seen to y 15150) |

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
   rows; the steps of a second staircase at x 6290-6740 over channel 1's rows, about 180 px each; the track x 7511 over s0's poly column, y 12920-13332; a track x 5843 that begins 35 px south
   of s4's pad (5843,12335) and lies on s4's poly for about 100 px: it is line 1 of piece `lc9`,
   `lc2_x6299`, after its second step). Readings: a contact somewhere
   along the overlap; or none. Assumed none: no pad, no ring, no green hole in the clean shot on any
   (measurements under piece `ch1` above; guide, trap 13). A contact would join one of these eight
   nets to another track's net.
5. **Red and yellowish patches on the poly rows and diagonals in the clean shot** (channel 2 at
   x 6600-6900, the diagonals at (5700,12610), (6250,12250)): as Ambiguity 1, colour only; the chip-2
   shots show nothing there. The same on piece `lc9`'s seven rows at x 6450-6900 (red, dark and
   green patches one track wide; the eight strongest are listed under the piece) and, greenish, where
   its tracks cross `cdp3_hw_c5`'s row y 10447 (five tracks in a row: a tap on each would short five
   nets to one register bit). A contact on any would join one of the nine nets to the net of the track
   above; none has a pad or a ring in either metal shot.
7. **A ring on `cdp4_bus_s2`'s diagonal poly at (6012,12480)** (clean shot, in the gap between lines 3
   and 4 of piece `lc9`, just east of line 3's corner (5996,12466); view `l9_s3.png`). Readings: a
   buried contact or a contact; or the clean shot's mark where a gap between two metals crosses a poly
   (guide, trap 2). Assumed the second: no metal is over the spot (the metal shot shows the poly bare in
   the gap) and nothing but the poly is there for a contact to join; so no connection depends on it.
8. **Line 5's identity with `lc2_w8450`** (piece `lc9`). The line is one metal with `lc3`'s
   `lc2_w8907`, the net of the ripple counter's clear gates. That `lc2_w8907` is `lc2_w8450` = NOT
   `lc1_w7170` rests on `lc2`'s uncertain poly and buried contact at (5598-5614, 8897-8916)
   (`trace/lc2.txt`, with its alias). Readings: joined there (then row y 14740 carries the inverse of
   `lc1_w7170` to the bottom-centre logic, and the line is an output of the left-centre strips); or
   not (then the clear's net has no driver in the left-centre strips and may be driven from the
   bottom-centre logic through this line). Working assumption: `lc2`'s. Would settle it: `lc2`'s box
   read in a second shot, or the far end of row y 14740 (`bc1`).
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

**Run 2, piece `ch1`. Round 1: full review** (2026-11-19 14:39 +0100; a fresh Fable 5.2 reviewer agent;
commit 44a0f6d; images in `cache/scratch/busl/review-2/`, 22 used).
Told to suspect: tracks claimed to run through a pad or to end on one, the T at (5800,11880), the near
misses (s3's corners above s2's and s4's pads, the metal that begins south of s4's pad), track identity
through the bends and diagonal steps, s3's pad-to-poly joint and its L beside `cdp3_hw_c3`'s pad, the
three diagonals, s0's poly column under the track x 7511, the staircase steps lying on channel 2's
rows, the rows' identity at x 7600 and row 11922's continuity, the coloured patches.
Checked: every track piece with `tools/tl5_tracks.py` and `tools/follow.py --gap 16` from every pad;
the four through pads (rings symmetric, 15-18 px each side in both chips, metal beyond on both
sides); the T (view and text map: one metal in both chips); every end pad (no metal beyond; s4's pad
has 32 px without metal and open poly before the other metal starts, which has no contact down to
y 12500); the near misses (40, 52 and 30 px apart); s3's L (joined to its pad in both stripped shots,
joined to row 13462, about 12 px clear of `cdp3_hw_c3`'s pad on both sides); the three diagonals
(single, separate, no pads); s0's column (leaves the pad, joins row 13332, ends there, no hole under
the metal); the rows (eight and eight at x 7600 within 3 px of `cdp4`'s, no step; row 11922 continuous
through its pad; the seven array rows to x 4780 and row 12745 without another pad); six contact-hole
candidates from the text scans (none has a ring or pad in the metal shots); the extraction,
`tools/unsure.py`, `tools/padjoin.py` (nothing listed).
Findings, both geometry only, both confirmed:
1. s0's diagonal step was drawn 16 px too far north (y 13900-13943). Tracer's check, the metal test in
   both chips every 10 px (`tools/px.py row Y 5486 5600 6 metal,metal1`): the east track is at
   x 5582-5588 at y 13905, 5564-5576 at 13935, 5540-5552 at 13955; s1's step is as drawn. Redrawn
   y 13916-13959. The two tracks stay 33 px or more apart.
2. Channel 1 also has a metal staircase lying on its rows (x about 6290-6740, y 11878-12138, about
   180 px a step), which the notes named only for channel 2. No pad or ring on any step (reviewer's
   views `ch1w.png`, `ch1e.png`). Now covered by Ambiguity 4.
`tools/t.sh busl sameconn.py 44a0f6d`: `connections identical`.
`.venv/bin/python tools/sameconn.py 44a0f6d`: `connections identical`.
Could not check, or only weakly: the joint of s3's pad to its L is under the pad's metal and rests on
the two stripped shots; the row and staircase crossings were judged at 1.3x in the metal shots and
by text scans, not each at 4x; s0 south of y 15000 was not viewed by the reviewer (the tracer's view
`j6.png`).

Round 1: no findings that change a connection.

**Run 3, piece `lc9`. Round 1: full review** (2026-11-19 16:58 +0100; a fresh Fable 5.2 reviewer agent;
commit 25f8257; images in `cache/scratch/busl/review-3/`, 20 used).
Told to suspect: a swap or bridge in either staircase (read by the tracer at 1.5x; the follower lost
line 4 at its second corner), line 1 beside `cdp4_bus_s4`'s pad (5843,12335) and on its poly, the
greenish and coloured patches at the crossings on the lines and on the rows (twelve places named), the
seven rows from x 6430 to x 7550 (a break, an early end, a change of position, a tapped track; row
y 14914 and the last 150 px most), the end pads (a second poly, a metal running on, the two pad columns
assigned to the wrong lines, the track x 6452), lines 2 and 3 at their corners and past line 1's pad
and row, the ring at (6012,12480).
Checked: both staircases in both metal shots at 2.1-2.5x with the trace, the follower on every line
(ten in, ten out, same order, no bridge); line 4 over the diagonal at 5x in four shots (bars of 15 px
at most); line 1 against s4's pad (about 14 px without metal at y 12354-12368 in both chips, text map
and a 5x view; no ring or hole along the overlap to y 12483); the ring (clean shot only, no metal over
it); a scan of its own of both metal shots for widening on either side of every line (none; it finds
three known pads); the four named crossings on the lines by text map (plain crossings); the end pads at
3.2-3.4x in four shots (one metal from the west, one poly east, field north and south, nothing running
on); lines 2 and 3 (plain corners, clear of line 1's pad, bars only over row 14914); the track x 6452
(no pad); the rows to x 7550 (no field colour on any centre line in the clean shot, edges constant, no
pad on any crossing track, uniform under the wide metals; (6846,14914) at 6x in four shots and
(6665,14567): colour only; (7533,14784): a gap ring); the join with `lc3` at y 10400 (same x within
1 px, metal continuous); the extraction.
Findings, neither changes a connection, both confirmed by the tracer:
1. Line 5's name rests on an uncertain item of `lc2`'s: `tools/unsure.py` lists `lc2_w8450` as two
   pieces, the line on `lc2_w8907`'s (trap 17). Tracer: confirmed (`tools/unsure.py`, the box at
   `trace/lc2.txt` lines 385-387). The notes said "no uncertain item on any of the nine nets" and gave
   the port as driven in `lc2`: both now say what they rest on (Inventory, Logic, Ports, Ambiguity 8).
   Nothing drawn changes: the label stays the net's canonical name.
2. The pads of rows 14827 and 14870 are fed from the north (tracks x 6927, x 6885), not "from the
   south" as the notes said. Tracer: confirmed (`tools/tl5_tracks.py v 6915 14850 15000` and
   `v 6872 14885 15000`: no metal south of either pad; `v 6885 14600 14850`: metal with the rows' bars).
   Notes corrected; neither pad is drawn.
Also reported, outside the piece: `tools/follow.py` going north steps from line 9 onto `rcs_e4` at
(6522-6552,9798) and from line 2 onto line 3 at y 9775, both follower artefacts (25 px of bare ground;
ground bright in chip 2 only), and `lc3_e9798`'s metal arrives at y 9798 from a track x 6514 from the
north (Not done; handoff).
The trace is unchanged since the reviewed commit.
`tools/t.sh busl sameconn.py 25f8257`: `connections identical`.
`.venv/bin/python tools/sameconn.py 25f8257`: `connections identical`.
Could not check, or only weakly: anything east of x 7550; the rows at x 6985-7320 seen only in the
chip-2 metal shot at 2.2x (the other shots by text); the plain staircase and foot corners at 2.1-2.5x,
not 4x; of the eight named row patches three were viewed, the rest covered by the scans.

Round 1: no findings that change a connection.

## Not done

- Everything else in the field: about 30 more tracks and the other rows. Next pieces, in the
  order they join things: (1) `cdp4`'s other lines at x 7600, each of which ends on a pad with a track
  (seen, not drawn): `cdp4_sel1` (y 12223, pad about (6735,12213)), `cdp4_sel2` (12481, pad
  (6735,12470)), `cdp4_sel3` (12530, pad (6690,12515)), `cdp4_sel4` (12788, pad (6735,12775)),
  `cdp4_rst` (12874, pad (7465,12872), track x 7465 south), `cdp4_ld` (12962, pad (7555,12985), track
  x 7556 south), `cdp4_ld8b` (11837, not looked at); the metal L from x 7465 that turns south at
  x 7511 (y 12830; the long track x 7511 from y 8902 to 14284, west along y 13940 to x 7404, to
  y 14284); (2) what else arrives from `lc3` at y 10400 (`ports.d/lc3.txt`): the six diagonal metals at
  x 5915, 5851, 5785, 5722, 5655, 5588 (`lc3_e9577` .. `lc3_e9793`), the polys at x 5475 (`rst_n`) and
  x 5541 (`lc2_w8450` again), the VCC metal x 5340-5390; (3) the top band's ninth row (y 10317,
  `cdp3_gate_f`) and the three poly rows at the top left (y 10560, 10686, 10736); (4) the staircases at
  x 5100-5700, y 10600-10960 west of piece `h8`'s; (5) the bands at y 11850-12150 and below; (6) the
  foot of the field: rows y 14827 and 14870 from their pads (6915,14828), (6872,14868) and those pads'
  tracks north (x 6927, x 6885); the net that starts on row y 14523 at the pad (7100,14522); the rows above y 14523
  (`bc1`'s bus has four more, y 14354-14482); the track x 6452 beside piece `lc9`'s pads.
- Piece `lc9`'s rows east of x 7550: 240-290 px more of each to its pad at x about 7790 or 7835 (the
  pads are listed under the piece), and from there `bc1`'s 13 bus metals east (`bc1` (continue), or
  this package with its region extended to x 7860). Lines 2 and 3 south of y 15000 (`bl0`).
- s0's last 45 px: the track from (5451,15000) to the pad (5365,15042) and the poly row west of it
  (`bl0`, or this package if its region is extended to y 15060).
- The diffusion rows and the poly rows west of x 4780 (`larr` (continue)).
- The northern part (6450-7600 x 6750-10400). Seen from this run: `lc3_e9798`'s metal along y 9798 turns north
  at x about 6515 (`tools/follow.py 6480 9798 E --gap 16`: north on x 6514, seen to y 9532; its end not
  read), 28 px short of `rcs_e4`'s metal x 6552-6564 (`tools/textmap.py 6420 9770 6600 9870 4`: a dark
  edge, bare ground with red 128-160, a dark edge, in both chips: not joined, and the round-3 reviewer's
  view at 5x agrees; `tools/follow.py` at `--gap 16` jumps it going north from (6429,10426), and going
  north from (6126,10426) it steps from line 2 onto line 3 at y 9775, in `lc3`: ground bright in chip 2
  only, guide trap 30).
- `trunks`' two lines in the field: taps not checked (R4).
