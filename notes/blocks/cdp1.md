# cdp1: central datapath, top rows (x 7600-10850, y 2950-5700)

**Slice tags and array columns.** This block's slices are tagged by position, `s0`..`s5`
left to right (cells `a0`..`a5`, `b1`..`b5`, `c1`..`c5`). The array's column cN has its
wide VSS rail starting at x = 7605 + 390.3 N; here the rails start at x 8377, 8770, 9161,
9551, 9941, 10331. So **s0 = c2, s1 = c3, s2 = c4, s3 = c5, s4 = c6, s5 = c7.** Row A
occupies c2..c7; rows B, C, D and E occupy c3..c7. Columns c0 and c1 do not exist in
this block (x 7600-8340 is random logic and belongs to tc1 / tc2).

## Status

Traced, placed in every slice, extracting (107 transistors, no errors, no open nets):
rows A and C (static register cell, 6 and 5 bits), row B (five XORs and the NOR that
makes the equality line), the wiring of channel B/C, the two poly lines under row A,
all bit lines down to y 5150, the fourteen bus lines of the big channel, and
`ra_eq_r9` to the block's edge. Second run (2026-11-15) added everything from row B's
XOR on. Not traced: rows D and E (surveyed, one median pair of views), the logic in
the slice-0 position below row A (x 8340-8750 and a little of slice 1 at y 4740-4870),
and where the two write lines go after they leave the block (both leave east and turn
south outside it).

## Inventory

In this region the array has six slice positions at a pitch of 390 px, left edges at
x 8380, 8770, 9160, 9550, 9940, 10330 (the wide VSS rail of each slice). Only row A
uses s0.

| Row | y | Slices | What | State |
|---|---|---|---|---|
| top wiring | 2950-3040 | - | VSS band and feeds, the q outputs of row A leaving upward | traced (to y 2950) |
| A | 3040-3330 | s0-s5 (6) | register cell `cdp1_reg` | traced |
| below A | 3330-3420 | all | two horizontal poly lines y 3340-3362 and 3385-3408, full width, one contact each at the right end | traced |
| B upper | 3440-3650 | s1-s5 | 5-input NOR `ra_eq_r9` | traced |
| B lower | 3650-3990 | s1-s5 | XOR cell `cdp1_xor` | traced |
| channel B/C | 3990-4230 | all | five poly lines from the east (the compare value), plus the poly that feeds a3's bit line from the west | traced |
| C | 4232-4524 | s1-s5 (5) | `cdp1_reg` again (dy = 1194) | traced |
| big channel | 4530-5150 | all | fourteen horizontal poly lines; bit lines cross in metal, one contact each | traced (lines and contacts; not the logic at x 8380-9080, y 4740-4870) |
| D | 5150-5390 | s1-s5 (5) | part of one cell with row E, see Not done | not traced |
| E | 5390-5700 | s1-s5 (5) | | not traced |

Per slice, vertical metal: VSS rail (about 48 wide, left edge of the slice), bit line
(16 wide, 62 px right of the rail centre), VCC rail (50 wide, 214 px right of the VSS
rail centre). Slice s5 has one more VSS rail on its right at x 10711-10765. East of it
two thin metal lines run north-south at x 10808 and x 10850 (see Ports).

Left of x 8750 below row A (the slice-0 position) there is random logic: two small
gates at y 4020-4100 and y 4190-4270 (x 8480-8650: VCC contacts at 8620,4060 and
8620,4230, pull-downs under the slice-0 VSS rail x 8395-8440), more at y 4740-4870
(x 8380-9080, including a diffusion strip with contacts at 8705,4808 and 8930,4800 and a
metal going down at x 8943 to a contact at 8940,5120) and at y 5150-5700. Not traced.

## Logic

### `cdp1_reg`: static register bit (traced; rows A and C)

Master: row A, slice 1, x 8745-9225, y 3040-3330. Six transistors:

| | Gate | Between | W/L | What |
|---|---|---|---|---|
| pass | row write line `wr` | bit line `bl` and `x` | 36/23 | write (and the only access to the cell) |
| pull-down 1 | `x` | `q1` and VSS | 55/27 | |
| load 1 | `q1` | VCC and `q1` | 27/58 | depletion load |
| pull-down 2 | `q1` | `q` and VSS | 61/23 | shares the next slice's VSS diffusion |
| load 2 | `q` | VCC and `q` | 30/70 | depletion load |
| feedback | **VSS** | `q` and `x` | 25/82 | long, narrow, gate grounded |

    q1 = NOT x          q = NOT q1 = x
    x  = bl while wr is high; otherwise held from q through the feedback transistor

