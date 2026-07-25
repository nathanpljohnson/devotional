"""Targeted re-search for the eight days whose top candidates were wrong or weak."""
import json, time, pathlib
from fetch_art_commons import api, clean, OUT

FIX = {
    5:  ["Isaiah seraph coal lips", "Isaiah vision of the Lord temple", "Prophet Isaiah Doré"],
    7:  ["Saul proclaimed king Mizpah", "Saul chosen king", "Samuel presents Saul to the people"],
    15: ["Moses appointing judges", "Jethro advises Moses", "Moses choosing the seventy elders"],
    16: ["Micaiah prophet Ahab", "Ahab and Jehoshaphat prophets", "Zedekiah strikes Micaiah"],
    21: ["Poussin Jugement de Salomon Louvre", "Judgment of Solomon Poussin painting"],
    27: ["Joab kills Abner", "Death of Abner Doré", "Abner slain by Joab"],
    29: ["Solomon in judgment throne painting", "King enthroned justice allegory", "Allegory of Justice painting"],
    30: ["Bendemann Jews mourning in exile", "By the waters of Babylon painting", "Jewish exiles Babylon painting"],
}

cache = json.loads(OUT.read_text())

for day, queries in FIX.items():
    got = False
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
            cache[f"fix{day}"] = cands
            OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
            print(f"\nD{day} via '{q}':")
            for i, c in enumerate(cands[:5]):
                print(f"   [{i}] {c['artist'][:26]:<26} | {c['file'][5:62]}")
            got = True
            break
        time.sleep(0.3)
    if not got:
        print(f"\nD{day} NOTHING for any of {queries}")
