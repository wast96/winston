#!/usr/bin/env python3
"""Build the reading edition: English prose, no page furniture, no inline
flags. The verification layer lives in back matter (translator's note +
glossary); the bilingual audit files stay outside the EPUB entirely.

Generalized for the full book: one XHTML per chapter (prologue + ch01..ch15),
all in one spine, one cumulative EPUB. Chapters are registered in book.json;
entries whose markdown does not exist yet are skipped, so interim builds
work at any point in the run.

Note numbering is CONTINUOUS across the whole book (decision recorded in
PROGRESS.md); ids ref{n}/note{n} are globally unique and the notes page
groups bodies under chapter headings. notes.json is a dict keyed by chapter
id. figures.json is a dict keyed by chapter id.

Usage: build_reading_epub.py out/wang-yaqiao.epub
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

META = {
    "title": "China's King of Assassins",
    "subtitle": "Wang Yaqiao",
    "title_full": "China's King of Assassins: Wang Yaqiao",
    "title_zh": "中国暗杀王：王亚樵",
    "author": "Dou Yingtai",
    "author_zh": "窦应泰",
    "author_sort": "Dou, Yingtai",
    "publisher": "Tuanjie Publishing House (团结出版社), Beijing, 2007",
    "isbn": "978-7-80130-758-3",
    "uid": "urn:uuid:wang-yaqiao-full-book-1",
    "language": "en",
    "date": "2007",
    "description": ("A popular biography of Wang Yaqiao (1889–1936), the "
                    "Republican-era assassin who rose from rural Anhui to lead "
                    "the Hatchet Gang and wage a decade-long campaign of "
                    "political killings against Chiang Kai-shek's regime. "
                    "Translated from the Chinese with historical annotations."),
    "subjects": ["China -- History -- Republic, 1912-1949",
                 "Wang, Yaqiao, 1889-1936",
                 "Assassins -- China -- Biography",
                 "Political violence -- China -- History"],
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
h3.notechap { margin-top: 2em; font-style: italic; }
p.dateline { text-indent: 0; font-style: italic; color: #666;
             font-size: 0.95em; margin: -0.8em 0 1.6em; }
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
    """Downsample a figure crop for the reading edition. Returns False if
    Pillow is unavailable, so the caller can fall back to a plain copy."""
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


def insert_notes(paragraph, notes, counter, doc, only_exact=False):
    """Attach a superscript reference after each note's anchor phrase.

    Candidates are ordered by where their reference will actually LAND -- the
    end of the anchor, not its start. Sorting by start position looks right
    until one anchor contains another ("Lushan" inside "Shanghai, Nanjing and
    Lushan, March to June 1931"): the containing anchor starts first but ends
    last, so its marker renders after the shorter one's and the numbering runs
    backwards. Sorting by end position makes the numbers follow the reader's
    eye in every case.

    Anchors are matched against the text BEFORE any markup substitution (the
    substitutions would otherwise eat the anchors) and after HTML escaping,
    same as the prose itself.

    only_exact restricts matching to a note whose anchor is the whole string.
    Translator-supplied text (the datelines) passes this so that a general
    prose note cannot be captured by our own insertion and stolen from the
    author's first use of the term.
    """
    hits = []
    for note in notes:
        if note.get("used"):
            continue
        if only_exact:
            if note["anchor"] == paragraph:
                hits.append((len(paragraph), note))
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


def render_notes_page(chapters, notes_by_chap):
    parts = ['<h1>Notes</h1>',
             '<p class="note">Each number links back to its place in the '
             'text. Notes marked as uncertain are places where the scan is '
             'damaged and my reading is inference rather than sight.</p>']
    any_used = False
    for chap in chapters:
        used = sorted([n for n in notes_by_chap.get(chap["id"], [])
                       if n.get("used")], key=lambda x: x["n"])
        if not used:
            continue
        any_used = True
        parts.append('<h3 class="notechap">%s</h3>' % esc(chap["nav"]))
        for note in used:
            parts.append(
                '<div class="endnote" id="note%d" epub:type="footnote">'
                '<p><a class="backref" href="%s#ref%d">%d.</a> %s</p></div>'
                % (note["n"], note["doc"], note["n"], note["n"], note["note"]))
    if not any_used:
        parts.append("<p>No notes.</p>")
    return "\n".join(parts)


def render_body(md_path, figures, notes, counter, doc, dateline=None):
    """Render one chapter.

    `dateline` is the TRANSLATOR'S inference, not the author's text: the book
    opens only some chapters with a date, and leaves the reader to carry the
    chronology forward from wherever it was last stated. Where we supply one
    it is set apart typographically and carries a note saying it was added
    and how sure of it we are, so it can never be mistaken for the original.
    """
    out, first = [], True
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
            if dateline:
                # through insert_notes so a note anchored to the dateline
                # text attaches its reference here
                out.append('<p class="dateline">[%s]</p>'
                           % insert_notes(esc(dateline), notes, counter, doc,
                                          only_exact=True))
            first = True
            continue
        if line.startswith("### "):
            # Section headings can legitimately carry a note: several are
            # translation notes ON the heading, flagging how the book's own
            # table of contents words it. Run them through insert_notes so
            # such a note attaches here instead of being dropped.
            out.append("<h3>%s</h3>"
                       % insert_notes(esc(line[4:]), notes, counter, doc))
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
        text = insert_notes(esc(line), notes, counter, doc)
        text = re.sub(r"\*([^*\n]+)\*", r"<i>\1</i>", text)
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
            note = (" · " + esc(rec["note"])) if rec.get("note") else ""
            status = ""
            if rec.get("status") == "provisional":
                status = " · <i>romanization mine; not found in English scholarship</i>"
            parts.append("<dt>%s <span lang=\"zh-Hans\">%s</span></dt>"
                         "<dd>%s%s%s</dd>"
                         % (esc(rec["en"]), esc(zh), esc(rec["pinyin"]), note, status))
        parts.append("</dl>")
    return "\n".join(parts)


TRANSLATOR_NOTE_BODY = """\
<p class="note">The source is a scanned book with no digital text. The text
was recovered by optical character recognition, read twice by independent
engine configurations and diffed, and corrected against magnified images of
the physical pages; every proper name and every load-bearing number that
appears here was verified against the scan rather than trusted to the OCR.
A complete bilingual audit file, keyed paragraph by paragraph to the Chinese
and marking every reading I could not fully confirm, exists alongside this
edition for anyone who wants to check the translation's workings.</p>
<p class="note">Where a chapter opens with a bracketed line of
place and date, that line is mine, not the author's, and a note on it says so
and gives my reasoning. Chapters that carry no such line are the ones the
author dated himself in his own opening sentence; there I have left his date
to stand alone rather than print a guess beside a fact.</p>
<p class="note">Renderings of names follow pinyin except where an English
conventional form exists (Chiang Kai-shek, Sun Yat-sen). Names marked in the
glossary as provisional are romanizations of my own that I could not find
attested in English-language scholarship. Notes state, where the book
crosses documented history, whether the book's claim is corroborated,
uncorroborated, or contradicted by the scholarship I could reach.</p>
<p class="note">The book is popular history in a novelistic key —
scenes, dialogue and inner thoughts are dramatized well beyond what any
source could support. The translation keeps that voice. It should be read as
storytelling built on a real life, not as documentation of one.</p>"""


def coverage_sentence(chapters):
    names = [c["nav"].split(":")[0] for c in chapters]
    if len(names) == 17:
        return ("<p class=\"note\">This edition contains the complete book: "
                "prologue and all fifteen chapters (printed pages 1 to 325 of "
                "the second edition, Tuanjie Publishing House, Beijing, "
                "2007).</p>")
    return ("<p class=\"note\">This build contains: %s. Remaining chapters "
            "follow in later builds.</p>" % ", ".join(esc(n) for n in names))


def write(path, body, title):
    with open(path, "w") as fh:
        fh.write(XHTML % {"title": esc(title), "body": body})


def main(epub_path):
    book = load_json("book.json", [])
    chapters = [c for c in book
                if os.path.exists(os.path.join(ROOT, c["file"]))]
    if not chapters:
        sys.exit("no chapter markdown found; check book.json")

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
            # Figure crops come off a 300 dpi render and run to several MB
            # each as PNG, which is absurd for a reading edition. Downsample
            # to a sane reading width and re-encode; these are halftone
            # photographs, so a little JPEG-style loss is invisible while the
            # file shrinks by an order of magnitude.
            if not shrink_image(src, dest):
                shutil.copy(src, dest)
            if spec["file"] not in manifest_figs:
                manifest_figs.append(spec["file"])

    cover = os.path.join(PNG, "cover.jpg")
    has_cover = os.path.exists(cover)
    if has_cover:
        shutil.copy(cover, os.path.join(oebps, "images", "cover.jpg"))

    with open(os.path.join(oebps, "style.css"), "w") as fh:
        fh.write(CSS)

    write(os.path.join(oebps, "titlepage.xhtml"),
          '<div class="tp"><h1>%s</h1>'
          '<p lang="zh-Hans">%s</p><p>%s · <span lang="zh-Hans">%s</span></p>'
          '<p class="note">%s</p><p class="note">English translation</p></div>'
          % (esc(META["title_full"]), esc(META["title_zh"]), esc(META["author"]),
             esc(META["author_zh"]), esc(META["publisher"])),
          META["title_full"])

    counter = [0]
    for chap in chapters:
        doc = chap["id"] + ".xhtml"
        body = render_body(os.path.join(ROOT, chap["file"]),
                           figspec.get(chap["id"], []),
                           notes_by_chap.get(chap["id"], []),
                           counter, doc, chap.get("dateline"))
        write(os.path.join(oebps, doc), body, chap["nav"])

    # A note whose anchor never matched is dropped without trace: no reference,
    # no body, and qa_epub stays green because refs and bodies still agree with
    # each other. Twelve notes went missing that way before this check existed.
    orphans = [(cid, n["anchor"]) for cid, lst in notes_by_chap.items()
               for n in lst if not n.get("used")]
    if orphans:
        sys.stderr.write("BUILD FAILED: %d note(s) never matched their anchor "
                         "and would be silently dropped:\n" % len(orphans))
        for cid, a in orphans:
            sys.stderr.write("  %-9s %s\n" % (cid, a[:88]))
        sys.exit(2)

    write(os.path.join(oebps, "notes.xhtml"),
          render_notes_page(chapters, notes_by_chap), "Notes")

    write(os.path.join(oebps, "backmatter.xhtml"),
          "<h1>Translator's Note</h1>"
          + coverage_sentence(chapters)
          + TRANSLATOR_NOTE_BODY
          + "<h1>Glossary of Names and Terms</h1>"
          + render_glossary(gloss),
          "Translator's Note")

    docs = [("titlepage.xhtml", "Title Page")]
    docs += [(c["id"] + ".xhtml", c["nav"]) for c in chapters]
    docs += [("notes.xhtml", "Notes"),
             ("backmatter.xhtml", "Translator's Note and Glossary")]

    first_body = chapters[0]["id"] + ".xhtml"
    nav = ('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
           + "".join('<li><a href="%s">%s</a></li>' % (f, esc(t)) for f, t in docs)
           + "</ol></nav>"
           '<nav epub:type="landmarks" hidden="hidden"><ol>'
           '<li><a epub:type="titlepage" href="titlepage.xhtml">Title Page</a></li>'
           '<li><a epub:type="bodymatter" href="%s">Begin Reading</a></li>'
           "</ol></nav>" % first_body)
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
                 % (META["uid"], esc(META["title_full"]), ncx))

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

    from datetime import datetime, timezone
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    subject_xml = "".join("<dc:subject>%s</dc:subject>" % esc(s)
                          for s in META.get("subjects", []))
    opf_meta = (
        '<?xml version="1.0" encoding="utf-8"?>'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
        'unique-identifier="pub-id">'
        '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" '
        'xmlns:opf="http://www.idpf.org/2007/opf">'
        '<dc:identifier id="pub-id">%(uid)s</dc:identifier>'
        '<dc:title id="main-title">%(title)s</dc:title>'
        '<meta refines="#main-title" property="title-type">main</meta>'
        '<dc:title id="subtitle">%(subtitle)s</dc:title>'
        '<meta refines="#subtitle" property="title-type">subtitle</meta>'
        '<meta refines="#subtitle" property="display-seq">2</meta>'
        '<dc:language>%(lang)s</dc:language>'
        '<dc:creator id="author">%(author)s</dc:creator>'
        '<meta refines="#author" property="role" scheme="marc:relators">aut</meta>'
        '<meta refines="#author" property="file-as">%(author_sort)s</meta>'
        '<dc:publisher>%(publisher)s</dc:publisher>'
        '<dc:source>ISBN %(isbn)s</dc:source>'
        '<dc:date>%(date)s</dc:date>'
        '<dc:description>%(description)s</dc:description>'
        '%(subjects)s'
        '<meta property="dcterms:modified">%(modified)s</meta>'
        '%(cover_meta)s'
        '</metadata>'
        '<manifest>%(manifest)s</manifest>'
        '<spine toc="ncx">%(spine)s</spine>'
        '</package>'
    )
    with open(os.path.join(oebps, "content.opf"), "w") as fh:
        fh.write(opf_meta % {
            "uid": META["uid"],
            "title": esc(META["title"]),
            "subtitle": esc(META.get("subtitle", "")),
            "lang": META.get("language", "en"),
            "author": esc(META["author"]),
            "author_sort": esc(META.get("author_sort", META["author"])),
            "publisher": esc(META["publisher"]),
            "isbn": META["isbn"],
            "date": META.get("date", ""),
            "description": esc(META.get("description", "")),
            "subjects": subject_xml,
            "modified": modified,
            "cover_meta": '<meta name="cover" content="cover"/>' if has_cover else "",
            "manifest": "".join(items),
            "spine": spine,
        })

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
    print("wrote", epub_path, "with %d chapters" % len(chapters))


if __name__ == "__main__":
    main(sys.argv[1])
