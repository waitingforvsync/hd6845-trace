# hcj: the horizontal counter lines hc0..hc5 from the counter to the comparators' c lines (x 13040-14130, y 13470-15990)

## Status

Traced 2026-11-17 09:48 (one agent, one pass with a numeric cross-check and overlays). File
`trace/hcj.txt`: metal tracks, three poly runs, four contacts; no transistors, no
uncertain items. Full extraction: 2039 nets (7 fewer: seven names merged), 3430
transistors, 0 errors, 0 warnings.

**All six joins come out as expected**: rdp3's six c-track nets are the counter's
`hc0` .. `hc5` (bd1's tracks k17, k9, k14 for bits 0, 2, 3; the wiring channel's
polys for bits 4 and 5; the counter row r17's poly, through bd1's track k11, for bit 1).
bd1's track k11 is `hc1`, as mrach expected. So the comparator c tracks of the
right datapath slices s1..s6 are the master outputs of counter rows r18, r17, r16, r15, r14,
r13 by drawn geometry. `tools/unsure.py` lists none of hc0, hc1, hc3, hc4, hc5; `hc2` is
listed as before for bd1's `?` poly from k9 into the mid-right array (not touched here):
the piece joined here (rdp3's c track to bd1's k9 metal) is one firm piece.

Before drawing: each of rdp3's two label sets (c track at y 11650, bundle track at
y 13400-13478) was already one net per bit in rdp3's own geometry (same net id).

The open-join names were renamed with `tools/rename.py` in 6e14273.

## Routes

| Line | From (rdp3) | Route | To | Evidence |
|---|---|---|---|---|
| `hc0` | poly (13871,13480) going south | poly x 13861-13881 to a pad, contact (13868,13632); metal south on x 13868; arm west along y 14041-14059; south on x 13825 (L11's position) | bd1's k17 (13826,14690) | `hc0_top.png`, `hc0_arm.png` (4x, both chips and acid1b) |
| `hc1` | L5 (13565,13480) | straight on x 13565 | bd1's k11 (13565,14690), then bd1's own metal: arm east at y 15005 onto x 13608, south to the pad (13608,15608); poly from the pad west along y 15620-15640, south-west from x 13454 to (13111,15973), west along y 15964-15986 to the counter's poly end at x 13053 | surveys; `k11_jog.png`, `k11_pad.png` (4x), `hc1_sv_metal.png`, `hc1_sv_acid1b.png` (2x), `hc1_p1.png`..`hc1_p3.png` (3x), `hc1_west.png` (4x), overlay `ov_hc1.png` |
| `hc2` | L3 (13478,13480) | straight on x 13478 | bd1's k9 (13478,14690) | surveys; crossings on `hc5_poly.png`, `hc4_diag.png` |
| `hc3` | L8 (13694,13480) | straight on x 13694 | bd1's k14 (13694,14690) | surveys; crossings on `hc5_poly.png`, `hc4_band.png` |
| `hc4` | metal (14108,13480) | x 14108 south to a pad, contact (14105,14022); poly west along y 14014-14035 under the vcc and vss rails, hc0's metal and the bundle; south-west from x 13612 | mrach's poly end (13425,14212) (row r14) | `hc4_ct.png` (4x), `hc4_band.png` (2.7x, three shots), `hc4_diag.png` |
| `hc5` | L10 (13782,13480) | x 13782 south to a pad, contact (13782,13893); poly west along y 13884-13902 under L9..L2 | mrach's poly end (13425,13893) (row r13) | `hc5_ct.png` (4x), `hc5_poly.png` (3x, three shots) |

Images are in `cache/scratch/hcj/`. Surveys at 1.6x: `sv_metal_a.png`, `sv_acid1b_a.png`
(y 13440-14120), `sv_metal_b.png`, `sv_acid1b_b.png` (y 14060-14740); overlay `ov_a.png`.

Numeric cross-check (`tools/hcj_prof.py`, the metal test of `follow.py` on a 7 px
column, both chips), so that no jog can hide between views:

- Down the gaps between tracks (x 13456, 13500, 13543, 13586, 13672, 13716, 13760, 13804,
  13847, 14085, 14131; y 13440-14710) chip 1 has no metal at all except wr_r1's arm
  (x 13804, y 13999-14007) and hc0's arm (x 13847, y 14041-14053). Chip 2 has the same two
  plus speckle (runs of 4-16 px). At x 13890 chip 2 shows the edge of rdp3's vss block
  (y 13485-13592), which lies beside hc0's poly, not its metal.
- Along the tracks: x 13478, 13565, 13694 have no non-metal run over 20 px from y 13440 to
  14710; x 13782 has none from 13480 to 13873, then none of metal to 13986; x 13868 is
  metal from y 13630 to 14052 only; x 13825 has no metal from y 14008 to 14041; x 14108 is
  metal down to y 14003 (chip 1) / 14029 (chip 2: the pad).
- For bd1's k11: x 13565 has no metal from y 15008 to 15191 (below that it is rst_a_n's
  metal), x 13608 none from 14961 to 14995 (between k12's pad and k11's arm) and no run
  over 19 px from there to the pad at y 15585; the gap columns x 13586 and x 13630 are
  empty on chip 1 except the arm (y 14997-15006).

