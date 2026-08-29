#!/usr/bin/env python3
"""Build the cumulative reading edition of a scanned-book translation.

Driven entirely by book.json (a dict with a "structure" list of chapters, each
with its sections). One XHTML per TRANSLATED chapter (a chapter is translated
when out/<id>_reading.md exists), all in one spine, one cumulative EPUB.

Every build ships a FULL table of contents covering ALL chapters and their
sections (the whole structure is known from book.json from day one): translated
chapters are linked (down to the section), untranslated ones are shown, visibly,
as "not yet translated". So the whole shape of the book is always on view, and
the reader can see what is done. The e-reader navigation is nested to section
level, so every section is a jump target.

Footnote numbering is CONTINUOUS across the translated chapters (notes.json is
keyed by chapter id). The builder REFUSES to build if any note anchor fails to
match its prose (a silent-skip builder once lost twelve notes on a real
project). Note anchors are inserted BEFORE the italic markup substitution, or
the substitution would eat them. The same refuse-don't-skip contract covers
figures: a figure spec whose 'before' anchor never matches fails the build.

Reading markdown per chapter uses: '## ' chapter title (h1), '### ' section
(h2, given the section's book.json id), '#### ' subsection (h3); every other
non-blank line is a paragraph, except for the set-off markers:

  ***    on its own line: a scene break, rendered as a centered asterism;
         not a body paragraph for pagination purposes.
  {v}    line prefix: a chapter-opening vignette -- italic, set off.
  {d}    line prefix: a dateline/place line -- centered small caps.
  {g}    line prefix: the source's own hour-note / gloss block.
  {p}    line prefix: verse -- one line per source line, no first-line indent.

A cover is emitted when book.json names a "cover_image" (copied byte-identical:
a cover is chrome, not a figure, so it is never greyscaled or re-encoded), or,
failing that, generated typographically when Pillow and a usable font are
present. Optional per-unit page maps (data/pagemap/<unit>.json) become EPUB 3
pagebreak markers plus a page-list nav, so printed folios are citable from the
reading edition.

Optional back matter (errata table, colophon) is rendered when back_matter.json
is present; translator's note text can be supplied via book.json's
"translator_note" field. See the template's data files for the shapes.

Usage: build_reading_epub.py [out/book.epub]
"""
import html
import json
import os
import re
import shutil
import sys
import uuid
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(ROOT, "data", "figs")
PNG = os.path.join(ROOT, "data", "png")
PAGEMAP = os.path.join(ROOT, "data", "pagemap")
BUILD = os.path.join(ROOT, "build")

# The source language tag used on lang= attributes for source-script spans
# (title page, glossary, colophon, errata). Set from book.json's
# "source_script" (e.g. "zh-Hant", "zh-Hans"); a hardcoded script tag on a
# simplified-character book (or vice versa) mislabels every span.
SRC_LANG = "zh"

# "translation" (default) or "annotated". An annotated edition reproduces an
# already-English source with an added apparatus, so the builder's chrome must
# not call it a translation ("English translation", "Not yet translated",
# "Notes are the translator's throughout"). Set from book.json "edition_kind".
EDITION = "translation"


def _annotated():
    return EDITION == "annotated"

CSS = """\
body { font-family: serif; line-height: 1.6; margin: 1em 1.2em; }
h1 { font-size: 1.5em; margin: 1.4em 0 0.6em; font-weight: normal; }
h2 { font-size: 1.15em; margin: 1.6em 0 0.6em; font-weight: normal; color: #333; }
h3 { font-size: 1.02em; margin: 1.4em 0 0.5em; font-weight: bold; color: #444; }
p { margin: 0 0 0.85em; text-indent: 1.4em; }
p.first, p.note { text-indent: 0; }
p.note { font-size: 0.92em; color: #444; }
p.brk { text-indent: 0; text-align: center; margin: 1.5em 0; color: #777; }
p.vignette { text-indent: 0; font-style: italic; color: #444; margin: 0 1.6em 0.85em; }
p.dateline { text-indent: 0; text-align: center; font-variant: small-caps; letter-spacing: 0.06em; margin: 1.2em 0 0.3em; }
p.hourgloss { text-indent: 0; font-size: 0.9em; color: #444; margin: 2.4em 0 0; padding-top: 0.9em; border-top: 1px solid #bbb; }
p.verse { text-indent: 0; font-style: italic; margin: 0.2em 2.2em 0.85em; }
figure { margin: 1.6em auto; text-align: center; page-break-inside: avoid; }
figure img { max-width: 70%; }
figcaption { font-size: 0.85em; color: #444; margin-top: 0.5em; }
dl.gloss dt { font-weight: bold; margin-top: 0.7em; }
dl.gloss dd { margin: 0 0 0 1.2em; }
a.noteref { text-decoration: none; }
a.noteref sup { font-size: 0.72em; color: #7a1f1f; padding-left: 1px; }
div.endnote { margin: 0 0 1.05em; }
div.endnote p { text-indent: 0; font-size: 0.94em; }
a.backref { text-decoration: none; font-weight: bold; color: #7a1f1f; }
p.castrow { text-indent: 0; margin: 0.55em 0; }
.tp { text-align: center; margin-top: 3em; }
.tp h1 { font-size: 1.7em; }
.tp p { text-indent: 0; }
.tp p.subtitle { font-style: italic; color: #555; margin-top: 0.2em; }
div.cover { text-align: center; margin: 0; padding: 0; }
div.cover img { max-width: 100%; height: auto; }
h3.notechap { margin-top: 2em; font-style: italic; font-weight: normal; }
ol.contents { list-style: none; padding-left: 0; }
ol.contents li { margin: 0.15em 0; }
ol.contents li.chap { margin-top: 0.9em; font-weight: bold; }
ol.contents ol { list-style: none; padding-left: 1.4em; }
ol.contents li.sec { font-weight: normal; }
ol.contents li.part { margin: 1.1em 0 0.3em; font-weight: bold; text-transform: uppercase; font-size: 0.95em; letter-spacing: 0.05em; color: #555; }
ol.contents li.sub { font-weight: normal; color: #555; font-size: 0.95em; }
span.pending { color: #999; font-style: italic; }
span.span { color: #888; font-size: 0.85em; }
ol.contents ol.secs { padding-left: 1.4em; }
nav#toc ol ol { list-style: none; padding-left: 1.3em; }
nav#toc ol ol li { font-size: 0.95em; }
table.errata { border-collapse: collapse; margin: 1.2em 0; font-size: 0.9em; }
table.errata th, table.errata td { border: 1px solid #bbb; padding: 0.25em 0.55em; text-align: left; vertical-align: top; }
table.errata th { background: #f0f0f0; font-weight: bold; }
table.errata td.hz { font-size: 1.05em; }
.colophon { text-align: center; margin-top: 2em; }
.colophon .notice { border: 2px solid #444; display: inline-block; padding: 0.4em 1.6em; margin: 1em 0; font-size: 1.3em; letter-spacing: 0.3em; }
.colophon p { text-indent: 0; }
"""

