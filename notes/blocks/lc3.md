# lc3: left-centre random logic, part 3 of 3 (x 4400-6450, y 9233-10400)

## Status

2026-11-18 04:48 +0100. Gate pair drawn on claude-opus (`trace/lc3.txt`, ports `ports.d/lc3.txt`; section "Gate pair at 6x"); the rest of the region is survey only, not drawn. Not yet reviewed. Earlier text: survey only, **nothing was drawn** (no `trace/lc3.txt`, no ports file, no floor-plan
fragment). The inventory below was read at 0.62x and 1.22x (metal + acid1b), one gate pair
at 3-3.4x; everything in it is "seen", not traced. Stopped early on the coordinator's
instruction (budget). Views: `cache/scratch/lc3/` (`survey.png`, `qa`..`qd.png`,
`s1_*.png`, `g2_*.png`).

No other block has geometry inside the region: `urch`'s floor-plan box (x 4240-4720) and
`larr`'s "not surveyed" box (4450-4780 x 8250-10500) overlap it, but the all-blocks render
shows only one drawn item, a short horizontal piece near (4800-4975, 9737), owner not looked up.

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

Everything. Suggested order:
1. Gate pair 5540-5900 x 9260-9520: boxes and load gate tie resolved (review round 1);
   still the channel width (profile poly y 9470 over x 5640-5740), the tracks `lc3_m5626`
   and `lc3_m5756` beyond the piece; then follow the west row y 9428 to its end (a pad was seen near (5250,9440)
   at 1.22x) and the tracks x 5560 and x 5517.
2. Crossing field 5480-6450 x 9540-10050: which crossings are contacts.
3. Logic columns A and B (4680-5240), rails first; try `findcell.py` with `tl1`/`tl5` cells
   (not tried).
4. West tracks and track field: join to `urch` and to `lc2` at y 9233.
5. Whose the drawn piece near (4800-4975, 9737) is.

## Review
