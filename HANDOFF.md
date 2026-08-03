# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-21 (ch01-ch21) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 22 (ch22). 3
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two
afterwords together).

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch
was `Chang'an B21`; the next is `Chang'an B22`). CLAUDE.md records the rule; the
kickoff block below opens with that name as its first line on purpose. Keep it
there.

## Message to paste into the next chat

```
Chang'an B22
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-21 (ch01-ch21) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 22 = ch22 (第二十二章 辰初 / "Chapter Twenty-Two. The Hour of the Dragon,
First Half (7 a.m.)") end to end. It is ~14,446 source chars. NOTE: data/src/ and
data/figs/ are gitignored and rebuild from source.epub; if data/src/ is absent in
a fresh clone, run `python3 scripts/ingest_epub.py source.epub` first. Read the
batch's source from its text_file in book.json (data/src/48_text00045.txt); the
source is authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch22_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct, and translate a recurring vignette identically in both places;
the source's content-file time-marker heading line is absorbed into the H2 title,
as in ch01-ch21; render the source's per-chapter time-gloss final line as the
source's own italic note, prefixed '*[The source appends a note on the hour to
each chapter:]*'. WATCH THE HOUR: ch20's gloss described the in-body FLASHBACK
dateline (午正/noon), not the chapter's nominal hour; ch21's gloss MATCHED its
nominal hour (卯/6 a.m.). Do not assume either way — render whatever the source's
own dateline and gloss say, and flag any mismatch in PROGRESS). Watch for the
source's scene-break rules (Image00005.jpg): the house style renders each scene
shift as a plain paragraph break, no separator glyph. Watch too for
extractor-split paragraphs (a logical paragraph broken across two data/src lines,
the first ending on a comma or mid-phrase); merge such halves into one bilingual
pair (ch07-ch21 each merged the dateline's split halves, and several the opening
vignette's; a quick scan: flag any source line whose last char is not in 。！？"）…—
nor a colon — but note lines ending in the full-width close-quote " are already
terminal, not split, and a multi-paragraph quotation whose earlier paragraph's
quote is left OPEN stays a separate pair). The most reliable method (B16-B21 used
it): write a small generator that reads the source lines from data/src, pairs each
with your hand-authored English, merges any extractor-split halves, and asserts
the concatenation of every '>' blockquote equals the source content
character-for-character before running the checks (B21 = scripts/gen_ch21_bilingual.py,
229 body paragraphs). Then generate out/ch22_reading.md and the parity source with
`scripts/split_bilingual.py out/ch22_bilingual.md ch22 "第二十二章　辰初"` (use the
exact full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch22_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail — if it is a real quantity, fix the ENGLISH
to carry the value rather than noising it; watch ORDERING, a new strip pattern must
precede any shorter built-in that would eat part of it first — an approximate like
百十余 must be in the --noise file so it strips before the built-ins reach it, and
watch the reverse trap B19 hit: a pre-existing entry like 四肢 can strip first and
orphan the 百 in 四肢百骸, so noise the residual 百骸; and watch the English parser —
it reads cardinals, a FEW ordinals INCLUDING thirteenth-through-twentieth,
twenty-fifth, and sixteenth but NOT "eleventh/eighteenth" and NOT the other
compound ordinals "twenty-first/second/third/fourth" unless you add them to
WORD_NUM as B21 added "twenty-fifth", and it CANNOT build "150" from "a hundred
and fifty" but CAN match "a million"/"a hundred"/"a thousand" via its article
rules, so carry high counts as "a hundred/thousand/million" or as digits) and
`scripts/check_structure.py --pairs data/zh/ch22.txt out/ch22_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch22" (verbatim English anchors; XHTML bodies with numeric character
references for punctuation/accents, literal CJK for Chinese terms is fine and
builds — ch01/ch09-ch21 do it — never HTML named entities; ~3 per chapter,
recurring subjects get their note at first appearance across the whole book, so
skip anything already noted in ch01-ch21). Add any figure specs to figures.json
only if the chapter has a real content illustration in data/figs/ (the source's
footnote-marker glyph Image00004.jpg and the decorative scene-break rule
Image00005.jpg are NOT figures). Rebuild with
`scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"` so the
pending-aware TOC links ch01-ch22 content and every other chapter's skeleton, then
run `scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"` until green. Do a
blind double-translation of a literary sample and a round-trip back-translation of
a number-dense sample (separate contexts), and record the checks and the sample
error rate in PROGRESS.md. Rewrite HANDOFF.md with the Batch 23 (= ch23) kickoff
message (its fenced block opening with the line `Chang'an B23`), commit, and push
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
- Batch 3 = ch03, complete: 4 notes (19 total), noise.txt extended, qa PASS.
- Batch 4 = ch04, complete: 3 notes (22 total), noise.txt extended, qa PASS.
- Batch 5 = ch05, complete: 3 notes (25 total), noise.txt extended, qa PASS.
- Batch 6 = ch06, complete: 3 notes (28 total), noise.txt extended, qa PASS.
- Batch 7 = ch07, complete: 3 notes (31 total), noise.txt extended, qa PASS.
- Batch 8 = ch08, complete: 3 notes (34 total), glossary grown, noise.txt
  extended, qa PASS.