XHTML = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><meta charset="utf-8"/><title>%(title)s</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
%(body)s
</body></html>
"""

MAX_FIG_WIDTH = 1100

# Declared media type follows the file EXTENSION for every image, cover and
# figure alike: a JPEG declared as image/png is an epubcheck error, and a
# builder that hardcoded image/png once shipped exactly that.
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".png": "image/png", ".gif": "image/gif"}


def mime_of(filename):
    return MIME.get(os.path.splitext(filename)[1].lower(), "image/png")


# Fonts for the generated fallback cover (present on most Linux boxes;
# make_cover degrades to no-cover when they are missing).
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
CJK_FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"


def make_cover(dest, title_en, title_zh, author_en, author_zh,
               tagline="Annotated English Translation"):
    """Generate a simple, clean typographic cover (1600x2560, Kindle/Books
    friendly ratio). Returns True on success, False if PIL or the fonts are
    unavailable -- the build then simply ships without a cover."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False
    if not (os.path.exists(SERIF) and os.path.exists(SERIF_BOLD)):
        return False
    W, H = 1600, 2560
    bg, ink, gold = (18, 22, 30), (238, 234, 226), (176, 141, 87)
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    def font(path, size):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            return ImageFont.truetype(SERIF, size)

    def wrap(text, fnt, max_w):
        words, lines, cur = text.split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=fnt) <= max_w:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def centered(lines, fnt, y, fill, gap):
        for ln in lines:
            w = d.textlength(ln, font=fnt)
            d.text(((W - w) / 2, y), ln, font=fnt, fill=fill)
            y += fnt.size + gap
        return y

    margin = 150
    d.rectangle([margin, 210, W - margin, 216], fill=gold)
    if title_zh:
        centered([title_zh], font(CJK_FONT, 120), 330, ink, 0)
    y = 720
    y = centered(wrap(title_en, font(SERIF_BOLD, 128), W - 2 * margin),
                 font(SERIF_BOLD, 128), y, ink, 24)
    d.rectangle([W / 2 - 120, y + 60, W / 2 + 120, y + 64], fill=gold)
    by = H - 640
    centered([author_en], font(SERIF, 74), by, ink, 0)
    if author_zh:
        centered([author_zh], font(CJK_FONT, 60), by + 96, ink, 0)
    centered([tagline], font(SERIF, 52), H - 360,
             gold, 0)
    d.rectangle([margin, H - 216, W - margin, H - 210], fill=gold)
    img.save(dest, format="PNG", optimize=True)
    return True


def shrink_image(src, dest):
    """Downsample an interior FIGURE for the reading edition (covers never come
    through here -- a cover is chrome and is copied byte-identical). Saves in
    the format the destination's extension declares, so the manifest media
    type stays truthful. Returns False (caller copies verbatim) when Pillow is
    missing or the format is one we do not re-encode."""
    try:
        from PIL import Image
    except ImportError:
        return False
    ext = os.path.splitext(dest)[1].lower()
    fmt = {".png": "PNG", ".jpg": "JPEG", ".jpeg": "JPEG"}.get(ext)
    if not fmt:
        return False
    img = Image.open(src)
    if img.width > MAX_FIG_WIDTH:
        h = int(img.height * MAX_FIG_WIDTH / img.width)
        img = img.resize((MAX_FIG_WIDTH, h), Image.LANCZOS)
    img.convert("L").save(dest, format=fmt, optimize=True)
    return True


def esc(text):
    return html.escape(text, quote=False)


def load_json(name, default):
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        return default
    return json.load(open(path))


def insert_notes(paragraph, notes, counter, doc):
    """Attach a superscript reference after each note's anchor phrase.

    Candidates are ordered by where their reference will actually LAND -- the
    end of the anchor, not its start. Sorting by start position looks right
    until one anchor contains another: the containing anchor starts first but
    ends last, so its marker renders after the shorter one's and the numbering
    runs backwards. Sorting by end position makes the numbers follow the
    reader's eye in every case; the counter is monotonic, so numbers ascend
    across the whole spine (qa_epub re-checks this from the built files).

    Matching happens on the escaped text BEFORE markup substitution (the
    substitutions would otherwise eat the anchors).
    """
    hits = []
    for note in notes:
        if note.get("used"):
            continue
        pos = paragraph.find(note["anchor"])
        if pos >= 0:
            hits.append((pos + len(note["anchor"]), note))
    for _, note in sorted(hits, key=lambda h: h[0]):
        counter[0] += 1
        note["n"] = counter[0]
        note["used"] = True
        note["doc"] = doc
        ref = ('<a class="noteref" epub:type="noteref" id="ref%d" '
               'href="notes.xhtml#note%d"><sup>%d</sup></a>'
               % (note["n"], note["n"], note["n"]))
        # The marker follows any closing punctuation right after the anchor
        # (convention: superscript after the period/comma/quote), but an
        # apostrophe followed by a letter is a possessive, not punctuation.
        pos = paragraph.find(note["anchor"])
        j = pos + len(note["anchor"])
        while j < len(paragraph) and paragraph[j] in ".,;:!?)…”’]\"'":
            if paragraph[j] in "’'" and j + 1 < len(paragraph) \
               and paragraph[j + 1].isalpha():
                break
            j += 1
        paragraph = paragraph[:j] + ref + paragraph[j:]
    return paragraph


# ---------------------------------------------------------------------------
# Typography: a display-layer pass applied at write() time to every XHTML body
# and title. Straight quotes become curly, '...' becomes an ellipsis. The
# split keeps tags and character references intact so attributes and entities
# are never touched, and quote state resets at block boundaries so an unpaired
# quote in one paragraph cannot flip every quote after it.
# ---------------------------------------------------------------------------

_OPENERS = " \t\n([{—–/‘“"  # after these, a quote opens


def _curl_text(text, prev):
    """Typographic pass on ONE text node: straight quotes/apostrophes to curly,
    '...' to an ellipsis. `prev` is the last text character emitted before this
    node (tags skipped), so quotes just after markup still resolve correctly.
    Already-curly text passes through unchanged (idempotent)."""
    out = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        if c == '"':
            out.append("“" if (not prev or prev in _OPENERS) else "”")
        elif c == "'":
            if prev.isalnum() and (nxt.isalnum()):
                out.append("’")          # contraction / possessive
            elif nxt.isdigit():
                out.append("’")          # '30s
            elif not prev or prev in _OPENERS or prev == '"' or prev == "“":
                out.append("‘")
            else:
                out.append("’")          # closing quote or s' possessive
        elif c == "." and text[i:i + 3] == "...":
            out.append("…")
            prev = "…"
            i += 3
            continue
        else:
            out.append(c)
        prev = out[-1]
        i += 1
    return "".join(out), prev


_TAG_SPLIT = re.compile(r"(<[^>]+>|&#?\w+;)")


def typographize(markup):
    """Apply _curl_text to the text nodes of an XHTML fragment, skipping tags
    and character references so attributes/entities are never touched."""
    prev = ""
    parts = []
    block = re.compile(r"</?(p|h\d|li|figcaption|div|blockquote|dt|dd|br|ol|ul)\b")
    for seg in _TAG_SPLIT.split(markup):
        if seg.startswith("<") or seg.startswith("&"):
            if block.match(seg):
                prev = ""
            parts.append(seg)
        else:
            seg, prev = _curl_text(seg, prev)
            parts.append(seg)
    return "".join(parts)


# ---------------------------------------------------------------------------
# Structure helpers: flatten the book to an ordered list of openers, compute
# each unit's page span, and group chapters by optional "part". Used by both the
# builder (skeleton pages, contents, nav) and scripts/survey.py.
# ---------------------------------------------------------------------------

