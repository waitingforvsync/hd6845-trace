# bc1: bottom-centre random logic, upper left part (x 7000-9000, y 14050-16300)

Trace: `trace/bc1.txt`. Scratch: `cache/scratch/bc1/`. Coordinates are metal-shot pixels.

## Status

Traced and shipped (extracts clean with `@requires cdp4`: no errors, no open nets;
overlays checked on the clean, stripped and metal shots):

1. **The driver of the row D latch strobe** (left gate group, x 7470-7860,
   y 14950-15600): a 2-input NAND and two identical strong inverters.
   `cdp4_ld6` = `bc1_ld_in1` AND `bc1_ld_in2`; a twin output `bc1_ld_a` (same logic,
   separate inverter) leaves upward at x 7448. The strobe metal is traced all the way
   to `cdp4`'s drawn end.
2. **Column A of the right gate group** (x 7990-8565, y 15070-15990): two inverters and
   three 2-input NANDs that decode two bus lines (`bc1_s0`, `bc1_s1`) into three of the
   four one-of-four lines (active low), plus one inverter with a weak load. All their
   wiring in the channel is traced.
3. **Routing field**: the six data lines of `cdp4` row D as far as they were followed
   (lines 1 and 2 joined to `cdp3_g_c2`, `cdp3_g_c3`).

Not traced: the sources of `bc1_ld_in1` / `bc1_ld_in2` (lower left gate group), the
left column of the left group, the dense column B right of the VCC rail x 8534, the
gates below y 16000 in column A, most of the routing field. See Not done.

## Inventory

Survey views: `cache/scratch/bc1/sv_metal.png`, `sv_acid.png` (whole block, 0.6x).

The block has three parts.

**1. Routing field, y 14050-14900 (whole width).** Not logic.
- Six horizontal poly lines at y 14089, 14132, 14175, 14218, 14261, 14304 (pitch 43),
  the data lines of `cdp4` row D (traced in part; see Logic, "Row D data lines").
- The strobe `cdp4_ld6` and its twin `bc1_ld_a` cross the field in metal (traced; see
  Logic, "Strobe driver").
- Other metal seen at the top left (`s1.png`, `o6.png`), not traced: two wide
  verticals from above at x 7770-7815 and x 7860-7905; the first joins a wide horizontal
  band y 14110-14160 that runs left to a wide vertical x 7575-7622 (which becomes RL2's
  feed, so these are VCC), the second a band y 14200-14250 that runs left to a wide
  vertical x 7662-7710 (which becomes RL3, VSS). A wide vertical x 7488-7537. A thin
  line that arrives from the left along y 14176, goes down at x 7190 to y 14285, right
  to x 7230 and down.
- Supplies: the VSS rail x 8013 of `cdp4` ends in a wide horizontal metal band
  y 14250-14305 running right to x about 8300, where rail R1 goes down (seen at 0.6x and
  2x). The VCC rail x 8228 turns right at y 14170-14240 and feeds a wide vertical
  x 8405-8465 that comes down to y 14930 and widens right into rail R2 (seen at 0.6x and
  2x; the corner at y 14925-14985 is in `t1.png`).
- A bus of 13 horizontal metal lines, y 14354 to 14873 (pitch 43.5: 14354, 14397, 14439,
  14482, 14526, 14570, 14613, 14656, 14699, 14744, 14786, 14832, 14873), x 7780-8280.
  Left ends: contacts in two columns at x about 7790 and 7830 onto horizontal polys
  arriving from the left. Right ends: most lines end on contacts at x 8250-8290 and
  continue (in poly under the rails x 8300-8560, then metal again from x 8560) towards
  x 9000. **The two lowest lines turn down into the channel: y 14832 = `bc1_s0`
  (turns down at x 8186), y 14873 = `bc1_s1` (turns down at x 8143)** (traced, `t1.png`).
- Vertical metals x 7000-7760 crossing the field (bundle continuing from the left bus
  field), not examined.

