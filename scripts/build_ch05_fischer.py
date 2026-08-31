#!/usr/bin/env python3
"""Gap-fix caught by the ch12 blind-critique loop (Batch 7): Louis Fischer, the
journalist Isaacs leans on for Borodin's private reasoning, is cited in the
AUTHOR notes throughout (ch03-ch14) but was never given an EDITORIAL
identification -- the prior handoffs listed him as "already placed" in error.
His first substantive appearance as a named source is in ch05 ("Louis Fischer,
for example, describes the sequel to March 20..."), so his editorial note
belongs there, at first appearance, not in ch12 where the loop surfaced him.
Placement PLUS vantage, minus the book/date the author citations already carry
(STYLE.local eyewitness rule).

Writes scratch/ch05_fischer_note.json for apparatus_merge.py.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOTE = {
    "anchor": "Louis Fischer, for example",
    "note": "Louis Fischer (1896&#8211;1970), an American journalist and Moscow "
    "correspondent, a sympathetic observer of the Soviet Union in these years "
    "(he broke with it only later). His close access to Soviet officials, "
    "Borodin among them, makes him Isaacs&#8217;s main source for Borodin&#8217;s "
    "private reasoning.",
    "ed": True,
}


def main():
    reading = open(os.path.join(ROOT, "out", "ch05_reading.md"),
                   encoding="utf-8").read()
    if reading.count(NOTE["anchor"]) != 1:
        sys.exit("ch05: anchor %r not unique" % NOTE["anchor"])
    batch = {"notes": {"ch05": [NOTE]}}
    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch05_fischer_note.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("ch05: 1 editorial note (Louis Fischer, first-appearance gap-fix)")
    print("wrote", path)


if __name__ == "__main__":
    main()
