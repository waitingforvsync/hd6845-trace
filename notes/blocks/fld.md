# fld: the logic west of the row address selector (x 6380-7120, y 4720-5780)

Serial work, 2026-11-16. Trace: `trace/fld.txt` (two inverters and two XOR cells; the upper group's west part not traced). Views in
`cache/scratch/rax/`: `fld_a.png`, `fld_m.png` (the upper group, clean and metal at 1.65x),
`fldR.png`, `fldM.png`, `fldL.png` (three tiles at 2.7x), `fldA1.png`, `fldA2.png` (chip-2
stripped shot at 3.4x: the clearest), `fldG.png`, `fldB.png`, `fldS.png`, `fldD.png`,
`fldE.png`.

## Why this block matters

The two signals that can become row address bit 0 in interlace sync and video
(`ras_o0_alt1`, `ras_o0_alt2`) and the two that switch the R9 comparator's bit 0
(`tc1_i`, `tc1_g`) all come from here. This is where the field (odd/even) logic is
expected. Most of it is not traced.

## Traced: two inverters at the east end (x 6700-7050, y 5020-5275)

    tc1_g = NOT fld_a_in        tc1_i = NOT fld_b_in

Each: VCC contact box under the rail x 6700-6750, a load (poly block x 6765-6825 over
the band, its tail tied back to the output through a buried contact, `?`), the output
band east as a thin diffusion to a buried contact at x 6975, and one pull-down under the
rail x 6880-6925 with a VSS contact box below the gate. 4 transistors. The rails' supply
assignment is by the layout rule, not followed.

- Upper (output `tc1_g`): the buried contact (6975,5048) is on the poly that goes north to
  the pad (6985,4958); from that pad a metal goes to the pad (7050,4830) and the poly on
  to the island (`trace/ras.txt`), and **a second poly goes west along y 4958 to a pad
  (6660,4958)**, whose metal runs south along x 6660, then on a diagonal, to a pad
  (6752,5428) in the lower gate group. Gate `fld_a_in`: poly from the north along
  x 7020-7048, which comes from a horizontal poly along y 4910 from the west.
- Lower (output `tc1_i`): the buried contact (6982,5178) is on the island's input poly,
  which arrives from the east along y 5178 (`trace/ras.txt`). Gate `fld_b_in`: poly from
  the pad (7030,5215); metal south to a pad (7032,5345); poly west along y 5345 past
  x 6560.

## Traced: two copies of the comparator's XOR cell (x 6580-7030, y 5410-6100)

`tools/findcell.py` on the lower gate group: scores 0.88-0.91 against the five slices of
`cdp1`'s row B (and the comparator slices of the right datapath). The group is a copy of
the cell `cdp1_xor`, and 347 px below it stands a second copy. Both instanced
(`@inst cdp1_xor -2581,1758 tag=fx` and `-2581,2105 tag=fy`); the overlay sits on every
contact, pad, load block and gate of both (`fx_chk_a.png`, `fx_chk_m.png`, `fy_chk_m.png`).
Rails: west VSS x 6575-6625, VCC x 6800-6840, east VSS x 6978-7028 with the contact that
the next slice provides in the comparator rows ((7005,5615) and (7005,5962), rings in the
metal shot). 14 transistors. From the extraction:

    fld_b_in    = cnt_la_a_n XOR tc1_g         (first cell)      tc1_i = NOT fld_b_in
    ras_o0_alt1 = rc0_n XOR fld_y_b       (second cell)

Ports:

| Cell | Input B (metal x 6754, two pads) | Input A (poly x 6919-6942) | Output "ne" |
|---|---|---|---|
| first | `tc1_g`: its metal from the pad (6660,4958) comes down x 6665, a diagonal, x 6753 onto the upper pad (6752,5428) | `cnt_la_a_n`: pad (6925,5718), metal west and south along x 6885 to a pad (6880,6062), poly south along x 6882 | a poly comes down x 6665 from the line along y 5345 (`fld_b_in`, the lower inverter's gate line) onto the cell's output diffusion |
| second | `fld_y_b`: the metal goes on south to y 6085 and west to a pad (6660,6085), poly west | `rc0_n`: the poly goes on south along x 6930 | a poly comes down from the pad (6662,5712) at the end of `ras_o0_alt1`'s metal |

**Assumption (trap 17), both cells**: the buried contact between the poly that arrives
from above and the output diffusion is not resolved in any shot (`?B`). It is placed
where the original cell has its buried contact to the comparator's NOR gate, and in both
copies a poly ends exactly there. `tools/unsure.py` cannot see these two joins (the
cell's output diffusion carries no label of its own).

So, as traced: the line that can become row address bit 0 when R9's bit 0 is set is
the XOR of two signals, and the comparator's bit-0 input for the same case is the XOR of
the upper inverter's output with a third signal. None of `cnt_la_a_n`, `rc0_n`,
`fld_y_b`, `fld_a_in`, `ras_o0_alt2` is traced to its source.

## The XOR cells' A inputs, traced to their sources (2026-11-16; drawn, extracted)

    fld_b_in    = cnt_la_a_n XOR tc1_g           tc1_i = NOT fld_b_in
    ras_o0_alt1 = rc0_n XOR fld_y_b              rc0_n = NOT rc0

**Row address bit 0, in shift mode with R9's bit 0 set, is the XOR of the inverted bit 0
of the character row counter with one more signal** (`fld_y_b`, not traced). That is
the shape interlace sync and video needs when a character row has an odd number of scan
lines: the parity of the lines flips from one row to the next.

Route of both inputs (views `fxs.png`, `fxs2.png`, `ch2lines.png`, `l6714a.png`,
`l6714c.png`, `l6756end.png`, `l6756w.png`, `knot_a.png`, `knot_c.png`, `l6802.png`,
`ch2e.png`, `ch2e_m.png`, `i2.png`, `i2in.png`, `i2end.png`):

1. From the cells the two polys run south (x 6882 and x 6930) to y 6600, south-east on
   parallel diagonals, and east as two lines of the central datapath's channel 2
   (y 6756 and y 6712).
2. **At x 7860-7960 every line of channel 2 steps down one position** (nested bends):
   6714 becomes 6756, 6756 becomes 6802, 6802 becomes 6844. Read at 6.5x in both
   stripped shots; the chip-2 shot shows the two lower bends plainly (orange poly with
   its outlines), the clean shot shows that the line at y 6756 west of the knot does not
   pass under the thin metal x 7910-7935 (pink there) while the one at y 6712 does. The
   first reading at 1.2x took each y for one line, which gave the two inputs the wrong
   sources (the same trap as R10: one y, two nets). East of the knot the top position
   (y 6714) carries other nets: a piece between pads (8165,6700) and (8320,6700), and from
   x 8700 the line of `wl_h0`.
3. East of the knot both lines run through the channel unbroken (strips at 1.2-1.5x) to
   pads at its east end: (11085,6800) and (11020,6755).
4. From (11085,6800) a metal south along x 11088 onto the metal of `cnt_la_a_n`
   (`trace/wl.txt`: the inverter I1's output, NOT `cnt_la_a`). From (11020,6755) a metal
   south along x 11025 to a pad (11022,7432) at the west end of the output poly of the
   inverter I2 of `wl`.
5. I2's input: from the pad (11022,7495) a metal runs south one track east of `wr_r8`
   (same nest, three 44 px steps and the long diagonal), down x 11592 to a pad
   (11585,12460) on the poly that `trace/mra.txt` draws from x 11690 as `rc0`. So I2's
   nets are `rc0` and `rc0_n` (renamed from the place names they had).

The extraction made exactly three joins (2,029 to 2,026 nets); `tools/unsure.py` finds
no `?` item on any of them.

**`cnt_la_a` is the open end.** It is the top piece of the metal x 12285 through the
counter rows (re-read item R8: no contact found on it). That piece runs from y 7110 to
y 12885, which is the bottom edge of row r10, the row of `rc0`; in the same row the cell's
node `rc0_q_n` lies under it. If its source is in that row (the slave side of bit 0),
the two XOR cells take the two phases of the same counter bit. Not established: a 2.6x
look at the row in three shots (`la_r10.png`) does not show a pad on the metal.

## Followed, not drawn

- `ras_o0_alt2`: from its pad (6922,4787) a poly west along y 4787 to a pad at about
  (6455,4787).
- The upper group's west part (x 6380-6700, y 5000-5290): two more VCC contact boxes
  (6540,5095), (6540,5255) with a poly foot beside each (from a pad (6447,5045) with a
  metal from the north, and from the south along x 6435), a buried contact box at
  (6495,5180) between them, polys under the thin metals x 6400 and x 6660.
- `cnt_la_a_n` south of (6882,6220), `rc0_n` south of (6930,6220), `fld_y_b` west of
  (6560,6085), `fld_b_in`'s line west of (6560,5345), `fld_a_in`'s line (y 4910) west.

## Read on the way, not drawn (2026-11-16)

Views `yb1.png`, `yb2.png`, `yb3.png`, `rf.png`, `rfR_c.png`, `rfW_c.png`, `four_a.png`,
`pad4478.png`.

- `fld_y_b`: from the pad (6660,6085) a poly west to x 6558, north to a pad (6535,5848);
  metal north along x 6536 to y 5482, west, north along x 6404 to y 4869 (follower); its
  top end at about (6405,4870) not looked at.
- `tc1_x1` (= NOT `ras_o0_sel1`, `notes/blocks/shm.md`) arrives in the routing field as
  the poly x 7015 from the north, turns west at y 4865 and ends on a pad (6490,4893);
  metal from there to the pad (6447,5045) with a poly foot beside the VCC box
  (6540,5095): an input of the untraced west part of the upper group.
- `fld_a_in`'s line (y 4910) continues west past x 6600 (a small jog to y 4935) to a pad
  at about (6300,4930). **It is not `tc1_x1`**: the two lines run 45 px apart for
  400 px. (If they were one net the island's second AND term would be dead; that
  absurdity was the reason to look twice before joining them.)
- So the upper group's west part (x 6380-6700, y 5000-5290: two loads, a buried-contact
  box between them, gates under the thin metals) takes at least `tc1_x1` and makes
  something on the way to `fld_a_in`, `fld_y_b` or `ras_o0_alt2`. It is the next thing
  to trace here.

## The upper group's west part: first reading, not drawn (2026-11-16)

Views `fw1.png`, `fw2.png` (chip-2 stripped shot at 4x), `nor_cm.png` (class map with
`--open`), `nor_c.png`. **A reading from one class map and two views; nothing of it is in
the trace.**

- The wide rail x 6520-6580 has two diffusion boxes with contact pits under it,
  (6548,5097) and (6548,5257). By the alternation of the rails here (x 6725 carries the
  inverters' loads, x 6902 their pull-downs) this rail is VSS and the boxes are sources.
- West of the rail, between the boxes, two poly blobs (6480-6505, 5120-5140) and
  (6480-6505, 5210-5230) lie on what the class map gives as open diffusion running
  north-south at x 6480-6520; between them a small box (6480-6520, 5160-5195).
  Reading: two pull-downs with a common output node between them: a 2-input NOR.
- Its inputs: the upper blob is the foot of the poly from the pad (6447,5045), which is
  `tc1_x1`; the lower blob is the foot of a poly that comes up x 6425-6445 from the
  south (below y 5290, not followed; the gate line of the lower inverter, `fld_b_in`,
  passes there along y 5345).
- Its output: a poly along y 5172-5188 leaves the box both ways: east under the rail to a
  block (6648-6680, 5172-5195) that the class map gives as poly over a channel (the load,
  under the thin metal x 6660, towards the VCC box at x 6705-6755), and west along
  y 5175 past x 6400 (a poly along y 5170 is seen further west turning north at x 6260
  and west along y 5040).

If that reading holds the block makes NOR(`tc1_x1`, something) and sends it west, away
from the selector: it would not be the source of `fld_a_in`, `fld_y_b` or `ras_o0_alt2`
after all. Those three then come from further west or north (pads at x 6300-6500,
y 4780-4930), where the field of vertical polys x 6050-6400 passes.

## `fld_a_in` and `fld_y_b` traced to a gate group west of the island (2026-11-16; drawn, partial)

Views `w1a.png`, `w2m.png`, `w2a.png`, `w3c.png`, `w3a.png`, `w3m.png`, `w4.png`, `w5cm.png`
(class map), `jog.png`, `eq10.png`; overlay check `tcw_chk.png`.

Both lines go north-west to one gate group at x 6380-6700, y 3880-4220, down two of the
vertical polys that cross the six bus metals at y 4470-4745:

- `fld_a_in`: inverter gate, north along x 7034, west along y 4915, a jog to y 4937 under
  the rail x 6520-6585 (checked at 4.4x, `jog.png`), west to x 6320, north to a pad
  (6316,4437); metal north, west along y 4182, north along x 6276 to a pad (6272,3957);
  poly east along y 3957.
- `fld_y_b`: pad (6660,6085), poly west and north along x 6558 to a pad (6535,5848);
  metal north along x 6536, west along y 5482, north along x 6404 to a pad (6400,4870);
  poly north along x 6405 to a pad (6405,4437); metal north to a pad (6400,4180).

The gate group, as far as drawn: under the rail x 6505-6560 one diffusion column with
three gates (class map: poly over channel at y 3986-4004, 4031-4052, 4126-4143, diffusion
between; two contact pits to the rail at y 4078 and 4100). From the extraction:

    fld_a_in : pulled to the rail through two gates in series, tcw_a AND tcw_b
    fld_y_b  : pulled to the rail through one gate, tcw_c

With loads (traced by `tcw`, run 2, 2026-11-17, in `trace/tcw.txt`; `fld_a_in` has a third pull-down there, gate `tcw_o3820`) and the rail being VSS: `fld_a_in` = NAND(`tcw_a`, `tcw_b`),
`fld_y_b` = NOT `tcw_c`. The three inputs arrive on pads with thin metals from the
north: `tcw_a` pad (6400,4005), metal x 6403 to y 3786, and a poly on west along y 4000;
`tcw_b` pad (6455,4045), metal x 6465 (not followed); `tcw_c` pad (6318,4135), metal
x 6319 to y 3740, and a poly on west along y 4130. They end in the next rows of the same
untraced region (x 6200-6700, y 3600-3800).

**AMB-014** (assumptions): the rail is VSS; both nodes have loads (candidates east of the
rail); the buried contacts that tie `fld_a_in`'s poly to the node above the series pair
and `fld_y_b`'s pad poly to the node below the third gate; the node above the series
pair is cut off from the rail contact at y 3905 (a strip of field at y 3948-3956 in the
class map); a 12 px dark spot on the rail at (6548,4188) is not a contact.

So the chain for the comparator's bit-0 input in interlace sync and video now reads, as
extracted: `tc1_g` = NOT `fld_a_in`; `fld_a_in` pulled low by `tcw_a` AND `tcw_b`; and for
row address bit 0 (R9 bit 0 set): `ras_o0_alt1` = `rc0_n` XOR `fld_y_b`, `fld_y_b` pulled
low by `tcw_c`. **`tcw_a`, `tcw_b`, `tcw_c` are the open ends**, and the whole region
west of the island (x 6200-6700, y 2500-4450) is untraced logic: it has to be taken as a
block, not chased line by line.

## Not done

Everything under "Followed, not drawn"; the routing field y 4720-4990 (seven horizontal
polys with pads at both ends).

## Note from `tc1` (coordinator, from the 2026-11-17 handoffs)

The thin metal that arrives from the north along x 6621 and ends at about (6622,5006) is
`tc1_p4308`, the input of the inverter `tc1_o4280` (`notes/blocks/tc1.md`). What it lands on in
this block's upper group is the source of that input.
