# areg: address lines into the decode array, and the logic right of the array

> **Correction (coordinator, 2026-11-15).** The load strobe `ar_load` is not simply
> NOT `e_b`. The bd2 block traced its driver: `ar_load = NOT ar_load_n`, with
> `ar_load_n = NOT(bd2_x OR (e_b AND wr_addr_sel))` and `wr_addr_sel = NOR(rw_d, rs_d, cs_d)`
> (see `notes/blocks/bd2.md`). The same block found this file's reading of the poly
> from (16252,14862) wrong: it ends on a buried contact.

Region x 15800-16950, y 12900-14700. Trace: `trace/areg.txt` (`@requires decode`).
Extracts with 0 errors, 0 warnings, no unnamed open nets.

## Status

- **The five cells at x 15930-16200 are not the address register. They are plain
  inverters**: upper row of each decode pair in, lower row out. Traced, placed five
  times, each instance checked, joined to the decode rows.
- **The address register is the row of five cells above the decode array**
  (x 14180-16150, y 13000-13290, one every 390 px, the datapath pitch). All five are
  instances of rdp3's latch cell `rdp3_lat` (`trace/rdp3.txt`, tags `ar0`..`ar4`); the
  fifth (x 15745-16150), which lies in this region, is the instance `ar4`. **Complete:
  6 transistors per cell, all extracted, every equation firm; each of the five instances
  checked by overlay at 3x and compared block by block in three shots** (2026-11-17
  17:37 +0000, see "Fifth register cell"). The partial drawing of the first run is
  superseded; everything it listed as "seen but not drawn" is accounted for below.
  The check found one error in the cell, fixed in `trace/rdp3.txt` in a commit of its
  own (64f8b04): the write pass transistor is 70 px wide, not 34.
