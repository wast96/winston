# HANDOFF: The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start the next batch. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch14's English (and ch01, the
> frozen register reference) before drafting ch15.

```
Sword Roars B17 Chapter Fifteen

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. In STYLE.local.md the top section "THE REGISTER REBASELINE
(B09 commissioner review)" and the "Footnote apparatus" and "Apparatus policy"
sections are the frozen reference for all further work. Work on branch
claude/the-sword-roars (the canonical book branch; if the harness starts you on
a stray per-task branch, consolidate per CLAUDE.md rule 2 and delete the stray,
local and remote). Run ./setup.sh first.

STATE: B16 is done. Chapter Fourteen (""Secret Number One"," ch14, PDF 308-323,
printed 293-308, 66 paragraphs, 6 sections) is drafted end to end against the frozen
doc: hand-transcribed off the 300-DPI images (OCR too noisy on the names), rendered in
the ch08-ch13 sardonic source-criticism register. It is the story of the Central Archive
(中央文库), the Party's first secret document repository, and the chain of keepers who
guarded it through terror, war and occupation: Zhang Weiyi (founder 1930), Ling Bing,
Chen Weiren (the tubercular hero, died 1937), Miao Guren ("a second Chen Weiren," died
1944) and Chen Laisheng, who handed it over intact in 1949 (it entered the Central
Archives in 1959). Woven in: Pan Hannian's South China Intelligence Bureau; the courier
Zheng Wendao, who killed himself under arrest rather than betray Nakanishi; and the Sorge
/ "Ramsay" ring's 1941 fall in Tokyo. The chapter opens on the renegade Luo Zhanglong's
venom and turns it against him. 12 footnotes (book total 395), 7 hand-cropped figures,
~65 new glossary rows, ch14 added to data/content_config.json. Tooling patch (DO NOT
REVERT): data/noise.txt got a B16 name-numeral block (瘰三, 立三, 陈三百). No script changes.
All checks green: parity 66=66, numbers 0 unresolved, content/entities clean, qa_epub PASS,
epubcheck 0/0/0/0, register within tolerance of ch01 (no stilted flag). See PROGRESS.md "B16"
for the "NOT re-noted" list, the settled renderings, and the standing sweep items.

This batch's job: DRAFT CHAPTER FIFTEEN (ch15, "The Last Effort," 第十五章 "最后的努力",
PDF 324-337, printed 309-322, 4 sections: s1 一、陈云来了 "Chen Yun Arrives" PDF 325,
s2 二、"三人团" "The Group of Three" PDF 329, s3 三、沧海横流，方显英雄本色 "Only in the Raging
Sea Is the Hero's True Color Seen" PDF 331, s4 四、在浦东上船 "Boarding the Boat at Pudong"
PDF 334) end to end against the frozen doc. Chapter Fifteen is the book's LAST chapter; ch16
Works Cited opens at PDF 338, so ch15 body ends PDF 337. Offset a constant 15 (printed = pdf
- 15); read each opener's folio off the scan. Re-render and re-OCR (data/png and data/zh are
gitignored, gone on a fresh checkout): render.py 324 337 --dpi 300, then ocr_crop.py 324 337
--left 0.06 --right 0.95 --top 0.11 --bottom 0.955 --lang chi_sim --psm 6. OCR is TOO NOISY on
the proper names, so HAND-TRANSCRIBE data/zh/ch15.txt off the 300-DPI page images directly
(data/png/p####.png), one paragraph per line, chapter title and section heads as ### (the
B08/B11/B12/B13/B15/B16 method; OCR is a cross-check, not the source). The chapter divider
(PDF 324) and any washed-out full-page painting are design furniture, not captioned figures;
watch for FULL-PAGE DOUBLE PLATES (pages of photos with captions but no body text, zero
paragraphs); eyeball every page for real photos/line art and hand-crop any (exclude the printed
caption, translator's caption with source-label provenance, real alt text). Numerals in
unit/place designations are load-bearing, crop-verify them. Add ch15 to data/content_config.json.

BEFORE translating, read the final two pages of ch14's English (the voice). Read
the zh against the en on every line; change register, never meaning; invent
nothing (CLAUDE.md rule 4; verify the TAIL of the unit explicitly against the
scan). Cite printed folios, never PDF pages. Then footnotes at reader-model
density (consult the "NOT re-noted" lists in PROGRESS; grep notes.json before
adding); glossary rows straight into the sectioned ledger (en ASCII only, WITH a
`pinyin` field), consulting authority.json first; flag any NEW recurring institutional term
recurring:true and any NEW concession street gazetteer:true+today. Run
check_structure --pairs (SOURCE first: data/zh/ch15.txt out/ch15_reading.md),
verify_unit, make_bilingual + qc_entities, check_align, check_content --config
data/content_config.json, apparatus_merge + check_apparatus, and check_register
--ref out/ch01_reading.md (informational). Rebuild, run qa_epub and epubcheck (jar
at /tmp/epubcheck-5.1.0/epubcheck.jar).

NOTE: ch15 is the last body chapter. After it, only the Preface (ch00, PDF 6-15) and
back matter (Works Cited ch16, Afterword ch17) remain, plus the whole-book reconciliation
sweep (check 12), cover, COMPLETION.md and the ch01-ch09 cleanup worklist. Those fold into a
final light batch (B18). Do NOT start them this batch unless ch15 finishes with room to spare.

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
- **B15 = ch13:** "Twin Lotus on One Stem," 139 paragraphs, 5 sections, PDF 284-307.
  Hand-transcribed; 17 notes (book 383), 4 figures, ~73 glossary rows; glossary `pinyin`-field
  back-fill (qc_entities needs it); B15 noise block. Shen Anna / Hua Mingzhi "twin lotus" story.
- **B16 (this batch) = ch14:** ""Secret Number One"," 66 paragraphs, 6 sections, PDF 308-323.
  Hand-transcribed; ch08-ch13 source-criticism register; 12 notes (book 395), 7 figures, ~65
  glossary rows; B16 noise block (瘰三, 立三, 陈三百). The Central Archive and its keepers
  (Chen Weiren, Miao Guren, Zheng Wendao, Chen Laisheng); the Sorge ring; Luo Zhanglong's
  venom turned against him. All checks green, epubcheck 0/0/0/0, register no stilted flag.
  See PROGRESS.md "B16". ch15, the Preface, and back matter remain.

## Tooling in place (DO NOT REVERT)
- **build_reading_epub.py:** `render_recurring` (Glossary of Recurring Terms),
  `render_gazetteer` (Street Gazetteer), `_walk_flagged`, `.gaz` CSS; both back-matter
  pages wired into spine/nav/ncx and rendered only when their data exists. Book/periodical
  titles are italicized in a reading file via `*...*` -> `<i>...</i>` (line ~553); ch14
  italicizes titles (like ch01/ch08/ch09), ch10-ch13 render them PLAIN, a reconciliation-sweep item.
- **check_content.py:** `AUTHOR` set (author self-naming) AND `HOMOGRAPHS` set: 严重 = the
  ch10 courier "Yan Zhong" but also the adjective "severe" (used in ch14 too); excluded from
  the content name-map.
- **qc_entities.py:** the SAME `HOMOGRAPHS = {"严重"}` stoplist. Keep the two lists in sync.
  It reads `rec["pinyin"]` for every glossary row, so **every glossary row must have a
  `pinyin` field** (B15 back-filled `pinyin = en` on the 72 rows that lacked one).
- Register-pass drivers: `edits/chNN_edits.md` + `scripts/apply_edits.py`;
  `scripts/anchor_check.py`.
- `scripts/indents.py`: furniture-band drop (FURNITURE_TOP=0.11, BOTTOM=0.955).
- `scripts/check_numbers.py`: arabic+万 combiner before the noise loop.
- `data/noise.txt` carries B02-B16 blocks (longest literal first); the B16 block adds
  瘰三 (Luosan), 立三 (Li Lisan split form), 陈三百 (Chen Sanbai) — all name numerals.
- `data/content_config.json`: docs+sources map for check_content, ch01-ch14. ADD ch15.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Transcription method (B08, confirmed again B16):** OCR is too noisy on the proper
  names; READ the 300-DPI page images (data/png/p####.png) directly and transcribe,
  cropping tight regions only for ambiguous names/numbers.
- **Parity gotcha:** in `data/zh/chNN.txt` mark the chapter title `### ` (like section
  heads), NOT `## `. English side: chapter title `## `, section heads `### `. AND run
  check_structure --pairs with the SOURCE file FIRST: `data/zh/chNN.txt out/chNN_reading.md`.
