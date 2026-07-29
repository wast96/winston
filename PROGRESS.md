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

## Batch B05 (ch15 Code Words, ch16 The Bank, ch17 The Suitcase)

217 source paragraphs translated (ch15 85, ch16 72, ch17 60). All apparatus in footnotes, never
inline; the novel's own voice kept: Lin Shi's solitary reflection and Chen Qianli's exposition of
the whole "Thousand Li of Rivers and Mountains plan" (ch15); Ye Qinian's reverie on the walk to the
bank and Cui Wentai's garrulous Wang Jinzhi anecdote (ch16); the rapid cross-cut heist, Ye Qinian's
ideological-cleansing speech, and Cui Wentai's last-second double reversal, "I'm going over to
nobody, I'm going over to myself" (ch17). This batch turns the plot: the title painting is spoken
aloud for the first time as the underground's passphrase, and Cui Wentai bolts with the gold.

### Checks run and results

- Faithful verbatim quotation: bilingual QC files built by make_bilingual.py (reads data/src/ lines
  VERBATIM, refuses on any paragraph-count mismatch). Built clean at 85 / 72 / 60 pairs.
- Paragraph parity (check_structure.py --pairs): ch15 85=85, ch16 72=72, ch17 60=60, all OK.
- Numeral invariants (check_numbers.py --noise check_noise.txt): all three chapters 0 unresolved.
  Fixes: (a) three non-quantity numerals added to check_noise.txt as idioms/names -- 退一万步
  ("even supposing"), 百褶 (pleated skirt), 千金 (千金之裘, "worth a fortune"). (b) three real counts
  rendered explicitly so the count is honest, not waived: 两位同志 -> "the two comrades", 前后两扇门
  -> "the two doors, front and back", 四壁 -> "the four walls". No real quantity waived.
- Blind double-translation (check 2): a subagent in a separate context, given ONLY the source
  Chinese of six argumentative/reflective passages (the lone-mission aphorism; Chen Qianli's plan
  exposition and the four-courier-lines paragraph; Ye Qinian's reverie; the meditation on the dead
  and the living in single-line contact; Ye Qinian's ideological-cleansing speech), translated them
  fresh. Reached the same readings on every one; no substantive divergence. It independently rendered
  四条秘密交通线 as "four secret transport lines", confirming the source really says four (footnoted
  against the documented three).
- Back-translation omission pass (check 3): a second subagent, given ONLY the English of six passages
  and forbidden data/, rendered them back into Chinese. Round-trip reproduced every clause of the
  source with no omission or addition (only artifact: it wrote the alias 少山 as the homophone 韶山).
- Deep audit (check 8): the twelve passages above are about 5% of the batch and got the full paranoid
  treatment (verbatim quote, double translation, back-translation). Observed substantive error rate: 0.
- Fact-check against scholarship (check 7): four research subagents with web access, reputable sources
  only (Palace Museum / dpm.org.cn, Wikipedia, Baidu Baike, PRC Ministry of Defense and People's Daily
  Party-history pages, university libraries); NO Grok / Grokipedia / AI sources. Every note labelled
  real-vs-fictional and corroborated / uncorroborated / contradicted. Honest hedges recorded: the
  courier-line "four" is the novel's count against the documented three (Central Red Route); the
  貂爪仁 "under-the-claw" fur is the novel's likely embellishment on real pieced-fur practice; the
  Wang Jinzhi murder case is unattested and appears to be the novel's invention (its Taikoo-steamer
  setting is real); "Professor Tao" is Tao Xisheng, real, but no 1933 anti-Communist primer by him is
  documented (his hard anti-Communist role is later); the "Mr. Song" / Ministry-of-Finance-bonds hint
  is footnoted as an invited reading toward the Soong family (T. V. Soong, finance minister 1928-33),
  not stated by the text.

### Footnote apparatus (rich, fact-checked)

- Grew from 90 to 108 notes. ch15 (6): the storming of the Soviet consulate at Guangzhou (Dec 1927);
  the painting A Thousand Li of Rivers and Mountains (Wang Ximeng, 1113, Palace Museum) -- spoken here
  first, as the passphrase, and the plan named for it; the August 7th Conference (Hankou, 1927); the
  jianren civil-service rank; the CCP courier lines / Central Red Route (Shanghai-Shantou-Ruijin), with
  the three-vs-four note; the Canton-Hong Kong Strike (1925-26). ch16 (7): marten-paw fur (real pieced-
  fur practice, this category the novel's); the ABC of Communism (Bukharin/Preobrazhensky, 1919); Tianjin
  Road as bank street; native banks (qianzhuang); "big yellow croaker" gold-bar slang; Seward Road (->
  Changzhi Rd, 1943); the Wang Jinzhi case (unattested) with the real Taikoo / China Navigation Co. ch17
  (5): the gendarmerie and armored cars; the Ministry-of-Finance-bonds / Soong-family hint; the Nanshi
  police and Shanghai's three police forces; the Three Principles of the People; Professor Tao (Tao
  Xisheng).

### Glossary rows added

