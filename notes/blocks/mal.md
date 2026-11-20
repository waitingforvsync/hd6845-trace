# mal: the fourteen copies of the ral cell in front of the MA pad drivers

## Status (2026-11-17 05:18, contributor session)

Placed (`trace/mal.txt`, 98 transistors: seven per copy, `ral_cell` being traced in full
traced, with inverter 2), and **every copy's output followed to its MA pad driver: copy m# drives MA#**,
m0 at the top (y 8155) to m13 at the bottom (y 18576). Depends on `trace/ral.txt`
(`@requires ral`). Inputs and the force taps' wiring are not drawn.

## Placement

`tools/findcell.py 14020 4265 14450 4525 --min 0.7 --region 2300,7800:3200,19000
--layer acid1b --cell ral_cell`: fourteen hits at 0.78-0.82, all turned 90 degrees about
(14235,4395), the first eleven also mirrored (`mx=14235`), the last three not. Centres
at x 2659-2661, y 8155, 8761, 9368, 9976, 10627, 11234, 12036, 12730, 13382, 15506,
16201, 17275, 17925, 18576 (tags m0-m13). Copy m0 checked by overlay in metal and the
clean shot at 1.45x and 3x (`cache/scratch/ral/m0.png`, `m0b.png`): the cell's middle
(VSS) rail lands on the vertical metal x 2600-2650, the top (VCC) rail on x 2780-2830,
the contacts on rings.

## Logic (as far as the cell is traced)

    ral_a_m#  <- input     pass transistor 16/26, gate ck_out    (all fourteen)
    ral_a_m#  <-> output   hold device 16/90, gate VSS
    ral_tf_m# -> VSS       pull-down 66/20, gate mal_frc_m#

**Each copy's strobe pad lands on `ck_out`'s left-edge trunk** (`trunks`: metal x
2500-2504, with "contact candidates about every 608 px (y 8360, 8965, 9573, 10181,
10831, 11440 ...): its taps into the left column, not looked at"). The copies' strobe
contacts are at y 8349, 8955, 9562, 10170, 10821, 11428, 12230, 12924, 13576, 15700,
16395, 17081, 17731, 18382, i.e. those taps. The cell being the latch
traced in `notes/blocks/ral.md`, **every MA output is latched, transparent while `ck_out` is
high (CLK low), and forced high by its `mal_frc_m#` line**, where the RA outputs are latched
on `ral_stb` and forced by `cnt_gab`. The fourteen `mal_frc_m#` are probably one line: a thin
vertical metal at x about 2700 runs past the copies' pads (seen y 10250-11350, tabs to m4 and
m5; not drawn).
Believed, not extracted: the cell's forward path is not traced.

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `ck_out` | metal | the trunk x 2500, contacts as above | in | strobe |
| input end of each pass transistor | diffusion | x about 2567, below each strobe contact | in | unnamed: the MA counter's (or start address's) bit, not followed |
| `ma0_drv_in` ... `ma13_drv_in` | poly, metal | each copy's output (below) | out | the MA pad drivers' inputs |
| `mal_frc_m0` ... `mal_frc_m13` | metal | pads at x 2728-2730 | in | force pull-down gates; each a pad of its own here |

## Outputs: copy m# -> MA# pad driver

Each copy's output poly leaves its bend west under the `ck_out` trunk to a contact; a
metal from there runs to the pad driver's input. Followed with `tools/follow.py`
started on each copy's own metal (starting on the shared column x 2195 makes the
follower jump between lines: it took m4 and m5 to MA7). Contacts read at 2.6-3.5x.

| Copy | Contact | Route | Driver end |
|---|---|---|---|
| m0 | (2195,8038) | west to x 2153, north to y 2142, east | (4606,2142), MA0 (x 4602) |
| m1 | (2148,8640) | west to x 2110, north to y 2100, east | (3069,2096), MA1 (x 3062) |
| m2 | (2108,9250) | north, jog west to x 2023 at y 8757, north | (2022,1659), MA2 (y 1658) |
| m3 | (2150,9858) | north, jog to x 2061 at y 8709, north | (2065,3265), MA3 (y 3264) |
| m4 | (2283,10510) | north along x 2283 | (2283,4914), MA4 (y 4912), poly hop west to the driver |
| m5 | (2240,11112) | north along x 2242 | (2240,6995), MA5 (y 6994), poly hop |
| m6 | (2197,11923) | larr's line x 2197 north | y 8555, MA6 (y 8555), poly hop; larr's line "not checked by a view" |
| m7 | (2198,12614) | a short foot west to x 2155, north to y 10120, west | (2018,10120), MA7 (y 10118) |
| m8 | (2283,13268) | west to x 2241, north | contact (2238,11870), poly west to MA8 (as larr found it) |
| m9 | (2458,15388) | west, north, west, north, west | contact (2027,14352), MA9 |
| m10 | (2455,16088) | west to x 2020, north | contact (2022,15918), MA10 |
| m11 | (2455,17392) | west to x 2026, south | contact (2025,17485), MA11 |
| m12 | (2455,18040) | west to x 2026, south | contact (2025,19214), MA12 |
| m13 | (2547,18905) | output poly south (with a jog east at y 18762-18785) to the pad, metal east along y 18908 | contact (3627,18902), MA13 |

The end contacts of m0-m3 and m7 were checked at 4x in both the metal and clean shots
(`cends.png`, `cends2.png`): a ring on a poly pad in each. Extraction: every copy's hold device joins
`ral_a_m#` to `ma#_drv_in`; 0 errors, 0 warnings.

This settles the bit order for the left column, and with `larr`'s carry direction it
can now be checked against the counter rows (each copy's **input**, not yet followed).

## Not done

1. Each copy's input: which counter row (or start-address bit) feeds it.
2. Where the force taps `mal_frc_m#` go.
3. Everything `ral` has not traced inside the cell.
4. The twentieth copy, at (8450,5562): findcell places it at 0.81 (turned 90 degrees, not
   mirrored, `@inst ral_cell -5785,1167 rot=90 o=14235,4395`), but an overlay at 1.5x
   (`cache/scratch/ral/t0.png`) does not put the cell's rails and pads on matching
   features, and its strobe contact (8298,5368) has no metal over it. Not placed.

## Corrections (coordinator, from the handoffs of 2026-11-20, third batch)

- "The fourteen `mal_frc_m#` are probably one line: a thin vertical metal at x about 2700 ... not drawn": the thin metal x 2690-2710 has a pad at (2700,15999) where `bl0_w15412` (= NOT `rst_n`, the fourth copy of the reset) arrives by a poly row across the left array's Gap 2 (`bl0` run 7, firm to the pad); a metal tab from the thin metal to `mal_frc_m9`'s pad (2728,15583) is seen at y 15575-15581. So the force line is, **believed**, the reset in `rst`'s sense, forcing the MA outputs. Not joined in the trace: the thin metal is not drawn (about 8 px wide; at y 15845-15895 it runs over a diffusion strip of its own width and reads at bare-ground level in chip 2; `follow.py` passes it from y 15960 to 14782, `tl5_tracks.py v 2697 14700 18700` fails on long stretches). It needs views at 6x, with the left column's cell (`larr` (continue)).
