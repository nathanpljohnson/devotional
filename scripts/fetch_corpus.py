"""Download public-domain source texts so every quote ships verbatim, not from memory."""
import json, time, subprocess, pathlib

CORPUS = pathlib.Path(__file__).parent.parent / "corpus"
CORPUS.mkdir(exist_ok=True)

PG = "https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"
CCEL = "https://ccel.org/ccel/s/schaff/{v}/cache/{v}.txt"
IA = "https://archive.org/stream/{id}/{id}_djvu.txt"

SOURCES = [
    # slug,                    kind,   ref,      label
    ("pascal_pensees",         "pg",   18269,    "Pascal, Pensées (Trotter tr.)"),
    ("mill_liberty",           "pg",   34901,    "Mill, On Liberty"),
    ("mill_repgov",            "pg",   5669,     "Mill, Considerations on Representative Government"),
    ("mill_utilitarianism",    "pg",   11224,    "Mill, Utilitarianism"),
    ("chesterton_orthodoxy",   "pg",   16769,    "Chesterton, Orthodoxy"),
    ("chesterton_heretics",    "pg",   470,      "Chesterton, Heretics"),
    ("chesterton_wrong",       "pg",   1717,     "Chesterton, What's Wrong with the World"),
    ("dostoevsky_karamazov",   "pg",   28054,    "Dostoevsky, The Brothers Karamazov (Garnett tr.)"),
    ("dostoevsky_crime",       "pg",   2554,     "Dostoevsky, Crime and Punishment (Garnett tr.)"),
    ("tolstoy_kingdom",        "pg",   43302,    "Tolstoy, The Kingdom of God Is Within You (Garnett tr.)"),
    ("machiavelli_prince",     "pg",   1232,     "Machiavelli, The Prince (Marriott tr.)"),
    ("more_utopia",            "pg",   2130,     "More, Utopia (Robinson tr.)"),
    ("tocqueville_dem1",       "pg",   815,      "Tocqueville, Democracy in America I (Reeve tr.)"),
    ("tocqueville_dem2",       "pg",   816,      "Tocqueville, Democracy in America II (Reeve tr.)"),
    ("burke_works3",           "pg",   15679,    "Burke, Works Vol. III (incl. Reflections)"),
    ("milton_paradise",        "pg",   26,       "Milton, Paradise Lost"),
    ("shakespeare_macbeth",    "pg",   1533,     "Shakespeare, Macbeth"),
    ("augustine_confessions",  "pg",   3296,     "Augustine, Confessions (Pusey tr.)"),
    ("augustine_cityofgod1",   "pg",   45304,    "Augustine, City of God I (Dods tr.)"),
    ("augustine_cityofgod2",   "pg",   45305,    "Augustine, City of God II (Dods tr.)"),
    ("emerson_essays1",        "pg",   2944,     "Emerson, Essays: First Series"),
    ("emerson_essays2",        "pg",   2945,     "Emerson, Essays: Second Series"),
    ("kierkegaard_sel",        "pg",   60333,    "Kierkegaard, Selections (Hollander tr., 1923)"),
    ("aquinas_summa_p1",       "pg",   17611,    "Aquinas, Summa Theologica I"),
    ("aquinas_summa_p2a",      "pg",   17897,    "Aquinas, Summa Theologica I-II"),
    ("aquinas_summa_p2b",      "pg",   18755,    "Aquinas, Summa Theologica II-II"),
    ("grotius_war",            "pg",   46564,    "Grotius, The Rights of War and Peace"),
    ("plutarch_lives",         "pg",   674,      "Plutarch, Lives (Dryden/Clough)"),
    ("aurelius_meditations",   "pg",   2680,     "Marcus Aurelius, Meditations (Long tr.)"),
    ("gregory_pastoral",       "ccel", "npnf212", "Gregory the Great, Book of Pastoral Rule (NPNF 2-12)"),
    ("chrysostom_priesthood",  "ccel", "npnf109", "Chrysostom, On the Priesthood (NPNF 1-09)"),
    ("bentham_morals",         "ia",   "anintroductiont00bentgoog",
     "Bentham, Introduction to the Principles of Morals and Legislation"),
]


def get(url):
    for a in range(4):
        try:
            r = subprocess.run(["curl", "-sSL", "--max-time", "120", url],
                               capture_output=True, text=True, check=True)
            if len(r.stdout) > 20000:
                return r.stdout
        except Exception:
            pass
        time.sleep(2 * (a + 1))
    return None


manifest = {}
for slug, kind, ref, label in SOURCES:
    dest = CORPUS / f"{slug}.txt"
    if dest.exists() and dest.stat().st_size > 20000:
        print(f"  cached  {slug}")
        manifest[slug] = {"label": label, "kind": kind, "ref": ref, "bytes": dest.stat().st_size}
        continue

    url = {"pg": PG.format(id=ref), "ccel": CCEL.format(v=ref), "ia": IA.format(id=ref)}[kind]
    text = get(url)
    if not text:
        print(f"  FAIL    {slug}  ({url})")
        continue
    dest.write_text(text, encoding="utf-8", errors="ignore")
    manifest[slug] = {"label": label, "kind": kind, "ref": ref, "bytes": len(text), "url": url}
    print(f"  ok      {slug:24} {len(text)//1024:6d}KB  {label[:50]}")
    time.sleep(0.5)

(CORPUS / "manifest.json").write_text(json.dumps(manifest, indent=1))
print(f"\n{len(manifest)}/{len(SOURCES)} texts -> {CORPUS}")
