# rax: the five units east of the row address selector (x 7860-8110, y 4700-5470)

Serial work, 2026-11-16. Trace: `trace/rax.txt` (**partial**). Views in
`cache/scratch/rax/`: `rows_acid1b.png`, `rows_metal.png` (the five units, one strip
each), `u4.png`, `q4L.png`, `q4R.png` (one unit at 4.4x in four shots), `cm4.png` (class
map), `pL_m.png`, `pL_a.png` (left margin of three units), `topv.png`, `bot.png` (ends
of the vertical metals); overlay check `chkC.png`.

## Status

Five identical units at the y of the selector's five output polys (4765, 4893, 5133,
5262, 5392). Drawn and extracted: in each, one pull-down transistor (W/L 112/20) from
the unit's output to VSS, gate = the selector output. **Not traced: the load, and
everything in the unit east of x 8000.** With the load taken for granted the unit is an
inverter, `rax_o#` = NOT `ras_o#` (AMB-011).

## What was read (master: the unit of `ras_o3`, poly at y 5252-5272)

- **The rail** x 7930-7985 is VSS: it runs from y 4345 to y 5640 and there steps 45 px
  east to become the rail x 7995-8040 of the central datapath's first column, labelled
  `vss` in `trace/cdp3.txt`/`cdp4.txt` (`bot.png`). One contact per unit, 40 px above
  the unit's poly, on a diffusion box (pits in the clean shot, ring in the metal shot).
- **The selector output's poly** runs east from the selector across the unit and ends,
  rounded, at about x 8035. From x 7888 to x 8000 it lies on diffusion (class map:
  "poly over a channel" in both the part under the thin metal x 7902 and the part under
  the rail; diffusion above and below in both). Above it the diffusion is the VSS box.
  Below it is a band, y 5275-5300, that goes on east to x 8048.
- **The band's west end** is a box under the thin metal (x 7890-7915, y 5292-5314).
  The poly of the unit's second pad (pad at x 7836, 40 px below the selector output's
  poly) comes east over field in the open and ends at the box's west edge in a heavy
  dark box: read as a buried contact. So the band is the node that leaves on the second
  pad: `rax_o#`.

## Assumptions (AMB-011)

1. The diffusion under the thin metal and the diffusion under the rail are one, above
   and below the poly. Between them (x 7918-7935) lies the gap between the two metals,
   where the clean shot's colours do not apply; a narrow dark-outlined feature runs
   down that gap from the poly to y 5312 and could be a separation.
2. The thin metal x 7902 has no contact to the box, although both metal shots show a
   small bright spot on it there (as in AMB-010: bright metal between the box's edge
   lines). The metal runs from a pad (7900,4372) to a pad (7900,5632) through all five
   units; a contact in each would short the five outputs.
3. The heavy dark box at the second pad's poly end is a buried contact, not a gap.
4. There is a load. Candidates seen east of x 8048: a vertical diffusion x 8052-8085
   with a vertical poly x 8085-8100 beside it (class map: poly over a channel) and a
   poly blob at (8058-8085, y+56..+73).

Independent support for "inverter": `notes/blocks/cdp2.md` found that its comparator is
an equality and a magnitude comparison only if its tracks carry the complement of a
value; and the tracks are these outputs.

## Seen in the unit and not understood

- A poly pad under the thin metal x 8027 at the y of the selector output's poly
  (x 8014-8040), with a metal contact (ring in both metal shots). Whether it is the end
  of the selector output's poly or a separate poly is not resolved; the trace stops the
  poly at x 8002.
- A box with a metal contact at (8030, y+50), below the band's east extension.
- Thin metal x 8027 is in short pieces (profile); thin metal x 8068 runs from a pad
  (8070,4372) south to y 5848, east to x 8122 and on south.
- A sixth pad at (7832,5522) west of the column, 130 px below the fifth unit's.

## Not done

The load; the unit east of x 8000; the three thin metals; a unit-by-unit check of the
four copies beyond the strips.

## Note (coordinator, from the handoffs of 2026-11-17/18)

From `tc2`: the thin metal x 8022-8040 is one line, not pieces, with no contact in the units; the
"poly pads with contact" are poly end caps and buried-contact boxes; the load candidates are
settled by `tc2`'s `tc2_rxl` (the units' loads). The unit poly runs on to x 8040, and the
pull-down diffusion may end at x 8017 rather than 8000 (W about 127, not 112): seen, not verified.
