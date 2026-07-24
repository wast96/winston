#!/usr/bin/env python3
"""Build the reading edition: English prose, no page furniture, no inline
flags. The verification layer lives in back matter (translator's note +
term ledger); the bilingual audit file stays outside the EPUB entirely.

Usage: build_reading_epub.py out/ch1_s1_reading.md out/wang-yaqiao-ch1.epub
"""
import html
import json
import os
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(ROOT, "data", "figs")
PNG = os.path.join(ROOT, "data", "png")
BUILD = os.path.join(ROOT, "build")

META = {
    "title": "China's King of Assassins: Wang Yaqiao",
    "title_zh": "中国暗杀王：王亚樵",
    "author": "Dou Yingtai",
    "author_zh": "窦应泰",
    "publisher": "Tuanjie Publishing House (团结出版社), Beijing, 2007",
    "isbn": "978-7-80130-758-3",
    "uid": "urn:uuid:wang-yaqiao-ch1-pilot-2",
}

CSS = """\
body { font-family: serif; line-height: 1.6; margin: 1em 1.2em; }
h1 { font-size: 1.45em; margin: 1.4em 0 0.2em; font-weight: normal; }
h2 { font-size: 1.1em; margin: 0.2em 0 1.4em; font-weight: normal;
     color: #555; font-style: italic; }
h3 { font-size: 1.05em; margin: 1.8em 0 0.8em; }
p { margin: 0 0 0.85em; text-indent: 1.4em; }
p.first, p.note { text-indent: 0; }
p.note { font-size: 0.92em; color: #444; }
figure { margin: 1.6em auto; text-align: center; page-break-inside: avoid; }
figure img { max-width: 55%; }
figcaption { font-size: 0.85em; color: #444; margin-top: 0.5em; }
dl.gloss dt { font-weight: bold; margin-top: 0.7em; }
dl.gloss dd { margin: 0 0 0 1.2em; }
a.noteref { text-decoration: none; }
a.noteref sup { font-size: 0.72em; color: #7a1f1f; padding-left: 1px; }
div.endnote { margin: 0 0 1.05em; }
div.endnote p { text-indent: 0; font-size: 0.94em; }
a.backref { text-decoration: none; font-weight: bold; color: #7a1f1f; }
.tp { text-align: center; margin-top: 4em; }
.tp h1 { font-size: 1.7em; }
.tp p { text-indent: 0; }
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

# Figures keyed to the paragraph they should precede in the reading flow.
FIGURES = {
    "p0022-f1.png": {
        "before": "Hmph. Today is the day you die",
        "caption": "Chen Diaoyuan, Chairman of the Anhui Provincial "
                   "Government, appointed by Chiang Kai-shek. From the "
                   "original edition.",
        "alt": "Portrait of Chen Diaoyuan"},
    "p0028-f1.png": {
        "before": "Chiang Kai-shek sat frozen.",
        "caption": "Photograph inset at this point in the original edition; "
                   "no caption is legible in the scan.",
        "alt": "Photograph inset in the original edition"},
    "p0031-f1.png": {
        "before": "Only then did Bo Wenwei understand",
        "caption": "Bo Wenwei, elder of the 1911 Revolution, as identified "
                   "by the caption in the original edition.",
        "alt": "Portrait of Bo Wenwei"},
}


def esc(text):
    return html.escape(text, quote=False)


def load_notes():
    path = os.path.join(ROOT, "notes.json")
    if not os.path.exists(path):
        return []
    return json.load(open(path))


def insert_notes(paragraph, notes, counter):
    """Attach a superscript reference after each note's anchor phrase.

    Candidates are ordered by where they actually fall in the paragraph, so
    the numbering follows the reader's eye rather than the order the notes
    happen to sit in the source file. Anchors are matched against the plain
    text before escaping, so they are written the way the prose reads.
    """
    hits = []
    for note in notes:
        if note.get("used"):
            continue
        pos = paragraph.find(note["anchor"])
        if pos >= 0:
            hits.append((pos, note))
    for _, note in sorted(hits, key=lambda h: h[0]):
        counter[0] += 1
        note["n"] = counter[0]
        note["used"] = True
        ref = ('<a class="noteref" epub:type="noteref" id="ref%d" '
               'href="notes.xhtml#note%d"><sup>%d</sup></a>'
               % (note["n"], note["n"], note["n"]))
        paragraph = paragraph.replace(note["anchor"], note["anchor"] + ref, 1)
    return paragraph


def render_notes_page(notes):
    used = sorted([n for n in notes if n.get("used")], key=lambda x: x["n"])
    parts = ['<h1>Notes</h1>',
             '<p class="note">Each number links back to its place in the '
             'text. Notes marked as uncertain are places where the scan is '
             'damaged and my reading is inference rather than sight.</p>']
    for note in used:
        parts.append(
            '<div class="endnote" id="note%d" epub:type="footnote">'
            '<p><a class="backref" href="ch01.xhtml#ref%d">%d.</a> %s</p></div>'
            % (note["n"], note["n"], note["n"], note["note"]))
    if not used:
        parts.append("<p>No notes.</p>")
    return "\n".join(parts)


def render_body(md_path, figures, notes):
    out, first = [], True
    counter = [0]
    for raw in open(md_path):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            continue                      # book title lives on the title page
        if line.startswith("## "):
            parts = line[3:].split(": ", 1)
            if len(parts) == 2:
                out.append("<h1>%s</h1><h2>%s</h2>" % (esc(parts[0]), esc(parts[1])))
            else:
                out.append("<h1>%s</h1>" % esc(line[3:]))
            first = True
            continue
        if line.startswith("### "):
            out.append("<h3>%s</h3>" % esc(line[4:]))
            first = True
            continue
        for fig in figures:
            if not fig.get("placed") and fig["before"] in line[:80]:
                out.append(
                    '<figure><img src="images/%s" alt="%s"/>'
                    "<figcaption>%s</figcaption></figure>"
                    % (fig["file"], esc(fig["alt"]), esc(fig["caption"])))
                fig["placed"] = True
        # notes first: the italic substitution below would otherwise eat
        # any anchor phrase containing the markup
        text = insert_notes(esc(line), notes, counter)
        text = text.replace("*Dongzheng*", "<i>Dongzheng</i>")
        cls = ' class="first"' if first else ""
        out.append("<p%s>%s</p>" % (cls, text))
        first = False
    return "\n".join(out)


def render_glossary(gloss):
    parts = []
    for section, entries in gloss.items():
        if section.startswith("_"):
            continue
        parts.append("<h3>%s</h3><dl class=\"gloss\">"
                     % esc(section.replace("_", " ").title()))
        for zh, rec in sorted(entries.items(), key=lambda kv: kv[1]["pinyin"]):
            note = (" \u00b7 " + esc(rec["note"])) if rec.get("note") else ""
            parts.append("<dt>%s <span lang=\"zh-Hans\">%s</span></dt>"
                         "<dd>%s%s</dd>"
                         % (esc(rec["en"]), esc(zh), esc(rec["pinyin"]), note))
        parts.append("</dl>")
    return "\n".join(parts)


TRANSLATOR_NOTE = """\
<h1>Translator's Note</h1>
<p class="note">This edition contains Chapter One complete (all four
sections, printed pages 9 to 26 of the second edition, Tuanjie Publishing
House, Beijing, 2007). Chapters Two through Fifteen follow in later
builds.</p>
<p class="note">The source is a scanned book with no digital text. The text
was recovered by optical character recognition and corrected against
magnified images of the physical pages; every proper name that appears here
was verified against the scan rather than trusted to the OCR. A complete
bilingual audit file, keyed paragraph by paragraph to the Chinese and
marking every reading I could not fully confirm, exists alongside this
edition for anyone who wants to check the translation's workings.</p>
<p class="note">Two of the Hatchet Gang members named in this section, Wu
Hongtai and Xuan Jimin, do not appear in English-language scholarship that I
could find, so the romanizations are mine. Chen Diaoyuan's offices, Bo
Wenwei's command of the 33rd Army, and the gift of British mortars and Krupp
guns are the author's claims; the first two are consistent with the standard
histories, the third I have not confirmed.</p>
<p class="note">The book is popular history in a novelistic key \u2014
scenes, dialogue and inner thoughts are dramatized well beyond what any
source could support. The translation keeps that voice. It should be read as
storytelling built on a real life, not as documentation of one.</p>"""


def write(path, body, title):
    with open(path, "w") as fh:
        fh.write(XHTML % {"title": esc(title), "body": body})


def main(md_path, epub_path):
    if os.path.isdir(BUILD):
        shutil.rmtree(BUILD)
    oebps = os.path.join(BUILD, "OEBPS")
    os.makedirs(os.path.join(oebps, "images"))
    os.makedirs(os.path.join(BUILD, "META-INF"))

    gloss = json.load(open(os.path.join(ROOT, "glossary.json")))

    figures, manifest_figs = [], []
    fm = os.path.join(FIGS, "manifest.json")
    if os.path.exists(fm):
        for rec in json.load(open(fm)):
            spec = FIGURES.get(rec["file"])
            if not spec:
                continue
            shutil.copy(os.path.join(FIGS, rec["file"]),
                        os.path.join(oebps, "images", rec["file"]))
            manifest_figs.append(rec["file"])
            figures.append(dict(spec, file=rec["file"]))

    cover = os.path.join(PNG, "cover.jpg")
    has_cover = os.path.exists(cover)
    if has_cover:
        shutil.copy(cover, os.path.join(oebps, "images", "cover.jpg"))

    with open(os.path.join(oebps, "style.css"), "w") as fh:
        fh.write(CSS)

    write(os.path.join(oebps, "titlepage.xhtml"),
          '<div class="tp"><h1>%s</h1>'
          '<p lang="zh-Hans">%s</p><p>%s \u00b7 <span lang="zh-Hans">%s</span></p>'
          '<p class="note">%s</p><p class="note">English translation \u00b7 pilot edition</p></div>'
          % (esc(META["title"]), esc(META["title_zh"]), esc(META["author"]),
             esc(META["author_zh"]), esc(META["publisher"])),
          META["title"])

    notes = load_notes()
    write(os.path.join(oebps, "ch01.xhtml"),
          render_body(md_path, figures, notes), "Chapter One")
    write(os.path.join(oebps, "notes.xhtml"), render_notes_page(notes), "Notes")

    write(os.path.join(oebps, "backmatter.xhtml"),
          TRANSLATOR_NOTE
          + "<h1>Glossary of Names and Terms</h1>"
          + render_glossary(gloss),
          "Translator's Note")

    docs = [("titlepage.xhtml", "Title Page"),
            ("ch01.xhtml", "Chapter One: A First Assassination, Badly Begun"),
            ("notes.xhtml", "Notes"),
            ("backmatter.xhtml", "Translator's Note and Glossary")]

    nav = ('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
           + "".join('<li><a href="%s">%s</a></li>' % (f, esc(t)) for f, t in docs)
           + "</ol></nav>"
           '<nav epub:type="landmarks" hidden="hidden"><ol>'
           '<li><a epub:type="titlepage" href="titlepage.xhtml">Title Page</a></li>'
           '<li><a epub:type="bodymatter" href="ch01.xhtml">Begin Reading</a></li>'
           "</ol></nav>")
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
                 % (META["uid"], esc(META["title"]), ncx))

    items = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
             '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
             '<item id="css" href="style.css" media-type="text/css"/>']
    for i, (f, _) in enumerate(docs, 1):
        items.append('<item id="d%d" href="%s" media-type="application/xhtml+xml"/>' % (i, f))
    for i, f in enumerate(manifest_figs, 1):
        items.append('<item id="fig%d" href="images/%s" media-type="image/png"/>' % (i, f))
    if has_cover:
        items.append('<item id="cover" href="images/cover.jpg" '
                     'media-type="image/jpeg" properties="cover-image"/>')
    spine = "".join('<itemref idref="d%d"/>' % i for i in range(1, len(docs) + 1))

    with open(os.path.join(oebps, "content.opf"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>'
                 '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
                 'unique-identifier="pub-id"><metadata '
                 'xmlns:dc="http://purl.org/dc/elements/1.1/">'
                 "<dc:identifier id=\"pub-id\">%s</dc:identifier>"
                 "<dc:title>%s</dc:title><dc:language>en</dc:language>"
                 "<dc:creator>%s</dc:creator><dc:publisher>%s</dc:publisher>"
                 "<dc:source>ISBN %s</dc:source>"
                 '<meta property="dcterms:modified">2026-01-01T00:00:00Z</meta>'
                 "</metadata><manifest>%s</manifest><spine toc=\"ncx\">%s</spine></package>"
                 % (META["uid"], esc(META["title"]), esc(META["author"]),
                    esc(META["publisher"]), META["isbn"], "".join(items), spine))

    with open(os.path.join(BUILD, "META-INF", "container.xml"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>'
                 '<container version="1.0" '
                 'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                 '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                 'media-type="application/oebps-package+xml"/></rootfiles></container>')
    with open(os.path.join(BUILD, "mimetype"), "w") as fh:
        fh.write("application/epub+zip")

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
    print("wrote", epub_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
