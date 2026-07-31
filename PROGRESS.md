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

## B02 = Chapters 5 to 7 (ch05 to ch07) — DONE

Translated end to end: ch05 (3,845 chars, 119 paras), ch06 (10,183 chars, 220
paras), ch07 (5,317 chars, 144 paras); ~19,345 source chars, 483 paragraphs.
One bilingual QC file per unit; reading text and parity source generated with
split_bilingual.py. The bilingual `>` lines were assembled from the raw source
with a new helper (scripts/make_bilingual.py) so the source is copied, never
re-typed. Story: Yang Muci's undercover ordeal at Du Luning's secret Juntong
training school (the lovers Guo Ziqiong/He Yashan; the letter; the waltz; the
electrocution) and, in parallel, the Rong household homecoming (Rong Sheng saves
the fainting He Yashu; A-Chu among the maids; Rong Gui's begging; the moonlit
dance with Fourth Madam).

Checks run and what they found:
- Check 1, faithful verbatim quotation: each parity source (data/zh/<id>.txt)
  diffed line-for-line against the raw source paragraphs. ZERO content diffs on
  all three units (119/220/144 paras); the only diff reported is the source
  files' missing final newline. Every source paragraph quoted verbatim, none
  dropped or merged.
- Check 4a, check_numbers.py --noise data/noise.txt: 0 unresolved on all three
  units (and re-verified 0 on all five B01 units after the tooling fix below).
- Check 4b, check_structure.py --pairs: paragraph parity OK on all three.
- Check 2, blind double translation: Du Luning's Analects address (ch05), He
  Yashan's letter (ch06), and the Rong-gate opening description (ch07) were
  re-rendered blind and diffed; no substantive divergence. The one genuine
  hard/uncertain point (the ch06 chapter-title line) is footnoted, not smoothed.
- Check 3, round-trip back-translation: He Yashan's letter (ch06) was checked
  clause-by-clause against the source; every clause recovered, no omissions.
- Check 7, scholarship: ch05 title 时人不识凌云木 = Du Xunhe, Xiao song —
  CORROBORATED (received text 直待 vs the novel's 直到, noted); Analects 1.1/1.4
  quotations CORROBORATED; Dai Li / Juntong-1938 CORROBORATED (anachronism as at
  ch04). ch06 title 宫花旋落已成尘 — the palace-blossom trope is corroborated
  (Yuan Zhen 行宫 etc.), but the exact line is NOT traceable to a single canonical
  poem: UNCORROBORATED as a direct quotation, and the note says so. 救救孩子 =
  close of Lu Xun's A Madman's Diary — CORROBORATED. ch07 title 却疑春色在邻家 =
  Wang Jia, Yu qing — CORROBORATED; 老佛爷 = Cixi and 合浦珠还 (Book of the Later
  Han) — CORROBORATED.
- Check 8, paranoid audit: the three double-translated passages plus the
  back-translated letter (~22 paras, ~4.5% of the batch) got the full treatment
  (verbatim-quote, double, back-translation). Observed substantive error rate: 0.

Notes (10 this batch; continuous numbering assigned by the builder — B02 notes
are #14 to #23): ch05 x3 (title = Du Xunhe/小松; Analects 1.1/1.4; 戴局长 = Dai
Li), ch06 x4 (格格 Manchu title; 救救孩子 = Lu Xun; title = 宫花 palace-blossom
trope, uncorroborated as a direct quotation; 伯乐/千里马 idiom + the pirate-site
watermark left out of the reading text), ch07 x3 (title = Wang Jia/雨晴; 老佛爷 =
Cixi; 合浦珠还 idiom).

Glossary rows added: 11 people (Du Luning promoted to a full row on his reveal;
Yu Xiaojiang, Xin Lili, Guo Ziqiong, He Yashan, He Yashu, Xing'er, Chan'er, A-Fu,
the second young mistress, Director Dai), 9 organizations (Hangzhou Police School;
Hongxia, St. Mary's, Mingchen girls' schools; Huamei Bookstore; Tongji Hospital;
Shanghai Vernacular News; Women's Vanguard; Telecommunications Technology), 3
places (Liyun Pavilion, Moju Studio, Hongli Pavilion), 1 term (格格 gege).
Provisional (romanization mine): Hongxia/Mingchen girls' schools, Shanghai
Vernacular News, Women's Vanguard. Attested: St. Mary's Girls' School, Tongji
Hospital, Director Dai (Dai Li), gege. Recurring cast reused unchanged
(Rong Sheng, A-Chu, Jiang Lishui, Rong Gui, Lao Yu, Yang Muci).

Figures: none in this batch.

Source contamination handled (check 1 / rule 4): ch06 has one pirate-site
watermark line ("阳光中文网 www.sunshe.com…") appended to an authorial sentence
(伯乐总算遇到了千里马). Kept VERBATIM in the bilingual `>` line for parity, but only
the authorial sentence is rendered in the reading text; the watermark is
identified in the note at "thousand-li steed" rather than translated into the book.

Tooling fixes made this batch (both generic, recorded per CLAUDE.md):
- scripts/make_bilingual.py (new): assembles out/<id>_bilingual.md from a raw
  source .txt (2 metadata lines skipped) and a one-paragraph-per-line English
  file, guaranteeing the `>` source lines are copied, not re-typed. Errors out on
  a paragraph-count mismatch.
- scripts/check_numbers.py: gave 十多/几多 ("ten-odd/several") the same digit
  lookbehind the clock-minute patterns already use, so compound counts like
  二十多/三十多 (twenty-/thirty-odd) survive instead of the generic 十多 eating the
  十 and orphaning a bare 二 read as 2. Re-verified all B01 units still 0.
- data/noise.txt additions (non-quantity numerals flagged and confirmed): 二话
  (二话没说), 千锤百炼, 千里马, 四起 (掌声四起), 四溢 (酒香四溢), 隔三岔五, 百事
  (百事乖违), 千恩万谢, 十八、九 (age-range idiom), 王八 (贼王八 insult).

Flagged for the read-through:
- ch06 title (宫花旋落已成尘): echoes the Tang palace-blossom poems but is not a
  traceable quotation; rendered literally and footnoted as such.
- ch06 pirate-site watermark: verbatim in QC, out of the reading text, footnoted.
- ch05 poem variant 直到 vs received 直待: kept the source's 直到, noted.

Build: out/On a Hair Trigger.epub rebuilt, 8 of 36 units translated, 23 notes.
qa_epub.py PASS (36 documents, 1088 paragraphs, 23 references = 23 bodies = 23
backlinks, all links resolve).
