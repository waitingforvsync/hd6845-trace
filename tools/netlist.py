"""Extract a transistor netlist from the trace geometry, and check it.

Rules
  - Poly over diffusion is a transistor channel, unless a buried contact covers it,
    in which case poly and diffusion are joined there.
  - A contact joins the metal over it to the poly under it, or failing that to the
    diffusion under it. A contact drawn over both is reported; add `butt=1` to the
    contact if it really does join all three.
  - Nets are the connected pieces of metal, poly and conducting diffusion joined by
    contacts and buried contacts.
"""
from collections import defaultdict
from dataclasses import dataclass, field

from shapely.ops import unary_union
from shapely.strtree import STRtree
from shapely.geometry import Point

import tracelib

GLOBAL_NETS = ('vss', 'vcc')   # joined by name; untraced gaps are reported, not fatal
SLIVER_AREA = 60.0      # channels smaller than this are drawing artefacts
MIN_OVERLAP = 0.25      # fraction of a contact that must lie on a layer to connect


def polys(g):
    if g.is_empty:
        return []
    if g.geom_type == 'Polygon':
        return [g]
    return [p for p in getattr(g, 'geoms', []) if p.geom_type == 'Polygon' and p.area > 0]


class UF:
    def __init__(self):
        self.p = {}

    def find(self, a):
        self.p.setdefault(a, a)
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


@dataclass
class Transistor:
    id: int
    gate: int
    c1: int
    c2: int
    x: float
    y: float
    w: float
    l: float
    kind: str = ''          # '', 'load', filled in by logic recovery
    geom: object = None


@dataclass
class Node:
    id: int
    names: list = field(default_factory=list)
    x: float = 0
    y: float = 0
    layers: str = ''
    gates: list = field(default_factory=list)      # transistor ids gated by this node
    chans: list = field(default_factory=list)      # transistor ids with a terminal here

    @property
    def name(self):
        return self.names[0] if self.names else f'n{self.id}'


