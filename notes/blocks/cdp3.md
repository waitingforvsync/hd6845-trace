# Central datapath, rows y 8450-11200 (`cdp3`)

Region x 7600-10850, y 8450-11200. Trace: `trace/cdp3.txt`. Helpers: `tools/cdp3_prof.py`
(runs of metal-looking or poly-looking pixels along a scan line) and `tools/cdp3_px.py`
(classifies poly / diffusion / field along a scan line from colour, in the chip-2 shots
and in the clean shot; thresholds are local to this block).

## Columns and tags

Everything is tagged by the array's **column**: `cN` starts at its wide VSS rail,
x = 7605 + 390.3 N (left edge; the rail is about 45 wide), and ends at the next rail.
There is a ninth rail, "c8", at x 10720-10768, which only ends the array.

Inside a column, from the left (x for c5, add 390.3 per column):

| x (c5) | What |
|---|---|
| 9548-9592 | VSS rail ("rail d" in the first run's wording) |
| 9628-9648 | line e: the column's bit line (`cdp3_bl_cN`) |
| 9675-9692 | line f (`cdp3_f_cN`) |
| 9722-9740 | line g, only between the row A cell and channel B (`cdp3_g_cN`) |
| 9765-9815 at the top of row C and in channel B; 9725-9769 from y 9295 down through rows D-G | VCC rail ("rail a") |
| 9808-9826 | line b: west output of the row C cell (`cdp3_cw_cN`) |
| 9848-9865 | line c: read output of the row C cell (`cdp3_cq_cN`), jogging to 9812 above row E |
| 9890-9908 | line h: node N of the column (`cdp3_n_cN`) from row E down to its channel G track |

The first run numbered "slices" `s0..s7` by a 390-px window that started at the VCC rail.
Its slice sK is column cK for the VCC rail, lines b, c, h and the row E/F transistors,
but its "lines e, f, g of sK" lie right of the next VSS rail and are in column c(K+1).
All net names and tags in the trace are now column numbers; `sK` survives only in a few
comments of the trace file, with that meaning.

Which columns each row occupies:

| Row | Columns |
|---|---|
| A (large cell, cut by the top edge) | c2..c7 |
| C (register cell) | c2..c7 |
| E (pass transistor to bus N) | c0..c7 (c0, c1 pass VSS) |
| F (pass transistor to bus N) | c0..c7 |
| H (register cell, upside down) | c0..c7 |
| lines e (bit lines) | c0..c7 in row H; c1..c7 in rows D-G; c2..c7 in row C |
| lines f | c2..c7 only |

## Status

- Traced, extracted (0 errors, no open nets) and overlay-checked:
  - row C: the register cell `cdp3_reg`, placed in c2..c7 (10 transistors each), with the
    VSS diffusion of each rail and the write line that loops through the cells;
  - row H: the same cell upside down in c0..c7, with its own write line;
  - the one gate beside row C in c0-c1 (a two-input NAND whose output is c1's line e),
    with the lines around it;
  - the three through lines to both ends, the VSS rails, the bit lines to both edges;
  - rows E and F (two pass transistors per column), their two gate lines, the tracks of
    channels D and G and the vertical metal joining them;
  - channel B: six tracks onto line g, six poly links from line f to the "x 9893" line.
- **Row A (y 8040-8830), traced** (run of 2026-11-19 22:35 -0600; 91 transistors, no uncertain item):
  six copies of `cdp4`'s comparator cell over six copies of `cdp4`'s latch cell: **R14 and its
  comparator with line g.** `g_eq_r14` = NOR of the six cells' "not equal" nodes. With every file loaded:
  2439 nets, 4541 transistors, 0 errors, 0 warnings. See "Row A" under Logic.
- **West logic, run of 2026-11-20 13:32 -0600** (Matt Godbolt's session, Claude Fable 5.2; 2 transistors and
  wiring, no uncertain item): **U1 of the gate column** (y 7940-8060), `cdp3_w8063` = NOT `cdp3_w7996` (now `lc2_w8646`), with
  its input wire (from a staircase metal of the bus field, by two poly hops) and its output wire (a metal
  x 7826-7848 to two pads whose polys go into the cluster beside row A); and **the output line of the gate
  beside row C** (the x 7880 line) drawn up to its end pad (7878,8385). See "West logic" under Logic.
- **A clock inverter west of the gate column** (run of 2026-11-20 13:55 -0600; piece `ckb`, 2 transistors and
  1,300 px of wire, no uncertain item): **`lc2_w8646` = NOT `ck_out`**, a wide inverter (pull-down W 210)
  at x 7475-7780, y 8660-8845 whose gate is the poly of `eofw`'s corner pad (7446,8732). Its output is
  U1's input (so `cdp3_w8063` = NOT `lc2_w8646`, a buffered copy of `ck_out` into the cluster beside row
  A) and, by a staircase line of the bus field, **the enable of `lc2`'s latch C**. The name `cdp3_w7996`
  of the first run is an alias of `lc2_w8646`. See "The clock inverter" under Logic.
- **The bit lines are the data bus** (run of 2026-11-20 13:40 -0600; wiring, six joins, no uncertain item):
  each of the six bit lines `cdp3_bl_c2`..`c7` runs on north of y 8040 as the same metal as `cdp2`'s bus
  line of that slice (drawn y 7556-8040): **`cdp3_bl_c2`..`c7` = `db_b5`, `db_b4`, `db_b3`, `db_b2`, `db_b1`,
  `db_b0`.** So R14's six latch cells (row A) and the register cells of rows C and H in these columns
  are written from data bus bits 5-0. See "The bit lines north of row A" under Logic.
- NOT traced: the gate cluster beside row A (x 7780-8200, y 8260-8800): surveyed, with a draft, and
  left out of the trace because five diffusion boundaries in it cannot be decided from the photos
  (Not done).

## Inventory

Rows (y), top to bottom:

| Row | y | What |
|---|---|---|
| A | about 8400-8790 (cut by the region's top edge) | large cell, six (c2..c7); x 7600-8300 holds other logic |
| B | 8790-9200 | channel: horizontal poly tracks and short poly links under vertical metal |
| C | 9195-9550 | register cell `cdp3_reg`, six (c2..c7); x 7780-8380 other logic |
| D | 9550-9810 | channel: six poly tracks, the west outputs of row C |
| E | 9828-10060 | one pass transistor per column, eight |
| F | 10088-10320 | one pass transistor per column, eight |
| G | 10300-10720 | channel: eight poly tracks in two pieces each |
| H | 10690-11050 | register cell `cdp3_reg` mirrored top to bottom, eight (c0..c7) |
| I | 11040-11200+ | next row, continues below the region |

Horizontal poly lines (y centres):

| y | Line |
|---|---|
| 8818 | `wr_r14`: poly line of channel B, y 8810-8826. East end: a pad with a metal contact at about (10893,8817), on a vertical metal line at x 10888 that comes up from the south and ends there. West end: x 8528 in c2 (field west of it to x 8440, measured). It passes 30 px below the bit-line contact of each row A cell (c5: 9636,8782); its branches into the row A cells are not traced |
| 8907 ... 9123 | channel B tracks onto line g of c7 ... c2 |
| 9533 | `cdp3_c_wr`, write line of row C: runs along y 9520-9546 and in every cell loops up (x 9581-9603 in c5), east along y 9476-9498 over the write transistor, and down again (x 9697-9719). West of c2 and east of c7 it runs straight on (seen to x 8355 and x 10900). The first run listed its two levels as separate lines "9493" and "9537". Its west end is the loop of c2 (x 8370; no poly at y 9533 west of that, measured). East end: a pad with a metal contact at about (10940,9531), on a vertical metal line at x 10935 that comes up from the south and ends there |
| 9581, 9624, 9668, 9711, 9754, 9797 | channel D tracks of c7 ... c2: from the west edge to the tap contact under line b |
| 10057, 10317 | gate lines of rows E and F |
| 10361 ... 10664 | channel G tracks of c7 ... c0, each in a west piece (to the row H cell) and an east piece (node N, to the east edge) |
| 10711 | `wr_r13`, write line of row H: the mirror image of row C's, along y 10700-10722 with a loop down to y 10746-10768 in every cell. Its west end is the loop of c0 (x 7605). It runs on east past x 10990, under five vertical metal lines (x 10803, 10848, 10888, 10935, 10975) without a contact |

## Logic

### Row C: `cdp3_reg`, a static register bit with two output buffers (traced)

Master in column c5, x 9545-9950, y 9195-9550; instances at dx -1171, -781, -390, 390,
781. Ten transistors (positions for c5):

| | Gate | Between | W/L | Where |
|---|---|---|---|---|
| write | `cdp3_c_wr` | bit line `cdp3_bl` and `x` | 72/22 | diffusion 9620-9692, write line across it at y 9476-9498; bit-line contact below at 9637,9527 |
| pull-down 1 | `x` | VSS and `q1` | 62/25 | x poly 9609-9634 over 9590-9657 x 9350-9412 |
| load 1 | `q1` | VCC and `q1` | 24/54 | strip y 9388-9412 under block C (9670-9724) |
| pull-down 2 | `q1` | `q` and next VSS | 50/19 | column 9914-9933, y 9216-9266 |
| load 2 | `q` | VCC and `q` | 33/54 | strip y 9229-9259 under block 9787-9845 |
| hold | **VSS** | `q` and `x` | 22/94 | L-shaped strip under the grounded block B (9664-9716 x 9241-9320) |
| pull-down W | `q1` | `cw` and next VSS | 79/19 | column, y 9308-9387 |
| load W | `cw` | VCC and `cw` | 26/16 | strip y 9378-9404 under poly 9782-9798 |
| pull-down R | `q1` | `cq` and next VSS | 79/19 | column, y 9415-9494 |
| load R | `cq` | VCC and `cq` | 26/16 | strip y 9448-9474 under poly 9782-9798 |

    x  = bl while cdp3_c_wr is high; otherwise held from q through the hold device
    q1 = NOT x        q = NOT q1 (= x)
    cw = NOT q1       west output, line b -> channel D track -> west edge
    cq = NOT q1       read output, line c -> row E pass transistor -> bus N

So the cell stores the bit line's value in true form and gives it out twice through
separate strong inverters (loads 26/16 against 24/54 and 33/54 inside the latch). The
hold device has its gate on VSS through a poly that does nothing else (pad under a bulge
of the VSS rail, contact at 9592,9218): as in `cdp1_reg` and `cdp2_lat`, only a depletion
device makes sense there. *Believed, not visible.*

The cell is the same circuit as cdp1's `cdp1_reg` (x, q1, q, grounded-gate hold, write
pass from a bit line 62 px right of the VSS rail centre) with the two output buffers
added; the layout is different (findcell with cdp1's master finds nothing here), and it
was traced from this block's photos only.

How the nodes are made, for checking:
- `x`: vertical poly 9609-9634 x 9292-9453. Its top lies on the west end of the hold strip
  (buried contact, drawn `?B`, see Ambiguities); its foot on a small box of diffusion
  (buried contact 9614-9644 x 9430-9458) that is the top-left corner of the write
  transistor's diffusion.
- `q1`: diffusion right of the x gate (9634-9657); an arm at y 9350-9367 to the tie box
  9666-9694 x 9348-9369; the poly over the tie widens east (to x 9752, y 9346-9371), has
  a strip down through block C (the load gate), and climbs in a Z under the VCC rail to
  "band U" (y 9285-9303, then 9275-9300) and the "column" 9914-9933 x 9202-9498 at the
  cell's right edge, where it gates the three pull-downs onto the next column's VSS
  diffusion.
- `q`: diffusion 9843-9908 x 9228-9262, tie box 9850-9892 x 9198-9226 to the load block,
  and the poly band along the top of the cell (y 9199-9222) west to a buried contact
  9676-9706 x 9197-9221 on the top of the hold strip. That band is what the first run
  took for a chain along the row: it stays inside one column cell (field at x 9664-9674).
- `cw`: diffusion "R1" 9862-9912 x 9322-9388 and the lobe west of it round the tie box
  9828-9856 x 9370-9396; the poly on the tie is the foot of the pad that line b lands on
  (contact 9817,9343), and the same poly's strip 9782-9798 x 9350-9414 is the load gate.
- `cq`: diffusion "R2" 9862-9912 x 9442-9495 with the contact of line c (9882,9470), and
  its extension west to the load; tie box 9828-9856 x 9453-9478 to the poly band
  9775-9856 x 9480-9498, whose strip 9782-9798 x 9432-9485 is the load gate. The two
  strips at x 9782-9798 are separate pieces: field at y 9418-9430 (measured).
- The pull-downs through the column are at y 9216-9266, 9308-9387, 9415-9494 (dark bars
  across the column at 9214, 9268, 9304, 9388, 9412, 9496); between them is field.

Instances: c3..c7 match the master (cellcheck 3-5 % of blocks, the differing ones in
channel D below). c2 differs only at its VSS rail: no cell to its left, so the diffusion
under the rail is one box (8386-8440 x 9350-9412, one contact) feeding pull-down 1.

*Believed:* a 6-bit register written from the data bus through the bit lines, readable
on bus N, whose outputs go west. R12 (display start, high) and R14 (cursor, high) are
the 6-bit readable registers of this chip type; which one this is depends on where the
`cdp3_cw` lines go west of x 7600, and on which select line drives `cdp3_c_wr`.

### Row H: the same register cell, eight bits (traced)

`cdp3_reg` mirrored about a horizontal line (y' = 20244 - y) in c0..c7; findcell scores
0.82-0.89 (0.75 for c0), cellcheck 3-6 % of blocks for c1..c7. The first run's "variant,
score 0.40 at offset 0,1538" was the unmirrored cell locking onto the rails. Same
equations with

    x  = bl while wr_r13 is high
    hw = NOT q1       west output: line b up to the west piece of the channel G track
    hq = NOT q1       read output: line c up to the row F pass transistor -> bus N

- The bit line is the same line e as in row C (contacts at 9637,9527 in row C and
  9637,10717 in row H, c5): the two registers share bit lines in c2..c7. In c1 the line
  runs on up past y 9500 (not followed); in c0 it was seen only inside the cell (its
  contact at 7686,10717), because above the cell a wide rail lies at x 7680-7728.
- c0 differs only at its VSS rail (one box of diffusion, 7598-7650 x 10832-10894, one
  contact), like c2 in row C. In c0 and c1 block B lies in the open: no line f there.

*Believed:* rows C and H are one 14-bit read/write register pair, high 6 bits in row C
(c2..c7) and low 8 bits in row H, i.e. R12/R13 or R14/R15, with c0, c1 of the high byte
reading 0. Bit order within a byte is not established here.

### Rows E and F (traced)

    row E, c2..c7:  pass transistor, gate cdp3_gate_e, between cdp3_cq_cN and cdp3_n_cN
    row E, c0, c1:  pass transistor, gate cdp3_gate_e, between VSS and cdp3_n_cN
    row F, c0..c7:  pass transistor, gate cdp3_gate_f, between cdp3_hq_cN (row H cell) and cdp3_n_cN

All sixteen are W/L about 190/28. `cdp3_n_cN` leaves east on its channel G track. So N is
an eight-line bus that gets the six row C bits (and 0 on c0, c1) when `cdp3_gate_e` is
high and the eight row H values when `cdp3_gate_f` is high: a read bus, with the two
unused top bits of the 6-bit register reading 0. That makes c0, c1 the two most
significant bits if the order is monotonic (not established).

### Gate beside row C, c0-c1 (traced; x 7810-8360, y 9150-9500)

Where row C has no cells there is one gate. Its pull-down chain is a diffusion
7932-8062 x 9250-9372 with two poly gates across it in series and the contact of c1's VSS
rail at the bottom (8000,9378); its load is a poly block 8116-8150 over a strip to a VCC
contact (8178,9275) under a wide VCC metal that becomes c1's VCC rail.

    out = NAND(bus_eq_r15, g_eq_r14)        extracted as cdp3_bl_c1 (see below)

- `bus_eq_r15` (gate 1, y 9279-9300): poly from the west edge along y 9450 to a contact
  (7765,9448), a metal bar east along y 9451, up the lower piece of the x 7880 line to
  the gate's pad (contact 7878,9297).
- `g_eq_r14` (gate 2, y 9328-9348): the gate poly runs down the left side and east along
  y 9423 to a contact (8335,9428) on a metal line at x 8327 that comes down from above
  y 9150 (not followed).
- Output: (1) a buried contact at the top left of the chain (7924-7958 x 9238-9271) to a
  poly strip and pad, contact 7878,9228, and up the upper piece of the x 7880 line past
  y 9150 (not followed; the two pieces of that line are separate, poly lies between the
  two contacts); (2) the load block's pad (8081-8105 x 9221-9254), on which **line e of
  c1** lands (contact 8080,9234). The pad is read as joining metal, load gate and output
  strip in one box (`?B`), which makes the gate's output and c1's line e one net.
- So, as traced, c1's line e (the "bit line" of the row H cell in c1, running on up past
  y 9150 and down to the bottom edge) is driven by this gate. What that means for the
  row H bit in c1 is open: see Ambiguities.
- `cdp3_k_a` only passes: metal at x 7835 from channel B (contact on the y 8864 poly from
  the west edge: seen by the first run, not re-checked, drawn `?`) down to a contact
  (7833,9165) on a poly line y 9168 that runs east to a contact at (8290,9165) (metal
  there not followed), on down to a contact (7835,9401), a poly cross-under below the
  metal bar of `bus_eq_r15` (no metal over it, checked at 4x in both metal shots), contact
  (7835,9490), metal west and then down at x 7772 to a contact at about (7770,10135)
  between rows E and F, which is not traced.

### West logic: U1 and the lines into the cluster beside row A (2026-11-20; traced)

**U1** (x 7296-7855, y 7940-8080) is the unit of the gate column between `eof`'s `g7700` and its three
inverters U2-U4: `eof`'s inverter cell `eof_dinv` moved by (0,-390), written out here and fitted (the
overlay `cache/scratch/cdp3/u1.png` fits; this copy's node has a poly cap on its buried contact that goes
nowhere, and its load plate's foot is the output):

```
cdp3_w8063 = NOT cdp3_w7996          pull-down W 57; load 27/56
```

- **Input** `cdp3_w7996`: the gate row y 7986-8006 runs west to a pad (7313,7995); a thin metal
  x 7309-7323 runs south from it to a pad (7313,8625) and ends on both (bare ground north of the first,
  `px.py col 7316 7950 7985 5`, and south of the second, `px.py col 7316 8636 8660 4`; `tl5_tracks.py v
  7316 8010 8610`: bars only). That pad's poly runs east and south (a column x 7393-7415, under a
  horizontal metal y 8700-8715 with no contact) to a pad (7400,8778), on which a metal from the west
  along y 8749-8765 ends (`textmap.py 7380 8762 7424 8802 3`; `px.py row 8757 7340 7400 6`). That metal is
  a line of the bus field's staircase (`follow.py 7340 8757 W`: corners (7146,8752), (7145,8714),
  (7013,8710), (7011,8628), (6843,8618), end (6843,8536)): drawn to x 7330 (port).
