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

## Batch B11 (ch31 The Cemetery, ch32 The Dairy Shed, ch33 North Station)

Source: data/src/34_part0032.txt, 35_part0033.txt, 36_part0034.txt (12,408 chars).
Pipeline: out/chNN_en.json -> make_bilingual.py (verbatim source, parity enforced) ->
split_bilingual.py. Paragraph parity locked: ch31 71 / ch32 74 / ch33 102.

Story: ch31 is the emotional climax -- at the Ningshao Manor cemetery on Lantern Festival day,
Chen Qianli confronts Ye Qinian at Ye Tao's grave and tells him the whole truth of her death:
she was a Communist agent who joined the Party at the Women's Normal University and led Chen to
the revolution; exposed inside the Zhanyuan but unable to leave, she used the matched-raincoat
ruse to slip Chen out; Ye Qinian's own agents, sent to kill Chen, shot her from behind at Mafu
Street; she died in the Shence Gate vault after passing the answer "Ouyang Min is the traitor,"
her rescue blocked by Ye's own street cordon. Chen takes Ye and Secretary Ma hostage to force the
release of Chen Qianyuan and Dong Huiwen -- all to keep the operation to move Comrade Haohan alive.
ch32: Chen's new plan turns on Wei Dafu; drunk in a Laoximen tavern, Wei feeds the mole Lu Zhongde
just enough to bait the enemy, then plants a Shen Bao advertisement and, as arranged, lets himself
be taken. ch33: Wei is hooded and driven to a Lai'an Li hotel by the North Station and tortured
(spotlight, inversion, joint-racking, waterboarding, klaxons) by You Tianxiao while Ye Qinian
listens from the shadows; Wei plays for time, giving up only what the enemy already knows. In a
side room Ye tells Lu his read: the Communist Central may be leaving Shanghai, "A Thousand Li of
Rivers and Mountains" is the evacuation, and a second Morse-coded ad has surfaced another Central
leader's name.

### Checks run

- check_numbers.py --noise check_noise.txt: all three clean (0 unresolved). Added to check_noise.txt:
  九条巷 (Jiutiao Lane), 三轮车 (pedicab), 七拐八弯 (idiom "winding"), 百般 (idiom "in every way").
  No real quantity was waived.
