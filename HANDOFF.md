# HANDOFF — The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start Batch 9. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch08's English first.

```
Sword Roars B09

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2). Run ./setup.sh first.

Do Batch 9 = Chapter Nine, "向忠发失踪之谜 / The Riddle of Xiang Zhongfa's
Disappearance" (ch09), PDF 208-235, printed 193-220, end to end per the pipeline
in CLAUDE.md. Nine sections: ch09s01 一、探勒车行 (PDF 209, printed 194),
ch09s02 二、那人只有九个指头 (PDF 210, printed 195), ch09s03 三、传话的"印象最深"
(PDF 214, printed 199), ch09s04 四、直接用钥匙开门 (PDF 216, printed 201),
ch09s05 五、我们的思想是相通的 (PDF 220, printed 205), ch09s06 六、通缉与卖人
(PDF 225, printed 210), ch09s07 七、脚下是一个陷阱 (PDF 229, printed 214),
ch09s08 八、屈膝跪地为免一死 (PDF 231, printed 216), ch09s09 九、"密电"依然"存在"
(PDF 233, printed 218). Simplified Chinese, horizontal; OCR chi_sim --psm 6;
crop --left 0.06 --right 0.95 --top 0.11 --bottom 0.955; offset is a constant 15
(printed = pdf - 15), no plate drift, but READ each opener's folio off the scan.

BEFORE translating, read the final two pages of Chapter Eight's English
(out/ch08_reading.md) so the voice carries over unbroken. Chapter One remains
the FROZEN register reference: run check_register.py --ref out/ch01_reading.md
on ch09 and record it (judge on the narratorial signals per
references/register-drift.md; the dialogue-contraction metric moves with how
dialogue-heavy the chapter runs, and is not itself drift). Chapters One-Eight's
data/zh were hand-transcribed off the scans (OCR too noisy on the proper names,
and direct reading of the 300-DPI page images is the reliable method); do the
same for ch09. In the hand-transcribed data/zh/ch09.txt mark the chapter title
with ### (same prefix as the section heads), NOT ##. Cite printed folios in
notes, never PDF pages. Never invent bridging text: if OCR breaks mid-sentence
or a leaf is damaged, crop the scan and read the real continuation, or footnote
the gap. Verify every name, number and low-confidence span against a magnified
crop before writing. Consult authority.json and glossary.json for settled
renderings (esp. the Central Special Branch, the Red Squad, the Zhongtong, the
Party Affairs Investigation Section, Zhou Enlai, Gu Shunzhang, Chen Geng,
Chiang Kai-shek, and from Ch.8: Xu Enzeng, Chen Lifu, Qian Zhuangfei, Li Kenong
[NOT in the entity glossary], Hu Di [NOT in glossary], Hua Guangqi = Gu's stage
name, Liming = Gu's alias, Cai Mengjian, the "Three Heroes of Longtan," the
Zhengyuan Industrial Company). This chapter is the sequel to Gu Shunzhang's
defection: 向忠发 Xiang Zhongfa, the CCP's General Secretary, is captured and
executed in Shanghai in June 1931; the chapter weighs the sources on how he was
caught (顾顺章 Gu Shunzhang's leads, the 探勒车行 "Delle Motor Garage," the
nine-fingered man), whether he broke under interrogation and knelt to beg for
his life, and the disputed "secret cable." Expect heavy source-criticism (render
it as running skeptical argument, verdict in the note) and a fresh cast. Add
ch09 to data/content_config.json when you translate it, or the displacement
check silently skips it.

Deliver the built EPUB attached in the chat, and paste the Batch 10 kickoff
verbatim in the same reply.
```

## DONE (one line per batch; do not redo)
- Survey: structure, offsets, style contract, skeleton EPUB. (earlier session)
- **B01 = ch01 (voice gate):** 165 paragraphs, 115 footnotes, 12 figures,
  glossary seeded, all checks green, epubcheck clean, blind-critique loop run,
  passed the human voice gate.
