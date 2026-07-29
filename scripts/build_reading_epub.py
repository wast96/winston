#!/usr/bin/env python3
"""Build the cumulative reading edition of an EPUB-source translation.

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

Optional back matter (a colophon) is rendered when back_matter.json supplies one;
translator's note text can be supplied via book.json's "translator_note" field.
See the template's data files for the shapes.

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
.colophon { text-align: center; margin-top: 2em; }
.colophon .notice { border: 2px solid #444; display: inline-block; padding: 0.4em 1.6em; margin: 1em 0; font-size: 1.3em; letter-spacing: 0.3em; }
.colophon p { text-indent: 0; }
p.dateline { text-indent: 0; text-align: center; font-style: italic; color: #555; margin: 2em 0 1.2em; letter-spacing: 0.02em; }
p.brk { text-indent: 0; text-align: center; color: #999; margin: 1.5em 0; letter-spacing: 0.5em; }
.epigraph { text-align: center; margin: 4em 1.2em 0; }
.epigraph p { text-indent: 0; font-style: italic; color: #444; margin: 0.4em 0; font-size: 1.2em; letter-spacing: 0.03em; }
ol.contents li.epig { margin-top: 0.9em; font-style: italic; color: #555; }
body.cover { margin: 0; padding: 0; text-align: center; }
body.cover img { max-width: 100%; max-height: 100%; }
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
# Structure helpers: a size label per unit and grouping by optional "part".
# ---------------------------------------------------------------------------

def span_label(node):
    """A short size label. For an EPUB source this is the source-character count
    ('chars', filled by ingest_epub.py); returns '' when unknown."""
    c = node.get("chars")
    if c is None:
        return ""
    return "{:,}&#160;chars".format(c)


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
    size, and its full section/subsection outline with real anchors, so the table
    of contents can link all the way down before any translation exists.
    Returns (body, ids_emitted)."""
    ids = set()
    out = ['<h1>%s</h1>' % esc(chap["title_en"])]
    sl = span_label(chap)
    out.append('<p class="note"><span class="pending">Not yet translated.</span>'
               '%s</p>' % ("&#160;" + sl if sl else ""))
    for sec in chap.get("sections", []):
        ids.add(sec["id"])
        out.append('<h2 id="%s">%s</h2>' % (esc(sec["id"]), esc(sec["title_en"])))
        ssl = span_label(sec)
        if ssl:
            out.append('<p class="note">%s</p>' % ssl)
        for sub in sec.get("subsections", []):
            ids.add(sub["id"])
            out.append('<h3 id="%s">%s</h3>'
                       % (esc(sub["id"]), esc(sub["title_en"])))
    return "\n".join(out), ids


def render_epigraph(md_path):
    """Render a front epigraph / dateline page (e.g. the book's opening
    '1933 / Around the Lunar New Year'): the source's own scene-setting lines,
    centered, with no chapter heading and no note anchors. Every non-blank line
    becomes a centered line; a leading '## ' marker, if present, is stripped."""
    lines = []
    for raw in open(md_path):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            line = line[3:]
        elif line.startswith("#"):
            continue
        lines.append("<p>%s</p>" % esc(line))
    return '<div class="epigraph">%s</div>' % "".join(lines), set()