- **Full-page double plates / painting pages:** a page can be all photos with captions and NO
  body text, or a washed-out full-page painting (ch14 p0323). Zero paragraphs; do not invent
  any. Count body paras off the actual prose, not the page count.
- **Glossary placement gotcha:** glossary.json is a DICT keyed by hanzi under
  people/organizations/places/terms. Add rows directly into the sub-objects (each row: `en`
  ASCII, `pinyin`, `status`, optional `note`). Where the prose uses a SHORT form, set `en`
  to it so the substring test in check_content/qc_entities passes.
- **Apostrophe gotcha (B16):** glossary `en` must use the STRAIGHT apostrophe `'` to match
  the reading text (e.g. "Dong Lin'ge", "Tan Chong'an"); a curly `’` in `en` fails check_content.
- **check_content full-name-vs-surname trap:** a glossary `en` of the full name fails when
  the body uses only the surname; set the glossary `en` to the SHORT form actually used.
  Also avoid a bare place row that is only ever a substring of a longer one (B16 removed
  小沙渡, which occurs only inside 小沙渡路 = Ferry Road).
- **VERY high-frequency recurring names with pronoun runs, and name/common-word
  homographs**, stay OUT of the entity glossary (or go in the HOMOGRAPHS stoplist in BOTH
  check_content and qc_entities).
