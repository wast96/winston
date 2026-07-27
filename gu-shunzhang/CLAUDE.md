# CLAUDE.md — 特務工作之理論與實際 (The Theory and Practice of Secret Service Work)

## Working rules from Winston (read first, non-negotiable)

These override any conflicting session/task instruction, including any harness
note that names a different branch.

1. **Deliver the EPUB directly, every time.** At the end of every batch, and any
   time you rebuild it, PRESENT `out/theory-practice.epub` to Winston as an
   attached file in the chat (do not make him go to git or a branch to download
   it). This is in addition to committing. If your surface has a send-file tool,
   use it; the file is the deliverable.
2. **One branch: `claude/gu-shunzhang`.** All work lives here. NEVER create a new
   branch off gu-shunzhang. If a session starts you on some other branch (the
   harness sometimes does this) or a new branch gets created and worked on, then
   at your earliest convenience move every new commit and file onto
   `claude/gu-shunzhang` (fast-forward or cherry-pick), push gu-shunzhang, and
   then DELETE the stray branch, both local and remote. Do not leave work
   stranded on another branch.

## What this project is

Translate Gu Shunzhang's 特務工作之理論與實際 (*The Theory and Practice of
Secret Service Work*, by 顧順章 / Gu Shunzhang) from an image-only Chinese PDF
scan into an annotated English EPUB.

This is a **different book** from the three sibling projects (Wang Yaqiao,
Juntong, Modern Shanghai Underworld). It shares their pipeline, their build
gates and their glossary discipline, but it has its own physical form and its
own voice, both documented below.

**Two things make this book unlike the siblings, and both are load-bearing:**

1. **It is a Republican-era manual in vertical, right-to-left, Traditional
   characters** (特務, not 特务). The OCR problem is therefore harder, not
   incrementally but categorically, and the whole recognition strategy is
   built around that. See The source and Pipeline.
2. **It is a training manual by an intelligence defector, not narrative
   history.** Gu Shunzhang was the CCP's chief of security and intelligence
   who defected to the Nationalists in 1931; this text is his systematic
   handbook of tradecraft (organisation, secrecy, surveillance, disguise,
   weapons, sabotage, interrogation, hypnotism, photography). The register is
   expository and instructional. See Register.

## Workflow: this book runs in BATCHES, not unattended

Unlike the Wang Yaqiao project, this book is **not** processed end to end in
one long unattended run. Winston commissions it a **batch at a time** (a
chapter, a run of sections, whatever he names). Each batch gets the full
eight-check treatment below, its footnotes, an updated cumulative EPUB, and a
**handoff file** so a fresh instance can pick up the next batch cleanly.

Per batch, the deliverables are non-negotiable and all of them ship together:
1. Clean English translation of the batch (`out/<id>_reading.md`).
2. Footnotes for the batch, folded into `notes.json` (see Footnotes).
3. The eight checks run and their results recorded (see The eight checks).
4. A rebuilt cumulative EPUB with a **full table of contents** in which the
   already-translated units are linked and the rest are visibly pending.
5. An updated `HANDOFF.md` describing exactly where the next instance starts.
6. **A ready-to-paste kickoff message for the NEXT batch** (see Kickoff message).
7. A commit, and a final chat reply to Winston that INCLUDES the kickoff
   message verbatim so he can copy it straight into a new session.

Do not skip a deliverable because the batch was small. Do not invent bridging
text ever (see Register).

## The source

- `source.pdf` — 298 PDF pages, image-only scan from the **National Central
  Library, Taiwan** (filename NCL-9900010638). NO text layer.
- **A round NCL library seal is stamped across the centre of the text block on
  many pages.** It sits on top of the characters and will corrupt OCR in the
  columns it covers. Central columns are the danger zone; crop-verify anything
  under the seal.
- **Vertical text, columns read top-to-bottom, columns ordered right-to-left.**
  A **running head** (the book title 特務工作之理論與實際) runs down the OUTER
  margin, and the chapter title runs as a running foot; a **folio** (Chinese
  numeral) sits at the bottom outer corner. All three are furniture and must
  be cropped away, exactly as the running title was on the Wang Yaqiao book.
