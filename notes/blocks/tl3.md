# tl3: top-left random logic, strip 3 (x 3533-4250, y 2500-6350)

Trace: `trace/tl3.txt` (`@requires tl1`, which requires `tla`). Views: `cache/scratch/tl3/`.
Started 2026-11-17 16:52 -0600 (Matt Godbolt's second session; the first holds `tl2`).

The strip holds the **middle cluster** of the row counter's step logic (`notes/blocks/tla.md`
names it: "the same construction 1042 px east"), the poly rows above it and the bus rows
below it. `tla` drew three things in it: the unit that makes `rcs_in1` (4081,4072), the
inverter `rcs_mu` (4050,3374) and the unit `rcs_mn3852` (4081,3852), with the VCC rail
x 3824-3868 and the east VSS rail x 3992-4041.

## Status

Traced, extracting (60 transistors of its own, 0 errors), the west column and three pieces of the east column:

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
  thin metals in the bus field east of it, the stretch of the thin metal x 3948-3962 over it (no contact) and a wire that passes through the bus field (`tl3_e4915`)
  (run 6, Tom Seddon, 2026-11-18 15:03 +0000).

Everything else in the strip is surveyed only (Inventory).

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
| x 3540-4250, y 5318-5342 | a poly row east from the pad (3540,5328) of latch B's enable metal, under the rail and across the cluster's foot. It is textured over x 3560-3640 and 3710-3815, where there are outlined areas above and below it (y 5270-5310, 5345-5355): diffusions it may gate, not read (`lb_row.png`) | drawn to x 3640 |
| east column, y 4165-4335 and 4990-5160 | the two NOR units (below) | traced |
| x 4099-4111, y ~3020-4152 | a thin metal down the east column over `tla`'s units, from a pad (4100,2900); it turns east at y 4152-4168 to the pad (4148,4200) and is track A from there. Bright most of the way (`px.py col 4101 3000 3880 20 metal,metal1`). Where it makes contact north of y 4106 is not read; over `rcs_in1`'s node box at (4102,4074) it has a bright centre in a dark surround in both metal shots and a patch in the clean shot that is neither a contact's green (186/182/139 against 140/150/85 at the contact (4146,4070)) nor a pass-over's tan (197/171/120 at (3606,5026)): undecided (`en_in1.png`, `en_in1b.png`, 9x) | drawn south of y 4106 |
| x 3870-4250, y 4514-4970 | **latch C** (below): `tl1_ua` and `tl1_ub` mirrored (`findcell`, clean shot: 1333,174 mx=2662.5, 0.75; 1334,174 mx=2662.5, 0.80) | traced |
| x 3948-3962, y 3616-5459 | a thin metal between the rails, over the east column's loads (the middle cluster's counterpart of `tla`'s thin metal E). **Its ends** (review 7, checked: `textmap.py 3906 3590 3972 3640 3`, `3920 5436 3980 5480 3`): north, it turns west at y ~3606 onto a pad with a contact (3930,3616), the foot of the load plate (x 3912-3950, y 3485-3600) of the rail unit at y 3440-3610; south, a pad with a contact (3953,5459) whose poly leaves west along y ~5450-5464. `follow.py 3955 4300 N` stops at y 3616 (its end), `S` at y 4454 (a stop only: it is there, bright, from y 4500 to 4960). Over latch C one contact-like spot, (3955,4541), taken as a pass-over (Ambiguity 6) | drawn y 4500-4960 only, no contact |
| east column, the rest (run 6 survey, `svA.png`, `svB.png`, `svC.png` 1.4x; `railprof.py 3992 4041 2900 5400`) | units built **under** the rail, none drawn: y 3440-3610 two gates under the rail (y 3498-3510, 3585-3597) with the node between them (y 3522-3578) and VSS boxes above and below (contacts about (4020,3470), (4020,3640)): a two-input NOR; y 3660-3830 one gate (y 3671-3684), node y 3695-3734, VSS box y 3761-3813; y 4350-4514 two gates (y 4366-4389, 4453-4477; the lower one is latch C's output row), node y 4390-4452, VSS box y 4478-4514; y 5190-5300 one gate (y 5235-5248), node y 5212-5227, VSS box y 5256-5300 with a contact about (4020,5280), its load's VCC box at 3825-3872 x 5192-5258. Loads west of the rail. `tla`'s `in1` unit by `findcell` (run 1) at 1,1129, 0,-1084, and turned at 0,-394, 0,-698 | not drawn |
| (4020,3030), y 2956-3066 | top unit of the east column, read by hand and not drawn: a rail gate (node strip y 2992-3015 under the rail, gate row y 3018-3038, VSS box y 3042-3090 with contact (4025,3062)); the node goes east to a ringed box 4075-4110 x 2972-3005 under the metal x 4095-4115 and west to a load (VCC box 3822-3870 x 2985-3045, plate x 3875-3935, y 2955-3030). `e1_q.png`, `e1_top4.png`, `e1_z.png`, `e1_load.png` | read, not drawn |
| y 5300-5560 | horizontal bus rows (metal) under the cluster's foot | not traced |
| y 5560-6350 | sparse wiring, a wide metal L at y 6100-6250 | not traced |

There is **no thin metal W** in this cluster's west column (the first cluster has one at
x 2689-2703): the middle of each unit, x 3700-3760, is in the open here, so the chip-2 shots
show its poly as orange.

