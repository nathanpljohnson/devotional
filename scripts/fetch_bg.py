"""NASA public-domain imagery for the ambient backgrounds: two per thematic week."""
import json, subprocess, pathlib, time

ROOT = pathlib.Path(__file__).parent.parent
BG = ROOT / "assets" / "bg"
BG.mkdir(parents=True, exist_ok=True)

# slug: (search query, preferred keyword in title)
WANTED = [
    ("w1a", "Sinai peninsula desert", "sinai"),
    ("w1b", "sand dunes desert Landsat", "dune"),
    ("w2a", "hurricane seen from space", "hurricane"),
    ("w2b", "thunderstorm clouds from orbit", "storm"),
    ("w3a", "sunrise seen from the space station", "sunrise"),
    ("w3b", "cloud layers atmosphere limb", "cloud"),
    ("w4a", "Himalaya mountains from space", "himalaya"),
    ("w4b", "mountain range snow Landsat", "mountain"),
    ("w5a", "Earth limb horizon from orbit", "earth"),
    ("w5b", "aurora from the space station", "aurora"),
]


def get(url):
    for a in range(4):
        try:
            r = subprocess.run(["curl", "-sSL", "--max-time", "45", url],
                               capture_output=True, text=True, check=True)
            return json.loads(r.stdout)
        except Exception:
            time.sleep(2 * (a + 1))
    return None


manifest = {}
for slug, query, prefer in WANTED:
    dest = BG / f"{slug}.jpg"
    if dest.exists() and dest.stat().st_size > 40000:
        print(f"  cached {slug}")
        continue
    s = get(f"https://images-api.nasa.gov/search?q={query.replace(' ', '%20')}&media_type=image")
    items = (s or {}).get("collection", {}).get("items", [])
    if not items:
        print(f"  NO RESULTS {slug} ({query})")
        continue

    items.sort(key=lambda it: 0 if prefer in str(
        it.get("data", [{}])[0].get("title", "")).lower() else 1)

    for it in items[:6]:
        data = it.get("data", [{}])[0]
        coll = get(it.get("href", ""))
        if not coll:
            continue
        jpgs = [u for u in coll if u.lower().endswith((".jpg", ".jpeg"))]
        if not jpgs:
            continue
        pick = next((u for u in jpgs if "~large" in u), None) or \
               next((u for u in jpgs if "~orig" in u), None) or jpgs[0]
        subprocess.run(["curl", "-sSL", "--max-time", "150", "-o", str(dest), pick],
                       capture_output=True)
        if dest.exists() and dest.stat().st_size > 40000:
            manifest[slug] = {
                "title": data.get("title", ""),
                "center": data.get("center", ""),
                "nasa_id": data.get("nasa_id", ""),
                "date": (data.get("date_created") or "")[:10],
            }
            print(f"  {slug}  {dest.stat().st_size//1024:5d}KB  {data.get('title','')[:56]}")
            break
        time.sleep(1)
    else:
        print(f"  FAILED {slug}")
    time.sleep(0.5)

path = ROOT / "data" / "bg.json"
existing = json.loads(path.read_text()) if path.exists() else {}
existing.update(manifest)
path.write_text(json.dumps(existing, ensure_ascii=False, indent=1))
print(f"\n-> {path}")
