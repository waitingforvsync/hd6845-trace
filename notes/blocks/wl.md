# wl: logic west of the 4-bit counter (x 11080-11700, y 6950-9450)

Serial work, started 2026-11-15. Trace: `trace/wl.txt`. Views: `cache/scratch/wl/`.

## Status

All the logic of the block is traced and extracted (23 transistors, no errors): **the clock
generator of the character-row counter** (y 7890-8900), the NOR that makes its step pulse
`p` (y 7650-7860) and two plain inverters (y 7265-7550). The rest of the block is wiring,
also drawn: four horizontal poly bands across its top that run on east over the counters,
three vertical metals that cross it from poly lines in the west to the bus channel below,
and five poly lines that arrive from the bus field in the west.

Not done: where those five poly lines and the bands' west and north ends come from. That
is the bus field x 10850-11080 and the logic north of y 6930 (`amr`), the next pieces.

## What is west of the counters

- x 10850-11700 from y 9450 down to 17000 is not logic: it is a field of about twenty
  vertical metal lines between the central datapath and the counters, with fans of poly
  taps into the central datapath's rows (y 7800-8000, 10300-10700, 13300-13600).
- The logic is one block, x 11080-11660, y 6950-9150, beside rows r0-r3 (the 4-bit counter).
  Two wide vertical rails run through it: **VSS x 11437-11487** and **VCC x 11605-11655**
  (a metal with a contact every 40 px onto a diffusion strip). At its bottom the VSS rail
  turns east along y 9100-9150 and runs into the mid-right array's rail x 11800-11850:
  that is the feed of mra's "vss rail x 11828" (mra A4, now closed).

## The row counter's clock generator (traced)

The two clock lines of the 7-bit counter come up out of the bus channel into this block:

| Line | mra name | Route from the channel |
|---|---|---|
| D, slave clock | `rc_ck_s` | contact (11655,9315), metal west, contact (11519,9315), poly north under the VSS bus, contact (11519,9010), metal x 11512-11533 north to the contact (11517,8150) |
| E, master clock | `rc_ck_m` | poly y 9351-9369 west to x 11565, north, contact (11564,9057), metal x 11553-11578 north to the contact (11567,8622) |

Extracted logic (names `wl_*`):

```
pb     = NOT p                     pull-down 62/22, load 35/40
D      = NOR(e_buf, p)             pull-downs 374/25 and 322/25, depletion load 100/40
E      = NOR(pb, d_buf)            pull-downs 340/20 and 382/23, depletion load 99/40
e_n    = NOT E      (62/22, load 25/87)        e_buf = NOT e_n   (64/27, load 41/35)
d_n    = NOT D      (65/23, load 28/92)        d_buf = NOT d_n   (64/21, load 40/35)
```

So with `p` low, D (slave clock) is high and E (master clock) low; a high `p` pulls D low
at once, and E rises only after `d_buf` has fallen; when `p` falls, E falls (through `pb`)
and D rises only after `e_buf` has fallen. It is a **non-overlapping two-phase generator
driven by the single signal `p`**: E follows `p`, D follows `NOT p`, each delayed past the
other's fall by two inverters. The counter's master latches take the next count while `p`
is high, the slaves pass it on when `p` is low again: the row counter steps once per pulse
of `p`.

### The step pulse `p`

`p` arrives on the vertical metal x 11277-11297 (contact (11285,8362) on the gate band)
from a contact (11287,7752) on the output of a NOR at y 7650-7860:

```
p = NOR(a, b)              pull-downs 44/22 each, load 31/40
a = rst_rc                band H3 (y 7158-7178) -> contact (11240,7168) -> metal x 11232-11252
b = rc_stepreq_n                   poly line y 7915-7937 from the bus field -> contact (11243,7925) -> metal
```

