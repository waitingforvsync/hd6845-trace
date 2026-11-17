# tl4: top-left random logic, the fourth strip (x 4250-4967, y 2500-6350)

Package `tl4` (part 4 of 6 of the top-left logic). Trace: `trace/tl4.txt`. Views:
`cache/scratch/tl4/`. The strip holds most of the vertical control's **right cluster**
(`tla`'s name for it): a bus field of vertical metals (x 4250-4680), a gate column on a rail
RA (x 4728-4775), loads between RA and a second rail RB (x 4905-4950).

## Status

2026-11-17 17:35 -0600. **Partial: three units.** The gate column repeats the first cluster's west column
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
| x 4690-4967, y 4390-5400 | further units (findcell: the NOR at 2125,912 score 0.56; the inverter at 2126,955 score 0.75; the wide NOR at 2126,174 score 0.53). Not drawn |
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

## Ports

None yet: no wire is drawn to the strip's edge (`ports.d/tl4.txt` is empty). The tracks leave
the pieces inside the strip; each is drawn only inside the views named above:

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

## Not done

- The nine tracks beyond the views (table under Ports), and their other pads.
- RA and RB between the drawn pieces (y 3232-3770) and south of y 4392, and where they are fed.
- The rest of the gate column: y 3220-3780 (no findcell match), y 4390-5400 (findcell: `tl1`'s
  inverter at 2126,955, score 0.75; weaker hits for the NOR at 2125,912 and the wide NOR at
  2126,174).
- A VCC box under RB at (4905-4960, 3893-3955) with a contact about (4928,3922) and a strip
  east under a plate at about x 4962-5015, y 3890-3925: a load of the logic east of RB (`tl5`).
- The bus field, the rows north of y 2960 and south of y 5400.