- The load strobe (`ar_load`) is traced from the register cells to where it leaves the
  region: metal at x 16299, y 14700, going down. Followed by eye below the region: it is
  the output of a gate at about x 15880-16150, y 15230-15330 (bd2's area), see Logic.
- Vertical bundle x 16200-16450: traced as labelled wires with ports.
- Right-hand column of cells (x 16480-16800) and everything right of x 16460: not started.

## Inventory

| What | Where | State |
|---|---|---|
| Row inverters `areg_inv` x 5 | 15930-16200 x 13730-14570, pitch 173 | traced, extracted, all five checked |
| Feeds of the upper rows | metal from x 15800 at y 13350/13391/13433/13480, poly L shapes | traced |
| VSS rail | enters at (16122,12900), diagonals, x 15925-15975 over the inverters, ends y 14625 | traced |
| VCC rail of the inverters | enters at (16282,12900), x 16142-16194, leaves at y 14700 | traced |
| VCC rail of the register row | x 15925-15975 from y 12900 to 13578, then the wide rail x 15795-15890 down to y 14700; joins the decode array's VCC bus | traced |
| Fifth register cell (`rdp3_lat` instance `ar4`, in `trace/rdp3.txt`) | 15745-16150 x 13000-13290 | traced, extracted, checked (see Logic) |
| Bundle: `ar_load`, `areg_w6`, `areg_w7`, `areg_rail_r` | x 16291-16451 | traced as wires |
| Right-hand column | x 16480-16800 | not traced |

## Logic

### Row inverter (traced)

One per row pair, identical (cellcheck: 95-96 % median correlation, differences only where
the feed joins).

- The pair's ground diffusion rail from the decode array (y 13782-13832 for pair 0) runs on
  to the right, takes a contact from the VSS rail at (15950,13805), and is the source of
  the pull-down.
- Upper row poly: arrives from the array at y 13753-13777, steps up under the VSS rail to a
  band at y 13731-13751, crosses the cell and ends in a tab under the VCC rail
  (16150-16182 x 13731-13773). A bar hangs from the band at x 15993-16018 down to y 13843:
  the pull-down gate (W/L 71/25).
- Output node: diffusion x 16018-16087, y 13790-13832.
- Load: poly block 16087-16130 x 13768-13865 over the diffusion strip (W/L 42/43), far end
  of the strip contacted to the VCC rail at (16165,13805). The block is part of the lower
  row poly, which is tied to the output node by a buried contact at
  16038-16068 x 13803-13843 (the "intricate shape": concentric arches in the clean shot).
- Lower row poly: block, bottom band y 13860-13882, steps up under the VSS rail to the
  array's lower row at y 13838-13864.

Traced: `ar<k>_n = NOT ar<k>`, k = 0..4. `ar<k>` is the **upper** row of pair k and is the
wire that arrives from the register; `ar<k>_n`, the lower row, is generated here.

### Feeds of the upper rows (traced)

| Pair | Enters | Route |
|---|---|---|
| 0 | metal, x 15800, y 13480 | contact 15887,13480; poly right to x 15975, down under the VSS metal into the cell's left pad at y 13731 |
| 1 | metal, x 15800, y 13433 | contact 15840,13433; poly right to x 16189, down, jog right at y 13565 to x 16210, down to cell 1's tab at y 13936 |
| 2 | metal, x 15800, y 13391 | contact 15885,13392; poly right to x 16231, down to contact 16232,13522; metal x 16232 down to contact 16232,14107 on a poly pad joined to cell 2's tab |
| 3 | metal, x 15800, y 13350 | contact 15840,13350; poly right to x 16280, down to y 14286, left into cell 3's tab |
| 4 | poly, from the fifth register cell at 16066,13280 | right along y 13309 to x 16320, down to y 14459, left (under `ar_load`) into cell 4's tab |

No gate anywhere on these routes: each upper row is the register cell's output node itself.
The four metal lines collect, in a wide view, one line from each of the four register
cells left of x 15800 (each cell's output poly goes down to a contact at about y 13308,
seen on cell 4 at 15668,13308). Which cell drives which line is in rdp3's area; the
natural guess (leftmost cell = pair 0) is not traced.

### Fifth register cell (traced: `rdp3_lat`, instance `ar4`)

The cell is not drawn in `trace/areg.txt`. It is the fifth copy (`@inst rdp3_lat 1170,0
tag=ar4` in `trace/rdp3.txt`) of the latch cell that rdp3 traced on the second cell from
the left (master x 14597-14987; add 1170 for this cell). `notes/blocks/rdp3.md`, "Latch
cell", is the reference for the cell; this section says what this package checked, what
it changed, and how the first run's partial reading maps onto the cell. Coordinates below
are those of the fifth cell.

Devices (6 per cell; extracted for all five, k = 0..4, data bit k on cell k):

| Device | Where (cell 5) | W/L | Gate | Between |
|---|---|---|---|---|
| T1, write pass transistor | 15776-15846 x 13060-13088 | **70/28** | `ar_load` | `db_b4` <-> `ar4_a` |
| T_b, pull-down of inverter 2 | 15780-15802 x 13152-13203 | 51/22 | `ar4_a` | `ar4_n2` <-> `vss` |
| L2, load of inverter 2 | 15877-15922 x 13100-13152 | 30/52 | `ar4_n2` (tied) | `vcc` <-> `ar4_n2` |
| T_a, pull-down of inverter 1 | 16070-16092 x 13098-13150 | 52/22 | `ar4_n2` | `ar4` <-> `vss` |
| L1, load of inverter 1 | 15967-16018 x 13072-13100 | 28/49 | `ar4` (tied) | `vcc` <-> `ar4` |
| hold device | 15897-15979 x 13224-13246 | 22/82 | `vss` | `ar4` <-> `ar4_a` |

Equations (`tools/unsure.py --equations '^ar'`: all FIRM):

```
ar4_a  <- db_b4          through T1 while ar_load is high
ar4_n2 =  NOT ar4_a
ar4    =  NOT ar4_n2     (so ar4 has the sense of the data line)
ar4_a <-> ar4            hold device, always on if it is a depletion device (believed)
ar4_n  =  NOT ar4        (row inverter, this block)
```

What rests on `?` items: only the hold device. Its diffusion strip (`?D`
15890-15994 x 13224-13246, in the cell) is rdp3's reading and stays uncertain: the
strip's two ends are hidden under metal-gap lines and the implant cannot be seen. The
three inverter equations and the write path do not depend on it. Without the hold
device the cell would be a dynamic latch (storage on the gate of T_b only).

**How the first run's "seen but not drawn" list maps onto the cell** (each looked at
again on cell 5, 3x overlay `c5_acid1b.png`, `c5_acid.png`, `c5_metal.png` in
`cache/scratch/areg/`, and at 4.6-5.8x where named):

