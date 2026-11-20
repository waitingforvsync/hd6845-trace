# tc2: top-centre random logic, lower half (x 6400-8250, y 4450-6400)

Trace: `trace/tc2.txt`. Ports: `ports.d/tc2.txt`. Views: `cache/scratch/tc2/`.
Tool: `tools/tc2_runs.py` (dark runs along a straight metal in both metal shots).

## Status (2026-11-18 01:22 +0000, dp111's session, run 4)

Most of this region was already drawn by other packages (`ras`, `rax`, `fld`, and the
crossing lines of `bust`, `amr`'s west route, `r9m`, `rde`): see the inventory. This package
adds what they left. Traced and extracted so far: 17 transistors (one NOR, a nine-transistor
latch, the loads of `rax`'s five units), 12 new named nets, 8 equations (the NOR and the five
unit inverters FIRM, the latch's two marked), seven lines of other packages carried on, two
lines of the nest west of the XOR cells (three now), the VCC rail of the units and the latch,
the two wide supply metals of y 6100-6400, and the supply metal that links `fld`'s rails.
Pieces 1 to 10 are through independent review; pieces 11 to 16 (run 4) are not. After run 4
and its sweep of the whole region the Not done list says exactly what is left.

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
  joined by drawn metal to `tcw`'s rail of that name. The metal join is real; the supply
  identity is still by the layout rule for both rails, because `tcw`'s labels are that rule
  too (AMB-014; review round 1).

**Piece 4** (run 2; not yet through an independent review round)

- The logic at x 7760-8250, y 5960-6300: a latch of two cross-coupled gates, 9 transistors,
  `tc2_sr_q` = NOR(`tc2_sr_q_n`, `tc2_sr_c`, `tc2_sr_g` AND `cdp1_lw1`) and
  `tc2_sr_q_n` = NOR(`tc2_sr_q`, `tc2_sr_g` AND `tc2_sr_s`), both loads traced. One poly join
  (12 px, in a gap between two metals) is marked `?`: both equations depend on it.
- Its lines: `tc2_sr_g`, `tc2_sr_s` and `tc2_sr_q` south past y 6400 in metal; `tc2_sr_q` also
  east past x 8250 in poly; `cdp1_lw1` north to the pad (7836,5520), east in poly to the pad
  (8031,5520) and onto a thin metal that runs over `rax`'s units to `cdp1_lw1` (piece 7); `tc2_sr_c` onto the top
  line of `cdp2`'s channel 2 (y 6367), drawn from its west pad (7490,6367) to x 8250, and its
  metal west past x 6400.
- The ground rail from `rax`'s piece (y 5645) to y 6400, and the VCC rail x 8206-8248 from
  y 5960 to y 6400 (joined by drawn metal to `tc1`'s VCC bus in piece 8).

**Piece 5** (run 2, wiring only; not through a review round)

- `tc1_p4308` and `lc3_w9947`: the two other metals of the nest west of the XOR cells, each
  from the region's west edge to a pad ((6490,6108), (6447,6150)) and on south in poly past
  y 6400.

**Piece 6** (run 2, wiring only; not through a review round)

- The ground rail on the east side of the crossing field (y 4380-4990), from `tc1`'s piece to
  `fld`'s. The dark dots on it are not contacts (4x, four shots, against a known contact).

**Piece 7** (run 3, wiring only; not through a review round)

- `cdp1_lw1` north of the pad (8031,5520): one thin metal x 8022-8040 over `rax`'s units 2, 3
  and 4 without a contact, the pad (8031,5066), a poly row east along y 5066, the pad
  (8291,5066), a metal north and east to the pad (8353,4981): the west end of `cdp1_lw1`. So
  the latch's line the wire `tc2` called sr_r **is `cdp1_lw1`** (declared by an alias (dropped at the rename of 2026-11-19)), the
  line that crosses the central datapath's channel and the bus field to x 15584.

**Piece 8** (run 3; not through a review round)

- The east half of each of `rax`'s five units: the load (W 68 / L 37) with its gate tied to
  the output band by a buried contact, and its contact to the VCC rail. With `rax`'s
  pull-down each unit is an inverter, `rax_o#` = NOT `ras_o#`, FIRM for all five.
- The VCC rail x 8117-8163 from `tc1`'s piece (y 4450) to its turn east at y 5754-5812 and on
  as the rail x 8205-8248 of the latch: the five unit loads and the latch's two loads are on
  drawn VCC.

**Piece 9** (run 3, wiring only; not through a review round)

- `ral_stb`, the strobe of the RA latch cells, south of `tc1`'s end (8205,4450): its thin metal
  down to the pad (8204,5672), with one contact on the way ((8204,5371), a poly east past
  x 8250); a poly row west along y 5673 to the pad (7748,5673); a metal south to the pad
  (7750,6065); a poly west, south and west to the pad (7488,6282); a metal south and west
  along y 6328 past x 6400. No transistor in this region; the line's source is west of x 6400.

**Piece 10** (run 3, wiring only; not through a review round)

- `tc2_r5718`: the line of the pad (7791,6152): a poly row y 5718 from past x 8250 west to the
  pad (7791,5718), a metal south to the pad (7791,6152), a poly west, south and west to the pad
  (7530,6324), a metal south past y 6400. Neither end is followed.

**Piece 11** (run 4, wiring only; not through a review round)

- `tc1_ns3` south of `tc1`'s end (7902,4450): its thin metal over `rax`'s five units, with no
  contact to their output boxes (measured against the line's own end contact), to the pad
  (7899,5633); a poly row west along y 5632, a poly south along x 7605, the pad (7660,6193),
  a metal south past y 6400. No transistor in this region.

**Piece 12** (run 4, wiring only; not through a review round)

- `tc2_r5589`: the line of the row y 5589: from the pad (8248,5262) (whose poly goes on east)
  a metal south, the pad (8246,5589), the row west, the pad (7488,5586), a metal south and
  west, the pad (7422,6065), a poly, the pad (7384,6282), a metal west along y 6283, the pad
  (6840,6282), a poly south past y 6400. No gate on it in this region.

**Piece 13** (run 4, wiring only; not through a review round)

- The L at the east end of `sl_eq_r5_n`'s row y 4676: south, east to the pad (8246,4716), a metal
  to the pad (8290,4850), a poly east that ends in a box at `cdp1`'s west edge (8370,4850),
  read as a buried contact onto a diffusion there (not traced). It joins no named net.

**Piece 14** (run 4, wiring only; not through a review round)

- `tc2_m6404`: the fourth pad of the nest, (6404,6107): its metal from the west edge, its poly
  south past y 6400; no contact to the ground metal or the two thin metals it passes under.

**Piece 15** (run 4, wiring only; not through a review round)

- The two wide supply metals of y 6100-6400: VCC (`fld`'s VCC rail, a band y 6105-6155, a
  south leg x 7695-7752) and VSS (`fld`'s west ground rail, a band y 6198-6243, a south leg
  x 7572-7620), each joined by drawn metal to a named rail. No contact and no diffusion under
  them here. `fld`'s east ground rail was drawn 73 px too far and is corrected in `fld`'s file.

**Piece 16** (run 4, wiring only; not through a review round)

- The supply metal between `fld`'s rails, which nobody had drawn: the inverters' VCC rail to
  the XOR cells' VCC rail (and that rail's gap at y 5690-5760), and the inverters' east ground
  rail to the XOR cells' east ground rail. Found by the sweep (a scan for undrawn metal).

**The sweep** (run 4): the whole region with every block's geometry, in ten tiles and three
scans: see "The sweep of the whole region".

Not done: see the end.

## Inventory (survey at 0.68x in the metal and clean shots: `survey_m.png`, `survey_a.png`)

| Where | What | Drawn by |
|---|---|---|
| x 6430-6990, y 4450-4850 | crossing field: horizontal poly rows under vertical metals (the rail x 6537-6583, thin metals x 6400-6417, 6612-6634, wide ones x 6680-6740, 6790-6800, 6830, the rail x 6858-6908), a pad at each end of each row | rows y 4527 (`r9m`), 4568, 4613 (`amr`'s west route), 4657, 4700 (`bust`, `?P`), 4745 (`r9m`); **row y 4482: piece 1; rows y 4786 and y 4829: piece 2**. The VCC rail x 6687-6737: **piece 3**. The ground rail on the east side (x 6838-6926): **piece 6** |
| x 6920-7900, y 4450-4800 | six bus metals and the fan of diagonal polys down to the selector | `r9m`, `amr`'s west route, `bust`, `ras`, `tc1`'s ends |
| x 6420-6710, y 5020-5290 | one NOR with its load (two pull-downs under the west edge of the rail x 6537-6583) | **piece 1** |
| x 6600-7050, y 5020-5275 | two inverters (`tc1_g`, `tc1_i`) | `fld` |
| x 6708-6840, y 5235-5405; x 6795-6840, y 5690-5760; x 6881-7014, y 5290-5440 | the supply metal between the inverters' rails and the XOR cells' rails | **piece 16** |
| x 6580-7030, y 5410-6100 | two copies of the comparator's XOR cell | `fld` |
| x 6400-6580, y 5350-6170 | a nest of metals turning from south to east; field pockets between them (clean shot khaki, chip-2 stripped shot red minus green 2-7: `tools/px.py pt` at (6490,5420)); each ends on a pad with a poly going south | `fld`'s metal of `fld_y_b`; **`tc1_m6817`'s metal: piece 2; `tc1_p4308`, `lc3_w9947`: piece 5; the fourth pad (6404,6107), `tc2_m6404`: piece 14** |
| x 7150-7420, y 4880-6000 | row address selector | `ras` |
| x 7430-7900, y 4500-6100 | nest of metals between the selector and its units | `ras`, `rde` |
| x 7860-8110, y 4700-5470 | five units, one per selector output | `rax` (pull-downs only) |
| x 8040-8170, y 4700-5470 | the units' east halves: per unit a load (diffusion x 8062-8167, poly block x 8083-8120, contact under the rail) and its tie (row and buried contact box x 8021-8048) | **piece 8** |
| x 8117-8163, y 4450-5812; y 5754-5812 to x 8248 | the VCC rail of the units, turning east to the latch's rail | **piece 8** |
| x 8022-8040, y 5066-5520; row y 5055-5078, x 8016-8308 | the thin metal over units 2-4 and the row east of its north pad (the wire `tc2` called sr_r = `cdp1_lw1`) | **piece 7** |
| x 8068-8082 | `db_b6`'s thin metal over the loads' output side, no contact | `bust`, `rde` |
| x 8198-8212, y 4450-5680 | `ral_stb`'s thin metal: a contact (8204,5371) with a poly going east, an end pad (8204,5672) | `tc1` to y 4450; **the rest: piece 9** |
| y 5663-5683, x 7730-8224; x 7742-7757, y 5666-6072; x 7476-7770, y 6049-6297; y 6316-6340, x 6400-7500 | `ral_stb` on: a poly row, a metal, a poly in three legs, a metal going west | **piece 9** |
| x 8170-8262, y 4676-4730 | the east end of `sl_eq_r5_n`'s row y 4676: it turns south at x 8186 and east to a pad (8246,4716), whose metal goes east and south to a pad (8290,4850) | **piece 13** |
| x 8235-8262, y 5250-5600 | a pad (8248,5262) and a thin metal x 8240-8258 south to a pad (8246,5589) on the row y 5578-5598 | **piece 12** (`tc2_r5589`) |
| x 7894-7909, y 4450-5640; y 5622-5643, x 7597-7918; x 7597-7612, y 5622-6203; x 7643-7678, y 6177-6400 | `tc1_ns3`: thin metal over `rax`'s units to the pad (7899,5633), a poly row west, a poly south, the pad (7660,6193), a metal south | `tc1` to y 4450; **the rest: piece 11** |
| y 5578-5598, x 7472-8266; x 7480-7500, y 5580-6075; x 7378-7440, y 6048-6300; y 6274-6292, x 6825-7402; x 6835-6851, y 6264-6400 | `tc2_r5589` west of its east pad: the row, a metal south and west, a poly west and south, a metal west, a poly south | **piece 12** |
| x 7830-8010, y 5770-5990 | comb of poly rows with a pad each (the five lines to `cdp2`'s comparator) | `ras` |
| x 7760-8250, y 5960-6300 | a latch: two cross-coupled gates (a diffusion stack of five gates x 7977-8073, two columns x 8106-8136, two loads x 8148-8198) and the pads of its lines | **piece 4** |
| x 7730-7810, y 6040-6170 | two pads, (7750,6065) and (7790,6152), at the south ends of metals from `ras`'s channel pads (7748,5673) and (7790,5718); each has a poly going west and south | (7750,6065) is `ral_stb`'s: **piece 9**; (7791,6152) is `tc2_r5718`'s: **piece 10** |
| y 6100-6400 | two wide supply metals: VCC (from `fld`'s VCC rail, band y 6105-6155, south leg x 7695-7752) and VSS (from `fld`'s west ground rail, band y 6198-6243, south leg x 7572-7620); vertical polys crossing under them; no contact, no diffusion | **piece 15**; the polys: `fld`, `ras`, `amr`'s west route, pieces 2, 5, 9-12, 14 |

`tools/findcell.py` was not run: nothing in the undrawn parts repeats (one NOR; one latch,
whose two halves are not copies of each other: the upper has three pull-down paths and the
lower two, and the columns and loads differ in their ties).

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

## Piece 4: the latch at x 7760-8250, y 5960-6300 (run 2, 2026-11-17)

Views (all in `cache/scratch/tc2/`): `g1_acid1b.png`, `g1_metal.png`, `g1_acid.png` (3.2x, the
whole piece in three shots), `g1_W1.png` (4x, x 7955-8120, clean and chip-2 stripped),
`g1_E1.png`, `g1_E1b.png` (4x, x 8075-8240, four shots), `g1_NE.png`, `g1_SE.png` (4.3x, four
shots), `g1_dc1top.png` (4.6x), `g1_gap.png`, `g1_tie.png`, `g1_swbox.png` (6.3-6.5x),
`g1_arm.png` (11x), `g1_S.png` (4x), `g1_N_a.png`, `g1_N_m.png` (4x), `g1_wpads.png` (4.2x),
`g1_pads1.png`, `g1_pads2.png` (4.2x tiles, three shots), `g1_Wm.png` (2.4x), `g1_bnorth.png`
(2.1x), `g1_crow.png` (1.5x), `g1_cpadw.png` (5x), `g1_cmet.png` (0.94x), `g1_cend.png` (2.6x),
`rails_m.png` (1.6x), `g2_r_a.png` (2.9x), `g2_m8030.png` (4.2x tiles), `ov_g2_m8030.png` (2.4x); overlays `ov_g1_a.png` (3.6x, clean), `ov_g1_m.png` (2.6x, metal).
Survey notes: `cache/scratch/tc2/survey-g1.md`. Tools written for it: `tools/tc2_q4.py` (four
shots of one rectangle), `tools/tc2_tiles.py` (several small squares, one row per shot),
`tools/tc2_items.py` (drawn items of all blocks in a rectangle).

Colours here (clean shot, under metal; `tools/px.py pt`): poly over field 213-220/160-165/110
(rows B, D, E under the metals x 7836 and x 7880), poly over a channel 236-249/166-178/115-128,
diffusion 188-200/175-184/130, field 187/125/125 (pink). In a gap of 10-25 px between two
metals the clean shot shows only dark bars and green rims (trap 2): every decision in such a
gap was made in the chip-2 shots or by a profile, and is listed below.

`tools/findcell.py` was not used: there is one latch, and its two halves differ.

### Logic (traced)

    tc2_sr_q   = NOT(tc2_sr_c | (tc2_sr_g & cdp1_lw1) | tc2_sr_q_n)     DEPENDS on one ?P
    tc2_sr_q_n = NOT((tc2_sr_g & tc2_sr_s) | tc2_sr_q)                  DEPENDS on one ?P

(`tools/unsure.py --equations`: both DEPENDS. The one uncertain item is the 12 px of poly that
joins the gate of `tc2_sr_q_n`'s pull-down to `tc2_sr_q`'s load poly; Ambiguity 1.)

A latch with a common gate line: while `tc2_sr_g` is high, `cdp1_lw1` high pulls `tc2_sr_q`
low and `tc2_sr_s` high pulls `tc2_sr_q_n` low (so `tc2_sr_q` high); `tc2_sr_c` high pulls
`tc2_sr_q` low at any time. **Believed, not traced**: what the five lines are. `tc2_sr_c` is
the top line of `cdp2`'s channel 2; the wire `tc2` called sr_r is `cdp1_lw1` (traced in run 3, piece 7: a line that
comes through the central datapath's channel from x 15584; its source is not followed); `tc2_sr_g`, `tc2_sr_s` and `tc2_sr_q` go south along x 7837, 7791
and 7922.

| Device | Where | W/L | Gate | Between |
|---|---|---|---|---|
| A | (8025,6026) | 96/22 (the extraction gives 103: the row's jog) | `tc2_sr_g` (row A) | `vss` (contact (8053,5982)), node A-B |
| B | (8025,6068) | 96/26 | `cdp1_lw1` (row B) | node A-B, `tc2_sr_q` |
| C | (8000,6150) | 47/26 | `tc2_sr_c` (row C) | `tc2_sr_q`, `vss` (contact (8060,6155)) |
| D | (8019,6193) | 84/20 | `tc2_sr_g` (row D) | `vss` (the same contact), node D-E |
| E | (8019,6239) | 84/22 | `tc2_sr_s` (row E) | node D-E, `tc2_sr_q_n` |
| upper column's gate | (8126,6027) | 24/26 | `tc2_sr_q_n` (east piece of row A's track) | `vss` (the top diffusion), `tc2_sr_q` |
| lower column's gate | (8122,6192) | 30/19 | `tc2_sr_q` (west arm of its load's poly; the join is `?`) | `vss` (the ground box), `tc2_sr_q_n` |
| load of `tc2_sr_q` | (8173,6098) | 27/50 | `tc2_sr_q` (tie box (8106-8126, 6113-6132)) | `tc2_sr_q`, `vcc` (contact (8227,6114)) |
| load of `tc2_sr_q_n` | (8174,6282) | 28/47 | `tc2_sr_q_n` (buried contact (8116-8148, 6220-6250)) | `tc2_sr_q_n`, `vcc` (contact (8227,6263)) |

Build. One diffusion x 7977-8073, of which x 7977-8024 lies in the open (outlined, its west
edge a dark line through every row in all three shots) and the rest under the ground rail
x 8030-8075. From the top: a contact box under the rail (5965-6000) with the top diffusion
(y 5990-6012), row A, row B, node `tc2_sr_q` (y 6083-6113; in the open down to row C), row C
(over the open part only: under the rail there is field, then the ground contact box
x 8042-8100, y 6127-6170), the ground node (y 6163-6185), row D, row E, node `tc2_sr_q_n`
(y 6250-6294). Below row C the diffusion's east edge is x 8061. East of the rail, under the
thin metal of `db_b6` (x 8108-8126), two diffusion columns x 8106-8136: the upper from the top
diffusion (which runs east above row A's track to x 8138) down to node `tc2_sr_q`, which
reaches it along y 6090-6110; the lower from the ground box (which reaches it along
y 6150-6178) down to node `tc2_sr_q_n`, which reaches it along y 6266-6288. Row A's track
holds two polys: the row from the west ends at x 8086, and a separate piece x 8098-8152
crosses the upper column and ends in the pad (8168,6028), whose metal runs south to the pad
(8166,6243); that pad's poly ends on the lower column in a buried contact and runs on down as
the gate of `tc2_sr_q_n`'s load. `tc2_sr_q`'s load is a poly block x 8148-8198 over a strip
from the upper column to a VCC box; the block's poly goes on south with an arm east (out of
the region) and an arm west across the lower column.

### Routes (each with its ends)

| Net | From | Path | To |
|---|---|---|---|
| `tc2_sr_g` | pad (7878,6022) of row A | metal south x 7870-7890, west along y 6100-6122, south x 7827-7847 through the pad (7837,6193) of row D | the region's edge (7837,6400); follower: end (7835,7218), not looked at |
| `cdp1_lw1` | pad (7837,6064) of row B | metal north x 7826-7846 over ten poly rows without a pad; pad (7836,5520); poly east y 5510-5530 under the thin metal x 7902 and `rax`'s ground rail (no gate: field on both sides); pad (8031,5520); thin metal x 8022-8040 north | the pad (8031,5066) north of `rax`'s unit 2, and from there to `cdp1_lw1` (piece 7) |
| `tc2_sr_c` | pad (7880,6155) of row C | metal south x 7869-7889; pad (7880,6368) on the poly row y 6358-6376 | the row's west end, the pad (7490,6367), from which a metal y 6360-6380 goes west to the region's edge (6400,6370) (follower: end (6184,6370) on a pad); and east along the row to the region's edge (8250,6367), going on (to x 11000 by `amr`'s notes) |
| `tc2_sr_s` | pad (7790,6258) of row E | metal south x 7782-7800 | the region's edge (7791,6400); follower: end (7791,6958) |
| `tc2_sr_q` | pad (7922,6108) on the poly that ends on the node | metal south x 7913-7931 | the region's edge (7922,6400); follower: end (7922,7046) |
| `tc2_sr_q` | the load's poly at (8162,6170) | poly east y 6163-6180 under the VCC rail | the region's edge (8250,6172), going on east past x 8320 |
| `tc2_sr_q_n` | pad (8166,6243) | metal north x 8156-8178 | pad (8168,6028); no other branch |
| `vss` | `rax`'s rail (x 7931-7985 to y 5645, step x 7945-8035 at y 5600-5650) | one metal x 7990-8040 to y 5945, widening east to x 8075 at y 5888-5945, then x 8030-8075; bulge to x 8092 at y 6095-6212 | the region's edge (8052,6400), going on |
| `vcc` | (8227,5960), where piece 8's rail arrives from `tc1`'s VCC bus | metal x 8206-8248 south | the region's edge (8227,6400); `cdp2` draws a `vcc` rail at x 8229 from y 7425 |

Joins between named nets made by this piece: none between two existing names. The ground
rail is joined by drawn metal to `rax`'s `vss`. `rde`'s `db_b6` metal passes over both
columns without a contact (below).

### Self-check: ends (each viewed at the zoom given, and 50 px beyond)

| End | Seen | Result |
|---|---|---|
| row A's east end (8086,6029) and the start of the east piece (8098,6027) | `g1_dc1top.png` (4.6x, four shots), `g1_gap.png` (6.5x), `px.py row 6022 8064 8124 3` and `row 6028` (three shots) | two polys: between x 8091 and 8099 both chip-2 shots are green (G over R: 133/140, 94/117; 136/138, 106/117) between the dark outlines of two rounded ends; the clean shot is khaki there. The row from the west is channel-bright to x 8070 and ends about x 8086 |
| row B's east end (8088,6068) | `g1_gap.png`, `px.py row 6068 7962 8092 4` | channel to x 8070, edge at x 8074, end cap x 8078-8086, then dark and the upper column's edge |
| row C's east end (8036,6150) | `g1_W1.png`, `px.py row 6150 7962 8092 4` | poly-coloured to x 8032 (202/157 at x 8030: poly over field under the rail), dark outline at x 8034-8042, then the ground box's tan. In the chip-2 stripped shot the row is orange to x 8002 and unclear from there to the rail (fringes): the end's exact x is from the clean shot |
| rows D and E, east ends (8073,6193), (8072,6239) | `g1_SE.png`, `g1_W1.png`, `px.py row 6192 8048 8096 3`, `row 6238 8048 8108 3` (four shots) | channel to x 8058, edge at x 8062, poly to x 8072; then field (pink 184-197/124 in the clean shot under the rail's bulge; green in both chip-2 shots for 12 px) |
| west arm's west end (8096,6192) | `px.py row 6192 8096 8160 3` | poly from x 8096; dark at x 8090-8093; field west of that |
| the vertical poly's south end (8162,6203) | `g1_SE.png` | rounded end at y 6203; field (pink) below |
| east arm at the region's edge (8250,6172) | `g1_pads2.png` third tile (4.2x, three shots, x 8225-8325), `px.py row 6172 8170 8290 6` | goes on east under the next metals; orange-brown in the bare gap x 8255-8282 of both metal shots |
| the stub (7957-8003, 6267-6297) | `g1_swbox.png` (6.4x, four shots) | a poly that ends at both ends; lighter box with a heavy outline on the strip's corner; nothing leaves it |
| pad (7922,6108) and the poly to the node's box | `g1_pads1.png` (4.2x), `g1_W1.png` | ring and bright centre in both metal shots, green hole in the clean shot; metal leaves south only (follower north: end (7919,6108)); the poly ends in nested rings at x 7977-8005 |
| pads (7878,6022), (7790,6258) | `g1_pads1.png` | contacts; metal leaves south only at each; (7790,6258)'s pad is 13 px east of another net's vertical poly x 7748-7760 (field between) |
| pads (7837,6064), (7837,6193), (7880,6155), the L's corner | `g1_wpads.png` (4.2x, clean and both metal shots) | (7837,6064): its metal arrives from the north; between its ring (to y 6082) and the L's upper edge (y 6100) there is no metal in either chip. (7837,6193): the L's leg runs into its ring and on south. (7880,6155): metal leaves south |
| pad (7880,6368) on the row y 6367 | `g1_pads2.png` first tile, `g1_cend.png` | contact on a widening of the row; the metal ends on it; the row goes on both ways |
| pad (7490,6367), the row's west end | `g1_cpadw.png` (5x, four shots) | contact; the poly leaves east only, the metal west only; the thin metal x 7523-7545 crosses the row 35 px east of it without a pad |
| pad (7836,5520) | `g1_pads2.png` second tile | contact; metal leaves south only; the poly leaves east |
| the poly y 5510-5530 from x 7850 to x 8015 | `g2_r_a.png` (2.9x, clean and chip-2 metal) | one poly, plain width; salmon under the thin metal x 7902 and under `rax`'s rail, pink field above and below it there (no diffusion: no gate); **read below 4x** |
| pad (8031,5520) and the metal north of it | `g2_m8030.png` first tile (4.2x, three shots), `ov_g2_m8030.png` (2.4x overlay) | ring and bright centre in both metal shots, green hole; the poly arrives from the west and ends; the metal leaves north only and is plain to y 5468 |
| pads (8168,6028), (8166,6243) and the metal between | `g1_dc1top.png`, `g1_SE.png`, `g1_E1.png`, `follow.py 8168 6100 S` and `N` | contacts at both ends, (8166,6248) to (8168,6026); no branch |
| metals south of the pads to y 6400 | `ov_g1_m.png` (2.6x), `g1_cend.png` (2.6x); followers from (7838,6300), (7926,6300), (7793,6290) | straight, no pad to y 6400; **read below 4x** |
| `cdp1_lw1`'s metal, y 5530-6050 | `g1_bnorth.png` (2.1x, three shots), `follow.py 7836 6040 N` | straight; the ten rows it crosses keep their width under it (no pad); **read below 4x** |
| the row y 6367 between its pads and to x 8250 | `g1_crow.png` (1.5x, both stripped shots) | one row; **read below 4x**; `amr`'s notes say the three top rows of channel 2 are straight from x 7500 to 11000 |
| the metal y 6370 west of the pad (7490,6367) | `g1_cmet.png` (0.94x, both metal shots and the clean shot), `tc2_runs.py row 6370 6190 7475 2`, `follow.py 7470 6366 W` | inside the region (x 6400-7475) no dark run over 19 px in chip 2 or over 22 px in chip 1 (x 7282-7303), and none at the same place in both; **read below 4x** |
| ground rail, y 5645-5950 | `rails_m.png` (1.6x), `g1_N_m.png` (4x from y 5850), `tc2_runs.py row` at y 5700, 5850, 5915 | one metal; **read below 4x** north of y 5850 |
| VCC rail at y 5960 | `rails_m.png`; piece 8's `e_turn.png` | the rail goes on north to a turn at y 5754-5812 (drawn in piece 8) |

### Self-check: widths (the gate profiled past both channel ends)

| Device | Measured | Result |
|---|---|---|
| A, B | `px.py row 6025 7962 8092 4`, `row 6068` | west edge: dark at x 7974-7978; channel-bright (237-248) x 8026-8066 under the rail; east edge: dark at x 8074. In the open part (x 7978-8022) the rows are speckled bright in the clean shot where they are dark red west of x 7975 |
| C | `row 6150` | x 7978 to the rail's edge line at x 8014-8022; under the rail the poly is over field (202/157). The strip's east edge is taken as x 8024 (the rail's margin hides it): W 47 +- 8 |
| D, E | `row 6193`, `row 6240` | west edge x 7974-7978; channel to x 8058; edge at x 8062 |
| upper column's gate | `row 6022`, `row 6028`, `px.py row Y 8094 8154 3` at y 6000, 6044, 6056, 6066, 6080, 6100 | on the gate: poly over field x 8103-8110 (207-233/147-162), a dark line at x 8112-8115, channel (247-254) x 8118-8137, dark at x 8140. The column is x 8106-8134 above and from y 6056 down, x 8118-8136 at y 6044 |
| lower column's gate | `row 6192`, rows y 6160, 6172, 6212, 6280 | dark at x 8105-8108, channel x 8111-8132, dark at x 8135; column x 8106-8136 |
| load of `tc2_sr_q` | `px.py col 8188 6060 6130 3`, `col 8162 6060 6215 4`, `row 6097 8095 8250 4` | strip y 6085-6110 between dark edges at y 6081 and 6112 (R 242-247 over it, 209-229 above and below); poly x 8148-8198; the strip is tan without an edge from the column through x 8136-8146 (`row 6100`) and ends in the VCC box at x 8203 |
| load of `tc2_sr_q_n` | `g1_S.png`, `g1_SE.png`, `row 6280` | speckled bright poly (in the open) x 8147-8197 over y 6267-6297; tan through x 8136-8146 |

### Self-check: what was read below 4x or decided in a gap

- The lines marked **read below 4x** above.
- **The top diffusion is one piece from the contact box to the upper column** (so that the
  upper column's gate has `vss` above it): the clean shot is tan through x 8075-8087 at y 6002
  with no edge (at y 6048 there is a dark edge at x 8075), and both metal shots and the chip-2
  stripped shot show one top edge line at y 5990 from x 7975 to x 8151 (`g1_dc1top.png`).
  Between x 8088 and 8103 the clean shot is a gap bar.
- **Node `tc2_sr_q` reaches the upper column** along y 6090-6110: tan in the clean shot under
  the rail's bulge (`g1_gap.png`); reddish in both chip-2 shots at x 8091-8100, y 6102.
- **Node `tc2_sr_q_n` reaches the lower column** along y 6266-6288: the gap x 8088-8103 is a
  bar in the clean shot. `px.py col 8095 6196 6312 4` (four shots, 5 x 5 patches): between
  dark edges at y 6256-6264 and y 6288-6292 a band that is redder than the field above and
  below it in every shot (clean +45..50 against -19..+7; chip-2 stripped +12..19 against
  -3..-13; chip-2 metal +29..37 against +7..19; chip-1 metal +27..44 against +10..15). Drawn
  firm. If it were not there, `tc2_sr_q_n`'s load and column would be a second gate of their
  own and the stack D-E would have no load.
- **The tie of `tc2_sr_q`'s load**: a box x 8108-8124, y 6113-6131 under `db_b6`'s metal, tan
  inside (207/175/130) with an outline, separated from the column above by a faint line in the
  clean shot (126/115/90); and a poly tab from the block to it along y 6117-6133, which is
  orange-red through x 8132-8147 in both chip-2 shots and chip 1's metal shot (R 125-169,
  R-G +16..+68) where the field 18 px south is green or neutral. Drawn firm.
- **The west arm's join to the vertical poly, x 8135-8152**: marked `?` (Ambiguity 1).
- A tiny ring with a bright centre at (8148,6126), 12 px across, at the block's lower west
  corner where the tab leaves it: in the clean shot plain, a red dot in the chip-2 stripped
  shot. Too small for a contact and no metal is above it. Not drawn.

### Self-check: omissions (rings in the metal shots and outlined boxes in the clean shot with no drawn item)

| Where | What it is |
|---|---|
| pads (7752,6062) and (7790,6152), their metals from the north and their polys going west | two other nets (`ras`'s Not done: the metals from its channel pads (7748,5672) and (7790,5718)); not drawn |
| `db_b6`'s metal over both columns and the tie box: bright between dark crossings at y 5990-6012, 6112-6130 | no contact: the clean shot under it is plain tan with no green hole (`g1_tie.png`, `px.py col 8116 6090 6160 3`); the dark crossings are the edges of the diffusions underneath in both chips |
| dark dot on the ground rail at (8040,6280), chip-2 metal shot | a blemish: chip 1's metal is whole and the clean shot plain (`textmap.py 8025 6265 8060 6295 3`) |
| dark dots on the VCC rail at about (8232,5979) and (8222,6025) | the clean shot under the rail is field (pink) there: no contact. Not looked at above 3.2x |
| outlined khaki or pink areas: x 7950-8020, y 5952-5988; x 8143-8195, y 5955-6000; x 8152-8190, y 6045-6068; x 8175-8200, y 6135-6160; x 8072-8097, y 6175-6260; x 7950-8020, y 6300-6345; x 8135-8195, y 6305-6350 | field between the features (khaki in the open, pink under metal); the thin dark curve at (8158-8195, 5980-5995) is residue on chip 1 |
| the slots x 8078-8100, y 6048-6100 and y 6205-6258 between the rail and `db_b6`'s metal | the upper: row B's end cap and the gap bar; the lower: field (green in both chip-2 shots, `px.py row 6240`) |
| nested rings at (7977-8005, 6092-6122), (8116-8148, 6220-6250), (7975-8005, 6264-6296) | the three buried contacts, drawn |

## Piece 5 (wiring only): the two other lines of the nest west of the XOR cells (run 2)

| Net | From | Path | To |
|---|---|---|---|
| `tc1_p4308` | the region's edge (6400,5567), a metal arriving from the west (follower: from (6318,4999) south along x 6320, east along y 5563) | metal east along y 5557-5577 to x 6448, south x 6438-6458 to y 5938, east to x 6490, south x 6480-6500; pad (6490,6108); poly south x 6483-6501 | the region's edge (6492,6400), going on south under the supply metals |
| `lc3_w9947` | the region's edge (6400,5611), a metal arriving from the west (follower: from (6276,4825) south along x 6271, east along y 5607) | metal south x 6396-6416 (on the region's edge) to y 5981, east to x 6447, south x 6437-6457; pad (6447,6150); poly south x 6443-6460 | the region's edge (6451,6400), going on south |

Joins between named nets: none (two new names; neither end is followed). Which end drives
is not known.

Self-check (ends, each with what lies beyond):

| End | Seen | Result |
|---|---|---|
| pads (6490,6108), (6447,6150) | `g2_pad6485.png` (4.6x, four shots) | each: ring and bright centre in both metal shots, a green hole in the pad in the clean shot; the metal arrives from the north and ends on the pad, the poly leaves south. Field between the three pads of the nest ((6533,6152) is `tc1_m6817`'s) |
| corners (6490,5938), (6448,5938), (6447,5981), (6406,5981) | `g2_nest1.png` (4.4x, chip-2 metal and clean) | plain corners over field, no pad, ring or hole |
| corners (6448,5567), (6406,5611) and both exits at x 6400 | `g2_nest2.png` (4.4x) | plain corners; both metals go on west of x 6400. A speck on `tc1_p4308`'s metal at (6430,5571) in chip 2's metal shot only (the clean shot is plain field there) |
| the straight stretches | `ov_g2_nest.png` (1.9x overlay, metal and clean), `follow.py 6489 6070 N`, `6449 6100 N` | field under them throughout; **read below 4x** |
| the polys from the pads to y 6400 | `g2_polyS.png` (4x, clean, chip-2 stripped, chip-2 metal; y 6125-6415) | each keeps its width under the four horizontal metals (y 6195-6245, 6315-6340, `tc2_sr_c`'s y 6360-6380, `amr`'s west route y 6407-6419): no pad; both go on past y 6400 |

No transistor. Rings and boxes inside the piece with no drawn item: a fourth pad of the nest
at (6404,6108), on the region's west edge, whose metal comes from the west along y 6015-6040
(`ov_g2_nest.png`); not drawn (Not done). Blobs on the green rims of the metals in the clean
shot at about (6384,5652), (6465,5610): residue (run 1 found the same kind at (6493,5615)).

## Piece 6 (wiring only): the ground rail east of the crossing field, y 4380-4990 (run 2)

| Net | From | Path | To |
|---|---|---|---|
| `vss` | `tc1`'s rail x 6858-6908 (drawn there to y 4380) | one metal: x 6860-6907 to y 4435; x 6838-6905 to y 4497; x 6840-6884 to y 4858; x 6838-6926 to y 4903; x 6882-6926 | `fld`'s rail x 6879-6925 (from y 4990) |

So `fld`'s ground rail (the pull-downs of `tc1_g` and `tc1_i`) is joined by drawn metal to
`tc1`'s rail of that name.

**The dark dots on the rail are not contacts.** Run 1 saw small dark dots at about (6860,4585),
(6860,4610), (6862,4628), (6865,4780), (6870,4890) "in both metal shots". At 4x in four shots
(`g3_dots.png`: chip-2 metal, chip-1 metal, clean, chip-2 stripped, with the west rail's
contact (6548,5092) in the same image for comparison):

| | The dots | The known contact (6548,5092) |
|---|---|---|
| chip-2 metal | specks of 6-8 px at (6862,4573), (6862,4630), (6870,4800), (6867,4893); a ring of 8 px at (6892,4390) | a dark ring 30 px across with a bright centre |
| chip-1 metal | specks at other places, 10-15 px from chip 2's: (6868,4587), (6875,4632), (6865,4795); none near (6867,4893) | the same ring and centre |
| clean | the crossing field's poly rows at their plain width and field (pink) between them: no box, no pad, no hole | a tan box with dark specks |
| chip-2 stripped | rows and green field | a box with black pits |

The specks do not repeat at the same places on the two chips, none has a ring with a bright
centre, and nothing lies under any of them. A dark dot in the clean shot at (6852,4813), in
the field under the rail, has nothing in either metal shot: residue.

Self-check:

| End or stretch | Seen | Result |
|---|---|---|
| meeting `tc1`'s rail at y 4380 | `g3_steps.png` first tile (4x, chip-2 metal and clean, x 6800-6950, y 4345-4495) | one metal, bright on through the edges of the rows y 4383-4401, 4428-4447; it widens west to x 6838 from y 4435, rounded corner |
| meeting `fld`'s rail at y 4990 | `g3_steps.png` second tile (y 4855-5005) | x 6838-6926 at y 4858-4903, x 6880-6927 below, onto `fld`'s piece |
| the widths and the step at y 4497 | `tools/tc2_runs.py row Y 6820 6940 1` at y 4480, 4505, 4545, 4590, 4680, 4765, 4810, 4840, 4895, 4912 and `row Y 6800 6960 1` at y 4400, 4445, 4460, 4985 (both metal shots); `ov_g3_rail.png` (1.9x overlay, both metal shots and the clean shot); run 1's `vssE.png` (1.9x) | chip 2: 6844-6902 at y 4480, 6839-6869 at y 4505 and 4545 (chip 1: 6840-6884: the stretch x 6870-6884 is dirty in chip 2), 6840-6883 from y 4590 to 4840, 6838-6925 at y 4895, 6884-6925 at y 4912. **The stretch y 4497-4858 was read at 1.9x and by these profiles**, with four 62 px squares of it at 4x |
| under the rail | `g3_dots.png`, `g3_steps.png`, `ov_g3_rail.png` (clean) | the rows y 4392 to 4958 cross without a pad; the pads of the rows' east ends stand at x 6910-6940, 20 px or more east of the rail's edge |

No transistor, no contact. Omissions: the specks (table above).

## Piece 7 (wiring only): `cdp1_lw1` from the pad (8031,5520) to `cdp1_lw1` (run 3, 2026-11-18)

Views: `e_survey.png` (1.5x), `e_line8031.png` (2.6x, the whole metal in both metal shots and
the clean shot), `e_m5.png` (2x mosaic of the five units), `e_m345.png` (3x), `e_pads4.png`
(3.7x tiles, four shots), `e_u1w.png` (6x, unit 1 in four shots), `e_u3w.png`, `e_u3a.png`
(4.4-4.5x), `e_bc.png` (4.5x), `e_top.png` (4.4x), `e_row5066.png` (2x), `e_pad8290.png`
(3.9x), `e_pads_r.png` (4.5x tiles, four shots), overlay `ov_p7.png` (3.3x).

**The question (former Ambiguity 4), answered.** The thin metal x 8022-8040 is one line from
the pad (8031,5520) to the pad (8031,5066), and it has no contact on the way.

| What was asked | Seen | Result |
|---|---|---|
| one line or pieces | `e_line8031.png`; `px.py col 8030` over each band | one line: both edge lines unbroken from y 5080 to 5505 in both chips; under it the clean shot (chip 1) has protected colours throughout (pink field, tan band and box, salmon end caps), where units 0 and 1, which have no metal there, show the same features in open colours. Over each unit's band (20 px between two edge lines) it is dark for 25-30 px with metal between the edges: 190-195/170 at y 5159-5161 and 176-191/167-186 at y 5418-5420 in chip 2; at unit 3 chip 2 is dark throughout (dirt), chip 1 has 154-162/102-135 at y 5288-5290. `tc2_runs.py` fails along most of this metal (thin and dim: trap 19) and is not used |
| the spots (8030,5133), (8030,5262), (8030,5392): `rax`'s "poly pads with a metal contact" | `e_m5.png`, `e_pads4.png`, `e_u1w.png`; `px.py row 5262 8012 8046 3`, `row 4893`, `row 5527` | not contacts. Each is the end cap of the selector output's poly: x 8021-8040, 25 px tall, the poly's own width (not widened). Units 0 and 1 are the same cell with the same cap and no metal over it. The "ring" in the metal shots is the cap's outline under the metal and the bright centre the metal between its edge lines (bright only over x 8024-8031; the cap's east end outline darkens x 8033-8040). No hole in the clean shot: 198/135/79, 242/177/108, 214/177/130, 132/126/99 and then the outline, where the contact (8031,5520) has green over red for 15 px. Three contacts on one line would also short `ras_o2`, `ras_o3`, `ras_o4` |
| the spots (8031,5180), (8031,5308), (8031,5440) | `e_bc.png`, `e_mb.png`, `e_u0tie.png` | not contacts: the unit's buried contact box (piece 8) under the metal; bare in units 0 and 1 |
| what `rax` drew there | `trace/rax.txt` | nothing: no metal at x 8031 and no contact (its notes say "short pieces (profile)" and "a metal contact"; both are corrected here and in the handoff). Its trace stops the selector output's poly at x 8002; the poly goes on to x 8040 as the end cap (over field east of x 8017: geometry only, nothing changes). `trace/rax.txt` is not changed |

### Route (with its ends)

| Net | From | Path | To |
|---|---|---|---|
| `cdp1_lw1` (= the wire `tc2` called sr_r) | pad (8031,5520) (piece 4) | metal x 8022-8040 north over units 4, 3, 2 (no contact); pad (8031,5066); poly row y 5055-5078 east under `db_b6`'s metal, the VCC rail and `ral_stb`'s metal; pad (8291,5066); metal x 8282-8300 north over `db_b6`'s row y 5024, east along y 4970-4990 | pad (8353,4981), the west end of the poly that `cdp1` draws from x 8340 as `cdp1_lw1` |

**Join between named nets: the wire `tc2` called sr_r = `cdp1_lw1`** (an alias (dropped at the rename of 2026-11-19); no `?` item on
the path: `tools/unsure.py` does not list it). `cdp1_lw1` crosses the central datapath's
channel (y 4981, stepping to y 5024) without a contact (`cdp1`) and the bus field to x 15584,
where a poly goes south (`bust`: not followed). Which end drives is not known: row B of the
latch is a gate, so the driver is beyond x 15584 or on a part not followed. The last 125 px
(x 8250-8375) lie east of this package's region and were not drawn by anyone.

### Self-check: ends

| End | Seen | Result |
|---|---|---|
| pad (8031,5066) | `e_top.png` (4.4x, clean and both metal shots), `e_pads_r.png` (4.5x, four shots) | ring and bright centre in both metal shots, green hole in the pad, pits in the chip-2 stripped shot. The metal ends on it: bare ground north of it to y 4985. The poly leaves east only (field west) |
| row y 5055-5078, x 8045-8275 | `e_top.png`, `ov_p7.png` (3.3x), `e_row5066.png`; `px.py row 5066 8040 8284 4`; `textmap.py 8062 5046 8092 5088`, `8192 5046 8222 5088`; `tc2_runs.py col 8140 5045 5090` | one poly: salmon under the three metals, and in each bare gap (x 8092-8108, 8172-8188, 8220-8268) poly-orange in chip 1's metal shot (R-G 40-80; field there 20). Under `db_b6`'s metal, the rail and `ral_stb`'s metal the metal is whole with two edge bars of 6-13 px and the clean shot has no hole: no contact |
| pad (8291,5066) | `e_pads_r.png`, `e_pad8290.png` (3.9x), `follow.py 8291 5040 S` (end (8290,5072)) | contact (ring, bright centre, green hole). The poly ends in the pad (khaki field east of it to x 8880 at 2x); the metal leaves north only |
| metal over `db_b6`'s row (8291,5024) | `e_pad8290.png`, `ov_p7.png`, `textmap.py 8276 5006 8306 5042` | no contact: metal whole between the row's two edge bars, the row uniform under it |
| corner (8291,4980) | `e_pad8290.png` (3.9x), `ov_p7.png` (3.3x), `follow.py 8291 5040 N` (corner (8294,4982) east) | plain corner; bare ground north of it. **Read at 3.9x** |
| pad (8353,4981) | `e_pads_r.png`, `textmap.py 8328 4958 8384 5004` | contact: bright centre (B-E) in a ring (2-4) in both metal shots, green hole 12 px across in the pad. The metal ends at the ring (x 8375); the poly leaves east only (pink field west of the pad under the metal's arm) |

No transistor. Read below 4x: the corner (3.9x) and the row between its crossings (3.3x and
profiles). Omissions: the dark dot on the VCC rail at (8152,4987) in chip 2's metal shot is a
blemish (chip 1's metal whole, field under it: `textmap.py 8134 4970 8170 5000`).

## Piece 8: the loads of `rax`'s five units, and the VCC rail (run 3, 2026-11-18)

Views: `e_u3a.png` (4.4x, unit 3, clean and chip-2 metal), `e_comp_a1b.png` (6.6x, median of
the five units, composite `tc2_rxu`), `e_eastA.png`, `e_eastB.png` (2.9x, all five),
`e_m345.png`, `e_m5.png`, `e_mb.png` (mosaics, four shots), `e_u3tie.png`, `e_u0tie.png`
(4.8x, four shots), `e_u1box.png` (6x), `e_bc.png` (4.5x), `e_rail.png` (0.82x), `e_turn.png`
(3.5x, both metal shots), `e_turn_a.png` (4x, clean), `e_railtop.png` (4x), `e_c4712.png`
(3.8x); overlays `ov_p8a.png` (3.6x, units 0 and 1), `ov_p8b.png` (3.3x, units 2 to 4).
Tool: `tools/tc2_loadchk.py` (the channel's extent and the band's opening, per copy, as text).

`tools/findcell.py 8045 5222 8172 5342` (the unit's east half) finds the five units and
nothing else in x 7990-8260, y 4650-5500: scores 0.82-0.90 in the clean shot, 0.85-0.88 in
the metal shot, at dy -499, -369, -130, 0, +130. No cell of another block was tried: the
unit is one load on `rax`'s inverter.

### Logic (traced; the pull-down is `rax`'s)

    rax_o# = NOT ras_o#     (# = 0..4)          FIRM, all five (tools/unsure.py --equations rax_o)

| Device (master: unit 3) | Where | W/L | Gate | Between |
|---|---|---|---|---|
| load | (8102,5276) | 68/37 | `rax_o3` (buried contact box (8021-8048, 5300-5323)) | `rax_o3`, `vcc` (contact (8138,5272)) |
| pull-down (`rax`) | (7945,5262) | 112/20 as `rax` draws it | `ras_o3` | `vss`, `rax_o3` |

Build (unit 3; the others are copies). `rax`'s output band (y 5280-5300, drawn there to
x 8048) runs on east into a diffusion x 8062-8167, y 5242-5310. A poly block x 8083-8120,
y 5229-5336 crosses it; east of the block the diffusion ends in a contact under the VCC rail.
Below the diffusion the block's poly runs west as a row y 5318-5336, to a heavy-outlined box
x 8021-8048, y 5300-5323 that hangs under the band: a buried contact, which ties the load's
gate to the output. `db_b6`'s thin metal (x 8068-8082) lies over the load's output side and
the thin metal of `cdp1_lw1` (piece 7) over the box of units 2-4: neither has a contact.

**Not `rax`'s guess**: its notes listed as load candidates "a vertical diffusion x 8052-8085
with a vertical poly x 8085-8100 beside it and a poly blob at (8058-8085, y+56..+73)". The
vertical diffusion is the load's output side, the poly the west third of the gate block, the
blob the tie's row.

### Self-check: widths and copies (`tools/tc2_loadchk.py`; `px.py col 8088 5218 5346 3`, `col 8114`, `row 5275 8050 8176 3`)

| Copy | Channel-bright in the clean shot at x 8088 / x 8114 (R over 235) | Band's row against a field row, x 8054-8066: darkest red, chip 2 / chip 1 | Overlay |
|---|---|---|---|
| unit 0 (dy -499) | y 5248-5298 / 5247-5301 (in the master's frame) | band 92 / 99; field 56 / 64 | `ov_p8a.png` |
| unit 1 (dy -369) | 5246-5305 / 5249-5304 | 88 / 101; 63 / 64 | `ov_p8a.png` |
| unit 2 (dy -130) | 5247-5306 / 5247-5305 | 100 / 99; 66 / 75 | `ov_p8b.png` |
| unit 3 (master) | 5247-5306 / 5247-5305 | 103 / 109; 62 / 75 | `ov_p8b.png` |
| unit 4 (dy +130) | 5247-5305 / 5248-5304 | 80 / 96; 54 / 66 | `ov_p8b.png` |

- The gate past both channel ends (master): at x 8088 the cap y 5229-5237 is poly over field
  (194-222/140-161), the diffusion's edges are dark at y 5239-5242 and 5309-5314, the channel
  bright (243-254) between, then poly over field again (163-195/106-151, the row) to y 5334
  and pink field from y 5338. The same at x 8114. W 68 (edge to edge 5242-5310).
- The gate is one poly 37 long, not two strips: its middle x 8095-8110 is in the gap between
  `db_b6`'s metal and the rail, bare in both metal shots, and is poly-orange there at y 5234,
  5275 and 5326 (chip 2 146-185/89-147, chip 1 118-147/45-107) where y 5222 and 5342, outside
  the block, are field (chip 1 73-121/56-102) (`px.py row Y 8084 8114 3`).
- **The band joins the load's diffusion** (the gap x 8048-8062 between the two thin metals
  hides the junction in the clean shot of units 2-4, and the metal's own edge hides it in the
  metal shots): on a field row (y 5255) the clean shot has a bright green gap x 8048-8056 and
  the diffusion's dark outline x 8058-8064, and both metal shots a dark outline (54-75); on
  the band's row (y 5290) the clean shot is tan to x 8048, has the gap's dark bar x 8052-8058
  and is tan again from x 8062, with no green and no outline, and the metal shots have no
  dark outline (80-109, the metal's edge alone). The same in all five copies (table).
- **The tie.** In units 0 and 1 nothing covers the box: in both chip-2 shots and chip 1's
  metal shot it is a heavy-outlined box with a lighter centre and the row leaving from under
  it, like the known buried contact (7990,6106) beside it in `e_bc.png`; in the clean shot
  (open there) nested rings. In units 2-4, under the thin metal, the clean shot shows it tan
  inside a dark outline, with the band above (tan) and the row below (salmon) (`px.py col 8034
  5270 5348 3`; `col 8072` for the row: salmon y 5320-5334). Drawn firm.

### Self-check: ends

| End | Seen | Result |
|---|---|---|
| block's top cap (y 5229) and bottom (y 5336) | `e_u3a.png`, `e_comp_a1b.png`, columns x 8088, x 8114 | field above (pink) and below (pink from y 5338); the open strip between the metals is field at y 5222 and 5342 |
| row's west end (under the box) | `e_mb.png` (3.3x, four shots, all five), `e_u0tie.png`, `px.py col 8054 4790 4850 3` and `col 8034` (unit 0, bare) | the row y 4821-4837 (unit 0) runs from the block west under the box and ends there; field (green pocket (8050-8058, 4806-4815)) between it, the band and the box's east side |
| diffusion's east end (x 8167) | `e_u3a.png`, `px.py row 5275` | edge at x 8166-8170 under the rail's east edge; the strip east of it is the gap between the rail and `ral_stb`'s metal (field) |
| the rail at y 4450 (meeting `tc1`'s) | `e_railtop.png` (4x, both metal shots and the clean shot) | one metal x 8118-8162 across y 4450; under it the poly rows of the bus field and pink field, no pad |
| the rail, y 4450-5750 | `e_rail.png` (0.82x), `segs.py 8090 8262` at twelve y (x 8118-8127 to 8158-8163 in both chips), `e_eastA.png`, `e_eastB.png` (2.9x) | one metal; **read below 4x** between the units |
| the turn | `e_turn.png` (3.5x, both metal shots), `e_turn_a.png` (4x, clean) | the west leg ends at y 5812, the horizontal part is y 5754-5812 from x 8117 to x 8248, the east leg x 8205-8248 goes south from y 5754 and is piece 4's rail from y 5960. The dark lines across the metal are the edges of `ras`'s rows y 5749-5944; the clean shot under the turn shows the rows at their plain width and pink field: no pad, no hole |

### Self-check: omissions

| Where | What it is |
|---|---|
| dark dots on the rail at (8140,4712) and (8152,4987), chip-2 metal shot | blemishes: chip 1's metal is whole (C-E) at both; under the first the clean shot is field with the yellow-green drift that this rail's field has between all the units (a scan of the clean shot down the rail finds it at y 4699-4738, 4819-4834, 4949-4989, 5179-5198, 5316-5346, 5449-5553: trap 15), no box and no pad (`e_c4712.png`, `textmap.py 8122 4696 8158 4728`, `8134 4970 8170 5000`) |
| the five rings on the rail at (8138, y+10) | the load contacts, drawn |
| end caps of the selector outputs' polys (x 8021-8040) and the diffusion's east edge at x 8017 above the poly | `rax`'s (its trace ends the poly at x 8002 and the diffusion at x 8000; reported in the handoff, not changed) |
| green pockets at (8050-8058, y+44..+52) and the green strips x 8045-8058 between the units | field between the features, and the gap between the two thin metals |
| green blob with a dark ring at (8190,4890) in the clean shot | residue in the gap between the rail and `ral_stb`'s metal; both metal shots plain there (`e_eastA.png`) |
| the thin metals x 8198-8212 (`ral_stb`) and x 8240-8258, the pads (8205,5368), (8205,5668), (8250,5262), (8245,5590), (8245,4716) | other nets: Not done |

## Piece 9 (wiring only): `ral_stb` from (8205,4450) to the region's west edge (run 3, 2026-11-18)

Views: `e_rail.png` (0.82x), `e_pads_e.png` (4x tiles, four shots: the pads (8204,5371),
(8204,5672), (8248,5262), (8246,5589)), `e_east2.png` (2.4x), `e_rows56.png` (2.7x),
`e_rows56w.png` (2.65x), `e_sw_a.png`, `e_sw_m.png` (2.4x), `e_p9a.png`, `e_p9b.png` (4.2x),
`e_p9c.png` (4x tiles, three shots), `e_p9d.png` (4.2x); overlays `ov_p9row.png` (2.5x),
`ov_p9poly.png` (3.3x), `ov_p9m.png` (2.25x).

| Net | From | Path | To |
|---|---|---|---|
| `ral_stb` | `tc1`'s thin metal x 8198-8212 at y 4450 | the metal south to its end pad (8204,5672), with one contact, (8204,5371) | (a) from (8204,5371): a poly east along y 5359-5379 to the region's edge (8250,5369) (it runs on to x 8425, where it hooks north, through what stands east of the region: seen at 2.4x, not drawn there) |
| | pad (8204,5672) | poly row y 5663-5683 west under the VCC rail, `db_b6`'s metal, `cdp1_lw1`'s thin metal, the ground rail, `tc1_ns3`'s metal and `cdp1_lw1`'s metal; pad (7748,5673); metal x 7742-7757 south over `ras`'s comb rows; pad (7750,6065); poly west along y 6055-6075 to x 7703, south along x 7703-7721 under the wide metal x 7690-7770, west along y 6270-6292; pad (7488,6282); metal south to y 6340 and west along y 6316-6340 | (b) the region's edge (6400,6328), going on west (follower: to x 6104, north, end (6012,6068), not looked at) |

Joins between named nets: none new (`ral_stb` only carried on; the extraction's net count is
unchanged). The line gates the five `ral` cells far to the east; nothing in this region
drives it, so its source lies beyond (6400,6328) or on the poly east of x 8250. **`trace/ral.txt`'s
and the glossary's remark that the pad (8205,5672)'s poly "runs east" is not what the photos
show**: that pad's poly goes west (this row); the poly that goes east is the one from the
contact (8204,5371).

### Self-check: ends and crossings

| End or crossing | Seen | Result |
|---|---|---|
| meeting `tc1`'s metal at y 4450 | `e_p9c.png` first tile (4x, both metal shots and the clean shot) | one metal x 8198-8212 across y 4450 |
| the metal y 4450-5672 | `e_rail.png`, `follow.py 8205 5000 S` (end (8203,5680)) and `N`, `segs.py 8090 8262` (x 8199-8211 at twelve y), `tc2_runs.py col 8205 4440 5665 2`; a scan of the clean shot down x 8200-8210 for green over red | one metal. The scan finds only the two contacts (y 5366-5379, 5672-5683) and a weak 15 px at y 4888-4902. Dark runs of 25 px or more at the same place in both chips: only the contact (8204,5371). Chip 2 alone is dark at y 4770-4793 and dim over the rows y 5024 and y 5066 (chip 1 bright there; the clean shot protected). **Read below 4x** between the tiles |
| the rows it crosses: bus field y 4460-4690, the L of `sl_eq_r5_n` y 4707-4725, `db_b6` y 5024, `cdp1_lw1` y 5066, the row y 5589 | `e_p9c.png` tiles 1, 2; `textmap.py 8180 4694 8226 4736`, `8192 5046 8222 5088`; `e_rows56.png` | no pad on any: the metal is whole between each row's two edge bars and the clean shot shows the row uniform under it |
| (8205,4895), the scan's weak spot and the follower's candidate | `e_p9c.png` third tile | not a contact: a notch in the metal's east edge in chip 2 only; field under the metal; the green blob with a dark ring beside it at (8190,4890) is residue in the gap west of the metal |
| contact (8204,5371) | `e_pads_e.png` first tile | ring and bright centre in both metal shots, green hole in a pad x 8188-8222; the metal goes on south; the poly leaves east only |
| the poly at x 8250 | `e_east2.png` (2.4x) | goes on east under the thin metal x 8240-8258 (no pad) and beyond; **read at 2.4x** |
| pad (8204,5672) | `e_pads_e.png` second tile | contact; the metal ends on it (bare ground south); the poly leaves west only (khaki field east of the pad) |
| the row y 5663-5683 | `ov_p9row.png` (2.5x, three shots), `e_rows56.png`; the scan along y 5668-5678 | one poly from pad to pad, no widening and no hole between; orange-brown in the bare stretches of both metal shots. **Read below 4x** |
| pad (7748,5673) | `e_p9d.png` (4.2x, three shots), `follow.py 7748 5700 N` (end (7748,5672)) | contact (ring, bright centre, green hole). The poly leaves east only (field west); the metal leaves south only: the horizontal metal 20 px north of the ring (y 5625-5640, one of `ras`'s lines) is separate (dark for 15 px between; the follower stops at the pad) |
| the metal x 7742-7757, y 5690-6050 | `follow.py 7748 5700 S` (end (7749,6070)), `tc2_runs.py col 7749 5680 6050 2` (runs of 8-19 px at `ras`'s rows), the scan | one metal, no pad on the rows it crosses. **Read by profile and at 2.4x** |
| pad (7750,6065), the poly's first corner | `e_p9a.png` (4.2x, clean and chip-2 metal) | contact (ring, green hole); the metal ends on it; the poly leaves west (orange-brown L in the bare ground of the metal shot) and turns south at x 7703-7721 |
| the vertical x 7703-7721 and the corner (7712,6281) | `e_p9a.png`, `e_p9b.png`, `ov_p9poly.png` (3.3x) | salmon under the wide metal, plain width, no pad; the scan's green at y 6176-6261 is the rim of the gap beside it |
| the row y 6270-6292 and the pad (7488,6282) | `e_p9b.png` (4.2x), `ov_p9poly.png` | one poly under three metals, no pad; contact (ring, bright centre, green hole); field west of the pad |
| the metal from the pad: south, corner, west | `e_p9c.png` fourth tile (4x), `e_p9b.png` | vertical x 7478-7502 from the ring down into the horizontal y 6312-6340; nothing east of x 7502 on that line |
| the metal y 6316-6340, x 6400-7478 | `ov_p9m.png` (2.25x, metal and clean), `tc2_runs.py row 6328 6400 7480 3`, the scan along y 6323-6333, run 2's `g2_polyS.png` (4x at x 6420-6520) | one metal; chip 2: no dark run over 14 px (the polys underneath); no hole. **Read below 4x** |

No transistor. Omissions inside the piece: the pads (7655,6193), (7530,6325), (7420,6065),
(7385,6283) and their lines, and the wide metals y 6105-6150, y 6195-6245 (Not done).

## Piece 10 (wiring only): `tc2_r5718`, the line of the pad (7791,6152) (run 3, 2026-11-18)

Views: `e_p10a.png` (4x tiles, three shots: the pad (7791,5718), the poly's lower corner, the
pad (7530,6324)), `e_p10row.png` (2.5x, three shots), `e_p9a.png`, `e_p9b.png` (4.2x),
`e_sw_a.png`, `e_sw_m.png` (2.4x); overlay `ov_p10.png` (3.3x).

| Net | From | Path | To |
|---|---|---|---|
| `tc2_r5718` | the region's edge (8250,5718), a poly row arriving from the east | row y 5708-5728 west under the VCC rail's east leg, `db_b6`'s metal, the ground rail and `cdp1_lw1`'s metal; pad (7791,5718); metal x 7783-7799 south over `ras`'s comb rows; pad (7791,6152); poly west along y 6140-6160 to x 7745, south along x 7745-7765 under the wide metal, west along y 6315-6335; pad (7530,6324); metal x 7522-7544 south over `tc2_sr_c`'s row | the region's edge (7533,6400), going on south (follower: to (7509,7456), west, end (7353,7465), not looked at) |

Joins between named nets: none (one new name; neither end is followed; which end drives is
not known).

| End or crossing | Seen | Result |
|---|---|---|
| the row at x 8250 | `e_p10row.png` (2.5x) | still there at x 8262, going on east. **Read at 2.5x** |
| the row y 5708-5728, x 7812-8250 | `e_p10row.png` | one poly: salmon under the four metals, dark red in the gaps, orange-brown in the bare stretches of both metal shots; no pad. **Read at 2.5x** |
| pad (7791,5718) | `e_p10a.png` first tile | ring and bright centre in both metal shots, green hole with pits in a pad x 7778-7814; the poly leaves east only (field west), the metal south only |
| the metal y 5735-6135 | `follow.py 7794 5760 S` (end (7791,6158)), `tc2_runs.py col 7791 5735 6135 2` (runs of 5-22 px at `ras`'s rows; none over 18 in chip 2), the clean-shot scan (only the two end contacts) | one metal, no pad on the rows. **Read by profile and at 2.4x** |
| pad (7791,6152) | `e_p9a.png` (4.2x, clean and chip-2 metal) | ring, green hole; the metal ends on it; the poly leaves west |
| the poly's two corners and legs | `e_p9a.png`, `e_p10a.png` second tile, `ov_p10.png` | x 7745-7765 from y 6140 to 6335 (salmon under the wide metal, 24 px east of `ral_stb`'s vertical x 7703-7721: pink field between them all the way), corner, west along y 6312-6335, 22 px south of `ral_stb`'s row |
| pad (7530,6324) | `e_p10a.png` third tile | ring and bright centre in both metal shots, green hole; field west of it; the metal leaves south only |
| the metal over `tc2_sr_c`'s row (7533,6367) | run 2's `g1_cpadw.png` (5x) | no pad; `tc2_sr_c`'s own pad (7490,6367) is 12 px west of this metal's edge |

No transistor. Omissions: as piece 9's.

## Piece 11 (wiring only): `tc1_ns3` from (7902,4450) to the region's south edge (run 4, 2026-11-18)

Views: `n3_u3.png` (5.5x, unit 3's box under the metal, four shots), `n3_pad.png` (4.6x, four
shots), `n3_rowW.png` (4x, clean, chip-2 stripped, chip-2 metal; x 7580-7890), `n3_vert.png`
(2x, three shots, the vertical leg), `n3_pad2.png` (4.6x, four shots), `n3_south.png` (4x,
metal and clean, y 6200-6415); overlay `ov_p11.png` (1.9x).

| Net | From | Path | To |
|---|---|---|---|
| `tc1_ns3` | `tc1`'s thin metal x 7894-7909 at y 4450 | the metal south over the bus field's rows and `rax`'s five units (no contact); pad (7899,5633); poly row y 5622-5643 west; corner at x 7597-7612; poly south along x 7597-7612 to y 6203; east along y 6183-6203; pad (7660,6193); metal x 7652-7670 south | the region's edge (7661,6400), going on south (follower: end (7661,7088), not looked at) |

Joins between named nets: none (`tc1_ns3` only carried on). No transistor: the poly crosses no
diffusion (pink field on both sides wherever it is under metal; in the open stretch y 5950-6100
the two outlined khaki areas beside it are field: `px.py pt` at nine points in them, red minus
green -4..+5 in the chip-2 stripped shot at seven, +19 and +32 at two that lie on pinkish curls
which only that shot has; `opendiff.py 7400 5940 7800 6110`: none). Which end drives is not known: `tc1`'s notes bring ns3 in from the east over the
top of the datapath.

**No contact to `rax`'s output boxes** (`rax`'s AMB-011, point 2; this package's former Not
done). The metal passes over the box of each unit (x 7888-7916; y 5292-5314 in unit 3).

| | At each box (all five: `textmap.py 7876 5270 7926 5330 3 --acid`, and `7879 Y0 7923 Y1` at dy -498, -369, -130, +130) | At the line's own end contact (7899,5633) (`textmap.py 7874 5605 7926 5660 3 --acid`) |
|---|---|---|
| clean shot | diffusion-tan (0-3) over the whole box, no hole; a green band 9 px tall and 18 px wide directly BELOW the box (y 5315-5324 in unit 3; 79-124/115-138/88-97, `px.py col 7901 5300 5332 2`) | a hole 12 x 12 px inside the poly pad (6-9 around it) |
| chip-2 metal | bright (B-E) only over the metal's west half, x 7894-7900, y 5297-5309; the east half dark; below it a dark stretch of 16 px (R 38-86) which is not bare ground (bare ground in the gap beside it: R 143-163) | bright centre (B-E) 12 px across inside a dark ring 40 px across |
| chip-1 metal | the same (unit 1 is dirty in chip 2, plain in chip 1) | the same |

So each spot is the box's edge lengthwise under a thin metal (tracing guide, trap 22), and the
green band is at the box's lower outline, where a contact's hole would be in the middle of
the box. The clean-shot scan down the metal (green over red, x 7897-7905, y 4450-5650) finds
those five bands, a 5 px speck at y 4788-4792 (unit 0's poly edge) and the end contact, nothing
else. Five contacts would short `rax_o0`..`rax_o4`.

### Self-check: ends

| End or crossing | Seen | Result |
|---|---|---|
| meeting `tc1`'s metal at y 4450 | `textmap.py 7880 4435 7925 4470 3` (both metal shots, clean) | one metal: bright (B-E) x 7895-7907 above and below; 6 px dark at y 4447-4450, the upper edge of the bus field's first poly row (y 4453-4462 in the clean shot) |
| the metal y 4450-5636 | `follow.py 7901 4460 S` (end (7899,5636)), `tc2_runs.py col 7901 4450 5630 2`, the clean-shot scan | one metal; the runs over 25 px are the five boxes (above) and y 4728-4756 in chip 2 only (chip 1: two edges of 9 and 18 px: `ras_o0`'s poly and the ground box). **Between the boxes read by profile only** |
| the rows it crosses: bus field y 4460-4700, `ras_o0`..`ras_o4` (gates of `rax`'s pull-downs, under it), `cdp1_lw1`'s poly y 5520, the row y 5589 | the scan; `r89_E.png` (3.3x) for y 5589 | no hole on any |
| pad (7899,5633) | `n3_pad.png`, the text map above | contact (ring, bright centre, green hole). The metal ends on it (bare ground south). Field east of the pad (khaki, then the ground rail's edge); the poly leaves west only |
| row y 5622-5643, x 7612-7882 | `n3_rowW.png`; scan along y 5628-5636, x 7600-7890: no green over red; `textmap.py 7795 5612 7830 5652 3 --acid` | one poly, salmon under the metals, dark red in the bare stretch x 7850-7880 (orange in both metal shots there). `rax_o4`'s metal lies on it lengthwise from x 7705 to 7792 (trap 13): no hole, no pad. The dark rings on the row at x 7645, 7687, 7812 are where the gaps between the vertical metals cross it (clean shot only; the row is whole poly through the ring at x 7812 in the text map) |
| corner (7605,5632) | `n3_rowW.png` (4x) | plain L; pink field west and north of it |
| vertical x 7597-7612, y 5643-6183 | `n3_vert.png` (2x, three shots), scan down x 7601-7609: no green over red; `textmap.py 7585 5895 7625 5930 3 --acid` | one poly: salmon in the 25 px gap between `rax_o1`'s and `rax_o2`'s metals and under the horizontal metals y 5894, 5937 and the wide one y 6105-6150; dark red with a green rim in the open (y 5950-6100), orange in the chip-2 stripped shot. The ring at (7603,5912) is the gap between the metals y 5894 and y 5937 (poly whole through it). **Read at 2x and by profile** |
| foot and pad (7660,6193) | `n3_pad2.png` | the vertical ends in a foot x 7593-7612, y 6183-6203; the poly runs east into the pad; contact (ring, bright centre, green hole 15 px). Pink field west and south of the foot. A small ring on the poly at (7634,6192) in the clean shot only (the 28 px gap between the wide metal's end and the pad's metal): poly-orange and no ring in both metal shots |
| the pad's metal against the wide metal y 6195-6245 | `n3_pad2.png` | separate: the wide metal ends at x 7622; bare ground x 7622-7650 in both metal shots; the pad's metal x 7652-7670 |
| metal x 7652-7670, y 6205-6400 | `n3_south.png` (4x), `follow.py 7661 6230 S` | one metal on past y 6400; the three rows under it (`ral_stb`'s y 6282, `tc2_r5718`'s y 6324, `tc2_sr_c`'s y 6367) are uniform salmon under it: no pad, no hole. The rings on those rows at x 7637 and x 7687 stand in the gaps either side of it |

Omissions: a dark dot on the wide metal y 6195-6245 at (7607,6230), in both metal shots (round
in chip 2, a small triangle in chip 1): the clean shot under it is plain pink field
(159/129/110), so no contact; what it is was not settled. The two green-rimmed dark ovals at
(7862,5610) and (7862,5655) in the clean shot: field between the rows (plain ground in both
metal shots).

## Piece 12 (wiring only): `tc2_r5589`, the line of the row y 5589 (run 4, 2026-11-18)

Views: `r89_E.png` (3.3x, four shots, x 7880-8270), `r89_pads.png` (3.9x tiles, three shots:
(8246,5589), (8248,5262), (8490,5262)), `r89_W.png` (4x, three shots), `r89_m7490.png` (2.4x),
`r89_sw.png`, `r89_p6283.png`, `r89_wend.png` (4.3x, four shots), `r89_s2.png` (3x, three
shots); overlay `ov_p12.png` (2.1x tiles at the six pads).

| Net | From | Path | To |
|---|---|---|---|
| `tc2_r5589` | the pad (8248,5262), whose poly leaves east along y 5252-5272 (drawn to x 8275) | metal x 8240-8258 south; pad (8246,5589); poly row y 5578-5598 west; pad (7488,5586); metal x 7480-7500 south, corner at y 6055-6075, west; pad (7422,6065); poly west to x 7387, south along x 7378-7396; pad (7384,6282); metal west along y 6274-6292; pad (6840,6282); poly south x 6835-6851 | the region's edge (6843,6400), going on south (still there at y 6440) |

East of the region the poly from the pad (8248,5262) runs to a pad with a contact at
(8490,5262), whose metal goes south (follower: end (8491,5714)): seen (`r89_pads.png`), not
drawn. Joins between named nets: none (one new name). No transistor: the row and the two
vertical polys have field on both sides (pink under the metals). Which end drives is not known.

### Self-check: ends

| End or crossing | Seen | Result |
|---|---|---|
| pad (8248,5262) | `r89_pads.png` second tile | ring, bright centre in both metal shots, green hole; the metal leaves south only; the poly leaves east only (orange in the bare ground of both metal shots); field west |
| the poly at x 8275 | `r89_pads.png` second and third tiles | goes on east to the pad (8490,5262), passing under a metal at x 8440-8452 |
| metal x 8240-8258, y 5272-5580 | `follow.py 8249 5400 N` and `S`, scan down x 8245-8253: only the two end contacts; run 3's `e_east2.png` (2.4x) | one metal; `ral_stb`'s poly y 5369 passes under it without a pad. **Read below 4x between the pads** |
| pad (8246,5589) | `r89_pads.png` first tile, `r89_E.png` | ring, bright centre, green hole; the metal ends on it (bare ground south); khaki field east of the pad; the poly leaves west only |
| row y 5578-5598, x 7505-8230 | `r89_E.png` (3.3x), `n3_rowW.png` (4x), `r89_W.png` (4x); scan along y 5584-5592, x 7460-8270 | one poly. Only the east pad's hole in the scan (and the green gap strip west of the west pad). `rax_o3`'s metal lies on it from x 7662 to 7750 (trap 13): no hole. Rings in the clean shot only, at the gaps between the vertical metals (x 7600, 7643, 7773, 7812, 7860, 7880, 7925, 8052, 8100, 8180): not in either metal shot or the chip-2 stripped shot. Dark specks on the ground rail's edge at (7966,5577) and (8160,5578) in chip 2's metal shot only. **x 7880-8230 read at 3.3x** |
| pad (7488,5586) | `r89_W.png`, `textmap.py 7456 5538 7520 5612 3 --acid`, `follow.py 7490 5700 N` (end (7488,5582)) | contact by both metal shots (bright centre B-E 12 px across at (7486,5587) in a ring 40 px across). **The clean shot shows no hole**: the pad is under a red-orange blob there (residue on chip 1); the chip-2 stripped shot has the pad with a lighter centre. Field west of the pad. `ras_o4`'s metal corner (x 7452-7495, y 5538-5553) passes north of it: 6-9 px of bare ground (8-9 chip 2, 7 chip 1) between that metal's edge (y 5556-5559) and the ring (from y 5571), open colours in the clean shot at y 5562-5571: separate (trap 16) |
| metal x 7480-7500, y 5600-6055 | `r89_m7490.png` (2.4x, clean and both metal shots), `tc2_runs.py col 7490 5600 6060 3`, scan | one metal over pink field only; chip 1 alone is dirty at y 5813-5838. **Read at 2.4x** |
| corner (7490,6065) and pad (7422,6065) | `r89_sw.png` | plain corner; contact (ring, bright centre, green hole); the metal ends on the pad; the poly leaves west |
| poly x 7378-7396, y 6075-6265 | `r89_s2.png` (3x), scan down x 7383-7391 | corner at (7387,6065); salmon under the two wide metals, no pad, pink field both sides; `ras`'s poly x 7337 and its pad (7337,6065) are 30 px west (field between). **Read at 3x** |
| pad (7384,6282) | `r89_p6283.png` | contact (ring, bright centre, green hole); the poly ends in it (pink field south); the metal leaves west only (chip 1's metal shot is dirty just north of the pad) |
| metal y 6274-6292, x 6850-7370 | `follow.py 7310 6284 W` (end (6834,6280)) and `E` (end (7384,6282)), `tc2_runs.py row 6284 6400 7370 3`, scan along y 6279-6287 | one metal; runs of 8-17 px at the polys underneath; no hole. **Read by profile** |
| pad (6840,6282) | `r89_wend.png` | contact (ring, bright centre in both metal shots; the hole in the clean shot is a dark mark with green); the metal ends on it (bare ground west); the poly leaves south only; `fld`'s vertical poly x 6873-6891 is 20 px east (field between) |
| poly x 6835-6851, y 6300-6400 | `r89_wend.png`, `px.py row 6340 6815 6870 3`, `row 6398`, `row 6440` | salmon under `ral_stb`'s and `tc2_sr_c`'s metals (no hole: scan), still there at y 6440 |

Omissions: the pad (7337,6065) and the poly x 7328-7346 are `ras`'s (drawn there).

## Piece 13 (wiring only): the L at the east end of `sl_eq_r5_n` (run 4, 2026-11-18)

Views: `l_a.png` (4.5x, clean and chip-2 stripped), `l_m.png` (4.5x, both metal shots),
`l_p4850.png` (4.3x, four shots), `l_join_a.png`, `l_join_m.png` (4.4x), `l_box.png` (4.3x,
four shots); overlay `ov_p13.png` (2.8x).

| Net | From | Path | To |
|---|---|---|---|
| `sl_eq_r5_n` | the end of `r9m`'s row y 4676 at x 8192 | poly south x 8179-8192, y 4668-4728, in the gap between the VCC rail and `ral_stb`'s metal; east along y 4707-4727 under `ral_stb`'s metal; pad (8246,4716); metal east, south along x 8279-8299; pad (8290,4850); poly east along y 4840-4860 | (8352,4850), 100 px east of the region. The poly ends 5 px further on in a heavy-outlined box x 8355-8385, y 4835-4865, read as a buried contact onto a diffusion that goes on east under the metals from x 8395 (`l_box.png`: one view, four shots): `cdp1`'s west edge, drawn by nobody, **not traced** |

Joins between named nets: none (`sl_eq_r5_n` only carried on; the extraction's net count does
not change with this piece). So `sl_eq_r5_n` does not become a line of `cdp1`'s channel: it ends
on a diffusion at the datapath's west edge (a source or drain there, or a gate's input by a
buried contact: not known). The C-shaped poly beside the metal (from the east along
y 4712-4728 to x 8330, south, east again along y 4795-4815) is the west end of `cdp1`'s line
y 4719, 30 px east of this metal with bare ground between: not joined, not drawn here.

| End or crossing | Seen | Result |
|---|---|---|
| the row's corner (8186,4676) | `l_a.png`, `l_m.png`; `px.py col 8187 4634 4740 4` (four shots), `row 4700 8160 8215 3` | poly-coloured without a break from y 4670 to 4726 (chip 1's metal shot 111-159/60-100; clean red over green by 30-70); a dark edge at y 4730 and field below; field (green over red, khaki in chip 1) at y 4650-4658 between the row and the row y 4635 above. The leg is x 8179-8192 between the rail's edge line and `ral_stb`'s |
| under `ral_stb`'s metal (8205,4716) | `l_a.png`, `l_m.png`, run 3's `textmap.py 8180 4694 8226 4736` | uniform salmon, the metal whole between two edge bars: no pad |
| pad (8246,4716) | `l_a.png`, `l_m.png` | ring, bright centre in both metal shots, green hole. Field east of the pad under the metal's arm (pink); the poly arrives from the west only; the metal leaves east only |
| the metal's corner (8289,4716) and leg | `l_m.png`, `l_join_m.png`, `follow.py 8286 4760 N` (corners (8293,4723), (8285,4724)) and `S` (end (8288,4856)) | plain corner; one metal x 8279-8299 over pink field; it does not go on north or east of the corner (bare ground; `bust`'s row y 4676 is 25 px north) |
| pad (8290,4850) | `l_p4850.png` | ring, bright centre, green hole; the metal ends on it (bare ground south, to y 4900); bare ground west; the poly leaves east only |
| the poly's east end | `l_join_a.png`, `l_join_m.png`, `l_box.png` | orange in the bare ground of both metal shots to x 8352, then the box. **The box and what lies east of it: one view; not traced** |

No transistor in the region. Omissions: none inside the piece (the ring at (8183,4655) in the
clean shot is on the row y 4635, in the same gap: `bust`'s row).

## Piece 14 (wiring only): `tc2_m6404`, the fourth pad of the nest west of the XOR cells (run 4, 2026-11-18)

Views: `p6404.png` (3.6x, four shots, x 6350-6460, y 6085-6260), `p6404n.png` (3.7x, four
shots, the staircase), `p6404t.png` (4.4x tiles, both metal shots and the clean shot: the pad,
the corner, the poly at y 6340-6430); overlay `ov_p15w.png` (1.35x).

| Net | From | Path | To |
|---|---|---|---|
| `tc2_m6404` | the region's edge (6400,6026), a metal arriving from the west | metal east along y 6012-6040 to x 6417, south x 6395-6417; pad (6404,6107); poly south x 6395-6415 | the region's edge (6405,6400), going on south |

West of the region the metal turns north at x 6352-6372 (seen to y 5955 in `p6404n.png`; the
follower from (6406,6070) gives north to y 5654, west along y 5649, north along x 6230, end
(6230,4870): not looked at, and the follower has jumped between the nest's metals before).
Joins between named nets: none (one new name). No transistor. Which end drives is not known.

| End or crossing | Seen | Result |
|---|---|---|
| the staircase of the nest's three western metals | `p6404n.png`, `p6404t.png` second tile | three separate metals, bare ground of 20 px or more between them at every step: `lc3_w9947`'s (east at y 5971-5991), this one (east at y 6012-6040), and a third west of the region (x 6310-6330, east at y 6055-6085, south at x 6345-6365 to a pad (6360,6150)). Plain corners, no pad |
| pad (6404,6107) | `p6404t.png` first tile (4.4x), `p6404.png` | ring and bright centre in both metal shots, a hole with a dark mark in the pad in the clean shot; the metal ends on it (bare ground south: the poly is orange-brown there in both metal shots); the poly leaves south only |
| the poly under the ground metal y 6198-6243 | `p6404.png`, `textmap.py 6376 6186 6432 6256 3 --acid` | no contact: the metal is bright (B-E) over x 6397-6415 for its whole height in both chips, with only the poly's two edge lines (x 6394, x 6418-6421) dark; no ring; the clean shot is poly-coloured (3-7) without a hole. The clean shot shows this stretch mottled orange and olive where the three neighbours are plain salmon: residue on chip 1 (the chip-2 stripped shot has a plain band with a fringe across it). Former Not done item, settled |
| the poly under `ral_stb`'s metal y 6316-6340 and `tc2_sr_c`'s metal y 6360-6380 | `textmap.py 6384 6300 6426 6390 3`, `p6404t.png` third tile, scan down x 6400-6408, y 6080-6420 (no green over red) | no contact at either: metal whole across the poly, the clean shot poly-coloured (5-A) throughout |
| the poly at y 6400 | `p6404t.png` third tile, `px.py col 6404 6250 6440 10` | goes on past y 6440 |

Omissions: the pad (6360,6150), its metal and its poly (x 6355-6375) are 40 px west of the
region: not drawn. A dark ring on the ground metal at (6368,6218) in chip 1's metal shot only
(over that western poly): dirt.

## Piece 15 (wiring only): the two wide supply metals of y 6100-6400 (run 4, 2026-11-18)

Views: `s_w_m.png`, `s_e_m.png` (1.35x, metal with every block's trace), `s_A_w.png` (4x, metal
and clean: the VCC metal's west end), `s_B_w.png` (4x: `fld`'s ground rail meeting the band),
`s_fldE.png` (3.6x, three shots: the end of `fld`'s east ground rail), `s_cl1.png`, `s_cl2.png`
(2x, clean over metal, x 6380-7640), `s_AE.png` (2.4x, metal and clean, x 7540-7800);
overlays `ov_p15w.png` (1.35x), `ov_p15e.png` (2.5x). Tool: `tools/tc2_band.py` (the clean
shot's class along a cut under a wide metal; **it is of no use in the middle of these bands**,
where the protected field drifts from pink to olive-green: only the image settles it).

| Net | From | Path | To |
|---|---|---|---|
| `vcc` | `fld`'s VCC rail (x 6800-6840, drawn there to y 6040) | one metal x 6795-6848 south to y 6155; east as a band y 6105-6155 to x 7695; south as a metal x 7695-7752 | the region's edge (7723,6400), going on south |
| `vss` | `fld`'s west ground rail (x 6575-6625, drawn there to y 6110) | the same metal south to y 6198; a band y 6198-6243 west to the region's edge and east to x 7620; south as a metal x 7572-7620 | the region's edges (6400,6220), going on west, and (7596,6400), going on south |

Joins: each band is joined by drawn metal to a rail of `fld` that carries that supply's name
(the names there follow the XOR cell's loads and pull-downs; the west ground rail is also
joined north to `tcw`'s by piece 1). No `?` item. **`fld`'s east ground rail
(x 6978-7028) does not reach the VCC band**: it ends at y 6037 (fixed in `trace/fld.txt` in a
commit of its own; it was drawn to y 6110, which would have shorted the supplies).

**No contact and no diffusion under either band between x 6400 and x 7752** (`s_cl1.png`,
`s_cl2.png`, `s_AE.png`): the clean shot shows field (pink at the edges, olive in the middle)
and the vertical polys that cross: under the VSS band `tc2_m6404`, `lc3_w9947`, `tc1_p4308`,
`tc1_m6817`; under both the polys at x 6873-6891 and x 6921-6939 (`fld`'s), x 7111-7129,
7155-7173, 7199-7217, 7263-7281, 7328-7346 (`ras`'s), x 7378-7396 (`tc2_r5589`) and x 7597-7612
(`tc1_ns3`, under the VCC band only); under the VCC metal's south leg `ral_stb`'s and
`tc2_r5718`'s vertical polys lengthwise and their rows, `tc2_sr_c`'s row; under the VSS
metal's south leg the same three rows. The supplies only pass through here.

| End or stretch | Seen | Result |
|---|---|---|
| `fld`'s VCC rail to the band (x 6795-6848, y 6040-6105) | `s_A_w.png` (4x), `tc2_runs.py col 6821 6000 6160 4` | one metal; no dark run at one place in both chips. A dark dot at (6815,6088) in chip 2 only; the clean shot under it is field |
| the VCC band's west end and corner | `s_A_w.png` | the L's outer corner at (6795,6155); nothing west of x 6790 or south of y 6157 (bare ground) |
| VCC band y 6105-6155, x 6850-7695 | `tc2_runs.py row 6130 6790 7730 4`, `s_cl1.png`, `s_cl2.png` (2x) | one metal: runs of 9-21 px at the polys' edges; the two longer ones (34 px at x 7151-7184 in chip 2, 33 px at x 7108-7140 in chip 1) are each two edges in the other chip. **Read at 2x and by profile** |
| VCC south leg x 7695-7752, y 6105-6400 | `s_AE.png` (2.4x), `ov_p15e.png` (2.5x), `tc2_runs.py col 7735 6100 6440 3`, `col 7712`, `segs.py 7660 7800` at seven y | one metal on past y 6400: no dark run of 25 px at one place in both chips at x 7735; at x 7712 chip 2 is dark for 27 px at y 6272-6298 (`ral_stb`'s poly corner lengthwise under it; chip 1 bright). It does not go on north of y 6105 (bare ground; `ral_stb`'s pad (7750,6065) is 27 px north of its corner). The dark lines lengthwise in it are the edges of the two vertical polys. **Read at 2.5x and by profile** |
| `fld`'s west ground rail to the band (x 6577-6623, y 6110-6198) | `s_B_w.png` (4x), `tc2_runs.py col 6600 6090 6230 4`, `textmap.py 6566 6080 6636 6120 3`, `segs.py 6530 6660 6120,6160,6185` | one metal x 6579-6624: a dark bar of 8 px at y 6095-6102 across it in both chips is the lower edge of `fld`'s poly row y 6076-6094 underneath (the clean shot: poly, then field); metal B-E above and below. The rail flares west to x 6555 at y 6160-6198 (not drawn) |
| VSS band y 6198-6243, x 6400-7620 | `tc2_runs.py row 6220 6385 7600 4`, `s_cl1.png`, `s_cl2.png`, `p6404.png` | one metal: runs of 7-22 px at the polys' edges in chip 2; chip 1 is dark for 35 px over the polys x 7337 and x 7387 (two edges each in chip 2). West of x 6400 it goes on (bright at x 6385) |
| VSS south leg x 7572-7620, y 6243-6400 | `s_AE.png`, `ov_p15e.png`, `tc2_runs.py col 7590 6200 6440 3`, `segs.py 7540 7650` at five y | one metal on past y 6400; `tc1_ns3`'s pad (7660,6193) and metal are 30 px east (bare ground, piece 11) |
| the end of `fld`'s east ground rail | `s_fldE.png` (3.6x, three shots), `s_A_w.png` (4x), `tc2_runs.py col 7003 5980 6120 6`, `px.py col 7000 6020 6070 5` | rounded end at y 6037 in both metal shots; no metal from y 6031 to 6111 in either chip (bare ground 168/138/88, 138/113/73); open field in the clean shot from y 6042 |

Omissions: the dark dots on both metals in chip 2's metal shot (among them (6585,6215),
(6608,6200), (6608,6228), (6645,6232), (6815,6088), (7415,6230), (7508,6218), (7603,6232),
(7607,6230)): pits in chip 2's wide metal; the clean shot under each is plain field. Chip 1
has its own at other places. None has a ring with a bright centre.

## Piece 16 (wiring only): the supply metal that links `fld`'s rails (run 4, 2026-11-18)

Found by the sweep below (the only metal in the region that is bright in both metal shots and
that no block had drawn). Views: `fr_m.png`, `fr_a.png` (3.3x, metal and clean, x 6680-7050,
y 5225-5460, with every block's trace); overlay `ov_p16.png` (3.3x).

| Net | From | Path | To |
|---|---|---|---|
| `vcc` | the VCC rail of `fld`'s two inverters (x 6700-6750, drawn there to y 5290) | its south end widens east to a block x 6708-6840 (y 5235-5290 west of x 6792, y 5258-5290 east of it); a rail x 6796-6840 south over the rows y 5300 and y 5345 | the XOR cells' VCC rail (x 6800-6840, drawn by `fld` from y 5400) |
| `vcc` | that rail at y 5690 | the same metal x 6795-6840 across y 5690-5760, where `fld`'s drawing has a gap | the rail's lower piece (drawn by `fld` from y 5760) |
| `vss` | the east ground rail of the inverters (x 6879-6925, drawn by `fld` to y 5290) | a rail x 6881-6925 south over the same two rows to y 5440; from y 5388 it widens east (a slanted edge from (6930,5370)) to a block x 6881-7014 | the XOR cells' east ground rail (x 6978-7028, drawn by `fld` from y 5400) |

Joins: supplies only. `fld`'s inverter VCC rail (joined to `tcw`'s by piece 3), the XOR cells'
VCC rail and the wide VCC metal of piece 15 are now one drawn metal; so are `tc1`'s ground rail
(piece 6), the inverters' east ground rail and the XOR cells' east ground rail. The
extraction's `vcc` goes from 114 to 112 separate pieces and `vss` from 166 to 165; nothing
else changes (`tools/sameconn.py`: connections identical).

| End or stretch | Seen | Result |
|---|---|---|
| the VCC block and its meeting with the inverters' rail | `fr_m.png`, `segs.py 6680 7050` at y 5245, 5262, 5280; `tc2_runs.py row 5262 6700 6845 4` | one metal x 6708-6839 at y 5262 in both chips, no dark run; at y 5245 it ends at x 6792 (east of that, `fld`'s box (6793-6827, 5230-5257) lies in bare ground) |
| VCC rail x 6796-6840, y 5290-5400 | `fr_m.png`, `tc2_runs.py col 6818 5235 5420 5`, `segs.py` at y 5372, 5385, 5410 | one metal: runs of 10-16 px at the two rows' edges in both chips. A dark ring-like spot at (6810,5305) over the row y 5300 in chip 2 only (chip 1 bright D-E there; the clean shot has the row uniform, no hole: `textmap.py 6786 5286 6836 5324 3`): no contact |
| VCC rail across y 5690-5760 | `segs.py 6760 6900 5695,5720,5745`, `tc2_runs.py col 6818 5670 5780 5` | metal x 6795-6840 at all three y in both chips; no dark run in that stretch. **Read by profile and at 1.3x (`sw_m_6400_5425.png`)** |
| ground rail x 6881-6925, y 5290-5440 | `fr_m.png`, `tc2_runs.py col 6903 5270 5440 5`, `segs.py` at y 5372, 5385 | one metal: chip 2 is dark for 33 px at y 5333-5365 (the row y 5345; chip 1 has its two edges with metal between) and chip 1 for 35 px at y 5397-5431 (chip 2: 12 px): no dark stretch at one place in both |
| the ground block and its meeting with the XOR rail | `fr_m.png`, `ov_p16.png`, `segs.py` at y 5410, 5430, `tc2_runs.py row 5410 6880 7030 4` | x 6882-7013 at y 5410; it ends at x 7014 (16 px of bare ground to x 7029 in both chips). `fld`'s rail below it is drawn to x 7028 and the metal's east edge is x 7013 all the way down (`segs.py 6940 7060 5400,5420,5470,5520,5600`): geometry only, not changed. The pad (7032,5345) of `fld_b_in`'s row is 14 px north of the block's corner and east of its edge: bare ground between |
| under all of it | `fr_a.png` | pink field and the two poly rows, uniform: no pad, no hole, no diffusion |

No transistor, no contact.

## The sweep of the whole region (run 4, 2026-11-18)

After piece 15 the region was looked over once more with every block's geometry laid on it
(`TRACE=` empty): six tiles of the clean shot at 1.35x (`sw_a_6400_4450.png`,
`sw_a_7325_4450.png`, `sw_a_6400_5100.png`, `sw_a_7325_5100.png`, `sw_a_6400_5750.png`,
`sw_a_7325_5750.png`) and four of the chip-2 metal shot at 1.3x (`sw_m_6400_4450.png`,
`sw_m_7325_4450.png`, `sw_m_6400_5425.png`, `sw_m_7325_5425.png`), and four scans:

| Scan | What it looks for | Result |
|---|---|---|
| metal bright in both metal shots (the follower's test) more than 9 px from any drawn metal or contact (inline script; groups of 150 px2 or more) | undrawn metal | eight groups, all the links of piece 16 (now drawn); nothing else. Thin dim metals fail the test (trap 19): the four metal tiles were read for those, and none without an outline was seen |
| `tools/tc2_undrawn.py 6400 4450 8250 6400 60` | protected poly colour or protected diffusion colour in the clean shot more than 8 px from a drawn item of that layer | poly: no group. Diffusion: five groups of 85-267 px2, all inside `ras`'s selector (below) |
| chip-2 stripped shot red minus green 25 or more and chip-1 metal shot orange, in the open, more than 8 px from any drawn poly, diffusion or contact (inline script; it finds about half of the drawn open poly) | undrawn poly in the open | eight slivers of 120-180 px2 along the edges of drawn items; nothing with a width |
| `tools/opendiff.py 6400 4450 8250 6400` | large open diffusion | thirty-odd green strips 8-16 px across beside rows and metals (gap rims, trap 3); none 25 px wide both ways |

Two attempts to find undrawn contacts by rule (holes in the clean shot, rings in both metal
shots) were of no use here (the first finds a fifth of the drawn contacts, the second fires at
every crossing of a metal and a row): contacts were looked for on the tiles, as pads without
a box, and none was seen.

Looked at because of the sweep:

| Where | Seen | What it is |
|---|---|---|
| dark dots on the ground rail at (8012,5765), (8015,5830), (8013,5880) (former Not done) | `dots_rail.png` (4.4x, both metal shots and the clean shot) | notches at the lower edge lines of `ras`'s comb rows in chip 2 ((8013,5790), (8012,5855)); chip 1 has specks at other places; the clean shot has the rows uniform and pink field between: no contact |
| dark dots on `fld`'s east ground rail at (6990,5728), (6996,5880) | `textmap.py 6962 5704 7016 5746 3`, `6962 5858 7016 5900 3` | chip 2 only (chip 1 bright B-D there): blemishes |
| `fld`'s comment "south to a pad at about (7032,5345) (NOT DRAWN further)" | `sw_7030.png` (3.6x, with every block's trace) | the pad is drawn (the east end of `fld_b_in`'s row y 5345) |
| the vertical poly x 6397-6413, y 4437-4870 on the region's west edge | `tools/tc2_items.py` | drawn by `fld` |
| tan under the metal x 7195-7215 at (7199-7224, 5711-5724) and (7198-7224, 5885-5898) | `cand_ras.png` (3.6x, clean and metal with every block's trace), `px.py pt 7205,5717 7205,5745 7205,5891 7205,5915` | **undrawn, not traced**: diffusion colour under the metal (198/174/127 and 198/174/129, against pink field 186/120/123 and 181/121/123 thirty px south under the same metal), just below `ras`'s two `?P` rows y 5685-5710 and y 5860-5885 and west of where `ras`'s drawn diffusion begins (x 7228). They are the west ends of the two lowest strips of `ras`'s selector, which its trace says were not seen clearly. Left to `ras` |
| the three smaller diffusion-coloured groups (7392-7403, 5624-5637), (7266-7274, 5210-5224), (7266-7274, 5378-5391) | the scan only | 85-114 px2, inside `ras`'s drawn cells; not looked at |

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
| `tc1_p4308` | M | x 6400, y 5557-5577 | ? | going on west (follower: end (6318,4999)) |
| `tc1_p4308` | P | x 6483-6501, y 6400 | ? | going on south |
| `lc3_w9947` | M | x 6400, y 5601-5621 | ? | going on west (follower: end (6276,4825)); its vertical x 6396-6416 lies on the edge |
| `lc3_w9947` | P | x 6443-6460, y 6400 | ? | going on south |
| `tc2_sr_g` | M | x 7827-7847, y 6400 | in | the latch's gate line, going on south (follower: end (7835,7218)) |
| `tc2_sr_s` | M | x 7782-7800, y 6400 | in | going on south (follower: end (7791,6958)) |
| `tc2_sr_q` | M | x 7913-7931, y 6400 | out | going on south (follower: end (7922,7046)) |
| `tc2_sr_q` | P | x 8250, y 6163-6180 | out | going on east under the VCC rail |
| `cdp1_lw1` | P | x 8340-8375, y 4975-4987 | ? | the pad (8353,4981): where this package's drawing of `cdp1_lw1` meets `cdp1`'s poly (125 px east of the region) |
| `rax_o0`..`rax_o4` | D | x 8040-8048, y 4781-4801, 4911-4931, 5150-5170, 5280-5300, 5410-5430 | - | not ports: where the loads' band meets `rax`'s (inside the region) |
| `tc2_sr_c` | P | x 8250, y 6358-6376 | ? | the top line of `cdp2`'s channel 2, going on east |
| `tc2_sr_c` | M | x 6400, y 6360-6380 | ? | going on west (follower: end (6184,6370) on a pad) |
| `ral_stb` | M | x 8198-8212, y 4450 | ? | from `tc1` (its bus metal ns4) |
| `ral_stb` | P | x 8250, y 5359-5379 | ? | the poly from the contact (8204,5371), going on east |
| `ral_stb` | M | x 6400, y 6316-6340 | ? | going on west: pad (6145,6322), row, pad (5755,6322), south (`tl6`; the follower's end (6012,6068) was a jump onto `rst_ck`'s metal x 6105) |
| `tc2_r5718` | P | x 8250, y 5708-5728 | ? | the row going on east |
| `tc2_r5718` | M | x 7522-7544, y 6400 | ? | going on south (follower: end (7353,7465)) |
| `tc1_ns3` | M | x 7894-7909, y 4450 | ? | from `tc1` (its contact (7905,4370)) |
| `tc1_ns3` | M | x 7652-7670, y 6400 | ? | going on south (follower: end (7661,7088)) |
| `tc2_r5589` | P | x 8275, y 5252-5272 | ? | the poly from the pad (8248,5262), going on east to a pad (8490,5262) (25 px east of the region) |
| `tc2_r5589` | P | x 6835-6851, y 6400 | ? | the poly from the pad (6840,6282), going on south |
| `sl_eq_r5_n` | P | x 8170-8192, y 4670-4682 | in (believed) | not a port: where this package's drawing meets `r9m`'s row (inside the region) |
| `sl_eq_r5_n` | P | x 8352, y 4840-4860 | ? | the poly from the pad (8290,4850), 100 px east of the region: it ends in a box at (8370,4850) at `cdp1`'s west edge |
| `tc2_m6404` | M | x 6400, y 6012-6040 | ? | going on west, then north at x 6352-6372 (seen to y 5955) |
| `tc2_m6404` | P | x 6395-6415, y 6400 | ? | going on south |
| `vcc` | M | x 6795-6848, y 6040 | - | meets `fld`'s VCC rail (inside the region) |
| `vcc` | M | x 7695-7752, y 6400 | - | the wide VCC metal's south leg, going on south |
| `vss` | M | x 6577-6623, y 6110 | - | meets `fld`'s west ground rail (inside the region) |
| `vss` | M | x 6400, y 6198-6243 | - | the wide ground metal, going on west |
| `vss` | M | x 7572-7620, y 6400 | - | the wide ground metal's south leg, going on south |
| `vss` | M | x 6860-6907, y 4380 | - | meets `tc1`'s rail (70 px north of the edge) |
| `vss` | M | x 6882-6926, y 4990 | - | meets `fld`'s rail (inside the region) |
| `vss` | M | x 7990-8040, y 5625-5650 | - | meets `rax`'s rail step |
| `vss` | M | x 8030-8075, y 6400 | - | the ground rail going on south |
| `vcc` | M | x 8206-8248, y 6400 | - | going on south (`cdp2`'s rail x 8229 from y 7425) |
| `vcc` | M | x 8117-8163, y 4450 | - | meets `tc1`'s VCC rail (x 8116-8165) |

## Ambiguities

- **`tc1_ns3`'s metal x 7902 over the five boxes of `rax`'s units** (x 7888-7916; unit 3 at
  y 5292-5326; the others at -499, -369, -130, +130): one metal passing over without
  contact is the reading drawn, with those five stretches `?M`. The photos are consistent
  with it but do not establish it: the metal test fails across the full width for about
  24 px at each box in both chips, with a blob of bare-ground brightness and a green band
  in the clean shot under it; against a contact: no ring, no hole, no contact centre (9x,
  four shots); against a break: it would leave dangling segments. So `tc1_ns3`'s join from
  tc1 to the pad (7899,5633) and its row rests on `?M` items and on that electrical
  argument (as AMB-011). An earlier note here said "dark for 16 px, not bare ground": that
  held only for the west half of the line.

None in pieces 1 to 3.

1. **Piece 4: the west arm's join to `tc2_sr_q`'s load poly, x 8135-8152, y 6183-6202**
   (`?P`). The arm (x 8096-8133, the gate over the lower column) and the vertical poly
   x 8152-8173 lie 18 px apart across the gap between `db_b6`'s metal and the metal x 8156-8178.
   For one poly: the arm's upper and lower edge lines (y 6181, y 6205) run through the gap in
   both chip-2 shots (`g1_arm.png`, 11x), the lower one on to the vertical's south end; the arm
   has no other connection (field west of it for 20 px, firmly). Against: the gap is dark with
   a slightly green sample at x 8136-8141 in the chip-2 shots (`px.py row 6192`; box means in
   the notes of run 2: chip-2 metal 97/110 and 50/45 where the two other polys that cross this
   same gap, row A's east piece at y 6027 and the tie's tab at y 6127, are 165/117 and
   153/111). Working assumption: joined. If it is not, the lower column's gate floats. What
   would settle it: a sharper shot of this gap, or the latch's behaviour in simulation.
2. **Piece 4: the top diffusion between the contact box and the upper column** (x 8088-8103
   is hidden by a gap bar in the clean shot): drawn firm from the edge line and the tan at
   x 8075-8087 (self-check above). If it were not continuous the upper column's gate would
   have a floating source.
3. **Piece 4: supply identities** (settled in run 3). The ground rail is `vss` by drawn
   metal to `rax`'s rail; the rail x 8205-8248 is `vcc` by drawn metal to `tc1`'s VCC bus
   (piece 8). Its metal south of y 6400 is not drawn.

4. **Piece 4: where `cdp1_lw1` comes from** (settled in run 3, piece 7): the thin metal is
   one line over `rax`'s units without a contact, and the wire `tc2` called sr_r is `cdp1_lw1`.

## Not done

After run 4 (pieces 11 to 16 and the sweep) **nothing that the sweep could see is left
undrawn inside the region except the two items under "Inside the region"**. What remains is
where lines leave it, and the review.

Inside the region:

- In `ras`'s selector, the west ends of its two lowest strips: diffusion colour under the
  metal x 7195-7215 at (7199-7224, 5711-5724) and (7198-7224, 5885-5898), west of `ras`'s
  drawn diffusion (from x 7228) and below its `?P` rows y 5685-5710, y 5860-5885
  (`cand_ras.png`; the sweep's table). Not traced: it is the part of `ras`'s cell that its
  trace marks as not seen clearly. Three smaller diffusion-coloured spots inside `ras`'s drawn
  cells, (7392-7403, 5624-5637), (7266-7274, 5210-5224), (7266-7274, 5378-5391): not looked at.
- The latch's two `?P` joins (Ambiguity 1 and review round 1 of the second round of work):
  the photos do not settle them.

Lines that leave the region (each is drawn to the edge; the port table has the place):

- West of x 6400: `tc2_o5175` (poly y 5173), `tc1_p4308` (poly y 5003), `tc1_o3527` (metal
  y 4482; follower: end (6012,4484)), `ras_o0_alt2` (metal y 4788; follower: end (6059,4876)),
  `tc1_p4308` (metal y 5567), `lc3_w9947` (metal y 5611), `tc2_m6404` (metal y 6026, turning
  north at x 6362), `ral_stb` (metal y 6328; west of the region by `tl6`'s route, not the follower's end (6012,6068)), `tc2_sr_c` (metal
  y 6370 to a pad (6184,6370)), the wide ground metal y 6198-6243.
- South of y 6400: `tc1_m6817` (poly x 6534), `tc1_p4308` (poly x 6492), `lc3_w9947` (poly
  x 6451), `tc2_m6404` (poly x 6405), `tc2_r5589` (poly x 6843), `tc2_r5718` (metal x 7533;
  follower: end (7353,7465)), `tc1_ns3` (metal x 7661; follower: end (7661,7088)),
  `tc2_sr_s`, `tc2_sr_g`, `tc2_sr_q` (metals x 7791, 7837, 7922; follower ends (7791,6958),
  (7835,7218), (7922,7046)), the wide ground metal's leg x 7572-7620, the wide VCC metal's
  leg x 7695-7752, the ground rail x 8030-8075 and the VCC rail x 8206-8248.
- East of x 8250: `ral_stb` (poly y 5369, seen to x 8425), `tc2_r5718` (poly row y 5718),
  `tc2_sr_q` (poly y 6172), `tc2_sr_c` (poly row y 6367, the top line of `cdp2`'s channel 2),
  `tc2_r5589` (poly y 5262 from x 8275 to a pad (8490,5262), whose metal goes south to
  (8491,5714)), `sl_eq_r5_n` (from (8352,4850): the box x 8355-8385, y 4835-4865 in which its
  poly ends, read as a buried contact, and the diffusion east of it at `cdp1`'s west edge,
  drawn by nobody: `l_box.png`).
- `cdp1_lw1` (= the wire `tc2` called sr_r) east of x 15584 (`bust`'s Not done): the latch's reset line is
  not identified until that end is followed.
- West of the region, seen and not drawn: the nest's third metal and its pad (6360,6150) with
  a poly going south (x 6355-6375).

Not done as work:

- The independent review of pieces 11 to 16 (the Review section below covers pieces 1 to 10).

## Review

Round 1 (full review, 2026-11-17 23:05 +0000, a fresh agent on claude-fable-5-2, at commit 5bed081). Told to
suspect the four adjacent crossing-field rows y 4482, 4786, 4829, 4873 (a one-track step
drawn straight; pads on the wrong row), the diagonal hop and vertical of `tc1_x1`, the two
north-edge joins onto tc1's lines, the no-contact calls, `tc1_m6817`'s long metal, the
NOR's gates and its load tie, `fld_b_in`'s corner, the rails, and widths, ends and undrawn
features. It tracked each row's edge pair every 12 px in the chip-2 stripped shot and every
18 px in the clean shot (within 2 px from x 6512 to 6908, no step under either rail or the
wide metals; all eight pads on their own rows, 3-4.5x), checked the north edge in four
shots, the diagonal and corner, the no-contact spots at 5.4x with text maps, the long metal
with the follower, and the NOR with profiles (strip to both VSS boxes, gate identities, the
tie's diffusion by a chip-2 column profile).
No finding in the trace. Two points in the notes, fixed: the supply identity of the two
rails was overstated (the metal joins are real; the identity is by the layout rule, as for
`tcw`); an unrecorded follower candidate at (6722,4852) under the VCC rail is not a contact
(dark notch in chip 2 only; chip 1 whole; no ring, no hole; 5x). Outside the package:
`bust`'s `?P` pads on rows y 4657 and y 4700 sit about 30 px off the photographed pads (in
the handoff).
Not checked: west of x 6400; the x 6364 stretch above 1.95x; the tie's diffusion in chip 1.

Round 1 of the first round of work: clean (no findings).

### Second round of work (pieces 4-6: the latch `tc2_sr`, two wires, the east ground rail)

Round 1 (full review of what was added since 7562c27, 2026-11-17 23:58 +0000, a fresh agent on
claude-fable-5-2). Told to suspect the latch as a circuit (which poly is which gate of the
five-gate stack, the nodes between, row A as two polys, the `?P`, the load ties, the band to
the lower column, the top diffusion, row C's end, the cross-coupling), the wires read below
4x (`cdp1_lw1`, the row y 6367 and the metal y 6370, the rails), the pads, and widths, ends
and undrawn features. Checked: the stack order and nodes at 4x in three shots (ground, A,
n20, B, q, C, ground, D, n21, E, q_n; no contact on n20, n21), row A's gap at 8x, the `?P`,
the tie of q's load by profiles, the diffusion links by column and row profiles in both
chip-2 shots, the stub, every pad, `cdp1_lw1`'s metal over ten rows at 4.4x, the row y 6367
and the metal y 6370 as one piece at 3.2-3.3x, both rails in both chips.
No finding changes a connection. Three minor points:
1. The join of q_n's buried-contact poly to its pad poly across x 8140-8150 was drawn
   certain on the same grade of evidence as the `?P` (dark in all four shots; only the
   C-shaped rings open east in the clean shot): confirmed by the tracer on
   `review2-1/l_qnbc.png`; that stretch is now `?P`. Connections identical. Note:
   `tools/unsure.py --equations` now prints `tc2_sr_q` as FIRM and `tc2_sr_q_n` as DEPENDS;
   that is where the name's label sits (on the gate side of the join), not more certainty:
   the latch's cross-coupling depends on both `?P` items.
2. The upper column's west edge at y 6052-6107 is at about x 8095 (drawn 8105), and
3. the top diffusion runs east to about x 8150 (drawn 8138): drain side only, the channels
   unchanged; recorded, not redrawn.
Not checked: `cdp1_lw1` north of y 5468 (left open by the trace), `tc2_sr_c`'s metal
y 6315-6338 (follower only), the VCC rail north of y 5960.

Round 2 (fix check, 2026-11-18 00:01 +0000, a fresh agent on claude-fable-5-2, against commit c9f19a2). The
split is placed right (row profiles in all shots: the poly is seen to x 8136-8138, a dark
band hides x 8138-8150, the pad's poly starts at x 8152); the firm part lies wholly inside
the buried-contact box, so no channel forms; `tools/sameconn.py`: connections identical.
The marking of the latch, stated exactly: **the latch is marked, not firm.** Only q's NOR
input structure is firm; q_n to q rests on the `?P` at x 8138-8152, and q to q_n (and that
channel's east end) on the `?P` at (8133-8154, 6183-6202). `tools/unsure.py` printing
`tc2_sr_q` as FIRM is a label artefact (the name's label is on the pad side of the join).

Round 2 of the second round of work: clean (no findings).

### Third round of work (pieces 7-10: the wire `tc2` called sr_r = `cdp1_lw1`, the loads of `rax`'s units, `ral_stb`, `tc2_r5718`)

Round 1 (full review of what was added since ad84a3b, 2026-11-18 00:51 +0000, a fresh agent on
claude-fable-5-2). Told to suspect every step of the join the wire `tc2` called sr_r = `cdp1_lw1` (the thin
metal as one piece where chip 2 is dark at unit 3, contacts at the end caps and boxes, the
row y 5066, the corner and the pad, and whether the pad is on `cdp1_lw1` or on `db_b6`
43 px away), the load cell and its five copies, the VCC rail, the stretches read below 4x,
the two polys under one wide metal, and widths, ends and undrawn features. Checked: the
thin metal at 5x in three shots (chip 1 reads the same at unit 3 as at units 2 and 4: not a
break); the caps and boxes by colour against the two real contacts, and in units 0 and 1
where no metal covers them; both pads and the row in four shots; the pad on `cdp1_lw1`'s
own row at 4.7x (the y 5024 row stays separate); all five load copies by overlay at
3.4-3.6x; the rail in both chips; `ral_stb`'s metal with the follower and its contact at
5x; the rows y 5673 and y 5718 at 4.9x with profiles; the two polys at 4.3x (separate, not
swapped); the metal y 6328 unbroken to x 6400.
No finding. One geometry nit, not changed: the metal along y 6328 is drawn 23 wide and
measures 12-17 px (it touches nothing). Could not be checked: the load tie's tab to the
band in units 2-4 (under metal; in units 0 and 1 the box sits flush under the band:
consistent, not proven; it decides the load's gate, not the equation `rax_o# = NOT ras_o#`).

Round 1 of the third round of work: clean (no findings).

### Fourth round of work (pieces 11-16: `tc1_ns3`, `tc2_r5589`, `sl_eq_r5_n`'s L, `tc2_m6404`, the supply bands; the fix to fld's rail)

Round 1 (full review of what was added since 9599d13, 2026-11-18 01:33 +0000, a fresh agent on
claude-fable-5-2). Told to suspect `tc1_ns3`'s metal over `rax`'s boxes, the pad (7488,5586),
the two metals lying on rows without contact, the two supply bands 40 px apart (separate?
each on the right rail, i.e. not swapped), the VCC south leg, the fld fix, the stretches
read below 4x and the membership of the pads at x 7384-7490. Checked: the pad in both metal
shots with the follower; the two Z-shaped metals at 4.5x; the bands (no metal in the gap
y 6166-6188 over x 6640-7700 in either chip; each band's join to its fld rail at 4x in both
metal shots; only field and crossing polys beneath); the VCC leg (straight; the poly
beneath turns west); the fld rail's end at y 6036 by profile; the verticals, corners and
all four pads' memberships (no swap); `sl_eq_r5_n`'s L in three shots.
No finding changes a connection. One point undecidable, now marked: `tc1_ns3`'s metal
over the boxes (9x, four shots): the five stretches are `?M` and the Ambiguities entry
states what is and is not shown. Not checked: beyond the ports; the four other units'
boxes at 9x; a green mark at (7245-7280, 6120) under the VCC band (clean shot only, no ring
in either metal shot).

Round 2 (fix check, 2026-11-18 01:35 +0000, a fresh agent on claude-fable-5-2, against commit c63b34b). It
measured the dark part at each of the five units with the follower's metal test down
x 7895-7909 (dark in both chips: y 4810-4828, 4940-4958, 5178-5197, 5310-5327, 5439-5457,
about 19 px each): every `?M` stretch covers its dark part (they sit about 4 px south of
centre: the north margin is nil, the south 9-11 px; not changed). Every other dark run on
the line is 6-12 px (poly-edge bars), except y 5609-5625 just north of the end pad
(7899,5633): the pad's ring on the arriving side, already reviewed; left firm.
`tools/sameconn.py`: connections identical; `tools/unsure.py` lists `tc1_ns3` as resting
on the uncertain items.

Round 2: no findings.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- Piece 13: the box (8355-8385, 4835-4865) "onto a diffusion ... not traced" is the output node of
  `eof`'s inverter `sl_eq_r5_n` = NOT `sl_eq_r5`; the C-shaped poly "not joined" is its input gate.
  `ports.d/tc2.txt`'s `sl_eq_r5_n` is driven from there (direction `in`).

## Corrections (coordinator, from the handoffs of 2026-11-19, second batch)

- `tc2_sr_g` ("metal x 7837 going south past y 6400, not followed") **is followed** (`eofw`): the metal
  runs 820 px south to a pad with a contact (7836,7215), whose poly row runs west under both rails to
  the pad (7313,7215) of row 2 of `eof`'s gate `g7700`; from that row's pad (7267,7736) a metal goes on
  south to a T (7273,8710) and by a staircase to `lc2`'s `tc2_sr_g`, **the enable of latch D**, with a
  corner pad (7446,8732) into `cdp3`'s gate column. So the latch `tc2_sr_q` / `tc2_sr_q_n` and latch D
  are gated by one line. Its driver is not found.
- `tc2_r5589`'s poly x 6843 south of y 6400 ("still there at y 6440") **is followed** (`eofw`): south
  to a corner (6843,6870), east along y 6870, to the pad (7272,6912) of the output of `eof`'s gate
  `g7700`. **`tc2_r5589` is driven by that gate**: `tc2_r5589` = NOT(`lc1_w7170` AND (`rst_ck` OR
  `tc2_sr_g`)). Its loads lie east of the pad (8248,5262).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- `lc3_w9947` ("neither end is followed"): followed south from y 6400 by `eof` (run 13, piece `ck5`: a pad (6450,7127), the track x 6688, pads (6645,8276), (6645,8580)) to the clock of the left-centre ripple counter; the net's canonical name is `lc3_w9947`.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- Piece 10 and ports, `tc2_r5718` M (7522-7544, 6400) ("follower: to (7509,7456), west, end (7353,7465), not looked at"): followed by `busl` (piece `fd`, 2026-11-20) by x 7533, x 7511, y 7453, x 7360, a poly hop between pads (7357,8667) / (7337,8798), a diagonal and tracks down the left bus field to the pad (7098,14525) and the row y 14524 at its foot (drawn to x 7550); no tap.
- The latch's gate line ("Its driver is not found"): it is the buffered clock `ck_out` (`tl4` runs 11-12, firm joins): `tc2_sr` is a latch on the clock.
