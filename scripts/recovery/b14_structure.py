#!/usr/bin/env python3
# Add data/structure.json rows for ch25/ch26/ch27 (chapter + all sections) with
# the EXACT title bytes from book.json and the PDF page each heading sits on.
# Idempotent: replaces any existing ch25*/ch26*/ch27* rows.
import json
import os

ROOT = "/home/user/winston"
book = json.load(open(os.path.join(ROOT, "book.json")))
S = os.path.join(ROOT, "data", "structure.json")
rows = json.load(open(S))

PREF = ("ch25", "ch26", "ch27")
rows = [r for r in rows if not r.get("id", "").startswith(PREF)]

new = []
for u in book["structure"]:
    if u["id"] in PREF:
        new.append({"id": u["id"], "pdf": u["pdf_page"], "title": u["title"]})
        for s in u.get("sections", []):
            new.append({"id": s["id"], "pdf": s["pdf_page"], "title": s["title"]})

allrows = rows + new
allrows.sort(key=lambda r: (r["pdf"], r["id"]))
json.dump(allrows, open(S, "w"), ensure_ascii=False, indent=1)
for r in new:
    print(r["id"], r["pdf"], r["title"])
print("wrote", len(new), "rows; total", len(allrows))
