# eofw: the wires of `eof`'s gate `g7700` beyond `eof`'s ports

End-of-frame lead group. Three wires, not a region (they run through x 6330-7860, y 6390-8810: the
ground of `busl`'s northern part, `lc1`, `cdp2` and `cdp3`, which keep everything else there).
Geometry: `trace/eofw.txt`. Ports: `ports.d/eofw.txt`. Coordinates are metal-shot pixels.

## Status

Run 1 (richtw1's session, Claude Fable 5.2; 2026-11-19 14:47 to 15:45 +0100). Wiring only, no
transistor, no uncertain item. **Done**: each of the three wires that `eof`'s piece `g7700` left at a
port is followed to a net another package drew.

- **The gate on `inh_ck`'s tap row is now named on every side** (`eof`'s gate, x 7541-7775,
  y 7585-7860):

  ```
  tc2_r5589 = NOT( lc1_w7170 AND ( inh_ck OR tc2_sr_g ) )
  ```

  with `eof_w7818` = `tc2_r5589` (the output), `eof_w7718` = `tc2_sr_g` = `lc1_w7908` (row 2) and
  `eof_w7777` = `lc2_w8474` = `lc1_w7170` (row 3).
- **`tc2_sr_g` and `lc1_w7908` are one net**: the gate line of `tc2`'s latch (`tc2_sr_q`,
  `tc2_sr_q_n`) is the enable of latch D, the latch that makes `lc_step`.
- Two open ends are left, both at a corner pad (7446,8732) on the same net, leading into `cdp3`
  (continue)'s ground (Not done).

How this came about: a test of method asked for by the user. `eof`'s piece `g7700` had been traced
in a 15-minute run; the gate was traced again, from the commit before that run and without sight of
it, by a fresh agent told to take all the care the piece deserved (39 minutes). The two traces of the
gate agree in every connection (the same four transistors and equation; drawn together they merge
net for net with no short; coordinates within 4 px). The second went on along each wire, and that
part is this package. `eof`'s geometry is not changed.

Extraction: the package by itself 4 nets, 0 transistors, 0 errors, 0 warnings. Every package:
2,395 nets (four fewer than without it: the four joins), 4,344 transistors, 0 errors, 0 warnings.
`tools/unsure.py`: 0 nets joined only through uncertain items in this package.

## Inventory

| Wire | From (`eof`'s end) | Path | To |
|---|---|---|---|
| Y, the output | `eof`'s poly north of the pad (7272,6912), x 7266-7286 | poly north to y 6870; west along y 6861-6879 (430 px, in the open); a corner (6843,6870); north at x 6834-6852 under eleven bus metals, no pad (465 px) | `tc2`'s poly `P 6843,6282 y6400` (`tc2_r5589`) |
| 2, north branch | `eof`'s poly row y 7204-7225 east of the pad (7313,7215), at x 7400 | the row east under `bw`'s metals x 7410-7432 and 7456-7478, a metal x 7520-7540, the VSS rail (x 7572-7620) and the VCC rail (x 7725-7775), no pad; a pad with a contact (7836,7215); metal x 7829-7843 north (820 px) | `tc2`'s metal `M ... x7837 y6400` (`tc2_sr_g`) |
| 2, south branch | `eof`'s metal south of row 2's pad (7267,7736), x 7266-7280 | metal south to a T (7273,8710) on a horizontal metal y 8703-8716; west of the T a staircase: (7190,8710), (7190,8672), (7060,8672), (7060,8585), (6883,8585), (6883,8498), (6710,8498), (6710,8411), (6515,8411), (6515,8259), west | `lc2`'s metal `M 6212,8067 y8259 x6450` (`lc1_w7908`) |
| 2, east of the T | the T (7273,8710) | metal y 8703-8715 east to a corner pad x 7426-7476, y 8703-8750 with a contact (7446,8732) on a poly pad x 7428-7482, y 8716-8750 | two open ends: the poly on east at (7490,8722-8745); the metal on south at (7458-7474,8800) |
| 3 | `eof`'s poly row y 7812-7832 at `lc1`'s edge x 6450 | the row west (110 px); a pad with a contact (6339,7824); metal x 6333-6349 south (245 px) | `lc2`'s metal `M 6341,8067 y8228` (`lc2_w8474`, the pad (6341,8214)) |

## Logic

No transistor. Traced: the four joins, each by one drawn wire with no `?` item, and with them the
gate's equation in the names above.

- `tools/unsure.py --equations tc2_r5589`: **DEPENDS**, "without ?: NOT((eof_w7777 & inh_ck) |
  (eof_w7777 & tc2_sr_g))". The gate and the joins to `tc2_r5589`, `tc2_sr_g` and `lc2_w8474` are
  firm; only the *name* `lc1_w7170` for row 3's net depends on uncertain items, and they are `lc2`'s
  (`trace/lc2.txt` aliases `lc2_w8474` to `lc1_w7170` across `?` geometry of its staircase).
