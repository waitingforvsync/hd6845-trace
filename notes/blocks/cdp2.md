# cdp2: central datapath, rows y 5700-8450 (x 7600-10850)

Trace: `trace/cdp2.txt`. Scratch: `cache/scratch/cdp2/`. Tools: `tools/cdp2_pt.py`
(colour at points, both chips; used to test for contacts), `tools/cdp2_map.py` (text map
of colour classes), `tools/cdp2_lines.py` (follow a horizontal poly line by colour),
`tools/cdp2_mo.py` (stripped shot with the metal outline), `tools/cdp2_cls.py` (false-colour
class map), `tools/cdp2_reg.py` and `tools/cdp2_cmont.py` (registration of the clean shot
against the metal shot), `tools/cdp2_w.py` (sharpened panels with the metal outline). `tools/rdp3_sharp.py` (unsharp
mask) at 3.3-5x on a median composite (`--comp cdp2_a`) is what made the junctions readable.

## Slice tags and array columns

**Tag sK of this block is array column cK** (K = 1..7; column c0, x 7605-7995, has no
cell in these rows). The column formula x = 7605 + 390.3 N gives the *left edge* of the
wide VSS rail of column N (c4: 9166); the first run's "VSS at x 9184 + 390 k" is the
*centre* of the same 46 px rail (s4: x 9161-9207). The two agree to 5 px: no conflict.
The numbering is also cdp4's (its s2 rail x 8381-8427 is this block's s2 rail at
x 8403). The rail at x 10744 is a ninth one, right of c7; it carries the pull-downs of
s7's cells. Rows A and B1/B2 occupy c3..c7, row C c1..c7, row D c2..c7.

Bit order (believed, from the direction of the chain in rows B, see Logic): **s3 is
the most significant of the five compared bits, s7 the least.**

## Status

- **Run of 2026-11-20 19:36 -0600**: **the inverter's output is `tc1_ns3`** (wiring, one join; it rests on piece `ga`'s two
  `?B`): the metal that ends on the output row's pad (7662,7083) is one metal (x 7652-7670) with the
  metal `tc2` draws from its pad (7660,6193) south to y 6400 as `tc1_ns3` (`tl5_tracks.py v 7661 6390
  7070`: bars of 10 px or less; bare ground south of the pad: `px.py col 7661 7085 7120 5`). Drawn
  y 6400-7083; `cdp2_w7065` is an alias of `tc1_ns3`. So **`tc1_ns3` = NOT `tc2_sr_q`** (marked): the line that
  runs north past `rax`'s units into the top-centre logic is the inverted output of `tc2`'s latch.