- Batch 9 = ch09, complete: 3 notes (37 total), glossary grown, noise.txt
  extended, qa PASS.
- Batch 10 = ch10, complete: 3 notes (40 total), glossary grown by 46 rows,
  noise.txt extended, qa PASS.
- Batch 11 = ch11, complete: 3 notes (43 total), glossary grown by 20 rows,
  noise.txt extended, qa PASS.
- Batch 12 = ch12, complete: 3 notes (46 total), glossary grown by ~15 rows,
  noise.txt extended, qa PASS.
- Batch 13 = ch13, complete: 3 notes (49 total), glossary grown by 23 rows,
  noise.txt extended, qa PASS.
- Batch 14 = ch14, complete: 3 notes (52 total), glossary grown by 26 rows,
  noise.txt extended, qa PASS.
- Batch 15 = ch15, complete: 3 notes (55 total), glossary grown by 26 rows,
  noise.txt extended, qa PASS.
- Batch 16 = ch16, complete: 3 notes (58 total), glossary grown by 19 rows,
  noise.txt extended, qa PASS.
- Batch 17 = ch17, complete: 3 notes (61 total), glossary grown by 10 rows,
  noise.txt extended, qa PASS.
- Batch 18 = ch18, complete: 3 notes (64 total), glossary grown by 25 rows,
  noise.txt extended by 7 entries, qa PASS.
- Batch 19 = ch19, complete: 3 notes (67 total), glossary grown by 14 rows,
  noise.txt extended by 7 entries, qa PASS.
- Batch 20 = ch20, complete: 3 notes (70 total), glossary grown by 29 rows,
  noise.txt extended by 2 entries, qa PASS. ch20's time-gloss describes 午正/noon
  = the in-body FLASHBACK dateline, NOT its nominal hour 卯初 (internally correct).
