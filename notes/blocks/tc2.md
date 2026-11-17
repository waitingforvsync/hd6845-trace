# tc2: top-centre random logic, lower half (x 6400-8250, y 4450-6400)

Trace: `trace/tc2.txt`. Ports: `ports.d/tc2.txt`. Views: `cache/scratch/tc2/`.
Tool: `tools/tc2_runs.py` (dark runs along a straight metal in both metal shots).

## Status (2026-11-17 22:50 +0000, dp111's session, run 1)

Most of this region was already drawn by other packages (`ras`, `rax`, `fld`, and the
crossing lines of `bust`, `amr`'s west route, `r9m`, `rde`): see the inventory. This package
adds what they left. Traced and extracted so far: 3 transistors, 1 new net, 1 equation
(FIRM), and five lines of other packages carried on. Nothing is marked `?`.

**Piece 1**

- `tc1_o3527` (cell B of `tc1`) from the island's south edge through the pad (6967,4481), a
  poly row and the pad (6490,4482) to a metal that leaves the region west at (6400,4482).
- `tc1_x1` from its contact (7055,4478) by poly and metal to a gate at (6500,5132).
- `tc1_p4308` from `tc1`'s pad (6620,4436) by metal and a poly row to (6400,5003), leaving west.
- The gate: `tc2_o5175` = NOR(`tc1_x1`, `fld_b_in`), with its load; the ground rail x 6537-6583
  between `tcw`'s piece and `fld`'s.

**Piece 2** (wiring only)

- `ras_o0_alt2` from the end of `ras`'s metal (6928,4786) on the row y 4786 to the pad
  (6447,4786) and west in metal past x 6400.
- `tc1_m6817` from `tc1`'s foot (6797,4372) south to the pad (6796,4829), the row y 4829, the
  pad (6492,4828), a metal through the nest west of the XOR cells to the pad (6533,6152), and
  a poly south past y 6400.

**Piece 3** (wiring only)

- The VCC rail through the crossing field, between `tcw`'s piece (to y 4455) and `fld`'s (from
  y 4990): `fld`'s rail, and with it the loads of `tc1_g`, `tc1_i` and `tc2_o5175`, is now
  joined to a labelled VCC rail by drawn metal (it was "VCC by the layout rule").

Not done: see the end.

## Inventory (survey at 0.68x in the metal and clean shots: `survey_m.png`, `survey_a.png`)

| Where | What | Drawn by |
|---|---|---|
| x 6430-6990, y 4450-4850 | crossing field: horizontal poly rows under vertical metals (the rail x 6537-6583, thin metals x 6400-6417, 6612-6634, wide ones x 6680-6740, 6790-6800, 6830, the rail x 6858-6908), a pad at each end of each row | rows y 4527 (`r9m`), 4568, 4613 (`amr`'s west route), 4657, 4700 (`bust`, `?P`), 4745 (`r9m`); **row y 4482: piece 1; rows y 4786 and y 4829: piece 2**. The VCC rail x 6687-6737: **piece 3**. Of the vertical metals the one at x 6830 is not drawn |
| x 6920-7900, y 4450-4800 | six bus metals and the fan of diagonal polys down to the selector | `r9m`, `amr`'s west route, `bust`, `ras`, `tc1`'s ends |
| x 6420-6710, y 5020-5290 | one NOR with its load (two pull-downs under the west edge of the rail x 6537-6583) | **piece 1** |
| x 6600-7050, y 5020-5275 | two inverters (`tc1_g`, `tc1_i`) | `fld` |
| x 6580-7030, y 5410-6100 | two copies of the comparator's XOR cell | `fld` |
| x 6400-6580, y 5350-6100 | a nest of metals turning from south to east; field pockets between them (clean shot khaki, chip-2 stripped shot red minus green 2-7: `tools/px.py pt` at (6490,5420)) | `fld`'s metal of `fld_y_b`; **`tc1_m6817`'s metal: piece 2**; the rest not drawn |
| x 7150-7420, y 4880-6000 | row address selector | `ras` |
| x 7430-7900, y 4500-6100 | nest of metals between the selector and its units | `ras`, `rde` |
| x 7860-8110, y 4700-5470 | five units, one per selector output | `rax` (pull-downs only) |
| x 8040-8250, y 4700-5470 | what stands east of the units (diffusions x 8050-8210, three thin metals): the units' loads are expected here | not drawn (`rax`'s Not done) |
| x 7830-8010, y 5770-5990 | comb of poly rows with a pad each (the five lines to `cdp2`'s comparator) | `ras` |
| x 7880-8250, y 5980-6320 | logic with heavy outlines (two or three gates) | **not drawn** |
| y 6100-6400 | wide horizontal supply metals with cross-unders; polys crossing south | a few polys (`fld`, `ras`, `amr`'s west route); the metals not drawn |

`tools/findcell.py` was not run: nothing in the undrawn parts repeats (one NOR; the logic at
x 7880-8250, y 5980-6320 was not looked at above 0.68x).

## Colours used (trap 1: calibrated here)

Calibrated on the two VSS contact boxes (6548,5092), (6548,5254) and on poly rows under the
rail x 6537-6583.

| | clean shot, under metal | clean shot, open | chip-2 stripped shot, open (red minus green) |
|---|---|---|---|
| poly | 215-224 / 155-170 / 117-124 | dark red-brown, green rim | 45-55 |
| diffusion | 198-204 / 161-175 / 130-139 | pinkish 165 / 115 / 105 | 20-33 |
| field | 190 / 120 / 126 | khaki 155 / 145 / 100 | 0-7 |

## Piece 1

### Logic (traced)

    tc2_o5175 = NOR(tc1_x1, fld_b_in)          FIRM (tools/unsure.py --equations)

| Device | Where | W/L | Gate | Between |
|---|---|---|---|---|
| pull-down 1 | (6500,5132) | 39/27 | `tc1_x1` | `tc2_o5175`, `vss` (contact (6548,5092)) |
| pull-down 2 | (6500,5219) | 39/28 | `fld_b_in` | `tc2_o5175`, `vss` (contact (6548,5254)) |
| load | (6676,5184) | 27/52 | `tc2_o5175` (buried contact (6627,5227)) | `tc2_o5175`, `vcc` (`fld`'s box, contact (6722,5200)) |

Build: a vertical diffusion strip x 6481-6520, y 5096-5250, just west of the rail; its two
ends are each one diffusion with a contact box under the rail; two gate polys cross it; the
part between them is the output node. A poly from the west (y 5161-5185) ends on the node in
a buried contact, and a diffusion band (y 5168-5186) leaves the node east under the rail to
the load: a poly block x 6650-6702 over the band's continuation (y 5170-5197), which ends in
the VCC contact box of `fld`'s lower inverter; the block's lower west corner has a tab into a
heavy-outlined box on a widening of the band (the tie).

**Believed, not traced**: with `fld`'s equations `fld_b_in` = `cnt_la_a_n` XOR `tc1_g`, and
`tc1_x1` = NOT `ras_o0_sel1` (`shm`; and see AMB-020: `tcw` drives the same line), so
`tc2_o5175` = `ras_o0_sel1` AND NOT (`cnt_la_a_n` XOR `tc1_g`) = `ras_o0_sel1` AND `tc1_i`.
Where `tc2_o5175` goes (west along y 5173 past x 6400) is not followed.

### Routes (each with its ends)

| Net | From | Path | To |
|---|---|---|---|
| `tc1_o3527` | `tc1`'s metal x 7003-7023 at y 4450 | metal to y 4492, west arm onto the pad (6967,4481); poly row y 4473-4491; pad (6490,4482); metal y 4470-4494 west | the region's edge (6400,4482); the follower gives the metal's end at (6012,4484), not looked at |
| `tc1_x1` | `tc1`'s metal x 7048-7068 at y 4450 | contact (7055,4478); poly south x 7057, diagonal (7057,4592)-(7017,4638), south x 7017, corner at y 4873, west along y 4865-4881 to x 6485, down into the pad (6492,4893); metal west to x 6450 and south | the pad (6450,5045), whose poly is pull-down 1's gate |
| `tc1_p4308` | `tc1`'s pad (6620,4436) | metal x 6612-6634 south; pad (6620,5002); poly row y 4993-5012 west | the region's edge (6400,5003); not followed |
| `fld_b_in` | `fld`'s row y 5345 (drawn there from x 6560) | row west under the rail to x 6423, corner, north along x 6423-6442 to y 5205, east | pull-down 2's gate; the row has no other end (field under the metal x 6397-6417) |
| `vss` | `tcw`'s rail (to y 4455) | one metal x 6537-6583 to y 5388, widening east to x 6625, west edge stepping to x 6575 at y 5445 | `fld`'s rail x 6575-6625 (from y 5400) |

Joins between named nets made by this piece: `tc1_o3527`, `tc1_x1`, `tc1_p4308`: each only
extended (no two existing names met). `fld_b_in` gained a gate. The rail joins `tcw`'s and
`fld`'s `vss` (both already `vss` by name).

### Self-check: ends (each viewed at the zoom given, and 50 px beyond)

| End | Seen | Result |
|---|---|---|
| `tc1`'s metal x 7013 onto the pad (6967,4481) | `pad2.png` (3.1x metal, clean), `padE.png` (4.5x chip-1 metal, both stripped), text map `textmap.py 6940 4455 7080 4505`, `follow.py 7013 4400 S` | one metal: ring 9 px either side of the contact's centre; a 6 px bar at x 6988-6991 (the pad's east edge under the metal); the follower turns west at y 4484. East of the pad: field |
| pad (6490,4482), metal west | `padw.png`, `padw2.png` (4x, four shots) | contact (ring, green centre); the poly ends at the pad (field west of it under the metal); the metal crosses the vertical poly x 6400-6420 without a pad |
| row y 4482 between the pads | `row4480.png` (2x), profile `px.py row 4481 6500 6960`, columns x 6700, 6850 | one row, y 4473-4491, no widening; read at 2x and by profile only |
| contact (7055,4478) | `pad2.png`, `padE.png`, `follow.py 7058 4400 S` (end (7054,4488)) | metal ends on the contact; poly leaves south |
| diagonal (7057,4592)-(7017,4638) | `x1diag.png` (4.6x, both stripped shots) | steps one track west; `ras`'s diagonal of `tc1_g` is separate (field between) |
| vertical x 7017, y 4638-4873 | `x1s.png` (2.6x), `x1s2.png` (3.3x), rows y 4700, 4840 | x 7008-7025 at both; crosses the bus metals without a pad; read below 4x |
| corner (7017,4873) and row y 4873 | `x1s2.png`, `row4877.png` (2x, three shots), columns x 6960, 6700 | row y 4865-4881; read at 2x and by profile only between x 6525 and 7005 |
| pad (6492,4893) | `x1pad.png`, `x1padm.png` (4.8x, four shots), `x1w.png` (4x) | the row turns down into the pad at x 6485-6510; contact; metal leaves west |
| metal (6492,4893) to (6450,5045) | `x1w.png`, text map `textmap.py 6420 4878 6480 5062` | continuous; bars of 6-9 px at y 4923, 4947, 4989, 5010 (edges of the rows y 4937 and 5003 underneath); the ring of the end contact |
| pad (6450,5045) | `lg2.png` (3.5x, both stripped shots), `lg1.png` (2.6x metal) | contact; the metal does not go on south; the poly does |
| `tc1`'s pad (6620,4436), metal south | `p4308top.png` (4.5x), `follow.py 6612 4700 N` and `S` | the metal starts on `tc1`'s contact and ends at (6622,5006) |
| pad (6620,5002), row west | `row5003.png` (4.2x, three shots) | contact; field east of the pad; the row passes under the metals x 6450 and x 6400-6417 without a pad and goes on west of x 6375 |
| row y 5345, west end | `g2row.png` (4.4x, three shots), rows y 5220, 5290 | corner at x 6423-6442; field under the metal x 6397-6417 west of it |
| row y 5345 at `fld`'s end (x 6560) | `g2row.png` | one poly under the rail |
| node poly, west | `g2s.png`, row y 5175 | salmon under the metal x 6397-6417 and red-brown west of it: goes on past x 6400 |
| band into the VCC box | row y 5183 (x 6580-6730), `lg3.png`, `lg4.png`, `lg4m.png` | the poly ends at x 6703, the box (tan under the rail) begins at x 6707 |
| rail, both ends | `rail.png` (1.25x), `railstep.png` (3x), `tc2_runs.py col 6560 4450 5445`, `col 6572` | no dark run over 21 px at x 6560 except the two contact rings (27, 29 px) and one of 33 px in chip 1 only (y 5354-5386; 10 px in chip 2); at x 6572 a run of 39 px at y 4901-4939 (`fld_a_in`'s poly jog lengthwise under the rail's east edge) and the two boxes |

### Self-check: widths

| Device | Measured | Result |
|---|---|---|
| pull-down 1 | `px.py row 5132 6425 6600` (three shots) | strip edges at x 6479 and 6517; the poly ends at x 6527, before the rail's metal; under the rail at this y the clean shot is grey-green 150/145/110 for 20 px (the halo of the contact box's lower edge 11 px above), then pink: no channel on the far side |
| pull-down 2 | `px.py row 5218 6425 6600` | the same edges; under the rail pink (field) |
| load | `px.py col 6667 5130 5260`, `col 6694` | strip y 5170-5197 between dark edges at y 5166-5170 and 5198-5202; the poly above (y 5152-5164) and below (y 5204-5240) has the colour of poly over field |

### Self-check: what was read below 4x or by eye

- The two long rows (y 4482, y 4873) and the vertical x 7017 between their ends: 2-3.3x and
  profiles. They are plain single lines in a field where every tap has a widened pad (trap 15).
- The diffusion between the band and the tie's box (x 6612-6641, y 5187-5210): in the clean
  shot it is khaki-green for about 10 px above the box (the box's rim); in the chip-2 stripped
  shot and the chip-2 metal shot the column x 6627 is uniform from y 5171 to 5202 (red minus
  green 16-20 and about 40: diffusion), and the heavy outline runs unbroken from the band's
  lower edge down the box's west side (`lg4.png`, `lg4m.png` 4.2x). Drawn firm. If it were
  not one diffusion the load's gate would not be tied to the output.

### Self-check: omissions (rings and outlined boxes inside the piece with no drawn item)

| Where | What it is |
|---|---|
| dark dot on the rail at (6545,5033), chip-2 metal shot | a blemish: chip 1's metal is whole there and the clean shot shows field (`textmap.py 6525 5015 6570 5050`) |
| outlined khaki boxes at x 6470-6525, y 5035-5095; x 6445-6525, y 5245-5330; x 6445-6530, y 5360-5470; x 6590-6650, y 5040-5150; x 6590-6680, y 5250-5290 | open field between the features (chip-2 stripped shot red minus green 2-7 at one point in each) |
| pale blob at (6500,5295) | residue on chip 1 only (chip-2 shots: field) |
| `tools/opendiff.py 6400 4450 6720 5480`: six green strips, 80 x 16 px, at x 6431-6514 beside rows of the crossing field | gaps between a row and the next metal: dark edge lines in the chip-2 shots (trap 3) |
| ring (6608,5300) and the poly east of it | `ras`'s pad of `ras_o0_alt1` (drawn there) |

## Piece 2 (wiring only; no transistor)

### Routes (each with its ends)

| Net | From | Path | To |
|---|---|---|---|
| `ras_o0_alt2` | the end of `ras`'s metal at (6922,4787) (its notes: "end not looked at") | contact (6928,4786) on a pad; poly row y 4778-4794 west; pad (6447,4786); metal y 4778-4798 west | the region's edge (6400,4788); the follower goes on west to x 6061, south, end (6059,4876): not looked at |
| `tc1_m6817` | `tc1`'s foot (6788-6826, y 4366-4380) | metal x 6789-6805 south; pad (6796,4829); poly row y 4821-4837 west; pad (6492,4828); metal west along y 4834 to x 6364, south to y 5525, east to x 6494, south to y 5902, east to x 6536, south; pad (6533,6152); poly x 6524-6544 south | the region's edge (6534,6400), going on south under the supply metals |

The stretch of `tc1_m6817`'s metal along x 6364 (y 4834-5525) lies 36 px west of this
package's region; it is drawn here so that the line is one piece.

Joins between named nets: none new (each line only carried on). `tc1_m6817` is the gate of
`tc1`'s cell D (`tc1_o2950` = NOT `tc1_m6817`), so the line is driven from its south end.

### Self-check: ends

| End | Seen | Result |
|---|---|---|
| the four pads (6447,4786), (6492,4828), (6796,4829), (6928,4786) | `pads2.png` (3.5x: chip-2 metal, chip-1 metal, clean) | each: bright centre in a dark ring in both metal shots, a green hole in the pad in the clean shot. (6447,4786): metal arrives from the west, poly leaves east. (6492,4828): the same. (6796,4829): metal arrives from the north, poly from the west. (6928,4786): metal leaves east, poly west |
| rows y 4786 and y 4829 between their pads | `rows2.png` (2.05x, three shots), `ov_rows2.png`, profiles `px.py row 4786 6460 6920 12`, `row 4829 6500 6790 12`, `col 6710 4768 4845` | poly throughout (salmon under the metals, red-brown in the gaps), y 4778-4793 and 4821-4836, no widening; read at 2x and by profile only |
| the wide metal x 6685-6758 over the row y 4829: it widens east by 18 px at y 4822 | `foot1.png`, `foot2.png` (4.8x, four shots), `textmap.py 6730 4805 6790 4850` | no contact: the metal is whole and bright over the row in both chips, the row keeps its width, no green hole |
| `tc1`'s foot and the metal south of it | `m6817.png` (4.6x, both metal shots and the clean shot), `textmap.py 6770 4405 6825 4470`, `tc2_runs.py col 6793 4380 4815` | the metal leaves the foot south at x 6789-6805; over `tc1_p4308`'s row (y 4438) it is whole in both chips with bars only at the row's edges and no hole in the clean shot: no contact. Chip 2: no dark run over 21 px; chip 1 has one of 36 px at y 4421-4456, which the text map resolves into the row's two edges |
| metal west of (6447,4786) | `pads2.png`, `tc2_runs.py row 4786 6400 6432` | on to x 6400 (bars of 9-10 px at the vertical poly x 6400-6420's edges) |
| the five corners of `tc1_m6817`'s metal: (6364,4834), (6364,5525), (6494,5525), (6494,5902), (6536,5902) | `corners_metal.png`, `corners_acid1b.png` (4x) | plain corners, no pad, ring or hole at any; the pad (6400,4870) beside the first is `fld`'s (`fld_y_b`) |
| the straight stretches between them | `tc2_runs.py col 6364 4845 5515`, `col 6494 5538 5890`, `col 6535 5912 6135`, `row 4834 6375 6475`, `row 5525 6378 6482`; `ov_r2.png` (0.9x overlay) | no dark run over 19 px in either chip |
| follower's contact candidate (6493,5615) and a blob at (6480,5925) in the clean shot | `blobs_acid.png`, `blobs_m1.png` (4x) | residue on chip 1's stripped die: nothing in chip 2's stripped shot, chip 1's metal whole |
| pad (6533,6152) | `r2end.png` (4.2x metal, clean) | contact; the metal ends on it; the poly leaves south. The pad (6485,6110) beside it is another net's (not drawn) |
| poly south of the pad | `r2south.png` (4.1x, y 6160-6450) | x 6523-6545, no pad, under the supply metals and on past y 6400; the poly x 6480-6500 beside it is the other pad's |

### Self-check: widths, weak spots, omissions

No transistor in this piece. Read below 4x: the two rows between their pads (as in piece 1).
Rings and boxes inside the piece with no drawn item: the pad (6485,6110) and its poly
x 6480-6500 going south (another net; Not done); the metal x 6830 (Not done); the wide metal
x 6685-6758 is piece 3; the pad (6558,5870)/(6535,5848) is `fld`'s.

## Piece 3 (wiring only): the VCC rail x 6687-6755, y 4455-4990

| Net | From | Path | To |
|---|---|---|---|
| `vcc` | `tcw`'s rail x 6687-6737 (to y 4455; `vcc` through `tc1`'s piece) | the same metal south to y 4822; it widens east to x 6755 at y 4822-4873; from y 4873 it is x 6703-6752 | `fld`'s rail x 6700-6750 (from y 4990) |

Seen: `vccstep.png` (3.2x, both metal shots and the clean shot: the widening, the step of the
west edge at y 4873, the meeting with `fld`'s rail); `ov_vcc.png` (1.6x overlay, both metal
shots, y 4430-5030); `ov_routes_m.png` (1.9x); rows `px.py row 4700 6670 6770`, `row 4940
6680 6770` (edges x 6686/6732 and 6706/6754); `tc2_runs.py col 6712 4330 5060 5` and `col 6728
4330 5060`: no dark run of 25 px or more at the same place in both chips (the longest, 30-36
px, are each in one chip only, where the edges of two rows lie 10 px apart). The stretch
y 4455-4800 was read at 1.6-2x and by these profiles only.

Under the rail in this stretch there are only the poly rows of the crossing field (y 4482 to
4958); none has a pad there, and the clean shot shows no diffusion box and no hole
(`row4480.png`, `rows2.png`, `row4877.png`, `foot2.png`). Omissions looked at: the dark dot on
the rail at (6712,4462) in chip 2's metal shot is a blemish (`spot.png`, 4.8x in four shots:
chip 1's metal whole, field in both stripped shots); the widening at y 4822 has no contact
(piece 2's table).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tc1_o3527` | M | x 6400, y 4470-4494 | out (of `tc1`) | goes on west; follower: end (6012,4484) |
| `tc1_p4308` | P | x 6400, y 4993-5012 | in (believed: its other end is a gate) | goes on west |
| `tc2_o5175` | P | x 6400, y 5161-5185 | out | the NOR's output, going west |
| `tc1_o3527` | M | x 7003-7023, y 4450 | in | from `tc1` |
| `tc1_x1` | M | x 7048-7068, y 4450 | in | from `tc1` |
| `tc1_p4308` | M | x 6612-6634, y 4450 | ? | `tc1`'s pad (6620,4436) is 14 px north of the edge |
| `fld_b_in` | P | x 6560, y 5337-5356 | in | `fld`'s row (inside the region; where this package's drawing meets `fld`'s) |
| `vss` | M | x 6537-6583, y 4450 | - | `tcw`'s rail |
| `vcc` | M | x 6687-6737, y 4450 | - | `tcw`'s rail |
| `ras_o0_alt2` | M | x 6400, y 4778-4798 | ? | goes on west; follower: end (6059,4876) |
| `tc1_m6817` | M | x 6789-6805, y 4450 | out (to `tc1`) | `tc1`'s foot (6797,4372) is 70 px north of the edge |
| `tc1_m6817` | P | x 6524-6544, y 6400 | in | going on south: the line's driver is that way (its other end is a gate in `tc1`) |
| `tc1_m6817` | M | x 6355-6373, y 4834-5525 | - | not a port: the stretch drawn 36 px outside the region |

## Ambiguities

None in piece 1.

## Not done

- `tc2_o5175`, `tc1_p4308`, `tc1_o3527`, `ras_o0_alt2` west of x 6400; `tc1_m6817` south of y 6400.
- The metal x 6830 of the crossing field.
- The pad (6485,6110) and its poly x 6480-6500 going south; the other metals of the nest
  x 6400-6580, y 5350-6100.
- The logic at x 7880-8250, y 5980-6320 (seen once at 1.7x, `br1.png`: a column of five or six
  horizontal polys over a vertical diffusion at x 7960-7975, a rail x 8030-8065 with contacts
  (8050,6030), (8050,6145), a rail x 8200-8240 with contacts (8215,6100), (8215,6260), a thin
  metal x 8105-8118; nothing drawn or decided).
- What stands east of `rax`'s units (x 8040-8250, y 4700-5470: `rax`'s own Not done); the
  supply metals and cross-unders y 6100-6400. Not looked at above 0.68x.
- The independent review of pieces 1 to 3 (the Review section below is empty).

## Review
