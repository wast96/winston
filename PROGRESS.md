# PROGRESS — The Whistling Wind (风萧萧) by Xu Xu (徐訏)

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, chapter/section scope), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup / Step 0 (ingest + survey) — DONE, awaiting batch approval

- Source EPUB: `source.epub` = 风萧萧, simplified-character digital text
  (publisher metadata credits epub掌上书苑 / cnepub, dated 2020-09-17). No OCR.
  Color cover art present (568x800 JPEG).
- Ingest (`scripts/ingest_epub.py`): 63 spine documents, 2 images, 235,864
  source characters. Text to `data/src/`, cover to `data/figs/cover.jpg`,
  report `out/INGEST.md`, draft `book.draft.json`.
- Structure: the source's file boundaries do NOT match the logical book, so
  `book.json` was authored by hand from the draft:
  - ch00 = About the Author (作者简介, source `chapter2.html`) — front matter.
  - ch01..ch58 = the novel's 58 numerically-headed chapters (源 一..五十八 =
    source `chapter3.html`..`chapter60.html`). Verified: my ch01..ch58 map
    one-to-one onto the source headings 一..五十八.
  - ch59 = Impressions of Xu Xu (徐訏印象, source `chapter62.html`) — appendix.
  - THREE source documents are deliberately NOT modelled as body chapters and
    are recorded in `book.json` `_source_note` so they are not silently
    dropped: `coverpage.html` (cover image + an uploader-supplied scholarly
    abstract, reused as cover art + basis for the English catalogue
    description); `chapter61.html` (a 45-char edition/imprint note — to become
    the translated Colophon back-matter on the final batch); `chapter1.html`
    (the source's own 目录/TOC, superseded by the build's hyperlinked TOC).
- Metadata: pulled from the source OPF and fact-checked against Wikipedia /
  Baidu Baike scholarship (author dates, original serialization, character
  roles). `book.json` now carries store metadata (title/author file-as sort
  keys, MARC `aut` role, language, 1943 date, subjects, English description,
  cover). `scripts/build_reading_epub.py` was extended to emit rich Dublin Core
  OPF metadata + a color cover (EPUB3 `cover-image` property, legacy
  `<meta name="cover">`, guide + landmark), formatted for Kindle and Apple Books.
- Survey (`scripts/survey.py --target 21000`): counts + full outline +
  proposed 13-batch plan (every batch <= 21,000 source chars, the commissioner's
  cap) in `out/SURVEY.md`.
- Skeleton EPUB built to `out/The Whistling Wind.epub`; `scripts/qa_epub.py`
  PASS (72 files, 66 documents, all links resolve). Fully navigable
  hyperlinked TOC, 0 of 60 chapters translated.

Checks run this step: JSON validity of book.json; numeral-mapping assertion
(ch01..ch58 == source 一..五十八); qa_epub PASS; OPF well-formedness + cover
wiring verified. No translation performed (Step 0 only).

## B01 = ch00 through ch08 (About the Author + Chapters 1 to 8) — DONE

Scope: units ch00..ch08, the front-matter "About the Author" bio plus the
novel's Chapters 1 to 8 (source headings 一..八), 18,512 source characters.
This covers the invitation puzzle, the narrator meeting Stephen (the American
naval surgeon), the introduction of Bai Ping, the all-night gambling / dawn Mass
sequence, the ring exchange, and Stephen's birthday party where Mei Yingzi and
Helen Manfield first appear.

Deliverables shipped this batch:
- Reading translations out/ch00_reading.md .. out/ch08_reading.md (generated
  from the aligned bilingual QC files via split_bilingual.py; the bilingual
  files are QC only and do not ship).
- 16 footnotes folded into notes.json (continuous numbering 1..16 across the
  batch, assigned by the builder in reading order).
- 33 new glossary rows in glossary.json (people, organizations, places, terms),
  each with status and attestation.
- figures.json unchanged (no in-text figures in these chapters; the colour
  cover is carried by book.json / the builder).
- Cumulative EPUB rebuilt to "out/The Whistling Wind.epub" (9 of 60 chapters
  translated; the other 51 still link to their skeleton outlines).

Checks run and results:
- check_numbers.py (with data/noise.txt) on every bilingual file: 0 unresolved
  across all 9 units (624 pairs total). A project noise file was started; a few
  built-in NOISE patterns (十分, 十[几]) were greedily eating the "十分/十几" out
  of 二十分钟 / 三点五十分 / 四十几, so a small ordered block for clock times and
  durations was added at the TOP of check_numbers.py NOISE (documented in the
  file). Project noise also strips 百合 (lily), 百乐门 (Paramount), 十字架
  (cross), 四围 (all around), 两个字, 五彩, 万种, 十二分, 星期X, decade labels,
  and the Route Lafayette house number.
- check_structure.py (config mode): paragraph parity OK on all 9 units;
  16 note anchors, 0 unresolved; heading shape uniform (1 distinct shape).
- qa_epub.py on the built EPUB: PASS (72 files, 66 documents, 16 note
  references / 16 bodies / 16 backlinks, all links resolve).
- Verbatim-quotation audit: a mechanical character-for-character comparison of
  every QC blockquote against data/src confirmed the source is quoted exactly
  and no sentence is dropped (all 9 units VERBATIM OK).
- Blind double translation (separate context) of the analytical/lyrical
  passages (the narrator's philosophy of the Solitary Island; the Mei Yingzi
  feeling-vs-will / sun-and-lamp exchange; the Narcissus / unrequited-love
  exchange; the dream sequence): converged with the shipped translation; no
  divergence pointing to an unresolved ambiguity. Independent readings of 孤岛,
  美感的距离, 纳虚仙子 and 鬼火 matched the choices made here.
- Round-trip back-translation (separate context) of three prose samples (the
  roulette run; the returned four thousand dollars; the "lamp is here" dream
  passage): every clause of the source was reproduced; no omission found.
- Random deep audit (~4%): the four double-translation passages plus the
  verbatim sweep gave the batch its paranoid treatment. Observed substantive
  error rate: 0 (no mistranslations or omissions found); the only source-level
  problems were the author/editor's own, handled as below.

Fact-checking (against Wikipedia / Baidu Baike / Chinese Wikipedia / academic
sources; no LLM-sourced references):
- The "About the Author" bio: birth 1908 Cixi, 1931 Peking University
  philosophy, 1937 Ghost Love, 1943 The Whistling Wind and the "Year of Xu Xu,"
  1944 USA, 1946 return, 1950 Hong Kong, 1956 River of Fury, died 1980 aged 72
  of lung cancer: all corroborated. (Scholarship adds a Sorbonne period
  1936-38 the bio omits; not a contradiction. The original name is given as
  徐傳琮 by Chinese sources.) River of Fury (江湖行) and Ghost Love (鬼恋) follow
  Frederik Green's usage.
- Shanghai geography (Route Lafayette, Bubbling Well Road, Medhurst Road,
  Yuyuan Road, Avenue Joffre, Avenue Haig, Route de Sieyès, Route Petain,
  Fourth Avenue / Foochow Road, Nanjing Road, Xujiahui / St Ignatius Cathedral,
  Renji Hospital): standard historical English names confirmed and used.
- The Solitary Island (孤岛, 1937 to Dec 1941) and its special status:
  corroborated. Shanghai Municipal Orchestra under Mario Paci, "finest in the
  Far East," Chinese premiere of Beethoven's Ninth (1936) with a large chorus
  (1939): corroborated; the novel's claim that the concert was moved to the
  evening because the chorus was not free by day is the narrator's own detail
  and is flagged as uncorroborated in the note.
- Hazlitt's Table-Talk (essay "On Living to One's-Self"), Debussy, Schelling,
  and Narcissus (纳虚仙子, an archaic transliteration): all confirmed.

Flagged for the read-through (things to keep an eye on):
- Source corruption at Chapter 5: 愿我用就有这样... , where 用就 looks like a
  slip for 永/永远 ("always"). Rendered to sense and footnoted (note 10), left
  visible per rule 4.
- Minor digitization glitches in the source rendered to their plain meaning and
  not footnoted: Chapter 7 仲出 for 伸出 ("held out"), 地 for 她 ("she"), and
  跳舞 written 髋舞 ("dance"); Chapter 8 请地 for 请她. Chapter 3 carries a
  dittography (也有也有); rendered once.
- Provisional renderings that a later attestation could improve: Helen's surname
  Manfield (曼斐儿), Dr. Philip (费利普 / 菲利浦, two source spellings), the
  Weibai Hotel (魏白饭店), the Bakou Apartments (芭口公寓), the Kaisha (凯莎),
  the Liti Cafe (立体咖啡馆), the Majestic Cinema (大华电影院). All are marked
  provisional in glossary.json.

## B02 = ch09 through ch14 (Chapters 9 to 14) — DONE

Scope: units ch09..ch14, the novel's Chapters 9 to 14 (source headings 九..十四),
19,469 source characters. Covers the evening at the Stephens' (Mrs. Stephen's
yellow drawing-room, the Municipal Orchestra concert where Helen reappears, the
Arcadia where the two Japanese officers Suzuki and Yamao join the party), the
all-night talk and Bai Ping's midnight visit (the sun/lamp exchange, Schumann's
Reverie), the four-day revelry, the Hangzhou trip (crossing the occupied North
Sichuan Road, the Geling climb and Mei Yingzi's warning about Bai Ping, the West
Lake boating), the narrator's flight home with Bai Ping on the train and his
resolve to change his life, and the tea-party where Helen sings, ending at Bai
Ping's silver apartment.

Deliverables shipped this batch:
- Reading translations out/ch09_reading.md .. out/ch14_reading.md (generated from
  the aligned bilingual QC files via split_bilingual.py; the bilingual files are
  QC only and do not ship).
- 12 footnotes folded into notes.json (continuous numbering 17..28 across the
  batch, assigned by the builder in reading order). Batch total now 28.
- 25 new glossary rows in glossary.json (people, org, places, one term); 63 rows
  total. New referents: Mario Paci (梅百器), Suzuki Jiro (铃木次郎), Yamao
  Motohara (山尾本原), Sophie (莎菲), Ah Mei (阿美), the cat Jimi (吉迷), Qi
  Baishi / Wu Changshuo / Ren Bonian, the National Academy of Art (国立艺术院),
  the Arcadia (阿卡第亚), the Xiangong (仙宫), Hangzhou, the Xiling Hotel
  (西冷饭店), the Golden Gate (金门), the Jinxiang (锦湘), North Sichuan Road,
  Route Massenet (马斯南路), Geling (葛岭), the Su and Bai Causeways, Solitary
  Hill (孤山), the Three Pools Mirroring the Moon, Niugong Mound (牛公墩,
  provisional), and cheongsam (旗袍, decided; matches B01 usage).
- figures.json unchanged (no in-text figures in these chapters).
- Cumulative EPUB rebuilt to "out/The Whistling Wind.epub" (15 of 60 chapters
  translated; the other 45 still link to their skeleton outlines).

