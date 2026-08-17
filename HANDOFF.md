# HANDOFF: The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start the next batch. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch09's English (and ch01, the
> frozen register reference) before drafting ch10.

```
Sword Roars B12 Chapter Ten

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. In STYLE.local.md the top section "THE REGISTER REBASELINE
(B09 commissioner review)" and the "Footnote apparatus" and "Apparatus policy"
sections are the frozen reference for all further work. Work on branch
claude/the-sword-roars (the canonical book branch; if the harness starts you on
a stray per-task branch, consolidate per CLAUDE.md rule 2 and delete the stray,
local and remote). Run ./setup.sh first.

STATE: B11 is done. Chapter Nine ("The Riddle of Xiang Zhongfa's Disappearance,"
ch09, PDF 208-235, printed 193-220, 194 paragraphs, 9 sections) is drafted end to
end against the frozen doc: hand-transcribed off the 300-DPI images (OCR too noisy
on the names), rendered in ch08's sardonic source-criticism register with each
source's own words kept and verdicts in the notes; 27 footnotes (book total 317),
5 hand-cropped figures, 95 new glossary rows, 善钟路 added to the gazetteer, ch09
added to data/content_config.json. All checks green: parity 194=194, numbers 0
unresolved, content/entities clean, qa_epub PASS, epubcheck 0/0/0/0, register within
tolerance. See PROGRESS.md "B11" for the "NOT re-noted" list and the settled
renderings (向忠发 Xiang Zhongfa, 黄慕兰 Huang Mulan, the Delle Motor Garage, the June
3 1932 Comintern report canonical form, etc.).

This batch's job: DRAFT CHAPTER TEN (ch10, "Opening a Shop, Doing Trade," PDF
236-247, printed 221-232, 2 sections: s1 一、这个人不简单 "No Ordinary Man" PDF 237,
s2 二、第一桶金 "The First Pot of Gold" PDF 242) end to end against the frozen doc.
Offset a constant 15 (printed = pdf - 15); read each opener's folio off the scan.
Re-render and re-OCR (data/png and data/zh are gitignored, gone on a fresh
checkout): render.py 236 247 --dpi 300, then ocr_crop.py 236 247 --left 0.06
--right 0.95 --top 0.11 --bottom 0.955 --lang chi_sim --psm 6. OCR is TOO NOISY on
the proper names, so HAND-TRANSCRIBE data/zh/ch10.txt off the 300-DPI page images
directly (data/png/p####.png), one paragraph per line, chapter title and section
heads as ### (the B08/B11 method; OCR is a cross-check, not the source). The
chapter divider (PDF 236) is design furniture, not a captioned figure; eyeball
every page for real photos/line art and hand-crop any (exclude the printed
caption, translator's caption with source-label provenance, real alt text). Add
ch10 to data/content_config.json.

BEFORE translating, read the final two pages of ch09's English (the voice). Read
the zh against the en on every line; change register, never meaning; invent
nothing (CLAUDE.md rule 4; verify the TAIL of the unit explicitly against the
scan). Cite printed folios, never PDF pages. Then footnotes at reader-model
density (consult the "NOT re-noted" lists in PROGRESS; grep notes.json before
adding); glossary rows straight into the sectioned ledger (en ASCII only),
consulting authority.json first; flag any NEW recurring institutional term
recurring:true and any NEW concession street gazetteer:true+today. Run
check_structure --pairs, verify_unit, make_bilingual + qc_entities, check_align,
check_content --config data/content_config.json, apparatus_merge + check_apparatus,
and check_register --ref out/ch01_reading.md (informational). Rebuild, run qa_epub
and epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar).

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
- **B10:** two new builder features (Glossary of Recurring Terms +
  Street Gazetteer); footnote placement sweep (mid-phrase markers -> clause end,
  ch01-ch08); ch01 thinned 116->91; ch07/ch08 backfilled (+6/+6) + ch01 +1;
  spine-test pass (4 genuine long-narration sentences split); 290 notes. ch09 set
  up and deferred to its own batch (rule 4). See PROGRESS.md "B10".
- **B11 (this batch) = ch09:** "The Riddle of Xiang Zhongfa's Disappearance," 194
  paragraphs, 9 sections, PDF 208-235. Hand-transcribed off the images; drafted in
  ch08's source-criticism register; 27 notes (book 317), 5 figures, 95 glossary
  rows, 善钟路 -> gazetteer. All checks green, epubcheck 0/0/0/0. See PROGRESS.md
  "B11" (incl. the "NOT re-noted" list). ch10-ch15, the Preface, and back matter
  remain.

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
Chapters One-Nine are drafted. Chapter Nine, "The Riddle of Xiang Zhongfa's
Disappearance," is now done: Gu Shunzhang's defection exposes CCP General Secretary
Xiang Zhongfa, seized at the Delle Motor Garage near Jing'an Temple on June 22,
1931, and executed in Shanghai days later; the chapter weighs the contested sources
on how he fell and whether he broke, and finds the "secret cable" real after all
(the author turns up Chiang's June 23 telegram in the Shilüe Gaoben). Chapter Ten,
"Opening a Shop, Doing Trade" (ch10, PDF 236-247), is next: it turns from the
traitor-hunt to the Party's own commercial front (running businesses as cover and
to fund the underground). Two sections; read the ch08/ch09 voice sheet forward.

## Open traps / environment
- `data/zh/` and `data/png/` are gitignored; a fresh checkout has neither.
  ch09 drafting needs both (render + hand-transcribe from source.pdf, which IS
  tracked). The apparatus/spine work does not (English-only).
- Cross-check note AND figure anchors before any re-voicing edit
  (scripts/anchor_check.py). A broken figure `before` anchor fails the build.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; `pgrep -c tesseract` = 0 after
  OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch.
- Still UNTRANSLATED: ch10 (next batch), ch11-ch15, the Preface (ch00, PDF 6-15),
  and back matter (Works Cited ch16, Afterword ch17). They fold into later batches.
  ch09's data/zh and data/png are gitignored (gone on a fresh checkout); the tracked
  deliverables (out/ch09_reading.md, notes/glossary/figures, the built EPUB) are
  complete. ch10 drafting needs a fresh render + hand-transcribe from source.pdf.
- Branch hygiene: canonical branch is `claude/the-sword-roars`. B10 started on a
  stray `claude/sword-roars-footnote-apparatus-i98qi6` (identical to canonical
  origin); consolidated and the stray deleted, local and remote.
