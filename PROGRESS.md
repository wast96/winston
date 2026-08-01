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