- "The first inverter's load, a poly block under strap M2 at 15885-15904 x 13105-13157":
  L2. The block is wider than it looked (15877-15922, on to the vertical piece at
  15921-15945 without a gap); only its part under the track shows channel-bright because
  the gap between the track and the VCC rail draws a dark bar down x 15902-15917. Profile
  of the clean shot across it in all five cells (R 237-248 at x 15890-15899 against
  213-228 for the same poly over field on either side); the strip itself measures
  x 15886-15913 just above the block.
- "`areg_s4_n` reaches `areg_g1` ... heavy edge at x 15905-15912, poly blob with a
  buried-contact box at 15828-15866 x 13127-13172": that is node `ar4_n2`. The drain of
  T_b runs right as a band (y 13172-13189) to the land at the foot of L2
  (15870-15914 x 13156-13190); the box is the gate tie of L2 (buried contact
  15830-15862 x 13140-13168 on a bump of the drain band), whose poly is the load gate
  block and continues down the right side (x 15921-15945) and along y 13162-13187 to the
  gate of T_a. The first run's names `areg_s4`, `areg_s4_n`/`areg_g1` are `ar4_a`,
  `ar4_n2`. (`hard5.png`, 4.6x, clean shot and chip-2 stripped shot.)
- "Static feedback ... poly pieces along y 13205-13245 ... two bands under the VCC rail":
  the gate poly of T_b runs on right along y 13210-13232 to a buried contact
  (15848-15870 x 13210-13240) on the feedback land (15850-15894 x 13214-13244); from
  there the hold device's strip runs under the block to the output land
  (15990-16038 x 13197-13243). So the storage node and the output node are **not** one
  net: they are joined through the hold device. Seen on cell 5 at 5.5x in three shots
  (`hold5_55x.png`): three bands under the VCC rail separated by thin dark lines at
  y 13221 and 13247, the middle band brighter and redder than the outer two. Measured
  in the clean shot at x 15945 in all five cells (R, R-G): upper band 185-195, +37..+56;
  middle band 199-227, +53..+86; lower band 188-216, +42..+74; reference under the bus
  line: gate over channel 232-242, +70..+73, poly over field 212-219, +56..+65. The
  middle band is the brighter in every cell (by 4 in cell 1, by 25-42 in the others),
  which is what poly over a channel does under metal (tracing guide, trap 6). It agrees
  with rdp3's reading and does not prove it: the strip stays `?D`.
- "A horizontal poly band at y 13250-13268, x 15748-15985": the lower part of the hold
  device's gate, which runs on left to a metal contact on the VSS rail at (15732,13256)
  (olive in the clean shot, R-G -17; the same in the other four, -24..-1).
