# lc3: left-centre random logic, part 3 of 3 (x 4400-6450, y 9233-10400)

## Status

2026-11-19 07:12 -0600, run 2 (Matt Godbolt, on Claude Fable 5.2). **Two more stages of `lc2`'s ripple counter are
drawn**, as copies of `lc2`'s flip-flop cell `lc2_ff` (sections "Stage W3" and "Stage E4" below; 37 transistors,
not yet reviewed). With them the counter's order is known: W3 clocks `lc2`'s first stage, and E4 is clocked by
`lc2`'s second. Still open: the unit below them (y 9960-10340), where W3's clock comes from, and everything east
of x 5460 but the gate pair. The corner x 4400-4750, y 9100-9700 is in `eof`'s claim (run 6): the copies reach
into it (to x 4580), and the three bus tracks west of them are drawn through it because the copies' rows end on them.

Run 1 (dp111, 2026-11-18 04:48 +0100): the gate pair drawn on claude-opus (section "Gate pair at 6x"), reviewed
on claude-opus; it still needs its Fable review (re-read item R31). The inventory below was read at 0.62x and
1.22x; everything in it that is not in a later section is "seen", not traced.

## The counter: order of the stages (traced; cell copies checked against the master)

`lc2`'s west cluster is a flip-flop cell (`lc2_ff`, `notes/blocks/lc2.md`) and its copy turned 180 degrees. The
same cell stands twice more directly south of them, in this strip:

| Stage | Where | Placed as | Clock | Slave output (the next stage's clock) |
|---|---|---|---|---|
| W3 | x 4580-4990, y 9180-9960 | `@inst lc2_ff 0,780` | `lc3_w9904`, from the south (metal x 4554-4572 below y 9970) | `lc2_w8475` |
| `lc2`'s first (the master) | x 4580-4990, y 8350-9190 | the cell | `lc2_w8475` | `lc2_w8298` |
| `lc2`'s second | x 4990-5450, y 8370-9200 | turned copy | `lc2_w8298` | `lc2_w9034` |
| E4 | x 4990-5450, y 9150-9930 | `@inst lc2_ff 260,716 rot=180 o=4826,8810` | `lc2_w9034` | `lc2_w9210` |

So the chain runs up the west column and down the east one. A clock enters a stage at the end of its thin
metal by gate K4 (an L-shaped metal in the unturned stages, a pad in the turned ones) and the slave output leaves
by track C at the other end. The two outputs that `lc2`'s AND-OR-INVERT south of latch B takes are the last two
stages': `lc2_w9125` = NOT(`lc2_w9034` AND `lc2_w9079` OR `lc2_w9210` AND `lc3_w9299`). **Input identified, not
logic changed**: `lc2_w9210` was "row 5's metal, south into `lc3`"; it is E4's slave output (one metal from
`lc2`'s pad (5341,9211) to E4's pads (5343,9343) and (5343,9822)).

Extraction (`tools/t.sh lc3 netlist.py`). `tools/unsure.py --equations`, as for `lc2`'s stages: the second and
third of each stage FIRM; the first DEPENDS for its clear term (`lc2_w8450`: the cell's uncertain diffusion west
of the rail) and the fourth DEPENDS on the cell's uncertain strip to its load:

- W3: `lc3_w9342` = NOT(`lc2_w8450` OR `lc2_w8475` AND `lc3_w9904` OR `lc3_w9505`); `lc3_w9505` = NOT(`lc3_w9342`
  OR `lc3_w9472` AND `lc3_w9904`); `lc2_w8475` = NOT(`lc3_w9472` AND (`lc3_w9505` OR `lc3_w9904`)); `lc3_w9472` =
  NOT(`lc1_w7170` AND `lc2_w8475` AND (`lc3_w9342` OR `lc3_w9904`)).