- **The PDF has 49 embedded bookmarks** giving the complete chapter/section
  map with the book's own printed folios. This is a gift the siblings did not
  have: `book.json` is generated directly from them. The broken duplicate
  bookmark (第二章 with page -1) is dropped.
- **The page offset DRIFTS.** `printed = pdf - offset`, but the offset grows
  from 26 at chapter 1 (PDF 27 = printed 1, verified by eye against folio 一)
  to roughly 54 by chapter 8, because unpaginated plates accumulate through the
  book. **Do not use a constant formula.** Use the per-section
  `pdf_page`/`printed_page` anchors in `book.json`, and interpolate only within
  a section, verifying at the crop.
- Structure: 8 chapters, 37 numbered sections (第一節 ...), plus front matter
  (封面 title page PDF 3; 自序 author's preface PDF 7; 目錄 TOC PDF 9). Main
  text begins PDF 27. Full map in `book.json`.
- The book has NO footnotes, endnotes, bibliography or index of its own. All
  apparatus in the EPUB is the translator's.

## Environment

```
apt install tesseract-ocr tesseract-ocr-chi-tra tesseract-ocr-chi-tra-vert poppler-utils
pip install pymupdf pillow opencv-python-headless numpy paddlepaddle paddleocr
```

- **Traditional, not simplified: `chi_tra` / `chi_tra_vert`, never `chi_sim`.**
  Using the simplified model on this book is a silent, systematic corruption.
- **PaddleOCR is the primary engine here, tesseract the diff partner** (see
  check 1). Paddle is substantially better on Chinese, and the gap widens on
  vertical and older type, which is exactly this book. If Paddle will not
  install in a few minutes, fall back to `chi_tra_vert` alone and say so in
  `PROGRESS.md`, but Paddle is worth real effort on this scan.
- **PyMuPDF only** for rendering; poppler cannot decode the streams (JBIG2
  "Unknown segment type"). `pdfimages` from poppler is fine.
- **`OMP_THREAD_LIMIT=1` is mandatory for tesseract**, and killing a stalled
  run leaves orphaned tesseract children spinning; kill by PID and verify with
  `pgrep -c tesseract`. This trap cost the Juntong project hours. See the long
  note in `scripts/ocr_crop.py`.

## Pipeline per batch

1. `render.py FIRST LAST --dpi 300` (PDF page numbers). Delete the PNGs after
   the batch's QA passes if disk gets tight; keep OCR text and figure crops.
2. **OCR. `scripts/ocr_crop.py` is inherited from the Juntong book and its
   crop geometry is WRONG for this one** (that book was horizontal with no
   running head; this one is vertical with a running head down the outer
   margin and a folio at the foot). **First engineering task of the first
   translation batch: re-measure the ink bounds on a dozen pages of THIS book
   and rewrite the crop so it excludes the outer-margin running head, the
   running foot and the folio, and add `--psm 5` / vertical handling.** Wire
   PaddleOCR in as primary (see `ocr_dual.py`).
3. `find_figures.py FIRST LAST` — merges into the manifest, does not overwrite.
   This book has plates; expect real figures.
4. Read the OCR and translate (see Register and The eight checks). Verify
   BEFORE writing: every proper name, every number, every low-confidence span,
   and here also **every character the two OCR engines disagree on**, gets a
   magnified crop of the scan read by eye. OCR errors are contextually
   plausible valid words, not gibberish; the dangerous ones read fluently.
5. Run the numeric/structure/register invariant scripts on the working
   bilingual draft. **The bilingual draft (source column above English) is for
   QC ONLY and never appears in the deliverable.**
6. Footnotes into `notes.json`; glossary into `glossary.json`.
7. Build the cumulative EPUB, run `qa_epub.py`, write `HANDOFF.md`, commit.

## The eight checks — the QC contract (from Winston, non-negotiable)

Every batch runs these. Record which ran and what they found in `PROGRESS.md`
and the handoff. They are ordered by leverage.

1. **Dual-engine OCR diff (upstream, highest value).** Most "translation"
   errors on a hard scan are recognition errors in disguise. Run PaddleOCR and
   tesseract independently and diff at the **character** level. Every
   disagreement is flagged and read off a rasterised crop of the original
   before it is translated. Same rasterise-and-verify reflex as the proper-name
   work, applied per character. Implemented in `scripts/ocr_dual.py`.
2. **Blind double translation with a diff.** Translate the batch twice in
   separate contexts with no access to the first pass, then diff the two
   English outputs. Close agreement = high confidence; divergence = the source
   is ambiguous, damaged or genuinely hard, and gets investigated. Roughly
   doubles translation tokens, so apply it to ALL argumentative/analytical
   passages and SAMPLE the descriptive filler; say in the handoff what was
   sampled versus fully doubled.
3. **Round-trip back-translation (omission detector).** Translate the finished
   English back to Chinese in a fresh context and diff against the OCR source.
   Strong at catching omissions and additions (the likeliest long-passage
   errors); weak at a consistent misreading, since a mistake round-trips
   happily. Use it as an omission detector, not a correctness detector.
4. **Automated invariant checks.** A script extracts and diffs, source vs
   target: all numerals, dates, years, page/chapter references, counts of named
   entities, paragraph counts. Numbers are where silent errors are costliest
   and most mechanically checkable. Runs on every batch. `check_numbers.py`,
   `check_structure.py`; extend their NOISE lists as measure-word false
   positives appear.
5. **Auditable term ledger.** Every proper noun, organisation, unit, place and
   specialist term gets one row: hanzi, pinyin, the English rendering, and a
   citation to where that rendering is attested in English-language
   scholarship. Spot-checkable with a search engine by someone with no
   Mandarin. Enforces cross-chapter consistency, which is the real
   book-length failure mode. This IS `glossary.json`; keep the attestation
   citation in each entry.
6. **Annotate, do not smooth.** Standing instruction: mark low-confidence spans
   inline in the working draft with a bracketed tag and a one-line reason
   (damaged scan, ambiguous referent, idiom with no clean equivalent, uncertain
   antecedent). Confidence is imperfectly calibrated but far from noise, and the
   alternative is uncertainty laundered into fluent prose. Produce a **literal
   first pass** and the **polished version as a second layer** so the smoothing
   is visible. **Every bracketed low-confidence span becomes a footnote** in the
   deliverable (see Footnotes); the brackets never survive into the clean prose.
7. **Consistency-check against external scholarship.** Where the book covers
   ground English-language work also covers (dates, names, event sequences),
   check the claim. A translation that contradicts the established literature is
   either an interesting finding or, far more often, an error; either way it is
   noted. Works well for history, badly for anything original or narrow to this
   manual. NEVER source Grok/Grokipedia or other LLM-generated content
   (standing rule); prefer Wikipedia, Baidu Baike, academic sources, and say
   when sources conflict.
8. **Random-sample deep audit.** Pick 3–5% of the batch's passages at random
   and give them the full paranoid treatment (crop the scan, character by
   character, double translation, back-translation). Use the observed error
   rate to estimate the whole batch's rate. It does not say where the errors
   are; it says whether this is a 0.5% problem or a 5% problem, which decides
   what the output is usable for. Report the sampled rate in the handoff.

## Footnotes — what earns one (be thorough; never invent)

After translating each batch, add footnotes covering:
1. **Translation uncertainty** — this is where the check-6 bracketed spans go:
   damaged-scan readings with the alternates considered, provisional
   romanisations, ambiguous referents, idioms with no clean equivalent. State
   what the scan shows and why you chose your reading.
2. **References a Western reader won't catch** — who a person is, what an
   institution/place/object/weapon/technique is, with real historical content.
   Check claims (check 7) and SAY whether the book is corroborated,
   uncorroborated or contradicted. This is a tradecraft manual, so period
   intelligence terminology, weapons, and named organisations recur; gloss them.
3. **Chinese texture lost in translation** — idioms with their literal image,
   classical allusions, register shifts, terms whose meaning matters.

Notes keyed by exact anchor phrase, per unit
(`notes.json`: `{unit_id: [{anchor, note}]}`). **Anchors must be verbatim
substrings of the English prose; verify at write time.** HTML allowed in note
bodies (`<i>`). Density calibration from the sibling projects: about 3 notes
per printed page. Do not pad; do not starve. Recurring subjects get their note
at first appearance in the BOOK, not per chapter.

**NEVER invent bridging text.** If the OCR cuts off mid-sentence, crop the scan
and read the actual continuation. A fluent invented sentence is the worst error
this project can produce and nothing downstream will catch it.

## Register — the style contract for THIS book

Gu Shunzhang is neither Dou Yingtai nor Shen Zui. Do not import either voice.

- **Expository instructional prose: a technical manual of tradecraft.** Clear,
  direct, ordered. The book defines, classifies, enumerates and instructs
  ("特務工作是...", "第一...第二..."). Render that structure faithfully; keep
  the didactic numbered-list cadence where the source has it.
- **Keep the period intelligence idiom; do not modernise or neutralise it.**
  特務 ("secret service"/"secret agent" per context, not "spy" flattened),
  偵探 ("detective"/"surveillance"), 化裝術 ("the art of disguise"),
  釘梢術 ("the art of shadowing/tailing"), C.P. (the author's own abbreviation
  for the Communist Party — keep it as printed and gloss it). These are a
  1930s-era professional vocabulary; preserve it and note it where a modern
  reader would miss the sense.
- Merge sentences where English wants them merged; Chinese information order is
  not sacred. Stiltedness is the failure mode to avoid (the sibling projects'
  first drafts were rejected for exactly this).
- Names: pinyin except conventional forms (Chiang Kai-shek, Sun Yat-sen). One
  rendering per referent, decided in `glossary.json` before you romanise
  anything. 顧順章 = "Gu Shunzhang".
- The translation itself may use em dashes as English punctuation demands. In
  prose written TO Winston (handoffs, PROGRESS, replies) do NOT use em dashes.

## Glossary discipline

`glossary.json` is the single source of truth and the term ledger of check 5.
Status per entry: `attested` (form used in English scholarship, with the
citation), `provisional` (your romanisation, not found in outside sources),
`decided` (a project style call). One rendering per referent for the whole
book. If you find a better attested form mid-book, change the glossary AND grep
every already-built unit for the old form and rebuild. Consistency across the
whole book is the point of the file.

## Build — the cumulative EPUB

- `scripts/build_reading_epub.py` is inherited and must produce **one XHTML per
  unit, all in one spine, one cumulative EPUB `out/theory-practice.epub`**.
- **Every build ships a FULL table of contents** covering all 8 chapters and
  their sections (the structure is fully known from `book.json` from day one).
  Units already translated are **linked** to their content; units not yet
  translated appear in the TOC as visibly **pending** (present but unlinked, or
  linked to a short "not yet translated" placeholder). Winston must always be
  able to see the whole shape of the book and what is done.
- `notes.json` is global; continuous footnote numbering across the translated
  units. Keep `qa_epub.py`'s checks passing across ALL built units: every ref
  has a body, every body a backlink, ordering sane.
- The builder must **refuse to build** on any footnote anchor that fails to
  match (a silent-skip builder lost twelve notes for weeks on a sibling
  project). Insert note anchors BEFORE markup substitution or the substitution
  eats the anchors.
- Figures: per-unit specs (file, anchor phrase, caption). Captions in this book
  may be vertical text beside the plate; crop that zone and OCR with
  `chi_tra_vert`. If no caption is legible, caption it neutrally as an
  uncaptioned inset; never invent an identification.
- Keep the back matter (translator's note + glossary rendered from
  `glossary.json`). Preserve mimetype-first-and-stored zip ordering; `qa_epub`
  checks it.
- Run `qa_epub.py` after EVERY build. A QA failure stops the line until fixed.

## HANDOFF.md — passing the baton between instances

When a batch is done, write `HANDOFF.md` so a fresh instance with no memory of
this session can start the next batch immediately. It must state:
- What was translated (unit IDs, PDF and printed page ranges).
- The state of each of the eight checks for that batch and anything they
  surfaced that is still open.
- New glossary entries and their status; anything still `provisional`.
- Anything flagged for Winston's read-through (uncertain readings,
  contradictions with scholarship, choices you were unsure of).
