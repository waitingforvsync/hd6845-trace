# urch: wiring channel east of the left array's counters (x 4240-4720, y 6140-10500)

Serial work, 2026-11-16. Trace: `trace/urch.txt`. Views: `cache/scratch/urch/`, and the
`outs_a.png`, `st*.png`, `top*.png` views in `cache/scratch/ur/`.

## Status

Drawn and extracted (wiring only): the nine counter outputs from their rows to the poly
lines that take them east, as far as x 4720. Not drawn: those poly lines beyond x 4720
(followed by eye, below), the other tracks of the channel, and the logic block at
x 4450-4780, y 8200-10500.

## The outputs

Each bit's master output (`c4l#`, `c5l#`: the poly at the top of its row) runs east out
of the cell to a pad with a contact on a vertical metal track.

| Bit (row) | Pad | Track | Ends on | Then |
|---|---|---|---|---|
| `c4l3` (u0) | (4272,6586) | x 4268-4290 north | contact (4278,6280) | poly east along y 6280 |
| `c4l2` (u1) | (4400,7068) | x 4400-4420 north to y 6240, east | contact (4495,6238) | poly east along y 6239 |
| `c4l1` (u2) | (4358,7548) | x 4358-4380 north to y 6197, east | contact (4535,6196) | poly east along y 6197 |
| `c4l0` (u3) | poly east and north to a pad (4280,7950) | x 4310-4335 north to y 6157, east | contact (4492,6157) | poly east along y 6157 |
| `sl4` (u4) | (4420,8590) | x 4432 north to y 8182, east to x 4632, north | contact (4627,6625) | poly east along y 6626 |
| `sl3` (u5) | (4380,9066) | x 4388 north to y 8138, east to x 4587, north to y 6497, east | contact (4625,6497) | poly east along y 6498 |
| `sl2` (u6) | (4335,9542) | x 4345 north to y 8092, east to x 4543, north | contact (4540,6540) | poly east along y 6541 |
| `sl1` (u7) | (4292,10018) | x 4301 north to y 8047, east to x 4498, north | contact (4495,6585) | poly east along y 6586 |
| `sl0` (u8) | (4283,10490) | north (x 4283, then 4258) to y 7997, east to x 4455, north | contact (4453,6672) | poly east along y 6673 |

The five tracks of the 5-bit counter step east together by nested corners at y 7985-8195
(checked at 2.6x: five separate metals). Metal routes are from `tools/follow.py`; every
end and the staircase were looked at in the metal shot, the pads in the clean shot.

## Where the lines go from x 4720 (followed by eye in the clean shot, NOT drawn)

**5-bit counter.** The five lines (y 6498, 6541, 6586, 6626, 6673) run east as alternating
pieces: poly to pads at x 4905-4960, metal over the vertical poly bus (x 5000-5450) to
pads at x 5610-5660, poly to pads at x 6130-6180, metal over a second set of vertical
polys to pads at x 7455-7500, and then poly: they are five of the thirteen lines of the
central datapath's **channel 2** (`notes/blocks/cdp2.md`: lines at y 6498, 6542, 6584,
6626, 6672, which cross the whole sliced part, x 7600-10850, with no contact). East of
the datapath they end on pads at x 11010-11070; metals go on east, turn south by nested
corners at x 11300-11580, and continue east as poly along y 6600-6710 under the logic
above the counters towards the top of the right datapath (x 13100-13980, where eight
horizontal polys run at y 6400-6710). Not followed pad by pad: which of those is which
is not established.

So the 5-bit counter's value is taken 9,000 px east, past the central datapath without
being used there, to the **upper right datapath** (`rdp1`, not traced). That is where its
comparators must be.

**4-bit counter.** The four lines (y 6157, 6197, 6239, 6280) go east from x 4720 under
the vertical metals at x 4670-4720. Not followed.

## Which counter is which

The 5-bit counter is the **scan line counter**: its five lines are now drawn to the R5
comparator (`notes/blocks/slbus.md`). The 4-bit counter's four lines (y 6157-6280) are
not followed.

## Corrections (coordinator, from the handoffs of 2026-11-19)

- From `lc2`: `sl4`'s horizontal is drawn 10 px south of the metal (photo y 8164-8180). A vertical metal
  x 4420-4442 with pads (4432,8708) and (4432,9186) lies just south of `sl4`'s pad (4420,8590); the
  upper pad's poly leaves west along y 8693-8710. Drawn by neither package.
