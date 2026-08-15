# Deep audit — The Rebel (叛逆者) / Bi Yu

Whole-book random-sample fidelity audit, run once at completion (B09).

## Method

- Population: every translated paragraph pair in the book — 2,158 pairs across
  all 51 units, taken from `data/zh/<id>.txt` (verbatim source) paired against
  `out/<id>_reading.md` (the reading translation). The two are parity-locked by
  `make_bilingual.py` and re-checked by `check_content.py`, so index i in one is
  index i in the other.
- Sample: 86 pairs = 4.0% of the population, drawn with Python `random.sample`
  under the FIXED seed `20260815` (reproducible: re-running the sampler yields
  the same 86). The draw touched 42 of the 51 chapters, spanning all four
  novellas.
- Each sampled pair was read source-against-translation and judged on the axes
  that matter here: meaning (is the sense the source's?), completeness (nothing
  dropped), fidelity of every name / number / place / unit, and — the class this
  work most fears — no invented content and no invented precision (definiteness
  the source withholds).

## Result

- Errors found in the 86-pair sample: **0**.
- No mistranslation, no omission, no displaced content, no fabricated sentence,
  no invented precision. Every number and named entity in a sampled source
  paragraph survived, exactly, into its pair (e.g. the thirteen buried men of
  ch45, the three days and three nights of ch26, the four years at a silent set
  of ch36, the two tire tracks of ch39).
- Idioms and set phrases in the sample were rendered to living English with the
  literal image carried where it earns a note (马革裹尸 → "shrouded in horsehide
  on the field," ch03; 伸头是一刀，缩头也是一刀 → "stick your neck out and it's
  the knife; pull it back and it's the knife all the same," ch38).

## Honest statistical statement

Zero errors in 86 sampled paragraphs does NOT prove a zero error rate. By the
rule of three, an observed 0 in n is consistent, at ~95% confidence, with a true
error rate up to about 3/n — here 3/86 ≈ **3.5%**. So the audit establishes that
the book's paragraph-level error rate is low (below roughly 3.5%), not that it is
nil. The scripted per-chapter gates (parity and verbatim quotation by
construction; numeric invariants; entity survival; alignment; content /
displacement) carry the rest of the assurance across the 100% of paragraphs the
sample does not reach.

## Invented-precision scan

A separate targeted grep of the closing batch's chapters (ch47–ch51) for the
invented-precision class — bare definite measures ("N weeks/days/miles"),
"exactly / precisely," and sharpened descriptors ("a tall man" where the source
has "a man") — returned nothing. Where the source is vague the translation stays
vague (方圆百里 → "within a hundred li"; 好一会儿 → "a good while"; 几天后 →
"some days later"). Definiteness is copied, never manufactured.

## First-appearance discipline

The batch's 28 new footnotes were checked against `notes.json` before authoring,
so nothing already covered book-wide was re-noted (New Year's Eve at ch39, li at
ch41, the political commissar at ch19, the stone memorial arch at ch09, the
cheongsam and silver dollar earlier). Each new note lands at the term's first
appearance in the book (the mu unit at ch49, the founding of New China at ch51),
and `check_apparatus.py` confirms every anchor resolves and the two note streams
are consistent.

## Sample (chapter#paragraph, fixed seed 20260815)

ch01#36, ch02#14, ch02#37, ch02#38, ch02#51, ch03#3, ch03#16, ch03#22, ch03#34,
ch03#40, ch04#10, ch04#17, ch04#23, ch04#27, ch05#24, ch06#15, ch06#28, ch07#7,
ch08#1, ch08#17, ch08#29, ch09#3, ch09#16, ch10#0, ch11#15, ch11#54, ch12#17,
ch12#38, ch13#12, ch17#6, ch17#26, ch18#25, ch19#24, ch20#45, ch21#46, ch23#20,
ch23#33, ch24#24, ch24#40, ch24#47, ch24#51, ch25#7, ch25#21, ch26#9, ch27#12,
ch28#6, ch29#12, ch29#14, ch29#17, ch31#23, ch31#44, ch33#37, ch34#22, ch34#43,
ch35#10, ch35#25, ch36#3, ch36#12, ch36#43, ch37#20, ch38#17, ch38#56, ch38#63,
ch38#76, ch39#1, ch39#14, ch39#20, ch39#34, ch39#37, ch39#46, ch39#53, ch40#4,
ch41#17, ch41#22, ch42#23, ch43#20, ch44#7, ch44#32, ch45#11, ch45#23, ch45#31,
ch45#33, ch48#7, ch48#26, ch49#13, ch50#15.
