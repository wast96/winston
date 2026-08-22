#!/usr/bin/env python3
# B14 (ch25 PDF 553-569, ch26 PDF 570-578, ch27 PDF 579-581) paragraph
# re-segmentation, run on data/zh/ch25.txt / ch26.txt / ch27.txt AFTER assemble.
# Robust variant of the b13 model: each SECTION body is concatenated into one
# blob and split at a list of paragraph-START markers.  markers[i] opens
# paragraph i+1; N paragraphs need N-1 markers.
#
# Markers here are written from the RAW OCR (garbles included), so no de-mangle
# is needed for matching (DEMANGLE is empty).  Matching normalizes only by
# stripping punctuation/space, with an index map back to the raw blob.
#
# NOT idempotent: re-assemble all units before re-running.
import os
import sys

ROOT = "/home/user/winston"
ZH = os.path.join(ROOT, "data", "zh")

# markers are raw OCR substrings, so no de-mangle needed
DEMANGLE = {}

STRIP = set("，,。、；;：:！!？?“”\"'‘’《》〈〉（）()…—-·　 \t\n[]{}｜|.9@$Q")


def normalize(s):
    out = list(s)
    for wrong, right in DEMANGLE.items():
        w = len(wrong)
        joined = "".join(out)
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


from b14_markers import CONFIG  # noqa: E402


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
        if not raw.strip():
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
    for unit in ("ch25", "ch26", "ch27"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s." % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME SECTIONS FAILED -- re-assemble.")
