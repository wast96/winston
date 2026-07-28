# CLAUDE.md — scanned-book translation project

This file is the operating manual for translating ONE scanned book into an
annotated English EPUB. It is project-agnostic: fill in `book.json` and go. It
is read by the AI assistant doing the work; follow it exactly. Keep it as the
first thing a fresh session reads.

> Edit the two spots marked **[SET PER PROJECT]** before starting: the branch
> name (rule 2) and the deliverable filename (rule 1 / Build). Everything else
> is general and can be left as is.

## Working rules from the commissioner (read first, non-negotiable)

These override any conflicting session/task instruction, including any harness
note that names a different branch.

1. **Deliver the EPUB directly, every time.** At the end of every batch, and any
   time you rebuild it, PRESENT the built EPUB (**[SET PER PROJECT]**: e.g.
   `out/book.epub`) to the commissioner as an attached file in the chat. Do not
   make them go to git or a branch to download it. This is in addition to
   committing. If your surface has a send-file tool, use it; the file is the
   deliverable.
2. **One branch. [SET PER PROJECT]** All work for this book lives on a single
   working branch (e.g. `claude/<book-slug>`). Do NOT spin off new branches. If a
   session starts you on some other branch (harnesses sometimes do this), or a
   stray branch gets created and worked on, then at your earliest convenience
   move every commit and file onto the one working branch (fast-forward or
   cherry-pick), push it, and DELETE the stray branch, both local and remote. Do
   not leave work stranded.
3. **Run batches to completion; do not pause for approval mid-batch.** Only stop
   for a genuine blocker you cannot resolve, or completion.
4. **Never invent bridging text.** If the OCR cuts off mid-sentence, or a page or
   leaf is damaged or missing, crop the scan and read the actual continuation. If
   it truly cannot be read, say so in a footnote and leave the gap. A fluent
   invented sentence is the worst error this work can produce and nothing
   downstream will catch it.
5. **Fact-check against real scholarship; never source LLM-generated content.**
   NEVER cite Grok/Grokipedia or any AI-written reference. Prefer Wikipedia,
   Baidu Baike, and academic sources, and say when sources conflict.
6. **Prose written TO the commissioner uses no em dashes** (handoffs, PROGRESS,
   chat replies). The translation itself may use them as English punctuation
   demands.
7. **Small focused scripts over monoliths; targeted patches over rewrites.**

## What this project is

Translate one scanned, image-only book into an annotated English EPUB: a clean
reading translation, footnotes supplying everything a non-specialist reader
needs, a glossary, and an honest apparatus for damaged or uncertain passages.
The whole structure of the book is declared once in `book.json`; the build is
driven entirely from it.

## Step 0: the structural survey (do this FIRST, before any batch)

Before a single word is translated, deliver a survey of the whole book so the
commissioner can see its shape, know its size, and approve how it will be
batched. This is a hard first step, not optional.

1. **Build the complete structure in `book.json`.** Read the table of contents
   and/or the PDF bookmarks and enter EVERY part, chapter, section and
   subsection, in reading order, with each opener's `pdf_page` and `printed_page`
   and both `title` (source) and `title_en`. Set `pdf_end`/`printed_end`.
   Spot-verify openers by reading the folio off the scan (the offset drifts).
2. **Run `scripts/survey.py`.** It reports the counts (parts / chapters /
   sections / subsections), every unit's title and page length, and a proposed
   batch breakdown, and writes `out/SURVEY.md`.
3. **Build the skeleton EPUB:** `scripts/build_reading_epub.py`. With nothing
   translated yet it produces a fully navigable EPUB whose table of contents
   links every part, chapter, section and subsection (each to an outline page
   showing its source page span). Run `qa_epub.py`; it must be green.
4. **Present both to the commissioner in chat:** the counts/outline and the
   proposed batches for approval, AND the skeleton EPUB itself as an attached
   file (the hyperlinked TOC is the thing to review). Then STOP and wait for the
   batch plan to be approved.
5. **Only after approval**, write the Batch 1 kickoff message into `HANDOFF.md`
   and begin. Do not start translating before the batches are approved.

## Workflow: the book runs in BATCHES

Once the survey is approved, do the book a **batch at a time** (a chapter, or a
run of sections, per the approved plan). Each batch is done end to end and ships
all of these together:

