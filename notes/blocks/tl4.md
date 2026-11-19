# tl4: top-left random logic, the fourth strip (x 4250-4967, y 2500-6350)

Package `tl4` (part 4 of 6 of the top-left logic). Trace: `trace/tl4.txt`. Views:
`cache/scratch/tl4/`. The strip holds most of the vertical control's **right cluster**
(`tla`'s name for it): a bus field of vertical metals (x 4250-4680), a gate column on a rail
RA (x 4728-4775), loads between RA and a second rail RB (x 4905-4950).

## Status

2026-11-18 15:39 -0600. **Everything in the strip is drawn** (nine units, 47 transistors, and the wiring
around them). Last piece, tenth run: **RA's supply**: the wide foot along y 2938-2997 runs into
RA's top end, and a wide vertical metal on the strip's east edge (x 4949-4995) takes it north
across all the rows to the band north of y 2500, the band that `tl5`'s rail RC ends on. So RA
is on the same supply as RC (both named vss from their boxes). No connection changes
(`tools/sameconn.py`: identical). What is open now lies outside the strip (Not done).

Before that, 2026-11-18 15:24 -0600: **the wiring south of the routing channel.** Traced in the
ninth run: **the strip south of the routing channel** (x 4250-4967, y 5790-6350: no device,
three pads). No gate changed and no equation prints differently. One join: **`rcs_x1` goes on
to `tl5`** (`rcs_x1`, its bus line x 5107): `tl3`'s metal of latch C's clear (`tl3_e4808`)
runs east along y 5895 to a pad (4629,5891) whose row is `tl5`'s. A second metal from the west
(y 5939, source in `tl3`'s strip, not followed) ends on a pad (4583,5936) of `tl5`'s row
y 5936 (`tl5_w5936`, bus line x 5063). `tl5`'s thin metal `tl5_w4590` (the clear of its latch
c) comes in along y 5984, turns south at x 4929, has a contact on a pad (4929,6323) whose row
runs west across the whole strip, and goes on south. The legs of the rails RA, RB and RC run
south out of the strip (no contact on them here).

Before that, 2026-11-18 15:01 -0600: **the wiring north of the units.** Traced in the
eighth run: **the tracks' north ends, the knot of pads at y 2740-2910 and the bus lines along
y 2500-2740** (x 4250-4967: no device, 16 pads; still 47 transistors). The tracks of the bus
field are now drawn to their north ends. **No gate changed.** It identifies five more inputs and
outputs, and nine merged equations print another name for one net (listed under "The tracks'
north ends" below):

- **`rcs_e3` = NOT `tl4_w3850`**: the inverter at y 3781-3911 (`rcs_e3`) drives the track
  x 4496 north to the sixth bus line (y 2728) and west to `tla`'s pad (4270,2725), the top of
  `tla`'s bus line E. `rcs_e3` was an unidentified input of the step logic; its source is
  `tl4_w3850` = `tl5_w5761`, the south bus line x 5412.
- **`tl4_w4590` is the gate of `tl3`'s inverter E1** (`tl3_e3028`): `tl3_w3373`, the enable of
  `tl3`'s latch A, = NOT `tl4_w4590`. The track x 4366 ends in the north on two pads whose rows
  both go west: (4366,3030), `tl3`'s row, and (4366,2812), a row on west at y 2801-2820
  (not followed: `tl3`'s strip). What drives `tl4_w4590` is still not known.
- **`tl4_w4718` is `tl5_w3245`** = NOR(`tl5_w3550`, `tl5_w4160`) (`tl5`'s NOR of its latches a
  and b): the track x 4581 ends on a pad (4648,2898) of `tl5`'s row y 2900. It is the set
  input of the pair here.
- **`tl3_e4243` goes on to `tl5`**: the track x 4321 runs north of the top NOR's pad to a pad
  (4410,2767), a poly link, a pad (4583,2811), a metal along y 2812, a pad (4866,2812) and
  `tl5`'s row y 2810: it is `tl5_w4458`, the enable of `tl5`'s latch c.
- `tl4_w3113` (the top NOR's output) goes to `tl5` the same way (two pads, a metal along
  y 2857, `tl5`'s row y 2855): `tl5_w2722` = NOT `tl4_w3113`.
- `tl4_w4068` (the upper latch's enable): `tl5`'s pad (4910,2767) has a second metal west
  along y 2771 to a pad (4539,2768), whose poly runs north out of the strip at y 2500.
- Passing: bus line 1 (`tl4_w2512`, new), line 4 (`tl5_w4937` = NOT `tl4_w4068`, west to a pad
  (4279,2640) and a row on west), line 5 (`tl5_w2722`, west out of the strip as metal).

Before that, 2026-11-18 12:20 -0600: **nine units and the wiring south and west of them.** Traced
in the seventh run: **the bus field's wires west of the gate column and the routing channel south
of it** (x 4250-4967, y 4300-5790: no device, 17 pads, eight poly rows; still 47 transistors).
It joins seven nets of this strip to their names elsewhere. **No gate changed; three merged
equations print a different input name** (`tl3_e4243` for `tl4_w3070`), and `tl3`'s
`tl3_w4978` prints `tl4_w4590` for `tl3_e5114`:

- `tl4_w3070` (the second latch's data, the top NOR's gate 1) **is `tl3`'s `tl3_e4243`** =
  NOR(`tl3_e4152`, `rcs_mv`): the track x 4318 leaves the strip west at (4250, 4236-4256).
- `tl4_w3850` (the input of the inverter `rcs_e3`) **comes from the south bus**: `tl5_w5761`.
- `tl4_w4590` (an input of the three-input NOR and of the pair) is `tl3_e5114` (gate 2 of
  `tl3`'s NOR e5, which makes its latch B's enable) and `tl5_w5674`.
- `tl4_w5068` (the NOR's output) goes on east as `tl5_w5500`; `tl4_w5455` (the strong
  inverter's row) as `tl5_w5457`, and west.
- **`rcs_mv` passes through**: from `tl3`'s pad by a poly L in this strip, `tl3`'s metal
  x 4236 (`tl3_e4915`), a pad and two rows to `tl5` (`rcs_mv`).
- Passing wires: `tc1_o3527` (`tl5_w5544`) by a jumper to the row y 5718 west; `tcw_a`
  (`tl5_w5631`) straight across; `tl3_e4372` and `tl3_e4635` each from a row in the south to
  `tl3`'s gate row in the north; `tl3_e5240`, a row-metal-row loop that enters and leaves west
  (`tl3`'s run 8, merged while this piece was in review, has its north row as the gate of an
  inverter whose output is the south row of `tl3_e4635`: so **`tl3_e4635` = NOT `tl3_e5240`**,
  the join `tl3` left open as `tl3_e4635_u`, aliased here).
- Seen, not drawn (it is in `tl3`'s strip): the row of `tcw_a` runs on west to `tl3`'s pad
  (4104,5633), which `tl3` has as `tl3_e4152` = `tl4_w4501`. If so, **`tcw_a` is `tl3`'s track A
  and gate 2 of the three-input NOR here.**

Before that, 2026-11-18 07:24 -0600: **nine units.** Traced in the sixth run: the rest of the gate
column, y 3225-3765, which is **a second transparent latch with its data inverter** (11
transistors, 47 in all), laid out by hand and strapped by two short metals: `tl4_w3245`,
`tl4_w3390` and `tl4_w3178` below. Inputs identified, no merged equation changed: `tl4_w3178`
(the top NOR's second input) is this latch's inverse output; its data is `tl4_w3070` (the top
NOR's first input), its clear `tl4_w4198` (the clear of the latch at y 3906-4390 and of `tl5`'s
latches a and b) and its enable `tl5_w3505` (`tl5`'s latch a's enable: one poly row along
y 2976-2996 from `tl5`'s pad (5494,2985) to the pad (4452,2985) here).
Before that, 2026-11-17 23:31 -0600: **eight units.** Traced in the fifth run: the three units
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
tl4_w3113 = NOR(tl3_e4243, tl4_w3178)                             firm   (tl3_e4243: tl4_w3070 until the seventh run, an alias now)
tl4_w3245 = NOT tl3_e4243                                         marked: the load's tie
tl4_w3390 = NOT( tl3_e4243 AND tl5_w3505  OR  tl4_w4198  OR  tl4_w3178 )   marked: the load ties (the lower one carries tl4_w3178 to this gate)
tl4_w3178 = NOT( tl4_w3245 AND tl5_w3505  OR  tl4_w3390 )         marked: the load ties (the upper one carries tl4_w3390 to this gate, the inverter's tl4_w3245)
rcs_e3    = NOT tl4_w3850                                         marked: the load's tie (`?`, as in tl1)   (rcs_e3: rcs_e3 until the eighth run, an alias now)
tl4_w3928 = NOT tl4_w4025                                         firm
tl4_w4113 = NOT( tl4_w4025 AND tl4_w4068  OR  tl4_w4243 )         marked: the two load ties
tl4_w4243 = NOT( tl4_w4198  OR  tl4_w4068 AND tl4_w3928  OR  tl4_w4113 )   marked: the two load ties
tl4_w4545 = NOR( tla_w3417, tcw_a, tl4_w4590 )                    marked: the load's tie   (tcw_a: tl4_w4501, tl3's alias since its run 9)
tl4_w4686 = NOT( tl5_w3245 AND tl4_w4590  OR  tl4_w4850 )         marked: the lower load's tie carries tl4_w4850 to this gate   (tl5_w3245: tl4_w4718 until the eighth run, an alias now)
tl4_w4850 = NOT( tl4_w4198  OR  tl4_w4545  OR  tl4_w4686 )        marked: the load ties; tl4_w4545 on two gates in series (one join `?`)
tl4_w5068 = NOR( tl4_w4545, tl4_w4850 )                           marked: the load's tie
tl4_w4025 = NOT tl4_w5068                                         marked: the load's tie (`?`, as in the inverter above the latch)
tl4_w5455 = NOT tl4_w4243                                         marked: the load's tie
```

So the chain is: the three-input NOR `tl4_w4545` and the set/reset pair's `tl4_w4850` are OR-ed
(`tl4_w5068` and its inverter) into the data `tl4_w4025` of the latch at y 3906-4390; the
latch's output `tl4_w4243` is inverted by a strong inverter onto a poly row at y 5445-5465
(`tl4_w5455`), which crosses the whole strip: east it is `tl5_w5457` (to `tl5`'s track x 5581 and a row out of its strip at y 4520), west it goes on into `tl3`'s strip.

The pair at y 4645-5000 is a set/reset latch: `tl4_w4718` AND `tl4_w4590` both high pull
`tl4_w4686` low, which lets `tl4_w4850` rise; `tl4_w4198` (the clear of the latch above as well)
or `tl4_w4545` pull `tl4_w4850` low again. `tl4_w4850` leaves south on the
track x 4581; `tl4_w4686` goes no further than the pair (its thin metal ends on the lower gate's pad).

**The second latch (y 3225-3765)**: open while `tl5_w3505` is high, it takes `tl4_w3070`
(`tl4_w3390` = NOT data, `tl4_w3178` = data, when open and not cleared); `tl4_w4198` high
forces `tl4_w3390` low. Only the side `tl4_w3178` leaves it, on the track x 4410 to the top
NOR, so `tl4_w3113` = NOR(`tl4_w3070`, `tl4_w3178`) is NOR(the latch's data, the latch's
inverse-side output). `tl4_w3390` and `tl4_w3245` go no further than the latch (their metals
end on its own pads). It is the same circuit as the latch below it and as `tl5`'s latch a, which
shares its enable and its clear.

A latch: open while `tl4_w4068` is high, it takes `tl4_w4025`; `tl4_w4198` high forces
`tl4_w4243` low. The same build as the two latches in front of `rcs_e4` and the third latch
of the small cluster (`notes/blocks/tl1.md`). **Unlike in the first cluster, the inverter
above the latch does not feed the latch's data here**: its output `rcs_e3` leaves north on
the metal x 4496, and the latch's data `tl4_w4025` comes from the south on the metal x 4452.
(Fifth run: that metal comes from the inverter at y 5175-5312, so the data is `tl4_w4545` OR `tl4_w4850`; the output `tl4_w4243` goes to the strong inverter at y 5297-5465.) What the enable and the clear are is not known beyond `tl5`'s names for them (`tl5_w3982`, `tl5_w3636`).

## Inventory

| Where | What |
|---|---|
| x 4250-4680, y 2700-5440 | bus field: nine vertical metal tracks, poly rows east into the column, pads. Drawn whole (seventh and eighth runs; the track x 4279 north of y 4073 is `tla`'s, the tracks x 4537 and x 4625 north of the units `tl5`'s) |
| x 4290-4967, y 3012-3222 | **the NOR** (`tl1`'s NOR at 2125,-520, findcell 0.77) |
| x 4300-4967, y 3225-3765 | **the second latch and its data inverter** (hand-traced; no cell matches), with the enable track's north pad (4452,2985) and its row east to the strip's edge |
| x 4400-4967, y 3781-3911 | **the inverter** (`tl1`'s inverter at 2125,-434, findcell 0.74) |
| x 4665-4967, y 3906-4390 | **the latch: this piece** |
| x 4250-4967, y 4410-4645 | **the three-input NOR** (hand-traced; no cell matches) |
| x 4347-4967, y 4645-5000 | **the cross-coupled pair** (hand-traced; no cell matches) |
| x 4560-4967, y 4990-5170 | **the two-input NOR** (hand-traced) |
| x 4437-4967, y 5175-5312 | **the inverter** onto the latch's data (the inverter at y 3781-3911 moved by 1,1389: `tl1`'s inverter at 2126,955, findcell 0.75) |
| x 4520-4967, y 5297-5465 | **the strong inverter** on the latch's output (hand-traced) |
| x 4250-4967, y 5440-5790 | **the routing channel**: eight poly rows (pitch 44) under the tracks' south ends and under RA and RB, eight pads. No diffusion: the green-rimmed strips between the rows in the clean shot are open field. Drawn (the row y 5585 is `bw`'s, the row y 5545 west and its pad `tla`'s) |
| x 4250-4967, y 5790-6350 | **south of the channel** (ninth run): two metals from the west (y 5895 `rcs_x1`, y 5939) ending on pads whose rows go east to `tl5`; `tl5`'s thin metal x 4929 and its pad (4929,6323) on the row y 6323; the legs of RA (x 4667-4715), RB (x 4754-4801, after a turn west along y 5806-5856) and RC (x 4841-4888, from `tl5`'s turned rail y 5891-5942). No diffusion. Drawn (the row y 5847 is `tla`'s, the metal L y 5982 / x 4628 `amrw`'s, the four rows y 6157-6281 and their pads `urch`'s and `amrw`'s) |
| x 4250-4967, y 2500-2910 | **the top of the strip** (eighth run): six metal bus lines along y 2512-2728 that step down one pitch (43 px) at x 4580-4712 and end on pads at x 4822-4912, whose poly rows go on east; the knot of eight pads at y 2767-2898 where the tracks end. Drawn (lines 2 and 3 are `r9m`'s, the pads (4910,2767), (4537,2940) and (4270,2725) `tl5`'s and `tla`'s) |
| x 4732-4995, y 2500-3004 | **the supply of RA** (tenth run): a wide vertical metal x 4949-4995 from the band north of y 2500 to a wide foot along y 2938-2997, which runs into RA's top end. Drawn as far as the strip's edge x 4967 |

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
- **Inverter.** Output `rcs_e3`: the node box's poly west along y 3797-3815 to a pad
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

### The second latch at y 3225-3765 (traced 2026-11-18, sixth run)

Views `h1`-`h7_*.png` (5.8-6x, the three shots, tiles of about 210 x 200 px), `h3_a/b.png`,
`h4_a/b.png` (4-5.4x, five shots), `k1`/`k2_*.png` (bus field, 2.75x), `m1`-`m4.png` (the
enable row's north pad and its way east); overlays `oe1`-`oe5.png`. No cell matches
(`tl1`'s column has a copy of its pair at the corresponding place). Not a row of units: one
circuit, whose two halves are joined by two short metals.

```
tl4_w3245 = NOT tl4_w3070
tl4_w3390 = NOT( tl4_w3070 AND tl5_w3505  OR  tl4_w4198  OR  tl4_w3178 )
tl4_w3178 = NOT( tl4_w3245 AND tl5_w3505  OR  tl4_w3390 )
```

**What lies under the two metals** (`tools/railprof.py 4732 4772 3220 3790`, and
`4683 4703 3220 3790` for the metal x 4680-4704; `tools/px.py col 4738` and `col 4764 3262 3460 4
acid1b`: gate salmon 245-254/163-188, diffusion tan 200/180/137):

| y under RA | what |
|---|---|
| 3229-3249 | poly over field: the inverter's plate poly on its way west to the pad (4690,3247) |
| 3272-3326 | VSS box 1, contact ring (4745,3285) |
| 3327-3356 | gate: the data row |
| 3357-3378 | d1 |
| 3379-3393 | gate: the enable row |
| 3403-3453 | the node `tl4_w3390` |
| 3454-3467 | gate: east piece of the row y 3452-3472 (`tl4_w3178`) |
| 3496-3545 | VSS box 2, contact (4745,3512) |
| 3557-3626 | the lower node `tl4_w3178` (a bar and a strip; field in the middle, see below) |
| 3627-3651 | gate: the enable row again |
| 3652-3681 | d3 |
| 3682-3706 | gate: the row of `tl4_w3245` |
| 3707-3755 | VSS box 3, contact (4750,3725) |

The diffusion of the upper stack is wider than RA: x 4700-4776 from y 3300 (the gap between the
two metals, x 4705-4722, is green field at y 3255-3300 and at y 3510-3560 and has no green
at y 3300-3440 and y 3490-3508; row 2 is a gate at x 4712, 234/165/123).

**The data inverter** is east of RA, y 3229-3360. A diffusion band y 3283-3320 (y 3283-3314 under the plate) runs from VSS box
1 east under a vertical poly (x 4788-4812, y 3265-3357, joined at its south end to the data row's
east end: salmon to x 4786 under RA's margin, then open poly, `px.py row 3340 4756 4880 3`), to
a patch at x 4813-4845 (the node), under the plate (x 4847-4898) and into the VCC box under RB
(rings (4930,3257), (4926,3305)). The band's two edges show as dark lines across the vertical
poly (y 3283, y 3320) and across the plate (y 3283, y 3313) in all three shots: that is how the
band was found. The plate's poly goes on north and west, as a bar y 3229-3249 over field under
RA, to a pad with a contact (4690,3247) (green hole in the clean shot, bright centre in a ring
in both metal shots): the top of the metal x 4680-4707, which runs south to a second such pad
(4690,3703) (`tools/follow.py 4692 3330 S`: end (4688,3708)), whose poly row y 3681-3700 is the
last gate of the lower stack. So the inverter's output reaches that gate through its load's
plate and the plate's tie (drawn `?`: the plate's lower band hooks down onto a heavy dark box
(4838-4872, 3330-3360)).

**The upper node `tl4_w3390`** has four pull-downs: the data and enable rows in series (stack),
and two side by side under the row y 3452-3472, which is **two polys**: all three stripped
shots show field in a box (4722-4752, 3442-3488) between them (pink 199/124/125 in the clean
shot, green in both chip-2 and chip-1 stripped shots; `px.py row 3462 4660 4800 4`), and RA has
a notch or an elongated ring there in both metal shots. The west piece (it ends at x 4724; field to x 4743) comes from the pad
(4540,3462) on the track x 4537 (`tl4_w4198`) and gates a column under the metal x 4680-4707
(bright gate salmon 249/181/124 at (4690,3462)); the east piece (x 4747-4800) comes from a
vertical poly east of RA (x 4793-4825, y 3449-3515) that is the foot of the lower load's plate
(`tl4_w3178`). Both columns end on VSS box 2. Load: a band y 3423-3443 from the node east
under the plate (x 4848-4900, y 3378-3463; its edges are the lines y 3420 and y 3450 across the
plate) to the VCC box under RB (elongated ring (4915-4945, 3415-3470)). The plate has a contact
(4863,3390) (green hole; bright blob in a ring) to the metal x 4851-4881, which ends in the
south on a pad (4863,3612) whose poly row y 3587-3610 runs west across the lower node's east
column: the cross-coupling gate.

**The lower node `tl4_w3178`**: east of RA a column x 4800-4843 from y 3520: a patch with the
load's band y 3523-3551 east under the plate (x 4847-4900, y 3497-3568; lines y 3522 and y 3552)
to the VCC box under RB (elongated ring (4918-4945, 3515-3640)); south of the patch the gate of
`tl4_w3390` (two orange blobs in the clean shot, x 4803-4840), then a J-shaped diffusion
(x 4820-4842 down to y 3730, west along y 3707-3730) onto VSS box 3. Under RA the node is a bar
west from the patch (y 3557-3582), a strip south (x 4740-4762) and a widening west above the
enable row to a column under the metal x 4680-4707 (x 4687-4714; `px.py row 3615` and `3655 4670
4730 3`); field inside (pink, x 4765-4790, y 3590-3660; `px.py col 4780 3640 3770 4`). The enable
row (y 3625-3645, from the pad (4455,3635), ends rounded at x 4772) crosses strip and column;
below it d3, the row of `tl4_w3245`, VSS box 3. The output leaves the column's top by a heavy
box (4673-4709, 3578-3607) (the metal above it is dark for 35 px with no bright centre: a
buried contact under the metal, guide trap 22) and a row y 3582-3602 west to the pad
(4413,3592), where the track x 4410 from the top NOR's pad (4413,3178) ends
(`follow.py 4410 3240 S`: end (4408,3598)).

**The rows** (`k1`/`k2_*.png`; salmon bands with `px.py col` at x 4500, 4590, 4690, 4740, 4766 and
`px.py row` at y 3372, 3416, 3462, 3592, 3635): the data row comes from a pad (4320,3372) on the
track x 4318 (`tl4_w3070`; `follow.py 4318 3240 S`: one metal), along y 3362-3382, up a riser
x 4558-4578 and east along y 3322-3342. The enable track x 4452 is a north piece of that track
(`follow.py 4452 3500 N` and `S`: (4451,2984)-(4452,3640); the south piece from y 4014 is
`tl4_w4025`) with three pads: (4452,2985), whose row y 2976-2996 runs east under the corner of
`tl4_w4068`'s metal and under a wide metal (y 2955-2997, east of x 4730) to the strip's edge and
on as `tl5`'s row to the pad (5494,2985) (`px.py row 2986 4700 4980 6 acid1b`: salmon throughout,
`m4.png`); (4455,3415), row y 3406-3427, riser x 4602-4622, row y 3366-3386; and (4455,3635).

Sizes: pull-downs 31-86 wide, loads 25-31 / 52; `tools/t.sh tl4 netlist.py`, t104-t115.

### The bus field's wires and the routing channel, x 4250-4967, y 4300-5790 (traced 2026-11-18, seventh run)

No device. Vertical metal tracks over horizontal poly rows; a track ends on a pad (a poly
square about 38 x 34 with a metal contact) and the pad's row carries the signal on. Views:
`n1_*.png` (1.9x, the channel), `n2_{w1,e1,w2,e2}.png` (3.8x, metal and clean shot),
`n3_pads1.png`, `n3_pads2.png`, `n5_pads3.png`, `n5_pads4.png` (5x mosaics of the 16 pads in
three shots, `tools/tl5_pads.py`), `n4_*.png`, `n6_*.png` (the bus field), `n7_b.png`,
`n7_c.png`, `n8_top.png`, `n9_join.png` (5-8x); overlays `of1.png`-`of6.png`, `of7_r5.png`.

How it was read:
- **Rows.** `tools/px.py col 4560 5436 5720 3 acid,acid1b,metal`: poly (chip-2 stripped shot
  about 150/125/60) at y 5449-5464, 5538-5550, 5583-5592, 5625-5637, 5670-5679, 5712-5720 and
  khaki field (155/150/95) between. The green-rimmed hollow strips that the clean shot shows
  between the rows are that field, bounded by the rows' rims and the metals' protected margins:
  not layout. Edges with `tools/tl4_edges.py col X 5430 5790` at x 4300, 4460, 4560, 4700, 4850
  (outline centres 5446/5468, 5489/5512, 5532/5555, 5576/5599, 5619/5643, 5663/5686,
  5707/5730, 5750/5774). They agree with `tl5`'s rows at x 4967.
- **Where each row runs.** `tools/t.sh tl4 tl5_tracks.py rows row 4150 4980 4 5435 5457 5478
  5500 ... 5783`: the clean shot along every row and between rows, 4 px a character (poly under
  metal, poly in the open, field under metal, other). Every row is unbroken where it is drawn
  and absent where it is not: the row y 5500 is two pieces (west of the pad (4321,5504), east of
  the pad (4625,5504), field between: the khaki box x 4345-4600); y 5545 two (`tla`'s west of
  the pad (4408,5545), this one east of the pad (4497,5547)); y 5675 starts at the pad
  (4411,5676); y 5718 is two (below); y 5761 two (pad (4410,5764) to the corner x 4555; pad
  (4626,5762) east). The rows y 5457, 5585 (`bw`'s) and 5631 cross the whole strip.
- **Metals and contacts.** `tools/follow.py` for each piece's ends and `tools/tl5_tracks.py
  v X Y0 Y1` (metal test in both metal shots; clean-shot red minus green under 24 on the line,
  the hole of a contact): on x 4321 (y 4350-5520) contacts at y 4374 and 5504 only; x 4625
  (y 5250-5520) 5504; x 4497 (y 5520-5740) 5547 and 5720; x 4366 (y 4780-5700) 5114; x 4583
  (y 5240-5780) none; x 4538 (y 4870-5250) 4896; x 4279 (y 2500-5440) 4332, 4570, 4636, 5200,
  5265, 5417 (the hits at 4604 and 5228 are open ground between pieces); x 4319 (y 3380-4262)
  and x 4411 (y 3890-4345) none but the end pads. Horizontal: (4410,5764), (4626,5762),
  (4411,5676). Every pad was then looked at in three shots (ring in the metal, green hole in
  the clean shot, pits in the chip-2 stripped shot): all 16 have a contact.
- **Under RA and RB** the rows are salmon between pink (poly on field under metal): no
  diffusion, no hole, so no gate and no contact (`n2_e1.png`, `n2_e2.png`). RA turns west at
  y 5715-5768 (a block x 4665-4786) and runs on south at x 4665-4718; the rows y 5718 and
  y 5761 pass under the block the same way. The dark specks on RA and RB in the chip-2 metal
  shot at (4761,5630) and (4942,5765) have nothing under them in the clean shot; the mark at
  (4683,5767) on RA's leg is in both metal shots (Ambiguities 10).

The wires (names as the full extraction prints them):

| Net | Path |
|---|---|
| `tl4_w5455` (= `tl5_w5457`) | the strong inverter's row y 5447-5467, from the T at x 4667-4691 west to (4250,5457) and east to (4967,5457), where it is `tl5`'s row to the pad (5538,5457); under seven metals without a contact |
| `tl4_w5068` (= `tl5_w5500`) | the track x 4625's south part ends on the pad (4625,5504); row y 5490-5510 east to (4967,5500): `tl5`'s row to the pad (5493,5500) |
| `tl3_e4372` | row y 5491-5510 from (4250,5500) to the pad (4321,5504); metal x 4321 north, one piece, to the pad (4321,4374); row y 4364-4381 west to (4250,4373): `tl3`'s gate row of the NOR that makes `rcs_mv`. (The other metal on this track, north of a 100 px gap, is `tl3_e4243`'s) |
| `tc1_o3527` (`tl5_w5544`) | row y 5534-5553 from (4967,5543) west to the pad (4497,5547); metal x 4497 south over three rows to the pad (4497,5720); row y 5708-5727 west to (4250,5718). 45 px of bare ground between the pad (4497,5547) and `tla`'s pad (4408,5545) on the same line |
| `tcw_a` (`tl5_w5631`) | row y 5621-5641 from (4967,5631) to (4250,5631), no pad in the strip. On west it reaches `tl3`'s pad (4104,5633) (`of7_r5.png`, 6x, three shots: unbroken under `tl3`'s two metals) |
| `tl4_w4590` (= `tl5_w5674` = `tl3_e5114`) | the track x 4366: south of the pad (4364,4762) a pad (4366,5112) whose row y 5102-5121 runs west to (4250,5112) (`tl3`'s gate 2 of e5), and at the south end an L east onto the pad (4411,5676); row y 5665-5684 east to (4967,5674) |
| `rcs_mv` (= `tl3_e4915` = `rcs_mv`) | `tl3`'s poly in at (4250, 4733-4751), south at x 4276-4292 under the metal x 4279 (no contact), west again along y 4904-4925 out at (4250,4915) into `tl3`'s pad (4234,4918); `tl3`'s metal x 4236 back in along y 5764 to the pad (4410,5764); poly east along y 5752-5772 to a corner at x 4533-4555, north to y 5708, east as the row y 5708-5728 to (4967,5718) |
| `tl4_w3850` (= `tl5_w5761`) | from the inverter's gate metal x 4410 (corner (4412,3852)) south to the pad (4410,4332); row y 4320-4338 west under the track x 4366 to the pad (4279,4332); metal x 4279 south to the pad (4279,4571); an arm east y 4555-4580 onto a poly x 4319-4337 that runs south under the metal x 4321 (no contact) to y 4902; row y 4884-4902 east to the pad (4538,4895); metal x 4538 south, a jog east at y 5236-5250 to x 4583, south to y 5764 and east onto the pad (4626,5762); row y 5752-5772 east to (4967,5762): `tl5`'s line to the bus line x 5412 |
| `tl3_e4635` | row y 4623-4642 from (4250,4633) to the pad (4279,4636); metal x 4279 south to the pad (4279,5200); row y 5189-5207 west to (4250,5198), which is the output row of `tl3`'s inverter at y 5180-5300 (`tl3_e4635_u` there, aliased in `trace/tl4.txt`): latch C's data is NOT `tl3_e5240` |
| `tl3_e5240` | row y 5233-5251 from (4250,5242) ending over the top of the pad (4279,5265); metal x 4279 south to the pad (4279,5413); row y 5403-5422 west to (4250,5412). Enters and leaves west: the row y 5242 is the gate row of `tl3`'s inverter at y 5180-5300, so the signal arrives on the row y 5412 |
| `tl3_e4243` (= `tl4_w3070`) | the track x 4318 from the second latch's data pad (4320,3372) south without a contact to a corner (4318,4247) and west to (4250,4246): `tl3`'s e3 output |

Three metals lie one after another on the track x 4279 (y 4320-4585, 4622-5214, 5251-5427)
and two on x 4321 (to y 4252; y 4360-5518): bare ground between, 25 px or more in both metal
shots (`tl5_tracks.py`). Two polys run under tracks for hundreds of pixels (x 4276-4292
under x 4279, x 4319-4337 under x 4321): salmon under the metal, no ring and no hole on them.

**What decides connections here, and how each was settled:**
- *The pad (4497,5720) and the corner poly x 4533-4555 are apart.* 16 px of field: the pad's
  outline at x 4517-4519, the poly's at x 4533 (`tl4_edges.py row 5718 4380 4660`), khaki between
  in the chip-2 stripped shot, green in the clean one, ground colour in the metal shot
  (`n3_pads2.png`, first tile). If they touched, `tc1_o3527` would be `rcs_mv`.
- *The two under-track polys are apart* (x 4292 to x 4319, pink and green between at every
  level: `n7_b.png`, `of4.png`), so `rcs_mv` is not `tl4_w3850`. The row y 4884-4902 ends on
  the east one (its bottom, y 4902); the west one turns west at y 4904-4925 just below.
- *The row y 5233-5251 and the pad (4279,5265)*: the row ends at x 4300 directly above the
  pad. In the clean shot there is no field between them (`px.py col 4284 5226 5290 3 acid1b`:
  open poly to y 5241, a transition at 5244, pad from 5247; nowhere green), `n9_join.png` 8x.
  The dark line between them in the chip-2 stripped shot is the pad's own outline, which that
  shot shows on every pad even across the side its row enters by. Drawn joined.
- *Every other row meets its pad from the side*, on the pad's own level, with no field between
  (mosaics).

Extraction: `tools/t.sh tl4 netlist.py` 933 nets, 1590 transistors, 0 errors; every file:
2357 nets, 4195 transistors, 0 errors, 0 warnings. `tools/sameconn.py` against the commit
before: the names joined above, the four equations that print another input name, nothing else.

### The tracks' north ends, the knot and the bus lines, x 4250-4967, y 2500-3070 (traced 2026-11-18, eighth run)

No device. Read on `g2_*.png` (3.1x, four shots, y 2740-3070), `g4_*.png` (5.6x, three shots:
the knot), `g5_w.png` and `g8_pads.png` (5x mosaics of eight pads in four shots), `g6_*.png`
(3.3x, the east pads), `g3_top.png` (the bus lines), `g8_col.png` (north of y 2500); overlays
`og1_*.png` to `og5_w.png`. Every metal was followed (`tools/t.sh tl4 follow.py X Y DIR
--trace`) and tested in both chips with a scan for contact holes (`tools/t.sh tl4
tl5_tracks.py v|h ...`): no stretch without metal in both chips except at pad rings and row
edges (under 20 px), and no hole except at the pads below.

**The tracks.**

| Net | Track | North of what was drawn |
|---|---|---|
| `tl3_e4243` | x 4321 | from the pad (4318,3070) north to a corner (4321,2771), east to pad A (4410,2767). `follow.py 4321 2900 N`; `tl5_tracks.py v 4321 2760 3075`: one hole, at y 3070 |
| `tl4_w4590` | x 4366 | one metal from y 4572 north to its end on the pad (4366,2812), over the pad (4366,3030). `tl5_tracks.py v 4366 2795 4575`: holes at y 2815 and y 3031 only |
| `tl4_w3113` | x 4408 | north to a corner (4411,2858), east to pad C (4454,2857). `follow.py 4408 2950 N` |
| `rcs_e3` (`rcs_e3`) | x 4496 | north from the inverter's pad to a corner (4496,2728), west as bus line 6 to `tla`'s pad (4270,2725). `follow.py 4350 2727 E` turns south at x 4496 and ends at (4494,3813); `tl5_tracks.py v 4496 2715 3790`: no hole |
| `tl5_w3245` (`tl4_w4718`) | x 4581 | north from the pair's pad to a corner (4582,2897), east to the pad (4648,2898). `follow.py 4581 3030 N`; `tl5_tracks.py v 4581 2885 4700`: no hole |

**The knot** (pads with a contact: a ring with a bright centre in both metal shots, a green
hole in the clean shot, a cross in the chip-2 stripped shot):

| Pad | Metal | Poly |
|---|---|---|
| A (4410,2767) | the track x 4321's corner piece, from the west | an arm east (y 2759-2776) to x 4468, south at x 4449-4468, east along y 2801-2821 under the track x 4496 to pad B |
| B (4583,2811) | east along y 2812 to the pad (4866,2812) | the link from A; nothing east of the pad |
| (4866,2812) | from B | a row east to x 4967: `tl5`'s row y 2801-2820 (`tl5_w4458`) |
| C (4454,2857) | the track x 4408's corner piece | a link east (y 2847-2864) under the track x 4496 to pad D |
| D (4538,2857) | east along y 2857 to the pad (4823,2855) | the link from C |
| (4823,2855) | from D | a row east to x 4967: `tl5`'s row y 2846-2865 (`tl5_w2855`) |
| E (4539,2768) | east along y 2771 to `tl5`'s pad (4910,2767), the top of `tl4_w4068`'s metal | a column x 4534-4550 north under the six bus lines and across y 2500; it goes on under the wide band to y ~2165 (`g8_col.png`) |
| (4648,2898) | the track x 4581's corner piece | on the row y 2890-2909, which runs east to x 4967 (`tl5`'s row); nothing west of the pad |
| (4366,2812) | the north end of the track x 4366 | a row west, y 2801-2820, across x 4250 |
| (4366,3030) | the track x 4366 passes | a row west, y 3018-3038, across x 4250: `tl3_e3028` |

The track x 4496 crosses both links (A-B and C-D) and the track x 4321 both rows of
`tl4_w4590` without a contact. The clean shot is covered by debris at x 4560-4690,
y 2770-2900 (pad B, the three metals east of the knot, the pad (4648,2898)): there the
reading is from the two metal shots and the chip-2 stripped shot.

**The bus lines** (metal, 13-20 px wide, pitch 43; each steps down one pitch on a 45-degree
diagonal, the diagonals 25 px further west from line to line; placed by `tl5_tracks.py v X
2495 2745` at ten columns x 4560-4740):

| Line | West | Diagonal | East end |
|---|---|---|---|
| 1, `tl4_w2512` | across x 4250 at y 2512 | (4669,2512)-(4712,2555) | pad (4908,2551), row y 2542-2560 east across x 4967. The pad's metal ends 25 px short of the wide vertical supply metal x 4950-4995 (`tl5_tracks.py h 2551 4700 4965`: no metal at x 4911-4949 in either chip) |
| 2, 3 | `r9m`'s (`ra_eq_r9`'s line and `r9m_l3`) | | pads (4867,2596), (4912,2641) |
| 4, `tl5_w4937` | pad (4279,2640), whose poly row comes from the west across x 4250 (y 2632-2650) | (4604,2641)-(4647,2684) | pad (4866,2681), row y 2675-2694 = `tl5`'s |
| 5, `tl5_w2722` | across x 4250 at y 2685 (the metal starts on a pad (4236,2683) in `tl3`'s strip, whose row goes on west: `og5_w.png`) | (4580,2685)-(4622,2727) | pad (4822,2723), row y 2714-2733 = `tl5`'s |
| 6, `rcs_e3` | `tla`'s pad (4270,2725) | none: it turns south at x 4496 | the track x 4496 |

**What it joins** (`.venv/bin/python tools/sameconn.py b4454bb`: only these joins; no
transistor's own nets change otherwise). No gate's logic changed; nine merged equations print
another name for one net:

| Join | Equations that print differently |
|---|---|
| `rcs_e3` (`tla`'s bus line E; this file's inverter output, formerly a placeholder) | `rcs_e3` = NOT `tl4_w3850` (was printed under the placeholder): the input `rcs_e3` of `rcs_in3` and `rcs_bc3460` has its driver |
| `tl4_w4590` = `tl3_e3028` | `tl3_w3373` = NOT `tl4_w4590` (was NOT `tl3_e3028`) |
| `tl4_w4718` = `tl5_w3245` | `tl4_w4686` = NOT(`tl4_w4590` AND `tl5_w3245` OR `tl4_w4850`); `tl5_w3245` = NOR(`tl5_w3550`, `tl5_w4160`) is unchanged |
| `tl3_e4243` = `tl5_w4458` | `tcw_c` = NOT(`tcw_m6232` OR `tl3_e4243` AND `tl5_w4318` OR `tl5_w4503`); `tl5_w4503` = NOT(`tcw_c` OR `tcw_m6320` AND `tl3_e4243`) (both had `tl5_w4458`) |
| `tl4_w3113` = `tl5_w2855` | `tl5_w2722` = NOT `tl4_w3113` (was NOT `tl5_w2855`) |

So `tl5`'s latch c is open while `tl3_e4243` = NOR(`rcs_mv`, `tcw_a`) is high, the same signal
that is the data of the second latch here and an input of the top NOR.

### South of the routing channel, x 4250-4967, y 5790-6350 (traced 2026-11-18, ninth run)

No device, no diffusion: an open field (x 4250-4660, y 5990-6130) and poly rows under metals.
Read on `h1_m.png`, `h1_a.png` (1.8x, whole area, every package's shapes), `h2_e.png` (3.1x,
metal and clean shot), `h2_s.png` (the row y 6323), `h3_pads.png` (5x mosaic of the three pads
and the thin metal's corner, four shots); overlays `oh1.png`, `oh2.png`, `oh3.png`.

| Net | What | Evidence |
|---|---|---|
| `rcs_x1` (`tl3_e4808`, `rcs_x1`) | `tl3`'s metal crosses x 4250 at y 5889-5901 and runs east to the pad (4629,5891); the pad's row (y 5880-5900) runs east under the legs of RA and RB and under RC's turned rail to x 4967 = `tl5`'s row to its bus line x 5107 | `tl5_tracks.py h 5893 4250 4640`: no stretch without metal over 15 px, one hole, at x 4626; `px.py col 4400 5870 5950 3 metal,acid1b`: metal y 5888-5902; pad: ring with a bright centre in both metal shots, green hole in the clean shot, nothing west of it in poly |
| `tl5_w5936` | a metal from the west along y 5939 (y 5933-5945) to the pad (4583,5936); row (y 5926-5946) east to x 4967 = `tl5`'s row to its bus line x 5063 | `tl5_tracks.py h 5935 4250 4600`: one hole, at x 4583; `oh3.png`: the metal goes on west of x 4250 |
| `tl5_w4590` | `tl5`'s thin metal (the clear of its latch c) enters at (4967,5984), turns south at x 4929 (x 4922-4936), has a contact on the pad (4929,6323) and runs on south across y 6350; the pad's row (y 6313-6333) runs west across the whole strip and x 4250, nothing east of the pad | `tl5_tracks.py v 4927 5975 6340`: no stretch without metal in both chips over 16 px, one hole, at y 6326; `px.py col 4600 6296 6344 3 acid1b`: row y 6314-6332; `tl5_tracks.py h 6320 4250 4930`: no metal along the row (poly) |
| RA (vss) | the leg x 4667-4715 from the block at y 5715-5768 south across y 6350 | `px.py row 6050 4650 4960 3 metal` |
| RB (vcc) | from the rail (x 4906-4950) west along y 5806-5856 to x 4754, south as a leg x 4754-4801 across y 6350. The horizontal piece lies on `tla`'s row y 5838-5858 for 200 px without a contact (the dark line at y 5835-5838 in the metal shots is the row's north edge under the metal: review round 10) | `px.py col 4850 5796 5866 3 metal1,acid1b`: chip-1 metal bright at y 5808-5832 and 5841-5850, the row cream (under metal) in the clean shot, against dark red (open) at x 4735; `tl5_tracks.py h 5826 4750 4960`, `v 4778 5800 6350`: no hole |
| RC (vss) | `tl5`'s rail RC, turned west along y 5891-5942, turns south at x 4841-4888 across y 6350; no contact to the rows y 5890 and y 5936 under it | `px.py row 5915 4830 4966 4 metal,metal1`; `px.py col 4910 5868 5952 3 metal,metal1,acid1b` (top edge y 5891: review round 10); `tl5_tracks.py v 4866 5880 6350`: no hole |

The clean-shot scan lists a weak mark at y 6043-6045 on all three legs (red minus green about
0 at a red of 174-193): the centre of each wide leg is grey-olive there over its whole length
(`px.py col 4692 6032 6056 3 acid1b`: 151/142/110 at every sample), not a hole.
`.venv/bin/python tools/sameconn.py 83d70d4`: the only names joined are `rcs_x1`'s net and
`rcs_x1`; no equation differs.

### RA's supply, x 4732-4967, y 2500-3004 (traced 2026-11-18, tenth run)

Read on `g7_sup.png` (2.1x, every package's shapes), `i1_foot.png` (4.1x, metal and clean
shot); overlay `oi1.png`.

- **The foot**: a wide metal along y 2938-2997 (north edge: Ambiguity 12, review round 11) from x 4732 east across x 4967.
  `tl5_tracks.py h 2962 4732 4967` and `h 2985 4732 4967`: metal in both chips at every sample,
  no hole. It lies on the rows y 2976-2996 (`tl5_w3505`) and y 2930-2950 (`tl4_w4198`) without a contact.
- **The foot runs into RA.** RA's metal (x 4729-4775, drawn from y 3000) is the foot's
  continuation south: `px.py col 4752 2925 3030 3 metal,metal1,acid1b` has metal in both chips
  from y 2958 to y 3009 except two dark lines of 6 px, at y 2973-2976 and y 2994-2997, which
  are the north and south edges of the row y 2976-2996 under the metal (the same in both);
  the clean shot at x 4729-4775 is pink (field that was under metal) on both sides of the row,
  y 2950-2975 and y 2998-3010, while east of x 4781 it is open field south of the row
  (`px.py row 3004 4718 4790 4 metal,metal1,acid1b`: metal x 4734-4778). Against that, RB's top
  end (y 3020) is 23 px of bare ground south of the foot. Drawn with a joint rectangle
  (4732-4775, 2990-3004).
- **The vertical**: x 4949-4995 (west edge `px.py row 2700 4930 4966 3 metal,metal1`: bright
  from x 4951), from the foot north to the band; its east part is in `tl5`'s strip.
  `tl5_tracks.py v 4958 2500 3000`: stretches without metal in both chips of 8-14 px at every
  row edge (the rows of the bus lines' pads and of the knot cross under it), none longer; no
  hole (the mark at y 2995 is the green rim of the foot's south edge in the clean shot). The
  pad (4908,2551) of bus line 1 ends 25 px short of it (eighth run).
- **The band's corner**: the band north of y 2500 comes down to y 2507 for x 4910-4948
  (`px.py col 4930 2488 2530 3 metal,metal1`, `px.py row 2507 4880 4966 4 metal,metal1`).

`.venv/bin/python tools/sameconn.py f3357ad`: `connections identical` (the new metal joins
only RA's net, which already has the name vss).

## Ports

The wires drawn to the strip's edges (the same list is `ports.d/tl4.txt`; `tools/ports.py
--prefix tl4`: every east port meets `tl5`'s at 0 px, the west ones `tl3`'s where it has one):

| Name | Layer | Where | Dir | What |
|---|---|---|---|---|
| `tl3_e4243` | metal | (4250, 4236-4256) | in | `tl3`'s e3 output on the track x 4318 (alias `tl4_w3070`): the second latch's data, the top NOR's gate 1 |
| `tl3_e4372` | poly | (4250, 4364-4381) | ? | the row of the pad (4321,4374): `tl3`'s gate row |
| `tl3_e4372` | poly | (4250, 5491-5510) | ? | the row of the pad (4321,5504), the other end of the same metal: on west, not followed |
| `tl4_w4501` | poly | (4250, 4492-4512) | in | gate 2 of the three-input NOR |
| `tl3_e4635` | poly | (4250, 4623-4642) | ? | the row of the pad (4279,4636): `tl3`'s latch C data |
| `tl3_e4635` | poly | (4250, 5189-5207) | in | the row of the pad (4279,5200), the other end: `tl3`'s inverter output (`tl3_e4635_u`) |
| `rcs_mv` | poly | (4250, 4733-4751) | in | from `tl3`'s pad (4192,4743) |
| `rcs_mv` | poly | (4250, 4904-4925) | out | into `tl3`'s pad (4234,4918) |
| `rcs_mv` | metal | (4250, 5754-5774) | in | `tl3`'s metal x 4236 along y 5764 |
| `tl4_w4590` | poly | (4250, 5102-5121) | ? | the row of the pad (4366,5112): `tl3_e5114` |
| `tl3_e5240` | poly | (4250, 5233-5251) and (4250, 5403-5422) | ? | both ends of the loop on the track x 4279: the north one is `tl3`'s inverter's gate row, the south one goes on west |
| `tl4_w5455` | poly | (4250, 5447-5467) | out | the strong inverter's row, on west, not followed |
| `tcw_a` | poly | (4250, 5621-5641) | ? | the row y 5631, on west to `tl3`'s pad (4104,5633) |
| `tc1_o3527` | poly | (4250, 5708-5727) | ? | the row of the pad (4497,5720), on west, not followed |
| `tl4_w2512` | metal | (4250, 2506-2518) | ? | bus line 1, on west |
| `tl5_w4937` | poly | (4250, 2632-2650) | out | the row of the pad (4279,2640), the west end of bus line 4, on west |
| `tl5_w2722` | metal | (4250, 2679-2691) | out | bus line 5; it starts on a pad (4236,2683) in `tl3`'s strip |
| `tl4_w4590` | poly | (4250, 2801-2820) | ? | the row of the pad (4366,2812), the north end of the track x 4366, on west |
| `tl4_w4590` | poly | (4250, 3018-3038) | out | the row of the pad (4366,3030): `tl3_e3028`, the gate of `tl3`'s inverter E1 |
| `tl4_w4068` | poly | (4534-4550, 2500) | ? | the column north of pad E (4539,2768), on north under the wide band |
| `tl4_w2512` | poly | (4967, 2542-2560) | ? | the row of the pad (4908,2551), the east end of bus line 1 |
| `tl5_w4937` | poly | (4967, 2675-2694) | in | the row of the pad (4866,2681), the east end of bus line 4: `tl5`'s inverter 2 output |
| `tl5_w2722` | poly | (4967, 2714-2733) | in | the row of the pad (4822,2723), the east end of bus line 5 |
| `tl3_e4243` | poly | (4967, 2801-2820) | out | the row of the pad (4866,2812): `tl5_w4458`, the enable of `tl5`'s latch c |
| `tl4_w3113` | poly | (4967, 2846-2865) | out | the row of the pad (4823,2855): `tl5_w2855` |
| `tl5_w3245` | poly | (4967, 2890-2909) | in | the row of the pad (4648,2898): `tl4_w4718`, from `tl5`'s NOR |
| `rcs_x1` | metal | (4250, 5889-5901) | in | `tl3`'s metal of its latch C's clear (`tl3_e4808`), to the pad (4629,5891) |
| `tl5_w5936` | metal | (4250, 5933-5945) | ? | the metal of the pad (4583,5936), on west |
| `tl5_w4590` | poly | (4250, 6313-6333) | ? | the row of the pad (4929,6323), on west |
| `rcs_x1` | poly | (4967, 5880-5900) | out | the row of the pad (4629,5891): `rcs_x1` |
| `tl5_w5936` | poly | (4967, 5926-5946) | ? | the row of the pad (4583,5936) |
| `tl5_w4590` | metal | (4967, 5977-5991) | ? | `tl5`'s thin metal, in along y 5984 |
| `tl5_w4590` | metal | (4922-4936, 6350) | ? | the same metal, on south past the pad (4929,6323) |
| `vss` | metal | (4667-4715, 6350) | - | RA's leg, on south |
| `vcc` | metal | (4754-4801, 6350) | - | RB's leg, on south |
| `vss` | metal | (4841-4888, 6350) | - | RC's leg, on south |
| `vss` | metal | (4967, 2938-2997) and (4949-4967, 2500) | - | RA's supply: the foot, on east, and the vertical x 4949-4995, on north to the band |
| `tl5_w3505` | poly | (4967, 2976-2996) | in | the second latch's enable |
| `tl4_w5455` | poly | (4967, 5447-5467) | out | `tl5_w5457` |
| `tl4_w5068` | poly | (4967, 5490-5510) | out | `tl5_w5500` |
| `tc1_o3527` | poly | (4967, 5534-5553) | in | `tl5_w5544` |
| `tcw_a` | poly | (4967, 5621-5641) | ? | `tl5_w5631` |
| `tl4_w4590` | poly | (4967, 5665-5684) | ? | `tl5_w5674` |
| `rcs_mv` | poly | (4967, 5708-5728) | out | `rcs_mv` |
| `tl4_w3850` | poly | (4967, 5752-5772) | in | `tl5_w5761` |

The tracks, as far as each is drawn:

| Name | Track | Followed (`tools/follow.py`, not looked at) |
|---|---|---|
| `tl3_e4243` (`tl4_w3070`) | metal x 4318 | north of the pad (4320,3070) to a corner (4321,2771) and east to pad A (4410,2767) (eighth run); from the pad (4320,3070) south through the pad (4320,3372), the second latch's data row, to a corner (4318,4247) and west out of the strip at (4250,4246): drawn whole |
| `tl4_w3178` | metal x 4410 | from the pad (4413,3178) south to the pad (4413,3592), the second latch's output row: drawn whole |
| `tl5_w3505` | metal x 4452 (north piece) | from the pad (4452,2985) south through the pad (4455,3415) to the pad (4455,3635): drawn whole, with the row east from the north pad to the strip's edge |
| `tl4_w3245` | metal x 4680-4707 | from the pad (4690,3247) to the pad (4690,3703): drawn whole; it passes over two heavy boxes, (4684,3420) (Ambiguities 4) and the buried contact at y 3593, with no contact |
| `tl4_w3390` | metal x 4851-4881 | from the plate's contact (4863,3390) to the pad (4863,3612): drawn whole |
| `tl4_w3113` | metal x 4408 | from the pad (4410,3113) north to a corner (4411,2858), east to pad C (4454,2857): drawn whole (eighth run) |
| `rcs_e3` (`rcs_e3`) | metal x 4496 | from the pad (4495,3808) north to a corner (4496,2728), west to `tla`'s pad (4270,2725): drawn whole (eighth run) |
| `tl4_w3850` | metal x 4410 | from the corner (4412,3852) south to the pad (4410,4332), and on by the wire in the table of the seventh run to (4967,5762): drawn whole |
| `tl4_w4025` | metal x 4452 | from the pad (4455,4025) south to the pad (4455,5197), the inverter's output row: drawn whole (`y1.png`, `y2.png`) |
| `tl4_w4068` | metal x 4625 | north of the pad (4625,4068) to a corner (4630,2988), east and north to `tl5`'s pad (4910,2767) (`tl5`'s drawing), and from that pad west along y 2771 to pad E (4539,2768) (eighth run) |
| `tl4_w4198` | metal x 4537 | y 2938 to y 4814, where it ends on gate 3's pad of the pair (4537,4808); candidates (4538,3782), (4540,4215); the pad (4540,3462) is the second latch's clear row. Drawn y 3440-4816 |
| `tl4_w4243` | metal x 4496 | from the pad (4490,4243) south to a corner at y 5327 and east onto the pad (4537,5325), the strong inverter's gate row: drawn whole (`y1.png`, `y2.png`) |
| `tl4_w4590` | metal x 4362-4366 | y 2802 to y 5682 through the pads (4366,2812), (4366,3030), (4364,4590), (4364,4762) and (4366,5112), ending on the pad (4411,5676): drawn whole (eighth run) |
| `tl4_w4545` | metal x 4626 | from the pad (4620,4545) south to the pad (4623,4893): drawn whole |
| `tl5_w3245` (`tl4_w4718`) | metal x 4581 (north part) | from the pad (4580,4718) north to a corner (4582,2897), east to the pad (4648,2898) on `tl5`'s row y 2900: drawn whole (eighth run) |
| `tl4_w4850` | metal x 4581 (south part) | from the pad (4580,4850) south to the pad (4583,5108), the NOR's gate 2: drawn whole |
| `tl4_w4545` (poly) | poly x 4619-4643 | from the pad (4623,4893) south past gate 5's row, then east as the row y 5011-5033, the NOR's gate 1: drawn whole |
| `tl4_w5068` | metal x 4625 (south part) | from the pad (4625,5068) south through the pad (4625,5240) to the pad (4625,5504), whose row runs east out of the strip: drawn whole |
| `tl4_w5455` | poly row y 5447-5467 | from the T under the strong inverter (x 4667-4691) east and west across the whole strip: drawn whole |

## Ambiguities

1. **The two load ties are `tl1`'s `?` items** (in the cells; here at (4801-4821, 4186-4216) and
   (4806-4834, 4065-4086)). Until one is read, the cross-coupling is an assumption, here as in
   `tl1` (AMB-026).
2. **The supplies of RA and RB** are named from structure only.
3. A copy checked by overlay at 4x and 2.5x; the cells' small items (the third pull-down's
   diffusion to the VSS box, the gate caps) were not each measured here.
4. **The heavy box at (4684,3420) under the metal of `tl4_w3245`** (second latch): inner box
   (4677-4698, 3408-3432) in nested outlines, against the west edge of the node `tl4_w3390`'s
   diffusion. Both metal shots show a bright centre about 12 px across (x 4677-4689,
   y 3414-3426) in a dark ring (x 4662-4704, y 3403-3438) (`tools/textmap.py 4662 3396 4712 3446
   3`), which I first drew as an uncertain contact on an uncertain poly pad. Review round 7:
   **not a contact**. The clean shot has no hole there (centre 203/176/131, against
   161-178/180-193/98-108 in the four real poly contacts of the two metals), the chip-2
   stripped shot no pits; in both stripped shots it is the same kind of object as the
   buried-contact box at (4673-4709, 3578-3607), over which chip 1's metal shot shows the same
   bright centre (`textmap.py 4662 3572 4712 3614 3`: chip 1 A-E at x 4680-4689, y 3587-3599);
   the "widening" west of the metal is the box's outline (dark, not metal). Its boundary to
   the node's diffusion is one weak line. Drawn now as an uncertain lobe of the node's
   diffusion (`?D 4662,3404:4703,3438`), with no contact. No poly was seen leaving it (pink
   field at (4680-4686, 3396-3399) towards the enable row, rows y 3438-3444 read 0-3 towards
   the clear row), so what it is for is not known. **If it were a contact of the metal, it
   would short `tl4_w3245` to `tl4_w3390`** (the node would gate its own pull-down and carry two
   loads): anyone who re-reads it as one must explain the rest of the latch.
5. **The field box (4722-4752, 3442-3488) in the row y 3452-3472** may be a substrate contact of
   RA (elongated ring in both metal shots, bright sliver x 4740-4748). Not drawn. Either way
   there is no poly and no diffusion in it, which is what makes the row two nets.
6. **In the second latch the load ties carry signals**: each cross-coupling gate and the
   inverter's output are taken from a load's plate, so the three equations hold only if each
   plate is tied to its node (the three `?` ties: heavy boxes at (4838-4872, 3330-3360),
   (4801-4826, 3388-3410) and (4801-4826, 3518-3547)). A depletion load needs the tie, and
   nothing else is on these plates but the contacts and rows drawn; but the three boxes were
   placed from outlines at 6x, not measured (AMB-026).
7. **Read from outlines only** in the second latch: the J-shaped diffusion from the lower
   node's east column to VSS box 3 (between two heavy lines, x 4818 and x 4840, in the chip-2
   stripped shot); the junctions hidden by the dark line of the gap between the two metals
   (x 4714-4726: the west columns onto the stack and onto VSS box 2, taken as joined because
   the line looks the same at every diffusion level and there is no green field in the gap
   there); the band from the node `tl4_w3390` east across RA's edge line (x 4790-4797) to the
   load. A small ring at (4868,3435) on the metal of `tl4_w3390` lies over the load's channel and
   has no hole in the clean shot: not drawn as a contact.
8. **The row y 5233-5251 onto the pad (4279,5265)** (`tl3_e5240`): the row ends over the pad's
   top edge instead of entering it from the side. No field between them in the clean shot;
   one dark line in the chip-2 stripped shot, taken as the pad's outline (above). Drawn joined,
   without `?`. If it were not, the pad would have a metal and no poly leaving it.
9. **`tcw_a` and `tl3_e4152`**: the row y 5621-5641 is drawn here from x 4250 and by `tl3` up
   to x 4160; the 90 px between are in `tl3`'s strip and look unbroken (`of7_r5.png`).
   **Closed**: `tl3`'s run 9 drew them, so `tcw_a` is track A, `tl3_e4152` and `tl4_w4501`
   (gate 2 of the three-input NOR here).
10. **Marks on the metals that are not drawn as contacts.** (4536,4992) on the metal x 4538
   (field under it) and the specks at (4761,5630) on RA and (4942,5765) on RB are in the chip-2
   metal shot only. **The mark at (4683,5767) on RA's leg is in both metal shots** (review round
   8; `px.py row 5766 4670 4700 3 metal,metal1,acid1b`: dark at x 4679-4688 in both, 62/33/17
   and 91/66/41), right over the row y 5752-5772 of `tl4_w3850`. Neither stripped shot has a
   hole, a pad or pits there (the clean shot is uniform salmon, 204-227/157-173/107-125, along
   the row), so it is not drawn. What it is is not known. If it were a contact it would tie
   `tl4_w3850` (and with it `tl5_w5761`) to RA.
11. **Under the debris of the clean shot (x 4560-4690, y 2770-2900)** the clean shot cannot
   show whether the three metals east of the knot (y 2771, 2812, 2857) have a contact:
   `follow.py` lists candidates at (4650,2771), (4657,2815) and (4640,2858), all inside the
   debris. Neither metal shot has a ring on those metals between their end pads, and the chip-2
   stripped shot has no pad or poly under them there (`g2_acid.png`, `g2_metal.png`,
   `g2_metal1.png`): none drawn. Pad B (4583,2811) and the pad (4648,2898) are under the
   debris too: both read from the two metal shots (ring, bright centre) and the chip-2 stripped
   shot (pad with a cross) (`g8_pads.png`).
12. **The foot's north edge** (RA's supply): first drawn at y 2955, as `tl5` has it, because the
   two-chip metal test fails along y 2946 for most of x 4749-4947 (`tl5_tracks.py h 2946 4690
   4967`). **Settled in review round 11: y 2938**, the row y 2930-2950 (`tl4_w4198`) is under
   the metal. `px.py row 2946 4704 4760 4 metal,metal1,acid1b`: the metal's west edge line is
   at x 4728-4731, as on y 2965; west of it open orange poly (clean shot dark, 80-110 red),
   east of it yellow metal in both chips and salmon in the clean shot (220/170/120); the
   outline's top-left corner is at (4730,2938) in both chips (`i1_foot.png`, the reviewer's
   `r1_ratop.png`). The metal test fails there because only about 6 px of clear metal lie
   between the row's edge line and the metal's own. No contact on that row
   (`tl5_tracks.py h 2945`: no hole), so nothing is joined.

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

### Round 6: full review of the NOR and the two inverters (2026-11-17, commit dd64e0f, images `review-6/`)

Covered: the three pieces at x 4437-4967, y 4990-5465 (one batch: 7 transistors). Told to
suspect: in the NOR, the pad (4583,5108) and the end of the track x 4581, the L of
`tl4_w4545`'s poly, the pad (4625,5068) and its buried contact, row 2's east end against the
tail, a third gate; in the inverter, the overlay of the copied body, the two long tracks
(x 4452, x 4496) and the output row's way under three metals; in the strong inverter, the
diffusion between x 4853 and the plate, the leg east of RA, the column west of RA, the corner
of the track x 4496 on the pad (4537,5325) beside the metal x 4583, the T into the row
y 5445-5465, and the dark spots on RA. Checked with 15 images (4.2x to 6x, `acid`, `acid1b`,
`metal`, the master of the inverter beside the copy) and with `px.py`, `textmap.py`,
`follow.py`, `railprof.py`, `tla_contacts.py`, `opendiff.py`, `unsure.py`.

Found correct: every item of the list. In particular: the track x 4581 is one metal from the pad
at y 4850 and ends on the pad (4583,5108); the metal x 4625 has contacts only at y 5068, y 5240
and its end pad (4627,5503); row 2's end abuts the tail's west edge and does not cross it; no
third gate; the copied body fits in both stripped shots; the tracks x 4452 and x 4496 are
straight with no pad or contact from y 4395 to their south ends; the output row has no contact
under the metals x 4496, x 4537 and x 4625; the corner of x 4496 lands on the pad (4537,5325)
with 15 px of bare ground to the metal x 4583 in both chips; diffusion edges cross the plate at
y 5306 and y 5376 (`px.py col 4888`), so the lower load is the wide transistor drawn; the leg
east of RA is outlined in three shots; the T has no line across it; the dark spots (4768,5195),
(4758,5337), (4755,5393) on RA and (4932,5285) on RB are not contacts.

Findings, both geometry only, both confirmed and fixed:
1. The upper inverter's arm `D 4666,5186:4728,5223`: next to RA the diffusion is only
   y 5205-5219 (my check: `px.py col 4714 5176 5230 3 acid1b,acid`, field to y 5185, edge
   y 5188-5200, diffusion y 5209-5217, edge y 5221). Drawn now as the box part to x 4708 and a
   neck y 5203-5223 to RA.
2. The upper inverter's tie box: the photo's box is about 4847-4875 x 5250-5283, against
   `?B 4832,5242:4880,5278`. Moved to `?B 4840,5244:4879,5282` with its `?P`.

`tools/t.sh tl4 sameconn.py dd64e0f`: `connections identical`.
`.venv/bin/python tools/sameconn.py dd64e0f`: `connections identical`.

Not checkable (reviewer): the three load ties (`?`, AMB-026: all the new equations stay
marked); whether the west columns join the diffusion under RA (RA's edge line hides x 4722-4732
in every shot; the reading does not depend on it); the leg's top and the 17 px strip west of
the lower plate by colour (read from outlines); the long tracks were looked at at 2.7x in the
chip-2 metal shot and otherwise with the text tools; the NOR's first input still rests on the
earlier `?P 4620,4908:4642,4924`.

Round 6: no findings that change a connection.

### Round 7: full review of the second latch (2026-11-18, commit cf49979, images `review-7/`)

A fresh reviewer (Fable 5.2), briefed with the claims (the three equations, every row with its
pad and track, each diffusion and plate, the two strap metals with their four contacts, the
three ties, the enable row to the strip's edge) and told to suspect: the ring at (4684,3420);
whether the row y 3452-3472 is two polys and what the box (4722-4752, 3442-3488) is; the
vertical poly east of RA and its band; the diffusion across the gap between the two metals; the
row y 3587-3610 and the J; the ties and the plates' other connections; the buried contact at
y 3593 and the follower's contact candidates on the strap; the enable row y 2976-2996 and the
metals over it; which rows are gates over which diffusions; anything left out. 20 images
(4.8x and more, the three shots and chip 1's metal), profiles and text maps.

Checked and found correct: two polys in the row y 3452-3472, the box is field; diffusion
crosses the metal gap at y 3356, 3412, 3420, 3496, 3612, 3655 (thin dark bar; the field gaps at
y 3482, 3520, 3552, 3590 read green); no poly crosses RA at y 3587-3610, the J is diffusion
into the third VSS box, no way round either gate end; the box at y 3593 is a buried contact;
the strap x 4680-4707 is one metal and the candidates y 3439, 3499, 3619, 3676 are edges
underneath; the east strap has only its two contacts and (4868,3435) is a blemish of chip 2;
the enable row is continuous to x 4967 with no taps; the node's band is continuous across RA's
edge; all four rows cross their diffusions fully; the five bus-field pads are real contacts,
no taps at the track crossings; RA has only its three VSS contacts; nothing undrawn
(`opendiff.py`). All eleven transistors and the three equations stand.

Findings, none changing a connection, all confirmed and fixed:
1. (4684,3420) is not a metal contact on a poly pad (Ambiguities 4 has the evidence; my check:
   `textmap.py 4662 3572 4712 3614 3` shows chip 1's bright centre over the y 3593 box too, and
   my own profiles had found no hole). The `?P` pad and `?C` were joined to nothing; replaced by
   `?D 4662,3404:4703,3438`, a lobe of the node's diffusion, no contact.
2. The clear row's west piece ends at x 4724, not 4718 (`px.py row 3462`: salmon to x 4720).
3. The inverter's band under the vertical gate reaches y 3320, not 3314 (`px.py col 4800 3272
   3332 3`: edges at y 3281-3284 and y 3317-3323). Drawn y 3283-3320 west of x 4832.
4. The second VSS box's west edge below y 3510 is x 4724, not 4705 (`px.py row 3520 4696 4736
   3`: pink to x 4708, green, tan from x 4729).
5. The row y 3587-3610 ends at x 4788, not 4797 (`px.py row 3598 4770 4812 3 acid1b,acid`).

`tools/t.sh tl4 sameconn.py cf49979`: `connections identical`.
`.venv/bin/python tools/sameconn.py cf49979`: `connections identical`.

Not checkable (reviewer): the three ties (each a heavy-outlined box at the drawn place; poly
over diffusion inside not resolvable: `?` stays, Ambiguities 6); the junction of the data row
with the vertical poly x 4788-4812 lies on RA's edge line (indirect evidence only: no field
colour between them in the clean shot, one continuous south edge).

Round 7: no findings that change a connection.

### Round 8: full review of the bus field's wires and the routing channel (2026-11-18, commit 90ec4f2, images `review-8/`)

Told to suspect: the join of the row y 5233-5251 to the pad (4279,5265); the separation of the
pad (4497,5720) from the corner poly x 4533-4555; the two polys under the tracks x 4279 and
x 4321 (poly or not, contacts to the metal above, their ends, their separation, the place where
the row y 4884-4902 ends beside the west one's turn); whether each metal is one piece between
its pads with no tap; the ring at (4536,4992); rows passing under a neighbouring track or under
RA's block; which side each row leaves its pad.
Checked at 4-6x in four shots with `px.py`, `textmap.py`, `tl5_tracks.py` (both chips), row
maps, the extraction, `sameconn.py`, `ports.py` (17 images).

- Geometry only, confirmed, fixed: both under-track polys were drawn about 6 px too wide on
  the west. `px.py row 4700` and `row 4820 4262 4344 3 acid1b`: the east one is cream at
  x 4322-4334 with pink at x 4313-4319, the west one cream at x 4277-4289. Now
  `P 4319,4555:4337,4902` and `P 4276,4733:4292,4925` (the gap between them is wider than drawn).
- Comment only, confirmed, recorded (Ambiguities 10): the mark at (4683,5767) on RA's leg is in
  both metal shots, not chip 2 only as the notes said; no hole, pad or pits under it in either
  stripped shot. Not a contact as far as the photos show; what it is is not known.
- Found correct: the row y 5233-5251 joins the pad (4279,5265) (no green or khaki between in
  the clean shot, one outline in the metal shot; the chip-2 stripped shot's dark line, minimum
  84/45/31, is like the one across the side entry of the pad (4411,5676), 73/28/20); the pad
  (4497,5720) and the corner poly are apart (ground colour at x 4520-4531 in four shots), and
  the corner stops short of the metal x 4583; no contact hole on either under-track poly
  (scans at x 4274, 4279, 4284, 4321, 4327), their ends at y 4557/4905 and y 4731/4927, field
  between them at every level including (4293-4320, 4880-4930); the arm from the pad
  (4279,4571) is poly in four shots; the east poly is 8-10 px clear of the pads (4364,4590) and
  (4364,4762); every metal is one piece with no tap, the gaps on the tracks x 4279, 4321, 4411,
  4538 and 4583 are bare for 37-120 px; the corner (4318,4247) reaches `tl3`'s pad; all 17 pads
  have ring, hole and pits and their rows leave on the stated sides; the rows run as drawn, none
  steps under RA or RB, no contact at any crossing (also under the neighbours' tracks x 4409,
  4453, 4496, 4236); RA's block and leg as drawn, no diffusion under the rails; the hollow
  strips are field; nothing left untraced in the region. Extraction 0 errors both ways; the
  connection differences against the commit before are the joins claimed; the east ports meet
  `tl5`'s at 0 px.
- Could not be checked: the chip-2 stripped shot under RA and RB (fringes only: "no contact"
  there rests on the clean shot and the two metal shots); the rows west of x 4250.

After the fixes: `tools/t.sh tl4 sameconn.py 90ec4f2` ends `connections identical`;
`.venv/bin/python tools/sameconn.py 90ec4f2` ends `connections identical`.

After the round, on merging main (2026-11-18 12:46): `tl3`'s run 8 had meanwhile drawn two rows
up to x 4250 that are the west ends of two wires of this piece, the row y 5231-5250
(`tl3_e5240`, the gate of its inverter at y 5180-5300) and the row y 5190-5205 (`tl3_e4635_u`,
that inverter's output, which `tl3`'s notes take to this strip's pad (4278,5198) and metal
x 4279 as an open join). No geometry of this piece changed: the wire named `tl4_w5243` in the
reviewed commit is now labelled `tl3_e5240`, and `@alias tl3_e4635 tl3_e4635_u` was added; both
rows were in the round's claims 9 and 10 and were found to run to x 4250 as drawn.
`tools/sameconn.py origin/main` lists, beyond the joins of this piece, only `tl3_e4635` +
`tl3_e4635_u` on one net (`tl3_e4635` = NOT `tl3_e5240`).

Round 8: no findings that change a connection.

### Round 9: full review of the tracks' north ends, the knot and the bus lines (2026-11-18, commit d737383, images `review-9/`)

A fresh reviewer (Claude Fable 5.2), 2026-11-18 15:20 -0600. One piece: the section "The tracks' north ends,
the knot of pads y 2740-2910 and the bus lines y 2500-2740" of `trace/tl4.txt` (x 4250-4967,
y 2500-3070, and the tracks it extends south to y 4700). It was given the thirteen claims
(five tracks, the knot's pads and links, bus lines 1, 4 and 5) and told to look hardest at:
the stretch under the clean shot's debris (pad B, the pad (4648,2898), the three metals
y 2771/2812/2857 at x 4560-4690); pad A's poly path and its separation from pad E; the track
x 4496 where it crosses the two links; which line each east pad belongs to; line 5's west
end; contacts missed on the long tracks; the corner (4496,2728).

Checked (16 images, 3.5x to 6x, with `follow.py`, `tl5_tracks.py`, `px.py`, `textmap.py`):
each of the five tracks is one metal in both chips with holes only at the known pads (dark
spots at (4496,3712), (4581,3345), (4581,3470) are chip-2 dirt or poly edges); the corner
(4496,2728) turns west, bare ground between it and line 5 in both chips; no ring, widening or
hole where the track x 4496 crosses the A-B and C-D links, poly continuous under it; pad A's
poly is one Z-shaped poly, about 10 px of field from pad E in both stripped shots; pad E has
nothing west or south and its column is continuous to y 2500; pad B and (4648,2898) are
contacts (ring and bright centre in both chips, pitted pad in the chip-2 stripped shot), B's
poly comes only from the west; under the three metals at x 4600-4810 the chip-2 stripped shot
reads ghost over field, no rings; the pad (4648,2898) is separate from `tl5`'s metal corner
(4690,2901) (no metal at x 4651-4683 in both chips); lines 1, 4 and 5 followed through their
diagonals to their pads, rows separate; line 1's pad does not reach the supply metal (bare
poly at x 4926-4941 in both chips); line 5 crosses x 4250 alone, line 4's pad poly comes from
the west; both pads of the track x 4366 are contacts with rows west only. Two dark blobs at
(4917-4935, 2784-2799) and (4908-4923, 2656-2668) are in the chip-2 shots only: not layout.

Findings: none. Tool caveat it reported: `follow.py` at its default `--gap 24` jumps from line
1's pad onto the supply metal and runs 33-46 px past pad A and line 5's pad over open poly
(with `--gap 16` it ends on line 1's pad); the trace follows the two-chip metal test, not the
follower's ends. Could not check: the clean shot under the debris (that stretch rests on the
two metal shots and the chip-2 stripped shot: Ambiguity 11); the east pads and pads B, D and
(4648,2898) were seen at 3.5x with text maps and profiles, not 4x.

Round 9: no findings.

### Round 10: full review of the strip south of the routing channel (2026-11-18, commit b433fa4, images `review-10/`)

A fresh reviewer (Claude Fable 5.2), 2026-11-18 15:35 -0600. One piece: the section "South of the routing
channel (x 4250-4967, y 5790-6350)" of `trace/tl4.txt`. It was given the five claims (the two
metals from the west with their pads and rows, `tl5`'s thin metal and the pad (4929,6323), the
three legs, nothing else in the area) and told to look hardest at: whether the two rows run
unbroken under the wide metals and whether either pad's poly goes west; a contact from RC's
horizontal metal to the rows under it; the thin metal's corner and its continuation south of
the pad; the row y 6313-6333 against the row y 6281; RB's horizontal piece against RA's leg and
RC; contacts on the legs; anything left out.

Checked (11 images, 3.1x to 5x, with `textmap.py`, `px.py`, `tl5_tracks.py`, `opendiff.py`):
both metals unbroken across x 4250, each with only its pad's contact (bright centre in both
chips, green hole), pink field west of both pads, both rows straight and unbroken to x 4967
and beyond; RC's horizontal has no contact to either row; the thin metal's corner is a plain
L, its only contact the pad (4929,6323), the metal present at y 6350 in both chips, the four
rows above crossed without pads; the row y 6313-6333 one poly from x 4250 to the pad, separate
from the row y 6281, nothing east of the pad; the three legs continuous, separated by bare
ground in both chips, no contact holes (nine line scans); RB's horizontal 35 px clear of RA's
leg and 34 px of RC; nothing left out (the `opendiff.py` groups are 10-14 px green rims).
Could not check: which supply each rail is (no device here); under the wide metals the
chip-2 stripped shot shows only fringes. Outside the strip it saw that the thin metal x 4929
ends or turns near y 6370-6415 (no metal in either chip at y 6377-6409, holes at y 6390 and
y 6414).

Findings, both geometry only, both confirmed and fixed:

1. **RB's horizontal piece was drawn too thin** (y 5806-5833): the metal runs y 5805-5856 and
   lies on `tla`'s row y 5838-5858 without a contact. Confirmed: `px.py col 4850 5796 5866 3
   metal1,acid1b` (chip-1 metal bright at y 5841-5850 below the dark line of the row's edge,
   the row cream in the clean shot there, dark red at x 4735 where it is in the open). Now
   `M 4754,5806:4950,5856`. No connection changes: metal over poly, no contact.
2. **RC's horizontal top edge is y 5891, not 5882** (`px.py col 4910 5868 5952 3
   metal,metal1,acid1b`: dark at y 5877-5892). Now `M 4841,5891:4967,5942` here; `tl5`'s own
   shape (`M 5127,5912 x4967 w=60`) and port keep 5882 (handoff). No connection changes.

`tools/t.sh tl4 sameconn.py b433fa4`: `connections identical`.
`.venv/bin/python tools/sameconn.py b433fa4`: `connections identical`.

Round 10: no findings that change a connection.

### Round 11: full review of RA's supply (2026-11-18, commit c4fd478, images `review-11/`)

A fresh reviewer (Claude Fable 5.2), 2026-11-18 15:49 -0600. One piece: the four metal rectangles under
"RA's supply" in `trace/tl4.txt`. It was given seven claims (the foot; the foot and RA one
metal; the foot clear of RB; no contact from the foot to the rows under it; the vertical metal
x 4949-4995 continuous from the foot to the band with no contact; the vertical clear of the
pads west of it; Ambiguity 12) and told to look hardest at whether the dark line across RA's
top is a row edge or a gap, at contacts on the foot and the vertical, and at the vertical's
continuity.

Checked (six images, 4x to 7x, with `px.py`, `textmap.py`, `tl5_tracks.py`): the dark line
across RA at y 2993-3001 is 8 px with a minimum red of 81-99 (chip 2) and 54-97 (chip 1), the
same as or lighter than the row's north edge under the foot, against 12 px and 61-66 followed
by bare ground at the real metal edge at x 4850; both chips have metal at y 3002-3010; the
west edge line x 4730 is unbroken from y 2938 to y 3035; the clean shot is pink there with no
gap strip: the foot and RA are one metal. The foot is continuous with no ring or hole; bare
ground at y 3000-3018 between the foot and RB in both chips; the vertical metal is continuous
from the band to the foot with only row-edge lines of 8-14 px, its single-chip dark spots
without a hole in the clean shot; bare ground at x 4922-4942 beside the three pads and the
thin metal. Not checked: the band north of y 2500 and its net; anything east of x 4967 beyond
text maps.

Finding, geometry only, confirmed and fixed: **the foot's north edge is y 2938, not y 2955**
(Ambiguity 12, above). Now `M 4732,2938:4967,2997`. `tl5` draws 2955 too (handoff). No
contact on the row, so no connection changes.

`tools/t.sh tl4 sameconn.py c4fd478`: `connections identical`.
`.venv/bin/python tools/sameconn.py c4fd478`: `connections identical`.

Round 11: no findings that change a connection.

## Not done

- West of x 4250 (`tl3`'s strip): where the rows of `tl4_w4590` at y 2810, of `tl5_w4937` at
  y 2641 and the metals of bus lines 1 (y 2512) and 5 (y 2685, with its pad (4236,2683)) go;
  the rows y 5457 and y 5718.
- North of y 2500: the poly column x 4534-4550 of `tl4_w4068` (seen to y ~2165 under the wide
  band, `g8_col.png`). East of x 4967: the row y 2542-2560 of bus line 1 (`tl4_w2512`).
- RA's supply east of x 4967 and north of y 2500: the east part of the vertical metal
  (x 4967-4995, `tl5`'s strip) and the band (y 2180-2507).
- South of y 6350: the three rails' legs and `tl5_w4590`'s thin metal go on. West of x 4250:
  the metal y 5939 (`tl5_w5936`) and the row y 6323 (`tl5_w4590`).
- The bus field's crossings were looked at only where a wire of the seventh or eighth run
  passes; the tracks between y 4320 and y 5440 were tested as each unit's run needed them.

## Corrections from `tl3` (coordinator, from the handoffs of 2026-11-18, second batch)

- Where this file has `tl4_w4501` as a "row from the west across the bus field": it is the row of
  `tl3`'s track A pad (4146,4510), net `tl3_e4152` = `tcw_a` (the east column's distributed line:
  latch C's enable, an input of e3 and e5).
- Ports: the rows at x 4250 (y 5412 `tl3_e5240`, 5457 `tl4_w5455`, 5500 `tl3_e4372`, 5631 `tcw_a`) are
  drawn on in `tl3`; `tl3_e5240` is `tl3_w5025` (latch B's inverted output) and `tl3_e4372` is
  `tl3_w4546` (`tl3`'s NOR 3); aliases in `trace/tl3.txt`.
- AMB-034 records Ambiguities 4-7 and 10 of this file.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- Bus line 1 (`tl4_w2512`), "source and loads not known": it is `r9m_l1w` = NOT `sl_eq_r5` (`eof`);
  west of x 4250 it is `tl1_w2592`.
- `tl4_w5455` ("crosses the foot to a pad (4040,5458) and goes south on a metal, not followed") is the
  4-bit counter's L3 line `c4l_l3` (`tl3` run 11).
- `tl4_w4198` (the clear of four latches) is a buffered copy of the reset NOR(`lpstb_b`, `res_b`)
  (`lc1_w7606`; `eof` run 2).