Checks run and results:
- check_numbers.py (with data/noise.txt) on every bilingual file: 0 unresolved
  across all 6 units (671 pairs total). Two check-infrastructure fixes this
  batch, both in the same class B01 documented (a greedy idiom pattern eating a
  digit out of a compound number):
  * added a whole-hour clock pattern r"[...]+点[钟鐘]" to the TOP of
    check_numbers.py NOISE, so "十一点钟" (eleven o'clock) is stripped before the
    built-in "一点" (=a little) idiom orphans a 十 read as 10;
  * added a negative lookbehind to the two bare-一 measure-word patterns so
    "一个" is not stripped out of "十一个" (eleven) and does not orphan a 十=10.
  data/noise.txt gained: 梅百器 (Mario Paci; 百≠100), 零[星落乱] (零≠0), 四川
    (North Sichuan Road; 四≠4), and 四为 (a ch14 digitization slip for 因为; 四≠4).
- check_structure.py (config mode over the batch): paragraph parity OK on all 6
  units; 12 note anchors, 0 unresolved; heading shape uniform (1 distinct shape).
- qa_epub.py on the built EPUB: PASS (72 files, 66 documents, 28 note references /
  28 bodies / 28 backlinks, all links resolve).
- Verbatim-quotation audit: whitespace-stripped character-for-character
  comparison of every QC blockquote against data/src (stripping the BOM and the
  duplicated chapter-numeral heading lines) confirms the source is quoted exactly
  and no sentence is dropped (all 6 units VERBATIM OK).
- Blind double translation (separate context): the analytical/lyrical passages
  (ch12 the North Sichuan Road / countryside-nostalgia passage; ch13 the West
  Lake elegy; ch12 the money-cannot-buy-love / "political finesse" exchange;
  ch14 the silver-vs-white aesthetic exchange) converged with the shipped
  translation; no divergence pointing to an unresolved ambiguity.
- Round-trip back-translation (separate context) of the ch13 silver-room close:
  every clause reproduced; no omission. The blind pass flagged three phrases as
  possibly "added" (the emblem of / contending against the passing of time / a
  silver girl); all three are faithful to the source read against 银色竟象徵着…,
  在时间中与青春争胜, and 银色的女孩 respectively (the flags came of the auditor not
  holding the source for that sample).
- Random deep audit (~3.3%, the four double-translation passages plus the
  back-translation sample given the full paranoid treatment): observed
  substantive error rate 0 (no mistranslations or omissions found).

Fact-checking (against Wikipedia / Stanford's Paci exhibit / Baidu Baike /
China Academy of Art history; no LLM-sourced references):
- Mario Paci (梅百器 = Mei Baiqi, 1878–1946), conductor of the Shanghai Municipal
  Orchestra 1919–1942 and teacher of many early Chinese pianists: corroborated.
- The Arcadia (阿卡第亚) as a real Shanghai dance hall / cabaret of the period:
  corroborated. North Sichuan Road as the artery of Japanese-controlled Hongkou,
  with sentries at the crossings from the concessions after 1937: corroborated
  (explains why the narrator had not been there since the fall of the city, and
  the 仇货 = boycotted enemy goods on the hoardings).
- The National Academy of Art (国立艺术院), founded on the West Lake in 1928 by
  Cai Yuanpei, first president Lin Fengmian, opened at Solitary Hill and later
  evacuated to the interior: corroborated (grounds the narrator's scattered
  "Art Academy" friends and the 孤山 landmark). West Lake landmarks (Su/Bai
  Causeways, Solitary Hill, Three Pools Mirroring the Moon) and Geling (Ge Hong):
  standard, corroborated. Route Massenet = today's Sinan Road, named for Jules
  Massenet: corroborated.
- 黄锡包 ("yellow tin-foil pack"): the tinned BAT cigarettes were nicknamed in
  Shanghai by pack colour (white Capstan, green Three Castles, red Ruby Queen);
  the yellow pack was one of these premium tins, but the exact English brand it
  names is not certain, so the note says so and the prose renders it literally as
  "yellow-packet cigarettes."

Flagged for the read-through (things to keep an eye on):
- Minor source digitization glitches rendered to plain meaning and NOT footnoted:
  ch09 史蒂芬太大 for 史蒂芬太太 ("Mrs. Stephen"); ch10 百合除放 for 百合初放
  ("a lily just opening"), 低声点说 (stray 点); ch11 白萍 for 白苹 ("Bai Ping");
  ch12 使她自己年容易 (stray 年); ch14 大概四为 for 因为 ("because"). The Chapter 9
  reading-list slip 「Eicht」 for Fichte IS footnoted (note 17), as is the
  occupied-zone context (note 22), per rule 4.
- Provisional renderings a later attestation could improve: Yamao Motohara
  (山尾本原), the Xiangong (仙宫), the Jinxiang (锦湘), Niugong Mound (牛公墩,
  not securely identified), and the cat's name Jimi (吉迷). All marked provisional
  in glossary.json.
- Speaker attribution in a few tag-less source paragraphs was resolved to the
  only coherent reading (ch10 白苹's "是的" + the narrator's jealousy question in
  one paragraph; ch14 the two toasts). No content added beyond a "said"/"answered"
  tag to name the speaker.

## B03 = ch15 through ch17 (Chapters 15 to 17) — DONE

Scope: units ch15..ch17, the novel's Chapters 15 to 17 (source headings 十五..
十七), 16,230 source characters (ch15 is long, ~10,004; ch16/ch17 short). Covers
the evening at the Manfields' (Helen the "calm river"; her English-reared
household; her mother's hopes and the family history of a singing gift sacrificed
to love); the settled new life and its unravelling; Mrs. Manfield's alarm that
Helen means to give up music for philosophy; the moonlit drive to Jessfield Park
(the essay on smell and culture) and the water-lily meeting with Helen by the
pond (the "philosophy is the highest art" debate); the three-month pact with Mei
Yingzi; Helen's transformation at the September dinner-dance into a creature of
vanity (Mei Yingzi's "sorcery"); and the narrator's plan of escape — the feigned
trip home — undone when Bai Ping reveals she is secretly the landlord of the very
apartment he had rented to hide in, and asks him to move in with her.

Deliverables shipped this batch:
- Reading translations out/ch15_reading.md .. out/ch17_reading.md (generated from
  the aligned bilingual QC files via split_bilingual.py; the bilingual files are
  QC only and do not ship). A batch helper scripts/_zip_bilingual.py pairs the
  VERBATIM source paragraphs (copied from data/src, BOM + the two duplicated
  chapter-numeral heading lines stripped) with the authored English, so the
  source side of the QC file is never re-typed.
- 7 footnotes folded into notes.json (continuous numbering 29..35 across the
  batch, assigned by the builder in reading order). Batch total now 35.
- 5 new glossary rows in glossary.json (68 rows total): Jessfield Park (兆丰公园),
  Route Winling (汶林路), Route Prosper Paris (姚主教路), the DD's Café (弟弟咖啡店),
  and the poet Tao Yuanming (陶渊明).
- figures.json unchanged (no in-text figures in these chapters).
- Cumulative EPUB rebuilt to "out/The Whistling Wind.epub" (18 of 60 chapters
  translated; the other 42 still link to their skeleton outlines).

Checks run and results:
- check_numbers.py (with data/noise.txt) on every bilingual file: 0 unresolved
  across all 3 units (447 pairs total). Number-check noise additions this batch,
  each a NON-quantity numeral or a parser artifact (documented in data/noise.txt):
  两样 ("no different"; 两≠2), 十足 ("to the full"; 十≠10), 光芒万丈 (idiom of
  radiance; 万丈 not a count), and a numeral+丈 pattern [一二三四五六七八九十两]丈
  because 丈 (a unit of length ~3.3 m) is rendered to feet (一丈 -> "ten feet",
  二丈 -> "twenty feet"), so its numeral is unit-converted and cannot survive
  as-is. Also 四十二四十三: an unpunctuated speed range "42-43" (needle 始终在
  四十二四十三上) that the source numeral parser miscomputes as a single 83; the
  real 42/43 are rendered. The one English-parser limit ("three hundred and forty"
  parses to 3/40/300, not 340) was met by writing the rent figure "340 dollars a
  month" as digits, not by touching the script (per the B02 caution).
- check_structure.py (config mode over all 18 translated units): paragraph parity
  OK on every unit (ch15 233 | ch16 51 | ch17 163); 35 note anchors, 0 unresolved;
  heading shape uniform (1 distinct shape).
- qa_epub.py on the built EPUB: PASS (72 files, 66 documents, 35 note references /
  35 bodies / 35 backlinks, all links resolve).
- Verbatim-quotation audit: whitespace-stripped character-for-character comparison
  of every QC blockquote against data/src (BOM + duplicated heading lines removed)
  confirms the source is quoted exactly and no sentence is dropped — ch15 11,730 /
  ch16 3,359 / ch17 4,115 characters, all VERBATIM OK.
- Blind double translation (separate context, source only): the analytical/lyrical
  passages — the essay on smell and culture (ch15), the "philosophy is the highest
  art" debate (ch15), and the toothpaste/toothbrush vanity exchange (ch15) — all
  converged with the shipped translation; no divergence pointing to an unresolved
  ambiguity. Independent readings of 臆说 ("conjecture"), 宗教的婢女 ("handmaid of
  religion"), 科学的科学 ("science of sciences") and the toothpaste/toothbrush
  figure matched the choices made here. The blind pass surfaced one more source
  glitch (see below), 月色胶洁 for 皎洁 ("luminous/pure moonlight").
- Round-trip back-translation (separate context): the Bai-Ping-is-the-landlord
  reveal (the name-card passage) and the Tao Yuanming / silver-room close (ch17):
  the back-translation mapped one-to-one onto the source — no content in the
  English absent from the source (no inventions), and no source content dropped.
  The only flags were sub-lexical nuance (the emphatic 就是 in "我就是你的房东",
  the elided 还), not additions or omissions.
- Random deep audit (~4%, the double-translation and back-translation passages
  given the full paranoid treatment plus the verbatim sweep): observed substantive
  error rate 0 (no mistranslations or omissions found); the only source-level
  problems were the digitization glitches below, rendered to plain sense.

Fact-checking (against Wikipedia / Historical Photographs of China / Baidu Baike /
Shanghai French-Concession road histories; no LLM-sourced references):
- Jessfield Park (兆丰公园): a large public garden in the west of the International
  Settlement, laid out by the Shanghai Municipal Council in 1914, renamed Zhongshan
  Park in 1941 for Sun Yat-sen; the novel keeps the older concession-era name.
  Corroborated.
- DD's Café (弟弟咖啡店 = 弟弟, "little brother" = DD's): a fashionable café on
  Avenue Joffre in the French Concession, resort of stage and screen people.
  Corroborated.
- Route Prosper Paris (姚主教路, today Tianping Road), named for the French Jesuit
  bishop Prosper Paris (Chinese name 姚宗李, Yao Zongli); Route Winling (汶林路,
  today Wanping Road), named for J. A. Winling: both corroborated concession
  road-names. The Jewish restaurant at the Winling/Joffre corner is footnoted to
  Shanghai's wartime Central-European Jewish refugee community (city required no
  visa from 1938): corroborated at the general level.
- Tao Yuanming (陶渊明 / Tao Qian, 365-427), the archetypal poet of reclusion:
  standard, corroborated. "Philosophy is the handmaid of religion" footnoted to
  the scholastic tag philosophia ancilla theologiae; Richard Wagner (1813-1883)
  footnoted like the earlier Debussy/Schubert composer notes.

Flagged for the read-through (things to keep an eye on):
- Minor source digitization glitches rendered to plain meaning and NOT footnoted:
  ch15 音东 for 音乐 ("music"), 月色胶洁 for 皎洁 ("luminous/pure moonlight"),
  双叠的下频 for 下颏 ("double chin"), 残校 for 残枝 ("withered stalks"), 自台布 for
  白台布 ("white cloth"), 罪衍 for 罪愆 ("sin"); ch17 到了两杯茶 for 倒了两杯茶
  ("poured two cups of tea"). Genuine reference/
  reading matter is footnoted instead (Jessfield Park, the Jewish refugees, the
  scholastic tag; Wagner; Tao Yuanming, Route Prosper Paris, DD's Café).
- Two-speakers-in-one-paragraph kept as single source paragraphs (parity): ch15
  Mei Yingzi's "Thank you" + the narrator's "Have you really come specially…"
  (tagged "I asked"); ch17 the narrator's "I've rented a room…" + Bai Ping's "When
  do you mean to move in?" No content added beyond the minimum speaker tag.
- The pronoun in ch15's "could it be true that her feeling for me was something
  more than friendship" reads Helen (the antecedent is Mei Yingzi's report that
  Helen loves a man), and is kept as "her" so the ambiguity the narrator himself
  feels is preserved.
- Provisional/attested renderings a later attestation could sharpen: Route Winling
  and Route Prosper Paris are given their concession English names; the DD's Café
  is attested. All other names reuse the fixed glossary forms (Helen, Mrs.
  Manfield, Mei Yingzi, Bai Ping, Stephen, Professor Paci, the Paramount, Hangzhou,
  Xujiahui, cheongsam).

