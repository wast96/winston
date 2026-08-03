# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4), B02 (Chapters 5 to 7), B03 (Chapters 8 to 10), B04 (Chapters 11
to 13), B05 (Chapters 14 to 15), B06 (Chapter 16), B07 (Chapters 17 to 18), B08
(Chapters 19 to 21), B09 (Chapters 22 to 24), B10 (Chapters 25 to 27) and B11
(Chapters 28 to 30) are DONE, checks green, committed. Batch B12 is next.

## Message to paste into the next chat

```
Hair Trigger B12 — Chapters 31 to 33 (ch31, ch32, ch33).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B12 end to end: Chapter 31 (ch31, ~6,085
source chars), Chapter 32 (ch32, ~5,612 chars) and Chapter 33 (ch33, ~6,274 chars),
~17,971 chars total. This continues the novel from Batch B11 (the Prologue and
Chapters 1 to 30 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch30 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title").

Read each unit's source from data/src/ (ch31 = 34_part0032.txt, ch32 =
35_part0033.txt, ch33 = 36_part0034.txt). Translate to the register in CLAUDE.md:
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
ch30 had none): if a real mid-sentence split occurs, keep the parity count, render
each source line as its own paragraph, and split the English at the matching point.

Run the checks and record them in PROGRESS.md, per unit:
- scripts/check_numbers.py --noise data/noise.txt out/<id>_bilingual.md  (must be
  0 unresolved). The non-quantity noise list lives in data/noise.txt; ADD to it
  (or to WORD_NUM in check_numbers.py for spelled-out ordinals your prose uses)
  whenever a NON-quantity numeral is flagged, and record what you added. Do NOT
  drop a real date/year/time; render clock times so their digits survive (e.g.
  "three thirty", "two twenty-five", "three in the morning", not "half past three"
  or "a quarter to eight"). The checker protects clock hours (十一点/十二点) and clock
  minutes and "-odd" counts via digit lookbehinds; maps English month names to
  their number (so "September" credits 9月/九). KNOWN PARSER TRAPS carried forward
  (noise the residue when they fire): the 万分 rule fragments 五万分之一 / 十X万分之一;
  the 几十 rule strips 几十 out of 几十万 and orphans a stray 万(=10000); the 千百 rule
  strips 千百 out of 千百万 and orphans a stray 万 (B10 noised "万劳苦"); a thousands
  comma ("2,594") is split into 2 and 594 (render digit strings without the comma);
  the English parser does NOT read "a hundred and eight" as 108 (render Arabic digits
  where the source does). The checker has NO 亿(=10^8) branch, so 一万亿 misparses to
  10000 (B11 noised 一万亿, rendered "a trillion"). Names/idioms carrying a numeral get
  NOISED, not dropped. B11 added five noise rows: 一万亿, 百姓 (in 老百姓), 零点 (clock
  "zero hour"/midnight, 零=0), 万籁 (in 万籁俱静), 一泻千里 (idiom). B10 added seven
  (零度, 万劳苦, 九泉, 二来, 一干二净, 百花, 五内); B09 twelve, B08 ten (full lists in
  PROGRESS.md and inline in data/noise.txt comments). B11 also fixed 四个字 by rendering
  "four words" (not by noising) so the count 4 survives faithfully — prefer that when a
  numeral is a real, translatable count.
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
grep -cF before building; XHTML bodies use NUMERIC character references only, e.g.
&#8212; &#8216; &#8217; &#8211; &#160; &#8230;, never named entities; hanzi may be
written literally). For each chapter the title couplet is the first thing to
footnote, anchored to a thematically apt verbatim phrase in that chapter's prose (the
H2 chapter title itself does not take a note ref). ch31 = 游鱼见食不见钩, ch32 =
醇酒美人鸳鸯剑, ch33 = 假做真时真亦假: trace each against scholarship and say
corroborated / uncorroborated / contradicted, and footnote it. NOTE ch33's title
假做真时真亦假 is the 红楼梦 太虚幻境 couplet (假作真时真亦假, 无为有处有还无) that was
ALREADY footnoted at Chapter 30 (note #97) — recurring refs get their note at FIRST
appearance only, so at ch33 render the title literally and, if you note it at all,
just cross-reference the ch30 note rather than repeat it (ch33 uses the variant 做 for
作). 鸳鸯剑 (the mandarin-duck / lovers' twin swords, ch32) is a known motif (it appears
in 红楼梦 as 尤三姐's sword and more broadly in wuxia) — trace and footnote it. Many of
this book's titles are the author's own seven-character lines in the old manner (ch17,
ch19, ch20, ch22, ch23, ch24, ch26, ch27, ch29, ch30 were all found to be pastiche,
not verifiable single quotations), so render a non-traceable title literally and
footnote it as such. Recurring literary/historical refs get their note at FIRST
appearance only. Already noted through B11: 梨花落 aria (ch12); 小松 杜荀鹤 (ch5);
瀑布联句 (ch15); 西厢记 (ch16); 陆羽 六羡歌 and Cao Zhi 七步诗 (ch17); Yu Xuanji 鱼玄机
and the 月份牌 poster (ch19); Pushkin "To the Sea", Dostoevsky, Mencius 孟子 (ch20);
千钧一发 韩愈 and 箭在弦上 陈琳 and Fang Zhitong's Xiang cover-name (ch21); Gu Shunzhang
顾顺章 and Wu Hao 伍豪 = Zhou Enlai (ch22); 黛玉焚稿 红楼梦 and 宁可错杀一千 (ch24);
插秧诗 (布袋和尚), 移花接木, 耳听为虚眼见为实 (ch25); 岳阳楼记, the Bai Yun title pun,
踏破铁鞋无觅处 (ch26); the peony/Wu Zetian legend and 回头是岸/水到渠成 (ch27); 间不容发
枚乘 and the Mukden Incident 九一八 and the anachronistic 《中国哲学简史》/Macmillan
(ch28); the China League for Civil Rights 中国民权保障同盟 and Wang Jingwei's 曲线救亡
(ch29); the 红楼梦 假作真 couplet (太虚幻境) and the 名古屋带 Nagoya obi (ch30).

Glossary rows into glossary.json for every NEW name, place, org and term, one decided
rendering per referent — CHECK the existing glossary first and reuse those renderings.
Recurring cast alive/active at the B11/B12 seam: the twins Yang Muci (杨慕次, 阿次 =
A-Ci, the Party's man / codename Drifting Wind 飘风) and Yang Muchu / A-Chu (杨慕初/阿初),
now openly allied and hunting the truth of their birth mother's murder; Xia Yuechun
(夏跃春, the surgeon, Muci's original contact), Han Zhengqi (韩正齐, deputy police-bureau
chief, A-Chu's man), Cong Feng (丛锋, the Comintern envoy, now sailed for Moscow), He
Yashu (和雅淑, A-Chu's mistress at Plum Blossom Lane No. 7), Rong Chu / Rong'er (荣初/荣儿,
courting Yang Sitong 杨思桐), Amah A-Yue (岳嬷嬷, A-Chu's household). CCP: Yu Xiaojiang
(俞晓江, revealed as the new "时雨"/Timely Rain, Muci's superior), Zhong Yundi (钟云迪,
Red Spear Squad deputy leader), Snow Wolf (雪狼, now the conference secretary-general).
Enemy: Du Luning (杜旅宁, Muci's teacher/chief, drifting pro-Japanese), Xiong Zida (熊自达,
just ousted as Detective-Division chief). The Japanese spy: Koyama Eiko (小山缨子,
provisional; living as the false 徐玉真/"Xu Yuzhen", the Imperial Flower 帝国之花), who
married Yang Yuhua (杨羽桦, who lives under the murdered 杨羽柏/Yang Yubo's identity) and
murdered the twins' birth mother at the Ciyun Temple 慈云寺. DEAD/removed: Li Qinhong
(李沁红, shot by Yu Xiaojiang in ch28), the Rivet 铆钉 (= 阿春), Ronghua (荣华, to be
named a martyr), Bai Yun (白云 = Tian Xiuyun 田秀芸). Keep one rendering per referent
across the whole book. Twin / identity handling: render 阿初 vs 阿次 by context (A-Chu /
A-Ci; Muci for the narration of 阿次); render the impostor reveal and any source name
slip as it stands, footnoting a genuine slip at first occurrence in a chapter rather
than silently reconciling.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/on-a-hair-trigger, and rewrite
HANDOFF.md with a paste-ready B13 kickoff (B13 = ch34 to ch35; B13 is the LAST batch,
so on B13 do any back matter and a whole-book QA pass and write a completion report
instead of another handoff). Cite chapters, never page numbers. Never invent bridging
text or silently drop material; footnote genuine ambiguity and leave it visible. If a
source carries a pirate-site watermark line (as ch06 and ch28 did), keep it verbatim in
the bilingual `>` line but leave it out of the reading text and footnote it. Do not
pause for approval mid-batch. When done, deliver out/On a Hair Trigger.epub to me as an
attached file in the chat.
```

