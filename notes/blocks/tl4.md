# tl4: top-left random logic, the fourth strip (x 4250-4967, y 2500-6350)

Package `tl4` (part 4 of 6 of the top-left logic). Trace: `trace/tl4.txt`. Views:
`cache/scratch/tl4/`. The strip holds most of the vertical control's **right cluster**
(`tla`'s name for it): a bus field of vertical metals (x 4250-4680), a gate column on a rail
RA (x 4728-4775), loads between RA and a second rail RB (x 4905-4950).

## Status

2026-11-17 23:31 -0600. **Partial: eight units.** Traced in the fifth run: the three units
below the pair, y 4990-5450 (7 transistors, 36 in all): a two-input NOR (`tl4_w5068`), an
inverter (`tl4_w4025`: **the upper latch's data, now identified**) and a strong inverter on the
upper latch's output (`tl4_w5455`). No merged equation changed.
Before that: **five units.** The fifth, traced in the fourth run, is a
cross-coupled pair at y 4645-5000 (9 transistors, 29 in all): `tl4_w4686` and `tl4_w4850` below.
Before that: **four units** (the fourth, a three-input NOR at y 4410-4645,
`tl4_w4545` = NOR(`tla_w3417`, `tl4_w4501`, `tl4_w4590`), traced in the third run: 4 transistors, 20 in all).
Before that: **three units.** The gate column repeats the first cluster's west column
(`tl1`'s units on R1/R2) 2125 px east and 434 px north (the top unit 520 px north). Traced:
the NOR at the top (y 3012-3222), the inverter above the latch (y 3781-3911) and the latch
(y 3906-4390): 16 transistors, each unit with the rows that feed it, read here. Full
extraction: 0 errors, 0 warnings.

```
tl4_w3113 = NOR(tl4_w3070, tl4_w3178)                             firm
tl4_w3808 = NOT tl4_w3850                                         marked: the load's tie (`?`, as in tl1)
tl4_w3928 = NOT tl4_w4025                                         firm
tl4_w4113 = NOT( tl4_w4025 AND tl4_w4068  OR  tl4_w4243 )         marked: the two load ties
tl4_w4243 = NOT( tl4_w4198  OR  tl4_w4068 AND tl4_w3928  OR  tl4_w4113 )   marked: the two load ties
tl4_w4545 = NOR( tla_w3417, tl4_w4501, tl4_w4590 )                marked: the load's tie
tl4_w4686 = NOT( tl4_w4718 AND tl4_w4590  OR  tl4_w4850 )         marked: the lower load's tie carries tl4_w4850 to this gate
tl4_w4850 = NOT( tl4_w4198  OR  tl4_w4545  OR  tl4_w4686 )        marked: the load ties; tl4_w4545 on two gates in series (one join `?`)tl4_w5068 = NOR( tl4_w4545, tl4_w4850 )                           marked: the load's tie
tl4_w4025 = NOT tl4_w5068                                         marked: the load's tie (`?`, as in the inverter above the latch)
tl4_w5455 = NOT tl4_w4243                                         marked: the load's tie
```

So the chain is: the three-input NOR `tl4_w4545` and the set/reset pair's `tl4_w4850` are OR-ed
(`tl4_w5068` and its inverter) into the data `tl4_w4025` of the latch at y 3906-4390; the
latch's output `tl4_w4243` is inverted by a strong inverter onto a poly row at y 5445-5465
(`tl4_w5455`), which crosses the whole strip and is not followed.

The pair at y 4645-5000 is a set/reset latch: `tl4_w4718` AND `tl4_w4590` both high pull
`tl4_w4686` low, which lets `tl4_w4850` rise; `tl4_w4198` (the clear of the latch above as well)
or `tl4_w4545` pull `tl4_w4850` low again. `tl4_w4850` leaves south on the
track x 4581; `tl4_w4686` goes no further than the pair (its thin metal ends on the lower gate's pad).

A latch: open while `tl4_w4068` is high, it takes `tl4_w4025`; `tl4_w4198` high forces
`tl4_w4243` low. The same build as the two latches in front of `rcs_e4` and the third latch
of the small cluster (`notes/blocks/tl1.md`). **Unlike in the first cluster, the inverter
above the latch does not feed the latch's data here**: its output `tl4_w3808` leaves north on
the metal x 4496, and the latch's data `tl4_w4025` comes from the south on the metal x 4452.
(Fifth run: that metal comes from the inverter at y 5175-5312, so the data is `tl4_w4545` OR `tl4_w4850`; the output `tl4_w4243` goes to the strong inverter at y 5297-5465.) What the other signals are is not known: their tracks are not followed yet.

## Inventory

| Where | What |
|---|---|
| x 4250-4680, y 2700-5800 | bus field: about ten vertical metals, poly rows east into the column, pads. Not drawn, except the pieces at the latch |
| x 4290-4967, y 3012-3222 | **the NOR** (`tl1`'s NOR at 2125,-520, findcell 0.77) |
| x 4690-4967, y 3220-3780 | units not matched by `tl1`'s first latch (findcell under 0.5). Not drawn |
| x 4400-4967, y 3781-3911 | **the inverter** (`tl1`'s inverter at 2125,-434, findcell 0.74) |
| x 4665-4967, y 3906-4390 | **the latch: this piece** |
| x 4250-4967, y 4410-4645 | **the three-input NOR** (hand-traced; no cell matches) |
| x 4347-4967, y 4645-5000 | **the cross-coupled pair** (hand-traced; no cell matches) |
| x 4560-4967, y 4990-5170 | **the two-input NOR** (hand-traced) |
| x 4437-4967, y 5175-5312 | **the inverter** onto the latch's data (the inverter at y 3781-3911 moved by 1,1389: `tl1`'s inverter at 2126,955, findcell 0.75) |
| x 4520-4967, y 5297-5465 | **the strong inverter** on the latch's output (hand-traced) |
| y 5445-5900 | a field of poly rows across RA and RB (pitch about 45), dark specks on RA between them. Not drawn |
| y 2500-2960 | rows and tracks north of the cluster (`r9m`'s lines along y 2560-2640) |
| y 5400-6350 | rows under the foot; the `c4l0`..`c4l3` rows y 6140-6270 |

## Logic

### The latch at y 3906-4390 (traced 2026-11-17: cells `tl1_ua`, `tl1_ub` at 2125,-434)

`tools/findcell.py` on the clean shot, restricted to 4600,2950:4967,5450: the master rectangles
2540-2842 x 4340-4590 and 2540-2842 x 4590-4800 both recur at 2125,-434 (scores 0.75, 0.80).
The two cells laid over the photos sit on the features: `b1.png`, `b2.png` (clean shot, 4x),
`b3.png` (metal, 2.5x): VSS boxes and contacts on RA, the gate bands, the two plates, the VCC
boxes under RB, the thin metal x 4682-4698 with its pads (4687,3925) and (4680,4333).

What the copy has of its own, read here:
- **Rows from the west** (`b4.png` clean 2.7x, `b5.png` metal and clean 2.2x with the trace).
  Each ends on a pad with a contact (ring in the metal shot, green centre in the clean shot) on
  a vertical metal:
  - `tl4_w4025`, row y 4016-4034, pad (4455,4025), metal x 4452: gate 1 of the three-input gate
    and the inverter's gate (the data).
  - `tl4_w4068`, metal x 4625 with two pads (4625,4068) and (4625,4285) and a row from each
    (y 4058-4076, y 4275-4293): the second series gate of both units (the enable). The metal
    between the pads is in view on `b3.png` and `b5.png`.
  - `tl4_w4198`, row y 4190-4208, pad (4533,4198), metal x 4537: the single pull-down west of
    the rail in the lower unit (the clear).
  - `tl4_w4243`, row y 4234-4252 from the lower unit's node box west to a pad (4490,4243),
    metal x 4494: the latch's output.
  - The box poly of the upper unit's node (y 4103-4123) is a stub with a closed end at x 4657,
    as in the master.
  The rows pass under the metals x 4537 and x 4575-4590 at constant width, without pads.
- **Thin metal x 4860-4875** between pads with contacts (4866,4064) and (4866,4268)
  (`textmap.py 4846 4040 4890 4084 4` and `4846 4250 4890 4290 4`: bright centre B-D inside a
  dark ring in both metal shots, a green hole in the clean shot; `follow.py 4867 4150 N/S` ends
  at y 4040 and y 4272): `tl4_w4113`, the upper unit's plate to the third pull-down's gate.
- **VSS box below the stack** (4725-4782, 4344-4390) with a contact (4745,4368) on RA
  (`textmap.py 4712 4338 4796 4410 4`: bright centre in a dark ring, both metal shots).
- **The VCC box's contact**: one elongated ring on RB, x 4915-4945, y 3995-4200 (`b3.png`; review round 1).
- There is no thin metal at the place of the first cluster's thin metal W (x 4814-4828): bare
  ground between RA and the thin metal x 4867 (`b3.png`).

The rails are drawn only where looked at (y 3880-4392) and are **named from structure**: RA
carries the pull-downs' boxes (`vss`), RB the loads' boxes (`vcc`). Neither is followed to a
supply yet.

### The NOR at y 3012-3222 and the inverter at y 3781-3911 (traced 2026-11-17, second run)

Both are `tl1`'s geometry (its NOR at 2540-2842 x 3558-3742, its inverter at 2535-2835 x
4215-4345; plain items there, not cells), moved by 2125,-520 and 2125,-434 and laid over the
clean shot at 3.8x (`n1.png`, `i1.png`): columns, node boxes, gate bands, strips, plates, tie
boxes and VCC boxes sit on the features. Read here:
- **NOR.** The VSS box above the column (4722-4777, 3012-3062) with a contact (4742,3036) and
  the one below with (4747,3202) (`textmap.py 4730 3014 4770 3046 4`). Rows (`n2.png`,
  `n3.png`: clean and metal, 2.7x): gate 1 `tl4_w3070`, y 3062-3082, from a pad (4320,3070) on
  the metal x 4318; gate 2 `tl4_w3178`, y 3148-3168, from a pad (4413,3178) at the north end
  of the metal x 4410; output `tl4_w3113`, the node's box poly west along y 3105-3125 to a pad
  (4410,3113) at the south end of a metal x 4408. Between the two pads on x 4410 there is no
  metal (y 3130-3160 bare in both views; `follow.py 4414 3140 S`: no metal).
- **Inverter.** Output `tl4_w3808`: the node box's poly west along y 3797-3815 to a pad
  (4495,3808) at the south end of the metal x 4496. Gate `tl4_w3850`: row y 3841-3859 across
  RA from a pad (4455,3850), whose metal runs west along y 3852 and turns south at x 4402-4422
  (`i2.png`, `i3.png`). One VCC contact, a ring with a bright centre at (4926,3838)
  (`textmap.py 4908 3800 4952 3912 4`); `tl1`'s second contact has no counterpart here. The
  load's tie is `tl1`'s `?` item.
- The rows pass under the metals x 4537, 4580 and 4625 at constant width without pads.

### The three-input NOR at y 4410-4645 (traced 2026-11-17, third run)

Not a copy of anything in the first cluster (`findcell`: `tla`'s unit at 2124,-651 scores 0.61;
the first cluster has `tla`'s wide NOR at the matching place, `c1.png`). Read by hand on
`u2.png` (clean), `u3.png` (chip-2 stripped), `u4.png` (chip-2 metal), `u5.png` (chip-1
stripped), all 3.9x of 4648-4968 x 4395-4645; the tie on `tie1.png`, `tie2.png` (9x, four
shots); the rows on `r1.png` (2.7x of 4250-4700 x 4400-4650, stripped and metal); overlays
`oa1.png`, `oa2.png` (3.3x).

- **The stack is a column of diffusion in the open west of RA** (x 4677-4716, y 4420-4628),
  crossed by three poly rows from the bus field (orange in the stripped shot, each ending at
  x 4722): y 4452-4470, y 4492-4512, y 4578-4598.
- **The output node is a ring of diffusion**: the column's top (above gate 1), a strip east
  under RA (y 4420-4440), a leg south in the open (x 4808-4830), and a band back west under RA
  (y 4537-4558) onto the column between gates 2 and 3. In the metal shot the ring is the space
  between two nested outlines (outer 4675-4832 x 4418-4540, inner 4715-4805 x 4440-4535).
- **VSS**: inside the ring, under RA, a box (4735-4790, 4470-4518) with a contact (4757,4495)
  (ring with a bright centre in the metal shot, specks in the clean shot), joined to the
  column between gates 1 and 2 by a neck (y 4474-4488: two edge lines running from the column
  into the box's west side in the clean shot). Below gate 3 the column's foot (y 4603-4628)
  runs east onto a second VSS box under RA (4728-4777, 4605-4645, contact (4745,4627)).
  So each of the three gates lies between the node and VSS: a NOR.
- **The node's wire**: a buried contact on the column's middle (heavy box 4675-4702 x
  4530-4562, concentric rings in the clean shot), poly west along y 4537-4558 to a pad with a
  contact (4620,4545), and the metal x 4626 south from the pad (`follow.py 4625 4620 S`: ends
  (4623,4900); `N`: ends (4623,4544)). Its south end is not read yet.
- **Load**: plate x 4845-4900, y 4520-4610 over a strip y 4543-4566 from the leg's foot to a
  VCC box under RB (4908-4962, 4480-4608; one long ring x 4915-4940, y 4495-4590). The plate's
  tail runs west along y 4590-4612 onto a heavy box (4812-4838, 4588-4615) at the end of a tail
  of the node (x 4814-4836): the tie, drawn `?` as in the other loads.
- **Inputs**:
  - gate 1 is `tla_w3417`: `tla`'s row y 4452-4470 from its pad (4410,4460), which `tla` drew
    to x 4520, runs on east without a break to the column (`r1.png`). **Input identified**: the
    selector's output (`notes/blocks/tla.md`) now has a destination; `tla`'s equation is unchanged.
  - gate 2, `tl4_w4501`: a row y 4492-4512 from the west, across the whole bus field under every
    track without a pad, and out of the strip at x 4250 (`r1.png`).
  - gate 3, `tl4_w4590`: a row y 4578-4598 from a pad with a contact (4364,4590) on the track
    x 4362. `follow.py 4362 4500 N/S`: one metal from y 2810 to y 5682, with contact candidates
    (4364,3014), (4362,4607), (4367,4779), (4366,5125). Only a stub of it is drawn.
- **RA is wider from y 4392 south**: x 4732-4786 (`px.py row 4405 4715 4800 3 metal,metal1`),
  against x 4734-4776 at y 4300.

### The cross-coupled pair at y 4645-5000 (traced 2026-11-17, fourth run)

Not a copy (`findcell` under 0.6). Read by hand on `b_metal.png`, `b_acid.png`, `b_acid1b.png`
(3.3x of 4590-4970 x 4630-4920), `c_*.png`, `d_*.png`, `e_*.png` (5.6x), `f_*.png` (5x of
4775-4970 x 4730-4930), `g1.png`, `g2.png` (8x of 4778-4862 x 4692-4812, four shots), `h_*.png`
(4x of 4640-4970 x 4850-5020), `j1.png`, `j2.png` (6x of 4596-4706 x 4866-4996, four shots),
`t2a.png`, `t2b.png` (9x, the lower tie), `w_acid.png`, `w_metal.png` (2.8x, the rows in the bus
field), `k1.png`; overlays `ob1.png`, `ob2.png` (3.6x), `ob3.png` (2.8x).

- **The stack is one wide diffusion, x 4677-4764**, in the open west of RA and on under RA
  without an edge between: `px.py row 4740 4636 4736 4 acid1b,acid` has no dark value between the
  column (about 90 82 52) and the tan under RA (from x 4728), against the unit above, where
  `row 4525` has the edge (38 26 22) at x 4712-4716 and pink under RA. The same at y 4785,
  y 4910 and y 4955. So each row is one gate about 85 px wide. Down the stack
  (`px.py col 4745 4640 4925 5 acid1b`: tan = diffusion, salmon = gate): node `tl4_w4686`
  (y 4668-4706), gate 1 (y 4708-4728), middle, gate 2 (y 4752-4772), VSS (y 4776-4795, with a box
  under RA, 4735-4792 x 4790-4826, contact (4758,4806)).
- **Gate 3 (y 4797-4815) is on the column only**: its row ends at RA's edge (x 4730), west of
  the VSS box. South of it the column is the node `tl4_w4850`: a buried contact (ringed box
  4675-4712 x 4828-4872) onto a poly west along y 4840-4860 to a pad with a contact (4580,4850)
  on the track x 4581, and east, under RA, a segment y 4848-4875 (a field band y 4830-4845 under
  RA separates it from the VSS box above).
- **Gates 4 and 5** (y 4880-4900 and y 4925-4946) cross the stack below that, in series, down to
  a second VSS (the column's foot y 4945-4965 and a box under RA with a contact (4747,4975)).
- **East of RA each node has a leg with one more pull-down, gated by the other node:**
  - `tl4_w4686` runs east under RA (y 4670-4705) into the open (x 4795-4848) and south as a leg
    x 4812-4848. On the leg a buried contact (ringed box 4815-4850 x 4705-4742) onto a poly pad
    with a contact (4868,4716): the thin metal x 4868, which runs south to a pad with a contact
    (4868,4930) (`follow.py 4868 4780 N/S`: ends y 4714 and y 4934). Below the box a poly crosses
    the leg (y 4752-4776), and the leg's foot is a band (y 4788-4801) west onto the VSS box.
    That poly is the lower load plate's: a stub from the plate north under the thin metal
    (rounded top at y 4750) with an arm west.
  - `tl4_w4850`'s segment under RA runs east into an open box (4795-4848, 4860-4908) and south
    as a leg x 4812-4850 to a VSS band (y 4950-4965) that runs west under RA onto the lower VSS
    box. The poly of the thin metal's south pad crosses the leg (y 4918-4946).
- **Loads**: upper: a strip y 4668-4690 from the node's open part under a plate (4848-4900,
  4648-4692) to a VCC box under RB (4905-4958, 4665-4730, one ring). Whether the plate and the
  pad below it are one poly cannot be seen (the pad's outline lies between): drawn `?P`; that
  join is the upper load's tie. Lower: a strip y 4850-4875 from the open box under a plate
  (4850-4900, 4820-4878) to a VCC box (4908-4960, 4805-4878, specks (4935,4828), (4920,4843)).
  The plate's tail west ends on a heavy box (4803-4832, 4820-4848) on a tail of the node, as in
  the unit above: drawn `?` (AMB-026). **The gate across the upper node's leg reaches
  `tl4_w4850` only through that tie.**
- **Inputs** (`w_metal.png`, `w_acid.png`):
  - gate 1, `tl4_w4718`: a pad with a contact (4580,4718) at the south end of the north part of
    the track x 4581 (`follow.py 4581 4650 N`: north to a corner (4586,2896), east to (4652,2902)).
  - gate 2 is `tl4_w4590`: a pad with a contact (4364,4762) on the track x 4362, the same metal
    as the three-input NOR's third input (`follow.py`, one metal y 2810-5682; now drawn y 4565-4785).
  - gate 3 is `tl4_w4198`, the upper latch's clear: a pad with a contact (4537,4808) at the south
    end of the metal x 4537 (`follow.py 4537 4700 N/S`: one metal from y 2938 to y 4814, candidate
    (4536,4195), which is the upper latch's pad). **Input identified**; the metal is now drawn
    from y 3895 to y 4816. The upper latch's equation is unchanged.
  - gate 4 is `tl4_w4545`, the three-input NOR's output: the pad (4623,4893) where its metal
    x 4626 ends.
  - gate 5 is `tl4_w4545` as well: its row comes from a vertical poly x 4620-4642 that starts
    under that pad and runs south to about y 5030, where it turns east as a row y 5005-5030
    (`k1.png`, `s1.png`, `s2.png`: that row is a gate of the unit below, under RA at x 4725-4780;
    not drawn south of y 4992). First drawn as a net of its own (`tl4_w4935`), because one
    signal on two gates in series does nothing; review round 4 showed the junction has no gap
    in any shot and looks like the known joins, and the poly has no other driver in view. The
    join is drawn `?P` (the pad's outline hides it). Why the pull-down has two gates on one
    net is not understood.

### The NOR and the two inverters at y 4990-5465 (traced 2026-11-17, fifth run)

Views: `n_metal.png`, `n_acid1b.png`, `n_acid.png` (2.8x of 4590-4970 x 4960-5420), `p_*.png`
(6x of 4775-4975 x 5020-5170, the NOR's load), `q_*.png` (5x of 4540-4790 x 4985-5165), `r_*.png`
and `s_*.png` (4.8x of 4560-4820 and 4770-4980 x 5165-5425, three shots each), `v_*.png` (7x of
4785-4965 x 5285-5410, the lower load, `acid1b`, `acid`, `metal1`), `u_metal.png` (3x of
4240-4660 x 5150-5430, the rows' pads), `y1.png`, `y2.png` (2.6x, the tracks x 4452 and x 4496
from y 4380 to y 5350), `x_metal.png` (3x of 4560-4980 x 5350-5680); overlays `oc_*.png`,
`od_*.png`.

Down RA (`px.py col 4755 4990 5420 5 acid1b`: tan = diffusion, salmon = gate): the pair's lower
VSS box (to y 5010), gate (y 5015-5033), tan (y 5040-5095), gate (y 5103-5120), VSS box
(y 5125-5168, greenish contact at y 5140-5155), field (y 5180-5195), edge (y 5200-5205), tan
(y 5210-5225), gate (y 5232-5250), VSS box (y 5255-5310, contact y 5270-5290), gate
(y 5318-5337), tan (y 5345-5360), edge (y 5365), field (to y 5420).

**The NOR, y 4990-5170.** `tl4_w5068` = NOR(`tl4_w4545`, `tl4_w4850`).
- The stack is one diffusion, x 4703-4780: under RA and in the open west of it (the column
  x 4703-4725; `px.py col 4712 4980 5180 5 acid1b,acid`: in the chip-2 stripped shot diffusion
  y 4995-5005, poly y 5015-5030, diffusion y 5045-5090, poly y 5105-5115, diffusion y 5130-5140,
  field from y 5155). No field between the column and the part under RA is visible, only the
  single dark line at RA's edge that every shot has (`px.py row 5065 4650 4870 5 acid1b,acid`):
  taken as one diffusion, as in the pair. Its top is the pair's lower VSS box (contact
  (4747,4975)), its bottom a VSS box under RA with a contact (4750,5145).
- Gate 1 (y 5011-5033) is `tl4_w4545`: the vertical poly x 4619-4643 that starts under the pad
  (4623,4893) turns east at its south end (`q_metal.png`: an L, no break).
- Gate 2 (y 5100-5122) is `tl4_w4850`: its row starts at a pad with a contact (4583,5108), on
  which the south part of the track x 4581 ends (`q_metal.png`, ring in the metal, green hole
  in the clean shot; no metal south of the pad). **Input identified.**
- The node (y 5038-5098) has an arm west (y 5055-5083) with a buried contact (heavy box
  4675-4703 x 5053-5085, dark in the clean shot) onto a poly that runs west to a pad with a
  contact (4625,5068): the north end of the south part of the track x 4625
  (`follow.py 4625 5150 N/S`: (4626,5064) to (4624,5506), contact candidate (4625,5257)).
- Load: the node runs east from under RA as a strip y 5050-5086 (lines at y 5048 and y 5088 in
  `p_acid.png`) under a plate (4832-4873, 5032-5132) to a VCC box under RB (4905-4958,
  5040-5092, ring (4925,5068)). West of the plate a tail of the node runs south (x 4799-4820,
  to y 5140) and east under the plate's lower left corner, where a heavy box (4829-4858,
  5106-5134, ringed in the clean shot) sits: the tie, drawn `?` (AMB-026).
- Both rows end just east of RA (x 4791): row 2's end is 8 px from the tail (`p_acid.png`,
  `p_acid1b.png`: a rounded end, then the tail's own outline).

**The inverter, y 5175-5312.** `tl4_w4025` = NOT `tl4_w5068`. The same body as the inverter at
y 3781-3911, 1389 px lower (findcell: `tl1`'s inverter at 2126,955, clean shot, score 0.75), and
drawn as that body moved, with the VSS box, its contact and the VCC box set to what is measured
here. The rows are read here (`u_metal.png`, `r_*.png`):
- the gate row (y 5231-5251) starts at a pad with a contact (4625,5240) on the track x 4625,
  the metal that starts on the NOR's output pad: `tl4_w5068`;
- the output row (y 5186-5206) runs from the node's buried contact (box 4670-4698 x 5190-5215)
  west to a pad with a contact (4455,5197), where the track x 4452 ends. That track is one
  straight metal from the latch's data pad (4455,4025) (`follow.py 4453 5150 N`: 1150 px to
  (4451,4024), no candidate; `y1.png`, `y2.png`: no pad between, five rows pass under it).
  **So the latch's data `tl4_w4025` is NOT `tl4_w5068` = `tl4_w4545` OR `tl4_w4850`. Input
  identified; the latch's equations are unchanged.**

**The strong inverter, y 5297-5465.** `tl4_w5455` = NOT `tl4_w4243`.
- One gate row (y 5316-5338) over a diffusion 133 px wide (x 4675-4808): a column in the open
  west of RA (in the chip-2 stripped shot red minus green is 18-25 on it at y 5305, against 0-6
  on the field east of x 4820: `px.py row 5305 4650 4960 5 acid1b,acid`), the part under RA, and
  a leg east of RA (outline 4786-4810 x 5297-5348 in `v_acid.png`, `s_metal.png`; the row ends
  20 px beyond it at x 4830). Above the row a strip y 5297-5315 on the inverter's VSS box (which
  reaches y 5312 under RA); below it the node (y 5340-5368). The strip's part east of RA is too
  small to tell from its colour and is taken from its outline; if it is not there the gate is
  only narrower.
- The row starts at a pad with a contact (4537,5325). The track x 4496 turns east onto that pad
  at y 5315-5340 (`u_metal.png`, `y2.png`); it is one straight metal from the latch's output pad
  (4490,4243) (`follow.py 4497 5250 N`: 1058 px to (4493,4216), no candidate; the follower's end
  (4507,5336) going south is the corner). **Input identified: `tl4_w4243`.**
- The node leaves west through a buried contact (heavy box 4664-4702 x 5356-5392) onto a poly
  x 4667-4691 that runs south into a row y 5445-5465 (`x_metal.png`: a T without an outline
  between). The row crosses the whole view, x 4560-4980, under RA and RB; only a stub is drawn.
- Load: east of RA the node is a strip y 5348-5375 to x 4853, where it turns north (x 4853-4873,
  to y 5303: the outline runs down x 4853 and turns WEST along y 5348, so the diffusion is on its
  south and east side) and runs under a vertical plate (x 4873-4908, y 5292-5385; its east 10 px
  salmon under RB's margin) to a VCC box under RB (4905-4958, 5303-5377, ring (4925, 5320-5360)).
  The channel is about 72 wide and 30 long: a strong load, against 25-37 wide and 40-50 long in
  the other units. The strip between x 4853 and the plate is 17 px between two outlines and
  cannot be classed by colour (`px.py row 5320 4830 4912 2 acid1b,acid`).
- The plate's foot (y 5380-5402) runs west to a heavy box (4808-4842, 5357-5394) on the node's
  strip: the tie, drawn `?` (AMB-026).

## Ports

One wire is drawn to the strip's edge: `tl4_w4501`, poly, west at (4250, 4492-4512), an input
(gate 2 of the three-input NOR). The tracks leave the pieces inside the strip; each is drawn
only inside the views named above:

| Name | Track | Followed (`tools/follow.py`, not looked at) |
|---|---|---|
| `tl4_w3070` | metal x 4318 | from the pad (4320,3070) south to a corner (4315,4252), west to (4231,4246): leaves the strip west; candidate (4323,3392) |
| `tl4_w3178` | metal x 4410 | from the pad (4413,3178) south to y 3599 |
| `tl4_w3113` | metal x 4408 | from the pad (4410,3113) north to a corner (4421,2858), east to (4455,2856) |
| `tl4_w3808` | metal x 4496 | from the pad (4495,3808) north to a corner (4495,2723), west to (4273,2727) |
| `tl4_w3850` | metal x 4412 | from the corner (4412,3852) south to y 4336 |
| `tl4_w4025` | metal x 4452 | from the pad (4455,4025) south to the pad (4455,5197), the inverter's output row: drawn whole (`y1.png`, `y2.png`) |
| `tl4_w4068` | metal x 4625 | north of the pad (4625,4068) to a corner (4630,2988), east to (4694,2989); candidate (4626,4054) is the pad |
| `tl4_w4198` | metal x 4537 | y 2938 to y 4814, where it ends on gate 3's pad of the pair (4537,4808); candidates (4538,3782), (4535,3447), (4540,4215). Drawn y 3895-4816 |
| `tl4_w4243` | metal x 4496 | from the pad (4490,4243) south to a corner at y 5327 and east onto the pad (4537,5325), the strong inverter's gate row: drawn whole (`y1.png`, `y2.png`) |
| `tl4_w4590` | metal x 4362 | y 2810 to y 5682 through the pads (4364,4590) and (4364,4762); candidates (4364,3014), (4366,5125). Drawn y 4565-4785 |
| `tl4_w4545` | metal x 4626 | from the pad (4620,4545) south to the pad (4623,4893): drawn whole |
| `tl4_w4718` | metal x 4581 (north part) | from the pad (4580,4718) north to a corner (4586,2896), east to (4652,2902). A stub is drawn |
| `tl4_w4850` | metal x 4581 (south part) | from the pad (4580,4850) south to the pad (4583,5108), the NOR's gate 2: drawn whole |
| `tl4_w4545` (poly) | poly x 4619-4643 | from the pad (4623,4893) south past gate 5's row, then east as the row y 5011-5033, the NOR's gate 1: drawn whole |
| `tl4_w5068` | metal x 4625 (south part) | from the pad (4625,5068) south through the pad (4625,5240) to (4624,5506) (`follow.py`): a pad at about (4625,5500) with a row east at y 5490-5510 (`x_metal.png`). Drawn to y 5250 |
| `tl4_w5455` | poly row y 5445-5465 | from the T under the strong inverter (x 4667-4691) east and west across the whole strip (`x_metal.png`: x 4560-4980 at least). A stub x 4650-4710 is drawn |

## Ambiguities

1. **The two load ties are `tl1`'s `?` items** (in the cells; here at (4801-4821, 4186-4216) and
   (4806-4834, 4065-4086)). Until one is read, the cross-coupling is an assumption, here as in
   `tl1` (AMB-026).
2. **The supplies of RA and RB** are named from structure only.
3. A copy checked by overlay at 4x and 2.5x; the cells' small items (the third pull-down's
   diffusion to the VSS box, the gate caps) were not each measured here.

## Review

Round 1 (full review, 2026-11-17 23:21 +0000, a fresh agent on claude-fable-5-2, at commit
2a0c723; images in `cache/scratch/tl4/review-1/`). Piece: the latch at y 3906-4390 with its
rows, pads and tracks. Told to suspect: any difference between the copy and the master, the
node boxes west of RA, each row's pad and metal (trap 16) and contacts under the metals the
rows cross, the metal x 4625 between its pads, the pads of the thin metal x 4860-4875 and the
polys they lie on, the third pull-down's drain and source, the contact (4768,4354), anything
undrawn between RA and the thin metal.
It checked: copy against master side by side at 2x (clean and metal) and at 4x in three shots
(no extra or missing gate, pad or contact); no thin metal at x 4814-4828; all nine pads (ring
with a bright centre in both metal shots, green hole in the clean shot); the four rows to their
pads at 4x in both stripped shots, with no green hole under the metals x 4537, 4580, 4625; the
metal x 4625 between its pads; the thin metals x 4690 and x 4867 on their pads; the stub
y 4103-4123; both node boxes; the upper unit's third pull-down gate (one poly with the lower
plate's top bar, 5x); the lower third pull-down (pad, stem and band one poly; drain strip
unbroken, 6x; source strip diffusion through to the VSS box); the extraction.
Findings, all geometry only, each checked by the tracer:
1. The VSS contact drawn at (4768,4354) is at about (4745,4368): confirmed (`textmap.py 4712
   4338 4796 4410 4`: bright centre C-D inside a dark ring at x 4740-4748, y 4362-4370 in both
   metal shots; plain bright metal at the drawn place). Moved. The reviewer noted that the old
   rectangle began 1 px below the gate band of `tl4_w3928`.
2. The VCC contact on RB is one ring x 4915-4945, y 3995-4200, not 24 x 60: confirmed
   (`px.py col 4930 3980 4216 8`: no dark bar between y 4004 and y 4190); drawn 24 x 165 next
   to the cell's own.
3. The inverter's pull-down gate (the cell's `P 2651,4388:2663,4470`, here x 4776-4788) is
   about 22 px long here, not 12: confirmed for the copy (`px.py row 3987 4770 4812 3`: dark
   edges at x 4785-4788 and x 4800-4803 in the chip-2 stripped shot). Not changed: the item is
   `tl1`'s cell, and the master was not looked at; in the handoff for `tl1`.
Could not be checked: the two `?` load ties, the supplies of RA and RB, the tracks beyond the
piece, the neighbours' VCC boxes on RB (undrawn).
`tools/t.sh tl4 sameconn.py 2a0c723`: `connections identical`.
`.venv/bin/python tools/sameconn.py 2a0c723`: `connections identical`.

Round 1: no findings that change a connection.

Round 1 of the second run (full review of a batch of two pieces, 2026-11-17 23:42 +0000, a
fresh agent on claude-fable-5-2, at commit 204c586; 14 images in
`cache/scratch/tl4/review-2/`). Pieces: the NOR (y 3000-3232) and the inverter (y 3770-3911).
Told to suspect: differences from the masters (a third gate, anything west of the column), the
five pads and their metals (trap 16), whether the track x 4408-4410 is cut between the NOR's
output pad and its gate 2 pad, whether the inverter's gate pad is separate from the latch's
data pad on the same track and its output pad from the latch's output pad, the load strips and
VCC boxes, a second VCC contact near (4930,3874), contacts under the metals the rows cross,
the gate row y 3841-3859.
It checked at 4x-6x in two to four shots, with profiles and text maps: the NOR's column
(exactly two gate bands, both across the diffusion; node box; both VSS boxes; field west of
it); both load strips east of RA (plain diffusion, no poly across); the cut of the track
x 4409 (no metal y 3124-3172 in either metal shot, open green in the clean shot); the five
pads; the gate pad's L metal and the field on the track x 4452 from y 3882 to 4002; no metal
on the track x 4493 from y 3872 to 4220 (chip 2; chip 1 has dirt at y 4094-4184); no contacts
under x 4362-4625; the two rows; the extraction.
Findings, geometry only, checked by the tracer and fixed:
1. The inverter's VCC box is x 4908-4955, y 3815-3868, not one diffusion to y 3904: a field
   band lies at y 3870-3890 and a second box (4905-4960, 3893-3955) with its own contact about
   (4928,3922) begins below it: confirmed (`textmap.py 4908 3800 4952 3912 4`: edge bars at
   y 3868-3872 and y 3888-3892, plain bright metal between). The box is drawn to y 3868. The
   second box feeds a strip east under a plate at about x 4962-5015, y 3890-3925: the east
   neighbour's load, not drawn (Not done).
2. The NOR's VCC box is y 3068-3148 with one elongated ring y 3078-3140 (`a1.png`): drawn so.
The reviewer also read the inverter's tie box (4838-4872, 3857-3888) as a heavy-outlined box on
the tail in four shots; the `?` is kept, because the item is copied from `tl1`'s uncertain one
and was not measured by the tracer.
Could not be checked: the far ends of the followed metals; a greenish patch in the clean shot
at (4918-4940, 3878-3887) under RB with no ring in either metal shot.
`tools/t.sh tl4 sameconn.py 204c586`: `connections identical`.
`.venv/bin/python tools/sameconn.py 204c586`: `connections identical`.

Round 2: no findings that change a connection.

### Review of the three-input NOR (third run)

Round 3, full review of one piece (the unit at y 4410-4645), 2026-11-17 18:22 -0600, at commit
5775898, a fresh Fable agent, images in `cache/scratch/tl4/review-3/` (14). Told to suspect: the
ring being one diffusion (top strip, leg, band under RA); the inner area being field and the VSS
box touching the column only through the neck; the rows' east ends; the foot's join to the lower
VSS box; the node's buried contact; the continuity of rows 1 and 2 and the pad (4364,4590); the
load and its tie. It measured with `px.py` columns x 4712, 4744, 4780 and rows y 4453, 4495,
4552, 4572, 4584, `textmap.py` on the pads and along row 2, and views at 4.2-6.5x.
No finding changes a connection. Geometry only, all confirmed on `oa1.png`/`u4.png` and fixed:
1. The three rows end at x 4726-4733 (RA's edge), not x 4722: drawn to x 4728.
2. The foot's rectangle covered field at x 4712-4728, y 4630-4645: split into the foot
   (y 4605-4628) and the box.
It also reports the south end of the metal x 4626: a pad with a contact at about (4625,4892)
(ring with a bright centre, green hole in the clean shot). Not drawn: it belongs to the next
unit (Not done). And an undrawn pad with a contact at about (4278,4571) in the bus field, on
none of the three rows (Not done).
Found correct: the ring is one diffusion (the column's east edge line is open at exactly four
places: y 4426-4435, 4480-4486, 4540-4555, 4609-4621; the band under RA reads 199/176/135
against the VSS box's 200/175/140 and field's 175-200/120-135/120-130); the inner area is
field; the rows do not run on under RA; the foot joins the lower box; both VSS contacts, the
buried contact and the two pads' contacts; row 1 continuous from `tla`'s end, row 2 without a
pad from x 4252 to x 4600; the load's strip reaches the VCC box; the tie kept `?`.
Could not be checked: the stripped shot under RA (fringes); whether the tie box's poly overlaps
the diffusion; row 2 west of x 4250; the track x 4362 beyond the stub.
`tools/t.sh tl4 sameconn.py 5775898`: `connections identical`.
`.venv/bin/python tools/sameconn.py 5775898`: `connections identical`.

Round 3: no findings that change a connection.

### Round 4: full review of the cross-coupled pair (2026-11-17, commit 541081e, images `review-4/`)

Told to suspect: which of gate 4's row and the vertical poly the pad (4623,4893) feeds; the
stack's continuity between the open column and the part under RA; the three joins across RA's
east edge; the crossing poly's join to the stub and its separation from gate 2's row (and the
lower pad poly from gate 5's row); where the rows end; the buried contact on the upper leg; the
contacts on the tracks; whether the thin metal touches the lower plate.
Checked at 6-10x with `px.py`, `textmap.py --acid`, `follow.py` (13 images).

- **Finding 1, changes a connection, confirmed.** Pad (4623,4893) to the vertical poly: the
  trace had a gap (gate 5 a net of its own, `tl4_w4935`). No gap in any of four shots; the dips
  between pad and poly are at different y in the two stripped shots (y 4914-4918 `acid`,
  y 4920-4924 `acid1b`), as at the known-joined pad (4580,4850). Checked here from the south
  (`s1.png`, `s2.png`): the poly's far end is only a gate row, so it has no other driver.
  Fixed: `?P 4620,4908:4642,4924` joins them, the name `tl4_w4935` is gone, and
  `tl4_w4850 = NOT(tl4_w4198 OR tl4_w4545 OR tl4_w4686)` with `tl4_w4545` on gates 4 and 5.
- Geometry only, fixed: VSS contact centre (4758,4806); rows 4/5 end near x 4786; the crossing
  poly and the lower pad poly start near x 4800. Not changed: the thin metal is about 24 px wide
  over the lower plate (no contact there); the node segment enters the open box through an
  opening about 10 px high.
- Found correct: nine transistors; the six contacts; rows cross the other tracks without
  contacts; metals x 4537 and x 4364 continuous; no metal at x 4581 between its pads; field
  between gate 2's row and the crossing poly, gate 5's row and the lower pad poly, pad and
  stub, closed stub and gate 1's row; stub joined to the lower plate; foot joined to the VSS
  box; gate 3's row stops short of the box; the `?P` plate-to-pad join supported.
- Could not be checked: the column's continuity under RA and the three joins across RA's east
  edge (the rail-edge line is there over field too: inferred); crossing poly to stub rests on
  the clean shot alone; the lower tie stays `?`.

`tools/t.sh tl4 sameconn.py 541081e`: `CONNECTIONS DIFFER (7 differences)`, all of them gate 5's
net (`tl4_w4935` gone, two transistors and one equation renamed).

Round 4: one finding that changes a connection, fixed.

### Round 5: fix check of round 4's fixes (2026-11-17, against commit 541081e, images `review-5/`)

Covered: the `?P` join of the pad (4623,4893) to the vertical poly, the VSS contact's new place,
the rows lengthened to x 4786, the two polys now starting at x 4800. Checked at 5.3x in four
shots and with `px.py`/`textmap.py` (8 images). The join is right (the poly comes straight out
of the pad's ring; the dark stretch y 4912-4920 is a single outline, the same as at the pad's
east exit); the reviewer did not re-check the poly's south end, and the `?` stays. The geometry
items are right: the rows end at x 4774-4786 with field at x 4796 before the pad poly; both
polys cross their whole legs (edges about 4812 and 4848). `sameconn` (tl4 alone and all files):
7 differences, all intended.

Round 5: no findings.

## Not done

- The nine tracks beyond the views (table under Ports), and their other pads.
- RA and RB between the drawn pieces (y 3232-3770) and south of y 5420, and where they are fed.
  `follow.py 4928 5150 S` takes RB to a corner (4920,5826) and west to (4756,5826): not looked at.
- The rest of the gate column: y 3220-3780 (no findcell match).
- The row field south of the strong inverter, y 5445-5900: poly rows across RA and RB at a pitch
  of about 45 (`x_metal.png`: y 5445-5465, which is `tl4_w5455`, y 5490-5510 from a pad at about
  (4625,5500) at the south end of `tl4_w5068`'s track, y 5540-5560, y 5575-5595 ...), with dark
  specks on RA between them (about (4755,5395), (4760,5585), (4760,5605), (4762,5630)): whether
  the rows are gates under the rails is not read.
- Where `tl4_w5455`'s row goes, east and west.
- Where `tl4_w4718` comes from (track x 4581 north).
- In the bus field: a row y 4880-4900 from a pad with a contact (4537,4892) on the south part
  of the metal x 4537 west to about x 4335; that metal jogs east at y 5235-5250 to x 4583 and
  runs on south (`u_metal.png`). A pad with a contact at about (4278,4571). Pads at about
  (4278,5197), (4278,5262) and (4278,5410) on the track x 4275 (`u_metal.png`).
- The west end of `tl4_w4501`'s row (in `tl3`'s strip) and the other pads of the track x 4362.
- A VCC box under RB at (4905-4960, 3893-3955) with a contact about (4928,3922) and a strip
  east under a plate at about x 4962-5015, y 3890-3925: a load of the logic east of RB (`tl5`).
- The bus field, the rows north of y 2960 and south of y 5400.