**2. Right gate group, x 7850-8960, y 14900-16300.**
- Wiring channel x 7860-8250: vertical metal tracks at x 7882, 7924, 7969, 8012, 8056,
  8098, 8143, 8186, 8229 (measured), horizontal polys under them into the gates.
  Tracks 8012-8229 are traced as far as they serve column A. Not traced: track 7969
  (from a contact at (7880,14910) via a horizontal at y 14912, down the whole channel to
  a contact at (7968,16300)); track 8012 below y 15865 (starts at contact (8012,15865)
  on a poly going left along y 15865); tracks 7882 (from contact (7880,15510)) and 7924
  (from contact (7925,15700)).
- Rail R1 = VSS, x 8336-8384. Rail R2 = VCC, x 8510-8558. Rail R3 = VSS, x 8686-8731.
- **Column A** (between R1 and R2), top to bottom: gates 1-6, y 15070-15990 (traced).
  Below, y 16000-16300 and on below the block: a different, wider gate structure under
  R1 (diffusion x 8300-8395, polys at y 16032, 16107, 16125, 16170, 16215) with loads at
  x 8430-8500 (not traced; it continues below y 16300).
- **Column B** (right of R2, x 8560-8900): dense. Loads hang on the right side of R2
  (poly blocks at x 8570-8620: y 14975-15050, 15105-15140, 15450-15520, ...), pull-downs
  under and right of R3, horizontal polys going right to contacts on vertical metals
  x 8790, 8837, 8881, 8925. A thin vertical metal x 8642 runs down the whole column
  between R2 and R3 (it is `bc1_dec00_n`). Only its first gate is understood (see Logic,
  "inverter A, seen not traced").
- Right of x 8900: vertical tracks at x 8925, 8967, ... (boundary with `bc2`), not
  examined.

**3. Left gate group, x 7100-7860, y 14950-16300.**
- Rails (traced where used): RL1 = VSS, x 7296-7345 (comes from a wide vertical
  x 7380-7430 above y 15020; not drawn); RL2 = VCC, x 7470-7520 (top at y 14935, fed
  from the right by a wide horizontal band y 14933-14976); RL3 = VSS, x 7640-7692.
  RL2 is VCC because the loads hang on it; RL1 and RL3 carry the pull-down sources.
- **Right part, upper (x 7520-7860, y 14950-15600): strobe driver (traced)**: two
  strong inverters (`bc1_drv`, y 14978-15163 and 218 lower) and the NAND under RL3
  (y 15400-15600).
- **Left column, upper (x 7200-7520, y 15030-15560)**, between RL1 and RL2, the same
  style as column A (seen in `L2.png`, not traced): an inverter at y 15032-15146 (VSS
  contact (7310,15050), gate poly y 15077-15095 from the left, output buried contact
  7238-7283 x 15109-15146 with a poly going left, load block 7411-7461 x 15085-15146,
  VCC contact (7492,15100)); a 2-input NOR at y 15159-15359 (VSS contacts (7310,15180)
  and (7310,15335), gate polys y 15207-15226 and y 15292-15311 from the left, shared
  output node between them, tall load poly 7395-7435 x 15231-15322, VCC contacts
  (7490,15215), (7500,15255)); a wider structure at y 15400-15560.
- **Lower part (x 7190-7860, y 15570-16300)**: dense, large gates (`LL_a.png`, stripped
  shot at 1.5x). Not traced. `bc1_ld_in1` and the tap of `bc1_ld_in2` enter it as polys
  going left from (7838,15820) and (7880,16252).
- Wiring between the two groups (x 7700-7990): verticals x 7727 (from a contact at
  (7745,15610)), x 7795 (contact (7793,15655) down to contact (7793,15865)), x 7838
  (contact (7838,15915) to contact (7838,16080)), x 7925 (from contact (7925,15700)
  down past y 16300), x 7969; a poly along y 15860 from the contact (8012,15865) left
  past (7793,15865) (`m1.png`).

## Logic

### Strobe driver (traced)

