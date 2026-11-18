# bc3: bottom-centre random logic (x 7000-9000, y 16300-18550)

Trace: `trace/bc3.txt`. Scratch: `cache/scratch/bc3/`. Coordinates are metal-shot pixels.

## Status

2026-11-18 05:33 (UTC+1). Traced on claude-opus (the Fable allowance was used up); a
survey and one small piece. Drawn: one inverter at x 7475-7775, y 17575-17705, a copy
of `tl5_inv` (`bc3_w17605` = NOT `bc3_w17646`) with its two rail boxes, and the
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
`bc3_w17605` = NOT `bc3_w17646`. Load from the box under the VCC rail x 7470-7520
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
| `bc3_w17646` | M x 7828-7850, y 16640 and y 17660 | in | inverter input; goes on north to pads near (7835,16590) and on south |
| vcc | M rail x 7470-7520, from y 16290 (bc1's RL2) to 17700 | - | the rail's south end not followed |
| vss | M rail x 7641-7691, from y 16290 (bc1's RL3) to 17705 | - | the rail's south end not followed |

## Not done

- Everything else in the region: the left and right gate groups, the centre tracks, the
  routing field.
- The rails' contacts between y 16300 and 17560 (the gate units' boxes), and the rails
  south of y 17705.
- The inverter's output metal north of y 17150 and its contact at (7795,17335); the input
  metal north of y 16640 and south of y 17660.
- Overlay the other findcell hits at 3x before placing any.

## Review
