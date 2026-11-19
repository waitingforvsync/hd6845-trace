# regs: which central-column row is which register (follow tasks from `sel` / `bd3`)

Trace: `trace/regs.txt`. Scratch: `cache/scratch/regs/` (`survey.md`). Started 2026-11-19 14:55 -0600.

## Status

- **Piece 1, the write strobes of R12-R15: traced** (2026-11-19 15:06 -0600). Four wires, no
  transistor, from where `bd3` leaves them (y 17300) to the write line of one register row each.
  Full extraction: 2378 nets (four joins), 4351 transistors, 0 errors, 0 warnings.
- `wr_r12`'s join rests on one uncertain item (a `?M`, Ambiguities 1); the other three joins have
  none (`tools/unsure.py` lists only `wr_r12`). `wr_r12` has a contact onto an undrawn structure in
  `bw`'s region, and `wr_r14` possibly one (Ambiguities 1).
- **Piece 2, the read selects of R14-R17: traced** (2026-11-19 15:29 -0600). Four wires, no
  transistor, from `bd3`'s lines (y 17300) to `cdp4`'s four selector lines as `busl` drew them
  (tracks x 6538-6668, to y 15000). Full extraction: 2374 nets (four more joins), 4351 transistors,
  0 errors, 0 warnings. No uncertain item on these joins.
