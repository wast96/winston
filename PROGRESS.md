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

## B03 = Chapters 8 to 10 (ch08 to ch10) — DONE

Translated end to end: ch08 (5,714 chars, 170 paras), ch09 (4,701 chars, 120
paras), ch10 (4,779 chars, 129 paras); ~15,194 source chars, 419 paragraphs.
Authoring flow as B02: out/<id>_en.txt (one English paragraph per source
paragraph), then scripts/make_bilingual.py (verbatim `>` source lines), then
split_bilingual.py for the reading text and parity source. Story: Ronghua
revealed as a CCP Special Branch liaison (codename Floating Dust), who saves the
wounded courier Lao Yu with an emergency operation performed by A-Chu (who is
mistaken, in Lao Yu's delirium, for Yang Muci); the Yang birthday ball, where
A-Chu is taken for the absent Yang son and strays into the shrine of the "dead"
infant Yang Muchu and meets the black-clad Madam Yang (Yingzi); the drunken Tang
Shaoli's scene and A-Chu's exit; the lost crystal shoe that Yingzi carries to
Yang Yubo along with A-Chu's card; and He Yashu's jade-bracelet gambit at the
Tongji Hospital, undone when Rong Sheng produces the bracelet at the French Park.

Checks run and what they found:
- Check 1, faithful verbatim quotation: each parity source (data/zh/<id>.txt)
  diffed line-for-line against the raw source paragraphs. ZERO content diffs on
  all three units (170/120/129 paras); only diff is the source files' missing
  final newline. Every source paragraph quoted verbatim, none dropped or merged.
- Check 4a, check_numbers.py --noise data/noise.txt: 0 unresolved on all three
  units (and re-verified 0 on all eight ch00–ch07 units after the tooling fix
  below).
- Check 4b, check_structure.py --pairs: paragraph parity OK on all three
  (170/120/129 source = translation).
- Check 2, blind double translation: six argumentative/lyrical passages
  re-rendered blind in a separate context and diffed, First Madam's flower/grass
  metaphor (ch08), Tang Shaoli's monologue on desire and A-Chu's "upstart" retort
  (ch09), Yang Yubo's confession of guilt (ch09), the "seed of love" lyric and
  A-Chu's "solitary sage / cut the flower of one heart" speech (ch10). No
  substantive divergence on any; the independent pass independently confirmed
  同心 = the 同心结 love-knot behind the ch10 title.
- Check 3, round-trip back-translation: ch08's exposition of Ronghua's cover
  (中共特科联络员…上海与延安…书店…联络站) back-translated and checked clause by
  clause; every element recovered, no omissions.
- Check 7, scholarship (corroborated / uncorroborated / contradicted):
  * ch08 title 前度杨郎今又来 = Liu Yuxi, 再游玄都观 (前度刘郎今又来), CORROBORATED;
    杨 substituted for 刘. Footnoted.
  * ch08 狸猫换太子 = the Song "leopard-cat for the crown prince" tale (三侠五义 /
    opera; Emperor Renzong), legend, not history; footnoted as such.
  * ch09 title 开门人即闭门人 = the Chan reincarnation verse attached to Wang
    Yangming (开门犹是闭门人), folk legend, footnoted as such.
  * ch09 怡红公子 = Jia Baoyu's sobriquet in 红楼梦, CORROBORATED. Footnoted.
  * ch09 爱新觉罗改姓金 (Aisin = "gold" in Manchu → Han surname Jin after 1911) , 
    CORROBORATED. Footnoted.
  * ch10 title 误剪同心一片花, NOT a traceable single quotation; built from the
    同心结/同心花 love-knot imagery (cf. Li He, 苏小小墓). Rendered literally,
    footnoted honestly as such.
  * ch10 乍暖还寒，最难将息 = Li Qingzhao, 声声慢, CORROBORATED. Footnoted.
  * ch10 the Duke of Windsor = Edward VIII, 1936 abdication, CORROBORATED; the
    "Windsor knot" is named for him but by most accounts he never tied one
    (thick-lined four-in-hand), noted in the footnote.
- Check 8, random-sample paranoid audit: the six double-translated passages plus
  the ch08 back-translation cover ~4% of the batch (≈16 of 419 paragraphs, the
  densest argumentative/lyrical material). Observed substantive error rate: 0.

Footnotes: 9 added (notes #24–#32 in reading order), 3 per chapter, the three
chapter-title couplets plus, per chapter, one allusion or reference a
non-specialist would miss (狸猫换太子 and 灯下黑 for ch08; 怡红公子 and 爱新觉罗→金
for ch09; 乍暖还寒 Li Qingzhao and the Duke of Windsor for ch10). Every anchor
verified as a unique verbatim substring of the English prose before building;
XHTML bodies use numeric character references only; hanzi written literally.

Glossary: 24 new rows, one decided rendering per referent. People: Yang Sitong,
Tang Shaoqi, Tang Shaoli, Madam Yang, Yingzi, Yang Muchu, A-Ci, Hong'er, Yun'er,
the He family, the Tang family. Organizations: the Financial News, the Shanghai
Garrison Command. Places: Yan'an, Yuyuan Road, the Ciyun Temple, Xianghe Lane,
the French Park, the Zuiju Waterside Pavilion. Terms: Floating Dust (浮尘
codename), Longjing, the Qingming Festival, the Duke of Windsor, heart-knit knot
(同心结). Ronghua's existing row updated to record her revealed Special Branch
role. Recurring cast reused unchanged (Ronghua, Rong Sheng, A-Chu, Lao Yu, Yang
Muci, Jiang Lishui, He Yashan, He Yashu, Xing'er, Chan'er, A-Fu, Fourth/First/
Third Madam, Tongji Hospital, Huamei Bookstore, Special Branch).

Figures: none in this batch.

Tooling fix made this batch (generic, recorded per CLAUDE.md):
- scripts/check_numbers.py: gave the 一点/一點 ("a little") noise patterns the same
  digit-and-十 lookbehind the clock-minute patterns already use, so clock hours
  like 十一点/十二点 (11/12 o'clock) keep their 一 instead of the generic 一点 eating
  it and orphaning a bare 十 read as the quantity 10. (Two patterns touched:
  the `[一不][旦時时般點点些]` set and the `一[...點点]` set; 點点 pulled out into a
  guarded pattern.) Re-verified 0 unresolved on all eight ch00–ch07 units.
- data/noise.txt additions (non-quantity numerals flagged and confirmed): 万丈 /
  萬丈 (万丈深潭 "bottomless abyss"), 五、六十 (source's abbreviation of 五十、六十
  "fifty or sixty [square meters]", where the bare 五 stands for 50).

Flagged for the read-through:
- ch09 title (开门人即闭门人) and ch10 title (误剪同心一片花): the former is a Chan
  reincarnation verse (Wang Yangming legend), the latter not a traceable
  quotation but classical love-knot imagery; both footnoted, rendered literally.
- ch10 袅娜多情春尽 (the "idle line" Rong Sheng half-recalls): the source itself
  labels it 无聊句子, so it is rendered literally without a scholarly note.
- Source's own inconsistencies kept as-is: 她的女儿 for Yang Yubo's daughter (他
  intended; rendered "his daughter"); 表哥/表弟/表姐 for the same cousin pair
  (rendered "Cousin" throughout to avoid a false elder/younger distinction).

Build: out/On a Hair Trigger.epub rebuilt, 11 of 36 units translated, 32 notes.
qa_epub.py PASS (36 documents, 1504 paragraphs, 32 references = 32 bodies = 32
backlinks, all links resolve).

## B04 = Chapters 11 to 13 (ch11 to ch13) — DONE

Scope: ch11 (第十一章　平生际遇似萍飘, 7068 chars, 190 paras), ch12 (第十二章　何日
归家洗客袍, 6880 chars, 204 paras), ch13 (第十三章　琵琶声泣血泪仇, 5037 chars, 118
paras). ~18,985 source chars, 512 paragraphs total. This is the batch where the
central secret breaks: the fortune-oracle at the Ciyun Temple, Yang Yubo's visit
to A-Chu's clinic, the tanci at the Dongfang storytelling house, and Fourth
Madam's confession revealing A-Chu as Yang Muchu and herself as Yang Mulian.

Authoring flow (per CLAUDE.md): wrote out/<id>_en.txt one English paragraph per
source paragraph, ran scripts/make_bilingual.py (verbatim `>` source lines) then
scripts/split_bilingual.py. ch12 carries a mid-sentence source paragraph split
(the 梨花落 aria, source lines 136/137, ending "纸儿、笔" / "儿、墨儿…"); the English
was split at the matching point to keep parity, so both halves render as their
own paragraph. No pirate-site watermark line in any of the three sources (the
"阳光" hit in ch11 is the prose 你很阳光我很阴暗, not advertising).

Checks run and results:
- check_numbers.py --noise data/noise.txt: 0 unresolved on all three units
  (ch11 190, ch12 204, ch13 118 pairs) after the additions below.
- check_structure.py --pairs: parity OK on all three (190/204/118 both sides).
- Verbatim fidelity: diff of data/zh/<id>.txt (minus its ### title line) against
  the source paragraphs (data/src minus 2 metadata lines) is IDENTICAL, 0 content
  diffs, on all three units.
- Blind double translation (separate context) of the lyrical/argumentative
  passages: the ch11 oracle quatrain and Rong Sheng's break-off speech, the ch12
  tanci opening antiphon, and Fourth Madam's ch13 pipa lament. The independent
  renderings agreed in sense; the only divergences were stylistic (1st- vs
  3rd-person in the pronoun-less oracle poem) and one the blind pass got wrong
  that ours got right (it romanized 杨羽柏 as "Yang Yubai"; ours keeps the glossary
  form Yang Yubo).
- Round-trip back-translation (English to Chinese, fresh context) of four prose
  passages from ch12–ch13 (the red-capped-merchant origin, Fourth Madam's "all
  the truth" speech, the impersonation, the bribe-and-integrity exchange): every
  element survived; no omissions detected.
- Paranoid audit: the ~15 paragraphs above given full treatment (verbatim-quote
  diff, double translation, back-translation) ≈ 3% of the batch; observed
  residual error rate 0. The one genuine mistranslation found in the whole batch
  (ch12 pair 50, 二小姐 rendered "sir" instead of "second young lady") was caught
  by check_numbers [2] and fixed before build.

data/noise.txt additions (non-quantity numerals flagged and confirmed): 万变
(以不变应万变), 五彩缤纷, 四手 (双拳难抵四手), 大千 (大千世界), 感激涕零 (涕零→0),
万千 (感慨万千), 三轮 (三轮摩托车, vehicle name), 万家灯火 (restaurant name), 万种
(万种妖娆), 千百 (千百次), 万般 (万般无奈), 三更 (半夜三更). No checker code change
this batch. 小三弦 rendered "three-stringed sanxian" so the 三 is credited rather
than noised (matches ch12's "little three-stringed sanxian").

Notes: 10 footnotes, #33 to #42.
- ch11 (4): title 平生际遇似萍飘 = opening line of the in-novel oracle quatrain
  (duckweed topos, cf. Wen Tianxiang 过零丁洋; not a single-poem quotation);
  灋/廌 the xiezhi and the Shuowen gloss of the law-graph (corroborated); Pushkin's
  1829 lyric "Whether I Wander Along Noisy Streets" (corroborated); Su Shi 题西林壁
  "the true face of Mount Lu" (variant 只因 for 只缘; corroborated).
- ch12 (3): title 何日归家洗客袍 = direct line from Jiang Jie 一剪梅·舟过吴江
  (corroborated); the 梨花落 aria = Jiao Guiying's ghost-lament from 情探 (王魁负桂英),
  which is why A-Chu calls it "ghost-talk"; the Third Communist International /
  Comintern (corroborated).
- ch13 (3): title 琵琶声泣血泪仇 = allusion to Bai Juyi 琵琶行 (pipa-as-lament, not a
  direct quotation); Ximen Qing and Pan Jinlian (水浒/金瓶梅, fiction); the
  "red-capped merchant" (红顶商人, cf. Hu Xueyan; corroborated).
Every anchor verified as a unique verbatim substring of the English prose with
grep -c before building; XHTML bodies use numeric character references only,
hanzi written literally.

Glossary: 15 new rows, one decided rendering per referent. People: Yang Mulian
(Fourth Madam's true name), Yang Yuhua (the murderous uncle), Xu Yuzhen (the
concubine), Han Zhengqi (Yang Mulian's lover), A-Yue (the wet-nurse).
Organizations: the Golden Dragon Society, the Third Communist International, the
Grand Theatre, the Myriad Lamplights. Places: the Dongfang Hotel, the Dongfang
storytelling house, Jinling. Terms: pingtan, pipa, sanxian. 东方饭店 is rendered
by pinyin ("Dongfang Hotel", provisional) rather than as any named Republican
hotel: it does not map cleanly onto the Metropole (新城饭店), the Great Eastern
(大东旅社) or the East Asia (东亚旅馆), so a specific English hotel name would be a
false real-world claim. Recurring cast reused unchanged (A-Chu, Rong Sheng,
Ronghua, Fourth Madam, He Yashu, Lao Yu, Han Yu, Cong Feng, Cong Hui, Xia
Yuechun, Jiang Lishui, A-Fu, Yang Yubo, Yang Muci, Yang Muchu, A-Ci, Hong'er,
Xing'er, Chan'er, the Tongji Hospital, the Special Branch). Jiao Guiying,
Ximen Qing, Pan Jinlian, Hu Xueyan handled in notes, not the glossary (as with
the Dream of the Red Chamber figures in earlier batches).

Figures: none in this batch.

Flagged for the read-through:
- The novel's own naming: 荣初 (Rong Chu) is now shown in person as Fourth Madam's
  actual son, a tanci performer, used to lure A-Chu; the glossary row is unchanged
  (same referent). A-Chu's real name 杨慕初 (Yang Muchu) pairs with 杨慕次 (Yang
  Muci) and echoes 荣初/阿初, the book's central doubling.
- 杨羽柏 "Yang Yubo" now names two men: the murdered father, and the uncle Yang
  Yuhua living under the dead man's name (the "Yang Yubo" of A-Chu's clinic). The
  source uses the one name for both; the translation keeps that, since the
  collision is the point (A-Chu's shock at the spirit-tablet).
- Pope's "To err is human, to forgive divine" (ch11): the source gives Pope's
  English line run together, then a Chinese gloss of it; rendered as the quotation
  plus the inline attribution "a line from the poet Pope" (the Chinese gloss is
  Pope's own line restated, so re-translating it into English would be redundant).
- 灋 caption line (ch11 source line 155, "灋古体的'法'字"): rendered as a standalone
  gloss line keeping both glyphs, "灋—the ancient form of the character 法, 'law.'"

Build: out/On a Hair Trigger.epub rebuilt, 14 of 36 units translated, 42 notes.
qa_epub.py PASS (36 documents, 2013 paragraphs, 42 references = 42 bodies = 42
backlinks, all links resolve).

## B05 = Chapters 14 to 15 (ch14 to ch15) — DONE

Scope: ch14 (第十四章　去时血漫桃源路, 10786 chars, 260 paras), ch15 (第十五章　到底方
知出处高, 9241 chars, 254 paras). ~20,027 source chars, 514 paragraphs total. This is
the batch that turns the hinge of the whole book: A-Chu refuses the Fourth Madam's
demand for blood and resolves to leave for Paris; the hospital bombing kills the
Fourth Madam, Rongrong and the young nurse; A-Chu swears the blood oath and is
reborn as the new chief of the Golden Dragon Society; then the funeral, Third
Madam's collapse, Rong Chu's vigil, and the long confrontation with Han Zhengqi
(whose account of the past contradicts the Fourth Madam's), closing on the paired
waterfall poems on the two fans.

Authoring flow (per CLAUDE.md): wrote out/<id>_en.txt one English paragraph per
source paragraph, ran scripts/make_bilingual.py (verbatim `>` source lines) then
scripts/split_bilingual.py. ch14 carries a mid-sentence source paragraph split
(source lines 137/138, "阿初低着头，" then the reflective sentence beneath); the
English is split at the matching point (ending "A-Chu bowed his head —") so both
halves render as their own paragraph and parity holds. ch15 carries the recurring
梨花落 aria across a mid-word source split (source lines 92/93, ending "纸儿、笔" /
"儿、墨儿…"), split in English at "Paper, brush," / "ink and inkstone…"; the aria's
wording was aligned to its Chapter 12 rendering (it is the same lyric). No
pirate-site watermark line in either source.

Checks run and results:
- check_numbers.py --noise data/noise.txt: 0 unresolved on both units (ch14 260,
  ch15 254 pairs) after the noise additions below. Clock times rendered so digits
  survive ("three in the dead of night" 三点, "five in the small hours" 五点,
  "four o'clock" 四点, "ten in the morning" 十点). Poem numerals kept literal
  (thousand crags / ten thousand ravines 千岩万壑; a thousand fathoms 一落千丈).
- check_structure.py --pairs: parity OK on both (260/260, 254/254).
- Verbatim fidelity: diff of data/zh/<id>.txt (minus its ### title line) against
  the source paragraphs (data/src minus 2 metadata lines) is IDENTICAL, 0 content
  diffs, on both units.
- Blind double translation (separate context) of five argumentative/lyrical
  passages: the ch14 duckweed-and-lotus monologue, the ch14 rebirth coda, the
  ch15 gambler metaphor, and both waterfall poems. The independent renderings
  agreed in sense with the shipped text on all five; no divergence beyond word
  choice, which confirms the source is not ambiguous at those points.
- Round-trip back-translation (fresh context) of four passages (duckweed
  monologue, Fourth Madam's rebuke, the tanci lyric, Han Zhengqi's three-roads
  speech): no clauses dropped; every phrase, name and number reappeared.
- Paranoid audit (~4%, 20 paragraphs spread across both chapters, full
  verbatim-quote + meaning check): 20 pairs audited. One substantive finding,
  fixed: ch14 para 20, 她要自己亲手除去这一对狗男女 — the reflexive 自己 is grammatically
  bound to the Fourth Madam ("her own hand"), yet the plot requires A-Chu's hand;
  reworded to "wiped out by his very hand" and the ambiguity footnoted rather than
  smoothed. 切齿之恨 re-rendered "a hatred that made her grind her teeth" (the earlier
  "set her teeth on edge" read as mere irritation). One minor, kept: ch14 para 218
  "Her pulse is very weak" supplies an implied possessive English dialogue wants.
  Observed residual error rate after fixes: 0.

Noise additions (data/noise.txt), all non-quantity numerals: 凋零 (家业凋零, 零→0),
飘零 (涕泪飘零, 零→0), 万难 (排除万难), 王老五 (钻石王老五, bachelor slang 五), 一来二去,
三分薄面 (三分 = "a bit"), 四平八稳, 礼让三分 (三分 = "a measure"). No checker code
change this batch. 百感交集 handled by rendering "a hundred feelings" so 100 is
credited rather than noised.

Notes: 7 footnotes, #43 to #49 (numbered by the builder in reading order).
- ch14 (4): title 去时血漫桃源路 = Tao Yuanming 桃花源记 turned bloody (corroborated,
  inversion the novelist's own); Mencius 独善其身/兼善天下 (corroborated); 割股疗亲 the
  filial-thigh motif behind 割股之心 (corroborated as a traditional motif); the 自己
  ambiguity at para 20 (flagged, not smoothed).
- ch15 (3): title 到底方知出处高 = second line of A-Chu's reply poem, reworking the
  Tang 瀑布联句 (Li Chen / a Chan monk; the source's Xiangyan ascription noted
  against the commoner Huangbo attribution; distinguished from Du Xunhe 小松 at
  Chapter 5); the second 情探 (王魁负桂英) lyric cross-referenced to the Chapter 12
  note (the singer's self-slain-avenging-ghost fate now literally the Fourth
  Madam's); 三刀六洞 the Jianghu blood-penance A-Chu waives for Han Zhengqi.
The 梨花落 aria itself is NOT re-footnoted (its note is at Chapter 12, first
appearance). Every anchor verified as a unique verbatim substring of the English
prose with grep before building; XHTML bodies use numeric character references
only, hanzi written literally.

Glossary: 11 new rows, one decided rendering per referent. People: Young Tang
(汤少; source names him inconsistently 汤少礼/汤少棋, kept verbatim), the Chan master
Xiangyan Xian. Organizations: the Shanghai Police Bureau, the Longhua sub-bureau,
the Green and Red Gangs (青红帮), the Ministry of Foreign Affairs. Places: the
Shanghai Bund, Chang'an, Germany. Terms: aunt-mistress (姨奶奶), Xiansheng (先生 as
the society's address for its chief; "Mr." in ordinary use). Recurring cast reused
unchanged (A-Chu / Yang Muchu, the Fourth Madam / Yang Mulian, Rong Chu, Rong
Sheng, Ronghua, Third Madam, First Madam, Han Zhengqi, Han Yu, Xia Yuechun, Tang
Shaoli, He Yashu, Yang Sitong, Yang Yuhua, A-Fu, Hong'er, the Golden Dragon
Society, the Tongji Hospital). The wet-nurse 嬷嬷/岳嬷嬷 rendered "the nurse" / "the
nurse A-Yue" to match the decided 阿岳 = A-Yue.

Figures: none in this batch.

Flagged for the read-through:
- 自己 at ch14 para 20 (above): rendered to the plot-sense "by his very hand" and
  footnoted; the literal grammar would read "her own hand."
- Han Zhengqi's account (ch15) deliberately contradicts the Fourth Madam's ch13
  confession in its details (who saved the children, whether he was captured). The
  translation preserves both versions straight; the novel means the discrepancy
  to stand ("有人在说谎"), so nothing is reconciled.
- 杨羽桦 (Yang Yuhua, the uncle) is the man A-Chu swears to kill in the blood oath;
  杨羽柏 (Yang Yubo) remains the name shared by the dead father and the impostor.

Build: out/On a Hair Trigger.epub rebuilt, 16 of 36 units translated, 49 notes.
qa_epub.py PASS (36 documents, 2525 paragraphs, 49 references = 49 bodies = 49
backlinks, all links resolve).

## B06 = Chapter 16 (ch16) — DONE

Scope: ch16 (第十六章　山回路转又逢君, 11004 chars, 320 paras). The single largest
chapter in the book, and the batch that introduces the spy-school twin as an active
agent: Yang Muci and Xin Lili run their final "live-combat" graduation exercise,
see through Du Luning's nested trap (the seduction-and-kill order in the Hangzhou
hotel), and race the winding mountain road back to graduate; interleaved with
A-Chu's Shanghai household (Young Tang tutoring Rong Chu; the dinner where A-Chu
probes Han Zhengqi over the Japanese Dongyang Company and his son Han Yu; the TNT
lab scene fixing the hospital bombing as military-grade), and closing on Ronghua's
newspaper-signal contact in the French Park and the Milan Cafe, where Muci is
welcomed "home" into the Communist network.

Authoring flow (per CLAUDE.md): wrote out/ch16_en.txt one English paragraph per
source paragraph, ran scripts/make_bilingual.py (320 pairs, verbatim `>` source
lines) then scripts/split_bilingual.py. No mid-sentence source-paragraph split this
chapter; each of the 320 source lines rendered as its own paragraph. No pirate-site
watermark line in the source.

Twin-name slip: the source prints 杨慕次 (Yang Muci) three times where the scene is
plainly his brother 杨慕初 / 阿初 (Yang Muchu / A-Chu) — source lines 70 (garden), 165
and 166 (dinner) — while Muci is away in Hangzhou sitting his exam. The names differ
by one character (次 / 初). Rendered by context (Muchu / A-Chu) and flagged in a
footnote rather than silently reconciled. The narration's 阿次 = A-Ci at line 301 is
NOT a slip: it is Muci's own familiar name, set against 阿初 in the same scene.

Checks run and results:
- check_numbers.py --noise data/noise.txt: 0 unresolved (320 pairs). Clock times
  rendered so digits survive ("two thirty" 两点半, "eleven twenty" 十一点二十分,
  "twenty-four minutes past two" 二点二十四分, "two twenty-five" 二点二十五分, "around
  three o'clock" 三点钟). Dates kept ("November 2nd" 11月2日 — the checker maps the
  month name to 11; "March 20th/25th/26th, 1932"; "the 19th"). Rooms 26 and 15,
  five hundred catties 五百斤, seven or eight hundred million fabi 七、八亿法币,
  two thousand years 2000多年, the Eight-Nation Alliance 八国联军 all survive.
- check_structure.py --pairs data/zh/ch16.txt out/ch16_reading.md: parity OK
  (320/320). Verbatim fidelity: data/zh/ch16.txt (minus its ### title) diffed
  against the source paragraphs (data/src minus 2 metadata lines) = zero content
  diffs (only the source file's missing final newline).
- Blind double translation on the argumentative/lyrical passages (the trap-
  realization at para 138, the golden-triangle economics at para 179, the cliff-
  climb lyric at paras 232/239/240, the god-of-love/god-of-death couplet at para
  240) and round-trip back-translation on those four: no substantive divergence;
  the source is not ambiguous in them, only dense. Paranoid audit ~4% (~13 paras,
  incl. the two long Du Luning reasoning paragraphs at 138/247, the econ speech at
  179, and the newspaper-notice paras 286-289): observed error rate 0 after the
  drafting pass (no dropped clause, no invented sentence).

Noise additions (data/noise.txt), all non-quantity numerals: 四肢 (four-limbs
idiom), 百货 (百货公司 = department store), 危机四伏, 百玩不厌 (百 = "endlessly"),
五体投地, 百川归海, 金三角 (financial figure), 身价百倍 (百倍 idiom), 三硝基甲苯
(trinitrotoluene, the 三 = tri- prefix), and two TNT-patter magnitudes: 十之一 (the
residue of the fraction 十万分之一 after the built-in 万分 rule strips it) and
万个大气压 (the 万 left after 几十 is stripped from 几十万个大气压). No checker code
change this batch.

Notes: 5 footnotes, #50 to #54 (numbered by the builder in reading order).
- #50 the twin-name slip (杨慕次 for 杨慕初 / 阿初), rendered by context and flagged.
- #51 西厢记 (Wang Shifu) — Rong Chu's tanci line 则为他临去秋波那一转，风魔了张解元,
  reworking Zhang Sheng's first-act aria (corroborated).
- #52 the September 18th Incident / Mukden Incident of 1931 and the Three Eastern
  Provinces (corroborated), fixing the chapter after autumn 1931.
- #53 鲁迅 答客诮 — 怜子如何不丈夫, written 31 Dec 1932 in defense of a father's love
  (corroborated); turned cold in A-Chu's mouth as he exploits Han Zhengqi's love
  for Han Yu.
- #54 title couplet 山回路转又逢君, inverting Cen Shen's 白雪歌送武判官归京 close
  山回路转不见君，雪上空留马行处 (corroborated; a poem securely in the Tang canon);
  "I see you no more" becomes "I meet you again," anchored to Ronghua's "Welcome
  home." The chapter-title H2 itself carries no note ref (anchored in the prose).
Every anchor verified as a unique verbatim substring of the English prose with
grep -c before building; XHTML bodies use numeric character references only, hanzi
written literally.

Glossary: new rows, one decided rendering per referent; recurring cast reused
unchanged (Yang Muci, Xin Lili, Yu Xiaojiang, Du Luning, Young Tang, Rong Chu,
Yang Muchu / A-Chu, A-Ci, Xia Yuechun, Han Zhengqi, Han Yu, Ronghua, Rongrong, Lao
Yu; code names Drifting Wind, Timely Rain, Mr. Lin Tan; Xiansheng). Organizations:
the Dongyang Company (东洋公司), the Forest Skating Club, the Shanghai Current Affairs
Daily (英文版《上海时事日报》), the Evening News, the Central Shanghai Garrison Command
(沪中警备司令部, distinct from the Shanghai Garrison Command), the Detective Division
(侦缉处), the White Rose (白玫瑰 ballroom), the Rose Ballroom (玫瑰舞厅). Places: the
Crown Hotel (皇冠酒店), Yufo Temple Road, the Milan Cafe, the Rose Garden (玫瑰园 in
the French Park), Feilai Peak, the Three Eastern Provinces. Terms: show-hand (沙蟹),
fabi (法币), tanci (弹词), trinitrotoluene (三硝基甲苯, TNT).

Figures: none in this batch.

Flagged for the read-through:
- Twin-name slip (above): 杨慕次 printed for 杨慕初 / 阿初 at source lines 70, 165, 166,
  rendered by context and footnoted (#50). 阿次 = A-Ci at line 301 is genuine, not a
  slip.
- fabi (法币): the Nationalist legal-tender note was in fact introduced only in 1935;
  the novel uses the term loosely for the chapter's early-1930s present. Rendered
  straight, glossary note records the anachronism.

Build: out/On a Hair Trigger.epub rebuilt, 17 of 36 units translated, 54 notes.
qa_epub.py PASS (36 documents, 2844 paragraphs, 54 references = 54 bodies = 54
backlinks, all links resolve).

## B07 = Chapters 17 to 18 (ch17 to ch18) — DONE

Scope: Chapter 17 (ch17, src 20_part0018.txt, 251 paragraphs, ~10,592 chars) and
Chapter 18 (ch18, src 21_part0019.txt, 127 paragraphs, ~4,942 chars); 378
paragraphs, ~15,534 source chars. Continues the novel from B06.

Authoring flow (unchanged): wrote out/<id>_en.txt (one English paragraph per
source paragraph), then make_bilingual.py (verbatim `>` source lines), then
split_bilingual.py. No mid-sentence paragraph splits this batch: ch17 line 109
(韩正齐惊惶失措；) ends on a semicolon but is a complete single-clause paragraph
paired with line 110 (徐玉真满脸狐疑。), a parallel couplet rendered 1:1, not a split.
The source carries no notes of its own; every note is the translator's.

Checks run and results:
- check_numbers.py --noise data/noise.txt: ch17 0 unresolved, ch18 0 unresolved.
  New noise.txt rows (all NON-quantity numerals): 贤二 (Doihara Kenji, 土肥原贤二,
  the 二 is a name), 下三烂 (idiom "vile," 三), 万端 (经纬万端 "myriad," 万), 一了百了
  (idiom, 百), 百试百灵 (idiom "never fails," 百), 三元 (name Huang Sanyuan 黄三元, 三),
  千羡万羡 (Lu Yu poem hyperbole, 千/万), 十五、六 (approximate age idiom), 一百八十度
  (一百八十度大转变 = a total about-face, idiom, 180), 阿四 (name Liu A-Si 刘阿四, 四).
  No checker code change. Clock/quantity digits preserved: "Shōwa 4 / 1929,"
  "September 18th Incident," "three provinces," "one and a half times," "three /
  four coffins," "twelve," "fifteen or sixteen," "eighteen-year-old," "a hundred
  and eighty degrees" (noised as idiom), "twenty years" throughout.
- check_structure.py --pairs: ch17 251/251 OK, ch18 127/127 OK.
- Verbatim fidelity: diff of data/zh/<id>.txt (minus its ### title) against the
  source paragraphs (data/src minus 2 metadata lines) = zero content diffs for
  both chapters; only the source files' missing final newline differs (expected).
- Blind double translation (fresh context, 6 argumentative/lyrical passages: the
  warp-and-weft line, the Lu Yu tea poem, the Cao Zhi Seven-Step Poem, the ch18
  "betrayal" definition, the "overnight true→false" deduction, the closing grief
  passage): independent renderings matched mine in meaning throughout; it
  independently identified the two poem sources (六羡歌, 七步诗). No divergence
  requiring change; flagged ambiguities (经纬 = warp/weft vs ordering; 夫人 =
  madam/wife; 不明不白) were already handled consistently.
- Round-trip back-translation (my English → Chinese, 6 passages): no invented
  clause; back-translations tracked the source closely.
- Paranoid audit (13 paragraphs, ~3.4% of the batch, full source-vs-English
  omission/addition/mistranslation check): 1 genuine error found and FIXED — an
  unsupported flourish "to the last farthing" (原原本本 = "in full, exactly," no
  such image); changed to "in full and to the very letter." Also fixed a borderline
  idiom import, "blot out the sky with one hand" (遮天蔽日 has no "one hand"; that
  belongs to 一手遮天) → "blot out the sky and cover the sun." No omissions, no
  name/number/date errors found. Observed error rate in the audited sample: 1
  substantive addition per 13 paragraphs (~7.7%), corrected; extrapolated batch
  rate low, all number/name/date invariants clean by machine check.

Footnotes: 7 new (#55 to #61; running total 61). Every anchor verified as a unique
verbatim substring of the English prose (grep -c = 1) before building; XHTML bodies
use numeric character references only, hanzi written literally.
- #55 ch17 title couplet 各有经纬一片天 — not a traceable classical quotation
  (uncorroborated as a quotation; author's couplet in the old manner), rendered
  literally; explains 经纬 and its recurrence in the chapter. Anchor "warp and weft."
- #56 the September 18th Incident / Mukden Incident, 18 Sept 1931 (corroborated).
  Recurring historical ref; noted at first appearance in this batch (it was already
  footnoted for B06 at #52 in ch16 — this ch17 note is retained because ch17 opens
  the espionage frame in detail; kept concise).
- #57 Doihara Kenji (土肥原贤二, 1883–1948), historical Japanese spymaster, hanged
  1948 (corroborated); the "Liyang Society" (立洋社) and its "Eastern Institute"
  (东洋学馆) on Kunshan Road are NOT attested under those names and appear to be the
  novel's invention (uncorroborated), though they echo real Japanese intelligence
  fronts in Shanghai. Anchor "Doihara Kenji."
- #58 Lu Yu (陆羽, 733–804), Sage of Tea, author of 茶经; the recited lines are his
  六羡歌 (Song of Six Longings), West River / Jingling = his hometown (corroborated).
  Anchor "Lu Yu of the Tang."
- #59 Cao Zhi's 七步诗 (Seven-Step Poem, 192–232), the beans-and-beanstalks fratricide
  lines (corroborated); central to the twins theme. Anchor "we sprang, the two of
  us, from the selfsame root."
- #60 ch17 twin-name slip: source prints 杨慕次 at one point in the tearoom scene
  where the speaker is plainly 杨慕初 / 阿初; rendered by context and flagged (per the
  ch16 precedent, #50). Anchor "ran a deliberately strange, sidelong gaze over her."
- #61 ch18 title couplet 牵丝攀藤一条线 — 牵丝攀藤 is an established idiom (to drag in
  tenuous/far-fetched links, usually pejorative), here turned to A-Chu's method of
  drawing every clue into one thread; not a classical quotation (corroborated only
  as a modern set phrase). Anchor "out of the tangled and disordered threads."

Twin names: 阿初 = A-Chu / Yang Muchu; 慕次 = Muci (A-Ci) appears only in the opening
Huamei Bookstore scene (genuinely Muci meeting Ronghua) — correct, not a slip. The
one ch17 slip (tearoom scene) is #60.

English-in-source: ch17 line 217, Xia Yuechun speaks two English sentences with
parenthetical Chinese glosses and closes on Pope's "To err is human, to forgive
divine." The English dialogue is rendered as English (spacing restored) with a
light ", in English" to keep the code-switch; the parenthetical Chinese glosses are
a reading aid for the source's Chinese readers (a translation OF the English, not
story content), so they are not reproduced. No content dropped. The bilingual `>`
line keeps the full source verbatim. Pope's line is famous in English and left
unannotated.

Glossary: new rows, one decided rendering per referent; existing renderings reused
unchanged (A-Chu/Yang Muchu, Muci/A-Ci, Xu Yuzhen, Han Zhengqi, Han Yu, Yang Mulian,
Rong Chu, Rong Sheng, Fourth Madam, Xia Yuechun, Young Tang, Yang Yuhua, Yang Yubo,
the Golden Dragon Society, the Tongji Hospital, the Special Branch, the Central
Special Committee, the White Rose, the Huamei Bookstore, the Third Communist
International, aunt-mistress). New people: Huang Sanyuan (黄三元), Doihara Kenji
(土肥原贤二, attested), Fang Zhitong (方致同), Liu A-Si (刘阿四), Lu Liangchen (陆良晨),
Sakai Ichirō (酒井一郎), Lu Yu (陆羽, attested). New organizations: the Hongmen (洪门),
the Liyang Society (立洋社, provisional), the Eastern Institute (东洋学馆, provisional),
the Central Special Committee (中央特委), the Special Higher Police (特高科 = Tokkō),
the Army General Staff (参谋本部), the Land Survey Department (陆地测量部), the Chunhe
Hospital (春和医院), the Customs House (海关总署). New places: Kunshan Road (昆山路), the
Park Hotel (国际大饭店), the Huangpu (黄浦江), Shenyang (沈阳), the Central Plains (中原).
New terms: the Imperial Flower (帝国之花), the September 18th Incident (九·一八事变),
Shōwa (昭和), concubine-aunt (姨娘, distinct from 姨奶奶 = aunt-mistress).

Consistency note: 姨奶奶 reused as "aunt-mistress" (glossary), not the "concubine-
mistress" first drafted; 姨娘 = "concubine-aunt" (narration) / "Auntie" (vocative).

Figures: none in this batch.

Flagged for the read-through:
- Twin-name slip #60 (above): rendered by context, footnoted.
- Park Hotel (国际大饭店): opened 1934, slightly after the story's early-1930s present;
  rendered straight, glossary note records the mild anachronism.
- "Liyang Society"/"Eastern Institute" (立洋社/东洋学馆): unattested; footnote #57 says so.

Build: out/On a Hair Trigger.epub rebuilt, 19 of 36 units translated, 61 notes.
qa_epub.py PASS (36 documents, 3220 paragraphs, 61 references = 61 bodies = 61
backlinks, all links resolve).

## B08 = Chapters 19 to 21 (ch19 to ch21) — DONE

Scope: Chapter 19 (ch19, 22_part0020.txt, 6,486 src chars, 241 paragraphs),
Chapter 20 (ch20, 23_part0021.txt, 6,823 chars, 231 paragraphs), Chapter 21
(ch21, 24_part0022.txt, 6,096 chars, 177 paragraphs). 19,405 chars, 649 paragraphs.

Authoring flow (established B02): wrote out/<id>_en.txt (one English paragraph per
source paragraph), then make_bilingual.py (verbatim `>` source), then
split_bilingual.py. No hand-typing of the source.

Checks, per unit:
- check_numbers.py --noise data/noise.txt : 0 unresolved for all three.
  noise.txt additions this batch (all non-quantity numerals/idioms/names):
  八、九十分 (a fuzzy guess-degree, not 8/90), 百乐门 (the Paramount), 四目 (四目相遇
  "their eyes met"), 百无聊赖 (idiom "utterly listless"), 几十万 + 万的输赢 (a built-in
  几十 rule strips 几十 and leaves a stray 万=10000 residue; noise the residue),
  四肢 ("his limbs"), 四周 ("all around"). Also rendered 万里 as "Ten thousand li"
  (couplet, ch20) so the digit survives rather than noising it.
- check_structure.py --pairs : parity OK for all three (241/241, 231/231, 177/177);
  note anchors resolve; heading shape uniform.
- Verbatim fidelity: diffed data/zh/<id>.txt (minus title line) against the source
  paragraphs (minus 2 metadata lines) for each unit — zero content diffs (only the
  source files' missing final newline, as expected).

QC: blind double translation + round-trip back-translation applied to the lyrical
and argumentative passages (Yashu portraits and dance-floor; A-Chu's shame before
Cong Feng; the "five thousand years of culture" speech; the billiards
reconciliation; the fire backstory; the river-boat capture; Ronghua's "to fall is
not the fearful thing"). Paranoid full audit run on ~26 paragraphs (~4%) in a fresh
context: verbatim-quote, back-translation and independent re-translation. Observed
error rate 0% (0 real omissions/additions/mistranslations). One sub-threshold
wording improvement applied: ch20 冷静 in the trait-list 孤僻、冷静、独立 changed from
"cold" to "cool-headed".

Footnotes: 9 new (#62 to #70 by build order), ~3 per chapter-equivalent.
- ch19: title 梅花一夜漏春工 (author's line in the old manner, plum "leaks/betrays"
  spring, Wang Anshi tradition; uncorroborated as a direct quotation; anchored to
  "a row of last plum trees"); Yu Xuanji (鱼玄机, real Tang courtesan-poet — the
  source's 遁入佛门/"Buddhist gate" is contradicted, she was a Daoist); 月份牌
  color-lithograph calendar posters (Shanghai commercial art).
- ch20: title 一笑相逢哪易得 (author's line; the phrase 一笑相逢 is stock Song lyric,
  cf. Zhou Bangyan's Die lian hua "一笑相逢蓬海路"; uncorroborated as a full quotation);
  Pushkin "To the Sea" ("free element", 1824) + Dostoevsky "The Insulted and the
  Injured" (1861), A-Chu's Russian hints about the delegate — both corroborated;
  Mencius (孟子, Gaozi) "no water that does not run downward" — corroborated; the
  杨羽柏/"Yang Yubo" (in quotes) vs 杨羽桦/Yang Yuhua identity (the impostor father,
  rendered by context, not silently reconciled).
- ch21: title 千钧一发箭在弦 — the source of the book's own title. 千钧一发 corroborated
  (Han Yu, 与孟尚书书, "其危如一发引千钧"); 箭在弦上 corroborated (Chen Lin, "矢在弦上，不得
  不发"); connected to 一触即发 / On a Hair Trigger and to this chapter's climax.
  向/老向/向先生/向书记 = Fang Zhitong's underground cover-surname Xiang.
XHTML note bodies use numeric character references only (verified: no named
entities in the new notes); anchors verified as unique verbatim substrings before
building.

Twin / identity handling this batch:
- No 杨慕次/杨慕初 twin-name slip occurs in ch19-21. The mistaken-identity scenes
  (Cong Feng and Xin Lili each greet A-Chu as A-Ci/"阿初"; ch19) are deliberate plot,
  not typos, and are rendered straight.
- ch20 line 184 prints the borrowed identity "杨羽柏" (in quotes) then reverts to the
  true name 杨羽桦; footnoted (#65-order) and rendered by context (Yang Yuhua = the
  man living as Yang Yubo). 徐玉真 in quotes = the impostor "mother"; kept in quotes.
- Deliberate source irony kept, NOT "fixed": Yang Yuhua's fire story says the nurse
  岳嬷嬷 "died" in the blaze (ch21), yet Amah A-Yue is alive and burn-scarred at
  A-Chu's house (ch20) — the reader has known since ch13 she survived. Rendered
  faithfully on both sides.

Glossary: 16 new rows, one decided rendering per referent; existing renderings
reused unchanged (A-Chu/Yang Muchu, Muci/A-Ci, Xu Yuzhen, Ronghua, Cong Feng/Cong
Hui, Rong Chu, Rong Sheng, He Yashu, Xin Lili, Young Tang, Xia Yuechun, Liu A-Si,
Lu Liangchen, Fang Zhitong, Du Luning, Yang Yuhua, Yang Yubo, the Golden Dragon
Society, the Detective Division, Longjing, fabi). New people: Li Qinhong (李沁红,
"the Flower of Juntong"), Xiong Zida (熊自达, chief of the Detective Division), Gao
Lei (高磊 = Captain Gao), Staff Officer Ming (明参谋), Xiang (向, Fang Zhitong's
cover-surname), Amah A-Yue (岳嬷嬷, the 嬷嬷 form of 阿岳), Rong'er (荣儿), Chu'er
(初儿), Little Wu (小吴). New organizations: the Paramount (百乐门), the English
Tearoom (英伦茶室), the English Times (英伦时报), the Grand Light Hostel (大光明旅社,
distinct from 大光明电影院 the Grand Theatre), the Central Shanghai Commandant's
Office (沪中长官公署, HQ of the garrison command). New places: Plum Blossom Lane
(梅花巷), Avenue Joffre (霞飞路).

Figures: none in this batch.

Flagged for the read-through:
- Source clock-time inconsistency (not a translation error): ch19 A-Chu tells Xia
  the tea meeting is at 四点/four o'clock, but tells Lili 两点/two o'clock; ch20
  confirms 下午两点/two o'clock. Each English line matches its own source line.
- 一夜漏春工 / 一笑相逢哪易得 titles: author's lines in the old manner, not verifiable
  single quotations — rendered literally and footnoted as such.

Build: out/On a Hair Trigger.epub rebuilt, 22 of 36 units translated, 70 notes.
qa_epub.py PASS (36 documents, 3866 paragraphs, 70 references = 70 bodies = 70
backlinks, all links resolve).

================================================================================
## Batch B09 — Chapters 22 to 24 (ch22, ch23, ch24)

Scope: ch22 (25_part0023.txt, 330 paragraphs, ~8,986 chars), ch23 (26_part0024.txt,
223 paragraphs, ~5,211 chars), ch24 (27_part0025.txt, 218 paragraphs, ~6,626 chars).
771 paragraphs, ~20,823 source chars. The novel's crisis: Fang Zhitong is poisoned
in his cell (the orderly Little Wu, a Party man, then shot by Li Qinhong); Ronghua
rams her car into the disguised raid convoy to warn the comrades and dies with
Muci gravely hurt beside her; A-Chu operates on his own twin and their blood mingles;
the Detective Division sets a telephone voice-trap to expose the "Rivet"/mole.

Authoring flow: wrote out/<id>_en.txt (one English paragraph per source paragraph),
ran make_bilingual.py (verbatim `>` source lines; errors on count mismatch), then
split_bilingual.py. No mid-sentence paragraph splits in any of the three chapters
(every source paragraph ends on terminal punctuation).

Checks run and results:
- check_numbers.py --noise data/noise.txt : ch22 0 unresolved, ch23 0, ch24 0.
  12 new noise.txt rows (B09 section), all NON-quantity numerals:
  三刻 (clock 45-min quarter, like the built-in 一刻; rendered "forty-five"),
  两句 (少说两句), 万不得已 (simplified of built-in 萬不得已), 七窍 (七窍流血),
  零星 (零=0), 急三火四, 第二个人 (二 ordinal idiom), 三长两短, 万事 (万事皆休),
  两个人 (like built-in 二人), 万能 (万能输血者 "universal donor"), 千帕 (kilopascal,
  千 = SI kilo-). Clock times rendered so digits survive: 四点三刻→"four forty-five",
  五点三刻→"five forty-five", 六点三刻→"six forty-five", 六点三十分→"six thirty",
  七点四十五分→"seven forty-five". 108套刑具 rendered "108" (source uses Arabic
  digits); 2594米 rendered "2594 metres" (no thousands comma, which the checker
  would split).
- check_structure.py --pairs : parity OK for all three (330/330, 223/223, 218/218).
- Verbatim fidelity: data/zh/<id>.txt (minus ### title) diffed against source
  paragraphs (minus 2 metadata lines) = 0 content diffs for all three.
- Blind double translation + round-trip back-translation applied to the lyrical /
  argumentative passages (Ronghua's death choice and its rationale, ch22 §327-331;
  the blood-kinship reflection, ch23 §196-197; Rong Sheng's elegy for Ronghua,
  ch24 §22-24; A-Ci's coded farewell, ch24 §206). Paranoid audit of ~30 paragraphs
  (~4%) across all three chapters: observed error rate 0% (no omissions or
  mistranslations; the coded farewell 风、雨俱已不在 correctly preserves the double
  sense — the weather and the codenames Drifting Wind / Timely Rain both "gone").

Footnotes: 9 (builder-numbered #71 to #79), all anchors verified verbatim/unique.
- ch22 (4): title 截断众流大气魄 (author's pastiche; borrows the Yunmen Chan phrase
  截断众流, "cut off the myriad streams" — uncorroborated as a full quotation,
  the Chan source corroborated); Gu Shunzhang (顾顺章, 1931 defection — corroborated
  against the historical record, incl. Qian Zhuangfei's cipher-office warning);
  Wu Hao (伍豪 = Zhou Enlai's documented alias — corroborated); the source's own
  bookstore-name slip (荣华书店 here vs 华美书店 elsewhere — rendered as it stands,
  not reconciled).
- ch23 (2): title 恶氛弥天血火焚 (author's own line — uncorroborated as a quotation;
  草木皆腥 plays on 草木皆兵 from the Fei River rout, corroborated); Rh-negative type A
  as the rare blood type (~3/1000 in Han Chinese) and the physical proof of kinship.
- ch24 (3): title 风雨未肯收余寒 (author's line in the old manner — uncorroborated as
  a quotation, rendered literally); 黛玉焚稿 (Dream of the Red Chamber ch.97 —
  corroborated literary allusion + foreshadowing); 宁可错杀一千 / 宁枉勿纵 (the
  Nationalist White Terror slogan — documented as a watchword, attribution to
  Chiang traditional and disputed).
Recurring refs already noted (not re-noted): the Xiang cover-name of Fang Zhitong
was footnoted at Chapter 21 (so "Xiang Chengfa" 向成发, the full cover name new here,
is glossed in the glossary only, not re-footnoted).

Glossary: 20 new rows, one decided rendering per referent; existing renderings
reused (A-Chu, A-Ci, Ronghua, Fang Zhitong, Xiong Zida, Li Qinhong, Gao Lei, Du
Luning, Han Zhengqi, Han Yu, Xia Yuechun, Rong Chu, Rong Sheng, Lu Liangchen, Liu
A-Si, Amah A-Yue, Yang Sitong, He Yashu, Little Wu, the Detective Division, the
Special Branch, Plum Blossom Lane, the Huamei Bookstore, the Chunhe Hospital, the
Grand Light Hostel, the Central Shanghai Commandant's Office, Longjing). New people:
Jiao Tongshun (焦同顺), Xu Cheng (徐诚), Liu Yun (刘云 = Adjutant Liu, 刘副官), Lu A-Zhen
(陆阿贞), Gu Shunzhang (顾顺章), Wu Hao (伍豪), Xiang Chengfa (向成发, Fang Zhitong's
full cover name). New orgs: the Majestic Theatre (美琪大戏院), the British police
station (英国巡捕房). New places: Hengji Li (恒吉里), Gordon Road (戈登路), Bubbling Well
Road (静安寺路), Suzhou Creek (苏州河), Weihai Road (威海路), Yunnan Road (云南路),
Guangdong Road (广东路), Qinghefang (清河坊). New term: the Rivet (铆钉, the Division's
informant codename).

Twin / identity handling this batch:
- No 杨慕次/杨慕初 twin-name slip occurs in ch22-24 (A-Chu is written 阿初 throughout;
  杨慕次 always denotes Muci). Rendered straight.
- Fang Zhitong appears under both his real name and his full cover name 向成发
  (Xiang Chengfa) within Xiong Zida's one speech (ch22 §18-22); rendered by context,
  with the Xiang cover-identity already footnoted at Chapter 21.
- Bookstore name slip (荣华书店 / 华美书店) rendered as it stands and footnoted, NOT
  reconciled (per CLAUDE.md rule 4).

Register / rendering notes:
- Clock times deliberately rendered so their digits survive per the QC contract
  ("four forty-five", "seven fifty-two"), not "a quarter to five" / "half past".
- 英国巡捕房 standardized to "the British police station" (ch24 initially had
  "British patrol house"; fixed to one rendering and glossed).

Figures: none in this batch.

Build: out/On a Hair Trigger.epub rebuilt, 25 of 36 units translated, 79 notes.
qa_epub.py PASS (36 documents, 4634 paragraphs, 79 references = 79 bodies = 79
backlinks, all links resolve).

---

## Batch B10 — Chapters 25 to 27 (ch25, ch26, ch27)

Scope: ch25 (退步原来是向前, 256 paragraphs), ch26 (白云可杀不可留, 253 paragraphs),
ch27 (踏破冰火九重天, 225 paragraphs). ~20,965 source chars, 734 paragraphs total.
Authoring flow as established: wrote out/<id>_en.txt (one English paragraph per
source paragraph), assembled the bilingual with make_bilingual.py (verbatim `>`
source lines), then split_bilingual.py for the reading files and parity sources.
No mid-sentence paragraph splits occurred in any of the three chapters; parity is
one English paragraph per source paragraph throughout.

Checks run and results:
- check_numbers.py --noise data/noise.txt: 0 unresolved on all three (ch25 256/256,
  ch26 253/253, ch27 225/225). New noise.txt rows added this batch (all non-quantity):
  零度 (降到零度 "to zero"), 万劳苦 (residue of 千百万劳苦大众 after the built-in 千百 rule
  orphans a stray 万), 九泉 (九泉之下), 二来 (一来...二来 enumerator), 一干二净, 百花
  (命百花盛开 / 百花神主), 五内 (五内如焚). 十足 and 一百八十度 were already present.
- check_structure.py --pairs: parity OK on all three (256/256, 253/253, 225/225).
- Verbatim fidelity: data/zh/<id>.txt (minus title) diffed against the source
  paragraphs (minus the 2 metadata lines) = zero content diffs on all three (only the
  source files' missing final newline differs, as expected).
- Blind double translation + round-trip back-translation run in a separate context on
  12 lyrical/argumentative paragraphs (Xia Yuechun's auditory-vs-visual-memory speech,
  the 插秧诗 quatrain, Zhong Yundi's mole-hunt logic, Bai Yun's recantation, the peony/
  Wu Zetian legend, Du Luning's clown-in-the-open strategy, the 移花接木 analysis, Li
  Qinhong's deduction, the 回头是岸/水到渠成 exchange, and others). No substantive
  divergences: every number, name, relationship and allusion survived both directions.
- Paranoid audit: the mechanical checks (numbers, parity, verbatim) ran on 100% of
  paragraphs; the full double/back-translation treatment plus a manual fact-dense deep
  read covered ~25 paragraphs (~3.4%). Observed error rate: 0%.

Footnotes (9 this batch, builder-numbered #80 to #88, ~3 per chapter):
- ch25: the title 退步原来是向前 traced to the 《插秧诗》 attributed to the Cloth-Bag Monk
  (布袋和尚 / 契此), corroborated as the traditional attribution (noting the novel's
  variant third line and its "former Tang" mislabel); 移花接木 (the substitution ruse);
  耳听为虚，眼见为实 (the visual-over-auditory proverb the trick exploits).
- ch26: 进亦不喜，退亦不忧 traced to Fan Zhongyan's 《岳阳楼记》 "是进亦忧，退亦忧"
  (corroborated); the title 白云可杀不可留 found to be the author's own line, punning on
  the character-name Bai Yun (uncorroborated as a quotation); 踏破铁鞋无觅处，得来全不费
  功夫 (corroborated proverb, from 夏元鼎 / 《水浒传》).
- ch27: the title 踏破冰火九重天 found to be author's pastiche, 九重天 glossed as the
  ninefold heaven (uncorroborated as a quotation); the peony / Wu Zetian legend and
  洛阳牡丹甲天下 (corroborated as a widely told legend, folklore not official history,
  though Wu Zetian's fondness for Luoyang peonies is attested); the 回头是岸 / 水到渠成
  proverb exchange between Muci and Rong Chu.

Glossary: 17 new rows (one decided rendering per referent, existing renderings reused).
New people: Zhong Yundi (钟云迪), Tian Xiuyun (田秀芸), Bai Yun (白云, her alias), A-Chun
(阿春, exposed as the Rivet). New orgs: the Red Spear Squad (红枪队), the Yang Industrial
Company (杨氏实业社), the Xianghe Cotton Mill (祥和纱厂), the Lanxin Theatre (兰心大戏院),
the White Rose Ballroom (白玫瑰舞厅), the Ren'ai Hospital (仁爱医院). New places: Fourth
Avenue (四马路), the Racecourse (跑马厅), Luoyang (洛阳), Zhabei District (闸北区). New
terms: Snow Wolf (雪狼, codename), police runner (包打听), Shaoxing opera (绍兴文戏).

Twin / identity handling this batch:
- A-Chu is written 阿初/杨慕初 and A-Ci 阿次/杨慕次 throughout; no genuine twin-name slip.
  ch25 deliberately marks the body double with quotes ("杨慕次") in the first-call scene
  and drops them for the real man; rendered faithfully with the quotes preserved, and
  the 移花接木 substitution is explained by the source itself (ch25 §178-189) and glossed.
- The mole/double-agent reveal (阿春, ostensibly a Special Branch peripheral, exposed as
  the Juntong "Rivet"; his wife 田秀芸 = 白云, a 1927 defector) is rendered as it stands.

Figures: none in this batch.

Build: out/On a Hair Trigger.epub rebuilt, 28 of 36 units translated, 88 notes.
qa_epub.py PASS (36 documents, 5365 paragraphs, 88 references = 88 bodies = 88
backlinks, all links resolve).

## Batch B11 — Chapters 28 to 30 (ch28, ch29, ch30)

Scope: Chapter 28 (ch28, 间不容发生死际, src 31_part0029.txt, 159 paras), Chapter 29
(ch29, 欲披荒草访疑尘, src 32_part0030.txt, 206 paras), Chapter 30 (ch30, 同生共死亲
兄弟, src 33_part0031.txt, 262 paras). ~17,303 source chars, 627 paragraphs total.
Continues from B10 (Prologue + Chapters 1 to 27 already built).

Plot delivered this batch:
- ch28: Xia Yuechun and Yu Xiaojiang spring the hospital trap. Yu Xiaojiang, in a
  nurse's uniform behind the ward screen, shoots Li Qinhong dead (silenced, plus the
  Juntong two extra rounds) and is revealed as the new "Timely Rain," Muci's superior.
  Cong Feng is passed out via the "Short History of Chinese Philosophy" fallback
  password to Snow Wolf and the Fourth-Avenue conference; A-Chu removes the body under
  cover of a false fire alarm; three days later Yu Xiaojiang raids an empty conference
  site. Du Luning and Yu Xiaojiang discuss the "unidentified radio" (she pins it on the
  Japanese, citing the Mukden Incident). Cong Feng sails; A-Chu and Xia Yuechun close
  with the Persian-chessboard parable and the returned cartridge cases.
- ch29: Winter 1932. Xiong Zida ousted (the Pravda / Xin Zhonghua Bao coverage did him
  in) and hands over to a Du-planted staff. Yu Xiaojiang tells Muci that Ronghua will be
  named a martyr and that the secret transmitter near Yuyuan Road is likely Japanese and
  likely in his own house; Muci names his "mother" as the suspect. Koyama Eiko (小山缨子,
  the false Xu Yuzhen) is shown at her radio, discovering her girlhood photo gone. Muci,
  who took it, goes over the wall to Plum Blossom Lane; he and A-Chu read the three
  photos (mother / disguised false mother / the false mother's true face) and set out at
  3 a.m. to survey the Ciyun Temple, where a beam drops on A-Chu — cliffhanger.
- ch30: Muci saves A-Chu into the crypt; the woman above blows the hall. Trapped, the
  twins talk (backstory, A-Chu's Rong-family childhood, his fall-triggered hallucination
  of the Nagoya-obi woman) and Muci reads the "mirror" as the water, finding the
  underwater passage and, in the wooden room, their real mother's skeleton (murdered by
  waist-cutting, her identity stolen by the Japanese impostor). They climb the hollow
  tree; at the top "Mother"/Koyama Eiko waits with a gun. Muci hooks A-Chu safe, refuses
  to drop him, shouts "Sitong!" — a shot rings out (cliffhanger into B12).

Checks run (recorded per unit):
- check_numbers.py --noise data/noise.txt: ch28 0 unresolved, ch29 0, ch30 0.
  Noise added this batch (5 rows): 一万亿 (chessboard-legend grain count; the checker has
  no 亿=10^8 branch so 一万亿 misparses to 10000 — rendered "a trillion" in prose); 百姓
  (in 老百姓, 百 lexicalized, not 100); 零点 ("zero hour / midnight", 零=0 not a quantity);
  万籁 (in 万籁俱静, 万 = "myriad", not 10000); 一泻千里 (idiom, 千 not 1000, not in the
  built-in list). One genuine fix rather than noise: ch30 §62 四个字 rendered "Those four
  words" (was "Those words") so the count 4 survives and the four-character judgment
  至柔至刚 stays faithful. Clock/date digits preserved: "three in the morning" (凌晨三点),
  "about one in the morning" (凌晨一点), midnight; 1910/1922/1932 as digits; the Mukden
  Incident rendered "the eighteenth of September" (September credits 9; 一八 parses to None
  so no residue). "sixty-four squares" (64) and "two" (第二/两) both survive.
- check_structure.py --pairs: parity OK for all three (159/159, 206/206, 262/262); note
  anchors resolve; headings uniform (one H2 couplet title per chapter, flat prose).
- Verbatim fidelity: data/zh/<id>.txt (minus ### title) diffed against source (minus 2
  metadata lines) — zero content diffs for all three (only the source files' missing
  final newline differs, as expected). The ch28 pirate-site watermark (阳光中文网 …) is
  kept verbatim in the bilingual `>` line, omitted from the reading text, and footnoted.
- Blind double translation + round-trip back-translation applied to the argumentative /
  lyrical passages: the Persian-chessboard parable and the king/minister accusation
  (ch28 §130, §133, §135), Koyama Eiko's interior monologue (ch29 §80 to §88), the
  transmitter call-sign scene (ch29 §90 to §92), the crypt Zen exchange (ch30 §38 to §44),
  and the reconstruction of the murder (ch30 §211 to §219). Divergences were of English
  phrasing only; no clause dropped, no ambiguity smoothed, nothing invented. Plain
  narration sampled throughout.
- Paranoid audit: the mechanical checks (numbers, parity, verbatim) ran on 100% of the
  627 paragraphs; the full double/back-translation plus fact-dense manual deep read
  covered ~24 paragraphs (~3.8%). Observed error rate: 0%.

Footnotes (10 this batch, builder-numbered #89 to #98):
- ch28: title 间不容发 traced to Mei Cheng's 《上书谏吴王》 (西汉), corroborated, and set
  beside the ch21 千钧一发 (Han Yu); the Mukden Incident / 九一八 (18 Sept 1931, Kwantung
  Army, South Manchuria Railway, Liutiaohu, Manchukuo 1932), corroborated; the recognition
  password 《中国哲学简史》 (Feng Youlan, Macmillan 1948) flagged as anachronism (book and
  publisher corroborated, the 1948 date makes it the author's anachronism); the ch28
  pirate-site watermark line noted (kept in QC, cut from reading text).
- ch29: title 欲披荒草访疑尘 found to be author's pastiche, no single source (uncorroborated);
  the 中国民权保障同盟 / China League for Civil Rights (Shanghai, Dec 1932), corroborated,
  dating the chapter; Wang Jingwei's 曲线救亡 accommodationist slogan, corroborated.
- ch30: title 同生共死亲兄弟 found to be a plain line in the old manner, not a traceable
  quotation (uncorroborated), answered by 有缘共死，不枉同生; 假作真时真亦假 traced to the
  《红楼梦》 太虚幻境 couplet (companion line 无为有处有还无), corroborated, 红楼梦 first
  noted at ch24; the 名古屋带 / Nagoya obi (a modern c.1920 sash), whose tie to the 桃山
  age the source gives loosely — contradicts the actual origin.

Glossary: 16 new rows (one decided rendering per referent; existing renderings reused —
Xu Yuzhen, Xiong Zida, Huamei Bookstore, Ciyun Temple, Amah A-Yue, the Imperial Flower,
Liu Yun, Rong'er, Shenyang, Timely Rain, Snow Wolf, all carried over unchanged).
New people: Koyama Eiko (小山缨子, provisional; the false Xu Yuzhen / Imperial Flower),
Wang Jingwei (汪精卫), Mao Zedong (毛泽东). New orgs: the China League for Civil Rights
(中国民权保障同盟), the Kwantung Army (关东军), the Northeast Army (东北军), Pravda (真理报),
the Xin Zhonghua Bao (新中华报). New places: Liutiaohu (柳条湖), the South Manchuria Railway
(南满铁路). New terms: a Nagoya obi (名古屋带), the Momoyama age (桃山时代), A Short History
of Chinese Philosophy (中国哲学简史), salvation by a roundabout path (曲线救亡), Green Bamboo,
Spring Dawn (翠竹春晓), the puppet state of Manchukuo (伪满).

Twin / identity handling this batch:
- A-Chu is written 阿初/杨慕初 and A-Ci 阿次/杨慕次 throughout; no genuine twin-name slip.
  The two spend chs 29-30 alone together for the first time; both self-designations are
  rendered by referent as established (A-Chu / A-Ci; Muci for narration of 阿次).
- The impostor's reveal is rendered as it stands: "徐玉真" (false mother, in quotes) is
  the Japanese agent Koyama Eiko (小山缨子); the murdered birth mother's skeleton and the
  identity-theft reconstruction are given faithfully, not reconciled or softened.

Figures: none in this batch.

Build: out/On a Hair Trigger.epub rebuilt, 31 of 36 units translated, 98 notes.
qa_epub.py PASS (36 documents, 5989 paragraphs, 98 references = 98 bodies = 98
backlinks, all links resolve).

## Batch B12 — Chapters 31 to 33 (ch31, ch32, ch33) — DONE

Scope: ch31 (游鱼见食不见钩, 207 paras), ch32 (醇酒美人鸳鸯剑, 172 paras), ch33
(假做真时真亦假, 195 paras). ~17,971 source chars, 574 paragraphs.

Pipeline: wrote out/<id>_en.txt (one English paragraph per source paragraph), assembled
out/<id>_bilingual.md with make_bilingual.py (verbatim `>` source lines), split with
split_bilingual.py to out/<id>_reading.md + data/zh/<id>.txt. Register per B11: straight
ASCII double quotes, ASCII ellipsis (...), semicolons/colons for flow, no em dashes, no
curly quotes.

Checks:
- check_structure parity OK: ch31 207/207, ch32 172/172, ch33 195/195.
- Verbatim fidelity: diff of data/zh/<id>.txt (minus title) against the source paragraphs
  = zero content diffs on all three (only the source's missing final newline differs).
- check_numbers --noise data/noise.txt: 0 unresolved on all three (and no regression:
  re-ran ch00..ch30, all still 0). Fixes this batch:
  * check_numbers.py: added a monetary rule r"[一二三四五六七八九十]千万" / r"[...]千萬"
    BEFORE the generic 千万 intensifier, which otherwise fragments 三千万/七千万/五千万
    and orphans a bare 3/7/5 (the residue cannot be safely noised, as extra-noise runs
    after the built-in NOISE). English carries the amounts faithfully ("thirty/seventy/
    fifty million"). Added WORD_NUM "eighteenth": 18 for 十八层地狱 ("the eighteenth level
    of hell").
  * data/noise.txt: 7 rows — 阿九 (A-Jiu, agent name; 九), 百看不厌 (idiom; 百),
    百合 (lily, plant name; 百), 千野 (Koyama Chino name; 千), 一万个 (in 一万个不痛快,
    intensifier; 万), 两边 (simplified "both sides", built-in list only strips 兩边; 两),
    五分属 (Japanese verse 此景五分属江户 = "half belongs to Edo"; 五分 = "half").
- Blind double translation (ch32 Koyama Chino's imperial-loyalty harangue; ch33 A-Chu's
  unmasking of the false Amah A-Yue): independent renderings matched in sense; only
  difference a subagent romanizing 缨子 as "Yingzi" vs the glossary's decided "Eiko".
- Round-trip back-translation (ch31 He Yashu's love monologue): every element survived
  (all five verbs 爱/敬/疼/恨/怨, the prejudice, the dream imagery); no omissions.
- Paranoid deep audit ~3.5% of the batch (the three hardest passages above + all-paragraph
  verbatim/number checks): observed error rate 0%.

Footnotes: 9 (#99 to #107). ch31 title 游鱼见食不见钩 (proverb 人见利而不见害，鱼见食而不见钩,
《镜花缘》/《鬼谷子》; the exact 7-char line the author's own — corroborated as a saying).
ch32 title 醇酒美人鸳鸯剑 traced to 醇酒美人 (史记·魏公子列传, 信陵君) + 鸳鸯剑 (红楼梦 尤三姐/
柳湘莲) — both corroborated; plus Thales/Thracian-girl (Plato, Theaetetus 174a, corroborated),
Nietzsche's tree (Thus Spoke Zarathustra I, "The Tree on the Mountainside", corroborated),
the ch32 pirate-site watermark line (阳光中文网, kept in QC, cut from reading text), and
文野三界之别 (Liang Qichao's 文野三界 schema via Fukuzawa — corroborated as his idea).
ch33 title 假做真时真亦假 cross-referenced to the ch30 红楼梦 太虚幻境 couplet note (variant
做 for 作, not re-noted); plus 上邪 (Han yuefu love-oath, 铙歌十八曲, corroborated) and the
富士山顶雪飘飘 Japanese verse (author's pastiche, uncorroborated).

Glossary: 17 new rows (existing renderings reused — He Yashu, Yang Yuhua, Xu Yuzhen, Amah
A-Yue, Koyama Eiko, Sakai Ichiro, Rong Sheng, Rong Gui, Rong Chu/Rong'er, Yang Sitong,
Young Tang, Liu A-Si, Lu Liangchen, Han Zhengqi, the Dongyang Company, Plum Blossom Lane,
the Huamei Bookstore, the Ciyun Temple, Mount Wu, the Imperial Flower — all carried over).
New people: Ming Tang (明堂), Koyama Chino (小山千野, provisional; source gives no gendered
pronoun, so none supplied), Thales (泰利士), Plato (柏拉图), Nietzsche (尼采), Liang Qichao
(梁启超), Mingxuan (明轩, provisional). New orgs: the Ming enterprises (明氏企业), the
Shanghai Stock Exchange (上海证券交易所), the Shanghai News (上海新闻报), Chen's Greenhouse
Flower-House (陈氏温室花房). New places: Changle Street (长乐街), Edo (江户), Mount Fuji
(富士山). New terms: the mandarin-duck swords (鸳鸯剑), Shang Ye (上邪), On the Distinction
of the Three Realms of Civilized and Barbarous (文野三界之别).

Twin / identity handling this batch:
- A-Chu (阿初/杨慕初) and A-Ci/Muci (阿次/杨慕次) rendered by referent as established. The
  ch33 climax turns on a body-double swap: Muci, disguised as A-Chu, is the one hypnotized
  while the real A-Chu waits at the door; both are rendered plainly as who they are, with
  Amah A-Yue's confusion ("You're not Yang Muchu?!") left as it stands.
- The impostor chain is rendered faithfully, not reconciled: the hypnotist falsely tells
  A-Chu the young skeleton is his birth mother (ch33 mid), and A-Chu later exposes that the
  cut-in-two skeleton is in fact the real Amah A-Yue (40+), murdered 20 years ago, whose
  identity the Japanese agent (present "Amah A-Yue") stole. Left visible, not smoothed.

Figures: none in this batch.

Build: out/On a Hair Trigger.epub rebuilt, 34 of 36 units translated, 107 notes.
qa_epub.py PASS (36 documents, 6560 paragraphs, 107 references = 107 bodies = 107
backlinks, all links resolve).

## Batch B13 — Chapters 34 to 35 (ch34, ch35) — DONE (FINAL BATCH)

Translated end to end: ch34 (6,568 source chars, 240 paragraphs) and ch35 (8,534
chars, 284 paragraphs); ~15,102 source chars, 524 paragraphs. This finishes the
novel: all 36 units (Prologue + 35 chapters) are now translated and built. One
bilingual QC file per unit, reading text and parity source generated with
split_bilingual.py. Flat book, one H2 couplet title per chapter; no mid-sentence
paragraph splits occurred (source paragraphs are sentence-complete).

Authoring flow: wrote out/<id>_en.txt (one English paragraph per source
paragraph), assembled the bilingual with make_bilingual.py (verbatim `>` source
lines), then split_bilingual.py. Not one source line hand-typed. No pirate-site
watermark line in either chapter.

Checks run and what they found:
- Check 1, faithful verbatim quotation: data/zh/ch34.txt and data/zh/ch35.txt
  diffed line-for-line against the raw source paragraphs (data/src, minus the two
  metadata lines). ZERO content diffs (only the source files' missing final
  newline). Every source paragraph quoted verbatim, none dropped or merged.
- Check 4, automated invariants:
  * check_structure.py parity OK for both (240/240, 284/284).
  * check_numbers.py --noise data/noise.txt: 0 unresolved for both. Real
    counts were rendered so their digits survive; a few flags were genuine
    counts fixed in the prose rather than noised: 三人 -> "the three of them"
    (ch35), 百感交集 rendered "a hundred feelings" (not "a thousand"; the first
    draft's "thousand" was the one genuine content slip, caught mechanically by
    check_numbers and corrected), and the closing dates rewritten with Arabic
    day numbers (August 13 / August 14 / September 22 / November 12) because
    WORD_NUM does not know thirteenth/fourteenth/twenty-second/twelfth.
  * noise.txt additions (4, all non-quantity numerals): 百川丛惠子 (百 in the
    Japanese surname Momokawa, not 100), 五金 (五金商行 "hardware," not 5), 万物
    (宇宙万物 / 万物复苏 "all things," 万 = myriad), 万念俱灰 (idiom, 万 = myriad).
- Checks 2/3, blind double translation + round-trip back-translation on the
  argumentative/lyrical passages (Keiko's 1909 confession, A-Chu's hypnotic
  dream, the 上邪 love-oath, the father-son bomb confrontation, the linked-verse
  coda, the 1937 broadcast): no divergence of sense and no omission surfaced.
- Check 5, term ledger: existing renderings reused throughout (A-Chu/A-Ci/Muci,
  Yang Yuhua/Yubo, He Yashu, Xia Yuechun, Du Luning, Yu Xiaojiang, Gao Lei, Han
  Zhengqi/Han Yu, Young Tang, Huang Sanyuan, Koyama Eiko/Chino, Rong Sheng/
  Rong'er, the Fourth Madam Yang Mulian, Rongrong/Ronghua, the Land Survey
  Department, the Imperial Flower, Plum Blossom Lane, the Park Hotel, and so on).
- Check 8, deep paranoid audit: ~14 paragraphs (~2.7%) given the full
  verbatim/double/back-translation treatment (ch34 pairs 10, 39, 46, 104, 200,
  238; ch35 pairs 16, 19, 44, 74, 107, 225, 246, 283). No residual omission or
  mistranslation; observed error rate ~0% post-correction.

Notes added: 7 (builder numbers #108 to #114 in reading order).
- ch34 (3): 反客为主 = Stratagem No. 30 of the Thirty-Six Stratagems (three十六计),
  anchored "turned the guest into the host" (corroborated); Momokawa Keiko
  (百川丛惠子) provisional Japanese reading, anchored "Momokawa Keiko"; the
  陆地测量部 / Land Survey Department of the IJA General Staff, a real 1888-1945
  mapping body (corroborated), anchored "the Land Survey Department of the Army
  General Staff."
- ch35 (4): the title 一举锄奸雁归行 as the author's own pastiche + the 雁行
  (geese-in-formation = brothers) image, anchored "Brothers are like geese in
  flight"; the closing 1937 broadcast as a real National Government / Chiang
  Kai-shek wartime statement issued around the fall of Shanghai in November 1937
  (corroborated; exact document/date given variously), anchored "an order given
  at dawn is answered by dusk"; the sons' names 爱中/爱华 = "love China" (爱中华),
  anchored "Aizhong and Aihua"; the linked verse 愿君怜取眼前人 echoing Yan Shu's
  (晏殊) Huanxi sha, anchored "May you cherish the one before your eyes."
- Recurring refs cross-referenced, not re-noted: 上邪 (noted ch33), the Nine
  Springs / 九泉 (noise), the Imperial Flower and Xu Yuzhen (earlier).

Glossary rows added (9): people 百川丛惠子 (Momokawa Keiko, provisional), 爱中
(Aizhong), 爱华 (Aihua); orgs 东方杂志 (the Eastern Miscellany, attested), 申报 (the
Shen Bao, attested), 明风矿厂 (the Mingfeng Mine), 荣氏药业公司 (the Rong
Pharmaceutical Company); places 芸香阁 (the Yunxiang Pavilion, provisional); terms
木符 (wooden charm). Twin/identity handling: bare 阿次 in narration rendered
"Muci," in address "A-Ci," per the established convention; no name-slip in either
chapter to footnote.

Translator's note: updated its middle sentence in book.json for the finished book
(the chapter titles are now rendered and their sources set out in the notes,
rather than "will be finalized ... as each chapter is translated").

Figures: none.

Build: out/On a Hair Trigger.epub rebuilt, 36 of 36 units translated, 114 notes.
qa_epub.py PASS (48 files, 42 documents, 7,082 paragraphs, 114 references = 114
bodies = 114 backlinks, all links resolve).

---

## Register pass R01 (2026-08-03): ch02, ch03, ch04, ch05, ch06 + ch00 note backfill

First execution batch of the whole-book register pass (see REGISTER_PASS.md).
Two workstreams run together: a style-only prose revision (never a
retranslation) and footnote densification to the new policy (a Western reader
with no background in Chinese custom, notes at first occurrence, coverage-driven
not a quota). ch00 and ch01 were the exemplar (commit 895d19c); ch01's notes
were already densified. Analysis was committed to edits/<id>_edits.md
(TOUCH/RECAST blocks and NOTE-ADD blocks) and then executed exactly (exact-match
replacement asserting count == 1, via Python; notes appended and anchors
verified as verbatim substrings before building).

Triage was deliberately conservative, per the exemplar's calibration: these are
ordinary chapters (like ch01), so most paragraphs LEAVE and prose touches are
few. The value this batch adds is chiefly in the notes.

Prose edits applied (6 total, all verified against source, no drift):
- ch02 p1 (T2) scene card "1931, England, Cardiff" set italic; p2 (T3) "the
  laughter of the two of them" to "their"; p31 (T3) "the tip of Cong Hui's toe"
  to "the tips of her toes".
- ch03 p20 (T1) 咬金嚼铁 "teeth set like grinding iron" to "jaw set like iron".
- ch04 p1 (T2) scene card "China, Shanghai, 16 March 1931" set italic.
- ch06 p203 (T3/T1) 春葱 "fingers like spring scallion sprouts" to "slender,
  tapering fingers" (the stock beauty-simile reads comically in English; effect
  kept, 苍白无力 kept as "pale and limp").
- ch05: no prose edits (a clean action/interrogation chapter; forcing edits
  would be churn).

Notes added (20 total; each checked against all prior units for first-occurrence
coverage, scholarship verified, XHTML with numeric character references):
- ch00 (+3, now 4): pear-blossom whiteness/parting motif; peony as emblem of
  rank; the golden-lotus bound foot.
- ch02 (+5, now 8): household bond-servant 家奴; the 私塾/洋学堂 (traditional vs
  Western school) divide; the xiao flute; opium and the pipe (with morphine
  weaning); the Confucian 报恩 gratitude-debt.
- ch03 (+3, now 6): the karmic-foe idiom 冤家 ("five hundred years"); the meaning
  of being made to kneel (下跪); the traditional-medicine 虚不受补 behind Rong
  Sheng's feigned illness by overdosing tonics.
- ch04 (+3, now 6): the "iron rooster" 铁公鸡 miser idiom; the 1927 KMT-CCP
  rupture and White Terror behind the underground; the rural Soviet base areas 苏区.
- ch05 (+1, now 4): the storm-before-upheaval allusion 山雨欲来风满楼 (Xu Hun).
- ch06 (+5, now 9): elite Shanghai girls' schools (St. Mary's Hall); the Butterfly
  Lovers 梁祝 / 殉情 behind the paper butterflies; the cupped-hand bow 长揖; the
  earth-god shrine 土地庙; the Bund 上海滩 with the 英雄救美 trope.

Recurring subjects were cross-referenced, not re-noted: Bannermen, the Madams,
wedding red, the moon gate and longevity lock (all ch01); Juntong and the
Special Branch, Dai Li, the codenames (ch04-05); the chapter-title poem
allusions and the existing Manifesto / Dream of the Red Chamber / Lu Xun notes.
Notes not added where the scene already makes the point plain or the item is not
Chinese-specific (mimeograph, telegraph office, Tokyo Imperial University).

Checks: per chapter, split_bilingual.py regenerated reading + data/zh; parity OK
(ch02 191, ch03 132, ch04 133, ch05 119, ch06 220); check_numbers 0 unresolved
(data/noise.txt unchanged, no idiom lost a real quantity); straight-quote guard
clean on all six reading files; no source ">" line changed in any bilingual file.

Glossary/figures: no changes (this pass never re-romanizes or renames).

Build: out/On a Hair Trigger.epub rebuilt, 36 of 36 units translated, 149 notes.
qa_epub.py PASS (48 files, 42 documents, 7,082 paragraphs, 149 references = 149
bodies = 149 backlinks, all links resolve).


## Register pass R02 (ch07 to ch11) — 2026-08-03

Second execution batch of the register pass (REGISTER_PASS.md): style-only prose
revision plus footnote densification. Content frozen; no source ">" line touched,
no paragraph merged or split, names per glossary.json. Edit lists committed under
edits/ (ch07 to ch11). Book-wide notes 149 to 170.

Prose edits (3 total; these are ordinary chapters like ch01, so most paragraphs
LEAVE and only genuine calques were touched):
- ch07 p005 (T1) 眼高手低 "high of eye and low of hand" to "her sights set high
  and her gifts modest" (high standards, modest ability; the image-by-image
  calque does not carry in English).
- ch07 p022 (T1) 虎头蛇尾 "ended like a tiger's head and a snake's tail" to
  "began with a flourish and trailed off to nothing" (imposing start, feeble
  finish; the tiger/snake image does not land).
- ch08 p038 (T1) 急风暴雨 "still such wind and rainstorm as ever?" to "still such
  a whirlwind as ever?" (of a person's headlong manner; "whirlwind" is natural).
- ch09, ch10, ch11: no prose edits (clean literary/dialogue chapters; forcing
  edits would be churn).

Notes added (21 total; each checked against ALL prior units for first-occurrence
coverage, scholarship verified, XHTML with numeric character references):
- ch07 (+6, now 9): the New Year print 年画 and its stock "advertisement girls";
  the kowtow 磕头 (with the old-rules waiver); burning incense to the ancestors
  祭祖; the Qingming tomb-sweeping festival 清明节; Guanyin 观音 with "building
  bridges and mending roads" 修桥铺路; Tongji Hospital 同济医院 (Paulun, 1907).
- ch08 (+5, now 8): the qipao 旗袍; Longjing 龙井 tea; the traditional styptic
  "white medicine" 白药 (Yunnan Baiyao); the Shanghai Garrison Command 淞沪警备司令部;
  the Yan'an 延安 anachronism (the 1931 base was the Jiangxi Soviet; Yan'an post-1935).
- ch09 (+2, now 5): the spirit-tablet 灵牌 and its shrine offerings; the death-day
  祭日 memorial anniversary.
- ch10 (+3, now 6): the jade bangle 玉镯 as an intimate love-token; the French
  Park / French Concession 法国公园 and extraterritorial Shanghai; the "warming,
  restorative" 温补 prescription and herbal decoction.
- ch11 (+5, now 9): the family head's private penal power 家法; temple lot-drawing
  divination 求签; bird's-nest-and-white-fungus 燕窝银耳 delicacy; Chinese painting's
  scattered-point perspective 散点透视 (国画); the Han Yu maxim 不平则鸣.

Recurring subjects were cross-referenced, not re-noted: the Special Branch and
Juntong and the Soviet base areas (ch04); the wife/concubine hierarchy and the
Madams, the bridal sedan, the longevity lock and three-years mourning (ch01); the
"five poisons" and the Aisin Gioro renaming (ch09 existing notes); the Bund and
the 英雄救美 trope (ch06). Notes NOT added where the scene already makes the point
plain (the substitute-bride 代嫁 logic is spelled out in ch09; ballroom dancing is
self-explained in ch08) or the item is not Chinese-specific (Cinderella, cocktail).

Checks: per chapter, split_bilingual.py regenerated reading + data/zh; parity OK
(ch07 144, ch08 170, ch09 120, ch10 129, ch11 190); check_numbers 0 unresolved
(data/noise.txt unchanged, no idiom lost a real quantity); straight-quote guard
clean on all five reading files; no source ">" line changed in any bilingual file.
Spot-audit: all 21 edited/annotated paragraphs (the whole touched set) re-read
against their source lines, no meaning drift.

Glossary/figures: no changes (this pass never re-romanizes or renames).

Build: out/On a Hair Trigger.epub rebuilt, 36 of 36 units translated, 170 notes.
qa_epub.py PASS (48 files, 42 documents, 7,082 paragraphs, 170 references = 170
bodies = 170 backlinks, all links resolve).

## Register pass R03 (ch12 to ch15) — 2026-08-04

Third execution batch of the register pass (REGISTER_PASS.md): style-only prose
revision plus footnote densification. Content frozen; no source ">" line touched,
no paragraph merged or split, names per glossary.json. Edit lists committed under
edits/ (ch12 to ch15). Book-wide notes 170 to 191.

Prose edits (1 total; ch12-15 are dramatic/operatic chapters whose heightened
register is intentional and already well made, so almost every paragraph LEAVES
and only one genuine calque was touched):
- ch12 p080 (T1) 不打自招 "a confession before the whip" to "as good as a
  confession" (the scarf in April weather was itself self-incrimination; the
  literal version wrongly imports a whip/torture image and reads as anticipating
  torture rather than giving oneself away).
- ch13, ch14, ch15: no prose edits (the revelation, the climax, and the funeral
  confrontation all read cleanly in their own register; forcing edits would be
  churn, per the ch01 calibration).

Notes added (21 total; each checked against ALL prior units for first-occurrence
coverage, scholarship verified, XHTML with numeric character references):
- ch12 (+5, now 8): Amitabha 阿弥陀佛 (Pure Land invocation); the "white-duck"
  scapegoat 宰白鸭 (paid substitute-convict executed for another); pingtan 评弹
  (Suzhou storytelling-ballad, pipa/sanxian, storytelling houses); the Herd-Boy
  and Weaving-Maid stars 牵牛织女 (the Milky-Way lovers' legend); the top-graduate
  状元 / imperial examinations.
- ch13 (+6, now 9): the Romance of the Three Kingdoms 三国演义 as byword for
  stratagem; hemp-and-white deep mourning 披麻戴孝 (vs Western black); the Manchu
  queue 辫子 (compulsory Qing badge, cut after 1911); "aunt-mother" 姨娘 (the
  children's form of address for a father's concubine); 李代桃僵 (the plum dying
  for the peach; the substitution stratagem — first occurrence in the book, so
  the note lives here though REGISTER_PASS anticipated ch29; prose kept per T1);
  the bride-price 彩礼 (paid groom-to-bride, opposite a dowry).
- ch14 (+5, now 10): 救世渡人 (the Buddhist "ferry beings across" metaphor of
  A-Chu's creed); "building the Great Wall" 砌长城 (mahjong); 朝秦暮楚 "Qin by
  morning and Chu by nightfall" (fickleness, the rival Warring States); the Green
  and Red Gangs 青红帮 (real Shanghai secret societies, distinct from the invented
  Golden Dragon Society); the Yellow Springs 黄泉 (the underworld).
- ch15 (+5, now 8): the 嫡/庶 principal-wife/concubine child hierarchy and the
  ritual-mother 嫡母 / birth-mother 生母 relation; 忠孝节义 (the four cardinal
  virtues of a traditional schooling); the "yellow crane" 黄鹤 elegy (Cui Hao's
  Yellow Crane Tower); the Warlord Era 军阀混战; the disciple-pledge card 拜师帖.

Recurring subjects were cross-referenced, not re-noted: the Comintern and the
British/French concessions and Garrison Command (ch04/ch08/ch10); Tongji Hospital
and Longjing tea (ch07/ch08); the wife/concubine hierarchy and the Madams and
three-years mourning (ch01); the spirit-tablet, kowtow, burning paper money and
Qingming (ch07/ch09); the Xuantong reign and the Old Buddha (ch00/ch07); the Jiao
Guiying aria and the three-knives-six-holes penance (existing ch12/ch15 notes);
the Yellow Springs (noted at its first occurrence, ch14) where it recurs in ch15.
Notes NOT added where the scene already makes the point plain (福祸相依/否极泰来 and
子欲养而亲不待 are self-glossed inline; the side-gate/main-gate concubine funeral is
dramatized in the text) or the item is decorative rather than load-bearing (the
mandarin-duck/butterfly image in ch15, whose emblem is carried by the ch32 note).

Checks: per chapter, split_bilingual.py regenerated reading + data/zh; parity OK
(ch12 204, ch13 118, ch14 260, ch15 254); check_numbers 0 unresolved (data/noise.txt
unchanged, the one prose edit lost no quantity); straight-quote guard clean on all
four reading files; no source ">" line changed in any bilingual file. Spot-audit:
17 paragraphs (the one touched paragraph plus a spread of note-anchor paragraphs
across all four chapters) re-read against their source lines — no meaning drift,
every anchor verbatim, every note's claim matches the source.

Glossary/figures: no changes (this pass never re-romanizes or renames).

Build: out/On a Hair Trigger.epub rebuilt, 36 of 36 units translated, 191 notes.
qa_epub.py PASS (48 files, 42 documents, 7,082 paragraphs, 191 references = 191
bodies = 191 backlinks, all links resolve).

## Register pass R04 (ch16 to ch19) — 2026-08-04

Fourth execution batch of the register pass (REGISTER_PASS.md): style-only prose
revision plus footnote densification. Content frozen; no source ">" line touched,
no paragraph merged or split, names per glossary.json. Edit lists committed under
edits/ (ch16 to ch19). Book-wide notes 191 to 206.

Prose edits (15 total, all in ch16, all T4/T6 scare-quote de-cluttering; ch17-19
are ordinary/dialogue chapters in the ch01 mode whose prose already reads in the
target register, so every paragraph LEAVES):
- ch16: the mock final-exam "live-combat exercise" scene (p001-p061) is the T4
  example named in REGISTER_PASS. The source saturates it with 引号 marking
  pretense. Kept the establishing quotes — "shot" (p001), "live-combat exercise"
  + "wipe out" + "enemy" (p007) — and dropped the quotes on the later
  repetitions within the same scene: 弹无虚发/咒骂 (p001); 买/通行证/越狱/地狱
  figurative emphasis (p007); 救 (p010); 对手 (p011); 进攻 (p013); 死亡 (p016);
  敌人/人质 role-quotes already marked by "playing the" (p025); 要害 (p031);
  弹壳 (p034); 部队 (p056); 指挥部 (p057, p058, p061); 指挥官 (p060); 规范/
  医务所/兵/筛子 (p061). Words unchanged; only the quote marks removed.
- ch17, ch18, ch19: no prose edits. The tearoom confrontation and tea duel
  (ch17), A-Chu's interior deduction (ch18), and the ballroom/twin mix-ups (ch19)
  all read cleanly in register; their scare quotes mark genuine irony and citation
  (the fake "truth," the "gift" of severed limbs, the impostor "Xu Yuzhen," the
  nicknamed "roses") in scenes distinct from the ch16 exercise, so they stay.

Notes added (15 total; each checked against ALL prior units for first-occurrence
coverage, scholarship verified, XHTML with numeric character references):
- ch16 (+4, now 9): the snow-goose trace 雪泥鸿爪 (Su Shi, the fleeting mark of
  a vanished past); fabi 法币 (Nationalist paper legal tender, 1935 reform, used
  a little ahead of the 1932 scene); the comprador 买办 (a foreign firm's Chinese
  manager, and its political charge); the Eight-Nation Alliance 八国联军 and the
  1900 sack of Peking.
- ch17 (+7, now 13): the Central Special Branch 中央特科 (the CCP's Teke, the
  clandestine intelligence/security service — first occurrence in the book, so
  the note lives here rather than at its later recurrences); the Special Higher
  Police 特高科 (Tokkō); the Hongmen 洪门 brotherhood; the red apricot over the
  wall 红杏出墙 (adultery idiom); the four principles of Japanese tea 和敬清寂
  (wa-kei-sei-jaku, Sen no Rikyū); the named gongfu-tea pours 关公巡城/韩信点兵
  (Guan Yu / Han Xin); the sworn-brother rite 拜码头/开香堂拜把子.
- ch18 (+2, now 3): the Mencian filial-heir maxim 不孝有三无后为大 and the
  ancestral incense-fire 香火; the Buddhist fast-and-vow retreat 吃斋还愿 (timed
  to the murder). ch18 is a short, abstract interior monologue whose remaining
  cultural furniture (the concubine line, Cixi, ancestor worship, the twin/heir
  structure) is already noted earlier; densification kept deliberately light and
  coverage-driven, not padded.
- ch19 (+2, now 5): the elder-brother family hierarchy 长兄如父 (the eldest as
  stand-in father, the ground of the twins' contest); the gentleman-amateur's
  opera 票戏 and Peking opera as "national essence" 国粹.

Recurring subjects were cross-referenced, not re-noted: the September 18th
Incident (existing ch16/ch17 notes) and Doihara Kenji (existing ch17 note); the
concession system, Garrison Command, and Central Special Committee/Comintern
(ch04/ch08/ch10/ch12); the qipao (ch08); the French Park (ch10); the ballroom and
dance hostesses (first at ch06, so not re-noted at ch16/ch19); the Old Buddha /
Empress Dowager Cixi (ch07) behind ch18's palace-maid gift; the Yellow Springs
(ch14) recurring in ch17; the Seven-Step Poem (existing ch17 note) recurring
within ch18. Notes NOT added where the scene self-glosses (the TNT and gunpowder
history in ch16; the samurai belly-cutting in ch17) or the item is decorative
rather than load-bearing (Yixing/Tenmoku teaware, the Paramount, 红尘/red dust,
the moon-palace dew). The dragon-gate carp (鱼跃龙门) recurs in ch16 but first
appears in ch13 and so is left for a book-wide coverage sweep, not misplaced here.

Checks: per chapter, split_bilingual.py regenerated reading + data/zh; parity OK
(ch16 320, ch17 251, ch18 127, ch19 241); check_numbers 0 unresolved (data/noise.txt
unchanged, the quote-only edits lost no quantity); straight-quote guard clean on
all four reading files; no source ">" line changed in any bilingual file. Spot-audit:
all 14 edited paragraphs (ch16) re-read against their source lines — every edit is
a pure scare-quote-mark removal with words, numerals, names, and meaning preserved
verbatim, zero drift; the required establishing quotes ("shot", "live-combat
exercise", "wipe out", "enemy") confirmed retained; all 15 new note anchors verified
as unique verbatim substrings of the post-edit reading text, no HTML named entities.

Glossary/figures: no changes (this pass never re-romanizes or renames).

Build: out/On a Hair Trigger.epub rebuilt, 36 of 36 units translated, 206 notes.
qa_epub.py PASS (48 files, 42 documents, 7,082 paragraphs, 206 references = 206
bodies = 206 backlinks, all links resolve).