- **Run of 2026-11-20 19:10 -0600**: **piece `wn`** (wiring, 3,100 px, no uncertain item; reviewed: round 7 a port's side, fixed; round 8, the fix check, no findings): the two metals of the upper
  series gate followed north to their ends. `cdp2_w7092` (the gate's output) ends on a pad (8290,5327)
  whose poly row goes east (port: a gate in the logic at y 5300-5350, undrawn). `cdp2_w7128` (its row 1)
  comes from a contact (8705,4810) on the west end of a diffusion band y 4776-4838 that goes on east
  (port at x 8745: `cdp1`'s undrawn slice-0 logic).

- **Run of 2026-11-20 18:57 -0600**: **piece `gh`, the load of the comparator's line `cdp2_b_hl`** (x 8578-8745,
  y 7352-7432; 1 transistor, one uncertain item, the load's tie; reviewed: round 6, no finding that changes a connection). `cdp2_b_hl`'s metal x 8715-8735 ends on a
  diffusion that a poly plate parts from a contact to the VCC metal x 8594-8644: a depletion load
  (about 37/42). The plate is one poly with row 2 of the lower series gate, so **`cdp2_w7344` is `cdp2_b_hl`** and
  `cdp2_w7272` = NOT(`cdp2_b_hl` AND `cdp2_b_s7_x`) (marked: through the tie's `?B`). With its load drawn,
  `cdp2_b_hl` extracts as a gate for the first time: NOT(OR over s3..s7 of (`_p1` AND `_y`)).

- **Run of 2026-11-20 18:21 -0600**: **piece `gu`, the upper series gate** (x 8205-8550, y 6300-7230; 3 transistors,
  one uncertain item, a `?M` on a passing metal): **`cdp2_w7092` = NOT(`cdp2_w7128` AND `cdp2_w7272`)**. Row 2 is
  the lower gate's output. Row 1 is a poly column from a pad (8530,6955), whose metal x 8503-8517 comes
  from a pad (8508,6325), the west end of a poly row to a pad (8680,6324) with a metal from the north
  (`cdp2_w7128`; source not followed). Its own output leaves by its load plate's poly north to a pad
  (8290,6997) and a thin metal north (port; the follower: to (8290,5323)). And the lower gate's row 1 is
  now joined to its source: **the comparator chain's output `cdp2_b_s7_x`** (the metal `cdp2` drew down
  from line 6888 ends on that row's pad (8682,7300)). So:
  `cdp2_w7092` = NOT(`cdp2_w7128` AND NOT(`cdp2_b_s7_x` AND `cdp2_w7344`)).
  (The first drawing made row 1 `db_b5`; review round 4 showed that `db_b5`'s metal turns away 37 px short
  of the pad.)

- **Run of 2026-11-20 18:00 -0600**: **piece `gl`, the lower of two series gates left of rows B** (x 8205-8600,
  y 7160-7400; 3 transistors, one uncertain item, a `?M` on a passing metal; reviewed: round 3, no finding that changes a connection): **`cdp2_w7272` = NOT(`cdp2_b_s7_x` AND `cdp2_w7344`)**, two
  pull-downs in series under the rail x 8375-8425 with a tied load. Its two gate rows come from the east
  (ports at x 8600, not followed); its output goes by a buried contact and a poly north to become row 2 of
  the gate above it (the same build, y 7075-7240, not drawn yet): the two look cross-coupled.

- **Run of 2026-11-20 17:16 -0600** (Matt Godbolt's session, Claude Fable 5.2): **piece `ga`, the first gate of
  the logic left of rows B** (x 7645-8253, y 6985-7140; 2 transistors, three uncertain items; reviewed: round 1 one finding that changes connections, fixed; round 2, the fix check, none): an inverter,
  **`cdp2_w7065` = NOT `tc2_sr_q`** (marked: its load's tie and its output's buried contact are both `?B`).
  The output leaves on a poly row west to a pad (7662,7083) and a metal north (port). Two thin metals
  pass over the gate without contact: `db_b6`'s (x 8107-8121) and a through line `cdp2_w6845` (x 7978-8000:
  from a pad (7335,6845) by a poly row and a pad (7987,6845) south 1,470 px to the pad (7878,8315) in
  `cdp3`'s cluster). The first drawing had both as contacts on the gate's node; review round 1 showed
  they are not. See "The logic left of rows B" under Logic. (Channel 3 needs nothing: `bw` draws its
  five lines.)

- Row A (y 6020-6345, five latch cells, s3..s7) and row C (y 7500-7825, seven latch
  cells, s1..s7): traced in the first run. **Changed in the second run: the track b
  that crosses every latch cell is a through track with no contact in the cell** (the
  first run had it contacted to the n2 land and, as a second piece, to the VCC land; see
  Ambiguities 3). The latch's only output is q.
- Channel 1 (y 5720-6060): traced in the first run between x 8480 and 10850. With the
  change above its long poly lines are the *sources* of the through tracks, not outputs
  of row A.
- Rows B1/B2 (y 6940-7480, s3..s7): **traced, one cell `cdp2_cmp` placed five times,
  instances checked (1-4 % bad blocks in both layers), extracts clean** (142 transistors
  in the file, no errors, no open nets): a 5-bit comparator of row C's register against
  the value on the through tracks. One connection inside the cell could not be seen
  and is left open (nets `p1` and `o2`, Ambiguities 6).
- Loose ends followed in the second run: the comparator's three outputs/inputs to
  where they enter the logic left of the rows, both strobes to their contacts just east
  of the region, the lower ends of the through tracks (they stop at the foot of row C).
- Not traced: row D (a large cell that continues below y 8450 as cdp3's row A),
  channels 2 and 3 as such, the logic left of the rows. See Not done.

## Conventions

- Master slice **s4** (VSS rail x 9161-9207, VCC rail x 9375-9425). Offsets from
  findcell: s3 -390, s4 0, s5 390, s6 780, s7 1170 (row C: -1171, -781, -391, 0, 390, 781,
  1171 for s1..s7).
- Rails: **VSS = the wide rail at x 9184 + 390k, VCC = the rail at x 9400 + 390k**
  (by the loads and pull-downs of rows A and B).
- Colours in the clean shot here (measured, `cdp2_pt.py`, `larr_px.py`). Under metal:
  poly over field salmon (221,164,120), **poly over a channel brighter (240,172,124)**,
  diffusion tan (196,178,134), field pink (195,117,126). In the open: poly dark orange
  and textured (over field and over channels alike), field khaki, diffusion mauve to
  light tan (not separable from field by colour: use the outline, and the metal shot,
  where open poly is orange-brown). The first run's contact test (greenish, speckled
  patch, s.d. over 12) also fires **where a metal line steps onto or off a poly block**
  and down the middle of the wide rails, so by itself it does not prove a contact; a
  contact also shows as a ring with a pad in the metal shot.
- **Metal looks narrow (an 8 px bright streak) where it runs over a poly block**, in
  both metal shots. It is not interrupted: the clean shot is protected (smooth salmon,
  tan) over the full width of the line there. This applies to the bus line at y 7180-7265
  and 7335-7372 (first run: "interrupted") and to track b over the latch's n2 load.
- Small dark rings on a poly line where it passes the gap between two metal lines
  (for example 9222,7248; 9275,7150; 9307,7392) are the metal-gap artefact, not contacts.
- Registration of the clean shot against the metal shot, checked on five contacts of the
  row B cell (`tools/cdp2_cmont.py`): within 2 px.

## Inventory (rows, top to bottom)

| y | What | Slices | State |
|---|---|---|---|
| 5720-6060 | channel 1: horizontal poly lines at y 5826, 5870, 5913, 5956, 6000 (long), 6042 and 5783 (short), pads at y 5740; they feed the through tracks; row A's q tracks cross them | - | traced between x 8480 and 10850 |
| 6020-6345 | **row A: five static latch bits** `cdp2_lat` | s3..s7 (x 8790-10745) | traced |
| 6000-6310, x 7700-8300 | random logic left of row A | - | not traced |
| 6314-6334 | row A's load strobe `wr_r11` (poly, loops through every cell) | - | traced inside the row; ends not followed |
| 6350-6900 | channel 2: 13 horizontal poly lines, pitch 43.3, at y 6366, 6410, 6456, 6498, 6542, 6584, 6626, 6672, 6714, 6756, 6802, 6844, 6888. Per-slice metal lines and rails cross over them | - | not traced |
| 6940-7480 | **rows B1/B2: 5-bit comparator**, cell `cdp2_cmp` (row C's register against the through tracks) | s3..s7 | traced |
| 6948-6966 | `cdp2_b_hl`: diffusion line along rows B, x 8705-10762 | - | traced; its metal exit at the left followed to y 7400 |
| 6900-7480, x 7900-8750 | irregular logic left of rows B | - | not traced |
| 7500-7825 | **row C: seven static latch bits**, same cell as row A (dy 1476; dx -1171, -781, -391, 0, 390, 781, 1171) | s1..s7 | traced |
| 7830-8030 | channel 3: five horizontal poly lines (y 7843, 7886, 7930, 7973, 8017); at the left (x 7650-7800) they turn down; only the bus lines and the rails cross it | - | not traced |
| 8040-8450+ | row D: large cell, six copies (s2's differs at the top), continues below y 8450 as cdp3's row A | s2..s7 | not traced |

Per-slice vertical metal in channel 2 (measured at y 6542/6563, master slice): VSS rail
x 9165-9205, line a x 9243-9252, a line at x 9333-9340, VCC x 9378-9402, a narrow line
at about x 9411-9420. Nothing between x 9423 and 9550.

## Logic

### Row A: five static latch bits (traced)

Cell `cdp2_lat`, master s4 at x 9160-9560, y 6020-6345. It is the cell of rdp3's row AR
(`rdp3_lat`) turned upside down: x' = x - 5379, y' = 19351 - y maps every feature of
that cell onto this one within a few px. Each feature was nevertheless placed from this
row's photos. Six transistors:

```
a   <- bus    pass transistor T1 (36/23 at 9246,6278), gate wr_r11
n2  = NOT a   pull-down T2 50/22 at 9243,6175; load 16/51 at 9345,6224
q   = NOT n2  pull-down T1' 53/22 at 9534,6226; load 28/54 at 9445,6266
a  <-> q      hold device 15/83 at 9390,6120, gate tied to VSS
```

- **Bus** `cdp2_a_sK_bus`: vertical metal x 9238-9254 (16 wide), runs through the cell
  top to bottom. Contact (9244,6313) to a land; the strip from the land goes up through
  the strobe gate and ends on a buried contact (9226-9264 x 6208-6230) to the poly that
  runs up under the bus line (gate of T2, node a) and on to the right (y 6119-6139) to a
  second buried contact on the feedback land (9300-9346 x 6110-6138).
- **Strobe** `wr_r11`: one poly line, y 6314-6334, through the whole row. In each cell
  it turns up at x 9196-9219, crosses the strip at y 6266-6289 (T1's gate) and comes
  down at x 9298-9320, so the bus contact sits inside the loop. All five bits load
  together when it is high. The line runs on to the right past s7 (seen to x 10884 at
  least); at the left it reaches about x 8520. Ends not traced.
- **Loads**: both hang from the VCC land (9334-9412 x 6251-6302, contact 9378,6276).
  Load of n2: strip x 9337-9353 up to the n2 land; gate block 9322-9370 x 6198-6250,
  tied to n2 through the tab and the buried contact at 9281-9313 x 6183-6211. The same
  poly runs on under the VCC rail (x 9366-9398), right along y 6166-6189 and down at
  x 9523-9545 as the gate of q's pull-down. Load of q: strip y 6252-6280, gate block
  9418-9472 x 6203-6292 whose upper half is a contact pad; tied to q by a tab onto the q
  drain (buried contact 9476-9504 x 6203-6240) and, through the strap (contacts
  9446,6223 and 9460,6135), to the output land 9436-9490 x 6110-6160.
- **q's pull-down** has its source on the *next* slice's VSS land (x 9550-9611); s7 uses
  a sixth VSS rail at x 10744.
- **Output**: output land -> buried contact 9495-9524 x 6106-6133 -> poly strip up to a
  contact (9508,6044) -> metal x 9499-9519 going up out of the cell. q is in the same
  sense as the bus.
- **Track c** (metal x 9499-9519, y 6084-6338): sits on the q drain, with a long narrow
  contact (speckled strip in the clean shot, in all five slices: s.d. 15-18). Its lower
  end lies over the strobe line with **no contact** (plain poly colour, s.d. 4-8, in all
  five slices, against s.d. 13-27 on the three known poly contacts of the cell). A dark
  line crosses the metal at y 6073-6082 between the output contact and the track; whether
  the metal is cut there does not matter, both pieces are q.
- **Track b** (metal x 9325-9347) is a **through track with no contact in the cell**
  (second run; the first run read a contact to the n2 land at 9337,6184 and a second
  metal piece contacted to the VCC land at 9338,6276; Ambiguities 3). It runs from
  channel 1 down through the cell, looking narrow over the n2 load (y 6191-6246), on
  through channel 2 and rows B to row C. n2 is used only inside the cell.
- **Hold device** (same structure as rdp3's AMB-1, same reading adopted): the poly band
  along the cell top (y 6082-6103, contact to the VSS rail at 9182,6096, confirmed by
  the contact test) widens under the VCC rail into a block (9348-9431 x 6083-6142) over
  a diffusion strip (y 6113-6128) that joins the feedback land (node a) to the output
  land (q). Vertical colour profile under the rail: poly over field 6084-6104, dark edge
  6106-6112, brighter "poly over channel" 6114-6126, dark edge 6128-6134, a thin poly
  overhang 6136-6140. In the open gap at x 9360 the poly is continuous over y 6086-6130.
  A gate at VSS only makes sense for a depletion device: a weak q -> a feedback that
  the bus overpowers while the strobe is high. Believed, not provable from the photos:
  the implant. The strip is drawn `?D`, the device is marked `A kind=hold`.

All five instances compared (cellcheck, both layers): s5, s6, s7 identical (0-3 % bad
blocks); s3 differs only above the cell (y 5985-6105), by the channel-1 wiring below.

### Channel 1: where row A's outputs go (traced)

Each crossing of a track with a poly line was tested with the contact test
(Conventions); the contacts listed are the only ones, and each also shows as a ring in
the metal shot.

| Slice | q (track c, x 9509 + 390(K-4)) | through track b (x 9336 + 390(K-4)), net `cdp2_trk_sK` |
|---|---|---|
| s3 | up to a contact at (9118,5740) | contact (8943,6044) to **line 6042**; top end contact (8943,5782) to a poly jumper (y 5783) that runs right to a contact (9332,5782) on the metal that comes down in s4's column from above y 5700 |
| s4 | up to (9508,5740) | starts at contact (9332,5869) on **line 5870**. Line 5870 also has a contact at (9463,5869) to a short metal link up to (9463,5782), from where a poly goes up out of the region at x 9463 |
| s5 | up to (9897,5740) | contact (9725,5916) on **line 5913**; runs on up to a contact at (9725,5740) |
| s6 | up to (10287,5740) | contact (10113,5958) on **line 5956**; up to (10113,5740) |
| s7 | up to (10677,5740) | contact (10502,6000) on **line 6000** (which ends there); up to (10502,5740) |

- So every bit sends q upward, and every through track has a contact to one long poly
  line of its own (s4: 5870, s5: 5913, s6: 5956, s7: 6000, s3: 6042) and also runs on
  upward (the pads at y 5740 lead, in poly, to the right and up across y 5700: seen at
  1x only, drawn as `?P` pads). **The five long lines carry a 5-bit value that is
  distributed to the comparators**: the tracks take it down to rows B (compared with
  row C's register) and up into cdp1's rows (where row A's q also goes). Which end
  drives the lines is not established here.
- Lines 5870, 5913, 5956 run on to the right past x 10850 and all four (with 6000) to
  the left past x 8480, where they jog up-left around the s2 VSS rail (x 8377-8427)
  and continue towards x 8150 at about y 5885, 5910, 5933. Not followed.
- Line 6042 (s3's n2) runs left to a contact at (8335,6042) on a metal line going down
  into the logic left of row A.
- **Line 5826 is not connected to row A.** In s3 an extra metal line e (x 8892-8908) has
  contacts to it at (8900,5825) and to a poly pad at (8900,5739), from which a poly
  band runs right to x 9086 and (seen at 1.4x) turns up across y 5700. Below the line
  e runs on as a stub to y 6115, where it ends over field just above the node-a poly of
  s3's latch: pink field colour under the end, no green speckle, metal ends 4 px short
  of the poly band in both metal shots. Named `rax_o4`.
- The bus lines cross channel 1 without any contact and leave the region upward.

Believed: a 5-bit register written from five bus lines when its strobe is high; its
outputs q feed a comparator in the rows above (cdp1), against the same 5-bit value that
rows B compare with row C's register. Which register it is is not established.

### Row C: seven more latch bits (traced)

`findcell` with the core of the row A cell finds seven copies at dy = 1476
(scores 0.92-0.94), and `cellcheck` on the core (master y 6080-6345) gives 0-6 % bad
blocks in both layers. The cell was therefore split: `cdp2_lat` is the core (everything
below the grounded band), `cdp2_lat_top` what joins it in row A, `cdp2_lat_ctop` what
joins it in row C. Nets of row C are named `cdp2_a_c_sK_a / _n2 / _q` (cell prefix + tag).

Tested in all seven slices (contact test): track b's contact to the n2 land, the long
contact of track c on the q drain, the band's contact to the VSS rail are there; track
c's lower end over the strobe line has no contact.

- Strobe `wr_r10`: poly line y 7790-7810, loops through the seven cells as in row A.
  By colour it runs from about x 7650 to past x 10885. Ends not traced.
- Top of the cell, s3..s7 (identical, cellcheck 0-6 %; from a 7-instance composite
  `--comp cdp2_ctop`): the **output q leaves upward in poly** (x 9502-9520, no metal, no
  contact) and crosses y 7425 into row B2. **Track b** (the through track, not n2) has
  a contact at (9334,7517) to a poly that runs right under the VCC rail (y 7506-7526)
  and then up at x 9453-9474 across y 7425: this is how the track's signal reaches the
  comparator's gates. The metal of track b comes down from rows B. The bus line runs on
  up: it is the same line as row A's.
- Top of the cell, **s1 and s2 are different** (traced from two views at 2.9x, every
  crossing tested, no contacts): the outputs leave **to the left** in poly. s2's output
  poly (x 8720-8740) turns left at y 7463-7481 (line L1) and runs across s1; s1's
  (x 8329-8349) turns left at y 7504-7522 (line L2). Both run on left of x 7990, where
  they join the bundle that bends down at x 7700-7950 (not followed). In s1 the metal
  on the track-c column also runs on up past y 7395 (q of s1 in metal), and so does
  track b (`cdp2_trk_s1`, a through track: where it comes from is not followed). s2's
  track b ends at the cell top (`cdp2_trk_s2`, an unused piece). Both bus lines jog right at y 7510-7528 (s1: x 8075 -> 8118, s2: x 8465 ->
  8535) and run on up; s1's jog lies on top of L2 without a contact.
- Bus lines: in s3..s7 the row C bus line is the row A bus line (one metal line per
  slice from above y 5700 to below y 7821; `cdp2_c_sK_bus` is an alias of
  `cdp2_a_sK_bus`). The first run saw it "interrupted" inside row B2 at y 7190-7240 and
  7317-7371: there it runs over poly blocks and only looks narrow (Conventions). s1 and
  s2 have their own lines (`db_b6`, `db_b5`).

Believed: a 7-bit register of which two bits (s1, s2) are used to the left of the array
and five (s3..s7) are compared in rows B with the 5-bit value on the through tracks.
That 5 + 2 split fits **R10** (cursor start raster in bits 0-4, blink mode in bits 5-6)
better than R4, R6 or R7. A guess from widths only: the strobe `wr_r10` has not been
followed to a select line.

### Channel 2 (surveyed, tested; line 6888 traced)

13 poly lines at y 6366 ... 6888. In slices s3..s7 the per-slice metal over them is: VSS
rail, bus line (x 9243-9254), the through track b (x 9326-9346), VCC rail (x 9379-9421,
with a dark line down its middle). Every crossing of the bus line, track b and x 9415
with the 13 lines was put through the contact test in s3..s7 (first run): all plain
poly, **no contact**. So in the sliced part channel 2 only passes through.

**Line 6888 is the comparator's chain output** (`cdp2_b_s7_x`): s7's x comes up in poly
at x 10806-10817 (under a narrow metal line that is not connected to it) and joins the
line, which runs west across the whole array and turns down at x 8672-8692 to a pad with
a contact (8683,7018) to a metal line going down at x 8685 (overlay-checked). The
contact at (8548,6885) that the first run noted sits on a separate pad beside the line.

### Rows B1/B2: 5-bit comparator (traced)

Cell `cdp2_cmp`, master s4, x 9150-9640, y 6940-7480, placed at s3..s7. `cellcheck` over
x 9215-9605: 1-4 % bad blocks against the master in both layers for all four other
slices. The strip x 9120-9225 (the cell's own VSS rail) differs in s3 only: s3 has no
VSS land at y 7010-7066 (that land takes the neighbouring slice's strip, so the cell
owns the land under the rail to its *right*). The ninth rail right of s7 has the same
lands and contacts as the others (seen). 14 transistors per slice:

| Net (tag = slice) | Gate | What |
|---|---|---|
| `cdp2_b_sK_y` | NOR(q, t) | pull-down gated by t at 9466,7344 (41/21) beside the VSS tab land (contact 9506,7340); pull-down gated by q at 9553,7344 (43/20) under the *next* slice's VSS rail; load 20/57 at 9376,7334 |
| `cdp2_b_sK_ne` | NOT(q.t + y) = q XOR t | t (70/20 at 9464,7452) and q (69/19 at 9511,7452) in series from the node to the next slice's VSS land; y (32/14 at 9253,7431, under the bus line) to the own VSS land; load 30/43 at 9284,7303 |
| `cdp2_b_sK_x` | NAND(ne, p1) | ne (48/18 at 9509,7091) and p1 (48/16 at 9509,7134) in series from the VSS strip; load 22/57 at 9472,7203 |
| `cdp2_b_sK_o2` | NOT x of the slice to the left (s3: NOT `cdp2_b_cin`) | pull-down 35/20 at 9238,7212; load 32/58 at 9315,7230 |
| `cdp2_b_hl` | wired, row-long | in each slice pulled to VSS through p1 (133/23 at 9358,6984) in series with y (133/26 at 9358,7027) |

q = `cdp2_a_c_sK_q`, the row C latch output (poly up at x 9511); t = `cdp2_trk_sK`, the
through track of the column (tapped in row C's top at 9334,7517, poly up at x 9463).

    y(K)   = NOR(q(K), t(K))
    ne(K)  = q(K) XOR t(K)
    x(K)   = NAND(ne(K), p1(K))
    o2(K)  = NOT x(K-1)            o2(s3) = NOT cdp2_b_cin
    hl     : pulled low when p1(K) AND y(K) in any slice K

**Not seen: what drives `p1` and what `o2` drives** (Ambiguities 6). Every other net of
the cell is closed. Believed: p1(K) = o2(K), through a buried contact hidden where p1's
poly steps down onto the end of o2's diffusion arm (9296-9312 x 7158-7180). The trace
file does **not** contain that connection. With it:

    p1(s3)  = NOT cin              p1(K+1) = p1(K) AND ne(K)
    x(s7)   = NOT( NOT cin AND ne(s3) AND ne(s4) AND ne(s5) AND ne(s6) AND ne(s7) )
    hl      = low when NOT cin and, for some K, ne(j) for every j left of K and q(K) = t(K) = 0

Reading (believed, depends on the polarity of the through tracks, which is set where
the long lines of channel 1 are driven): if the tracks carry the complement of a value
N, then ne(K) is "bit K equal", the chain is "all bits to the left equal", y(K) is
"N has a 1 where the register has a 0", and

    x(s7) = NOT( enable AND N == register )         enable = NOT cin
    hl    = NOT( enable AND N >  register )         with s3 the most significant bit

an equality output and a greater-than output of one 5-bit comparison. If the tracks
carry N true the same hardware gives "N == NOT register" and no magnitude, which is
why the first reading is preferred.

How the nets are made (coordinates of the master):

- `hl`: one diffusion line y 6948-6966 from x 10762 (it ends under the ninth VSS rail,
  no contact there; rails cross it without contact: flat tan under the VCC rail and
  track b, s.d. 3-5) to a land left of s3's rail (8705-8752 x 6935-6975) with a contact
  (8727,6951) to a metal line x 8715-8735 that goes down to about y 7400 (Ports). In
  each slice the stack hangs from it: bar 1 (poly y 6972-6995), strip y 6998-7012, bar 2
  (y 7014-7040), VSS strip y 7048-7070, which runs on to the right under m4 to the VSS
  land under the next rail (contacts 9537,7030 and 9570,7030). Profile at x 9333: tan
  6952-6968, bright poly 6976-6990, tan 7000-7012, bright poly 7020-7032, tan 7044-7066.
- `p1`: bar 1, joined at its left end (the boxed piece 9266-9290 x 6968-6998 is bar 1 in
  the open between the bus line's protected margin and the diffusion edge at x 9290,
  which runs on down to y 7072: no buried contact) to the poly under the bus line
  (x 9240-9262, y 6972-7160, over field all the way), right along y 7142-7160, a step
  down at x 9300-9310 to y 7158-7171, under track b and the VCC rail, up at x 9398-9412,
  right along y 7126-7142: the lower gate of the NAND pair, ending in a cap at x 9547.
  No contact from the bus line, m3, track b or the VCC rail (field pink between the
  poly and the cap of o2's gate, 9230-9262 x 7163-7178, measured).
- `y`: the strip under the VCC rail (9408-9452 x 7285-7400, the line seen in it at
  x 9435 is the rail-edge artefact) with a foot (9360-9452 x 7366-7400); its land with
  m4's lower contact (9465,7273), the band y 7285-7300 to the right over the VSS tab
  land, and the piece under the next slice's VSS rail (9566-9597 x 7285-7365, no
  contact to the rail). m4 (metal x 9454-9472, continuous by profile) takes it up to bar
  2's pad (contact 9463,7016). Its gate on `ne`: poly from the load block left and down
  under track b (x 9333-9352, y 7302-7403), left along y 7385-7403, down under the bus
  line (x 9246-9260). `?`: the neck between the land and the strip (9440-9460 x
  7285-7300), the load's gate tie (9388-9406 x 7306-7360) and the join of the gate poly
  to the load block (9343-9366 x 7305-7325) each lie under a metal-gap line.
- `ne` = metal m3 (x 9280-9298) with three contacts: (9289,7096) to the pad of the poly
  line y 7082-7100 (upper gate of the NAND pair), (9289,7342) to the load's gate pad
  (9255-9308 x 7322-7365; buried contact 9226-9254 x 7336-7362 to the load's output
  land), (9288,7430) to the diffusion land (9265-9312 x 7410-7452) from which the band
  y 7442-7462 runs right under track b and the VCC rail to the series pair
  (9437-9540 x 7405-7472: ne | t | middle | q | VSS land of the next slice). m3 passes
  over o2's arm at (9292,7182) without contact (flat tan, no ring).
- `x`: diffusion below the pair (9485-9533 x 7143-7176), down into a buried-contact box
  (9506-9548 x 7186-7228: a dark-outlined box without metal in both metal shots) where
  the load's gate block ties in. The block's body (textured, 9480-9545 x 7222-7272,
  wrapped round m4's land) runs on right along y 7243-7262 under the next VSS rail and
  becomes the gate of the next slice's inverter (x 9618-9638 there). s7's runs on under
  the ninth rail and up at x 10806-10817 to channel 2's line y 6888.
- `o2`: diffusion x 9251-9279, y 7176-7262 (the dark line seen inside it at x 9262 is
  the bus line's margin artefact) with an arm to the right under m3 (to x 9305). Its
  load's gate tie is not resolved (`?B` at the block's lower left corner).
- VCC: land 9345-9435 x 7185-7260 (contact about 9395,7235) with an extension down
  (9362-9400 x 7250-7302) and left under track b (9320-9368 x 7265-7300); all four
  loads hang from it. The VCC metal is drawn narrow (x 9405-9425) for y 7255-7380; it
  is probably wider there (the load block of y is protected), which changes nothing.

### The logic left of rows B: piece `ga` (2026-11-20; traced)

Under the VSS rail (x 8030-8076 here; it widens onto row C's rail at y 7430-7470) lies a diffusion
x 7975-8105 with a source box and rail contact (8043,7008) (ring and bright centre in both metal shots,
`textmap.py 8020 6990 8066 7030 3`), a gate row y 7028-7050 across all of it (`railprof.py 8015 8065 6980
7120`: diffusion, gate, diffusion, field), and the node below (y 7050-7078).

- **The gate row** runs west to a pad (7922,7040), on which the metal x 7913-7931 from the north ends: it is
  `tc2`'s metal of `tc2_sr_q` (drawn there to y 6400), one metal down to this pad (`tl5_tracks.py v 7922
  6400 7030`: bars of 14 px or less; `textmap.py 7902 7020 7944 7062 3`).
- **The load.** East of the rail the node narrows to a neck (y 7057-7088) and widens under a poly block
  (x 8169-8205, y 7012-7110; channel about 73 wide, 37 long) to a box with two contacts ((8225,7045),
  (8222,7105)) on the wide VCC metal x 8203-8253. The block's tail runs west (y 7092-7110) and ends in a
  small heavy-outlined box (8100-8134, 7080-7104) that abuts the neck with no outline and no field
  between (review round 1: the clean shot's minimum red there is 115-140 against 85-93 on the neck's
  north edge): the load's tie, a buried contact, drawn `?B`.
- **The output.** The node's south-west tab (7975-8020, 7076-7100) holds a second such box, on which
  the east end of a poly row y 7076-7096 lies (an orange row ending at the box in both chip-2 shots,
  `cache/scratch/cdp2/gA3.png`, 9x): the output's buried contact, drawn `?B`. The row runs west to a pad
  (7662,7083) (a 35 px pad, ring, green hole: `textmap.py 7640 7060 7690 7104 3`) on which a metal from
  the north ends (port).
- **Two thin metals pass over the two boxes and do not contact them** (review round 1, confirmed): at
  each the metal keeps its width with no ring across it (`px.py row 7088 8096 8134 3 metal` against `row
  7200`; `row 7084 7968 8008 3` against `row 7130`), and the clean shot's centre is tan, not the green
  hole of a contact (`px.py pt 8116,7088,2 7988,7086,2 7662,7084,2 acid1b`: 184/165/104 and 136/148/109
  against 168/186/110 on the real pad of the same row); the boxes are 20 px, the pads of these wires
  35 px. One is `db_b6`'s metal x 8107-8121 (continuous to row C's piece at y 7395, and on north). The
  other, x 7978-8000, is a through line, `cdp2_w6845`: north it ends on a pad (7987,6845) whose poly row
  y 6836-6858 runs west to a pad (7335,6845), where a metal from the west ends (`follow.py 7300 6848 W`:
  to (6142,6847); not drawn); south it runs by two jogs (x 7950 from y 7388 to 8212) to the pad
  (7878,8315) in `cdp3`'s ground, an input of the gate cluster beside `cdp3`'s row A.

```
cdp2_w7065 = NOT tc2_sr_q            pull-down W 130; load 74/36       (marked: both ties are ?B)
```

### The logic left of rows B: piece `gl` (2026-11-20; traced)

Under the VSS rail x 8375-8425 (`railprof.py 8380 8420 7040 7420`): a top node y 7259-7292, a gate
y 7293-7316, a node with no contact, a gate y 7336-7360, and a diffusion y 7361-7419 with the rail
contact (8405,7380) (ring and centre in both chips, `textmap.py 8384 7362 8424 7400 3`). The column is
x 8365-8446. The two gate rows (y 7290-7311, y 7333-7354) end rounded just west of the diffusion at
x 8350 and run on east, in the open and under the thin metal x 8525-8540 without a pad. **Row 1** runs on
under the wide metal x 8595-8645 to a pad (8682,7300) (ring and bright centre in chip 2, a hole in the
clean shot: `textmap.py 8660 7280 8704 7322 3`), on which the metal x 8675-8695 from the north ends
(`tl5_tracks.py v 8685 7040 7290`: bars only; no metal south of the pad): the metal `cdp2` drew from the
pad (8683,7018) of the comparator chain's output line 6888, `cdp2_b_s7_x`. Row 2 runs on east into
the plate of piece `gh`.

- **Load.** The top node has a tab west (y 7255-7277; open diffusion green at x 8340-8348, tan under the
  thin metal x 8328-8345, which passes over it: the metal is dimmer there but has no ring, `px.py row
  7275 8320 8356 3 metal`), a strip under a poly plate (x 8265-8320; the strip's edges show across the
  plate at y 7251 and 7281, `px.py col 8290 7236 7330 5`) to a box with a contact (8226,7276) on the VCC
  metal (`textmap.py 8200 7240 8262 7310 4`). An L of diffusion runs from the tab down (x 8322-8345) and
  west into a heavy-outlined box (8296-8324, 7298-7322) under the plate's finger: the tie.
- **Output.** The top node has an arm east from the column (x 8444-8460, y 7252-7268; the band below
  it, y 7272-7288, is field: review round 3) into a tab (x 8455-8496) with a buried
  contact (8463-8500, 7244-7273); a poly leaves it east and turns north at x 8500-8518 (orange in the
  chip-2 stripped shot, `cache/scratch/cdp2/n3.png`, 9x), runs up to y 7170 and turns west as the row
  y 7160-7181: row 2 of the gate above (`cache/scratch/cdp2/n4.png`). Drawn to x 8445.

```
cdp2_w7272 = NOT( cdp2_b_s7_x AND cdp2_w7344 )        pull-downs W 82; load 27/54
```

The gate above is piece `gu`.

### The logic left of rows B: piece `gu` (2026-11-20; traced)

The same build as `gl`, 173 px north, under the same rail: column x 8365-8446 with the top node
y 7078-7115, row 1 y 7117-7139, a node with no contact, row 2 y 7160-7181 (the output of `gl`), and a
box with the rail contact (8413,7208). Load: the node's tab west (y 7081-7105), the strip under the
plate (edges at y 7078 and 7108 across the plate: `px.py col 8290 7056 7160 5`) on west into the VCC box
that piece `ga` drew, the L of diffusion x 8322-8337 down to y 7148 (`px.py col 8330 7076 7160 6`) and
the tie box (8296-8324, 7126-7150) under the plate's finger. Two things differ from `gl`:

- **The output does not leave east.** The arm and tab east of the column (chip-2 stripped red minus
  green 15-55 at y 7087, like `gl`'s arm: `px.py row 7087 8430 8462 4 acid`) end in a buried-contact box
  (8463-8500, 7070-7101) that has only a poly cap: a closed outline in both chip-2 shots, plain ground
  between it and the poly column at x 8520 (`cache/scratch/cdp2/u2.png`, 5x; `px.py row 7060 8500 8560 4`).
  Instead the load plate's poly runs on north as a column x 8283-8298 to a pad (8290,6997) (a 35 px
  pad, green hole in the clean shot, ring in both metal shots: `textmap.py 8270 6982 8312 7022 3`,
  `cache/scratch/cdp2/u3.png`), on which a thin metal from the north ends (`follow.py 8290 6975 N`: to
  (8290,5323)). The plate is tied to the node, so that metal carries the gate's output.
- **Row 1** runs east to x 8545 and up a poly column x 8520-8545 to a pad (8530,6955) (a real contact:
  ring and bright centre in chip 1, a hole in the clean shot; weak in chip 2). **The thin metal
  x 8525-8540 that lies lengthwise on the column does not reach the pad** (review round 4): it is
  `db_b5`'s, drawn by `rde`, and turns west at y 6999 to x 8464; between its corner and the pad there
  are 37 px without metal in both chips (`tl5_tracks.py v 8532 6930 7160`: none at y 6960-6997), open
  poly there. The pad's metal is x 8503-8517, from the north (`px.py row 6930 8494 8546 4`: metal at
  x 8506-8514), stepping onto the pad from the west. It runs north without a break (`tl5_tracks.py v
  8510 6340 6950`: bars of 14 px or less) to a pad (8508,6325) (ring, bright centre, hole: `textmap.py
  8486 6300 8530 6350 3`), the west end of a poly row y 6314-6334 that runs east to a second pad
  (8680,6324) (`textmap.py 8656 6300 8702 6346 3`; view `cache/scratch/cdp2/w2.png`) and ends there: it
  is not the strobe `wr_r11`, whose poly on the same y begins 95 px further east with field between. A
  metal from the north ends on the second pad (port; the follower runs it north past y 5481).

```
cdp2_w7092 = NOT( cdp2_w7128 AND cdp2_w7272 )        pull-downs W 81; load 27/55
```

Also drawn here: the thin metal x 8328-8345 that passes over both gates' tabs (a `?M` over each: dark for
55 and 58 px) starts on a pad (8332,6954) (ring and centre in both chips), whose poly row y 6942-6962
goes west (port). South of y 7395 it is the metal `cdp2` drew as "q of s1" on row C's track-c column.

### The logic left of rows B: piece `gh`, the load of `cdp2_b_hl` (2026-11-20; traced)

`cdp2_b_hl`'s metal (x 8715-8735, from the land at the west end of the row-long diffusion line of rows B)
ends on a contact (8712,7399); 115 px west a second contact (8598,7398) is on the wide VCC metal
x 8594-8644 (both: ring and bright centre in both metal shots, a hole in the clean shot: `textmap.py 8692
7380 8736 7420 3`, `8580 7380 8622 7418 3`). They are on one diffusion, x 8578-8745, y 7372-7420 (a closed
rounded outline in all shots; its north edge is y 7375 west of the plate and y 7383 under and east of it), and a poly plate lies across it between them (x 8632-8676 over the channel; only its head, y 7352-7378, runs on east to x 8692: review round 6): chip-2 stripped
red minus green 30-43 along y 7400 from x 8630 to 8672 and 14-25 to x 8690, about 5 on the diffusion at
both sides (`px.py row 7400 8570 8750 6 acid1b,acid`); down x 8670 the poly runs from y 7350 to 7432
with the diffusion's edge line across it at y 7380 (`px.py col 8670 7340 7446 5`). Under the VCC metal's
edge it is salmon (x 8636-8650), in the open dark red-brown. Views `cache/scratch/cdp2/x1_acid1b.png`,
`x1_metal.png`, `x1_acid.png` (6x), `o_gh.png`.

Row 2 of piece `gl` (y 7333-7354) runs east into the plate's north-west corner: one poly (orange without
a break round the corner in the chip-2 stripped shot). At the plate's north-east corner a small
heavy-outlined box (8690-8715, 7352-7372) sits on top of a tab of the line's diffusion (tan from y 7376
down, `px.py col 8705 7340 7392 4`): read as the load's tie, a buried contact, drawn `?B`. With it:

```
load of cdp2_b_hl: about 37/42, gate tied to the line        cdp2_w7344 = cdp2_b_hl
cdp2_w7272 = NOT( cdp2_b_hl AND cdp2_b_s7_x )           (marked: the tie)
cdp2_b_hl  = NOT( OR over s3..s7 of (cdp2_b_s#_p1 AND cdp2_b_s#_y) )
```

Without the tie the plate would be a pull-up gated by an undriven poly, and the line would have no load
anywhere: the tie is the only reading that makes a circuit, but the box's inside cannot be seen.

### Piece `wn`: the upper series gate's two metals, north (2026-11-20; traced, wiring only)

`cdp2_w7092`: the thin metal x 8283-8297 runs north from the pad (8290,6997) without a break
(`tl5_tracks.py v 8290 5345 6975`: bars of 14 px or less; one stretch of 40 px at y 5682-5722 fails the
test in both chips: on a view the metal is there, dimmer, with one edge bar at y 5683-5690 and no ring or
widening: `cache/scratch/cdp2/y3.png`, 7x) to a pad (8290,5327) (ring and bright centre in chip
2, a hole in the clean shot, weaker centre in chip 1: `textmap.py 8270 5306 8312 5346 3`; view
`cache/scratch/cdp2/y1.png`), whose poly row y 5316-5336 runs 30 px east and ends on a heavy-outlined box (8335-8365, 5315-5345), not
read (port at x 8336).

`cdp2_w7128`: the metal x 8676-8690 runs north from the pad (8680,6324) (`tl5_tracks.py v 8684 4910 6300`:
bars of 13 px or less; at y 5456-5510, the follower's candidate, the metal narrows beside a second
bright stripe and has no ring: `textmap.py 8664 5456 8706 5512 3`), steps east by a square jog at
y 4862-4887 (`textmap.py 8668 4838 8722 4906 4`: one metal, x 8676-8712 wide at the step) and ends on a
contact (8705,4810) (ring and bright centre in both chips, a hole in the clean shot: `textmap.py 8684
4790 8728 4832 3`) on a diffusion land (8690-8726, 4778-4838; view `cache/scratch/cdp2/y2.png`), the west end of a band that
goes on east from x 8726 with field north of y 4776 (review round 7: chip-2 stripped red minus green
21 at (8740,4800), 2 at (8740,4760)). So the
upper gate's first input is the output node of something in the logic north of the datapath there.

## Ports

| Name | Layer | Where it crosses | Direction | What |
|---|---|---|---|---|
| `cdp2_a_sK_bus` (K=3..7) = `cdp2_c_sK_bus` | metal | x 8856, 9246, 9636, 10026, 10416 at y 5700 (top edge, no contact in channel 1) and at y 7821 (down below row C: they cross channel 3 without contact in s4, s5 and enter row D; drawn to y 7821 only) | into the rows | data bus bit lines; one line per slice through rows A, B and C |
| `db_b6`, `db_b5` | metal | x 8118 and x 8535 at y 7395, going up; x 8075, 8465 at y 7821 going down | in | bus lines of row C's s1, s2 (jog at the cell top) |
| `cdp2_a_sK_q` (K=3..7) | metal, contact at y 5740 | (9118,5740), (9508,5740), (9897,5740), (10287,5740), (10677,5740); beyond the contact not traced | out, to the rows above | row A latch output, same sense as the bus |
| `cdp2_trk_s3` | metal | x 9334, y 5700 (the metal in s4's column, via the jumper y 5783) | ? | through track of s3, upper end |
| `cdp2_trk_s3` | metal | (8335,6066) going down | ? | same net, via line 6042, to the logic left of row A |
| `cdp2_trk_s4` | poly | x 9463, y 5700 going up | ? | through track of s4 (line 5870) |
| `cdp2_trk_s5`, `s6`, `s7` | poly pads | (9725,5740), (10113,5740), (10502,5740); poly on from there right and up, not traced | ? | through tracks |
| `cdp2_trk_s4` | poly | line y 5870: x 8480 (continues left) and x 10850 (continues right) | ? | the long line of the track |
| `cdp2_trk_s5` | poly | line y 5913: x 8480 and x 10850 | ? | |
| `cdp2_trk_s6` | poly | line y 5956: x 8480 and x 10850 | ? | |
| `cdp2_trk_s7` | poly | line y 6000: x 8480 west to the row address units, east past x 10518 (first read as its end: wrong) to a pad (10975,6000) | `rax_o0`, `notes/blocks/rab.md` | |
| `cdp2_trk_s1` | metal | x 8165, y 7395 going up | ? | through track of row C's s1 |
| `rax_o4` | poly | line y 5826: x 8480 and x 10850; band at y 5730 to x 9086, then up across y 5700 at x 9080 (`?`) | unknown | not connected to row A |
| `cdp2_a_c_s2_q` | poly | line L1, x 7990, y 7472, going left | out | output of row C's s2 |
| `cdp2_a_c_s1_q` | poly | line L2, x 7990, y 7513, going left | out | output of row C's s1 |
| `cdp2_a_c_s1_q` | metal | x 8338, y 7395, going up | out | same net in metal (if track c is contacted to q, Ambiguities 7) |
| `cdp2_b_hl` | metal | x 8725, y 7400 (ends there on a diffusion in the logic left of rows B; not traced) | out | comparator's wired line: low when (believed) enable and N > register |
| `cdp2_b_cin` | poly | y 7252, x 8650 (comes from the left; not followed) | in | chain input of the comparator (believed: enable, active low) |
| `cdp2_b_s7_x` | metal | x 8685, y 7300 (seen to there; goes on down into the logic left of rows B). Route: poly up at x 10811, west along channel 2's line y 6888 across the whole array, down at x 8672-8692, contact (8683,7018) | out | chain output: low when (believed) enable and N == register |
| `wr_r10` | poly | y 7800, x 10850 (east edge). Ends 46 px beyond on a contact (10894,7801) to a metal line that goes south at x 10894 (metal unbroken to y 9400 at least by profile). West end: poly colour to about x 7650, not examined | in | load strobe of row C |
| `wr_r11` | poly | y 6324, x 10850 (east edge). Ends on a contact (10896,6325) to a metal line going south at x 10896 as far as y 7715, where it must step east (to about x 10940: the same staircase cdp1 and cdp3 report) to pass row C's contact. West end: s3's cell (x 8780); the poly seen at x 8518-8690 on the same y is a separate piece (field between, x 8704-8764) | in | load strobe of row A |
| `vss` | metal | x 8794, 9184, 9574, 9964, 10354, 10744 (46 wide) at y 5960 and y 7830; x 8013, 8403 at y 7425 and 7830 | - | rails, run on both ways |
| `vcc` | metal | x 9010 + 390k (50 wide) at y 5960; x 8997 + 390k (54 wide) at y 7830; x 8229, 8619 at y 7425 | - | rails, run on both ways |
| channel 2 lines | poly | y 6366, 6410, 6456, 6498, 6542, 6584, 6626, 6672, 6756, 6802, 6844 at x 7600 and x 10850 (poly colour across the whole width by `cdp2_lines.py`; not drawn, not checked by eye outside s3..s7) | ? | pass over the array without contact in s3..s7; line 6714 is cut into pieces with contact pads at (8145,6705), (8315,6703), (8708,6703) |
| channel 3 lines | poly | y 7843, 7886, 7930, 7973, 8017: from x 7650-7800 at the left (where they turn down) to beyond x 11100 at the right; no contact seen in s4, s5; not drawn | ? | |
| (not named) | metal | x 8540-8560 from a contact (8548,6885) on a poly pad beside line 6888 (not on it) up through channel 2 to about y 5790 | ? | belongs to the logic left of the rows |

## Ambiguities

1. **Hold device** (9341-9446 x 6083-6142): see Logic. Same open question as rdp3's
   AMB-1. Between the block's right end (x 9431) and the output land (x 9436) there is
   one dark line, at the edge of the VCC rail; read as the metal-edge artefact over a
   continuous strip. If the strip did not reach the land the latch would be dynamic.
2. **Load of n2** (9320-9366 x 6188-6247): in the clean shot the strip under the gate
   block is smooth bright salmon (243,170,122) although no metal covers it on either
   chip, while q's load, also in the open, is textured orange. The geometry is drawn as
   in rdp3's cell (strip, block, gate tie); the connectivity (n2 land - strip - VCC
   land, gate tied to n2) is the only one that gives n2 a load. A thin bright line
   (x 9335-9343, y 6191-6246) shows in both metal shots over the strip. Second run: it
   is the metal of track b, which looks narrow wherever it runs over a poly block
   (Conventions); that metal is also why the block is smooth salmon (protected), so the
   colour says nothing against the load.
3. **Track b in the latch cell: contact to n2 or not** (9337,6184; and 9338,6276 on
   the VCC land). The first run read both as contacts from the speckle test, with track
   b ending at y 6190 and a second metal piece below y 6252. Second run: (a) the metal is
   one line: it only looks narrow over the n2 load, where the clean shot is protected
   over x 9320-9350 (Conventions), and it is continuous on through channel 2 and rows B
   (protected colours under it all the way; dim over the poly blocks at y 7240-7270 and
   7300-7335) to row C's track b; (b) with both contacts VCC would be tied to row C's n2;
   with the n2 contact alone, row A's n2, row C's n2 and a long line of channel 1 would
   be one net, and the pair of transistors at (9464,7452)/(9511,7452) in rows B would
   have n2 and q of the same latch on its two gates, never both high; (c) the two
   speckled patches sit exactly where the line steps onto and off the n2 load's poly
   block, and the same greenish speckle is found at (9338,7300) in rows B where the
   line steps onto a poly and no contact is possible; (d) the agent of rdp3 came to the
   same reading for the same cell (its AMB-6) and cdp1 saw no contact on the
   corresponding metal of its register cell. **Working assumption: no contact; track b
   is a through track.** Evidence for the first run's reading that remains: the speckle
   itself, s.d. 17-22 at (9337,6184) in all slices. What would settle it: where the
   long lines of channel 1 are driven (if by a gate output, the tracks cannot also be
   latch nodes).
5. **End of line e in s3** (8900,6115): see channel 1. A metal line that ends is
   expected to end on a contact; none is seen, as with track c over the strobe line.
4. Small dark boxes in the open beside the strobe gate (9270-9297 x 6244-6260 and
   9277-9298 x 6288-6313): read as bulges of the strobe poly over field. No diffusion
   there, so no device.

6. **Rows B: what drives `p1`, and what `o2` drives** (per slice). p1 (the poly of
   bar 1 and of the lower NAND gate) has no buried contact and no metal contact along
   the whole of its length as far as can be seen; o2 (the inverter of the left
   neighbour's x) drives no gate. The two nets meet at one corner: p1's poly steps down
   from y 7142-7160 to 7158-7171 at x 9300-9310, exactly at the upper right corner of
   o2's diffusion arm (9251-9305 x 7176-7194), which has no other purpose (m3 passes
   over it without contact). The corner is hidden under the dark line of the gap
   between m3 and track b in the clean shot, and the other stripped shots show only
   fringes there (5.5-9x, `cache/scratch/cdp2/b_sr2.png`, `b_corner.png`). Candidate
   readings: (a) a buried contact there, p1 = o2: the cell becomes an equality chain
   with a magnitude output (Logic); (b) no connection, and a driver of p1 not found.
   Ruled out by measurement: a tie of p1 to `hl` at the boxed left end of bar 1 (the
   diffusion edge at x 9290 runs straight past it); a link from p1 to the gate of o2's
   inverter (field between them). Working assumption: (a), **not drawn**. What would
   settle it: a sharper photo of (9300,7168), or the behaviour of the outputs.
7. **Track c and q** (first run: long contact at 9508,6222 to the q drain). The agent of
   rdp3 removed the corresponding contact in its copy of the cell (its AMB-3: in one
   slice there the track carries a through line). Not re-examined here; it matters only
   for row C's s1, whose track c metal runs on up past y 7395.
8. **Loads of rows B: three gate ties are `?`** (o2's at 9262-9282 x 7244-7262; y's at
   9388-9406 x 7306-7360 with the join of y's gate poly at 9343-9366 x 7305-7325; the
   neck of y at 9440-9460 x 7285-7300). Each lies under a metal-gap line; each is the
   only way the device seen there (a long poly block over a strip from the VCC land)
   can be a load, and the cell extracts as closed gates with them.

Run of 2026-11-20:

- **The two small boxes of `ga`** (8100-8134, 7080-7104) and (7972-8002, 7072-7100): each lies under a thin
  metal and was first drawn as a metal contact (bright in the metal shots where the metal crosses the
  box). Review round 1 compared them with nine real contacts and four known pass-overs: 20 px boxes with
  a heavy outline, tan inside, no hole at the centre, metal not widened. They are read as buried
  contacts (the load's tie; the output onto the poly row) with the metal passing over, and drawn `?B`.
  The other reading (metal contacts) would put `db_b6` on the gate of a wide pull-up and the node on the
  through line `cdp2_w6845`; the photos do not exclude it outright.
- **The tie of `cdp2_b_hl`'s load** (the box 8690-8715, 7352-7372 at the plate's north-east corner): drawn
  `?B`. It decides that row 2 of the lower series gate is `cdp2_b_hl` (and so `cdp2_w7272`'s equation).

## Not done

- **Row D** (y 8040-8450 and on below, to about y 8800: it is cdp3's untraced row A):
  not traced. Six cells, pitch 390, at s2..s7 (x 8380-10720); s2's differs at the top.
  Seen at 2.7x in s2 (x 8330-8800): VSS contacts at about (8400,8180), (8630,8180);
  textured load blocks at (8700,8170), (8700,8310), (8745,8310), (8680,8400),
  (8730,8410); horizontal poly bars y 8125-8145, 8195-8210, 8375-8390; contacts at
  (8490,8295), (8545,8440), (8540,8245). From above only the bus line, the VSS rail and
  the VCC rail of each slice reach it (the through tracks and track c stop at the foot
  of row C); two metal pieces per slice start at y 8045 (x 9280-9295 and 9325-9340 in
  s4). It is not the latch and not the comparator cell (findcell, four orientations).
  Whoever traces it needs y 8040-8800, across the cdp2/cdp3 boundary.
- **Channel 2 (y 6350-6900)**: only line 6888 (the chain output) is drawn. The other
  twelve run the whole width by colour (Ports) with no contact in s3..s7; left of
  x 8780 they are interwoven with the logic there (pads on line 6714, bends at
  x 7800-8080, y 6780-6890).
- **Channel 3 (y 7830-8030)**: five poly lines (Ports), not drawn.
- **Logic left of the rows** (x 7600-8750, y 6000-7480): one gate traced (piece `ga`, 2026-11-20); both series gates traced (pieces `gl`, `gu`); the rest (`gu`'s output metal north of the pad (8290,6997), the poly row west of the pad (8332,6954), the unit at x 8140-8260, the gate at x 8560-8700, y 7370-7410) not traced. Open ends: the through line `cdp2_w6845` west of the pad (7335,6845) (`busl` has since drawn it on west: its port at (6118,6847)); a thin metal x 8152-8166 that crosses the gate, in line with row C's track b, drawn by no one north of y 7395. Beside piece `gl`, seen and not drawn: a poly column x 8565-8590 from the north ending at y 7266; a contact pad near (8605,7395). It receives
  `cdp2_b_hl` (metal x 8725, ends about y 7400 on a diffusion) and `cdp2_b_s7_x` (metal
  x 8685, seen to y 7300), drives `cdp2_b_cin` (poly y 7252 at x 8650), takes L1/L2 (row
  C's s1, s2 outputs, y 7472/7513 at x 7990), `cdp2_trk_s3` (metal 8335,6066) and the
  metal x 8548 from (8548,6885).
- **Channel 1, left part**: lines 5826-6000 left of x 8480 (they jog at x 8300-8470 and
  go on to x < 8150); right of x 10850 they belong to whoever has that area. The poly
  from the y 5740 pads upward crosses into cdp1's rows. These lines decide the polarity
  question of the comparator (Logic) and Ambiguities 3.
- **Which registers rows A and C are**: both strobes end on the innermost track
  (x 10894) of the bundle of vertical metal lines east of the array, which is fed from
  the south and steps one track east at every tap. Following that staircase from
  y 7800 down to the select logic (sel/bd3 ports at x 14100) was not done, so neither
  row is identified. Do not take the 5 + 2 width argument for more than a guess.
- Rails are drawn for s3..s7 from y 5960 to 7830 and for s1, s2 over row C only.
- Composites: `--comp cdp2_b` (rows B, master frame 9150,6890:9590,7500), `--comp cdp2_a`
  (row A, 9150,5940:9590,6350), `--comp cdp2_ctop` (top of row C, 9150,7420:9590,7610).
- Tools written in the second run: `cdp2_cls.py` (class map; its metal mask is patchy
  where poly edges cut the metal), `cdp2_mcol.py` (is there metal along a track, with
  the clean shot's class under it: the quickest way to follow a line), `cdp2_reg.py`,
  `cdp2_cmont.py`, `cdp2_w.py`.

## Review

(Earlier runs' reviews are in the journal; this section starts with the run of 2026-11-20.)

Round 1 (full review of piece `ga`; fresh Fable 5.2 reviewer; 2026-11-20 17:37 -0600; commit bdab944; images
`cache/scratch/cdp2/review-1/`). Told to suspect: the pad of `db_b6`'s metal (buried contact or plain
pad); the join of the west poly row to the node; the thin metal x 7978-8000 over its length; the metal
x 7922; diffusion round the gate's ends; anything left out. Checked: the metal x 7922 one metal from
y 6400 to its pad; the gate row across the whole diffusion; the rail contact, none on the node; the
block across the whole strip, both box contacts on the VCC metal, both rails joined to row C's; the
metal x 8114 continuous to y 7395 and on north; the thin metal 6845-8315 one metal through both jogs
with real end pads; the rows y 6845 and y 7086 continuous. Not checked: `tc2`'s side north of y 6400;
the metals beyond the two port stubs.

Findings:

1. **Changes connections.** `C 8112,7088` and `C 7990,7084` are not metal contacts: both boxes look like
   a thin metal passing over a buried-contact box (compared with five poly pads and four thin-metal
   diffusion contacts, which all show a 35 px pad, a hole or pits, a square ring; and with four known
   pass-overs, which look like these). The east box abuts the neck. Confirmed (`px.py` rows across both
   metals at the boxes and away from them; the clean shot's centres). Fixed: both contacts removed,
   both boxes drawn `?B`; the gate is `cdp2_w7065` = NOT `tc2_sr_q`, and the two thin metals are no
   longer on it (`db_b6`; the through line renamed `cdp2_w6845`).
2. Geometry: the block's west edge is x 8169 (drawn 8160) and the diffusion's about 8149 (drawn 8140).
   Fixed.
3. Left out, no connection here: a thin metal x 8152-8166 crossing the gate (row C's track b's line).
   Recorded in Not done.

Round 1: one finding that changes connections, fixed; two geometry or notes findings.

Round 2 (fix check of round 1's fixes; fresh Fable 5.2 reviewer; 2026-11-20 17:53 -0600; against commit bdab944; images
`cache/scratch/cdp2/review-2/`). Checked at 5x or more with profiles and text maps: the east box (metal
of unchanged width, no pad, the clean shot's centre 195/180/123 with no hole, fringes in the chip-2
stripped shot against a pitted pad at the real contact (7922,7040); the tail open orange poly ending by
x 8104; one edge line only between box and neck); the south-west box (the row red-brown without a field
stripe up to the box, ending at about x 7992 inside it; metal not widened, no ring); no other pad or
contact on either thin metal between y 6990 and 7150; the row does not go on east (field, then pink
under the rail); block and tail touch only the box; nothing left unconnected; the geometry
(diffusion edge x 8148, poly edge 8169-8170). `.venv/bin/python tools/sameconn.py bdab944`: exactly the
four intended differences. One marking item, no connection change: the through line's metal is dark for
19 px over the node's box (y 7087-7105), which trap 27 wants drawn `?M` with an alias: done
(`cdp2_w6845s` aliased to `cdp2_w6845`). Outside the diff: a third thin metal (x 8154-8170, y 6714-7658)
passes over the load's strip and tail without contact; noted in the trace and in Not done.

The marking's effect, measured against the commit before it: with the `?M` stretch alone (the second
label and the alias line left out) `tools/t.sh cdp2 sameconn.py 64ffb1b` and `.venv/bin/python
tools/sameconn.py 64ffb1b` both end: connections identical. With the label and alias in, the only
differences are the two "names on one net" lines for `cdp2_w6845` / `cdp2_w6845s`.

Round 2: no findings that change a connection.

Round 3 (full review of piece `gl`; fresh Fable 5.2 reviewer; 2026-11-20 18:14 -0600; commit b67770e; images
`cache/scratch/cdp2/review-3/`). Told to suspect: the output path (box, poly east, north and west; the
strip); the thin metal x 8328-8345 over the tab and L (a real contact read as a pass-over); the plate as
one poly; the tie; contacts on the two nodes; the rows separate and without pads; anything left out.
Checked: no contact on the top or middle node; the rows across the whole column and separate (field
between them at three places), no pad under the thin metal x 8525-8540; no contact of the thin metal
x 8328-8345 (width unchanged, no ring, hole or pits); the tab joined to the column; the plate one poly
with the strip's edges at y 7252 and 7282; the tie box and the vcc contact; the output poly continuous
from the box east, north along x 8509 and west along y 7171, going nowhere else. Could not check: the
two buried contacts beyond their appearance (the output box's west outline is a double line 8 px apart);
the clean shot around the output box (inverted there, trap 28: read from the other three shots).

Findings, all geometry only:

1. The band `D 8438,7272:8520,7288` is field (chip-2 stripped red minus green -14..0, like the field
   between the rows), and the node reaches the tab by an arm x 8436-8458, y 7252-7268 that was not
   drawn; the false strip was the only join. Confirmed (`px.py row 7260 / 7280 / 7323 8430 8462 4 acid`:
   red minus green 12-57 on the arm, -14..9 on the band and on the control). Fixed: strip deleted, arm
   drawn. Same net.
2. The L is x 8322-8337 (drawn to 8345). Fixed.
3. The column's edges are x 8365 and 8446 (drawn 8358 and 8440). Fixed.
4. Left out: the two thin metals over the piece (now drawn; x 8328-8345 with a `?M` over y 7268-7326,
   where it is dark in both chips: trap 27); a poly column x 8565-8590 from the north ending at y 7266,
   not joined to row 1 (field between); a contact pad near (8605,7395). The last two are in Not done.

`tools/t.sh cdp2 sameconn.py b67770e`: connections identical. `.venv/bin/python tools/sameconn.py b67770e`:
connections identical.

Round 3: no findings that change a connection.

Round 4 (full review of piece `gu`; fresh Fable 5.2 reviewer; 2026-11-20 18:37 -0600; commit c30b7f3; images
`cache/scratch/cdp2/review-4/`). Told to suspect: the pad (8530,6955) and the metal on it; the plate's
poly north to its pad and the plate's tie; a poly leaving the east box; the thin metal over the tab; the
rows and nodes; the strip into the vcc box. Checked: both rows across the whole column, the only
contact the box's, an edge bar with field north of the top node; row 2 ending at x 8350; row 1's corner
and column; the strip into the vcc box, the L and tie like `gl`'s sample for sample; the plate's poly
continuous to the pad (8290,6997), a real contact with metal from the north only; field round the east
box, no poly leaving it; the pad (8332,6954) real, its metal starting there, a pass-over at the L. Not
checked: the far end of the north metal; the `?M` stretch's continuity.

Findings:

1. **Changes a connection.** The thin metal x 8525-8540 does not reach the pad (8530,6955): it turns
   west at y 6990-7012 (as `rde` draws `db_b5`), with open poly between its corner and the pad; the
   pad's metal is x 8503-8517 from the north. So row 1 is not `db_b5`. Confirmed (`tl5_tracks.py v 8532
   6930 7160`, `h 6999 8472 8524`, `v 8510 6340 6950`; `px.py row 6930 8494 8546 4`). Fixed: the wrong
   metal removed; the north metal, its pad (8508,6325), the poly row to the pad (8680,6324) and that
   pad's metal stub drawn; the net is `cdp2_w7128`.
2. Geometry: the output poly column is x 8286-8305 (drawn 8283-8298); the tab's lower edge is y 7098
   in the gap x 8345-8365 (drawn 7105). Fixed.

Round 4: one finding that changes a connection, fixed; geometry findings.

Added with the fixes, for the same fix check: the lower gate's row 1 is drawn on east to its pad
(8682,7300) and so joined to `cdp2_b_s7_x`. The row's placeholder name of the earlier merge, `cdp2_b_s7_x`,
is kept as an alias of `cdp2_b_s7_x` in the trace (it occurs in the coordinator's journal and master
list, which are not a tracer's to edit); the next refresh can rename it.

Round 5 (fix check of round 4's fix and of the added join; fresh Fable 5.2 reviewer; 2026-11-20 18:48 -0600; against
commit c30b7f3; images `cache/scratch/cdp2/review-5/`). Checked: the metal x 8503-8517 one straight track
from y 6340 to 6962 (bars of 8-14 px at the poly rows, no hole, the protected strip unbroken), ending on
both pads; `db_b5`'s metal stopping at its corner with about 20 px of open poly up to the pad's ring; the
poly row y 6314-6334 continuous between its pads, no contact under the metals crossing it, ending at the
pad (8680,6324) (bare ground and field east of it), that pad's metal from the north only; row 1 of `gl`
continuous from x 8540 to its pad, no contact to either crossing metal; the metal x 8675-8695 from the
pad (8683,7018) to the new pad, across `cdp2_b_cin` without contact, bare ground south of y 7324; row 2
parted from row 1 and the pad by field; the geometry. `.venv/bin/python tools/sameconn.py c30b7f3`:
exactly the expected differences. Weaker evidence, recorded: the pad (8530,6955) has no bright centre in
chip 2 and the pad (8682,7300) none in chip 1 (each has the clean shot's hole and the other chip's
centre); chip-1 debris over the metal x 8675-8695 at y 7026-7083.

Round 5: no findings.

Round 6 (full review of piece `gh`; fresh Fable 5.2 reviewer; 2026-11-20 19:05 -0600; commit 9a7c108; images
`cache/scratch/cdp2/review-6/`). Told to suspect: the tie (a buried contact at all; to which side); the
plate as one poly across the whole diffusion; the row and plate as one poly; both contacts and their
metals; which supply the wide metal is; anything left out. Checked: both contacts real; the thin metal
ending on its land (no metal y 7419-7469); the wide metal continuous y 7200-7660 and `vcc` by the older
label; the plate one poly (the dark line at x 8646-8650 is the metal's edge: the same where it crosses
row 1), across both diffusion edges, its foot an overhang going nowhere; the row and plate continuous
poly at x 8641 from y 7337 to 7376, no contact under the wide metal; the box at the head's east end in
all four shots, like the control box of piece `gl`, the diffusion's north edge line absent at
x 8704-8710 (open into the land), field north and east, nothing on the VCC side. Could not check: the
box's opening south in the chip-2 shots (dark there): `?B` stays; the rail's identity beyond the label.

Findings, geometry only:

1. The plate's east edge over the channel is x 8675 (drawn 8692); only its head runs on east into the
   box. L about 40. Fixed.
2. The diffusion's north edge under and east of the plate is y 7383 (drawn 7372); the west box's 7375.
   W about 38. Fixed.

`tools/t.sh cdp2 sameconn.py 9a7c108`: connections identical. `.venv/bin/python tools/sameconn.py 9a7c108`:
connections identical.

Round 6: no findings that change a connection.

Round 7 (full review of piece `wn`; fresh Fable 5.2 reviewer; 2026-11-20 19:21 -0600; commit 79d34e1; images
`cache/scratch/cdp2/review-7/`). Told to suspect both north ends (the metal reaching the pad; a real
contact; diffusion or poly), both metals over their length (the stretch y 5682-5722; the candidate
(8684,5481); the step), contacts at the many crossings, the pad's polys. Checked: the pad (8290,5327) a
real contact with metal from the south only and poly east only; wire 1 one metal at x 8290 throughout
(at y 5682-5722 its west edge lies on a poly L, the east half bright in both chips); the contact
(8705,4810) real and on diffusion, metal from the south only; neither arm continuing past the jog; at
(8684,5481) a box under the metal's east edge, a pass-over; no hole in the clean shot on either wire.
Not checked: most row crossings at 5x (hole scan and 1.6x views only).

Findings:

1. **A port's side** (counted as a connection by the workflow; no geometry of a net changes): the land
   of the contact (8705,4810) is the west end of a diffusion band that goes on EAST from x 8726; north
   of y 4776 is field. The port was given on the north edge. Confirmed (`px.py pt 8740,4800,3 8740,4760,3
   acid`). Fixed: the land drawn to x 8745, the port moved to the east edge.
2. Geometry: the step is a square jog y 4862-4887, not a diagonal. Fixed.
3. Geometry: wire 1's poly row is 30 px long and ends on a heavy-outlined box (8335-8365, 5315-5345).
   The port is now at x 8336 and the notes say what it meets.

Round 7: one finding on a port's side, fixed; two geometry findings.

Round 8 (fix check of round 7's fixes; fresh Fable 5.2 reviewer; 2026-11-20 19:25 -0600; against commit 79d34e1; images
`cache/scratch/cdp2/review-8/`). Checked: the band one piece from the contact's ring to x 8756, no poly
or edge line across it (row y 4808 flat over x 8728-8756 in both metal shots), its edges at y 4774-4778
and 4838-4842, field north, south and west of the land, going on east under the metal at x 8760; the
jog inside the metal in both chips, no metal at x 8725; the poly row x 8312-8331 running straight into
the west outline of a box (8332-8368, 5309-5347) that reads as a buried-contact box at the poly's end
(a gap under 10 px cannot be excluded). `.venv/bin/python tools/sameconn.py 79d34e1` and `TRACE=cdp2
.venv/bin/python tools/sameconn.py 79d34e1`: connections identical.

Round 8: no findings.

Round 9 (full review of the join with `tc1_ns3`; fresh Fable 5.2 reviewer; 2026-11-20 19:39 -0600; commit 496a9cf; images
`cache/scratch/cdp2/review-9/`). Checked: the metal continuous y 6380-7075 (bars of 8-12 px at the poly
rows, nothing in the hole scan; a dark blob in the clean shot at (7665,6467) with no ring, centre or pad
and field in the chip-2 stripped shot: a blemish); the same track throughout (row cuts every 12 px from
y 6226 to 7060: x 7656-7669 in both chips, no jog, branch or pad; in line with `tc2`'s metal from the pad
(7660,6193)); the metal reaching the pad (7662,7083) with no bare ground before the ring and nothing
south of it; extraction and `sameconn.py 30c94a3` (only the two names joined and their consequences).

Round 9: no findings.

## Correction from the coordinating session (2026-11-15)

Channel 3 (y 7830-8030) was read in the clean shot from x 7950 to x 11040 while following
its five lines from the east (`notes/blocks/bw.md`). There is no contact on any of them on
the way; the lowest (y 8006-8024, the R2 match) ends on a pad with a contact (8340,8010);
the other four turn **north** at x 7790-7930 (not down, as the Ports table above says).
Their nets: y 7840 bus line B's line, y 7882 `ck_a`, y 7926 the row counter's step `rc_stepreq_n`,
y 7971 band H1's line.

## Channel 2, five of its lines identified (coordinating session, 2026-11-16)

The lines at y 6498, 6542, 6584, 6626 and 6672 are the outputs `sl3`, `sl2`, `sl1`,
`sl4`, `sl0` of the 5-bit counter in the left array's upper rows, followed from the
west (`notes/blocks/urch.md`). They pass through this block unused and go on east to the
upper right datapath. Not drawn here yet.

## Where the long lines of channel 1 come from and go to (2026-11-16)

Traced from outside this block (`notes/blocks/ras.md`, `notes/blocks/rab.md`): the lines
at y 6000, 5956, 5913, 5870, 5826 are the outputs `rax_o0` ... `rax_o4` of the five units
that take the row address selector's outputs, bit 0 on slice s7 up to bit 4 on the line
that s3 does not tie to. East of this block each ends on a pad (x 10975-11150) and goes on
in metal to the logic in front of the RA pad drivers. So row B compares row C's register
with the row address (after the selector; polarity set by the units, not traced), and the
"through tracks" are driven from the west, not by row A.

## Which registers these are (2026-11-16)

By their load strobes, followed to the strobe tracks and joined in the extraction
(`notes/blocks/wrs.md`): **row A is R11, row C is R10.** The "guess from widths only"
above is now a traced result, subject only to the decoder's numbering of its select
lines. Row B therefore compares R10's five low bits with the row address lines `rax_o#`.

## Channel 2 west of the slices: a knot (2026-11-16)

Found while tracing two lines through it (`notes/blocks/fld.md`): at x 7860-7960 every
line of channel 2 steps down one position by nested bends (6714 to 6756, 6756 to 6802,
6802 to 6844, and by the same rule 6844 to 6888), and east of the knot the top position
(y 6714) carries other nets (a piece between pads at x 8165 and 8320; from x 8700 the line
of `wl_h0`, which ends on a pad (11060,6712)). Identified so far, east of the knot: y 6756
`rc0_n`, y 6802 `cnt_la_a_n`. The line at y 6888 that this block traced as its
comparator's chain output is, west of the knot, the line at y 6844, which goes to a pad
(7330,6845) and on west and north along x 6840 (not drawn).

## Corrections (coordinator, from the handoffs of 2026-11-20)

- Not done, "Row D ... (it is cdp3's untraced row A)": traced as `cdp3`'s row A (2026-11-20): the comparator of line g with R14 (y 8040-8490) over R14's latch row. Whether the bit lines join this block's bus lines above y 8040 was not examined.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- Not done / the coordinator's earlier correction "Whether the bit lines join this block's bus lines ...": they do (`cdp3`, 2026-11-20, firm): `cdp3`'s bit lines of columns c2-c7 are each one metal with this block's bus line of its slice (`db_b5`..`db_b0`). The latch cell draws the metal to y 7821; `cdp3` draws y 7556-8040.
- The bus line at x 8075 is `db_b6`; whether it is `cdp3`'s c1 line e (x 8076, drawn from y 9150 south) is open: the metal between is narrow and dim inside the cluster beside `cdp3`'s row A (y 8377-8768).
- A pad (7335,6845) with a metal from the west and a poly row y 6835-6858 east to a pad (7987,6845), whose metal runs down to the pad (7878,8315): an input of that cluster (seen by `cdp3`, not drawn).

## Corrections (coordinator, from the handoffs of `busl` run 16, 2026-11-21)

- `cdp2_w6845`, "the metal west of the pad (7335,6845) (follower: to (6142,6847))": drawn by `busl` (piece `hb`) to an end pad (6146,6847); the wire goes on west in poly to a pad (5668,6846) and in metal along y 6849 to about x 5339 (`lc1`'s band, undrawn).

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- The reviewer of `cdp4` run 12 notes that the chain's poly row drawn to x 10842 at about y 6880-7262 ends at
  about x 10821; the track x 10808 (`cdp4_w10808`) lies lengthwise on it with no pad (no connection).
