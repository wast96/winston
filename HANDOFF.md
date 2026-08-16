# HANDOFF: The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start the next batch. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch08's English (and ch01, the
> frozen register reference) before drafting ch09.

```
Sword Roars B11 Chapter Nine

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. In STYLE.local.md the top section "THE REGISTER REBASELINE
(B09 commissioner review)" and the "Footnote apparatus" and "Apparatus policy"
sections are the frozen reference for all further work. Work on branch
claude/the-sword-roars (the canonical book branch; if the harness starts you on
a stray per-task branch, consolidate per CLAUDE.md rule 2 and delete the stray,
local and remote). Run ./setup.sh first.

STATE: B10 is done. Two new builder features are in and shipping: a back-matter
GLOSSARY OF RECURRING TERMS (rows flagged recurring:true in glossary.json) and a
STREET GAZETTEER (places flagged gazetteer:true with a today field). The footnote
apparatus sweeps are done: mid-phrase markers moved to their clause end across
ch01-ch08; ch01 thinned 116->91 notes (passing warlords/minor glosses cut, every
dropped item still in the glossary); ch07 +6 and ch08 +6 first-appearance notes,
plus a War-of-Resistance note in ch01; 290 notes total, densities evened (ch01
174, ch08 634 words/note, ch01 outlier fixed). The spine-test pass split the four
genuine long-narration offenders (2 ch08, 1 ch01, 1 ch07); the rest over 90 words
are exempt quoted-document / anaphora / list sentences. EPUB rebuilt
(out/sword-roars.epub), qa_epub PASS, epubcheck 0/0/0/0.

This batch's job: DRAFT CHAPTER NINE (ch09, "The Riddle of Xiang Zhongfa's
Disappearance," PDF 208-235, printed 193-220) end to end against the frozen doc.
Groundwork from B10: offset a constant 15 (printed = pdf - 15), verified at
folios 195/196/197; read each opener's folio off the scan. Re-render and re-OCR
(data/png and data/zh are gitignored, gone on a fresh checkout):
render.py 208 235 --dpi 300, then ocr_crop.py 208 235 --left 0.06 --right 0.95
--top 0.11 --bottom 0.955 --lang chi_sim --psm 6. OCR is TOO NOISY on the proper
names (向忠发, 陈志皋, 黄慕兰, 探勒车行 all mangled), so hand-transcribe
data/zh/ch09.txt off the 300-DPI page images directly (data/png/p####.png), one
paragraph per line, chapter title and section heads as ### (the B08 method; OCR
is a cross-check, not the source). book.json carries ch09's 9-section structure
(openers at PDF 209,210,214,216,220,225,229,231,233). Section 2 has a portrait of
黄慕兰 (Huang Mulan) on p0211 -> a figure for figures.json (hand-crop, exclude the
printed caption, translator's caption with source-label provenance). The chapter
is source-CRITICAL: it weighs contested accounts of Xiang Zhongfa's capture (the
Huang Mulan memoir vs others) and of whether he broke under interrogation, and is
skeptical of the "secret cable"; render it in ch08's sardonic source-criticism
register, keep each source's own words, put the verdict in the note (corroborated
/ uncorroborated / contradicted). Add ch09 to data/content_config.json.

BEFORE translating, read the final two pages of ch08's English (the voice). Read
the zh against the en on every line; change register, never meaning; invent
nothing (CLAUDE.md rule 4; verify the TAIL of the unit explicitly against the
scan -- this chapter's tail is the highest-stakes source-criticism). Cite printed
folios, never PDF pages. Then footnotes at reader-model density (consult the
"NOT re-noted" lists; grep notes.json before adding); glossary rows straight into
the sectioned ledger, consulting authority.json first; run verify_unit,
check_align, check_content, check_apparatus, and check_register --ref
out/ch01_reading.md (informational). Rebuild, run qa_epub and epubcheck.

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
- **B10 (this batch):** two new builder features (Glossary of Recurring Terms +
  Street Gazetteer); footnote placement sweep (mid-phrase markers -> clause end,
  ch01-ch08); ch01 thinned 116->91; ch07/ch08 backfilled (+6/+6) + ch01 +1;
  spine-test pass (4 genuine long-narration sentences split); 290 notes. ch09 set
  up and deferred to its own batch (rule 4). See PROGRESS.md "B10".

## Tooling in place (DO NOT REVERT)
- **build_reading_epub.py:** `render_recurring` (Glossary of Recurring Terms, from
  rows flagged `recurring:true`), `render_gazetteer` (Street Gazetteer, from places
  flagged `gazetteer:true` with a `today` field), and the `_walk_flagged` helper;
  `.gaz` table CSS. Both pages are wired into spine/nav/ncx and rendered only when
  their data exists. qa_epub.py's APPARATUS set now lists terms.xhtml + gazetteer.xhtml.
- Register-pass drivers: `edits/chNN_edits.md` + `scripts/apply_edits.py`;
  `scripts/anchor_check.py` (checks a chapter's edit-file OLDs against note AND
  figure anchors). Scratchpad helpers from B10 (not committed): `move_markers.py`
  (placement sweep, dry-run default), `long_sentences.py` (spine worklist),
  `marker_scan.py` (marker-landing classifier).
- `scripts/indents.py`: furniture-band drop (FURNITURE_TOP=0.11, BOTTOM=0.955).
- `scripts/check_numbers.py`: arabic+万 combiner before the noise loop.
- `build_reading_epub.py` alt-attribute escaping (B04). `data/noise.txt` carries
  B02-B08 blocks (longest literal first).
- `data/content_config.json`: docs+sources map for check_content, ch01-ch08.
  ADD ch09 when you translate it.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Transcription method (B08, confirmed again B10 on ch09 pages):** OCR is too
  noisy on the proper names; READ the 300-DPI page images (data/png/p####.png)
  directly and transcribe, cropping tight regions only for ambiguous names/numbers.
- **Parity gotcha:** in `data/zh/chNN.txt` mark the chapter title `### ` (like
  section heads), NOT `## `. English side: chapter title `## `, section heads `### `.
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the
  JSON top level; the builder needs them under people/organizations/places/terms.
  Add rows directly into those sub-objects with a re-read-verified one-shot.
