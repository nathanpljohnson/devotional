import json, time, subprocess, pathlib
from plan import PLAN

OUT = pathlib.Path(__file__).parent.parent / "data" / "bible.json"
result = json.loads(OUT.read_text()) if OUT.exists() else {}


def get(url):
    return subprocess.run(
        ["curl", "-sSL", "--max-time", "45", url],
        capture_output=True, text=True, check=True,
    ).stdout


for day, date, week, title, slug, art in PLAN:
    if str(day) in result:
        continue
    url = f"https://bible-api.com/{slug}?translation=web"
    for attempt in range(6):
        try:
            d = json.loads(get(url))
            break
        except Exception as e:
            if attempt == 5:
                raise SystemExit(f"FAILED day {day} {slug}: {e}")
            time.sleep(5 * (attempt + 1))

    verses = [{"n": v["verse"], "t": " ".join(v["text"].split())} for v in d["verses"]]
    result[str(day)] = {
        "reference": d["reference"],
        "book": d["verses"][0]["book_name"],
        "chapter": d["verses"][0]["chapter"],
        "verses": verses,
    }
    words = sum(len(v["t"].split()) for v in verses)
    print(f"day {day:2d}  {d['reference']:<20} {len(verses):3d} verses  {words:5d} words")
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1))
    time.sleep(1.5)

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1))
total = sum(len(v["verses"]) for v in result.values())
print(f"\n{len(result)} chapters, {total} verses -> {OUT}")
