# ch05 revision edits (R3 sweep) — TIER 1+2, mechanical/tic only

Applied with `python3 scripts/apply_edits.py ch05`. Every OLD occurs exactly
once; every edit is a single-word/phrase substitution or a phrase recast that
cannot move a paragraph boundary (parity invariant by construction). No numeral
changes. Note-body date reformats are handled separately in notes.json.

ch05 is the last big narrative chapter and the only R3 chapter with genuine
defects; ch06-ch11 are near-KEEP (obituary, posthumous writings, chronology,
references, afterword) and take zero prose edits. KEEP honoured here: the two
1961 letters ({v}, lines 175/183), the forged "Notice of Wu Hao and Others"
(document title, lines 47-50), the {p} verse (line 79), the 13 precepts (lines
136-148, Chen's posthumous voice), and the author's institutional first person.
ch05 uses em dashes already (41 of them), so the two 等-tag recasts reuse the
existing appositive dashes and introduce none.

## TIER 1 — Politburo (政治局 -> "the Politburo", never "Political Bureau")

### p042 T1 TOUCH
OLD: only four members of the Party's Central Political Bureau remained in Shanghai
NEW: only four members of the Party's Central Politburo remained in Shanghai
WHY: 政治局 = Politburo (shelf canon); "Political Bureau" is a bare calque.

# The note anchored on this clause must move with the prose edit:
NOTE-ANCHOR
OLD: only four members of the Party's Central Political Bureau remained in Shanghai
NEW: only four members of the Party's Central Politburo remained in Shanghai

### p045 T1 TOUCH
OLD: a provisional Central Political Bureau
NEW: a provisional Central Politburo
WHY: 政治局 = Politburo (no note/figure anchor on this span).

## TIER 1 — White Terror (白色恐怖 -> "the White Terror", the specific KMT terror)

### p081 T1 TOUCH
OLD: back in the days of the white terror, when he was in the Central Special Branch
NEW: back in the days of the White Terror, when he was in the Central Special Branch
WHY: 白色恐怖, the specific post-1927 Shanghai terror (the Gu Shunzhang-defection
     era); definite named use, not the generic carve-out.

## TIER 1 — ellipsis in narration -> period

### p074 T1 TOUCH
OLD: the Panmunjom talks during the War to Resist America and Aid Korea...
NEW: the Panmunjom talks during the War to Resist America and Aid Korea.
WHY: trailing "..." in narration (the career-sweep sentence before "Who was
     he?"); plan sec.3.2 keeps "..." only inside quotations the source truncates,
     narration gets a period. The note anchor "the Panmunjom talks during the War
     to Resist America and Aid Korea" is preserved verbatim (only the trailing
     dots change).

## TIER 2 — litotes calque -> stated positively

### p053 T2 TOUCH
OLD: he handled no small number of grave matters
NEW: he handled a good many grave matters
WHY: 不少; "no small number of" litotes calque -> "a good many" (narration; not
     in a {v} block or quoted matter).

## TIER 2 — 等-tags: vary the dominant "and others" (thin, don't zero it)

# "and others" dominates ch05's list-closers (~10 hits vs "and the others"/"and
# the rest"); front two as "among them" appositives, reusing the existing em
# dashes. Both spans are clear of note and figure anchors.

### p017 T2 TOUCH
OLD: Li Shiying, Xu Jianguo, Wang Jinxiang, Zhou Xing, and others
NEW: among them Li Shiying, Xu Jianguo, Wang Jinxiang, and Zhou Xing
WHY: vary the dominant "and others" tag to a fronted "among them" appositive.

### p026 T2 TOUCH
OLD: Chen Yi, Pan Hannian, Li Shiying, Wu Kejian, Liang Guobin, Wang Fan, Yang Fan, and others
NEW: among them Chen Yi, Pan Hannian, Li Shiying, Wu Kejian, Liang Guobin, Wang Fan, and Yang Fan
WHY: vary the dominant "and others" tag to a fronted "among them" appositive.
