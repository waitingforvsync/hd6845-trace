# tl6: top-left random logic, the sixth strip (x 5683-6400, y 2500-6350)

Package `tl6` (part 6 of 6 of the top-left logic, the eastmost strip). Trace: `trace/tl6.txt`.
Views: `cache/scratch/tl6/`. The strip is a **track field**: vertical metal tracks at a 43.5 px
pitch, poly rows under them, pads. No gate and no diffusion has been found in it. Its job is
to carry the signals of `tl5`'s gate column (and of the strips west of it) to the gate column
`tcw`, to the crossing field in front of the island `tc1`/`tc2`, and south.

## Status

2026-11-18 03:20 +0000. **Partial: piece 1 of three is traced**: the rows of all thirteen of
`tl5`'s east ports north of y 6200 to their ends, the tracks U0, U1, U2 and the north pieces of
U4 and U5 to both their ends, the bus metals y 4482 and y 4787 to `tc2`'s ports, and `ral_stb`
from `tc2`'s port to the south edge. Wiring only: no transistor (none found in the strip).
Eight joins between named nets, all without a `?` item: `tl5_w4395` = `tcw_m6320`,
`tl5_w4590` = `tcw_m6232`, `tl5_w4633` = `tcw_c`, `tl5_w4503` = `tl5_w4850`, `tl5_w4807` =
`ras_o0_alt2`, `tl5_w5544` = `tc1_o3527`, `tl5_w5631` = `tcw_a`, and `ral_stb`'s way west.
Full extraction: 0 errors, 0 warnings. Not traced: Not done.

## Inventory

