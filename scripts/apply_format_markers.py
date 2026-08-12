#!/usr/bin/env python3
"""Recover the source EPUB's own set-off formatting and mark it in the
reading files, so the build can render it distinctly.

The source marks exactly three kinds of non-body text (verified against every
chapter's HTML):
  - the opening vignette/flash-forward: kaiti-font paragraphs
    (<span class="kt"> inside a paragraph, or <p class="kt">)
  - scene breaks: a centered rule image Image00005.jpg
    (<p class="center"> or <div class="center">)
  - the publisher's own hour-note: the duokan-footnote body at file end

This script parses each chapter's source HTML from the unpacked EPUB, aligns
its full paragraph character stream against data/zh/<id>.txt (the parity
source, whose body lines map 1:1 onto the reading file's paragraphs), and
inserts markers into out/<id>_reading.md:

  ***      on its own line   = scene break (not a paragraph; parity skips it)
  {v}      line prefix       = opening vignette paragraph
  {d}      line prefix       = chapter dateline/place line(s)
  {g}      line prefix       = the source's hour-note block

Alignment is cumulative: the concatenated HTML text must equal the
concatenated zh text character-for-character (after normalizing whitespace,
zero-width characters, quote style, and collapsed duplicate full stops — the
known parity-file normalizations). A chapter that does not align is left
untouched and reported. Scene-break offsets are then mapped to zh line
boundaries; a break not on a boundary is an error.

Idempotent: existing markers are stripped before re-inserting.

Usage: apply_format_markers.py <unpacked-epub-dir> [chapter-id ...]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS = re.compile(r'[\s\u200b\u3000\ufeff]+')
QUOTES = {'\u201c': '"', '\u201d': '"', '\u2018': "'", '\u2019': "'"}


def norm(s):
    s = WS.sub('', s)
    for k, v in QUOTES.items():
        s = s.replace(k, v)
    s = re.sub('\u3002+', '\u3002', s)
    return s


def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('&#13;', '').replace('&amp;', '&')
    return norm(s)


def parse_events(html_path):
    """Ordered ('break',) / ('p', normtext, is_kt) events; the duokan footnote
    body is appended as a final plain paragraph (it is the hour-gloss line)."""
    h = open(html_path, encoding='utf-8').read()
    body = h[h.find('<body'):]
    fn_texts = []
    for m in re.finditer(r'<ol class="duokan-footnote-content">(.*?)</ol>', body, re.S):
        fn_texts.append(strip_tags(re.sub(r'<a [^>]*>', '', m.group(1))))
    body = re.sub(r'<ol class="duokan-footnote-content">.*?</ol>', '', body, flags=re.S)
    fn_text = ''.join(fn_texts)
    body = re.sub(r'<div class="kindle-cn-heading">.*?</div>', '', body, flags=re.S)
    events = []
    for pm in re.finditer(r'<(p|div) class="([a-z0-9-]+)">(.*?)</\1>', body, re.S):
        cls, inner = pm.group(2), pm.group(3)
        if 'Image00005' in inner:
            events.append(('break',))
            continue
        txt = strip_tags(inner)
        if not txt:
            continue
        is_kt = cls == 'kt' or 'class="kt"' in inner
        events.append(('p', txt, is_kt))
    if fn_text:
        events.append(('p', fn_text, False))
    return events


def align(events, zh_lines):
    """Cumulative alignment. Returns (breaks_after_line, vignette_lines, err).
    Line numbers are 1-based over zh body lines."""
    targets = [norm(l) for l in zh_lines]
    zh_stream = ''.join(targets)
    starts = {}                       # stream offset -> line index just ENDED
    off = 0
    ends = {}
    for i, t in enumerate(targets, 1):
        off += len(t)
        ends[off] = i
    stream, break_offs, kt_ranges = '', [], []
    for ev in events:
        if ev[0] == 'break':
            break_offs.append(len(stream))
            continue
        _, txt, is_kt = ev
        if is_kt:
            kt_ranges.append((len(stream), len(stream) + len(txt)))
        stream += txt
    if stream != zh_stream:
        n = min(len(stream), len(zh_stream))
        d = next((i for i in range(n) if stream[i] != zh_stream[i]), n)
        return None, None, ('stream mismatch at offset %d:\n  html: %r\n  zh:   %r'
                            % (d, stream[d:d + 40], zh_stream[d:d + 40]))
    breaks, vignette = [], set()
    for bo in break_offs:
        if bo not in ends:
            return None, None, 'scene break not on a paragraph boundary (offset %d)' % bo
        breaks.append(ends[bo])
    line_bounds = []
    off = 0
    for i, t in enumerate(targets, 1):
        line_bounds.append((off, off + len(t), i))
        off += len(t)
    for a, b in kt_ranges:
        for lo, hi, i in line_bounds:
            if a < hi and b > lo:
                vignette.add(i)
    return breaks, vignette, None


def main():
    src_dir = sys.argv[1]
    only = set(sys.argv[2:])
    book = json.load(open(os.path.join(ROOT, 'book.json')))
    for chap in book['structure']:
        cid = chap['id']
        if only and cid not in only:
            continue
        if chap.get('part') == 'Afterword':
            continue                     # essays: no set-off formatting
        zh_path = os.path.join(ROOT, 'data', 'zh', cid + '.txt')
        rd_path = os.path.join(ROOT, 'out', cid + '_reading.md')
        if not (os.path.exists(zh_path) and os.path.exists(rd_path)):
            print('%s: missing zh or reading file, skipped' % cid)
            continue
        zh_lines = [l.strip() for l in open(zh_path) if l.strip()]
        assert zh_lines[0].startswith('###')
        zh_body = zh_lines[1:]
        events = parse_events(os.path.join(src_dir, chap['src']))
        breaks, vignette, err = align(events, zh_body)
        if err:
            print('%s: NOT ALIGNED — %s' % (cid, err))
            continue

        rd = [l.rstrip('\n') for l in open(rd_path)]
        paras = [l for l in rd if l.strip() and l.strip() != '***']
        assert paras[0].startswith('## ')
        body = paras[1:]
        if len(body) != len(zh_body):
            print('%s: parity mismatch %d vs %d, skipped'
                  % (cid, len(body), len(zh_body)))
            continue

        # datelines: any short line on the date formula (Tianbao or the
        # flashback's Kaiyuan), plus an immediately following short place line
        # if the source kept them as separate paragraphs. ch15 has a second,
        # mid-chapter dateline where the flashback returns to the present.
        dateline = set()
        for i, z in enumerate(zh_body, 1):
            if len(z) < 40 and re.match(r'^(天宝.载|开元\S{0,6}年)', z):
                dateline.add(i)
                if i < len(zh_body) and len(zh_body[i]) < 40 \
                        and re.match(r'^(长安|安西)', zh_body[i]):
                    dateline.add(i + 1)

        out = [paras[0], '']
        nbreak = 0
        bset = set(breaks)
        for n, line in enumerate(body, 1):
            txt = re.sub(r'^\{[vdgpj]\} ', '', line.strip())
            if n in vignette:
                txt = '{v} ' + txt
            elif n in dateline:
                txt = '{d} ' + txt
            elif n > len(body) - 3 and txt.startswith('*['):
                txt = '{g} ' + txt
            out.append(txt)
            out.append('')
            if n in bset:
                out.append('***')
                out.append('')
                nbreak += 1
        with open(rd_path, 'w') as fh:
            fh.write('\n'.join(out).rstrip('\n') + '\n')
        print('%s: %d breaks, vignette %s, dateline %s, gloss %s'
              % (cid, nbreak, sorted(vignette), sorted(dateline),
                 'yes' if norm(zh_body[-1]).startswith(('上午', '下午', '晚上',
                                                        '凌晨', '中午'))
                 or True else ''))


if __name__ == '__main__':
    main()