- Batch 21 = ch21, complete and committed: out/ch21_reading.md, data/zh/ch21.txt,
  3 notes (73 total: the 长恨歌 couplet 在天愿作比翼鸟，在地愿为连理枝 + the "man
  surnamed Bai" = Bai Juyi anachronism; 轧荦山/Yaluoshan = An Lushan's childhood
  name Easter egg; 行百里者半九十 from the 战国策). glossary.json grown by 27 rows
  (people 轧荦山/Yaluoshan, 贞顺武皇后/Empress Wu Zhenshun, 武惠妃/Consort Wu, 李瑛/
  Li Ying, 高祖/Emperor Gaozu; places 疾陵城/Jiling, 陇西/Longxi, 太极殿/the Taiji
  Hall, 永安宫/the Yong'an Palace, 望仙门/the Wangxian Gate, 通化门/the Tonghua Gate,
  曲江/Qujiang, 朱雀街/the Vermilion Bird Avenue alias, 贞顺武皇后庙/the Temple of
  Empress Wu Zhenshun; terms 夹城/the walled corridor, 复道/the elevated corridor,
  跸口/passing-bay, 缒架/the lowering-frame, 号旗/signal-flag, 披帛/silk stole, 假披/
  false drape, 手实/hand-declaration, 隐寄/concealed holding, 授宅推恩令/the Edict of
  Grace on the Bestowal of Residences, 象牙柄折刀/ivory-handled folding knife, 城上郎/
  wall-officer, 邀风阁/the Wind-Wooing Hall [source variant of 邀风堂]). noise.txt
  extended by 5 entries (漏洞百出, 智计百出 [both 百出="countless"], 两情相悦, 判若
  两人 [两-idioms], 三个字 [character-count for 走夹城] — all non-quantity).
  check_numbers.py WORD_NUM extended: "twenty-fifth": 25 (compound ordinal 开元
  二十五年). qa PASS (73 notes). Verbatim-quote check: concatenation of every source
  blockquote + the time-gloss equals the source content char-for-char (14,710
  chars, lines 2-232); parity 230/230; check_numbers 0 unresolved; blind
  double-translation (L39-L41, the couplet/dream) and back-translation (L129-L130,
  the walled-corridor numbers) both clean, 0 content errors. ch21's time-gloss
  describes 卯/6 a.m. = its nominal hour 卯正 (MATCHES; no flashback, no mismatch —
  flagged in PROGRESS). Source variant 邀风阁 (阁) for 邀风堂 (堂) rendered with the
  decided form "the Wind-Wooing Hall" (flagged in PROGRESS).

## What is NEXT

- Batch 22 = ch22 (第二十二章 辰初, ~14,446 source chars, data/src/48_text00045.txt).
  Then B23=ch23 (辰正, ~12,529), B24=ch24 (巳初, ~18,618), B25 = ch25 (后记一) +
  ch26 (后记二) together. See book.json's structure/batches.

## House style set by Batches 1-21 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged. Keep the
  book's own coarseness where it is coarse (ch13 rendered Zhang's "我他妈" as
  "I didn't fucking say ..."; ch14 kept 贱婢 as "treacherous slut"; ch15 kept Xiao
  Gui's "你他妈的" as "Can't you fucking give it me first?"; ch19 rendered Chen
  Xuanli's 还他妈的敢说这种胡话 as "such fucking nonsense" and 大胆贱婢 as
  "insolent slut"; ch21 kept 臭娘们 as "vile wench"). The Son of Heaven's imperial
  first person 朕 is rendered with the royal "Us/We/Our" (ch20, ch21); 陛下 =
  "Your Majesty" (direct address), "His Majesty" (reference); the Pifu's
  mock-humble 微臣 = "your humble servant." 坤道 = "female Daoist."
