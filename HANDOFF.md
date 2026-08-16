# HANDOFF — The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start Batch 8. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch07's English first.

```
Sword Roars B08

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2). Run ./setup.sh first.

Do Batch 8 = Chapter Eight, "金陵夜，十万火急 / A Nanjing Night, Deadly Urgent"
(ch08), PDF 172-207, printed 157-192, end to end per the pipeline in CLAUDE.md.
Ten sections: ch08s01 一、徐恩曾栽在了钱壮飞手里 (PDF 173, printed 158),
ch08s02 二、铁三角 (PDF 176, printed 161), ch08s03 三、只要不死，就会看到他叛变
(PDF 183, printed 168), ch08s04 四、化广奇 (PDF 186, printed 171), ch08s05
五、刺杀蒋介石 (PDF 188, printed 173), ch08s06 六、对付共产党的大计划 (PDF 194,
printed 179), ch08s07 七、地图被小刀划出大叉 (PDF 196, printed 181), ch08s08
八、破例要了一支烟 (PDF 200, printed 185), ch08s09 九、大魔术家并不等于魔术大师
(PDF 203, printed 188), ch08s10 十、英雄死了，英雄长在 (PDF 204, printed 189).
Simplified Chinese, horizontal; OCR chi_sim --psm 6; crop --left 0.06 --right
0.95 --top 0.11 --bottom 0.955; offset is a constant 15 (printed = pdf - 15),
no plate drift, but READ each opener's folio off the scan.

BEFORE translating, read the final two pages of Chapter Seven's English
(out/ch07_reading.md) so the voice carries over unbroken. Chapter One remains
the FROZEN register reference: run check_register.py --ref out/ch01_reading.md
on ch08 and record it (judge on the narratorial signals per
references/register-drift.md; the dialogue-contraction metric moves with how
dialogue-heavy the chapter runs, and is not itself drift). Chapters One-Seven's
data/zh were hand-transcribed off the scans (OCR too noisy on the proper names,
assemble breaks on figure/opener pages); do the same for ch08 where assemble
misaligns, and keep parity exact. In the hand-transcribed data/zh/ch08.txt mark
the chapter title with ### (same prefix as the section heads), NOT ##. Cite
printed folios in notes, never PDF pages. Never invent bridging text: if OCR
breaks mid-sentence or a leaf is damaged, crop the scan and read the real
continuation, or footnote the gap. Verify every name, number and low-confidence
span against a magnified crop before writing. Consult authority.json and
glossary.json for settled renderings (esp. the Central Special Branch, the Red
Squad, the Zhongtong, the Party Affairs Investigation Section, Zhou Enlai, Gu
Shunzhang, Chen Geng, Chiang Kai-shek, and from earlier chapters: 徐恩曾 Xu
Enzeng, 陈立夫 Chen Lifu, 钱壮飞 Qian Zhuangfei, 化广奇 Hua Guangqi = Gu's stage
name, 黎明 Liming = Gu's alias). This is the great "Qian Zhuangfei's warning"
chapter: the three Party men inside the KMT intelligence service (钱壮飞 Qian
Zhuangfei, 李克农 Li Kenong, 胡底 Hu Di — the "铁三角/iron triangle"), the
decoding of Gu Shunzhang's defection cables, the plot to assassinate Chiang,
and Gu's end. Expect fresh institutions and material culture to note, and a
martyr set-piece at the close (keep the temperature; footnote the verdict).
Add ch08 to data/content_config.json when you translate it, or the displacement
check silently skips it.

Deliver the built EPUB attached in the chat, and paste the Batch 9 kickoff
verbatim in the same reply.
```

## DONE (one line per batch; do not redo)
- Survey: structure, offsets, style contract, skeleton EPUB. (earlier session)
- **B01 = ch01 (voice gate):** full translation (165 paragraphs), 115 footnotes,
  12 figures, glossary seeded, all checks green, epubcheck clean, blind-critique
  loop run, held at and passed the human voice gate. Details in PROGRESS.md.
- **B02 = ch02:** 56 paragraphs, 28 footnotes, 5 figures, 14 new glossary rows;
  all checks green, qa_epub PASS, epubcheck 0/0.