- With `inh_ck` high the output is NOT `lc1_w7170`; with it low, NAND(`lc1_w7170`, `tc2_sr_g`).
- From other packages' notes (not traced here): `lc1_w7170` is the input of `lc1`'s inverter that
  makes `rcs_x1` (`rcs_x1` = NOT `lc1_w7170`) and holds `lc2`'s ripple counter clear while low;
  `lc1_w7908` is the enable of latch D (`lc1_w7040` = NOT(`rst_c` OR `lc1_w7908` AND `lc1_w7862` OR
  `lc1_w7928`), whose inverse is `lc_step`); `tc2_sr_g` gates both sides of `tc2`'s latch
  (`tc2_sr_q` = NOR(`tc2_sr_q_n`, `tc2_sr_c`, `tc2_sr_g` AND `tc2_sr_r`), `tc2_sr_q_n` =
  NOR(`tc2_sr_q`, `tc2_sr_g` AND `tc2_sr_s`)); `tc2_r5589` runs through `tc2` to a pad (8248,5262)
  whose poly goes on east (no load drawn yet: no extracted gate has it as an input).
- Believed, not traced: nothing about what the gate is for. `lc1`'s notes believe `lc1_w7908` to be
  a chip-wide inverted clock; this package finds one more gate and one more latch on it, and no
  driver: every end reached is a gate, a pad or a port.

The evidence for each stretch (every command is in `cache/scratch/eofw/survey.md`; images there):