- **Piece 3, the buffered selects of R12 and R13: traced in two parts** (2026-11-19 15:44 -0600). South: from
  `bd3`'s poly ends along the bottom bus to the tracks x 6452 and x 6494 at y 14990, the south edge
  of the left bus field (`busl`'s claimed region). North: the same two wires from y 10400 to the
  west ends of `cdp3`'s read-gate rows `cdp3_gate_e` and `cdp3_gate_f`. **The 4,600 px between
  (y 10400-15000) are read with the follower and not drawn** (they are `busl`'s): two open joins.
  Full extraction: 2374 nets, 4351 transistors, 0 errors, 0 warnings (no new net: each part lies on
  a net that exists).

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
| Read selects: first diagonals | pads (11942,17470), (11984,17514), (12027,17558), (12068,17602) to pads (11592,17730), (11555,17773), (11592,17818), (11552,17862) | four parallel poly diagonals south-west under the clock lines, x + y = 29368, 29434, 29503, 29565 (measured on cuts of the clean shot); order kept (4x, both stripped shots) |
| Second diagonals | pads (11238,17732), (11282,17776), (11324,17819), (11365,17863) to poly rows y 18036, 18080, 18122, 18166 | x + y = 28956, 29023, 29088, 29153. Six diagonals run here; ours are the upper four (the other two start on pads (11350,17945), (11305,17990)) |
| Third diagonals | rows y 18036-18166 at x 10333-10400 to pads (10182,18165), (10138,18210), (10182,18252), (10225,18297) | x + y = 28369, 28438, 28501, 28566. **Seven** rows arrive at x 10450: the top one (y 17990, from a pad (10470,17985)) is another wire and takes the pad (10138,18120) and the metal row y 18124; each of ours lands three rows further down than it arrived (3.2x clean, 5x chip-2 stripped) |
| Straight hops on the rows y 18168, 18212, 18255, 18299 | x 9550-9808; 8382-8638; 7385-7600 | poly between pads under one or two vertical metals; rows straight (1.8x, 3.4x, 2.9x in `metal` and `acid1b`) |
| Corners and tracks | x 6668, 6626, 6582, 6538, y 16515-18299 | each row turns north (nested: the northernmost row takes the easternmost track) |
| Vertical hop | y 16168-16558 | poly between pads under the horizontal metal rows y 16260-16480: pads (6668,16210)/(6668,16558), (6624,16168)/(6626,16515), (6581,16210)/(6582,16558), (6538,16168)/(6538,16515); five columns hop here (the fifth, x 6711, is `eof`'s `bd1_n2` track), all straight (2.7x, both shots) |
| Tracks north | y 15000-16168 | metal to `busl`'s south edge, where `cdp4_sel1`..`4` are drawn; six poly rows cross at y 15070-15190 without a contact |
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

### The buffered selects of R12 and R13 (piece 3)

| Select | Row after the third diagonals | Track at y 15000 | North end (by the follower through `busl`'s region) |
|---|---|---|---|
| `rsel13_buf` | y 18343 | x 6494 | `cdp3_gate_f`, pad (6730,10317): the gates of row F, which pass row H onto bus N |
| `rsel12_buf` | y 18387 | x 6452 | `cdp3_gate_e`, pad (6730,10055): the gates of row E, which pass row C onto bus N |

Route. `rsel12_buf`: `bd3`'s poly x 14199 ends on a pad (14195,17730); metal row y 17736 west, a
metal diagonal (13520,17736)-(13262,17994), pad (13212,17993); poly under the vertical trunks to
pad (12805,17995); metal to the sixth pad of the second diagonals (11305,17990); poly diagonal
(x + y = 29284) to the poly row y 18250; third diagonal (28698) to pad (10225,18385); metal row
y 18386 with the three straight hops (pads 9808/9592, 8638/8425, 7558/7385); north on x 6452; the
vertical hop (pads y 16515 / 16168); north to y 14990. `rsel13_buf`: `bd3`'s poly x 15512 ends on a
pad (15512,17688); metal row y 17691 west through the rail hop (pads 14672/14456), a metal diagonal
(13501,17692)-(13241,17952), pad (13168,17950); poly to pad (12850,17950); metal to the fifth pad
(11350,17946); poly west to x 11271 and diagonal (29219) to the row y 18208; third diagonal (28632)
to pad (10267,18340); metal row y 18342 (pads 9764/9550, 8597/8382, 7600/7428); north on x 6494;
vertical hop (y 16558 / 16210); north to y 14990.

The stretch not drawn, as the follower gives it (`follow.py X 15500 N`, both chips; one 4x view of
the corners at y 12050-12170, `q5.png`): x 6452 north to (6454,12986), east to (6516,12979), north
to (6521,12099), east along y 12095 **on top of `busl`'s poly row `cdp4_bus_s2`** (no pad, no
contact seen: trap 13), a corner north at x 6690, and north to y 10400. x 6494 north to
(6501,13024), east to (6565,13023), north to (6562,12141), east along y 12140, north at x 6735 to
y 10400. North of y 10400 (drawn): x 6690 steps east at y 10270 to x 6733 and ends on the pad
(6730,10055); x 6733 ends on the pad (6730,10317); each pad's poly row runs east to `cdp3`'s edge
(x 7600) under about twenty vertical metals without a pad (1.36x, both stripped shots).

So, **if the middle stretch is as the follower gives it: R12's buffered select reads row C and
R13's reads row H onto bus N**, the same rows their write strobes end on (piece 1): R12 = row C
and R13 = row H from two independent directions, which also supports the marked `wr_r12` join.
Marked, not firm: the two joins are open until the middle is drawn.

### The read selects (piece 2)

| Select | Row after the third diagonals | Track | Joins | Selector source (`cdp4`) |
|---|---|---|---|---|
| `rsel16_buf` | y 18168 | x 6668 | `cdp4_sel4` | c: the 6-bit latch row D (s2..s7) |
| `rsel17_buf` | y 18212 | x 6626 | `cdp4_sel3` | d: the 8-bit latch row C |
| `rsel15_buf` | y 18255 | x 6582 | `cdp4_sel2` | b: the 8-bit latch row R1, lower half |
| `rsel14_buf` | y 18299 | x 6538 | `cdp4_sel1` | a: the 6-bit source from above row R1 (s2..s7) |

So **`cdp4`'s four-way selector is the read multiplexer of R14-R17** (traced: the four joins).
Two things agree with it that were found separately: the widths (R14 and R16 six bits, R15 and R17
eight), and R15, whose write strobe `wr_r15` ends on the same latch row (R1, lower half) that
`rsel15_buf` selects for reading. Rows C and D, loaded together by `bc1_ld_n` (`busl`), are then
R17 and R16, the light pen register (believed, from the data sheet: read only, 14 bits latched by
one event). The 6-bit source a is R14 as read; that it is `cdp3`'s row A, which `wr_r14` strobes,
is not traced (`cdp4` row R1's upper half).

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
| `rsel16_buf`, `rsel17_buf`, `rsel15_buf`, `rsel14_buf` | metal | (15388 / 15431 / 15474 / 15517, 17290) | in | from `bd3`'s lines |
| `rsel16_buf` | metal | 6668,14990 | out | onto `busl`'s `cdp4_sel4` |
| `rsel17_buf` | metal | 6624,14990 | out | onto `cdp4_sel3` |
| `rsel15_buf` | metal | 6581,14990 | out | onto `cdp4_sel2` |
| `rsel14_buf` | metal | 6538,14990 | out | onto `cdp4_sel1` |
| `rsel12_buf` | poly | 14199,17290 | in | from `bd3`'s poly |
| `rsel13_buf` | poly | 15512,17490 | in | from `bd3`'s poly |
| `rsel12_buf` | metal | 6452,14990 | out | into `busl`'s region: track x 6452, undrawn there |
| `rsel13_buf` | metal | 6494,14990 | out | into `busl`'s region: track x 6494, undrawn there |
| `cdp3_gate_e` | metal | 6690,10400 | in | from `busl`'s region: believed `rsel12_buf` |
| `cdp3_gate_f` | metal | 6733,10400 | in | from `busl`'s region: believed `rsel13_buf` |

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
     minus green 6-18, never greener than red; +6 to +30 by the fix check), and the chip-2 stripped
     shot is red over green by 35-50 at the centre, where the real contact on `wr_r12` is
     grey-green: it leans toward a pass-over (trap 26), not a contact.
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
2. **Green stretches under the read selects' tracks** (`tl5_tracks.py v`): (6538, 16115-16150),
   35 px, just north of the hop's pad, where the clean shot has interference colours over an area
   wider than the track; (6626, 17203-17436) and (6626, 17456-17528), (6668, 17446-17496), far too
   long for contacts. Read as not contacts; no pad or ring in the metal shot at 2.7x for the first.
   The same value at x 6917 on all four rows (8-9 px) is one vertical feature beneath, not four
   contacts.

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

**Round 2, fix check, 2026-11-19 15:20 -0600** (fresh Fable reviewer; the changes since 8e1aa03, at
commit 81387d1; three images in `cache/scratch/regs/review-2/`). Change 1 (contact on `wr_r12`):
right; bright centre red 214-229 in both metal shots, green hole red minus green -9 to -18 (the
pad (11243,11830) reads -8 to -25), box is poly as drawn. Change 2 (`?C` on `wr_r14`): uncertain is
the right call, and the photos lean against a contact (no green hole; poly-red in the chip-2
stripped shot); the trace's comment and Ambiguities 1 now say so. Geometry only (a comment).
Change 3 (`?M` 14 px): right, inside the two edge lines, 25 px clear of the `?P` box and of the
metal on x 11331. `tools/t.sh regs sameconn.py 8e1aa03`: `connections identical`.
`.venv/bin/python tools/sameconn.py 8e1aa03`: `connections identical`. After the comment fix,
against 81387d1: both `connections identical` again.
Round 2: no findings that change a connection.

**Round 3, full review of piece 2, 2026-11-19 15:35 -0600** (fresh Fable reviewer; the four read selects, at
commit 1c5b259; 28 images in `cache/scratch/regs/review-3/`). Told to suspect: the third diagonals
(seven rows, an off-by-one), the second and first diagonals, every straight hop, the vertical hop,
the corners, the tracks to y 14990 and the green stretches of Ambiguities 2, the ends on `bd3`'s and
`busl`'s metals, missed taps. Checked: the third diagonals at 4x in `acid1b` and `acid` (five
separate bands to five pads, ours bands 2-5, no off-by-one); the poly rows x 10440-10920 on 13
cuts; the second diagonals at 2.8-4x (six from six pads, ours the upper four); the first diagonals
at 2.4x in three shots (separate in the chip-2 stripped shot, where the debris is absent); all hops
at 2-4x with text rows; the vertical hop at 2.8x; the corners; `tl5_tracks.py` on every straight
metal piece (no stretch over 18 px without metal in both chips); the green stretches (interference
colour, unbroken metal, no ring); no taps (about 1x metal); both ends. Not checked: the second
diagonals under metal at 4x except one passage; the long runs at high zoom; `metal1` as an image.
Round 3: no findings.

## Not done

- **The two open joins**: `rsel12_buf` (6452,14990) to `cdp3_gate_e` (6690,10400) and `rsel13_buf`
  (6494,14990) to `cdp3_gate_f` (6733,10400), through `busl`'s claimed region; route in Logic.
- The wire of the seventh row: from a pad (10470,17985), poly row y 17990, first of the third
  diagonals, pad (10138,18120), metal row y 18124 west through the same hops to x 6708 and (by the
  follower) north on x 6711, which is `eof`'s `bd1_n2` track (drawn there from y 15000 to 16185).
  Not ours; seen, not drawn. A ninth row y 17648 crosses the rail hop too (west pad (14500,17648),
  west end (13316,17803)): not followed.
- The structure of Ambiguities 1.
- `cdp3_l8819`'s branches into the row A cells (`cdp3` (continue)); the source of `cdp4`'s 6-bit
  input a (`cdp4` (continue)).