- "Straps M2 (x 15877-15897) and M5 (x 16050-16068) with no contact found": both are
  isolated metal stubs, the pieces inside the cell of two tracks that run through the
  same cell in the register rows above (rdp3: the `hc` track and a track that is a
  through line in one slice). M2 is `ar4_trk`. Measured in the clean shot in all five
  cells: where each stub crosses the strobe's top band the poly is salmon (R-G +26..+40,
  no olive patch; the metal contacts on poly in the same cell read -24..-1), at the
  bottom band likewise (+45..+62). M5 lies on the drain of T_a (flat tan, no specks) and
  on the output's buried contact. At 5x in both metal shots and the clean shot
  (`t56_5x.png`) M5 shows no ring anywhere from y 13012 to 13275, only the dark lines of
  the edges it crosses. If M5 did touch the drain or the output land it would change
  nothing: both are `ar4`.

**The check of the five instances.** (a) Overlay of the whole trace on the clean shot at
3x, one image per cell (`c1_acid1b.png` .. `c5_acid1b.png`): every outline of the cell
sits on its feature in each of the five; cell 5 also on the chip-2 stripped shot and the
metal shot. (b) `tools/rdp3_cmp.py 15740,12995:16160,13295` with offsets 0, -390, -780,
-1170, -1560, blocks of 30 px, in `acid1b`, `metal` and `acid`: the cells agree
everywhere except (i) the right-hand 60 px of cell 5 (x 16100-16160: the sixth VSS rail
is narrower there and there is no next cell: no bottom band and no band contact at
(16122,13256)), (ii) the left-hand edge and the track at x 14322 in cell 1 (the `hc0`
track runs through that cell; rdp3), (iii) scattered single blocks at contacts (pits
differ). (c) The contact and no-contact readings above were measured in all five cells
(`tools/rdp3_boxstat.py`). (d) Below the cell: cells 1-4 end their output poly on a pad
with a metal contact at y 13308; cell 5 has none, its output poly (x 16045-16070) turns
right at y 13297-13317 and is the feed of row pair 4, continuous in poly under the VSS
and VCC rails in both stripped shots (`out5.png`, 3.8x). (e) The strobe's right end:
poly from the cell's top band under both rails to a pad with a metal contact at
(16296,13023) (`strobe_end.png`, 4x).

**Pass transistor: found wrong in the cell, fixed (commit 64f8b04, `trace/rdp3.txt`).**
The cell had T1's diffusion as the 34 px strip under the bus line. The diffusion is one
P-shaped region: the bus contact land (x 15772-15822, y 13010-13045) widens to
x 15848 from y 13045 to 13105 and the gate band (y 13060-13088) crosses all of it; below
y 13105 only the strip under the bus line goes on down to the buried contact of node a.
Evidence: one closed outline with rounded corners at (15846,13047) and (15848,13105),
continuous with the land's outline, in both metal shots at 6x (`pass5_m.png`,
`pass5_wide.png`), the same in all five AR cells (`pass_mos_metal.png`,
`pass_mos_metal1.png`); the band between is poly-coloured, the areas above and below
plain. In the AR row that part is in the open, where the clean shot cannot tell channel
from field; in the rows where a metal covers it, the gate band is channel-bright over
the whole 70 px in the clean shot (`passR_acid1b.png`: four cells of R1/R2;
`passX1.png`, `passX2.png`: cells in the rows of R4, R6, R7, R5, R3; review round 1
measured all 46 covered copies of R1-R7). In R0's row, as in the AR row, that part is in
the open and rests on the outlines in the two metal shots. The
strobe's riser beside it stands at x 15851-15872 (the cell had 15837-15867, which
would have lain on the wider diffusion). Effect: 59 pass transistors (all copies of the
cell in rdp1, rdp2, rdp3) change from 34/28 to 70/28; no net changes; the full
extraction still has 3760 transistors, 0 errors, 0 warnings. The first run of this
package had read it so (W/L 70/20). With it the write path is about nine times as
strong as the hold device (2.5 squares against 0.27).

What the cell is: a level-sensitive latch written through one pass transistor,
transparent while `ar_load` is high, two inverters, and (believed) a weak always-on
feedback from the output to the storage node that makes it static. No clock is
involved. Data input of cell 5: `db_b4`, the bus line at x 15797 (contact
(15792,13035)); so the address register takes data bits 0-4 in order, cell k = bit k.