def render_body(md_path, section_ids, sub_ids, figures, notes, counter, doc,
                ids=None, scenes=None):
    """Render one chapter's reading markdown to XHTML.

    section_ids / sub_ids are the chapter's book.json section and subsection ids,
    consumed in order as '### ' and '#### ' headings are met, so the contents
    page can deep-link each section and subsection. Either list may be empty,
    in which case the matching heading gets no id (linked at the coarser level).

    scenes (from scenes.json) marks the source's own scene structure: its
    'datelines' are the terse time/place lines that head a scene (rendered
    distinctly, centered), and its 'breaks' are anchor prefixes before which a
    hard scene cut gets a centered divider. The source carries no typographic
    dividers of its own; this restores the scene rhythm without altering a word.
    """
    scenes = scenes or {}
    datelines = set(scenes.get("datelines", []))
    breaks = list(scenes.get("breaks", []))
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
        # A terse time/place scene-header line, rendered as a centered dateline.
        if line in datelines:
            out.append('<p class="dateline">%s</p>'
                       % insert_notes(esc(line), notes, counter, doc))
            first = True
            continue
        # A hard scene cut with no dateline of its own: a centered divider.
        for i, anchor in enumerate(breaks):
            if anchor is not None and line.startswith(anchor):
                out.append('<p class="brk">*&#160;*&#160;*</p>')
                breaks[i] = None
                first = True
                break
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
    otherwise), with its source size. Because every chapter always has a page,
    every chapter entry resolves -- the whole contents is hyperlinked from the
    first (survey) build onward.

    ids_present maps a chapter id to the set of section/subsection anchor ids
    actually emitted in that chapter's page, so a chapter translated a batch at a
    time links only its finished sections and shows the rest as pending text
    (never a link to an anchor that does not exist, which qa_epub rejects)."""
    ids_present = ids_present or {}
    n_ch = sum(1 for c in structure if c.get("kind") != "epigraph")
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
             'their source size, so the whole shape of the book is navigable '
             'from the start.</p>' % tally,
             '<ol class="contents">']
    for part_label, chaps in groups:
        if part_label:
            parts.append('<li class="part">%s</li>' % esc(part_label))
        for chap in chaps:
            cid = chap["id"]
            if chap.get("kind") == "epigraph":
                parts.append('<li class="epig"><a href="%s.xhtml">%s</a></li>'
                             % (cid, esc(chap["title_en"])))
                continue
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
        '<i>%(title_zh)s</i> (<i>%(title_en)s</i>), made from the digital '
        'source edition.</p>'
        '<p class="note">The source text was translated in full; a '
        'paragraph-by-paragraph bilingual audit file exists alongside this '
        'edition for anyone who wants to check the workings. Names follow pinyin '
        'except where an English conventional form exists. Renderings marked '
        '"provisional" in the glossary are romanizations not found attested in '
        'English-language scholarship. Notes are the translator\'s throughout, '
        'kept distinct from any notes the source itself carries; where a passage '
        'is genuinely ambiguous the choice is stated in a note and nothing is '
        'invented to smooth it over.</p>'
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
    }
    structure = [c for c in book.get("structure", []) if c.get("id", "").startswith("ch")]
    if not structure:
        sys.exit("no chapters in book.json structure")

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
    scenes_by_chap = load_json("scenes.json", {})

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

    # cover: reproduce the source's own cover image verbatim (NOT through the
    # figure pipeline, which greyscales and re-encodes). A dedicated cover page
    # first in the spine, plus the manifest cover-image property and the legacy
    # <meta name="cover"> below, so the Apple Books and Kindle libraries both
    # show it and read the title from the metadata.
    cover_img = book.get("cover", "cover.jpeg")
    cover_src = os.path.join(FIGS, cover_img)
    have_cover = os.path.exists(cover_src)
    cover_media = {"jpg": "image/jpeg", "jpeg": "image/jpeg",
                   "png": "image/png"}.get(cover_img.rsplit(".", 1)[-1].lower(),
                                           "image/jpeg")
    if have_cover:
        shutil.copy(cover_src, os.path.join(oebps, "images", cover_img))
        with open(os.path.join(oebps, "cover.xhtml"), "w") as fh:
            fh.write(
                '<?xml version="1.0" encoding="utf-8"?>\n'
                '<!DOCTYPE html>\n'
                '<html xmlns="http://www.w3.org/1999/xhtml" '
                'xmlns:epub="http://www.idpf.org/2007/ops" lang="en">\n'
                '<head><meta charset="utf-8"/><title>Cover</title>'
                '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
                '<body class="cover" epub:type="cover">'
                '<img src="images/%s" alt="%s"/></body></html>\n'
                % (esc(cover_img), esc(meta["title_en"])))

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
        if chap["id"] in translated and chap.get("kind") == "epigraph":
            body, ids = render_epigraph(md_of(chap["id"]))
        elif chap["id"] in translated:
            section_ids = [s["id"] for s in chap.get("sections", [])]
            sub_ids = [sub["id"] for s in chap.get("sections", [])
                       for sub in s.get("subsections", [])]
            body, ids = render_body(md_of(chap["id"]), section_ids, sub_ids,
                                    figspec.get(chap["id"], []),
                                    notes_by_chap.get(chap["id"], []),
                                    counter, doc,
                                    scenes=scenes_by_chap.get(chap["id"]))
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
    have_backmatter = bool(back_matter.get("colophon"))
    if have_backmatter:
        write(os.path.join(oebps, "colophon.xhtml"),
              render_colophon(back_matter), "Colophon")

    # spine order: cover first (if any), then every chapter (translated or
    # skeleton) is in the spine.
    docs = []
    if have_cover:
        docs.append(("cover.xhtml", "Cover"))
    docs += [("titlepage.xhtml", "Title Page"),
             ("contents.xhtml", "Contents")]
    docs += [(c["id"] + ".xhtml", c["title_en"]) for c in structure]
    docs += [("notes.xhtml", "Notes"),
             ("backmatter.xhtml", "Translator's Note and Glossary")]
    if have_backmatter:
        docs += [("colophon.xhtml", "Colophon")]

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
        nav_items += ['<li><a href="colophon.xhtml">Colophon</a></li>']
    nav = ('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
           + "".join(nav_items) + "</ol></nav>"
           '<nav epub:type="landmarks" hidden="hidden"><ol>'
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
    if have_cover:
        items.append('<item id="cover-image" href="images/%s" media-type="%s" '
                     'properties="cover-image"/>' % (cover_img, cover_media))
    for i, (f, _) in enumerate(docs, 1):
        items.append('<item id="d%d" href="%s" media-type="application/xhtml+xml"/>' % (i, f))
    for i, f in enumerate(manifest_figs, 1):
        items.append('<item id="fig%d" href="images/%s" media-type="image/png"/>' % (i, f))
    spine = "".join('<itemref idref="d%d"/>' % i for i in range(1, len(docs) + 1))

    # Metadata tuned so both the Apple Books and the Kindle libraries show the
    # document as "A Thousand Li of Rivers and Mountains" by Sun Ganlu, in
    # English, with the cover. dc:title is the library display name; the
    # refines give a sort title and the author's file-as/role; the legacy
    # <meta name="cover"> is what older Kindle tooling reads for the cover.
    year = str(meta["year"]) if meta["year"] else ""
    cover_meta = ('<meta name="cover" content="cover-image"/>'
                  if have_cover else "")
    date_meta = ('<dc:date>%s</dc:date>' % esc(year)) if year else ""
    with open(os.path.join(oebps, "content.opf"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>'
                 '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
                 'unique-identifier="pub-id" xml:lang="en" '
                 'prefix="rendition: http://www.idpf.org/vocab/rendition/#">'
                 '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
                 "<dc:identifier id=\"pub-id\">%s</dc:identifier>"
                 '<dc:title id="title">%s</dc:title>'
                 '<meta refines="#title" property="title-type">main</meta>'
                 '<meta refines="#title" property="file-as">%s</meta>'
                 "<dc:language>en</dc:language>"
                 '<dc:creator id="creator">%s</dc:creator>'
                 '<meta refines="#creator" property="role" '
                 'scheme="marc:relators">aut</meta>'
                 '<meta refines="#creator" property="file-as">%s</meta>'
                 "%s%s"
                 '<meta property="dcterms:modified">2026-01-01T00:00:00Z</meta>'
                 "</metadata><manifest>%s</manifest>"
                 "<spine toc=\"ncx\">%s</spine></package>"
                 % (meta["uid"], esc(meta["title_en"]), esc(meta["title_en"]),
                    esc(meta["author_en"]), esc(meta["author_en"]),
                    date_meta, cover_meta, "".join(items), spine))

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
