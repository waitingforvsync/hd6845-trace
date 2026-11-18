# eof: the end-of-frame lead group (follow tasks; spots across the die)

Queue row `eof` of `notes/work-packages.md`: wires whose ends decide the end-of-frame sequence,
followed to their gates. Only what no other package draws is in `trace/eof.txt`; the rest of each
path is other packages' geometry, named where it is used. Coordinates are metal-shot pixels;
images are in `cache/scratch/eof/`.

## Status

Run 1 (Tom Seddon's session, Claude Fable 5.2; 2026-11-18 23:30 +0000).

- **Task 1, where R4's match goes: done** (piece `r4`, wiring only, no transistors, no uncertain
  items). `rc_eq_r4` is drawn end to end from R4's comparator to its loads: it is the net that
  `rdp3` called `rdp3_n7s9` and `bd1` called `bd1_a`, **the data input of the latch in the gate
  column beside the strobe channel and the input of inverter A there**.
- Tasks 2-4 of the queue row (`sl_eq_r5` west of x 8340; `tcw_a`'s source; `rcs_x1`'s driver):
  not started.

Full extraction with this file: 2,359 nets, 4,230 transistors, 0 errors, 0 warnings; the package
by itself (it loads `rdp3`): 0 errors, 0 warnings.

## Inventory

| Piece | Where | What |
|---|---|---|
| `r4`, link A | x 13416-13667, y 9647-10705 | from `mrach`'s poly end (13425,9663): pad and contact (13433,9665), the upper piece of bundle track L2 (y 9652-9938), pad and contact (13432,9925), poly bar y 9916-9934 east under L3-L6, pad and contact (13650,9925), track L7 south to `rdp3`'s piece at y 10700 |
| `r4`, link B | x 13729-13747, y 13475-14695 | bundle track L9, straight, from `rdp3`'s end (13738,13480) to `bd1`'s track k15 (13738,14690) |

The bundle left of the right datapath has tracks L0..L11 at x 13348 + 43.4 k.

## Logic

Wiring only. What the join gives (traced; equations from the full extraction):

```
rc_eq_r4 = NOR(r4c_b0_x .. r4c_b6_x)                 rdp2: high when the row counter equals R4
bd1_an   = NOT rc_eq_r4                              bd1's inverter A            (firm)
bd1_n1   = NOT(bd1_q OR (inh_lat AND rc_eq_r4))      upper half of bd1's latch   (depends on bd1's ? items)
bd1_n2   : pull-downs (bd1_an AND inh_lat), bd1_n1   lower half; its load is not traced (bd1)
```

`tools/unsure.py --equations`: `rc_eq_r4` FIRM, `bd1_an` FIRM, `bd1_n1` DEPENDS (on `bd1`'s
uncertain items, none of them on this wire). `tools/unsure.py` does not list `rc_eq_r4`: no
uncertain item lies on the path from the comparator's NOR to the two gates.

Believed, not traced (from `notes/blocks/bd1.md`): the two halves are a transparent latch of this
signal, open while `inh_lat` is high; `inh_lat` is a copy of `inh_src`, the signal that also
stops `ck_b` (`inh_ck`) and the row counter's step (`inh_rc`). So **what R4's match does at the
end of the frame goes through this latch**; the latch's lower half (its load, the driver of
`bd1_q`) and where `bd1_n1`, `bd1_n2` and `bd1_an` go are `bd1`'s untraced part (the queue's
`bd1`-`bd3` row).

### The path, north to south

