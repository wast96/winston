# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-23 (ch01-ch23) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 24 (ch24). 1
chapter plus 2 afterwords remain: B24 = ch24, then B25 = ch25 + ch26 (the two
afterwords together).

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch
was `Chang'an B23`; the next is `Chang'an B24`). CLAUDE.md records the rule; the
kickoff block below opens with that name as its first line on purpose. Keep it
there.

## Message to paste into the next chat

```
Chang'an B24
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-23 (ch01-ch23) are
done; the 25-batch plan (one chapter per batch, B25 = both afterwords) is approved.

Do Batch 24 = ch24 (第二十四章 巳初 / "Chapter Twenty-Four. The Hour of the Snake,
First Half (9 a.m.)") end to end. It is ~18,618 source chars (the longest chapter
remaining). NOTE: data/src/ and data/figs/ are gitignored and rebuild from
source.epub; if data/src/ is absent in a fresh clone, run
`python3 scripts/ingest_epub.py source.epub` first. Read the batch's source from
its text_file in book.json (data/src/52_text00049.txt); the source is
authoritative, quote it verbatim in the bilingual QC file and render it faithfully
and in full. Author one aligned bilingual QC file out/ch24_bilingual.md (source
'>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct, and translate a recurring vignette identically in both places;
the source's content-file time-marker heading line is absorbed into the H2 title,
as in ch01-ch23; render the source's per-chapter time-gloss final line as the
source's own italic note, prefixed '*[The source appends a note on the hour to
each chapter:]*'. WATCH THE HOUR: the gloss is attached to whatever dateline it
footnotes and is NOT reliably the chapter's nominal hour — ch20's gloss described
its FLASHBACK dateline (午正/noon); ch21's MATCHED its nominal hour (卯/6 a.m.);
ch22's chapter is 辰初/7 a.m. but its gloss REPEATED ch21's 卯/5 a.m. gloss (a
source mismatch); ch23's chapter is 辰正/8 a.m. and its gloss MATCHED (辰/8 a.m.).
Do not assume; render whatever the source's own dateline and gloss say, and flag
any mismatch in PROGRESS). Watch for the source's scene-break rules
(Image00005.jpg): the house style renders each scene shift as a plain paragraph
break, no separator glyph. Watch too for extractor-split paragraphs (a logical
paragraph broken across two data/src lines, the first ending on a comma or
mid-phrase); merge such halves into one bilingual pair (ch07-ch23 each merged the
dateline's split halves; NOTE the split shape VARIES — ch22's dateline tail was
the TWO full-width periods 。。, ch23's was a single 。 AND ch23 also had the
OPENING VIGNETTE split across L2/L3 on a comma; a quick scan: flag any source line
whose last char is not in 。！？"）…—： — but note lines ending in the full-width
close-quote " are already terminal, not split, and a multi-paragraph quotation
whose earlier paragraph's quote is left OPEN stays a separate pair). The most
reliable method (B16-B23 used it): write a small generator that reads the source
lines from data/src, pairs each with your hand-authored English, merges any
extractor-split halves, and asserts the concatenation of every '>' blockquote
equals the source content character-for-character before running the checks
(B23 = scripts/gen_ch23_bilingual.py, 207 body paragraphs). Then generate
out/ch24_reading.md and the parity source with
`scripts/split_bilingual.py out/ch24_bilingual.md ch24 "第二十四章　巳初"` (use the
exact full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch24_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail — if it is a real quantity, fix the ENGLISH
to carry the value rather than noising it; watch ORDERING, a new strip pattern must
precede any shorter built-in that would eat part of it first — an approximate like
百十余 must be in the --noise file so it strips before the built-ins reach it, and
watch the reverse traps: (a) a pre-existing entry like 四肢 can strip first and
orphan the 百 in 四肢百骸, so noise the residual 百骸; (b) the built-in MEASURE rules
一[…张…]/一[…天…]/一[…个…] run AFTER the --noise pass and can eat the 一 out of a
compound like 万一张/万一天/十一个 and orphan a bare 万=10000 or 十=10 — noise the
WHOLE idiom/number (万一, or 十一 as in B23) in the --noise file so it strips first;
(c) a NAME containing a numeral, like 陆三 in B23, must be noised so its 三 does not
flag; AND watch the English parser — it reads cardinals, a FEW ordinals INCLUDING
first-through-tenth, thirteenth-through-seventeenth, twentieth, and twenty-fifth
but NOT "eleventh/eighteenth/nineteenth" and NOT the other compound ordinals
"twenty-first/second/third/fourth" unless you add them to WORD_NUM, and it CANNOT
build "150" from "a hundred and fifty" but CAN match "a million"/"a hundred"/"a
thousand" via its article rules, so carry high counts as "a hundred/thousand/
million" or as digits) and
`scripts/check_structure.py --pairs data/zh/ch24.txt out/ch24_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch24" (verbatim English anchors; XHTML bodies with numeric character
references for punctuation/accents, literal CJK for Chinese terms is fine and
builds — ch01/ch09-ch23 do it — never HTML named entities; ~3 per chapter,
recurring subjects get their note at first appearance across the whole book, so
skip anything already noted in ch01-ch23). Add any figure specs to figures.json
only if the chapter has a real content illustration in data/figs/ (the source's
footnote-marker glyph Image00004.jpg and the decorative scene-break rule
Image00005.jpg are NOT figures). Rebuild with
`scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"` so the
pending-aware TOC links ch01-ch24 content and ch25/ch26 skeleton, then run
`scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"` until green. Do a
blind double-translation of a literary sample and a round-trip back-translation of
a number-dense sample (separate contexts), and record the checks and the sample
error rate in PROGRESS.md. Rewrite HANDOFF.md with the Batch 25 (= ch25 后记一 +
ch26 后记二, the two afterwords together — the LAST batch) kickoff message (its
fenced block opening with the line `Chang'an B25`; on that last batch the message
says to do the two afterwords, any back matter/colophon, a whole-book QA pass, and
write a COMPLETION REPORT instead of another handoff). Commit and push to branch
claude/the-longest-day-in-changan. Cite chapters/sections, never page numbers.
Never invent bridging text; footnote genuine ambiguity rather than smoothing it.
Do not pause for approval mid-batch. Deliver the rebuilt EPUB in chat as an
attached file.
```

## What is DONE (do not redo)

- Step 0 ingest + survey + skeleton EPUB, approved. 25-batch plan approved.
- Batch 1 = ch01, complete and committed: 12 notes, glossary seeded, qa PASS.
- Batch 2 = ch02, complete: 3 notes (15 total), EPUB metadata set for Kindle/Apple
  Books, qa PASS.
- Batches 3-20 = ch03-ch20, complete: 3 notes each (70 total by ch20), noise.txt
  and glossary grown each batch, qa PASS throughout. (ch10 AND ch11 time-glosses
  are MISMATCHED; ch20's gloss describes its FLASHBACK dateline 午正/noon.)
- Batch 21 = ch21, complete: 3 notes (73 total). glossary +27 rows, noise.txt +5.
  qa PASS. ch21's gloss (卯/6 a.m.) MATCHES its nominal hour 卯正.
- Batch 22 = ch22, complete: 3 notes (76 total). glossary +11, noise.txt +4. qa
  PASS. HOUR MISMATCH: ch22 is nominally 辰初/7 a.m. but its gloss REPEATS ch21's
  卯/5 a.m. gloss (source-side, like ch10/ch11; not a flashback).
- Batch 23 = ch23, complete and committed: out/ch23_reading.md, data/zh/ch23.txt,
  scripts/gen_ch23_bilingual.py (207 body paragraphs, 14,239 source chars incl.
  gloss). 3 notes (79 total: 应龙/the Yinglong responding-dragon flag; the lychee /
  Yang Guifei / Du Mu 过华清宫 allusion; 双陆/shuanglu the Tang board game).
  glossary +14 rows (person 陆三/Lu San; places 永崇坊/Yongchong Ward, 靖安坊/Jing'an
  Ward, 涪州/Fuzhou, 子午谷/the Ziwu Valley, 户县/Hu County; terms 应龙旗/the Yinglong
  flag, 山文甲/mountain-pattern armor, 迷幻香/befuddling-incense, 迷魂香/soul-stealing
  incense, 双陆/shuanglu, 城门郎/the gate-commander, 监门/the Gate Watch, 鱼符/
  fish-tally). noise.txt +3 (陆三 [name with 三]; 骈四丽六 [4/6 idiom]; 十一
  [LOAD-BEARING reverse-trap: strips before the built-in 一[…个…] rule orphans a
  bare 十=10 out of 十一个]). No WORD_NUM change. qa PASS (79 notes). Verbatim-quote
  check: concat of every source blockquote + the gloss equals the source content
  char-for-char (14,239 chars, L2-L211); parity 208/208; check_numbers 0
  unresolved; blind double-translation (L114-L116, the runner biting his tongue)
  and back-translation (L130/L206/L208, the loan and the Pinglu accounts) both
  clean, 0 content errors. HOUR MATCHES: ch23 is 辰正/8 a.m. and its gloss describes
  辰/8 a.m. — dateline, nominal hour, and gloss all agree. The traitor 通传/"the
  runner" (from ch01) is revealed to be 陆三, a Shouzhuolang agent of the Pinglu
  留后院; Li Bi tracks the paymaster to 平卢节度使 = 安禄山 (An Lushan; note at ch16).

## What is NEXT

- Batch 24 = ch24 (第二十四章 巳初, ~18,618 source chars, data/src/52_text00049.txt).
  Then B25 = ch25 (后记一, ~1,838) + ch26 (后记二, ~966) together, the LAST batch
  (afterwords + colophon/back matter + whole-book QA + completion report). See
  book.json's structure/batches.

## House style set by Batches 1-23 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged. Keep the
  book's own coarseness where it is coarse (ch13 "我他妈" = "I didn't fucking say";
  ch14/ch19 kept 贱婢; ch15 kept "你他妈的"; ch21 臭娘们 = "vile wench"; ch23 kept
  封大伦's 小娼妇 = "little whore" and his raving). The Son of Heaven's imperial 朕 =
  royal "Us/We/Our"; 陛下 = "Your Majesty" (address) / "His Majesty" (reference);
  圣人/圣上 = "the Sage"; 微臣 = "your humble servant"; 坤道 = "female Daoist"; 妾身
  (a woman's humble self) = "I".
- Openings: NOT every chapter has an epigraph. Each opening differs (flash-forward
  vignette, scene-setting description, or the dateline direct); translate whatever
  the source has, and translate a recurring vignette identically in both places
  (ch20's vignette recurs verbatim inside L93; ch21's two vignette paragraphs recur
  at the head of L53; ch22's two vignette paragraphs recur concatenated at the head
  of L161; ch23's opening vignette [L2+L3, extractor-split-merged: "这时候远方东边的
  日头正喷薄而出，天色大亮，整个移香阁开始弥漫起醉人的香味。"] recurs verbatim at the
  head of L88 — all rendered from a shared VIG constant). The content-file
  time-marker heading line (子正/寅正/卯正/辰正 etc.) is absorbed into the H2 chapter
  title, not made a paragraph. When the dateline is followed by a short scene-
  setting location line (ch18 "长安，万年县，安邑常乐路口。"; ch22 "长安，长安县，安业
  坊。"; ch23 "长安，长安县，兴化坊。"), that line is its own paragraph. The per-chapter
  time-gloss is the SOURCE's own note, in italics, prefixed "*[The source appends a
  note on the hour to each chapter:]*". WATCH THE HOUR: the gloss is attached to
  whatever dateline it footnotes and is NOT reliably the nominal hour — ch20 flash-
  back; ch21 MATCHED; ch22 REPEATED the previous 卯 gloss on a 辰初 chapter; ch23
  MATCHED (辰/8 a.m.). Render whatever the source says; flag any mismatch in PROGRESS
  rather than "correcting" it.
- Scene breaks: rendered as a plain paragraph break with NO separator glyph (the
  rule image Image00005.jpg is not a figure), matching ch01-ch23.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. Cast/terms that MUST be reused
  verbatim include everything decided through ch22 PLUS the ch23 additions and
  reuses: Zhang Xiaojing (张阎王 = Zhang the Yama, matching the earlier 张阎罗; 张大帅
  = "the great Chief Zhang", keeping 帅 = Chief; 张帅 = "Chief Zhang"; 张大头 = Zhang
  Big-Head; 独眼 = single eye; 五尊阎罗 = the Five-Faced Yama; 不良帅 = buliang chief),
  Xiao Gui, Li Bi (长源 Changyuan) / Deputy Director Li (靖安司丞), Li Linfu = the
  Right Minister, Li Heng / heir apparent / the Eastern Palace, Yao Runeng, Tanqi,
  Yuan Zai, Adjutant Zhao, Aluoyue, Cen Shen, Wen Ran, Wen Wuji, Wang Yunxiu, Feng
  Dalun (虞部主事 = a recorder of the Forestry and Crafts Bureau [主事 = recorder];
  熊火帮 = the Bear Fire Gang), Chen Xuanli, Prince Yong, An Lushan (安禄山, the ch23
  reveal; note at ch16), Lu San (陆三, the runner/traitor), the runner (通传, common
  noun), the Son of Heaven / the Sage, Taizhen, the Pifu/aphids (蚍蜉 — RENDERED
  "the aphids" in ch20-ch23; the glossary's older form is "the Pifu", used ch01-19).
  Orgs: the Jing'an Bureau, the Jingzhao Prefecture, the Shouzhuolang (队正 = squad
  leader, 火师 = firemaster, 守捉城 = garrison-town, 留后院 = resident-agent courtyard
  [historical synonym 进奏院], 节度使 = military commissioner), the Longwu/Yulin
  Armies, the Lüben Guards, the Left/Right Xiao Guard, the Left/Right Qianniu Guard,
  the Jinwu Guard, the Southern/Northern Command, the Court of Judicial Review, plus
  all prior. Places: Chang'an, Wannian/Chang'an County, the great watchtower, the
  Qinzheng Wuben Tower, the Yixiang Pavilion (移香阁, Feng Dalun's), the Xingqing
  Palace, the Yanxing Gate, the Qixia Gate (启夏门), Anye/Guangde/Xinghua/Yongchong
  (永崇坊)/Jing'an (靖安坊) Wards, the Cibei Temple, the Wen Incense Shop, the Pingkang
  Quarter, Liu's Bookshop, Yuezhou/Pinglu/Fanyang/Yingzhou, Fuzhou/the Ziwu Valley/
  Hu County, plus all prior. Terms: shichen / 时辰 = double-hour, watchtower / 号旗 =
  signal-flag, buliang chief, chi/li/zhang, 弹指 = finger-snap, the Yinglong flag,
  mountain-pattern armor, befuddling-incense, shuanglu, the gate-commander/the Gate
  Watch/fish-tally, the Lantern Festival, plus all prior.
- Titles/address: 靖安司丞 (Li Bi) = "Deputy Director"; 中书令 (Li Linfu) = "the
  Secretariat Director"; 李相/右相 = "the Right Minister"; 都尉 (Zhang) = "Commander";
  参军 = "Adjutant"; 评事 = "Evaluator"; 主事 = "recorder"; 郎君 = "young master";
  太子/东宫 = "heir apparent" / "the Eastern Palace"; 殿下 = "Your Highness"; 永王 =
  "Prince Yong"; emperors by temple name. Offices per Hucker (see glossary).
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name with a digit like 陆三, an idiom, a round number
  spelled out analytically, an "all-directions" 四X idiom, a myriad-idiom, a
  character-COUNT like 三个字, a literary-form idiom like 骈四丽六, a 两-idiom, an "in
  the event" idiom 万一), extend noise.txt (own-line comments) or WORD_NUM, and say
  so in PROGRESS. ORDERING is load-bearing: a new strip pattern must precede any
  shorter built-in/earlier entry that would eat part of it first — AND watch the
  reverse traps: (a) a pre-existing entry (e.g. 四肢) can strip first and orphan a
  residual (百 in 四肢百骸), so noise the residual (百骸); (b) the built-in MEASURE
  rules 一[…张…]/一[…天…]/一[…个…] run AFTER the --noise pass and can eat the 一 out
  of a compound (万一张, 十一个) and orphan a bare 万=10000 or 十=10 — noise the WHOLE
  idiom/number (万一; 十一 as in B23) so it strips first. If a flag is a REAL quantity,
  fix the ENGLISH to carry the value instead of noising it (ch18 一百五十尺 → "150
  chi"; ch20 百万百姓 → "a million commonfolk"; ch22 十二座城门 → "twelve gates";
  ch23 一万贯 → "ten thousand strings", 十一个守捉城 → "eleven garrison-towns" [the
  count is carried in the English even though 十一 is noised for the checker]). A
  genuinely dropped number must still fail. WATCH the checker's English parser: it
  reads cardinals and a FEW ordinals (first-tenth, thirteenth-seventeenth,
  twentieth, twenty-fifth) but NOT "eleventh"/"eighteenth"/"nineteenth", NOT the
  other compound ordinals unless you ADD them to WORD_NUM, and it CANNOT build "150"
  from "a hundred and fifty" — but it CAN match "a hundred"/"a thousand"/"a million"
  via its article rules. Extra-noise entries run BEFORE the built-in NOISE list.
- 二楼/二层 rendered with an English number-word so its numeral survives ("the
  second floor/tower", "two-story"); 第三层 = "the third floor"; for approximate
  "ten-odd" (十余/十几/十来) render "ten-odd" (keeps 10), not "a dozen or so". 尺 =
  "chi", 里 = "li", 丈 = "zhang", 抱 = "arm-span", 分 = "fen", 弹指 = "finger-snap",
  刻 = "mark".

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. B06-B23 were each started on a
  stray per-batch branch and all work was consolidated onto
  claude/the-longest-day-in-changan, the remote's canonical branch. B23
  specifically: the session opened on claude/batch-23-ch23-translation-njsbc5, whose
  HEAD equaled origin/claude/the-longest-day-in-changan; the canonical branch was
  checked out, reset to origin, the work done there, committed and pushed.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships (and is not committed). Note anchors must be
  verbatim English substrings or the build refuses; make the anchor unique. XHTML
  note bodies: literal CJK is fine, numeric character references for typographic
  punctuation and accented Latin (&#8212; &#8216; &#8217; &#160; ...), never HTML
  named entities. The builder inserts note anchors BEFORE markup substitution.
- When editing the JSON ledgers, use a Python load/modify/dump (ensure_ascii=False,
  indent=2 for glossary.json AND notes.json) rather than hand-editing braces; then
  json.load to verify.
- A repeatable way to build the bilingual with GUARANTEED verbatim quotation: write
  a small generator that reads the source lines from data/src, pairs each with your
  hand-authored English, and emits the '>'/English pairs (merging any extractor-
  split halves). Then assert the concatenation of all '>' lines equals the source
  content char-for-char before running the checks (B16-B23 did this; B23 =
  scripts/gen_ch23_bilingual.py, 14,239 chars incl. gloss, 207 body paragraphs).
- Extractor artifacts: a logical paragraph is sometimes split across two lines in
  data/src (no sentence-ending punctuation on the first). Merge such halves into
  one bilingual pair (ch07-ch23 merged the dateline's split halves; ch23 ALSO had
  its opening vignette split across two lines on a comma). The split TAIL varies —
  ch22's dateline tail was 。。 (two periods), ch23's was a single 。 — so check the
  exact split shape each time. A quick way to find splits: scan for source lines
  whose last char is not in 。！？"）…—： — BUT lines ending in the full-width
  close-quote " are already terminal dialogue, not split (skip them), and the
  content-marker heading (line 1) and any trailing U+200B line are not paragraphs.
  Multi-paragraph quotations stay separate.
- Cite by chapter, never by page.
- Dating: the source advances the day at the Rat hour — ch13 (亥正) is 元月十四日,
  ch14 (子初) through ch23 (辰正) are 元月十五日 (Tianbao 3 = 744 CE), present day, no
  flashback this stretch. ch23's dateline is 天宝三载元月十五日，辰正 (8 a.m.).
- The source's per-chapter time-gloss is NOT reliably the chapter's nominal hour:
  ch10/ch11 mismatched; ch20's described its FLASHBACK dateline (午正); ch22's
  REPEATED ch21's 卯/5 a.m. gloss on a 辰初/7 a.m. chapter (source mismatch); ch21's
  and ch23's MATCHED. Render whatever the source says; flag, don't "correct."
- The source sometimes uses 中元 ("Ghost Festival") where it means 上元 ("Lantern
  Festival"); translate the intent. BUT ch06's 盂兰盆节 river-lanterns AND ch22's
  中元节渡鬼 water-lanterns are genuine Ghost-Festival references; render them
  faithfully.
- Watch for authorial slips and source variants (ch03 祆正-for-Sabao; ch06/ch07
  time-gloss 日铺 for 日晡; ch07 五桶 where the math needs 十五桶; ch09 远怀坊 for
  怀远坊; ch10 AND ch11 time-glosses MISMATCHED; ch13 春名门 for 春明门, recurs
  ch16/ch22; ch21 邀风阁 for 邀风堂; ch22 烽燧堡 for 烽燧城, and the 辰初 chapter
  carrying the 卯 time-gloss). Render the intent for a mis-named established referent
  (using its DECIDED rendering) and render genuine source errors faithfully and
  visibly (rule 4); flag both in PROGRESS.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files AND check
  notes.json. Already-noted or already-appeared-and-passed subjects to NOT re-note
  include everything in notes.json ch01-ch23 and: 口蜜腹剑 (Li Linfu, ch09), the
  长恨歌 couplet + Bai Juyi (ch21), 轧荦山/Yaluoshan (ch21), 行百里者半九十 (ch21),
  统万城/赫连勃勃 (ch22), 祖道 (ch22), 利高者疑 (ch22), the Yinglong flag (ch23), the
  lychee / Yang Guifei / Du Mu allusion (ch23), 双陆/shuanglu (ch23), plus the whole
  ch01-ch20 list in prior handoffs (He Zhizhang, Yuan Zai, Prince Yong, Ozmish
  Khagan, the Right Shad, Sun Simiao, Cen Shen, the Pifu, the xiezhi, the Sogdian
  Whirl, Lai Junchen / the Eight Methods of the house of Lai, Ji Wen, the
  Shouzhuolang, the Self-Raining Pavilion, Chao Heng, the Tianshu, the makara, the
  Xuanwu Gate Incident, the Tanglong/Xiantian coups, An Lushan [ch16 — the ch23
  reveal lands on it], Jieli Khagan/Li Jing, Cao Gui, the 鸱吻/chiwen, the 长恨歌
  pieces, Sister Taizhen/Yang Guifei [ch13], etc.). Xinfeng wine (ch15), the
  jie-drum (ch06/ch10), the suanni (ch18), Emperor Yang of Sui (ch20), the Ghost
  Festival (ch06) already appeared; do not note them.
