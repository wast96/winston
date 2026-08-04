# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-22 (ch01-ch22) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 23 (ch23). 2
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two
afterwords together).

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch
was `Chang'an B22`; the next is `Chang'an B23`). CLAUDE.md records the rule; the
kickoff block below opens with that name as its first line on purpose. Keep it
there.

## Message to paste into the next chat

```
Chang'an B23
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-22 (ch01-ch22) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 23 = ch23 (第二十三章 辰正 / "Chapter Twenty-Three. The Hour of the Dragon,
Second Half (8 a.m.)") end to end. It is ~12,529 source chars. NOTE: data/src/ and
data/figs/ are gitignored and rebuild from source.epub; if data/src/ is absent in
a fresh clone, run `python3 scripts/ingest_epub.py source.epub` first. Read the
batch's source from its text_file in book.json (data/src/50_text00047.txt); the
source is authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch23_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct, and translate a recurring vignette identically in both places;
the source's content-file time-marker heading line is absorbed into the H2 title,
as in ch01-ch22; render the source's per-chapter time-gloss final line as the
source's own italic note, prefixed '*[The source appends a note on the hour to
each chapter:]*'. WATCH THE HOUR: the gloss is attached to whatever dateline it
footnotes and is NOT reliably the chapter's nominal hour — ch20's gloss described
its FLASHBACK dateline (午正/noon); ch21's MATCHED its nominal hour (卯/6 a.m.);
ch22's chapter is 辰初/7 a.m. but its gloss REPEATED ch21's 卯/5 a.m. gloss (a
source mismatch). Do not assume; render whatever the source's own dateline and
gloss say, and flag any mismatch in PROGRESS). Watch for the source's scene-break
rules (Image00005.jpg): the house style renders each scene shift as a plain
paragraph break, no separator glyph. Watch too for extractor-split paragraphs (a
logical paragraph broken across two data/src lines, the first ending on a comma or
mid-phrase); merge such halves into one bilingual pair (ch07-ch22 each merged the
dateline's split halves; NOTE ch22's dateline split had the tail line as the TWO
full-width periods 。。, not a single 。, so watch the exact split shape; a quick
scan: flag any source line whose last char is not in 。！？"）…—： — but note lines
ending in the full-width close-quote " are already terminal, not split, and a
multi-paragraph quotation whose earlier paragraph's quote is left OPEN stays a
separate pair). The most reliable method (B16-B22 used it): write a small
generator that reads the source lines from data/src, pairs each with your
hand-authored English, merges any extractor-split halves, and asserts the
concatenation of every '>' blockquote equals the source content
character-for-character before running the checks (B22 = scripts/gen_ch22_bilingual.py,
269 body paragraphs). Then generate out/ch23_reading.md and the parity source with
`scripts/split_bilingual.py out/ch23_bilingual.md ch23 "第二十三章　辰正"` (use the
exact full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch23_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail — if it is a real quantity, fix the ENGLISH
to carry the value rather than noising it; watch ORDERING, a new strip pattern must
precede any shorter built-in that would eat part of it first — an approximate like
百十余 must be in the --noise file so it strips before the built-ins reach it, and
watch the reverse trap: a pre-existing entry like 四肢 can strip first and orphan
the 百 in 四肢百骸, so noise the residual 百骸; AND watch the B22 trap that the
built-in MEASURE rules 一[…张…]/一[…天…] run AFTER the --noise pass and can eat the
一 out of a compound like 万一张/万一天 and orphan a bare 万=10000 — noise the whole
idiom 万一 in the --noise file so it strips first; and watch the English parser —
it reads cardinals, a FEW ordinals INCLUDING thirteenth-through-twentieth,
twenty-fifth, and sixteenth but NOT "eleventh/eighteenth" and NOT the other
compound ordinals "twenty-first/second/third/fourth" unless you add them to
WORD_NUM, and it CANNOT build "150" from "a hundred and fifty" but CAN match "a
million"/"a hundred"/"a thousand" via its article rules, so carry high counts as
"a hundred/thousand/million" or as digits) and
`scripts/check_structure.py --pairs data/zh/ch23.txt out/ch23_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch23" (verbatim English anchors; XHTML bodies with numeric character
references for punctuation/accents, literal CJK for Chinese terms is fine and
builds — ch01/ch09-ch22 do it — never HTML named entities; ~3 per chapter,
recurring subjects get their note at first appearance across the whole book, so
skip anything already noted in ch01-ch22). Add any figure specs to figures.json
only if the chapter has a real content illustration in data/figs/ (the source's
footnote-marker glyph Image00004.jpg and the decorative scene-break rule
Image00005.jpg are NOT figures). Rebuild with
`scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"` so the
pending-aware TOC links ch01-ch23 content and every other chapter's skeleton, then
run `scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"` until green. Do a
blind double-translation of a literary sample and a round-trip back-translation of
a number-dense sample (separate contexts), and record the checks and the sample
error rate in PROGRESS.md. Rewrite HANDOFF.md with the Batch 24 (= ch24) kickoff
message (its fenced block opening with the line `Chang'an B24`), commit, and push
to branch claude/the-longest-day-in-changan. Cite chapters/sections, never page
numbers. Never invent bridging text; footnote genuine ambiguity rather than
smoothing it. Do not pause for approval mid-batch. Deliver the rebuilt EPUB in
chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 ingest + survey + skeleton EPUB, approved. 25-batch plan approved.
- Batch 1 = ch01, complete and committed: 12 notes, glossary seeded, qa PASS.
- Batch 2 = ch02, complete: 3 notes (15 total), EPUB metadata set for Kindle/Apple
  Books, qa PASS.