Where two nets come close: hc0's arm (top edge y 14041) and wr_r1's arm (bottom edge
y 14010) with hc4's poly band between them (`hc0_arm.png`); k11's arm and the ring of
k12's pad, 18 px (`k11_jog.png`); hc5's pad (to x 13800) and L11 (from x 13816).

Crossings without contact (looked at, no pad or ring on the metal, poly plain in acid1b):
hc5's poly under L2..L9; hc4's band under vcc, vss, x 13868 (hc0), x 13782 (wr_r1), L9..L6;
hc4's diagonal under L5 (hc1), L4, L3 (hc2), L2; hc1's poly under x 13565 (rst_a_n), 13521,
13478 and the nine tracks x 13435..13131 (the last is hc0's metal). The dark rings on
these polys in `acid1b` all sit in the gaps between tracks (guide trap 2).

## Ambiguities

None left open on the six joins. Two things that were looked at twice:

- k11 on x 13565 where it crosses hc3's poly (y 14897-14928): chip 2 fails the metal test
  for 32 px (a dark spot at (13562,14910)), chip 1 fails it for about 30 of 33 px too. Both
  metal shots show a bright metal square between the two dark poly-edge lines, as on the
  neighbouring tracks, with no ring and no metal ends (independent review, 6x); `acid1b` shows the poly under the track in its metal-protected
  colour, with the gap rings either side, and no pad. Read as continuous metal with dirt;
  a break there would need two metal ends without contacts.
- Chip 2 reads as metal in the gap columns at x 13586 (y 15402-15410, 15419-15428,
  15486-15495, 15508-15544) and x 13630 (y 15418-15436); chip 1 has nothing there and the
  views show bare ground with speckle (`k11_pad.png`; review `k11_low.png`).

## Other blocks

- `trace/bd1.txt`: the pad and contact at the foot of k11 lose their `?` (own commit,
  ee37967); the pad is taller than bd1 drew it (to y 15642), drawn here.
- The open-join names are renamed with `tools/rename.py` in the commit after the drawing
  (rdp3, bd1, wrj, the glossary, work-packages).
- `notes/blocks/mrach.md` (rows r13, r14, r17 "not drawn between" / "not found yet") and
  `notes/blocks/rdp3.md`'s south-edge table (`hc4` "by scan to y 14032": it ends on the
  contact (14105,14022); `hc0`'s contact is at (13868,13632)) are not updated here.

## Review

Independently reviewed (2026-11-17) with a swapped counter bit or a bridged jog as the
main suspicion: all six routes, the k11 crossing, the row identities of mrach's r13, r14
and r17 (by geometry; the bit order itself is mra's) confirmed. Its wording fixes are in.

## Not done

- L9 (x 13738, rdp3's `rc_eq_r4` to bd1's `rc_eq_r4`): straight and unbroken in the same
  views and profiles as wrj reported, not drawn (not this package).
- L0..L2 (x 13348-13434: `rst_rc`, rdp3's `h_eq_r0` / `h_eq_r1` to bd1's k7 / k8):
  seen straight on the surveys, not profiled, not drawn.
- bd1's `?` poly of `hc2` from k9's contact (13520,15390) into the mid-right array: not
  re-read.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- Not done, L9: drawn by `eof` (piece `r4`), as part of `rc_eq_r4`.
