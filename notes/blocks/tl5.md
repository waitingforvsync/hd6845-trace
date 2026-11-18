# tl5: top-left random logic, the fifth strip (x 4967-5683, y 2500-6350)

Package `tl5` (part 5 of 6 of the top-left logic). Trace: `trace/tl5.txt`. Views:
`cache/scratch/tl5/`. The strip holds a **gate column** east of `tl4`'s rail RB (the mirror
image of the first cluster's west column: `tl1`'s units, here on the rails RC and RB) and a
**bus field** of eleven vertical metal tracks east of it.

## Status

2026-11-18 02:08 +0000. **Partial: the gate column is traced from y 3040 to y 5045** (42 transistors): an
inverter at the top (hand-traced), a NOR, three latches and two inverters (mirrored copies of
`tl1`'s NOR, cells `tl1_ua`/`tl1_ub` and inverter); **the eight north rows** that bring their
signals in from `tl4`'s strip, **the thin metal W** over the column and the track pieces between
(wiring). Every row that feeds or leaves a unit is read here. Full extraction: 0 errors,
0 warnings. Not traced: the column's foot, the rows under the foot and the rest of the bus
field (Not done).

```
tl5_w2722 = NOT tl5_w2855                                            marked: the load's tie (`?`); the pull-down is firm
tl5_w3245 = NOR( tl5_w4160, tl5_w3550 )                              firm
tl5_w3364 = NOT tl5_w3461                                            firm
tl5_w3550 = NOT( tl5_w3461 AND tl5_w3505  OR  tl5_w3680 )            marked: the load ties (`?` in tl1's cells)
tl5_w3680 = NOT( tl5_w3636  OR  tl5_w3505 AND tl5_w3364  OR  tl5_w3550 )   marked likewise
tl5_w3841 = NOT tl5_w3680                                            firm
tl5_w4027 = NOT( tl5_w3680 AND tl5_w3982  OR  tl5_w4160 )            marked
tl5_w4160 = NOT( tl5_w3636  OR  tl5_w3982 AND tl5_w3841  OR  tl5_w4027 )   marked
tl5_w4318 = NOT tl5_w4395                                            firm
tl5_w4503 = NOT( tl5_w4395 AND tl5_w4458  OR  tl5_w4633 )            marked
tl5_w4633 = NOT( tl5_w4590  OR  tl5_w4458 AND tl5_w4318  OR  tl5_w4503 )   marked
tl5_w4807 = NOT tl5_w4850                                            marked: the load's tie (`?`, as in tl1)
tl5_w4937 = NOT tl5_w3982                                            marked likewise
```

- **The top inverter** (y 3040-3150), a wide rail gate (122/19) with a strong load: its input
  `tl5_w2855` comes in on the north row y 2855 and T8, its output `tl5_w2722` goes onto T3, which
  runs from the north row y 2722 south to y 6114.
- **Latch a** (y 3343-3803): open while `tl5_w3505` is high, takes `tl5_w3461`, cleared
  (output low) by `tl5_w3636`. Output `tl5_w3680`, inverse output `tl5_w3550`.
- **Latch b** (y 3820-4280): open while `tl5_w3982` is high, **takes latch a's output**
  (`tl5_w3680`: the track T8 joins a's output pad to b's data pad), cleared by the same
  `tl5_w3636` (one metal, T0, with both clear pads). Output `tl5_w4160`.
- **Latch c** (y 4297-4757): open while `tl5_w4458` is high, takes `tl5_w4395`, cleared by
  `tl5_w4590`. Output `tl5_w4633` and inverse output `tl5_w4503` both leave the strip east.

- **The NOR** (y 3142-3352) takes latch b's output (`tl5_w4160`, by the track T9) and latch a's
  inverse output (`tl5_w3550`, by T8): `tl5_w3245` is high only while b's output is low and a's
  output is high. It leaves north on T5.

- **Two inverters** below latch c: `tl5_w4807` = NOT `tl5_w4850` (input and output both on rows
  that leave the strip east) and `tl5_w4937` = NOT `tl5_w3982`, the inverse of latch b's enable
  (T7 ends on its gate pad), out south on a piece of T4.

- **Where the signals enter and leave** (wiring, no `?` item on any of it): eight poly rows cross
  the strip's west edge at y 2685-2985, each to the north pad of one track: latch a's enable
  `tl5_w3505` (y 2985, T6), the clear of a and b `tl5_w3636` (y 2940, T0, which also runs on
  south to y 6113), the NOR's output `tl5_w3245` (y 2900, T5's north piece), latch b's enable
  `tl5_w3982` (y 2767, T7), latch c's enable `tl5_w4458` (y 2810, T4's north piece), and
  **inverter 2's output `tl5_w4937` = NOT `tl5_w3982`**, which runs from T4's south piece by a row
  along y 5237 onto the thin metal W, up the whole column and out west on the row y 2685.