class Netlist:
    def __init__(self, trace=None):
        self.trace = trace or tracelib.load()
        self.errors = []
        self.warnings = []
        self.nodes = {}
        self.transistors = []
        self._build()

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    # ------------------------------------------------------------------
    def _build(self):
        tr = self.trace
        L = {k: [it for it in tr.items if it.layer == k] for k in tracelib.LAYERS}
        metal_u = unary_union([it.geom for it in L['M']]) if L['M'] else None
        poly_u = unary_union([it.geom for it in L['P']]) if L['P'] else None
        diff_u = unary_union([it.geom for it in L['D']]) if L['D'] else None
        bur_u = unary_union([it.geom for it in L['B']]) if L['B'] else None

        from shapely.geometry import GeometryCollection
        empty = GeometryCollection()
        metal_u = metal_u or empty
        poly_u = poly_u or empty
        diff_u = diff_u or empty
        bur_u = bur_u or empty

        gate_poly = poly_u.difference(bur_u)
        chan_all = polys(diff_u.intersection(gate_poly))
        channels = []
        for ch in chan_all:
            if ch.area < SLIVER_AREA:
                c = ch.centroid
                self.warn(f'sliver channel ({ch.area:.0f} px2) at {c.x:.0f},{c.y:.0f}: '
                          'poly/diffusion/buried-contact edges nearly coincide')
            else:
                channels.append(ch)
        diffc = diff_u.difference(gate_poly)

        self.metal = polys(metal_u)
        self.poly = polys(poly_u)
        self.diff = polys(diffc)
        self.channels = channels
        trees = {'M': (self.metal, STRtree(self.metal) if self.metal else None),
                 'P': (self.poly, STRtree(self.poly) if self.poly else None),
                 'D': (self.diff, STRtree(self.diff) if self.diff else None)}
        self._trees = trees

        def hits(layer, g, min_area=1.0):
            geoms, tree = trees[layer]
            out = []
            if tree is None:
                return out
            for i in tree.query(g):
                a = geoms[i].intersection(g).area
                if a >= min_area:
                    out.append((i, a))
            return out

        uf = UF()
        for k in ('M', 'P', 'D'):
            for i in range(len(trees[k][0])):
                uf.find((k, i))

        # contacts
        for it in L['C']:
            c = it.geom
            cx, cy = c.centroid.x, c.centroid.y
            where = f'contact at {cx:.0f},{cy:.0f} ({it.src})'
            m = hits('M', c)
            if not m:
                self.err(f'{where}: no metal over it')
                continue
            if len(m) > 1:
                self.err(f'{where}: bridges {len(m)} separate metal shapes')
            p = [(i, a) for i, a in hits('P', c) if a / c.area >= MIN_OVERLAP]
            d = [(i, a) for i, a in hits('D', c) if a / c.area >= MIN_OVERLAP]
            butt = it.attrs.get('butt') == '1'
            if p and d and not butt:
                self.warn(f'{where}: lies over both poly and diffusion; joined to '
                          + ('poly' if sum(a for _, a in p) >= sum(a for _, a in d) else 'diffusion')
                          + ' only (mark butt=1 if it joins both)')
                if sum(a for _, a in p) >= sum(a for _, a in d):
                    d = []
                else:
                    p = []
            if not p and not d:
                self.err(f'{where}: nothing under it')
                continue
            for i, _ in m:
                uf.union(('M', m[0][0]), ('M', i))
            for i, _ in p:
                uf.union(('M', m[0][0]), ('P', i))
            for i, _ in d:
                uf.union(('M', m[0][0]), ('D', i))

        # buried contacts
        for b in polys(bur_u):
            cx, cy = b.centroid.x, b.centroid.y
            p = hits('P', b, 4.0)
            d = hits('D', b, 4.0)
            if not p or not d:
                self.err(f'buried contact at {cx:.0f},{cy:.0f}: needs poly and diffusion '
                         f'(poly {len(p)}, diffusion {len(d)})')
                continue
            for i, _ in p:
                uf.union(('P', p[0][0]), ('P', i))
            for i, _ in d:
                uf.union(('P', p[0][0]), ('D', i))

        # supply nets are joined by name: find every labelled piece first
        self.supply_pieces = {}
        for gname in GLOBAL_NETS:
            first = None
            pieces = set()
            for lb in tr.labels:
                if lb.name != gname:
                    continue
                geoms, tree = trees[lb.layer]
                pt = Point(lb.x, lb.y)
                found = [i for i in (tree.query(pt) if tree is not None else [])
                         if geoms[i].contains(pt)]
                if not found:
                    continue
                key = (lb.layer, found[0])
                pieces.add(uf.find(key))
                if first is None:
                    first = key
                else:
                    uf.union(first, key)
            self.supply_pieces[gname] = len(pieces)

        # node ids
        roots = {}
        layers_of = defaultdict(set)
        for k in ('M', 'P', 'D'):
            for i in range(len(trees[k][0])):
                r = uf.find((k, i))
                roots.setdefault(r, len(roots))
                layers_of[roots[r]].add(k)
        self._node_of = lambda k, i: roots[uf.find((k, i))]
        for r, nid in roots.items():
            g = trees[r[0]][0][r[1]].representative_point()
            self.nodes[nid] = Node(nid, [], g.x, g.y, ''.join(sorted(layers_of[nid])))

        # labels
        seen = {}
        for lb in tr.labels:
            geoms, tree = trees[lb.layer]
            pt = Point(lb.x, lb.y)
            found = [i for i in (tree.query(pt) if tree is not None else []) if geoms[i].contains(pt)]
            if not found:
                self.err(f'label {lb.name} at {lb.x:.0f},{lb.y:.0f} ({lb.src}): '
                         f'no {lb.layer} there')
                continue
            nid = self._node_of(lb.layer, found[0])
            n = self.nodes[nid]
            if lb.name not in n.names:
                n.names.append(lb.name)
            if lb.name in seen and seen[lb.name] != nid and lb.name not in GLOBAL_NETS:
                self.warn(f'name {lb.name} is on two unconnected nets '
                          f'(second at {lb.x:.0f},{lb.y:.0f})')
            seen.setdefault(lb.name, nid)
        for n in self.nodes.values():
            canon = [nm for nm in n.names if nm not in tracelib.ALIASES]
            # an alias may reach the canonical name through another alias (two families of
            # aliases meet when a wire joins two nets that each had other names: 2026-11-19)
            if len(canon) == 1 and all(tracelib.canonical(nm) == canon[0]
                                       for nm in n.names if nm != canon[0]):
                n.names = canon + [nm for nm in n.names if nm != canon[0]]
                continue
            if len(n.names) > 1:
                self.err(f'net at {n.x:.0f},{n.y:.0f} carries several names: '
                         + ', '.join(n.names) + ' (short, or an alias)')

        # transistors
        for ch in channels:
            c = ch.representative_point()
            where = f'channel at {c.x:.0f},{c.y:.0f}'
            g = hits('P', ch.buffer(0.5), 1.0)
            if not g:
                self.err(f'{where}: no gate poly found')
                continue
            gate = self._node_of('P', max(g, key=lambda t: t[1])[0])
            near = ch.buffer(1.5)
            terms = []
            for i, a in hits('D', near, 2.0):
                terms.append((i, a / 1.5))
            if len(terms) != 2:
                self.err(f'{where}: {len(terms)} diffusion terminals (expected 2); '
                         'gate may not fully cross the diffusion')
                if len(terms) < 2:
                    continue
            terms.sort(key=lambda t: -t[1])
            (i1, w1), (i2, w2) = terms[0], terms[1]
            w = (w1 + w2) / 2
            t = Transistor(len(self.transistors), gate, self._node_of('D', i1),
                           self._node_of('D', i2), c.x, c.y, w, ch.area / w if w else 0,
                           geom=ch)
            for an in L['A']:
                if an.geom.contains(Point(c.x, c.y)) and 'kind' in an.attrs:
                    t.kind = an.attrs['kind']
            self.transistors.append(t)
            self.nodes[gate].gates.append(t.id)
            self.nodes[t.c1].chans.append(t.id)
            self.nodes[t.c2].chans.append(t.id)
            if t.c1 == t.c2:
                self.warn(f'{where}: both terminals are the same net')

        self.by_name = {}
        for n in self.nodes.values():
            for nm in n.names:
                self.by_name.setdefault(nm, n.id)

    # ------------------------------------------------------------------
    def nm(self, nid):
        return self.nodes[nid].name

    def recover_logic(self, vcc='vcc', vss='vss'):
        """Classify transistors and describe each driven net as a logic expression.

        Returns (gates, passes): gates is a list of (output node id, expression string,
        [transistor ids]); passes is a list of transistors not part of any static gate.
        """
        VCC = self.by_name.get(vcc)
        VSS = self.by_name.get(vss)
        gates, used = [], set()
        if VCC is None or VSS is None:
            return gates, list(self.transistors)
        loads = {}
        for t in self.transistors:
            if t.kind in ('clamp', 'field', 'hold'):
                used.add(t.id)          # off in normal operation: not part of any gate
                continue
            for a, b in ((t.c1, t.c2), (t.c2, t.c1)):
                if a == VCC and b != VSS and t.gate == b:
                    t.kind = 'load'
                    loads[b] = t
                    used.add(t.id)
        strong = set(loads) | {VCC, VSS}

        def paths(node, target, seen_nodes, seen_t):
            """Enumerate channel paths from node to target through internal nodes."""
            out = []
            for tid in self.nodes[node].chans:
                t = self.transistors[tid]
                if t.kind in ('load', 'clamp', 'field', 'hold') or tid in seen_t:
                    continue
                other = t.c2 if t.c1 == node else t.c1
                if other == target:
                    out.append([tid])
                elif other not in strong and other not in seen_nodes:
                    for p in paths(other, target, seen_nodes | {other}, seen_t | {tid}):
                        out.append([tid] + p)
            return out

        for out_node, load in sorted(loads.items()):
            ps = paths(out_node, VSS, {out_node}, set())
            tids = sorted({t for p in ps for t in p})
            used.update(tids)
            terms = []
            for p in ps:
                names = sorted(self.nm(self.transistors[t].gate) for t in p)
                terms.append(' & '.join(names) if len(names) > 1 else names[0])
            terms = sorted(set(terms))
            if not terms:
                expr = '1  (load only, no pull-down found)'
            elif len(terms) == 1 and '&' not in terms[0]:
                expr = f'NOT {terms[0]}'
            elif all('&' not in t for t in terms):
                expr = 'NOR(' + ', '.join(terms) + ')'
            elif len(terms) == 1:
                expr = 'NAND(' + terms[0].replace(' & ', ', ') + ')'
            else:
                expr = 'NOT(' + ' | '.join(f'({t})' if '&' in t else t for t in terms) + ')'
            gates.append((out_node, expr, [load.id] + tids))
        passes = [t for t in self.transistors if t.id not in used]
        return gates, passes

    def report(self):
        lines = []
        lines.append(f'{len(self.nodes)} nets, {len(self.transistors)} transistors, '
                     f'{len(self.errors)} errors, {len(self.warnings)} warnings')
        for g, n in self.supply_pieces.items():
            if n > 1:
                lines.append(f'note   {g} is traced as {n} separate pieces, joined by name')
        for e in self.errors:
            lines.append('ERROR  ' + e)
        for w in self.warnings:
            lines.append('warn   ' + w)
        gates, passes = self.recover_logic()
        lines.append('')
        lines.append('transistors')
        for t in self.transistors:
            lines.append(f'  t{t.id:<4d} at {t.x:6.0f},{t.y:6.0f}  W/L {t.w:4.0f}/{t.l:<4.0f} '
                         f'{t.kind or "-":5s} gate {self.nm(t.gate):12s} '
                         f'{self.nm(t.c1)} <-> {self.nm(t.c2)}')
        lines.append('')
        lines.append('gates')
        for out, expr, tids in gates:
            lines.append(f'  {self.nm(out):12s} = {expr}')
        if passes:
            lines.append('')
            lines.append('not part of a static gate')
            for t in passes:
                lines.append(f'  t{t.id} at {t.x:.0f},{t.y:.0f} gate {self.nm(t.gate)}: '
                             f'{self.nm(t.c1)} <-> {self.nm(t.c2)}')
        # open ends: every net should be driven and used inside what is traced, or be named
        gate_outs = {o for o, _, _ in gates}
        opens = []
        for n in self.nodes.values():
            if n.names:
                continue
            if n.gates and not n.chans:
                opens.append(f'  {n.name} at {n.x:.0f},{n.y:.0f}: gates {len(n.gates)} transistor(s) but nothing drives it')
            elif n.id in gate_outs and not n.gates:
                opens.append(f'  {n.name} at {n.x:.0f},{n.y:.0f}: a gate output that goes nowhere')
            elif not n.gates and not n.chans and 'M' in n.layers and len(n.layers) == 1:
                pass        # a bare piece of metal: wiring in progress
        if opens:
            lines.append('')
            lines.append('unnamed open nets (find the missing connection, or name the net as a port)')
            lines += opens
        return '\n'.join(lines)

    def to_json(self):
        return {
            'nodes': [{'id': n.id, 'name': n.name, 'named': bool(n.names),
                       'x': round(n.x), 'y': round(n.y), 'layers': n.layers}
                      for n in self.nodes.values()],
            'transistors': [{'id': t.id, 'gate': t.gate, 'c1': t.c1, 'c2': t.c2,
                             'x': round(t.x), 'y': round(t.y),
                             'w': round(t.w, 1), 'l': round(t.l, 1), 'kind': t.kind}
                            for t in self.transistors],
        }


if __name__ == '__main__':
    nl = Netlist()
    print(nl.report())
