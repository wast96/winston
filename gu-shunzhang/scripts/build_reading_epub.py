#!/usr/bin/env python3
"""Build the cumulative reading edition of 特務工作之理論與實際.

Driven entirely by book.json (a dict with a "structure" list of chapters, each
with its sections). One XHTML per TRANSLATED chapter (a chapter is translated
when out/<id>_reading.md exists), all in one spine, one cumulative EPUB
out/gushunzhang.epub.

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

Usage: build_reading_epub.py out/gushunzhang.epub
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

# Fonts for the generated cover (present on this box; degrade gracefully).
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
CJK_FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"


def make_cover(dest, title_en, title_zh, author_en, author_zh):
    """Generate a simple, clean typographic cover (1600x2560, Kindle/Books
    friendly ratio). Returns True on success, False if PIL is unavailable."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False
    W, H = 1600, 2560
    bg, ink, gold = (18, 22, 30), (238, 234, 226), (176, 141, 87)
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    def font(path, size):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            return ImageFont.load_default()

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
    centered(["Annotated English Translation"], font(SERIF, 52), H - 360,
             gold, 0)
    d.rectangle([margin, H - 216, W - margin, H - 210], fill=gold)
    img.save(dest, format="PNG", optimize=True)
    return True


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


def render_contents(structure, translated, sec_done=None):
    """The visible full map: every chapter and section, translated ones linked
    down to the section, the rest marked 'not yet translated'.

    sec_done maps a chapter id to the set of its section ids that are actually
    present in that chapter's reading doc. A chapter translated a batch at a
    time (ch6 runs across three batches) is itself linked, but only its
    completed sections are deep-linked; the sections still pending are shown,
    honestly, as 'not yet translated' even though the chapter file exists."""
    sec_done = sec_done or {}
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
            done_secs = sec_done.get(cid)
            for sec in chap["sections"]:
                linked = done and (done_secs is None or sec["id"] in done_secs)
                if linked:
                    parts.append('<li class="sec"><a href="%s.xhtml#%s">%s</a></li>'
                                 % (cid, esc(sec["id"]), esc(sec["title_en"])))
                else:
                    parts.append('<li class="sec"><span class="pending">%s '
                                 '&#183; not yet translated</span></li>'
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
    return (
        '<h1>Errata</h1>'
        '<p class="note">The book prints a publisher\'s errata table '
        '(<span lang="zh-Hant">勘誤表</span>) on its final leaf. It is reproduced '
        'here in full. Its columns give, for each correction, the printed folio, '
        'the line, the character position within that line, and the fix &#8212; '
        'a dropped character to be inserted, or a misprinted character to be '
        'replaced. Every correction has been checked against this translation. '
        'The two that fall within Chapter&#160;8 (folios&#160;233 and&#160;236) '
        'are applied and are reflected in the reading text; the remainder fall on '
        'earlier chapters, whose translation &#8212; made by reading the scanned '
        'characters for sense &#8212; already follows the corrected readings. The '
        'entry for folio&#160;206 directs that a clause and a diagram of the '
        'Soviet G.P.U.\'s relationship to the army be added; that diagram is '
        'reproduced in Chapter&#160;7.</p>'
        '<table class="errata"><tr><th>Folio</th><th>Printed page</th>'
        '<th>Location</th><th>Correction</th></tr>%s</table>'
        % "".join(rows))


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
        '<p class="note">This edition is complete: all eight chapters are '
        'translated, together with the publisher\'s errata table and colophon, '
        'reproduced as back matter. One physical gap remains that no translation '
        'can close: the final leaf of the book &#8212; printed folio&#160;237, '
        'which would have carried the last sentence or two of Chapter&#160;8 '
        '&#8212; is missing from the library scan, where a duplicate of '
        'folio&#160;235 was fed in its place. The text therefore breaks off, as '
        'the scan does, in the middle of a closing quotation; nothing has been '
        'invented to bridge the gap. The publisher\'s errata correct nothing '
        'beyond folio&#160;236, so what is lost is at most a sentence or two.</p>'
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
        "md": book.get("metadata", {}),
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

    # A chapter may be translated a batch at a time (ch6 spans three batches):
    # its reading doc carries only the '### ' section headings done so far, and
    # render_body assigns section ids to them in book.json order. Record which
    # section ids are actually present so the contents page deep-links only
    # those and shows the rest as pending, instead of pointing at anchors that
    # do not exist yet (which qa_epub rightly rejects).
    sec_done = {}
    for chap in chapters:
        n_secs = sum(1 for l in open(md_of(chap["id"]))
                     if l.startswith("### "))
        sec_done[chap["id"]] = {s["id"]
                                for s in chap.get("sections", [])[:n_secs]}

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

    # cover image + cover page (Kindle and Apple Books both want a real cover)
    have_cover = make_cover(os.path.join(oebps, "images", "cover.png"),
                            meta["title_en"], meta["title_zh"],
                            meta["author_en"], meta["author_zh"])
    if have_cover:
        write(os.path.join(oebps, "cover.xhtml"),
              '<div style="text-align:center;margin:0;padding:0">'
              '<img src="images/cover.png" alt="%s" '
              'style="max-width:100%%;height:auto"/></div>'
              % esc(meta["title_en"]), "Cover")

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
          render_contents(structure, translated, sec_done), "Contents")

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

    back_matter = load_json("back_matter.json", {})
    have_backmatter = bool(back_matter.get("errata_rows") or
                           back_matter.get("colophon"))
    if have_backmatter:
        write(os.path.join(oebps, "errata.xhtml"),
              render_errata(back_matter), "Errata")
        write(os.path.join(oebps, "colophon.xhtml"),
              render_colophon(back_matter), "Colophon")

    # spine order (cover first, so Kindle/Books open on it)
    docs = []
    if have_cover:
        docs.append(("cover.xhtml", "Cover"))
    docs += [("titlepage.xhtml", "Title Page"),
             ("contents.xhtml", "Contents")]
    docs += [(c["id"] + ".xhtml", c["title_en"]) for c in chapters]
    docs += [("pending.xhtml", "Not yet translated"),
             ("notes.xhtml", "Notes"),
             ("backmatter.xhtml", "Translator's Note and Glossary")]
    if have_backmatter:
        docs += [("errata.xhtml", "Errata"), ("colophon.xhtml", "Colophon")]

    # e-reader nav: full chapter-level TOC (all eight), pending ones point at
    # the placeholder so they are navigable and honest.
    nav_items = ['<li><a href="titlepage.xhtml">Title Page</a></li>',
                 '<li><a href="contents.xhtml">Contents</a></li>']
    for chap in structure:
        cid = chap["id"]
        if cid in translated:
            nav_items.append('<li><a href="%s.xhtml">%s</a>'
                             % (cid, esc(chap["title_en"])))
        else:
            nav_items.append('<li><a href="pending.xhtml">%s '
                             '(not yet translated)</a>'
                             % esc(chap["title_en"]))
        # section-level sub-entries: linked when the section is done, shown as
        # pending otherwise, so the reader can jump straight to any section.
        if chap.get("sections"):
            done_secs = sec_done.get(cid, set())
            subs = []
            for sec in chap["sections"]:
                if cid in translated and sec["id"] in done_secs:
                    subs.append('<li><a href="%s.xhtml#%s">%s</a></li>'
                                % (cid, esc(sec["id"]), esc(sec["title_en"])))
                else:
                    subs.append('<li><a href="%s">%s (not yet translated)</a></li>'
                                % ("%s.xhtml" % cid if cid in translated
                                   else "pending.xhtml", esc(sec["title_en"])))
            nav_items.append("<ol>" + "".join(subs) + "</ol>")
        nav_items.append("</li>")
    nav_items += ['<li><a href="notes.xhtml">Notes</a></li>',
                  '<li><a href="backmatter.xhtml">Translator\'s Note and '
                  'Glossary</a></li>']
    if have_backmatter:
        nav_items += ['<li><a href="errata.xhtml">Errata</a></li>',
                      '<li><a href="colophon.xhtml">Colophon</a></li>']
    cover_landmark = ('<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>'
                      if have_cover else "")
    nav = ('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
           + "".join(nav_items) + "</ol></nav>"
           '<nav epub:type="landmarks" hidden="hidden"><ol>'
           + cover_landmark +
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
    if have_cover:
        items.append('<item id="cover-image" href="images/cover.png" '
                     'media-type="image/png" properties="cover-image"/>')
    for i, (f, _) in enumerate(docs, 1):
        items.append('<item id="d%d" href="%s" media-type="application/xhtml+xml"/>'
                     % (i, f))
    for i, f in enumerate(manifest_figs, 1):
        items.append('<item id="fig%d" href="images/%s" media-type="image/png"/>' % (i, f))
    spine = "".join('<itemref idref="d%d"/>' % i for i in range(1, len(docs) + 1))

    # full metadata for Kindle / Apple Books
    md = meta.get("md", {})
    m = ["<dc:identifier id=\"pub-id\">%s</dc:identifier>" % meta["uid"],
         '<dc:title id="t">%s</dc:title>' % esc(meta["title_en"]),
         '<meta refines="#t" property="title-type">main</meta>']
    if md.get("title_file_as"):
        m.append('<meta refines="#t" property="file-as">%s</meta>'
                 % esc(md["title_file_as"]))
    if meta["title_zh"]:
        m.append('<dc:title id="t2" xml:lang="zh">%s</dc:title>'
                 % esc(meta["title_zh"]))
        m.append('<meta refines="#t2" property="title-type">main</meta>')
    m.append('<dc:language>%s</dc:language>' % esc(md.get("language", "en")))
    m.append('<dc:creator id="au">%s</dc:creator>' % esc(meta["author_en"]))
    m.append('<meta refines="#au" property="role" scheme="marc:relators">aut</meta>')
    if md.get("author_file_as"):
        m.append('<meta refines="#au" property="file-as">%s</meta>'
                 % esc(md["author_file_as"]))
    m.append('<meta refines="#au" property="display-seq">1</meta>')
    if md.get("translator"):
        m.append('<dc:contributor id="tr">%s</dc:contributor>'
                 % esc(md["translator"]))
        m.append('<meta refines="#tr" property="role" scheme="marc:relators">trl</meta>')
    if md.get("publisher"):
        m.append('<dc:publisher>%s</dc:publisher>' % esc(md["publisher"]))
    if md.get("pubdate"):
        m.append('<dc:date>%s</dc:date>' % esc(md["pubdate"]))
    if md.get("description"):
        m.append('<dc:description>%s</dc:description>' % esc(md["description"]))
    for subj in md.get("subjects", []):
        m.append('<dc:subject>%s</dc:subject>' % esc(subj))
    if md.get("source_ref"):
        m.append('<dc:source>%s</dc:source>' % esc(md["source_ref"]))
    if md.get("rights"):
        m.append('<dc:rights>%s</dc:rights>' % esc(md["rights"]))
    stamp = (md.get("pubdate") or "2026-01-01")[:10] + "T00:00:00Z"
    m.append('<meta property="dcterms:modified">%s</meta>' % stamp)
    if have_cover:
        m.append('<meta name="cover" content="cover-image"/>')

    guide = ""
    if have_cover:
        guide += '<reference type="cover" title="Cover" href="cover.xhtml"/>'
    guide += ('<reference type="toc" title="Contents" href="contents.xhtml"/>'
              '<reference type="text" title="Begin Reading" href="%s"/>'
              % (chapters[0]["id"] + ".xhtml"))

    with open(os.path.join(oebps, "content.opf"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="utf-8"?>'
                 '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
                 'unique-identifier="pub-id" xml:lang="en"><metadata '
                 'xmlns:dc="http://purl.org/dc/elements/1.1/">'
                 "%s</metadata><manifest>%s</manifest>"
                 '<spine toc="ncx" page-progression-direction="ltr">%s</spine>'
                 "<guide>%s</guide></package>"
                 % ("".join(m), "".join(items), spine, guide))

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
         os.path.join(ROOT, "out", "gushunzhang.epub"))