So a and b are two latches in series with one clear, the build of the two latches in front of
`rcs_e4` in the first cluster (`notes/blocks/tl1.md`), and the NOR picks out the state "a set,
b not (yet) set". What any of the signals is, is not known: the tracks are not followed to
their other ends yet (Not done).

## Inventory

Survey: `survey.png` (0.33x, all blocks' geometry), `sv0.png`-`sv2.png` (0.9x, chip-2 metal and
clean shot), the bus field in the clean shot at 2.35x: `r0_a.png` (y 2500-2925), `r1_a.png`
(y 2920-3345), `ra_a.png` (y 3335-3815), `rb_a.png` (y 3812-4292), `rc_a.png` (y 4289-4769).

Rails: RB x 4906-4951 (VCC; `tl4`'s east rail, shared: the loads of both columns end on boxes
under it), RC x 5081-5127 (the pull-downs' boxes: VSS, named from structure). Thin metals over
the column: x 4984-4996 (pieces, plate to third pull-down, as in the master), x 5028-5046
("thin W", runs the length of the column: Not done), x 5171-5185 (pieces, inverter output to
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
| x 4967-5210, y 5045-5330 | the column's foot (`sv2.png`): RC runs on to about y 5300; **W's south pad (5038,5237) with its row east to the pad (5407,5237)** | the pad and row traced; RC's end not looked at |
| x 5200-5683, y 2540-5800 | the bus field: rows of the column to pads on the tracks, rows that pass east out of the strip, pads of the east neighbour's rows (x 5560-5683, y 4380-4530: pads (5665,4425), (5665,4470), (5580,4520) with rows east) | the traced units' rows and the tracks down to y 5250 drawn (table under "The tracks"); the neighbour's pads and everything south of y 5250 not |
| x 4967-5683, y 5330-5800 | rows under the foot (y 5440-5760), `bw`'s row y 5585 among them; pads at x 5490-5560 | not drawn |
| x 4967-5683, y 5800-6350 | `amrw`'s four counter lines and their pads; the poly bus x 5100-5290 going south (`tla`'s `rcs_e4` line among them); pads (5190,6058), (5232,6098) of T1/T2 | others' geometry only |

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

**Rails.** RC is drawn y 3140-4790 (looked at on `n_m.png`, `a_m.png` and the overlays; its
top end is at about y 3000, and it runs on south) and is named `vss` **from structure** (it
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
| gate | row y 4840-4858 from the east: under every track without a pad, out of the strip (`tl5_w4850`) | row y 4970-4988 from the pad (5538,4980), the south end of T7 (`tl5_w3982`, latch b's enable); the row runs on east through the pad, out of the strip | `rd_a.png` 2.35x; `pi1.png` 4x (the pads; the rows at x 5610-5690; bare ground south of the T7 pad) |
| the gate under RC | `px.py row 4849 5046 5216 6 acid1b,acid`: west end at x 5075, poly over a channel (229/166/120) x 5082-5136, open poly east of RC | `row 4979`: the same | `px.py col 5112 4800 4916 4`: node (tan) y 4820-4836, gate y 4844-4856, VSS box from y 4868 |
| east of RC the gate row lies on field | no diffusion edge across the band east of x 5145 in the chip-2 stripped shot; the node box above ends at y 4833 | the same | `inv_c2.png` |
| output | buried contact on the node box (5161-5205, 4794-4830), poly y 4798-4818 east out of the strip (`tl5_w4807`) | poly y 4928-4948 east to the pad (5407,4937), the north end of a piece of T4 (`tl5_w4937`) | `rd_a.png`, `pi1.png` |
| both rows of inverter 1 cross T4's position in the open (T4 has no metal y 4690-4925) | two unbroken orange bands in the metal shot | | `pi2.png` |
| VSS box | (5091-5145, 4860-4910), contact (5114,4884) | 130 lower, contact (5116,5013) | `pi2.png`: rings |
| VCC box | `tl4`'s (4908-4960, 4805-4878), its contact | of its own (4912-4962, 4935-4995), one ring (4918-4945, 4940-4985) | `pi2.png`, `inv_c2.png` |
| load tie | the master's `?` items: a ringed box (5000-5040, 4855-4885) at the tab's end | the same | `inv_c2.png`; not measured |

### The inverter at the top of the column, y 3040-3156 (traced 2026-11-18 02:08 +0000, by hand)

Read on `u1_a.png` (clean), `u1_c2.png` (chip-2 stripped), `u1_m.png` (chip-2 metal), all 4.8x of
4955-5217 x 3028-3163; overlay `u1_ov.png`; pads `pu1.png` (4x, two shots).

| Item | Reading | Seen (profiles: `tools/px.py`, clean shot / chip-2 stripped shot) |
|---|---|---|
| gate row y 3103-3122 | from the pad (5580,3113), the south end of T8's north piece (`tl5_w2855`), west across RC to an end at x 5048 | `row 3113 5034 5150 4`: field under W (185/128/130) to x 5046, poly from x 5050, bright over a channel (235/166/118) x 5074-5130 under RC; `pu1.png`: the pad, bare ground south of it; the row under T0 and T5 without a pad |
| under RC | node y 3086-3102, gate y 3108-3122, then diffusion without a break y 3128-3188 (the VSS region and the NOR's VSS box, contact (5112,3168)) | `col 5105 3040 3200 5`: olive (field under a rail) to y 3075, tan 197/166/139 y 3090-3100, salmon 240/174/122 y 3110-3120, tan 192-201/154-183/135 y 3130-3185 |
| west edge of the channel, about x 5068 | the VSS side is tan from x 5072 with a dark edge at x 5060-5068; the gate is bright from x 5074 | `row 3136 5040 5150 5`, `row 3113` |
| **the channel runs on east of RC to x 5190** | east of RC at x 5150 the gate lies between two diffusions: neck of the node y 3086-3094 (red minus green 14-24 in the chip-2 stripped shot), gate y 3106-3122 (orange), wing y 3134-3142 (16-23), field above y 3074 and below y 3154 | `col 5150 3050 3160 4`, `col 5170 3050 3166 4`; the diffusion's east edge is a dark line across the gate band at x 5188-5196 in the chip-2 stripped shot and the chip-2 metal shot (`row 3113 5140 5216 4 acid,metal`), orange poly on both sides of it |
| the wing | diffusion x 5140-5186, y 3130-3147, field east (x 5205) and south (y 3154-3162) of it; one with the VSS region under RC as far as can be told: the dark line at x 5134-5138 between them is on the gate poly as well (the rail's edge line) | `row 3138 5130 5215 5`: 166-170/141-153/97-102 (red minus green 13-29) x 5145-5180, 159/154 at x 5205 |
| node east of RC | neck y 3084-3098 from under RC (tan to x 5132, the rail's edge line, diffusion x 5144-5156), box (5152-5192, 3058-3098) with a buried contact (concentric rings) | `row 3093 5120 5212 4`; `u1_c2.png` |
| output | poly on the buried contact east along y 3063-3082 to the pad (5364,3070) on T3 (`tl5_w2722`); T3 passes through the pad | `pu1.png` 4x; `r1_a.png` |
| load | the node's strip y 3077-3095 west under W (tan y 3078-3087 at x 5042) and under the plate (x 4964-4999, y 3042-3140, in the open) onto `tl4`'s VCC box (4905-4965, 3068-3148) | `col 5042 3034 3104 3`; `col 5010 3056 3152 4`: at x 5010 diffusion only y 3076-3090, field below (green over red in the chip-2 stripped shot) |
| the load's width | **uncertain**: one edge line crosses the plate, at y 3066-3074, none lower (`col 4981 3034 3152 4`, and the three views); east of the plate the strip's bottom edge runs into the plate's east edge and down it (`u1_m.png`). Read as the diffusion filling the plate from y 3072 to y 3138: W/L about 66/35. The strip is drawn firm, the widening `?D` | |
| tie (`?`) | a bar from the plate's top east along y 3041-3053 (salmon y 3043-3049 at x 5042), and under W a small box with a heavy outline (5033-5052, 3056-3076) between the bar and the strip. Taken as the tie of the plate to the node; neither the bar's join to the plate nor the box is resolved: four `?` items | `col 5042`; `u1_a.png`, `u1_c2.png` |

Extracted: pull-down W/L 122/19 (gate `tl5_w2855`, node to VSS), load 70/33 with the uncertain
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
| y 2675-2694 | (5038,2685): the row ends on it (closed east end x 5058; 17 px of field to `r9m_l3`'s step at x 5075-5090) | the thin metal W south (`pw1.png`) | `tl5_w4937` |
| y 2714-2733 | (5364,2722), north end of T3 (`pt1.png`) | T3 south: one metal to (5363,6114) (`follow.py 5365 2900 N/S`; candidate (5364,3086) = the pad (5364,3070) of the top inverter's output); drawn to y 5250 | `tl5_w2722` |
| y 2758-2777 | (5452,2767): its metal is an arm east to a corner (5538,2770) and T7 south (`pt1.png`: both tiles; the clean shot is pink from the pad to the corner) | latch b's two enable pads, the pad (5538,4980) | `tl5_w3982` |
| y 2801-2820 | (5407,2810), north end of T4's north piece (`pt1.png`) | (5406,2810)-(5404,4682) (`follow.py 5408 3400 N/S`): latch c's two enable pads | `tl5_w4458` |
| y 2846-2865 | (5580,2855), north end of a piece of T8 (`pt2.png`) | (5582,2852)-(5581,3120) (`follow.py`): to the pad (5580,3113) of the top inverter's gate row. The follower's candidate (5580,2942) is a speck (`pw2.png`) | `tl5_w2855` |
| y 2890-2909 | (5452,2900), north end of T5's north piece (`pt2.png`) | the NOR's output pad (5452,3245) | `tl5_w3245` |
| y 2930-2950 | (5165,2945): its metal is an arm east onto the north end of T0 (`pt2.png`: bright metal leaves the ring east; `follow.py 5234 4300 N`: corner (5233,2944), west end (5161,2944)) | T0 south through the clear pads (5233,3636) and (5233,4113), on to a corner (5231,6026), west, south to (5145,6113) (`follow.py`); drawn to y 5250 | `tl5_w3636` |
| y 2975-2994 | (5494,2985), north end of T6's upper piece (`pt2.png`) | latch a's two enable pads | `tl5_w3505` |

The tracks, as drawn (each piece one metal; "to y 5250" means it runs on south of what was
looked at; the 2.35x clean views show every piece as one pink band without a pad other than
those listed):

| Track | Piece | Pads | Net |
|---|---|---|---|
| T0 x 5233 | from the arm at y 2945 to y 5250 (on south) | (5165,2945), (5233,3636), (5233,4113) | `tl5_w3636` |
| T3 x 5364 | y 2710-5250 (on south) | (5364,2722), (5364,3070) | `tl5_w2722` |
| T4 x 5407 | y 2798-4689 | (5407,2810), (5407,4458), (5407,4677) | `tl5_w4458` |
| T4 | y 4925-5249 | (5407,4937), (5407,5237); the speck (5407,5028) is not a contact (`pw2.png`) | `tl5_w4937` |
| T5 x 5451 | y 2888-3257 | (5452,2900), (5452,3245) | `tl5_w3245` |
| T5 | y 3450-5250 (on south: `follow.py` to (5450,5766)) | (5452,3461) | `tl5_w3461` |
| T6 x 5494 | y 2973-3734 | (5494,2985), (5494,3505), (5494,3722) | `tl5_w3505` |
| T6 | y 3860-5250 (on south: `follow.py` to (5494,5418)) | (5492,3872), (5492,4590) | `tl5_w4590` |
| T7 x 5538 | from the arm at y 2769 to y 4992 | (5452,2767), (5538,3982), (5538,4200), (5538,4980) | `tl5_w3982` |
| T8 x 5581 | y 2843-3125 | (5580,2855), (5580,3113) | `tl5_w2855` |
| T8 | y 3278-3562 | (5580,3290), (5580,3550) | `tl5_w3550` |
| T8 | y 3668-3950 | (5580,3680), (5580,3938) | `tl5_w3680` |
| T9 x 5625 | from the arm at y 3202 to y 4172 | (5580,3200), (5622,4160) | `tl5_w4160` |
| T10 x 5667 | y 4380-4407 (on north: `follow.py` to a corner (5677,3660) and east out of the strip) | (5665,4395) | `tl5_w4395` |

**Believed, not joined** (from `tl4`'s notes of where its tracks turn east towards this strip;
the polys between are in `tl4`'s strip and are not drawn): `tl4_w4068` (corner (4630,2988), east)
is at the y of `tl5_w3505`'s row; `tl4_w4198` (metal x 4537 from y 2938) at the y of `tl5_w3636`'s;
`tl4_w4718` (corner (4586,2896), east) at the y of `tl5_w3245`'s; `tl4_w3113` (corner (4421,2858),
east) at the y of `tl5_w2855`'s. `r9m` gives the metal of the row y 2685 as ending west on a pad
(4866,2681), from which a metal runs to a pad (4270,2640) in the middle cluster. Rows step one
track at hops here (`r9m`), so none of these is a join until its poly is read.

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

## Self-check (tracer, before any review)

**Ends.** Every wire end drawn, and how it was looked at (all at 4x in the chip-2 metal shot and
the clean shot unless noted): the pads in the tables above (`pa1`-`pa4`, `pb1`, `pb2`, `pc1`-`pc3`,
`pn1`, `pn2`, `pi1`, `pi2`, `pt1`, `pt2`, `pw1`, `pw2`, each `.png`; latch b's and c's thin-metal
pads only on the 3.6x overlays and by the block comparison with latch a's); the stub of latch b's node
(`pb2.png`); the eight rows at the west edge (x 4955-4967 on `north_a.png` 3.1x and `n_a.png`
2.75x: under metal, running on west; **below 4x**: the edge itself was not looked at closer); the
seven rows at the east edge (`pc3.png`, `pi1.png` 4x at x 5610-5690); track pieces that are drawn
short of their ends are listed as such in the tracks table (T0, T3, T5, T6 south of y 5250;
T10 north of y 4380).
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
the east neighbour's pads at x 5560-5683, y 4380-4530 are not drawn (Not done).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tl5_w4937` | poly | (4967, 2675-2694) | out | inverter 2's output, from the thin metal W's north pad |
| `tl5_w2722` | poly | (4967, 2714-2733) | out | the row of T3's north pad |
| `tl5_w3982` | poly | (4967, 2758-2777) | ? | latch b's enable (T7) |
| `tl5_w4458` | poly | (4967, 2801-2820) | in | latch c's enable (T4's north piece: only gates on it) |
| `tl5_w2855` | poly | (4967, 2846-2865) | ? | the row of T8's north pad |
| `tl5_w3245` | poly | (4967, 2890-2909) | out | the NOR's output |
| `tl5_w3636` | poly | (4967, 2930-2950) | ? | the clear of latches a and b (T0) |
| `tl5_w3505` | poly | (4967, 2975-2994) | ? | latch a's enable (T6) |
| `tl5_w3505` | poly | (5683, 3712-3732) | ? | latch a's enable: the row of its second pad runs on east |
| `tl5_w4590` | poly | (5683, 3862-3882) | ? | latch c's clear: the row from the north pad of T6's lower piece |
| `tl5_w4503` | poly | (5683, 4580-4600) | out | latch c's inverse output |
| `tl5_w4633` | poly | (5683, 4623-4643) | out | latch c's output |
| `tl5_w4807` | poly | (5683, 4798-4818) | out | inverter 1's output |
| `tl5_w4850` | poly | (5683, 4840-4858) | in | inverter 1's gate |
| `tl5_w3982` | poly | (5683, 4970-4988) | ? | latch b's enable: the row of T7's south pad (5538,4980) runs on east |

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

- The tracks south of y 5250: T0 (`tl5_w3636`, to (5145,6113)), T3 (`tl5_w2722`, to (5363,6114)),
  T5 (`tl5_w3461`, to (5450,5766)), T6's lower piece (`tl5_w4590`, to (5494,5418)); T10 north of
  (5667,4380) (`tl5_w4395`; only a 27 px stub of T10 is drawn, y 4380-4407; its north end is NOT an end: the metal runs y 3654-4402 and leaves east near y 3657 (`follow.py`; review round 1), so `tl5_w4395` has no port row yet).
- The column's foot: RC south of y 5045 and where it ends; RB south of `tl4`'s end.
- The rows under the foot (y 5330-5800), the pads at x 5490-5560 there, the tracks T7-T10 south
  of y 5000, and everything at y 5800-6350 that `amrw`, `tla` and `trunks` have not drawn.
- The east neighbour's pads in the bus field (x 5560-5683, y 4380-4530) and T10's metal east along
  y 3657; the row y 2552 at the top; `r9m`'s open ends here (its poly from the pad
  (5400,2596) north at x 5175, said to turn west along y 2550).
- The wide vertical metal at x 4900-4995, y 2540-2995 north of RB's top end (in both strips),
  and RC north of y 3140 (it runs on north unbroken into a large undrawn metal at y 2200-2500 (review round 1: follower corners (5185,2505), (4559,2399), (5262,2217)); no drawn or named metal is there, so `vss` is by structure only).
- The joins to `tl4`'s tracks listed as believed under "The north rows".

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

Round 1: no findings.
