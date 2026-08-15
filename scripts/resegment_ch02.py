#!/usr/bin/env python3
"""Reconcile the OCR-assembled zh scaffolding for ch02 to true source paragraphs.

The ch02 body pages are figure-heavy: inline photos throw the indent flags and
tesseract's blank lines out of register, so assemble.py under-segments the zh
(137 body paras vs the 167 true source paragraphs). This step splits the merged
paragraphs and appends section 5's tail on printed p73 (PDF 109), giving zh
parity with out/ch02_reading.md (167). It is a post-assembly step:

    render.py 82 109 --dpi 300
    ocr_crop.py 82 109 ... (measured crop) ; ocr_dual.py 82 109
    indents.py 82 108 ; assemble.py ch02 82 108 --offset 36 --blank-assist
    python3 scripts/resegment_ch02.py     # <- this file

data/zh is gitignored (raw OCR); this script is the reproducible bridge.
"""

import re, json, os
ROOT='/home/user/winston'
lines=open(os.path.join(ROOT,'data/zh/ch02.txt')).read().split('\n')
# Build list of tokens preserving headings; collect body paras with 1-based idx
items=[]  # (type,text) type in {'head','body'}
bidx=0
bmap={}   # body index -> position in items
for l in lines:
    if l.startswith('###'):
        items.append(['head',l])
    elif l.strip():
        bidx+=1
        bmap[bidx]=len(items)
        items.append(['body',l])
# --- MERGES: join body index into previous body ---
merges=[16, 19,20, 56, 129]   # each merges into the immediately preceding BODY paragraph
# perform merges by concatenating text into previous body item, mark removed
removed=set()
for m in merges:
    pos=bmap[m]
    # find previous body item not removed
    p=pos-1
    while p>=0 and (items[p][0]!='body' or p in removed):
        p-=1
    items[p][1]+=items[pos][1]
    removed.add(pos)
# rebuild items without removed
items=[it for i,it in enumerate(items) if i not in removed]

def split_para(text, markers, mode):
    parts=[]; rest=text
    for mk in markers:
        i=rest.find(mk)
        if i<0:
            print("  !! marker NOT FOUND:", repr(mk), "in", repr(rest[:50]))
            continue
        if mode=='before':
            parts.append(rest[:i]); rest=rest[i:]
        else: # after
            j=i+len(mk)
            parts.append(rest[:j]); rest=rest[j:]
    parts.append(rest)
    return [p for p in parts if p.strip()]

# --- SPLITS: keyed by a distinctive substring that identifies the (post-merge) body paragraph ---
splits=[
 ("延安城顿时震惊", ['董必武出面讲'], 'after'),
 ("中共接管延安，西北保卫局特别注意", ['还有两个奇怪的和尚'], 'before'),
 ("那个发生伏击事件的劳山", ['1937年初中央进驻'], 'before'),
 ("边区政府在甘谷驿", ['按说，这个案件'], 'before'),
 ("就连特务头子", ['1928年初'], 'before'),
 ("谁能料到，1938年4月", ['升格了','简称','副局长','就此登台','心腹大患'], 'after'),
 ("二海特科于1935", ['1937年12月'], 'before'),
 ("军事封锁的重任由胡宗南", ['一举而歼灭之'], 'after'),
 ("向南到西安的八", ['向东北，经绥德'], 'before'),
 ("中蕉中央还着手恢复", ['延安成为中共运作全国','延安南向通路'], 'before'),
 ("离开中部县的张国", ['自以为计划周密','特派李克农'], 'before'),
 ("周恩来反复说服", ['得到蒋介石勉励'], 'before'),
 ("攻期译管情报保卫工作", ['康生出身山东'], 'before'),
 ("从苏联归国的王明", ['刚刚抵达陕北一年','的欢迎不是客气'], 'before'),
 ("正在健全情报保卫工作", ['具有国际经验的康生'], 'before'),
 ("李克农一生处于", ['曾经在'], 'before'),
 ("最显眼的是一支警察队", ['延安城里主要路口','陕甘宁边区的主要军事力量','保安团第一任团长','中社部是党的机构','始终面对强大','中共这边'], 'before'),
 ("周兴在中共的情报保卫系统", ['十四岁'], 'before'),
 ("党忆明是山西人", ['训练班'], 'before'),
]
# apply splits
for key,markers,mode in splits:
    done=False
    for it in items:
        if it[0]=='body' and key in it[1]:
            newparts=split_para(it[1],markers,mode)
            it[1]='\x00'.join(newparts)  # temp marker
            done=True
            break
    if not done:
        print("  !! split KEY not found:",repr(key))
# expand temp-split bodies into multiple items
newitems=[]
for it in items:
    if it[0]=='body' and '\x00' in it[1]:
        for part in it[1].split('\x00'):
            newitems.append(['body',part])
    else:
        newitems.append(it)
items=newitems

# --- APPEND p109 tail (4 clean paragraphs) at end (section 5) ---
tail=[
 "后来，李启明一直留在陕西，“文化大革命”前任陕西省省长，“文化大革命”后任云南省委常务书记。",
 "分析周兴、赵苍璧、李启明这批边保干部的来源，可以看到，中共情报、保卫干部的配备正在发生变化。",
 "中共向来重视情报保卫系统的干部配备，高层领导送苏联培训，骨干成员强调工人成分。邓发是海员出身，周兴、欧阳毅、陈复生、谢滋群等人都是手工业工人出身。可是，组织成分纯而又纯，并没有保证不出顾顺章那样的叛徒，并没有保证不犯李韶九那样的严重错误。",
 "经历挫折的中共更会用人，新配备的保卫干部来源多方：既有一批经历过二万五千里长征的老干部，又重视培训陕北当地农民干部；既有许多来自红区的工农干部，又充实来自白区的地下党干部，还特别注意吸收外来知识分子。",
]
for t in tail:
    items.append(['body',t])

# write out
out=[it[1] for it in items]
open(os.path.join(ROOT,'data/zh/ch02.txt'),'w').write('\n'.join(out)+'\n')
nb=sum(1 for it in items if it[0]=='body')
print("total body paras now:",nb)
# per-section
secs=[i for i,it in enumerate(items) if it[0]=='head']
for k,si in enumerate(secs):
    end=secs[k+1] if k+1<len(secs) else len(items)
    cnt=sum(1 for it in items[si+1:end] if it[0]=='body')
    print(f"  {items[si][1][:22]!r}: {cnt}")