## Logic

### Latch A (west column, y 3212-3652): traced

    tl3_w3233 = NOT tl3_w3333
    tl3_w3419 = NOT( tl3_w3333 AND tl3_w3373  OR  tl3_w3550 )
    tl3_w3550 = NOT( tl3_w3506  OR  tl3_w3373 AND tl3_w3233  OR  tl3_w3419 )

A cross-coupled pair: open while `tl3_w3373` is high, when `tl3_w3550` takes `tl3_w3333`
and `tl3_w3419` its inverse; `tl3_w3506` high clears it (`tl3_w3550` low). The same circuit
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
| y 3497-3515 | `tl3_w3506` (clear) | west under the metal x 3540 (no pad) out of the strip, to a pad (3455,3503) |
| y 3540-3560 | `tl3_w3550` (output) | a stub: rounded end at x ~3570. The true output is not taken west here |

### Latch B (west column, y 4818-5258): traced

    tl3_w4839 = NOT tl3_w4720
    tl3_w5025 = NOT( tl3_w4720 AND tl3_w4978  OR  tl3_w5156 )
    tl3_w5156 = NOT( tl3_w5112  OR  tl3_w4978 AND tl3_w4839  OR  tl3_w5025 )

Latch A's circuit again, 1606 px lower: open while `tl3_w4978` is high, when `tl3_w5156` takes
the data and `tl3_w5025` its inverse; `tl3_w5112` high clears it. **Its data is NOR 4's
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
| y 5103-5121 | `tl3_w5112` (clear) | from the west, under the metal x 3540 (no hole: `textmap.py 3522 5096 3560 5128 3`) |
| y 5146-5166 | `tl3_w5156` (output) | a stub on the node's box, as in latch A |