Survey (written first to `cache/scratch/tl6/survey.md`): `survey.png` (0.33x, every block's
geometry), `sv0_m.png`..`sv2_m.png`, `sv0_a.png`..`sv2_a.png` (0.95x, chip-2 metal and the clean
shot, three sections), `n_top.png` (1.8x, y 2490-2770), `a_w.png`, `a_e.png` (2.4x, the rows
y 3630-4160 at their west and east ends), `b_w1.png`, `b_w2.png` (1.9x, x 5675-6065,
y 4390-5100), `c_top.png`, `c_bot.png` (2.1x, the crossing field's top and foot), `d_sw.png`
(2.0x), `d_se.png` (1.75x) (y 5960-6360).

**Known cells first.** `tools/findcell.py` was not run: the cells of `tl1`, `tl5`, `tla`, `tc1`
and `tcw` are gates on a rail with a load under a second rail, and the strip has no rail, no
box and no diffusion (the six survey views at 0.95x and the eleven closer ones show only
tracks, rows, pads and bare ground; `tools/opendiff.py`: below, Self-check). A track field is
read track by track.

Tracks, by x (`segs.py 5683 6400` at 25 values of y, both metal shots; `tools/tl5_tracks.py v X
2500 6350` for every track: the stretches without metal and the clean shot's green holes):
U0 5712, U1 5755, U2 5799, U3 5843, U4 5886, U5 5930, U6 5973, U7 6016/6022, U8 6059, U9 6103,
U10 6146, U11 6190, then `tcw`'s 6233, 6276, 6320, 6363.

| Where | What | State |
|---|---|---|
| U0 x 5712, y 3722-6192 | one metal, pads at both ends | traced (piece 1) |
| U1 x 5755, y 4002-6065 | one metal from an arm at y 4002; pads (5800,4002), (5757,5632), (5755,6065) | traced (piece 1) |
| U2 x 5799 | three pieces: y 4135-4633, y 4698-4850, y 4980 to the south edge | traced (piece 1) |
| U3 x 5843 | `r9m`'s `r9m_l3` north of its pad (5845,5045); `bw`'s `rc_stepreq_n` south of the pad (5838,5585) | theirs; the pad (5845,5045)'s poly east along y 5045: not traced |
| U4 x 5886, U5 x 5930, north pieces | y 2722-4522 and y 2680-4437, pads at both ends, polys north out of the strip | traced (piece 1) |
| U4-U7 south of y 4565 | `amrw`'s and `bust`'s `c4l0`..`c4l3` | theirs |
| U6 x 5973, U7 x 6022 north | `r9m`'s `ra_eq_r9` and `r9m_l1w` | theirs |
| U8 x 6059, U9 6103, U10 6146, U11 6190, north of the crossing field | U8 from a pad (6058,2592) (poly north), U9 from a pad (6102,2550) (poly east), U10 and U11 from corners at y 2572 and y 2620 (metals east out of the strip); south ends on the north pads of the crossing field's polys | not traced (piece 2) |
| x 6040-6420, y 4390-4890 | **the crossing field**: eight vertical polys (x 6059 `r9m`'s, 6101, 6143, 6187, 6228, 6275, 6316 `fld`'s, 6405 `fld`'s) under eight bus metals (y 4482 `tc1_o3527`, 4528 `ra_eq_r9`, 4572 `c4l0`, 4613 `c4l1`, 4658 `c4l2`, 4701 `c4l3`, 4742 `r9m`'s, 4787 `ras_o0_alt2`) | the bus metals y 4482 and y 4787: traced (piece 1); the five polys x 6101-6275: not traced (piece 2) |
| x 6090-6400, y 4830-6160 | five metals south from the field's south pads and one from a pad (6316,5003), a nest of corners at y 5568-5790 | not traced (piece 2) |
| the rows y 3659, 3872, 4003, 4134 | from `tl5`'s ports and from the pads (5800,3658), (5800,4002), (5798,4135) east to pads of `tcw` and `fld` | traced (piece 1) |
| the rows y 4437-4979 | `tl5`'s nine ports there, to pads on U2, U4, U5, the pad (6010,4480) and the pad (6058,4872) | traced (piece 1) |
| the rows y 5632, 6065, 6151, 6195, 6325 | to pads on U1 and to four pads at x 5972-6145, whose metals leave south or east | traced (piece 1) |
| the row y 6238 (`tl5_w5717`) | east to about x 6240, where a poly goes south | not traced (piece 3) |
| x 5890-6190, y 5985-6240 | a wide metal: a band y 5985-6025, a leg x 5890-5925 south, a leg x 6150-6190 south to a band y 6195-6240 east (`tc2`'s `vss` port at (6400, 6198-6243)) | not traced |
| x 6230-6400, y 6100-6350 | three pads (6283,6150), (6323,6108), (6365,6150) with polys south, between them narrow outlined strips | not traced (piece 2) |
| x 5683-6400, y 2500-2700 | the tracks' north ends, a poly along y 2535 east of the pad (6102,2550), the rim of the wide metal band at y 2500 | not traced (piece 2) |

## Logic

No transistor. What the wiring joins (every join below is drawn without a `?` item;
`tools/unsure.py`):

### Piece 1 (traced 2026-11-18 03:15 +0000): the rows of `tl5`'s east ports and the tracks U0, U1, U2, U4, U5

| `tl5`'s port | Path (all read at 4x in the chip-2 metal shot and the clean shot unless noted) | Result |
|---|---|---|
| `tl5_w4395`, metal y 3659 (latch c's data) | the metal runs on 115 px to a pad (5800,3658); the pad's poly east along y 3650-3668 under U3-U11 and `tcw`'s track x 6233 onto `tcw`'s drawn poly (from x 6205) and its pad (6315,3655) | **`tl5_w4395` = `tcw_m6320`** |
| `tl5_w3505`, row y 3722 (latch a's enable) | ends on a pad (5712,3722), the north end of U0; U0 south to its pad (5712,6192); poly east along y 6195 to a pad (5972,6193); metal south across y 6350 | leaves south at (5972,6350) |
| `tl5_w4590`, row y 3872 (latch c's clear) | east under U0 (no pad) and U3-U11 into `tcw`'s pad (6232,3870) | **`tl5_w4590` = `tcw_m6232`** |
| `tl5_w5500`, row y 4437 | pad (5928,4437), U5's north piece north to its pad (5928,2680); poly north across y 2500 | leaves north at (5928,2500) |
| `tl5_w5544`, pad (5666,4480) | poly east to a pad (6010,4480), the west end of the bus metal y 4482, which crosses the field to `tc2`'s port | **`tl5_w5544` = `tc1_o3527`** |
| `tl5_w5457`, row y 4521 | pad (5886,4522), U4's north piece north to its pad (5887,2722); poly north across y 2500 | leaves north at (5887,2500) |
| `tl5_w4503`, row y 4590 (latch c's inverse output) | east to a corner at x 5867 (in the open between U3 and U4), south, west along y 4699 to a pad (5797,4698); U2's middle piece south to a pad (5797,4850); the row y 4849 west | **`tl5_w4503` = `tl5_w4850`**: inverter 1's input is latch c's inverse output |
| `tl5_w4633`, row y 4633 (latch c's output) | pad (5797,4633), U2's upper piece north to a pad (5798,4135); poly east along y 4134 into `fld`'s pad (6318,4135) | **`tl5_w4633` = `tcw_c`** |
| `tl5_w4807`, row y 4808 (inverter 1's output) | east under U0-U7, south at x 6058 to a pad (6058,4872); metal north to the west end of the bus metal y 4787, which crosses the field to `tc2`'s port | **`tl5_w4807` = `ras_o0_alt2`** |
| `tl5_w4850`, row y 4849 | the pad (5797,4850) above | |
| `tl5_w3982` (`tl4_w4068`), row y 4979 | pad (5798,4980), U2's south piece south across y 6350 | leaves south at (5799,6350) |
| `tl5_w5631`, pad (5666,5632) | poly east under U0 to a pad (5757,5632) **on U1** | **`tl5_w5631` = `tcw_a`** |
| `tl5_w5674`, pad (5667,6150) | poly east along y 6151 to a pad (6016,6150); metal south across y 6350 | leaves south at (6016,6350) |

And from the east:

| Net | Path | Result |
|---|---|---|
| `tcw_a` (`fld`'s pad (6400,4005)) | poly west along y 4003 to a pad (5800,4002); metal west to a corner (5755,4002) and south as U1, pads (5757,5632) and (5755,6065); the south pad's poly east along y 6065 to a pad (6016,6066); metal east to a corner (6105,6066) and south across y 6350 | `tcw_a` is `tl5_w5631` and leaves south at (6105,6350) |
| `ral_stb` (`tc2`'s metal y 6328) | west to a pad (6145,6322); poly west along y 6325 to a pad (5755,6322); metal south across y 6350 | leaves south at (5755,6350). `tc2`'s notes give the follower's end (6012,6068) for this metal: the follower jumped from the pad to the metal x 6105 (which passes 40 px west of it without a contact: `t11.png` 4x, three shots) |

**What that says about the logic** (the equations are `tl5`'s, `tcw`'s and `fld`'s, with the
names joined here):

```
latch c (tl5):   tl5_w4633 = NOT( tcw_m6232  OR  tl5_w4458 AND NOT tcw_m6320  OR  tl5_w4503 )     = tcw_c
                 tl5_w4503 = NOT( tcw_m6320 AND tl5_w4458  OR  tl5_w4633 )
inverter 1:      ras_o0_alt2 = NOT tl5_w4503
tcw / fld:       fld_y_b = NOT tcw_c ;  tcw_o3820 = NOT( fld_a_in OR (tcw_a AND tcw_c) ) ;  fld_a_in = NOT( (tcw_a AND tcw_b) OR tcw_o3820 )
```

- **`ras_o0_alt2`, the signal that drives row address bit 0 in interlace sync-and-video mode
  when R9's bit 0 is clear, is latch c of `tl5`'s column, buffered**: `ras_o0_alt2` = NOT
  `tl5_w4503`, and `tl5_w4503` is the latch's inverse output. Latch c is open while
  `tl5_w4458` is high, takes `tcw_m6320` (from `tcw`'s gate column) and is cleared by
  `tcw_m6232`.
- **The same latch's output is `tcw_c`**: the data of `tcw`'s latch (the cross-coupled pair
  `fld_a_in` / `tcw_o3820`, gated by `tcw_a`) and, inverted, `fld_y_b`, the second input of the
  XOR that makes `ras_o0_alt1`. So both sources of row address bit 0 in that mode come from
  latch c: it is the best candidate for the **field (odd/even) flip-flop**; believed, not
  shown (what clocks and clears it is not identified).
- `tc1_o3527` (cell B's output of `tc1`) goes west to `tl5`'s track T10 and on into `tl4`'s
  strip on the row y 5544.

**Seen** (4x tiles: chip-2 metal over the clean shot, 104 x 100 px each):

| Item | Reading | Seen |
|---|---|---|
| pads (5800,3658), (5712,3722), (5800,4002) with its corner (5762,4003) | each a ring with a bright centre and a green hole on a salmon pad; T10's metal arrives from the west and ends on the first, bare ground east; the row y 3722 ends on the second (closed east end x 5733), U0 leaves south, bare ground north; the third's metal goes west and turns south | `t1.png` |
| pads (5798,4135), (5928,4437), (5886,4522) | U2 leaves the first south (closed west end); U5 arrives on the second from the north (closed east end x 5947, bare ground south); U4 arrives on the third from the north (closed east end x 5905, bare ground south to `amrw`'s corner at y 4565) | `t2.png` |
| pads (5797,4633), (5797,4698), the corner (5867,4590) | U2's upper piece ends on the first (bare ground, an hourglass of open field, between the two pads); the second's poly leaves east | `t3.png` |
| the L of `tl5_w4503`, x 5857-5877, y 4580-4708 | one poly in the open between U3 and U4: `px.py col 5866 4566 4722 6 metal,metal1,acid`: poly colour (146-170/112-135/46-61 in chip 2) without a dark line from y 4584 to y 4704, dark edges at y 4578 and y 4710, bare ground beyond; the row y 4590 has the same colour at the corner (x 5860-5868) as in the gap between U2 and U3 (x 5816-5824), where it surely runs on; `px.py row 4699 5810 5885 5` | `t4.png` (4x: chip-2 stripped, clean, chip-1 metal) |
| pads (5797,4850), (5798,4980), the corner (6058,4808) and pad (6058,4872) | U2's middle piece ends on the first (bare ground south); U2's south piece starts on the second (bare ground north); the row y 4808 turns south into a 30 px wide pad stem; the pad's metal goes north to the bus metal | `t5.png` |
| the pad (6010,4480) and `r9m`'s corner (6022,4442) / pad (6059,4440) beside it | the row y 4480 ends on the pad (6010,4480), whose metal runs east as the bus metal y 4482; `r9m`'s metal turns east 20 px north of it onto its own pad: 14 px of dark between the two metals in both chips | `q1.png` (4x, three shots) |
| joins to `tcw`'s poly at (6205-6215, 3655), to `tcw`'s pad (6232,3870), to `fld`'s pads (6318,4135) and (6400,4005) | each row runs into the other block's drawn pad or poly as one salmon band | `t6.png`, `t7.png` |
| pads (5887,2722), (5928,2680) | north ends of U4 and U5 (bare ground north of each metal); each pad's poly goes north | `t7.png`; the polys at y 2500-2560: `t12.png` (they run on under the band's rim) |
| pad (5757,5632) on U1 | ring with a bright centre in both metal shots, green hole; the row from `tl5`'s pad (5666,5632) passes under U0 (no widening) and ends on it (closed east end x 5775); U1 runs through | `t10.png` (4x, three shots); found by `tl5_tracks.py v 5755 4012 6052` (hole at y 5634) |
| pads (5712,6192), (5972,6193), (5755,6065) | U0 ends on the first; the row y 6195 ends on the second (closed east end x 5990), metal south; U1 ends on the third, poly east | `t8.png` |
| pads (6016,6066), (6016,6150), (5755,6322) | the row y 6065 ends on the first, metal east; the row y 6151 ends on the second, metal south; the third's poly goes east, its metal south | `t9.png` |
| pad (6145,6322) and the metal x 6105 | the row y 6325 ends on the pad, whose metal goes east (`ral_stb`); the metal x 6105 crosses the row 40 px west of the pad at constant width without a ring | `t11.png` (4x, three shots) |
| the south edge at x 5725-6045, the north edge at x 5855-5960 | the metals x 5755, 5799, 5972, 6016 and the two polys run on across the edge | `t12.png` |
| the east edge at y 4482, 4787, 6328 | each metal runs on into `tc2`'s drawn piece (its `tc1_o3527`, `ras_o0_alt2`, `ral_stb`) | `t13.png` |

**The rows between their ends.** The clean shot along each row (a cream test, red > 195 and
red - green > 30, over 7 px): cream under every track the row crosses and nowhere widened; the
gaps between are the 25-30 px gaps between tracks (gap marks, tracing guide trap 2). Along
each track, `tools/tl5_tracks.py v`:

| Piece | Longest stretch without metal in both shots | Green holes |
|---|---|---|
| U0, x 5712, y 3735-6180 | 15 px (row edges) | none |
| U1, x 5755, y 4012-6052 | 18 px (y 5608-5626) and 16 px (y 5636-5652): the ring of the pad (5757,5632) | 5634 (the pad) |
| U2 upper, x 5799, y 4148-4622 | 9 px | none |
| U2 middle, x 5798, y 4712-4838 | 9 px | none |
| U2 south, x 5800, y 4992-6350 | 15 px (y 5570-5585) | none |
| U5 north, x 5930, y 2692-4425 | 11 px | none |
| U4 north, x 5886, y 2735-4510 | 12 px | none |
| bus metal y 4483, x 6025-6405 | 16 px (the pad's ring); 8-11 px at each poly's edges | none |
| bus metal y 4787, x 6062-6405 | 13 px | none |
| T10's piece y 3659, x 5683-5785 | none | none |
| x 6105, y 6075-6420; x 6016, y 6165-6360; x 5972, y 6208-6360; y 6328, x 6160-6420 | 12 px | none |

## Self-check (tracer, before any review)

**Piece 1 (2026-11-18 03:20 +0000).**
*Ends.* Every pad, corner and edge crossing drawn is in the "Seen" table: 21 pads and 4 corners
at 4x in the chip-2 metal shot and the clean shot (three shots where a neighbour's metal is
close), each with the ground about 50 px beyond; the edges on `t12.png` (south, north) and
`t13.png` (east); the west edge is `tl5`'s ports (its `pc3.png`, `pi1.png`, `g_n.png`,
`p2_c.png`; the rows at x 5676-5700 on `a_w.png` 2.4x and `ov1.png` 2x: **below 4x**; they are
straight bands onto `tl5`'s drawn rows, and the extraction joins each to `tl5`'s net).
The south edge at x 6105 and x 5972: `t12.png` shows x 5972 and x 6016; x 6105 at y 6350 only
by the metal test (`tl5_tracks.py v 6105 6075 6420`: metal to y 6420).
*Widths.* No transistor. No row or track drawn crosses a diffusion: `tools/opendiff.py 5683
2500 6400 6350` lists 22 green groups, all strips 8-12 px wide beside pads or between metals
(none wider than 12 px in its narrow direction).
*Weak spots.* (1) The rows between x 5830 and x 6200 (y 3659, 3872, 4003, 4134) rest on the
0.95x and 2.4x views and the cream test, not on a 4x view of every crossing; their ends are at
4x. (2) U0, U1, U2, U4, U5 between their pads rest on the metal test and the hole scan (which
found the pad (5757,5632)), and the 0.95x views. (3) The L of `tl5_w4503` is in the open with
a gap mark on each corner in the clean shot: decided by the colour profile in the chip-2 metal
shot (table). (4) The bus metals y 4482 and y 4787 over the field: the metal test and the hole
scan; the five polys under them are piece 2.
*Omissions* inside what is traced: rings in the metal shots without a drawn item: none on the
drawn tracks (specks only; no hole under them). Outlined boxes in the clean shot without a
drawn item: the khaki boxes between rows and tracks (open field between protected margins);
the hourglass (5775-5820, 4650-4685) between the pads (5797,4633) and (5797,4698): open
field, bare ground in the metal shot (`t3.png`).
*Track fields.* The table of metal tests above. Each pad's track: U0, U1, U2 are the three
westmost tracks and each of their pads has its metal seen leaving it at 4x; the pad
(5886,4522) is on U4 and (5928,4437) on U5 (`t2.png`: the metal over each pad, U3 `r9m`'s
drawn line beside the first).
*Joins to other blocks.* `tcw`'s poly `P 6315,3655 x6205` (its pad (6315,3655), net
`tcw_m6320`); `tcw`'s pad `P 6214,3853:6250,3888` (`tcw_m6232`); `fld`'s pads
`P 6383,3988:6418,4022` (`tcw_a`) and `P 6300,4118:6336,4152` (`tcw_c`); `tc2`'s metals
`M 6400,4482...` (`tc1_o3527`), its `ras_o0_alt2` row metal and `M 7489,6274 y6328 x6400`
(`ral_stb`); `tl5`'s rows and pads at x 5683. `tools/amr_at.py` gives the joined name on every
piece.

## Ports

The same ports are in `ports.d/tl6.txt`. West-side ports carry `tl5`'s names (aliases).

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tl5_w4395` | metal | (5683, 3652-3666) | ? | = `tcw_m6320`; latch c's data |
| `tl5_w3505` | poly | (5683, 3712-3732) | ? | latch a's enable, to U0 |
| `tl5_w4590` | poly | (5683, 3862-3882) | ? | = `tcw_m6232`; latch c's clear |
| `tl5_w5500` | poly | (5683, 4427-4447) | ? | to U5's north piece |
| `tl5_w5544` | poly | (5683, 4470-4490) | ? | = `tc1_o3527` |
| `tl5_w5457` | poly | (5683, 4511-4531) | ? | to U4's north piece |
| `tl5_w4503` | poly | (5683, 4580-4600) | in | latch c's inverse output |
| `tl5_w4633` | poly | (5683, 4623-4643) | in | = `tcw_c`; latch c's output |
| `tl5_w4807` | poly | (5683, 4798-4818) | in | = `ras_o0_alt2`; inverter 1's output |
| `tl5_w4850` | poly | (5683, 4840-4858) | ? | = `tl5_w4503`; inverter 1's gate |
| `tl5_w3982` | poly | (5683, 4970-4988) | ? | = `tl4_w4068`; to U2's south piece |
| `tl5_w5631` | poly | (5683, 5622-5642) | ? | = `tcw_a` |
| `tl5_w5674` | poly | (5683, 6142-6160) | ? | to the pad (6016,6150) |
| `tl5_w5457` | poly | (5877-5897, 2500) | ? | north from U4's north pad |
| `tl5_w5500` | poly | (5918-5938, 2500) | ? | north from U5's north pad |
| `tcw_m6320` | poly | (6212, 3649-3667) | ? | onto `tcw`'s poly |
| `tcw_m6232` | poly | (6225, 3862-3882) | ? | into `tcw`'s pad (6232,3870) |
| `tcw_a` | poly | (6392, 3994-4012) | ? | into `fld`'s pad (6400,4005) |
| `tcw_c` | poly | (6310, 4125-4143) | ? | into `fld`'s pad (6318,4135) |
| `tc1_o3527` | metal | (6400, 4472-4492) | in | bus metal y 4482 |
| `ras_o0_alt2` | metal | (6400, 4777-4797) | ? | bus metal y 4787 |
| `ral_stb` | metal | (6400, 6318-6338) | ? | on east as `tc2`'s piece |
| `ral_stb` | metal | (5749-5761, 6350) | ? | from the pad (5755,6322) |
| `tl4_w4068` | metal | (5793-5805, 6350) | ? | U2's south piece |
| `tl5_w3505` | metal | (5966-5978, 6350) | ? | from the pad (5972,6193) |
| `tl5_w5674` | metal | (6010-6022, 6350) | ? | from the pad (6016,6150) |
| `tcw_a` | metal | (6099-6111, 6350) | ? | from the corner (6105,6066) |

## Ambiguities

None in piece 1.

## Not done

- Piece 2: U8-U11 north of the field (ends in the Inventory), the five polys x 6101-6275 of the
  crossing field with their pads, the metals south of the field and their nest of corners to
  `tc2`'s ports and to the pads (6283,6150), (6323,6108), (6365,6150); `tcw`'s track x 6276
  north of y 2700 (a corner at y 2665, east).
- Piece 3: the row y 5045 east of `r9m`'s pad (5845,5045); the row y 6238 (`tl5_w5717`) east of
  x 5683; the wide metal x 5890-6190, y 5985-6240; `amrw`'s and `bust`'s pads at x 5880-5935,
  y 5805-5935 are theirs.

## Review
