// The traced worked example as a 3D layer stack, built from the extracted polygons.
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { LAYER_COLOUR } from './photo.js';

function renderer_touch(cv) { cv.style.touchAction = 'pan-y'; cv.tabIndex = 0; cv.setAttribute('role', 'img'); cv.setAttribute('aria-label', '3D view of the traced layers; drag to rotate, scroll or pinch to zoom'); }
const T = { D: 6, P: 8, M: 9, B: 10 };          // thickness in die pixels, for looks only

export class StackViewer {
  constructor(el, ex, { photo } = {}) {
    this.el = el; this.ex = ex;
    this.explode = 0.35;
    this.vis = { D: true, P: true, M: true, C: true, B: true, ground: true };
    this.sel = null;                              // {nets:Set, tid}
    this.paintFn = null;
    this.onPick = null;
    this.renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.setClearColor(0x14130f, 1);
    this.box = document.createElement('div'); this.box.className = 'pv-canvas';
    this.box.appendChild(this.renderer.domElement); el.appendChild(this.box);
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(32, 1, 20, 6000);
    const [W, H] = ex.size;
    this.centre = new THREE.Vector3(W / 2, -H / 2, 30);
    this.camera.up.set(0, 0, 1);
    this.camera.position.set(W / 2 - 330, -H / 2 - 700, 520);
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.target.copy(this.centre);
    renderer_touch(this.renderer.domElement);
    this.controls.enableDamping = true; this.controls.dampingFactor = 0.12;
    this.controls.addEventListener('change', () => (this.dirty = true));
    this.scene.add(new THREE.HemisphereLight(0xffffff, 0x303030, 1.35));
    const sun = new THREE.DirectionalLight(0xffffff, 1.7); sun.position.set(-300, -200, 900); this.scene.add(sun);
    this.tip = document.createElement('div'); this.tip.className = 'pv-tip'; el.appendChild(this.tip);
    this._build(photo);
    this.setExplode(this.explode);
    this._wire();
    this._resize();
    new ResizeObserver(() => this._resize()).observe(el);
    this.dirty = true;
    this._loop = this._loop.bind(this);
    requestAnimationFrame(this._loop);
  }