### The east column's two NOR units: traced

    tl3_e4243 = NOR(tl3_e4152, rcs_mv)        unit e3, y 4165-4335
    tl3_w4978 = NOR(tl3_e4152, tl3_e5114)     unit e5, y 4990-5160: latch B's enable

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
| e3 gate 1, y 4191-4209 | `tl3_e4152` | east to a pad with a contact (4148,4200) on **track A**, a metal x 4141-4155 that runs south to y 5008 (`follow.py 4148 4290 S`) with four more pads, (4146,4510), (4146,4681), (4146,4900), (4147,5005), each with a hole in the clean shot and a poly row leaving it (`textmap.py 4130 Y-14 4168 Y+14 3`). North of the pad it turns west along y 4152-4168 and north at x 4099-4111 (`follow.py 4148 4290 N`) as the thin metal of the Inventory. Drawn from y 4106 to y 5012 |
| e3 gate 2, y 4280-4300 | `rcs_mv` | east under track A (no hole) to a pad with a contact (4190,4288) on `tla`'s track x 4192 |
| e3 output, y 4232-4252 | `tl3_e4243` | east under both tracks (no hole: `textmap.py 4128 4184 4256 4304 3`) to a pad with a contact (4236,4246); its metal leaves east into `tl4`'s strip (it turns north at x 4323 and runs to y 2772: `follow.py 4270 4243 E`) |
| e5 gate 1, y 5016-5034 | `tl3_e4152` | east to the pad (4147,5005), where track A arrives from the north. **The net goes on** (found by the review): a metal arm leaves the pad west along y 4996-5008 to x ~4106 and runs south at x 4100-4112, beside the metal x 4148 and apart from it, to a pad with a contact (4104,5633), whose poly leaves east along y 5620-5645, not followed (`arm1.png`, `arm_s.png`, 5x; `textmap.py 4084 5612 4130 5656 3`). It passes over e5's node box (y 5050-5083) and over a boxed poly end at 4088-4112 x 5188-5216 where the row y ~5195-5207 ends: neither has a hole in the clean shot (`px.py col 4104 5090 5622 3 acid1b`, and at x 4108, 4112: green only for 3-6 px at y 5183-5186), so both are taken as pass-overs (assumed, tracing guide trap 22) |
| e5 output, y 5057-5077 | `tl3_w4978` | east to a pad with a contact (4147,5070) at the north end of a metal x 4142-4155 (`follow.py 4148 5090`: y 5064-5332), which crosses three rows without a hole (`textmap.py 4124 5098 4262 5130 3`, `4130 5186 4168 5252 3`) and ends on a contact (4148,5330) on the east pad of latch B's enable row (`textmap.py 4126 5300 4172 5352 3`). That row, y 5318-5342, is one poly from x 3550 to x 4132: no break and no other hole (`px.py row 5330 3560 4160 3 acid1b`) |
| e5 gate 2, y 5105-5123 | `tl3_e5114` | from the east, across the bus field under four tracks without a contact; out of the strip at x 4250 |

So latch B is open while `tl3_e4152` and `tl3_e5114` are both low. `tl3_e4152` is the east
column's distributed line (five gate pads on track A, and a sixth pad at (4104,5633)).

### Latch C (east column, y 4514-4970): traced

    tl3_e4537 = NOT tl3_e4635
    tl3_e4720 = NOT( tl3_e4635 AND tl3_e4152  OR  tl3_e4852 )
    tl3_e4852 = NOT( tl3_e4808  OR  tl3_e4152 AND tl3_e4537  OR  tl3_e4720 )

