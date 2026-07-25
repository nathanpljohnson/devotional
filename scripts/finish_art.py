"""Retry rate-limited downloads with backoff, then downsize every plate for a phone."""
import json, subprocess, pathlib, time

ROOT = pathlib.Path(__file__).parent.parent
CAND = json.loads((ROOT / "data" / "art_commons.json").read_text())
ART = json.loads((ROOT / "data" / "art.json").read_text())
ARTDIR = ROOT / "assets" / "art"
UA = "devotional/1.0 (personal offline devotional reader; contact nathanpljohnson@gmail.com)"

RETRY = {22: ("22", 2), 23: ("23", 0), 26: ("26", 1), 31: ("31", 0),
         32: ("32", 0), 33: ("33", 0), 34: ("34", 2)}

for day, (bucket, idx) in RETRY.items():
    if str(day) in ART:
        continue
    c = CAND[bucket][idx]
    dest = ARTDIR / f"day{day:02d}.jpg"
    for attempt in range(6):
        subprocess.run(["curl", "-sSL", "--max-time", "120", "-H", f"User-Agent: {UA}",
                        "-o", str(dest), c["thumb"]], capture_output=True)
        if dest.exists() and dest.stat().st_size > 20000:
            break
        wait = 8 * (attempt + 1)
        print(f"  day {day} attempt {attempt+1} failed, waiting {wait}s")
        time.sleep(wait)
    if not (dest.exists() and dest.stat().st_size > 20000):
        print(f"day {day:2d}  STILL FAILING")
        continue
    ART[str(day)] = {
        "img": f"assets/art/day{day:02d}.jpg",
        "title": c["file"][5:].rsplit(".", 1)[0].replace("_", " "),
        "artist": c["artist"], "date": c["date"],
        "licence": c["licence"], "source": c["page"],
    }
    print(f"day {day:2d}  OK {dest.stat().st_size//1024}KB  {c['artist'][:24]}")
    time.sleep(3)

(ROOT / "data" / "art.json").write_text(json.dumps(ART, ensure_ascii=False, indent=1))
print(f"\n{len(ART)}/35 in art.json")

print("\nresizing…")
total = 0
for f in sorted(ARTDIR.glob("day*.jpg")):
    subprocess.run(["sips", "-Z", "1500", "-s", "format", "jpeg",
                    "-s", "formatOptions", "80", str(f), "--out", str(f)],
                   capture_output=True)
    kb = f.stat().st_size // 1024
    total += kb
    if kb > 400:
        print(f"  {f.name} still {kb}KB")
print(f"art total: {total/1024:.1f}MB across {len(list(ARTDIR.glob('day*.jpg')))} files")
