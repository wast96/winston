#!/usr/bin/env python3
"""Parse the printed back-of-book INDEX (printed 374-384, PDF 397-407) into a
structured data/index.json that the builder renders as a linked back-matter
Index page (book.json _index_decision). The source is a clean born-digital
two-column index; this reconstructs its logical entries so every folio
reference can be turned into a hyperlink to the matching pg-<unit>-<folio>
anchor the pagemaps emit.

Layout facts (measured):
  - Two columns, split at x = page_width/2; read left column top-to-bottom then
    right column top-to-bottom.
  - Indents (x0), per column base b (54 left / 223 right):
      main entry       b        (rel 0)
      wrapped ref line b+9..12   (starts with a digit or 'passim')
      sub-entry        b+15..18  (starts with a word/phrase, or 'See also')
      wrapped sub-ref  b+24      (starts with a digit or 'passim')
  - A soft line-break hyphen ('intermit-','pas-') joins to the next line with
    no space (so 'pas-'+'sim' -> 'passim').
  - Running head ('INDEX' / the book title) and the page folio are stripped.
  - The explanatory 'Passim' note on the first page is captured separately.

Each logical line is: a TERM, then a comma, then a reference string (page
numbers, ranges like '256-57' meaning 256-257, roman folios like 'xix', and
the word 'passim'), OR a cross-reference ('See X' / 'See also X'). A main entry
may be followed by indented sub-entries.

Writes data/index.json:
  {"intro": "...passim note...",
   "entries": [
     {"id": "...", "term": "...", "refs": "...raw ref string...",
      "see": ["..."], "see_also": ["..."],
      "subs": [{"term": "...", "refs": "...", "see": [...], "see_also": [...]}]},
     ...]}
The renderer (build_reading_epub) tokenizes the raw ref strings and resolves
folios to anchors; keeping the raw string here means the printed text is
reproduced verbatim and only the linking is done at build time.

Usage: parse_index.py [--dump]
"""
import json
import os
import re
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "source.pdf")
INDEX_PDF_FIRST, INDEX_PDF_LAST = 397, 407   # printed 374-384
TITLE_UPPER = "TRAGEDY OF THE CHINESE REVOLUTION"


def page_logical_lines(page, folio):
    """Return the page's index lines in reading order (left col, then right),
    soft-hyphen-joined, with running head and folio stripped. Each item is
    (indent_rel, text) where indent_rel is x0 minus the column base."""
    W = page.rect.width
    raw = []
    for b in page.get_text("dict")["blocks"]:
        if "lines" not in b:
            continue
        for l in b["lines"]:
            txt = "".join(s["text"] for s in l["spans"]).rstrip()
            if not txt.strip():
                continue
            raw.append((l["bbox"][0], l["bbox"][1], txt))
    out = []
    for col, base in (("L", 54.0), ("R", 223.0)):
        rows = [(x0, y, t) for (x0, y, t) in raw
                if (x0 < W / 2) == (col == "L")]
        rows.sort(key=lambda r: r[1])
        for x0, y, t in rows:
            s = t.strip()
            if s in ("Index", "INDEX") or s.upper() == TITLE_UPPER:
                continue
            if s == str(folio) and (y < 160 or y > 595):
                continue
            out.append((round(x0 - base), t.strip()))
    # soft-hyphen join (a line ending in '-' continues into the next, no space)
    merged = []
    for rel, t in out:
        if merged and merged[-1][1].endswith("-") and not merged[-1][1].endswith("--"):
            prev_rel, prev = merged[-1]
            merged[-1] = (prev_rel, prev[:-1] + t)
        else:
            merged.append((rel, t))
    return merged


MAXPAGE = 339   # printed_end; a numeric token above this is a YEAR, not a page ref
_NUM = r"\d+(?:[–-]\d+)?"


def _roman_int(s):
    vals = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    s = s.lower()
    if not s or any(ch not in vals for ch in s):
        return None
    total, prev = 0, 0
    for ch in reversed(s):
        v = vals[ch]
        total += -v if v < prev else v
        prev = max(prev, v)
    return total


