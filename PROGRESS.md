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