The circuit of latches A and B a third time, as a mirror image east of the east rail: open
while `tl3_e4152` is high, when `tl3_e4852` takes the data `tl3_e4635` and `tl3_e4720` its
inverse; `tl3_e4808` high clears it (`tl3_e4852` low). **Its enable is `tl3_e4152`, track A**:
both enable rows end on track A's pads (4146,4681) and (4146,4900). Latch B is open while
`tl3_e4152` and `tl3_e5114` are both low (`tl3_w4978`), so B and C are never open together.
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
| enable, rows y 4666-4684 and y 4882-4902 | `tl3_e4152` | each ends on a pad of track A: (4146,4681), (4146,4900) (run 5's contacts) |
| the upper node, y 4705-4736 | `tl3_e4720` | the poly on its box is a stub (rounded end at x ~4125, `lc_bf1.png`). It leaves by the plate: the thin metal x 3902-3914 (`follow.py 3908 4780`: (3914,4646)-(3907,4880)) from a contact (3909,4674) on the plate to a contact (3908,4877) on the pad of the lower unit's third gate (`tl3_e4675`, aliased) |
| clear, row y 4800-4817 | `tl3_e4808` | east under track A (no hole) to a pad with a contact (4190,4808), the north end of a metal x 4186-4199 on `rcs_mv`'s track (no metal between `rcs_mv`'s pad (4192,4743) and this one: `px.py col 4192 4290 4830 12 metal,metal1`: 160/144/88 at y 4770-4782; `lc_bf1.png`). The metal runs south to y 5896 and turns east out of the strip (`follow.py 4192 4870 S`: corner (4201,5896) E, on to (4629,5893); `textmap.py 4172 5874 4262 5916 3`: a plain corner, bare ground south and west of it, no hole). On the way it has **a second contact (4192,5373)** on a pad whose poly row y 5366-5376 runs west across the cluster's foot (`textmap.py 4170 5364 4216 5406 3`, `4100 5356 4262 5392 3`: ring, bright centre, green hole; the row passes under the metal arm x 4100-4112 of `tl3_e4152` without a hole): drawn to x 4124, not followed |
| output, row y 4843-4859 | `tl3_e4852` | east under track A and the clear's metal without a contact (`textmap.py 4120 4834 4252 4870 3`) to a pad with a contact (4234,4852), the south end of a metal x 4229-4243 (`follow.py 4238 4700`: (4234,4432)-(4235,4856); bare ground north of y 4440). Its north end has a contact (4236,4461) on a pad whose poly row y 4453-4466 runs west under two tracks without a contact (`textmap.py 4110 4440 4262 4482 3`) to the rail, where a gate lies under the rail at y 4453-4477 (the unit at y 4350-4514, not drawn): drawn to x 4118 |

Two wires of other nets drawn with it:

- **`tl3_e4152`'s pad (4146,4510)**: its row y 4496-4510 runs east under two tracks without a
  contact (`textmap.py 4126 4486 4254 4520 3`) and out of the strip at x 4250, where `tl4` has
  it as `tl4_w4501`, gate 2 of its three-input NOR `tl4_w4545`. One net (`@alias tl3_e4152
  tl4_w4501`; the geometry joins at x 4250).
- **`rcs_mv`'s track ends on a pad with a contact (4192,4743)** (`tla` had "bottom end not
  looked at"); the pad's poly leaves east along y 4736-4751 under the metal x 4229-4243 without
  a contact and crosses x 4250 (`textmap.py 4170 4722 4254 4762 3`). So `rcs_mv` comes from the
  east (the glossary already says: a poly that leaves the bus field at (4283,4745)).
- **`tl3_e4915`, a wire that only passes through** (found by review 7): a pad with a contact
  (4234,4918) on the track x 4236, 60 px below latch C's output pad and apart from it (bare
  ground y 4877-4892 in both metal shots). The pad's poly leaves east across x 4250 along
  y 4904-4925; a metal x 4229-4243 runs south from the contact to y 5766 and turns east out of
  the strip (`follow.py 4236 4990 S`: corner (4245,5770) E, on to (4411,5762)). No hole under it
  on the way and a plain corner (`textmap.py 4204 4868 4264 4940 3`, `4224 4930 4251 5790 3`
  filtered for green samples, `4216 5744 4264 5790 3`). Both ends are in `tl4`'s strip.

### The NOR units of the west column: traced

    tl3_w3765 = NOR(tl3_w3722, tl3_w3803)      NOR 1, y 3688-3872
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
| y 3755-3775 | `tl3_w3765` (NOR 1 output) | west out of the strip |
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
    tl3_w4243 = NOR(tl3_w4200, tl3_w4290, tl3_w3803)   lower unit

