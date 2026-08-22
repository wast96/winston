#!/usr/bin/env python3
"""R5 reconciliation: collapse the 叛徒 rendering "renegade" -> "traitor".

The 叛徒 variety check (REVISION_PLAN.md section 3.2) found that "renegade"
(29 occurrences) is confined to ch21/ch22 (batch B12) and ch24, all rendering
the SAME source word 叛徒 that is rendered "traitor" everywhere else in the
book — and that ch21/ch22 use BOTH "traitor" and "renegade" for 叛徒 in the
same chapters. That is per-batch drift, not distinct-source variation.
STYLE.md sanctions "traitor" OR "turncoat" for 叛徒 but NOT "renegade", so
"turncoat" (an early-batch deliberate variant) is kept and only "renegade"
collapses to the primary rendering "traitor".

This is a GLOBAL rendering correction, so it is done grep-driven across all
affected built units (CLAUDE.md corrections workflow), not as per-site
edits/*.md blocks. It is anchor-safe: no notes.json anchor, and no glossary
or note body, contains "renegade" (verified before running).

Exception (REVISION_PLAN.md 3.2): "renegade" is kept where the SAME SENTENCE
already uses "traitor" (avoids "the traitor X ... the traitors' ranks"
repetition). One such site exists: ch21 "the renegade Chen Weiru, ... the
traitors' ranks."

Idempotent-ish: run once. Prints per-file replacement counts.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UNITS = ["ch21", "ch22", "ch24"]
# same-sentence-traitor exception: protect this exact span
PROTECT = "the renegade Chen Weiru"
SENTINEL = "\x00RENEGADE_KEEP\x00"

# longest-first so possessive/plural forms map correctly
SUBS = [
    ("renegades'", "traitors'"),
    ("renegade's", "traitor's"),
    ("Renegades", "Traitors"),
    ("Renegade", "Traitor"),
    ("renegades", "traitors"),
    ("renegade", "traitor"),
]


def main():
    total = 0
    for cid in UNITS:
        path = os.path.join(ROOT, "out", "%s_reading.md" % cid)
        text = open(path, encoding="utf-8").read()
        before = len(re.findall(r"[Rr]enegade", text))
        text = text.replace(PROTECT, SENTINEL)
        for old, new in SUBS:
            text = re.sub(r"\b%s\b" % re.escape(old), new, text)
        text = text.replace(SENTINEL, PROTECT)
        after = len(re.findall(r"[Rr]enegade", text))
        open(path, "w", encoding="utf-8").write(text)
        print("%s: %d 'renegade' -> 'traitor' (%d kept: same-sentence-traitor)"
              % (cid, before - after, after))
        total += before - after
    print("total collapsed: %d" % total)


if __name__ == "__main__":
    main()
