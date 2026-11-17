# r9c: what R9 is compared with (x 10840-17660, y 2090-5900)

Serial work, 2026-11-16. Trace: `trace/r9c.txt`. Views in `cache/scratch/rax/`:
`r9cmp_a.png`, `r9cmp2.png`, `gap45.png`, `r9src_m.png`, `r9src_a.png`, `r9src2.png`,
`r9e.png`, `r9f.png` (the lines); `u9a.png`, `u9w.png`, `u9b.png`, `u9e.png`, `u9n.png`,
`u9s.png` (the units and their inputs); overlay check `chkD.png`.

## Result (from the extraction)

    ra0_cmp ... ra4_cmp : each pulled to VSS by one transistor (W/L 50/18) whose gate is
                          the input line of the pad driver of RA0 ... RA4
    cdp1_b#_ne  = R9 bit XOR ra#_cmp              bits 4, 3, 2, 1
    cdp1_b5_ne  = cdp1_b5_a XOR ra0_cmp           bit 0, cdp1_b5_a from the island tc1
    ra_eq_r9   = NOR of the five

**R9 is compared with the row address as it goes to the pins**: the five lines that enter
the RA pad drivers (`ra#_drv_in`; the pad is the inverse of that line) are each taken to
a unit near the right edge, and the units' outputs run 6,500 px west to the comparator
above R9's register. With the units' loads (not traced) each `ra#_cmp` is the inverse of
`ra#_drv_in`, that is, the level of pin RA#. So this compare sits after the row address
selector, after the inverters `rax` and after the stage in front of the pad drivers
(`ral`), while R10's comparator takes the lines before that stage (`rax_o#`).

For RA0 and RA1 the join to the pad driver's input is drawn and extracted
(`ra0_drv_in`, `ra1_drv_in`: the same nets as the gates of the pad cells' first
inverters). For RA2, RA3, RA4 the units' input metals are drawn to where they were
followed and labelled `ra2_drv_in`, `ra3_drv_in`, `ra4_drv_in_u` (open joins): RA2's
ends on the pad (15210,4805) of the third poly that comes down from the pad drivers'
lines; RA3's and RA4's metals end at (16290,5109) and (16202,5153), not looked at.

## The five units (x 17290-17500, y 5190-5870)

One per bit, pitch 130; the top one (bit 0) is flipped upside down and shares its VSS
contact with the second. In each: a horizontal poly (the input) crosses the diffusion
under a wide rail; on one side of the crossing a box with a contact to the rail, on the
other the output band, which reaches west to a heavy dark box (read as a buried contact)
on a poly that goes to a pad with the output's metal.

| Bit | Input poly (gate at y) | Input arrives | Output pad |
|---|---|---|---|
| 0 | 5325 | pad (17135,4975), poly east and south along x 17318 | 17380,5195 |
| 1 | 5410 | pad (17095,5018), along x 17278 | 17335,5455 |
| 2 | 5540 | pad (17135,5062), along x 17238 | 17335,5585 |
| 3 | 5670 | pad (17095,5105), along x 17190 | 17330,5712 |
| 4 | 5805 | pad (17135,5150), run south not seen end to end (`?`) | 17290,5845 |

The five input polys come down between the five output metals. The input pads are fed
by five metals from the west along y 4981, 5025, 5068, 5111, 5155.

## The compare lines (units to `cdp1`)

Each: metal north from the unit's pad, west along y 4770 ... 4938, north to a pad; poly
under two rails (five-wide cross-under at x 16382-16550, y 4130-4435); metal west in a
nest to pads at x 15380-15428, y 3915-4090; poly west under the three metals that come
down to the RA0-RA2 driver polys (no contact: the rings there are the gaps between
metals), bits 0 and 1 turning south to their pads; metal west 3,300 px along
y 4005-4179; poly under the supply metal x 11280-11600 and the four strobe lines into
`cdp1`'s channel B/C.

## Assumptions

1. **The rail the units sit under is VSS.** Followed north to y 4684, west along y 4670
   and up x 16606 to the rails of the band in front of the pad drivers, not to a labelled
   rail. Taken as ground because the gates cross the diffusion under it and the load
   blocks (poly at x 17550-17600) stand towards the next rail east.
2. **Each unit has a load**, so `ra#_cmp` = NOT `ra#_drv_in`. Traced by `dbus` (2026-11-17,
   cell `dbus_r9l` in `trace/dbus.txt`): a load to the rail x 17616-17667, which is VCC
   (metal-continuous with `pads_out`'s `vcc`), so assumption 1 holds too (AMB-012).
3. The buried contacts at the output polys' ends (`?B`).
4. On bits 0 and 1's poly from the pads (14952,4003) and (14995,4048) north and east, a
   metal lies along the same path (bright in the metal shot); the follower ends at the
   pads, so the metal is taken as another net lying on the poly (trap 13).

## How sure

- Every metal stretch: `tools/follow.py`, corners seen on views. Polys: clean shot at
  1.9-2.6x.
- The extraction: five joins of one compare line with one `cdp1` comparator input each,
  in the order bit 0 = slice 5 ... bit 4 = slice 1, and two joins with pad driver
  inputs; nothing else merged. The order agrees with the columns (slice 5 stands in the
  column that is bit 0 in the block below).
- The overlay sits on all five units' pads, rail contacts and gate polys.

## Not done

The units' loads and east halves: traced by `dbus` (above). The pad (17330,5800) on bit 4's input
poly, with a metal going south. RA2-RA4's driver lines to the pad cells. The metal from
RA0's line west to the pad (14340,4764) and its poly north are drawn; the cell they
come from (`ral`) is not traced.
