# ucz: where the upper right array's counter lines `rc0`..`rc6` come from

## Status (2026-11-17 09:15, contributor session; independently reviewed, see Review)

Wiring drawn (`trace/ucz.txt`): all seven lines, each from the end contact of its `uc`
track in `rdp2`'s routing zone back to a net that was already named. No transistors.
**Every `uc_bK` comes out as `rcK`**: the seven lines of the upper right array are the
character row counter, bit 0 at the left. Extraction: 2024 nets (seven fewer than before:
the seven joins), 3430 transistors (unchanged), 0 errors, 0 warnings. With the seven
`@alias` lines taken out, the extraction reports exactly seven "carries several names",
`rcK` with `uc_bK` for each K and nothing else: the joins are made by the geometry, and no
item of this file carries a `?`.

Method: poly from the clean shot and chip 2's stripped shot side by side (the chip-2 shot
shows the nested L's best: `nest_acid.png`); metal by eye in both metal shots, because
these lines are thin and dim (the follower was used only where it started and ended on
contacts that were then looked at); every pad in a mosaic (`padsA.png`, `padsB.png`,
`padsC.png`: ring in the metal shot, green centre in the clean shot, and the side of the
pad opposite the row closed). Images: `cache/scratch/ucz/`.

## Route table

The `uc` tracks are `rdp2`'s (x 13541 + 390.4 K); its latch cell already draws each to
y 9072, and the metal goes on south to the end contact in the first column.

