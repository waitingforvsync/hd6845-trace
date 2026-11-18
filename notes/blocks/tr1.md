# tr1: top-right logic rows, part 1 (x 11900-14150, y 3400-4500)

## Status

Inverter A and gate B drawn (2026-11-18, traced on claude-opus): `trace/tr1.txt`, 4 transistors, extraction
0 errors 0 warnings (`TRACE=tr1` and full). Gate B (x 12065-12200) read at 3x in three shots, its
extra box not drawn. Gate C (x 12205-12330) is NOT drawn. Survey views:
`cache/scratch/tr1/survey.png` (0.57x), `row_11900.png`, `row_12650.png`, `row_13400.png`
(1.65x), `cellA*.png`; drawing views `a.png` (3.5x, clean / chip-2 stripped / chip-2 metal),
`a_tr.png` (3x, trace over clean and stripped shots).

## Inventory

| Piece | Where | What was seen |
|---|---|---|
| Track field | y 3400-3650 | six horizontal metal tracks, centres y 3420, 3464, 3507, 3550, 3594, 3637. Each is several pieces (metal test in both metal shots, breaks in x): 3420: 12221-13089, 13247-14045; 3464: 11958-12589, 12646-13133, 13168-13346, 13372-13907; 3507: 12431-13392, 13427-14085; 3550: 12083-12654, 12905-13435, 13475-14016; 3594: from west of 11850 to 14244 with dark spots at 12855-12889, 12941-12986, 13479-13513 (contacts or breaks, not looked at); 3637: west of 11850 to 13561, and 14036 on east. Vertical polys drop from the tracks (and from north of y 3400) into the gate row. No end was looked at above 1.65x. |
| Upper rail | y 3747-3785 | metal, believed VSS from structure (pull-down sources contact it, e.g. (12042,3758)). Not traced to a supply. |
| Thin metal | y 3827-3839 | runs through the row from west of x 11850, many pieces; crosses the inverters' output diffusion without a contact at (11975,3833) (clean shot plain tan, no pit). |
| Lower rail | y 3920-3964 | metal, believed VCC from structure (load diffusions contact it, e.g. box 11960-12020 x 3912-3965). Not traced to a supply. |
| Gate row | y 3650-3980, x 11900-14150 | about 16 gates. Three look-alike inverters at x 11940-12065, 12075-12195, 12205-12330 (pitch about 130; the second and third seen only at 1.65x). East of x 12330 a mixed row of multi-input gates and what look like pass gates under the upper rail (pairs of vertical polys with a jog at x 12340-12400, 12830-12890, 13080-13130, 13320-13370, 13560-13620, 13790-13830, 14030-14080): possibly a repeated cell of pitch about 240-480; `tools/findcell.py` was not run. Loads (textured poly, y 3850-3900) at x about 11970, 12100, 12230, 12350, 12700, 12860, 13160, 13320, 13620, 13760, 14120. VCC contact boxes at y 3912-3965, x 11960-12020, 12090-12150, 12220-12280, 12460-12560, 12950-13040, 13120-13160, 13430-13530, 13600-13650, 13900-14000, 14080-14130. |
| Bus | y 3990-4510 | twelve horizontal metals, all already drawn by other blocks and none of them tr1's: centres y 4008 `ra0_cmp`, 4051 `ra1_cmp`, 4095 `ra2_cmp`, 4138 `ra3_cmp`, 4181 `ra4_cmp`, 4246 `ral_stb`, 4289 `cnt_gab`, 4333-4500 `rax_o0`-`rax_o4` (`tools/amr_at.py` at x 12600, all blocks). No tap from the gate row down into this bus was seen at 0.57x; the lower rail lies between them. |

## Logic

Inverter A, x 11940-12065 (drawn; `tr1_w11960 = NOT tr1_w12005`; `unsure.py --equations`: DEPENDS on the two `?` items of the load tie, not firm):