A set/reset latch: `tl3_w4112` high makes `tl3_w3803` low; `tl3_w4200` or `tl3_w4290` high
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
| y 4191-4209 | `tl3_w4200` (set) | west out of the strip |
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

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tl3_w3333` | poly | (3533, 3324-3342) | in | data of latch A |
| `tl3_w3419` | poly | (3533, 3409-3429) | out | latch A's inverted output |
| `tl3_w3506` | poly | (3533, 3497-3515) | in | clear of latch A |
| `tl3_w3373` | poly pad | (3606,2985) | ? | enable of latch A; a poly row y 2955-2975 goes on east from the pad, not drawn |
| `tl3_w3722` | poly | (3533, 3712-3732) | in | NOR 1 gate 1 |
| `tl3_w3765` | poly | (3533, 3755-3775) | out | NOR 1 output |
| `tl3_w3896` | poly | (3533, 3886-3906) | in | NOR 2 gate 1 |
| `tl3_w3939` | poly | (3533, 3929-3949) | out | NOR 2 output |
| `tl3_w3982` | poly | (3533, 3972-3992) | in | NOR 2 gate 2 |
| `tl3_w4763` | poly | (3533, 4753-4773) | in | NOR 4 gate 2 |
| `tl3_w4112` | poly | (3533, 4101-4120) | in | the pair: gate of the upper unit |
| `tl3_w4200` | poly | (3533, 4191-4209) | in | the pair: lower unit gate 1 |
| `tl3_w4290` | poly | (3533, 4281-4299) | in | the pair: lower unit gate 2 |
| `tl3_w4373` | poly | (3533, 4363-4383) | out | the inverter's output |
| `tl3_w4414` | poly | (3533, 4405-4423) | in | the inverter's input |
| `tl3_w4503` | poly | (3533, 4493-4513) | in | NOR 3 gate 1 |
| `tl3_w4546` | poly | (3533, 4536-4556) | out | NOR 3 output |
| `tl3_w5025` | poly | (3533, 5015-5035) | out | latch B's inverted output |
| `tl3_w5112` | poly | (3533, 5103-5121) | in | clear of latch B |
| `tl3_e4243` | metal | (4250, 4235-4255) | out | e3's output, on east into `tl4`'s strip |
| `tl3_e5114` | poly | (4250, 5105-5123) | in | e5's gate 2, from the east |
| `tl3_e4152` | metal | (4105,4106) | ? | the thin metal x 4099-4111: drawn end; it goes on north |
| `tl3_e4152` | poly | (4160, 5620-5645) | ? | the poly of its south pad (4104,5633): drawn end; it goes on east |
| `tl3_e4635` | poly | (4250, 4627-4642) | in | latch C's data, from the east |
| `tl3_e4808` | metal | (4250, 5889-5901) | in | latch C's clear: the metal x 4192 from the pad (4190,4808), east out of the strip along y 5895 |
| `tl3_e4808` | poly | (4124, 5366-5377) | ? | the row of the clear metal's second pad (4192,5373): drawn end, it goes on west across the foot |
| `tl3_e4852` | poly | (4118, 4453-4466) | out | latch C's output, the row of the pad (4236,4461): drawn end, it goes on west under the rail as a gate of the unit at y 4350-4514 |
| `tl3_e4152` | poly | (4250, 4496-4510) | ? | the row of track A's pad (4146,4510), on east: `tl4`'s `tl4_w4501` |
| `rcs_mv` | poly | (4250, 4736-4751) | in | the poly of the pad (4192,4743) at the south end of `rcs_mv`'s track, from the east |
| `tl3_e4915` | poly | (4250, 4904-4925) | ? | the poly of the pad (4234,4918), on east |
| `tl3_e4915` | metal | (4250, 5760-5772) | ? | the metal x 4236 from that pad, east out of the strip along y 5766 |
| `tl3_tm3955` | metal | (3955,4500) and (3955,4960) | ? | the thin metal x 3948-3962: drawn ends, it goes on north and south |
| `vss` | metal | x 3645-3695, y 5330 | - | west rail, drawn to here |

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

1. **Changes a connection.** `tl3_e4152` does not end at the pad (4147,5005): a metal arm goes
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
   out of the strip, no other contact. Drawn as `tl3_e4915`.

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
(`tl3_tm3955` apart from `tl3_e4537`; the new net `tl3_e4915`).

Round 1: two findings that change a connection, fixed.

**Round 2, fix check** (2026-11-18 15:34 +0000, a fresh Fable 5.2 agent, 8 images in
`cache/scratch/tl3/review-8/`; changes since b5c7392). Told what changed and to test: its own
judgement of the spot (3955,4541) against real contacts of thin metals on pads, the master's
box under thin W and a certain pass-over; `tl3_e4915`'s pad, its separation from the output pad,
the metal's whole run south, the corner, where the pad's poly leaves; anything disturbed; both
`sameconn.py` runs. It found both changes right. The spot: the metal shots do not decide it (a
centre at full brightness, but between two straight bars along the poly row's edges, not in a
round ring, and the metal keeps its 13 px width); in the clean shot a grey band 4 px high
(y 4540-4543) across the box, red minus green 0-6, no pits, as in the master's boxes (-3..10 and
5-20), where real contact holes are round, about 8 px, red minus green -5..-16: a pass-over.
`tl3_e4915`: the pad closed west, north and south, its poly on east past x 4250 along
y 4903-4928; bare ground y 4862-4898 between it and the output pad in both metal shots and no
poly there in either stripped shot; uniform poly, no hole and no widening at every row the
metal crosses (4x views of y 5040-5680); a plain corner. Not checked: that a contact would
short two outputs (it rests on the undrawn end pads; (3930,3616) confirmed as a contact).
`tools/t.sh tl3 sameconn.py b5c7392` and `.venv/bin/python tools/sameconn.py b5c7392` show only
the intended differences (`tl3_tm3955` apart from `tl3_e4537`; the new net `tl3_e4915`).

Round 2: no findings.

## Not done

- Next, in this order: the east column's rail units (Inventory, run 6 survey): y 4350-4514 first
  (latch C's output is its lower gate; resume from `cache/scratch/tl3/survey.md` if it is on
  your machine, else from the Inventory row), then y 3440-3610 and 3660-3830, y 5190-5300, the
  top unit E1 (read, not drawn); the foot of the cluster (y 5260-5560).
- The thin metal x 3948-3962 north of y 4500 (to its pad (3930,3616)) and south of y 4960 (to its
  pad (3953,5459), whose poly leaves west along y ~5450-5464): not drawn; `follow.py`'s contact
  candidates on it are not read (Ambiguity 6). Draw it with the unit at y 3440-3610.
- `tl3_e4915`'s two ends east of x 4250 are `tl4`'s.
- `tl3_e4808`'s row y 5366-5376 west of x 4124 (the clear of latch C: where it comes from or
  goes to in the foot); the clear's metal east of (4250,5895) is `tl4`'s. `tl3_e4635` and
  `rcs_mv`'s poly east of x 4250 are `tl4`'s.

- A box under the VCC rail, x 3825-3872, y 5192-5258, contact near (3845,5222), with a strip
  east under a plate east of the rail (review of latch B): an east-column load's VCC end.
- What latch B's enable row y 5318-5342 gates on its way (it lies over unread areas at
  x 3560-3640 and 3710-3815, Inventory).
- The thin metal x 4099-4111 north of y 4106 and its contacts (`tl3_e4152`'s source). (The rows
  of track A's pads at y 4510, 4681 and 4900 are drawn since run 6: `tl4`'s row and latch C's
  two enable rows.)
- Where the true outputs of latch A and latch B are taken (`tl3_w3550`, `tl3_w5156` end in
  stubs; only the inverted outputs leave west).
- Where the seven rows of the pair, the inverter and NOR 3 go west of x 3533 is `tl2`'s.
- The poly row y 2955-2975 east from the pad (3606,2985): `tl3_w3373`'s other end
  (towards E1's load plate at x 3875-3935; not followed).
- The west rail south of y 5330, and the metal north of the link (review round 1: wider
  metal x ~3648-3762 above y 2598, a supply feed, not drawn); the VCC rail's top (y 2918) is `tla`'s.
- The VCC boxes of NOR 1 and NOR 4 run on south of the cell's box with more contacts (review:
  to about y 3880 with a contact near (3845,3840); y 4700-4810): not drawn. The inverter's VCC
  box has more contact marks than the one drawn.
- The west rail is drawn to y 5330 from low-zoom views; its contacts between the drawn boxes are not read.
- The rows of latch A west of x 3533 are `tl2`'s.
