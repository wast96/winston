#!/usr/bin/env python3
# B14 (ch25 PDF 553-569, ch26 PDF 570-578, ch27 PDF 579-581) furniture strip,
# run on data/txt BEFORE assemble.  Follows the b13 model and adds:
#   * strip_folio: this batch's crop (bottom 0.95) intermittently caught the
#     printed folio at the page foot (S$10 / 和4l11 / S$12 / S$34); drop it.
#   * REMOVE_BETWEEN: the p561 Shen Bao clipping sits MID-page between the
#     colon-intro and the notice's printed headline; drop clipping + caption.
#
#   1. strip trailing folio garble.
#   2. figures: p561 mid-page clipping (REMOVE_BETWEEN), p568 foot manuscript
#      (TRUNCATE_AFTER).
#   3. peel foot-of-page author-citation blocks (line-based is_citation), foot
#      first; stripped citations -> data/b14_footnotes.txt for Author's-notes.
#   4. normalize garbled chapter/section headings to the EXACT book.json titles.
#
# NOT idempotent on the raw txt: restore from data/txt_backup_b14 before re-run.
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
    553: [(["与破灭"], "ch25"),
          (["伪造的《伍豪"], "ch25s01")],
    558: [(["临时中央为周恩来"], "ch25s02")],
    563: [(["斩断江青射出"], "ch25s03")],
    570: [(["结束语"], "ch26")],
    579: [(["后记"], "ch27")],
}

# Figure-caption blocks that OCR'd INTO the body.
#   TRUNCATE_AFTER: caption sits at page FOOT; keep through the anchor line,
#   drop the rest.
TRUNCATE_AFTER = {
    568: "将此事搁置起来不办",   # Zhou's handwritten report manuscript (fig ch25-2)
}
#   REMOVE_BETWEEN: figure sits MID-page.  Drop lines strictly between the line
#   containing `start` and the first later line that (stripped) EQUALS `end`.
# end is matched as a SUBSTRING; everything strictly between the start line and
# the first later line containing `end` is dropped (clipping + caption + the
# notice's redundant printed headline, since para11 already names the notice).
REMOVE_BETWEEN = {
    561: ("党内熟知的周恩来的别名", "效据周少山君"),  # Shen Bao clipping (fig ch25-1)
}

# --- folio peeler -----------------------------------------------------------
def is_folio(s):
    s = s.strip()
    if not s or len(s) > 6:
        return False
    han = len(re.findall(r"[一-鿿]", s))
    hasdig = bool(re.search(r"[0-9SsIl$]", s))
    return hasdig and han <= 1


def strip_folio(page):
    p = path(page)
    lines = open(p).read().split("\n")
    idxs = [i for i, l in enumerate(lines) if l.strip()]
    if idxs and is_folio(lines[idxs[-1]]):
        dropped = lines[idxs[-1]].strip()
        del lines[idxs[-1]]
        while lines and lines[-1].strip() == "":
            lines.pop()
        open(p, "w").write("\n".join(lines) + "\n")
        return dropped
    return None


# --- foot-citation peeler ---------------------------------------------------
BIB = re.compile(r"《|》|出版社|年版|谈话记录|第.{1,3}期|第.{1,4}辑|回忆录|"
                 r"文史资料|人民日报|党的文献|党史研究|党史资料|情报与外交|"
                 r"季米特洛|模糊的荧屏|秘密的岗位|李克农|中统特工秘录|纪念陈养山")
PAGEREF = re.compile(r"\d+\s*[~\-—]+\s*\d+|第\d+\s*页|\d+\s*页|页[。，\.]")
GLYPH = re.compile(r'^["\'”’@中外电也人OGD①-⑨]')
CONT = re.compile(r"^版社|^\d{4}年版|^\d+\s*[~\-—]\s*\d+\s*页|^版,第")


def is_citation(s):
    s = s.strip()
    if not s:
        return False
    if CONT.match(s):
        return True
    return bool(BIB.search(s)) and (bool(PAGEREF.search(s))
                                    or bool(GLYPH.match(s)) or "谈话记录" in s
                                    or "第" in s and "期" in s)


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


def remove_between(page, start, end):
    p = path(page)
    lines = open(p).read().split("\n")
    i = next((k for k, l in enumerate(lines) if start in l), None)
    if i is None:
        print("p%04d: REMOVE_BETWEEN start %r NOT FOUND" % (page, start))
        return
    j = next((k for k in range(i + 1, len(lines)) if end in lines[k]), None)
    if j is None:
        print("p%04d: REMOVE_BETWEEN end %r NOT FOUND" % (page, end))
        return
    dropped = j - i - 1
    lines = lines[:i + 1] + lines[j:]
    open(p, "w").write("\n".join(lines))
    print("p%04d: removed %d lines between clipping intro and %r"
          % (page, dropped, end))


if __name__ == "__main__":
    # folios first (they sit below everything, including foot citations)
    folios = []
    for pg in range(553, 582):
        d = strip_folio(pg)
        if d:
            folios.append("p%04d: %s" % (pg, d))
    print("stripped folios:", folios)
    # figures
    for pg, (s, e) in REMOVE_BETWEEN.items():
        remove_between(pg, s, e)
    for pg, anc in TRUNCATE_AFTER.items():
        truncate_after(pg, anc)
    # foot citations
    fn_log = []
    for pg in range(553, 582):
        for i, s in peel_footnotes(pg):
            fn_log.append("p%04d (printed %d) L%d: %s" % (pg, pg - 44, i, s))
    # headings
    for pg, specs in HEADING_FIX.items():
        fix_headings(pg, specs)
    with open(os.path.join(ROOT, "data", "b14_footnotes.txt"), "w") as fh:
        fh.write("\n".join(fn_log) + "\n")
    print("peeled %d foot-citation lines -> data/b14_footnotes.txt" % len(fn_log))