```
bc1_ld_n = NAND(bc1_ld_in1, bc1_ld_in2)      gate under RL3, y 15442-15598
cdp4_ld6 = NOT bc1_ld_n                      inverter cell 2 (y 15196-15381)
bc1_ld_a = NOT bc1_ld_n                      inverter cell 1 (y 14978-15163)
```

So the row D latches of `cdp4` are transparent while `bc1_ld_in1` and `bc1_ld_in2`
are both high, and `bc1_ld_a` is an identical, separately buffered copy.

- **NAND.** VSS contact (7674,15560) on RL3; diffusion column x 7637-7699 crossed by
  band 2 (y 15514-15534, input 2, next to VSS) and band 1 (y 15467-15486, input 1,
  next to the output); output node y 15442-15464. Load: poly block 7523-7567 x
  15404-15483 over the strip y 15441-15481, land contacted by RL2 at (7485,15462), gate
  tie by a buried contact 7580-7610 x 15402-15436 on a bump above the strip. The output
  node runs right to a buried contact 7723-7772 x 15417-15453, poly to a pad, contact
  (7795,15435) to a vertical metal x 7795 (y 15076-15447) that feeds both inverters.
  - input 1: pad and contact (7838,15477), metal x 7838 down to contact (7838,15820),
    poly going left along y 15822 (followed to x 7750).
  - input 2: contact (7880,15522), metal x 7882 down past y 16300; on the way a contact
    (7880,16252) to a poly going left along y 16258.
- **Inverter cell `bc1_drv`** (two copies, 218 apart). One active area under and right
  of RL3 (7546-7758 x 15059-15163 in cell 1) contacted by RL3 at (7663,15131). An
  S-shaped gate poly (pad at (7795,15086) under the metal x 7795; band y 15075-15098
  across the top, down the left side x 7604-7634, band y 15111-15140 along the bottom
  to x 7532) separates the source (the land with the contact and a strip along the
  bottom) from the drain (a strip above the top band, y 15059-15075, plus the block
  7546-7600 x 15052-15111 left of the gate). Extracted W/L about 250/26. Load: a wide
  poly block 7540-7632 x 15006-15050 between the drain block and a VCC diffusion band
  above it (y 14978-15000, joined to a land contacted by RL2 at (7492,15005); in
  cell 2 contacts (7492,15215), (7500,15255)); current flows vertically, W/L about
  54/44. Two buried contacts sit on the drain strip: the left one (7618-7660 x
  15020-15060) ties the load gate, the right one (7717-7771 x 15028-15063) holds a
  poly patch.
  - Cell 1 output: a poly from the left buried contact goes up at x 7648 and left
    along y 14961 (under the RL2 feed) to a contact at (7338,14958); metal x 7338 up to
    y 14803, right to x 7427, up to y 14627, right to x 7448, up through the routing
    field (followed to y 14050; continues). The right buried contact of cell 1 has no
    wire (measured: no poly and no contact between it and the strobe metal).
    The corner of this poly (x 7610-7640, y 14950-14963, in the open between the RL2
    feed and RL3) was checked by a colour grid in both stripped shots: poly-coloured
    all the way, field-coloured just below it.
  - Cell 2 output: poly from the right buried contact to a contact at (7838,15260);
    metal x 7838 up to y 15045, left to x 7795, up to y 14913, left to x 7752, up to
    y 14283, right to x 7947, up into `cdp4` (`cdp4_ld6`). Cell 2 has no poly on its
    left buried contact other than the load gate.

**Believed, not traced:** `bc1_ld_a` goes up the bundle left of `cdp4` to the strobe of
its 8-bit row C latch (`cdp4_ld`), so that rows C and D form one 14-bit register loaded
by one event; `cdp4.md` reports a contact near that strobe line at (7557,12975). The
six data lines of row D arrive on the poly lines y 14089-14304 (below).

### Source of `bc1_ld_in1` (seen at 2.3-2.9x in `n1.png`, `n2.png`; NOT traced)

Recorded so the next agent can start here; none of it is in the trace.