- Batches 3-20 = ch03-ch20, complete: 3 notes each (70 total by ch20), noise.txt
  and glossary grown each batch, qa PASS throughout. (ch10 AND ch11 time-glosses
  are MISMATCHED; ch20's gloss describes its FLASHBACK dateline 午正/noon, NOT its
  nominal hour 卯初 — internally correct.)
- Batch 21 = ch21, complete: 3 notes (73 total: the 长恨歌 couplet + Bai Juyi
  anachronism; 轧荦山/Yaluoshan; 行百里者半九十). glossary +27 rows, noise.txt +5.
  qa PASS. ch21's gloss describes 卯/6 a.m. = its nominal hour 卯正 (MATCHES).
- Batch 22 = ch22, complete and committed: out/ch22_reading.md, data/zh/ch22.txt,
  scripts/gen_ch22_bilingual.py (269 body paragraphs, 16,401 source chars incl.
  gloss). 3 notes (76 total: 统万城/赫连勃勃 = Helian Bobo's fortress-capital and its
  awl-tested rammed walls; 祖道 = the roadside shrine of the god of journeys;
  利高者疑 = the "he who profits most is suspect" maxim). glossary +11 rows (people
  赫连勃勃/Helian Bobo; places 统万城/Tongwan City, 兴化坊/Xinghua Ward; orgs 南衙/
  the Southern Command, 北衙/the Northern Command, 大理司/the Court of Judicial
  Review [source variant of 大理寺]; terms 巽位/the Xun position, 中元节/the Ghost
  Festival, 祖道庙/the roadside shrine of the god of journeys, 风脚野驼/wind-footed
  wild camel, 水灯/water-lantern). noise.txt +4 (统万; 万一 [LOAD-BEARING, strips
  before the built-in 一[…张…]/一[…天…] measure rules orphan a bare 万]; 千辛万苦;
  四出). No WORD_NUM change. qa PASS (76 notes). Verbatim-quote check: concat of
  every source blockquote + the time-gloss equals the source content
  char-for-char (16,401 chars, L2-L272); parity 270/270; check_numbers 0
  unresolved; blind double-translation (L148-L152, Xiao Gui's death exchange) and
  back-translation (L94/L95/L215/L228, the wall/moat/Kaiyuan numbers) both clean,
  0 content errors. HOUR MISMATCH flagged: ch22 is nominally 辰初/7 a.m. but its
  gloss REPEATS ch21's 卯/5 a.m. gloss (source-side, like ch10/ch11; not a
  flashback). Source variants rendered with decided forms: 烽燧堡→"the beacon-fort"
  (堡 for 烽燧城), 春名门→"the Chunming Gate" (the known slip). The Jing'an Bureau's
  内鬼 traitor is revealed to be 通传, "the runner," rendered per the ch01 decided
  common-noun form.

## What is NEXT

