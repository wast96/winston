# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->

## 2026-08-03 — Register pass R02 (ch07 to ch11)
Second execution batch of the register pass (REGISTER_PASS.md): style-only prose
revision plus footnote densification. Content frozen; no source line touched, no
paragraph merged or split, names per glossary.json. Edit lists committed under
edits/. Book-wide notes 149 to 170.

- ch07: 2 prose touches (眼高手低 "high of eye and low of hand" to "her sights set
  high and her gifts modest"; 虎头蛇尾 "a tiger's head and a snake's tail" to
  "began with a flourish and trailed off to nothing"). 6 notes (New Year print
  年画; kowtow 磕头; burning incense to the ancestors; Qingming 清明节; Guanyin
  观音 and charitable merit; Tongji Hospital 同济医院). Now 9.
- ch08: 1 prose touch (急风暴雨 "wind and rainstorm" to "whirlwind"). 5 notes
  (qipao 旗袍; Longjing 龙井 tea; "white medicine" 白药; Shanghai Garrison Command;
  the Yan'an anachronism). Now 8.
- ch09: 0 prose touches. 2 notes (spirit-tablet 灵牌; death-day 祭日). Now 5.
- ch10: 0 prose touches. 3 notes (jade bangle 玉镯; French Park / French Concession;
  the 温补 warming-tonic decoction). Now 6.
- ch11: 0 prose touches. 5 notes (family discipline 家法; temple lot-drawing 求签;
  bird's-nest soup 燕窝银耳; Chinese painting's scattered-point perspective;
  Han Yu's 不平则鸣). Now 9.

Checks: parity OK all five (144 / 170 / 120 / 129 / 190); check_numbers 0
unresolved; straight-quote guard clean; spot-audit of the whole touched set, no
drift. Rebuilt out/On a Hair Trigger.epub, qa_epub PASS (170 refs = 170 bodies =
170 backlinks).

## 2026-08-03 — Register pass R01 (ch02 to ch06, plus ch00 note backfill)
First execution batch of the register pass (REGISTER_PASS.md): style-only prose
revision plus footnote densification. Content frozen; no source line touched, no
paragraph merged or split, names per glossary.json. Edit lists committed under
edits/. Book-wide notes 129 to 149.

- ch02: 3 prose touches (opening scene card italicized; "the laughter of the two
  of them" to "their"; "the tip of Cong Hui's toe" to "the tips of her toes").
  5 notes (household bond-servant 家奴; the 私塾/洋学堂 school divide; the xiao;
  opium and the pipe; the Confucian 报恩 gratitude-debt). Now 8 notes.
- ch03: 1 prose touch (咬金嚼铁, "teeth set like grinding iron" to "jaw set like
  iron"). 3 notes (the karmic-foe idiom 冤家; the meaning of being made to kneel;
  the traditional-medicine 虚不受补 behind the tonic self-poisoning). Now 6.
- ch04: 1 prose touch (opening scene card italicized). 3 notes (the "iron
  rooster" miser; the 1927 rupture and White Terror behind the CCP underground;
  the Soviet base areas 苏区). Now 6.
- ch05: 0 prose touches (already-clean action and interrogation). 1 note (the
  storm-before-upheaval allusion 山雨欲来风满楼). Now 4.
- ch06: 1 prose touch (春葱, "fingers like spring scallion sprouts" to "slender,
  tapering fingers"). 5 notes (elite Shanghai girls' schools; the Butterfly
  Lovers behind the paper butterflies; the cupped-hand bow 长揖; the earth-god
  shrine 土地庙; the Bund 上海滩 with 英雄救美). Now 9.
- ch00: note backfill only (prose was done in 895d19c). 3 notes (the pear-blossom
  and parting motif; the peony as emblem of rank; the golden-lotus bound foot).
  Now 4.

Per chapter: parity OK, check_numbers 0 unresolved (data/noise.txt unchanged),
straight-quote guard clean. Rebuilt out/On a Hair Trigger.epub; qa_epub PASS
(149 refs = 149 bodies = 149 backlinks). Spot-audit of all 6 edited paragraphs
against source: no meaning drift.

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
- Footnote policy raised (commissioner): the reader is a Westerner with no
  background in Chinese custom; the old ~3-notes-per-chapter calibration
  under-annotated. CLAUDE.md density rule rewritten (expect 8-15 per chapter,
  coverage-driven); REGISTER_PASS.md gains "The annotation gap" workstream and
  NOTE-ADD edit-list blocks; R01 backfills ch00/ch01. Two model notes seeded in
  ch01: wedding red, and the First/Second/Third/Fourth Madam hierarchy (now 119
  notes; qa green).
- ch01 note-densification backfill done ahead of R01 (commissioner asked what
  else ch01 needed): ten notes added under the new policy: the bridal sedan
  chair (and its blue-satin opposite), the lamp-flower double-bloom omen and
  wedding-night curtain, the three-years mourning rite, an honest check of the
  "extreme penalty" legal claim against the Qing Code (contradicted; the clan
  danger corroborated), the cold palace, birth-sign clashes, the ghost
  stand-in belief, the longevity lock, the moon gate, and gan-son nominal
  kinship. ch01 now 15 notes; book 129; qa green.
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