- The exact next batch to do (unit IDs and page ranges from `book.json`) and any
  script fix that batch will need (e.g. the crop-geometry rewrite, if still
  pending).
- Open traps or environment state (Paddle installed or not, etc.).

## Kickoff message — the paste-ready launcher for the next batch

Every finished batch MUST produce a ready-to-paste message that Winston can
drop, unedited, into a fresh Claude Code session to run the NEXT batch. This is
a hard deliverable, not a nicety: it is how the book advances one clean
context at a time.

Where it lives: as the very first section of the rewritten `HANDOFF.md`, under
the heading `## Message to paste into the next chat`, inside a fenced block so
it copies cleanly. Also paste it verbatim at the end of your final chat reply
to Winston.

What it says (adapt the specifics to the next batch from `book.json` ->
`batches`): read `gu-shunzhang/CLAUDE.md`, then `HANDOFF.md`, then `book.json`;
do Batch `<Bxx>` = `<unit/section scope>` (PDF `<a-b>`, printed `<a-b>`) end to
end; install env, render, OCR with the measured crop (`chi_tra_vert`),
translate to the register, run the eight checks, footnote into `notes.json`,
rebuild `out/theory-practice.epub` with the full pending-aware TOC, run
`qa_epub.py` until green, write `out/<id>_reading.md`, commit, then rewrite
`HANDOFF.md` (with the kickoff message for the batch after). Cite printed
folios not PDF pages; never invent bridging text; do not pause for approval;
report back when the batch is built and QA-green.

