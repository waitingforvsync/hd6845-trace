# dbl: data bus bits 0-3 to the D-pin units of `dbus`

## Status (2026-11-17 08:51, contributor session)

Wiring only (`trace/dbl.txt`), no transistors, no new net names. Stacked on `r3d`.
Data bus bits 0-3 (`db_b0`..`db_b3`) are followed from the right datapath's
routing zone to the wiring field left of the `dbus` column, and down it to a contact in
each of the units 0-3: **bit k ends in unit k**, on a poly that runs east into that unit's
cluster (not traced, so the extraction does not yet join a data line to a pin).

## Route

| Bit | From | East contact | Metal | End contact (poly east into the unit) |
|---|---|---|---|---|
| 0 | tap (16270,9203) on its thin metal x 16274 (`r3d`) | row y 9205 to (16960,9210) | east along y 9210 to x 17125, south to y 9465, east | (17207,9467), unit 0 |
| 1 | the R3 tap (16400,9400), row y 9400 on east | (16985,9400) | x 16985 south to y 9660, east to x 17078, south | (17077,10832), unit 1 |
| 2 | the R3 tap (16615,9355), row y 9355 on east | (17030,9355) | x 17032 south to y 9580, east to x 17166, south | (17165,12200), unit 2 |
| 3 | the R3 tap (16660,9312), row y 9310 on east | (16985,9310) | east along y 9312 to x 17085, south to y 9530, east to x 17210, south | (17208,13563), unit 3 |

The four metals are four of the five vertical lines of `dbus`'s wiring field (x 17078,
17166, 17210 and the short x 17125; the fifth, x 17122 below unit 0, is D1's `P_y`, and
x 17253 is `M_b`). They turn into the field as four nested L's at y 9210-9660
(2.1x, `cache/scratch/r3d/stair.png`; overlay `cache/scratch/dbl/ov1.png`).

Evidence:
- The rows on east of the R3 taps: straight in the chip-2 shot at 2.4x (`r3d/ce.png`).
  Row y 9355 at x 16630-16700: continuous in acid, metal and metal1 at 6x (independent
  review); the clean shot's "oval" there is the ordinary open-poly look.
- Bit 0's tap: a ring in both metal shots and a pad with a green centre in the clean shot
  at 4.5x (`r3d/tap0.png`); the thin metal runs through it north and south (independent
  review of `r3d` found the same at 6x).
- Verticals: `tools/follow.py` started on each line: x 17078 9720-10840, x 17166
  9700-12206, x 17210 9700-13572, one piece each. Its other contact candidates on x 17166
  and x 17210 are plain line, a poly corner and dirt (4x mosaic, `r3d/taps.png`). A poly
  U of another net lies under the x 17210 metal at y 10480-10795 (both arms leave east
  under `M_b`): no ring or pad in either metal shot, so no tap (review, 5x).
- Ends: each metal ends on a ring with a poly leaving east (3-3.5x, `r3d/b1end.png`,
  `b2end.png`, `b3end.png`, `u0.png`). Below bit 1's end a separate metal starts at
  x 17078 on its own contact (17077,10925).

## What this establishes

- The end contacts sit at y 9467, 10832, 12200, 13563, one unit pitch (1366) apart (x 17077
  for bit 1, 17165-17208 for the others). `dbus` traced chain 1 from the D1 pad (and
  chain 0 from D0); chains 2-5 are tagged by position. So the data line numbered bit 1 (by
  `bust`'s register-width match) goes to D1's unit and bit 0 to D0's: an independent check
  of the bit numbering for those two, and consistent for bits 2 and 3. It becomes a join
  to the pins when the clusters are traced.
- Each end's poly runs east to a heavy-outlined box of about 25 x 25 px at x 17300-17325
  with no poly beyond it (independent review, 5x in three shots): the look of a buried
  contact. In unit 0 it sits at the corner of `dbus`'s node N2. It ties to a diffusion: the
  output node of `dbus_drv` in every unit (a buried contact at each node's south-west tab,
  (17314,9466) in unit 0), so **the unit drives the data line** (`dbus`, 2026-11-17, review
  rounds 1, 2 and 4).

## Review

Independently reviewed (2026-11-17): rows, the nested L's (no swap), verticals, ends and
the extraction confirmed. Its corrections (the end's buried-contact look instead of a gate
line; wording for bits 2-3; the poly under bit 3's metal; row y 9355 firm) are in.

## Not done

- The clusters (`dbus`'s "Not done"). Bits 4-7's routes to units 4-7.
