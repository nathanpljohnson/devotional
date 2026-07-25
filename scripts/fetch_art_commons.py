"""Curate one public-domain artwork per day from Wikimedia Commons.
Metadata (artist, date, licence) comes from Commons itself, never from guesswork."""
import json, time, subprocess, pathlib, urllib.parse

OUT = pathlib.Path(__file__).parent.parent / "data" / "art_commons.json"
API = "https://commons.wikimedia.org/w/api.php"

QUERIES = {
    1:  "Moses and the Burning Bush painting",
    2:  "Moses and Aaron before Pharaoh painting",
    3:  "Gideon angel painting",
    4:  "Rembrandt Jeremiah Lamenting the Destruction of Jerusalem",
    5:  "Isaiah vision seraphim painting",
    6:  "Samuel anointing Saul painting",
    7:  "Saul and Samuel painting",
    8:  "Moses with the Tablets of the Law painting",
    9:  "Rembrandt Bathsheba at her bath",
    10: "Rembrandt Nathan Admonishing David",
    11: "Solomon idolatry painting",
    12: "Rehoboam painting",
    13: "William Blake Nebuchadnezzar",
    14: "Bruegel Fall of the Rebel Angels",
    15: "Moses and Jethro painting",
    16: "Micaiah Ahab prophets painting",
    17: "Daniel before Nebuchadnezzar painting",
    18: "Gentileschi Esther before Ahasuerus",
    19: "Amos prophet painting",
    20: "Nehemiah rebuilding the walls of Jerusalem",
    21: "Poussin Judgment of Solomon",
    22: "Joshua commanding the sun to stand still painting",
    23: "Destruction of Jerusalem siege painting",
    24: "Stoning of Achan",
    25: "David and Saul in the cave painting",
    26: "Abigail meeting David painting",
    27: "Death of Abner Joab painting",
    28: "Elisha and the Syrian army painting",
    29: "Solomon on his throne painting",
    30: "Tissot The Flight of the Prisoners Babylon",
    31: "Jeremiah in the cistern dungeon",
    32: "Turner Shadrach Meshach and Abednego fiery furnace",
    33: "Man of Sorrows painting Christ",
    34: "Christ washing the feet of the disciples painting",
    35: "Munkacsy Christ before Pilate",
}

cache = json.loads(OUT.read_text()) if OUT.exists() else {}


def api(params):
    qs = urllib.parse.urlencode({**params, "format": "json"})
    for a in range(4):
        try:
            r = subprocess.run(["curl", "-sSL", "--max-time", "40", f"{API}?{qs}"],
                               capture_output=True, text=True, check=True)
            return json.loads(r.stdout)
        except Exception:
            time.sleep(2 * (a + 1))
    return None


def clean(s):
    if not s:
        return ""
    out, depth = [], 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(ch)
    return " ".join("".join(out).split())


def main():
  for day in sorted(QUERIES):
      key = str(day)
      if key in cache and cache[key]:
          continue
      s = api({"action": "query", "list": "search", "srsearch": QUERIES[day],
               "srnamespace": 6, "srlimit": 10})
      titles = [x["title"] for x in (s or {}).get("query", {}).get("search", [])
                if x["title"].lower().endswith((".jpg", ".jpeg", ".png"))]
      if not titles:
          cache[key] = []
          print(f"day {day:2d}  NO FILES  ({QUERIES[day]})")
          continue

      info = api({"action": "query", "titles": "|".join(titles[:10]),
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
              "licence": lic,
              "thumb": ii.get("thumburl"),
              "page": ii.get("descriptionurl"),
              "w": ii.get("width"), "h": ii.get("height"),
          })
      cache[key] = cands
      OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
      top = cands[0] if cands else None
      print(f"day {day:2d} [{len(cands)}] " + (
          f'{top["artist"][:26]} — {top["file"][5:50]}' if top else "EMPTY"), flush=True)
      time.sleep(0.3)



if __name__ == "__main__":
    main()
    print(f"-> {OUT}")