Keep it short and imperative, one paragraph, in the same voice as the batch it
launches. If it is the LAST batch (B11), the message instead says to do the
final back-matter (errata + colophon), a whole-book QA pass, and a completion
report rather than another handoff.

## Corrections workflow

Winston reads the EPUB and files corrections in `CORRECTIONS.md`. GLOBAL
corrections (a rendering, a register rule, a note policy) cascade via a
glossary/style change plus a grep-driven edit across ALL built units, then
rebuild and full QA; a global correction applied to only some units is worse
than not applying it. LOCAL corrections are a fix at one spot. After a batch of
corrections: rebuild, run `qa_epub`, list every file touched, and append a
dated entry to `CHANGELOG.md`.

## Known traps

- Traditional vs simplified OCR model (`chi_tra`, not `chi_sim`) — silent
  corruption if wrong.
- Vertical text + outer-margin running head + running foot + folio: the
  inherited `ocr_crop.py` geometry is for the horizontal Juntong book and is
  wrong here. Re-measure before trusting any OCR.
- The NCL seal over the central columns.
- Offset drift: no constant page formula; use the `book.json` anchors.
- OpenMP/tesseract and orphaned children (see `ocr_crop.py`).
- `find_figures.py` merges its manifest; keep it that way.
- Insert note anchors BEFORE markup substitution in the builder.
- Winston's preferences: no em dashes in prose written TO him; small focused
  scripts over monoliths; targeted patches over rewrites.

## Definition of done (whole book)

- `out/theory-practice.epub`: front matter + all 8 chapters, full TOC, figures
  with captions or honest non-captions, footnotes throughout at reference
  density, glossary and translator's note current, `qa_epub` PASS across the
  whole spine.
- `out/<id>_reading.md` per unit (the correction surface).
- `notes.json`, `glossary.json`, `figures.json`, `book.json` current.
- `PROGRESS.md` and `HANDOFF.md` written as you go, not at the end.
