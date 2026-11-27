# rdp2: right datapath, middle rows

Region: x 13350-16950, y 8100-10700. Trace: `trace/rdp2.txt` (`@requires rdp3`).
Scratch: `cache/scratch/rdp2/`. No own tools; `tools/rdp3_cmp.py` and
`tools/rdp3_strips.py` did the comparing and line following.

**Slice tags and array columns.** Tags are rdp3's: s0..s7 from the left, pitch 390. The
cells of slice sK lie between the VSS rail at x 13783 + 390 K (left edge; the slice's own
pull-downs use the land under this rail) and the one at x 14174 + 390 K. Taking a column's
rail to be the one at its left edge, **sK = column c(K-1)**: s1..s7 are c0..c6 (rails
x 14174..16516), **s0 lies one pitch left of c0** (rail x 13783), and c7 (rail x 16906,
the ninth rail) has no cells in the rows traced here.
The **upper array** (y 8048-9080) has seven slices one place further left: tag `sm1`
(cells between the rails x 13393 and 13783, two pitches left of c0), then s0..s5 at the
same x as the lower array's s0..s5 (so its columns are c-2..c4).
Believed bit order of the lower array (see Logic, comparator D): s1..s7 = bits 0..6,
s0 = bit 7, i.e. column cN = bit N and bit 7 sits left of c0. The upper array's bit
order is not known.

## Status

- Lower array, traced, placed, every instance checked: register row RC (8 latches) =
  **R0**; comparator C above it (8 XORs, wired NOR) = "c = R0"; comparator D above that
  (7 XORs, wired NOR), which compares c of each slice with the R0 bit of the next slice
  = "c = R0 shifted by one bit"; the wiring between them; both equality lines out to
  bundle tracks at the left edge; R0 bit 7's line round the array.
- Upper array, cells placed and checked: register row RE (7 latches) = **R4** (strobe
  traced to track L1, which rdp3 follows to `wr_r4`); comparator E above it (7 XORs,
  wired NOR; output leaves west in poly at y 8339); register row RF (7 latches; strobe
  leaves west in poly at y 8295, register not identified; its comparator is in rdp1).
  The upper array's c lines and data lines are drawn only through these rows.
- 311 transistors of this block; extracts with no errors and no open nets.
- **Nothing in this block drives the lower `c` lines.** Each c track ends at its topmost
  comparator contact (s1..s7 at y 9723 in comparator D, s0 at y 10244 in comparator C).
  They are fed from rdp3's side (routing zone below row RA).
- Not traced: the routing zone y 9080-9560 between the arrays (where the upper array's
  c lines and data lines go), the other lines of the s0 column and of the left bundle,
  x 16160-16950 at y 8100-9440 (a bundle of vertical lines).

## Inventory

Per slice sK (x for s2; add 390 per slice), as in rdp3: VSS rail 14565, bus 14626, T2
track 14673, c track 14712, VCC rail 14772, strap track 14886 (in s7 a through line,
x 16838).

| y | What |
|---|---|
| 8048-8318 | **register row RF**, slices sm1, s0..s5: `rdp3_lat` upside down; strobe poly y 8285-8313 |
| 8318-8415 | gap: RF's strobe going west (y 8287-8303), comparator E's exit line (y 8331-8347), rounded top ends of the T2 pieces (y 8377) |
| 8415-8806 | **comparator E**, slices sm1, s0..s5: `rdp3_mpd1` (sm1, with the load) / `rdp3_mpd` at y 8415-8544, `rdp2_xor` at y 8544-8806 |
| 8807-9077 | **register row RE = R4**, same slices: `rdp3_lat` upside down; strobe poly y 9044-9072 |
| 9080-9560 | routing zone: many horizontal poly lines; seen only at 0.35x except the lines traced (R0 bit 7 at y 9480-9494, comparator D's exit at y 9523-9541, RE's strobe at x 13385-13403) |
| 9563-9954 | **comparator D**, slices s1..s7: `rdp3_mpd1` (s1, with the load) / `rdp3_mpd` at y 9563-9692, `rdp2_xor` at y 9692-9954 |
| 9440-10084, x 13800-14180 | s0 has no comparator D cell: routing column (poly bars from the bundle to tracks going north), see Not done |
| 9954-10084 | gap: T2 top contacts (y 10010) and poly bars to the XORs of comparator D; exit line of comparator C (y 10000-10021, s0) |
| 10084-10475 | **comparator C**, slices s0..s7: `rdp3_mpd1` (s0, with the load) / `rdp3_mpd` at y 10084-10213, `rdp2_xor` at y 10213-10475 |
| 10475-10564 | gap: q of RC up into the XORs, bar and contact to the T2 track (y 10529) |
| 10564-10834 | **register row RC = R0**: `rdp3_lat` upside down, eight copies; strobe poly y 10801-10829 |

