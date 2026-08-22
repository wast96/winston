# HANDOFF: The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start the next batch. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read ch01 (the frozen register reference) and a couple of
> late body chapters before drafting the Preface and Afterword.

```
Sword Roars B18 Front & Back Matter, Reconciliation, Completion (FINAL batch)

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. In STYLE.local.md the top section "THE REGISTER REBASELINE
(B09 commissioner review)" and the "Footnote apparatus" and "Apparatus policy"
sections are the frozen reference for all further work. Work on branch
claude/the-sword-roars (the canonical book branch; if the harness starts you on
a stray per-task branch, consolidate per CLAUDE.md rule 2 and delete the stray,
local and remote). Run ./setup.sh first.

STATE: ALL 15 BODY CHAPTERS ARE DONE. B17 drafted Chapter Fifteen (ch15, "The
Last Effort," PDF 324-337, printed 309-322, 55 paragraphs, 4 sections), the
book's last body chapter: Chen Yun sent from the Long March to rebuild the
shattered Shanghai Party, then smuggled with Pan Hannian to the USSR; the
short-lived "Group of Three," the united-front turn (August First Declaration,
Dimitrov, the 7th Comintern Congress), the collapse of the "Walton"
intelligence ring, and Chen Yun's Random Notes on the Western March. Hand-
transcribed off the 300-DPI images; 10 footnotes (book total 405), 4 hand-
cropped figures, 123 new glossary rows, ch15 added to data/content_config.json.
Tooling patch (DO NOT REVERT): data/noise.txt got a B17 name-numeral block
(王养三, 秦叙五, 俞三元, 水番三郎). No script changes. All checks green: parity 55=55,
numbers 0 unresolved, content/entities clean, qa_epub PASS, epubcheck 0/0/0/0,
register within tolerance of ch01 (no stilted flag). See PROGRESS.md "B17".

This batch's job: THE FINAL LIGHT BATCH. Do these, end to end:

1. FRONT MATTER: translate the Preface (ch00, "前言 历史不能被妖魔化 / History Must
   Not Be Made a Monster," PDF 6-15, printed runs a separate roman sequence;
   read the folios off the scan). Render, render figures if any, footnote at
   reader-model density. Same pipeline as a body chapter (render.py, ocr_crop.py
   with THIS book's crop --left 0.06 --right 0.95 --top 0.11 --bottom 0.955
   --lang chi_sim --psm 6, then HAND-TRANSCRIBE data/zh/ch00.txt off data/png,
   OCR is a cross-check only). check_structure --pairs (SOURCE first), verify_unit,
   make_bilingual + qc_entities, check_align, check_content, apparatus_merge +
   check_apparatus, check_register --ref out/ch01_reading.md.

2. BACK MATTER: (a) Works Cited (ch16, 参考文献, PDF 338-347): render into
   back_matter.json or the builder's Works Cited page as a full bilingual
   entry list (Chinese title + English), per STYLE "cited-work titles: English
   only in the body, full bilingual entry in the back-matter Works Cited."
   Every cited work named in the notes/ledger should resolve here. (b) Afterword
   (ch17, 后记 守住清贫，耐住寂寞 / "Keep to Poverty, Endure the Silence," PDF 348-...):
   translate like a body unit.

3. WHOLE-BOOK RECONCILIATION SWEEP (check 12; run check_reconcile.py). Resolve
   the standing consistency items: (i) "Song Qingling" is the decided form (fix
   the 3 "Soong Ching-ling" outliers in earlier chapters); "Dabu" the decided
   form (1 "Dapu" outlier). (ii) ch01 Yang Du note birth year "1875" -> "1874".
   (iii) ch09 para 163 "Fourth Avenue" -> "Sima Road" for 四马路. (iv) Book-wide
   title-italics decision: ch10-ch13 render book/film/periodical titles PLAIN;
   ch01/ch08/ch09/ch14/ch15 italicize them. Pick one (italic is the STYLE.md
   rule) and grep-fix the plain ones, then rebuild. (v) LATENT CAPTION BUG: the
   builder passes figure captions through html.escape, which double-escapes
   numeric character references; ch14 captions store &#8217;/&#8220; and will
   render the literal entity text. Fix ch14 (and any other) captions to plain
   ASCII quotes (ch15 already uses ASCII). Consider whether to teach the builder
   to leave existing numeric entities alone instead; either way, verify in the
   built EPUB. (vi) check_reconcile's drift candidates are for a HUMAN read; some
   variation is legitimate.

4. COVER: book.json cover_image is data/figs/cover.png. Confirm it exists and is
   copied byte-identical, or generate the typographic cover; the front-cover
   painting (PDF 1) can be the source. qa_epub + epubcheck must stay clean.

5. COMPLETION: write COMPLETION.md from the template (sampled error rate, residual
   uncertainties), render out/term_ledger.md and out/deep_audit.md, update
   authority.json with this book's decided renderings (whole-book completion, not
   per batch). Set book.json to state the build is COMPLETE. Commit the final EPUB
   itself: git add -f out/sword-roars.epub (branches outlive containers, chat
   attachments do not). Rewrite HANDOFF.md to say the book is COMPLETE and further
   work is a corrections pass; do NOT modify the kickoff section afterward (the
   Stop hook would demand a block that no longer exists).

Cite printed folios, never PDF pages. Offset for the body is a constant 15
(printed = pdf - 15); the Preface runs its OWN roman-numeral sequence, so read
its folios off the scan. Never invent bridging text (CLAUDE.md rule 4; verify
tails against the scan). Do not pause for approval. Deliver the rebuilt EPUB
attached in the chat, and (this being the last batch) paste the COMPLETION
summary in the same reply in place of a next kickoff.
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
- **B16 = ch14:** ""Secret Number One"," 66 paragraphs, 6 sections, PDF 308-323.
  Hand-transcribed; 12 notes (book 395), 7 figures, ~65 glossary rows; B16 noise block. The
  Central Archive and its keepers; the Sorge ring; Luo Zhanglong's venom turned against him.
- **B17 (this batch) = ch15:** "The Last Effort," 55 paragraphs, 4 sections, PDF 324-337. THE
  LAST BODY CHAPTER. Hand-transcribed; ch08-ch14 source-criticism register; 10 notes (book 405),
  4 figures, 123 glossary rows; B17 noise block (王养三, 秦叙五, 俞三元, 水番三郎). Chen Yun
  arrives, the "Group of Three," the united-front turn, the Walton ring's fall, Chen Yun and
  Pan Hannian shipped to the USSR. All checks green, epubcheck 0/0/0/0, register no stilted
  flag. See PROGRESS.md "B17". Remaining: Preface (ch00), back matter (ch16 Works Cited, ch17
  Afterword), reconciliation sweep, cover, COMPLETION, ch01-ch09 cleanup worklist -> B18.

## Tooling in place (DO NOT REVERT)
- **build_reading_epub.py:** `render_recurring` (Glossary of Recurring Terms),
  `render_gazetteer` (Street Gazetteer), `_walk_flagged`, `.gaz` CSS; both back-matter
  pages wired into spine/nav/ncx and rendered only when their data exists. Book/periodical
  titles are italicized in a reading file via `*...*` -> `<i>...</i>` (line ~553).
  KNOWN LIMITATION: figure captions go through `esc()` = html.escape, which double-escapes
  numeric character references and strips `<i>`/`*` markup; ch15 captions therefore use plain
  ASCII quotes and no title italics. ch14 captions still hold `&#8217;`/`&#8220;` (a B18 fix).
