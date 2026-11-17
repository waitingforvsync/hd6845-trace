# Ports

One file per package, `PREFIX.txt`: where each of the package's nets leaves it, one line per
port, so that a tool can find which ports of different packages meet. The tracer of the
package keeps it, beside the Ports table of `notes/blocks/PREFIX.md` (which keeps the prose).
Expected for new work; a block traced before 2026-11-17 gets one when it is next opened.

```
NAME  LAYER  X,Y  DIR  free-text note
```

- NAME: the net's name in the trace. LAYER: `M`, `P` or `D`, the layer the wire is on there.
- X,Y: where it crosses the package's edge or where the drawn wire ends, in metal-shot
  pixels. Either number may be a range `A-B`, the wire's extent across the edge.
- DIR: `in` (driven from outside), `out` (driven inside this package), `?` (not known), `-`
  (a supply rail).
- `#` starts a comment. A wire that leaves in several places has one line per place. Only
  ports with a definite place: do not guess a coordinate to fill a line.

`tools/ports.py` reads them all: ports of different packages that meet (and whether their
names, layers and directions agree), names two packages both list at places that do not
meet, ports with no partner; `--near X,Y`, `--prefix P`. Its docstring has the details.
