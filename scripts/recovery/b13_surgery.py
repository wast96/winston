#!/usr/bin/env python3
# B13 (ch23 PDF 485-526, ch24 PDF 527-552) paragraph re-segmentation, run on
# data/zh/ch21.txt and ch22.txt AFTER assemble.  Robust variant of the b11
# model: each SECTION body is concatenated into one blob and split at a list of
# paragraph-START markers.  markers[i] opens paragraph i+1; N paragraphs need
# N-1 markers.
#
# Matching is done on a NORMALIZED view of the blob (systematic OCR name mangles
# de-mangled -- all same length -- then punctuation/space stripped), with an
# index map back to the raw blob, so markers can be written in CLEAN text and
# still land exactly on the raw paragraph start.  No sentence-end snap is used;
# the split is exactly at the mapped raw position, so mangled seams do not need
# restoring for segmentation.  apply_fixes runs AFTER this.
#
# NOT idempotent: re-assemble both units before re-running.
import os
import sys

ROOT = "/home/user/winston"
ZH = os.path.join(ROOT, "data", "zh")

# same-length de-mangle map (blob only, for MATCHING).  All entries preserve
# length so raw indices are unchanged.
DEMANGLE = {
    # Chen Geng 陈赓 (real 陈X kept: 陈云/陈立/陈果/陈康/陈连/陈寿/陈原/陈养)
    "陈庆": "陈赓", "陈广": "陈赓", "陈刻": "陈赓", "陈废": "陈赓", "陈记": "陈赓",
    "陈钴": "陈赓", "陈短": "陈赓", "陈笋": "陈赓", "陈乌": "陈赓", "陈鹿": "陈赓",
    "陈唐": "陈赓",
    # Liu Ding 刘鼎 (real 刘X kept: 刘杞夫/刘少/刘英/刘亚/刘伯/刘动/刘后)
    "刘易": "刘鼎", "刘瞻": "刘鼎", "刘里": "刘鼎", "刘蜀": "刘鼎", "刘哆": "刘鼎",
    "刘晶": "刘鼎", "刘刚": "刘鼎", "刘罗": "刘鼎", "刘弓": "刘鼎", "刘昂": "刘鼎",
    "刘时": "刘鼎",
    # Gu Shunzhang / Xu Enzeng / Jiang
    "磊顺章": "顾顺章", "显顺章": "顾顺章", "吴顺章": "顾顺章", "电顺章": "顾顺章",
    "顾咕章": "顾顺章", "顾顺音": "顾顺章", "顾顺更": "顾顺章",
    "徐思曾": "徐恩曾", "徐恩兽": "徐恩曾",
    "头介石": "蒋介石", "薪介石": "蒋介石", "范介石": "蒋介石",
    # Zhang Guotao 张国焘 (always mangled here; all refer to him)
    "张国帮": "张国焘", "张国琳": "张国焘", "张国春": "张国焘", "张国霖": "张国焘",
    "张国栋": "张国焘", "张国玫": "张国焘", "张国态": "张国焘", "张国总": "张国焘",
    # Chen Yangshan / Zhou Enlai / Li Yimang (same-length mangles; also in ocr_fixes)
    "陈养出": "陈养山", "周思来": "周恩来", "周册来": "周恩来",
    "李一让": "李一氓", "李一旋": "李一氓",
    "显丹章": "顾顺章", "顾硕章": "顾顺章", "徐轧曾": "徐恩曾", "徐乱曾": "徐恩曾",
}

STRIP = set("，,。、；;：:！!？?“”\"'‘’《》（）()〈〉…—-·　 \t\n[]{}｜|.9@")


def normalize(s):
    """De-mangle (same length) then strip punctuation, returning the stripped
    string plus a list mapping each kept char to its index in the ORIGINAL s."""
    # de-mangle: iterate, replacing 2/3-char keys (all same length)
    out = list(s)
    for wrong, right in DEMANGLE.items():
        w = len(wrong)
        i = 0
        joined = "".join(out)
        # replace all occurrences preserving length
        idx = joined.find(wrong)
        while idx != -1:
            for k in range(w):
                out[idx + k] = right[k]
            joined = "".join(out)
            idx = joined.find(wrong, idx + w)
    demangled = "".join(out)
    kept, idxmap = [], []
    for i, c in enumerate(demangled):
        if c in STRIP:
            continue
        kept.append(c)
        idxmap.append(i)
    return "".join(kept), idxmap


def norm_marker(m):
    return "".join(c for c in m if c not in STRIP)


def load(unit):
    return [l.rstrip("\n") for l in open(os.path.join(ZH, "%s.txt" % unit))]


def section_blobs(lines):
    """Return list of (heading, blob) preserving order; blob is concatenated
    body text (no headings)."""
    out = []
    name = None
    cur = []
    for l in lines:
        if l.startswith("###"):
            if name is not None:
                out.append((name, "".join(cur)))
            name = l
            cur = []
        elif l.strip():
            cur.append(l)
    if name is not None:
        out.append((name, "".join(cur)))
    return out


def split_blob(raw, markers, tag):
    norm, idxmap = normalize(raw)
    positions = []
    ok = True
    for m in markers:
        nm = norm_marker(m)
        c = norm.count(nm)
        if c != 1:
            print("  %s: MARKER %r found %d times (need 1)" % (tag, m, c))
            ok = False
            continue
        j = norm.find(nm)
        positions.append(idxmap[j])
    if not ok:
        return None
    if positions != sorted(positions):
        print("  %s: markers OUT OF ORDER: %s" % (tag, positions))
        return None
    pieces = []
    prev = 0
    for p in positions:
        pieces.append(raw[prev:p])
        prev = p
    pieces.append(raw[prev:])
    return pieces


# CONFIG[unit] = [ [markers for section 1], [markers for section 2] ]
CONFIG = {}
from b13_markers import CONFIG as _C  # noqa: E402
CONFIG = _C


def process(unit, apply):
    lines = load(unit)
    blobs = section_blobs(lines)
    seclists = CONFIG[unit]
    content = [(h, b) for (h, b) in blobs if b.strip()]
    if len(content) != len(seclists):
        print("  %s: %d content sections in file, %d in CONFIG"
              % (unit, len(content), len(seclists)))
        return False
    out = []
    ok = True
    ci = 0
    for heading, raw in blobs:
        out.append(heading)
        if not raw.strip():          # chapter-title heading, no body
            continue
        markers = seclists[ci]
        ci += 1
        pieces = split_blob(raw, markers, "%s/%s" % (unit, heading[4:]))
        if pieces is None:
            ok = False
            continue
        print("  %s/%s: %d paragraphs" % (unit, heading[4:], len(pieces)))
        out.extend(pieces)
    if ok and apply:
        with open(os.path.join(ZH, "%s.txt" % unit), "w") as fh:
            fh.write("\n".join(out) + "\n")
        body = [l for l in out if not l.startswith("###")]
        print("  %s WRITTEN: %d body paragraphs" % (unit, len(body)))
    return ok


if __name__ == "__main__":
    apply = "--apply" in sys.argv
    allok = True
    for unit in ("ch23", "ch24"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s." % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME SECTIONS FAILED -- re-assemble.")