## What is DONE (do not redo)

- Step 0: ingested source.epub, authored book.json (final), survey approved,
  skeleton EPUB built, QA green. Kindle/Apple Books metadata + cover wired in.
- Batch B01 = Prologue (ch00) + Chapters 1 to 4 (ch01 to ch04), ~20,041 chars.
  13 footnotes (#1 to #13). See PROGRESS.md.
- Batch B02 = Chapters 5 to 7 (ch05 to ch07), ~19,345 chars. 10 footnotes
  (#14 to #23), 24 new glossary rows.
- Batch B03 = Chapters 8 to 10 (ch08 to ch10), ~15,194 chars. 9 footnotes
  (#24 to #32), 24 new glossary rows.
- Batch B04 = Chapters 11 to 13 (ch11 to ch13), ~18,985 chars. 10 footnotes
  (#33 to #42), 15 new glossary rows.
- Batch B05 = Chapters 14 to 15 (ch14 to ch15), ~20,027 chars. 7 footnotes
  (#43 to #49), 11 new glossary rows.
- Batch B06 = Chapter 16 (ch16), ~11,004 chars. 5 footnotes (#50 to #54).
- Batch B07 = Chapters 17 to 18 (ch17 to ch18), ~15,534 chars. 7 footnotes
  (#55 to #61), ~25 new glossary rows.
- Batch B08 = Chapters 19 to 21 (ch19 to ch21), ~19,405 chars. 9 footnotes
  (#62 to #70), 16 new glossary rows; 10 noise.txt additions.
- Batch B09 = Chapters 22 to 24 (ch22 to ch24), ~20,823 chars. 9 footnotes
  (#71 to #79), 20 new glossary rows; 12 noise.txt additions.
- Batch B10 = Chapters 25 to 27 (ch25 to ch27), ~20,965 chars. 9 footnotes
  (#80 to #88), 17 new glossary rows; 7 noise.txt additions.
- Batch B11 = Chapters 28 to 30 (ch28 to ch30), ~17,303 chars, 627 paragraphs.
  Bilingual QC files, reading files, parity sources, 10 footnotes (#89 to #98) and
  16 new glossary rows all written; check_numbers 0 unresolved (5 noise.txt additions:
  一万亿, 百姓, 零点, 万籁, 一泻千里; plus the 四个字 -> "four words" fix), check_structure
  parity OK (159/159, 206/206, 262/262), verbatim parity zero content diffs, blind double
  translation + round-trip back-translation on the lyrical/argumentative passages,
  paranoid audit ~3.8% with observed error rate 0%. See PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 31 of 36 units translated, 98 notes, qa green.

## What is NEXT

- Batch B12 = ch31 to ch33 (~17,971 chars). Then B13 = ch34 to ch35 (see book.json
  "batches"). B13 is the LAST batch: do any back matter and a whole-book QA pass and
  write a completion report instead of another handoff.

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another per-batch branch, but fold all work onto claude/on-a-hair-trigger
  and retire the stray branch. (B11 was handed a stray branch
  claude/hair-trigger-b11-*; origin/claude/on-a-hair-trigger carried only the Step-0
  setup while the harness branch carried B01..B10, so B11 fast-forwarded
  claude/on-a-hair-trigger onto the full history + the B11 commit and deleted the stray
  branch, local and remote. Do the same each batch: commit, bring claude/on-a-hair-trigger
  to the new HEAD, push it, delete the stray.)
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). out/*_en.txt
  and out/*.epub are also gitignored. A fresh container has only source.epub + the
  committed out/*_bilingual.md (force-added past the ignore), out/*_reading.md,
  notes.json, glossary.json, book.json, data/noise.txt, PROGRESS.md, HANDOFF.md.
  Re-run ingest_epub.py to rebuild data/src; re-run split_bilingual.py on each
  committed bilingual (ch00..ch30) to rebuild data/zh and out/*_reading.md BEFORE
  building. When you commit new bilinguals, force-add them: git add -f
  out/ch31_bilingual.md (etc.); the reading files add normally.
- Authoring flow (established B02): write out/<id>_en.txt (one English paragraph
  per source paragraph), then scripts/make_bilingual.py to get the bilingual with
  verbatim `>` source lines, then split_bilingual.py. Do NOT hand-type the source
  into the bilingual.
- Source structure: one spine file per chapter; single H2 couplet title; no h3/h4;
  scene breaks are separate source paragraphs, rendered as paragraph breaks. The
  source carries NO notes of its own; every note is the translator's. Watch for
  mid-sentence paragraph splits (ch08, ch12, ch14 each had one; ch15 had a mid-word
  split in the 梨花落 aria; ch16 through ch30 had none); keep the parity count, render
  each source line as its own paragraph and split the English at the matching point.
- check_numbers noise: data/noise.txt is the project non-quantity list; ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. The checker protects clock hours/minutes and "-odd" counts via digit
  lookbehinds; maps English month names to their number (September -> 9); WORD_NUM
  knows one..thirteen, teens, tens, and first..tenth ordinals plus seventeenth,
  sixteenth. Prefer rendering a quantity so its digit survives (or, if it is a real
  translatable count, spell/render it faithfully, as B11 did with 四个字 -> "four words")
  over noising it; noise only genuine non-quantity numerals (idioms, names, 零 in
  凋零/飘零/零星/零度/零点, 百 in 老百姓, the 千 of a unit like 千帕, etc.). TRAPS carried
  forward: 万分 fragments the fraction 五万分之一 / 十万分之一 (noise residue); 几十 strips
  几十 out of 几十万 (noise the stray 万); 千百 strips 千百 out of 千百万 (B10 noised "万劳苦");
  a thousands comma ("2,594") splits into 2 and 594 (render digit strings without the
  comma); the English parser does NOT read "a hundred and eight" as 108 (render Arabic
  digits where the source does); the checker has NO 亿 branch, so 一万亿 misparses to
  10000 (B11 noised 一万亿). B11 noise: 一万亿, 百姓, 零点, 万籁, 一泻千里. B10 noise: 零度,
  万劳苦, 九泉, 二来, 一干二净, 百花, 五内. B09 noise: 三刻, 两句, 万不得已, 七窍, 零星,
  急三火四, 第二个人, 三长两短, 万事, 两个人, 万能, 千帕. B08 noise: 八、九十分, 百乐门,
  四目, 百无聊赖, 几十万, 万的输赢, 四肢, 四周. B07 noise: 贤二, 下三烂, 万端, 一了百了,
  百试百灵, 三元, 千羡万羡, 十五、六, 一百八十度, 阿四.
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
  See the kickoff message's footnote list for the full already-noted roster (now
  through ch30: 间不容发, 九一八, 中国哲学简史 anachronism, 中国民权保障同盟, 曲线救亡,
  the 红楼梦 假作真 couplet, and the 名古屋带 Nagoya obi). NOTE ch33's title 假做真时真亦假
  IS that 红楼梦 couplet, already noted at ch30 — do not re-note; render literally.
- Prose written TO the commissioner (this HANDOFF, PROGRESS, chat) uses no em
  dashes (CLAUDE.md rule 6); the translation itself may use them.
- Plot state after B11 (the hospital trap sprung, the birth-mother mystery opened):
  * ch28: Yu Xiaojiang (revealed as the new "时雨"/Timely Rain, Muci's superior) shoots
    Li Qinhong dead in the ward and passes Cong Feng out via the "《中国哲学简史》"
    fallback password to Snow Wolf and the Fourth-Avenue Special-Committee conference;
    A-Chu removes the body under a false fire alarm; the conference finishes and Cong
    Feng sails for Moscow. Du Luning and Yu Xiaojiang open the "unidentified radio"
    thread (she pins it on the Japanese, citing the Mukden Incident).
  * ch29: Winter 1932. Xiong Zida is ousted (Pravda / Xin Zhonghua Bao coverage did him
    in). Yu Xiaojiang tells Muci that Ronghua will be named a martyr and that the secret
    transmitter near Yuyuan Road is likely Japanese and likely in his own house; Muci
    names his "mother" (徐玉真) as the suspect. She is shown to be Koyama Eiko (小山缨子),
    a Japanese agent radioing as the Imperial Flower, who finds her girlhood photo gone.
    Muci (who took it) goes to A-Chu at Plum Blossom Lane; they read three photos (mother
    / disguised false mother / her true face) and drive to the Ciyun Temple 慈云寺 at 3
    a.m. A trap-brick drops a beam on A-Chu (cliffhanger).
  * ch30: Muci saves A-Chu into an underground crypt; the impostor above blows up the
    hall. Trapped, the twins bond and, using A-Chu's fall-triggered childhood memory
    (the "mirror" = the water), find the underwater passage and, in a wooden room, their
    birth mother's skeleton (murdered by waist-cutting; her identity stolen by the
    Japanese impostor, who married Yang Yuhua). They climb the hollow tree; at the top
    "Mother"/Koyama Eiko waits with a gun, offers Muci his life if he drops A-Chu. Muci
    hooks A-Chu safe, refuses, shouts "思桐/Sitong!" — a shot rings out. B12 opens here.
  * The name-slip / body-double / impostor devices are rendered as they stand, never
    reconciled; genuine slips get a first-occurrence footnote.
- Anachronism flags recorded in glossary/notes: fabi (法币, 1935) used loosely for the
  early-1930s present; the Park Hotel (国际大饭店, opened 1934) named a little early; the
  Fung Yu-lan 《中国哲学简史》/Macmillan password (pub. 1948) is anachronistic in a 1931/32
  scene (footnote #91); the Xin Zhonghua Bao name (Yan'an, 1937) is loose for the setting;
  the 名古屋带/Nagoya obi (c. 1920) is tied loosely to the 桃山/Momoyama age (footnote #98).
  Gordon Road (戈登路), Bubbling Well Road (静安寺路), Avenue Joffre (霞飞路), the Racecourse
  (跑马厅), Fourth Avenue (四马路), Yuyuan Road (愚园路), the Lyceum/Lanxin (兰心大戏院) and
  the Paramount (百乐门) are attested Shanghai landmarks; the Mukden Incident (九一八, South
  Manchuria Railway, Liutiaohu, Manchukuo) and the China League for Civil Rights are
  attested history.