- **check_content.py:** `AUTHOR` set (author self-naming) AND `HOMOGRAPHS` set (严重). Matches
  each glossary hanzi as an independent substring with NO overlap removal, so a bare place row
  that is a substring of a longer one (江西 inside 江西路) demands its own token in the English;
  ch15 para 2 re-glosses 江西路 as "Kiangse Road (today Jiangxi Middle Road)" to supply "Jiangxi."
- **qc_entities.py:** the SAME `HOMOGRAPHS = {"严重"}` stoplist. Reads `rec["pinyin"]` for every
  glossary row (en OR pinyin satisfies), so **every glossary row must have a `pinyin` field**.
- Register-pass drivers: `edits/chNN_edits.md` + `scripts/apply_edits.py`; `scripts/anchor_check.py`.
- `scripts/indents.py`: furniture-band drop (FURNITURE_TOP=0.11, BOTTOM=0.955).
- `scripts/check_numbers.py`: arabic+万 combiner before the noise loop. Spelled-out English
  numbers (thirty-six, eight, forty, seventy) ARE matched; only name numerals need noise entries.
- `data/noise.txt` carries B02-B17 blocks (longest literal first); the B17 block adds
  王养三 (Wang Yangsan), 秦叙五 (Qin Xuwu), 俞三元 (Yu Sanyuan), 水番三郎 (Mizuban Saburo).
