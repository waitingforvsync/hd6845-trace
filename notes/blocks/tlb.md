# tlb: the wide metal band north of the top-left strips

Region 2100-6400 x 2180-2500 (carved from `padring`'s, 2026-11-18). Trace: `trace/tlb.txt`.
Run 1: Matt Godbolt (Claude Fable 5.2), 2026-11-19 13:17 -0600.

## Status

**Done.** The band is one VSS plane with seven poly lines under it and no transistor. Four of the seven are
drawn here (two of trunks' pass through, already drawn; the west end is `eof`'s NOR `r5nor`). They give
**four joins between named nets**, all firm (no uncertain item on any of them):

| Join | What it says |
|---|---|
| the wire `tl1` called w3333 = `tl4_w4068` | the data of `tl1`'s third latch is the enable of `tl4`'s latch (which is also `tl4_w4068`, the enable of `tl5`'s latch b) |
| the bus-fan line y 2554 of `tc1` = `c4l_l3` | the 4-bit counter's L3 line (= NOT `tl4_w4243`) also goes east on `tc1`'s top bus track y 2554 |
| `tl4_w5068` (the wire `tl5` called w5500) = `tl4_w5068` | `tl4`'s NOR(`tl4_w4545`, `tl4_w4850`) goes east on `tc1`'s track y 2684 |
| `tl6_p6101` = `tc1_bus2814` | `tl6`'s track x 6059 and `tc1`'s north poly x 7117-7133 are one poly (the track y 2814 itself hangs on `tc1`'s `?M` at x 7140-7164) |

The three rows to `tc1` run on east of the region's edge x 6400 to x 7218, in ground no package holds
(`padring`'s band): drawn to their ends, as a follow task is.

## Inventory

- **The plane** (vss): metal from x 2593 east past x 7240 (not followed further), north edge y 2193. Lower
  edge y 2506 for x 2593-3388, y 2462 for x 3388-4914 except a tab south at x 3645-3770 (onto `tl3`'s west
  rail), y 2505 from x 4914 east. Hanging from it: `eof`'s arm of `r5nor` (x 2593, y 2347-2404), `tl1`'s R1
  (x 2600-2650), `tl2`'s strip, the tab, `tl4`'s RA (x 4940-4995), `tl5`'s RC (x 5081-5127), `tc1`'s rail
  (x 6858-6906). Measured with the metal test (R > 177, G > 128) in both metal shots at 28 vertical cuts and
  one horizontal cut y 2485; views `c1.png`, `c3.png`.
- **Under the plane** (`tools/tlb_scan.py 2590 6420 2210 2250 2300 2350 2380 2420 2450`: poly colour with
  dark edges along seven cuts; only what persists through all cuts is poly, the rest is the fringe pattern
  the clean shot has under this plane): four columns, x 3453-3466, 4536-4549, 5275-5287, 5341-5353. The
  last two are `trunks`' (`res_b`, `lpstb_b`), drawn there. No diffusion, no contact, no transistor.
- **Column x 3460 and column x 4542, joined north of the plane**: `tl2`'s poly (3450-3470, 2500) runs
  north under the plane and under `mal`'s metal y 2142 (no pad, no widening) to a pad with a contact
  (3458,2096); a metal y 2091-2105 runs east 1,090 px to a pad with a contact (4540,2098)
  (`tools/t.sh tlb follow.py 3500 2096 E --gap 16`: end 4540,2098; west: end 3452,2098; one contact candidate
  at x 4370, which is a speck in the clean shot only: `tools/t.sh tlb textmap.py 4340 2080 4400 2115 3` shows
  unbroken metal in both chips, view `a3.png`); from that pad a poly runs south under `mal`'s metal (which
  ends 60 px east on its own contact (4600,2142)) and the plane onto `tl4`'s column (4534-4550, 2500).
  Views `a1.png`, `a2.png` (3.3x, both metal-side and both stripped shots).
- **Three nested polys under the plane's south-east part** (in the clean shot salmon on the fringed ground,
  under the metal all the way): each comes north out of `tl6`'s strip, turns east, and turns south onto
  `tc1`'s bus fan.

  | Net | From (`tl6`, y 2500) | Row y | To (`tc1`, y 2500) |
  |---|---|---|---|
  | `c4l_l3` | x 5877-5897 | 2394-2406 | x 7201-7218 (`c4l_l3`) |
  | `tl4_w5068` | x 5918-5938 (`tl4_w5068`) | 2437-2450 | x 7160-7176 (`tl4_w5068`) |
  | `tl6_p6101` | x 6052-6072 | 2480-2495 | x 7117-7133 (`tc1_bus2814`) |

  Rows: `tools/tlb_scan.py v 2370 2515 5980 6100 6250 6400 6550 6700 6800 6950 7050 7090` (the same three
  bands at all ten x; a fourth band y 2498-2512 it lists is the pink margin of the plane's edge, and the
  extra hits at x 6550 and 6800 are fringe). Corners: `b1.png` (west, 2.2x, three shots), `b3.png` (east,
  3.4x, clean shot and chip-1 metal). The order is kept (outermost west is outermost east); no row steps.
- **West end, x 2100-2593**: `eof`'s NOR `r5nor`, `tl1`'s polys, `mal`'s and the pad ring's verticals at
  x 2098-2160: all drawn by their packages (view `w1.png`, every package outlined). Nothing left.
- **The sliver between the plane's edge y 2462 and y 2500, x 3388-4914**: `sl_eq_r5_n`'s metal (`tl2`, `eof`,
  `tl4`), the two poly columns, bare ground (views `c1.png`, `c2.png`).

## Logic

None of its own. With the joins: `tl1_w5841` = NOT((`ck_out` AND `tl4_w4068`) OR `tl1_w6022`) and
`tl1_w5706` = NOT `tl4_w4068` (inputs identified, logic unchanged; printed so by the extraction).

## Ports

| Name | Layer | Place | Dir | Note |
|---|---|---|---|---|
| `tl4_w4068` | P | (3450-3470, 2506) | ? | onto `tl2`'s poly `tl4_w4068` |
| `tl4_w4068` | P | (4533-4551, 2506) | ? | onto `tl4`'s column |
| `c4l_l3` | P | (5878-5896, 2506) | in | from `tl6`'s poly |
| `c4l_l3` | P | (7200-7218, 2506) | out | onto `c4l_l3`'s poly |
| `tl4_w5068` | P | (5919-5937, 2506) | in | from `tl6`'s poly `tl4_w5068` |
| `tl4_w5068` | P | (7159-7177, 2506) | out | onto `tl4_w5068`'s poly |
| `tl6_p6101` | P | (6053-6071, 2506) | ? | onto `tl6`'s poly |
| `tl6_p6101` | P | (7116-7134, 2506) | ? | onto `tc1_bus2814`'s poly |
| `vss` | M | (7240, 2193-2505) | - | the plane goes on east |
| `vss` | M | (3645-3770, 2500) | - | the tab south onto `tl3`'s west rail |

## Ambiguities

None. (The clean shot is fringed under this plane, so "nothing else under it" rests on poly's dark edges
and salmon colour persisting along a cut: a diffusion without poly under the plane would not be found by
`tlb_scan.py`. None is expected: nothing enters the plane's outline in diffusion at any edge looked at.)

## Review

**Round 1: full review** (2026-11-19 13:23 -0600; a fresh Claude Fable 5.2 reviewer; trace at commit 5748a9e; images
`cache/scratch/tlb/review-1/`, 21 used). Covered the whole package. Told to suspect: the 1,300 px rows under the
plane (a step, a swap, a tap), the corners at both ends of each row, the junctions with the neighbours' stubs
at y 2500-2506, the two crossings under the metal y 2142 and the metal y 2098 (the candidate at x 4370),
anything else under the plane, the plane's lower edge and the tab.

Checked: the rows with `tlb_scan.py v` at 70 cuts (every 20 px, x 5860-7240) and in the clean shot at 3.2x
end to end, chip 1's metal at 1x for the edge lines printing through; both corners at 4.5x in both stripped
shots; every junction with a neighbour's stub at 5x in three shots with all traces outlined (the ring at
(7210,2510) and one at (4540,2480) are in the clean shot only: not contacts); both pads (bright centre in both
metal shots, green hole in the clean shot); both crossings under y 2142 (two edge lines only, text map); the
metal y 2098 at 2.2x in both metal shots and with the follower; the field round both pads (the other
package's poly pad north of (3458,2096) ends at y 2062, a field stripe y 2068-2074 in all four shots); under
the plane with four 1x views and about 96 scan cuts; the rims; the tab at 5x (metal continuous with the plane,
`sl_eq_r5_n` passes under it in poly); the extraction and `unsure.py`.

Findings: none.

Not checked: the rows between the corners at 4x in a chip-2 shot (fringed there: their straightness rests on
the clean shot and chip 1's metal print-through); a diffusion with no poly under the plane (excluded only by
the absence of outlines in chip 1's metal at 1x); the neighbours' own naming of their stubs; the plane east of
x 7430.

Round 1: no findings.

## Not done

- The plane east of x 7240 (`padring`'s band / the top bus): not followed.
- South of y 2500 between x 6400 and 6750 (`tcw` (continue)'s ground): the pad (6413,2617) with its poly
  east, the poly along y 2530 (`tl6_p6143`) and the metals y 2575-2620 are undrawn there (view `e1.png`).
  Not in this package's region.
