# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4), B02 (Chapters 5 to 7), B03 (Chapters 8 to 10), B04 (Chapters 11
to 13), B05 (Chapters 14 to 15), B06 (Chapter 16), B07 (Chapters 17 to 18) and B08
(Chapters 19 to 21) are DONE, checks green, committed. Batch B09 is next.

## Message to paste into the next chat

```
Hair Trigger B09 — Chapters 22 to 24 (ch22, ch23, ch24).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B09 end to end: Chapter 22 (ch22, ~8,986
source chars), Chapter 23 (ch23, ~5,211 chars) and Chapter 24 (ch24, ~6,626 chars),
~20,823 chars total. This continues the novel from Batch B08 (the Prologue and
Chapters 1 to 21 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch21 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title").

Read each unit's source from data/src/ (ch22 = 25_part0023.txt, ch23 =
26_part0024.txt, ch24 = 27_part0025.txt). Translate to the register in CLAUDE.md:
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
ch12, ch14 each had one; ch15 had a mid-word split in the 梨花落 aria; ch16 through
ch21 had none): if a real mid-sentence split occurs, keep the parity count, render
each source line as its own paragraph, and split the English at the matching point.

Run the checks and record them in PROGRESS.md, per unit:
- scripts/check_numbers.py --noise data/noise.txt out/<id>_bilingual.md  (must be
  0 unresolved). The non-quantity noise list lives in data/noise.txt; ADD to it
  (or to WORD_NUM in check_numbers.py for spelled-out ordinals your prose uses)
  whenever a NON-quantity numeral is flagged, and record what you added. Do NOT
  drop a real date/year/time; render clock times so their digits survive (e.g.
  "three thirty", "two twenty-five", not "half past three"). The checker protects
  clock hours (十一点/十二点) and clock minutes and "-odd" counts via digit
  lookbehinds; maps English month names to their number (so "November" credits
  11月). Watch the fraction trap: a built-in 万分 rule fragments 五万分之一 /
  十X万分之一 — noise the residue. Watch the built-in 几十 rule too: it strips 几十 out
  of 几十万 and leaves a stray 万(=10000) before the following char — noise that
  residue (B08 noised "万的输赢"). Names and idioms containing a numeral (e.g. 黄三元,
  刘阿四, 土肥原贤二, 一了百了, 一百八十度, 八、九十分, 百乐门, 四目, 百无聊赖, 四肢, 四周)
  get noised, not dropped — B08 added ten such rows to data/noise.txt.
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
&#8212; &#8216; &#8217; &#8211; &#160;, never named entities; hanzi may be written
literally). For each chapter the title couplet is the first thing to footnote,
anchored to a thematically apt verbatim phrase in that chapter's prose (the H2
chapter title itself does not take a note ref). ch22 = 截断众流大气魄, ch23 =
恶氛弥天血火焚, ch24 = 风雨未肯收余寒: trace each against scholarship and say
corroborated / uncorroborated / contradicted, and footnote it. If a title or line
is not a traceable quotation, render it literally and footnote it as such (many of
this book's titles are the author's own seven-character lines in the old manner:
ch17, ch19, ch20 were all found to be author's pastiche, not verifiable quotations).
Recurring literary refs get their note at FIRST appearance only (already noted:
梨花落 aria at Chapter 12; 小松 杜荀鹤 at Chapter 5; the 瀑布联句 waterfall poem at
Chapter 15; 西厢记 at Chapter 16; 陆羽 六羡歌 and Cao Zhi 七步诗 at Chapter 17; Yu Xuanji
鱼玄机 at Chapter 19; the 月份牌 calendar poster at Chapter 19; Pushkin "To the Sea"
and Dostoevsky "The Insulted and the Injured" at Chapter 20; Mencius 孟子 "水无有不下"
at Chapter 20; 千钧一发 韩愈 and 箭在弦上 陈琳 at Chapter 21).

Glossary rows into glossary.json for every NEW name, place, org and term, one
decided rendering per referent — CHECK the existing glossary first and reuse those
renderings. Recurring cast: the two twins — Yang Muci (杨慕次, familiar 阿次 = A-Ci,
the Party's man / codename Drifting Wind 飘风, a major and adjutant in the Detective
Division of the Central Shanghai Garrison Command) and Yang Muchu / A-Chu (杨慕初/
阿初, the Golden Dragon chief) — plus Ronghua (荣华, CCP Special Branch), Cong Feng
(丛锋, the Comintern delegate now lodged at Plum Blossom Lane) and Cong Hui (丛惠),
Rong Chu / Rong'er (荣初/荣儿, groomed to play the Rong young master), Amah A-Yue
(岳嬷嬷/阿岳, the burn-scarred nurse), Xin Lili (辛丽丽), He Yashu (和雅淑), Young Tang
(汤少), Xia Yuechun (夏跃春), Du Luning (杜旅宁), Huang Sanyuan (黄三元), Han Yu (韩禹),
Yang Yuhua (杨羽桦, living under the murdered Yang Yubo's 杨羽柏 identity, Muci's
"father"; the impostor "mother" 徐玉真; A-Chu has sworn to kill Yang Yuhua). NEW in
B08 and already in glossary: Li Qinhong (李沁红, "the Flower of Juntong"), Xiong Zida
(熊自达, chief of the Detective Division), Gao Lei (高磊 = Captain Gao), Staff Officer
Ming (明参谋), Xiang (向 = Fang Zhitong's underground cover-surname; 方致同 was captured
on the river boat at the end of ch21 and "turned traitor"). Keep one rendering per
referent across the whole book. NOTE the twin-name slip and the identity-doubling:
the source occasionally prints 杨慕次 where the scene is plainly Muchu/A-Chu (none in
B08, but expect more), and prints the borrowed name "杨羽柏" (in quotes) for Yang
Yuhua — render by context and footnote the slip at first occurrence in a chapter
rather than silently reconciling; 阿次 = A-Ci is Muci's genuine familiar name.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/on-a-hair-trigger, and rewrite
HANDOFF.md with a paste-ready B10 kickoff (B10 = ch25 to ch27). Cite chapters,
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
  7 footnotes (#55 to #61), ~25 new glossary rows. See PROGRESS.md.
- Batch B08 = Chapters 19 to 21 (ch19 to ch21), ~19,405 chars, 649 paragraphs.
  Bilingual QC files, reading files, parity sources, 9 footnotes (#62 to #70) and
  16 new glossary rows all written; check_numbers 0 unresolved (10 noise.txt
  additions), check_structure parity OK (241/241, 231/231, 177/177), verbatim
  parity zero content diffs, blind double translation + round-trip back-translation
  on the lyrical/argumentative passages, paranoid audit ~4% with observed error
  rate 0%. See PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 22 of 36 units translated, 70 notes, qa green.

## What is NEXT

- Batch B09 = ch22 to ch24 (~20,823 chars). Then B10 = ch25 to ch27, and so on
  through B13 = ch34 to ch35 (see book.json "batches").

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another branch, but fold all work onto claude/on-a-hair-trigger and retire
  any stray branch. (B08 was handed a stray branch claude/hair-trigger-b08-*; all
  prior work — B01..B07 — actually sat on that stray, so it was fast-forwarded onto
  claude/on-a-hair-trigger and the B08 work committed there. Delete stray batch
  branches, local and remote, once folded.)
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). A fresh
  container has only source.epub + the committed out/*_bilingual.md, notes.json,
  glossary.json, book.json, data/noise.txt. Re-run ingest_epub.py to rebuild
  data/src; re-run split_bilingual.py on each committed bilingual (ch00..ch21) to
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
  split in the 梨花落 aria; ch16 through ch21 had none); keep the parity count, render
  each source line as its own paragraph and split the English at the matching point.
- check_numbers noise: data/noise.txt is the project non-quantity list; ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. The checker protects clock hours/minutes and "-odd" counts via digit
  lookbehinds; maps English month names to their number (November -> 11); WORD_NUM
  knows one..thirteen, teens, tens, and first..tenth ordinals. Prefer rendering a
  quantity so its digit survives over noising it (B08 rendered 万里 as "Ten thousand
  li"); noise only genuine non-quantity numerals (idioms, names, 零 in 凋零/飘零,
  bachelor-slang 五 in 王老五, etc.). TRAPS: the built-in 万分 rule fragments the
  fraction 五万分之一 / 十万分之一 (a stray 十/五) — noise the residue; the built-in 几十
  rule strips 几十 out of 几十万 and leaves a stray 万(=10000) before the next char —
  noise that residue (B08 noised "万的输赢"). B07 noise additions: 贤二, 下三烂, 万端,
  一了百了, 百试百灵, 三元, 千羡万羡, 十五、六, 一百八十度, 阿四. B08 noise additions:
  八、九十分, 百乐门, 四目, 百无聊赖, 几十万, 万的输赢, 四肢, 四周.
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
  Cao Zhi 七步诗 at Chapter 17; the September 18th Incident at Chapters 16 and 17;
  Yu Xuanji (鱼玄机) and the 月份牌 calendar poster at Chapter 19; Pushkin "To the Sea"
  and Dostoevsky "The Insulted and the Injured" at Chapter 20; Mencius (孟子, Gaozi)
  at Chapter 20; 千钧一发 (韩愈) and 箭在弦上 (陈琳) at Chapter 21.
- Prose written TO the commissioner (this HANDOFF, PROGRESS, chat) uses no em
  dashes (CLAUDE.md rule 6); the translation itself may use them.
- Plot state after B08:
  * A-Chu track: A-Chu forgave Han Zhengqi (a blank in the gun) and kept him in the
    society; took over the White Rose Ballroom and other legitimate businesses;
    pulled He Yashu off the dance floor and moved to place her; met his old friend
    the Comintern delegate Cong Feng (lodged with Ronghua at Plum Blossom Lane No.5,
    A-Chu looking at No.7); is grooming his nephew Rong Chu to play the Rong young
    master. A-Chu confronted his twin Muci at the English Tearoom, demanded one
    million as "hush money" for saving Lao Yu, told Muci "you have no kin left except
    me" and to guard against his own parents. A blue-orchid handkerchief hints Rong
    Chu has a secret woman.
  * Muci track: borrowed one million from his "father" Yang Yuhua (who gave it
    gladly, a father-son reconciliation over billiards); that same night found a
    hidden clandestine radio in his own garden, and his sleepwalking "mother" Xu
    Yuzhen (the impostor) — whose fingertips carry the telegraph-key calluses of a
    professional radio operator. Muci now suspects his mother is an enemy agent, and
    is all but certain the "Mr. Chu" who is shaking him down is his own twin. His
    superior Yang Yuhua told him the fire backstory (mother's affair with the driver
    Han, the twin brother "killed," the nurse "dead") — the impostor's version.
  * The Party is hit hard: Fang Zhitong (cover-name Xiang), Secretary of the Central
    Special Branch, was seized on a decoy river boat by Li Qinhong ("the Flower of
    Juntong") of the Detective Division's Second Section, and by that afternoon had
    "turned traitor" — putting the Central Office, the Special Committee's lodgings
    and the Secretariat (and Muci himself) into the chief Xiong Zida's pocket. The
    enlarged Central Special Committee meeting (with Cong Feng and delegates from
    Yunnan/Guangdong) is now in mortal danger. B09 opens here.
- Twin / identity handling: 阿初/杨慕初 = A-Chu, 阿次/杨慕次 = A-Ci (identical twins);
  footnote a 杨慕次-for-Muchu (or vice versa) slip at first occurrence per chapter,
  render by context. 杨羽桦 (Yang Yuhua) lives under the murdered 杨羽柏 (Yang Yubo)'s
  identity (source prints "杨羽柏" in quotes for the present-day father); "徐玉真" in
  quotes = the impostor mother. Deliberate source irony (e.g. the nurse 岳嬷嬷 said to
  have "died" in the fire yet alive and burn-scarred at A-Chu's house) is rendered
  faithfully, NOT reconciled.
- Anachronism flags recorded in glossary notes: fabi (法币, 1935) used loosely for
  the early-1930s present; the Park Hotel (国际大饭店, opened 1934) named a little
  before its time. The Paramount (百乐门) and Avenue Joffre (霞飞路) are attested
  Shanghai landmarks. The "Liyang Society"/"Eastern Institute" (立洋社/东洋学馆) are
  unattested Japanese-spy fronts of the novel (footnote #57).
