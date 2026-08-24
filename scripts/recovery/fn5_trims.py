#!/usr/bin/env python3
"""Apply FN5 reconciliation trims: subjects whose full note sat later than
their first appearance get the identification moved to first appearance (done
in fn5_notes.json) and the later note trimmed to a cross-reference.
Matches by exact existing anchor; refuses if the anchor or expected old text
is not found (so a re-run or a changed note fails loudly instead of silently)."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = os.path.join(ROOT, "notes.json")
n = json.load(open(p, encoding="utf-8"))

RSQ = "&#8217;"

# (unit, anchor, substring that must be present in the OLD body, new body)
TRIMS = [
    ("ch17", "the Shanghai Shen Bao",
     "founded 1872",
     ("See the note on the <i>Shen Bao</i> at chapter&#160;10, its first "
      "appearance. Reproducing a hostile press notice was a common device of "
      "this book" + RSQ + "s author, letting the enemy" + RSQ + "s own record "
      "date and confirm an episode.")),
    ("ch18", "Study and work at 'Sun Yat-sen University' went on as usual",
     "founded in 1925",
     "Sun Yat-sen University in Moscow: see the note at chapter&#160;3, its first appearance."),
    ("ch19", "Zhang Guotao, Shen Zemin, and Chen Changhao to the Hubei-Henan-Anhui border",
     "second-largest Communist base",
     ("The Hubei-Henan-Anhui (E-Yu-Wan) Soviet: see the note at its first "
      "appearance, chapter&#160;15. Under Zhang Guotao" + RSQ + "s leadership its "
      "main force was driven out in 1932, as Mu Xin relates. Zhang Guotao is "
      "treated in the notes to chapters&#160;1 and 5.")),
]

changed = 0
for unit, anchor, must, newbody in TRIMS:
    lst = n.get(unit, [])
    hit = [e for e in lst if e["anchor"] == anchor]
    if not hit:
        sys.exit("anchor not found in %s: %r" % (unit, anchor))
    e = hit[0]
    if must not in e["note"]:
        sys.exit("expected old text %r not in %s note; aborting" % (must, unit))
    e["note"] = newbody
    changed += 1
    print("trimmed %s: %s" % (unit, anchor[:50]))

with open(p, "w", encoding="utf-8") as fh:
    json.dump(n, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("applied %d trims" % changed)
