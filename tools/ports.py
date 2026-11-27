#!/usr/bin/env python3
"""Ports: where each package's nets leave it, and which ports of different packages meet.

usage: ports.py [--prefix P] [--near X,Y] [--radius R] [--tol N]

Reads every ports.d/PREFIX.txt (the file's name is the package). One line per port:

    NAME  LAYER  X,Y  DIR  free-text note

  NAME   the net's name in the trace (the name a label gives it; `tc1_x1_u` for an open join)
  LAYER  M, P or D: the layer the wire is on where it crosses or ends
  X,Y    where it crosses the package's edge, or where the drawn wire ends, in metal-shot
         pixels. Either number may be a range A-B, the wire's extent across the edge
         (8350,2846-2868 is a poly crossing x 8350 between y 2846 and y 2868); the tool
         measures from the range, and prints its middle
  DIR    in (driven from outside), out (driven inside this package), ? (not known),
         - (does not apply: a supply rail)
  note   anything: where it comes from, what it is believed to be, what was not checked

Blank lines and lines starting with # are ignored; a # after the fields starts a comment.
A wire that crosses the edge in several places has one line per place. Only ports with a
definite place go in the file; a wire seen "going on west" with no coordinate stays in the
notes' prose until someone follows it.

Output, plain text:

  1. meetings: ports of different packages whose places lie within N px (--tol, default 40).
     Marked `same name`, or `NAMES DIFFER` (a join to make and a rename: follow it in the
     photos first, trap 17); `layers differ` where one is on M and the other on P or D (a
     contact must be there for them to join: look), and `BOTH out` / `both in` where the
     directions cannot both be right.
  2. names that two packages both list but at places that do not meet (nearest distance
     given): one of the two has the wrong name, or the stretch between is not traced.
     Supplies are left out.
  3. ports with no partner: the edge of what is traced, or a neighbour that has no ports
     file yet. While few packages have a ports file, most ports are here.

--prefix P   only what involves package P
--near X,Y   instead of the report: every port within R px of the point (--radius,
             default 200), nearest first
A line that does not parse is reported with its file and line number, and the exit status
is 1; the rest is still read.
"""
import argparse
import glob
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTS_DIR = os.path.join(ROOT, 'ports.d')
SUPPLY = ('vss', 'vcc')
RANGE = re.compile(r'^(\d+)(?:-(\d+))?$')


class Port:
    def __init__(self, prefix, name, layer, xs, ys, direction, note, src):
        self.prefix, self.name, self.layer, self.dir, self.note, self.src = prefix, name, layer, direction, note, src
        self.x0, self.x1 = xs
        self.y0, self.y1 = ys

    @property
    def at(self):
        return (self.x0 + self.x1) // 2, (self.y0 + self.y1) // 2

    def where(self):
        return '%d,%d' % self.at

    def dist(self, o):
        """Gap between the two places (0 if the ranges overlap)."""
        dx = max(self.x0 - o.x1, o.x0 - self.x1, 0)
        dy = max(self.y0 - o.y1, o.y0 - self.y1, 0)
        return math.hypot(dx, dy)

    def dist_pt(self, x, y):
        dx = max(self.x0 - x, x - self.x1, 0)
        dy = max(self.y0 - y, y - self.y1, 0)
        return math.hypot(dx, dy)

    def text(self):
        return '%-8s %-18s %s %-11s %-3s' % (self.prefix, self.name, self.layer, self.where(), self.dir)


def span(tok):
    m = RANGE.match(tok)
    if not m:
        raise ValueError('bad coordinate %r' % tok)
    a = int(m.group(1))
    b = int(m.group(2)) if m.group(2) else a
    return (min(a, b), max(a, b))


