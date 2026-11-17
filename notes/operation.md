# How the HD6845S works: what the trace has established

This is the short version. The block notes (`notes/blocks/`) are the reference; the
glossary of names is `notes/signals.md`. Last checked against the extraction on
2026-11-17 (2,191 nets, 3,890 transistors; third refresh).

## How to read this page

Every statement carries one of three marks.

| Mark | Meaning |
|---|---|
| **Firm** | The extracted netlist says it, and still says it when every item marked uncertain (`?`) is deleted from the trace. `tools/unsure.py --equations NAME` prints this for any equation: 779 of the 1,136 extracted equations are firm. |
| **Marked** | Extracted, but it depends on at least one uncertain item or on a join that is believed and not drawn. The assumption is named. |
| **Open** | Not traced. Nothing is claimed. |

"Firm" means the drawing says so without any flagged doubt. It does not mean the chip
has been simulated: nothing has been.

**The short answer to the three questions this page was asked to answer:**

- *What is each counter clocked on?* Known, and firm, for all five counters found so far.
- *How is each counter reset?* **Open for every counter.** The cell's next-value network
  is not fully extracted. One candidate mechanism is known (below).
- *What happens when each comparator fires?* **Open for every comparator.** Each
  comparator's output is traced some way; none is traced into the logic that uses it,
  except that the row counter's step logic is partly known.

## Clocks