- **B02 = ch02:** 56 paragraphs, 28 footnotes, 5 figures, 14 new glossary rows.
- **B03 = ch03 "Who Is Judas":** 146 paragraphs, 33 footnotes, 4 figures.
- **B04 = ch04 "Bloodshed on Avenue Joffre":** 131 paragraphs, 24 footnotes, 10 figures.
- **B05 = ch05 "A Real Vault, a False Marriage":** 66 paragraphs, 27 footnotes, 5 figures.
- **B06 = ch06 "It Was Not Me, It Was the Wind":** 165 paragraphs, 28 footnotes, 3 figures.
- **B07 = ch07 "The Great Hermit Hides in the City":** 99 paragraphs, 20 footnotes,
  6 figures. GLOBAL fix: 卡德路 "Cardan"→"Carter Road".
- **B08 = ch08 "A Nanjing Night, Deadly Urgent":** 252 paragraphs (the Qian
  Zhuangfei warning), 21 footnotes, 4 figures, 43 new glossary rows; parity
  252=252, numbers 0, align/content/entities clean, register within tolerance
  (dialogue metric high but correct, memoir-interview-heavy), qa_epub PASS
  (296 notes total), epubcheck 0/0. Details in PROGRESS.md.

## Tooling in place — DO NOT REVERT
- `scripts/indents.py`: furniture-band drop by y-position (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`).
- `scripts/check_numbers.py`: arabic+万 combiner BEFORE the noise loop; matches
  English number-WORDS, ordinals, and MONTH NAMES.
- `build_reading_epub.py` alt-attribute escaping (fixed B04): figure `alt` through
  `html.escape(..., quote=True)`. Prefer single quotes in alt.
- `data/noise.txt`: this book's event-date names, numeral-bearing proper names,
  decade labels, idioms. B02-B08 blocks appended. **B08 block:** 张万栋, 万状,
  百昌, 千奇百怪, 百计, 千计, 六安, 九旬, 接二连三, 九江, 星期六, 垂涎三尺,
  三四十年代, 万安 (each strips a SOURCE numeral carrying no cardinal quantity: a
  name/place with a word-internal digit, an idiom, or a rounded rhetorical form
  the English already carries). Extend per its header; longest literal first.
- `data/content_config.json`: docs+sources map for check_content; now covers
  ch01-ch08. ADD ch09 when you translate it. Run check_content with
  `--config data/content_config.json`.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Transcription method (confirmed B08):** ocr_dual.py produces nothing directly
  consumable here; the reliable path is to READ the 300-DPI page images
  (data/png/p####.png) directly and transcribe, cropping tight regions
  (a 6-line PIL helper) only for genuinely ambiguous names/numbers. OCR text is a
  cross-check, not the source of truth.
- **Parity gotcha (B05-B08):** in `data/zh/chNN.txt` mark the chapter title `### `
  (same prefix as section heads), NOT `## `. On the English side
  (`out/chNN_reading.md`) the chapter title is `## `, section heads `### `.
- **Section-boundary editing gotcha (B08):** when appending sections to the
  reading file by Edit, DO NOT anchor a later section's edit on the LAST paragraph
  of the previous section unless that paragraph is truly its tail; a mid-append
  can orphan the section's remaining paragraphs to the end of the file. After the
  full draft, run the per-section count (zh sections[1:] vs en sections) to catch
  it before check_structure only reports the TOTAL.
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the
  JSON TOP LEVEL; the builder's render_glossary needs them under
  people/organizations/places/terms. Add rows DIRECTLY into those sub-objects with
  a re-read-verified one-shot script (see data/ch08_glossary_add.json + the
  scratchpad merge script). Notes and figures go through apparatus_merge normally.
- **Glossary `en` must be ASCII;** curly punctuation only in note bodies (numeric
  char refs) applied at the render layer.
- **Event names stay OUT of the entity-checked glossary** (false displacement).
- **VERY high-frequency recurring names with pronoun runs stay OUT of the entity
  glossary** (B08 confirmed for 李克农/胡底): adding them fires false
  check_content displacement across the whole book. Render consistently and rely
  on qc_entities' leniency; only add names whose English form reliably appears
  wherever the hanzi does.
- **figures.json `file` is a BASENAME**; builder prepends `data/figs/`. `before`
  anchors fall in the FIRST ~80 chars of a paragraph and the anchor string is
  under ~55 chars; cannot sit on a `##`/`###` heading. Match the anchor's exact
  punctuation (straight quotes) to the reading file. Full-page line-art/document
  figures (a map, an archive table) are legitimate figures with only a caption;
  find_figures misses these, so eyeball every page and hand-crop, excluding the
  printed caption line.
- **Washed-out full-page chapter-divider illustrations** (ch07 p0150, ch08 p0207)
  are design furniture, NOT captioned figures. Exclude them.
- **Number-check "keep the counted numeral" rule (STYLE.local):** when the source
  counts a NAMED group, keep the numeral in English.
- **Inline citation style:** `（作者，年份）` renders inline as `(Author, YEAR)`.
- **Set-off block quotes render `{v}`** (one source line, marker only on the
  English side; parity still holds). **Verse renders `{p}`, one line per source
  line** (first used B08 for the Internationale).

## Renderings settled through B08 (also in glossary.json / STYLE.local.md)
- 中央特科 = the Central Special Branch (handle: the Special Branch); 红队 / 打狗队
  = the Red Squad / the dog-beating squad; 中统 = the Zhongtong; 党务调查科 = the
  Party Affairs Investigation Section (handle: the Investigation Section);
  化广奇 = Hua Guangqi (Gu's stage name; archive spells it 化光奇); 黎明 = Liming.
- **B08 core cast (carry forward):** 徐恩曾 Xu Enzeng; 陈立夫 Chen Lifu (二陈 = the
  two Chens, the CC Clique); 钱壮飞 Qian Zhuangfei; 李克农 Li Kenong and 胡底 Hu Di
  (the other two of the 龙潭三杰 "Three Heroes of Longtan"; NOT in entity glossary);
  蔡孟坚 Cai Mengjian (the KMT interrogator, self-serving memoir); 顾顺章 Gu
  Shunzhang; 陈云 Chen Yun; 张国焘 Zhang Guotao; 董健吾 Dong Jianwu; 聂荣臻 Nie
  Rongzhen; 邹韬奋 Zou Taofen; 宋庆龄 Song Qingling; 魏斐德 Wakeman; 鲍罗廷 Borodin.
  Family interviewees (colloquial voices): 钱泓 Qian Hong, 李力 Li Li, 李仑 Li Lun,
  聂力 Nie Li, 董惠芳 Dong Huifang, 黎莉莉 Li Lili.
- **B08 orgs:** 正元实业社 the Zhengyuan Industrial Company; 长江通讯社 the Yangtze
  News Agency; 民智通讯社 the Minzhi News Agency; 长城通讯社 the Great Wall News
  Agency.
- Numbers: full value; 享年X岁 = "at the age of X"; 万 count-unit = full value.
- Spelling locale: AMERICAN (center, color, favor, organize, defense); "the Party
  Center." Comintern (with "Communist International" glossed ch01).

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with a
  sardonic edge and open reverence for his subjects; heat in the verbs and rhythm,
  ration exclamation and rhetorical questions. He does sustained SOURCE-CRITICISM
  (ch06 the first-station address; ch07 the congress venue; **ch08 the Wuhan
  "assassinate Chiang" question, whether Qian Zhuangfei really dawdled, and the
  three rival accounts of Qian's death**): render it as running skeptical argument
  in plain English, keep the sources' own wrong words, put the verdict in the note.
  He places himself in the story as interviewer (Dong Huifang in the nursing home);
  keep the first person.
- **Martyr set-pieces run at full temperature, verdict in the note:** ch06 the
  prison deaths; ch07 Zhao Yiman; **ch08 the two heroes singing the Internationale
  in the burning Hankou house, and Zhou Enlai weeping over Qian Zhuangfei's bound,
  stabbed body.** Do not launder the interested-witness framing (匪 "bandit,"
  叛徒 "renegade," kept as the sources' words).
- **Zhou Enlai:** warm and big-brotherly; distinct from martyr-proclamation and
  deathbed registers. **Gu Shunzhang:** the foil, written hot and contemptuous
  (the drunken Hankou scene, the arrogance). **Cai Mengjian / KMT memoirists:**
  officialese, self-congratulatory; keep the pomp so the reader hears the
  self-regard. **Party leaders / descendants in interview:** clipped, factual,
  colloquial and contracted.
- (B01-B07 voice sheets still stand for reruns.)

## Where the story stands
Chapters One-Two founded the Special Branch and drew the moral contrast; Three
("Who Is Judas") ran the first betrayal; Four ("Bloodshed on Avenue Joffre") the
double-agent thread; Five ("A Real Vault, a False Marriage") the safe-house
machinery; Six ("It Was Not Me, It Was the Wind") the radio and the martyrs;
Seven ("The Great Hermit") the 1930 congress hidden in a fake hospital. Eight
("A Nanjing Night, Deadly Urgent") is the great counter-stroke: the three Party
agents (Qian Zhuangfei, Li Kenong, Hu Di) planted inside Xu Enzeng's Kuomintang
intelligence service; Gu Shunzhang's arrest and defection in Wuhan; Qian
Zhuangfei's overnight decoding of Cai Mengjian's cables and his knife-slashed
warning; Zhou Enlai's emergency evacuation of the whole Shanghai underground; and
Qian Zhuangfei's death on the Long March in 1935. Chapter Nine, "The Riddle of
Xiang Zhongfa's Disappearance," is the direct sequel: Gu Shunzhang's defection
exposes the CCP General Secretary Xiang Zhongfa, who is caught and executed in
Shanghai in June 1931, and the chapter weighs the contested sources on how he
fell and whether he broke.

## Next-batch scope
B09 = ch09, PDF 208-235 (printed 193-220), nine sections ch09s01-s09 (openers at
PDF 209,210,214,216,220,225,229,231,233). Expect figures (eyeball every page;
find_figures misses line art and dense newsprint) and heavy source-criticism.

## Open traps / environment
- `data/zh/` is gitignored (copyright); a fresh checkout cannot regenerate the
  hand-transcribed sources. Use per-unit `check_structure --pairs` /
  `verify_unit.py`.
- `find_figures.py` misses dense-newsprint clippings and line-art/document images;
  eyeball every page and hand-crop, excluding the printed caption line.
- `tests/run_tests.py` "hook stands down on template stub" FAIL is benign (a real
  kickoff is present). setup.sh prints "CHECKER REGRESSION TESTS FAILED" for this
  one line only; ignore it.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; verify `pgrep -c tesseract` = 0
  after OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch; the
  B01-B08 decided renderings are in glossary.json and listed above.
- The Preface (ch00, PDF 6-15) is still UNTRANSLATED; it and the back matter
  (Works Cited ch16, Afterword ch17) fold into the final batches.
- Branch hygiene: the canonical branch is `claude/the-sword-roars`. The harness
  may start a session on a stray per-task branch; consolidate onto the canonical
  branch and delete the stray (local + remote) per CLAUDE.md rule 2. (B08 started
  on a stray `claude/sword-roars-chapter-eight-*` that carried all prior work at
  origin/the-sword-roars's tip; consolidated onto claude/the-sword-roars and the
  stray was deleted, local; it was never on the remote.)
