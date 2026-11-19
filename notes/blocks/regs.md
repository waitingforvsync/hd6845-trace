# regs: which central-column row is which register (follow tasks from `sel` / `bd3`)

Trace: `trace/regs.txt`. Scratch: `cache/scratch/regs/` (`survey.md`). Started 2026-11-19 14:55 -0600.

## Status

- **Piece 1, the write strobes of R12-R15: traced** (2026-11-19 15:06 -0600). Four wires, no
  transistor, from where `bd3` leaves them (y 17300) to the write line of one register row each.
  Full extraction: 2378 nets (four joins), 4351 transistors, 0 errors, 0 warnings.
- `wr_r12`'s join rests on one uncertain item (a `?M`, Ambiguities 1); the other three joins have
  none (`tools/unsure.py` lists only `wr_r12`).
- Not done: the read selects (`rsel14_buf` .. `rsel17_buf`, `rsel12_buf`, `rsel13_buf`), see Not done.

## Inventory

| What | Where | Notes |
|---|---|---|
| Eight rows west from `bd3`'s tracks | y 17302, 17345, 17388, 17432 (strobes); 17475, 17519, 17562, 17604 (read selects, not drawn) | each track of x 15214-15517 turns west at its row; pitch 43.3 |
| Hop under trunks' X and the VCC rail | x 14456-14714 | poly between pads: east pad x 14714 (rows 17302, 17388) or 14672 (17345, 17432), west pad 14497 or 14456. Straight: eight rows in, eight out, same y (3x, `metal` and `acid1b`) |
| Hop under the vertical trunks | x 12805-13430 | poly between pads 13386 / 13430 and 12805 / 12850, straight (1.85x, both shots); the same cross-under as `wrs`'s four rows above |
| `wr_r13`'s hop | x 11375, y 17340-17428 | poly between two pads under `wr_r15`'s row (4.5x, both shots) |
| Nest west and north | x 11245-11463 | the four lines turn north at x 11463 / 11418 / 11375 / 11331, step 88 px west at y 14785 / 14824 / 14868 / 14915, and run north inside `wrs`'s four |
| Diagonals | (11331,10709)-(10895,10273) `wr_r14`; (11375,10688)-(10938,10251) `wr_r12` | parallel to `wrs`'s; placed by `follow.py --max` in stages, overlay at 1.85x |
| Ends | pads (10935,9532), (11243,10705), (10893,8819), (11243,11830) | each a metal contact on the east end of a poly row |
| Not drawn: a structure on `wr_r12`'s line | x 11320-11400, y 11740-12350 | Ambiguities 1 |

## Logic

