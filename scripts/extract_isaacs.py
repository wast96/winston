#!/usr/bin/env python3
"""Extract ONE chapter of Isaacs verbatim from source.pdf.

This is an ANNOTATED EDITION, not a translation: the source is already English
and source.pdf has a clean born-digital text layer. Extraction is a FAITHFUL
RESET (CLAUDE.md rule 4 / STYLE.local.md) -- mechanical fixes only:

  - rejoin words split by a soft line-break hyphen, but KEEP real hyphens
    (anti-imperialist, Chiang Kai-shek). The decision uses the system word
    lists plus Isaacs's own whole-word vocabulary built from the whole PDF,
    so "pro-|ductivity" rejoins while "Hung-|chang" and "man-|drawn" do not;
  - fold the drop-cap initial back into its word;
  - strip running heads, folios, the chapter number/title, and the 8pt
    asterisk page-foot footnotes (captured separately);
  - drop the 5.5pt superscript reference digits and the asterisk marks from
    the prose (they become footnote anchors instead);
  - preserve paragraph breaks (one source paragraph per output line) and
    Isaacs's italics (as *...*).

Writes out/<id>_reading.md and data/pagemap/<id>.json, and prints a REVIEW
report: every de-hyphenation decision and the captured asterisk footnotes,
so a human can check the mechanical layer before it ships.

Usage: extract_isaacs.py <chid>            # writes files + report
       extract_isaacs.py <chid> --dry      # report only, writes nothing
"""
import json
import os
import re
import sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "source.pdf")
# printed = pdf_page(1-indexed) - offset. The offset is per unit and read from
# book.json (pdf_page - printed_page): 23 for the body, 1 for the roman front
# matter. NEVER hardcode it -- the front matter runs its own sequence.

BODY_LO, BODY_HI = 9.3, 10.4       # body text point size
DROP_MIN = 40.0                    # drop-cap initial
FOOT_LO, FOOT_HI = 7.6, 8.4        # asterisk page-foot footnote
QUOTE_LO, QUOTE_HI = 8.6, 9.2      # set-off block quotation (smaller type)
QUOTE_X0_LO, QUOTE_X0_HI = 63, 110  # block-quote left indent (body ~54-57;
#   running heads sit at x0 57 verso / 264+ recto, folios ~210 -- all excluded)


def load_words():
    words = set()
    for name in ("american-english", "british-english"):
        p = os.path.join("/usr/share/dict", name)
        if os.path.exists(p):
            for w in open(p, encoding="latin-1"):
                w = w.strip()
                if w.endswith("'s"):
                    w = w[:-2]
                words.add(w.lower())
    return words


def isaacs_vocab():
    """Count how often Isaacs writes each token CLOSED vs HYPHENATED across the
    whole PDF. A soft line-break fragment carries a trailing '-' (excluded from
    the hyphenated tally) and its continuation is a bare token, so neither
    pollutes the closed/hyphenated COUNTS for the specific word we later test.
    Counts, not sets, let the decision follow Isaacs's dominant usage: he
    writes 'to-day' 4x and never 'today', so a 'to-|day' break keeps the
    hyphen; he writes 'reform(s)' constantly and 're-form' once, so a
    're-|forms' break fuses."""
    from collections import Counter
    doc = pymupdf.open(PDF)
    closed, hyph = Counter(), Counter()
    for pg in doc:
        for w in pg.get_text("words"):
            core = w[4].strip().strip(".,;:!?()[]“”‘’\"'—–")
            if not core:
                continue
            if "-" in core and not core.endswith("-") and not core.startswith("-"):
                hyph[core.lower()] += 1
            elif core.replace("’", "'").replace("'", "").isalpha():
                closed[core.lower()] += 1
    doc.close()
    return closed, hyph


WORDS = load_words()
ISAACS_CLOSED, ISAACS_HYPH = isaacs_vocab()
REJOIN_LOG = []


