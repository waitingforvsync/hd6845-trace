// A flat, zoomable view of the die photographs, drawn with three.js.
// All coordinates are die-photo pixels (origin top-left, y down), as in the trace files.
import * as THREE from 'three';

export const LAYER_COLOUR = { M: 0x4aa3ff, P: 0xff5a4d, D: 0x2fd36b, C: 0xffd23f, B: 0xd96bff, T: 0xffffff };
export const LAYER_NAME = { M: 'Metal', P: 'Poly', D: 'Diffusion', C: 'Metal contact', B: 'Buried contact', T: 'Transistor channel' };

const VERT = `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`;
const FRAG = `uniform sampler2D tA; uniform sampler2D tB; uniform float mixv; uniform float opacity; uniform float dim;
varying vec2 vUv;
void main(){ vec3 c = mix(texture2D(tA, vUv).rgb, texture2D(tB, vUv).rgb, mixv); gl_FragColor = vec4(c * dim, opacity); }`;

export function pointInRing(x, y, ring) {
  let inside = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const [xi, yi] = ring[i], [xj, yj] = ring[j];
    if ((yi > y) !== (yj > y) && x < ((xj - xi) * (y - yi)) / (yj - yi) + xi) inside = !inside;
  }
  return inside;
}

const loader = new THREE.TextureLoader();
const texCache = new Map();
// One texture per URL, shared by every viewer; each viewer that asks hears when it has loaded.
export function releaseTexture(url) {
  const e = texCache.get(url);
  if (e) { e.tex.dispose(); texCache.delete(url); }
}
function texLoaded(url) { const e = texCache.get(url); return !!(e && e.loaded); }
function texture(url, onLoad) {
  let e = texCache.get(url);
  if (!e) {
    e = { cbs: [], loaded: false };
    e.tex = loader.load(url, () => { e.loaded = true; e.cbs.splice(0).forEach(f => f()); });
    e.tex.colorSpace = THREE.NoColorSpace;        // the photographs go to the screen as they are
    e.tex.minFilter = THREE.LinearMipmapLinearFilter;
    e.tex.magFilter = THREE.LinearFilter;
    e.tex.anisotropy = 8;
    texCache.set(url, e);
  }
  if (onLoad) { if (e.loaded) setTimeout(onLoad, 0); else e.cbs.push(onLoad); }
  return e.tex;
}

/**
 * tiles: [{x, y, w, h, urls: {shot: url}, fade: [from, to]}]; a tile with `fade` appears over
 * the one below it as the zoom (screen pixels per die pixel) passes from..to, so that one view
 * runs from the whole die down to the photograph's own resolution.
 * Shots a tile does not have fall back through `urls.fallback`.
 */
