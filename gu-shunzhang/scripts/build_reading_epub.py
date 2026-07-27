#!/usr/bin/env python3
"""Build the cumulative reading edition of 特務工作之理論與實際.

Driven entirely by book.json (a dict with a "structure" list of chapters, each
with its sections). One XHTML per TRANSLATED chapter (a chapter is translated
when out/<id>_reading.md exists), all in one spine, one cumulative EPUB
out/theory-practice.epub.

Every build ships a FULL table of contents covering all eight chapters and
their thirty-seven sections: translated chapters are linked (down to the
section), untranslated ones are shown, visibly, as "not yet translated". So the
whole shape of the book is always on view, and the reader can see what is done.

Footnote numbering is CONTINUOUS across the translated chapters (notes.json is
keyed by chapter id). The builder REFUSES to build if any note anchor fails to
match its prose (a silent-skip builder once lost twelve notes on a sibling
project). Note anchors are inserted BEFORE the italic markup substitution, or
the substitution would eat them.

Reading markdown per chapter uses: '## ' chapter title (h1), '### ' section
(h2, given the section's book.json id), '#### ' subsection (h3); every other
non-blank line is a paragraph.

Usage: build_reading_epub.py out/theory-practice.epub
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
span.pending { color: #999; font-style: italic; }
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


def render_body(md_path, section_ids, figures, notes, counter, doc):
    """Render one chapter's reading markdown to XHTML.

    section_ids is the chapter's list of book.json section ids, consumed in
    order as '### ' section headings are met, so the contents page can deep-link
    each section.
    """
    out, first = [], True
    sids = list(section_ids)
    for raw in open(md_path):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#### "):
            out.append("<h3>%s</h3>"
                       % insert_notes(esc(line[5:]), notes, counter, doc))
            first = True
            continue
        if line.startswith("### "):
            sid = sids.pop(0) if sids else None
            idattr = ' id="%s"' % esc(sid) if sid else ""
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
    return "\n".join(out)


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


def render_contents(structure, translated):
    """The visible full map: every chapter and section, translated ones linked
    down to the section, the rest marked 'not yet translated'."""
    parts = ['<h1>Contents</h1>',
             '<p class="note">The complete book runs to eight chapters and '
             'thirty-seven sections. Chapters already translated are linked; '
             'the rest are shown here so the whole shape of the book is on '
             'view, and will be linked as they are completed.</p>',
             '<ol class="contents">']
    for chap in structure:
        cid = chap["id"]
        done = cid in translated
        if done:
            parts.append('<li class="chap"><a href="%s.xhtml">%s</a></li>'
                         % (cid, esc(chap["title_en"])))
        else:
            parts.append('<li class="chap">%s '
                         '<span class="pending">&#183; not yet translated</span></li>'
                         % esc(chap["title_en"]))
        if chap.get("sections"):
            parts.append('<ol>')
            for sec in chap["sections"]:
                if done:
                    parts.append('<li class="sec"><a href="%s.xhtml#%s">%s</a></li>'
                                 % (cid, esc(sec["id"]), esc(sec["title_en"])))
                else:
                    parts.append('<li class="sec"><span class="pending">%s</span></li>'
                                 % esc(sec["title_en"]))
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


def translator_note(meta, n_chapters):
    return (
        '<h1>Translator\'s Note</h1>'
        '<p class="note">This is an English translation of Gu Shunzhang\'s '
        '<i>%(title_zh)s</i> (<i>The Theory and Practice of Secret Service '
        'Work</i>), a training manual of intelligence tradecraft printed in '
        '%(year)s. The source is an image-only library scan from the National '
        'Central Library, Taiwan, with no digital text; a round library seal '
        'is stamped across the middle of many pages.</p>'
        '<p class="note">The text was recovered by optical character '
        'recognition on the vertical, right-to-left, Traditional-character '
        'columns, and then read character by character against magnified images '
        'of the physical pages. Every proper name, every number, and every '
        'passage the machine and the eye disagreed on was checked against the '
        'scan rather than trusted to the OCR. Two independent translation passes '
        'and a round-trip back-translation were run over the argumentative '
        'passages to catch silent errors and omissions; a bilingual audit file, '
        'keyed paragraph by paragraph to the Chinese, exists alongside this '
        'edition for anyone who wants to check the workings.</p>'
        '<p class="note">This is an expository manual, not narrative history, '
        'and the translation keeps its plain, ordered, instructional voice. The '
        'period vocabulary of intelligence work is preserved rather than '
        'modernised: 特務 as "secret service" or "secret agent" (not flattened '
        'to "spy"), 非常 as "extraordinary" in the sense of out-of-the-ordinary, '
        'and so on. Names follow pinyin except where an English conventional '
        'form exists (Chiang Kai-shek, Sun Yat-sen). Renderings marked '
        '"provisional" in the glossary are romanizations of my own that I could '
        'not find attested in English-language scholarship. Notes are the '
        'translator\'s throughout; the book carries none of its own.</p>'
        '<p class="note">The author is no neutral witness. Gu Shunzhang built '
        'the Chinese Communists\' secret service and then defected to the '
        'Nationalists in 1931; this manual, written for his new masters, sets '
        'down the craft he had turned. It should be read as what it is &#8212; '
        'a defector\'s handbook, partisan and self-interested &#8212; and not '
        'as a disinterested account.</p>'
        '<p class="note">This build contains %(n)s of the eight chapters; the '
        'rest follow in later builds.</p>'
        % {"title_zh": esc(meta["title_zh"]), "year": meta["year"],
           "n": n_chapters})


def write(path, body, title):
    with open(path, "w") as fh:
        fh.write(XHTML % {"title": esc(title), "body": body})


def main(epub_path):
    book = load_json("book.json", {})
    meta = {
        "title_en": book.get("title_en", "The Theory and Practice of Secret "
                                         "Service Work"),
        "title_zh": book.get("title_zh", ""),
        "author_en": book.get("author_en", "Gu Shunzhang"),
        "author_zh": book.get("author_zh", ""),
        "year": book.get("year", 1933),
        "uid": "urn:uuid:gu-shunzhang-theory-practice-1",
    }
    structure = [c for c in book.get("structure", []) if c.get("id", "").startswith("ch")]
    if not structure:
        sys.exit("no chapters in book.json structure")

    def md_of(cid):
        return os.path.join(ROOT, "out", "%s_reading.md" % cid)

    chapters = [c for c in structure if os.path.exists(md_of(c["id"]))]
    translated = {c["id"] for c in chapters}
    if not chapters:
        sys.exit("no chapter reading markdown found (out/<id>_reading.md)")

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
    write(os.path.join(oebps, "titlepage.xhtml"),
          '<div class="tp"><h1>%s</h1>'
          '<p lang="zh-Hant">%s</p>'
          '<p>%s &#183; <span lang="zh-Hant">%s</span></p>'
          '<p class="note">A training manual of intelligence tradecraft, %d</p>'
          '<p class="note">English translation</p></div>'
          % (esc(meta["title_en"]), esc(meta["title_zh"]),
             esc(meta["author_en"]), esc(meta["author_zh"]), meta["year"]),
          meta["title_en"])

    # contents map
    write(os.path.join(oebps, "contents.xhtml"),
          render_contents(structure, translated), "Contents")

    # a single placeholder that pending chapter links target in the nav
    write(os.path.join(oebps, "pending.xhtml"),
          '<h1>Not yet translated</h1>'
          '<p class="note">This chapter has not yet been translated. See the '
          '<a href="contents.xhtml">contents</a> for the whole plan of the '
          'book and what is complete.</p>', "Not yet translated")

    # chapter bodies
    counter = [0]
    for chap in chapters:
        doc = chap["id"] + ".xhtml"
        section_ids = [s["id"] for s in chap.get("sections", [])]
        body = render_body(md_of(chap["id"]), section_ids,
                           figspec.get(chap["id"], []),
                           notes_by_chap.get(chap["id"], []),
                           counter, doc)
        write(os.path.join(oebps, doc), body, chap["title_en"])

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

    # spine order
    docs = [("titlepage.xhtml", "Title Page"),
            ("contents.xhtml", "Contents")]
    docs += [(c["id"] + ".xhtml", c["title_en"]) for c in chapters]
    docs += [("pending.xhtml", "Not yet translated"),
             ("notes.xhtml", "Notes"),
             ("backmatter.xhtml", "Translator's Note and Glossary")]

    # e-reader nav: full chapter-level TOC (all eight), pending ones point at
    # the placeholder so they are navigable and honest.
    nav_items = ['<li><a href="titlepage.xhtml">Title Page</a></li>',
                 '<li><a href="contents.xhtml">Contents</a></li>']
    for chap in structure:
        if chap["id"] in translated:
            nav_items.append('<li><a href="%s.xhtml">%s</a></li>'
                             % (chap["id"], esc(chap["title_en"])))
        else:
            nav_items.append('<li><a href="pending.xhtml">%s '
                             '(not yet translated)</a></li>'
                             % esc(chap["title_en"]))
    nav_items += ['<li><a href="notes.xhtml">Notes</a></li>',
                  '<li><a href="backmatter.xhtml">Translator\'s Note and '
                  'Glossary</a></li>']
    nav = ('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
           + "".join(nav_items) + "</ol></nav>"
           '<nav epub:type="landmarks" hidden="hidden"><ol>'
           '<li><a epub:type="titlepage" href="titlepage.xhtml">Title Page</a></li>'
           '<li><a epub:type="toc" href="contents.xhtml">Contents</a></li>'
           '<li><a epub:type="bodymatter" href="%s">Begin Reading</a></li>'
           "</ol></nav>" % (chapters[0]["id"] + ".xhtml"))
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

    with open(os.path.join(oebps, "content.opf"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>'
                 '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
                 'unique-identifier="pub-id"><metadata '
                 'xmlns:dc="http://purl.org/dc/elements/1.1/">'
                 "<dc:identifier id=\"pub-id\">%s</dc:identifier>"
                 "<dc:title>%s</dc:title><dc:language>en</dc:language>"
                 "<dc:creator>%s</dc:creator>"
                 '<meta property="dcterms:modified">2026-01-01T00:00:00Z</meta>'
                 "</metadata><manifest>%s</manifest>"
                 "<spine toc=\"ncx\">%s</spine></package>"
                 % (meta["uid"], esc(meta["title_en"]), esc(meta["author_en"]),
                    "".join(items), spine))

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
         os.path.join(ROOT, "out", "theory-practice.epub"))