- people: 小施 Little Shi, 纪先生 Mr. Ji (Chen Qianli's bank alias), 王金枝 Wang Jinzhi (all fictional);
  陶希圣 Professor Tao, 宋子文 T. V. Soong (real).
- organizations: 裕记钱庄 (fictional); 南市警察署, 太古 Taikoo (real).
- places: 天津路, 熙华德路, 江西路, 汕头, 武汉, 杭州 (real); 阜成里, 逸园咖啡馆 (likely fictional).
- terms: 大黄鱼, 钱庄, 估衣铺, 简任, 八七会议, 省港大罢工, 三民主义, 共产主义ABC, 中央红色交通线 (real);
  貂爪仁 (the novel's embellishment).

### Scene typography

The source carries no dividers. ch15 has 2 hard cuts (to the firecracker street / Chen Qianli's
arrival; to the downstairs parlor). ch16 has 4 (Ye Qinian leaves the Cathay; the Cui Wentai
midnight-call flashback; Lin Shi and Ling Wen at the clinic; the car to the bank). ch17 has 7 -- a
rapid heist montage cross-cutting the vault, the Yiyuan Cafe, the Yuji command post, Little Shi's
desk, the bank hall and the street. All 13 break anchors verified against the reading files and
confirmed rendered in the built EPUB (ch15 2, ch16 4, ch17 7). No datelines in this batch.

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 17 of 37 units translated (epigraph + ch02-ch17),
108 notes. qa_epub.py: PASS (47 files, 42 documents; 108 references = 108 bodies = 108 backlinks;
numbering sequential in reading order; all links resolve).

## Batch B06 (ch18 The Maochang Coal Company, ch19 February, ch20 The Xingchang Apothecary)

190 source paragraphs translated (ch18 54, ch19 48, ch20 88). All apparatus in footnotes, never
inline; the novel's own voice kept. ch18 is Chen Qianli's after-action reconstruction -- how the
dying Old Fang's half-written 山, screened behind a drainpipe, pointed at the traitor's surname
崔 (Cui) -- folded into the group's flight to the Zhaojiabang coal yard and Lin Shi's opening
address on the national situation. ch19 turns to Ling Wen: her arrest and rescue after the Great
Revolution, the bookshop where Yi Junnian first approached her over Rou Shi's novel February, and
her taking command of the Guangzhou leg. ch20 crosses to Guangzhou -- a dense travelogue of real
places -- where Mrs. Mo tells the story of the tall stranger who once saved her (taken for Long
Dong), and a Ruijin courier, Old Xiao, carrying a secret oral order for the absent Lin Shi, must
decide whether to entrust it to Ling Wen.

### Checks run and results

- Faithful verbatim quotation: bilingual QC files built by make_bilingual.py (reads data/src/ lines
  VERBATIM, refuses on any paragraph-count mismatch). Built clean at 54 / 48 / 88 pairs.
- Paragraph parity (check_structure.py --pairs): ch18 54=54, ch19 48=48, ch20 88=88, all OK.
- Numeral invariants (check_numbers.py --noise check_noise.txt): all three chapters 0 unresolved.
  Fixes: (a) seven non-quantity numerals added to check_noise.txt as names/idioms -- 十足十 ("done
  to perfection", placed before 十足), 十七甫 (Shiqifu, a Guangzhou lane), 五味子 (schisandra) and
  五指毛桃 (hairy fig-root, herb names), 八婆 (Cantonese "gossip") and 两公婆 (Cantonese "married
  couple"). (b) "thirteenth" added to WORD_NUM for 老开 = 第十三张牌 (the King, the 13th card).
  (c) real counts kept honest, not waived: 两天 rendered "two days", the clock times 半夜十二点 and
  十二点前 rendered "twelve midnight" / "twelve o'clock" so the 12 survives. No real quantity waived.
- Blind double-translation (check 2): a subagent in a separate context, given ONLY the source
  Chinese of four argumentative/literary passages (the 山/崔 blood-clue; Lin Shi's political speech
  on Ninghan/Ningyue and political tutelage; Wei Dafu's physiognomy insult; Old Xiao's cipher-and-
  wireless reasoning), translated them fresh. Reached the same readings on all four; no substantive
  divergence (it independently rendered 脑后见腮/反骨 as jowls jutting past the back of the head and
  a rebel's bone, and 豪密 as a plain-code base worked by addition and subtraction, matching the note).
- Back-translation / faithfulness audit (check 3): a second subagent, given six source+English pairs
  across all three chapters, found every pair faithful -- no omission, no invented bridging, no number
  or name error. Two micro-notes: 中央交通局 rendered "the Central Committee's Liaison Bureau" (adds
  "Committee's", historically accurate and consistent with how 中央 is handled book-wide); and 极易出
  现意外情况 was first rendered "ran the greatest risk of the unforeseen" -- tightened to "very readily
  met the unexpected" to match 极易.
- Deep audit (check 8): the ten passages above are roughly 5% of the batch and got the full paranoid
  treatment (verbatim quote, double translation, back-translation/audit). Observed substantive error
  rate: 0.
- Fact-check against scholarship (check 7): four research subagents with web access, reputable sources
  only (Wikipedia EN/ZH, Baidu Baike, PRC government / Party-history and university pages, Britannica,
  a peer-reviewed climate journal); NO Grok / Grokipedia / AI sources. Every note labelled
  real-vs-fictional and corroborated / uncorroborated / contradicted. Honest hedges recorded: the
  first-edition cover of February was a Tao Yuanqing LINE DRAWING, not the woodcut the novel describes
  (the note says so); the People's Palace was funded from seized SMUGGLER money, not the opium-boat
  fines Mrs. Mo names (noted); the strike Labour College and Deng Zhongxia are real but the college's
  siting on the Nanhua Building's fourth floor is the novel's detail; the Hao cipher's "pattern from
  overuse" is Old Xiao's own reasoning, not a recorded break; the captured high-power radio telescopes
  the 1930 Longgang "half radio" and the 1931 second-campaign 100-watt set into one; Zhu Huiri is a
  real Guangzhou police chief (from Oct 1927), his exact 1933 tenure undocumented; Lu Zhongde and
  Ouyang Min appear to be the novel's invention.

### Footnote apparatus (rich, fact-checked)

- Grew from 108 to 130 notes. ch18 (5): the French Concession Municipal Council (公董局, distinct from
  the SMC); the 山/崔 blood-clue (a name legible only in the script); the 脑后见腮/反骨 physiognomy
  allusion (Zhuge Liang reading Wei Yan's "bone of rebellion" in the Three Kingdoms); the Ninghan /
  Ningyue mergers and the declaration of political tutelage (训政); the playing-card code names (Laokai
  = the King, the 13th card). Redundant candidates dropped: the 1931 floods (already noted at ch14),
  the Zhaojiabang (ch11), the Special Operations Headquarters (ch03). ch19 (4): Rou Shi's novella
  February -- Chunchao Book Company 1929, Lu Xun's preface, its widow-and-two-children story, and Rou
  Shi himself a Longhua martyr shot 7 Feb 1931, the same ground and month as this book; the cover
  discrepancy (a Tao Yuanqing line drawing, not the novel's woodcut); the Relief Society (济难会 / China
  Red Aid, which really hired lawyers to bail out arrested comrades); the stove-cat idiom (煨灶猫). The
  Great Revolution was NOT re-noted (glossed and first appears at ch07; the 1927 collapse is covered by
  the ch09 April Twelfth note). ch20 (13): Dashatou Station (Canton-Kowloon east terminus); Deng
  Zhongxia and the strike Labour College; Chen Jitang's Guangdong; the Sincere Company rooftop; Shamian
  (short, cross-referencing the ch15 Shaji-shooting note); Lingnan architecture (竹筒屋/骑楼/满洲窗); the
  People's Palace; the 吊钟花 / Shuangmendi flower market; the Hao cipher (豪密, Zhou Enlai/Wu Hao); the
  captured high-power radio and the Shanghai-Ruijin link; Zhu Huiri; the Guangzhou Republican Daily;
  Lu Zhongde / Ouyang Min (fictional).

### Glossary rows added

- people: 莫少球 Boss Mo, 莫太太 Mrs. Mo, 老肖 Old Xiao, 卢忠德 Lu Zhongde, 欧阳民 Ouyang Min (all
  fictional); 邓中夏 Deng Zhongxia, 陈济棠 Chen Jitang, 朱晖日 Zhu Huiri, 柔石 Rou Shi, 陶元庆 Tao
  Yuanqing (real).
- organizations: 济难会 the Relief Society, 劳动学院 the Labour College, 公董局 the French Concession
  Municipal Council, 先施公司 the Sincere Company, 广州民国日报 the Guangzhou Republican Daily (all real).
- places: 沙面 Shamian, 大沙头 Dashatou, 顾家宅公园 Gujiazhai Park, 平民宫 the People's Palace, 浆栏街
  Jianglan Street, 双门底 Shuangmendi, 高第街 Gaodi Street (real); 茂昌煤号 the Maochang Coal Company,
  兴昌药号 the Xingchang Apothecary, 添男茶楼 the Tiannan Teahouse, 南华楼 the Nanhua Building (settings).
- terms: 二月 February (Rou Shi's novella), 吊钟花 hanging-bell flower, 竹筒屋 bamboo-tube house,
  满洲窗 Manchu windows, 骑楼 arcade, 豪密 the Hao cipher (real); 煨灶猫 stove-cat (idiom).
- Rendering consistency settled against earlier chapters: 交通站 = "liaison station", 交通局 =
  "Liaison Bureau", 机要交通员 = "secret courier" (aligned with 特工总部 = "the Special Operations
  Headquarters" from ch03; ch18's first-draft "Special Services Headquarters" was corrected).

### Scene typography

The source carries no dividers. ch18 has 3 hard cuts (Chen Qianli's after-action reconstruction; the
Gujiazhai-Park safe house; the walk to the coal yard). ch19 has 2 (Ling Wen's flashback to her arrest
and the bookshop; the return to the present as Chen Qianli opens the inner-room door). ch20 has 0 --
one continuous Guangzhou afternoon. All 5 break anchors verified against the reading files and
confirmed rendered in the built EPUB (ch18 3, ch19 2, ch20 0). No datelines in this batch.

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 20 of 37 units translated (epigraph + ch02-ch20),
130 notes. qa_epub.py: PASS (47 files, 42 documents; 130 references = 130 bodies = 130 backlinks;
numbering sequential in reading order; all links resolve).


## Batch B07 (ch21 The Tanglong Door, ch22 The Tiannan Teahouse)

### Translation

ch21 (161 paragraphs) and ch22 (56 paragraphs), 217 in all. These are the hinge chapters.
ch21: Ling Wen, on the pretext of the mission, hunts Guangzhou's newspaper archives and the
crime-scene house (No. 23, the Rear Street of Tianguan Li, on Haoxian Road) for a trace of
Long Dong, who vanished after the 1929 raid. Yi Junnian, cold and sleepless, is unnerved by
her groundless intuitions and by the feeling that a dead Long Dong is watching him. The
distinctive tanglong door, and a photograph he once showed her, break the memory open: he
swore his Party oath in that house with Long Dong as his sponsor, then killed him and took the
picture. He murders Ling Wen off-page (only the blood on his hands, wiped on a torn door
couplet, tells it) and strangles the blind diviner who recites an oracle naming "Xi Shi" to
his face. ch22: Old Xiao, the Ruijin secret courier carrying an oral order about Comrade
Haohan's safety, is ambushed at the Tiannan Teahouse, escapes a first cordon, is cornered in
a Xiguan back-lane, and is "rescued" by a bicycling Yi Junnian, who shoots the detective-squad
men and carries the wounded courier to a Tanka boat. The rest is Yi Junnian's own history: he
is the original "Xi Shi," Ye Qinian's ace, planted in the Shanghai underground under a dead
man's name, and he wants the secret in Old Xiao's head. The whole teahouse ambush was a piece
he staged, killing the enemy's own men to buy the courier's trust.

The novel's own voice kept throughout: novelistic and close third; the newspaper clipping in
ch21 rendered in a stiffer Republican officialese to hold the enemy-press register, with the
KMT term for 1927 (广州暴动) set as "the Guangzhou revolt," distinct from the Party's "Guangzhou
Uprising." 爱人 rendered "lover" (Long Dong is Ling Wen's secret lover; her dead husband was a
merchant). Cantonese texture preserved where it lands (fo sui, one cup and two plates, the
tanglong door, wok-ear gables) and footnoted where it cannot survive.

### Checks run and results

- Verbatim source quotation: guaranteed by make_bilingual.py, which reads the source lines
  straight from data/src/ and enforces paragraph parity. ch21 161 = 161, ch22 56 = 56.
- check_numbers.py (with --noise check_noise.txt): both chapters clean. Flags resolved were
  street names (十八甫, 下九甫), reduplicated and set-phrase numerals (四四方方 / 四方, 两样),
  the amah's name (七姑), and 九龙 / 零散 / 零碎, all added to check_noise.txt as non-quantities.
  Real quantities were kept as figures so they survive the check: 中午十二点 as "twelve o'clock",
  二楼 as "second floor", 二十五万 as "two hundred and fifty thousand", 十一天 as "eleven days".
  Two principled parser fixes were made in check_numbers.py: a negative lookbehind on the
  一[天次年...] measure-word stripper (so a teen-plus-measure like 十一天 keeps its 11 instead of
  orphaning 十 as 10), and a "<ones> hundred and <tens> thousand" composite in spelled_numbers
  (so 二十五万 = 250000 is recognized). Both were regression-checked against ch18, ch19 and ch20,
  which still pass.
- check_structure.py: paragraph parity OK for both (161 and 56).
- Blind double-translation (subagent, separate context) on five argumentative/literary passages
  (the windowless-room speech, the oracle couplet, the gold-mine / Xi Shi reveal, Ye Qinian's
  1924 prophecy, the staged-ambush bargain): independent renderings agree closely with the
  shipped text. The only real divergence is the oracle's 郭素, which the blind translator read
  variously (as a name, or literally); this is a genuine source ambiguity, now flagged in the
  footnote (the source writes 郭素 where the standard word is 郭索, and the line is cut off).
- Back-translation omission pass (subagent, separate context) on five passages: no dropped or
  added content. Every query resolved as faithful once checked against the source: the Haoxian
  homophone is staged in the source; the Yiddish song is not titled in the source (only hummed);
  同乐会 = "social club" and 直巷 = "straight lane" are descriptive, not proper names.
- Random-sample deep audit (about 4%): the tradecraft paragraph (the Hong Kong shop-surety and
  the "run agent" in the Settlement police station) and the door-architecture paragraph were
  given the full verbatim-quote and back-translation treatment; both faithful.

### Footnote apparatus (rich, fact-checked; three research subagents, web sources only)

16 new notes (book now at 146; ch21 notes 131 to 139, ch22 140 to 146). ch21 (9): Haoxian Road
/ 濠弦街 "Moat-Bowstring" (real; the moat-and-bowstring etymology documented; renamed 豪贤 to
honor the Ming loyalist Li Suiqiu), with the Tianguan Li address on it flagged as the novel's
own; the Wong Tai Sin oracle-lots (deity and 求签 practice real, but the quoted lot-73 verse is
the author's invention, the reverse of the real auspicious lot 73); Cao Song's "one general's
fame is built on ten thousand rotting bones" (己亥岁); the self-combed women / amahs of Shunde
(七姑); the Cantonese fo sui (kerosene); the tanglong door (the three-part Xiguan door, the
chapter title); the wok-ear gables (镬耳墙); the Haizhu Bridge (real, Feb 1933, so Qigu's
landmark misdates her own memory); and the oracle's 东施效颦 / 西子 / 郭索 pun, which names
Xi Shi to Yi Junnian's face. ch22 (7): the Da Mei Wan Bao (real; Chinese edition from 16 Jan
1933); the naamyam 客途秋恨 with its female xiaosheng, its Miao Lianxian line and its Peach
Blossom Spring line (song and lines genuine, the Miao attribution disputed); the 枪牌 Browning
(FN M1900, named for its pistol stamp); the Reflection Institute (反省院, real); Liao Zhongkai
(shot 20 Aug 1925, real; the hint that the fictional Ye Qinian had a hand in it is the novel's);
Dai Jitao and Daiism (real anti-communist theorist); and the 1924 chronology (Feng Yuxiang jails
Cao Kun in the October Beijing Coup; Sun Yat-sen goes north). Not re-noted (covered earlier):
Xi Shi (ch03), Shen Bao (ch07), the Canton-Hong Kong Strike (ch15), Bo Gu / the Jan 1933 Ruijin
move (ch13), the courier lines and Kowloon radio (ch15), Haohan (ch04), Chen Jitang and the
"King of the Southern Sky" (ch20), February / Rou Shi (ch19), the Yiddish tumbalalaika (ch09).

### Glossary rows added

- people: 七姑 Qigu (fictional amah); 廖仲恺 Liao Zhongkai, 戴季陶 Dai Jitao, 冯玉祥 Feng Yuxiang,
  曹锟 Cao Kun, 缪莲仙 Miao Lianxian, 黎遂球 Li Suiqiu (all real).
- places: 豪贤路 Haoxian Road, 光复路 Guangfu Road, 十八甫 Shibafu Street (real); 天官里 Tianguan Li
  (fictional lane on the real Haoxian Road).
- organizations: 大美晚报 the Da Mei Wan Bao, 反省院 the Reflection Institute, 国华报 the Guohua Bao,
  广州报界公会 the Guangzhou Press Association (all real; the Guohua Bao's two-run detail uncorroborated).
- terms: 趟栊门 tanglong door, 自梳女 self-combed woman, 疍家 Tanka, 客途秋恨 Ke Tu Qiu Hen,
  黄大仙 Wong Tai Sin, 火水 fo sui.
- Rendering consistency settled against earlier chapters: 叶主任 = "Director Ye" alongside 叶老师 =
  "Teacher Ye" (both 叶启年); 广州暴动 (KMT press voice) = "the Guangzhou revolt" against 广州起义 =
  "the Guangzhou Uprising"; 爱人 = "lover".

### Scene typography

The source carries no dividers. ch21 has 2 hard cuts (the arrival at Haoxian Road after the
newspaper clipping; the post-murder coda where Yi Junnian wipes the blood and meets the
diviner). ch22 has 0 (one continuous run, teahouse to chase to boat, with Yi Junnian's
back-story woven into the boat scene as reflection, like ch20's single continuous Guangzhou
afternoon). Both break anchors verified against the reading file and confirmed rendered in the
built EPUB (ch21 2, ch22 0). No datelines in this batch.

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 22 of 37 units translated (epigraph +
ch02 to ch22), 146 notes. qa_epub.py: PASS (47 files, 42 documents; 146 references = 146 bodies
= 146 backlinks; numbering sequential in reading order; all links resolve).

## Batch B08 (ch23 Garrick, ch24 Backstage, ch25 Jiaoli)

Three chapters, 189 paragraphs (ch23 63, ch24 71, ch25 55). Parity clean on all three;
check_numbers clean on all three after adding non-quantity noise (see below). This is the
reveal batch. ch23-24: Chen Qianli, in Guangzhou to trace the vanished Ling Wen and the
wounded courier Old Xiao, follows the rare Garrick cigarette to the "dead" constable Lu
Zhongde, and from the actress Little Phoenix hears Lu's whole history -- a KMT provocateur who
staged an anti-communist incident in the Zhongshan-Warship era, faked his death, was slipped
into the Shanghai underground under the cover name Yi Junnian, lured Long Dong to his death at
Moat-Bowstring Street, and is Ye Qinian's ace "Xi Shi." ch25 disposes of Cui Wentai: he bolts
with the suitcase after the bank fiasco, drives blindly out to the Dianshan Lake reed country,
is run down at Jiaoli (Zhujiajiao) by You Tianxiao -- the case holds only coal-yard
scale-weights, Chen having switched the gold inside the vault -- and is drowned in the lake; that
night Ye Qinian sets the wharf ambush for Chen's return on the Guisheng, which opens B09.

### Checks run

- Parity (check_structure --pairs): ch23 63|63, ch24 71|71, ch25 55|55, all OK.
- Numbers (check_numbers --noise check_noise.txt): all three clean. New noise entries (non-
  quantities): 五颜六色, 六神无主, 五花大绑, 三七二十一 (不管三七二十一), 零件. Added
  "twelfth":12 to WORD_NUM (正月十二 -> "the twelfth of the first month"); the built-in list
  had the cardinal "twelve" but not the ordinal. Clock/floor numbers kept as figures so the
  count survives (中午十二点 -> "around twelve o'clock"; 晚上八点 -> "eight that evening"; the
  1929 Duanwu dates 六月十一日/十三号/九号/十一号/民国十八年 all survive).
- Blind double-translation (subagent, separate context, source-only, no sight of the shipped
  text) on five argumentative/literary passages: the identity/chameleon meditation (ch23), the
  actress's lament 今时不同往日 (ch24), Chen's deduction of Ye Qinian's plant (ch24), the driver's
  gold-smell panic (ch25), and You Tianxiao's "smell of gold" line (ch25). The independent
  version matched the shipped reading in sense throughout. Its only divergence was mis-guessing
  茄力克 as a different cigarette brand ("Craven"); the shipped "Garrick" is the researched-correct
  reading (Lambert & Butler). The ambiguities it flagged (the unnamed referent of 他那一走; 凌汶
  as a woman vs the male 他 driver) are preserved correctly in the shipped text.
- Faithfulness / omission audit (subagent, separate context, source + shipped English) on six
  pairs incl. the Central Park history, the 夫/苦 pun line, the bomb-and-letter passage, the
  Shangta paragraph, Ye Qinian's vault reconstruction, and the "he goes by Yi" beat: all six
  reported faithful and complete, no omissions/inventions/reversals. One minor lexical flag --
  包头 rendered "head-dresser lead" (the "lead" interpretive) -- left as is: she is the 正印花旦
  (lead huadan), and the footnote glosses 包头 explicitly.
- Deep-audit sample (~5%): the Central Park paragraph, the 夫/苦 pun, and the Shangta paragraph
  got the full verbatim-quote + faithfulness treatment above; observed error rate nil.

### Footnotes added (19; book now 165), all fact-checked via web-enabled subagents

ch23 (7): Guangzhou's Central Park (real; Yuan/Ming yamen -> 平南王府 of Shang Kexi, one of the
three feudatories, revolt 1673-1681 -> Guangdong governor's office; Sun proposed the park, opened
1921 as First Municipal Park, named Central 1926, today 人民公园; corroborated); Kang Youwei's
Italian sphinx statues (real reformer, 1858-1927; the donation attested only in popular local
sources; the sphinx recurs on the Garrick tin); Three Castles (三炮台, real, Wills, from 1878);
Garrick (茄力克, real, Lambert & Butler, sphinx tin -- the chapter's identity clue, Yi Junnian
smoked it in ch08; the Shamian/one-dollar retail detail uncorroborated period color); fantan
(番摊, real); the Duanwu customs 午时符 (noon-hour charm) and 洗龙舟水 (dragon-boat-water bathing),
real Lingnan customs; the all-female Cantonese 女班 / huadan / xiaosheng / 包头 (real; 群芳艳 echoes
the real troupe 群芳艳影, mixed-sex ban lifting only after 1933). ch24 (5): the Cantonese opera
十美绕宣王 / 背解红罗 / 苏金定 (real repertoire; the red-silk-knot riddle shadows Chen's errand);
the silver-shield (银盾) patron custom (real 捧角 practice; the north-to-Guangzhou spread the
novel's coloring); Whampoa Military Academy (黄埔军校, 1924, real); the Zhongshan Warship Incident
(中山舰事件, 20 Mar 1926, real -- the constable's bomb/letter is the novel's invented spark of just
such a manufactured incident); Little Phoenix's 胭脂用尽 (texture/ambiguity, the reading flagged as
the translator's). ch25 (7): Dianshan Lake (淀山湖, real); Jiaoli/Zhujiajiao (角里 = 朱家角, ch25
title; real, read Jiǎolǐ, distinct from the Suzhou 甪里/Lùlǐ); Shangta (商榻, real, "merchants'
lodging" etymology attested); Songze (崧泽, real Neolithic type-site; the source's roadside 菘泽 is
a folk miswriting); the western-Shanghai roads Brenan (白利南路 = Changning Rd) / Warren (华伦路 =
Gubei Rd) / Rubicon (罗别根路 = Hami Rd) / Hongqiao (虹桥路) + Hongqiao airfield (from 1921, in
service 1929); the Zhu-Hu county road (珠沪县道, Qingpu's real 1932-36 Zhujiajiao-Hongqiao project);
straw-tied pork (稻草扎肉, real Qingpu specialty). Not re-noted: Xi Shi (ch03), Haoxian Road /
Moat-Bowstring (ch21), Shamian and the Sincere rooftop garden and Dashatou (ch20), the Reflection
Institute (ch22), North Sichuan Road (ch07). No AI-written sources used.

### Glossary rows added

- people: 小凤凰 Little Phoenix (fictional huadan). 卢忠德 Lu Zhongde note UPDATED to the ch23-24
  reveal (= "Yi Junnian" = "Xi Shi").
- places (real): 中央公园 Central Park, 东濠涌 Donghao Creek, 淀山湖 Dianshan Lake, 朱家角 Zhujiajiao,
  商榻 Shangta, 崧泽 Songze, 青浦 Qingpu, 白利南路 Brenan Road, 华伦路 Warren Road, 罗别根路 Rubicon
  Road, 虹桥路 Hongqiao Road, 虹桥机场 Hongqiao airfield, 北站 North Station. Decided/fictional:
  乐华 the Lehua, 新亚旅社 the Xinya Hotel, 正元旅社 the Zhengyuan Hotel, 珠沪县道 the Zhu-Hu county road.
- organizations: 群芳艳 the Qunfangyan troupe (fictionalized), 黄埔军校 Whampoa Military Academy (real).
- terms: 三炮台 Three Castles, 番摊 fantan, 花旦 huadan, 稻草扎肉 straw-tied pork, 中山舰事件 the
  Zhongshan Warship Incident, 午时符 the noon-hour charm.

### Scene typography

ch23: 1 dateline (正月初十，立春 -> "The tenth of the first lunar month; the Beginning of Spring")
+ 2 breaks (into the flashback of the waterside shed where Old Xiao lies; the return to the park
gate and the afternoon cigarette-shop hunt). ch24: 0 breaks (one continuous evening at the Lehua
theatre, dressing-room to stage). ch25: 1 break (the cut to the Zhengyuan Hotel that evening,
where You Tianxiao reports to Ye Qinian). Anchors verified against the reading files and confirmed
in the built EPUB (grep class="brk": ch23 2, ch24 0, ch25 1; class="dateline": ch23 1).

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 25 of 37 units translated (epigraph + ch02 to
ch25), 165 notes. qa_epub.py: PASS (47 files, 42 documents; 165 references = 165 bodies = 165
backlinks; numbering sequential in reading order; all links resolve).

## Batch B09 (ch26 The Guisheng, ch27 The Gonghexiang Wharf)

Two chapters, 106 paragraphs (ch26 50, ch27 56). Parity clean on both; check_numbers clean on
both after the fixes below. The shipboard return from Guangzhou to Shanghai. ch26 is largely
interior: aboard the Jardine liner Guisheng, Chen Qianli first relays (in flashback) the dying
Old Xiao's message -- Comrade Shaoshan's newspaper-advertisement contact signal for the
underground Comrade Haohan, entrusted to "Yi Junnian" -- then sinks into the long Nanjing/Shanghai
memory of Ye Tao: Ye Qinian's teacher-days anarchist salon on Xinzha Road, Ye Tao's drift from
Kropotkin to Lenin, her burrowing into the Party Affairs Investigation Section at the Zhanyuan,
and her death carrying out the answer to whether Ouyang Min had turned traitor -- the riddle that
now resolves. ch27: Liang Shichao and Chen work out that the man killed on Haoxian Road was the
real Yi Junnian (Long Dong), that Lu Zhongde usurped the alias, and that Chen must NOT kill or
expose Lu yet, because Lu is the only line to the endangered Haohan. The Guisheng docks at the
Gonghexiang Wharf; Chen meets Lu under Ye Qinian's gun (a rooftop marksman, agents in the cars),
plays out a piece of theatre -- asking Lu to hire a small cargo boat and find a safe house -- and
lets Lu deliver his rehearsed, self-incriminating lie about Ling Wen's disappearance in Guangzhou.

### Checks run

- Parity (check_structure --pairs): ch26 50|50, ch27 56|56, both OK.
- Numbers (check_numbers --noise check_noise.txt): both clean. Root-cause fix in check_numbers.py:
  the built-in "十多" stripper orphaned the leading digit of "X十多" (五十多 -> stray 5, 三十多 ->
  stray 3); extended the rule to an optional ones-digit prefix so "X十多" strips whole. This only
  REMOVES source numerals (such "-odd" figures are approximate and were never precisely checkable),
  so it can never mask a dropped quantity; supersedes the older 二(?=岁) case, which is left in
  place (do not revert). New noise entries (non-quantities): 二十年代 (decade name), 零食/零钱
  (零 not the count 0), 五金 ("five metals" = hardware), 百老汇 (Broadway, 百 part of the
  transliteration), 两个字 (counts the graphs of 撤离, does not transfer to one English word).
  Real drops fixed in the prose, not waived: restored 两个人 twice in ch26 ("the two of them"),
  and rendered 二楼 as "the second floors" (floor number kept as a figure). Clock/tide/knot
  numbers kept as figures so the count survives (十点五十分 -> "fifty minutes past ten"; 十二点 ->
  "twelve o'clock"; 十一节 -> "eleven knots"; 十六海里 -> "sixteen knots").
- Blind double-translation (subagent, separate context, source-only) on four of ch26's
  argumentative/biographical passages (Ye Tao as Chen's guide; her move to the Party Affairs
  Investigation Section; the Xinzha-Road reading-list drift; the reopened safe and Ouyang Min).
  The independent version matched the shipped reading in sense throughout; its only differences
  were the project renderings it could not know (Zhanyuan vs "Zhan Garden"; "Party Affairs
  Investigation Section" vs "Bureau of Party Affairs Investigation"). No omissions.
- Back-translation / omission audit (subagent, separate context, English-only) on four ch27
  passages (the Duanwu sighting logic; the Long-Dong/Little-Phoenix "withdraw" beat; the Guangzhou
  station-closure orders to Mo Shaoqiu; the wharf arrival). Back-translation recovered every
  clause -- names, the closed liaison stations, the tide/time/berth details -- with no omission
  or addition; the only variance was expected character-name homophone spellings.
- Verbatim-quote check: the bilingual QC files are assembled by make_bilingual.py directly from
  data/src/*.txt, so the source side is copied, never retyped.
- Fact-check (subagents, web; Wikipedia/Baidu Baike/academic/government; NO AI-written sources,
  and a stray Grokipedia hit was explicitly discarded). All annotated items corroborated: the
  1925 dissolution of the Beijing Women's Normal University under Duan Qirui (minister Zhang
  Shizhao; Lu Xun's involvement); Jessfield Park / 兆丰花园 (opened 1914; the swans are the novel's
  touch, flagged uncorroborated); Plum Blossom Hill / 梅花山 (plums planted from 1929, young in
  1933); the literary/ideological refs (Pushkin's Captain's Daughter, Kropotkin's Appeal to the
  Young, Chen Duxiu's New Youth, Bakunin vs Lenin, the 1920 Chen Wangdao Manifesto, Lenin's 1917
  Letters from Afar, the CCP journal Bolshevik 1927-32); the First United Front and the Western
  Hills anti-communist right (1925); the Hongkou wharf district (Gonghexiang Wharf, East Broadway,
  Wayside/N.Y.K./Yehsong/Shuntai firms); Shanghai borscht (罗宋汤, White-Russian origin); Cantonese
  靓 "leng."

### Notes added (11; running total 176)

ch26 (6): the 1925 closure of the Beijing Women's Normal University (real; the Duan Qirui
government via minister Zhang Shizhao); Zhaofeng Garden = Jessfield Park (real, opened 1914; swans
the novel's own detail); the reading-list drift anchored on An Appeal to the Young (Pushkin /
Kropotkin / New Youth; real); Bakunin vs Lenin (the anarchism-to-Marxism turn); the three Marxist
titles anchored on Letters from Afar (Manifesto 1920 / Lenin 1917 / Bolshevik 1927-32); Plum
Blossom Hill (real, over Sun Quan's tomb, plums from 1929). ch27 (5): the Nationalist right wing /
First United Front and the Western Hills faction (real backdrop; Ye Qinian's speech invented); the
Gonghexiang Wharf (real North-Bund dock; ch27 title); East Broadway and its real wharf firms
(Wayside/N.Y.K./Yehsong/Shuntai); borscht (罗宋汤, White-Russian Shanghai); Cantonese 靓 "leng."
Not re-noted: the Zhanyuan (瞻园, ch03/ch05), the Party Affairs Investigation Section (ch03),
Nekrasov (ch12; the recited "storm" line is the same poem), Esperanto (ch12), the China Merchants
Steam Navigation Co. (ch02), Duanwu (ch23), the Wusong bar (ch07), Jardine (ch21, first appeared),
Xi Shi (ch03), Whampoa (ch23). No AI-written sources used.

### Glossary rows added

- people: 段祺瑞 Duan Qirui (real).
- places (real): 兆丰花园 Zhaofeng Garden (Jessfield Park), 梅花山 Plum Blossom Hill, 秦淮河 the
  Qinhuai River, 栖霞山 Qixia Hill, 石婆婆巷 Shipopo Lane, 道署街 Daoshu Street, 马府街 Mafu Street,
  舟山群岛 the Zhoushan Archipelago, 公和祥码头 the Gonghexiang Wharf, 东百老汇路 East Broadway.
- organizations (real): 怡和公司 the Jardine company, 汇山码头 the Wayside Wharf, 日本邮船会社 the
  Japan Mail Steamship Company (N.Y.K.), 耶松船厂 the Yehsong Dockyard, 顺泰码头 the Shuntai Wharf,
  北京女子师范大学 the Beijing Women's Normal University.

### Scene typography

ch26: 0 datelines + 2 breaks (into the Guangzhou flashback of Old Xiao's message aboard ship;
into the long Ye Tao memory that fills the rest of the chapter). ch27: 0 datelines + 1 break
(the cut from the night cabin to the mid-morning arrival at the Wusong bar and the wharf). Anchors
verified against the reading files and confirmed in the built EPUB (grep class="brk": ch26 2,
ch27 1; class="dateline": 0/0).

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 27 of 37 units translated (epigraph + ch02 to
ch27), 176 notes. qa_epub.py: PASS (47 files, 42 documents; 176 references = 176 bodies = 176
backlinks; numbering sequential in reading order; all links resolve).

## Batch B10 (ch28 Xiaotaoyuan, ch29 The Dyeworks Drying Ground, ch30 The Yangzhou Master)

Three chapters, 223 paragraphs (ch28 109, ch29 46, ch30 68). Parity clean on all three;
check_numbers clean on all three after the fixes below. The batch cuts three ways on the same
day (the fourteenth of the first month, the eve of the Lantern Festival). ch28 is the enemy's
interior: Ye Qinian rides into the Settlement, plants the coded newspaper advertisement that will
draw Haohan onto the hook, drops "Xi Shi"/Lu Zhongde after a flashback of their night meeting,
then withdraws to his hidden peach garden Xiaotaoyuan to pour out to Old Meng (a retired assassin,
his only confidant) the whole backstory of Ye Tao -- her Beiping years, the Guangzhou leak she ran
using his cipher, the killer he set on Chen Qianli, and her death in a soldiers' shelter-vault at
the Shence Gate -- ending in his Laozi-quoting creed of the strong. ch29 is Chen Qianli's counter:
he decodes the advertisement, escapes the Menghua Street trap over the dyeworks drying ground
(killing two agents), keeps up the fiction before Lu, then walks into the Zhaojiabang coal-yard
ambush laid for him and cuts his way through it to reach the pinned Lin Shi and Li Han. ch30 is
the human cost: Chen Qianyuan and Dong Huiwen spend a lovers' day (Hongkou Park, the Scotto Cup
football, the flashback of how they met over a Ma Zhenhua play), then the Yangzhou-master dinner
at Dong's father's table -- the Three Heads Banquet -- until You Tianxiao and the detective squad
break in to take them.

### Checks run

- Parity (check_structure --pairs): ch28 109|109, ch29 46|46, ch30 68|68, all OK.
- Numbers (check_numbers --noise check_noise.txt): all three clean. One root-cause patch in
  check_numbers.py: added "nil"/"zero" = 0 to WORD_NUM, so the football score 一比零 ("one to
  nil") is fully accounted (the source prints 零 and English scores it "nil"). This only ADDS a
  spelled-zero mapping; it cannot mask a drop. Do not revert. New noise entries (non-quantities):
  八仙桥 (Baxianqiao, a place name), 四分五裂 (idiom "in fragments"), 成千上百 (idiom "hundreds
  upon thousands"), 王八蛋 (abuse, 八 part of the idiom), 千爱 (Chiai-li / Chiai Road place name).
  Real quantities fixed in the prose, not waived: rendered 两个人 as "two of them" in ch29 (kept
  the count as a figure) and 成千上百条蓝布 as "hundreds upon thousands of lengths of blue cloth."
- Blind double-translation (subagent, separate context) on nine argumentative/lyrical passages
  (ch28 the Ye Qinian / Old Meng debate incl. the fascism paragraph and the closing Laozi tirade;
  ch30 the first-meeting flashback and the football-field open). No substantive divergence from
  the shipped text. One fidelity correction taken from it: 史考托杯 reads phonetically as "Scotto"
  (史考特 would be "Scott"), so "the Scott Cup" was changed to "the Scotto Cup" everywhere (prose,
  scenes.json break anchor, footnote).
- Round-trip back-translation (subagent, separate context) on the same nine passages: the Chinese
  round-trips to the source with no omissions. The subagent's flagged "weak spots" were all its
  own hanzi guesses for romanized names/leagues, not defects in the English.
- Random-sample deep audit (~2% : ch28 34, ch29 14 and 42, ch30 46 and 48): verbatim quotation and
  completeness confirmed. One lexical refinement: 鮰鱼 rendered "river catfish" (was "gray-fish").
- Faithful, complete quotation (check 1): guaranteed by make_bilingual.py, which reads the source
  paragraphs verbatim from data/src; parity (check 4) is the mechanical backstop.
- Consistency vs scholarship (check 7): every historical footnote fact-checked by web subagents
  against Wikipedia, Baidu Baike, government and academic sources; each note states real vs.
  invented and corroborated / uncorroborated / contradicted. No AI-written sources used.

### Notes added (19; running total 195)

ch28 (8): Chiang Kai-shek's slogan 攘外必先安内 (real; corroborated); the extra-settlement road
disputes and the Lai'an Li case (real; corroborated); Huangniqiang, the real Xianfeng-era peach
locality (corroborated), paired with a note marking the walled garden Xiaotaoyuan itself as the
novel's invention (its name echoing Tao Yuanming's Peach Blossom Spring); the Zhuangyuanlou /
Ningbo tangyuan (cuisine real; the specific restaurant carries a 1938-dating caveat, flagged);
the soldiers' shelter-vault 藏兵洞 in the Nanjing wall at the Shence Gate (real; corroborated);
the Third Party / Deng Yanda (real; corroborated); the closing Laozi quotation "Heaven and earth
are not benevolent... straw dogs" (Dao De Jing ch. 5). ch29 (2): the National Products Market /
国货运动 (real); the French tramway company (real) with the "first-and-third-class, no second"
detail flagged as the novel's characterization (uncorroborated; early trams were first/second).
ch30 (9): the Uchiyama Bookstore (real; Lu Xun's haunt); Chiai-li and its cherry-blossom name,
with the "English sound of the cherry blossom" derivation flagged as folk etymology
(uncorroborated); the Ma Zhenhua 1928 suicide-and-stage-drama (real; corroborated); the Settlement
football scene / Scotto Cup / Jinan University (league and Jinan real; the named cup and Lux club
uncorroborated); the Zhengjia wooden bridge (real); the Lantern Festival (real); Hart Road / Robert
Hart (real); standard-gold speculation 标金 (real); the Yangzhou "Three Heads" of Huaiyang cuisine
(dishes real; the named guild plausible but unverified). Not re-noted (checked glossary + grep of
earlier reading files for first appearance): Zhaojiabang (ch11), the Shence Gate as a place (ch05
Xuanwu Lake note -- the new note is about the 藏兵洞 feature), Hongkou Park (ch09), the Women's
Normal University / Duan Qirui (ch26/B09), The Guide / 向导 (ch04), Bukharin's ABC of Communism
(ch16), Dai Jitao / 季陶 (ch22), Chen Guofu (ch13 Mr. Lifu note), the 1927 purge (ch09 April
Twelfth), Nekrasov (ch12), Miss Tao (ch04), the Zhanyuan (ch03), the Party Affairs Investigation
Section (ch03).

### Glossary rows added

- people: 孟老 Old Meng (fictional), 董师傅 Master Dong (fictional), 邓演达 Deng Yanda (real),
  穆处长 Section Chief Mu (fictional). (董慧文, 陈千元, 陶小姐, 李汉, 林石, 崔文泰, 陈济棠 already in
  the ledger; renderings verified against it.)
- places: 黄泥墙 Huangniqiang (real), 小桃源 Xiaotaoyuan (fictional garden), 千爱里 Chiai-li (real),
  赫德路 Hart Road (real), 郑家木桥 the Zhengjia wooden bridge (real), 界路 Boundary Road (real).
- organizations: 内山书店 the Uchiyama Bookstore (real), 法商电车公司 the French tramway company
  (real), 暨南大学 Jinan University (real).
- terms: 标金 standard gold (real), 第三党 the Third Party (real), 越界筑路 extra-settlement road
  building (real), 藏兵洞 soldiers' shelter-vault, 攘外必先安内 (Chiang's slogan, real).

### Scene typography

The source again carries no dividers. ch28: 0 datelines + 2 breaks (into the yesterday-evening Lu
Zhongde flashback; back to the present as Ye Qinian leaves for Xiaotaoyuan). ch29: 0 datelines +
0 breaks (one continuous chase, following Chen Qianli through the day). ch30: 0 datelines + 3
breaks (into Dong Huiwen's flashback of the first meeting; back to the football match; the cut from
the match to the evening dinner at Master Dong's). Anchors verified against the reading files and
confirmed in the built EPUB (grep class="brk": ch28 2, ch29 0, ch30 3; class="dateline": 0/0/0).

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 30 of 37 units translated (epigraph + ch02 to
ch30), 195 notes. qa_epub.py: PASS (47 files, 42 documents; 195 references = 195 bodies = 195
backlinks; numbering sequential in reading order; all links resolve).