## Batch B04 (ch18 through ch21: Chapters 18 to 21) — DONE

Scope: units ch18, ch19, ch20, ch21 (source 22_chapter20.txt through
25_chapter23.txt; heads 十八/十九/二十/二十一), ~19,962 source characters. The
narrator moves into Bai Ping's Route Prosper Paris flat; Bai Ping is shot and
wounded outside the Paramount; Mei Yingzi descends on the flat and blesses the
supposed couple; the narrator moves back home and drifts from Bai Ping; the
Pacific war breaks out (Dec 1941); Stephen is interned, Helen sings from the
soul, the narrator lends money to Mrs. Manfield; and Mrs. Stephen swears the
narrator to secrecy and recruits him into American naval intelligence.

Deliverables:
- out/ch18_reading.md (209 paras), ch19 (126), ch20 (180), ch21 (96); one clean
  English paragraph per source paragraph, book's own first-person voice.
- Bilingual QC files out/chNN_bilingual.md authored via scripts/_zip_bilingual.py
  (source side copied VERBATIM from data/src, never re-typed) and split with
  scripts/split_bilingual.py; parity source in data/zh/chNN.txt.
- 8 new footnotes into notes.json (numbering continuous, assigned by the builder
  in reading order). Batch total now 43.
- 8 new glossary rows in glossary.json (76 rows total): Wu Zetian (武则天), the
  Western Empress Dowager = Cixi (西太后), Miyama Toshimi (宫间登水, tentative),
  Tianjin (天津), Pudong (浦东), the Zhongxi Sanatorium (中西疗养院), the Palace of
  the Moon (月宫), and the drink Kolisa (寇莉莎).
- figures.json unchanged (no in-text figures in these chapters).
- Cumulative EPUB rebuilt to "out/The Whistling Wind.epub" (22 of 60 chapters
  translated; the other 38 still link to their skeleton outlines).

