# dlat: the input latches and bus inverters of data bits 4-7

Region 16450-16950 x 13900-15800 (the gate column west of the data bus column `dbus`), plus,
since run 2, the four bus inverters north of it (x 16480-16810, y 13095-13860) and the routes
to them (x 16320-16480, y 13250-15400). Trace: `trace/dlat.txt` (it `@requires dbus`).
Started 2026-11-17 21:00 +0000 (Tom Seddon's session, Claude Fable 5.2).

## Status

Runs 1 and 2 (2026-11-17). **Traced** (48 transistors): the four input latches of data bits
4-7 (cell `dlat_lat`, ten transistors, four copies), the four inverters that drive the
internal data bus bits 4-7 (cell `dlat_drv`, two transistors, four copies), the routes of the
four latch outputs to them, the joins of the inverters' outputs to `db_b4`..`db_b7`, the two
rails, the latch enable `dbus_le` through the column, and the buffered pin levels
`d4_d`..`d7_d` from x 16950 into the latches. As extracted with every trace file loaded, for
# = 4..7:

    d#_d_n  = NOT d#_d
    dl#_q   = NOT( (d#_d_n AND dbus_le) OR dl#_q_n )
    dl#_q_n = NOT( (d#_d   AND dbus_le) OR dl#_q   )
    db_b#   = NOT dl#_q_n

the same as bits 0-3 (`notes/blocks/dbus.md`): a transparent latch on the pin, open while
`dbus_le` is high, and a static inverter that drives the internal data bus bit all the time.
**So all eight internal data bus lines are driven from the data pins' input latches by
static inverters.** **Not traced**: `dbus_le` south of y 15935 and its driver; the rails'
ends. See Not done.

## Inventory

| What | Where | State |
|---|---|---|
| Latch, bit 5 | 16466-16848 x 14329-14814 | cell `dlat_lat` (master), traced |
| Latch, bits 6, 7 | the same cell at (0,477), (0,954); in bit 7 the VCC land of the two loads runs on into N3's VCC land (drawn per copy; both VCC) | placed: `tools/dbus_localmatch.py 16488 14329 16848 14814 0 477 12` (and `0 954`): best offset exactly (0,477) and (0,954), 0.82-0.90 in the clean shot, the metal shot and the chip-2 stripped shot |
| Latch, bit 4 | the same cell **upside down** (`my=14350`: y' = 28700 - y), y 13886-14371 | placed: `findcell` with `dbus_lat` (rot 180), clean shot 0.64, metal 0.65; overlay on both shots at 1.6x (`c4_ov.png`) |
| VCC rail | metal x 16491-16539, through the inverters and the latches and on north and south | drawn y 13060-15790 |
| VSS rail | metal x 16666-16712, the same | drawn y 13060-15790 |
| `dbus_le` | metal, from `dbus`'s (16950,13614): west to x 16860, south to y 13812, west to x 16819, south to y 15802, west to x 16774, south out of the region | drawn to y 15935 |
| `d4_d`..`d7_d` | poly rows y 13994-14016, 14684-14706, 15161-15183, 15638-15660 from x 16955 west into band E of each latch | drawn |
| East strip x 16850-16950 | nothing but the above and `dbus`'s capacitor rectangles and pads (views `e_top.png`, `e_bot.png`, 1.3x, metal and clean shot) | - |
| Bus inverter, bit 6 (`k2`) | 16480-16810 x 13290-13470, north of the latches between the same two rails | cell `dlat_drv` (master), traced (run 2). Not a copy of `dbus_drv` (`findcell`: 0.40-0.44) |
| Bus inverters, bits 7, 5, 4 (`k1`, `k3`, `k4`) | the same cell at (0,-195), (0,195), (0,390) | placed: `tools/dbus_localmatch.py 16500 13290 16820 13470 0 195 8`: best offset exactly (0,195), 0.93 clean shot, 0.89 metal; `tools/cellcheck.py dlat_drv`: median 0.95-0.97 in the metal shot and both stripped shots, 3-12 % of blocks differing |
| Routes `dl4_q_n`..`dl7_q_n` | x 16320-16480, y 13250-15400 | drawn (run 2), see "The routes" |
| `db_b4`, `db_b5`, `db_b6` | thin metals x 16818, 16862, 16904 from `rdp3`'s south edge (y 12900) down to end pads at (16818,13721), (16862,13525), (16904,13330) | drawn from y 12895 |
| `db_b7` | poly x 16787-16805 from `rdp3`'s south edge down to `k1`'s output box | drawn from y 12895 |

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

### The bus inverter cell `dlat_drv` (traced, run 2)

Master = the second cell from the top (`k2`, y 13290-13470); views at 3x in the clean shot,
the metal shot and the chip-2 stripped shot (`k2_b.png`, `k2_m.png`, `k2_a.png`), the node
strip and both boxes at 5x in both stripped shots (`k2_top5.png`), overlay `k2_ov2.png`.

    out = NOT in          (for the four copies: db_b7, db_b6, db_b5, db_b4 = NOT dl#_q_n)

| What | Where (master) |
|---|---|
| VCC land | 16495-16545 x 13325-13398, long contact 16505-16527 x 13337-13385 under the VCC rail |
| Load | gate: an open poly block 16548-16588 x 13300-13405 over the strip y 13330-13400 (W 70, L 40: a strong load); its arm runs east along y 13298-13322 and ends in a heavy-outlined box 16612-16650 x 13314-13347 (both stripped shots): the buried contact that ties the gate to the node. The load strip's top end and the node strip's west end meet in that box |
| Node | a strip above the gate band, y 13340-13362, from the box east under the VSS rail (tan there: `tools/px.py col 16690 13284 13452 6`: edge at y 13338, tan 13344-13356) to x 16772, with a tab north at x 16742-16786 up to y 13318 |
| Pull-down | gate band: poly y 13364-13386 from a rounded west end at x 16632 to x 16802; bright salmon (236/165/120, poly over a channel) under the rail; the diffusion runs through under it from the node strip to the VSS side, x 16650-16772 as drawn (W 100-125, L 22: the west edge is a dark line across the band at x 16644-16650, and on the node side the last 25 px are a narrow slit under the output box) |
| VSS land | below the band: under the rail a land x 16678-16724 down to y 13438 with the contact (16690,13410) (a ring in the metal shot); east of the rail only a strip y 13388-13406 to x 16772 (`tools/px.py col 16745 13386 13440 6 acid`: red minus green 16-28 down to y 13404, -14 to 4 below) |
| Input | the band's east end joins a vertical open poly x 16786-16804 that runs down to the input row, a poly y 13451-13469 under the cell's lower edge, which arrives from the west |
| Output | a second heavy-outlined box 16756-16788 x 13318-13347 on the node's tab, with no metal over it (a buried contact); the poly leaves it east along y 13320-13343 |

What is not diffusion: the patch under the VSS rail above the node strip (y 13284-13334) is
grey-khaki, not pink, in the clean shot (144/135/107), but green field in the chip-2 stripped
shot (146/152/91) with no outline: field (`tools/railprof.py` calls it diffusion in this cell
and field in the cell above). The four khaki pockets with heavy outlines at the cell's corners
are field too (`tools/px.py pt 16595,13428 16620,13428 16780,13300 16600,13285 acid1b,acid`:
red minus green -2 to 1 in the chip-2 stripped shot).

### The outputs: `db_b4`..`db_b7`

`rdp3` ends the four data lines at its south edge (y 12900): `db_b7` as a poly x 16788-16808,
`db_b4`, `db_b5`, `db_b6` as thin metals x 16818, 16862, 16908. Here:

| Cell | Output | Evidence |
|---|---|---|
| `k1` | the poly comes straight down x 16787-16805 to the east side of the output box: **`db_b7`** | `tools/px.py row 13000 | 13080 | 13120 16768 16832 4`: open poly at x 16792-16804 on each; 5x in both stripped shots, `k1_out.png` |
| `k2` | poly east along y 13320-13343, under the metals of `db_b4` and `db_b5` without contact, to a pad and contact (16904,13330) at the end of **`db_b6`**'s metal | `tools/follow.py 16905 13200 N|S`: one piece from y 12654 (`rdp3`'s contact (16908,12656)) to y 13334; `tools/textmap.py 16877 13307 16931 13349 3`: bright centre in a dark ring in both metal shots, a hole in the pad in the clean shot |
| `k3` | the same to the pad and contact (16862,13525): **`db_b5`** | follower: one piece y 12696-13528; text map as above |
| `k4` | the same to the pad and contact (16818,13721): **`db_b4`** | follower: one piece y 12742-13724; its contact candidate (16820,13227) is not a contact (metal bright through it, no ring, no hole: `tools/textmap.py 16793 13206 16847 13248 3`) |

So the top cell is bit 7 and the bottom one bit 4. With every trace file loaded the extraction
joins each output to its `db_b#` net of `rdp3` by overlap at y 12895-12900.

### The routes of the latch outputs (run 2)

Each `dl#_q_n` leaves its latch west along the exit row (x 16466). Views `w_top.png`,
`w_bot.png` (1.5x, three shots), overlay `diag_ov.png` (1.5x, metal and clean shot with
`areg`'s trace), and:

| Line | Route | Evidence |
|---|---|---|
| `dl4_q_n` | the exit row (y 14256-14273) turns north at x 16459-16477, a poly in the gap between `areg_rail_r` and the VCC rail, up to y 13841, and east as `k4`'s input row | chip-2 stripped shot: poly (red minus green 45-75) all the way down `tools/px.py col 16467 13830 14290 20 acid`, field above y 13840; rows across at y 13900, 14100, 14230: one poly at x 16460-16476; `row 13850`: poly from x 16464 east into the row |
| `dl5_q_n` | the exit row (y 14427-14444) runs on west under `areg_rail_r` to x 16400, north under that rail along x 16400-16418 to y 13646, and east as `k3`'s input row | clean shot: salmon all the way down `tools/px.py col 16408 13630 14460 30`, pink field at y 13630; rows across at y 13700 ... 14400: salmon at x 16402-16416, pink on its east side, open ground on its west; `row 13655`: the row east from the corner |
| `dl6_q_n` | a diagonal north-west from the exit row (16466,14912) to (16364,14810), then north along x 16354-16374 into the poly that `areg` draws from y 14700 as `areg_w7`, which runs up to y 13453 and east to x 16480: `k2`'s input row | `tools/dlat_polyruns.py row 14912 16320 16480 14890 ... 14720`: the poly's centre at (16451,14890), (16430,14870), (16411,14850), (16385,14830), (16367,14810), then x 16362-16368 on every row up to y 14720 |
| `dl7_q_n` | a diagonal north-west from the exit row (16466,15389) through (16408,15330) to (16341,15240), north along x 16332-16350 to a pad and contact (16339,14868), then the thin metal x 16340 north into the metal that `areg` draws from y 14700 as `areg_w6`, to its contact (16337,13264) and a poly east along y 13263: `k1`'s input row | `tools/dlat_polyruns.py row 15389 ...`: centres (16438,15360), (16408,15330), (16385,15300), (16360,15270), (16338,15240); `tools/px.py col 16338 14850 15260 15`: poly from y 15255 to 14985 in the open and salmon under a metal at y 14910-14955, the pad at y 14880; `tools/textmap.py 16311 14845 16365 14890 3`: the contact (bright centre in a ring in both chips, hole in the pad); `tools/follow.py 16341 14780 N`: one piece to (16339,13262); its candidate (16341,14268) is not a contact (`tools/textmap.py 16314 14240 16368 14296 4`) |

`areg_w6` and `areg_w7` are therefore `dl7_q_n` and `dl6_q_n` (`@alias` in `trace/dlat.txt`;
the rename is proposed to the coordinator). `k1`'s and `k2`'s input rows west of x 16480, and
the stretch of both lines north of y 14700, are `areg`'s drawing, not re-read here beyond the
follower run and the survey view `n_wide.png`.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `dbus_le` | metal | (16960,13606-13624) | ? | joins `dbus`'s metal at x 16950 |
| `dbus_le` | metal | x 16765-16783, y 15935 | in (believed) | the enable goes on south along x 16774 over the box ends of `d4_out_n` and `d3_out_n` (no contact), followed to y 16104; its driver is further on |
| `d4_d`, `d5_d`, `d6_d`, `d7_d` | poly | x 16955, y 13994-14016, 14684-14706, 15161-15183, 15638-15660 | in | from `dbus`'s buffers (its ports at x 16950) |
| `dl6_q_n` | poly | x 16354-16374, y 14695 | out | joins `areg`'s poly (`areg_w7`) at y 14700 |
| `dl7_q_n` | metal | x 16333-16348, y 14695 | out | joins `areg`'s metal (`areg_w6`) at y 14700 |
| `dl6_q_n`, `dl7_q_n` | poly | x 16470, y 13451-13469 and y 13256-13274 | in | `areg`'s rows arriving at `k2` and `k1` (its drawing ends at x 16480) |
| `db_b7` | poly | x 16787-16805, y 12895 | out | joins `rdp3`'s poly at y 12900 |
| `db_b4`, `db_b5`, `db_b6` | metal | x 16818, 16862, 16904 (16 wide), y 12895 | out | join `rdp3`'s metals at y 12900 |
| `vcc` | metal | x 16491-16539, y 13060 and y 15790 | - | the column's VCC rail, continues both ways |
| `vss` | metal | x 16666-16712, y 13060 and y 15790 | - | the column's VSS rail, continues both ways |

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

**Round 2: fix check** (2026-11-17 22:30-22:45 +0000, a fresh agent on claude-fable-5-2, of the
changes since 8d1ec73, at commit 6e79f1a; images in `cache/scratch/dlat/review-2/`, 4 used).
Told the two findings of round 1 and their fixes, and to check: that `dbus_le` is one metal
through the dark stretch y 15810-15858, the corner at (16774,15802), no contact at the box or
anywhere down to y 15935; that bit 7's added diffusion lies on diffusion, that no poly crosses
it, and that its contact is there; everything within about 100 px of a changed item.

Checked and found correct (its report): the box's interior is protected tan in the clean shot
(187/173/129), like the boxes at y 15957 and 16087 and the buried boxes under M_c, where real
contact holes nearby are green ((16815,15867): 152/177/96; the line's own pads 141/164/89); all
three boxes give the same text-map pattern in both metal shots (about 50 px dark with a
half-bright 6 px spot) and at boxes 2 and 3 the line is bright on both sides, so it is one
metal; the arm is bright at y 15798-15806 and ends at x 16767, the vertical at x 16768-16780, no
metal north of the arm; the band crossing at y 15858-15876 is salmon with no hole or ring and
y 15885-15935 is bright over pink field; the metal at x 16815 that starts on the pad
(16815,15867) is separate (`d5_out_n`'s poly shows between it and the arm). Bit 7: the column
x 16530 is uniform tan from y 15566 to 15662, where bits 4, 5 and 6 each have a pink gap between
two edges; no poly crosses (167 transistors as before); both metal shots show one long ring.
Both `tools/sameconn.py 8d1ec73` runs: `connections identical`.

It remarked, as geometry needing no change: bit 7's contact spans about y 15611-15697 against
the drawn union 15616-15681, and that land's west edge at y 15630 is about x 16500, not 16493.
Left as drawn (within the cell's general accuracy; both VCC).

Round 2: no findings.

### Run 2 (2026-11-17)

**Round 1, full review of what run 2 added** (2026-11-17 23:10-23:25 +0000, a fresh agent on
claude-fable-5-2, at commit 7c1c5ae; 25 images in `cache/scratch/dlat/review-3/`). Three pieces
in one brief: A the bus inverter cell `dlat_drv` and its three copies, B the outputs to
`db_b4`..`db_b7`, C the routes of the four latch outputs. Told to suspect: how the load strip,
the tie box and the node strip connect; the channel's extent in the open east of the rail and
any other diffusion under the band or the vertical; the patch under the VSS rail called field
against `tools/railprof.py`; whether the output box is a buried contact; per-copy differences;
`k1`'s junction with the poly from the north and that poly's run to `rdp3`; the three end
contacts and the crossings under the thin metals; trap 10 on both diagonals and on the polys
under and beside the wide rail; `dl7_q_n`'s vertical and its contact (trap 22); which input
row each route reaches; anything left out of 16450-16930 x 12900-13880.

Checked and found correct (its report). A: load, tie box and node strip at 6x in both stripped
shots; neither box has metal over it; the patch under the rail at y 13284-13334 is field (no
tan, no outline, a dark edge between it and the node); the vertical x 16786-16804 is poly
throughout, the source strip ends at x 16775 and the pocket is field; output poly and the
band's vertical are 12 px of field apart in all four copies; `k1`, `k3`, `k4` by overlay at
3.2-3.5x in the clean shot and per-copy profiles. B: `k1`'s junction at 6x in both stripped
shots, its poly does not go on east; the north run at 2.5x in three shots (one poly, three
metals, field between); the three end contacts (bright centre in a ring in both chips, green
hole in the clean shot); no contact at the crossings or at (16820,13227); the follower gives
one piece per metal up to `rdp3`'s contacts. C: both diagonals at 3.9x in both stripped shots;
`dl7_q_n`'s vertical continuous in three shots and its contact (16339,14868) real; the metal
branch over it at y 14905-14960 has no contact; (16341,14268) is not a contact; `dl5_q_n` and
`dl4_q_n` with their corners at 4x in both stripped shots, no tap or break, field between
them; each route reaches the row claimed and crosses no diffusion; the four equations; nothing
untraced in 16450-16930 x 12900-13880 but the rails north of y 13060. Not checked: `areg`'s
stretches of `dl6_q_n` and `dl7_q_n` (y 13264-14700) above 1.7x; `dl7_q_n`'s vertical is only
weakly orange in the chip-2 stripped shot (it rests on both metal shots and the clean shot);
`k1`, `k3`, `k4` in chip 2 by profiles and a 1.28x survey only.

Findings, both geometry only:

1. **The VSS land east of the rail was overdrawn** (all four copies): the drawn column
   16660-16772 x 13340-13438 included the field pocket 16728-16772 x 13408-13438. **Confirmed**:
   `tools/px.py col 16745 13386 13440 6 acid` and `col 16760`: red minus green 16-28 down to
   y 13404, -14 to 4 from y 13410 on. Fixed: the column ends at y 13406, with a separate land
   16678-16724 x 13400-13438 under the rail. No poly crosses the removed part; all `vss`.
2. **The pull-down's width**: the channel's west edge is at about x 16648, not 16660, and on
   the node side x 16748-16776 is a narrow slit. **Confirmed** as far as the profiles go
   (`tools/px.py row 13375 16630 16670 3 acid,acid1b`: dark at x 16642-16654, the band bright
   from x 16660). Fixed: west edge at x 16650; W recorded as 100-125. One transistor either way.

`tools/t.sh dlat sameconn.py 7c1c5ae`: `connections identical`; `.venv/bin/python
tools/sameconn.py 7c1c5ae`: `connections identical`.

Round 1: no findings that change a connection.

## Not done

- `dbus_le` south of y 15935 (metal x 16767-16781; seen to y 16104), to its driver.
- The three boxes it passes over are the west ends of `d5_out_n`, `d4_out_n`, `d3_out_n` (`dbus` draws those polys to x 16817, 16860, 16905): each a buried contact onto a diffusion that leaves west. Not drawn: they are the outputs of those lines' drivers, in `bd2 (rest)`'s column.
- The rails north of y 13060 and south of y 15790 (both go on).
- North of `k1` (x 16480-16810, y 12900-13095) and the strip x 16810-16950, y 12900-13600 beside
  the three data metals: not looked at beyond the survey views (`n_wide.png`, `oe.png`: no
  device seen).
- `areg`'s part of `dl6_q_n` and `dl7_q_n` (north of y 14700 and the two rows west of x 16480)
  was not re-read here.
- Sizes: `dlat_lat`'s poly and diffusion are `dbus_lat`'s mirrored (within 3-5 px by
  `tools/dlat_shift.py`); `dlat_drv`'s shapes are from 3x views and one overlay, good to
  about 5 px.
