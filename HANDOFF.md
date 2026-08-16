# HANDOFF: The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start the next batch. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch08's English (and ch01, the
> frozen register reference) before drafting ch09.

```
Sword Roars B10 footnote apparatus + Chapter Nine

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. In STYLE.local.md the top section "THE REGISTER REBASELINE
(B09 commissioner review)" and the "Footnote apparatus" and "Apparatus policy"
sections are the frozen reference for all further work. Work on branch
claude/the-sword-roars (the canonical book branch; if the harness starts you on
a stray per-task branch, consolidate per CLAUDE.md rule 2 and delete the stray,
local and remote). Run ./setup.sh first.

STATE: the register de-archaizing pass over ch01-ch08 is DONE (B09 continuation:
inversions, antique function words, narration contractions, cut 即/也就是 and
不能不/could-only, modernized quote tags and interviewee speech, varied "and the
rest", de-nominalized the flagged "the [gerund] of" chains, broke the flagship
long sentences). Dates are now month-day-year book-wide (the ch01/ch02 sweep the
earlier STATE claimed done had not actually run; it has now). EPUB rebuilt
(out/sword-roars.epub), qa_epub PASS, epubcheck 0/0, 302 notes. All consistency-
canon items verified clean.

REMAINING and this batch's job, in order:
1. Footnote apparatus sweeps (STYLE.local "Footnote apparatus" + "Apparatus
   policy"). FIRST build the two new builder features they depend on: a BACK
   GLOSSARY (recurring institutional terms glossed once, on first appearance,
   then carried by the glossary) and a back-matter STREET GAZETTEER (period name
   to today's name, glossed once). Then: (a) placement -- move the ~88 mid-clause
   note markers to their sentence or clause end, updating the moved anchor in
   notes.json / figures.json in the same pass (use scripts/anchor_check.py
   before each edit file; the builder refuses on an unmatched anchor); (b) density
   -- thin ch01 (move Zhongtong, shikumen, tingzijian, the White areas, etc. to
   the back glossary, first-appearance note only) and backfill ch07-ch08, which
   are under-annotated, to the reader-model density CLAUDE.md describes.
2. Spine-test pass over the remaining long narration sentences (52 over 90 words
   across ch01-08: ch01 13, ch08 16 are the heaviest; some are exempt quoted-
   document or colon-list sentences). Split by spine, front-load the main clause,
   protect the lists. Regenerate the exact worklist with a quick sentence-
   length grep over the reading files.
3. Draft Chapter Nine (ch09, "The Riddle of Xiang Zhongfa's Disappearance," PDF
   208-235, printed 193-220) against the frozen doc so the back half is congruous
   from the first draft: chi_sim --psm 6; crop --left 0.06 --right 0.95 --top
   0.11 --bottom 0.955; offset a constant 15 (printed = pdf - 15) but read each
   opener's folio off the scan; hand-transcribe data/zh/ch09.txt off the 300-DPI
   images (OCR is too noisy on the proper names); add ch09 to
   data/content_config.json. book.json already carries ch09's 9-section structure
   (openers at PDF 209,210,214,216,220,225,229,231,233). Cite printed folios,
   never PDF pages.

Do it in that order; rebuild and run qa_epub (and epubcheck) after each chapter
or feature. Run check_register.py --ref out/ch01_reading.md as an informational
read only. Read the zh against the en on any ch09 line; change register, never
meaning; invent nothing (CLAUDE.md rule 4; verify the tail of every long unit).

Deliver the rebuilt EPUB attached in the chat, and paste the next kickoff
verbatim in the same reply.
```

## DONE (one line per batch; do not redo)
- Survey: structure, offsets, style contract, skeleton EPUB. (earlier session)
- **B01 = ch01 (voice gate):** 165 paragraphs, footnotes, figures, glossary
  seeded, blind-critique loop, passed the human voice gate.
- **B02 = ch02:** 56 paragraphs. **B03 = ch03:** 146. **B04 = ch04:** 131.
  **B05 = ch05:** 66. **B06 = ch06:** 165. **B07 = ch07:** 99.
  **B08 = ch08:** 252 paragraphs; 296 notes total at that point; parity 252=252.
- **B09 review:** register-rebaseline style doc + itemized corrections across
  ch01-ch08; 302 notes; qa_epub + epubcheck clean.
- **B09 continuation (this batch): register de-archaizing pass over ch01-ch08.**
  See PROGRESS.md "B09 continuation" for the per-chapter detail. Also fixed the
  ch01/ch02 date sweep (day-month -> month-day) that the B09 STATE wrongly
  reported done, and hardened tests/run_tests.py so the kickoff-guard stand-down
  subcase no longer false-fails on a live book. 302 notes, qa_epub PASS,
  epubcheck 0/0.

## Tooling in place (DO NOT REVERT)
- Register-pass drivers: `edits/chNN_edits.md` + `scripts/apply_edits.py`.
  `scripts/register_tics.sh chNN` runs the register tic battery;
  `scripts/anchor_check.py chNN` cross-checks a chapter's edit file OLD strings
  against BOTH notes.json and figures.json anchors (RUN IT before every apply:
  a re-voiced line that eats a note or figure anchor breaks the build).