- check_structure.py --pairs: parity OK on all three (71/74/102).
- Blind double-translation (separate subagent context) of the ch31 confrontation + death narration
  (source paras 24-34, 42-56) and the ch33 analytical monologue + closing paragraph: independent
  rendering matched on every load-bearing point (Ye had his own daughter shot; bullet from behind;
  Ye Tao's concealed pocket pistol killed the tailing agent; dying message "Ouyang Min is the
  traitor"; the vault holds several thousand). No divergences to fix.
- Back-translation omission pass (separate subagent context) over ch31 and ch33, paragraph by
  paragraph: CLEAN -- no omissions, no additions, no referent/number/who-did-what errors. (ch32 is
  plainer narration; covered by parity + number + structure checks per the sampling rule.)
- Fact-check (subagents, web, real scholarship only -- no AI sources): all referents corroborated;
  two novel-specific claims flagged in the notes as uncorroborated (the named "Ningshao Manor"
  cemetery; the Dec-1932 Puhui Creek/Caohejing joining project).

### Footnotes added (9; running total 204)

ch31 (4): 宁绍山庄 Ningshao Manor (Ningbo-Shaoxing native-place charitable cemetery institution real;
this named manor unattested); 蒲汇塘/漕河泾 Puhui Creek & Caohejing (real geography; the 1932
dredging-to-join uncorroborated); 梅雨 the plum-rains season (real; the wet season that makes the
raincoat ruse unremarkable); 桂花糖芋苗 osmanthus-sugared taro shoots (real Nanjing sweet).
ch32 (3): 法华镇 Fahua town (real border market town); the western-Shanghai dairy belt (real setting;
the novel's milk company its own); 望平街 Wangping Street (real "Newspaper Street" by the Shen Bao
building). ch33 (2): the North Station / Zhabei bombed in the January 28, 1932 fighting (real; folded
into the "Japanese army bombed Zhabei" anchor, cross-referencing the ch05 Nineteenth Route Army /
January 28 note, NOT re-noting it); the GMD 自首/自新/反省院 repentance machinery and the 危害民国
紧急治罪法 (real; "Reflection Institutes" to match the established ch22 rendering).
NOT re-noted (already placed, verified by grep of glossary + earlier reading files): Shen Bao (ch07),
the Nineteenth Route Army / January 28 (ch05), the Soviet areas / encirclement (ch06), the Zhanyuan
(ch03), the Party Affairs Investigation Section (ch03), the Shence Gate / 藏兵洞 (ch05/ch28), the
Women's Normal University (ch26), extra-settlement road building (ch28), Morse-code ads (ch29),
Dongjiadu / Mafu Street (already in glossary).

### Glossary rows added

- places: 宁绍山庄 Ningshao Manor (provisional; institution real, named manor unattested), 蒲汇塘 the
  Puhui Creek (real), 漕河泾 the Caohejing (real), 小闸镇 Xiaozha (real), 法华镇 Fahua town (real),
  望平街 Wangping Street (real), 老西门 Laoximen (real), 浙江路 Zhejiang Road (real), 大舞台 the Great
  Stage (decided). (北站 North Station and 反省院 the Reflection Institute were already in the ledger;
  renderings reused.)
- terms: 烧酒 grain spirit (decided; kept distinct from 绍酒/Shaoxing wine).
- Fictional cast reused from the ledger without change: 欧阳民 Ouyang Min, 田非 Tian Fei, 马秘书
  Secretary Ma, 董家渡 Dongjiadu, 马府街 Mafu Street.

### Scene typography

Source carries no dividers. ch31: 1 dateline ("The fifteenth of the first month; the Lantern
Festival.") + 1 break (the hard cut to the town of Caohejing after the car scene). ch32: 0 datelines
+ 2 breaks (the night return to Fahua town; the next-morning departure). ch33: 0 datelines + 1 break
(the cut from the interrogation to the Ye/Lu conversation in another room). Anchors verified against
the reading files and confirmed in the built EPUB (grep class="brk": ch31 1, ch32 2, ch33 1;
class="dateline": ch31 1, others 0).

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 33 of 37 units translated (epigraph + ch02 to
ch33), 204 notes. qa_epub.py: PASS (47 files, 42 documents; 204 references = 204 bodies = 204
backlinks; numbering sequential in reading order; all links resolve).

---

## Batch B12 (ch34-ch37) -- the resolution + documentary coda; FINAL BATCH

Units: ch34 鱼生粥 Fish Congee (58 paras), ch35 黄浦江 The Huangpu River (79 paras, ending on
the author's completion line), ch36 一封没有署名的信 An Unsigned Letter (11 paras, the martyr's
letter), ch37 附录 Appendix (H2 chapter + two H3 sections, Material One 26 + Material Two 12 = 38
paras), assembled from two source files by scripts/assemble_ch37.py.

### Checks run

- check_numbers.py --noise check_noise.txt: all four units clean (0 unresolved: 58/79/11/38).
  Added to check_noise.txt (all non-quantity numerals): 一大早 (idiom), 独一无二 (idiom), 六十年代
  (decade), 十万火急 (idiom), 万全 (万全之策 idiom), 横七竖八 (idiom), and 零零碎碎 (idiom; placed
  BEFORE 零碎, which otherwise strips the inner pair and orphans a 零 -- this fixed a pre-existing
  latent false positive surfaced in the whole-book regen of ch09). No real quantity was waived.
- check_numbers.py patched (same additive lookbehind style as B03/B07): (1) the 一[点…] idiom
  stripper got a (?<![…十]) lookbehind so a clock time like 十一点 (11 o'clock) is not eaten down to
  10; (2) the 几X measure stripper got a (?<!十) lookbehind so 十几分钟 (ten-odd minutes) strips whole
  instead of orphaning a 十=10. Both only REMOVE source numerals conditionally, so neither can mask a
  dropped quantity. No existing patch reverted. Whole-book regen (32 en.json units) re-checked: all 0.
- check_structure.py --pairs: parity OK on all four (58/79/11/38). Whole-book anchor check
  (--config): 217 notes, 0 unresolved, glossary drift 0. Heading-shape variance (ch01 epigraph = ();
  ch37 Appendix = (2,3); all others (2,)) is the documented, legitimate kind, not a defect.
- Blind double-translation (separate subagent context) of the argumentative/literary core -- the
  whole ch36 letter, the ch37 Material One reflection (perilous-hour summary, the dialectical-
  materialism line, the 死间 exchange, "Ye Tao knows"), and a sample of the ch35 finale: independent
  rendering matched on every load-bearing point (the botany, the Braille/Esperanto image, the peach
  orchard, the courier line, "one open and one hidden," the 死间 verdict). Its one variant --
  "doomed agent" for 死间 -- is exactly the alternative the ch37 note already gives (Giles' "doomed
  spy"); no fix.
- Back-translation omission pass (separate subagent context) over the same passages + the ch37
  Material Two register (Ye Tao and Lin Shi entries): found ONE real omission -- 从上海 ("from
  Shanghai") dropped from the ch37 liaison-line sentence -- now restored ("running from Shanghai to
  Ruijin by a roundabout way through Guangdong"). Rechecked clean. Everything else complete.
- Fact-check (two subagents, web, real scholarship only -- NO AI sources): all referents verified.
  Correction caught: 环龙 = René Vallon (1880-1911), NOT "Vrignaud"; died 1911, the road/monument
  1912. The ch37 "April 4, 1933 Longhua" deaths confirmed as the novel's invention (Qingming eve;
  real anchor = the Longhua Twenty-Four of 7 Feb 1931, incl. the Left League Five). 死间, dialectical
  necessity/contingency, 拨乱反正, Women's Normal University, Duanwu 1929, the Ming-wall 藏兵洞/神策门,
  the 党务调查科/中统, 正广和/Aquarius, and the Tangqiao-Dongjiadu ferry all corroborated.

### Footnotes added (13; running total 217)

ch34 (4): 鱼生粥 raw-fish congee (real dish; the chapter's governing metaphor); the 孝经 filial-piety
allusion (身体发肤，受之父母); 正广和洋行 the Aquarius Company (real 1864 Shanghai firm); 沙船业公所
the Sand-Boat Guild (real). ch35 (2): 环龙碑 the Vallon Monument (real; René Vallon, China's first
air-crash death, 1911; fixes the park identity -- French Park = Gujiazhai Park = today's Fuxing Park);
思南 Sinan (real; the author's literary quarter, where the book is dated). ch36 (1): the double-petaled
flowers (real horticulture; doubling via stamen/pistil conversion trades fertility for show -- the
book's own theme). ch37 (6): 拨乱反正 setting-things-to-rights (real; post-CR, c.1977-82); 死间 the
"dead/doomed agent" (Sun Tzu, Art of War ch.13 -- the key that recasts Wei Dafu); the dialectical
necessity/contingency commonplace; the character 践 (praxis/keeping faith); the Material Two register
+ "4 April 1933 at Longhua Prison" (THE payoff note -- the invented martyrs, Qingming-eve dating, and
the real Longhua Twenty-Four / Left League Five); and "Anonymous" (the deliberately nameless martyr).
NOT re-noted (verified by grep of glossary + earlier reading files): Longhua & the Bao'en Pagoda
(ch03), the Women's Normal University (ch26), the Party Affairs Investigation Section (ch03), the Ming
city wall / 藏兵洞 / Shence Gate (ch05/ch28), Duanwu/端午 (ch23), Esperanto (ch12/ch26), Ruijin (ch22),
the January 28 fighting (ch05), the Nineteenth Route Army (ch05), Fahua town (ch32).

### Glossary rows added

- places: 环龙碑 the Vallon Monument, 塘桥 Tangqiao, 浦东 Pudong, 王家码头街 Wangjia Wharf Street,
  厦门 Xiamen, 正广和洋行 the Aquarius Company, 蓬莱路 Penglai Road, 新舞台 the New Stage, 华商电车公司
  the Chinese Tramway Company, 思南 Sinan, 沙船业船舶会馆 the Sand-Boat Guild hall, 水利局 the Water
  Conservancy Bureau (all attested/decided real); 林泰航运公司 the Lintai Shipping Company, 公茂运输行
  the Gongmao Transport firm (decided; the novel's inventions).
- terms: 死间 dead agent (attested, Sun Tzu), 拨乱反正 setting things to rights (attested), 白色恐怖
  the White Terror (attested), 中统局 the Central Statistics Bureau (attested; the Zhongtong).
- Fictional/established cast reused from the ledger unchanged (Chen Qianli/Qianyuan, Ye Qinian, Lu
  Zhongde, You Tianxiao, Wei Dafu, Lin Shi/Old Kai, Ling Wen, Fang Yunping, Dong Huiwen, Li Han,
  Liang Shichao, Tian Fei, Qin Chuan'an, Haohan, Ye Tao, Ouyang Min, Mu Chuan, Secretary Ma).

### Scene typography

Source carries no dividers. ch34: 0/0 (one continuous night). ch35: 1 dateline (the closing
"Completed at Sinan, Shanghai, March 2022.") + 5 breaks (Dongjiadu night; the Zhengyuan-Hotel
Ye/Mu scene; back to the ferry; the Tangqiao restaurant; Chen intercepting the ferry). ch36: 0/0
(a single letter; its parenthetical subtitle set as an italic first line). ch37: 0/0 (documentary
lists; structured by the two H3 section headings). Confirmed in the built EPUB (grep class="brk":
ch35 = 5; class="dateline": ch35 = 1; ch34/36/37 = 0/0).

### Back matter, cover, metadata (final-batch tasks)

- Colophon authored (back_matter.json): the copyright leaf, reproduced and translated. Publisher
  discrepancy resolved -- the leaf prints 上海文化出版社, but the ISBN prefix 5321 and the Weibo/WeChat
  handles are 上海文艺出版社 (Shanghai Literature and Art Publishing House); the latter set as the true
  imprint, the leaf's error flagged in the English note.
- Cover + metadata (scripts/build_reading_epub.py extended, not reverted): the source's own cover
  (data/figs/cover.jpeg) is embedded verbatim (color, byte-identical -- NOT run through the
  greyscaling figure pipeline) as a dedicated cover page first in the spine, with the manifest
  cover-image property and the legacy <meta name="cover">. dc:title = "A Thousand Li of Rivers and
  Mountains" (the library/document name in both Apple Books and Kindle), dc:creator "Sun Ganlu" (role
  aut, file-as), dc:language en, dc:date 2022, title/creator refines. qa_epub PASS.

### Build

scripts/build_reading_epub.py out/thousand-li.epub: 37 of 37 units translated (the whole book),
217 notes. qa_epub.py: PASS (50 files, 44 documents; 217 references = 217 bodies = 217 backlinks;
numbering sequential 1-217 in reading order; all links resolve). THE BOOK IS COMPLETE.

## Retrofit round R1 (ASSESSMENT.md section 6): ch02-ch10 densification

### Step 0: doctrine upgrade to v2.4

Adopted the shelf-wide v2.4 doctrine on this branch (commit "R1 step 0"). Copied the
current CLAUDE.md, the whole styles/ layers, REVISION_PLAN.template.md, and every shared
script the branch lacked (anchor_check, apparatus_merge, apply_edits, apply_format_markers,
check_align, check_apparatus, check_content, check_reconcile, check_register,
check_style_freshness, compose_style, qc_entities, reflow, register_tics, smart_quotes,
stamp_deliverable, verify_unit, voice_gate_critique). Composed STYLE.md (zh + fiction) with
compose_style.py and seeded STYLE.local.md. Added book.json "deliverable" (the full English
title per the naming policy), plus source_language and genre. The branch's own patched
check_numbers, check_structure and build_reading_epub were left untouched. No reading text
was touched in step 0.

Note on ASSESSMENT.md: this session cloned the branch at d453d63, before ASSESSMENT.md and
authority.json had been pushed to the remote; they arrived on origin/claude/thousand-li
mid-round and were integrated by rebasing the R1 commits onto them. R1 matches ASSESSMENT.md
section 6 exactly (R1 = ch02-ch10, R2 = ch11-ch19, R3 = ch20-ch28, R4 = ch29-ch37,
thinnest-first, reading text frozen). The six authority deviations in section 2 were
cross-checked: only 老闸捕房 (Louza, ch04) and 吴淞口 (Wusong, ch07) fall in the R1 range and are
both conformed; 海格路/Avenue Haig, 马斯南路/Route Massenet, 大美晚报/the Shanghai Evening Post and
Mercury, 反省院/reflection-institute-case, and 白区/the White areas are all in ch11+ (R2-R4).

### R1 = ch02-ch10 (nine units), thinnest-first

Densified nine chapters, 79 new notes added (book-wide 217 -> 296), in two passes. Per-chapter
totals now: ch02 28 (+18), ch03 11 (+7), ch04 14 (+9), ch05 18 (+15), ch06 8 (+4), ch07 22 (+11),
ch08 15 (+5), ch09 12 (+4), ch10 11 (+6). ch05 (thinnest at 3) got the most new notes (15),
as directed; the thinnest chapters were lifted first.

Candidates were sourced from glossary.json's referents, CLAUDE.md's four coverage domains,
and the lost-in-translation idiom/allusion layer. Every new note carries a real-vs-fiction
and corroborated/uncorroborated/invention verdict. Fact-checking was done by three research
subagents against Wikipedia (EN/ZH), Baidu Baike, and academic/government/museum sources
(never Grok/Grokipedia). Findings that changed a note: the secret-service book You Tianxiao
carries (ch03) is a light rename of a REAL Gu Shunzhang text, not an invention; the garrison's
German "electric-torture apparatus" (ch05) is the novel's, on a real German-military backdrop;
the Louza station (ch04) is the very SMP station of the May 30, 1925 shooting; Baiyunguan (ch02)
really did host a garrison detective-squad lock-up; Park Road is today Huanghe Road (not
Huangpi); Pu'enjishi Road is today Jinxian Road. Xiaobangwan (ch07) could not be verified and
was not given a note.

HONEST NOTE ON DENSITY (matters for the commissioner's R2-R4 calibration). ASSESSMENT.md
section 6 targets the directive band (~30-40 notes/chapter, ~290-460 new/round) or, at the
moderate tier, ~25/chapter (~160 new/round). R1 lands well under that: 79 new, ~15/chapter
total, with only the two content-rich chapters (ch07 22, ch02 28) reaching the moderate tier
and the short/interior ones (ch03 11, ch06 8, ch09 12, ch10 11) below it. This is a judgment
call under two binding constraints, made deliberately rather than by omission:
(1) The no-pad rule (CLAUDE.md: "notes added just to add them are still the failure mode").
    These are short narrative chapters -- several almost pure cell-dialogue (ch06) or interior
    monologue (ch09) -- and even ch02, the densest, at 28 notes over ~1,000 words of English is
    already about one note per two sentences; pushing a narrative novel to 40/chapter would
    read as padding, not annotation. The band appears calibrated for denser (nonfiction /
    documentary) material than these particular chapters carry.
(2) First-appearance discipline. Many obvious early referents were already footnoted at a LATER
    recurrence by the original batches, so re-noting in ch02-ch10 would duplicate: the Garrick
    brand (a deliberate identity-reveal note at ch23), the Central Liaison Bureau's courier
    lines (ch15). R1 relocated the clean cases (political tutelage ch18 -> ch05) and added fresh
    first-appearance notes where the later mention was only incidental (Suzhou Creek, Nanshi,
    the silver dollar, the boycott, the tram). Remaining inversions are logged in HANDOFF.
If the commissioner wants R2-R4 pushed harder toward the band, the levers are: accept more
light texture/material-culture notes at the margin, and relocate every later-noted
first-appearance referent into its round (a broader move than R1 made). Flagged for the R2
kickoff decision; R1 held to no-pad.

### Tier A conformances folded (ch02-ch10 only)

- Names (authority.json decided renderings appearing in range), with glossary.json in lockstep:
  ch04 "the Laozha Police Station" -> "the Louza police station"; ch07 "the Wusong bar" ->
  "the mouth of the Wusong River". (Massenet Road/Route Massenet first appears ch11; Da Mei Wan
  Bao does not appear in range; both are later rounds.)
- Dates -> "Month Day, Year": reading text, ch10 "the eleventh of March" -> "March 11" (the only
  day-first date in the range's body; the ch07 "eighteenth year of the Republic" is Republican
  reckoning, left as period voice and footnoted). Note bodies, ch02-ch10: nine day-first dates
  reordered ("31 January 1931" -> "January 31, 1931", etc.). ch11+ note dates are NOT swept this
  round (later rounds).
- First-appearance relocation: the political-tutelage gloss moved from the ch18 note to a
  focused note at ch05 (its first appearance); the ch18 note trimmed to avoid a duplicate.

### Checks run (R1)

- anchor_check.py per unit before apply_edits.py: no collisions. apply_edits.py applied 3 prose
  conformances and 73 notes across the nine units.
- check_structure.py --pairs data/zh/<id>.txt: paragraph parity OK for all nine (edits were 1:1).
- check_numbers.py --noise check_noise.txt on regenerated bilinguals for ch06-ch10: 0 unresolved.
  ch02-ch05 numerals unchanged in range (only ch04 edited, a non-numeric name conformance).
- register_tics.py --profile ch02-ch10: day-month-date battery reads 0 over the range;
  british-spelling hits are real venue names (Theatre) and are exempt; the remaining
  narration-side batteries are pre-existing candidates in the FROZEN reading text (content is
  frozen this round), informational only.
- Build: build_reading_epub.py "out/A Thousand Li of Rivers and Mountains.epub" (the new
  deliverable name), 37/37 units, 290 notes. qa_epub.py: PASS (50 files, 44 documents; 290
  references = 290 bodies = 290 backlinks; numbering sequential 1-290; all links resolve). One
  numbering-order failure was caught and fixed mid-round: the ch02 "Judge Advocate's office"
  anchor had contained the existing "Longhua Garrison Command" anchor and shared its end
  position, inverting two note numbers; shortening the anchor fixed it.
- Deliverable stamped with stamp_deliverable.py R1.

## Retrofit round R2 (ASSESSMENT.md section 6): ch11-ch19 densification

### R2 = ch11-ch19 (nine units), thinnest-first

Densified nine chapters, 23 new fact-checked notes added (book-wide 296 -> 319). Per-chapter
totals now: ch11 12 (+3), ch12 15 (+6), ch13 10 (+2), ch14 7 (+3), ch15 7 (+1), ch16 10 (+3),
ch17 5 (+0), ch18 9 (+4), ch19 5 (+1). The thinnest chapters (ch14, ch19, ch17 at 4-5) were
taken first; ch12 (a location-rich Hongkou chapter) absorbed the most new notes.

Candidates were sourced from glossary.json's referents, CLAUDE.md's four coverage domains, and
the lost-in-translation idiom/allusion/tradecraft layer, under strict first-appearance discipline
(the WHOLE notes.json was grepped, anchors AND bodies, before each note). Fact-checking was done by
three web-enabled research subagents against Wikipedia (EN/ZH), Baidu Baike, ChinaKnowledge, a
peer-reviewed history journal, the Marxists Internet Archive and cultural/culinary sources (never
Grok/Grokipedia). Every new note carries a real-vs-fiction and corroborated/uncorroborated verdict.

New notes by chapter (all first-appearance, non-duplicate):
- ch11: the recognition-signal/countersign tradecraft; the gown-vs-foreign-suit class code; the
  Settlement/Chinese-city jurisdictional border as a safe-house tradecraft advantage.
- ch12: Chengzhong Middle School (real, Ye Chengzhong, c.1900); Xiahai Temple (real Hongkou
  fisherfolk temple); Lenin's Letters from Afar (远方来信, 1917; the manuscript title is Lenin's
  actual first letter, and gives the chapter its Chinese title); the Soviet cadre-training school
  (real Comintern schools; the novel's unnamed manor/Siberian-forest campus is atmosphere); the
  "one striking feature" disguise tradecraft; tangyuan.
- ch13: the Bund (外滩); the tea dance (茶舞/the dansant).
- ch14: Shaoxing wine (huangjiu); the Mauser C96 pistol (盒子炮/驳壳枪); the bao/baojia unit
  (honest on the 1932 systematization) and Fengxian.
- ch15: eight-treasure rice (八宝饭).
- ch16: fengshui/geomancy (the canted corner door); door-opening firecrackers (开门炮仗); the
  secret service's 家法 "family discipline" (line is ch16, not ch17 -- caught during apply).
- ch17: +0. A pure operation chapter; every referent (armored car, the Ministry-of-Finance bond
  business/T. V. Soong, the Nanshi police car, the Three Principles, Professor Tao) was already
  noted. No first-appearance gap; not padded.
- ch18: the Xujiahui film-studio district (Lianhua, kept general); the penghu (棚户) refugee
  shanty settlements; Rue Pere Robert (金神父路 -> Ruijin Er Road); Gujiazhai Park (French Park,
  today Fuxing Park).
- ch19: the nine-dragon/meteor firework names (traditional, evocative, honestly flagged).

HONEST NOTE ON DENSITY (R2). Like R1, R2 lands well under the directive band (23 new, ~2.6/chapter;
finals 5-15/chapter). This is deliberate under the no-pad rule, and structural to this stretch:
ch11-ch19 are interior conversation/operation chapters (a recruitment interview, a brothers'
reunion, a hotel briefing, a bank job, a coal-yard council) whose big referents -- the Settlement
and its police, the Songhu Garrison and its Judge Advocate's office, the Party Affairs Investigation
Section / Special Operations Headquarters, the Guangzhou Uprising, the Northern Expedition, the
August 7th Conference, the Bund's Cathay/Sassoon, Fourth Avenue, Shen Bao, the surety bond, the
zhang measure, the Fourth Avenue market raid -- were ALL already footnoted at their first appearance
in ch02-ch10 or in the chapters' own existing notes. Re-noting them would duplicate. The genuine
new material is the Hongkou/French-Concession micro-geography (ch12, ch18), a few real institutions
(Chengzhong, the film district, the baojia unit), the Lenin/tradecraft layer, and the festival
material-culture (Shaoxing wine, eight-treasure rice, tangyuan, the firecracker customs). The
density gate here is first-appearance discipline, not effort: the launching chat gave no
"push-harder-toward-the-band" instruction and CORRECTIONS.md is the empty template, so R2 held to
no-pad, exactly as R1 did and as the R2 kickoff's density policy directs. Two thin chapters are
honestly capped: ch17 (+0, all referents pre-noted) and ch19 (+1, Ling Wen's interior backstory).

### Tier A conformances folded (ch11-ch19 only)

- Names (authority.json decided renderings appearing in range), glossary.json updated in lockstep
  and the broken note anchors moved/reglossed:
  - ch11 马斯南路 "Massenet Road" -> "Route Massenet" (2 reading occurrences; the ch11 note anchored
    "Massenet Road" moved to "Route Massenet" and its body reglossed).
  - ch11 海格路 "Haige Road" -> "Avenue Haig" (1 reading occurrence; the ch11 "Zhaozhujiao Road"
    note body reglossed from "Haige Road (海格路, Avenue Haig...)" to "Avenue Haig (海格路...)").
  - ch13 吴淞口 "the Wusong bar" -> "the mouth of the Wusong River" (1 reading occurrence; already
    noted at ch07 in R1, so a name conformance only).
  glossary.json 马斯南路 and 海格路 flipped to status "decided" with the authority form; out/ch11_en.json
  and out/ch13_en.json synced to the reading files (R1 precedent). 大美晚报, 反省院 (ch22) and 白区 do
  NOT appear in the ch11-ch19 reading text and wait for R3/R4.
- Dates -> "Month Day, Year": the ch11-ch19 reading text carried NO day-first dates (register_tics
  day-month-date reads 0 over the range, before and after). Note bodies did: 12 day-first dates in
  the pre-retrofit ch11/ch13/ch14/ch15/ch19 note bodies were reordered via scripts/patch_note_bodies.py
  (e.g. "11 December 1931" -> "December 11, 1931", "(11-12 February)" -> "(February 11-12)").
  Republican-reckoning and lunar dates left as period voice.

### Scene-break review (commissioner directive; ch11-ch19)

Reviewed all nine units against the calibrated principle (add only at a genuine jump in place, time
AND vantage; leave camera-flips inside a continuous cross-cut, and causally/aurally sutured cuts,
hard). NO new breaks or datelines were warranted:
- ch11 (The Tenant) and ch12 (A Letter from Afar): genuinely single-scene (one continuous
  conversation each, memories braided in but no new scene), left empty, as the earlier survey noted.
- ch13-ch19 already carry breaks at their genuine scene changes (ch13 1, ch14 1, ch15 2, ch16 4,
  ch17 7, ch18 3, ch19 2); the built EPUB renders exactly those counts. Borderline cuts left hard
  and why: ch14's Cui Wentai 1927 flashback is braided with the live dinner dialogue (not a set-off
  block like ch19's Ling Wen flashback, which already has its break), so a divider there would
  over-segment; ch19's outer-room shift to Yi Junnian and Ling Wen (para "I don't think Chen Qianli
  is telling the truth") is a same-place, same-time perspective change, not a new scene.

### First-appearance inversions logged (for the whole-book reconciliation)

- Zhonghui Trust Bank (中汇银行, the gold-holding bank): first appears ch10 (The Clinic), OUTSIDE the
  R2 range, and is UNNOTED book-wide. The real 中汇银行 was Du Yuesheng's bank, opened 1929; the novel's
  "中汇信托银行" lightly renames it. R1's ch10 did not note it; a reconciliation pass should add a
  first-appearance note at ch10.
- Letters from Afar: a fresh first-appearance note was added at ch12 (its true first appearance and a
  plot element); the existing ch26 note keeps its own placement (a three-title gloss tied to ch26's
  action), so this is an added first-appearance note, not a relocation.

### Checks run (R2)

- anchor_check.py per unit before apply_edits.py: only the expected ch11 Massenet collisions (handled
  by the NOTE-ANCHOR move). apply_edits.py applied 4 prose conformances (ch11 x3, ch13 x1), 1 anchor
  move, and 23 notes across eight units (ch17 had none). One mis-filed anchor (the "family discipline"
  line is ch16, not ch17) was caught by apply_edits' verbatim-substring guard and refiled before the
  notes.json write.
- scripts/patch_note_bodies.py: 12 note-body edits (2 name reglosses + 10 date normalizations), each
  guarded to match exactly one note and one occurrence.
- check_structure.py --pairs data/zh/<id>.txt: paragraph parity OK for all nine (82/106/83/70/85/72/60/54/48).
- check_numbers.py --noise check_noise.txt on regenerated bilinguals for all nine: 0 unresolved.
- register_tics.py --profile ch11-ch19: day-month-date 0, british-spelling 0 over the range; the
  remaining narration-side batteries are pre-existing candidates in the FROZEN reading text
  (informational this round).
- Build: build_reading_epub.py "out/A Thousand Li of Rivers and Mountains.epub", 37/37 units, 319
  notes. qa_epub.py: PASS (50 files, 44 documents; 319 references = 319 bodies = 319 backlinks;
  numbering sequential; all links resolve). Scene breaks re-verified by grepping the built chapter
  xhtml (class="brk"/"dateline") -- counts unchanged, as intended.
- Deliverable stamped with stamp_deliverable.py R2.

## Retrofit round R3 (ASSESSMENT.md section 6): ch20-ch28 densification

R3 densifies the third range (ch20 The Xingchang Apothecary through ch28 Xiaotaoyuan), thinnest-first,
and folds the Tier A conformances that fall in it. 13 new fact-checked notes were added and one note
relocated to its first appearance, taking the book from 319 to 331 notes. Per chapter (new notes):
ch20 0, ch21 2, ch22 1, ch23 1, ch24 3, ch25 1, ch26 3 (one relocated in), ch27 2, ch28 0. Resulting
counts: ch20 13, ch21 11, ch22 8, ch23 8, ch24 8, ch25 8, ch26 9, ch27 7, ch28 8.

Thinnest-first was honored against the R2-handoff thinnest in range (ch24 5, ch27 5, ch26 6): ch24
lifted to 8 (+3), ch27 to 7 (+2), ch26 to 9 (+3). The words-per-note swing across the range tightened
from 5-13 notes/chapter to 7-13.

The new notes, all fact-checked against real scholarship (Wikipedia EN/ZH, Baidu Baike, Britannica,
museum/government/academic sources; never an AI-written source; Grokipedia results that surfaced were
excluded by rule 5), each carrying its real-vs-fiction and corroboration verdict:
- ch21: Jardine, Matheson (怡和洋行, the Ewo firm) and its Indo-China Steam Navigation Company coastal
  line (real; the ships Fusheng/Guisheng are the novel's, built on Jardine's genuine "-生/-sang" naming
  series); the Xiguan newspaper street / Guangfu Road (renamed 1931) / Guangzhou Press Association
  (1908) apparatus (street and association corroborated; a press-association back-number clipping
  service plausible but not independently attested, so hedged).
- ch22: the Tanka / 疍家 boat people (real, corroborated: sampans, creek-side stilt-huts, the bar from
  living ashore and the imperial exams, Yongzheng's 1729 emancipation).
- ch23: the Beginning of Spring / 立春, first of the twenty-four solar terms (corroborated); placed on
  the chapter's opening dateline (the builder attaches the marker inside the centered dateline, verified
  in the built ch23.xhtml).
- ch24: the comprador / 买办 (corroborated); Canton embroidery / 广绣, one of China's four famous
  embroidery traditions, gold-couched on opera costume (corroborated); the Dashatou airfield / 大沙头机场,
  one of China's first airfields, chiefly military/official flying in the 1920s (corroborated, with the
  honest note that scheduled civil air service on the Shanghai-Guangzhou line dates only from 1929).
- ch25: the idiom 咸鱼翻身 ("the salted fish turns over") behind "flip like a salted fish come back to
  life" (texture; the image is the point).
- ch26: the Qinhuai River / 秦淮河, old Nanjing's pleasure quarter (corroborated); Minnan tangerine-red
  cakes / 橘红糕 (corroborated, with the honest note that the sweet's regional attribution varies by
  source); and the osmanthus-sugared taro shoots / 桂花糖芋苗 note RELOCATED from ch31 to ch26, its true
  first appearance (the ch31 duplicate removed; see inversions below).
- ch27: the Zhoushan Archipelago / 舟山群岛 as a reef-strewn navigation hazard (corroborated); the idiom
  瞒天过海 ("deceiving heaven and crossing the sea"), first of the Thirty-Six Stratagems (corroborated).

HONEST NOTE ON DENSITY (R3). Like R1 (~15/chapter of new notes) and R2 (~2.6/chapter), R3 lands well
under the directive band: 13 new notes across nine units, ~1.4/chapter. The launching chat gave no
"push-harder-toward-the-band" instruction and CORRECTIONS.md carries only the scene-break directive, so
R3 held to no-pad exactly as the kickoff's density policy directs. The reason is real and structural,
not effort: these middle chapters are Guangzhou/Nanjing-history-heavy and were already annotated
generously in B06-B08 (ch20 alone carries 13 notes, ch28 8), and their big referents (the concessions
and their police, the Songhu Garrison, the Special Operations Headquarters / Party Affairs Investigation
Section, the Guangzhou Uprising, the Canton-Hong Kong Strike, Shen Bao, the Bund, the Nineteenth Route
Army / January 28, the Zhanyuan, Whampoa, Manchukuo, the ABC of Communism, the April Twelfth purge, Dai
Jitao, Chen Guofu, Zhu Huiri) are ALL already footnoted at their first appearance in earlier rounds; a
second note would duplicate. Three chapters are honestly capped: ch20 (+0, all referents pre-noted; the
densest in range at 13), ch28 (+0, likewise saturated at 8), and ch25 (+1, largely Cui Wentai's interior
flight, its geography already noted). The genuine first-appearance gaps that remained (a firm, a craft,
an airfield, two Guangzhou institutions, a boat people, a river, two sweets, a solar term, two idioms)
were filled thinnest-first.

### Tier A conformances folded (ch20-ch28 only)

- 大美晚报 "Da Mei Wan Bao" -> "the Shanghai Evening Post and Mercury" (authority.json decided form; ch22,
  1 reading occurrence). The existing ch22 note anchored "Da Mei Wan Bao" was moved to the English
  masthead and its body reglossed to lead with the masthead and gloss 大美晚报/Da Mei Wan Bao once;
  glossary.json 大美晚报 flipped to status "decided". out/ch22_en.json synced.
- 反省院 "the Reflection Institute" -> "the reflection institute" (a CASE fix; ch22, 1 reading occurrence).
  Generic institution lowercased; the proper "Capital Reflection Institute" in the note body kept its
  caps. The ch22 note anchor moved to "the reflection institute in Nanjing" and its body opening
  lowercased; glossary.json 反省院 flipped to "decided". out/ch22_en.json synced.
- 吴淞口 "the Wusong bar" -> "the mouth of the Wusong River" (authority.json decided form; ch27, 1 reading
  occurrence, "The Guisheng came in across the Wusong bar"). That exact phrase is ALSO the ch27
  scene-break anchor in scenes.json, so the reading text, the scenes.json ch27 "breaks" string, and
  out/ch27_en.json were conformed in the same pass; the built ch27.xhtml still shows class="brk" = 1.
  (吴淞口 was already glossed at ch07/ch13, so a name conformance only, no new note.)
- Locale spelling: "a piece of theatre" -> "a piece of theater" (x2, ch27), the only genuine common-noun
  locale strays ASSESSMENT flagged; the real concession venue names (the Lehua Theatre etc.) keep their
  period "Theatre" spelling and are exempt (ch20/ch26 british-spelling hits are those exempt venues).
  out/ch27_en.json synced.
- 海格路 Avenue Haig, 马斯南路 Route Massenet, 白区 the White areas: grepped ch20-ch28, NONE appear in range
  (done in R2 / not in range).
- Dates -> "Month D, YYYY": the ch20-ch28 reading text carried NO day-first dates (register_tics
  day-month-date reads 0 over the range). Seven day-first dates in pre-retrofit note bodies were
  reordered via scripts/patch_note_bodies_r3.py: ch20 "23 June 1925" -> "June 23, 1925"; ch22 "16
  January 1933" -> "January 16, 1933", "20 August 1925" -> "August 20, 1925", "23 October" -> "October
  23", "13 November" -> "November 13"; ch24 "20 March 1926" -> "March 20, 1926"; ch28 "30 November 1931"
  -> "November 30, 1931". Republican-reckoning and lunar dates left as period voice.

### Scene-break review (commissioner directive; ch20-ch28)

Reviewed all nine units against the calibrated principle (add only at a genuine jump in place, time AND
vantage where the new scene stands apart; leave camera-flips inside a continuous cross-cut and
causally/aurally sutured cuts hard). NO new breaks or datelines were warranted:
- Genuinely single continuous scenes, left with 0 breaks: ch20 (one arrival-to-apothecary sequence
  across one afternoon, Mrs. Mo's courier story braided in as recollection, not a new scene); ch22
  (teahouse -> chase -> Tanka boat is one continuous pursuit, and Yi Junnian's recruitment backstory is
  interior reflection in the same boat scene, closed by "The scull stirred the river water", so no hard
  cut); ch24 (a single dressing-room conversation, Little Phoenix's monologue).
- Already segmented at their genuine scene changes, left unchanged: ch21 (2 breaks), ch23 (1 dateline +
  2 breaks), ch25 (1 break: the lake killing -> the Zhengyuan Hotel report), ch26 (2 breaks: the ship
  present -> the Ye Tao flashback), ch27 (1 break: shipboard night -> the wharf arrival), ch28 (2 breaks:
  the car/advertisement -> the previous-evening flashback -> Xiaotaoyuan). The built EPUB renders exactly
  these counts (grep class="brk"/"dateline"). This matches R2's outcome (no new breaks in ch11-ch19): a
  legitimate result, not a failure to look.

### First-appearance relocation and inversions (for the whole-book reconciliation)

- RELOCATED: the osmanthus-sugared taro shoots note (桂花糖芋苗) was placed at ch31 in B11, but its FIRST
  appearance is ch26 (the Zhanyuan-gate peddler / Mafu Street). R3 adds the note at ch26 and removes the
  ch31 duplicate (ch31 now 3 notes). The body is the same; the tie to Mafu Street holds at ch26 too.
- STILL OPEN (out of R3 range, logged for reconciliation): Zhonghui Trust Bank (中汇银行) unnoted, first
  appears ch10; the tram, note at ch29 but first appears ch07; the Garrick brand first appears ch08 with
  its dedicated identity-reveal note kept at ch23 (a deliberate plot-payoff, checked and left); the
  Central Liaison Bureau first named ch07, note at ch15; the Peach Blossom Spring / Tao Yuanming allusion
  first glances by in a ch22 opera lyric but is dedicatedly noted at ch28 (the Xiaotaoyuan title payoff,
  left).

### Checks run (R3)

- anchor_check.py per unit before apply_edits.py: only the expected ch22 collisions (the Da Mei and
  Reflection TOUCH/NOTE-ANCHOR pairs), handled by the moves. A tooling trap was caught and fixed here:
  apply_edits' 5-line OLD/NEW scan window bled between tightly-spaced TOUCH/NOTE-ANCHOR blocks, so ch22
  and ch27 edit files were re-spaced with two blank lines between blocks; the first (aborted) run left
  ch22_reading.md half-edited and was reverted with git checkout before the clean re-run (notes.json is
  written only at the end, so it was untouched).
- apply_edits.py: 5 prose conformances (ch22 x2, ch27 x3), 2 anchor moves (ch22), 13 notes across seven
  units. scripts/patch_note_bodies_r3.py: 9 note-body edits (7 date normalizations + the Da Mei regloss
  + the Reflection case fix) and 1 note removal (the ch31 osmanthus relocation), each guarded.
- check_structure.py --pairs data/zh/<id>.txt: paragraph parity OK for all nine (88/161/56/63/71/55/50/56/109).
- check_numbers.py --noise check_noise.txt on regenerated bilinguals for the two units whose reading
  changed (ch22, ch27): 0 unresolved.
- register_tics.py --profile ch20-ch28: day-month-date 0 over the range; british-spelling reduced to the
  exempt venue "Theatre" names (ch27's "piece of theatre" strays cleared); the remaining narration-side
  batteries are pre-existing candidates in the FROZEN reading text (informational this round).
- Build: build_reading_epub.py "out/A Thousand Li of Rivers and Mountains.epub", 37/37 units, 331 notes.
  qa_epub.py: PASS (50 files, 44 documents; 331 references = 331 bodies = 331 backlinks; numbering
  sequential; all links resolve). Scene typography re-verified in the built xhtml (ch27 brk=1, ch23
  dateline=1 with its new note marker inside).
- Deliverable stamped with stamp_deliverable.py R3.

## Retrofit round R4 (ASSESSMENT.md section 6): ch29-ch37 densification -- FINAL ROUND

R4 densifies the last range (ch29 The Dyeworks Drying Ground through ch37 the two-part Appendix),
thinnest-first, folds the Tier A conformances that fall in it, and, as the closing round, does the
whole-book reconciliation and final QA and writes the completion report (COMPLETION.md) instead of a
next-round kickoff. 7 new fact-checked notes were added (one of them a whole-book first-appearance fix
at ch13), taking the book from 331 to 338 notes. Per chapter (new notes): ch29 +1, ch30 +1, ch31 0,
ch32 +1, ch33 0, ch34 +1, ch35 +2, ch36 0, ch37 0, plus ch13 +1 (reconciliation). Resulting R4-range
counts: ch29 3, ch30 10, ch31 3, ch32 4, ch33 2, ch34 5, ch35 4, ch36 1, ch37 6.

Thinnest-first was honored against the R3-handoff thinnest in range (ch36 1, ch29 2, ch33 2, ch35 2):
ch35 lifted to 4 (+2) and ch29 to 3 (+1); ch33 and ch36 genuinely capped (see the honest note). The new
notes, all fact-checked against real scholarship (Wikipedia EN/ZH, Baidu Baike, museum/government/
academic sources; never an AI-written source; Grok/Grokipedia excluded by rule 5), each carrying its
real-vs-fiction and corroboration verdict:

- ch13 (RECONCILIATION, first appearance): Dongjiadu / 董家渡, the old-city riverside wharf quarter south
  of the Bund, with St. Francis Xavier's Church (董家渡天主堂, 1853), the oldest surviving church in
  Shanghai (real; corroborated). Dongjiadu first appears at ch13 (a car destination) but becomes the
  operational hub of the ch32-ch35 river escape, and was unnoted book-wide; the note is placed at first
  appearance and covers all later uses.
- ch29: Laoximen / 老西门, the "Old West Gate" locality of the old walled city, named for the Ming Yifeng
  Gate (仪凤门, 1553), "old" since a smaller west gate opened nearby in 1908; wall pulled down 1912-13
  for the ring road, the name surviving for the crowded market quarter (real; corroborated).
- ch30: the Settlement Volunteers / Shanghai Volunteer Corps (万国商团), the International Settlement's
  multinational citizen militia (founded 1853; ~20 companies by the early 1930s, a Japanese company from
  1907), with a rifle range by Hongkou Park for live-fire drill (real; corroborated -- the exact
  range specifics rest on a single memoir source, so those were left out and only the corroborated
  outline kept).
- ch32: the Great Stage / 大舞台 on Second Avenue (二马路, today Jiujiang Road), a real Peking-opera house
  (opened c.1909 as 文明大舞台; bought 1919 by Huang Jinrong / 黄金荣, renamed 荣记大舞台; today the
  People's Grand Stage / 上海人民大舞台), distinct from the Tianchan on Fuzhou Road (real; corroborated).
- ch34: the numbered wharf "share gangs" / 股党 (the Six-, Eight-, Sixteen-, Thirty-Two-, Seventy-Two-
  Gang) -- the Green-Gang-tied dock-labor system, hiring through contract bosses (包工头); the system and
  the "eight-share" naming (Du Yuesheng's 小八股党) are real and corroborated, but the graded ascending
  series the novel lists is its own extrapolation, not a documented set of gangs (flagged as
  uncorroborated).
- ch35: the New Stage / 新舞台 (real, corroborated: opened 1908 by Pan Yuejiao / 潘月樵 and the Xia
  brothers, China's first Western-proscenium playhouse and a home of 文明戏) -- BUT its documented sites
  were Shiliupu and the Nine-Mu Field, and it had closed by the late 1920s, so a working theater on
  Penglai Road in 1933 answers rather to the later Penglai Grand Theater / 蓬莱大戏院; the note flags the
  novel's placement on Penglai Road as uncorroborated, likely a conflation (a translation-uncertainty
  note, kept honest per rule 4). And the two rival Nationalist secret services / 中统 vs 军统: Ye
  Qinian's party-run Special Operations Headquarters (the 中统 lineage) versus the military bureau Mu
  Chuan is joining (Dai Li's / 戴笠 Special Services Department, 1932, later nicknamed 军统 only from
  1938 -- so the novel's descriptive phrasing is period-accurate; corroborated).

### Tier A conformances folded (in the ch29-ch37 range + whole-book reconciliation)

- Dates -> "Month D, YYYY" (the BIG R4 Tier A job). The ch37 appendix reading text carried all 11 of the
  book's remaining day-first dates; scripts/conform_r4.py normalized them in out/ch37_reading.md AND in
  out/ch37b_en.json (Material Two): "10 January 1933" -> "January 10, 1933", "16 January 1933" ->
  "January 16, 1933", "2 February 1933" -> "February 2, 1933", "8 February 1933" -> "February 8, 1933",
  and the seven byte-identical "4 April 1933 at Longhua Prison" lines -> "April 4, 1933, at Longhua
  Prison" (a global replace-all, done in a guarded script rather than apply_edits because seven lines are
  identical and TOUCH requires OLD unique). register_tics day-month-date now reads 0 over the whole
  ch29-ch37 range. Day-first dates in existing note bodies were reordered via
  scripts/patch_note_bodies_r4.py: ch30 Ma Zhenhua "17 March 1928" -> "March 17, 1928"; ch33 Zhabei
  "28-29 January" -> "January 28-29"; ch35 Vallon "6 May 1911" -> "May 6, 1911"; ch37 frame "4 April
  1933" -> "April 4, 1933", "5 April in 1933" -> "April 5 in 1933", "7 February 1931" -> "February 7,
  1931"; ch37 Anonymous "10 January 1933" -> "January 10, 1933". Republican-reckoning and lunar dates
  left as period voice.
- 吴淞口 "the Wusong bar" -> "the mouth of the Wusong River" (authority.json decided form). This was the
  one authority stray still in the reading text book-wide: ch34 (x2) and ch35 (x2). Conformed in the
  reading text via apply_edits TOUCH (edits/ch34_edits.md, edits/ch35_edits.md) and in out/ch34_en.json /
  out/ch35_en.json via conform_r4.py. (吴淞口 was already glossed at ch07/ch13/ch27, so a name
  conformance only, no new note; glossary.json already carried the conformed en.)
- 白区 "the White area" -> "the White areas" (authority.json decided form, number). It does NOT appear in
  the reading text anywhere book-wide (grepped); it survived only in one pre-retrofit note body (ch11
  "Red China"), conformed to plural via patch_note_bodies_r4.py (the ch06 body already read plural).
  glossary.json 白区 flipped to status "decided" with en "the White areas".
- Anchor move: normalizing the ch37 reading broke the frame note's anchor "4 April 1933 at Longhua
  Prison"; patch_note_bodies_r4.py moved it to "April 4, 1933, at Longhua Prison" (verified a substring
  of the post-conform reading; qa_epub confirms it resolves).
- 海格路 Avenue Haig, 马斯南路 Route Massenet, 大美晚报, 反省院: grepped ch29-ch37, NONE recur in range
  (done in earlier rounds). Whole-book stray grep for every authority OLD form (Haige Road, Massenet
  Road, Laozha Police, Da Mei Wan Bao, the Wusong bar, the Reflection Institute, "a piece of theatre"):
  0 remaining after R4.

### Scene-break review (commissioner directive; ch29-ch37)

Reviewed all nine units against the calibrated principle (add only at a genuine jump in place, time AND
vantage where the new scene stands apart; leave camera-flips inside a continuous cross-cut and
causally/aurally sutured cuts hard). NO new breaks or datelines were warranted, matching R2 (ch11-ch19)
and R3 (ch20-ch28):
- Left with 0 breaks as genuinely single continuous scenes: ch29 (one continuous chase following Chen
  Qianli from the Laoximen teahouse across the dyeworks to the Maochang coal-yard trap -- a journey, one
  vantage, one day, no hard cut); ch34 (the whole chapter is one continuous night intercut between two
  rooms of one building -- Wei Dafu's interrogation and the Ye Qinian/Lu Zhongde conference; a break was
  weighed at the Wei-Dafu-room -> conference-room shift, para 49, but left hard: it is a causally
  sutured cross-cut, Lu Zhongde carrying what Wei Dafu said straight into the next room, and a vantage
  change alone is not enough); ch36 (a single continuous letter); ch37 (documentary lists -- the H3
  section headings do the structural work, and the "......" marks are abridgment, not scene cuts).
- Already segmented at their genuine scene changes, left unchanged: ch30 (3 breaks: park -> the "first
  meeting" flashback -> Scotto Cup -> the Dong home), ch31 (1 dateline + 1 break: cemetery confrontation
  -> the Caohejing phone call; the long Ye Tao death flashback is dialogue-embedded, not a cut), ch32 (2
  breaks: tavern -> Fahua dairy shed -> next-morning Shen Bao), ch33 (1 break: the North Station
  interrogation -> the Zhengyuan Hotel), ch35 (5 breaks across the cross-cut climax). The built EPUB
  renders exactly these counts (grep class="brk" = 56, class="dateline" = 7 book-wide, unchanged by R4).

### Whole-book reconciliation (final-round task) -- inversions resolved

- Zhonghui Trust Bank (中汇银行): logged as "unnoted, add at ch10" -- found ALREADY noted at ch10 (a real
  Du Yuesheng 1929 bank with a trust department; also glossed at ch17). RESOLVED: no action needed; the
  handoff item was stale.
- The tram (first appears ch07; note at ch29): DECIDED to LEAVE the ch29 note as specifically the French
  Concession tram company (Compagnie Francaise, with the first/third-no-second class characterization);
  the ch07 tram is a generic Settlement tram named in passing, and a general Settlement-tram note there
  would be low-value padding. No ch07 note added.
- The Central Liaison Bureau / 中央交通局 (first named ch07; courier-lines note at ch15): DECIDED to LEAVE
  the note at ch15. The dedicated note is about the clandestine courier-line apparatus, whose substantive
  first treatment is ch15; at ch07 the bureau is only named in passing. Relocating a rich courier-lines
  note away from where the courier lines are the topic would serve the reader worse.
- The Peach Blossom Spring / Tao Yuanming allusion (ch22 opera lyric; dedicated note at ch28 Xiaotaoyuan
  title payoff): LEFT at ch28 (a deliberate plot-payoff, per the handoff).
- Dongjiadu (董家渡): first appears ch13, unnoted book-wide -> fresh first-appearance note added at ch13
  (see the new-notes list). CLOSED.
- Women's Normal University (北京女子师范大学): checked -- already noted at ch26 (its first appearance, the
  Duan Qirui 1925 dissolution, Lu Xun), covering the ch31 and ch37 recurrences. No action.
- The Central Statistics Bureau / 中统 (ch37) and the Party Affairs Investigation Section (党务调查科): the
  ch03 note already names 党务调查科 as "the forerunner of the wartime Bureau of Investigation and
  Statistics (中统)", so ch37's "Central Statistics Bureau" is covered; the new ch35 note adds the 军统
  side of the pair.
- Decided-rendering drift grep: 97 "decided" glossary renderings grep-counted across all 37 built units;
  each referent carries one rendering, no drift. TOC links all 37 units; note numbering sequential 1-338
  end to end (qa_epub enforces both).

### Checks run (R4)

- anchor_check.py per unit before apply_edits.py (ch13, ch29, ch30, ch32, ch34, ch35): no anchor
  collisions. Edit-parse pre-verified (parse_edits + count each OLD/anchor == 1; named-entity scan
  clean) before applying, per the R3 window-bleed lesson; two blank lines between every TOUCH block.
- apply_edits.py: 4 prose conformances (ch34 x2, ch35 x2, all the Wusong-bar TOUCH) and 7 new notes
  across six units (ch13, ch29, ch30, ch32, ch34, ch35). conform_r4.py: ch37 reading + ch37b_en.json
  date normalization and ch34/ch35 en.json Wusong sync, all exact-count guarded. patch_note_bodies_r4.py:
  8 note-body edits (7 date normalizations + the ch11 White-areas number fix), 1 anchor move, and the
  glossary 白区 update, each guarded.
- check_structure.py --pairs data/zh/<id>.txt: paragraph parity OK for all nine
  (46/68/71/74/102/58/79/11/38).
- check_numbers.py --noise check_noise.txt on regenerated bilinguals for the units whose reading/en.json
  changed (ch34, ch35, ch37 via assemble_ch37.py): 0 unresolved (the date reorderings preserve every
  numeral value).
- register_tics.py --profile ch29-ch37: day-month-date 0 and british-spelling 0 over the range; the
  remaining narration-side batteries (could-only, trailing-besides, nominalization, narration-ellipsis)
  are pre-existing candidates in the FROZEN reading text (informational this round, not touched).
- Build: build_reading_epub.py "out/A Thousand Li of Rivers and Mountains.epub", 37/37 units, 338 notes.
  qa_epub.py: PASS (50 files, 44 documents; 338 references = 338 bodies = 338 backlinks; numbering
  sequential 1-338; all links resolve). Spot-read of the built xhtml: all 7 new note markers present,
  the moved ch37 anchor and the normalized ch37 dates render, no double-encoded entities, scene
  typography intact (brk=56, dateline=7).
- Deliverable stamped with stamp_deliverable.py R4.

HONEST NOTE ON DENSITY (R4). Like R1 (~15/chapter of new notes), R2 (~2.6/chapter) and R3 (~1.4/chapter),
R4 lands well under the directive band: 7 new notes across nine units (~0.8/chapter). The launching chat
and CORRECTIONS.md gave no "push harder toward the band" instruction, so the standing no-pad policy
governs (a note must say something a no-background reader needs; padding is the failure mode). R4's range
is the most recycled of all: it is the resolution, revisiting places, people and organizations already
footnoted at their first appearance across R1-R3 (Longhua and its Bao'en Pagoda and peach blossoms at
ch03; the Zhanyuan/瞻园, Party Affairs Investigation Section, Special Operations Headquarters, Shence Gate
and soldiers' shelter-vault; the Nineteenth Route Army and the January 28 Incident with the Commercial
Press burning; Hongkou Park, Nekrasov, China Merchants, jianren rank, Suzhou Creek, the courier lines and
the painting the mission is named for -- all already noted). It also contains the book's two shortest
units: ch36 (a 553-character interior letter, whose real referents are all covered at ch03 -- capped at
1) and ch37 (the documentary appendix, already carrying the round's densest and most careful apparatus:
the Longhua Twenty-Four / 7 Feb 1931 anchor and the Qingming-dated invention, the 死间 "dead agent" from
Sun Tzu, the 践/praxis character, 拨乱反正, the unnamed informant -- capped at 6). ch33 (a single-room
interrogation) genuinely capped at 2, its real referents (North Station/Zhabei/January 28, the
self-surrender/reflection-institute machinery) all noted. This is the same recycling the three prior
HONEST NOTE ON DENSITY entries record, not a failure to look: every unit was read in full and grepped
against the whole notes.json and the ch01-ch28 reading files before any note was written.

The book is COMPLETE. See COMPLETION.md for the full completion report.
