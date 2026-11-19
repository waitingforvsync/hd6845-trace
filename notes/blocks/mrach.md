# mrach: wiring channel right of the counters (x 13040-13425, y 7130-14700)

Traced 2026-11-15 (serial session). File `trace/mrach.txt`; no transistors, wiring only.
With it the full extraction closes fourteen joins between the counters (`mra`), the right
datapath (`rdp2`, `rdp3`) and the strobe channel (`bd1`) by geometry alone.

## How it is built

- Seven metal tracks T0..T6 at x 13087 + 43.4 k, 20 wide. T6 is the right datapath's L0.
- **Poly runs hidden under the metal tracks**, in places for 400-800 px. The chip-2 metal
  shot shows nothing of it; the clean shot shows it as salmon on the pink of the track.
  Any channel like this one has to be read in the clean shot.
- At y 12606-12796 the tracks T2..T6 from the north each step one place west; T1 from the
  north ends on a contact and T6 to the south starts on one (a poly link joins them).
- Views: `chb0..chb4.png` (clean, 1.7x, `tools/strips.py`), `chan0..chan3.png` (metal,
  1.6x), `r0top.png`, `r0top_b.png`, `stair.png`; overlays `chk0.png`, `chk1.png`.

## Tracks, north to south

| Track | Piece | Net | Ends |
|---|---|---|---|
| T0 | y 7130-8727 | `hsw0` | leaves north; contact (13087,8711) on r3's line |
| T0 | y 8822-14690 | `wr_r6` | contact (13086,8836), poly diagonal and north beside T5, leaves east at (13425,8299) = rdp2's RF strobe: **RF is R6**; south = bd1's k0 |
| T1 | y 7130-7380 | `hsw2` | leaves north; contact (13129,7365), poly west and south under T0 to r1's line (y 7748-7769) |
| T1 | y 7417-12586 | `rst_rc` | contact (13129,7431) on the poly from the band above r0; contact (13130,12570), poly south under T1 and east along y 12830 to rdp3's pad under T6 |
| T2 | y 7130-12616, then T1 to 14690 | `wr_r5` | leaves north; bd1's k1 |
| T3 | y 7130-7489 | `hsw1` | leaves north; contact (13215,7474), poly west and south under T2 to r2's line (y 8225-8246) |
| T3 | y 7527-12659, then T2 | `wr_r7` | contact (13217,7541), poly leaves east at (13425,7541) (into rdp1: R7's strobe); bd1's k2 |
| T4 | y 7130-7293 | `hsw3` | leaves north; contact (13259,7278) on r0's line |
| T4 | from x 13327 north, step at y 7368, y to 12707, then T3 | `wr_r3` | leaves north on x 13327; bd1's k3 |
| T5 | y 7571-12745, then T4 | `rc_eq_r6` | contact (13300,7585), poly leaves east at (13425,7585) (into rdp1) |
| T6 | y 9346-9678 | `rc_eq_r4` | "uc = R4" match: from the east at (13425,8343), poly south in the open strip x 13334, contacts (13348,9360) and (13349,9663), poly east again at y 9663 |
| T6 | y 9822-12789, then T5 | `h_eq_r0half` | rdp2's and rdp3's L0; bd1's k5 |
| T6 | y 12816-14690 | `rst_rc` | rdp3's pad and contact (13346,12829); bd1's k6 |

So the four outputs of the 4-bit counter (rows r0-r3), the strobes of R3 and R5 and one
line of `rst_rc`'s net (the band above r0, going west) leave the array **northwards**:
whatever compares the 4-bit counter (R3, the sync widths) is up there.

## Counter outputs (`n1` = master output of each bit)

| Row | Leaves the channel | Goes to |
|---|---|---|
| r0, r1, r2, r3 | north on T4, T1, T3, T0 | not followed |
| r4 | east at (13425,9748), after a diagonal | rdp2: contact (13649,9747) on a piece of L7 going north (rdp2's notes; not drawn there) |
| r5 | steps up 43 px at x 13157, east at (13425,9884) | rdp2's bar "P3" to a contact at (14065,9877), track x 14062 north (not drawn there) |
| r6 | diagonal north-east, north on x 13331, diagonal, east at (13425,9963) | rdp2's bar "P4" to (14105,9965), track x 14105 north (not drawn there) |
| r7 | east at y 10957-10978 | `rc3`: L8 north |
| r8 | east at y 11435-11456 | `rc2`: L6 north |
| r9 | east at y 11912-11933 | `rc1`: L5 north |
| r10 | east at y 12389-12410 | `rc0`: L4 north |
| r11 | north at the cell's edge, east at y 12995-13013 | `hc7` |
| r12 | north beside T0, east at y 13408-13425 | `hc6` |
| r13 | north beside T0, east at (13425,13893) | rdp3's `c_s6` line ends on a poly at (13782,13893) (not drawn between) |
| r14 | diagonal up to the east, (13425,14212) | rdp3's `c_s5` (x 14108, by scan) (not drawn between) |
| r15, r16, r18 | (bd1) | `hc3` = `c_s4`, `hc2` = `c_s3`, `hc0` = `c_s1` |
| r17 | (bd1, not found yet) | expected `c_s2` on k11 |

**The 8-bit counter (rows r11-r18) is the horizontal character counter**: its master
outputs are the `c` lines that the R0, R1 and R2 comparators use. Bit order (carry enters
at r18): bit 0 = r18 = slice s1, bit 1 = r17 = s2 (expected), bit 2 = r16 = s3, bit 3 =
r15 = s4, bit 4 = r14 = s5, bit 5 = r13 = s6, bit 6 = r12 = s7, bit 7 = r11 = s0. So in
the right datapath slices s1..s7 are bits 0..6 and s0 is bit 7, which is what rdp2's
"c against R0 shifted by one slice" comparator needs to be a compare with R0/2.

The 7-bit counter (rows r4-r10, carry in at r10) goes to the upper array of the right
datapath, which compares it with R4 and R6: the character-row counter.

## Other lines through the channel

| Line | Path | What |
|---|---|---|
| bus A | from (13030,9187) by a staircase to (13425,9406) | from the routing channel between r3 and r4; not identified |
| bus B | from (13030,9231), south in the open strip, staircase, to (13425,9447) | not identified |
| bus F | from (13425,9707) by a diagonal to (13030,9381) and on west | the R2 match line `h_eq_r2` (rdp2's notes: contact (13475,9705) on L3); not drawn between x 13425 and the contact |

## Not done

- East of x 13425 at y 7541 and 7585 (rdp1), y 9406, 9447, 9707, 9748, 9884, 9963 (rdp2's
  bundle and s0 column, "seen, not drawn" there), y 13893 and 14212 (the stretch between
  rdp3 and bd1).
- North of y 7130: where T0, T1, T3, T4 (4-bit counter), T2 (`wr_r5`) and x 13327
  (`wr_r3`) go.
- The z stubs: in every row the poly of net `z` ends free about 12 px east of the rail. In
  no row of this channel does it go on.
- Row r17's output, and the lower channel y 14700-17000 beyond what bd1 drew.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- T6's row "poly east again at y 9663": drawn by `eof`: it is `rc_eq_r4`, on to `bd1`'s latch.