| Transistor | Gate | Between | W/L | Where |
|---|---|---|---|---|
| pull-down | `tr1_w12005` | `vss` - `tr1_w11960` | 47/22 | channel (12005,3758): diffusion box 11966-12062 x 3735-3782, source contact (12042,3758) on the upper rail |
| load (depletion) | `tr1_w11960` (?) | `tr1_w11960` - `vcc` | 21/52 | channel (11972,3879): textured poly 11942-12003 x 3853-3905 over the strip x 11962-11983; drain in the box 11960-12020 x 3912-3962, contact (11988,3938) on the lower rail |

Gate B, x 12065-12200 (drawn by hand from `b5.png`, 3x clean / chip-2 stripped / metal; `tr1_w12090 = NOT tr1_w12135`; DEPENDS on its own two `?` tie items):

| Transistor | Gate | Between | W/L | Where |
|---|---|---|---|---|
| pull-down | `tr1_w12135` | `vss` - `tr1_w12090` | 50/22 | channel (12135,3757): box 12092-12195 x 3732-3782, source contact (12165,3755) (ring in the metal shot); `px.py col 12135 3715 3805`: bright y 3740-3775, poly end about 3795 |
| load (depletion) | `tr1_w12090` (?) | `tr1_w12090` - `vcc` | 21/52 | channel (12102,3879): textured poly 12072-12133 x 3853-3905 over the strip x 12092-12113; drain box 12090-12150 x 3912-3962, contact (12117,3937) |

B's extra box: 12168-12195 x 3850-3905, east of the tie lobe and separated from it by a dark edge
at x 12162-12170 (`px.py row 3865 12120 12200 4`: bright x 12172-12192 in both shots, dark
x 12136-12148 at the tie and 12164-12168 at the edge); clean shot shows a dot at (12183,3880).
It is NOT drawn: no layer or contact was settled for it. It touches neither the load strip nor the
pull-down box as seen at 3x; if it is a diffusion box with a contact to the thin metal or the lower
rail, it belongs to the next gate east and does not change B.

Bit cell's gates in full: one enhancement pull-down to VSS and one depletion load to VCC whose
gate is (believed) tied to the output: an inverter.

Wires: the output diffusion runs north from the gate's west side along x 11965-11983 to a
buried contact 11945-11988 x 3672-3705 and a poly x 11950-11972 north to y 3650 (end of
drawing); south along the same strip, crossing two dark lines at y 3800-3812 and the thin metal
without contact, to the load; an arm east along y 3825-3848 to a lobe 12008-12036 x 3825-3878.
Gate profile (`px.py col 12005 3720 3805`): bright channel y 3736-3780 in both shots, poly end
about y 3795, dark field from y 3800.

Rings/boxes in the piece with no drawn item: the two dark lines at y 3800-3812 crossing the
output strip (thin metal or a field edge; not a contact on the strip, not drawn); the bright
poly at x 11960-11975 north of y 3650 and the poly x 12000 north of y 3650 (not followed).
## Ports

`ports.d/tr1.txt`: `tr1_w12005` (in) and `tr1_w11960` (out), both poly ends at y 3650 where the drawing stops; neither followed north.

## Ambiguities

- Which rail is which is from structure only.
- The load's gate tie is drawn as `?P 12000,3855:12020,3875` and `?B 12006,3853:12022,3877`.
  `px.py row 3865 11995 12030 3`: both stripped shots dark at x 12004-12019 (clean 44-86,
  chip-2 81-149), lighter both sides; the lobe 12008-12036 x 3825-3878 has its own dark ring
  in both shots. A dark spot in a diffusion lobe beside the load's poly fits a buried contact,
  and a depletion load's gate is normally tied to its source, but this was not confirmed at
  5x. If wrong, the load's gate is something else and the gate is not a plain inverter.

## Not done

Gate B is drawn (its extra box 12168-12195 x 3850-3905 is not: read it at 5x). Resume with gate C (view `bc.png`: gate poly 12255-12275, pull-down box runs on east past x 12320 into the next gate; draw it on its own),
then A's copies at +130 and +260 (read each copy's inputs on the photo), then follow
the two polys north into the track field; then the gates east of x 12330, the track
field's ends and contacts, the thin metal y 3827-3839, the rails' supplies, and the
strip y 3400-3650 north boundary to `pads_in_top` / `inprot`. `tools/findcell.py` with
`ral_cell`, the pad-driver cells and those of `tl1`, `tl5` was not tried.

## Review
