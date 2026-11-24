# Trunks: long-distance wiring of the global signals

Trace: `trace/trunks.txt` (requires clock, inrow, pads_in_top). Coordinates are
metal-shot pixels. "L" = left, "R" = right, "U" = up (smaller y), "D" = down.

## Status

State at the end of the first session (2026-11-15). Everything below is in
`trace/trunks.txt` unless it says "not drawn".

| Signal | Followed to | Left open |
|---|---|---|
| `ck_out` | all four routes out of the clock block, to their entry points | top end of the left-edge trunk (x 2504; seen only at 0.5x above y 18300); `ck_out` #1 beyond x 10230; the taps |
| `ck_a` | rail up the right edge of the mid-right array to its end; second entry at the array's bottom row | nothing outside the array |
| `ck_b` | bottom row of the mid-right array (its only route) | nothing outside the array |
| S (`rst_ck`, the clock notes' `rst_ck`) | gate g5; the long run along the bottom and up the left bus field to (6690,8366), still running | where it ends; its taps |
| X (input of gate 0, so S = NOT X) | back to (13566,15880) in the channel right of the mid-right array | **its source** (most likely `ck_b`, not shown) |
| `e_b` | entry below the decode logic at (16170,17690); seen running up to y 16400 | where it ends |
| `rw_d`, `rs_d`, `cs_d` | entry below the decode logic; verticals to about y 16200 | upper ends of `rw_d`, `rs_d` |
| `res_b`, `lpstb_b` | routing channel of the top-left logic, to y 3790 | further down |
| `clk` | contact (7500,18772) on a cell row by the CUDISP pad | that row |
| `clk_b` | not looked at (it enters the clock driver logic; whether it also leaves the clock block is not known) | all |

The line the clock notes call `rst_ck` is **not** `ck_a` (Ambiguities A1).

## How to use this file

- "Trunk segments by position" (next section) is the look-up table: find a wire by
  its x or y and read off the net.
- Per-signal sections give the route in order, every branch, and every entry point
  into a block.
- Everything listed was followed on the photos junction by junction unless marked
  "(not verified)" or "(seen at low zoom)".

## Trunk segments by position

Vertical segments, sorted by x:

| x | y range | Layer | Net | Notes |
|---|---|---|---|---|
| 2495-2514 | about 6000-18952 | metal | `ck_out` | left-edge trunk, continues from the bottom trunk at the corner (2504,18952). Followed at 1.8x to y 18300 (tap contact at 2500,18385 to a poly going right), above that at 0.5x only; top end not found |
| 5265-5290 | 2553-3790+ | metal | `res_b` | from contact (5277,2553); runs down a routing channel of the top-left logic, still running at y 3790 |
| 5268-5290 | 2140-2553 | poly | `res_b` | under the wide bus y 2185-2505 |
| 5310-5330 | 2553-3790+ | metal | `lpstb_b` | from contact (5343,2553) (its pad reaches left to x 5320); beside `res_b` |
| 5335-5355 | 2093-2553 | poly | `lpstb_b` | under the wide bus |
| 6135-6160 | 18850-18948 | poly | `ck_out` | tap from the bottom trunk, contact (6148,18948), up into the cell at 5950-6160 x 18790-18940 |
| 6570-6595 | 1965-2095 | poly | `lpstb_b` | under the supply rail y 2004-2052 |
| 6698-6722 | 1965-2095 | poly | `res_b` | under the supply rail |
| 6750-6765 | 8366-8452 | metal | S | then left along y 8357-8375 |
| 6789-6807 | 13331-17990 | metal | S | innermost (rightmost) line of the bundle up the left bus field below y 17090; poly link 16170-16515 under the supply buses; passes over the horizontal polys of the grid at y 13400-14800 without contact |
| 6790-6808 | 17990-18428 | poly | S | from contact (6797,18428) up under nine bus lines to contact (6798,17990) |
| 6853-6870 | 8990-13331 | metal | S | after the step right at y 13322-13340 (every line of the bundle steps right there, one after another, y 13290-13600); then diagonal to (7034,8815) |
| 6922-6940 | 8452-8548 | metal | S | |
| 7027-7047 | 8535-8797 | poly | S | between contacts (7034,8797) and (7034,8535) |
| 9309-9347 | 18945-19253 | poly (wide) | `ck_out` | between contacts (9337,18945) and (9337,19253); passes under the VCC bus y 19095-19145 |
| 9440-9480 | 18760-19335 | poly (wide) | `clk` | CLK pin node; from contact (9467,19335); passes under both `ck_out` lines and the VCC bus. Do not confuse with the `ck_out` wide poly 130 px to its left |
| 9455-9475 | 19335-19902 | metal | `clk` | up from the line along the bottom of the clock block |
| 10300-10320 | 17908-18473 | metal | `ck_out` | "ck_out #1": left arm of the ring; turns left at y 17908 |
| 10330-10370 | 18555-18926 | poly (wide) | `ck_out` | contacts (10356,18926) and (10355,18555); under the VCC band and the S line (y 18590-18612) |
| 10347-10365 | 18473-18555 | metal | `ck_out` | from the wide poly's top contact to the ring |
| 10349-10368 | 17560-18390 | metal | not identified ("c") | comes down between the two `ck_out` verticals, turns right at y 18375-18395 to a contact at (10398,18428); has a branch at y 17633-17658 to a vertical x 10392-10410 going up. There is also a poly under it |
| 10389-10408 | 17689-18342 | metal | `ck_out` | "ck_out #2": right arm of the ring |
| 10392-10410 | <17560-17635 | metal | not identified ("c") | branch of "c"; do not confuse with `ck_out` #2 below it |
| 10432-10452 | 18342-18473 | metal | `ck_out` | ring, right side |
| 10430-10450 | 17733-18312 | metal | not identified ("e") | from contact (10440,17733) down to a contact at (10480,18297), then poly right under the wide metal x 10548-10598 to bus line L2 |
| 10433-10450 | <16880-17689 | metal | `ck_out` | "ck_out #2" continues up the left side of the gate column x 10450-10750 (contacts on it at about y 17234 and 17168; at 0.5x it runs on to about y 14700 with a contact every 200-250 px) |
| 10438-10497 | 18800-19005 | diffusion | (VCC strip of an island device) | gate = `ck_out` branch W |
| 10848-10867 | 19015-19306 | metal | `ck_out` | joins the clock trace; corner contact at (10853,19015) |
| 11000-11040 | 18322-19032 | poly (wide) | `ck_out` | passes under the VCC band and bus lines L4, L5, L6 without contact |
| 12513-12533 | 16900-16996 | metal | `ck_b` | entry into the mid-right array, bottom row |
| 12603-12624 | 16800-16953 | metal | `ck_a` | from contact (12631,16954) up into the mid-right array, bottom row |
| 12733-12757 | 16950-18471 | poly | `ck_a` | long poly from contact (12740,18471) up under the whole bus field (continuity between y 17050 and 18220 seen at 0.9x only) |
| 13000-13035 | 18455-18772 | poly | `ck_b` | from the end of line B up through the VCC band |
| 13012-13033 | 16995-18469 | metal | `ck_b` | ends at contact (13023,16995) |
| 13013-13037 | 7270-16945 | metal | `ck_a` | rail up the right edge of the mid-right array; a contact to a poly going left at every row (y 16570, 16090, 15624, 15140, ... every 477). Top end at y 7270 lies over a poly band (y 7265-7292) without a visible contact. Straightness between the ends seen at 0.5x |
| 13055-13077 | 16952-18471 | metal | `ck_a` | jogs left to x 13025 at y 16943-16960 |
| 13085-13120 | 18455-18724 | poly | `ck_a` | from the end of line A up through the VCC band |
| 13120-13145 | <15400-16412 | metal | not identified | starts at contact (13130,16412), whose poly goes left along y 16440-16462 under the `ck_a` rail into the mid-right array. **Not `ck_out`**, although it is in line with the `ck_out` vertical below it |
| 13122-13143 | 16562-18337 | metal | `ck_out` | ends at contact (13131,16562) |
| 13192-13212 | 18385-18775 | poly | S | see `S` below |
| 13555-13578 | <15880-16188 | metal | X | continues up the channel (not followed) |
| 13660-13684 | 16190-16822 | metal | X | from contact (13655,16822) up to contact (13672,16190), which also taps a poly going right into the logic at x 13790 |
| 13703-13727 | 15930-16711 | metal | `ck_out` | rail at the left edge of the logic below the decode array; contacts (13715,16711), (13716,16565), (13716,16490), (13716,15930) |
| 13849 | 18537-18775 | metal | S | output of input-row gate 0 |
| 14535-14552 | 16992-18082 | metal | X | beside the wide VCC vertical x 14585-14630 |
| 16160-16180 | <16400-17691 | metal | `e_b` | **entry: logic below the decode array, right part, from below.** Runs up beside the gate column x 15900-16250 with taps to the left (one at about y 17030); followed at 1x to y 16400, continues |
| 16290-16308 | <15900-17558 | metal | `rw_d` | from contact (16298,17558); taps (contact, poly going left) seen at y 16680, 16290, 16030 |
| 16290-16308 | 17558-17903 | poly | `rw_d` | then diagonal down-right to (16537,18142) |
| 16333-16352 | <15900-17515 | metal | `rs_d` | from contact (16342,17515); taps seen at y 16590, 16335 |
| 16333-16352 | 17515-17873 | poly | `rs_d` | then diagonal to (16584,18115) |
| 16375-16395 | 16170-17560 | metal | `cs_d` | from contact (16385,17560); taps seen at y 17170, 16815, 16430 and the top end at 16170 |
| 16375-16395 | 17560-17847 | poly | `cs_d` | then diagonal to (16625,18087) |
| 16525-16550 | 18142-18634 | poly | `rw_d` | up through the input row's VCC band, from contact (16535,18620) |
| 16572-16596 | 18115-18592 | poly | `rs_d` | from contact (16582,18578) |
| 16610-16640 | 18087-18549 | poly | `cs_d` | from contact (16622,18535) |
| 16660-16705 | 18105-18552 | poly (wide) | `e_b` | from the E buffer (inrow) to contact (16690,18120) |
| 16807-16827 | 17691-18121 | metal | `e_b` | the third of four nested corners here (the others, at x 16765-16785, 16850-16870, 16893-16912, are not identified) |

Horizontal segments, sorted by y:

| y | x range | Layer | Net | Notes |
|---|---|---|---|---|
| 2085-2105 | 5343-6580 | metal | `lpstb_b` | |
| 2130-2150 | 5277-6712 | metal | `res_b` | the lines at the same two y further left (x 3810-4605) are other signals |
| 7265-7292 | <12960-13260 | poly | not identified | passes under the top end of the `ck_a` rail; contact (13260,7280) to a vertical metal x 13250-13270 going up |
| 8357-8375 | <6690-6757 | metal | S | going left; not followed further |
| 8443-8462 | 6757-6937 | metal | S | top one of three nested horizontals (the others: y 8490-8508, 8530-8548 left of x 6870) |
| 8525-8548 | 6932-7034 | metal | S | from contact (7034,8535) |
| 13322-13340 | 6798-6862 | metal | S | step in the bundle |
| 16440-16462 | <12970-13132 | poly | not identified | from contact (13130,16412) left under the `ck_a` rail |
| 16175-16200 | 13566-13690 | metal | X | contact (13672,16190) |
| 16530-16574 | 13131-13715 | poly (wide) | `ck_out` | from contact (13131,16562) right under six vertical metals to contact (13715,16562) |
| 16900-16915 | 13655-13952 | metal | X | from contact (13655,16908) |
| 16943-16960 | 13025-13066 | metal | `ck_a` | jog |
| 16945-16965 | 12631-12745 | poly | `ck_a` | to contact (12631,16954) |
| 16966-17001 | 12878-13040 | poly | `ck_b` | under the wide VCC vertical (x 12935-12980) |
| 16985-17000 | 13952-14543 | metal | X | top line of the bus group above the input row; a poly runs under it for x 14235-14550 |
| 16987-17004 | 12523-12892 | metal | `ck_b` | from contact (12892,16991) left |
| 17677-17698 | 10398-10441 | metal | `ck_out` | jog of `ck_out` #2; a poly lies under it |
| 17683-17700 | 16170-16817 | metal | `e_b` | third of four nested horizontals (17595-17612, 17640-17658, **17683-17700**, 17725-17745); passes over the `rw_d`/`rs_d`/`cs_d` polys |
| 17900-17915 | <10230-10311 | metal | `ck_out` | `ck_out` #1 going left (not yet followed) |
| 18075-18090 | 13782-14543 | metal | X | bottom line of the bus group; contact (13782,18080) to gate 0's input poly |
| 18112-18130 | 16690-16817 | metal | `e_b` | from the contact on the wide poly |
| 18243-18262 (L1) | ...-12807 | metal | not identified | ends at contact (12807,18253); poly on to contact (13216,18251), metal on right |
| 18290-18305 (L2) | 10615-12849 | metal | not identified ("e") | left end: poly under the wide metal x 10548-10598 to contact (10480,18297) and the vertical x 10430-10450. Right end: contact (12849,18296), poly to contact (13176,18297), metal on right |
| 18331-18352 | 10398-10442 | metal | `ck_out` | ring, top side |
| 18335-18350 (L3) | 11027-12807 | metal | `ck_out` | contacts at both ends only |
| 18332-18348 | 12807-13132 | poly | `ck_out` | under the vertical metals |
| 18375-18395 (L4) | 10857-12849 | metal | S | contacts at both ends only |
| 18415-18437 | 6797-10268 | metal / poly | S | **the run to the left**: middle one of three bus lines (y 18383, 18426, 18470). In poly under vertical metals for x 9557-9777, 8382-8602 and 7420-7600 (a contact at each end) |
| 18378-18393 | 12849-13212 | poly | S | then down at x 13200 |
| 18420-18437 (L5) | 10810-12807 | metal | not identified | turns up at x 10803-10820; right end contact (12807,18427), poly to contact (13156,18427), metal on right |
| 18458-18480 | 10358-10600 | poly | `ck_out` | from contact (10358,18470) on the ring to a device at 10600-10710 x 18390-18525 (poly ring round a diffusion; not traced) |
| 18460-18480 (L6, left piece) | 10900-11870 | metal | S | contacts (10900,18470), (11772,18467) to gate g5's poly, (11852,18468) to a poly that goes up to a buried contact on a plain diffusion rectangle (11500-11720 x 18275-18400, added capacitance) |
| 18460-18480 (L6, right piece) | 12095-12740 | metal | `ck_a` | from g6's output poly (x 12110) to contact (12740,18471) |
| 18462-18485 | 10311-10442 | metal | `ck_out` | ring, bottom side; contact (10358,18470) |
| 18590-18612 | 10255-10680 | metal | S | (route from clock.md; seen, not yet re-followed) |
| 18525-18545 | 16428-16622 | metal | `cs_d` | contacts at both ends |
| 18610-18628 | 15170-16535 | metal | `rw_d` | from contact (15170,18618) below the R/W group |
| 18655-18672 | 15802-16582 | metal | `rs_d` | from contact (15802,18663); turns up at x 16572-16592 to contact (16582,18578) |
| 18703-18722 | 15303-... | metal | RS pin node (after protection) | arrives from the right; contact (15303,18712) to the RS group's input poly. Not `rs_d` |
| 18742-18760 | 15930-... | metal | CS pin node (after protection) | arrives from the right; contact (15930,18750) to the CS group's input poly |
| 18700-18722 | ...-13090 | metal | `ck_a` | line A of the clock block; end contact (13085,18709) |
| 18745-18768 | ...-13010 | metal | `ck_b` | line B; end contact (13000,18756) |
| 18745-18778 | 8600-9460 | poly (wide) | `clk` | under the VCC pad's bus |
| 18763-18780 | 7500-8600 | metal | `clk` | to contact (7500,18772) |
| 18765-18785 | 13200-13522 | poly | S | |
| 18765-18785 | 13522-13852 | metal | S | from contact (13522,18774) to the drop from gate 0 |
| 18895-18912 | 2548-3632 | metal | not identified | inner line at the bottom-left corner, between contacts (2548,18905) and (3632,18905); the poly from the latter passes under the `ck_out` trunk without contact |
| 18918-18940 | 9337-9890 | metal | `ck_out` | route N, from contact (9337,18945); steps down to y 18940-18962 at x 9890 |
| 18920-18955 | 8567-9337 | poly (wide) | `ck_out` | route B, under the VCC pad's bus (x 8640-9290) |
| 18938-18957 | 10440-10858 | poly | `ck_out` | branch W, under the VSS and VCC verticals to the island device at 10438-10499 |
| 18940-18957 | 2504-4611, 5320-8567 | metal | `ck_out` | **bottom trunk**. Tap at (6148,18948) |
| 18940-18962 | 9890-10363 | metal | `ck_out` | route N, to contact (10356,18926) |
| 19005-19025 | 10853-11023 | metal | `ck_out` | between the corner contact and the wide poly's foot |
| 19022-19045 | 4611-5320 | metal | `ck_out` | bottom trunk, the stretch that dips down |
| 19240-19262 | 9337-9545 | metal | `ck_out` | from the clock block to contact (9337,19253) |

## ck_out

Source: clock block output stage (NOT CLK). Four routes leave the clock block.

### Route E (east): to the logic below the decode array

1. Vertical metal x 10848-10867 from the clock block (y 19306) up to a corner contact
   at (10853,19015).
2. From that contact, metal right along y 19005-19025 to a contact at (11023,19015),
   the foot of a wide poly line (x 11000-11040).
3. The wide poly runs up through the open area, under the VCC band (y 18518-18665)
   and under bus lines L6, L5, L4 (no contacts; checked at 3x) to a contact at
   (11027,18340).
4. Bus line L3 (metal, y 18335-18350) from there right to a contact at (12807,18339).
   It crosses two polys without contact: at x 11843-11865 (see A1) and at
   x 12733-12757 (`ck_a`).
5. Poly along y 18332-18348 under the wide VCC vertical and the `ck_b`, `ck_a`
   verticals to a contact at (13132,18337).
6. Vertical metal x 13122-13143 up through the bus crossing field to a contact at
   (13131,16562). **The metal ends there.** The vertical metal in line with it above
   y 16412 is a different net.
7. Wide poly right along y 16530-16574, under six vertical metals, to a contact at
   (13715,16562).
8. **Entry: logic below the decode array (left edge).** Vertical metal rail
   x 13703-13727 from contact (13715,16711) up to contact (13716,15930). Taps to the
   right at (13715,16711), (13716,16490) and (13716,15930) (poly or diffusion going
   right into the gates at x 13750+).

### Branch W: an island device

At the corner contact (10853,19015) a poly leaves upwards (x 10838-10858), turns left
at y 18938-18957, passes under the VSS (x 10763-10817) and VCC (x 10677-10730)
verticals and ends as the gate of an island device at 10438-10499 x 18925-18957 of the
kind listed in AMB-006: diffusion strip down from under the VCC band, gate, stub with a
contact at (10465,18987), isolated metal pad over stub and gate. A dead end.

### Route N (north): into the bottom-centre logic

1. From the clock block, metal left along y 19240-19262 to a contact at (9337,19253).
2. Wide poly x 9309-9347 up under the VCC bus to a contact at (9337,18945).
3. Metal right along y 18918-18940, stepping down at x 9890 to y 18940-18962, to a
   contact at (10356,18926).
4. Wide poly x 10330-10370 up through the VCC band and under the S line to a contact
   at (10355,18555).
5. Metal up at x 10347-10365 to a ring of metal: bottom y 18462-18485 (x 10311-10442),
   right side x 10432-10452 up to y 18342, top y 18331-18352 back left to x 10398.
   Two verticals leave it upwards, crossing the diagonal bus lines (which pass under
   in poly):
   - **`ck_out` #1**, x 10300-10320, up to y 17908, then left along y 17900-17915
     (followed to x 10230; not yet further).
   - **`ck_out` #2**, x 10389-10408, up to y 17689, right along y 17677-17698 to
     x 10441, up at x 10433-10450. **Entry: bottom-centre logic, from below, at
     (10441,17680).** It then runs up the left side of the gate column x 10450-10750
     with taps (first two at about y 17234 and 17168; seen at 0.5x up to about
     y 14700).
6. A contact on the ring's bottom at (10358,18470) feeds a poly that runs right along
   y 18458-18480 to a small device at 10600-10710 x 18390-18525 (a poly ring round a
   diffusion; a second poly, from the unidentified vertical "c", also arrives there).
   Not traced.

Lines that look like part of this and are not: "c" (x 10349-10368, between the two
`ck_out` verticals) and "e" (x 10430-10450 below y 18312, which continues the line of
the ring's right side downwards from above). The gap between "e" and the ring's top
(y 18312-18331) was checked at 4x in both metal shots.

### Route B (bottom trunk and left edge)

1. From the contact (9337,18945), wide poly left along y 18920-18955 under the VCC
   pad's bus to a contact at (8567,18946).
2. Metal left along y 18940-18957: x 8567 to 5320; down to y 19022-19045 for
   x 5320-4611; back up to y 18940-18957; on to the bottom-left corner (2504,18952).
   One tap seen: contact (6148,18948), poly up into the cell at 5950-6160 x
   18790-18940. The polys that cross it at x 6950-7540 and at x 3632 have no contact.
3. **Up the left edge: vertical metal x 2495-2514.** Followed at 1.8x to y 18300 (tap
   at (2500,18385): contact to a poly going right) and at 0.5x up to about y 6000,
   where it is still running; the top end has not been found. **Entry: left vertical
   array, all along its left edge.**

## ck_b

1. Line B (metal, y 18745-18768) ends at a contact at (13000,18756).
2. Poly x 13000-13035 up through the VCC band to a contact at (13022,18469).
3. Vertical metal x 13012-13033 up through the bus crossing field to a contact at
   (13023,16995). **The metal ends here.**
4. Poly left along y 16966-17001 under the wide VCC vertical to a contact at
   (12892,16991).
5. Metal left along y 16987-17004 to x 12523, then up.
   **Entry: mid-right array, bottom row, metal going up at x 12513-12533, y 16900.**

## ck_a

1. Line A (metal, y 18700-18722) ends at a contact at (13085,18709).
2. Poly x 13085-13120 up through the VCC band to a contact at (13108,18471).
3. Metal: left to x 13066, up at x 13055-13077 through the bus crossing field to
   y 16952, jog left along y 16943-16960, then up at x 13013-13037.
4. **Entry: mid-right array, right edge.** The vertical metal x 13013-13037 is a rail
   that runs the full height of the array to y 7270. At every row (y 16570, 16090,
   15624, 15140, ..., pitch 477) a contact on the rail feeds a poly that goes left
   into the row (checked at 2.4x for y 16570; the others seen at 0.5-1x).
5. The rail's top end (y 7270) lies over a poly band (y 7265-7292) that runs from
   inside the array right to a contact at (13260,7280) and a vertical metal going up.
   At 5x no contact ring shows between rail and band, so they are taken as not
   joined (A2).

Second route (from gate g6 of the clock block, whose output is on line A according
to the clock trace): poly x 12098-12125 up to contact (12108,18467); bus line L6
right piece (metal, y 18460-18480) right to contact (12740,18471); poly x 12733-12757
up under bus lines L5..L1 (no contacts; checked at 2.25x) and on up to y 16950; left
along y 16945-16965 to a contact at (12631,16954); metal up at x 12603-12624.
**Entry: mid-right array, bottom row, metal going up from (12631,16954).**

## e_b

1. The wide poly from the E buffer (x 16660-16705, inrow trace) comes up through the
   input row's VCC band to a contact at (16690,18120).
2. Metal right along y 18112-18130 to x 16817, up at x 16807-16827 to y 17691, left
   along y 17683-17700 to x 16170, up at x 16160-16180. On the way left it crosses
   over the three polys of `rw_d`, `rs_d`, `cs_d` and seven other vertical polys.
3. **Entry: logic below the decode array, right part (x 15900-16250), from below at
   (16170,17690).** The vertical runs up beside that gate column with taps to the left;
   followed at 1x to y 16400 and still running. Where it ends, and whether it goes on
   to the data bus column, is not known.

`e_n` (NOT E) was not seen leaving the input row.

## rw_d, rs_d, cs_d

Only the `_d` output of each four-inverter group leaves the input row (`_d` = pin
level, four inversions). The `_a`, `_b`, `_c` nodes stay inside the row.

| Net | Leaves the group at | Metal below the row | Poly up through the VCC band | Contact, then vertical metal |
|---|---|---|---|---|
| `rw_d` | contact (15170,18618) | y 18610-18628 to contact (16535,18620) | x 16525-16550 | (16298,17558), x 16290-16308 |
| `rs_d` | contact (15802,18663) | y 18655-18672, up at x 16582 to contact (16582,18578) | x 16572-16596 | (16342,17515), x 16333-16352 |
| `cs_d` | contact (16428,18535) | y 18525-18545 to contact (16622,18535) | x 16610-16640 | (16385,17560), x 16375-16395 |

Above the band the three polys run diagonally up and to the left, parallel, under the
nested metal lines, and straighten at y about 17850-17900. Their left-to-right order
is the same at both ends (they are on one layer and cannot cross): `rw_d`, `rs_d`,
`cs_d`.

**Entry: logic below the decode array, right part, from below, at the three contacts.**
The three vertical metals run up side by side (x 16298, 16342, 16385) with taps
(a contact on the line, poly going left under the neighbours) into the logic at
x < 16250: `cs_d` at y 17170, 16815, 16430 and its top end at about 16170; `rs_d` at
16590, 16335; `rw_d` at 16680, 16290, 16030 (seen at 1x). `rw_d` and `rs_d` carry on
above y 15900 into dense logic; not followed.

The metal lines at y 18703-18722 and y 18742-18760 below the row are the RS and CS pin
nodes arriving from their protection cells, not outputs.

## S: output of input-row gate 0 (`rst_ck`; the clock notes' `rst_ck`)

Source: the single inverter at the left end of the input row (gate 0, x 13730-13925).
S = NOT X. It is one of the most widely distributed lines on the die and behaves like
a clock line, so its identity matters; see "What S is" below.

Route:
1. Gate 0's output contact (13850,18537), metal down at x 13849 to y 18775, left along
   y 18765-18785 to a contact at (13522,18774).
2. Poly left along y 18765-18785 to x 13200, up at x 13192-13212 (under the VCC
   band) to y 18385, left along y 18378-18393 under the vertical metals to a contact
   at (12849,18384).
3. Bus line L4 (metal, y 18375-18395) left to a contact at (10857,18383).
4. Poly down from there (under L5) to a poly link between contacts (10810,18470) and
   (10900,18470).
5. From (10900,18470): bus line L6 left piece right to x 11870: **gate g5 of the clock
   block** (contact 11772,18467) and a capacitor rectangle (contact 11852,18468).
6. From (10810,18470): metal down to contact (10808,18600); poly under the wide metal
   x 10722-10772 to contact (10680,18600); metal left along y 18590-18612 (over the
   `ck_out` wide poly, no contact) to x 10268; up to y 18426; then left along
   y 18415-18437, the middle of three parallel bus lines, with three poly links
   under vertical metals, to a contact at (6797,18428).
7. Poly up under nine bus lines to a contact at (6798,17990); metal up at
   x 6789-6807 as the innermost line of the bundle that climbs the left bus field;
   poly link under the supply buses (contacts 6797,16515 and 6797,16170); on up
   through the grid of horizontal polys (y 13400-14800; no contacts on S) to y 13331;
   step right to x 6853-6870; up to y 8990; diagonal up-right to a contact at
   (7034,8797).
8. Poly up to a contact at (7034,8535); metal left along y 8525-8548, up at
   x 6922-6940, left along y 8443-8462, up at x 6750-6765, left along y 8357-8375.
   Followed to x 6690; **it goes on to the left** (towards the left-centre logic).

No tap was seen on S between gate g5 and (7034,8797): the whole run delivers S to
whatever lies beyond (6690,8366). Checked at 1x for the bottom run and the straight
verticals, at 2-3x at every turn and link.

X, gate 0's input, followed backwards: poly from the gate up to a contact at
(13782,18080); metal right along y 18075-18090 to x 14543; up at x 14535-14552 to
y 16992; left along y 16985-17000 to x 13952; up to y 16907; left to a contact at
(13655,16908); poly up to a contact at (13655,16822); vertical metal x 13660-13684 up
to a contact at (13672,16190) (which also feeds a poly going right into the logic at
x 13790); left along y 16175-16200; up at x 13555-13578. Drawn to y 15880; seen at 1.7x to run
on up to a contact at (13565,15275), where a poly leaves to the right along
y 15255-15290, and probably further to a second contact at (13565,15190). That is in
the channel between the mid-right array and the logic below the decode array.

### What S is (believed, not traced)

Gate g5 of the clock block takes S and, according to the clock trace, puts its output
on line B (`ck_b`); g6 inverts line B onto line A. That is only consistent if S is low
whenever `ck_b` is high, i.e. X is `ck_b` or a copy of it and S is an inverter-made
NOT `ck_b` (a full-swing phase much like `ck_a`). `ck_b`'s only route goes into the
bottom row of the mid-right array, and X comes down the channel beside that array, so
this is plausible; but the join between `ck_b` and X has not been seen. Until it is,
treat S as an unknown clock-like control line.

## res_b, lpstb_b

Both leave the buffers by the top pads the same way (`trace/pads_in_top.txt` ends at
y 1962):

| Net | Contact, poly under the supply rail | Metal going left | Contact, poly under the wide bus | Vertical metal going down |
|---|---|---|---|---|
| `lpstb_b` | (6580,1965) to (6580,2095) | y 2085-2105 to (5343,2093) | to (5343,2553) | x 5310-5330 |
| `res_b` | (6710,1965) to (6712,2095) | down to y 2130-2150, left to (5277,2140) | to (5277,2553) | x 5265-5290 |

**Entry: top-left logic, from above, at y 2553.** The two verticals run down side by
side in a routing channel (more verticals join on their right at x 5350-5490),
crossing many horizontal polys; followed at 1x to y 3790 and still running. No taps
identified.

## clk and clk_b

`clk` (the CLK pin node, after its protection resistor) does more than feed the clock
block: the line along the bottom of that block (y 19892-19912) turns up at
x 9455-9475, becomes a wide poly at contact (9467,19335), runs up under both `ck_out`
lines and the VCC bus to y 18760, turns left under the VCC pad's bus to a contact at
(8600,18770), and continues in metal along y 18763-18780 to a contact at (7500,18772).
That contact sits on a wide poly belonging to a row of three large U-shaped poly gates
at 6945-7540 x 18750-18940, just above the CUDISP pad. **Entry: that cell row** (it
is in nobody's package yet; the bottom `ck_out` trunk passes right under it at
y 18947 without touching it). Not traced.

`clk_b`: not followed. Inside the clock block it comes down V5 into the driver logic;
whether a branch leaves the block was not checked.

## Ambiguities

### A1. `rst_ck` is not `ck_a`: trace/clock.txt has a wrong link

`trace/clock.txt` ends with eight uncertain shapes ("seen at 1.1x; drawn roughly") and
`@alias ck_a rst_ck`. They say that the bus piece feeding gate g5 (L6 left piece) is
joined to gate g6's output through a line at y 18335-18358 with contacts at
(12741,18347) and (11852,18347). Checked at 2.25x-6x in all four shots:

- The line at y 18335-18350 (L3) starts at the contact (11027,18340) on the wide poly
  that comes up from `ck_out`, and ends at the contact (12807,18339). It is `ck_out`.
- At (12741,18347) L3 passes over the poly x 12733-12757 with no contact; that poly
  carries on up beyond y 18220 (to the mid-right array).
- At (11852,18347) the poly from contact (11852,18468) ends in a buried contact on a
  small diffusion pad (11834-11880 x 18340-18385) that is joined by a narrow strip
  (y 18355-18368) to the plain diffusion rectangle 11500-11720 x 18275-18400. L3
  passes over the top of the pad; it does not widen and shows no contact ring.

So L6's left piece is not connected to L6's right piece. What is on it was followed
the other way: L4, the poly at x 13200, and the metal at y 18775 lead to the output
of input-row gate 0.

Consequence for the extraction: with `clock.txt` as it stands, `ck_out`, `ck_a` and
`rst_ck` are shorted (reported as one error by `netlist.py`). Fix in `clock.txt`:
delete the eight `?` shapes after "line A is also the line first labelled rst_ck"
and the `@alias ck_a rst_ck`.

Consequence for the clock block's logic (not re-traced here): gate g5's input is S,
not `ck_a`. The clock notes have g5's output on line B and g6 (input line B) driving
line A; at 5x the two contacts (line B to g6's gate poly at 11985,18757; the long
contact from line A to g6's output at 11965-12030 x 18705-18720) do look real. If so,
g5 pulls `ck_b` low whenever S is high, which only makes sense if X is a `ck_b`-like
signal. X must be traced to its source to settle this.

### A2. Top end of the `ck_a` rail

At (13023,7278) the rail's tip covers a poly band exactly. No ring or pitted box shows
in any shot at 5x, so no contact is drawn. If there is one, `ck_a` also reaches the
vertical metal x 13250-13270 above y 7280.

### A3. Approximate supply shapes in other traces that touch these routes

- `trace/clock.txt` draws the VCC band as `M 10760,18512:13050,18668`. Its left end is
  really at x 10862 (for y 18518-18650); as drawn it covers the S line's contact at
  (10808,18600) and shorts S to VCC in the extraction. Fix: start it at x 10862.
- `trace/inrow.txt` draws the input row's VCC band with its top edge at y 18130; at
  x 16650-16850 the edge is at about y 18160. The `e_b` metal at y 18112-18130 is
  drawn 2 px narrow in `trunks.txt` to stay clear of it.

`tools/trunks_check.py` runs the extraction against copies of the traces with the A1
and A3 corrections applied: 0 errors, 0 warnings.

## Not done

In rough order of value:

1. **Source of X** (and so the meaning of S): resolve the two contacts on the vertical
   metal x 13555-13578 at (13565,15275) and (13565,15190) and follow on from there.
2. Where S goes after (6690,8366).
3. `ck_out` left-edge trunk x 2504: verify above y 18300 at 1x, find its top end and
   whether it turns along the top; list its taps into the left array.
4. `ck_out` #1 along y 17900-17915 west of x 10230.
5. `e_b` above y 16400 (does it reach the data bus column?); `rw_d`, `rs_d` above
   y 15900.
6. `res_b`, `lpstb_b` below y 3790.
7. `clk_b`; the cell row at 6945-7540 x 18750-18940 that `clk` feeds.
8. The unidentified lines met on the way, all listed in the position tables: bus lines
   L1, L2 ("e"), L5; "c"; the vertical x 13120-13145 above y 16412; the three nested
   lines round `e_b`.
9. The small device on `ck_out` at 10600-10710 x 18390-18525.
10. Taps are recorded only where they were seen in passing; none is drawn except the
    one at (6148,18948).

## `res_b` and `lpstb_b` to their ends (coordinating session, 2026-11-16)

Both lines run down the whole top-left logic (x 5277 and x 5320, y 2550-6110) **without a
tap** (metal followed with `tools/follow.py`; class map of the full length shows no pad on
either). At the bottom each turns west onto the pad of one line of a bus of five vertical
poly lines (x 5100-5290, y 6060-6850):

| Signal | Last metal | Contact | Poly bus line |
|---|---|---|---|
| `res_b` | west along y 6055-6080 from x 5280 | (5190,6065) | line 3, x 5180-5205 |
| `lpstb_b` | west along y 6100-6120 from x 5320 | (5232,6105) | line 4, x 5225-5250 |

Line 5 (x 5268-5292) is `rcs_e4` (see `notes/blocks/tla.md`); `res_b`'s metal lies on it
for 217 px without a contact. Lines 1 and 2 are not identified (line 2 has a pad with a
contact at (5145,6110) under a metal from the north). All five lines go south to y 6850,
fan out diagonally and become horizontal metals going east from pads at x 6130-6165,
y 6950-7350. Not followed beyond the pads except `rcs_e4`.

## `h_eq_r0`, `h_eq_r1` and `rst_lat` (coordinating session, 2026-11-16)

- **Joins closed.** The R0 and R1 match lines are single straight metals between the right
  datapath's bundle (y 13480) and the strobe channel's tracks k7 and k8 (y 14690):
  `tools/follow.py` from (13391,14750) north runs to (13431,10010) (the R0 comparator's
  exit) and from (13434,14750) north to (13476,11701) (the R1 comparator's exit). Drawn in
  `trace/trunks.txt`; the labels (former names `h_eq_r0_u`, `h_eq_r1_u`) are now on the real nets.
- **`h_eq_r1` beyond the strobe channel**: track k8's metal (x 13478) turns south-west at
  y 16776, runs down x 13345-13352 to a contact (13345,17645); poly west along y 17647
  under the wide VCC rail to a contact (12805,17647); metal west to x 11851, north to
  y 17476, west to a contact (11240,17475); poly west and then diagonally south-west
  (seen to (10940,17598)): **into the bottom-centre logic**. Not followed further.
- **`rst_lat`** takes the parallel route one line over: x 13435 turns south-west at
  y 16761, down x 13303 to a contact (13303,17688), poly west along y 17691, contact
  (12850,17691), metal west to x 11810, north to y 17514, west to a contact (11288,17517),
  poly west and south-west (seen to (10980,17640)).
- Two more lines run with them (poly y 17557 and y 17603 from pads at (13385,17555) and
  (13425,17600); metal west of x 12805/12850 to pads at (12030,17560) and (12075,17603)):
  not identified, not drawn.
- `h_eq_r0` (track k7) ends inside the strobe channel: contact (13432,15888), poly east
  along y 15889 into the gate column (`notes/blocks/bd1.md`).

The R1 match (end of the displayed part of a line) going to the bottom-centre logic fits
the DISPTMG pad being at the bottom edge; that logic is not traced.

## `ck_out`: the left-edge trunk to its top (2026-11-16)

The bottom trunk (branch (B) of `ck_out`, from the contact (8567,18946)) had been followed
at 1x up the left edge to y 18300. `tools/follow.py`, started at the other end, follows
one metal from (2500,7960) down the left edge (x 2500-2504) and along the bottom to
x 8580: 17,238 px, the same line. Drawn in `trace/trunks.txt`.

- At its top the trunk ends on the pad (2500,7907) of an inverter in the left column of
  the left array (beside upper row 2): `clk_tl` = NOT `ck_out`, the clock of the top-left
  logic (`notes/blocks/tla.md`).
- From the pad it also goes on: west and north on a metal at x 2360-2380 to a contact
  (2365,5847) at the foot of the top-left clusters, then in poly east across a gate under
  the VSS rail at (2620,5849) to a contact (2745,5842). Not followed further.
- Along the left edge the follower lists contact candidates about every 608 px
  (y 8360, 8965, 9573, 10181, 10831, 11440, 12142 ...): the trunk's taps into the left
  column cells of the left array. Not looked at.

## `rst_a` followed west (2026-11-16)

Drawn in `trace/trunks.txt` (last section); views `cache/scratch/bd1/inh1.png` ...
`inh17.png`. From where `trace/bd1.txt` left it at (13480,17150):

| Stretch | Layer | Ends |
|---|---|---|
| south to y 17662, south-west, west along y 17815 under the vertical trunks | poly | pad (12805,17815) |
| west along y 17822, the middle one of three nested Z bends at x 11640-11725, west along y 17650 | metal | pad (11245,17650) |
| west, south-west under ten vertical metals, west along y 17950 | poly | pad (10262,17950) |
| south, short diagonal, west along y 18083, over a pad (10075,18080) | metal | pad (9770,18081) |
| from the pad (10075,18080): north along x 10075, east along y 17770 | poly | pad (10262,17770) |
| north along x 10266, jog at y 17428, north along x 10312 | metal | pad (10310,16950) |
| from that pad west along y 16950 and north | poly | pad (10225,16820) |
| north along x 10225 | metal | ends on a pad with a contact (10226,15912) (`eof`, piece `isrc`, 2026-11-19; the drawing shortened from y 15886) |

**All three ends are followed since 2026-11-19** (`notes/blocks/eof.md`, piece `isrc`): the first is the clear of `bc2`'s latch unit a, the third feeds a metal x 8968 with taps into the gate column x 8650-8800, the second is a gate row at x 10540-10585; no driver on any. As written then, three ends are open: the metal x 10225 north of y 15886; the poly along y 16950 east of
x 10470, into the bottom-centre logic; the bus line west of the pad (9770,18081) (poly
under two vertical metals to a pad at about x 9562, then metal to x 8978 at least). So
`rst_a` is a widely distributed line of the bottom bus, and its driver is at none of
the places looked at so far. The full extraction is unchanged by the new geometry
(one net, no new joins).

On the way: `rst_lat`'s poly from the pad (11288,17517) goes west along y 17515,
south-west to (10960,17640), west along y 17645 over a pad at (10850,17645) on the
vertical metal x 10850, and on west. `h_eq_r1`'s goes west along y 17600 past x 10800.
Neither drawn beyond what the trace had.

## The RA pad drivers' inputs, followed from the pads (2026-11-16, not drawn)

Views `cache/scratch/rdp1/ra0_m.png`, `ra_end_m.png`, `ra_s.png`, `ra_t_a.png`,
`ra_t_m.png`. All metal routes are `tools/follow.py` output.

- `ra0_drv_in`: contact (14935,2090); metal `14850,2097 x14730 y3376 x14996 y3838 x15299
  y4140` to a pad at (15300,4120); poly south along x 15305 to a pad (15305,4762), where a
  metal goes west along y 4764 to x 14338; the poly goes on south to y 4985 and east to a
  pad (15430,4980) with a metal east.
- `ra1_drv_in`: metal `16490,2097 x14965 y2141 x14778 y3333 x15039 y3794 x15342 y4184` to a
  pad (15340,4170); poly south along x 15345 to a pad (15345,4590), where a metal goes west
  along y 4592 to x 14774; the poly goes on to y 4750 and a pad (15385,4762), metal south
  along x 15385 to y 5020 and east.
- A third poly from a pad (15255,4170) (its metal not followed; RA2's by position) runs
  south along x 15255/15215 to a pad (15210,4805); metal east to x 15340 and south.
- Two more metals pass here from the west: `15250,4678 x13692 y4455 x11671` (ends east
  on a pad (15425,4675), poly north) and `15250,4722 x13644 y4500 x11650` (goes on east).

None of these has been joined to the row address selector's outputs (`notes/blocks/ras.md`),
which were followed only to x 7860. The stretch between (x 7860 to 11650, y 4450-4800,
along the top of the central datapath) is the gap.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- Line S (lines 16, 106, 340, 454) does not end in the left-centre logic: from (6690,8366) it runs west
  to (6559,8367), north, west and north through `lc2`'s and `lc1`'s strips without a gate, with one tap
  at (6427,7648), and on into the top-left logic as `rst_ck` (`eof` run 2). S = `rst_ck`.
  R4: part done there (`eof`); chip 1 is damaged on line S at y 16570-16650, 16822, 17483.

## Corrections (coordinator, from the handoffs of 2026-11-19, third batch)

- "source of X": X (`rst_a`) is `lc2`'s first through line (`eof` run 9): the driver
  is at or beyond `lc2`'s east edge (6450,8630).
- `trace/trunks.txt`, `ck_out #1` (`M 10320,17908 x10230`, "followed to x 10230 only"): it lies for 96 px
  on `bd1_n2`'s poly row without a contact and runs on west to a pad at about (9770,17910), with a poly
  beyond to a pad (9595,17905); its end is not drawn (`eof` run 8; R4).

## Corrections (coordinator, from the handoffs of 2026-11-19, fourth batch)

- The signal on track A / line X / the first through line of the left-centre strips, which these notes call a clock, a strobe "once per scan line" or leave without a source, **is the reset**: `rst_a`, the buffered copy of `rst` = NOR(`lpstb_b`, `res_b`) made by `lc1`'s gate 5 (`eof` run 10, piece `isrc5`, firm). `rst_ck`, `rst_rc` and `rst_lat` are further buffered copies of it: high while the RES and LPSTB pins are both low, and only then. The belief "a strobe once per scan line" is withdrawn. So "source of X" is found.
- `res_b` and `lpstb_b` do not end at `lc1`'s NOR: they run on down the left-centre strips and the left bus field to (6366,15000) and (6408,15000) (`eof` run 11, piece `rl`).

## Corrections (coordinator, from the handoffs of 2026-11-20)

- `ck_out #1` "turns left along y 17900-17915 (followed to x 10230; not yet further)": it runs on west, unbroken, to a pad with a contact (9769,17910), then by a poly to a pad (9596,17909) and a metal to a pad (8598,17908), drawn by `eof` (piece `in350`, run 18); from there one metal goes north to the latch behind the ripple counter's clock and a poly west to a pad (8424,17908). Four open ends of `ck_out` there are not followed.

## Corrections (coordinator, from the handoffs of 2026-11-20, `bl0`)

- `res_b` and `lpstb_b` do not end at (6366,15000) and (6408,15000) nor in `bl0`'s gate group: each runs
  on east in poly and south by a track to a pad, (6882,16170) and (6928,16217), and on south in poly
  (drawn to y 16250; `notes/blocks/bl0.md`, piece `pe`). In the gate group they make `lpstb_nres` =
  NOR(NOT `lpstb_b`, `res_b`), which forces the carry into the address counter's row s7.

## Corrections (coordinator, from the handoffs of `busl` run 15, 2026-11-21)

- Taps in the left bus field (R4): none on the one line there between y 8995 and y 15000 (`busl`, under piece `xm`: method and numbers). South of y 15000 and its poly cross-unders are not checked.

## Corrections (coordinator, from the handoffs of `cdp3`, `cdp4` runs 4-15, `eof` runs 36-51 and `regs` runs 5-6, 2026-11-21)

- `rst_lat`'s diagonal from the contact (11288,17517) ("poly west and south-west. Not followed", here and in
  `trace/trunks.txt`): followed by `cdp4` run 12: it ends in a row y 17633-17653 through a pad (10852,17648)
  on the track x 10852, which is `rst_lat` up the east side of the central datapath to y 3592 and into `tr1`'s
  gate row.
- The metal on the track position x 10810 south of y 16430 (a pad (10808,16430), then south to this block's
  piece at y 18458) is a separate metal from `cdp4_w10808`'s track (650 px of bare ground between); y
  16430-18458 of it is undrawn.

## Corrections (coordinator, from the handoffs of `eof` runs 52-54, 2026-11-22)

- `h_eq_r1`, "poly west and south-west" with its diagonal to (10940,17598) (here and in the comment in
  `trace/trunks.txt`): followed by `eof` run 52: the diagonal becomes a row y 17592-17612 west to a column
  x 10432-10448 north, the gate of the pull-down on `bl0_w15566` at (10548,17515). `h_eq_r1` is an alias of
  `h_eq_r1`.

## Corrections (coordinator, from the handoffs of `eof` runs 55-62, 2026-11-23)

- The table row `| 10433-10450 | <16880-17689 | metal | ck_out | "ck_out #2" continues up the left side of the
  gate column ... (contacts on it at about y 17234 and 17168 ...`: the `ck_out` metal ends on the pad
  (10439,17238) (the "contact at about y 17234"); the contact at y 17168 is the pad of another metal, the output
  of the NOR `bc2_w14955` = NOR(`rst_lat`, `ck_out`), which runs north from there. `trace/trunks.txt`'s line
  `M 10311,17908 y18473 x10442 y18342 x10398 y17689 x10441 y16880` now ends `y17238` (`eof`, cdc4d7d; open poly
  at y 17206-17218 in both metal shots, no metal in either chip at y 17175-17199; review round 68 of `eof`).
  The stretch y 16885-17168 is `eof`'s metal of that NOR. R53.
- The poly row y 17772 between x 10075 and the pad (10262,17770), and the poly column x 10225 between y 16820
  and y 16950, each have another net's metal (`eof_w16560`, `eof` run 62) lying on them with no contact: that
  metal is not `rst_a`'s.

## Corrections (coordinator, from the handoffs of `eof` runs 63-68, 2026-11-23)

- `rst_a`'s poly row y 16950 (`P 10470,16950 10225,16950 10225,16820`, drawn to x 10470; "the second is a gate
  row at x 10540-10585", "the poly along y 16950 east of x 10470, into the bottom-centre logic"): it runs on to a
  cap at x ~10546 and is a gate of the NOR `eof_w16996` = NOR(`rst_a`, `eof_w17345`, `eof_w16889`) (drawn by
  `eof` run 63, piece `u16996`), one half of a set/reset latch; it does not cross under the rail.
- An undrawn bus metal at y 18420-18440, between bus line L4 (y 18385) and L6 (y 18470), runs east from
  x 10806 (to x 10990 at least); `eof_w16432` (`eof` run 66) joins it from the north at x 10811 by a thin metal
  x 10804-10817 and is not on `rst_ck`'s contact (10810,18470). Its source is in no trace file.
