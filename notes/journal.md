# Journal

## 2026-11-14 19:28  M0: groundwork and pilot

Done
- Both shots converted to raw arrays; acid shot resampled into the metal frame
  (`tools/align.py`: affine fit over 270 patches, 0.57 px RMS, residual after
  resampling under 1 px almost everywhere, 2.5 px worst case).
- `tools/view.py` (two-layer views with grid and trace overlay), `tools/tracelib.py`
  (trace format, cells and mirrored instances), `tools/netlist.py` (extraction, rule
  checks, static gate recovery), `tools/build.py` (SVG, netlist, report, floor plan).
- Layer legend worked out on real structures (`notes/layers.md`). The process has
  buried contacts; loads are recognised by their gate-to-output tie.
- Pilot: `trace/pilot.txt`, two gates at 14280-14640 x 14880-15300. Extracts with no
  errors as `a_out = NOT in_a`, `b_out = NOR(a_out, in_c)`. The first overlay fitted
  without correction. A mirrored instance fits the right-hand half of the column.
- Coarse floor plan from a 12-tile survey at 0.2x (`floorplan.txt`, 68 blocks, all
  provisional) and repeat pitches by autocorrelation.
- Provisional pad table (`notes/pads.md`).

Found
- Automatic segmentation is not usable for geometry (reason in `notes/layers.md`).
- The first circuit tried, the RES/LPSTB buffers by the top pads, is a poor teaching
  example because it lies under wide rails; left as AMB-001.
- The die has two kinds of array: horizontal bit-slices at 390.3 px (central and right
  datapaths) and rows at 477 px (left and mid-right arrays). The left array is about
  25 rows tall, more than the 14 bits of MA, so it is not simply one bit per row.
- Rough size: about 26,000 px2 per transistor in dense logic, which puts the chip
  near 5,000 transistors.

Tracing rate
- Not yet representative. Understanding the legend took about 25 views. Once
  understood, a 380 x 380 px region with five transistors took one pass of entry and
  one overlay check. Estimate to be revised after M1 and M2: 300-ish unique dense
  regions after allowing for repetition, a handful of views each.

Not done yet (planned for later milestones)
- Image-space check of cell instances against their master (start of M3).
- Coverage checks (metal or contacts in the photo with no trace over them).
- Rule checks beyond the basics: floating gates, undriven nets.

Next: M1, the pad ring. Start by following the metal plane from the VSS pad and the
rail from the VCC pad to confirm which is which, then each pad's buffer or driver.

## 2026-11-14 20:07  M1 in progress: pad ring

Done
- VSS/VCC confirmed. The top-middle pad sits in the peripheral plane (outer ring =
  VSS). The bottom-middle pad feeds the band inside the pad ring (inner band = VCC).
  With pin 1 fixed, the mix of plain inputs, outputs with drivers and bidirectional
  pads round the die matches the pinout in only one orientation, so the pad table in
  `notes/pads.md` is now firm.
- Output driver cell traced once (MA3) and instanced at all 23 output pads
  (`trace/pads_out.txt`); every instance extracts as two inverters plus a push-pull
  pair, pad = NOT(core signal). Details in `notes/blocks/pads.md`.
- Input side: five identical protection cells under the bottom-right pads, in pad
  order CLK, R/W, E, then RS and CS (which of the last two is which is not yet
  followed to the pads). Each is a wide long-channel clamp to the rail at y 18968.
- Buffer row above them (`trace/inrow.txt`), traced from the left so far:
  gate 0 inverter (input from the core in poly, output leaves left along y 18775),
  gate 2 three-finger inverter fed by CLK, gate 1 two-finger inverter fed by gate 2
  (so gate 1 output is buffered CLK, leaving left along y 19070 towards the block at
  9550-12300 x 19050-19950), gate 3 R/W inverter, gates 4 and 5 inverters in a
  chain, giving both polarities of R/W.

New tools
- `findcell.py`: finds copies of a rectangle anywhere on the die in all eight
  orientations. It can lock onto the wrong finger of a periodic structure (MA11);
  check every placement by overlay.
- `cellcheck.py`: side-by-side picture of each instance against the master. The
  bad-block percentage is only a rough guide; look at the pictures.
- `composite.py` + `view.py --comp`: per-pixel median over all instances of a cell.
  Removes etch residue, debris and metal grain. This is what made the logic under
  the VCC band readable. Use it for every repeated cell.
- `view.py --shift dx,dy`: look at another instance in the master's coordinates. Raw
  metal of a clean instance shows where metal really is (grain = metal).

Things learned about reading the die
- Two logic-cell styles. Small gates: load is a tall poly block (about 70 x 105) over
  a 27 px diffusion strip coming down from a VCC contact, W/L about 0.25; the block
  is tied to the output by a buried-contact box at its lower corner; outputs often
  leave through a second buried contact into a poly bar that becomes the next gate's
  input. Big buffers: load block beside a VCC diffusion strip with the channel
  running sideways under it (W/L about 1.8), and a two- or three-finger pull-down
  with a metal strap joining the outer diffusions.
- Under wide metal the acid shot is unreliable in any single instance (residue,
  fringes). Dark lines seen through metal are edges of poly or diffusion beneath.
- Keep rendered views under about 1400 px wide; wider ones are downscaled on read.

Open
- AMB-003: data pad cell, layers under the VCC band (parked until M2).
- AMB-001 can now be re-read: the RES/LPSTB buffers use the same big-buffer cell as
  gates 1 and 2 of the buffer row.
- Pad squares and the two supply rings are not drawn yet (only MA3's pad).

Next
- Finish the buffer row to x 17500 and the wiring below it (bus lines at
  y 18620-18750, four large rectangles at y 18575-18794, links to the protection
  cells and pads). Then RES and LPSTB, then the block left of the CLK pad.

## 2026-11-14 20:20  M1 status

Traced and extracting cleanly (290 transistors, no rule errors):
- 23 output drivers (cell `outdrv`).
- Bottom-right inputs: five protection cells (`inprot`), CLK and E two-stage buffers
  (`buf3f` + `buf2f`), R/W, RS and CS four-inverter groups (`ingrp`), R/W taps and
  their two diffusion rectangles, one unidentified inverter at the left end.
- Top inputs: LPSTB and RES two-stage buffers (`topin` + flipped `buf2f`).

Still to do for M1, in the order I would take them:
1. The block left of the CLK pad (9550-12300 x 19050-19950) and the wiring between
   it and the input row (12400-13700 x 18500-19600). `clk_b` arrives there on the
   metal at y 19056 (ends at a contact at 12570,19055); the CLK node itself also runs
   left on the metal at y 19103 and turns down at x 12615. A U-shaped poly joins the
   contacts at 12570,19055 and 12852,19103, which cannot be a plain link between
   those two metals, so there are transistors here that need 2.4x views. The block
   has two large multi-finger arrays (9570-10650) and tall rectangles that look like
   bootstrap capacitors (10920-11700 x 19350-19850). This is where the internal clock
   phases are made.
2. Wiring below the input row: strips from pads to protection cells and on to the
   buffers, RS and CS taps and rectangles, and the lines that leave to the right at
   y 18615-18750 (`rw_d`, RS node, `rs_d`, CS node).
3. The two comb protection cells by LPSTB and RES.
4. Pad squares and the two supply rings as drawn metal.
5. Data pad cell (AMB-003), after the bus-interface logic that drives it.

## 2026-11-14 21:25  Clock block

Result
- The main internal clock is NOT CLK. The CLK pin node runs along the bottom of the
  block and drives, through a single contact, a three-stage buffer built from the
  two big arrays: inverter (3 fingers of W 480), inverter (2 fingers), then a
  push-pull pair whose pull-up gate is the inverse of its pull-down gate. No gating,
  no division. Output `ck_out` goes up into the core at x 10845-10870 and away to
  the left at y 19240-19262.
- A gate row of six inverters buffers a global signal `inh_ck` into both polarities
  (lines A and B). Those go right into the core, and down into a "driver logic" of
  two mirrored circuits together with CLK. `inh_ck` was followed 4000 px along the
  bottom bus field to the foot of the left bus field; its source is not known.
- The driver logic is not traced (AMB-007).

Traced: 321 transistors in total, no rule errors. New in the tools: an `edges`
layer in view.py (outlines present in both photos), an annotation layer for
devices that are off in normal operation (`A ... kind=clamp|field`), and `@alias`.

Corrections to earlier work
- Input protection cells redrawn from 4x composites: the pad arrives in poly, a comb
  of buried contacts ties it to the node, and the wide band above is a thick-oxide
  clamp (AMB-005). The previous drawing had the pad strip as diffusion.
- The six "island" devices in the clock wiring are taken to be clamps to VCC
  (AMB-006).

Method notes
- Following one metal line across the die by eye is slow (about one view per
  1300 px at full scale). Lines in the bus fields should be traced as bundles when
  those fields are done, not one at a time.
- Big multi-finger devices are quick: columns of contacts and gate strips read
  directly at 0.9x, and a schematic rectangle per group is enough for the netlist.
- The decisive questions were all junctions: which poly reaches which contact.
  Each took one 5-6x view. Deciding early which junctions matter, and looking only
  at those, would have saved many of the survey views.

Next
- M2: bus interface and register decode. `rw`, `rs`, `cs` and `e` are ready at the
  input row; the decode array is at 14180-15780 x 13480-14680.
- Carry AMB-007 and the source of `inh_ck` as open items to pick up from the core.

## 2026-11-14 23:19  Second die, clock generator, register decode

Three shots of a second die were added and registered into the reference frame
(`tools/align.py`, layers `metal1`, `acid1`, `acid1b`). `acid1b` (hd6845acid2.jpg) is
clean and changes what is readable; its colour legend is in `notes/layers.md`.

Done, in the order agreed
1. Legend for the clean shot, calibrated on six known places. Two lessons: metal
   protects a margin beyond its edges (narrow gaps between lines leave only a thin
   dark bar), and the colours shift across the die (open diffusion is green near
   the edge, pink in the decode array), so the legend must be re-checked locally
   against structure.
2. Clock driver logic: it is a two-phase non-overlapping clock generator.
   `ck_a` = NOR(delayed `ck_b`, CLK), `ck_b` = NOR(delayed `ck_a`, NOT CLK). Traced.
   The earlier reading of this block from the chip-2 shots was wrong in several
   places; the note in `notes/blocks/clock.md` replaces it.
3. Data pad cell: re-read, much more established, still not traced. It has more
   logic than two inverters. Parked again with the facts listed (AMB-003).
4. Existing traces checked against the clean shot: gate groups, protection cell and
   output pre-driver agree; the two inferred joins in the clock output stage are
   confirmed.
5. Register decode array read (`notes/blocks/decode.md`): 18 columns, each a 5-input
   NOR, selecting R7 R6 R4 R0 R2 R1 R10 R5 R3 R8 R9 R11 R13 R12 R14 R15 R17 R16 from
   left to right. Read by measuring colour at every crossing, with four independent
   consistency checks.

Trace: 443 transistors, no rule errors.

Method notes
- Regular arrays should be measured, not eyeballed: at 2.7x my impression of
  which crossings had transistors was wrong in places where the colour measurement,
  backed by the consistency checks, was right.
- Phase correlation fails inside regular arrays, so `acid1b` registration there is
  interpolated. Calibrate row and column positions from profiles before sampling
  (`tools/pla_read.py` hard-codes the measured ones).
- A cell that resists two passes should be left until its inputs are known. The
  data pad cell cost about 25 views over two sessions without a consistent reading.

Next
- M2: row drivers of the decode array and the address register; the cells above the
  array; where the 18 select lines go; then the bus interface that produces the two
  lines into each data pad cell, and back to AMB-003.

## 2026-11-15 18:48  Parallel round

Twenty-six agent runs on seventeen blocks, each working from `notes/tracing-guide.md`
on its own files. The round ended when the usage limit was reached; the last eleven
runs were resumed after it reset and all reported. By the user's instruction, work
is serial again from here.

All blocks together: 2,593 transistors, no rule errors, no warnings (443 before the
round). Cross-block joins are in `trace/zz_joins.txt`.

Established by tracing
- Register decode rows come straight from a 5-bit address register (five transparent
  latches above the decode array); five inverters right of the array make the
  complement rows.
- Register strobes: `wr_rN` = (register N selected) AND NOT `wr_stb_n` for R0-R15;
  R12-R17 also have a buffered select (believed read enables); R16/R17 have no strobe.
- `wr_stb_n` is the output of a latch, open while E is high:
  `c = NOR(rw_d, m255, cs_d)` with m255 believed NOT rs_d, `n1 = NOT(qb OR (E AND NOT c))`,
  `qb = NOT(n1 OR (E AND c))`, `wr_stb_n = NOT n1`. Nothing traced closes the strobe
  when E falls. The address register's load strobe is
  NOT(NOT(x OR (E AND NOR(rw_d, rs_d, cs_d)))), x unknown.
- Horizontal registers in the right datapath, identified by following their strobes:
  R0, R1, R2 (8 bits each) and R4 (7 bits), each with an equality comparator
  (true XOR per bit, wired-NOR line) against per-slice `c` lines. R0 has a second
  comparator against R0 shifted one place (R0/2), 7 bits. No `c` line is driven in
  the right datapath: all leave at its lower left.
- Central datapath: static register rows (6, 5, 6, 8 bits, the last two readable onto
  an 8-line bus), two 5-bit comparators (one plain equality with one bit's register
  input replaced by a three-term function from the logic beside it; one with a ripple
  chain between slices), a 4-way selector with three latch rows. No counter found.
- Left array: the 14-bit memory address counter (incrementer with carry groups of
  7, 3, 4; dynamic node taking the incremented value or a load value; static stored
  bit; clear device). Reload path and bit numbering not yet traced.
- Mid-right array: 19 rows in groups of 4, 3, 4, 4, 4; an AND chain over a per-row
  node q with group look-ahead, toggle-like logic, a stage clocked by `ck_a` and
  `ck_b`; right-hand columns not traced.
- Global wiring: `ck_out`, `ck_a`, `ck_b`, E, R/W, RS, CS, RES, LPSTB mapped to their
  first entries. The clock block's `inh_ck` is not `ck_a`: it is the inverse of a
  core signal X, whose driver is an inverter in the gate column left of the select
  logic; X also gates a latch there.

Corrections made during the round (each was a wrong statement at the time)
- `inh_ck` = `ck_a` (mine, from a 1.1x view): no such link.
- "strobe = NOT E" (one agent): the line it followed is broken; settled by a second
  agent's measurement.
- "this row is R0" (one agent): a track-scanning tool bridged a jog; two later runs
  agree it is R2.
- Several briefs of mine guessed structure wrongly (address register position, data
  bus units per pad, "logic" that was a routing channel, eight slices everywhere).

What worked
- One file prefix per block, `TRACE=` isolation, a locked commit script, and a ports
  table per block. Joins show up as multi-name errors in the combined extraction and
  are resolved in one coordinator file.
- Independent re-derivation: both wrong identifications above were caught because a
  second agent reached the same wires from another side.
- Measurement over impression: colour profiles for junctions, grain for metal breaks.

What did not
- Yield per run: 60-80 images buys one or two cells in an array (100-250 transistors
  with repetition) or about 25 transistors of random logic.
- Track-scanning tools are not safe for connectivity (bridges at jogs, false breaks).
- The clean shot's colours are local; three blocks needed their own legend.

Next (serial, in this order)
1. Mid-right array, x 12770-13040 and its wiring channel: is q the stored bit of a
   counter, and do its 19 outputs become the `c` lines the horizontal and vertical
   comparators use? (Groups 4+3, 4+4, 4 would fit a 7-bit, an 8-bit and a 4-bit
   counter; that is a hypothesis.)
2. Where the R0, R1, R2, R4 match lines go (tracks k7, k8 of the strobe channel and
   onward): the horizontal control logic.
3. The lower half of the top-centre logic (source of the three signals that modify
   one comparator bit), and the cross-coupled group below the central datapath.
4. Memory address counter: reload path and bit numbering.
5. Remaining rows of both datapaths; data bus; pad ring; then simulation (M5).

## 2026-11-15 21:05  Serial again: the counters

After the parallel round, back to one block at a time (user instruction). Two requests
from the user during the session, both recorded in `PLAN.md` and `CLAUDE.md`: a "visual
6845" as a deliverable (so every transistor is to be traced, M7), and schematics that
show registers, comparators and counters as blocks plus one gate-level sheet per kind.

**Established**

- The mid-right array is three synchronous counters built from one bit cell: 8 bits
  (rows r11-r18), 7 bits (r4-r10), 4 bits (r0-r3). The cell is a master-slave pair:
  `na = NOR(L3, NOT m)`, master `a` takes `na` on the master clock, `p3 = NOT a`,
  `d = n1 = NOT p3`, slave `q` takes `d` on the slave clock; `m` is the next value, made
  from `q` and the carry. Extracted, 629 transistors, all 19 rows checked against the
  master in two shots.
- **The 8-bit counter is the horizontal character counter.** Its master outputs `n1`
  are the `c` lines of the R0, R1 and R2 comparators: six of the eight joins closed by
  geometry when the wiring channel was drawn (rdp3's and bd1's ports met mine), the
  other two are named in both blocks' notes. Bit 0 is the bottom row; in the right
  datapath slices s1..s7 are bits 0..6 and s0 is bit 7.
- **The comparators see the master, not the slave.** What leaves each bit is `n1`, the
  buffered master latch, which already holds the next count during `ck_b`.
- **The three counters have separate clocks.** The horizontal and the 4-bit counter run
  on `ck_b`/`ck_a` every cycle. The 7-bit counter's master and slave clocks are two bus
  lines from the west (E and D of the routing channel between r3 and r4), so it steps
  only when the logic there pulses them. Its outputs go to the upper right array (the R4
  and R6 comparators): the character-row counter.
- rdp2's unidentified 7-bit register "RF" is **R6**: its strobe line runs down track T0
  of the wiring channel into bd1's `wr_r6`.
- `ck_a` reaches the 4-bit counter by a diffusion cross-under, a tapless line through
  rows r10-r4 and a bus line; the same bus line carries `ck_a` on west.
- Fourteen cross-block joins closed by geometry (`trace/zz_joins.txt`); full extraction
  2,745 transistors, 0 errors, 0 warnings.

**Corrections to what was reported before**

- "`q` is a line from outside, so the array is probably not a counter" (third mra run,
  repeated in my last summary): wrong. The `q` poly ends in a buried contact on the slave
  pass gate. My own hypothesis in that summary (8 + 7 + 4 counters) is what the trace
  now shows.
- "The line x 12902 is `ck_b`" and "the rail x 13025 is `ck_a` for all 19 rows" (third
  run and trunks): both wrong. The first ends free above the `ck_b` contact and is fed
  from the top; the second is three pieces on three nets.
- My first drawing of L3 for rows r4-r10 had no feed (AMB-008). It has one: its widened
  lower end turns onto a contact I had given to the neighbouring line.
- Twice in this session the eye joined two diffusions in the clean shot that a colour
  profile showed to be 20 px of field apart.

**Tools and method**

- `tools/classmap.py` and `view.py --layers class`: false-colour class map of the clean
  shot (poly / channel / diffusion / field). It made the fourth column readable in an
  afternoon. Limits are in its docstring and in `notes/blocks/mra.md`.
- `tools/strips.py`: a long channel as strips side by side, any layer, with the trace.
- **Wiring channels must be read in the clean shot.** Poly runs hidden under the metal
  tracks for hundreds of pixels; the metal shot shows none of it. bd1's and bd3's
  channels were read mostly from the metal shot and should be looked at again.
- Where no metal lies above, the chip-2 metal shot shows diffusion directly.
- A through-line drawn "once, full length" by an agent is a claim about every routing
  channel it crosses. Three of those claims were wrong here. Check each crossing.

**Open, in the order I would take them**

1. The logic west of the counters (x 10400-11700 and the bands above row r0): it makes
   the row counter's two clocks (bus lines D, E), its L3 line (metal along y 13005), the
   carry-ins of r10 and r18, `cnt_gab`, and it receives the R2 match (bus line F/G) and
   `ck_a` (bus line C). This is the end-of-line / end-of-frame control: M4.
2. The rest of the bit cell: node `m`'s pull-up and the unresolved branch (B3, B4, load
   1 in `mra_col2`). Until then "next = q XOR carry" is believed, not extracted, and how
   a counter is cleared is unknown (L3 is `ck_a` for the horizontal counter, verified by
   following its poly in the clean shot, so the clear is not there).