- **figures.json `file` is a BASENAME**; builder prepends `data/figs/`. `before` anchors
  fall in the FIRST ~80 chars of a paragraph, cannot sit on a heading. Two separate photos on
  one page (ch14 p0318: Miao Guren + Zheng Wendao) are two figure specs.
- **Washed-out full-page divider/illustration pages** are design furniture, NOT captioned
  figures (exclude them; ch14's are p0308 the divider and p0323 the painting).
- Set-off block quotes render `{v}`; verse `{p}`; dateline `{d}`; `check_structure.py`
  strips markers before parity. ch10-ch14 used ZERO markers: cited memoir/document passages
  read cleanly as normal paragraphs with a "(Name, year)" attribution or a colon lead-in.

## Apparatus state after B16 (frozen doc = STYLE.local top sections)
- 395 notes (ch09 +27, ch10 +15, ch11 +19, ch12 +15, ch13 +17, ch14 +12). Densities taper as
  the book's furniture gets covered; ch14 reused much established furniture (Sorge, Ozaki,
  Gu Shunzhang, Wang Jingwei, Liao Zhongkai, Nakanishi, the Comintern all cross-referenced
  rather than re-noted). A modest new-note count remains healthy for ch15.
- The Glossary of Recurring Terms and Street Gazetteer carry the recurring furniture and the
  concession streets; gloss such terms ONCE at first appearance and let the back matter carry
  the rest. When drafting ch15, flag any NEW recurring institutional term `recurring:true`
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
  Road (today Hankou Road). ch09 para 163 has the ONE outlier "Fourth Avenue" -> fix in sweep.
- B16 additions (full list in PROGRESS "B16"): the Central Archive cast (陈为人 Chen Weiren /
  陈涛 Chen Tao; 张唯一 Zhang Weiyi; 韩慧英 Han Huiying; 凌炳 Ling Bing; 缪谷稔 Miao Guren; 郑文道
  Zheng Wendao / 程和生 Cheng Hesheng; 陈来生 Chen Laisheng), the Shanghai/HK net (李默农 Li
  Monong = 李少石; 董麟阁 Dong Lin'ge; 史永 Shi Yong / 沙文威; 董慧 Dong Hui; 李德生 Li Desheng;
  汪锦元 Wang Jinyuan; 陈一峰 Chen Yifeng), the Sorge ring (左尔格 Sorge, 尾崎秀实 Ozaki, 宫城与德
  Miyagi Yotoku, 克劳森 Clausen, 西里龙夫 Nishizato Tatsuo), 孔祥熙 Kong Xiangxi (H.H. Kung).
  NEW recurring orgs: 中央文库 the Central Archive; 华南情报局 the South China Intelligence Bureau;
  东北抗联 the Northeast Anti-Japanese United Army; 满铁调查部 the South Manchuria Railway; 日本同盟社
  the Dōmei News Agency; 共产国际 the Comintern. NEW gazetteer streets: 恺自迩路 Rue Kraetzer,
  开纳路 Kinnear Road, 小沙渡路 Ferry Road, 贝勒路 Rue Amiral Bayle, 江西路 Kiangse Road.