No transistor. Four joins (extraction; names gathered by `@alias`, the renames are the refresh's):

| Strobe | Ends on | Row | Bits |
|---|---|---|---|
| `wr_r12` | `cdp3_c_wr`, pad (10935,9532) | `cdp3` row C, register cell x 6 (c2..c7) | 6 |
| `wr_r13` | `cdp3_h_wr`, pad (11243,10705) | `cdp3` row H, register cell x 8 (c0..c7) | 8 |
| `wr_r14` | `cdp3_l8819`, pad (10893,8819) | the line into `cdp3`'s row A (six large cells c2..c7; its branches into the cells are not traced) | 6 (believed, from the row) |
| `wr_r15` | `cdp4_ld8b`, pad (11243,11830) | `cdp4` row R1, lower half: eight latches | 8 |

So, by their strobes: **R12 is `cdp3`'s row C, R13 its row H, R15 `cdp4`'s 8-bit latch row R1
(lower half); R14's strobe is the line into `cdp3`'s row A.** The widths agree with the data sheet
in all four (R12 and R14 six bits, R13 and R15 eight). Traced for R13, R14, R15; marked for R12
(Ambiguities 1). All of it rests on `sel`'s assignment of select lines to register numbers, as in
`wrs`.

`cdp3`'s notes had `cdp3_h_wr` running "on east past x 10990 without a contact": it ends on the
pad (11243,10705). `cdp4`'s strobe row (`cdp4_ld8b`, drawn there to x 10600, "ends not examined")
is one poly row y 11824-11844 east to the pad (11243,11830) (`tl5_tracks.py rows` in the clean
shot: poly all the way, field on both sides).

## Ports

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `wr_r12` | metal | 15214,17290 | in | from `bd3`'s line on T7's position |
| `wr_r14` | metal | 15258,17290 | in | from `bd3` |
| `wr_r15` | metal | 15301,17290 | in | from `bd3` |
| `wr_r13` | metal | 15344,17290 | in | from `bd3` |
| `wr_r12` | poly | 10835,9533 | out | onto `cdp3_c_wr` |
| `wr_r14` | poly | 10835,8818 | out | onto `cdp3_l8819` |
| `wr_r13` | poly | 10835,10709 | out | onto `cdp3_h_wr` |
| `wr_r15` | poly | 10590,11835 | out | onto `cdp4_ld8b` |

## Ambiguities

1. **`wr_r12` across the structure at x 11320-11400, y 11740-12350** (in `bw`'s region; nobody has
   drawn it). The full-width metal from the south stops at (11373,11905); a full-width metal
   starts at (11376,11757) and runs north to row C's pad. Between them `tl5_tracks.py v 11376`
   finds no metal by the follower's test, and profiles (`px.py row` at y 11780-11890) give at most
   red 150-165 in a 6 px peak at x 11380, which is bare-ground level. Sharpened views of both metal
   shots (`rdp3_sharp.py`, `g5.png`) show a thin bright speckled line x 11370-11380 joining the two
   ends, in both chips. Drawn `?M`, 8 px wide.
   What lies beneath (sharpened clean shot, `g4.png`, `g6.png`): a wide diffusion-coloured
   rectangle x 10530-11400, y 11915-12185 with seven contacts in a column at x 10540 (west end,
   beside `cdp4`'s s7 supply rail); at its east end two mirrored units. Top unit: a poly plate
   x 11325-11393, y 11838-11893 over the neck of the rectangle; a strip of the rectangle's colour
   x 11358-11375 from the plate north to y 11757, turning east along y 11742-11756 (seen to
   x 11480, not followed); a heavy-outlined box (11325-11343, 11798-11820) joined to the plate's
   west part, under `wr_r14`'s metal. Bottom unit: plate y 12205-12260, a U-shaped strip down to
   y 12342, box (11373-11392, 12283-12298) under `wr_r12`'s metal. Both boxes show a bright centre
   in a dark ring in both metal shots, and the clean shot reads 163/156/101 at (11330,11812),
   which is the value of the four end pads' contacts (152-169 / 141-166 / 79-101) and not of a
   pass-over (trap 26: 186-203 / 176-182 / 131-139); the L's corner reads 156/152/101 at
   (11380,11752).
   Readings: (a) two depletion loads fed from the rectangle (a supply cross-under), the top one's
   output strip contacted by `wr_r12`'s metal along y 11757-11835, so that the "thin line" is the
   metal in a long contact: an extra pull-up on the long strobe line. Then `wr_r12` is one net
   through the structure, as drawn. (b) Two transistors whose plates are contacted by `wr_r14`
   (top) and `wr_r12` (bottom), with `wr_r12`'s south metal ending on the bottom plate's box: then
   row C's write line would be driven from the top unit's strip and **not be `wr_r12`**.
   Working assumption (a): the thin line is seen in both chips, a metal cannot end at (11373,11905)
   without a contact, and the row widths fit (row C is six bits, as R12). What would settle it:
   tracing the two units (`bw`), following the strip east along y 11748, and finding what the
   column of contacts at x 10540 is on.
   Whether `wr_r14`'s metal contacts the top box at (11331,11808) is likewise open: not drawn.
   `tl5_tracks.py v 11331` shows no break of 25 px there, so `wr_r14`'s own continuity does not
   depend on it.

## Review

(none yet)

## Not done

- The read selects. `rsel16_buf`, `rsel17_buf`, `rsel15_buf`, `rsel14_buf` (bd3's lines at
  x 15388, 15431, 15474, 15517, y 17300) turn west at y 17475, 17519, 17562, 17604 (`follow.py`),
  cross both hops like the strobes (pads east 14714 / 14672, west 14497 / 14456; 13386 / 13430 and
  12805 / 12850; seen in the same views, not drawn), and end on pads at about (11955,17470),
  (11998,17515), (12040,17560), (12085,17605). From each a poly diagonal runs south-west under the
  clock lines to a pad at about x 11450-11520 on the rows y 17725, 17770, 17815, 17860; metal rows
  go on west from those to pads at x 11240-11375 and further poly diagonals south-west (one 1.28x
  view, `r1.png`; which diagonal lands on which row is not read).
- `rsel12_buf` (poly x 14199, south of y 17320) and `rsel13_buf` (poly x 15512, south of y 17700):
  `bd3`'s ends, not followed.
- The structure of Ambiguities 1.
- `cdp3_l8819`'s branches into the row A cells (`cdp3` (continue)).