Checks run and results:
- check_numbers.py (with data/noise.txt) on every bilingual file: 0 unresolved
  across all 4 units (611 pairs total). Two classes of fix this batch:
  (a) data/noise.txt additions, each a NON-quantity numeral or parser artifact:
  二房东 ("sublandlady"; 二 not a count), 飘零 ("drift/fall"; 零 not 0), 二○号
  (Renji ward No. 20, written 二 + circle-zero U+25CB, which the parser cannot
  join, orphaning a bare 二 read as 2 while "twenty" is rendered), [一二三四五]更
  (night-watches; 四更 = "the small hours"), 六角 ("hexagonal"; 六 not a count),
  大千世界 (Buddhist idiom; 千 not 1000).
  (b) a principled check_numbers.py bug-fix, NOT a script hack: the two idiom
  patterns r"[一不][旦時时般點点些]" and r"一[...日夜時时...]" lacked the negative
  lookbehind their sibling measure-word patterns already carry, so they ate the
  一 out of a COMPOUND number - 十一日 ("the 11th") and 十一时半 ("half past
  eleven") - and orphaned a 十 read as 10. Added the same
  (?<![零一二两兩三四五六七八九十百千万萬億]) lookbehind to both, and "eleventh":11
  to WORD_NUM. Verified strictly monotonic/safe: rebuilt pseudo-bilingual pairs
  for ALL prior chapters ch00-ch17 from data/zh + out/*_reading.md and re-ran
  the new checker: 0 flags, no regression (the change can only PRESERVE a
  compound number previously mangled, never orphan a new one). Direct spot
  checks: 十一时半 -> 11, 十一日 -> 11, 两点半 -> 2, 一点 -> stripped,
  十一点钟 -> stripped (B02 case unaffected).
- check_structure.py (config over all 22 translated units ch00-ch21): paragraph
  parity OK on every unit (ch18 209 | ch19 126 | ch20 180 | ch21 96); 43 note
  anchors, 0 unresolved; heading shape uniform (1 distinct shape); glossary
  drift 0 (variants guard: Mei Yingzi, Bai Ping, cheongsam, the Paramount,
  Mrs. Stephen, Mrs. Manfield).
- qa_epub.py on the built EPUB: PASS (72 files, 66 documents, 43 note references /
  43 bodies / 43 backlinks, all links resolve).
- Verbatim-quotation audit: whitespace-stripped character-for-character
  comparison of every QC blockquote against data/src (BOM + duplicated heading
  lines removed) confirms the source is quoted exactly and no sentence is
  dropped - ch18 9,045 / ch19 4,917 / ch20 6,194 / ch21 3,610 characters, all
  VERBATIM OK.
- Blind double translation (source only, re-derived independently): the
  analytical/lyrical passages all converged with the shipped text - Mei Yingzi's
  youth-belongs-to-society monologue and her Wu Zetian / Western Empress Dowager
  aside (ch18); the desolate-night "wave behind drives on the wave ahead"
  meditation (ch18); Helen singing "from the soul," the wounded bird-of-prey
  figure (ch20); and the closing crystalline light-vision "all that radiance was
  laughter" (ch21). No divergence pointing to an unresolved ambiguity.
- Round-trip back-translation (omission check): the Pacific-war opening and the
  gunboat news (ch20), and Mrs. Stephen's Bible oath and recruitment questions
  (ch21), mapped one-to-one onto the source - no English content absent from the
  source (no inventions), no source content dropped.
- Random deep audit (~4%, ~24 paragraphs given the full paranoid treatment plus
  the verbatim sweep): observed substantive error rate 0 (no mistranslations or
  omissions found); the only source-level problems were the digitization
  glitches below, each rendered to plain sense.

Fact-checking (against Wikipedia / Baidu Baike / standard reference; no
LLM-sourced references):
- December 7-8, 1941 / outbreak of the Pacific war: the Shanghai action was the
  sinking of the British gunboat HMS Peterel (crew refused to surrender and
  largely died) and the capture of the American gunboat USS Wake in the Huangpu
  on the morning of Dec 8 (Shanghai time; Dec 7 Hawaii time). Corroborated; the
  novel's "night of Dec 7" fits the local experience across the date-line.
- Wu Zetian (624-705), sole reigning female emperor of the Tang; the Western
  Empress Dowager = Cixi (1835-1908) of the late Qing. Corroborated.
- Pudong internment: after Pearl Harbor Japan interned Allied service-members
  (Woosung, Kiangwan) and, from 1943, civilians (the Pootung/Pudong Civil
  Assembly Centre). The novel places Stephen "on the Pudong side." Corroborated
  in outline; the note does not overclaim which specific camp held him.
- The July 7 (七七) Incident = Marco Polo Bridge (Lugou Bridge) Incident of
  July 7, 1937, opening the full-scale War of Resistance. Corroborated.
- Zhongxi Sanatorium (中西疗养院) and the drink 寇莉莎 (Kolisa) not securely
  identified in outside sources; rendered provisionally and flagged.

Flagged for the read-through (things to keep an eye on):
- Minor source digitization glitches rendered to plain meaning and NOT footnoted
  (no genuine reading uncertainty): ch18 写上就去 for 马上就去 ("go at once"),
  没辱 for 玷辱/污辱 ("sully" your standing); ch19 梅赢子 for 梅瀛子 (Mei Yingzi;
  赢 for 瀛); ch20 照顾飞那麽 with a spurious 飞 (read 照顾, "looked after"); ch21
  蒂芬太太 for 史蒂芬太太 (Mrs. Stephen; dropped 史), 浮起丁 for 浮起了 ("a strange
  feeling rose"; 丁 for 了). Genuine reading uncertainty is footnoted instead
  (the admirer's name Miyama Toshimi, ch19).
- Two-speakers-in-one-paragraph kept as single source paragraphs (parity): ch18
  Mei Yingzi's "you have lived together a long while..." + the narrator's "It is
  an insult to us!"; and her "Do you know how Helen thinks of you?" + the
  narrator's "Helen?". No content added beyond the minimum.
- Recurring subjects NOT re-noted (already noted at first appearance in
  B01-B03): Stephen, Bai Ping, Mei Yingzi, Helen, Mrs. Manfield, Mrs. Stephen,
  the Solitary Island, the Paramount, Renji Hospital, Jessfield Park, the DD's
  Café, Route Prosper Paris, Professor Paci, Dr. Philip, the narrator's name Xu,
  the cheongsam. New footnotes only for genuinely new material.
- Provisional renderings a later attestation could sharpen: Miyama Toshimi
  (宫间登水), the Zhongxi Sanatorium (中西疗养院), Kolisa (寇莉莎). All other names
  reuse the fixed glossary forms.

## Batch B05 (ch22 through ch25: Chapters 22 to 25) — DONE

Scope: units ch22, ch23, ch24, ch25 (source 26_chapter24.txt through
29_chapter27.txt; heads 二十二/二十三/二十四/二十五), ~18,788 source characters.
The narrator visits Dr. Philip's clinic and is met by Mei Yingzi, who drives him
to the Benner Inn and commissions his first mission: to steal a wax-sealed
Japanese Navy Ministry document from Bai Ping's flat. He finds it inside a copy
of Faust, takes it while pretending to court Bai Ping, quarrels with her, hands
it to Mei Yingzi at the Standford gambling-club, gambles till dawn, and slips it
back the next morning. He then sinks into Bai Ping's collaborationist social
round; at a gambling night in Colonel Arita's requisitioned Hongkou house he and
Bai Ping rescue Helen, now transformed and in the hands of Major Yamao.

Deliverables:
- out/ch22_reading.md (108 paras), ch23 (157), ch24 (153), ch25 (70); one clean
  English paragraph per source paragraph, in the book's own first-person voice.
- Bilingual QC files out/chNN_bilingual.md authored via scripts/_zip_bilingual.py
  (source side copied VERBATIM from data/src, never re-typed) and split with
  scripts/split_bilingual.py; parity source in data/zh/chNN.txt. Verbatim
  parity confirmed by the whitespace-stripped char comparison of the joined '>'
  blockquotes vs the joined source paragraphs (ch22 4422 | ch23 7454 |
  ch24 5289 | ch25 5059 chars; all MATCH).
- 7 new footnotes into notes.json (numbering continuous, assigned by the builder
  in reading order). Book total now 50. New notes: Sai Jinhua, the Fuyuan native
  bank, the Sarofan (ch22); the Shitao landscape, Ren Jinshu (ch23); Japanese
  notes and national currency, Hongkou (ch25). ch24 adds no new footnote (its
  references — the roulette den, the neon "Standford" — are self-explanatory and
  the recurring cast/places are already noted at first appearance).
- 15 new glossary rows in glossary.json (84 rows total). People: Sai Jinhua
  (赛金花), Shitao (石涛), Ren Jinshu (任堇, emended from the source's 任董叔),
  Honsa Jiro (本佐次郎, tentative), Arita (有田), Takeshima (武岛), Yamao (山尾,
  the surname of Major Yamao 山尾少佐). Organizations: the Fuyuan native bank
  (福源钱庄). Places: Great Western Road (大西路), Columbia Road (哥伦比亚路),
  Scott Road (施高塔路), Hongkou (虹口), the Benner Inn (槟纳饭店), the Sarofan
  (赛罗凡, unidentified), the Standford (the neon club off Columbia Road).
- figures.json unchanged (no in-text figures in these chapters).
- Cumulative EPUB rebuilt to "out/The Whistling Wind.epub" (26 of 60 chapters
  translated; the other 34 still link to their skeleton outlines).

Checks run and results:
- check_numbers.py (with data/noise.txt) on every bilingual file: 0 unresolved
  across all 4 units (488 pairs total). Fixes this batch:
  (a) two real quantities rendered so they survive: 十来张桌子 = "about ten
  tables" (was "a dozen" = 12, corrected to "ten"); 二十四开 = the 24-mo paper
  size, written "a twenty-four-mo sheet" so the parser reads 24 (a hyphen-joined
  "twenty-fourmo" parsed only to 20).
  (b) data/noise.txt additions, each a NON-quantity numeral: 两[手膝] (两手 "both
  hands", 两膝 "both knees"; 两 not a count), 连三接四 (idiom "one after another";
  三/四 not counts), 零碎 ("odd/sundry tasks"; 零 not 0, cf. the existing 零星/
  零落/零乱 entry).
  (c) one idiom the built-in measure rule half-eats: 一次两次 ("time and again")
  — the generic 一+measure pattern strips "一次" and orphans the 两, so rather
  than mask a real "twice" globally with a noise line, the English was reworded
  to carry the count ("taking care a time or two"). No script edit; verified 0
  regressions on the prior chapters' checks.
- check_structure.py (config scratch/b05_check.json over the 4 batch units):
  paragraph parity OK on every unit (ch22 108 | ch23 157 | ch24 153 | ch25 70);
  7 note anchors, 0 unresolved; heading shape uniform (1 distinct shape);
  glossary drift 0 (variants guard: Bai Ping, Mei Yingzi, Ah Mei, Jessfield
  Park, the Benner Inn, Great Western Road, Yamao, Dr. Philip).
- qa_epub.py on the built EPUB: PASS (72 files, 66 documents, 50 note references /
  50 bodies / 50 backlinks, all links resolve).
- Blind double translation on the analytical/lyrical passages (ch23 the four
  kinds of imagination; ch24 "life is the intoxication of gambling"; ch25 the
  tiger-tamer / unfading-flower simile) and sampled on the plain narration: no
  substantive divergence; the only judgement call is 说明的想像 rendered
  "interpretive imagination" (vs "expository"), kept consistent.
- Round-trip back-translation as an omission check on the long paragraphs
  (ch23 the search of the flat and the finding of the document; ch24 the
  remorse-and-return paragraph; ch25 Helen's tangled emotions and the
  tiger-tamer paragraph): every source clause accounted for; no dropped
  sentence or list-item.
- Random deep audit (~4%, verbatim quote + double + back-translation): ch22
  para on the envelope's description (二十四开报纸大小…火漆的印子), ch23 para on
  drawing Faust from the shelf (…夹着的页码是八十三页…), ch25 para on the
  robe-and-cap reasoning (山尾穿着人的衣裳…). Observed error rate 0 material
  errors; one rendering polished after audit (衣冠 "robe and cap", not the
  academic-sounding "cap and gown").

Fact-checking (against Wikipedia / Baidu Baike / standard reference; no
LLM-sourced references):
- Sai Jinhua (赛金花, c. 1872–1936), the late-Qing courtesan linked in legend to
  Field Marshal von Waldersee during the Boxer occupation of Beijing (1900).
  Corroborated. "Bai Ping is a true Sai Jinhua" = a beauty who consorts with the
  occupier, half collaborator, half secret protector.
- Shitao (石涛, 1642–c. 1707), early-Qing monk-landscapist of the fallen Ming
  house. Corroborated.
- Shanghai roads: 大西路 = Great Western Road (today part of Yan'an West Road);
  哥伦比亚路 = Columbia Road (today Panyu Road); 施高塔路 = Scott Road (today
  Shanyin Road), in Hongkou. All corroborated.
- 虹口 (Hongkou), the district north of Suzhou Creek that was the heart of
  Japanese Shanghai, where the occupying officers are billeted. Corroborated.
- Dual currency (ch25 "Japanese notes and national currency"): occupied Shanghai
  ran several currencies at once — the Nationalist fabi (法币), Japanese military
  notes, and later puppet-regime scrip. Corroborated in outline.

Flagged for the read-through (things to keep an eye on):
- Minor source digitization glitches rendered to plain meaning and NOT footnoted
  (no genuine reading uncertainty): ch22 在字 for 名字 ("the name the nurse
  called"); ch23 戒者 for 或者 ("or else"), 厨门 for 橱门 ("the wardrobe door"),
  "在一封是日文的" for "有一封是日文的" ("one of them in Japanese"), 掷踢 for
  踯躅 ("paced about the room"), 不造 for 不自然 ("my posture very awkward");
  ch25 "同我内行" for "同我(内地)行" ("come inland with me").
- Genuine reading/identification uncertainty IS footnoted, not smoothed: 任堇
  (source prints the corrupt 任董叔; ch23), and 赛罗凡 "the Sarofan" (a Western
  restaurant name not identified with certainty; ch22).
- 山尾少佐 (Major Yamao, ch25) is rendered with the same surname form as the
  earlier 山尾本原 "Yamao Motohara" (a colonel), but the source does not make
  clear whether the two are the same man; noted in the glossary row, not
  asserted in the prose.
- Two-speakers-in-one-paragraph kept as single source paragraphs (parity): ch23
  "Ah Mei smiled." + the narrator's question; ch23 her "Do you want anything?" +
  the narrator's "No." No content added beyond the minimum.
- Recurring subjects NOT re-noted (already noted at first appearance in
  B01-B04): Stephen, Bai Ping, Mei Yingzi, Helen, Dr. Philip, the Paramount,
  Jessfield Park, Route Prosper Paris, Avenue Joffre, Avenue Haig, Bubbling Well
  Road, North Sichuan Road, the cheongsam, the narrator's name Xu. New footnotes
  only for genuinely new material.
- Provisional renderings a later attestation could sharpen: Honsa Jiro
  (本佐次郎), the Sarofan (赛罗凡), the Standford (standford), the Fuyuan native
  bank (福源钱庄). All other names reuse the fixed glossary forms.

## Batch B06 (ch26 through ch31: Chapters 26 to 31) — DONE

Scope: units ch26, ch27, ch28, ch29, ch30, ch31 (source 30_chapter28.txt through
35_chapter33.txt; heads 二十六..三十一), ~20,716 source characters. The night drive
home from Colonel Arita's, Helen's questioning at Bai Ping's flat about the Hailin
radio job, and the narrator's move into hiding on Weihaiwei Road under the alias
Chen Ji; Mei Yingzi's rose-bearing visit and the long argument over her using the
innocent Helen ("for victory"); the transformed Manfield household and Helen's wish
to quit; Stephen's release on bail and his death at the Gaolang Hospital, and the
narrator's realization that "Stephen and his wife" were never truly married but a
work-cover; the funeral at the International Cemetery and Helen's dawn vigil, her
shame and return to her natural self (giving up the social round and her post); Mei
Yingzi's fury at losing Helen and the reconciliation, and Helen's refusal then
consent to attend Rear Admiral Umetake's Christmas party "for you"; and Mei Yingzi's
strange night out (the Yuanyutai tavern, a dance hall behind the Great World) with
its premonition of tomorrow's dangerous mission and the tenths-odds exchange.

Deliverables:
- out/ch26_reading.md (141 paras), ch27 (111), ch28 (77), ch29 (89), ch30 (109),
  ch31 (96); one clean English paragraph per source paragraph, in the book's own
  first-person voice. ch30 carries the source's lone "──" divider as a lone "—".
- Bilingual QC files out/chNN_bilingual.md authored via scripts/_zip_bilingual.py
  (source side copied VERBATIM from data/src, never re-typed) and split with
  scripts/split_bilingual.py; parity source in data/zh/chNN.txt. Verbatim parity
  confirmed by the whitespace-stripped char comparison of the joined '>' blockquotes
  vs the joined source paragraphs (ch26 5242 | ch27 4032 | ch28 3760 | ch29 4003 |
  ch30 3834 | ch31 3677 chars; all MATCH).
- 6 new footnotes into notes.json (numbering continuous, assigned by the builder in
  reading order). Book total now 56. New notes: the Hailin Broadcasting Station and
  the alias Chen Ji (ch26); the International Cemetery and Isadora Duncan (ch29); the
  proverb "true gold fears no fire" (ch30); the Great World (ch31). ch27 and ch28 add
  no new footnote (their references are the already-noted recurring cast and places).
- 16 new glossary rows in glossary.json (100 rows total). People: Nomura (野村),
  Umetake (梅武少将, Rear Admiral; tentative Japanese reading), Chen Ji (陈寂, the
  narrator's alias), Dr. Gaolang (高朗). Organizations: the Hailin Broadcasting
  Station (海邻广播电台). Places: Weihaiwei Road (威海卫路), the Racecourse (跑马厅),
  the International Cemetery (万国公墓), Jing'an Temple (静安寺), Malang Road (马浪路),
  Beiping (北平), the Huimei Hotel (汇美饭店), Gaoye Road (高叶路), the Gaolang
  Hospital (高朗医院), the Yuanyutai (源裕泰), the Great World (大世界).
- figures.json unchanged (no in-text figures in these chapters).
- Cumulative EPUB rebuilt to "out/The Whistling Wind.epub" (32 of 60 chapters
  translated; the other 28 still link to their skeleton outlines).

Checks run and results:
- check_numbers.py (with data/noise.txt) on every bilingual file: 0 unresolved
  across all 6 units (623 pairs total). Fixes this batch:
  (a) one principled check_numbers.py NOISE addition (NOT a script hack), in the same
  class B01-B04 documented (a greedy short pattern eating a compound): the built-in
  r"[十几幾]多" ate the "十多" out of 五十多 ("fifty-odd") and orphaned a 五 read as 5
  (ch28, 五十多岁 "a pastor of fifty-odd"). Added r"[一二三四五六七八九]十多" at the TOP
  block, mirroring the existing 四十几 line; an approximate tens is not a money/count/
  year quantity, so stripping it whole is safe. Verified no collision: grep of all
  prior parity (ch00-ch25) shows no [数]十多 token, so no regression.
  (b) data/noise.txt additions, each a NON-quantity numeral or reduplicated idiom:
  万物 ("all things"; 万 not 10000, ch29), 两两三三 ("in twos and threes"; not counts,
  ch26), 畸零 ("odd/isolated"; 零 not 0, ch26 畸零而落寞的人), 万国 (万国公墓 "Cemetery
  of All Nations"; 万 not 10000, ch29).
  (c) one prose fix rather than a global mask: ch29 "只有在你我两人的时候" (两人 = 2)
  reworded to "Only when it is just the two of us" so the count survives. The tenths
  odds in ch31 (十分之十/十分之三/十分之六/十分之七/十分之九) are stripped by the
  built-in fraction pattern and rendered faithfully in the prose ("ten in ten",
  "three in ten", etc.); the check does not re-verify fractions, as before.
- check_structure.py (config scratch/b06_check.json over all 32 translated units
  ch00-ch31): paragraph parity OK on every unit (ch26 141 | ch27 111 | ch28 77 |
  ch29 89 | ch30 109 | ch31 96); 56 note anchors, 0 unresolved; heading shape uniform
  (1 distinct shape); glossary drift 0 (variants guard: Mei Yingzi, Bai Ping,
  cheongsam, Mrs. Stephen, Mrs. Manfield, Ah Mei, Jessfield Park, Scott Road, the
  Benner Inn, the Great World, the Racecourse, Chen Ji, the International Cemetery).
- qa_epub.py on the built EPUB: PASS (72 files, 66 documents, 56 note references /
  56 bodies / 56 backlinks, all links resolve).
- Blind double translation (separate context, source only) of the analytical/lyrical
  passages — Mei Yingzi's "for victory" sacrifice speech and the demon/graveyard
  vision (ch26); the remembered-song passage (ch27); the smile-and-film exchange and
  the Madonna/cherubs reflection (ch29); the tenths-odds and "only by dying now"
  exchange (ch31) — all converged with the shipped translation; no divergence
  pointing to an unresolved ambiguity (independent readings of 毒菌 "poison-toadstools/
  fungi", 圣画里玛丽亚 "the Madonna in sacred paintings", and the tenths odds matched).
- Round-trip back-translation (separate context, omission check): Stephen's deathbed
  description and the "smoke-screen" realization (ch28), the welling-feeling
  reconciliation paragraph (ch30), and the "true gold fears no fire" exchange (ch30)
  mapped one-to-one onto the source — no English content absent from the source (no
  inventions), no source content dropped.
- Random deep audit (~4%, the eight double-/back-translation passages plus a manual
  clause-by-clause audit of the long ch28 reasoning paragraph, 我从这银色的房中出来…):
  observed substantive error rate 0 (no mistranslations or omissions); the only
  source-level problems were the digitization glitches below, each rendered to sense.

Fact-checking (against Wikipedia / Baidu Baike / Britannica / Historic Shanghai /
concession road histories / RadioHeritage; no LLM-sourced references — a Grokipedia
hit that surfaced in one search was explicitly discarded):
- 万国公墓 (the International Cemetery): the Shanghai "Cemetery of All Nations," open to
  Chinese and foreigners alike, founded 1909 on Hongqiao Road in the western outskirts
  (part later became the Soong Ching-ling Mausoleum). Corroborated; "the International
  Cemetery" is the conventional English name.
- 跑马厅 (the Racecourse): the Shanghai Race Club's course opened 1862 in the middle of
  the International Settlement, on the site of today's People's Square / People's Park;
  racing ran to 1949. Corroborated.
- 威海卫路 (Weihaiwei Road): built 1913 in the International Settlement; shortened to
  威海路 (Weihai Road) only in the 1960s, so 威海卫路 is correct for the 1943 setting.
  Corroborated.
- 大世界 (the Great World): the many-storeyed amusement palace opened 14 July 1917 by
  Huang Chujiu at the French-Concession edge (Avenue Edward VII / Yu Ya Ching Road),
  famous for its distorting mirrors. Corroborated; "the Great World" standard.
- 马浪路 (Malang Road): officially the Rue Brenier de Montmorand (named 1906 for the
  French consul-general Brenier; today Madang Road), universally shortened by residents
  to 马浪路. The source uses the colloquial short form, kept here as "Malang Road" with
  the official name recorded in the glossary. Corroborated.
- Isadora Duncan (1877–1927): American pioneer of modern/free dance who broke from
  classical ballet's fixed vocabulary — aptly invoked for Helen's return to a natural
  bearing. Corroborated.
- Japanese-controlled English-language radio in occupied Shanghai: after Pearl Harbor
  the Japanese took over the settlement station XMHA (kept as an English-language Axis
  propaganda outlet, "The Call of the Orient") and the Axis German-owned XGRS carried
  English programming — so a Japanese-controlled English-language station is well
  grounded for the fictional Hailin. Corroborated in outline (the fictional 海邻 is
  not itself identified).

Flagged for the read-through (things to keep an eye on):
- Minor source digitization glitches rendered to plain meaning and NOT footnoted (no
  genuine reading uncertainty): ch28/ch29 短髦 (for 短髭, "stubble"), used consistently;
  ch28 "她对於我们两方面的背境" — 她 for 他 (Stephen; rendered "his reading"); ch30
  "从透亮的房手过来" — 房手 for 房间 ("coming from the bright room").
- Genuine references ARE footnoted, not smoothed (the Hailin station and the alias
  Chen Ji; the International Cemetery; Isadora Duncan; the proverb "true gold fears no
  fire"; the Great World).
- Recurring phrase 铁青的面颊 (Stephen's dead cheek, recurring ch28/ch29/ch31) rendered
  "iron-gray cheek" throughout for consistency (铁青 is properly "livid/ashen"; the
  softer "iron-gray" is kept as the single fixed rendering).
- Two-speakers-in-one-paragraph kept as single source paragraphs (parity): ch26
  Helen's "If it hadn't been for you..." + her changed-tone "Bai Ping, I shall be
  grateful..."; ch27 the maid's announcement lines. No content added beyond the
  minimum.
- Provisional renderings a later attestation could sharpen: Umetake (梅武), Dr. Gaolang
  (高朗) and the Gaolang Hospital, Gaoye Road (高叶路), the Huimei Hotel (汇美饭店), the
  Yuanyutai (源裕泰), the Hailin Broadcasting Station (海邻广播电台). All recurring names
  reuse the fixed glossary forms.

## Batch B07 (ch32 through ch36: Chapters 32 to 36) — DONE

Scope: the Christmas-Eve climax. Helen's farewell letter and her flight to Nanjing
(ch32); the arrival at Rear Admiral Umetake's requisitioned residence in Jiangwan and
Bai Ping crowned "president" of the revels (ch33); the cake, the gambling upstairs, and
the narrator's watch on the moonless garden (ch34); Bai Ping crowned "Queen," and Mei
Yingzi handing the narrator the packet he fears is poison (ch35); the vomiting that
clears him, the theft of the two sealed documents from Bai Ping's handbag on the drive
home, and the escape to the Standford at dawn on the Christmas Eve of 1941 (ch36).
Source: 18,411 chars across 36_chapter34.txt through 40_chapter38.txt.

Deliverables this batch:
- out/ch32_reading.md through out/ch36_reading.md (the correction surface).
- out/ch32_bilingual.md through out/ch36_bilingual.md (QC only, never shipped),
  authored via scripts/_zip_bilingual.py so the source side is copied verbatim.
- data/zh/ch32.txt through data/zh/ch36.txt (parity source, from split_bilingual.py).
- notes.json: 4 new footnotes (56 to 60). notes 57 to 58 in ch33, notes 59 to 60 in ch35.
- glossary.json: 5 new rows (100 to 105): Miko (person), Jiangwan, the Kaidi Restaurant,
  the White Palace (places), Greater East Asia (term).
- data/noise.txt: 4 new entries (凋零, 四顾, 万岁, 百般).
- scripts/check_numbers.py: WORD_NUM gained "twentieth" (20) and "twenty-third" (23),
  both day-of-month / century ordinals the tens-ones matcher does not reach (same
  mechanism as the earlier "eleventh"/"seventeenth" additions); and 两/兩 were added to
  the top clock-time and duration char classes (see the number-check note below).
- out/The Whistling Wind.epub rebuilt: 37 of 60 chapters translated (ch00 to ch36), the
  other 23 still linking their skeleton outlines; TOC fully navigable.

Checks run and results:
- Verbatim source parity (whitespace-stripped char comparison of the joined '>'
  blockquotes vs the joined source paragraphs): ch32 4268=4268, ch33 4654=4654,
  ch34 4068=4068, ch35 4343=4343, ch36 3857=3857. All MATCH (source copied, not retyped).
- Paragraph parity (check_structure.py --config): ch32 80|80, ch33 63|63, ch34 58|58,
  ch35 105|105, ch36 63|63. All OK. Note anchors: 4 notes, 0 unresolved. Headings:
  1 shape. Glossary drift: 0. ALL STRUCTURAL CHECKS PASS.
- Number check (check_numbers.py --noise data/noise.txt): all five green (80/63/58/105/63
  pairs, 0 unresolved) after the noise and script fixes below.
- Blind double translation (analytical/lyrical passages, re-rendered in a separate pass
  and diffed): ch32 Mei Yingzi's "organization, an organism, a single life" speech and
  the "eyes fail, the hands must shoulder the peril" figure; ch35 the snob's-heart
  opening (人心也许就是势利的...) and the Lady-of-the-Camellias desolation paragraph;
  ch36 the "fish leaps from the land into the water" release passage. Divergences were
  only word choice; sense and completeness identical.
- Round-trip back-translation (fresh context, omission check): ch32 Helen's letter
  (paras 0 to 11), ch35 opening (para 0) and the poison/hand passage (para 85), ch36 the
  handbag search (para 4) and the tiller-by-turns close (para 58). Each mapped
  one-to-one onto the source: no English content absent from the source (no inventions),
  no source content dropped.
- Random deep audit (~4%, roughly 13 of ~369 paragraphs given the full paranoid
  treatment: the double-/back-translation passages above plus a clause-by-clause audit
  of the two densest survey/search paragraphs, ch34 para 53 (the garden circuit, 石阶
  一二三四五六...) and ch36 para 5 (the mirror-chain-zipper search): observed substantive
  error rate 0 (no mistranslations, no omissions). The only source-level problems were
  the digitization glitches listed below, each rendered to plain sense.

Number-check notes (what was flagged and why it is noise / a fix, not a real drop):
- 凋零 ("wither and fall," of flowers, ch32) the 零 is not the quantity 0; added to noise.
- 四顾 ("look all around," 她没有四顾, ch34) the 四 is not the count 4; added to noise.
- 万岁 ("long live / banzai," 我们的Queen万岁, ch35) the 万 is not 10000; added to noise.
- 百般 ("in every way," 百般的讨好, ch35) the 百 is not 100; added to noise.
- 两点四十分 ("2:40," ch35): a genuine gap, not noise. The built-in clock-time strip's
  char class omitted 两, so the whole-clock pattern failed and the built-in 十分 (=very)
  then ate the "十分" out of "四十分", orphaning a 四 read as 4. Fix: added 两/兩 to the
  three top clock/duration char classes in check_numbers.py so 两点X分 / 两点钟 / 两分钟
  strip whole (before 十分 can run). Clock times are not the money/count/year quantities
  this check guards, so stripping them whole is safe, consistent with the existing block.
- Ordinals: "the twentieth century" (二十世纪, ch32) and the date "December the
  twenty-third" (二十三日, ch32) needed 20 and 23; \btwenty\b does not match inside
  "twentieth", and the cardinal matcher does not reach the ordinal "twenty-third", so
  both were added to WORD_NUM (same as the earlier eleventh/seventeenth entries).
- Prose fix (not a script change): 十来个 ("ten or so," ch33) rendered "ten or so"
  rather than "a dozen or so" so the source 10 survives to the target.
- Not re-verified by the check but rendered faithfully in the prose by hand: the clock
  times (一点半 half past one ch32; 两点四十分 2:40 ch35, kept as "Twenty to three"),
  durations (半个钟头, 二十分钟, 十五分钟, 三分钟), the positional years (一九四○年
  Buick, 一九四一年 Christmas Eve), the speeds in li (二十五/三十八/四十/四十四), the bow
  angles (二十度 / 四十五度), and the step-count 一二三四五六 (all present as "one...six").

Fact-checking (Wikipedia / Baidu Baike; no LLM-sourced references):
- Jiangwan (江湾) and "our Municipal Government Building": the Nationalist "Greater
  Shanghai Plan" (大上海计划) of the early 1930s laid out a civic centre in Jiangwan,
  north of the settlement; its centrepiece, the Shanghai Special Municipality Government
  Building, opened 1933 in a monumental Chinese-palace style, and the district was taken
  over for Japanese military use after 1937. Corroborated; footnoted (note 57).
- Greater East Asia (大东亚) / "goddess of peace" / "Sino-Japanese friendship": the
  Greater East Asia Co-Prosperity Sphere (大东亚共荣圈) was proclaimed by Japan in 1940;
  "peace" and "Sino-Japanese amity" were standard collaborationist slogans. Corroborated;
  footnoted (note 58) and added to the glossary.
- Ghost Love (鬼恋): Xu Xu's own 1937 novella, the sensation that made his name (already
  stated in the About-the-Author front matter, ch00); its heroine is a beautiful,
  enigmatic woman in black met by night who claims to be a ghost. Corroborated;
  footnoted at the allusion in ch35 (note 59).

Footnotes added (density: 4 across five chapters, all genuinely new references; the many
recurring names/places/terms in these chapters already carry their note at first
appearance in B01 to B06 and were deliberately not re-noted):
- note 57 (ch33): Jiangwan and the Greater Shanghai Plan civic centre.
- note 58 (ch33): the Greater East Asia Co-Prosperity Sphere propaganda slogans.
- note 59 (ch35): the heroine of Ghost Love (Xu Xu's own novella).
- note 60 (ch35): the idiom 小鹿乱撞 kept literal as "little deer" (texture note).

Source digitization glitches rendered to plain meaning and NOT footnoted (no genuine
reading uncertainty):
- ch32 para 0 "跳出生活中在生活" (garbled) rendered to sense "leap clear of this life and
  truly live"; Helen's argument (the double standard she throws back at the narrator) is
  intact around it.
- ch34 para 51 "接巧的路灯" (接巧 for 凑巧, "conveniently placed") rendered "the
  well-placed lamp."
- ch35 para 61 dittography: the clause "从玻璃门推进去，我看到白苹拿着杯子站在桌上，大家围着"
  is printed twice in the source; rendered once ("Pushing in through the glass door, I
  saw Bai Ping standing on the table, glass in hand..."). Quoted verbatim (both copies)
  in the QC file for parity; deduplicated in the reading text.
- ch36 para 2 "小憧" (for 小僮/小童, a page-boy) rendered "the page"; the correctly written
  小僮 recurs in para 3 ("the boy who had fetched the car").
- 轮柏 (ch33/ch34/ch36), the tall conifer dressed as the Christmas tree, is almost
  certainly 龙柏 (dragon juniper) or 桧柏 mis-digitized; rendered consistently as
  "cypress." No meaning is at risk (it is plainly the evergreen tree of the party scene).
- ch36 para 58 "宾纳饭店" is the same place as the earlier "槟纳饭店"; rendered
  consistently as "the Benner Inn."
- ch36 para 4 "化学的派司封套": 化学 here means "celluloid/plastic," 派司 is the loanword
  "pass"; rendered "a celluloid pass-holder" (holding, the narrator supposes, a park
  pass). Loanwords, not an error.

Provisional renderings a later attestation could sharpen (all recurring names reuse the
fixed glossary forms): Miko (米可; the source itself flags the name's nationality as
unknown), the Kaidi Restaurant (凯第饭店), the White Palace (白宫舞厅), plus the earlier
provisionals that recur here (Umetake 梅武, the Standford, the Benner Inn, Honsa 本佐次郎,
Weihaiwei Road, Route Prosper Paris).

## Batch B08 (ch37 through ch41: Chapters 37 to 41) — DONE

Translated ch37 (三十七, 41_chapter39.txt, 85 paras), ch38 (三十八, 42_chapter40.txt,
72 paras), ch39 (三十九, 43_chapter41.txt, 33 paras), ch40 (四十, 44_chapter42.txt,
102 paras), ch41 (四十一, 45_chapter43.txt, 50 paras). ~17,945 source chars. Clean
first-person narrative prose; all apparatus in the notes. The batch's arc: the shooting
in the narrator's room and Dr. Philip's extraction to the Gaolang Hospital (ch37); the
three operations and the long convalescence, with Philip's cover-story conversation
(ch38); Helen's letter from Qingdao and the narrator's night of reflection (ch39); Mei
Yingzi's visit and her full account of the pistol/locket confrontation with Bai Ping,
which unknots the whole spy plot (ch40); Bai Ping sends the cat Jimi and her silver
diary, Mrs. Stephen and Mrs. Manfield visit, and the first diary page is read (ch41).

Bilingual QC files authored with scripts/_zip_bilingual.py (source side COPIED verbatim
from data/src, never re-typed), reading + parity split with split_bilingual.py.

Checks run and results:
- Verbatim source quotation: the whitespace-stripped char comparison of the joined '>'
  blockquotes vs the joined source paragraphs MATCHES for all five units (ch37 4377,
  ch38 4006, ch39 3890, ch40 4372, ch41 3776 chars). Source quotation is verbatim by
  construction (the zip helper copies it).
- check_numbers.py --noise data/noise.txt: all five GREEN (0 unresolved) after three
  new noise entries (below). Numbers preserved include the clock times (11:30, 12:15
  ch37; 9/10/2 o'clock ch38; 7 a.m. ch40; 9:00 and 10:30 ch41), the "sixty hours" and
  "five weeks" of ch38, the ordinals (second/third operation), the two packets/two
  trunks/two stars, "seven or eight times," "fifty-odd," "one or two usable people,"
  and the date January the fourth (ch39, in Helen's letter and the narrator's memory).
- check_structure.py --config scratch/b08_check.json (regenerated; scratch/ is
  gitignored): paragraph parity OK for all five (85/72/33/102/50); note anchors 3/3
  resolve, 0 unresolved; heading shape uniform; glossary drift 0 (variants map carried
  ONLY wrong forms, never the canonical).
- Blind double translation on the lyrical/analytical passages (Helen's sea-and-music
  letter ch39 paras 2/9/11; Mei Yingzi's "two orbs" cosmic passage ch40 para 98; the
  narrator's meditation on scale ch41 para 46) and round-trip back-translation as an
  omission check on the emotional beats (the pledge ch37 51-52; the locket exchange
  ch40 80-86); no divergence beyond wording. No omissions found.
- Random deep audit (~3.5%, 12 paragraphs: ch37 13/32/59, ch38 5/45/66, ch39 2/7,
  ch40 81/97, ch41 30/46): every source clause accounted for; observed error rate 0
  (the only source-side anomalies were the expected digitization glitches below, each
  rendered to plain sense).

data/noise.txt additions (each a non-quantity numeral the number check flagged):
- 四肢 ("the four limbs" i.e. the limbs generally, ch37 "额角四肢都有涔涔的汗"); 四≠4.
- 四望 ("to look around in all directions," ch39 "四望浸在月光中的房间"); 四≠4 (cf.
  the earlier 四顾/四围/四面).
- 万念 ("a myriad thoughts / every thought," ch38 "万念占据了我的心灵"); 万≠10000 (cf.
  万物/万国/万岁; 万种 was already in the noise list).

Footnotes added (3 across five chapters, all genuinely new references; every recurring
name/place/term in these chapters already carries its note at first appearance in
B01–B07 and was deliberately NOT re-noted). Numbering continuous; B07 ended at 60.
- note 61 (ch37): the Christmas-Eve dream's "holy robe of Atri in a novel by Flaubert" —
  translation-uncertainty note. The source misspells Flaubert ("Flaulert") and the robe
  "阿特立" (Atri) cannot be securely matched to anything in Flaubert; kept as printed and
  the uncertainty left visible (rule 4).
- note 62 (ch38, first appearance of Qingdao): Qingdao as a German/Japanese-leasehold
  seaside summer resort — the historical reference behind Helen's letter.
- note 63 (ch39): Mr. Stoyevsky and the White Russian émigré musicians of China's port
  cities — the milieu the fictional teacher belongs to.

Glossary rows added (glossary.json now 118 term rows): 青岛 Qingdao (attested, place);
史托亦夫斯基 Stoyevsky (provisional, the White Russian music teacher; source gives no
Latin spelling); 福楼拜 Flaubert (attested; source misspells as "Flaulert"); 巴哈 Bach,
贝多芬 Beethoven, 孟德尔仲 Mendelssohn (attested; the composers of Helen's letter, the
last written 孟德尔仲 for the usual 孟德尔松). REUSED without change: Mei Yingzi, Bai Ping,
Stephen/Mrs. Stephen, Helen, Mrs. Manfield, Dr. Philip, Ah Mei (阿美), Jimi (吉迷, the
white Persian cat), Dr. Gaolang/Gaolang Hospital (高朗) and Gaoye Road (高叶路), Honsa
Jiro, Umetake, Beiping, Jiangwan, Route Prosper Paris (姚主教路), the cheongsam (旗袍).

Fact-checking (Wikipedia / Baidu Baike; no LLM-sourced references):
- Qingdao: German Kiautschou (Jiaozhou) leasehold from 1898; seized by Japan 1914;
  restored to Chinese sovereignty 1922; reoccupied by Japan January 1938. Long developed
  as a beach/villa summer resort drawing Shanghai holidaymakers and foreign-navy crews.
  Corroborated; footnoted (note 62).
- White Russian émigré musicians: after the 1917 Revolution and Civil War, large émigré
  communities formed in Harbin, Shanghai, Tianjin and Qingdao, with many professional
  musicians teaching and performing (some in the Shanghai Municipal Orchestra). The
  fictional Stoyevsky fits this documented milieu. Corroborated as a phenomenon;
  footnoted (note 63).
- Flaubert: Gustave Flaubert (1821–1880). The dream's specific "holy robe of Atri"
  cannot be matched to any Flaubert work; reported as uncorroborated / unidentifiable
  and left visible (note 61), not silently "fixed."

Source digitization glitches rendered to plain meaning and NOT footnoted (no genuine
reading uncertainty):
- ch37: "手抢" for 手枪 (pistol) rendered "pistol"; "枪扭" for 枪机 (the earlier form)
  rendered "pulled the trigger"; "江弯" for 江湾 rendered "Jiangwan" (the glossed form).
- ch39: "孟德尔仲" for 孟德尔松 (Mendelssohn) rendered "Mendelssohn" (glossary note).
- ch40: "胸坏" for 胸怀 ("heart/breast," in "宽大的胸坏去原谅人") rendered "a broad
  enough heart to forgive people."

Provisional renderings a later attestation could sharpen (all recurring names reuse the
fixed glossary forms): Stoyevsky (史托亦夫斯基; the source gives no Latin spelling),
"Atri" (阿特立; unidentifiable, kept as printed and footnoted), plus the earlier
provisionals that recur here (Umetake 梅武, Honsa Jiro 本佐次郎, Dr. Gaolang 高朗 /
Gaoye Road 高叶路, Manfield 曼斐儿, Dr. Philip 费利普). The flower-name "莲菊" (ch38) has
no standard English equivalent and is rendered descriptively as "lotus-daisies."

## Batch B09 (ch42 through ch45: Chapters 42 to 45) — DONE

Translated ch42 (四十二, 46_chapter44.txt, 132 paras), ch43 (四十三, 47_chapter45.txt,
96 paras), ch44 (四十四, 48_chapter46.txt, 70 paras), ch45 (四十五, 49_chapter47.txt,
139 paras). ~14,344 source chars. The batch's arc: ch42 is Bai Ping's diary — the
extracts the narrator copies from her silver diary (introduced end of ch41), her own
coded shorthand decoded by his interpolated "My note:" glosses, ending with the
pistol-under-the-mattress reveal that she and Mei Yingzi are secret allies; ch43, out
of hospital with a maimed left arm, the three agents plot the masked-ball theft and
draw lots (the Lucky Strike among the 555s), and Helen comes back from Qingdao changed,
and the narrator half-promises to go with her to Beiping; ch44, the eve of the ball,
Helen's ten-thousand-yuan check from Mrs. Stephen, and the operation briefing with the
diamond-cross ring and the Korean dancer Miko as the way in; ch45, the long night-
before dialogue with Bai Ping, who begs to take the task herself, walks him through the
will, the no-confession vow, and the three "quinine" suicide pills, and at the end
smiles for him "like a lily just opening," tears in her eyes.

The DIARY (ch42) presentation, following ch41's convention and noted at the first
extract (note 64): each diary entry is a self-contained double-quoted paragraph; a lone
source 「──」 divider renders as a lone em-dash paragraph "—", a lone 「……」 as a lone
"…"; a fused open 「──X」 keeps a leading em-dash inside the quote ("—X"), a fused close
「X──」 a trailing one ("X—"); the narrator's own 「──...──」 block-boundaries around his
"My note:" glosses are the source's way of fencing the extracts. Every source paragraph
maps 1:1 (the _zip_bilingual.py count guard held at 132).

Bilingual QC files authored with scripts/_zip_bilingual.py (source side COPIED verbatim
from data/src, never re-typed), reading + parity split with split_bilingual.py.

Checks run and results:
- Verbatim source quotation: whitespace-stripped char comparison of the joined '>'
  blockquotes vs the joined source paragraphs MATCHES for all four units (ch42 4088,
  ch43 4067, ch44 3604, ch45 5364 chars). Verbatim by construction.
- check_numbers.py --noise data/noise.txt: all four GREEN (0 unresolved) after the
  noise additions below and two WORD_NUM ordinals. Numbers preserved include the ball
  date (March 11/12/13), the clock times (half past twelve, twelve noon, eleven forty-
  five, half past four to five, past four), the arm angles (67-68/10/80 degrees), the
  ten-thousand-yuan check, "nine chances in ten," the one-tenth/nine-tenths of the
  diary, the "four/eight/six/two parts" of Bai Ping's plea, the three pills, "two days
  in jail... two hours at a concert," and the drawing-of-lots rounds (second/third).
  Three "no one else / secondly / the two of us" spots were reworded so the source
  第二/第二方面/两个人 count survives (first pass rendered them "no one else / on the
  other / together").
- check_structure.py --config scratch/b09_check.json (regenerated; scratch/ is
  gitignored): paragraph parity OK for all four (132/96/70/139); note anchors 69/69
  resolve, 0 unresolved; heading shape uniform across all 46 built docs; glossary drift
  0 (variants map carried ONLY wrong forms, never the canonical).
- Blind double translation (separate context) on the analytical/lyrical passages — the
  diary aphorisms (ch42 the "two extremes" para 2, the "what does she mean" para 30, the
  "thousand kinds of people" para 73, the two coded-gloss annotations), the "two kinds
  of people" opening (ch43 para 3), the native-place meditation (ch43 para 83), the
  long philosophy reflection (ch44 para 36), Bai Ping's "what is wrong with being
  afraid" catalogue (ch45 para 55), her "four parts / eight parts" plea (para 108) and
  the cock-crow passage (para 112): no divergence beyond wording; the blind pass
  independently flagged 肩牌 as a typo for 肩膀 "shoulder" (already so rendered) and read
  對手 as the espionage "adversary" (as rendered).
- Round-trip back-translation (separate context) as an omission check on five number-
  and clause-heavy passages (ch42 para 2, ch42 para 73, ch43 para 3, ch45 para 108, ch45
  para 112): no dropped clause, name, negation, or numeral; the flagged four "parts"
  (四/八/六/二) were confirmed against the source and by check_numbers.
- Random deep audit (~3.2%, 14 paragraphs across the four chapters, incl. the long
  ch44 para 36, ch45 para 55, ch45 para 108): every source clause accounted for;
  observed error rate 0 (the only source-side anomalies were the digitization glitches
  below, each rendered to plain sense).

data/noise.txt additions (each a non-quantity numeral the number check flagged), and
two WORD_NUM ordinals in check_numbers.py:
- 千种 ("a thousand kinds of people," ch42 千种人，万种人); 千≠1000 (万种 already listed;
  the built-in 千万 strips 千万种, so only 千种 needed its own line).
- 三五牌 = State Express 555 cigarettes (the ch43 lots); a brand, not 3/5.
- 十字 = "cross" the shape (ch44 划一个十字, 以这十字为记号); 十≠10 (十字架 already listed;
  this covers the bare 十字 without 架).
- [一二三四五六七八九十]刻 = quarter-hour time unit (ch45 十一时三刻 "eleven forty-five");
  a clock expression, strips the numeral before 刻 so 十一时 → 11 survives whole.
- WORD_NUM: "twelfth" → 12, "thirteenth" → 13 (date ordinals: "the twelfth/thirteenth
  of March" render 三月十二日/十三日; the cardinals were present but not the ordinals).

Glossary rows added (glossary.json now 120 term rows): 国泰 the Cathay (attested; the
Cathay Theatre on Avenue Joffre, opened 1 Jan 1932, where the narrator and Helen see a
film, ch43); chez Rovere (provisional; a Western restaurant, the name printed in Latin
script in the source, ch43). REUSED without change: Bai Ping, Mei Yingzi, Helen, Mrs.
Stephen/Stephen, Mrs. Manfield, Dr. Philip (费先生/电费 = Fei = Dr. Philip), Ah Mei,
Jimi, Umetake (梅武), Honsa Jiro (本佐次郎), Colonel Arita (有田大佐), Miko (米可), the
Standford, Qingdao, Beiping, Stoyevsky, the Bakou Apartments, Dr. Gaolang / Gaolang
Hospital (高朗), the cheongsam, Greater East Asia.

Footnotes added (6 across the four chapters, notes 64–69, all genuinely new; every
recurring name/place/term already carries its note at first appearance in B01–B08):
- note 64 (ch42): the diary presentation — that Chapter 42 is copied extracts with the
  narrator's interpolated "My note:" glosses decoding the coded vocabulary, the dashes
  and dots marking his omissions.
- note 65 (ch42): the "longed to be a man" line is Mei Yingzi's remembered remark
  admiring the ring, the diary slipping into others' recorded words.
- note 66 (ch43): State Express 555 and Lucky Strike as the cigarette lots (555 a BAT
  brand hugely popular in China then; the lone Lucky Strike the marked lot).
- note 67 (ch43): "the interior" (後方) = unoccupied Free China, governed from Chongqing,
  as against Japanese-held Beiping.
- note 68 (ch44): Korea a Japanese colony since 1910, hence the dancer Miko, taken for
  Japanese, is in fact Korean.
- note 69 (ch45): quinine (金鸡纳霜) the ordinary anti-malarial, the medicine bottle a
  blind for the three suicide pills, later spoken of in code as the narrator's "aspirin."

Fact-checking (Wikipedia / Baidu Baike; no LLM-sourced references):
- Cathay Theatre (国泰大戏院/Cathay Cinema), Avenue Joffre, Shanghai: opened 1 January
  1932 (first as the "Cathay Grand"), Art Deco house by C. H. Gonda, 1,080 seats.
  Corroborated; used for the glossary row (ch43).
- State Express 555: a British American Tobacco brand (from the Ardath Tobacco Co.,
  overseas rights to BAT 1925), a major seller in Republican-era China. Corroborated;
  footnoted (note 66).
- Japan's annexation of Korea, 1910: corroborated; footnoted (note 68).
- Quinine as the standard cinchona-derived anti-malarial of the day: corroborated;
  footnoted (note 69).

Source digitization glitches rendered to plain meaning and NOT footnoted (no genuine
reading uncertainty; the blind translation pass independently confirmed 肩牌):
- ch42: "勾谷" (para 76, 入她的勾谷而听她指使) rendered "snare" (a non-word; sense fixed
  by 听她指使 "do her bidding"); "一一" used for an em-dash (para 68 麽？一一梅瀛子; also
  ch43 para 47 「一一纪念我的新生」) rendered "—"; "我的抱了许久" (para 128, stray 的)
  rendered "I held her long."
- ch43: "收起丁照相" (para 46, garbled 了) rendered "gathered up the photographs";
  "史蒂芬基前" (para 88, 基 for 墓 grave) rendered "before Stephen's grave."
- ch44: "他但这是不必同海伦说明的" (para 19, stray 他) rendered "only there was no need
  to explain it to Helen."
- ch45: "肩牌" (para 112, for 肩膀 shoulder) rendered "patted her shoulder."

## Batch B10 (ch46 through ch48: Chapters 46 to 48) — DONE

Translated ch46 (四十六, 50_chapter48.txt, 151 paras), ch47 (四十七, 51_chapter49.txt,
116 paras), ch48 (四十八, 52_chapter50.txt, 146 paras). ~17,009 source chars. The
batch is the theft operation and the ball (narrative, not diary). ch46: the night
before is abandoned (the narrator gives up his plan to say goodbye to Helen and the
others), Bai Ping telephones and they pass a strained afternoon at the Xiangong tea
dance, then Honsa Jiro's dinner (the demure Miyama Yoshiko as guest of honor), and the
masked ball, where the ring codes, palm-traced crosses and the whispered safe
combination "GH509K8" hand the narrator the key; he climbs the short ladder into the
safe-room and, hidden under the round table, watches an unknown woman in white open the
safe, take the two documents, set a bomb inside, and leave, and he squirts ink from his
Parker onto her trailing skirt. ch47: alone again, he climbs back down, meets Mei
Yingzi, who reads the intrusion as Bai Ping's "rivalry for credit," and the two of them
slip back in; the ink-marked woman ("the blue rattlesnake") is danced down, and she
gives her name as Asamura Toshimiko and lets fall that she spent ten years in Manchukuo.
ch48: the 5 o'clock unmasking reveals the blue-snake woman to be Miyama Yoshiko (the
same demure girl from the dinner), the narrator drives Sophie home and goes to Bai
Ping's, dozes into a snake-and-gunshot dream, and Bai Ping returns in triumph with
Miyama Yoshiko's real address (Youheng Road, by Juxian Village); the three settle that
the real target is now the woman herself, and the narrator, unable to leave for Beiping
with Helen, resolves to stay on.

Bilingual QC files authored via scripts/_zip_bilingual.py (source side copied verbatim
from data/src, BOM and the two duplicated chapter-numeral heading lines stripped);
paragraph counts matched on the first pass for all three (151 / 116 / 146). The
whitespace-stripped char comparison of the joined '>' blockquotes against the joined
source paragraphs was IDENTICAL for every unit (ch46 9474, ch47 5039, ch48 5218), so
the source is quoted verbatim. The lone source "──" divider in ch47 (para 43) renders
as a lone "—" paragraph; the ch46 song (paras 83 to 94) is kept line by line as verse.

The checks (recorded per the QC contract):
1. Faithful verbatim quotation: confirmed by the char-identical comparison above.
2. Blind double translation (separate context, subagent, cold): the reflective/analytic
   and lyric passages (ch46 the three considerations; ch47 the "rivalry for credit"
   reflection; the ch46 song; the ch47 Manchukuo exchange). No meaningful divergence
   from the shipped rendering, so the source is not ambiguous in these passages.
3. Round-trip back-translation (subagent, cold): ch48's closing Stephen reflection and
   ch46's safe-room paragraph. No omissions or additions; every flag the back-translator
   raised resolved as faithful when checked against the source (the piled-up
   "cunning / crookedness / dark quality" = 刁滑/弯曲/阴涩, three real terms; "mystery" =
   神秘; "waning moon" = 下弦月; "drive past" = the author's own 驶过).
4. Automated invariant checks: check_numbers.py --noise data/noise.txt GREEN on all
   three (0 unresolved) after two noise additions (below); check_structure.py --config
   over the batch (scratch/b10_check.json, regenerated) PASS on all four checks
   (parity 151/116/146 exact, 4 note anchors resolve, one heading shape, 0 glossary drift).
5. Term ledger: glossary.json updated (below); one rendering per referent reused.
6. Annotate, do not smooth: uncertain Japanese name readings marked provisional in the
   glossary and footnoted (note 73); no uncertainty laundered into fluent prose.
7. Consistency against scholarship: fact-checked (below).
8. Random deep audit (~4%, 6 long paragraphs: ch46 002/067/148, ch47 028, ch48 026/145):
   full verbatim/mistranslation/omission pass. Observed substantive error rate 0; one
   stylistic note only (the author's mechanical verb 驶 "drive/speed" for a skirt's
   motion is kept literal rather than smoothed to "glide," per the keep-the-voice rule).

Number-check noise added to data/noise.txt (B10 block), each because the check flagged a
non-quantity numeral:
- GH[五○九K八×]+ — the safe-combination cipher "GH509K8" (ch46), plus its redacted
  GH五××K八 and partial GH五○ forms; the 五/九/八 are cipher digits, not quantities.
  The English keeps the code as "GH509K8", which the target extractor reads as 509, so
  the source 五/九 went unaccounted until the whole token was stripped.
- 万千 / 萬千 — "万千人民" (ch48), "thousands upon thousands / the myriads of our people";
  rhetorical multitude, parsed as 11000. The built-in strips the reversed 千万 but not
  万千, so it needed its own entry (cf. 万物 / 万念 / 万国).

Footnotes added (4, notes 70–73, all genuinely new; recurring names/places/terms already
carry their note at first appearance in B01–B09):
- note 70 (ch46): Columbia Road and the Xujiahui church as Mei Yingzi's private code for
  her two collaborators (Bai Ping and Miko); Columbia Road a real western-Shanghai road
  (Columbia Avenue, laid out 1925, renamed Panyu Road 1943), its old name period-correct.
- note 71 (ch47): the "blue snake" code, from the ink the narrator squirted on the
  intruder's skirt drying into a line of dots like a small snake; the source varies the
  epithet (蓝色响尾蛇 / 蓝尾蛇 / 蓝色的小蛇), and the variation is kept.
- note 72 (ch47): Manchukuo, the Japanese puppet state (1932–1945) in the Northeast under
  Puyi; the pointed exchange over whether it is Chinese soil.
- note 73 (ch48): the Miyama Yoshiko / Asamura Toshimiko reveal, both names Japanese and
  read tentatively; the surname 宫间 (Miyama) echoes the hospital flower-sender 宫间登水,
  and the element 登水 recurs in 登水子.

Glossary rows added (glossary.json): people — 宫间美子 Miyama Yoshiko (provisional),
朝村登水子 Asamura Toshimiko (provisional), 木谷 Kiya (provisional), 本佐太太 Mrs. Honsa
(decided); places — 明湖春 the Minghu Chun (provisional), 歌伦比亚路 Columbia Road
(attested), 有恒路 Youheng Road (decided, pinyin), 聚贤村 Juxian Village (provisional);
terms — 蓝尾蛇 the blue-tailed snake (decided, the code-name). The existing Sophie row
(莎菲) was updated to record the source's other spelling 沙菲, used throughout ch46–ch48;
one rendering, Sophie, throughout. Reused the whole prior cast and geography exactly
(Honsa Jiro, Umetake, Arita, Miko, Dr. Philip, Bai Ping, Mei Yingzi, Helen, the
Manfields, Ah Mei, Jimi, the Xiangong, Yuyuan Road, North Sichuan Road, Hongkou, Beiping,
Greater East Asia).

Fact-checking (Wikipedia / Shanghai Daily / Baidu Baike; no LLM-sourced references):
- Columbia Road (Columbia Avenue, 歌伦比亚路): built by the Shanghai Municipal Council in
  1925 in the far west of the city, renamed Panyu Road (番禺路) in October 1943.
  Corroborated; the novel's wartime setting predates the rename, so "Columbia Road" fits.
  Used for the glossary row and note 70.
- Manchukuo (满洲国): Japanese puppet state in the Northeast (Manchuria), created 1932,
  nominally ruled by Puyi the last Qing emperor, dissolved 1945. Corroborated; note 72.
- 有恒路 (Youheng Road): a real Hongkou road named in the source but its modern name not
  confirmed in the search, so kept as a project pinyin rendering (status "decided"), not
  claimed as attested.

Source digitization glitches rendered to plain meaning and NOT footnoted (no genuine
reading uncertainty):
- ch46 para 95: "轮桌己撤" (己 for 已) rendered "the trolley tables had been cleared away."
- ch46 para 141: "有咱五对人" (stray 咱) rendered "some five couples."
- ch48 para 63: "我摄出桌外" (摄 for 爬, to crawl) rendered "I crawled out from under the
  table."
- ch48 para 78: "我听见你梦吃中直叫白苹" (梦吃 for 梦呓, sleep-talking) rendered "I heard
  you calling out 'Bai Ping' straight through your sleep-talking."

Build: python3 scripts/build_reading_epub.py "out/The Whistling Wind.epub" — 49 of 60
chapters translated (ch00–ch48), 73 notes; the TOC stays pending-aware, the 11
untranslated chapters still linking their skeleton outlines. qa_epub.py GREEN
(72 files, 66 documents, 73 references / 73 bodies / 73 backlinks, all links resolve).

## Batch B11 — Chapters 49 to 52 (ch49, ch50, ch51, ch52)

Units and sizes (source chars, from the ingest): ch49 = 6,129 (源 四十九),
ch50 = 4,330 (源 五十), ch51 = 5,313 (源 五十一), ch52 = 5,045 (源 五十二).
Batch = 346 source paragraphs. This is the aftermath of the failed theft turning into
the book's action climax: ch49 the second visit to Honsa Jiro's and the intercepted
dossier signed "S.V"; ch50 Mei Yingzi burning the two sheets and Bai Ping's resolve to
go for the documents; ch51 the drive to Youheng Road, the shooting of Bai Ping and the
narrator's reflexive return fire, the flight to the Suzhou Creek boats, and the
introduction of the boat girl Cishan; ch52 the night on the boat, grief for Bai Ping,
Mei Yingzi's disguise, and the heroin-slum passage.

The checks (QC contract), all run this batch:
1. Faithful, complete quotation: the bilingual QC files quote the source VERBATIM
   (built with scripts/_zip_bilingual.py, which copies the source paragraphs and errors
   on any paragraph-count mismatch). Confirmed by the whitespace-stripped char comparison
   of the joined '>' blockquotes vs the joined source paragraphs: ch49 5998=5998,
   ch50 4235=4235, ch51 5228=5228, ch52 4973=4973; paragraph counts 121/87/75/63 exact.
2. Blind double translation (separate context, subagent): 15 sample paragraphs across the
   batch (the analytical/lyrical passages plus the intercept dossier and the shooting)
   forward-translated blind and diffed. FULL substantive agreement; the only divergences
   were provisional name readings where this project already fixes the form in the
   glossary (梅武 Umetake, 朝村登水子 Asamura Toshimiko, 秋雨三郎 Akiu Saburo) and the
   八角/四角 money unit (rendered "eight jiao / four jiao" here to keep the source numeral,
   glossed in note 81, vs the subagent's naturalizing "eighty/forty cents"). The subagent
   independently flagged the same two ch52 digitization corruptions handled below.
3. Round-trip back-translation (separate context, subagent): 5 English paragraphs
   (the dossier letter, the shooting, the ch52 opening, the intimacy paragraph, the
   coincidence paragraph) translated back to Chinese and diffed against the source as an
   omission detector. No omissions; every clause, name, and number present.
4. Automated invariant checks: check_numbers.py --noise data/noise.txt on each bilingual
   file — 0 unresolved on all four (121/87/75/63 pairs). check_structure.py --config
   over all 53 translated units (scratch/b11_check.json, regenerated) PASS on all four:
   parity 121/87/75/63 exact, 83 note anchors resolve (0 unresolved), one heading shape,
   0 glossary drift.
5. Term ledger: glossary.json updated (below); one rendering per referent reused across
   the whole cast and geography.
6. Annotate, do not smooth: uncertain name readings marked provisional in the glossary and
   footnoted (notes 74, 75); the ch52 source corruption (a dropped negative) footnoted
   (note 80) rather than silently smoothed; no uncertainty laundered into fluent prose.
7. Consistency against scholarship: fact-checked (below).
8. Random deep audit (~4.3%, 15 paragraphs: ch49 005/071/074/115/118, ch50 023/047,
   ch51 015/016/065/074, ch52 001/026/030/037): full verbatim / mistranslation / omission
   pass via the blind forward-translation and back-translation above. Observed substantive
   error rate 0.

Number-check noise added to data/noise.txt (B11 block), each because the check flagged a
non-quantity numeral:
- 三郎 — the Japanese given-name suffix Saburo (in 秋雨三郎, Miyama Yoshiko's male alias,
  ch49); the 三 names the third son, not a count. The English keeps "Akiu Saburo" (no
  digit), so the source 三 went unaccounted until stripped.
- 第一万 — a source corruption in ch52 (a dropped negative: "第一，千万[不]要告诉人…"); the
  collapsed "第一万" parses as the ordinal 1 + 一万 = 10000, neither a real quantity.

Source digitization glitches rendered to plain meaning and NOT footnoted (no genuine
reading uncertainty):
- ch50 para 2: "看她E 我换了" (stray "E" for a period) rendered as a sentence break,
  "...to look at her so any longer. I turned my eyes instead to Bai Ping..."
- ch50 para 7: "我以为我你现在的问题" (dittographic 我 before 你) rendered "I thought your
  problem now was Miyama Yoshiko..."
- ch50 para 77: "我对於白苹的坚决开始非常饮佩" (饮佩 for 钦佩, "admire") rendered "I began to
  admire Bai Ping's resolve greatly."
- ch52 para 26: "第一万要告诉人你有客人在这里" — a dropped negative reversing the sense;
  restored to "on no account tell anyone you have guests here" AND footnoted (note 80),
  left visible rather than smoothed.
- ch52 para 26 ends on a stray "、" (dun-comma for a full stop); rendered with a period.
- ch52 para 26: "鸩溺" (for 沉溺, "immersed/drowned in") rendered "drowned in"; "极桌"
  (for 板桌, the plank table used earlier in the chapter) rendered "the plank table."

Footnotes added (10, notes 74-83, all genuinely new; recurring names/places/terms already
carry their note at first appearance in B01-B10):
- note 74 (ch49): Kawashima Yoshiko (川岛芳子, 1907-1948), the real Manchu-princess spy
  Miyama Yoshiko is said to have followed; corroborated.
- note 75 (ch49): the aliases Lang Diyi (郎第仪) and Akiu Saburo (秋雨三郎), both provisional
  romanizations, the source giving none; the mannish alias echoes Kawashima.
- note 76 (ch49): Edinburgh Road (忆定盘路, today Jiangsu Road), whose Chinese name
  transliterates "Edinburgh"; the Yuyuan Road corner address differs from the Youheng
  Road house the ch48 intelligence gave as Miyama's real residence.
- note 77 (ch51): the dialect romanization Tche San / Teh-San mapped to the Mandarin name
  Cishan, and the coincidence with the fictitious country girl of the narrator's decoy
  letters.
- note 78 (ch51): the boat people (船户) of Suzhou Creek, the destitute sampan community
  the pair take refuge among.
- note 79 (ch51): sealing off a district (封锁), the Japanese barbed-wire/rope-barrier
  cordon used to trap a fugitive after an incident.
- note 80 (ch52): the dropped-negative corruption in the source (第一万要告诉人…), sense
  restored, left visible.
- note 81 (ch52): "white powder" (白面) = heroin, and the jiao (角) money unit of the
  addicts' fixed daily dose.
- note 82 (ch52): Mei Lanfang (梅兰芳, 1894-1961) and "The Heavenly Maiden Scatters Flowers"
  (天女散花, first staged 1917); corroborated.
- note 83 (ch52): the paired 寿 (shou, "long life") character on the earrings as an
  auspicious charm, set against Bai Ping's "lucky earrings."

Glossary rows added (glossary.json, now 141 rows): people — 慈珊 Cishan (provisional),
川岛芳子 Kawashima Yoshiko (attested), 郎第仪 Lang Diyi (provisional), 秋雨三郎 Akiu Saburo
(provisional), 梅兰芳 Mei Lanfang (attested); places — 忆定盘路 Edinburgh Road (attested),
斐伦路 Fearon Road (attested), 聚贤里 Juxian Li (decided; the ch51 sign for the same lane
ch48 wrote 聚贤村 Juxian Village, source varies the suffix 里/村), 苏州河 Suzhou Creek
(attested); terms — 摩理斯 Morris (attested), 白面 white powder (attested; heroin),
天女散花 The Heavenly Maiden Scatters Flowers (attested), 大英牌 Great Britain brand
(decided). Reused the whole prior cast and geography exactly (Honsa Jiro, Umetake,
Miyama Yoshiko, Asamura Toshimiko, Bai Ping, Mei Yingzi, Ah Mei, Stephen, Yuyuan Road,
Youheng Road, Route Prosper Paris, Hongkou, North Sichuan Road, Pudong, Chongqing,
Manchukuo, the Pacific war, the cheongsam).

Fact-checking (Wikipedia / Baidu Baike / Shanghai road-history sources; no LLM-sourced
references):
- Kawashima Yoshiko (川岛芳子): real historical figure, born Aisin Gioro Xianyu, Manchu
  princess raised in Japan by Kawashima Naniwa, spy for the Kwantung Army and Manchukuo,
  known for male dress, executed for treason 1948. Corroborated; note 74, glossary row.
- Mei Lanfang (梅兰芳, 1894-1961) and "The Heavenly Maiden Scatters Flowers" (天女散花,
  premiered 1917, from the Vimalakirti Sutra, famous for the ribbon dance). Corroborated;
  note 82, glossary rows.
- 忆定盘路 = Edinburgh Road (transliteration of "Edinburgh"), today Jiangsu Road.
  Corroborated. 斐伦路 = Fearon Road (transliteration of "Fearon"), by the Hongkou
  waterfront near Suzhou Creek, today Jiulong Road. Corroborated. 姚主教路 confirmed again
  as Route Prosper Paris (Route Mgr. Prosper Paris, today Tianping Road), the form already
  fixed in the glossary. Reused.

Build: python3 scripts/build_reading_epub.py "out/The Whistling Wind.epub" — 53 of 60
chapters translated (ch00-ch52), 83 notes; the TOC stays pending-aware, the 7 untranslated
chapters (ch53-ch59) still linking their skeleton outlines. qa_epub.py GREEN
(72 files, 66 documents, 83 references / 83 bodies / 83 backlinks, all links resolve).
