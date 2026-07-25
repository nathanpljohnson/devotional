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
- [x] Deploy to GitHub Pages + Add to Home Screen instructions (README)

## Rules for this build
- No invented quotes. Verbatim from a real source or it doesn't ship.
- In-copyright thinkers: short quote + citation only. PD: full passage.
- Context = who/what/when only. No interpretation from me.

## Verified
- All 58 precache URLs fetch 200 and cache (13.65 MB) — checked in-page
- All 35 days render live: 988 verses, no JS errors, every day has plate + label + voice
- Live: https://nathanpljohnson.github.io/devotional/

## Known limits
- The embedded review browser reports the service worker "activated" but does not
  execute it, so end-to-end offline could not be exercised here. Precache manifest
  was validated instead. Confirm on the phone: load once on wifi, then airplane mode.
- Day 9's plate was swapped from Rembrandt's Bathsheba (a nude) to his David and
  Uriah, since this is read at work.
