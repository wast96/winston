#!/usr/bin/env python3
# Add data/structure.json rows for ch23/ch24 (chapter + all sections) with the
# EXACT title bytes from book.json and the PDF page each heading sits on.
# Idempotent: replaces any existing ch23*/ch24* rows.
import json
import os

ROOT = "/home/user/winston"
book = json.load(open(os.path.join(ROOT, "book.json")))
S = os.path.join(ROOT, "data", "structure.json")
rows = json.load(open(S))

# drop any existing ch23*/ch24* rows
rows = [r for r in rows if not (r.get("id", "").startswith("ch23")
                                or r.get("id", "").startswith("ch24"))]

new = []
for u in book["structure"]:
    if u["id"] in ("ch23", "ch24"):
        new.append({"id": u["id"], "pdf": u["pdf_page"], "title": u["title"]})
        for s in u["sections"]:
            new.append({"id": s["id"], "pdf": s["pdf_page"], "title": s["title"]})

# insert after the last ch22 row to keep reading order
out = []
inserted = False
for r in rows:
    out.append(r)
for r in rows:
    pass
# simplest: append and sort by pdf
allrows = rows + new
allrows.sort(key=lambda r: (r["pdf"], r["id"]))
json.dump(allrows, open(S, "w"), ensure_ascii=False, indent=1)
for r in new:
    print(r["id"], r["pdf"], r["title"])
print("wrote", len(new), "rows; total", len(allrows))
