# Below the register-select gates (`bd3`, x 14100-15900, y 16550-17100 and along the wires)

> **Correction (coordinator, 2026-11-15).** This block's finding "strobe = NOT `e_b`, so each
> write strobe is select AND E" is wrong. The bd2 block showed by measurement that the
> metal line this run followed from the strobe driver's gate down to `e_b` is broken at
> y 15443-15470. The driver's input is the output of a latch that is open while E is high
> and set by "write, chip selected, RS high" (see `notes/blocks/bd2.md`). Everything else
> below stands.

## Status

- Traced and extracted (trace/bd3.txt, `@requires sel`, 0 errors, no open nets): the
  strobe's two lines and the link between them; the row at y 16740-16870 (a two-inverter
  buffer of rsel12); two more inverter + NOR pairs in the right-hand column (write
  strobes of R12 and R13) and a two-inverter buffer of rsel13 below them; all 16 tracks
  down to where they leave the region, including the nested corners and supply-rail
  crossings of T0-T6.
- The strobe has no driver inside the region; it was followed east to its driver at
  x 15900-16270, y 15030-15160 (package bd2's area), which is traced too:
  **strobe = NOT e_b**, one big inverter. So wr_rN = rselN AND E.
- Not traced: anything south of y 17100 except T3-T6's corners and the R13 buffer.
- **Run 3 (2026-11-28)**: the two strobe pairs of the right-hand column (R12, R13) are `bd3`'s own cell
  `bd3_rwr`, drawn from the photos with real loads (no `?` item), and the first inverter of the R12 select
  buffer has its real width (44, was 134). No connection changed. See "Run 3".
- **Run 4 (2026-11-28)**: the R13 select buffer is drawn from the photos (it was a copy of `sel`'s cell `sel_rbuf`
  with schematic loads): first inverter 43/20 against 28/54 (the strobe cell's inverter once more), second
  inverter 132/22 against 68/39. The R12 select buffer's loads and second inverter were re-read: as drawn, but
  for the second load's foot row, which lies 11 px south of where it was drawn. No connection changed; the
  package has no `?` item left. See "Run 4".
- Every piece was checked by overlay (1.1x-1.65x for wiring, 3-6x at the junctions
  that decide a net: the strobe link, the driver's output and input, the rsel12 bar
  under the tracks).

## Inventory

| What | Where | Notes |
|---|---|---|
| Gate column, last row | x 14290-14930, y 16740-16870 | two inverters in series (not the inverter + NOR of the rows above): right half first stage, left half second stage |
| Ground rails of the gate column | x 14434 and 14789 | both end at y 16876 |
| Supply rail of the gate column | x 14584-14634 | runs on south past y 17300; by scan (sel_tracks) it reaches the VCC band of the input row at y 18130, and a 2.5x view at (14609,18125) shows it merging into that band. So sel's `vcc` label on it is traced, not only inferred from the loads |
| Wide rail | y 16907-16954, x 14060-14634 | joins the supply rail at its east end (seen at 1.1x and 1.65x, no dark line between); so `vcc`. Runs on west of x 14060 and turns north near x 13970-14030 |
| Strobe link | poly, contact 14239,16865 - x 14242 south - y 16996 east - contact 14673,16997 | joins `wr_stb_n` to T0 (`wr_stb_n`) |
| Horizontal bundle | y 16998-17258 (and on to 17432), x < 14912 | T0-T6 after turning west, pitch 43.3. Each crosses the supply rail in poly between two contacts (x 14672/14713 east, 14456/14499 west, alternating) |
| Right-hand gate column | x 15540-15890, y 16490-17360 | the circuit of `sel`'s cell `sel_rwr` twice more, since run 3 as `bd3`'s own cell `bd3_rwr` (master at R12, y 16490-16855; R13 at 0,304); then the R13 select buffer (y 17100-17376), drawn from the photos since run 4 |
| Track shuffle | x 15214-15344, y 16860-17040 | T8, T9, T10 each step one track left where the track to their left has ended |

## Logic

Traced (extracted by netlist.py) unless marked believed.

### The strobe

`wr_stb_n` and `wr_stb_n` are one net (traced):
- `wr_stb_n` (metal x 14307) turns west at y 16739 below the R7 NOR's contact, runs to
  x 14239 and down to a contact at (14239,16865) on a poly pad.
- The poly runs south along x 14242 under the wide rail to y 16996, then east along
  y 16996 (y 16987-17005) under the supply rail to a contact at (14673,16997).
- T0 (`wr_stb_n`, x 14912) comes down, turns west at y 16998 and ends on that contact.

The trace declares `@alias wr_stb_n wr_stb_n`.

Loads of the strobe in sel + bd3: the 16 NOR gates, one per register R0-R15 (R0-R11 in
the gate column; R14, R15, R12, R13 in the right-hand column). Nothing else. T15
(x 15561) ends at the R13 NOR's contact (15560,17072). T0 has no tap between y 16700
and its end. No gate in this region drives the strobe: its only other end is the
poly that arrives from the east along y 14825 at x 15850 (sel's port).

### The strobe's driver (outside the region, traced: block `bd3_stb` in the trace)

    wr_stb_n = NOT e_b       pull-down W/L 282/28, load 75/37

Route, from the gates back to the driver:
- sel's poly along y 14825 runs on east from x 15850, turns down at x 15932 to a
  contact at (15932,14870) (4.2x overlay: no other branch).
- Metal east along y 14872 (x 15952-16238 by scan) to a contact at (16257,14872).
- Poly south along x 16259 under the wide rail y 14912-14959, to y 15040, then west to a
  buried contact at (16200,15046). At 4x (acid and acid1b) the poly turns west there;
  it does **not** run on to the contact pad 30 px further south at (16255,15085),
  which is the gate's input. Clear gap y 15050-15066 between them.
- The buried contact is on the drain of one wide transistor. Its gate is L-shaped: a
  band y 15072-15100 from the pad at (16255,15085) west to x 15979 and then down
  x 15979-16009 to y 15163, wrapping the source, which has a contact at (16035,15122)
  to the rail x 16012-16065 (that rail comes from the east along y 14912-14959 and
  turns south here; ground by the orientation of this gate). No other poly crosses
  the diffusion: a single pull-down.
- Load: poly block x 15903-15940, y 15034-15160 over a strip (y 15073-15147) that comes
  from under the supply rail of sel's right-hand column (x 15795-15890, contacts
  there); tied to the drain by a buried contact at (15945,15048).
- Gate input: from the pad (16255,15085) metal runs down x 16255 to y 15221, west to
  x 16167 and down. Checked at 2x in the metal shot from y 15190 to 16430: one
  unbroken line, with tap contacts at (16165,15430), (16165,15605), (16165,15735),
  (16165,15822) and a branch west at y 15475 (none of the taps followed). trunks.txt
  has `e_b` on x 16170 from the E buffer up to y 16400. So the input is `e_b` (E
  buffered, same sense as the pin).

Consequence (traced): every write strobe is wr_rN = rselN AND e_b. Nothing but E
gates the strobe; CS, RS and R/W must act somewhere else (on the select lines through
the address rows, or on the data path). The strobe net has exactly these loads: the
16 NORs.

### The gate of wr_r7 (and wr_r11): row 5 of the gate column

Already in sel.txt as the sixth pair of `sel_wr` instances (NOR at y 16600-16720).
Looked at again here in passing (1.6x overlay for the left half, 1x for the right):
the cell sits on the features, the strobe contacts are at (14305,16696) on `wr_stb_n`
and (14918,16696) on T0, the outputs leave as sel has them. wr_r7 = NOR(rsel7_n,
strobe), nothing different from the rows above. Its output poly goes west along
y 16651, down x 14135 and west again along y 16864 (4x), out of the region.

### R12 select buffer (row y 16740-16870)

    rsel12_bufn = NOT rsel12        (right half; pull-down W/L 44/22 since run 3 (was drawn 134/22), weak load 27/56)
    rsel12_buf = NOT rsel12_bufn       (left half;  pull-down W/L 135/22, load 67/31)

- Input: T8's upper part (rsel12) ends at a contact at (15258,16668). Poly from it goes
  west along y 16668, south along x 15196, then west along y 16778 under tracks T7..T0
  (no contacts; 3.6x view) and is the gate bar of the first inverter, under the right
  ground rail.
- First inverter's output: buried contact at (14860,16820), poly east, south along
  x 14912 (directly under T0's metal, no contact), west along y 16910 across the supply
  rail and under the top edge of the wide rail to a pad at (14305,16867); metal up to a
  contact at (14306,16778) on the gate bar of the second inverter.
- Second inverter's output: buried contact at (14365,16822), poly west along y 16822,
  then south along x 14199 under the wide rail and all the horizontal lines. Seen to
  y 17320, still going.
- Both loads hang from one supply contact at (14609,16790).
- Believed: this is the read enable of R12, as `rsel14_buf`..`rsel17_buf` are for R14-R17.
  It leaves southwards on its own instead of on a bundle track.

### Right-hand gate column, continued

    rsel12_n = NOT rsel12     wr_r12 = NOR(rsel12_n, wr_stb_n)     gates at y 16562; 16691, 16779
    rsel13_n = NOT rsel13     wr_r13 = NOR(rsel13_n, wr_stb_n)     gates at y 16866; 16995, 17083

(Gate positions as read in run 3; runs 1-2 had them 6-12 px north, from `sel`'s cell placed at multiples of 300.)

- rsel12: contact (15258,16560) on T8, poly east (in sel.txt).
- rsel13: T7 ends at a contact at (15214,16864); poly east along y 16862 to the inverter.
  The same poly also runs south from the pad along x 15216, directly under the metal
  that occupies T7's line below y 16902 (which is wr_r12), to y 17168, and east along
  y 17168 to the R13 buffer (below).
- Strobe gates: contacts on T15 at about (15559,16780) and (15559,17084) (run 3; runs 1-2: (15560,16772),
  (15560,17072)); T15 ends there.
- Outputs: poly west along y 16735 to a contact at (15258,16734) (T8's lower part starts
  there), and along y 17038 to a contact at (15344,17036) (a new line starts there on
  T10's x).

### R13 select buffer (right-hand column, y 17130-17360)

    rsel13_bn = NOT rsel13            (pull-down W/L 43/20 under the ground rail only, weak load 28/54)
    rsel13_buf = NOT rsel13_bn        (pull-down W/L 132/22, load 68/39)

Two inverters in series, drawn from the photos in run 4 (until then a copy of `sel`'s cell `sel_rbuf` at
dy 2258, with schematic loads; details under "Run 4"). Gate bars at y 17170 and y 17301. Output: buried
contact at (15620,17342), poly west along y 17340, then south along x 15512; seen to y 17700, still going.

So R12 and R13 each have an ordinary write strobe and a buffered select, exactly like
R14 and R15. (R12's buffer sits in the gate column and is called `rsel12_buf`; R13's is in
the right-hand column and is called `rsel13_buf`.) Believed: the buffered selects are read
enables, so R12 and R13 are readable on this chip.

### Where each track goes

| Track | x at y 16550 | Net | Below y 16550 |
|---|---|---|---|
| T0 | 14912 | wr_stb_n | down to y 16998, west to contact (14673,16997), poly on to wr_stb_n. Ends |
| T1 | 14954 | wr_r5 | corner at y 17041; contacts (14713,17040), (14499,17040); west along y 17041 |
| T2 | 14998 | wr_r3 | corner y 17084; contacts (14672,17084), (14456,17084); west along y 17084 |
| T3 | 15041 | wr_r8 | corner y 17128; contacts (14713,17127), (14499,17127); west |
| T4 | 15085 | wr_r9 | corner y 17172; contacts (14672,17171), (14456,17171); west |
| T5 | 15128 | wr_r11 | corner y 17215; contacts (14713,17214), (14499,17214); west |
| T6 | 15171 | wr_r10 | corner y 17258; contacts (14672,17257), (14456,17257); west |
| T7 | 15214 | rsel13 | ends at contact (15214,16864) |
| T8 | 15258 | rsel12 | ends at contact (15258,16668). From contact (15258,16734): wr_r12, down to y 16910, steps west to x 15214, south |
| T9 | 15301 | wr_r14 | down to y 16955, steps west to x 15258, south |
| T10 | 15344 | wr_r15 | down to y 16998, steps west to x 15301, south. From contact (15344,17036): wr_r13, south |
| T11 | 15388 | rsel16_buf | straight south |
| T12 | 15431 | rsel17_buf | straight south |
| T13 | 15474 | rsel15_buf | straight south |
| T14 | 15517 | rsel14_buf | straight south |
| T15 | 15561 | wr_stb_n | ends at contact (15560,17072) |

By scan only (sel_cut.py, not drawn): the lines on x 15214, 15258, 15301, 15344 also
turn west, at y 17302, 17346, 17388, 17432, and cross the supply rail the same way
(pads at x 14713/14499 for 17302 and 17388); at x 14110 there are lines at every
43.3 px from y 16998 to 17432. At the west end the bundle turns north in nested corners
(y 16998 line at x 13957, y 17042 line at x 13915; one 3x view).

## Ports

| Name | Layer | Crossing | Direction | What |
|---|---|---|---|---|
| wr_stb_n = wr_stb_n | metal | 14307,16550 and 14912,16550 and 15561,16550 (top) | in (from sel) | strobe; one net |
| rsel12, rsel13, wr_rN, rselN_buf | metal | tracks at y 16550 (top) | in | see the track table |
| wr_r7 | poly | 14100,16864 (west) | out | turns west at y 16864 (from x 14135); goes on past x 14040 |
| rsel12_buf | poly | 14199,17100 (bottom; drawn to 17300) | out | rsel12 buffered; seen to y 17320 |
| rsel13_buf | poly | 15512,17500 (drawn to there) | out | rsel13 buffered; poly going south, seen to y 17700 |
| (trunks' X) | metal | 14100,16998 (west) and 14543,17100 (bottom) | through | not one of the tracks and not drawn in bd3.txt: see Ambiguities |
| wr_r5 | metal | 14100,17041 (west) | out | |
| wr_r3 | metal | 14100,17084 (west) | out | |
| wr_r8 | metal | 14100,17128 (west) | out | below the region's bottom edge |
| wr_r9 | metal | 14100,17172 (west) | out | |
| wr_r11 | metal | 14100,17215 (west) | out | |
| wr_r10 | metal | 14100,17258 (west) | out | |
| wr_r12 | metal | 15214,17100 (bottom) | out | |
| wr_r14 | metal | 15258,17100 (bottom) | out | |
| wr_r15 | metal | 15301,17100 (bottom) | out | |
| wr_r13 | metal | 15344,17100 (bottom) | out | |
| rsel16_buf | metal | 15388,17100 (bottom) | out | |
| rsel17_buf | metal | 15431,17100 (bottom) | out | |
| rsel15_buf | metal | 15474,17100 (bottom) | out | |
| rsel14_buf | metal | 15517,17100 (bottom) | out | |
| vcc | metal | 14584-14634, 17100 (bottom); 14060, 16907-16954 (west) | - | supply rail and the wide rail |
| vss | metal | 15663-15718, 17100 (bottom) | - | ground rail of the right-hand column runs on |
| vcc | metal | 15795-15890, 17100 (bottom) | - | supply rail of the right-hand column runs on |

The same ports, one per line with the place where each drawn wire ends, are in `ports.d/bd3.txt` (made in run 3).
The two rows of the strobe's driver (`e_b`, its ground rail) left this table in run 3: that drawing was removed
from the trace by the coordinator (the driver is `bd2`'s).

## Ambiguities

- **Trunks' line X and the strobe.** The metal line "X" of trace/trunks.txt (input of
  inrow's gate 0, believed there to be a clock-like signal; `M 13770,18082 x14543
  y16992 x13952 ...`) comes up x 14543 from the south, turns west at y 16998 and north
  at x 13957. For 300 px (x 14250-14553) it lies exactly on top of the strobe's poly
  link. No contact ring is visible anywhere along it in `metal` or `metal1` (3.8x), and
  the trace has none, so the two are separate nets. Against: the line occupies the
  place T0 would have in the bundle west of the supply rail, and the poly under it
  looks darker in `acid1b` at x 14235-14390 than poly under metal usually does (but so
  does poly under the supply rail, where there is certainly no contact). For: rsel13's
  poly runs under wr_r12's metal and `rsel12_bufn`'s poly under T0's metal in the same way,
  so poly under foreign metal is this layout's habit; and the strobe is now traced to a
  plain inverter of `e_b`, which has no business on a clock line. If X ever turns out to
  be E-like, look here again. (bd3.txt does not draw X; trunks.txt does.)
- **notes/blocks/areg.md reads the strobe's driver differently** ("a poly going down
  x 16247-16265 to a contact at (16255,15085)", i.e. the strobe wire would be `e_b`
  itself). That was a low-zoom reading. At 4x in `acid` and `acid1b` and at 6x in `metal`
  and `metal1` (view x 16215-16310, y 15015-15110) the poly coming down x 16259 turns
  west at y 15030-15048 and ends on the buried contact at (16200,15046); a band of bare
  field, y 15050-15068, unbroken in both chips, lies between it and the pad at
  (16255,15085). So the strobe is the inverter's output (NOT `e_b`), not `e_b`.
- sel.txt draws `wr_stb_n`'s metal straight down to y 16760; it really turns west at
  y 16739. Harmless (the overshoot touches nothing).
- Loads of `sel_rwr` (R12, R13 pairs): **settled in run 3** (real geometry in `bd3_rwr`). The R13 select
  buffer's loads: **settled in run 4** (real geometry; "Run 4").
- Pull-down diffusion of the two buffer inverters: **settled in run 3**. The first inverter's bar lies on
  field east of its rail (W 44, under the rail only); the second inverter's bar has diffusion on both sides
  for its whole drawn width (W 135: edge lines across the bar at x 14352 and x 14485).

## Not done

As of run 4 (2026-11-28). **Nothing is left in this package's own files**: every unit in `trace/bd3.txt` is drawn
from the photos, with no `?` item. The older items are done elsewhere: the strobe's driver is `bd2`'s;
`rsel12_buf`, `rsel13_buf` and the tracks south of y 17100 are followed by `regs`; the unit below the R13 buffer
is `regs`' inverter (`d7_out_n`).

What remains nearby is other packages':

- `sel`'s own six cells of the right-hand column (four `sel_rbuf`, two `sel_rwr`, x 15540-15890, y 14850-16550):
  schematic `?` loads, pull-downs drawn the full length of each bar, copies at multiples of 300 and 260 where the
  column's pitch is 304. `sel`'s file. Starting points: `bd3_rwr` placed at 0,-304 and 0,-608 for R14 and R15
  (`tools/dbus_localmatch.py`: scores 0.80-0.89; not checked by overlay); for the four buffers the R13 buffer's
  geometry of run 4 (`sel_rbuf`'s master against it: 0..1,-2256..-2257, scores 0.58-0.69 only, so they may be
  built differently: read each).
- The west-going bundle beyond x 14100 (`wr_r5`, `wr_r3`, `wr_r8`, `wr_r9`, `wr_r11`, `wr_r10`, and `wr_r7`'s
  poly): drawn to x 14090; `bd1`'s notes say `wr_r9`, `wr_r11`, `wr_r10` west of x 14100 lie in `busc`'s region.

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- Not done, the four strobe tracks south of y 17100: followed by `regs` (run 1: the write strobes of R12-R15 to their rows).
- `rsel12_buf` and `rsel13_buf` are followed by `regs` (run 3; pads (14195,17730), (15512,17688)).

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- The ground rail and the supply rail of the right-hand gate column do not end at y 17380: the ground rail's
  metal ends at about y 17527 and the supply rail runs on south past y 17760. Under the undrawn stretch is an
  inverter (`regs` run 5: `d7_out_n` = NOT `rd_b7`, x 15577-15895, y 17372-17491); `trace/regs.txt`
  draws the ground rail to y 17527 and the supply rail to y 17500.

## Re-read item R2 (2026-11-27): the channel's 16 tracks

Matt Godbolt, on Claude Fable 5.2, 2026-11-27 07:29 -0600. Region x 14100-15880, y 16550-17100. **Found as drawn; no trace
line changed.**

R2 asks for the 16 tracks end to end in the clean shot (the notes cited the metal shot for the track checks).
Done with the audit written for R1, `tools/bd1_audit.py 14100 16550 15880 17100` (every trace file loaded:
55 drawn metal items), and `tools/bd1_sheet.py` for the flagged spots (sheet `cache/scratch/bd3/r2/sh1.png`):

1. Breaks (a drawn thin metal with no metal in either metal shot along 14 px or more): **none**.
2. Undrawn metal: **none**; and on two overlays of the whole region (`ovw.png`, `ove.png`, 1.5x, metal shot
   with every package's trace) every metal has its outline: the 16 tracks x 14998-15560 top to bottom, the
   rails, the horizontal lines y 16920-17090 and the short verticals of the west half.
3. Contact holes in the clean shot under drawn thin metal: 19, of which 17 are drawn contacts (`sel`'s and
   `bd3`'s). The other two: (15214,16709) is a triangular scratch beside a plain track (bright and unringed in
   both chips); (14307,16754) is the upper rim of the drawn contact (14306,16778)'s pad. Three drawn contacts
   had no olive hole, (14456,17084), (14239,16865), (14306,16778): each is a pad with ring and bright centre in
   both metal shots and a red-brown box in the clean shot: real. So **no contact that is not drawn, and every
   drawn contact real**.
4. Poly gaps (field colour inside a drawn thin poly): **none**.

Limits as in the tool's docstring: its metal thresholds are weak on dim tracks (hence the two overlays), and it
does not look for a contact on open diffusion beside a metal.

## Run 3 (2026-11-28): the right-hand column's R12 and R13 strobe cells, read at their own place

Tom Seddon's session, on Claude Fable 5.2, 2026-11-28 from 12:13 +0000. Piece `rwr`: x 15575-15895, y 16490-17160.

Until this run the two inverter + NOR pairs were copies of `sel`'s cell `sel_rwr` (`@inst sel_rwr 0,600` and
`0,900`), whose four loads are schematic (`?`) shapes and whose pull-downs were drawn from a low-zoom view. They
are now `bd3`'s own cell **`bd3_rwr`**, drawn from the photos at R12 (the master) and placed once more for R13 at
0,304. **No connection changed** (`tools/t.sh bd3 sameconn.py 0ed5ae7`: connections identical; `rsel12_n` = NOT
`rsel12`, `wr_r12` = NOR(`rsel12_n`, `wr_stb_n`), and the same for R13, as before). What changed is every size,
and the four loads are real geometry with no `?` item.

| Transistor | W/L now | W/L in `sel_rwr` | How read |
|---|---|---|---|
| inverter pull-down | 43/20 | 123/22 | the gate bar lies on field west of the rail; the channel is under the rail only |
| inverter load | 28/54 | schematic | plate x 15780-15834, y 16562-16623, strip edges across it at y 16578 and 16609 |
| NOR pull-downs (two) | 68/22 | 90/24 | the strip runs 26 px west of the rail: an edge line crosses both bars at x 15639 |
| NOR load | 33/40 | schematic | plate x 15762-15804, y 16697-16772, band edges across it at y 16717 and 16754 |

Pull-down against load is about 4 for both gates (2.2 against 0.52; 3.1 x 2 inputs each against 0.83), where the
old inverter's 123/22 against any load of this size would have been 10.

**The pitch of this column is 304, not 300.** `tools/dbus_localmatch.py 15580 16500 15895 16830 0 303 15`: R13 at
0,303 (clean shot, 0.87) and 0,304 (both chip-2 shots, 0.81, 0.82); R14 at 0,-304 and R15 at 0,-607/-608 the same
way. `sel`'s master is drawn at R15 and placed at multiples of 300, so its copies lay 4 px (R14), 8 px (R12) and
12 px (R13) north of the features (`tools/railprof.py 15666 15712 16490 17130`: gate bars under the rail at
y 16554-16574, 16685-16705, 16771-16791 for R12, where the copy had 16545-16567, 16670-16694, 16760-16784). The
two output rows are redrawn to match: `wr_r12`'s poly row is at y 16735 (was 16732), `wr_r13`'s at y 17038 (was
17032; `px.py col 15592 17014 17062 3`: poly y 17031-17045, and salmon y 17032-17044 under the tracks at x 15400).

### The inverter (master, R12)

- Ground land 1 under the rail, x 15666-15708 (`px.py row 16528 15624 15740 4`: tan x 15668-15704 in the clean
  shot, edge 15708-15712, pink field under the rail's margin at 15716), from the NOR above (`sel`'s R14) down to
  the gate. Ground contact about (15683,16518).
- Gate bar y 16552-16572 (`px.py col 15648`, `col 15686`), from the select's poly in the west to its end at
  x 15729. **West of the rail it lies on field**: no edge line crosses it from x 15576 to x 15654 in either metal
  shot (`px.py row 16563 15570 15760 3 all`: chip 2 150-178/100-126/45-68 without a dip), and at x 15648 there is
  field directly north of it (one edge line y 16544-16550, then 160/140/75) and, south of it, a lighter gap of
  6 px (y 16576-16580) between the bar's edge line and the edge line of the output wire (`px.py col 15648 16526
  16626 2 all`): the wire runs beside the bar, not against it. Under the rail the channel's edges cross the bar at
  x 15664 (with the rail's own edge) and x 15708 (dark in the clean shot at 15708-15711, in chip 2's metal at
  15705-15708, with metal on both sides).
- Output band under the rail y 16575-16600; a wire y 16586-16598 west to the output box (x 15606-15636,
  y 16585-16611: dark ring, plain centre), from which the output poly runs west, south as a column x 15576-15598
  and east again as the NOR's gate A (one orange C in both chip-2 shots, 4.4x, `o3-col.png`); the ground it
  encloses (x 15600-15640, y 16618-16660) is field (`px.py col 15650 16610 16816 3`).
- East of the rail the wire (y 16584-16600 at x 15745: `px.py col 15745`) runs to a strip y 16580-16608 under the
  load plate and on, as a neck, to the supply land x 15850-15890, y 16551-16626 under the supply rail, with an
  oval supply contact (ring y 16546-16614: `px.py col 15862`).
- **The tie**: a diffusion arm x 15756-15770 runs north from the wire to y 16538 (`px.py col 15765`: pinker than
  field in chip 2's metal shot, green in the clean shot, from y 16540 to y 16598), and the plate has a north arm
  x 15777-15800 (orange at x 15787, y 16564-16572) into a box x 15772-15800, y 16530-16558 whose centre is plain
  in both metal shots (chip 2 150/105/60 to 150/126/69, chip 1 103/103/79, red equal to green) between dark bands
  of 10-12 px: a buried contact as trap 24 describes it. The load's gate is on its output side: a depletion load.

### The NOR (master, R12)

- Ground land 2 under the rail, y 16634-16680, x 15666-15708; between it and the inverter's output band the rail
  lies on **field** for 30 px (y 16604-16632: greenish grey 141/148/105 in the clean shot against tan 199/180/131
  for the band; `tools/railprof.py` calls it diffusion, trap 18). Ground land 3, y 16790-16853, is also the next
  cell's land 1.
- The strip under the two gate bars runs from x 15640 to x 15708: an edge line crosses both bars at x 15636-15642
  in both metal shots and the clean shot (`px.py row 16695`, `row 16781`), and west of the rail there is
  diffusion on both sides of each bar (`px.py col 15650 16610 16816 3`: a sliver y 16662-16672 north of gate A,
  the output node y 16709-16758 between the bars, a sliver y 16797-16808 south of gate B; pinker than field in
  chip 2's metal shot, red over green by 14-24 in its stripped shot, where the enclosed field reads -5 to -9).
- Gate A (y 16680-16702) is the inverter's output poly; gate B (y 16768-16790) comes from the contact on T15,
  about (15559,16780).
- Output node: west to the output box x 15606-15636, y 16722-16750 (the output row leaves west from it), east as
  a band y 16719-16752 under the load plate to the supply land x 15848-15890, y 16673-16754 with its oval
  contact (`px.py col 15865`).
- **The tie**: a diffusion arm x 15732-15749 runs south from the band to y 16802 (`px.py col 15741`), its foot
  turns east, and the plate's south end lies on it in a box x 15756-15790, y 16776-16803 with a plain centre at
  (15773,16790) in both metal shots (`px.py col 15778`: 137/133/74 and 137/134/58). Between the arm and the plate
  above the box there is 8 px of field (text map, y 16759-16771).

### The copy (R13, at 0,304)

Overlay at 2x on the metal shot and the clean shot (`o2-r13.png`): every outline on its feature, the loads, tie
boxes, lands and contacts included. Its land 3 (y 17104-17157) is the land of the R13 select buffer's first
inverter. Two ring-like specks inside the enclosed field of this copy, at (15627,16952) and (15610,17112), are
in the clean shot only (flat field in both metal shots and chip 2's stripped shot: `px.py row 16952 15606 15648 3
all`, `row 17112 15600 15642 3 all`): residue on chip 1.

### Traps met

- The clean shot is inverted in the open gap between the two rails' margins at the inverter load's tie (x 15770-
  15798): pale where both metal shots have a dark wall (row y 16546, x 15773-15779). Trap 28; the tie was read
  from the two metal shots and chip 2's stripped shot.
- `tools/opendiff.py 14100 16550 15850 17100` lists three "green" areas at x 15822-15850 as undrawn diffusion:
  they are field under the middle of the supply rail (greenish grey in the clean shot there), which the tool's
  docstring excludes.

### Ambiguities of run 3

1. **The joins in the ground rail's west edge line** (x 15660-15666): the inverter's output wire to its band
   under the rail (y 16586-16599), and the NOR's two slivers (y 16662-16673, y 16796-16809) to ground lands 2
   and 3. The rail's edge line hides them and the clean shot is inverted just west of the rail. Drawn joined:
   the dark line there is 4-6 px wide, against 12 px where a land ends (review round 2). If a sliver were cut
   off, that pull-down would be 42 wide instead of 68; the equations would be the same. The same in the copy.
2. **The output wire's widening under the inverter load's plate**: the wire is y 16584-16600 at x 15745 and the
   strip y 16578-16609 under the plate; where it widens (drawn at x 15771) was not measured. Sizes only.
3. The NOR's gate bars and the inverter's end at different x east of the rail (15721 and 15729): as measured,
   all three past the strip's edge (x 15708).

### Piece `buf`: the R12 select buffer's pull-downs (gate column, y 16740-16845)

The notes carried both pull-downs as "W about 135, uncertain by 30%": each gate bar runs 50-90 px beyond its
ground rail. Read by the same test as the strobe cell (an edge line across the bar; diffusion against both of
the bar's edges):

- **First inverter (right half, ground rail drawn x 14763-14815): W 44, not 134.** East of the rail no edge line crosses the
  bar from x 14822 to x 14896 in either metal shot (`px.py row 16778 14730 14906 4`; the dip at x 14898-14902 is
  T0's metal edge), and there is field directly north of the bar at x 14830, 14850 and 14884 (`px.py col`: one
  edge line y 16760-16766, then 157-166/131-139/75-85; chip 2's stripped shot red over green by 1-7) and, south
  of it, a 6 px lighter gap before the output band's own edge (x 14830, 14850) or field (x 14884). So the bar
  lies on field there. Under the rail the channel runs from x 14773 (edge in the clean shot at 14770-14774) to
  x 14817 (bright salmon to 14814, edge 14818-14822); the land north of the bar is x 14776-14814 (`px.py row
  16755`: tan, with pink field under the rail's margin west of it), and it is the foot of the R11 NOR's strip
  (`sel`). The diffusion `D 14756,16755:14890,16797` is redrawn `D 14774,16750:14818,16800`. Pull-down against
  load is now 2.0 against 0.48 (was 6.1 against 0.48).
- **Second inverter (left half, ground rail drawn x 14408-14460): W 135 stands.** Edge lines cross its bar at x 14348-14356
  and x 14484 in both metal shots and the clean shot (`px.py row 16778 14296 14508 4`), and between them the bar
  has diffusion on both sides in the open stretches (`px.py col 14380`, `col 14474`: a sliver y 16752-16759
  north of the bar and the output band south of it, pinker than field in chip 2's metal shot and red over
  green by 23-31 in its stripped shot); west of the edge line there is field on both sides (`px.py col 14338`).
  Against its load of 64/31 that is 6.1 against 2.1: a driver, where 44 would give 1.

`tools/t.sh bd3 sameconn.py 0ed5ae7`: connections identical (`rsel12_bufn` = NOT `rsel12`, `rsel12_buf` = NOT
`rsel12_bufn`, as before). Overlay `b2-inv1-new.png` (2.8x, metal and clean shot).

## Run 4 (2026-11-28): the R13 select buffer read at its own place; the R12 select buffer's loads re-read

Tom Seddon's session, on Claude Fable 5.2, 2026-11-28 from 12:55 +0000. Two pieces: `rbuf` (x 15575-15895,
y 17100-17376, south of the row's region, in `bd3`'s file since run 1) and `buf2` (gate column, x 14290-14740,
y 16740-16855).

**No connection changed** (`tools/t.sh bd3 sameconn.py 6b08a309` and `.venv/bin/python tools/sameconn.py 6b08a309`:
connections identical; `rsel13_bn` = NOT `rsel13`, `rsel13_buf` = NOT `rsel13_bn`, as before). `tools/unsure.py
--equations`: `rsel13_bn`, `rsel13_buf`, `rsel12_bufn`, `rsel12_buf`, `wr_r12` and `wr_r13` are all firm; the
package has no `?` item left.

### Piece `rbuf`: the R13 select buffer

Until this run `@inst sel_rbuf 0,2258 tag=13`: `sel`'s cell, whose two loads are schematic (`?`) shapes and
whose pull-downs are both drawn 133 wide. Now plain geometry in `trace/bd3.txt`, read from the photos.

| Transistor | W/L now | W/L in `sel_rbuf` | How read |
|---|---|---|---|
| first inverter, pull-down | 43/20 | 133/22 | the gate bar lies on field west of the rail; the channel is under the rail only |
| first inverter, load | 28/54 | schematic | the strobe cell's inverter load again: plate x 15780-15834, y 17170-17231, strip edges at y 17187, 17215 |
| second inverter, pull-down | 132/22 | 133/22 | edge lines across the bar at x 15609 and x 15741, diffusion on both sides of the bar between them |
| second inverter, load | 68/39 | schematic | plate x 15805-15844 under the supply rail over a strip y 17277-17345 |

Pull-down against load: 2.2 against 0.52 (4.1) and 6.0 against 1.74 (3.4). The first stage is small and the
second is the driver of the long line `rsel13_buf`, as in the R12 select buffer (2.0 against 0.48, 6.1 against 2.2).

**The first inverter is the strobe cell's inverter a third time**, two pitches south of R12's
(`tools/dbus_localmatch.py 15580 16500 15895 16640 0 608 15 acid1b,metal,acid,metal1`: 0,607 or 1,608, scores
0.88, 0.81, 0.84, 0.85), so its geometry is `bd3_rwr`'s inverter moved by 0,608 and checked junction by junction:

- Gate bar y 17160-17180. West of the rail it lies on field: no edge line crosses it from x 15570 to x 15654 in
  either metal shot (`px.py row 17171 15570 15760 4 all`: chip 2 158-179/106-129 without a dip), field directly
  north of it at x 15648 and, south of it, the 6 px lighter gap before the output wire's own edge (`px.py col 15648
  17134 17234 2 all`). The channel is under the rail, x 15665-15708; the bar ends at x 15729.
- Output band under the rail y 17182-17209 (clean shot tan from x 15665 to x 15722: `px.py row 17200 15590 15900 3
  all`); wire west y 17194-17207 to the output box x 15606-15636, y 17193-17219 (plain centre x 15614-15624
  between dark bands: `px.py row 17207 15596 15668 3 all`), from which the output poly runs west, south as a
  column x 15576-15598 and east again as the second gate bar.
- **Field under the rail between the band and the second inverter's ground land**, y 17209-17240 (`px.py col 15686
  17176 17252 3 all`: clean shot grey 141-160/122-141/98-119 against tan 197/180/130 for the band and 208/176/136
  for the land; `tools/railprof.py` calls part of it diffusion, trap 18).
- East of the rail the wire (y 17193-17208) runs to the strip under the plate; the tie's diffusion arm x 15756-15770
  runs north from the wire to y 17146 (`px.py col 15763 17130 17214 3 all`: diffusion colour without a break from
  y 17148 to y 17205), and the plate's north arm ends in the tie box x 15772-15800, y 17140-17166 (`px.py col 15787
  17130 17240 3 all`: dark 17136-17148, plain 17151-17154 with red equal to green in chip 1, dark 17157-17169, then
  the plate's orange; trap 24's box).
- **One difference from the strobe cell**: the supply land is 20 px shorter (y 17159-17214; the strobe cell's is
  75 tall: `px.py col 15864 17140 17240 4 all`, `col 15880` here and at R12). So the unit is not placed as a copy
  of a cell. The supply contact's hole is at about (15856,17182) in the clean shot.

**The second inverter is its own layout** (views `r3-inv2-metal.png`, `r4-inv2-clean.png` at 3.9x; `r5-knot-a.png`,
`r6-knot-b.png` at 6x in four shots; overlay `r9-inv2-ov.png`):

- Ground land 2 under the rail, y 17240-17290 (contact about (15683,17263)).
- Gate bar y 17290-17312, from the column in the west to an end cap at x 15758. **Edge lines cross it at
  x 15606-15612 and x 15738-15744** in both metal shots (`px.py row 17301 15570 15790 3 all`), and between them
  there is diffusion on both sides of the bar west and east of the rail: a sliver y 17274-17283 north of it and
  the output band south of it (`px.py col 15635 17244 17366 2 all`: chip 2 177/132/88 and 183/135/85 against field
  157/133/81, chip-2 stripped shot red over green by 19-28; `px.py col 15730 17244 17376 2 all` the same, weaker
  in chip 2 and plain in chip 1: 164-172/118-121/55-73 against 145/120/80). So the channel is 132 wide,
  x 15609-15741; `sel`'s 133 stands for this one.
- Output band south of the bar: y 17316-17326 west of the rail, to y 17332 under it, y 17317-17338 east of it.
  Below it under the rail y 17343-17364 is field (`px.py col 15686 17304 17384 3 acid1b,metal1`: greenish
  128-137/150-156/91-108), then `regs`' inverter's land.
- Output box x 15604-15636, y 17328-17356, hanging under the band's west end; the output poly leaves it west.
- East, the band narrows to a wire y 17322-17334 that runs to the load's strip at x 15793 (`px.py row 17328 15716
  15812 3 all`: no dark break, chip 2 135-182 in red throughout; dimmer over the tie box, where it is about 10 px
  between two edge lines; continuous tan in chip 2's stripped shot).
- Load: a strip x 15793-15850, y 17277-17345 from the wire to the supply land x 15850-15892, y 17255-17345 (contact
  hole at about (15866,17300) in the clean shot), crossed by the plate x 15805-15844 under the supply rail (clean shot:
  bright salmon over the strip, pale salmon above it from y 17262 and below it to y 17374).
- **The tie**: the plate's foot is a poly row y 17358-17374 that runs west from under the rail to x 15746 (`px.py
  col 15781 17306 17380 2 all`: orange 17358-17371; `row 17366 15730 15850 3 all`), and ends under a box
  x 15743-15773, y 17333-17362 that hangs from the output wire: dark band y 17332-17338, plain centre y 17340-17352
  (chip 2 153-161/131-144/65-78, chip 1 132-156/117-135/51-80), dark band y 17354-17362 (`px.py col 15758 17306
  17380 2 all`). A buried contact of trap 24's form: the load's gate on its output, a depletion load. Between the
  box, the wire, the row and the rail a pocket x 15773-15790, y 17341-17352 is field.

### Piece `buf2`: the R12 select buffer's loads and second inverter, re-read

Run 3 left these as run 1 drew them. Read on two overlays (`q1-r12loads.png` 4.5x, `q2-r12inv2.png` 3.9x) and by
profiles in both metal shots and chip 2's stripped shot:

- **First load** (east of the supply rail): as drawn. Plate y 16778-16841, strip edges across it at y 16796 and
  y 16825 (`px.py col 14670 16770 16850 3 metal,metal1,acid`; W 29, drawn 27); tie box plain centre y 16759-16765
  between dark bands (`px.py col 14690 16738 16792 3`); the strip reaches the supply land under the rail's margin
  (`px.py row 16810 14620 14660 2 all`: clean shot tan to x 14639, the plate from x 14642).
- **Second load** (west of the rail): the circuit as drawn, **the foot row 11 px south of where it was drawn**.
  The plate's poly runs from y 16744 to y 16850 with the strip's edges across it at y 16757 and y 16825 (`px.py col
  14566 16742 16850 3`; W 67, drawn 64), and its foot row is at y 16835-16851 (`px.py col 14530 16796 16862 2`:
  the output band y 16802-16816, dark y 16820-16834, orange y 16836-16850; drawn y 16823-16841). The tie box is
  x 14483-14512, y 16811-16840, plain centre y 16821-16833 (`px.py col 14498 16788 16850 3`, `row 16830 14470 14560
  3`), hanging under the output band like the R13 buffer's, with the foot row ending under it. The output side of
  the load is a strip only 14 px wide between the plate and an edge line at x 14529 (`px.py row 16780 14518 14590
  3 all`), and the band runs into it without an edge (`px.py row 16806 14496 14590 3 all`). Redrawn: the row, the
  plate's ends (y 16744-16851), the box, the strip's south edge (16823). Load 67/31 (was 64/31).
- **First output box** (x 14843-14879, y 16803-16836): dark bands, plain centre x 14857-14863, y 16813-16822,
  the output poly leaving east (`px.py row 16819 14830 14900 3`, `col 14861 16786 16846 3`): as drawn.
- **Second inverter**: bar, channel (edges x 14353 and x 14488), band, the output box in the west with its poly, the
  pad (14306,16778): each outline on its feature (`q2-r12inv2.png`).

### Traps met

- The clean shot is inverted at the R13 buffer's second tie box (a pale oval at y 17330-17338 where both metal
  shots are darkest): trap 28 again, in the open group between the two rails. Read from both metal shots and
  chip 2's stripped shot.
- A profile along a narrow diffusion's flank reads darker and greyer than field (`px.py row 17275`, on the north
  flank of the sliver y 17274-17283): the column profile across it decided. Trap 38's point.
- A low-zoom reading put a poly row 11 px off (the R12 buffer's foot row, from run 1's views): a column profile
  across a row gives its place to 2 px.

### Ambiguities of run 4

1. **The joins in the ground rail's edge lines**, as in run 3: the second inverter's slivers and band to the land
   and band under the rail (x 15660-15666 and x 15712-15720), the first inverter's wire to its band. Drawn joined.
   If the second inverter's parts outside the rail were cut off, its pull-down would be 44 wide instead of 132
   (against a load of 68/39: a ratio of 1.2, which no gate here has); the equations would be the same.
2. **Each tie box is read from its form** (a 30 px box with a plain centre between dark bands, the load's poly
   ending in it, the output diffusion against it), not from seeing poly on diffusion; the clean shot is inverted
   at the second. Without the tie the plate would have no connection at all.
3. **The edge at x 15741 across the second bar** is read as the diffusion's east edge, with the bar running on
   17 px to its end cap. If it were the bar's end, the width would be the same.
4. The first inverter's ground contact is the R13 strobe NOR's (land 3 of `bd3_rwr`'s copy, drawn at
   (15683,17118)); `sel`'s cell had a second one at (15683,17133) on the same land. It is one contact, bright
   centre y 17110-17140 in both metal shots (`px.py col 15683 17092 17162 3 metal,metal1,acid1b`), so drawn once.

## Review

### Round 1 (full review), 2026-11-27: the re-read of the channel (R2)

A fresh Claude Fable 5.2 agent, on commit bd5e6a1, images in `cache/scratch/bd3/review-1/`. Told to suspect: a
contact on a track that is not drawn, a track that ends or jogs where it is drawn straight (the staircase at
x 15220-15350, y 16880-17010), which track each drawn contact is on, and the audit's blind spots (dim metals,
contacts beside a metal). It took its own sample and did not rely on the audit.

**No findings** in `bd3`'s drawing. Checked and found correct: all 16 tracks by `tools/follow.py` and the
two-chip test `tools/tl5_tracks.py v` (the only stretches without metal are the drawn ones: T7 y 16870-16905, T8
y 16674-16729 and y 16916-16946, T9 y 16961-16990, T10 y 17004-17033; T5 starts at its pad; T15 ends at its
pad); the tight gaps (T7's pad to `wr_r12`'s corner is open poly; T10's arm to the `wr_r13` pad 9 px of bare
ground; bare ground between T8's two pads in all four shots; `wr_stb_n`'s corner clear of the pad
(14306,16778)); the staircase's three arms; all 37 crossings of the rows y 16560, 16650, 16732, 16778, 16862,
17036 with the tracks at 3-4x in three or four shots (plain except the drawn pads; each row ends as drawn); all
18 listed contacts real and on the stated track; line X over the strobe poly (no ring in either chip); eleven
clean-shot specks and a dot on the rail at (14432,16655) (residue: no ring); no undrawn metal on 16 cuts
(`tools/busl_mdrawn.py`) and two overlays; no lengthwise poly under any track but the drawn columns x 14912
and x 15214. Not checked by the reviewer: plain track stretches between rows at 4x (text tools and 1.7x only),
the gate columns' cells and rail contacts, under the wide rail, row ends east of x 15580.

Two geometry remarks on **other packages' lines** in this region (not `bd3`'s files; in the handoff as
proposals, nothing changed here): `sel`'s contact at T15's lower end, drawn (15560,17072) by its cell, has its
centre at about (15560,17082), and the metal ends at about y 17097 (drawn 17085); `trunks`' line X
(`trunks.txt:159`) is drawn along y 16992 and its centre is y 16998 (a metal test along y 16992 reads its north
edge and reports false breaks).

No trace line changed before or after the round. Recorded 2026-11-27 07:41 -0600.

Round 1: no findings.

### Round 2 (full review), 2026-11-28: run 3's pieces `rwr` and `buf`

A fresh Claude Fable 5.2 agent, on commit 1b59c905, images in `cache/scratch/bd3/review-2/` (12 used). Pieces:
`rwr` (the cell `bd3_rwr` at R12 and its copy at R13) and `buf` (the R12 select buffer's two pull-downs). Told
to suspect: whether the inverter's bar lies on field west of the ground rail (master and copy); both loads'
ties (the arm, the box, the plate's clearance); whether each load's strip reaches its supply land, and the
supply contacts; the field under the ground rail between the inverter's output band and the NOR's land (else
`rsel12_n` would be grounded) and the slivers' joins to the lands; the strip's edge lines at x 15639 and
x 15708; the output boxes as buried contacts and the output poly's C; every difference of the R13 copy (its
lower end, its output row y 17038, the strobe contact on T15); in `buf` a sliver beside the first inverter's
bar east of the rail, the channel's east edge under the rail, and the second inverter's edge lines.

**One finding, geometry only** (confirmed by the tracer, fixed):

- The NOR's gate B was drawn to x 15729, 3 px from the load's tie arm (x 15732), and gate A to the same x. The
  poly of both ends at the ground rail's east edge, about x 15721 (`px.py row 16779 15706 15740 2
  metal,metal1,acid1b`: dark x 15716-15722, plain 72/63/36 and 76-90/74-90 at x 15724-15728, the arm's own edge
  at x 15730-15734; `px.py row 16691`: dark x 15716-15724, field from x 15728). Both bars now end at x 15721;
  each still crosses the whole strip (to x 15708), and the arm is uncrossed (`px.py col 15740`: unbroken
  diffusion y 16722-16800). The inverter's bar does end at x 15729 (orange at x 15723-15726, row 16563) and is
  left. Does not change a connection.

  `tools/t.sh bd3 sameconn.py 1b59c905`: `connections identical`
  `.venv/bin/python tools/sameconn.py 1b59c905`: `connections identical`

Checked by the reviewer and found correct (4x in two to four shots, profiles and text maps): the inverter's bar
on field west of the rail in master and copy (no edge line across it x 15606-15654 in either metal shot, where
the NOR's bars have one at x 15636-15642; field north of it in both chip-2 shots, red minus green 1-6 against
15-25 on the NOR's slivers); field under the ground rail at y 16604-16632 (edge lines at y 16600 and y 16632
in both metal shots; the same at y 16908-16932 in the copy); the inverter load's tie (arm unbroken from the
wire to y 16540, one 12 px outline to the box with no field stripe, plain centre, poly continuous from box to
plate; the arm's and the plate's edges merge at x 15770-15778, both on `rsel12_n`); the NOR load's tie (arm
continuous with the band, foot reaching the box, a field stripe x 15753-15759 between arm and plate); both
strips unbroken tan to their supply lands, both supply contacts (ring and bright centre in both metal shots,
pits in the clean shot); the two output boxes (no metal above, plain centres) and the C-shaped output poly, with
field between the input bar and the column's top; the strip's edges x 15639 and x 15708; the R13 copy at +304
by overlay and by every profile repeated, its rows y 16862 and y 17038 continuous without taps, the pad
(15344,17036) clear of T10's corner, the strobe contact (15559,17084) real with T15 ending there; in `buf` no
edge across the first bar x 14824-14896 with field north of it and the clean shot's channel x 14776-14816, and
the second inverter's edge lines at x 14350 and x 14485 with diffusion on both sides between; the extraction
(0 errors, sizes as claimed, no uncertain join); the green areas `tools/opendiff.py` lists under the supply
rail are field.

Not checked (could not be): the joins that lie exactly in the ground rail's west edge line (the output wire to
the band at x 15660-15666, the two slivers to the lands), where the clean shot is inverted; only the narrowness
of the dark line there (4-6 px, against 12 px where a land ends) supports them. And that poly and diffusion join
inside each box, which is read from the box's form. Both are in "Ambiguities of run 3".

Recorded 2026-11-28 12:47 +0000.

Round 2: no findings that change a connection.
