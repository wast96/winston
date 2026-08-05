#!/usr/bin/env python3
"""Convert straight ASCII quotes/apostrophes to typographic quotes across the
reading files and every display surface that must stay in sync with them.

The conversion is strictly 1 character -> 1 character, so text offsets never
move; note anchors are re-derived by locating each anchor in the ORIGINAL
unit text and taking the same-offset span of the converted text, which keeps
them verbatim substrings by construction.

Applies to:
  - out/<id>_reading.md            (all units)
  - notes.json                     (anchors by offset mapping; bodies outside tags)
  - glossary.json                  ('en' and 'note' fields)
  - book.json                      (title_en, description, translator_note)

Reports any line where double quotes come out unbalanced, for manual review.

Usage: smart_quotes.py [--check]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OPENERS = set(' \t\n([{—–‘“　')

DENORM = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})


def smart(s):
    s = s.translate(DENORM)
    out = []
    for i, c in enumerate(s):
        p = out[i - 1] if i else ''       # converted context
        n = s[i + 1] if i + 1 < len(s) else ''
        if c == '"':
            # An opener needs an opening context — except after an em-dash
            # with nothing following: that is interrupted speech ( You—" ),
            # a closer. ("...Speech openings keep the dots after the quote.)
            if (not p or p in OPENERS) and \
                    not (p == '—' and (n == '' or n in ' \t\n,.;:!?')):
                out.append('“')
            else:
                out.append('”')
        elif c == "'":
            if (not p or p in OPENERS or p == '“') and (n.isalnum() or n in '"“'):
                out.append('‘')
            else:
                out.append('’')
        else:
            out.append(c)
    return ''.join(out)


def smart_outside_tags(s):
    parts = re.split(r'(<[^>]*>)', s)
    return ''.join(p if p.startswith('<') else smart(p) for p in parts)


def convert_files():
    warn = []
    originals = {}
    for name in sorted(os.listdir(os.path.join(ROOT, 'out'))):
        m = re.match(r'(ch\d\d)_reading\.md$', name)
        if not m:
            continue
        path = os.path.join(ROOT, 'out', name)
        orig = open(path).read()
        originals[m.group(1)] = orig
        conv = smart(orig)
        assert len(conv) == len(orig)
        for ln, line in enumerate(conv.splitlines(), 1):
            if line.count('“') != line.count('”'):
                warn.append('%s:%d unbalanced doubles: %s' % (name, ln, line[:70]))
        with open(path, 'w') as fh:
            fh.write(conv)
    return originals, warn


def convert_notes(originals):
    path = os.path.join(ROOT, 'notes.json')
    notes = json.load(open(path))
    misses = []
    for cid, lst in notes.items():
        orig = originals.get(cid)
        conv = smart(orig) if orig else None
        for e in lst:
            a = e['anchor']
            if orig is not None:
                pos = orig.find(a)
                if pos >= 0:
                    e['anchor'] = conv[pos:pos + len(a)]
                else:
                    misses.append((cid, a[:60]))
            e['note'] = smart_outside_tags(e['note'])
    json.dump(notes, open(path, 'w'), ensure_ascii=False, indent=2)
    return misses


def convert_ledgers():
    gpath = os.path.join(ROOT, 'glossary.json')
    gloss = json.load(open(gpath))
    for section, entries in gloss.items():
        if section.startswith('_'):
            continue
        for rec in entries.values():
            for k in ('en', 'note'):
                if rec.get(k):
                    rec[k] = smart(rec[k])
    json.dump(gloss, open(gpath, 'w'), ensure_ascii=False, indent=2)

    bpath = os.path.join(ROOT, 'book.json')
    book = json.load(open(bpath))
    for k in ('title_en', 'description'):
        if book.get(k):
            book[k] = smart(book[k])
    if book.get('translator_note'):
        book['translator_note'] = [smart_outside_tags(p)
                                   for p in book['translator_note']]
    json.dump(book, open(bpath, 'w'), ensure_ascii=False, indent=2)


def main():
    originals, warn = convert_files()
    misses = convert_notes(originals)
    convert_ledgers()
    print('converted %d unit files' % len(originals))
    for w in warn:
        print('  WARN', w)
    for cid, a in misses:
        print('  ANCHOR MISS %s %s' % (cid, a))
    # verify every anchor resolves post-conversion
    notes = json.load(open(os.path.join(ROOT, 'notes.json')))
    bad = 0
    for cid, lst in notes.items():
        text = open(os.path.join(ROOT, 'out', cid + '_reading.md')).read()
        for e in lst:
            if e['anchor'] not in text:
                print('  UNRESOLVED %s %s' % (cid, e['anchor'][:60]))
                bad += 1
    print('anchors: %d unresolved' % bad)


if __name__ == '__main__':
    main()