  _mesh(pts, depth, layer, meta) {
    const shape = new THREE.Shape(pts.map(([x, y]) => new THREE.Vector2(x, -y)));
    const g = new THREE.ExtrudeGeometry(shape, { depth: 1, bevelEnabled: false });
    const m = new THREE.MeshStandardMaterial({ color: LAYER_COLOUR[layer], roughness: 0.55, metalness: layer === 'M' ? 0.5 : 0.05, transparent: true });
    const mesh = new THREE.Mesh(g, m);
    const edges = new THREE.LineSegments(new THREE.EdgesGeometry(g, 30), new THREE.LineBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.45 }));
    mesh.add(edges);
    mesh.userData = { layer, depth, ...meta, base: new THREE.Color(LAYER_COLOUR[layer]) };
    this.scene.add(mesh);
    return mesh;
  }

  _build(photo) {
    const { ex } = this;
    const [W, H] = ex.size;
    // the substrate, carrying the photograph it was traced from
    const gm = new THREE.MeshBasicMaterial({ color: 0x55524a });
    if (photo) {
      const t = new THREE.TextureLoader().load(photo, () => (this.dirty = true));
      t.colorSpace = THREE.NoColorSpace; t.anisotropy = 8;
      gm.map = t; gm.color.set(0xffffff);
    }
    const g = new THREE.PlaneGeometry(W, H); g.translate(W / 2, -H / 2, 0);
    this.ground = new THREE.Mesh(g, gm);
    this.ground.userData = { layer: 'ground' };
    this.scene.add(this.ground);
    this.layers = { D: [], P: [], M: [], C: [], B: [], T: [] };
    for (const L of ['D', 'P', 'M']) {
      for (const p of ex.layers[L]) this.layers[L].push(this._mesh(p.pts, T[L], L, { net: p.net }));
    }
    for (const c of ex.contacts) this.layers.C.push(this._mesh(c.pts, 1, 'C', { to: c.to, net: -1 }));
    for (const b of ex.buried) this.layers.B.push(this._mesh(b, T.B, 'B', { net: -1 }));
    for (const ch of ex.channels) this.layers.T.push(this._mesh(ch.pts, 3, 'T', { tid: ch.id, net: -1, gate: ch.gate }));
    for (const m of this.layers.T) { m.material.color.set(0xffffff); m.userData.base.set(0xffffff); }
    this.all = Object.values(this.layers).flat();
  }

  /** e in 0..1: how far the layers are pulled apart */
  setExplode(e) {
    this.explode = e;
    this._refit(e);
    const G = e * 90;
    const zD = 3, zP = zD + T.D + 3 + G, zM = zP + T.P + 12 + G * 1.6;
    this.z = { D: zD, P: zP, M: zM };
    for (const L of ['D', 'P', 'M']) for (const m of this.layers[L]) { m.position.z = this.z[L]; m.scale.z = T[L]; }
    for (const m of this.layers.T) { m.position.z = zP + T.P - 1; m.scale.z = 3; }
    for (const m of this.layers.B) {     // poly to diffusion, straight down
      const lo = zD + T.D, hi = zP + 1;
      m.position.z = lo; m.scale.z = Math.max(2, hi - lo);
    }
    for (const m of this.layers.C) {     // metal down to what it lands on
      const hi = zM + 1, lo = m.userData.to === 'P' ? zP + T.P : zD + T.D;
      m.position.z = lo; m.scale.z = Math.max(2, hi - lo);
    }
    this.dirty = true;
  }

  _refit(e) {            // pull the camera back as the layers move apart so nothing leaves the frame
    const dir = this.camera.position.clone().sub(this.controls.target);
    const base = this.baseDist || (this.baseDist = dir.length());
    dir.setLength(base * (1 + e * 0.55) * Math.max(1, 1 / this.camera.aspect));
    this.camera.position.copy(this.controls.target).add(dir);
    this.dirty = true;
  }

  setVisible(map) { Object.assign(this.vis, map); this.dirty = true; this._style(); }
  setPhoto(url) {
    const t = new THREE.TextureLoader().load(url, () => (this.dirty = true));
    t.colorSpace = THREE.NoColorSpace; this.ground.material.map = t; this.ground.material.needsUpdate = true; this.dirty = true;
  }
  /** nets: Set of net ids to light up; tid: a transistor id or null. null clears. */
  select(sel) { this.sel = sel; this._style(); }
  /** fn(userData) -> THREE.Color or null; colours shapes by simulated level. */
  paint(fn) { this.paintFn = fn; this._style(); }

  _style() {
    const sel = this.sel, anySel = !!sel;
    for (const m of this.all) {
      const u = m.userData, L = u.layer;
      m.visible = L === 'T' ? this.vis.P : !!this.vis[L];
      let col = u.base.clone(), op = 0.92, em = 0;
      if (this.paintFn) { const c = this.paintFn(u); if (c) col = c; }
      if (anySel) {
        const hit = (u.net >= 0 && sel.nets && sel.nets.has(u.net)) || (sel.tid != null && u.tid === sel.tid);
        const rel = (L === 'C' || L === 'B') && sel.nets;   // cuts stay lit if selection is set
        op = hit ? 1 : (rel ? 0.55 : 0.28); em = hit ? 0.45 : 0;
      }
      m.material.color.copy(col);
      m.material.emissive.copy(col).multiplyScalar(em);
      m.material.opacity = op;
      m.material.depthWrite = op > 0.9;
    }
    this.ground.visible = !!this.vis.ground;
    this.dirty = true;
  }

  _wire() {
    const cv = this.renderer.domElement;
    const ray = new THREE.Raycaster(), p = new THREE.Vector2();
    let down = null;
    const at = e => {
      const r = cv.getBoundingClientRect();
      p.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
      ray.setFromCamera(p, this.camera);
      const hits = ray.intersectObjects(this.all.filter(m => m.visible), false);
      return hits.length ? hits[0].object : null;
    };
    this.controls.enableZoom = false;       // hovering alone lets the page scroll; pressing in the view enables zoom
    cv.addEventListener('pointerleave', () => (this.controls.enableZoom = false));
    cv.addEventListener('pointerdown', e => { this.controls.enableZoom = true; down = { x: e.clientX, y: e.clientY }; });
    cv.addEventListener('pointerup', e => {
      if (down && Math.hypot(e.clientX - down.x, e.clientY - down.y) < 5 && this.onPick) this.onPick(at(e)?.userData || null);
      down = null;
    });
    cv.addEventListener('pointermove', e => {
      const o = at(e);
      if (this.onHover) this.onHover(o ? o.userData : null, e, this.tip);
      cv.style.cursor = o ? 'pointer' : 'grab';
    });
    cv.addEventListener('pointerleave', () => { this.tip.style.display = 'none'; });
  }

  _resize() {
    const r = this.el.getBoundingClientRect();
    this.w = Math.max(50, r.width); this.h = Math.max(50, r.height);
    this.renderer.setSize(this.w, this.h, true);
    this.camera.aspect = this.w / this.h; this.camera.updateProjectionMatrix();
    this.dirty = true;
  }
  /** Look at a die rectangle (relative to this view's origin) from the south-west. */
  look(x, y, w, h, dist = 520) {
    const c = new THREE.Vector3(x + w / 2, -(y + h / 2), 30);
    const d = this.camera.position.clone().sub(this.controls.target).normalize().multiplyScalar(dist);
    this.camera.position.copy(c.clone().add(d)); this.controls.target.copy(c); this.controls.update(); this.dirty = true;
  }
  _loop() {
    if (this.controls.update()) this.dirty = true;
    if (this.dirty) { this.dirty = false; this.renderer.render(this.scene, this.camera); }
    requestAnimationFrame(this._loop);
  }
}