`a` is the line the strobe channel calls `rst_rc` (NOT X, where X is the line whose
inverse, made by input-row gate 0, is the clock block's `rst_ck`: so `a` and `rst_ck` are
two copies of one signal, `NOT X`). In the clock block a high `rst_ck` holds `ck_b` low.
Here a high `a` holds `p` low. So **one core signal stops both the horizontal counter's
master clock and the row counter's step**; what it is has still to be found at its source
(bd1's `rst_a`, which comes from the bottom bus field). While `a` is low, `p = NOT b`: the
row counter steps on a low pulse of `b`.

## The two inverters

```
la_n     = NOT cnt_la_a      (42/22, load 30/38)   y 7265-7380
i2_out   = NOT i2_in       (42/22, load 30/38)   y 7440-7550, mirror image
```

- `cnt_la_a` is the metal x 12276-12294 in the counter array. mra drew it as one line through
  all nineteen rows with no contact. Looked at again from here at 3x: it is **three
  pieces**, cut at the routing channels y 12885-13030 and y 14965-15010 (it passes over the
  other two channels unbroken), each with plain rounded ends, and the bottom end at y 16940
  has no contact either. The top piece (rows r0-r10: the 4-bit and the row counter) has a
  top contact (12285,7124) on band H2's east piece, which runs west to a pad with the
  contact (11350,7122); a metal x 11315-11338 hangs from the pad and ends on the gate of
  this inverter. **Nothing has been found that drives this net**: a contact on the piece
  inside the rows has been missed (re-read item R8 in `notes/work-packages.md`). Until
  then the inverter's input is unknown. The inverter's output goes by a
  buried contact, a poly, the metal x 11277-11297 and band H2's west piece to a contact
  (11092,7122) and leaves north on the metal x 11080-11100.
- I2 (input `rc0`, the row counter's bit 0, traced 2026-11-16 in `trace/fld.txt`; output
  `rc0_n`, which goes to the XOR cell that makes row address bit 0 in interlace sync and
  video, `notes/blocks/fld.md`) takes its input from the bus field on the poly y 7486-7508 and returns its output
  there on the poly y 7441-7462.

## Wiring through the block

Horizontal poly bands at the top (all go on east over the top of the mid-right array):

| Band | y | West end | East | Net |
|---|---|---|---|---|
| H0 | 7030-7048 | turns north in poly at x 11345-11362, leaves at y 6930 | under the rails to x 12060, north, then east along y 6943-6962 (into `amr`) | `wl_h0` |
| H1 | 7068-7088 | pad, contact (11155,7078): metal down, jogging west at y 7273, to a contact (11107,7972) on a poly line from the west (y 7960-7982) | pad, contact (11978,7083), metal strap north to a contact (11978,7000) on a poly going north | `wl_h1` |
| H2 west | 7112-7132 | pad, contact (11092,7122), metal x 11080-11100 north | pad, contact (11285,7122): metal down to I1's output | `cnt_la_a_n` |
| H2 east | 7112-7132 | pad, contact (11350,7122): metal down to I1's gate | pad, contact (12285,7124): the line x 12285 down the array | `cnt_la_a` |
| H3 | 7158-7178 | pad, contact (11240,7168): metal down to gate a | into the wiring channel (mrach) | `rst_rc` |
| H4 | 7200-7222 | runs on west into the bus field | feed of mra's line x 12902 (`cnt_gab`); on the way a pad with a contact (11392,7210) under a metal that leaves north (x 11380-11400) | `cnt_gab` |

Vertical metals over the clock drivers (no contact to them). Each steps one pitch east by a
diagonal at y 8500-8600:

| Metal (top / bottom x) | Top end | Bottom end | Net |
|---|---|---|---|
| 11189-11209 / 11235-11255 | contact (11197,7842), poly line y 7830-7850 from the west | bus line B, contact (11655,9228): on east through the channel into rdp2 at (13425,9447) | `cnt_bus_b` |
| 11147-11167 / 11190-11210 | contact (11155,7882), poly line y 7872-7893 | bus line C, contact (11608,9272): **`ck_a`** from the counters' own `ck_a` line | `ck_a` |
| 11101-11121 / 11145-11165 | contact (11106,8060), poly up to the line y 8005-8025 | bus line G, contact (11655,9402): the **R2 match** line from the right datapath | `h_eq_r2` |

So `ck_a` and the R2 match (horizontal sync position) are taken west into the bus field
here, and a signal on bus line B passes between the bus field and the upper right datapath.

### How it is built (for reading the rest of the block)

- Pull-downs are horizontal poly bands across diffusion; the VSS rail runs over a column of
  that diffusion and contacts it between the bands. The two big NORs use one diffusion
  area x 11140-11497 each, crossed by two bands, so each pull-down is 320-380 px wide.
  The bands are fed at one end and run in loops round the area's edge to reach the far
  columns (one crosses a column diagonally).
- Loads are in the right-hand column, under the two clock metals: a strong load is a
  vertical poly x 11557-11597 over a strip between the node (left) and the VCC strip
  (right); a weak load is a poly plate 90 px long over a 25 px strip. Each load gate is
  tied to its node by a buried contact on a short neck of the node's diffusion.
- The signal metals pass over the big diffusion areas without contact. Between the metals
  the diffusion is open and looks pink (boxes with a heavy outline) or greenish in the
  clean shot; under the metals it is tan. The dark lines between are the margins of the
  metal (tracing guide, trap 2), not layout. Open diffusion was told from open field by the
  chip-2 shots: `tools/classmap.py --open`.

## Ports

| Name | Layer | Where | Dir | What |
|---|---|---|---|---|
| `rc_ck_s` | M | (11655,9315) | out | slave clock of the row counter |
| `rc_ck_m` | P | (11640,9360) | out | master clock of the row counter |
| `rc_stepreq_n` | P | (11040,7926) | in | from the bus field: NOT (row counter step), while `a` is low |
| `rc0`, `rc0_n` | P | (11040,7497), (11040,7451) | in, out | inverter I2 |
| `cnt_la_a_n` | M | (11090,6930) | out | NOT `cnt_la_a`, leaves north |
| `cnt_gab` | P / M | (11040,7211); (11390,6930) | ? | band H4: from the bus field, and a branch north |
| `wl_h0` | P | (11353,6930); (12360,6952) | ? | band H0 |
| `wl_h1` | P | (11040,7971); (11979,6930) | ? | band H1 and the poly line y 7960-7982 |
| `cnt_bus_b` | P | (11040,7840) | ? | bus line B's line into the bus field |
| `ck_a` | P | (11040,7882) | out | `ck_a` into the bus field |
| `h_eq_r2` | P | (11040,8015) | out | R2 match into the bus field |
| vss | M | y 9100-9150 at x 11832; x 11434-11478 at y 6930 | - | joins mra's rail; continues north |
| vcc | M | x 11605-11655 at y 6930, continues north | - | |

## Not done

- Sources and sinks of everything in the Ports table that ends at x 11040 or y 6930.
- The bottom end of `cnt_la_a` (y 16942).
- The leftmost vertical metals (x 11010-11080) are bus-field lines and are not drawn.

Tools: `tools/wl_net.py` (extraction report restricted to a box), `tools/wl_px.py` (patch
colours in three shots), `tools/classmap.py --open`.

## The generator is a cell (2026-11-16)

The left array has a second copy of this clock generator, for its two counters
(`notes/blocks/ur.md`). `trace/wl.txt` therefore defines the devices and internal wires
as the cell `wl_ckgen` (tag `rc` here, `lc` there); the rails, the VCC strip, the two
clock metals, and the pad and metal that bring the step signal are drawn outside the
cell for each copy. The extraction of this block is unchanged.

## Corrections (coordinator, from the handoffs of `busl` run 16, 2026-11-21)

- `wl_h1` ("not identified"): its west end is the data input of `tl5`'s latch a in the top-left logic (`busl`, piece `ha`).
