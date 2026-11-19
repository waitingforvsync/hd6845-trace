# tl3: top-left random logic, strip 3 (x 3533-4250, y 2500-6350)

Trace: `trace/tl3.txt` (`@requires tl1`, which requires `tla`). Views: `cache/scratch/tl3/`.
Started 2026-11-17 16:52 -0600 (Matt Godbolt's second session; the first holds `tl2`).

The strip holds the **middle cluster** of the row counter's step logic (`notes/blocks/tla.md`
names it: "the same construction 1042 px east"), the poly rows above it and the bus rows
below it. `tla` drew three things in it: the unit that makes `rcs_in1` (4081,4072), the
inverter `rcs_mu` (4050,3374) and the unit `rcs_mn3852` (4081,3852), with the VCC rail
x 3824-3868 and the east VSS rail x 3992-4041.

## Status

Traced, extracting (69 transistors of its own, 0 errors), the west column and pieces of the east column:

- **latch A, y 3212-3652**, by placing `tl1`'s two unit cells, with its rows, its two thin
  metals and the cluster's west rail (merged 2026-11-17, db5ab84);
- **three NOR units** (cell `tl3_nor`, 3 transistors each): NOR 1 (y 3688-3872), NOR 2
  (y 3862-4046), NOR 4 (y 4643-4827), with their rows and two metals (2026-11-17 17:16 -0600);
- **the pair at y 4046-4330** (7 transistors): a cross-coupled NOR pair, which drives
  `tl3_w3803`; **the inverter at y 4345-4490** (2); **NOR 3** (y 4469-4653, 3), the fourth
  copy of `tl3_nor` (2026-11-17 17:48 -0600);
- **latch B, y 4818-5258** (11), `tl1`'s two unit cells again, with its rows and metals
  (2026-11-17 18:09 -0600);
- **two NOR units of the east column** (cell `tl3_enor`, 3 transistors each), y 4165-4335 and
  y 4990-5160, with their wiring in the bus field; the lower one drives latch B's enable
  (2026-11-18 07:43 -0600);
- **latch C, east column y 4514-4970** (11): the two unit cells a third time, mirrored, written
  out (not instanced) with its metal and contacts placed from this copy; its rows, tracks and
  thin metals in the bus field east of it, the stretch of the thin metal x 3948-3962 over it (no contact) and a wire that passes through the bus field (`rcs_mv`)
  (run 6, Tom Seddon, 2026-11-18 15:03 +0000).
- **the NOR under the east rail at y 4345-4514** (3): it drives `rcs_mv` (run 7, Tom Seddon,
  2026-11-18);
- **the NOR under the rail at y 3450-3660** (3) and **the inverter under the rail at y 3655-3745**
  (2), with the poly that takes the inverter's output to the upper gate of `tla`'s `rcs_mn3852`
  unit and the top of that unit (1) (run 7, 2026-11-18 16:13 +0000).

- **the inverter under the south end of the east rail, y 5180-5300** (2): it drives the row that
  runs, by a track in `tl4`'s strip, to latch C's data (run 8, Tom Seddon, 2026-11-18 17:08 +0000).
- **the top unit E1 of the east column, y 2950-3090** (2): an inverter under the rail whose load
  plate is one poly with the row of `tl3_w3373`: **it drives latch A's enable** (run 8,
  2026-11-18 17:16 +0000).
- **the load of `tla`'s unit `rcs_mn3852`** (1), **and a third pull-down of that unit**: a
  diffusion branch from its load strip leads to the transistor under gate `rcs_mu`, which
  `tla` had on `rcs_in1`. `rcs_mn3852` = NOR(`tl3_e3712`, `rcs_in1`, `rcs_mu`) and `rcs_in1` =
  NOT `rcs_mv` (run 8; found by its review; one line of `trace/tla.txt` corrected).

- **the foot of the cluster, y 5345-5660** (wiring only, no transistor): five poly rows between
  `tl2`'s strip and `tl4`'s, two pads, the metals that cross it. It closes four joins: latch C's
  clear is `rcs_x1`; the inverter that makes latch C's data takes latch B's inverted output; gate 1
  of `rcs_mv`'s NOR is NOR 3's output; track A (latch C's enable) is `inh_ck` (run 9, Tom Seddon,
  2026-11-18 19:14 +0000).

- **the thin metal x 3948-3962, end to end** (run 9, 2026-11-18 19:25 +0000): from its north pad
  on the load plate of `tl3_e3550`'s unit to its south pad (3953,5458) on `tl1_w4937`'s row, firm
  but for six stretches over load-tie boxes, drawn uncertain. With it **`rcs_e4` =
  NOR(`tl1_w4678`, `tl3_e3550`)**: R9's match (AND NOT `tc2_o5175`) reaches the step logic
  through `tl1`'s NOR (marked: Ambiguity 11).

- **the row y 2899 and the thin metal x 4099-4111 north of track A** (run 10, Tom Seddon,
  2026-11-18 21:36 +0000; wiring only): `tl2`'s row of `tl1_w3594` runs on across the strip to a pad
  with a contact (4103,2899), the north end of the thin metal, which is drawn down to track A,
  firm but for six stretches over the units' node boxes (uncertain). With it **`tl1_w3594` is
  `inh_ck`** (marked: Ambiguity 13): the enable of `tl1`'s two latches, an input of `rcs_a2` and
  gate 1 of NOR 1.

- **south of the foot, y 5660-6350** (run 11, Tom Seddon, 2026-11-18 22:25 +0000; wiring only, no
  transistor, no diffusion): three metals from the foot to their pads, the rows from those pads, a
  wire of two metal pieces and two poly pieces that ends on the north pad of the 4-bit counter's
  L3 line, both rails to the strip's south edge, and the row y 6327 with its two pads. Five things
  follow. **`tl3_w4763` is `tc1_o3527`** (firm). **`tl3_w3982` is `tl5_w5936`** (firm; a bus line
  that leaves `tl5`'s strip south, so still no driver). **The 4-bit counter's L3 line `c4l_l3` is
  `c4l_l3`** = NOT `tl4_w4243`, the inverse of `tl4`'s latch (firm for the join; the inverter
  and the counter cells are marked as before). **The 4-bit counter's pass-gate line `c4l_gab` is
  `c4l_gab`**, the clear of `tl5`'s latch c (firm for the join). **`rcs_thin_e`'s row y 6327
  ends on a pad whose metal goes south to `ur`'s pad (3968,6410); that pad is not on the 5-bit
  counter's L3 line** as `ur` had drawn it: three corrections to `trace/ur.txt` (a commit of
  their own, a1c5d8b).

Everything else in the strip is surveyed only (Inventory): the rows above y 2890.

## Inventory

Survey: `sv_top.png`, `sv_bot.png` (0.68x, metal and clean shot, all traces);
`tools/t.sh tl3 railprof.py 3992 4041 2900 5340` and `3645 3690 3180 3720`.

| Where | What | State |
|---|---|---|
| y 2580-2900 | horizontal poly rows above the cluster (`r9m`'s and `tla`'s lines cross here) | not traced here |
| x 3645-3695, y 2595 to beyond 4060 | **west rail: VSS**. One metal with the east VSS rail (x 3995-4045) through a wide link along y 2595-2648 (`top_m.png`, 2.2x metal; `follow.py 3667 3400 N`: corners (3680,2638) E, (4028,2638) S). The mirror of `tla`'s R1 | drawn to y 4060 |
| x 3575-3880, y 3212-3652 | latch A (below) | traced |
| x 3575-3880, y 3688-4046 and 4469-4827 | NOR 1, NOR 2, NOR 3, NOR 4 (below) | traced |
| x 3575-3880, y 4046-4330 | the cross-coupled pair (below): the mirror image of `tla`'s `rcs_u3425` and `rcs_b1` (`findcell` on the clean shot, window 3570 4040 3880 4345: -792,-651 mx=3725, 0.71) | traced |
| x 3575-3880, y 4345-4490 | the inverter (below): `tl1`'s inverter (2535 4215 2835 4345) at 1041,130 (`findcell` 0.76) | traced |
| x 3575-3880, y 4818-5258 | latch B (below): `tl1_ua` and `tl1_ub` again at 1042,478 (`findcell` 0.80, 0.82) | traced |
| x 3540-4250, y 5318-5342 | a poly row east from the pad (3540,5328) of latch B's enable metal, under the rail and across the cluster's foot. The outlined areas above and below it in the open stretches are the field slots between the foot's rows, not diffusions (run 9: `opendiff.py 3533 5300 4250 5660`) | drawn to its east pad (4148,5330) |
| east column, y 4165-4335 and 4990-5160 | the two NOR units (below) | traced |
| x 4099-4111, y ~3020-4152 | a thin metal down the east column over `tla`'s units, from a pad (4100,2900); it turns east at y 4152-4168 to the pad (4148,4200) and is track A from there. Bright most of the way (`px.py col 4101 3000 3880 20 metal,metal1`). Where it makes contact north of y 4106 is not read; over `rcs_in1`'s node box at (4102,4074) it has a bright centre in a dark surround in both metal shots and a patch in the clean shot that is neither a contact's green (186/182/139 against 140/150/85 at the contact (4146,4070)) nor a pass-over's tan (197/171/120 at (3606,5026)): undecided (`en_in1.png`, `en_in1b.png`, 9x) | drawn end to end (run 10): from its north pad (4103,2899) on the row y 2899, firm with six uncertain stretches over node boxes (Ambiguities 12, 13) |
| x 3870-4250, y 4514-4970 | **latch C** (below): `tl1_ua` and `tl1_ub` mirrored (`findcell`, clean shot: 1333,174 mx=2662.5, 0.75; 1334,174 mx=2662.5, 0.80) | traced |
| x 3948-3962, y 3616-5459 | a thin metal between the rails, over the east column's loads (the middle cluster's counterpart of `tla`'s thin metal E). **Its ends** (review 7, checked: `textmap.py 3906 3590 3972 3640 3`, `3920 5436 3980 5480 3`): north, it turns west at y ~3606 onto a pad with a contact (3930,3616), the foot of the load plate (x 3912-3950, y 3485-3600) of the rail unit at y 3440-3610; south, a pad with a contact (3953,5459) whose poly leaves west along y ~5450-5464. `follow.py 3955 4300 N` stops at y 3616 (its end), `S` at y 4454 (a stop only: it is there, bright, from y 4500 to 4960). Over latch C one contact-like spot, (3955,4541), taken as a pass-over (Ambiguity 6) | drawn end to end (run 9): firm, with six uncertain stretches over tie boxes (Ambiguity 11); no contact on the way |
| east column, y 3450-3660, 3655-3745, 4345-4514 | the units built under the rail (below) | traced |
| east column, y 5180-5300 | the inverter under the rail's south end (below) | traced |
| east column, y 2950-3090 | the top unit E1 (below): an inverter under the rail; its load plate is one poly with the row y 2957-2973 to latch A's enable pad (3606,2985) | traced |
| y 5345-5660 | the foot: a crossing field of poly rows (y 5371, 5415, 5458, 5500, and `tla`'s 5543, `bw`'s 5585, `amrw`'s and `tl4`'s 5631) under the cluster's metals; no diffusion (below) | traced (run 9) |
| y 5660-6350 | sparse wiring between the foot and the left array: the pads at the south ends of three metals, four poly rows (y 5718, 5936, 6065, 6327; `tla`'s y 5848 and `amrw`'s y 5979 were drawn by those blocks), the two rails' turns east (two Ls) and their legs south, the north pads of two of `ur`'s counter lines; no diffusion (`opendiff.py 3533 5660 4250 6350`: none) | traced (run 11) |

There is **no thin metal W** in this cluster's west column (the first cluster has one at
x 2689-2703): the middle of each unit, x 3700-3760, is in the open here, so the chip-2 shots
show its poly as orange.

## Logic

### Latch A (west column, y 3212-3652): traced

    tl3_w3233 = NOT tl3_w3333
    tl3_w3419 = NOT( tl3_w3333 AND tl3_w3373  OR  tl3_w3550 )
    tl3_w3550 = NOT( rcs_x1  OR  tl3_w3373 AND tl3_w3233  OR  tl3_w3419 )

A cross-coupled pair: open while `tl3_w3373` is high, when `tl3_w3550` takes `tl3_w3333`
and `tl3_w3419` its inverse; `rcs_x1` high clears it (`tl3_w3550` low). The same circuit
as `tl1`'s two latches and its third (`notes/blocks/tl1.md`). **Traced**: the equations, by
extraction. **Believed**: the cross-coupling from `tl3_w3419` to the third pull-down of the
lower unit, which runs over the upper unit's load plate and the thin metal x 3783 and so
rests on the plate's tie (`?` in `tl1`'s cell; `@alias tl3_w3419 tl3_w3368`), and likewise
the other way through the lower unit's plate (AMB-026 covers `tl1`'s copies of the same tie).

How it was traced:

- `findcell` on the clean shot: `tl1_ua` (2535 4340 2790 4590) at 1041,-1128, score 0.79;
  `tl1_ub` (2535 4590 2790 4780) at 1041,-1128, score 0.80. Placed as `@inst`.
- `tools/t.sh tl3 cellcheck.py tl1_ua --bbox 2535,4340:2840,4595 --layer acid1b --only a`:
  8 of 61 blocks bad, median 0.93; `tl1_ub --bbox 2535,4590:2840,4800`: 8 of 52, 0.91. The
  tinted blocks are the unit's middle column (protected by thin W in the master, open here)
  and the VCC boxes' pits.
- The middle column at 4x in three shots (`la_mid1.png`, `la_mid2.png`): row y 3222-3245 with
  the buried box 3729-3761 on the node column, the plate's stem and plate (3763-3816 x
  3267-3332), the wide node y 3275-3312, the top bar y 3358-3371 with the thin metal's pad
  (3783,3368), the tie box (3715-3745, 3375-3400); in the lower unit the node strip
  x 3738-3757 widening at y 3606, the third gate's band y 3616-3638 with its rounded west end
  at x 3722. All as the master.
- Under the rail (`railprof.py 3645 3690 3180 3720`): gates at y 3325-3337, 3368-3381,
  3439-3445, 3577-3588, 3620-3641, as the cells' stacks; VSS box y 3651-3719 below, with a
  contact ring in both metal shots (`textmap.py 3636 3648 3704 3726 4 --acid`: ring
  3644-3700 x 3664-3692, bright centre x 3656-3668).
- Metal overlay `la_mov.png` (2.3x): the rail contacts (3661,3292), (3669,3482), the VCC
  contacts, the thin metals x 3605 (`follow.py`: y 3234-3650) and x 3783 (y 3370-3576).

Rows and wiring outside the cells (`la_west.png` 2.4x, `la_rows.png` 3.5x in three shots):

| Row | Net | Where it goes |
|---|---|---|
| y 3324-3342 | `tl3_w3333` (data) | west under the metal x 3540 (no pad) and out of the strip; it turns north at x 3510-3525 |
| y 3364-3382 and y 3580-3600 | `tl3_w3373` (enable) | each ends on a pad with a contact under the metal x 3531-3549: (3540,3372) and (3540,3590). The metal runs on north to y 2988 and east to a pad (3606,2985) (`follow.py 3540 3450 N`; `la_pad.png`, 4.5x four shots: ring and bright centre in both metal shots, green centre on a salmon pad). A poly row y 2955-2975 leaves that pad east: not drawn |
| y 3409-3429 | `tl3_w3419` (inverted output) | west under the metal x 3540 (no pad) out of the strip, to a pad (3495,3418) under a metal going south |
| y 3497-3515 | `rcs_x1` (clear) | west under the metal x 3540 (no pad) out of the strip, to a pad (3455,3503) |
| y 3540-3560 | `tl3_w3550` (output) | a stub: rounded end at x ~3570. The true output is not taken west here |

### Latch B (west column, y 4818-5258): traced

    tl3_w4839 = NOT tl3_w4720
    tl3_w5025 = NOT( tl3_w4720 AND tl3_w4978  OR  tl3_w5156 )
    tl3_w5156 = NOT( rcs_x1  OR  tl3_w4978 AND tl3_w4839  OR  tl3_w5025 )

Latch A's circuit again, 1606 px lower: open while `tl3_w4978` is high, when `tl3_w5156` takes
the data and `tl3_w5025` its inverse; `rcs_x1` high clears it. **Its data is NOR 4's
output**, `tl3_w4720` = NOR(`tl3_w3803`, `tl3_w4763`). Traced: the equations, by extraction.
Believed: the two cross-couplings, which rest on the plates' ties as in latch A (AMB-026;
`@alias tl3_w5025 tl3_w4974`).

- `findcell` (clean shot): `tl1_ua` and `tl1_ub` at 1042,478 (0.80, 0.82). `cellcheck.py tl1_ua
  --bbox 2535,4340:2840,4595 --layer acid1b --only b`: 6 of 61 blocks bad, median 0.94;
  `tl1_ub --bbox 2535,4590:2840,4800`: 5 of 52, 0.94.
- Overlays `lb_ov1.png`, `lb_ov2.png` (3.4x, clean shot), `lb_m1.png`, `lb_m2.png` (3.3x,
  metal): the rail contacts, the pads, both thin metals (`follow.py 3605 5050`: y 4842-5256;
  `follow.py 3783 5080`: y 4972-5182).
- Under the rail (`railprof.py 3645 3690 4800 5400`): gates at y 4932-4953, 4975-4996,
  5047-5066, 5184-5204, 5233-5247, the cells' stacks; the VSS box below from y 5255, with a
  contact ring in the metal shot at (3662,5284).
- The VCC box of the lower unit is the cell's own here (clean shot tan y 5008-5126 down
  x 3847), not the longer box latch A has; one contact drawn at (3847,5030) (ring in both metal
  shots: `textmap.py 3826 4996 3870 5050 3`).

| Row | Net | Where it goes |
|---|---|---|
| y 4930-4948 | `tl3_w4720` (data) | the poly of the pad (3540,4912), NOR 4's output |
| y 4970-4988 and y 5186-5206 | `tl3_w4978` (enable) | each ends on a pad with a contact under the metal x 3534-3549: (3541,4980), (3541,5199). The metal (`follow.py 3540 5080`: y 4978-5332) has a third contact on a pad (3541,5328), whose poly runs east along y 5318-5342 under the rail and on across the cluster's foot: drawn to x 3640 (`lb_en.png`, 3x metal and clean shot; `textmap.py 3520 4964 3562 4992 2`, `3520 5182 3562 5210 2`, `3516 5310 3566 5350 2`: ring, bright centre and green hole at each) |
| y 5015-5035 | `tl3_w5025` (inverted output) | west under the metal x 3540 (no hole: `textmap.py 3522 5008 3560 5042 3`) out of the strip |
| y 5103-5121 | `rcs_x1` (clear) | from the west, under the metal x 3540 (no hole: `textmap.py 3522 5096 3560 5128 3`) |
| y 5146-5166 | `tl3_w5156` (output) | a stub on the node's box, as in latch A |

### The east column's two NOR units: traced

    tl3_e4243 = NOR(inh_ck, rcs_mv)        unit e3, y 4165-4335
    tl3_w4978 = NOR(inh_ck, tl3_e5114)     unit e5, y 4990-5160: latch B's enable

