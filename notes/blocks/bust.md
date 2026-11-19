# bust: the bus between the central datapath and the right datapath (queue: busT)

## Status (2026-11-17 08:31, contributor session; corrected after independent review; bit 0 joined)

Wiring drawn (`trace/bust.txt`): twelve of the fourteen lines of `cdp1`'s big channel
from its east edge (x 10845) through the cross-under at x 11230-11700 and east as metal
to their ends at x 12000-16926, and five of the east ends joined to what they feed. No
transistors. (The thirteenth, `cdp1_l4676`, is drawn by `r9m` the same way; the
fourteenth, `c4l0`, does not drop: it is `amr` c0's outer line, below: an input, the counter bit `c4l0`.)


**Names (refresh 2026-11-17).** The data bus lines are now one name per bit, `db_b0`..`db_b7`. The tables below were written when the central datapath's slice lines and the right datapath's `ubus`/`rbus` lines had names of their own; where a row now shows the same name on both sides, read the left as the line of the slice it names and the right as its continuation in the right datapath.

## Route and order

West of the staircase each line is poly; it drops about 65 px by a 45-degree diagonal
under the wide supply metal (lower lines further west, so no two cross) and comes up on a
pad at x 11655 or 11697 (alternating). **Since poly lines cannot cross, the order is the
mapping**; every line was also followed by eye at 1.35x and 2.5x in the clean shot
(`cache/scratch/bust/xu.png`, `dg1.png`, `dg2.png`), and the pads checked at 3x in both
metal shots (`pe.png`: they are separate from the wide metal, which the follower's
default gap bridges). East of the staircase: metal, `tools/follow.py` from each pad,
2,000-5,250 px; the lower eight step down one track at x 13200-13525 (`jog.png`).

| cdp1 line (x 10845) | metal y | east end | joined to |
|---|---|---|---|
| `c4l1` | 4655 | 12000 | `amr` c1's outer line, an input (`c4l1`; alias of `c4l1`); drop seen end to end at 3x (`c0a.png`) |
| `cdp1_l4632` | 4697 | 12390 | `amr` c2's outer line, an input (`c4l2`; `amr_ob_c2`) |
| `cdp1_l4676` | 4740 | 12782 | `amr` c3's outer line, an input (`c4l3`; drawn by `r9m`) |
| `sl_eq_r5` | 4787 | pad (13540,4787) | **R5's match**: poly south to `rdp1`'s poly x 13533-13556 from y 5450 (alias of `sl_eq_r5`) |
| `db_b0` | 4830 / 4850 | pad (13715,4850) | **`db_b0`**: poly south at x 13706 to a pad (13705,5628) (it ends there, above `rdp1`'s eq-line load), metal west along y 5632 and down as `db_b0` (2.7x in four shots, `c5.png`; follower) |
| `db_b1` | 4873 / 4894 | 13848 | **`db_b1`** (poly x 13845 to the data line's top, 5635) |
| `db_b2` | 4916 / 4937 | 14238 | **`db_b2`** |
| `db_b3` | 4959 / 4981 | 14630 | **`db_b3`** |
| `db_b4` | 5002 / 5024 | 15020 | **`db_b4`** |
| `db_b5` | 5045 / 5068 | 15280 | `amr` c1's inner line (data bit 5 into R3); **`db_b5`**: poly to a pad (15275,5628), metal down x 15277 to a pad (15277,6826), poly east under the VCC rail to a pad (15405,6826), `db_b5`'s metal south (3x, `b5.png`) |
| `cdp1_lw1` | 5088 / 5110 | 15584 | a poly south at x 15580 (not drawn) |
| `db_b6` | 5131 / 5153 | 16146 | `amr` c2's inner line (data bit 6 into R3); **`db_b6`**: poly to a pad (16146,5625), metal down x 16144 and west to a pad (16005,6825), poly west under the VCC rail to a pad (15870,6825), metal to `db_b6` (2.5x, `b6.png`) |
| `db_b7` | 5175 / 5196 | 16926 | `amr` c3's inner line (data bit 7 into R3); **`db_b7`**: poly to a pad (16922,5625), metal down x 16926, west to x 16839 and south: the through line on slice s7's strap track that `rdp2`/`rdp3` already identified as `db_b7`'s branch "to the upper array" (drawn from y 9440) |

## What this establishes

- **The data bus bit order of the central datapath**: `cdp1`'s slice bit lines are the
  right datapath's data lines, slice 4 = `db_b1`, slice 3 = `db_b2`, slice 2 =
  `db_b3`, slice 1 = `db_b4` (firm geometry, `tools/unsure.py` does not list them).
  slice 5 = `db_b0` and slice 0 = `db_b5`. That is slice = 5 - bit, the order the glossary already gives
  for R9's comparator
  (`cdp1_b#_b`, "# = 5 minus the bit"). So R8's and R9's bits can be named.
- **R5's match** (vertical total adjust: scan line = R5) leaves the right datapath north
  and runs west on `sl_eq_r5`, through the central datapath's channel unbroken
  (`cdp1` found no contact on it), towards the west logic. Where it is used: not
  followed west of x 8340.
- **`amr`'s lines on the bus** (corrected 2026-11-17 by the trace of `amr`'s slice,
  `notes/blocks/amr.md`): the four outer lines `c4l0`, `c4l1`, `cdp1_l4632`,
  `cdp1_l4676` are **inputs** to `amr` (each ends on two gate contacts there), the 4-bit value
  compared with R3 bits 4-7; they are driven from the west, source not found. The inner
  lines are data bits 4-7, written into R3. The earlier text here called both outputs.

## Not done

1. The east ends left as ports (table).
2. `cdp1_lw1` (east end 15584, a poly south at x 15580): not followed.
   Bit 7 of the upper array not identified. (R3's low-nibble data lines: drawn by `r3d`, data bits 0-3.)
3. Renaming the bus as data bus bits once the coordinator agrees on names (aliases are
   used for now).

## A problem found in `rdp1`'s trace (fix proposed as its own commit)

`rdp1` drew the VCC rail x 13600 from y 5560; the metal shots show no metal there above
y 5650 (`rail.png`, `c5b.png`): it starts at about y 5655. The overhang shorted VCC to the
metal from the bit-0 line's pad to its continuation (y 5632), and the extraction reported it. The
one-line fix to `trace/rdp1.txt` is a separate commit so it can be reviewed on its own.

With `db_b5` joined, the extraction shows one net writing R8's slice-0 bit (`wr_r8`)
and bit 5 of R7, R6 and R4 (`wr_r7`, `wr_r6`, `wr_r4`): one data bus line across the
chip, as expected.

With bits 6 and 7 joined: `db_b6` writes bit 6 of R7, R6, R4 and `db_b7`
writes bit 7 of R0, R1, R2 and R8's row-A slice 2 (which is therefore R8 bit 7, a cursor
skew bit). The eight data lines now joined across the chip:

| Data bit | central datapath line | right datapath |
|---|---|---|
| 0 | `db_b0` (slice 5) | `db_b0` |
| 1 | `db_b1` (slice 4) | `db_b1` |
| 2 | `db_b2` (slice 3) | `db_b2` |
| 3 | `db_b3` (slice 2, row C) | `db_b3` |
| 4 | `db_b4` (slice 1) | `db_b4` |
| 5 | `db_b5` (slice 0, row A) | `db_b5` |
| 6 | `db_b6` (slice 3, row A) = `db_b6` (enters from the west) | `db_b6` |
| 7 | `db_b7` (slice 2, row A) | `db_b7` |

`amr`'s inner lines take bits 5, 6 and 7 (c1, c2, c3) into R3's high nibble.

## West of the central datapath (corrected 2026-11-17 07:15)

The through-lines leave `cdp1`'s west edge (x 8340) as poly. **Between x 8215 and 8345
every row steps down one track** by nested L's (vertical legs at x 8337, 8297, 8262,
8230; 3x in both stripped shots, `stair2.png`, and `stair.png` at 2.1x). The first
drawing ran them straight, which put every west pad on the line one track too high; an
independent review of `r9m-route` found the step, and this was redrawn and checked by
overlay (`rv_bust/fixstair.png` in the reviewer worktree). The rows west of the step end
on a staircase of pads at x 7810-7860, from which metals run west:

| cdp1 line (east of the step) | west row, pad | metal west | `amr` |
|---|---|---|---|
| `c4l0` | y 4500, pad about (7860,4500) | not followed | c0 outer |
| `c4l1` | y 4547, pad (7810,4547) | west to x 7532, south to (7535,4619), end not looked at | c1 outer |
| `cdp1_l4632` | y 4592, pad (7848,4592) | west, south, west along y 4657 to (6913,4658), across the crossing field | c2 outer |
| `cdp1_l4676` | y 4635, pad (7830,4635) | west, south, west along y 4704 to (6921,4699), across the crossing field | c3 outer |
| (none) | y 4676, pad (7855,4676) | `r9m`'s `sl_eq_r5_n`; the row turns south near x 8190 | - |

`sl_eq_r5` (R5's match): not drawn west of `cdp1` (a straight guess crossed `ras`
geometry; with the step, it probably comes from the row that turns south at x 8190 or
the pad near (8245,4718): to be read).

### Across the crossing field to the top-left logic

The two metals that reach the crossing field under the three rails (x 6450-6960) end on
pads at matching y on both sides: (6960,4655)/(6460,4657) and (6923,4695)/(6470,4702)
(3.4x, `cfe.png`; `hop3.png`). The polys across are drawn `?P` (not seen end to end).
West of it they run along y 4660 / 4702, south along x 5972 / 6016, and end on contacts
onto poly pads (5885,5893) and (5922,5935) into the untraced top-left logic (2.7x,
`we.png`). So **`amr` c2's and c3's outer lines** (by the corrected mapping; inputs, the counter `c4l`) come from the
top-left logic near (5900,5900); c1's ends at (7535,4619) (not looked at) and c0's west
end is not followed. None of them is `ra_eq_r9` (that is R9's match:
`notes/blocks/r9m.md`, correction).

## `amr`'s slice c0: its two lines drawn (inputs: see `notes/blocks/amr.md`)

c0's top contacts are at (11523,5585) and (11607,5585), each with a metal down the slice
to y 6302-6312 as in c1-c3 (follower; 3x, `cache/scratch/bust/c0t.png`). Its polys run
north, 45 degrees north-east under the supply metal, and north beside the staircase
(overlay at 1x on the clean shot, `c0ov.png`):

- **inner output** -> along x 11740 to a contact (11738,5000) on the bus metal y 5002,
  i.e. **data bit 4** (`db_b4`) (4x in four shots, `c0e.png`);
- **outer output** -> along x 11786, 45 degrees north-west to (11640,4544), and west as
  **`c4l0`**, the top through-line. It passes `rab`'s bit-0 pad with a dark edge
  between them (5x, `c0c.png`): `rax_o0` has no second driver.

So all four of `amr`'s slices put an outer output on a through-line into the west logic
(c0 `c4l0`, c1 `c4l1`, c2 `cdp1_l4632`, c3 `cdp1_l4676`), and an
inner output on a data bus bit (c0 bit 4, c1 bit 5, c2 bit 6, c3 bit 7). Four slices,
data bits 4-7, and one result each to the west: the shape of a read-back or comparison
unit on the upper nibble. That's a guess from the wiring; the slice is not traced.

## Check: the register widths the data bus now gives

`tools/bust_fanout.py` lists, from the extraction, the write strobes of the register bits
on each data line (merged tree, 2026-11-17):

| Data line | Written into |
|---|---|
| bit 0, bit 1, bit 4 | R4, R5, R6, R7, R8, R9 |
| bit 2, bit 3 | R4, R5, R6, R7, R9 |
| bit 5 | R4, R6, R7, R8 |
| bit 6 | R4, R6, R7 |
| bit 7 | R0, R1, R2, R8 |
| `db_b6` (not yet joined to a data line) | R8 |

(R0-R2 bits 0-6 are on `rbus`, which `rdp2`/`rdp3` traced; R10-R15 are not yet on these
lines.) This is exactly the datasheet's layout, and nothing in the trace assumed it:
R5 and R9 are 5 bits (0-4), R4, R6 and R7 are 7 bits (0-6), and R8 has bits 0, 1, 4, 5, 7
plus the bit line of row A's slice 3, so **that line is data bit 6 and row A's slice 3 is R8 bit 6** (the datasheet's R8 is bits 0-1, 4-5,
6-7). **Prediction**: that bit line joins the write-line link y 5024 (bit 6) somewhere west of the central
datapath (it leaves `cdp1` towards `tc1`, as `db_b6`).

**Confirmed** (same session): `db_b6`'s metal runs on south along x 8075 and has a contact
(8078,5020) on the poly y 5024 that enters `cdp1` from the west as `db_b6` (3x,
`lw2w.png`; ring in the metal shot; the poly band continuous to x 8340 in the chip-2
stripped shot, column profiles at x 8110, 8240, 8310). Drawn; firm (`tools/unsure.py`
does not list it). Bit 6 now writes R4, R6, R7 and R8. The bit-6 group's canonical
name was settled by `zz_joins.txt`; since the refresh it is `db_b6`.

Hence the central datapath rows: **R8 = row A**, slice 5 bit 0, slice 4 bit 1, slice 1
bit 4, slice 0 bit 5, slice 3 bit 6 (by the above), slice 2 bit 7; **R9 = row C**,
slice 5 bit 0 ... slice 1 bit 4. That settles the bit order the "rename" package was
waiting for.

## The right datapath's routing zone (y 9080-9600), where `ubus` meets `rbus`

R0-R2's bits 0-6 are on `db_b0`..`b6` (lower right array, `rdp2`/`rdp3`); the upper
array's are `db_b0`..`b6`. `rbus_bk` sits at the x of `ubus_b(k+2)`: each line shifts
two slices (781 px) east across `rdp2`'s untraced routing zone. Ends (tools/follow.py):

| Bit | `ubus` x, end going south | `rbus` x, top going north | Route (drawn) |
|---|---|---|---|
| 0 | 13455, 9168 | 14235, 9444 | contact (13455,9163), poly down x 13455 under the wide band y 9225-9275 to (13455,9313), metal down x 13452 to (13455,9578), poly east along y 9578, north on x 13866 (outermost nested L), east along y 9445 to the top contact (14238,9445) (`b0_w2.png`, `b0_z2.png`-`b0_z4.png`, `b0_ov.png`) |
| 1 | 13845, 9104 | 14625, 9400 | contact (13842,9102), poly down to (13842,9222), thin metal down through the rows to (13842,9398), poly east along y 9400 to the top contact (four shots at 2.2x, `b1m.png`; `b1r.png`) |
| 2 | 14235, 9104 | 15016, 9356 | contact (14240,9100), poly east along y 9100 to (14862,9097), thin metal down x 14863 to (14862,9355), poly east to the top contact (`b2r.png`, `b2m.png`) |
| 3 | 14625, 9320 | 15406 | contact (14625,9315), poly east along y 9310 to (15402,9310), the top of the metal x 15406 down to `db_b3` (`b3r.png`, `b3a.png`) |
| 4 | 15016, 9276 | 15796 | contact (15018,9272), poly east along y 9270 to (15790,9272) (4x, `b4c.png`), metal x 15796 down to `db_b4` |
| 5 | 15406, 9234 | 16187, 9268 | contact (15407,9232), poly east, step down at x 15838 (3.5x, `b5s.png`), east along y 9266 to the top contact |
| 6 | 15796, 9104 | 16577, 9096 | contact (15795,9100), poly along y 9100 to the top contact (`b6r.png`) |

Each crossing's metal stretches were checked with the follower's metal test in both metal
shots (the only gaps are 5-17 px poly crossings and contact rings). The `rbus` lines are
already named by bit (`rdp3`), so a wrong crossing would show as a name clash in the
extraction; none did. **`tools/bust_fanout.py` now gives, for bits 0-7, the
datasheet's registers** (for bits 0-3 a lower bound, see the review notes below): bit 0, 1 and 4 R0-R2, R4-R9; bit 2 and 3 R0-R2, R4-R7, R9 (no R8);
bit 5 and 6 R0-R2, R4, R6-R8; bit 7 R0-R2, R8.

**Bit 0** (drawn 2026-11-17, after the first review round): the route is in the table. The
earlier reading that `db_b0`'s row turns south "near x 13890" took the second nested L;
the chip-2 shot at 2.2x (`b0_z2.png`) shows three nested L's whose verticals are at
x 13860, 13895 and 13935, and the outermost (top row y 9445, vertical x 13860-13873) is the
one whose foot turns west as bit 0's row y 9578. Every poly stretch was read at 3x or more
(the drop under the wide band at 4.5x in two shots: straight, no track step), the metal
x 13452 with the metal test in both metal shots, and the join changes no transistor count.
The second row y 9615 (contacts (13560,9620) and (13842,9618)) is another net, as before.
With it, bit 0 writes R0-R2 and R4-R9, as the datasheet says (a lower bound: its row runs
on east, below). Independent review (2026-11-17) confirmed every stretch and the corner.

### Review notes on the routing zone and the fan-out check

- The poly rows of bits 0, 1, 2 and 3 do not end at the `rbus` top contacts: rows y 9445
  (past x 16100, review of bit 0 at 1-5x), 9400, 9358 and 9315 run on east past (14625,9400), (15014,9358) and (15410,9316), cross
  x 16839, and appear to reach further pads near x 16400-17030 (independent review, 0.7x
  only). Not drawn; the fan-out for bits 0-3 is therefore a lower bound.
- The register-width check cannot detect a swap of bits 1 and 4, 2 and 3, or 5 and 6
  (identical strobe sets); the order within those pairs rests on the geometry, which the
  review checked. "Exactly the datasheet" leaves out R3 (`wr_r3` reaches no data line yet).

**Correction (coordinator, from the 2026-11-17 handoffs).** Where this file calls `amr`'s lines outputs (the c0 section above,
"an outer output on a through-line into the west logic"), they are inputs: the outer lines are
the left array's 4-bit counter `c4l0`..`c4l3`, run from `urch`'s ends to the slices, and the inner
lines are data bits into R3's high nibble (`notes/blocks/amr.md`). c1's west end "(7535,4619)
(not looked at)" is a corner and goes on west (drawn in `trace/amrw.txt`). The two `?P` rows at
y 4657 and 4700 were seen end to end in both stripped shots by two reviews and can be made firm.

## Note (coordinator, from the handoffs of 2026-11-17/18)

From `tc2`'s review: the `?P` pads on rows y 4657 and y 4700 are drawn about 30 px off the
photographed pads (real: x ~6490 and ~6447); connectivity unaffected
(`cache/scratch/tc2/review-1/w1.png`).

## Corrections (coordinator, from the handoffs of 2026-11-19)

- `sl_eq_r5` (lines 50 and 113, and the comment in `trace/bust.txt`, line 191): its row y 4719 ends at
  x 8331 in a C-shaped poly that is the gate of an inverter (`eof`): `sl_eq_r5_n` = NOT `sl_eq_r5`. The row
  that turns south at x 8190 and the pad (8246,4716) are that inverter's output, not `sl_eq_r5`; the
  metal from the pad (7782,4766) is another net, not looked at.