def iter_openers(structure):
    """Yield (node, level, chapter) for every chapter/section/subsection in
    reading order. level: 1 chapter, 2 section, 3 subsection."""
    for chap in structure:
        yield chap, 1, chap
        for sec in chap.get("sections", []):
            yield sec, 2, chap
            for sub in sec.get("subsections", []):
                yield sub, 3, chap


def compute_spans(structure, book=None):
    """Annotate every node with _pdf=(start,end), _pp=(start,end) printed, and
    _pages, using the next opener at the same-or-higher level as the end. The
    last unit's end comes from book['pdf_end']/'printed_end' if given, else is
    left open (_pages None). Safe to call more than once."""
    book = book or {}
    nodes = list(iter_openers(structure))
    n = len(nodes)
    for i, (node, level, _chap) in enumerate(nodes):
        start = node.get("pdf_page")
        end = None
        for j in range(i + 1, n):
            if nodes[j][1] <= level:
                nxt = nodes[j][0].get("pdf_page")
                if nxt is not None:
                    end = nxt - 1
                break
        else:
            end = book.get("pdf_end")
        node["_pdf"] = (start, end)
        pstart = node.get("printed_page")
        pend = None
        if end is not None and start is not None and pstart is not None:
            pend = pstart + (end - start)
        node["_pp"] = (pstart, pend)
        node["_pages"] = (end - start + 1) if (start is not None
                                               and end is not None) else None
    return structure


def span_label(node):
    """A short 'pp. a-b (N pp.)' label, printed folios if known, else PDF."""
    ps, pe = node.get("_pp", (None, None))
    if ps is not None and pe is not None:
        pp = "%s" % ps if ps == pe else "%s&#8211;%s" % (ps, pe)
    else:
        a, b = node.get("_pdf", (None, None))
        if a is None:
            return ""
        pp = "PDF %s" % a if b is None else "PDF %s&#8211;%s" % (a, b)
    n = node.get("_pages")
    return "%s%s" % (pp, "" if not n else "&#160;(%d&#160;pp.)" % n)


def part_groups(structure):
    """Group chapters by their optional 'part' field, preserving order.
    Returns [(part_label_or_None, [chapters])]."""
    groups, cur, label = [], [], object()
    for chap in structure:
        p = chap.get("part")
        if p != label:
            if cur:
                groups.append((label if label is not object() else None, cur))
            cur, label = [], p
        cur.append(chap)
    if cur:
        groups.append((label if label is not object() else None, cur))
    return groups


def render_skeleton(chap):
    """A placeholder page for a chapter not yet translated: its title, source
    page span, and its full section/subsection outline with real anchors, so the
    table of contents can link all the way down before any translation exists.
    Returns (body, ids_emitted)."""
    ids = set()
    out = ['<h1>%s</h1>' % esc(chap["title_en"])]
    sl = span_label(chap)
    pending = "Not yet prepared." if _annotated() else "Not yet translated."
    out.append('<p class="note"><span class="pending">%s</span>'
               '%s</p>' % (pending, " Source&#160;" + sl if sl else ""))
    for sec in chap.get("sections", []):
        ids.add(sec["id"])
        out.append('<h2 id="%s">%s</h2>' % (esc(sec["id"]), esc(sec["title_en"])))
        ssl = span_label(sec)
        if ssl:
            out.append('<p class="note">Source&#160;%s</p>' % ssl)
        for sub in sec.get("subsections", []):
            ids.add(sub["id"])
            out.append('<h3 id="%s">%s</h3>'
                       % (esc(sub["id"]), esc(sub["title_en"])))
    return "\n".join(out), ids


def load_pagemap(unit):
    """Optional per-unit map of printed folios to body-paragraph boundaries:
    data/pagemap/<unit>.json is a list of {printed, pdf, body_paragraph}
    entries. Returns {body_paragraph_index: printed_folio}; {} when absent (no
    pagemap files means no pagebreak markers and no page-list, and qa_epub's
    pagination gate passes trivially at 0 == 0)."""
    p = os.path.join(PAGEMAP, "%s.json" % unit)
    if not os.path.exists(p):
        return {}
    return {e["body_paragraph"]: e["printed"] for e in json.load(open(p))}


def render_body(md_path, section_ids, sub_ids, figures, notes, counter, doc,
                ids=None, pagemap=None, unit=None, page_index=None):
    """Render one chapter's reading markdown to XHTML.

    section_ids / sub_ids are the chapter's book.json section and subsection ids,
    consumed in order as '### ' and '#### ' headings are met, so the contents
    page can deep-link each section and subsection. Either list may be empty,
    in which case the matching heading gets no id (linked at the coarser level).

    pagemap maps body-paragraph indices to printed folios; where present, an
    EPUB 3 pagebreak marker is emitted before that paragraph and recorded in
    page_index for the page-list nav. Body paragraphs are every rendered
    paragraph line, set-off ({v}/{d}/{g}/{p}) lines included; headings and the
    '***' scene break are not paragraphs and are not counted.
    """
    out, first = [], True
    ids = ids if ids is not None else set()
    sids, ssids = list(section_ids), list(sub_ids)
    pagemap = pagemap or {}
    body_n = 0
    for raw in open(md_path):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#### "):
            subid = ssids.pop(0) if ssids else None
            idattr = ' id="%s"' % esc(subid) if subid else ""
            if subid:
                ids.add(subid)
            out.append("<h3%s>%s</h3>"
                       % (idattr,
                          insert_notes(esc(line[5:]), notes, counter, doc)))
            first = True
            continue
        if line.startswith("### "):
            sid = sids.pop(0) if sids else None
            idattr = ' id="%s"' % esc(sid) if sid else ""
            if sid:
                ids.add(sid)
            out.append("<h2%s>%s</h2>"
                       % (idattr, insert_notes(esc(line[4:]), notes, counter, doc)))
            first = True
            continue
        if line.startswith("## "):
            out.append("<h1>%s</h1>" % esc(line[3:]))
            first = True
            continue
        if line.startswith("# "):
            continue
        if line == "***":
            out.append('<p class="brk">*&#160;*&#160;*</p>')
            first = True
            continue
        special = None
        m = re.match(r"^\{([vdgp])\} ", line)
        if m:
            special = {"v": "vignette", "d": "dateline",
                       "g": "hourgloss", "p": "verse"}[m.group(1)]
            line = line[4:]
        for fig in figures:
            if not fig.get("placed") and fig["before"] in line[:80]:
                out.append(
                    '<figure><img src="images/%s" alt="%s"/>'
                    "<figcaption>%s</figcaption></figure>"
                    % (fig["file"], esc(fig.get("alt", "")),
                       esc(fig["caption"])))
                fig["placed"] = True
        # PAGE-BREAK MARKER, before the paragraph the printed page opens on.
        # epub:type="pagebreak" is the EPUB 3 mechanism for citable print
        # pagination: it renders as nothing, and reading systems expose the
        # label as the page the reader is on. The marker cannot be exact -- a
        # printed page nearly always turns mid-sentence and English will not
        # break where the source did -- so it sits at the paragraph boundary
        # at or after the turn.
        if body_n in pagemap:
            n = pagemap[body_n]
            pid = "pg-%s-%s" % (unit, n)
            out.append('<span epub:type="pagebreak" role="doc-pagebreak" '
                       'id="%s" aria-label="%s"></span>' % (pid, n))
            if page_index is not None:
                page_index.append((doc, pid, n, unit))
        body_n += 1
        # notes first: the italic substitution below would otherwise eat any
        # anchor phrase containing the markup
        text = insert_notes(esc(line), notes, counter, doc)
        text = re.sub(r"\*([^*\n]+)\*", r"<i>\1</i>", text)
        if special:
            out.append('<p class="%s">%s</p>' % (special, text))
            first = True
            continue
        cls = ' class="first"' if first else ""
        out.append("<p%s>%s</p>" % (cls, text))
        first = False
    return "\n".join(out), ids