- Openings: NOT every chapter has an epigraph. Each chapter's opening differs
  (flash-forward vignette, scene-setting description, or the dateline direct);
  translate whatever the source has, and translate a recurring vignette
  identically in both places (ch04 Qujiang; ch05 writing-case; ch06 kiln-duel;
  ch07 festival-crowd; ch08 plain-oil-fritters; ch09 ox-cart ambush; ch10
  Bureau-fire; ch11 Long-Bo's-pavilion; ch12 the golden-horsemen vignette; ch13
  Long-Bo-climbing-from-the-cellar; ch14 Taizhen-catching-Tanqi's-hands; ch15 the
  reversed-crossbow standoff; ch16 Li-Bi-crouched-in-the-water-channel; ch17 the
  crowd-falling-silent-for-the-wonder; ch18 the carriage-horses-turning-their-ears;
  ch19 the one-eyed-Zhang-making-out-the-many-colored-gauze; ch20 the crowd
  turning to the girl who holds the lantern-float red tally; ch21 the two figures
  sliding down the wall like lovebirds — each recur later and were translated
  identically. ch20's vignette (L2, L3+L4) recurs verbatim inside L93; ch21's
  vignette (L2, L3 — two SEPARATE paragraphs, each already terminal) recurs
  verbatim at the head of L53, both rendered from the same VIG_A/VIG_B constants).
  The content-file time-marker heading line (子正/寅正/卯正 etc.) is absorbed into
  the H2 chapter title, not made a paragraph. When the dateline is followed by a
  short scene-setting location line (ch18 "长安，万年县，安邑常乐路口。"; ch20 "长安，
  万年县，靖恭坊。"; ch21 "长安，兴庆宫。"), that line is its own paragraph. The
  source's per-chapter time-gloss (its own footnote on the dateline) is rendered as
  the SOURCE's own note, in italics, prefixed "*[The source appends a note on the
  hour to each chapter:]*", distinct from translator's notes. Its ordinary words
  are translated; only technical hour-names are romanized. WATCH THE HOUR: the
  gloss is attached to the dateline it footnotes — ch20's chapter is nominally 卯初
  (5 a.m.) but opens with a FLASHBACK at 午正 (noon), and the gloss describes noon;
  ch21 has no flashback and its gloss MATCHES its nominal hour (卯/6 a.m.). Render
  whatever the source's dateline and gloss say; flag any hour mismatch in PROGRESS
  rather than "correcting" it.
