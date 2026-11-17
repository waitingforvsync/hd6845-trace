# dlat: the input latches of data bits 4-7

Region 16450-16950 x 13900-15800 (the gate column west of the data bus column `dbus`), and
the four latch outputs where they leave it west. Trace: `trace/dlat.txt` (it `@requires dbus`).
Started 2026-11-17 21:00 +0000 (Tom Seddon's session, Claude Fable 5.2).

## Status

Run 1 (2026-11-17). **Traced**: the four input latches of data bits 4-7 (cell `dlat_lat`, ten
transistors, four copies: 40 transistors), the two rails, the latch enable `dbus_le` from
`dbus`'s end at x 16950 through the column and out of it south at x 16774 (drawn to y 15935), and the four buffered pin levels
`d4_d`..`d7_d` from x 16950 into the latches. As extracted, for # = 4..7:

    d#_d_n  = NOT d#_d
    dl#_q   = NOT( (d#_d_n AND dbus_le) OR dl#_q_n )
    dl#_q_n = NOT( (d#_d   AND dbus_le) OR dl#_q   )

the same transparent latch as bits 0-3 (`notes/blocks/dbus.md`). **Not traced**: where the
four `dl#_q_n` lines go after they leave the column west (seen, see "Where the outputs go"),
and so the inverters that drive `db_b4`..`db_b7`. See Not done.

## Inventory

| What | Where | State |
|---|---|---|
| Latch, bit 5 | 16466-16848 x 14329-14814 | cell `dlat_lat` (master), traced |
| Latch, bits 6, 7 | the same cell at (0,477), (0,954); in bit 7 the VCC land of the two loads runs on into N3's VCC land (drawn per copy; both VCC) | placed: `tools/dbus_localmatch.py 16488 14329 16848 14814 0 477 12` (and `0 954`): best offset exactly (0,477) and (0,954), 0.82-0.90 in the clean shot, the metal shot and the chip-2 stripped shot |
| Latch, bit 4 | the same cell **upside down** (`my=14350`: y' = 28700 - y), y 13886-14371 | placed: `findcell` with `dbus_lat` (rot 180), clean shot 0.64, metal 0.65; overlay on both shots at 1.6x (`c4_ov.png`) |
| VCC rail | metal x 16491-16539, through the whole column and on north and south | drawn y 13880-15790 |
| VSS rail | metal x 16666-16712, the same | drawn y 13880-15790 |
| `dbus_le` | metal, from `dbus`'s (16950,13614): west to x 16860, south to y 13812, west to x 16819, south to y 15802, west to x 16774, south out of the region | drawn to y 15935 |
| `d4_d`..`d7_d` | poly rows y 13994-14016, 14684-14706, 15161-15183, 15638-15660 from x 16955 west into band E of each latch | drawn |
| East strip x 16850-16950 | nothing but the above and `dbus`'s capacitor rectangles and pads (views `e_top.png`, `e_bot.png`, 1.3x, metal and clean shot) | - |
| Bus inverters | **not in the column**: the latches fill y 13886-15768 without a gap (`findcell` with `dbus_drv`: 0.41-0.43, no copy) | see "Where the outputs go" |

## Logic

### The latch cell `dlat_lat` (traced)

The circuit and the layout of poly and diffusion are those of `dbus_lat`
(`notes/blocks/dbus.md`, "The input latch"), mirrored left to right: VCC rail on the west,
VSS rail in the middle, `dbus_le` on the east. What was checked and how:

- `findcell` with `dbus_lat`'s rectangle (17230 8885 17590 9370), all eight orientations,
  finds four copies and nothing else: `-742,5444 mx=17410` (bit 5), `-742,5921`, `-742,6398`
  (bits 6, 7) and `-742,5001 rot=180` (bit 4).
- `tools/dlat_shift.py` (block-by-block displacement of the bit-5 copy against the mirrored
  master): poly and diffusion lie within 3-5 px of the mirror image in the clean shot.
- **The contacts, pads and metals do not**: they lie 6-17 px west of where a mirror image
  puts them (`tools/textmap.py` on each contact: bright centre in both metal shots and the
  hole in the clean shot agree to 3 px). So the cell is drawn here as a cell of its own, the
  poly and diffusion mirrored from `dbus_lat` and every contact and metal measured:

  | Contact | mirror image | measured |
  |---|---|---|
  | M_d top (third pull-down's pad) | (16587,14454) | (16576,14455) |
  | M_d bottom (N1's load gate) | (16587,14657) | (16578,14658) |
  | M_c top (band A's pad) | (16778,14388) | (16766,14389) |
  | M_c bottom | (16765,14789) | (16756,14792) |
  | `dbus_le` on band B / band D | (16826,14434) / (16826,14652) | (16819,14436) / (16818,14654) |
  | VSS land, top / middle / bottom | (16714,14354) / (16716,14531) / (16710,14729) | (16697,14350) / (16701,14530) / (16702,14729) |
  | VCC, long contact / N3's | x 16508-16532 / (16523,14712) | x 16502-16522 / (16512,14710) |

  Metals (runs where R > 176 and G > 128 on rows of both metal shots): M_d bright
  x 16567-16580, M_c 16745-16758, `dbus_le` 16812-16825, VCC rail 16491-16538, VSS rail
  16666-16711.
- Views of the bit-5 copy at 3.1x in the clean shot with the outline and in the chip-2
  stripped shot (`c5t_b.png`, `c5t_a.png`, `c5b_b.png`, `c5b_a.png`): every band, load gate,
  tie box and land of the master is there.
- **Band A and the third pull-down's gate are two polys** (the junction that would short
  `d#_d_n` to `dl#_q_n`): 4x in three shots (`j1.png`). The gate poly from M_d's pad ends at
  x 16641 and band A at x 16665, both inside a field pocket 16628-16673 x 14386-14459 (a closed
  outline in both stripped shots; green in the clean shot between them:
  `tools/px.py row 14398 16596 16704 4`).
- **Band D ends at x 16669**, short of the tie box of N1's load at x 16620-16645
  (`tools/px.py row 14652 16596 16700 4`: dark and green from x 16644 to 16660).
- There is no thin metal through this cell (the one in `dbus_lat` is D0's output line), so
  the strip x 16600-16660 is open here and the clean shot's colours differ there from the
  master's: that is what `cellcheck.py`'s 14-21 % of badly matching blocks are.

What differs from `dbus_lat`'s circuit: nothing. What differs in the wiring:

- **`dl#_q_n` leaves west.** From the foot of the vertical poly at M_d's top pad a poly runs
  west along y 14427-14444 under the VCC rail (salmon there: `tools/px.py col 16510 14408
  14462 3`) and on in the open. The same in all four copies (`tools/px.py row` at y 14913,
  15390, 14264).
- **N1's east stub is cut short**: in `dbus_lat` the poly from N1's buried contact carries
  `dl#_q_n` to the bus inverter; here it ends at x 16790, like N0's stub above it (the two
  rows have the same profile: `tools/px.py row 14608 16740 16812 4` and `row 14479`).
- `d#_d` reaches band E directly in poly from the east (no metal).

### The latch enable `dbus_le`

One metal from `dbus`'s end (16950,13614) (`tools/follow.py 16900 13614 W`: corners
(16862,13616), (16858,13810), (16820,13813), (16812,15803), stop (16772,15800)).
Pads with contacts on bands B and D of the four latches (y 14046, 14264; 14436, 14654;
14913, 15131; 15390, 15608). The follower's other contact candidates (y 14723, 14746, 14788)
are not contacts: `tools/textmap.py 16798 14705 16846 14800 3` shows metal throughout in both
chips, no ring and no hole, against the pad at y 14652 as reference.

**It does not end in the region** (corrected after review round 1). The west arm
(y 15795-15808) turns south at x 16774 and the metal runs on south along x 16767-16781, bright
in both metal shots from y 15860 to 15935, 15990 to 16002 and 16020 to 16062
(`tools/textmap.py 16747 15790 16803 15975 5` and `16747 15960 16803 16110 6`). On the way it
passes over three heavy-outlined boxes, each at the west end of one of `dbus`'s output data
polys (`d5_out_n` at y 15815-15836, continuous to `dbus`'s pad (16863,15827): `tools/px.py row
15826 16780 16870 6`; then `d4_out_n`'s at y about 15957 and `d3_out_n`'s at y about 16087).
At each box the metal is dark for about 50 px and `tools/follow.py` stops. **These are not
contacts** (trap 22): the box centre measures 122/147/53 (chip 2) and 140/125/49 (chip 1),
greenish and dim, against 207/197/97 and 210/191/103 on this line's real pads; in the clean shot
it is tan (180/169/131), not the green of a contact hole (140/155/91) (`tools/px.py pt
16774,15826 16819,14436 metal,metal1,acid,acid1b`). The boxes are the buried contacts where
those polys land on a diffusion that leaves west. Run 1 first drew the box at (16772,15824) as
the enable's end contact, from blurred 6x views (`le_m.png`, `le_a.png`) in which the greenish
centre looked like a contact's bright centre; that would have joined `dbus_le` to `d5_out_n`'s
poly. Drawn to y 15935; where the metal goes after y 16104 is not followed. The enable's driver
is somewhere along it (its other end is the pad on D0's latch).

### Where the outputs go (seen, not drawn)

Views `w_top.png`, `w_bot.png` (1.5x, metal, chip-2 stripped and clean shot, x 16330-16500):

| Line | Leaves the cell | Then |
|---|---|---|
| `dl4_q_n` | west along y 14256-14273 | turns north at x 16458-16477, a poly in the gap between `areg_rail_r` and the VCC rail (orange in both chip-2 shots), from y 14255 up past y 13860 |
| `dl5_q_n` | west along y 14427-14444 | under `areg_rail_r` to x 16400, north along x 16400-16416 under that rail (salmon in the clean shot) past y 13860. `areg`'s notes: the arms at y 14431 and y 13657 of "the poly under `areg_rail_r`" |
| `dl6_q_n` | west along y 14904-14921 | a diagonal north-west from (16460,14900) to about (16365,14810), into the bundle: believed `areg_w7` (poly x 16364, which `areg` draws from y 14700 up to y 13453 and east to x 16480) |
| `dl7_q_n` | west along y 15381-15398 | a diagonal north-west from (16460,15380) past (16340,15255): believed `areg_w6` (`bd2`'s notes: contact (16337,14866), poly down x 16330-16345; `areg` draws the metal x 16341 from y 14700 up to the contact (16337,13264) and a poly east along y 13263 to x 16480) |

All four head for `areg`'s "four identical cells" at x 16480-16800, y 13060-13840, north of
this region: **believed** the four bus inverters (`db_b#` = NOT `dl#_q_n`). None of this is
drawn. Seen in one survey view (`n_wide.png`, 1.1x, metal and clean shot, x 16320-16880,
y 13010-13910, with `areg`'s trace):

- Four like cells between the same two rails, at y about 13100-13230, 13295-13425,
  13490-13620, 13685-13815 (pitch about 195). Each has a VCC land with a contact at about
  x 16530-16570, a load gate (open poly) at x 16575-16610, a gate band under the VSS rail at
  x 16650-16740, and a pad with a contact at about x 16750 near its top.
- A poly row runs east under each cell's lower edge, from the west: y 13263 (`areg_w6`, so
  bit 7 by the table above), y 13453 (`areg_w7`, bit 6), y 13657 (from x 16400: the poly
  under `areg_rail_r`, bit 5) and y about 13850 (from x about 16460: bit 4). Each reaches
  x about 16790.
- East of the cells: thin vertical metals at x about 16795 and 16845, with pads at about
  (16855,13520) and (16805,13710), and short polys east at y about 13330 and 13520: the
  candidates for the outputs towards the `db_b#` lines.

The pairing of rows with bits in the second item is from the direction each line was seen to
take, not from a drawn route.

Also checked with text tools in this run: `tools/dlat_contacts.py` (every metal contact of
all four copies: a bright centre in a dark ring within 3 px of the drawn place in both metal
shots, except three that are dim in one chip and bright in the other), and the poly rows of
`d4_d`, `d6_d`, `d7_d` from x 16842 to 16955 (`tools/px.py row 14005 | 15172 | 15649`: open
poly or poly under metal all the way).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `dbus_le` | metal | (16960,13606-13624) | ? | joins `dbus`'s metal at x 16950 |
| `dbus_le` | metal | x 16765-16783, y 15935 | in (believed) | the enable goes on south along x 16774 over the box ends of `d4_out_n` and `d3_out_n` (no contact), followed to y 16104; its driver is further on |
| `d4_d`, `d5_d`, `d6_d`, `d7_d` | poly | x 16955, y 13994-14016, 14684-14706, 15161-15183, 15638-15660 | in | from `dbus`'s buffers (its ports at x 16950) |
| `dl4_q_n`, `dl5_q_n`, `dl6_q_n`, `dl7_q_n` | poly | x 16466, y 14256-14273, 14427-14444, 14904-14921, 15381-15398 | out | the latch outputs, on west (see above) |
| `vcc` | metal | x 16491-16539, y 13880 and y 15790 | - | the column's VCC rail, continues both ways |
| `vss` | metal | x 16666-16712, y 13880 and y 15790 | - | the column's VSS rail, continues both ways |

## Ambiguities

1. **Which rail is which** rests on the loads (every load's far end is on the west rail), as
   in `dbus`; neither rail was followed to a known supply.
2. `?D` (16587-16613, 14384-14430) and its copies: the width of the third pull-down of N0
   (41 or 17), copied from `dbus_lat`'s Ambiguity 5. Sizes only.
3. `?B`/`?P` at N0's east tab (16750-16790, 14464-14492): a buried contact with a stub that
   goes nowhere, as in `dbus_lat`. Connects nothing.

## Review

**Round 1: full review** (2026-11-17 22:05-22:25 +0000, a fresh agent on claude-fable-5-2, at
commit 8d1ec73; images in `cache/scratch/dlat/review-1/`). Covered the one piece: the four
latches, the rails, `dbus_le`, `d4_d`..`d7_d`. Told to suspect: the cell's poly and diffusion
(mirrored from `dbus_lat`, not drawn from this column); the junctions band A / third pull-down
gate and band D / tie box in bits 4, 6, 7; the upside-down bit-4 copy; the buried-contact
boxes; N1's east stub; the west exits; `dbus_le`'s end and its pads; `d7_d`'s row under other
metals; anything left out of the region.

Checked and found correct (its report): band A / third pull-down gate, field through the
pocket in all four copies (`tools/px.py col 16650`; bit 5 at 4x in three shots); band D / tie
box, a gap at x 16652-16656 in all four (bits 5 and 4 at 4x); both east stubs end at about
x 16790 in all four, field under `dbus_le`; no contact of M_c or M_d on the tabs (6x), on bands
D and E or on N0's load gate, and the two load gates separate; the west exits, poly under the
VCC rail in all four, no contact; `dbus_le`'s eight taps real, the line continuous from
y 13614, no other contact on the run; `d4_d`..`d7_d` continuous to x 16955, `d7_d` without a
contact under the two crossing metals; the copies (`cellcheck.py` median 0.94-0.96 in three
shots, 0.99 on the open strip x 16592-16676; bit-4 overlay); rails unbroken; the east strip
holds only `dbus`'s shapes; `tools/unsure.py` lists nothing. Not checked: the junctions of
bits 6 and 7 by image (profiles and `cellcheck.py` only), N1's tab at 6x, `dbus`'s side of
`d5_out_n`, which rail is which, the structures at x 16450-16490, y 15440-15800 (`bd2`'s).

Findings:

1. **`dbus_le`'s end is wrong** (changes a connection: a contact that does not exist, and
   where the wire leaves the package). The box under the "end contact" (16772,15824) is the
   west end of `dbus`'s `d5_out_n` poly, and the metal does not end there: it runs on south.
   **Confirmed** by the tracer: `tools/px.py row 15826 16780 16870 6` (poly continuous from
   x 16798 to `dbus`'s pad), `tools/textmap.py 16747 15790 16803 15975 5` (metal bright in both
   chips at y 15860-15935, the same dark stretch again at y 15940-15965), `tools/px.py pt
   16774,15826 16819,14436 metal,metal1,acid,acid1b` (centre greenish and dim, clean shot tan:
   a pass-over of a buried-contact box, trap 22). Fixed: contact, pad and label removed, the
   metal drawn on south to y 15935, port moved; notes, glossary, `operation.md`, floor plan.
2. **Bit 7's VCC land differs from the master** (geometry only: both lands are VCC). The
   clean shot is one tan area at x 16516 from y 15470 to 15700; the master has field at
   y 14636-14684. **Confirmed**: `tools/px.py col 16516 15570 15712 6` against `col 16516 14616
   14758 6` (one edge line at y 15645 against 45 px of field), metal contact bright from
   y 15614 to 15692 in chip 1. Fixed: a diffusion and a contact for bit 7 outside the cell.

`tools/t.sh dlat sameconn.py 8d1ec73`: `connections identical`; `.venv/bin/python
tools/sameconn.py 8d1ec73`: `connections identical` (the removed contact joined the metal to a
pad that carried the same name, so the extraction's nets do not change; the finding counts as
a connection change all the same: a contact was drawn that is not there).

Round 1: one finding that changes a connection (`dbus_le`'s end), fixed; one geometry finding, fixed.

## Not done

- **The four outputs** `dl4_q_n`..`dl7_q_n` west of x 16466, as far as the gates they drive
  (table above), and those gates: the bus inverters of bits 4-7 and their joins to
  `db_b4`..`db_b7`. Start from the table; the cells are north of this region
  (x 16480-16800, y 13060-13840, in `areg`'s old region).
- `dbus_le` south of y 15935 (metal x 16767-16781; seen to y 16104), to its driver.
- The three boxes it passes over are the west ends of `d5_out_n`, `d4_out_n`, `d3_out_n` (`dbus` draws those polys to x 16817, 16860, 16905): each a buried contact onto a diffusion that leaves west. Not drawn: they are the outputs of those lines' drivers, in `bd2 (rest)`'s column.
- The rails north of y 13880 and south of y 15790.
- Sizes: the cell's poly and diffusion are `dbus_lat`'s mirrored, not re-measured edge by
  edge here (within 3-5 px by `tools/dlat_shift.py`).
