#!/usr/bin/env python3
# B13 (ch23 PDF 485-526, ch24 PDF 527-552) furniture strip, run on data/txt
# BEFORE assemble.  Follows the b11/b12 model but replaces the per-page
# footnote-marker list with a robust LINE-BASED foot-citation peeler (this
# batch has ~26 foot citations, several glued to the last body line with no
# blank between, which the group-based b12 peeler could not reach).
#
#   1. Normalize garbled / mid-page section+chapter headings to the EXACT
#      book.json titles (byte-exact, incl. the fullwidth quotes in ch23s04).
#   2. Peel foot-of-page author-citation blocks: from each page's foot, drop
#      contiguous citation lines (bibliographic marker + page-ref / note-glyph).
#      The stripped citations are reproduced as "Author's note." on QUOTED
#      passages via notes.json; see data/b13_footnotes.txt.
#   3. Remove figure-caption blocks that OCR'd INTO the body (three plates:
#      Smedley p517 top, Rewi Alley p520 top, Zhou's Ruijin office p523 foot).
#
# NOT idempotent on the raw txt: restore from data/txt_backup_b13 before re-run.
import json
import os
import re

ROOT = "/home/user/winston"
TXT = os.path.join(ROOT, "data", "txt")

book = json.load(open(os.path.join(ROOT, "book.json")))
TITLE = {}


def _walk(nodes):
    for u in nodes:
        if "id" in u and "title" in u:
            TITLE[u["id"]] = u["title"]
        for s in u.get("sections", []):
            TITLE[s["id"]] = s["title"]


_walk(book["structure"])

# page -> [(clean tokens avoiding the garbled glyph, structure id)]
HEADING_FIX = {
    485: [(["撤退、转移"], "ch23"),
          (["特委会调整和特科改组"], "ch23s01")],
    489: [(["养山转移天津"], "ch23s02")],
    499: [(["到莫斯科深造"], "ch23s03")],
    502: [(["去中央苏区立新功"], "ch23s04")],
    512: [(["撤离一波三折"], "ch23s05")],
    522: [(["安抵红都瑞金"], "ch23s06")],
    527: [(["的可耻下场"], "ch24"),
          (["人人喊打的过街老鼠"], "ch24s01")],
    532: [(["变本加厉的出卖"], "ch24s02")],
    540: [(["献媚取宠的书"], "ch24s03")],
    546: [(["徐恩曾处决"], "ch24s04")],
}

# Figure-caption blocks that OCR'd INTO the body.
#   REMOVE_UNTIL: caption sits at page TOP; drop every line before the anchor
#   (the first BODY line).
REMOVE_UNTIL = {
    517: "了中国民权保障同盟",     # Agnes Smedley plate (fig ch23-1)
    520: "秘密会见东北抗日义勇军",  # Rewi Alley plate (fig ch23-2)
    543: "的中心里去",             # Gu's 2nd-Branch network diagram + caption (fig ch24-1)
}
#   TRUNCATE_AFTER: caption sits at page FOOT; keep through the anchor line,
#   drop the rest.
TRUNCATE_AFTER = {
    523: "忆述当时离沪的情形",      # Zhou's Ruijin office plate (fig ch23-3)
}

# --- foot-citation peeler ---------------------------------------------------
BIB = re.compile(r"《|》|出版社|年版|谈话记录|第.{1,3}期|第.{1,4}辑|回忆录|"
                 r"文史资料|人民日报|党的文献|纪念陈养山|中统特工秘录|中共党史")
PAGEREF = re.compile(r"\d+\s*[~\-—]+\s*\d+|第\d+\s*页|\d+\s*页|页[。，\.]")
GLYPH = re.compile(r'^["\'”’@中外电也OGD①-⑨]')
CONT = re.compile(r"^版社|^\d{4}年版|^\d+\s*[~\-—]\s*\d+\s*页|^版,第")


def is_citation(s):
    s = s.strip()
    if not s:
        return False
    if CONT.match(s):
        return True
    return bool(BIB.search(s)) and (bool(PAGEREF.search(s))
                                    or bool(GLYPH.match(s)) or "谈话记录" in s)


def path(page):
    return os.path.join(TXT, "p%04d.txt" % page)


def peel_footnotes(page):
    p = path(page)
    lines = open(p).read().split("\n")
    idxs = [i for i, l in enumerate(lines) if l.strip()]
    peeled = []
    j = len(idxs) - 1
    while j >= 0 and is_citation(lines[idxs[j]]):
        peeled.insert(0, (idxs[j], lines[idxs[j]].strip()))
        j -= 1
    if not peeled:
        return []
    keep_upto = idxs[j] if j >= 0 else -1
    new = lines[:keep_upto + 1]
    while new and new[-1].strip() == "":
        new.pop()
    open(p, "w").write("\n".join(new) + "\n")
    return peeled


def fix_headings(page, specs):
    p = path(page)
    lines = open(p).read().split("\n")
    for i, l in enumerate(lines):
        s = l.strip()
        for tokens, sid in specs:
            good = TITLE[sid]
            if len(s) > len(good) + 5:
                continue
            if s == good:
                continue
            if all(t in s for t in tokens):
                lines[i] = good
                print("p%04d: heading '%s' -> '%s'" % (page, s, good))
    open(p, "w").write("\n".join(lines))


def remove_until(page, anchor):
    p = path(page)
    lines = open(p).read().split("\n")
    idx = next((i for i, l in enumerate(lines) if anchor in l), None)
    if idx is None:
        print("p%04d: REMOVE_UNTIL anchor %r NOT FOUND" % (page, anchor))
        return
    open(p, "w").write("\n".join(lines[idx:]))
    print("p%04d: removed %d head lines before %r" % (page, idx, anchor))


def truncate_after(page, anchor):
    p = path(page)
    lines = open(p).read().split("\n")
    idx = next((i for i, l in enumerate(lines) if anchor in l), None)
    if idx is None:
        print("p%04d: TRUNCATE_AFTER anchor %r NOT FOUND" % (page, anchor))
        return
    open(p, "w").write("\n".join(lines[:idx + 1]) + "\n")
    print("p%04d: kept through %r, dropped %d tail lines"
          % (page, anchor, len(lines) - idx - 1))


if __name__ == "__main__":
    # figures first (before foot peel, so a foot caption is gone before peel)
    for pg, anc in REMOVE_UNTIL.items():
        remove_until(pg, anc)
    for pg, anc in TRUNCATE_AFTER.items():
        truncate_after(pg, anc)
    fn_log = []
    for pg in range(485, 553):
        for i, s in peel_footnotes(pg):
            fn_log.append("p%04d (printed %d) L%d: %s" % (pg, pg - 44, i, s))
    for pg, specs in HEADING_FIX.items():
        fix_headings(pg, specs)
    with open(os.path.join(ROOT, "data", "b13_footnotes.txt"), "w") as fh:
        fh.write("\n".join(fn_log) + "\n")
    print("peeled %d foot-citation lines -> data/b13_footnotes.txt" % len(fn_log))
