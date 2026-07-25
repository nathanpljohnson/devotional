# Leadership & the Kingdom

A thirty-five day devotional on leadership, power, and political authority in Scripture — 25 July to 28 August 2026 — read alongside philosophy and literature. Built as an offline-first PWA for iPhone.

## Put it on your phone

1. Open the deployed URL in **Safari** on your iPhone (must be Safari, not Chrome).
2. Tap the **Share** button, then **Add to Home Screen**.
3. Open it from the home-screen icon. It runs fullscreen with no browser chrome.
4. Let it sit on wifi for ~30 seconds the first time so it caches all 13.6 MB of art and text.
5. After that it works with no connection at all. Test it: turn on airplane mode and reopen.

It opens to whatever today's reading is, based on your device date. Outside the date range it clamps to day 1 or day 35.

## Using it

- **Swipe left/right** — previous / next day. Arrow keys on desktop.
- **Tap "Day N of 35"** — the day grid, grouped by the five weeks.
- **Tap the person icon** — the people index: who each thinker was and why they're here.
- **Tap any author's name** under a quote — jumps to their entry in the index.
- Light and dark follow your system appearance automatically.

## What's in each day

1. Week name, day, date, title, passage reference
2. **The voice** — a substantial passage from a public-domain thinker
3. The day's **painting**, framed, with a wall label
4. **The situation** — short factual framing of the chapter: who, what, when
5. **A second voice** where there is one — often a modern writer who cuts against the first
6. The **full chapter**, World English Bible, as flowing prose with a drop cap

## Sourcing

Nothing here is paraphrased from memory.

- **Scripture** is the World English Bible (public domain), fetched complete from `bible-api.com`. 35 chapters, 988 verses, bundled for offline use.
- **Long quotations** are extracted verbatim from public-domain source texts downloaded into `corpus/` from Project Gutenberg, CCEL, and the Internet Archive — 32 works. `scripts/q.py` and `scripts/batch.py` are the tools used to locate each passage in its source.
- **Short quotations from in-copyright authors** (Lewis, Weil, Arendt, Solzhenitsyn, Endō) are kept brief, fully attributed, and were verified against published sources rather than recalled. Where a passage could not be verified it was dropped — Bentham is represented through Mill's exposition because the only available scan of *Principles of Morals and Legislation* was too OCR-degraded to quote safely.
- **Art** is public-domain, sourced from Wikimedia Commons with artist, date, and licence pulled from Commons metadata. Wall labels were then written by hand.
- **Backgrounds** are NASA public-domain imagery, two per thematic week.

The framing text in "The situation" is written to be factual — who is speaking, what is happening, when — and deliberately stops short of interpretation. The interpretive weight is carried by the named thinkers.

## Structure

| Week | Theme |
|---|---|
| 1 | The Call and the Refusal |
| 2 | Power and What It Does to You |
| 3 | Counsel, Dissent, and Truth-Telling |
| 4 | Command, War, and Restraint |
| 5 | The Kingdom That Isn't Yours |

## Files

```
index.html app.css app.js       the whole app — no build step, no dependencies
sw.js                           offline cache (58 entries). bump VERSION to force a refresh
manifest.webmanifest            home-screen identity
data/days.json                  quotes, framing, day plan
data/bible.json                 35 full chapters, WEB
data/art.json  data/people.json data/bg.json
assets/art/     35 plates       assets/bg/  10 backgrounds
scripts/                        every fetch and build step, re-runnable
corpus/                         public-domain sources (gitignored; run scripts/fetch_corpus.py)
serve.py                        local static server: python3 serve.py -> :8077
```

## Editing content

Content lives in `scripts/build_days.py`. Edit it and re-run:

```bash
cd scripts && python3 build_days.py && python3 build_people.py
```

Then bump `VERSION` in `sw.js` so phones pick up the change instead of serving the cached copy.

## Local development

```bash
python3 serve.py
```

Then open `http://localhost:8077/?nosw=1` — the `nosw` flag skips the service worker, which otherwise serves cached files and hides your edits.