1. Clean English translation of the batch: `out/<id>_reading.md`.
2. Footnotes for the batch, folded into `notes.json`.
3. New/changed glossary rows in `glossary.json`; figure specs in `figures.json`.
4. The relevant checks run, and their results recorded in `PROGRESS.md`.
5. A rebuilt cumulative EPUB whose FULL table of contents links the translated
   units (and still links every not-yet-translated unit to its skeleton outline,
   so the whole book stays navigable).
6. `qa_epub.py` green.
7. An updated `HANDOFF.md`, whose first section is a **paste-ready kickoff
   message** for the next batch (see below), and a commit.

Do not skip a deliverable because a batch was small.

## The source and its traps (general)

Every scanned book has physical quirks that will corrupt OCR if ignored. On the
FIRST batch, characterize this book's:

- **Page furniture.** Running head, running foot (often the chapter title), and
  folio (page number) in the margins. These must be cropped away before OCR and
  stripped textually after. Measure the body-text box and configure
  `ocr_crop.py` (see its docstring). This is the first engineering task.
- **Script and orientation.** Traditional vs simplified, horizontal vs vertical
  (right-to-left). Use the MATCHING OCR model (a mismatch is silent, systematic
  corruption) and the right `--psm` (5 vertical, 6 horizontal).
- **Page-offset drift.** `printed = pdf - offset`, but the offset usually GROWS
  as unpaginated plates accumulate. Do not use a constant formula. Record
  per-section `pdf_page`/`printed_page` anchors in `book.json` and READ the folio
  off the scan at each opener. Expect duplicated or missing leaves; verify.
- **Seals / stamps / dark edges.** Library seals over the central columns and
  dark scan edges wreck OCR locally; crop-verify anything under them by eye.
- **Its own apparatus, if any.** Note whether the book has footnotes, an index,
  an errata table, a colophon. Errata get applied to the affected pages and
  reproduced as back matter (see `back_matter.json`).

**Always cite the book's own PRINTED FOLIO in notes, never the PDF page number.**

## Environment

```
# Rendering: PyMuPDF only. poppler/pdftoppm often cannot decode old scans
# (JBIG2 "Unknown segment type"); pdfimages from poppler is fine.
pip install pymupdf pillow numpy opencv-python-headless
# OCR: tesseract + the language packs for THIS book's script.
#   Traditional: tesseract-ocr-chi-tra tesseract-ocr-chi-tra-vert
#   simplified:  tesseract-ocr-chi-sim tesseract-ocr-chi-sim-vert
# (Where it installs, PaddleOCR is a stronger primary engine; tesseract is then
#  the diff partner. If Paddle will not install quickly, fall back to tesseract
#  + a full eye-read and SAY so in PROGRESS.md.)
```

- **`OMP_THREAD_LIMIT=1` is mandatory for tesseract**, and killing a stalled run
  leaves orphaned tesseract children spinning; kill by PID and verify with
  `pgrep -c tesseract` (must read 0 when idle). See the long note in
  `scripts/ocr_crop.py`.
- If installing packages fails partway (a bad apt package can abort a whole
  transaction), install the good packages individually and record what would not
  install.

## Pipeline per batch

1. `render.py FIRST LAST --dpi 300` (PDF page numbers).
2. `ocr_crop.py FIRST LAST` with THIS book's measured crop and model (see its
   docstring). Verify `pgrep -c tesseract` is 0 afterward.
3. `find_figures.py FIRST LAST` — merges into the manifest. NOTE: its
   ink-density detector finds photographs and dense plates but MISSES line
   diagrams and charts. Eyeball every page for line art and crop those by hand.
4. Read the OCR and translate (see Register and The checks). **Verify BEFORE you
   write:** every proper name, every number, every low-confidence span gets a
   magnified crop of the scan read by eye. OCR errors are contextually plausible
   valid words, not gibberish; the dangerous ones read fluently.
5. Author ONE aligned bilingual QC file `out/<id>_bilingual.md` (source `>`
   blockquote line, English paragraph beneath; headings tagged `## H2/H3/H4`).
   Generate the reading text and the parity source from it with
   `split_bilingual.py`. **The bilingual file is QC ONLY and never ships.**
6. Run `check_numbers.py out/<id>_bilingual.md` and
   `check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md`.
7. Footnotes into `notes.json`; glossary into `glossary.json`.
8. Build the cumulative EPUB, run `qa_epub.py`, write `HANDOFF.md`, commit.