export class PhotoViewer {
  constructor(el, { tiles, bounds, minHalf = 12, origin = [0, 0], dimBelow = 1 }) {
    this.el = el;
    this.bounds = bounds;                     // x, y, w, h the view may show
    this.minHalf = minHalf;
    this.origin = origin;                     // overlay polygons are given relative to this
    this.shots = ['metal', 'metal'];
    this.mixv = 0;
    this.overlayStyle = () => null;           // meta -> {color, opacity, outline} or null (hidden)
    this.items = [];                          // overlay pick items
    this.notes = [];
    this.onHover = null;
    this.onClick = null;
    this.canvasBox = document.createElement('div');
    this.canvasBox.className = 'pv-canvas';
    el.appendChild(this.canvasBox);
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, preserveDrawingBuffer: true });
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.setClearColor(0x14130f, 1);
    this.canvasBox.appendChild(this.renderer.domElement);
    this.scene = new THREE.Scene();
    this.camera = new THREE.OrthographicCamera(-1, 1, -1, 1, -10, 10);
    this.overlay = new THREE.Group();
    this.tiles = tiles.map((t, i) => this._tile(t, i));
    this.scene.add(this.overlay);
    this.noteLayer = document.createElement('div');
    this.noteLayer.className = 'pv-notes';
    el.appendChild(this.noteLayer);
    this.hintEl = document.createElement('div'); this.hintEl.className = 'pv-hint'; this.hintEl.textContent = 'Click, then scroll to zoom'; el.appendChild(this.hintEl);
    this.zoomBox = document.createElement('div'); this.zoomBox.className = 'pv-zoom';
    for (const [t, f, l] of [['+', 0.6, 'Zoom in'], ['\u2212', 1 / 0.6, 'Zoom out']]) { const b = document.createElement('button'); b.textContent = t; b.title = b.ariaLabel = l; b.onclick = () => this.zoomBy(f); this.zoomBox.appendChild(b); }
    el.appendChild(this.zoomBox);
    this.tip = document.createElement('div');
    this.tip.className = 'pv-tip';
    el.appendChild(this.tip);
    const [bx, by, bw, bh] = bounds;
    this.cx = bx + bw / 2; this.cy = by + bh / 2; this.half = bw / 2;
    this.anim = null;
    this._wire();
    this._resize();
    new ResizeObserver(() => this._resize()).observe(el);
    this._loop = this._loop.bind(this);
    this.dirty = true;
    requestAnimationFrame(this._loop);
  }

  _tile(t, i) {
    const mat = new THREE.ShaderMaterial({
      uniforms: { tA: { value: null }, tB: { value: null }, mixv: { value: 0 }, opacity: { value: 1 }, dim: { value: 1 } },
      vertexShader: VERT, fragmentShader: FRAG, transparent: true, depthTest: false, side: THREE.DoubleSide,
    });
    const g = new THREE.PlaneGeometry(t.w, t.h);
    g.translate(t.x + t.w / 2, t.y + t.h / 2, 0);   // uv's v runs up, die y runs down: flip it
    const uv = g.attributes.uv;
    for (let k = 0; k < uv.count; k++) uv.setY(k, 1 - uv.getY(k));
    const mesh = new THREE.Mesh(g, mat);
    mesh.renderOrder = i;
    this.scene.add(mesh);
    if (t.lazy) mesh.visible = false;
    return { def: t, mat, mesh, curA: null, curB: null, used: 0 };
  }

  urlFor(tile, shot) {
    const u = tile.def.urls;
    return u[shot] || u[{ acid: 'acid1b', metal1: 'metal', acid1b: 'acid1b', metal: 'metal' }[shot]] || u.metal;
  }

  setShots(a, b = a, mix = 0) {
    this.shots = [a, b]; this.mixv = mix;
    for (const t of this.tiles) {
      if (t.def.lazy) { t.mat.uniforms.mixv.value = mix; continue; }     // loaded in _draw, when in view
      t.mat.uniforms.tA.value = texture(this.urlFor(t, a), () => (this.dirty = true));
      t.mat.uniforms.tB.value = texture(this.urlFor(t, b), () => (this.dirty = true));
      t.mat.uniforms.mixv.value = mix;
    }
    this.dirty = true;
  }
  setMix(m) { this.mixv = m; for (const t of this.tiles) t.mat.uniforms.mixv.value = m; this.dirty = true; }
  setDim(d) { for (const t of this.tiles) t.mat.uniforms.dim.value = d; this.dirty = true; }

  // ---- overlay -------------------------------------------------------------------------
  /** polys: [{pts: [[x,y]..], meta: {...}}] relative to this.origin. Replaces the overlay. */
  setOverlay(polys) {
    for (const o of [...this.overlay.children]) { this.overlay.remove(o); o.traverse(n => { n.geometry && n.geometry.dispose(); }); }
    this.items = [];
    const [ox, oy] = this.origin;
    polys.forEach((p, i) => {
      const shape = new THREE.Shape(p.pts.map(([x, y]) => new THREE.Vector2(x + ox, y + oy)));
      const fill = new THREE.Mesh(new THREE.ShapeGeometry(shape), new THREE.MeshBasicMaterial({ transparent: true, depthTest: false, side: THREE.DoubleSide }));
      const line = new THREE.LineLoop(new THREE.BufferGeometry().setFromPoints(p.pts.map(([x, y]) => new THREE.Vector3(x + ox, y + oy, 0))),
        new THREE.LineBasicMaterial({ transparent: true, depthTest: false }));
      fill.renderOrder = 100 + (p.meta.order || 0) * 2; line.renderOrder = fill.renderOrder + 1;
      this.overlay.add(fill, line);
      this.items.push({ ...p, fill, line, abs: p.pts.map(([x, y]) => [x + ox, y + oy]), i });
    });
    this.restyle();
  }

  restyle() {
    for (const it of this.items) {
      const s = this.overlayStyle(it.meta, it);
      it.fill.visible = it.line.visible = !!s;
      if (!s) continue;
      it.fill.material.color.set(s.color); it.fill.material.opacity = s.opacity;
      it.line.material.color.set(s.outlineColor ?? s.color); it.line.material.opacity = s.outline ?? 1;
    }
    this.dirty = true;
  }

  /** topmost visible overlay item under die point (x, y) */
  pick(x, y) {
    let best = null;
    for (const it of this.items) {
      if (!it.fill.visible) continue;
      if (pointInRing(x, y, it.abs)) {
        const o = it.meta.order || 0;
        if (!best || o >= (best.meta.order || 0)) best = it;
      }
    }
    return best;
  }

  // ---- notes (HTML labels pinned to die points) ------------------------------------------
  setNotes(list) {
    this.noteLayer.innerHTML = '';
    this.notes = list.map(n => {
      const d = document.createElement('div');
      d.className = 'pv-note' + (n.cls ? ' ' + n.cls : '');
      d.innerHTML = n.html;
      this.noteLayer.appendChild(d);
      return { ...n, el: d };
    });
    this.dirty = true;
  }

  // ---- camera --------------------------------------------------------------------------
  get pxPerDie() { return this.w / (2 * this.half); }
  _resize() {
    const r = this.el.getBoundingClientRect();
    this.w = Math.max(50, r.width); this.h = Math.max(50, r.height);
    this.renderer.setSize(this.w, this.h, true);
    this.dirty = true;
  }
  _clamp() {
    const [bx, by, bw, bh] = this.bounds;
    const aspect = this.h / this.w;
    this.half = Math.min(Math.max(this.half, this.minHalf), Math.max(bw / 2, bh / 2 / aspect));
    const hh = this.half * aspect;
    this.cx = Math.min(Math.max(this.cx, bx + Math.min(this.half, bw / 2)), bx + bw - Math.min(this.half, bw / 2));
    this.cy = Math.min(Math.max(this.cy, by + Math.min(hh, bh / 2)), by + bh - Math.min(hh, bh / 2));
  }
  /** Show the die rectangle x,y,w,h (aspect preserved), animating over ms. */
  flyTo(x, y, w, h, ms = 700) {
    const aspect = this.h / this.w;
    const half = Math.max(w / 2, h / 2 / aspect);
    const to = { cx: x + w / 2, cy: y + h / 2, half };
    if (!ms || matchMedia('(prefers-reduced-motion: reduce)').matches) { Object.assign(this, to); this._clamp(); this.dirty = true; return; }
    this.anim = { from: { cx: this.cx, cy: this.cy, half: this.half }, to, t0: performance.now(), ms };
  }
  reset() { const [x, y, w, h] = this.bounds; this.flyTo(x, y, w, h, 0); }

  _wire() {
    const cv = this.renderer.domElement;
    cv.style.touchAction = 'pan-y';          // a swipe along the page must still scroll it
    cv.tabIndex = 0; cv.setAttribute('role', 'img'); cv.setAttribute('aria-label', this.label || 'Zoomable photograph of the chip; drag to pan, click then scroll to zoom');
    let drag = null;
    const toDie = e => {
      const r = cv.getBoundingClientRect();
      const aspect = this.h / this.w;
      return [this.cx + ((e.clientX - r.left) / r.width - 0.5) * 2 * this.half,
              this.cy + ((e.clientY - r.top) / r.height - 0.5) * 2 * this.half * aspect];
    };
    cv.addEventListener('pointerdown', e => { this.active = true; this._hint(); cv.setPointerCapture(e.pointerId); drag = { x: e.clientX, y: e.clientY, moved: 0 }; this.anim = null; });
    cv.addEventListener('pointermove', e => {
      const [x, y] = toDie(e);
      if (drag) {
        const dx = e.clientX - drag.x, dy = e.clientY - drag.y;
        drag.x = e.clientX; drag.y = e.clientY; drag.moved += Math.abs(dx) + Math.abs(dy);
        const k = (2 * this.half) / this.w;
        this.cx -= dx * k; this.cy -= dy * k; this._clamp(); this.dirty = true;
      }
      const it = this.items.length ? this.pick(x, y) : null;
      this.hover = it;
      if (this.onHover) this.onHover(it, x, y, e, this.tip);
      cv.style.cursor = drag ? 'grabbing' : (it && this.onClick ? 'pointer' : 'grab');
    });
    cv.addEventListener('pointerleave', () => { this.tip.style.display = 'none'; this.active = false; this._hint(); if (this.onHover) this.onHover(null, 0, 0, null, this.tip); });
    cv.addEventListener('pointerup', e => {
      const moved = drag ? drag.moved : 0; drag = null;
      if (moved < 5 && this.onClick) { const [x, y] = toDie(e); this.onClick(this.pick(x, y), x, y, e); }
    });
    cv.addEventListener('wheel', e => {
      if (!(this.active || e.ctrlKey || e.metaKey)) return;     // hovering alone lets the page scroll
      e.preventDefault();
      const [x, y] = toDie(e);
      const f = Math.exp(e.deltaY * 0.0015);
      const before = this.half;
      this.half = Math.min(Math.max(before * f, this.minHalf), this._maxHalf());
      const k = this.half / before;
      this.cx = x - (x - this.cx) * k; this.cy = y - (y - this.cy) * k;
      this._clamp(); this.anim = null; this.dirty = true;
    }, { passive: false });
    cv.addEventListener('dblclick', () => this.reset());
  }
  _maxHalf() { const [, , bw, bh] = this.bounds; return Math.max(bw / 2, bh / 2 / (this.h / this.w)); }
  _hint() { if (this.hintEl) this.hintEl.style.opacity = this.active ? 0 : 1; }
  zoomBy(f) { this.half = Math.min(Math.max(this.half * f, this.minHalf), this._maxHalf()); this._clamp(); this.dirty = true; }

  _loop(now) {
    if (this.anim) {
      const a = this.anim, t = Math.min(1, (now - a.t0) / a.ms), e = t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      // interpolate the half-width geometrically so the zoom feels even
      this.half = Math.exp(Math.log(a.from.half) * (1 - e) + Math.log(a.to.half) * e);
      this.cx = a.from.cx + (a.to.cx - a.from.cx) * e; this.cy = a.from.cy + (a.to.cy - a.from.cy) * e;
      this._clamp();
      if (t >= 1) this.anim = null;
      this.dirty = true;
    }
    if (this.dirty) { this.dirty = false; this._draw(); }
    requestAnimationFrame(this._loop);
  }

  _draw() {
    const aspect = this.h / this.w, hh = this.half * aspect;
    Object.assign(this.camera, { left: this.cx - this.half, right: this.cx + this.half, top: this.cy - hh, bottom: this.cy + hh });
    this.camera.updateProjectionMatrix();
    const z = this.pxPerDie;
    for (const t of this.tiles) {
      const f = t.def.fade;
      t.mat.uniforms.opacity.value = f ? Math.min(1, Math.max(0, (z - f[0]) / (f[1] - f[0]))) : 1;
      t.mesh.visible = t.mat.uniforms.opacity.value > 0.001;
      if (t.def.lazy) {
        const d = t.def, inView = d.x < this.cx + this.half && d.x + d.w > this.cx - this.half && d.y < this.cy + hh && d.y + d.h > this.cy - hh;
        if (!(t.mesh.visible && inView)) { t.mesh.visible = false; continue; }
        t.used = performance.now();
        const ua = this.urlFor(t, this.shots[0]), ub = this.urlFor(t, this.shots[1]);
        if (t.curA !== ua) { t.curA = ua; t.mat.uniforms.tA.value = texture(ua, () => (this.dirty = true)); }
        if (t.curB !== ub) { t.curB = ub; t.mat.uniforms.tB.value = texture(ub, () => (this.dirty = true)); }
        t.mesh.visible = texLoaded(ua) && texLoaded(ub);
      }
    }
    // keep memory bounded: drop the textures of the least recently seen lazy tiles
    const held = this.tiles.filter(t => t.def.lazy && t.curA).sort((p, q) => q.used - p.used);
    for (const t of held.slice(10)) {
      for (const u of new Set([t.curA, t.curB])) releaseTexture(u);
      t.curA = t.curB = null; t.mat.uniforms.tA.value = t.mat.uniforms.tB.value = null; t.mesh.visible = false;
    }
    this.renderer.render(this.scene, this.camera);
    // notes
    for (const n of this.notes) {
      const sx = ((n.x - (this.cx - this.half)) / (2 * this.half)) * this.w;
      const sy = ((n.y - (this.cy - hh)) / (2 * hh)) * this.h;
      const vis = sx > -20 && sx < this.w + 20 && sy > -20 && sy < this.h + 20;
      n.el.style.display = vis ? '' : 'none';
      const nw = n.el.offsetWidth + 16;
      n.el.style.transform = `translate(${Math.min(sx, Math.max(0, this.w - nw))}px, ${sy}px)`;
    }
    if (this.onView) this.onView(this);
  }
}