| Fact | Mark |
|---|---|
| Two phases are made from CLK. `ck_b` can be high only while CLK is high; `ck_a` only while CLK is low. Each waits for the other to fall (cross-coupled NORs with two-inverter delays), so they never overlap. | Firm |
| `ck_b` is also held low whenever `inh_ck` is high. | Firm (the gate); the inverter that makes `inh_ck` has one uncertain item |
| `inh_ck`, `inh_rc` and `inh_lat` are three copies of one signal, `inh_src`. | Firm |
| Where `inh_src` comes from, and so what it means. | Open |
| A separate large buffer makes `ck_out` = NOT CLK for the rest of the chip; `clk_tl` = NOT `ck_out` is used in the top-left logic. | Firm, except the join from the CLK pad to the buffer (one uncertain item in the pad's input network) |

## Counters

Five counters are identified. All use the same master-slave bit cell.

| Counter | Bits | Clocked by | Gets a clock when | Mark |
|---|---|---|---|---|
| Horizontal character counter `hc` | 8 | `ck_b` and `ck_a` directly | every CLK cycle in which `ck_b` is allowed to rise | Firm |
| Horizontal sync width counter `hsw` | 4 | `ck_b` and `ck_a` directly | as above | Firm |
| Character row counter `rc` | 7 | its own pair `rc_ck_m`, `rc_ck_s` | once per pulse of `rc_step` | Firm |
| Scan line counter `sl` | 5 | a second pair `lc_ck_m`, `lc_ck_s` | once per pulse of `lc_step` | Firm |
| A 4-bit counter `c4l`, compared with R3 bits 4-7 (`amr`): believed the vertical sync width counter | 4 | the same pair as `sl` | once per pulse of `lc_step` | Firm |

How the two private clock pairs are made (the same cell twice):

    X_ck_m = NOR(X_step_n, X_ck_s delayed)      master clock: high during the step pulse
    X_ck_s = NOR(X_step,   X_ck_m delayed)      slave clock: high between pulses

| Fact | Mark |
|---|---|
| The two equations above, for both copies. | Firm |
| `rc_step` = NOR(`inh_rc`, `rc_stepreq_n`): the row counter steps when the step logic asks and the inhibit signal is low. | Firm |
| `rc_stepreq_n` = NOR of three terms; the step happens when term 1 is high, or when NOT `rcs_e4` AND NOT (`rcs_e3` AND `rcs_a2`). | Marked (one term's gate has an uncertain item); and the inputs `rcs_e3`, `rcs_e4`, `rcs_a2` are **not identified**. `rcs_e4` = NOR(`tl1_w4678`, `tl1_w4937`) (marked: the load's tie; the pull-downs and the join to the line are drawn without `?`). **`tl1_w4678` is the output of two latches in series** (`notes/blocks/tl1.md`; marked: all pull-downs are drawn without `?`, but each latch's cross-coupling runs over its load plates, whose four ties to their nodes are `?`). Each latch is a cross-coupled pair: `tl1_w4703` = NOT(`tl1_w3594` AND `tl1_w4243` OR `tl1_w4678`), `tl1_w4678` = NOT(`tl1_w3594` AND NOT `tl1_w4243` OR `tl1_w4703` OR `tl1_w4025`), so it is open while `tl1_w3594` is high and then takes `tl1_w4243`; the first latch, a copy, is open while `tl1_w3636` = NOR(`tl1_w3594`, `tl1_w3678`) (firm) is high, takes `tl1_w2857`, and feeds `tl1_w4243`. So `rcs_e4` = NOT `tl1_w4937` AND NOT (`tl1_w2857` as it was while `tl1_w3594` and `tl1_w3678` were last both low, passed on while `tl1_w3594` is high), and `tl1_w4025` high clears both latches (making `rcs_e4` = NOT `tl1_w4937`). **Open**: what `tl1_w2857`, `tl1_w3594`, `tl1_w3678`, `tl1_w4025`, `tl1_w4937` are; all enter on poly rows from the east |
| Term 1 is `rcs_in1` = NOR(`rcs_mu`, `rcs_mv`), and `rcs_mu` is made by an inverter whose input is **R9's match** (`ra_eq_r9`): so term 1 = R9's match AND NOT `rcs_mv`. The row counter steps when the scan line (as compared at the RA pins) equals R9, unless `rcs_mv`. | Firm for the join from R9's comparator to the inverter (AMB-013, resolved 2026-11-17); marked for the equations (the comparator's NOR and `rcs_in1` depend on uncertain items). `rcs_mv` is open |
| In the west column of the same cluster an inverting two-way selector: `tla_w3417` = NOT(`rcs_thin_e` AND `tla_w3376` OR NOT `rcs_thin_e` AND `amr_eq_r3`). The select is the net on the thin metal that runs the length of the cluster; its driver, the source of `tla_w3376` (the small cluster below) and where the output goes (drawn as far as a poly entering the right cluster at (4520,4461)) are open. `amr_eq_r3` is believed to be `amr_eq_r3`, the vertical sync width match (a line followed from `amr` on a branch not merged here; not joined). | Firm for the selector's equation; marked for the inverter that makes NOT `rcs_thin_e` (its load tie); the identities are open |
| In the west column of the small cluster below the step logic, a latch of the same build as the two that make `rcs_e4`: `tl1_w6022` = NOT(`tl1_w5978` OR `ck_out` AND NOT `tl1_w3333` OR `tl1_w5841`), `tl1_w5841` = NOT(`tl1_w3333` AND `ck_out` OR `tl1_w6022`). It is open while `ck_out` is high (CLK low), takes `tl1_w3333`, and `tl1_w5978` high clears it (`notes/blocks/tl1.md`). | Marked (all pull-downs and both `ck_out` gates are drawn without `?`; the cross-coupling runs over the two load plates, whose ties are `?`). **Open**: what `tl1_w3333`, `tl1_w5978` are and where `tl1_w6022` goes (east along y 6195) |
| What makes `lc_step`. | Open |
| The memory address counter (14 bits, left array) and what clocks it. | Open (cells traced, control lines not) |

Inside a counter:

| Fact | Mark |
|---|---|
| In `hc` and `hsw` the master latch loads on `ck_b` (CLK high) and the slave on `ck_a` (CLK low). | Marked (the cell contains uncertain items; that these two lines gate the pass devices of exactly these twelve bits is firm) |
| The value the rest of the chip sees (the comparators, the outputs) is the buffered master, not the slave. | Firm for the buffer; marked for the cell behind it |
| Carry ripples up the bits: carry out = carry in AND the bit's slave. `hc` and `rc` also have a look-ahead line over bits 0-3. | Firm per bit; the bit-to-bit link is marked |
| The carry into bit 0 of each counter (what makes it count at all). | Open |
| The next-value function (increment, hold, clear). | **Open**: one pull-up and one branch of the network are not resolved |

**Reset.** Not established for any counter. What is known: in every bit the value on
its way to the master passes a gate `NOR(L3, …)`, so while the counter's line "L3" is
high the master is loaded with 0 (marked). For `rc`, `hsw`, `sl` and `c4l` that line
arrives from outside the counter and its source is open; it is the candidate for a
synchronous clear. For `hc` the same line is believed to be `ck_a` (join not drawn),
which would make it part of the clocking there and not a clear. So even the mechanism
is not settled.

## Registers and writing

| Fact | Mark |
|---|---|
| Each register bit is a transparent latch: it follows the data line while its write strobe is high and holds when it falls. | Extracted; the cell has uncertain items |
| In the latch cell of the right datapath and the address register (`rdp3_lat`, 59 copies) the write pass transistor is 70/28 and the feedback that holds the bit is one weak device (22/82, gate on VSS) from the output back to the storage node, so a write overpowers it about nine to one. | Firm for the pass transistor and the two inverters; the hold device is marked (its strip is an uncertain item, and that it is a depletion device is believed) |
| `wr_r#` = register # selected AND the common strobe (`wr_stb_n` low). | Firm for R0-R11; marked for R12-R15 |
| The common strobe is a latch of "write, chip selected, RS high" that is open while E is high. | Marked (four of its nets are joined only through uncertain items) |
| Whether anything ends the strobe when E falls, or re-times it to CLK. | **Open**. As drawn nothing does; that reading rests on the marked nets above |
| The register rows of R3 (one nibble), R5, R6, R7, R8, R9, R10, R11 are identified by their strobe lines, drawn end to end. | Firm for the joins; the register *numbers* rest on the address decoder's numbering of its lines |
| The rows of R0, R1, R2, R4 are identified by their strobe lines, drawn end to end (`notes/blocks/wrj.md`). | Firm for the joins; the register *numbers* rest on the address decoder's numbering of its lines |
| The data bus: all eight bits are joined from the right datapath across the chip to the central datapath (`notes/blocks/bust.md`); bits 0-3 reach the D0-D3 units of the data bus column (`dbl`). The registers each bit writes match the datasheet's widths exactly (R5, R9 bits 0-4; R4, R6, R7 bits 0-6; R8 bits 0, 1, 4-7; R0-R2 bits 0-7), which nothing in the trace assumed. | Firm for the joins; the bit numbers rest on that match and, for bits 0-3, on the pins D0-D3 being joined to the units that drive `db_b0`..`db_b3` |
| Data bits 0-3 reach the bus through a **transparent latch per bit** in the data bus column: `dl#_q` follows pin D# (through four inverters) while `dbus_le` is high and holds when it falls, and a static inverter drives `db_b#` = NOT `dl#_q_n` all the time. The internal data bus is not tri-stated at this end (`notes/blocks/dbus.md`). The latch is a cross-coupled pair gated by `dbus_le`: `dl#_q` = NOT((`d#_d_n` AND `dbus_le`) OR `dl#_q_n`). | Firm (equations and the joins to `db_b0`..`db_b3`), from the pin itself for D0-D3: the input lines of D2 and D3 are drawn (`notes/blocks/dbus.md`) |
| What `dbus_le` is: one metal through all eight input latches, which runs on south along x 16774 below the latches of bits 4-7 (followed to y 16104, `notes/blocks/dlat.md`); its driver is not traced. | Open |
| Data bits 4-7: the pins D4-D7 have their four-inverter input buffers in the same column (D6's and D7's are another layout of the same chain; the inputs of D4, D5 and D6 are drawn from their pins, D7's is assigned by position). The buffered levels `d4_d`..`d7_d` leave the column west into four more copies of the same transparent latch (mirror image, `notes/blocks/dlat.md`): `dl#_q` = NOT((`d#_d_n` AND `dbus_le`) OR `dl#_q_n`) for # = 4..7, on the same `dbus_le`. Their outputs `dl#_q_n` run west and north to four static inverters above the latches, which drive the bus: `db_b#` = NOT `dl#_q_n` for # = 4..7, joined to the data lines that come down from the right datapath. So all eight internal data bus bits are driven all the time from the pins' input latches; nothing at this end is tri-stated. | Firm for the buffers, the joins of D4, D5 and D6 to their pins, the four latch equations, their joins to `d#_d` and `dbus_le`, and the four inverter equations with their joins to `db_b4`..`db_b7` (D7's pin join is by position, as before) |
| The first inverter of every data input buffer has two pull-downs on the pin: its gate poly's L-shaped arm crosses a second diffusion under a metal (AMB-004 said the arm crosses nothing). The logic is the same; the device is a third wider. | Firm (eight buffers) |
| R8 is the central datapath's row A and R9 its row C; slice = 5 - bit (R8's bit 6 is in slice 3, bit 7 in slice 2). | Firm for the joins (from the data bus) |
| R3's high nibble is the four-slice block `amr` (bits 4-7 from data bits 4-7 on `wr_r3`), so every data bit writes R3, as the datasheet's R3. | Firm for the latch equations and the data joins (`notes/blocks/amr.md`) |
| R10 (central datapath `cdp2` row C, bits 0-6) and R11 (row A, bits 0-4) take their data from the data bus (`notes/blocks/rde.md`). | Firm for bits 5 and 6; marked for bits 0-4 (AMB-019) |
| R12-R15 (start address, cursor), R16/R17 (light pen), the status register. | Open beyond their strobe gates |
| Which nibble of R3 the 4-bit row is: the low one (bits 0-3, horizontal sync width). Its four data lines are the data bus lines of bits 0-3 (`notes/blocks/r3d.md`). | Firm for the joins; the bit numbers of the data lines rest on the register-width match (`notes/blocks/bust.md`) |

## Comparators

All are bit-by-bit equality (XOR per bit, NOR over the bits) unless noted. For the first
seven rows of the table the NOR is firm and each XOR has one uncertain link inside its
cell, so the bit equations are marked. R9's and R10's comparators are marked
throughout.

| Output | Compares | Counter inputs | Where the output goes |
|---|---|---|---|
| `h_eq_r0` | `hc` with R0 (8 bits) | all drawn (bits 0-5 joined by `hcj`; bit 2 rests on one uncertain poly in `bd1`) | to a gate column beside the strobe channel; ends on a buried contact there. **Use: open** |
| `h_eq_r0half` | `hc` bits 0-6 with R0 bits 1-7 (R0 / 2) | as above | towards the same gate column. **Use: open** |
| `h_eq_r1` | `hc` with R1 | as above | into the bottom-centre logic. **Use: open** |
| `h_eq_r2` | `hc` with R2 | as above | runs west of the counters on bus line G (joined, `notes/blocks/ucz.md`). **Use: open** |
| `hsw_eq_r3` | `hsw` with the R3 nibble (4 bits) | drawn | not followed. **Use: open** |
| `amr_eq_r3` | R3 bits 4-7 (the vertical sync width, `amr`) with the 4-bit counter `c4l0`..`c4l3` (drawn through `c4l0`..`cdp1_l4676`; `c4l2`, `c4l3` over two `?P` rows of `bust`) | drawn | leaves through a buried contact at c0 (marked) and runs about 12,000 px west to `tla`'s west column, where it is a data input of the selector `tla_w3417 = NOT(rcs_thin_e·tla_w3376 + tla_w3505·amr_eq_r3)`. Per bit XOR and the NOR marked (`?` items in the cell). **Use: the selector's output, to the right cluster, not followed** |
| `rc_eq_r4`, `rc_eq_r6`, `rc_eq_r7` | the row counter `rc` with R4, R6, R7 | drawn: the seven lines of the upper array are `rc0`..`rc6`, joined on firm geometry (`notes/blocks/ucz.md`) | R6's goes to the strobe channel, R7's leaves west; not followed. **Use: open** |
| `sl_eq_r5` | scan line counter with R5 (5 bits) | drawn | leaves north and runs west on `sl_eq_r5` through the central datapath's channel (`notes/blocks/bust.md`); not followed west of it. **Use: open** |
| R9's (`ra_eq_r9`) | **the row address as it goes to the RA pins** with R9 (5 bits) | the five lines are `ra#_cmp` = NOT `ra#_drv_in`: an inverter per bit on the RA pad driver's input line, loads traced (`notes/blocks/dbus.md`). Firm for bits 0-3; bit 4 marked (one uncertain poly on its input, the open join `ra4_drv_in_u`). The comparator's own cells are marked | drawn to the row counter's step logic: it is the input of the inverter that makes `rcs_mu` (AMB-013, resolved). **Use: the row counter's step request (above)** |
| R10's (central datapath) | the row address one stage earlier with R10 bits 0-4; gives "equal" and "greater" | marked | not followed. **Use: open** |

Not found at all: comparators for R11 (cursor end), R12-R15 against the address
counter.

## The row address (RA0-RA4)

| Fact | Mark |
|---|---|
| The RA pins are not the scan line counter directly. Between them: a selector, a row of five units, then a five-cell stage (`ral`) in front of the pad drivers. | Firm that they are there |
| The `ral` stage is a **latch with a force line**: each cell passes its input onto node a while its strobe (`ral_stb`) is high, holds it through a weak device, and drives the pad driver's input with out = node a OR `cnt_gab` (`ral_n1` = NOR(`ral_a`, `cnt_gab`), out = NOT `ral_n1`; `notes/blocks/ral.md`, AMB-018 resolved). | Firm (all five RA copies; RA4's line marked). Where `ral_stb` comes from, and what `cnt_gab` does in use (AMB-017): open |
| The fourteen MA outputs pass through the same cell, strobed by `ck_out` (high while CLK is low) and forced by `mal_frc_m#`: copy m# drives MA# (`notes/blocks/mal.md`). So every MA output is latched while CLK is high. | Firm (equations, all fourteen copies, and the bit order); what feeds each copy and what drives the force line: open |
| The selector passes scan line bit k to output k, or to output k+1 (a shift up by one bit). The two control lines are opposites: `ras_straight` = NOT `ras_shift`. | Firm for the control; six strip joins inside the selector are uncertain |
| `ras_shift` = R8 bit 0 AND R8 bit 1 (`r8_b0_q`, `r8_b1_q`): the interlace field, set to 3 ("interlace sync and video"). | Marked for the gate (four buried contacts in its NAND); firm that the two inputs are R8's bits 0 and 1 (R8's bit order from the data bus, `notes/blocks/bust.md`) |
| In shift mode output 0 has no counter bit; **R9's bit 0** (`r9_b0_q`) chooses which of two signals drives it (`ras_o0_sel1` = shift AND R9 bit 0, `ras_o0_sel2` = shift AND NOT R9 bit 0). | Firm (equations and the bit's identity, from the data bus) |
| One of those two signals is NOT(row counter bit 0) XOR another signal. | Marked; the other signal is open |
| In shift mode the R9 comparator does not compare R9's bit 0; the comparator's input is switched to another signal. | Firm that it is switched; what it is switched to is marked and its source open |
| Where the field (odd/even) signal is made. | **Open**: expected in the gate column west of the nine-gate island, which is being traced. Marked, from that column (`notes/blocks/tcw.md`, run 2): the input of `tc1_g`'s inverter is one half of a cross-coupled pair gated by `tcw_a` (`fld_a_in` = NOT((`tcw_a` AND `tcw_b`) OR `tcw_o3820`), `tcw_o3820` = NOT(`fld_a_in` OR (`tcw_a` AND `tcw_c`))), a latch; `fld_y_b` = NOT `tcw_c`. What `tcw_a`, `tcw_b` and `tcw_c` are is not traced |