The standard unit of `tla`'s east column (`rcs_c1`'s) again: a diffusion column east of the
rail (x 4072-4105) between two arms onto the rail's VSS boxes, two gate rows from the bus field,
the node between them with a buried contact to the output row, and the load west of the rail
(node strip under the rail and the thin metal x 3948-3962 to a plate x 3884-3939 and a VCC box
under the VCC rail, shared with the west column's loads; tail and tab tie). Cell `tl3_enor`:
`tla`'s lines for `rcs_c1`'s unit moved by 1042,1127; copy at 0,825.

- `findcell` (clean shot, 2778 3030 3088 3200): 1042,1127 (0.88), 1042,1952 (0.71). Overlays
  `en_ov.png` (2.9x, both stripped shots), `e5_ov.png` (2.8x, clean and metal).
- The VSS box above e3 (4008-4056, 4141-4190, contact marks at (4020,4150-4170) in both stripped
  shots) is the land `tla` drew as `?D 4005,4130:4092,4165` below `rcs_in1`'s gate `rcs_mv`
  with a `?C`: one box, so that land's VSS contact is now drawn firm.

Wiring (`en_bus.png` 3x, `en_padA.png` 6x, `en_w1.png`, `en_w2.png` overlays):

| Wire | Net | Where it goes |
|---|---|---|
| e3 gate 1, y 4191-4209 | `inh_ck` | east to a pad with a contact (4148,4200) on **track A**, a metal x 4141-4155 that runs south to y 5008 (`follow.py 4148 4290 S`) with four more pads, (4146,4510), (4146,4681), (4146,4900), (4147,5005), each with a hole in the clean shot and a poly row leaving it (`textmap.py 4130 Y-14 4168 Y+14 3`). North of the pad it turns west along y 4152-4168 and north at x 4099-4111 (`follow.py 4148 4290 N`) as the thin metal of the Inventory. Drawn from y 4106 to y 5012 |
| e3 gate 2, y 4280-4300 | `rcs_mv` | east under track A (no hole) to a pad with a contact (4190,4288) on `tla`'s track x 4192 |
| e3 output, y 4232-4252 | `tl3_e4243` | east under both tracks (no hole: `textmap.py 4128 4184 4256 4304 3`) to a pad with a contact (4236,4246); its metal leaves east into `tl4`'s strip (it turns north at x 4323 and runs to y 2772: `follow.py 4270 4243 E`) |
| e5 gate 1, y 5016-5034 | `inh_ck` | east to the pad (4147,5005), where track A arrives from the north. **The net goes on** (found by the review): a metal arm leaves the pad west along y 4996-5008 to x ~4106 and runs south at x 4100-4112, beside the metal x 4148 and apart from it, to a pad with a contact (4104,5633), whose poly leaves east along y 5620-5645, not followed (`arm1.png`, `arm_s.png`, 5x; `textmap.py 4084 5612 4130 5656 3`). It passes over e5's node box (y 5050-5083) and over a boxed poly end at 4088-4112 x 5188-5216 where the row y ~5195-5207 ends: neither has a hole in the clean shot (`px.py col 4104 5090 5622 3 acid1b`, and at x 4108, 4112: green only for 3-6 px at y 5183-5186), so both are taken as pass-overs (assumed, tracing guide trap 22) |
| e5 output, y 5057-5077 | `tl3_w4978` | east to a pad with a contact (4147,5070) at the north end of a metal x 4142-4155 (`follow.py 4148 5090`: y 5064-5332), which crosses three rows without a hole (`textmap.py 4124 5098 4262 5130 3`, `4130 5186 4168 5252 3`) and ends on a contact (4148,5330) on the east pad of latch B's enable row (`textmap.py 4126 5300 4172 5352 3`). That row, y 5318-5342, is one poly from x 3550 to x 4132: no break and no other hole (`px.py row 5330 3560 4160 3 acid1b`) |
| e5 gate 2, y 5105-5123 | `tl3_e5114` | from the east, across the bus field under four tracks without a contact; out of the strip at x 4250 |

So latch B is open while `inh_ck` and `tl3_e5114` are both low. `inh_ck` is the east
column's distributed line (five gate pads on track A, and a sixth pad at (4104,5633)).

### Latch C (east column, y 4514-4970): traced

    tl3_e4537 = NOT tl3_e4635
    tl3_e4720 = NOT( tl3_e4635 AND inh_ck  OR  tl3_e4852 )
    tl3_e4852 = NOT( rcs_x1  OR  inh_ck AND tl3_e4537  OR  tl3_e4720 )

The circuit of latches A and B a third time, as a mirror image east of the east rail: open
while `inh_ck` is high, when `tl3_e4852` takes the data `tl3_e4635` and `tl3_e4720` its
inverse; `rcs_x1` high clears it (`tl3_e4852` low). **Its enable is `inh_ck`, track A**:
both enable rows end on track A's pads (4146,4681) and (4146,4900). Latch B is open while
`inh_ck` and `tl3_e5114` are both low (`tl3_w4978`), so B and C are never open together.
**Traced**: the equations, by extraction. **Believed**: the two cross-couplings, which run
over the load plates and rest on the plates' ties (`?`, as in `tl1`'s cells: AMB-026;
`@alias tl3_e4720 tl3_e4675`).

How it was traced (run 6):

- `findcell` (clean shot): `tl1_ua` at 1333,174 mx=2662.5 (0.75), `tl1_ub` at 1334,174
  mx=2662.5 (0.80). `cellcheck.py tl1_ua --bbox 2535,4340:2840,4595 --layer acid1b` on the
  mirrored copy: 5 of 61 blocks bad, median 0.91; `tl1_ub --bbox 2535,4590:2840,4800`: 5 of 52,
  0.92. The bad blocks: the two VCC boxes' pits; the strip the thin metal x 3948-3962 protects
  (7 px west of where the mirror puts thin W); latch B's VCC box at the copy's lower left, which
  the master does not have; a blemish of chip 1 on the output row at (3978,4533) (plain in the
  chip-2 stripped shot).
- Poly and diffusion are the cells' lines mirrored (x' = 6658 - x for `tl1_ua`, 6659 - x for
  `tl1_ub`, y + 174), checked on `lc_ov1.png`, `lc_ov2.png` (3x clean shot) and `lc_w1.png`,
  `lc_w2.png` (3x, metal, clean and chip-2 stripped with the outlines).
- **The metal and the contacts are not where the mirror puts them** (re-read item R34: the
  layout was drawn again). The rail is x 3992-4041 where the mirror gives 4004-4054; the unit's
  thin metal is at x 4077-4089 (mirror 4087-4101); the rail contacts are at (4031,4599) and
  (4022,4790) (mirror (4038,4594), (4031,4784)); the VCC contact at (3846,4616) (mirror
  (3855,4621)). So the units are written out in `trace/tl3.txt`, not instanced, and every
  contact is placed from a text map of this copy (`tools/t.sh tl3 textmap.py 4000 4570 4064 4626
  3`, `4000 4758 4064 4822 3`, `3818 4576 3886 4832 4`, `4056 4514 4126 4566 3`, `4062 4690 4126
  4960 3`, `3884 4656 3936 4700 3`, `3884 4852 3936 4900 3`: each a ring with a bright centre in
  both metal shots and a green hole in the clean shot). Metal overlay `lc_mov.png` (2.6x).
- The lower unit's gate 2 and its third gate's band are two polys: open field at x 3972-3990
  between the band's end and gate 2's rounded end at x ~4003 (`px.py row 4930 3936 4014 3
  acid1b,acid,metal`), as in the master.
- The stack's diffusion runs on below gate 2 onto e5's upper VSS box (`railprof.py 3992 4041`:
  diffusion y 4949-5013), which is also where the third pull-down's VSS strip y 4956-4970 lands.
- The VCC box of the lower unit and of the upper unit's three-input gate is one box
  y 4704-4818 with NOR 4's (west column), with a long contact ring y ~4744-4800 south of NOR 4's
  contact; the inverter's VCC box (y 4578-4646) has its own contact (3846,4616).

Wiring (`lc_e1.png`, `lc_e2.png` 2.3x metal and clean; `lc_bf1.png`, `lc_bf2.png` 3x in three
shots; the text maps named):

| Wire | Net | Where it goes |
|---|---|---|
| data, row y 4627-4642 | `tl3_e4635` | from the east: under track A, `rcs_mv`'s track and the track x 4236 without a contact (`textmap.py 4120 4618 4252 4652 3`: poly unbroken, no hole, no ring), out of the strip at x 4250. Its west end turns north along the rail's west edge as the inverter's gate |
| the inverter's output, row y 4527-4546 | `tl3_e4537` | west onto the node's buried contact box and the load plate's stem; east under the rail to a pad with a contact (4086,4540); a thin metal x 4077-4089 from it south to the pad (4097,4941) of the lower unit's gate 2 (`follow.py 4082 4600`: (4085,4536)-(4077,4702), a stop where the metal is dark over the node's box; `textmap.py 4062 4690 4126 4960 3`: metal on both sides of each dark stretch (y 4708-4735 over the upper node's box, y 4837-4866 over the lower node's box), no hole between the pads; the metal is 15 px wide over field at y 4744-4765) |
| enable, rows y 4666-4684 and y 4882-4902 | `inh_ck` | each ends on a pad of track A: (4146,4681), (4146,4900) (run 5's contacts) |
| the upper node, y 4705-4736 | `tl3_e4720` | the poly on its box is a stub (rounded end at x ~4125, `lc_bf1.png`). It leaves by the plate: the thin metal x 3902-3914 (`follow.py 3908 4780`: (3914,4646)-(3907,4880)) from a contact (3909,4674) on the plate to a contact (3908,4877) on the pad of the lower unit's third gate (`tl3_e4675`, aliased) |
| clear, row y 4800-4817 | `rcs_x1` | east under track A (no hole) to a pad with a contact (4190,4808), the north end of a metal x 4186-4199 on `rcs_mv`'s track (no metal between `rcs_mv`'s pad (4192,4743) and this one: `px.py col 4192 4290 4830 12 metal,metal1`: 160/144/88 at y 4770-4782; `lc_bf1.png`). The metal runs south to y 5896 and turns east out of the strip (`follow.py 4192 4870 S`: corner (4201,5896) E, on to (4629,5893); `textmap.py 4172 5874 4262 5916 3`: a plain corner, bare ground south and west of it, no hole). On the way it has **a second contact (4192,5373)** on a pad whose poly row y 5366-5376 runs west across the cluster's foot (`textmap.py 4170 5364 4216 5406 3`, `4100 5356 4262 5392 3`: ring, bright centre, green hole; the row passes under the metal arm x 4100-4112 of `inh_ck` without a hole): drawn to x 4124, not followed |
| output, row y 4843-4859 | `tl3_e4852` | east under track A and the clear's metal without a contact (`textmap.py 4120 4834 4252 4870 3`) to a pad with a contact (4234,4852), the south end of a metal x 4229-4243 (`follow.py 4238 4700`: (4234,4432)-(4235,4856); bare ground north of y 4440). Its north end has a contact (4236,4461) on a pad whose poly row y 4453-4466 runs west under two tracks without a contact (`textmap.py 4110 4440 4262 4482 3`) to the rail, where a gate lies under the rail at y 4453-4477 (the unit at y 4350-4514, not drawn): drawn to x 4118 |

Two wires of other nets drawn with it:

- **`inh_ck`'s pad (4146,4510)**: its row y 4496-4510 runs east under two tracks without a
  contact (`textmap.py 4126 4486 4254 4520 3`) and out of the strip at x 4250, where `tl4` has
  it as `inh_ck`, gate 2 of its three-input NOR `tl4_w4545`. One net (`@alias inh_ck
  inh_ck`; the geometry joins at x 4250).
- **`rcs_mv`'s track ends on a pad with a contact (4192,4743)** (`tla` had "bottom end not
  looked at"); the pad's poly leaves east along y 4736-4751 under the metal x 4229-4243 without
  a contact and crosses x 4250 (`textmap.py 4170 4722 4254 4762 3`). So `rcs_mv` comes from the
  east (the glossary already says: a poly that leaves the bus field at (4283,4745)).
- **`rcs_mv`, a wire that only passes through** (found by review 7): a pad with a contact
  (4234,4918) on the track x 4236, 60 px below latch C's output pad and apart from it (bare
  ground y 4877-4892 in both metal shots). The pad's poly leaves east across x 4250 along
  y 4904-4925; a metal x 4229-4243 runs south from the contact to y 5766 and turns east out of
  the strip (`follow.py 4236 4990 S`: corner (4245,5770) E, on to (4411,5762)). No hole under it
  on the way and a plain corner (`textmap.py 4204 4868 4264 4940 3`, `4224 4930 4251 5790 3`
  filtered for green samples, `4216 5744 4264 5790 3`). Both ends are in `tl4`'s strip.

### The NOR under the east rail, y 4345-4514: traced, one link uncertain

    rcs_mv = NOR(tl3_e4372, tl3_e4852)

**This is the driver of `rcs_mv`**, the second input of the NOR that makes `rcs_in1` (so
`rcs_in1` = R9's match AND (`tl3_e4372` OR latch C's output `tl3_e4852`)) and gate 2 of e3.
A unit built under the rail: one diffusion column under the rail and east of it (x 4005-4076),
from e3's lower VSS box down to a VSS box of its own (contact (4028,4495)); two gate rows from
the bus field cross it, and the node is between them.

- Column and gates: `px.py col 4017 4340 4520 6 acid1b,acid` (clean shot under the rail: tan,
  gate y 4365-4381, tan y 4388-4442, gate y 4450-4470, tan to y 4512); east of the rail the
  chip-2 shots show the column plain between edge lines at x 4046 and x 4078 with both rows
  orange across it (`rn1_out.png`, 4.2x, three shots; `rn1_b.png`, 3.3x both stripped shots).
  The VSS contact: `textmap.py 3996 4474 4084 4522 3 --acid` (ring, bright centre, green hole).
- Gate 1, `tl3_e4372`: a row y 4366-4380 from the east, under track A and `rcs_mv`'s track
  without a contact, out of the strip at x 4250 (`textmap.py 4086 4352 4262 4396 3`: poly
  unbroken, no hole, no ring; no metal on the track x 4236 at this y).
- Gate 2, `tl3_e4852`: latch C's output row, the row of the pad (4236,4461), drawn in run 6 to
  x 4118 and here on west across the column.
- **Output.** East of the column a buried contact box: heavy frame 4083-4112 x 4402-4432, light
  centre 4090-4101 x 4413-4425, in both chip-2 shots (`px.py row 4420 4040 4146 3`, `col 4096
  4388 4446 3`; `rn1_box.png`, 6x four shots). A poly row y 4410-4426 leaves it east, passes
  under track A without a contact and ends on a pad with a contact (4193,4420) on `rcs_mv`'s
  track (`textmap.py 4104 4398 4262 4440 3`: ring and bright centre in both metal shots, a
  green hole 4191-4200 x 4416-4425 in the pad). **The link from the column to the box is
  uncertain** (`?D 4070,4408:4102,4428`): the column's east edge line and the box's west frame
  merge into 15 px of dark (x 4073-4088) and no shot resolves the 10 px of diffusion between
  them (Ambiguity 9). Without it the node has no output and the box hangs.