Left of the lower array, x 13348-13782: the bundle L0..L8 (x 13348 + 43.4 k), continued
from rdp3. Top ends of its lines inside this region are under Not done. The upper
array's leftmost VSS rail (x 13393, 56 wide) ends at y 9275; the thin track below it on
the same x is L1.

Upper array, x per slice (sm1; add 390 per slice): VSS rail 13393, data line 13455, T2
piece 13501, c track 13541, VCC rail 13600, strap track 13714 (in sm1 a through line).
Right of the upper array, x 16160-16950, y 8100-9440: vertical metal lines (not looked
at).

## Logic

### Row RC = R0 (traced)

`@inst rdp3_lat` at dx -781, -391, 0, 390, 780, 1170, 1561, 1951, dy -2456 (rdp3's mirror
and rotation). Compared copy by copy with row RB (`rdp3_cmp`, offset 0,-757): identical
except the top edge, where q leaves. Per bit, as rdp3: `a <- bus` while the strobe is
high, `n2 = NOT a`, `q = NOT n2`, weak hold device q -> a. q is in the sense of the bus.

- Bus lines `db_b7..s7` (one contact per cell, y 10809). s0's bus line ends at the
  top of its RC cell (y 10567); the others run on north through both comparators with no
  contact.
- **Strobe: `wr_r0`, so RC is R0.** The row poly runs west under the first
  VSS rail to a pad with a contact at (13690,10815) on bundle track L8 (x 13694), metal
  south. Followed outside the region: L8 straight to y 12400, there one step left onto
  x 13652 (both metal shots, `jog.png`: the three tracks L6, L7, L8 each step one place
  left at y 12310, 12355, 12400), straight on to the contact at (13652,15000)
  (`l8_a.png`, `l8_b.png`, `l8_c.png`), which sel and bd1 give as `wr_r0`. rdp3's run 3
  found the same independently and draws pad, contact and track (its file names the net).
  By the same staircase RB's strobe (contact 13648,11571 on x 13652) lands on x 13608 =
  `wr_r2`: rdp3's earlier "RB = R0" came from a track scan that bridged the 25 px
  between the two steps.

### XOR cell `rdp2_xor` (rdp3's cell, traced there)

Text copy of `rdp3_xor` less its metal piece on the T2 track, which is absent in
comparator D and in s1 of comparator C and is a real wire elsewhere in C. Master at
comparator C, slice s2.

```
nor = NOR(c, q)          x = NOT(nor + c.q) = c XOR q
```

c from the slice's c track (contacts at y 10244 and 10429 in C; 9723 and 9908 in D); q in
poly from below at x 14879-14901 (s2).

### Comparator C (traced): c = R0

```
r0c_bK_x = c_sK XOR R0_sK        K = 0..7
h_eq_r0   = NOR(r0c_b7_x .. r0c_b6_x)      high when the eight c lines equal R0
```

- The cells are band A's moved by (dx,-1692/-1691); all eight XORs and the seven plain
  pull-downs compared with the median of bands A, C, D by `rdp3_cmp`: no difference
  except where a metal line is missing (s1 has no T2 track, s0 no bus line here).
- The load of the eq line (`rdp3_mpd1`) is in **s0** (rdp3's bands have it in s1).
- q of each RC cell comes up in poly through the 89 px gap (x 14879-14901, y 10500-10600)
  into the XOR.
- eq strip: diffusion y 10084-10106, x 13768-16925. **Exit** (`eqc_left.png`,
  `c_s0_top.png`, `eqc_tab.png`): a tab comes up at x 13924-13946, buried contact
  (13922-13948 x 10052-10074) onto poly that goes up to y 10000-10021 and west under the
  first VSS rail and the bundle to a pad with a contact at (13434,10012) on **track L2**;
  metal south. rdp3 draws L2 on from y 10700 as `h_eq_r0` (jog onto L1 at y 12486, bd1's
  k7 at y 13480).

### Comparator D (traced): c against R0 shifted one slice

```
r0hc_sK_x = c_sK XOR R0_s(K+1)    K = 1..6
r0hc_s7_x = c_s7 XOR R0_s0
h_eq_r0half   = NOR(r0hc_s1_x .. r0hc_s7_x)
```

- Seven slices, s1..s7; cells are band A's moved by (dx,-2213/-2212), compared as above:
  differences only on the T2 and c track columns, where the metal is absent.
- The load of the eq line is in s1. Right end as in rdp3's bands (VSS lands under the
  ninth rail; seen at 1.3x and 2x).