def should_rejoin(left, right):
    """left ends the line before a hyphen (hyphen stripped); right begins the
    next line. Return True to fuse into one word (soft break), False to keep
    the hyphen (real compound / romanization). Decision order: proper-noun
    fragments keep the hyphen; then Isaacs's own dominant usage decides; then
    the system dictionary; else fuse (soft breaks dominate justified text)."""
    lclean = left.strip("“”‘’\"'([")
    rclean = right.strip(".,;:!?)]“”‘’\"'")
    combo = (lclean + rclean).lower()
    hyphenated = (lclean + "-" + rclean).lower()

    def log(joined, why):
        REJOIN_LOG.append((left, right, joined, why))
        return joined

    # 1. Capitalized fragment on either side -> romanization / proper noun
    #    (Chiang Kai-|shek, Li Hung-|chang, Tse-|hsu, Sian-|fu). Keep.
    if any(c.isupper() for c in lclean[1:]) or rclean[:1].isupper():
        return log(False, "keep: capitalized fragment (proper noun)")
    # 2. Isaacs has a documented preference: go with his dominant form.
    hc = ISAACS_HYPH.get(hyphenated, 0)
    cc = ISAACS_CLOSED.get(combo, 0)
    if hc or cc:
        if cc >= hc:
            return log(True, "rejoin: Isaacs closed=%d >= hyphen=%d" % (cc, hc))
        return log(False, "keep: Isaacs hyphen=%d > closed=%d" % (hc, cc))
    # 3. Isaacs silent: the system dictionary knows the fused word -> soft break.
    if combo in WORDS:
        return log(True, "rejoin: '%s' in dictionary" % combo)
    # 4. Nothing recognizes the fusion: soft breaks dominate -> fuse, but log
    #    loudly for review.
    return log(True, "rejoin: DEFAULT (review) '%s'" % combo)


def line_text(line):
    """Reconstruct a line's text, wrapping italic runs in *...*, dropping the
    superscript reference digits AND the inline asterisk footnote markers (both
    become footnote anchors). A dropped reference mark that sat between two
    words leaves a space in its place, or the words would fuse ('cannon's
    mouth' + ref + 'provided' must not become 'mouthprovided')."""
    out = []
    ital = False
    gap = False   # a reference/asterisk marker was just dropped
    for s in line["spans"]:
        # source asterisk footnote markers are full-size (flags 4) inline '*';
        # strip every literal source asterisk (we add our own italic '*'), and
        # note the gap so the surrounding words keep their space.
        t = s["text"].replace("*", "")
        if bool(s["flags"] & 1):        # superscript reference digit -> drop
            if s["text"].strip():
                gap = True
            continue
        if s["text"] != t:              # a literal asterisk was stripped
            gap = True
        is_ital = bool(s["flags"] & 2)
        if is_ital and not ital:
            out.append("*")
            ital = True
        elif not is_ital and ital:
            out.append("*")
            ital = False
        if gap and t[:1] and (t[0].isalnum() or t[0] in "([“‘\"'"):
            prev = "".join(out)
            if prev and not prev[-1].isspace():
                out.append(" ")
        gap = False
        out.append(t)
    if ital:
        out.append("*")
    return "".join(out)


def block_text(block):
    """Reconstruct a paragraph block: join its lines, de-hyphenating soft
    line-break hyphens and collapsing internal whitespace."""
    lines = [line_text(l) for l in block["lines"]]
    text = ""
    for i, ln in enumerate(lines):
        ln = ln.rstrip()
        if i == 0:
            text = ln
            continue
        if text.endswith("-"):
            # candidate soft hyphen: last token of text, first of ln
            m = re.search(r"(\S+)-$", text)
            nxt = ln.lstrip()
            n = re.match(r"(\S+)", nxt)
            if m and n and should_rejoin(m.group(1), n.group(1)):
                text = text[:-1] + nxt  # drop hyphen, fuse
            else:
                text = text + nxt       # keep hyphen
        else:
            text = text + " " + ln.lstrip()
    # collapse any doubled spaces introduced by span joins
    text = re.sub(r"[ \t]{2,}", " ", text).strip()
    # merge adjacent italic runs "*a**b*" -> "*a b*" never happens; but
    # "* *" empty italics can appear -> clean
    text = text.replace("**", "")
    return text


