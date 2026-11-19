# busl: the left bus field

Queue row `busl` of `notes/work-packages.md` (written busL until 2026-11-19): the wiring between the
left array (`larr`, rows end at x 4780) and the central datapath (`cdp3`, `cdp4`, from x 7600).
Claimed region: x 4780-7550, y 10400-15000 (the main part; the northern part 6450-7600 x 6750-10400
is not started). Coordinates are metal-shot pixels; images are in `cache/scratch/busl/`. Wiring only:
no transistor has been found in the field so far. Seven pieces are drawn: `h8`, `ch1`, `lc9`, `ctl`, `d6`, `sr`, `kb`.
Pieces `d6`, `sr` and `kb` begin in the northern part (x 7180-7600, y 8795-10400), drawn there as far
as their pads or, for `sr`, the end of `eofw`'s metal; nothing else of the northern part is.

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

Run 4 (richtw1's session, Claude Fable 5.2; 2026-11-19 17:02 to 17:20 +0100). One piece, `ctl`, wiring
only, one uncertain item (a metal over a box):

- **`cdp4`'s six control rows are followed across the field** (piece `ctl`). Each of the poly rows
  `cdp4_sel1` .. `cdp4_sel4` (the selector's four select lines), `cdp4_rst` (the gate line of the
  pull-downs on the selector nodes) and `cdp4_ld` (the strobe of the 8-bit latch row C) runs west from
  x 7600 to a pad with a metal track.
  - **The four selects come from the south.** Their tracks step west in one nested staircase
    (y 13073-13204) and run on south out of the region at (6538,15000), (6581,15000), (6624,15000),
    (6668,15000) (the follower runs each to y about 16150-16190, in `bl0`'s ground). On the way each
    runs through one more pad, the west end of a poly row that goes back east to the gate group at the
    bottom-left corner of `cdp4` (x 7560-7650, y 13650-14030, not drawn): `cdp4_sel1` on the row
    y 13701, `cdp4_sel3` on 13809, `cdp4_sel4` on 13961, `cdp4_sel2` on 14004. So each select is also
    an input of that group.
  - **`cdp4_rst` ends on that group.** Its track (x 7468) ends on a pad (7467,13897); a poly from the
    pad runs 70 px east, under one track, to a heavy-outlined box (7535-7580, 13903-13940) at the
    group's west edge, read as a buried contact onto the group's node diffusion (not drawn: Ambiguity 9).
    Believed: the group drives `cdp4_rst`, from the four selects among other inputs.
  - **`cdp4_ld` is `bc1_ld_a`**, the twin output of the bottom-centre strobe driver (`bc1`: `bc1_ld_a`
    = NOT `bc1_ld_n`, the same NAND as row D's strobe `cdp4_ld6`). Its track (x 7556) passes over the
    same box, where neither metal shot shows it for 51 px (drawn `?M`, guide trap 27), comes out
    south of it, turns west along y 13982 to x 7448 and runs south onto `bc1`'s metal at (7448,14050).
    The two names are gathered by `@alias bc1_ld_a cdp4_ld`; `tools/unsure.py` lists the net as two
    pieces without the uncertain item.

Run 5 (richtw1's session, Claude Fable 5.2; 2026-11-19, after the run-4 handoff of 17:42 +0100). One
piece, `d6`, wiring only, no uncertain items:

- **The six data lines of `cdp4`'s 6-bit latch row D are the six "line g" rows of `cdp3`'s row A
  cells** (piece `d6`). Each poly row `cdp3_g_c#` (# = 2..7; x 7600, y 9123 .. 8907: `cdp3` follows it
  east to a contact on line g, which comes down from the large cell of row A in column c#) ends west on
  a pad of a staircase (x 7336 .. 7553). The pad's metal track runs south, steps 86 px west
  (y 9190 .. 9407), runs 4,300 px down the east side of the field with no pad or contact, steps 65 px
  west in a second staircase (y 13722 .. 13938) and becomes the metal that `bc1` draws from y 14040
  onto the contact of one of its six poly lines (y 14089 .. 14304). The order is kept: c2 goes to line 1
  (the foot of `cdp4_in6_s1`), c3 to line 2 (`cdp4_in6_s2`), c4 .. c7 to lines 3 .. 6 (`bc1_d3` ..
  `bc1_d6`, which `bc1` follows east only to x 8040; believed `cdp4_in6_s3` .. `s6`). Line 6 (c7) is the
  long track that the earlier runs met at x 7468 / 7511. The names are gathered by `@alias`
  (`cdp3_g_c#` canonical).

Run 6 (richtw1's session, Claude Fable 5.2; 2026-11-19 18:06 to 18:20 +0100). Two pieces, `sr` and `kb`,
wiring only, no uncertain items:

- **`tc2_sr_g` runs down the whole field** (piece `sr`). The metal that `eofw` left as an open end south
  of its corner pad (7446,8732) (net `tc2_sr_g` = `lc1_w7908`, the enable of latch D, = `eof_w7718`,
  row 2 of the gate on `inh_ck`'s tap row) is one metal from there to the south edge of the region:
  south to y 8910, a diagonal south-west (the south-east line of the diagonal bundle) to (7209,9168),
  4,500 px south at x 7209 (the track west of piece `d6`'s line 1), the seventh step of the lower
  staircase (west along y 13680 to x 7145), three more jogs (y 14176, 14285, 14588) and out at
  (7187,15000). No pad or contact on the way. It runs on in `bc1`'s ground (seen at 1x, not drawn):
  south to y 15482, west to x 7103, south; the follower ends at (7100,16279).
- **`cdp3_k_b` comes from a diffusion at the foot of `cdp3`'s column 0** (piece `kb`). The poly row
  y 9450 (`cdp3`: the input of gate 1 of the NAND beside its row C) ends west of x 7600 on a pad
  (7554,9450); the pad's metal track runs 1,670 px south at x 7555 with no pad or contact and ends on a
  contact (7555,11118) on a diffusion pad, from which a diffusion band (y 11100-11127) runs east under
  column 0's VSS rail into `cdp3`'s ground (drawn to x 7600).
- Looked at and not this package's: **`cdp4_ld8b`'s row y 11837 does not enter the field**: west of
  x 7598 there is bare field at that height in both metal shots and the clean shot (view `b_ends.png`,
  3x); the row's west end is at about x 7603-7640 under `cdp4`'s metal x 7600-7645 (`cdp4` (continue)).

Full extraction with run 6: 2,390 nets (unchanged: the two wires lengthen `eofw`'s and `cdp3`'s nets),
4,345 transistors, 0 errors, 0 warnings. The package by itself: 39 nets, 0 errors, 0 warnings.

Full extraction with run 5: 2,391 nets (six fewer: the six joins), 4,345 transistors, 0 errors,
0 warnings. The package by itself: 37 nets, 0 errors, 0 warnings.

Full extraction with run 4: 2,398 nets (one fewer: `cdp4_ld` and `bc1_ld_a`), 4,345 transistors,
0 errors, 0 warnings; 847 of 1,276 equations firm, as before. The package by itself: 31 nets, 0 errors,
0 warnings.

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

Piece `ctl` (pad contacts with `tools/busl_padc.py` in both metal shots; row centres with
`tools/busl_rowy.py` in open columns; tracks with `tools/follow.py --gap 16` and `tools/sel_cut.py`;
metals 13-16 px wide, drawn 14; every row is poly, 23-24 px between its edge lines):

| Net | Row at x 7600 (y) | Pad at its west end | Track | Second pad, and its row east to x 7550 | Leaves |
|---|---|---|---|---|---|
| `cdp4_sel1` | 12225 | (6732,12226) | arm west along y 12228 to x 6602; south; west along y 13073 to x 6538; south | (6537,13701): row y 13701 | south, (6538,15000) |
| `cdp4_sel2` | 12485 | (6732,12485) | arm west along y 12488 to x 6646; south; west along y 13116 to x 6581; south | (6580,14004): row y 14004 | south, (6581,15000) |
| `cdp4_sel3` | 12528 | (6687,12528) | x 6689 south; west along y 13160 to x 6624; south | (6623,13809): row y 13809 | south, (6624,15000) |
| `cdp4_sel4` | 12788 | (6731,12788) | x 6733 south; west along y 13204 to x 6668; south | (6666,13961): row y 13961 | south, (6668,15000) |
| `cdp4_rst` | 12874 | (7467,12875) | x 7468 south to a pad (7467,13897) | from that pad a poly 20 px wide east along y 13916 to x 7532 | on the box (7535-7580, 13903-13940) |
| `cdp4_ld` | 12962 | (7556,12983), below the row's end | x 7556 south; over the box y 13899-13949 (`?M`); south to y 13982; west to x 7448; south | none | onto `bc1`'s metal of `bc1_ld_a` at (7448,14050) |

- The six row-end pads (views `n8_selpads.png`, `n9_rstld.png`, 3.2-3.4x, three shots): each a widened
  poly pad with a green hole in the clean shot and a ring with a bright centre in the metal shot; the
  metal leaves west (sel1, sel2) or south (sel3, sel4, rst, ld), the poly east. `cdp4_ld`'s pad hangs
  below the row's west end (the row enters its top right corner); 15 px north of it is the pad
  (7554,12919) of `cdp4_bus_s0`, whose track ends there: `tools/follow.py 7556 13050 N` ends at y 12980.
- A long track of another net (not drawn; Not done) comes down x 7468 from the north, turns east at
  y 12835 just above `cdp4_rst`'s pad and goes on south along x 7511. It is not on the pad:
  `tools/textmap.py 7444 12816 7500 12884 3`: the corner's metal ends at y 12842, then open ground in
  the clean shot for 12 px (y 12849-12858, both metal shots at ground level), then the pad's ring.
- Another net's metal corner at about (7430,13897) (a step of the staircase of `cdp4`'s row D data
  lines) lies 10-16 px west of `cdp4_rst`'s south pad: separated by ground (round-4 reviewer, 4x).
- The nested staircase (view `n10_stair.png`, 2.4x, metal and clean shots; overlay `ct_o1.png`): six
  tracks step west one after another, the two westernmost of other nets (x 6516 at y about 12995,
  x 6559 at 13033), then sel1, sel2, sel3, sel4; plain right-angle steps over field, nothing beneath.
  Each track was followed through its step by itself (`tools/follow.py`); `tools/sel_cut.py h` gives
  6603/6646/6689 at y 12700 and 6538/6580/6624/6668 at y 13300.
- **Every select track runs on through its second pad** (view `n7_pads.png`, 4x, both metal shots and
  the clean shot: a ring with a bright centre on a widened row-end pad, the track at full width above
  and below). `tools/follow.py` stops at each ring; `tools/tl5_tracks.py v X 13230 14100` shows the
  ring's two dark stretches (14-17 px) and metal on both sides; `tools/follow.py 6580 14062 S` and
  `6538 13780 S` run to y 16192 and 16150. Guide, trap 32.
- No other pad on a track: `tools/tl5_tracks.py v` down each select track from y 13230 to 15000, down
  x 7468 (y 12890-13885) and x 7556 (y 12995-13900): only the 8-13 px bars of the rows crossed (channel
  2's eight rows, the rows y 13701-14004, `bc1`'s six lines y 14089-14304, the rows y 14354-14914).
  The south boundary: view `ct_o5.png` (3.2x): four plain tracks across y 15000.
- The four rows east of their pads (views `n6_rows.png`, overlay `ct_o2.png`, 1.14x; `ct_stair.png`,
  3.1x): straight, the same y within 1 px at x 6690, 7080, 7210 and 7534, under about twenty tracks
  each, no pad on any. Two more rows of other nets lie between them (y 13744 and y 13852, both from
  west of x 6500; not drawn). A metal staircase (the six data lines of `cdp4`'s row D on their way to
  `bc1`'s lines y 14089-14304; not drawn) crosses the band, and **one of its steps lies on
  `cdp4_sel3`'s row y 13809 for 80 px** (x 7267-7347; the other steps lie between rows or on row
  y 13852): no pad, no ring, the clean shot's row unbroken under it (tile 5 of `ct_c1.png`, 3.6x, four
  shots): no contact (Ambiguity 4).
- `tools/tl5_tracks.py h` along the ten row stretches lists greenish stretches in the clean shot
  (thirty-odd; the longest (6669,13701), (6712,13701), (7061,13809), (6712,14004)): tiles at 3.6x in
  four shots (`ct_c1.png`): they are the row's open stretches between two tracks, olive in the clean
  shot; every track crosses at its own width in both metal shots (Ambiguity 5).
- At x 7550 (view `n11_east.png`, 4x): the four rows run on under the track x 7556 to the gate group's
  diffusion column under the wide metal x 7598-7650, where each is a gate band: sel1's row steps 12 px
  north at x 7548 (band y 13677-13698), sel3's continues (13792-13812), sel4's and sel2's continue
  (`n5_ldsouth.png`). The wide metal has contacts onto the column at (7607,13718) and (7607,13838).
  Rows y 13744 and y 13852 end there too (y 13852 steps south to a band y 13862-13882).
- **`cdp4_rst`'s south end** (views `n3_rstld.png` 3.6x, `ct_o4.png` 3.3x): the pad (7467,13897) has a
  ring with a bright centre in both metal shots and a green hole in the clean shot
  (`tools/textmap.py 7438 13860 7500 13930 3`); the poly leaves its lower edge east as a band
  y 13906-13927, passes under the track x 7511 (the metal bright throughout, one edge bar each side:
  no contact) and ends on the west outline of the box at x about 7532.
- **The box (7535-7580, 13903-13940) and `cdp4_ld`'s track over it** (`tools/textmap.py 7526 13890
  7590 13955 3`, against the known through pad (5713,12443) and `cdp4_rst`'s pad in the same form;
  `tools/tl5_tracks.py v 7556 13860 13990`): neither metal shot shows metal for 51 px (y 13898-13949);
  no bright centre in either (chip 2 reaches ground level at one spot west of the track's line, chip 1
  at one spot on it, (7557,13929): Ambiguity 9); the clean shot shows a heavy outline with a plain tan inside and no green hole, in
  protected colours (so metal was over it). The track is at full brightness to y 13897 and again from
  y 13949, where it runs on to the corner (7556,13982) (`tools/follow.py 7556 13960 S`: west to
  x 7442; `7452 14040 N`: the same piece from the other end). The arm y 13975-13989 lies over field
  between the rows y 13961 and y 14004; the track x 7448 crosses row y 14004 without a pad
  (`ct_o4.png`). `bc1` draws the same metal from (7448,14050) south (`trace/bc1.txt` line 214).

Piece `d6` (pad contacts with `tools/busl_padc.py` in both metal shots; row centres with
`tools/busl_rowy.py 7578 8880 9145` in the open column east of the last track; arm heights with
`tools/sel_cut.py v` between the tracks; track centres with `tools/sel_cut.py h` at fifteen heights;
metals 13-17 px wide, drawn 14; every row is poly, 22-25 px between its edge lines):

| Line | Net | Row at x 7600 (y) | Pad at its west end | Track from the pad | Step west at y | Long run x | Lower step west at y | Lower x, onto `bc1`'s metal at y 14040-14050 | `bc1`'s line and contact |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `cdp3_g_c2` | 9123 | (7336,9122) | 7338 | 9190 | 7252 | 13722 | 7189 | line 1, y 14089, (7188,14091): the foot of `cdp4_in6_s1` |
| 2 | `cdp3_g_c3` | 9080 | (7380,9080) | 7382 | 9234 | 7296 | 13766 | 7231 | line 2, y 14132, (7230,14131): the foot of `cdp4_in6_s2` |
| 3 | `cdp3_g_c4` | 9036 | (7423,9036) | 7426 | 9276 | 7339 | 13810 | 7274 | line 3, y 14175, (7274,14172): `bc1_d3` |
| 4 | `cdp3_g_c5` | 8993 | (7467,8994) | 7468 | 9320 | 7382 | 13855 | 7317 | line 4, y 14218, (7317,14217): `bc1_d4` |
| 5 | `cdp3_g_c6` | 8949 | (7510,8950) | 7512 | 9363 | 7426 | 13898 | 7360 | line 5, y 14261, (7361,14260): `bc1_d5` |
| 6 | `cdp3_g_c7` | 8906 | (7553,8905) | 7556 | 9407 | 7468 to y 12835; east to 7512; south | 13938 | 7404 | line 6, y 14304, (7405,14304): `bc1_d6` |

- The north end (view `d6_north_m.png`, 2.3x, chip-2 metal shot with every package's trace; overlay
  `d6_o1.png`, 1.65x, metal and clean shots): six pads in a staircase, 43 px apart both ways, each a
  ring with a bright centre on the widened west end of its row; one metal leaves each pad south; the
  rows run east under the tracks of the lines north of them (plain crossings: `tools/tl5_tracks.py v`
  down the six upper tracks shows only 8-13 px edge bars) to x 7600, where `trace/cdp3.txt` draws them
  on (lines 215-235; its y within 1 px of these). The six upper arms are plain right-angle steps over
  field. North-west of the pads lies the diagonal bundle (not this piece).
- The long runs: `tools/sel_cut.py h` gives 7252, 7296, 7339, 7382, 7426, 7468 at y 9450, 9800, 10400,
  11000, 11600, 12700 (no step). `tools/tl5_tracks.py v` down all nineteen vertical segments
  (`cache/scratch/busl/d6_scan.txt`): no stretch of 18 px or more without metal in both chips; only
  the 8-16 px edge bars of the rows crossed (`lc3`'s
  rows y 9561-9814, two rows y 10041-10072, the top band y 10300-10680, channel 1, the rows
  y 12210-12241, 12469-12543 and 12728-12804, channel 2, the rows y 13685-13870). `tools/tl5_tracks.py
  h` along all thirteen arms: no gap, no hole.
- No pad or contact on the way. `tools/follow.py`'s contact candidates and the scan's greenish
  stretches of the clean shot, as tiles at 3.4x in three or four shots (`d6_c1.png`, `d6_c3.png`):
  (7382,11275), (7252,12579), (7253,10992), (7295,10986), (7338,9382), (7427,11596) are spots at the
  edge of a plain track over field (nothing beneath to tap); (7296,10057), (7382,9666), (7426,9667),
  (7468,9709), (7467,9699), (7512,13600) are plain crossings of a poly row, the track at its own
  width, no ring. The six tracks cross `cdp4_bus_s1`'s poly row y 12745 without a pad (`d6_c2.png`,
  4x, both metal shots and the clean shot).
- Line 6's corner at y 12835 (x 7468 to 7512) ends 16 px above `cdp4_rst`'s north pad, with open
  ground between (piece `ctl`'s text map); from there the track lies over `cdp4_bus_s0`'s poly column
  (y 12920-13332) and crosses `cdp4_rst`'s poly (y 13906-13927), without a contact on either
  (`tools/tl5_tracks.py v 7512 12845 13930`: edge bars only).
- The lower staircase (view `d6_stair_m.png`, 3.6x, chip-2 metal shot; overlay `d6_o2.png`, 1.85x,
  metal and clean shots): six right-angle steps, each arm 65 px long; no track goes on south of its
  arm and no lower track north of it. A seventh track west of them (x 7210, stepping along y 13678 to
  x 7142; another net, not drawn) has the same shape. Line 3's arm lies on `cdp4_sel3`'s row y 13809
  and line 4's on the undrawn row y 13852, each for 80 px (Ambiguity 4). Line 5's corner (7426,13898)
  is 20 px west of `cdp4_rst`'s south pad: `tools/px.py row 13898 7424 7470 3 metal,metal1,acid1b`:
  metal to x 7431, a dark edge, bare ground at x 7442-7449 (red 124-156 in both chips, the clean shot
  green 120/159/82), the pad's ring from x 7451.
- Chip 2 alone shows dark notches on the metal at (7366,13853), (7512,13066-13076) and
  (7512,13270-13282) (round-5 reviewer; `tools/px.py pt 7366,13853 7512,13071 7512,13276 7512,13150
  all`: chip-2 metal 116/76/22, 43/22/16, 72/40/29 against 164/115/62 on the plain track; chip-1 metal
  157/115/31, 211/148/97, 184/140/82; the clean shot protected, 216-218/160-166/112-121, no hole):
  marks on chip 2's metal, not contacts. In the clean shot the row-end pads of lines 1 and 2 are
  stained red (142/40/28, 139/40/27 at the contact) and show no green hole; their contacts rest on the
  ring and bright centre in both metal shots (`tools/busl_padc.py`: red 225/179 and 220/212) and, for
  pad 1, the hole in the chip-2 stripped shot.
- The south ends (view `d6_o3.png`, 3x, chip-2 metal shot with every package's trace): each track
  ends on the pad of its own line of `bc1`'s, in a staircase; `tools/tl5_tracks.py v` from each pad on
  south: no metal in either chip for 60 px or more beyond any of the six. Line 1's track is dark for
  20 px (y 14067-14087) just north of its contact, the others for 15-19 px: the pad's ring with the
  row's north edge. Another metal turns south at about (7187,14165), 70 px below line 1's pad
  (`tools/textmap.py 7160 14080 7216 14180 4`: no metal between them in either chip): not joined.

Piece `sr` (the line with `tools/follow.py --gap 16`, in stages (`--max 60` .. `900`) through the
diagonal; track centres with `tools/sel_cut.py h` at twenty heights and arm heights with `sel_cut.py v`;
one metal 13-18 px wide, drawn 14):

| Stretch | From | To | What it passes |
|---|---|---|---|
| `eofw`'s metal | the corner pad (7446,8732) | (7466,8800) | drawn in `trace/eofw.txt` (`M 7466,8745 y8800`) |
| south, x 7467 | y 8795 | y 8910 | the poly y 8850-8875 that leaves the pad (7425,8862) east (edge bars y 8846-8855, 8870-8878) |
| diagonal, x + y = 16377 | (7467,8910) | (7209,9168) | field; 57 px north-west of piece `d6`'s row-end pads |
| south, x 7209 | y 9168 | y 13680 | `lc3`'s rows y 9561-9814, the rows y 10041-10072, the top band, channel 1, the bands y 12210-12241, 12469-12543, 12728-12804, channel 2 |
| west, y 13680 | x 7209 | x 7145 | field (between channel 2's last row and row y 13701) |
| south, x 7145 | y 13680 | y 14176 | rows y 13701 (`cdp4_sel1`), 13744, 13809 (`cdp4_sel3`), 13852, 13961, 14004, `bc1`'s lines 1 and 2 (y 14089, 14132) |
| east, y 14176 | x 7145 | x 7187 | lies on `bc1`'s line 3 (the poly row y 14175, `cdp3_g_c4`) for 45 px |
| south, x 7187 | y 14176 | y 14285 | `bc1`'s lines 4 and 5 (y 14218, 14261) |
| east, y 14285 | x 7187 | x 7231 | between line 5 and line 6 (y 14304) |
| south, x 7231 | y 14285 | y 14588 | line 6 and the rows y 14354-14567 |
| west, y 14588 | x 7231 | x 7187 | between the rows y 14567 and 14611 |
| south, x 7187 | y 14588 | y 15000 | the rows y 14611-14914 (piece `lc9`'s) |

- The north end (view `sr_n1.png`, 2.5x, chip-2 metal shot with every package's trace; overlay
  `sr_o1.png`, 1.9x): the metal comes south from `eofw`'s corner pad at its own width, crosses the poly
  that runs east from another line's pad (7425,8862) (two edge bars, the metal bright between them; no
  ring) and turns into the diagonal at y 8910. Three more diagonals lie north-west of it (other nets;
  one ends on that pad). The diagonal is plain, over field, and turns south at (7209,9168), 45 px west
  of `d6`'s line 1 (x 7252).
- The long run: `tools/sel_cut.py h` gives 7208-7210 at y 9250, 9450, 9800, 10400, 11000, 11600, 12200,
  12700, 13300, 13600 (no step). `tools/tl5_tracks.py v` and `h` on all ten straight segments
  (`cache/scratch/busl/sr_scan.txt`): edge bars of 8-13 px at every row crossed, and four longer
  stretches, each looked at as a tile at 4x in both metal shots and the clean shot (`sr_c1.png`,
  `sr_c2.png`): (7209,9176-9243), chip 1 only, a dirt blob on chip 1's metal (chip 2 plain);
  (7231,14373-14394), chip 1 only, dirt rings wider than the track (chip 2 plain); (7187,14678-14694),
  17 px, the north edge of row y 14697 with a red spot on chip 1; and **(7145,13728-13749), 22 px
  without metal in both chips, on the poly row y 13744: Ambiguity 13**.
- The follower's contact candidates: (7207,9579), where the track crosses `lc3_e9577`'s poly row (the
  clean shot olive under the track for 7 px, gap rings at x 7232; the metal at its own width in both
  metal shots, no ring: guide, trap 15); (7208,12618), a green spot at the track's west edge over field
  (nothing beneath).
- The seventh step and the three jogs (views `sr_s1.png`, `sr_s2.png`, 2.9x, both metal shots and the
  clean shot; overlay `sr_o2.png`, 1.4x): right-angle corners, the metal continuous round each in both
  chips. `tools/follow.py 7188 14215 N` and `S` and `7186 14630 N` and `S` each run to the next corner
  both ways. The arm y 14176 lies on `bc1`'s line 3 between x 7145 and 7187: no pad, no ring, the clean
  shot's row plain under it (`tools/tl5_tracks.py h 14176 7150 7182`: no gap, no hole): no contact
  (Ambiguity 4). `d6`'s line 1 ends on its pad (7188,14091) 70 px north of the corner (7187,14176):
  bare ground between (piece `d6`'s text map). Another net's track at x 7143 (from an arm y 14390 to a
  pad (7143,14480)) begins 200 px south of the corner (7145,14176): rows only between them.
- South of y 15000 (view `sr_s3.png`, 1.03x, metal and clean shots; not drawn): the track runs on at
  x 7186 over `tla`'s poly (y 15334-15444) to a corner (7186,15482), west to x 7103 and south between
  the pads and gates of `bc1`'s group; `tools/follow.py 7186 14630 S` ends at (7100,16279) with contact
  candidates at (7100,15596-15660). None of it has been read.

Piece `kb` (pad contacts with `tools/busl_padc.py` in both metal shots; the row with
`tools/busl_rowy.py 7585 9410 9480`; the track with `tools/follow.py --gap 16` both ways and
`tools/sel_cut.py h` at six heights (7554-7556); metal 13 px wide, drawn 14):

| Net | Row at x 7600 (y) | Pad at its west end | Track | South end |
|---|---|---|---|---|
| `cdp3_k_b` | 9449 (poly, 24 px between its edge lines) | (7554,9450) | x 7555 south, 1,670 px | contact (7555,11118) on a diffusion pad (7538-7584, 11096-11144); a diffusion band y 11100-11127 east to x 7600 and on under the VSS rail |

- The north pad (view `b_ends.png`, tile 1, 3x, both metal shots and the clean shot): a ring with a
  bright centre on the widened west end of the row; field west of it; no metal north of it
  (`tools/follow.py 7555 9600 N` ends at y 9446; the upper arm of `d6`'s line 6 passes 25 px north, with
  open ground between: piece `d6`'s review). `trace/cdp3.txt` draws the row from x 7600 at y 9450.
- The track: `tools/tl5_tracks.py v 7555 9470 11095`: only the 8-12 px edge bars of the rows crossed
  (`lc3`'s rows y 9561-9814, y 10041-10072, the top band y 10298-10680); one stretch where chip 2 alone
  fails (y 10897-10916) and one greenish in the clean shot (y 10877): tiles at 4x (`b_c1.png`): dark
  specks on chip 2's metal over plain field, chip 1 plain; and the follower's candidate (7554,10070), a
  plain crossing of the poly row y 10056.
- The south end (views `b_s1.png` 3.2x, `kb_o1.png` 4x, chip-2 metal shot and clean shot): the track
  ends on a pad with a ring and a bright centre in both metal shots and a black pit in the clean shot
  at (7555,11113); no metal south of it (`tools/follow.py 7555 9600 S` ends at y 11126). The pad is
  plain tan inside a heavy outline in the clean shot (`tools/px.py row 11112 7520 7605 5`:
  193-197/164-176/115-126 under the pad's metal, red minus green 20-29, against 215/160/113 for poly
  under a track): **diffusion**, not poly. East of the pad a band between two edge lines (y 11095 and
  11128; `tools/busl_rowy.py 7590 11090 11170`) runs to the VSS rail and is the same tan under the
  rail's edge (194/176/122 at x 7595-7605). The dark bar across it at x 7585 in the clean shot is not
  in either chip-2 shot (metal 160-168, stripped 121-153 at x 7580-7585): the mark of the gap between
  the pad's metal and the rail (guide, trap 2). Ambiguity 14.

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

Piece `ctl`. Traced: `cdp4_sel1` .. `cdp4_sel4` each reach, on one metal track from the south,
both the selector's gate row in `cdp4` and one poly row into the gate group at `cdp4`'s bottom-left
corner (no uncertain item on any of the four). `cdp4_rst` runs from its gate row to a poly that ends on
a box of that group (no uncertain item on what is drawn; the box itself is not drawn). **`cdp4_ld` =
`bc1_ld_a` = NOT `bc1_ld_n` = `bc1_ld_in1` AND `bc1_ld_in2`**: the 8-bit latch row C and the 6-bit
latch row D (`cdp4_ld6`, the same NAND through a second inverter) are loaded by the same event. That
join is **marked**: it rests on the `?M` over the box (51 px where the photos do not show the metal)
and on the reading that the box makes no contact with the metal (Ambiguity 9). Nothing in the field
drives or loads any of the six. Not traced: what drives the four selects (south of y 15000); the gate
group (`cdp4` (continue)). Believed: the group makes `cdp4_rst` from the selects (a gate band of each
select lies on its diffusion column, and `cdp4_rst`'s poly is tied to a node of that column), so that
the selector's nodes are pulled low when no select is high; and rows C and D together are one 14-bit
register loaded from the selector's bus lines.

Piece `d6`. Traced (no uncertain item on any of the six nets): `cdp3_g_c2` .. `cdp3_g_c7`, the lines
that `cdp3` follows from a contact on line g of each row A cell west to x 7600, are one metal each from
their row-end pads to `bc1`'s six row D data lines. So in the extraction **the data input of `cdp4`'s
row D latch bit under slice s1 (the pass transistor gated by `cdp4_ld6`) is `cdp3_g_c2`, and under s2
`cdp3_g_c3`**; `cdp3_g_c4` .. `c7` are `bc1_d3` .. `bc1_d6`, which `bc1` draws only as far as x 8040.
Believed: these run on to `cdp4_in6_s3` .. `s6` in the same order, so that the 6-bit latch row D takes
line g of the six large cells of `cdp3`'s row A, column c(k+1) into the bit under slice sk. Nothing in
the field drives or loads the six. Not traced: the row A cells (`cdp3` (continue), `cdp2` (continue)),
so what line g is; a latch's data input does not drive, so the cells must (believed).

Piece `sr`. Traced (no uncertain item of this package; the net's other joins are `eofw`'s): `tc2_sr_g`,
which is also `lc1_w7908` (the enable of latch D, the latch that makes `lc_step`) and row 2 of the gate
`tc2_r5589` = NOT(`lc1_w7170` AND (`inh_ck` OR `tc2_sr_g`)), runs from `eofw`'s corner pad down the
field and out at (7187,15000), with no contact in the field. So the net has a third branch, into the
bottom-centre logic. Not traced: its end (in `bc1`'s group x 7000-7860, y 15000-16300). Believed: the
driver of `tc2_sr_g`, which no package has found, is there (the net's three drawn ends, `tc2`'s latch,
`eof`'s gate and latch D's enable, are all gates). The reading rests on Ambiguity 13 (no contact
where the track crosses row y 13744).

Piece `kb`. Traced (no uncertain item): `cdp3_k_b`, gate 1 of the NAND beside `cdp3`'s row C, is one
net with a diffusion pad at (7555,11118) and the band east of it. Not traced: what that diffusion is
(a source or drain under or east of column 0's VSS rail, `cdp3` (continue)); it is the only drawn end of
the net that can drive it.

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
| `cdp4_sel1`, `cdp4_sel2`, `cdp4_sel3`, `cdp4_sel4` | P | x 7600, y 12225, 12485, 12528, 12788 (23 px wide) | in (driven from south of y 15000) | `cdp4`'s select rows, drawn there from x 7600 |
| `cdp4_sel1`, `cdp4_sel3`, `cdp4_sel4`, `cdp4_sel2` | P | x 7550, y 13701, 13809, 13961, 14004 (24 px wide) | in | poly rows on east 40-100 px to gate bands on the diffusion column of `cdp4`'s corner gate group (not drawn; sel1's steps 12 px north at x 7548) |
| `cdp4_sel1`, `cdp4_sel2`, `cdp4_sel3`, `cdp4_sel4` | M | y 15000, x 6538, 6581, 6624, 6668 (14 px wide) | in | tracks on south into `bl0`'s ground (followed to y about 16150-16190) |
| `cdp4_rst` | P | x 7600, y 12874 (22 px wide) | not known (believed in: driven by the corner gate group) | `cdp4`'s row, drawn there from x 7600 |
| `cdp4_rst` | P | (7532, 13906-13927) | not known | the poly ends on the west outline of the box (7535-7580, 13903-13940), not drawn (Ambiguity 9) |
| `bc1_ld_a` (`cdp4`'s name: `cdp4_ld`) | P | x 7600, y 12962 (22 px wide) | in (driven in `bc1`, through the `?M`) | `cdp4`'s strobe row of latch row C, drawn there from x 7600 |
| `bc1_ld_a` | M | (7448,14050), 14 px wide | in | joins `bc1`'s metal of the strobe driver's twin output |
| `cdp3_g_c2` .. `cdp3_g_c7` | P | x 7600, y 9123, 9080, 9036, 8993, 8949, 8906 (23 px wide) | not known (believed in: driven by `cdp3`'s row A cells) | `cdp3`'s channel B tracks onto line g, drawn there from x 7600 |
| `cdp3_g_c2` .. `cdp3_g_c7` | M | y 14050, x 7189, 7231, 7274, 7317, 7360, 7404 (14 px wide) | as above | each joins `bc1`'s metal (drawn there from y 14040) onto the contact of its line 1 .. 6 (`cdp4_in6_s1`, `cdp4_in6_s2`, `bc1_d3` .. `bc1_d6`) |
| `tc2_sr_g` | M | (7460-7474,8795), 14 px wide | not known | onto `eofw`'s metal south of the corner pad (7446,8732) (`M 7466,8745 y8800`; `eofw`'s port there is named `lc1_w7908`, an alias) |
| `tc2_sr_g` | M | (7180-7194,15000), 14 px wide | not known (believed in: driven in `bc1`'s group) | the track goes on south in `bc1`'s ground: to y 15482, west to x 7103, south; the follower ends at (7100,16279) (not read) |
| `cdp3_k_b` | P | x 7600, y 9438-9460 (22 px wide) | out (driven from the diffusion at its south end; received by `cdp3`'s gate 1) | `cdp3`'s row y 9450, drawn there from x 7600 |
| `cdp3_k_b` | D | x 7600, y 11100-11127 | in | the diffusion band goes on east under column 0's VSS rail (x 7600-7646) into `cdp3`'s ground (not drawn) |

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
   `lc2_x6299`, after its second step; one step of the staircase x 7130-7440, 80 px on `cdp4_sel3`'s row y 13809 at x 7267-7347, piece `ctl`: it is line 3 of piece `d6`, `cdp3_g_c4`; line 4's arm, `cdp3_g_c5`, lies the same way on the undrawn row y 13852 at x 7310-7390). Readings: a contact somewhere
   along the overlap; or none. Assumed none: no pad, no ring, no green hole in the clean shot on any
   (measurements under piece `ch1` above; guide, trap 13). A contact would join one of these eight
   nets to another track's net.
5. **Red and yellowish patches on the poly rows and diagonals in the clean shot** (channel 2 at
   x 6600-6900, the diagonals at (5700,12610), (6250,12250)): as Ambiguity 1, colour only; the chip-2
   shots show nothing there. The same on piece `lc9`'s seven rows at x 6450-6900 (red, dark and
   green patches one track wide; the eight strongest are listed under the piece) and, greenish, where
   its tracks cross `cdp3_hw_c5`'s row y 10447 (five tracks in a row: a tap on each would short five
   nets to one register bit). A contact on any would join one of the nine nets to the net of the track
   above; none has a pad or a ring in either metal shot. The same on piece `ctl`'s rows (the open
   stretches between tracks are olive in the clean shot; the longest are listed under the piece).
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
9. **The box at (7535-7580, 13903-13940)** (piece `ctl`; at the west edge of `cdp4`'s corner gate
   group, half outside this package's region). `cdp4_rst`'s poly ends on its west outline and
   `cdp4_ld`'s metal passes over its middle. Readings: (a) a buried contact joining `cdp4_rst`'s poly
   to the group's node diffusion (the tan area east of it, between the gate bands y 13862-13882 and
   y 13949-13973), the metal passing over without contact; (b) a poly pad with a metal contact, which
   would make `cdp4_rst` and `cdp4_ld` one net (the poly then a cross-under beneath the track x 7511);
   (c) a metal contact onto that diffusion, which would put the strobe on the group's node. Working
   assumption: (a). For it: the box has a heavy outline and a plain inside, unlike the pad at the
   other end of the same poly 90 px west (widened, green hole, ring with a bright centre: a contact);
   no bright centre in either metal shot and no green hole in the clean shot (guide, traps 22, 26); a
   metal is dark for 35-80 px over such a box. Against: one spot of 9 x 10 px on the track's line at
   (7557,13929), found by the round-4 reviewer (`tools/px.py pt 7557,13929 all`: chip-1 metal
   140/122/62, the brightness of bare ground there and well under the track's 160-190; chip-2 metal
   97/89/51, dark; chip-2 stripped shot 136/154/83, greenish like the ghosts of this piece's real
   contacts; clean shot 196/169/118, not green). It has no ring of its own, is not bright in chip 2
   and sits off-centre in the dark stretch, so it is not a contact by the usual tests; `tl3`'s node
   boxes under its thin metal show brighter spots than this (guide, trap 26). A pass-over cannot be
   told from these photos with certainty, which is why the stretch is `?M`. The box and the diffusion are not
   drawn here: they are the gate group's (`cdp4` (continue)), whose tracing settles it (if the node is
   the output of a gate whose inputs are the selects, (a) is right).
10. **`cdp4_ld`'s metal over the box** (the `?M` at x 7556, y 13895-13953): no metal in either metal
   shot for 51 px. Readings: one metal, dark over the box (trap 27); or two metals that both end at the
   box, on a contact inside it or on nothing. Assumed one metal: the clean shot shows the box in
   protected colours, a metal line does not end without a contact, and under reading (b) or (c) of
   Ambiguity 9 the two pieces are joined through the contact all the same. So `cdp4_ld` = `bc1_ld_a`
   holds under every reading; what differs is whether `cdp4_rst` or the group's node is on it too.
11. **Which end drives `cdp3_g_c#`** (piece `d6`): the field holds no transistor. One end is the data
   input of `cdp4`'s row D latch (a pass transistor: it does not drive), the other `cdp3`'s row A cell,
   untraced. Settled by tracing that cell (`cdp3` (continue)).
12. **`bc1_d3` .. `bc1_d6` and `cdp4_in6_s3` .. `s6`** (piece `d6`): `bc1` draws lines 3-6 only to
   x 8040 ("continues right: staircase, then beyond x 8500"), so the extraction does not join
   `cdp3_g_c4` .. `c7` to row D's bits s3 .. s6. Working assumption: joined in order, as lines 1 and 2
   are. Settled by `bc1` (continue).
13. **The track of `tc2_sr_g` over the poly row y 13744, at (7145,13728-13749)** (piece `sr`). Neither
   metal shot passes the metal test for 22 px along the track there (the other rows it crosses give
   8-13 px edge bars). Chip 2 shows a dark disc about 12 px across at (7145,13738) between the row's two
   edge bars (`tools/px.py col 7145 13722 13764 3`: red 44-86 from y 13731 to 13746); chip 1 shows the
   north edge bar and then a dim reddish stretch (red 112-177, green 78-99 at x 7145; 148-174/121-150
   at x 7150), under the test's level. Readings: (a) a plain crossing with marks on the metal; (b) a
   contact from the track onto the row, which would put `tc2_sr_g` on the row y 13744 (an undrawn poly
   row from west of x 6500 to a gate band, y 13750-13768, of `cdp4`'s corner gate group). Working
   assumption: (a). For it: the metal is not widened (18 px above, at and below the crossing; every
   contact in this field has a pad of about 40 px) and neither is the row (edges y 13734 and 13752, as
   elsewhere); the clean shot shows the row in protected poly colour under the track (215/160/113 at
   (7145,13740-13746), no hole, the protected strip as wide as above and below the row); the chip-2
   stripped shot reads as at the plain crossing of row y 13701 60 px north
   (`tools/textmap.py 7118 13690 7172 13772 3 --acid`); no bright centre in chip 2; and chip 2's metal
   alone is dark the same way where this track crosses row y 13852 (y 13850-13872) and at three places
   the round-5 reviewer found on piece `d6`'s tracks. Against: both chips are dim at the same spot,
   which dirt on one chip does not explain. Views `sr_c1.png` (4x), `sr_c3.png` (7x), `sr_c4.png` (the
   two rows under thirty tracks, 1.5x). Would settle it: the far ends of row y 13744 (if `tc2_sr_g` were
   on it, the row would need no other driver) and the corner gate group (`cdp4` (continue)).
14. **The south end of `cdp3_k_b`'s track** (piece `kb`): the pad (7538-7584, 11096-11144) is read as
   diffusion from its plain tan colour under the pad's metal in the clean shot, and the band east of it
   as the same diffusion from its two edge lines and the tan under the rail's edge. In the open gap
   between the pad's metal and the rail (x 7585-7597) the band has no colour of its own (clean shot
   110/93/64, chip-2 stripped shot 97/95/79, red minus green 2, like field) and the clean shot has a
   dark bar across it at x 7585 that the chip-2 shots do not have. Readings: one diffusion from the pad
   to under the rail; or a pad that ends at x 7584 with something else east of it. Working assumption:
   one diffusion (the two edge lines run unbroken from the pad's corners to the rail in the chip-2
   metal shot). What is under the rail is `cdp3` (continue)'s; nothing drawn depends on it yet.
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

**Run 4, piece `ctl`. Round 1: full review** (2026-11-19 17:39 +0100; a fresh Fable 5.2 reviewer agent;
commit 01aa682; images in `cache/scratch/busl/review-4/`, 33 used).
Told to suspect: the box (7535-7580, 13903-13940) and the metal x 7556 across it (a contact, two metals
or one, whether `cdp4_rst`'s poly reaches it); the four through pads (the right track, running on, the
right row); the nested staircase (read at 2.4x); the near misses (sel2's arm above sel3's pad, the
corner north of `cdp4_rst`'s pad, `cdp4_ld`'s pad below `cdp4_bus_s0`'s, the arms y 13938 and 13982
beside the rows); the staircase step on row y 13809 and the one north of row y 13701; the ten row
stretches (a break, a step, an early end, a tapped track, whether the four lower ones go on past
x 7550); the rows' identity at x 7600; taps on the six tracks; eight coloured stretches and the dot
(7558,13792).
Checked: the box at 4x and 7x in four shots (protected colours in the clean shot up to its north and
south outlines on the track's line, open ground beside; poly colour on both sides of its west outline
in the chip-2 stripped shot; the pad (7467,13897) and the band one poly; no metal between that pad and
the arm y 13938); the staircase at 4.4x in both metal shots (four right-angle steps, order kept, no
bridge; a green patch under sel2 at (6583,13120-13170) in chip 1 only); all eleven pads at 4.2-4.5x in
both chips (ring and bright centre, each on its claimed track; the four through tracks carry on south);
the near misses (ground or bare poly between, and one more: another net's corner (7430,13897) 10-16 px
west of `cdp4_rst`'s south pad); the rows (six at x 7600, matching `cdp4`; all ten stretches
continuous, poly colour in every open gap in chip 2; the four lower rows run on past x 7550); the
crossings on all six tracks (edge bars only); the step on row y 13809 at 5x and the greenish spots (no
ring, pad or widening); the join to `bc1` (the corner (7448,13982), the crossing of row y 14004, one
metal on to y 14636); the extraction and `tools/unsure.py`.
Findings: one, a comment only, confirmed by the tracer:
1. Ambiguity 9 said "Against: nothing" and the inventory "no bright centre in either": there is a
   9 x 10 px spot at (7557,13929) on the track's line inside the box, at ground brightness in chip 1's
   metal shot and greenish in the chip-2 stripped shot. Tracer: confirmed (`tools/px.py pt 7557,13929
   7557,13915 7556,13880 7535,13929 all`: 97/89/51, 140/122/62, 136/154/83, 196/169/118 at the spot;
   the track at (7556,13880) 205/134/59 and 199/159/98). Not a contact by the tests (no ring, dark in
   chip 2, off-centre); recorded in Ambiguity 9 and under the piece. Nothing drawn changes: the stretch
   stays `?M` and the box undrawn.
The trace is unchanged since the reviewed commit.
`tools/t.sh busl sameconn.py 01aa682`: `connections identical`.
`.venv/bin/python tools/sameconn.py 01aa682`: `connections identical`.
Could not check, or only weakly: whether the metal is continuous over the box and what the box is (the
corner gate group settles it); most row crossings by the two-chip metal test and text maps, not each
at 4x; the clean shot's hole test is weak in this field (sure contacts read red minus green from -12
to +61); anything south of y 15000, east of the drawn ends, or `bc1`'s metal beyond y 14060.

Round 1: no findings that change a connection.

**Run 5, piece `d6`. Round 1: full review** (2026-11-19 18:02 +0100; a fresh Fable 5.2 reviewer agent;
commit d9c6e0e; images in `cache/scratch/busl/review-5/`, 15 read).
Told to suspect: a swap or bridge in either staircase (the upper read at 2.3x, the lower at 3.6x, in
the chip-2 metal shot; the follower leaves lines 1, 2 and 4 at their lower arms), the long runs (a
step of one track, a pad, a contact or a break; line 6's detour at y 12835), a track running on
through either end, a second poly on a row-end pad, the rows from the pads to x 7600, each lower track
on the right line of `bc1`'s, the dismissed spots (six named, the crossings of row y 12745, the 20 px
dark stretch north of line 1's contact), the two near misses beside `cdp4_rst`'s pads, the arms lying
on the rows y 13809 and y 13852.
Checked: the six north pads at 4x in the chip-2 metal shot and both stripped shots (each on its own
row's west end, field west and north, no second poly, no metal for 55 px or more north of any in
either chip); the rows to x 7600 (unbroken, onto `cdp3`'s rows at the same y); the upper staircase at
3.6x in both metal shots (six nested right-angle steps over field, order kept; the pad (7554,9450) of
another net 8-10 px of open ground below line 6's arm); the long runs by a scan of its own of all
nineteen vertical segments in both metal shots (no widening to 21 px in both chips, no 14 px without
metal in both, a steady centre per 300 px) and strips at 1.12x in the metal and clean shots (no pad,
no poly under a track); line 6's detour at 4x in three shots with text maps (the track x 7512 from
the north ends on its own pad (7510,12742), no metal at y 12766-12820; open ground at y 12848-12854
between the arm and `cdp4_rst`'s north pad); the lower staircase at 3.2x in both metal shots and arms 3
and 4 at 4x in four shots (order kept; no ring or hole on either arm; open ground at x 7440-7448
between line 5's corner and `cdp4_rst`'s south pad; line 6's arm clear of the box at x 7535); the south
ends (each track on the claimed pad of `bc1`'s, no metal on south; line 1's dark stretch is ring plus
row edge); the seventh track where it crosses `bc1`'s rows (no ring, widening or hole); the dismissed
spots by text map and the y 12745 crossings at 4x; the extraction and `tools/unsure.py` (none of the
six nets listed).
Findings: none. Two comments for the notes, both checked by the tracer and added under the piece
(chip 2's dark notches on the metal at three places; the red stain on pads 1 and 2 in the clean shot).
The trace is unchanged since the reviewed commit.
Could not check, or only weakly: the long runs end to end at 2x or more (they rest on the 1.12x
strips and the two numeric scans); `bc1`'s rows east of the pads and `cdp3`'s rows east of x 7780.

Round 1: no findings.

## Not done

- Everything else in the field: about 20 more tracks and the other rows. Next pieces, in the
  order they join things: (1) done in run 6 (pieces `sr`, `kb`; `cdp4_ld8b`'s row does not enter the field); (2) the rows
  y 13744 and y 13852 (from west of x 6500 to gate bands of `cdp4`'s corner gate group) and the two
  tracks that step west of the selects' staircase (x 6516, x 6559 at y 12700); (3) what else arrives
  from `lc3` at y 10400 (`ports.d/lc3.txt`): the six diagonal metals at x 5915, 5851, 5785, 5722, 5655,
  5588 (`lc3_e9577` .. `lc3_e9793`), the polys at x 5475 (`rst_n`) and x 5541 (`lc2_w8450` again), the
  VCC metal x 5340-5390; (4) the top band's ninth row (y 10317, `cdp3_gate_f`) and the three poly rows
  at the top left (y 10560, 10686, 10736); (5) the staircases at x 5100-5700, y 10600-10960 west of
  piece `h8`'s; (6) the bands at y 11850-12150 and below; (7) the foot of the field: rows y 14827 and
  14870 from their pads (6915,14828), (6872,14868) and those pads' tracks north (x 6927, x 6885); the
  net that starts on row y 14523 at the pad (7100,14522); the rows above y 14523 (`bc1`'s bus has four
  more, y 14354-14482); the track x 6452 beside piece `lc9`'s pads; the metal that turns south at
  about (7187,14165) below line 1's end pad.
- Piece `sr`'s south end: `tc2_sr_g`'s track from (7187,15000) on: x 7186 south over `tla`'s poly
  (y 15334-15444) to (7186,15482), west to x 7103, south; the follower ends at (7100,16279), contact
  candidates at (7100,15596-15660) (`bc1` (continue): the group x 7000-7860, y 15000-16300; seen at 1x
  in `sr_s3.png`, nothing read). The driver of `tc2_sr_g` is expected there. And the row y 13744, whose
  ends decide Ambiguity 13 (item (2) above).
- Piece `kb`'s south end: the diffusion band east of x 7600 at y 11100-11127, under column 0's VSS
  rail (`cdp3` (continue)); the three other diagonals of the bundle north-west of `sr`'s (one ends on
  the pad (7425,8862), whose poly runs east along y 8850-8875 under `sr`'s track; the northern part).
- `cdp4_ld8b`'s west end at about x 7603-7640, y 11825-11850, under the metal x 7600-7645 (`cdp4`
  (continue); view `b_ends.png`, tile 3).
- Piece `d6`'s ends: `bc1`'s lines 3-6 east of x 8040 to the feet of `cdp4_in6_s3` .. `s6` (`bc1`
  (continue); Ambiguity 12); the row A cells of `cdp3` on line g (`cdp3` (continue)).
- Piece `ctl`'s ends: the four select tracks south of y 15000 (x 6538, 6581, 6624, 6668; to y about
  16150-16190: `bl0`, `bl1`), where their drivers must be; **the gate group at `cdp4`'s bottom-left
  corner** (`cdp4` (continue), x 7550-7870, y 13640-14040): the box (7535-7580, 13903-13940) on which
  `cdp4_rst`'s poly ends (Ambiguity 9), the diffusion column under the wide metal x 7598-7650 with its
  contacts (7607,13718), (7607,13838) and the gate bands of sel1 (y 13677-13698), row y 13744
  (13750-13768), sel3 (13792-13812), row y 13852 (13862-13882), sel4 (13949-13973), sel2 (y 14004 on).
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
