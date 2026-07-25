# -*- coding: utf-8 -*-
"""Turn Commons filenames into wall-label captions, and Wikidata date blobs into years."""
import json, re, pathlib

ROOT = pathlib.Path(__file__).parent.parent
ART = json.loads((ROOT / "data" / "art.json").read_text())

JUNK = [
    r"\bWGA\d+\b", r"\bMET\s+[A-Z]{2}\d+[A-Z]*\b", r"\bDP\d+\b", r"\bDT\d+\b",
    r"\bRP-P-[\w.\-]+\b", r"\bLACMA\s+[\w.\-]+\b", r"\bKMS[\w]*\b", r"\bSM\s*sg\d+\b",
    r"\bE\d{4,}\b", r"\bL\d{5}-[\w\-]+\b", r"Google Art Project", r"\bmerge\b",
    r"\b\d{4}\.\d+\.\d+\b", r"\b\d{7,}\b", r"\bcropped\b", r"\bFXD\b",
    r"\b\d{4}\.\d{2}\b", r"\bx-raynocap\b", r"\(\s*\)",
]


def clean_title(raw, artist):
    t = raw.replace("_", " ")
    t = re.sub(r"^\d{2,3}\.\s*", "", t)                    # Doré plate numbers
    parts = [p.strip() for p in t.split(" - ")]
    # drop any segment that is just the artist, or dates, or junk
    surnames = [w for w in re.split(r"[\s,;/()]+", artist) if len(w) > 3]
    keep = []
    for p in parts:
        if not p:
            continue
        low = p.lower()
        if any(s.lower() in low for s in surnames) and len(p.split()) <= 6:
            continue
        if re.fullmatch(r"[\d\W]+", p):
            continue
        keep.append(p)
    t = " — ".join(keep) if keep else parts[0]
    for j in JUNK:
        t = re.sub(j, "", t, flags=re.I)
    t = re.sub(r"\(\d{4}-\d{4}\)", "", t)
    t = re.sub(r"\s{2,}", " ", t).strip(" —-–,;·|")
    t = re.sub(r"\s+([,;.])", r"\1", t)
    return t or raw


def clean_date(raw):
    if not raw:
        return ""
    s = str(raw)
    s = re.sub(r"date\s*QS:.*$", "", s, flags=re.I | re.S)
    s = re.sub(r"[+\-]?\d{4}-\d{2}-\d{2}T[\d:]+Z?(/\d+)?", "", s)
    rng = re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b\s*[-–—/]\s*\b(1[0-9]{3}|20[0-2][0-9])\b", s)
    if rng:
        return f"{rng.group(1)}–{rng.group(2)}"
    circa = re.search(r"\b(ca?\.?|circa|c)\s*(1[0-9]{3})\b", s, re.I)
    if circa:
        return f"c. {circa.group(2)}"
    yr = re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", s)
    return yr.group(1) if yr else ""


def clean_artist(raw):
    a = re.sub(r"\s*\(.*?\)\s*", " ", raw)
    a = re.sub(r"(Unknown author)+", "Unknown", a, flags=re.I)
    a = re.sub(r"^(After|Attributed to)\s+", r"\1 ", a, flags=re.I)
    a = re.sub(r"\s*[/,]\s*.*$", "", a) if len(a) > 46 else a
    a = re.sub(r"–\s*Artist.*$", "", a)
    a = re.sub(r"\s{2,}", " ", a).strip(" ,;/–-")
    return a or "Unknown"


for k in sorted(ART, key=int):
    a = ART[k]
    a["artist"] = clean_artist(a["artist"])
    a["title"] = clean_title(a["title"], a["artist"])
    a["date"] = clean_date(a["date"])
    print(f"D{k:>2}  {a['artist'][:26]:<26} | {a['title'][:46]:<46} | {a['date']}")

(ROOT / "data" / "art.json").write_text(json.dumps(ART, ensure_ascii=False, indent=1))
print("\ncleaned -> data/art.json")