- `data/content_config.json`: docs+sources map for check_content, ch01-ch15. ADD ch00/ch16/ch17
  when they are drafted.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955 --lang chi_sim
  --psm 6`. Offset constant 15 (printed = pdf - 15); the Preface runs a SEPARATE roman sequence.
- **Transcription method (confirmed again B17):** OCR is too noisy on the proper names; READ the
  300-DPI page images (data/png/p####.png) directly and transcribe. OCR wholly lost 孙诗圃, 陈翰笙.
- **Parity gotcha:** in `data/zh/chNN.txt` mark the chapter title `### `, section heads `### `.
  English side: chapter title `## `, section heads `### `. Run check_structure --pairs with the
  SOURCE file FIRST: `data/zh/chNN.txt out/chNN_reading.md`.
- **Number-check gotcha:** 100+ counts stated as English words can miss (一百 -> "Hundred" was
  not matched; 一万二千 -> "twelve thousand" was not); render 100 and 12,000 as digits (house
  style anyway wants figures at 100 and up).
- **Glossary placement gotcha:** glossary.json is a DICT keyed by hanzi under
  people/organizations/places/terms. Add rows directly (each row: `en` ASCII, `pinyin`, `status`,
  optional `note`/`recurring`/`gazetteer`/`today`). Set `en` to the SHORT form actually used so
  the substring test passes (共青团 -> "Youth League", not "Communist Youth League").
- **Apostrophe gotcha:** glossary `en` must use the STRAIGHT apostrophe `'` to match the reading
  text (e.g. "Cao Yi'ou", "Laotai'anli"); a curly apostrophe fails check_content.
- **figures.json `file` is a BASENAME**; builder prepends `data/figs/`. `before` anchors fall in
  the FIRST ~80 chars of a paragraph, cannot sit on a heading. A page can carry a composite
  (book cover + handwriting, ch15 p0329) = one figure spec.
- **Chapter divider pages** (the page listing the section titles, e.g. ch15 p0324) are design
  furniture, NOT captioned figures. Watch for full-page double plates (all photos, zero body
  text) and washed-out full-page paintings; ch15 had none.
- Set-off block quotes / cited memoir + document passages read cleanly as normal paragraphs with
  a "(Name, year)" attribution or a colon lead-in; ch10-ch15 used ZERO set-off markers.

## Apparatus state after B17 (frozen doc = STYLE.local top sections)
- 405 notes (ch09 +27, ch10 +15, ch11 +19, ch12 +15, ch13 +17, ch14 +12, ch15 +10). Densities
  taper as the book's furniture gets covered; ch15 reused much established furniture (Long March,
  Great Revolution, Shanghai uprisings, Feng Yuxiang, Blue Shirts, GPU, Sorge, Zunyi, united
  front, Noulens, Song Qingling all cross-referenced rather than re-noted).
- The Glossary of Recurring Terms and Street Gazetteer carry the recurring furniture and the
  concession streets; gloss such terms ONCE at first appearance. When drafting the Preface, flag
  any NEW recurring institutional term `recurring:true` and any NEW concession street
  `gazetteer:true`+`today`.
- Marker placement: put a marker at the end of the clause/sentence that holds the referent,
  never mid-phrase.

## Renderings settled (also in glossary.json / STYLE.local.md)
- Consistency canon (verified clean in-chapter): Center (not Centre), the Politburo, the White
  Terror, the White areas / soviet areas, the ten-li foreign quarter. Dates month-day-year.
  Spelling: AMERICAN. Book/film/periodical titles italic (a book-wide sweep item for ch10-ch13).
- 中央特科 the Central Special Branch (handle: the Special Branch); 上海中央局 the Shanghai
  Central Bureau; 三人团 / 五人团 the "Group of Three" / "Group of Five"; 共青团 the Youth League;
  格柏乌 GPU; 联共（布）the CPSU(B); 中华苏维埃政府 the Chinese Soviet government.
