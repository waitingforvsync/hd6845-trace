# tl4: top-left random logic, the fourth strip (x 4250-4967, y 2500-6350)

Package `tl4` (part 4 of 6 of the top-left logic). Trace: `trace/tl4.txt`. Views:
`cache/scratch/tl4/`. The strip holds most of the vertical control's **right cluster**
(`tla`'s name for it): a bus field of vertical metals (x 4250-4680), a gate column on a rail
RA (x 4728-4775), loads between RA and a second rail RB (x 4905-4950).

## Status

2026-11-17 18:15 -0600. **Partial: four units** (the fourth, a three-input NOR at y 4410-4645,
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
```

A latch: open while `tl4_w4068` is high, it takes `tl4_w4025`; `tl4_w4198` high forces
`tl4_w4243` low. The same build as the two latches in front of `rcs_e4` and the third latch
of the small cluster (`notes/blocks/tl1.md`). **Unlike in the first cluster, the inverter
above the latch does not feed the latch's data here**: its output `tl4_w3808` leaves north on
the metal x 4496, and the latch's data `tl4_w4025` comes from the south on the metal x 4452.
What the signals are is not known: their tracks are not followed yet.

## Inventory

| Where | What |
|---|---|
| x 4250-4680, y 2700-5800 | bus field: about ten vertical metals, poly rows east into the column, pads. Not drawn, except the pieces at the latch |
| x 4290-4967, y 3012-3222 | **the NOR** (`tl1`'s NOR at 2125,-520, findcell 0.77) |
| x 4690-4967, y 3220-3780 | units not matched by `tl1`'s first latch (findcell under 0.5). Not drawn |
| x 4400-4967, y 3781-3911 | **the inverter** (`tl1`'s inverter at 2125,-434, findcell 0.74) |
| x 4665-4967, y 3906-4390 | **the latch: this piece** |
| x 4250-4967, y 4410-4645 | **the three-input NOR** (hand-traced; no cell matches) |
| x 4640-4967, y 4645-4920 | two or three units of a denser build on the same column (rows y 4705-4900, buried-contact boxes at (4685,4675) and (4688,4850), a thin metal x 4860-4885). Surveyed, not drawn |
| x 4690-4967, y 4920-5400 | further units (findcell: the NOR at 2125,912 score 0.56; the inverter at 2126,955 score 0.75; the wide NOR at 2126,174 score 0.53). Not drawn |
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
| `tl4_w4025` | metal x 4452 | from the pad (4455,4025) south to y 5202 |
| `tl4_w4068` | metal x 4625 | north of the pad (4625,4068) to a corner (4630,2988), east to (4694,2989); candidate (4626,4054) is the pad |
| `tl4_w4198` | metal x 4537 | y 2938 to y 4814; candidates (4538,3782), (4535,3447), (4540,4215) |
| `tl4_w4243` | metal x 4494 | from the pad (4490,4243) south to (4507,5336) |
| `tl4_w4590` | metal x 4362 | y 2810 to y 5682 through the pad (4364,4590); candidates (4364,3014), (4367,4779), (4366,5125) |
| `tl4_w4545` | metal x 4626 | from the pad (4620,4545) south to (4623,4900): drawn whole, its south end not read |

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

## Not done

- The nine tracks beyond the views (table under Ports), and their other pads.
- RA and RB between the drawn pieces (y 3232-3770) and south of y 4392, and where they are fed.
- The rest of the gate column: y 3220-3780 (no findcell match), y 4645-5400 (findcell: `tl1`'s
  inverter at 2126,955, score 0.75; weaker hits for the NOR at 2125,912 and the wide NOR at
  2126,174). The units at y 4645-4920 are surveyed (`b_metal.png`, `b_acid.png`,
  `b_acid1b.png`; `cache/scratch/tl4/survey.md`): the column x 4677-4716 goes on south from a
  buried-contact box (4662-4700, 4660-4690) with rows crossing at y 4705-4725, 4750-4770,
  4795-4815, 4880-4900; the metal x 4626 from the three-input NOR ends among them.
- The south end of the metal x 4626 (`tl4_w4545`): a pad with a contact at about (4625,4892), seen by
  the reviewer, and the row it feeds. A pad with a contact at about (4278,4571) in the bus field.
- The west end of `tl4_w4501`'s row (in `tl3`'s strip) and the other pads of the track x 4362.
- A VCC box under RB at (4905-4960, 3893-3955) with a contact about (4928,3922) and a strip
  east under a plate at about x 4962-5015, y 3890-3925: a load of the logic east of RB (`tl5`).
- The bus field, the rows north of y 2960 and south of y 5400.