The feedback device has its gate tied to VSS through a poly line that does nothing
else, so it must be a depletion transistor used as a resistor (an enhancement device
there would never conduct and the poly line would be pointless). *Believed, not
visible*: the implant cannot be seen. With it the cell is a static latch that the bit
line overpowers when `wr` is high.

`q` (true data, same sense as the bit line when written) is the only output: it leaves
the top of the cell in poly (`pt`). `q1` is used only inside the cell.

How the nodes are made (so the next reader can check): `x` is one poly piece (gate of
pull-down 1, an arm to a buried contact at 8898-8928 x 3097-3130 on the feedback
diffusion, and a tail to a buried contact at 8836-8872 x 3202-3230 on a small diffusion
island that is the pass transistor's upper side). `q1` is the diffusion right of the
gate (8868-8894 x 3133-3188), a narrow band along y 3152-3170 to the top of the load
strip at 8958-8985, a buried contact at 8896-8932 x 3174-3204 to the load's gate, and
that gate's poly running right along y 3150-3176 to the gate of pull-down 2
(9130-9153). `q` is the diffusion under m5's upper contact, m5, the big poly block
9028-9098 x 3185-3285 (load 2's gate), its buried contact at 9082-9112 x 3190-3224 and
the diffusion under m6 at 9104-9130.

### Row A (traced): 6-bit register, **believed R8** (interlace 2 bits, DISPTMG skew 2 bits, cursor skew 2 bits)

- Six cells `a0`..`a5`. Each `q` leaves upward on its own wire to the logic above and
  left of the array, not to a comparator.
- Bit lines (traced, see "Bit lines and the big channel"): a1, a4 and a5 share their bit
  line with row C's cell in the same slice; a0, a2 and a3 have bit lines of their own.
  That is what a register using data bits 0, 1, 4, 5, 6, 7 beside one using bits 0-4
  would look like (three shared, three not), which is R8's pattern; with the width of six
  it is the reason for the R8 belief. Not proven: the bus lines are not followed to the
  data pads, and the write line is not followed to a strobe.
- `wr_r8`: one poly line that meanders through the cells; its west end is the leg
  of cell a0 (8395-8445 x 3250-3322, nothing connected there); east of the block it
  ends on a contact at (10890,3308) to a metal line that runs south at x 10894 and
  shifts to x 10937 at y 4420-4440 (seen and scanned; outside the block).

### Row C (traced): 5-bit register, function not known (a 5-bit register compared for equality)

- Five cells `c1`..`c5`. `q` of c1..c4 goes up in metal from a poly pad at the top of the
  cell (9113+k*390, 4222) to the pad at the foot of row B (9113+k*390, 3958): the A input
  of that slice's XOR. c5's `q` goes up at x 10634 past row B to the lower poly line under
  row A and west out of the block (to tc1's island, which returns the bit for slice 5's
  XOR: see row B).
- `wr_r9`: the same kind of meander, y 4494-4516. West end: the leg of cell c1 under
  slice 1's VSS rail (x 8780), nothing connected. East of the block it ends on a contact
  at (10893,4505) to a metal line going south at x 10894 (below where row A's line has
  left that track).

### Row B upper half (traced): `ra_eq_r9 = NOR(cdp1_b1_ne .. cdp1_b5_ne)`

- The output is a diffusion line along the row, closed at both ends (x 8778 and
  x 10765). One pull-down per slice (W/L 164/23; slice 1: 124/23), one depletion load
  in slice 1 (65/35, VCC contact 9012,3605, gate tied to the line by the buried contact
  at 9070-9112 x 3505-3546).
- It leaves through a buried contact in slice 1 (8928-8962 x 3476-3510) into a poly
  line y 3424-3450 going left under slice 1's VSS rail to a pad at 8725,3437, and from
  there in metal downward (x 8727): see "`ra_eq_r9` (traced to the edge)".
- `cdp1_bN_ne` (N = 1..5) are the gates of the pull-downs; each comes up from the XOR
  of its slice through a buried contact at 9234-9266 x 3652-3682 (+390 per slice;
  slice 1: 8844-8876).
- `eq` = 1 exactly when no slice's `ne` is high: row C's value equals the compare value
  (with the fifth bit as modified by tc1's island).

### Row B lower half (traced): `cdp1_bK_ne = A XOR B`, cell `cdp1_xor`

Master slice 2 (x 9150-9560, y 3650-3990), placed five times. Seven transistors:

| | Gate | Between | W/L | Where (slice 2) |
|---|---|---|---|---|
| load of `n2` | `n2` | VCC and `n2` | 27/54 | strip x 9400-9427 under the block 9377-9452 x 3792-3846 (half under the VCC rail) |
| pull-down | A | `n2` and VSS | 37/23 | 9500-9523 x 3863-3900, VSS = the next slice's land |
| pull-down | B | `n2` and VSS | 50/27 | blob 9259-9328 x 3853-3880 over the column x 9268-9318 |
| load of `ne` | `ne` | VCC and `ne` | 23/49 | block 9272-9321 x 3727-3776 over the band y 3742-3765 |
| pull-down | `n2` | `ne` and VSS | 39/25 | west end of the n2 poly (y 3798-3823) over x 9204-9243 |
| series pair | B (upper), A (lower) | `ne` - mid - VSS | 69/22 each | x 9476-9498 and x 9521-9543 over the diffusion y 3699-3768 |

    n2 = NOR(A, B)        ne = NOT(n2 + A.B) = A XOR B       (extracted, all five slices)

- **A** is the poly that comes up from the pad at the foot of the slice (9503,3958): row C's
  `q` in slices 1-4, in the same sense as the bit written into the register. **B** is the
  thin metal line x 9325-9345 that comes up from channel B/C, with two poly taps
  (9336,3672 and 9336,3858). Neither input is inverted and the gate is symmetric, so
  `ra_eq_r9` = 1 exactly when the five A bits equal the five B bits.
- **Slice 5 is wired differently** (traced): its pad at the foot (10677,3958) is not fed
  from row C below but by a metal line x 10669-10689 going *up* through the cell to a
  contact (10680,3354) on the upper of the two poly lines under row A's foot
  (`cdp1_b5_a`, y 3340-3362); row C's fifth bit `r9_b0_q` goes up on the next metal line
  (x 10634, no contact in row B) to a contact (10634,3396) on the lower poly line
  (y 3385-3408). Both poly lines run left under the whole array, with no other contact
  between x 8340 and their pads (colour test along both lines), and leave the block at
  x 8340. So the comparator's fifth bit is `B5 XOR cdp1_b5_a`, where `cdp1_b5_a` is made
  from `r9_b0_q` (and whatever else) in the logic left of the array. Believed: this
  is where a mode bit modifies the comparison; the left logic must be traced to say how.
- How the nodes are made. `ne`: one diffusion: under `cdp1_nor`'s buried contact
  (9240-9265 x 3650-3675), down the left side x 9204-9243 to the n2 gate, a band right
  along y 3742-3765 through the load gate to the VCC land (9367-9427 x 3738-3786,
  contact 9398,3758), and a band right along y 3678-3712 (narrowing to y 3699-3712 at
  x 9318, passing under the B line and the VCC rail) to the series pair. The load's gate
  is tied to `ne` by a buried contact at the west end of its tab (9220-9248 x 3703-3737).
  `n2`: the load strip from the VCC land down to a band along the bottom (y 3885-3899 in
  the middle, y 3863-3900 at its east end), which ends in the A pull-down on the east
  and the B pull-down on the west; the load gate block is tied to it through the box at
  9452-9480 x 3822-3852 and a neck (9457-9472) down to the band; the same poly runs
  west along y 3798-3823 to gate `ne`'s pull-down.
- VSS: each slice has a land under its rail (9166-9243 x 3830-3900, contact 9183,3865),
  with a tab east under the bit line (y 3830-3848, source of the B pull-down), a west arm
  (y 3864-3900, source of the previous slice's A pull-down) and, from slice 2 on, a strip
  up under the rail (x 9158-9180, y 3702-3836, source of the previous slice's series
  pair). Slice 1's rail has no strip (pink field, seen). Slice 5's pair and A pull-down
  end on a wider strip and land under the extra rail at x 10716-10773.
- The bit line of row A runs over `ne`'s buried contact without touching it (no contact
  colour: 172/139/115 against 160/165/93 on the known contacts; the bright spot in the
  metal shots there is the metal riding over the box).

What rests on what (colour profiles are of the median of slices 2-4, `tools/cdp1_px.py`):

| Junction | Evidence |
|---|---|
| series pair, not two parallel pull-downs | the middle region between the gates is closed top (y 3697) and bottom (y 3768) by lines that cross both gates; no contact, nothing else reaches it (6x view of all four shots) |
| pair's east end is VSS | diffusion colour under the next rail (197/174/129 against field 185/116/122) continuous to the land with the rail contact |
| band y 3699-3712 passes under the B line and the VCC rail | diffusion colour between dark lines at y 3696 and 3714 under both |
| A pull-down of n2 | the band's top edge (y 3862) and bottom edge (y 3900) cross the A poly; poly brighter between them in all four shots |
| n2 load | poly-over-channel colour (239/170/125) under the block for x 9400-9423, plain poly (210/155/115) left of x 9399; diffusion colour below the block down to y 3897 |
| B pull-down of n2 | the bottom band reaches under the B line (diffusion colour y 3887-3897) to the column; the VSS tab reaches under the bit line (diffusion colour y 3834-3846). The column itself is in the open, where field and diffusion have the same colour: its sides are taken from outlines only |
| n2 poly ends past ne's diffusion | poly to x 9194, diffusion edge x 9202, field colour between it and the VSS strip |
| ne load gate tied to ne | tan box with heavy outline at the tab's west end, under the bit line |
| band y 3678-3712 joined to the diffusion under the buried contact | **inferred**, see Ambiguities 8 |

### Channel B/C, y 3990-4200 (traced)

Five horizontal poly lines, each 14-16 px wide, at y 4003, 4046, 4089, 4132, 4176. Each
one **starts at a pad under the B line of one slice and runs east out of the block**
(x 10850; scanned unbroken and without another contact to x 10900):

| Line y | Starts at (pad, contact) | Feeds |
|---|---|---|
| 4176 | 8928-8962, contact 8946,4180 | `ra4_cmp`, B input of slice 1 |
| 4132 | 9316-9352, contact 9336,4138 | `ra3_cmp` |
| 4089 | 9706-9742, contact 9724,4092 | `ra2_cmp` |
| 4046 | 10098-10132, contact 10116,4049 | `ra1_cmp` |
| 4003 | 10488-10522, contact 10506,4006 | `ra0_cmp` |

So the five-bit value that row C is compared with comes from the **east**, one bit per
line, the top line going to the rightmost slice. What drives them is outside the block.

A sixth poly net lies in the same channel and is **not** one of those: the bit line of
row A's slice 3 (`db_b6`) ends on a pad at 9620-9656 x 4078-4106 (contact
9637,4092); from there poly runs west along y 4090, down a hook at x 9243-9260, west
along y 4132, down at x 8656-8672 (in the open gap east of slice 0's VCC rail) and west
along y 4372 out of the block at x 8340. It is in line with two of the five lines but
separate from them: field under metal between x 9265 and 9315 on y 4132 (colour map),
open field between x 9656 and 9705 on y 4090.

### `ra_eq_r9` (traced to the edge)

From the pad at 8725,3437 the metal runs down x 8716-8738 past row B and channel B/C
with no contact (colour scan y 3440-4470), steps west at y 4460 to a contact at
8683,4460, and a poly line (y 4452-4466) runs west under slice 0's rails. It crosses
no diffusion between x 8340 and the pad and leaves the block at x 8340; a colour scan
shows it unbroken to x 7900 at least.

### The two poly lines under row A's foot (traced)

y 3340-3362 (`cdp1_b5_a`) and y 3385-3408 (`r9_b0_q`), from their pads at x 10660-10694
and 10612-10652 west under every rail and bit line (no contact: colour test at every
crossing) to x 8285, where they meet the two polys that `trace/tc1.txt` draws to
x 8290: **`cdp1_b5_a` is tc1's `tc1_f` and `r9_b0_q` is tc1's `tc1_a`**. tc1's island
gives (its notes): `f = a.NOT b + b.NOT a.NOT g + a.b.NOT i`. So the fifth comparator bit
sees row C's fifth bit itself when `ras_shift` is low, and a modified bit when it is high.

### Bit lines and the big channel, y 4530-5150 (traced)

The bit lines are the per-column vertical metal lines at x 8857 + 390 k (16 wide). The
same lines run on down past y 5700, where cdp2 calls them `cdp2_a_sK_bus`. In the big
channel each one has exactly one contact, to a horizontal poly line that starts there
and runs **east** out of the block:

| Bit line | Serves | Route | Contact | Track at the east edge (x 10850) |
|---|---|---|---|---|
| `db_b5` | a0 | x 8466 under the cell, diagonal step at y 3350-3382, down x 8509 | 8509,4940 | y 4981 |
| `db_b4` | a1 and c1 | x 8857 straight | 8857,4893 | y 4937 |
| `db_b3` | c2 | x 9247, starts at the top of cell c2 | 9247,4852 | y 4893 |
| `db_b7` | a2 | x 9247, jog right at y 4047, down x 9290 over cell c2 without a contact | 9290,5070 | y 5110 |
| `db_b2` | c3 | x 9637, starts at the top of cell c3 | 9636,4850 | y 4850 |
| `db_b6` | a3 | x 9637 down to channel B/C, then poly west (see channel B/C) | 9637,4092 | leaves **west** at 8340,4372 |
| `db_b1` | a4 and c4 | x 10027 straight | 10027,4809 | y 4806 |
| `db_b0` | a5 and c5 | x 10417 straight | 10417,4765 | y 4764 |

Fourteen poly lines, 11-12 px wide on a 43.5 px pitch (which lines pass under each rail
and each bit line was measured with `tools/cdp1_under.py`; contacts by colour test along
every vertical line):

- y 4544, 4588, 4632, 4676, 4719 (`c4l0` ..): cross the whole block from x 8340 to
  x 10850 with no contact in it. Not identified.
- The six that exist at x 9412-9580 step down one track there (diagonals, 2.6x view):
  west of the step they lie at y 4850 (c2), 4893 (c1), 4937 (a0), 4981, 5024, 5068 (a2),
  east of it at 4893 .. 5110. Three more start east of the step, at c3's, c4's and c5's
  contacts. So at the east edge the order from the top is c5, c4, c3, c2, c1, a0,
  `cdp1_lw1`, `db_b6`, a2.
- `cdp1_lw1` (west y 4981, east y 5024) and `db_b6` (west y 5024, east y 5068) cross the
  whole block, west edge to east edge, with no contact in it.
- The a0 line (track y 4937 west of the step) has a second contact at (8727,4937): a
  metal line goes down from it at x 8727 into rows D and E's slice-0 position (drawn
  to y 5150, not followed further).

Believed, not traced: these are the internal data bus, c5..c1 = five adjacent data bits
in order and a0, a3, a2 the other three (a3 reaching its bus line west of the block,
perhaps as `cdp1_lw1` or `db_b6`). Which end is bit 0 is not established here: the lines
have to be followed east.

## Ports

| Name | Layer | Where it crosses | Dir | What |
|---|---|---|---|---|
| `vss` | M | feeds at 9140-9197, 9900-9987, 10711-10765 x y 2950 (from the plane under the VSS pad); band continues left at 8340, y 2987-3037 | in | supply |
| `vss` | M | rails x 8796, 9187, 9577, 9967, 10357, 10738 at y 4530 (drawn to there; they continue down). Slice 0's rail (x 8403) is drawn only to y 3440: below that it widens and continues at x 8395-8440 through the slice-0 logic | - | |
| `vcc` | M | rails x 9010, 9400, 9790, 10180, 10570 at y 4530 (drawn to there; they continue down; top end is in row A). Slice 0's (x 8620) drawn to y 3530 only | in | supply, from below. VCC is identified by the loads hanging from it, not by following it to the pad |
| `r8_b5_q` | P | 8340,3024 going left | out | row A bit, slice 0 |
| `r8_b4_q` | P | 8340,2985 going left | out | row A bit, slice 1 |
| `r8_b7_q` | M | 9507,2950 (turns left at y 2940 just above) | out | row A bit, slice 2 |
| `r8_b6_q` | P | 9872,2950 (pad with metal contact at 9865,2940 just above) | out | row A bit, slice 3 |
| `r8_b1_q` | M | 10275,2950 going up | out | row A bit, slice 4 |
| `r8_b0_q` | P | 10665,2950 (pad with metal contact at 10655,2940 just above) | out | row A bit, slice 5 |
| `wr_r8` | P | 10850,3311 going east; contact (10890,3308) to metal south at x 10894, shifting to x 10937 at y 4420-4440; that line is at x 10937 at y 5700 | in | row A write line. Not followed to its strobe |
| `wr_r9` | P | 10850,4505 going east; contact (10893,4505) to metal south at x 10894; at x 10894 at y 5700 | in | row C write line. Not followed to its strobe |
| `cdp1_b5_a` | P | 8285,3351 (drawn to there to meet `trace/tc1.txt`) | in | = `tc1_f`. A input of slice 5's XOR |
| `r9_b0_q` | P | 8285,3396 (likewise) | out | = `tc1_a`. Row C's fifth bit |
| `cdp1_bK_b` (K = 1..5) | P | 10850, y 4176, 4132, 4089, 4046, 4003 | in | the compare value, one bit per line; K = 5 is the top line |
| `db_b6` | P | 8340,4372 going west | in/out | bit line of a3 |
| `ra_eq_r9` | P | 8340,4459 going west (unbroken to x 7900 by colour scan) | out | 1 when row C equals the compare value |
| `c4l0`, `_l4588`, `_l4632`, `_l4676`, `_l4719` | P | 8340 and 10850 at those y | - | pass through |
| `db_b0`, `_c4_bl`, `_c3_bl`, `_c2_bl`, `_c1_bl`, `_a0_bl` | P | 10850, y 4764, 4806, 4850, 4893, 4937, 4981 | in/out | bus lines of the bit lines (c1, c4, c5 also serve a1, a4, a5) |
| `cdp1_lw1`, `db_b6` | P | 8340, y 4981 and 5024; 10850, y 5024 and 5068 | - | pass through, one track lower on the east |
| `db_b7` | P | 10850,5110 | in/out | bus line of a2's bit line |
| `cdp1_cK_bl` (K = 1..5) | M | x 8857, 9247, 9637, 10027, 10417 at y 5150 (drawn to there), going down through rows D and E to cdp2 (`cdp2_a_sK_bus` at y 5700) | - | continuity through rows D and E seen in the metal median of slices 3-5 only |
| `db_b5` | M | 8727,5150 going down (the tap at 8727,4937) | - | not followed |
| `db_b7` | M | the metal goes on down from its contact, jogging to x 9335 at y 5095-5110 | - | not drawn below y 5084, not followed |
| (not mine) | M | x 10808 from a contact at (10808,3637) on a poly line from the east (y 3625-3645); x 10850 from a contact at (10850,3590) on a poly line from the east (y 3580-3597); both run south past y 5750 | - | two trunks along the east edge; not drawn |

## Ambiguities

1. **m3 and m6 have no contact that I can see.** Each cell has two more vertical metal
   pieces that end inside it: m3 (8934-8956 x 3060-3168, a 10 px neck down to a pad at
   8936-8960 x 3288-3321) and m6 (9105-9127 x 3060-3322). Neither shows a contact ring
   or a widened pad, and `acid1b` shows no contact specks or patch under them, where
   every certain contact in the cell shows both. They are traced as floating metal
   (`cdp1_*_m3`, `cdp1_*_m6`). In row C, m6 is joined to `q` by the pad at the top of
   `pt`. Candidates if they do connect: m3 to the feedback diffusion under it at
   8930-8955 x 3098-3125 (that is `x`); m6 to the diffusion arm under it at 9098-9132 x
   3098-3122 or the diffusion at 9104-9130 x 3185-3240 (both `q`). None of these would
   change the logic. What would settle it: a sharper metal shot, or finding the same
   cell elsewhere with m3/m6 used. The dark rings on the poly write line at 9133-9148 x
   3300-3318 and 8962-8975 x 3295-3318 are *not* contacts: they sit in the gaps between
   two metal lines (trap 2 of the guide).
2. **`pt` to `q`** (buried contact at 9096-9134 x 3096-3126, drawn `?B`). `pt` ends on
   the arm of the q diffusion; a box with a heavy outline is there but lighter inside
   than the other buried contacts. Inferred: `pt` touches nothing else in the cell, and
   in row C it drives a gate of row B, so it must be an output.
3. **Feedback transistor.** Read as one diffusion 8905-9132 x 3099-3124 under a
   widening (8958-9040 x 3066-3128) of the grounded poly. The alternative reading, a
   separate poly strip 8958-9040 x 3100-3123 butted to diffusion at both ends, would
   make `x` = `q` by a plain wire and leave the grounded poly without any function, so
   it is rejected; the poly shows as one piece from y 3066 to 3120 in the 10 px sliver
   between m3 and the VCC rail (8960-8975).
4. **Load 1 geometry.** The load strip is taken as 8958-8985 under a poly block
   8933-9016 x 3176-3234; the block's left tie is the buried contact at 8896-8932.
   The strip's exact position under the block is not certain (it is hidden by m3's neck
   and the VCC rail); the connectivity (VCC - load - q1, gate = q1) does not depend on it.
5. Slice 0 of row A has no VSS diffusion tail to its left and no neighbour; the cell
   was drawn so that this needs no exception. The first cell's write-line leg is wider
   (8395-8445) than the others.

6. **NOR load in slice 1** (`?D 9040,3575:9140,3640`): the diffusion between the VCC
   contact land and the gate bar is hidden by heavy outlines; drawn as inferred. The
   bar, its buried contact on the line and the diffusion on its right are clear.
7. (Settled.) The strip under each VSS rail in row B (x 9158-9180, y 3702-3836 in
   slice 2) is diffusion (197/174/129 against 185/116/122 for field under metal) and is
   the source of the previous slice's series pair. Slice 1's rail has none.
8. **Row B XOR: how the band to the series pair joins the output diffusion**
   (`?D 9258,3680:9308,3696`). The band y 3699-3712 under the B line and the VCC rail is
   diffusion-coloured and its lower edge runs on west as one line, curves up round the
   load gate's tab at x 9300 and runs along y 3696 to x 9250; above it a plain region
   reaches up to a heavy line at y 3676 (the region's top edge, from x 9200 to 9325).
   So the band widens to y 3678-3696 west of x 9318 and heads for the diffusion under
   `cdp1_nor`'s buried contact. Between the two, at x 9262-9272, all four shots show a
   narrow outlined strip coming down from the right side of the buried-contact box to
   y 3688, with about 8 px of plain colour between its end and the y 3696 line.
   Candidate readings: (a) the diffusion is continuous past the end of the strip
   (drawn); (b) the strip is part of the buried contact and joins both sides; (c) the
   band is a separate island. In (a) and (b) the pair hangs on `ne`. In (c) it would
   hang on nothing at all: there is no contact on it and the only poly near its west
   end is the load gate, itself tied to `ne`. So the logic `ne = NOT(n2 + A.B)` does
   not depend on the choice between (a) and (b); what is not directly seen is the
   8 px passage. A sharper shot of 9255-9280 x 3675-3700 would settle it.
9. **Row B XOR, B pull-down of n2** (column x 9268-9318, y 3828-3899). The column lies
   in the open between the bit line and the B line, where field and diffusion have the
   same colour (142/128/92 against 143/134/100), so its two sides were placed from
   outlines that coincide with the edges of the metal's protection margin. Both ends
   are measured (VSS tab under the bit line, n2 band under the B line) and the blob
   poly with the B contact has no other purpose, so the transistor is certain; its
   width (50) is not.

## Not done

- **Rows D and E** (y 5150-5700, slices 1-5; slice 5 = slices 2-4 by `tools/cdp1_diff.py`,
  slice 1 differs only at its left edge x 8750-8830). **Surveyed, not traced**: the cell
  has more junctions than the rest of the block together and I stopped rather than
  ship unchecked geometry. Sharp medians, coordinates in slice 2's frame:
  `tools/cdp1_sr.py 9140 5130 410 590 --offsets "390,0 780,0 1170,0" --layers acid1b`
  (whole cell, 2x) and the quadrants `9140 5140 210 285`, `9345 5140 210 285`,
  `9140 5415 210 290` at `--up 3 --layers acid1b,metal`. What those show (seen, not
  measured; every item needs its junctions checked):
  - Metal: VSS rail x 9158-9208 with contacts at (9180,5250), (9180,5430), (9183,5655);
    the column bit line x 9240-9256 straight through to y 5700; a line x 9283-9305 from
    a contact at (9292,5315) down to contacts at (9288,5562) and (9288,5652); a line
    x 9320-9345 from y 5153 to 5700 (in slice 2 a2's bus line arrives on this track
    after its jog at y 5095-5110: whether the other slices' line is fed there too was
    not looked at); VCC rail x 9375-9425 with a contact at (9395,5460); a strap
    x 9440-9465 between contacts (9460,5240) and (9455,5500).
  - **A band along the whole row at y 5165-5185** between two heavy lines (seen from
    x 8790 to 10750 at 0.5x). It is diffusion-coloured under the VSS rail, the bit line
    and the VCC rail, with no contact specks there. Believed a shared node along the
    row, like `ra_eq_r9`'s line; its ends and its load were not looked for.
  - A diffusion column x 9290-9315 hangs from that band down to y 5297 and is crossed
    by two poly bars, y 5195-5217 and y 5237-5262: believed two transistors in series.
    The upper bar's poly runs from x 9430 west to x 9257, down under the bit line to
    y 5373 and east again along y 5370-5390. The lower bar's poly runs east under the
    VCC rail to a pad (9452-9492 x 5225-5267) with the strap's contact (9460,5240).
    What the column's foot (y 5268-5297) joins was not seen; a poly band lies just
    below it.
  - That poly band, y 5300-5330, starts at a pad with the contact (9292,5315) and runs
    east to a bar at x 9482-9538, y 5303-5322. A second bar, y 5345-5365, comes from
    under the VCC rail (x 9400-9420, where it turns down to y 5400). Both bars cross a
    column x 9485-9535 that starts on the next slice's VSS land (9515-9555 x 5233-5297):
    believed a series pair to VSS with its lower end at y 5370-5395.
  - Row E: a poly pad 9253-9310 x 5550-5588 under contact (9288,5562), a diffusion land
    9268-9313 x 5635-5682 under contact (9288,5652), several short poly gates at
    x 9230-9340, y 5425-5545. Not analysed.
  - The colour test gives a contact-like patch on the left edge of the bit line at about
    (9243 + 390 k, 5546) in three of the five slices. Not established either way.
  - cdp2 reports that its row A's outputs come up to contacts at (9118+390k,5740) and
    that its bus lines are these bit lines.
- The logic in the slice-0 position and under slice 1's left edge (see Inventory).
- **The write strobes.** `wr_r8` and `wr_r9` leave on two metal lines going south
  just east of the block (x 10937 and x 10894 at y 5700). `sel_tracks.py` shows both
  unbroken to y 6209 / 6255, where a group of lines (x 10894, 10937, 10981) shifts
  track one after another (again near y 7690 and 8700). Following them means following
  that bundle down the east edge of cdp2-cdp4. Until then neither row is tied to a
  register number by its strobe.
- East ends of the bus lines, of the five compare lines and of the five pass-through
  lines (x 10850); west ends of `ra_eq_r9`, `db_b6`, `cdp1_lw1` and the five
  pass-through lines (x 8340).
- The metal of a2's bus line below its contact (jog to x 9335, on down through rows D
  and E), and the tap of a0's bus line at x 8727 below y 5150.
- m3 and m6 of the register cell (Ambiguities 1).

## Method notes for whoever continues

- Colours in `acid1b` here: diffusion is light tan with a heavy dark outline *whether or
  not metal was above*; poly is salmon under or near metal and dark orange-red, textured,
  in the open; field is pink under metal and olive in the open. Olive pockets with a
  thin outline and green rim are open field, not diffusion.
- `tools/cdp1_sr.py x y w h --offsets "..." --layers metal,acid1b,metal1,acid --up 5`
  aligns all instances of a cell to a fraction of a pixel and takes the median at 5x.
  It is much sharper than a single view or `composite.py` and is what resolved this
  cell. Offsets for `cdp1_reg`: `0,0 391,0 781,0 1171,0 1561,0 -391,0 0,1193 781,1192
  1172,1192 1562,1192` (acid1b offsets; the trace uses the metal-shot offsets).
- `tools/cdp1_tab.py` prints a brightness table of a strip; metal reads 60-75, bare
  field 45-55. It showed where a thin metal line really runs.
- `tools/cdp1_px.py` measures colours on the sharp median (boxes, profiles averaged over a
  band, and a text class map). Single-shot pixels are too grainy to profile; the median
  is not. In this area field and diffusion have the same colour *in the open*; under
  metal they differ plainly (pink against tan), and poly over a channel under metal is
  brighter than poly over field. That is what decided the XOR's junctions.
- `tools/cdp1_diff.py` prints where one copy of a cell differs from the median of the
  others; `tools/cdp1_line.py` classifies what lies along a track; `tools/cdp1_under.py`
  lists the poly lines passing under a rail (it gave the whole bus-line map of the big
  channel in two commands).
- Contact test used throughout: a metal contact is a greenish patch in the clean shot
  (R about equal to G, B under 100: 160/165/93, 143/135/80), plain poly under metal is
  216/160/115, a buried contact under metal 172/139/115.

## Which registers these are (2026-11-16)

By their write lines, followed to the strobe tracks and joined in the extraction
(`notes/blocks/wrs.md`): **row A is R8, row C is R9**, and row B is R9's equality
comparator. The five compare-value lines of channel B/C leave east along y 4003-4176 and
were followed 3,300 px east to the RA pad drivers' input lines (not drawn).

## Corrections (coordinator, from the handoffs of 2026-11-19)

- The "more [logic] at y 4740-4870" in the slice-0 position is an inverter, `sl_eq_r5_n` = NOT `sl_eq_r5`
  (x 8330-8650, y 4700-4880; drawn by `eof` with slice 0's rails there). The row y 4719 does not end at
  x 8340, and it is 22-25 px wide, not 12 (R36).
- The slice-0 data line `M 8466,3325 8466,3350 8509,3382 y4952 w=16` crosses that inverter's tie box at
  (8508-8538, 4783-4815), dark in both metal shots: by trap 27 it should be `?M` there (R41).
