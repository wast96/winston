#!/usr/bin/env python3
# Final paragraph-structure surgery on assembled ch02/ch03 (anchor-based, robust
# to line shifts). Fixes garbled headings, page-seam splits (merge), blank-less
# page welds (split), and one OCR-clipped short line. Character-level name/number
# OCR fixes are applied separately via apply_fixes.py.
import os, re
ZH = "/home/user/winston/data/zh"
MARK = "4册中0①②③④⑤⑥忆>"  # trailing footnote-marker / stray junk chars

def load(u): return [l for l in open(os.path.join(ZH,u+".txt")).read().split("\n") if l.strip()!=""]
def save(u,P): open(os.path.join(ZH,u+".txt"),"w").write("\n".join(P)+"\n")

def find_end(P, suf, start=0):
    for i in range(start,len(P)):
        if P[i].startswith("###"): continue
        s=P[i]
        while s and s[-1] in MARK+" ": s=s[:-1]
        if s.endswith(suf): return i
    raise SystemExit("suffix not found: "+suf)

def find_contains(P, sub, start=0):
    for i in range(start,len(P)):
        if sub in P[i]: return i
    raise SystemExit("substr not found: "+sub)

def merge_after(P, suf):
    """Merge the paragraph ending with suf and the following body paragraph."""
    i=find_end(P,suf)
    j=i+1
    nxt=P[j].lstrip("”’\" 　")   # strip stray leading closing-quote from seam
    P[i]=P[i]+nxt
    del P[j]

def split_at(P, sub, keep_with_first):
    """Split the paragraph containing sub; keep_with_first ends the first half."""
    i=find_contains(P,sub)
    k=P[i].index(keep_with_first)+len(keep_with_first)
    a,b=P[i][:k],P[i][k:]
    P[i]=a; P.insert(i+1,b)

# ---------------- ch02 ----------------
P=load("ch02")
P[0]='### 一科——特科的“总管家”'
# p65 weld: OCR dropped "生涯。" (scan shows "革命生涯。凡是当年"); restore + split
i=find_contains(P,"共的革命凡是当年")
P[i]=P[i].replace("共的革命凡是当年","共的革命生涯。\x00凡是当年")
a,b=P[i].split("\x00"); P[i]=a; P.insert(i+1,b)
merge_after(P,"做过地下工作")      # "凡是当年...做过地下工作" + "的同志...一带。"
merge_after(P,"外贸部下属一")      # p62 -> p64 (photo p63 blanked)
merge_after(P,"因同国民党")        # p66 -> p67
merge_after(P,"成员的聚居")        # p67 -> p69 (photo p68 blanked)
merge_after(P,"须予以制")          # p71 -> p72
merge_after(P,"延请")              # p73 -> p74
merge_after(P,"李强就是经常")      # p74 -> p75
merge_after(P,"工作人员,除")       # p75 -> p76
save("ch02",P)

# ---------------- ch03 ----------------
P=load("ch03")
P[0]='### 情报科长“王庸”——陈赓'
P[1]='### 陈赓的传奇经历'
# restore OCR-clipped short line "客车。" (scan-verified, end of 1961 anecdote)
i=find_end(P,"三等"); P[i]=P[i]+'客车。”'
# Zhang Kexia block quote: join the 7 split quote-lines into one, then split off
# the p91 narration that welded onto its tail.
i=find_contains(P,"在上海期间,党派许多同志")
while "难以忘怀" not in P[i]:
    P[i]=P[i]+P[i+1]; del P[i+1]
split_at(P,"难以忘怀。陈","难以忘怀。")   # quote | "陈赓置身龙潭虎穴..."
merge_after(P,"革命委员会委员")    # p83 body -> p84 ("及其主席团成员...")
merge_after(P,"党中央交")          # p86 -> p87
merge_after(P,"副队")              # p92 -> p93 (钱大钧 bio)
merge_after(P,"调任国民党")        # -> p93 ("某菲"司令...辖区。)
split_at(P,"辖区。当年火车","辖区。")     # 钱大钧 bio | train narrative
save("ch03",P)
print("surgery done")