- **Output** `cdp3_w8063`: the plate's foot runs east to a pad (7838,8062); a metal x 7826-7848 runs
  south through a pad (7836,8430) to a pad (7838,8582), where it ends (`tl5_tracks.py v 7837 8080 8600`).
  The first pad's poly row goes east and the second's goes west and round into a row y 8675-8697: two
  gates of the cluster beside row A (ports).

**The output line of the gate beside row C** (the upper piece of the x 7880 line): one metal from
y 9150 north to a pad (7878,8385), where it ends (`tl5_tracks.py v 7879 8400 9240`: bars of 14 px or
less). The pad's poly row goes east into the cluster (port). A second metal on the same x comes from the
north and ends on a pad (7878,8315), 70 px away: another net (bare ground between,
`px.py col 7880 8330 8372 4`).

### The bit lines north of row A (2026-11-20; traced, wiring only)

`cdp2` draws each slice's bus-line metal to y 7556 at s2 and, through its latch cell placed at dy 1476, to y 7821 at s3..s7 with the contact at y 7789 (x 8465, 8855, 9246, 9636, 10026, 10416; review round 3: the lines drawn here duplicate that stretch); this file's
bit lines start at y 8040 (x 8466, 8857, 9248, 9638, 10028, 10419). Between the two each is one metal:
`tools/tl5_tracks.py v X 7560 8050` for the six x finds no stretch without metal over 21 px, and the
stretches over 14 px are the ring of the contact at y 7789 ON the line (bright centre and ring in both metal shots; at (8466,7604) and y 7700-7730 the dark stretches have no hole in the clean shot and are not breaks: review round 3), `textmap.py 8836 7754 8880 7824 3`, `8444 7574 8490 7620 3`): taps of
`cdp2`'s channel 3, which are that package's and are not drawn here. View `cache/scratch/cdp3/bl3.png`
(c3, 3.6x). The names are joined by `@alias` (the bus names are canonical):

