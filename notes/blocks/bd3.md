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
- Not traced: anything south of y 17100 except T3-T6's corners and the R13 buffer. The
  loads of the three new right-hand cells are the schematic (`?`) loads of sel's cells.
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
| Right-hand gate column | x 15540-15890, y 16540-17360 | cell `sel_rwr` (from sel.txt) twice more: dy 600 (R12) and dy 900 (R13); then `sel_rbuf` at dy 2258 (R13 buffer) |
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

    rsel12_bufn = NOT rsel12        (right half; pull-down W/L 134/22, weak load 27/56)
    rsel12_buf = NOT rsel12_bufn       (left half;  pull-down W/L 135/22, load 64/31)

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

    rsel12_n = NOT rsel12     wr_r12 = NOR(rsel12_n, wr_stb_n)     gates at y 16556; 16682, 16772
    rsel13_n = NOT rsel13     wr_r13 = NOR(rsel13_n, wr_stb_n)     gates at y 16856; 16982, 17072

- rsel12: contact (15258,16560) on T8, poly east (in sel.txt).
- rsel13: T7 ends at a contact at (15214,16864); poly east along y 16862 to the inverter.
  The same poly also runs south from the pad along x 15216, directly under the metal
  that occupies T7's line below y 16902 (which is wr_r12), to y 17168, and east along
  y 17168 to the R13 buffer (below).
- Strobe gates: contacts on T15 at (15560,16772) and (15560,17072); T15 ends there.
- Outputs: poly west along y 16732 to a contact at (15258,16734) (T8's lower part starts
  there), and along y 17032 to a contact at (15344,17036) (a new line starts there on
  T10's x).

### R13 select buffer (right-hand column, y 17130-17360)

    rsel13_bn = NOT rsel13       rsel13_buf = NOT rsel13_bn

sel's two-inverter cell `sel_rbuf` once more (dy 2258 from its master; gate bars at
y 17168 and 17295, overlay at 1.5x). Output: buried contact at (15620,17340), poly west
along y 17340, then south along x 15512; seen to y 17700, still going.

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
| e_b | metal | 16167,16410 | in | input of the strobe's driver; joins trunks' `e_b` (x 16170, y 16400) |
| vss | metal | 16012-16065, 14990-15180 | - | rail the strobe driver's source sits on; only this piece drawn |
| vcc | metal | 14584-14634, 17100 (bottom); 14060, 16907-16954 (west) | - | supply rail and the wide rail |
| vss | metal | 15663-15718, 17100 (bottom) | - | ground rail of the right-hand column runs on |
| vcc | metal | 15795-15890, 17100 (bottom) | - | supply rail of the right-hand column runs on |

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
- Loads of `sel_rwr` (R12, R13 pairs) are sel's schematic `?` loads; at 1.3x the real
  load blocks are where the cell puts them. Exact outlines not traced.
- Pull-down diffusion of the two buffer inverters: the gate bars extend 50-70 px
  beyond the ground rail on the outer side with only slivers of diffusion visible above
  and below them; drawn as full-width transistors (W about 135). W is uncertain by 30%.

## Not done

- Around the strobe's driver (bd2's area): the other taps of `e_b`, where the rail
  x 16012-16065 comes from, exact outline of the drain (drawn from 2x and 3x views).
- Where `rsel12_buf` (poly x 14199, south of y 17700) and `rsel13_buf` (poly x 15512, south
  of y 17700) go.
- The right-hand column goes on below the R13 buffer: next gate bar at y 17427, fed
  from a contact at (15560,17430) on a metal line that comes up x 15560 from the south
  (not T15, which ended at y 17072).
- The tracks south of y 17100 and the west-going bundle beyond x 14100.

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

## Review