- E4: `lc3_w9774` = NOT(`lc2_w8450` OR `lc2_w9034` AND `lc2_w9210` OR `lc3_w9696`); `lc3_w9696` = NOT(`lc3_w9774`
  OR `lc2_w9034` AND `lc3_w9644`); `lc2_w9210` = NOT(`lc3_w9644` AND (`lc3_w9696` OR `lc2_w9034`)); `lc3_w9644` =
  NOT(`lc1_w7170` AND `lc2_w9210` AND (`lc3_w9774` OR `lc2_w9034`)).

Believed, not established: with a stage 0 in the unit below (it has the cell's latch K in the west column and the
cell's gates K3 and K4, turned, in the east one), the counter would have five stages and the AND-OR-INVERT would
choose between its fourth and fifth outputs, which is what a cursor blink of 1/16 or 1/32 of the field rate
needs. Nothing drawn yet says what clocks the chain.

## Stage W3 (x 4580-4990, y 9180-9960): `lc2_ff` 780 px lower

Found by `tools/findcell.py 4700 8400 4960 9150 --region 4400,9100:6450,10500 --layer acid1b` (score 0.91 at
4830,9555). Checked: the cell's outline over both shots at 1.7x and 2.3x (`w3_*.png`, `p1ov_a.png`,
`p1ov_b.png`); master and copy side by side in three bands on the clean shot and the metal shot at 1.6x
(`mo_8390_*.png`, `mo_8650_*.png`, `mo_8910_*.png`: the same but for the ends); what lies under the west rail,
`tools/railprof.py 4758 4796 9130 9960` against `8350 9180`: the same run of nodes and gates, row for row.

The copy's own (not in the cell), each read here:

- **Its VSS contact**: the master has a column of contacts above gate K1 and a large open diffusion west of
  it; here the stage above ends 20 px higher (its node Z, y 9158-9174), and K1's VSS node (y 9200-9245) has
  one contact (4769,9214) (ring in the metal shot, dark spot in the clean shot: `p1_9170.png`, 3x). No open
  diffusion west of it (field).