### Is the upper row of each pair the true address bit?

Traced, and extracted with firm equations: the upper row of pair k is `ark`, the output
node of register cell k with no gate in between; `ark` = NOT `ark_n2` = `ark_a`, the
stored value of `db_bk`, in the sense of the data line; the lower row is `ark_n` = NOT
`ark`. So decode.md's naming holds: **upper row = true address bit**, provided `db_bk`
carries data bit k uninverted (that is the data bus column's business, `dbus`).

### Where the load strobe comes from (seen below the region, not traced: bd2's area)

Followed `ar_load` past the boundary at 1-3x, without tracing:

- Metal x 16291-16307 goes down from y 14700 to a contact at (16298,14822), ducks under a
  horizontal metal band (y 14905-14960, a branch of `areg_rail_r`) in poly, and comes back
  to metal at a contact at (16298,15000).
- That metal runs down to y 15265, turns left and **ends** at a contact at (16255,15258).
  Nothing continues down at x 16299 below y 15270.
- From the contact a poly runs left along y 15245-15268 to a buried contact at about
  16105-16130 x 15250-15275 on a diffusion strip (y 15258-15288) that runs on to the left
  under a wide vertical rail (x 16005-16050) to beyond x 15985.
- Directly below that strip a long poly band (y 15290-15312, x 15990-16195) with
  diffusion on its far side (y 15315-15350, contacted to the wide rail at about
  16035,15335): a pull-down on the strobe node. The band comes from a contact at
  (16210,15300) whose metal goes down at x 16200-16220.
- So **`ar_load` is the output node of a gate at about x 15880-16150, y 15230-15330**,
  not a pin signal wired straight through. The rest of that gate (its load and other
  pull-downs, to the left of x 15985) was not looked at.
- Warning for whoever joins the ports: `notes/blocks/trunks.md` has `rw_d` on a metal at
  x 16290-16308 from y 17558 up to "above 15900, not followed", and `rs_d` at
  x 16333-16352. These are in line with `ar_load` (x 16299) and `areg_w6` (x 16341) but
  **`ar_load` is not that metal continued**: its metal ends at (16255,15258). `areg_w6`
  likewise leaves metal at a contact at (16337,14862) and continues as a poly that runs
  down x 16340 to y 15255 and then diagonally down-right to about (16490,15390). Whether
  either trunk line reaches these by another route is open.
- Also seen: a third contact at (16252,14862) beside the two cross-unders takes a
  horizontal metal from the left (y 14855-14875) into a poly going down x 16247-16265 to
  a contact at (16255,15085); from there a metal goes down to y 15213, left to x 16170 and
  down at x 16160-16180 (trunks has `e_b` on a metal at x 16160-16180 further down).

## Ports

| Name | Layer | Crosses at | Direction | What |
|---|---|---|---|---|
| `ar0` | metal | x 15800, y 13480 | from outside (left) | output of a register cell, for row pair 0 |
| `ar1` | metal | x 15800, y 13433 | from outside | same, pair 1 |
| `ar2` | metal | x 15800, y 13391 | from outside | same, pair 2 |
| `ar3` | metal | x 15800, y 13350 | from outside | same, pair 3 |
| `ar0`..`ar4`, `ar0_n`..`ar4_n` | poly | x 15800, the ten decode rows | upper rows pass through to the array, lower rows driven here | joined to `trace/decode.txt` by overlap |
| decode ground rails | diffusion | x 15775, y 13782-13832 and every 173 below | - | also contacted to VSS here |
| `ar_load` | metal | x 16299, y 14700 | from outside (below) | load strobe of the address register; no tap in this region other than the register |
| `ar_load` | poly | x 15800, y 13061-13081 | passes on to the left | the same strobe continuing to the other four register cells |
| `db_b4` | metal | x 15797, y 12900 | from outside (above) | data line of the fifth register cell (drawn in `trace/rdp3.txt`) |
| `vss` | diffusion | x 15745, y 13150-13200 | - | source of T_b of the fifth cell: the VSS land under the rail at x 15735, contact (15725,13163) (in the cell) |
| `areg_w6` | metal | x 16341, y 14700 | unknown | up the bundle to contact 16337,13264, then poly right along y 13263; drawn to x 16480, goes on to the right-hand column |
| `areg_w7` | poly | x 16364, y 14700 | unknown | up the bundle to y 13453, then right; drawn to x 16480, goes on to the right-hand column |
| `areg_rail_r` | metal | x 16426, y 12900 and y 14700 | supply? | 49 px wide rail through the whole region; which supply is not established |
| `vss` | metal | x 16122, y 12900 | supply | VSS rail entering from above |
| `vcc` | metal | x 16282, y 12900 and x 16168, y 14700 | supply | VCC rail of the inverters |
| `vcc` | metal | x 15950, y 12900 and x 15795-15890, y 14700 | supply | VCC rail of the register row / wide rail; also joins the decode VCC bus at x 15775, y 13518-13632 |

No taps on `ar_load`, `areg_w6`, `areg_w7` between their ends: looked at in the clean and
metal shots over the full height.

## Ambiguities

1. Tab at the right end of each upper row (16150-16182 x 13731-13773 for pair 0), under the
   VCC rail. For pairs 1-4 it is where the feed joins; for pair 0 the feed joins at the
   left and the tab is a dead end. No contact seen on it in either metal shot or the clean
   shot (a contact would short `ar0` to VCC). Working assumption: no contact.
2. Register cell, join between the strobe band's left end (x 15772) and cell 4's leg
   (x 15745-15766): a dark line at x 15768-15775 lies between them. **Closed: one poly.**
   The line is the bar that the 16 px gap between the VSS rail (edge x 15765) and the bus
   line (edge x 15781) leaves on whatever is underneath (layers.md, traps); it is there in
   all five cells and in both stripped shots, with poly of the same height on both sides.
   The cell draws the strobe as one snake. (For cell 5 nothing depends on it: its gate
   band is fed from the right, by the riser.)
3. Register cell, output poly start (16042-16071 x 13218-13245), with stub M5 over it.
   **Closed: buried contact, no metal contact.** Flat tan box with a heavy outline and no
   specks in the clean shot, no ring in either metal shot at 5x (`t56_5x.png`). A metal
   contact there would only put the stub on `ar4`.
4. Register cell, stubs M2 and M5. **Closed: no contact on either** (see Logic).
5. Register cell, how the storage diffusion meets the gate poly of T_b. The first run
   read a buried contact on a tab at 15818-15850 x 13088-13106 and a poly down the right
   edge of the bus line; the cell has the strip going on down under the bus line to a
   buried contact at 15774-15812 x 13120-13142. The "tab" is the lower part of the wide
   pass-transistor diffusion (see "Pass transistor"). Under the bus line the clean shot
   shows, from the top: diffusion to y 13110, a box with a heavy outline and a tan inside
   at y 13113-13135, poly from y 13138, the channel of T_b from y 13152 (`arm5.png`,
   5.8x). That is the cell's reading. Either way the net is the same (`ar4_a`).
5a. Register cell, "concentric arches" at 16028-16050 x 13113-13147, which the first run
   drew as the buried contact of load L1. This run read them as a metal-gap artefact; that
   is wrong: review round 1 found a closed box there in BOTH metal shots, in every cell
   viewed (ar0-ar4 and three register cells, 6.5x, `review-1/arch_mos.png`; confirmed by
   the tracer), with a top edge at y 13113-13120 that the trace has no item for. It is a
   real feature of `rdp3_lat`, probably a second poly-to-diffusion tie from L1's pad onto
   the `ar4` drain; undecided. L1's drawn gate tie is the box at 16016-16044 x 13066-13100.
   Every reading puts the load gate on `ar4`, so no net depends on it. Not drawn (the
   cell is rdp3's): in the handoff.
5b. `rdp3_lat`'s L2 gate block: its left edge is drawn at x 15877; both metal shots put
   it at about 15863-15866 in all five AR cells (review round 1). Poly over field only,
   no device or net change; about 12 px from the wide diffusion's corner (15847,13104),
   no overlap. Not changed (rdp3's cell): in the handoff.
6. Which supply `areg_rail_r` is. The loads of the right-hand column cells will tell.
7. Under `areg_rail_r` a poly runs along its left edge (x 16402-16420) from y 13650 to
   y 14440, with an arm to the right at each end (y 13650-13665 and y 14422-14440). Seen
   in the clean shot, not drawn.

## Not done

- Fifth register cell: nothing. (The hold device's strip stays `?D` in the cell; what
  would settle it is a shot that shows the implant, or the strip's two ends, which lie
  under metal-gap lines at x 15893-15900 and x 15978-15985 in every cell.)
- Not checked by this package: the copies of `rdp3_lat` in rdp1 and rdp2 other than the
  pass transistor (ten sampled for that), and the cell's W/L values other than T1's and
  L2's width.
- The gate that drives `ar_load` (about x 15880-16150, y 15230-15330, outside the
  region): trace it and its inputs. This is the question that matters most.
- Right-hand column, x 16480-16800: four identical cells at about y 13060-13250,
  13270-13450, 13470-13640, 13660-13840 (pitch about 190, each with a contact near
  x 16540), then larger, different cells from y 13900 to 14700. Wide vertical metals at
  x 16490-16540 and x 16650-16700, thin ones at x 16790-16830. Horizontal poly lines
  arrive from the bundle at y 13263 (`areg_w6`), y 13453 (`areg_w7`), y 13657 and y 14431
  (the two arms of the poly under `areg_rail_r`).
- Region right of x 16800 (a block at 16860-16950 x 13820-13930, lines to the right edge).
- The neighbouring items left of x 15800 that belong to this cell row are rdp3's.

## Review

Round 1 (full review, 2026-11-17 17:50 +0000, a fresh agent on claude-fable-5-2, at commit a0069a7). Told to
suspect the T1 width change in every register row (a cell variant with the narrow strip),
the moved riser (a new transistor or short), the node-a buried contact, the "arches", L2's
right edge, and cell 5 against cells 1-4. It measured the gate band in all 46 covered
copies of R1-R7 in the clean shot, viewed nine at 3.7x, profiled all 13 open copies (AR,
R0) in both metal shots, compared the netlists before and after the cell fix (identical
except 59 transistors 34/28 -> 70/28), and checked cell 5's joins in four shots.
No finding changes a connection or needs a geometry change in this package. Findings,
each confirmed by the tracer in the reviewer's images:
1. The "arches" are a real closed box, not a metal-gap artefact: Ambiguity 5a rewritten.
2. L2's gate block left edge is about 12 px east of the photo: recorded as Ambiguity 5b.
3. R0's row is in the open like AR's (the notes had it among the covered rows): corrected.
Not checked: the hold strip's ends (stays `?D`), the riser of the non-AR copies beyond the
nine viewed.

Round 2 (fix check, 2026-11-17 17:55 +0000, a fresh agent on claude-fable-5-2; no geometry changed since
a0069a7, only these notes). It checked the three corrected statements at 4.6x in metal,
metal1 and acid1b in ar1-ar4 and four register cells: the box (5a) is closed in both metal
shots, has no metal over its interior (not a metal contact), and is separated from stub
M5, the `n2` band and T_a's gate by straight edges, field and plain diffusion, so no
reading of it changes a net; L2's left edge (5b) at x 15864-15866, 16-19 px from the
diffusion corner; R0's row in the open like AR.

Round 2: no findings.
