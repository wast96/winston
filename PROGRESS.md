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
