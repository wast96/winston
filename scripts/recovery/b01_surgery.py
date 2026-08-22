#!/usr/bin/env python3
# B01 (ch00 Preface PDF 36-38, ch01 PDF 45-59) paragraph-structure surgery on the
# re-assembled source, run AFTER assemble.py and BEFORE apply_fixes.py.
#
# B01 predates the recovery-script discipline: it had no strip/surgery script and
# no saved raw-OCR backup, so a fresh QC regen with a different tesseract build
# reproduces the CHARACTER stream closely (apply_fixes replays the char fixes) but
# not the exact BLANK-LINE paragraph structure. This script replays the
# paragraph-boundary repairs, anchor-based (robust to line shifts), so verify_unit
# parity is reproducible. It changes NO characters; those are apply_fixes's job.
#
# ch00: strip the running-head furniture ("前") and the trailing source citation
# ("@..."); fix the two OCR-misplaced breaks (one mid-sentence at "赢得了|中国
# 人民", one weld of the radio-work paragraph onto the "由于中共中央..." quote).
# Result: 6 body paragraphs, matching out/ch00_reading.md.
import os

ZH = "/home/user/winston/data/zh"
MARK = "4册中0①②③④⑤⑥忆>"


def load(u):
    return [l for l in open(os.path.join(ZH, u + ".txt")).read().split("\n")
            if l.strip() != ""]


def save(u, P):
    open(os.path.join(ZH, u + ".txt"), "w").write("\n".join(P) + "\n")


def find_end(P, suf, start=0):
    for i in range(start, len(P)):
        if P[i].startswith("###"):
            continue
        s = P[i]
        while s and s[-1] in MARK + " ":
            s = s[:-1]
        if s.endswith(suf):
            return i
    raise SystemExit("b01: suffix not found: " + suf)


def find_contains(P, sub, start=0):
    for i in range(start, len(P)):
        if sub in P[i]:
            return i
    raise SystemExit("b01: substr not found: " + sub)


def merge_after(P, suf):
    i = find_end(P, suf)
    j = i + 1
    nxt = P[j].lstrip("”’\" 　")
    P[i] = P[i] + nxt
    del P[j]


def split_at(P, sub, keep_with_first):
    i = find_contains(P, sub)
    k = P[i].index(keep_with_first) + len(keep_with_first)
    a, b = P[i][:k], P[i][k:]
    P[i] = a
    P.insert(i + 1, b)


# ---------------- ch00 (Preface) ----------------
P = load("ch00")
# Drop page furniture: the running-head fragment and the trailing source citation.
P = [l for l in P if l.strip() != "前" and not l.lstrip().startswith("@")]
# en1|en2: OCR broke the last sentence of para 1 mid-clause ("...赢得了 | 中国人民
# 和世界人民的爱戴和尊敬。周恩来作为..."). Rejoin, then split at the real boundary.
merge_after(P, "赢得了")
split_at(P, "世界人民的爱戴和尊敬。周恩来", "世界人民的爱戴和尊敬。")
# en4|en5: the radio-work paragraph is welded to the "由于中共中央..." quote block.
split_at(P, "同共产国际也通了报。“由于", "同共产国际也通了报。")
save("ch00", P)
print("b01 ch00: %d body paragraphs" % len(P))