| bit line | x | is |
|---|---|---|
| `cdp3_bl_c2` | 8466 | `db_b5` |
| `cdp3_bl_c3` | 8857 | `cdp2_c_s3_bus` = `db_b4` |
| `cdp3_bl_c4` | 9248 | `cdp2_c_s4_bus` = `db_b3` |
| `cdp3_bl_c5` | 9638 | `cdp2_c_s5_bus` = `db_b2` |
| `cdp3_bl_c6` | 10028 | `cdp2_c_s6_bus` = `db_b1` |
| `cdp3_bl_c7` | 10419 | `cdp2_c_s7_bus` = `db_b0` |

No gate's equation changes: six bus equations (`db_b#` = NOT `dl#_q_n`) gain the alias, and 108 transistor
terminals in this package now read `db_b#`. **Not joined**: c1's line e (x 8076). Its metal north of
y 9150 fails the metal test on long stretches inside the cluster beside row A (y 8377-8768, narrow and
dim); `cdp2` names the bus line at x 8075 `db_b6`. If they are one metal, the gate beside row C has
`db_b6` on its load's pad (the `?B` there): not established.

### The clock inverter (piece `ckb`, 2026-11-20; traced)

Under the VSS rail (x 7552-7645 at this height) and the wide VCC metal (x 7682-7770) lies one diffusion,
x 7547-7712, y 8660-8770 (`railprof.py 7560 7615 8640 8810`, `7685 7710 8640 8860`). The poly of `eofw`'s
corner pad (7446,8732), which is `ck_out`, enters from the west along y 8722-8745, turns north at
x 7625-7648 and east along y 8678-8698 to its end at x 7722: it parts the top-left of the diffusion (two
rail contacts, (7572,8680) and (7592,8688)) from the rest, the output node. East of the rail a second
poly (y 8772-8802) crosses the node's south end down to a diffusion that runs east to a box with a
contact (7755,8818) on the VCC metal: the load, its gate tied to the node by a tail west and a buried
contact (7598-7626, 8768-8798) on a tab. The thin outlined strip at x 7655-7672 between the two metals
is the usual artefact of a gap between metals (layers notes), not layout.