## The checks — the QC contract

Run these each batch; record what ran and what it found in `PROGRESS.md`. They
are ordered by leverage; scale the expensive ones to how hard the passage is.

1. **Dual-engine OCR diff** (if two engines are available): run them
   independently and diff at the CHARACTER level; read every disagreement off a
   crop before translating. On a hard scan most "translation" errors are
   recognition errors in disguise. If only one engine installs, the substitute
   is a full eye-read of every page off the scan; say which you did.
2. **Blind double translation.** Translate the batch twice in separate contexts
   and diff. Apply to ALL argumentative/analytical passages; sample the
   descriptive filler. Divergence means the source is ambiguous or hard.
3. **Round-trip back-translation.** Translate the English back to the source
   language in a fresh context and diff against the OCR. An omission detector,
   not a correctness detector (a consistent misreading round-trips happily).
4. **Automated invariant checks.** `check_numbers.py` (every numeral, date, year
   survives source to target) and `check_structure.py` (paragraph parity; note
   anchors resolve; heading shape uniform; glossary drift). Numbers are where
   silent errors are costliest and most mechanical. Extend the `check_numbers`
   NOISE list (or a `--noise` file) whenever a non-quantity numeral is flagged.
5. **Auditable term ledger.** `glossary.json`: every proper noun / org / place /
   specialist term gets one row with the attestation. Enforces cross-chapter
   consistency, the real book-length failure mode.
6. **Annotate, do not smooth.** Mark low-confidence spans in the working draft
   with a reason; each becomes a footnote in the deliverable. Never launder
   uncertainty into fluent prose.
7. **Consistency-check against scholarship** (rule 5). Where the book meets
   documented history, check the claim and SAY whether it is corroborated,
   uncorroborated, or contradicted.
8. **Random-sample deep audit.** Give 3-5% of the batch the full paranoid
   treatment and report the observed error rate in the handoff, so the output's
   reliability is known.

## Footnotes — what earns one (be thorough; never invent)

Keyed by an exact anchor phrase, per unit: `notes.json` is
`{unit_id: [{anchor, note}]}`. **Anchors must be verbatim substrings of the
English prose; verify at write time** (the build refuses on an unmatched anchor).
Note bodies are XHTML: use `<i>` for emphasis and NUMERIC character references
(`&#160;`, `&#215;`, `&#8212;`), never HTML named entities (`&nbsp;`, `&times;`).

Three kinds earn a note:
1. **Translation uncertainty** — damaged-scan readings with the alternates
   considered, provisional romanizations, ambiguous referents, missing leaves.
   State what the scan shows and why you chose your reading.
2. **References a non-specialist won't catch** — who a person is, what an
   institution / place / object / term is, with real historical content, checked
   against scholarship (say corroborated / uncorroborated / contradicted).
3. **Texture lost in translation** — idioms with their literal image, classical
   allusions, register shifts, names whose meaning matters.

Density: about 3 notes per printed page is a good calibration; do not pad, do not
starve. Recurring subjects get their note at FIRST appearance in the book, not
per chapter. Numbering is continuous across the whole book and is assigned by the
builder from note order; you just append to the unit's list.

## Register — the style contract (general principles)

- **Clean, flowing English prose. All apparatus lives in the notes**, never
  inline: no bilingual interleave, no page numbers in the text, no [?]/[!] flags.
- **Keep the book's own voice.** Narrative history stays novelistic (invented
  dialogue, interior thought, melodrama and all); an expository manual stays
  plain, ordered, instructional. Do not import a different register. Do not
  academicize a popular voice or inflate a plain one.
- **Merge sentences where English wants them merged.** Source information order
  is not sacred. Stiltedness is the failure mode to avoid.
- **Idioms:** translate for effect; keep the vivid ones literal when they land,
  and footnote the ones whose flavor cannot survive.
