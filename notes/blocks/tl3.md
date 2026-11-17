# tl3: top-left random logic, strip 3 (x 3533-4250, y 2500-6350)

Trace: `trace/tl3.txt` (`@requires tl1`, which requires `tla`). Views: `cache/scratch/tl3/`.
Started 2026-11-17 16:52 -0600 (Matt Godbolt's second session; the first holds `tl2`).

The strip holds the **middle cluster** of the row counter's step logic (`notes/blocks/tla.md`
names it: "the same construction 1042 px east"), the poly rows above it and the bus rows
below it. `tla` drew three things in it: the unit that makes `rcs_in1` (4081,4072), the
inverter `rcs_mu` (4050,3374) and the unit `rcs_mn3852` (4081,3852), with the VCC rail
x 3824-3868 and the east VSS rail x 3992-4041.

## Status

Traced, extracting (20 transistors of its own, 0 errors), all in the west column:

- **latch A, y 3212-3652**, by placing `tl1`'s two unit cells, with its rows, its two thin
  metals and the cluster's west rail (merged 2026-11-17, db5ab84);
- **three NOR units** (cell `tl3_nor`, 3 transistors each): NOR 1 (y 3688-3872), NOR 2
  (y 3862-4046), NOR 4 (y 4643-4827), with their rows and two metals (2026-11-17 17:16 -0600).

Everything else in the strip is surveyed only (Inventory).

## Inventory

Survey: `sv_top.png`, `sv_bot.png` (0.68x, metal and clean shot, all traces);
`tools/t.sh tl3 railprof.py 3992 4041 2900 5340` and `3645 3690 3180 3720`.