| Track | `uc` track ends on | Route | Joins | Evidence |
|---|---|---|---|---|
| `uc` track 0 | contact (13542,9164) | poly west along y 9167, south on x 13503 under the wide metal band, pad and contact (13500,9358); the pad's metal leaves south-east as bundle track L4 (x 13521), straight to y 10700 | `rc0` (`rdp3`'s L4) | `b0.png` (4x, three shots), `b0pad.png` (5x, both metal shots), `bundle.png` |
| `uc` track 1 | contact (13932,9101) | poly south on x 13932 to a pad and contact (13932,9231); metal foot west, south on x 13890 through the rows to a hook onto a pad and contact (13845,9620); poly bar west along y 9620 to a pad and contact (13563,9620) = top of L5, straight south | `rc1` (`rdp3`'s L5) | `b1top.png` (4x), `b1foot.png` (5x), `t13891.png` (3x), `b1bar.png` (3x, four shots) |
| `uc` track 2 | contact (14322,9360) | row y 9358 west (it ends at the pad), innermost L: south on x 13784, west along y 9533 to a pad and contact (13607,9533) = top of L6, straight south | `rc2` (`rdp3`'s L6) | `rowsA.png`, `rowsB.png` (3x), `nest_acid1b.png`, `nest_acid.png` (4x) |
| `uc` track 3 | contact (14713,9273) | row y 9273 west to x 14544 only, **one track down under the VSS rail x 14565** to the row y 9317, west, middle L: south on x 13740, west along y 9487 to a pad and contact (13692,9487) = top of L8, straight south to `rdp3`'s contact (13692,10745) | `rc3` (`rdp3`'s L8) | `b3hop.png`, `b3hopm.png` (5x, four shots), `rowsA.png`, `rowsB.png`, nest views |
| `uc` track 4 | contact (15102,9230) | row y 9230 west to a pad and contact (14105,9230); metal south on x 14105 to a pad and contact (14109,9966); row y 9966 west | `rc4` (`mrach`, x 13425) | `east0.png`-`east2.png` (2x, three shots), `t14062.png` (1.6x, four shots), `p34.png`, `westrows.png` |
| `uc` track 5 | contact (15492,9187) | row y 9187 west to a pad and contact (14062,9187); metal south on x 14062 to a pad and contact (14062,9881); row y 9881 west | `rc5` (`mrach`) | the same |
| `uc` track 6 | contact (15882,9143) | row y 9143 west to a pad and contact (14475,9143); short metal south on x 14474 to a pad and contact (14473,9273); row y 9276 west, outermost L: south on x 13697, west along y 9445 to a pad and contact (13647,9445); metal south on x 13650 to a pad and contact (13652,9750); row y 9750 west | `rc6` (`mrach`) | `east0.png`-`east2.png`, nest views, `padsC.png`, `westrows.png` |

## What this establishes

- **`uc` is the character row counter**, bit K on `uc_bK`: `rc_eq_r4`, `rc_eq_r6` and
  `rc_eq_r7` compare the row counter with R4, R6 and R7 (`notes/operation.md` is updated in
  the same commit). The bit order was
  not assumed anywhere: each line was followed to a net that already had its name, and
  the seven results are in order.
- The contact (13647,9445) at the top of the metal x 13650 takes the **outermost** L
  (row y 9276), which was the open question in the nest. cnt_bus_b passes that pad
  with field between (it goes north at x 13613, east along y 9400, north again at x 13655
  and on up past y 9250); cnt_bus_a turns north at x 13590. Neither is drawn here.
- Rows on one y are several nets. y 9273-9276: `rc6` west of the pad (14473,9273), `rc3`
  from x 14544 to the pad (14713,9273), `bust`'s `db_b4` row from x 15018. y 9317:
  `rc3` west of x 14544, `bust`'s `db_b3` row from its pad (14625,9315).

## Ambiguities

None on the seven routes. Weakest evidence, for a reviewer:

- The long rows y 9143, 9187 and 9230 (x 14062-15882) were read by the author at 2x and by
  the independent review at 3.5x over their full length: straight, no pad on the way.
- The `uc` metals between y 9075 and their end contacts were read by eye (`ucm.png`,
  `ucm1.png` at 2x; `rowsB.png`, `east1.png` for b2-b4): the metal test fragments them.
- The box at (14497-14530 x 9250-9300) between the pad (14473,9273) and the start of
  `rc3`'s upper row is an open-field pocket between the pad's metal and the VSS rail
  (khaki with a green rim in the clean shot at 4x, independent review); no poly crosses it.
- A dark speck on the corner of the hop in the clean shot (14556,9287) and another in the
  rail in the chip-2 metal shot (14557,9318) are at different places on the two chips:
  read as dirt, not contacts.

## R2's match to L3 (added 2026-11-17)

mrach's row y 9707 (`h_eq_r2`) runs straight on from x 13425 to a pad with a contact
(13475,9705), the top of bundle track L3 (metal x 13478, one piece by `tools/follow.py`
to y 10860, no contact candidates), which `rdp3` names `h_eq_r2` from y 10700 (4.5x in
three shots, `cache/scratch/ucz/r2.png`). Firm geometry (`tools/unsure.py` does not
list it), so the open join that ended at x 13425 is closed and carries the one name.

## Review

Independently reviewed (2026-11-17), read from the photos alone with a swap in the
nested staircase as the main suspicion: every corner of the three nested L's, the hop of
`rc3`, the long rows (3.5x, full length), the s0-column metals and `rc0`/`rc1` were
confirmed, and no two lines are swapped. The identity `rcK` rests on `mrach`'s and
`rdp3`'s traces west of x 13415 and south of y 10700, which were not re-read.

## Not done

- cnt_bus_a, cnt_bus_b east of x 13425 (both go north through the nest; seen, above).
- The bars of L0/L2 at
  y 9663 and of L2/L7 at y 9920; L7's lower piece (`rdp3_n7s9`) north of y 10700.
- Renaming `uc_b#` to `rc#` (`tools/rename.py`): the joins are firm, aliases are used for
  now; `rdp2`'s notes still say "believed" (corrections listed below).

## Other blocks' notes that this corrects (their files are not edited)

- `rdp2.md`, Not done, left bundle: "L7's piece y 9593-9733 ends on a contact at
  (13649,9747)". The metal on x 13650 is one piece from the contact (13647,9445) to the
  contact (13652,9750); it is `rc6`, not part of L7's lower line.
- `rdp2.md`, routing zone: the track scan's ends of the upper c tracks ("9176, 9218,
  9242, 9196, 9153, 9108") do not match the contacts: the tracks end at y 9164 (b0),
  9101 (b1), 9360 (b2), 9273 (b3), 9230 (b4), 9187 (b5), 9143 (b6).
- `rdp2.md`: the metal on x 13890 ("T2 track position, metal y 9398-9629") starts at the
  foot of `rc1`'s pad (13932,9231), not at y 9398.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- Not done, "the bars of L0/L2 at y 9663 and of L2/L7 at y 9920": drawn by `eof` (piece `r4`); the bar
  is at y 9916-9934, the contacts at (13433,9665), (13432,9925), (13650,9925).