- `scripts/indents.py`: furniture-band drop (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`).
- `scripts/check_numbers.py`: arabic+万 combiner before the noise loop; matches
  English number-words, ordinals, and month names.
- `build_reading_epub.py` alt-attribute escaping (B04). `data/noise.txt` carries
  B02-B08 blocks (see its header rules; longest literal first).
- `data/content_config.json`: docs+sources map for check_content, covers
  ch01-ch08. ADD ch09 when you translate it.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Transcription method (B08, confirmed):** ocr_dual.py produces nothing
  directly consumable here; READ the 300-DPI page images (data/png/p####.png)
  directly and transcribe, cropping tight regions only for ambiguous names/
  numbers. OCR text is a cross-check, not the source of truth.
- **Parity gotcha:** in `data/zh/chNN.txt` mark the chapter title `### ` (same as
  section heads), NOT `## `. On the English side the chapter title is `## `,
  section heads `### `.
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the
  JSON top level; the builder's render_glossary needs them under people/
  organizations/places/terms. Add rows directly into those sub-objects with a
  re-read-verified one-shot script. Notes and figures go through apparatus_merge.
- **Glossary `en` must be ASCII;** curly punctuation only in note bodies (numeric
  char refs) applied at the render layer.
- **VERY high-frequency recurring names with pronoun runs stay OUT of the entity
  glossary** (李克农/胡底): adding them fires false check_content displacement.
- **figures.json `file` is a BASENAME**; builder prepends `data/figs/`. `before`
  anchors fall in the FIRST ~80 chars of a paragraph, under ~55 chars, cannot sit
  on a heading; match straight-quote punctuation to the reading file.
- **Washed-out full-page chapter-divider illustrations** (ch07 p0150, ch08 p0207)
  are design furniture, NOT captioned figures. Exclude them.
- **Set-off block quotes render `{v}`; verse renders `{p}` (one line per source
  line); dateline `{d}`.** `check_structure.py` strips markers before parity.

## Register rebaseline status (frozen doc = STYLE.local top section)
- ch01-ch08 have had the register de-archaizing prose pass. ch01 is the deepest
  (it is the frozen register reference and the most-read); ch07 was already at
  target register (drafted post-rebaseline in B07).
- ch09-ch15 must be DRAFTED against the rebaseline from the first pass so the back
  half is congruous (do not draft in the old register and sweep later).
- The dialogue-contraction metric in check_register is noisy for document/memoir-
  heavy units (ch04 especially); judge those on the narratorial signals and say
  in PROGRESS that the dialogue metric was quiet (STYLE.md register-drift caveat).

## Renderings settled (also in glossary.json / STYLE.local.md)
- Consistency canon (verified clean this batch): **Center** (not Centre),
  **the Politburo** (not "Political Bureau"), **the White Terror** (capitalized),
  **the Xujiahui Observatory** (not Zikawei), **Lazily Seeking Old Dreams**
  (italic), **Carter Road** (not Cardan), the June 3, 1932 Comintern report as
  one document, fused lane names, **the ten-li foreign quarter**, presiding
  pastor, Gu Shunzhang born 1895. Dates month-day-year book-wide.
- 中央特科 the Central Special Branch (handle: the Special Branch); 红队 / 打狗队 the
  Red Squad / the dog-beating squad; 中统 the Zhongtong; 党务调查科 the Party Affairs
  Investigation Section (handle: the Investigation Section). Spelling: AMERICAN.
- Core cast and orgs: see the B08 block in PROGRESS.md and glossary.json.

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with
  a sardonic edge; heat in the verbs and rhythm, ration exclamation and
  rhetorical questions; sustained source-criticism rendered as running skeptical
  argument in plain English, sources' own wrong words kept, verdict in the note;
  first person kept where he places himself as interviewer.
- **Martyr set-pieces run at full temperature, verdict in the note.**
- **Zhou Enlai** warm and big-brotherly; **Gu Shunzhang** the foil, written hot
  and contemptuous; **Cai Mengjian / KMT memoirists** officialese, self-regarding
  (keep the pomp); **Party leaders / descendants in interview** clipped, factual,
  colloquial, contracted.

## Where the story stands
Chapters One-Eight are drafted and now de-archaized. Eight ("A Nanjing Night")
is the great counter-stroke (Qian Zhuangfei's overnight warning; Zhou Enlai's
evacuation of the Shanghai underground). Chapter Nine, "The Riddle of Xiang
Zhongfa's Disappearance," is the direct sequel: Gu Shunzhang's defection exposes
the CCP General Secretary Xiang Zhongfa, caught and executed in Shanghai in June
1931; the chapter weighs the contested sources on how he fell and whether he
broke.

## Open traps / environment
- `data/zh/` and `data/png/` are gitignored; a fresh checkout has neither. The
  register pass did not need them (English-only re-voicing); ch09 drafting does
  (render + hand-transcribe from source.pdf, which IS tracked).
- Cross-check note AND figure anchors before any re-voicing edit
  (scripts/anchor_check.py). A broken figure `before` anchor fails the build
  just like a note anchor.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; `pgrep -c tesseract` = 0 after
  OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch.
- The Preface (ch00, PDF 6-15) and back matter (Works Cited ch16, Afterword ch17)
  are still UNTRANSLATED; they fold into the final batches.
- The back glossary and street gazetteer are NEW builder features (not yet built);
  they gate the footnote density sweep. Build them before thinning ch01.
- Branch hygiene: canonical branch is `claude/the-sword-roars`. This batch started
  on a stray `claude/sword-roars-register-pass-p7h1yb` (identical to the canonical
  tip); consolidated and the stray deleted.