## The data pins (D0-D7) as outputs

| Fact | Mark |
|---|---|
| Each data pin has a push-pull driver whose two gates are made by two NOR gates in the pad cell: `d#_pu` = NOR(`d_hiz`, `d#_out_n`), `d#_pd` = NOR(`d_hiz`, `d#_pu`) (`notes/blocks/dpad.md`). While `d_hiz` is high both gates are low and the pin floats; while it is low the pin is the inverse of `d#_out_n`. | Firm (all sixteen equations) |
| `d_hiz` is one line common to the eight pad cells. | Firm (drawn end to end) |
| `d0_out_n` = NOT `dbus_do0_in`: an inverter at the foot of the data bus column drives D0's line up the whole column on one thin metal. `dbus_do0_in`, the bit read out on D0 in true sense, arrives by a metal that leaves the column west at (16950,16712) and is not followed. D1's line `d1_out_n` is drawn from its pad cell to a poly that leaves the column west at (16950,16344): its driver is not at the column's foot. | Firm (the equation and the join into D0's pad cell) |
| What drives `d_hiz` and the `d#_out_n` lines of D1-D7, and so when the chip drives the bus and with what. | Open |
| The pull-up fingers are ordinary transistors with their drain on VCC (source followers), so a driven high level is below VCC by a threshold. | Firm for the connection; that they are enhancement devices is not visible in the photos |

## Not established at all

So that silence is not read as knowledge:

- How HSYNC, VSYNC, DISPTMG and CUDISP are made from the comparator outputs.
- The end-of-frame sequence (R4, then R5 extra lines, then restart) and the interlace
  odd/even logic.
- Why some registers act as N and others as N-1: no comparator's timing relative to its
  counter is established.
- The R8 skew path, the light pen, the status register, reset from the RES pin (the
  buffered `res_b` line is followed across the chip; what it does at its taps is not).
  Of the skew path only the wires' first stretch is traced: `r8_b5_q` and `r8_b4_q` leave the
  datapath westwards through the top bus field of `tc1` and go on west of x 6750 at
  y 2568-2626, into logic that is not traced yet.
- The memory address counter's control, and the cursor compare.

The list of what is assumed, with the evidence for and against each, is
`notes/ambiguities.md` (AMB-001 to AMB-026). Work still to re-check before anything is
simulated is the "Re-read list" in `notes/work-packages.md` (R1-R30).
