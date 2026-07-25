"""Run many corpus searches at once, compactly. Edit JOBS and run."""
import re, sys, pathlib, json

CORPUS = pathlib.Path(__file__).parent.parent / "corpus"
_cache = {}


def paras(slug):
    if slug not in _cache:
        t = (CORPUS / f"{slug}.txt").read_text(encoding="utf-8", errors="ignore").replace("\r\n", "\n")
        _cache[slug] = [" ".join(p.split()) for p in re.split(r"\n\s*\n", t)]
    return _cache[slug]


def run(jobs, width=620, maxhits=2, minlen=180):
    for label, slug, pat in jobs:
        print(f"\n╔══ {label}  [{slug}]")
        n = 0
        for p in paras(slug):
            if len(p) < minlen:
                continue
            m = re.search(pat, p, re.I)
            if m:
                n += 1
                lo = max(0, m.start() - width // 3)
                hi = min(len(p), m.start() + width)
                pre = "…" if lo else ""
                post = "…" if hi < len(p) else ""
                print(f"║ ── {n}\n{pre}{p[lo:hi]}{post}")
                if n >= maxhits:
                    break
        if not n:
            print("║ NO MATCH")


if __name__ == "__main__":
    jobs = json.loads(pathlib.Path(sys.argv[1]).read_text())
    w = int(sys.argv[2]) if len(sys.argv) > 2 else 620
    h = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    run([(j[0], j[1], j[2]) for j in jobs], width=w, maxhits=h)