- **Decided name forms (glossary):** 宋庆龄 **Song Qingling** (pinyin, not Soong Ching-ling; 3
  earlier "Soong Ching-ling" outliers -> sweep); 大埔 **Dabu** (not Dapu; 1 outlier -> sweep);
  陈云 Chen Yun; 潘汉年 Pan Hannian (code name 小开 Xiaokai, ch11; "Mister" = Chen Yun, "the
  Boss" = Kang Sheng, all ch11).
- B17 additions (full list in PROGRESS "B17"): the Shanghai cast (章秋阳 Zhang Qiuyang, 孙诗圃
  Sun Shipu, 浦化人 Pu Huaren, 董维键 Dong Weijian, 刘仲华 Liu Zhonghua, 贺昌之 He Changzhi,
  朱军 Zhu Jun, 陈潭秋 Chen Tanqiu, 曾山 Zeng Shan, 马海德 Ma Haide / George Hatem, 陈翰笙 Chen
  Hansheng), the foreign transliterations (格伯特 Gebert, 波克利洛夫 Pokrylov [= Zhang Wentian],
  华尔敦 Walton, 基洛夫 Kirov, 季米特洛夫 Dimitrov, 维克托·乌索夫 Victor Usov), the Mao children
  (毛岸英/青/龙), and the historiographers (郝在今 Hao Zaijin, 赖安 Lai An). NEW gazetteer streets:
  天主堂街 Cathedral St, 新永安街 New Yong'an St, 环龙路 Route Vallon, 垃圾桥 Rubbish Bridge, 北京路
  Beijing Rd, 大马路 Dama Rd. 北山西路 rendered "Beishanxi Road" as printed + footnoted (likely
  misprint for 山西北路 Shanxi North Road).
- Consult authority.json before romanizing; update it at whole-book completion (B18), not per batch.

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with a sardonic
  edge; heat in the verbs and rhythm, ration exclamation and rhetorical questions; sustained
  source-criticism as running skeptical argument in plain English, sources' own words kept,
  verdict in the note; first person kept where he places himself as reader of the archive. In
  ch15 he corrects Xia Yan (董牧师 = Dong Jianwu, not Dong Weijian) and the Chen Yun biography
  (Su Mei's husband was Qiu Wen, not "Chuwen"); preserve that argumentative motion.
- **Interviewee / memoir set-pieces run at natural, contracted, spoken register** (Sun Shipu's
  1995 recollection, Ma Haide's 1981 account, Chen Tongsheng's "blackest of times"); **quoted
  1930s documents** (Party resolutions, the "August First Declaration," newspaper court reports)
  stay starchy and formal, that is period work and is correct.
- **Zhou Enlai** warm and big-brotherly; **Party leaders / descendants / martyrs in interview**
  clipped, factual, contracted; **KMT memoirists / officials** officialese, self-regarding.
- **Preface note for B18:** the Preface is titled "History Must Not Be Made a Monster"; expect
  the author at his most direct and polemical (the interested-witness voice at full volume, the
  frame for the whole book). Keep the heat; footnote the verdicts.

## Where the story stands
Chapters One-Fifteen are drafted; the narrative is COMPLETE. Chapter Fifteen, "The Last Effort,"
closed the book on the Central Special Branch's Shanghai years: Chen Yun's last effort to rebuild
the Party there, its failure under the White Terror, and his and Pan Hannian's passage to Moscow
in 1935 as the Long March redrew everything. What remains is not story but apparatus: the Preface
(the author's frame), the Works Cited and Afterword, the whole-book reconciliation, the cover,
and the completion report.

## Open traps / environment
- `data/zh/` and `data/png/` are gitignored; a fresh checkout has neither. B18 drafting of ch00/
  ch16/ch17 needs both (render + hand-transcribe from source.pdf, which IS tracked). The tracked
  deliverables (out/chNN_reading.md, notes/glossary/figures, data/figs/*.png, the built EPUB) are
  complete for ch01-ch15.
- Cross-check note AND figure anchors before any re-voicing edit (scripts/anchor_check.py). A
  broken figure `before` anchor fails the build. Note anchors must match the reading file
  byte-for-byte INCLUDING inner punctuation and any `*italic*` markup.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; `pgrep -c tesseract` = 0 after OCR (ocr_crop
  exits 1 when the final `pgrep -c` finds 0 processes, that is SUCCESS, not failure).
  epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion (B18), not per batch.
- **ch01-ch09 cleanup + reconciliation worklist (B18):** (1) ch01 Yang Du note "1875" -> "1874";
  (2) ch09 para 163 "Fourth Avenue" -> "Sima Road"; (3) book-wide title-italics (ch10-ch13 plain
  vs the rest italic); (4) "Soong Ching-ling" (3) -> "Song Qingling"; "Dapu" (1) -> "Dabu";
  (5) ch14 (and any) figure-caption numeric-entity double-escape bug -> ASCII quotes or a builder
  fix; (6) check_reconcile.py drift candidates for a human read.
- Branch hygiene: canonical branch is `claude/the-sword-roars`. B17 started on a stray
  `claude/the-sword-roars-ugxd41` (its remote ref was already gone/stale, same commit as
  origin/canonical); consolidated onto canonical, stray pruned local and remote.
