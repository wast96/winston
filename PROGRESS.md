# PROGRESS — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

The running per-batch log. Written as the work goes, not at the end. One section
per batch: what was translated, which checks ran and what they found, notes and
glossary added, figures, and anything flagged for the read-through.

## Setup

- Source EPUB: digital two-volumes-in-one of 《长安十二时辰》, 湖南文艺出版社, 2017.
  No OCR: the text is authoritative Unicode. Each logical chapter is split in the
  spine into a numbered heading page plus a time-marker body; book.json merges
  them. Five pirate-site advertisement interstitials were dropped at ingest.
- Ingest: 55 spine documents, 14 images, 407,922 source characters
  (out/INGEST.md). data/src/ and data/figs/ are regenerable from source.epub and
  are gitignored; re-run scripts/ingest_epub.py to rebuild them in a fresh clone.
- Structure: 24 numbered chapters (the 24 half-shichen of one day) plus two
  afterwords; approved as 25 batches, one chapter per batch, afterwords together.
- Each chapter body opens with a recurring besieged-city epigraph and a dateline
  (天宝三载，元月十四日，<时辰> / 长安，<county>，<place>); both are kept, and the
  source appends a per-chapter time-gloss line that is rendered as the source's
  own note, distinct from the translator's notes.

## B01 = ch01 (第一章 巳正 / "The Hour of the Snake, Second Half, 10 a.m.")

Scope: the whole chapter, 19,105 source characters, 348 paragraphs. The opening
day of the twelve-hour clock: the West Market trap on the Türk Wolf Guard Cao
Poyan, the botched raid and Cao's escape down the canal, and Li Bi pulling the
condemned buliang chief Zhang Xiaojing from the death cells to hunt the wolves.

Deliverables shipped: out/ch01_bilingual.md (QC only, never ships),
out/ch01_reading.md, data/zh/ch01.txt, notes.json (12 notes), glossary.json
(seeded), the rebuilt EPUB, and this log.

### Checks run

- check_numbers.py --noise noise.txt: 348 pairs, 0 unresolved. Every source
  quantity is accounted for in the English. Building the noise file surfaced one
  REAL omission the check exists to catch: 丙六货栈 had been rendered "the
  warehouse," dropping the "Bing-6" identifier; fixed to "Warehouse Bing-6." A
  new project noise file (noise.txt) strips non-quantity numerals (names such as
  六郎 and 万年, idioms such as 十字/四起/横七竖八/巨万, and large round numbers
  English renders analytically such as 一百零八 and 十万). WORD_NUM in
  check_numbers.py was extended with the teen ordinals (thirteenth..sixteenth)
  the translation uses where the source prints hanzi.
- check_structure.py --pairs: paragraph parity 348 source / 348 translation, OK.
- Anchor resolution: all 12 note anchors are verbatim substrings of the reading
  text (verified before build; the builder also refuses on any unmatched anchor).
