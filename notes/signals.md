# Signal names

Every named net in the trace is listed here, by name or by pattern. `tools/build.py`
checks this: a net name that no row of these tables covers is reported as
"not in notes/signals.md" in the build output and in `out/report.txt`.

In a pattern, `#` stands for a number and `*` for any run of letters, digits and
underscores. The first column of every table is read by the build, so keep each pattern
in backticks in the first column.

## Rules

1. **A signal is named for what it is** as soon as tracing shows what it is: pin names
   as on the datasheet (`e`, `rw`, `ma5`), register numbers (`r1_b3_q`, `wr_r6`), counter
   bits (`hc0`, `rc3_q`), results (`h_eq_r0`).
2. **A signal that is not identified is named for where it is**: a block prefix and a
   local name (`cdp3_h_c5_q`, `rcs_e4`). The table says what is known about it. When it
   is identified it is renamed everywhere with `tools/rename.py` (trace files, notes,
   floor plan) and its old name goes into "Former names" at the end of this file.
3. Suffixes: `_n` inverse (active low), `_q` output of a latch or register bit, `_b#` bit
   number (bit 0 = least significant), `_s#` slice number where the bit order is not
   established, `_dly` a delayed copy, `_buf` a buffered copy.
4. **`_u` marks an open join**: a piece of wire believed to be the same net as the name
   without the suffix, whose connection has not been drawn (`ck_a_u`). Every
   `_u` name is a task; the build lists them.
