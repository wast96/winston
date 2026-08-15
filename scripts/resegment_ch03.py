#!/usr/bin/env python3
"""Reconcile the OCR-assembled zh scaffold for the B04 span (Chapter 3, the
whole chapter, plus its chapter-end Principal Sources) to true source
paragraphs.

Chapter 3 (the 图文版) is heavily figure-laden: nearly every opener page and
many body pages carry inline portrait plates, group photos, a facsimile and a
photo caption or two. assemble.py's indent/blank signals desync around the
plates, so the OCR merges many true paragraphs into one line (and, at a couple
of page/figure boundaries, splits one true paragraph across two lines). This
post-assembly step applies the merges and splits that bring the zh into 1:1
parity with out/ch03_reading.md, and rewrites the chapter-end "主要资料:" body
line as a translated-section "### Principal Sources" heading. It is the B04
analogue of resegment_ch02.py / resegment_ch02b03.py.

    render.py 134 170 --dpi 300
    ocr_crop.py 134 170 ... (measured crop) ; ocr_dual.py 134 170
    indents.py 134 170
    assemble.py ch03 134 170 --offset 36 --blank-assist
    python3 scripts/resegment_ch03.py     # <- this file

data/zh is gitignored (raw OCR); this script is the reproducible bridge.
Split markers are matched against the (garbled) OCR text, so they are drawn
verbatim from what tesseract actually produced, not from clean source. A few
embedded figure-caption fragments survive as a garbled tail on the paragraph
they abut; the bilingual is QC-only and never ships, so this is cosmetic.
"""

import os

ROOT = '/home/user/winston'
path = os.path.join(ROOT, 'data/zh/ch03.txt')
raw = [l for l in open(path).read().split('\n') if l != '']

items = [['head' if l.startswith('###') else 'body', l] for l in raw]


def find_pos(key):
    for i, it in enumerate(items):
        if it[0] == 'body' and key in it[1]:
            return i
    raise SystemExit('  !! MERGE/anchor key NOT FOUND: %r' % key)


# --- 1. MERGES: join a body line into the immediately preceding body line ---
# (OCR split one true paragraph across a page/figure boundary.)
merges = [
    '国共合作之后，中央又指派王世英',   # Wang Shiying para, split by his p138 portrait
    '的地下党员间又文和杨子明',          # Yan Youwen para (阎->间 OCR), split by p146/147 plate
]
for key in merges:
    pos = find_pos(key)
    p = pos - 1
    while p >= 0 and items[p][0] != 'body':
        p -= 1
    items[p][1] += items[pos][1]
    items[pos][0] = 'dead'
items = [it for it in items if it[0] != 'dead']


# --- 2. SPLITS: (key identifying the body line, [markers]) split before each ---
splits = [
    # section 1
    ('同国民党打交道', ['这个电台既要保持']),
    ('1937年8月，国民党与共产党达成协议', ['既然有了合法身份']),
    ('国民党的特务机关，此刻正在眩',
     ['专职反共的中统首脑徐恩曾', '上面转向', '不过，国民党的特务机关还是很快']),
    ('毛泽东的老师徐特立到长沙', ['谢觉哉到兰州']),
    ('领袖周恩来，亲自领率驻京八办', ['桂林行营主任李济深']),
    # section 2
    ('国民党中统局长徐恩', ['共产党在重庆担任上层统战工作的']),
    ('这是秘密活动方式的重大转变', ['实行社会化以后']),
    # section 3
    ('周恩来十分敏锐', ['各地党组织紧急调动党员']),
    ('这是一个极其成功的高级情报工',
     ['系大将白崇禧精于作战', '北方局派回广西老家']),
    ('南方局委员博', ['沈安娜长期']),
    ('1942年，秘密联络员徐仲航被捕', ['有了为党牺牲的准备']),
    ('情报侦察工作，外围观察不如内部', ['深入虎穴，先要披上']),
    # section 4
    ('各根据地知道中央困难',
     ['赚钱最多最快的还是办公司', '大上海，最富裕的是宁波人']),
    ('南方局情报部长刘少文很有创意',
     ['刘少文提出', '中共最大的党产公司华润公司成立']),
    # section 5
    ('女记者黄芍回国采访抗日', ['菲律宾华侨庄焰']),
    ('缅甸华侨党员郑祥鹏和王楚惠', ['共产主义的幽灵到处游']),
    ('中国的东部沿海始终是战略要地', ['八路军总司令朱德同美国上将史迪威']),
    # section 6
    ('公开机构:八路军西安办事处', ['半公开机构', '隐蔽机构']),
    ('周恩来在国统区各大城市都实行三线配置', ['周恩来在国统区各大城市都实行三线配置']),
    ('吴德峰在西安租了一个院落', ['西安情报站发展了诸多重要关系']),
    ('索性以查户口为名进门搜查', ['八办也为延安采办物资']),
    ('共产党方面判断',
     ['西安情报站布置内线', '西安事变之后', '藉鼎文是宣侠父',
      '蒋介石对枪杆子向来把得很紧', '参加过淞沪抗战的胡宗南']),
    ('杀宣使父的内幕', ['在国共合作的局面下，国民党居然暗杀']),
    # section 7
    ('回到驻地，下令给八路军', ['不要以为毛泽东']),
    # Principal Sources
    ('地下十二年与周恩来', ['姚蓝']),
    ('阁又文之女', ['郝之美']),
    ('协商民主', ['耘山、周']),
    ('王楚惠的丈夫郑祥', ['王明爱、庄']),
    ('吴德轿之女', ['陈建宇:陈养山之子', '张严佛:《宣侠父']),
]

for key, markers in splits:
    pos = find_pos(key)
    text = items[pos][1]
    cut = []
    for m in markers:
        idx = text.find(m)
        if idx <= 0:
            raise SystemExit('  !! SPLIT marker NOT FOUND (%r in %r...)' % (m, text[:40]))
        cut.append(idx)
    cut = sorted(set(cut))
    pieces, prev = [], 0
    for c in cut:
        pieces.append(text[prev:c])
        prev = c
    pieces.append(text[prev:])
    items[pos:pos + 1] = [['body', p] for p in pieces]

# --- 3. rewrite the "主要资料:" body line as a translated-section heading ---
for it in items:
    if it[0] == 'body' and it[1].startswith('主要资料'):
        it[0] = 'head'
        it[1] = '### Principal Sources'
        break

out = '\n'.join(it[1] for it in items) + '\n'
open(path, 'w').write(out)

body = sum(1 for it in items if it[0] == 'body')
head = sum(1 for it in items if it[0] == 'head')
print('  ch03 resegmented: %d body paragraphs, %d headings' % (body, head))