def render_notes_page(chapters, notes_by_chap):
    if _annotated():
        headnote = ('Each number links back to its place in the text. Notes '
                    'marked <i>Ed.</i> are editorial, added in this edition; '
                    'every other note is the author\'s own.')
    else:
        headnote = ('Each number links back to its place in the text. Notes '
                    'are the translator\'s throughout; the source book carries '
                    'none of its own.')
    parts = ['<h1>Notes</h1>', '<p class="note">%s</p>' % headnote]
    any_used = False
    for chap in chapters:
        used = sorted([n for n in notes_by_chap.get(chap["id"], [])
                       if n.get("used")], key=lambda x: x["n"])
        if not used:
            continue
        any_used = True
        parts.append('<h3 class="notechap">%s</h3>' % esc(chap["title_en"]))
        for note in used:
            parts.append(
                '<aside class="endnote" id="note%d" epub:type="footnote">'
                '<p><a class="backref" href="%s#ref%d">%d.</a> %s</p></aside>'
                % (note["n"], note["doc"], note["n"], note["n"], note["note"]))
    if not any_used:
        parts.append("<p>No notes yet.</p>")
    return "\n".join(parts)


def _span_suffix(node):
    sl = span_label(node)
    return ' <span class="span">%s</span>' % sl if sl else ""


def render_contents(structure, translated, ids_present=None):
    """The visible full map: every part, chapter, section and subsection, each
    linked to its place (real content when translated, a skeleton outline page
    otherwise). Because every chapter always has a page, every chapter entry
    resolves -- the whole contents is hyperlinked from the first (survey) build
    onward.

    Page spans are shown ONLY on pending units (a finished unit's span is
    workshop scaffolding, not reader information), and once every unit is
    translated the pending-explainer paragraph and the spans drop away
    entirely, leaving a clean finished contents page.

    ids_present maps a chapter id to the set of section/subsection anchor ids
    actually emitted in that chapter's page, so a chapter translated a batch at a
    time links only its finished sections and shows the rest as pending text
    (never a link to an anchor that does not exist, which qa_epub rejects)."""
    ids_present = ids_present or {}
    all_done = all(c["id"] in translated for c in structure)
    n_ch = len(structure)
    n_sec = sum(len(c.get("sections", [])) for c in structure)
    n_sub = sum(len(s.get("subsections", [])) for c in structure
                for s in c.get("sections", []))
    groups = part_groups(structure)
    n_parts = sum(1 for lbl, _ in groups if lbl)
    tally = ("%s%d chapters, %d sections"
             % ("%d parts, " % n_parts if n_parts else "", n_ch, n_sec)
             + (", %d subsections" % n_sub if n_sub else ""))
    parts = ['<h1>Contents</h1>']
    if not all_done:
        parts.append(
             '<p class="note">The complete book: %s. Every entry links to its '
             'place; units not yet translated link to a skeleton outline showing '
             'their source page span, so the whole shape of the book is '
             'navigable from the start.</p>' % tally)
    parts.append('<ol class="contents">')
    for part_label, chaps in groups:
        if part_label:
            parts.append('<li class="part">%s</li>' % esc(part_label))
        for chap in chaps:
            cid = chap["id"]
            here = ids_present.get(cid, set())
            done = cid in translated
            mark = "" if done else ' <span class="pending">&#183; pending</span>'
            # A nested list must live INSIDE its parent <li>: an <ol> that
            # is a direct child of an <ol> is invalid XHTML, and epubcheck
            # rejected two shipped books' contents pages for exactly this.
            parts.append('<li class="chap"><a href="%s.xhtml">%s</a>%s%s'
                         % (cid, esc(chap["title_en"]),
                            "" if done else _span_suffix(chap), mark))
            if chap.get("sections"):
                parts.append('<ol>')
                for sec in chap["sections"]:
                    if sec["id"] in here:
                        label = ('<a href="%s.xhtml#%s">%s</a>'
                                 % (cid, esc(sec["id"]), esc(sec["title_en"])))
                    else:
                        label = ('%s <span class="pending">&#183; pending</span>'
                                 % esc(sec["title_en"]))
                    parts.append('<li class="sec">%s%s'
                                 % (label,
                                    "" if sec["id"] in here else _span_suffix(sec)))
                    if sec.get("subsections"):
                        parts.append('<ol class="secs">')
                        for sub in sec["subsections"]:
                            if sub["id"] in here:
                                sl = ('<a href="%s.xhtml#%s">%s</a>'
                                      % (cid, esc(sub["id"]), esc(sub["title_en"])))
                            else:
                                sl = esc(sub["title_en"])
                            parts.append('<li class="sub">%s%s</li>'
                                         % (sl, "" if sub["id"] in here
                                            else _span_suffix(sub)))
                        parts.append('</ol>')
                    parts.append('</li>')
                parts.append('</ol>')
            parts.append('</li>')
    parts.append('</ol>')
    return "\n".join(parts)


def render_characters(gloss):
    """Front-matter "Principal Characters" page, from glossary rows flagged
    "principal": true. Published translations of Chinese books nearly always
    carry one, because Western readers reliably lose track of Chinese names;
    the glossary already holds everything needed. The optional "cast" field
    is the one-line description shown here (falls back to the row's note);
    optional "cast_order" sorts the page (default: alphabetical by en).
    Returns None when no row is flagged, and the page simply does not exist.
    """
    rows = []

    def walk(d):
        for k, v in d.items():
            if k.startswith("_"):
                continue
            if isinstance(v, dict) and "en" in v:
                if v.get("principal"):
                    rows.append((v.get("cast_order", 999),
                                 v.get("en", ""), v, k))
            elif isinstance(v, dict):
                walk(v)
    walk(gloss)
    if not rows:
        return None
    rows.sort(key=lambda r: (r[0], r[1]))
    parts = ["<h2>Principal Characters</h2>"]
    for _, en, v, hz in rows:
        desc = v.get("cast") or v.get("note") or ""
        zh = ' <span lang="%s">%s</span>' % (SRC_LANG, esc(hz))
        # desc is an XHTML fragment like note bodies: numeric refs, <i> --
        # inserted raw (the glossary double-escape lesson)
        parts.append('<p class="castrow"><b>%s</b>%s &#8212; %s</p>'
                     % (esc(html.unescape(en)), zh, desc))
    return "\n".join(parts)


