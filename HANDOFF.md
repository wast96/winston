# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4), B02 (Chapters 5 to 7), B03 (Chapters 8 to 10), B04 (Chapters 11
to 13), B05 (Chapters 14 to 15), B06 (Chapter 16), B07 (Chapters 17 to 18), B08
(Chapters 19 to 21) and B09 (Chapters 22 to 24) are DONE, checks green, committed.
Batch B10 is next.

## Message to paste into the next chat

```
Hair Trigger B10 — Chapters 25 to 27 (ch25, ch26, ch27).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B10 end to end: Chapter 25 (ch25, ~8,943
source chars), Chapter 26 (ch26, ~9,044 chars) and Chapter 27 (ch27, ~7,345 chars),
~20,965 chars total. This continues the novel from Batch B09 (the Prologue and
Chapters 1 to 24 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch24 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title").

Read each unit's source from data/src/ (ch25 = 28_part0026.txt, ch26 =
29_part0027.txt, ch27 = 30_part0028.txt). Translate to the register in CLAUDE.md:
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
ch24 had none): if a real mid-sentence split occurs, keep the parity count, render
each source line as its own paragraph, and split the English at the matching point.

Run the checks and record them in PROGRESS.md, per unit:
- scripts/check_numbers.py --noise data/noise.txt out/<id>_bilingual.md  (must be
  0 unresolved). The non-quantity noise list lives in data/noise.txt; ADD to it
  (or to WORD_NUM in check_numbers.py for spelled-out ordinals your prose uses)
  whenever a NON-quantity numeral is flagged, and record what you added. Do NOT
  drop a real date/year/time; render clock times so their digits survive (e.g.
  "three thirty", "two twenty-five", "seven fifty-two", not "half past three" or
  "a quarter to eight"). The checker protects clock hours (十一点/十二点) and clock
  minutes and "-odd" counts via digit lookbehinds; maps English month names to
  their number (so "November" credits 11月). A big number written with a thousands
  comma ("2,594") is split by the checker into 2 and 594; render such digit strings
  without the comma ("2594"), or spell them so the parser reconstructs them. The
  English number parser does NOT combine "a hundred and eight" into 108; where the
  source prints Arabic digits (e.g. 108套刑具, 2594米), render the digits (B09 wrote
  "108", "2594 metres"). Watch the fraction trap: a built-in 万分 rule fragments
  五万分之一 / 十X万分之一 — noise the residue. Watch the built-in 几十 rule too: it
  strips 几十 out of 几十万 and leaves a stray 万(=10000) before the following char —
  noise that residue (B08 noised "万的输赢"). Clock quarters: the built-in list
  noises 一刻 (the 一 of "quarter"); B09 added 三刻 (the 三 of the 45-minute quarter),
  and renders the minutes as "forty-five". Names and idioms containing a numeral
  (e.g. 黄三元, 刘阿四, 土肥原贤二, 一了百了, 一百八十度, 八、九十分, 百乐门, 四目, 百无聊赖,
  四肢, 四周, 七窍, 三长两短, 万能, 千帕) get noised, not dropped — B09 added twelve such
  rows to data/noise.txt (三刻, 两句, 万不得已, 七窍, 零星, 急三火四, 第二个人, 三长两短,
  万事, 两个人, 万能, 千帕).
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
chapter title itself does not take a note ref). ch25 = 退步原来是向前, ch26 =
白云可杀不可留, ch27 = 踏破冰火九重天: trace each against scholarship and say
corroborated / uncorroborated / contradicted, and footnote it. If a title or line
is not a traceable quotation, render it literally and footnote it as such (many of
this book's titles are the author's own seven-character lines in the old manner:
ch17, ch19, ch20, ch22, ch23, ch24 were all found to be author's pastiche, not
verifiable single quotations — though ch25's 退步原来是向前 is a known line from the
Chan poem attributed to 契此/布袋和尚, "手把青秧插满田，低头便见水中天……退步原来是向前",
so check it). Recurring literary/historical refs get their note at FIRST appearance
only (already noted: 梨花落 aria at Chapter 12; 小松 杜荀鹤 at Chapter 5; the 瀑布联句
waterfall poem at Chapter 15; 西厢记 at Chapter 16; 陆羽 六羡歌 and Cao Zhi 七步诗 at
Chapter 17; Yu Xuanji 鱼玄机 at Chapter 19; the 月份牌 calendar poster at Chapter 19;
Pushkin "To the Sea" and Dostoevsky "The Insulted and the Injured" at Chapter 20;
Mencius 孟子 "水无有不下" at Chapter 20; 千钧一发 韩愈 and 箭在弦上 陈琳 at Chapter 21; the
Xiang cover-name of Fang Zhitong at Chapter 21; Gu Shunzhang 顾顺章 and Wu Hao 伍豪
(= Zhou Enlai) at Chapter 22; 黛玉焚稿 红楼梦 and the White-Terror slogan 宁可错杀一千 at
Chapter 24).

Glossary rows into glossary.json for every NEW name, place, org and term, one
decided rendering per referent — CHECK the existing glossary first and reuse those
renderings. Recurring cast: the two twins — Yang Muci (杨慕次, familiar 阿次 = A-Ci,
the Party's man / codename Drifting Wind 飘风, a major and adjutant in the Detective
Division; now gravely injured, in the Chunhe Hospital, his whole Party line dead)
and Yang Muchu / A-Chu (杨慕初/阿初, the Golden Dragon chief, a trained doctor, who
operated on his twin and now openly claims him as a brother) — plus Ronghua (荣华,
CCP Special Branch, DEAD: she rammed the raid convoy at Chapter 22 to save the
network), Cong Feng (丛锋, the Comintern delegate, escaped the crash and was seized
by A-Chu's men, who burned the Huamei Bookstore), Rong Chu / Rong'er (荣初/荣儿, the
Rh-negative blood donor, groomed to play the Rong young master; Yang Sitong is now
sweet on him), Rong Sheng (荣升, Ronghua's grieving half-brother), Amah A-Yue
(岳嬷嬷/阿岳), He Yashu (和雅淑, now installed by A-Chu in a Plum Blossom Lane house
via a "job"), Xia Yuechun (夏跃春, the surgeon), Han Yu (韩禹), Du Luning (杜旅宁),
Yu Xiaojiang (俞晓江), Li Qinhong (李沁红, "the Flower of Juntong"), Xiong Zida (熊自达,
chief of the Detective Division), Gao Lei (高磊 = Captain Gao), Adjutant Liu (刘副官
= Liu Yun 刘云), Han Zhengqi (韩正齐, deputy chief of the police bureau, secretly
A-Chu's man). Keep one rendering per referent across the whole book. NOTE the
twin-name slip and identity-doubling: the source can print 杨慕次 where the scene is
plainly Muchu/A-Chu (none in B09) and prints the borrowed name "杨羽柏" (in quotes)
for Yang Yuhua; render by context and footnote the slip at first occurrence in a
chapter rather than silently reconciling; 阿次 = A-Ci is Muci's genuine familiar
name. B09 also saw a source name slip on the bookstore (荣华书店 vs 华美书店, one shop):
render as it stands and footnote, do NOT reconcile.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/on-a-hair-trigger, and rewrite
HANDOFF.md with a paste-ready B11 kickoff (B11 = ch28 to ch30). Cite chapters,
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
  9 footnotes (#62 to #70), 16 new glossary rows; 10 noise.txt additions. See
  PROGRESS.md.
- Batch B09 = Chapters 22 to 24 (ch22 to ch24), ~20,823 chars, 771 paragraphs.
  Bilingual QC files, reading files, parity sources, 9 footnotes (#71 to #79) and
  20 new glossary rows all written; check_numbers 0 unresolved (12 noise.txt
  additions), check_structure parity OK (330/330, 223/223, 218/218), verbatim
  parity zero content diffs, blind double translation + round-trip back-translation
  on the lyrical/argumentative passages, paranoid audit ~4% with observed error
  rate 0%. See PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 25 of 36 units translated, 79 notes, qa green.

## What is NEXT

- Batch B10 = ch25 to ch27 (~20,965 chars). Then B11 = ch28 to ch30, B12 = ch31 to
  ch33, B13 = ch34 to ch35 (see book.json "batches"). B13 is the LAST batch: do any
  back matter and a whole-book QA pass and write a completion report instead of a
  handoff.

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another per-batch branch, but fold all work onto claude/on-a-hair-trigger
  and retire the stray branch. (B09 was handed a stray branch
  claude/hair-trigger-b09-*; origin/claude/on-a-hair-trigger already carried
  B01..B08, so the B09 commit fast-forwarded straight onto it and the stray branch
  was deleted, local and remote. Do the same each batch: commit, fast-forward
  claude/on-a-hair-trigger, push it, delete the stray.)
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). out/*_en.txt
  and out/*.epub are also gitignored. A fresh container has only source.epub + the
  committed out/*_bilingual.md (force-added past the ignore), out/*_reading.md,
  notes.json, glossary.json, book.json, data/noise.txt, PROGRESS.md, HANDOFF.md.
  Re-run ingest_epub.py to rebuild data/src; re-run split_bilingual.py on each
  committed bilingual (ch00..ch24) to rebuild data/zh and out/*_reading.md BEFORE
  building. When you commit new bilinguals, force-add them: git add -f
  out/ch25_bilingual.md (etc.); the reading files add normally.
- Authoring flow (established B02): write out/<id>_en.txt (one English paragraph
  per source paragraph), then scripts/make_bilingual.py to get the bilingual with
  verbatim `>` source lines, then split_bilingual.py. Do NOT hand-type the source
  into the bilingual.
- Source structure: one spine file per chapter; single H2 couplet title; no h3/h4;
  scene breaks are separate source paragraphs, rendered as paragraph breaks. The
  source carries NO notes of its own; every note is the translator's. Watch for
  mid-sentence paragraph splits (ch08, ch12, ch14 each had one; ch15 had a mid-word
  split in the 梨花落 aria; ch16 through ch24 had none); keep the parity count, render
  each source line as its own paragraph and split the English at the matching point.
- check_numbers noise: data/noise.txt is the project non-quantity list; ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. The checker protects clock hours/minutes and "-odd" counts via digit
  lookbehinds; maps English month names to their number (November -> 11); WORD_NUM
  knows one..thirteen, teens, tens, and first..tenth ordinals. Prefer rendering a
  quantity so its digit survives over noising it; noise only genuine non-quantity
  numerals (idioms, names, 零 in 凋零/飘零/零星, the 千 of a unit like 千帕/kilopascal,
  etc.). TRAPS carried forward: the 万分 rule fragments the fraction 五万分之一 /
  十万分之一 (noise the residue); the 几十 rule strips 几十 out of 几十万 and leaves a
  stray 万 (noise it); a thousands comma ("2,594") is split into 2 and 594 (render
  digit strings without the comma); the English parser does NOT read "a hundred and
  eight" as 108 (render Arabic digits where the source does). B07 noise: 贤二, 下三烂,
  万端, 一了百了, 百试百灵, 三元, 千羡万羡, 十五、六, 一百八十度, 阿四. B08 noise: 八、九十分,
  百乐门, 四目, 百无聊赖, 几十万, 万的输赢, 四肢, 四周. B09 noise: 三刻, 两句, 万不得已, 七窍,
  零星, 急三火四, 第二个人, 三长两短, 万事, 两个人, 万能, 千帕.
- Reign-era dates appear beside their Western years; keep both, and let
  check_numbers see the Western year. Japanese Shōwa era also appears (Shōwa 4 =
  1929); render both the era number and the Western year.
- Deliverable filename has a space: quote it, "out/On a Hair Trigger.epub".
- Write JSON via a file (not shell heredocs) so Chinese glyphs are not mangled;
  re-read to verify (and scan `en` fields for stray hanzi). Watch apostrophes in a
  Python heredoc: an English apostrophe inside a single-quoted string breaks it
  (B09 hit this on "Jing'an"); use double-quoted strings or a .py file. XHTML note
  bodies use numeric character references only.
- Recurring names AND recurring literary/historical allusions get their note at
  FIRST appearance in the book; reuse glossary renderings, do not re-romanize.
  Already footnoted: 梨花落 aria (情探 / 王魁负桂英) at Chapter 12; 小松 (杜荀鹤) at
  Chapter 5; the 瀑布联句 waterfall poem at Chapter 15; 西厢记 at Chapter 16; 陆羽 六羡歌
  and Cao Zhi 七步诗 at Chapter 17; the September 18th Incident at Chapters 16 and 17;
  Yu Xuanji (鱼玄机) and the 月份牌 calendar poster at Chapter 19; Pushkin "To the Sea"
  and Dostoevsky "The Insulted and the Injured" at Chapter 20; Mencius (孟子, Gaozi)
  at Chapter 20; 千钧一发 (韩愈) and 箭在弦上 (陈琳) at Chapter 21; Fang Zhitong's Xiang
  cover-name at Chapter 21; Gu Shunzhang (顾顺章) and Wu Hao (伍豪 = Zhou Enlai) at
  Chapter 22; 黛玉焚稿 (红楼梦) and the White-Terror slogan 宁可错杀一千 at Chapter 24.
- Prose written TO the commissioner (this HANDOFF, PROGRESS, chat) uses no em
  dashes (CLAUDE.md rule 6); the translation itself may use them.
- Plot state after B09 (the book's turning point):
  * The Party's Shanghai catastrophe plays out: Fang Zhitong (cover-name Xiang /
    向成发) is poisoned in his Detective Division cell by the young orderly Little Wu
    (小吴), a Party man, who is then shot by Li Qinhong. Ronghua (荣华), unable to warn
    every comrade in time, rams her own car into the disguised raid convoy at the
    mouth of Hengji Li (Gordon Road No. 1141), dying to throw the raid into chaos
    and save the network; the dragnet collapses. Muci, in the passenger seat of the
    truck she hit, is gravely injured (ruptured femoral artery, fractured breastbone
    and knee). Cong Feng escapes the crash; A-Chu's men seize him and burn Ronghua's
    Huamei Bookstore to erase every trace of "the second young master."
  * A-Chu, a trained doctor, operates on his own twin with Xia Yuechun and Han Yu;
    Rong Chu (荣初, also Rh-negative type A) gives blood. Seeing his blood mingle with
    A-Ci's, A-Chu for the first time feels real tenderness for his brother and, from
    this night, openly claims him. He tells Muci he means to establish their
    brotherhood formally, and hints he holds the secret of Muci's family; Muci,
    cool and wary, rebuffs the overture and refuses to be leveraged.
  * A-Ci is now a masterless agent: his uplink (Ronghua) and downlink both dead, his
    top leader (Fang Zhitong) a dead traitor. "Drifting Wind" survives only because
    he lived. He sends A-Chu a coded farewell for "your Soviet friend" (Cong Feng):
    "the wind and the rain are both gone now" (Drifting Wind and Timely Rain both
    lost), "beware the thief within the house" (there is a mole inside the Special
    Branch too, who phoned the Hengji Li address to the enemy).
  * Li Qinhong, certain there is a "mole"/"Rivet" (铆钉, an informant she planted
    inside the Party) inside the Detective Division, sets a telephone voice-trap:
    her Rivet, who heard the mole's voice on the phone, will pick it out by ear, and
    every man (Muci included) is to be screened. Xiong Zida orders Hengji Li 1141
    and Plum Blossom Lane No. 5 watched. As B09 ends the enemy is about to send an
    army surgeon to move the recovering Muci (to the army hospital, or to prison)
    and has secretly installed the trap telephone next to his ward; A-Chu resolves
    on a risky plan to save him. B10 opens here.
  * A-Chu's civil life continues in parallel: he calls on He Yashu (和雅淑), whom he
    has quietly set up in a Plum Blossom Lane house through a fake securities job,
    keeping up a slow courtship that he half-admits has shifted from feeling to
    convenience; the meeting was staged on purpose. Han Zhengqi (韩正齐), deputy chief
    of the police bureau and secretly A-Chu's man, stalls the crash investigation
    for A-Chu.
- Twin / identity handling: 阿初/杨慕初 = A-Chu, 阿次/杨慕次 = A-Ci (identical twins);
  footnote a 杨慕次-for-Muchu (or vice versa) slip at first occurrence per chapter,
  render by context. 杨羽桦 (Yang Yuhua) lives under the murdered 杨羽柏 (Yang Yubo)'s
  identity (source prints "杨羽柏" in quotes for the present-day father); "徐玉真" in
  quotes = the impostor mother. Fang Zhitong appears as both 方致同 and his full cover
  name 向成发 (Xiang Chengfa); the Xiang cover-identity is footnoted at Chapter 21.
  Deliberate source irony (e.g. the nurse said "died" in the fire yet alive and
  burn-scarred) is rendered faithfully, NOT reconciled; likewise the bookstore
  name slip (荣华书店 / 华美书店, one shop) is rendered as it stands and footnoted.
- Anachronism flags recorded in glossary notes: fabi (法币, 1935) used loosely for
  the early-1930s present; the Park Hotel (国际大饭店, opened 1934) named a little
  before its time. Gordon Road (戈登路), Bubbling Well Road (静安寺路), the Majestic
  Theatre (美琪大戏院), the Paramount (百乐门) and Avenue Joffre (霞飞路) are attested
  Shanghai landmarks. The "Liyang Society"/"Eastern Institute" (立洋社/东洋学馆) are
  unattested Japanese-spy fronts of the novel (footnote #57).