- Consult authority.json before romanizing (Zhou Enlai, Mao Zedong, Dong Biwu, Chiang
  Kai-shek, Deng Yingchao, Bo Gu, Li Kenong, Ye Jianying, Lin Boqu, Chen Yun all confirmed
  shelf-wide; ch15 opens on 陈云 Chen Yun).

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with a sardonic
  edge; heat in the verbs and rhythm, ration exclamation and rhetorical questions; sustained
  source-criticism as running skeptical argument in plain English, sources' own words kept,
  verdict in the note; first person kept where he places himself as reader of the archive. In
  ch14 he opens on the renegade Luo Zhanglong's slanders and turns them against him, and sets
  Huang Jieran's interview against the Chen Weiren biography and Li Qiang's remarks; preserve
  that argumentative motion.
- **Interviewee / martyr set-pieces run at natural, contracted, spoken register** where the
  witness speaks, and rise to the author's heat at the martyr climaxes (Chen Weiren's "I will
  not die, I still have work to do"; Zheng Wendao's two suicide attempts). Keep the
  temperature; verdict in the note; do not iron flat.
- **Zhou Enlai** warm and big-brotherly; **Party leaders / descendants / martyrs in
  interview** clipped, factual, contracted; **KMT memoirists / officials** officialese,
  self-regarding; **quoted 1930s-40s documents** (resolutions, directives, Party decisions)
  stay starchy and formal, that is period work and is correct.

## Where the story stands
Chapters One-Fourteen are drafted. Chapter Thirteen told the Shen Anna "twin lotus" story;
Chapter Fourteen, "Secret Number One," told the story of the Central Archive and its keepers.
Chapter Fifteen, "The Last Effort" (ch15, PDF 324-337), is the book's LAST chapter: four
sections (陈云来了 "Chen Yun Arrives," "三人团" "The Group of Three," 沧海横流，方显英雄本色
"Only in the Raging Sea Is the Hero's True Color Seen," 在浦东上船 "Boarding the Boat at
Pudong"). Chen Yun enters. Read the ch08-ch14 source-criticism voice sheet forward.

## Open traps / environment
- `data/zh/` and `data/png/` are gitignored; a fresh checkout has neither. ch15 drafting
  needs both (render + hand-transcribe from source.pdf, which IS tracked). The tracked
  deliverables (out/chNN_reading.md, notes/glossary/figures, the built EPUB) are complete.
- Cross-check note AND figure anchors before any re-voicing edit (scripts/anchor_check.py).
  A broken figure `before` anchor fails the build. Note anchors must match the reading file
  byte-for-byte INCLUDING inner punctuation and any `*italic*` markup (anchors are inserted
  BEFORE markup substitution).
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; `pgrep -c tesseract` = 0 after OCR (ocr_crop
  exits 1 when the final `pgrep -c` finds 0 processes, that is SUCCESS, not failure).
  epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch.
- **ch01-ch09 cleanup-sweep worklist (do at the end, not mid-batch):** (1) ch01 Yang Du
  note birth year "1875" -> "1874"; (2) ch09 para 163 "Fourth Avenue" -> "Sima Road" for
  四马路; (3) book-wide title-italics decision (ch10-ch13 plain vs ch01/ch08/ch09/ch14 italic).
- Still UNTRANSLATED: ch15 (last chapter), the Preface (ch00, PDF 6-15), and back matter (Works
  Cited ch16, Afterword ch17). They fold into B17 (ch15) and a final light B18 (front/back
  matter + reconciliation + cover + COMPLETION).
- Branch hygiene: canonical branch is `claude/the-sword-roars`. B16 started on a stray
  `claude/sword-roars-ch14-p4uja9` (its remote ref was stale, pointing at the same commit as
  origin/canonical); consolidated onto canonical, stray pruned local and remote.