```
lc2_w8646 = NOT ck_out            pull-down W 210 (the poly's whole path across the diffusion); load 70/29
```

The node leaves west by a neck (y 8750-8764: a tab bounded by edge lines at y 8747 and 8765 in both
chip-2 shots, `cache/scratch/cdp3/w3.png`, 9x) into a buried contact (7495-7533, 8762-8792) under the end
of a poly row y 8768-8790, which runs west under the track x 7455-7475 (poly colours without a break,
`px.py row 8778 7400 7556 8`) onto the pad (7400,8778): the pad of U1's input wire. So the two pieces of
this run are one circuit: this inverter drives U1 and the metal that ends on that pad.

That metal is a line of the bus field's staircase. From the pad it runs west along y 8757, north at
x 7146, west along y 8713, north at x 7012, west along y 8621, north at x 6843, west along y 8541, north
at x 6667, west along y 8452 and north at x 6467 onto the metal that `lc2` draws as the branch of latch
C's enable (`M 6168,8301 x6450`). Every piece passes the two-chip metal test with bars of 14 px or less
(`tl5_tracks.py` on the ten pieces: the bars are the edges of the poly columns under the staircase). At
(6843,8533) the follower stops on such a bar; the metal turns west there (`px.py row 8541 6790 6850 4`:
metal at x 6794-6802, 6814-6830, 6838-6848 with two 8 px bars; `cache/scratch/cdp3/st2.png`, 6x).
With every package loaded the join gives:

```
lc2_w8822 = NOT((lc2_w8646 & tl3_w3982) | lc2_w8688)        lc2's latch C, enabled while ck_out is low
lc2_w8688 = NOT((lc2_w8646 & lc2_w9005) | lc2_w8822 | rst_c)
cdp3_w8063 = NOT lc2_w8646                                  U1
```

### Channel B (traced, wiring only)

- Six poly tracks from the west edge (y 8907 ... 9123) each end at a contact on line g of
  one column (c7 ... c2). Line g comes down from the row A cell and **ends at that
  contact** (checked in all six: no metal below it; the first run had drawn it down to
  y 9200). So each row A cell gets one line from the west.
- Six poly links join line f of a column (contact at x 9681 in c5) to the "x 9893" line of
  the same column, which comes down from the row A cell and ends at the link (links at
  y 8862 for c2, c3, c5, c6 and at y 9144 for c4, c7). Line f then runs down through the
  row C cell without a contact and on to the bottom edge.

### Row A: R14's latch row and the comparator of line g with R14 (2026-11-19; traced)