3. North of the array (y < 7130): the 4-bit counter's outputs, `wr_r3`, `wr_r5`, L3 of
   r0-r3 and the VSS/VCC rails all leave there (`amr`, `rdp1`).
4. The east ends of the wiring channel that rdp2 saw and did not draw (row counter bits
   r4-r6, bus lines A, B, F), and the stretch between rdp3 and bd1 (bits r13, r14, r17).
5. Then as before: remaining datapath rows, data bus and pad cell (AMB-003), bd1/bd2/bd3
   re-read in the clean shot, top-left / left-centre / bottom logic, pad ring.

## 2026-11-15 22:59  West of the counters: the row counter's clock generator

Serial. Blocks `wl` (new, complete) and `bw` (new, wiring part-way). Full extraction
1,669 nets, 2,768 transistors, 0 errors, 0 warnings.

**What was established**

- West of the counters there is almost no logic: x 10850-11700 below y 9450 is a bus field
  of about twenty vertical metals. The logic is one block beside the 4-bit counter
  (x 11080-11660, y 6950-9150), 23 transistors, all extracted (`notes/blocks/wl.md`).
- **The character-row counter's two clocks are made there from one step pulse `p`** by a
  non-overlapping generator: slave clock = NOR(buffered master clock, p), master clock =
  NOR(NOT p, buffered slave clock). The two NOR drivers are 350 px wide with strong loads.
  So the row counter's master latches take the next count while `p` is high and its slaves
  pass it on when `p` is low again: one step per pulse of `p`.
- **`p` = NOR(a, b).** `a` is `inh_rc`, the same core signal whose other copy (`inh_ck`)
  holds `ck_b` low in the clock block: one signal stops both the horizontal counter's
  master clock and the row counter's step. `b` comes from far away: followed west along the
  central datapath's channel 3, north in a nested bundle at x 7790-7930, west through the
  crossing field x 6330-7700 to a contact (5838,7470) and up a metal x 5841 that goes north
  into the top-left logic (`notes/blocks/bw.md`).
- `ck_a` and the R2 match (the horizontal sync position) are taken west on the same
  channel; `ck_a` then goes north at x 7421, the R2 match ends on a metal at x 8340.
- The VSS rail of the block feeds mra's "rail x 11828" (mra's open point A4, closed).

**Corrections**

- mra's line x 12285 (`cnt_la_a`), "one metal through all nineteen rows, no contact", is
  three pieces cut at two of the four routing channels. The top piece feeds an inverter in
  `wl` and nothing found drives it: a contact has been missed in the rows (re-read R8).
- cdp2's note that the channel-3 lines "turn down" at their west end: they turn north.

**The user's instruction about revisits (2026-11-15)**

"Make sure the need to revisit is noted somewhere where it will be done later, and please
learn from this for the future." Done as: a **Re-read list** in `notes/work-packages.md`
(nine entries now, each a task with region and reason, to be worked off before M5), a
Re-read rule in `CLAUDE.md`, and traps 10-12 in `notes/tracing-guide.md`. A doubt about
earlier work goes on that list in the same commit; a remark in a report does not count.

**Tools and method**

- `tools/classmap.py --open`: where neither chip has metal, the class comes from the two
  chip-2 shots, which show open diffusion redder than open field. In the clean shot alone a
  wide open diffusion is only slightly greener than field (it had been read as field) and
  appears as pink boxes with heavy outlines between metals. With this the big drivers
  could be read in one pass.
- A crossing of a poly line under a metal in the clean shot shows a dark ring at each metal
  edge. That is the metal's margin, not a contact: a contact has a widened pad and a green
  dot. All five channel-3 lines cross twenty metals this way with no contact.
- Trap 11 struck again within the hour (`cnt_la_a`). Any line longer than one row group gets
  looked at where it crosses each routing channel before it is used.

**Open, in the order I would take them**

1. The source of `b`: the metal x 5841 north of y 6300 (top-left logic, `tl`). That is
   where the row counter's step is decided (scan line count, end of line): M4.
2. What `a` / `inh_ck` is: bd1's `inh_src`, which comes from the bottom bus field.
3. Re-read R8/R9 in the counters (the line x 12285 and node `z`), then the rest of the bit
   cell (node `m`'s pull-up, B3/B4): the counters' next-state and clear are still not
   extracted.
4. North of the counters (`amr`): the 4-bit counter's outputs, bands H0/H1/H4, `la_n`.
5. The bus field's own lines; the ends of the other channel-3 lines; then as before.

## 2026-11-15 23:24  The row counter's step followed to its gate

Serial. Blocks `bw` (route completed), `tla` (new, three gates). Full extraction 1,676
nets, 2,778 transistors, 0 errors, 0 warnings.

**What was established**

- `rc_stepreq_n`, the row counter's step, was followed to its driver: up the metal x 5841 to
  (5838,5585), west as poly through a second crossing field to (3518,5587), by metal to
  (3283,5238) and by poly to a buried contact on the output node of a gate at (2975,5035)
  in the top-left logic. About 9,000 px of wire from the counters, all drawn.
- That gate: **`b = NOR(in1, in2, in3)`**. Beside it: `in3 = NOR(e3, e4)` and
  `m2 = NOR(in2, in3)`. All three extracted (`notes/blocks/tla.md`). So the row counter
  steps when `in1` or `in2` is high, or when `e3` and `e4` are both low.
- `in1`, `in2`, `e3`, `e4` each lead on into bus fields: `in1` up a 2,200 px bus line and
  east along the top of the logic to another field at x 4140-4420; `in2` to a poly going
  west at y 5411; `e3` and `e4` onto two more bus lines. None reached a gate yet.

**What it means for the plan**

The top-left "logic" (2100-6400 x 2500-6350) is gate clusters joined by bus fields whose
lines are in pieces. Chasing one signal at a time does not converge there. It has to be
traced whole: every cluster, and every bus piece with its contacts. That is the bulk of M4
and it is large (my estimate: 300-500 transistors and several hundred wire pieces). It
would divide well among parallel agents (one cluster or one bus field each), which by the
standing rule needs the user's word.

**Method notes**

- Under a wide rail the clean shot shows field as pink with an olive stripe down the
  middle, and the class map paints the stripe as diffusion. It is not: diffusion under a
  rail is the tan boxes only. (Read as a continuous column at first; it would have made a
  transistor with VSS on both sides.)
- A load plate in the open shows the edges of the diffusion strip under it as two dark
  lines across the plate, so one plate over a 28 px strip looks like two or three plates.
  The chip-2 shots show it as one piece of poly.
- A bus line piece and the next piece at the same x can be 40 px apart end to end. Every
  bus line is followed in both shots; a 1x metal view shows one line.

**Open, in the order I would take them**

1. The cluster x 2440-3090, y 4590-5330 in full (R1's columns, the remaining loads, the
   column above gate E0, the thin metal's taps), then the vertical bus x 3090-3380 piece by
   piece, then the clusters above and below it.
2. The rest as listed in the previous entry (what `a` is; re-read R8/R9; `amr`; the bus
   field between datapath and counters).

## 2026-11-16 00:25  The step logic, three levels deep

Serial, block `tla`. Full extraction after this entry: see the ship line. User: "carry on
serially for now please. The NOR gates are intriguing and I would love to know what they
are doing."

**What was established** (all extracted, `notes/blocks/tla.md`)

- step = in1 OR (NOT e4 AND ((x1 AND NOT a2) OR NOT e3)), from seven gates:
  b = NOR(in1, in2, in3); in2 = NOR(w2, e4); in3 = NOR(e3, e4); w2 = NOT c1;
  c1 = NOR(a2, b1); b1 = NOR(x1, a2); and m2 = NOR(in2, in3), the complement of the
  bracket, which feeds further logic in the same column.
- The cluster is two mirrored columns of small NORs either side of a VCC rail, each NOR on
  a diffusion column beside a VSS rail with its load between the rails. It runs from
  y 2940 to 5330.
- `e4` is a global: 7,000 px followed, from the cluster to the left bus field at x 6559,
  still going south. Every contact on it so far is a gate.
- `e3`, `a2`, `x1` all come from the east (y 2728, 3761, 3547); `in1` from the bus field
  at x 4279.

**Not established**: what any of the five inputs is. The reading "end-of-line strobe and
scan-line comparisons" is a guess from the formula's shape.

**Corrections**

- The round blob at each load's lower corner is the load gate's buried-contact tie, not a
  metal contact to the thin metal (I had drawn in3's node onto the thin metal).
- Bus line A's pieces A1 and A2 are 35 px apart end to end, with the gate poly visible
  between their pads: settled at 6.5x in both chips. Had they been one piece, c1's output
  would have been tied to its own input.

**Tools**

- `tools/tla_tracks.py`: where a track has metal; `tools/tla_contacts.py`: contact
  candidates on a track from the clean shot's colour. Both only say where to look.
  The contact finder missed A2's third contact (3103,3762) on the first pass because the
  line's x drifts 8 px along its length: profile at the measured x of each stretch.
- `strips.py --layer class`: 3,000 px of a bus in one image, pieces, crossings and contacts
  all visible.
- A net with gates on it and no driver means a contact is still missing: it found A2's.

**Open, in the order I would take them**

1. `e4`'s source: on south down the left bus field (x 6559 from y 8850); and from the
   other side the R0 match line on bd1's k7/k8 (re-read item R1 covers that channel).
2. The rest of this cluster: y 3400-4590 east, the west side above y 4940, b1's load.
3. `in1` (bus field x 4140-4420, then the middle or right gate column), `e3`, `a2`, `x1`
   to the east.
4. As before: what `a` (`inh_rc`) is; re-read R8/R9; `amr`; the bus fields.

## 2026-11-16 01:00  The chase of e4

Serial, blocks `tla`, `trunks`. Full extraction 1,683 nets, 2,789 transistors, 0 errors,
0 warnings. User: "shall we carry on then?"

**Aim**: name `e4`, the input that gates the whole step logic. **Not achieved.**

**What was established**

- `e4`'s net is drawn end to end: 17,000 px from the top-left cluster to a gate in bc1's
  left column at (7317,15435). It has five loads, all gates; its driver was not found.
- It is not RES and not `m2` (both looked possible; both refuted at high zoom).
- `res_b` and `lpstb_b` are traced to their ends: lines 3 and 4 of a five-line poly bus at
  x 5100-5290, where `e4` is line 5. From there all five go east together.
- bc1's 13-line bus line y 14526 is two nets split at x 7012/7100.

**Tools**

- `tools/follow.py`: follows one metal line through corners and diagonals using both
  chips' metal shots. Tested on four hand-traced lines. Two faults found and fixed in use:
  it bridged a gap before looking for a corner (stepping onto the next line of a
  staircase), and its corner test did not bridge the 4-8 px step line where metal comes
  off a poly edge. One fault remains: it can miss a corner right at a contact-rich end
  (it ended `res_b` 20 px short of its last turn). Ends are looked at by eye.
- `tools/xfield.py`: contact colours over a crossing field. Not usable where there are no
  pads (the colour drifts by the row); kept for fields with pads.

**What went wrong and what I changed**

- I followed the wrong net for 2,500 px (the eastern half of bus line y 14526) because a
  1.9x strip showed one continuous line; it is two pads 90 px apart. Caught when the
  metal shot at 5x showed the pads' metals going different ways.
- I nearly reported "e4 is RES" on the strength of a 217 px overlap and a tool's end
  point. Traps 13-15 in the tracing guide are from this.

**Assessment**

Chasing one signal from its loads does not find its driver in this part of the die: the
nets are long, cross three bus fields and have no landmarks. Two days of serial work have
given the step formula and five well-drawn but unnamed inputs. Naming them needs the
regions they come from traced as wholes: the top-left clusters (where the scan line
counter probably is), bc1/bc2 and the gate column of bd1. That is the same conclusion as
on 2026-11-16, now with tools that make the bus fields cheap.

**Open, in the order I would take them**

1. Finish the `tla` cluster as a block (about twenty gates), using the unit structure and
   `follow.py` for its bus pieces; then the cluster's twin columns at x 3450-3900 and
   x 4650-5050.
2. bd1's gate column (re-read R1): it holds what the R0 match feeds and what makes X.
3. The poly bus's other four lines east of the pads, and the diagonal fan.

## 2026-11-16 01:23  Signal names

The user asked whether signals were being renamed as they were understood (they were
not: only joined by alias), and then: "one of the aims here should be to ensure that all
labels are meaningful, or at very least are described in a table if it's hard to name
them. Make sure that all the documents reference the correct names."

Done, at the source:

- 672 net names renamed in the trace files (labels, templates, tags, aliases): counter
  bits (`hc0`-`hc7`, `rc0`-`rc6`, `hsw0`-`hsw3` and their nodes), registers and comparators
  by register number and bit (`r1_b3_q`, `r0c_b5_x`), match lines (`h_eq_r0`...), write
  strobes (`wr_r6`), the row counter's clocks and step (`rc_ck_m`, `rc_step`,
  `rc_stepreq_n`), the inhibit signal and its copies (`inh_n`, `inh_ck`, `inh_rc`,
  `inh_lat`), bus control (`wr_data_sel`...). Extraction unchanged: 1,683 nets, 2,789
  transistors, 0 errors, 0 warnings.
- The same table applied to every note, the plan, the instructions and the floor-plan
  descriptions (771 replacements). **This journal was rewritten too**: entries above use
  the new names. The old names are in "Former names" at the end of `notes/signals.md`.
- `notes/signals.md`: the glossary. Every one of the 1,526 named nets is covered by a row
  (name or pattern) saying what it is or, for a placeholder, what is known. `tools/build.py`
  checks it and reports names it does not cover (now 0).
- Convention `NAME_u` for a wire believed to be NAME whose join is not drawn. The rename
  exposed 14 such open joins that had been hidden behind unrelated-looking names; they
  are listed in `notes/work-packages.md`.
- Overlays and the SVG now show the canonical name of a net at every label.
- `tools/rename.py OLD NEW` for every later identification; `tools/signals.py` for the
  check on one block.

Not renamed: the central datapath rows, the left array and the two small logic blocks,
whose registers have no numbers yet. Their names stay by place and are described in the
glossary.

## 2026-11-16 02:03  Floor plan, names, and the step logic two more levels deep

Serial, no agents (user: "while unsupervised, just work serially"). The user asked for the
floor-plan labels to be tidied, for tracing to continue, and "let's see if later on new
discoveries reveal the nature of e4". Full extraction at the end: see the ship line
(2,810 transistors at the last build, 0 errors, 0 warnings).

**Housekeeping done**

- Floor plan: labels are placed inside their own block clear of smaller blocks and of each
  other; blocks too small for a name get a number and a legend panel; names made consistent;
  superseded coarse blocks dropped; `out/floorplan_legend.txt` lists every block as text.
- Signal names: see the entry above ("Signal names"). The glossary check is part of the
  build and stays at zero uncovered names.
- Two open joins closed by drawing them: `h_eq_r0` and `h_eq_r1` between the right
  datapath and the strobe channel. `h_eq_r1` and `inh_lat` followed on, through the bottom
  bus field, to poly lines entering the bottom-centre logic at (10940,17598).

**The step logic (block `tla`)**

- Corrected formula: **step = in1 OR (NOT e4 AND NOT (e3 AND a2))**. `b1` has a third
  pull-down that the first pass missed (a strap from an inverter of NOR(e3,e4) to a gate
  hidden under a thin metal), which removes `x1` from the step.
- `in1` = NOR(`rcs_mu`, `rcs_mv`) is made in the middle cluster (x 3450-4110), a twin of the
  first; `rcs_mu` is an inverter there.
- The step condition does not only go to the step gate. `rcs_cond` = NOT e4 AND NOT(e3 AND
  a2) is sampled by a pass transistor into a dynamic latch (`rcs_cond_lat`) and gated into
  an AND-OR-INVERT (`rcs_n4200`) by a strobe, `clk_tl` (one junction of this is
  AMB-009).
- That strobe was followed to its far end: 4,500 px, out of the cluster's foot and south
  down x 2457 to the **left column beside upper row 2 of the left array** (`larr`).
- So the vertical logic is: three gate clusters at x 2450-5050, y 2950-5450, plus the nine
  upper rows of the left array and their left column. About 34 of perhaps 75 gates of the
  clusters are not traced; the upper rows are not traced at all.

**e4**: still not identified. Nothing found today names it. Its driver is not in the
first cluster; every contact on its 17,000 px is a gate.

**Method notes**

- Where no metal lies over a structure, read it in the **chip-2 shots at 6-7x**: poly bands
  are crisp, and a diffusion edge shows as a dark line running across the bands. The clean
  shot is poor there (it is the shot for what was under metal).
- A poly that ends inside a diffusion without crossing it, inside a ring, is a buried
  contact; one that crosses with the diffusion's edge lines visible through it is a gate.
  Class runs down the diffusion (`classmap.classify` on a 7 px column) tell the two apart
  where a thin metal hides them.
- Check a newly extracted gate for sense. `rcs_cond` first came out as NOR(strobe, m2)
  feeding a gate with the term (strobe AND that NOR), which can never be true: that is
  what exposed the pass transistor reading.
- `tools/follow.py` now stops when it returns to a corner it has turned (it was started on
  a wide rail and looped).

**Open, in the order I would take them**

1. The left column beside the upper rows of the left array (x 2480-2860, y 6700-10900) and
   those nine rows: where `clk_tl` comes from. With them the scan-line side of the
   vertical logic should become nameable, and through it e3, a2 and e4.
2. The remaining units of the three clusters, unit by unit (first cluster: y 3690-3800,
   4320-4535, 4830-5330 east; the whole west column above y 4940).
3. The gate column of the strobe channel (y 15860-16125), where `h_eq_r0` is sampled on
   `ck_out`: observations are in `notes/blocks/bd1.md`.
4. The bottom-centre logic, which receives `h_eq_r1`, `inh_lat` and e4.

**Addendum, same session: the strobe has a driver.** The strobe (former name `rcs_bb3807`) is now `clk_tl`:
it is the output of an inverter at (2626,7908) in the left column beside upper row 2 of
the left array (traced, extracted: `clk_tl` = NOT `ck_out`). The left column there is
the downward continuation of the first cluster's west side (same VSS and VCC rails, same
"rail gate" inverter as `rcs_w2`). Its input `ck_out` comes down a metal at x 2370 from
a contact (2365,5847) at the foot of the first cluster and carries on south at x 2500.
A signal that is made in one place, run 2,000 px, inverted locally and run 2,200 px back
is being distributed like a clock; which signal it is, is the next thing to find, in the
small cluster at y 5650-6300.

**Second addendum: the strobe is the clock.** Following the inverter's input (not its
output) with `tools/follow.py` gave the answer in one call: the metal that leaves the
inverter's pad southwards runs 17,238 px down the left edge and along the bottom to the
clock block. It is the left-edge trunk of `ck_out`, which trunks had drawn only to
y 18300. So the inverter's input (former name `rcs_stb_n`) **is `ck_out`** and the strobe is `clk_tl` = NOT `ck_out` (CLK
polarity). Joined by geometry (the missing 10,300 px of trunk are drawn; the extraction
merged the two nets with no warning) and renamed everywhere.

