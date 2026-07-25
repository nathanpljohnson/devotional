(() => {
'use strict';

const FIRST = '2026-07-25';
const LAST  = '2026-08-28';
const N     = 35;

const $ = s => document.querySelector(s);
const el = (tag, cls, html) => {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (html != null) n.innerHTML = html;
  return n;
};
const esc = s => String(s).replace(/[&<>"]/g, c =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

let DATA = null, BIBLE = null, ART = null, PEOPLE = null;
let cur = 1;

/* ── which day is it ─────────────────────────────────────── */
function todayIndex() {
  const now = new Date();
  const local = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
  if (local < FIRST) return 1;
  if (local > LAST) return N;
  const ms = new Date(local + 'T00:00:00') - new Date(FIRST + 'T00:00:00');
  return Math.min(N, Math.max(1, Math.round(ms / 86400000) + 1));
}

function prettyDate(iso) {
  const d = new Date(iso + 'T00:00:00');
  return d.toLocaleDateString(undefined, { weekday: 'long', month: 'long', day: 'numeric' });
}

/* ── render ──────────────────────────────────────────────── */
function quotePanel(v, labelText, small) {
  const p = el('section', 'panel q rise');
  p.appendChild(el('p', 'label', esc(labelText)));
  p.appendChild(el('span', 'qmark', '&ldquo;'));
  p.appendChild(el('blockquote', 'qtext' + (small ? ' small' : ''), esc(v.text)));

  const a = el('div', 'attrib');
  const who = el('button', 'who', esc(v.author));
  who.addEventListener('click', () => openPeople(v.author));
  a.appendChild(who);
  a.appendChild(el('span', null, `${esc(v.work)}${v.year ? ' &middot; ' + esc(v.year) : ''}`));
  p.appendChild(a);

  if (v.note) p.appendChild(el('p', 'qnote', esc(v.note)));
  return p;
}

function chapterHTML(b) {
  const parts = b.verses.map((v, i) => {
    const t = esc(v.t);
    if (i === 0) {
      const m = t.match(/^(\W*)(\w)([\s\S]*)$/);
      if (m) return `<span class="v"><sup>${v.n}</sup>${m[1]}<span class="drop">${m[2]}</span>${m[3]}</span>`;
    }
    return `<span class="v"><sup>${v.n}</sup>${t}</span>`;
  });
  return parts.join(' ');
}

function render(n, animate = true) {
  cur = n;
  const d = DATA.days[String(n)];
  const wk = DATA.weeks[String(d.week)];
  const b = BIBLE[String(n)];
  const art = ART[String(n)];
  const host = $('#day');
  host.textContent = '';

  /* background */
  const bgimg = $('#bgimg');
  const url = `assets/bg/${d.bg}.jpg`;
  if (bgimg.dataset.src !== url) {
    bgimg.dataset.src = url;
    const pre = new Image();
    pre.onload = () => { bgimg.style.backgroundImage = `url("${url}")`; };
    pre.src = url;
  }

  /* masthead */
  const head = el('section', 'panel rise');
  head.id = 'head';
  head.appendChild(Object.assign(el('p', null, esc(wk.title)), { id: 'week' }));
  head.appendChild(Object.assign(el('p', null,
    `Day ${d.day} of ${N} &nbsp;·&nbsp; ${esc(prettyDate(d.date))}`), { id: 'dayline' }));
  head.appendChild(Object.assign(el('h1', null, esc(d.title)), { id: 'title' }));
  head.appendChild(Object.assign(el('p', null, esc(b.reference)), { id: 'ref' }));
  if (d.day === 1 || DATA.days[String(d.day - 1)]?.week !== d.week) {
    head.appendChild(Object.assign(el('p', null, esc(wk.blurb)), { id: 'weekblurb' }));
  }
  host.appendChild(head);

  /* main voice */
  host.appendChild(quotePanel(d.voice1, 'The voice'));

  /* plate */
  if (art) {
    const fig = el('figure', 'panel plate rise');
    const frame = el('div', 'frame');
    const img = el('img');
    img.src = art.img;
    img.alt = art.title;
    img.loading = 'eager';
    img.decoding = 'async';
    frame.appendChild(img);
    fig.appendChild(frame);
    const cap = el('figcaption');
    cap.appendChild(el('span', 't', esc(art.title)));
    cap.appendChild(el('span', null,
      `${esc(art.artist)}${art.date ? ', ' + esc(art.date) : ''}`));
    cap.appendChild(el('span', 'lic', esc(art.licence) + ' · Wikimedia Commons'));
    fig.appendChild(cap);
    host.appendChild(fig);
  }

  /* context */
  const ctx = el('section', 'panel rise');
  ctx.appendChild(el('p', 'label', 'The situation'));
  ctx.appendChild(el('p', 'ctx', esc(d.context)));
  host.appendChild(ctx);

  /* second voice */
  if (d.voice2) host.appendChild(quotePanel(d.voice2, 'A second voice', true));

  /* scripture */
  const ch = el('section', 'panel rise');
  ch.appendChild(el('p', 'label', esc(b.reference) + ' · World English Bible'));
  ch.appendChild(Object.assign(el('div', null, chapterHTML(b)), { id: 'chap' }));
  host.appendChild(ch);

  /* stagger */
  [...host.children].forEach((c, i) => {
    if (animate) c.style.animationDelay = `${Math.min(i * 55, 330)}ms`;
    else c.classList.remove('rise');
  });

  $('#barlabel').textContent = `Day ${n} of ${N}`;
  $('#prev').disabled = n <= 1;
  $('#next').disabled = n >= N;
  document.title = `${d.title} — Day ${n}`;
  try { localStorage.setItem('devo:last', String(n)); } catch {}
  window.scrollTo({ top: 0, behavior: animate ? 'instant' : 'auto' });
}

/* ── sheets ──────────────────────────────────────────────── */
function openSheet(title, node) {
  $('#sheettitle').textContent = title;
  const c = $('#sheetcontent');
  c.textContent = '';
  c.appendChild(node);
  c.scrollTop = 0;
  $('#sheet').hidden = false;
  document.body.style.overflow = 'hidden';
}
function closeSheet() {
  $('#sheet').hidden = true;
  document.body.style.overflow = '';
}

function openGrid() {
  const wrap = el('div');
  for (let w = 1; w <= 5; w++) {
    wrap.appendChild(el('p', 'gridweek', esc(DATA.weeks[String(w)].title)));
    const g = el('div', 'daygrid');
    Object.values(DATA.days).filter(d => d.week === w).forEach(d => {
      const b = el('button', d.day === cur ? 'on' : (d.day < todayIndex() ? 'past' : ''), String(d.day));
      b.addEventListener('click', () => { closeSheet(); render(d.day); });
      g.appendChild(b);
    });
    wrap.appendChild(g);
  }
  openSheet('Thirty-five days', wrap);
}

function openPeople(focus) {
  const wrap = el('div');
  const names = Object.keys(PEOPLE).sort((a, b) => {
    const la = a.split(' ').pop(), lb = b.split(' ').pop();
    return la.localeCompare(lb);
  });
  names.forEach(name => {
    const p = PEOPLE[name];
    const box = el('div', 'person');
    box.id = 'p-' + name.replace(/\W+/g, '');
    box.appendChild(el('h3', null, esc(name)));
    box.appendChild(el('p', 'meta', `${esc(p.dates)} · ${esc(p.role)}`));
    box.appendChild(el('p', null, esc(p.why)));
    const jump = el('div', 'jump');
    p.days.forEach(dn => {
      const b = el('button', null, `Day ${dn}`);
      b.addEventListener('click', () => { closeSheet(); render(dn); });
      jump.appendChild(b);
    });
    box.appendChild(jump);
    wrap.appendChild(box);
  });
  openSheet('The people', wrap);
  if (focus) {
    const t = wrap.querySelector('#p-' + focus.replace(/\W+/g, ''));
    if (t) requestAnimationFrame(() =>
      $('#sheetcontent').scrollTo({ top: t.offsetTop - 8, behavior: 'instant' }));
  }
}

/* ── input ───────────────────────────────────────────────── */
function go(delta) {
  const n = cur + delta;
  if (n >= 1 && n <= N) render(n);
}

function wire() {
  $('#prev').addEventListener('click', () => go(-1));
  $('#next').addEventListener('click', () => go(1));
  $('#grid').addEventListener('click', openGrid);
  $('#ppl').addEventListener('click', () => openPeople());
  $('#sheetclose').addEventListener('click', closeSheet);
  $('#sheetbg').addEventListener('click', closeSheet);

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') return closeSheet();
    if ($('#sheet').hidden === false) return;
    if (e.key === 'ArrowLeft') go(-1);
    if (e.key === 'ArrowRight') go(1);
  });

  let x0 = null, y0 = null;
  document.addEventListener('touchstart', e => {
    if (e.touches.length !== 1) return;
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY;
  }, { passive: true });
  document.addEventListener('touchend', e => {
    if (x0 == null || !$('#sheet').hidden) { x0 = null; return; }
    const dx = e.changedTouches[0].clientX - x0;
    const dy = e.changedTouches[0].clientY - y0;
    if (Math.abs(dx) > 62 && Math.abs(dx) > Math.abs(dy) * 1.7) go(dx < 0 ? 1 : -1);
    x0 = null;
  }, { passive: true });
}

/* ── boot ────────────────────────────────────────────────── */
async function boot() {
  const j = async p => (await fetch(p, { cache: 'no-cache' })).json();
  try {
    [DATA, BIBLE, ART, PEOPLE] = await Promise.all([
      j('data/days.json'), j('data/bible.json'), j('data/art.json'), j('data/people.json'),
    ]);
  } catch (err) {
    $('#day').innerHTML =
      '<section class="panel"><p class="label">Could not load</p>' +
      '<p class="ctx">The readings did not load. If this is the first run, check your connection ' +
      'once so the app can cache itself.</p></section>';
    console.error(err);
    return;
  }
  wire();
  render(todayIndex(), true);

  // ?nosw=1 skips offline caching — useful while editing
  if ('serviceWorker' in navigator && !location.search.includes('nosw')) {
    // If a NEW worker takes over an already-controlled page, the content on screen is
    // stale — reload once so an edit shows up without needing a manual second open.
    const hadController = !!navigator.serviceWorker.controller;
    let reloaded = false;
    navigator.serviceWorker.addEventListener('controllerchange', () => {
      if (!hadController || reloaded) return;
      reloaded = true;
      location.reload();
    });
    try { await navigator.serviceWorker.register('sw.js'); } catch (e) { console.warn(e); }
  }
}

boot();
})();