def parse(path, errors):
    prefix = os.path.basename(path)[:-4]
    out = []
    for i, raw in enumerate(open(path), 1):
        line = raw.split('#', 1)[0].strip()
        if not line:
            continue
        src = '%s:%d' % (os.path.relpath(path, ROOT), i)
        f = line.split(None, 4)
        try:
            if len(f) < 4:
                raise ValueError('needs NAME LAYER X,Y DIR')
            name, layer, xy, d = f[:4]
            if not re.match(r'^[a-z][a-z0-9_]*$', name):
                raise ValueError('bad name %r' % name)
            if layer not in ('M', 'P', 'D'):
                raise ValueError('layer %r is not M, P or D' % layer)
            if xy.count(',') != 1:
                raise ValueError('bad place %r (X,Y; either may be a range A-B)' % xy)
            xs, ys = (span(t) for t in xy.split(','))
            if d not in ('in', 'out', '?', '-'):
                raise ValueError('direction %r is not in, out, ? or -' % d)
            out.append(Port(prefix, name, layer, xs, ys, d, f[4] if len(f) > 4 else '', src))
        except ValueError as e:
            errors.append('%s: %s' % (src, e))
    return out


def load():
    errors, ports = [], []
    for path in sorted(glob.glob(os.path.join(PORTS_DIR, '*.txt'))):
        ports += parse(path, errors)
    return ports, errors


def flags(a, b):
    out = ['same name' if a.name == b.name else 'NAMES DIFFER']
    if a.layer != b.layer:
        out.append('layers differ (%s, %s): needs a contact' % (a.layer, b.layer))
    if a.dir == 'out' and b.dir == 'out':
        out.append('BOTH out')
    elif a.dir == 'in' and b.dir == 'in':
        out.append('both in')
    return '; '.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--prefix')
    ap.add_argument('--near')
    ap.add_argument('--radius', type=float, default=200)
    ap.add_argument('--tol', type=float, default=40)
    a = ap.parse_args()
    ports, errors = load()
    for e in errors:
        print('ERROR  ' + e)
    files = sorted({p.prefix for p in ports})
    print('ports: %d in %d files (%s)' % (len(ports), len(files), ' '.join(files) or 'none'))

    if a.near:
        try:
            x, y = (int(v) for v in a.near.split(','))
        except ValueError:
            sys.exit('--near X,Y')
        hits = sorted(((p.dist_pt(x, y), p) for p in ports
                       if p.dist_pt(x, y) <= a.radius and (not a.prefix or p.prefix == a.prefix)),
                      key=lambda dp: (dp[0], dp[1].prefix, dp[1].at))
        print('within %d px of %d,%d:' % (a.radius, x, y))
        for d, p in hits:
            print('  %4d px  %s  %s' % (d, p.text(), p.note))
        if not hits:
            print('  none')
        sys.exit(1 if errors else 0)

    def wanted(*ps):
        return not a.prefix or any(p.prefix == a.prefix for p in ps)

    pairs = []
    for i, p in enumerate(ports):
        for q in ports[i + 1:]:
            if p.prefix != q.prefix and p.dist(q) <= a.tol:
                pairs.append((p, q))
    partnered = {id(p) for pq in pairs for p in pq}

    print('\n1. ports of different packages that meet (within %d px):' % a.tol)
    shown = [(p, q) for p, q in pairs if wanted(p, q)]
    for p, q in sorted(shown, key=lambda pq: (pq[0].prefix, pq[0].at)):
        print('  %s\n    %s  %d px  %s' % (p.text(), q.text(), p.dist(q), flags(p, q)))
    if not shown:
        print('  none')

    print('\n2. names that two packages both list, at places that do not meet:')
    by = {}
    for p in ports:
        if p.name not in SUPPLY:
            by.setdefault(p.name, {}).setdefault(p.prefix, []).append(p)
    n = 0
    for name in sorted(by):
        pk = sorted(by[name])
        for i, u in enumerate(pk):
            for v in pk[i + 1:]:
                if a.prefix and a.prefix not in (u, v):
                    continue
                d, p, q = min(((p.dist(q), p, q) for p in by[name][u] for q in by[name][v]), key=lambda t: t[0])
                if d > a.tol:
                    n += 1
                    print('  %-18s %s at %s (%s), %s at %s (%s): nearest %d px apart'
                          % (name, u, p.where(), p.layer, v, q.where(), q.layer, d))
    if not n:
        print('  none')

    print('\n3. ports with no partner:')
    lone = [p for p in ports if id(p) not in partnered and wanted(p)]
    for p in sorted(lone, key=lambda p: (p.prefix, p.at)):
        print('  %s  %s' % (p.text(), p.note[:70]))
    if not lone:
        print('  none')
    print('\n%d meetings, %d ports without a partner' % (len(shown), len(lone)))
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
