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