5. Rows and slices are places and keep their numbers in the notes ("row r18", "slice
   s3"); the tables below say which bit each one is.

## Where the bits are

Counters (mid-right array, rows r0-r18 from the top, `notes/blocks/mra.md`):

| Rows | Counter | Bit of row |
|---|---|---|
| r18 ... r11 | horizontal character counter, `hc0` ... `hc7` | r18 = bit 0 (carry enters there), r11 = bit 7 |
| r10 ... r4 | character row counter, `rc0` ... `rc6` | r10 = bit 0, r4 = bit 6 |
| r3 ... r0 | horizontal sync width counter, `hsw0` ... `hsw3` (4 bits, on the character clock; compared bit for bit with R3's nibble in the upper right datapath) | r3 = bit 0, r0 = bit 3 |

Counters in the left array's upper rows (rows u0-u8 from the top, `notes/blocks/ur.md`; the
same bit cell as the mid-right array's):

| Rows | Counter | Bit of row |
|---|---|---|
| u8 ... u4 | scan line counter, `sl0` ... `sl4` (5 bits; stepped by `lc_step`; compared bit for bit with R5) | u8 = bit 0 (the carry enters there from the left column), u4 = bit 4 |
| u3 ... u0 | 4-bit counter, `c4l0` ... `c4l3` (compared with R3 bits 4-7 in `amr`: believed the vertical sync width counter; same clocks as the scan line counter) | u3 = bit 0, u0 = bit 3 |

Right datapath, lower array (R0, R1, R2 and their comparators): slice s1 = bit 0, s2 =
bit 1, ... s7 = bit 6, **s0 = bit 7** (from the counter lines: `hc0` arrives at s1, `hc7`
at s0). Upper array (R4, R6, R7, R5 and their comparators): the slices that the notes of
`rdp2` call sm1, s0, s1, ... s5 (left to right) are **bits 0 to 6** (from the scan line
counter's lines at R5's comparator, `notes/blocks/rdp1.md`). R3's four slices (t0-t3 in
the first notes) are bits 0-3 of that nibble.

Central datapath (registers identified by their write strobes, `notes/blocks/wrs.md`):

| Rows | Register | Slices |
|---|---|---|
| `cdp1` row A | R8 (6 bits) | columns c2-c7 (cells a0-a5). Bit order from the data bus (`notes/blocks/bust.md`): slices 5, 4, 1, 0, 3, 2 are bits 0, 1, 4, 5, 6, 7 (`r8_b#_*`); bits 0 and 1 are the two whose AND is `ras_shift` |
| `cdp1` row C, comparator row B | R9 (5 bits) | slices 1-5 = columns c3-c7; slice k = bit 5 - k, from the data bus (`r9_b#_*`) |
| `cdp2` row A | R11 (5 bits) | s3-s7 |
| `cdp2` row C, comparator rows B | R10 (7 bits) | s1-s7; s3-s7 compared, s7 = bit 0 ... s3 = bit 4 (from the `rax_o#` lines); s1, s2 the two mode bits |

## Supplies, pins and pad circuits

| Name | What it is |
|---|---|
| `vcc`, `vss` | supplies |
| `clk`, `e`, `rw`, `rs`, `cs`, `res`, `lpstb` | the pin itself (pad node) |
| `cs_p`, `e_p`, `rs_p`, `rw_p` | the pin's node behind its protection strip, at the input of its buffer |
| `clk_n`, `clk_b` | NOT CLK and CLK buffered (input row; `clk_b` feeds the phase generator) |
| `e_n`, `e_b` | NOT E and E buffered. `e_b` is the E that the bus control logic uses |
| `rw_a`, `rw_b`, `rw_c`, `rw_d`, `rs_a`, `rs_b`, `rs_c`, `rs_d`, `cs_a`, `cs_b`, `cs_c`, `cs_d` | the four inverters of each input chain: `_a` and `_c` inverted, `_b` and `_d` true. The core uses `_d` |
| `res_n`, `res_b` | NOT RES and RES buffered. `res_b` runs down the top-left logic to line 3 of the poly bus at x 5100-5290. `res_b` and `lpstb_b` go on south in `tl5`'s poly bus to pads (5190,6845), (5237,6803) and are the two inputs of `lc1`'s NOR: `rst` = NOR(`lpstb_b`, `res_b`), the reset (`notes/blocks/eof.md`, piece `x1`) |
| `lpstb_n`, `lpstb_b` | the same for LPSTB; `lpstb_b` ends on line 4 of that bus |
| `rst`, `rst_n`, `rst_a`, `rst_b`, `rst_c` | `rst` = NOR(`lpstb_b`, `res_b`): high while the RES and LPSTB pins are both low (traced, firm: `lc1`'s gate 3, its inputs joined by `eof` run 2). `rst_n` = NOT `rst` (gate 4); `rst_a`, `rst_b`, `rst_c` = NOT `rst_n` (gates 5-7), three buffered copies in `rst`'s sense. `rst_a` clears `tl4`'s and `tl5`'s latches (four) and `tl4`'s pair; `rst_c` clears latches B, C and D of `lc2` (D is the `lc_step` latch, so `lc_step` is high during it). **Believed**: the chip's reset; the datasheet's wording on LPSTB during reset is not re-read. Named 2026-11-19 (`lc1_w7304` etc.: Former names) |
| `ma#`, `ra#`, `hsync`, `vsync`, `disptmg`, `cudisp` | output pins (pad node) |
| `*_drv_in` | the signal from the core that an output pad cell receives (the pad is its inverse) |
| `*_pu`, `*_pd` | inside an output pad cell: gate of the pull-up fingers (first inverter) and of the pull-down fingers (second inverter) |
| `d#_in` | data pin D# behind its protection, at its input buffer. With the pad's series strip drawn it is the pad's own net: an alias of `d#` (`trace/dpad.txt`) |
| `d#` | data pins D0-D7: the bond pad, the metal of the output fingers, and (D0-D6) the series strip, the protection node and the line to the input buffer. On the chip the strip is a diffused resistor between pad and node; the netlist has one net (`notes/blocks/dpad.md`) |
| `d_hiz` | output disable of the data pins, one line common to the eight pad cells (metal x 17631-17651, y 7374-18850, a contact in each cell): high turns off both output gates of every data pad. Driven from the bus-interface column; the driver is not traced. The "P_x" of the first notes |
| `d#_out_n` | the per-bit data line into data pad cell #, from the bus-interface column: while `d_hiz` is low the pin D# is its inverse. The "P_y" of the first notes. `d0_out_n` is the thin metal x 17438-17459 down the whole column, driven by an inverter at its foot (y 16415-16590); `d1_out_n` is drawn from D1's pad cell to the column's west edge at (16950,16344), driver not found |
| `d#_pu`, `d#_pd` | inside data pad cell #: gate of the pull-up fingers, NOR(`d_hiz`, `d#_out_n`), and gate of the pull-down fingers, NOR(`d_hiz`, `d#_pu`) |
| `d#_a`, `d#_b`, `d#_c`, `d#_d` | the four inverters of data input buffer #: `_a`, `_c` inverted, `_b`, `_d` true. Buffers 0-5 are cell `dbus_in`, 6 and 7 cell `dbus_in2` (`notes/blocks/dbus.md`). `d#_d` feeds the input latch: in the data bus column for bits 0-3; `d4_d`..`d7_d` leave it west at x 16950 and enter the latches of bits 4-7 in the column x 16466-16848 (`notes/blocks/dlat.md`) |
| `dbus_do0_in` | input of the inverter at the foot of the data bus column that drives `d0_out_n` (`d0_out_n` = NOT `dbus_do0_in`): a poly along y 16444-16463 from a pad (16993,16451), fed by a metal that leaves the column west at (16950,16712), not followed. The bit the chip puts on D0, in true sense |
| `dbus_cap#b` | # = 0-5: a plain diffusion rectangle beside data input buffer # with a contact that carries only a dot of metal, joined to nothing. The capacitor that a metal strap would have put on `d#_b` (whose pad nearby also has only a dot): a metal option not taken (`notes/blocks/dbus.md`, "The capacitor taps of chains 1-5") |
| `d#_d_n` | NOT `d#_d`: the inverter inside data input latch # (`notes/blocks/dbus.md`; bits 4-7: `notes/blocks/dlat.md`) |
| `dl#_q`, `dl#_q_n` | the data input latch of bit # in the data bus column: two cross-coupled AND-OR-invert gates, transparent while `dbus_le` is high. `dl#_q` follows pin D#; `db_b#` = NOT `dl#_q_n` (a static inverter drives the bus bit). Bits 4-7 are the same latch in the column west of it (cell `dlat_lat`), and their `dl#_q_n` run west and north to four inverters above the latches (cell `dlat_drv`) that drive `db_b4`..`db_b7` (`notes/blocks/dlat.md`); `dl7_q_n` and `dl6_q_n` are `dl7_q_n` and `dl6_q_n` (aliases in `trace/dlat.txt`) |
| `dbus_le` | enable of the data input latches: a vertical metal x 17243-17262 down the data bus column from y 8988 (to y 13614, then west); west of x 16950 it is the metal that runs south along x 16819 past the latches of bits 4-7 (a pad on each of their two gate bands) then turns west at y 15802 and runs on south along x 16774, out of that column, passing over the box ends of `d5_out_n`, `d4_out_n` and `d3_out_n` without contact (`notes/blocks/dlat.md`; followed to y 16104). Source not traced |

## Clocks

| Name | What it is |
|---|---|
| `ck_a` | phase high only while CLK is low (non-overlapping with `ck_b`). Slave clock of the horizontal and 4-bit counters |
| `ck_b` | phase high only while CLK is high. Master clock of the horizontal and 4-bit counters. Held low while `inh_ck` is high |
| `ck_a_u` | the line that gates the second pull-down of the horizontal counter's `_nx_g` nodes: followed in poly to the `ck_a` bus line of the clock block; join not drawn |
| `ck_out` | NOT CLK from the big three-stage buffer: the main internal clock, distributed along the bottom and left edges |
| `clk_tl` | NOT `ck_out`, i.e. CLK polarity, for the top-left logic: made by an inverter at (2626,7908) in the left column beside upper row 2 of the left array, where the left-edge trunk of `ck_out` arrives, and run back north (thin metal x 2457, poly y 5587, bus lines D and B). In the step logic it enables the first term of `rcs_n4200` and gates units at y 3765 and y 4410 (those two contacts, (3150,3812) and (3150,4418), are not in the trace yet). It does **not** gate the band y 4535-4558 on `rcs_cond`'s column (once read as the pass transistor of `rcs_cond_lat`): that gate's row ends 14 px short of `clk_tl`'s pad (3152,4548) and is on `tl3_w3982`, and the band is a pull-down of `rcs_cond`'s gate (`notes/blocks/tl2.md`, runs 2 and 4) |
| `ck_a_pu`, `ck_b_pu` | gates of the source-follower pull-ups of the two phase drivers |
| `ck_g#` | outputs of the clock gate row: `ck_g1`, `ck_g2` = `ck_b` delayed by one and two inverters, `ck_g3`, `ck_g4` = the same for `ck_a` |
| `ck_clkn` | NOT `clk_b` inside the phase generator |
| `ck_t`, `ck_n#`, `ck_ga` | internal nodes of the main clock buffer (first stage output, second stage output, gate of the output pull-up) |

## The inhibit signal

One core signal stops both the horizontal counter's master clock and the row counter's
step. Its source is not traced. It is a line of the bottom bus field with at least four
branches (followed 2026-11-16 from the strobe channel 3,700 px west, `notes/blocks/trunks.md`).
All five names below are copies of it.

| Name | What it is |
|---|---|
| `inh_src` | the signal itself: a bottom-bus line that reaches the gate of the driver of `inh_n`, a metal north along x 10225, a poly east into the bottom-centre logic at (10470,16950) and the bus further west than x 8978; **it is `lc2_x6299`**, the first through line of the left-centre strips (one net since `eof`'s piece `isrc4`, 2026-11-19: `@alias inh_src lc2_x6299`), so it arrives down the left bus field from `lc2`'s east edge (6450,8630); source unknown, east of that point |
| `inh_n` | NOT `inh_src`: "line X" of the notes. Input of the lone inverter in the input buffer row |
| `inh_ck` | NOT `inh_n` from that inverter: holds `ck_b` low in the clock block, and is distributed along the bottom bus field and up the left bus field ("S" in the notes). It goes on north as the top-left logic's track A (`notes/blocks/eof.md`, run 2: line S runs on from (6690,8366) up a staircase of metals to `tl6`'s metal x 6105 and on to the pad (6400,4005); one net on firm geometry; renamed 2026-11-19, see Former names): so it is also the enable of the vertical control's master/slave latch pairs and of `tcw`'s field latch path |
| `inh_rc` | NOT `inh_n` from the upper inverter in the strobe channel: runs up the wiring channel, over the top of the counters, to the row counter's step gate (`rc_step` = NOR(`inh_rc`, `rc_stepreq_n`)) |
| `inh_lat` | NOT `inh_n` from the lower inverter: gates the latch in the strobe channel's gate column |

## Counters

For `<bit>` read `hc#` (horizontal), `rc#` (character row), `hsw#` (horizontal sync
width), `sl#` (scan line) or `c4l#` (the left array's 4-bit counter, compared with R3 bits 4-7 in `amr`: believed the
vertical sync width counter). Each
bit is a master-slave pair (`notes/blocks/mra.md`; the node letters used there are given
in brackets).

| Name | What it is |
|---|---|
| `hc#`, `rc#`, `hsw#`, `sl#`, `c4l#` | the bit as the rest of the chip sees it: the buffered **master** (node n1). The comparators compare this, not the slave |
| `hc#_q`, `rc#_q`, `hsw#_q`, `sl#_q`, `c4l#_q` | slave latch (q): takes `_d` on the slave clock |
| `*_q_n` | NOT `_q` (g1) |
| `*_m` | master latch node (a): takes `_nx_g` on the master clock |
| `*_mb` | node b, joined to `_m` through a pass transistor gated by `cnt_gab`; gate of the feedback device from `_d` to `_m` |
| `*_m_n` | NOT `_m` (p3) |
| `*_d` | NOT `_m_n`: the copy of the master that the slave gate passes to `_q` (d) |
| `*_nx` | next-value node of the bit (m): pulled low through networks of the carry and `_q`; its pull-up and one branch are not resolved, so the next-state function is not extracted |
| `*_nx_n` | NOT `_nx` (nb) |
| `*_nx_g` | NOR(L3 line, `_nx_n`) (na): the next value, forced low while the counter's L3 line is high |
| `*_ci_n` | NOT carry-in of the bit (n2) |
| `*_co` | carry out of the bit = carry-in AND `_q` (x); carry-in of the next row up |
| `*_tab` | a diffusion tab pulled low by `_q_n` (spare finger); in rows r7-r10 and r15-r18 it is on the look-ahead line |
| `*_rb` | lower part of the diffusion R in the `_nx` network; its continuation is not resolved |
| `*_z` | far side of the weak always-on device from `_q`; ends as a free stub as traced (re-read item R9) |
| `*_md`, `*_mt` | metal straps between a row and its neighbour in the chain column (lower, upper); their joins are in `notes/blocks/mra.md` |
| `hc_ci`, `rc_ci`, `hsw_ci` | carry-in of each counter's bit 0. Sources not traced |
| `hc_lo4_set`, `rc_lo4_set` | look-ahead line: low while any of bits 0-3 is clear, i.e. high when `_q` of bits 0-3 are all 1 (group lines B and A) |
| `rc_ck_m`, `rc_ck_s` | master and slave clock of the row counter (bus lines E and D), made by the generator below |
| `rc_l3`, `hsw_l3` | the L3 line of the row counter (from the west along y 13005) and of the 4-bit counter (from the north). What they carry is not known; for the horizontal counter L3 is `ck_a` |
| `lc_ck_m`, `lc_ck_s` | master clock (line L1) and slave clock (rail x 4218) of both counters of the left array's upper rows: one line each through all nine rows. Made by a second copy of the row counter's clock generator, in the left column beside rows u0-u2: `lc_ck_s` = NOR(`lc_ck_m_dly`, `lc_step`), `lc_ck_m` = NOR(`lc_step_n`, `lc_ck_s_dly`) |
| `lc_step`, `lc_step_n` | the step pulse of those two counters and its inverse: both counters step once per pulse. `lc_step` comes from the left-centre logic (poly up x 5012, west along y 6368 over the counters, metal down x 2412); its gate is not traced |
| `lc_ck_m_n`, `lc_ck_m_dly`, `lc_ck_s_n`, `lc_ck_s_dly` | inverse and two-inverter delay of each of the two clocks, inside that generator |
| `c4l_l3`, `sl_l3` | the L3 lines of those two counters (while the line is high every bit's master is loaded with 0). The 4-bit one's comes from the north: its thin metal runs at x 3794-3808 from a pad (3801,6286) in `tl3`'s strip down to a diagonal step at y 6674-6698, and that pad is the end of a wire from `tl4`'s strong inverter, so **`c4l_l3` is `c4l_l3`** = NOT `tl4_w4243`, the inverse of the right cluster's latch (`notes/blocks/tl3.md`, run 11; an alias, `tl4`'s name is the net's until a refresh). The 5-bit one's comes from a pad (3757,6410) on a poly along y 6410 that arrives from the west (drawn to x 3560, not followed); that poly does not run on east to the pad (3968,6410), which is another net (`rcs_thin_e`) |
| `c4l_gab`, `sl_gab` | their pass-gate lines (the gates of the m/mb pass transistors). The 4-bit one's comes from the north: its thin metal runs at x 4077-4091 from a pad (4083,6327) in `tl3`'s strip, shifts 11 px east at y ~6602, and the pad's poly row runs east through `tl4`'s strip to the pad (4929,6323) of `c4l_gab`, so **`c4l_gab` is `c4l_gab`**, the net that clears `tl5`'s latch c (`notes/blocks/tl3.md`, run 11; an alias); its driver is not found. The 5-bit one's comes from a poly from the east along y 6520, ending on a contact at (4087,11005) |
| `cnt_gab` | gate line of the `_m` to `_mb` pass transistors of all 19 bits (x 12902), fed from the top by band H4. **Also** the line y 4354 through the five `ral` cells, where it gates one of the two pull-downs of each cell's NOR (`ral_n1_s#` = NOR(`ral_a_s#`, `cnt_gab`)), so a high level sets that RA output high; the cells only read it: from `wl`'s contact (11392,7210) on H4 north along x 11396 / 11242, through the cross-under at x 11243-11694, east along y 4287 and a poly L into the band (`trace/ral.txt`, firm). Source not traced |
| `cnt_l2_a`, `cnt_l2_b`, `cnt_l2_c` | three pieces of the metal line L2 that passes through the rows without a contact |
| `cnt_la_a`, `cnt_la_b`, `cnt_la_c` | three pieces of the metal x 12285 through the rows; no contact found in the rows (re-read item R8). `cnt_la_a` feeds an inverter west of the counters |
| `cnt_la_a_n` | NOT `cnt_la_a`; leaves north |
| `cnt_bus_a`, `cnt_bus_b` | bus lines A and B of the channel between rows r3 and r4; not identified. B runs from the datapath channel 3 to the upper right datapath |

## Row address selector (`notes/blocks/ras.md`)

Eleven pass transistors between the scan line counter and five output nodes.

| Name | What it is |
|---|---|
| `ras_o#` | output bit # of the selector (# = 0-4). Expected to be the row address that goes to pin RA#; not yet followed to the pad |
| `ras_straight` | NOT `ras_shift` (made in the island `tc1`): gate line (left poly band) of the five pass transistors `sl`# to `ras_o`# |
| `ras_shift`, `ras_shift_n` | the mode line and its inverse: `ras_shift` = `r8_b1_q` AND `r8_b0_q`, R8's bits 1 and 0 (the interlace field: both set = interlace sync and video), made by a NAND and an inverter below R8's row (`notes/blocks/shm.md`). Gate line (right poly band) of the four pass transistors `sl`# to `ras_o`(#+1), and input of the island `tc1` |
| `ras_o0_alt1`, `ras_o0_alt2` | the two sources of `ras_o0` when `ras_shift` is high: `alt1` when R9's bit 0 is set, `alt2` when it is clear. `ras_o0_alt1` = `rc0_n` XOR `fld_y_b` (`notes/blocks/fld.md`). `alt2` runs from its pad (6928,4786) on a poly row west through the crossing field to a pad (6447,4786) and on west in metal past x 6400 (`notes/blocks/tc2.md`); not followed further (follower: end (6059,4876)) |
| `ras_o0_sel1`, `ras_o0_sel2` | made in the island `tc1`: `sel1` = `ras_shift` AND R9 bit 0, `sel2` = `ras_shift` AND NOT R9 bit 0. Gates of the pass transistors from `ras_o0_alt1` and `ras_o0_alt2` to `ras_o0`, and of the island's own AND-OR |
| `rax_o#` | output of the unit that takes selector output `ras_o`# (# = 0-4): pulled to VSS by a transistor gated by `ras_o`#; with the unit's load (`trace/tc2.txt`, piece 8: gate tied to the output, on the VCC rail x 8117-8163) NOT `ras_o`#, the complement of the row address (AMB-011). Each runs from its unit's pad at x 7836 through the nest of metals, along a line of the central datapath's channel 1 (the comparator's through track: `cdp2_trk_s7` is `rax_o0` ... `cdp2_trk_s4` is `rax_o3`), north along x 10981-11154, under the supply metal at y 4331-4500 and east to the logic in front of the RA pad drivers (`notes/blocks/rab.md`) |

## Row counter clock generator and step

| Name | What it is |
|---|---|
| `rc_stepreq_n` | request to step the row counter, active low. Made by a three-input NOR in the top-left logic |
| `rc_step` | NOR(`inh_rc`, `rc_stepreq_n`): the step pulse. The row counter's masters load while it is high |
| `rc_step_n` | NOT `rc_step` |
| `rc_ck_m_n`, `rc_ck_m_dly` | NOT `rc_ck_m`, and `rc_ck_m` delayed by two inverters; `rc_ck_s` = NOR(`rc_ck_m_dly`, `rc_step`) |
| `rc_ck_s_n`, `rc_ck_s_dly` | the same for `rc_ck_s`; `rc_ck_m` = NOR(`rc_step_n`, `rc_ck_s_dly`) |
| `rcs_in1`, `rcs_in2`, `rcs_in3` | the three inputs of the NOR that makes `rc_stepreq_n`. `rcs_in2` = NOR(`rcs_w2`, `rcs_e4`), `rcs_in3` = NOR(`rcs_e3`, `rcs_e4`). `rcs_in1` = NOT `rcs_mv` (`notes/blocks/tl3.md`, run 8; until then read as NOR(`rcs_mu`, `rcs_mv`)): it comes from the middle cluster by the bus field at x 4279 |
| `rcs_w2`, `rcs_c1`, `rcs_b1` | `rcs_w2` = NOT `rcs_c1`; `rcs_c1` = NOR(`rcs_a2`, `rcs_b1`); `rcs_b1` = NOR(`rcs_x1`, `rcs_a2`, `rcs_u3425`) |
| `rcs_cond_n` | NOR(`rcs_in2`, `rcs_in3`) = `rcs_e4` OR (`rcs_e3` AND `rcs_a2`): the step condition inverted (called m2 in the block notes) |
| `rcs_cond` | NOR(`rcs_cond_n`, `tl3_w3982`): the row counter's step condition apart from `rcs_in1`, held low while `tl3_w3982` is high (the second pull-down is the band `tla` had as a pass transistor: `notes/blocks/tl2.md`, run 4, AMB-009). On bus line A's piece A3; first gate of the series pair in `rcs_n4200`, and the input of the inverter that drives `rcs_cond_lat` |
| `rcs_cond_lat` | NOT `rcs_cond`: the output of an inverter between R2 and R3 at y 4005-4145 (node `tl2_w4080`; the join runs through the load's `?` tie), on a poly row y 4011-4030, a metal x 3042 and two poly pads; gate of the lower pull-down of `rcs_bd3330`'s unit, so that the pair `rcs_n4200` / `rcs_bd3330` is a latch for `rcs_cond` that is open while `clk_tl` is high. **Not a latch node**, as its name says and as `tla` first read it: the buried contact of AMB-009 is not there (`notes/blocks/tl2.md`, run 4). A rename is proposed to the coordinator |
| `rcs_e3`, `rcs_e4`, `rcs_a2`, `rcs_x1` | inputs of the step logic. **`rcs_e3` = NOT `tl4_w3850`** (`notes/blocks/tl4.md`, eighth run: the inverter at (4400-4967, 3781-3911) of the right cluster drives `tla`'s bus line E by the track x 4496 and the sixth bus line y 2728; `tl4_w3850` is `tl5_w5761`, the south bus line x 5412, not followed further); `rcs_a2` is **not identified**. `rcs_x1` is one of three inputs of `rcs_n4200` = NOT((`clk_tl` AND `rcs_cond`) OR `rcs_x1` OR `rcs_bd3330`) (`tl2`'s run 3: the gate row `tla` had drawn as one poly on `rcs_x1` is two). `rcs_e4` gates everything except `rcs_in1`; it is a long control line (17,000 px, five gate loads) that runs beside `res_b` and `lpstb_b`. Its driver is in the west column of the first cluster: `rcs_e4` = NOR(`tl1_w4678`, `tl1_w4937`), at (2607,4890) (`notes/blocks/tl1.md`); `tl1_w4937` is the net of the middle cluster's thin metal x 3948-3962 and so `tl3_e3550`, R9's match AND NOT `tc2_o5175` (marked: `tl3`'s run 9, row `tl3_tm3955`); `rcs_x1` clears five latches (latch C too); `tl1_w4678` is the output of two latches in series (open on `tl1_w3594` low-and-`tl1_w3678`-low, then on `tl1_w3594` high; data `tl1_w2857`; cleared by `rcs_x1`). **`rcs_x1` = NOT `lc1_w7170`** (`notes/blocks/eof.md`, piece `x1`): `tl5`'s bus line x 5107 ends on a pad (5105,6761) of `lc1`'s metal M_a, the output of the gate column's separate inverter (`rcs_x1`, an alias); its input arrives from `lc2`'s strip on a thin metal |
| `rcs_u#` | output of a unit of the step logic cluster that has no better name yet, by the y of its buried contact (`rcs_u3288` = NOR(`rcs_g3245`, `rcs_bd3330`), where `rcs_bd3330` is the node of the AND-OR-INVERT unit below `rcs_n4200`'s, NOT(`rcs_n4200` OR (`clk_tl` AND `rcs_cond_lat`)), cross-coupled with `rcs_n4200` through that unit's load tie (a `?` item): `notes/blocks/tl2.md`, run 3; `rcs_u3425` = NOT `rcs_bc3460` = `rcs_e3` OR `rcs_e4` OR `tl2_w3722` OR `clk_tl`, third input of `rcs_b1`: `rcs_bc3460` is a four-input NOR, two pull-downs in `tla`'s unit at y 3892 and two in the unit above it, `notes/blocks/tl2.md`, run 3) |
| `rcs_n#` | output of an AND-OR-INVERT unit of the first cluster (`rcs_n4200` = NOT(`rcs_cond` AND `clk_tl` OR `rcs_x1` OR `rcs_bd3330`), the last through a load's `?` tie: `notes/blocks/tl2.md`, run 3); leaves on a metal strap x 2845-2885 |
| `rcs_iso#` | a gate poly of the first cluster on which no connection has been found, by its x. `rcs_iso2958`: a vertical poly x 2950-2968, y 3447-3547, under the west edge of the VSS rail R3, gate of a second transistor from `rcs_u3425` to VSS (its diffusion link is drawn uncertain). If the rail contacts it, the transistor is always off |
| `rcs_g#` | an input of the cluster that arrives on a poly line from outside, by the y of that line. `rcs_x1` is `rcs_x1` (alias, `trace/tl2.txt`: the row ends on a tap of the bus metal x 3456); `rcs_g3245` comes down the upper piece of the same track (y 2674-3256) from a pad (3454,2683) whose row leaves east along y 2683 (`notes/blocks/tl2.md`) |
| `rcs_ba#`, `rcs_bb#`, `rcs_bc#`, `rcs_bd#`, `rcs_be#`, `rcs_bf#`, `rcs_bg#` | a piece of bus line A-G beside the first cluster (x 3090-3380) whose driver was not known when it was named, by the y of its top end. Found since: `rcs_bc3460` = NOR(`rcs_e3`, `rcs_e4`, `tl2_w3722`, `clk_tl`); `rcs_bd3330` = NOT(`rcs_n4200` OR (`clk_tl` AND `rcs_cond_lat`)) (`notes/blocks/tl2.md`, run 3) |
| `rcs_bp#`, `rcs_bq#`, `rcs_br#`, `rcs_bs#`, `rcs_bt#`, `rcs_bu#`, `rcs_bv#` | the same for the second bus field (x 4140-4420; tracks P-V at x 4148, 4192, 4235, 4279, 4322, 4365, 4409) |
| `amr_oa_c#`, `amr_ob_c#` | the two vertical metals of `amr`'s slice in column # (c1 x 11880, c2 12270, c3 12660; c0's two are drawn in `trace/bust.txt` and carry the bus names `db_b4` / `c4l0`), named before the slice was traced. Inner (`oa`, x 11916 + 390(#-1)): **a data bus bit** (bits 5, 6, 7), written into R3 bits 5-7 on `wr_r3`. Outer (`ob`, x 12001 + ...): **an input**, the bit that R3's bit is compared with (aliases of `c4l1`, `cdp1_l4632`; c3's is `cdp1_l4676`, which west of `cdp1` is fed from the row y 4635, not `ra_eq_r9`: `notes/blocks/r9m.md`, correction). To bus lines y 5047/5135/5177 and 4657/4696/4742 (`notes/blocks/amr.md`) |
| `r9m_l3` | the bundle's line 3: track P's lower piece (x 4148, y 3371-3596, contact (4148,3588) with a poly west into the middle cluster), the stub at y 3376, metal up x 4194, west along y 2641 / 2599, the pad (4912,2641), a poly stepping down to the pad (5405,2681), metal along y 2685 and down x 5848 to (5845,5045). Driven by `tc2_o5175` (joined by `tl6`, contact (5845,5043)) |
| `sl_eq_r5_n` | the metal from the pad (5400,2596) (whose poly goes north at x 5175, not followed) east along y 2599, down x 6022, across the crossing field to the pad (7855,4676) and the row y 4676, which turns south near x 8190 at `cdp1`'s west edge. Drawn on in `trace/tc2.txt` (piece 13): south along x 8186, east along y 4717 to the pad (8246,4716), a metal east and south to the pad (8290,4850), a poly east to (8352,4850), where it ends in a box read as a buried contact onto a diffusion at `cdp1`'s west edge. **That diffusion is the output node of an inverter (`trace/eof.txt`, piece `r5inv`): `sl_eq_r5_n` = NOT `sl_eq_r5`, R5's match inverted.** West of the pad (5400,2596) its poly runs on along y 2551 to `tl4`'s bus line 1 and by a cross-under at x 3606-3800 to `tl2`'s metal (piece `r5w`): `sl_eq_r5_n` are aliases of it in `trace/eof.txt`; it leaves the top-left strips north at (2493-2508,2500), loads not found. It does not become a line of `cdp1`'s channel |
| `rcs_mu`, `rcs_mv` | two bus pieces of the second bus field (x 4192), once read as the two inputs of the NOR that makes `rcs_in1`. **Since `tl3`'s run 8 only `rcs_mv` is an input of `rcs_in1`** (`rcs_in1` = NOT `rcs_mv`): the transistor under gate `rcs_mu` pulls down `rcs_mn3852` (the column `tla` drew from it to `rcs_in1`'s node is field for 70 px). `rcs_mu` = NOT `ra_eq_r9` (an inverter at y 3413), an input of `rcs_mn3852` and of `tl3_e3550`; `rcs_mv` = NOR(`tl3_e4372`, `tl3_e4852`): a NOR under the middle cluster's east rail at y 4345-4514 drives its track by a contact (4193,4420) (`notes/blocks/tl3.md`, run 7; one uncertain 10 px link at the output box); the poly of the track's south pad (4192,4743) goes on east across (4250,4744) |
| `rcs_mn#` | output of a unit of the middle cluster, by the y of its output. `rcs_mn3852` = NOR(`tl3_e3712`, `rcs_in1`, `rcs_mu`) (`notes/blocks/tl3.md`, runs 7 and 8): the third pull-down is the transistor under gate `rcs_mu` at (4081,3940), which `tla` had on `rcs_in1`; its drain goes west under the VSS rail as a diffusion band y 3966-3984 and north under the thin metal x 3948-3962 to this unit's load strip. So `rcs_mn3852` = `tc2_o5175` AND `rcs_mv` AND R9's match. It leaves north on the bus piece x 4233 to y 2852 |
| `rcs_thin_e` | thin metal E of the first cluster (x 2903-2923, y 2986-5400 and on south to about y 6036), over the east loads. Its north end is found: west along y 2986, north at x 2696 to a contact (2695,2768), poly west along y 2768, contact (2326,2768), metal x 2326 south to contacts (2326,3243) and (2326,3333). There it is the **select** of the mux unit `tla_w3417` and the input of the inverter `tla_w3505`. Its south end runs on to a pad with a contact (2913,6327), and a poly row leaves it east along y 6316-6337, across `tl2`'s strip and on in `tl3`'s to a pad with a contact (3973,6329), whose metal runs south to `ur`'s pad (3968,6410); that pad's poly leaves east along y 6402-6422 (seen to x 4256, not drawn). It is not the 5-bit counter's L3 line, as `ur` had drawn it (`notes/blocks/tl3.md`, run 11). The driver is not found |
| `rcs_thin_w` | the piece of thin metal W (x 2688-2708) drawn at y 4940-5330, over the west loads of the first cluster; what it joins is not read, and it is not shown to be one metal with the upper piece (`rcs_u3288_n`, which follow.py ends at y 4002) |
| `rcs_u3288_n` | NOT `rcs_u3288`: output of the inverter at the top of the west column of the first cluster (rail gate under R1 at (2626,3112), strong load), carried by the upper piece of thin metal W (contact (2738,3027), x 2696, y 3026-4000). Its loads are not traced (contact candidates at y 3690-3949) |
| `tl1_w#` | a wire of the westmost strip of the top-left logic (`notes/blocks/tl1.md`), by the y of its defining contact or poly row. `tl1_w3636` = NOR(`tl1_w3594`, `tl1_w3678`) (unit at y 3558-3742, output on the metal x 2283 to gates of the two units below); `tl1_w4243` = NOT `tl1_w4287` (inverter at y 4215-4345; the first latch's output and the second latch's data); `tl1_w4678` (= NOT(`rcs_x1` OR `tl1_w3594` AND `tl1_w4360` OR `tl1_w4703`), the unit at y 4590-4800; a buried contact puts it on a poly L to the NOR) and `tl1_w4937` (metal x 2370 from the row y 5460 under the foot, which comes from the east) are the two inputs of the NOR that drives `rcs_e4`; `tl1_w2857`, `tl1_w3678`, `tl1_w3594` enter on the poly rows y 2857, 2812, 2899 from the east; `rcs_x1` is the metal x 2457 (y 4012-5372) with the row y 5372 under the foot, and the gate of one pull-down in each of the units at y 3982 and y 4590; `tl1_w4070` = NOT(`rcs_x1` OR `tl1_w3636` AND `tl1_w3752` OR `tl1_w4287`) is the unit at y 3982-4215, a copy of the one at y 4590, and with `tl1_w4287` = NOT(`tl1_w2857` AND `tl1_w3636` OR `tl1_w4070`) (y 3732-3982) the first latch; `tl1_w4360` = NOT `tl1_w4243` and `tl1_w3752` = NOT `tl1_w2857` are the south and north pieces of the thin metal x 2557-2573 over the west column, each from the output of the inverter of the unit above (y 4345 and y 3737) to the second series gate of the unit below; `tl1_w4703` (= NOT(`tl1_w4243` AND `tl1_w3594` OR `tl1_w4678`), the other side of the second latch) and `tl1_w4095` are the two pieces of the thin metal x 2742, each from the load plate of the three-input gate of the unit above (y 4487 and y 3879) to the gate of the third pull-down of the unit below; `tl1_w4095` is an alias of `tl1_w4287` (one net through the `?` tie of that plate: an assumption); the west column of the small cluster (y 5690-6175) is a third latch of the same build (a second copy of the two units), open while `ck_out` is high: `tl1_w5706` = NOT `tl1_w3333` (the thin metal x 2557-2573, y 5697-6120), `tl1_w5841` = NOT(`tl1_w3333` AND `ck_out` OR `tl1_w6022`) (the thin metal x 2742, y 5829-6059), `tl1_w6022` = NOT(`tl1_w5978` OR `ck_out` AND `tl1_w5706` OR `tl1_w5841`) (the latch's output: metal x 2414 and the row y 6195 east out of the strip); `tl1_w5978` (pad (2326,5978), metal x 2326 on south) is its clear; `tl1_w3333`, its data, is a 4,700 px wire from a pad (2563,2550) at the top, by metal to (2197,3333) and by poly down the west side to the row y 5800; `tl1_w5936` (= NOT `tl2_w6070`, the third latch's output buffered by `tl2`'s two inverters) enters on the row y 6237 from the east and runs by the metal x 2500, the row y 5935 and a wire up the west margin (poly x 2094, metal x 1980, poly x 2137, metal x 2064: two cross-unders of the MA driver lines) to the poly along the strip's north edge (y 2506), which turns north out of the strip at x 2380; north of y 2790 only wiring: `tl1_w3333` leaves east by a metal from the pad (2826,2553), `tl1_w3678` by a metal from the pad (2830,2811); `tl1_w2637` and `sl_eq_r5_n` are polys from the north (x 2455, x 2500) that turn into the rows y 2636 (to a pad (2827,2637) and a metal east) and y 2591 (east); None identified |
| `tl2_w#` | a wire of the second strip of the top-left logic (`notes/blocks/tl2.md`), by the y of its defining strip or row. `tl2_w4260`: the poly that is the gate of the load of `rcs_bd3330`'s unit and, by a vertical in the gap between thin metal E and R3 (x 2927-2947, y 4235-4300), the west gate of the third pull-down of `rcs_n4200`'s unit at (2970,4240); aliased to `rcs_bd3330` in `trace/tl2.txt` across the load's `?` tie (Ambiguity 17 of the block notes), which makes the two units a cross-coupled pair. `tl2_w4080` = NOT `rcs_cond`: the node of the inverter between R2 and R3 at y 4005-4145 (box under thin metal E at (2915,4085)), aliased to `rcs_cond_lat` across its load's `?` tie (run 4; Ambiguity 19). `tl2_w4452`: the node between the two series pull-downs of `rcs_bd3330`'s unit (gates `clk_tl` above it, `rcs_cond_lat` below), a diffusion under R3 at y 4425-4462. `tl2_w6070` = NOT `tl1_w6022`: the node between the two inverters of the small cluster's east half (drain strip y 6064-6084, buried contact (3053,6067), and the poly loop that is the gate of the inverter driving `tl1_w5936`). In the bus field east of the first cluster (run 2, wiring only): `tl2_w3722` is track F's upper piece (x 3326, y 2630-3732) with a row east along y 2639 from its top pad and a row west along y 3722 from its bottom pad, which is a gate of `rcs_bc3460` = NOR(`rcs_e3`, `rcs_e4`, `tl2_w3722`, `clk_tl`) at (3045,3722) (run 3); not identified. (Track F's lower piece, track G's lower piece and the U-shaped poly under track G carry tl3's names `tl3_w4546`, `tl3_w5025`, `tl3_w4373`: they are the far ends of tl3's rows.) The same run joined, on geometry without `?`, groups of names that are now aliases in `trace/tl2.txt`: `rcs_x1` (track I, x 3456: one signal that clears tl1's two latches and tl3's latch and is an input of `rcs_b1` and `rcs_n4200`), `tl1_w3594` = `tl3_w3722`, `tl1_w2637` = `tl3_w3333`, `rcs_a2` (so `rcs_a2` = NOR(`tl1_w3594`, `tl3_w3803`)), `tl3_w3419` = `tl3_w3896`; and where its rows meet tl3's at x 3533: `rcs_x1` (so `rcs_x1` also clears tl3's latch B and is an input of `tl3_w4243`), `tl3_w3982` = `tl3_w4290`, `tl3_w3939` = `tl3_w4112`, `tl3_w4763` = `tl3_w4414`, `tl3_w4373` = `tl3_w4503`. `tl3_w3982` (not an alias: tl3's name kept for the whole net) is track F's middle piece (y 4278-4470), track J's lower piece (x 3499, y 3972-5374 and an arm east) and the rows y 4461 and y 4285; a poly under track A takes it to the gate of the pass transistor at (3046,4546), which `tla` had on `clk_tl` |
| `tl3_e#` | a wire of the middle cluster's east column (`notes/blocks/tl3.md`), by the y of its row or of its metal's corner: `tl3_e4243` = NOR(`inh_ck`, `rcs_mv`); `tl3_w4978` (latch B's enable) = NOR(`inh_ck`, `tl3_e5114`); `inh_ck` is track A (x 4148, five gate pads) and the thin metal x 4105 north of it; **it is `inh_ck`** (run 9: the row of its south pad (4104,5633) is `tl4`'s row of `inh_ck`; an alias, with `tl4`'s `inh_ck`, the row of its pad (4146,4510) into `tl4`'s three-input NOR). The thin metal's north end is a pad (4103,2899) on the row y 2899 of `tl1_w3594`, so **`tl1_w3594` (the enable of `tl1`'s two latches, an input of `rcs_a2`, `tl3_w3722`) is `inh_ck` too**: marked, the thin metal is drawn uncertain over six node boxes (run 10; `notes/blocks/tl3.md`, Ambiguity 13). Latch C (y 4514-4970, the mirrored copy of `tl1_ua`, `tl1_ub`): `tl3_e4537` = NOT `tl3_e4635`; `tl3_e4720` = NOT(`tl3_e4635` AND `inh_ck` OR `tl3_e4852`); `tl3_e4852` = NOT(`rcs_x1` OR `inh_ck` AND `tl3_e4537` OR `tl3_e4720`): open while `inh_ck` is high, data `tl3_e4635` (from the east at (4250,4635)), clear `rcs_x1` (a metal x 4192 from the east at (4250,5895), with a second pad at (4192,5373) on the row y 5371 of `rcs_x1`: **the clear is `rcs_x1`**, run 9, an alias); the data's driver takes latch B's inverted output (`tl3_e5240` is `tl3_w5025`, by the row y 5415 across the foot), output `tl3_e4852` (track x 4236 to a row y 4460 west under the rail); `tl3_e4675` is the thin metal x 3908 on `tl3_e4720`'s load plate (aliased across the plate's tie); `rcs_mv` = NOR(`tl3_e4372`, `tl3_e4852`) (a NOR under the rail at y 4345-4514; `tl3_e4372` is a row from the east at (4250,4373), and is `tl3_w4546`, NOR 3's output, by the row y 5500 across the foot: run 9); `tl3_e3550` = NOR(`rcs_mu`, `tc2_o5175`) (the NOR under the rail at y 3450-3660; its only exit is its load plate, which carries the north end of the thin metal x 3948-3962; that metal's south pad is on `tl1_w4937`'s row, so `tl3_e3550` is the second input of `rcs_e4`'s NOR: marked, row `tl3_tm3955`); `tl3_e3712` = NOT `tc2_o5175` (the inverter at y 3655-3745), whose poly is the upper gate of `rcs_mn3852`'s unit; `rcs_mv` is a wire that only passes through the bus field (poly in at (4250,4915), a pad (4234,4918), metal x 4236 south and out at (4250,5766)). None identified |
| `tl3_e3000`, `tl3_e3028` | the top unit E1 of the middle cluster's east column (y 2950-3090, `notes/blocks/tl3.md`, run 8): `tl3_e3000` = NOT `tl3_e3028`, an inverter under the east rail. Its node's way out is its load plate, which is one poly with the row y 2957-2973 to the pad of `tl3_w3373`, latch A's enable: aliased to `tl3_w3373` in `trace/tl3.txt` across the plate's uncertain tie, so `tl3_w3373` = NOT `tl3_e3028`. `tl3_e3028` is the gate row, from the east at (4250,3028); not identified |
| `tl3_e4635`, `tl3_e5240` | `tl3_e4635` = NOT `tl3_e5240`: the inverter under the south end of the middle cluster's east rail (y 5180-5300, `notes/blocks/tl3.md`, run 8). Its output row leaves the strip east at (4250,5197) and ends on a pad (4278,5198) of a metal x 4279 whose north pad (4278,4636) is on the row of `tl3_e4635`, latch C's data: both pads measured, the track not drawn (it lies in `tl4`'s strip), hence `_u`. `tl3_e5240` is its gate row, from the east at (4250,5240); not identified |
| `tl3_tm3955`, `tl3_tm3955_u` | the thin metal x 3948-3962 that runs the length of the middle cluster's east column between the rails, over the loads: from a pad (3930,3614) on the load plate of the NOR `tl3_e3550` to a pad (3953,5458) on the row of `tl1_w4937` in the cluster's foot. Drawn end to end since `tl3`'s run 9, firm but for six stretches over load-tie boxes, where neither metal shot shows it (`?M`); taken to make no contact on the way. Both names and `tl1_w4937` are aliases of `tl3_e3550` (across those stretches and the plate's uncertain tie), which gives `rcs_e4` = NOR(`tl1_w4678`, `tl3_e3550`), marked (`notes/blocks/tl3.md`, Ambiguities 6, 10, 11) |
| `tl4_w#` | a wire of the fourth strip of the top-left logic, the vertical control's right cluster (`notes/blocks/tl4.md`), by the y of its defining row or pad. A latch at y 3906-4390, a copy of `tl1`'s: `tl4_w4025` data (row y 4025, metal x 4452), `tl4_w4068` enable (metal x 4625), `rst_a` clear (metal x 4537), `tl4_w3928` = NOT `tl4_w4025`, `tl4_w4113` = NOT(`tl4_w4025` AND `tl4_w4068` OR `tl4_w4243`), `tl4_w4243` = NOT(`rst_a` OR `tl4_w4068` AND `tl4_w3928` OR `tl4_w4113`): the output, on the metal x 4494 south. Above it `tl4_w3113` = NOR(`tl4_w3070`, `tl4_w3178`) (unit at y 3012-3222, output north on the metal x 4408), and a second latch at y 3225-3765 with the same circuit, laid out by hand: data `tl4_w3070` (track x 4318), enable `tl5_w3505` (`tl5`'s latch a's enable: its row y 2976-2996 runs on west to the pad (4452,2985) of the track x 4452's north piece), clear `rst_a`, `tl4_w3245` = NOT `tl4_w3070` (metal x 4680-4707), `tl4_w3390` = NOT(`tl4_w3070` AND `tl5_w3505` OR `rst_a` OR `tl4_w3178`) (metal x 4851-4881), `tl4_w3178` = NOT(`tl4_w3245` AND `tl5_w3505` OR `tl4_w3390`): the output, on the track x 4410 to the NOR and `rcs_e3` = NOT `tl4_w3850` (inverter at y 3781-3911, output north on the metal x 4496). Below the latch `tl4_w4545` = NOR(`tla_w3417`, `inh_ck`, `tl4_w4590`) (unit at y 4410-4645; `inh_ck` a row from the west at y 4502, `tl4_w4590` the track x 4362, output south on the metal x 4626). Below that a cross-coupled pair at y 4645-5000: `tl4_w4686` = NOT(`tl4_w4718` AND `tl4_w4590` OR `tl4_w4850`) and `tl4_w4850` = NOT(`rst_a` OR `tl4_w4545` OR `tl4_w4686`); `tl4_w4718` from the north on the track x 4581, `tl4_w4850` out south on the track x 4581. Below that `tl4_w5068` = NOR(`tl4_w4545`, `tl4_w4850`) (unit at y 4990-5170, output on the track x 4625 south), its inverter, whose output is the latch's data `tl4_w4025` = NOT `tl4_w5068` (y 5175-5312, by the track x 4452), and a strong inverter on the latch's output, `c4l_l3` = NOT `tl4_w4243` (y 5297-5465), out on a poly row at y 5445-5465. Other sources and destinations not followed, except `tla_w3417` Seventh run (wiring only, `notes/blocks/tl4.md`): `tl4_w3070` is an alias of `tl3_e4243` (= NOR(`inh_ck`, `rcs_mv`): the track x 4318 leaves the strip west at (4250,4246)), so the second latch's data and the top NOR's gate 1 are `tl3`'s e3 output; `tl4_w3850` (the input of the inverter `rcs_e3`) runs south by the track x 4279, a poly under the track x 4321 and the metal x 4538/4583 to the row y 5761 and is `tl5_w5761` (alias); `tl4_w4590` has `tl3_e5114` and `tl5_w5674` as aliases (a pad (4366,5112) with a row west, and the row y 5675 east); `tl4_w5068` has `tl5_w5500`, `c4l_l3` has `c4l_l3` (rows y 5500 and y 5457 east); `rcs_mv` passes through the strip (aliases `rcs_mv`); on the track x 4279 two more wires of `tl3`'s pass: `tl3_e5240` (the gate row y 5242 of `tl3`'s inverter, from a pad (4279,5265), a metal and the row y 5412, which leaves west again) and `tl3_e4635` (that inverter's output row y 5198, `tl3_e4635` in `trace/tl3.txt` and aliased here, up the metal y 4622-5214 to latch C's data row y 4633): so `tl3_e4635` = NOT `tl3_e5240`. Eighth run (the tracks' north ends and the bus lines y 2500-2740): the inverter's output is `rcs_e3` (renamed from its placeholder 2026-11-19; the inverter's output goes north on the track x 4496 and west on the sixth bus line to `tla`'s bus line E: `rcs_e3` = NOT `tl4_w3850`); `tl4_w4718` is an alias of `tl5_w3245` = NOR(`tl5_w3550`, `tl5_w4160`) (the track x 4581 ends on a pad of `tl5`'s row y 2900); `tl4_w4590` has `tl3_e3028` as an alias (the pad (4366,3030): `tl3_w3373` = NOT `tl4_w4590`) and a second row west at y 2810; `tl3_e4243` has `tl5_w4458` (the enable of `tl5`'s latch c) and `tl4_w3113` has `tl5_w2855` as aliases (two pads and a metal each, to `tl5`'s rows y 2810 and y 2855); `sl_eq_r5_n` is the first of the six bus lines along the top of the strip (y 2512, to a pad (4908,2551) and a row east), source and loads not known. Ninth run (south of y 5790, wiring only): `rcs_x1` runs on into `tl5`'s bus line x 5107 (`tl3`'s metal of latch C's clear runs on along y 5895 to a pad (4629,5891) and `tl5`'s row y 5890, its bus line x 5107). `rst_a`, the clear, is the buffered reset NOR(`lpstb_b`, `res_b`) of `lc1`'s gate column (`notes/blocks/eof.md`, piece `x1`) |
| `lc1_w#` | a wire of the top strip of the left-centre logic (`notes/blocks/lc1.md`), by the y of its defining row or band. In the gate column x 4750-5100: `lc1_w7040` the poly row (y 7040, from the east) whose inverse is `lc_step`; `rcs_x1` = NOT `lc1_w7170` (input on the thin metal x 5038 from the south, output north on the metal x 5080); `rst` = NOR(`lpstb_b`, `res_b`) (two poly rows from the east); `rst_n` = NOT `rst` (on the metal x 5083, south); `rst_a`, `rst_b`, `rst_c` = NOT `rst_n`, three copies, each leaving east on its own poly row; `lc1_w7990` = NOT `rst_c`, leaving south under the metal x 5083. `lc1_w7040` is followed back to gate cluster E in the same strip (row y 7953), where it is the output of the upper unit of a latch (`tl1_ub` turned 180 degrees): `lc1_w7040` = NOT(`rst_c` OR `lc1_w7908` AND `lc1_w7862` OR `lc1_w7928`), with `rst_c` the clear, `lc1_w7908` the enable (a metal from the north at x 6016, through the pad (6213,7908) and on south), `lc1_w7862` (thin metal x 6111) and `lc1_w7928` (thin metal x 5931) the two lines from the latch's lower unit in `lc2`; `rst` also leaves east on a poly row at y 7388; `rst_a` and `rst_b` leave north on the metals x 5125 and x 5299, `rst_c` south on the metal x 5476. In cluster E: `lc1_w7780` = NOT `lc1_w7733` (input from the poly row y 7561 by the metal x 6298; output east on the row y 7780 and south on the metal x 6297). Joined by `eof`'s piece `x1` (2026-11-19): `res_b` is `res_b` and `lpstb_b` is `lpstb_b` (aliases), so `rst` = NOR(`lpstb_b`, `res_b`) and its three buffered copies are copies of the reset; `rst_a` is `rst_a`; `rcs_x1` is `rcs_x1` |
| `tl5_w#` | a wire of the fifth strip of the top-left logic, the gate column east of the rail RB and its bus field (`notes/blocks/tl5.md`), by the y of its defining row or pad. Three latches, mirrored copies of `tl1`'s. Latch a (y 3343-3803): `tl5_w3461` data (row y 3461, track x 5451), `tl5_w3505` enable (track x 5494, y 2984-3728, and a row east out of the strip at y 3722), `rst_a` clear (track x 5233, also latch b's clear), `tl5_w3364` = NOT `tl5_w3461`, `tl5_w3550` = NOT(`tl5_w3461` AND `tl5_w3505` OR `tl5_w3680`), `tl5_w3680` = NOT(`rst_a` OR `tl5_w3505` AND `tl5_w3364` OR `tl5_w3550`): the output, by the track x 5581 to latch b's data. Latch b (y 3820-4280): `tl5_w3982` enable (track x 5538), `tl5_w3841` = NOT `tl5_w3680`, `tl5_w4027` = NOT(`tl5_w3680` AND `tl5_w3982` OR `tl5_w4160`), `tl5_w4160` = NOT(`rst_a` OR `tl5_w3982` AND `tl5_w3841` OR `tl5_w4027`): the output, north on the track x 5625 to the NOR above the latches: `tl5_w3245` = NOR(`tl5_w4160`, `tl5_w3550`) (unit at y 3142-3352, output north on the track x 5451). Latch c (y 4297-4757): `tl5_w4395` data (pad (5665,4395), track x 5667 from the north), `tl5_w4458` enable (track x 5407), `c4l_gab` clear (track x 5494, y 3860 on south, and a row east out of the strip at y 3872), `tl5_w4318` = NOT `tl5_w4395`, `tl5_w4503` = NOT(`tl5_w4395` AND `tl5_w4458` OR `tl5_w4633`) and `tl5_w4633` = NOT(`c4l_gab` OR `tl5_w4458` AND `tl5_w4318` OR `tl5_w4503`), both out east along y 4590 and y 4633. Below it two inverters: `tl5_w4807` = NOT `tl5_w4850` (y 4786-4912; both rows leave east) and `tl5_w4937` = NOT `tl5_w3982` (y 4916-5042; output on the track x 5407 south, the row y 5237 west, the thin metal x 5038 north over the whole column and the row y 2685 west out of the strip). Eight rows cross the west edge at y 2685-2985 to the tracks' north pads: `tl5_w4937`, `tl5_w2722` (track x 5364, y 2722-6114: the output of the strong inverter at the top of the column, y 3040-3156, `tl5_w2722` = NOT `tl5_w2855`), `tl5_w3982`, `tl5_w4458`, `tl5_w2855` (track x 5581, y 2843-3125: that inverter's input), `tl5_w3245`, `rst_a` (its track runs on south to y 6113), `tl5_w3505`. South of the column (wiring only, no device): `c4l_gab` leaves west in metal at y 5982, `rst_a`, `tl5_w2722` and `tl5_w3461` go south in the poly bus (x 5150, 5365, 5453 at y 6350); `c4l_l3`, `tl5_w5500`, `tl5_w5544` are three rows from the east edge (y 4520, 4437, 4480) taken down the tracks x 5581, 5625, 5667 to rows that leave west at y 5457, 5500, 5544; `inh_ck` and `tl5_w5674` rows from the west edge to pads on the east edge at (5666,5632) and (5667,6150); `rcs_mv` a row from the west edge that leaves east at y 6238; `tl5_w5761`, `rcs_x1`, `tl5_w5936` rows from the west edge that turn south into the poly bus (x 5412, 5107, 5063 at y 6350). `tl5_w3982` is an alias of `tl4_w4068` (one net: the row y 2767 runs on to a pad (4910,2767) whose metal is `tl4`'s track x 4625; the extraction prints `tl4_w4068`); `rst_a` is an alias of `rst_a` (the row y 2940 runs on west to the north pad (4537,2940) of `tl4`'s track x 4537); `tl5_w4395` comes from the east edge along y 3659. The other sources and destinations beyond the strip not followed. `rst_a` is `rst_a`, a buffered copy of NOR(`lpstb_b`, `res_b`): the reset (`notes/blocks/eof.md`, piece `x1`); `tl5_w5936` runs on south past y 6880 beside `lc1`'s metal M_a |
| `tr1_w#` | a wire of the first part of the top-right logic rows (`notes/blocks/tr1.md`), by the x of its defining poly in the gate row y 3650-3980. Inverter A (x 11940-12065): `tr1_w12005` its input (poly x 11994-12016 from the north, not followed past y 3650), `tr1_w11960` = NOT `tr1_w12005` its output (poly x 11950-11972 north from the buried contact (11966,3688), not followed past y 3650). The load's gate tie to the output is marked uncertain. Gate B (x 12065-12200): `tr1_w12135` its input (poly x 12124-12146 from the north, not followed past y 3650), `tr1_w12090` = NOT `tr1_w12135` its output (poly x 12080-12102 north from the buried contact (12096,3688)), load tie uncertain likewise. Gate C (x 12195-12330): `tr1_w12265` its input (poly x 12254-12276 from the north, not followed past y 3650), `tr1_w12220` = NOT `tr1_w12265` its output (poly x 12210-12232 north from the buried contact (12226,3688)), load tie uncertain likewise |
| `lc2_w#` | a wire of the left-centre middle strip (`notes/blocks/lc2.md`), by the y of its pad or defining row. Latch B (x 5590-5895, y 8055-8560, `tl1`'s latch upside down): `lc2_w8169` enable (metal x 5560, pads (5558,8169), (5558,8386), north into `lc1`), `lc2_w8450` data (pad (5558,8450), metal south), `rst_c` clear (pad (5472,8254)), `lc2_w8532` = NOT `lc2_w8450` (the cell's thin metal x 5624), `lc2_w8341` = NOT(`lc2_w8450` AND `lc2_w8169` OR `lc2_w8215`): output Na, pad (5514,8341); `lc2_w8215` = NOT(`rst_c` OR `lc2_w8169` AND `lc2_w8532` OR `lc2_w8341`): Nb, not taken out (stub on its box). Latch C (x 5840-6275, y 8525-9030, latch B turned left-right): `lc2_w8646` enable (metal x 6167, pads (6168,8646), (6168,8862)), `lc2_w8906` data (pad (6214,8906)), `rst_c` clear (pad (6257,8731)), `lc2_w9005` = NOT `lc2_w8906` (the cell's thin metal x 6106), `lc2_w8822` = NOT(`lc2_w8906` AND `lc2_w8646` OR `lc2_w8688`): output Na, pad (6257,8822); `lc2_w8688` = NOT(`rst_c` OR `lc2_w8646` AND `lc2_w9005` OR `lc2_w8822`): Nb (box poly stub (6105,8688)). Run 3 (bus field east of the latches): `rst_c` is `rst_c` (latch D's clear, by a cross-under and a metal; the extraction prints `rst_c`); `lc2_w8646` runs north out of the strip on the metal x 6168 and east on a branch y 8301; `lc2_w8906` comes from the north on the metal x 6471 (pad (6470,8127)); `lc2_w8083` the row of latch D's lower node `lc1_w7928` (y 8083, north out at x 6408; an alias: one net through the cell's `?` tie); `lc2_w8474` the poly from the pad (6341,8214) (row y 8474, then y 8514, then west along y 8643; ends not found); `inh_ck` a metal x 6431 from the north that turns east at y 8172. Run 4: `lc2_w9124` = NOT `lc2_w8822`, the output of the inverter below latch C (pad (6168,9124)), on the thin metal x 5967-5981 north through latches C and D into `lc1`; `rst_c` is `rst_c` (latch B's clear: `lc1`'s metal runs on to the pad; the extraction prints `rst_c`); `lc2_w8474` goes on west by a pad (5428,8648) in the run of a metal x 5429 (pads (5428,8516), (5429,8994); the last one's poly is the first gate row of the NOR). Run 5 (as corrected by review round 5): **`lc2_w8450` (latch B's data) = NOT `lc2_w8474`**, an inverter south of latch B, on the thin metal x 5626 (`lc3_m5626` is an alias of it); **`lc2_w9125` = NOT(`lc2_w9034` AND `lc2_w9079` OR `lc3_w9299` AND `lc2_w9210`)**, an AND-OR-INVERT gate below it (node D, no metal on it); `lc2_w9185` its output poly (row y 9185 east under the VCC rail, south at x 5932 into `lc3`; an alias, joined through uncertain items); `lc2_w9034`, `lc2_w9079`, `lc2_w9210` gate rows 2, 3, 5 (from the west); `lc2_w9166` row 4, an alias of `lc3_w9299`; the thin metal x 5756 through latch B carries `lc3`'s name `lc3_m5756` (no contact found in the strip). Run 6: `lc2_w8474` is `lc1_w7170` (one metal up the staircase to `lc1`'s T1; the extraction prints `lc1_w7170`), so `lc2_w8450` = NOT `lc1_w7170`; `lc2_w8907` the poly row y 8907 from drain A's box west to the contact (5386,8951) of the staircase's fourth line (pad (5190,8258) to the strip's south edge on x 5386): an alias of `lc2_w8450` through an uncertain buried contact. Run 7: `lc2_w8298` the poly row y 8298 above the west cluster, from the fifth staircase line's pad (5234,8300) to the pad (4626,8301) of the track x 4562. Round 16: `lc2_w9034` (row 2 of the AND-OR-INVERT south of latch B) is the second flip-flop's slave output; `lc2_w9171` the top node of a stack under the east rail south of the cluster, pulled down by `lc2_w9034`, on into `lc3`. Run 10 (the east column: a second flip-flop, the cell `lc2_ff` turned 180 degrees, clocked by `lc2_w8298`): `lc2_w8992`, `lc2_w8914` (its master's outputs, the copies of `lc2_w8552`, `lc2_w8725`), `lc2_w9034`, `lc2_w8862` (its slave's, the copies of `lc2_w8298`, `lc2_w8692`); `lc2_w9034` leaves south into `lc3` at (5255,9233). Run 9 (gates K3, K4: with latch K a toggle flip-flop clocked by `lc2_w8475` and cleared while `lc1_w7170` is low): `lc2_w8298` = NOT(`lc2_w8692` & (`lc2_w8475` | `lc2_w8725`)) and `lc2_w8692` = NOT(`lc1_w7170` & `lc2_w8298` & (`lc2_w8475` | `lc2_w8552`)). `lc2_w8857` (K3's output node, its loads and thin metal) is an alias of `lc2_w8298` (track C), and `lc2_w8930` (K4's output node T, its load and K3's strip) an alias of `lc2_w8692` (K2's data row): the trace keeps both labels, the extraction prints the older names. Run 8 (west gate cluster, latch K): `lc2_w8552` = NOT(`lc2_w8475` & `lc2_w8298` | `lc2_w8450` | `lc2_w8725`) and `lc2_w8725` = NOT(`lc2_w8475` & `lc2_w8692` | `lc2_w8552`), a gated cross-coupled pair; `lc2_w8475` its enable (thin metal x 4648), `lc2_w8692` K2's data row (y 8692, source to the south not traced), `lc2_w8552` leaves on the thin metal x 4604, `lc2_w8725` on the poly x 4622-4640. Run 7: `lc2_w8127` = NOT `lc1_w7990`, gate 9 of `lc1`'s gate column (output row y 8127 to the pad (5127,8080), metal north into `lc1`). the net is `inh_ck` (`notes/blocks/eof.md`, piece `tcwa`: the metal from the north is `inh_ck`'s, and east of the strip it runs on to `trunks`' line S) |
| `lc3_w#` | a wire of the left-centre bottom strip (`notes/blocks/lc3.md`), by the y of its pad or row. Gate pair x 5540-5900, y 9255-9520 (two inverters, mirror images): `lc3_w9470` lower input (pad (5560,9470), metal x 5560 south), `lc3_w9432` = NOT `lc3_w9470` (poly row y 9429 west, buried contact (5625,9432)), `lc3_w9299` upper input (pad (5560,9299), metal x 5560 north), `lc3_w9337` = NOT `lc3_w9299` (poly row y 9340 west). Boxes are buried contacts only, load gates tied to the outputs (review round 1). Followed in run 2b: `lc3_w9432` is `lc1_w7170` (the lower inverter drives it) and `lc3_w9337` is `lc2_w9079`; `lc3_w9470` comes by crossing row 8 from a metal that enters at (6450,9455) and runs on south; `lc3_w9299`'s source (north) not followed. **Two stages of the ripple counter** (`notes/blocks/lc3.md`, "The counter"): stage E4 (x 4990-5450, y 9150-9945, `lc2`'s cell `lc2_ff` turned): clock `lc2_w9034`, `lc3_w9774`, `lc3_w9696` its master latch's outputs, `lc3_w9644` its slave's second output; its slave's first output is `lc2_w9210`. Stage B0 (x 4440-5480, y 9940-10580, the same gates folded over both columns): `lc3_w9947` its clock (`lc2`'s through line `lc2_x6432`, by a poly row y 9936-9958 from the pad (6211,9948), the metal x 5292-5308 and the thin metal x 4641-4655), `lc3_w10123`, `lc3_w10201` its master latch's outputs, `lc3_w10210` its slave's second output; its slave's first output is `eof_w9255`, the clock of stage W3 (`eof`'s `ff3`) |
| `lc2_x#` | a metal line that passes through the south-east corner of the left-centre middle strip with no contact in it (`notes/blocks/lc2.md`, piece P), by its x at the strip's south edge: `lc2_x6299`, `lc2_x6342`, `lc2_x6387`, `lc2_x6432` (they enter at the east edge at y 8630, 8692, 8756, 9165); `lc2_x6299` is `inh_src` (alias in `trace/eof.txt`, piece `isrc4`) |
| `lc3_e#` | a line that enters the left-centre bottom strip at its east edge (x 6450), by its y there (`notes/blocks/lc3.md`, "The wiring east of the counter"): `lc3_e9577`, `lc3_e9621`, `lc3_e9665`, `lc3_e9708`, `lc3_e9750`, `lc3_e9793` are poly rows 1-6 of the crossing field, each ending on a pad at the top of a vertical metal that runs south and turns diagonal south-west (they cross y 10400 at x 5915, 5851, 5785, 5722, 5655, 5588); `lc3_e9756`, `lc3_e9798` are metals that turn south on x 6342 and x 6428. Sources and destinations not followed |
| `lc3_m#` | a metal track of `lc3` passing over the gate pair with no contact in it, by its x: `lc3_m5626` (x 5615-5638, over the output boxes), `lc3_m5756` (x 5746-5766, over the load tie strips; south of the pair it runs diagonally to x 5647 and ends on a pad (5646,9992), whose poly is crossing row 10, east to the strip's edge); `lc3_m5626` is `lc2_w8450`, on south to a pad (5540,10165) and a poly south |
| `eof_w#` | a wire of the gate at the end of `inh_ck`'s tap row (`notes/blocks/eof.md`, piece `g7700`; x 7541-7775, y 7585-7860), by the y of its row at the gate: `eof_w7818` = NOT(`eof_w7777` AND (`inh_ck` OR `eof_w7718`)), the output, west and north by two pads and a metal x 7272 to a pad (7272,6912), on north in poly; `eof_w7718` (row 2), from a pad (7267,7736) with a metal north to a pad (7313,7215) and one south; `eof_w7777` (row 3), a poly row from the west that enters at (6450,7821) from the left-centre strip (it is not `lc1_w7780`). **Piece `ff3`** (a third copy of `lc2`'s flip-flop cell `lc2_ff` in the left-centre strip's column A, x 4440-4990, y 9185-9990; names by the master's row y + 780): `eof_w9255` its clock (thin metal x 4648, pads (4648,9254) to (4648,9904); fed by an L-shaped metal from the south, x 4553-4575, source not traced), `eof_w9332` = NOT(`eof_w9255` AND `lc2_w8475` OR `eof_w9505` OR `lc2_w8450`) and `eof_w9505` = NOT(`eof_w9255` AND `eof_w9472` OR `eof_w9332`) (the master latch; the copies of `lc2_w8552`, `lc2_w8725`), `eof_w9472` = NOT(`lc2_w8475` AND `lc1_w7170` AND (`eof_w9255` OR `eof_w9332`)) (the slave's second output, the copy of `lc2_w8692`); the slave's first output is `lc2_w8475`, the clock of `lc2`'s first flip-flop **Followed on by `eofw`** (`notes/blocks/eofw.md`, `trace/eofw.txt`, 2026-11-19): `eof_w7818` is `tc2_r5589`, `eof_w7718` is `tc2_sr_g` (and `lc1_w7908`: one net), `eof_w7777` is `lc2_w8474` (= `lc1_w7170` by `lc2`'s alias); gathered by `@alias` until the next refresh renames them |
| `tl6_p#` | a net of the sixth strip of the top-left logic, a track field without a gate (`notes/blocks/tl6.md`), named by the x of its vertical poly in the crossing field (x 6040-6420, y 4390-4890). `tl6_p6101`: a poly from the north edge (x 6062, turning east under the wide metal band), the track x 6059 (y 2595-4395), the field's poly x 6101, a metal south and through the nest to a pad (6275,6152), a poly south across y 6350 at x 6282. `tl6_p6143`: a poly from the east edge along y 2530, the track x 6103, the field's poly x 6143, a metal to a pad (6318,6110), a poly south at x 6322. `tl6_p6187`: a metal from the east edge along y 2573, the track x 6146, the field's poly x 6187, a metal to a pad (6360,6152), a poly south at x 6365. None has a driver or a gate in the strip; neither end is followed |
| `tl3_w#` | a wire of the third strip of the top-left logic, the middle cluster's west column (`notes/blocks/tl3.md`), by the y of its row or contact. The latch at y 3212-3652 (copies of `tl1_ua`, `tl1_ub`): `tl3_w3233` = NOT `tl3_w3333`; `tl3_w3419` = NOT(`tl3_w3333` AND `tl3_w3373` OR `tl3_w3550`); `tl3_w3550` = NOT(`rcs_x1` OR `tl3_w3373` AND `tl3_w3233` OR `tl3_w3419`): open while `tl3_w3373` is high, data `tl3_w3333`, cleared by `rcs_x1`; `tl3_w3419` (the inverted output) leaves west. NOR units below it: `rcs_a2` = NOR(`tl3_w3722`, `tl3_w3803`), `tl3_w3939` = NOR(`tl3_w3896`, `tl3_w3982`), `tl3_w4720` = NOR(`tl3_w3803`, `tl3_w4763`) (its output goes to the data row of the unit below). `tl3_w3803` is made by a cross-coupled pair at y 4046-4330: `tl3_w3803` = NOR(`tl3_w4112`, `tl3_w4243`) (the second input across a `?` join), `tl3_w4243` = NOR(`rcs_x1`, `tl3_w4290`, `tl3_w3803`); below it an inverter `tl3_w4373` = NOT `tl3_w4414` and `tl3_w4546` = NOR(`tl3_w4503`, `tl3_w3803`). Latch B at y 4818-5258 is latch A again with data `tl3_w4720`, enable `tl3_w4978`, clear `rcs_x1`, outputs `tl3_w5156` and `tl3_w5025` (inverted, leaves west), inner nets `tl3_w4839`, `tl3_w4974`. `tl3_w3368` is the thin metal x 3783 inside the latch, aliased to `tl3_w3419` across a `?` tie. None identified Run 11 (`notes/blocks/tl3.md`, south of the foot): **`tl3_w4763` is `tc1_o3527`** (its metal ends on a pad (3565,5720) whose row runs east into `tl4`'s row of `tc1_o3527`; an alias), so `tl3_w4720` = NOR(`tl3_w3803`, `tc1_o3527`) and `tl3_w4373` = NOT `tc1_o3527`; **`tl3_w3982` is `tl5_w5936`** (pad (3607,5938), a row, pad (3954,5938), a thin metal east into `tl4`'s metal y 5939; an alias), a bus line that leaves `tl5`'s strip south: its driver is south of y 6350 |
| `tla_w#` | a line of the west column of the first cluster (under rail R1, x 2558-2693), by the y at which its poly crosses the rail. `tla_w3417` = NOT(`rcs_thin_e` AND `tla_w3376` OR `tla_w3505` AND `amr_eq_r3`): the output of a two-way selector (inverting), leaving by the metal x 2326, the poly y 5543 east along the cluster's foot to (4408,5545), track V of the second bus field north to (4410,4460) and a poly east along y 4461 to gate 1 of `tl4_w4545` in the right cluster. `tla_w3505` = NOT `rcs_thin_e`. `tla_w3376`: input, from the small cluster below (metal x 2199, poly y 5500, metal x 2870 south from (2870,5502)). `amr_eq_r3`: input, from the metal x 2239 whose south end (2239,5632) is on a poly that leaves east along y 5632; believed to be the vertical sync width match `amr_eq_r3` (an unmerged branch follows that line from `amr`; not joined here) |
| `rc0_n` | NOT `rc0`: output of the inverter I2 west of the counters, whose input was traced to the row counter's bit 0 on 2026-11-16 (its two nets had place names until then: see Former names). One input of the XOR that makes `ras_o0_alt1` |
| `wl_h#` | horizontal poly bands H0 and H1 above the counters; not identified |

## Registers, comparators and their results

| Name | What it is |
|---|---|
| `rsel#` | select line of register # from the address decode (high when the address register holds #) |
| `rsel#_n` | NOT `rsel#` |
| `rsel#_bn`, `rsel#_buf`, `rsel#_bufn` | buffer of a select line: first inverter and output (`rsel12_bufn` is the first inverter of R12's separately built buffer) |
| `wr_stb_n` | common write strobe, active low |
| `wr_r#` | write strobe of register #: `rsel#` AND NOT `wr_stb_n` |
| `wr_r#_u` | the load strobe line at the register's latch row, where its join to `wr_r#` is not drawn |
| `r#_b#_a`, `r#_b#_n2`, `r#_b#_q` | register R#, bit #: storage node (loaded from the bus while the strobe is high), its inverse, and the output (= the stored bit) |
| `r#_b#_m#` | the metal straps of a register bit cell (in `cdp1`'s rows: `_m3`, `_m6`; `_m6` is also the output `_q` in row C) |
| `r#c_b#_nor`, `r#c_b#_x` | comparator of R#, bit #: NOR(counter bit, register bit), and x = counter bit XOR register bit |
| `r#hc_s#_nor`, `r#hc_s#_x` | comparator of the horizontal counter against R0 shifted one place (R0/2), by slice |
| `sl_eq_r#` | high when the scan line counter equals R5 (vertical total adjust). Leaves the comparator northwards; not followed |
| `amr_eq_r#` | high when the 4-bit counter `c4l0`..`c4l3` (on the lines `c4l0`..`cdp1_l4676`) equals R3 bits 4-7: the wired NOR of `r3c_b4_x` ... `r3c_b7_x` on a diffusion line y 6246-6272 through `amr`'s four slices, load in the first column. It leaves through a buried contact at c0 and runs west to a gate in `tla`'s first cluster (`notes/blocks/amr.md`). Named for the block until its use is traced |
| `hsw_eq_r#` | high when the horizontal sync width counter equals R3's nibble (the end of HSYNC). Not followed |
| `h_eq_r#` | high when the horizontal counter equals R# (R0: end of line; R1: displayed width; R2: sync position) |
| `h_eq_r#half` | high when the horizontal counter equals R0/2 |
| `h_eq_r#_u` | a piece believed to be `h_eq_r#` whose join is not drawn (tracks k7, k8 of the strobe channel) |
| `rc_eq_r#` | high when the row counter `rc` (its seven lines through the upper right array, joined by `ucz`) equals R4 (vertical total), R6 (vertical displayed) or R7 (vertical sync position). `rc_eq_r6` goes down the wiring channel to the strobe channel (its track k4); `rc_eq_r7` leaves west along y 6820. `rc_eq_r4` is drawn end to end (`notes/blocks/eof.md`): down bundle tracks L2, L7, L6, L5, L9 to the strobe channel's track k15, where it is the data input of the latch gated by `inh_lat` and the input of inverter A (`rc_eq_r4` are aliases of it in `trace/eof.txt`) |
| `hc#_u` | the horizontal counter line at the comparators, where its join to `hc#` is not drawn |
| `db_b#` | **the internal data bus, bit #** (0-7). One net per bit across the chip: the right datapath's data lines (formerly `ubus_b#` in the upper array and `rbus_b#` in the lower one), the central datapath's bit lines (`notes/blocks/bust.md`), R3's data lines, `amr`'s inner lines. It writes R0-R11 by the register widths of the datasheet (`tools/bust_fanout.py`). The bit numbers rest on the counters' carry direction (the comparators) and on that fan-out; bits 0 and 1 also end in the D0 and D1 units of `dbus` (`notes/blocks/dbl.md`). Bits 0-3 are driven onto the bus by the input latches of pins D0-D3 in the data bus column (`dbus`: `db_b#` = NOT `dl#_q_n`), bits 4-7 the same way by the latches and inverters of `dlat` (`notes/blocks/dlat.md`). Bits 0-4 continue to R10 and R11 only through `?M` (AMB-019): the names `cdp2_a_s#_bus`, `cdp2_c_s#_bus` stay aliases there |
| `ar#`, `ar#_n` | address register bit # and its inverse (rows of the decode array) |
| `ar#_a`, `ar#_n2`, `ar#_q`, `ar#_trk` | nodes of address register bit #: storage node, its inverse, output, and the track that takes it to the decode |
| `ar_load`, `ar_load_n` | load strobe of the address register and its inverse |

## Bus control

| Name | What it is |
|---|---|
| `wr_data_sel` | NOR(`rw_d`, `bd2_rs_n`, `cs_d`): a write to the data register is addressed |
| `wr_data_sel_n` | NOT `wr_data_sel` |
| `wr_data_lat`, `wr_data_lat_n` | transparent latch of `wr_data_sel`, open while `e_b` is high |
| `wr_data_e_n` | NOT(`wr_data_sel` AND `e_b`) |
| `wr_addr_sel` | NOR(`rw_d`, `rs_d`, `cs_d`): a write to the address register is addressed |
| `bd2_rs_n` | believed NOT `rs_d` (its gate is not fully traced) |
| `bd2_x` | second term of the address register load, from the untraced right-hand column |

## Strobe channel gate column (`notes/blocks/bd1.md`)

| Name | What it is |
|---|---|
| `bd1_k#` | tracks of the channel not yet identified (`rc_eq_r6`, `hc1`) |
| `rc_eq_r4`, `bd1_an` | input and output of inverter A. `rc_eq_r4` is `rc_eq_r4`, R4's match (joined by `eof`; an alias until it is renamed), so `bd1_an` = NOT `rc_eq_r4` |
| `bd1_n#`, `bd1_q`, `bd1_k` | nodes of the latch on R4's match gated by `inh_lat`: `bd1_n1` the upper half's node (NOT the match while open), `bd1_n2` the lower half's (the match as latched); `bd1_q`, the poly of the upper half's gate G4 and of the lower half's load, is `bd1_n2` (`eof`'s piece `r4lat`: an alias, through the load's uncertain tie); `bd1_k`, the wire that leaves the latch west, is `bd1_n2` too (`eof`'s piece `n2out`, 2026-11-19: an alias on firm geometry; the strip under `inh_src`'s gate is a third pull-down of N2, so `bd1_n2` = NOT((`bd1_an` AND `inh_lat`) OR `bd1_n1` OR `inh_src`)): the latch's output, followed by piece `n2w` to (6711,15000) in the left bus field |

## Central datapath (`notes/blocks/cdp1.md` ... `cdp4.md`)

None of these rows has a register number yet, so all names are by place. Columns are
`c#`, slices `s#`, counted from the left.

| Name | What it is |
|---|---|
| `r8_b#_*`, `r9_b#_*` | R8 (cdp1 row A) and R9 (cdp1 row C), static register bit cell `cdp1_reg`: `_a` storage node (the bit line while the write line is high), `_n2` its inverse, `_q` output, `_m#` metal straps. Bit order from the data bus (`notes/blocks/bust.md`): R8 slices 5, 4, 1, 0, 3, 2 = bits 0, 1, 4, 5, 6, 7; R9 slice k = bit 5 - k. Renamed from `cdp1_a#_*`, `cdp1_c#_*` (former names) |
| `wr_r8`, `wr_r9` | the write strobes of R8 and R9, which are the write lines of rows A and C: **row A is R8, row C is R9** (`notes/blocks/wrs.md`) |
| `cdp1_b5_a` | the register-side input of R9's comparator in slice 5 (bit 0): not the register bit but the output of the island `tc1` |
| `ra#_cmp` | the row-address-side input of R9's comparator for bit # (# = 0-4): output of a unit near the right edge whose pull-down is gated by `ra#_drv_in`; with the unit's load (traced in `trace/dbus.txt`, cell `dbus_r9l`), NOT `ra#_drv_in`, the level of pin RA# (AMB-012, resolved but for `r9c`'s `?B` ties; `notes/blocks/r9c.md`). The comparator cell's own name for the same net, `cdp1_b#_b` with # = 5 minus the bit, is kept as an alias |
| `ra#_drv_in_u` | (# = 4) the input of r9c's RA4 unit, aliased to `ra4_drv_in` (`trace/rad.txt`) through r9c's `?P`. RA2's and RA3's were renamed when the joins through `ral` came out firm |
| `ral_stb` | the strobe of the `ral` cells' input pass transistors (metal y 4548 under the band). Followed back and drawn (`trace/ral.txt`): north along x 13862, west along y 4245 (the sixth line of rab's bundle), a cross-under at x 11150-11650, north along x 11068, west along y 2768 with three poly hops, to x 8350, where it is `tc1`'s nested bus metal ns4 (old name under former names). That metal goes south past y 4450 to its end pad (8204,5672) (`trace/tc2.txt`, piece 9), with one contact on the way, (8204,5371), onto a poly that runs east past x 8250 (seen to x 8425, not drawn). From the end pad the line goes on: a poly row west along y 5673, the pad (7748,5673), a metal south, the pad (7750,6065), a poly to the pad (7488,6282), and a metal west along y 6328 past x 6400 (follower: to (6012,6068)). Source: not found yet (west of x 6400) |
| `ral_a_s#` | `ral` cell s# (s0-s4 west to east; s0 is RA bit 0's cell), node a: the input pass transistor's far side (strobe `ral_stb`), the diffusion strip y 4479-4494 to the hold device (gate VSS), which joins it to the cell's output (`ra#_drv_in`; `ra4_drv_in_u` for 4), and the gate of one pull-down of the cell's NOR (a diffusion wire under the VSS rail, a buried contact, the poly bar y 4322-4344) |
| `ral_a_m#` | the same node in the fourteen copies of the `ral` cell in front of the MA pad drivers (`trace/mal.txt`, tags m0-m13 top to bottom; **copy m# drives MA#**: each output followed to its pad driver) |
| `mal_frc_m#` | the gate tab of the force pull-down in MA copy m# (`ral_n1_m#` = NOR(`ral_a_m#`, `mal_frc_m#`)): drawn as a pad of its own per copy; a thin vertical metal at x about 2700 runs past the pads and probably joins them all (seen, not drawn: `notes/blocks/mal.md`) |
| `ral_n1_s#`, `ral_n1_m#` | the output of the NOR of `ral` cell s# / MA copy m# (NOR of node a and `cnt_gab` / `mal_frc_m#`): its diffusion (north of the bar, the drain of the `cnt_gab` pull-down, the band above that line's pad) and, through a buried contact, the Z-shaped gate poly of the output inverter; the cell's output = NOT this |
| `cdp1_b#_n2`, `cdp1_b#_ne` | NOR(a, b) and a XOR b |
| `ra_eq_r9` | R9's match: NOR of the five `_ne` of the comparator in `cdp1` row B, high when R9 equals the 5-bit value on the `_b` lines, which are the row address as it goes to the RA pins (`ra#_cmp`; marked, AMB-012). In slice 5 the register bit is replaced by `cdp1_b5_a`, made by `tc1`. It runs to the row counter's step logic, where it is the input of the inverter that makes `rcs_mu` (contact (4148,3335); AMB-013, resolved; `notes/blocks/r9m.md`) |
| `cdp1_l#`, `cdp1_lw#` | horizontal lines of the data bus channel, named by their y; and two write-line links. East of the block they cross under the supply metal and go on east as the bus to the right datapath (`notes/blocks/bust.md`): `c4l0`, `c4l1`, `cdp1_l4632`, `cdp1_l4676` are the four inputs of `amr`'s comparator (the 4-bit counter `c4l0`..`c4l3`, compared with R3's high nibble; the last two keep their positional names until `bust`'s two `?P` rows are firm); `sl_eq_r5` is R5's match (`sl_eq_r5`, alias); `db_b6` is `amr` c2's inner line, an input there (the data written into the slice's latch); `cdp1_lw1` comes from the west: its west end is the pad (8353,4981), joined by a metal, a poly row and a thin metal to row B of the latch `tc2_sr` (its line `tc2_sr_r`, an alias; `notes/blocks/tc2.md`, piece 7) |
| `cdp2_a_s#_*` | cdp2 row A (5-bit latch), slice #: `_a` storage node, `_n2` inverse, `_q` output, `_bus` bit line |
| `cdp2_a_c_s#_*` | cdp2 row C (7-bit latch), the same nodes |
| `wr_r11`, `wr_r10` | the write strobes of R11 and R10, which are the load strobes of rows A and C: **row A is R11, row C is R10** (`notes/blocks/wrs.md`) |
| `cdp2_a_s#`, `cdp2_c_s#`, `cdp2_c_s#_bus` | per-slice lines and bit lines of those rows |
| `cdp2_b_s#`, `cdp2_b_s#_*` | cdp2 row B comparator with a ripple chain, slice #: `_y` = NOR(q, t), `_ne` = q XOR t, `_x` chain output of the slice, `_o2` inverse of the previous slice's chain output, `_p1` internal node |
| `cdp2_b_cin`, `cdp2_b_hl` | chain input of that comparator; and a row-long line pulled low per bit |
| `cdp2_trk_s#` | the value that row B compares row C against, per slice (through track). s7, s6, s5, s4 are aliases of `rax_o0`, `rax_o1`, `rax_o2`, `rax_o3`; `rax_o4`'s line (y 5826) has no through track tied to it as traced (slice s3 is wired differently) |
| `cdp2_ch#_#` | a line of channel 1, named by its y |
| `cdp3_c_c#_*`, `cdp3_h_c#_*` | cdp3 rows C (6 bit) and H (8 bit), static register bit in column #: `_x`, `_q1`, `_q` as in cdp1 |
| `cdp3_c_wr`, `cdp3_h_wr` | write lines of rows C and H |
| `cdp3_cw_c#`, `cdp3_hw_c#` | west outputs of those bits |
| `cdp3_cq_c#`, `cdp3_hq_c#` | read outputs of those bits, to the pass transistors onto bus N |
| `cdp3_n_c#` | bus N, column # |
| `cdp3_gate_e`, `cdp3_gate_f` | gates of the read pass transistors of rows E (row C onto bus N) and F (row H onto bus N) |
| `cdp3_bl_c#`, `cdp3_f_c#`, `cdp3_g_c#` | column lines e (bit line), f and g |
| `cdp3_k_a`, `cdp3_k_b`, `cdp3_k_c` | lines of the NAND beside row C |
| `cdp3_l#` | a line of channel B, named by its y |
| `cdp4_lc_s#_*`, `cdp4_lr_s#_*`, `cdp4_ldr_s#_*` | cdp4 latch rows C (8 bit), R1-lower (8 bit, upside down) and D (6 bit), slice #: `_a` storage node, `_n2` inverse, `_q` output, `_x2` internal strap |
| `cdp4_ld`, `cdp4_ld#b`, `cdp4_ld#` | load strobes of those rows (C, R1-lower, D) |
| `cdp4_in_s#`, `cdp4_in#b_s#`, `cdp4_in#_s#` | data inputs of those rows |
| `cdp4_n_s#` | output node of the 4-way selector, slice # |
| `cdp4_a_s#`, `cdp4_b_s#`, `cdp4_c_s#`, `cdp4_d_s#` | the selector's four sources per slice |
| `cdp4_sel#` | the four select lines of the selector |
| `cdp4_rst` | gate of the pull-down on the selector node |
| `cdp4_bus_s#` | the eight poly lines of channel 1; each is one net with `cdp4_in_s#` (the row C latch input of the same slice) and with one poly row of the left array, joined in the left bus field (`busl`, piece `ch1`; `@alias` in `trace/busl.txt` until the rename) |

## Left array (`notes/blocks/larr.md`): the 14-bit memory address counter

Row tags `s0` ... `s13` are rows from the top; which MA bit each is has not been fixed.

| Name | What it is |
|---|---|
| `larr_n#_s#` | inverters of the row: `_n2` = the stored bit Q, `_n3` = NOT(carry-in XOR Q), `_n4`, `_n5` = the value sampled into the latch part |
| `larr_g#_s#` | storage node of the bit (`g6`) |
| `larr_x#_s#` | `_x1` dynamic node that takes the incremented or the loaded value; `_x2` = NOT `larr_ld` |
| `larr_ld_s#` | value offered for loading, from the right |
| `larr_y_s#`, `larr_z_s#` | new value leaving to the right; value written back to the bit |
| `larr_a_s#`, `larr_mid_s#` | internal nodes of the incrementer |
| `larr_cin_s#`, `larr_cout_s#` | carry in and out of a row |
| `larr_h_s#` | line H along a row boundary |
| `larr_l#_g#`, `larr_l#nc_s#` | group carry lines and their pieces |
| `larr_vm#` | vertical control lines Vm1-Vm6 of the latch part (clear, count, load, tied off, transfer, write) |

## Top-centre island and bottom-centre block

| Name | What it is |
|---|---|
| `tc1_l4_out`, `tc1_r#_out` | the island's remaining internal outputs: `tc1_r1_out` = NOT R9 bit 0; `tc1_r2_out` = NOR(R9 bit 0, `ras_shift`); `tc1_r5_out` = NOT((`tc1_i` AND `ras_o0_sel1`) OR (`tc1_g` AND `ras_o0_sel2`)), `tc1_r4_out` its inverse; `tc1_l4_out` = NOR(`ras_o0_sel2`, `tc1_w1`), leaves west |
| `tc1_g`, `tc1_i`, `tc1_w#`, `tc1_x#` | the island's other inputs and channel lines. `tc1_g` and `tc1_i` are used where the selector uses `ras_o0_alt2` and `ras_o0_alt1`; each is the output of a small inverter west of the selector (`notes/blocks/fld.md`), and they are **not** shown to be the selector's two nets |
| `tc1_x1` | NOT `ras_o0_sel1` (an inverter below R8's row, `notes/blocks/shm.md`); runs west past the island and into the logic west of the selector (`notes/blocks/fld.md`), from the contact (7055,4478) by poly and metal to a gate of the NOR `tc2_o5175` at (6500,5132) (`notes/blocks/tc2.md`). Its channel metal x 7053 also runs north: the ring gate of the driver `tc1_o4020`. A small inverter there, `tc1_o4280` = NOT `tc1_p4308`, may be on this line too; that join is not drawn (`notes/blocks/tc1.md`, Ambiguity 17; AMB-020; open join `tc1_x1_u`). The channel metal x 7053 runs north past the driver (contact (7054,4092)) to (7054,3134), with a tap at about (7055,3730) not looked at. The poly row y 4383-4401 that `tc1` labelled `tc1_x1_u` is the output of `tcw`'s last inverter, NOT `tcw_m6362c` (`notes/blocks/tcw.md`, run 2): if `tc1`'s assumed joins hold, `tc1_x1` has two drivers |
| `fld_a_in`, `fld_b_in` | gates of the two inverters whose outputs are `tc1_g` and `tc1_i` (`notes/blocks/fld.md`). `fld_a_in` = NOT((`inh_ck` AND `tcw_b`) OR `tcw_o3820`): pull-downs in the gate group west of the island, load and third pull-down east of the ground rail (`notes/blocks/tcw.md`, run 2); it is also the third gate input of `tcw_o3820` (supply assignment of the rails: AMB-014). `fld_b_in` = `cnt_la_a_n` XOR `tc1_g` (output of the first XOR cell) |
| `fld_y_b` | the metal input of the second XOR cell west of the selector: `ras_o0_alt1` = `rc0_n` XOR `fld_y_b`. Pulled low through `tcw_c` in the gate group west of the island (`fld_y_b` = NOT `tcw_c`; load traced in `tcw` run 2; AMB-014) |
| `tcw_b`, `tcw_c` | with `inh_ck`, the three gate inputs of the group at x 6380-6700, y 3880-4220 (top-centre west), named by place: pads (6400,4005), (6455,4045), (6318,4135), each with a thin metal from the north. `inh_ck` and `tcw_c` are also gates of the AND-OR-invert above the group (pads (6400,3788), (6318,3740)). Sources of `tcw_b` and `tcw_c` not traced. The first input is `inh_ck` (renamed 2026-11-19, see Former names) (`notes/blocks/eof.md`, run 2): its metal x 6105 runs south from `tl6`'s strip to `trunks`' line S, the output of the lone inverter of the input buffer row; a contact (6427,7648) on the way taps it onto a poly row east to a gate group at (7540-7670, 7600-7750), not traced |
| `tcw_o#` | output node of a pull-down stack of the gate column west of the island, named by its y under the ground rail (`notes/blocks/tcw.md`). `tcw_o3820` = NOT(`fld_a_in` OR (`inh_ck` AND `tcw_c`)), leaving on a pad (6648,3785) and a thin metal to a pad (6646,3986), whose poly gates a third pull-down of `fld_a_in`: the two are a cross-coupled pair, a latch gated by `inh_ck`. `tcw_o3550` = NOT `c4l_gab` (an inverter; alias of `tcw_m6362b`, the bus metal it leaves on, AMB-015). `tcw_o3326` (alias `tcw_o3437`: two stacks joined on their east side, AMB-015): low through `tcw_m6362a`, `tcw_m6404`, or `tcw_o3550` AND `tcw_m6320`; its load and destination not traced. `tcw_o2823` is an alias of `tcw_m6362a` (low through `tcw_m6404` AND `tcw_m6320`); `tcw_o2993` low through `tcw_m6404` AND `tcw_m6278`, gate of the next pair; `tcw_o3115`, `tcw_o3180` the middle and bottom nodes of that pair (which is its output is open) `tcw_o3240` = NOT(`tcw_m6320` AND `tcw_o3550` AND (`tcw_m6362a` OR `tcw_m6404`)) (run 3): the top node of the stack at y 3232-3410, with its load; `tcw_o3326` and `tcw_o3437` are one node inside that gate, not an output |
| `tcw_m#`, `tcw_m6362a`, `tcw_m6362b`, `tcw_m6362c` | a thin vertical metal of the bus west of the gate column, named by its x (and a letter where one x holds two nets). `tcw_m6404`: pads at y 2745, 2915, 3135, 3393: gates four pull-downs (a common enable or clock); comes from the south: its metal ends on a pad (6275,4405) at the top of a vertical poly under the six bus metals, not followed further. `tcw_m6320`: pads at y 2787, 3263, 3655. `c4l_gab`: pads at y 2875 (a poly to the rail) and 3526. `tcw_m6278`: pads at y 2958 and 3178; runs on north and south. `tcw_m6362a`: from the pad (6355,2830) to (6378,3355); the output of the top pair of the column (AMB-016). `tcw_m6362b`: y 3437-3570; the output of the inverter `tcw_o3550` (AMB-015). `tcw_m6362c`: pads (6362,3832) and (6362,4266); gate of the column's last pull-down |
| `cdp1_fx_n2`, `cdp1_fy_n2`, `cdp1_fx_b`, `cdp1_fy_b` | names that the comparator cell's template gives the two copies west of the selector: `_n2` the cell's internal NOR of its inputs; `cdp1_fx_b` is an alias of `tc1_g`, `cdp1_fy_b` of `fld_y_b` |
| `tc1_ns#` | north-south lines ns1-ns6 east of the island. `tc1_ns2` (x 8132-8148, from a poly out of the logic at the datapath's slice-0 position) runs north to the bus line y 2727, west through the top bus field in poly to a pad (6773,2790), and south on the thin metal x 6765-6785 (`tc1_p3698`, aliased to it) to gate 1 of the second driver `tc1_o3740`. `tc1_ns3` south of the island (`trace/tc2.txt`, piece 11): the thin metal x 7902 over `rax`'s five units without a contact to the pad (7899,5633), a poly row west along y 5632, a poly south along x 7605, the pad (7660,6193), a metal x 7661 south past y 6400 (not followed) |
| `tc1_bus#` | a through line of the top bus field north of the island that has no other name yet, named by the y of its metal track (`notes/blocks/tc1.md`, "The bus fan and the top bus field"). `tc1_bus2554` and `tc1_bus2684`: a poly from the north (x 7201-7218, x 7160-7176 at y 2500) to a metal track going east over the datapath. `tc1_bus2814`: a poly from the north (x 7117-7133) to the track y 2814 and on east as a poly (x 8350, y 2890-2907). `tc1_bus2858`: a poly row from the west (x 6750, y 2520-2540) to the track y 2858 and on east as a poly (x 8350, y 2933-2950). The two tracks below them are `r8_b4_q` (y 2899) and `r8_b5_q` (y 2943) |
| `tc1_o#` | output node of a gate in the columns west of the island's channel, named by its y (`notes/blocks/tc1.md`). `tc1_o4020` = NOR(`tc1_g`, `tc1_x1`): a wide driver at x 6800-6990, y 3925-4222 with a strong load; leaves on the channel metal x 7133-7152, a poly through the top bus field and the bus metal y 2641 going east over the datapath (drawn to x 8350; the follower gives its end at (9098,2639)). `tc1_o3740` = NOR(`tc1_ns2`, `tc1_x1`) (gate 1 arrives on the thin metal `tc1_p3698`, gate 2 on the thin metal `tc1_x1_u`): the second driver, north of the first (x 6690-7035, y 3600-3900); leaves on a metal that runs north, west along y 3653-3665 and north again at x 6941-6956 to a contact (6948,2977) and, across an uncertain metal (`notes/blocks/tc1.md`, Ambiguity 20, join J6), on into `tc1_m7056` (aliased to it) and east on the bus line y 2598. `tc1_o2950` = NOT `tc1_m6817`: cell D, a pull-down under the rail with a load of its own north of cell C (x 6690-6990, y 2800-2990); its output band ends in the box (6936-6974, 2944-2972), drawn as an uncertain buried contact onto `tc1_p3051` (aliased to it; join J4), which makes it gate row 1 of cell C. That the contact (6948,2977) of `tc1_o3740`'s thin metal is on the same band (J5) is not drawn. `tc1_o4280` = NOT `tc1_p4308`: the output node of a small inverter south of that driver (a strip under the rail, x 6803-6934, y 4270-4293). It runs up to `tc1_x1`'s pad (6962,4268); the join is not drawn (`notes/blocks/tc1.md`, Ambiguity 17), so it has no destination in the trace. `tc1_o3527` = NOR(`tc1_o3353`, `tc1_o3095`): cell B, the NOR north of the second driver (x 6690-7160, y 3405-3625); its poly runs south under the channel metal x 7048-7068 to the contact (7011,3852), and the channel metal x 7003-7023 takes it south out of the package at y 4450. `tc1_o3353` = NOR(`tc1_m7100`, `tc1_l4_out`): cell A, the next NOR north (x 6690-7160, y 3240-3420); its output is a C-shaped poly (y 3345-3362 / x 7137-7154 / y 3472-3492) that is cell B's gate row 1. `tc1_o3095` (formerly named as the channel metal x 7003-7023) = NOR(`tc1_p3051`, `tc1_x1`, `tc1_m7100`), with `tc1_p3051` = `tc1_o2950` if join J4 holds: cell C, the three-input NOR north of cell A (x 6690-7080, y 2940-3240); it leaves by the contact (7010,3093) on the channel metal x 7003-7023, which ends on cell B's gate row 2 |
| `tc1_m#` | a thin vertical metal of the gate columns west of the island's channel, named by its x. `tc1_m6817` passes over the driver `tc1_o4020`; no contact is drawn there (`notes/blocks/tc1.md`, Ambiguity 12), nor over cell B's buried contact (Ambiguity 18); its north end is a contact (6815,2833) on a pad whose C-shaped poly is the gate of cell D's pull-down (`tc1_o2950`); from its foot (6797,4372) it runs south to a pad (6796,4829), west on a poly row to a pad (6492,4828), by metal west, south along x 6364 and in three steps to a pad (6533,6152), and from there on a poly going south past y 6400 (`notes/blocks/tc2.md`): it is driven from the south, not followed further. `tc1_m7056`: the L-shaped metal y 2933-2948 / x 7049-7063 from the box of Ambiguity 20 to the contact (7054,2812), with the poly from there to the contact (7425,2596) and the bus metal y 2598 going east over the datapath (drawn to x 8350; the follower ends it at (9056,2595)); aliased to `tc1_o3740` across an uncertain metal. `tc1_m7100`: the upper piece of the channel metal x 7091-7110, ending south on the contact (7100,3180), whose poly is gate row 1 of cell A (`tc1_o3353`) and a gate of the next cell north; the metal goes north to y 2769, west along y 2762-2776 and north to a contact (6946,2680) on a pad of the poly row y 2652-2666, which comes from the west under the rail x 6858-6906 (its driver is west of x 6750) |
| `tc1_p#` | a poly of the gate columns west of the island's channel, named by its y. `tc1_p3698`: gate 1 of the second driver `tc1_o3740`; its vertical poly under the supply rail's east edge (x 6725-6740) ends at a pad with the contact (6772,3591), from which the thin metal x 6765-6785 goes north to a contact (6773,2790) on the west end of `tc1_ns2`'s poly: the two names are aliased. `tc1_p3051`: gate row 1 of cell C (`tc1_o3095`); its poly runs north to a box (6936-6974, 2944-2970) at the east end of a diffusion band, beside a contact (6948,2977) of `tc1_o3740`'s thin metal; the band is cell D's output, and the box is drawn as an uncertain buried contact, the name aliased to `tc1_o2950` (`notes/blocks/tc1.md`, Ambiguity 20). `tc1_p4308`: the input of the inverter `tc1_o4280` (gate of its pull-down under the rail x 6858-6908); its poly runs south and then west along y 4428-4448 (drawn to x 6750) to a pad with a contact at (6620,4436), whose metal goes south along x 6621 into the logic west of the selector (seen, not drawn) (`notes/blocks/tc1.md`, Ambiguity 17) |
| `tc1_x1_u` | the thin metal x 6968 over the same driver: an open join of `tc1_x1` (aliased in `trace/tc1.txt`): it has a contact on the pad (6962,4268) at the end of a branch of `tc1_x1`'s ring poly, and the branch meets the pad across a gap drawn `?P`. Its south end is a contact (6947,4396) on a pad whose poly runs west along y 4385-4405 (drawn to x 6750; seen to about x 6445). Its north end turns east into the contact (7009,3789) on gate 2 of the second driver `tc1_o3740` |
| `tc2_o#` | output node of a gate in the top-centre logic's lower half, named by its y (`notes/blocks/tc2.md`). `tc2_o5175` = NOR(`tc1_x1`, `fld_b_in`): two pull-downs west of the ground rail x 6537-6583 at y 5132 and 5219, load east of it; leaves west on a poly along y 5173 past x 6400, not followed |
| `tc2_sr_q`, `tc2_sr_q_n` | the two nodes of a latch of two cross-coupled gates at x 7977-8198, y 5990-6300 (`notes/blocks/tc2.md`, piece 4): `tc2_sr_q` = NOR(`tc2_sr_q_n`, `tc2_sr_c`, `tc2_sr_g` AND `tc2_sr_r`), `tc2_sr_q_n` = NOR(`tc2_sr_q`, `tc2_sr_g` AND `tc2_sr_s`); both depend on one `?` poly. `tc2_sr_q` leaves south on a metal x 7922 (past y 6400) and east on a poly y 6163-6180 (past x 8250); `tc2_sr_q_n` stays in the latch. Not identified |
| `tc2_sr_g` | the latch's common gate line: the gates in series with `tc2_sr_r` and with `tc2_sr_s`. Metal x 7837 south past y 6400, followed by `eofw` (2026-11-19): to a pad (7836,7215), west by a poly row to row 2 of the gate on `inh_ck`'s tap row (`eof`'s `g7700`; `eof_w7718`), and from that row's pad by a metal staircase to `lc2`'s `lc1_w7908`, the enable of latch D: one net (aliases in `trace/eofw.txt`). A corner pad (7446,8732) leads on into `cdp3`'s gate column. Driver not found |
| `tc2_sr_r` | an alias of `cdp1_lw1` (`trace/tc2.txt`, piece 7): the latch's line that, with `tc2_sr_g` high, pulls `tc2_sr_q` low. From row B's pad by a metal x 7836 north, the pad (7836,5520), a poly east, the pad (8031,5520), a thin metal x 8031 north over `rax`'s units 2-4 without a contact, the pad (8031,5066), a poly row east along y 5066, the pad (8291,5066) and a metal to the pad (8353,4981), the west end of `cdp1_lw1` |
| `tc2_sr_s` | with `tc2_sr_g` high, pulls `tc2_sr_q_n` low. Metal x 7791 going south past y 6400 (not followed) |
| `tc2_sr_c` | pulls `tc2_sr_q` low by itself. It is the top line of `cdp2`'s channel 2 (poly y 6367, from the pad (7490,6367) east past x 8250), with a metal from that pad west along y 6370 past x 6400 (not followed either way) |
| `tc2_m#` | a metal of the nest west of the XOR cells (x 6400-6580, y 5350-6170), named by the x of its pad (`notes/blocks/tc2.md`, piece 5). `tc2_m6490`: from the west along y 5567 to the pad (6490,6108), poly south past y 6400. `tc2_m6447`: from the west along y 5611 to the pad (6447,6150), poly south past y 6400. Neither end is followed. `tc2_m6404` (piece 14): from the west along y 6026 (it comes down x 6362 west of x 6400) to the pad (6404,6107), poly south past y 6400 under the ground metal y 6198-6243 without a contact. Neither end is followed |
| `tc2_r#` | a line through the top-centre logic's lower half, named by the y of its poly row (`notes/blocks/tc2.md`, piece 10). `tc2_r5718`: a poly row y 5718 from past x 8250 west to the pad (7791,5718), a metal south to the pad (7791,6152), a poly to the pad (7530,6324), a metal south past y 6400. Not identified, neither end followed. `tc2_r5589` (piece 12): from the pad (8248,5262) (its poly goes on east to a pad (8490,5262)) a metal south to the pad (8246,5589), the poly row y 5589 west to the pad (7488,5586), a metal south and west to the pad (7422,6065), a poly to the pad (7384,6282), a metal west along y 6283 to the pad (6840,6282), a poly south past y 6400, which `eofw` follows (2026-11-19) to the output of the gate on `inh_ck`'s tap row: **`tc2_r5589` = NOT(`lc1_w7170` AND (`inh_ck` OR `tc2_sr_g`))** (`eof`'s `g7700`; its name there `eof_w7818`). The east end (loads) not followed |
| `bc1_s#`, `bc1_s#_n` | the two bus lines the 2-bit decoder decodes, and their inverses |
| `bc1_dec#_n` | decoder outputs, active low (00, 10, 01) |
| `bc1_ld_in#`, `bc1_ld_n`, `bc1_ld_a` | inputs, NAND output and twin output of the driver of cdp4's row D strobe |
| `bc1_d#` | data lines 3-6 into cdp4's row D |
| `bc3_w#` | a wire of the bottom-centre logic package bc3 (`notes/blocks/bc3.md`), by the y of its row (or the x of its rail). `bc3_w17605` = NOT `bc3_w17646` (inverter at x 7475-7775, y 17575-17705, a copy of `tl5_inv`; each row ends east in a contact to metal, at (7795,17605) and (7840,17648); the output metal runs north on x 7795, the input on a vertical metal x 7839); its load box is on VCC (bc1's rail RL2, x 7470-7520), its pull-down box on VSS (RL3, x 7641-7691) |
| `bc2_w#` | a wire of the bottom-centre logic (`notes/blocks/bc2.md`), by the y of its pad or defining row. East column latch unit a (x 10380-10778, y 14800-15285, `tl1`'s unit at 7940,10454): `bc2_w14912` data (pad (10395,14912), metal west), `bc2_w14955` enable (metal x 10441, pads (10441,14955), (10441,15172)), `inh_src` clear (pad (10395,15087), metal x 10395 south), `bc2_w14876` = NOT `bc2_w14912` (the cell's thin metal x 10500), `bc2_w15000` = NOT(`bc2_w14912` AND `bc2_w14955` OR `bc2_w15029`): output, pad (10395,15000), metal from the north-west; `bc2_w15029` = NOT(`inh_src` OR `bc2_w14955` AND `bc2_w14876` OR `bc2_w15000`): the other side, not taken out; `bc2_w14955`'s metal x 10441 jogs west at y 15392 to x 10398 and runs on south (it does not reach unit b's pads). Latch unit b (x 10212-10779, y 15277-15752, the same unit at 7941,10930): `bc2_w15388` data (pad (10352,15388), metal x 10353 south), `bc2_w15432` enable (metal x 10441 from y 15418 south, pads (10441,15432), (10441,15650)), `bc2_w15565` clear (pad (10226,15565), metal x 10226 north), `bc2_w15352` = NOT `bc2_w15388` (the cell's thin metal x 10500), `bc2_w15476` = NOT(`bc2_w15388` AND `bc2_w15432` OR `bc2_w15607`): the upper node, not taken out; `bc2_w15607` = NOT(`bc2_w15565` OR `bc2_w15432` AND `bc2_w15352` OR `bc2_w15476`): output, the lower node's row to the pad (10267,15607), metal x 10267 north. Sources and destinations not followed |
| `bc1_g#_in`, `bc1_g#_out` | input and output of inverter 6 |

## Odd ones

| Name | What it is |
|---|---|
| `rdp#_n#s#`, `rdp#_t#` | two short pieces of bundle wiring in the right datapath, named by track and position |

## Former names

Names used before 2026-11-16, for reading older commits; `tools/rename.py` adds a line for
every later rename. Row tags of the counter cells changed with the names: r18...r11 became
hc0...hc7, r10...r4 became rc0...rc6, r3...r0 became c4b0...c4b3; slice tags of the lower right
datapath s1...s7, s0 became b0...b6, b7.

| Old | New | Example |
|---|---|---|
| areg_load | ar_load | |
| bd2_a | wr_data_sel_n | |
| bd2_al_n | ar_load_n | |
| bd3_b12 | rsel12_buf | |
| bd2_c | wr_data_sel | |
| bd1_g | inh_src | |
| bd1_k7 | h_eq_r0_u | |
| bd1_k8 | h_eq_r1_u | |
| bd1_k5 | h_eq_r0half | |
| bd1_k14 | hc3 | |
| bd1_k17 | hc0 | |
| bd1_k9 | hc2 | |
| bd2_m255 | bd2_rs_n | |
| bd2_m210 | wr_addr_sel | |
| bd3_n12 | rsel12_bufn | |
| bd2_n1 | wr_data_lat | |
| bd2_nu | wr_data_e_n | |
| bd2_qb | wr_data_lat_n | |
| bd1_x | inh_n | |
| bd1_xn2 | inh_lat | |
| bd1_xn1 | inh_rc | |
| ck_src | inh_ck | |
| mra_a_r# | c#b#_m | mra_a_r0 -> c4b3_m |
| mra_a_r# | hc#_m | mra_a_r11 -> hc7_m |
| mra_a_r# | rc#_m | mra_a_r10 -> rc0_m |
| mra_b_r# | c#b#_mb | mra_b_r0 -> c4b3_mb |
| mra_b_r# | hc#_mb | mra_b_r11 -> hc7_mb |
| mra_b_r# | rc#_mb | mra_b_r10 -> rc0_mb |
| mra_busa | cnt_bus_a | |
| mra_busb | cnt_bus_b | |
| mra_busg | h_eq_r2 | |
| mra_cin_r3 | c4b_ci | |
| mra_cin_r18 | hc_ci | |
| mra_cin_r10 | rc_ci | |
| mra_cka2 | ck_a_u | |
| mra_ckb | ck_b | |
| mra_d_r# | c#b#_d | mra_d_r0 -> c4b3_d |
| mra_d_r# | hc#_d | mra_d_r11 -> hc7_d |
| mra_d_r# | rc#_d | mra_d_r10 -> rc0_d |
| mra_g#_r# | c#b#_q_n | mra_g1_r0 -> c4b3_q_n |
| mra_g#_r# | hc#_q_n | mra_g1_r11 -> hc7_q_n |
| mra_g#_r# | rc#_q_n | mra_g1_r10 -> rc0_q_n |
| mra_gab | cnt_gab | |
| mra_gla | rc_lo4_set | |
| mra_glb | hc_lo4_set | |
| mra_l2a | cnt_l2_a | |
| mra_l2b | cnt_l2_b | |
| mra_l2c | cnt_l2_c | |
| mra_l3m | rc_l3 | |
| mra_l3n | c4b_l3 | |
| mra_la | cnt_la_a | |
| mra_la2 | cnt_la_b | |
| mra_la3 | cnt_la_c | |
| mra_m7 | rc_ck_m | |
| mra_m_r# | c#b#_nx | mra_m_r0 -> c4b3_nx |
| mra_m_r# | hc#_nx | mra_m_r11 -> hc7_nx |
| mra_m_r# | rc#_nx | mra_m_r10 -> rc0_nx |
| mra_md_r# | c#b#_md | mra_md_r0 -> c4b3_md |
| mra_md_r# | hc#_md | mra_md_r11 -> hc7_md |
| mra_md_r# | rc#_md | mra_md_r10 -> rc0_md |
| mra_mt_r0 | c4b3_mt | |
| mra_mt_r# | hc#_mt | mra_mt_r11 -> hc7_mt |
| mra_n#_r# | c#b# | mra_n1_r0 -> c4b3 |
| mra_n#_r# | c#b#_ci_n | mra_n2_r0 -> c4b3_ci_n |
| mra_n#_r# | hc# | mra_n1_r11 -> hc7 |
| mra_n#_r# | hc#_ci_n | mra_n2_r11 -> hc7_ci_n |
| mra_n#_r# | rc# | mra_n1_r10 -> rc0 |
| mra_n#_r# | rc#_ci_n | mra_n2_r10 -> rc0_ci_n |
| mra_na_r# | c#b#_nx_g | mra_na_r0 -> c4b3_nx_g |
| mra_na_r# | hc#_nx_g | mra_na_r11 -> hc7_nx_g |
| mra_na_r# | rc#_nx_g | mra_na_r10 -> rc0_nx_g |
| mra_nb_r# | c#b#_nx_n | mra_nb_r0 -> c4b3_nx_n |
| mra_nb_r# | hc#_nx_n | mra_nb_r11 -> hc7_nx_n |
| mra_nb_r# | rc#_nx_n | mra_nb_r10 -> rc0_nx_n |
| mra_p#_r# | c#b#_m_n | mra_p3_r0 -> c4b3_m_n |
| mra_p#_r# | hc#_m_n | mra_p3_r11 -> hc7_m_n |
| mra_p#_r# | rc#_m_n | mra_p3_r10 -> rc0_m_n |
| mra_q_r# | c#b#_q | mra_q_r0 -> c4b3_q |
| mra_q_r# | hc#_q | mra_q_r11 -> hc7_q |
| mra_q_r# | rc#_q | mra_q_r10 -> rc0_q |
| mra_rb_r# | c#b#_rb | mra_rb_r0 -> c4b3_rb |
| mra_rb_r# | hc#_rb | mra_rb_r11 -> hc7_rb |
| mra_rb_r# | rc#_rb | mra_rb_r10 -> rc0_rb |
| mra_s7 | rc_ck_s | |
| mra_tab_r# | c#b#_tab | mra_tab_r0 -> c4b3_tab |
| mra_tab_r# | hc#_tab | mra_tab_r11 -> hc7_tab |
| mra_tab_r# | rc#_tab | mra_tab_r10 -> rc0_tab |
| mra_x_r# | c#b#_co | mra_x_r0 -> c4b3_co |
| mra_x_r# | hc#_co | mra_x_r11 -> hc7_co |
| mra_x_r# | rc#_co | mra_x_r10 -> rc0_co |
| mra_z_r# | c#b#_z | mra_z_r0 -> c4b3_z |
| mra_z_r# | hc#_z | mra_z_r11 -> hc7_z |
| mra_z_r# | rc#_z | mra_z_r10 -> rc0_z |
| rdp3_ar_ld | ar_load | |
| rdp#_ar_s#_a | ar#_a | rdp3_ar_s1_a -> ar0_a |
| rdp#_ar_s#_n# | ar#_n# | rdp3_ar_s1_n2 -> ar0_n2 |
| rdp#_ar_s#_q | ar#_q | rdp3_ar_s1_q -> ar0_q |
| rdp#_ar_s#_trk | ar#_trk | rdp3_ar_s1_trk -> ar0_trk |
| rdp#_bus_s# | rbus_b# | rdp3_bus_s0 -> rbus_b7 |
| rdp#_c_s# | hc# | rdp3_c_s0 -> hc7 |
| rdp#_c_s# | hc#_u | rdp3_c_s1 -> hc0_u |
| rdp3_ca_eq | h_eq_r1 | |
| rdp#_ca_s#_nor | r#c_b#_nor | rdp3_ca_s0_nor -> r1c_b7_nor |
| rdp#_ca_s#_x | r#c_b#_x | rdp3_ca_s0_x -> r1c_b7_x |
| rdp3_cb_eq | h_eq_r2 | |
| rdp#_cb_s#_nor | r#c_b#_nor | rdp3_cb_s0_nor -> r2c_b7_nor |
| rdp#_cb_s#_x | r#c_b#_x | rdp3_cb_s0_x -> r2c_b7_x |
| rdp2_cc_eq | h_eq_r0 | |
| rdp#_cc_s#_nor | r#c_b#_nor | rdp2_cc_s0_nor -> r0c_b7_nor |
| rdp#_cc_s#_x | r#c_b#_x | rdp2_cc_s0_x -> r0c_b7_x |
| rdp2_cd_eq | h_eq_r0half | |
| rdp#_cd_s#_nor | r#hc_s#_nor | rdp2_cd_s1_nor -> r0hc_s1_nor |
| rdp#_cd_s#_x | r#hc_s#_x | rdp2_cd_s1_x -> r0hc_s1_x |
| rdp2_ce_eq | uc_eq_r4 | |
| rdp#_ce_s#_nor | r#c_s#_nor | rdp2_ce_s0_nor -> r4c_s0_nor |
| rdp#_ce_s#_x | r#c_s#_x | rdp2_ce_s0_x -> r4c_s0_x |
| rdp2_ce_sm1_nor | r4c_sm1_nor | |
| rdp2_ce_sm1_x | r4c_sm1_x | |
| rdp3_n4 | rc0 | |
| rdp3_n5 | rc1 | |
| rdp3_n6 | rc2 | |
| rdp3_n8 | rc3 | |
| rdp3_ra_ld | wr_r1_u | |
| rdp#_ra_s#_a | r#_b#_a | rdp3_ra_s0_a -> r1_b7_a |
| rdp#_ra_s#_n# | r#_b#_n# | rdp3_ra_s0_n2 -> r1_b7_n2 |
| rdp#_ra_s#_q | r#_b#_q | rdp3_ra_s0_q -> r1_b7_q |
| rdp3_rb_ld | wr_r2_u | |
| rdp#_rb_s#_a | r#_b#_a | rdp3_rb_s0_a -> r2_b7_a |
| rdp#_rb_s#_n# | r#_b#_n# | rdp3_rb_s0_n2 -> r2_b7_n2 |
| rdp#_rb_s#_q | r#_b#_q | rdp3_rb_s0_q -> r2_b7_q |
| rdp3_rc_ld | wr_r0_u | |
| rdp#_rc_s#_a | r#_b#_a | rdp3_rc_s0_a -> r0_b7_a |
| rdp#_rc_s#_n# | r#_b#_n# | rdp3_rc_s0_n2 -> r0_b7_n2 |
| rdp#_rc_s#_q | r#_b#_q | rdp3_rc_s0_q -> r0_b7_q |
| rdp2_re_ld | wr_r4_u | |
| rdp#_re_s#_a | r#_s#_a | rdp3_re_s0_a -> r4_s0_a |
| rdp#_re_s#_n# | r#_s#_n# | rdp3_re_s0_n2 -> r4_s0_n2 |
| rdp#_re_s#_q | r#_s#_q | rdp3_re_s0_q -> r4_s0_q |
| rdp3_re_sm1_a | r4_sm1_a | |
| rdp3_re_sm1_n2 | r4_sm1_n2 | |
| rdp3_re_sm1_q | r4_sm1_q | |
| rdp2_rf_ld | wr_r6 | |
| rdp#_rf_s#_a | r#_s#_a | rdp3_rf_s0_a -> r6_s0_a |
| rdp#_rf_s#_n# | r#_s#_n# | rdp3_rf_s0_n2 -> r6_s0_n2 |
| rdp#_rf_s#_q | r#_s#_q | rdp3_rf_s0_q -> r6_s0_q |
| rdp3_rf_sm1_a | r6_sm1_a | |
| rdp3_rf_sm1_n2 | r6_sm1_n2 | |
| rdp3_rf_sm1_q | r6_sm1_q | |
| rdp3_s0 | inh_rc | |
| rdp#_ubus_s# | ubus_s# | rdp2_ubus_s0 -> ubus_s0 |
| rdp2_ubus_sm1 | ubus_sm1 | |
| rdp#_uc_s# | uc_s# | rdp2_uc_s0 -> uc_s0 |
| rdp2_uc_sm1 | uc_sm1 | |
| sel_b# | rsel#_buf | sel_b13 -> rsel13_buf |
| sel_bn# | rsel#_bn | sel_bn13 -> rsel13_bn |
| sel_n# | rsel#_n | sel_n0 -> rsel0_n |
| sel_stb_l | wr_stb_n | |
| sel_stb_r | wr_stb_n | |
| sel_w# | wr_r# | sel_w0 -> wr_r0 |
| t_g0_in | inh_n | |
| t_g0_out | inh_ck | |
| tla_a2 | rcs_a2 | |
| tla_b1 | rcs_b1 | |
| tla_c1 | rcs_c1 | |
| tla_e# | rcs_e# | tla_e3 -> rcs_e3 |
| tla_in# | rcs_in# | tla_in1 -> rcs_in1 |
| tla_m2 | rcs_m2 | |
| tla_thin | rcs_thin_e | |
| tla_thinw | rcs_thin_w | |
| tla_w2 | rcs_w2 | |
| tla_x1 | rcs_x1 | |
| wl_b | rc_stepreq_n | |
| wl_d_buf | rc_ck_s_dly | |
| wl_d_n | rc_ck_s_n | |
| wl_e_buf | rc_ck_m_dly | |
| wl_e_n | rc_ck_m_n | |
| wl_la_n | cnt_la_a_n | |
| wl_p | rc_step | |
| wl_pb | rc_step_n | |
| h_eq_r0_u | h_eq_r0 | |
| h_eq_r1_u | h_eq_r1 | |
| rcs_ba4100 | rcs_cond | |
| rcs_cm4028 | rcs_cond_lat | |
| rcs_m2 | rcs_cond_n | |
| rcs_bb3807 | rcs_stb | |
| rcs_stb_n | ck_out | |
| rcs_stb | clk_tl | |
| bd1_k4 | uc_eq_r6 | |
| c4b0 | hsw0 | |
| c4b0_ci_n | hsw0_ci_n | |
| c4b0_co | hsw0_co | |
| c4b0_d | hsw0_d | |
| c4b0_m | hsw0_m | |
| c4b0_m_n | hsw0_m_n | |
| c4b0_mb | hsw0_mb | |
| c4b0_nx | hsw0_nx | |
| c4b0_nx_g | hsw0_nx_g | |
| c4b0_nx_n | hsw0_nx_n | |
| c4b0_q | hsw0_q | |
| c4b0_q_n | hsw0_q_n | |
| c4b0_rb | hsw0_rb | |
| c4b0_tab | hsw0_tab | |
| c4b0_z | hsw0_z | |
| c4b1 | hsw1 | |
| c4b1_ci_n | hsw1_ci_n | |
| c4b1_co | hsw1_co | |
| c4b1_d | hsw1_d | |
| c4b1_m | hsw1_m | |
| c4b1_m_n | hsw1_m_n | |
| c4b1_mb | hsw1_mb | |
| c4b1_md | hsw1_md | |
| c4b1_nx | hsw1_nx | |
| c4b1_nx_g | hsw1_nx_g | |
| c4b1_nx_n | hsw1_nx_n | |
| c4b1_q | hsw1_q | |
| c4b1_q_n | hsw1_q_n | |
| c4b1_rb | hsw1_rb | |
| c4b1_tab | hsw1_tab | |
| c4b1_z | hsw1_z | |
| c4b2 | hsw2 | |
| c4b2_ci_n | hsw2_ci_n | |
| c4b2_co | hsw2_co | |
| c4b2_d | hsw2_d | |
| c4b2_m | hsw2_m | |
| c4b2_m_n | hsw2_m_n | |
| c4b2_mb | hsw2_mb | |
| c4b2_md | hsw2_md | |
| c4b2_nx | hsw2_nx | |
| c4b2_nx_g | hsw2_nx_g | |
| c4b2_nx_n | hsw2_nx_n | |
| c4b2_q | hsw2_q | |
| c4b2_q_n | hsw2_q_n | |
| c4b2_rb | hsw2_rb | |
| c4b2_tab | hsw2_tab | |
| c4b2_z | hsw2_z | |
| c4b3 | hsw3 | |
| c4b3_ci_n | hsw3_ci_n | |
| c4b3_co | hsw3_co | |
| c4b3_d | hsw3_d | |
| c4b3_m | hsw3_m | |
| c4b3_m_n | hsw3_m_n | |
| c4b3_mb | hsw3_mb | |
| c4b3_md | hsw3_md | |
| c4b3_mt | hsw3_mt | |
| c4b3_nx | hsw3_nx | |
| c4b3_nx_g | hsw3_nx_g | |
| c4b3_nx_n | hsw3_nx_n | |
| c4b3_q | hsw3_q | |
| c4b3_q_n | hsw3_q_n | |
| c4b3_rb | hsw3_rb | |
| c4b3_tab | hsw3_tab | |
| c4b3_z | hsw3_z | |
| c4b_ci | hsw_ci | |
| c4b_l3 | hsw_l3 | |
| c5l0 | sl0 | |
| c5l0_ci_n | sl0_ci_n | |
| c5l0_co | sl0_co | |
| c5l0_d | sl0_d | |
| c5l0_m | sl0_m | |
| c5l0_m_n | sl0_m_n | |
| c5l0_mb | sl0_mb | |
| c5l0_nx | sl0_nx | |
| c5l0_nx_g | sl0_nx_g | |
| c5l0_nx_n | sl0_nx_n | |
| c5l0_q | sl0_q | |
| c5l0_q_n | sl0_q_n | |
| c5l0_rb | sl0_rb | |
| c5l0_tab | sl0_tab | |
| c5l0_z | sl0_z | |
| c5l1 | sl1 | |
| c5l1_ci_n | sl1_ci_n | |
| c5l1_co | sl1_co | |
| c5l1_d | sl1_d | |
| c5l1_m | sl1_m | |
| c5l1_m_n | sl1_m_n | |
| c5l1_mb | sl1_mb | |
| c5l1_md | sl1_md | |
| c5l1_nx | sl1_nx | |
| c5l1_nx_g | sl1_nx_g | |
| c5l1_nx_n | sl1_nx_n | |
| c5l1_q | sl1_q | |
| c5l1_q_n | sl1_q_n | |
| c5l1_rb | sl1_rb | |
| c5l1_tab | sl1_tab | |
| c5l1_z | sl1_z | |
| c5l2 | sl2 | |
| c5l2_ci_n | sl2_ci_n | |
| c5l2_co | sl2_co | |
| c5l2_d | sl2_d | |
| c5l2_m | sl2_m | |
| c5l2_m_n | sl2_m_n | |
| c5l2_mb | sl2_mb | |
| c5l2_md | sl2_md | |
| c5l2_nx | sl2_nx | |
| c5l2_nx_g | sl2_nx_g | |
| c5l2_nx_n | sl2_nx_n | |
| c5l2_q | sl2_q | |
| c5l2_q_n | sl2_q_n | |
| c5l2_rb | sl2_rb | |
| c5l2_tab | sl2_tab | |
| c5l2_z | sl2_z | |
| c5l3 | sl3 | |
| c5l3_ci_n | sl3_ci_n | |
| c5l3_co | sl3_co | |
| c5l3_d | sl3_d | |
| c5l3_m | sl3_m | |
| c5l3_m_n | sl3_m_n | |
| c5l3_mb | sl3_mb | |
| c5l3_md | sl3_md | |
| c5l3_nx | sl3_nx | |
| c5l3_nx_g | sl3_nx_g | |
| c5l3_nx_n | sl3_nx_n | |
| c5l3_q | sl3_q | |
| c5l3_q_n | sl3_q_n | |
| c5l3_rb | sl3_rb | |
| c5l3_tab | sl3_tab | |
| c5l3_z | sl3_z | |
| c5l4 | sl4 | |
| c5l4_ci_n | sl4_ci_n | |
| c5l4_co | sl4_co | |
| c5l4_d | sl4_d | |
| c5l4_m | sl4_m | |
| c5l4_m_n | sl4_m_n | |
| c5l4_mb | sl4_mb | |
| c5l4_md | sl4_md | |
| c5l4_nx | sl4_nx | |
| c5l4_nx_g | sl4_nx_g | |
| c5l4_nx_n | sl4_nx_n | |
| c5l4_q | sl4_q | |
| c5l4_q_n | sl4_q_n | |
| c5l4_rb | sl4_rb | |
| c5l4_tab | sl4_tab | |
| c5l4_z | sl4_z | |
| c5l_gab | sl_gab | |
| c5l_l3 | sl_l3 | |
| hsw_eq_r3_x | hsw_eq_r3 | |
| r3_t0_a | r3_b0_a | |
| r3_t0_d | r3_b0_d | |
| r3_t0_n2 | r3_b0_n2 | |
| r3_t0_q | r3_b0_q | |
| r3_t1_a | r3_b1_a | |
| r3_t1_d | r3_b1_d | |
| r3_t1_n2 | r3_b1_n2 | |
| r3_t1_q | r3_b1_q | |
| r3_t2_a | r3_b2_a | |
| r3_t2_d | r3_b2_d | |
| r3_t2_n2 | r3_b2_n2 | |
| r3_t2_q | r3_b2_q | |
| r3_t3_a | r3_b3_a | |
| r3_t3_d | r3_b3_d | |
| r3_t3_n2 | r3_b3_n2 | |
| r3_t3_q | r3_b3_q | |
| r3c_t0_nor | r3c_b0_nor | |
| r3c_t0_x | r3c_b0_x | |
| r3c_t1_nor | r3c_b1_nor | |
| r3c_t1_x | r3c_b1_x | |
| r3c_t2_nor | r3c_b2_nor | |
| r3c_t2_x | r3c_b2_x | |
| r3c_t3_nor | r3c_b3_nor | |
| r3c_t3_x | r3c_b3_x | |
| r4_s0_a | r4_b1_a | |
| r4_s0_n2 | r4_b1_n2 | |
| r4_s0_q | r4_b1_q | |
| r4_s1_a | r4_b2_a | |
| r4_s1_n2 | r4_b2_n2 | |
| r4_s1_q | r4_b2_q | |
| r4_s2_a | r4_b3_a | |
| r4_s2_n2 | r4_b3_n2 | |
| r4_s2_q | r4_b3_q | |
| r4_s3_a | r4_b4_a | |
| r4_s3_n2 | r4_b4_n2 | |
| r4_s3_q | r4_b4_q | |
| r4_s4_a | r4_b5_a | |
| r4_s4_n2 | r4_b5_n2 | |
| r4_s4_q | r4_b5_q | |
| r4_s5_a | r4_b6_a | |
| r4_s5_n2 | r4_b6_n2 | |
| r4_s5_q | r4_b6_q | |
| r4_sm1_a | r4_b0_a | |
| r4_sm1_n2 | r4_b0_n2 | |
| r4_sm1_q | r4_b0_q | |
| r4c_s0_nor | r4c_b1_nor | |
| r4c_s0_x | r4c_b1_x | |
| r4c_s1_nor | r4c_b2_nor | |
| r4c_s1_x | r4c_b2_x | |
| r4c_s2_nor | r4c_b3_nor | |
| r4c_s2_x | r4c_b3_x | |
| r4c_s3_nor | r4c_b4_nor | |
| r4c_s3_x | r4c_b4_x | |
| r4c_s4_nor | r4c_b5_nor | |
| r4c_s4_x | r4c_b5_x | |
| r4c_s5_nor | r4c_b6_nor | |
| r4c_s5_x | r4c_b6_x | |
| r4c_sm1_nor | r4c_b0_nor | |
| r4c_sm1_x | r4c_b0_x | |
| r5_s0_a | r5_b1_a | |
| r5_s0_n2 | r5_b1_n2 | |
| r5_s0_q | r5_b1_q | |
| r5_s1_a | r5_b2_a | |
| r5_s1_n2 | r5_b2_n2 | |
| r5_s1_q | r5_b2_q | |
| r5_s2_a | r5_b3_a | |
| r5_s2_n2 | r5_b3_n2 | |
| r5_s2_q | r5_b3_q | |
| r5_s3_a | r5_b4_a | |
| r5_s3_n2 | r5_b4_n2 | |
| r5_s3_q | r5_b4_q | |
| r5_sm1_a | r5_b0_a | |
| r5_sm1_n2 | r5_b0_n2 | |
| r5_sm1_q | r5_b0_q | |
| r5c_s0_nor | r5c_b1_nor | |
| r5c_s0_x | r5c_b1_x | |
| r5c_s1_nor | r5c_b2_nor | |
| r5c_s1_x | r5c_b2_x | |
| r5c_s2_nor | r5c_b3_nor | |
| r5c_s2_x | r5c_b3_x | |
| r5c_s3_nor | r5c_b4_nor | |
| r5c_s3_x | r5c_b4_x | |
| r5c_sm1_nor | r5c_b0_nor | |
| r5c_sm1_x | r5c_b0_x | |
| r6_s0_a | r6_b1_a | |
| r6_s0_n2 | r6_b1_n2 | |
| r6_s0_q | r6_b1_q | |
| r6_s1_a | r6_b2_a | |
| r6_s1_n2 | r6_b2_n2 | |
| r6_s1_q | r6_b2_q | |
| r6_s2_a | r6_b3_a | |
| r6_s2_n2 | r6_b3_n2 | |
| r6_s2_q | r6_b3_q | |
| r6_s3_a | r6_b4_a | |
| r6_s3_n2 | r6_b4_n2 | |
| r6_s3_q | r6_b4_q | |
| r6_s4_a | r6_b5_a | |
| r6_s4_n2 | r6_b5_n2 | |
| r6_s4_q | r6_b5_q | |
| r6_s5_a | r6_b6_a | |
| r6_s5_n2 | r6_b6_n2 | |
| r6_s5_q | r6_b6_q | |
| r6_sm1_a | r6_b0_a | |
| r6_sm1_n2 | r6_b0_n2 | |
| r6_sm1_q | r6_b0_q | |
| r6c_s0_nor | r6c_b1_nor | |
| r6c_s0_x | r6c_b1_x | |
| r6c_s1_nor | r6c_b2_nor | |
| r6c_s1_x | r6c_b2_x | |
| r6c_s2_nor | r6c_b3_nor | |
| r6c_s2_x | r6c_b3_x | |
| r6c_s3_nor | r6c_b4_nor | |
| r6c_s3_x | r6c_b4_x | |
| r6c_s4_nor | r6c_b5_nor | |
| r6c_s4_x | r6c_b5_x | |
| r6c_s5_nor | r6c_b6_nor | |
| r6c_s5_x | r6c_b6_x | |
| r6c_sm1_nor | r6c_b0_nor | |
| r6c_sm1_x | r6c_b0_x | |
| r7_s0_a | r7_b1_a | |
| r7_s0_n2 | r7_b1_n2 | |
| r7_s0_q | r7_b1_q | |
| r7_s1_a | r7_b2_a | |
| r7_s1_n2 | r7_b2_n2 | |
| r7_s1_q | r7_b2_q | |
| r7_s2_a | r7_b3_a | |
| r7_s2_n2 | r7_b3_n2 | |
| r7_s2_q | r7_b3_q | |
| r7_s3_a | r7_b4_a | |
| r7_s3_n2 | r7_b4_n2 | |
| r7_s3_q | r7_b4_q | |
| r7_s4_a | r7_b5_a | |
| r7_s4_n2 | r7_b5_n2 | |
| r7_s4_q | r7_b5_q | |
| r7_s5_a | r7_b6_a | |
| r7_s5_n2 | r7_b6_n2 | |
| r7_s5_q | r7_b6_q | |
| r7_sm1_a | r7_b0_a | |
| r7_sm1_n2 | r7_b0_n2 | |
| r7_sm1_q | r7_b0_q | |
| r7c_s0_nor | r7c_b1_nor | |
| r7c_s0_x | r7c_b1_x | |
| r7c_s1_nor | r7c_b2_nor | |
| r7c_s1_x | r7c_b2_x | |
| r7c_s2_nor | r7c_b3_nor | |
| r7c_s2_x | r7c_b3_x | |
| r7c_s3_nor | r7c_b4_nor | |
| r7c_s3_x | r7c_b4_x | |
| r7c_s4_nor | r7c_b5_nor | |
| r7c_s4_x | r7c_b5_x | |
| r7c_s5_nor | r7c_b6_nor | |
| r7c_s5_x | r7c_b6_x | |
| r7c_sm1_nor | r7c_b0_nor | |
| r7c_sm1_x | r7c_b0_x | |
| sl_eq_r5_x | sl_eq_r5 | |
| ubus_s0 | ubus_b1 | |
| ubus_s1 | ubus_b2 | |
| ubus_s2 | ubus_b3 | |
| ubus_s3 | ubus_b4 | |
| ubus_s4 | ubus_b5 | |
| ubus_s5 | ubus_b6 | |
| ubus_sm1 | ubus_b0 | |
| uc_s0 | uc_b1 | |
| uc_s1 | uc_b2 | |
| uc_s2 | uc_b3 | |
| uc_s3 | uc_b4 | |
| uc_s4 | uc_b5 | |
| uc_s5 | uc_b6 | |
| uc_sm1 | uc_b0 | |
| cdp2_ch1_5826 | ch1w_5758 | |
| ch1w_5890 | cdp2_trk_s6 | |
| ch1w_5848 | cdp2_trk_s5 | |
| ch1w_5800 | cdp2_trk_s4 | |
| ch1w_5758 | rax_o4 | |
| cdp1_a_wr | wr_r8 | |
| cdp1_c_wr | wr_r9 | |
| cdp2_a_ld | wr_r11 | |
| cdp2_c_ld | wr_r10 | |
| tc1_b | ras_shift | |
| tc1_l2_out | ras_o0_sel2 | |
| tc1_l1_out | ras_straight | |
| tc1_l3_out | ras_o0_sel1 | |
| tc1_ns6 | cdp1_a5_q | |
| tc1_ns5 | cdp1_a4_q | |
| fld_x_a | cnt_la_a_n | |
| fld_y_a | rc0_n | via wl_i2_out |
| wl_i2_in | rc0 | |
| wl_i2_out | rc0_n | |
| h_eq_r2_u | h_eq_r2 | |
| wr_r0_u | wr_r0 | |
| wr_r1_u | wr_r1 | |
| wr_r2_u | wr_r2 | |
| wr_r4_u | wr_r4 | |
| rdp3_n1s4 | wr_r4 | |
| hc0_u | hc0 | |
| hc1_u | hc1 | |
| hc2_u | hc2 | |
| hc3_u | hc3 | |
| hc4_u | hc4 | |
| hc5_u | hc5 | |
| bd1_k11 | hc1 | |
| ra3_drv_in_u | ra3_drv_in | |
| ral_frc | cnt_gab | |
| ral_tf_s# | ral_n1_s# | |
| ral_tf_m# | ral_n1_m# | |
| tc1_ns4 | ral_stb | |
| ra2_drv_in_u | ra2_drv_in | |
| uc_b0 | rc0 | |
| uc_b1 | rc1 | |
| uc_b2 | rc2 | |
| uc_b3 | rc3 | |
| uc_b4 | rc4 | |
| uc_b5 | rc5 | |
| uc_b6 | rc6 | |
| uc_eq_r4 | rc_eq_r4 | |
| uc_eq_r6 | rc_eq_r6 | |
| uc_eq_r7 | rc_eq_r7 | |
| cdp1_l4719 | sl_eq_r5 | |
| rdp3_n2s1 | h_eq_r0 | |
| rdp3_n0 | h_eq_r0half | |
| cdp1_b_eq | ra_eq_r9 | |
| rcs_bq3335 | ra_eq_r9 | |
| cdp1_a0_x | r8_b5_a | |
| cdp1_a0_q1 | r8_b5_n2 | |
| cdp1_a0_q | r8_b5_q | |
| cdp1_a0_m3 | r8_b5_m3 | |
| cdp1_a0_m6 | r8_b5_m6 | |
| cdp1_a0_bl | db_b5 | |
| cdp1_a1_x | r8_b4_a | |
| cdp1_a1_q1 | r8_b4_n2 | |
| cdp1_a1_q | r8_b4_q | |
| cdp1_a1_m3 | r8_b4_m3 | |
| cdp1_a1_m6 | r8_b4_m6 | |
| cdp1_a1_bl | db_b4 | |
| cdp1_a2_x | r8_b7_a | |
| cdp1_a2_q1 | r8_b7_n2 | |
| cdp1_a2_q | r8_b7_q | |
| cdp1_a2_m3 | r8_b7_m3 | |
| cdp1_a2_m6 | r8_b7_m6 | |
| cdp1_a2_bl | db_b7 | |
| cdp1_a3_x | r8_b6_a | |
| cdp1_a3_q1 | r8_b6_n2 | |
| cdp1_a3_q | r8_b6_q | |
| cdp1_a3_m3 | r8_b6_m3 | |
| cdp1_a3_m6 | r8_b6_m6 | |
| cdp1_a3_bl | db_b6 | |
| cdp1_a4_x | r8_b1_a | |
| cdp1_a4_q1 | r8_b1_n2 | |
| cdp1_a4_q | r8_b1_q | |
| cdp1_a4_m3 | r8_b1_m3 | |
| cdp1_a4_m6 | r8_b1_m6 | |
| cdp1_a4_bl | db_b1 | |
| cdp1_a5_x | r8_b0_a | |
| cdp1_a5_q1 | r8_b0_n2 | |
| cdp1_a5_q | r8_b0_q | |
| cdp1_a5_m3 | r8_b0_m3 | |
| cdp1_a5_m6 | r8_b0_m6 | |
| cdp1_a5_bl | db_b0 | |
| cdp1_c1_x | r9_b4_a | |
| cdp1_c1_q1 | r9_b4_n2 | |
| cdp1_c1_q | r9_b4_q | |
| cdp1_c1_m3 | r9_b4_m3 | |
| cdp1_c1_m6 | r9_b4_m6 | |
| cdp1_c1_bl | db_b4 | |
| cdp1_c2_x | r9_b3_a | |
| cdp1_c2_q1 | r9_b3_n2 | |
| cdp1_c2_q | r9_b3_q | |
| cdp1_c2_m3 | r9_b3_m3 | |
| cdp1_c2_m6 | r9_b3_m6 | |
| cdp1_c2_bl | db_b3 | |
| cdp1_c3_x | r9_b2_a | |
| cdp1_c3_q1 | r9_b2_n2 | |
| cdp1_c3_q | r9_b2_q | |
| cdp1_c3_m3 | r9_b2_m3 | |
| cdp1_c3_m6 | r9_b2_m6 | |
| cdp1_c3_bl | db_b2 | |
| cdp1_c4_x | r9_b1_a | |
| cdp1_c4_q1 | r9_b1_n2 | |
| cdp1_c4_q | r9_b1_q | |
| cdp1_c4_m3 | r9_b1_m3 | |
| cdp1_c4_m6 | r9_b1_m6 | |
| cdp1_c4_bl | db_b1 | |
| cdp1_c5_x | r9_b0_a | |
| cdp1_c5_q1 | r9_b0_n2 | |
| cdp1_c5_q | r9_b0_q | |
| cdp1_c5_m3 | r9_b0_m3 | |
| cdp1_c5_m6 | r9_b0_m6 | |
| cdp1_c5_bl | db_b0 | |
| ubus_b0 | db_b0 | |
| rbus_b0 | db_b0 | |
| ubus_b1 | db_b1 | |
| rbus_b1 | db_b1 | |
| ubus_b2 | db_b2 | |
| rbus_b2 | db_b2 | |
| ubus_b3 | db_b3 | |
| rbus_b3 | db_b3 | |
| ubus_b4 | db_b4 | |
| rbus_b4 | db_b4 | |
| ubus_b5 | db_b5 | |
| rbus_b5 | db_b5 | |
| ubus_b6 | db_b6 | |
| rbus_b6 | db_b6 | |
| rbus_b7 | db_b7 | |
| r3_b0_d | db_b0 | |
| r3_b1_d | db_b1 | |
| r3_b2_d | db_b2 | |
| r3_b3_d | db_b3 | |
| amr_oa_c1 | db_b5 | |
| amr_oa_c2 | db_b6 | |
| amr_oa_c3 | db_b7 | |
| cdp1_lw2 | db_b6 | |
| tc1_x2 | db_b6 | |
| tc1_m7013 | tc1_o3095 | |
| tc1_o3740_u | tc1_p3051 | |
| tc1_b2554 | tc1_bus2554 | |
| tc1_b2684 | tc1_bus2684 | |
| tc1_b2814 | tc1_bus2814 | |
| tc1_b2858 | tc1_bus2858 | |
| cdp1_l4544 | c4l0 | |
| cdp1_l4588 | c4l1 | |
| amr_ob_c1 | c4l1 | |
| tla_w3461 | amr_eq_r3 | |
| areg_w6 | dl7_q_n | |
| areg_w7 | dl6_q_n | |
| tl1_w2506 | tl1_w5936 | |
| tl4_w3808 | rcs_e3 | |
| tl5_w5717 | rcs_mv | |
| tl5_w5890 | rcs_x1 | |
| tcw_a | inh_ck | |
| lc2_w8172 | inh_ck | |
| tl3_e4152 | inh_ck | |
| tl4_w4501 | inh_ck | |
| tl5_w5631 | inh_ck | |
| lc1_w7140 | rcs_x1 | |
| tl1_w4025 | rcs_x1 | |
| tl3_w3506 | rcs_x1 | |
| tl3_w4200 | rcs_x1 | |
| tl3_w5112 | rcs_x1 | |
| tl3_e4808 | rcs_x1 | |
| rcs_g4240 | rcs_x1 | |
| tl3_e4915 | rcs_mv | |
| tl3_w3765 | rcs_a2 | |
| lc1_w7343 | res_b | |
| lc1_w7257 | lpstb_b | |
| bd1_a | rc_eq_r4 | |
| rdp3_n7s9 | rc_eq_r4 | |
| tl4_w5455 | c4l_l3 | |
| tl5_w5457 | c4l_l3 | |
| tcw_m6232 | c4l_gab | |
| tl5_w4590 | c4l_gab | |
| r9m_l1w | sl_eq_r5_n | |
| tl4_w2512 | sl_eq_r5_n | |
| tl1_w2592 | sl_eq_r5_n | |
| lc1_w7304 | rst | |
| lc1_w7468 | rst_n | |
| lc1_w7606 | rst_a | |
| tl5_w3636 | rst_a | |
| tl4_w4198 | rst_a | |
| lc1_w7734 | rst_b | |
| lc1_w7864 | rst_c | |
| tl3_e4635_u | tl3_e4635 | |
| lc2_w8254 | rst_c | |
| lc2_w8731 | rst_c | |
| bc2_w15087 | inh_src | |
