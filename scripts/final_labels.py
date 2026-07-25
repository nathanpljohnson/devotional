# -*- coding: utf-8 -*-
"""Swap day 9 for a work-appropriate plate, then apply hand-written wall labels.
Dates are left blank rather than guessed."""
import json, subprocess, pathlib, time
from fetch_art_commons import api, clean

ROOT = pathlib.Path(__file__).parent.parent
ART = json.loads((ROOT / "data" / "art.json").read_text())
UA = "devotional/1.0 (personal offline devotional reader)"

# ── swap day 9 ──
target = "File:Rembrandt, David and Uriah.jpg"
info = api({"action": "query", "titles": target, "prop": "imageinfo",
            "iiprop": "url|size|extmetadata", "iiurlwidth": 1200})
page = list(info["query"]["pages"].values())[0]
ii = page["imageinfo"][0]
em = ii.get("extmetadata", {})
dest = ROOT / "assets" / "art" / "day09.jpg"
for attempt in range(5):
    subprocess.run(["curl", "-sSL", "--max-time", "120", "-H", f"User-Agent: {UA}",
                    "-o", str(dest), ii["thumburl"]], capture_output=True)
    if dest.exists() and dest.stat().st_size > 20000:
        break
    time.sleep(6 * (attempt + 1))
subprocess.run(["sips", "-Z", "1100", "-s", "format", "jpeg", "-s", "formatOptions", "72",
                str(dest), "--out", str(dest)], capture_output=True)
ART["9"]["source"] = ii.get("descriptionurl")
ART["9"]["licence"] = clean(em.get("LicenseShortName", {}).get("value", "")) or "Public domain"
print(f"day 9 replaced -> {dest.stat().st_size//1024}KB  ({ART['9']['licence']})")

# ── hand-written labels ──
LABELS = {
 1:  ("Landscape with Moses and the Burning Bush", "Sébastien Bourdon"),
 2:  ("Moses and Aaron before Pharaoh: An Allegory of the Dinteville Family",
      "Master of the Dinteville Family"),
 3:  ("Gideon and the Angel", "Ferdinand Bol"),
 4:  ("Jeremiah Lamenting the Destruction of Jerusalem", "Rembrandt"),
 5:  ("Isaiah's Vision of the Destruction of Babylon", "Gustave Doré"),
 6:  ("Samuel, Saul and David", "Andalusian School"),
 7:  ("Samuel Anointing Saul", "François de Nomé"),
 8:  ("Moses with the Tables of the Law", "Guido Reni"),
 9:  ("David and Uriah", "Rembrandt"),
 10: ("Nathan Admonishing David", "Rembrandt"),
 11: ("The Idolatry of Solomon", "Adriaen van Stalbemt"),
 12: ("Rehoboam and Abijah, Sistine Chapel lunette", "Michelangelo"),
 13: ("Nebuchadnezzar", "William Blake"),
 14: ("The Fall of the Rebel Angels", "Pieter Bruegel the Elder"),
 15: ("Jethro Advising Moses", "Jan van Bronchorst"),
 16: ("The Sacrifice of Elijah before King Ahab", "Nicola Malinconico"),
 17: ("Nebuchadnezzar and Daniel", "Shigeru Aoki"),
 18: ("Esther before Ahasuerus", "Artemisia Gentileschi"),
 19: ("The Prophet Amos", "Gustave Doré"),
 20: ("Nehemiah Views the Ruins of Jerusalem's Walls", "Gustave Doré"),
 21: ("The Judgment of Solomon", "Nicolas Poussin"),
 22: ("Joshua Commanding the Sun to Stand Still", "Ilario Spolverini"),
 23: ("The Siege and Destruction of Jerusalem by the Romans", "David Roberts"),
 24: ("Achan Stoned to Death", "Gustave Doré"),
 25: ("Saul and David in the Cave of En-gedi", "Willem de Poorter"),
 26: ("David Meeting Abigail", "Giovanni Gioseffo dal Sole"),
 27: ("Joab Kills Abner", "Anonymous, Rijksmuseum"),
 28: ("Elisha Bringing the Blinded Syrian Army to the King", "Antonio Tempesta"),
 29: ("Allegory of Good Government", "Ambrogio Lorenzetti"),
 30: ("Cyrus Restores the Vessels of the Temple", "Gustave Doré"),
 31: ("Jeremiah Lifted out of the Cistern", "Jost Amman"),
 32: ("Shadrach, Meshach and Abednego in the Burning Fiery Furnace", "J. M. W. Turner"),
 33: ("Christ as the Man of Sorrows", "Albrecht Dürer"),
 34: ("Christ Washing the Feet of His Disciples", "Jacopo Tintoretto"),
 35: ("Christ before Pilate", "Mihály Munkácsy"),
}

for n, (title, artist) in LABELS.items():
    a = ART[str(n)]
    a["title"], a["artist"] = title, artist

(ROOT / "data" / "art.json").write_text(json.dumps(ART, ensure_ascii=False, indent=1))
blank = [n for n in LABELS if not ART[str(n)]["date"]]
print(f"\n35 labels applied. Days with no date on Commons (left blank): {blank}")
