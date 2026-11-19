# lc3: left-centre random logic, part 3 of 3 (x 4400-6450, y 9233-10400)

## Status

2026-11-19 07:44 -0600, run 2 (Matt Godbolt, on Claude Fable 5.2). **Two stages of `lc2`'s ripple counter are drawn
here**: stage E4 (a copy of `lc2`'s flip-flop cell `lc2_ff`, turned) and stage B0 (the same four
gates folded over both columns, drawn by hand), both reviewed (rounds 3 and 4), 37 new transistors (E4's top one is also in `lc2`'s drawing). With `eof`'s piece `ff3` (stage
W3) the counter has five stages and its order is known. Still open: everything east of x 5480 but the gate pair
(the crossing field, where stage B0's clock and the clear come from), the gate pair's Fable review (R31).

Split with `eof` (Tom Seddon, run 6, whose claim covers the corner x 4400-4750, y 9100-9700): the west copy,
stage W3, was drawn by both of us within minutes; `eof`'s `ff3` reached its branch first, so this file's drawing of
it was removed (it was in this package's review round 1, which found it as `eof` has it). What is kept from it
here: track B from `lc2`'s end to its END pad, and the middle rail.

Run 1 (dp111, 2026-11-18 04:48 +0100): the gate pair drawn on claude-opus (section "Gate pair at 6x"), reviewed
on claude-opus; it still needs its Fable review (re-read item R31). The inventory below was read at 0.62x and
1.22x; everything in it that is not in a later section is "seen", not traced.

## The counter: order of the stages (traced)

`lc2`'s west cluster is a flip-flop cell (`lc2_ff`, `notes/blocks/lc2.md`) and its copy turned 180 degrees. The
same four gates stand three more times directly south of them, in this strip:

| Stage | Where | Drawn as | Clock | Slave output (the next stage's clock) |
|---|---|---|---|---|
| B0 | x 4440-5480, y 9940-10580 | by hand: latch K west, gates K3, K4 turned east, five crossing rows (this file) | `lc3_w9947`, a poly row from the east | `eof_w9255` (unnamed in this file) |
| W3 | x 4580-4990, y 9180-9960 | `@inst lc2_ff 0,780` (`eof`'s piece `ff3`) | `eof_w9255` | `lc2_w8475` |
| `lc2`'s first (the master) | x 4580-4990, y 8350-9190 | the cell | `lc2_w8475` | `lc2_w8298` |
| `lc2`'s second | x 4990-5450, y 8370-9200 | turned copy | `lc2_w8298` | `lc2_w9034` |
| E4 | x 4990-5450, y 9150-9945 | `@inst lc2_ff 254,716 rot=180 o=4826,8810` (this file) | `lc2_w9034` | `lc2_w9210` |

So the chain starts at the bottom, runs up the west column and down the east one. A clock enters a stage at the
end of its thin metal by gate K4 and the slave output leaves by track C at the other end. The two outputs that
`lc2`'s AND-OR-INVERT south of latch B takes are the last two stages': `lc2_w9125` = NOT(`lc2_w9034` AND
`lc2_w9079` OR `lc2_w9210` AND `lc3_w9299`). **Input identified, not logic changed**: `lc2_w9210` was "row 5's
metal, south into `lc3`"; it is E4's slave output (one metal from `lc2`'s pad (5341,9211) to E4's pads
(5343,9343) and (5343,9822)).

All five stages have the same clear (`lc2_w8450`, by tracks B and B') and the same gating of the slave by
`lc1_w7170` (tracks A and A').

Believed, not established: a divider by 16 or by 32 of whatever `lc3_w9947` carries, chosen by `lc3_w9299`, is what
a cursor blink of 1/16 or 1/32 of the field rate needs. Read but not yet drawn (next pieces): the clock's row
ends on a pad (6211,9948) of a metal that is `lc2`'s through line `lc2_x6432` four tracks further west (from
`lc2`'s east edge at (6450,9165)); the upper inverter of the gate pair drives `lc2_w9079` (so the two selects of
`lc2_w9125` are complements) and the lower one drives `lc1_w7170`.

## Stage W3 (x 4580-4990, y 9180-9960): `eof`'s piece `ff3`

Not drawn here (see Status). This package read it independently before the two drawings were found to be the
same (`findcell` 0.91; master and copy side by side in three bands, `mo_8390_*.png`, `mo_8650_*.png`,
`mo_8910_*.png`; `tools/railprof.py 4758 4796 9130 9960` against the master's `8350 9180`; tracks A, B and C by
`tools/tl5_tracks.py v`), and review round 1 checked it against the photos: the same instance, the same VSS
contact (4766-4769, 9211-9217), the same joins of tracks A, B and C. Nothing found that `eof`'s notes do not have.

## Stage E4 (x 4990-5450, y 9150-9945): `lc2_ff` turned 180 degrees

`findcell` 0.75 (centre 5082,9561). Placed as `@inst lc2_ff 254,716 rot=180 o=4826,8810`: a point (x,y) of the
master is at (9906-x, 18336-y). (First placed 6 px further east, as `findcell` gave it; review round 1 measured
its pads, contacts and thin metals 8-10 px west of that, the rows and nodes fitting either way; overlay
`e4s_metal.png`, 3x.) Checked on overlays at 2.5x in both shots (`p2ov_9150_*.png`, `p2ov_9560_*.png`);
`tools/railprof.py 5116 5152 9560 10000`.

Extraction: `lc3_w9774` = NOT(`lc2_w8450` OR `lc2_w9034` AND `lc2_w9210` OR `lc3_w9696`); `lc3_w9696` =
NOT(`lc3_w9774` OR `lc2_w9034` AND `lc3_w9644`); `lc2_w9210` = NOT(`lc3_w9644` AND (`lc3_w9696` OR `lc2_w9034`));
`lc3_w9644` = NOT(`lc1_w7170` AND `lc2_w9210` AND (`lc3_w9774` OR `lc2_w9034`)). `tools/unsure.py --equations`, as
for `lc2`'s stages: the second and third FIRM; the first DEPENDS for its clear term (the cell's uncertain
diffusion beside the rail) and the fourth DEPENDS on the cell's uncertain strip to its load.

- **Its top is what `lc2` drew by hand south of its east column** (`lc2`'s round 16: node `lc2_w9171`, the gate
  of `lc2_w9034`, the VSS contact (5124,9224), the strip x 5062-5078): that is this stage's gate K4, its lower
  node Z, its clock row and its VSS node. The two drawings lie on each other and extract as one transistor;
  `lc2`'s lines are left as they are (proposal in the handoff: delete them there).
- **Its clock** is `lc2_w9034`: `lc2`'s metal to the pad (5254,9208) lies on the copy's end pad and thin metal.
- **Its VSS contact** at the bottom of the column: ring (5137,9896), box x 5113-5160, y 9880-9923 (`e4bot.png`, 5x).
- **East rail**: x 5102-5150, with x 5086-5150 at y 9250-9300, x 5084-5162 at y 9395-9552 and a foot west to
  x 5084 at y 9925-9945 (`tools/textmap.py` rows at twelve heights; round 1).
- **Middle rail** x 4924-4980, y 9180-9970 (shared with stage W3; `eof` draws it too).
- **Track C'** (x 5334-5352): one metal from `lc2`'s pad (5341,9211) through the end pad (5343,9343) to the pad
  (5343,9822) of K1's row 2, where it ends (`tl5_tracks.py v 5343 9150 10420`: metal y 9206-9824; the 18 px
  without metal at y 9215-9233 is the pad's ring, as at the other pads: round 1 agreed).
- **Track B'** (x 5378-5394, `lc2`'s staircase line `lc2_w8907`): from `lc2` through the pad (5386,9735) of the
  clear row (`tools/textmap.py 5366 9706 5418 9760 3`) to its END pad (5386,9990) (stage B0's section).
- **Track A'** (x 5422-5438, `lc1_w7170`, `lc2`'s staircase line `lc2_w8474`): from `lc2` through the pad
  (5430,9298) of K4's row and **a second pad (5428,9428)** (`textmap.py 5404 9404 5456 9452 3`: a contact), whose
  poly leaves east along y 9418-9440 (read: it is the lower inverter's output row; not drawn yet), to its END pad
  (5428,10080) on stage B0's row.

## Stage B0 (x 4440-5480, y 9940-10580): the counter's first flip-flop, folded

Below stages W3 and E4 the same four gates stand once more, but split between the two columns: the cell's master
latch K (gates K1, K2) in the west column, 1561 px below `lc2`'s (`tools/findcell.py 4700 8400 4960 8780`: 0.89 at
4830,10151), and its slave gates K3 and K4 turned 180 degrees in the east column (`findcell.py 4700 8780 4960 9150`:
0.71 at 5083,10152; a point (x,y) of the master at (9913-x, 19117-y)). Half a cell cannot be placed, so the unit is
drawn by hand: the cell's lines moved to both places (scratch `mkbot.py`, `mkb0.py`), every item that differs read
on the photos and changed, and the wiring between the halves drawn new.

Checked: master beside this unit, both halves, clean shot and metal shot (`mow_8390_*.png`, `mow_8590_*.png` west;
`moe_8360_*.png`, `moe_8580_*.png` east, against `lc2`'s turned stage): the gates, loads, tie boxes and nodes are
the cell's; the differences are all at the ends of rows. Overlays of the finished drawing at 2.6-2.9x in both
shots (`b0_bw_*.png`, `b0_be_*.png`, `b0_ww_*.png`, `b0_we_*.png`). `tools/railprof.py 4758 4796 9940 10600`.
`tools/opendiff.py 4580 9940 5480 10600`: only the narrow green gaps between features.

**What differs from the cell**

- West, as in stage W3: K1's VSS node has one contact (4766,10000) (`tools/textmap.py 4744 9960 4812 10030 4`).
- West, new: row b of K2 does not come up a vertical poly from gate K4; it runs west to a pad (4517,10253) on a
  metal of its own. Track B (the clear) **ends** on the pad (4517,10166) of the clear row, 70 px north of that
  pad (`tools/tl5_tracks.py v 4517 8690 10420`: no metal y 10170-10248).
- West, new: K2's output box (x 4683-4730, y 10278-10310) sends its poly south, not west (`k2o_*.png`, 5x, three
  shots). Under the west rail south of K2's output node there is nothing until the crossing rows (field: greenish
  under the wide metal, `tools/px.py col 4777 10255 10400 6`).
- East: each row of K4 ends one track further east than in the cell: the clock row on a pad (5298,9990), the third
  row on a pad (5342,10036), the top row on a pad (5386,10122); the second row on the END pad (5428,10080) of
  track A' (`lc1_w7170`). The cell's two END pads at (5309,10037) and (5353,10121) are not there: the metals
  x 5292-5308 and x 5335-5351 pass over those rows (`tl5_tracks.py v 5300 9930 10600`, `v 5343`: 8-9 px bars
  only). K3's row d has its pad at (5257,10252), row c a pad (5298,10294).
- East: K4's output row (y 10192-10216) runs on east to x 5445 and turns south (not down a poly at x 5317-5335).
- East contacts, by `tools/textmap.py`: K4's VSS (5122,10008), box S (5150,10205), K3's VSS box (5131,10332).

**The wiring between the halves**: five poly rows cross under the west and middle rails south of the unit
(`railprof.py`: poly over field at y 10373-10392, 10412-10437, 10462-10481, 10499-10522, 10547-10567), each from
something in the west column to a pad east of the middle rail (`bsw_*.png` 3.4x, `bse_*.png` 2.6x, `bse2_*.png`
4x in three shots, `tl5_tracks.py h` along each row and `v` down each metal):

| Row | West end | East end | Carries |
|---|---|---|---|
| H1, y 10382 | the poly of K2's output box (south on x 4685-4707, then east) | pad (5059,10383); metal east and north (x 5248-5264) to the pad (5257,10252) of K3's row d | K2's output `lc3_w10201` |
| H2, y 10423 | pad (4671,10423) at the foot of the thin metal x 4641-4655 (K1's row 1, K2's row a) | pad (5015,10422); metal east and north on x 5292-5308: pad (5298,10294) of K3's row c, pad (5298,9990) of K4's clock row | the stage's clock `lc3_w9947` |
| H3, y 10467 | pad (4714,10467) at the foot of K1's output metal x 4598-4612 | pad (5059,10467); metal east to a pad (5299,10467); poly east and north (x 5335-5351) to the pad (5345,10336) of the metal x 5335-5351, which ends on the pad (5342,10036) of K4's third row | K1's output `lc3_w10123` |
| H4, y 10511 | pad (4671,10511) at the foot of track C (x 4554-4572) | pad (5015,10511); metal east to a pad (5256,10511); poly east and north (x 5383-5400) to the pad (5387,10296) of the metal x 5378-5394, which ends on the pad (5386,10122) of K4's top row | K3's output: the stage's slave output (stage W3's clock) |
| H5, y 10556 | pad (4714,10556) at the foot of the metal from row b's pad (4517,10253) | pad (5059,10556); metal east to a pad (5298,10557); poly east and north (x 5421-5445) to the east end of K4's output row | K4's output `lc3_w10210` |