- Load: the node's strip y 4402-4436 runs west under the rail, through the gap between the rail
  and the thin metal x 3948-3962, under that metal and under a plate x 3912-3948, y 4384-4444
  to the VCC box of the west column's inverter (`px.py row 4420 3870 4012 4`, `col 3925 4368
  4500 4`; `rn1_load.png`, 3x three shots). W/L 34/36. In the gap (x 3972-3986) the clean shot
  shows the strip only as a dark bar (trap 2) and I first took it for a vertical poly; the
  chip-2 metal shot is plain there, not orange (`px.py col 3976 4380 4504 4`, and the
  calibration `px.py pt 4100,4373 4120,4462 4095,4199 4064,4420 4066,4410 ...`: open poly
  169-171/129-139/53-74 in the chip-2 stripped shot, open diffusion 165-176/138-151/90-97).
- The tie (`?`): a tail of the strip runs down the gap (x 3966-3984, to y 4486) to a heavy box
  (3927-3970, 4455-4488) under the thin metal, where the plate's tab (x 3916-3938 down to
  y ~4480, then east) meets it. The standard tail-and-tab tie, read from outlines, drawn `?`.

Overlay `rn1_ov.png` (2.4x, metal and clean shot).

### The NOR under the east rail, y 3450-3660: traced; its tie uncertain

    tl3_e3550 = NOR(rcs_mu, tc2_o5175)

One diffusion under the rail (x 4005-4054) from a VSS box above (contact (4029,3468)) to a VSS
box below (a long contact, (4029,3637)), with a part east of the rail (x 4050-4082,
y 3468-3625); two gate rows from the bus field cross it and the node is between them
(`px.py col 4017 3440 3830 6`; `rn2_b.png`, 3.3x both stripped shots; `textmap.py 3999 3444 4089
3498 3`, `3999 3602 4089 3664 3`).

- Gate 1, `rcs_mu`: the row y 3497-3514 ends on a pad with a contact (4190,3506) on `rcs_mu`'s
  track (`textmap.py 4160 3482 4216 3526 3`; `rn2_bf.png`, 3x).
- Gate 2: the row y 3582-3600 ends on a pad with a contact (4148,3592), the south end of the
  metal x 4138-4160 (`tla`'s lower piece of track P; `textmap.py 4124 3570 4176 3700 4`). `r9m`
  joins that piece to its line 3 by the stub at y 3376 (its notes: 5-6 px of dark at the join,
  taken as an edge under continuous metal), and `tl6` joined line 3 to `tc2_o5175`: so the
  gate is `tc2_o5175` = NOR(`tc1_x1`, `fld_b_in`) in the full extraction. That rests on `r9m`'s
  stub; with `tl3` alone the gate is the unnamed track piece.
- The node's box east of the rail (4074-4110, 3534-3572) carries only a stub of poly ending at
  x ~4125. **The thin metal x 4099-4111 (`inh_ck`'s north part) passes over it without
  contact**: dark for 36 px (y 3532-3568) with no bright centre in either metal shot, protected
  poly and no hole in the clean shot (`textmap.py 4050 3514 4130 3584 3`; `rn2_east.png`, 5x
  four shots: the "ring" there is the stub's rounded end).
- Load: the node's strip y 3533-3566 runs west under the rail, the gap and the thin metal
  x 3948-3962, under a plate x 3913-3950, y 3516-3600 to latch A's lower VCC box (`px.py row
  3550 3872 4010 4`, `col 3930 3470 3634 4`). W/L 33/37.
- **The plate's foot is a pad with a contact (3930,3614): the north end of the thin metal
  x 3948-3962** (`textmap.py 3906 3590 3972 3640 3`: ring, bright centre, green hole; the metal
  leaves east and south, none north of y 3600). So the node's way out is its load plate and
  that thin metal, if the plate is tied to the node.
- The tie (`?`): a tail of the strip runs up the gap, x 3966-3984 to y ~3486 (diffusion: `px.py
  col 3977 3476 3548 6`, no edge at y 3533; drawn firm since review 9), and beside it, under
  the thin metal, all shots are heavy dark over x 3928-3972, y 3486-3530 (`px.py row 3508 3900
  3996 4`, `col 3968 3480 3580 4`): the box where the plate's tab would meet the tail. The tab
  and the buried contact are drawn uncertain (Ambiguity 10).

**The thin metal x 3948-3962** was not drawn between y 3640 and y 4500 until run 9, because over
every load-tie box it crosses it is dark in both metal shots and the clean shot is greenish under
it (`textmap.py 3945 3625 3969 4500 3`; `textmap.py 3930 4440 3982 4506 2 --acid`). Run 9 drew it
end to end, with those stretches uncertain: "The thin metal x 3948-3962, end to end", below, and
Ambiguity 11.

### The inverter under the east rail, y 3655-3745, and `rcs_mn3852`'s upper gate: traced

    tl3_e3712  = NOT tc2_o5175
    rcs_mn3852 = NOR(tl3_e3712, rcs_in1)      (`tla`'s unit; its load is not drawn)

- The gate row y 3669-3688 is one poly with the pad (4148,3592): the pad's poly runs south
  (x 4146-4158) into the row's east end (`textmap.py 4124 3570 4176 3700 4`; `rn3_bf.png`,
  `rn3_polys.png`). The transistor is under the rail only, between the VSS box (4029,3637)
  and the node y 3693-3716: east of the rail there is field above the row (`px.py col 4066
  3655 3800 4`: chip-2 stripped shot red minus green 12 at y 3655-3659).
- The node goes east by a link y 3704-3718 into a buried contact box (frame 4079-4118 x
  3700-3738; `px.py row 3718 4040 4130 3`, `rn3_east.png`), whose poly is **one C-shaped line**
  round a field island (4118-4143, 3735-3795): east along y 3708-3734, south along
  x 4144-4168, back west along y 3799-3819, under the thin metal x 4099-4111 and across the
  column of `tla`'s unit `rcs_mn3852` as its upper gate, which `tla` had "not read yet"
  (`rn3_polys.png`, 4.6x: orange in both chip-2 shots; `rn3_bf2.png`; `px.py row 3808 4030 4130
  4`: the column's west edge at x 4070-4074 under the poly, bright salmon over the channel).
- The thin metal x 4099-4111 passes over this box too, read as a pass-over (review 9): about
  50 px of dark with a bright centre 8 px wide at (4101,3719) in both metal shots
  (183/163/76, 155/130/56), where `follow.py` stops, but the clean shot there is tan
  (200/169/132), not a contact's green hole (143/152/86, 154/166/99 at real contacts). The
  same signature as the undecided spot (4102,4074) of Ambiguity 1; no contact drawn.
- The top of that unit, drawn here: the rail's VSS box (contact (4027,3775): `textmap.py 4002
  3752 4062 3798 3`), an arm east y 3778-3794 (`px.py row 3786 4040 4124 4`) and the column
  x 4072-4106 down to `tla`'s node at y 3838 (`px.py col 4085 3764 3850 4`: arm, gate
  y 3799-3819, node from y 3826). Between the inverter's box and that arm, east of the rail,
  is field (y 3727-3767 at x 4066).
- Load: strip y 3700-3725 west under the rail, the gap and the thin metal, under a plate
  x 3884-3938, y 3680-3743 to a VCC box of its own (tan y 3674-3722, contact (3846,3695):
  `textmap.py 3820 3640 3884 3752 4`; `px.py col 3910 3640 3752 4`, `row 3711 3868 4012 4`;
  `rn3_load.png`). W/L 25/54. The tie (`?`): a heavy box x 3912-3944, y ~3655-3685 above the
  plate and diffusion colour under the thin metal beside it (`px.py row 3670 3880 3996 4`).

Overlay of both units: `rn23_ov.png` (1.6x, metal and clean shot).

### The inverter under the south end of the east rail, y 5180-5300: traced; its tie uncertain

    tl3_e4635 = NOT tl3_e5240

**Its output is, by a track in `tl4`'s strip, the data of latch C** (believed: the track is
measured at both ends and not drawn, so the name carries `_u`).

- The east rail ends at y ~5296 (`textmap.py 3960 5176 4130 5316 4 --acid`: bright metal at
  x 3996-4004 down to y 5292). Under it one diffusion column x 4012-4054: the node
  (y 5202-5226), the gate (y 5231-5250, bright salmon 232-240/157-169 in the clean shot) and a
  VSS box (y 5254-5298) with a contact (4028,5278): ring with a bright centre x 4024-4032,
  y 5272-5284 in both metal shots (`px.py col 4017 5176 5330 4`, `row 5241 3984 4100 4`: a dark
  line at x 4008-4012 is the column's west edge under the gate; `row 5270 3990 4110 4`).
- **The transistor is under the rail only.** East of the rail, below the gate row, the rectangle
  x 4062-4092, y 5256-5308 is field: the same in all four shots as the field at (3895,5270)
  (`px.py col 4075 5250 5326 3`, `pt 3895,5270 4066,5185`; `opendiff.py 3870 5160 4130 5320`:
  none; `rg_se.png`, 4.4x three shots). Its four sides are the rail, the gate row, the thin
  metal x 4100-4112 and the row y 5318-5342.
- Gate, `tl3_e5240`: a row y 5231-5250 from the east, under the metals x 4105, 4148, 4192 and
  4236 without a contact (edge bars only, poly unbroken and no hole in the clean shot:
  `textmap.py 4110 5180 4480 5258 5 --acid`), across x 4250; in `tl4`'s strip it turns south at
  x ~4265-4290.
- **Output.** The node goes east of the rail as a diffusion y 5203-5222 (`px.py pt 4070,5213`:
  chip-2 stripped shot 167/143/95, diffusion; the gate row at (4064,5241) is 175/116/69, poly)
  into a buried contact box (heavy frame 4079-4113 x 5187-5218; `rg_box.png`, 4.7x three
  shots). A poly row y 5190-5205 leaves the box east (`px.py col 4126 5170 5262 3`, `col 4170`),
  under the same three tracks without a contact, across x 4250. **In `tl4`'s strip it ends on a
  pad with a contact (4278,5198)** (`textmap.py 4246 5168 4312 5232 3`: bright centre
  x 4273-4282, y 5195-5201 in a ring in both metal shots, hole x 4276-4282 in the pad), the
  south end of a metal x 4279 that runs north (`follow.py 4279 5165 N`: to y 4631) to **a pad
  with a contact (4278,4636) on the east end of the row y 4627-4640, which is `tl3_e4635`,
  latch C's data** (`textmap.py 4240 4606 4312 4664 3`: bright centre x 4273-4282, y 4633-4639,
  hole, the row's poly arriving from x 4240). The track and its two pads lie 28 px inside
  `tl4`'s strip, which is claimed, and are not drawn: the row is drawn to x 4250 and named
  `tl3_e4635`.
- The thin metal x 4100-4112 (`inh_ck`'s south arm) passes over the box: Ambiguity 12.
- Load: the node's strip y 5200-5226 runs west under the rail, through the gap (diffusion:
  `px.py row 5214 3816 4014 4`, chip-2 stripped shot blue 88-94 at x 3976-3984, where poly has
  53-74), under the thin metal x 3948-3962 and under a plate x 3884-3936, y 5182-5240 to a VCC
  box (x 3828-3880, y 5200-5260) with a long contact (3844,5226) (`textmap.py 3816 5172 4000
  5312 4 --acid`: bright centre x 3836-3852, y 5214-5238 in a ring; `px.py col 3908 5166 5250 3`:
  the plate is poly from y 5181 to y 5238 in both chip-2 shots, with the strip's edges across
  it at y 5196 and y 5224; `rg_load.png`, 4.2x three shots). W/L 24/52.
- The tie (`?`): a tail of the strip runs south **under the thin metal** (x 3946-3964, to
  y ~5272: tan in the clean shot, an outlined strip in the chip-2 stripped shot; in the other
  rail units the tail is in the gap), and a tab of the plate runs south (x 3915-3938) into a
  heavy box (3910-3944, 5244-5276) beside the tail's end. How the box meets the tail is not
  resolved (Ambiguity 10).

Overlay `rg_ov.png` (2.9x, metal and clean shot).

### The top unit E1, y 2950-3090: traced; its tie uncertain

    tl3_w3373 = NOT tl3_e3028        (the node is tl3_e3000; the join to tl3_w3373 is the plate's tie)

**This is the driver of latch A's enable.** The same build as the inverter at y 5180-5300.

- Column under the rail, x 4012-4054: the node (y 2990-3014), the gate (y 3018-3038, 214-246/
  114-159 in the clean shot) and a VSS box (y 3042-3088) with a contact (4029,3064) (`px.py col
  4017 2940 3100 4`; `row 3063 3994 4064 4`: bright x 4026-4034 in a ring in both metal shots).
  East of the rail below the gate row is field (`px.py pt 4075,3060 3930,3080`: the same in four
  shots): the transistor is under the rail only.
- Gate, `tl3_e3028`: a row y 3018-3038 from the east, under the thin metal x 4099-4111 and the
  metals x 4148, 4190, 4234 without a contact, across x 4250 and on beyond x 4327 (`textmap.py
  4044 3008 4262 3052 5`, `4216 3004 4330 3052 3`: poly unbroken, no hole, bright metal over it
  between edge bars). The ring at (4124,3027) in the clean shot lies in the gap between two
  metals and is in neither chip-2 shot (trap 2).
- The node east of the rail: diffusion y 2993-3008 (`px.py row 3000 4040 4124 4`: chip-2
  stripped shot 169/148/97 at x 4060-4072) into a heavy box (4076-4114 x 2972-3010) under the
  thin metal x 4099-4111. Inside it a pale square (4090-4106 x 2983-2998), drawn as a stub of
  poly; **nothing leaves the box** (field under the thin metal north of it; `e1_box.png`, 4.6x
  three shots), as at the box of `tl3_e3550`. The thin metal over it: Ambiguity 12.
- Load: the node's strip y 2984-3008 runs west under the rail and through the open (the thin
  metal x 3948-3962 does not reach this far north) under a plate x 3884-3938, y 2968-3030 to a
  VCC box (x 3828-3880, y 2982-3042) with a contact ring about 20 x 30 px at (3846,3010)
  (`e1_a.png`, 2.8x three shots: the strip's edges cross the plate at y 2982 and y 3010 in the
  chip-2 metal shot). W/L 24/54. The VCC rail's metal is drawn here from y 2922 to `tla`'s
  start at y 3040 (`px.py col 3858 2920 3056 4`: bright, with bars of 4-12 px where the row's
  and the box's edges pass under).
- **The plate is one poly with the row y 2957-2973**, which runs west under the VCC rail,
  through the open and under the west rail to the pad (3606,2985) of `tl3_w3373` (`textmap.py
  3586 2944 3900 2996 5`: poly continuous from x 3606 to x 3896, no hole, no break; overlay
  `e1_ov.png`, 2.35x).
- The tie (`?`), in the open here (`e1_tie.png`, 5.5x three shots): a tail of the strip runs
  south (x 3948-3964, closed end at y ~3054) and a tab of the plate runs south (x 3916-3938)
  into a heavy box (3912-3944 x 3032-3058, light centre 3920-3935 x 3040-3052) beside the tail.
  Between the box and the tail both chip-2 shots show a dark wall 7 px wide; the diffusion's
  way into the box is not seen even here, where no metal covers it. So `tl3_w3373` = the node
  rests on this tie (`@alias tl3_w3373 tl3_e3000`; Ambiguity 10).

### The load of `rcs_mn3852`'s unit (y 3788-3882): traced; its tie uncertain

    rcs_mn3852 = NOR(tl3_e3712, rcs_in1, rcs_mu)      (now printed by the extraction)
    rcs_in1    = NOT rcs_mv                           (was NOR(rcs_mu, rcs_mv) in `tla`'s drawing)

`tla` drew this unit's node and lower gate, run 7 its upper gate; the load was drawn by nobody.

**The third pull-down (found by review 10, confirmed by the tracer).** The diffusion under the
thin metal x 3948-3962 beside the plate is real and does not end at the load strip:

- `px.py col 3962 3832 3996 4`: the clean shot is tan (196-205/168-181/129-141) without a break
  from y 3832 to y 3976, with no edge where the strip's lower side would cross it (y 3864),
  and pink field from y 3992. Its edges are at x 3952 and x 3972 (`px.py row 3900 3936 3992 3`).
  (I had first taken this stripe for an effect of the metal's edge, because it goes on south
  of the strip: that was the error.)
- At y 3966-3984 it turns east as a band through the gap and **under the whole VSS rail**:
  `px.py row 3976 3940 4096 4` reads tan from x 3984 to x 4048 where the same row at y 4020 is
  pink, both metal shots have edge lines right across the rail at y 3966 and y 3984 (`textmap.py
  3940 3934 4124 4064 4 --acid`), and east of the rail the band is open diffusion to x 4084
  (chip-2 stripped shot 172-186/131-145/103-109). Views `fx_a.png` (3.4x), `fx_ov.png` (2.9x,
  overlay), the reviewer's `review-10/c_south.png`, `c_wide.png`, `c_band.png`.
- Its east end is the diffusion below `tla`'s gate `rcs_mu` (x 4052-4092, y 3955-3984).
  **Below y 3988 `tla`'s column is field**: `px.py col 4070 3944 4112 4` reads 151-158/135-143/
  97-106 (clean) and 156-160/147-158/97-103 (chip-2 stripped) from y 3992 to y 4056, the values
  of open field (`pt 3930,3080`), with an edge line across at y 3984-3988 in both metal shots,
  and diffusion again only from y 4080 (the strip to `rcs_in1`'s box). `trace/tla.txt`'s
  `D 4052,3955:4090,4135` is split there (commit e22fb03, a commit of its own).
- So the transistor under gate `rcs_mu` (4081,3940) is between VSS and `rcs_mn3852`, and
  `rcs_in1`'s only pull-down is the one under gate `rcs_mv`. In words: `rcs_mn3852` =
  `tc2_o5175` AND `rcs_mv` AND R9's match; `rcs_in1` = NOT `rcs_mv`.
- Not resolved: the inside of gate mu's transistor (`fx_mu.png`, 4.6x: an edge at x ~4072 runs
  through the gate, so its channel may be x 4072-4095 and not `tla`'s 58 px: a width); what
  gate mv's row does under the rail (`tla`'s note).

- The VCC diffusion under the VCC rail is **one box** from NOR 1's (cell `tl3_nor`, y 3757-3797)
  down to y ~3866, with a second contact ring at (3846,3838) (`mn_a.png`, 3.0x three shots: ring
  x 3835-3858, y 3824-3852 in the metal shot, specks in the clean shot; `px.py row 3856 3816
  4110 4`: tan from x 3832 to x 3876). This is the "more contacts south of NOR 1's box" of the
  earlier Not done list.
- The strip y 3838-3863 runs east under a plate x 3882-3938, y 3788-3882 (`px.py col 3912 3790
  3960 4`: poly in both chip-2 shots from y 3790 to y 3878, the strip's edges across it at
  y 3836 and y 3864), under the thin metal x 3948-3962, through the gap and under the VSS rail,
  where it is narrower (y 3846-3862: `px.py col 4017 3786 3950 4`), onto `tla`'s node box
  (x 4052-4110) across the rail's east edge line. W/L 25/56.
- The tie (`?`): a heavy box under the thin metal at (3945-3972, 3784-3815), beside the plate's
  top right corner, with diffusion colour under the metal from it down to the strip
  (`mn_tie.png`, 4.3x three shots; `px.py row 3826 3936 3992 3`). The tail is drawn firm from
  the strip up to the box (the same diffusion as the branch above); the box and the plate's
  tab into it are drawn `?`.

Overlay `mn_ov.png` (2.9x, metal and clean shot).

### The NOR units of the west column: traced

    rcs_a2 = NOR(tl3_w3722, tl3_w3803)      NOR 1, y 3688-3872
    tl3_w3939 = NOR(tl3_w3896, tl3_w3982)      NOR 2, y 3862-4046
    tl3_w4546 = NOR(tl3_w4503, tl3_w3803)      NOR 3, y 4469-4653
    tl3_w4720 = NOR(tl3_w3803, tl3_w4763)      NOR 4, y 4643-4827

The unit is `tla`'s `in2` unit / `tl1`'s NOR (`tl1_w3636`) again: a diffusion column west of
the rail (x 3591-3633) between two arms onto the rail's VSS boxes, two gate rows across it,
the node between them with a buried contact (concentric box) to the output row, and the load
east of the rail (strip under a plate x 3763-3816 to a VCC box under the VCC rail; tail and
buried-contact tie at the plate's lower corner). Cell `tl3_nor`, master NOR 1: `tl1`'s
geometry moved by 1042,130; copies at 0,174, 0,781 and 0,955.

- `findcell` (clean shot, `tl1`'s NOR 2535 3558 2842 3742): 1042,130 (0.73), 1041,304
  (0.79), 1042,911 (0.74), 1042,1085 (0.73).
- Overlays `n12_ov.png`, `n34_ov.png` (1.42x, metal and clean shot): every outline on its
  feature in all four units. NOR 1 at 4x in both stripped shots: `n1_w.png` (column, gates,
  box, node strip under the rail), `n1_e.png` (load: the strip's edges show as lines across
  the plate at y ~3760 and ~3790 in the chip-2 stripped shot, so the strip is drawn 24 wide
  where `tl1`'s is 17; the tail x 3735-3752 and the plate's tab x 3735-3765, y 3805-3830).
- Metal overlay `n34_mov.png` (2.4x): the rail contacts (3664,4633), (3664,4807), the VCC
  contacts, the pads.
- **NOR 3 (y 4469-4653, at 0,781)**, placed 2026-11-17 17:48 -0600. It was left out of the
  first round because its top arm lands on the diffusion under the rail at y 4425-4488, then
  unread. That diffusion is the VSS box below the gate of the inverter above (contact ring in
  the metal shot at about (3660,4455); `px.py col 3668 4296 4500 4`: clean shot tan y 4432-4488,
  the gate y 4408-4424, the node y 4384-4400, and field y 4352-4372, where the chip-2 stripped
  shot is greener than red). `cellcheck.py tl3_nor`: n3 2 of 57 blocks bad, median 0.97 (n2 4,
  n4 6). Overlay `n3_ov.png` (3.4x, both stripped shots).

Rows and wiring (`n12_rows.png`, `n34_rows.png`, 3.3x in three shots; `trk_both.png`,
`trk4920.png`, 4x in four shots):

| Row | Net | Where it goes |
|---|---|---|
| y 3712-3732 | `tl3_w3722` (NOR 1 gate 1) | west out of the strip |
| y 3755-3775 | `rcs_a2` (NOR 1 output) | west out of the strip |
| y 3798-3818 | `tl3_w3803` (NOR 1 gate 2) | pad with a contact (3540,3803) at the north end of a metal x 3533-3548 (`follow.py 3541 3850`: (3543,3806)-(3542,4596)). The metal has two more contacts on pads: (3540,4068), whose poly goes east to the buried contact box on the node of the pair's upper unit (**the driver of `tl3_w3803`**, below), and (3540,4590) |
| the pad (3540,4590) | `tl3_w3803` | its poly is an L: south along x 3533-3555 and east along y 4667-4687 as **NOR 4's gate 1**; a row y 4579-4599 also goes east from the pad: **NOR 3's gate 2** |
| y 4493-4513 | `tl3_w4503` (NOR 3 gate 1) | west out of the strip |
| y 4536-4556 | `tl3_w4546` (NOR 3 output) | west under the metal x 3540 (smooth pale poly in the clean shot, no hole) out of the strip |
| y 3886-3906 | `tl3_w3896` (NOR 2 gate 1) | west under the metal x 3540 (no pad) out of the strip, to a pad (3497,3890) |
| y 3929-3949 | `tl3_w3939` (NOR 2 output) | west out of the strip |
| y 3972-3992 | `tl3_w3982` (NOR 2 gate 2) | west under the metal x 3540 (no pad) out of the strip, to a pad (3497,3978) |
| y 4710-4730 | `tl3_w4720` (NOR 4 output) | pad with a contact (3540,4720) (`textmap.py 3480 4690 3570 4750`: ring, bright centre, green hole); a metal south from it (`follow.py 3540 4718 S`) to a pad with a contact (3540,4912), whose poly goes on east along y 4930-4948: the data row of the unit below (`findcell`: `tl1_ua` again), not drawn |
| y 4753-4773 | `tl3_w4763` (NOR 4 gate 2) | west out of the strip |

So `tl3_w3803` gates NOR 1, NOR 3 and NOR 4, and NOR 4's output is the data of the second
latch, if that unit is the copy `findcell` says it is (believed).

### The cross-coupled pair (west column, y 4046-4330): traced, one join believed

    tl3_w3803 = NOR(tl3_w4112, tl3_w4243)              upper unit
    tl3_w4243 = NOR(rcs_x1, tl3_w4290, tl3_w3803)   lower unit

A set/reset latch: `tl3_w4112` high makes `tl3_w3803` low; `rcs_x1` or `tl3_w4290` high
makes `tl3_w4243` low and so (with `tl3_w4112` low) `tl3_w3803` high. `tl3_w3803` is the
metal x 3540 that gates NOR 1, NOR 3 and NOR 4. `tl3_w4243` goes nowhere else.

It is the mirror image of `tla`'s inverter `rcs_u3425` and NOR `rcs_b1` east of R3 (x 2778-3088,
y 3390-3695): the same column, rail boxes, node strips under the rail, loads with their plates,
the strap, and the vertical poly under the rail's edge. Drawn from this cluster's photos, with
`tla`'s lines mirrored as the first draft (x' = about 6650 - x, y + 651; the parts fit to
within 10 px, not as one rigid copy, so no `@inst`).

- **Upper unit.** Column x 3597-3630 west of the rail; one gate row y 4101-4120 from the west;
  above it the node, which goes east under the rail (strip y 4065-4092) to a box east of the
  rail (x 3712-3752, y 4065-4151) and the load (plate A x 3760-3812, VCC box under the VCC
  rail, contact (3842,4100)); below the gate the rail's VSS box (contact ring (3655,4152)).
  The node's buried contact box (3582-3612, 4056-4092) carries the poly that runs west to the
  pad (3540,4068) of the metal x 3540 (`g_m.png`, 3.6x metal: one outline from the pad to
  the box; `g_w2.png`, 4.4x both stripped shots). In `tla`'s mirror the same box has no poly
  leaving it.
- **Lower unit.** The column goes on down (y 4129-4313) with two gate rows from the west,
  y 4191-4209 and y 4281-4299; the node between them goes east under the rail (strip
  y 4228-4252) to a second box east of the rail (x 3712-3752, y 4215-4320). There the arm of
  the pad (3783,4290) crosses it at y 4268-4290: the third pull-down, to the rail's VSS box
  below (contact (3663,4330)) through the link y 4296-4320. The pad is the bottom end of the
  strap, the metal x 3765-3800, whose top pad (3782,4137) is plate A's pad, tied to the upper
  node's box by a buried contact: so the third gate is `tl3_w3803`. Load: plate B (x 3760-3812,
  y 4180-4248) over the strip y 4213-4243 to a VCC box with two contact rings ((3846,4222),
  (3843,4262)); the plate's pad has an arm west tied to the top of the box by a buried contact.
- **The node's buried contact box of the lower unit** (3580-3614, 4228-4260) is a poly patch
  from which nothing leaves (`px.py row 4243 3516 3640 3`: field under the metal x 3531-3552,
  field x 3558-3570). In `tla`'s mirror this is the box that carries `rcs_b1` out.
- **The vertical poly** x 3690-3710, y 4097-4196, under the rail's east edge: a second
  pull-down on the upper node, between the rail's VSS box (west) and the node's box (east). It
  is over a channel at y 4118-4153 (`px.py row 4135 3676 3764 2`: clean shot 230-244/165-177/
  115-125 across x 3692-3708, the VSS box's tan up to x 3684; `row 4108`: 178-194/155-175 over
  the field above). Its top is a cap 5 px below the upper node's strip, with no tie seen.
  **Its bottom end is taken as joined to the lower unit's plate arm** (`?P 3704,4182:3728,4204`),
  which makes its gate `tl3_w4243` and the pair a latch. Evidence: between the poly's end
  (x 3690-3710, to y 4196) and the arm's buried contact box (from x ~3712) no shot shows field,
  only dark lines for about 10 px (`px.py row 4184`, `4190`, `4196 3684 3770 3`; `g_j1.png`,
  `g_j2.png`, 6.6x four shots: at the limit of the photos); two separate polys do not lie
  that close anywhere else here (rows are 23 px apart or more); the poly runs 43 px past its
  channel for no other reason; and without the join the gate floats and the lower unit drives
  nothing. Without the `?`, `tools/unsure.py --equations` gives NOR(`tl3_w4112`, a floating
  gate). **Believed, not seen.**
- The metal x 3540 crosses the rows y 4101-4120, 4191-4209 and 4281-4299 without contacts. At
  (3542,4286) the chip-2 metal shot has a dark spot on the metal that looks like half a ring
  (`g_ov2m.png`); the clean shot has poly colour straight through and no hole, and the chip-1
  metal shot is plain there (`textmap.py 3518 4262 3566 4308 2 --acid`, against the real
  contact at (3540,4068): `textmap.py 3518 4050 3566 4088 2 --acid`). No contact.
- Which areas east of the rail are diffusion was taken from the chip-2 stripped shot (red over
  green by 22-31 in the two boxes down x 3732, against -5 to 6 for field: `px.py col 3732 4050
  4330 4 acid,acid1b`), because the clean shot's colours are ambiguous there.

Overlays: `g_ov2.png` (clean shot), `g_ov2m.png` (metal), 3.4x.

| Row | Net | Where it goes |
|---|---|---|
| y 4101-4120 | `tl3_w4112` (reset of `tl3_w3803`) | west under the metal x 3540 out of the strip |
| y 4191-4209 | `rcs_x1` (set) | west out of the strip |
| y 4281-4299 | `tl3_w4290` (set) | west out of the strip |

### The inverter (west column, y 4345-4490): traced

    tl3_w4373 = NOT tl3_w4414

A rail gate, `tl1`'s inverter `tl1_w4243` again (its lines moved by 1041,130 and fitted on
`h_ov.png`, 3.4x both stripped shots): the gate row y 4405-4423 comes from the west and
crosses under the rail; the node is the diffusion under the rail above it (y 4382-4402), with
a part west of the rail whose buried contact box (3579-3623, 4359-4395) carries the output
row y 4363-4383 west; below the gate the rail's VSS box (y 4425-4488), on which NOR 3's top
arm lands. Load: the node's strip east (y 4376-4399) under the plate (x 3763-3817) to a VCC
box (contact (3845,4395)); a tail x 3737-3757 down from the strip into the tab box below the
plate's left end (`h_tail.png`, `h_tailm.png`, 5x four shots). The tab's tie is `?`, as in
`tl1` (AMB-026). Between this unit's node and the VSS box of the pair above there is field
(y 4352-4372).

| Row | Net | Where it goes |
|---|---|---|
| y 4363-4383 | `tl3_w4373` (output) | west under the metal x 3540 out of the strip |
| y 4405-4423 | `tl3_w4414` (input) | from the west |

### The row y 2899 and the thin metal x 4099-4111 north of track A: traced, six stretches uncertain (run 10)

**The row.** `tl2`'s row y 2890-2908 of `tl1_w3594` (from `tl1`'s pad (2502,2899), through `tl2`'s
track H pad (3410,2899); `tl2`: "every known end is a gate") enters at x 3533 and runs east
across the whole strip at y 2892-2906 to a pad with a contact (4103,2899). It is in the open
except under the west rail (x 3644-3704) and the east rail (x 3989-4049), where it is protected
poly at the same height with no hole; the VCC rail's top (y ~2922) is south of it. One poly, no
other pad (`textmap.py 3530 2881 4140 2918 3`, clean map and chip-2 metal map: the row is the
bright band between its two edge lines in the metal shot; the two dips at x 3641-3644 and
x 4052-4058 are the rails' margin lines; overlay `r10_row_ov.png`, 2x).

**The pad (4103,2899)**: poly x 4086-4126, y 2880-2913, orange in the chip-2 stripped shot;
ring with a bright centre at x 4100-4109, y 2893-2902 in both metal shots (B in chip 2, C-D in
chip 1), a hole x 4100-4109, y 2896-2908 in the clean shot; field east of it, then the metal
x 4142-4154 of another net (`textmap.py 4052 2866 4166 2962 3 --acid`; overlay `r10_pad_ov.png`,
4x). The pad's metal leaves south only: ring y 2905-2919, then the thin metal x 4099-4111,
bright (C-D) from y 2920.

**The thin metal from the pad to track A** (y 2905-4106, where run 5's drawing of track A
begins). It runs over the node boxes of the column's units, which sit at x 4076-4114 east of
the rail, and over the node diffusion of `rcs_mn3852`'s unit. `tools/t.sh tl3 tl3_thin.py 4095
4115 2905 4110 --thr 176 --min 8` lists 25 stretches where neither metal shot shows metal: eleven
of 8-12 px (plain edges) and fourteen of 15-39 px in six groups, each over a box. The six are
drawn `?M`; the rest firm:

| `?M` | What lies under it | What the shots show (`textmap.py 4088 Y0 4124 Y1 3`) |
|---|---|---|
| y 2964-3021 | E1's node box | dark y 2967-3018; a spot at (4103,2986-2992) bright in chip 1 only (B-C), dim in chip 2; no hole |
| y 3381-3444 | the box of `tla`'s inverter `rcs_mu` | dark y 3384-3440; a spot at (4101,3410-3419), A-B in both chips, clean 1-4, no hole |
| y 3527-3574 | the node box of `tl3_e3550`'s NOR | dark y 3530-3568, no spot (run 7: stub only, pass-over) |
| y 3686-3748 | the box of the inverter at y 3655-3745 | dark y 3689-3744; a spot at (4101,3716-3725), A-B; no hole |
| y 3771-3969 | the diffusion column x 4072-4106, y 3778-3842 east of the rail (run 7's; over it the line is narrow and dim from y ~3783, bars of 10-12 px: marked from here since review 13), then `rcs_mn3852`'s node column, lengthwise | the line is 6-9 px wide and dim (A-B in chip 2, 8-A in chip 1, about bare ground's level) with four bars of 16-29 px; at 5x it is a metal-coloured line in both metal shots, and the clean shot has an unbroken protected strip x 4108-4120 beside it for the whole 150 px (`r10_tmE.png`) |
| y 4051-4108 | `rcs_in1`'s node box | dark y 4054-4104; a spot at (4102,4072-4078), B-D in chip 2, 8-9 in chip 1; clean 0-2 with a few green samples, no round hole |

None of the six has a pad or a widening; the spots are those run 8 measured against this metal's
two real contacts (Ambiguity 12): 6-9 px, at or under the line's own brightness, with no hole in
the clean shot, where the contacts (4103,2899) and (4104,5633) have a 12 px centre in a ring and
a hole.

What follows, **marked** (Ambiguity 13):

    tl1_w3594 = inh_ck
    tl1_w3636 = NOR(inh_ck, tl1_w3678)              tl1's first latch is open while inh_ck and tl1_w3678 are low
    tl1_w4678 = NOT(rcs_x1 OR inh_ck AND tl1_w4360 OR tl1_w4703)     tl1's second latch is open while inh_ck is high
    rcs_a2    = NOR(inh_ck, tl3_w3803)

so `tl1`'s two latches in series (whose output goes into `rcs_e4`) are a master and a slave on
`inh_ck`, like latches B and C here. The names are gathered by alias (`inh_ck`: `tl1_w3594`,
`tl3_w3722`, `inh_ck`), not merged. Firm without any uncertain item: the row is
on the pad, and the pad's metal is the thin metal down to y 2964.

### The thin metal x 3948-3962, end to end: traced, six stretches uncertain (run 9)

One metal, 13 px wide, from the pad with a contact (3930,3614) on the foot of the load plate of
`tl3_e3550`'s unit (east to x 3954, then south) down the column between the VCC rail and the east
VSS rail to the pad with a contact (3953,5458) on `tl1_w4937`'s row in the foot. Both ends are
real contacts on widened pads (review 7; `textmap.py 3906 3590 3972 3640 3`, `3940 5300 3972 5480
3`). Between them it has no pad and no widening.

**How its continuity was measured**: `tools/t.sh tl3 tl3_thin.py 3944 3966 3628 5450 --thr 176
--min 8` (a tool of this run: for every y the brightest 3x3 sample across the line's width in
each metal shot; it lists the stretches where neither shot reaches 176, which is above bare
ground there, 163 in chip 2 and 143 in chip 1 at (3978,5000-5050), and below metal, 192-240).
It lists 33 stretches:

- 27 of 8-13 px: the bar a metal shows over any edge that passes under it. The same line has
  the same bars over the foot's plain poly rows (y 5310-5320, 5335-5342, 5355-5363, 5399-5407,
  5420-5428: 8-11 px), where nothing can be in doubt.
- **six places of 14 px or more, each over a load-tie box**: y 3780-3796 and 3802-3821 (17 and
  20 px: the tie box of `rcs_mn3852`'s load), y 4277-4291 and 4305-4320 (15, 16: e3's),
  y 4455-4492 (**38 px**: the rail NOR's at y 4345-4514), y 4673-4686 (14; chip 1 dark to y 4706:
  latch C's upper tie), y 4783-4805 (23: latch C's lower tie), y 5103-5116 and 5129-5143 (14, 15:
  e5's). (A seventh, y 5437-5450, is the ring of the south pad's contact.)

Those six are drawn `?M` (y 3775-3826, 4272-4325, 4450-4497, 4668-4691, 4778-4810, 5098-5148);
everything else is drawn firm. Views of two of them, 6x, both metal shots and the clean shot:
`r9_tm_c.png` (y 4455-4492: no metal brightness at all over the box, two dim spots; the clean
shot has a pale box under it) and `r9_tm_f.png` (e5's: bright spots at y 5088-5100 and 5113-5128
on the line's east half between two bars). The two stretches over latch C were drawn firm by run
6; they are uncertain like the others now (same nets either way).

What follows, **marked** (the six `?M` and the plate's tie, Ambiguities 10 and 11; and it assumes no contact at the spot (3955,4541), Ambiguity 6, the most contact-like place on the line):

    rcs_e4 = NOR(tl1_w4678, tl3_e3550)          (tl1's NOR; its second input was tl1_w4937)
    tl3_e3550 = NOR(rcs_mu, tc2_o5175)          = R9's match AND NOT tc2_o5175

so `rcs_e4` is low while the row address equals R9 and `tc2_o5175` is low, or while `tl1`'s
latch output `tl1_w4678` is high. The names are gathered by alias (`tl3_e3550`: `tl3_tm3955_u`,
`tl3_tm3955`, `tl1_w4937`), not merged (trap 17). Firm without any uncertain item: `tl1_w4937`'s
row is on the thin metal's south pad, and the thin metal's north pad is on that load plate.

The metal crosses node boxes too, with no contact drawn at any: latch C's inverter box at
(3955,4541) (Ambiguity 6) and the tie boxes themselves. Over y 3864-3984 it lies lengthwise on
the edge of the diffusion wire of `rcs_mn3852`'s node (run 8), which shows as a dark line down
its middle with the bright strip on its east half (`textmap.py 3940 3600 3972 4060 3`).

### The foot, y 5345-5660: wiring, traced (run 9)

A crossing field: poly rows run from `tl2`'s strip (x 3533) to `tl4`'s (x 4250) under the metals
that come down out of the cluster. There is no diffusion in it (`opendiff.py 3533 5300 4250
5660`: rims only; the outlined slots between the rows are open field, and what the Inventory of
run 5 took for "outlined areas the enable row may gate" are those slots). Views `r9_foot_sv.png`
(1.7x, metal over clean), `r9_pads.png` (5x, three shots), `r9_dip.png` (6x), overlay
`r9_foot_ov.png`.

How the rows were read: the clean shot as text at 3 px (`textmap.py 3530 Y-15 4258 Y+16 3` for
Y = 5371, 5415, 5458, 5500, 5630): protected poly under each metal, textured poly in the open,
no stretch of field on any row; and in the open stretches both metal shots (`px.py row` / `col`:
the chip-1 metal shot's green is 66-89 on a row and 124-139 on field). How the crossings were
read: a text map down each metal (`textmap.py X-15 Y0 X+16 Y1 3` for X = 3566, 3608, 3955, 4037,
4105, 4192, 4236): over each row the metal is bright over the row's middle with a 6-9 px dark bar
at each edge of the row, and the clean shot under it is protected poly with no hole: a pass-over
(trap 15: no widened pad on any row except the pads below).

| Row (y) | West end | East end | Net |
|---|---|---|---|
| 5365-5378 | `tl2`'s row of `rcs_x1` at x 3533 | the pad with a contact (4192,5373) in mid-run of latch C's clear metal; field east of the pad | `rcs_x1` (alias of `rcs_x1`) |
| 5408-5421 | `tl2`'s row from track G's bottom pad (3368,5414): `tl3_w5025` | x 4250, where `tl4` draws it on to its pad (4279,5413) and a metal north to the gate row y 5240 of the inverter under the rail's south end | `tl3_w5025` (alias of `tl3_e5240`) |
| 5450-5465, west | `tl2`'s row of `tl1_w4937` at x 3533 (5 px higher west of x 3551) | a pad with a contact (3953,5458): the south end of the thin metal x 3948-3962 | `tl1_w4937` |
| 5450-5465, east | a pad with a contact (4040,5458), whose metal x 4036-4048 goes south | x 4250: `tl4`'s row of its strong inverter | `c4l_l3` |
| 5493-5508 | `tl2`'s pad (3518,5498) at the end of track F's arm: `tl3_w4546` | x 4250, where `tl4` draws it on to its pad (4321,5504) and a metal north to gate 1 of `rcs_mv`'s NOR | `tl3_w4546` (alias of `tl3_e4372`) |
| 5621-5641, east | track A's south pad (4104,5633) (run 6) | x 4250: `tl4`'s row `inh_ck` | `inh_ck` |

The rows y 5535-5550 (`tla`: `tla_w3417`) and y 5576-5594 (`bw`: `rc_stepreq_n`) and the west
part of y 5621-5641 with its pad (3739,5630) (`amrw`: `amr_eq_r3`) were drawn by those blocks.

What follows (all four joins on geometry without an uncertain item; `tools/unsure.py` lists no
new net):

    tl3_e4852 = NOT(rcs_x1 OR inh_ck AND tl3_e4537 OR tl3_e4720)     latch C: cleared by rcs_x1, open while inh_ck is high
    tl3_e4635 = NOT tl3_w5025                                       latch C's data = latch B's true value
    rcs_mv    = NOR(tl3_e4852, tl3_w4546)                           gate 1 is NOR 3's output
    tl4_w4545 = NOR(inh_ck, tl4_w4590, tla_w3417)                    (tl4's NOR: its second input is inh_ck)

- **`rcs_x1` clears a fifth latch** (latch C, beside `tl1`'s two and latches A and B).
- **Latch C takes latch B's value**: the inverter under the rail's south end is fed with latch
  B's inverted output. Latch B is open only while track A is low and latch C while it is high
  (run 6), so B and C are a master and a slave on the two levels of one signal, and that signal
  is `inh_ck` (believed a flip-flop: both latch equations are marked, the load ties).
- Track A's signal is `inh_ck`, the enable of `tcw`'s cross-coupled pair `fld_a_in` / `tcw_o3820`
  (the latch that takes `tl5`'s latch c, the candidate field flip-flop: `notes/operation.md`).
- **The two pads at y 5458 are two nets.** Between them, x 3975-4022, is plain field in the
  chip-2 metal shot, the chip-2 stripped shot and the clean shot (`r9_pads.png`; clean map values
  1-3 there, as on the large field at y 5615-5645; the hourglass outline is the two pads' rims).
  West pad: `tl1_w4937`'s row and the thin metal x 3948-3962 (ring, centre x 3946-3958,
  y 5453-5462 in both metal shots, hole x 3949-3958 in the clean shot: `textmap.py 3940 5300 3972
  5480 3`). East pad: `c4l_l3`'s row and a metal south (`textmap.py 4022 5440 4053 5600 3`).
- So **`tl1_w4937`, the second input of `rcs_e4`'s NOR in `tl1`, is the net of the thin metal
  x 3948-3962**, which is drawn end to end (above): `rcs_e4` = NOR(`tl1_w4678`, `tl3_e3550`),
  marked.
- Things looked at and left: on row y 5371 the clean shot has a dark stripe at x 3881-3887; it
  is the VCC rail's margin line, which crosses the field above and below the row too (`px.py row
  5371 / 5415 / 5392 3866 3902 3 all`; both metal shots have poly there). On row y 5500 the
  same at x 3545-3551, the gap between `tl2`'s pad metal and the metal x 3566 (`px.py row 5500
  3530 3562 3 all`). The thin metal x 3948-3962 is dim in the chip-2 metal shot over row y 5415
  ((3955,5411-5417), R 80-130) and bright in chip 1, with protected poly and no hole under it: a
  blemish. In the gap between the metals x 4192 and x 4236 the three rows are poly (`px.py col
  4214 5400 5512 4 all`).
- Metals: `tl2`'s track J arm (`tl3_w3982`) turns south at x 3608 and its track H arm
  (`tl3_w4763`) at x 3566; both are drawn to y 5660 (`follow.py`: they end at (3608,5942) and
  (3563,5724)). The metal from the east pad is drawn to y 5660 (`follow.py 4037 5520 S` runs
  into the wide metal at y ~6100, not looked at). The west rail and the VCC rail are drawn on to
  y 5660; neither has a contact in the foot. South of y 5660 both rails turn east
  (`r9_south_sv.png`, 0.95x): not drawn.

### South of the foot, y 5660-6350: wiring, traced (run 11)

Sparse wiring between the cluster's foot and the left array's upper rows (`ur`). No device and no
diffusion (`tools/t.sh tl3 opendiff.py 3533 5660 4250 6350`: none; the outlined khaki areas in the
clean shot are the open field between the metals' protected margins). Survey `r11_sv.png`
(0.89x, all traces); `cache/scratch/tl3/inbox.py X0 Y0 X1 Y1` lists every package's items in a
rectangle. Read from text maps of both metal shots, the clean shot and the chip-2 stripped shot;
overlays `r11_ov_all.png` (0.89x), `r11_ov1.png`-`r11_ov4.png` (2.4-3.3x), `r11_Ls.png` (2.1x,
three shots, the rails).

How a crossing was read, as in the foot: under a metal that passes over a row the metal is bright
over the row's middle with a dark bar at each edge of the row, and the clean shot has protected
poly and no hole. How a pad's contact was read: a bright centre in a dark ring in both metal
shots and a green hole in the clean shot.

| Piece | What | Read from |
|---|---|---|
| S1 | The metal x 3560-3572 of `tl3_w4763` (`tl2`'s track H arm) ends on a pad with a contact (3565,5720). The pad's poly row, y 5708-5728, runs east across the whole strip under seven metals (x 3608, the west rail, `amrw`'s x 3738, the VCC rail, x 4042, x 4192, x 4236), with no pad, to x 4250, where `tl4` draws it on to the pad (4497,5720) of `tc1_o3527` | `textmap.py 3540 5690 3600 5744 3 --acid` (centre x 3561-3570, y 5717-5723 in both chips; hole x 3558-3567); `textmap.py 3590 5700 3922 5740 4 --acid`, `3918 5700 4262 5740 4 --acid` (edge lines at y 5704-5708 and y 5728-5732 unbroken in both metal shots; no hole on the row) |
| S2 | The metal x 3602-3614 of `tl3_w3982` (`tl2`'s track J arm) ends on a pad with a contact (3607,5938). Its poly row, y 5926-5946, runs east under the west rail, `amrw`'s metal and the VCC rail to a second pad with a contact (3954,5938); the poly ends there, and a thin metal runs on east along y 5933-5945 to x 4250, where `tl4` draws it on to the pad (4583,5936) of `tl5_w5936` | `textmap.py 3585 5915 3632 5960 3 --acid` (chip 2's centre is only 9-B, chip 1's B-C; hole x 3600-3615); `3930 5912 3990 5962 3 --acid`; `3616 5916 3948 5960 4 --acid`; `3960 5922 4262 5956 4` |
| S3 | The metal x 4036-4048 from the pad (4040,5458) (`c4l_l3`) runs south over the row y 5718 and `tla`'s row y 5848 to y 5882, west along y 5866-5882 to x 3904, and south at x 3904-3920 over the rows y 5936 and y 5979 to a pad with a contact (3910,6068). The pad's poly runs west under the VCC rail to x 3797, turns south (x 3797-3817), passes under the horizontal part of the VSS rail's L and ends on a pad with a contact (3801,6286). From that pad a thin metal x 3794-3808 runs south out of the strip: `ur`'s `c4l_l3` | `textmap.py 3890 5856 4060 5896 3`; `3780 6030 3945 6102 3 --acid`; `3770 6096 3850 6262 4 --acid`; `3760 6250 3850 6356 3 --acid`; the crossings `3594 5826 3624 5872 3`, `4028 5826 4058 5866 3`, `3896 5958 3930 6002 3` |
| S4 | The west rail (VSS) runs on south to y 6244, turns east along y 6198-6244 to x 3934 and goes south as a leg x 3888-3934 out of the strip (`ur`'s `vss` x 3913). The VCC rail runs on south to y 6157, turns east along y 6109-6157 to x 4174 and goes south as a leg x 4126-4174 (`ur`'s `vcc` x 4150). No contact on either | `px.py row 5900 3630 3710 4`, `row 6222 3630 3960 6`, `col 3670 6170 6270 4`, `col 3800 6180 6260 4`, `col 3910 6170 6360 6`, `row 6000 3806 3886 4`, `col 4000 6090 6180 4`, `row 6300 4110 4190 4` (all `metal`); `follow.py 3846 5680 S`; `r11_Ls.png` |
| S5 | The row y 6317-6337. West piece: `tl2`'s row of `rcs_thin_e` runs on east from x 3533, under the L3 metal and the VSS leg, to a pad with a contact (3973,6329) (pad A); its metal x 3967-3979 runs south out of the strip to `ur`'s pad (3968,6410). Bare ground from x 4004 to x 4064. East piece: a pad with a contact (4083,6327) (pad B), whose thin metal x 4077-4089 runs south out of the strip (`ur`'s `c4l_gab`) and whose poly runs east under the VCC leg to x 4250, where `tl4` draws it on to the pad (4929,6323) of `c4l_gab` | `textmap.py 3533 6300 3790 6346 4`; `3812 6300 3970 6348 4 --acid`; `3930 6290 4262 6352 4 --acid`; `3948 6296 4002 6548 3`; `4056 6296 4128 6356 3 --acid` |

What follows, in the full extraction (2,342 nets, 4,200 transistors, 0 errors, 0 warnings; four
nets fewer than before the run; `tools/sameconn.py dc5aba1` lists exactly these four joins and
nothing else; `tools/unsure.py`: no new net joined through an uncertain item, and no uncertain
item drawn):

    tl3_w4720 = NOR(tc1_o3527, tl3_w3803)        NOR 4's gate 2 is tc1_o3527   (firm)
    tl3_w4373 = NOT tc1_o3527                    the inverter's input too      (marked as before: its load tie)
    c4l#_nx_g = NOR(c4l#_nx_n, c4l_l3)        # = 0..3: the 4-bit counter's L3 line   (the cells are marked, as before)
    c4l_l3 = NOT tl4_w4243                    (tl4's strong inverter; marked: its load tie)
    c4l#_m <-> c4l#_mb through gate c4l_gab    the 4-bit counter's pass gates ("gab")

- **`tl3_w4763` is `tc1_o3527`** = NOR(`tc1_o3095`, `tc1_o3353`), cell B of the top-centre gate
  column (`notes/blocks/tc1.md`), which `tl6` and `tl5` had followed west as far as `tl4`'s pad
  (4497,5720). It is gate 2 of NOR 4 and the input of the west column's inverter: `tl3_w4373` =
  NOT `tc1_o3527`, and through it NOR 3 and `rcs_mv`: `tl3_w4546` = NOR(`tl3_w3803`,
  NOT `tc1_o3527`), `rcs_mv` = NOR(`tl3_e4852`, `tl3_w4546`). Alias in the trace (the canonical
  name is `tc1_o3527`). No uncertain item on the join.
- **`tl3_w3982` is `tl5_w5936`**, the bus line x 5063 of `tl5`, which leaves that strip south at
  (5053-5073, 6350). So the net that holds `rcs_cond` low, gates NOR 2 and resets the pair still
  has no driver in the top-left logic: it comes from south of y 6350. No uncertain item.
- **`c4l_l3` is `c4l_l3`**: the L3 line of the left array's 4-bit counter is driven by `tl4`'s
  strong inverter, the inverse of the right cluster's latch output `tl4_w4243`. In every bit of
  that counter the value on its way to the master passes NOR(L3, ...) (`notes/blocks/ur.md`,
  `notes/blocks/mra.md`), so **while `tl4`'s latch is clear (`tl4_w4243` low) the 4-bit counter's
  masters are loaded with 0, and it can count only while the latch is set** (traced: the join,
  with no uncertain item on the wire; the two ends are marked as before, the inverter's load tie
  and the counter cell's uncertain items; believed: that the 4-bit counter is the vertical sync
  width counter, `notes/blocks/amr.md`, which would make `tl4`'s latch the "in vertical sync"
  flag). `tl4`'s name stays the net's (`tl4` aliases `c4l_l3` to it); `c4l_l3` is an alias.
- **`c4l_gab` is `c4l_gab`**: the gate line of that counter's m/mb pass gates is the net that
  clears `tl5`'s latch c (`c4l_gab`, `tl6`'s join to `c4l_gab`) and is the input of
  `tcw_o3550`. Its driver is still not found. Alias in the trace. No uncertain item.
- **`rcs_thin_e` does not reach the 5-bit counter's L3 line.** Its row ends on pad A, whose metal
  runs south to `ur`'s pad with a contact (3968,6410) (seen: `textmap.py 3948 6296 4002 6548 3`:
  one metal x 3967-3979 from pad A over `ur`'s row y 6362-6374 to the pad's centre (3973,6413);
  no metal from there to `ur`'s next pad (3973,6521)). `ur` had that pad on one poly with the
  pad (3757,6410) at the top of `sl_l3`; **there is no poly between the two pads** (below). The
  pad's poly leaves east along y 6402-6422, under `c4l_gab`'s metal and the VCC leg, seen to
  x 4256 (`textmap.py 4000 6384 4260 6440 4 --acid`); it is outside this strip (`urch`'s
  region begins at x 4240) and not drawn. So the select of `tla`'s selector goes south-east
  towards the channel east of the left array, and `sl_l3` is fed only by the poly that reaches
  the pad (3757,6410) from the west.

**Three corrections to `trace/ur.txt`** (commit a1c5d8b, a commit of their own; each blocked a
join of this piece or would have made a false one):

1. `c4l_l3`, drawn `M 3780,6330 y8500`: the metal is not at x 3780 north of the first counter
   row. From the pad (3801,6286) it runs at x 3794-3808 to y 6674 and steps west on a diagonal
   at y 6674-6698 onto the L3 position (`px.py row Y 3764 3816 4 metal,metal1` for Y = 6345,
   6380, 6420, 6500, 6540-6660, 6680, 6690, 6700, 6710, 6740; `textmap.py 3783 6345 3819 6700 3`:
   bright in both chips all the way, bars only at the edges of `ur`'s rows, field under it and
   no hole; `r11_l3step.png`, 5x three shots: the diagonal is there in both chips). At x 3780
   there is bare ground with an open poly beside the metal. Now `M 3801,6330 y6674 3781,6698
   y8500`.
2. `c4l_gab`, drawn `M 4095,6330 y8505`: the metal is at x 4077-4091 from the pad (4083,6327)
   down to y ~6602, where it shifts 11 px east (`px.py row Y 4066 4110 4 metal,metal1` for
   Y = 6352, 6400, 6500, 6600, 6660-6720, 6760, 6800, 6900, 7300; `r11_gabstep.png`). Now
   `M 4084,6330 y6602 x4095 y8505`.
3. `P 3560,6400:3985,6420`, the poly that joined the pads (3757,6410) and (3968,6410): between
   the pads there is no poly. `textmap.py 3700 6384 4012 6440 4 --acid`: the edge lines at y 6400
   and y 6424 that the row has west of the first pad (x 3700-3744) and east of the second
   (x 3992 on) are absent from x 3780 to x 3950 in both metal shots (bare-ground brightness on
   every row of the map at x 3820-3876); the clean shot has open field there (values 0-2, no
   poly) and field under the L3 metal and under the VSS leg; the chip-2 stripped shot has 2-7
   at x 3828-3876 where poly is F. Cut to `P 3560,6400:3760,6420`.

`TRACE=ur tools/t.sh tl3 sameconn.py dc5aba1` (`ur` alone, before and after the three edits):
`connections identical`, with one net more (the pad (3968,6410) and its metal are no longer part
of `sl_l3`'s net; alone in `ur` they carry no name and no transistor). With this piece the only
differences in the full extraction are the four joins above.

Things looked at and left as they are:

- **A dark blob on the VSS band where it lies over the vertical poly, (3805-3815, 6205-6235)**, in
  the chip-2 metal shot only (`px.py col 3800 6180 6260 4 metal,metal1`; `r11_Ls.png`,
  `r11_ov3.png`): chip 1 is bright there and the clean shot under it is protected poly with no
  hole (`textmap.py 3770 6096 3850 6262 4 --acid`). A blemish, no contact (a contact would
  ground the L3 line).
- The dark specks on both rails' Ls are at different places in the two chips' metal shots, and
  the clean shot under both Ls is field (pink, with the grey-green centre line every wide metal
  has here): no contact.
- The narrow outlined strip in the clean shot at y 6167-6182, x 3822-3945, between the two Ls, is
  the open field between their protected margins (trap 2), checked in the chip-2 shots as that
  trap asks: `px.py pt 3910,6174 3850,6174 3760,6174 3720,6120 acid,acid1b,metal,metal1` gives
  the colour of the open field beside it in all four (chip-2 stripped 158/155/95 against
  158/155/102 and 155/154/98).
- Pad A's centre is dim in the chip-2 metal shot (5-8 of 16 inside a ring of 2-3) and B-D in
  chip 1, with a hole x 3969-3981, y 6326-6335 in the clean shot: taken as a contact
  (Ambiguity 14).
- The horizontal piece y 5866-5882 of the L3 wire lies 8 px south of `tla`'s row y 5838-5858 and
  does not touch it; the metal x 4042 crosses that row as a pass-over.
- `ur`'s other lines here: the metal of `sl_l3` from the pad (3757,6410) is drawn stepping west
  at y 6560 and is still at x ~3757 at y 6650 (`r11_l3step.png`); `ur`'s `vcc` line x 3630 is
  drawn from y 6330, where there is no metal down to y ~6570 (`px.py col 3630 6330 6620 20
  metal,metal1`). Neither touches anything of this piece; not changed (handoff).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tl3_w3333` | poly | (3533, 3324-3342) | in | data of latch A |
