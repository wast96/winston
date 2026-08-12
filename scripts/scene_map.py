#!/usr/bin/env python3
"""Report scene-break positions for a source chapter, read from the raw XHTML.

The ingest collapses <p><br/></p> blanks, so scene breaks are invisible in the
data/src/*.txt. This reads the original data/src_epub XHTML, walks the <p>
elements of the main body in order, and reports where a run of TWO OR MORE
consecutive blank (<br/>-only) paragraphs falls between body text paragraphs.
Such a run is a scene break; the single blank run right after the chapter title
is only the title/body separator and is NOT reported.

Output: one line per scene break, "after body paragraph N" (1-based index into
the body, i.e. into data/src/<file>.txt lines starting at line 3), plus a tail
count line. Body paragraph count is printed so it can be cross-checked against
data/src.

Usage: scene_map.py OEBPS/Text/part0004.xhtml
       scene_map.py data/src_epub/OEBPS/Text/part0004.xhtml
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def items(xhtml):
    main = re.search(r'<div class="main">(.*?)</body>', xhtml, re.S)
    body = main.group(1) if main else xhtml
    out = []
    for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', body, re.S):
        inner = m.group(1)
        if re.fullmatch(r'\s*<br\s*/?>\s*', inner):
            out.append(('BR', ''))
        else:
            txt = html.unescape(re.sub(r'(?s)<[^>]+>', '', inner)).strip()
            out.append(('P', txt))
    return out


def scene_breaks(xhtml):
    seq = items(xhtml)
    # locate the title: the first P item. Header = up to that P, then the
    # first following BR run (title/body separator). Body = P items after.
    first_p = next(i for i, (k, _) in enumerate(seq) if k == 'P')
    j = first_p + 1
    while j < len(seq) and seq[j][0] == 'BR':   # swallow title/body separator
        j += 1
    body_seq = seq[j:]
    breaks = []          # body-paragraph index (1-based) after which a break falls
    body_i = 0
    run = 0
    for k, _ in body_seq:
        if k == 'BR':
            run += 1
        else:
            if run >= 2 and body_i >= 1:
                breaks.append(body_i)
            run = 0
            body_i += 1
    n_body = body_i
    return breaks, n_body


def main(path):
    if not os.path.isabs(path) and not os.path.exists(path):
        path = os.path.join(ROOT, 'data', 'src_epub', path)
    xhtml = open(path, encoding='utf-8').read()
    breaks, n_body = scene_breaks(xhtml)
    for b in breaks:
        print('scene break after body paragraph %d' % b)
    print('%d body paragraphs, %d scene break(s)' % (n_body, len(breaks)))


if __name__ == '__main__':
    main(sys.argv[1])
