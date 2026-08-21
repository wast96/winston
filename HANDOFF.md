# HANDOFF: The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start the next batch. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch13's English (and ch01, the
> frozen register reference) before drafting ch14.

```
Sword Roars B16 Chapter Fourteen

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. In STYLE.local.md the top section "THE REGISTER REBASELINE
(B09 commissioner review)" and the "Footnote apparatus" and "Apparatus policy"
sections are the frozen reference for all further work. Work on branch
claude/the-sword-roars (the canonical book branch; if the harness starts you on
a stray per-task branch, consolidate per CLAUDE.md rule 2 and delete the stray,
local and remote). Run ./setup.sh first.

STATE: B15 is done. Chapter Thirteen ("Twin Lotus on One Stem," ch13, PDF 284-307,
printed 269-292, 139 paragraphs, 5 sections) is drafted end to end against the frozen
doc: hand-transcribed off the 300-DPI images (OCR too noisy on the names), rendered in
ch08-ch12's sardonic source-criticism register — the story of Shen Anna (沈安娜, born
沈琬 Shen Wan), the CCP stenographer-mole, and her husband Hua Mingzhi, the "twin lotus"
married intelligence pair: her recruitment as a Zhejiang-government stenographer; the Red
Army Advance/Vanguard Column (粟裕/刘英) her intel supported after Fang Zhimin's force fell
at Mount Huaiyu; her infiltration of the KMT Central Party HQ secretariat via patron Zhu
Jiahua (taking the minutes at Chiang's secret meetings); the three-year loss of contact
after handler Xu Zhonghang's 1942 arrest; Wu Kejian's 1945 reconnection and the late-war
windfall haul, to her deathbed murmur. The author weighs the memoir (Shen Anna 2016/2007),
Liu Ying's essay, a KMT internal document and Chiang's Draft Chronicle against one another.
17 footnotes (book total 383), 4 hand-cropped figures, ~73 new glossary rows, ch13 added to
data/content_config.json. Two tooling patches (DO NOT REVERT): data/noise.txt got a B15
event-name/idiom block; the glossary now carries a `pinyin` field on every row (72 back-filled
pinyin=en) — qc_entities Keyerrors on a row without one, so NEW rows must include `pinyin`.
All checks green: parity 139=139, numbers 0 unresolved, content/entities clean, qa_epub PASS,
epubcheck 0/0/0/0, register within tolerance of ch01 (no stilted flag). See PROGRESS.md "B15"
for the "NOT re-noted" list, the settled renderings, and the standing sweep items.

This batch's job: DRAFT CHAPTER FOURTEEN (ch14, "Secret Number One," 第十四章 "一号机密",
PDF 308-323, printed 293-308, 6 sections: s1 一、中央文库 "The Central Archive" PDF 309,
s2 二、决不让一个纸片落到敌人手里 "Not One Scrap of Paper to Fall into Enemy Hands" PDF 312,
s3 三、我不死，我还要工作 "I Will Not Die; I Still Have Work to Do" PDF 313, s4 四、"小老大"
"The Little Boss" PDF 316, s5 五、让自己永远沉默 "To Silence Herself Forever" PDF 318, s6 六、
档归我们天下 "The Archive Comes Home to Us" PDF 321) end to end against the frozen doc. Offset
a constant 15 (printed = pdf - 15); read each opener's folio off the scan. Re-render and
re-OCR (data/png and data/zh are gitignored, gone on a fresh checkout): render.py 308 323
--dpi 300, then ocr_crop.py 308 323 --left 0.06 --right 0.95 --top 0.11 --bottom 0.955
--lang chi_sim --psm 6. OCR is TOO NOISY on the proper names, so HAND-TRANSCRIBE
data/zh/ch14.txt off the 300-DPI page images directly (data/png/p####.png), one paragraph
per line, chapter title and section heads as ### (the B08/B11/B12/B13/B15 method; OCR is a
cross-check, not the source). The chapter divider (PDF 308) and any washed-out full-page
painting are design furniture, not captioned figures; watch for FULL-PAGE DOUBLE PLATES
(pages of photos with captions but no body text — zero paragraphs, as ch13's p0297 was);
eyeball every page for real photos/line art and hand-crop any (exclude the printed caption,
translator's caption with source-label provenance, real alt text). Numerals in unit/place
designations are load-bearing — crop-verify them. Add ch14 to data/content_config.json.

BEFORE translating, read the final two pages of ch13's English (the voice). Read
the zh against the en on every line; change register, never meaning; invent
nothing (CLAUDE.md rule 4; verify the TAIL of the unit explicitly against the
scan). Cite printed folios, never PDF pages. Then footnotes at reader-model
density (consult the "NOT re-noted" lists in PROGRESS; grep notes.json before
adding); glossary rows straight into the sectioned ledger (en ASCII only, WITH a
`pinyin` field), consulting authority.json first; flag any NEW recurring institutional term
recurring:true and any NEW concession street gazetteer:true+today. Run
check_structure --pairs (SOURCE first: data/zh/ch14.txt out/ch14_reading.md),
verify_unit, make_bilingual + qc_entities, check_align, check_content --config
data/content_config.json, apparatus_merge + check_apparatus, and check_register
--ref out/ch01_reading.md (informational). Rebuild, run qa_epub and epubcheck (jar
at /tmp/epubcheck-5.1.0/epubcheck.jar).

Do it end to end; do not pause for approval. Deliver the rebuilt EPUB attached in
the chat, and paste the next kickoff verbatim in the same reply.
```

