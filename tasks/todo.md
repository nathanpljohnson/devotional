# Devotional build — 35 days, Jul 25 – Aug 28 2026

## Decisions locked
- PWA, home screen, offline via service worker. iOS 26.5.2.
- WEB (World English Bible), public domain, full chapters bundled.
- ~10 min/day. Short context, long thinker.
- NASA/USGS public-domain imagery as ambient background.
- Met open-access painting as framed plate, after quote, before chapter.
- Five-week topical arc.
- Features: people index, auto light/dark. Nothing else.

## Steps
- [x] Scaffold dirs, verify bible-api / Met / NASA APIs
- [x] Lock 35-day plan (theme, passage, thinkers, art)
- [x] Fetch 35 WEB chapters -> data/bible.json
- [x] Curate 35 Met paintings -> data/art.json, download images
- [x] Curate NASA backgrounds -> assets/bg/
- [x] Source + verify thinker passages (PD verbatim from Gutenberg/CCEL)
- [x] Write day content -> data/days.json
- [x] Write people index -> data/people.json
- [x] Build PWA (index.html, app.js, style.css, sw.js, manifest)
- [x] Verify in browser, screenshot, check offline
- [ ] Deploy + Add to Home Screen instructions

## Rules for this build
- No invented quotes. Verbatim from a real source or it doesn't ship.
- In-copyright thinkers: short quote + citation only. PD: full passage.
- Context = who/what/when only. No interpretation from me.
