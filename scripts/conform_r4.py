#!/usr/bin/env python3
"""R4 Tier A conformances that do NOT go through apply_edits.

Two jobs, each an exact-count guarded global replace (never a heredoc):

 1. Date format -> "Month D, YYYY" in the ch37 appendix:
    - out/ch37_reading.md   (the 11 day-first dates of Material Two)
    - out/ch37b_en.json     (the same paragraphs, English split)
    (ch37a has no day-first dates; Material One is untouched.)

 2. Authority rendering 吴淞口 "the Wusong bar" -> "the mouth of the Wusong
    River" in the en.json split of ch34/ch35 (the reading-text occurrences are
    conformed via apply_edits' TOUCH in edits/ch34_edits.md, edits/ch35_edits.md;
    this keeps out/<id>_en.json in lockstep).

Reading-text date normalization for ch37 is done here, not via apply_edits,
because seven of the eleven lines are byte-identical ("Died on 4 April 1933 at
Longhua Prison, Shanghai.") and apply_edits' TOUCH requires OLD to occur once.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (substring OLD, NEW, expected count) applied to BOTH the reading file and
# the en.json paragraphs of ch37.
DATE_PAIRS = [
    ("died on 10 January 1933 at the market",
     "died on January 10, 1933, at the market", 1),
    ("on 16 January 1933, while covering",
     "on January 16, 1933, while covering", 1),
    ("On 2 February 1933 she was murdered",
     "On February 2, 1933, she was murdered", 1),
    ("on 8 February 1933, shot in a struggle",
     "on February 8, 1933, shot in a struggle", 1),
    ("Died on 4 April 1933 at Longhua Prison, Shanghai.",
     "Died on April 4, 1933, at Longhua Prison, Shanghai.", 7),
]

WUSONG = ("the Wusong bar", "the mouth of the Wusong River")


def patch_text_file(path, pairs):
    txt = open(path, encoding="utf-8").read()
    for old, new, want in pairs:
        c = txt.count(old)
        if c != want:
            sys.exit("%s: %r occurs %dx (want %d)" % (path, old, c, want))
        txt = txt.replace(old, new)
    open(path, "w", encoding="utf-8").write(txt)
    print("patched %s" % os.path.relpath(path, ROOT))


def patch_json_list(path, pairs):
    data = json.load(open(path, encoding="utf-8"))
    if not isinstance(data, list):
        sys.exit("%s: expected a JSON list of paragraphs" % path)
    blob = "\n".join(data)
    for old, new, want in pairs:
        c = blob.count(old)
        if c != want:
            sys.exit("%s: %r occurs %dx (want %d)" % (path, old, c, want))
    data = [_apply(p, pairs) for p in data]
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("patched %s" % os.path.relpath(path, ROOT))


def _apply(s, pairs):
    for old, new, _ in pairs:
        s = s.replace(old, new)
    return s


def patch_wusong(path, want):
    data = json.load(open(path, encoding="utf-8"))
    c = sum(p.count(WUSONG[0]) for p in data)
    if c != want:
        sys.exit("%s: %r occurs %dx (want %d)" % (path, WUSONG[0], c, want))
    data = [p.replace(*WUSONG) for p in data]
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("patched %s (Wusong x%d)" % (os.path.relpath(path, ROOT), want))


def main():
    p = lambda *a: os.path.join(ROOT, *a)
    # 1. ch37 dates: reading + en.json (Material Two)
    patch_text_file(p("out", "ch37_reading.md"), DATE_PAIRS)
    patch_json_list(p("out", "ch37b_en.json"), DATE_PAIRS)
    # 2. Wusong bar in the en.json splits (reading done via apply_edits)
    patch_wusong(p("out", "ch34_en.json"), 2)
    patch_wusong(p("out", "ch35_en.json"), 2)
    print("conform_r4: done")


if __name__ == "__main__":
    main()