| Stretch | Drawn by | What | Evidence |
|---|---|---|---|
| comparator to the counter channel | `rdp2`, `mrach` | NOR at about (15000,8426); poly west and south to track T6 (= L0), contacts (13348,9360), (13349,9663); poly east along y 9663 to x 13425 | their notes; not re-read |
| **link A** | `eof` | the poly row runs on under L1 (`wr_r4`: no pad, no hole) to a pad with a contact (13433,9665), top of L2's upper piece; that metal ends on a pad with a contact (13432,9925); a poly bar goes east along y 9925 under L3 (`h_eq_r2`), L4, L5 (`rc1`), L6 with no contact, to a pad with a contact (13650,9925), top of L7 | `a_top.png` (2.8x, metal / chip-2 stripped / clean), `a_bar.png` (4x, three shots), overlay `ov_a.png`; text maps of both pads' rows and of the whole bar in both metal shots and the clean shot (each end pad: bright centre in a dark ring in both chips and a green hole in the clean shot; the bar plain between); `tools/follow.py` on both metals; `tools/tla_contacts.py` on both: no candidate |
| L7, L6, L5, link, L9 | `rdp3` | L7 from y 10700, jog west onto L6 at y 11507, onto L5 at y 12313, contact (13565,12826), poly link east under L6 and L7, contact (13736,12826), L9 south to y 13480 | read again here from text: `tools/follow.py 13651 10710 S` gives the two jogs and the end as drawn; its three contact candidates ((13651,11346), (13564,12585), (13563,12611)) are field under whole metal (text maps); the link's poly is continuous under L6 and L7 with no hole. The east contact: see Ambiguity 1 |
| **link B** | `eof` | L9, one straight metal y 13480-14690; crosses `hc5`'s poly (y 13880-13908) and `hc4`'s band (y 14010-14038) without a pad | `b_l9_m.png`, `b_l9_c.png` (2x strips, metal and clean shot, every package's trace outlined); follower positions every 200 px; text maps of the band crossing and of the one contact candidate (y 14222: field under whole metal) |
| k15 to the gates | `bd1` | k15 from y 14690, jog west at y 15087 to x 13652, contact (13655,15391), poly to gate P2 (in series with `inh_lat`'s P3 on node `bd1_n1`) and P4 (inverter A) | `tools/follow.py 13738 14700 S` gives the jog and the end as drawn; `d_bd1.png` (2.35x, all traces): the overlay sits on the features. The gate column itself was not re-read (`bd1`'s re-read item R1 stays) |

## Ports

The net is driven outside the package (by `rdp2`'s NOR). `in` marks the port beyond which the
driver lies; the other three lead to the loads.

| Name | Layer | Where | Direction | What |
|---|---|---|---|---|
| `rc_eq_r4` | poly | (13420, 9654-9672) | in | from `mrach`'s poly row (its file ends it at x 13425) |
| `rc_eq_r4` | metal | (13641-13659, 10705) | to loads | track L7, on into `rdp3`'s piece (`rdp3_n7s9`) |
| `rc_eq_r4` | metal | (13729-13747, 13475) | from `rdp3` | track L9, `rdp3`'s end |
| `rc_eq_r4` | metal | (13729-13747, 14695) | to loads | track L9, on into `bd1`'s track k15 (`bd1_a`) |

## Ambiguities

1. **`rdp3`'s contact (13736,12826)**, the top of L9 on the east pad of its poly link (not this
   package's geometry; the join rests on it). Both metal shots show a bright centre in a dark
   ring and the metal ends on the pad (`c_l9top.png`, 3.1x, four shots), which is what a contact
   at a line's end looks like (traps 12, 14). But the clean shot shows no green hole in the pad:
   its centre is orange-red (red minus green 80-100, text map `textmap.py 13540 12805 13765 12848
   3`), where the west pad of the same link (13565,12826) has the usual dull hole
   (`c_l5bot.png`). Readings: (a) a contact whose hole looks different in chip 1's stripped shot
   (residue); (b) no contact, which would leave L9's top and the poly link's east end as two free
   ends on one pad. Working assumption: (a), as `rdp3` drew it. What would settle it: the pad in
   `acid1` (chip 1's other stripped shot), or an independent reader.

## Review

(none yet)

## Not done

- Task 2: `sl_eq_r5` west of x 8340 (`notes/blocks/bust.md`): the row that turns south near
  x 8190 or the pad near (8245,4718), then on to its gates.
- Task 3: `tcw_a`'s source: its thin metal comes from the north to the pad (6400,4005) (`tcw`);
  its row y 5631 crosses `tl4`'s strip and goes on south across y 6350.
- Task 4: the driver of `rcs_x1`: beyond `tl5`'s bus line x 5107 (the row y 5890).
- For `bd1` (queue row `bd1`-`bd3`): the latch's lower half and where `bd1_n1`, `bd1_n2`,
  `bd1_an` go now decide what R4's match does.
