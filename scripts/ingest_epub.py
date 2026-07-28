#!/usr/bin/env python3
"""Ingest a source-language EPUB: the first step, in place of render+OCR.

Unlike a scanned book, an EPUB already carries reliable digital text -- there is
no OCR, no page furniture, no folios. This script unpacks the source EPUB, reads
its spine in reading order, extracts the plain text and headings of each spine
document, counts the source characters (the natural size metric for Chinese),
pulls out the embedded images, and writes:

  data/src_epub/            the unzipped source (kept for reference)
  data/src/<NN>_<slug>.txt  plain text of each spine document, in order
  data/figs/<name>          every embedded image (for re-use as figures)
  out/INGEST.md             an outline report: spine item, headings, char count
  book.draft.json           a DRAFT book.json structure (one chapter per spine
                            document, sections from its <h2> headings, char
                            counts and a 'src' locator filled in)

Then author book.json from the draft: refine titles, add English titles, and
MERGE or SPLIT where the source's file boundaries do not match its logical
chapters (a spine file may hold several chapters, or one chapter may span
several files). Keep each unit's 'src' (the spine href, optionally with #anchor)
and 'chars' so the survey can size the batches.

Usage: ingest_epub.py [source.epub]
"""
import html
import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_EPUB = os.path.join(ROOT, "data", "src_epub")
SRC = os.path.join(ROOT, "data", "src")
FIGS = os.path.join(ROOT, "data", "figs")

OPF = "{http://www.idpf.org/2007/opf}"
CN = "{urn:oasis:names:tc:opendocument:xmlns:container}"


def strip_tags(xhtml):
    """Plain text from an XHTML string: drop script/style, turn block ends into
    newlines, unescape entities, collapse whitespace per line."""
    xhtml = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", xhtml)
    xhtml = re.sub(r"(?i)</(p|div|h[1-6]|li|br|tr|section)\s*>", "\n", xhtml)
    xhtml = re.sub(r"(?i)<br\s*/?>", "\n", xhtml)
    text = re.sub(r"(?s)<[^>]+>", "", xhtml)
    text = html.unescape(text)
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in text.splitlines()]
    return "\n".join(ln for ln in lines if ln)


def headings(xhtml):
    out = []
    for m in re.finditer(r"(?is)<h([1-4])[^>]*>(.*?)</h\1>", xhtml):
        level = int(m.group(1))
        txt = html.unescape(re.sub(r"(?s)<[^>]+>", "", m.group(2))).strip()
        if txt:
            out.append((level, txt))
    return out


def cjk_chars(text):
    return len(re.findall(r"[㐀-鿿豈-﫿]", text))


def slug(href):
    base = os.path.splitext(os.path.basename(href))[0]
    return re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-").lower()[:40] or "doc"


def main(epub_path):
    if not os.path.exists(epub_path):
        sys.exit("source EPUB not found: %s (pass the path, or place it at "
                 "source.epub)" % epub_path)
    for d in (SRC_EPUB, SRC, FIGS):
        os.makedirs(d, exist_ok=True)

    z = zipfile.ZipFile(epub_path)
    z.extractall(SRC_EPUB)

    container = ET.fromstring(z.read("META-INF/container.xml"))
    opf_path = container.find(".//" + CN + "rootfile").get("full-path")
    opf = ET.fromstring(z.read(opf_path))
    base = os.path.dirname(opf_path)

    manifest = {}
    for item in opf.findall(".//" + OPF + "item"):
        href = item.get("href")
        full = href if not base else base + "/" + href
        manifest[item.get("id")] = (full, item.get("media-type", ""))

    # images out
    n_img = 0
    for iid, (full, mt) in manifest.items():
        if mt.startswith("image/"):
            data = z.read(full)
            with open(os.path.join(FIGS, os.path.basename(full)), "wb") as fh:
                fh.write(data)
            n_img += 1

    spine = [ref.get("idref") for ref in opf.findall(".//" + OPF + "itemref")]
    report = ["# EPUB ingest report", "",
              "Source: `%s`  |  spine documents: %d  |  images: %d"
              % (os.path.basename(epub_path), len(spine), n_img), ""]
    draft = {"_README": "DRAFT structure from ingest_epub.py. Refine into "
             "book.json: add English titles, and merge/split units where the "
             "source's file boundaries do not match its logical chapters. Keep "
             "each unit's 'src' and 'chars'.",
             "title_en": "", "title_zh": "", "author_en": "", "author_zh": "",
             "source_epub": os.path.basename(epub_path), "structure": []}

    total = 0
    chn = 0
    for idref in spine:
        if idref not in manifest:
            continue
        full, mt = manifest[idref]
        if "html" not in mt and "xml" not in mt:
            continue
        xhtml = z.read(full).decode("utf-8", "replace")
        text = strip_tags(xhtml)
        if not text.strip():
            continue  # nav, blank, or cover-only page
        chn = cjk_chars(text)
        total += chn
        chn_i = chn
        hs = headings(xhtml)
        href = full[len(base) + 1:] if base and full.startswith(base + "/") else full
        fname = "%02d_%s.txt" % (len(draft["structure"]) + 1, slug(href))
        with open(os.path.join(SRC, fname), "w") as fh:
            fh.write(text)

        title_zh = hs[0][1] if hs else slug(href)
        report.append("## %s  (`%s`, %d chars)" % (title_zh, href, chn_i))
        for lvl, t in hs:
            report.append("%s- h%d %s" % ("  " * (lvl - 1), lvl, t))
        report.append("")

        chn += 1
        chapter = {
            "id": "ch%02d" % (len(draft["structure"]) + 1),
            "chapter": len(draft["structure"]) + 1,
            "title": title_zh, "title_en": "",
            "src": href, "chars": chn_i, "text_file": "data/src/" + fname,
            "sections": [],
        }
        # sections from h2 headings within this document
        h2s = [t for lvl, t in hs if lvl == 2]
        for si, t in enumerate(h2s, 1):
            chapter["sections"].append({
                "id": "ch%02ds%02d" % (len(draft["structure"]) + 1, si),
                "section": si, "title": t, "title_en": "",
                "src": "%s#h2-%d" % (href, si),
            })
        draft["structure"].append(chapter)

    report.insert(3, "Total source characters: **%d** (~%d per spine doc)\n"
                  % (total, total // max(1, len(draft["structure"]))))
    with open(os.path.join(ROOT, "out", "INGEST.md"), "w") as fh:
        os.makedirs(os.path.join(ROOT, "out"), exist_ok=True)
        fh.write("\n".join(report) + "\n")
    with open(os.path.join(ROOT, "book.draft.json"), "w") as fh:
        json.dump(draft, fh, ensure_ascii=False, indent=2)

    print("ingested %d spine documents, %d images, %d source chars"
          % (len(draft["structure"]), n_img, total))
    print("wrote data/src/*.txt, data/figs/*, out/INGEST.md, book.draft.json")
    print("next: author book.json from book.draft.json (English titles; "
          "merge/split to logical chapters), then run scripts/survey.py")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else
         os.path.join(ROOT, "source.epub"))