What that settles: the step condition `rcs_cond` is latched while CLK is high. What it
does not settle: e3, e4, a2 and in1 are still unnamed.

Lesson: when a net has only gate loads, follow the *input* of whatever drives it before
giving up, and try the follower from the far end of any long line a trace left unfinished:
`ck_out`'s trunk "followed at 1x to y 18300" was 10,000 px short of its end.

## 2026-11-16 08:42  Two more counters, their clock generator, and the upper right datapath

Serial. New blocks `ur`, `urch`, `rdp1`, `slbus`. Full extraction 2,014 nets, 3,364
transistors, 0 errors, 0 warnings. User: "let's continue".

**What was established**

- **The nine upper rows of the left array are counter bits**: nine copies of the mid-right
  array's bit cell (`tools/findcell.py`, scores 0.88-0.92). A 4-bit counter (rows u0-u3)
  and a 5-bit one (u4-u8), plain ripple chains, sharing one master and one slave clock.
- **Their clock generator is a second copy of the row counter's**, in the left column
  beside rows u0-u2 (found the same way; the generator is now a shared cell). Both
  counters step once per pulse of `lc_step`, which comes from the left-centre logic.
- **The 5-bit counter is the scan line counter** (`sl0`-`sl4`). Its five output lines were
  followed and drawn 9,000 px east, through the central datapath's channel 2 (unused
  there), to the comparator of R5 in the upper right datapath.
- **The upper right datapath's top rows** (`rdp1`) are built from the cells of the rows
  below: R6's comparator, R7 and its comparator, and a top row holding **R5** (5 bits) and
  **one nibble of R3** (4 bits), each with a comparator. 284 transistors by instancing.
  Strobes `wr_r7`, `wr_r5`, `wr_r3` followed in; `rc_eq_r6` joined to the strobe
  channel's track k4.
- **The mid-right 4-bit counter is the horizontal sync width counter** (`hsw0`-`hsw3`):
  its four outputs end under the counter tracks of R3's comparator.
- **Bit order of the upper right array**: slices left to right are bits 0-6. Names of R4,
  R6, R7, R5, their comparators and the lines `ubus`, `uc` now carry bit numbers.

So the registers found so far: R0, R1, R2 (lower right), R4, R6, R7, R5, R3-nibble (upper
right), all with equality comparators. Still to find: R9 and the cursor and start-address
registers (central datapath), R3's other nibble, R8.

**Mistakes caught**

- Instancing the clock generator put its input contact on the neighbouring metal
  (`clk_tl`); the first extraction said "the scan line counter is clocked by CLK". The
  overlay showed the real pad one track to the west. Per-copy differences of an instanced
  cell must be looked for at every port, on the overlay, before the extraction is read.
- The last comparator slice of a group came out as "x = NOT nor": its series pair ends on
  a VSS land of the next slice's rail, absent at a group's right end.
- A straight "c track" profile showed a gap in every latch row; it is a jog of the track,
  the same in every row, not a break.

**Method**

- **`findcell.py` first.** Three blocks today (252 + 16 + 284 transistors) came from
  cells already traced. Before tracing any regular-looking region by hand, try every known
  cell against it, in all orientations.
- `tools/rowstrips.py`: the same strip for every row of an array in one image.
- Poly lines that change line position in a knot: check the result against an independent
  expectation (here: bits must come out in order across the slices).

**Open, in the order I would take them**

1. Where `lc_step` is made (left-centre logic, at about (5030,7000-7150)): the scan line
   counter's step. And the scan line counter's other comparators (R9 at least): its lines
   pass channel 2 unused, so R9's comparator takes them elsewhere, or they are tapped
   further west (the pads at x 4925-6196, and the vertical poly bus they cross).
2. `rdp2`'s routing zone (y 9080-9560): joins the row counter to the `uc` lines, closing
   `rc_eq_r4/r6/r7` against `rc`.
3. Where the match lines go: `sl_eq_r5` (north), `hsw_eq_r3`, `rc_eq_r7` (west),
   `rc_eq_r6` and `h_eq_r0` (strobe channel gate column), `h_eq_r1` (bottom-centre).
4. The rest of the step-logic clusters; the 4-bit left counter's outputs; `e4`.

## 2026-11-16 10:48  the row address selector; `inh_src` is a bus line

Questions from the user: is the scan line counter put out directly as RA0-4; how do the
R5 and R9 compares work; what makes VSYNC width 0 special. And two sets of questions on
jsbeeb issue 1866 (write strobe and E, R8 skew path, compare phase, shortest CLK pulse,
what `inh` does).

**Found**

- **The scan line counter does not go straight to the pins.** Its five lines are tapped
  at x 7120-7337 and feed a column of eleven pass transistors (`trace/ras.txt`,
  `notes/blocks/ras.md`): one gate line passes `sl` k to output k, the other passes `sl`
  k to output k+1, and output 0 has two more gated sources. A shift by one bit with a
  separate bit 0: the shape of interlace sync and video. 3,375 transistors, 2,025 nets,
  no errors.
- `inh_src` followed 3,700 px west from the strobe channel and drawn: a bottom-bus line
  with four branches, three still open (`notes/blocks/trunks.md`). Not made locally.
- RA0's and RA1's pad driver inputs followed from the pads to x 15300, y 4140-4800,
  where they meet metals from the west (not drawn; `notes/blocks/trunks.md`).

**Not found**

- The selector's outputs are not joined to the pads (gap: x 7860 to 11650 along
  y 4450-4800) nor to the central datapath's channel 1, towards which a nest of metals
  east of the column turns. If channel 1's lines are the selector's outputs, R9, R10 and
  R11 are compared with what goes to the pins, not with the counter. Open.
- R9's comparator: still not identified. Candidates are the central datapath's rows A
  (five latches) and B (5-bit comparator on the through tracks).
- R3's high nibble and the 4-bit counter `c4l`: nothing new.

**Method**

- A structure with no supply rail over it is worth a second look before assuming gates:
  this column is pass transistors only.
- The strip pattern was plain in the chip-2 stripped shot at 2.5x and unreadable in the
  clean shot at 4.4x (narrow diffusion fingers between two edge lines print black
  there). Try the other stripped shot before zooming further.

**Open, in the order I would take them**

1. The selector's five outputs to their ends, and the nest of metals at x 7530-7715 into
   channel 1; then the two gate lines and bit 0's extra sources (interlace logic).
2. Where `lc_step` is made; where `sl_eq_r5` goes.
3. `inh_src`'s three open ends.
4. As before: `rdp2`'s routing zone; the other match lines; the step-logic clusters;
   `c4l`'s outputs and R3's high nibble; `e4`.

**Later the same day.** All five selector outputs leave east as poly lines (y 4765, 4893,
5133, 5262, 5392) into a column at x 7860-8100 that is not traced. `ras_o3` also runs,
through the nest of metals east of the selector, onto a line of the central datapath's
channel 1; with the five channel lines drawn to `cdp2`'s, the extraction makes
`cdp2_trk_s7` and `ras_o3` one net. So the central datapath's 5-bit comparator (rows B,
against row C's register) sees the selector's output on at least that bit. Lesson for
the method: a named net of one block turning out to be a named net of another is
reported by the extraction as "carries several names"; that message is the join being
confirmed, and the fix is one name (`tools/rename.py`, or `@alias` where the name comes
from a cell template).

## 2026-11-16 11:18  correction: `cdp2_trk_s7` is not `ras_o3`

Yesterday's last commit joined `ras_o3`'s pad (7577,5262) to a metal that only passes it
(trap 16, R11). Corrected in the trace and in `notes/blocks/ras.md`. What stands:

- No selector output goes anywhere but into its own unit of a column of five identical
  units at x 7860-8100 (`rax`, not traced).
- Each unit has a second pad; the five lines from those pads are now all drawn and the
  extraction joins them to `cdp2`'s comparator tracks, bit 0 on slice s7 up to bit 4 on
  s3. That order is the one `cdp2`'s magnitude chain needs.

What made me look again: the result did not fit (output 3 on the slice that should be
bit 0), and the unit's second pad looked like an output. A result that breaks a regular
pattern is a reason to re-test the join that produced it before writing it up.

**Same day, later: the row address lines to the RA logic.** The five lines that feed the
central datapath's comparator (`rax_o0`-`rax_o4`) do not stop there: each goes on east of
the comparator, north 1,500 px, under a supply metal, east 2,000 px along the top of the
right-hand arrays and into a band of logic at x 13990-15500, y 4300-4520, out of which
the RA pad drivers' inputs come (`trace/rab.txt`, `notes/blocks/rab.md`). So the path of
a row address bit is: scan line counter, selector (`ras`), unit (`rax`), then both the
cursor-style comparator and, through one more band of logic (`ral`), the pin. Two blocks
on that path are untraced (`rax`, `ral`).

Mistakes of earlier blocks found on the way and corrected: `cdp2`'s line 6000 does not
end at x 10518. Method note: `tools/follow.py --gap 50` bridges real gaps (it joined a
pad at (7900,4372) to a rail 40 px away); keep the default 24 and look at every reported
corner near a rail.

**Same day: the units and the stage in front of the pads.** `rax`: the pull-down of each
unit drawn (five transistors); taken to be inverters (AMB-011), load not traced. `ral`:
the band in front of the RA pad drivers is five copies of one cell, and
`tools/findcell.py` finds the same cell fourteen times in the left array's untraced left
column, in front of the MA drivers. Ports read, cell not traced; it looks like the
register rows' static latch on a strobe line (`notes/blocks/ral.md`). `bd2`: looked for
where `wr_data_e_n` goes (the write-strobe question of jsbeeb issue 1866): it leaves on a
strap between two poly pads, destination not read.

**Open, in the order I would take them**

1. The `ral` cell (twenty copies: RA and MA outputs), then its strobe and force lines to
   their sources.
2. `bd2`'s gate group east of the rail: `wr_data_e_n`'s destination.
3. `rax`: the load and the east half of the unit.
4. The selector's two gate lines and bit 0's extra sources (interlace logic).
5. As before: `lc_step`; `sl_eq_r5`; `inh_src`'s three ends; `rdp2`'s routing zone; R3's
   high nibble and `c4l`; `e4`.

## 2026-11-16 13:15  R8, R9, R10, R11 identified by their write strobes

The user doubted that the 7-bit row with the comparator is R10. Settled by tracing
instead of by elimination: the four strobe tracks T3-T6 followed 11,000-14,000 px each
to the central datapath (`trace/wrs.txt`, `notes/blocks/wrs.md`). The extraction joins
`wr_r8` to `cdp1` row A (6 bits), `wr_r9` to `cdp1` row C (5), `wr_r11` to `cdp2` row A
(5), `wr_r10` to `cdp2` row C (7). 2,021 nets, 3,380 transistors, no errors.

So the 7-bit row is R10 (five raster bits and two cursor mode bits), and **R9's
comparator is found**: `cdp1`'s row B, traced weeks ago without a name. One of its five
bits does not take the register bit but the output of the island `tc1`, switched by
`ras_shift`: the place where interlace changes the R9 compare. Its compare value comes from
the RA pad drivers' input lines (followed, not drawn), not from the lines R10 uses.

**Method**

- An identification "by elimination" is a guess. Where a register row's strobe can be
  followed to a decoder line, do that first: here it took four follower runs.
- `tools/follow.py` does not report diagonals (tracing guide, tools).

**Open, in the order I would take them**

1. R9's five compare-value lines to their sources; `ras_shift`, `tc1_g`, `ras_o0_alt1`.
2. The `ral` cell (twenty copies) and its strobe.
3. `bd2`: `wr_data_e_n`'s destination.
4. The selector's gate lines; `rax`'s load; then as before.

