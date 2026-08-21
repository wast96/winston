#!/usr/bin/env python3
# B12 (ch21 PDF 429-457, ch22 PDF 458-484) paragraph re-segmentation, run on
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
    # 陈赓 Chen Geng, the pervasive mangle
    "陈刻": "陈赓", "陈庆": "陈赓", "陈广": "陈赓", "陈记": "陈赓", "陈钴": "陈赓",
    "陈废": "陈赓", "陈唐": "陈赓", "陈煞": "陈赓", "陈短": "陈赓",
    "陈委": "陈赓", "陈笋": "陈赓", "陈庚": "陈赓", "陈灿": "陈赓", "陈铸": "陈赓",
    "陈菠英": "陈藻英",  # 陈藻英 alias (NOT Chen Geng here)
    # 王根英 Wang Genying
    "王根灿": "王根英", "王根负": "王根英", "王根喘": "王根英", "王根关": "王根英",
    "王根类": "王根英",
    # misc mangles that fall inside chosen markers (all length-preserving)
    "木费": "木凳", "杨狂": "杨铨", "杨欠": "杨铨", "杨镍": "杨铨", "杨猴": "杨铨",
    "杨镁": "杨铨", "沈醇": "沈醉", "顾硕章": "顾顺章", "丘顺章": "顾顺章",
    "省护律师": "辩护律师", "陈藻更": "陈藻英", "爱国非犯": "爱国罪犯",
    "在政人的": "在敌人的", "会审公演": "会审公堂", "儿天": "几天", "尴欣": "尴尬",
    "搭记着": "搭讪着", "狭诈": "狡诈", "高怠": "高昂", "闻文仪": "邓文仪",
    "插呈": "卑鄙", "一同高度": "一向高度", "如般": "如磐", "张道沙": "张道藩",
    "查佛": "杏佛",
    # 蒋介石 mangles
    "将介石": "蒋介石", "葛介石": "蒋介石", "藉介石": "蒋介石", "攻介石": "蒋介石",
    "萝介石": "蒋介石", "薪介石": "蒋介石", "莉介石": "蒋介石",
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
from b12_markers import CONFIG as _C  # noqa: E402
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
    for unit in ("ch21", "ch22"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s." % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME SECTIONS FAILED -- re-assemble.")
