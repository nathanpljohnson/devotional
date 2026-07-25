"""Met open-access art. Plain search (title=true is broken server-side), then filter on real titles."""
import json, time, subprocess, pathlib, re

OUT = pathlib.Path(__file__).parent.parent / "data" / "art_candidates3.json"
BASE = "https://collectionapi.metmuseum.org/public/collection/v1"
DEPTH = 90

# day: [(search term, regex the object title must match)]
TERMS = {
    1:  [("Moses burning bush", r"burning bush"), ("Moses", r"\bmoses\b")],
    2:  [("Moses Aaron Pharaoh", r"aaron|pharaoh"), ("Moses", r"\bmoses\b")],
    3:  [("Gideon", r"gideon")],
    4:  [("Jeremiah prophet", r"jeremiah"), ("prophet", r"prophet")],
    5:  [("Isaiah prophet", r"isaiah"), ("seraph", r"seraph|prophet")],
    6:  [("Samuel prophet", r"samuel"), ("Saul", r"saul")],
    7:  [("Saul Samuel anointing", r"saul"), ("Samuel", r"samuel")],
    8:  [("Moses tablets law", r"tablets|law"), ("Moses", r"\bmoses\b")],
    9:  [("Bathsheba David", r"bathsheba"), ("David", r"\bdavid\b")],
    10: [("Nathan David", r"nathan"), ("David", r"\bdavid\b")],
    11: [("Solomon idolatry", r"solomon"), ("Solomon", r"solomon")],
    12: [("Rehoboam", r"rehoboam|jeroboam"), ("Solomon", r"solomon")],
    13: [("Nebuchadnezzar", r"nebuchadnezzar"), ("Daniel", r"daniel")],
    14: [("fall rebel angels", r"rebel angel|fall of|lucifer"), ("pride", r"pride|vanity")],
    15: [("Moses Jethro", r"jethro"), ("Moses", r"\bmoses\b")],
    16: [("Ahab Micaiah prophets", r"ahab|micaiah"), ("prophet king", r"prophet")],
    17: [("Daniel Babylon", r"daniel"), ("Daniel", r"daniel")],
    18: [("Esther Ahasuerus", r"esther|ahasuerus|mordecai"), ("Esther", r"esther")],
    19: [("Amos prophet", r"amos"), ("prophet", r"prophet")],
    20: [("Nehemiah Jerusalem", r"nehemiah"), ("Jerusalem rebuilding", r"jerusalem")],
    21: [("Judgment of Solomon", r"judgment of solomon"), ("Solomon", r"solomon")],
    22: [("Joshua", r"joshua")],
    23: [("siege city", r"siege"), ("battle", r"battle|siege")],
    24: [("Achan Joshua", r"achan|\bai\b"), ("Joshua", r"joshua")],
    25: [("David Saul cave", r"david and saul|saul"), ("David", r"\bdavid\b")],
    26: [("Abigail David", r"abigail")],
    27: [("Abner Joab David", r"abner|joab"), ("David", r"\bdavid\b")],
    28: [("Elisha", r"elisha")],
    29: [("Solomon throne justice", r"solomon|justice"), ("justice", r"justice")],
    30: [("Babylon captivity exile", r"babylon|captivity|exile"), ("Jerusalem destruction", r"jerusalem")],
    31: [("Jeremiah", r"jeremiah"), ("prophet dungeon", r"prophet")],
    32: [("fiery furnace", r"furnace"), ("three Hebrews Daniel", r"furnace|daniel")],
    33: [("Man of Sorrows", r"man of sorrows"), ("Christ crowned thorns", r"thorns|sorrows")],
    34: [("washing of the feet", r"washing.*feet|feet"), ("Christ apostles", r"christ.*(apostle|disciple)")],
    35: [("Christ before Pilate", r"pilate"), ("Ecce Homo", r"ecce homo")],
}

cache = json.loads(OUT.read_text()) if OUT.exists() else {}


def get(url):
    for a in range(5):
        try:
            r = subprocess.run(["curl", "-sSL", "--max-time", "40", url],
                               capture_output=True, text=True, check=True)
            return json.loads(r.stdout)
        except Exception:
            time.sleep(1.5 * (a + 1))
    return None


def rank(c):
    cls = (c["classification"] or "").lower()
    return (0 if "painting" in cls else 1 if "print" in cls else 2, c["tier"])


for day in sorted(TERMS):
    key = str(day)
    if key in cache and cache[key]:
        continue
    seen, cands = set(), []
    for tier, (term, want) in enumerate(TERMS[day]):
        s = get(f"{BASE}/search?q={term.replace(' ', '%20')}&hasImages=true")
        if not s or not s.get("objectIDs"):
            continue
        for oid in s["objectIDs"][:DEPTH]:
            if oid in seen:
                continue
            seen.add(oid)
            o = get(f"{BASE}/objects/{oid}")
            time.sleep(0.06)
            if not o or not o.get("isPublicDomain") or not o.get("primaryImageSmall"):
                continue
            cls = (o.get("classification") or "").lower()
            if not any(k in cls for k in ("painting", "print", "drawing")):
                continue
            if not re.search(want, (o.get("title") or ""), re.I):
                continue
            cands.append({
                "id": oid, "title": o.get("title"),
                "artist": o.get("artistDisplayName") or "Unknown",
                "date": o.get("objectDate"),
                "classification": o.get("classification"),
                "image": o.get("primaryImageSmall"),
                "large": o.get("primaryImage"),
                "url": o.get("objectURL"), "tier": tier,
            })
            if len(cands) >= 6:
                break
        if len(cands) >= 4:
            break
    cands.sort(key=rank)
    cache[key] = cands
    OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
    top = " | ".join(f'{c["artist"][:14]}: {c["title"][:26]}' for c in cands[:2]) or "EMPTY"
    print(f"day {day:2d} [{len(cands)}] {top}", flush=True)

print(f"\n-> {OUT}")