## DONE (one line per batch; do not redo)
- Survey: structure, offsets, style contract, skeleton EPUB. (earlier session)
- **B01 = ch01 (voice gate):** 165 paragraphs, blind-critique loop, human gate.
- **B02 = ch02:** 56. **B03 = ch03:** 146. **B04 = ch04:** 131. **B05 = ch05:** 66.
  **B06 = ch06:** 165. **B07 = ch07:** 99. **B08 = ch08:** 252.
- **B09 review:** register-rebaseline style doc + itemized corrections ch01-ch08.
- **B09 continuation:** register de-archaizing pass over ch01-ch08; dates
  month-day-year book-wide.
- **B10:** two builder features (Glossary of Recurring Terms + Street Gazetteer);
  footnote placement sweep; ch01 thinned; ch07/ch08 backfilled; spine-test pass; 290 notes.
- **B11 = ch09:** "The Riddle of Xiang Zhongfa's Disappearance," 194 paragraphs, 9
  sections; 27 notes (book 317), 5 figures, 95 glossary rows; 善钟路 -> gazetteer.
- **B12 = ch10:** "Opening a Shop, Doing Trade," 39 paragraphs, 2 sections; 15 notes
  (book 332), 3 figures, 101 glossary rows; 华润 = "Huarun" (glossed China Resources).
- **B13 = ch11:** "The Wild Swan," 82 paragraphs, 3 sections, PDF 248-263. Hand-transcribed;
  19 notes (book 351), 3 figures, 108 glossary rows; 薛华立路 -> gazetteer; check_content
  HOMOGRAPHS patch (严重).
- **B14 = ch12:** "A Purge in the Red-Light District," 139 paragraphs, 7 sections, PDF
  264-283. Hand-transcribed; 15 notes (book 366), 2 figures, 75 glossary rows; 四马路 -> Sima
  Road (gazetteer); qc_entities HOMOGRAPHS patch (严重, mirrors check_content).
- **B15 (this batch) = ch13:** "Twin Lotus on One Stem," 139 paragraphs, 5 sections, PDF
  284-307. Hand-transcribed; ch08-ch12 source-criticism register; 17 notes (book 383), 4
  figures, ~73 glossary rows; glossary `pinyin`-field back-fill (qc_entities needs it);
  B15 noise block (event-name/idiom numerals). Shen Anna / Hua Mingzhi "twin lotus" story.
  All checks green, epubcheck 0/0/0/0, register no stilted flag. See PROGRESS.md "B15".
  ch14-ch15, the Preface, and back matter remain.

## Tooling in place (DO NOT REVERT)
- **build_reading_epub.py:** `render_recurring` (Glossary of Recurring Terms),
  `render_gazetteer` (Street Gazetteer), `_walk_flagged`, `.gaz` CSS; both back-matter
  pages wired into spine/nav/ncx and rendered only when their data exists. Book/periodical
  titles are italicized in a reading file via `*...*` -> `<i>...</i>` (line ~553); ch10-ch13
  render titles PLAIN (no markup) while ch01/ch08/ch09 italicize — a reconciliation-sweep item.
- **check_content.py:** `AUTHOR` set (author self-naming) AND `HOMOGRAPHS` set: 严重 = the
  ch10 courier "Yan Zhong" but also the adjective "severe"; excluded from the content name-map.
- **qc_entities.py:** the SAME `HOMOGRAPHS = {"严重"}` stoplist. Keep the two lists in sync.
  It reads `rec["pinyin"]` for every glossary row, so **every glossary row must have a
  `pinyin` field** (B15 back-filled `pinyin = en` on the 72 rows that lacked one).
- Register-pass drivers: `edits/chNN_edits.md` + `scripts/apply_edits.py`;
  `scripts/anchor_check.py`.
- `scripts/indents.py`: furniture-band drop (FURNITURE_TOP=0.11, BOTTOM=0.955).
- `scripts/check_numbers.py`: arabic+万 combiner before the noise loop.
- `data/noise.txt` carries B02-B15 blocks (longest literal first); the B15 block adds
  九一八, 八一三 (event-date names spelled out in English), 万人空巷, 万不可, 万变, 千里迢迢
  (idioms), 五云山 (place), 华韵三, 鸣三 (personal-name numerals).
