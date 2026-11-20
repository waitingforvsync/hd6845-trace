# tl5: top-left random logic, the fifth strip (x 4967-5683, y 2500-6350)

Package `tl5` (part 5 of 6 of the top-left logic). Trace: `trace/tl5.txt`. Views:
`cache/scratch/tl5/`. The strip holds a **gate column** east of `tl4`'s rail RB (the mirror
image of the first cluster's west column: `tl1`'s units, here on the rails RC and RB) and a
**bus field** of eleven vertical metal tracks east of it.

## Status

2026-11-18 02:48 +0000. **Partial: the gate column is traced from y 3040 to its foot** (42 transistors): an
inverter at the top (hand-traced), a NOR, three latches and two inverters (mirrored copies of
`tl1`'s NOR, cells `tl1_ua`/`tl1_ub` and inverter); **the eight north rows** that bring their
signals in from `tl4`'s strip, **the thin metal W** over the column, **every track T0-T10 to both
its ends**, **the foot** (y 5045-5440: no device), **the eight rows under it** (y 5447-5770) and
**the poly bus going south** (y 5880-6350): wiring, no transistor south of y 5045. RC is drawn
from the wide metal band at y 2505 to where it leaves west at y 5882-5942 (`vss` by structure
only: the band is not drawn by any block). **Latch b's enable is `tl4`'s `tl4_w4068`** (drawn
join, all metal; `tl4_w4068` is now an alias of it) and **the clear of latches a and b is
`tl4`'s `rst_a`** (drawn join: the row y 2940 to the north pad of the track x 4537;
`rst_a` is an alias of it). Full extraction: 0 errors, 0 warnings. Not
traced: the other six north rows' ways west of x 4967 (seen, in a table; not drawn), the row
y 2552 (Not done).

In the equations below `tl4_w4068` is the net the extraction prints as `tl4_w4068`, and
`rst_a` the one it prints as `rst_a`.

```
tl5_w2722 = NOT tl4_w3113                                            marked: the load's tie (`?`); the pull-down is firm
tl5_w3245 = NOR( tl5_w4160, tl5_w3550 )                              firm
tl5_w3364 = NOT tl5_w3461                                            firm
tl5_w3550 = NOT( tl5_w3461 AND tl5_w3505  OR  tl5_w3680 )            marked: the load ties (`?` in tl1's cells)
tl5_w3680 = NOT( rst_a  OR  tl5_w3505 AND tl5_w3364  OR  tl5_w3550 )   marked likewise
tl5_w3841 = NOT tl5_w3680                                            firm
tl5_w4027 = NOT( tl5_w3680 AND tl4_w4068  OR  tl5_w4160 )            marked
tl5_w4160 = NOT( rst_a  OR  tl4_w4068 AND tl5_w3841  OR  tl5_w4027 )   marked
tl5_w4318 = NOT tcw_m6320                                            firm
tl5_w4503 = NOT( tcw_m6320 AND tl3_e4243  OR  tcw_c )            marked
tcw_c = NOT( c4l_gab  OR  tl3_e4243 AND tl5_w4318  OR  tl5_w4503 )   marked
ras_o0_alt2 = NOT tl5_w4503                                            marked: the load's tie (`?`, as in tl1)
tl5_w4937 = NOT tl4_w4068                                            marked likewise
```

- **The top inverter** (y 3040-3150), a wide rail gate (122/19) with a strong load: its input
  `tl4_w3113` comes in on the north row y 2855 and T8, its output `tl5_w2722` goes onto T3, which
  runs from the north row y 2722 south to y 6114.
- **Latch a** (y 3343-3803): open while `tl5_w3505` is high, takes `tl5_w3461`, cleared
  (output low) by `rst_a`. Output `tl5_w3680`, inverse output `tl5_w3550`.
- **Latch b** (y 3820-4280): open while `tl4_w4068` is high, **takes latch a's output**
  (`tl5_w3680`: the track T8 joins a's output pad to b's data pad), cleared by the same
  `rst_a` (one metal, T0, with both clear pads). Output `tl5_w4160`.
- **Latch c** (y 4297-4757): open while `tl3_e4243` is high, takes `tcw_m6320`, cleared by
  `c4l_gab`. Output `tcw_c` and inverse output `tl5_w4503` both leave the strip east.

- **The NOR** (y 3142-3352) takes latch b's output (`tl5_w4160`, by the track T9) and latch a's
  inverse output (`tl5_w3550`, by T8): `tl5_w3245` is high only while b's output is low and a's
  output is high. It leaves north on T5.

- **Two inverters** below latch c: `ras_o0_alt2` = NOT `tl5_w4503` (input and output both on rows
  that leave the strip east) and `tl5_w4937` = NOT `tl4_w4068`, the inverse of latch b's enable
  (T7 ends on its gate pad), out south on a piece of T4.

- **Where the signals enter and leave** (wiring, no `?` item on any of it): eight poly rows cross
  the strip's west edge at y 2685-2985, each to the north pad of one track: latch a's enable
  `tl5_w3505` (y 2985, T6), the clear of a and b `rst_a` (y 2940, T0, which also runs on
  south to y 6113), the NOR's output `tl5_w3245` (y 2900, T5's north piece), latch b's enable
  `tl4_w4068` (y 2767, T7), latch c's enable `tl3_e4243` (y 2810, T4's north piece), and
  **inverter 2's output `tl5_w4937` = NOT `tl4_w4068`**, which runs from T4's south piece by a row
  along y 5237 onto the thin metal W, up the whole column and out west on the row y 2685.

So a and b are two latches in series with one clear, the build of the two latches in front of
`rcs_e4` in the first cluster (`notes/blocks/tl1.md`), and the NOR picks out the state "a set,
b not (yet) set". What any of the signals is, is not known: every track is followed to both its
ends inside the strip, and each leaves the strip as a row or a bus
line (Ports), not yet joined to anything named, except latch b's enable, which is `tl4_w4068`. Known by name: `res_b` and `lpstb_b` (T1, T2,
`trunks`') go south in the poly bus beside the clear of latches a and b (`rst_a`), the strong
inverter's output (`tl5_w2722`) and latch a's data (`tl5_w3461`).

## Inventory

Survey: `survey.png` (0.33x, all blocks' geometry), `sv0.png`-`sv2.png` (0.9x, chip-2 metal and
clean shot), the bus field in the clean shot at 2.35x: `r0_a.png` (y 2500-2925), `r1_a.png`
(y 2920-3345), `ra_a.png` (y 3335-3815), `rb_a.png` (y 3812-4292), `rc_a.png` (y 4289-4769).