| Place | Reading | Evidence |
|---|---|---|
| corner (7276,6870) | the poly from the pad (7272,6912) turns west; it does not go on east to the pad (7335,6845), which ends the metal y 6840-6858 above | `s14_T_ma.png`, `s14_T_cm.png` (5x, four shots): an orange L in both chip-2 shots and chip 1's metal shot, plain ground east of x 7290; `px.py row 6892 7256 7296 2 metal,acid` (edge lines x 7264, 7288) |
| row y 6861-6879, x 6852-7267 | one poly in the open | `px.py row 6870 6820 7300 8 metal,acid`: R-G 41-57, blue 44-65 at every sample from x 6836 to 7276; edges y 6857 and 6879; `o3_w1north.png` |
| corner (6843,6870) | turns north; nothing goes on west | `s17_outcorner.png` (3.6x, metal and clean) |
| poly x 6834-6852, y 6400-6860 | one straight poly under eleven bus metals, no pad | `s18_x6842_c.png` (clean), `s18_x6842_a.png` (chip-2 stripped), strips at 3x: two continuous edge lines, no hole, no widening |
| (6843,6400) | meets `tc2`'s poly, same x, same width | overlay `join2.png`; `ports.py --prefix eofw`: 5 px, same name |
| row y 7204-7225, x 7400-7818 | one poly under five metals, no pad | `px.py col 7405 7194 7234 2 metal,acid`; `px.py row 7214 7330 7700 10 metal,acid`, `row 7214 7600 7830 6 metal,acid1b`: poly colour in every open stretch, salmon under the rails; `o4_w2north.png`, `o7_pad7836.png` (4x) |
| pad (7836,7215) | contact; metal leaves north only | `textmap.py 7806 7186 7870 7240 3 --acid`: ring, bright centre in both chips, hole in the clean shot; `o7_pad7836.png` |
| metal x 7829-7843, y 6400-7200 | one metal onto `tc2`'s | `tl5_tracks.py v 7836 6400 7195`: 23 bars of 8-13 px, no hole; `follow.py 7835 7185 N` runs on into `tc2`'s L; `adj_x7836.png` (1.5x, three shots); `tc2`'s port note: its follower from the north ended at (7835,7218) |
| thin metal x 7266-7280, y 7757-8703 | one metal | `px.py row 7795 7252 7292 2 metal,metal1`; `tl5_tracks.py v 7273 7760 8700`: bars of 8-10 px; chip 2 alone dim at y 8173-8192 (dirt: `textmap.py 7246 8160 7300 8206 3 --acid`) |
| T (7273,8710) | the vertical merges into the horizontal metal, which goes both ways | `s27_T7273.png` (5x, both metal shots): no line between them; `railgap.py 7268 7278 8667 8757 --min 4`, `railgap.py 8707 8717 7228 7318 --h` |
| the staircase's corners | each an L of one metal | `follow.py 7273 7800 S` and `follow.py 6480 8259 E --gap 12` give the same corners from the two ends (`eof`'s run 5 follower also ended at (6514,8254)); `railgap.py` across each: metal on two arms, 29-41 px of none beyond; `tl5_tracks.py` on each stretch: bars of 7-15 px, no hole; `s19_stair.png`, `adj_stair.png` (overlays, 1.2x and 1.5x) |
| corner (6515,8259) | an L; the horizontal arm is `lc2`'s metal | `s25_c6515.png` (5x; metal, metal1, clean); `px.py row 8259 6470 6530 2`; `textmap.py 6440 8226 6560 8290 3`; Ambiguity 1 |
| corner pad (7446,8732) | the metal from the T ends in a pad with a contact onto a poly pad; poly leaves east, the metal goes on south | `textmap.py 7410 8684 7500 8740 3`; `s20_eastend.png` (3.4x, three shots), `s26_c7466.png` (6x), `o6_ecorner.png`; Ambiguity 3 |
| row y 7812-7832, x 6356-6455 | one poly on from `eof`'s end | `px.py col 6460 7802 7842 2 metal,acid` (edge lines y 7811, 7833); `px.py row 7821 6350 6900 5 metal,acid1b`; `s22_lowrow.png` |
| pad (6339,7824) | contact; metal leaves south only; nothing west | `textmap.py 6300 7786 6384 7860 3 --acid`; `s24_pad6339.png` (3.2x, four shots); Ambiguity 4 |
| metal x 6333-6349, y 7843-8067 | one metal onto `lc2`'s | `tl5_tracks.py v 6340 7845 8070`: bars at y 7938-7946 and 7959-7968 (`lc1`'s row y 7953 under it), no hole; `follow.py 6338 7900 S --gap 16` ends at the ring of `lc2`'s pad (6341,8214) |

Overlays of the eight places where these wires meet `eof`'s, `tc2`'s and `lc2`'s drawn ends, with all
four packages' traces: `join1.png`, `join2.png` (3-4x, metal and chip-2 stripped).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `tc2_r5589` | P | (7267-7285,6900) | in | `eof`'s poly north of the pad (7272,6912): the gate's output (`eof_w7818`) |
| `tc2_r5589` | P | (6834-6852,6395) | not known | onto `tc2`'s poly (6843,6400) |
| `tc2_sr_g` | P | (7395,7204-7224) | not known | `eof`'s row east of the pad (7313,7215) (`eof_w7718`) |
| `tc2_sr_g` | M | (7829-7843,6395) | not known | onto `tc2`'s metal (7837,6400) |
| `lc1_w7908` | M | (7266-7280,7790) | not known | `eof`'s metal south of row 2's pad (`eof_w7718`) |
| `lc1_w7908` | M | (6445,8252-8266) | not known | onto `lc2`'s metal (6450,8259) |
| `lc1_w7908` | P | (7490,8722-8745) | not known | **open end**: the poly east of the corner pad, into `cdp3` (continue)'s ground |
| `lc1_w7908` | M | (7458-7474,8800) | not known | **open end**: the corner pad's metal on south, `cdp3` (continue)'s ground |
| `lc2_w8474` | P | (6455,7812-7832) | not known | `eof`'s row at `lc1`'s edge (`eof_w7777`): a gate input |
| `lc2_w8474` | M | (6333-6349,8072) | not known | onto `lc2`'s metal (6341,8067) |