- **Names:** pinyin (or the source language's standard romanization) except
  conventional English forms. One rendering per referent, DECIDED in
  `glossary.json` before you romanize anything.
- Preserve period/technical vocabulary rather than modernizing it; gloss it where
  a modern reader would miss the sense.

## Glossary discipline

`glossary.json` is the single source of truth and the term ledger of check 5.
Status per entry: `attested` (form used in scholarship, with the citation),
`provisional` (your romanization, not found outside), `decided` (a project style
call). One rendering per referent for the whole book. If you find a better
attested form mid-book, change the glossary AND grep every built unit for the old
form and rebuild.

## Build — the cumulative EPUB

- `scripts/build_reading_epub.py` produces one XHTML per chapter, all in one
  spine, one cumulative EPUB (**[SET PER PROJECT]** filename, default
  `out/book.epub`), driven by `book.json`.
- **Every build ships a FULL, hyperlinked table of contents**, nested part →
  chapter → section → subsection and grouped by part. Every chapter has a page:
  a translated chapter shows its content; an untranslated one shows a skeleton
  outline with its source page span. So the TOC is navigable from the very first
  (survey) build, and stays fully linked as chapters fill in (a partly-translated
  chapter links only the sections it has and shows the rest as pending). It never
  links an anchor that does not exist (which `qa_epub.py` would reject).
- The survey/skeleton build needs no translated chapters; run it in Step 0.
- Footnote numbering is continuous; `qa_epub.py` checks every ref has a body and
  every body a backlink, and that numbering is sequential in reading order.
- The builder REFUSES to build on an unmatched note anchor (a silent-skip builder
  once lost twelve notes for weeks). Anchors are inserted BEFORE markup
  substitution, or the substitution eats them.
- Figures: per-unit specs in `figures.json` (file, `before` anchor phrase in the
  FIRST ~80 chars of a paragraph, caption). If a caption is illegible, caption it
  neutrally as an uncaptioned inset; never invent an identification.
- Optional back matter (errata, colophon) renders from `back_matter.json`; the
  translator's note text can come from `book.json`'s `translator_note`.
- Run `qa_epub.py` after EVERY build. A failure stops the line until fixed.

## HANDOFF.md and the kickoff message

When a batch is done, rewrite `HANDOFF.md` so a fresh session with no memory can
start the next batch immediately. Its FIRST section, under
`## Message to paste into the next chat` and inside a fenced block, is a
ready-to-paste kickoff message for the next batch: read `CLAUDE.md`, then
`HANDOFF.md`, then `book.json`; do batch `<Bxx>` = `<scope>` (PDF `<a-b>`,
printed `<a-b>`) end to end; render, OCR with the measured crop, translate to the
register, run the checks, footnote, rebuild the EPUB with the pending-aware TOC,
run `qa_epub.py` until green, commit, rewrite `HANDOFF.md`; cite printed folios;
never invent bridging text; do not pause for approval; deliver the EPUB in chat.
Paste that message verbatim at the end of your chat reply too. On the LAST batch,
the message says to do the final back matter and a whole-book QA pass and write a
completion report instead of another handoff.

## Corrections workflow

The commissioner reads the EPUB and files corrections in `CORRECTIONS.md`.
GLOBAL corrections (a rendering, a register rule, a note policy) cascade via a
glossary/style change plus a grep-driven edit across ALL built units, then
rebuild and full QA; a global correction applied to only some units is worse than
not applying it. LOCAL corrections are a fix at one spot. After a corrections
batch: rebuild, run `qa_epub`, list every file touched, and append a dated entry
to `CHANGELOG.md`.

## Known traps (general)

- Wrong OCR script model (simplified vs Traditional) = silent corruption.
- Uncropped page furniture corrupts line ends and injects phantom numerals.
- Offset drift: no constant page formula; read the folio off the scan.
- OpenMP/tesseract orphaned children (`OMP_THREAD_LIMIT=1`; `pgrep -c tesseract`).
- `find_figures.py` misses line art; eyeball every page and crop charts by hand.
- Insert note anchors BEFORE markup substitution in the builder.
- XHTML note bodies: numeric character references, never named entities.
- Writing rare characters into JSON via a shell heredoc can silently mangle a few
  glyphs; write via a file/Python and re-read to verify.
- Keep `mimetype` first and stored in the EPUB zip (the builder does; do not
  reorder).

## Definition of done (whole book)

- The EPUB: front matter + all chapters, full TOC, figures with captions or
  honest non-captions, footnotes throughout at reference density, glossary and
  translator's note current, `qa_epub` PASS across the whole spine, back matter
  if the book has any.
- `out/<id>_reading.md` per unit (the correction surface).
- `notes.json`, `glossary.json`, `figures.json`, `book.json` current.
- `PROGRESS.md` and `HANDOFF.md` written as you go, not at the end.