Row A is, in each of c2..c7, the cell pair of `cdp4`'s row R1, 3015 px north (`tools/findcell.py 8370
11060 8790 11490` and `... 8370 11495 8790 11845`: six hits each at dy -3015/-3016, scores 0.83-0.88; c2's
comparator 0.72, see below). It is placed from `cdp4`'s cells (`@requires cdp4`), and every copy was
checked with `tools/cellcheck.py`. The gates in full are in `notes/blocks/cdp4.md` ("Row R1 upper", "Row
C latch"); with this row's names:

    cdp4_la_c#_a   : storage node, written from the bit line cdp3_bl_c# while wr_r14 is high
    cdp4_la_c#_n2  = NOT cdp4_la_c#_a
    cdp4_la_c#_q   = NOT cdp4_la_c#_n2
    cdp3_f_c#      = NOT cdp4_la_c#_n2            (the buffered output: R14 as read, cdp4's selector source a)
    cdp4_xr_c#_nor = NOR(cdp3_g_c#, cdp4_la_c#_q)
    cdp4_xr_c#_ne  = NOT((cdp3_g_c# AND cdp4_la_c#_q) OR cdp4_xr_c#_nor)        = cdp3_g_c# XOR cdp4_la_c#_q
    g_eq_r14       = NOR(cdp4_xr_c2_ne, ..., cdp4_xr_c7_ne)                     high when line g equals R14's q in all six columns

- **Latch row** (y 8490-8830): the latch cell upside down, strobe `wr_r14` (the poly y 8818 already drawn),
  data from the bit line (line e; contact (8466+dx, 8794)), buffered output by the land's contact
  (8712+dx, 8757) onto the metal x 8722 (the "x 9500 line") and the link poly to line f. So **row A is
  R14** (firm: `wr_r14` by `regs`), and line f is R14's buffered output.
- **Comparator row** (y 8040-8490): the bus-tap metal of the cell (x 8556+dx, top end y 8047) is line g,
  which the tracks of channel B bring from the west. Line f's metal runs on up through the row as a stub
  (top end y 8052, no contact above the link).
- **c2** has the short pull-down and, east of it, the match line's load, exactly as `cdp4`'s slice s0
  (hand-drawn, `cdp4`'s items moved by +782,-3015): poly A x 8407-8604 with its leg on field, VCC
  contact (8632,8175) under a pad of the rail, load gate x 8685-8727 with a buried contact on the line at
  its head, and the same tab of the line under the top end of the tap track (8548-8570, 8059-8099; no
  contact read, as `cdp4`'s Ambiguity 12).
- **West end of the match line**: the band ends in a framed box (8328-8368, 8098-8145) read as a buried
  contact; a poly runs south from it (x 8333-8350) to a pad (8323-8357, 8192-8227) whose contact
  (8334,8209) starts the thin metal x 8336. `tools/follow.py 8330 8260 S` follows that metal to (8336,9430),
  the contact of the NAND's gate 2: **the match line is `g_eq_r14`**. The one contact candidate on the way
  (8336,9090) is a crossing (`tools/textmap.py 8318 9072 8354 9110 3`: no hole).
- **East end**: the line stops under the ninth VSS rail; c7's comparator and latch take VSS from lands
  under that rail (contacts (10745,8443), (10745,8637)).

So the NAND beside row C is NAND(`bus_eq_r15`, `g_eq_r14`) = NOT((bus lines = R15) AND (line g = R14)): with
the bus lines and line g believed to be the low eight and high six address bits, **the cursor match,
active low** (believed for what the lines are; the gates are firm).

## Ports

West edge, x 7600 (all poly, all continue west beyond x 7540):

| Name | y | Direction | What |
|---|---|---|---|
| cdp3_g_c7 .. cdp3_g_c2 | 8907, 8950, 8994, 9037, 9080, 9123 | ? | one line into each row A cell |
| cdp3_k_a | 8864 | ? | poly to the x 7835 metal (first run's observation, drawn `?`); passes the gate beside row C and ends at about (7770,10135). The y 9168 poly on the same net starts at x 7820, not at the west edge |
| bus_eq_r15 | 9450 | in | gate 1 of the NAND beside row C |
| cdp3_cw_c7 .. cdp3_cw_c2 | 9581, 9624, 9668, 9711, 9754, 9797 | out | row C register outputs (true), each from a 26/16 load |
| cdp3_gate_e | 10057 | in | read row C onto N |
| cdp3_gate_f | 10317 | in | read row H onto N |
| cdp3_hw_c7 .. cdp3_hw_c0 | 10361, 10404, 10447, 10490, 10535, 10577, 10621, 10664 | out | row H register outputs (true), each from a 26/16 load |

East edge, x 10850 (poly):

| Name | y | What |
|---|---|---|
| cdp3_n_c7 .. cdp3_n_c0 | 10361, 10404, 10447, 10490, 10535, 10577, 10621, 10664 | bus N. c7's track ends at a metal contact at about 10855,10355 and c6's at about 10900,10400, each on a vertical metal line that comes down from the north with a diagonal jog at y 10250-10330 (seen at 0.85x); the other six run on east at least to x 10960 |
| wr_r14 | 8818 | in (believed): line into the row A cells; ends 43 px east of the edge on a contact to the vertical metal line x 10888 |
| cdp3_c_wr | 9533 | in: write line of row C; ends 90 px east of the edge on a contact to the vertical metal line x 10935 |
| wr_r13 | 10711 | in: write line of row H; runs on east past x 10990 |

The vertical metal lines east of the region (x 10803, 10848, 10888, 10935, 10975, seen at
y 8780-8860, 9490-9575, 10670-10750) are not in this block: 10888 and 10935 end at the
contacts above, coming from the south; 10803 and 10848 run on north past y 8780.

Top edge (y 8450) and bottom edge (y 11200), per column (x for c5):

| Line | x | What |
|---|---|---|
| VSS rail | 9548-9596 | contacts at 9568,8437 and 9568,8500 (row A), 9570,11200 |
| cdp3_bl_cN | 9628-9648 | bit line. Top edge: c2..c7 (through channel B; through the row A cells drawn `?`, each with a contact at about y 8782 that is not drawn). c1 runs on up past y 9500, not followed; c0 seen only from y 10684. Bottom edge: c0..c7, drawn `?` through row I (metal present all the way, profile) |
| cdp3_f_cN (N 2..7) | 9675-9692 | from the row A cell (via the link in channel B); no contact in rows C-H; drawn `?` through row I to the bottom edge |
| VCC rail | 9765-9815 at the top, 9770-9815 at the bottom | |

Into parts not yet traced (the labels sit on the stubs):

| Name | Layer | Where | To |
|---|---|---|---|
| g_eq_r14 | metal | x 8327, y 9150, going up | gate 2 of the NAND; source above not followed |
| cdp3_bl_c1 | metal | x 7880, y 9150, going up (output of the NAND) and x 8076, y 9150, going up (line e of c1) | logic beside row A |
| cdp3_k_a | metal | stub at (8290,9150-9178); and x 7772, y 10150 | not followed |
| cdp3_g_cN (N 2..7) | metal | x 9731 + 390 (N-5), y 8790 | row A cell |
| x 9893 line (same net as cdp3_f_cN) | metal | x 9893 + 390 (N-5), y 8790 | row A cell |

## Ambiguities

- **Top of the x poly** (9607-9637 x 9291-9319 in c5, drawn `?B`). The hold strip comes
  out of block B's left edge as a pale strip (9622-9664 x 9296-9314) and ends under the
  top of the x poly, where the clean shot shows only a dark blob in the gap between the
  VSS rail and line e. Read as a buried contact (strip to x), as in `cdp1_reg`. The
  alternative, the strip passing under the poly as a transistor, leads nowhere: nothing
  is west of the poly but the VSS rail's field.
- **Joint between the west buffer's tie and R1** (9855-9868 x 9374-9390, drawn `?D`). The
  tie box's right outline and R1's left outline merge into one dark line there in both
  stripped shots. Without the joint R1 would be a pull-down with nothing on it and the
  load would have no pull-down. The read buffer below, same layout, shows its joint
  plainly (continuous tan at y 9453-9462).
- **Line f over block B.** In the metal shots line f looks slightly wider at 9673-9691 x
  9287-9312 (between the two edges of the strip under it), in all six cells. Read as no
  contact: the line is no wider than elsewhere, and the clean shot shows unbroken poly
  below. A contact there would put line f on the grounded poly.
- **Pad of the NAND's load** (8079-8107 x 9241-9258, `?B`). In the clean shot the pad is a
  pale box with a heavy outline directly above the output strip, with a thin dark line
  between them at 1.85x; line e's contact ring sits on it. Readings: (a) one box joining
  metal, poly and diffusion (adopted: a depletion load needs its gate on its output, and
  no other tie is visible); (b) metal to poly only, the load being a pull-up gated by
  line e. Needs a 5x look at 8060-8110 x 9215-9280.
- **A gate driving a bit line.** With reading (a) c1's line e is the NAND's output, yet
  the same line is the bit line of the row H register cell in c1 and runs on south. Either
  line e of c0/c1 is not a data-bus bit line below (the row H bits in c0, c1 would then
  be loaded from logic), or it is cut somewhere between y 9560 and 10690 (seen unbroken
  only at 0.95x), or the reading is wrong. Not resolved; the c2..c7 bit lines are not
  affected.
- Rail identity. The rails are labelled from structure (loads hang from "rail a", pull-
  downs end on "rail d") and from their x matching the VSS / VCC rails that `cdp1`
  followed to the VSS pad plane at y 4530. Not followed through cdp2 here.
- The gate lines' east ends were seen at 0.85x only (row E's poly visible to about
  x 10690; row F's not visible east of c7's gate).
- Neighbours: `cdp4` (below) tags the column whose VSS rail is at x 8405 as its s2, so its
  sK is column c(K) here; `cdp2` (above) uses the same numbering as cdp4.

- **A tab of row A's match line under the top end of c2's tap track**, (8548-8570, 8059-8106), as in
  `cdp4`'s slice s0 (its Ambiguity 12). Both metal shots show a bright centre about 12-15 px across in a
  dark ring at (8557,8068); c3's track end is plain. Neither stripped shot shows a pit there (clean shot
  200/174/135, flat), while the known contacts (8712,8757) and (8632,8178) do. Read as no contact by the
  tracer and the reviewer; a contact would short `cdp3_g_c2` to `g_eq_r14`. The tab is drawn, no contact.

## Not done

- **The gate cluster beside row A** (x 7780-8200, y 8260-8800; run of 2026-11-20): surveyed at 5-9x and
  drafted, **not in the trace**. Survey and draft: `cache/scratch/cdp3/survey.md`, `draft-ku.txt`; views
  `ka_*`, `kb_*`, `cm_a`, `cm_b`, `k1_*`, `kB`, `kC1`-`kC3`, `kL1`, `kL2`, `j1`-`j5`. What is read:
  - Three gates on the rail x 7986-8030 (`vss`: contacts (7998,8338), (7995,8562), (7992,8788)) with
    three loads east of it under a wide metal x 8160-8200 (boxes with contacts (8187,8362), (8185,8480),
    (8173,8575)); each load's plate has a buried contact to its node.
  - Their gate polys: the row of the pad (7878,8385) (the gate beside row C's output), which crosses the
    rail's diffusion at y 8383-8405 and turns north east of the rail to cross a strip y 8335-8375; the
    row of U1's output (pad (7836,8430)) at y 8428-8452; an L from the pad (7878,8315) to a row
    y 8502-8525 over two fingers (x 7932-7966, x 8003-8040), which runs on east and south into the third
    load's plate; U1's second row y 8675-8697; a row y 8730-8752 from a pad (7945,8750); a row
    y 8645-8668 from a pad (8118,8660) east of the rail.
  - A metal x 7927-7957 from a pad (7940,8300) (the poly of the first load's plate) contacts two
    diffusions, at (7937,8474) and (7935,8648), and goes on.
  - **Undecided**: five boundaries between diffusions lie in the 25 px gaps between two metals (x 7960-7985
    and x 8040-8060), where the clean shot shows a dark bar whether the diffusion is continuous or two
    edges meet, and the chip-2 stripped shot is fringes: the contact box (7930-7966, 8457-8498) against
    the node east of it; the box (7930-7968, 8527-8560) against the rail box (7985-8035, 8537-8592); the
    stem (7945-7968, 8660-8672) against the arm x 7985-8010; the box (7945-7968, 8700-8722) against the
    node east of it; the band y 8612-8632 (x 7985-8045) against the diffusion x 8060-8095. With all five
    joined the third gate would gate its own node; with none joined two transistors hang on closed
    boxes. Which are joined decides whether there are two or three separate gate outputs. One reading
    that makes sense throughout (second and fourth joined, first separate): `P` = NOT(row C gate's
    output OR `A` OR `cdp3_w8063` AND row y 8740), `N` = NOT(`A` OR row C gate's output AND `cdp3_w8063`),
    `A` = the third node. Believed at most.
  - **Review round 2's independent reading** (2026-11-20): all five boundaries are one diffusion each
    (controls in the same gap: field shows a green strip at x 7968-7974 in the clean shot and an edge
    line in both metal shots; two diffusions, at the box (7935,8648), show the box's edge and green
    field; the five pairs show neither). And: the row y 8502-8525 may not be continuous under the rail at
    x 7984-8005 (pink in the clean shot there, an orange patch inside a dark ring in both metal
    shots). If it is two polys, the west one (from the pad (7878,8315)) and the east one (into the
    third load's plate) are different nets, which may remove the contradiction. Start there.
  - **Checked 2026-11-20 13:52: the row is two polys.** At y 8502-8525 the west poly (from the pad
    (7878,8315)) ends at about x 7977 and the east poly starts at about x 7995: between them the clean
    shot is pink (field under metal) and chip 2's metal shot grey bare ground, in a notch of the rail
    (`cache/scratch/cdp3/j6.png`, 9x, three shots; `textmap.py 7960 8490 8050 8536 3`). The east poly
    crosses the east finger (x 8003-8040) and runs on east and south (x 8058-8072, y 8505-8545) into the
    third load's plate. With all five boundaries joined this still leaves a transistor whose gate and
    drain are one net (the east finger: gate = the third load's plate, which is tied to its node, which
    by boundaries (e), (c) and the metal x 7927-7957 is the node above the finger). So one of these is
    still misread: the two contacts of that metal ((7937,8474), (7935,8648)), the plates' ties, or a
    boundary. Not resolved; nothing of the cluster is drawn.
  - Also there and not drawn: two thin metals at x 8050-8058 and x 8076-8084 (narrow, in pieces), the
    metal from the pad (8118,8448) south, the metal from the north onto the pad (7878,8315) (follower:
    a corner (7989,7386), end (7986,6844)).
- (Done 2026-11-19: row A, y 8040-8830, and what the notes called row I, which is `cdp4`'s comparator
  row, traced there in its run 3. The items below on the row A cell and row I are superseded by "Row A"
  under Logic.) Left from row A: (done 2026-11-20: the bit lines join `cdp2`'s bus lines; they are `db_b5`..`db_b0`;
  c1's line e at x 8076 is not followed north of y 9150); the logic beside row A (x 7600-8300, y 8040-8800), through which `g_eq_r14`'s
  thin metal only passes.

- Row A cell (c2..c7, y about 8400-8790, cut by the top edge): not a copy of `cdp3_reg` in
  any orientation (findcell finds nothing above 0.5 in y 8250-8900). Not traced.
- Row I (y 11050-11200+): not a copy of `cdp3_reg` (nothing above 0.5 in y 10950-11600),
  nor of cdp2's latch. It is the top of the tall cell row that `cdp4` lists as its row R1
  (y about 11100-11800), so it belongs with that block; lines e and f run into it.
- The logic beside row A, x 7600-8400, y 8440-8800 (contacts at about 7840,8480;
  7880,8480; 7790,8560; 7850,8600; 7960,8640; 8060,8620; 8140,8590), and where the lines
  from the gate beside row C go in it (x 7880, 8076, 8327 and 8290 at y 9150).
- What is known of the row A cell (c5 coordinates, from a 1.5x view): spans y about
  8330-8790 and probably further up (cdp2 calls y 7980-8450 its row D); contacts on the
  VSS rail at 9568,8437 / 9568,8510 / 9570,8635 / 9565,8780; a bit-line contact on a
  diffusion box 9615-9680 x 8752-8812 (9636,8782), 30 px above `wr_r14`; other metal
  contacts at about 9716,8427 / 9838,8537 / 9828,8622 / 9760,8687 / 9872,8750; line g
  (from the west, channel B) and the x 9893 line (to line f, going south to cdp4) end
  in it. *Believed:* a second 6-bit register on the same bit lines, with more logic per
  bit (comparator?), whose per-bit output is line f.
- The VCC rails are drawn in channel B, in the register rows and between them (c2..c7);
  not through rows A and I, and not for c0, c1 in rows D-G (next item).
- c0 in rows D-G is not standard: a wide rail at x 7680-7728 from the top of row D to
  y 10150, which jogs right (y 10150-10400, contacts at about 7770,10135 and 7685,10280)
  to the usual VCC position x 7775-7822 above row H; a thin line at x 7772 comes down from
  the logic above and ends at the 7770,10135 contact. c1's VCC rail starts at y 9750 with
  a tab to x 8255; above it a narrower line at x 8215-8255 comes down from the logic.

## Tools and method notes

- The clean shot here: poly salmon under metal and dark red textured in the open;
  diffusion flat tan under metal and mauve-pink in the open; field pink under metal and
  khaki in the open. In a gap between two metal lines only a strip a few px wide is
  "open", so poly shows there as a dark red bar and field as a green one with a dark
  centre (the "rings" at 9660,9333 and 9705,9333 are field).
- The median composite over the six cells (`composite.py`, name `cdp3_col`, frame of
  column c5) at 4x in the clean shot was the most useful single view. Above 4x nothing
  more is resolved.
- `tools/cdp3_px.py` (colour classes along a scan line) settled several things a view did
  not: that the strips at x 9782-9798 are two pieces, where the pull-downs cross the
  column, that the stair between R1 and R2 is field. Letters next to an edge are noise.
- `tools/cdp3_strips.py` cuts a long horizontal strip into pieces and stacks them: one
  picture follows a through line across the whole array.
- `findcell.py` must be run without `--orient` restrictions: row H is the row C cell
  mirrored top to bottom, which the first run's search (two orientations) missed.
- `tools/cdp3_prof.py --mode metal` needs `--thr 150`; with a lower threshold plain field
  counts as metal.

## Corrections (coordinator, from the handoffs of 2026-11-19, second batch)

- The channel G west pieces (`cdp3_hw_c7` .. `cdp3_hw_c0`, x 7600, y 10361 .. 10664) have their far
  ends (`busl`, piece `h8`): each runs across the left bus field to a diffusion row of the left array at
  x 4780, y 11338, 11815, 12291, 12768, 13247, 13725, 14202, 14894 (c7 northernmost).
- The top unit of the gate column x 7460-7800 (y 7585-7860) is drawn by `eof` (piece `g7700`):
  `tc2_r5589` = NOT(`lc1_w7170` AND (`rst_ck` OR `tc2_sr_g`)) in the names `eofw` joined it to.
- Two wires of `tc2_sr_g` enter the gate column from a corner pad with a contact (7446,8732) (`eofw`): a
  poly east at (7490, 8722-8745) and a metal south at (7458-7474, 8800). Not followed.
- **Trace corrected** (geometry only): column 0's VSS rail `M 7623,8450 y11200 w=46` began 106 px too far
  north. At y 8500 the ground at x 7612-7660 is bare in both metal shots (163/135/85, 139/113/74) and the
  rail is the metal x 7552-7600; at x 7623 the metal begins at y 8556-8560 (`tools/px.py row 8500 7540
  7660 8 metal,metal1`, `col 7623 8500 8590 8 metal,metal1`; seen independently by `eof`'s run 5 and by
  `eofw`'s tracer). Now `M 7623,8556 y11200 w=46`; `tools/sameconn.py`: connections identical. The rail
  north of there is the metal x 7552-7598, drawn by `eof` for y 7585-7860 and by nobody between.

## Corrections (coordinator, from the handoffs of 2026-11-19, third batch)

- Ports, "`cdp3_g_c7` .. `cdp3_g_c2` | 8907 .. 9123 | ? | one line into each row A cell": the other end of
  each is traced (`busl`, piece `d6`): a row-end pad just west of x 7600 (x 7336-7553), a track down the
  left bus field, and `bc1`'s row D data line of the same order (c2 to `cdp3_g_c2`). So line g is what
  `cdp4`'s 6-bit latch row D latches on `cdp4_ld6`; believed an output of the row A cell, not "a line in
  from the west".
- `bus_eq_r15` ("in", gate 1 of the NAND beside row C): its row y 9450 ends west on a pad (7554,9450)
  whose metal track runs south on x 7555 to a contact (7555,11118) on a diffusion pad; the diffusion
  runs east under column 0's VSS rail at y 11092-11127 (`busl`, piece `kb`; not drawn in `cdp3`). That
  diffusion is the net's only possible driver drawn so far.
- The metal south of `eofw`'s corner pad (7446,8732) does not enter the gate column: it is `tc2_sr_g`'s
  branch down the left bus field (`busl`, piece `sr`). The pad's poly on east is still open.

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- Row H's write line ("runs on east past x 10990 ... without a contact") ends on a pad with a metal contact at (11243,10705) on the write strobe of R13 (`regs` run 1, firm): **row H is R13**. The line into row A's six large cells is R14's write strobe (firm), and row C's write line is R12's (marked: one `?M` on the way).
- The gate column x 7460-7800 ("about six units with loads"): below `eof`'s `g7700` there are four inverters at a pitch of 130 (U1 y 7940-8060, U2, U3, U4); U2-U4 are drawn by `eof` (run 12, piece `d3982`: three inverters in series, `tl3_w3982` = NOT NOT NOT `lc1_w7928`); U1 is not drawn.
- `bus_eq_r15` comes from a diffusion band at (7600, 11092-11127) under column 0's VSS rail (`busl` run 6), undrawn here.
- `cdp3_gate_e` and `cdp3_gate_f` enter from the west on pads (6730,10055) and (6730,10317), each with a track from the south (`regs` run 3); believed the read selects of R12 and R13 (two open joins through the left bus field): rows E and F are then the read gates of R12 and R13.

## Review

### Row A (run of 2026-11-19)

Round 1 (full review, 2026-11-19 22:51 -0600; a fresh Fable reviewer, images in `cache/scratch/cdp3/review-1/`;
commit before the round e1b2cc7). Piece: row A, x 8280-10800, y 8030-8840, and the thin metal x 8336 to
y 9160. Told to suspect: the west end (box, poly, pad, the metal's start and run), the latch gates' poly
being `wr_r14`, the joins at y 8765-8795, line f's and the bit line's lack of contacts, c2's hand-drawn
part and its tab, c2's copy, the east end, anything left out. Checked at 4x or more in up to four shots
with profiles and text maps: the west end (pad contact with ring and bright centre in both chips, no metal
north of the pad, the metal continuous to (8336,9430), the crossing at y 9090 a poly-row edge); the copies
(c3..c7 at most 4 % bad blocks in three shots, c2's all in the hand-drawn part and the west rail edge);
c2's leg on field, load, head box, VCC contact; the metals' top ends and joins; the east end's lands and
contacts; the extraction (91 transistors, equations as claimed).

- Finding 1, **geometry only**: `wr_r14`'s poly (an older line, `P 8528,8818 x10850`) is not straight:
  under every bit line and line f metal there is field at y 8812-8830; the band is joined through each
  latch cell's loop. Confirmed (`tools/px.py row 8820 8826 8930 8 acid1b,acid`: pink 201/117/115 at
  x 8850-8866 and 8898-8906; view `strobe.png`). Redrawn as six segments, with the dead-end stub under c2's
  VSS rail.
- Finding 2, **geometry only**: the tab joined the pocket by a 2 px overlap. Lengthened to y 8106.
- Finding 3, **geometry only**: the six older `?M` bit-line pieces (y 8450-8795) doubled the firm metals.
  Removed.
- Ambiguity recorded: the tab under c2's tap track (no contact read by both).
- Not checked by the reviewer: c4..c7 individually above 1x (composite and `cellcheck.py` only); the
  masters' internals (reviewed in `cdp4`).

`tools/t.sh cdp3 sameconn.py e1b2cc7`: connections identical.
`.venv/bin/python tools/sameconn.py e1b2cc7`: connections identical.

Round 1: no findings that change a connection.

### West logic and the bit lines (run of 2026-11-20)

Round 2 (full review of the west-logic piece; fresh Fable 5.2 reviewer; 2026-11-20 13:46 -0600; commit 2eb4695; images
`cache/scratch/cdp3/review-2/`). Told to suspect the metal at every pad's ring, the inverter copy's fit,
contacts at the crossings, a pad on the x 7880 metal, anything left out. Checked at 4-6x in two or more
shots with `tl5_tracks.py` and `px.py`: the U1 copy (rail contact, gate row, node, the closed west box,
strip, tail, tie, VCC box); the pads (7838,8062), (7836,8430) (metal through, rings both sides),
(7838,8582) (metal ends), (7313,7995), (7313,8625), (7400,8778); the metal x 7837 over the rows at
y 8305-8330 and 8500-8522; the gate row under the metals x 7355 and x 7400; the row y 8615-8635 under
`tc2_r5718`'s metal (8 px of field from that metal's pad poly); the column under the metal y 8700-8715;
the metal x 7880 as one metal from y 9150 to the pad (7878,8385), bare ground y 8327-8382 to the next
pad. Not checked: the staircase metal west of x 7330; the polys beyond the ports.

Findings, geometry only: the load plate's lower-left corner steps in to x 7700 below y 8050 (over field;
left as drawn).

The same reviewer read the five undecided boundaries of the cluster beside row A independently (Not
done): all five as one diffusion each, against three controls in the same gap, and noted that the row
y 8502-8525 may be broken under the rail at x 7984-8005.

Round 2: no findings that change a connection.

Round 3 (full review of the six bit-line joins; fresh Fable 5.2 reviewer; 2026-11-20 13:46 -0600; commit c411e90; images
`cache/scratch/cdp3/review-3/`). Checked: all six lines continuous y 7480-8110 (no stretch without metal
over 21 px; every stretch of 15 px or more on 4x views of both metal shots, c2 and c5 at 6x in three
shots); the same track at both ends, no jog; no other metal joins or crosses; whole-die extraction 0
errors; `sameconn.py 2eb4695`: every difference carries `cdp3_bl_c2..7` or `db_b0..5`. Remarks, notes
only: `cdp2`'s cell already draws the metal to y 7821 with the contact at y 7789 (the notes said y 7556
and "taps not drawn"; corrected); c7's metal centre is x 10414-10416 (drawn 10419, overlapping).

Round 3: no findings.

## Corrections (coordinator, from the handoffs of 2026-11-20)

- "Row I (y 11050-11200+) ... not traced" and Not done: it is the top of `cdp4`'s comparator row (the bus lines against R15), traced in `cdp4` run 3; lines e and f pass through it with no contact. The uncertain metal pieces of the bit lines and line f at y 11048-11200 were removed from `trace/cdp3.txt` (`cdp4` draws the same metals firm; `tools/sameconn.py`: connections identical).
- `bus_eq_r15` ("in"): its driver is `cdp4`'s comparator: `bus_eq_r15` = NOR of the eight "not equal" nodes `cdp4_xr_s#_ne`.
- Ambiguities, "A gate driving a bit line" (reading (a), the `?B` at 8081-8105 x 9221-9254): the NAND's output is extracted on `cdp3_bl_c1`, which is now known to run on south as `cdp4`'s in track of slice 1, the data line of R15's latch, and both NAND inputs are the two comparators' match lines. A gate output on a register's data line adds to the doubt on reading (a); the box is to be read again (the master list's row `cdp3` (continue)).

## Corrections (coordinator, from the handoffs of 2026-11-20, second batch)

- The gates of rows E and F ("drivers not known"): they are `rsel12_buf` and `rsel13_buf`, the read selects of R12 and R13 (`busl` run 8, pieces `r12`, `r13`: one thin metal each up the left bus field from `regs`' ports, no uncertain item). So R12 is read through row E (row C onto bus N) and R13 through row F (row H onto bus N). Seen in the extraction: in columns c0 and c1 the transistor gated by `rsel12_buf` lies between `vss` and `cdp3_n_c#` (t1523, t1977), in c2-c7 between `cdp3_cq_c#` and `cdp3_n_c#`: the two bits R12 does not have read as a fixed level. The two gate labels are renamed at the next refresh.