def render_glossary(gloss):
    parts = []
    for section, entries in gloss.items():
        if section.startswith("_"):
            continue
        parts.append("<h3>%s</h3><dl class=\"gloss\">"
                     % esc(section.replace("_", " ").title()))
        for zh, rec in sorted(entries.items(),
                              key=lambda kv: kv[1].get("pinyin", kv[0])):
            # note fields are XHTML fragments (numeric refs + <i>), inserted
            # raw like the notes page -- esc() here once turned every &#8212;
            # into visible '&#8212;' text; en/pinyin may carry numeric refs but
            # no markup, so decode them before escaping.
            note = (" &#183; " + rec["note"]) if rec.get("note") else ""
            status = ""
            if rec.get("status") == "provisional":
                status = (" &#183; <i>romanization mine; not found in English "
                          "scholarship</i>")
            pinyin = esc(html.unescape(rec.get("pinyin", "")))
            parts.append("<dt>%s <span lang=\"%s\">%s</span></dt>"
                         "<dd>%s%s%s</dd>"
                         % (esc(html.unescape(rec["en"])), SRC_LANG, esc(zh),
                            pinyin, note, status))
        parts.append("</dl>")
    return "\n".join(parts)


def render_errata(bm):
    """The publisher's errata table, rendered as translator's back matter."""
    rows = []
    for r in bm.get("errata_rows", []):
        folio = esc(str(r["folio"]))
        page = esc(str(r["page"]))
        loc = "line %s, char %s" % (esc(str(r["line"])), esc(str(r["char"])))
        if r["kind"] == "wrong":
            fix = ("<span lang=\"%s\">%s</span> &#8594; "
                   "<span lang=\"%s\">%s</span>"
                   % (SRC_LANG, esc(r["printed"]), SRC_LANG, esc(r["correct"])))
        elif r["kind"] == "append":
            fix = "&#8212;"
        else:
            fix = ("insert <span lang=\"%s\">%s</span>"
                   % (SRC_LANG, esc(r["correct"])))
        note = (" &#183; " + esc(r["note"])) if r.get("note") else ""
        rows.append(
            "<tr><td>%s</td><td>%s</td><td>%s</td><td class=\"hz\">%s%s</td></tr>"
            % (folio, page if str(r["page"]) != str(r["folio"]) else "&#8212;",
               loc, fix, note))
    headnote = bm.get("errata_headnote") or (
        "The book prints a publisher's errata table on its final leaf, "
        "reproduced here in full. Each row gives the printed folio, the line, "
        "the character position within that line, and the fix &#8212; a dropped "
        "character to insert or a misprinted character to replace. Every "
        "correction has been checked against this translation and applied where "
        "it bears on the reading text.")
    return (
        '<h1>Errata</h1>'
        '<p class="note">%s</p>'
        '<table class="errata"><tr><th>Folio</th><th>Printed page</th>'
        '<th>Location</th><th>Correction</th></tr>%s</table>'
        % (headnote, "".join(rows)))


def render_colophon(bm):
    c = bm.get("colophon", {})
    return (
        '<h1>Colophon</h1>'
        '<p class="note">The book\'s original copyright leaf, '
        'reproduced and translated.</p>'
        '<div class="colophon">'
        '<p lang="%(sl)s">%(title_zh)s</p>'
        '<p lang="%(sl)s">%(author_zh)s&#160;著</p>'
        '<p class="notice" lang="%(sl)s">%(notice_zh)s</p>'
        '<p>%(notice_en)s</p>'
        '<p lang="%(sl)s">%(date_zh)s</p>'
        '<p>%(date_en)s</p>'
        '</div>'
        % {"sl": SRC_LANG,
           "title_zh": esc(c.get("title_zh", "")),
           "author_zh": esc(c.get("author_zh", "")),
           "notice_zh": esc(c.get("notice_zh", "")),
           "notice_en": esc(c.get("notice_en", "")),
           "date_zh": esc(c.get("date_zh", "")),
           "date_en": esc(c.get("date_en", ""))})


def translator_note(meta, n_chapters):
    """The translator's note.

    Prefer to write it per project: put a list of paragraph strings under
    "translator_note" in book.json and they are rendered verbatim (inline
    <i>...</i> is honored; use numeric character references like &#8212; not
    named entities). If that field is absent, a generic note describing the
    method is used, with the title/year/chapter-count filled in.
    """
    heading = esc(meta.get("note_heading") or "Translator's Note")
    paras = meta.get("translator_note_paragraphs")
    if paras:
        body = "".join('<p class="note">%s</p>' % p for p in paras)
        return "<h1>%s</h1>" % heading + body
    return (
        '<h1>%s</h1>' % heading +
        '<p class="note">This is an English translation of '
        '<i>%(title_zh)s</i> (<i>%(title_en)s</i>), from an image-only scan '
        'with no digital text layer.</p>'
        '<p class="note">The text was recovered by optical character '
        'recognition and then read against magnified images of the physical '
        'pages. Every proper name, every number, and every passage the machine '
        'and the eye disagreed on was checked against the scan rather than '
        'trusted to the OCR. A paragraph-by-paragraph bilingual audit file '
        'exists alongside this edition for anyone who wants to check the '
        'workings.</p>'
        '<p class="note">Names follow pinyin except where an English '
        'conventional form exists. Renderings marked "provisional" in the '
        'glossary are romanizations not found attested in English-language '
        'scholarship. Notes are the translator\'s throughout; the source '
        'carries none of its own. Where the scan is damaged or a leaf is '
        'missing, the gap is stated in a note and nothing is invented to bridge '
        'it.</p>'
        '<p class="note">This build contains %(n)s translated '
        'chapter(s).</p>'
        % {"title_zh": esc(meta["title_zh"]),
           "title_en": esc(meta["title_en"]), "n": n_chapters})


def coverage_sentence(structure, translated):
    """The honesty line on the title page: is this the finished book, an
    interim build, or the pre-translation survey skeleton, and what is in it."""
    n = len(structure)
    done_word = "prepared" if _annotated() else "translated"
    progress = "in progress" if _annotated() else "a translation in progress"
    if not translated:
        return ('<p class="note">Survey skeleton: the full structure of the '
                'book, nothing yet %s.</p>' % done_word)
    if len(translated) == n:
        return ('<p class="note">This edition contains the complete book: '
                'all %d chapter%s.</p>' % (n, "" if n == 1 else "s"))
    names = [c["title_en"] for c in structure if c["id"] in translated]
    return ('<p class="note">This is an interim build, %s. '
            'It contains %d of the book\'s %d chapters: %s. The '
            'rest follow in later builds.</p>'
            % (progress, len(names), n, "; ".join(esc(x) for x in names)))


def write(path, body, title):
    with open(path, "w") as fh:
        fh.write(XHTML % {"title": esc(typographize(title)),
                          "body": typographize(body)})


def resolve_uid(uid, title_en):
    """The package's unique identifier. A urn:uuid whose tail is not a real
    UUID gets REPLACED with a deterministic UUIDv5 of the title -- a malformed
    urn:uuid once made Apple Books silently refuse a finished book, and the
    stub uid a template ships with is exactly that shape. Any other non-empty
    uid (a DOI, an ISBN urn, a proper uuid) is kept verbatim."""
    if uid:
        if not uid.startswith("urn:uuid:"):
            return uid
        try:
            uuid.UUID(uid[len("urn:uuid:"):])
            return uid
        except ValueError:
            pass
    return "urn:uuid:%s" % uuid.uuid5(uuid.NAMESPACE_URL,
                                      "winston-translation:" + title_en)


