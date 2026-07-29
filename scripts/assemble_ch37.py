#!/usr/bin/env python3
"""Assemble out/ch37_bilingual.md for the two-section Appendix.

ch37 is ONE chapter (Appendix) with TWO H3 sections built from two source files:
  40_part0038.txt -> Material One   (skip 未知, 附录, 材料一; body = the rest)
  41_part0039.txt -> Material Two   (skip 未知, 材料二, 在相关...; body = the entries)
Source paragraph lines are read VERBATIM; English comes from the two JSON arrays.
The section subtitle line (在相关行动中牺牲的中共地下组织成员) is folded into the
Material Two H3 heading, matching book.json's ch37s02 title.
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def lines(p):
    return [l.rstrip("\n") for l in open(os.path.join(ROOT, p), encoding="utf-8")]

f40 = [l for l in lines("data/src/40_part0038.txt")]
f41 = [l for l in lines("data/src/41_part0039.txt")]
# f40: [0]未知 [1]附录 [2]材料一 [3:]body
# f41: [0]未知 [1]材料二 [2]在相关... [3:]body
body_a = [l for l in f40[3:] if l.strip()]
body_b = [l for l in f41[3:] if l.strip()]
en_a = json.load(open(os.path.join(ROOT, "out/ch37a_en.json"), encoding="utf-8"))
en_b = json.load(open(os.path.join(ROOT, "out/ch37b_en.json"), encoding="utf-8"))
assert len(body_a) == len(en_a), "Material One: %d src vs %d en" % (len(body_a), len(en_a))
assert len(body_b) == len(en_b), "Material Two: %d src vs %d en" % (len(body_b), len(en_b))
assert f40[1] == "附录" and f40[2] == "材料一", ("unexpected f40 heads: %r" % f40[:3])
assert f41[1] == "材料二", ("unexpected f41 heads: %r" % f41[:3])

out = ["## H2 Appendix", "## H3 Material One"]
for zh, en in zip(body_a, en_a):
    out += ["> " + zh, en]
out += ["## H3 Material Two: Members of the CCP Underground Organization "
        "Who Died in the Related Operations"]
for zh, en in zip(body_b, en_b):
    out += ["> " + zh, en]
dest = os.path.join(ROOT, "out/ch37_bilingual.md")
open(dest, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("wrote %s (Material One %d + Material Two %d = %d pairs)"
      % (dest, len(body_a), len(body_b), len(body_a) + len(body_b)))
