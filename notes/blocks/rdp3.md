# rdp3: right datapath, lower rows

Region: x 13350-16950, y 10700-12900, plus x 13350-15800, y 12900-13480.
Trace: `trace/rdp3.txt`. Scratch: `cache/scratch/rdp3/`.
Own tools:
- `tools/rdp3_sharp.py`: view.py with an unsharp mask.
- `tools/rdp3_strips.py`: montage of vertical strips, for following per-slice lines.
- `tools/rdp3_cmp.py`: compares copies of a rectangle with their median, block by block,
  as text (no image needed), and can save the median as a composite. Every instance
  below was checked with it. Composites: `rdp3_w16` (x 14490-15010, y 11690-12445, the
  whole period of a slice: comparator cells and latch, median of 12 inner slices of both
  bands), `rdp3_p16` (narrower, all 16), `r0w` (the AR cells).
- `tools/rdp3_boxstat.py`: mean colour of small boxes in all shots, by class, with R-G of
  the clean shot: tells a metal contact on poly (olive, R-G -22..+7, bright in `metal1`)
  from a buried contact or diffusion under metal (tan, R-G +30..+40).
- `tools/rdp3_prof.py`: colour profile along a row or column, on the die or a composite,
  with R-G per layer, in columns that line up.
- `tools/rdp3_t7.py`: the measurement that settled T7 (strip against field and diffusion
  references, 16 slices, three shots).
- `tools/rdp3_jogs.py`: for a bundle of vertical tracks, where metal crosses the gaps
  between tracks (jogs) and where a track has no metal. `tools/sel_tracks.py` bridges
  gaps up to 14 px and so reads two nets that share a track across a jog as one line.

Slice tags and columns: s0..s7 from the left; sK has its VSS rail (left edge of the
slice) at x 13783 + 390 K, i.e. s(K) = right-datapath column c(K-1); s0 lies left of c0.

## Status

- Traced, placed and checked: the address register row AR (5 latches), the two 8-bit
  register rows RA and RB (16 latches), under each a full 8-bit equality comparator
  (per slice a true XOR of the register bit with a per-slice line `c`, and a pull-down
  on a row-wide wired-NOR line with one load), the exits of both equality lines, the
  left-edge bundle and the routing zone between RA and AR. Every bus line, c line,
  strobe and equality line is drawn to the region's edge and is in the ports table.
  256 transistors; extracts with no errors and no open nets.