- The poly y 15818-15831 from the pad at (7838,15822) runs left to x about 7735 and ends
  against a narrow outlined strip (7706-7730 x 15790-15855) that continues the
  diffusion under RL3: taken to be a buried contact onto node N1, so `bc1_ld_in1`
  would be the output node N1 of the gate under RL3 at y 15745-15945.
- Under RL3 (diffusion x 7660-7708), top to bottom: VSS contact (7677,15745); poly A
  y 15768-15790; node N1 y 15792-15855; poly B y 15858-15877; node N2 y 15880-15899;
  poly C y 15901-15919; VSS land with contact (7672,15945). Read as
  N1 = NOT(A OR (B AND C)), if N1 has a load (not found yet).
- Poly B is the long poly along y 15860 that carries contacts at (8012,15865) (metal
  x 8012 going down) and (7793,15865) (metal x 7795 up to a contact at (7793,15655));
  it continues left of RL3 to about x 7527. Poly C comes from the contact (7838,15915)
  (metal x 7838 down to a contact at (7838,16080)).
- Poly A (y 15759-15790) runs left from RL3 to about x 7523, the edge of a large VCC
  land under RL2 (7475-7521 x 15723-15852, long contact). Between RL2 and RL3 there are
  poly blocks at 7525-7577 x 15724-15742, 15757-15776, 15800-15814, 15823-15842 and a
  poly pad with a metal contact at (7552,15872). So poly A is probably the output of
  another gate whose load sits there: two gates feeding each other, i.e. a latch. This
  is where the flip-flops of the strobe timing are.

### Row D data lines (traced in part)

Six poly lines at y 14089, 14132, 14175, 14218, 14261, 14304 from x 7000 eastwards.
Line 1 ends on the foot contact of `cdp3_g_c2` at (8075,14084). Line 2 steps up at
x 8118 to y 14087 and ends on the foot contact of `cdp3_g_c3` at (8463,14083). Lines
3-6 (`cdp3_g_c4`..`cdp3_g_c7`) step up in the same nested way (x 8150-8200) and continue
right past x 8500, in order, presumably to `cdp4_in6_s3`..`s6` (not followed). Each
line also has a contact to a vertical metal that arrives from above and ends on it:
(7188,14091), (7230,14131), (7274,14172), (7317,14217), (7361,14260), (7405,14304).
The lines continue left past these contacts to x 7000. Which end drives them is not
known.

### Column A (traced)

Structure of every gate: VSS contact on R1, the diffusion column under the rail crossed
by one or two horizontal gate polys that arrive from the channel, the output node
below them; from the node a diffusion strip runs right through a depletion load (poly
block 8448-8500, strip under it) to a land contacted by R2; the load gate is tied to
the strip by a buried contact on a hook-shaped bump (above the block; below it in
gate 6). The node also runs left to a buried contact (x 8271-8308) into a poly line
that goes to a contact on a channel track.

| Gate | y | Function | Inputs (track) | Output (track) |
|---|---|---|---|---|
| 1 | 15072-15196 | `bc1_s0_n` = NOT `bc1_s0` | s0: x 8186 above y 15089, x 8229 below; contact (8229,15128) | x 8186, y 15160-15617, contact (8186,15172) |
| 2 | 15203-15327 | `bc1_s1_n` = NOT `bc1_s1` | s1: x 8143, contact (8143,15262) | x 8098, y 15291-15739, contact (8098,15303) |
| 3 | 15335-15507 | `bc1_dec00_n` = NAND(`s1_n`, `s0_n`) | contacts (8098,15390), (8186,15433) | x 8056 up to contact (8056,14960) |
| 4 | 15507-15677 | `bc1_dec10_n` = NAND(`s1`, `s0_n`) | contacts (8143,15563), (8186,15605) | contact (8056,15652), metal left to x 8012, up to y 14913, right to contact (8100,14913) |
| 5 | 15676-15855 | `bc1_dec01_n` = NAND(`s1_n`, `s0`) | contacts (8186,15738), (8229,15780) | contact (8186,15823), metal to x 8143, down to y 16170, left to x 8056, down out of the block |
| 6 | 15853-15990 | `bc1_g6_out` = NOT `bc1_g6_in` | x 8143 from below the block, jog at y 16260 to x 8186, contact (8186,15910) | contact (8229,15956), x 8229 down to contact (8229,16107), poly right into the untraced gates below y 16000 |

