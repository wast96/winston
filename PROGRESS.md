# PROGRESS — On a Hair Trigger (一触即发) by Zhang Yong

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, chapter scope), which checks ran and what
they found, notes added (count and numbering), glossary rows added with status,
figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup

- Source EPUB: 一触即发 by Zhang Yong (张勇). Digital EPUB (Calibre-repackaged
  EasyPub text, internal timestamp 2015), reliable Unicode, no OCR. One embedded
  image (the cover). The source carries no notes of its own.
- Ingest (out/INGEST.md): 38 spine documents, 1 image, 232,092 source characters
  in total; of these the translatable content is 231,699 chars across the
  prologue and 35 chapters (the 目录 and cover pages are the remainder).
- Structure: the source's file boundaries DO match logical chapters (one spine
  file per chapter), so no merge/split was needed; the source's cover page and
  目录 were dropped from book.json because the builder regenerates a title page
  and a full hyperlinked contents. Flat book: Prologue (ch00) + ch01 to ch35,
  no sections or subsections.
- Batch plan: approved at a 21,000-char maximum, 13 batches (book.json
  "batches").
- Skeleton EPUB built to out/On a Hair Trigger.epub; scripts/qa_epub.py PASS
  (48 files, 42 documents, all links resolve). Kindle/Apple Books metadata and
  cover embedded.

## B01 = Prologue + Chapters 1 to 4 (ch00 to ch04) — DONE

Translated end to end: ch00 (Prologue, 506 chars), ch01 (4,017), ch02 (7,826),
ch03 (3,809), ch04 (3,883); ~20,041 source chars. One bilingual QC file per unit
(out/<id>_bilingual.md), reading text and parity source generated with
split_bilingual.py. The book is flat: one H2 couplet title per chapter, then
continuous prose; source scene breaks rendered as paragraph breaks.

Checks run and what they found:
- Check 1, faithful verbatim quotation: each parity source (data/zh/<id>.txt) was
  diffed line-for-line against the raw source paragraphs (data/src, minus the two
  metadata lines). ZERO diffs across all five units (21/100/191/133/133 paras) —
  every source paragraph quoted verbatim, none dropped or merged.
- Check 4a, check_numbers.py --noise data/noise.txt: 0 unresolved on all five
  units. Two fixes were needed to make it usable, both recorded below.
- Check 4b, check_structure.py: paragraph parity OK on all five; heading shape
  uniform (1 distinct shape); note anchors 13 written, 0 unresolved, 0 waived
  (3 attach at first of several occurrences, expected); glossary drift 0.
- Check 2, blind double translation (separate contexts): the Prologue, the
  A-Chu/Rong Sheng spring-grass exchange (ch02), the Cong Feng dockside
  confrontation (ch02), and Yang Muci's nightmare (ch04) were each re-translated
  blind and diffed. No substantive divergence — these passages are unambiguous.
- Check 3, round-trip back-translation: the ch03 reveal ("you have not been ill
  at all…") was back-translated to Chinese in a fresh context; every clause of
  the source recovered, no omissions.
- Check 7, scholarship: Xuantong reign-years (1910/1911) corroborated; Cao Pi's
  Yan ge xing (ch01 title) corroborated; Meng Jiao's Youzi yin / 春晖 (ch02 title)
  corroborated; Communist Manifesto London Feb 1848 and 1888 English ed.
  corroborated; Declaration of the Rights of Man 1789 corroborated; Daodejing
  飘风 corroborated; CCP 特科 (1927, Shanghai) corroborated; 军统 as a named organ
  dates to 1938, so its 1931 use is a mild anachronism — flagged in the ch04 note.
- Check 8, paranoid audit: the four blind-double passages plus the back-translated
  passage (~65 lines, ~4% of the batch) got the full treatment. Observed
  substantive error rate: 0.

Notes (13; continuous numbering assigned by the builder in reading order):
ch00 x1 (Xuantong reign), ch01 x3 (Bannermen; Jinlian/golden-lotus; ch01 title =
Cao Pi), ch02 x3 (Manifesto 1848 fact-check; Dream of the Red Chamber name-cluster;
ch02 title = Meng Jiao/春晖), ch03 x3 (沉塘 lineage drowning; source's 威尔逊卡迪芙
slip for 威尔士; ch03 title = 同林鸟 proverb), ch04 x3 (Juntong/特科 orgs + 军统
anachronism; 飘风/时雨 codenames; ch04 title = 阴差阳错 idiom).

Glossary rows added: 30 people, 11 organizations, 15 places, 8 terms. One decided
rendering per referent (pinyin). Provisional (romanization mine, not attested in
English scholarship): Fenghui Bank (丰汇银行), the Lanxin Western Restaurant
(兰心西餐厅), Yu'er (瑜儿). Attested forms used for real referents (CCP, 特科, Tokyo
Imperial University, Communist Manifesto, place names, Bannermen, xiao).

Figures: none in this batch (the source's only image is the cover, already wired
into the builder).

Tooling fixes made this batch (both generic, recorded per CLAUDE.md):
- scripts/check_numbers.py: the two `十分` noise entries ("very"/十几) were eating
  the `十分` inside clock minutes (二十分, 三十分), corrupting e.g. 20 -> 2. Added a
  negative lookbehind so 十分/十几 are stripped only when 十 is not preceded by a
  digit; clock minutes now survive. Also added the date ordinal "sixteenth": 16 to
  WORD_NUM (the book spells out "the sixteenth of March", 3月16日).
- data/noise.txt (new): project noise list for non-quantity numerals flagged this
  batch (五彩斑斓, 万状, 千金, 两个字, 三步 [waltz], 正儿八经, 十足, 千刀万剐, 四溅,
  两眼, 二人, 七荤八素, 第二天). Pass with --noise data/noise.txt.

Flagged for the read-through:
- 威尔逊卡迪芙 (ch03): treated as a source slip for 威尔士 (Wales) Cardiff; footnoted.
- 军统 in a 1931 scene: mild anachronism, footnoted rather than altered.
- 瑜儿 (ch01): appears to be Master Rong's pet name (瑜); marked provisional.
- The Rong Chu / A-Chu / Yang Muci "who is who" doubling is deliberately left
  unglossed so as not to spoil; names are all in the glossary.

Build: out/On a Hair Trigger.epub rebuilt, 5 of 36 units translated, 13 notes.
qa_epub.py PASS (48 files, 42 documents, 13 references = 13 bodies = 13 backlinks,
numbering sequential, all links resolve).