def dominant_size(block):
    szs = [round(s["size"], 1) for l in block["lines"] for s in l["spans"]
           if s["text"].strip()]
    if not szs:
        return 0.0
    return max(set(szs), key=szs.count)


def classify(block):
    sz = dominant_size(block)
    if sz >= DROP_MIN:
        return "drop"
    x0 = block["bbox"][0]
    # a set-off block quotation: smaller type AND indented from the body margin.
    # The geometry gate is what separates a 9.0pt quote (x0 ~68-71) from the
    # 9.0pt running heads (x0 57 / 264+) and folios (x0 ~210) at the same size.
    if QUOTE_LO <= sz <= QUOTE_HI and QUOTE_X0_LO <= x0 <= QUOTE_X0_HI:
        return "quote"
    if FOOT_LO <= sz <= FOOT_HI:
        return "foot"
    if BODY_LO <= sz <= BODY_HI:
        return "body"
    return "skip"


def main(chid, dry=False):
    book = json.load(open(os.path.join(ROOT, "book.json")))
    node = next(c for c in book["structure"] if c["id"] == chid)
    nodes = [c for c in book["structure"]]
    idx = nodes.index(node)
    pdf_start = node["pdf_page"]
    pdf_end = (nodes[idx + 1]["pdf_page"] - 1) if idx + 1 < len(nodes) \
        else book["pdf_end"]
    printed_start = node["printed_page"]
    offset = pdf_start - printed_start  # per-unit; 23 body, 1 front matter
    title_en = node["title_en"]

    doc = pymupdf.open(PDF)
    paragraphs = []          # paragraph text, in reading order
    para_start_page = []      # pdf page each paragraph STARTS on
    para_kind = []            # "body" or "quote" per paragraph
    foots = []                # captured asterisk footnotes (text)
    drop_letter = None

    # Collect body AND quote blocks across the whole unit in reading order
    # (top-to-bottom per page), so a set-off quotation stays in sequence with
    # the narrative it interrupts. Drop caps and page-foot footnotes are pulled
    # out here; everything else (running heads, folios, title) is skipped.
    flow = []   # (pnum, kind, block)
    for pnum in range(pdf_start, pdf_end + 1):
        page = doc[pnum - 1]
        blocks = [b for b in page.get_text("dict")["blocks"] if "lines" in b]
        blocks.sort(key=lambda b: b["bbox"][1])
        for b in blocks:
            kind = classify(b)
            if kind == "drop":
                # the drop-cap initial letter (opener only)
                letters = "".join(s["text"] for l in b["lines"]
                                  for s in l["spans"]).strip()
                if len(letters) == 1 and letters.isalpha():
                    drop_letter = letters
            elif kind == "foot":
                foots.append(block_text(b))
            elif kind in ("body", "quote"):
                flow.append((pnum, kind, b))

    # New-paragraph indent threshold is per kind: body first lines indent to
    # ~68 from a ~54-57 margin; a quote's own first lines indent to ~78 from
    # its ~68-71 margin. A flush (un-indented) first line at the top of a page
    # is a paragraph continuing across the page turn, of the same kind.
    NEW_PARA = {"body": 62, "quote": 75}
    # The body's normal line-to-line spacing. Used to tell a spurious mid-page
    # block split (a superscript reference mark at a line end breaking one
    # paragraph into two blocks) from a REAL new paragraph that happens to be
    # flush-left: a spurious split follows at the normal line rhythm, while a
    # real break carries extra leading (and a scene-break ornament, dropped
    # from the flow, widens the gap further). Indentation alone cannot tell
    # them apart -- both sit flush at the margin.
    body_gaps = []
    for _, k, bb in flow:
        if k != "body":
            continue
        ys = [l["bbox"][1] for l in bb["lines"]]
        body_gaps.extend(ys[i + 1] - ys[i] for i in range(len(ys) - 1))
    body_lh = sorted(body_gaps)[len(body_gaps) // 2] if body_gaps else 13.0
    GAP_FACTOR = 1.35        # <= this * body_lh apart -> same paragraph
    prev_page = None
    last_kind = None
    prev_last_y = None
    for pnum, kind, b in flow:
        first_line_x = round(b["lines"][0]["bbox"][0])
        indented = first_line_x >= NEW_PARA[kind]
        txt = block_text(b)
        if not txt:
            continue
        page_first = (pnum != prev_page)
        prev_page = pnum
        # A new paragraph's first line is INDENTED; a block whose first line is
        # flush to the margin is a CONTINUATION of the current same-kind
        # paragraph -- either a genuine cross-page turn (page first), or a
        # spurious mid-page block split. For the mid-page case, require the
        # block to follow at the normal line rhythm (no extra paragraph leading
        # and no dropped scene-break ornament in the gap).
        same_flow = (prev_last_y is not None
                     and b["lines"][0]["bbox"][1] - prev_last_y
                     <= body_lh * GAP_FACTOR)
        if (not indented and paragraphs and last_kind == kind
                and (page_first or same_flow)):
            # continuation of the previous same-kind paragraph
            prev = paragraphs[-1]
            if prev.endswith("-"):
                m = re.search(r"(\S+)-$", prev)
                n = re.match(r"(\S+)", txt)
                if m and n and should_rejoin(m.group(1), n.group(1)):
                    paragraphs[-1] = prev[:-1] + txt      # soft hyphen: fuse
                else:
                    paragraphs[-1] = prev + txt           # real hyphen: keep
            else:
                paragraphs[-1] = prev + " " + txt
        else:
            paragraphs.append(txt)
            para_start_page.append(pnum)
            para_kind.append(kind)
        last_kind = kind
        prev_last_y = b["lines"][-1]["bbox"][1]

    doc.close()

    # fold the drop-cap initial into the first paragraph
    if drop_letter and paragraphs:
        paragraphs[0] = drop_letter + paragraphs[0]

    # build the pagemap: first NEW paragraph index that starts on each folio
    pagemap = []
    seen_pages = {}
    for i, pg in enumerate(para_start_page):
        if pg not in seen_pages:
            seen_pages[pg] = i
    for pg in sorted(seen_pages):
        pagemap.append({"printed": pg - offset, "pdf": pg,
                        "body_paragraph": seen_pages[pg]})

    # ----- report -----
    nquote = sum(1 for k in para_kind if k == "quote")
    print("=== %s: %s ===" % (chid, title_en))
    print("pdf %d-%d  printed %d-%d  paragraphs=%d (body=%d, block-quote=%d)"
          % (pdf_start, pdf_end, printed_start, pdf_end - offset,
             len(paragraphs), len(paragraphs) - nquote, nquote))
    print("\n--- de-hyphenation decisions (%d) ---" % len(REJOIN_LOG))
    for left, right, joined, why in REJOIN_LOG:
        mark = "FUSE " if joined else "KEEP "
        print("  %s %-16s | %-16s  %s" % (mark, left[-16:], right[:16], why))
    print("\n--- asterisk page-foot footnotes (%d) ---" % len(foots))
    for f in foots:
        print("  * %s" % f)
    print("\n--- pagemap (%d folios) ---" % len(pagemap))
    print("  " + ", ".join("%d->p%d" % (e["printed"], e["body_paragraph"])
                           for e in pagemap))

    if dry:
        print("\n[dry run: nothing written]")
        return

    out_md = os.path.join(ROOT, "out", "%s_reading.md" % chid)
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write("## %s\n\n" % title_en)
        for p, k in zip(paragraphs, para_kind):
            prefix = "{q} " if k == "quote" else ""
            fh.write(prefix + p + "\n\n")
    pm_dir = os.path.join(ROOT, "data", "pagemap")
    os.makedirs(pm_dir, exist_ok=True)
    with open(os.path.join(pm_dir, "%s.json" % chid), "w", encoding="utf-8") as fh:
        json.dump(pagemap, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("\nwrote %s (%d paragraphs)" % (out_md, len(paragraphs)))
    print("wrote data/pagemap/%s.json (%d folios)" % (chid, len(pagemap)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], dry="--dry" in sys.argv)
