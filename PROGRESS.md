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
