# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4), B02 (Chapters 5 to 7), B03 (Chapters 8 to 10), B04 (Chapters 11
to 13), B05 (Chapters 14 to 15), B06 (Chapter 16), B07 (Chapters 17 to 18), B08
(Chapters 19 to 21), B09 (Chapters 22 to 24), B10 (Chapters 25 to 27), B11
(Chapters 28 to 30) and B12 (Chapters 31 to 33) are DONE, checks green, committed.
Batch B13 is next, and it is the LAST batch.

## Message to paste into the next chat

```
Hair Trigger B13 — Chapters 34 to 35 (ch34, ch35). THIS IS THE LAST BATCH.

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B13 end to end: Chapter 34 (ch34, ~6,568
source chars) and Chapter 35 (ch35, ~8,534 chars), ~15,102 chars total. This
finishes the novel (the Prologue and Chapters 1 to 33 are already translated and
built). Because it is the last batch, ALSO do any back matter, a whole-book QA
pass, and write a COMPLETION REPORT instead of another handoff (see the end).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch33 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title"; a shell loop over book.json is quickest).

Read each unit's source from data/src/ (ch34 = 37_part0035.txt, ch35 =
38_part0036.txt). Translate to the register in CLAUDE.md: clean, flowing novelistic
English, the book's own voice, all apparatus in the notes and nothing inline.
Match the established house style (set through B11/B12): straight ASCII double
quotes, ASCII ellipsis (...), semicolons/colons for flow, NO em dashes, NO curly
quotes; inner quotes as ASCII single quotes.

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
ch33 had none): if a real mid-sentence split occurs, keep the parity count, render
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
  their number (so "September" credits 9月/九); WORD_NUM knows one..thirteen, the
  teens, the tens, and first..tenth plus sixteenth/seventeenth/eighteenth ordinals.
  KNOWN PARSER TRAPS carried forward (noise the residue when they fire): the 万分
  rule fragments 五万分之一 / 十X万分之一; the 几十 rule strips 几十 out of 几十万 and
  orphans a stray 万(=10000); the 千百 rule strips 千百 out of 千百万 and orphans a stray
  万 (B10 noised "万劳苦"); a thousands comma ("2,594") is split into 2 and 594 (render
  digit strings without the comma); the English parser does NOT read "a hundred and
  eight" as 108 (render Arabic digits where the source does). The checker has NO
  亿(=10^8) branch, so 一万亿 misparses to 10000 (B11 noised 一万亿) and simplified 亿
  is not read at all (一个亿 in ch31 went uncaught, harmless). NEW in B12: the generic
  千万 intensifier rule fragments a MONETARY 三千万/七千万/五千万 and orphans a bare 3/7/5;
  B12 fixed this in check_numbers.py by adding r"[一二三四五六七八九十]千万" (and 千萬)
  BEFORE the bare 千万 entry, since extra-noise runs AFTER the built-in NOISE and so
  cannot pre-empt it — if a similar N千万/N千萬 money amount appears, that rule already
  covers it; render English as "thirty million" etc. Names/idioms carrying a numeral
  get NOISED, not dropped. B12 added seven noise rows (阿九, 百看不厌, 百合, 千野, 一万个,
  两边, 五分属) plus the check_numbers.py money rule and WORD_NUM "eighteenth". B11 added
  five (一万亿, 百姓, 零点, 万籁, 一泻千里); B10 seven (零度, 万劳苦, 九泉, 二来, 一干二净,
  百花, 五内); B09 twelve; B08 ten (full lists in PROGRESS.md and inline in data/noise.txt
  comments). Prefer rendering a real, translatable count faithfully (B11 did 四个字 ->
  "four words") over noising it.
- scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md  (parity
  must be OK). Also sanity-check verbatim fidelity by diffing data/zh/<id>.txt
  (minus its first ### title line) against the source paragraphs (data/src file,
  minus its first two metadata lines) — aim for zero content diffs (the source
  files' missing final newline is the only expected diff).
Apply blind double translation and round-trip back-translation to the argumentative
or lyrical passages and sample the plain narration; give 3 to 5 percent of the
batch the full paranoid audit and report the observed error rate.

Footnotes into notes.json (about 3 per chapter-equivalent, so ~6 across the two
chapters; anchors must be exact verbatim substrings of the English prose — the
builder REFUSES to build on an unmatched anchor, so verify each with a quick
grep -cF before building; XHTML bodies use NUMERIC character references only, e.g.
&#8212; &#8216; &#8217; &#8211; &#160; &#8230;, never named entities; hanzi may be
written literally, but re-read the JSON to confirm no glyph got mistyped — B12
initially mistyped 铙 as 馓 and 醇 as 醶 and had to fix). For each chapter the title
couplet is the first thing to footnote, anchored to a thematically apt verbatim
phrase in that chapter's prose (the H2 chapter title itself does not take a note
ref). ch34 = 反客为主深造次 (反客为主 is one of the Thirty-Six Stratagems 三十六计,
"turn the guest into the host" — trace and confirm corroborated), ch35 = 一举锄奸雁归行
(likely the author's own seven-character line in the old manner — trace, and if not
traceable render literally and footnote it as pastiche). Many of this book's titles
ARE the author's pastiche, not verifiable single quotations (ch17, ch19, ch20, ch22,
ch23, ch24, ch26, ch27, ch29, ch30, ch31's exact 7-char form). Recurring literary/
historical refs get their note at FIRST appearance only. Already noted through B12:
梨花落 aria (ch12); 小松 杜荀鹤 (ch5); 瀑布联句 (ch15); 西厢记 (ch16); 陆羽 六羡歌 and Cao
Zhi 七步诗 (ch17); Yu Xuanji 鱼玄机 and the 月份牌 poster (ch19); Pushkin "To the Sea",
Dostoevsky, Mencius 孟子 (ch20); 千钧一发 韩愈 and 箭在弦上 陈琳 and Fang Zhitong's Xiang
cover-name (ch21); Gu Shunzhang 顾顺章 and Wu Hao 伍豪 = Zhou Enlai (ch22); 黛玉焚稿 红楼梦
and 宁可错杀一千 (ch24); 插秧诗 (布袋和尚), 移花接木, 耳听为虚眼见为实 (ch25); 岳阳楼记, the
Bai Yun title pun, 踏破铁鞋无觅处 (ch26); the peony/Wu Zetian legend and 回头是岸/水到渠成
(ch27); 间不容发 枚乘 and the Mukden Incident 九一八 and the anachronistic 《中国哲学简史》/
Macmillan (ch28); the China League for Civil Rights 中国民权保障同盟 and Wang Jingwei's
曲线救亡 (ch29); the 红楼梦 假作真 couplet (太虚幻境) and the 名古屋带 Nagoya obi (ch30); the
游鱼见食不见钩 fishing proverb (ch31); 醇酒美人 (史记 信陵君) + 鸳鸯剑 (红楼梦 尤三姐), Thales/
Plato (Theaetetus), Nietzsche's tree (Zarathustra), and 文野三界之别 Liang Qichao (ch32);
上邪 (汉乐府 铙歌十八曲) and the 富士山顶雪飘飘 Japanese verse (ch33). NOTE: the 红楼梦 太虚幻境
假作真 couplet was noted at ch30 and cross-referenced (not re-noted) at ch33 — do the same
for any recurring ref.

Glossary rows into glossary.json for every NEW name, place, org and term, one decided
rendering per referent — CHECK the existing glossary first and reuse those renderings.
Recurring cast active at the B12/B13 seam: the twins Yang Muci (杨慕次, 阿次 = A-Ci, the
Party's man / codename Drifting Wind 飘风) and Yang Muchu / A-Chu (杨慕初/阿初), the surgeon
and Party superior's ally, now openly allied and closing the net; He Yashu (和雅淑, A-Chu's
mistress, who has pledged herself to him and become his willing decoy/hook); Xia Yuechun
(夏跃春, the surgeon, A-Chu's contact who warns him via the Thales/Plato cipher); Ming Tang
(明堂, the Stock Exchange broker who buys up the ruined Yang enterprises for A-Chu); Rong
Sheng (荣升) and Rong Gui (荣归) at the Huamei Bookstore; Rong Chu / Rong'er (荣初/荣儿);
Liu A-Si (刘阿四), Lu Liangchen (陆良晨); Han Zhengqi (韩正齐), Yu Xiaojiang (俞晓江, the new
"时雨"/Timely Rain, Muci's superior), Zhong Yundi (钟云迪), Snow Wolf (雪狼). Enemy/target:
Du Luning (杜旅宁, Muci's chief, whose car-bomb near-miss opens B12); Xiong Zida (熊自达,
ousted). CAPTURED at the end of B12: the false Amah A-Yue (岳嬷嬷 — a Japanese agent, NOT the
real Amah A-Yue, who was murdered 20 years ago and is the cut-in-two skeleton; the impostor
tried to hypnotize A-Chu via medicinal food and is now cuffed, mid-interrogation). ON THE RUN:
Yang Yuhua (杨羽桦, living under the murdered 杨羽柏/Yang Yubo's identity), who in ch32 shot and
killed the Japanese spy Koyama Eiko (小山缨子 = the false 徐玉真/"Xu Yuzhen", the Imperial Flower
帝国之花) in his drawing room, was seen by his daughter Yang Sitong (杨思桐) over the corpse, and
fled a Detective-Division raid. DEAD: Koyama Eiko (小山缨子, shot by Yang Yuhua, ch32); her elder
sibling/handler Koyama Chino (小山千野, appears only in the 1909 flashback). Keep one rendering
per referent across the whole book. Twin / identity handling: render 阿初 vs 阿次 by context
(A-Chu / A-Ci; Muci for the narration of 阿次); the ch33 body-double swap (Muci disguised as
A-Chu, hypnotized while the real A-Chu waits) and any source name slip are rendered as they
stand, footnoting a genuine slip at first occurrence rather than silently reconciling.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(with ch34 and ch35 done, all 36 units are translated; the TOC links every chapter's
content). Run scripts/qa_epub.py "out/On a Hair Trigger.epub" until green.

BECAUSE THIS IS THE LAST BATCH, also:
- Back matter: check back_matter.json (colophon) and book.json's translator_note; make sure
  the translator's note and any colophon render and read cleanly for the finished book.
- Whole-book QA pass: re-run split_bilingual.py for ALL ids ch00..ch35, then
  check_structure.py (parity) and check_numbers.py --noise on ALL bilinguals (all 0/OK),
  and qa_epub.py on the final build (green). Confirm the full hyperlinked TOC, continuous
  footnote numbering, glossary and translator's note current, figures/captions if any.
- Write a COMPLETION REPORT (a new file, e.g. COMPLETION.md, and a dated CHANGELOG.md entry)
  summarizing the finished book: total chapters, total footnotes, glossary size, the checks
  run book-wide and their results, known anachronisms/annotations, and the observed audit
  error rate. Do NOT write another HANDOFF kickoff.

Commit on branch claude/on-a-hair-trigger. Cite chapters, never page numbers. Never invent
bridging text or silently drop material; footnote genuine ambiguity and leave it visible. If
a source carries a pirate-site watermark line (as ch06, ch28 and ch32 did), keep it verbatim
in the bilingual `>` line but leave it out of the reading text and footnote it. Do not pause
for approval mid-batch. When done, deliver out/On a Hair Trigger.epub to me as an attached
file in the chat.
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
- Batch B11 = Chapters 28 to 30 (ch28 to ch30), ~17,303 chars. 10 footnotes
  (#89 to #98), 16 new glossary rows; 5 noise.txt additions.
- Batch B12 = Chapters 31 to 33 (ch31 to ch33), ~17,971 chars, 574 paragraphs.
  Bilingual QC files, reading files, parity sources, 9 footnotes (#99 to #107) and
  17 new glossary rows all written; check_numbers 0 unresolved (7 noise.txt additions:
  阿九, 百看不厌, 百合, 千野, 一万个, 两边, 五分属; plus a check_numbers.py money rule
  r"[一二三四五六七八九十]千万"/千萬 before the bare 千万 intensifier, and WORD_NUM
  "eighteenth": 18); check_structure parity OK (207/207, 172/172, 195/195), verbatim
  parity zero content diffs, blind double translation + round-trip back-translation on
  the argumentative/lyrical passages (no divergence, no omission), paranoid audit ~3.5%
  with observed error rate 0%. See PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 34 of 36 units translated, 107 notes, qa green.

## What is NEXT

- Batch B13 = ch34 to ch35 (~15,102 chars). This is the LAST batch: do any back matter
  and a whole-book QA pass and write a completion report instead of another handoff.

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another per-batch branch, but fold all work onto claude/on-a-hair-trigger
  and retire the stray branch. (Each batch has been handed a stray per-batch branch;
  origin/claude/on-a-hair-trigger carried only the Step-0 setup while the harness
  branch carried the accumulated batch work, so each batch fast-forwards
  claude/on-a-hair-trigger onto the full history + the new commit and deletes the
  stray branch, local and remote. Do the same: commit, bring claude/on-a-hair-trigger
  to the new HEAD, push it, delete the stray.)
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). out/*_en.txt
  and out/*.epub are also gitignored. A fresh container has only source.epub + the
  committed out/*_bilingual.md (force-added past the ignore), out/*_reading.md,
  notes.json, glossary.json, book.json, data/noise.txt, PROGRESS.md, HANDOFF.md.
  Re-run ingest_epub.py to rebuild data/src; re-run split_bilingual.py on each
  committed bilingual (ch00..ch33) to rebuild data/zh and out/*_reading.md BEFORE
  building. When you commit new bilinguals, force-add them: git add -f
  out/ch34_bilingual.md (etc.); the reading files add normally.
- Authoring flow (established B02): write out/<id>_en.txt (one English paragraph
  per source paragraph), then scripts/make_bilingual.py to get the bilingual with
  verbatim `>` source lines, then split_bilingual.py. Do NOT hand-type the source
  into the bilingual.
- House style (B11/B12): straight ASCII double quotes, ASCII ellipsis (...),
  semicolons/colons for flow, NO em dashes, NO curly quotes; inner quotes as ASCII
  single quotes. (Earlier chapters ch00..ch27 used curly quotes/em dashes; do not
  "fix" them — leave each chapter as built.)
- Source structure: one spine file per chapter; single H2 couplet title; no h3/h4;
  scene breaks are separate source paragraphs, rendered as paragraph breaks. The
  source carries NO notes of its own; every note is the translator's. Watch for
  mid-sentence paragraph splits (ch08, ch12, ch14 each had one; ch15 had a mid-word
  split in the 梨花落 aria; ch16 through ch33 had none); keep the parity count, render
  each source line as its own paragraph and split the English at the matching point.
- One source line can carry a pirate-site watermark appended to real content (ch32
  line "生命短暂才显得美丽啊。阳光中文网 www.sunshe.com..."): translate only the real
  sentence into the reading text, keep the whole line verbatim in the bilingual `>`,
  and footnote the watermark. ch06 and ch28 had standalone watermark lines.
- check_numbers noise: data/noise.txt is the project non-quantity list; ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. Extra-noise is applied AFTER the built-in NOISE, so it cannot pre-empt a
  built-in rule that fragments a real quantity — those fixes go in check_numbers.py
  itself (as B12 did for N千万). The checker protects clock hours/minutes and "-odd"
  counts via digit lookbehinds; maps English month names to their number; WORD_NUM
  knows one..thirteen, teens, tens, first..tenth plus sixteenth/seventeenth/eighteenth.
  Prefer rendering a quantity so its digit survives (or, if a real translatable count,
  render it faithfully) over noising it; noise only genuine non-quantity numerals
  (idioms, names, 零 in 凋零/飘零/零星/零度/零点, 百 in 老百姓/百合/百看不厌, the 千 of a name
  like 千野, etc.). TRAPS carried forward: 万分 fragments 五万分之一/十万分之一 (noise residue);
  几十 strips 几十 out of 几十万 (noise the stray 万); 千百 strips 千百 out of 千百万 (B10
  noised "万劳苦"); the bare 千万 intensifier fragments a MONETARY N千万 (B12 fixed in the
  .py before the bare rule); a thousands comma ("2,594") splits into 2 and 594 (render
  digit strings without the comma); "a hundred and eight" is not read as 108 (render
  Arabic digits where the source does); no 亿 branch, so 一万亿 -> 10000 (B11 noised it)
  and simplified 亿 (一个亿) is uncaught (harmless). B12 noise: 阿九, 百看不厌, 百合, 千野,
  一万个, 两边, 五分属. B11 noise: 一万亿, 百姓, 零点, 万籁, 一泻千里. B10 noise: 零度, 万劳苦,
  九泉, 二来, 一干二净, 百花, 五内. B09 noise: 三刻, 两句, 万不得已, 七窍, 零星, 急三火四,
  第二个人, 三长两短, 万事, 两个人, 万能, 千帕. B08 noise: 八、九十分, 百乐门, 四目, 百无聊赖,
  几十万, 万的输赢, 四肢, 四周. B07 noise: 贤二, 下三烂, 万端, 一了百了, 百试百灵, 三元,
  千羡万羡, 十五、六, 一百八十度, 阿四.
- Reign-era dates appear beside their Western years; keep both, and let check_numbers
  see the Western year. 宣统元年 = 1909; a Japanese flashback in ch32 dates the whole
  Koyama backstory to early May 1909. Japanese Shōwa era also appears (Shōwa 4 = 1929).
- Deliverable filename has a space: quote it, "out/On a Hair Trigger.epub".
- Write JSON via a file (not shell heredocs) so Chinese glyphs are not mangled;
  re-read to verify (and scan `en` fields for stray hanzi). Watch apostrophes in a
  Python heredoc (B09 hit "Jing'an"); use double-quoted strings or a .py file. XHTML
  note bodies use numeric character references only. Also re-read note bodies for
  MISTYPED hanzi (B12 typed 馓 for 铙 and 醶 for 醇 and fixed them).
- Recurring names AND recurring literary/historical allusions get their note at
  FIRST appearance in the book; reuse glossary renderings, do not re-romanize.
  See the kickoff message's footnote list for the full already-noted roster (now
  through ch33). A recurring ref gets a cross-reference, not a repeat (as ch33 did
  for the ch30 红楼梦 假作真 couplet).
- Prose written TO the commissioner (this HANDOFF, PROGRESS, chat) uses no em
  dashes (CLAUDE.md rule 6); the translation itself may use them (though B11/B12
  chose not to, for house-style consistency at the seam).
- Plot state after B12 (the impostors run to ground, the mystery all but closed):
  * ch31: Muci's cry "思桐/Sitong!" throws Koyama Eiko off; she flees the false hollow
    tree at the Ciyun Temple. A-Chu's people (Rong Chu, Liu A-Si, Lu Liangchen) arrive;
    the twins part coldly, A-Chu now composed and dominant. A-Chu's rigged car-bomb at
    the mountain gate nearly kills Du Luning; Muci saves him, and Du orders Muci not to
    go home and to search the Yuyuan Road radio. The Yang Bank is collapsing: Ming Tang
    (Stock Exchange broker) forces Yang Yuhua to sell everything; A-Chu, it emerges, is
    the buyer/destroyer, and courts He Yashu openly to use her as bait against Yang
    Yuhua. Muci confronts A-Chu for using a woman as a decoy; Yashu, undeterred, pledges
    herself to A-Chu as his willing "hook."
  * ch32: Muci, treated by Xia Yuechun, hints at a hidden traitor near A-Chu; Yuechun
    warns A-Chu by the Thales/Plato cipher ("the master overlooks what is at his side").
    A-Chu, softening toward Yashu, half-senses the medicinal-food hypnosis but does not
    yet place it. The 1909 backstory unfolds in full: Koyama Chino (Eiko's handler) forced
    Eiko to seduce Yang Yuhua, blackmail and remake him by face-changing surgery to
    replace his brother Yang Yubo. In the present, ruined and cast off, Yang Yuhua shoots
    Koyama Eiko dead in his drawing room; a second woman's scream ends the chapter.
  * ch33: the screamer is his daughter Yang Sitong, who sees him over the corpse and flees;
    a Detective-Division raid drives Yang Yuhua out through the back garden, a fugitive.
    At the Huamei Bookstore, Rong Sheng deduces from Yashu's book-list that her man is
    A-Chu (a blue book-bag with a florist's card and an 上邪 love-oath thread the scene).
    At No. 18 Changle Street, the "Amah A-Yue" hypnotizes "A-Chu" via congee — but it is
    Muci in disguise; the real A-Chu waits at the door. They unmask her: she is a Japanese
    agent (the true Amah A-Yue was murdered 20 years ago and IS the cut-in-two skeleton the
    twins found; the impostor faked it younger to pass it off as their birth mother). She is
    cuffed and, as ch33 ends, is under Muci's interrogation, having begun to break.
  * Open for B13: Yang Yuhua at large; the false Amah A-Yue's confession (the birth mother's
    real fate and remains); Rong Sheng's discovery; the endgame of the twins' operation. The
    name-slip / body-double / impostor devices are rendered as they stand, never reconciled.
- Anachronism flags recorded in glossary/notes: fabi (法币, 1935) used loosely for the
  early-1930s present; the Park Hotel (国际大饭店, opened 1934) named a little early; the
  Fung Yu-lan 《中国哲学简史》/Macmillan password (pub. 1948) is anachronistic (footnote #91);
  the Xin Zhonghua Bao name (Yan'an, 1937) is loose; the 名古屋带/Nagoya obi (c. 1920) is
  tied loosely to the 桃山/Momoyama age (footnote #98). Attested Shanghai/history: Gordon
  Road, Bubbling Well Road, Avenue Joffre, the Racecourse, Fourth Avenue, Yuyuan Road, the
  Lyceum/Lanxin, the Paramount; the Mukden Incident (九一八) and the China League for Civil
  Rights. B12 references checked: 醇酒美人 (史记 信陵君) and 鸳鸯剑 (红楼梦 尤三姐), Thales via
  Plato's Theaetetus, Nietzsche's Zarathustra tree, 上邪 (汉乐府), Liang Qichao's 文野三界 —
  all corroborated; the 富士山顶雪飘飘 Japanese verse and ch31's exact 7-char title are the
  author's pastiche (uncorroborated).