def main(epub_path):
    global SRC_LANG
    book = load_json("book.json", {})
    # Legacy field names (title_en, author_en, year, publication_date,
    # publisher, description, subject, language, uid) are honored as-is;
    # the richer optional fields extend them without replacing anything.
    subjects = book.get("subjects", book.get("subject", []))
    if isinstance(subjects, str):
        subjects = [subjects]
    meta = {
        "title_en": book.get("title_en", "Untitled"),
        "title_zh": book.get("title_zh", ""),
        "subtitle_en": book.get("subtitle_en", ""),
        "title_file_as": book.get("title_file_as", ""),
        "author_en": book.get("author_en", ""),
        "author_zh": book.get("author_zh", ""),
        "author_file_as": book.get("author_file_as", ""),
        "translator_en": book.get("translator_en", ""),
        "year": book.get("year", ""),
        "publication_date": book.get("publication_date", ""),
        "publisher": book.get("publisher", ""),
        "description": book.get("description", ""),
        "subjects": subjects,
        "rights": book.get("rights", ""),
        "source_ref": book.get("source_ref", ""),
        "series": book.get("series", ""),
        "series_index": book.get("series_index", ""),
        "language": book.get("language", "en"),
        "source_language": book.get("source_language", ""),
        "source_script": book.get("source_script", "zh"),
        "cover_image": book.get("cover_image", ""),
        "uid": resolve_uid(book.get("uid", ""),
                           book.get("title_en", "Untitled")),
        # dcterms:modified is DETERMINISTIC: book.json's "modified" if set,
        # else a fixed epoch. A wall-clock timestamp makes every rebuild a
        # byte-different OPF, which defeats diffing and re-uploads unchanged
        # books to readers' libraries.
        "modified": book.get("modified", "2026-01-01T00:00:00Z"),
        "translator_note_paragraphs": book.get("translator_note"),
        "note_heading": book.get("note_heading",
                                 "Translator's Note"),
    }
    global EDITION
    EDITION = book.get("edition_kind", "translation")
    SRC_LANG = meta["source_script"]
    structure = [c for c in book.get("structure", []) if c.get("id", "").startswith("ch")]
    if not structure:
        sys.exit("no chapters in book.json structure")
    compute_spans(structure, book)

    def md_of(cid):
        return os.path.join(ROOT, "out", "%s_reading.md" % cid)

    chapters = [c for c in structure if os.path.exists(md_of(c["id"]))]
    translated = {c["id"] for c in chapters}
    # No translated chapters yet is fine: this builds the SURVEY skeleton -- a
    # fully navigable EPUB whose TOC links every part/chapter/section/subsection
    # to an outline page, so the whole structure can be reviewed before any
    # translation begins.
    skeleton_only = not chapters

    if os.path.isdir(BUILD):
        shutil.rmtree(BUILD)
    oebps = os.path.join(BUILD, "OEBPS")
    os.makedirs(os.path.join(oebps, "images"))
    os.makedirs(os.path.join(BUILD, "META-INF"))

    gloss = load_json("glossary.json", {})
    notes_by_chap = load_json("notes.json", {})
    figspec = load_json("figures.json", {})

    manifest_figs = []
    for chap in chapters:
        for spec in figspec.get(chap["id"], []):
            src = os.path.join(FIGS, spec["file"])
            if not os.path.exists(src):
                continue
            dest = os.path.join(oebps, "images", spec["file"])
            if not shrink_image(src, dest):
                shutil.copy(src, dest)
            if spec["file"] not in manifest_figs:
                manifest_figs.append(spec["file"])

    with open(os.path.join(oebps, "style.css"), "w") as fh:
        fh.write(CSS)

    # cover: a supplied cover image is copied byte-identical (a cover is
    # chrome, not a figure -- never greyscale or re-encode it); with none
    # supplied a typographic cover is generated when Pillow and fonts allow.
    # Kindle and Apple Books key the library thumbnail off the manifest's
    # properties="cover-image" item AND the legacy <meta name="cover"> hint,
    # so both are emitted below.
    have_cover = False
    cover_name = ""
    if meta["cover_image"]:
        for base in (ROOT, os.path.join(ROOT, "data"), FIGS, PNG):
            csrc = os.path.join(base, meta["cover_image"])
            if os.path.exists(csrc):
                cover_name = "cover" + os.path.splitext(csrc)[1].lower()
                shutil.copy(csrc, os.path.join(oebps, "images", cover_name))
                have_cover = True
                break
        if not have_cover:
            sys.exit("book.json cover_image not found: %s" % meta["cover_image"])
    else:
        cover_name = "cover.png"
        tagline = ("Annotated Edition" if _annotated()
                   else "Annotated English Translation")
        have_cover = make_cover(os.path.join(oebps, "images", cover_name),
                                meta["title_en"], meta["title_zh"],
                                meta["author_en"], meta["author_zh"],
                                tagline=tagline)
    if have_cover:
        write(os.path.join(oebps, "cover.xhtml"),
              '<div class="cover"><img src="images/%s" alt="Cover: %s"/></div>'
              % (esc(cover_name), esc(meta["title_en"])), "Cover")

    # title page (with the coverage sentence: complete, interim, or skeleton)
    byline = esc(meta["author_en"])
    if meta["author_zh"]:
        byline += (' &#183; <span lang="%s">%s</span>'
                   % (SRC_LANG, esc(meta["author_zh"])))
    yr = (' <p class="note">%s</p>' % esc(str(meta["year"]))) if meta["year"] else ""
    sub = ('<p class="subtitle">%s</p>' % esc(meta["subtitle_en"])
           if meta["subtitle_en"] else "")
    # The source-title line only makes sense for a translation; an annotated
    # English edition has no separate source title, and title_zh is empty.
    zh_line = ('<p lang="%s">%s</p>' % (SRC_LANG, esc(meta["title_zh"]))
               if meta["title_zh"] else "")
    edition_line = ('<p class="note">Annotated edition</p>' if _annotated()
                    else '<p class="note">English translation</p>')
    write(os.path.join(oebps, "titlepage.xhtml"),
          '<div class="tp"><h1>%s</h1>%s%s'
          '<p>%s</p>%s%s%s</div>'
          % (esc(meta["title_en"]), sub, zh_line,
             byline, yr, edition_line,
             coverage_sentence(structure, translated)),
          meta["title_en"])

    # chapter bodies: EVERY chapter gets a page -- real content if translated,
    # else a skeleton outline -- so every table-of-contents link resolves.
    # ids_present[cid] records the section/subsection anchors actually emitted,
    # so the contents and nav link only anchors that exist (a chapter translated
    # a batch at a time emits only its finished sections).
    counter = [0]
    ids_present = {}
    page_index = []
    for chap in structure:
        doc = chap["id"] + ".xhtml"
        if chap["id"] in translated:
            section_ids = [s["id"] for s in chap.get("sections", [])]
            sub_ids = [sub["id"] for s in chap.get("sections", [])
                       for sub in s.get("subsections", [])]
            body, ids = render_body(md_of(chap["id"]), section_ids, sub_ids,
                                    figspec.get(chap["id"], []),
                                    notes_by_chap.get(chap["id"], []),
                                    counter, doc,
                                    pagemap=load_pagemap(chap["id"]),
                                    unit=chap["id"], page_index=page_index)
        else:
            body, ids = render_skeleton(chap)
        ids_present[chap["id"]] = ids
        write(os.path.join(oebps, doc), body, chap["title_en"])

    # contents map (after the bodies, so it links only anchors that exist)
    write(os.path.join(oebps, "contents.xhtml"),
          render_contents(structure, translated, ids_present), "Contents")

    # a note whose anchor never matched would be silently dropped; refuse.
    orphans = [(cid, n["anchor"]) for cid, lst in notes_by_chap.items()
               for n in lst if cid in translated and not n.get("used")]
    if orphans:
        sys.stderr.write("BUILD FAILED: %d note anchor(s) never matched and "
                         "would be silently dropped:\n" % len(orphans))
        for cid, a in orphans:
            sys.stderr.write("  %-9s %s\n" % (cid, a[:88]))
        sys.exit(2)

    # same contract for figures: an unmatched 'before' anchor would silently
    # drop the image; refuse.
    lost = [(cid, f["file"], f["before"]) for cid, lst in figspec.items()
            if not cid.startswith("_") and cid in translated
            for f in lst if not f.get("placed")]
    if lost:
        sys.stderr.write("BUILD FAILED: %d figure(s) never placed:\n" % len(lost))
        for cid, fn, b in lost:
            sys.stderr.write("  %-9s %s before=%s\n" % (cid, fn, b[:60]))
        sys.exit(2)

    write(os.path.join(oebps, "notes.xhtml"),
          render_notes_page(chapters, notes_by_chap), "Notes")

    backmatter_title = "%s and Glossary" % (meta.get("note_heading")
                                             or "Translator's Note")
    write(os.path.join(oebps, "backmatter.xhtml"),
          translator_note(meta, len(chapters))
          + "<h1>Glossary of Names and Terms</h1>"
          + render_glossary(gloss),
          backmatter_title)

    back_matter = load_json("back_matter.json", {})
    have_backmatter = bool(back_matter.get("errata_rows") or
                           back_matter.get("colophon"))
    if have_backmatter:
        write(os.path.join(oebps, "errata.xhtml"),
              render_errata(back_matter), "Errata")
        write(os.path.join(oebps, "colophon.xhtml"),
              render_colophon(back_matter), "Colophon")

    # spine order: cover FIRST (Kindle/Books open on it), then every chapter
    # (translated or skeleton).
    docs = []
    if have_cover:
        docs.append(("cover.xhtml", "Cover"))
    docs += [("titlepage.xhtml", "Title Page")]
    cast_page = render_characters(gloss)
    if cast_page:
        write(os.path.join(oebps, "characters.xhtml"), cast_page,
              "Principal Characters")
        docs += [("characters.xhtml", "Principal Characters")]
    docs += [("contents.xhtml", "Contents")]
    docs += [(c["id"] + ".xhtml", c["title_en"]) for c in structure]
    docs += [("notes.xhtml", "Notes"),
             ("backmatter.xhtml", backmatter_title)]
    if have_backmatter:
        docs += [("errata.xhtml", "Errata"), ("colophon.xhtml", "Colophon")]

    # e-reader nav: the full TOC, nested part -> chapter -> section -> subsection.
    # Every entry links to a real anchor (content or skeleton), so the whole
    # book is navigable from the survey build onward.
    def sec_nav(chap):
        cid = chap["id"]
        here = ids_present.get(cid, set())
        items = []
        for sec in chap.get("sections", []):
            sub = ""
            if sec.get("subsections"):
                sub = "<ol>" + "".join(
                    ('<li><a href="%s.xhtml#%s">%s</a></li>'
                     % (cid, esc(s["id"]), esc(s["title_en"]))
                     if s["id"] in here
                     else '<li><a href="%s.xhtml">%s</a></li>'
                     % (cid, esc(s["title_en"])))
                    for s in sec["subsections"]) + "</ol>"
            if sec["id"] in here:
                items.append('<li><a href="%s.xhtml#%s">%s</a>%s</li>'
                             % (cid, esc(sec["id"]), esc(sec["title_en"]), sub))
            else:
                items.append('<li><a href="%s.xhtml">%s</a>%s</li>'
                             % (cid, esc(sec["title_en"]), sub))
        return "<ol>" + "".join(items) + "</ol>" if items else ""

    nav_items = ['<li><a href="titlepage.xhtml">Title Page</a></li>']
    if cast_page:
        nav_items.append('<li><a href="characters.xhtml">Principal '
                         'Characters</a></li>')
    nav_items.append('<li><a href="contents.xhtml">Contents</a></li>')
    for part_label, chaps in part_groups(structure):
        chap_lis = []
        for chap in chaps:
            pend = "" if chap["id"] in translated else " (pending)"
            chap_lis.append('<li><a href="%s.xhtml">%s%s</a>%s</li>'
                            % (chap["id"], esc(chap["title_en"]), pend,
                               sec_nav(chap)))
        if part_label:
            nav_items.append('<li><span>%s</span><ol>%s</ol></li>'
                             % (esc(part_label), "".join(chap_lis)))
        else:
            nav_items.extend(chap_lis)
    nav_items += ['<li><a href="notes.xhtml">Notes</a></li>',
                  '<li><a href="backmatter.xhtml">%s</a></li>'
                  % esc(backmatter_title)]
    if have_backmatter:
        nav_items += ['<li><a href="errata.xhtml">Errata</a></li>',
                      '<li><a href="colophon.xhtml">Colophon</a></li>']

    # page-list: one entry per pagebreak marker in the text, and none at all
    # when no pagemap files exist (qa_epub's pagination gate then compares
    # 0 == 0). Front-matter units keep their own sequence labeled apart.
    page_list = ""
    if page_index:
        pl_items = []
        for f, pid, n, unit in page_index:
            label = ("fm %s" % n) if str(unit).startswith("fm") else str(n)
            pl_items.append('<li><a href="%s#%s">%s</a></li>'
                            % (f, pid, esc(label)))
        page_list = ('<nav epub:type="page-list" hidden="hidden">'
                     '<h1>Printed pages</h1><ol>' + "".join(pl_items)
                     + "</ol></nav>")

    nav = ('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
           + "".join(nav_items) + "</ol></nav>" + page_list
           + '<nav epub:type="landmarks" hidden="hidden"><ol>'
           + ('<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>'
              if have_cover else "")
           + '<li><a epub:type="titlepage" href="titlepage.xhtml">Title Page</a></li>'
           '<li><a epub:type="toc" href="contents.xhtml">Contents</a></li>'
           '<li><a epub:type="bodymatter" href="%s">Begin Reading</a></li>'
           "</ol></nav>" % (structure[0]["id"] + ".xhtml"))
    write(os.path.join(oebps, "nav.xhtml"), nav, "Contents")

    ncx = "".join(
        '<navPoint id="n%d" playOrder="%d"><navLabel><text>%s</text></navLabel>'
        '<content src="%s"/></navPoint>' % (i, i, esc(t), f)
        for i, (f, t) in enumerate(docs, 1))
    with open(os.path.join(oebps, "toc.ncx"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>'
                 '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
                 '<head><meta name="dtb:uid" content="%s"/></head>'
                 "<docTitle><text>%s</text></docTitle><navMap>%s</navMap></ncx>"
                 % (meta["uid"], esc(meta["title_en"]), ncx))

    items = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
             '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
             '<item id="css" href="style.css" media-type="text/css"/>']
    for i, (f, _) in enumerate(docs, 1):
        items.append('<item id="d%d" href="%s" media-type="application/xhtml+xml"/>' % (i, f))
    for i, f in enumerate(manifest_figs, 1):
        items.append('<item id="fig%d" href="images/%s" media-type="%s"/>'
                     % (i, f, mime_of(f)))
    if have_cover:
        items.append('<item id="cover-image" href="images/%s" media-type="%s" '
                     'properties="cover-image"/>' % (cover_name,
                                                     mime_of(cover_name)))
    spine = "".join('<itemref idref="d%d"/>' % i for i in range(1, len(docs) + 1))

    # Rich Dublin Core metadata, formatted for the catalogues Kindle and Apple
    # Books build: a main title with sort form (+ optional subtitle and the
    # source title as dcterms:alternative), a creator with MARC role, file-as
    # sort key and alternate-script original name, the translator as a
    # contributor, publisher, date, description, subjects, rights, source
    # reference, series (both the calibre legacy metas and the EPUB3
    # collection), the Apple fonts flag, and the deterministic modified stamp.
    lang = esc(meta["language"] or "en")
    src_primary = SRC_LANG.split("-")[0]
    md = ['<dc:identifier id="pub-id">%s</dc:identifier>' % esc(meta["uid"]),
          '<dc:title id="title">%s</dc:title>' % esc(meta["title_en"]),
          '<meta refines="#title" property="title-type">main</meta>',
          '<meta refines="#title" property="file-as">%s</meta>'
          % esc(meta["title_file_as"] or meta["title_en"])]
    if meta["subtitle_en"]:
        md += ['<dc:title id="subtitle">%s</dc:title>' % esc(meta["subtitle_en"]),
               '<meta refines="#subtitle" property="title-type">subtitle</meta>']
    if meta["title_zh"]:
        md.append('<meta property="dcterms:alternative" xml:lang="%s">%s</meta>'
                  % (esc(src_primary), esc(meta["title_zh"])))
    md.append('<dc:language>%s</dc:language>' % lang)
    if meta["source_language"]:
        md.append('<meta property="dcterms:language">%s</meta>'
                  % esc(meta["source_language"]))
    if meta["author_en"]:
        md += ['<dc:creator id="creator">%s</dc:creator>' % esc(meta["author_en"]),
               '<meta refines="#creator" property="role" scheme="marc:relators">aut</meta>',
               '<meta refines="#creator" property="file-as">%s</meta>'
               % esc(meta["author_file_as"] or meta["author_en"])]
        if meta["author_zh"]:
            md.append('<meta refines="#creator" property="alternate-script" '
                      'xml:lang="%s">%s</meta>'
                      % (esc(src_primary), esc(meta["author_zh"])))
    if meta["translator_en"]:
        md += ['<dc:contributor id="translator">%s</dc:contributor>'
               % esc(meta["translator_en"]),
               '<meta refines="#translator" property="role" '
               'scheme="marc:relators">trl</meta>']
    if meta["publisher"]:
        md.append('<dc:publisher>%s</dc:publisher>' % esc(meta["publisher"]))
    if meta["publication_date"]:
        md.append('<dc:date>%s</dc:date>' % esc(meta["publication_date"]))
    elif meta["year"]:
        md.append('<dc:date>%s-01-01</dc:date>' % esc(str(meta["year"])))
    if meta["description"]:
        md.append('<dc:description>%s</dc:description>' % esc(meta["description"]))
    for subj in meta["subjects"]:
        md.append('<dc:subject>%s</dc:subject>' % esc(subj))
    if meta["rights"]:
        md.append('<dc:rights>%s</dc:rights>' % esc(meta["rights"]))
    if meta["source_ref"]:
        md.append('<dc:source>%s</dc:source>' % esc(meta["source_ref"]))
    if meta["series"]:
        idx = str(meta["series_index"] or 1)
        md += ['<meta name="calibre:series" content="%s"/>'
               % esc(meta["series"]),
               '<meta name="calibre:series_index" content="%s"/>' % esc(idx),
               '<meta id="series" property="belongs-to-collection">%s</meta>'
               % esc(meta["series"]),
               '<meta refines="#series" property="collection-type">series</meta>',
               '<meta refines="#series" property="group-position">%s</meta>'
               % esc(idx)]
    md.append('<meta property="ibooks:specified-fonts">true</meta>')
    md.append('<meta property="dcterms:modified">%s</meta>' % esc(meta["modified"]))
    if have_cover:
        md.append('<meta name="cover" content="cover-image"/>')

    # EPUB2 guide block: obsolete in EPUB3 but still read by Kindle's older
    # ingestion paths, and harmless everywhere else.
    guide = ""
    if have_cover:
        guide += '<reference type="cover" title="Cover" href="cover.xhtml"/>'
    guide += ('<reference type="toc" title="Contents" href="contents.xhtml"/>'
              '<reference type="text" title="Begin Reading" href="%s"/>'
              % (structure[0]["id"] + ".xhtml"))

    with open(os.path.join(oebps, "content.opf"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>\n'
                 '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
                 'unique-identifier="pub-id" xml:lang="%s" prefix="ibooks: '
                 'http://vocabulary.itunes.apple.com/rdf/ibooks/vocabulary-extensions-1.0/">\n'
                 '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
                 % lang
                 + "\n".join(md) + "\n"
                 "</metadata>\n<manifest>\n" + "\n".join(items) + "\n</manifest>\n"
                 '<spine toc="ncx" page-progression-direction="ltr">\n'
                 + spine + "\n</spine>\n"
                 "<guide>" + guide + "</guide>\n</package>")

    # Apple Books honours embedded/specified fonts only when this OCF-level
    # file says so as well as the OPF property.
    with open(os.path.join(BUILD, "META-INF",
                           "com.apple.ibooks.display-options.xml"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>'
                 '<display_options><platform name="*">'
                 '<option name="specified-fonts">true</option>'
                 "</platform></display_options>")

    with open(os.path.join(BUILD, "META-INF", "container.xml"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>'
                 '<container version="1.0" '
                 'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                 '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                 'media-type="application/oebps-package+xml"/></rootfiles></container>')
    with open(os.path.join(BUILD, "mimetype"), "w") as fh:
        fh.write("application/epub+zip")

    os.makedirs(os.path.dirname(epub_path), exist_ok=True)
    if os.path.exists(epub_path):
        os.remove(epub_path)
    with zipfile.ZipFile(epub_path, "w") as z:
        z.write(os.path.join(BUILD, "mimetype"), "mimetype",
                compress_type=zipfile.ZIP_STORED)
        for base, _, files in os.walk(BUILD):
            for name in sorted(files):
                if name == "mimetype":
                    continue
                full = os.path.join(base, name)
                z.write(full, os.path.relpath(full, BUILD),
                        compress_type=zipfile.ZIP_DEFLATED)
    print("wrote %s (%d of %d chapters translated, %d notes, %d pagebreaks)"
          % (epub_path, len(chapters), len(structure), counter[0],
             len(page_index)))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        _out = sys.argv[1]
    else:
        # The deliverable name lives in book.json so builder, QA and the Stop
        # hook agree on it; the out/book.epub default bit real projects that
        # built the default name and shipped a stale deliverable.
        try:
            _out = json.load(open(os.path.join(ROOT, "book.json")))\
                .get("deliverable") or os.path.join(ROOT, "out", "book.epub")
        except Exception:
            _out = os.path.join(ROOT, "out", "book.epub")
        if not os.path.isabs(_out):
            _out = os.path.join(ROOT, _out)
    main(_out)
