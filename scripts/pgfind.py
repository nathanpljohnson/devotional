"""Search the local Gutenberg catalog: python3 pgfind.py "author substr" "title substr" """
import csv, sys, pathlib

CAT = pathlib.Path(__file__).parent.parent / "data" / "pg_catalog.csv"
author_q = sys.argv[1].lower()
title_q = sys.argv[2].lower() if len(sys.argv) > 2 else ""

csv.field_size_limit(10_000_000)
with CAT.open(newline="", encoding="utf-8", errors="ignore") as f:
    for row in csv.DictReader(f):
        if row["Language"] != "en" or row["Type"] != "Text":
            continue
        a = (row["Authors"] or "").lower()
        t = (row["Title"] or "").lower()
        if author_q in a and title_q in t:
            print(f'{row["Text#"]:>6}  {row["Title"][:78]}')
            print(f'        {(row["Authors"] or "")[:78]}')
