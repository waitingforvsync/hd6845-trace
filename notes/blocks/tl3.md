# tl3: top-left random logic, strip 3 (x 3533-4250, y 2500-6350)

Trace: `trace/tl3.txt` (`@requires tl1`, which requires `tla`). Views: `cache/scratch/tl3/`.
Started 2026-11-17 16:52 -0600 (Matt Godbolt's second session; the first holds `tl2`).

The strip holds the **middle cluster** of the row counter's step logic (`notes/blocks/tla.md`
names it: "the same construction 1042 px east"), the poly rows above it and the bus rows
below it. `tla` drew three things in it: the unit that makes `rcs_in1` (4081,4072), the
inverter `rcs_mu` (4050,3374) and the unit `rcs_mn3852` (4081,3852), with the VCC rail
x 3824-3868 and the east VSS rail x 3992-4041.

## Status

One piece traced, extracting (11 transistors of its own, 0 errors): **latch A in the west
column, y 3212-3652**, by placing `tl1`'s two unit cells, with its rows, its two thin metals
and the cluster's west rail. Everything else in the strip is surveyed only (Inventory).

## Inventory

Survey: `sv_top.png`, `sv_bot.png` (0.68x, metal and clean shot, all traces);
`tools/t.sh tl3 railprof.py 3992 4041 2900 5340` and `3645 3690 3180 3720`.

| Where | What | State |
|---|---|---|
| y 2580-2900 | horizontal poly rows above the cluster (`r9m`'s and `tla`'s lines cross here) | not traced here |
| x 3645-3695, y 2595 to beyond 4060 | **west rail: VSS**. One metal with the east VSS rail (x 3995-4045) through a wide link along y 2595-2648 (`top_m.png`, 2.2x metal; `follow.py 3667 3400 N`: corners (3680,2638) E, (4028,2638) S). The mirror of `tla`'s R1 | drawn to y 4060 |
| x 3575-3880, y 3212-3652 | latch A (below) | traced |
| x 3575-3880, y 3688-4813 | by `findcell` (clean shot, `tla`'s `in2` unit 2535 5120 2790 5290): four NOR units at 1041 with dy -1432, -1259, -651, -477 (scores 0.80-0.83), and `tl1`'s inverter (2535 4215 2835 4345) at 1041,130 (0.76; y 4345-4475) | not checked, not drawn |
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

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tl3_w3333` | poly | (3533, 3324-3342) | in | data of latch A |
| `tl3_w3419` | poly | (3533, 3409-3429) | out | latch A's inverted output |
| `tl3_w3506` | poly | (3533, 3497-3515) | in | clear of latch A |
| `tl3_w3373` | poly pad | (3606,2985) | ? | enable of latch A; a poly row y 2955-2975 goes on east from the pad, not drawn |
| `vss` | metal | x 3645-3695, y 4060 | - | west rail, drawn to here |

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

- Everything in the Inventory marked not drawn. Next, in this order: the four NOR units and
  the inverter of the west column (y 3688-4813) by `@inst`/copy after an overlay check each;
  the second latch (y 4818-5258); the east column's units by the `findcell` hits; the top
  unit E1 (read, not drawn).
- The poly row y 2955-2975 east from the pad (3606,2985): `tl3_w3373`'s other end
  (towards E1's load plate at x 3875-3935; not followed).
- The west rail south of y 4060, and the metal north of the link (review round 1: wider
  metal x ~3648-3762 above y 2598, a supply feed, not drawn); the VCC rail's top (y 2918) is `tla`'s.
- A draft of the four NOR units' cell is in `cache/scratch/tl3/draft-nor.txt` (`tl1`'s NOR
  geometry moved by 1042,130; `n12_q.png` shows units 1 and 2 where expected): not overlaid yet.
- The rows of latch A west of x 3533 are `tl2`'s.
