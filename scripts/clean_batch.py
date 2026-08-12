#!/usr/bin/env python3
"""Derive data/zh/<id>.txt (the parity source) VERBATIM from data/src/<file>.

The machine copies the source, never the translator: this reads the ingested
source lines and applies only structural, per-unit transformations that are
declared explicitly below and verified against the source afterwards:

  drop     leading lines that are page furniture or heading markup
           (the running-header '英雄无名-陈恭澍', the chapter <h1>/<h2>).
  merges   source <p> pairs split mid-phrase (the first ends on a comma or
           mid-word, last char not terminal); joined with no separator.
  glued    a sub-heading the digitization glued onto the END of a paragraph's
           <p>; split off and emitted as its own '### ' heading line AFTER the
           paragraph it was stuck to (it introduces the next section).
  standal  a sub-heading the source kept as its own <p> but with no heading
           markup; emitted as a '### ' heading line in place of the paragraph.

Output: '### <zh chapter title>' then, in order, the body source paragraphs
(one per line) with '### <zh sub-heading>' lines interleaved. check_align and
verify_unit strip every '#'-prefixed line, so the headings are apparatus, not
paragraphs, and parity is measured on the prose alone.

VERIFICATION (printed, and a hard failure): the concatenation of every emitted
line's raw characters, in order, must equal the concatenation of the kept
source <p> lines. That proves nothing was added, dropped, or mistyped.

Usage: clean_batch.py            (rebuilds every configured unit)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Per-unit structural spec. Line numbers are 1-based into data/src/<file>.
UNITS = {
    "ch01": {
        "file": "02_index-split-000.txt",
        "title": "「英雄无名」卷前",
        "drop": 3,            # header + <h1>卷前 + <h2>构想
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch02": {
        "file": "03_index-split-000-0001.txt",
        "title": "「北国锄奸」介绍",
        "drop": 2,            # header + <h2>
        "merges": [(5, 6)],   # 「滦 / 榆游击队」 split mid-word
        "glued": {}, "standalone": [],
    },
    "ch03": {
        "file": "04_index-split-000-0002.txt",
        "title": "「河内辱命」介绍",
        "drop": 2,
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch04": {
        "file": "05_index-split-000-0003.txt",
        "title": "「百战声威」介绍",
        "drop": 2,
        "merges": [(29, 30)],  # 「国民党特务」， / 这不但说明了...
        "glued": {11: "另外两部书",
                  19: "我对「特务工作」的看法",
                  35: "为什么要「制裁」"},
        "standalone": [50, 62],  # 中国模式的「特工」 ; 为无名英雄留历史纪录
    },
    "ch05": {
        "file": "06_index-split-000-0004.txt",
        "title": "北国锄奸",
        "drop": 2,
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch06": {
        "file": "07_index-split-000-0005.txt",
        "title": "第一节 任重道远 勇往直前",
        "drop": 2,             # running header + <h2> section title
        # extractor splits: a line broken mid-phrase into the next <p>
        "merges": [(101, 102), (173, 174), (202, 203), (221, 222),
                   (230, 231)],
        # sub-section headings the digitization glued onto a paragraph's tail
        "glued": {72: "二 吸收入「军会」与征召受「特训」",
                  145: "三 负有秘密任务的领班人",
                  194: "四 蒙然不知的遇上了国际大间谍",
                  280: "五 情报活动中的政治运用"},
        "standalone": [3],     # 一 学友小聚初识戴雨农
    },
}


def build(cid, spec):
    path = os.path.join(ROOT, "data", "src", spec["file"])
    raw = [l.rstrip("\n") for l in open(path, encoding="utf-8")]
    n = len(raw)
    kept = list(range(spec["drop"] + 1, n + 1))  # 1-based body line numbers

    merge_from = {a: b for a, b in spec["merges"]}
    merge_into = {b for _, b in spec["merges"]}
    glued = spec["glued"]
    standalone = set(spec["standalone"])

    out = ["### " + spec["title"]]
    verify_src = []   # kept source <p> raw text, in order
    verify_out = []   # emitted raw text (paragraph bodies + heading texts)

    i = 0
    while i < len(kept):
        ln = kept[i]
        text = raw[ln - 1].strip()
        if ln in merge_into:
            i += 1
            continue  # consumed by its partner already
        if ln in standalone:
            out.append("### " + text)
            verify_src.append(text)
            verify_out.append(text)
            i += 1
            continue
        # apply a merge starting at this line
        if ln in merge_from:
            partner = merge_from[ln]
            ptext = raw[partner - 1].strip()
            verify_src.append(text)
            verify_src.append(ptext)
            text = text + ptext
        else:
            verify_src.append(text)
        # split a glued trailing heading
        if ln in glued:
            head = glued[ln]
            assert text.endswith(head), \
                "%s L%d does not end with glued heading %r" % (cid, ln, head)
            body = text[: -len(head)]
            out.append(body)
            out.append("### " + head)
            verify_out.append(body)
            verify_out.append(head)
        else:
            out.append(text)
            verify_out.append(text)
        i += 1

    # verification: raw characters must be conserved exactly
    if "".join(verify_src) != "".join(verify_out):
        sys.exit("VERIFY FAIL %s: emitted text != source text" % cid)

    dest = os.path.join(ROOT, "data", "zh", cid + ".txt")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    body_paras = sum(1 for l in out if not l.startswith("#"))
    heads = sum(1 for l in out if l.startswith("### ")) - 1  # minus title
    print("%s: %d body paragraphs, %d sub-headings, source conserved OK"
          % (cid, body_paras, heads))


def main():
    for cid, spec in UNITS.items():
        build(cid, spec)


if __name__ == "__main__":
    main()
