# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4), B02 (Chapters 5 to 7), B03 (Chapters 8 to 10), B04 (Chapters 11
to 13), B05 (Chapters 14 to 15), B06 (Chapter 16) and B07 (Chapters 17 to 18) are
DONE, checks green, committed. Batch B08 is next.

## Message to paste into the next chat

```
Hair Trigger B08 — Chapters 19 to 21 (ch19, ch20, ch21).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B08 end to end: Chapter 19 (ch19, ~6,486
source chars), Chapter 20 (ch20, ~6,823 chars) and Chapter 21 (ch21, ~6,096 chars),
~19,405 chars total. This continues the novel from Batch B07 (the Prologue and
Chapters 1 to 18 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch18 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title").

Read each unit's source from data/src/ (ch19 = 22_part0020.txt, ch20 =
23_part0021.txt, ch21 = 24_part0022.txt). Translate to the register in CLAUDE.md:
clean, flowing novelistic English, the book's own voice, all apparatus in the notes
and nothing inline.

Author each reading text WITHOUT re-typing the source: write out/<id>_en.txt with
one English paragraph per line (same count and order as the source paragraphs),
then run
  python3 scripts/make_bilingual.py data/src/<file> out/<id>_en.txt <id> "## H2 <english chapter title from book.json title_en>"
which assembles out/<id>_bilingual.md with the source `>` lines copied verbatim
(it errors on a paragraph-count mismatch). Then
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
generates out/<id>_reading.md and the parity source data/zh/<id>.txt. The book is
flat: one H2 couplet title per chapter, then continuous prose, no sections/
subsections; source scene breaks are separate source paragraphs, rendered as
paragraph breaks. Watch for mid-sentence paragraph splits in the source (ch08,
ch12, ch14 each had one; ch15 had a mid-word split in the 梨花落 aria; ch16, ch17,
ch18 had none — but ch17 line 109 韩正齐惊惶失措； is a complete single-clause
paragraph paired with line 110, a parallel couplet, NOT a split): if a real
mid-sentence split occurs, keep the parity count, render each source line as its
own paragraph, and split the English at the matching point.

Run the checks and record them in PROGRESS.md, per unit:
- scripts/check_numbers.py --noise data/noise.txt out/<id>_bilingual.md  (must be
  0 unresolved). The non-quantity noise list lives in data/noise.txt; ADD to it
  (or to WORD_NUM in check_numbers.py for spelled-out ordinals your prose uses)
  whenever a NON-quantity numeral is flagged, and record what you added. Do NOT
  drop a real date/year/time; render clock times so their digits survive (e.g.
  "three thirty", "two twenty-five", not "half past three"). The checker protects
  clock hours (十一点/十二点), clock minutes and "-odd" counts, and maps English
  month names to their number (so "November" credits 11月). Watch the fraction
  trap: a built-in 万分 rule can fragment 五万分之一 / 十X万分之一 — noise the residue.
  Names and idioms containing a numeral (e.g. 黄三元, 刘阿四, 土肥原贤二, 一了百了,
  一百八十度) get noised, not dropped — B07 added ten such rows to data/noise.txt.
- scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md  (parity
  must be OK). Also sanity-check verbatim fidelity by diffing data/zh/<id>.txt
  (minus its first ### title line) against the source paragraphs (data/src file,
  minus its first two metadata lines) — aim for zero content diffs (the source
  files' missing final newline is the only expected diff).
Apply blind double translation and round-trip back-translation to the argumentative
or lyrical passages and sample the plain narration; give 3 to 5 percent of the
batch the full paranoid audit and report the observed error rate.

Footnotes into notes.json (about 3 per chapter-equivalent, so ~8 or 9 across the
three chapters; anchors must be exact verbatim substrings of the English prose —
the builder REFUSES to build on an unmatched anchor, so verify each with a quick
grep -c before building; XHTML bodies use NUMERIC character references only, e.g.
&#8212; &#8216; &#8217; &#8211;, never named entities; hanzi may be written
literally). For each chapter the title couplet is the first thing to footnote,
anchored to a thematically apt verbatim phrase in that chapter's prose (the H2
chapter title itself does not take a note ref). ch19 = 梅花一夜漏春工, ch20 =
一笑相逢哪易得, ch21 = 千钧一发箭在弦 (this one is the source of the book's own title,
一触即发 / "on a hair trigger" — trace it and connect it): trace each against
scholarship and say corroborated / uncorroborated / contradicted, and footnote it.
If a title or line is not a traceable quotation, render it literally and footnote it
as such. Recurring literary refs get their note at FIRST appearance only (already
noted: 梨花落 aria at Chapter 12; 小松 杜荀鹤 at Chapter 5; the 瀑布联句 waterfall poem
at Chapter 15; 西厢记 at Chapter 16; 陆羽 六羡歌 and Cao Zhi 七步诗 at Chapter 17).

Glossary rows into glossary.json for every NEW name, place, org and term, one
decided rendering per referent — CHECK the existing glossary first and reuse those
renderings. Recurring cast: the two twins — Yang Muci (杨慕次, familiar 阿次 = A-Ci,
the Party's man, now a major/adjutant in the Detective Division of the Central
Shanghai Garrison Command, holding the captured Japanese "Imperial Flower" survey
maps and running a Comintern-delegate escort under Fang Zhitong) and Yang Muchu /
A-Chu (杨慕初/阿初, the Golden Dragon chief) — plus Xin Lili (辛丽丽), Rong Chu (荣初),
Han Yu (韩禹, now leverage-in-hand, his father Han Zhengqi dead by his own hand at
the end of ch18), Xia Yuechun (夏跃春), Young Tang (汤少), Du Luning (杜旅宁), Yu
Xiaojiang (俞晓江), Ronghua (荣华, CCP Special Branch), Huang Sanyuan (黄三元, Hongmen
+ French Concession police, A-Chu's sworn brother), the impostor "Xu Yuzhen"
(徐玉真), Yang Yuhua (杨羽桦, the uncle A-Chu has sworn to kill), Yang Yubo (杨羽柏), the
Golden Dragon Society, the Hongmen (洪门), the CCP Special Branch vs Juntong. Keep
one rendering per referent across the whole book. NOTE the twin-name slip: the
source occasionally prints 杨慕次 where the scene is plainly Muchu/A-Chu (and vice
versa is possible) — render by context and, at first occurrence in a chapter,
footnote the slip rather than silently reconciling; 阿次 = A-Ci is Muci's genuine
familiar name, not a slip.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/on-a-hair-trigger, and rewrite
HANDOFF.md with a paste-ready B09 kickoff (B09 = ch22 to ch24). Cite chapters,
never page numbers. Never invent bridging text or silently drop material; footnote
genuine ambiguity and leave it visible. If a source carries a pirate-site watermark
line (as ch06 did), keep it verbatim in the bilingual `>` line but leave it out of
the reading text and footnote it. Do not pause for approval mid-batch. When done,
deliver out/On a Hair Trigger.epub to me as an attached file in the chat.
```