| `tl3_w3419` | poly | (3533, 3409-3429) | out | latch A's inverted output |
| `rcs_x1` | poly | (3533, 3497-3515) | in | clear of latch A |
| `tl3_e3028` | poly | (4250, 3018-3038) | in | gate of the top unit E1, from the east (seen on to x 4327) |
| `tl3_w3722` | poly | (3533, 3712-3732) | in | NOR 1 gate 1 |
| `rcs_a2` | poly | (3533, 3755-3775) | out | NOR 1 output |
| `tl3_w3896` | poly | (3533, 3886-3906) | in | NOR 2 gate 1 |
| `tl3_w3939` | poly | (3533, 3929-3949) | out | NOR 2 output |
| `tl3_w3982` | poly | (3533, 3972-3992) | in | NOR 2 gate 2 |
| `tl3_w4763` | poly | (3533, 4753-4773) | in | NOR 4 gate 2 |
| `tl3_w4112` | poly | (3533, 4101-4120) | in | the pair: gate of the upper unit |
| `rcs_x1` | poly | (3533, 4191-4209) | in | the pair: lower unit gate 1 |
| `tl3_w4290` | poly | (3533, 4281-4299) | in | the pair: lower unit gate 2 |
| `tl3_w4373` | poly | (3533, 4363-4383) | out | the inverter's output |
| `tl3_w4414` | poly | (3533, 4405-4423) | in | the inverter's input |
| `tl3_w4503` | poly | (3533, 4493-4513) | in | NOR 3 gate 1 |
| `tl3_w4546` | poly | (3533, 4536-4556) | out | NOR 3 output |
| `tl3_w5025` | poly | (3533, 5015-5035) | out | latch B's inverted output |
| `rcs_x1` | poly | (3533, 5103-5121) | in | clear of latch B |
| `tl3_e4243` | metal | (4250, 4235-4255) | out | e3's output, on east into `tl4`'s strip |
| `tl3_e5114` | poly | (4250, 5105-5123) | in | e5's gate 2, from the east |
| `inh_ck` | poly | (3533, 2892-2906) | ? | the row y 2899 from the pad (4103,2899) at the north end of the thin metal x 4099-4111 (track A's net), on west: `tl2`'s and `tl1`'s `tl1_w3594` (alias across six `?M`); driven from track A if the thin metal is one metal (Ambiguity 13) |
| `tl3_e4635` | poly | (4250, 4627-4642) | in | latch C's data, from the east |
| `rcs_x1` | metal | (4250, 5889-5901) | in | latch C's clear: the metal x 4192 from the pad (4190,4808), east out of the strip along y 5895 |
| `tl3_e4372` | poly | (4250, 4366-4380) | in | gate 1 of the NOR under the rail that drives `rcs_mv`, from the east |
| `inh_ck` | poly | (4250, 4496-4510) | ? | the row of track A's pad (4146,4510), on east: `tl4`'s `inh_ck` |
| `rcs_mv` | poly | (4250, 4736-4751) | in | the poly of the pad (4192,4743) at the south end of `rcs_mv`'s track, from the east |
| `rcs_mv` | poly | (4250, 4904-4925) | ? | the poly of the pad (4234,4918), on east |
| `rcs_mv` | metal | (4250, 5760-5772) | ? | the metal x 4236 from that pad, east out of the strip along y 5766 |
| `tl3_e5240` | poly | (4250, 5231-5250) | in | gate of the inverter under the rail's south end; in `tl4`'s strip the row turns south at x ~4277 |
| `tl3_e4635` | poly | (4250, 5190-5205) | out | that inverter's output row; in `tl4`'s strip it ends on a pad (4278,5198) of a metal x 4279 whose north pad (4278,4636) is on `tl3_e4635`'s row (not drawn: open join) |
| `rcs_x1` | poly | (3533, 5365-5378) | in | the row of latch C's clear (pad (4192,5373)), from `tl2`'s row y 5371 |
| `tl3_w5025` | poly | (3533, 5408-5421) | out | latch B's inverted output again: the row from `tl2`'s track G, across the foot |
| `tl3_w5025` | poly | (4250, 5408-5421) | out | the same row, on east to `tl4`'s pad (4279,5413) (`tl4`: `tl3_e5240`) |
| `tl3_e3550` | poly | (3533, 5450-5465) | out | the row of the pad (3953,5458) at the south end of the thin metal x 3948-3962 (`tl2`'s and `tl1`'s `tl1_w4937`); on west to `tl1`'s NOR of `rcs_e4`. Driven here if the thin metal is one metal (Ambiguity 11) |
| `c4l_l3` | poly | (4250, 5450-5465) | in | the row of the pad (4040,5458), from `tl4`'s strong inverter |
| `tl3_w4546` | poly | (3530, 5494-5508) | out | NOR 3's output again: the row from `tl2`'s pad (3518,5498), across the foot |
| `tl3_w4546` | poly | (4250, 5494-5508) | out | the same row, on east to `tl4`'s pad (4321,5504) (`tl4`: `tl3_e4372`) |
| `inh_ck` | poly | (4250, 5621-5641) | in | the row of track A's south pad (4104,5633), on east: `tl4`'s `inh_ck` |
| `tl3_w3982` | metal | (3533, 5367-5380) | in | `tl2`'s track J arm; turns south at x 3608 |
| `tl3_w4763` | metal | (3533, 5430-5442) | ? | `tl2`'s track H arm; turns south at x 3566 |
| `c4l_l3` | metal | (3794-3808, 6350) | out | run 11: the metal from that pad, by two metal pieces and two poly pieces, to the pad (3801,6286) and on south: `ur`'s `c4l_l3`, the 4-bit counter's L3 line |
| `tl3_w3982` | metal | (4250, 5933-5945) | ? | run 11: the metal runs south to a pad (3607,5938); a row east to a pad (3954,5938); a thin metal east out of the strip: `tl4`'s metal y 5939 to `tl5_w5936` (an alias). Every known end here is a gate, so probably in |
| `tc1_o3527` | poly | (4250, 5708-5728) | in | run 11: `tl3_w4763`'s metal runs south to a pad (3565,5720), whose row runs east out of the strip: `tl4`'s row of `tc1_o3527` (cell B of `tc1`); `tl3_w4763` is an alias |
| `vss` | metal | (3888-3934, 6350) | - | the west rail's leg, after its turn east along y 6198-6244; on south as `ur`'s `vss` x 3913 |
| `vcc` | metal | (4126-4174, 6350) | - | the VCC rail's leg, after its turn east along y 6109-6157; on south as `ur`'s `vcc` x 4150 |
| `rcs_thin_e` | poly | (3533, 6317-6337) | ? | the row y 6327 from `tl2`'s pad (2913,6327) at the south end of thin metal E, on east to pad A (3973,6329) |
| `rcs_thin_e` | metal | (3967-3979, 6350) | ? | pad A's metal, south out of the strip to `ur`'s pad (3968,6410), whose poly leaves east along y 6402-6422 (seen to x 4256, not drawn) |
| `c4l_gab` | metal | (4077-4089, 6350) | ? | pad B's (4083,6327) thin metal, south out of the strip: `ur`'s `c4l_gab`, the 4-bit counter's pass-gate line (an alias) |
| `c4l_gab` | poly | (4250, 6316-6336) | ? | pad B's row, east out of the strip: `tl4`'s row to the pad (4929,6323) of `c4l_gab` (the clear of `tl5`'s latch c) |

## Ambiguities

1. The two cross-couplings of latch A rest on the load plates' ties, `?` items in `tl1`'s
   cells (AMB-026). Not read again here; in this cluster the ties are in the open (no thin
   W), so the chip-2 shots at 6x may settle them for all copies: (3715-3745, 3375-3400) and
   (3713-3737, 3492-3522).
2. `tl3_w3550`'s poly on the lower unit's box was read as a stub from one 3.5x view
   (`la_rows.png`): a rounded end at x ~3570 with nothing under the metal x 3540 at
   y 3540-3560.

3. **The bottom end of the vertical poly (3700,4190)**: joined to the lower unit's plate arm or
   not (see the pair, above). Drawn joined, `?`. The same structure in `tla` (`rcs_iso2958`,
   whose stub ends 4 px from `rcs_b1`'s plate arm in `tla`'s own geometry) is drawn unjoined
   there, "no connection found": the two readings should agree, and the join would make
   `rcs_u3425` = NOR(`rcs_bc3460`, `rcs_b1`), a latch with `rcs_b1`. Proposed in the handoff.
4. The pair's column meets the rail's VSS box along a weak dark line at x 3628-3632
   (`px.py row 4160 3586 3700 3`: one sample 107/73/63, against 48/12/25 at the column's
   outer edge). Drawn joined: both units' pull-downs need it, and `tla` assumes the same.
5. The load-plate ties of the inverter (`?`, as `tl1`'s) and of the pair's plates (drawn firm,
   as `tla`'s) are buried contact boxes read from outlines.

6. **Does the thin metal x 3948-3962 make contact with latch C's inverter node at (3955,4541)?**
   **Working assumption: no, it passes over** (no contact drawn; the first drawing had a `?C`
   and an alias, removed after review 7). For a contact: both metal shots have a round bright
   centre 10-12 px across at the line's full brightness in a dark ring x 3940-3970, y 4523-4550
   (`px.py col 3955 4514 4562 3`, `row 4540 3934 3980 3`: 214-227/184-191/92-103 in chip 2,
   224-234/190-201/80-101 in chip 1; the master's W over the same box is dimmer, 151-186, and
   the pass-over at e3's tie box (3958,4299) too); the clean shot has a grey-green band under
   the metal (152-161/147-160/102-127, red minus green 0-4; `tm_inv.png`, 5x four shots).
   Against (the reviewer's points, each checked): the metal has **two real end contacts on
   pads**, (3930,3616) and (3953,5459), each with a widened pad, a ring and a green hole, and
   here there is no pad; the pale band runs the full width of the box (x 3944-3966,
   y 4540-4544), not a round hole, and the master's box under thin W has the same band
   (`px.py row 4366 2684 2722 3`: 160-183/142-172/99-141; the copy 608 px higher, `row 3758`:
   169-193/150-175/100-138), where `tl1` draws a pass-over; a real contact hole nearby is
   greener (164/175/95 at (3909,4675), 112/132/76 at (4190,4810)); and a contact would put the
   inverter's output on the net of the two end pads, the north one being on the load plate of
   another gate. If it were a contact after all, the thin metal would carry NOT `tl3_e4635`.
   What would settle it: reading the unit at y 3440-3610 (is the plate with the north pad tied
   to that unit's node?) and the row of the south pad; if the thin metal then has a driver of
   its own, the spot is a pass-over.
7. Latch C's two load-plate ties are the `?` items of `tl1`'s cells, mirrored: (3949-3977,
   4673-4694) under the thin metal x 3948-3962 (dark for 28 px over it, y 4676-4700, clean shot
   mostly tan: a pass-over by trap 22) and (3963-3987, 4794-4824), east of that metal. AMB-026.
8. The stub on the upper node's box (4083-4126, 4711-4731) was read as a stub from one 3x view
   in three shots (`lc_bf1.png`: rounded end at x ~4125, field east of it to track A).

9. **The link from the rail NOR's node to its output box** (4070-4088, 4408-4428): drawn `?D`.
   The column's east edge line (x 4073-4078, continuous from y 4350 to 4490 in the chip-2
   shots) and the box's west frame are one 15 px dark band; whether the diffusion passes under
   it into the box cannot be seen (`rn1_box.png`, 6x four shots; `px.py row 4420 4040 4146 3`:
   two lighter samples at x 4079-4082 between the dark ones). For: a buried contact box holds
   diffusion, and the column is the only diffusion within 100 px; the same box sits on the
   column in e3, e5 and `tla`'s units. If it were not joined, `rcs_mv` would be driven only
   from the east (the poly of its pad (4192,4743)). Review 9 adds for the join: the column's
   edge line at x 4080 is absent at y 4416-4426 in three shots (`review-9/a_link.png`).

10. **The load ties of the rail units** ((3942-3976, 3500-3532), (3936-3966, 3656-3686),
    (3950-3972, 4456-4488), and since run 8 (3912-3944, 5244-5276) E1's (3912-3944, 3032-3058) and that of `rcs_mn3852`'s load (3944-3972, 3784-3814)) are drawn `?` from heavy boxes at the standard place of a tail-and-tab
    tie; none is resolved. For the NOR at y 3450-3660 the tie decides more than the load: the
    node's only exit is the plate (its foot carries the thin metal x 3948-3962), so
    `@alias tl3_e3550 tl3_tm3955_u` rests on it.
11. **Is the thin metal x 3948-3962 one metal from its north pad (3930,3614) to its south pad
    (3953,5458)?** Working assumption since run 9: **yes**; drawn end to end, with the six
    stretches over load-tie boxes uncertain (`?M`: y 3775-3826, 4272-4325, 4450-4497, 4668-4691,
    4778-4810, 5098-5148). For: `tools/tl3_thin.py` (Logic, "The thin metal x 3948-3962, end to
    end") finds metal brightness in at least one metal shot everywhere else, with only the 8-13 px
    bars every edge makes; the line has no pad and no widening between its two end pads, and a
    piece of metal that stopped at a box would have to make contact there (trap 14), which trap
    22 says this signature is not; a buried-contact box under a wide metal is dark in the same
    way (`textmap.py 2597 7520 2658 7594 3`: the box (2615-2639, 7538-7576) of `ur`'s clock
    generator under a 50 px metal: dark for 12 px, partly bright, dark again for 10 px).
    Against: over the rail NOR's tie box neither metal shot shows any metal for 38 px
    (y 4455-4492) and the clean shot has a greenish band right across at y 4482-4487
    (`r9_tm_c.png`); over the others the dark stretches are 14-23 px. (Review 12: the same
    band lies under the line at y 4300-4306, 3714-3723, 3860-3866 and 3978-3982, always at the
    south edge of a diffusion feature and 16-40 px wide, wider than the metal: it is a feature
    of the ground, not a contact hole, so the band is weak evidence either way.) If it were broken at one of
    them, `tl3_e3550` would not reach `tl1`'s NOR and the piece south of the break would be
    driven by a contact not found. What would settle it: a third chip's metal shot, or the
    simulation (does the row counter step at R9's match without this path?).
    The equation it gives is `rcs_e4` = NOR(`tl1_w4678`, `tl3_e3550`).

12. **Does the thin metal x 4100-4112 (`inh_ck`'s south arm) make contact with the box of the
    inverter at y 5180-5300, at (4101,5202)?** Working assumption: no (no contact drawn, as run 6
    had it). The metal is dark from y 5184 to y 5228 with a spot of R 160-185 about 6 x 9 px at
    x 4099-4102, y 5199-5205 in chip 2 (R 145-170 in chip 1), and the clean shot has no hole
    there (red minus green 8-32). The same metal's real contact (4104,5633) has R 190-220 over
    12 x 12 px in both chips and a hole 9 x 12 px (`textmap.py X-30 Y-30 X+30 Y+33 3 --acid` at
    both; the same for (4101,3719), (4102,4074), (4100,5066): the other boxes this metal
    crosses). If it were a contact, latch C's data would be its own enable line. The same kind
    of spot as (4101,3719) (Logic, the inverter at y 3655-3745) and (4102,4074) (Inventory).
    **And over E1's box, at (4104,2988)**, on the metal's north part: dark in chip 2
    (84/73/26), a spot of 172/126/37 in chip 1, and a pale patch in the clean shot
    (192/171/140, red over green, where the metal's real north contact (4102,2899) is green,
    155/164/91, with 173 and 206 in the two metal shots: `px.py col 4104 2880 3060 4`,
    `textmap.py 4060 2868 4150 2940 3 --acid`). E1's box holds only a stub, so a contact there
    would make the thin metal E1's second output. Not drawn.

13. **Is the thin metal x 4099-4111 one metal, without a contact on the way, from its pad
    (4103,2899) to track A?** Working assumption since run 10: **yes**; drawn, with six stretches
    over node boxes uncertain (`?M`: y 2964-3021, 3381-3444, 3527-3574, 3686-3748, 3771-3969,
    4051-4108; Logic, "The row y 2899 and the thin metal"). For: both ends are real contacts on
    pads and nothing between has a pad or a widening; the pad (4103,2899) has no other metal, and
    every known end of its row is a gate (`tl2`), so the row's driver must arrive by this metal;
    the boxes' interiors under the metal are red over green in the clean shot (194-207/172-174/
    132-138 at (4103,2989), (4101,3414), (4101,3720)) where this metal's two real contact holes
    are green over red with low blue (169/169/98, 158/172/102), and in the chip-2 stripped shot
    they look like the boxes at (4097,4241) and (4097,4417) that no metal crosses (review 13:
    `mosA.png`, `mosB.png`, `b3400.png`, `b3719.png`); for two of the boxes a contact would make
    a gate constant (E1's: latch B's enable NOR(`inh_ck`, `tl4_w4590`) with `inh_ck` = NOT
    `tl4_w4590`; `rcs_in1`'s: `tl3_e4243` = NOR(`rcs_mv`, `inh_ck`) with `inh_ck` = NOT `rcs_mv`);
    the dark stretches are trap 22's pass-over, as on the
    other thin metal (Ambiguity 11). Against: **`inh_ck`'s source is not traced** (in the full extraction it is
    only ever a gate, eleven loads), so logic does not exclude that one of the other four units
    drives it through a contact here (`rcs_mu`'s inverter, `tl3_e3550`'s NOR, the inverter
    `tl3_e3712`, `rcs_mn3852`): the no-contact reading rests on the two stripped shots. The
    most contact-like spot is (4103,4075), on `rcs_in1`'s box: as bright in chip 2 as a real
    centre (187/181/85), not in chip 1 (152/135/49), and red equal to green in the clean shot
    (172/172/132; the holes have blue 98-102). The metal shots show nothing of the metal for
    40-55 px over each box, and over y 3826-3969 it is at bare ground's brightness (the clean
    shot's protected strip and the line's colour at 5x are what show it there); four of the
    boxes have a small bright spot (Ambiguity 12). What it gives: `tl1_w3594` = `inh_ck` (the
    enable of `tl1`'s two latches, an input of `rcs_a2`, gate 1 of NOR 1). What would settle it:
    a third chip's metal shot; the source of `inh_ck` (if it is found driving a clock-like enable,
    the reading fits); the simulation.

14. **Pad A's contact (3973,6329), on the row y 6327 of `rcs_thin_e`.** Working assumption: a
    contact (drawn firm). In the chip-2 metal shot the centre is dim, 5-8 of 16 (80-140) inside a
    ring of 2-3, where the other pads of this piece have B-D; in chip 1 it is B-D, x 3969-3975,
    y 6326-6329, and the clean shot has a hole x 3969-3981, y 6326-6335 (`textmap.py 3948 6296
    4002 6548 3`). The metal that leaves the pad south is plain in both chips, and a metal that
    ends on a pad makes contact there (trap 14). If it were not a contact, the row of
    `rcs_thin_e` would end on nothing and `ur`'s pad (3968,6410) would be fed from pad A's metal
    alone. Pad (3607,5938) is a milder case of the same (chip 2's centre 9-B).

## Review

**Round 1, full review of latch A** (2026-11-17 17:05 -0600, a fresh Fable 5.2 agent, 52 tool
uses, images in `cache/scratch/tl3/review-1/`; commit reviewed 19e1cd2). Told to suspect: a
cell copy differing from its master by one contact, box or poly end (the inverter's
pull-down, both third pull-downs); the three rows passing under the metal x 3540 and that
metal's three pads; the stub reading of `tl3_w3550`; the contacts (3670,3685) and
(3846,3477); the ports at x 3533; the rail link. It checked: `cellcheck` on the clean and
metal shots and master-against-copy mosaics at 4x in the chip-2 stripped shot; the
inverter's pull-down, both third gates and the stub with row and column profiles
(`tools/px.py`) and 4x views; the rows under x 3540 and the three pads with text maps; the
three ports at the boundary in both stripped shots; both thin metals (contacts real, none
between; the dark stretches of x 3605 over the two buried boxes are pass-overs); the rail
link with `follow.py` and a 2x view.

Findings, all geometry only, each checked by the tracer:

1. The lower VCC box is one box y 3363-3577 with one long contact ring y 3372-3504, where
   the cell's two pieces span y 3397-3520 and the contact was 24x44 at (3846,3477).
   Confirmed (`tools/t.sh tl3 px.py col 3846 3350 3592 8 acid1b,metal`: clean shot tan from
   y 3366 to 3566). Fixed: `D 3819,3363:3879,3572`, `C 3846,3438 s=24x120`. Still VCC.
2. The VSS contact's ring is centred nearer (3662,3680) than (3670,3685). Fixed.
3. In the cell `tl1_ua` (here): the third gate's west end is at x ~3638 against 3647 drawn,
   and its arm turning south is about x 3710-3737 wide against 13 px drawn. Not changed:
   the cell is `tl1`'s; passed on in the handoff.
4. The data row's corner north straddles x 3533 (x 3510-3535). The port stands.
5. North of the link the west rail continues as wider metal (x ~3648-3762 above y 2598):
   not drawn. Added to Not done.

Not checked by it: the two plate ties (AMB-026; in passing its `mid3.png` shows heavy boxes
at (3722-3745, 3372-3395) and (3716-3738, 3490-3512), which fits the drawn reading); the
masters; the rail outside y 3200-3725.

    tools/t.sh tl3 sameconn.py 19e1cd2             -> connections identical
    .venv/bin/python tools/sameconn.py 19e1cd2     -> connections identical

Round 1: no findings that change a connection.

**Round 1, full review of the three NOR units** (second piece; 2026-11-17 17:27 -0600, a
fresh Fable 5.2 agent, 19 images in `cache/scratch/tl3/review-2/`; commit reviewed f6d3984).
Told to suspect: a copy differing from the master by one contact, box, arm or poly end;
NOR 4's top arm and the box it lands on; the pad (3540,4590), its L poly and the gaps to the
pad and metal below; the six rows under the metal x 3540 and at x 3533; the load strip's
width and the tie; the contacts (3540,4068), (3540,4912). It checked: the three copies by
overlay in `acid`, `acid1b` and `metal` at 3.3-3.4x; all four arms onto their VSS boxes at 5x
in four shots, with the box 3640-3694 x 4608-4653's contact ring at (3662,4633); that
nothing joins NOR 1's box to NOR 2's strip under the rail (y 3894-3926 is field by profile;
`railprof.py` wrongly reports diffusion to y 3905 there); the five pad contacts with text
maps; the metal x 3540 continuous from y 3803 to 4598 with no contact at the rows it
crosses nor at a blemish (3540,4285); no metal at x 3540 between y 4598 and 4712 and field
between the L and the pad at y 4692-4697 (6x); the ports (rows 3722, 3765, 3939, 4763 run
on west past x 3440; 3896 and 3982 end on pads at x 3497); the extraction.

Findings, all geometry only, each checked by the tracer against `n1_e.png`, `n34_rows.png`
and `n34_mov.png`:

1. The load strip under the plate is about y 3758-3790 (30 px) in all three units, drawn 24.
   Fixed in the cell: `D 3747,3760:3827,3789`.
2. The contact (3540,3803)'s bright centre is at about (3541,3810). Fixed: `C 3541,3808`.
3. The L's vertical poly is x 3533-3560, drawn to 3555. Fixed.
4. The VCC diffusion at NOR 1 runs on south to about y 3880 with a second contact near
   (3845,3840); NOR 4's runs about y 4700-4810 with more pits. All VCC. Not drawn (not
   checked by the tracer): Not done.

Not checked by it: the `cellcheck` tint images; the west rail at y 4050-4650 beyond a 1.6x
view (continuous in both metal shots) and y 2622-3680; features at x 3870-3885 and the row
at y ~4825-4850, which belong to units not drawn.

    tools/t.sh tl3 sameconn.py f6d3984             -> connections identical
    .venv/bin/python tools/sameconn.py f6d3984     -> connections identical

Round 1: no findings that change a connection.

**Round 1, full review of the pair, the inverter and NOR 3** (2026-11-17 18:04 -0600, a fresh
Fable 5.2 agent, 78 tool uses, 21 images in `cache/scratch/tl3/review-3/`; commit reviewed
b5bd64c). Told to suspect: the join at the vertical poly's bottom end and its top end; the
poly from the pad (3540,4068) to the upper node's box; the column's join to the rail's VSS
box and the link y 4296-4320; which areas east of the rail are diffusion; whether the lower
node or plate B goes anywhere else; contacts where the metal x 3540 crosses the rows
((3542,4286) above all); the inverter's node against the VSS box above it, its gate across the
rail, its tab; NOR 3 by overlay and the box its top arm lands on; anything left out in
x 3533-3885, y 4040-4660. It checked each at 4x to 6.5x in two or more shots with row
profiles and text maps; `cellcheck` and master-against-copy mosaics for NOR 3; `follow.py`
on the strap; `opendiff.py` (no large open diffusion).

The join (Ambiguity 3) stays unproven: no shot shows a gap and none shows the poly passing
through the box's ring. The reviewer adds, for the join (`px.py` rows 4165-4198, `j_bot.png`
6.5x): above y 4178 the poly's east edge is a dark line at x 3712-3715 in both metal shots
and the chip-2 stripped shot, and at y 4183-4193 those samples are poly-bright in all three,
so the poly steps east at the arm's level; its bottom edge at y 4200 is in line with the
arm's; and the dark band to the box's interior is 12 px with no tan strip in it, where the
upper box (row 4138) has a tan strip between poly and ring.

Findings, all geometry only, each checked by the tracer (`px.py row 4135`, `row 4160`, pt
(3700,4308)):

1. The vertical poly's east edge is about x 3712 (drawn 3710). Fixed (and the arm's box and
   diffusion start at x 3716, so the join still rests on the `?P` alone).
2. The link strip is y 4302-4318 at x 3700 (drawn 4296-4320). Fixed.
3. The VSS box's east edge is about x 3678 at y 4160 (drawn 3688). Fixed; its upper part still
   reaches the poly.

Found correct: the vertical poly's top (a rounded cap at y 4094, a green rim between it and
the strip, no contact on the poly); the pad (3540,4068) and its poly into the node's box; no
contact at any of the seven crossings of the metal x 3540 ((3542,4286) and (3545,4548) are
blemishes of chip 2); the column and the VSS box are one outline (the weak line is the rail's
margin); the boxes east of the rail are diffusion, with diffusion east of the channel; the
link; the third gate across the whole box; nothing leaves the lower node's box; the strap
(no contact on plate B); three VCC contacts; the inverter (field y 4352-4376 above its node,
gate across the rail's diffusion, tab as the NOR cell's); NOR 3 (1.7 % and 3.5 % bad blocks,
top arm on a contacted VSS box). Not checked: whether any buried contact box ties (all read
from outlines); the rows west of x 3521; the plates east of the VCC rail at (3882-3940,
4215-4310), which are the east column's.

`tools/t.sh tl3 sameconn.py b5bd64c`: `connections identical`.
`.venv/bin/python tools/sameconn.py b5bd64c`: `connections identical`.

Round 1: no findings that change a connection.

**Round 1, full review of latch B** (2026-11-17 18:21 -0600, a fresh Fable 5.2 agent, 52 tool
uses, 20 images in `cache/scratch/tl3/review-4/`; commit reviewed 794186a). Told to suspect: a
cell copy differing from its master by one contact, box or poly end (the inverter's
pull-down, both third pull-downs, the buried boxes, the thin metal x 3605 and `follow.py`'s
contact candidates on it); whether the metals on x 3540 around y 4920-4972 are two; the
enable metal's three pads and any further contact on it; the data row and the pad (3540,4912)
against the enable pad 13 px below; the VCC box and contact, the VSS box below the stack, the
rail contacts; the stub reading of `tl3_w5156`; anything left out in x 3533-3885,
y 4818-5310. It checked with master-against-copy mosaics (2.1x) and 4x slabs in the clean and
chip-2 stripped shots, text maps and profiles at each pad and crossing, and 4x to 5.3x views
in two to four shots.

Findings, all geometry only or omissions, each checked by the tracer:

1. A box under the VCC rail, x 3825-3872, y 5192-5258, with a metal contact near (3845,5222),
   is not drawn. A strip leaves it east under a plate east of the rail: the VCC end of an
   east-column load; nothing goes west from it. Added to Not done.
2. The VCC contact (3847,5030), drawn 24x36, is one long ring y ~5025-5108 (the tracer's own
   `textmap.py 3826 4996 3870 5050 3` has the ring from y 5017 on). Fixed: `C 3847,5066 s=24x84`.
3. The stub of `tl3_w5156` is drawn from x 3582 (the cell's); the poly ends at the box's
   outline, x ~3590-3597. The stub reading is right. Not changed (`tl1`'s cell).
4. The cell's inverter gate is drawn x 3693-3705; the salmon runs x 3696-3706. The channel is
   there (`px.py col 3700`). Not changed (`tl1`'s cell); passed on in the handoff.
5. The VSS contact's ring is centred nearer (3663,5277) than (3662,5284). Fixed.

Found correct: two metals on x 3541 (no metal at y 4940-4962; the pads (3540,4912) and
(3541,4980) are separate polys with field between); the data row one poly with the pad
(3540,4912); the enable metal's three contacts and no others, nothing at the crossings y 5025
and 5112, both rows on west past x 3533; the thin metal x 3605 (contacts only at (3604,4839)
and (3597,5245); over the two buried boxes it has no hole, as in the master); the thin metal
x 3784 (two contacts); a field gap between gate 2's east end and the third pull-down band;
the upper third gate one poly with the lower plate's top bar; the rail contacts and boxes; the
rail to y 5325; the copies against the masters. Not checked: the plates' ties (AMB-026);
x 3533-3575, y 4818-4895 by image; a green strip at x 3881-3885, y 4867-4920 on the east edge.

`tools/t.sh tl3 sameconn.py 6f72ec6`: `connections identical`.
`.venv/bin/python tools/sameconn.py 6f72ec6`: `connections identical`.

Round 1: no findings that change a connection.

**Round 1, full review of the two east NOR units and their wiring** (2026-11-18 07:55 -0600, a fresh
Fable 5.2 agent, 52 tool uses, images in `cache/scratch/tl3/review-5/`; commit reviewed
fe3aa04). Told to suspect: whether track A is one metal and the metal x 4148 below it a
separate one; the L-shaped metal's join to the pad (4148,4200); every claimed contact and
every crossing without one; the long row y 5318-5342 for a break or a contact; the two cell
copies (gates, arms, the output box, the load under the rail and the thin metal x 3948-3962,
the tab); further connections of the outputs and gates; anything left out at x 4045-4250,
y 4130-4360 and 4960-5350. It checked with profiles, text maps and the follower, and 4x-6x
views in two or more shots.

Findings:

1. **Changes a connection.** `inh_ck` does not end at the pad (4147,5005): a metal arm goes
   on west and south to a contact (4104,5633) (above, in the wiring table). Confirmed by the
   tracer (`arm1.png`, `arm_s.png`; the contact's hole in `textmap.py 4084 5612 4130 5656 3`).
   Fixed: the metal, the pad, the contact and the start of the pad's poly are drawn. No
   equation of the package changes; the net gains a sixth pad. The reviewer left one point to
   the tracer: the boxed poly end at 4088-4112 x 5188-5216 under this metal. Read as a
   pass-over (no hole: profiles above), recorded as an assumption.
2. Geometry only: e3's bottom arm is at y ~4303-4316 (drawn 4296-4310). Fixed in the cell.

Found correct: track A one metal from (4148,4200) to (4147,5005) (the dark bands are 8-10 px
edge bars); the pad (4148,4200) is mid-metal and the L continuous with it, no contact along
the L; all nine contacts (ring, bright centre in both metal shots, green hole); no metal at
y 5010-5060, so the metal x 4148 is separate; no hole under track A, `rcs_mv` or the metal
x 4148 except at the pads; e3's output and gate 2 cross the tracks without contact; the row
y 5318-5342 one poly from x 3560 to 4132 with no hole under any metal; both cell copies at 4x
(the thin metal x 3948-3962 passes the load strip and tail without contact). Not checked:
north of y 4106; e5's gate 2 row inside the gaps between the tracks in the chip-2 stripped
shot; the loads' VCC end beyond x 3877; whether the long row gates anything.

Round 1: one finding that changes a connection, fixed.

**Round 2, fix check** (2026-11-18 07:59 -0600, a fresh Fable 5.2 agent, images in
`cache/scratch/tl3/review-6/`; changes since fe3aa04). Told what changed and to test: the
arm's join to the pad (4147,5005) and its continuity to (4104,5633); a contact anywhere on the
way (the node box at y 5050-5083, the boxed poly end at y 5188-5216, each row crossed); its
separation from the metal x 4142-4155; the south contact and where its poly leaves; anything
disturbed. It found the arm right (9 px of dark at the join against 15 px of ring where track
A arrives; the same streak between every dark bar in both metal shots), no contact on the way
(clean shot green only at the south pad; the two boxes read alike, tan centres 177/165/126 and
185/164/139 with metal centre R ~118, against 162/178/105 and R 208 at the real contact), bare
ground between the two metals on every row sampled, the contact (4104,5633) real with its poly
leaving east only, no metal south of y ~5650, and the bottom arm right (y 4303-4317).

Two notes, geometry only: the VSS box below the unit clipped gate 2 by 2x1 px (two sliver
warnings): fixed, box top at y 4301. The arm peaks at x ~4111 for y 5010-5130, drawn
4100-4112: not changed (same ends).

`tools/t.sh tl3 sameconn.py 945a512`: `connections identical`.
`.venv/bin/python tools/sameconn.py 945a512`: `connections identical`.

Round 2: no findings that change a connection.

**Round 1, full review of latch C and its wiring** (2026-11-18 15:25 +0000, a fresh Fable 5.2 agent, 89 tool
uses, images in `cache/scratch/tl3/review-7/`; commit reviewed b5c7392). Told to suspect: the
uncertain contact (3955,4541); anything in which the mirrored copy differs from its master (the
vertical inverter gate, the three buried boxes, the stub on the upper node's box, both third
pull-downs, the gap between gate 2's west end and the third gate's band); the stack's and the
strip's join to the VSS box below; the thin metal x 4077-4089 between its pads; the clear's
metal (its separation from `rcs_mv`'s pad, other contacts on the way south, the corner); the
output metal's ends; every row under a track; the contacts placed from text maps; anything left
out in x 3870-4250, y 4514-4970. It checked with text maps, profiles and the follower, a mirror
comparison with the master, and 2.7x-7x views in two or more shots.

Findings, each checked by the tracer:

1. **Changes a connection.** The `?C` at (3955,4541) is most likely a pass-over: the thin metal
   x 3948-3962 has two real end contacts on pads, (3930,3616) and (3953,5459), neither on latch
   C; the clean shot's pale patch is a band the box's full width, as under thin W in the
   master. Checked (`textmap.py 3906 3590 3972 3640 3`, `3920 5436 3980 5480 3`: both end
   contacts with ring, bright centre and green hole; `px.py row 4366 2684 2722 3`, `row 3758`:
   the master's band). The spot itself stays ambiguous (round bright centre at full
   brightness), so this is the better working assumption, not a proof: Ambiguity 6. Fixed: the
   `?C` and `@alias tl3_e4537 tl3_tm3955` removed; `tl3_tm3955` is a net of its own.
2. **Left out** (a contact and two ports: counted as changing a connection). A pad with a
   contact (4233,4915) on the track x 4236, its poly east across x 4250 and a metal south from
   it. Confirmed (`textmap.py 4204 4868 4264 4940 3`: ring, bright centre, hole at (4234,4918);
   bare ground between it and the output pad) and followed: the metal runs to y 5766 and east
   out of the strip, no other contact. Drawn as `rcs_mv`.

Found correct: the three equations; the vertical inverter gate (joined to the data row, channel
y 4580-4608); the stub (ends at x ~4122, ground at x 4129-4135 in both metal shots); gate 2
and the third gate's band two polys (ground at x 3978-3987); the strip y 4956-4970 and the
stack onto the VSS box; the VSS arm; the upper third gate's turn south; pad, stem and band of
the lower third gate; all pads' contacts; no contact under any track on the five rows; the
data row, the row y 4496-4510 and `rcs_mv`'s poly across x 4250; the clear's metal (bare ground
at y 4767-4785 in both chips, one contact (4192,5373), a simple corner); the output metal (bare
ground north of y 4440); the mirror comparison. Not checked: the continuity of the thin metal
x 4077-4089 over the two boxes (dim in both shots at y 4706-4739 and 4835-4870, no bright
centre and no hole there); the two load ties (`?`); the north unit's plate tie; the VCC contact
(3846,4772) beyond a 2.7x view.

`tools/t.sh tl3 sameconn.py b5c7392` after the fixes: `CONNECTIONS DIFFER`, the intended ones
(`tl3_tm3955` apart from `tl3_e4537`; the new net `rcs_mv`).

Round 1: two findings that change a connection, fixed.

**Round 2, fix check** (2026-11-18 15:34 +0000, a fresh Fable 5.2 agent, 8 images in
`cache/scratch/tl3/review-8/`; changes since b5c7392). Told what changed and to test: its own
judgement of the spot (3955,4541) against real contacts of thin metals on pads, the master's
box under thin W and a certain pass-over; `rcs_mv`'s pad, its separation from the output pad,
the metal's whole run south, the corner, where the pad's poly leaves; anything disturbed; both
`sameconn.py` runs. It found both changes right. The spot: the metal shots do not decide it (a
centre at full brightness, but between two straight bars along the poly row's edges, not in a
round ring, and the metal keeps its 13 px width); in the clean shot a grey band 4 px high
(y 4540-4543) across the box, red minus green 0-6, no pits, as in the master's boxes (-3..10 and
5-20), where real contact holes are round, about 8 px, red minus green -5..-16: a pass-over.
`rcs_mv`: the pad closed west, north and south, its poly on east past x 4250 along
y 4903-4928; bare ground y 4862-4898 between it and the output pad in both metal shots and no
poly there in either stripped shot; uniform poly, no hole and no widening at every row the
metal crosses (4x views of y 5040-5680); a plain corner. Not checked: that a contact would
short two outputs (it rests on the undrawn end pads; (3930,3616) confirmed as a contact).
`tools/t.sh tl3 sameconn.py b5c7392` and `.venv/bin/python tools/sameconn.py b5c7392` show only
the intended differences (`tl3_tm3955` apart from `tl3_e4537`; the new net `rcs_mv`).

Round 2: no findings.

**Round 1, full review of the three units under the east rail** (pieces A y 4345-4514, B
y 3450-3660, C y 3655-3845; 2026-11-18 16:39 +0000, a fresh Fable 5.2 agent, 90 tool uses, 19 images in
`cache/scratch/tl3/review-9/`; commit reviewed 5629748). Told to suspect: A's `?D` link, the pad
(4193,4420) and its track, whether the strip in the gap is diffusion or a vertical poly, the
column's join to the VSS box above; B's diffusion east of the rail under both rows, the stub,
the thin metal x 4099-4111 over the box, the two pads, the plate's foot pad; C's pad poly into
the row, a second transistor east of the rail, the C-shaped poly (one line? touching the gate
row? through the box? across the column?), the column's joins, the thin metal over the box and
the band; the supply contacts; anything left out in x 3870-4215, y 3440-3850 and y 4340-4520.
It checked with profiles, text maps, the follower and `opendiff.py`, and 4x-5x views.

Findings, each checked by the tracer, all geometry only:

1. B's tail was drawn `?D 3954,3508:3972,3540`; the diffusion is at x ~3967-3983 from the strip
   up to y ~3485, with field at (3958-3964, 3520). Confirmed (`px.py col 3977 3476 3548 6`).
   Fixed: `D 3966,3486:3984,3540`; the tie still rests on the `?P` and `?B`.
2. C's pad poly was drawn 12 px wide; it is x ~4144-4164. Confirmed (`px.py row 3635 4132 4172
   4`). Fixed.
3. A gap in the notes: the thin metal x 4099-4111 over C's box (a bright centre at (4101,3719)
   in 50 px of dark, clean shot tan): a pass-over, now written under the inverter.

Found correct: A: two gates across the column with channel to x ~4077, the column continuous
to both VSS contacts, no contact under either track on the three rows, the pad (4193,4420) a
contact on a track that runs y 4112-4748, the gap strip and its tail diffusion, **the `?D` link
supported** (the column's edge line at x 4080 is absent at y 4416-4426 in three shots,
`a_link.png`; left `?` here). B: channel to x ~4077 under both rows, both pads contacts, the
box a stub ending x ~4121, the thin metal over it a pass-over, plate, neck and foot pad one
poly with the thin metal's north end on it. C: the pad's poly turns into the row as an L; 10 px
of bare ground between the row and the C-shape's top band in three shots; field east of the
rail above the row and under the rail between node and VSS box; the C-shape one poly, its
bottom band ending at x ~4051 and gating the column between the arm and `tla`'s node; the
contacts. Nothing left out in either window. Not checked: the three load ties (unresolved at
5x); the continuity of the thin metals x 3948-3962 and x 4099-4111; `r9m`'s stub at y 3376.

    tools/t.sh tl3 sameconn.py 5629748             -> connections identical
    .venv/bin/python tools/sameconn.py 5629748     -> connections identical

Round 1: no findings that change a connection.

**Round 1, full review of run 8's three pieces** (A the inverter at y 5180-5300, B the top unit
E1, C the load of `rcs_mn3852`'s unit; 2026-11-18 17:51 +0000, a fresh Fable 5.2 agent, 84 tool uses, 19 images
in `cache/scratch/tl3/review-10/`; commit reviewed 9754c80). Told to suspect: A: the thin metal
over the box at (4101,5202), the box's join of node and row, field or diffusion east of the
rail below the gate, the strip through the gap, contacts under the tracks; B: anything leaving
the box at (4076-4114, 2972-3010), the row y 2956-2973 under both rails and its joins to the
plate and the pad, the VCC rail over the contact; C: what the strip touches under the VSS rail,
the VCC box as one diffusion, the join onto `tla`'s node box; all: widths (a second patch
beyond the rail), contacts, anything left out. It used profiles, text maps, the follower,
`opendiff.py`, `unsure.py` and 4x-5x views.

Findings, each checked by the tracer:

1. **Changes a connection. Confirmed.** Piece C leaves out a diffusion branch of the node: from
   the load strip south under the thin metal (x ~3952-3968, y 3863-3982), east as a band
   y 3966-3984 under the VSS rail, onto the diffusion below `tla`'s gate `rcs_mu`; and `tla`'s
   column from there down to `rcs_in1`'s node is field at y 3988-4052. Checked: `px.py col 3962
   3832 3996 4`, `row 3976 3940 4096 4`, `col 4070 3944 4112 4`, `textmap.py 3940 3934 4124 4064
   4 --acid`, `fx_a.png`, `fx_mu.png`, `fx_ov.png` (Logic, "The third pull-down"). Fixed in two
   commits: `trace/tla.txt`'s column split (e22fb03), the branch drawn here. Result:
   `rcs_mn3852` = NOR(`rcs_in1`, `rcs_mu`, `tl3_e3712`), `rcs_in1` = NOT `rcs_mv`.
2. Geometry only. Confirmed. B's strip in the open is y ~2989-3010 (drawn 2984-3008): `px.py col
   3978 2974 3018 3`, `col 3910 2974 3018 3`. Fixed: y 2988-3010.

Found correct: A: no contact at (4101,5202) (a 9 px half-bright spot, no hole, no widening,
against the real contact (4104,5633)); the row y 5190-5205 ends in the box; both rows pass every
track and the thin metal without hole or ring; field east of the rail below the gate (clean
shot as field; the chip-2 stripped shot slightly redder, 8-13 against 2 for field and 24 for
diffusion); the strip continuous through the gap with no poly across; channel x 4010-4056; the
two pads in `tl4`'s strip are real contacts and the follower joins them (text only). B: no
hole at the box in either stripped shot, nothing leaves it, a field band y 3008-3017 between
it and the gate row; the row y 2956-2973 one poly from pad to plate under both rails; plate and
row one poly; the VCC rail continuous y 2924-3048; field east of the rail; the gate row on past
x 4250. C: the VCC box one diffusion y 3757-3866 with a real contact (3846,3838); the strip
under the rail y 3845-3865 with field above and below; the join at x 4048-4058 a single line
in each shot; no thin-metal contact at the tie box. Overlays fit; no open diffusion left out
in the three rectangles. Not checked: the three ties (uncertain; all three equations depend on
them); the thin metal x 3948-3962 beyond these crossings; the inside of gate mu's transistor.

    .venv/bin/python tools/sameconn.py 9754c80     -> CONNECTIONS DIFFER (6 differences): the transistor
        under gate rcs_mu moves from rcs_in1 to rcs_mn3852, and the two equations change as above

Round 1: one finding that changes a connection, fixed; one geometry finding, fixed.

**Round 2, fix check** (2026-11-18 18:07 +0000, a fresh Fable 5.2 agent, images in
`cache/scratch/tl3/review-11/`; changes since 9754c80 in `trace/tl3.txt` and the split line of
`trace/tla.txt`). Told what the three changes were for and to be hard on the first: the stripe's
continuity with the load strip and the band, the band as diffusion (not poly) and unbroken to
east of the rail, whether x 4055-4090, y 3990-4060 is field or a colourless diffusion wire,
what is left on `rcs_in1`'s node, whether the transistor under gate `rcs_mu` is there.

It found the three fixes right as drawn: the stripe x 3954-3970 protected tan with edges at
x 3953 and 3971 and no edge across at y 3864 or y 3966 in any shot, ending at y 3984; the band
diffusion and not poly (185/173/128 against gate mv under the same rail, 240/176/130), both its
edge lines unbroken from the stripe to east of the rail, the dark bar at x 3976 the gap's
artefact (the same on the load strip at y 3850, absent in both metal shots), no gate across
it, field between it and the VSS box above and everything below; x 4055-4090, y 3990-4060
field (flat in four shots, no inner edges, edge lines across at y 3986 and y 4064); no contact
of either thin metal onto the node; findings 2 and 3 as drawn. `sameconn.py 9754c80`, the
package alone and every file: only the intended differences.

No finding on the changes. Two observations on `tla`'s older geometry, not checked by me and
passed on in the handoff (same nets either way; `trace/tla.txt` is not changed for them):
gate `rcs_mu`'s channel is x ~4072-4108, not 4052-4110, and the piece below it an L; the
pull-down of `rcs_in1` under gate `rcs_mv` is under the rail, and east of the rail below that
gate reads field, so `D 4052,4066:4090,4135` should stop at y ~4096.

Round 2: no findings.

### Run 9: the foot's rows and the thin metal x 3948-3962 (one review for both pieces)

**Round 1 (full review), 2026-11-18 19:48 +0000**, a fresh agent on Claude Fable 5.2, commit before the
round 2e448e2, 25 images in `cache/scratch/tl3/review-12/`. Pieces: F (the foot, x 3533-4250,
y 5345-5660) and T (the thin metal x 3948-3962, y 3614-5468).

Told to suspect, piece F: a row broken or stepping a track under a rail or metal; the dark
stripe on row y 5371 at x 3881-3887; row y 5500 at x 3540-3556; poly between the two pads at
y 5458; whether row y 5371 ends on the pad (4192,5373); the dim spot (3955,5411-5417); the two
west metals' corners; the joins to `tl2`'s and `tl4`'s rows at x 3533 and x 4250; a tap under
a rail; metal north of the pad (4040,5458). Piece T: each `?M` stretch for a break or a
contact; the firm crossings ((3955,4541), y 3650, 3719, 4522, 4937); y 3864-3984 (one line or
two); how the metal leaves its north pad.

What it checked (4-6x views in the metal shots and the clean shot, `px.py`, `textmap.py`,
`follow.py`, `tl3_thin.py`, the full extraction, `unsure.py`) and found as drawn: every row one
poly at constant y, unbroken under every metal and both rails, uniform in height, no hole; the
stripe a margin line (`f_c5500.png` for row y 5500's west end, 6x); field between the pads and
no metal north of (4040,5458) (`f_pads.png`, 5x); row y 5371 ends on its pad (`f_east.png`);
the dim spot in chip 2 only; both corners are corners (`f_corners.png`); the joins at both
edges are the same polys (`f_west.png`, `f_east.png`, `f_tcwa.png`); no tap under either rail
(`f_westrail.png`, `f_vccrow.png`: dark blotches on the rails over rows y 5371 and 5458 in chip
2 only, no hole); the slots are field. Piece T: the north pad's metal leaves east then south
only (`t_north.png`); one line with no step and no second line over y 3864-3984 (161-229 in
chip 1 against 136-150 for bare ground); the 8-13 px bars need no `?M`; all six `?M` stretches
at 5-6x have no pad, no widening and no round hole with pits, each with a small bright spot
inside the box, like the reviewed pass-over at (4101,5200).

Findings, each checked by me:

1. `M 4037,5448 y5660` sits 4-5 px west of the metal, which is x 4036-4047. **Confirmed**
   (`px.py row 5565 4024 4054 3 metal,metal1`: metal 4036-4048 in both shots; I had read the
   columns of my text map one sample off). Geometry only: it overlapped the pad and contact
   either way. Fixed: `M 4042,5448 y5660 w=13`; the notes and `ports.d/tl3.txt` say x 4036-4048.
2. Ambiguity 11 named a greenish band in the clean shot only at y 4482-4487; the same
   east-west band lies under the line at y 4300-4306 (147/151/86 at x 3957), 3714-3723,
   3860-3866 and 3978-3982, each at the south edge of a diffusion feature and 16-40 px wide,
   wider than the metal: not contact holes. **Accepted** (notes only): it weakens the one
   point "against" in Ambiguity 11; added there.
3. (3955,4541) is the most contact-like spot on the line (full metal brightness in both
   chips, 219/194/98 and 236/193/82; clean shot 169/168/127; no pad, no pits; `t_4541.png`, 6x):
   Ambiguity 6 stands, and what `rcs_e4` rests on should name it. **Accepted** (notes only):
   added to the thin metal's section and to `notes/operation.md`.

It could not check: whether the metal is unbroken and without contact over the six boxes
(neither metal shot shows it: the `?M` stands); where the metal from (4040,5458) goes south
of y 5660; and the slots between the rows y 5543 and y 5585, which read 13-14 (red minus
green) in the chip-2 stripped shot against -1 to 6 in the slots further north, and khaki in
the clean shot. I measured them (`px.py pt 3750,5563 3910,5563 4000,5563 4070,5563 3750,5392
3910,5392 3750,5437 3950,5630 acid,acid1b,metal,metal1`): 8-25 in the stripped shot against 5-8
elsewhere; in the clean shot 95/90-95/53-57, darker than the other slots (132-137/118-121/83)
but not green (an open diffusion is 118/155/90 there); both metal shots as field
(155-160/130-135). The slot is 26 px high, the others 29-30, so the rows' rims fill it. Taken
as field; no poly crosses it, so it could not be a transistor either way.

Connections before and after the fix of finding 1:

    tools/t.sh tl3 sameconn.py 2e448e2             -> connections identical
    .venv/bin/python tools/sameconn.py 2e448e2     -> connections identical

Round 1: no findings that change a connection.

### Run 10: the row y 2899 and the thin metal x 4099-4111 north of track A

**Round 1 (full review), 2026-11-18 21:53 +0000**, a fresh agent on Claude Fable 5.2, commit before the
round d6e9b8a, 14 images in `cache/scratch/tl3/review-13/`. Piece N (x 3533-4130, y 2880-4108).

Told to suspect: a contact between the thin metal and one of the six boxes it crosses (the
bright spots at (4103,2986-2992), (4101,3410-3419), (4101,3716-3725), (4102,4072-4078)); a break
(a pad or widening; whether the line is there at all over y 3826-3969); the firm stretches (a
sideways step, another line); the pad (metal leaving another way, poly leaving north or east,
the row passing under it); the row (a break or tap under the two rails, the two dips, the join
at x 3533, a swap with the row y 2857).

What it checked and found as drawn. (a) No contact on any box: the spots are 6-8 px by 12-15,
on each box's floor; the metal shots alone do not settle it ((4103,4075) is as bright in chip 2
as a real centre), but in the clean shot every box interior is cream, red over green
(194-208/161-180/128-138), where the real holes at (4105,2899) and (4106,5633) are green over
red (155-160/169-173/102), and in the chip-2 stripped shot the boxes under the metal look like
the boxes at (4097,4241) and (4097,4417) that no metal crosses, while three real contacts
nearby show an olive patch in a salmon pad (`mosA.png`, `mosB.png`, 4x four shots; `b3400.png`
6x; `b3719.png` 5x). (b) No break: no pad or widening; over y 3826-3969 a 6-8 px strip at
x 4100-4104, metal-coloured in both chips (177/148/71, 171/170/62) between dark edges, and the
clean shot protected out to x ~4120 all the way (`dim.png`, 5x). (c) The firm stretches are
straight at x 4105 with row-edge bars only; `follow.py` finds no corner; its candidate at
(4101,3911) is a row-edge bar; it is the line that reaches (4105,4106). (d) The pad: ring and
centre in both metal shots, hole in the clean shot, metal south only, the row runs into it,
nothing leaves north or east (`pad.png`, 4x). (e) The row: one poly from x 3500 to the pad, at
`tl2`'s y, field between it and the row y 2857 throughout, salmon without a hole under both
rails (`wrail.png`, `erail.png`, 5x); two marks are dirt in one shot each; the VCC rail's top
is at y ~2912.

Findings: none. One remark, on marking only: the line is narrow and dim from y ~3783, where
the trace was firm to y 3828. **Accepted**: `tl3_thin.py 4095 4115 3750 3830 --thr 176 --min 3`
has three bars of 10-12 px there with one shot dark between them; the `?M` now starts at y 3771.
It could not check: the "no contact" reading has no electrical cross-check, because `inh_ck` is
only ever a gate in the extraction and its source is untraced, so a contact on one box would
make that unit the driver (taken into Ambiguity 13, with my own measurement of the same six
points: `px.py pt 4103,2989 4101,3414 4101,3720 4103,4075 4105,2900 4106,5633 4097,4241 4097,4417
acid1b,acid,metal,metal1`); the middle of the row (x 3710-3790, 3870-3985) was read from text
maps and 3x only.

Connections before and after the change of marking:

    tools/t.sh tl3 sameconn.py d6e9b8a             -> connections identical
    .venv/bin/python tools/sameconn.py d6e9b8a     -> connections identical

Round 1: no findings that change a connection.

### Run 11: south of the foot, y 5660-6350, and three corrections to `trace/ur.txt`

**Round 1 (full review), 2026-11-18 22:43 +0000**, a fresh agent on Claude Fable 5.2, commit before the
round 1ce8e16, 14 images in `cache/scratch/tl3/review-14/` (its report says 16). One piece: the
wiring of pieces S1-S5 (x 3533-4250, y 5660-6350) with the three lines of `trace/ur.txt` changed
in a1c5d8b (y 6330-6700).

Told to suspect: the cut of `ur`'s poly between the pads (3757,6410) and (3968,6410), decided
from text maps only; the bare stretch x 4004-4064 on the row y 6327; pad A's contact (dim centre
in chip 2) and the pad (3607,5938); the L3 metal from its pad to the step (a break, a contact on
a row, the diagonal, anything at x 3780); the gab metal's shift; the chip-2 blob on the VSS band
over the vertical poly; the specks on the rails; the 8 px between the horizontal metal and
`tla`'s row and the two corners; the pass-overs (x 4236 over the row y 5718, x 4042 over `tla`'s
row in particular); anything undrawn (the outlined areas, the strip y 6167-6182).

What it checked and found as drawn. (a) The cut: x 3780-3950, y 6400-6420 is bare ground in both
metal shots and both stripped shots, field under the L3 metal and the VSS leg; the poly reaches
the pad (3757,6410) from the west only; the pad (3968,6410)'s poly leaves east, unbroken to
x 4260 with no hole under the gab metal or the VCC leg; no metal between the pads (3968,6410) and
(3968,6520) (`U.png`, 4.4x four shots). (b) The gap between pad A and pad B is bare in all four
shots (`padAB.png`, 5.3x). (c) Pad A is a contact: bright centre in chip 1, green hole in the
clean shot, a pit in the chip-2 stripped shot; the pad (3607,5938) too (chip 2's centre is split
by a dark bar: `s2padw.png`); the other five pads have a bright centre in both chips and a hole.
(d) The L3 metal is one metal at x 3794-3808 from its pad to y ~6670 and a diagonal to x 3780, in
both chips, with no pad or hole on any row it crosses and nothing at x 3780 north of the step
(`l3run.png`, `l3step.png`); the gab metal shifts east at y ~6597-6606 in both chips
(`gabstep.png`). (e) The blob at (3808,6222) is in chip 2 only, over plain protected poly with no
hole and no pad (`s3poly.png`). (f) The rails' specks differ between the chips and the clean shot
under both Ls is field; `railprof.py` calls y 6091-6118 under the VCC rail "diffusion", which is
the grey-green centre band (the same colour at (3846,5800)), with no outline in either metal shot
(`Ls.png`). (g) The strip y 6167-6182 is bare in both chip-2 shots. (h) Field under the
horizontal metal y 5866-5882, no hole, corners as drawn (`s3corners.png`). (i) Pass-overs: x 4236,
4192, 4042, 3608 and both rails over the row y 5718; x 3608, 4042, 4192 and both rails over
`tla`'s row; x 3912 over the rows y 5936 and y 5979; the L3 metal and both legs over the row
y 6327: bright over the row, no hole. (j) S2's poly ends at the pad (3954,5938); the metal east is
unbroken (`follow.py`, 500 px) and separate from `amrw`'s. (k) Nothing undrawn (`sv.png`,
`sv2.png`; `opendiff.py`: none). (l) Extraction 2,342 nets, 4,200 transistors, 0 errors;
`unsure.py` lists none of the run's nets; `sameconn.py` on `ur`: connections identical.

Findings: none. One thing it saw outside this run's lines, geometry only, in `ur`: `sl_l3`'s
metal steps west at y ~6665-6700, not at y 6560 as drawn (`l3run.png`); not changed here (it is
in the handoff, with `ur`'s `vcc` line x 3630).

It could not check: where the pad (3968,6410)'s poly goes east of x 4260 (not drawn:
`rcs_thin_e`'s far end); `ur`'s cells south of y 6700; and a dark mark in the chip-2 metal shot
at (3536-3545, 5704-5716), beside S1's pad, which it judged from chip 1 and the clean shot only.
The last, checked after the round: `tools/t.sh tl3 px.py pt 3540,5710 3540,5760 3540,5680
acid,acid1b,metal,metal1`: chip-2 metal 52/34/15 at the mark against 152-158/128-131/77-87 beside
it, chip 1 the same at all three (138-142/114-129/77-80), the clean shot green open field
(123/158/82): dirt on chip 2, nothing drawn there.

Round 1: no findings.

## Not done

- Next: the rows above y 2890 (y 2580-2880: `r9m`'s and `tla`'s lines cross here; the row y 2857
  of `tl1_w2857`, the row y 2813 of `tl1_w3678`).
- (Done, run 11: south of the foot, y 5660-6350.) Left from it, all outside the strip: the poly
  that leaves `ur`'s pad (3968,6410) east along y 6402-6422 (seen to x 4256: `urch`'s region),
  which is where `rcs_thin_e` goes; `tl5_w5936`'s bus line south of y 6350 (the source of
  `tl3_w3982`); `c4l_gab`'s driver. In `ur` (not changed): `sl_l3`'s metal is drawn stepping
  west at y 6560 and is still at x ~3757 at y 6650; `ur`'s `vcc` line x 3630 is drawn from
  y 6330, with no metal there down to y ~6570; the poly that reaches the pad (3757,6410) from the
  west is drawn to x 3560 and not followed.
- The six uncertain stretches of the thin metal x 3948-3962 over tie boxes (Ambiguity 11).
- `rcs_mv`'s two ends east of x 4250 are `tl4`'s.
- The clear's metal east of (4250,5895) is `tl4`'s. `tl3_e4635` and `rcs_mv`'s poly east of
  x 4250 are `tl4`'s, and `tl3_e3028`'s row (E1's gate).

- In `tla`'s units around the branch: the inside of gate mu's transistor (its channel is
  probably x 4072-4095, not 58 px); what gate `rcs_mv`'s row does under the rail; and whether
  any other of `tla`'s columns east of the rail is drawn through field (the unit at y 4165-4335
  was re-drawn by `tl3` as `tl3_enor`; `rcs_mu`'s inverter at y 3320-3436 was not re-read).
- **For `tl4`** (its strip, claimed; not drawn here): the pad with a contact (4278,5198), the metal
  x 4279 north from it to the pad with a contact (4278,4636) on `tl3_e4635`'s row (which closes
  the open join `tl3_e4635`), and `tl3_e5240`'s row east of x 4250, which turns south at
  x ~4265-4290 beyond y 5255.
- `inh_ck`'s source (east of the strip: the row y 5631 into `tl4`, `tl5`, `tl6`).
- Where the true outputs of latch A and latch B are taken (`tl3_w3550`, `tl3_w5156` end in
  stubs; only the inverted outputs leave west).
- Where the seven rows of the pair, the inverter and NOR 3 go west of x 3533 is `tl2`'s.
- The six uncertain stretches of the thin metal x 4099-4111 over node boxes (Ambiguities 12, 13).
- The metal north of the link (review round 1: wider
  metal x ~3648-3762 above y 2598, a supply feed, not drawn); the VCC rail's top (y 2918) is `tla`'s.
- The VCC box of NOR 4 runs on south of the cell's box with more contacts (review: y 4700-4810):
  not drawn. (NOR 1's is drawn since run 8: it is the VCC end of `rcs_mn3852`'s load.) The inverter's VCC
  box has more contact marks than the one drawn.
- The west rail is drawn to y 5330 from low-zoom views; its contacts between the drawn boxes are not read.
- The rows of latch A west of x 3533 are `tl2`'s.

## Corrections (coordinator, from the handoffs of 2026-11-18/19)

- `inh_ck` (track A) is `inh_ck` (`eof` run 2, firm): latches B and C, and through AMB-033 `tl1`'s two
  latches, are master/slave pairs on `inh_ck`.
- `rcs_x1` = NOT `lc1_w7170` (`lc1`'s gate 2; `eof` run 2).
- From `tl4` (2026-11-18), where this file still says so: `rcs_mv`'s poly at (4250,4736-4751) is an
  output (it leaves and comes straight back as `rcs_mv`, one L in `tl4`'s strip); `tl3_e3028`, "gate
  of the top unit E1 ... from the east", is `tl4_w4590`, which crosses x 4250 again at y 2801-2820 (the
  pad (4366,2812)): that row is the only way left to `tl4_w4590`'s driver.

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The signal on track A / line X / the first through line of the left-centre strips, which these notes call a clock, a strobe "once per scan line" or leave without a source, **is the reset**: `rst_a`, the buffered copy of `rst` = NOR(`lpstb_b`, `res_b`) made by `lc1`'s gate 5 (`eof` run 10, piece `isrc5`, firm). `inh_ck`, `inh_rc` and `inh_lat` are further buffered copies of it: high while the RES and LPSTB pins are both low, and only then. The belief "a strobe once per scan line" is withdrawn.
- `rcs_x1` = NOT `lc1_w7170`, and `lc1_w7170` = NOT `rst_c` (`eof` run 13, piece `rc`, firm): the clear of the step logic's five latches is the reset, two inverters later. Where these notes call its source open, it is found.
- `tl3_w3982` (= `tl5_w5936`) is followed (`eof` runs 11-12): it is latch C's data in `lc2` (`lc2_w8906`) and is driven by the inverter U4 at (7575,8386): `tl3_w3982` = NOT `eof_w8298`, three inverters after latch D's lower node `lc1_w7928`.
