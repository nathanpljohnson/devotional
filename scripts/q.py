"""Quote finder: python3 q.py <corpus_slug> "<regex>" [chars_of_context]
Prints flowed paragraphs around each hit so passages can be copied verbatim."""
import re, sys, pathlib

CORPUS = pathlib.Path(__file__).parent.parent / "corpus"
slug, pattern = sys.argv[1], sys.argv[2]
width = int(sys.argv[3]) if len(sys.argv) > 3 else 900

text = (CORPUS / f"{slug}.txt").read_text(encoding="utf-8", errors="ignore")
text = text.replace("\r\n", "\n")
paras = re.split(r"\n\s*\n", text)
flowed = [" ".join(p.split()) for p in paras]

hits = 0
for i, p in enumerate(flowed):
    if re.search(pattern, p, re.I):
        hits += 1
        print(f"\n───── hit {hits}  [para {i}] ─────")
        print(p[:width])
        if hits >= 8:
            break
if not hits:
    print("no match")