- Scene breaks: the source divides multi-scene chapters with a decorative rule
  image (Image00005.jpg, alt="line"). House style renders each scene shift as a
  plain paragraph break with NO separator glyph (the rule image is not a figure),
  matching ch01-ch21. If visible scene breaks are ever wanted, that is a global
  change across all chapters at once, not a per-batch call.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. The cast/terms decided across
  ch01-ch21 that MUST be reused verbatim include: Zhang Xiaojing (张大头 = Zhang
  Big-Head, 大头 = Big-Head as Xiao Gui hails him), Li Bi (Changyuan) / Deputy
  Director Li / Academician Li (待诏翰林), Director He / He Zhizhang (holder of the
  靖安令), Yao Runeng, Cui Qi (Commander Cui), Cao Poyan, Xu Bin (Youde) / Recorder
  Xu, Tanqi, Wen Ran, Wen Wuji, the Wen Incense Shop, Li Heng (heir apparent) / the
  Eastern Palace, Li Linfu (李相 = the Right Minister), Long Bo (= 萧规 Xiao Gui,
  revealed ch15), the Son of Heaven / Li Longji (Xuanzong; 朕 = "Us/We"), Prince
  Yong / Li Lin, Taizhen (太真 = Yang Yuhuan 杨玉环), the Lady Guo (郭氏), the Eighth
  Company death-roll, the named Pifu (伍归一/Wu Guiyi, 莫洼儿/Mo Wa'er, 索法惠/Suo
  Fahui), Old Ge, the Great Sabao, Tong'er, Wang Yunxiu, Ma Ge'er, Xiao Yi, Wang
  Zhongsi, Feng Dalun, Yuan Zai (元评事 = Evaluator Yuan), Jia Shiqi, Gan Shoucheng
  / General Gan, Adjutant Zhao / Zhao Qilang, Cen Shen, the Right Shad, Ozmish
  Khagan, Ashina, Yisi, Alopen, Mishihe, Registrar Pang, Puzhe, Ji Wen (Deputy
  Director / Vice-Duan / Censor Ji), the cruel-official cluster (Lai Junchen, Zhou
  Xing, Zhou Lizhen, Huan Yanfan, Wu Sansi, Hao Xiangxian), Liu Shiqi, Mojialuo,
  Yuchang, Peroz, Old Zhao, Guan Zhong, Lao Dan / Laozi, Li the Swallow, Zhang Luo
  (Recorder Zhang), Consort Wei (韦氏), Chao Fen, Chao Heng (= Abe no Nakamaro), Mao
  Shun (Director Mao), Mao Poluo, Xu Hezi, Prince Shou (寿王) / Li Mao (李瑁), Empress
  Dowager Dou, Cao Gui, Emperor Yang of Sui, Xiao Gui (萧规), Gai Jiayun / Protector
  Gai, Zhao Xiao, Zhao Li, Duke Li of Wei (= Li Jing), the Sage Confucius, Chen
  Xuanli / Grand General / General Chen, An Lushan / Commissioner An of Pinglu,
  Jieli Khagan, Empress Wei (韦后), Princess Taiping, Ji Xu, Xue Yi, AND the new
  ch21 cast: 轧荦山/Yaluoshan (= An Lushan's childhood name, the war-god idol),
  贞顺武皇后/Empress Wu Zhenshun (= 武惠妃/Consort Wu), 李瑛/Li Ying (the deposed heir
  apparent), 高祖/Emperor Gaozu (with 太宗/Emperor Taizong, 高宗/Emperor Gaozong
  already decided). Orgs: the Jing'an Bureau, the Lüben Guards, the Jinwu Guard, the
  Longwu Army, the Right/Left Xiao Guard, the Qianniu Guard, the Yulin Army, the
  Gate Guards, the Wanqi, the Right Awesome Guard, the Court of Judicial Review, the
  Censorate, the Ministry of Justice/Works/War/Revenue, the Forestry and Crafts
  Bureau, the Palace Domestic Service, the Jingzhao Prefecture, the Stores Section,
  the Secretariat / the Phoenix Pavilion, the Bureau of Sacrifices, the
  Shouzhuolang, the Eighth Company, the Assault-Resisting Garrison, the Pear Garden,
  the entertainers' quarter, the imperial guards (禁军), the Türk Wolf Guards, the
  Protectorate of the Western Regions. Places: Chang'an, Wannian/Chang'an County,
  the Vermilion Bird Avenue (朱雀大街/朱雀街), the West/East Markets, the many wards
  (Pingkang, Jinggong, Dunyi, Anye 安业坊, Guangde 光德坊, Changming, Daozheng, Anyi,
  Xinchang, Shengdao, Shengping, Xiuxing, Guangde, Yanshou, Xuanyang, Yongle,
  Changxing, Anren, Zhiye, Xuanping, and the two Changle wards), the Xingqing Palace
  + the Qinzheng Wuben Tower (whose third floor is the 邀风堂/邀风阁 Wind-Wooing Hall
  and seventh floor the 摘星殿/Star-Plucking Hall) + the Longchi + the Chenxiang
  Pavilion + the Taishang Xuanyuan Lantern-Tower + the Self-Raining Pavilion, the
  Daming Palace + the Taiji Hall (太极殿) + the Yong'an Palace (永安宫), the
  Chengtian/Zhuque Gates, the Yanxing/Wangxian (望仙门)/Tonghua (通化门) Gates, the
  Guanyin temple, the Leyou Plateau, the Huaqing Pool, the Zhongnan Mountains, the
  beacon-fort, the Protectorate of Anxi, Yanzhou, Tianzhu, Kucha, Persia, the Arab
  lands, Izumo/Japan, Balhuan, Hejian, Jincheng, Henan County, Qujiang (曲江) / the
  Qujiang Pool (曲江池), Jiling (疾陵城), Longxi (陇西), the Anye Ward Temple of
  Empress Wu Zhenshun (贞顺武皇后庙). Terms: shichen, watchtower / great watchtower,
  constable, post-soldier, squad leader, buliang chief/men, county commandant, Türk,
  Türgesh, the Sage, His/Your Majesty (陛下), Your Highness, the Lantern Festival,
  the lantern-floats / lantern-float red tally, the Xi cart, barrier-knife, modao,
  pocket/hand crossbow, smoke pellet, the art of the Great Archive, rock-oil,
  fierce-fire / fierce-fire thunder / fierce-fire oil, green-vitriol oil, the Que-le
  Huo-duo, the Tianshu, the qilin-arm, the crown-loft, the lantern-tower, the suanni,
  the finger-snap, the Hutuo dance, the Tanglong / Xiantian coups, the tongtian
  crown, the diexie belt, Guanyin, the Eight Methods of the house of Lai / All
  Streams Return to the Source, the chiwen, "Zhang the Yama" / the Five Yamas, AND
  the new ch21 terms: the walled corridor (夹城) / elevated corridor (复道) /
  passing-bay (跸口), the lowering-frame (缒架), signal-flag (号旗), silk stole (披帛)
  / false drape (假披), hand-declaration (手实) / concealed holding (隐寄), the Edict
  of Grace on the Bestowal of Residences (授宅推恩令), the ivory-handled folding knife
  (象牙柄折刀), wall-officer (城上郎), the seven-fragrance carriage (七香车).
- Titles/address: 太子/东宫 = "heir apparent" / "the Eastern Palace"; 太子妃 =
  "Consort Wei"; 司丞 (Li Bi, Ji Wen) = "Deputy Director"; 靖安令 = "the Director of
  the Jing'an Bureau"; 贺监 = "Director He"; 都尉 (Zhang) = "Commander"; 节度使 =
  "military commissioner"; 殿下 = "Your Highness"; 陛下 = "His/Your Majesty"; 圣人/
  圣上 = "the Sage"; 郎君 = "young master"; 朕 = "Us/We/Our". OFFICE-TITLE renderings:
  主事 = "recorder" (徐主事 = "Recorder Xu"); 录事 = "registrar"; 评事 = "Evaluator";
  参军 = "adjutant"; 校尉 = "commandant"; 县尉 = "county commandant"; 将军 = "General";
  大将军 = "Grand General"; 员外郎 = "vice-director"; 执事 = "deacon"; 大主教 =
  "archbishop"; 长老 = "elder"; 队正 = "squad leader"; 永王 = "Prince Yong"; 寿王 =
  "Prince Shou"; 尚灯监 = "Director of Lanterns"; 都护 = "Protector"; 待诏翰林 =
  "Academician-in-Waiting of the Hanlin"; 李相/右相 = "the Right Minister" (Li Linfu);
  emperors by temple name (高祖/太宗/高宗 = Emperor Gaozu/Taizong/Gaozong). Offices
  per Hucker (see glossary).
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name, an idiom, a round number spelled out analytically,
  an "all-directions" 四X idiom incl. 四下/四外/四海/四周/四处, a color idiom, a
  swear-word, a myriad-idiom, a 千古-type, an organ idiom, a ranking-name, a list
  enumerator, a probability idiom, a classifier, a cn_to_int mis-compound, a
  character-COUNT like 三个字/四个字, a UNIT-NAME numeral like 千牛卫/万骑/六合靴/
  七香车, an idiom like 千恩万谢/接二连三/漏洞百出/智计百出/百感交集, a 两-idiom like
  首鼠两端/两不相欠/两情相悦/判若两人, a 十X intensifier like 十足, a torture-name),
  extend noise.txt (own-line comments) or WORD_NUM, and say so in PROGRESS. ORDERING
  is load-bearing: a new strip pattern must precede any shorter built-in/earlier
  entry that would eat part of it first — AND watch the REVERSE trap B19 hit: a
  pre-existing entry (e.g. 四肢) can strip first and orphan the 百 in 四肢百骸, so
  noise the residual (百骸). If a flag is a REAL quantity, fix the ENGLISH to carry
  the value instead of noising it (ch10 近百 → "fully a hundred"; ch14 数以百计 → "a
  hundred and more"; ch18 一百五十尺 → the DIGIT "150 chi"; ch20 百万百姓 → "a million
  commonfolk", 三百人/一千人/一万人不到; ch21 三载→"third year", 十五日→"fifteenth day",
  开元二十五年→"twenty-fifth year of Kaiyuan" [needs WORD_NUM "twenty-fifth":25],
  开元十六年/十六里→"sixteenth"/"sixteen", 三百下→"three hundred times", 五十步→"fifty
  paces", 二百步→"two hundred paces", 三十多→"thirty-odd", 六进→"six courtyards",
  行百里者半九十→"a hundred-li … ninety li" carried AND footnoted, 七香车→
  "seven-fragrance carriage" [glossary form self-carries "seven"], 三步并作两步→"two
  strides for three" [self-carries 3 and 2], 四目相对→"four eyes meeting"
  [self-carries 4]). A genuinely dropped number must still fail. WATCH the checker's
  English parser: it reads cardinals and a FEW ordinals (fifth/…/tenth,
  thirteenth/fourteenth/fifteenth/sixteenth/seventeenth/twentieth/twenty-fifth) but
  NOT "eleventh"/"eighteenth", NOT the other compound ordinals unless you ADD them
  to WORD_NUM (B21 added "twenty-fifth":25), and it CANNOT build "150" from "a
  hundred and fifty" — but it CAN match "a hundred"/"a thousand"/"a million" via its
  article rules. When a name's numeral must be stripped only in ONE context (ch11
  十七违背 = "Shiqi"), noise the context-specific string. Extra-noise entries run
  BEFORE the built-in NOISE list.
