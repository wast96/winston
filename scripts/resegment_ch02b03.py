#!/usr/bin/env python3
"""Reconcile the OCR-assembled zh scaffold for the B03 span (ch02 sections 6-8
plus the chapter-end Principal Sources) to true source paragraphs.

The section 6-8 body pages are figure-heavy (inline photos, a checkpoint map,
several portrait plates), so assemble.py's indent/blank signals desync and the
OCR merges many true paragraphs into one line, while splitting a few across the
figure/page boundary. This step drops the section-5 tail carried on PDF 109
(already translated in B02), applies the merges and splits that bring the zh
into 1:1 parity with out/ch02b03_reading.md, and inserts the Principal Sources
heading. It is a post-assembly step, the B03 analogue of resegment_ch02.py:

    render.py 109 133 --dpi 300
    ocr_crop.py 109 133 ... (measured crop) ; ocr_dual.py 109 133
    indents.py 109 133
    assemble.py ch02b03 109 133 --offset 36 --blank-assist
    python3 scripts/resegment_ch02b03.py     # <- this file

data/zh is gitignored (raw OCR); this script is the reproducible bridge.
Split markers are matched against the (garbled) OCR text, so they are drawn
verbatim from what tesseract actually produced, not from clean source.
"""

import os

ROOT = '/home/user/winston'
raw = open(os.path.join(ROOT, 'data/zh/ch02b03.txt')).read().split('\n')
raw = [l for l in raw if l != '']

# --- 1. keep from the first "### 6" heading on (drop the section-5 tail) ---
start = next(i for i, l in enumerate(raw) if l.startswith('### 6'))
lines = raw[start:]

# build items with body index bookkeeping
items = []  # [type, text]
for l in lines:
    items.append(['head' if l.startswith('###') else 'body', l])


def find_item(key):
    for it in items:
        if it[0] == 'body' and key in it[1]:
            return it
    raise SystemExit('  !! key NOT FOUND: %r' % key)


# --- 2. MERGES: join a body line into the immediately preceding body line ---
merges = [
    '个国民党管辖的县',      # Luo Guang para split by the checkpoint map (s7)
    '这位中统负责人对自己',   # Xu Enzeng source note, 2nd OCR line
    '秦平等一起工作的同志',   # Qin Ping source note, 2nd OCR line
]
for key in merges:
    pos = next(i for i, it in enumerate(items) if it[0] == 'body' and key in it[1])
    p = pos - 1
    while p >= 0 and items[p][0] != 'body':
        p -= 1
    items[p][1] += items[pos][1]
    items[pos][0] = 'dead'
items = [it for it in items if it[0] != 'dead']

# --- 3. SPLITS: (key identifying the body line, [markers], mode) ---
# mode 'before': split immediately before each marker.
splits = [
    # section 6
    ('着重增养新人', ['这攻培放'], 'before'),
    ('第三期在1938年底', ['王炎堂年少志大'], 'before'),
    ('1992年国家安全部',
     ['当时的边区', '1938年6月开班的一期有三十六', '这第一期训练班的领导', '中央政治局委员陈云'],
     'before'),
    ('浦石英的丈夫罗绍华',
     ['组织上介绍浦琼英', '这个浦防英就是卓琳', '卓琳与邓小3', '邓小业与卓琳的婚礼',
      '卓末的运气很好', '保安处训练班的女生人才出众'],
     'before'),
    ('便衣队长类荐壁', ['这期学员也出了不少干部'], 'before'),
    ('一期学员毛培春', ['二期学员郝苏', '十里铺训练班本来就为了'], 'before'),
    ('共产党这边，情报保卫机关也有人事问题', ['一个单位能否搞好团结'], 'before'),
    # section 7
    ('许多人本来主张杀人偿命', ['审判长实读了毛', '审判长庄严宣布'], 'before'),
    ('国民党的警察经常', ['满城的老百姓'], 'before'),
    # principal sources
    ('尹琪', ['王炎堂'], 'before'),
    ('杨玉英，前公安部机关党委', ['马光祥、康润民'], 'before'),
    ('吕瑛:前全国妇联', ['王友群'], 'before'),
    ('罗光;前成都市民政局', ['王卓超:前江西省'], 'before'),
]


def split_text(text, markers):
    parts = []
    rest = text
    for mk in markers:
        i = rest.find(mk)
        if i < 0:
            raise SystemExit('  !! marker NOT FOUND: %r in %r' % (mk, rest[:60]))
        parts.append(rest[:i])
        rest = rest[i:]
    parts.append(rest)
    return [p for p in parts if p.strip()]


for key, markers, mode in splits:
    it = find_item(key)
    it[1] = '\x00'.join(split_text(it[1], markers))

new = []
for it in items:
    if it[0] == 'body' and '\x00' in it[1]:
        for part in it[1].split('\x00'):
            new.append(['body', part])
    else:
        new.append(it)
items = new

# --- 4. insert the Principal Sources heading before the first source entry ---
pos = next(i for i, it in enumerate(items) if it[0] == 'body' and it[1].startswith('于桑'))
items.insert(pos, ['head', '### 主要资料'])

# --- write out & report ---
out = [it[1] for it in items]
open(os.path.join(ROOT, 'data/zh/ch02b03.txt'), 'w').write('\n'.join(out) + '\n')

secs = [i for i, it in enumerate(items) if it[0] == 'head']
for k, si in enumerate(secs):
    end = secs[k + 1] if k + 1 < len(secs) else len(items)
    cnt = sum(1 for it in items[si + 1:end] if it[0] == 'body')
    print('  %-28s %d' % (items[si][1][:26], cnt))
print('TOTAL body:', sum(1 for it in items if it[0] == 'body'))
