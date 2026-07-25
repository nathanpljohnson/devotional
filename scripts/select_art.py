"""Lock one artwork per day and download it locally for offline use."""
import json, subprocess, pathlib, time

ROOT = pathlib.Path(__file__).parent.parent
CAND = json.loads((ROOT / "data" / "art_commons.json").read_text())
ARTDIR = ROOT / "assets" / "art"
ARTDIR.mkdir(parents=True, exist_ok=True)

# day: (candidate bucket, index)
PICKS = {
    1: ("1", 0), 2: ("2", 0), 3: ("3", 0), 4: ("4", 2), 5: ("5", 0),
    6: ("7", 0), 7: ("6", 1), 8: ("8", 1), 9: ("9", 2), 10: ("10", 1),
    11: ("11", 0), 12: ("12", 0), 13: ("13", 2), 14: ("14", 1),
    15: ("fix15", 0), 16: ("fix16", 3), 17: ("17", 0), 18: ("18", 1),
    19: ("19", 0), 20: ("20", 0), 21: ("fix21", 2), 22: ("22", 2),
    23: ("23", 0), 24: ("24", 1), 25: ("25", 0), 26: ("26", 1),
    27: ("fix27", 4), 28: ("28", 0), 29: ("fix29", 0), 30: ("fix30", 0),
    31: ("31", 0), 32: ("32", 0), 33: ("33", 0), 34: ("34", 2), 35: ("35", 0),
}

out = {}
for day in sorted(PICKS):
    bucket, idx = PICKS[day]
    pool = CAND.get(bucket, [])
    if idx >= len(pool):
        print(f"day {day:2d}  BAD INDEX {bucket}[{idx}] (len {len(pool)})")
        continue
    c = pool[idx]
    dest = ARTDIR / f"day{day:02d}.jpg"
    if not dest.exists() or dest.stat().st_size < 20000:
        r = subprocess.run(["curl", "-sSL", "--max-time", "90",
                            "-H", "User-Agent: devotional/1.0 (personal offline reader)",
                            "-o", str(dest), c["thumb"]], capture_output=True)
        time.sleep(0.4)
    size = dest.stat().st_size if dest.exists() else 0
    if size < 20000:
        print(f"day {day:2d}  DOWNLOAD FAILED  {c['file'][:50]}")
        continue
    title = c["file"][5:].rsplit(".", 1)[0].replace("_", " ")
    out[str(day)] = {
        "img": f"assets/art/day{day:02d}.jpg",
        "title": title,
        "artist": c["artist"],
        "date": c["date"],
        "licence": c["licence"],
        "source": c["page"],
    }
    print(f"day {day:2d}  {size//1024:4d}KB  {c['artist'][:22]:<22} | {title[:44]}")

(ROOT / "data" / "art.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(f"\n{len(out)}/35 artworks -> data/art.json")