- **B03 = ch03 "Who Is Judas":** 146 paragraphs, 33 footnotes, 4 figures, 59 new
  glossary rows; all checks green, qa_epub PASS, epubcheck 0/0.
- **B04 = ch04 "Bloodshed on Avenue Joffre":** 131 paragraphs, 24 footnotes, 10
  figures, 62 new glossary rows; all checks green, qa_epub PASS, epubcheck 0/0.
- **B05 = ch05 "A Real Vault, a False Marriage":** 66 paragraphs, 27 footnotes,
  5 figures, 75 new glossary rows; all checks green, qa_epub PASS, epubcheck 0/0.
- **B06 = ch06 "It Was Not Me, It Was the Wind":** 165 paragraphs (3 {v} block
  quotes), 28 footnotes, 3 figures, ~120 new glossary rows; all checks green,
  qa_epub PASS (255 notes), epubcheck 0/0.
- **B07 = ch07 "The Great Hermit Hides in the City":** 99 paragraphs (all inline
  quotation), 20 footnotes, 6 figures (incl. a full-page street map), ~90 new
  glossary rows; parity 99=99, numbers 0, align/content/entities clean, anchors
  20/20, register within tolerance (dialogue metric quiet — memoir-dominated
  chapter, correct), qa_epub PASS (275 notes total), epubcheck 0/0. GLOBAL fix
  this batch: 卡德路 "Cardan Road" → "Carter Road" (glossary + ch04, rebuilt).
  Details in PROGRESS.md.

## Tooling in place — DO NOT REVERT
- `scripts/indents.py`: furniture-band drop by y-position (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`). Folio + running head are one TOP band; no foot.
- `scripts/check_numbers.py`: arabic+万 combiner ("31万"=310,000) BEFORE the
  noise loop; matches English number-WORDS, ordinals, and MONTH NAMES.
- `build_reading_epub.py` alt-attribute escaping (fixed B04): figure `alt` is
  emitted through `html.escape(..., quote=True)`. Keep it; prefer single quotes
  in alt.
- `data/noise.txt`: this book's event-date names, numeral-bearing proper names,
  decade labels, idioms. B02-B07 blocks appended. **B07 block:** 一九三○ (Ding
  Ling's title year), 三三五五, 四郊, 八秩, 千言万语, 瘪三, 两回事, 牌九, 两白银,
  几十两, 零食 — each strips a SOURCE numeral carrying no cardinal quantity (an
  idiom, a measure word like 两=tael, a game name like 牌九, or a word-internal
  0/3/9), so none can mask a real drop. Extend per its header; longest literal
  first; comment every entry.
- `data/content_config.json`: docs+sources map for check_content; now covers
  ch01-ch07. ADD ch08 when you translate it. Run check_content with
  `--config data/content_config.json`.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Parity gotcha (confirmed B05/B06/B07):** in the hand-transcribed
  `data/zh/chNN.txt`, mark the chapter title `### ` (same prefix as section
  heads), NOT `## `. `check_structure` strips only `###`-prefixed lines on the
  source side; a `## ` chapter line inflates the source count by one. On the
  English side (`out/chNN_reading.md`) the chapter title is `## ` and section
  heads `### `; both are stripped there.
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the
  JSON TOP LEVEL; the builder's render_glossary chokes on a flat row. Add rows
  DIRECTLY into people/organizations/places/terms with a re-read-verified one-shot
  script. Notes and figures go through apparatus_merge normally.
- **Glossary `en` must be ASCII (B07 lesson):** check_content matches the glossary
  `en`/`pinyin` against the reading text, which uses plain ASCII apostrophes;
  a curly ' in an `en` field (Jing'an, Ning'er) reads as a displacement. Keep
  `en`/`pinyin` ASCII; curly punctuation belongs only in note bodies (as numeric
  char refs) and is applied at the render layer.
- **Event names stay OUT of the entity-checked glossary (B07 lesson):** a long
  event name with a short handle (全国苏维埃区域代表大会 → "the Congress") triggers
  false check_content displacement in every paragraph that uses the handle. Note
  such events in a footnote; do not add them to glossary.json.
- **Glossary vs check consistency (B05/B06):** set each new glossary row's `en`
  to the form you ACTUALLY render. check_content matches the full capitalised
  `en`; qc_entities is lenient (en / pinyin / first-or-last word).