- 二楼/二层 rendered with an English number-word so its numeral survives ("the
  second floor", "two-story"); 第三层 = "the third floor" (third=3); for approximate
  "ten-odd" (十余/十几/十来) render "ten-odd" (keeps 10), not "a dozen or so" (loses
  it). 尺 = "chi", 里 = "li", 丈 = "zhang", 抱 = "arm-span", 分 = "fen", 弹指 =
  "finger-snap(s)", 刻 = "mark".

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. B06-B21 were each started on
  a stray per-batch branch and all work was consolidated onto
  claude/the-longest-day-in-changan, the remote's canonical branch. B21
  specifically: the session opened on claude/the-longest-day-in-changan-z1vkdg,
  whose HEAD equaled origin/claude/the-longest-day-in-changan; the canonical branch
  was checked out, reset to origin, the work done there, committed and pushed.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships (and is not committed). Note anchors must be
  verbatim English substrings or the build refuses; make the anchor unique. XHTML
  note bodies: literal CJK is fine, numeric character references for typographic
  punctuation and accented Latin (&#8212; &#8216; &#8217; &#252; &#160; ...), never
  HTML named entities. The builder inserts note anchors BEFORE markup substitution.
- When editing the JSON ledgers, use a Python load/modify/dump (ensure_ascii=False,
  indent=2 for glossary.json AND notes.json) rather than hand-editing braces; then
  json.load to verify.
- A repeatable way to build the bilingual with GUARANTEED verbatim quotation: write
  a small generator that reads the source lines from data/src, pairs each with your
  hand-authored English, and emits the '>'/English pairs (merging any extractor-split
  halves). Then assert the concatenation of all '>' lines equals the source content
  char-for-char before running the checks (B16-B21 did this; B21 =
  scripts/gen_ch21_bilingual.py, 14,710 chars incl. gloss, 229 body paragraphs).
- Extractor artifacts: a logical paragraph is sometimes split across two (or three)
  lines in data/src (no sentence-ending punctuation on the first). Merge such
  halves into one bilingual pair (ch07-ch21 merged the dateline's split halves; some
  opening vignettes were THREE lines; ch18 had ONLY the dateline split; ch19/ch20
  each had TWO splits; ch21 had ONLY the dateline split — 天宝三载元月十五日，卯正 /
  。 — the two vignette lines L2/L3 each being already terminal). A quick way to find
  them: scan for source lines whose last char is not in 。！？"）…— nor a colon — BUT
  lines ending in the full-width close-quote " are already terminal dialogue, not
  split (skip them), and the content-marker heading (line 1) and any trailing U+200B
  line are not paragraphs. Multi-paragraph quotations stay separate.
- Cite by chapter, never by page.
- Dating: the source advances the day at the Rat hour — ch13 (亥正) is 元月十四日,
  ch14 (子初) through ch21 (卯正) are 元月十五日 (Tianbao 3 = 744 CE). ch21's dateline
  is 天宝三载元月十五日，卯正 (present day, 6 a.m.); no flashback this chapter (contrast
  ch15's 开元二十三年 beacon-fort flashback and ch20's 天宝二载十月七日 polo-ground
  flashback). Render whatever the source's dateline says, and when a per-chapter
  time-gloss is attached to a flashback dateline (as ch20's was), it describes THAT
  hour, not the chapter's nominal hour — flag, don't "correct."
- The source sometimes uses 中元 ("Ghost Festival") where it means 上元 ("Lantern
  Festival"); translate the intent. (BUT ch06's 盂兰盆节 river-lanterns is a genuine
  Ghost-Festival reference; render it faithfully.)
- Watch for authorial slips (ch03 祆正-for-Sabao and a tutor date; ch04 麻格心 for
  麻格儿; ch05 doubled negative; ch06/ch07 time-gloss 日铺 for 日晡; ch07 五桶 where
  the math needs 十五桶; ch08 time-gloss 17是至19时; ch09 line 271 远怀坊 for 怀远坊;
  ch10 AND ch11 the time-gloss is MISMATCHED; ch13 春名门 for 春明门, recurs ch16;
  ch17 临行通道 reads as a variant/slip for 临时). Render the intent for a mis-named
  established referent; render genuine source errors faithfully and visibly (rule 4)
  and flag them in PROGRESS. NOTE: ch12-ch21's time-glosses are internally CORRECT
  (ch20's describes its FLASHBACK dateline 午正, not its nominal hour 卯初; ch21's
  MATCHES its nominal hour 卯正 — neither is an error); do not assume every hour-note
  is broken. SOURCE VARIANT: ch21 writes the third-floor hall as 邀风阁 (阁) where
  ch19/ch20 wrote 邀风堂 (堂) — same referent, rendered "the Wind-Wooing Hall"
  (glossary carries a 邀风阁 cross-ref row); not "corrected" in the quotation.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files. Already-noted
  or already-appeared-and-passed subjects to NOT re-note include: He Zhizhang, Yuan
  Zai, Prince Yong, Ozmish Khagan, the Right Shad, Sun Simiao, the Right Xiao Guard,
  the Censorate, Cen Shen, the Pifu, the xiezhi, the Sogdian Whirl, Lai Junchen, Ji
  Wen, the Shouzhuolang, the Self-Raining Pavilion, A Moonlit Night on the Spring
  River, storax, the Guan Zhong shrine, Yuchang, Peroz, Ksitigarbha, Taizhen (Yang
  Yuhuan), the Rainbow-Feather Dance, the tongtian crown, fire-proof cloth, the
  mercy-release pond, Chao Heng, the Tianshu, Xu Hezi, the Tang Rhymes, Balhuan/the
  beacon-fort, Gai Jiayun, the old charcoal-seller (Bai Juyi's 卖炭翁 — note that
  Bai Juyi's 长恨歌 is separately noted at ch21), 茱萸/the Double Ninth dogwood,
  投名状/the Water Margin blood-pledge, the makara, the ch16 subjects (Chen Xuanli,
  An Lushan, Jieli Khagan / Li Jing), the ch17 subjects (Kuafu, King Tang's net, the
  Longchi), the ch18 subjects (the Xuanwu Gate Incident, the Tanglong/Xiantian coups
  + Empress Wei + Princess Taiping, the two-Changle-wards note), the ch19 subjects
  (the 移春槛 spring-moving frame, the Analects 2.1 pole-star, the Tang Code hostage
  statute), the ch20 subjects (Cao Gui's 肉食者鄙, 君辱臣死, the 鸱吻/chiwen), the
  ch21 subjects (the 长恨歌 couplet 比翼鸟/连理枝 + the Bai Juyi anachronism, 轧荦山/
  Yaluoshan = An Lushan's childhood name, 行百里者半九十 from the 战国策), and
  everything in notes.json ch01-ch21. Xinfeng wine (ch15), the jie-drum (ch06/ch10),
  the suanni (ch18), Emperor Yang of Sui (ch20) already appeared; do not note them.
