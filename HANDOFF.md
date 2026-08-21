# HANDOFF: The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start the next batch. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch11's English (and ch01, the
> frozen register reference) before drafting ch12.

```
Sword Roars B14 Chapter Twelve

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. In STYLE.local.md the top section "THE REGISTER REBASELINE
(B09 commissioner review)" and the "Footnote apparatus" and "Apparatus policy"
sections are the frozen reference for all further work. Work on branch
claude/the-sword-roars (the canonical book branch; if the harness starts you on
a stray per-task branch, consolidate per CLAUDE.md rule 2 and delete the stray,
local and remote). Run ./setup.sh first.

STATE: B13 is done. Chapter Eleven ("The Wild Swan," ch11, PDF 248-263, printed
233-248, 82 paragraphs, 3 sections) is drafted end to end against the frozen doc:
hand-transcribed off the 300-DPI images (OCR too noisy on the names, Pan Hannian
especially), rendered in ch08/ch09/ch10's sardonic source-criticism register with
each source's own words kept and verdicts in the notes; 19 footnotes (book total
351), 3 hand-cropped figures, 108 new glossary rows, ch11 added to
data/content_config.json. Andersen's "The Wild Swans" (Elisa forbidden to speak) is
the title figure; the chapter is Pan Hannian's, and its long third section is the
source-critical life of Yang Du (monarchist turned secret Communist) and the fight to
record his Party membership in the Cihai. Decided 薛华立路 = Route Stanislas Chevalier
(gazetteer, today Jianguo Middle Road); flagged the source slip 十五万将军入闽 -> 蒋军
"150,000 of Chiang's troops" with a [—Trans.] note. All checks green: parity 82=82,
numbers 0 unresolved, content/entities clean, qa_epub PASS, epubcheck 0/0/0/0. The
register STILTED flag is the documented document/memoir-heavy quiet-dialogue case
(narratorial signals on-reference). See PROGRESS.md "B13" for the "NOT re-noted" list,
the settled renderings, and one open ch01-sweep item (Yang Du b. 1874, not 1875).

This batch's job: DRAFT CHAPTER TWELVE (ch12, "A Purge in the Red-Light District,"
PDF 264-283, printed 249-268, 7 sections: s1 一、枪响"小花园" "Shots at the 'Little
Garden'" PDF 265, s2 二、1469号车牌 "License Plate 1469" PDF 267, s3 三、谣言杀人 "Rumor
Kills" PDF 270, s4 四、葬身之所 "A Place to Die" PDF 272, s5 五、如入无人之境 "As Through
an Empty Land" PDF 275, s6 六、神枪手 "The Crack Shot" PDF 277, s7 七、殉道者永受赞美
"The Martyr Forever Praised" PDF 279) end to end against the frozen doc. Offset a
constant 15 (printed = pdf - 15); read each opener's folio off the scan. Re-render and
re-OCR (data/png and data/zh are gitignored, gone on a fresh checkout): render.py 264
283 --dpi 300, then ocr_crop.py 264 283 --left 0.06 --right 0.95 --top 0.11 --bottom
0.955 --lang chi_sim --psm 6. OCR is TOO NOISY on the proper names, so HAND-TRANSCRIBE
data/zh/ch12.txt off the 300-DPI page images directly (data/png/p####.png), one
paragraph per line, chapter title and section heads as ### (the B08/B11/B12/B13 method;
OCR is a cross-check, not the source). The chapter divider (PDF 264) and any washed-out
full-page painting are design furniture, not captioned figures; eyeball every page for
real photos/line art and hand-crop any (exclude the printed caption, translator's
caption with source-label provenance, real alt text). Numerals in unit/plate/case
designations (1469号车牌) are load-bearing — crop-verify them. Add ch12 to
data/content_config.json.

BEFORE translating, read the final two pages of ch11's English (the voice). Read
the zh against the en on every line; change register, never meaning; invent
nothing (CLAUDE.md rule 4; verify the TAIL of the unit explicitly against the
scan). Cite printed folios, never PDF pages. Then footnotes at reader-model
density (consult the "NOT re-noted" lists in PROGRESS; grep notes.json before
adding); glossary rows straight into the sectioned ledger (en ASCII only),
consulting authority.json first; flag any NEW recurring institutional term
recurring:true and any NEW concession street gazetteer:true+today. Run
check_structure --pairs (SOURCE first: data/zh/ch12.txt out/ch12_reading.md),
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
  sections; 27 notes (book 317), 5 figures, 95 glossary rows, 善钟路 -> gazetteer.
- **B12 = ch10:** "Opening a Shop, Doing Trade," 39 paragraphs, 2 sections; 15 notes
  (book 332), 3 figures, 101 glossary rows; 华润 = "Huarun" (glossed China Resources).
- **B13 (this batch) = ch11:** "The Wild Swan," 82 paragraphs, 3 sections, PDF 248-263.
  Hand-transcribed; ch08-ch10 source-criticism register; 19 notes (book 351), 3 figures,
  108 glossary rows; 薛华立路 -> gazetteer; check_content HOMOGRAPHS patch (严重).
  All checks green, epubcheck 0/0/0/0. See PROGRESS.md "B13". ch12-ch15, the Preface,
  and back matter remain.

## Tooling in place (DO NOT REVERT)
- **build_reading_epub.py:** `render_recurring` (Glossary of Recurring Terms),
  `render_gazetteer` (Street Gazetteer), `_walk_flagged`, `.gaz` CSS; both back-matter
  pages wired into spine/nav/ncx and rendered only when their data exists.
- **check_content.py:** `AUTHOR` set (author self-naming) AND now `HOMOGRAPHS` set
  (B13): 严重 = the ch10 courier "Yan Zhong" collides with the adjective "severe"; it is
  excluded from the content name-map so ordinary "白色恐怖最严重" no longer flags.
- Register-pass drivers: `edits/chNN_edits.md` + `scripts/apply_edits.py`;
  `scripts/anchor_check.py`. Scratchpad helpers from B10 (not committed).
- `scripts/indents.py`: furniture-band drop (FURNITURE_TOP=0.11, BOTTOM=0.955).
- `scripts/check_numbers.py`: arabic+万 combiner before the noise loop.
- `data/noise.txt` carries B02-B13 blocks (longest literal first); the B13 block adds
  瘪三/拉三/二百五/千要万要/两个字.
- `data/content_config.json`: docs+sources map for check_content, ch01-ch11.
  ADD ch12 when you translate it.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Transcription method (B08, confirmed again B13):** OCR is too noisy on the proper
  names; READ the 300-DPI page images (data/png/p####.png) directly and transcribe,
  cropping tight regions only for ambiguous names/numbers.
- **Parity gotcha:** in `data/zh/chNN.txt` mark the chapter title `### ` (like section
  heads), NOT `## `. English side: chapter title `## `, section heads `### `. AND run
  check_structure --pairs with the SOURCE file FIRST: `data/zh/chNN.txt
  out/chNN_reading.md` — swapping them makes the '##' English chapter title miscount by
  one (source 83 | translation 82).
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the JSON
  top level; the builder needs them under people/organizations/places/terms. glossary.json
  is a DICT keyed by hanzi under each of those sub-objects. Add rows directly into the
  sub-objects with a re-read-verified one-shot (NOT via apparatus_merge's glossary path).
- **Glossary `en` must be ASCII;** curly punctuation only in note bodies (numeric char
  refs), applied at the render layer.
- **VERY high-frequency recurring names with pronoun runs, and name/common-word
  homographs, stay OUT of the entity glossary** (or go in the HOMOGRAPHS stoplist):
  adding them fires false check_content displacement.
- **figures.json `file` is a BASENAME**; builder prepends `data/figs/`. `before` anchors
  fall in the FIRST ~80 chars of a paragraph, cannot sit on a heading.
- **Washed-out full-page chapter-divider illustrations** are design furniture, NOT
  captioned figures (exclude them; ch11's is p0248, a faint Pan Hannian portrait).
- Set-off block quotes render `{v}`; verse `{p}`; dateline `{d}`; `check_structure.py`
  strips markers before parity. ch10 and ch11 used ZERO markers — cited memoir/document
  passages read cleanly as normal paragraphs with a "(Name, year)" attribution or a
  colon lead-in; keep that unless a passage is genuinely a set-off verse/inscription.

## Apparatus state after B13 (frozen doc = STYLE.local top sections)
- 351 notes (ch09 +27, ch10 +15, ch11 +19). Densities taper as the book's furniture gets
  covered; ch11 runs ~290 words/note (reference-dense but heavily pre-noted from ch01,
  which carries Yang Du, Pan Hannian, the Nineteenth Route Army/Fujian Incident, Du
  Yuesheng, tingzijian). A late chapter with a modest new-note count is healthy.
- The Glossary of Recurring Terms and Street Gazetteer carry the recurring furniture and
  the concession streets; gloss such terms ONCE at first appearance and let the back
  matter carry the rest. When drafting ch12, flag any NEW recurring institutional term
  `recurring:true` and any NEW concession street `gazetteer:true`+`today`.
- Marker placement: put a marker at the end of the clause/sentence that holds the
  referent, never mid-phrase (right after a complete referent noun-phrase is fine).

## Renderings settled (also in glossary.json / STYLE.local.md)
- Consistency canon (verified clean): Center (not Centre), the Politburo, the White
  Terror, the Xujiahui Observatory, Lazily Seeking Old Dreams (italic), fused lane names,
  the ten-li foreign quarter, presiding pastor. Dates month-day-year. Spelling: AMERICAN.
- 中央特科 the Central Special Branch (handle: the Special Branch); 红队 / 打狗队 the Red
  Squad / the dog-beating squad; 中统 the Zhongtong; 华润 Huarun (China Resources).
- B13 additions: 潘汉年 Pan Hannian (codes 小开/开/小K/K); 杨度 Yang Du (b. 1874 per the
  book's Cihai entry — ch01 note says 1875, fix in the sweep); 十九路军 the Nineteenth
  Route Army (recurring); 筹安会 the Chou'an Society (recurring); 蔡廷锴 Cai Tingkai / 蒋光鼐
  Jiang Guangnai / 戴戟 Dai Ji / 陈铭枢 Chen Mingshu / 李济深 Li Jishen; 徐名鸿 Xu Minghong;
  梅龚彬 Mei Gongbin; 章士钊 Zhang Shizhao; 夏衍 Xia Yan; 二房东 "second landlord";
  薛华立路 Route Stanislas Chevalier (gazetteer, today Jianguo Middle Road).
- Consult authority.json before romanizing (Sun Yat-sen, Du Yuesheng, Deng Yanda, Guo
  Moruo, Feng Xuefeng, Wang Jingwei, Song Qingling all confirmed shelf-wide).

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with a
  sardonic edge; heat in the verbs and rhythm, ration exclamation and rhetorical
  questions; sustained source-criticism as running skeptical argument in plain English,
  sources' own wrong words kept, verdict in the note; first person kept where he places
  himself as interviewer. His SARDONIC scare-quoting of hyped sources is his voice —
  preserve it; in ch11 he ends by handing the last word to a Taiwan historian who
  reframes Yang Du's "conversion" as one more turn of a lifelong gift for playing every
  side. Do not iron this flat; do not quilt unremarkable fragments either.
- **Martyr set-pieces run at full temperature, verdict in the note.** ch12 is a purge/
  assassination chapter ("A Purge in the Red-Light District") ending on a martyr set-
  piece (七、殉道者永受赞美) — expect the full-temperature register there.
- **Zhou Enlai** warm and big-brotherly; **Gu Shunzhang** the foil, hot and contemptuous;
  **Cai Mengjian / KMT memoirists** officialese, self-regarding; **Party leaders /
  descendants in interview** clipped, factual, contracted.

## Where the story stands
Chapters One-Eleven are drafted. Chapter Ten turned from the traitor-hunt to the Party's
commercial fronts; Chapter Eleven, "The Wild Swan," is Pan Hannian's — his going deep
underground, his brokering with the Nineteenth Route Army and the doomed Fujian revolt,
and the long source-critical recovery of Yang Du, the monarchist theorist who died a
secret Communist. Chapter Twelve, "A Purge in the Red-Light District" (ch12, PDF 264-283),
is next: seven sections, a return to the Special Branch's assassinations/counter-traitor
work (the "Little Garden" shooting, License Plate 1469, a crack marksman, a martyr's
end). Read the ch08-ch11 source-criticism voice sheet forward, and the martyr-set-piece
note for the closing section.

## Open traps / environment
- `data/zh/` and `data/png/` are gitignored; a fresh checkout has neither. ch12 drafting
  needs both (render + hand-transcribe from source.pdf, which IS tracked). The tracked
  deliverables (out/chNN_reading.md, notes/glossary/figures, the built EPUB) are complete.
- Cross-check note AND figure anchors before any re-voicing edit (scripts/anchor_check.py).
  A broken figure `before` anchor fails the build.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; `pgrep -c tesseract` = 0 after OCR.
  epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch.
- **ch01-ch08 cleanup-sweep worklist (do at the end, not mid-batch):** Yang Du birth
  year 1875 -> 1874 in the ch01 note (this book's Cihai entry says 1874).
- Still UNTRANSLATED: ch12-ch15, the Preface (ch00, PDF 6-15), and back matter (Works
  Cited ch16, Afterword ch17). They fold into later batches.
- Branch hygiene: canonical branch is `claude/the-sword-roars`. B13 started on a stray
  `claude/sword-roars-ch11-draft-m9cre4` (identical commit; never on origin); consolidated
  onto canonical, stray pruned local and remote.