- In each NAND the input nearer VSS is the first one listed.
- Low when: `dec00_n` s1=0,s0=0; `dec10_n` s1=1,s0=0; `dec01_n` s1=0,s0=1. There is no
  gate for s1=1,s0=1 in this column.
- Loads: gates 1-5 W/L about 26/52; gate 6 about 33/78 (weaker).
- Where the outputs go (traced): `bc1_dec00_n`: poly from (8056,14960) right along
  y 14960, up at x 8255, right along y 14913 under R1 and the R2 feeder to a contact at
  (8642,14910) on the thin vertical metal x 8642 that runs down column B (seen to
  y 16000; its taps not traced). `bc1_dec10_n`: poly from (8100,14913) right, up at
  x 8210, right along y 14870 under R1 to about x 8500, where it continues right
  under or into a horizontal metal line (not resolved, not followed).

**Believed, not traced:** a 2-to-4 decode of a two-bit register field that arrives on
the bus from the left (the widths suggest one of the two-bit fields of R8 or R10, but
the two bus lines have not been followed to a register).

### Inverter A at the top of column B (seen, not traced)

y 14940-15060. VSS contact on R3 at (8715,14965); gate poly y 14988-15009 from a
contact at (8838,14998) on the vertical metal x 8837; output node under R3 (y
15009-15033) runs left to a load at x 8572-8603 against R2 (VCC land 8515-8565 x
15008-15058) and right to a buried contact at 8768-8795 x 15025-15054, from which a poly
leaves right along y 15042 (seen to x 8892). The load's gate tie is a box at 8616-8651
x 14977-15006 that lies under the thin metal x 8642: whether that box is a buried
contact or a metal contact from x 8642 was not settled, so the gate is not in the trace.
The vertical x 8837 has further contacts at about y 15127, 15300, 15455, 15520.

## Ports

