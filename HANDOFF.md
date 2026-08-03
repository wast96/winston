# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4), B02 (Chapters 5 to 7), B03 (Chapters 8 to 10), B04 (Chapters 11
to 13), B05 (Chapters 14 to 15), B06 (Chapter 16), B07 (Chapters 17 to 18), B08
(Chapters 19 to 21), B09 (Chapters 22 to 24) and B10 (Chapters 25 to 27) are DONE,
checks green, committed. Batch B11 is next.

## Message to paste into the next chat

```
Hair Trigger B11 — Chapters 28 to 30 (ch28, ch29, ch30).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B11 end to end: Chapter 28 (ch28, ~4,620
source chars), Chapter 29 (ch29, ~6,337 chars) and Chapter 30 (ch30, ~6,346 chars),
~17,303 chars total. This continues the novel from Batch B10 (the Prologue and
Chapters 1 to 27 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch27 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title").

Read each unit's source from data/src/ (ch28 = 31_part0029.txt, ch29 =
32_part0030.txt, ch30 = 33_part0031.txt). Translate to the register in CLAUDE.md:
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
ch27 had none): if a real mid-sentence split occurs, keep the parity count, render
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
  noise that residue (B08 noised "万的输赢"). The SAME orphaned-万 trap hit B10 on
  千百万劳苦大众: the built-in 千百 rule strips 千百 and leaves a stray 万 — B10 noised
  the residue "万劳苦". Clock quarters: the built-in list noises 一刻 (the 一 of
  "quarter"); B09 added 三刻 (the 三 of the 45-minute quarter). Names and idioms
  containing a numeral get noised, not dropped. B10 added seven such rows to
  data/noise.txt (零度, 万劳苦, 九泉, 二来, 一干二净, 百花, 五内).
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
chapter title itself does not take a note ref). ch28 = 间不容发生死际, ch29 =
欲披荒草访疑尘, ch30 = 同生共死亲兄弟: trace each against scholarship and say
corroborated / uncorroborated / contradicted, and footnote it. Note 间不容发 is a
documented idiom ("not a hair's breadth between", from 枚乘《上书谏吴王》: "系绝于天…
其出不出，间不容发"), so check it; many of this book's other titles are the author's
own seven-character lines in the old manner (ch17, ch19, ch20, ch22, ch23, ch24,
ch26, ch27 were all found to be author's pastiche, not verifiable single
quotations), so render a non-traceable title literally and footnote it as such.
Recurring literary/historical refs get their note at FIRST appearance only. Already
noted: 梨花落 aria at Chapter 12; 小松 杜荀鹤 at Chapter 5; the 瀑布联句 waterfall poem
at Chapter 15; 西厢记 at Chapter 16; 陆羽 六羡歌 and Cao Zhi 七步诗 at Chapter 17;
Yu Xuanji 鱼玄机 and the 月份牌 calendar poster at Chapter 19; Pushkin "To the Sea"
and Dostoevsky "The Insulted and the Injured" and Mencius 孟子 at Chapter 20;
千钧一发 韩愈 and 箭在弦上 陈琳 and Fang Zhitong's Xiang cover-name at Chapter 21; Gu
Shunzhang 顾顺章 and Wu Hao 伍豪 (= Zhou Enlai) at Chapter 22; 黛玉焚稿 红楼梦 and the
White-Terror slogan 宁可错杀一千 at Chapter 24; the 插秧诗 (布袋和尚 退步原来是向前),
移花接木, and 耳听为虚眼见为实 at Chapter 25; 岳阳楼记 (进亦不喜退亦不忧), the Bai Yun
title pun, and 踏破铁鞋无觅处 at Chapter 26; the peony / Wu Zetian legend
(洛阳牡丹甲天下) and 回头是岸/水到渠成 at Chapter 27.

Glossary rows into glossary.json for every NEW name, place, org and term, one
decided rendering per referent — CHECK the existing glossary first and reuse those
renderings. Recurring cast alive/active at the B10/B11 seam: the two twins — Yang
Muci (杨慕次, familiar 阿次 = A-Ci, the Party's man / codename Drifting Wind 飘风; a
recovering patient at the Chunhe Hospital, now carrying Xin Lili's hidden gun) and
Yang Muchu / A-Chu (杨慕初/阿初, the Golden Dragon chief and Yang Industrial Company
boss, a trained doctor, openly claiming Muci as his brother) — plus Cong Feng (丛锋,
the Comintern envoy, hidden in A-Chu's house, now breaking cover to reach Muci at
the hospital and walking into Li Qinhong's trap), Xia Yuechun (夏跃春, the surgeon,
racing to cut Cong Feng off), Han Zhengqi (韩正齐, deputy police-bureau chief,
secretly A-Chu's man), Liu A-Si (刘阿四, A-Chu's man), He Yashu (和雅淑, now A-Chu's
mistress at Plum Blossom Lane No. 7), Young Tang (汤少 = 汤少棋 Tang Shaoqi). Enemy
side: Li Qinhong (李沁红, "the Flower of Juntong", disguised as a nurse at bed 19),
Du Luning (杜旅宁, Muci's teacher/chief, watching the hospital), Yu Xiaojiang (俞晓江,
his aide), Xin Lili (辛丽丽/丽丽, the "hibernating" Juntong agent in love with Muci),
Gao Lei (高磊 = Captain Gao), Xiong Zida (熊自达, chief of the Detective Division).
Rong side: Rong Sheng (荣升), the First/Second/Third Madams (大/二/三太太), Jiang
Lishui (江丽水/丽水), the maid Xing'er (杏儿), Rong Gui (荣归), Rong Chu / Rong'er
(荣初/荣儿, the Rh-negative donor now courting Yang Sitong 杨思桐). CCP side: Zhong
Yundi (钟云迪, Red Spear Squad deputy leader), the new "时雨"/Timely Rain (a woman,
unnamed), Tian Xiuyun (田秀芸 = alias Bai Yun 白云, exposed as a 1927 defector),
"Snow Wolf" (雪狼). DEAD/removed at B10: the Rivet 铆钉 (= 阿春, killed by A-Chu),
Ronghua (荣华). Keep one rendering per referent across the whole book. NOTE the
twin / identity-doubling: render 阿初 vs 阿次 by context; ch25 deliberately marks a
body double with quotes ("杨慕次") in the phone-trap scene (render the quotes as they
stand — the source explains the 移花接木 ruse itself); the double-agent reveal (阿春 =
the Rivet; his wife 田秀芸 = Bai Yun) is rendered as it stands. If a source name slip
occurs, render by context and footnote at first occurrence in a chapter rather than
silently reconciling.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/on-a-hair-trigger, and rewrite
HANDOFF.md with a paste-ready B12 kickoff (B12 = ch31 to ch33). Cite chapters,
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
- Batch B02 = Chapters 5 to 7 (ch05 to ch07), ~19,345 chars. 10 footnotes
  (#14 to #23), 24 new glossary rows. See PROGRESS.md.
- Batch B03 = Chapters 8 to 10 (ch08 to ch10), ~15,194 chars. 9 footnotes
  (#24 to #32), 24 new glossary rows. See PROGRESS.md.
- Batch B04 = Chapters 11 to 13 (ch11 to ch13), ~18,985 chars. 10 footnotes
  (#33 to #42), 15 new glossary rows. See PROGRESS.md.
- Batch B05 = Chapters 14 to 15 (ch14 to ch15), ~20,027 chars. 7 footnotes
  (#43 to #49), 11 new glossary rows. See PROGRESS.md.
- Batch B06 = Chapter 16 (ch16), ~11,004 chars. 5 footnotes (#50 to #54).
- Batch B07 = Chapters 17 to 18 (ch17 to ch18), ~15,534 chars. 7 footnotes
  (#55 to #61), ~25 new glossary rows. See PROGRESS.md.
- Batch B08 = Chapters 19 to 21 (ch19 to ch21), ~19,405 chars. 9 footnotes
  (#62 to #70), 16 new glossary rows; 10 noise.txt additions. See PROGRESS.md.
- Batch B09 = Chapters 22 to 24 (ch22 to ch24), ~20,823 chars. 9 footnotes
  (#71 to #79), 20 new glossary rows; 12 noise.txt additions. See PROGRESS.md.
- Batch B10 = Chapters 25 to 27 (ch25 to ch27), ~20,965 chars, 734 paragraphs.
  Bilingual QC files, reading files, parity sources, 9 footnotes (#80 to #88) and
  17 new glossary rows all written; check_numbers 0 unresolved (7 noise.txt
  additions), check_structure parity OK (256/256, 253/253, 225/225), verbatim
  parity zero content diffs, blind double translation + round-trip back-translation
  on the lyrical/argumentative passages, paranoid audit ~3.4% with observed error
  rate 0%. See PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 28 of 36 units translated, 88 notes, qa green.

## What is NEXT

- Batch B11 = ch28 to ch30 (~17,303 chars). Then B12 = ch31 to ch33, B13 = ch34 to
  ch35 (see book.json "batches"). B13 is the LAST batch: do any back matter and a
  whole-book QA pass and write a completion report instead of a handoff.

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another per-batch branch, but fold all work onto claude/on-a-hair-trigger
  and retire the stray branch. (B10 was handed a stray branch
  claude/hair-trigger-b10-*; origin/claude/on-a-hair-trigger already carried
  B01..B09, so the local branch fast-forwarded onto it and the B10 commit lands on
  claude/on-a-hair-trigger; the stray branch is deleted, local and remote. Do the
  same each batch: commit, fast-forward claude/on-a-hair-trigger, push it, delete
  the stray.)
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). out/*_en.txt
  and out/*.epub are also gitignored. A fresh container has only source.epub + the
  committed out/*_bilingual.md (force-added past the ignore), out/*_reading.md,
  notes.json, glossary.json, book.json, data/noise.txt, PROGRESS.md, HANDOFF.md.
  Re-run ingest_epub.py to rebuild data/src; re-run split_bilingual.py on each
  committed bilingual (ch00..ch27) to rebuild data/zh and out/*_reading.md BEFORE
  building. When you commit new bilinguals, force-add them: git add -f
  out/ch28_bilingual.md (etc.); the reading files add normally.
- Authoring flow (established B02): write out/<id>_en.txt (one English paragraph
  per source paragraph), then scripts/make_bilingual.py to get the bilingual with
  verbatim `>` source lines, then split_bilingual.py. Do NOT hand-type the source
  into the bilingual.
- Source structure: one spine file per chapter; single H2 couplet title; no h3/h4;
  scene breaks are separate source paragraphs, rendered as paragraph breaks. The
  source carries NO notes of its own; every note is the translator's. Watch for
  mid-sentence paragraph splits (ch08, ch12, ch14 each had one; ch15 had a mid-word
  split in the 梨花落 aria; ch16 through ch27 had none); keep the parity count, render
  each source line as its own paragraph and split the English at the matching point.
- check_numbers noise: data/noise.txt is the project non-quantity list; ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. The checker protects clock hours/minutes and "-odd" counts via digit
  lookbehinds; maps English month names to their number (November -> 11); WORD_NUM
  knows one..thirteen, teens, tens, and first..tenth ordinals plus seventeenth,
  sixteenth. Prefer rendering a quantity so its digit survives over noising it;
  noise only genuine non-quantity numerals (idioms, names, 零 in 凋零/飘零/零星/零度,
  the 千 of a unit like 千帕/kilopascal, etc.). TRAPS carried forward: the 万分 rule
  fragments the fraction 五万分之一 / 十万分之一 (noise the residue); the 几十 rule strips
  几十 out of 几十万 and leaves a stray 万 (noise it); the 千百 rule strips 千百 out of
  千百万 and leaves a stray 万 (B10 noised the residue "万劳苦"); a thousands comma
  ("2,594") is split into 2 and 594 (render digit strings without the comma); the
  English parser does NOT read "a hundred and eight" as 108 (render Arabic digits
  where the source does). B07 noise: 贤二, 下三烂, 万端, 一了百了, 百试百灵, 三元,
  千羡万羡, 十五、六, 一百八十度, 阿四. B08 noise: 八、九十分, 百乐门, 四目, 百无聊赖,
  几十万, 万的输赢, 四肢, 四周. B09 noise: 三刻, 两句, 万不得已, 七窍, 零星, 急三火四,
  第二个人, 三长两短, 万事, 两个人, 万能, 千帕. B10 noise: 零度, 万劳苦, 九泉, 二来,
  一干二净, 百花, 五内.
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
  See the kickoff message's footnote list for the full already-noted roster
  (now including ch25 插秧诗/移花接木/耳听为虚, ch26 岳阳楼记/Bai Yun pun/踏破铁鞋,
  ch27 peony-Wu Zetian legend/回头是岸-水到渠成).
- Prose written TO the commissioner (this HANDOFF, PROGRESS, chat) uses no em
  dashes (CLAUDE.md rule 6); the translation itself may use them.
- Plot state after B10 (A-Chu clears the trap around Muci; the mole falls):
  * The phone voice-trap (Chapter 25): A-Chu and Xia Yuechun run a "grafting"
    (移花接木) ruse: a body double first plays the injured "杨慕次" in the ICU and
    answers the first (voice-matching) call, so the enemy fix Muci's identity by
    sight; the real Muci then answers the later calls, and the voice-matcher (the
    Rivet) can no longer be sure. A-Chu arrives openly with He Yashu to confirm
    Muci visually, and Li Qinhong's suspicion collapses. A-Chu then formally makes
    He Yashu his mistress at Plum Blossom Lane No. 7 (courtship consummated; he
    quotes the 插秧诗). The nurses are sent to the Ren'ai Hospital in England for a
    year.
  * A-Chu hunts and kills the Rivet (铆钉) (Chapter 26): he clears "Snow Wolf" (雪狼,
    a Central Secretariat secretary jailed as the Hengji Li murder suspect), then
    catches 阿春 at the Police Bureau. 阿春, ostensibly a Special Branch peripheral
    and 田秀芸's husband, is exposed as the Juntong Rivet: he killed the Hengji Li
    amah, switched her evacuation warning to a safe-signal, and did the phone
    voice-matching. A-Chu has him strangled; Han Zhengqi disposes of the body by
    walking "Snow Wolf" out disguised as "A-Chun," who then "vanishes." Three days
    later Bai Yun's body is found in the Huangpu.
  * CCP side (Chapter 26): the Red Spear Squad (钟云迪 deputy leader) holds Ronghua's
    memorial; a new "时雨"/Timely Rain (a woman) takes over and issues Wu Hao's three
    orders (root out the mole, protect the envoy, punish traitors). She exposes
    田秀芸/白云 as a 1927 defector via an old recantation, and directs using A-Chu's
    hospital and Plum Blossom Lane as cover/bait. Rong Sheng buries Ronghua in
    secret and keeps the Third Madam in the dark with a "gone to Yan'an" lie; means
    to rebuild the burnt bookstore under Rong Gui.
  * Enemy side (Chapter 27): Du Luning (杜旅宁, Muci's teacher/chief) watches the
    hospital, disdains Li Qinhong (old grudge: she killed a student of his out of
    jealousy five years back); Yu Xiaojiang (俞晓江) proposes lifting the watch on
    A-Ci and sweeping the busy Concession for the conference venue (three
    conditions: in the Concession, in the busiest quarter with many exits, able to
    house 100-plus). Xin Lili (辛丽丽, a "hibernating" Juntong agent still in love
    with Muci) comes to visit; Yu Xiaojiang slaps her, smashes Muci's hand with a
    pistol butt to break up the contact, but Muci ends with Lili's small gilt gun
    hidden under his gown. Rong Chu visits with Yang Sitong; he and Muci fence over
    his identity (回头是岸 / 水到渠成).
  * B10 CLIFFHANGER: Cong Feng (丛锋), penned in A-Chu's house nearly a week, breaks
    cover to reach his one live contact (Muci) at the Chunhe Hospital; his rickshaw
    man is a Detective Division agent, so his appearance at two sensitive spots is
    now flagged. Li Qinhong, disguised as a nurse, waits by bed 19 with her hand in
    her pocket; Cong Feng's hand is on the sickroom door-handle. Both A-Chu (to Plum
    Blossom Lane) and Xia Yuechun (at the hospital) race to cut him off. B11 opens
    here.
- Twin / identity handling: 阿初/杨慕初 = A-Chu, 阿次/杨慕次 = A-Ci (identical twins);
  render by context; footnote a genuine name slip at first occurrence per chapter
  rather than reconciling. 杨羽桦 (Yang Yuhua) lives under the murdered 杨羽柏 (Yang
  Yubo)'s identity (source prints "杨羽柏" in quotes for the present-day father);
  "徐玉真" in quotes = the impostor mother. Fang Zhitong appears as both 方致同 and his
  full cover name 向成发 (Xiang Chengfa); the Xiang cover-identity is footnoted at
  Chapter 21. Deliberate source irony and name slips (the bookstore 荣华书店 / 华美书店,
  one shop) are rendered faithfully and footnoted, NOT reconciled.
- Anachronism flags recorded in glossary notes: fabi (法币, 1935) used loosely for
  the early-1930s present; the Park Hotel (国际大饭店, opened 1934) named a little
  before its time. Gordon Road (戈登路), Bubbling Well Road (静安寺路), Avenue Joffre
  (霞飞路), the Racecourse (跑马厅), Fourth Avenue (四马路), the Lyceum/Lanxin Theatre
  (兰心大戏院) and the Paramount (百乐门) are attested Shanghai landmarks. The "Liyang
  Society"/"Eastern Institute" (立洋社/东洋学馆) are unattested Japanese-spy fronts of
  the novel (footnote #57).