- Batch 23 = ch23 (第二十三章 辰正, ~12,529 source chars, data/src/50_text00047.txt).
  Then B24=ch24 (巳初, ~18,618), B25 = ch25 (后记一) + ch26 (后记二) together. See
  book.json's structure/batches.

## House style set by Batches 1-22 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged. Keep the
  book's own coarseness where it is coarse (ch13 "我他妈" = "I didn't fucking say";
  ch14/ch19 kept 贱婢 as "treacherous/insolent slut"; ch15 kept "你他妈的"; ch21
  臭娘们 = "vile wench"; ch22 kept Xiao Gui's cold register and the coarse edges).
  The Son of Heaven's imperial 朕 = royal "Us/We/Our"; 陛下 = "Your Majesty"
  (address) / "His Majesty" (reference); 圣人/圣上 = "the Sage"; 微臣 = "your humble
  servant"; 坤道 = "female Daoist"; 官家 = "the imperial house."
- Openings: NOT every chapter has an epigraph. Each opening differs (flash-forward
  vignette, scene-setting description, or the dateline direct); translate whatever
  the source has, and translate a recurring vignette identically in both places
  (ch20's vignette recurs verbatim inside L93; ch21's two separate vignette
  paragraphs recur at the head of L53; ch22's two separate vignette paragraphs
  [L2 = "看着张小敬左右为难的窘境，萧规十分享受。", L3 = "他努力把身子挪过去，贴着
  耳朵低声说出了一句话。"] recur concatenated at the head of L161 — all rendered
  from the same VIG_A/VIG_B constants). The content-file time-marker heading line
  (子正/寅正/卯正/辰初 etc.) is absorbed into the H2 chapter title, not made a
  paragraph. When the dateline is followed by a short scene-setting location line
  (ch18 "长安，万年县，安邑常乐路口。"; ch21 "长安，兴庆宫。"; ch22 "长安，长安县，
  安业坊。" — note 长安县, the OTHER metropolitan county, not 万年县), that line is
  its own paragraph. The per-chapter time-gloss is rendered as the SOURCE's own
  note, in italics, prefixed "*[The source appends a note on the hour to each
  chapter:]*". WATCH THE HOUR: the gloss is attached to whatever dateline it
  footnotes and is NOT reliably the nominal hour — ch20's described its flashback
  hour; ch21's MATCHED; ch22's REPEATED the previous chapter's 卯 gloss on a 辰初
  chapter (a source mismatch). Render whatever the source says; flag any mismatch
  in PROGRESS rather than "correcting" it.
- Scene breaks: rendered as a plain paragraph break with NO separator glyph (the
  rule image Image00005.jpg is not a figure), matching ch01-ch22.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. Cast/terms that MUST be reused
  verbatim include everything decided through ch21 (see the ledger and prior
  handoffs) PLUS the ch22 additions and reuses: Zhang Xiaojing (张大头 = Zhang
  Big-Head, 大头 = Big-Head; 张帅 = "Chief Zhang" as the townsfolk hail him;
  张阎罗 = Zhang the Yama; 不良帅 = buliang chief; 靖安都尉 = Commander of the
  Jing'an Bureau), Xiao Gui (= Long Bo), Li Bi (Changyuan 长源) / Deputy Director Li
  (靖安司丞), Li Linfu = the Right Minister (中书令 = the Secretariat Director), Yao
  Runeng, Tanqi, Yuan Zai (大理评事/大理司 = Evaluator of the Court of Judicial
  Review), Adjutant Zhao, Aluoyue (阿罗约, the East-Market camel-breaker of Linyi,
  established ch06), 登徒子 = "the lecher," the runner (通传, incl. the revealed
  traitor), Chen Xuanli, Wen Wuji, Prince Yong, Taizhen, the Son of Heaven / the
  Sage, the Pifu/aphids (蚍蜉), Helian Bobo (赫连勃勃) + Tongwan City (统万城). Orgs:
  the Jing'an Bureau, the Lüben Guards, the Longwu/Yulin Armies, the Left/Right
  Xiao Guard, the Left/Right Qianniu Guard, the Jinwu Guard, the Southern Command
  (南衙) / the Northern Command (北衙), the Court of Judicial Review (大理寺/大理司),
  the Jingzhao Prefecture, plus all prior. Places: Chang'an, Wannian/Chang'an
  County (长安县), the great watchtower, the Qinzheng Wuben Tower, the Self-Raining
  Pavilion, the Longchi, the Xingqing Palace, the Chunming Gate (春名门/春明门,
  known slip), the Yanxing Gate, the Guangtong/Yong'an/Longshou Canals, Anye/
  Guangde/Zhiye/Xinghua (兴化坊) Wards, the beacon-fort (烽燧城/烽燧堡), plus all
  prior. Terms: shichen, watchtower / great watchtower, buliang chief, the Xun
  position (巽位) / the Eight Trigrams, the tower within the tower (楼内楼), the
  hand-declaration (手实) / concealed holding (隐寄), the walled corridor (夹城),
  signal-flag (号旗), the Ghost Festival (中元节) / water-lantern (水灯), the
  roadside shrine of the god of journeys (祖道庙), the Que-le Huo-duo, the Eighth
  Company (九死无悔 salute), chi/li/zhang, plus all prior.
- Titles/address: 靖安司丞 (Li Bi) = "Deputy Director"; 中书令 (Li Linfu) = "the
  Secretariat Director"; 李相/右相 = "the Right Minister"; 都尉 (Zhang) =
  "Commander"; 参军 = "Adjutant"; 评事 = "Evaluator"; 郎君 = "young master";
  太子/东宫 = "heir apparent" / "the Eastern Palace"; 殿下 = "Your Highness"; 永王 =
  "Prince Yong"; emperors by temple name (高祖/太宗/高宗 = Emperor Gaozu/Taizong/
  Gaozong). Offices per Hucker (see glossary).
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name, an idiom, a round number spelled out analytically,
  an "all-directions" 四X idiom incl. 四下/四外/四海/四周/四处/四出, a myriad-idiom,
  a 千古-type, an organ idiom, a character-COUNT like 三个字, a UNIT-NAME numeral,
  an idiom like 千辛万苦/千恩万谢/接二连三/漏洞百出, a 两-idiom, an "in the event"
  idiom 万一, a torture-name), extend noise.txt (own-line comments) or WORD_NUM,
  and say so in PROGRESS. ORDERING is load-bearing: a new strip pattern must
  precede any shorter built-in/earlier entry that would eat part of it first —
  AND watch two reverse traps: (a) a pre-existing entry (e.g. 四肢) can strip first
  and orphan the 百 in 四肢百骸, so noise the residual (百骸); (b) the built-in
  MEASURE rules 一[…张…]/一[…天…] run AFTER the --noise pass and can eat the 一 out
  of a compound like 万一张/万一天, orphaning a bare 万=10000 — noise the whole idiom
  (万一) in the --noise file so it strips first (the B22 fix). If a flag is a REAL
  quantity, fix the ENGLISH to carry the value instead of noising it (ch10 近百 →
  "fully a hundred"; ch18 一百五十尺 → "150 chi"; ch20 百万百姓 → "a million
  commonfolk"; ch21 开元二十五年 → needs WORD_NUM "twenty-fifth":25; ch22 四丈→"four
  zhang", 十二座城门→"twelve gates", 两百步→"two hundred paces" [200], 开元二十年→
  "twentieth year of Kaiyuan" [20], 十倍→"ten times", 三魂七魄→"three souls and
  seven spirits"). A genuinely dropped number must still fail. WATCH the checker's
  English parser: it reads cardinals and a FEW ordinals (fifth/…/tenth,
  thirteenth/fourteenth/fifteenth/sixteenth/seventeenth/twentieth/twenty-fifth) but
  NOT "eleventh"/"eighteenth", NOT the other compound ordinals unless you ADD them
  to WORD_NUM, and it CANNOT build "150" from "a hundred and fifty" — but it CAN
  match "a hundred"/"a thousand"/"a million" via its article rules. Extra-noise
  entries run BEFORE the built-in NOISE list.
- 二楼/二层 rendered with an English number-word so its numeral survives ("the
  second floor/tower", "two-story"); 第三层 = "the third floor"; for approximate
  "ten-odd" (十余/十几/十来) render "ten-odd" (keeps 10), not "a dozen or so". 尺 =
  "chi", 里 = "li", 丈 = "zhang", 抱 = "arm-span", 分 = "fen", 弹指 = "finger-snap",
  刻 = "mark".

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. B06-B22 were each started on a
  stray per-batch branch and all work was consolidated onto
  claude/the-longest-day-in-changan, the remote's canonical branch. B22
  specifically: the session opened on claude/changan-b22-translation-jo5h1h, whose
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
  hand-authored English, and emits the '>'/English pairs (merging any
  extractor-split halves). Then assert the concatenation of all '>' lines equals
  the source content char-for-char before running the checks (B16-B22 did this; B22
  = scripts/gen_ch22_bilingual.py, 16,401 chars incl. gloss, 269 body paragraphs).
- Extractor artifacts: a logical paragraph is sometimes split across two lines in
  data/src (no sentence-ending punctuation on the first). Merge such halves into
  one bilingual pair (ch07-ch22 merged the dateline's split halves). NOTE ch22's
  dateline tail line was the TWO full-width periods 。。 (not a single 。 as in
  ch21), so check the exact split shape each time. A quick way to find splits: scan
  for source lines whose last char is not in 。！？"）…—： — BUT lines ending in the
  full-width close-quote " are already terminal dialogue, not split (skip them),
  and the content-marker heading (line 1) and any trailing U+200B line are not
  paragraphs. Multi-paragraph quotations stay separate.
- Cite by chapter, never by page.
- Dating: the source advances the day at the Rat hour — ch13 (亥正) is 元月十四日,
  ch14 (子初) through ch22 (辰初) are 元月十五日 (Tianbao 3 = 744 CE). ch22's dateline
  is 天宝三载元月十五日，辰初 (present day, 7 a.m.); no flashback this chapter.
- The source's per-chapter time-gloss is NOT reliably the chapter's nominal hour:
  ch10/ch11 mismatched; ch20's described its FLASHBACK dateline (午正); ch21's
  MATCHED (卯); ch22's REPEATED ch21's 卯/5 a.m. gloss on a 辰初/7 a.m. chapter (a
  source mismatch, no flashback). Render whatever the source says; flag, don't
  "correct."
- The source sometimes uses 中元 ("Ghost Festival") where it means 上元 ("Lantern
  Festival"); translate the intent. BUT ch06's 盂兰盆节 river-lanterns AND ch22's
  中元节渡鬼 water-lanterns are genuine Ghost-Festival references; render them
  faithfully.
- Watch for authorial slips and source variants (ch03 祆正-for-Sabao; ch06/ch07
  time-gloss 日铺 for 日晡; ch07 五桶 where the math needs 十五桶; ch09 远怀坊 for
  怀远坊; ch10 AND ch11 time-glosses MISMATCHED; ch13 春名门 for 春明门, recurs
  ch16 AND ch22; ch21 邀风阁 for 邀风堂; ch22 烽燧堡 for 烽燧城, and the 辰初 chapter
  carrying the 卯 time-gloss). Render the intent for a mis-named established
  referent (using its DECIDED rendering) and render genuine source errors
  faithfully and visibly (rule 4); flag both in PROGRESS.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files AND check
  notes.json. Already-noted or already-appeared-and-passed subjects to NOT re-note
  include everything in notes.json ch01-ch22 and: 口蜜腹剑 (Li Linfu's honey-and-
  sword epithet, first appears ch09 — do NOT re-note in later Li Linfu scenes), the
  长恨歌 couplet + Bai Juyi (ch21), 轧荦山/Yaluoshan (ch21), 行百里者半九十 (ch21),
  统万城/赫连勃勃 (ch22), 祖道 (ch22), 利高者疑 (ch22), plus the whole ch01-ch20 list
  in prior handoffs (He Zhizhang, Yuan Zai, Prince Yong, Ozmish Khagan, the Right
  Shad, Sun Simiao, Cen Shen, the Pifu, the xiezhi, the Sogdian Whirl, Lai Junchen,
  Ji Wen, the Shouzhuolang, the Self-Raining Pavilion, Chao Heng, the Tianshu, the
  makara, the Xuanwu Gate Incident, the Tanglong/Xiantian coups, An Lushan, Jieli
  Khagan/Li Jing, Cao Gui's 肉食者鄙 and 君辱臣死, the 鸱吻/chiwen, the 长恨歌 pieces,
  etc.). Xinfeng wine (ch15), the jie-drum (ch06/ch10), the suanni (ch18), Emperor
  Yang of Sui (ch20), the Ghost Festival (ch06) already appeared; do not note them.