| Name | Layer | Where it crosses | Direction | What |
|---|---|---|---|---|
| `cdp4_ld6` | metal | x 7947, y 14050 (drawn up to y 13835, overlapping `cdp4`'s metal) | driven inside | row D latch strobe = in1 AND in2 |
| `bc1_ld_a` | metal | x 7448, y 14050 (continues up) | driven inside | twin of the strobe; believed to go to `cdp4_ld` |
| `bc1_ld_in1` | poly | y 15822, drawn to x 7750 (continues left into the lower left group) | from the lower left group | NAND input next to the output |
| `bc1_ld_in2` | metal | x 7882, y 16300 (continues down); tap poly y 16258 drawn to x 7750 | unknown | NAND input next to VSS |
| `cdp3_g_c2` | poly | y 14089, x 7000; metal x 7189, y 14040 | unknown | row D data line 1 |
| `cdp3_g_c3` | poly | y 14132, x 7000; metal x 7231, y 14040 | unknown | row D data line 2 |
| `cdp3_g_c4`..`cdp3_g_c7` | poly | y 14175, 14218, 14261, 14304 at x 7000; drawn east to x 8040 (continue); metal x 7274, 7317, 7360, 7404 at y 14040 | unknown | row D data lines 3-6 (believed `cdp4_in6_s3`..`s6`) |
| `bc1_s0` | metal | bus line y 14832, drawn from x 8040 (the line continues left to about x 7790) | from outside | decoder input, low bit |
| `bc1_s1` | metal | bus line y 14873, drawn from x 8040 (continues left to about x 7790) | from outside | decoder input, high bit |
| `bc1_dec01_n` | metal | x 8056, y 16300 (continues down) | driven inside | low when s1=0, s0=1 |
| `bc1_dec10_n` | poly | y 14870, drawn to x 8500 (continues right) | driven inside | low when s1=1, s0=0 |
| `bc1_dec00_n` | metal | x 8642, drawn y 14898-15060 (continues down column B) | driven inside | low when s1=0, s0=0 |
| `bc1_g6_in` | metal | x 8143, y 16300 (continues down) | from outside (below) | input of inverter 6 |
| `bc1_g6_out` | poly | y 16107, drawn to x 8300 | driven inside | into the untraced gates at y 16000-16300 |
| `vss` | metal | R1 x 8360 and RL3 x 7666, drawn to y 16300 (continue down); tops not joined to `cdp4`'s rails in the trace | - | rails |
| `vcc` | metal | R2 x 8534 and RL2 x 7495, drawn to y 16300 (continue down); tops not joined | - | rails |

Seen, not drawn: the 13 bus lines at their left ends (x 7790) and right ends.

## Ambiguities

1. **Supply identity of the rails.** R1, R3, RL1, RL3 = VSS and R2, RL2 = VCC are taken
   from the circuits: every depletion load (gate tied to its output node by a buried
   contact) has its other end on a land contacted by R2 or RL2, and every pull-down
   source is contacted by R1, R3, RL1 or RL3. The low-zoom path of the rails up to the
   `cdp4` rails agrees for R1 (to the VSS rail x 8013 through the band y 14250-14305)
   and R2 (to the VCC rail x 8228 through the wide vertical x 8405-8465). None of these
   joints is drawn; the rails are joined by name only.
2. **Load hooks.** The hook between each load block and the strip is drawn as a
   diffusion bump with a buried contact at its end (as in the pilot example). It could
   equally be a poly stem with the buried contact on the strip; the connectivity (load
   gate tied to the output) is the same.
3. **Right end of `bc1_dec10_n`** (poly y 14870 at x about 8500): the poly appears to
   continue right underneath a horizontal metal line that starts at x 8510; a contact
   there was not looked for.
4. **Extent of the active areas of the strobe driver.** Open diffusion and open field
   have nearly the same colour in this part of the die in every shot, so the active
   areas right of RL3 are drawn from their outlines: the rectangle 7700-7758 x
   15098-15163 (and its copy) is taken as part of the source land because one closed
   outline surrounds both; the drain block 7546-7600 x 15052-15111 because it lies
   between the load gate and the bottom band of the gate. If the block were field, the
   inverter would have only the top band as its gate (W about 120 instead of 250) and
   the load would have no drain: so the drawn reading is the only one that gives the
   load a path. For the NAND the column is drawn only as wide as RL3 (x 7637-7699);
   whether it extends right of the rail under the two bands was not settled (width only).
5. **Data lines between x 7430 and x 8040**: followed at 1.6x and 2x only
   (`topL.png`, `top2.png`): straight salmon bands at constant y in the clean shot,
   under seven vertical metals. No contact was seen on them there, but they were not
   examined at high zoom. The four `bc1_d` lines are not joined to their `cdp4` tracks.
6. **`bc1_ld_in2` at the contact (7880,16252)**: the vertical metal x 7882 appears to
   continue below this contact (bright in the metal shot to y 16320, 20 px gap in the
   automatic metal detection at the contact itself). Drawn as one line.

## Not done

In order of value:

- **Sources of `bc1_ld_in1` and `bc1_ld_in2`**: the lower left gate group, x 7190-7860,
  y 15570-16300 (`LL_a.png`). Start from the poly y 15822 going left from (7838,15820)
  and the poly y 16258 going left from (7880,16252). This is the logic that times the
  14-bit latch (rows C and D of `cdp4`).
- Where `bc1_ld_a` goes above y 14050 (x 7448), to confirm it is `cdp4_ld`.
- Left column of the left group, x 7200-7520, y 15030-15560 (inverter, NOR, one more:
  see Inventory) and its inputs from the field on the left (verticals x 7058, 7101,
  7145, 7188 with contacts on polys).
- Column B, x 8560-8900, y 14940-16300 (dense; start with `d1a.png`, `e1.png`,
  `e1b.png`). Open questions there: the boxes under the thin metal x 8642 at 8616-8651 x
  14977-15006 and 8621-8648 x 15157-15193 (buried contacts or taps of `bc1_dec00_n`?);
  the island at 8569-8619 x 15145-15190 with a metal contact at (8590,15170) to a short
  vertical metal x 8592 that ends on a second contact at (8590,15380). The stripped
  chip-2 shot (`--layers acid`) showed poly far more clearly than the clean shot in
  the left group; try it here first.
- Column A below y 16000 (the gates fed by `bc1_g6_out`; contacts at (8290,16030),
  (8229,16171), (8143,16215)).
- Routing field: the 13-line bus (where `bc1_s0`, `bc1_s1` and the other 11 lines come
  from and go), data lines 3-6 east of x 8040, the supply joints.
- Channel tracks x 7924, 7969 and 8012 below y 15865.

## Corrections (coordinator, from the handoffs of 2026-11-19, third batch)

- "Believed, not traced: `bc1_ld_a` goes up the bundle left of `cdp4` to the strobe of its 8-bit row C
  latch (`cdp4_ld`)" and Not done "Where `bc1_ld_a` goes above y 14050": traced (`busl`, piece `ctl`):
  x 7448 north to y 13982, east to x 7556, north over a box to the pad (7556,12983) on `cdp4_ld`'s row.
  Marked (one `?M`; AMB-038).
- "the 13 bus lines at their left ends (x 7790)": the poly rows arriving there are identified for seven
  (`busl`, piece `lc9`): row y 14567 `lc3_e9798`, 14611 `lc2_w9079`, 14654 `lc3_e9756`, 14697 `rst_c`,
  14740 `lc2_w8450`, 14784 `lc3_w9947` (the ripple counter's clock), 14914 `rst_a`; row y 14523 is two
  nets (`rcs_e4` to the pad (7012,14522), another from the pad (7100,14522) east), as R10 says.
- Survey ("Not traced: track 7969 (from a contact at (7880,14910) via a horizontal at y 14912, down the
  whole channel to a contact at (7968,16300))") and Not done ("Channel tracks x 7924, 7969 and 8012 below
  y 15865"): track 7969 is drawn by `eof` (piece `isrc4`) and is `rst_a`; its top contact (7880,14914)
  is on the poly row y 14914 that `busl` brings from the west.
- The six verticals "from above ending on the lines" (x 7189 .. 7404, drawn from y 14040) are
  `cdp3_g_c2` .. `c7`, line g of `cdp3`'s row A cells (`busl`, piece `d6`).
- A seventh track (x 7145 / 7187 / 7231 between y 13680 and 15000, running on to about (7100,16279)) is
  `ck_out` (`busl`, piece `sr`): it lies on line 3 at y 14176 (x 7145-7187) and crosses line 6 at
  (7231,14304) without a contact. Its driver is expected in the group x 7000-7860, y 15000-16300.

## Corrections (coordinator, from the handoffs of 2026-11-20)

- Survey, "Right ends: most lines end on contacts at x 8250-8290 and continue (in poly under the rails x 8300-8560, then metal again from x 8560) towards x 9000": not so for the line y 14786 (`lc3_w9947`): from its pad (8293,14785) the poly goes south 40 px and east along y 14816-14834 under the rails and the VSS band to a turn at x 8968 and a pad (8967,14870), with no metal between (`eof`, piece `ck6`).
- Ports, `bc1_g6_in` "from outside (below)": the metal continues 1,520 px down the bundle and by two pads and a poly row to the output of `eof`'s inverter `inv17` (`eof_w17040` = NOT `eof_w16823`; `notes/blocks/eof.md`, piece `o040`). The join passes three uncertain stretches of a thin metal (an alias, not a rename).
- Column B (x 8508-8940) is drawn by `eof` from y 14942 to 15472 and from y 15886 south; column A's VSS rail (R1) is drawn on south of y 16300 to its end at y 17568.

## Corrections (coordinator, from the handoff of `bl0` run 12, 2026-11-20)

- The six poly lines "line 1 .. line 6" (drawn from x 7000): believed to run on west to pads at about x 5760-5800, where six tracks start that `bl0` (run 12) draws from y 15000 south into the left array's six lower rows (follower only; not read; the stretch is in `busl`'s region).
- A poly row out of the gate group at y 15566 (it runs on east under the rail x 7292-7342) ends west on a pad (7143,15566): it is `h_eq_r1_n` (`bl0` run 12, piece `m7144`), a wire with no transistor that goes south and east to a poly row east of (8360,17821) in `bc3`. A second net lies beside it (pads (7186,15520), (7187,15696)), undrawn.

## Corrections (coordinator, from the handoff of `busl` run 14, 2026-11-21)

- Not done / the correction above ("The six poly lines ... believed to run on west to pads at about x 5760-5800"): drawn (`busl` run 14, piece `a6`): pads at (5757,14092), (5800,14136), (5756,14178), (5800,14223), (5757,14265), (5800,14308), no tap between; from them six nested Ls to `bl0`'s six tracks. The lines are `cdp3_g_c2`..`c7` to the left array's six lower rows.

## Corrections (coordinator, from the handoffs of `busl` run 16, 2026-11-21)

- "The VSS plate at the foot of the s0 rail" / the wide metal over the row y 14870: it is VSS from `cdp4`'s plate (`busl`, piece `vb`) and leaves south at (7383-7432, 15000); RL2's top bar (y 14935-14970, east of x 7468) is separate from it.

## Corrections (coordinator, from the handoffs of `eof` runs 28-35, 2026-11-21)

- Ports, `bc1_dec01_n` "x 8056, y 16300 (continues down)": it continues to the pad (8010,17210) and is gate B of the NOR that makes `eof_w17338` (`trace/eof.txt`, piece `in207`; the neck at y 16613 uncertain, AMB-049). No other load was seen on the stretch south of y 16300.
- Ports, `bc1_g6_out` ("poly, y 16107, drawn to x 8300 ... into the untraced gates at y 16000-16300") and Not done "Column A below y 16000": the gate fed by `bc1_g6_out` is the data input of the latch `lat18` (`trace/eof.txt`), a copy of `tl1`'s latch at y 16015-16447; the poly leaves the pad as the row y 16120-16138, not along y 16107 (geometry only: `trace/bc1.txt`'s `P 8221,16107 x8300` is a stub that joins nothing else; the block's Ambiguity 114 in `eof`).
- The west gate column (rail x 7294-7342): four units are drawn by `eof` (y 15024-15900): `eof_w15128` = NOT `rst_n`; `eof_w15262` = NOR(`lc1_w7780`, `rcs_mv`); `eof_w15523` = NOR(`rcs_e4`, `eof_w16040`, `h_eq_r1_n`); `eof_w15781` = NOR(`eof_w15523`, `eof_w15262`, `eof_w15128`) (each marked by its two ties). The rail's north end turns east at y 15024-15069 onto the VSS metal x 7383-7432 (`busl`, piece `vb`). The box `D 7462,15194:7540,15284` also feeds the load of `eof_w15262` from its west side.

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- Its west gate column (rail x 7294-7342) is drawn by `eof` from y 15024 to y 16930 (eight units: an inverter,
  three NORs, two wide inverters on `eof_w15781`, two select-line inverters); `bc1` draws none of them.

## Corrections (coordinator, from the handoff of `eof` run 69, 2026-11-24)

- `h_eq_r1_n`, gate 3 of the NOR `eof_w15523` in the west gate column, is NOT `h_eq_r1` (`eof` piece
  `ld566`, firm), so `eof_w15523` = `h_eq_r1` AND NOT `rcs_e4` AND NOT `eof_w16040` (marked, as that NOR is).