- `data/content_config.json`: docs+sources map for check_content, ch01-ch13. ADD ch14.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Transcription method (B08, confirmed again B15):** OCR is too noisy on the proper
  names; READ the 300-DPI page images (data/png/p####.png) directly and transcribe,
  cropping tight regions only for ambiguous names/numbers.
- **Parity gotcha:** in `data/zh/chNN.txt` mark the chapter title `### ` (like section
  heads), NOT `## `. English side: chapter title `## `, section heads `### `. AND run
  check_structure --pairs with the SOURCE file FIRST: `data/zh/chNN.txt out/chNN_reading.md`.
- **Full-page double plates:** a page can be TWO captioned photos with NO body text (ch13
  p0297). Its paragraph count is zero; do not invent paragraphs for it. Count body paras off
  the actual prose, not the page count.
- **Glossary placement gotcha:** glossary.json is a DICT keyed by hanzi under
  people/organizations/places/terms. Add rows directly into the sub-objects (each row: `en`
  ASCII, `pinyin`, `status`, optional `note`). Where the prose uses a SHORT form, set `en`
  to it so the substring test in check_content/qc_entities passes: e.g. 华明之 -> "Mingzhi",
  中西功 -> "Nakanishi", 邓肯 -> "Duncan", 怀玉山 -> "Huaiyu" (full form still at first mention).
- **check_content full-name-vs-surname trap:** a glossary `en` of the full name fails when
  the body uses only the surname; set the glossary `en` to the SHORT form actually used.
- **VERY high-frequency recurring names with pronoun runs, and name/common-word
  homographs**, stay OUT of the entity glossary (or go in the HOMOGRAPHS stoplist in BOTH
  check_content and qc_entities).
- **figures.json `file` is a BASENAME**; builder prepends `data/figs/`. `before` anchors
  fall in the FIRST ~80 chars of a paragraph, cannot sit on a heading.
- **Washed-out full-page divider/illustration pages** are design furniture, NOT captioned
  figures (exclude them; ch13's is p0284 the divider).
- Set-off block quotes render `{v}`; verse `{p}`; dateline `{d}`; `check_structure.py`
  strips markers before parity. ch10-ch13 used ZERO markers — cited memoir/document passages
  read cleanly as normal paragraphs with a "(Name, year)" attribution or a colon lead-in. A
  standalone "……" memoir elision is rendered as a single ellipsis line (parity-locked).

## Apparatus state after B15 (frozen doc = STYLE.local top sections)
- 383 notes (ch09 +27, ch10 +15, ch11 +19, ch12 +15, ch13 +17). Densities taper as the
  book's furniture gets covered; ch13 ran reference-dense (whole new Shen Anna cast, plus the
  Red Army Advance Column and the KMT-document source-criticism). A modest new-note count is
  healthy for ch14 (the Central Archive story reuses much established furniture).
- The Glossary of Recurring Terms and Street Gazetteer carry the recurring furniture and the
  concession streets; gloss such terms ONCE at first appearance and let the back matter carry
  the rest. When drafting ch14, flag any NEW recurring institutional term `recurring:true`
  and any NEW concession street `gazetteer:true`+`today`.
- Marker placement: put a marker at the end of the clause/sentence that holds the referent,
  never mid-phrase (right after a complete referent noun-phrase is fine).

## Renderings settled (also in glossary.json / STYLE.local.md)
- Consistency canon (verified clean): Center (not Centre), the Politburo, the White Terror,
  the Xujiahui Observatory, Lazily Seeking Old Dreams, fused lane names, the ten-li foreign
  quarter, presiding pastor. Dates month-day-year. Spelling: AMERICAN.
- 中央特科 the Central Special Branch (handle: the Special Branch); 红队 / 打狗队 the Red
  Squad / the dog-beating squad; 中统 the Zhongtong; 华润 Huarun (China Resources).
- **Numbered Shanghai avenues = pinyin:** 四马路 Sima Road (today Fuzhou Road), 三马路 Sanma
  Road. ch09 para 163 has the ONE outlier "Fourth Avenue" -> fix to "Sima Road" in the sweep.
- B15 additions (full list in PROGRESS "B15"): the Shen Anna intelligence ring (沈安娜 Shen
  Anna / 沈琬 Shen Wan; 华明之 "Mingzhi"; 舒曰信 Shu Yuexin; 沈伊娜 Shen Yina; 鲁自诚 Lu Zicheng;
  华韵三 Hua Yunsan; 姚子健 Yao Zijian; 吴克坚 Wu Kejian; 徐仲航 Xu Zhonghang), the KMT patrons
  (朱家骅 Zhu Jiahua; 甘乃光 Gan Naiguang; 吴铁城 Wu Tiecheng), the Red Army Advance Column cast
  (粟裕 Su Yu; 刘畴西 Liu Chouxi; 方志敏 Fang Zhimin; 宗孟平 Zong Mengping; 黄绍竑 Huang Shaohong),
  and 中西功 Nakanishi, 阎宝航 Yan Baohang, 邓肯 Duncan. Institutions: 挺进师 the Vanguard Column;
  新四军 New Fourth Army (recurring); 八路军办事处 Eighth Route Army Office (recurring); 中央社会部
  Central Social Affairs Department (recurring); 中共南方局 CCP Southern Bureau (recurring).
- Consult authority.json before romanizing (Zhou Enlai, Mao Zedong, Dong Biwu, Chiang
  Kai-shek, Deng Yingchao, Bo Gu, Li Kenong, Ye Jianying, Lin Boqu, Fang Zhimin, Guo Moruo,
  Lu Xun all confirmed shelf-wide).

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with a sardonic
  edge; heat in the verbs and rhythm, ration exclamation and rhetorical questions; sustained
  source-criticism as running skeptical argument in plain English, sources' own words kept,
  verdict in the note; first person kept where he places himself as interviewer/reader of the
  archive. In ch13 he sets Shen Anna's memoir, Liu Ying's essay, the KMT internal directive
  and Chiang's Draft Chronicle against one another; preserve that argumentative motion.
- **Interviewee memoir voice runs at natural, contracted, spoken register.** Shen Anna's
  first-person account (2007/2016) is the ch13 type specimen: contractions, plain syntax,
  present feeling. ch14 turns to the Central Archive and its keepers (Chen Wei, Zhang
  Weizhen, Chen Laisheng, "the Little Boss") — same interviewee-heat and martyr set-pieces;
  keep the temperature, verdict in the note, do not iron flat.
- **Zhou Enlai** warm and big-brotherly; **Party leaders / descendants / martyrs in
  interview** clipped, factual, contracted; **KMT memoirists / officials** officialese,
  self-regarding; **quoted 1930s-40s documents** (resolutions, directives, Chiang's records)
  stay starchy and formal — that is period work and is correct.

## Where the story stands
Chapters One-Thirteen are drafted. Chapter Twelve returned to the Special Branch's
counter-traitor killings; Chapter Thirteen, "Twin Lotus on One Stem," told the long story of
the stenographer-mole Shen Anna and her husband Hua Mingzhi. Chapter Fourteen, "Secret Number
One" (ch14, PDF 308-323), is next: six sections on the Central Archive (中央文库) — the Party's
secret document repository — and those who guarded it (中央文库 "The Central Archive," 决不让一个
纸片落到敌人手里 "Not One Scrap of Paper to Fall into Enemy Hands," 我不死，我还要工作 "I Will Not
Die; I Still Have Work to Do," "小老大" "The Little Boss," 让自己永远沉默 "To Silence Herself
Forever," 档归我们天下 "The Archive Comes Home to Us"). Read the ch08-ch13 source-criticism voice
sheet forward.

## Open traps / environment
- `data/zh/` and `data/png/` are gitignored; a fresh checkout has neither. ch14 drafting
  needs both (render + hand-transcribe from source.pdf, which IS tracked). The tracked
  deliverables (out/chNN_reading.md, notes/glossary/figures, the built EPUB) are complete.
- Cross-check note AND figure anchors before any re-voicing edit (scripts/anchor_check.py).
  A broken figure `before` anchor fails the build. Note anchors must match the reading file
  byte-for-byte INCLUDING inner punctuation (a comma sitting inside quotes, e.g. `"August
  Thirteenth,"`, must be in the anchor).
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; `pgrep -c tesseract` = 0 after OCR (ocr_crop
  exits 1 when the final `pgrep -c` finds 0 processes — that is SUCCESS, not failure).
  epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch.
- **ch01-ch09 cleanup-sweep worklist (do at the end, not mid-batch):** (1) ch01 Yang Du
  note birth year "1875" -> "1874"; (2) ch09 para 163 "Fourth Avenue" -> "Sima Road" for
  四马路; (3) book-wide title-italics decision (ch10-ch13 plain vs ch01/ch08/ch09 italic).
- Still UNTRANSLATED: ch14-ch15, the Preface (ch00, PDF 6-15), and back matter (Works Cited
  ch16, Afterword ch17). They fold into later batches.
- Branch hygiene: canonical branch is `claude/the-sword-roars`. B15 started on a stray
  `claude/sword-roars-b15-ch13-a5naf5` (the remote-tracking ref was stale; the branch was not
  actually on origin); consolidated onto canonical, stray pruned local and remote.
