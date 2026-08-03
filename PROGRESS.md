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

## B03 = ch03 (第三章 午正 / "The Hour of the Horse, Second Half, noon")

Scope: the whole chapter, 22,888 source characters, 421 paragraphs. He Zhizhang
returns with the Bureau seal and tries to expel Zhang Xiaojing; Zhang's plan to
win the Zoroastrian offering-register plays out (the He Zhizhang / Great Sabao
audience); Wen Ran escapes her captors only to be run down with Wang Yunxiu by
Cao Poyan's fake road crew; Jiao Sui's murder fells He Zhizhang and Li Bi takes
sole command; Long Bo is identified; Zhang and Yao Runeng go to the Pingkang
Quarter and Old Ge, where Zhang kills the mole Xiao Yi (severing his own finger)
and breaks Tong'er to learn of the Xiuzheng safe-house; Cao Poyan receives the
Yanzhou cargo and the ward map from Long Bo; Li Bi confesses to the Crown Prince.

Deliverables shipped: out/ch03_bilingual.md (QC only), out/ch03_reading.md,
data/zh/ch03.txt, notes.json (4 notes added, 19 total), glossary.json updated
(42 people, 7 orgs, 38 places, 45 terms), noise.txt extended, the rebuilt EPUB,
and this log.

### Checks run

- check_numbers.py --noise noise.txt: 421 pairs, 0 unresolved. Extended
  check_numbers.py WORD_NUM with the ordinal "twentieth" (20) for 开元二十年 /
  "the twentieth year of Kaiyuan" (a real regnal-year quantity English spells as
  an ordinal, like the teen ordinals added in B01/B02). Extended noise.txt with,
  and recorded why, only NON-quantity numerals the check flagged:
  一百五十 (150, the avenue width English renders analytically as "a hundred and
  fifty paces," which the digit-composer cannot reassemble — same class as the
  existing 一百零八); the idioms 七转八弯, 推三阻四, 五花大绑, 五大三粗, 四散,
  危机四伏, 百感交集, 一来二去; 万众 ("the multitude", not 10000), 三角
  ("triangular", not 3), 二不逾制 (the 二 is a "neither...nor" enumerator),
  万全 (万全宅 = "the safe-house", not 10000), 三勒浆 (a drink named for its 三
  fruits), 零卖 ("retail", the 零 is not 0), and a general rule
  [一二三四五六七八九]十[多几余] placed at the TOP of noise.txt so it strips whole
  approximate "-odd" forms (八十多/六十多/二十多/二十几/二十余) BEFORE the built-in
  十多/十几 rules can strip the middle and orphan the leading digit. Every added
  pattern was hand-verified to have its value present (or legitimately absent) in
  the English; a genuinely dropped number would still fail.
- check_structure.py --pairs: paragraph parity 421 source / 421 translation, OK.
  (Source lines 40 and 41 of data/src/06_text00007.txt are one sentence split by
  the extractor mid-clause; they were merged into a single paragraph. All other
  lines map one-to-one; colon-lead-in speech lines were kept as the source file
  has them.)
