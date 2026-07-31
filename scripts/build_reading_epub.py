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
the substitution would eat them.

Reading markdown per chapter uses: '## ' chapter title (h1), '### ' section
(h2, given the section's book.json id), '#### ' subsection (h3); every other
non-blank line is a paragraph.

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
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(ROOT, "data", "figs")
PNG = os.path.join(ROOT, "data", "png")
BUILD = os.path.join(ROOT, "build")

CSS = """\
body { font-family: serif; line-height: 1.6; margin: 1em 1.2em; }
h1 { font-size: 1.5em; margin: 1.4em 0 0.6em; font-weight: normal; }
h2 { font-size: 1.15em; margin: 1.6em 0 0.6em; font-weight: normal; color: #333; }
h3 { font-size: 1.02em; margin: 1.4em 0 0.5em; font-weight: bold; color: #444; }
p { margin: 0 0 0.85em; text-indent: 1.4em; }
p.first, p.note { text-indent: 0; }
p.note { font-size: 0.92em; color: #444; }
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
.tp { text-align: center; margin-top: 3em; }
.tp h1 { font-size: 1.7em; }
.tp p { text-indent: 0; }
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


def shrink_image(src, dest):
    try:
        from PIL import Image
    except ImportError:
        return False
    img = Image.open(src)
    if img.width > MAX_FIG_WIDTH:
        h = int(img.height * MAX_FIG_WIDTH / img.width)
        img = img.resize((MAX_FIG_WIDTH, h), Image.LANCZOS)
    img.convert("L").save(dest, format="PNG", optimize=True)
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

    Candidates are ordered by where the reference lands (end of anchor), so a
    contained anchor cannot make the numbering run backwards. Matching happens
    on the escaped text BEFORE markup substitution.
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
        paragraph = paragraph.replace(note["anchor"], note["anchor"] + ref, 1)
    return paragraph


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
    out.append('<p class="note"><span class="pending">Not yet translated.</span>'
               '%s</p>' % (" Source&#160;" + sl if sl else ""))
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


def render_body(md_path, section_ids, sub_ids, figures, notes, counter, doc,
                ids=None):
    """Render one chapter's reading markdown to XHTML.

    section_ids / sub_ids are the chapter's book.json section and subsection ids,
    consumed in order as '### ' and '#### ' headings are met, so the contents
    page can deep-link each section and subsection. Either list may be empty,
    in which case the matching heading gets no id (linked at the coarser level).
    """
    out, first = [], True
    ids = ids if ids is not None else set()
    sids, ssids = list(section_ids), list(sub_ids)
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
        for fig in figures:
            if not fig.get("placed") and fig["before"] in line[:80]:
                out.append(
                    '<figure><img src="images/%s" alt="%s"/>'
                    "<figcaption>%s</figcaption></figure>"
                    % (fig["file"], esc(fig["alt"]), esc(fig["caption"])))
                fig["placed"] = True
        text = insert_notes(esc(line), notes, counter, doc)
        text = re.sub(r"\*([^*\n]+)\*", r"<i>\1</i>", text)
        cls = ' class="first"' if first else ""
        out.append("<p%s>%s</p>" % (cls, text))
        first = False
    return "\n".join(out), ids


def render_notes_page(chapters, notes_by_chap):
    parts = ['<h1>Notes</h1>',
             '<p class="note">Each number links back to its place in the '
             'text. Notes are the translator\'s throughout; the source book '
             'carries none of its own.</p>']
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
                '<div class="endnote" id="note%d" epub:type="footnote">'
                '<p><a class="backref" href="%s#ref%d">%d.</a> %s</p></div>'
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
    otherwise), with its source page span. Because every chapter always has a
    page, every chapter entry resolves -- the whole contents is hyperlinked from
    the first (survey) build onward.

    ids_present maps a chapter id to the set of section/subsection anchor ids
    actually emitted in that chapter's page, so a chapter translated a batch at a
    time links only its finished sections and shows the rest as pending text
    (never a link to an anchor that does not exist, which qa_epub rejects)."""
    ids_present = ids_present or {}
    n_ch = len(structure)
    n_sec = sum(len(c.get("sections", [])) for c in structure)
    n_sub = sum(len(s.get("subsections", [])) for c in structure
                for s in c.get("sections", []))
    groups = part_groups(structure)
    n_parts = sum(1 for lbl, _ in groups if lbl)
    tally = ("%s%d chapters, %d sections"
             % ("%d parts, " % n_parts if n_parts else "", n_ch, n_sec)
             + (", %d subsections" % n_sub if n_sub else ""))
    parts = ['<h1>Contents</h1>',
             '<p class="note">The complete book: %s. Every entry links to its '
             'place; units not yet translated link to a skeleton outline showing '
             'their source page span, so the whole shape of the book is '
             'navigable from the start.</p>' % tally,
             '<ol class="contents">']
    for part_label, chaps in groups:
        if part_label:
            parts.append('<li class="part">%s</li>' % esc(part_label))
        for chap in chaps:
            cid = chap["id"]
            here = ids_present.get(cid, set())
            done = cid in translated
            mark = "" if done else ' <span class="pending">&#183; pending</span>'
            parts.append('<li class="chap"><a href="%s.xhtml">%s</a>%s%s</li>'
                         % (cid, esc(chap["title_en"]),
                            _span_suffix(chap), mark))
            if not chap.get("sections"):
                continue
            parts.append('<ol>')
            for sec in chap["sections"]:
                if sec["id"] in here:
                    label = ('<a href="%s.xhtml#%s">%s</a>'
                             % (cid, esc(sec["id"]), esc(sec["title_en"])))
                else:
                    label = ('%s <span class="pending">&#183; pending</span>'
                             % esc(sec["title_en"]))
                parts.append('<li class="sec">%s%s</li>'
                             % (label, _span_suffix(sec)))
                if sec.get("subsections"):
                    parts.append('<ol class="secs">')
                    for sub in sec["subsections"]:
                        if sub["id"] in here:
                            sl = ('<a href="%s.xhtml#%s">%s</a>'
                                  % (cid, esc(sub["id"]), esc(sub["title_en"])))
                        else:
                            sl = esc(sub["title_en"])
                        parts.append('<li class="sub">%s%s</li>'
                                     % (sl, _span_suffix(sub)))
                    parts.append('</ol>')
            parts.append('</ol>')
    parts.append('</ol>')
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
            note = (" &#183; " + esc(rec["note"])) if rec.get("note") else ""
            status = ""
            if rec.get("status") == "provisional":
                status = (" &#183; <i>romanization mine; not found in English "
                          "scholarship</i>")
            pinyin = esc(rec.get("pinyin", ""))
            parts.append("<dt>%s <span lang=\"zh-Hant\">%s</span></dt>"
                         "<dd>%s%s%s</dd>"
                         % (esc(rec["en"]), esc(zh), pinyin, note, status))
        parts.append("</dl>")
    return "\n".join(parts)


def render_errata(bm):
    """The publisher's errata table, rendered as translator's back matter.

    The corrections have been checked against the translation. Those that fall
    within chapter 8 are applied and reflected in the reading text; the rest
    fall on chapters whose translation, made by reading the scan for sense,
    already follows the corrected readings. Folio 206's entry appends a chart,
    reproduced in chapter 7 as a figure.
    """
    KIND = {"dropped": "character dropped", "wrong": "misprint",
            "append": "clause / chart appended"}
    rows = []
    for r in bm.get("errata_rows", []):
        folio = esc(str(r["folio"]))
        page = esc(str(r["page"]))
        loc = "line %s, char %s" % (esc(str(r["line"])), esc(str(r["char"])))
        if r["kind"] == "wrong":
            fix = ("<span lang=\"zh-Hant\">%s</span> &#8594; "
                   "<span lang=\"zh-Hant\">%s</span>"
                   % (esc(r["printed"]), esc(r["correct"])))
        elif r["kind"] == "append":
            fix = "&#8212;"
        else:
            fix = ("insert <span lang=\"zh-Hant\">%s</span>"
                   % esc(r["correct"]))
        note = (" &#183; " + esc(r["note"])) if r.get("note") else ""
        rows.append(
            "<tr><td>%s</td><td>%s</td><td>%s</td><td class=\"hz\">%s%s</td></tr>"
            % (folio, page if str(r["page"]) != str(r["folio"]) else "&#8212;",
               loc, fix, note))
    headnote = back_matter.get("errata_headnote") or (
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
        '<p class="note">The book\'s original copyright leaf '
        '(<span lang="zh-Hant">版權頁</span>), reproduced and translated.</p>'
        '<div class="colophon">'
        '<p lang="zh-Hant">%s</p>'
        '<p lang="zh-Hant">%s&#160;著</p>'
        '<p class="notice" lang="zh-Hant">%s</p>'
        '<p>%s</p>'
        '<p lang="zh-Hant">%s</p>'
        '<p>%s</p>'
        '</div>'
        % (esc(c.get("title_zh", "")), esc(c.get("author_zh", "")),
           esc(c.get("notice_zh", "")), esc(c.get("notice_en", "")),
           esc(c.get("date_zh", "")), esc(c.get("date_en", ""))))


def translator_note(meta, n_chapters):
    """The translator's note.

    Prefer to write it per project: put a list of paragraph strings under
    "translator_note" in book.json and they are rendered verbatim (inline
    <i>...</i> is honored; use numeric character references like &#8212; not
    named entities). If that field is absent, a generic note describing the
    method is used, with the title/year/chapter-count filled in.
    """
    paras = meta.get("translator_note_paragraphs")
    if paras:
        body = "".join('<p class="note">%s</p>' % p for p in paras)
        return "<h1>Translator's Note</h1>" + body
    return (
        '<h1>Translator\'s Note</h1>'
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


def write(path, body, title):
    with open(path, "w") as fh:
        fh.write(XHTML % {"title": esc(title), "body": body})


def main(epub_path):
    book = load_json("book.json", {})
    meta = {
        "title_en": book.get("title_en", "Untitled"),
        "title_zh": book.get("title_zh", ""),
        "author_en": book.get("author_en", ""),
        "author_zh": book.get("author_zh", ""),
        "year": book.get("year", ""),
        "uid": book.get("uid", "urn:uuid:translation-" +
                        re.sub(r"[^a-z0-9]+", "-",
                               book.get("title_en", "book").lower())[:48]),
        "translator_note_paragraphs": book.get("translator_note"),
        "publisher": book.get("publisher", ""),
        "description": book.get("description", ""),
        "subject": book.get("subject", []),
        "language": book.get("language", "en"),
        "publication_date": book.get("publication_date", ""),
    }
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

    # title page
    byline = esc(meta["author_en"])
    if meta["author_zh"]:
        byline += ' &#183; <span lang="zh-Hant">%s</span>' % esc(meta["author_zh"])
    yr = (' <p class="note">%s</p>' % esc(str(meta["year"]))) if meta["year"] else ""
    write(os.path.join(oebps, "titlepage.xhtml"),
          '<div class="tp"><h1>%s</h1>'
          '<p lang="zh-Hant">%s</p>'
          '<p>%s</p>%s'
          '<p class="note">English translation</p></div>'
          % (esc(meta["title_en"]), esc(meta["title_zh"]), byline, yr),
          meta["title_en"])

    # chapter bodies: EVERY chapter gets a page -- real content if translated,
    # else a skeleton outline -- so every table-of-contents link resolves.
    # ids_present[cid] records the section/subsection anchors actually emitted,
    # so the contents and nav link only anchors that exist (a chapter translated
    # a batch at a time emits only its finished sections).
    counter = [0]
    ids_present = {}
    for chap in structure:
        doc = chap["id"] + ".xhtml"
        if chap["id"] in translated:
            section_ids = [s["id"] for s in chap.get("sections", [])]
            sub_ids = [sub["id"] for s in chap.get("sections", [])
                       for sub in s.get("subsections", [])]
            body, ids = render_body(md_of(chap["id"]), section_ids, sub_ids,
                                    figspec.get(chap["id"], []),
                                    notes_by_chap.get(chap["id"], []),
                                    counter, doc)
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

    write(os.path.join(oebps, "notes.xhtml"),
          render_notes_page(chapters, notes_by_chap), "Notes")

    write(os.path.join(oebps, "backmatter.xhtml"),
          translator_note(meta, len(chapters))
          + "<h1>Glossary of Names and Terms</h1>"
          + render_glossary(gloss),
          "Translator's Note and Glossary")

    back_matter = load_json("back_matter.json", {})
    have_backmatter = bool(back_matter.get("errata_rows") or
                           back_matter.get("colophon"))
    if have_backmatter:
        write(os.path.join(oebps, "errata.xhtml"),
              render_errata(back_matter), "Errata")
        write(os.path.join(oebps, "colophon.xhtml"),
              render_colophon(back_matter), "Colophon")

    # spine order: every chapter (translated or skeleton) is in the spine.
    docs = [("titlepage.xhtml", "Title Page"),
            ("contents.xhtml", "Contents")]
    docs += [(c["id"] + ".xhtml", c["title_en"]) for c in structure]
    docs += [("notes.xhtml", "Notes"),
             ("backmatter.xhtml", "Translator's Note and Glossary")]
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
                     else '<li>%s</li>' % esc(s["title_en"]))
                    for s in sec["subsections"]) + "</ol>"
            if sec["id"] in here:
                items.append('<li><a href="%s.xhtml#%s">%s</a>%s</li>'
                             % (cid, esc(sec["id"]), esc(sec["title_en"]), sub))
            else:
                items.append('<li>%s%s</li>' % (esc(sec["title_en"]), sub))
        return "<ol>" + "".join(items) + "</ol>" if items else ""

    nav_items = ['<li><a href="titlepage.xhtml">Title Page</a></li>',
                 '<li><a href="contents.xhtml">Contents</a></li>']
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
                  '<li><a href="backmatter.xhtml">Translator\'s Note and '
                  'Glossary</a></li>']
    if have_backmatter:
        nav_items += ['<li><a href="errata.xhtml">Errata</a></li>',
                      '<li><a href="colophon.xhtml">Colophon</a></li>']
    nav = ('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
           + "".join(nav_items) + "</ol></nav>"
           '<nav epub:type="landmarks" hidden="hidden"><ol>'
           '<li><a epub:type="titlepage" href="titlepage.xhtml">Title Page</a></li>'
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
        items.append('<item id="fig%d" href="images/%s" media-type="image/png"/>' % (i, f))
    spine = "".join('<itemref idref="d%d"/>' % i for i in range(1, len(docs) + 1))

    from datetime import datetime, timezone
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lang = esc(meta["language"] or "en")
    md_parts = [
        '<dc:identifier id="pub-id">%s</dc:identifier>' % meta["uid"],
        '<dc:title id="title">%s</dc:title>' % esc(meta["title_en"]),
        '<meta refines="#title" property="title-type">main</meta>',
        '<dc:language>%s</dc:language>' % lang,
    ]
    if meta["author_en"]:
        md_parts.append('<dc:creator id="creator">%s</dc:creator>' % esc(meta["author_en"]))
        md_parts.append('<meta refines="#creator" property="role" scheme="marc:relators">aut</meta>')
        md_parts.append('<meta refines="#creator" property="file-as">%s</meta>'
                        % esc(meta["author_en"]))
    if meta["publisher"]:
        md_parts.append('<dc:publisher>%s</dc:publisher>' % esc(meta["publisher"]))
    if meta["description"]:
        md_parts.append('<dc:description>%s</dc:description>' % esc(meta["description"]))
    for subj in meta["subject"]:
        md_parts.append('<dc:subject>%s</dc:subject>' % esc(subj))
    if meta["publication_date"]:
        md_parts.append('<dc:date>%s</dc:date>' % esc(meta["publication_date"]))
    elif meta["year"]:
        md_parts.append('<dc:date>%s-01-01</dc:date>' % esc(str(meta["year"])))
    md_parts.append('<meta property="dcterms:modified">%s</meta>' % modified)
    md_parts.append('<meta property="ibooks:specified-fonts">true</meta>')

    with open(os.path.join(oebps, "content.opf"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>\n'
                 '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
                 'unique-identifier="pub-id" prefix="ibooks: '
                 'http://vocabulary.itunes.apple.com/rdf/ibooks/vocabulary-extensions-1.0/">\n'
                 '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
                 + "\n".join(md_parts) + "\n"
                 "</metadata>\n<manifest>\n" + "\n".join(items) + "\n</manifest>\n"
                 '<spine toc="ncx">\n' + spine + "\n</spine>\n</package>")

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
    print("wrote %s (%d of %d chapters translated, %d notes)"
          % (epub_path, len(chapters), len(structure), counter[0]))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else
         os.path.join(ROOT, "out", "book.epub"))