| Where | What | State |
|---|---|---|
| y 2580-2900 | horizontal poly rows above the cluster (`r9m`'s and `tla`'s lines cross here) | not traced here |
| x 3645-3695, y 2595 to beyond 4060 | **west rail: VSS**. One metal with the east VSS rail (x 3995-4045) through a wide link along y 2595-2648 (`top_m.png`, 2.2x metal; `follow.py 3667 3400 N`: corners (3680,2638) E, (4028,2638) S). The mirror of `tla`'s R1 | drawn to y 4060 |
| x 3575-3880, y 3212-3652 | latch A (below) | traced |
| x 3575-3880, y 3688-4046 and 4643-4827 | NOR 1, NOR 2, NOR 4 (below) | traced |
| x 3575-3880, y 4031-4653 | by `findcell` (clean shot, `tla`'s `in2` unit 2535 5120 2790 5290): four NOR units at 1041 with dy -1432, -1259, -651, -477 (scores 0.80-0.83), and `tl1`'s inverter (2535 4215 2835 4345) at 1041,130 (0.76; y 4345-4475) | not checked, not drawn |
| x 3575-3880, y 4818-5258 | by `findcell`: `tl1_ua` and `tl1_ub` again at 1042,478 (0.80, 0.82): a second latch | not checked, not drawn |
| east column (east of the rail x 3992-4041) | by `findcell`: `tla`'s `in3` unit (2840 5120 3070 5290) at 1041,-955 (0.91; y 4165-4335) and 1042,-130 (0.85; y 4990-5160); `tla`'s `in1` unit of this cluster (3820 4040 4120 4150) at 1,1129 (0.92), 0,-1084 (0.83), and turned at 0,-394, 0,-698; mirrored hits of the west cells at y 4514-4954 | not checked, not drawn |
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

### The NOR units of the west column: traced (three of four)

    tl3_w3765 = NOR(tl3_w3722, tl3_w3803)      NOR 1, y 3688-3872
    tl3_w3939 = NOR(tl3_w3896, tl3_w3982)      NOR 2, y 3862-4046
    tl3_w4720 = NOR(tl3_w3803, tl3_w4763)      NOR 4, y 4643-4827

The unit is `tla`'s `in2` unit / `tl1`'s NOR (`tl1_w3636`) again: a diffusion column west of
the rail (x 3591-3633) between two arms onto the rail's VSS boxes, two gate rows across it,
the node between them with a buried contact (concentric box) to the output row, and the load
east of the rail (strip under a plate x 3763-3816 to a VCC box under the VCC rail; tail and
buried-contact tie at the plate's lower corner). Cell `tl3_nor`, master NOR 1: `tl1`'s
geometry moved by 1042,130; copies at 0,174 and 0,955.

- `findcell` (clean shot, `tl1`'s NOR 2535 3558 2842 3742): 1042,130 (0.73), 1041,304
  (0.79), 1042,911 (0.74), 1042,1085 (0.73).
- Overlays `n12_ov.png`, `n34_ov.png` (1.42x, metal and clean shot): every outline on its
  feature in all four units. NOR 1 at 4x in both stripped shots: `n1_w.png` (column, gates,
  box, node strip under the rail), `n1_e.png` (load: the strip's edges show as lines across
  the plate at y ~3760 and ~3790 in the chip-2 stripped shot, so the strip is drawn 24 wide
  where `tl1`'s is 17; the tail x 3735-3752 and the plate's tab x 3735-3765, y 3805-3830).
- Metal overlay `n34_mov.png` (2.4x): the rail contacts (3664,4633), (3664,4807), the VCC
  contacts, the pads.
- **The fourth unit (y 4469-4653, at 0,781) is a copy too and is not placed.** Its top arm
  lands on the diffusion under the rail at y 4433-4486 (`railprof.py 3645 3690 4330 4500`:
  diffusion y 4330-4409, gate y 4410-4432, diffusion y 4433-4486), which belongs to the
  unit above (`findcell`: `tl1`'s rail-gate inverter at 1041,130) and is not read: whether
  that diffusion is a VSS box or the inverter's node decides what the unit is. Its rows:
  gate 1 y 4493-4513 and output y 4536-4556 from the west, gate 2 y 4579-4599 from the pad
  (3540,4590).

Rows and wiring (`n12_rows.png`, `n34_rows.png`, 3.3x in three shots; `trk_both.png`,
`trk4920.png`, 4x in four shots):

| Row | Net | Where it goes |
|---|---|---|
| y 3712-3732 | `tl3_w3722` (NOR 1 gate 1) | west out of the strip |
| y 3755-3775 | `tl3_w3765` (NOR 1 output) | west out of the strip |
| y 3798-3818 | `tl3_w3803` (NOR 1 gate 2) | pad with a contact (3540,3803) at the north end of a metal x 3533-3548 (`follow.py 3541 3850`: (3543,3806)-(3542,4596)). The metal has two more contacts on pads: (3540,4068), whose row goes east into the units not read yet, and (3540,4590) |
| the pad (3540,4590) | `tl3_w3803` | its poly is an L: south along x 3533-3555 and east along y 4667-4687 as **NOR 4's gate 1**; a row y 4579-4599 also goes east from the pad (gate 2 of the unit not placed) |
| y 3886-3906 | `tl3_w3896` (NOR 2 gate 1) | west under the metal x 3540 (no pad) out of the strip, to a pad (3497,3890) |
| y 3929-3949 | `tl3_w3939` (NOR 2 output) | west out of the strip |
| y 3972-3992 | `tl3_w3982` (NOR 2 gate 2) | west under the metal x 3540 (no pad) out of the strip, to a pad (3497,3978) |
| y 4710-4730 | `tl3_w4720` (NOR 4 output) | pad with a contact (3540,4720) (`textmap.py 3480 4690 3570 4750`: ring, bright centre, green hole); a metal south from it (`follow.py 3540 4718 S`) to a pad with a contact (3540,4912), whose poly goes on east along y 4930-4948: the data row of the unit below (`findcell`: `tl1_ua` again), not drawn |
| y 4753-4773 | `tl3_w4763` (NOR 4 gate 2) | west out of the strip |

So `tl3_w3803` gates NOR 1 and NOR 4 (and the unit between), and NOR 4's output is the data
of the second latch, if that unit is the copy `findcell` says it is (believed).

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
| `tl3_w3803` | poly pad | (3540,4068) | ? | a pad of the metal x 3540; its row goes east into units not read |
| `tl3_w4720` | poly pad | (3540,4912) | out | NOR 4's output; the pad's poly goes on east along y 4930-4948, not drawn |
| `vss` | metal | x 3645-3695, y 4850 | - | west rail, drawn to here |

## Ambiguities

1. The two cross-couplings of latch A rest on the load plates' ties, `?` items in `tl1`'s
   cells (AMB-026). Not read again here; in this cluster the ties are in the open (no thin
   W), so the chip-2 shots at 6x may settle them for all copies: (3715-3745, 3375-3400) and
   (3713-3737, 3492-3522).
2. `tl3_w3550`'s poly on the lower unit's box was read as a stub from one 3.5x view
   (`la_rows.png`): a rounded end at x ~3570 with nothing under the metal x 3540 at
   y 3540-3560.

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

## Not done

- Everything in the Inventory marked not drawn. Next, in this order: the units at y 4031-4475
  of the west column (the row from the pad (3540,4068) leads in; `findcell` has `tl1`'s
  inverter at y 4345-4475) and with them the third NOR (y 4469-4653, see Logic); the second
  latch (y 4818-5258), whose data row starts at the pad (3540,4912); the east column's units by the `findcell` hits; the top
  unit E1 (read, not drawn).
- The poly row y 2955-2975 east from the pad (3606,2985): `tl3_w3373`'s other end
  (towards E1's load plate at x 3875-3935; not followed).
- The west rail south of y 4850, and the metal north of the link (review round 1: wider
  metal x ~3648-3762 above y 2598, a supply feed, not drawn); the VCC rail's top (y 2918) is `tla`'s.
- The west rail is drawn to y 4850 from low-zoom views; its contacts between the drawn boxes are not read.
- The rows of latch A west of x 3533 are `tl2`'s.