## What is DONE (do not redo)

- Step 0: ingested source.epub, authored book.json (final), survey approved,
  skeleton EPUB built, QA green. Kindle/Apple Books metadata + cover wired in.
- Batch B01 = Prologue (ch00) + Chapters 1 to 4 (ch01 to ch04), ~20,041 chars.
  13 footnotes (#1 to #13). See PROGRESS.md.
- Batch B02 = Chapters 5 to 7 (ch05 to ch07), ~19,345 chars, 483 paragraphs.
  10 footnotes (#14 to #23), 24 new glossary rows. See PROGRESS.md.
- Batch B03 = Chapters 8 to 10 (ch08 to ch10), ~15,194 chars, 419 paragraphs.
  9 footnotes (#24 to #32), 24 new glossary rows. See PROGRESS.md.
- Batch B04 = Chapters 11 to 13 (ch11 to ch13), ~18,985 chars, 512 paragraphs.
  10 footnotes (#33 to #42), 15 new glossary rows. See PROGRESS.md.
- Batch B05 = Chapters 14 to 15 (ch14 to ch15), ~20,027 chars, 514 paragraphs.
  7 footnotes (#43 to #49), 11 new glossary rows. See PROGRESS.md.
- Batch B06 = Chapter 16 (ch16), ~11,004 chars, 320 paragraphs. 5 footnotes
  (#50 to #54). See PROGRESS.md.
- Batch B07 = Chapters 17 to 18 (ch17 to ch18), ~15,534 chars, 378 paragraphs.
  Bilingual QC files, reading files, parity sources, 7 footnotes (#55 to #61) and
  ~25 new glossary rows all written; check_numbers 0 unresolved (11 noise.txt
  additions), check_structure parity OK (251/251, 127/127), verbatim parity zero
  content diffs, blind double translation on 6 passages + round-trip back-
  translation on 6 + paranoid audit ~3.4% (1 addition found and fixed). See
  PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 19 of 36 units translated, 61 notes, qa green.

## What is NEXT

- Batch B08 = ch19 to ch21 (~19,405 chars). Then B09 = ch22 to ch24, and so on
  through B13 = ch34 to ch35 (see book.json "batches").

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another branch, but fold all work onto claude/on-a-hair-trigger and retire
  any stray branch (the B02..B07 stray batch branches were each folded on and
  deleted).
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). A fresh
  container has only source.epub + the committed out/*_bilingual.md, notes.json,
  glossary.json, book.json, data/noise.txt. Re-run ingest_epub.py to rebuild
  data/src; re-run split_bilingual.py on each committed bilingual (ch00..ch18) to
  rebuild data/zh and out/*_reading.md BEFORE building (the builder reads the
  reading files).
- Authoring flow (established B02): write out/<id>_en.txt (one English paragraph
  per source paragraph), then scripts/make_bilingual.py to get the bilingual with
  verbatim `>` source lines, then split_bilingual.py. Do NOT hand-type the source
  into the bilingual.
- Source structure: one spine file per chapter; single H2 couplet title; no h3/h4;
  scene breaks are separate source paragraphs, rendered as paragraph breaks. The
  source carries NO notes of its own; every note is the translator's. Watch for
  mid-sentence paragraph splits (ch08, ch12, ch14 each had one; ch15 had a mid-word
  split in the 梨花落 aria; ch16, ch17, ch18 had none); keep the parity count, render
  each source line as its own paragraph and split the English at the matching point.
- check_numbers noise: data/noise.txt is the project non-quantity list; ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. The checker protects clock hours/minutes and "-odd" counts via digit
  lookbehinds; maps English month names to their number (November -> 11); WORD_NUM
  knows one..thirteen, teens, tens, and first..tenth ordinals. Prefer rendering a
  quantity so its digit survives over noising it; noise only genuine non-quantity
  numerals (idioms, names, 零 in 凋零/飘零, bachelor-slang 五 in 王老五, etc.). Names and
  idioms carrying a numeral get noised: B07 added 贤二, 下三烂, 万端, 一了百了, 百试百灵,
  三元, 千羡万羡, 十五、六, 一百八十度, 阿四. TRAP: the built-in 万分 rule fragments the
  fraction 五万分之一 / 十万分之一 (a stray 十/五) — noise the residue, not the whole
  fraction.
- Reign-era dates appear beside their Western years; keep both, and let
  check_numbers see the Western year. Japanese Shōwa era also appears (Shōwa 4 =
  1929); render both the era number and the Western year.
- Deliverable filename has a space: quote it, "out/On a Hair Trigger.epub".
- Write JSON via a file (not shell heredocs) so Chinese glyphs are not mangled;
  re-read to verify (and scan `en` fields for stray hanzi). XHTML note bodies use
  numeric character references only.
- Recurring names AND recurring literary allusions get their note at FIRST
  appearance in the book; reuse glossary renderings, do not re-romanize. Already
  footnoted: 梨花落 aria (情探 / 王魁负桂英) at Chapter 12; 小松 (杜荀鹤) at Chapter 5;
  the 瀑布联句 waterfall poem at Chapter 15; 西厢记 at Chapter 16; 陆羽 六羡歌 and
  Cao Zhi 七步诗 at Chapter 17; the September 18th Incident at Chapters 16 and 17.
- Prose written TO the commissioner (this HANDOFF, PROGRESS, chat) uses no em
  dashes (CLAUDE.md rule 6); the translation itself may use them.
- Plot state after B07: A-Chu (杨慕初/阿初) sprang his trap at a Japanese tearoom in
  the French Concession: he holds Han Yu, sent the impostor "Xu Yuzhen" off carrying
  the dismembered kidnappers (including a Japanese agent, Sakai Ichirō) as a "gift"
  for Yang Yuhua, and then drove Han Zhengqi to shoot himself after laying out the
  full truth — that the real Xu Yuzhen (A-Chu's birth mother) was murdered about
  twenty years ago at the Ciyun Temple and replaced by an impostor allied with Yang
  Yuhua; Han Zhengqi was the seduced accomplice; Yang Mulian (the sister) shielded
  A-Chu and was killed by the impostor. A-Chu is now sworn brother to Huang Sanyuan
  (Hongmen + French Concession police); Xia Yuechun and Young Tang overheard the
  "play behind the screen." On the other track, Muci (杨慕次/阿次), the Party's man,
  holds the captured Japanese "Imperial Flower" survey maps (drawn under Doihara
  Kenji) and is set to escort a Comintern delegate to an enlarged Central Special
  Committee meeting under Fang Zhitong; he noticed the mapmaker's handwriting is
  one he has "seen before."
- Twin-name slip: source has printed 杨慕次 for Muchu/A-Chu at ch16 (#50) and ch17
  (#60, once, in the tearoom scene); footnoted at first occurrence per chapter and
  rendered by context. Expect more; render by context. 阿次 = A-Ci is genuine.
- Anachronism flags recorded in glossary notes: fabi (法币, 1935) used loosely for
  the early-1930s present; the Park Hotel (国际大饭店, opened 1934) named a little
  before its time. The "Liyang Society"/"Eastern Institute" (立洋社/东洋学馆) are
  unattested Japanese-spy fronts of the novel (footnote #57).
