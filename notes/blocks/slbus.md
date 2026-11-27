# slbus: the scan line counter's five lines from the left array to the R5 comparator

Serial work, 2026-11-16. Trace: `trace/slbus.txt`. Views: `cache/scratch/rdp1/c5a.png`,
`c5b.png`, `w5m.png`, `knot_chk.png`; `cache/scratch/urch/e5.png`, `e6.png`.

## Status

Drawn end to end and extracted (wiring only): the five outputs `sl0`-`sl4` of the 5-bit
counter in the left array's upper rows, from where `trace/urch.txt` leaves them (x 4720)
to the contacts under the counter tracks of the R5 comparator (`trace/rdp1.txt`). With
this the full extraction gives, for every bit k, `r5c_bk_x = NOT((slk AND r5_bk_q) OR
r5c_bk_nor)`: the scan line counter is compared with R5 bit for bit.

## Route (the same for all five, west to east)

| Stretch | Layer | Ends |
|---|---|---|
| x 4720 to 4925 / 4968 | poly | pad with contact |
| to x 5615 / 5658 | metal, over the vertical poly bus x 5000-5450 (no contact) | pad with contact |
| to x 6152 / 6196 | poly | pad with contact |
| to x 7438 / 7482 | metal | pad with contact |
| to x 11032 / 11076 | poly, through the central datapath's channel 2 (no contact) | pad with contact |
| east to x 11178-11352, south, (east) | metal, nested corners | pad with contact at x 11305 / 11345 |
| east to the R5 comparator | poly | contact under a counter track |

Pads alternate between two x positions from line to line. Line y at the west end:
`sl3` 6498, `sl2` 6541, `sl1` 6586, `sl4` 6626, `sl0` 6673 (the order in which the
counter's tracks arrive, `notes/blocks/urch.md`).

After the nested corners the lines lie at y 6645, 6690, 6740, 6782, 6826. At
x 11730-11930 **all five step up one line position** by nested bends (3.3x view
`c5b.png`: each line turns north for 43 px and continues east one position higher; a
sixth line, on the top position west of the knot, leaves north there, and a new line
starts on the bottom position east of it). East of the knot: `sl3` y 6605, `sl2` 6648,
`sl1` 6690, `sl4` 6732, `sl0` 6775, which are the y of the five contacts in the routing
zone of the upper right datapath: (14660,6603), (14268,6645), (13878,6690), (15050,6732),
(13498,6775), under the counter tracks of bits 3, 2, 1, 4, 0.

## How sure

- Metal stretches: `tools/follow.py` for the two long ones and the cornered one; the
  short one over the poly bus from a 1.6x metal view (the follower cannot start there:
  a poly bar crosses the line every 45 px).
- Poly stretches: followed by eye in the clean shot at 1.0-1.3x; channel 2 was read end
  to end earlier (no contact on any of its lines).
- The knot is read from one 3.3x view. Its reading is supported by the result: the five
  lines arrive on exactly the five line positions that the comparator's contacts use,
  and the bits come out in the order 0, 1, 2, 3, 4 across the slices from left to right.
  A wrong reading of the knot would have scrambled that order.

## Not done

The sixth line that leaves the knot northwards, and the line that starts on the bottom
position east of it (y 6820; in the routing zone this position carries R7's match line
westwards: not followed between).

## Corrections (coordinator, from the handoff of `busl` run 19, 2026-11-24)

- The row "y 6452" beside the five lines is `rcs_thin_e`'s (`busl` piece `yc`). `sl3`'s corner beside
  the box (11703,6556) has its west edge at x 11735-11738, where `P 11345,6645 x11760 y6605 x14670`
  puts the bend at x 11751-11769 (geometry only: about 18 px of field remain between it and `busl`'s
  column either way; not changed).