Track C (x 4554-4572) is the metal that `eof`'s piece `ff3` draws south from stage W3's L (its port at y 9990): one
metal from there through the pad (4561,10077) of K1's row 2 to the foot at y 10511 (`tl5_tracks.py v 4562 8690
10420`, `v 4563 10230 10600`). So **this stage's slave output is stage W3's clock**. The net has no name in this
file: `eof` names it `eof_w9255`, and it takes that name when `ff3` is on main (below it is written K3).

**Its clock** is on the metal x 5292-5308 and the thin metal x 4641-4655, joined by row H2: four gates and no
driver in the unit. From the pad (5298,9990) the poly runs on north (x 5292-5314) and east as a row y 9936-9958
(`ckn_*.png`, 8x): it crosses the track field and the crossing field under fifteen metals without a pad
(`cf_5470.png`, `cf_5960.png`, 2.6x, three shots) to a pad (6210,9945) on a vertical metal x 6200-6222, which
comes from the north and runs on south. Drawn to x 5480.

**The clear's track B'** (`lc2_w8907`) ends on a pad (5386,9990); its poly runs south (x 5380-5402) and east as a
row y 10022-10045, 12 px clear of the pad (5342,10036) of K4's third row (`tb_*.png`, 7x, three shots: a plain
gap x 5367-5378 between two outlines each rounded at its own corner; `px.py row 10036 5340 5420 3`). The row runs
east to a pad (6257,10035), whose metal x 6245-6265 runs south. Drawn to x 5480.

Extraction (`tools/t.sh lc3 netlist.py`):

- `lc3_w10123` = NOT(`lc2_w8450` OR `K3` AND `lc3_w9947` OR `lc3_w10201`)
- `lc3_w10201` = NOT(`lc3_w10123` OR `lc3_w10210` AND `lc3_w9947`)
- `K3` = NOT(`lc3_w10210` AND (`lc3_w10201` OR `lc3_w9947`))
- `lc3_w10210` = NOT(`lc1_w7170` AND `K3` AND (`lc3_w10123` OR `lc3_w9947`))

the cell's four equations, with `lc3_w9947` as the clock.

## Inventory (seen, not traced)

| Piece | x | y | What it looks like |
|---|---|---|---|
| West tracks | 4425-4655 | whole height | vertical metals at x about 4431, 4476, 4518, 4562, 4608, 4650 (pitch about 43; `urch`'s channel), with pads and contacts feeding poly rows east into the logic |
| Logic column A | 4680-5010 | 9233-10400 | dense gates either side of two rails: wide metal x about 4750-4800 (full of contacts) and x 4930-4975; inputs arrive as poly rows from the west tracks |
| Logic column B | 5010-5240 | 9233-10400 | gates around a rail x 5085-5108; poly rows leave east to pads on the track field |
| Track field | 5240-5570 | whole height | vertical metals at x about 5256, 5300, 5343, 5386, 5430, 5473, 5517, 5560 (pitch 43), pads with contacts at many heights |
| Gate pair | 5540-5900 | 9260-9520 | two small gates, mirror images about y 9384.5 (`findcell.py 5540 9395 5900 9525`: second hit score 0.85 at 5720,9309). Supply metals x 5665-5712 (contact (5680,9505)) and the wide x 5840-5890 (contacts (5865,9455), (5865,9310)) |
| Wide metal | 5840-5890 at y 9250, diagonal to x 5690-5735 at y 9700-10050, diagonal SW to about (5450,10330) | | a supply rail by its width; which supply not established |
| Empty field | 5900-6230 | 9250-9530 | nothing but a ring line along its west and south edges (x 5880-5900, y 9530) |
| Crossing field | 5480-6450 | 9540-10050 | horizontal poly rows at y about 9575, 9620, 9665, 9710, 9755, 9800, 9850, 9885, 9940, 9985, 10030 under vertical metals x 5820-6440 (pitch 43); west ends are pads in a staircase with metal rings near (5750,9575), (5700,9620), (5650,9665), (5600,9710), (5550,9755), (5500,9800); further rings near (5500,9850), (5555,9870), (5640,9990), (6205,9945), (6245,10030), (6300,9870), (6380,9840). Dots at many crossings in acid1b: contacts or not, not decided |
| Corner bundle | 6000-6450 | 9250-9700 | nested L-shaped metals turning from south to east |
| South bundle | 5550-6450 | 10050-10400 | the vertical metals carry on south; six of them (x 5820-6000) turn diagonal SW; a row y about 10365 with a pad near (6045,10360) |

## Logic

Nothing traced. **Believed** for the lower gate of the pair (3.4x in metal, acid1b, acid; not
drawn because two points were not resolved): an inverter. Input poly from a contact pad
(5560,9470) east along y 9458-9482 to an end near x 5733, crossing a diffusion column
x about 5655-5708 between the contact (5680,9505) and a band y 9428-9450; the band runs east
through a load block x 5785-5835 to the contact (5865,9455) on the wide metal. A poly row
y 9415-9440 arrives from the west at x about 5600, at a box (5625,9432) under the metal track
x 5612-5640.

## Ports

`ports.d/lc3.txt` has every port with its place. Gate pair: inputs `lc3_w9470` (metal x 5560, south edge y 9520)
and `lc3_w9299` (metal x 5560, north edge y 9255); outputs `lc3_w9432`, `lc3_w9337` (poly rows at x 5540); `vss`
(x 5665-5712), `vcc` (wide metal x 5840-5890, named from the loads). Counter stages: the joins to `lc2` at
y 9180-9256 and to `eof`'s `ff3` (track C at y 9970-9990, track B) are made by overlapping metal; stage B0's
clock `lc3_w9947` and the clear `lc2_w8907` leave east as poly rows at x 5480 (y 9936-9958, y 10022-10045); the
second pad of track A' has a poly east at (5446, 9418-9440); the three rails run on south of the drawing.

## Gate pair at 6x (2026-11-18, claude-opus)

Drawn as one cell `lc3_inv` (the lower gate) and its mirror about y 9384.5. Extraction
(4 transistors): `lc3_w9432 = NOT lc3_w9470`, `lc3_w9337 = NOT lc3_w9299`;
`unsure.py --equations`: both FIRM after review round 1 (0 `?` items).

Review round 1 fixes (checked by the tracer at 5x, metal | metal1 | acid1b | acid, `fix1.png`
5590-5670 x 9240-9580, `fix2.png` 5720-5840 x 9240-9520):
- Boxes (5625,9432)/(5625,9335): **no metal contact**. The metal x 5615-5638 runs unbroken
  over the whole piece in both metal shots, the boxes only dark-edged; acid1b pale inside,
  no contact spot. The `?C`/`?M` pads are deleted; the track is drawn as its own net
  `lc3_m5626` (`M 5626,9255 y9520 w=24`, ports at both ends), touching no contact. The
  boxes stay buried contacts (poly row onto the output band); outputs are separate nets.
- Load gate tie: the load poly runs south `P 5780,9455:5812,9500` onto a buried contact
  `B 5780,9468:5812,9500` (square outline in metal and metal1, contact spots in acid1b),
  met by a pale diffusion strip from the band, `D 5744,9445:5812,9502` (x 5744-5776 south
  to y 9500, then east under the box). Seen in both copies (upper at y 9268-9300). The old
  `?P 5770,9455:5800,9505` and `?B 5770,9432:5786,9448` are deleted.
- A second metal x 5746-5766 runs the full height with no contact seen where the tie strip
  passes under it (y 9445-9502, both metal shots continuous): drawn as its own net
  `lc3_m5756` (`M 5756,9255 y9520 w=20`, ports at both ends).
Coordinates of the drawn pull-downs, load poly (x 5785-5835) and rows come from the survey and
one 1.6x overlay (`ov.png`); the channel widths were not profiled and wire ends not viewed
50 px beyond: to check in review.

Views `bc_3.png` (5590-5675 x 9400-9465), `ld_3.png` (5750-5900 x 9400-9510), `bx_6.png`
(5590-5710 x 9300-9460), each acid1b | acid | metal at 6x. Not drawn: the time box ran out
before every connection could be read in two shots and the gates profiled.

- Boxes (5625,9335) and (5625,9432): in acid1b each is a square outline about x 5610-5640,
  y 9322-9348 and y 9418-9446, pale inside, at the meeting of a horizontal poly row (from the
  west) and the vertical diffusion/poly edge at x about 5645 - the look of a buried contact.
  In the metal shot both lie under the track x 5612-5640, which shows a brighter blob at each
  (5625,9330), (5625,9432) but also bright grain between them (y 9380-9410); no clear dark
  contact ring was seen at either. Leaning: buried contact only, metal passing over; **not
  decided** (needs a profile along x 5625 in metal and a check whether the track x 5612-5640
  is continuous over y 9300-9460).
  Profiles (`px.py`, metal shot): column x 5626 is dark y 9308-9352 and y 9412-9456, bright
  y 9356-9404 (and acid1b dark lines at y 9316, 9348, 9420, 9452: the box edges). Row y 9380:
  bright x 5620-5630 between dark edges x 5615, 5635 (a narrow metal about x 5617-5633).
  Rows y 9330 and y 9432: dark over x 5605-5635. So the metal track is visible only between
  the boxes and each box is a dark square in the metal shot. That fits a metal contact ring
  as well as a track hidden by step relief over a buried contact: **open**, and it decides
  whether the two outputs are joined by metal (if both boxes are metal contacts on one track,
  the gates' outputs are shorted, so at most one can be, or the track is cut between them).
- Load of the lower gate (`ld_3.png`): metal contact ring (5865,9455) on the wide metal,
  ring about x 5843-5885, y 9430-9475 (clear in acid1b and metal). West of it the diffusion
  band y 9428-9450 runs from x 5760 to the contact; a box x 5770-5835, y 9435-9500 is dense
  red/orange in acid (implant-looking: depletion load). Its gate tie: a poly/box shape
  x 5770-5800, y 9470-9505 reaches the band's south edge near x 5785; whether it ties to the
  output band (usual load) was not settled.
- Diffusion column x about 5655-5710 (acid shot, pink): continuous y 9350-9420 between two
  poly rows y about 9338 and 9430, which is the gap between the two gates' outputs.


- (5625,9432) and its mirror (5625,9335): buried contact of the west poly row onto the output
  band with the metal track merely passing over, or a metal contact as well. If both were
  metal contacts the two gates' outputs would be shorted by the track x 5612-5640, so the
  first reading is expected; 6x views `bc_*.png`, `ld_*.png` were rendered but not read.
- The pair is not symmetric in its wiring: the upper gate's west row ends on a pad with a ring
  near (5515,9338) (track x 5517), the lower one's row runs on west past x 5480; the upper
  input track x 5560 comes from the north, the lower from the south. Read each copy's inputs
  on the photo.
- Which of the supply metals is VCC and which VSS: expected from the load (wide metal = VCC,
  x 5665-5712 = VSS), not traced to a named rail.

## Not done

1. **The gate pair's Fable review (R31)**, with its rows and tracks, read and drafted (`cache/scratch/lc3/draft-p5.txt`)
   but not drawn: the lower output row runs west under the tracks x 5517 and x 5473 to the pad (5428,9428) of
   track A' (so `lc1_w7170` = NOT `lc3_w9470`); the upper output row ends on a pad (5517,9340) of the track
   x 5509-5527, `lc2_w9079` (so `lc2_w9079` = NOT `lc3_w9299`), which runs on to an END pad (5517,9838) and a
   poly row east; the lower input's track ends on a pad (5558,9882) and a poly row from the east.
2. **The crossing field and the corner bundle**, x 5480-6450, y 9233-10100 (survey in `cache/scratch/lc3/survey.md`):
   eleven poly rows (centres y 9577, 9621, 9665, 9708, 9750, 9793, 9838, 9880, 9947, 9990, 10032) under about
   fifteen vertical metals; pads only at the rows' ends: (6037,9581), (5993,9623), (5950,9667), (5908,9711),
   (5865,9754), (5822,9797) (the tops of six verticals), (6386,9840), (6298,9884), (6211,9948) (stage B0's clock),
   (6257,10036) (the clear), (5646,9992). `lc2`'s four through lines each step one track west at y 9260-9450 and
   turn west and south round the corner (nested L-shaped metals), so `lc2_x6432` is the metal of the pad
   (6211,9948); a fifth line enters at about (6450,9450). Stage B0's clock row and the clear's row are drawn to
   x 5480.
3. The wide VCC metal's diagonal and foot (it crosses stage B0's south-east corner: from about (5460,10320)
   south-west, then south on x 5338-5393 from y 10450; no contact on the three polys under it: round 4). The track
   field x 5440-5760 south of y 9540: `rst_n`'s metal ends on a pad (5475,10207), poly south;
   `lc2_w8450`'s metal (x 5626, then x 5604) to a pad (5540,10165), poly south; the wide metal's diagonal.
4. The south bundle (y 10050-10400): the verticals on south, six of them diagonal.
5. West of x 4580 (`urch`'s channel and `eof`'s corner): the metal x 4420-4442, the tan boxes under track A
   (y 9099-9243 and 9573-9717 by review round 1).
6. Green patches under the rails in the clean shot at about (4780,9186), (4795,9712), (5112,9408), (5125,9932)
   (review round 1: no outline or ring in either metal shot; read as field; `eof` reads the second the same way).

## Review

**Model note: the inverter pair was traced AND reviewed on claude-opus, not
claude-fable-5-2** (the contributor's Fable allowance is exhausted). The survey was on
Fable.

Round 1 (full review at commit ac7f681, a fresh agent on claude-opus; the tracer had
checked the pair only on one 1.6x overlay, so every item was treated as unverified).
Three findings, each then seen by the tracer on its own 5x views before it was applied:
1. The boxes (5625,9432) and (5625,9335) are buried contacts, not metal contacts: the
   metal x 5615-5638 runs unbroken over both in both metal shots. The `?C`/`?M` items were
   deleted and the metal drawn as a through net `lc3_m5626`. This changes connections: the
   two outputs are not joined (two inverters, not one gate).
2. The load's gate tie was drawn in the wrong place: it is a box x 5780-5812, y 9468-9500
   at the load poly's south end, met by a diffusion strip from the band. Redrawn, firm
   (same connection: gate tied to the output).
3. An undrawn second through metal x 5746-5766: drawn as `lc3_m5756`.
Checked and correct: pull-down column, input rows and pads, the VSS and VCC contacts on
their rails, the mirror about y 9384.5, the load's x position.

Round 2 (fix check, 2026-11-18 08:42 +0000, a fresh agent on claude-opus, against ac7f681): all three changes
match the photos in `metal`, `metal1`, `acid1b` and `acid`, at the lower inverter and at
the mirrored one: no contact on either through metal over the boxes or over the strip;
the buried contact where poly and strip overlap; bare field east of the tie box (nothing
joins VCC). Extraction 0 errors; both equations FIRM; outputs and both through metals
separate nets. Geometry only: the strip's west edge is about x 5754 in the photo against
5744 drawn. Not checked in either round: gate widths past the channel ends by profile;
50 px beyond the west ends of the output rows.

Round 2: no findings.

Round 3 (run 2, Fable; the first full review of the counter stages; 2026-11-19, a fresh agent on Claude
Fable 5.2, against b7bcf40; images `cache/scratch/lc3/review-1/`). Pieces: stage W3 (then drawn here as
`@inst lc2_ff 0,780` with its own lines) and stage E4. Told to suspect: each copy against the master (extra poly
on a pad, a metal running on through a pad, an extra or missing contact or transistor); the 18 px without metal
on track C' below the pad (5341,9211); track C's join to `lc2`'s L; the pads (5386,9735) and (5428,9428); the ends
of track A and track C'; tracks A and B for undrawn pads; both ends of each column; the east rail's wide part.
It looked at master and copy side by side at 1.5-5x at the row ends, the K3 strip and both sides of K4, the pad
fields in three shots, overlays in both shots, and measured with `textmap.py`, `follow.py`, `tl5_tracks.py`.
All eight equations stand. Findings:
1. Track B' does not end free at y 9969: it ends on a pad (5385,9991) (ring and bright centre in both metal
   shots; a red blob, not a green hole, in the clean shot), whose poly was undrawn. **Adds a connection** at the
   piece's edge (where the clear's wire goes on). Confirmed (my `tb_*.png`, 7x): drawn with stage B0 (the pad,
   its poly south and the row east), which has its own full review.
2. Track B is a through line (to y 10170) drawn as ending at y 9392, and track A' runs on south of y 9440.
   Geometry only (drawn short, said so in the notes, not in the trace). Both now drawn to their END pads.
3. An undrawn poly row y 9937-9955 from x 5290 east, passing under B' and A' with no pad. Geometry only for
   these pieces: it is stage B0's clock row, drawn with it.
4. E4's metals, contacts and pads lie 8-10 px west of where the turned cell put them; the east rail has a foot
   west to x 5083 at y 9925-9940. Geometry only. The instance moved 6 px west (`254,716`), the foot added.
Checked and found correct: track C' is one metal (the 18 px is the pad's ring); track C is one metal with `lc2`'s
L; the pads (5386,9735), (5428,9428), (5430,9298), (5343,9343) are contacts and (5428,9428)'s poly leaves east
only; tracks A and C' end where drawn; no pad on A or B on the way; both column ends; E4's top is `lc2`'s hand
drawing (one contact, one transistor); the wide part of the east rail touches only its contact; no extra or
missing poly, pad or contact in either copy. Not checked: the cell's own uncertain items; green patches under
the rails (Not done, 6).
For finding 4 (E4 alone, before stage W3 was removed and stage B0 added): `tools/t.sh lc3 sameconn.py b7bcf40`
ended `connections identical` (the full-extraction command was not run at that point; after the other changes
`.venv/bin/python tools/sameconn.py b7bcf40` differs only by stage W3 removed and stage B0 added, no line of E4).

Round 3: one finding that adds a connection (track B''s END pad), drawn with stage B0; three geometry only, fixed. A fix check follows with stage B0's review.

Round 4 (run 2, Fable; full review of stage B0, and the fix check of round 3's changes to stage E4; 2026-11-19 08:07 -0600,
a fresh agent on Claude Fable 5.2, against 49d3495; images `cache/scratch/lc3/review-2/`, 24 used). Told to
suspect: which row or metal each of the five crossing rows joins at each end; every pad (the dark-red ones above
all; metals running on through pads; second polys); the three polys north under the diagonal metals; the gap at
x 5367-5378; the contacts absent at (5309,10037), (5353,10121) and present at (5298,10294), (5342,10036),
(5386,10122); the hand-copied gates against the master and against `lc2`'s turned copy; K2's output; anything
undrawn. For E4: the 6 px move, the rail's foot, track B''s END pad. It looked at all ten row ends at 3.9x in
three shots, every metal's ends with `tl5_tracks.py`, every pad in both metal shots and both stripped shots, both
halves by mosaic. Findings, all geometry only:
1. K3's output thin metal and its two contacts were drawn 8-9 px east of the photo (centres (5042,10120),
   (5023,10226), metal x 5032-5044). Confirmed (`k3m.png`, 6x) and moved.
2. Three pad boxes left over from the cell, with no contact (at (5263,9993), (5307,10037), (5352,10121)): the
   rows are plain there. Removed.
3. E4's rail foot starts at y 9931, not 9925. Changed.
Seen and not drawn (Not done, 3): the wide metal crossing the piece's south-east corner (from about (5460,10320)
south-west, then south on x 5338-5393 from y 10450), over the three polys with no contact on them (no ring in
either metal shot, no hole, the polys' width uniform); `rst_n`'s pad (5472,10208), 8-10 px east of K4's
output-row corner and apart from it in three shots.
Checked and found correct: the pairing of the crossing rows (both nestings are planar); every metal's ends; every
pad a contact (the seven dark-red ones and (5345,10336) have no green hole in the clean shot but are pitted in
the chip-2 stripped shot, with ring and bright centre in both metal shots); H3's arm one poly; the gap at
x 5367-5378 is field in three shots; no contact at (5309,10037), (5353,10121) or any row crossing; K2's output
leaves south only, field under the west rail down to H1; 19 transistors and the four equations; E4's contacts
now within 1-4 px, its equations intact, track B' ends on (5386,9990), the east rail continuous into B0.
Not checked: the cell's uncertain diffusion at the clear's pull-down (4721,10165) (its outline shows in chip 2,
the colour reads as field, as in the master); K3's thin metal is dark at y 10122-10148 in both chips, as in
`lc2`'s copy and the master (its END pad's ring), drawn plain; the two rows east of x 5480.
For the three fixes: `tools/t.sh lc3 sameconn.py 49d3495` ends `connections identical`;
`.venv/bin/python tools/sameconn.py 49d3495` ends `connections identical`.

Round 4: no findings that change a connection.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- From `lc2`: `lc3_m5626` is `lc2_w8450` (latch B's data); `lc3_m5756` runs north through `lc2` and latch B
  into `lc1` with no contact found; `lc3_w9299`'s metal x 5560 passes through the pad (5560,9166) of
  `lc2`'s gate row 4 and on north into `lc1`. `lc3`'s shapes start at y 9255: the joins are made by
  `lc2`'s items drawn to y 9256. `lc2_w9185` (x 5924-5940) enters at y 9233 and runs to about y 9540,
  then east along y 9525-9545 (undrawn here). At y 9233: `lc2_w9034` (x 5255), `lc2_w9210` (x 5342),
  `lc2_w9079` (x 5518) and the rails have ports in `ports.d/lc2.txt`; the stack under the east rail at
  y 9160-9300 has its top gate in `lc2` (`lc2_w9034`, node `lc2_w9171`), its second gate and load here.
  The clock of `lc2`'s ripple counter, `lc2_w8475`, comes from the south (an L-shaped metal at
  x 4553-4575, y 9190): this strip is in the end-of-frame lead group (`eof` (d)).
