# wrj: the write strobes of R0, R1, R2, R4 between rdp3 and bd1 (x 13500-13850, y 13480-14700)

## Status

Traced 2026-11-17 09:30 (one agent, one pass with a numeric cross-check). File
`trace/wrj.txt`: four metal lines, no transistors, no uncertain items. Full extraction:
2046 nets, 3430 transistors, 0 errors, 0 warnings. `tools/unsure.py` lists none of the
four nets.

**All four joins come out as expected**: rdp3's `wr_r0`, `wr_r1`, `wr_r2` and
rdp2's `wr_r4` are bd1's `wr_r0`, `wr_r1`, `wr_r2`, `wr_r4`. So, by
geometry from the select gates to the register rows: rdp3's row RA is R1, row RB is R2,
rdp2's row RC is R0 and row RE is R4. (That statement also rests on rdp3's own drawing of
the bundle north of y 13480, on bd1's tracks south of y 14690 and on rdp2's poly link for
row RE, none of which was re-read here.)

The open-join names were renamed with `tools/rename.py` in 82ba48e.

## What is in the stretch

Twelve bundle tracks come down from rdp3 (L0..L11, 43.4 px pitch); the eight from L4 east
were read. Everything was looked at in both metal shots and in `acid1b`.

- The tracks L4..L9 are straight and unbroken from y 13480 to 14700.
- L10 (x 13782, rdp3's `hc5`) ends on a contact at (13782,13893); a poly leaves it west
  along y 13880-13908 under L9..L4 and on. No metal on x 13782 from y 13915 to 13992
  (open field in `acid1b`).
- L11 (x 13825) turns west at y 14001 and takes over L10's position.
- The line at x 13868 (starts on a contact at (13868,13630) under a poly from the north:
  rdp3's `hc0`, by its position) turns west at y 14041-14058 and takes over L11's
  position (bd1's `hc0` at (13826,14700)). Seen, not drawn: its contact was not read.
- A poly band at y 14010-14038 comes from the east under all the tracks, turns south-west
  at x 13600 and runs diagonally under L5 and L4 (it passes L4 at y 14088-14136). It lies
  exactly between L11's arm and the x 13868 line's arm. It has no contact inside
  x 13500-13900. Not identified.
- `acid1b` shows plain field under every track between the crossings: no poly hidden
  under the metal and no contact pad anywhere on L4..L11 in this stretch (unlike `mrach`).

## Routes

| Strobe | From (rdp3) | Route | To (bd1) | Evidence |
|---|---|---|---|---|
| `wr_r4` | L4, (13521,13480), net `wr_r4` | straight on x 13521 | k10, (13521,14690) | surveys; poly crossings `xA.png` (y 13880-13908), `xC.png` (diagonal, y 14088-14136) |
| `wr_r2` | L6, (13608,13480) | straight on x 13608 | k12, (13608,14690) | surveys; `xA.png`, `xB.png` (the band's corner, y 14010-14050) |
| `wr_r0` | L7, (13651,13480) | straight on x 13651 | k13, (13652,14690) | surveys; `xA.png`, `xB.png`; dirt at y 13585 (chip 1) and 14385 (chip 2) on `blem1.png` |
| `wr_r1` | L11, (13825,13480) | x 13825 to y 14001, west along y 13993-14010 to x 13782, south | k16, (13782,14690) | `jog11_m.png` (4x, both chips), `jog11_a.png` (stripped shots), overlay `jog11_ov.png` |

Images are in `cache/scratch/wrj/`. Surveys at 2x: `sv_metal_13460.png`,
`sv_metal_14080.png`, `sv_metal1_13460.png`, `sv_metal1_14080.png`,
`sv_acid1b_13460.png`, `sv_acid1b_14080.png`.

The numeric cross-check (so that no jog can hide between the views): the metal test of
`follow.py` (R > 170, G > 125) down the centre line of every gap between tracks from
x 13500 to 13847, y 13400-14700. On chip 1 there is no metal in any gap except L11's arm
(x 13804, y 13998-14008) and the x 13868 line's arm (x 13847, y 14041-14054). Chip 2
gives the same two plus speckle (about 5 %, runs of 2-20 px), which on `blem1.png` is
bare field. Along the tracks every dark run of 25 px or more is one of the poly crossings
above, and each was looked at 4.6-5x.

The one place where two nets come close: L11's arm (bottom edge y 14010) and the x 13868
line's arm (top edge y 14041) are 31 px apart with the poly band between them, and on
x 13825 there is no metal from y 14008 to 14041 in either chip.

## Review

Independently reviewed (2026-11-17), with the old bridged-jog error as the main
suspicion: the jog of `wr_r1` (6x in both chips and the clean shot, profiles of the
empty stretches on x 13782 and x 13825), L4/L6/L7, the poly crossings and the meeting
points with rdp3's and bd1's geometry confirmed.

## Ambiguities

None on the four joins.

Names: the pieces in rdp2, rdp3 and bd1 carry the same names `wr_r0`, `wr_r1`, `wr_r2`,
`wr_r4` (renamed with `tools/rename.py` in the commit after the drawing; the former
`_u` names are in the glossary's former-names table).

## Not done

- The x 13868 line (`hc0`): metal seen from the contact (13868,13630) to
  (13825,14700), contact and poly not read at high zoom, not drawn.
- L5, L8, L9 (rdp3's `hc1`, `hc3`, `rc_eq_r4`; bd1's `hc1`, `hc3`, `rc_eq_r4`):
  straight and unbroken in the same views and profiles, not drawn (not this package).
- L0..L3 (x 13348-13478): not read here.
- The poly from L10's contact going west (y 13893) and the poly band at y 14010-14038 with
  its diagonal: seen, not followed.
- rdp3's bundle north of y 13480 was not re-read.
