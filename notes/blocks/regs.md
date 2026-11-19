# regs: which central-column row is which register (follow tasks from `sel` / `bd3`)

Trace: `trace/regs.txt`. Scratch: `cache/scratch/regs/` (`survey.md`). Started 2026-11-19 14:55 -0600.

## Status

- **Piece 1, the write strobes of R12-R15: traced** (2026-11-19 15:06 -0600). Four wires, no
  transistor, from where `bd3` leaves them (y 17300) to the write line of one register row each.
  Full extraction: 2378 nets (four joins), 4351 transistors, 0 errors, 0 warnings.
- `wr_r12`'s join rests on one uncertain item (a `?M`, Ambiguities 1); the other three joins have
  none (`tools/unsure.py` lists only `wr_r12`). `wr_r12` has a contact onto an undrawn structure in
  `bw`'s region, and `wr_r14` possibly one (Ambiguities 1).
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

1. **The structure at x 11320-11400, y 11740-12350 on `wr_r12`'s and `wr_r14`'s lines** (in `bw`'s
   region; nobody has drawn it). A wide diffusion-coloured rectangle x 10530-11400, y 11915-12185
   with seven contacts in a column at x 10540 (west end, beside `cdp4`'s s7 supply rail) has two
   mirrored units at its east end (sharpened clean shot, `g4.png`, `g6.png`). Top unit: a poly
   plate x 11325-11393, y 11838-11893 over the rectangle's neck; a strip of the rectangle's colour
   x 11358-11375 from the plate north to y 11757, turning east along y 11742-11756 (seen to
   x 11480, not followed); a heavy-outlined box (11325-11343, 11798-11820) joined to the plate's
   west part, under `wr_r14`'s metal. Bottom unit: plate y 12205-12260, a U-shaped strip down to
   y 12342, box (11373-11392, 12283-12300) joined to the plate's east part, under `wr_r12`'s metal.
   - **`wr_r12` contacts the bottom box at (11378,12297): drawn** (found by review round 1). Both
     metal shots have a bright centre 12 px across (red 220) in a dark ring; the clean shot has a
     green hole (154/168/117; `textmap.py 11356 12274 11404 12320`). So the bottom unit's plate is
     on `wr_r12`. The plate itself is not drawn.
   - **`wr_r14` may contact the top box at (11331,11810): drawn `?C` on a `?P` box.** The same ring
     and bright centre in both metal shots; the clean shot reads 152-178 / 146-160 / 95-103 (red
     minus green 6-18), between a hole and a pass-over (trap 26).
   - **`wr_r12` at y 11757-11905: drawn `?M`.** The line's two edge lines (x 11364, 11386) run
     through in both chips, the interior is dim (red 100-160 against 215-240 north and south of
     it), and the clean shot east of the centre line is protected without a break (`px.py col
     11383`). So the metal is there, and one net is the better reading (reviewer and tracer); it
     cannot be shown unbroken from these photos (traps 22, 27). No contact is seen at the north
     end (11376,11750): bright metal between the two edge bars of the strip's east arm, no hole.
   What the units are is not read. With the plate on the strobe that passes over its box, each
   looks like an extra pull-up on one long strobe line (a depletion load whose plate is its
   output, fed from the rectangle as a supply cross-under): believed only. If instead they are
   transistors gated by the strobes, the strips are two more nets (the top one leaves east along
   y 11748). Either way `wr_r12` reaches row C's write line by its own metal; what would settle
   the rest is tracing the two units, the strip east along y 11748 and the contact column at
   x 10540 (`bw`).

## Review

**Round 1, full review, 2026-11-19 15:16 -0600** (fresh Fable reviewer; piece 1, at commit 8e1aa03; 24
images in `cache/scratch/regs/review-1/`). Told to suspect: `wr_r12` across the structure and
over its mirrored unit, `wr_r14`'s metal there, the order of the nests at the corners y 14785-14915
and the turns, the two diagonals, both poly hops, the four end pads and their rows, `wr_r13`'s hop.
Checked at 3.2-5x in `metal`, `metal1`, `acid1b` (hops not in `acid`), with `px.py`, `textmap.py`,
`tl5_tracks.py` and 0.9x views of the long runs: corners, turns, diagonals, the 44 px step, both
hops (eight rows straight), the end pads (a hole each, no metal beyond), the rows y 10709 and
y 11835 (continuous, no pads under the crossing metals), no contact where `wr_r14` crosses row C or
at a poly end beside `wr_r12` at y 12905; a ring at (13218,17425) is in chip 2 only, not a contact.
Could not check: what the two units are; `bd3`'s names; the rows west of x 10570 / 10825.
Findings:
1. Undrawn contact on `wr_r12` at (11378,12297). **Changes a connection** (a contact exists).
   Confirmed by the tracer (`px.py pt`, `textmap.py`): drawn, with the box.
2. Probable contact on `wr_r14` at (11331,11810), borderline in the clean shot. Would change a
   connection. Undecidable: drawn `?C` on a `?P` box, Ambiguities 1.
3. `wr_r12` at y 11757-11905: the metal is there (edge lines through, interior dim); the notes'
   "no metal" was wrong and the `?M` too narrow. Geometry only: `?M` widened to 14 px, notes
   corrected.
`tools/t.sh regs sameconn.py 8e1aa03`: `connections identical`. `.venv/bin/python tools/sameconn.py
8e1aa03`: `connections identical` (the plate the new contact lands on is not drawn, so the
extraction does not change; the finding still counts, because a contact was added).
Round 1: three findings, fixed (one contact added, one marked uncertain, one geometry).

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
