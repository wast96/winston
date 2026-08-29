#!/usr/bin/env python3
"""QA battery for a built EPUB.

Checks, in order of how badly each one breaks a reader:
  1. mimetype is the first zip entry and is stored uncompressed
  2. container.xml points at a rootfile that exists
  3. every XHTML document is well-formed XML
  4. every manifest item resolves to a file in the archive
  5. every file in the archive is declared in the manifest
  6. every internal href and img src resolves, including fragments
  7. every spine itemref names a real manifest id

Usage: qa_epub.py out/book.epub
Exit 1 on any failure.

Size gate (commissioner rule, 2026-08-29): the built EPUB must be UNDER 30 MB,
hard cap, and ideally much less. qa fails the build at the cap and warns from
20 MB up, listing the largest archive members so the fix (usually recompressing
oversized figure images) is obvious.
"""
import os
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

OPF = "{http://www.idpf.org/2007/opf}"
CN = "{urn:oasis:names:tc:opendocument:xmlns:container}"
XH = "{http://www.w3.org/1999/xhtml}"

SIZE_HARD_MB = 30.0   # absolute cap: fail
SIZE_WARN_MB = 20.0   # early warning: shrink before it becomes a cap problem


def main(path):
    fails = []
    z = zipfile.ZipFile(path)
    names = z.namelist()

    size_mb = os.path.getsize(path) / (1024.0 * 1024.0)
    print("size: %.1f MB (warn at %.0f, hard cap %.0f)"
          % (size_mb, SIZE_WARN_MB, SIZE_HARD_MB))
    if size_mb >= SIZE_WARN_MB:
        biggest = sorted(z.infolist(), key=lambda i: -i.compress_size)[:5]
        for i in biggest:
            print("  largest: %-40s %6.1f MB stored (%.1f raw)"
                  % (i.filename, i.compress_size / (1024.0 * 1024.0),
                     i.file_size / (1024.0 * 1024.0)))
        if size_mb >= SIZE_HARD_MB:
            fails.append("EPUB is %.1f MB; the hard cap is %.0f MB "
                         "(recompress the largest members above; figures "
                         "rarely need more than ~150 KB each)"
                         % (size_mb, SIZE_HARD_MB))
        else:
            print("  WARNING: over %.0f MB; shrink the largest members "
                  "before this reaches the %.0f MB cap"
                  % (SIZE_WARN_MB, SIZE_HARD_MB))

    infos = z.infolist()
    if not infos or infos[0].filename != "mimetype":
        fails.append("mimetype is not the first zip entry")
    elif infos[0].compress_type != zipfile.ZIP_STORED:
        fails.append("mimetype is compressed; it must be stored")
    elif z.read("mimetype") != b"application/epub+zip":
        fails.append("mimetype content is wrong")

    root = ET.fromstring(z.read("META-INF/container.xml"))
    rootfile = root.find(".//" + CN + "rootfile").get("full-path")
    if rootfile not in names:
        fails.append("container rootfile missing: " + rootfile)
        print("\n".join(fails))
        return 1

    opf = ET.fromstring(z.read(rootfile))
    base = posixpath.dirname(rootfile)
    manifest = {}
    for item in opf.findall(".//" + OPF + "item"):
        href = posixpath.normpath(posixpath.join(base, item.get("href")))
        manifest[item.get("id")] = href
        if href not in names:
            fails.append("manifest item not in archive: " + href)

    # META-INF/* is reserved for the OCF layer (container.xml, Apple's
    # display-options, encryption.xml ...) and is never manifested.
    declared = set(manifest.values()) | {"mimetype", rootfile}
    for name in names:
        if name.startswith("META-INF/"):
            continue
        if name.endswith("/"):
            continue
        if name not in declared:
            fails.append("file in archive but not in manifest: " + name)

    for ref in opf.findall(".//" + OPF + "itemref"):
        if ref.get("idref") not in manifest:
            fails.append("spine references unknown id: " + str(ref.get("idref")))

    ids = {}
    docs = [h for h in manifest.values() if h.endswith(".xhtml")]
    for doc in docs:
        try:
            tree = ET.fromstring(z.read(doc))
        except ET.ParseError as exc:
            fails.append("not well-formed XML: %s (%s)" % (doc, exc))
            continue
        ids[doc] = {el.get("id") for el in tree.iter() if el.get("id")}

    for doc in docs:
        if doc not in ids:
            continue
        tree = ET.fromstring(z.read(doc))
        targets = [(el.get("href"), "href") for el in tree.iter(XH + "a")]
        targets += [(el.get("src"), "src") for el in tree.iter(XH + "img")]
        for target, kind in targets:
            if not target or target.startswith(("http:", "https:", "mailto:")):
                continue
            file_part, _, frag = target.partition("#")
            dest = doc if not file_part else posixpath.normpath(
                posixpath.join(posixpath.dirname(doc), file_part))
            if dest not in names:
                fails.append("%s in %s points at missing file: %s" % (kind, doc, dest))
                continue
            if frag and frag not in ids.get(dest, set()):
                fails.append("%s in %s points at missing anchor: %s#%s"
                             % (kind, doc, dest, frag))

    # chapter body documents, in spine order
    spine_order = [manifest[ref.get("idref")] for ref in
                   opf.findall(".//" + OPF + "itemref")
                   if ref.get("idref") in manifest]
    # Identify content documents by EXCLUDING the known apparatus documents,
    # rather than by matching a filename pattern. The pattern version looked
    # for prologue/chNN and silently reported "0 documents, 0 paragraphs" the
    # first time a unit was named anything else -- here the front matter,
    # fm01_gaikuang. A check that quietly measures nothing is worse than no
    # check, and this one is meant to be the last gate before a build ships,
    # so it must not depend on a naming convention it does not enforce.
    APPARATUS = {"cover.xhtml", "titlepage.xhtml", "nav.xhtml",
                 "contents.xhtml", "notes.xhtml", "backmatter.xhtml",
                 "errata.xhtml", "colophon.xhtml", "glossary.xhtml",
                 "characters.xhtml"}
    content_docs = [d for d in spine_order
                    if posixpath.basename(d) not in APPARATUS
                    and d.endswith(".xhtml")]

    total_paras = 0
    for doc in content_docs:
        body = z.read(doc).decode()
        zh = len(re.findall(r'class="src"', body))
        en = len(re.findall(r'class="trg"', body))
        if zh or en:
            print("%s bilingual pairs: %d source, %d translation" % (doc, zh, en))
            if zh != en:
                fails.append("%s: source and translation paragraph counts differ (%d vs %d)"
                             % (doc, zh, en))
        else:
            total_paras += len(re.findall(r"<p[ >]", body))
    print("reading edition: %d documents, %d paragraphs" % (len(content_docs), total_paras))

    nav_doc = [d for d in docs if d.endswith("nav.xhtml")]
    if nav_doc:
        nv = z.read(nav_doc[0]).decode()
        pl = re.search(r'page-list.*?</nav>', nv, re.S)
        n_pages = len(re.findall(r"<li>", pl.group(0))) if pl else 0
        n_marks = sum(len(re.findall(r'epub:type="pagebreak"', z.read(d).decode()))
                      for d in content_docs)
        print("pagination: %d page-list entries, %d markers in the text"
              % (n_pages, n_marks))
        if n_pages != n_marks:
            fails.append("page-list entries (%d) and page-break markers (%d) "
                         "disagree" % (n_pages, n_marks))

    notes_doc = [d for d in docs if d.endswith("notes.xhtml")]
    if notes_doc:
        nt = z.read(notes_doc[0]).decode()
        # TWO NOTE STREAMS, distinguished by numeral system and both restarting
        # per chapter (commissioner decision): author notes arabic, editorial
        # roman. Every id carries stream (n|en) and unit, e.g. ref-n-ch01-1,
        # ref-en-ch01-i, so ids stay unique across the spine. The in-text refs
        # are collected in reading order; bodies and backlinks come from the
        # notes page; the two must agree, and each (unit, stream) must number
        # 1..k in reading order.
        ref_re = re.compile(r'id="(ref-(n|en)-([A-Za-z0-9]+)-([0-9ivxlcdm]+))"')
        ordered = []
        for doc in content_docs:
            for m in ref_re.finditer(z.read(doc).decode()):
                ordered.append((m.group(1), m.group(2), m.group(3), m.group(4)))
        refids = [o[0] for o in ordered]
        ref_bodies = set(r[len("ref-"):] for r in refids)
        bodies = set(re.findall(
            r'<aside[^>]*\bid="((?:n|en)-[A-Za-z0-9]+-[0-9ivxlcdm]+)"', nt))
        backs = set(re.findall(
            r'href="[^"#]*#(ref-(?:n|en)-[A-Za-z0-9]+-[0-9ivxlcdm]+)"', nt))
        print("notes: %d references, %d bodies, %d backlinks"
              % (len(refids), len(bodies), len(backs)))
        if len(refids) != len(set(refids)):
            fails.append("duplicate note reference ids in the text")
        if ref_bodies != bodies:
            fails.append("note references and bodies do not match: %s"
                         % sorted(ref_bodies ^ bodies))
        if backs != set(refids):
            fails.append("note backlinks incomplete: %s"
                         % sorted(backs ^ set(refids)))

        def roman_to_int(s):
            vals = {"i": 1, "v": 5, "x": 10, "l": 50,
                    "c": 100, "d": 500, "m": 1000}
            total, prev = 0, 0
            for ch in reversed(s):
                v = vals.get(ch, 0)
                if v < prev:
                    total -= v
                else:
                    total += v
                    prev = v
            return total

        seq = {}
        for _id, stream, unit, label in ordered:
            val = int(label) if stream == "n" else roman_to_int(label)
            seq.setdefault((unit, stream), []).append(val)
        for (unit, stream), vals in sorted(seq.items()):
            kind = "author/arabic" if stream == "n" else "editorial/roman"
            if vals != list(range(1, len(vals) + 1)):
                fails.append("%s %s note numbering is not sequential in "
                             "reading order: %s" % (unit, kind, vals))

    if fails:
        print("FAIL")
        for f in fails:
            print("  -", f)
        return 1
    print("PASS: %d files, %d documents, all links resolve" % (len(names), len(docs)))
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        _p = sys.argv[1]
    else:
        import json as _json, os as _os
        _root = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
        try:
            _p = _json.load(open(_os.path.join(_root, "book.json")))\
                .get("deliverable") or _os.path.join(_root, "out", "book.epub")
        except Exception:
            _p = _os.path.join(_root, "out", "book.epub")
        if not _os.path.isabs(_p):
            _p = _os.path.join(_root, _p)
    sys.exit(main(_p))
