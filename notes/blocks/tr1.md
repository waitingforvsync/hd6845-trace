# tr1: top-right logic rows, part 1 (x 11900-14150, y 3400-4500)

## Status

Survey only (2026-11-18 04:48 +0100). Nothing is drawn: there is no `trace/tr1.txt` yet. One inverter was
read on the photos but not drawn or self-checked (see Logic). Views:
`cache/scratch/tr1/survey.png` (0.57x), `row_11900.png`, `row_12650.png`,
`row_13400.png` (1.65x, metal over clean shot), `cellA*.png` (3.6-5x).

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

Read, NOT drawn, not self-checked (one pass, clean shot and chip-2 stripped shot at 5x,
colour profiles with `tools/px.py`):

Inverter A, x 11940-12065. Pull-down: gate poly x 11994-12016 coming from the north
(y 3650) and ending at y 3795; diffusion y 3735-3780 from x 11968 to 12062, source
contact at (12042,3758) on the upper rail; W about 43, L about 22. Output: diffusion
west of the gate, north along x 11965-11982 to a buried-contact box 11945-11988 x
3672-3705 and a poly going north along x 11950-11972; south along x 11965-11988 to the
load. Load: poly 11942-12003 x 3853-3905 over a diffusion strip x 11962-11983 (W about
21, L about 52), south end in the contact box on the lower rail; gate tied to the
output by an arm of diffusion east along y 3825-3848 to a buried-contact box about
12008-12036 x 3850-3878. Equation if this stands: out = NOT in. Where the two polys go
north of y 3650 was not followed.

## Ports

None yet (nothing drawn; `ports.d/tr1.txt` not created).

## Ambiguities

- Which rail is which is from structure only.
- Whether the load poly reaches the buried-contact box at x 12003-12010, y 3855-3875:
  the profile along y 3865 is dark at x 12005-12017. Needs a 5x look in both stripped
  shots before the load's tie is drawn.

## Not done

Everything: resume by drawing inverter A (check each end and both gate widths first),
then its copies at +130 and +260 (read each copy's inputs on the photo), then follow
the two polys north into the track field; then the gates east of x 12330, the track
field's ends and contacts, the thin metal y 3827-3839, the rails' supplies, and the
strip y 3400-3650 north boundary to `pads_in_top` / `inprot`. `tools/findcell.py` with
`ral_cell`, the pad-driver cells and those of `tl1`, `tl5` was not tried.

## Review