Rails: RB x 4906-4951 (VCC; `tl4`'s east rail, shared: the loads of both columns end on boxes
under it), RC x 5081-5127 (the pull-downs' boxes: VSS, named from structure). Thin metals over
the column: x 4984-4996 (pieces, plate to third pull-down, as in the master), x 5028-5046
("thin W", runs the length of the column: traced), x 5171-5185 (pieces, inverter output to
series gate, in the cells). Tracks of the bus field, by x: T0 5233, T1 5277 (`res_b`, drawn by
`trunks`), T2 5320 (`lpstb_b`, `trunks`), T3 5364, T4 5407, T5 5451, T6 5494, T7 5538, T8 5581,
T9 5625, T10 5667 (`segs.py 5195 5690 3420,3580,3760`: both metal shots). Each track is in
pieces; a piece ends on a pad or plainly.

| Where | What | State |
|---|---|---|
| x 4967-5600, y 2540-3000 | poly rows from the west to the pads of the tracks' north ends: `r9m`'s three (y 2596, 2641, 2685 east of their steps) and **eight more, y 2685 (west of the step) to y 2985** | traced (the row y 2552 at the top, under `r9m`'s L, is not looked at) |
| x 4960-5215, y 3040-3156 | **the top inverter** (findcell: `tl1`'s inverter at 2371,-1171 mirrored, score 0.54: not a copy; hand-traced) | traced |
| x 4901-5203, y 3142-3352 | **the NOR** (findcell: `tl1`'s NOR at 2359,-390 mirrored, 0.74) | traced |
| x 4901-5203, y 3343-3803 | **latch a** (findcell: `tl1_ua` 2361,-997 mx 0.70; `tl1_ub` 2361,-998 mx 0.78) | traced |
| x 4901-5203, y 3820-4280 | **latch b** (`tl1_ua` 2361,-520 0.71; `tl1_ub` 2361,-521 0.74) | traced |
| x 4901-5203, y 4297-4757 | **latch c** (`tl1_ua` 2361,-43 0.75; `tl1_ub` 2361,-43 0.75) | traced |
| x 4951-5213, y 4786-4912 and y 4916-5042 | **two inverters** (findcell: `tl1`'s inverter at 2373,565 mx 0.78 and 2373,695 mx 0.77) | traced |
| x 4967-5210, y 5045-5440 | **the column's foot**: RC and the tracks over bare field; W's south pad (5038,5237) with its row east to the pad (5407,5237) | traced: no device |
| x 5200-5683, y 2540-5800 | the bus field: rows of the column to pads on the tracks, rows that pass east out of the strip, the pads (5623,4437), (5666,4480), (5580,4521) of three rows from the east (north ends of T9's, T10's and T8's south pieces) | traced, except T10's north part (y 3654-4402) |
| x 4967-5683, y 5400-5780 | **the rows under the foot**: eight poly rows from the west edge (`bw`'s `rc_stepreq_n` row y 5585 the fourth), one more between two pads (y 5411); six pads at x 5493/5538, three nested corners of T8-T10 | traced: wiring |
| x 4967-5683, y 5780-6350 | **the poly bus going south** (ten vertical polys x 5063-5497), RC's turn west (y 5882-5942), the metal x 5189 and its turn west (y 5982), the south pads of T0 (5148,6108) and T3 (5363,6108), the metal x 5627 to the pad (5667,6150); `amrw`'s four counter lines and their pads, `trunks`' pads of T1/T2, `tla`'s `rcs_e4` line (theirs) | traced: wiring |

## Logic

### The three latches (traced 2026-11-18 01:48 +0000: cells `tl1_ua`, `tl1_ub`, mirrored)

**That they are copies.** `tools/findcell.py` (clean shot, masters 2540-2842 x 4340-4590 and
x 4590-4800, region 4940,2900:5260,5250, orientations 0, m0, 180, m180) gives the six hits in the
inventory, all mirrored about a vertical line. The cells laid over the clean shot at 3.6x
(`a_ua.png`, `a_ub.png`, `b_ua.png`, `b_ub.png`, `c_ua.png`, `c_ub.png`: each copy singly) and
over the chip-2 metal shot at 2.7x (`a_m.png`) sit on the features: VSS boxes and contacts on
RC, gate bands, node boxes east of RC with their buried contacts, the inverter's vertical gate
at the rail's west edge, the strips and plates, the tie boxes, the VCC boxes under RB.
`tools/cellcheck.py tl1_ua` and `tl1_ub` (clean shot; each copy brought back to the master's
orientation): 8-11 % of the blocks match badly, all of them under RB (where the boxes are
shared with `tl4`'s column and so differ from the master's), at the cell's edges or on dirt
(`cellcheck_tl1_ub_a.png`). `tools/rdp3_cmp.py 4900,3340:5210,3810 --offsets "0,0 0,477 0,954"`
(clean shot and chip-2 metal, 30 px blocks): the three copies agree with their median
everywhere except in the columns x 4900-4960 (RB). `tools/railprof.py 5088 5122 3380 3840`
(latch a under RC): VSS box, gate y 3455-3478, gate y 3498-3511, node y 3524-3568, gate
y 3569-3593, box, gate y 3707-3720, gate y 3751-3768, VSS box: the master's sequence.
The copies' offsets are not exact for every item: the thin metal the cell's pads belong to is
at x 4990 (the mirror gives 5001) and the VSS contacts' rings are about 10 px west of the
cell's rectangles; every drawn overlap holds.

**What each copy has of its own** (read here; "Seen" = how):

| Item | Latch a | Latch b | Latch c | Seen |
|---|---|---|---|---|
| data row (gate 1 of the three-input gate, the inverter's gate) | y 3452-3471 to pad (5452,3461), north end of a piece of T5 | y 3928-3947 from pad (5580,3938), south end of the piece of T8 from a's output pad | y 4404-4423, a 15 px step up at x 5565-5580 in the open, y 4385-4405 to pad (5665,4395), south end of a piece of T10 | `ra_a.png`, `rb_a.png`, `rc_a.png` 2.35x; pads `pa1.png`, `pb1.png`, `pc1.png` 4x, two shots |
| enable (gate 2 of the three-input gate and the series gate of the lower unit) | T6: pads (5494,3505) and (5494,3722); T6 ends on the lower pad; that row runs on east out of the strip | T7: pads (5538,3982) and (5538,4200); the metal runs on both ways | T4: pads (5407,4458) and (5407,4677); T4 ends on the lower pad | `pa1.png`, `pa2.png`, `pb1.png`, `pb2.png`, `pc1.png`, `pc2.png`; `follow.py 5492 3600 N/S`: (5492,2984)-(5491,3728) |
| three-input gate's node (box poly east of RC) | row y 3541-3560 to pad (5580,3550), south end of a piece of T8 | a stub with a closed round end at x 5212 | row y 4494-4513 to x 5552, south along x 5530-5552 under T7 (no contact), east along y 4580-4600 out of the strip | `pa1.png`, `pb2.png` (the stub), `pc1.png`, `pc2.png` (the corners; 12 px of field between the corner and the pad (5492,4590)) |
| clear (single pull-down east of RC in the lower unit) | pad (5233,3636) on T0 | pad (5233,4113) on T0, the same metal | pad (5492,4590) on T6's lower piece, which starts on a pad (5492,3872) with a row east out of the strip | `pa2.png`, `pb1.png`, `pc2.png`, `pc3.png` |
| output (lower node's box poly) | row y 3670-3690 to pad (5580,3680), north end of the piece of T8 to b's data | row y 4147-4167 to pad (5622,4160), south end of a piece of T9 | row y 4623-4643 east out of the strip, no pad | `pa2.png`, `pb1.png`, `pc3.png` |
| thin metal x 4990 (plate to third pull-down) | contacts (4990,3499), (4991,3705) | (4990,3976), (4991,4182) | (4990,4453), (4991,4659) | `pa4.png` 4x (a); b, c by the block comparison and `b_*.png`, `c_*.png`; `follow.py 4989 3600 N/S`: ends y 3500, y 3706 |
| thin metal x 5171-5185 (inverter output to the lower unit's second series gate; in the cell) | pads (5174,3366), (5183,3769) | 477 lower | 954 lower | `pa3.png` 4x (a) |
| VSS box below the stack | (5092-5145, 3780-3832), contact (5112,3802) | (5095-5150, 4257-4307), contact (5116,4282) | (5095-5150, 4735-4785), contact (5120,4758) | `pa3.png`, `pb2.png`, `pc2.png` 4x |
| VCC boxes under RB | inverter's: ring y 3416-3464; the lower two units': one long ring y 3520-3636 | one with `tl4`'s boxes (its contacts) | one with `tl4`'s boxes | `textmap.py 4900 3396 4960 3660 4`; `pa4.png` |

The rows pass under the tracks they cross at constant width without pads (the dark dots on
them in the clean shot lie in the gaps between the tracks: the gaps' marks, tracing guide
trap 2). The ends: every pad above has a ring with a bright centre in the chip-2 metal shot
and a green hole on a salmon pad in the clean shot; where a metal "ends" on a pad the ground
beyond is bare in the metal shot and khaki (never under metal) in the clean shot. The rows
that leave east were looked at at x 5610-5690 (`pc3.png`): constant width, no pad.

**Rails.** RC is drawn from y 3140 to its turn west at y 5882-5942 (looked at on `n_m.png`, `a_m.png` and the
overlays, and south of y 5045 as in the section on the foot; it runs on north unbroken into a
large undrawn metal at y 2200-2500) and is named `vss` **from structure** (it
carries the pull-downs' boxes); RB is `tl4`'s (drawn here only y 3232-3772, where `tl4` has not
drawn it).

### The NOR at y 3142-3352 (traced 2026-11-18 01:53 +0000: `tl1`'s NOR, mirrored)

`tl1`'s NOR (2540-2842 x 3558-3742; plain items there) mirrored and moved (x' = 7741 - x,
y' = y - 390; findcell 0.74) and laid over the clean shot and the chip-2 stripped shot at 4x
(`nor_a.png`, `nor_c2.png`): column, gate bands, node box, strip, plate, tab and tie box sit on
the features. Read here:

| Item | Reading | Seen |
|---|---|---|
| column x 5150-5192, y 3168-3330, in the open east of RC | diffusion, with two gate bands and the node box between | `px.py col 5160 3156 3344 4 acid,acid1b`: chip-2 stripped shot field to y 3160, tan (160/144/100) y 3176-3184, orange poly (174/134/70) y 3196-3204, tan y 3220-3228, the box y 3232-3264, orange y 3284-3296, tan y 3308-3316, field from y 3332 |
| arms onto the rail's VSS boxes (y 3168-3188, y 3310-3330) | diffusion from the column west to each box | `px.py row 3174` and `row 3320`, x 5124-5164: red over green by 13-50 without a break from x 5136 to x 5163 in the chip-2 stripped shot, where `row 3158` and `row 3336` have field (red minus green about 0) east of the box's edge |
| VSS boxes | above (5097-5140, 3148-3195), contact (5112,3168); below (5089-5143, 3307-3352), contact (5119,3332) | `pn2.png` 4x: ring in the metal shot, specks on tan in the clean shot; `nor_c2.png`: pits |
| gate 1, `tl5_w4160` | row y 3192-3212 from the pad (5580,3200), whose metal is an arm east to the north end of T9; T9 runs south without a pad to latch b's output pad (5622,4160) | `pn1.png` 4x; `textmap.py 5556 3176 5644 3240 3`: the ring between the pad's bright centre and the arm is 6 px in chip 2 (9 px in chip 1), the west ring 9 px; the clean shot is pink (under metal) without an open strip from the pad's east edge to T9; `ra_a.png`, `rb_a.png`: no pad on T9 between |
| gate 2, `tl5_w3550` | row y 3278-3298 from the pad (5580,3290), the north end of the piece of T8 that ends on latch a's pad (5580,3550); the row crosses T5's position, where there is no metal, in the open | `pn1.png` (the pad, bare ground north of it; the crossing at (5452,3290): one orange band in the metal shot) |
| output, `tl5_w3245` | buried contact (concentric box 5164-5194, 3230-3262), poly east along y 3235-3255 to the pad (5452,3245), the south end of a piece of T5 (bare ground south) | `pn1.png`, `pn2.png` |
| load | strip y 3241-3255 west under RC to a box under the thin metal x 5028-5046, strip under the plate (x 4967-5020, y 3218-3312) to the VCC box (4910-4963, 3232-3332; two rings (4932,3254), (4932,3305)); W/L about 23/53 | `nor_c2.png`: the plate is one orange area with the strip's edges as lines across it at y 3238 and y 3265; `pn2.png` |
| tie | the plate's tab (y 3288-3310) west onto a ringed box (5034-5058, 3285-3310) at the foot of a tail of the node | `nor_a.png`, `nor_c2.png` 4x: a box with a heavy outline in both stripped shots, as in the master, where it is drawn without `?`; drawn so here. The thin metal x 5028-5046 passes over it |

Widths: both gate rows end west at RC's east edge (x 5143; field under RC between the boxes and
the strip: pink on `nor_a.png`) and cross the whole column (W 42); east of the column they are
over field to their pads.

### The two inverters at y 4786-4912 and y 4916-5042 (traced 2026-11-18 01:56 +0000: `tl1`'s inverter, mirrored)

`tl1`'s inverter (2535-2835 x 4215-4345, a "rail gate": the pull-down lies under the rail between
the node and the VSS box) mirrored and moved (x' = 7743 - x, y' = y + 565 and y + 695), as a
cell `tl5_inv` placed twice, laid over the clean shot and the chip-2 stripped shot at 4x
(`inv_a.png`, `inv_c2.png`): node box east of RC with its buried contact, the strip west under
RC, gate band, VSS box, plate, tail and tie box sit on the features in both units.

| Item | Inverter 1 | Inverter 2 | Seen |
|---|---|---|---|
| gate | row y 4840-4858 from the east: under every track without a pad, out of the strip (`tl5_w4503`) | row y 4970-4988 from the pad (5538,4980), the south end of T7 (`tl4_w4068`, latch b's enable); the row runs on east through the pad, out of the strip | `rd_a.png` 2.35x; `pi1.png` 4x (the pads; the rows at x 5610-5690; bare ground south of the T7 pad) |
| the gate under RC | `px.py row 4849 5046 5216 6 acid1b,acid`: west end at x 5075, poly over a channel (229/166/120) x 5082-5136, open poly east of RC | `row 4979`: the same | `px.py col 5112 4800 4916 4`: node (tan) y 4820-4836, gate y 4844-4856, VSS box from y 4868 |
| east of RC the gate row lies on field | no diffusion edge across the band east of x 5145 in the chip-2 stripped shot; the node box above ends at y 4833 | the same | `inv_c2.png` |
| output | buried contact on the node box (5161-5205, 4794-4830), poly y 4798-4818 east out of the strip (`ras_o0_alt2`) | poly y 4928-4948 east to the pad (5407,4937), the north end of a piece of T4 (`tl5_w4937`) | `rd_a.png`, `pi1.png` |
| both rows of inverter 1 cross T4's position in the open (T4 has no metal y 4690-4925) | two unbroken orange bands in the metal shot | | `pi2.png` |
| VSS box | (5091-5145, 4860-4910), contact (5114,4884) | 130 lower, contact (5116,5013) | `pi2.png`: rings |
| VCC box | `tl4`'s (4908-4960, 4805-4878), its contact | of its own (4912-4962, 4935-4995), one ring (4918-4945, 4940-4985) | `pi2.png`, `inv_c2.png` |
| load tie | the master's `?` items: a ringed box (5000-5040, 4855-4885) at the tab's end | the same | `inv_c2.png`; not measured |

### The inverter at the top of the column, y 3040-3156 (traced 2026-11-18 02:08 +0000, by hand)

Read on `u1_a.png` (clean), `u1_c2.png` (chip-2 stripped), `u1_m.png` (chip-2 metal), all 4.8x of
4955-5217 x 3028-3163; overlay `u1_ov.png`; pads `pu1.png` (4x, two shots).

| Item | Reading | Seen (profiles: `tools/px.py`, clean shot / chip-2 stripped shot) |
|---|---|---|
| gate row y 3103-3122 | from the pad (5580,3113), the south end of T8's north piece (`tl4_w3113`), west across RC to an end at x 5048 | `row 3113 5034 5150 4`: field under W (185/128/130) to x 5046, poly from x 5050, bright over a channel (235/166/118) x 5074-5130 under RC; `pu1.png`: the pad, bare ground south of it; the row under T0 and T5 without a pad |
| under RC | node y 3086-3102, gate y 3108-3122, then diffusion without a break y 3128-3188 (the VSS region and the NOR's VSS box, contact (5112,3168)) | `col 5105 3040 3200 5`: olive (field under a rail) to y 3075, tan 197/166/139 y 3090-3100, salmon 240/174/122 y 3110-3120, tan 192-201/154-183/135 y 3130-3185 |
| west edge of the channel, about x 5068 | the VSS side is tan from x 5072 with a dark edge at x 5060-5068; the gate is bright from x 5074 | `row 3136 5040 5150 5`, `row 3113` |
| **the channel runs on east of RC to x 5190** | east of RC at x 5150 the gate lies between two diffusions: neck of the node y 3086-3094 (red minus green 14-24 in the chip-2 stripped shot), gate y 3106-3122 (orange), wing y 3134-3142 (16-23), field above y 3074 and below y 3154 | `col 5150 3050 3160 4`, `col 5170 3050 3166 4`; the diffusion's east edge is a dark line across the gate band at x 5188-5196 in the chip-2 stripped shot and the chip-2 metal shot (`row 3113 5140 5216 4 acid,metal`), orange poly on both sides of it |
| the wing | diffusion x 5140-5186, y 3130-3147, field east (x 5205) and south (y 3154-3162) of it; one with the VSS region under RC as far as can be told: the dark line at x 5134-5138 between them is on the gate poly as well (the rail's edge line) | `row 3138 5130 5215 5`: 166-170/141-153/97-102 (red minus green 13-29) x 5145-5180, 159/154 at x 5205 |
| node east of RC | neck y 3084-3098 from under RC (tan to x 5132, the rail's edge line, diffusion x 5144-5156), box (5152-5192, 3058-3098) with a buried contact (concentric rings) | `row 3093 5120 5212 4`; `u1_c2.png` |
| output | poly on the buried contact east along y 3063-3082 to the pad (5364,3070) on T3 (`tl5_w2722`); T3 passes through the pad | `pu1.png` 4x; `r1_a.png` |
| load | the node's strip y 3077-3095 west under W (tan y 3078-3087 at x 5042) and under the plate (x 4964-4999, y 3042-3140, in the open) onto `tl4`'s VCC box (4905-4965, 3068-3148) | `col 5042 3034 3104 3`; `col 5010 3056 3152 4`: at x 5010 diffusion only y 3076-3090, field below (green over red in the chip-2 stripped shot) |
| the load's width | **uncertain**: one edge line crosses the plate, at y 3066-3074, none lower (`col 4981 3034 3152 4`, and the three views); east of the plate the strip's bottom edge runs into the plate's east edge and down it (`u1_m.png`). Read as the diffusion filling the plate from y 3072 to y 3138: W/L about 66/35. The strip is drawn firm, the widening `?D` | |
| tie (`?`) | a bar from the plate's top east along y 3041-3053 (salmon y 3043-3049 at x 5042), and under W a small box with a heavy outline (5033-5052, 3056-3076) between the bar and the strip. Taken as the tie of the plate to the node; neither the bar's join to the plate nor the box is resolved: four `?` items | `col 5042`; `u1_a.png`, `u1_c2.png` |

Extracted: pull-down W/L 122/19 (gate `tl4_w3113`, node to VSS), load 70/33 with the uncertain
widening (18/35 without it). It is the strong version of the rail gate: the node drives T3,
3,400 px of metal.

### The north rows and the tracks (traced 2026-11-18 02:01 +0000: wiring)

Eight poly rows come out of `tl4`'s strip across x 4967, under metal (salmon) to x 5135 and in
the open from there, each to a pad with a contact. `north_a.png` (3.1x clean, x 4955-5275, with
`r9m`'s polys outlined), `north_c2.png` (4x, chip-2 stripped and metal: the five rows y 2722-2900
are straight orange rows at x 5125-5290; the blobs on them in the clean shot are dirt on chip 1),
`r0_a.png`, `r1_a.png` (2.35x clean), `n_a.png` (2.75x: the rows y 2940 and y 2985 at x 4895-5215);
overlay `ov_north.png`.

| Row | Pad (seen at 4x, chip-2 metal and clean) | Then | Net |
|---|---|---|---|
| y 2675-2694 | (5038,2685): the row ends on it (closed east end x 5058; 17 px of field to `tc2_o5175`'s step at x 5075-5090) | the thin metal W south (`pw1.png`) | `tl5_w4937` |
| y 2714-2733 | (5364,2722), north end of T3 (`pt1.png`) | T3 south: one metal to (5363,6114) (`follow.py 5365 2900 N/S`; candidate (5364,3086) = the pad (5364,3070) of the top inverter's output); drawn to y 5250 | `tl5_w2722` |
| y 2758-2777 | (5452,2767): its metal is an arm east to a corner (5538,2770) and T7 south (`pt1.png`: both tiles; the clean shot is pink from the pad to the corner) | latch b's two enable pads, the pad (5538,4980) | `tl4_w4068` |
| y 2801-2820 | (5407,2810), north end of T4's north piece (`pt1.png`) | (5406,2810)-(5404,4682) (`follow.py 5408 3400 N/S`): latch c's two enable pads | `tl3_e4243` |
| y 2846-2865 | (5580,2855), north end of a piece of T8 (`pt2.png`) | (5582,2852)-(5581,3120) (`follow.py`): to the pad (5580,3113) of the top inverter's gate row. The follower's candidate (5580,2942) is a speck (`pw2.png`) | `tl4_w3113` |
| y 2890-2909 | (5452,2900), north end of T5's north piece (`pt2.png`) | the NOR's output pad (5452,3245) | `tl5_w3245` |
| y 2930-2950 | (5165,2945): its metal is an arm east onto the north end of T0 (`pt2.png`: bright metal leaves the ring east; `follow.py 5234 4300 N`: corner (5233,2944), west end (5161,2944)) | T0 south through the clear pads (5233,3636) and (5233,4113), on to a corner (5231,6026), west, south to (5145,6113) (`follow.py`); drawn to y 5250 | `rst_a` |
| y 2975-2994 | (5494,2985), north end of T6's upper piece (`pt2.png`) | latch a's two enable pads | `tl5_w3505` |

The tracks, as drawn (each piece one metal; "to y 5250" means it runs on south of what was
looked at; the 2.35x clean views show every piece as one pink band without a pad other than
those listed):

| Track | Piece | Pads | Net |
|---|---|---|---|
| T0 x 5233 | from the arm at y 2945 to a corner (5233,6027), west, south at x 5150 to its south pad | (5165,2945), (5233,3636), (5233,4113), (5148,6108) | `rst_a` |
| T3 x 5364 | y 2710-6120 | (5364,2722), (5364,3070), (5363,6108) | `tl5_w2722` |
| T4 x 5407 | y 2798-4689 | (5407,2810), (5407,4458), (5407,4677) | `tl3_e4243` |
| T4 | y 4925-5249 | (5407,4937), (5407,5237); the speck (5407,5028) is not a contact (`pw2.png`) | `tl5_w4937` |
| T5 x 5451 | y 2888-3257 | (5452,2900), (5452,3245) | `tl5_w3245` |
| T5 | y 3450-5771 | (5452,3461), (5451,5759) | `tl5_w3461` |
| T6 x 5494 | y 2973-3734 | (5494,2985), (5494,3505), (5494,3722) | `tl5_w3505` |
| T6 | y 3860-5423 | (5492,3872), (5492,4590), (5493,5411) | `c4l_gab` |
| T7 x 5538 | from the arm at y 2769 to y 4992 | (5452,2767), (5538,3982), (5538,4200), (5538,4980) | `tl4_w4068` |
| T8 x 5581 | y 2843-3125 | (5580,2855), (5580,3113) | `tl4_w3113` |
| T8 | y 3278-3562 | (5580,3290), (5580,3550) | `tl5_w3550` |
| T8 | y 3668-3950 | (5580,3680), (5580,3938) | `tl5_w3680` |
| T8 | y 4509-5457, a corner (5581,5457) and west | (5580,4521), (5538,5457) | `c4l_l3` |
| T9 x 5625 | from the arm at y 3202 to y 4172 | (5580,3200), (5622,4160) | `tl5_w4160` |
| T9 | y 4425-5501, a corner (5625,5501) and west | (5623,4437), (5493,5500) | `tl4_w5068` |
| T10 x 5667 | from the strip's east edge along y 3650-3668 to a corner (5668,3659), south to y 4407 | (5665,4395) | `tcw_m6320` |
| T10 | y 4468-5545, a corner (5667,5545) and west | (5666,4480), (5538,5544) | `tc1_o3527` |
| x 5189 | y 5399-5982, a corner (5189,5982) and west out of the strip | (5190,5411) | `c4l_gab` |
| x 5627 | from the pad (5493,5674) east along y 5676, a corner (5627,5676), south, a corner (5627,6150), east | (5493,5674), (5667,6150) | `ck_out` |

T1 (`res_b`) and T2 (`lpstb_b`) are `trunks`' (to their pads (5190,6065) and (5232,6105)); T7 ends on
the pad (5538,4980).

**West of the edge** (traced 2026-11-18 02:43 +0000 for the row y 2767; the rest seen, not drawn). Each
north row ends west of x 4967 on a pad with a contact in `tl4`'s strip. The five nearest on
`j_w2.png` (4x, clean and chip-2 metal: ring with a bright centre, green hole, closed west end
of the pad), the others on `j_w1.png`, `j_w1m.png` (2.1x: below 4x, so nothing is drawn from them):

| Row | Pad | The pad's metal (`follow.py` from the pad) | State |
|---|---|---|---|
| y 2685 `tl5_w4937` | (4865,2685) | west to (4252,2637): `r9m`'s "line 3", to the pad (4270,2640) of the middle cluster | seen at 4x; not drawn |
| y 2722 `tl5_w2722` | (4820,2722) | west to (4230,2684): `r9m`'s "line 4", to the pad (4232,2683) | seen at 4x; not drawn |
| y 2767 `tl4_w4068` | (4910,2767) | two metals: west along y 2767 to a pad (4534,2769) (not drawn), and **south, west, south, west and south as `tl4`'s track x 4625 to the pad (4625,4068): `tl4_w4068`** | **drawn** (below) |
| y 2810 `tl3_e4243` | (4865,2810) | west to a pad (4578,2814) | seen at 4x; not drawn |
| y 2855 `tl4_w3113` | (4820,2855) | west to a pad (4534,2857); `tl4`'s `tl4_w3113` track ends on a pad (4455,2856) 80 px further west, a poly between them in the 2.1x view | seen; not drawn, not a join |
| y 2900 `tl5_w3245` | (4645,2900), which is the east end of the metal from the corner (4586,2896) of `tl4`'s track x 4581 (`tl5_w3245`); `tl5_tracks.py v 4581 2890 4695`: one metal, no hole | | **not drawn**: between the pad's east edge (x 4664) and the row's cream (from x 4680) there are 12 px of darkness in both stripped shots (`px.py row 2900 4636 4712 4`), poly-coloured in both metal shots (147/99/47, 155/87/47 against bare ground 165/140/88): a gap mark across a continuous poly, very probably, which would make **`tl5_w3245` = the wire `tl4` called w4718**; a join through a dark gap stays out until it is read another way |
| y 2940 `rst_a` | (4537,2940), the north end of `tl4`'s track x 4537 (`rst_a`) | south as that track to `tl4`'s drawn piece (from y 3895); a second pad on it at (4537,3463) | **drawn** (below) |
| y 2985 `tl5_w3505` | about (4450,2985) | not followed | 2.1x only: not drawn |

So of the four joins the first run listed as believed, none stands as listed: `tl4_w4068` was
put on the row y 2985 from the y of its corner (4630,2988), and it is on the row y 2767
(`tl4_w4068`), by a metal that runs on from that corner east and north; `rst_a` (row y 2940) is right and is now drawn; `tl5_w3245` (row y 2900) is probably right
and is not drawn; `tl4_w3113` (row y 2855) ends
80 px short of the row's pad.

**The drawn join, the wire `tl5` called w3982 = `tl4_w4068`** (alias in `trace/tl5.txt`; `tools/unsure.py`: no
`?` item on the path):

| Item | Reading | Seen |
|---|---|---|
| row y 2758-2777 west of the edge | 40 px to the pad (4910,2767) | `j_w2.png` 4x |
| the pad's two metals | from the west along y 2767 and from the south at x 4900-4915: the ring between the pad's bright centre and the metal is 9 px on the west side and 10-12 px on the south side in both chips, and the clean shot is pink (never open) from the pad to the metal south of it | `textmap.py 4876 2740 4942 2812 3`; `follow.py 4910 2830 N`: ends (4907,2766) |
| the path | south over the rows y 2810 and y 2855, corner (4907,2901), west along y 2893-2909 (on top of the row y 2900, no contact), corner (4690,2901), south, corner (4690,2988), west, corner (4625,2988), south at x 4625 to `tl4`'s drawn metal (from y 4056) and its pad (4625,4068) | `follow.py 4910 2830 S`: corners (4900,2900), (4690,2901), (4685,2987), (4625,2988), end (4625,4292); corners at 4x: `j_c2.png` (two shots), `j_c1.png`, `j_c1b.png` (four shots); the track x 4625 on `j_s1.png` (1.2x, three shots: one metal, one pink band, no pad); overlay `ov_j1.png` 3.3x |
| metal test and holes | `tl5_tracks.py v 4907 2775 2905`, `h 2901 4685 4910`, `v 4689 2896 2995`, `h 2988 4620 4692`, `v 4625 2985 4060`: no green hole on any piece; the longest stretch without metal in both chips is 17 px (y 2970-2986 on x 4689, a row's edges) | text |
| not the neighbouring metal | the pad (4645,2900) 45 px west of the corner (4690,2901) belongs to the track x 4581: 30 px without metal between its centre and the corner, against a 12 px ring on its west side | `px.py row 2900 4636 4712 4 metal,metal1`; `j_c1.png` |
| not drawn | the pad's other metal, west along y 2767 to a pad (4534,2769): more of the same net | `follow.py 4880 2767 W` |

So **`tl4`'s latch (y 3906-4390) and latch b here are open at the same time**, and
`tl5_w4937` = NOT `tl4_w4068`.

**The drawn join, `rst_a`** (traced 2026-11-18 02:48 +0000; alias in `trace/tl5.txt`;
`tools/unsure.py`: no `?` item on the path):

| Item | Reading | Seen |
|---|---|---|
| the pad (4537,2940) | ring with a bright centre, green hole on a cream pad; bare ground north of it, the metal goes on south: the north end of the track x 4537 | `j2_a.png` 4x, clean, chip-2 stripped, chip-2 metal; `tl5_tracks.py v 4537 2925 3900`: hole at y 2946 |
| the row y 2930-2950, x 4553-4967 | one poly, at the same y in every cut: along the north edge of the wide metal foot (no metal over the row at x 4694-4947 in either chip) y 2935-2995 from x 4950 to x 4725, a gap mark at x 4704-4708, under the metal x 4690, in the open x 4604-4672, under the metal x 4581, a gap mark at x 4556-4566, the pad | `j2_b.png` (4x, clean and chip-2 stripped: x 4700-4970), `j_c1.png`, `j_c1b.png` (4x, four shots: x 4565-4725), `j2_a.png` (x 4495-4655); `px.py row 2940 4548 4736 4 acid1b,acid`: cream or open poly (red over green by 40-60) at every sample but the three marks, no sample green or pink; `tl5_tracks.py rows col 2880 3004 3` at 23 cuts x 4960-4430; overlay `ov_j2.png` 2.7x |
| the mark beside the pad (4556-4566, 2932-2945) | a dark blob in the 17 px gap between the pad's metal and the metal x 4581, with cream above and below it inside the row (181/142/112 at y 2935, 165/143/116 at y 2947) and poly-coloured in both metal shots (chip 2 120-137/86-103/38-50, chip 1 114-140/62-77/30-40, against bare ground 147/130/67 and 117/93/74 at y 2920) | `px.py col 4560 2920 2960 3 acid1b,acid,metal,metal1`; `col 4564` |
| the track x 4537, y 2940-3900 | one metal x 4528-4545; no stretch without metal in both chips over 16 px; holes only at the north pad and at (4537,3463) | `tl5_tracks.py v 4537 2925 3900`; `j2_s.png` (1.3x, three shots); `tl4`'s notes (`follow.py`: y 2938 to y 4814) |
| not drawn | the second pad (4537,3463) of the track: a ring in both metal shots, its poly east along y 3450-3470 (`tl4`'s field) | `j2_s.png` |

So **latches a and b, `tl4`'s latch and `tl4`'s cross-coupled pair have one clear** (`rst_a`).

**RC north of the column** (traced 2026-11-18 02:43 +0000). RC runs north from y 3140 over the north rows and
`r9m`'s rows (poly over field under it: `railprof.py 5088 5122 2480 3150`; olive field
148/143/107 at y 3000-3068, `px.py col 5105 2996 3070 6`) and joins the lower edge of the wide
metal band y 2180-2500 at y 2505 (`tl5_tracks.py v 5104 2505 3140 --half 10`: no stretch
without metal in both chips over 15 px; chip 2 is dark for 8 px at y 2505-2510 where chip 1 is
bright: an edge under the band's rim; `rc_n2.png` 1.75x, `rc_n.png` 0.62x). No ring on it and no
speck under it between. **No block has drawn the band** (no metal item lies on it between
x 2200 and x 13000), so RC does not reach a named supply: `vss` by structure only. Seen and not
drawn: a second finger of the band, x 4950-5000, y 2505-2990 (half in `tl4`'s strip), without a
contact (`tl5_tracks.py v 4975 2505 3000 --half 10`), whose foot runs west as a wide metal
y 2935-2995 to x 4725, the top of `tl4`'s rail RA (`ov_j1.png`): RA and RC hang on the same band.

**T10's north piece** (traced 2026-11-18 02:43 +0000): from the pad (5665,4395) north to a corner (5668,3659)
and east along y 3650-3668 out of the strip (`t10_n.png` 4x, clean and chip-2 metal: bare ground
north and west of the corner, one pink L band; `follow.py 5667 4300 N`: corner (5677,3660), east
to (5801,3657); `tl5_tracks.py v 5667 3630 4400`: no stretch without metal over 11 px between
the corner and the pad's ring, no hole but the pad's; it crosses the rows y 3722 and y 3872
without a pad). So `tcw_m6320`, latch c's data, comes from the east.

### The thin metal W (traced 2026-11-18 02:01 +0000: wiring)

One metal x 5031-5045 over the whole column, from a pad with a contact (5038,2685) on the row
y 2685 to a pad with a contact (5038,5237); that pad's poly runs east along y 5227-5247 to the
pad (5407,5237), where T4's south piece from inverter 2's output pad ends.

| Item | Reading | Seen |
|---|---|---|
| both end pads | ring with a bright centre, green hole on a salmon pad; the metal ends on each (bare ground beyond) | `pw1.png` 4x, two shots |
| between the ends | constant width; no widened pad and no ring with a bright centre anywhere | `w_m.png`, `w_a.png` (3.3x strips, chip-2 metal and clean shot, y 2670-5250); `a_m.png` 2.7x |
| dark stretches | over the loads' tie boxes and tails (y 3265-3320 at the NOR, y 3495-3530 and y 3590-3640 in latch a, and the same places in b and c, y 4855-4885 and y 4985-5015 at the inverters): a thin metal over a buried contact or along an edge (tracing guide, trap 22); and y 3045-3100 over the top inverter's tie box and strip (no pad, no bright centre: `u1_m.png` 4.8x) | `w_m.png`; no green hole under W at the NOR's tie (`nor_a.png` 4x) |
| the row y 5237 | under RC it lies on field (pink above and below, plain salmon; no box, no ring); under T0-T3 no pad; in the open one orange band | `pw2.png`, `pw1.png` 4x; `rd_a.png` |
| `follow.py 5035 3450 N` | to (5037,2680); its contact candidates (y 3427, 3363, 3270, 3117, 3055) and those of `tla_contacts.py` lie on diffusion crossings and tie boxes | text |

So W is not connected to any unit of the column it runs over (as traced): it is the return
path of `tl5_w4937` north.

### The foot, the rows under it and the poly bus (traced 2026-11-18 02:36 +0000: wiring, no transistor)

`tools/findcell.py` was not run here: there is no unit south of y 5045, only rails, tracks, rows
and pads (`f_sv1.png` 0.85x, `f_foot.png` 2.1x, `f_r1_acid1b.png`, `f_r1_metal.png`,
`f_s1_acid1b.png`, `f_s1_metal.png` 1.7x; overlays `ov_rows.png`, `ov_bus.png` 1.7x, all blocks'
geometry). `tools/tl5_tracks.py` (new) gives, for a straight piece of track, the follower's metal
test in both metal shots and the clean shot's green holes, and for a field of rows a text cut.

**The foot (y 5045-5440).** RC runs on south over bare field; no box, no contact, no poly but W's
row y 5237. Then RC crosses the eight rows and `tla`'s `rcs_e4` row (y 5838-5857), and at
y 5882-5942 turns west as one rail about 60 px wide, out of the strip, with two polys under it.

| Item | Reading | Seen |
|---|---|---|
| under RC, y 5050-5440 | field: olive 140/146/106 without a dark line, against tan 192/161/137 on the VSS box at y 5000 | `px.py col 5105 5000 5450 10 acid1b,metal,metal1`; `f_foot.png` |
| RC's dark specks (5090,5165), (5088,5280), (5110,5335), (5105,5370) | on the metal only: nothing under them in the clean shot (no box, no speck) | `f_foot.png`, two shots |
| under RC at the rows | every row is poly over field (no diffusion between the rows) | `railprof.py 5088 5122 5030 5830` |
| RC's turn | the rail's west-going part is metal from y 5882 to y 5942 at x 5000 (bare ground 160-172/142/86 at y 5868-5872 and from y 5956; the dark lines at y 5880-5892, 5900-5904, 5924 and 5940-5944 are the edges of the two polys under it; the clean shot is pink or cream, never open, from y 5872 to y 5948); its outer corner at (5128,5945) | `px.py col 5000 5856 5960 4 metal,metal1,acid1b`; `row 5920 5060 5150 5`; `h_rc_metal.png`, `h_rc_acid1b.png` 4x |
| RC's supply | still **by structure only**: the rail leaves the strip west at (4967, 5882-5942) into `tl4`'s strip, where nothing is drawn | |

**The rows under the foot (y 5400-5780).** Eight poly rows cross the west edge and run straight
east under RC, the metal x 5189 and the tracks. None crosses a diffusion.

| Row | West | East end | Then | Net |
|---|---|---|---|---|
| y 5402-5421 | starts on a pad (5190,5411), the north end of the metal x 5189 (bare ground north and west of the pad) | pad (5493,5411), the south end of T6's lower piece (bare ground south and east) | the metal x 5189 south to a corner (5189,5982), west along y 5975-5989 out of the strip (`follow.py 5187 5500 S`: on to (4924,5992), south, east along y 6370) | `c4l_gab` (latch c's clear) |
| y 5447-5467 | edge | pad (5538,5457) | metal east, corner (5581,5457), north as T8's south piece to its north pad (5580,4521); that pad's row east along y 4510-4530 out of the strip | `c4l_l3` |
| y 5490-5510 | edge | pad (5493,5500) | metal east, corner (5625,5501), T9's south piece north to its pad (5623,4437); row east along y 4427-4447 out of the strip | `tl4_w5068` |
| y 5534-5553 | edge | pad (5538,5544) | metal east, corner (5667,5545), T10's south piece north to its pad (5666,4480), which lies on the strip's east edge (x 5650-5690); its poly leaves east | `tc1_o3527` |
| y 5576-5594 | `bw`'s `rc_stepreq_n` row: through the strip without a pad (theirs) | | | |
| y 5621-5641 | edge | pad (5538,5631) | metal east along y 5632 to a pad (5666,5632) on the east edge; its poly leaves east | `rst_ck` |
| y 5665-5684 | edge | pad (5493,5674) | metal east, corner (5627,5676), south over `amrw`'s four rows (no pad, no hole), corner (5627,6150), east to a pad (5667,6150) on the east edge; its poly leaves east | `ck_out` |
| y 5708-5727 | edge | no pad: a corner at x 5485-5507 and south, under `amrw`'s metal x 5495 from y 5850, a corner at y 6228-6248 and east, in the open from x 5600, out of the strip | | `rcs_mv` |
| y 5751-5770 | edge | no pad: a corner at x 5402-5424 and south as the bus line x 5412 | | `bd1_n2` |

Seen: the pads at 4x in the clean shot and the chip-2 metal shot, each with a ring with a bright
centre and a green hole on a cream pad, and the ground 50 px beyond each: `g_a.png` ((5493,5411),
(5538,5457), (5493,5500), (5538,5544)), `g_b.png` ((5538,5631), (5493,5674), the corner of the
row y 5717), `g_c.png` ((5190,5411)), `g_d.png`, `g_f.png` (T5's south pad and the corner of the
row y 5761), `g_e.png` (the three nested corners of T8-T10, three separate pink bands; the pad
(5666,5632)), `g_n.png` (the three north pads and their rows east, to x 5700). The west edge:
`g_w2.png` (4x, clean, chip-2 stripped and chip-2 metal, x 4927-5037): eight straight rows that run
on west under RB's metal. That the rows keep their order from the edge to the pads:
`tl5_tracks.py rows col 5396 5780 3` at 21 cuts from x 4975 to x 5538, every row at the same y
in every cut (no hop steps a track).
**T5's south pad is not on the row y 5761**: the row's corner is 12 px west of the pad
(`px.py row 5760 5390 5475 4 acid1b,acid,metal`: clean shot green over red at x 5426-5430, the
chip-2 stripped shot dark, 85/60/31 to 57/69/38, at x 5426-5434 with orange on neither side of
it joined; `g_f.png` 4x in both stripped shots). The pad's own poly runs south from it.

**The poly bus (y 5880-6350).** Ten vertical polys; nine cross the south edge y 6350.

| Line (x at y 6350) | From | Net |
|---|---|---|
| 5063 | a poly from the west edge along y 5926-5946, under RC's turned rail, corner at x 5053-5073 | `tl3_w3982` |
| 5107 | a poly from the west edge along y 5880-5900, under the rail, corner at x 5097-5117 | `rcs_x1` |
| 5150 | T0's south pad (5148,6108) | `rst_a` (the clear of latches a and b) |
| 5193 | `trunks`' pad (5190,6065) | `res_b` |
| 5237 | `trunks`' pad (5232,6105) | `lpstb_b` |
| 5281 | `tla`'s line (drawn there) | `rcs_e4` |
| 5365 | T3's south pad (5363,6108) | `tl5_w2722` (the strong inverter's output) |
| 5412 | the row y 5761 | `bd1_n2` |
| 5453 | T5's south pad (5451,5759) | `tl5_w3461` (latch a's data) |
| 5497, to y 6238 only | the row y 5717; east along y 6228-6248 out of the strip | `rcs_mv` |

Seen: `h_rc_acid1b.png`, `h_rc_metal.png` (4x: the two corners under the rail, nested, 24 px of
pink between them; both polys on to the west edge), `p2_a.png` (4x: T0's corner and south pad,
`trunks`' two pads and their stems), `p2_b.png` (T3's pad; the lines x 5412 and x 5453 pass it),
`p2_d.png` (the corner at (5497,6238): closed west end, pink to the line x 5453), `p2_c.png` (the
row y 6238 to x 5700; the pad (5667,6150)), `p2_s1.png`, `p2_s2.png` (4x, clean and chip-2
stripped: the nine lines at y 6288-6363, straight, on south under the metal y 6370), `p2_e.png`
(3x, three shots). Straightness: `tl5_tracks.py rows row 5040 5520 3` at 13 cuts from y 5800 to
y 6348, every line at the same x. **`amrw`'s four counter metals cross the bus without a
contact**: `tl5_tracks.py h 6153 5030 5450`, `h 6196 5000 5495`, `h 6240 5030 5540`,
`h 6283 5000 5582`: no green hole under any of them, and no stretch without metal longer than
17 px (the lines' edges); so nothing here joins `c4l0`..`c4l3`, and `amr_eq_r3` is not in the
strip's drawn part (its metal crosses at y 6412, south of the region).

**Track pieces: the metal test** (`tl5_tracks.py v X Y0 Y1`; both metal shots; a stretch without
metal in both is given when 8 px or longer):

| Piece | Longest stretch without metal in both | Green holes |
|---|---|---|
| T8 south, x 5581, y 4500-5470 | 16 px (y 4532-4547: the north pad's ring) | 4527 (the pad) |
| T9 south, x 5625, y 4420-5515 | 20 px (y 4442-4461: the north pad's ring and the row's edge) | 4440 (the pad) |
| T10 south, x 5667, y 4460-5560 | 16 px (y 4488-4503: the pad's ring) | 4483 (the pad) |
| T6 lower, x 5494, y 4600-5425 | 19 px (y 4834-4852: inverter 1's rows; review round 1), 18 px (the south pad's ring) | 5416 (the pad) |
| T5, x 5451, y 5240-5770 | 18 px (the south pad's ring); 8-11 px at each row edge | 5762 (the pad) |
| T3, x 5364, y 5240-6125 | 18 px (y 5586-5603, over `bw`'s row: below), 19 px (the pad's ring) | 6110 (the pad) |
| T0, x 5233, y 5240-6035 | 16 px (y 5746-5761) | none |
| x 5189, y 5400-5995 | 17 px (y 5702-5718), 16 px (y 5659-5674) | 5417 (the pad) |
| x 5627, y 5680-6150 | 14 px | none |
| the horizontal pieces (y 5457, 5501, 5545, 5632, 5676, 5982, 6027, 6150) | 15 px (each pad's ring) | none |

The four longest stretches that are not pad rings were looked at at 5x in both metal shots
(`k_gaps_metal.png`, `k_gaps_metal1.png`): metal on both sides of a row's two edge lines in each.
**T3 over `bw`'s row (5362,5590)** is dimmer than the other crossings in both chips, with a dark
spot; `textmap.py 5338 5562 5392 5612 3` against the same row under T0 (`5207 5562 5261 5612`):
the clean shot is the same protected poly (6-7) with no green hole, the row is not widened, the
metal is 9-C where the reference is C-D. Read as a blemish on the metal, not a contact; if it
were one, `tl5_w2722` would be `rc_stepreq_n`.

## Self-check (tracer, before any review)

**Ends.** Every wire end drawn, and how it was looked at (all at 4x in the chip-2 metal shot and
the clean shot unless noted): the pads in the tables above (`pa1`-`pa4`, `pb1`, `pb2`, `pc1`-`pc3`,
`pn1`, `pn2`, `pi1`, `pi2`, `pt1`, `pt2`, `pw1`, `pw2`, each `.png`; latch b's and c's thin-metal
pads only on the 3.6x overlays and by the block comparison with latch a's); the stub of latch b's node
(`pb2.png`); the eight rows at the west edge (x 4955-4967 on `north_a.png` 3.1x and `n_a.png`
2.75x: under metal, running on west; **below 4x**: the edge itself was not looked at closer); the
seven rows at the east edge (`pc3.png`, `pi1.png` 4x at x 5610-5690); no track piece is drawn short of its end.
**Widths.** The latches' transistors are the cells' (compared block by block with the master and
with each other; one rail profile); the NOR's two gates and the inverters' gates were profiled
past both ends (tables above). No row drawn here crosses a diffusion outside the units: the
rows lie on field in the bus field and under RC at y 5237 (`pw2.png`).
**Weak spots.** (0) The top inverter: the load's width and its tie (`?`); that the wing and the
node box east of RC are one diffusion with the parts under RC is inferred across the rail's edge
line (the transistor at x 5150, east of RC, does not depend on it for its channel, only for its
VSS). (1) The copies' load ties are `?` (not measured here). (2) The NOR's tie is
drawn firm from two 4x views, as in the master. (3) T0, T3, T4, T5, T6, T7 between their pads
rest on the 2.35x clean views (pink band, no pad) and `follow.py`, not on 4x views of every
crossing. (4) The join of the pad (5580,3200) to T9 and of the pads (5452,2767), (5165,2945) to
T7 and T0 are arms read at 4x and, for T9, measured. (5) The data row of latch c steps 15 px at
x 5565-5580 in the open: one poly in the chip-2 metal shot at 4x (`pc1.png`); not profiled.
**Omissions** inside what is traced: an outlined open box at (5425-5520,
2790-2840) between T4's north pad, T7's arm and the row y 2855: open ground with pale blobs
(dirt on chip 1; plain in the chip-2 shots); khaki boxes along the tracks (ra_a.png and the
like) are the open ground where a track has no metal; the dark round blob at (5592,3575) in the
chip-2 metal shot south of the pad (5580,3550) has nothing under it in the clean shot (dirt);
the pads at x 5560-5683, y 4420-4540 are the north pads of T8's, T9's and T10's south pieces (drawn).

**South of y 5045 (2026-11-18 02:36 +0000).**
*Ends.* Every pad, corner and edge crossing drawn there is in the "Seen" lines of the section on
the foot: 15 pads (and `trunks`' two) at 4x in two shots with the ground beyond them; the west edge at 4x in three
shots (`g_w2.png`; the two polys and the two metals at y 5880-5990 on `h_rc_*.png`, x 4950 on);
the east edge on `g_n.png`, `g_e.png`, `p2_c.png` (x 5700); the south edge on `p2_s1.png`,
`p2_s2.png` (y 6363). Three pads lie on the east edge itself ((5666,4480), (5666,5632),
(5667,6150): poly x 5650-5690); they are drawn to x 5683 and their polys' way east is the
neighbour's.
*Widths.* No transistor is drawn south of y 5045 and none was found: no row or bus line crosses
a diffusion (`railprof.py` under RC; `tools/opendiff.py 4967 5045 5683 6350`: nine green groups,
all strips 8-17 px wide beside pads or between metals; `px.py pt` in the chip-2 stripped shot at
eight points of the large khaki areas: red minus green 0-8, field).
*Weak spots.* (1) T3 over `bw`'s row at (5362,5590): read as a blemish (above). (2) The rows
between x 5130 and x 5470 rest on the 1.7x views and the text cuts, not on a 4x view of every
crossing; the pads there are at 4x. (3) The bus lines between y 6130 and y 6290, under `amrw`'s
four metals, rest on the 1.7x views, the text cuts and the contact scan. (4) The lines x 5193
and x 5237 join `trunks`' stubs by overlap at y 6150-6160 (`p2_a.png`: one stem each).
*Omissions.* Rings in the metal shots without a drawn item: none (specks on RC, on the metal
x 5189 at (5175,5905) and on T0 at (5235,5880): no hole under them, `tl5_tracks.py`). Outlines in
the clean shot without a drawn item: the khaki boxes between rows and tracks (open field between
protected margins: tracing guide trap 2); three small rings at (5063,5957), (5083,5957),
(5108,5957) and one at (5557,6237), each in a 25 px gap between two metals and absent in the
chip-2 shots (gap marks); an irregular outline at (5600-5690, 6175-6220) and blobs at
(5540-5600, 5750-5775), in the clean shot only (bare ground in the chip-2 metal shot, field in
the chip-2 stripped shot: `px.py pt 5630,6190 5660,6210 5640,6200`).
*Track fields.* The table of metal tests above; each pad's track: the three nested corners on
`g_e.png` and `follow.py 5625 5300 S` (to (5487,5502)), `5667 5300 S` (to (5532,5545)),
`5581 5300 S` (corner (5576,5460)), `5560 5672 E` (corner (5626,5681), end (5634,6161)).

**The join, RC north, T10 north (2026-11-18 02:43 +0000).**
*Ends.* For the second join: the pad (4537,2940) at 4x in three shots, the row end to end at 4x
(three views, two to four shots each), the track's south end on `tl4`'s drawn metal (overlap
y 3895-3900). For the first: the pad (4910,2767) and both its metals (`j_w2.png` 4x, `textmap.py`); the four corners
of the path at 4x in two to four shots; its south end is `tl4`'s drawn metal and pad (4625,4068)
(overlap y 4056-4062; `j_s1.png`). T10's corner and the edge at x 5700 (`t10_n.png` 4x). RC's
north end on the band: 1.75x and a profile only (**below 4x**; it decides nothing, the band
being undrawn). *Widths.* No transistor added. *Weak spots.* The gap mark beside the pad (4537,2940) (measured, table above). The tracks
x 4625 between y 3000 and y 4056 and x 4537 between y 2960 and y 3895 rest on the metal test, the hole scan, the follower and a 1.2x strip, not on 4x
views of each row crossing. *Omissions.* The pad (4910,2767)'s west metal and the pad (4537,3463) (Not done); on `ov_j1.png` the
other rings are `tl4`'s pads (4865,2810), (4820,2855), (4645,2900), not drawn by anyone.
*Track fields.* The table of the drawn join; the track x 4625 against its neighbour x 4581 on
`j_s1.png` and `j_c1.png` (the corner (4625,2988) is the inner one, x 4581's corner (4586,2896)
lies outside it).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tl5_w4937` | poly | (4967, 2675-2694) | out | inverter 2's output, from the thin metal W's north pad |
| `tl5_w2722` | poly | (4967, 2714-2733) | out | the row of T3's north pad |
| `tl4_w4068` | poly | (4967, 2758-2777) | ? | latch b's enable (T7); the row runs on 40 px to the pad (4910,2767): the net is `tl4_w4068` |
| `tl4_w4068` | metal | (4898, 2760-2775) | ? | the other metal of the pad (4910,2767), which runs west along y 2767 to a pad (4534,2769): not drawn west of the pad |
| `tl3_e4243` | poly | (4967, 2801-2820) | in | latch c's enable (T4's north piece: only gates on it) |
| `tl4_w3113` | poly | (4967, 2846-2865) | ? | the row of T8's north pad |
| `tl5_w3245` | poly | (4967, 2890-2909) | out | the NOR's output |
| `rst_a` | poly | (4967, 2930-2950) | ? | the clear of latches a and b (T0); the row runs on west to the pad (4537,2940) of `tl4`'s track x 4537: the net is `rst_a` |
| `tl5_w3505` | poly | (4967, 2975-2994) | ? | latch a's enable (T6) |
| `tl5_w3505` | poly | (5683, 3712-3732) | ? | latch a's enable: the row of its second pad runs on east |
| `tcw_m6320` | metal | (5683, 3650-3668) | in | latch c's data: T10's north piece leaves east |
| `c4l_gab` | poly | (5683, 3862-3882) | ? | latch c's clear: the row from the north pad of T6's lower piece |
| `tl5_w4503` | poly | (5683, 4580-4600) | out | latch c's inverse output |
| `tcw_c` | poly | (5683, 4623-4643) | out | latch c's output |
| `ras_o0_alt2` | poly | (5683, 4798-4818) | out | inverter 1's output |
| `tl5_w4503` | poly | (5683, 4840-4858) | in | inverter 1's gate |
| `tl4_w4068` | poly | (5683, 4970-4988) | ? | latch b's enable: the row of T7's south pad (5538,4980) runs on east |
| `tl4_w5068` | poly | (5683, 4427-4447) | ? | the row of T9's south piece's north pad (5623,4437) |
| `tc1_o3527` | poly | (5683, 4464-4496) | ? | the pad (5666,4480) of T10's south piece, on the edge |
| `c4l_l3` | poly | (5683, 4510-4530) | ? | the row of T8's south piece's north pad (5580,4521) |
| `c4l_l3` | poly | (4967, 5447-5467) | ? | the row of the pad (5538,5457) |
| `tl4_w5068` | poly | (4967, 5490-5510) | ? | the row of the pad (5493,5500) |
| `tc1_o3527` | poly | (4967, 5534-5553) | ? | the row of the pad (5538,5544) |
| `rst_ck` | poly | (4967, 5621-5641) | ? | the row of the pad (5538,5631) |
| `rst_ck` | poly | (5683, 5616-5649) | ? | the pad (5666,5632), on the edge |
| `ck_out` | poly | (4967, 5665-5684) | ? | the row of the pad (5493,5674) |
| `ck_out` | poly | (5683, 6134-6166) | ? | the pad (5667,6150), on the edge |
| `rcs_mv` | poly | (4967, 5708-5727) | ? | a row without a pad in the strip |
| `rcs_mv` | poly | (5683, 6228-6248) | ? | the same line, after its two corners |
| `bd1_n2` | poly | (4967, 5751-5770) | ? | a row without a pad in the strip |
| `bd1_n2` | poly | (5402-5422, 6350) | ? | the same line, bus line x 5412 |
| `rcs_x1` | poly | (4967, 5880-5900) | ? | under RC's turned rail |
| `rcs_x1` | poly | (5097-5117, 6350) | ? | the same line, bus line x 5107 |
| `tl3_w3982` | poly | (4967, 5926-5946) | ? | under RC's turned rail |
| `tl3_w3982` | poly | (5053-5073, 6350) | ? | the same line, bus line x 5063 |
| `vss` | metal | (4967, 5882-5942) | - | RC, turned west; vss by structure only |
| `vss` | metal | (5081-5127, 2505) | - | RC's north end, on the lower edge of the wide metal band y 2180-2500 (not drawn by any block) |
| `c4l_gab` | metal | (4967, 5975-5989) | ? | latch c's clear: from T6's lower piece by the row y 5411 and the metal x 5189 |
| `rst_a` | poly | (5140-5160, 6350) | ? | the clear of latches a and b: bus line x 5150 from T0's south pad |
| `res_b` | poly | (5182-5202, 6350) | in | bus line x 5193 from `trunks`' pad |
| `lpstb_b` | poly | (5227-5247, 6350) | in | bus line x 5237 from `trunks`' pad |
| `tl5_w2722` | poly | (5355-5375, 6350) | out | the strong inverter's output: bus line x 5365 from T3's south pad |
| `tl5_w3461` | poly | (5443-5463, 6350) | in | latch a's data: bus line x 5453 from T5's south pad |

## Ambiguities

1. **The load ties are `tl1`'s `?` items** (two per latch, in the cells). Until one is read the
   cross-coupling of each latch is an assumption, here as in `tl1` and `tl4` (AMB-026).
2. **The supplies of RC and RB** are named from structure only.
4. **The top inverter's load**: its width (the diffusion under the plate: 18 wide for certain,
   read as 66) and its tie (four `?` items at (4995-5056, 3041-3080)). What would settle them: a
   shot in which the plate is transparent, or the same build read elsewhere.
5. **Thin metal W over the tie boxes**: dark there in both metal shots, read as a metal over a
   buried contact (trap 22), in every unit. If one of these were a contact, `tl5_w4937` would be
   shorted to that unit's output; none has a pad or a bright centre.
3. The copies were checked by overlay (3.6x), block comparison and one rail profile; the cells'
   small items were not each measured in each copy.

## Not done

- **An undrawn tap on `rst_a` (in tl4's strip):** track x 4537 has a second
  pad at (4537,3463); its poly row y 3450-3470 runs east over two gate-coloured stretches
  at x 4670-4720 and x 4755-4790, in ground nobody has drawn (x 4640-4960, y 3400-3520;
  review, 2.5-3x). So the shared clear drives devices not yet traced. It does not reach
  tl5's row y 3461 (which starts at x 5195).
- RC's turned rail at the strip's south is drawn from y 5882; both chips put its north
  edge at about y 5894 (12 px; one rail either way).

- The north rows west of x 4967 (table "West of the edge"): six of the eight are not drawn
  there. The probable join `tl5_w3245` = the wire `tl4` called w4718 lacks the 12 px dark gap at (4664-4680,
  2900) between the pad (4645,2900) and the row, and a look at the track x 4581 south of y 4080.
  `rst_a`'s second pad (4537,3463) and its poly east. `tl4_w4068`'s other branch: the metal from
  the pad (4910,2767) west along y 2767 to a pad (4534,2769).
- The row y 2552 at the top; `r9m`'s open ends here (its poly from the pad (5400,2596) north at
  x 5175, said to turn west along y 2550).
- The wide metal band y 2180-2500 that RC and the finger x 4950-5000 hang on (no block has
  drawn it): until it is followed to a supply pad, `vss` on RC is by structure only.
- Where the wires of the south part go beyond the strip: the eight rows west of x 4967 (under
  RB's metal there), the nine bus lines south of y 6350, the rows east of x 5683; T10's north
  piece east of x 5683 (`tcw_m6320`).

## Review

Round 1 (full review, 2026-11-18 02:20 +0000, a fresh agent on claude-fable-5-2, at commit 82a5d8e). Told to
suspect the track field (piece ends, a pad one track off, a missing contact), the three
arms, each mirrored copy's inputs (rows read from gate to pad on the photo), thin metal W
over the tie boxes, the top inverter, latch c's data row and corner, row y 2685's end, rail
RC's supply, the copies, and widths, ends and undrawn features. Checked: a metal test in
both metal shots along all eleven tracks over y 2600-5350 (every drawn piece end within
8 px; the one 32 px gap, on T7 at y 3948-3980, is a row edge plus a pad ring, 6x); a
clean-shot contact scan along each track (only the drawn contacts); the ground one gap
beyond each of 23 pads in three shots; every row's pad assignment for the three latches and
the inverters; the three arms at 3.6x; latch c's step (one poly) and corner (separate from
the pad, green field between); row y 2685's closed end; W at 4.8x with text maps (dark up
to 30 px over the tie boxes in both chips, edge lines continuing, no bright centre,
widening or hole: pass-over); the top inverter at 4.5x; the NOR and inverters at 4x; the
rail profile under RC.
No finding in the trace. Three points in the documents, fixed: RC's north end (it runs on
north into an undrawn metal; `vss` by structure only); T10 is drawn as a stub whose north
end is not an end (said so in Not done); a port's direction. Not checked: the cell copies
item by item above 2.9x, the `?` load ties, RB's supply, the west ports against tl4's rows,
anything south of y 5260.

Round 1 of the first round of work: clean (no findings).

### Second round of work (the tracks to both ends, the rows south of the column, two joins to tl4)

Round 1 (full review of what was added since 3cd7985, 2026-11-18 02:59 +0000, a fresh agent on
claude-fable-5-2). Told to suspect the two joins to tl4 step by step (the gap mark on row
y 2940, the pads (4537,2940) and (4910,2767), the four corners, the tracks x 4537 and
x 4625 as single metals among tl4's parallel tracks, and the tl4 nets they meet), T3 over
`bw`'s row at (5362,5590), T5's south pad against row y 5761, the rows and bus lines read at
1.7x, the east-edge pads, the counter metals over the bus, and RC. Checked: JOIN 2's pad at
4.4x in four shots, the gap mark by colour in both metal shots (poly-coloured: a trap-2
bar), the track x 4537 to tl4's pad (4533,4198) at 2.5-3x (no dark stretch over 16 px; one
other pad); JOIN 1's pad at 5.5x with a text map and the follower, its four corners at 4.6x
in four shots, the track x 4625 to tl4's pad (4625,4068) with no pad or hole; T3 at 5.5x
(no contact); T5's pad in four shots; the edge pads and south pads; the bus polys and
corners; RC as one metal in both chips; the full extraction (no unintended merge;
`tl5_w2722` apart from `rc_stepreq_n`).
No finding changes a connection. Three notes, recorded: an undrawn tap on the shared clear
in tl4's strip (Not done; for tl4's tracer), a comment's wording (fixed), RC's turned
rail's north edge 12 px off (recorded). Not checked: the two tracks above 3x at each row
crossing, T10's north corner beyond the follower, the west-edge crossings of the south
rows.

Round 1: no findings.

## Note (coordinator, from the handoffs of 2026-11-17/18)

From `tl6`: latch c's outputs reach `ras_o0_alt2` (through its inverter) and `tcw_c`.

## Corrections from `tl4` (coordinator, from the handoffs of 2026-11-18, second batch)

- `tl5_w3505`'s row y 2985 runs on west to the pad (4452,2985): the enable of `tl4`'s second latch.
- `tl5_w3245`'s row y 2900 ends on the pad (4648,2898) of `tl4`'s track x 4581 = `tl5_w3245`, the set
  input of `tl4`'s pair at y 4645-5000 (the probable join of this file's Not done is drawn).
- `tl3_e4243` (latch c's enable) is `tl3_e4243` = NOR(`rcs_mv`, `rst_ck`); the wire `tl5` called w2855 is `tl4_w3113`.
- `tl4_w4068`'s "other metal of the pad (4910,2767), not drawn west of the pad" is drawn, to the pad
  (4539,2768) and a poly column north (`tl4_w4068`). `tl5_w4937` and `tl5_w2722` go west on `tl4`'s bus
  lines 4 and 5.
- `c4l_l3` (NOT `tl4_w4243`); the wire `tl5` called w5500 = `tl4_w5068` (NOR(`tl4_w4545`,
  `tl4_w4850`)); the wire `tl5` called w5674 = `ck_out`; this file's bus line x 5717 is `rcs_mv`; the bus line x 5412 of tl5 = `bd1_n2`.
- The bus line x 5107 is `rcs_x1` (renamed 2026-11-19); `tl3_w3982` (bus line x 5063) comes from a pad (4583,5936)
  and a metal on west along y 5939; `c4l_gab`'s metal x 5189 / y 5982 turns south at x 4929 to a pad
  (4929,6323) and a row on west.
- Geometry only: RC's turned rail `M 5127,5912 x4967 w=60` and the port `vss M 4967,5912` give
  y 5882-5942; its top edge is y 5891. The comment at the row y 2930-2950 ("no metal over the row at
  x 4694-4947") is wrong from x 4732 east: the row is under `tl4`'s wide metal foot there, no contact.
- The wide metal band y 2180-2500 that RC's north end is on also feeds `tl4`'s RA, by the vertical
  metal x 4949-4995 (its east part, x 4967-4995, lies in this strip, undrawn) and the foot. Package
  `tlb` (queue).
- Re-read items R41 (`tl5_w4937`'s thin metal) and R42 (`tl5_inv`) apply here.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `rst_a` (the clear of four latches) is a buffered copy of the reset
  NOR(`lpstb_b`, `res_b`) (`rst_a`); `rcs_x1`'s driver is `lc1`'s gate 2 (`eof` run 2).
- This file's clear of latch c is also the 4-bit counter's pass-gate line `c4l_gab`; `tl3_w3982` is
  `tl3_w3982` (`tl3` run 11).
- R43: the south bus's pads T0, T3, T5 (y 5759-6108): the polys go on below them (`eof`).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The south bus line x 5412 (the row y 5761; "driver open") **is `bd1_n2`**, the output of `bd1`'s latch on R4's match: followed south by `eof`'s piece `n2n` (the middle row y 6996 of the left-centre diagonal bundle, the track x 6991, the track x 6775) and through the left bus field by `busl`'s piece `n2`.
- the wire `tl5` called w5936 (= `tl3_w3982`; "source open") is followed (`eof` runs 11-12, pieces `w5936`, `d3982`): it is latch C's data in `lc2` and is driven by the inverter U4 at (7575,8386), the last of three in series from latch D's lower node (`lc1_w7928`).

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- Ports, `tl5_w2722` P (5355-5375,6350) out ("the strong inverter's output: from T3's south pad (5363,6108)"): the column runs on south to a bend (5367,6806) and by a diagonal and the row y 7041 to the left bus field's staircase bundle and the row y 14350 of the bottom-centre bus (`busl`, piece `gd`, 2026-11-20; no tap in 11,000 px; load open).