- **Where q comes from** (`gap1_s2.png`, `gap2_s2.png`, `bar1_*.png`, `bar2_*.png`,
  `ov_mid.png`): in the gap under comparator C a poly bar (y 10520-10538) takes q of RC
  left to a pad with a contact (y 10529) on the slice's T2 track. The track runs up
  through comparator C and ends on a contact at y 10010; from that pad a poly bar
  (y 10001-10019) runs left, under the VSS rail, and turns up into the q input of the
  XOR of the slice to the **left**. Slices s2..s7 have this; s1 has no T2 track and no
  bar (R0_s1 goes only to comparator C).
- **s0's bit goes round the array** (`s0_d.png`, `t2s0_top.png`, `q0_strips_*.png`,
  `hq_0..2.png`, `east2a/b.png`, `ov_right.png`): s0's T2 track runs on up to a pad at
  (13910,9708); poly north (x 13911-13924) to y 9480, east along y 9480-9494 under every
  rail and track of the array, south at x 16946-16964 (right of the ninth rail) to
  y 10020, west along y 10000-10020 under the ninth rail into the q input of s7's XOR.
- eq strip: diffusion y 9563-9585, x 14158-16925. **Exit** (`eqd_exit.png`,
  `eqd_tab.png`, `ov_s0s1.png`, `pads_l0l2.png`): in s1 a tab of the strip comes up into a
  buried-contact box (14308-14347 x 9518-9560) on the east end of a poly line: west along
  y 9523-9541 to x 13950, south (x 13950-13963) to y 9845, west along y 9828-9845 to a
  pad with a contact at (13346,9837) on **track L0**; metal south. rdp3 draws L0 on from
  y 10700 as `h_eq_r0half` (straight to y 12789, steps left to x 13307, leaves at 13307,12850).

Believed: the pairing is a one-bit shift, so the bits ascend s1, s2, .., s7, s0, and
`h_eq_r0half` is "c[6:0] = R0[7:1]", i.e. c = R0/2 with **bit 7 of c (slice s0) not
compared**. This fits the CPC document's "VSYNC on C0 = R0/2" for interlace and rdp3's
guess that the address register (slices s1..s5) takes D0..D4. If c is the horizontal
counter, `h_eq_r0` is end of line. Not traced: which slice is which data bit.

### Upper array: rows RE = R4 and RF, comparator E (traced)

All three rows are rdp3's cells unchanged, seven slices (sm1, s0..s5). Checked with
`rdp3_cmp` against row RB and band A: no difference except at the row ends; overlays
`ov_upmid.png`, `ov_upleft.png`, `up_right.png`, `ov_rf_right.png`.

```
RE:  a <- ubus_sK while wr_r4;  q = a (two inverters, hold device)
RF:  a <- ubus_sK while wr_r6;  q = a
r4c_sK_x = uc_sK XOR q(RE, K)        K = sm1, s0..s5
rc_eq_r4  = NOR(the seven x)              high when the seven uc lines equal RE
```

- **RE's strobe = track L1 = `wr_r4`, so RE is R4** (vertical total, 7 bits). At the
  foot of sm1's loop the row poly steps left and runs south under the VSS rail
  (x 13385-13403) to a pad with a contact at (13391,9311) just below the rail's end;
  thin metal south on L1, straight to y 10700 (`re_ld2.png`, `re_s_c.png`,
  `re_s_m.png`; the crossings at y 9650-9760 checked in both metal shots, `l1_x.png`).
  rdp3 follows L1 from there to `wr_r4`.
- RF's strobe: from the foot of sm1's loop the poly goes west along y 8287-8303 and
  leaves the region (`rf_ld.png`). Not identified. RF's q lines go up in poly into the
  comparator above it (rdp1).
