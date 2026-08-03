# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->

## 2026-08-03 — Readability: typography normalized; register pass begun
Commissioner feedback: the book reads rough. Two causes found and addressed.

- GLOBAL typography (commit e24c96b): ch01-ch11 used curly quotes while
  ch12-ch35 used straight typewriter quotes; ellipses and apostrophes switched
  styles mid-book; a few !! survived from the source. All English prose is now
  uniform book typography (paired curly quotes, typographic apostrophes, real
  ellipses, single !). Note anchors, glossary en/pinyin fields, and book.json
  titles converted in lockstep. This supersedes the earlier same-day
  straight-apostrophe normalization of Hong'er/Yun'er/Yan'an (whole ledger and
  text are now consistently typographic).
- Register (commit 895d19c): the English at many points calqued the Chinese
  (铺天盖地 "a red that covered heaven and earth", 迅雷不及掩耳 "quick as a
  thunderclap that leaves no time to cover the ears", 水落石出 "until the water
  sinks and the stones show through") and kept the source's cinematic scene
  cards as bare body copy. Prologue (ch00) recast wholesale; ch01 smoothed at 9
  spots; scene cards now italic scene-setting lines. Content unchanged; anchors
  kept in step; all checks green.
- REGISTER_PASS.md written: the full instruction set for revising ch02-ch35
  (taxonomy, triage, ANALYZE/EXECUTE two-phase workflow, constraints, batch
  plan R01-R12). HANDOFF.md now carries the R01 kickoff.

## 2026-08-03 — Final whole-book QC read-through (accuracy, readability, apparatus)
A close bilingual pass over all 36 units against the source, plus an apparatus and
EPUB-structure audit. No critical defects; the fixes below are minor accuracy,
readability, and formatting corrections. Rebuilt, qa_epub PASS (117 refs = 117
bodies = 117 backlinks), parity OK and check_numbers 0 unresolved on all 36 units.

- GLOBAL (glossary.json): fixed 12 glossary note fields that used HTML numeric
  character references (`&#8216;` etc.). The builder plain-text-escapes glossary
  notes, so these rendered as literal `&#8216;` garbage in the back-matter
  glossary; replaced with literal Unicode punctuation. Entries: 汤少, 小山缨子,
  汪精卫, 东北军, 新中华报, 东方杂志, 申报, 桃山时代, 中国哲学简史, 曲线救亡,
  翠竹春晓, 伪满. (Chapter footnotes were never affected — notes.xhtml emits raw
  XHTML, so numeric refs are correct there.)
- LOCAL (glossary.json): normalized three romanizations from a curly to a straight
  apostrophe to match the shipped text — Hong'er (红儿), Yun'er (云儿), Yan'an (延安).
- notes.json: three new footnotes for reader clarity — ch14 flags the source's own
  汤少礼/汤少棋 (Tang Shaoli/Tang Shaoqi) name slip; ch24 glosses the 孙悟空/沙和尚
  (Monkey King / Sha Monk) pair from Journey to the West; ch35 glosses 格格 (gege).
  Note 21 disambiguated the Tang writer Han Yu (韩愈) from the character 韩禹.
- LOCAL accuracy fixes (bilingual + regenerated reading): ch02 restored the logic
  of 要是有名有姓 (a reversed negation); ch05 restored the dropped rank 少校 (Major)
  for Yu Xiaojiang; ch06 corrected a pronoun (the words are A-Chu's, "his" not
  "her"); ch11 "Hui" → "Cong Hui" (one rendering per referent); ch12 也许是
  "Perhaps not" → "Perhaps so" (a reversal).
- LOCAL readability fixes: ch00 "six toes on each foot" → "six toes" (六趾 does not
  say each foot); ch15 de-garbled 二丈金刚摸不着头脑 to plain sense; ch24 fixed a
  garbled 不想 clause and rendered opaque "Sandy" as "Sha Monk"; ch06 harmonized the
  elder sister's letter, quoted verbatim in ch06 and ch10, to read identically.
- LOCAL formatting: ch19/20/21 reading/bilingual H2 headings given the "Chapter NN."
  prefix (book.json and the EPUB TOC already carried it; correction-surface only).
- data/noise.txt: +1 row (二丈金刚) for the idiom numeral dropped by the ch15 fix.

## 2026-08-03 — B13 (Chapters 34-35), final batch: book complete
- Translated ch34 (反客为主深造次) and ch35 (一举锄奸雁归行), 524 paragraphs; the
  novel is now fully translated (36 of 36 units).
- 7 new footnotes (#108-#114); 9 new glossary rows; 4 non-quantity noise.txt rows
  (百川丛惠子, 五金, 万物, 万念俱灰). All checks green book-wide: verbatim parity zero
  diffs, check_structure parity OK and check_numbers 0 unresolved on all 36 units,
  qa_epub PASS (114 refs = 114 bodies = 114 backlinks).
- book.json translator_note: middle sentence updated for the finished book.
- Added COMPLETION.md (whole-book completion report).

