# tl5: top-left random logic, the fifth strip (x 4967-5683, y 2500-6350)

Package `tl5` (part 5 of 6 of the top-left logic). Trace: `trace/tl5.txt`. Views:
`cache/scratch/tl5/`. The strip holds a **gate column** east of `tl4`'s rail RB (the mirror
image of the first cluster's west column: `tl1`'s units, here on the rails RC and RB) and a
**bus field** of eleven vertical metal tracks east of it.

## Status

2026-11-18 01:53 +0000. **Partial: three latches and a NOR** (36 transistors). The latches are mirrored copies
of `tl1`'s cells `tl1_ua` and `tl1_ub`, the NOR a mirrored copy of `tl1`'s NOR; every row that
feeds or leaves them is read here. Full extraction: 0 errors, 0 warnings.

```
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
```

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
| x 4967-5260, y 2540-2920 | poly rows in the open running west from the pads of the tracks' north ends (y 2595, 2638, 2682, 2722, 2767, 2810, 2855, 2900); `r9m`'s three rows among them | only `r9m`'s drawn |
| x 4967-5210, y 2920-3170 | top of the column: a pad (5165,2945); a unit at y 3044-3174 (findcell: `tl1`'s inverter at 2371,-1171 mirrored, score 0.54: not a copy) with rows y 2985 (to the pad (5494,2985), T6's north end), y 3070 (pad (5364,3070), T3), y 3113 (pad (5580,3113), T8) | not drawn |
| x 4901-5203, y 3142-3352 | **the NOR** (findcell: `tl1`'s NOR at 2359,-390 mirrored, 0.74) | traced |
| x 4901-5203, y 3343-3803 | **latch a** (findcell: `tl1_ua` 2361,-997 mx 0.70; `tl1_ub` 2361,-998 mx 0.78) | traced |
| x 4901-5203, y 3820-4280 | **latch b** (`tl1_ua` 2361,-520 0.71; `tl1_ub` 2361,-521 0.74) | traced |
| x 4901-5203, y 4297-4757 | **latch c** (`tl1_ua` 2361,-43 0.75; `tl1_ub` 2361,-43 0.75) | traced |
| x 4967-5210, y 4780-5040 | two units (findcell: `tl1`'s inverter at 2373,565 mx 0.78 and 2373,695 mx 0.77) | not drawn |
| x 4967-5210, y 5040-5330 | the column's foot (`sv2.png`): RC runs on to about y 5300; a pad (5040,5237) with a row east to a pad (5407,5237) | not drawn |
| x 5200-5683, y 2540-5800 | the bus field: rows of the column to pads on the tracks (the latches' are drawn), rows that pass east out of the strip, pads of the east neighbour's rows (x 5560-5683, y 4380-4530) | the latches' rows and the track pieces between their pads drawn |
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

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tl5_w3505` | poly | (5683, 3712-3732) | ? | latch a's enable: the row of its second pad runs on east |
| `tl5_w4590` | poly | (5683, 3862-3882) | ? | latch c's clear: the row from the north pad of T6's lower piece |
| `tl5_w4503` | poly | (5683, 4580-4600) | out | latch c's inverse output |
| `tl5_w4633` | poly | (5683, 4623-4643) | out | latch c's output |

## Ambiguities

1. **The load ties are `tl1`'s `?` items** (two per latch, in the cells). Until one is read the
   cross-coupling of each latch is an assumption, here as in `tl1` and `tl4` (AMB-026).
2. **The supplies of RC and RB** are named from structure only.
3. The copies were checked by overlay (3.6x), block comparison and one rail profile; the cells'
   small items were not each measured in each copy.

## Not done

- The tracks beyond the drawn pieces: T5's north piece north of (5451,2925) (`tl5_w3245`; a pad
  about (5452,2900) and a row west), T5 south of (5451,3482) (`tl5_w3461`), T6 north of
  (5494,3490) (`tl5_w3505`; to the pad (5494,2985) and a row west along y 2985), T0 beyond y 3622-4127
  (`tl5_w3636`), T7 beyond y 3968-4214 (`tl5_w3982`; `follow.py`: north to a corner (5532,2772)
  and west to a pad (5452,2767); south to y 4984), T10 north of (5667,4380) (`tl5_w4395`; `follow.py`: to a corner (5677,3660) and
  east out of the strip at y 3657), T4 north of (5407,4444) (`tl5_w4458`), T6's lower piece south
  of (5494,4604) (`tl5_w4590`).
- The thin metal x 5028-5046 over the column ("thin W" of the master): `follow.py 5035 3450 N`
  runs to (5037,2680), south it is dim over the tie boxes. Not drawn; its contacts are not found.
- The rest of the column: the units at y 2920-3142 and y 4780-5330 (inventory).
- The rest of the bus field, the rows north of y 2920 and under the foot.

## Review
