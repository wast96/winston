#!/usr/bin/env python3
"""Assemble the AUTHOR-note batch for ch01: Isaacs's own 30 numbered endnotes
(bodies verbatim from the back matter, cleaned of line-break hyphenation and
italic-run splits) plus his 2 asterisk page-foot footnotes, each anchored to
the exact phrase it follows in out/ch01_reading.md. Author notes carry NO "ed"
flag, so the builder numbers them in the arabic stream by position.

Writes scratch/ch01_author_notes.json (a batch-apparatus file for
apparatus_merge.py). The orphan endnote 31 (no in-text mark; duplicates 29) is
NOT emitted here; it is handled as an editorial discrepancy note.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from dump_endnotes import endnotes  # noqa: E402

READING = os.path.join(ROOT, "out", "ch01_reading.md")

# anchor hint (plain apostrophes/quotes; resolved to the exact reading.md slice)
ANCHOR = {
    1: "capacity for self-renewal",
    2: "Chinese tea and silk",
    3: "at the cannon's mouth",
    4: "legalized the trade in opium",
    5: "shortage of cultivable land",
    6: "contraction of the internal market",
    7: "coinage came into use",
    8: "in the three subsequent decades",
    9: "back to Europe and the United States",
    10: "port merchants and mandarins",
    11: "in return for their benevolent support",
    12: "expropriation of petty landholders",
    13: "in the eyes of the subject Chinese",
    14: "the smuggling of opium",
    15: "collective sharing of landed property",
    16: "antagonized the influential classes",
    17: "the immediate interests of the foreigners",
    18: "control of the customs administration",
    19: "carrying out of the new agreement",
    20: "The industrialization of China had begun",
    21: "an uninterrupted growth",
    22: "the reformers were helpless",
    23: "one power after another",
    24: "Long Live the Imperial Dynasty",
    25: "driving the Court toward concessions",
    26: "of the present century",
    27: "underground revolutionary societies",
    28: '"popular" elections',
    29: "a chance to leap forward",
    30: "grew to 182 by 1927",
}

# Isaacs's two asterisk page-foot footnotes (author notes), verbatim.
ASTERISK = [
    ("238 piculs", "1 picul equals 133⅓ pounds."),
    ("emperor Hsuan Tung",
     "Otherwise known as Henry Pu Yi, destined to become Emperor Kang Teh "
     "of Japan’s puppet state, Manchukuo."),
]


def clean_body(body):
    body = re.sub(r"^\d+\.\s*", "", body)          # strip the leading number
    body = body.replace("-</i> <i>", "")           # fuse hyphenated italic split
    body = body.replace("</i> <i>", " ")           # merge adjacent italic runs
    body = re.sub(r"(\w)- (\w)", r"\1\2", body)     # fuse soft line-break hyphens
    body = body.replace("<i> ", "<i>").replace(" </i>", "</i>")
    body = re.sub(r"\s{2,}", " ", body).strip()
    return body


def norm(s):
    return (s.replace("’", "'").replace("‘", "'")
             .replace("“", '"').replace("”", '"'))


def resolve(raw, nraw, hint):
    h = norm(hint)
    i = nraw.find(h)
    if i < 0:
        sys.exit("anchor not found: %r" % hint)
    if nraw.find(h, i + 1) != -1:
        sys.exit("anchor NOT UNIQUE: %r" % hint)
    return raw[i:i + len(h)]


def main():
    raw = open(READING, encoding="utf-8").read()
    nraw = norm(raw)

    bodies = {}
    n = 0
    started = False
    for kind, txt in endnotes(1, 363, 365):
        if kind == "HEAD" and txt.strip().startswith("1. Seeds"):
            started = True
            continue
        if kind == "HEAD" and started and txt.strip().startswith("2."):
            break
        if kind == "NOTE" and started:
            m = re.match(r"\s*(\d+)\.", txt)
            if m:
                bodies[int(m.group(1))] = clean_body(txt)

    notes = []
    for num in range(1, 31):
        if num not in bodies:
            sys.exit("missing endnote body %d" % num)
        notes.append({"anchor": resolve(raw, nraw, ANCHOR[num]),
                      "note": bodies[num]})
    for hint, body in ASTERISK:
        notes.append({"anchor": resolve(raw, nraw, hint), "note": body})

    out = {"notes": {"ch01": notes}}
    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch01_author_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote %s (%d author notes)" % (path, len(notes)))
    print("orphan endnote 31 (no in-text mark):", bodies.get(31))


if __name__ == "__main__":
    main()