- **Glossary `en` must be ASCII;** curly punctuation only in note bodies (numeric
  char refs), applied at the render layer.
- **VERY high-frequency recurring names with pronoun runs stay OUT of the entity
  glossary** (李克农/胡底): adding them fires false check_content displacement.
- **figures.json `file` is a BASENAME**; builder prepends `data/figs/`. `before`
  anchors fall in the FIRST ~80 chars of a paragraph, cannot sit on a heading.
- **Washed-out full-page chapter-divider illustrations** are design furniture, NOT
  captioned figures (exclude them; ch09's is p0208).
- Set-off block quotes render `{v}`; verse `{p}` (one line per source line);
  dateline `{d}`. `check_structure.py` strips markers before parity.

## Apparatus state after B10 (frozen doc = STYLE.local top sections)
- 290 notes. Densities (words/note): ch01 174, ch02 124, ch03 283, ch04 417,
  ch05 264, ch06 383, ch07 377, ch08 634. ch01 outlier corrected; residual
  extremes are structural (short ch02; long ch08 whose furniture is pre-noted).
- The Glossary of Recurring Terms (20 rows) and Street Gazetteer (24 streets) now
  carry the recurring furniture and the concession streets; gloss such terms ONCE
  at first appearance and let the back matter carry the rest. When drafting ch09,
  flag any NEW recurring institutional term `recurring:true` and any NEW concession
  street `gazetteer:true`+`today` so they join the back matter automatically.
- Marker placement: put a marker at the end of the clause/sentence that holds the
  referent, never mid-phrase (a marker right after a complete referent noun-phrase
  is fine). Draft ch09's markers this way from the start.

## Renderings settled (also in glossary.json / STYLE.local.md)
- Consistency canon (verified clean): Center (not Centre), the Politburo (not
  "Political Bureau"), the White Terror (capitalized), the Xujiahui Observatory
  (not Zikawei), Lazily Seeking Old Dreams (italic), Carter Road (not Cardan),
  the June 3 1932 Comintern report as one document, fused lane names, the ten-li
  foreign quarter, presiding pastor, Gu Shunzhang born 1895. Dates month-day-year.
- 中央特科 the Central Special Branch (handle: the Special Branch); 红队 / 打狗队 the
  Red Squad / the dog-beating squad; 中统 the Zhongtong; 党务调查科 the Party Affairs
  Investigation Section (handle: the Investigation Section). Spelling: AMERICAN.
- For ch09: 向忠发 = Xiang Zhongfa (in glossary; keep OUT of the entity-checked set
  if pronoun runs are heavy -- check); 黄慕兰 = Huang Mulan; 陈志皋 = Chen Zhigao;
  探勒车行 = the Delle Motor Garage (per book.json title_en); 潘汉年 Pan Hannian and
  谭嗣同 Tan Sitong already glossed (ch01). Consult authority.json before romanizing.

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with a
  sardonic edge; heat in the verbs and rhythm, ration exclamation and rhetorical
  questions; sustained source-criticism as running skeptical argument in plain
  English, sources' own wrong words kept, verdict in the note; first person kept
  where he places himself as interviewer. His SARDONIC scare-quoting of hyped
  sources (the Huang Mulan memoir's blurb language in ch09 s2) is his voice --
  preserve it; do not iron it flat, but do not quilt unremarkable fragments either.
- **Martyr set-pieces run at full temperature, verdict in the note.**
- **Zhou Enlai** warm and big-brotherly; **Gu Shunzhang** the foil, hot and
  contemptuous; **Cai Mengjian / KMT memoirists** officialese, self-regarding;
  **Party leaders / descendants in interview** clipped, factual, contracted.

## Where the story stands
Chapters One-Eight are drafted, de-archaized, and now carry the B10 apparatus and
spine work. Chapter Nine, "The Riddle of Xiang Zhongfa's Disappearance," is the
direct sequel to Eight: Gu Shunzhang's defection exposes the CCP General Secretary
Xiang Zhongfa, seized at the Delle Motor Garage near Jing'an Temple on June 22,
1931, and executed in Shanghai days later; the chapter weighs the contested
sources on how he fell and whether he broke, and is skeptical of the "secret
cable." It is source-critical throughout, like Eight.

## Open traps / environment
- `data/zh/` and `data/png/` are gitignored; a fresh checkout has neither.
  ch09 drafting needs both (render + hand-transcribe from source.pdf, which IS
  tracked). The apparatus/spine work does not (English-only).
- Cross-check note AND figure anchors before any re-voicing edit
  (scripts/anchor_check.py). A broken figure `before` anchor fails the build.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; `pgrep -c tesseract` = 0 after
  OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch.
- Still UNTRANSLATED: ch09 (next batch), ch10-ch15, the Preface (ch00, PDF 6-15),
  and back matter (Works Cited ch16, Afterword ch17). They fold into later batches.
- Branch hygiene: canonical branch is `claude/the-sword-roars`. B10 started on a
  stray `claude/sword-roars-footnote-apparatus-i98qi6` (identical to canonical
  origin); consolidated and the stray deleted, local and remote.