- **Run 3 corrects run 2: RB is R2 and RA is R1; R0 is row RC (rdp2's), the row above.**
  The bundle steps one track to the left at y 12300-12540, which the track scan could
  not see. So `h_eq_r2` is "c = R2" (horizontal sync position) and `h_eq_r1` is
  "c = R1" (horizontal displayed). The R0 comparator is rdp2's band C.
- Both equality lines leave through a buried contact in slice s1 onto a poly line going
  west to bundle track L3: `h_eq_r2` then goes **north** (out of the region at
  13478,10700), `h_eq_r1` **south** (out at 13434,13480, bd1's track k8). Neither is
  gated or latched inside the region.
- The R0 match itself (rdp2's `h_eq_r0`) crosses this region in the bundle as
  `h_eq_r0`: in on L2 at (13434,10700), jog left at y 12486, out on L1 at
  (13391,13480) = bd1's track k7. No contact, gate or latch on the way.
- Not done: only details (see the end).

## Inventory

Slices: 8, pitch 390, numbered s0..s7 from the left. In slice sK:

| x (s2; add 390 per slice) | What |
|---|---|
| 14565 | VSS rail (60 wide); a ninth one at x 16906 right of s7 |
| 14626 | bus line (data), `rbus_bK` |
| 14673 | metal piece y 11738-12200 in each band, no contact found ("T2") |
| 14712 | `hcK`: the line the register bits are compared with |
| 14772 | VCC rail (56 wide) |
| 14886 | strap inside each latch cell, no contact; in s7 a through line (x 16838), which is bus line s0 (see "Routing zone") |

Rows (band B = band A moved up by 846; the two bands are identical from the top of the
comparator down, measured: block correlation 0.93-0.98):

| y | What |
|---|---|
| 10561-10831 | register row RC (rdp2's; the region's top edge y 10700 cuts through it) |
| 10831-10925 | gap: the poly line of `h_eq_r2` at y 10846-10867 (from slice s1 west to the bundle); RC's strobe poly is at y 10800-10830 |
| 10925-11056 | band B match pull-downs (`rdp3_mpd`), `h_eq_r2` strip at y 10930-10952 |
| 11056-11321 | band B XOR cells (`rdp3_xor`) |
| 11321-11591 | **register row RB = R2** (`rdp3_lat` upside down), strobe poly y 11558-11586 |
| 11591-11775 | gap: empty field except the poly line of `h_eq_r1` at y 11693-11713 (from slice s1 west to the bundle) and the rounded top ends of the T2 pieces at y 11738 |
| 11775-11905 | band A match pull-downs, `h_eq_r1` strip at y 11776-11798 |
| 11905-12167 | band A XOR cells |
| 12167-12437 | **register row RA = R1** (`rdp3_lat` upside down), strobe poly y 12404-12432 |
| 12437-13010 | routing zone: poly lines east-west under the rails take the bus lines to the lower right and the c lines to the lower left (traced, run 3) |
| 13010-13280 | **row AR**: 5 latch cells under slices s1..s5 |
| 13280-13500 | the five AR outputs, nested L-shaped lines going right |

Left of the array, x 13348-13825: a bundle of 12 vertical metal tracks on a 43.4 px
pitch, L0..L11 at x 13348 + 43.4 k (bd1 calls the same tracks k6..k17 at y 14700).
L10 and L11 exist only below the array (L10's place is the first VSS rail higher up).
See "Left-edge bundle" under Logic.

Below the array the rails shift: the first VSS rail (x 13783) narrows and steps right at
y 12631 to x 13912; the four right-hand rails run diagonally down-left between y 12450
and 12960 (VCC 16332 to x 16215, VSS 16516 to 16428, VCC 16723 to 16520, VSS 16906 to
16690).

Rails: which is which was settled by the first run (both loads of every latch hang from
the x 14772 + 390k rail, which also runs into the decode array's VCC bus). All new
cells agree: every load strip starts on a land contacted by that rail.

## Logic

### Latch cell `rdp3_lat` (traced)

Master at x 14597-14987, y 13010-13280 (slice s2 of row AR). 6 transistors:

```
a   <- bus      pass transistor T1 while the strobe is high        70/28 (was 34/28: corrected by `areg`, 2026-11-17, all 59 copies)
n2  = NOT a     pull-down 51/22, load 30/52
q   = NOT n2    pull-down 52/22, load 28/49
a  <-> q        hold device, gate tied to VSS, 22/82 (see below)
```

- Bus contact at the strobe edge of the cell; strip under the strobe poly's loop (T1);
  buried contact to the poly that is the first inverter's gate (node a).
- q is in the same sense as the bus. It leaves by a buried contact on the output land
  onto a poly strip (down in AR, up into the comparator in RA/RB).
- T_a's source is the VSS land of the next slice to the right; the last cell of a row
  has a land under the rail to its right (AR: x 16125; RA/RB: ninth rail, x 16906).
- **Hold device (was AMB-1/AMB-2, read on the composites at 6-7x in three shots).** The
  poly band along the cell edge is contacted to the VSS rail (AR 14562,13256) and
  widens under the VCC rail into a block, AR 14727-14809 x 13206-13272. Two thin dark
  lines cross the block at y 13223 and 13246: what the first run saw as three stripes
  S1/S2/S3 is one piece of poly with the edges of a diffusion strip showing through
  (the gaps between the "stripes" are 3-5 px, far below any spacing rule; in the slot
  between the c track and the VCC rail, where the poly shows in open colours, S3 and S2
  look joined, which agrees but is not decisive on its own). The strip runs from the feedback land (node a, buried contact) to the
  output land (q). So: a transistor a <-> q, W/L about 22/82, gate at VSS. An
  enhancement device would never conduct, so it is believed to be depletion mode: a weak
  feedback that holds the latch and that the bus overpowers during a write. The strip is
  drawn uncertain (`?D`), the transistor is tagged `kind=hold`. Not visible: the
  implant, and the strip's ends where they meet the two lands (each is hidden by a
  metal-gap line).

### Rows RA, RB (traced): 8 bits each

`@inst rdp3_lat ... rot=180` at dx -782, -391, 0, 390, 780, 1170, 1560, 1951 and
dy -853/-854 (RA), -1699/-1700 (RB). The cell is the AR cell unchanged: the first run's
doubts about the cell's upper edge were the hold device's stripes and poly seen between
metal lines. Differences are outside the cell: the bus line and the c track run through;
q goes up in poly.

- Strobe `wr_r1`: row poly; right end free (ends at x 16925); at the left end it
  turns down at x 13782 under the first VSS rail to a pad with a contact at
  (13823,12700); thin metal on bundle track L11 (x 13825) goes down from there and
  leaves the region at y 13480.
- Strobe `wr_r2`: row poly; right end free; runs on west to a pad with a contact
  at (13648,11571); metal goes down on track L7 (x 13651), **jogs left at y 12357 onto
  track L6 (x 13608)** and leaves the region on L6.
- Which registers (run 3; the lower ends are bd1's table of tracks at y 14700, the
  stretch y 13480-14700 between the two regions was checked with `tools/rdp3_jogs.py`
  in both metal shots: no jog, and no break longer than a poly line passing under):
  - `wr_r2` arrives on L6 = bd1's k12 = `wr_r2` (contact 13609,14956).
    **RB = R2** (horizontal sync position).
  - `wr_r1` goes down L11 to y 14000, **jogs left onto L10** (x 13782; seen,
    `cache/scratch/rdp3/l11_jog.png`) = bd1's k16 = `wr_r1` (contact 13785,14913).
    **RA = R1** (horizontal displayed). The metal on L11 below y 14050 is another net
    (bd1's k17, which comes from a track at x 13868 by a jog at y 14050); the piece of
    L10 above y 13893 is a third net (ends there on a contact to a poly line going west).
  - `wr_r0` (bd1's k13, x 13652) comes up L7, **jogs right onto L8 at y 12400** and
    ends on the contact (13690,10815) on the west end of the strobe poly of row RC, the
    register row above RB, which is rdp2's. **RC = R0.** Drawn here as `wr_r0`.
  - The three rows from the top are therefore R0, R2, R1: the order of those three
    select columns in the decode array.
  - Run 2 had RB = R0 from a track scan of L7 "continuous from y 11566 to 15000". It is
    not one line: at the jog two nets share the track 22 px apart, and
    `tools/sel_tracks.py` bridges gaps up to 14 px on either side of a dark line.
  - On chip 2 the `wr_r0` line has a 10 px dark gap at (13652,12708). Chip 1's metal is
    unbroken there and nothing lies under it: dirt or a scratch on that die, not layout.

### Comparator (traced): `rdp3_xor`, `rdp3_mpd`, `rdp3_mpd1`

Per slice, master s2 of band A (x 14545-14952, y 11776-12167):

```
nor = NOR(c, q)              load 31/58;  T6 gate c 41/24;  T7 gate q 36/22
x   = NOT(nor + c.q)         load 27/50;  T5 gate nor 40/23; series pair c 72/25, q 72/24
eq  = NOR(x of 8 slices)     per slice 269/23 (s1: shorter); one load 67/42, in slice s1
```

so x = c XOR q and `eq` is high when the register equals the eight `c` lines.

- `c` reaches the cell on the x 14712 track through two contacts onto poly pads:
  (14720,11936), poly east under the VCC rail to gate G1 (x 14853-14878), and
  (14715,12121), poly west = gate of T6.
- q comes up from the latch in poly at x 14879-14901, jogs right at y 12095 and is gate
  G2 (x 14901-14925); on the way it crosses the nor node (T7).
- x is a diffusion node (band under the bus at y 11937-11961, strip down the left to
  T5, strip east at y 11963-11978 to the series pair). A tab (14624-14644 x
  11913-11942) carries it up to a buried contact on the pull-down's gate.
- Match pull-down `rdp3_mpd`: C-shaped gate round a VSS diffusion (land and contact at
  14562,11870); outside the C the diffusion is the `eq` line, a strip y 11776-11798
  that runs through all eight slices (under the VSS rails) and ends dead under the
  first rail (x 13768) and under the ninth (x 16925). Its top edge is notched 10 px
  down (to y 11786) across x 14610-14795 of each regular slice, under the bus, T2 and c
  tracks (both stripped shots; drawn so in run 3). None of those tracks has a contact
  to the strip: under T2 the strip is the same flat tan as under the c track and the
  bus line, which cannot have one.
- **Exit of the `eq` line (run 3).** In slice s1 a tab of the strip comes up under the c
  track (x 14314-14336) to a buried contact (box 14312-14338 x 11744-11766 in band A,
  y 10898-10920 in band B) on the end of a poly line. The line runs up 50 px, then west
  through the gap above the band (band A y 11693-11713, band B y 10846-10867), under
  slice s0's lines and rails and under bundle tracks L4..L9 without contact, to a pad
  with a metal contact on track L3: (13479,11703) and (13477,10857).
  - The box is a buried contact and not a contact to the c track that passes over it
    (run 2's reading, "feed of c_s1"). Measured with `tools/rdp3_boxstat.py`: inside the
    box the clean shot is tan, R-G = +37 (band A) and +34 (band B), the same as the eq
    strip under the same track (+38, +32); the 24 known metal contacts from the c tracks
    to poly pads give -22..+7 (one +29) and are bright in the chip-1 metal shot
    (180-212), the box is not (125-140, as the strip: 136-160). A column profile down
    x 14322 shows poly (R-G +63..+99) down to the box and diffusion colour, not field,
    from the box to the strip. Both bands show the same structure
    (`cache/scratch/rdp3/eq_tab_c.png`, 6x, both bands side by side).
  - A contact to the track would also tie c of slice s1 to both eq lines.
  - `h_eq_r2` goes **north** from (13477,10857) on L3 and leaves the region at
    (13478,10700); by scan the metal runs on to about y 9960. `h_eq_r1` goes **south**
    from (13479,11703) on L3, jogs left at y 12530 onto L2 (x 13434) and leaves the
    region at (13434,13480); that track is bd1's k8, which bd1 has not traced.
  - Nothing gates or latches either line inside the region: wired NOR, one load, poly,
    metal.
- Slice s1 (`rdp3_mpd1`): the C is shorter (right arm at x 14352-14372) and the room is
  taken by the load of `eq`: VCC land with contact (14403,11862), strip east under a
  gate block (14455-14497 x 11812-11915), up at x 14502-14524 to the `eq` strip; the
  block's neck ends on a buried contact on the strip (14473-14499 x 11774-11803).
- **T7's diffusion (14808-14945 x 12128-12164): settled in run 3, it is diffusion, the
  gate is a true XOR.** Run 2 left it uncertain because the part left of the q poly
  (x 14818-14872), which is not under metal, has roughly the colour of field in the
  clean shot. Measured (`tools/rdp3_t7.py`, R-G of the strip against a field reference
  and a diffusion reference inside the same cell, all 16 slices):

  | Shot | strip | field (two points) | diffusion (node x) |
  |---|---|---|---|
  | chip 2 stripped | +22 (sd 2.8; range +17..+26) | +0.4 (sd 4.6), +2.7 (sd 4.8) | +20 (sd 3.6) |
  | chip 2 metal (area not under metal) | +38 (sd 2.3) | +27 (sd 4.8), +23 (sd 1.7) | +42 (sd 1.7) |
  | chip 1 clean | +8 (sd 25; -27..+65) | +16 (sd 3.8), +19 (sd 2.1) | +34 (sd 20) |

  In both chip-2 shots the strip is diffusion in 16 slices of 16, with no overlap with
  field. In the clean shot field is uniform from slice to slice (sd 2-4) while the strip
  scatters as widely as the known open diffusion does (sd 25 and 20) and lies inside the
  field's range in only 4 slices of 16: open thin-oxide areas have no stable colour in
  that shot here, which is why it looked like field in the composite. Three more things
  agree: (a) right of the q poly, in the margin protected by the VSS rail, a tab of the
  VSS land reaches towards the poly at exactly the strip's height (clean shot at
  x 14929: tan, R-G +15..+27 in 14 slices of 14, between dark edges at y 12126 and
  12162; pink field below); (b) the strip is outlined on all four sides in both
  stripped shots; (c) the buried contact that ties load L3's gate to its output
  (14847,12098) reaches the nor band and T6 only through this strip, so its left part
  must be diffusion whatever the colour.
  With T7: nor = NOR(c, q), x = c XOR q, eq = (register = c), which is what an equality
  comparator needs. T6 and T7 are the same size (41/24, 36/22). The AND-NOT reading
  (x = c AND NOT q) is excluded.

Believed: the `c` lines are the bits of the horizontal character counter (R0, R2 and
R1 are all compared with them, R0 in rdp2's band C). Then `h_eq_r2` is "counter =
R2", the start of horizontal sync, and `h_eq_r1` is "counter = R1", the end of the
displayed part of the line.

### Row AR (first run): 5 bits, the address register

Instances `ar_s1`..`ar_s5`. Data `db_b0`..`s5`; strobe `ar_load` (joined to
`ar_load` in zz_joins); outputs `arK_q` go right at y 13352-13481 with a poly
cross-under beneath each VCC rail (joined to `ar0`..`ar4`).

### Routing zone (traced, run 3): bus lines

`rbus_bK`: thin metal at x 13845, 14236, 14626, 15016, 15407, 15797, 16187, 16577
(K = 0..7) at the top edge y 10700, straight down, one contact per latch cell. Below
row RA, in the routing zone (poly lines 20 wide, east-west, under the rails; each end a
contact with a ring in the metal shot and a pad in the clean shot):

| Bus | Path below RA | Leaves the region |
|---|---|---|
| s0 | contact (13843,12505); poly east along y 12506 under seven slices; contact (16058,12506); metal link down x 16058; contact (16058,12831); poly east along y 12831, down at x 16798 | poly, (16798,12900) going south |
| s0, second branch | contact (16601,12830) on the same poly line; metal up x 16603, diagonally up-right between the rails, then north on **x 16838, the strap track of slice s7**, through bands A and B | metal, (16838,10745) going north (drawn to there; by scan it runs on) |
| s1..s4 | straight down into the AR cells; nothing else | (end in AR) |
| s5 | contact (15797,12744); poly east along y 12744; contact (16818,12744); metal south. The line itself goes on down to AR's cell s5 | metal, (16818,12900) going south |
| s6 | ends on contact (16187,12699); poly east along y 12700; contact (16862,12700); metal south | metal, (16862,12900) going south |
| s7 | ends on contact (16580,12570); poly down x 16583, east along y 12657; contact (16908,12656); metal south | metal, (16908,12900) going south |

So the through line on x 16838 that run 2 could not place (`rdp3_t16837`) is bus line
s0: the leftmost slice's data line is also carried up the right-hand edge of the array.

Bit order: nothing in the region shows which slice is which data bit (no carry chain;
the comparator treats all slices alike). Inference only: the address register takes
D0-D4 and uses s1..s5; s0, s5, s6, s7 leave together at the lower right.

### Left-edge bundle (traced, run 3)

Thin metal, 18 wide, tracks L0..L11 at x 13348 + 43.4 k. Between y 12300 and 12540
most lines step one track to the left going down, so a track number names a place, not
a net. Each net, from north to south (all drawn; overlay `ov_bun1.png`):

| Net | North end | Path | South end |
|---|---|---|---|
| `h_eq_r0half` | L0 at y 10700 | straight down L0 to y 12789, steps left to x 13307 | leaves the region west/south at (13307,12850); the track at x 13307 above y 12745 is another line, which turns west there |
| `inh_rc` | poly pad from the west, contact (13346,12829) | L0 | L0 at y 13480 (bd1's k6 = `inh_rc`) |
| `wr_r4` | L1 at y 10700 | L1 to contact (13390,12438); poly link east y 12426-12454 under L2, L3; contact (13522,12440); L4 | L4 at y 13480 = bd1's k10 = **`wr_r4`** (so R4's write strobe goes north on L1) |
| `h_eq_r0` | L2 at y 10700 | L2, jog left at y 12486, L1 | L1 at y 13480 (bd1's k7, untraced there) |
| `h_eq_r2` | L3 at y 10700 | L3 down to contact (13477,10857) | (poly east to comparator B) |
| `h_eq_r1` | (poly from comparator A) contact (13479,11703) | L3, jog left at y 12530, L2 | L2 at y 13480 (bd1's k8, untraced there) |
| `rc0` | L4 at y 10700 | L4 to contact (13522,12375); poly west y 12387-12407 under L3..L0 | leaves west at (13330,12397) |
| `rc1` | L5 at y 10700 | L5 to contact (13565,11920); poly west y 11910-11931 | leaves west at (13330,11920) |
| `rc2` | L6 at y 10700 | L6 to contact (13608,11438); poly west y 11429-11452 | leaves west at (13330,11440) |
| `rc_eq_r4` | L7 at y 10700 | L7, jog left at y 11507, L6, jog left at y 12313, L5 to contact (13565,12826); poly link east y 12815-12837 under L6, L7, L8; contact (13736,12826); L9 | L9 at y 13480 (bd1's k15, untraced there) |
| `rc3` | L8 at y 10700 | L8 to contact (13692,10745); poly west y 10737-10758, down between L1 and L2 (x 13413), west y 10954-10976 | leaves west at (13330,10965) |
| `wr_r0` | contact (13690,10815) on RC's strobe poly | L8, jog left at y 12400, L7 | L7 at y 13480 = bd1's k13 = **`wr_r0`** |
| `wr_r2` | contact (13648,11571) on RB's strobe poly | L7, jog left at y 12357, L6 | L6 at y 13480 = bd1's k12 = **`wr_r2`** |
| `wr_r1` | contact (13823,12700) on RA's strobe poly | L11 | L11 at y 13480; at y 14000 it jogs onto L10 = bd1's k16 = **`wr_r1`** |

Lines that start in the routing zone and go south are c lines (next section): L3 from
contact (13478,12916) is `hc2`, L5 from (13565,12959) `hc1`, L8 from
(13692,12872) `hc3`, L10 from (13780,12786) `hc5`. Three poly lines pass
under the bundle on their way west: `hc7` (y 12744, then down x 13413 and west
along y 13004), `hc6` (y 13418) and, higher up, `rc3`.

Four lines from the north turn west one after another (`rc3` at y 10965, `rc2`
at 11440, `rc1` at 11920, `rc0` at 12397), towards the mid-right array. What
they are is rdp2's to say.

### Routing zone (traced, run 3): the `c` lines

`hcK`: thin metal at x 13931 + 390 K, from the top edge y 10700 down through both
comparators (two contacts per comparator cell) and both register rows (no contact). In
the routing zone each one is taken to the lower left:

| Slice | Path | Leaves the region |
|---|---|---|
| s0 | ends on contact (13933,12568); poly down x 13933, west along y 12744 under the first rail and the whole bundle, down between L1 and L2 (x 13413), west along y 13004 | poly, (13330,13004) going west |
| s1 | no contact in the routing zone; the track runs on through AR's cell s1 (no contact there) and ends on contact (14324,13458) below the row; poly west along y 13461, south at x 13871 | poly, (13871,13480) going south. By scan: a contact at about (13868,13630), metal south on x 13868, jog at y 14050 onto L11 = bd1's k17 (`hc0`), which bd1 follows into the mid-right array |
| s2 | ends on contact (14712,12961); poly west along y 12961; contact (13565,12959) on L5 | metal, (13565,13480) south = bd1's k11 |
| s3 | ends on contact (15105,12917); poly west along y 12917; contact (13478,12916) on L3 | metal, (13478,13480) south = bd1's k9 |
| s4 | ends on contact (15496,12873); poly west along y 12874; contact (13692,12872) on L8 | metal, (13694,13480) south = bd1's k14 (`hc3`, which bd1 follows west into the mid-right array at y 15020) |
| s5 | ends on contact (15885,12830); poly west along y 12831; contact (14107,12830); metal south on x 14108 | metal, (14108,13480) south (by scan to y 14032) |
| s6 | ends on contact (16276,12786); poly west along y 12787; contact (13780,12786) on L10 | metal, (13782,13480) south; ends on a contact at (13782,13893), poly west along y 13895 (seen, `l11_jog.png`) |
| s7 | ends on contact (16666,12462); poly west along y 12461; contact (15668,12461); metal link down x 15668; contact (15668,12744); poly west along y 12744; contact (14065,12743); metal south on x 14065; contact (14065,13409); poly west along y 13418 under the whole bundle | poly, (13330,13418) going west |

- Two separate poly lines lie on y 12744 (c_s7's, x 14050-15683, and bus s5's, x
  15783-16833) and a third (c_s0's, x 13403-13943); likewise two on y 12831 (c_s5's to
  x 15900, bus s0's from x 16043). The gaps were checked: under the VCC rail at x 15942
  the clean shot is plain field colour, and the metal shot shows no poly edges at
  x 16022 (`tools/rdp3_prof.py`); between x 13950 and 14050 on y 12744 there is no poly
  (`rz_s0.png`).
- **Source of `c_s1`, and of all the c lines.** Run 2 had a poly line from the west
  feeding c_s1: that line is the exit of `h_eq_r1`. Nothing in the region drives any
  c line: all eight come past the top edge and all eight go out at the lower left.
  rdp2 finds no driver north of here either (the lines end at y 9705-10220 after R0's
  comparator). So the c lines are driven from the lower left: they **enter** at the
  eight lower-left ports above, each from the mid-right array or the logic below it
  (bd1 has two of them, `hc3` and `hc0`, coming out of the mid-right array),
  and run north through the comparators of R1, R2 and R0.
- **The track inside the latch cells (was AMB-6): continuous, no contact.** In both
  metal shots the track looks interrupted over the n2 load of every latch cell (AR
  y 13100-13170; only a 5 px bright line at x 14720) and its piece above seems to end on
  the n2 land. Measured in the clean shot, all 21 cells: the field just left of the
  load's gate block (14704,13118) and the load's channel (14724,13118) have protected
  colours (R 205-232 and 227-251; open poly would be about 136/86/60, open field
  157/137/101), and the nearest other metal is 36 px away, so metal lay over the load.
  The n2 land under the track is flat tan in 4 AR cells of 5 (no contact specks; the
  fifth has dirt). The track runs over the edge of the gate block, the edge of the load
  strip and the gate tie, which is why it photographs dark. A break would also leave
  comparator A's c inputs floating, and a contact would tie the n2 nodes of three
  registers together.
  **cdp2 reads the same cell differently**: its "track b" ends on the n2 land with a
  contact and is the latch's n2 output, the metal beyond the load being a separate
  piece. One of the two readings is wrong, or the cells differ in the metal; cdp2's
  ambiguity 2 (the n2 load looks protected "although no metal covers it") is the same
  observation that decides it here.
- In AR's cells s2..s5 the piece of this track inside the cell is an isolated stub: the
  clean shot shows open field above and below the cell at x 14712 + 390 k (and metal
  for s1), `ar1_trk`..`s5_trk`.

## Ports

North edge, y 10700 (all metal, all continue into rdp2):

| Name | x | Direction | What |
|---|---|---|---|
| `db_b7`..`s7` | 13845, 14236, 14626, 15016, 15407, 15797, 16187, 16577 | through | data lines (rdp2: s0's own line ends at y 10567, in row RC) |
| `db_b7` (second branch) | 16838 (drawn to y 10745) | through | bus s0 on the strap track of slice s7; rdp2 follows it north past y 9440 (its `rdp3_t16837`), so this is how bit s0 reaches the upper array |
| `hc7`..`s7` | 13931, 14321, 14712, 15102, 15492, 15882, 16272, 16663 | out (to rdp2's R0 comparator) | lines compared with R1 and R2; rdp2 finds no driver either and has them end at y 9705-10220, so they are driven from the lower left |
| `h_eq_r0half` | 13348 (L0) | in | rdp2's `h_eq_r0half` (its comparator D); goes south, leaves at (13307,12850) |
| `wr_r4` | 13391 (L1) | out (driven from the south) | `wr_r4` going north = rdp2's `wr_r4` |
| `h_eq_r0` | 13434 (L2) | in | **rdp2's `h_eq_r0`: R0 = c**, the end-of-line match; passes through here, leaves south on L1 |
| `h_eq_r2` | 13478 (L3) | **out** | **R2 = c**; rdp2 has it end on a contact at (13475,9705), poly west along y 9705 |
| `rc0` | 13521 (L4) | ? | turns west at y 12397 |
| `rc1` | 13565 (L5) | ? | turns west at y 11920 |
| `rc2` | 13608 (L6) | ? | turns west at y 11440 |
| `rc_eq_r4` | 13651 (L7) | ? | leaves south on L9; rdp2: its top is a contact at (13649,9919), poly bar from L2's upper piece |
| `rc3` | 13694 (L8) | ? | turns west at y 10965 |
| `vss` | 13783 + 390 k (9 rails) | - | |
| `vcc` | 13990 + 390 k (8 rails) | - | |

Inside the region at its top: `wr_r0`, contact (13690,10815) on the west end of
RC's strobe poly (y 10798-10830; the row is rdp2's, the same net as `wr_r0`).

West edge, x 13330 (all poly, going west):

| Name | y | What |
|---|---|---|
| `rc3` | 10965 | from L8 north |
| `rc2` | 11440 | from L6 north |
| `rc1` | 11920 | from L5 north |
| `rc0` | 12397 | from L4 north |
| `h_eq_r0half` | 12789 (metal, stepping to x 13307) | from L0 north |
| `inh_rc` | 12829 (pad at 13328-13364) | to L0 south (`inh_rc`); the pad's poly comes from the west, not followed |
| `hc7` | 13004 | c line of slice s0 |
| `hc6` | 13418 | c line of slice s7 |

South edge, y 13480 (metal unless noted):

| Name | x | bd1's track at y 14700 | What |
|---|---|---|---|
| `inh_rc` | 13347 (L0) | k6 `inh_rc` | |
| `h_eq_r0` | 13391 (L1) | k7 (untraced) | **R0 = c** (`h_eq_r0`), out |
| `h_eq_r1` | 13434 (L2) | k8 (untraced) | **R1 = c**, out |
| `hc2` | 13478 (L3) | k9 (untraced) | |
| `wr_r4` | 13521 (L4) | k10 `wr_r4` | in |
| `hc1` | 13565 (L5) | k11 (partly traced) | |
| `wr_r2` | 13608 (L6) | k12 `wr_r2` | in: RB's load strobe |
| `wr_r0` | 13651 (L7) | k13 `wr_r0` | in: RC's load strobe |
| `hc3` | 13694 (L8) | k14 `hc3` | |
| `rc_eq_r4` | 13738 (L9) | k15 (untraced) | |
| `hc5` | 13782 (L10) | (ends at 13782,13893 on poly going west) | |
| `wr_r1` | 13825 (L11) | jogs to L10 at y 14000: k16 `wr_r1` | in: RA's load strobe |
| `hc0` | 13871 (poly) | by scan: metal x 13868 from y 13630, k17 `hc0` | |
| `hc4` | 14108 | (by scan to y 14032) | |
| `vss` | 13912; 16125 (bending left) | | |
| `vcc` | 13990; 14382..15942 at y 13520 | | into the decode array's VCC bus |
| `ar0_q`..`s4_q` | contacts 15884,13482; 15839,13437; 15884,13392; 15839,13352 (then poly east) | | `ar0`..`ar3` |
| `ar4_q` | poly, 16170,13307 going east | | `ar4` |
| `ar_load` | 16296,13080 going down | | load strobe of row AR (= `ar_load`) |

Lower right, y 12900 (x > 15800):

| Name | Layer | x | What |
|---|---|---|---|
| `db_b7` | poly | 16798 | going south |
| `db_b4`, `s6`, `s7` | metal | 16818, 16862, 16908 | going south: each ends on the output of one of `dlat`'s bus inverters (as does `db_b7` above); none goes further |
| `vcc` | metal | 16262 (diagonal), 16520 | |
| `vss` | metal | 16428, 16690 | |

The strobes' identities rest on bd1's table for y 14700 and on the stretch y 13480-14700
between the two regions, which belongs to no package: checked there with
`tools/rdp3_jogs.py` in both metal shots (no jog on L6 and L7; L11 to L10 at y 14000,
seen) and not drawn.

## Ambiguities

- **AMB-1 (narrowed, see the hold device).** Left open: depletion or enhancement (not
  visible), and the strip's two ends.
- **AMB-3, the strap at x 14886 and the piece at x 14673 ("T2").** Each is a piece of
  metal as long as one cell (strap y 12174-12430 in RA; T2 y 11738-12200) with no
  contact found at either end or along it. In slice s7 the strap track carries bus line
  s0 through bands A and B, so a contact from the strap to the latch's q drain (run 1's
  reading, and cdp2's reading of the same cell in the central datapath, "track c") is
  excluded at least in s7: it would tie bus s0 to bit s7 of RA and RB. In s0..s6 the
  strap is a stub and a contact would change nothing. Measured in run 3: the q drain
  under the strap looks the same in all 16 cells of RA and RB, s7 included (clean shot
  164/148/113, s.d. 15-18; chip-1 metal dim, 106-132), so whatever makes the strap look
  dim and narrow over the q drain (y 12297-12349 in RA) is not a contact: it is there in
  s7 too, where a contact is impossible. T2 lies over the gate of T6 at
  y 12121-12145 and over the VSS-tied band at its lower end; a contact to either was
  looked for at 5x by run 2 and not seen. Both look like unused feed-through tracks of
  the cells.
- **AMB-8, node x to the series pair.** The strip y 11963-11978 meets the band's right
  end at x 14694-14700 exactly under a metal-gap line (dark bar, as over diffusion;
  over field it would be an olive strip). Taken as joined.
- **AMB-9, the same latch cell read differently by cdp2** (see "the track inside the
  latch cells"): here the middle track is continuous with no contact (measured in 21
  cells) and the strap has no contact; cdp2 has the middle track ending on the n2 land
  with a contact and the strap on the q drain with a contact. Not mine to fix; the
  measurement that decides it here is `tools/rdp3_boxstat.py` on the points quoted.
- **AMB-10, a break in `wr_r0`'s line on chip 2** at (13652,12708): a 10 px dark gap
  in the chip-2 metal shot only. Chip 1's metal is unbroken and nothing lies under the
  spot. Taken as dirt or a scratch on that die.
- Settled in run 3 and removed: AMB-4 (the contact at the east end of `ar_load` is at
  (16296,13023), ring with a bright centre and a pad, metal south on x 16296: run 1 had
  it 11 px too far west, `arld.png`), AMB-5 (AR track stubs: s1 runs through, s2..s5 are
  isolated stubs), AMB-6 (track continuous in the latch cells), AMB-7 (T7 is real).

## Not done

- North of y 10700 everything continues into rdp2: in particular where `h_eq_r2`
  goes from (13478,10700) (by scan to about y 9960) and the nine other bundle lines.
- `h_eq_r1` south of y 13480: bd1's track k8, untraced there. By scan the metal on
  x 13434 runs to about y 15139, with a jog between L2 and L3 at y 15126-15136.
- The poly pad of `inh_rc` at (13328-13364,12829): where its poly goes west.
- The stretch y 13480-14700 of the bundle (no package): followed by measurement only.
- AMB-3 (T2 and the strap).
- Which slice is which data bit.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `rc_eq_r4` (lines 297, 381, 415) is `rc_eq_r4` (`eof`): its top is the contact (13650,9925); the
  bar comes from L2's upper piece, which starts at the contact (13433,9665). The contact (13736,12826)
  at the top of L9 is on that path (AMB-036).
