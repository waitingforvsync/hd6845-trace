# bc3: bottom-centre random logic (x 7000-9000, y 16300-18550)

Trace: `trace/bc3.txt`. Scratch: `cache/scratch/bc3/`. Coordinates are metal-shot pixels.

## Status

2026-11-18 05:33 (UTC+1). Traced on claude-opus (the Fable allowance was used up); a
survey and one small piece. Drawn: one inverter at x 7475-7775, y 17575-17705, a copy
of `tl5_inv` (`bc3_w17605` = NOT `ck_out`) with its two rail boxes, and the
two rails: `bc1`'s RL2 (VCC, x 7470-7520) and RL3 (VSS, x 7641-7691) carried on from
y 16300 to the inverter (continuous metal in both metal shots). Neither row is followed
beyond the piece. Extraction with the piece: 0 errors,
0 warnings. Not reviewed yet.

## Inventory

Survey: `cache/scratch/bc3/survey.png` (0.57x, metal and clean shot side by side, with
every block's geometry). Read at 0.57x only: the coordinates below are within about 20 px.

- **Vertical metal rails** (wide, bright): x ~7300-7330 (y 16300-17700), x 7463-7520
  (whole height; the inverter's VCC box is under it at y 17575-17665), x 7641-7691
  (whole height; the inverter's VSS box at y 17660-17705), x ~8350-8390 and x ~8520-8560
  (whole height). x 7470-7520 is `bc1`'s RL2 (VCC) and x 7641-7691 its RL3 (VSS), both
  drawn here from y 16290 to the inverter (`r1.png`, `r2.png`, `r3.png`, 2.1-2.4x, metal and
  chip-1 metal: bright metal throughout, contacts only inside it). The others not followed.
- **Left gate group**, x 7050-7850, y 16350-17700: a column of gate units on both sides
  of the rails x 7463 and x 7641 (diffusion and load plates seen in the clean shot at
  x 7270-7700), with buried contacts and metal crossovers; the traced inverter is the
  lowest unit east of x 7520.
- **Right gate group**, x 8150-8950, y 16350-17650: a similar column on both sides of
  the rails x ~8350 and ~8540, larger units (a big diffusion area x 8250-8400,
  y 17450-17620).
- **Centre**, x 7850-8150: vertical metal tracks (about ten, pitch ~25) bending into
  horizontal tracks at y 17600-17950 that run to both sides.
- **Routing field**, y 17700-18550, whole width: horizontal poly and metal rows at
  pitch ~45; columns of contact pads at x ~7400, ~7550, ~8380, ~8600 (y 17750-18450)
  where vertical metal takes rows; a horizontal metal y ~17950 from x 7580 to 7900 with
  pads at both ends.
- **Drawn by other blocks**: only a line across the bottom at y ~18405-18420 with contact
  boxes at x ~7400-7600 and ~8380-8600 (larr's metal turns at y 18405; not checked).
- **findcell** (clean shot, region 7000,16300:9000,18550, min 0.6):
  - `tl5_inv` (master 4951,4786:5213,4910): 0.85 at 7644,17645 offset 2562,12797 (placed:
    the piece); 0.79 at 8687,17305 (3605,12457 mx=5082 rot=180); 0.66 at 7346,17306 and
    0.61 at 7345,17175 (rot=180). Not overlaid except the first.
  - `tl1_ua` (2532,4350:2838,4600): 0.76 at 8414,16750 (5729,12275); 0.67 at 8657,16620
    (mx). `tl1_ub` (2535,4347:2838,4797): 0.75 and 0.65 at the same places. Not overlaid
    (scores near 0.8 can lie: guide trap).
  - `bc1_drv` (7530,14978:7795,15163): no hit at 0.6.

## Logic

Inverter i1 (x 7475-7775, y 17575-17705), `@inst tl5_inv 2562,12797 tag=i1`:
`bc3_w17605` = NOT `ck_out`. Load from the box under the VCC rail x 7470-7520
(contact (7490,17620): dot in the clean shot, ring in metal; `w5.png`, 5x three shots);
pull-down to the box under the VSS rail x 7641-7691 (contact (7676,17681); `e5.png`, 5x three
shots). Overlay `i1.png` (3x, metal and clean). The cell's tab tie (buried contact
7551-7599 x 17649-17685) stays `?` as in the master. The output poly ends in a pad with a
contact (7795,17605) to metal, the gate row in a pad with a contact (7840,17648) to metal
(`x5.png`, 5x, three shots); only the metal over each contact is drawn. `follow.py` takes
the output's metal north along x 7795 (to y 17328 at least) and the input's along a vertical
x 7839. Both metals are drawn as far as seen continuous (`v1.png`, `v2.png`, 2x, two
metal shots, plus a metal profile: no gap over 19 px): the output's x 7783-7806 north to
y 17150, the input's x 7828-7850 north to y 16640. Their contacts on the way (a ring at
(7795,17335)), their ends (a box near (7795,17130); pads near (7835,16590)) and the input
metal south of y 17660 are not drawn.

## Ports

| Net | Where | Dir | Note |
|---|---|---|---|
| `bc3_w17605` | M x 7783-7806, north end y 17150 | out | inverter output; goes on north to a box near (7795,17130) |
| `ck_out` | M x 7828-7850, y 16640 and y 17660 | in | inverter input; goes on north to pads near (7835,16590) and on south |
| vcc | M rail x 7470-7520, from y 16290 (bc1's RL2) to 17700 | - | the rail's south end not followed |
| vss | M rail x 7641-7691, from y 16290 (bc1's RL3) to 17705 | - | the rail's south end not followed |

## Not done

- **An undrawn tap on the output `bc3_w17605`** (review round 1): the output metal
  x 7783-7806 has a real contact at (7795,17337) (ring on a widened pad in both metal shots;
  in the clean shot a pad about 7775-7810 x 17320-17360 with a green centre, between the
  poly rows at y about 17295 and 17385). Whether poly or diffusion lies under it is not
  read: an open continuation of the net. The drawn ends are not real ends either: the
  output runs on to a contact near (7793,17125); the input goes north to a contact near
  (7837,16605) and beyond, and south past y 17725.

- Everything else in the region: the left and right gate groups, the centre tracks, the
  routing field.
- The rails' contacts between y 16300 and 17560 (the gate units' boxes), and the rails
  south of y 17705.
- The inverter's output metal north of y 17150 and its contact at (7795,17335); the input
  metal north of y 16640 and south of y 17660.
- Overlay the other findcell hits at 3x before placing any.

## Claims for the reviewer

1. Inverter i1 is a copy of `tl5_inv` at offset 2562,12797 (box 7475-7860 x 17575-17705):
   load from the VCC box (contact (7490,17620)), pull-down to the VSS box (contact
   (7676,17681)), gate row y 17637-17655, output node with buried contact 7723-7767 x
   17591-17627; tab tie 7551-7599 x 17649-17685 `?` as in the master.
2. The rails x 7470-7520 (VCC) and x 7641-7691 (VSS) are continuous from y 16290 to the
   inverter.
3. Output poly pad and contact (7795,17605); input row on east to the pad and contact
   (7840,17648).
4. Output metal x 7783-7806 continuous y 17150-17617; input metal x 7828-7850 continuous
   y 16640-17660.

## Review

**Model note: the survey and this inverter were traced AND reviewed on claude-opus, not
claude-fable-5-2** (the contributor's Fable allowance is exhausted).

Round 1 (full review, 2026-11-18 08:43 +0000, a fresh agent on claude-opus). Checked at 4-5x in the clean and
both metal shots with profiles: the copy of `tl5_inv` on the photo (gate 7635-7775 x
17637-17655 past both edges of the diffusion column x 7650-7707; load plate, buried contact
and output poly in place); the load contact (7490,17620) in the VCC rail and the pull-down
contact (7676,17681) in the VSS rail (not reversed); both rails bright metal from y 16240
to 17610 in both chips (dark bands up to about 22 px are contact rings or edges beneath),
starting on bc1's RL2 (vcc) and RL3 (vss); the output contact (7795,17605) and input
contact (7840,17648) on their poly pads; the two long metals not swapped; the input metal
without a contact between y 16640 and 17660; no metal south of the output contact; the
extraction (0 errors; bc3's nets are `bc3_w17605`, `ck_out`, vcc, vss; no merge with
bc1's metals at x 7795 / 7838, which end at y 15447 / 15830).
No finding changes a drawn connection. One omission, recorded in Not done: a real contact
on the output metal at (7795,17337) is not drawn (an open tap). Not checked: the `?` tab
tie (as in the master), the chip-2 stripped shot, gate edges by profile.

Round 1: no findings in what is drawn; one undrawn tap on the output listed in Not done.

## Corrections (coordinator, from the handoffs of 2026-11-19, third batch)

- Survey, "Centre, x 7850-8150: vertical metal tracks": the tracks step one position east going north
  at y 17250-17350 and again (two positions) at y 16640-16750; the track that is x 8057 at y 17700 is
  `rst_a` (`eof` run 9, piece `isrc4`), and the track x 8098 lies on `rst_a`'s poly row y 17736 from
  x 8096 to 8388 without a contact.

## Corrections (coordinator, from the handoffs of 2026-11-20)

- Inventory, "Vertical metal rails ... x ~8350-8390 and x ~8520-8560 (whole height)": the rail x 8338-8382 steps west to x 8316-8362 at y 17240-17270 and ends at y 17568 (20 px of bare ground to the metal y 17599-17614; `eof`, piece `g174`).
- Inventory, "Right gate group ... a big diffusion area x 8250-8400, y 17450-17620": it is the active area of `eof`'s piece `g174`, x 8258-8368, y 17266-17560, with three gates on it.
- Under the rail x 8686-8732 `eof` draws everything from y 15886 to y 17290 (two copies of `tl1`'s latch in series, two inverters, a NOR); the `findcell` hit `tl5_inv` at (8687,17305) is still undrawn.

## Corrections (coordinator, from the handoffs of 2026-11-20, second batch)

- The gate column under the rail x 7292-7342 (bands at y 16866-16884, 16986-17051, 17160-17180, 17290-17310 and on south: `tools/railprof.py 7295 7340 16860 17400`) is in this package's region. Its units at y 16941-17235 are drawn in `trace/bl0.txt` (`bl0` run 2): `bl0_w17085` = NOT(`lpstb_b` AND `res_b`) and `bl0_w17210` = NOT `bl0_w17085`, the light pen strobe passed only while RES is high. The rail is not drawn here (this package draws x 7495 `vcc` and x 7666 `vss`); `bl0` draws its stretch y 16925-17240 and names it `vss` by the orientation of the gates only. `bl0`'s `vcc` ports at (7470-7520, 17020 and 17240) are on this package's rail x 7495.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- Survey, "left gate group": the gate column under the rail x 7292-7342, y 16941-17755, is drawn in full in `trace/bl0.txt` (`bl0` runs 2-4; five units; the rail ends at y 17755): the strobe gate `bl0_w17085` and its inverter `bl0_w17210`, `bl0_w17337` = NOT `bl0_w17210`, and the cross-coupled pair `bl0_w17440` / `bl0_w17610`, the light pen flag. The band y 16866-16884 north of it is not drawn.
- The gate column east of the supply rail x 7470-7520 takes the flag `bl0_w17610` on the poly row y 17378-17398 from the pad (7882,17389) (`bl0`'s port (7760,17378-17398)); `rcs_mv` arrives on a poly row east of the pad (6968,16780) (port (7040,16770-16790)). Neither unit is drawn.
- The pad (7840,17648) of the track x 7840 is on the buffered clock (`tl4` runs 11-12: a branch of the clock's metal from the pad (7641,17908) north, east along y 17824 and north on x 7840): the inverter of that pad is NOT `ck_out`. The track north of the pad (drawn here to y 16640; follower to (7837,16386)) leads to more loads of the clock.
