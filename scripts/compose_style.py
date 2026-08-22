#!/usr/bin/env python3
"""Compose a book's working STYLE.md from the shelf-wide style layers.

    styles/_base.md  +  styles/lang-<x>.md  +  styles/genre-<y>.md  ->  STYLE.md

Selection is mechanical, from book.json (see styles/INDEX.md):
  - language from source_language (ja | zh)
  - genre    from book.json "genre" if set, else inferred from "subjects"

The composed STYLE.md is a BUILD ARTIFACT: never hand-edit it. A book's own
rulings live in STYLE.local.md (created here from the template if absent), which
sessions read alongside STYLE.md. The composed file carries a manifest of the
source layers and their content hashes so check_style_freshness.py can tell when
the layers have moved on. No wall-clock timestamp is written, so an unchanged
set of layers recomposes to a byte-identical file.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

LANG_BY_CODE = {"ja": "lang-ja.md", "zh": "lang-zh.md"}
GENRES = ("fiction", "nonfiction")


def die(msg):
    sys.stderr.write("compose_style: " + msg + "\n")
    sys.exit(1)


def infer_genre(subjects):
    """fiction | nonfiction from BISAC-style subject strings."""
    low = " ".join(subjects).lower()
    if "nonfiction" in low or "non-fiction" in low:
        return "nonfiction"
    if re.search(r"\bfiction\b", low):
        return "fiction"
    return "nonfiction"


def strip_leading_directives(text):
    """Drop leading blank lines and full-line <!-- ... --> comments."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s == "" or (s.startswith("<!--") and s.endswith("-->")):
            i += 1
            continue
        break
    return "\n".join(lines[i:])


def demote_headings(text):
    """Add one '#' to every ATX heading so a layer nests under one H1."""
    return re.sub(r"(?m)^(#{1,5}) ", r"#\1 ", text)


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--book", default="book.json")
    ap.add_argument("--styles", default="styles")
    ap.add_argument("--out", default="STYLE.md")
    ap.add_argument("--local", default="STYLE.local.md")
    ap.add_argument("--genre", choices=GENRES, help="override book.json genre")
    ap.add_argument("--language", choices=sorted(LANG_BY_CODE),
                    help="override book.json source_language")
    args = ap.parse_args()

    styles = Path(args.styles)
    if not styles.is_dir():
        die("styles dir not found: %s" % styles)
    try:
        book = json.loads(Path(args.book).read_text(encoding="utf-8"))
    except FileNotFoundError:
        die("book.json not found: %s" % args.book)
    except json.JSONDecodeError as e:
        die("book.json is not valid JSON: %s" % e)

    # --- resolve language ---
    lang = args.language or book.get("source_language")
    if lang not in LANG_BY_CODE:
        die("source_language %r has no layer (have: %s); set --language or add "
            "styles/lang-<code>.md" % (lang, ", ".join(sorted(LANG_BY_CODE))))
    lang_file = styles / LANG_BY_CODE[lang]

    # --- resolve genre ---
    if args.genre:
        genre, basis = args.genre, "override"
    elif book.get("genre") in GENRES:
        genre, basis = book["genre"], "book.json genre"
    else:
        genre = infer_genre(book.get("subjects", []))
        basis = "inferred from subjects"
    genre_file = styles / ("genre-%s.md" % genre)

    base_file = styles / "_base.md"
    for f in (base_file, lang_file, genre_file):
        if not f.is_file():
            die("missing layer: %s" % f)

    base_raw = base_file.read_text(encoding="utf-8")
    lang_raw = lang_file.read_text(encoding="utf-8")
    genre_raw = genre_file.read_text(encoding="utf-8")

    # --- voice target from the genre layer's directive ---
    m = re.search(r"<!--\s*VOICE_TARGET:\s*(.+?)\s*-->", genre_raw)
    if not m:
        die("no VOICE_TARGET directive in %s" % genre_file)
    voice_target = m.group(1).strip()

    if "{{VOICE_TARGET}}" not in base_raw:
        die("base layer has no {{VOICE_TARGET}} placeholder to fill")
    base_filled = base_raw.replace("{{VOICE_TARGET}}", voice_target)

    # --- assemble ---
    title = book.get("title_en") or book.get("title") or "this book"
    layers = [
        ("_base.md", base_file, base_raw),
        (LANG_BY_CODE[lang], lang_file, lang_raw),
        ("genre-%s.md" % genre, genre_file, genre_raw),
    ]
    manifest = {
        "note": "COMPOSED BY scripts/compose_style.py FROM styles/ LAYERS. "
                "DO NOT EDIT. Regenerate after editing a layer; put this "
                "book's own rulings in STYLE.local.md.",
        "language": lang,
        "genre": genre,
        "genre_basis": basis,
        "layers": [{"file": name, "sha256": sha(raw)} for name, _, raw in layers],
    }
    header = (
        "<!-- STYLE_MANIFEST\n"
        + json.dumps(manifest, ensure_ascii=False, indent=2)
        + "\nSTYLE_MANIFEST -->\n\n"
        + "# STYLE.md — composed prose contract for %s\n\n" % title
        + "> Build artifact composed from the shelf-wide `styles/` layers "
        "(%s + %s + %s). Do not edit this file; edit the layers and recompose, "
        "and put this book's own rulings in `STYLE.local.md`, which you must "
        "read alongside this file.\n" % (layers[0][0], layers[1][0], layers[2][0])
    )

    body_parts = []
    body_parts.append(demote_headings(strip_leading_directives(base_filled)))
    body_parts.append(demote_headings(strip_leading_directives(lang_raw)))
    body_parts.append(demote_headings(strip_leading_directives(genre_raw)))
    composed = header + "\n" + "\n\n---\n\n".join(body_parts) + "\n"

    stray = re.findall(r"\{\{[A-Z_]+\}\}", composed)
    if stray:
        die("unfilled placeholder(s) left in composed output: %s"
            % ", ".join(sorted(set(stray))))

    Path(args.out).write_text(composed, encoding="utf-8")

    # --- ensure the local ledger exists ---
    local = Path(args.local)
    local_status = "exists (left as is)"
    if not local.exists():
        tmpl = styles / "STYLE.local.template.md"
        if tmpl.is_file():
            local.write_text(tmpl.read_text(encoding="utf-8"), encoding="utf-8")
            local_status = "created from template"
        else:
            local_status = "MISSING and no template to seed it"

    print("compose_style: %s" % title)
    print("  language: %s  ->  %s" % (lang, LANG_BY_CODE[lang]))
    print("  genre:    %s  ->  genre-%s.md  (%s)" % (genre, genre, basis))
    print("  voice:    %s" % voice_target)
    print("  wrote %s (%d lines)" % (args.out, composed.count("\n")))
    print("  %s: %s" % (args.local, local_status))


if __name__ == "__main__":
    main()