- **Rails**: west x 4752-4802 (wider at y 9580-9718 and from y 9825, as the master's), middle x 4924-4980; both
  continuous from `lc2`'s (`p1_9170.png`, `p1_9370.png`, the overlays).
- **Track C** (x 4553-4571) runs on north from the pad of K1's row 2 (4561,9296) to `lc2`'s L-shaped metal
  (drawn there to y 9190): one metal, `tools/tl5_tracks.py v 4562 8690 10420` (metal y 9120-9780 with the pads
  9298 and 9775 and nothing else). That is the join that makes this stage's slave output `lc2`'s clock.
- **Track B** (x 4508-4526, `lc2_w8907`, which is `lc2_w8450` through `lc2`'s uncertain buried contact) comes
  from `lc2` (drawn there to y 8700) to the pad (4517,9384) of the clear row and runs on south (to a pad at
  y 10166, the unit below): `tl5_tracks.py v 4517 8690 10420`, one metal to y 10143.
- **Track A** (x 4466-4484, `lc1_w7170`) comes from `lc2` (drawn there to y 9060) and **ends** on the pad
  (4473,9818) of gate K4's row: `tl5_tracks.py v 4475 8690 10420` (metal to y 9823, pads 9038 and 9819; the
  short dark stretches at 9244-9253 and 9722-9730 are edges beneath, 8-9 px).
- **The clock's L**: from the end pad (4648,9904) of the thin metal x 4641-4655 a metal runs west (y 9900-9918)
  and south (x 4554-4572): `tools/textmap.py 4536 9876 4664 9990 4`. It runs on south past the pad (4561,10080)
  of the unit below and beyond y 10420 (not drawn below y 9970).

## Stage E4 (x 4990-5450, y 9150-9930): `lc2_ff` turned 180 degrees

`findcell` 0.75 (centre 5082,9561); a point (x,y) of the master is at (9912-x, 18336-y). Checked on overlays at
2.5x in both shots (`p2ov_9150_*.png`, `p2ov_9560_*.png`); `tools/railprof.py 5116 5152 9560 10000`.

- **Its top is what `lc2` drew by hand south of its east column** (`lc2`'s round 16: node `lc2_w9171`, the gate
  of `lc2_w9034`, the VSS contact (5124,9224), the strip x 5062-5078): that is this stage's gate K4, its lower
  node Z, its clock row and its VSS node. The two drawings lie on each other and extract as one transistor
  (112/21); `lc2`'s lines are left as they are (proposal in the handoff: delete them there). The contact's ring
  is at (5124,9224), where `lc2` has it; the cell's own contact lands 13 px off it on the same node.
- **Its clock** is `lc2_w9034`: `lc2`'s metal to the pad (5254,9208) lies on the copy's end pad (5264,9212)
  and thin metal x 5257-5271.
- **Its VSS contact** at the bottom of the column: ring (5137,9896), box x 5113-5160, y 9880-9923 (`e4bot.png`, 5x).
- **East rail**: x 5102-5150, with x 5086-5150 at y 9250-9300 and x 5084-5162 at y 9395-9552 (`tools/textmap.py`
  rows at twelve heights; it lies about 8 px west of the west rail's turned image, as in `lc2`).
- **Track C'** (x 5334-5352): one metal from `lc2`'s pad (5341,9211) through the end pad (5343,9343) to the pad
  (5343,9822) of K1's row 2, where it ends (`tl5_tracks.py v 5343 9150 10420`: metal y 9206-9824; the 18 px
  without metal at y 9215-9233 is the pad's ring, as at the other two pads).
- **Track B'** (x 5378-5394, `lc2`'s staircase line `lc2_w8907`): from `lc2` to the pad (5386,9735) of the clear
  row (bright centre in a ring in both metal shots, green hole in the clean shot: `tools/textmap.py 5366 9706
  5418 9760 3`); the metal ends at about y 9969.
- **Track A'** (x 5422-5438, `lc1_w7170`, `lc2`'s staircase line `lc2_w8474`): from `lc2` to the pad (5430,9298)
  of K4's row, and on to **a second pad (5428,9428)** (`textmap.py 5404 9404 5456 9452 3`: a contact), whose poly
  leaves east along y 9418-9440: not followed yet; it is in line with the lower inverter's output row
  (`lc3_w9432`), and if it is that row, that inverter drives `lc1_w7170`. The metal runs on south to a pad at
  about y 10084-10104 (drawn to y 9440).

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

`ports.d/lc3.txt`: inputs `lc3_w9470` (metal x 5560, south edge y 9520) and `lc3_w9299`
(metal x 5560, north edge y 9255); outputs `lc3_w9432`, `lc3_w9337` (poly rows at x 5540);
`vss` (x 5665-5712), `vcc` (wide metal x 5840-5890, named from the loads).

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

1. **The unit below the two stages**, x 4580-5450, y 9960-10400: the cell's latch K in the west column
   (`findcell` 0.89 at 4830,10151) and its gates K3 and K4 turned in the east one (0.71 at 5083,10152), by hand
   (half a cell cannot be placed). With it: W3's clock (`lc3_w9904`, the metal x 4554-4572 south of y 9970, which
   passes the pad (4561,10080)), track B's end (pad y 10166), track A' (pad about y 10084-10104), the rails'
   feet, the metals that turn west and east below y 10340.
2. **The gate pair's Fable review (R31)**, with the row from the pad (5428,9428) to the lower inverter's
   output (is it one poly?), the pad near (5515,9338) of the upper output, the tracks x 5517 and x 5560.
3. The track field x 5240-5570 south of y 9560, `rst_n`'s metal x 5465-5481 (it ends about y 10186).
4. Crossing field 5480-6450 x 9540-10050: which crossings are contacts.
5. The corner bundle, the south bundle, the wide metal's diagonal (inventory).
6. West of x 4580 (`urch`'s channel and `eof`'s corner): the metal x 4420-4442, the tan areas under and beside
   track A (x 4440-4480, y 9240-9650).

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
