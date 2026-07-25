/* Offline shell for the devotional. Bump VERSION to force a refresh. */
const VERSION = 'devo-v2';
const ASSETS = [
  "./",
  "index.html",
  "app.css",
  "app.js",
  "manifest.webmanifest",
  "data/days.json",
  "data/bible.json",
  "data/art.json",
  "data/people.json",
  "data/bg.json",
  "assets/icon-180.png",
  "assets/icon-192.png",
  "assets/icon-512.png",
  "assets/art/day01.jpg",
  "assets/art/day02.jpg",
  "assets/art/day03.jpg",
  "assets/art/day04.jpg",
  "assets/art/day05.jpg",
  "assets/art/day06.jpg",
  "assets/art/day07.jpg",
  "assets/art/day08.jpg",
  "assets/art/day09.jpg",
  "assets/art/day10.jpg",
  "assets/art/day11.jpg",
  "assets/art/day12.jpg",
  "assets/art/day13.jpg",
  "assets/art/day14.jpg",
  "assets/art/day15.jpg",
  "assets/art/day16.jpg",
  "assets/art/day17.jpg",
  "assets/art/day18.jpg",
  "assets/art/day19.jpg",
  "assets/art/day20.jpg",
  "assets/art/day21.jpg",
  "assets/art/day22.jpg",
  "assets/art/day23.jpg",
  "assets/art/day24.jpg",
  "assets/art/day25.jpg",
  "assets/art/day26.jpg",
  "assets/art/day27.jpg",
  "assets/art/day28.jpg",
  "assets/art/day29.jpg",
  "assets/art/day30.jpg",
  "assets/art/day31.jpg",
  "assets/art/day32.jpg",
  "assets/art/day33.jpg",
  "assets/art/day34.jpg",
  "assets/art/day35.jpg",
  "assets/bg/w1a.jpg",
  "assets/bg/w1b.jpg",
  "assets/bg/w2a.jpg",
  "assets/bg/w2b.jpg",
  "assets/bg/w3a.jpg",
  "assets/bg/w3b.jpg",
  "assets/bg/w4a.jpg",
  "assets/bg/w4b.jpg",
  "assets/bg/w5a.jpg",
  "assets/bg/w5b.jpg"
];

async function report(msg) {
  const cs = await self.clients.matchAll({includeUncontrolled: true});
  cs.forEach(c => c.postMessage(msg));
}

self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const failures = [];
    let cache;
    try {
      cache = await caches.open(VERSION);
    } catch (err) {
      await report({type: 'sw-install', fatal: 'open: ' + err.name + ' ' + err.message});
      return;
    }
    for (const u of ASSETS) {
      try {
        const res = await fetch(u, {cache: 'reload'});
        if (!res.ok) { failures.push(u + ' -> HTTP ' + res.status); continue; }
        await cache.put(u, res);
      } catch (err) {
        failures.push(u + ' -> ' + err.name + ': ' + err.message);
      }
    }
    const n = (await cache.keys()).length;
    await report({type: 'sw-install', cached: n, wanted: ASSETS.length, failures: failures.slice(0, 8)});
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  e.respondWith((async () => {
    const cached = await caches.match(req, {ignoreSearch: true});
    if (cached) return cached;
    try {
      const res = await fetch(req);
      if (res.ok) {
        const c = await caches.open(VERSION);
        c.put(req, res.clone()).catch(() => {});
      }
      return res;
    } catch (err) {
      if (req.mode === 'navigate') {
        const shell = await caches.match('index.html') || await caches.match('./');
        if (shell) return shell;
      }
      throw err;
    }
  })());
});
