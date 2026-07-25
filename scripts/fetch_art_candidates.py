import json, time, subprocess, pathlib
from plan import PLAN

OUT = pathlib.Path(__file__).parent.parent / "data" / "art_candidates.json"
BASE = "https://collectionapi.metmuseum.org/public/collection/v1"
OK_CLASS = ("painting", "print", "drawing")

cache = json.loads(OUT.read_text()) if OUT.exists() else {}


def get(url):
    for attempt in range(5):
        try:
            r = subprocess.run(["curl", "-sSL", "--max-time", "40", url],
                               capture_output=True, text=True, check=True)
            return json.loads(r.stdout)
        except Exception:
            time.sleep(3 * (attempt + 1))
    return None


for day, date, week, title, slug, terms in PLAN:
    key = str(day)
    if key in cache:
        continue
    seen, cands = set(), []
    for term in terms:
        q = term.replace(" ", "%20")
        s = get(f"{BASE}/search?q={q}&hasImages=true")
        if not s or not s.get("objectIDs"):
            continue
        for oid in s["objectIDs"][:14]:
            if oid in seen:
                continue
            seen.add(oid)
            o = get(f"{BASE}/objects/{oid}")
            time.sleep(0.12)
            if not o or not o.get("isPublicDomain") or not o.get("primaryImage"):
                continue
            cls = (o.get("classification") or "").lower()
            if not any(k in cls for k in OK_CLASS):
                continue
            cands.append({
                "id": oid,
                "title": o.get("title"),
                "artist": o.get("artistDisplayName") or "Unknown",
                "date": o.get("objectDate"),
                "classification": o.get("classification"),
                "image": o.get("primaryImage"),
                "small": o.get("primaryImageSmall"),
                "url": o.get("objectURL"),
                "term": term,
            })
    cache[key] = cands
    OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
    print(f"day {day:2d}  {title[:34]:<34} {len(cands):3d} candidates")

print(f"\n-> {OUT}")