`tools/ports.py --prefix eofw`: thirteen meetings. Four with `eof` (names differ: the aliases), four
with `tc2` and `lc2` at 5 px with the same name; the other five are neighbouring tracks 24-29 px or
more away (`lc1_w7780` at (6297,8067) and (6450,7780), `lc2_w8646` at (6450,8301), `tc2_sr_s` at
(7791,6400)), which these wires do not touch. Two ports without a partner: the open ends.

## Ambiguities

1. **The corner (6515,8259).** A dark line 6-8 px wide crosses the metal at x 6503-6509, between
   `lc2`'s horizontal piece and the vertical x 6509-6521. Readings: the edge of something underneath;
   or two metals that end facing each other. Assumed the first: a poly x 6510-6528 lies under the
   vertical metal (seen in the clean shot from y 8230 to 8290) and its west edge is there; both arms
   have their top edge at y 8250; 6-8 px is an edge line's width, and a gap between two metals would
   be 20 px or more with bare ground in it; and as two metals each would end on nothing. If it were a
   gap, row 2's net would still be `tc2_sr_g` but not latch D's enable.
2. **The south metal on row 2's pad (7267,7736)** is `eof`'s Ambiguity 14, and the whole south branch
   hangs on it: 12 px of dark between the pad's bright centre and the metal that starts at y 7757,
   against 15 px on the north side, where no metal leaves, and 6-8 px on the east. Read as joined (by
   `eof`'s tracer and both its reviewers, and here): the metal's two edge lines run on from the pad's
   sides in both metal shots (`s26_pad7270.png`, 6x), and the pad's own poly edge lies under that
   ring, which the east side has not (the row arrives there). Ambiguities 1 and 2 are the two places
   on which "`lc1_w7908` is `tc2_sr_g`" rests.
3. **The corner pad (7446,8732).** Read as one piece of metal (the run from the T, a contact in the
   inside of the corner, the metal on south) from a 3.4x view, a 6x view and a text map. The vertical
   metal has a dark bar of 8-11 px at y 8714-8725 where the poly pad's edge lies under it. If the
   south metal were separate, the port (7458-7474,8800) would not be this net; nothing else changes.
4. **The pad (6339,7824) shows no hole in the clean shot** (residue on chip 1). The contact is read
   from the ring and bright centre in both metal shots and the pale centre in the chip-2 stripped
   shot. Without it row 3 would end on an unconnected pad under a metal that begins there.
5. **Stretches read by text tools and low zoom only**: nine staircase corners (the follower both
   ways, `railgap.py`, `tl5_tracks.py`, overlays at 1.2x and 1.5x; not each at 4x); the metal x 7836
   from y 6400 to 7200 (`tl5_tracks.py`, the follower from both ends, one 1.5x view in three shots).
   A hop onto a neighbouring line at a corner would show as metal beyond the corner or a break.
6. **The name `lc1_w7170` for row 3's net** is `lc2`'s alias across `lc2`'s own uncertain items
   (above, Logic); the join here is to `lc2_w8474`.

## Review

**Round 1: full review** (2026-11-19 15:41 to 15:59 +0100; one fresh reviewer agent on Claude Fable
5.2 at high effort, started for this round only; commit reviewed e99cd11; 25 images in
`cache/scratch/eofw/review-1/`). It was given the four joins and the equation as claims, and told to
suspect the staircase's ten corners (text tools and low zoom only), the corner (6515,8259), the
south metal at the pad (7267,7736), the T and the corner pad, the metal x 7836, the two polys under
metals, the corner (7276,6870), the pad (6339,7824) and the lower row.

What it checked, and how:

- **The staircase**: `follow.py` from both ends (the same ten corners); `tl5_tracks.py` on all twelve
  stretches (bars of 15 px or less; 20 px or more of no metal beyond each corner); every corner seen
  in both metal shots (`b1`, `b2`, `q1`, `q2` at 4x, `r1` at 5x, `c1`, `c2` at 2.9x with the outline).
  Each is an L of one metal; the nested neighbour stays 24-30 px away.
- **The corner (6515,8259)** (`d1`, 5x, four shots): one metal. The 8 px dark line at x 6503-6509
  continues north of the metal's top edge in both metal shots, as the west edge of the poly column
  the vertical arm lies on; the top edge line y 8246-8249 is continuous across both arms; `lc2`'s
  piece is the same metal (bars of 8-9 px only, x 6206-6500); no contact on the arm.
- **The pad (7267,7736)** (`f1`, 6x): the south metal is on the pad (ring 14-16 px against 12 px on
  the east side; wire 3's pad has 16 px on its own line; the clean shot's pink runs unbroken from
  pad to metal).
- **The T and the corner pad** (`b1`, `g1`, `p1`): one metal; the contact exists (ring and centre in
  both chips, a 12 px green hole); metal leaves south and poly east, nothing else; the pad's poly is
  separate from the poly column x 7399-7423 (10 px of field).
- **The metal x 7836** (`h1_a`, `h1_b`, 3x): one straight metal, bars of 13 px or less, no hole, no
  pad; the pad (7836,7215) (`i1`, 6x) is closed south and east.
- **The row y 7214** (`j1_a`, `j1_b`, 4.4x, three shots): one poly, no widening, no hole (a dark patch
  on the VCC rail at (7750,7214) is on chip 1 only; a small ring at (7752,7202) on chip 2 only).
- **The corner (7276,6870)** (`k1`): the poly turns west only. **The row y 6870, the corner
  (6843,6870), the poly x 6843** (`l1`, `m1_a`, `m1_b`): continuous, nothing leaves west or south.
- **The pad (6339,7824)** (`n1`): contact by ring and centre in both metal shots and a pale patch in
  the chip-2 stripped shot; bare ground west and north; the row to x 6455 is one poly; the metal
  x 6418-6435 crosses it without contact. **The metal x 6341** (`o1`) runs to `lc2`'s pad.
- The extraction: 4 nets alone; 2,395 nets and 0 errors with every package; the equation as claimed.

Findings: one, a comment. The poly x 6834-6852 passes under **eleven** bus metals between y 6400 and
6860, not ten (its metal test at x 6815 in both chips: y 6410-6422, 6453, 6496, 6540, 6584, 6626,
6669, 6711, 6756, 6802, 6842-6855); all eleven crossings are clean. Corrected in the trace file's
comment and in these notes. Proof that no connection changed (the trace file differs only in that
comment):

```
tools/t.sh eofw sameconn.py e99cd11            ->  connections identical
.venv/bin/python tools/sameconn.py e99cd11     ->  connections identical
```

Could not check: the clean-shot hole at the pad (6339,7824) (residue; chip 2's centre there is dim,
R 171-186); the two open ends beyond their stubs; `tc2`'s and `lc2`'s own geometry (the name
`lc1_w7170` rests on `lc2`'s `?` items); and that the corner (6515,8259) and the pad (7267,7736)
rest on measurements, since a photo cannot show metal continuity directly.

Round 1: no findings that change a connection.

## Not done

- The two open ends at the corner pad (7446,8732): the poly on east (a dark line crosses it at
  x 7492-7498; poly colour again to x 7545 under the VSS rail) and the metal on south (seen to
  y 8850). `cdp3` (continue): the gate column x 7460-7800.
- The supply rails of `eof`'s gate between `tc2`'s labelled rails at y 6400 and `eof`'s pieces at
  y 7585 / 7720 are drawn by nobody. Followed here by profiles and two 1x views only
  (`railgap.py 7582 7615 6400 7340`, `7560 7595 7370 7900`, `7735 7768 7070 7900`, `7705 7745 6400
  7030`; a jog of the VCC rail at y 7000-7065; `s6_railsN.png`, `s6_railsS.png`): the west rail runs
  into the metal `tc2` labels `vss`, the east one into the metal it labels `vcc`. That supports
  `eof`'s reading of its wide metal x 7725-7775 as VCC (its Ambiguity 15), but it is not a trace of
  the rails.
- `tc2_r5589`'s loads: `tc2` draws the line to the pad (8248,5262), whose poly goes on east.
- The driver of `tc2_sr_g` / `lc1_w7908`: not found on any stretch drawn here.

## Corrections (coordinator, from the handoffs of 2026-11-19, third batch)

- Not done ("the metal on south (seen to y 8850). `cdp3` (continue)") and `ports.d/eofw.txt`
  (`lc1_w7908 M 7466,8800`, open end): drawn on by `busl` (piece `sr`): south to y 8910, a diagonal to
  (7209,9168), down the left bus field at x 7209 and out at (7187,15000) into `bc1`'s ground, no tap. It
  is not `cdp3`'s ground. The poly east of the corner pad is still open.