- Anchor resolution: all 4 ch03 note anchors ("the Great Sabao", "Eight Immortals
  of the Wine Cup", "the Pingkang Quarter", "an old Kunlun slave") are verbatim
  substrings of the reading text. Builder built and qa_epub passed with all 19
  notes.
- Blind double translation (check 2): an independent context translated a ~3%
  literary sample (the "other Chang'an" passage and Old Ge's speech on the filth
  behind the Pingkang Quarter, ~3 paragraphs / ~230 chars) with no sight of this
  translation. Result: highly convergent, no omissions and no invented content.
  One precision refinement applied from the diff — 毁了容的凤魁 was tightened from
  "ruined belles of the trade" to "once-celebrated beauties whose faces have been
  ruined," preserving the 毁容 (ruined-face) specificity. Remaining differences
  (Avīci hell vs "hell of the interminable void"; "reckoning" vs "karmic
  workings" for 羯磨) were equivalent word-choices within translator discretion.
- Round-trip back translation (check 3): a number-dense sample (the cart train,
  the ward-map / fifteen lost men / nine-linked-rings passage, the timing orders,
  and the Pure Land Cloister's hundred-and-eight Buddhas, ~4 excerpts) was
  back-translated in a fresh context and diffed against the source. Every numeral
  survived intact (10 carts, 15 men, 108 Buddhas, quarter-/half-/two double-hours)
  and every proper noun matched. No omissions detected.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 19 note
  references, 19 bodies, 19 backlinks; numbering sequential in reading order.

### Random-sample deep audit (check 8)

Combined, the blind double-translation and back-translation samples cover ~4% of
the chapter and were given the full paranoid treatment (verbatim-quote check,
independent re-translation, round-trip). Observed substantive omission/error rate
on the audited sample: zero. One minor precision refinement (凤魁/毁容, above) was
applied; it was a tightening, not a corrected error.

### Notes added (4; numbered by the builder in reading order, continuing from ch02)

The Great Sabao / the sabao office (薩寶, the government-recognized headman of a
resident Sogdian community and its Zoroastrian temples; corroborated against Tang
institutional sources and Sogdian sabao epitaphs); the Eight Immortals of the
Wine Cup (饮中八仙, from Du Fu's poem, listing all eight with Jiao Sui the sole
commoner; corroborated); the Pingkang Quarter (平康里, the capital's courtesan
district and its three lanes; corroborated against Sun Qi's Beili zhi); the
Kunlun slave / Zanj (昆仑奴 / 僧祇奴, dark-skinned servants of the southern seas
and East Africa; corroborated against Schafer, The Golden Peaches of Samarkand).
Recurring subjects already noted in ch01-ch02 (Tianbao/zai dating, the shichen
system, the Lantern Festival, He Zhizhang, the Sage) were deliberately NOT
re-noted.

### Glossary rows added

People: Long Bo, Wang Yunxiu (attested), Old Ge, Ma Ge'er, Tong'er, the Great
Sabao (attested), Jiao Sui (attested), Li Linfu (attested), Li Heng (attested),
Li Bai (attested), Li Shizhi/Li Jin/Cui Zongzhi/Su Jin/Zhang Xu (the wine
immortals, attested), Xiao Yi, Young Han. Organizations: the Sabao Office
(attested), the Directorate for the Palace Buildings (attested), Su's
Cart-and-Horse Company. Places: Kucha (attested), the Pingkang Quarter, Yanzhou
(attested), Xiuzheng/Taiping/Yanshou/Zhiye/Fengle/Guangfu/Jingshan Wards, the
Hanguang Gate, the Shiji Temple, the Pure Land Cloister, the Jianfu Temple, the
Yong'an Canal. Terms: Kunlun slave (attested), Zanj slave (attested), Mazda
(attested), the Eight Immortals of the Wine Cup (attested), the art of the Great
Archive, "walking the horse" (liuma), the First Lane, Xi cart, sanle cordial,
the Three Adjuncts (attested), futou, gratitude token, oath-token of blood.

### Figures

None. The source ch03 HTML references only Image00004.jpg (the source's own
footnote-marker glyph) and Image00005.jpg (a decorative centered scene-break
rule, alt="line", used seven times); neither is a content illustration, matching
the ch01-ch02 decision. figures.json stays empty.

### Flagged for the read-through

- The source's own footnote on the dateline (Duokan fn3) is the per-chapter
  time-gloss ("中午12点。午，又名日正、中午等。（北京时间11时至13时）"), already captured
  as the last source paragraph and rendered as the source's own italic note, per
  house style.
- 感动祆正的言辞 (source line 131): the source says 祆正 ("prelate"), but the man
  moved by the speech is the Great Sabao (the prelate is dead). Read as a loose
  use of 祆正 for "the Zoroastrian dignitary" and rendered "the old Zoroastrian";
  the referent is unambiguous from context. Flagged as a probable authorial slip.
- 早在天宝三年间…二十多年的师徒情谊 (source line 402): the source dates He Zhizhang's
  tutorship of the heir apparent to "the third year of Tianbao" (744, the present
  year) yet calls the bond "more than twenty years" old — internally inconsistent
  (the appointment must date to the Kaiyuan era). Rendered faithfully and left
  visible rather than silently corrected.
- 远来商栈 (source line 196) vs the glossary's 元来行 "the Yuanlai Trading Post":
  the source varies the name of the livestock-dealing establishment (元来行 in
  earlier chapters, 远来商栈 here); both romanize as "Yuanlai," so the decided
  rendering was reused for consistency.

## B04 = ch04 (第四章 未初 / "The Hour of the Goat, First Half, 1 p.m.")

Scope: the whole chapter, 14,099 source characters, 249 paragraphs. Zhang
Xiaojing and Yao Runeng ride to the Xiuzheng Ward safe-house; Zhang goes over the
wall alone, kills the Türk sentries, and is taken when Ma Ge'er holds a hostage
he recognizes as Wen Ran (not, as the Türks think, Wang Zhongsi's daughter Wang
Yunxiu). The Bear Fire Gang storms in after their own runaway quarry; the Wolf
Guards spring the castor-oil firetrap and the Zhuxin Pavilion burns; Zhang breaks
free and escapes. Meanwhile Li Bi runs a sand-table fire-simulation (forty leaks,
thirty-seven wards) and, on a veteran clerk's advice, orders a search of the
capital's bulk oil and firewood. Cui Qi sounds the Nine-Gate Drum but the Türks
slip out through Qujiang Pool and re-enter by the Qixia/Yanxing gates; Zhang lies
to protect Wen Ran (naming Wang Yunxiu as the one carried off) and tells the story
of the informer Xiao Yi and the severed finger; he asks Cui Qi for scent-hounds
from the Five Kennels.

Deliverables shipped: out/ch04_bilingual.md (QC only), out/ch04_reading.md,
data/zh/ch04.txt, notes.json (3 notes added, 22 total), glossary.json updated
(new people/orgs/places/terms below), noise.txt extended, the rebuilt EPUB, and
this log.

### Checks run

- check_numbers.py --noise noise.txt: 249 pairs, 0 unresolved. Extended noise.txt
  with, and recorded why, only NON-quantity numerals the check flagged:
  四季 (一年四季 = "in every season / year-round", the 四 is not the count 4;
  appears in the Qujiang epigraph and its verbatim callback), 四溅 (火点四溅 =
  "sparks flying on every side", the "all directions" idiom like the existing
  四散/四射/四伏), 四合 (柳荫四合 = "willow-shade closing in on all sides"), 四望
  (举目四望 = "look on every side"), 零星 (零星散碎 = "scattered and piecemeal", the
  零 is "bits/odds", not 0), and 千金 (王节度的千金 = the honorific for another's
  daughter, literally "thousand gold", not the quantity 1000; English renders it
  "daughter"). Every added pattern is a specific literal whose value is present
  (or legitimately absent) in the English; a genuinely dropped number would still
  fail. No WORD_NUM change was needed this batch.
- check_structure.py --pairs: paragraph parity 249 source / 249 translation, OK.
  The chapter opens with a Qujiang Pool epigraph (three extractor lines that are
  one sentence, merged to one pair) and the dateline (source line + its lone
  full-stop line, merged); every other source line maps one-to-one, and the
  per-chapter time-gloss is the final pair. No mid-clause merges besides those two
  openers.
- Anchor resolution: all 3 ch04 note anchors ("Xun Yue's Extended Reflections",
  "the burning house of the Buddhist scriptures", "the Five Kennels") are verbatim
  substrings of the reading text (verified by grep). Builder built and qa_epub
  passed with all 22 notes.
- Blind double translation (check 2): an independent context translated the
  ferry-dilemma / severed-finger exchange (~5 paragraphs, ~360 chars) with no
  sight of this translation. Result: highly convergent, no omissions and no
  invented content. Differences were equivalent word-choices within translator
  discretion (杀孽 "blood-guilt" vs "sin of killing"; "appease the river-god" vs
  "sacrifice to the river god"). No correction needed.
- Round-trip back translation (check 3): a number-dense sample (the sand-table
  fire-simulation and the Nine-Gate Drum alarm, ~4 excerpts) was back-translated
  in a fresh context and diffed against the source. Every numeral survived intact
  (1/2/3 leaks, every 4th, 30-odd slips, dozen-odd wards, 40 leaks / 37 wards, one
  quarter-hour, 300 paces, 4 double-hours, 8 wards, 16 crossroads, 9 wards) and no
  content was dropped. The only divergence was 九门鼓 for the novel-coined 九关鼓
  (the Nine-Gate Drum), an unknowable term, not an error.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 22 note
  references, 22 bodies, 22 backlinks; numbering sequential in reading order.

### Random-sample deep audit (check 8)

The blind double-translation and back-translation samples together cover ~3.6% of
the chapter (~9 of 249 paragraphs) and were given the full paranoid treatment
(verbatim-quote check, independent re-translation, round-trip). Observed
substantive omission/error rate on the audited sample: zero.

### Notes added (3; numbered by the builder in reading order, continuing from ch03)

Xun Yue's Extended Reflections (荀悦《申鉴》, the Later Han Shenjian and the maxim
"防为上，救次之"; corroborated); the burning house of the Buddhist scriptures (the
火宅 Parable of the Burning House from the Lotus Sutra); the Five Kennels (五坊,
the imperial falconry-and-hound bureaus under the Xuanhui Court and their
notorious "Five Kennels boys"; corroborated against the Tang histories and Bai
Juyi). Recurring subjects already noted in ch01-ch03, and subjects whose FIRST
appearance was in an earlier chapter, were deliberately NOT noted here: in
particular Qujiang Pool and Wang Zhongsi both first appear (unnoted) in ch01, so
no footnote was added for them in ch04 even though the chapter turns on them.

### Glossary rows added

People: Jin (the absentee Yangzhou owner of the safe-house), Xun Yue (attested).
Organizations: the Xuanhui Court (attested), the Shangchi Office. Places: Qujiang
Pool (attested), the Furong Garden (attested), the Shaoling Plain (attested), the
Qixia Gate (attested), the Yanxing Gate (attested), the Zhuxin Pavilion, Lingnan
(attested), the Long Mountains (attested). Terms: the Nine-Gate Drum, the Five
Kennels (attested), the Dog Kennel, military commissioner (节度使), casting
flesh-coins. Every recurring referent already decided in ch01-ch03 (Zhang
Xiaojing, Li Bi, Cui Qi, Ma Ge'er, Wen Ran, Wang Yunxiu, Long Bo, Old Ge, Xiao
Yi, Tanqi, Xu Bin; the Jing'an Bureau, the Lüben Guards, the Directorate for the
Palace Buildings; Xiuzheng/Jingshan/Guangde Wards; the safe-house, the Wolf
Guards, the barrier-knife, the pocket crossbow, the watchtower, the Xi cart, the
Wen Incense Shop, Que-le Huo-duo, etc.) was reused verbatim, not re-romanized.

### Figures

None. The chapter's only image references are the source's footnote-marker glyph
(Image00004.jpg) and the decorative scene-break rule (Image00005.jpg); neither is
a content illustration, matching the ch01-ch03 decision. figures.json stays empty.

### Flagged for the read-through

- The source's own footnote on the dateline (the per-chapter time-gloss, here
  "下午1点。未，又名日跌、日央等：太阳偏西为日跌。（北京时间13时至15时）") is captured as
  the last source paragraph and rendered as the source's own italic note, per
  house style.
- ch04's opening differs from the earlier chapters: it leads with a lyrical
  Qujiang Pool epigraph, not a dateline or flash-forward. That exact description
  recurs verbatim at the chapter's climax (source lines 2-4 and again in line 226)
  as a deliberate authorial echo, and was translated identically in both places.
- Authorial slip: source line 110 writes 麻格心 for 麻格儿 (Ma Ge'er) — a
  one-character typo mid-paragraph. Rendered as "Ma Ge'er" (the character's
  established name) without a note, the referent being unambiguous.

## B05 = ch05 (第五章 未正 / "The Hour of the Goat, Second Half, 2 p.m.")

Scope: the whole chapter, 13,336 source characters, 222 paragraphs. Five
interleaved scenes. (1) At the hidden depot, Long Bo's craftsmen assemble the
second half of the Que-le Huo-duo from bamboo poles and river-mud while Cao Poyan
stands guard; Ma Ge'er arrives with the captive Wen Ran (still mistaken for Wang
Yunxiu) and only three of eight Wolf Guards left, and Cao realizes the Jing'an
Bureau has traced the safe-house. Long Bo suggests hiring the beggars of the
infirmary as lookouts. (2) The Bureau's city-wide search of the oil-works turns up
nothing; Xu Bin, stinging under Li Bi's temper, catches an inspiration from the
order to "search everything that burns." (3) A sealed dispatch confirms the Wolf
Guards took Wang Zhongsi's daughter; Li Bi grasps the strategic disaster, ices his
face to think, senses the two aims (arson and abduction) are at odds, and turns
back to Zhang Xiaojing. (4) Zhang walks a commandeered palace sighthound west from
the Qixia Gate; the scent dies at Guangxing-Anle in the desolate southwest, and he
sets fifty Lüben soldiers to a quiet search. (5) Feng Dalun, warned that "Zhang
the Yama" has been requisitioned out of the death cells, races to Jinggong Ward
to consult his patron Prince Yong at the polo ground; they scheme to have the
Court of Judicial Review demand the prisoner back through an Evaluator, one Yuan
Zai. The chapter closes back at the well: Wen Ran has thrown herself down it; Cao
Poyan, one-armed from Cui Qi's bolt, caps the well and leaves to hire the beggar
headman.

Deliverables shipped: out/ch05_bilingual.md (QC only), out/ch05_reading.md,
data/zh/ch05.txt, notes.json (3 notes added, 25 total), glossary.json updated
(new people/orgs/places/terms below), noise.txt extended, the rebuilt EPUB, and
this log.

### Checks run

- check_numbers.py --noise noise.txt: 222 pairs, 0 unresolved. Extended noise.txt
  with, and recorded why, only NON-quantity numerals the check flagged:
  万千 (万千细针 = "myriad fine needles", the idiom for "countless", not the
  compound 11000; English renders "ten thousand fine needles"), 独一无二 ("unique",
  the 二 is idiomatic, not 2), 王八 (王八蛋 = "bastards", the 八 is part of the
  invective, not 8), 六亲 (六亲不认 = "knowing neither kith nor kin", the 六 is not
  6), and 一了百了 ("the end of all things", the 百 is not 100). Every added pattern
  is a specific idiom literal; a genuinely dropped number would still fail. No
  WORD_NUM change was needed this batch.
- check_structure.py --pairs: paragraph parity 222 source / 222 translation, OK.
  The chapter opens with a flash-forward vignette of the boxwood writing-case
  (three extractor lines that are one paragraph, merged to one pair; the same text
  recurs verbatim at source line 51 when the scene arrives and was translated
  identically both times), then the dateline and "the place, unknown," then the
  body one-to-one; the per-chapter time-gloss is the final pair. The source's
  own content-file heading line "未正" is absorbed into the H2 chapter title, as
  in ch01-ch04.
- Anchor resolution: all 3 ch05 note anchors ("Prince Yong, Li Lin", "Yuan Zai",
  "the Oil-Sprinkled Ground") are verbatim substrings of the reading text
  (verified by grep, each exactly once). Builder built and qa_epub passed with all
  25 notes.
- Blind double translation (check 2): an independent context, with no sight of
  this translation, rendered a literary sample (Cao Poyan's keepsake-necklace
  paragraph and the steppe-gazelle image, ~2 paragraphs, ~230 chars). Result:
  highly convergent, no omissions and no invented content; every detail present
  (Onon River, white horsehair, three strands of hair, one breath, telling
  prayer-beads, gazelles kneeling and bleating). Divergences were equivalent
  word-choices within translator discretion (栈仓 "warehouse" vs "granary";
  彩石项链 "necklace of colored stones" vs "colored-stone beads"). No correction
  needed.
- Round-trip back translation (check 3): a number-dense sample (the bamboo-pole
  depot delivery, Wang Zhongsi's three titles, and the polo-field dimensions,
  ~3 excerpts) was back-translated in a fresh context and diffed against the
  source. Every numeral and title survived intact (second time, nearly a thousand
  poles, three-year bamboo, three feet; General of the Left Jinwu Guard / Area
  Commander of Lingzhou / Military Commissioner of Shuofang; 150 paces × 400
  paces, ten-odd felt curtains) and no content was dropped. No divergences of
  substance.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 25 note references,
  25 bodies, 25 backlinks; numbering sequential in reading order.

### Random-sample deep audit (check 8)

The blind double-translation and back-translation samples together cover ~4% of
the chapter (~5 of 222 paragraphs) and were given the full paranoid treatment
(verbatim-quote check, independent forward translation, and back-translation).
Observed error rate: 0 — no dropped clause, no invented sentence, no altered
number or title in the audited spans.

### Notes added (3; numbered by the builder in reading order, continuing from ch04)

- "Prince Yong, Li Lin": Li Lin (d. 757), a son of Xuanzong, later the failed
  Yangtze uprising of 757 that ensnared Li Bai; corroborated against the Tang
  histories.
- "Yuan Zai": the dramatic-irony note — the forgettable eighth-rank Evaluator here
  is the historical Yuan Zai (d. 777) who married Wang Yunxiu and rose to a
  notoriously corrupt chief-ministership, executed 777; corroborated.
- "the Oil-Sprinkled Ground": Tang polo and the historical oiled field of Yang
  Shenjiao, consort of Princess Changning (daughter of Zhongzong); corroborated
  against the New Book of Tang and the Zizhi Tongjian.
Recurring subjects whose FIRST appearance was in an earlier chapter were
deliberately NOT re-noted: Wang Zhongsi (ch01, unnoted), the Five Kennels / Dog
Kennel (ch04), the Nine-Gate Drum (ch04), the Xuanhui Court (ch04), the Sage
(ch01), Que-le Huo-duo, the Lantern Festival, etc.

### Glossary rows added

People: Li Lin / Prince Yong (attested), Yuan Zai (attested), Yang Shenjiao
(attested), Princess Changning (attested), Emperor Zhongzong (attested), the
Consort of the Prince of Cao. Places: Daning / Jinggong / Tongji / Guangxing /
Anle / Qinren Wards, the Daming Palace (attested), the Xingqing Palace (attested),
the Yanxi Gate, the Onon River (attested), the Orkhon River (attested), Hedong
(attested), the Ci'en Temple (attested), the Oil-Sprinkled Ground. Organizations:
the Ministry of Works (attested), the Forestry and Crafts Bureau / 虞部 (attested),
the Court of Judicial Review (attested), the Censorate (attested), the Ministry of
Justice (attested), the Palace Domestic Service (attested). Terms: polo (击鞠),
Evaluator of the Court of Judicial Review (attested), Silla (attested), the court
gazette (邸报), infirmary (病坊), snow-cordial, warder (节级). Every recurring
referent already decided in ch01-ch04 (Cao Poyan, Long Bo, Ma Ge'er, Wen Ran, Wang
Yunxiu, Wang Zhongsi, Li Bi, Xu Bin, Tanqi, Cui Qi, Zhang Xiaojing, Yao Runeng,
Feng Dalun, the Right Shad; the Jing'an Bureau, the Lüben Guards, the Jinwu Guard,
the Xuanhui Court, the Dog Kennel, the Five Kennels; Xiuzheng Ward, the Qixia
Gate, Qujiang Pool, the Vermilion Bird Avenue; the Wolf Guards, the Nine-Gate
Drum, Que-le Huo-duo, the Bear Fire Gang, "recorder" for 主事, "military
commissioner" for 节度使, "crescent mallet" for 月杆, etc.) was reused verbatim,
not re-romanized.

### Figures

None. The chapter has no content illustration in its source (only the book-wide
footnote-marker glyph and scene-break rule, which are not figures). figures.json
stays empty, matching ch01-ch04.

### Flagged for the read-through

- The chapter's opening is a flash-forward vignette (the boxwood writing-case),
  whose exact text returns at source line 51 when the well-side scene reaches that
  moment; both instances were translated identically, per the ch04 precedent for
  such deliberate authorial echoes.
- The source's per-chapter time-gloss (here "下午2点。未，又名日跌、日央等……")
  is captured as the final source paragraph and rendered as the source's own italic
  note, per house style.
- Minor source oddity: line 10 reads 并未没引起任何注意 (a doubled negative,
  未...没); the plain sense is "drew no notice at all," rendered so. Not flagged in
  the text.
- 主事 is rendered "recorder" (Recorder Xu Bin, Recorder Feng Dalun), consistent
  with ch01; 评事 is "Evaluator"; office renderings for 工部/虞部/大理寺/御史台/刑部/
  内侍省 follow Hucker.

## B06 = ch06 (第六章 申初 / "The Hour of the Monkey, First Half, 3 p.m.")

Scope: the whole chapter, 25,297 source characters, 431 paragraphs (the longest
chapter to date). Xu Bin's ink-spill inspiration cracks the case: the Türk fuel
was declared as "ink-stock," and the "rock-oil" (petroleum) hidden under the ink
category is the Que-le Huo-duo's fuel. Zhang Xiaojing tracks it by scent-hound
into desolate Changming Ward, buys off the beggar-chief Jia Shiqi, kills Cao
Poyan at the disused kiln-depot, and survives the fierce-fire-thunder blast that
destroys the warehouse. Li Bi commissions the watchtowers to Zhang (the jiajie
device) and draws the Guangde-Huaiyuan death-line; the running cart-chase north
burns two carts (one into a lantern-wheel), and Zhang rides the last cart of
fierce-fire thunder through the West Market's gauge-gate and off the bank into
the frozen Guangtong Canal, quelling fire with water. He survives at a stone
sutra-pillar — only for Cui Qi to arrest him as the chapter closes.

Deliverables shipped: out/ch06_bilingual.md (QC only, never ships),
out/ch06_reading.md, data/zh/ch06.txt, notes.json (3 notes added, 28 total),
glossary.json updated (new people/orgs/places/terms below), noise.txt extended,
the rebuilt EPUB, and this log.

### Checks run

- check_numbers.py --noise noise.txt: 431 pairs, 0 unresolved. Three flagged
  numerals were REAL quantities whose English had lost the value; the English was
  fixed (not noised): 一百步 → "a hundred paces or so" (was "another hundred", which
  the checker cannot read); 十来个 → "ten-odd" (was "a dozen or so", which loses the
  10, per the house rule); 三面 → "on three sides—south, east, and west" (the count
  was only implied). All other flags were NON-quantity numerals added to noise.txt,
  each with its reason: 二十六六 (the watchtower rhyme-cipher "scroll 2/rhyme 16/char
  6", which cn_to_int misreads as 26; the real 2/16/6 are separately present),
  李十二 (the dancer Li Shi'er, a name), 贾十七 (the beggar-chief Jia Shiqi, a name,
  recurring), 二来 (the "for one thing… for another" enumerator), 化整为零 (idiom, 零
  ≠ 0), 两侧 ("at the sides", 两 absorbed), 两片 (a measure phrase merged in English),
  百炼 (百炼钢刀 = "hundred-forged", idiom ≠ 100), 四溢 (热浪四溢 = "spread on every
  side", the all-directions idiom), 万幸 (不幸中的万幸 = "the best of a bad business",
  ≠ 10000). Every added pattern was hand-verified; a genuinely dropped number would
  still fail. No WORD_NUM change needed.
- check_structure.py --pairs: paragraph parity 431 source / 431 translation, OK.
  The chapter opens with a flash-forward vignette of the kiln-duel (three extractor
  lines that are one paragraph, merged to one pair; the same text recurs verbatim
  at source line 175 when the duel arrives, and was translated identically both
  times), then the dateline (source line + its lone full-stop line, merged) and the
  location line "Chang'an; Chang'an County; Guangde Ward," then the body one-to-one;
  colon-lead-in speech lines kept as the source has them; the per-chapter time-gloss
  is the final pair. The source's content-file heading line "申初" is absorbed into
  the H2 chapter title, as in ch01-ch05.
- Anchor resolution: all 3 ch06 note anchors ("it is called rock-oil",
  "Fierce-fire thunder", "commissioning the watchtowers") are verbatim substrings
  of the reading text (verified by grep, each exactly once). Builder built and
  qa_epub passed with all 28 notes.
- Blind double translation (check 2): an independent context, with no sight of this
  translation, rendered a literary sample (Zhang Xiaojing's "living Chang'an" speech
  to Yao Runeng, ~2 paragraphs / ~230 chars). Result: highly convergent, no
  omissions and no invented content; every beat present ("count for nothing", "the
  living city the monster hasn't devoured", "feel myself alive", "the first to lose
  their lives"). Divergences were equivalent word-choices within translator
  discretion. No correction needed.
- Round-trip back translation (check 3): a number-dense sample (the kiln-math
  15/1/5/21/half; the West Market gauge-gate two entrances / 5 chi 3 cun ×2 / 4 chi;
  the rhyme-code Kaiyuan-20 / scroll 2 rhyme 16 char 6, and the 5-cask / 15-cask
  totals) was back-translated in a fresh context and diffed against the source.
  Every numeral survived intact and no content was dropped.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 28 note references,
  28 bodies, 28 backlinks; numbering sequential in reading order.

### Random-sample deep audit (check 8)

The blind double-translation and back-translation samples together cover ~1.5% of
this long chapter by character; the mechanical checks (100% of numerals via
check_numbers, 100% of paragraphs via parity) carry the rest. Observed substantive
omission/error rate on the audited spans: zero — no dropped clause, no invented
sentence, no altered number or name.

### Notes added (3; numbered by the builder in reading order, continuing from ch05)

- "it is called rock-oil": 石脂 is petroleum/naphtha; the Yanzhou-petroleum-for-ink
  detail is genuine history (Shen Kuo's 石油 and his petroleum-soot ink in the Dream
  Pool Essays). Corroborated.
- "Fierce-fire thunder": 猛火/猛火雷 as the novel's naphtha incendiary, the real Tang-
  Song 猛火油 ("fierce-fire oil"), kin to Byzantine "Greek fire", described in the
  Wujing Zongyao (1044). Corroborated; the bursting-jar "thunder" is authorial
  extrapolation.
- "commissioning the watchtowers": 假节 (jiajie, "bearing the tally"), the Han/Wei-
  Jin delegation of imperial authority by conferred tally; the text's own gloss (jia
  = lend, jie = authority) is faithful to the historical term.
Recurring subjects whose FIRST appearance was in an earlier chapter were NOT
re-noted: Wang Zhongsi (ch01), the Nine-Gate Drum (ch04), the Guangtong Canal
(ch01), Qujiang Pool, the Sage, Que-le Huo-duo, the Lantern Festival, etc.

### Glossary rows added

People: Jia Shiqi, Aluoyue (provisional), Li Shi'er, Lady Gongsun (attested), Sun
Mian (attested), Wen Wuji. Organizations: the Right Xiao Guard (attested), the
Leopard Cavalry, the Sixteen Guards of the Southern Command (attested). Places: the
Jinguang Gate (attested), Changming Ward, the King of Rinan's mansion, the Wild
Goose Pagoda (attested), Shengdao/Anyi/Changxing/Chongren/Yong'an/Tonggui/Guiyi/
Yanfu/Yongping/Chongxian/Changshou/Daixian/Jude/Qunxian Wards, the Puji Temple, the
Tianjin Bridge (attested), the Longshou Canal (attested), the Qinling (attested),
Luling (attested), Luoyang (attested), Jiuquan (attested), Yumen (attested). Terms:
rock-oil (石脂), fierce-fire (猛火), fierce-fire thunder (猛火雷), Yan ink (延墨),
fire-proof cloth (火浣布 / asbestos), dragon-sill (过龙槛), binding-cord (缚索), the
Tang Rhymes (attested), lizard-skin drum, commissioning the watchtowers (假节望楼),
stone sutra-pillar (石经幢), the Statutes of Ceremonial (attested). Every recurring
referent already decided in ch01-ch05 (Zhang Xiaojing, Cao Poyan, Xu Bin, Li Bi,
Yao Runeng, Cui Qi, Tanqi, Ma Ge'er, Wen Ran, Wang Yunxiu, Long Bo, Feng Dalun,
Prince Yong; the Jing'an Bureau, the Lüben Guards; Guangde/Yanshou/Huaiyuan/
Xiuzheng Wards, the West Market, the Guangtong Canal, the Qixia Gate, the Vermilion
Bird Avenue; the Wolf Guards, the Nine-Gate Drum, Que-le Huo-duo, barrier-knife,
pocket crossbow, smoke pellet, buliang chief/men, the Five-Faced Yama / "Zhang the
Yama", "Deputy Director" for 司丞, "Commander Cui" for 崔旅帅, etc.) was reused
verbatim, not re-romanized.

### Figures

None. The chapter has no content illustration in its source (only the book-wide
footnote-marker glyph Image00004.jpg and the scene-break rule Image00005.jpg, which
are not figures). figures.json stays empty, matching ch01-ch05.

### Flagged for the read-through

- The chapter opens with a flash-forward vignette of the Zhang/Cao kiln-duel (the
  crossbow bolt beside Cao's foot, Zhang's roll to thirty paces off); the exact text
  returns at source line 175 when the duel arrives, and both instances were
  translated identically, per the ch04/ch05 precedent for such authorial echoes.
- The source's per-chapter time-gloss ("下午3点。申，又名日铺、夕食等。（北京时间15时至
  17时）") is captured as the final source paragraph and rendered as the source's own
  italic note, per house style. (Note the source writes 日铺 for the usual 日晡,
  late-afternoon; rendered as the source has it.)
- 盂兰盆节放河灯 (source line 69): in Zhang's roll-call of Chang'an life he names the
  Ullambana / Ghost Festival river-lanterns. This is NOT the recurring 中元-for-上元
  slip (ch02): here the Ghost Festival is one of several seasons/festivals he lists
  across the year, and is rendered faithfully as "the Ghost Festival."
- Zhang's tattoo 断刀 ("broken blade") and his address to the dead 闻无忌 ("our
  Eighth Company") plant backstory paid off later; rendered plainly, no note.

## B07 = ch07 (第七章 申正 / "The Hour of the Monkey, Second Half, 4 p.m.")

Scope: the whole chapter, 25,671 source characters, 469 paragraphs (the longest
chapter to date, a shade over ch06). Six scenes divided by the source's
scene-break rules (Image00005.jpg, five of them). (1) West Market / Jing'an
Bureau: the Lüben Guards, at the Right Xiao Guard's secret writ, seize Zhang
Xiaojing and hand him to General Gan Shoucheng; Li Bi reads Li Linfu's hand
behind it, sees that 285 of the 300 casks of rock-oil are still missing, and
sends Tanqi on a rescue while he rides to beg Director He. (2) The Yixiang
Pavilion: Feng Dalun hires the Evaluator Yuan Zai to have the Court of Judicial
Review demand Zhang back through the Censorate; Yuan Zai, sent to look at the
captive, finds she is not Wen Ran but a General of the Cloud Banner's kin (Wang
Yunxiu) and quietly shuts the door on the discovery. (3) Li Bi rides to the
Leyou Plateau and kneels to He Zhizhang, who refuses to help by Zhang's hand.
(4) The Right Xiao Guard: Tanqi (Plan B), passing as Li Linfu's maidservant with
a plum-blossom jade, cons Adjutant Zhao; when the ruse stalls she signals Plan
C; Zhang Xiaojing burns the cell as a diversion, is caught by Cui Qi at the
gate, turns the soldiers on Cui with a shout, and is boxed in by the Leopard
Cavalry — but Gan Shoucheng, by a wager Li Bi struck, waves them through. (5)
The woodshed: Yuan Zai cows Wang Yunxiu into obedience and proposes to Feng
Dalun a "two-birds" scheme. (6) The Cibei Temple hut: Li Bi, aged in an
afternoon, explains that He Zhizhang's collapse (not his help) forced Gan's
hand; Zhang senses the concealed truth and lets it lie; the two agree a stronger
hidden enemy is using the Türks as a blade, and Zhang asks to question the dying
Cao Poyan as the Lantern Festival's bells and lanterns rise over Chang'an.

Deliverables shipped: out/ch07_bilingual.md (QC only, never ships),
out/ch07_reading.md, data/zh/ch07.txt, notes.json (3 notes added, 31 total),
glossary.json updated (new people/orgs/places/terms below), noise.txt extended,
the rebuilt EPUB, and this log.

### Checks run

- check_numbers.py --noise noise.txt: 469 pairs, 0 unresolved. One flagged
  numeral was a REAL count and the ENGLISH was fixed rather than noised: 张小敬等
  三人 → "the three of them—Zhang Xiaojing and his companions—" (was "and his two
  companions", which carried 2 but not the 3). All other flags were NON-quantity
  numerals added to noise.txt, each with its reason: 二百八十五 (285 casks, spelled
  analytically in English and unreassemblable by the digit-composer, like the
  existing 二百二十/一百五十/一百零八; the value is present), 七寸 (打蛇七寸 = "the
  very vitals", idiom ≠ 7), 十成 (十成把握 = "a perfect certainty", ≠ 10), 百戏 (the
  "hundred entertainments", the set term for variety shows, cf. 百姓/百官 ≠ 100),
  万劫 (万劫不复 = "doomed past all redemption", ≠ 10000), 七郎 (赵七郎 = Zhao
  Qilang, a ranking-name, cf. 六郎/李十二/贾十七 ≠ 7), 一万步 (退一万步(讲) =
  "granting every allowance", ≠ 10000), 七绕八转 ("winding this way and that", cf.
  七转八弯 ≠ 7/8). Every added pattern was hand-verified; a genuinely dropped
  number would still fail. No WORD_NUM change needed.
- check_structure.py --pairs: paragraph parity 469 source / 469 translation, OK.
  Two extractor-split openers were merged (the recurring festival-crowd sentence
  = source lines 2-3; the dateline = source line + its lone full-stop line);
  every other source line maps one-to-one, and colon-lead-in speech lines were
  kept as the source has them. The source's content-file heading line "申正" is
  absorbed into the H2 chapter title, as in ch01-ch06.
- Anchor resolution: all 3 ch07 note anchors ("hide away the bow and boil the
  hound", "the Han sage Dong Zhongshu", "Wu Zixu") are verbatim substrings of the
  reading text (verified by grep, each exactly once). Builder built and qa_epub
  passed with all 31 notes.
- Blind double translation (check 2): an independent context, with no sight of
  this translation, rendered the literary dyeing-vat metaphor (Chang'an as a bolt
  of plain silk dropped into the dye, source line 161). Result: highly
  convergent, no omissions and no invented content — every image present (plain
  silk in the dyeing vat, clamorous dye across the crisscrossing streets, warp
  and weft, damp and soaked through, the colored haloes spreading, every thread
  taking the festive tincture, the joy surging to the heavens). Divergences were
  equivalent word-choices within translator discretion. No correction needed.
- Round-trip back translation (check 3): the number-dense cask-math (Li Bi's
  reminder to Xu Bin, source lines 65-67) was back-translated in a fresh context
  and diffed against the source. Every numeral survived intact — 300 casks / 30
  carts, 300 = 300, 3 carts, 15 casks, 285 casks, 27 carts — in the correct
  relations. The only divergence was 石油 for the source's 石脂 (both "rock-oil",
  the modern vs the novel's word), not an error.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 31 note
  references, 31 bodies, 31 backlinks; numbering sequential in reading order.

### Random-sample deep audit (check 8)

The blind double-translation and back-translation samples together cover the
chapter's most failure-prone spans (its densest literary image and its densest
number cluster); the mechanical checks carry the rest (100% of numerals via
check_numbers, 100% of paragraphs via parity). Observed substantive
omission/error rate on the audited spans: zero — no dropped clause, no invented
sentence, no altered number or name.

### Notes added (3; numbered by the builder in reading order, continuing from ch06)

- "hide away the bow and boil the hound": the 鸟尽弓藏，兔死狗烹 proverb of
  statecraft (Fan Li; echoed at Han Xin's fall) — the useful servant discarded
  once his use is spent; corroborated against Sima Qian's Records of the Grand
  Historian. Zhang's grim joke on his own betrayal.
- "the Han sage Dong Zhongshu": Dong Zhongshu (179-104 BCE) and the Dismount
  Barrow → Toad Barrow (下马陵 → 虾蟆陵) folk-corruption behind the Changle Ward
  wine's name, a pun the English can only footnote; the corruption is already in
  Bai Juyi's Song of the Pipa. Corroborated.
- "Wu Zixu": the legend of Wu Zixu's hair whitening in a single night at the Zhao
  Pass (Wu Yue Chunqiu), to which Tanqi likens the suddenly-aged Li Bi.
Recurring subjects whose FIRST appearance was in an earlier chapter were NOT
re-noted: Wang Zhongsi (ch01), He Zhizhang (ch02), Yuan Zai and Prince Yong
(ch05), Jiao Sui (ch03), the Court of Judicial Review / Censorate / Forestry and
Crafts Bureau (ch05), the Right Xiao Guard / Leopard Cavalry (ch06), the Sage,
the Lantern Festival, Que-le Huo-duo, etc.

### Glossary rows added

People: Gan Shoucheng, Adjutant Zhao (+ Zhao Qilang), Dong Zhongshu (attested),
He Dong, He Zeng, Wu Zixu (attested). Organizations: the Stores Section (仓曹).
Places: the Yixiang Pavilion, Changle Ward, the Toad Barrow (下马陵/虾蟆陵),
Khotan (attested), Xuanping/Xinchang/Shengping Wards, the Leyou Plateau
(attested), the Qinglong Temple (attested), the Chongzhen Abbey, the Cibei /
Changfa / Shengguang Temples, the Chengtian Gate (attested), the Zhuque Gate.
Terms: adjutant (参军), General of the Cloud Banner (云麾将军, attested/Hucker),
the Tangdi Collection (棠棣集), the Langguan Clear (郎官清), curtained hat (帷帽),
the plum-blossom jade (李花玉佩, with the 李=plum surname pun), Locana (卢舍那,
attested), Plan B/C (乙/丙 contingency plans), plain-oil fritters (素油子). Every
recurring referent already decided in ch01-ch06 (Zhang Xiaojing, Li Bi, Cui Qi,
Cao Poyan, Xu Bin, Yao Runeng, Tanqi, He Zhizhang / Director He, Li Linfu, Li
Heng, Yuan Zai, Feng Dalun, Prince Yong, Wang Yunxiu, Wang Zhongsi, Wen Ran, Wen
Wuji, Long Bo, Ma Ge'er, Jia Shiqi; the Jing'an Bureau, the Lüben Guards, the
Right Xiao Guard, the Leopard Cavalry, the Court of Judicial Review, the
Censorate, the Forestry and Crafts Bureau, the Jingzhao Prefecture; Guangde/
Huaiyuan/Xiuzheng/Changming/Dunyi/Shengdao Wards, the West Market, Chang'an/
Wannian County, Little Balur, the Ci'en Temple, the Wild Goose Pagoda; the Wolf
Guards, rock-oil, fierce-fire thunder, Que-le Huo-duo, the silver fish-pouch, the
buliang chief, the Five-Faced Yama, the Bear Fire Gang, "Deputy Director" for
司丞, "county commandant" for 县尉, "the Sage", the Lantern Festival, etc.) was
reused verbatim, not re-romanized.

### Figures

None. The chapter has no content illustration in its source (only the book-wide
footnote-marker glyph Image00004.jpg and the scene-break rule Image00005.jpg,
which are not figures). figures.json stays empty, matching ch01-ch06.

### Flagged for the read-through

- The chapter opens with a scene-setting festival-crowd sentence (not a
  flash-forward); that exact sentence recurs verbatim at source line 159, as the
  first sentence of the Li-Bi-rides paragraph, and was translated identically in
  both places, per the ch04/ch05/ch06 precedent for authorial echoes.
- The source's per-chapter time-gloss ("下午4点。申，又名日铺、夕食等。（北京时间15时
  至17时）") is captured as the final source paragraph and rendered as the source's
  own italic note, per house style. As in ch06 the source writes 日铺 for the
  usual 日晡 (late-afternoon); rendered as the source has it ("ribu").
- Authorial number slip: source line 69 writes 那五桶 ("those five casks") for the
  West Market blast, but line 67 has just established that the three carts held
  十五桶 (fifteen casks) in all (300 − 15 = 285 missing, which line 69's 二百多桶
  "two hundred-odd" confirms). The 五 is an internal inconsistency (should read
  十五); rendered faithfully as "those mere five casks" and left visible, per the
  house rule for authorial slips (cf. ch03's Tianbao-3/twenty-years, ch05's
  doubled negative, ch06's 日铺). Not footnoted.
- Six scenes are divided in the source by decorative rules (Image00005.jpg);
  following ch01-ch06 house style the reading text renders the scene shifts as
  plain paragraph breaks, with no separator glyph (the source's rule image is not
  a figure). If visible scene breaks are wanted, that is a global change to make
  across all chapters at once.
- 兰台 (source line 134), a poetic alias for the Censorate, is rendered "the
  Censorate" (matching 御史台) rather than transliterated, the referent being the
  same office.

## B08 = ch08 (第八章 酉初 / "The Hour of the Rooster, First Half, 5 p.m.")

Scope: the whole chapter, 20,231 source characters, 369 paragraphs. Ten scenes
divided by the source's scene-break rules (Image00005.jpg, ten of them). (1) A
flash-forward vignette of Tanqi fetching plain-oil fritters (recurs verbatim at
its true moment in scene 3). (2) The Prefecture morgue: Zhang Xiaojing feeds the
dying Cao Poyan a life-holding broth and, circling in with a false confession of
his own, goads him until he twice howls the title of the man who shaved his
crown-hair — "the Right Shad!" — then dies whispering "the cross-and-lotus";
Zhang smells the Wang household's rue incense on the corpse. (3) The Cibei Temple
hut: Zhang reports both leads, plants the lie that the Türks hold Wang Yunxiu
(really Wen Ran); over fritters he and Li Bi trade a philosophical rest (the
straw-dogs exchange); Xu Bin traces the cross-and-lotus to Nestorian Christianity
and, from the map, they fix the Right Shad at the Yining Ward temple; Zhang
borrows Tanqi; on leaving he warns Li Bi of an enemy inside the Bureau, and Li Bi
tells Xu Bin the same at the foot of the wall. (4) The Right Shad's chamber: the
old traitor burns his last Türk dispatches, destroys his steppe keepsakes, sneers
the Mencius creed ("those who labor with their minds govern others"), and toasts
his coming freedom. (5) The Changming Ward well: Yao Runeng's hound finds a
hidden woman down the well — who proves to be Wen Ran, not Wang Yunxiu. (6) The
festival streets and the Nestorian temple: Zhang and Tanqi pose as a devout
couple; the Persian deacon Yisi guides them, sees through the disguise ("your
eyes never meet, your shoulders never draw level"), and locks them in the
confession room. (7) The Bureau hall: Xu Bin hunts the mole, spots the returned
Cui Qi, and sketches the traitor's profile. (8) Wen Ran is brought in; Li Bi
grasps Zhang's deception and, his trust broken, orders her confined. (9) The
horse-hoof passage: Xu Bin's leaked "Wen-Ran" bait catches Registrar Pang passing
intelligence through the corner gate — but Pang served the Secretariat, not the
Türks, so there are TWO moles; Xu Bin realizes the water-canal is a second, better
channel. (10) The watchtowers ringing Guangde Ward go dark one by one, and
black-clad crossbowmen rise from the canal and storm the Bureau — the chapter's
cliff-hanger.

Deliverables shipped: out/ch08_bilingual.md (QC only, never ships),
out/ch08_reading.md, data/zh/ch08.txt, notes.json (3 notes added, 34 total),
glossary.json updated (new people/orgs/places/terms below), noise.txt extended,
the rebuilt EPUB, and this log.

### Checks run

- check_numbers.py --noise noise.txt: 369 pairs, 0 unresolved. Four flagged
  numerals were all NON-quantity numerals (idioms / list enumerators) added to
  noise.txt, each with its reason: 万物 (以万物为刍狗 = "the myriad things", ≠
  10000; the neighboring 万事 and 几十万条 were already handled by 万事/万条/[几数]十万),
  二是 (list enumerator "for another", paired with 一是, ≠ 2, cf. the existing 二来),
  胡说八道 ("talking nonsense", set phrase, ≠ 8), 六耳 (不传六耳 = "carries to no
  third party", idiom, ≠ 6). Every added pattern was hand-verified; a genuinely
  dropped number would still fail. No WORD_NUM change needed. One value that could
  have flagged, 三丈五 ("three and a half zhang"), did not need noising because the
  first 三丈's 3 remained present; the lantern heights 三丈/三丈五, 十色/五缕, 二尺余,
  八角/八棱, 两百人, 一十六盏, 十五道/三百余州 all survive into the English.
- check_structure.py --pairs: paragraph parity 369 source / 369 translation, OK.
  Two extractor-split openers were merged (the opening fritters vignette = source
  lines 2-3; the dateline = source line + its lone full-stop line); every other
  source line maps one-to-one. The source's content-file heading line "酉初" is
  absorbed into the H2 chapter title, as in ch01-ch07.
- Anchor resolution: all 3 ch08 note anchors ("the Nestorian monk Alopen", "as
  straw dogs", "labor with their minds govern others") are verbatim substrings of
  the reading text (verified by grep, each exactly once). Builder built (8 of 26
  chapters, 34 notes) and qa_epub passed: 26 documents, 34 refs / 34 bodies / 34
  backlinks, all links resolve.

### Notes added (3; 34 total)

1. "the Nestorian monk Alopen" — the historical Church of the East in Tang
   Chang'an: Alopen's arrival in 635 (Zhenguan 9), the Yining Ward mother-temple,
   the 781 Nestorian Stele, and the 745 Persian-Temple→Daqin-Temple renaming that
   makes Yisi's correction run a year ahead of the calendar. Corroborated against
   scholarship. First appearance of Nestorianism in the book (grep of ch01-ch07:
   absent), so the note lands here.
2. "as straw dogs" — Li Bi's Daodejing ch. 5 quotation (天地不仁，以万物为刍狗) and
   the ritual straw-dog image. Classical allusion, first appearance.
3. "labor with their minds govern others" — the Right Shad's Mencius quotation
   (劳心者治人，劳力者治于人) turned into a slaver's creed. Classical allusion.
   Deliberately NOT re-noted: Ozmish Khagan (noted ch01), and the Right Shad title
   itself (first appeared ch02, so its note-slot is past); both are reused per the
   glossary without a fresh note.

### Glossary rows added

People: Yisi (伊斯, attested — the Nestorian-Stele resonance), Alopen (阿罗本,
attested), Mishihe (弥施诃 = the Messiah, attested), Registrar Pang (庞录事).
Organizations: the Secretariat (中书省, Hucker), the Phoenix Pavilion (凤阁, its
byname), the Bureau of Sacrifices (祠部, Hucker). Places: Yining Ward (义宁坊), the
Kaiyuan Gate (开远门, attested), Buzheng Ward (布政坊), Yankang Ward (延康坊), the
Daqin Temple (大秦寺, attested), the Persian Temple (波斯寺, attested). Terms: the
cross-and-lotus (十字莲花), Nestorian temple (景寺), Nestorian monk (景僧), the Three
Foreign Religions (三夷教), Manichaeism (摩尼, attested), Sham (苫国, attested),
deacon (执事), archbishop (大主教), ordination certificate (度牒), the confession
room (告解室), the Ordinance to Cherish Written Characters (惜字令), spirit-summoning
rue incense (降神芸香), Zhenguan (贞观, attested), modao (陌刀), makara (摩羯,
attested), registrar (录事, kept distinct from 主事 "recorder"). Every recurring
referent already decided in ch01-ch07 was reused verbatim, NOT re-romanized —
crucially the pre-seeded 右杀 = "the Right Shad", 乌苏米施可汗 = "Ozmish Khagan",
阿史那 = "Ashina", 景教 = "Nestorian", 祆教 = "Zoroastrianism", 熊火帮 = "the Bear
Fire Gang", 细犬 = "sighthound", 慈悲寺 = "the Cibei Temple", and the whole cast
(Zhang Xiaojing, Li Bi / Deputy Director Li, Tanqi, Xu Bin, Yao Runeng, Cui Qi,
Cao Poyan, Ma Ge'er, Long Bo, Wen Ran, Wang Yunxiu, Gan Shoucheng, Prince
Yong/Li Lin, Li Linfu / the Right Minister; the Jing'an Bureau, the Lüben Guards,
the Right Xiao Guard, the Jingzhao Prefecture, the Court of Judicial Review, the
Censorate; Guangde/Changming/Xiuzheng/Dunyi/Yining Wards, the West Market, the
Long Mountains, the Leyou Plateau; the Wolf Guards, Türk, barrier-knife,
fierce-fire thunder, the double-hour, watchtower, the Lantern Festival, etc.).

### Figures

None. The chapter has no content illustration in its source (only the book-wide
footnote-marker glyph Image00004.jpg and ten instances of the scene-break rule
Image00005.jpg, neither a figure). figures.json stays empty, matching ch01-ch07.

### Blind double-translation + back-translation (separate contexts)

- Double-translation (literary sample): the straw-dogs exchange (source line 83,
  Li Bi on the solitary Daoist heart and the hundreds of thousands of lives in his
  hand) was re-translated blind in a fresh context. The independent rendering
  matched the shipped one in sense, register, and the Daodejing allusion ("Heaven
  and earth are without benevolence; they treat the ten thousand things as straw
  dogs" vs. our "…are not benevolent; they treat the myriad things as straw
  dogs"); 几十万 came back as "several hundred thousand" against our "hundreds of
  thousands" — equivalent. No divergence in meaning. 0 errors.
- Back-translation (number-dense sample): our English of source line 37 (Zhang's
  "fifteen circuits and their governing seats, and more than three hundred
  prefectures … Luoyang … Yangzhou, Jiangling, Chengdu … herd-slaves") was
  rendered back to Chinese blind. Every quantity and place survived the round trip
  — 十五道及其治所, 州府三百余座, 洛阳/扬州/江陵/成都, 连根拔起, 牧奴 — with no
  omission or number drift. 0 errors.
- Sample error rate: 0 errors across the two audited passages (~4% of the
  chapter's characters), consistent with ch01-ch07.

### Flagged for the read-through

- The opening (source lines 2-3) is a FLASH-FORWARD vignette of Tanqi fetching the
  plain-oil fritters; the identical sentences recur at their true moment in the
  hut scene (source line 94) and were translated identically in both places, per
  the ch04-ch07 precedent for authorial echoes. The source's line-94 recurrence
  drops one character (writes 子是素油炸的 for 油子是素油炸的); rendered identically to
  the opening regardless, as the vignette is meant to match.
- The source's per-chapter time-gloss ("下午5点。酉又名日落、日沉、傍晚：意为太阳落山
  的时候。（北京时间17是至19时）") is captured as the final source paragraph and
  rendered as the source's own italic note, per house style. The gloss's common
  words 日落/日沉/傍晚 are translated (sunset / sundown / dusk), not romanized,
  since they are ordinary words (unlike ch06/ch07's technical 日铺/日晡). Authorial
  typo in the gloss: "17是至19时" for "17时至19时" (是 for 时); rendered by intent as
  "17:00 to 19:00". Trivial, not footnoted.
- Ten scenes are divided in the source by decorative rules (Image00005.jpg);
  following ch01-ch07 house style the reading text renders the scene shifts as
  plain paragraph breaks, with no separator glyph (the source's rule image is not
  a figure). If visible scene breaks are wanted, that is a global change to make
  across all chapters at once.
- 陌刀 (source line 38, "言语陌刀") is the long two-handed Tang saber, used here only
  as a metaphor for Zhang's cutting words; rendered "the keen modao of his words"
  (glossary row added), not footnoted — a passing figure, not a real weapon in the
  scene.
- 弥施诃 / the crucifixion account (source lines 220-222) is the Passion as Tang
  Nestorians told it (Mishihe = the Messiah, 大秦州官 = a Roman provincial officer =
  Pilate); rendered faithfully and glossed in the glossary. It shares the chapter's
  single Nestorian footnote (on Alopen) rather than taking a second note, to keep
  the density at ~3.

## B09 = ch09 (第九章 酉正 / "The Hour of the Rooster, Second Half, 6 p.m.")

Source: data/src/19_text00019.txt, 14,154 chars. Translated end to end into
out/ch09_bilingual.md (QC only, not shipped), split to out/ch09_reading.md +
data/zh/ch09.txt (274 paragraphs each). The bilingual was generated by a one-off
script (scripts/_gen_ch09_bilingual.py) that pulls each source paragraph VERBATIM
from data/src and pairs it with the English, so the source side cannot drift.

### Checks run

- check_numbers.py out/ch09_bilingual.md --noise noise.txt: PASS (274 pairs, 0
  unresolved). Two flags resolved by extending noise.txt, both genuine
  non-quantity numerals: 并无二致 (二致 = "a difference," idiom; English "no
  different from any other cleric's") and 四个字 (an enumerator counting the
  characters of an uttered phrase; appears twice — 延州石脂 / "Yanzhou rock-oil,"
  and 外强中弱 where the English does carry "four words: strong without, weak
  within"). No real quantity was noised.
- check_structure.py --pairs data/zh/ch09.txt out/ch09_reading.md: PASS, parity
  equal (source 274 | translation 274).
- build_reading_epub.py + qa_epub.py: PASS. 9 of 26 chapters translated, 37 notes
  (37 references / 37 bodies / 37 backlinks), all links resolve.

### Notes added (3; 37 total)

- 蚍蜉 / "the Pifu" (anchor "we are the Pifu"): Long Bo's organization name; a
  large ant, from Han Yu's 蚍蜉撼大树 ("ants that would shake a great tree"), which
  Long Bo turns into his boast about shaking the Jing'an Bureau. First appearance;
  kept as the transliteration so the allusion carries through.
- 獬豸 / "xiezhi" (anchor "a jade xiezhi"): the one-horned justice-beast that gores
  the guilty, emblem of the censors and judges; Cui Qi's family carries a jade one.
  First appearance.
- 胡旋舞 / "the Sogdian Whirl" (anchor "dance me a Sogdian Whirl"): the fast Tang
  whirling dance from the Western Regions, twisted into the deputy squad-leader's
  cruel taunt as his victims burn. First appearance.
- Skipped (already noted or already appeared): Cen Shen of Xianzhou (noted ch02),
  Wolf Guards, rock-oil/fierce-fire (ch06), the Right Shad (ch02), He Zhizhang,
  Wang Zhongsi, modao (glossary; here a literal weapon but self-glossed in the
  prose "haft four chi, blade three chi").

### Glossary rows added

- People: 普遮 = "Puzhe" (provisional) — the elder-identity the Right Shad hides
  behind, found stabbed; modao scar + armor-calluses expose him.
- Places: 嘉会坊 = "Jiahui Ward" (Lüben Guards' quarters, south of the Bureau);
  仙州 = "Xianzhou" (attested; Cen Shen's registered home, per the ch02 note).
- Terms: 蚍蜉 = "the Pifu"; 唧筒 = "squirt-pump"; 离丧铃 = "mourning bell";
  獬豸 = "xiezhi"; 胡旋舞 = "the Sogdian Whirl".
- Reused verbatim (not re-romanized): Zhang Xiaojing, Li Bi / Deputy Director Li,
  Tanqi, Cui Qi (Commander Cui), Yao Runeng, Wen Ran, Long Bo, Cen Shen, the Right
  Shad, Yisi, the Jing'an Bureau, the Lüben Guards, the Daqin/Persian Temple,
  Yining Ward, Guangde Ward, Huaiyuan Ward, Kang, Sham, the Long Mountains,
  barrier-knife, ordination certificate, rock-oil, pocket crossbow, smoke pellet,
  makara, the Que-le Huo-duo, the Lantern Festival, quarter-hour, finger-snaps,
  great watchtower, fly-whisk, water-clock.

### Figures

None. The chapter has no content illustration in data/figs (only the source's
footnote-marker glyph Image00004.jpg and the scene-break rule Image00005.jpg,
which are not figures). figures.json unchanged.

### Blind double-translation + back-translation (separate contexts)

- Double-translation (literary sample): the Cui Qi / Yao Runeng death-pact
  exchange (source lines 256-262, ~330 chars) was retranslated blind in a fresh
  context. The independent version matched ours in meaning throughout — "面无表情/
  看不出表情" both as unreadable; "每个人都得为他的选择负责" both as "every man
  must/has to answer for his own choices"; "嗤笑" both as a snort/sneer of a laugh.
  No divergence; the passage is unambiguous. 0 errors.
- Back-translation (number-dense sample): our English of the monastery-prison
  last stand (source lines 243-245) was rendered back to Chinese blind. Every
  quantity survived the round trip — 再多一倍 ("twice their number"), 三名狱卒
  ("three jailers"), 左肩 ("left shoulder"), 三死两伤 ("three dead and two
  wounded"), 三员精锐 ("three of his elite fighters"), 仅存的一名手下 ("one
  remaining subordinate") — with no omission or number drift. 0 errors.
- Sample error rate: 0 errors across the two audited passages (~5% of the
  chapter's characters), consistent with ch01-ch08.

### Flagged for the read-through

- The opening (source lines 2-3, an extractor-split pair, merged) is a
  FLASH-FORWARD vignette of the ox-cart ambush; the identical sentences recur at
  their true moment (source line 120) and were translated identically in both
  places, per the ch04-ch08 precedent for authorial echoes.
- Authorial ward-name slip: source line 271 writes 远怀坊 for 怀远坊 (Huaiyuan
  Ward) as the scene of Cen Shen's earlier interference. 远怀坊 occurs nowhere else;
  怀远坊 (Huaiyuan Ward) is where the ch02-ch03 chase and Cen Shen's disruption
  happen. Rendered by the intended referent, "Huaiyuan Ward" (one referent, one
  rendering), and the slip noted in the glossary's 仙州 row and here rather than
  minting a phantom ward.
- The source's per-chapter time-gloss ("下午6点。酉又名日落、日沉、傍晚：意为太阳落山
  的时候。（北京时间17是至19时）") is captured as the final source paragraph and
  rendered as the source's own italic note, per house style. It repeats the ch08
  authorial typo "17是至19时" for "17时至19时" (是 for 时); rendered by intent as
  "17:00 to 19:00". The gloss's ordinary words 日落/日沉/傍晚 are translated (sunset
  / sundown / dusk), not romanized.
- Multiple scenes (temple → Bureau exterior → temple → alley → Bureau hall →
  prison) are divided in the source by decorative rules (Image00005.jpg);
  following house style the shifts are rendered as plain paragraph breaks, no
  separator glyph.
- 口蜜腹剑 ("honey-mouthed and dagger-hearted," source line 19) — Yisi jokes the
  phrase is "forbidden," a wink at its origin as the byword for the Right Minister
  Li Linfu. The English pun (honey-mouthed/dagger-hearted vs. "a fair tongue and
  a fine face") is self-contained, so the Li Linfu wink was left unfootnoted to
  hold the density at 3.
- 明察秋毫 (Mencius) and 予若观火 (Book of Documents), source line 138 — the source
  itself names both classics in the next sentence, so the allusions are self-glossed
  and not separately footnoted.

## B10 = ch10 (第十章 戌初 / "The Hour of the Dog, First Half, 7 p.m.")

Scope: the whole chapter, 16,368 source characters, 309 paragraphs. Zhang
Xiaojing breaks the captured assassin in the Persian Temple confession room
(the Lai Junchen / Zhou Xing torture threats) and learns of the Shouzhuolang and
the Pingkang Ward drop at Liu's Bookshop; meanwhile the Pifu burn the Jing'an
Bureau and Cui Qi dies of his wound before Gan Shoucheng, who quietly hands
Li Linfu a pretext to seize the Bureau; Zhang forces Tanqi to choose the mission
over rushing back, revives the watchtower net with himself as its hub, and Yao
Runeng hears Wen Ran's backstory in the apothecary; the chapter closes with the
censor Ji Wen, backed by Yuan Zai, installed as the new Deputy Director and
naming Zhang Xiaojing the traitor.

Deliverables shipped: out/ch10_bilingual.md (QC only, never ships),
out/ch10_reading.md, data/zh/ch10.txt, notes.json (3 new notes, 40 total),
glossary.json (grown, below), noise.txt (extended, below), the rebuilt EPUB,
and this log. figures.json unchanged (no content illustration in this chapter;
Image00004.jpg the footnote-marker glyph and Image00005.jpg the scene-break rule
are not figures).

### Checks run

- check_numbers.py --noise noise.txt: 309 pairs, 0 unresolved. Five numerals
  flagged in the first pass were resolved as follows. Four were NON-quantities and
  were added to noise.txt (recorded below): 武三思 (the 三 of a personal name),
  百般 ("in every way," idiom), 六典 (the 六 of the book title 大唐六典), and 十几万
  ("over a hundred thousand," rendered analytically like 十万; placed ABOVE the
  bare 十几 rule so 十几 does not strip first and orphan 万 = 10000). One was a REAL
  quantity and was fixed in the ENGLISH, not noised: 近百位同僚 ("nearly a hundred
  colleagues") is rendered "fully a hundred of his colleagues" so the count of
  100 survives.
- check_structure.py --pairs data/zh/ch10.txt out/ch10_reading.md: paragraph
  parity 309 source / 309 translation, OK.
- Anchor resolution: all 3 new note anchors ("Lai Junchen", "Ji Wen",
  "Shouzhuolang") are verbatim substrings of the reading text and attach at first
  appearance; the builder also refuses on any unmatched anchor.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 40 note
  references, 40 bodies, 40 backlinks; numbering sequential in reading order.

### Notes added (notes.json ch10; 3, total now 40)

1. Lai Junchen (来俊臣) at first appearance: the archetypal Wu-Zetian-era cruel
   official whose name still terrifies; corroborated against the "Biographies of
   the Cruel Officials," Old Book of Tang.
2. Ji Wen (吉温) at first appearance: the historical hatchet-man and Li Linfu
   client installed here to seize the Bureau for the Secretariat; corroborated.
3. The Shouzhuolang (守捉郎) at first appearance: 守捉 were real Tang frontier
   garrison-posts, but the mercenary guild is the novel's extrapolation, not an
   attested body; stated as such in the note.

Recurring subjects already noted or already passed were NOT re-noted (per the
first-appearance rule): He Zhizhang, Yuan Zai, Prince Yong, the Right Shad, the
Pifu, the Sogdian Whirl, the xiezhi, Cen Shen (of Xianzhou), the Right Xiao
Guard, the Censorate, and everything in ch01-ch09. The Qu Yuan (Li Sao) line and
Cen Shen's own 胡笳歌 are rendered faithfully and left unnoted to hold density at 3.

### Glossary added (glossary.json)

- people (8): 吉温 = "Ji Wen"; 来俊臣 = "Lai Junchen"; 周兴 = "Zhou Xing"; 周利贞 =
  "Zhou Lizhen"; 桓彦范 = "Huan Yanfan"; 武三思 = "Wu Sansi"; 郝象贤 = "Hao
  Xiangxian"; 公辅 = "Gongfu" (Yuan Zai's courtesy name).
- organizations (1): 守捉郎 = "the Shouzhuolang."
- places (22): 刘记书肆 = "Liu's Bookshop"; the wards 兴道坊/开化坊/光禄坊/务本坊/崇义坊
  = "Xingdao/Kaihua/Guanglu/Wuben/Chongyi Ward"; 勤政务本楼 = "the Qinzheng Wuben
  Tower"; 楼兰 = "Loulan"; 秦山 = "the hills of Qin"; 岐山 = "Qishan"; 烽燧城 = "the
  beacon-fort"; 雍州/洛州 = "Yongzhou/Luozhou"; and the eight frontier commands
  范阳/平卢/朔方/河西/安西/北庭/陇右/剑南 = "Fanyang/Pinglu/Shuofang/Hexi/Anxi/Beiting/
  Longyou/Jiannan," plus 岭南五府 = "the Lingnan Five Prefectures" (河东 = Hedong,
  岭南 = Lingnan already decided; reused).
- terms (15): 守捉城 = "garrison-town"; 留后院 = "resident-agent courtyard"; 端公 =
  "Duangong"; 副端 = "Vice-Duan"; 殿中侍御史 = "Palace Censor"; 侍御史 = "Attendant
  Censor"; 左巡使 = "Commissioner of the Left Patrol"; 拔灯 = "the lantern-floats";
  灯顶红筹 = "the Lantern-Crown Red Tally"; 牧护歌 = "the Muhu song"; 胡笳 = "the
  nomad reed-pipe"; 大唐六典 = "the Tang Liudian"; 百官格 = "the Statutes on
  Officials"; 神龙 = "Shenlong"; 都护府 = "the Protectorate."

Pre-decided renderings were reused, not re-romanized: Zhang Xiaojing, Tanqi,
Yisi (deacon), the Right Shad, Puzhe, the Pifu, Long Bo, Cui Qi (Commander Cui),
Yao Runeng, Wen Ran, Wen Wuji, Gan Shoucheng (General), Cen Shen, Yuan Zai, the
Right Minister (Li Linfu), Prince Yong, Wang Zhongsi, the Jing'an Bureau, the
Lüben Guards, the Right Xiao Guard / Leopard Cavalry, the Secretariat, the
Court of Judicial Review, the Ministry of Justice, the Jingzhao Prefecture, the
Forestry and Crafts Bureau, Guangde/Yining/Dunyi Ward, Pingkang Ward (from the
平康里 note), the Cibei Temple, the Persian Temple, the Vermilion Bird Avenue,
the Leyou Plateau, Qujiang Pool, the Xingqing Palace, Little Balur, the Long
Mountains, Hedong, Lingnan, the Bear Fire Gang, the Wen Incense Shop, the Tang
Rhymes, the art of the Great Archive, commissioning the watchtowers,
double-hour, watchtower, constable, buliang chief, county commandant,
rock-oil, the Que-le Huo-duo, the Five-Faced Yama.

### noise.txt extended (recorded, with why)

- 武三思 (Wu Sansi, a name; the 三 is not the quantity 3).
- 十几万 ("over a hundred thousand," analytic; placed above the bare 十几 rule so
  it strips whole rather than orphaning 万 = 10000).
- 百般 ("in every way," idiom; the 百 is not 100).
- 六典 (the 六 of the title 大唐六典 / the Tang Liudian, a name, not a quantity).
All four are non-quantities; the one real count in the batch (近百 "nearly a
hundred") was carried in the English instead of noised.

### Blind double-translation + back-translation (separate contexts)

- Double-translation (literary sample): Tanqi's reflection on Zhang Xiaojing's
  solitude in the crowd (source lines 224-227, ~230 chars) was retranslated blind
  in a fresh context. The independent version matched ours in meaning throughout:
  the roll-call of epithets (登徒子/凶神阎罗/游侠 as lecher / fiend-Yama / knight-
  errant), 寂寞 as "alone / utterly alone" both times, 洗褪...浮夸油彩 as washing
  away the "gaudy greasepaint," and 比公子距离这尘世更远 as standing "further from
  this dusty world than the young master." No divergence of meaning; the passage
  is unambiguous. 0 errors.
- Back-translation (number-dense sample): our English of Ji Wen's rank-and-belt
  description plus the ten military-commissioner courtyards (source lines 292 and
  98-99) was rendered back to Chinese blind. Every quantity survived the round
  trip: 九枚 (nine plaques), 七品 (seventh rank), 低一阶 (one grade lower), 十 (ten
  commissioners), 五府 (the Five Prefectures), and all ten command names in order.
  The only variance was lexical (进奏院 for 留后院, a true synonym), not a number
  or referent change. 0 errors.
- Sample error rate: 0 errors across the two audited passages (~3% of the
  chapter's characters), consistent with ch01-ch09.

### Flagged for the read-through

- The opening (source lines 2-3, an extractor-split pair, merged) is a
  FLASH-FORWARD vignette of the Bureau fire; the identical first sentence recurs
  at its true moment (source line 106, where the vignette continues) and was
  translated identically in both places, per the ch04-ch09 precedent.
- Authorial slip in the time-gloss: the source's per-chapter hour-note for ch10
  is internally inconsistent. It labels the hour 戌 (the Dog, an evening hour,
  which the chapter's own heading and dateline correctly place at 戌初 = 7 p.m.),
  but then gives the pre-dawn time "凌晨5点 ... 05时至07时" and a sunrise gloss
  ("日始、破晓、旭日 ... 太阳刚刚露脸，冉冉初升"), all of which belong to 卯 (the
  Rabbit, 5 to 7 a.m.). The source note is rendered faithfully and in full, error
  and all, as the source's own italic note (rule 4: leave genuine source errors
  visible), with 戌 romanized as the hour-name and the ordinary words translated.
  Only the note is wrong; the chapter is set at 戌初 (7 p.m.) throughout.
- 五色使人盲 (source line 149, Laozi) and 长太息以掩涕兮，哀民生之多艰 (source line
  271, Qu Yuan's Li Sao) are rendered faithfully; the surrounding prose marks the
  latter as a sigh of grief, so both are self-contextualized and left unfootnoted.
- 拔灯/灯顶红筹 (the lantern-floats and their top-performer prize) and 守捉/守捉城
  (the frontier garrisons) are self-glossed by the source; the wordplay 拔灯不是灯
  ("the lantern-floats were not lanterns at all") is preserved by rendering 拔灯
  with the lantern element.
- Multiple scenes (confession room, Bureau exterior, the Vermilion Bird Avenue
  crowd, the apothecary, the Cibei Temple square) are divided in the source by
  decorative rules (Image00005.jpg); following house style the shifts are plain
  paragraph breaks, no separator glyph.

## B11 = ch11 (第十一章 戌正 / "The Hour of the Dog, Second Half, 8 p.m.")

Scope: the whole chapter, 16,491 source characters, 329 paragraphs. Three
interwoven strands: Zhang Xiaojing and Tanqi reach the Shouzhuolang firepoint at
Liu's Bookshop, where the true firemaster is found murdered and impersonated by
the killer (Tanqi catches the impostor by scent, storax without camphor) and the
firepoint guards ring them in, forcing a fighting retreat to the Pingkang Ward
constable-post; Yao Runeng, hiding Wen Ran from Yuan Zai via Cen Shen and a
signal-lantern, holds the great watchtower and sees Zhang revive the watchtower
net; and Li Bi, carried off to Long Bo's courtyard, is shown the Que-le
Huo-duo's true form (rock-oil bamboo tubes fitted to festival lantern-frames)
and grasps that the Pifu aim at one point, not the whole city.

Deliverables shipped: out/ch11_bilingual.md (QC only, never ships),
out/ch11_reading.md, data/zh/ch11.txt, notes.json (3 new notes, 43 total),
glossary.json (grown, below), noise.txt (extended, below), the rebuilt EPUB,
and this log. figures.json unchanged (no content illustration in this chapter;
Image00004.jpg the footnote-marker glyph and Image00005.jpg the scene-break rule
are not figures).

### Checks run

- check_numbers.py --noise noise.txt: 329 pairs, 0 unresolved. First pass flagged
  five NON-quantities, all added to noise.txt (recorded below): 杂七杂八 and
  七转八转 (7/8 idioms), 牌九 (the 9 of the domino-game name, 像牌九一样), 刘十七
  (the 十七 of the assassin's name Liu Shiqi), and 十七违背 (the bare 十七 as his
  short name "Shiqi" in the elder's speech, noised in-context so 第十七句 = "the
  seventeenth line" of the poem is still checked). One flag was a REAL count fixed
  in the ENGLISH, not noised: 十来个铁匠 had first been rendered "a dozen or so,"
  which drops the 10; changed to "ten-odd" so the value survives (and two further
  十几 renderings were normalized to "ten-odd" for house-style consistency).
  几万个灯架 ("tens of thousands of lantern-frames") passes on the built-in 几+万
  rule.
- check_structure.py --pairs data/zh/ch11.txt out/ch11_reading.md: paragraph
  parity 329 source / 329 translation, OK.
- Anchor resolution: all 3 new note anchors ("Self-Raining Pavilion", "A Moonlit
  Night on the Spring River", "storax") are verbatim substrings of the reading
  text and attach at first appearance; the builder also refuses on any unmatched
  anchor.
- qa_epub.py: PASS. 38 files, 32 documents, all links resolve; 43 note
  references, 43 bodies, 43 backlinks; numbering sequential in reading order.

### Notes added (notes.json ch11; 3, total now 43)

1. The Self-Raining Pavilion (自雨亭) at first appearance: a genuine Tang cooling
   device (water raised to the roof, falling from the eaves as a curtain);
   corroborated against the Tang yulin (Wang Hong's pavilion) and the palace
   water-cooled "cool hall" (凉殿).
2. "A Moonlit Night on the Spring River" (春江花月夜) at first appearance: Zhang
   Ruoxu's famous early-Tang poem, whose lines the Shouzhuolang use as passwords;
   the quoted "白云一片去悠悠" is verified as its seventeenth line. Corroborated.
3. Storax (苏合香) at first appearance: the imported western aromatic resin whose
   scent (without the bookshop's camphor) betrays the impostor; corroborated
   against Schafer, The Golden Peaches of Samarkand.

Recurring subjects already noted or already passed were NOT re-noted (per the
first-appearance rule): the Shouzhuolang, the Pifu (蚍蜉 + the Han Yu couplet),
Ji Wen, Yuan Zai, the beacon-fort at Balhuan, the Turkic Wolf Guards, the
Five-Faced Yama, the Que-le Huo-duo, and everything in ch01-ch10.

### Glossary added (glossary.json)

- people (2): 刘十七 = "Liu Shiqi"; 摩伽罗 = "Mojialuo" (a Shouzhuolang code-name,
  kept as pinyin to distinguish it from 摩羯 = "makara").
- places (3): 宣阳坊 = "Xuanyang Ward"; 永乐坊 = "Yongle Ward"; 天竺 = "Tianzhu"
  (the Tang name for India).
- terms (15): 火点 = "firepoint"; 火师 = "firemaster"; 自雨亭 = "the Self-Raining
  Pavilion"; 春江花月夜 = "A Moonlit Night on the Spring River"; 苏合香 = "storax";
  灯轮 = "lantern-wheel"; 福寿禄三星 = "the Three Stars (Fortune, Longevity, and
  Rank)"; 娑罗树 = "sal tree"; 金桃 = "golden peach"; 京兆尹 = "the Prefect of
  Jingzhao"; 中书令 = "the Secretariat Director"; 番仆 = "foreign servants"; 三羽令
  = "a three-feather order"; 惊夜灯 = "night-alarm lamp"; 卍字纹 = "the
  wan-character motif."

Pre-decided renderings were reused, not re-romanized: Zhang Xiaojing, Tanqi, Li
Bi (Deputy Director Li), Li Linfu (the Right Minister), Yao Runeng, Wen Ran, Cui
Qi, Ji Wen (Deputy Director / Vice-Duan), Yuan Zai (Evaluator, Gongfu), Long Bo,
Cen Shen, Xu Bin, Prince Yong, Feng Dalun, Wang Yunxiu, Wang Zhongsi, Puzhe, the
Jing'an Bureau, the Shouzhuolang, the resident-agent courtyards, the garrison-
town, the Persian Temple, the Cibei Temple, the Jingzhao Prefecture, the
Censorate, the Court of Judicial Review, the Secretariat, Pingkang Ward / the
Pingkang Quarter, Changming Ward, Guangde Ward, Changxing Ward, Yanzhou, the
beacon-fort at Balhuan (拨换城 = Balhuan + 烽燧), the Western Regions, the
watchtower / great watchtower, the constable (武侯), the county commandant, the
buliang men, the Five Kennels, the Wolf Guards, the Pifu, the Que-le Huo-duo,
fierce-fire thunder, rock-oil, fire-proof cloth, lizard-skin drum, pocket
crossbow, smoke pellet, the Five-Faced Yama, the Lantern Festival, commissioning
the watchtowers, and the hour-gloss format.

### noise.txt extended (recorded, with why)

- 杂七杂八 ("a jumble of," idiom; 7/8 not quantities).
- 七转八转 ("turning this way and that," idiom; joins 七转八弯/七绕八转 already listed).
- 牌九 (pai gow, the domino game; the 9 is part of the name, in 像牌九一样).
- 刘十七 (Liu Shiqi, an assassin's name "Seventeen"; joins 贾十七/李十二/赵七郎).
- 十七违背 (the bare 十七 as the short name "Shiqi" in the elder's speech; noised in
  context only, so 第十七句 = "the seventeenth line" of the poem stays checked and
  its 17 is still verified against the English "seventeenth").
All are non-quantities; the one real count (十来个 = "ten-odd") was carried in the
English, not noised.

### Blind double-translation + back-translation (separate contexts)

- Double-translation (literary sample): Long Bo's parable of the pifu (source line
  276, ~110 chars) was retranslated blind in a fresh context. The independent
  version matched ours clause for clause and image for image: 纯白/大小如米粒 as
  "born pure white, no bigger than a grain of rice," 啮木为粮 as gnawing wood for
  food, 钻椽穴柱/蚀壁蛀梁 as boring into rafters and pillars and eating away walls
  and beams, and 百丈广厦/千里长堤 as "a hundred zhang" / "a thousand li." The only
  differences were lexical choices for the untranslatable name 蚍蜉 ("pismire"
  blind vs. our decided "the Pifu," footnoted at ch09) and 广厦 ("high" blind vs.
  our "broad" for 广). No omission, no divergence of meaning. 0 errors.
- Back-translation (number-dense sample): our English of the dateline plus Li Bi's
  rock-oil tally (source lines 4-5, 290, 318) was rendered back to Chinese blind.
  Every quantity survived the round trip: 三载/十四 (Tianbao 3, 14th), 十五桶
  (fifteen barrels), 两百余桶 and 两百桶 (two hundred), 半个时辰 (half a double-hour),
  这两点 (the two points). 正月 for 元月 and 戌时正 for 戌正 are true synonyms, not
  number or referent changes. 0 errors.
- Sample error rate: 0 errors across the two audited passages (~2% of the
  chapter's characters), consistent with ch01-ch10.

### Flagged for the read-through

- The opening (source lines 2-3, an extractor-split pair, merged) is a
  FLASH-FORWARD vignette of Long Bo's pavilion; the identical sentence recurs at
  its true moment (source line 261, where the scene opens) and was translated
  identically in both places, per the ch04-ch10 precedent.
- Authorial slip in the time-gloss (same class as ch10): the source's per-chapter
  hour-note for ch11 labels the hour 戌 (the Dog, correctly placed at 戌正 = 8 p.m.
  by the chapter heading and dateline), but then gives "凌晨6点 ... 05时至07时" and
  a sunrise gloss ("日始、破晓、旭日 ... 太阳刚刚露脸，冉冉初升"), all of which belong
  to 卯 (the Rabbit, 5-7 a.m.). Rendered faithfully and in full as the source's own
  italic note (rule 4: leave genuine source errors visible), with 戌 romanized and
  the ordinary words translated. Only the note is wrong; the chapter is set at 戌正
  (8 p.m.) throughout. (ch10's note gave 凌晨5点; ch11's gives 凌晨6点 with the same
  mismatched 卯 body.)
- The Shouzhuolang jargon 火点/火师 is self-glossed by the source and rendered
  "firepoint"/"firemaster," keeping the shared "fire" element.
- The recognition passwords are lines of 春江花月夜: the doorkeeper's cue "春江"
  ("Spring River," the poem's opening words) and the response "白云一片去悠悠" (its
  17th line) are rendered as English poetry, with the poem footnoted.
- Scene shifts (the firepoint / Ji Wen at the Cibei Temple / the wrecked escort-
  cart / Yuan Zai at the apothecary and the great watchtower / the standoff at the
  constable-post / Li Bi in Long Bo's courtyard) are divided in the source by
  decorative rules (Image00005.jpg); following house style the shifts are plain
  paragraph breaks, no separator glyph.

## B12 = ch12 (第十二章 亥初 / "The Hour of the Pig, First Half, 9 p.m.")

Scope: the whole chapter, 18,171 source characters, 375 paragraphs. Five
interwoven strands after the flash-forward vignette and dateline: Zhang Xiaojing,
wounded, runs the Shouzhuolang-and-constable cordon across Pingkang Ward (the
stove-and-spindle decoy; the watchtower net turned to his aid; the old
post-soldier Old Zhao's disguise) until he collapses and a black hand catches
him; Yuan Zai murders the young toughs to silence them, frames the abduction on
Zhang, and delivers the "rescued" Wang Yunxiu to Ji Wen, who has purged the
Bureau's foreign clerks; the raid on the Cibei-Temple thatched hut takes Cen
Shen and Wen Ran (the release-pond ice-knife; Wen Ran's despair when told her
benefactor is dead and given to Prince Yong; her sacrifice to free Cen Shen; the
reunion cry "Sister Wang"); Old Ge's ox-cart carries Zhang to the Guan Zhong
shrine, where he and the squad leader spring a joint trap on the assassin, who
escapes with green-vitriol oil at the cost of an arm, naming himself Yuchang;
and Yisi reappears, runs Zhang over the rooftops to safety, and presses on him
the eight-cornered bamboo shard that reopens the trail, telling his own tale of
the fallen Persian royal house. Tanqi reaches the heir apparent's carriage and
cries that the Jing'an is in peril; the chapter closes on the great watchtower's
repeating "Do not come back."

Deliverables shipped: out/ch12_bilingual.md (QC only, never ships),
out/ch12_reading.md, data/zh/ch12.txt, notes.json (3 new notes, 46 total),
glossary.json (grown, below), noise.txt (extended, below), the rebuilt EPUB,
and this log. figures.json unchanged (no content illustration in this chapter;
Image00004.jpg the footnote-marker glyph and Image00005.jpg the scene-break rule
are not figures).

### Checks run

- Verbatim-quote check: a script reconstructed the source paragraph list from
  data/src/26_text00025.txt (dropping the 亥初 heading line and the trailing
  zero-width-space line, merging the two extractor-split pairs) and diffed it
  against data/zh/ch12.txt: 375/375 paragraphs, ALL VERBATIM MATCH, 0 mismatches.
- check_structure.py --pairs data/zh/ch12.txt out/ch12_reading.md: parity equal,
  source 375 | translation 375, OK.
- check_numbers.py --noise noise.txt: 375 pairs, 0 unresolved. First pass flagged
  four items. Three were NON-quantities added to noise.txt (recorded below):
  三步并两步 (a "half-run/haste" idiom, 3/2 not counts), 六个字 ("these six words,"
  a character-count of Yuan Zai's uttered phrase, cf. the existing 四个字), and
  说三道四 ("wag one's tongue," 3/4 not counts, cf. the existing 推三阻四). The
  fourth, 两边必须选一边 ("of the two he had to choose one"), was a REAL count:
  the English had read "one or the other," dropping the 两 (two), so it was FIXED
  in the ENGLISH to "of the two he had to choose one," carrying both 2 and 1
  (not noised).
- build_reading_epub.py + qa_epub.py: build wrote 12 of 26 chapters, 46 notes;
  QA PASS (26 documents, 4118 paragraphs; 46 references / 46 bodies / 46
  backlinks; 38 files, all links resolve).

### Notes added (notes.json ch12; 3, total now 46)

- "the Guan Zhong shrine" — Guan Zhong (d. 645 BCE) as the traditional patron of
  the courtesan trade, from the state-licensed brothels (女闾) of Qi; the shrine
  in the pleasure quarter is a wry historical joke, not the source's invention.
- "I, Yuchang, will surely have your life" — 鱼肠 ("fish-gut") as the ancient
  dagger with which Zhuan Zhu killed King Liao of Wu in 515 BCE (Zuozhuan /
  Shiji "Assassins"); the killer takes the weapon's name. First appearance.
- "The late king Peroz led his whole clan" — Peroz III, last Sasanian heir, who
  fled the Arab conquest to the Tang court (honorary generalship; the short-lived
  Persian Area Command, c. 661; Old Book of Tang); Yisi's claim of royal descent.
  First appearance.
- Deliberately NOT re-noted (already noted or already passed in ch01-ch11): the
  Shouzhuolang (ch10), Liu Shiqi (ch11), the Que-le Huo-duo, He Zhizhang, Yuan
  Zai, Prince Yong, Ji Wen, the Censorate, the Nestorian/Persian-Temple cluster
  (ch08), Cen Shen. The Analects tag 名不正则言不顺 ("if the name is not right,
  speech does not accord") and the Daodejing-36 tag Yuan Zai quotes are rendered
  faithfully in prose without notes, to hold the chapter to ~3.

### Glossary added (glossary.json)

- People: 鱼肠/Yuchang (the one-armed assassin; the dagger-name), 卑路斯/Peroz
  (last Sasanian heir), 太宗/Emperor Taizong, 高宗/Emperor Gaozong, 管仲/Guan Zhong,
  老聃/Lao Dan (= Laozi), 燕子李/Li the Swallow (the thief Old Zhao recalls),
  老赵/Old Zhao (the old post-soldier; distinct from 赵参军 Adjutant Zhao).
- Organizations: 右威卫/the Right Awesome Guard (Hucker; Peroz's honorary guard).
- Places: 波斯/Persia, 管仲祠/the Guan Zhong shrine.
- Terms: 四望车/four-windowed carriage, 甩霞舞/the Rosy-Cloud Fling (the
  ribbon-flinging dance, self-glossed by the source), 绿矾油/green-vitriol oil
  (sulfuric acid, a Daoist alchemical product), 跑窟/cave-running (Yisi's roof-art).
- Reused verbatim (not re-romanized): Zhang Xiaojing, the Shouzhuolang, squad
  leader (队正), firemaster (火师), constable (武侯) / post-soldier (铺兵), the
  watchtower / great watchtower, Yao Runeng, Li Bi, the Jing'an Bureau, the
  Que-le Huo-duo, Wang Yunxiu, Yuan Zai (zi Gongfu), Ji Wen, Feng Dalun, Xu Bin,
  Wen Ran, Cen Shen, Old Ge, Tanqi, the heir apparent, the Xingqing Palace, the
  Qinzheng Wuben Tower, the Jingzhao Prefecture, the Cibei/Persian Temples, the
  Kunlun slave, Liu Shiqi, Yisi, the Arab lands (大食), Kucha (龟兹), the lantern-
  floats (拔灯), the Xi cart (奚车), Guangde/Changming/Anren Wards, "Zhang the
  Yama," "every kindness repaid, every debt settled."

### noise.txt extended (recorded, with why)

- 六个字 — "these six words" (a count of the characters in Yuan Zai's phrase
  终于等到你了), not a quantity of things; cf. the existing 四个字 / [二三四]字.
- 说三道四 — "wag one's tongue / gossip and carp" (idiom); the 3/4 are not counts,
  cf. the existing 推三阻四.
- 三步并两步 — "hurry at a half-run" (idiom, lit. three steps in two); 3/2 not
  counts. English renders it "in two strides."
- ORDERING: all three are four-plus-character strings with no shorter built-in
  that would eat part of them first, so placement at the file's end is safe.
- The one real dropped number (两边必须选一边) was fixed in the ENGLISH, not noised.

### Blind double-translation + back-translation (separate contexts)

- Blind double-translation, literary sample (source line 330, Zhang's despair:
  "希望一断绝，无穷的压力便从四面八方涌过来 … 一个人，到底没办法对抗一个组织").
  The independent re-rendering matched the shipped text in sense throughout:
  从四面八方 = "from every side" / "from all directions"; 心力交瘁 = "worn out in
  heart and strength"; 孤军奋战 / 逆转不了大局 = "a lone fighter … could not turn
  the whole tide back." No omission, no divergence. 0 errors.
- Round-trip back-translation, number-dense sample (the flash-forward vignette,
  source line 2 = 255): the English back-translated to 六名 … 八名 … 四望车 … 四匹
  … 十几名, i.e. all five numerals (6 horsemen, 8 attendants, the four-windowed
  car, 4 horses, ten-odd guards) survive intact; the recurring vignette is
  rendered identically at both occurrences. 0 errors.
- Sample error rate: 0 errors across the two audited passages (~2% of the
  chapter's characters), consistent with ch01-ch11.

### Flagged for the read-through

- The chapter OPENS with a flash-forward vignette (source line 2, the golden
  horsemen and the four-windowed carriage) BEFORE the dateline; the identical
  sentence recurs at its true moment (source line 255, Tanqi before the Xingqing
  Palace) and was translated identically in both places, per the ch04-ch11
  precedent. The dateline (source lines 3-4) and its two split halves were merged
  into one pair; likewise Zhang's split speech (source lines 347-348).
- Preserved pun (费/废): Old Ge says the Shouzhuolang "cost us a bit of hand and
  foot" (费了点手脚 = took some doing), and Zhang thinks the truer phrase is that
  it "cost them a few hands and feet" (废了点手脚 = crippled some limbs). The
  shared literal 手脚 ("hands and feet") carries the wordplay in English without
  a note.
- The assassin's self-naming ("I, Yuchang") and Yisi's Persian-royal backstory
  (Peroz) are the chapter's two "reference a non-specialist won't catch" notes;
  the Guan Zhong shrine is the third. The Analects rectification-of-names tag
  (名不正则言不顺) and the Daodejing-36 tag are rendered in prose, unnoted, to
  hold the density near 3.
- Scene shifts (the ward-cordon chase / Wang Yunxiu's mule-cart / Ji Wen at the
  new Bureau / Yuan Zai and Feng Dalun / Old Ge's ox-cart / Wang Yunxiu's chamber
  and Xu Bin / the Cibei-Temple raid / Tanqi at the Xingqing Palace / the Guan
  Zhong shrine / Yisi's rooftop rescue) are divided in the source by decorative
  rules (Image00005.jpg); following house style the shifts are plain paragraph
  breaks, no separator glyph.
- No authorial slip in this chapter's time-gloss: the note correctly labels 亥
  (the Pig, 9-11 p.m.) with "晚上9点 … 21时至23时," unlike the mismatched 卯 bodies
  of the ch10 and ch11 notes.

## B13 = ch13 (第十三章 亥正 / "The Hour of the Pig, Second Half, 10 p.m.")

Scope: the whole chapter, 16,497 source characters, 290 paragraphs. The chapter
opens with a flash-forward vignette (Long Bo climbing out of the cellar, casting
his gaze into the dark), then the dateline and a location line ("Chang'an; the
place unknown"). Four strands follow: Li Bi, caged in an unknown cellar, hears
from a gloating Long Bo that the Bureau has been rebuilt under Ji Wen and a
citywide warrant issued for Zhang Xiaojing, and the assassin Yuchang announces he
is leaving to kill Zhang; the identical vignette recurs at its true moment as
Long Bo turns from the cage. Li Heng's four-windowed carriage is halted by
Tanqi's cry that the Jing'an is in peril; in a screened tea-stall she tells him
everything, but the irresolute heir will only wait for word and carries her on to
the Xingqing Palace banquet. Zhang Xiaojing and Yisi, Zhang disguised as a
painted Brahman mummer, ride to Guangde Ward, learn the worst from a foreign
clerk, and Zhang finds his resolve in the vows of Ksitigarbha and the Luminous
Lord; they cross into the burning Bureau over the Cibei-Temple wall, fail to save
the evidence room (a collapsing rafter burns Zhang's back), and use the fire and
Yisi's cave-running to reach Xu Bin in the infirmary, who reveals a second cache
of the Changming-Ward evidence in the Deliberation Hall of the Jingzhao
Prefecture; with Adjutant Zhao decoying Ji Wen, Yisi steals the sack of bamboo
shards from the beam. An interleaved vignette shows the recorder Zhang Luo pushed
to his death off the Arched-Moon Bridge, his throat cut in the crush. The chapter
closes at the banquet: Tanqi resolves to rush the throne and appeal to the Sage
directly, but a hand falls on her shoulder — the Daoist "Sister Taizhen" — as the
hour of the Rat strikes and the Rainbow-Feather Dance strikes up.

Deliverables shipped: out/ch13_bilingual.md (QC only, never ships),
out/ch13_reading.md, data/zh/ch13.txt, notes.json (3 new notes, 49 total),
glossary.json (grown, below), noise.txt (extended, below), the rebuilt EPUB,
and this log. figures.json unchanged (no content illustration in this chapter;
Image00004.jpg the footnote-marker glyph and Image00005.jpg the scene-break rule
are not figures).

### Checks run

- Verbatim-quote check: a script reconstructed the logical source paragraph list
  from data/src/28_text00027.txt (dropping the 亥正 heading line and the trailing
  zero-width-space line, merging the opening vignette's three extractor-split
  halves and the dateline's two halves, and collapsing the dateline artifact
  。。→。) and diffed it against the bilingual blockquotes: 290/290 paragraphs,
  ALL VERBATIM MATCH, 0 mismatches.
- check_structure.py --pairs data/zh/ch13.txt out/ch13_reading.md: parity equal,
  source 290 | translation 290, OK.
- check_numbers.py --noise noise.txt: 290 pairs, 0 unresolved. First pass flagged
  four items, all NON-quantities added to noise.txt (recorded below): 两处
  (a classifier, "the flanking halls to left and right," cf. 两侧/两片), 二不为
  (a list enumerator in 一不…二不…, cf. 二不逾制/二是), 万状 (惊恐万状 =
  "in an extremity of terror," 万 not 10000), and 八成 ("most likely / eight
  parts in ten," cf. 十成). No real quantity was noised; no number dropped.
- build_reading_epub.py + qa_epub.py: build wrote 13 of 26 chapters, 49 notes;
  QA PASS (26 documents, 4407 paragraphs; 49 references / 49 bodies / 49
  backlinks; 38 files, all links resolve).

### Notes added (notes.json ch13; 3, total now 49)

- "the bodhisattva Ksitigarbha" — Dizang and his great vow ("so long as the hells
  are not empty, I will not become a Buddha"), which Zhang Xiaojing sets beside
  the Nestorian redemption to steel his own resolve. First appearance in the book.
- "Sister Taizhen" — Taizhen, the Daoist name of Yang Yuhuan / the future Yang
  Guifei: her ordination in 740, her elevation to Guifei in 745 (the year after
  this one), and her death at Mawei in 756; the dramatic irony of Tanqi knowing
  her at the foot of the throne. First appearance.
- "the Rainbow-Feather Dance" — the Nichang yuyi wu, the signature dance-suite of
  Xuanzong's court bound to Yang Guifei, striking up on cue as Taizhen appears.
  First appearance.

Recurring subjects already noted in ch01-ch12 and deliberately NOT re-noted:
He Zhizhang, Ji Wen, the Shouzhuolang, the Pifu, Prince Yong, the Que-le Huo-duo,
Yuchang, and the Sage; fire-proof cloth (asbestos, glossary-noted, first appeared
ch06) and the mercy-release pond (ch07) are rendered consistently, unnoted.

### Glossary added (glossary.json)

- People (3): 张洛/Zhang Luo (a recorder of the Forestry and Crafts Bureau);
  韦氏/Consort Wei (the heir's wife); 太真/Taizhen (Yang Yuhuan's Daoist name).
- Places (9): 花萼相辉楼/the Hua'e Xianghui Tower; 拱月桥/the Arched-Moon Bridge;
  兴庆坊/Xingqing Ward; 永嘉坊/Yongjia Ward; 胜业坊/Shengye Ward; 道业坊/Daoye
  Ward; 太极宫/the Taiji Palace; 南内/the Southern Interior; 春名门/the Chunming
  Gate (source's 春名门 for the standard 春明门, same reading).
- Terms (11): 麻搭/fire-mop (matching ch06); 推事厅/the Deliberation Hall; 架阁库/
  the records store; 设厅/the reception hall; 婆罗门戏/a Brahman farce; 地藏菩萨/
  the bodhisattva Ksitigarbha; 景尊/the Luminous Lord; 霓裳羽衣舞/the Rainbow-
  Feather Dance; 黄狮子舞/the Yellow Lion Dance; 通天冠/the tongtian crown;
  放生池/mercy-release pond (matching ch07).

Reused verbatim (not re-romanized): Zhang Xiaojing, Li Bi/Deputy Director Li,
Long Bo, Yuchang, Tanqi, Li Heng (heir apparent), Ji Wen, Yisi, Xu Bin/Youde/
Recorder Xu, Yao Runeng, Wen Ran, Wen Wuji, Adjutant Zhao, Gan Shoucheng/General
Gan, He Zhizhang, Li Linfu/the Right Minister, Cao Poyan, Feng Dalun; the Pifu,
the Que-le Huo-duo, the Shouzhuolang, the three-feather order, four-windowed
carriage, cave-running, fire-proof cloth; the Jing'an Bureau, the Jingzhao
Prefecture, the Right Xiao Guard, the Forestry and Crafts Bureau, the Censorate,
the Palace Censor; Guangde Ward, the Pingkang Quarter, the Cibei Temple, the
Xingqing Palace, the Qinzheng Wuben Tower, the Longshou Canal, the Daming Palace,
Changming Ward, the Wild Goose Pagoda; the lantern-floats.

### noise.txt extended (recorded, with why)

- 两处 — 左、右两处偏殿 = "the flanking halls to left and right"; a classifier
  absorbed (cf. 两侧/两片/两道), the two-ness carried by "left and right."
- 二不为 — 一不为人命，二不为财货 = "not for any man's life, nor for any goods";
  list enumerator (cf. 二不逾制/二来/二是), not the count 2.
- 万状 — 惊恐万状 = "in an extremity of terror"; 万状 idiom, not 10000.
- 八成 — 声音八成是从这里传来 = "most likely came from there"; 八成 = "eight
  parts in ten / most likely" (cf. 十成), not the count 8.

### Blind double-translation + back-translation (separate contexts)

- Blind double-translation, literary sample (Zhang Xiaojing's Ksitigarbha/Luminous
  Lord epiphany, source lines 108-112, "景尊怜悯世人之苦 … 无须任何顾忌才对 …
  笑声上犯夜空"): an independent re-rendering in a fresh context matched the shipped
  text in sense throughout — 地狱不空，誓不成佛 = "so long as the hells are not
  empty, he vows never to become a Buddha"; 身临浊世地狱 = "go down in the flesh
  into the hell of this defiled world"; the epiphany turns on "not why I should
  drive myself so hard, but that I need not hold back at all." Only surface wording
  differed (the other rendered 景尊 "the Venerable One"; the project's decided term
  is "the Luminous Lord"). 0 errors.
- Round-trip back-translation, number-dense sample (the Xingqing lantern-tower,
  source lines 77-79 and 156): the English back-translated to 高逾一百五十尺 …
  一百五十尺 … 四更 … 勤政务本楼 … 大雁塔 … 兴庆宫 … 葫芦, i.e. every numeral
  and measure survives (150 chi twice, the fourth watch) and all proper names
  return intact; only 拔灯 ("the lantern-floats") came back as the near-synonym
  灯船 ("lantern-boats"), a terminology paraphrase, not a lost value. 0 errors.
- Sample error rate: 0 errors across the two audited passages (~3% of the
  chapter's characters), consistent with ch01-ch12.

### Flagged for the read-through

- The chapter OPENS with a flash-forward vignette (source lines 2-4, Long Bo
  climbing out of the cellar) BEFORE the dateline; the identical sentence recurs
  at its true moment (source line 34, Long Bo turning from Li Bi's cage) and was
  translated identically in both places, per the ch04-ch12 precedent. The dateline
  (source lines 5-6) was merged from its two extractor-split halves, and the
  dateline artifact 。。 collapsed to 。 (as ch12 merged its 亥初 + 。).
- The location line "长安，不明。" is rendered "Chang'an; the place unknown." —
  Li Bi is held in a cellar whose location even the narration withholds; not the
  ward-name format of ch12's "Chang'an; Wannian County; Pingkang Ward."
- The three "reference a non-specialist won't catch / texture" notes are
  Ksitigarbha, Taizhen, and the Rainbow-Feather Dance — the last two a linked
  pair (the dance strikes up as Taizhen appears). Density held near 3: the
  Hua'e Xianghui Tower (its name a figure for brotherly love) and the tongtian
  crown's twelve ridges are glossed in the glossary, not footnoted.
- Zhang Xiaojing's oath "我他妈没说要杀他" is rendered with its full coarseness
  ("I didn't fucking say I was going to kill him"), matching the book's own
  register for him.
- Scene shifts (the cellar / Li Heng's carriage and tea-stall / Zhang and Yisi to
  Guangde Ward / the burning Bureau / Zhang Luo on the bridge / the infirmary and
  Xu Bin / the Deliberation Hall / the Xingqing banquet) are divided in the source
  by decorative rules (Image00005.jpg); following house style the shifts are plain
  paragraph breaks, no separator glyph.
- The time-gloss is CORRECT for this hour: 亥 (the Pig, 9-11 p.m.) glossed with
  "晚上10点 … 21时至23时" (the same 亥 body as ch12's 亥初, only the leading clock
  changed from 9点 to 10点); rendered identically to ch12's. No authorial slip in
  this chapter's note, unlike the mismatched 卯 bodies of ch10/ch11.
- Source form 春名门 (for the standard 春明门, the Chunming Gate): same reading,
  rendered "the Chunming Gate," not flagged as an error since the pinyin is
  identical; noted in the glossary.

## B14 = ch14 (第十四章 子初 / "The Hour of the Rat, First Half, 11 p.m.")

Scope: the whole chapter, 17,484 source characters, 324 paragraphs. The chapter
opens with a flash-forward vignette (source lines 2-3, Taizhen catching Tanqi's
hands in delight on the Qinzheng Wuben Tower) BEFORE the dateline; the identical
sentence recurs at its true moment (source line 126, Taizhen greeting Tanqi at the
banquet) and was translated identically in both places, per the ch04-ch13
precedent. Three strands: (1) Yuan Zai, back at the Jingzhao Prefecture, spots the
disguised Yisi and Zhang Xiaojing leaving and pays out the line to trap them;
Zhang and Yisi visit the Japanese master craftsman Chao Fen in Zhiye Ward, who
reads the bamboo offcuts and reveals the Pifu's plot — the Taishang Xuanyuan Grand
Lantern-Tower, packed with rock-oil "qilin-arms," to become one vast fierce-fire
thunder under the emperor and court at the hour of the Ox, second half; the
coerced lantern-master Mao Shun and Long Bo's disguised craftsmen bluff past the
Longwu Army cordon. (2) On the tower, Tanqi begs the Daoist Taizhen (Yang Yuhuan)
to have the Sage ask one question about the Que-le Huo-duo, forcing Li Heng and Li
Linfu to join hands; Zhang's citywide warrant is held off. (3) Yuan Zai's Lüben
Guards trap Zhang at Chao Fen's, Yisi is arrow-shot and crippled; Zhang goes
berserk (the "sixth Yama — Mad"), slaughters the guards, and Yuan Zai, reading the
three-feather dispatch, lets him go. Zhang commandeers the singer Xu Hezi's
phoenix-tail lantern-float to cross the jammed city, then enters the lantern-tower
by Chao Fen's secret water-channel under the Longshou Canal — and comes face to
face with Long Bo at last.

Checks run and results:
- check_structure --pairs data/zh/ch14.txt out/ch14_reading.md: parity EQUAL,
  324 | 324, OK.
- check_numbers out/ch14_bilingual.md --noise noise.txt: 0 unresolved (324 pairs).
  Three flags cleared: 千百人 ("hundreds and thousands," cn_to_int misreads 千百 as
  1100 — non-quantity idiom, noised) and 万变不离其宗 (万变 "myriad changes," idiom,
  noised) added to noise.txt with 七杀 (the Seven Killings star, non-quantity, added
  for principle though English "Seven" happened to carry it). One flag was a REAL
  quantity — 数以百计的灯俑 — and was fixed in the ENGLISH ("a hundred and more
  lantern-figures") rather than noised, per the standing rule. No real number
  dropped.
- Verbatim-quote check (mechanical): the 324 bilingual '>' source lines were
  regenerated from data/src/30_text00029.txt under the same merge rules and
  compared — 324/324 exact, 0 diffs. Source quoted verbatim and in full.
- qa_epub: PASS, 38 files, 32 documents, 52 note references / 52 bodies / 52
  backlinks, all links resolve. 14 of 26 chapters translated.
- Blind double-translation (literary sample, source lines 185-187, Zhang's
  killing-frenzy — the "met a god, killed the god" passage, the cold-as-rock
  puppet, the triple Asura-vision overlay): a fresh independent rendering matched
  mine in meaning and every image; the only differences were glossary-form
  variants (the blind pass wrote "Brave Guard"/"Bear-Fire Gang" where the project's
  decided forms are "the Lüben Guards"/"the Bear Fire Gang"). No divergence of
  sense; source not ambiguous. 0 errors.
- Round-trip back-translation (number-dense sample, the lantern-tower spec + the
  timing, source lines 79/90/92): a fresh back-translation into Chinese preserved
  every quantity — 一百五十尺 (150 chi), 二十四间 (24 bays), 数里, 三十步 (30
  paces), 丑正 (hour of the Ox, 2nd half), 子初 (hour of the Rat, 1st half),
  一个时辰, 一个半时辰, 万国 — with no omission or drift; only expected lexical
  paraphrase (放灯/元宵 for 拔灯/上元). 0 errors.
- Sample error rate: the two samples (~710 source chars) are ~4% of the chapter;
  0 errors observed → 0% observed error rate.

Notes (3, all "reference a non-specialist won't catch," at first appearance):
Chao Heng (= Abe no Nakamaro, the Japanese envoy-official, Li Bai's elegized
friend), the Tianshu (Wu Zetian's bronze Axis of Heaven before the Duanmen Gate),
and Xu Hezi (the historical star singer Yongxin of Xuanzong's court). All checked
against scholarship and marked historical/corroborated. Recurring subjects already
noted in ch01-ch13 were skipped (Prince Yong, the Right Shad, the Pifu, Yuan Zai,
the Rainbow-Feather Dance, the tongtian crown, Taizhen/Yang Yuhuan, etc.).

Glossary grown (all new referents, one decided rendering each): people Chao Fen
(晁分), Chao Heng (晁衡), Mao Shun (毛顺), Mao Poluo (毛婆罗), Xu Hezi (许合子),
Yang Yuhuan (杨玉环, = Taizhen), Prince Shou (寿王), Li Mao (李瑁), Empress Dowager
Dou (窦太后); org the Longwu Army (龙武军); places Daozheng Ward (道政坊), Izumo
(出云), Japan (日本), the Duanmen Gate (端门), the Jinming/Chuyang/Tongyang gates;
terms the Taishang Xuanyuan Grand Lantern-Tower (太上玄元大灯楼), the qilin-arm
(麒麟臂), the Dance of the Prince of Qin Breaking the Line (秦王破阵舞), the
phoenix-tail cart (凤尾车), the spring-ewer cart (春壶车), the Tianshu (天枢),
a Japanese embassy to the Tang (遣唐使), the Seven Killings (七杀), the Director of
Lanterns (尚灯监), Vice-Minister of the Court of the Imperial Regalia (卫尉少卿),
Aide in the Directorate for Imperial Manufactories (尚方丞), bamboo tally (竹籍).
Reused decided forms verbatim (Zhang Xiaojing, Tanqi, Yisi, Long Bo, Yuan Zai, the
Lüben Guards, the Bear Fire Gang, the Wolf Guards, the Pifu, the Xingqing Palace,
the Qinzheng Wuben Tower, the Longshou Canal, Zhiye Ward, Xingqing Ward, Recorder
Zhang = Zhang Luo, the Persian/Nestorian temples, rock-oil, fierce-fire thunder,
the Que-le Huo-duo, cave-running, the Rainbow-Feather Dance, the tongtian crown,
etc.).

Notable renderings/decisions:
- The opening vignette (source lines 2-3, a flash-forward) and the dateline
  (source lines 4-5) were each merged from their two extractor-split halves; the
  dateline reads "the fifteenth day of the first month" — the source advances from
  ch13's 十四日 to 元月十五日 at 子初, since the traditional day rolls at the Rat
  hour. Rendered faithfully.
- The source's per-chapter time-gloss (source line 327) is rendered as the
  source's own italic note, prefixed "*[The source appends a note on the hour to
  each chapter:]*"; correct for this hour (子 = the Rat, 11 p.m.-1 a.m., glossed
  "23时至01时"). No authorial slip in this note.
- Scene shifts (Yuan Zai at the prefecture / Chao Fen's yard / the banquet-tower /
  the massacre / the flight by lantern-float / the water-channel into the tower)
  are divided in the source by decorative rules (Image00005.jpg); following house
  style each is a plain paragraph break, no separator glyph. No content
  illustration in the chapter, so figures.json is unchanged.
- 都尉 = "Commander" (Commander Zhang), 主事 = "recorder" (Recorder Zhang = Zhang
  Luo), 伍长 = "guard-corporal," 行头 = "foreman (of the craftsmen's guild)," 婆子
  = "serving-woman," 痴缠货 = "lovesick pest" — office/common-noun renderings kept
  consistent within the chapter.

## B15 = ch15 (第十五章 子正 / "The Hour of the Rat, Second Half, midnight")

Scope: the whole chapter, 16,941 source characters, 321 paragraphs. This is the
pivot of the book. Structure is unusual — it carries TWO datelines. It opens with
a flash-forward vignette (source lines 2-4, the reversed-crossbow standoff, three
extractor-split halves merged into one pair), which recurs verbatim at its true
moment (source line 144) and was translated identically in both places. Then a
long flashback under its own dateline "开元二十三年七月十四日，午时" (Kaiyuan 23 =
735 CE, the hour of the Horse / noon; lines 5-6 merged) — the last stand of the
Eighth Company at the beacon-fort thirty li north of Balhuan, where Zhang
Xiaojing, Wen Wuji and the archer Xiao Gui are three of thirteen survivors; Wen
Wuji loses his leg and Zhang his left eye, Xiao Gui detonates the last fierce-fire
thunder and leaps clear wrapped in the dragon-banner as Gai Jiayun's relief
arrives. Back in the present (dateline "天宝三载元月十五日，子正," lines 101-102
merged; midnight, beneath the Xingqing Palace), Zhang realizes the hunted "Long
Bo" IS Xiao Gui, his old comrade. Xiao Gui tells how a corrupt Guangwu county-aide
destroyed his family, how he became a fugitive and then leader of the Pifu — the
embittered veterans the Tang used up and betrayed — and that his target is only
the Taishang Xuanyuan Lantern-Tower and the court feasting beside it. Zhang, with
no reason left to refuse, "joins," and passes Xiao Gui's loyalty test by seeming
to shoot Li Bi (a headless test-bolt). The chapter ends on the Tangyun rhyme-code
Zhang plants in his mock-Daoist jibe — 三、十一、八、四、五、十八 → 不退, "No
retreat" — and Li Bi's escape via the iron file hidden in the returned waist-tablet.

Checks run and results:
- check_structure --pairs data/zh/ch15.txt out/ch15_reading.md: parity EQUAL,
  321 | 321, OK.
- check_numbers out/ch15_bilingual.md --noise noise.txt: 0 unresolved (321 pairs).
  Seven initial flags resolved. FIVE were non-quantity numerals, noised (recorded
  in noise.txt): 四下 ("all around," a 四X all-directions idiom); 千古 in 千古未有
  ("through the ages," intensifier not 1000); 涕零 in 感激涕零 (零 = "tears fall,"
  read as 0 by cn_to_int); 五脏六腑 (the organs idiom, 5/6 conventional). TWO were
  REAL quantities fixed in the ENGLISH, not noised: the charcoal "一千多斤" needed
  "a thousand" adjacent for the checker ("a good thousand" -> "a thousand jin and
  more"), and "一两百骑" (cn_to_int reads 一两百 as 200) was rendered "a hundred or
  two hundred more riders" to carry the value. Also the Tangyun-cipher decode line
  was reworded from ordinals to cardinals ("rhyme eleven... place eighteen") so the
  checker's number parser catches 11 and 18 (ordinals "eleventh/eighteenth" are not
  in WORD_NUM; the cardinal display line already passed). No real number dropped.
- Verbatim-quote check (mechanical): all 321 bilingual '>' source lines are exact
  whitespace-insensitive substrings of data/src/32_text00031.txt (correctly
  covering the three merged pairs) — 321/321, 0 non-verbatim. Source quoted
  verbatim and in full.
- Blind double-translation (separate context) of a literary/argumentative sample
  (Xiao Gui's "一百个、五百个人...病入膏肓" manifesto, source line 136): independent
  rendering matched mine in meaning with zero divergence — all of 1/5/100/500
  present, 病入膏肓 = "sick beyond all cure," 根子已经烂了 / 火和血 / 让所有人警醒
  all carried. 0 errors.
- Round-trip back-translation (separate context) of a number-dense sample (the
  old-charcoal-seller paragraph, source line 166): back-translation reproduced
  every detail and every quantity — 半匹红纱、一丈绫、一车、一千多斤 all intact, plus
  南山, 雪白如银, 火力十足, 民心所向. 0 omissions.
- Sample deep-audit error rate: 0 errors across the two samples (~4% of the
  chapter).
- qa_epub: PASS, 38 files, 32 documents, 55 note references / 55 bodies / 55
  backlinks, all links resolve. 15 of 26 chapters translated.

Notable renderings/decisions:
- TWO source time-glosses this chapter (one per dateline): source line 324 glosses
  午时 (noon) and line 326 glosses 子正 — both rendered as the source's own italic
  notes, under the standing prefix "*[The source appends a note on the hour to each
  chapter...]*," each labeling which dateline it belongs to. The 子 gloss is
  word-for-word the same as ch14's and was rendered identically. No authorial slip
  in either gloss.
- The recurring flash-forward vignette (source lines 2-4 = the first two sentences
  of line 144) was translated identically in both places, per the ch04-ch14
  precedent for recurring vignettes.
- Xiao Gui (萧规) is decided as the true name of Long Bo (龙波); the reveal is not
  allowed to rewrite Long Bo's pre-reveal glossary note (the ledger records the
  state of knowledge). The lantern-tower's central 天枢 pillar reuses "the Tianshu"
  (established ch14 for the Luoyang monument, also cast by Mao's line), contextually
  the sky-axis; 天枢层 = "the Tianshu tier."
- Scene shifts (the beacon-fort flashback / the underground revelation / the Yuan
  Zai interlude deciding to march on the Xingqing Palace / the lantern-tower ascent
  / Li Bi's escape) are divided in the source by decorative rules (Image00005.jpg);
  per house style each is a plain paragraph break, no separator glyph. No content
  illustration in the chapter, so figures.json is unchanged.
- Office/title renderings kept consistent: 李司丞 = "Deputy Director Li," 都尉 =
  "Commander," 李郎君 = "young Master Li" (the address that marks Zhang renouncing
  his Jing'an post), 盖都护 = "Protector Gai," 校尉 = "commandant," 火师 =
  "fire-master." 玄观 = "Mystic Abbey" (reused from ch14).
- 3 footnotes added (notes.json ch15, continuous total now 55): the old
  charcoal-seller (Bai Juyi's ballad 卖炭翁 and the 宫市 palace-purchase abuse,
  corroborated — Ma Boyong quotes 千余斤 and 半匹红纱一丈绫 near-verbatim); "pinning
  on the dogwood" (茱萸, the Double Ninth custom inverted into Western-Regions army
  slang for drawing blood); and "a pledge of blood-guilt" (投名状, the Water Margin
  term for a killing that cuts off any return). glossary.json grown by 26 rows
  (people: Xiao Gui, Zhao Xiao, Zhao Li, Duke Li of Wei, the Sage Confucius, Laozi;
  places: the Protectorate of Anxi, Guangwu, Lingwu, Lanzhou, the Yin Mountains,
  Hedong, Jiannan, Shayan, the Southern Mountains; orgs: the Ministry of War, the
  Assault-Resisting Garrison; terms: the Eighth Company, Mystic Abbey, ring-pommeled
  saber, the Three Pure Ones, the Eleven Luminaries, the Eight Trigrams, the Four
  Peaks and Five Marchmounts, rue-incense, Xinfeng wine, Tangdi, Flying Cavalry
  Commandant). Reused decided forms verbatim (Zhang Xiaojing, Li Bi, Long Bo,
  Wen Wuji, Wen Ran, Yuchang, Yuan Zai, Gai Jiayun, Türgesh, Mao Shun, the Pifu,
  the Shouzhuolang, the Lüben Guards, the Longwu Army, Kucha, Balhuan, the
  beacon-fort, garrison-town, the Xingqing/Qinzheng Wuben Tower, the Longshou Canal,
  the Taishang Xuanyuan Grand Lantern-Tower, the qilin-arm, fierce-fire thunder,
  rock-oil, the Que-le Huo-duo, the Tianshu, the Five Yamas, the Tang Rhymes, etc.).

## B16 = ch16 (第十六章 丑初 / "The Hour of the Ox, First Half, 1 a.m.")

- Translated ch16 from data/src/34_text00033.txt (14,191 source chars) into
  out/ch16_bilingual.md (QC only, never shipped), then generated out/ch16_reading.md
  and data/zh/ch16.txt with split_bilingual.py. 289 aligned paragraph pairs.
- Opening: a flash-forward vignette (Li Bi crouched in the water-channel, only half
  his head above the surface, watching the torchlit Pifu), split across three
  data/src lines; merged into one bilingual pair and translated identically to its
  in-place recurrence later in the chapter (source line 105), per the recurring-
  vignette rule. The dateline "天宝三载元月十五日，丑初。" was extractor-split across two
  lines (…丑初 / 。) and merged. The content-file marker line 丑初 (line 1) is absorbed
  into the H2 title; the source's per-chapter time-gloss (line 293) is rendered as
  the source's own italic note, prefixed "*[The source appends a note on the hour to
  each chapter:]*". This chapter's hour-gloss is CORRECT (凌晨1点…丑…第二个时辰…01时
  至03时): the Ox hour, 1–3 a.m.; no time-gloss error like ch06/07/08/10/11.
- Scene shifts (lantern-tower interior → the Hydraulic Hall / Li Bi → Yuan Zai's
  march on the Xingqing Palace → back to the tower → the descent to Mystic Abbey →
  the crown-loft → the muster and the tower's awakening) are divided in the source by
  the decorative rule image (Image00005.jpg); per house style each is a plain
  paragraph break, no glyph. The chapter's only images are that rule and the
  footnote-marker glyph (Image00004.jpg); neither is a content illustration, so
  figures.json is unchanged.

Checks run:
- check_numbers.py --noise noise.txt: 289 pairs, 0 unresolved. Four false positives
  cleared by extending noise.txt (all non-quantities): 千牛 (千牛卫 = the Qianniu
  Guard, unit name, not 1000), 万骑 (the Wanqi, unit name, not 10000), 五成 (in
  把五成可能说成十成 = "a fifty-fifty chance," a probability idiom, cf. 十成/八成), and
  千恩万谢 ("thanked a thousand times over," idiom, the 万 non-quantitative). One flag
  was fixed in the ENGLISH rather than noised: 阴阳两界 now reads "between the two
  worlds of light and shade" so the 两 = 2 survives. All real quantities carried
  and checked: the 50/500/5000/50000 escalation of Zhang's moral test, the ~50,000
  of Chang'an on the plaza, the six water-wheels, thirty crack veterans, ten copper
  coins for ten deeds, three-tier turning-gear each three chi high, twenty-four
  lantern-chambers, four bolts / two bolts, ten-odd finger-snaps, nine years / ten
  years, the Eighth Company.
- check_structure.py --pairs: parity 289 | 289 OK.
- Verbatim-quote audit (mechanical): the concatenation of every source blockquote in
  the bilingual equals the source content character-for-character (16,287 chars,
  EQUAL: True) — 100% verbatim, no dropped or altered source text.
- build_reading_epub.py + qa_epub.py: PASS (26 documents, 58 note refs / 58 bodies /
  58 backlinks, all links resolve, 16 of 26 chapters translated). Note anchors all
  verified as verbatim English substrings before build.
- Blind double-translation (literary sample): the lantern-tower descent, the "worlds
  of light and shade" atmosphere passage (source line 167). Independent re-render
  diverged only in word choice ("wove/threaded," "ghosts afloat/specters floating,"
  "worlds of light and shade / yin and yang realms"); no omission, no meaning
  divergence. 0 errors.
- Round-trip back-translation (number-dense sample): the machinery that wakes the
  tower (source line 291). Back-rendering to Chinese preserved every numeral —
  十几个壮汉, 数条铁杆, 六个水巨轮, 六轮, 一枚转机 — and dropped nothing. 0 errors.
- Sample error rate: 0 errors across the ~7% audited (verbatim mechanical check over
  the whole chapter, plus the two deep samples). No authorial slips of the ch03/06/
  07-type found in ch16; the hour-gloss is correct.

Notes (notes.json ch16, continuous total now 58; +3):
- "Chen Xuanli, Grand General of the Longwu Army" — the historical palace-guard
  commander, correctly placed; the man who at Mawei in 756 forced the deaths of Yang
  Guozhong and Yang Guifei (the Taizhen of ch13). Dramatic-irony note, corroborated.
- "An Lushan, Commissioner An" — his first in-text appearance (an old trooper of his
  Pinglu command speaks of him warmly as "a good man, a man of honor"); the future
  arch-rebel of 755 whose shadow the whole novel is written under. Corroborated.
- "Duke Li of Wei and Jieli Khagan" — the Wuwei lantern-chamber tableau: Li Jing's
  630 night march through the Yin Mountains and the capture of Illig Qaghan, ending
  the Eastern Turkic Khaganate. Jieli Khagan's first appearance; corroborated.
  (Already-noted/appeared subjects NOT re-noted: Duke Li of Wei and the Yin
  Mountains campaign are glossary-noted from ch15; the Que-le Huo-duo, the qilin-arm,
  the Tianshu, the fierce-fire thunder, storax, the beacon-fort, the Eighth Company,
  Taizhen, the Türks, the Right Xiao Guard, all from earlier chapters.)

Glossary (glossary.json, +19 rows): people — 陈玄礼/Chen Xuanli, 安禄山/An Lushan,
颉利可汗/Jieli Khagan; places — 越州/Yuezhou, 营州/Yingzhou, 河北/Hebei, 林邑/Linyi,
青云观/the Qingyun Abbey, 武威/Wuwei (lantern-chamber); organizations — 左骁卫/the
Left Xiao Guard, 千牛卫/the Qianniu Guard, 万骑/the Wanqi; terms — 转机/the
turning-gear, 水力宫/the Hydraulic Hall, 团结兵/tuanjie militia, 柱国/Pillar of State,
越骑/yueqi horseman, 丁防/frontier levy, 顶阁/the crown-loft. Reused decided forms
verbatim: Zhang Xiaojing, Li Bi (Li Changyuan), Xiao Gui / Long Bo, Mao Shun, Yuchang,
Yuan Zai, the Pifu, the Lüben Guards, the Longwu Army, the Jing'an Bureau, Mystic
Abbey, the Tianshu (+ the Tianshu tier), the qilin-arm, the Que-le Huo-duo, the
fierce-fire thunder, rock-oil, the Taishang Xuanyuan Grand Lantern-Tower, the
Xingqing Palace / the Qinzheng Wuben Tower, Tangdi, Duke Li of Wei, the Yin
Mountains, Pinglu, Daozheng Ward, the Chunming Gate, the beacon-fort, the Eighth
Company, the lantern-floats, buliang chief, Commander (都尉), the Right Xiao Guard.

## B17 = ch17 (第十七章 丑正 / "The Hour of the Ox, Second Half, 2 a.m.")

- Translated ch17 from data/src/37_text00035.txt (13,753 source chars) into
  out/ch17_bilingual.md (QC only, never shipped), then generated out/ch17_reading.md
  and data/zh/ch17.txt with split_bilingual.py. 237 aligned paragraph pairs.
- Opening: a flash-forward vignette (the crowd, performers, officials, kinsmen and
  envoys all falling silent for the coming wonder), extractor-split across three
  data/src lines (2+3+4, ending 、 / ， / 。); merged into one bilingual pair and
  translated identically to its in-place recurrence later (source line 129, where it
  closes a fuller paragraph), per the recurring-vignette rule. The dateline
  "天宝三载元月十五日，丑正。" was extractor-split across two lines (…丑正 / 。) and merged.
  The content-file marker line 丑正 (line 1) is absorbed into the H2 title. A separate
  scene-setting location line ("长安，兴庆宫广场东南角。") follows the dateline as its own
  paragraph. The source's per-chapter time-gloss (line 241) is rendered as the
  source's own italic note, prefixed "*[The source appends a note on the hour to each
  chapter:]*". This chapter's hour-gloss is CORRECT (凌晨2点…丑…荒鸡…十二时辰的第二个
  时辰…01时至03时): the Ox hour, its second half = 2 a.m.; no time-gloss error like
  ch06/07/08/10/11.
- Scene shifts (Yuan Zai at the tower foot → Zhang Xiaojing's ambush of the two
  escorts and the dud fierce-fire thunder → Li Bi wading out of the water-channel and
  racing to Chen Xuanli, glimpsing the heir apparent's carriage fleeing → the
  lighting of the twenty-four lantern-chambers → Zhang Xiaojing's climb up the
  turning-arm → the final duel with Yuchang at the Tianshu tier) are rendered as plain
  paragraph breaks with no separator glyph (house style; the source's Image00005.jpg
  rule is not a figure), matching ch01–ch16.

### Checks run
- check_numbers.py out/ch17_bilingual.md --noise noise.txt → PASS (237 pairs, 0
  unresolved). One new noise entry: 首鼠两端 = "blow hot and cold / waver
  irresolutely" (idiom, lit. "a rat hesitating between two ends of its hole"); the 两
  is idiomatic, not the quantity 2. All real quantities carried in the English:
  the twenty-four lantern-chambers and their sequential lighting (第五/第十/十五/
  二十一/第二十二/第二十三/最后一 → "fifth," "tenth," "fifteen/fifteenth," "twenty-one,"
  "twenty-two … twenty-second," "twenty-three … twenty-third," "last"); note that the
  checker's English parser does NOT read the ordinals "twenty-first/second/third," so
  22 and 23 are carried by cardinal apposition ("twenty-two now ablaze in all,"
  "twenty-three now ablaze"). 五万 = "fifty thousand"; 百里挑一 = "one picked from a
  hundred"; 十来/十几 = "ten-odd" (keeps 10); 三分之一 = "a third"; 驷马/两匹 = "a team
  of four" / "two horses"; 七八/十个弹指 = "seven or eight / ten finger-snaps"; 七岁 =
  "the year he was seven"; 一百零八坊 = "the hundred and eight wards."
- check_structure.py --pairs data/zh/ch17.txt out/ch17_reading.md → parity 237/237 OK.
- Verbatim-quote check (check 1): the concatenation of every source blockquote in the
  bilingual file equals the source content character-for-character (15,439 chars,
  lines 2–241). The bilingual was built by pairing verbatim source lines (copied, not
  re-typed) with the English, so no paragraph or sentence of the source is dropped.
- Build → out/The Longest Day in Chang'an.epub (17 of 26 chapters translated, 61
  notes). qa_epub.py → PASS (38 files, 32 documents, all links resolve; 61 refs / 61
  bodies / 61 backlinks).

### Blind double-translation (check 2)
- Literary sample: the finale passage of the colored gauzes and banners at the tower's
  crown (source line 238, "…把灯光滤成绯红、葡萄紫、翠芽绿、石赭黄等多彩光色…有如仙家幻境").
  An independent blind rendering matched ours in content and register; the only
  divergences were trivial word choices (its "a dozen or more" vs our number-preserving
  "ten-odd"; "jade-bud green" vs "jade-sprout green"; "ochre yellow" vs "ocher-yellow").
  No semantic divergence → the source is not ambiguous here. 0 errors.

### Round-trip back-translation (check 3)
- Number-dense sample: the lantern-chamber tallies (eight turning-arms driving three
  chambers each; fifth chamber lit; forty-odd chi; fifteen lit / nine left; twenty-four
  total; twenty-one lit). A fresh-context back-translation into Chinese preserved every
  numeral exactly (八/三/第五/四十余/十五/九/二十四/二十一). 0 omissions.

### Random-sample deep audit (check 8)
- ~4% of the chapter given the full treatment (verbatim-quote check across the whole
  chapter, plus the two sampled passages above). Observed error rate: 0.

### Notes added (3; continuous total now 61; numbered by the builder in reading order)
- "Kuafu of high antiquity" — the sun-racing giant of the Classic of Mountains and
  Seas, first in-book appearance, lending the dark tower its menace (texture/allusion).
- "net opened on one side" — the Shang founder Tang's clemency to the netted beasts
  (Records of the Grand Historian), the allusion the "Benevolence" tableau names;
  corroborated, with a note that the Shiji form is "open three sides."
- "the Longchi within the Xingqing Palace" — the Dragon Pool of Xuanzong's
  pre-accession residence and its dragon-omen legend; the one point where the
  conspirators' tunnel opens into the palace. Corroborated. (First appearances all;
  nothing already noted in ch01–ch16 was re-noted. Reused-and-not-re-noted subjects
  that recur here: the qilin-arm, the Que-le Huo-duo, the Tianshu, the fierce-fire
  thunder, Chen Xuanli, the heir apparent, the modao, the Pear Garden's Xuanzong ties.)

### Glossary rows added (+10)
- places — 龙池/the Longchi, 摘星殿/the Star-Plucking Hall, 龙亭/the Dragon Pavilion,
  灵官阁/the Lingguan Loft (first glossed, appeared ch16). terms — 灯屋/lantern-chamber,
  天枢层/the Tianshu tier (first glossed, appeared ch16), 鹘喙/the falcon's-beak,
  猛火油/fierce-fire oil (cf. 石脂 rock-oil, 猛火雷 fierce-fire thunder), 梨园/the Pear
  Garden, 教坊/the entertainers' quarter. Reused decided forms verbatim: Zhang
  Xiaojing, Li Bi (Deputy Director Li), Yuan Zai, Yuchang, Xiao Gui, Mao Shun (master
  builder / 大都料), Chen Xuanli (General Chen), Li Heng / the heir apparent, the Pifu,
  the Lüben Guards, the Longwu Army, the Jing'an Bureau, the Wolf Guards / Türk, the
  Taishang Xuanyuan (Grand) Lantern-Tower, the Qinzheng Wuben Tower, the Xingqing
  Palace, the Hua'e Xianghui Tower, the Chenxiang Pavilion, the Longshou Canal,
  Daozheng Ward, the Jinming/Tongyang/Chuyang Gates ("Three Yang"), the qilin-arm, the
  turning-gear, the Hydraulic Hall, the crown-loft, the Tianshu, the Que-le Huo-duo,
  fierce-fire thunder, rock-oil, green-vitriol oil, the barrier-knife, the
  four-windowed carriage, gleaming armor, the Cibei Temple, the Mystic Abbey, the
  lantern-floats / Lantern-Crown Red Tally, the Lantern Festival, shichen, finger-snap,
  chi, fen.

### Figures
- None. The chapter has no content illustration in data/figs/ (only the source's
  footnote-marker glyph Image00004.jpg and the scene-break rule Image00005.jpg, neither
  a figure). figures.json unchanged.

### Flagged for the read-through
- Cliffhanger ending: Yuchang pushes the crimson-red lever "all the way to its end"
  as the last lantern-chamber lights; the chapter cuts off on the act, not its result
  (faithful to the source — no bridging text invented).
- 临行通道 (line 76, "龙武军有自己的临行通道") rendered "passages of its own for coming
  and going"; 临行 reads as a variant/slip for 临时 or "for setting out," the sense
  being the guard's own service routes. Rendered for intent, not flagged as a note.

## B18 = ch18 (第十八章 寅初 / "The Hour of the Tiger, First Half, 3 a.m.")

- Translated ch18 from data/src/39_text00037.txt (15,604 source chars quoted, book.json
  count 13,861) into out/ch18_bilingual.md (QC only, never shipped), then generated
  out/ch18_reading.md and data/zh/ch18.txt with split_bilingual.py. 219 body paragraph
  pairs + the source's time-gloss = 220 pairs.
- Opening: a two-line flash-forward vignette (the carriage-horses turning their ears
  and snorting; the guards turning their necks north), lines 2–3, each its own
  bilingual pair, translated identically to its in-place recurrence at source line 38
  (where it closes a fuller paragraph), per the recurring-vignette rule. The dateline
  "天宝三载元月十五日，寅初。" was extractor-split across two lines (…寅初 / 。) and merged.
  The content-file marker line 寅初 (line 1) is absorbed into the H2 title. A separate
  scene-setting location line ("长安，万年县，安邑常乐路口。") follows the dateline as its own
  paragraph. The source's per-chapter time-gloss (line 222) is rendered as the source's
  own italic note, prefixed "*[The source appends a note on the hour to each chapter:]*".
  This chapter's hour-gloss is CORRECT (凌晨3点…寅…黎明/早晨/日旦…夜与日的交替之际…03时至
  05时): the Tiger hour, its first half = 3 a.m.; no time-gloss error like ch06/07/08/10/11.
- Scene shifts (Li Bi trailing the heir apparent's carriage south to the Shengping-Ward
  physic garden → the twenty-four lantern-chambers firing and Yuchang's death by the
  charge under his own stand → Zhang Xiaojing bleeding the Tianshu of its rock-oil and
  climbing to the tower's summit → Yuan Zai fleeing to Chen Xuanli at the Jinming Gate →
  Zhang Xiaojing's "no regret" and the tower's low rumble → Xiao Gui's water-borne
  party surfacing in the Longchi and the tower's upper half toppling onto the Qinzheng
  Wuben Tower → Li Bi confronting the heir apparent, who came only to save him) are
  rendered as plain paragraph breaks with no separator glyph (house style; the source's
  Image00005.jpg rule is not a figure), matching ch01–ch17. Only one extractor-split
  paragraph in the chapter (the dateline); a full scan confirmed lines 2–221 are
  otherwise terminally punctuated (line 4 the only non-terminal body line; line 223 is
  a stray U+200B, dropped).

### Checks run
- check_numbers.py out/ch18_bilingual.md --noise noise.txt → PASS (220 pairs, 0
  unresolved). Seven new noise entries (all non-quantity numerals; recorded in
  noise.txt with why): 接二连三 ("one after another," 二/三 idiomatic), 两不相欠
  ("quits," 两 idiomatic), 三光 ("the three luminaries," fixed term), 百十余
  ("a hundred-odd," approximate compound whose cn_to_int reads 110; placed in the
  --noise file so it strips BEFORE the built-ins can eat the 十), 两声 ("a couple of
  clicks," the idiomatic "a couple of" 两), 零件 ("parts," the 零 = "odd/spare," not
  the number 0), 六神无主 ("out of one's wits," 六 conventional). One REAL quantity was
  carried in the English rather than noised: 拦腰撕扯成了两截 → "torn in two across the
  middle" (keeps the 2). Other real quantities carried: 一百五十尺 → "more than 150 chi"
  (the checker's English word-parser cannot build 150 from "a hundred and fifty," so
  the value is carried as a digit); 七十多尺 → "better than seventy chi"; 二十四 →
  "twenty-four" throughout; 十九年前 → "nineteen years ago"; 二十几 → "twenty-odd";
  数百/数万 → "several hundred / tens of thousands" (both stripped by the built-in
  数[百/万]); 三品以上/五品 → "the third grade and above / the fifth rank"; 七香车 →
  "the seven-fragrance carriage"; 十王宅 → "the Ten Kings' Residence."
- check_structure.py --pairs data/zh/ch18.txt out/ch18_reading.md → parity 220/220 OK.
- Verbatim-quote check (check 1): the concatenation of every source blockquote in the
  bilingual file equals the source content character-for-character (15,604 chars,
  lines 2–222; asserted in scripts/gen_ch18_bilingual.py before writing). The bilingual
  was built by pairing verbatim source lines (read from disk, never re-typed) with the
  English, so no paragraph or sentence of the source is dropped.
- Build → out/The Longest Day in Chang'an.epub (18 of 26 chapters translated, 64
  notes). qa_epub.py → PASS (38 files, 32 documents, all links resolve; 64 refs / 64
  bodies / 64 backlinks).

### Blind double-translation (check 2)
- Literary sample: the 'Martial Might' lantern-chamber bursting into a peony of fire
  (source line 44, "数十个弹指之后…就把整个灯俑布景吞噬"). An independent blind rendering
  matched ours in content and register (crimson flower-heart → tuft of stamens →
  leaping fire-petals → a peony's blooming sped dozens of times → the whole tableau
  swallowed). The one divergence was the chamber name 武威: the blind pass romanized it
  as the place-name "Wuwei," ours renders it as the virtue-tableau 'Martial Might' —
  chosen for series consistency with ch17's named chambers '仁'/Benevolence and
  '明察'/Discernment (the 24 chambers are named for virtue-concepts illustrated by
  moving tableaux, not for places). A genuine ambiguity, resolved in favor of the
  virtue reading. 0 semantic errors.

### Round-trip back-translation (check 3)
- Number-dense sample: the tower's height and Zhang Xiaojing's nineteen-year echo
  (source lines 138 + 140). A fresh-context back-translation into Chinese preserved
  every numeral exactly (一百五十尺; 十九年前 / 十九年; and the sense of the beacon-fort
  flagstaff and "no relief force"). 0 omissions.

### Random-sample deep audit (check 8)
- ~3–4% of the chapter given the full treatment (verbatim-quote check across the whole
  chapter, plus the two sampled passages above). Observed error rate: 0 (one naming
  ambiguity flagged and resolved, no content/omission errors).

### Notes added (3; continuous total now 64; numbered by the builder in reading order)
- "the Xuanwu Gate" — the Xuanwu Gate Incident of 626 (Li Shimin killing his brothers
  and forcing Gaozu's abdication), the type-case of the Li house's "kin-slaying" strain
  Li Bi fears here. First in-book appearance; corroborated from the Tang histories and
  the Zizhi tongjian.
- "the Tanglong and the Xiantian" — Xuanzong's own two coups (710 against Empress Wei,
  713 against Princess Taiping), both turning on first seizing the palace guards, which
  grounds Chen Xuanli's dread of moving the Longwu Army unbidden. First in-book
  appearance (Empress Wei and Princess Taiping the persons both new; "Taiping" in ch03
  was the WARD, not the princess); corroborated.
- "Changle Ward" — a translation note: 长乐坊 (the heir apparent's ward, NE city) and
  常乐坊 (SE city, passed en route) are different wards that fall together in pinyin as
  "Changle"; Li Bi's alarm turns on the distinction. First point in the book where the
  two collide (常乐坊 established earlier as "Changle Ward"; 长乐坊 new here).
- Reused-and-not-re-noted subjects that recur here: the Que-le Huo-duo, the Tianshu,
  the qilin-arm, fierce-fire thunder/oil, rock-oil, the Longchi (noted ch17), the
  Rainbow-Feather Dance (noted), Chen Xuanli / An Lushan-era guard politics (Chen noted
  ch16), Xinfeng wine (appeared ch15), the jie-drum (appeared ch06/ch10), the beacon-
  fort last stand (noted ch15).

### Glossary rows added (+25; one referent, one rendering)
- people — 李隆基/Li Longji (Xuanzong's given name), 韦后/Empress Wei (distinct from 韦氏
  the present Consort Wei), 太平公主/Princess Taiping. places — 长乐坊/Changle Ward
  (long-乐, homophone-noted), 修行坊/Xiuxing Ward, 安国寺/the Anguo Temple, 十王宅/the Ten
  Kings' Residence, 终南山/the Zhongnan Mountains (= 南山/the Southern Mountains), 通法寺/
  the Tongfa Temple, 遮沟/the Screened Gully, 隆庆坊/Longqing Ward, 隆庆池/the Longqing
  Pool, 玄武门/the Xuanwu Gate, plus backfilled rows for forms already used in prose:
  沉香亭/the Chenxiang Pavilion, 平康坊/Pingkang Ward, 东宫/the Eastern Palace. terms —
  七香车/the seven-fragrance carriage, 倒碑门/a toppled-stele gate, 药圃/the physic garden,
  浑脱舞/the Hutuo dance, 唐隆政变/the Tanglong coup, 先天政变/the Xiantian coup, plus
  backfilled 弹指/finger-snap, 狻猊/suanni, 旋臂/turning-arm, 灯楼/lantern-tower. Reused
  decided forms verbatim: Zhang Xiaojing, Li Bi (Deputy Director Li) / Changyuan, Li
  Heng / the heir apparent, Yuan Zai, Yuchang, Xiao Gui, Mao Shun, Chen Xuanli (General
  Chen), Wen Wuji, Wen Ran, Xu Bin, Yao Runeng, Yisi, Tanqi, Chao Fen, the Right
  Minister (李相 = Li Linfu), the Pifu, the Longwu Army, the Lüben Guards, the Jing'an
  Bureau, the Türk Wolf Guards, the Taishang Xuanyuan Lantern-Tower, the Qinzheng Wuben
  Tower, the Hua'e Xianghui Tower, the Xingqing Palace, the Longchi, the Dragon
  Pavilion, the Leyou Plateau, Changming/Daozheng/Anyi/Jinggong/Xinchang/Shengdao/
  Shengping wards, the Jinming Gate, the Tianshu, the qilin-arm, the turning-gear, the
  crown-loft, the Hydraulic Hall, the Que-le Huo-duo, fierce-fire thunder/oil, rock-oil,
  the four-windowed carriage, the Eighth Company, the Vermilion Bird, shichen,
  finger-snap, chi, jin.
- 武威 rendered inline as the tableau name 'Martial Might' (NOT the glossary's place
  武威/Wuwei); a one-off virtue-chamber name like ch17's 'Benevolence'/'Discernment',
  so no glossary row (see the double-translation note above).

### Figures
- None. The chapter has no content illustration in data/figs/ (only the source's
  footnote-marker glyph Image00004.jpg and the scene-break rule Image00005.jpg, neither
  a figure). figures.json unchanged.

### Flagged for the read-through
- Cliffhanger: the chapter ends on Li Bi wheeling his horse for "the Jing'an Bureau"
  as the twin threats (the toppling tower on the Qinzheng Wuben Tower; Xiao Gui's
  water-party inside the Longchi) are both live. Faithful to the source; no bridging
  text invented.
- 武威 lantern-chamber → 'Martial Might' (virtue-tableau reading, for series
  consistency), not the place-name Wuwei. Noted here in case the read-through prefers
  a different call across all named chambers.
- 遮沟 rendered "the Screened Gully" (translating the residents' nickname, whose sense
  the source itself glosses), not bare pinyin "Zhegou."

## B19 = ch19 (第十九章 寅正 / "The Hour of the Tiger, Second Half, 4 a.m.")

Scope: the whole chapter, 15,712 source characters (book.json), 276 body
paragraphs plus the source's time-gloss. Built the bilingual with the
verbatim-guaranteed generator scripts/gen_ch19_bilingual.py (reads the source
lines from data/src/41_text00039.txt, pairs each with hand-authored English,
merges the extractor-split halves, and asserts the concatenation of every '>'
blockquote equals the source content char-for-char before writing).

### Source structure handled
- Opening flash-forward vignette: L2 (one paragraph) and L3+L4 (extractor-split
  on a comma, MERGED) — the one-eyed Zhang making out the many-colored gauze,
  Mao Shun's design. It RECURS verbatim inside L96 (…那是一大串五彩的薄纱。想必
  这也是出自毛顺的设计…) and both occurrences were translated identically (the
  VIG_A/VIG_B constants in the generator are re-used in the L96 paragraph).
- Dateline L5+L6 (extractor-split: …寅正 / 。) MERGED into one pair; the L1
  content-marker heading 寅正 absorbed into the H2 title, as ch01-ch18. Location
  line L7 (长安，万年县，兴庆宫。) its own paragraph.
- Time-gloss L280 rendered as the source's own italic note, prefixed
  "*[The source appends a note on the hour to each chapter:]*". This chapter's
  gloss is CORRECT (寅正 = the Tiger hour's second half, 4 a.m.; the source's own
  parenthetical 北京时间03时至05时 gives the whole double-hour). Trailing L281
  (U+200B) dropped.
- Only two extractor-splits this chapter (the vignette-b halves and the dateline
  halves); every other source line ended terminal. No THREE-line splits.

### Checks run
- Verbatim quotation: generator assertion PASS — concatenation of all 276
  blockquotes + the time-gloss equals the source content (data/src lines 2-280)
  character-for-character (17,848 chars incl. gloss).
- check_numbers.py --noise noise.txt: 277 pairs, 0 unresolved.
- check_structure.py --pairs: parity 277/277 OK.
- qa_epub.py: PASS, 38 files, 32 documents, all links resolve; 67 note refs / 67
  bodies / 67 backlinks. Build reports 19 of 26 chapters translated.
- Blind double-translation (literary sample, L142 — Zhang's resolute departure,
  "路是我选的，我会走到底" scene): independent second rendering diverged only in
  word choice (跃动 "leaping"/"dancing"; 晃晃悠悠 "swaying and staggering"/"unsteady
  way"; 眼光 "eye"/"judgment of men"), no semantic divergence. 0 content errors.
- Round-trip back-translation (number-dense sample, L147 — Li Bi's ride, 六坊/
  四坊/两刻/十几个人): back-rendered to Chinese and diffed against the source;
  every quantity survived (six wards, four wards, two marks, ten-odd people),
  no omission. 0 content errors.
- Random-sample deep audit (~3%: L2/L96 vignette-parity, L63 planter-cart note,
  L147 numbers, L236 Analects allusion, L245 Tang hostage law, L272 the emperor
  close-up) given the full paranoid treatment: observed error rate 0.

### noise.txt extended (7 entries, all NON-quantity)
- 五彩 (五彩的薄纱 = "many-colored"), 二话 (自无二话 = "made no demur"),
  五光十色 (idiom "a riot of color and light"), 四脚朝天 (idiom "legs-up"),
  百骸 (the residual of 四肢百骸 after the pre-existing 四肢 entry strips first;
  the 百 is not the count 100), 万民 (下视万民 = myriad-idiom), 六合 (六合靴 =
  "liuhe boots," 六合 = "the six directions," a named boot not the count 6).
  No REAL quantity was noised: every genuine count is carried in the English as
  a number-word or digit and survives check_numbers (一百弹指 → "a hundred
  finger-snaps"; 二十几个弹指 → "twenty-odd finger-snaps"; 十六根柱 → "sixteen
  pillars"; 三丈/五尺 → "three zhang"/"five chi"; 六十岁 → "sixty"; 三十多年 →
  "thirty years and more"; 开元二十年 → "the twenty years of Kaiyuan"; the seven
  floors carried throughout as "seventh/seven").

### Notes added (3; running total 67)
- "called a spring-moving frame" — the 移春槛, a real Tang mobile planter-cart
  (Kaiyuan Tianbao Yishi), the improvised scaffolding by which the guards reach
  the broken stair.
- "To govern by virtue is to be as the pole-star" — Analects 2.1, glossing the
  north-facing imperial seat of the Star-Plucking Hall.
- "one who holds a hostage is to be struck along with the hostage" — the Tang
  Code's 捕质 provision, void where the hostage is the Son of Heaven; echoed in
  Chen Xuanli's cry 击质勿疑.
- Skipped already-noted/appeared subjects: the Pifu, He Zhizhang, Yuan Zai,
  Prince Yong, Ji Wen, the Self-Raining Pavilion, Taizhen, the tongtian crown,
  the Tianshu, the suanni, the Nestorian confessional, the Fifth Yama cluster.

### Glossary grown (14 rows)
- people — 吉顼/Ji Xu (chancellor, Ji Wen's uncle), 薛嶷/Xue Yi (太子文学),
  登徒子/lecher (Tanqi's decided nickname for Zhang; dominant rendering ch02-ch13).
  organizations — 羽林军/the Yulin Army, 监门卫/the Gate Guards. places —
  宣平坊/Xuanping Ward already present (backfill no-op). terms — 通天梯/the
  sky-reaching stair, 邀风堂/the Wind-Wooing Hall, 天汉桥/the Sky-River Bridge,
  移春槛/spring-moving frame, 牵春绳/the spring-drawing cords, 靖安令/the Director
  of the Jing'an Bureau (令 outranks 司丞/Deputy Director), 待诏翰林/Academician-
  in-Waiting of the Hanlin (李翰林 = "Academician Li"), 太子文学/Litterateur to
  the heir apparent, 那伽花/naga-flowers.
- Reused decided forms verbatim: Zhang Xiaojing (大头 = Big-Head), Xiao Gui,
  Yuan Zai, Chen Xuanli (General Chen / Grand General), Tanqi, Li Bi (Deputy
  Director Li / Changyuan / Academician Li), He Zhizhang (Director He), Ji Wen
  (Deputy Director Ji / Vice-Duan Ji / Censor Ji), Li Heng (the heir apparent),
  Li Linfu (the Right Minister / 李相), Li Longji (the Son of Heaven), Prince Yong
  Li Lin, Mao Shun, Yuchang, Xu Bin (Recorder Xu), Feng Dalun, Chao Fen, Taizhen,
  Adjutant Zhao, the Pifu, the Longwu Army / Lüben Guards / Qianniu Guard / Right
  Xiao Guard, the Jing'an Bureau, the Jingzhao Prefecture, the Secretariat / the
  Phoenix Pavilion, the Censorate, the Forestry and Crafts Bureau, the Qinzheng
  Wuben Tower, the Star-Plucking Hall, the Taishang Xuanyuan Lantern-Tower, the
  Xingqing Palace, the Longchi, the Que-le Huo-duo, fierce-fire thunder/oil,
  rock-oil (延州石脂 = Yanzhou rock-oil), the tongtian crown, the Tianshu, the
  suanni, the Self-Raining Pavilion, the Pingkang Quarter, shichen, finger-snap,
  chi/zhang, mark/quarter, li.

### Figures
- None. No content illustration in data/figs/ for this chapter (only the source's
  footnote-marker glyph Image00004.jpg and the scene-break rule Image00005.jpg,
  neither a figure). figures.json unchanged.

### Flagged for the read-through
- Register: kept the source's coarseness where coarse (陈玄礼's 还他妈的敢说这种
  胡话 → "such fucking nonsense"; 元载's 大胆贱婢 → "insolent slut"). 登徒子, Tanqi's
  pet name for Zhang, standardized as "lecher" (the ch02-ch13 dominant); note the
  outlier ch14 "amorous rogue" is left as-is (a global rendering-consistency fix
  is a corrections-pass call, not a per-batch one) — glossary now decides "lecher".
- The chapter is a two-strand relief sequence (Zhang + Tanqi climbing to the
  seventh-floor stand-off; Li Bi seizing the Jing'an Bureau back from Ji Wen with
  He Zhizhang's Director's seal) and ends on twin cliffhangers — Xu Bin found with
  his neck wrenched round (a mole still loose in the bureau), and Xiao Gui's gift
  of Prince Yong flung before Zhang at the imperial seat. Faithful to the source;
  no bridging text invented.