**Same day: what R9 is compared with.** The five compare-value lines of R9's comparator
drawn end to end (`trace/r9c.txt`): they are the outputs of five units near the right
edge, below the RA4 pad driver, whose gates are the pad drivers' input lines. The
extraction joins each to one comparator input (bit 0 at slice 5 ... bit 4 at slice 1)
and, for RA0 and RA1, the unit's gate to the pad cell's own input net. So R9 is compared
with the row address at the pins, one stage later than R10. 2,024 nets, 3,385
transistors, no errors; three new open joins (RA2-RA4's lines to the pad cells).

Method: the same five-line bundle had been taken for "data bus interface" in the floor
plan because it ends beside the data pads' column. A coarse floor-plan label that
nobody traced is not evidence of anything.

**Open, in the order I would take them**

1. `ras_shift`, `tc1_g`, `ras_o0_alt1`: the three inputs that switch bit 0 of the R9 compare.
2. The `ral` cell (twenty copies) and its strobe: it sits between R10's and R9's view of
   the row address.
3. `bd2`: `wr_data_e_n`'s destination. Then the selector's gate lines, the loads of `rax`
   and of the R9 units, RA2-RA4's lines.

**Same day: the selector's controls are the island's outputs.** The five polys that leave
the nine-gate island `tc1` southwards are the selector's two gate lines, the gates of bit
0's two extra pass transistors and one of bit 0's alternative sources (`trace/ras.txt`,
last section; five joins in the extraction, 2,019 nets). The island's letters got the
selector's names. Result: `ras_straight` = NOT `ras_shift`; in shift mode R9's bit 0
selects which of two signals is put on row address bit 0 (`ras_o0_sel1` = shift AND bit,
`ras_o0_sel2` = shift AND NOT bit), and the R9 comparator's bit 0 is switched to the
inverse of the same signal. `notes/blocks/ras.md`.

Mistake found on the way: `ras_o0_sel1`'s metal had been drawn along a bus line the
follower jumped to (24 px gap). Tracing guide and R11 extended.

**Open, in the order I would take them**

1. The driver of `ras_shift`, and `ras_o0_alt1`, `ras_o0_alt2`, `tc1_g` to their sources:
   the interlace mode and the field signal.
2. The `ral` cell (twenty copies) and its strobe; the loads of `rax` and of the R9 units
   (they fix the polarity of the bit-0 compare).
3. `bd2`: `wr_data_e_n`'s destination.

**Same day: the mode line is the AND of two bits of R8.** `trace/shm.txt`: a NAND and an
inverter in the slice-0 position below R8's row; their inputs are the outputs of R8's
bits in columns c6 and c7, which reach the island's metals ns5 and ns6 along two of five
lines above the row (two poly cross-unders each). 2,019 nets, 3,390 transistors. The
chain is now extracted end to end: R8's two bits, the mode line, the selector's shift,
the choice of bit 0's source by R9's bit 0, and the switch of the R9 comparator's bit 0.

**Open, in the order I would take them**

1. `ras_o0_alt1`, `ras_o0_alt2`, `tc1_g`: the two signals that can become row address
   bit 0 (the field), followed only to pads at (7078,5303)'s metal, (6922,4787) and
   (6985,4958).
2. Where `ra_eq_r9` (R9's match) goes: leaves west along y 4459.
3. The `ral` cell and its strobe; the loads of `rax` and of the R9 units.
4. `bd2`: `wr_data_e_n`'s destination.

## 2026-11-16 16:04  correction: `tc1_i` is not `ras_o0_alt1`; two inverters west of the selector

Yesterday's "five joins" between the island and the selector were four. The fifth
(`tc1_i` = `ras_o0_alt1`) was a `?` poly of my own drawing, reported as extracted (trap
17, re-read item R12). Corrected in the trace, the notes and the glossary: the island's
input i comes from an inverter (`trace/fld.txt`), as does its input g:
`tc1_g` = NOT `fld_a_in`, `tc1_i` = NOT `fld_b_in`. 2,022 nets, 3,394 transistors.

So the statement "in shift mode the comparator's bit 0 is fed from the same signal that
becomes row address bit 0" is **not established**: the selector's two sources and the
comparator's two inputs are four nets, all of which lead into two untraced gate groups
west of the selector (`notes/blocks/fld.md`).

**Open, in the order I would take them**

1. `fld`: the upper group's west part and the lower gate group (field logic).
2. Where `ra_eq_r9` (R9's match) goes.
3. The `ral` cell and its strobe; the loads of `rax` and of the R9 units.
4. `bd2`: `wr_data_e_n`'s destination. R12.

**Same day: R9's match followed to the step logic.** `ra_eq_r9` runs 9,000 px west and
north-west (three poly cross-unders, the top line of the bus above the selector, up
x 5974, along y 2640) and comes down x 4192 into the middle cluster of the row counter's
step logic, ending 12 px from the metal of `ra_eq_r9`, the input of the term
`rcs_in1` of the step. Whether it is on that net is not decided (AMB-013): another line of
the same bundle ends on that contact. Not drawn (`notes/blocks/r9m.md`).

Also: `tools/unsure.py` (R12) finds 57 nets joined only through `?` items, among them
the four nets of the write-strobe latch in `bd2`.

## 2026-11-16 16:32  row address bit 0 in interlace sync and video comes from the row counter

`trace/fld.txt`, `notes/blocks/fld.md`. 2,026 nets, 3,408 transistors, no errors.

- The lower gate group west of the selector is **two copies of the comparator's XOR
  cell** (`tools/findcell.py`, scores 0.88-0.91); instanced, ports checked on overlays.
- Their A inputs traced end to end, 4,000-10,000 px each, through the central datapath's
  channel 2: `ras_o0_alt1` = `rc0_n` XOR `fld_y_b`, where `rc0_n` is the inverter I2 of
  the west logic and its input is **the character row counter's bit 0**; and the
  comparator's bit-0 input `tc1_i` = NOT(`cnt_la_a_n` XOR `tc1_g`).
- Channel 2 has a knot at x 7860-7960 where every line steps down one position. Taking
  each y for one line gave the wrong sources at first; caught by looking at an apparent
  gap in one line (R10 extended).

Open ends on this path: `cnt_la_a` (R8: the metal x 12285 through the counter rows; its
top piece ends at the bottom edge of `rc0`'s row), `fld_y_b`, `fld_a_in`, `ras_o0_alt2`.

**Open, in the order I would take them**

1. `fld_y_b`, `fld_a_in`, `ras_o0_alt2` to their sources; R8 in row r10.
2. R9's match (`r9m`): draw it, settle AMB-013 through the bundle's first line.
3. The `ral` cell and its strobe; loads of `rax` and of the R9 units; `bd2` (R12).

**Same day, later.** A third gate below R8's row: `tc1_x1` = NOT `ras_o0_sel1`
(`trace/shm.txt`), a line the island's notes had as "only passes through". It goes on
into the west part of `fld`'s upper group, which is therefore the next piece: it sits
between `tc1_x1` and the still unsourced `fld_a_in`, `fld_y_b`, `ras_o0_alt2`. I did not
join `tc1_x1` to `fld_a_in` although the first view suggested it: they are two lines.

## 2026-11-16 17:02  the bit-0 sources followed to a gate group west of the island

`trace/fld.txt`. 2,030 nets, 3,413 transistors, no errors.

- `fld_a_in` and `fld_y_b` drawn end to end (1,500 and 2,300 px, two poly cross-unders
  of the six-line bus each) to one gate group at x 6380-6700, y 3880-4220: a series pair
  pulls `fld_a_in` low, a single gate pulls `fld_y_b` low (loads untraced, AMB-014).
- The three inputs of that group (`inh_ck`, `tcw_b`, `tcw_c`) come on thin metals from the
  next rows north. The region west of the island is one untraced block (`tcw` in the
  queue); it is where the field flip-flop has to be, and it should be traced as a block.

Method: before joining the line along y 4937/4915 I looked at its unclear 80 px at 4.4x
(trap 17); it is one line with a jog under a rail.

**Open, in the order I would take them**

1. `tcw` as a block.
2. R8 in row r10 (`cnt_la_a`); `ras_o0_alt2`.
3. R9's match (`r9m`, AMB-013); the `ral` cell; `bd2` (R12).

## 2026-11-16 17:31  first gate of the column west of the island

`trace/tcw.txt`, `notes/blocks/tcw.md`. 2,033 nets, 3,417 transistors, no errors.

- `tools/findcell.py` with six known cells: nothing in the column but weak matches of
  `fld`'s inverter. It is hand work.
- The row above the bit-0 source gates is an AND-OR-invert:
  `tcw_o3820` = NOT(`tcw_x3855` OR (`inh_ck` AND `tcw_c`)). `inh_ck` and `tcw_c` are shared
  with the group below, so the same two signals gate both the bit-0 source lines and
  this gate; neither is driven in the part traced.
- The class map with `--open` is not usable east of the rail at y 3940-4200 as it stands
  (uncalibrated there); the loads of the bit-0 source gates stay untraced.

**Open, in the order I would take them**

1. `tcw`: calibrate the class map, then the column in tiles from y 3690 up.
2. R8 (`cnt_la_a`), `ras_o0_alt2`; `r9m` (AMB-013); the `ral` cell; `bd2` (R12).

## 2026-11-16 17:40  the gate column as text; its middle stretch drawn

- `tools/railprof.py` prints what lies under a rail from the clean shot's protected
  colours. For the ground rail of `tcw` it lists seventeen gates in five stretches of
  diffusion in one call, and finds the six already traced within 6 px. Contacts it does
  not find (two blob detectors tried, neither reliable).
- With it, a track profile of the six bus metals and one 2.4x view, the stretch
  y 3230-3620 is drawn as three pull-down stacks with their gate polys, pads and bus
  metals (`trace/tcw.txt`): 2,043 nets, 3,422 transistors, no errors. Outputs and loads
  are not traced, and the bus metals are marked uncertain.

Method: text first (rail profile, track profile), then one view per stretch to place
pads and polys, then an overlay on the metal shot to check pad rings and rail contacts.
That is three images for five transistors, against six or more by views alone.

**Open, in the order I would take them**

1. `tcw`: outputs and loads of the middle stretch (the arms east and the pads there);
   then stretch A (six gates) and E; then the second column.
2. As before: R8, `ras_o0_alt2`, `r9m` (AMB-013), `ral`, `bd2` (R12).

## 2026-11-16 17:45  the east side of the column's middle stretch, with all five shots

The two shots not used there before (chip 1's metal shot and its fringed stripped shot)
gave three joins, all drawn as uncertain items (AMB-015): the two upper stacks are one
gate; the inverter below them has its load; its output goes back up a bus metal to the
middle gate of the first stack. Extracted: `tcw_o3550` = NOT `c4l_gab`; `tcw_o3326` low
through `tcw_m6362a`, `tcw_m6404`, or `tcw_o3550` AND `tcw_m6320`. 2,041 nets, 3,423
transistors. Not found: the top node's connection, the load of `tcw_o3326`, where it goes.

Method: the chip-2 stripped shot's legend (diffusion tan, field greener, poly orange) is
the opposite way round from the clean shot's open-area legend (diffusion green). A green
patch means field in one and diffusion in the other; name the shot whenever a colour is
used as evidence.

## 2026-11-16 17:54  the gate column's top stretch drawn; a wrong doubt and a wrong profile

`trace/tcw.txt`: 2,047 nets, 3,429 transistors, no errors. The top stretch (six gates in
three pairs) is drawn with its pads, polys and bus metals; the overlay sits on every pad
ring. The first column of `tcw` now has sixteen of its seventeen gates in the trace.

- The bus metal `tcw_m6404` gates four pull-downs of the column: a common enable.
- The top pair's output is the bus net that gates stretch B's big gate (AMB-016).
- What I held this stretch back for yesterday (two NANDs feeding each other) came from
  assuming a poly reached a node; the class map shows 30 px of field between. Not drawn.

Method: `tools/tla_tracks.py` along a thin metal that horizontal polys cross reports
the crossings and misses the metal (unbridged) or invents continuity (bridged). For a
bus, look at the metal shots; the profile is not evidence either way.

**Open, in the order I would take them**

1. East of the rail for the whole column (loads, output arms), now that every node on
   the rail is named: start with pair 3's middle node and stretch B's big gate.
2. The sources of `tcw_m6404`, `tcw_m6320`, `tcw_m6278`, `c4l_gab` (their far ends).
3. The second column; then the standing list (R8, `ras_o0_alt2`, `r9m`, `ral`, `bd2`).

**Same day, later.** The bus metals followed south: the common enable `tcw_m6404` comes up
from the vertical poly field under the six bus metals (pad (6275,4405)); `c4l_gab`'s
lower pad sends a poly to the rail at the height where the profile had reported a dull
poly, right beside `fld_a_in`'s node (AMB-014 extended: possibly a third pull-down). A
third metal on the x 6362 track gates the column's last pull-down. 2,050 nets, 3,430
transistors; all seventeen gates under the first column's ground rail are in the trace.

## 2026-11-16 18:04  Dates repaired; `notes/operation.md`

The user: "the journal dates are nonsense", and the notes are too dense to read; wanted a
summary of what is certain.

- **Dates.** From the entry on the chase of `e4` onward I had been advancing the date by
  a day with each piece of work; the real commits all lie on 2026-11-14 to 16. Repaired
  from `git blame`: every date that lay after its own line's commit date (126 lines in
  the notes, trace comments and one tool) is replaced by the commit date, and the journal
  headings now carry the commit's date and time. Rule added to `CLAUDE.md`.
- **`notes/operation.md`**: clocks, counters, registers, comparators and the row address
  path, each statement marked firm, marked or open. "Firm" is a test, not a feeling:
  `tools/unsure.py --equations` extracts the netlist with and without every uncertain
  item; 683 of 1,013 equations are unchanged. The page says plainly that no counter's
  reset and no comparator's effect is established yet.


## 2026-11-17 11:48  Collaborator PRs #1-#12 merged

A collaborator (dp111) opened twelve PRs, all on 6101f6e: three stacks, merged as their
five tips (#4, #11, #5, #6, #9), which bring in the other seven. Before merging: each tip
and the trial merge extracted (0 errors, 0 warnings, 0 names outside the glossary);
`tools/unsure.py` on main and on the merge differ only in three nets, each disclosed in
its block's notes (`ra4_drv_in`, `wr_r3`, and `hc2`, whose uncertain stretch is old);
all eleven block notes read; three claims checked in the photos by me (r9m's two hops,
which step one track in the chip-2 stripped shot; ucz's hop at x 14544; mal's copy m7).
The packages had independent reviews on the contributor's side, which caught two errors
before the PRs were opened (r9m's hops, bust's staircase at cdp1's west edge).

Result: 2,090 nets, 3,525 transistors (+95: the `ral` cell, 5 RA and 14 MA copies);
open joins 15 -> 1 (`ck_a_u`, plus `ra4_drv_in_u` aliased across a `?`).

What it establishes (details in `notes/operation.md`):
- **R9's match drives the row counter's step request**: `rcs_mu` = NOT R9's match, so
  term 1 of the step request = R9 match AND NOT `rcs_mv` (AMB-013 resolved).
- The data bus joined across the chip; the register fan-out per bit is the datasheet's
  layout without having assumed it. R8 = cdp1 row A, R9 = row C, bit order settled, so
  the `rename` package is unblocked.
- R3's 4-bit row is the low nibble; `amr` is believed to be the high nibble.
- `uc` = the row counter (R4, R6, R7's comparators); `hc0`-`hc5` and the R0/R1/R2/R4
  strobes joined.
- RA and MA outputs pass through one cell (`ral`), believed a latch (MA on `ck_out`);
  its inverter 1 is not traced (AMB-018). `cnt_gab` has no driver on its drawn net
  (AMB-017).

Coordinator follow-up in the same push: conflicts in `signals.md` and
`work-packages.md` resolved by hand (row additions on both sides); stale former names and
"on branch X" wording fixed; Re-read items R13 (straight-drawn hops), R14 (`ral` device
sizes, x19), R15 (other blocks' notes the new packages contradict); trap 10 extended;
AMB-017, AMB-018; floor plan: the coarse "logic above the counters" block removed, the
top-right logic rows trimmed above the `ral` band; `out/` rebuilt.

Next: the `rename` package (now unblocked), then the queue as before.

## 2026-11-17 13:01  Parallel work for remote collaborators; the master list covers the die

The user: claims must show at once, by commit and push, so that several remote
collaborators can work in parallel; the workflow must be where they see it first,
including an independent review; we keep the master list. Then: "do we have the entire
die mapped out into blocks for tracing", and a `/trace6845` command that does a package
end to end. Collaborators will be given write access.

- **Claims**: `tools/claim.py take` pulls main into the checkout (fast-forward only,
  user: "Ensure that the remote is always pulled before claiming a task"), refuses a
  prefix the master list does not name, a taken prefix or an overlapping region, and
  pushes `claims/PREFIX.md` straight to main with git plumbing (the working tree is not
  touched; a race loses at the push and sees the winner's claim). `list`, `release`,
  and `done` (after a merge: the claim becomes "merged, awaiting coordinator" and holds
  the tracer's proposals for the coordinator's files). Tested against a local bare copy.
- **Work**: one branch and worktree per package (`tools/newwork.sh`); `tools/ship.sh`
  pushes the current branch and refuses main unless `HD_COORD=1`; its lock now works in
  worktrees.
- **Gate**: `tools/mergecheck.py PREFIX` (branch contains main; only own files, the
  glossary, `operation.md` and named trace fixes changed; extraction 0/0; glossary and
  former names clean; a Review section ending "Round N: no findings."; new `?`-only joins
  written up). Run on main for `wrj`: passes all but the review wording, as expected.
- **`/trace6845`** (`.claude/skills/trace6845/SKILL.md`): pull, choose the first free
  queue row, claim, worktree, trace by the guide, review rounds with a fresh agent each
  round until one finds nothing (at most five, else stop without merging), merge through
  the gate, push to main, hand off.
- Documents: `notes/workflow.md` (new), the top of `CLAUDE.md`, `README.md` (new),
  `.github/pull_request_template.md` (for those without write access), the tracing
  guide's sections 1, 9 and 10, the master list's header.

**Coverage.** `tools/coverage.py` (new) draws the die: traced, untraced inside some
package's region, untraced in none. Before: 28 % of the die rectangle in none. The gaps:
the pad ring (39 of 40 pad squares are not drawn: only MA3's is; the RA0-RA4 drivers are
traced but not their pad squares or the metal to them), the D0-D7 pad cells (named in
`dbus`'s row without a region), a bus field with a gate group at 13200-17750 x
16900-18560, a gate group at 4780-7000 x 15000-17000, the test structures, and seams
between regions. New queue rows `dpad`, `busC`, `bl0`, `teststr`; `padring` given
regions; seams closed. After: 0.0 % in none. About 54 % of the die rectangle is traced
(within 100 px), which overstates it inside partly traced arrays.

## 2026-11-17 14:24  PRs #13 (rde) and #14 (amr) merged

Both from dp111, both on b8e2524, independent of each other; merged onto main without
conflicts. Checks on the merged tree: 2,112 nets, 3,582 transistors (+57: `amr`'s slice),
0 errors, 0 warnings; glossary and former names clean; `tools/unsure.py`: five new nets
joined only through `?` items, `db_b4`..`db_b0` (rde's `?M` neck, disclosed,
now AMB-019). Notes read in full; the slice equations checked by hand (x = NOT(NOR(c, q) +
c.q) = c XOR q). Photo spot checks: `amr` c3 overlaid on the clean shot at 1.5x (every
outline on a feature); rde's neck at (9630, 5545-5595) at 4x in two shots: no metal can be
seen across it, as the notes say.

- **R3's high nibble is traced** (`amr`): four latches on `wr_r3` from data bits 4-7,
  and a 4-bit equality comparator, `amr_eq_r3`, against four lines from the west. Those
  lines are **inputs**; `bust` and the first survey had called them outputs (corrected
  in `bust.md` and the glossary; trap 20, re-read R18). Where `amr_eq_r3` goes and what
  drives the four lines: not found.
- **R10 and R11** take their data from the bus (`rde`): `cdp2` row A = R11 (bits 0-4),
  row C = R10 (bits 0-6), as the datasheet. Bits 0-4 marked (AMB-019).
- Method notes from both became traps 18-19 and re-read items R16-R17.

The PRs predate the claim workflow, so there were no claims to release.

## 2026-11-17 14:30  /refresh6845

User: a skill to regenerate `out/`, update `notes/operation.md` and rename the default
named signals whose purpose is now clear. `.claude/skills/refresh6845/SKILL.md`
(coordinator only, on main): baseline; renames in batches, each proved by
`tools/names.py compare` (transistors and connections identical, only names changed)
and the glossary checks, committed per batch; `operation.md` against
`tools/unsure.py --equations`; `tools/build.py`; journal. `tools/names.py` (new):
`candidates` lists placeholders and old `@alias` names beside a functional name, split
into firm (rename) and through `?` items (do not, trap 17), plus glossary hints;
`snapshot` / `compare`. On today's tree it lists, among others, `rc0`..`rc6` ->
`rc0`..`rc6`, `sl_eq_r5` -> `sl_eq_r5`, `h_eq_r0` -> `h_eq_r0`, and keeps rde's
data bits 0-4 apart (AMB-019). Not run yet.

## 2026-11-17 14:43  Refresh

The first run of `/refresh6845`. Every rename batch was proved by `tools/names.py
compare` against the snapshot taken first: 2,112 nets and 3,582 transistors before and
after, every transistor and connection identical, only names changed (86 nets).

- **Batch 1**: the upper array's counter lines `uc_b0`..`uc_b6` -> `rc0`..`rc6` (they were
  aliases); `uc_eq_r4/6/7` -> `rc_eq_r4/6/7`; `cdp1_l4719` -> `sl_eq_r5`; `rdp3_n2s1` ->
  `h_eq_r0`, `rdp3_n0` -> `h_eq_r0half`; R9's match `cdp1_b_eq` and its far end
  `rcs_bq3335` -> `ra_eq_r9`.
- **Batch 2**: the data bus is one name per bit, `db_b0`..`db_b7` (it had been `ubus_b#`,
  `rbus_b#`, `cdp1_*_bl`, `r3_b#_d`, `amr_oa_c#` and two link names: see Former names); R8 and R9's bits
  (`cdp1` rows A and C) are `r8_b#_a/_n2/_q/_m#` and `r9_b#_*`. The cell `cdp1_reg` now
  takes the whole stem as its tag, and no longer labels its bit line (the bus names it).
- Wording repaired where the renames made notes circular (ucz's route table, r9m's
  correction, bust's tables: a note at its top explains the old two-sided tables).
- **Not renamed, on purpose**: R10 and R11 (`cdp2` rows C, A), whose bits 0-4 rest on
  AMB-019 (their `cdp2_*_bus` names stay aliases of `db_b#`); R9's comparator cells
  (`cdp1_b#_*`); aliases that are a cell's own name for a pin (`ar#_q`, `*_tab`,
  `cdp1_b#_b`); `ra4_drv_in_u` (joined only through `?`).
- `operation.md`: `ras_shift` = R8 bit 0 AND bit 1 (the bits' identity is now firm, the
  gate still marked); R9's bit 0 is what selects RA output 0's source in shift mode
  (firm); names current. 708 of 1,049 equations firm, as before.
- `out/` rebuilt: 0 errors, 0 warnings, 0 names outside the glossary. Coverage: about
  54 % traced, 99.3 % of the die rectangle in some package, 0.0 % in neither.

Branches in flight that use an old name fail `tools/mergecheck.py` until they run
`tools/rename.py OLD NEW` after merging main (the former-names table has every pair).

## 2026-11-17 16:17  The review step made proportionate; review cost tracked

User: the review loop is a new requirement of `/trace6845`, "but maybe it's too slow and
expensive". Changed: round 1 is a full review (as before, with a budget of about 40 images and
text tools first); rounds 2 and 3 are fix checks, which a fresh agent does from the diff since
the previous round and the junctions it touches (about 15 images); at most three rounds, not
five; a package with confirmed errors after round 3 is not merged. `tools/costs.py` now marks
review agents by their brief and records review cost per package; the dashboard shows it.

Measured so far: no review agent has run on this machine. A first count that found five
(02) was wrong: it took tracing agents' "check ... against the photo" for review wording.
The reviews in the 2026-11-17 merges ran on dp111's machine and have no cost report. A
tracing agent run costs about $18 API-equivalent here, which is the only guide to what a full
review round may cost until `/trace6845` runs produce numbers.

## 2026-11-17 16:27  Claims no longer wait for the coordinator

A collaborator's agent pointed out that each `/trace6845` loop finishes only part of a package
and then left the package's name locked ("merged, awaiting coordinator") until this session
released it. Changed: `tools/claim.py done` writes the tracer's proposals to `handoffs/` on main
and, in the same commit, keeps the claim (`--continue`, for the next round of a loop) or releases
it. `take` of a package you already hold is a no-op; `tools/newwork.sh` reuses the worktree and
branch; `/trace6845` resumes a held claim first. The coordinator works through `handoffs/`
(`tools/claim.py handoffs`) and removes each file once applied; claims are the tracers' own.
The dashboard lists the handoffs waiting. Tested end to end in a scratch clone with its own
remote (take, take again, done --continue, done, someone else's prefix refused, two handoffs
in one second kept apart).

## 2026-11-17 20:35  Refresh

The second run of `/refresh6845`. Since the first (14:43): three collaborators merged through
the gate with the new claim and handoff flow: dp111 (`dpad`, the D0-D7 pad cells; `areg`;
`tla`; `amr`), Tom Seddon (`dbus`, twice) and Matt Godbolt (`tc1`, five merges in a loop, the
claim kept between them). Twelve handoffs wait in `handoffs/`.

- **Renames: none.** The candidates are deliberate aliases (`ar#_q`, `*_tab`, the data pins'
  `d0_in`/`d1_in`/`d6_in`, `cdp2_c_s#_bus` while R10/R11 stay unrenamed under AMB-019) or
  rest on uncertain geometry. One labelling to fix with the dpad/dbus handoffs: `d2_in_u` ..
  `d6_in_u` sit on the pad side, aliased to the pins, so they mark no open join; the open
  join is on the buffer side (`dbus`'s `d2_in` .. `d5_in`, `d7_in`: `d2_a = NOT d2_in`).
- **`operation.md`**: the collaborators had added their rows (data pins as outputs, the input
  latches, the latch cell's 70-wide pass transistor, the step logic's selector). Checked
  against the equations; one mark corrected: the input latches follow the pin itself only
  for D0 and D1, D2/D3's buffers take `d2_in`/`d3_in` whose join to the pin is not drawn.
  Header and counts current.
- **`out/`** rebuilt: 2,168 nets, 3,845 transistors, 0 errors, 0 warnings, 0 names outside the
  glossary, 772 of 1,117 equations firm. The coarse floor-plan blocks "D0-D7 pad cells" and
  "data bus interface column" removed: `dpad` and `dbus` cover them. Coverage: 60.0 % of the
  die rectangle traced (54.4 % at the first refresh), 99.3 % in some package, 0.0 % in none.
- Three pushes were rejected because collaborators merged meanwhile; each time pulled,
  re-checked, rebuilt and pushed (the protection on main doing its job).
- Open PRs from dp111 opened before write access: #15 (`amr`'s comparator inputs are
  `c4l0`-`c4l3`; `amr_eq_r3` drawn to `tla`), #16 (`ral`'s inverter 1: the RA/MA output
  cell is a latch with a force line; AMB-017/018, R14), #17 (`dbus`: all eight input latches,
  D6/D7 buffers, `dlat_en`'s driver). **#17 overlaps Tom Seddon's active `dbus` claim.**

## 2026-11-17 13:33 -0600  Process changes from a tracer's suggestions: batched reviews, the round rule, ports, shared tools

User: apply the suggestions of the `tc1` tracing session (eight runs, 2026-11-17; two of them
were already questions in its handoffs of `3c0efe1` and `48b43dd`). Done on a branch
(`process-suggestions`), not traced: no trace file changed.

- **Small pieces share a review.** One reviewer used about 250,000 tokens on a three-transistor
  NOR, most of it the fixed cost of reading the guide and calibrating. Two or three small
  cells of the same build may now be traced, each shipped as it is finished, and reviewed in
  one full round: at most three pieces and about a dozen transistors, one brief listing every
  piece's claims and suspicions (`notes/workflow.md` step 6, `/trace6845` steps 5 and 6).
- **Only findings that change a connection count against the three rounds.** `tc1`'s run 3
  was kept out of main by a third round of a rail's width, a diffusion's width and a comment.
  A geometry-only finding is fixed and recorded, and needs no further round if
  `tools/sameconn.py COMMIT` (new) ends `connections identical` for the package and for every
  file: it compares the nets' names, each transistor's three nets and the equations between
  a commit and the working tree, ignoring sizes and positions. (`tools/names.py compare` is
  the test for renames and fails when any transistor's size moves, so it could not serve.)
  Run on `tc1`'s history, the run-3 round-3 fixes (`92b9dcf` to `937a48b`) and run 6's width
  fix (`6b214a1` to `61e6cf2`) both read `connections identical`. A moved port is a changed
  connection that the extraction cannot see; the rule says so.
  The gate (`tools/mergecheck.py`, check 5) now reads the **last** `Round N:` line of the
  Review section: `Round N: no findings.`, or `Round N: no findings that change a connection.`
  with the words `connections identical` in the section. Before, "no findings" anywhere in the
  section passed, so an unfinished later cycle passed on an earlier one's clean round. Notes
  with no `Round N:` line pass as before. `--review-test FILE` runs that check alone.
  The gate now also **fails when the last `Round N:` line is not a clean one**
  (`STRICT_LAST_ROUND` in `tools/mergecheck.py`). This is stricter than before for every
  collaborator and was not among the suggestions; it was pushed switched off, and the user
  turned it on the same day ("yeah let's turn that on").
- **Ports are machine-readable**: `ports.d/PREFIX.txt`, one line per port (name, layer, place
  or range, direction, note), a tracer's own file (workflow step 3, guide sections 8-10, the
  gate, the pull request template; `tools/rename.py` and `tools/signals.py --docs` cover it).
  `tools/ports.py` lists the ports of different packages that meet within 40 px and whether
  names, layers and directions agree, names used by two packages at places that do not meet,
  and ports with no partner; `--near X,Y`, `--prefix P`. Seeded with `ports.d/tc1.txt`, 50
  lines transcribed from the tables in `notes/blocks/tc1.md`; with one file, nothing meets yet.
  Optional for blocks already traced, expected for new work.
- **Two traps** (guide, section 4): 21, bright green in the open is a large diffusion, which
  the class map paints as field; 22, a thin metal is dark for 35-80 px over a buried contact
  and that is not a contact. Both can have misled earlier blocks, so both are on the Re-read
  list: **R19** (areas called field from green or from the class map without `--open`: `tcw`
  first, then the rest of the top-centre and top-left logic) and **R20** (contacts on thin metals accepted from a dark stretch: `tcw`'s bus
  metals first). The layer tables did not need changing: they already give open diffusion as
  green and open field as khaki.
- **Shared measuring tools**, since six packages had each written their own: `tools/px.py`
  (colour profiles: rows, columns, points, any shots, composites), `tools/textmap.py` (text
  maps; `--acid` adds the chip-2 stripped shot), `tools/opendiff.py` (large open diffusions).
  Each prints the same as the tool it came from (`tc1_px.py`, `tc1_hex.py`, `tc1_green.py`) on
  the calls tried; the per-block tools stay, because notes cite them.
- **`/trace6845`**: the survey and a draft of the geometry are written to
  `cache/scratch/PREFIX/` before anything is drawn (it made resuming after a compaction a
  matter of reading two files); the point to compact or start afresh is right after a merge
  and handoff. The reviewer briefs carry the lines tracers had been adding by hand: `cd` into
  the worktree in every command, `--out cache/scratch/PREFIX/review-N/NAME.png` (a bare name
  lands in the tracer's folder), which N, do not read the Review section, no agents, no web.
- **`tools/costs.py` missed reviewers whose brief had been edited.** It matched two fixed
  phrases; the run-7 reviewer's brief began "You are reviewing one piece of a die trace" and
  two fix checks "You are checking one correction to a die trace", so three review agents
  counted as tracing (the review figure stood at $51.08 across run 7's review).
  It now goes by how the brief opens and by the description the agent was started with
  ("Review ...", "Fix check ..."). On this machine's transcripts, run back to back: review
  $57.55 before, $68.79 after, of $152.69. The committed cost reports are not regenerated
  here: the next `tools/costs.py` run will show the higher figure.
## 2026-11-17 20:46  Thirteen handoffs processed; PR #17 held

Handoffs taken in (all merged to main earlier today by their tracers): `dpad` (dp111, e3b6adf),
`areg` (dp111, 0d5e402), `tla` (dp111, 0cbaceb), `ral` (dp111, 8667009), `amr` (dp111, 8171755),
`dbus` runs 2 and 3 (Tom Seddon, c492bf6, c034e51), `tc1` runs 3-9 (Matt Godbolt, six handoffs,
3c0efe1 to 8650cb8). Extraction 2,169 nets, 3,849 transistors, 0 errors, 0 warnings; 773 of 1,119
equations firm; traced 60.0 % of the die, 0.0 % in no package.

- **Master list.** `dpad`, `areg`, `ral`, `mal`, `amr` done; `tla`, `dbus`, `tc1` partial (claims of
  `dbus` and `tc1` kept by their tracers). New package **`dlat`** (16450-16950 x 13900-15800, the
  input latches of data bits 4-7, proposed by `dbus` and `areg`), replacing the queue row `areg
  (continue)`. Notes for `tcw` (two poly rows from `tc1` at x 6750) and `tc2` (where `tc1`'s cell B
  output lands). Open join `tc1_x1_u` listed.
- **Re-read list** R21-R27 (after Matt Godbolt's R19, R20, which already cover `tc1`'s two lessons:
  bright green in the open, and a thin metal dark over a buried contact): `pads`' data pad readings
  (R21), pass-transistor widths on a widened land (R22), pull-downs on both sides of a rail (R23),
  gap artefacts not checked in the chip-2 shots (R24), the input inverters' L arm (R25), follower
  jumps at pads beside wide metal (R26), mixed medians (R27).
- **Ambiguities.** AMB-003 resolved (the data pad cell, `dpad`); AMB-004 changed (the L arm is a second
  pull-down in the data bus column); AMB-005 extended; AMB-017 reading B struck; AMB-018 resolved (the
  `ral` cell is a latch with a force line, FIRM in all 19 copies). New: AMB-020 (`tc1_x1`'s three
  joins), AMB-021 (D6's line and the `d0_out_n` inverter, assumed no contact), AMB-022 (`rcs_iso2958`),
  AMB-023 (`amr` c0's box, assumed buried).
- **Tracing guide.** Trap 2 extended (check a gap artefact in both chip-2 shots); traps 23 (the L arm) and
  24 (medians, widened lands, rails) new, after Matt's traps 21 and 22.
- **Other blocks' notes.** `rdp3` (T1 70/28), `dbl` (the unit drives the data line; the poly U is
  `dl1_q_n`), `bd2` (the metal at (16772,15800) is `dbus_le`), `bust` (`amr`'s lines are inputs),
  `mal` (the latch is traced; 98 transistors), `pads` (data pad section superseded by `dpad`), `dpad`
  (D6's line drawn by `dbus`), `tcw`, `fld`, `shm` (notes from `tc1`); glossary rows `db_b#`, `tc1_x1`,
  `d#_in_u`, `dbus_le`; `operation.md`'s RA and MA rows (the latch is firm). `trace/dpad.txt`: the labels
  `d2_in_u`..`d6_in_u` and their aliases dropped (Tom's run 4, which landed during this work, draws
  D2-D5's lines; D6's was drawn in run 3); `trace/mal.txt` header.
- **Not applied.** `notes/blocks/dbus.md`'s "depletion load on P_x / P_y" (from `dpad`): left to Tom,
  whose claim is active and whose run 3 already names P_x `d_hiz`. `bust`'s two `?P` rows (made firm
  only by tracing, noted in the `amr` row). Dropping `amr_eq_r3`'s redundant alias from `tla` (done in the refresh below): `tla`'s
  region is inside dp111's `tl1` claim, so it waits for the next refresh.
- **PR #17** (dp111's bits 4-7 latches) is kept open on purpose (user): an independent trace of what
  `dlat` covers, to compare when that package lands. Checked against main today: 222 of main's 236
  transistors in x 16300-17760 matched within 20 px, 81 nets mapped with 0 inconsistencies; #17 has 48
  transistors main has not (bits 4-7) and predates the `rdp3_lat` width fix.
- Two runs merged over the coordinator's earlier Opus session (`amr`, `ral`: mergecheck 8b) with the
  contributor's approval; the tracing and reviews were Fable 5.2.
- Matt's questions in the `tc1` handoffs (the colour trap, the review limit) were answered by his
  process change of 13:33 -0600 above; the `shm` `?B` re-look is in AMB-020 and `shm.md`; the west
  boundary at x 6750 is `tcw`'s (its row).
- `/refresh6845` step 0 now points at `tools/claim.py handoffs`.

## 2026-11-17 20:53  Handoff `dbus` run 4 (Tom Seddon, 9302a30); claim released

Arrived while the thirteen above were being pushed. Extraction 2,165 nets, 3,854 transistors, 0
errors, 0 warnings; 777 of 1,124 equations firm.

- **Master list.** `dbus` partial, 127 transistors, claim released by its tracer; the queue row
  `dbus (continue)` now lists only the wiring left (`d2_out_n`..`d7_out_n`, the drivers of
  `dbus_do0_in` and `d1_out_n`, `d7_in`, the capacitor taps, `d_hiz`'s driver, AMB-021). `r9c`: its
  units' loads are traced (in `trace/dbus.txt`, cell `dbus_r9l`).
- **AMB-012** resolved for the loads and the rails (the east rail is VCC): `ra#_cmp` = NOT `ra#_drv_in`.
  Left: `r9c`'s `?B` ties at the units' west ends. Notes of `r9c`, its floor-plan line, the glossary
  row `ra#_cmp` updated.
- **Re-read.** R22 widened to pull-downs drawn from the land under a rail (`dbus_in`'s G1, G4: 60 ->
  94; `inrow`, `dbus_in`'s G2/G3, first-session blocks). New R28 (ports drawn to a region's edge
  without looking at the edge; `dbus`'s `d4_d`..`d7_d`, `dbus_le`, `d7_c` at x 16950, for `dlat`)
  with trap 25. Guide section 2: tools must load the aligned arrays, not `cache/acid.npy`.
- `dpad.md`: D2-D6's node contacts and D1's `d1_out_n` recorded. The `d#_in_u` aliases had already
  gone in the entry above.
- **PR #17** stays open: Tom's run 4 confirms the bits 4-7 latches are not in `dbus`'s region, so
  the comparison waits for `dlat`.

## 2026-11-17 22:45  Eight handoffs processed; Refresh

**Handoffs** (e125938, da0d0fd): `dbus` runs 5-6 (Tom Seddon; claim released), `tc1` runs 10-11
(Matt Godbolt; **done**, claim released), `tcw` run 2 (Matt Godbolt), `tl1` three runs (dp111;
claim kept).

- Master list: `dbus` down to AMB-021 and a look along `d_hiz` inside its region; what leaves it
  went to `busC` (`d6_out_n`, `d7_out_n`, `d7_in`, `d7_c`, `d_hiz`'s driver) and `bd2` (rest) (the
  drivers of `d1_out_n`..`d5_out_n` and `dbus_do0_in`, a second staircase of pads). `tc1` done
  (54 transistors, 41 nets). `tcw`'s south end complete; its region is now x 6380-6760. `tl1`: the
  west column is two latches in series in front of `rcs_e4`'s NOR (marked).
- **AMB-020** grew: `tcw` drives the row `tc1_x1_u`, and with `tc1`'s alias the extraction gives
  `tc1_x1` = NOR(`ras_o0_sel1`, `tcw_m6362c`) (DEPENDS): two inverters wired onto one line. Either
  the design or a wrong join (J2, J3); the pads (6962,4268) and (6968,3905) are first to re-read.
- AMB-014 (loads found by `tcw`), AMB-015 (a note); new AMB-024 (the wide NOR across R1's edge),
  AMB-025 (`tl1_w4678`'s source), AMB-026 (`tl1`'s load-plate ties). Re-read R29 (`tla`: track
  tool's false breaks, abutting VCC boxes, gate polys past the rail) and R30 (a "load" that
  reaches the VSS box is a pull-down; a thin metal's edge taken for a poly edge).
- Notes: `fld` (loads in `tcw`), `tc1` (the pointer to `tcw`'s driver), `dpad` (D2-D7 output
  lines), `tla` (thin W's "end" a follower stop; two VCC boxes to correct). Floor plan: the
  coarse top-centre block trimmed to its lower half (`tc2`).
- Not taken up: Matt's suggestions for the shared tools (`sameconn.py` telling "input renamed"
  from "logic changed"; asking that a gate's inputs be followed before it is merged). For the
  user. `build.py --help` was already fixed by Matt (f98bb29), and `build.py` now needs
  `HD_COORD=1`.
- **Tom claimed `dlat`** (22:3x): the independent trace of bits 4-7 that PR #17 (held) will be
  compared with.

**Refresh.** Renames (`names.py compare`: only names changed): the counter's lines on firm
geometry, `cdp1_l4544` -> `c4l0`, `cdp1_l4588` -> `c4l1`, `amr_ob_c1` -> `c4l1`; `tla_w3461` ->
`amr_eq_r3` (the alias in `trace/amrw.txt` dropped). Left on purpose: `c4l2`, `c4l3` (joined only
through `bust`'s two `?P` rows), and the deliberate aliases (`ar#_q`, `*_tab`, `d#_in`,
`cdp2_c_s#_bus` under AMB-019). Branches using the old names need `tools/rename.py` after merging
main. `operation.md`: the tracers had already added their rows (`tl1`'s latches, `tcw`'s field
latch); header and count updated. Extraction 2,191 nets, 3,890 transistors, 0 errors, 0 warnings;
779 of 1,136 equations firm. Coverage: traced 60.3 %, in a package 99.3 %, in neither 0.0 %.

## 2026-11-18 11:26  32 handoffs processed (overnight); Refresh

Merged overnight by their tracers: `dbus` run 7 (Matt Godbolt), `dlat` (Tom Seddon, done), `tc2`
(dp111, four runs, done), `tcw` run 3 (Matt), `tl1` (dp111, fourth run, released), `tl2` (Matt run 1,
Tom runs 2-3), `tl3` and `tl4` (Matt, claims kept), `tl5` and `tl6` (dp111, done), and five small
packages by dp111 on Opus (below). Extraction 2,347 nets, 4,156 transistors, 0 errors, 0 warnings;
822 of 1,222 equations firm; traced 62.2 %, in a package 99.3 %, in neither 0.0 %.

- **Opus work.** dp111's Fable allowance ran out (about a week). `bc2` (22 transistors), `bc3` (2),
  `lc2` (22), `lc3` (4) and `tr1` (6) were traced and reviewed on claude-opus and merged although the
  gate's model check (8b) failed; the handoffs said so. The user (2026-11-18): **keep them on main,
  have each reviewed on Fable (R31), and no more Opus merges** (dp111 to pause until Fable is back;
  a message drafted for the user). `bc4` is a survey on its branch only.
- **Master list.** `dbus` done (the `dbus (continue)` row dropped; AMB-021 kept by three readers);
  `dlat` done, so **PR #17 can now be compared** with it; `tc2` done as far as the photos allow;
  `tl1`-`tl6`, `lc1`-`lc3`, `bc2`-`bc4`, `tr1`/`tr2` now give each part's status; the `tcw` row's name
  and region repaired (my edit of 2026-11-17 had overwritten the name). `lc1` is claimed by Matt for
  scarybeasts (no write access yet). New in the `tl` row: the wide metal band y 2180-2500 north of the
  strips is drawn by no block.
- **Re-read** R31 (the Opus pieces, a Fable review), R32 (`tl2`'s five traps in the clusters: rows run
  onto a pad across a gap, one poly drawn across a rail/thin-metal gap, load ties by analogy, load
  gate polys stopped at the tie, NORs short of inputs), R33 (`railprof.py` under rails), R34
  (mirrored `findcell` copies may be re-drawn layouts), R35 (`tl1`'s cells omit the thin metal
  through each unit; their master geometry), R36 (rails drawn to a round coordinate), R37 (every
  `@alias`: it joins nothing). R20 and R26 extended.
- **Ambiguities.** AMB-009 corrected (the pass transistor's gate is `tl3_w3982`, not `clk_tl`);
  AMB-014, 015, 020, 021, 026 updated; new AMB-027 (`tc2`'s latch joins), 028 (`tc1_ns3` over `rax`;
  `tc2_sr_r`), 029 (`tl2`'s pair through one load tie), 030 (`tl3`'s gate to the lower unit's arm).
- **Other blocks' notes**: `dbus`, `dpad`, `areg`, `bd2`, `rdp3`, `rax`, `fld`, `r9m`, `tc2`, `tl1`, `tl5`,
  `bust`, `tla` (a corrections section from `tl1`-`tl4`); glossary rows `rcs_thin_e`, `tla_w#`, `r9m_l3`;
  `ports.d/tl1.txt` (`tl1_w5936` is an input). Floor plan: `areg`'s untraced strip removed and
  `bd2`'s right-hand column trimmed (both now `dlat`), the coarse lower top-centre block removed
  (`tc2`). `tools/ports.py --near` no longer crashes on two ports at equal distance (from `tc2`).

**Refresh.** Renamed (`names.py compare`: only names changed): `areg_w6` -> `dl7_q_n`, `areg_w7` ->
`dl6_q_n` (the bit 7 and bit 6 latch outputs, proposed by `dlat`); the glossary row `areg_w#` dropped.
Left on purpose: `rcs_a2` and `rcs_x1` gather placeholders of `tl1` and `tl3` but are themselves
unidentified, and `tl3` is claimed; the deliberate aliases as before. `operation.md`: the tracers had
added their rows (`tl2`'s step-logic gates, `rcs_x1` as the clear of four latches, `tl4`, `tl5`,
`tc2`, `dlat`); header and count updated.

## 2026-11-18 23:58  15 handoffs and pull request #20 processed

Pulled 110 commits: `tl1` run 5, `tl2` runs 4-5, `tl3` runs 5-10, `tl4` runs 6-10 (Tom Seddon,
Matt Godbolt), `lc1` (scarybeasts, pull request #20, merged by Matt as d1f70ac), and Matt's dashboard
fixes. Full extraction before any change: 2,363 nets, 4,224 transistors, 0 errors, 0 warnings; one
open join (`ck_a_u`). Claims now: `tl3` (Tom, run 11), `lc2` (Matt, continuing dp111's latches).

- **Done.** `tl4`: the whole strip x 4250-4967 (47 transistors, all wiring and rails; claim released).
  `tl2` done as far as its strip goes. `lc1` partial (24 transistors, Fable only): `lc_step` = NOT
  `lc1_w7040`, the output of a latch whose lower half lies in `lc2`.
- **What changed in the step logic.** AMB-009 resolved the other way: `rcs_cond` =
  NOR(`rcs_cond_n`, `tl3_w3982`), and `rcs_cond_lat` is an inverter's output (AMB-031), not a latch
  node. `rcs_in1` = NOT `rcs_mv` (`tla`'s column ran through field, split by `tl3`); R9's match is an
  input of `rcs_mn3852` and reaches the step request through `tl3_e3550` and `rcs_e4` (marked,
  AMB-032). `tl1_w3594` = `inh_ck` (marked, AMB-033): `tl1`'s two latches and `tl3`'s latches B and C
  are master/slave pairs on `inh_ck`. Latch C's clear is `rcs_x1`.
- **Master list.** Rows `tl1`-`tl6`, `lc1`-`lc3` and `tla` updated. New rows `decode`, `clock` and
  `pads`: blocks traced early that had no row, so the dashboard and `coverage.py` could not show them
  (Matt's handoff). New queue row `tlb`: the wide metal band y 2180-2500 north of the top-left strips,
  carved out of `padring`. Six wires of `tl1`/`tl2` and the rails RA and RC end on it.
- **Re-read** R38 (ends taken from `tools/follow.py`), R39 (poly stubs ending under rails; undrawn
  units), R40 (`tla`'s units in the middle cluster's east column), R41 (thin metals across tie boxes:
  `tools/tl3_thin.py`, `?M` with aliases), R42 (gates at a rail's edge from the clean shot). R20, R30,
  R34, R35, R36 extended; R35(b)'s inverter gate done at the master.
- **Traps 26-31** in the tracing guide: a bright centre without the hole; thin metals over boxes;
  the rail/thin-metal gap; wires under rails; where the follower ends; half a cell at a package
  boundary.
- **Ambiguities.** AMB-009 resolved; AMB-013, 026 and 029 updated. New: AMB-031 (`rcs_cond_lat` through
  a load tie), AMB-032 and AMB-033 (the middle cluster's two thin metals), AMB-034 (`tl4`'s ring-like
  marks), AMB-035 (`tc2_o5175` to `tl3`'s gates through `r9m`'s stub).
- **Other blocks' notes.** Corrections appended to `tla`, `tl1`, `tl2`, `tl4`, `tl5`, `r9m` and `ur`.
  `ports.d/tl1.txt` gains the VSS arm at x 2817. Not edited, because they are under active claims:
  `tl3.md` (`tl4`'s corrections on `rcs_mv`'s direction, `tl3_e3028`, the rows at x 4250) and `lc2.md`
  (`lc1`'s latch D lower unit and the joins `rst_c`, `lc2_w8169`). Both are listed in the master list
  rows for their claimants.
- **Floor plan.** The coarse top-left block is trimmed to strip 3 (`tl3`); the fragments of
  `tl1`, `tl2` and `tl4`-`tl6` cover the rest.
- **Dashboard.** Matt fixed `read_master()`: it dropped the first row after each blank line, so
  eight packages were missing. It also gained legend hover. That was a Sonnet session doing tooling,
  not tracing, so the Fable rule does not apply.
- **`tools/costs.py` (Matt, 1add61d; with the user's approval).** A main session's response now counts
  as coordination unless the same transcript made a tracing call (`tools/t.sh`, `tools/ship.sh`, or an
  Edit/Write of `trace/*.txt` or `notes/blocks/*.md`) between it and the commit it would join. This is
  so that a second session under one git name no longer lands on another package's gate (`lc2` failed
  8b on nine Sonnet responses from dashboard work). Reviewed: the change is right for that case. One
  gap: a session that writes trace files through Bash (a heredoc, `sed -i`, a Python script) without
  `t.sh` or `ship.sh` is not seen as tracing, so another model's responses could pass 8b. A package whose
  responses are all coordination still fails 8b ("models seen: none"). Reported to the user, not
  changed. `lc2`'s claim was released, paused; run 3's piece is on its branch.


## 2026-11-19 00:06  Refresh

- **Renamed** (`names.py compare`: only names changed): `tl4_w3808` -> `rcs_e3`, `tl5_w5717` ->
  `rcs_mv`, `tl5_w5890` -> `rcs_x1` (`tl4`'s firm joins, runs 7-9). Three tautologies that the rename
  left in the prose (a name set equal to itself) were reworded by hand.
- **Left on purpose.** `tl3`'s firm renames wait for Tom's active claim to end, because they would
  rewrite `trace/tl3.txt` under his branch: `tl3_e5240` -> `tl3_w5025`,
  `tl3_e4372` -> `tl3_w4546`,
  and the open join of latch C's data. The joins through `?M` stay as aliases (AMB-032, AMB-033), and so does
  `rcs_cond_lat` (AMB-031). Placeholder-to-placeholder aliases such as `tl4_w3070` -> `tl3_e4243` are
  not renamed. All of this is listed in the master list's `rename` row.
- **`operation.md`.** The tracers had kept their rows current (AMB-009's resolution, `rcs_in1` = NOT
  `rcs_mv`, the foot's joins, `tl1_w3594` = `inh_ck`, the top of `tl4`'s strip, `lc_step`). I updated
  the header (2,363 nets, 4,224 transistors), the firm count (832 of 1,246 equations) and the ranges
  (AMB-001 to AMB-035, R1-R42).
- **`out/` rebuilt**: 0 errors, 0 warnings, 0 names outside the glossary; one open join (`ck_a_u`).
  Coverage: 62.6% traced, 99.7% in a package, 0.0% in neither.

## 2026-11-19 00:12  End-of-frame lead group at the head of the queue

On the user's request, a new queue row `eof` goes first, so `/trace6845` without a prefix takes it. It
holds the follow tasks that block the end-of-frame sequence, in order: where R4's match
`rc_eq_r4` goes (east of x 13425 at y 9663, from track T6 of the counter channel); where R5's match
`sl_eq_r5` goes (west of x 8340); `inh_ck`'s source (eleven gate loads, among them the master/slave
latch pairs and the field latch path); the driver of `rcs_x1` (beyond `tl5`'s bus line x 5107).
`bd1`-`bd3` moves up to second. `tl4_w4590`'s driver (in `tl3`'s strip) and `lc2`'s latch D data wait
for their claims.

## 2026-11-19 00:16  The left bus field second in the queue

On the user's request, `busL` (4780-7550 x 10400-15000) is split from the `busL`, `busB`, `busT` row
and placed second in the queue, after `eof`. It is wiring with few or no transistors expected; the point
is the joins between the left array and the central datapath, so that names can be carried across the
two halves of the die. The row asks for `ports.d/busL.txt` at both edges and points at trap 10 and
R1-R4 (poly under the tracks). The floor plan's label names the package.

## 2026-11-19 10:11  Nine handoffs processed (eof, tl3, lc2, costs.py)

Pulled: `eof` runs 1-2 (Tom Seddon), `tl3` run 11 (Tom), `lc2` runs 3-10 (Matt Godbolt), and a second
change to `tools/costs.py` (Matt, at the user's instruction). Full extraction before any change: 2,379
nets, 4,282 transistors, 0 errors, 0 warnings. No active claims.

- **End of frame (`eof`, the lead group's first two runs).** R4's match `rc_eq_r4` is drawn end to end
  and is the data of `bd1`'s latch gated by `inh_lat` and the input of `bd1`'s inverter A (firm join;
  AMB-036 on one contact). R5's match `sl_eq_r5` drives one inverter in `cdp1`'s slice-0 position
  (`sl_eq_r5_n` = NOT `sl_eq_r5`, firm), whose output runs west through the top-left strips into the band
  `tlb`, where its loads must be. **`inh_ck` is `inh_ck`** (firm): `trunks`' line S climbs on to the top
  left, so the inhibit/strobe of the input buffer row is what opens the vertical control's master/slave
  latch pairs and the field latch path. **`rcs_x1` = NOT `lc1_w7170`**, and **`rst` =
  NOR(`lpstb_b`, `res_b`)** (firm; believed the reset), whose buffered copies clear `tl4`'s and `tl5`'s
  latches and latch D.
- **`lc2` is done but for its edges** (80 transistors, Fable): latch D, the `lc_step` latch, is
  complete (data `lc1_w7780`); and the west gate cluster is **a two-stage ripple counter** (two toggle
  flip-flops), held clear with `rcs_x1`'s input, clocked from `lc3`. A 2-bit counter beside the scan
  line counter's step latch is a candidate for counting the first cycles of a line (believed only).
  R31 done for `lc2`.
- **`tl3` run 11**: the 4-bit counter's L3 line is `tl4`'s strong inverter (`c4l_l3`; the first counter
  L3 with a traced driver), its gab is `c4l_gab`; `rcs_thin_e` is not `sl_l3` (`trace/ur.txt`
  corrected).
- **Master list.** The `eof` row gives the lead group's state and next steps in order: `tlb` (moved up
  to third), `inh_src`'s source, the gate group at `inh_ck`'s tap (7540-7780, 7600-7820), `lc3` (the
  counter's clock), `bd1`'s latch, `lc1_w7170`'s driver. Rows `tl1`-`tl6` (`tl3` released), `lc1`-`lc3`,
  `ur`, `r9m`, `trunks` (continue) updated. Re-read R43 (polys that go on below a pad), R44 (`ur`'s
  through lines and rows between pads), R45 (copies' pads); R4, R26, R31 (done for `lc2`), R36, R41
  extended. Traps 32-36 (look all round every pad; two pads on a line; rows beyond a rail's edge; a
  load's plate away from its output; bright stretches that are diffusion), trap 30 extended.
- **Ambiguities.** AMB-033 updated (track A is `inh_ck`); new AMB-036 (`rdp3`'s contact on R4's path),
  AMB-037 (`inh_ck`'s staircase over other nets).
- **Other blocks' notes**: corrections appended to `bust`, `cdp1`, `tc2`, `r9m`, `tl1`, `tl2`, `tl4`, `tl5`,
  `tl6`, `rdp2`, `rdp3`, `bd1`, `hcj`, `ucz`, `mrach`, `lc1`, `lc3`, `trunks`, `tcw`, `fld`, `ur`, `tla`,
  `urch`; `tl3.md` now that its claim has ended (including `tl4`'s corrections of 2026-11-18).
  `ports.d/tl6.txt` (`inh_ck` in) and `ports.d/tc2.txt` (`sl_eq_r5_n` in). Not changed: comments in
  `trace/bust.txt` and `trace/tc2.txt` that the notes now correct.
- **Floor plan.** The coarse left-centre block is split into what `lc1` and `lc3` have not drawn
  (`lc2` is its fragment); the top-left strip 3 block is cut to the rows above y 2890.
- **`tools/costs.py`, second change** (Matt, e836694, at the user's instruction): a main session is
  credited with a package only for its own calls on that package (`tools/t.sh PACKAGE`, `ship.sh` of its
  files, Edit/Write of them). It fixes the cross-session case. The gap noted on 2026-11-18 remains: a
  session that edits trace files through Bash is not seen as working on the package.
- **From `tl3`'s handoff, on the merge step:** main moved under the gate six times in a row during the
  last handoff pass and refresh. Each move meant a re-merge and a fresh cost-report commit. Proposal:
  the coordinator pushes its series as one push where it can, or `mergecheck.py` says at once that main
  has moved. Taken: from this pass the handoff work goes in one push and the refresh in as few as its
  steps allow.

## 2026-11-19 10:22  Refresh

- **Renamed** (`names.py compare` after each batch: only names changed; 26 nets). No claims were
  open, so `tl3`'s and `lc2`'s placeholders could be taken too.
  - Batch 1: `tcw_a`, `lc2_w8172`, `tl3_e4152`, `tl4_w4501`, `tl5_w5631` -> `inh_ck`.
  - Batch 2, firm joins into names already in use:
    `lc1_w7140`, `tl1_w4025`, `tl3_w3506`, `tl3_w4200` -> `rcs_x1`;
    `tl3_w5112`, `tl3_e4808`, `rcs_g4240` -> `rcs_x1`; `tl3_e4915` -> `rcs_mv`;
    `tl3_w3765` -> `rcs_a2`; `lc1_w7343` -> `res_b`; `lc1_w7257` -> `lpstb_b`; `bd1_a`, `rdp3_n7s9`
    -> `rc_eq_r4`; `tl4_w5455`, `tl5_w5457` -> `c4l_l3`; `tcw_m6232`, `tl5_w4590` -> `c4l_gab`.
  - Batch 3, new names: `r9m_l1w`, `tl4_w2512`, `tl1_w2592` -> `sl_eq_r5_n`; `lc1_w7304` -> `rst`,
    `lc1_w7468` -> `rst_n`, `lc1_w7606`/`tl5_w3636`/`tl4_w4198` -> `rst_a`, `lc1_w7734` -> `rst_b`,
    `lc1_w7864` -> `rst_c`; the open join `tl3_e4635_u` -> `tl3_e4635`.
  - `rst` is named for what its traced equation does (NOR of the two pins, clearing latches). That it
    is the datasheet's reset is believed, and its glossary row says so.
  - The renames left about 45 tautologies in the prose ("X = X") across notes, journal, trace
    comments and floor-plan labels. They were reworded by script and by hand. Older journal entries
    were reworded where the former-names check required it.
- **Left on purpose**: the joins through `?M` (AMB-032, AMB-033), `rcs_cond_lat` (AMB-031), and
  placeholder-to-placeholder aliases (listed in the `rename` row).
- **`operation.md`**: header (2,379 nets, 4,282 transistors), 839 of 1,261 equations firm, ranges
  AMB-001 to AMB-037 and R1-R45. The `inh_ck`, `rcs_x1` and reset passages were reworded after the
  renames (`rcs_x1`'s input is `lc2`'s staircase line, which also clears `lc2`'s counter). The
  "Not established" bullet on the end-of-frame sequence now says what the lead group has traced
  towards it.
- **`out/` rebuilt**: 0 errors, 0 warnings, 0 names outside the glossary, one open join (`ck_a_u`).
  Coverage: 63.0% traced, 99.7% in a package, 0.0% in neither.
- **Pushed in two pushes** (handoffs, then the refresh), following `tl3`'s request to spare the
  tracers' gate runs.

## 2026-11-19 10:32  Floor plan of the top-left logic brought up to date

The user asked whether the floor plan reflects the latest top-left findings. Every traced piece had
its box, but the labels lagged:
- `tl4`'s and `tl5`'s blocks were still drawn provisional although both packages are done. The
  `?` is dropped on all of them except `tl5`'s rail RC, which is VSS by structure only.
- Labels now say what is known: "latch that drives the 4-bit counter's L3 line", "c4l_l3 driver",
  "data inverter of the c4l_l3 latch", "inverter that makes rcs_e3", "latch c: field flip-flop
  candidate".
- `tla`'s fragment predated `tl1`-`tl5`. It drew coarse provisional blocks over the middle and
  right clusters ("not traced"), the second bus field and the small cluster; these are removed, since
  the strips' own fragments cover them. Its step-logic cluster, vertical bus and second crossing
  field are no longer provisional. The poly bus label now names its five lines (`eof`).
- Still provisional, rightly: `tla`'s rows along the top (y 2620-2900, `tl3`'s last item) and the
  diagonal fan in `lc1`'s strip.
- `out/` rebuilt.

## 2026-11-19 10:59  Queue: the central column's registers and the rest of the top left

The user asked for priority on the top-left random logic and on the registers and latches down the
central column (R12-R17). After `eof`, `busL` and `tlb` the queue now runs:
1. `regs`: a follow lead group. It takes `wr_r14`, `wr_r15`, `rsel12`, `rsel13` and the four read
   selects from `sel`'s bottom edge to the rows they strobe, to say which row is which register.
2. `tl3` (continue): the rows above y 2890, which hold the only way left to `tl4_w4590`'s driver.
3. `cdp4` (continue), moved up.
4. `cdp3` (continue): row A's six large cells, with `cdp2`'s row D, the top of the same cells.
5. `tla` (continue): its Left list and R38-R42.
6. `cdp2` (continue).
7. `cdp1` (continue).

Floor plan: `ral`'s label was still "believed a latch per bit (partly traced)" and provisional,
although `ral` has been done since 2026-11-17 (a static latch per bit, firm in all 19 copies). The
label is corrected. `out/` rebuilt.

## 2026-11-19 11:08  Floor plan: a sweep for stale labels

The user asked for every stale label to go and for everything now identified to be named.

**Method.**
- Every block (628) that was provisional or whose text said "not traced", "believed", "unknown" or the
  like was checked against the master list and the notes.
- Every signal name in a label was checked against the netlist.

**Changed.**
- `mal`: was "believed a latch per bit (partly traced)"; now a static latch per bit, firm (as `ral`).
- `bd1`: its labels now name R4's match (`rc_eq_r4`), the latch gated by `inh_lat`, and the `inh_rc` /
  `inh_lat` inverters and `inh_n`'s driver, instead of "line X" and "NOT X".
- `cdp1`: R8 by its data bus joins, not "believed"; the data bus channel names `db_b0`..`db_b7`.
- `rdp2`: R4's comparator is against the row counter `rc0`..`rc6` (firm), not "believed the row
  counter", and its output goes to `bd1`.
- `amr`: the compared lines are `c4l0`..`c4l3`, not `cdp1`'s old line names.
- `dbus`: D7's input buffer is no longer provisional.
- `tl1`: two gates no longer provisional; the wide metal is labelled as the VSS arm onto R3's top.
- `tl3`: latch C's data join is drawn now.
- `tla`, `bw`: "the step signal b" is now `rc_stepreq_n`; the step formula uses the `rcs_` names.
- `tc1`: `l2_out`/`l3_out` are now `ras_o0_sel2`/`ras_o0_sel1`.
- `tcw`: its latch is marked as the field latch path.
- The input buffer row's extra inverter is named as `inh_ck`'s.
- New provisional block for the metal band north of the top-left strips (`tlb`).

**Removed as superseded** (another fragment now covers them):
- `tc1`'s four "gate columns, not traced" blocks at x 6400-6750 (`tcw`'s);
- `fld`'s "upper group (untraced)" (`tc2`'s);
- `fld`'s "bit-0 source gates, partial" (`tcw`'s latch).

**`operation.md`**: "`amr_eq_r3` is believed to be `amr_eq_r3` ... not joined" corrected: `amr` joined it
firmly on 2026-11-17.

**Still provisional, rightly** (not traced):
- the top-left's last rows, `lc1`'s rest and `lc3`, `tr1`/`tr2`;
- the bottom-centre and bottom-left logic;
- `bc3`'s groups, `bd1`'s two lower gate columns, `bd2`'s lower part;
- `cdp1`'s rows D/E and the large cells of `cdp2`/`cdp3`;
- `larr`'s middle and right columns and carry gaps;
- `tla`'s top lines and the diagonal fan, D7's protection;
- the comb cells by LPSTB/RES, the small cell by the die marking.

## 2026-11-19 11:17  Floor plan: the logic west of the large cells

The user saw untraced logic left of the row A cells with no block on the floor plan.

**New provisional blocks in `floorplan.txt`**, from views of the clean shot:
- a gate column x 7460-7800, y 7580-8440: about six units with loads; its top is the gate group at
  the end of `inh_ck`'s tap row, `eof` (c);
- gates below it at y 8620-8800;
- the cluster x 7850-8300, y 8260-8800 ("the logic beside row A" of `cdp3`'s notes).

**Master list.** The `cdp3` (continue) row now covers them: region 7460-10850 x 7580-8800.

**Labels.** `cdp2`'s "row of large cells" and `cdp3`'s "row A cells" are the same six cells cut by
the two packages' boundary. They are now labelled "six large cells, upper part (cdp2's row D)" and
"... lower part (cdp3's row A)".

`out/` rebuilt.

## 2026-11-19 11:23  Die coverage: a stricter check, and the gaps it found

The user asked for confirmation of full die coverage. `tools/coverage.py` said 0.0% "in neither", but
it counts a spot as covered if any region anywhere in the master list contains it, done packages
included. `/trace6845` picks only from the Queue, so a gap can hide inside a done or partial
package's region. That is how the logic beside the large cells went unnamed.

**The tool.** `coverage.py` now also prints "in a Queue row's region" and "untraced and in no Queue
row" (CLAUDE.md: the latter must hold only empty field, supply metal and the die marking). The first
run gave 0.8%.

**Fixed.**
- Twelve partial packages had no Queue row: `larr`, `bc1`, `rdp2`, `fld`, `tcw`, `bw`, `rdp1`, `ur`,
  `urch`, `mra`, `rax`, `clock`. Each now has a "(continue)" row at the end of the queue, with its
  Left list. `fld`'s old 6250-12480 x 3880-12480 blanket is cut to 6250-7100 x 3880-6200.
- `busL` gains its northern part, 6450-7600 x 6750-10400: the strip between the left-centre logic and
  the central datapath, with `bw`'s crossing field.
- `lc1`-`lc3` gains the band 4400-6450 x 6350-6900 above `lc1`.
- `mra` (continue) starts at y 6850, for three small gates at the counter array's top.
- `padring`'s west region now reaches x 2400, closing a 50 px sliver beside `larr`.
- `teststr` names the die marking.
- An untraced gate group at `cdp4`'s bottom-left corner (x 7560-7860, y 13650-14030) goes to `cdp4`
  (continue) and gets a floor-plan block.

**Now 0.4% is untraced and in no Queue row.** I looked at each piece:
- the wide supply plates east of the right datapath (x 16950-17700, y 2675-8375);
- the supply band at y 5325-5525;
- empty field east of `wl` and at `cdp4`'s bottom-right;
- a few slivers of wiring under 100 px.

## 2026-11-19 11:38  Pull requests #17 and #19; Refresh

Both reviewed at the user's request, and closed with the user's approval.

**#19** (Tom Seddon): adds a missing count ("29 meetings, 16 ports without a partner") to a `tl3`
handoff that was processed and removed on 2026-11-18. Merging it would have brought the file back.
Closed with the count noted in the comment.

**#17** (dp111, dbus-cont, open since 2026-11-17): compared with main as planned.
- The bits 4-7 latches and bus drivers (its `trace/dbus_h.txt`) against Tom's `dlat`: all 40
  transistors pair up within 25 px, and every gate and channel terminal is on the same named net. That
  is an independent confirmation of `dlat`.
- Its `dbus_n9` is `dbus`'s `d0_out_n` = NOT `dbus_do0_in`, the same two transistors.
- Not merged:
  - it rewrites `dbus`'s files, which Tom has since traced;
  - dp111's cost report shows part of this work on Opus (Fable-only rule; no further non-Fable merges).
- Its one new piece is `dbus_le`'s route south from (16774,15935) to a NOR under `bd2`'s VSS rail,
  `dbus_le` = NOR(`cs_d`, X). It is recorded as a lead in the `bd1`-`bd3` row, to be traced again on
  Fable, and as "believed" in `operation.md`'s `dbus_le` row.
- The `dlat` row and `operation.md`'s data bits 4-7 row now note the confirmation.

**Handoffs:** none waiting. **Claims:** none.

**Refresh:**
- Renamed (`names.py compare`: only names changed): `lc2_w8254`, `lc2_w8731` -> `rst_c`.
- `operation.md`: totals unchanged (2,379 nets, 4,282 transistors; 839 of 1,261 equations firm).
- `out/` rebuilt: 0 errors, 0 warnings, 0 names outside the glossary.
- Coverage: 63.0% traced; untraced and in no Queue row 0.4% (supply plates and empty field).

## 2026-11-19 12:26  Handoff: eof run 3, the NOR on R5's inverted match

Traced by this session with `/trace6845` (claim 6a6bfba, merged 17714ea, claim released); the handoff
processed at the user's request.

**What came in** (`notes/blocks/eof.md`, piece `r5nor`; 4 transistors, no uncertain items):
- The four polys that leave `tl1`'s strip north at x 2362-2515 end on one gate in the band, at
  x 2330-2550, y 2180-2470: `tl1_w2637` = NOR(`tl1_w5936`, `rcs_c1`, `sl_eq_r5_n`) (firm).
- So R5's match, inverted once, is gated by `rcs_c1` and `tl1_w5936` into the data of the middle
  cluster's latch A. It is the first load of `sl_eq_r5_n` that is drawn; its poly ends there.
- The load is fed by a diffusion strap from seven contacts under the plane north of y 1963, named
  `vcc` from the load's orientation only (its Ambiguity 8; for `padring`).
- Review: one full round on Fable, no finding that changes a connection; three geometry fixes (two
  pad edges, the head and its contacts), both `sameconn` runs identical.

**Checks:** overlay of the merged piece at 1.7x on the chip-2 metal and clean shots
(`cache/scratch/eof_handoff_ov.png`): every outline on its feature. Full extraction 2,379 nets,
4,286 transistors, 0 errors, 0 warnings; `tools/unsure.py`: 90 nets joined only through uncertain
items, none of them this piece's.

**Applied:**
- Master list: the `eof` row's task (a) marked done as a gate, with what is next on that path
  (latch A's enable `tl4_w4590`, by `tl3` (continue)'s row (4250,2810)); the `tlb` row no longer
  leads the end-of-frame group and lists what is left of the band (four of its six edge wires closed).
- `notes/blocks/tl1.md`: the three ports north and the Not done entry now say where the polys end.
- `floorplan.txt`: the band's coarse block trimmed to x 2600-6400.
- `notes/operation.md`: totals (4,286 transistors; 840 of 1,262 equations firm).
- No Re-read item, no new AMB entry.
- `out/` rebuilt: 0 names outside the glossary. Coverage: 63.1% traced; untraced and in no Queue
  row 0.4%, as before.

**Handoffs:** none waiting. **Claims:** none.

## 2026-11-19 12:50  Handoff: eof run 4, inh_src's open ends (driver not found)

Traced by this session with `/trace6845` (claim 54fc826, merged a4d06bc, claim released); the handoff
processed at the user's request.

**What came in** (`notes/blocks/eof.md`, piece `isrc`; wiring only, no uncertain items):
- `inh_src` is the clear of `bc2`'s latch unit a (joined to that unit's clear pad by an alias; the unit still waits for R31).
- Its west bus line is drawn on from the pad (9770,18081) to a pad (8967,17735), from which a metal runs
  north along x 8968 for 2,470 px with two tap pads and an end pad, and a second metal west. Four polys
  leave those pads west into the gate column x 8650-8800: stubs and ports, not followed.
- The task's goal, `inh_src`'s driver, is **not found**: every end seen is a gate.
- Review: one full round on Fable, no finding that changes a connection; three geometry or comment fixes.

**Checks:** overlay of the metal x 8968 and its two tap pads at 1.3x
(`cache/scratch/eof_handoff_ov2.png`): on the features. Full extraction 2,378 nets (one fewer: the
join), 4,286 transistors, 0 errors, 0 warnings; `tools/unsure.py` does not list `inh_src`.

**Applied:**
- `trace/trunks.txt`: the metal x 10225 shortened from y 15886 to y 15905 (it ends on the ring of the
  pad (10226,15912); it was drawn 48 px over open poly). `tools/sameconn.py HEAD`: connections identical.
- Master list: the `eof` row's task (b) marked not found, with the six places to go on from; notes
  added to the `trunks` (continue), `bc1` (continue) and `bc2`/`bc3`/`bc4` rows.
- `notes/blocks/trunks.md` and `bc2.md`: the ends that are now followed.
- `notes/operation.md`: the net count.
- No Re-read item, no new AMB entry. The clear pad's placeholder name is left as an alias of `inh_src` for the next refresh.
- `out/` rebuilt.

**Handoffs:** none waiting. **Claims:** none.

## 2026-11-19 12:59  Refresh

At the user's request, after the two `eof` handoffs of today. **Handoffs:** none waiting. **Claims:** none.

**Renamed** (`names.py compare`: only names changed; one batch):
- the clear of `bc2`'s latch unit a (its placeholder is under Former names in the glossary) -> `inh_src`:
  a firm join, `eof`'s piece `isrc`, link G; the alias in `trace/eof.txt` is dropped by the rename.

**Left on purpose** (`names.py candidates`, section 1): `ar#_q`, `d#_in`, the `*_tab` cell pins (a
cell's own name for a pin), `cdp2_c_s1_bus`/`cdp2_c_s2_bus` (kept with their row under AMB-019).
Section 2 (joins through uncertain geometry) untouched, as the rule says.

**`operation.md`** (seventh refresh): header (2,378 nets, 4,286 transistors; 840 of 1,262 equations
firm, unchanged since `eof`'s run 3); the `inh_src` row now gives the equation of the latch it clears
(marked); R5's path (the NOR into latch A's data) was taken in with run 3. No equation changed status
(`eq_before` against `eq_after`). AMB-001 to AMB-037 and R1-R45 unchanged.

**`out/`** rebuilt: 0 errors, 0 warnings, 0 names outside the glossary, 630 floor-plan blocks.
Coverage: 63.3% traced; in some package region 99.9%; untraced and in no Queue row 0.4%.

## 2026-11-19 13:50  Bus-field packages renamed to lower case

At the user's request ("please sort out the issue with busL"). `tools/claim.py` accepts only lower-case
prefixes, and the master list named four packages with a capital, so none of them could be claimed
(found when `/trace6845` tried to take the queue's second row). A prefix names files and a branch,
which must not differ only by case, so the names changed, not the tool:

- busL -> `busl`, busB -> `busb`, busC -> `busc`, busT -> `bustop` (`bust` is taken: the contributor
  package that did busT's data bus part).
- Changed in `notes/work-packages.md` (with a paragraph on the rule), `floorplan.txt`,
  `notes/blocks/bust.md`, `dbus.md`, `dpad.md` and a comment in `trace/bust.txt`. Left as written:
  earlier journal entries, `notes/blocks/eof.md` (one mention; `eof` is claimed and being edited)
  and the waiting handoff.
- `out/` rebuilt: 2,382 nets, 4,290 transistors, 0 errors, 0 warnings (this takes in `eof`'s run 5,
  whose handoff `handoffs/eof-20261119-133240-431bea8.md` is still to be applied).

**Handoffs:** one waiting (`eof` run 5). **Claims:** `eof` (tom-seddon), `tlb` (this session; to be
released for `busl`, which the user wants done next).

## 2026-11-19 16:18  Handoffs: eof runs 5 and 6, busl runs 1 and 2, lc3 runs 2 and 2b, eofw; a test of effort

At the user's request ("apply waiting handoffs"). Seven handoffs, applied together.

**What came in**

- `eof` run 5 (richtw1; piece `g7700`, 4 transistors): the gate at the end of `inh_ck`'s tap row, one
  AND-OR-INVERT under column 0's VSS rail (firm).
- `eof` run 6 (Tom Seddon; piece `ff3`, 19 transistors): the clock of `lc2`'s first flip-flop is the
  slave output of a third copy of `lc2_ff` in `lc3`'s column A; `lc2_w8475` = NOT(`eof_w9472` AND
  (`eof_w9255` OR `eof_w9505`)) (firm).
- `lc3` runs 2 and 2b (Matt Godbolt; 37 transistors and the wiring): two more counter stages (E4 a
  turned copy, B0 folded over both columns, by hand): **the ripple counter has five stages**, clocked by
  `lc2`'s through line `lc2_x6432`; the gate pair: **`lc1_w7170` = NOT `lc3_w9470`** (the driver `eof`
  (f) asked for) and `lc2_w9079` = NOT `lc3_w9299`, so `lc2_w9125` chooses between the counter's fourth
  and fifth outputs. R31 done for `lc3`. Released: done but for its edges.
- `busl` runs 1 and 2 (richtw1; wiring, 16 nets): `cdp3`'s row H west outputs reach eight diffusion rows
  of the left array (piece `h8`); `cdp4_bus_s#` = `cdp4_in_s#` for all eight slices, each also on a poly
  row of the left array (piece `ch1`). Claimed, continuing.
- `eofw` (richtw1; wiring, new package): the three wires of `g7700` followed to named nets:
  **`tc2_r5589` = NOT(`lc1_w7170` AND (`inh_ck` OR `tc2_sr_g`))**, and **`tc2_sr_g` is `lc1_w7908`**, the
  enable of latch D. Two open ends at a corner pad (7446,8732) into `cdp3`'s gate column.

**The test of effort** (user: "test the results against a high effort trace"). `g7700` had been traced
in a 15-minute run. A fresh agent at high effort traced the gate again from the commit before that
run, without sight of it (39 minutes). On the gate the two agree in every connection: the same four
transistors and equation, and drawn together they merge net for net with no short (coordinates within
4 px; where they differ at the wires' ends the second is nearer the photos by 3-5 px). The difference
was how far the wires were followed: the first run left each at a port within 1,200 px, the second
reached a named net on each. That part became `eofw`, reviewed by a fresh reviewer at high effort
(round 1: no findings that change a connection). The user then asked for a high-effort review of the
other pieces claimed that day: `eof`'s `r5nor` and `isrc`, `busl`'s `h8` and `ch1`, each by a fresh
Fable reviewer at high effort. **None found anything that changes a connection**; the geometry and
notes items they found are in the master list's `eof` and `busl` rows for the claims' holders. One
sample, and the two tracing runs had different briefs, so "followed further" cannot be put down to
effort alone; the lesson taken is a rule for follow tasks (below).

**Checks:** overlays at 1.15-1.5x of `ff3` (`cache/scratch/handoff/h_ff3.png`), `lc3`'s stage B0 and its
wiring east of the counter (`h_b0.png`, `h_lc3e.png`): on the features; `eofw`'s joins at 3-4x
(`cache/scratch/eofw/join1.png`, `join2.png`). Full extraction 2,400 nets, 4,344 transistors, 0 errors,
0 warnings; `tools/unsure.py`: 90 nets joined only through uncertain items (none of them from these
packages' own geometry: the cell copies carry `lc2`'s `?D`).

**Applied:**
- Master list: `eof` row ((c) done, (d) done as far as `eof` goes, (f)'s driver found by `lc3`; what is
  left; the geometry fixes waiting in `trace/eof.txt`; the follow-task rule); `busl` row (status, what
  arrives from `lc3`, what `eofw` draws in the northern part, the second-look review's notes);
  `lc1`-`lc3` row (`lc3` done but for its edges; `lc1`'s corrections); `cdp3` (continue), `bl0`,
  `urch` (continue) rows; R31 (done for `lc3`), R45 (applied by `eof` run 6 and `lc3`). `eofw`'s row,
  added to the Queue at 15:25 so that it could be claimed, is moved to the contributor table as done.
- `notes/tracing-guide.md`: trap 30 gets `tl5_tracks.py`'s "hole" where a line has stepped off its
  track; new **trap 37** (a second copy of a cell may be folded: try the halves, read every row end);
  section 5 gets a paragraph on `@alias` (one canonical name per net, no chains; a label of the
  canonical name in one's own file) and one on follow tasks (finished at a drawn net, not at the first
  pad). No Re-read item: no earlier block is known to be affected by trap 37, and the first run of
  `g7700` misread nothing.
- `trace/cdp3.txt`: column 0's VSS rail `M 7623,8450 y11200 w=46` began 106 px too far north (bare
  ground at x 7612-7660 down to y 8548 in both metal shots; seen independently by both tracers of
  `g7700`); now from y 8556, its label moved onto it. `tools/sameconn.py HEAD`: connections identical.
- Corrections sections added to `notes/blocks/lc1.md`, `lc2.md`, `lc3.md`, `cdp3.md`, `cdp4.md`,
  `larr.md`, `tc2.md`. Not edited: `notes/blocks/eof.md` (claimed: Tom Seddon) and `busl.md` (claimed);
  what concerns them is in their master-list rows.
- `floorplan.txt`: the coarse block for the left-centre strip 3 removed (`lc3`'s and `eof`'s fragments
  cover it); the gate column west of the large cells trimmed to start below `eof`'s gate (y 7860).
- No new AMB entry (none proposed).
- `out/` rebuilt. Coverage: 65.5% traced; in some package region 99.9%; untraced and in no Queue row 0.4%.

**Handoffs:** none waiting. **Claims:** `busl` (waitingforvsync), `eof` (tom-seddon).

## 2026-11-19 16:20  Handoff: eof run 7, the latch on R4's match closes

It arrived (bb9af14) while the entry above was being pushed; applied in the same sitting.

**What came in** (Tom Seddon; piece `r4lat`, 1 transistor, three uncertain items): the load of the lower
half of `bd1`'s latch on R4's match, a block under `bd1`'s band east of the ground rail
(x 13937-13992, y 15630-15702), with a tie box (13889-13913, 15660-15682) drawn uncertain. With it
`bd1_q` is `bd1_n2` (alias) and the pair is cross-coupled: `bd1_n1` = NOT(`bd1_n2` OR (`inh_lat` AND
`rc_eq_r4`)), `bd1_n2` = NOT((`bd1_an` AND `inh_lat`) OR `bd1_n1`) (marked: the two load ties): a
transparent latch of R4's match, open while `inh_lat` is high. Where its outputs go is not found.
Review: round 9 on Fable, no finding that changes a connection.

**Checks:** overlay at 4x, metal and clean (`cache/scratch/handoff/h_r4lat.png`): on the features.
Full extraction 2,399 nets (one fewer: the alias), 4,345 transistors, 0 errors, 0 warnings.

**Applied:**
- Master list: `eof` row ((e): the latch complete, what is left of it); `bd1` row and the `bd1`-`bd3`
  queue row; **R42 extended** in this commit: in an open group beside a rail the clean shot can be
  inverted as a whole and read as a misregistration; to re-read with that in mind: `bd1`'s gate column
  y 15850-16125, `bd2` (rest).
- `notes/tracing-guide.md`: trap 28 gets the same.
- `notes/blocks/bd1.md`: a corrections section; `floorplan.d/bd1.txt`: the lower half's line.
- `trace/bd1.txt`: the band `P 13896,15630:13996,15650` ends at x 13993 (`eof`'s review round 9);
  `tools/sameconn.py HEAD`: connections identical. Its two `?` items that `eof` re-read are left
  marked (`trace/eof.txt` draws firm items over both).
- No new AMB entry. `out/` rebuilt.

**Handoffs:** none waiting. **Claims:** `busl` (waitingforvsync), `eof` (tom-seddon).

## 2026-11-19 16:26  Refresh

At the user's request, after the eight handoffs above. **Handoffs:** none waiting. **Claims:** `busl`
(waitingforvsync), `eof` (tom-seddon).

**Renamed:** nothing. `names.py candidates`, section 1, lists only the deliberate aliases, as before
(`ar#_q`, `d#_in`, the `*_tab` cell pins, `cdp2_c_s1_bus`/`cdp2_c_s2_bus` under AMB-019).

**Left on purpose:** the day's new joins are placeholder to placeholder, kept as `@alias` until one
side has a functional name: `tc2_r5589` / `eof_w7818`; `tc2_sr_g` / `eof_w7718` / `lc1_w7908`;
`lc1_w7170` / `lc2_w8474` / `eof_w7777` / `lc3_w9432`; `lc2_w9079` / `lc3_w9337`; `lc3_w9947` /
`lc2_x6432`; `cdp4_bus_s#` / `cdp4_in_s#` (eight); `bd1_n2` / `bd1_q` (through an uncertain tie).
Section 2 (joins through uncertain geometry) untouched, as the rule says. The glossary rows of
`tc2_sr_g` and `tc2_r#` now say where those two lines go.

**`operation.md`** (eighth refresh): header (2,399 nets, 4,345 transistors; 847 of 1,276 equations
firm, from 840 of 1,262). Taken in: the gate on `inh_ck`'s tap row is named on every side,
`tc2_r5589` = NOT(`lc1_w7170` AND (`inh_ck` OR `tc2_sr_g`)) (firm, now also in the name `lc1_w7170`:
`lc3`'s gate pair ends on the same line); latch D's enable `lc1_w7908` is `tc2_sr_g`; "Not
established at all" no longer says the ripple counter's length and consumers are untraced (five
stages, clock `lc2_x6432` with its source open, `lc2_w9125` choosing between the fourth and fifth
outputs). The tracers had already written the counter's table, `lc1_w7170`'s driver and the latch on
R4's match. Against the last refresh's equations: 16 new (9 firm), two gone by name (`lc3_w9432`,
`lc3_w9337`, now `lc1_w7170` and `lc2_w9079`), none changed status. AMB-001 to AMB-037 and R1-R45
unchanged in range (R31, R42, R45 edited).

**`out/`** rebuilt: 0 errors, 0 warnings, 0 names outside the glossary, 647 floor-plan blocks; the
floor plan looked at round the left-centre strips and the new routes (`cache/scratch/refresh/fp_crop.png`):
no label over another. Coverage: 65.5% traced; in some package region 99.9%; untraced and in no Queue
row 0.4%.