# The front matter runs roman i..xxii; a roman REFERENCE is one of those folios
# (or a range of them). Restricting to real folio values keeps English words
# built from roman letters (I Ho Chuan, civil, mill) from being read as refs.
_ROMAN_SET = set()
def _seed_roman():
    def to_roman(n):
        out, table = "", [(10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
        for val, sym in table:
            while n >= val:
                out += sym
                n -= val
        return out
    for n in range(1, 23):
        _ROMAN_SET.add(to_roman(n))
_seed_roman()


def _is_roman_folio(tok):
    tok = tok.strip().lower()
    n = _roman_int(tok)
    return n is not None and 1 <= n <= 22 and tok in _ROMAN_SET


NOTE_REF = re.compile(r"\d+n\d+$")   # e.g. 340n4 -> printed p.340, note 4


def _one_ref(tok):
    """A single reference (no trailing 'passim'): a page number/range <= MAXPAGE,
    a roman folio/range, or an endnote reference like '340n4'."""
    tok = tok.strip()
    if NOTE_REF.fullmatch(tok):
        return True
    m = re.fullmatch(r"(\d+)(?:[–-](\d+))?", tok)
    if m:
        return int(m.group(1)) <= MAXPAGE
    parts = re.split(r"[–-]", tok)
    return len(parts) <= 2 and all(_is_roman_folio(p) for p in parts)


def is_ref_token(tok):
    """True if a comma-token is a page/roman reference (optionally '... passim'),
    or bare 'passim'."""
    tok = tok.strip()
    if tok.lower() == "passim":
        return True
    m = re.fullmatch(r"(.*?)\s+passim", tok, re.I)
    if m:
        tok = m.group(1).strip()
    return _one_ref(tok)


def starts_ref(text):
    """True if a line begins a reference continuation. The first comma-segment
    must be ENTIRELY a reference token: a page number <= MAXPAGE, a roman folio,
    or '... passim' / 'passim'. This rejects a leading year (>MAXPAGE), a word,
    and a roman-lettered NAME whose first letter is a folio ('I Ho Chuan' -> 'I'
    is roman i, but 'I Ho Chuan' as a whole is not a ref token)."""
    if not text.strip():
        return False
    return is_ref_token(text.strip().split(",")[0])


def slug(term, seen):
    s = re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-") or "entry"
    s = "ix-" + s
    base, i = s, 2
    while s in seen:
        s = "%s-%d" % (base, i)
        i += 1
    seen.add(s)
    return s


def split_term_refs(text):
    """A logical line -> (term, refs, see, see_also). Handles:
      * a line that IS a cross-reference ('See X' / 'See also X');
      * a trailing 'See X' / 'See also X' after a term AND/OR a ref list
        ('secret societies, 12-15 passim, 66. See also Triads');
      * 'Term, <ref list>' where the term itself may contain commas (e.g.
        'Adams, John') and even a date ('coup of April 12, 1927, and').
    Method: strip any trailing cross-reference first, then find the term/ref
    boundary by peeling reference tokens off the RIGHT -- a token is a
    reference only if it is a page number (<= MAXPAGE), a roman folio, an
    endnote ref, or 'passim' (so a year like 1927 stays in the term)."""
    text = text.strip()
    # a whole-line cross-reference (a sub-entry that is only 'See ...')
    m = re.match(r"^(See also|See)\s+(.+)$", text)
    if m:
        targets = [x.strip() for x in re.split(r";", m.group(2)) if x.strip()]
        return "", "", (targets if m.group(1) == "See" else []), \
               (targets if m.group(1) == "See also" else [])
    # strip a trailing cross-reference (tolerating a closing quote/paren before
    # 'See', e.g. '“Boxers.” See I Ho Chuan'); it may follow a ref list
    see, see_also = [], []
    m = re.search(r"\s(See also|See)\s+(.+)$", text)
    if m:
        targets = [x.strip() for x in re.split(r";", m.group(2)) if x.strip()]
        if m.group(1) == "See also":
            see_also = targets
        else:
            see = targets
        text = text[:m.start()].strip().rstrip(".,")
    # peel reference tokens off the right, at comma boundaries
    parts = [p.strip() for p in text.split(",")]
    i = len(parts)
    while i > 0 and is_ref_token(parts[i - 1]):
        i -= 1
    if i == len(parts):
        # no comma-separated ref tail; maybe a space-separated trailing ref
        m = re.search(r"\s+(%s(?:\s+passim)?|passim)$" % _NUM, text)
        if m and is_ref_token(m.group(1)):
            return text[:m.start()].strip(), m.group(1).strip(), see, see_also
        return text.rstrip(".,"), "", see, see_also
    term = ", ".join(parts[:i]).strip()
    refs = ", ".join(parts[i:]).strip()
    return term, refs, see, see_also


def main():
    doc = pymupdf.open(PDF)
    intro = ""
    # Pass 1: assemble raw logical lines, joining ref-run continuations. Each is
    # (kind, raw_text) with kind 'main' or 'sub'.
    logical = []
    for pno in range(INDEX_PDF_FIRST, INDEX_PDF_LAST + 1):
        folio = pno - 23
        for rel, text in page_logical_lines(doc[pno - 1], folio):
            if text.startswith("“Passim”"):
                intro = text
                continue
            prev_see = logical and re.search(r"\bSee( also)?$",
                                             logical[-1][1].rstrip())
            if (starts_ref(text) or prev_see) and logical:
                # a wrapped reference run, or a cross-reference target that
                # wrapped after a dangling 'See' / 'See also': append to the
                # open logical line, preserving the printed comma between pieces
                prev_kind, prev = logical[-1]
                if prev.endswith(",") or prev_see:
                    sep = " "          # wrapped 'See also' target joins with a space
                elif text.lower().startswith("passim"):
                    sep = " "          # 'passim' attaches to the preceding range
                else:
                    sep = ", "
                logical[-1] = (prev_kind, (prev + sep + text))
                continue
            logical.append(("main" if rel <= 8 else "sub", text))

    # Pass 2: split each logical line into term/refs/cross-refs; nest subs.
    seen = set()
    entries = []
    cur = None
    for kind, raw in logical:
        term, refs, see, see_also = split_term_refs(raw)
        if kind == "main" or cur is None:
            cur = {"id": slug(term or "see", seen), "term": term, "refs": refs,
                   "see": see, "see_also": see_also, "subs": []}
            entries.append(cur)
        else:
            cur["subs"].append({"term": term, "refs": refs,
                                "see": see, "see_also": see_also})

    # Cleanup: a cross-reference target that wrapped mid-name leaves a
    # fully-dangling main entry (no refs, subs, or cross-refs) right after the
    # cross-ref line ('...See Shanghai' + 'General Labor Union'). Fold such a
    # stray back onto the previous entry's last cross-ref target.
    cleaned = []
    for e in entries:
        dangling = not (e["refs"] or e["subs"] or e["see"] or e["see_also"])
        if dangling and e["term"] and cleaned:
            prev = cleaned[-1]
            tgt = prev["see_also"] or prev["see"]
            if tgt:
                tgt[-1] = (tgt[-1] + " " + e["term"]).strip()
                continue
        cleaned.append(e)
    entries = cleaned

    out = {"intro": intro, "entries": entries}
    if "--dump" in sys.argv:
        for e in entries:
            head = e["term"]
            extra = ""
            if e["refs"]:
                extra = "  -> " + e["refs"]
            if e["see"]:
                extra += "  [See %s]" % "; ".join(e["see"])
            if e["see_also"]:
                extra += "  [See also %s]" % "; ".join(e["see_also"])
            print("%s%s" % (head, extra))
            for s in e["subs"]:
                sx = ("  -> " + s["refs"]) if s["refs"] else ""
                if s["see"]:
                    sx += "  [See %s]" % "; ".join(s["see"])
                if s["see_also"]:
                    sx += "  [See also %s]" % "; ".join(s["see_also"])
                print("    - %s%s" % (s["term"], sx))
        print("\n%d main entries" % len(entries))
        return
    dest = os.path.join(ROOT, "data", "index.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote %s (%d entries)" % (dest, len(entries)))


if __name__ == "__main__":
    main()