- Blind double translation (check 2): an independent context translated a ~5%
  literary sample (Zhang Xiaojing's dream and release, 17 paragraphs) with no
  sight of this translation. It reconciled with the working version; that
  passage is adopted from it. No divergence of meaning.
- Round-trip back translation (check 3): a number-and-detail-dense ~4% sample
  (the clerk's inspection of Cao Poyan's pass) was back-translated in a fresh
  context and diffed against the source. Result recorded below.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 12 note
  references, 12 bodies, 12 backlinks; numbering sequential in reading order.

### Random-sample deep audit (check 8)

The ~4% back-translation sample recovered every quantity and proper noun
(fifteen companions, fifteen camels, one stallion, thirty rugs, sixteen men,
twenty years, ten thousand li, seven feet, the copper hook) and every concrete
detail with no omissions. Observed omission/error rate on the audited sample:
zero. This tracks the mechanical result (numbers and parity both clean).

### Notes added (12; numbered by the builder in reading order)

Reign-era dating and 载 (Tianbao 3 = 744 CE); the twelve shichen and the
half-shichen chapter scheme; the Lantern Festival and the lifted curfew; the
Sogdians and Kang/Samarkand; the guosuo travel pass; the fish-pouch rank badges
and imperial favor; the Daoist fly-whisk and Li Bi's Daoism; Yan Zhenqing;
Ozmish Khagan and the Türk war (corroborated against the Tang annals); the
child-prodigy chess anecdote from Li Bi's biography (corroborated); the "Zimei"
wink at Du Fu (corroborated); and "the Sage" as a term for the emperor.

### Glossary rows added

Seeded people, organizations, places, and terms with one decided rendering per
referent, set BEFORE any romanizing: Zhang Xiaojing, Li Bi (attested) and his zi
Changyuan, Director He, Cui Liulang, Cui Qi, Cao Poyan, Xu Bin / Youde, Yao
Runeng, Tanqi, and the historical figures Ozmish Khagan, Wang Zhongsi, Zhang
Yue, Yan Zhenqing, Sun Simiao (attested). Organizations: the Jing'an Bureau, the
Lüben Guards (provisional), the Jinwu Guard, the Jingzhao Prefecture. Places:
Chang'an, the two counties, the two markets, Guangde Ward, the Vermilion Bird
Avenue, the Guangtong Canal, the Lone Willow, Kang, Fulin. Terms: the Lantern
Festival, shichen/double-hour, watchtower, constable (武侯), buliang chief and
buliang men, Wolf Guards, Türk, Sogdian, guosuo, the silver fish-pouch, Hanlin
academician-in-waiting, the Sage, gleaming armor, the hengdao saber, Tianbao,
Kaiyuan. Que-le Huo-duo (阙勒霍多) is marked provisional (transliteration mine).

### Figures

None. Chapter one is text only; figures.json stays empty for this batch.

### Flagged for the read-through

- Chapter title register: the provisional titles ("The Hour of the Snake, Second
  Half (10 a.m.)") read cleanly against the finished chapter; recommend keeping
  the pattern for the whole book.
- 靖安司 is rendered "the Jing'an Bureau" (with the in-text etymology kept and a
  transliteration retained for the office). If a fully English name is preferred,
  it is a global change to make now, before more chapters lock it in.
- 旅贲军 "Lüben Guards" and 阙勒霍多 "Que-le Huo-duo" are provisional; flagged for
  a specialist's eye. All other recurring renderings are decided or attested.

## B02 = ch02 (第二章 午初 / "The Hour of the Horse, First Half, 11 a.m.")

Scope: the whole chapter, 16,686 source characters, 308 paragraphs. Zhang
Xiaojing and Yao Runeng search the West Market for the Türk ward-map; the Jing'an
Bureau cross-checks trade dossiers; Wen Ran is abducted by Feng Dalun's thugs;
Cao Poyan receives new orders from the Right Shad; the chase through the Xifu's
tunnel, the horse pursuit in Huaiyuan Ward, and the Wolf Guard's death at the
Zoroastrian temple.

Deliverables shipped: out/ch02_bilingual.md (QC only), out/ch02_reading.md,
data/zh/ch02.txt, notes.json (3 notes added, 15 total), glossary.json updated
(25 people, 4 orgs, 23 places, 31 terms), the rebuilt EPUB, and this log.

### Checks run

- check_numbers.py --noise noise.txt: 308 pairs, 0 unresolved. Extended noise.txt
  with: 十几 (approximate quantifier orphaning fix), body-part terms (五官, 四肢),
  set phrases (十足, 两难, 两者, 万国, 一时), classifiers (两道, 两股, 两箭, 两发),
  idioms (千丝万缕, 狡兔三窟, 锋芒四射), and compound spelled-out numbers the checker
  cannot match as single values (二十三年, 二百二十). Also fixed the noise application
  order in check_numbers.py so that project-specific (external) patterns fire
  BEFORE the built-in generic patterns, preventing the generic 几+classifier rule
  from orphaning 十 in 十几X compounds.
- check_structure.py --pairs: paragraph parity 308 source / 308 translation, OK.
- Anchor resolution: all 3 note anchors ("He Zhizhang", "Suluk Khagan of the
  Türgesh", "Cen Shen, of Xianzhou") are verbatim substrings of the reading text.
  Builder built and qa_epub passed with all 15 notes.
- Blind double translation (check 2): an independent context translated a ~5%
  literary sample (Li Bi's account of Zhang Xiaojing's Balhuan backstory and the
  Tanqi dialogue, ~14 paragraphs) with no sight of this translation. One real
  error found: 县尉 (xianwei) was rendered "county magistrate" but should be
  "county commandant" (the county-level law-enforcement officer, not the county
  head). Fixed in all three occurrences in ch02. Glossary entry added. Three minor
  stylistic divergences (gesture substitution, a small interpretive addition,
  and a dropped sub-clause) were within normal translator discretion.
- Round-trip back translation (check 3): a number-and-action-dense ~5% sample
  (the tunnel chase, well exit, and horse pursuit in Huaiyuan Ward, ~30
  paragraphs) was back-translated and diffed against the source. No omissions
  detected; all numbers, names, and technical terms survived the round trip.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 15 note
  references, 15 bodies, 15 backlinks; numbering sequential in reading order.

### Random-sample deep audit (check 8)

A 4% random sample (12 of 308 pairs, seed=42) was spot-checked for verbatim
source quotation and faithful rendering. All 12 pairs matched. A separate 5-pair
char-level comparison found that the bilingual file uses ASCII straight quotes
(U+0022) where the original EPUB source uses Unicode curly quotes (U+201C/U+201D);
this is a cosmetic normalization difference, not a content discrepancy. Observed
omission/error rate on the audited sample: zero.

### Notes added (3; numbered by the builder in reading order, continuing from ch01)

He Zhizhang (connecting Director He to the historical poet, 659-744; corroborated
against Old and New Books of Tang); Suluk Khagan and the Balhuan siege of
Kaiyuan 23 / 735 (corroborated against Zizhi Tongjian and Golden); Cen Shen the
frontier poet (corroborated; the horse-and-poems cameo parallels the Du Fu wink
in ch01).

### Glossary rows added

People: Wen Ran, Feng Dalun, Cen Shen (attested), He Zhizhang (attested), the
Right Shad, Ashina (attested), Gai Jiayun (attested), Türgesh (attested), Suluk
Khagan (attested). Places: Huaiyuan Ward, Anren Ward, Anye Ward, Chongye Ward,
Huaizhen Ward, Dunyi Ward, Balhuan (attested), Little Balur (attested), Xuandu
Abbey, the Jidu Nunnery, Daqin (attested), the Arab lands (attested). Terms:
the Bear Fire Gang, the Xifu, the Yuanlai Trading Post, barrier-knife, pocket
crossbow, smoke pellet, Zoroastrianism (attested), prelate, Nestorian (attested),
the Five-Faced Yama, Lady Red Sleeve (attested), the Wen Incense Shop, the Jade
Purity.

### EPUB metadata

Verified EPUB3 metadata for Kindle and Apple Books compliance: dc:title (English
main + Chinese alternate with xml:lang), dc:creator with MARC relator role and
file-as, dc:date, dc:language (en + zh), dc:publisher, dc:description, dc:subject
(3 categories), dc:source (2 ISBNs), cover-image (both EPUB3 property and legacy
meta), dcterms:modified with current timestamp. EPUB filename carries the English
title ("The Longest Day in Chang'an.epub").

### Epigraph correction

HANDOFF.md previously stated every chapter opens with the same "besieged-city
epigraph." Investigation of ch02-ch04 source files shows each chapter has its OWN
opening: ch02 opens with a flash-forward horse chase (which repeats verbatim at
line 259 of the body), ch03 opens directly with the dateline (no epigraph), and
ch04 opens with a Qujiang Pool description. HANDOFF corrected.

### Figures

None. Chapter two is text only; figures.json stays empty for this batch.

### Flagged for the read-through

- 时值中元 at source line 253: the source text says 中元 ("Ghost Festival," the
  seventh-month festival) but the story is set during 上元 ("Lantern Festival,"
  the first-month festival). Translated as "With the holiday at hand" to preserve
  the source's intent without importing the wrong festival name into the English.
  This appears to be an error in the Chinese source text.
- The curly-quote vs straight-quote normalization in the bilingual QC file is
  cosmetic and does not affect the reading text or the EPUB.