- Comparator E's load is in sm1. Exit as comparator C's (`eqe_exit.png`): tab at
  x 13535-13557, buried contact, poly up and west along y 8331-8347 under the rail
  x 13393, out of the region. The c track of sm1 passes over the buried contact without
  touching it (rdp3 settled this for the same structure in its bands; in comparator C
  the box has no metal over it at all).
- Both registers hang on the same seven data lines `ubus_sK` and comparator E on
  the seven lines `uc_sK`; all of these go on north (RF's comparator) and south
  (routing zone), untraced. Believed: `uc` is the vertical (character row) counter and
  `rc_eq_r4` is "row counter = R4".
- sm1 has a thin through line on its strap track (x 13714), as s7 has in the lower
  array (x 16838).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `db_b0`..`s7` | metal | x 14236, 14626, 15016, 15407, 15797, 16187, 16577 at y 9540, going north | through | data lines; drawn to y 9540, they go on north (track scan: to about y 9480 and beyond in places) |
| `db_b7` | metal | ends at (13845,10567) | - | top end of s0's data line |
| `hc7`..`s7` | metal | joined to rdp3's at y 10700 (x 13931, 14321, 14712, 15102, 15492, 15882, 16272, 16663) | in | compared with R0; not driven here; top ends y 10220 (s0), 9705 (others) |
| `wr_r0` | poly | (13750,10815) going west to rdp3's pad | in | R0 load strobe = `wr_r0` |
| `h_eq_r0` (= `h_eq_r0`) | metal | 13434,10700 going south (track L2) | out | high when c = R0 |
| `h_eq_r0half` (= `h_eq_r0half`) | metal | 13348,10700 going south (track L0) | out | high when c_s1..s7 = R0_s2..s7,s0 |
| `rdp3_t16837` | metal | 16838,9440 going north | through | thin line on s7's strap track, no contact seen in comparators C, D or row RC |
| `wr_r4` | metal | 13391,10700 going south (track L1) | in | R4 load strobe = `wr_r4` |
| `wr_r6` | poly | 13340,8295 going west | in | RF load strobe, not identified |
| `rc_eq_r4` | poly | 13340,8339 going west | out | high when uc = R4 |
| `db_b0`, `_s0`..`_s5` | metal | x 13455, 13845, 14236, 14626, 15016, 15407, 15797; north at y 8051, south at y 9075 | through | data lines of the upper array |
| `rc0`, `_s0`..`_s5` | metal | x 13541, 13931, 14321, 14712, 15102, 15492, 15882; north at y 8051, south at y 9075 | in | compared with R4 (and by rdp1's comparator with RF) |
| `r6_b0_q`, `_s0_q`..`_s5_q` | poly | x 13707, 14097, 14487, 14878, 15268, 15658, 16048 (22 wide) at y 8048 going north | out | RF's bits, into rdp1's comparator |
| `rdp2_t13714` | metal | 13714,8051 north; 13714,9075 south | through | thin line on sm1's strap track |
| `vss` | metal | x 13393, 13783, 14174, .., 16125 (8) at y 8040 going north; x 16516, 16906 at y 9540 going north | - | rails. x 13393 ends at y 9275; x 13783 is cut at y 9100-9400 (AMB-5) |
| `vcc` | metal | x 13600, 13990, .., 15942 (7) at y 8040 going north; x 16332, 16723 at y 9540 going north | - | rails. x 13600 is drawn to y 9080 only (AMB-5) |

`r0_b7_q` (R0 bit of slice s0) leaves the region for 14 px at (16950-16964, 9480 to
10020) and comes back; nothing else is on it out there as far as seen (`east1.png`).

## Ambiguities

- **Correction to rdp3 run 2 (already made by its run 3):** RB is R2, not R0; R0 is RC.
  The alias in `trace/zz_joins.txt` that joined R0's strobe to R2's piece was wrong and
  has been removed (its comment there records it).
- **AMB-1, buried contact of comparator D's exit** (14308-14347 x 9518-9560). Larger than
  the ones in the other three bands (38 x 40 against 26 x 22) and the poly reaches it
  straight from the west instead of from above. No metal over it in either metal shot,
  heavy outline, lighter inside, directly on the tab above the strip: read as a buried
  contact. If it were not one, comparator D's line would have no exit.
- **AMB-2, right-end VSS lands** of both comparators (16886-16940 x 10398-10475 and
  x 9877-9954) and of RC (16878-16926 x 10659-10744): placed where rdp3's bands have
  them; seen as tan areas with contact specks at 1.3x and 2x, not at tracing zoom.
- **AMB-3, the through line x 16838** lies over the q input poly of s7's XORs for its
  whole length. No contact ring seen at 2x (`ov_right.png`); not looked at closer.
- **AMB-4, RF's right-end VSS land** (16097-16145 x 8143-8228, `?D`, `?C`): placed as
  RE's (which was seen at 1.35x with its contact speck); seen at 1.4x only.
- **AMB-5, rails between the arrays** (`rz_l.png`, `rz_r.png`, 0.9x). The rails
  x 14174..16125 (VSS) and 13990..15942 (VCC) run straight through y 9080-9540 and are
  drawn so. Not drawn, because seen only at 0.9x: the upper array's VCC rail x 13600
  turns east in a wide strap at about y 9140-9190 and joins the rail x 13990; the VSS
  rail x 13783 is cut by that strap (upper piece drawn to y 9100, lower piece from
  y 9400); the lower piece appears to be fed by a wide horizontal piece at about
  y 9250-9290 from the foot of the rail x 13393. Each piece is labelled by what its
  cells' lands and loads use.
- Inherited from rdp3's cells: its AMB-1 (hold device), AMB-7 (T7's diffusion, `?D`),
  AMB-8.

## Not done

- **Routing zone y 9080-9560.** Here the upper array's data lines and c lines end on
  contacts to horizontal poly lines (about twelve, y 9130-9450), and the lower array's
  data lines begin. Needed to know which upper slice is which bit, how the two sets of
  data lines are joined, and where `uc` comes from. Seen at 0.9x only (`rz_l.png`,
  `rz_r.png`). Track scan (metal present, y): upper c tracks end at about 9176 (s0),
  9218 (s1), 9242 (s2), 9196 (s3), 9153 (s4), 9108 (s5); upper data lines at 9370 (s0),
  9055 (s1), 9285 (s2), 9241 (s3), 9196 (s4), 9055 (s5); lower data lines start at
  about 9481 (s1), 9480 (s2), 9394 (s3), 9352 (s4), 9309 (s5), 9264 (s6), 9093 (s7).
  Two extra tracks come down into the s0 column: x 14062 (top contact about 14061,9172)
  and x 14105 (about 14109,9220).
- RF's comparator and everything above y 8048 (rdp1).
- x 16160-16950, y 8100-9440: vertical metal lines right of the upper array.
- **s0 routing column, x 13800-14180, y 9440-10084** (`s0_d.png`, `bundle1.png`,
  `ov_s0s1.png`). Poly bars come in from the west under the first VSS rail; seen, not
  drawn:
  - y 9612-9630: from a contact at (13563,9616) on L5's top end to a pad with a contact
    at (13850,9620); metal hooks right and goes north on the T2 track position
    (x 13890; track scan: metal y 9398-9629).
  - y 9872-9888 ("P3"): from west of x 13330 to a pad with a contact at (14065,9877);
    metal north on a track at x 14062.
  - y 9958-9975 ("P4"): from the south-west (diagonal at x 13330-13405) to a pad with a
    contact at (14105,9965); metal north on the strap track x 14105 (scan: y 9264-9952).
  - a bar at y 9573 from a contact at about (13455,9573) east through the column;
    a bar at y 9525 from L6's top contact (13607,9528) east to x 13786, then north.
- **Left bundle, x 13330-13782, y 9440-10700**: only L0 and L2 south of their pads are
  drawn. Seen at 1.28x (`bundle1.png`), coordinates approximate: L3 (`h_eq_r2`) ends on
  a contact at (13475,9705), poly west along y 9705; L2's piece from the north ends at
  (13433,9922), poly bar y 9915-9932 east to a contact at (13649,9919), which is the top
  of L7 south (`rc_eq_r4`); L7's piece y 9593-9733 ends on a contact at (13649,9747),
  poly west along y 9745; L8's top contact at (13691,9485); L0's upper piece
  (y 9396-9646) and L2's top end share a poly bar at y 9661 that goes west. Track scan of
  all twelve (gap 8) is in the run's log, not kept.
- The upper pad (13692,10748) on L8 is in rdp3's file (`rc3`).
- Which slice is which data bit (needs the data bus followed to the D pads).

## Corrections (coordinator, from the handoffs of 2026-11-19)

- Not done, the left bundle's L2 piece and the bar to L7: drawn by `eof` (piece `r4`), as `rc_eq_r4`.