- **figures.json `file` is a BASENAME**; the builder prepends `data/figs/` and
  `images/`. Figure `before` anchors must fall in the FIRST ~80 chars of a
  paragraph AND the anchor string itself must be short enough to sit in that
  window (keep it under ~55 chars). Note/figure anchors CANNOT sit on a
  `##`/`###` heading line. A full-page line-art figure (a map, a diagram) is a
  legitimate figure with only a caption; find_figures misses these — eyeball
  every page and hand-crop, excluding the printed caption line.
- **Number-check "keep the counted numeral" rule (STYLE.local):** when the source
  counts a NAMED group (两/三/四/十七 + 人/同志/etc. with the members named), keep
  the numeral in English (六大 = "Sixth Congress", 四人 = "four in all", 两人 =
  "the two of them"). Names do not carry the count for the reader OR check_numbers.
- **Inline citation style:** `（作者，年份）` renders inline as `(Author, YEAR)`
  right after the quoted material; multi-author as "(A and B, YEAR)".

## Renderings settled through B07 (also in glossary.json / STYLE.local.md)
- 中央特科 = the Central Special Branch (handle: the Special Branch); 红队 / 打狗队
  = the Red Squad / the dog-beating squad; 中统 = the Zhongtong; 党务调查科 = the
  Party Affairs Investigation Section; 化广奇 = Hua Guangqi (Gu's stage name);
  黎明 = Liming (glossed "the Dawn"). 徐恩曾 = Xu Enzeng, 陈立夫 = Chen Lifu.
- **B07 people (carry forward):** 熊式辉 = Xiong Shihui (the KMT garrison
  commander, this chapter's foil); 李一氓 = Li Yimang; 张文秋 = Zhang Wenqiu;
  林育南 = Lin Yunan; 刘鼎 = Liu Ding; 邹志淑 = Zou Zhishu; 宋再生 = Song Zaisheng
  (Chen Geng's mole); 何长工 = He Changgong; 滕代远 = Teng Daiyuan; 萧克 = Xiao
  Ke; 胡也频 = Hu Yepin; 丁玲 = Ding Ling; 茅盾 = Mao Dun; 尾崎秀实 = Ozaki
  Hotsumi; 左尔格 = Sorge; 赵一曼 = Zhao Yiman (= 李一超 Li Yichao / 李坤泰 Li
  Kuntai); 钱壮飞 = Qian Zhuangfei; 邓发 = Deng Fa.
- **B07 concession geography:** 卡尔登大戏院 = the Carlton Theatre (今长江剧场);
  白克路 = Burkill Road (今凤阳路); 派克路 = Park Road (今黄河路); 卡德路 = Carter
  Road (今石门二路, corrected from "Cardan"); 爱文义路 = Avenue Road (今北京西路);
  赫德路 = Hart Road (今常德路); 麦特赫斯脱路 = Medhurst Road (今泰兴路); 静安寺路
  = Bubbling Well Road; 静安寺 = Jing'an Temple; 跑马厅 = the Racecourse; 洋泾浜 =
  the Yangjingbang; 苏州河 = Suzhou Creek; 黄浦江 = the Huangpu River; 虹口 =
  Hongkou.
- **B07 event/org handles (footnoted, NOT in entity glossary):** 全国苏维埃区域
  代表大会 = the National Congress of Soviet Areas (handle "the Congress"); 苏准会
  = the "Prep Committee"; 苏维埃工农兵代表会议 = the soviet congress of workers,
  peasants, and soldiers. In glossary: 工部局 = the Municipal Council; 公董局 =
  the French Municipal Council; 中华全国总工会 = the All-China Federation of Trade
  Unions; 中国左翼作家联盟 = the League of Left-Wing Writers ("Left League").
- Numbers: full value; 享年X岁 = "at the age of X"; 万 count-unit = full value.
- Spelling locale: AMERICAN (center, color, favor, organize, defense); "the
  Party Center". Comintern (with "Communist International" glossed ch01). British
  spellings in earlier chapters are a known minor inconsistency, dominated by
  American forms; the final whole-book reconcile (check 12) should normalize.

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with
  a sardonic edge and open reverence for his subjects; heat in the verbs and
  rhythm, ration exclamation and rhetorical questions. He does sustained
  SOURCE-CRITICISM (ch06 the first-station address; ch05 the Xiong-Zhu marriage;
  **ch07 the congress venue across six memoirs, and the "Fang Lin = Deng Fa"
  question**): render it as running skeptical argument in plain English, keep the
  sources' own wrong words (the "British Concession"), put the verdict in the
  note (see the new STYLE.local rule). He repeatedly places himself in the story
  as interviewer ("In March 2007 I went to see her...", his own old home on
  Beijing West Road); keep the first person.
- **Martyr set-pieces run at full temperature, verdict in the note:** ch06 the
  prison deaths; ch07 Zhao Yiman's farewell letter to "Ning'er." Do not launder
  the interested-witness framing (日本鬼子 = "the Japanese devils," kept).
- **Zhou Enlai:** warm and big-brotherly with juniors; distinct from the
  martyr-proclamation and deathbed registers. **Chen Geng / Li Qiang / quoted
  memoirists:** clipped and factual. **Gu Shunzhang:** the foil, written hot and
  contemptuous. **Marshals/generals speaking colloquially** (Liu Bocheng in ch07)
  take natural contractions ("that's," "we've").
- (B01-B06 voice sheets for the Party leaders in committee, the Xiong-Zhu couple,
  the radio men, etc. still stand for reruns.)

## Where the story stands
Chapters One-Two founded the Special Branch and drew the moral contrast; Three
("Who Is Judas") ran the first betrayal (Luo Yinong); Four ("Bloodshed on Avenue
Joffre") the double-agent thread (Bai Xin); Five ("A Real Vault, a False
Marriage") the Party's safe-house machinery (the Xiong-Zhu couple); Six ("It Was
Not Me, It Was the Wind") the radio and the martyrs. Seven ("The Great Hermit
Hides in the City") is the counter-intelligence set-piece: how the Special Branch
hid the 1930 National Congress of Soviet Areas inside a fake hospital behind the
Carlton Theatre in the International Settlement, ran a fake birthday party as
cover, built a jump-across escape route, and — through Chen Geng's mole Song
Zaisheng inside Xiong Shihui's own men — foiled the raid; it closes on Zou
Zhishu, killed later by Gu Shunzhang, and her contested memory. Chapter Eight,
"A Nanjing Night, Deadly Urgent," turns to the Party's three agents inside the
KMT intelligence service and Qian Zhuangfei's decoding of Gu Shunzhang's
defection cables — the warning that saved the Shanghai underground.

## Next-batch scope
B08 = ch08, PDF 172-207 (printed 157-192), ten sections ch08s01-s10 (openers at
PDF 173,176,183,186,188,194,196,200,203,204). A large chapter. Expect figures
(eyeball every page; find_figures misses line art and dense newsprint) and heavy
quoted-memoir material.

## Open traps / environment
- `data/zh/` is gitignored (copyright); a fresh checkout cannot regenerate the
  hand-transcribed sources. Use per-unit `check_structure --pairs` /
  `verify_unit.py`.
- `find_figures.py` misses dense-newsprint clippings and line-art diagrams (ch07
  had a full-page street map it would skip); eyeball every page and hand-crop.
  When cropping a captioned photo, exclude the printed caption line. Washed-out
  full-page chapter-divider illustrations (e.g. p0150) are design furniture, not
  captioned figures.
- `tests/run_tests.py` "hook stands down on template stub" FAIL is benign (a real
  kickoff is present). setup.sh prints "CHECKER REGRESSION TESTS FAILED" for this
  one line only; ignore it.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; verify `pgrep -c tesseract` = 0
  after OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch; the
  B01-B07 decided renderings are in glossary.json and listed above.
- The Preface (ch00, PDF 6-15) is still UNTRANSLATED; it and the back matter
  (Works Cited ch16, Afterword ch17) fold into the final batches.
- Branch hygiene: the canonical branch is `claude/the-sword-roars`. The harness
  may start a session on a stray per-task branch; consolidate onto the canonical
  branch and delete the stray (local + remote) per CLAUDE.md rule 2. (B07 started
  on a stray `claude/sword-roars-ch07-*`, which held no unique commits;
  consolidated onto claude/the-sword-roars and the stray was already gone from
  the remote.)
