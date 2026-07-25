"""Fill days that came back empty, trying progressively broader queries."""
import json, time, subprocess, pathlib, urllib.parse
from fetch_art_commons import api, clean, OUT

FALLBACKS = {
    5:  ["Vision of Isaiah", "Isaiah prophet engraving", "Prophet Isaiah"],
    8:  ["Moses tablets of the law", "Moses Ten Commandments painting", "Moses law"],
    9:  ["Bathsheba painting", "David and Bathsheba", "Bathsheba bathing"],
    15: ["Jethro Moses", "Moses father in law Jethro", "Jethro"],
    16: ["Micaiah", "Ahab prophet Zedekiah", "Ahab king Israel painting"],
    20: ["Nehemiah", "Nehemiah wall Jerusalem", "Nehemiah prophet"],
    22: ["Joshua battle painting", "Joshua son of Nun", "Joshua Israelites"],
    23: ["Siege of Jerusalem painting", "Roman siege Jerusalem Titus", "ancient siege city painting"],
    27: ["Abner", "Joab", "Abner death"],
    28: ["Elisha", "Elisha prophet", "Elisha Syrians"],
    29: ["Solomon throne", "King Solomon painting", "Solomon judgment throne"],
    30: ["Babylonian captivity painting", "By the rivers of Babylon", "Jews exile Babylon painting"],
    31: ["Jeremiah cistern", "Jeremiah prophet dungeon", "Prophet Jeremiah engraving"],
}

cache = json.loads(OUT.read_text())

for day, queries in FALLBACKS.items():
    key = str(day)
    if cache.get(key):
        continue
    for q in queries:
        s = api({"action": "query", "list": "search", "srsearch": q,
                 "srnamespace": 6, "srlimit": 14})
        titles = [x["title"] for x in (s or {}).get("query", {}).get("search", [])
                  if x["title"].lower().endswith((".jpg", ".jpeg", ".png"))]
        if not titles:
            continue
        info = api({"action": "query", "titles": "|".join(titles[:14]),
                    "prop": "imageinfo", "iiprop": "url|size|extmetadata",
                    "iiurlwidth": 1400})
        cands = []
        for page in (info or {}).get("query", {}).get("pages", {}).values():
            ii = (page.get("imageinfo") or [{}])[0]
            if not ii:
                continue
            em = ii.get("extmetadata", {})
            lic = clean(em.get("LicenseShortName", {}).get("value", ""))
            if not any(k in lic.lower() for k in ("public domain", "pd", "cc0")):
                continue
            if (ii.get("width") or 0) < 700:
                continue
            cands.append({
                "file": page["title"],
                "artist": clean(em.get("Artist", {}).get("value", "")) or "Unknown",
                "date": clean(em.get("DateTimeOriginal", {}).get("value", "")),
                "credit": clean(em.get("Credit", {}).get("value", ""))[:120],
                "licence": lic, "thumb": ii.get("thumburl"),
                "page": ii.get("descriptionurl"),
                "w": ii.get("width"), "h": ii.get("height"),
            })
        if cands:
            cache[key] = cands
            OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
            print(f"day {day:2d} [{len(cands)}] via '{q}' — {cands[0]['artist'][:24]} / {cands[0]['file'][5:52]}", flush=True)
            break
        time.sleep(0.3)
    else:
        print(f"day {day:2d} STILL EMPTY", flush=True)

still = [k for k, v in cache.items() if not v]
print(f"\nremaining empty: {still}")
