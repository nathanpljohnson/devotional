"""Pull a pool of NASA imagery candidates for visual review (titles alone mislead)."""
import json, subprocess, pathlib, time

ROOT = pathlib.Path(__file__).parent.parent
CD = ROOT / "assets" / "bg" / "cand"
CD.mkdir(parents=True, exist_ok=True)

QUERIES = [
    "Earth as Art Landsat", "Blue Marble Earth Apollo", "aurora australis space station",
    "sunset atmosphere from orbit", "Sahara sand dunes satellite", "Himalaya snow satellite",
    "cloud vortex over ocean", "glacier ice satellite image", "river delta satellite image",
    "volcanic landscape aerial", "Grand Canyon aerial view", "Earth night lights horizon",
    "noctilucent clouds", "Andes mountains satellite", "Milky Way night sky observatory",
    "storm clouds from space station", "salt flats Landsat", "forest canopy aerial",
]


def get(url):
    for a in range(3):
        try:
            r = subprocess.run(["curl", "-sSL", "--max-time", "40", url],
                               capture_output=True, text=True, check=True)
            return json.loads(r.stdout)
        except Exception:
            time.sleep(2 * (a + 1))
    return None


meta = {}
n = 0
for q in QUERIES:
    s = get(f"https://images-api.nasa.gov/search?q={q.replace(' ', '%20')}&media_type=image")
    items = (s or {}).get("collection", {}).get("items", [])
    taken = 0
    for it in items[:8]:
        if taken >= 2:
            break
        data = it.get("data", [{}])[0]
        title = data.get("title", "")
        low = title.lower()
        # skip obvious non-scenery
        if any(k in low for k in ("damage", "assessment", "portrait", "logo", "patch",
                                  "briefing", "conference", "administrator", "employee",
                                  "building", "facility", "test", "engineer", "map of")):
            continue
        coll = get(it.get("href", ""))
        if not coll:
            continue
        jpgs = [u for u in coll if u.lower().endswith((".jpg", ".jpeg"))]
        if not jpgs:
            continue
        pick = next((u for u in jpgs if "~large" in u), None) or jpgs[0]
        n += 1
        dest = CD / f"c{n:02d}.jpg"
        subprocess.run(["curl", "-sSL", "--max-time", "120", "-o", str(dest), pick],
                       capture_output=True)
        if not dest.exists() or dest.stat().st_size < 60000:
            dest.unlink(missing_ok=True)
            n -= 1
            continue
        subprocess.run(["sips", "-Z", "900", "-s", "format", "jpeg",
                        "-s", "formatOptions", "70", str(dest), "--out", str(dest)],
                       capture_output=True)
        meta[f"c{n:02d}"] = {"title": title, "nasa_id": data.get("nasa_id", ""),
                             "center": data.get("center", ""), "query": q}
        taken += 1
        print(f"  c{n:02d}  {title[:62]}", flush=True)
    time.sleep(0.3)

(ROOT / "data" / "bg_cands.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))
print(f"\n{n} candidates in {CD}")
