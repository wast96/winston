# PROGRESS — A Thousand Li of Rivers and Mountains (千里江山图), Sun Ganlu

The running per-batch log. Written as the work goes, not at the end.

## Setup

- Source EPUB: Shanghai Literature and Art Publishing House digital edition, reliable
  Unicode text, no OCR. The source carries no footnotes or endnotes of its own;
  every note in the build is the translator's.
- Ingest: 41 spine documents, 1 image (the cover only), 157,360 source characters
  (out/INGEST.md). data/src/ is regenerable and gitignored; re-run
  scripts/ingest_epub.py source.epub at the start of a fresh session to recreate it.
- Structure: book.json is the logical structure (epigraph, 34 titled chapters, a
  closing unsigned letter, a two-part appendix). Front matter in the spine is not a
  translation unit.

## Tooling notes (this batch)

- Added scripts/make_bilingual.py: assembles out/<id>_bilingual.md from the VERBATIM
  source lines (read straight from data/src) zipped with a JSON list of English
  paragraphs, so the source can never be mistyped and paragraph parity is enforced
  at build time. One source line maps to one English paragraph.
- Added check_noise.txt (project noise for check_numbers.py, pass with
  --noise check_noise.txt). It strips numerals that are names or idiom, not
  quantities: 牌九 (pai gow), 四散, 十足, 百货, 四合, 颠三倒四, 百叶, and the personal
  names 陈千元 / 陈千里 (which contain 千 = 1000).
- Patched scripts/check_numbers.py: (1) added teen ordinals (fifteenth, sixteenth,
  etc.) to WORD_NUM for lunar-calendar days; (2) gave the 十分 / 十几 noise patterns a
  negative lookbehind so they no longer eat the 十 out of a clock time such as 四十分
  (40 min) or 五十分 (50 min). This book is full of clock times; without the fix the
  check orphaned a stray ones-digit on every one of them.

## B01 = ch01–ch05 (epigraph, Dice, Longhua, Miss Tao, Xuanwu Lake)

Scope: the epigraph "1933: Around the Lunar New Year"; ch02 骰子 Dice; ch03 龙华
Longhua; ch04 陶小姐 Miss Tao; ch05 玄武湖 Xuanwu Lake. 15,918 source characters,
366 translated paragraphs (81 / 42 / 114 / 129; the epigraph is a title page only).

### Checks run and what they found

1. Faithful, complete quotation of the source. Each bilingual QC file quotes the
   source verbatim (copied by make_bilingual.py straight from data/src, not retyped).
2. Paragraph parity (check_structure --pairs): ch01 0/0, ch02 81/81, ch03 42/42,
   ch04 114/114, ch05 129/129. All OK.
3. Number invariant (check_numbers --noise check_noise.txt): all five 0 unresolved.
   Two GENUINE catches were fixed, not waived: ch02 had dropped "两侧 / both sides"
   (a real quantity smoothed away) and rendered "两个六点" as "the two sixes" where the
   checker could not see the numeral; both corrected in the prose. The rest of the
   flags were the checker's generic noise list colliding with clock times, game and
   idiom terms, and the name 陈千元; handled by the check_numbers patch and
   check_noise.txt above.
4. Note anchors (check_structure): 13 notes, 0 unresolved, headings uniform.
5. Blind double-translation (separate context) of four literary/argumentative
   passages (ch03 the Investigation-Section aside; ch04 Ling Wen on the man who
   jumped and on Long Dong / Winter; ch05 Ye Qinian on over-complicated plans; ch02
   the closing pork joke). The independent renderings matched mine in meaning. The
   one divergence was the blind translator guessing 取车 as "fetch his bicycle";
   in context Cui Wentai is a hired-CAR driver returning the car, so "car" (mine) is
   correct. No change needed.
6. Back-translation omission pass (separate context) on four passages (ch02 the
   traitor paragraph; ch05 the five-meters-from-the-teacher passage; ch04 the
   don't-drink-the-water defiance; the smuggled letter). Every clause of the source
   came back; no omissions or additions. The letter's euphemism 入院 ("entered the
   hospital", the cover word for imprisonment) is kept literal in the text and its
   real meaning is disclosed only by the secret-writing reveal, as in the source.
7. Random-sample deep audit: the ~11 paragraphs above (about 3% of the batch) given
   the full verbatim-quote / double-translation / back-translation treatment.
   Observed substantive error rate: 0.

### Notes added (13; numbered by the builder, continuous)

- ch02 (5): Fourth Avenue (四马路); Shanghai Municipal Council (工部局) and the
  jurisdiction problem; the film Cuckoo Soul Abroad (海外鹃魂) and Jin Yan; the
  Longhua garrison and the 1931 "Longhua Martyrs"; the 1933 China Merchants (招商局)
  embezzlement case with Li Guojie, Li Hongzhang, Chen Fumu and Du Yuesheng.
- ch03 (2): the KMT Party Affairs Investigation Section (党务调查科) / Special
  Operations Headquarters, forerunner of the 中统; the code name Xi Shi (西施).
- ch04 (3): the Emergency Law for Crimes Endangering the Republic (危害民国紧急治罪法);
  Haohan (浩瀚) and The Guide Weekly (向导); the May Thirtieth Movement (五卅运动).
- ch05 (3): Da Hong Pao (大红袍) rock tea; the Nineteenth Route Army (十九路军) and the
  January 28 Incident, with Commander Cai; Xuanwu Lake (玄武湖) and the Nanjing
  landmarks.

### Fact-checks against scholarship (rule 5)

- Longhua Martyrs, Feb 1931, at the Songhu Garrison Command site, including the Five
  Martyrs of the League of Left-Wing Writers: CORROBORATED (executedtoday; Wikipedia,
  "The Five Martyrs"). Sources differ on the count (23 vs the Chinese "24"); the note
  says "some two dozen" to avoid asserting a contested figure.
- 1933 China Merchants (招商局) embezzlement case: CORROBORATED (Chinese audit-history
  and Wikipedia on 李国杰). Li Guojie, grandson of Li Hongzhang, mortgaged Shanghai
  wharves (the Jinliyuan among them, the same wharf named in ch02) for a loan to an
  American firm and took a kickback; Chen Fumu was a go-between and fled; a Shanghai
  court gave Li eight years in April 1933; Du Yuesheng and the Hatchet Gang's killing
  of the company's Nanjing-appointed director figure in the affair. The novel's
  detective gossip tracks the record.
- Film Cuckoo Soul Abroad (海外鹃魂), a Lianhua production starring Jin Yan with
  Ziluolan: CORROBORATED (Chinese-Wikipedia 金焰; Lianhua filmographies).
- Nineteenth Route Army and the January 28 Incident (1932); Emergency Law of 1931;
  党务调查科 as forerunner of the 中统; The Guide Weekly as the CCP organ of the 1920s;
  Xi Shi of Yue: standard reference facts, stated with due modesty.

### Glossary rows added

Populated glossary.json as the term ledger: people (fictional cast + the historical
figures footnoted), organizations, places, and terms. One rendering per referent,
decided before romanizing. Statuses: fictional names "decided" (standard pinyin);
established English names and real history "attested"; one "provisional" (普恩济世路 /
Pu'enjishi Road, my romanization, which the build marks visibly). Settled per the
kickoff: Longhua (龙华) as district + garrison + prison + pagoda + 1931 martyrs.
Also settled: 军法处 = "the Judge Advocate's office" (its head rendered "Director");
世界大旅社 = "the World Hotel"; 兰心大戏院 = "the Lyceum Theatre"; 侦缉队 = "the
detective squad"; 特工总部 = "the Special Operations Headquarters".

### Figures

None. The source has one image (the cover); no in-text figures in this batch.
figures.json stays empty.

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 5 of 37 chapters translated,
13 notes. qa_epub.py: PASS (47 files, 42 documents; 13 references = 13 bodies = 13
backlinks; all links resolve).

### Flagged for the read-through

- 陶小姐 / Miss Tao is left as "Miss Tao" (her role name); Xu Zhenya (徐枕亚) she
  name-drops is glossed in the ledger but not footnoted, to avoid over-annotating.
- The publisher discrepancy (上海文化 vs 上海文艺) is still open for the colophon.
- Provisional English titles for later chapters remain to be settled as they arrive
  (Garrick, Jiaoli, Xiaotaoyuan, The Tanglong Door, The Guisheng).

## Batch B02 (ch06 Identity, ch07 Old Fang, ch08 The Race Ticket)

### Translation

- 255 paragraphs (ch06 54, ch07 135, ch08 66), each one English paragraph per source
  paragraph. Built with make_bilingual.py (verbatim source lines) then split_bilingual.py.
- The prison letter and the "dice are out / there is a traitor" secret-writing line
  recur here from ch05; rendered verbatim identical to ch05 for consistency.

### Checks run and what they found

- Paragraph parity (check_structure.py): ch06/07/08 all OK (54/135/66 both sides).
- Number invariants (check_numbers.py --noise check_noise.txt): clean after adding to
  the noise list 四下 ("on all sides"), 第二天 ("the next day"), 年三十 (New Year's Eve
  date-name), 四川 (Sichuan, in 北四川路), and 二(?=岁) (the stray 二 the built-in 十多
  rule orphans out of 二十多岁). Money in jiao/fen (五角, 两角五分) was rendered in cents
  and passed on the existing idiom coverage; no real quantity was dropped.
- Blind double-translation (two subagents, separate contexts) on the argumentative and
  literary passages of all three chapters: no meaningful divergence from the delivered
  text, no ambiguity flags. Confirms the readings.
- Back-translation omission pass (subagent, English to Chinese, sample across the three
  chapters): matched the source with no additions or omissions.
- Consistency with scholarship (five subagents; Wikipedia, Baidu Baike, academic and
  government sources; never Grok/Grokipedia): the footnote apparatus below.
- Random-sample deep audit: the Lenin passage Chen Qianyuan is translating was traced
  to the opening of "Letters from Afar" (First Letter, 1917) and set to the Collected
  Works wording; the reused letter checked verbatim against ch05.

### Footnote apparatus (expanded at the commissioner's request)

- Grew from 13 notes to 46, across ch02 through ch08, each fact-checked and labelled
  corroborated / uncorroborated / contradicted, and saying whether a person, place or
  event is real or the novel's invention.
- Real vs fictional established: the principals are invented against a real 1933 backdrop;
  the appendix frames the book as homage to the real Longhua martyrs. Notable findings:
  the garrison's "32nd Army" is the novel's own (the real NRA 32nd Army was in Hebei) and
  is flagged contradicted; "Bao'en Pagoda" is a genuine traditional alternate name of the
  Longhua Pagoda, not an error; the "World Hotel" is undocumented (likely the novel's) on
  a real streetscape; the Four Banks' Savings Society building is the Park Hotel; the
  Zhejiang, Grand and (rebuilt) buildings are Hudec's; the Turandot poster line paraphrases
  the Act I executioner chorus (the San Carlo company is real, its 1933 Carlton run
  unconfirmed). Ling Wen's novel "Winter" is a book within the book.
- glossary.json expanded with the B02 referents; real figures/places moved to "attested"
  with the fact behind them, fictional cast marked as such; three provisional street names.

### Structure and typography (commissioner queries)

- ch01 "1933 / Around the Lunar New Year" was rendering as a content-less chapter. It is a
  front epigraph, not a chapter: it is absent from the source's own table of contents, and
  no other chapter carries such a lead-in. Reframed as kind:"epigraph" in book.json; the
  builder now renders it centered and lists it as an epigraph, excluded from the chapter
  tally (now 36 chapters).
- Scene rhythm: the digital source marks NO scene breaks typographically (every paragraph
  is one style). It heads some scenes with terse time/place lines and hard-cuts the rest.
  Added scenes.json, which drives (a) centered "datelines" for the source's own scene-header
  lines and (b) centered scene breaks before hard cuts that have no dateline. B01 chapters
  updated too (ch02 three datelines and seven breaks; ch04 two; ch05 three; ch07 two).
  Editorial typography only: no word added, dropped, or changed.
- build_reading_epub.py patched for datelines, scene breaks and the epigraph, plus a
  reader-facing translator's note (real/fictional framing and the typography convention)
  supplied via book.json "translator_note".

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 8 of 37 units translated (epigraph +
ch02-ch08), 46 notes. qa_epub.py: PASS (47 files, 42 documents; 46 references = 46 bodies =
46 backlinks; numbering sequential in reading order; all links resolve).

## Batch B03 (ch09 The Photograph, ch10 The Clinic, ch11 The Tenant)

### Translation

- 255 paragraphs (ch09 69, ch10 104, ch11 82), one English paragraph per source paragraph.
  Built with make_bilingual.py (verbatim source lines) then split_bilingual.py.
- ch10 carries a formal classical business letter (safe-deposit box notice); rendered in a
  starched epistolary register to mark the source's own shift out of narrative prose, and
  footnoted as such. Every numeral/date in it (本月十日, 二七九号, 三月十一日) preserved.

### Checks run and what they found

- Paragraph parity (check_structure.py --pairs): ch09 69/69, ch10 104/104, ch11 82/82, OK.
- Number invariants (check_numbers.py --noise check_noise.txt): all three 0 unresolved.
  Added to the noise list the personal/place names that carry a digit but are not
  quantities: 吴四宝 (Wu Sibao) and 三成坊 (Sancheng Fang, a lane name). One GENUINE
  tokenizer fix, not a waiver: the built-in idiom stripper 一[日夜时…] was eating the 一
  out of the real date 十一日 (mis-reading March 11 as "10"); gave it a negative lookbehind
  (mirroring the existing 十分 guard) so 十一日 parses as 11, and registered the ordinal
  "eleventh" in WORD_NUM. Verified the change is conservative (standalone 一日/一时 idioms
  still stripped; 十一日/二十一日 now correct). No real quantity was waived.
- Note anchors: 22 new notes (+1 retro on ch07), all anchors verbatim substrings, builder
  accepted them (it refuses on an unmatched anchor); qa_epub sequential numbering PASS.
- Blind double-translation (three subagents, separate contexts, one per chapter, blind to
  the delivered text): independent renderings matched mine in meaning throughout. The only
  divergences were the blind translators mis-identifying two romanized road names
  (善钟路 as "Chungking Road", 赵主教路 as "Route Père Robert") — my safe pinyin renderings
  and the fact-checked glossary are correct; no change needed.
- Back-translation omission pass (subagent, English to Chinese, all three chapters): came
  back a faithful mirror of the source, no omissions or additions. Its "verify" flags
  (the balalaika passage, the burn scar, the letter's numbers, Detective Yao vs Captain You
  as distinct men, 小董/Young Dong, 好汉/Haohan, the Zhaojiabang/Li Han insert) were each
  checked against the source and confirmed faithful.
- Random-sample deep audit: the balalaika/Hongkou memory (ch09) and the letter scene (ch10)
  given the full verbatim-quote / double-translation / back-translation treatment.
  Observed substantive error rate: 0.

### Footnote apparatus (rich, fact-checked; five research subagents, web sources only)

- Grew from 46 to 69 notes. New notes: ch07 (1, retro) 铺保 surety bond; ch09 (8) the April
  Twelfth 1927 massacre, Wu Sibao (a real Green-Gang/No.76 figure the novel plants as a
  minor tenant), the 兔子不吃窝边草 proverb, 二房东 second landlord, the 1930-31 AB-Corps /
  Futian internal purges behind "we've paid a bitter price", Hongkou Park (today Lu Xun
  Park), Tumbalalaika/balalaika, the Leica; ch10 (5) the Zhonghui Bank (Du Yuesheng's, with
  a real safe-deposit vault), Guanshengyuan, the letter's epistolary register, the (likely
  fictional) Rentai Bank, the provisional Party branch; ch11 (9) the 邋遢冬至清爽年 proverb,
  Jing'an Temple and the New-Year first incense, 水门汀 (cement loanword), Zhaojiabang creek,
  Massenet Road (today Sinan Road), the road cluster (Haige/Shanzhong/Zhaozhujiao with their
  present-day names), Red China + Third Counter-Encirclement Campaign, Old Bolshevik, the
  Tiangu Estate. Each labelled real-vs-fictional and corroborated/uncorroborated.
- Sources: Wikipedia, Baidu Baike, academic/government pages; NO Grok/Grokipedia (a research
  agent flagged Grokipedia surfacing for Tumbalalaika and deliberately did not use it).
- One correction caught and applied: 赵主教路's present-day name is 五原路 (Wuyuan Road, after
  Bishop Maresca), NOT Shaanxi South Road as one draft suggested.

### Glossary rows added

- people: 吴四宝 (attested, real figure), 吴作民 / Assistant Manager Wu, 金德林 (fictional).
- organizations: 中汇信托银行 (attested), 仁泰银公司 (likely fictional), 东陆经租处 (fictional),
  冠生园 (attested).
- places: 马立斯新村, 虹口公园, 静安寺, 同福里, 三成坊, 田谷邨 (provisional), 愚园路, 地丰路,
  海格路, 善钟路, 赵主教路, 马斯南路, 肇嘉浜 — real roads "attested" with their present-day names.
- terms: 二房东, 四一二, 老布尔什维克, 水门汀, 巴拉莱卡, 第三次反围剿, 邋遢冬至清爽年.

### Scene typography

- ch09, ch10, ch11 are each a single continuous scene (an evening at Ling Wen's; an afternoon
  at the clinic; Wei Dafu's afternoon and the meeting), with no terse time/place header lines
  and no hard cuts. Added scenes.json entries with empty datelines/breaks (as ch06/ch08).

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 11 of 37 units translated (epigraph +
ch02-ch11), 69 notes. qa_epub.py: PASS (47 files, 42 documents; 69 references = 69 bodies =
69 backlinks; numbering sequential in reading order; all links resolve).

## Batch B04 (ch12 A Letter from Afar, ch13 The Revolving Door, ch14 New Year's Eve)

259 source paragraphs translated (ch12 106, ch13 83, ch14 70). All apparatus in footnotes,
never inline; the novel's own voice kept (Chen Qianli's reunion with his brother; Ye Qinian's
cold meditation at the Cathay; Cui Wentai's self-justifying backstory, including the source's
mid-paragraph slip into accusatory second person, which the translation preserves).

### Checks run and results

- Faithful verbatim quotation: bilingual QC files built by make_bilingual.py, which reads the
  source lines VERBATIM from data/src/ and refuses on any paragraph-count mismatch. Built clean
  at 106 / 83 / 70 pairs.
- Paragraph parity (check_structure.py --pairs): ch12 106=106, ch13 83=83, ch14 70=70, all OK.
- Numeral invariants (check_numbers.py --noise check_noise.txt): all three chapters 0 unresolved
  after two kinds of fix. (a) Non-quantity numerals added to check_noise.txt: bare given names
  千元/千里, weekday families 星期[一二三四五六] and 礼拜[一二三四五六], idioms 目迷五色 / 一不做二不休,
  八角形, 两下, 零星, the unit name 二十六军, the personal name 小五子. (b) Two loose 两 ("these two
  years" / "these two days") rendered with "two" so the count is honest, and the compound
  date-ordinals the checker could not parse (twentieth / twenty-first / twenty-second, for 民国二十年
  and 腊月二十一 / 二十二) added to WORD_NUM in check_numbers.py. No real quantity was waived.
- Blind double-translation (check 2): a subagent, given ONLY the source and forbidden to read out/,
  independently re-translated the ten hardest argumentative/literary passages across the three
  chapters. It reached the same readings on every one, including the three-person countersign, the
  seventy-two transformations allusion, the "a judge said it" aphorism, Ye Qinian dying-for-nothing
  reflection, and Cui Wentai's second-person self-indictment. No substantive divergence.
- Back-translation omission pass (check 3): a second subagent, given ONLY the English and forbidden
  to read data/, rendered the same ten passages back into Chinese. Round-trip reproduced every
  clause of the source with no omission or addition.
- Deep audit (check 8): the ten passages above are about 4% of the batch and got the full paranoid
  treatment (verbatim quote, double translation, back-translation). Observed substantive error rate: 0.
- Fact-check against scholarship (check 7): four research subagents with web access, reputable
  sources only (Wikipedia, Baidu Baike, Chinese Party-history / government outlets, Yad Vashem /
  Jewish-history institutions); NO Grok / Grokipedia / AI sources. Every note labelled real-vs-
  fictional and corroborated / uncorroborated / contradicted. Three honest hedges recorded in the
  notes: Nekrasov's "The Storm" is a love lyric, not a revolutionary poem (the novel re-weaponizes
  it); 少山 is a genuine Zhou Enlai alias but Zhou had left Shanghai by late 1931, so the early-1933
  use is literary; and the "肚皮上有一只蟹" mishearing of "I Belong to Your Heart" is untraceable in
  the reliable record (marked uncorroborated).

### Footnote apparatus (rich, fact-checked)

- Grew from 69 to 90 notes. ch12 (9): Tilanqiao Prison, the Hongkou foreign/Jewish quarter that
  predates the 1938 refugee ghetto, tingzijian, Ye Tao (first appearance, fictional), Nekrasov and
  "The Storm", Comrade Shaoshan (a real Zhou Enlai alias), Duoyunxuan and the peach-blossom / 桃 pun,
  Esperanto and Chinese anarchism, rice-water invisible ink. ch13 (8): the abolished-calendar campaign,
  the Cathay Hotel / Sassoon, Bernard Shaw's Feb 1933 Shanghai visit and Hong Kong speech, the Monkey
  King's seventy-two transformations, the disputed youth-and-revolution aphorism, the "crab on your
  belly" mondegreen (uncorroborated), Chen Lifu ("Mr. Lifu"), Bo Gu / Qin Bangxian and the Provisional
  Central's move to Ruijin. ch14 (4): the workers' pickets, the Twenty-Sixth Army and the April 12
  disarming, the 1931 floods and cholera (toll given as a range), the Shanghai New Year's-Eve dishes.

### Glossary rows added

- people: 叶桃 Ye Tao, 小五子 Xiaowuzi (fictional); 少山 Shaoshan, 秦邦宪 Qin Bangxian, 陈立夫 Chen Lifu,
  沙逊 Sassoon, 涅克拉索夫 Nekrasov (real). 崔文泰 note updated to record the ch14 reveal that he is "Xi Shi".
- organizations: 云禄车行 (fictional), 红色中华, 工人纠察队, 临时中央 (attested).
- places: 提篮桥监狱, 华懋饭店, 澄衷中学, 下海庙, 新闸路, 仁记路, 外滩, 黄浦江, 董家渡, 奉贤, 瑞金 (attested).
- terms: 亭子间, 世界语, 朵云轩, 特派员, 北伐, 废历.

### Scene typography

- ch12 is one continuous scene (the reunion in the tingzijian, flashbacks woven in): empty datelines
  and breaks. ch13 has one hard cut, at the turn from the Cathay to the riverside meeting with Cui
  Wentai (break anchor "As You Tianxiao was getting into the car on Renji Road"). ch14 has one, at the
  closing coda outside in the dark (break anchor "The street blazed with light"). All anchors verified
  against the reading files.

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 14 of 37 units translated (epigraph + ch02-ch14),
90 notes. qa_epub.py: PASS (47 files, 42 documents; 90 references = 90 bodies = 90 backlinks; numbering
sequential in reading order; all links resolve).
