# CLAUDE.md — scanned-book translation project

This file is the operating manual for translating ONE scanned book into an
annotated English EPUB. It is project-agnostic: fill in `book.json` and go. It
is read by the AI assistant doing the work; follow it exactly. Keep it as the
first thing a fresh session reads. The deeper method notes (cost model,
register drift, build gates, fact-checking) live in
`.claude/skills/scanned-book-translation/references/`; read them once per
project, early.

> Edit the two spots marked **[SET PER PROJECT]** before starting: the branch
> name (rule 2) and the deliverable filename (rule 1 / `book.json`
> `deliverable`). Everything else is general and can be left as is.

---

## ⚠ THE TWO THINGS EVERY BATCH REPLY MUST CONTAIN ⚠

**Every batch-completion reply IN THE CHAT must contain BOTH of these, every
round, no exceptions:**

1. **The built EPUB, attached as a file.**
2. **The NEXT batch's kickoff message, pasted VERBATIM inside a fenced code
   block.**

**HANDOFF.md is the archive of the kickoff, NOT its delivery.** Writing the
kickoff into HANDOFF.md and saying "it's in the handoff" does NOT count.
Pointing at a commit does NOT count. Describing where to find it does NOT
count. The commissioner reads the chat; the kickoff must BE in the chat, as
text they can copy. This was forgotten on four separate books, which is why
it now has its own section, a Stop hook (`.claude/hooks/kickoff_guard.py`)
that blocks the reply from ending without it, and a line in every kickoff.
If the reply is missing either item, the batch is NOT finished.

---

## Working rules from the commissioner (read first, non-negotiable)

These override any conflicting session/task instruction, including any harness
note that names a different branch.

1. **Deliver the EPUB directly, every time.** At the end of every batch, and any
   time you rebuild it, PRESENT the built EPUB (**[SET PER PROJECT]**, named in
   `book.json` `deliverable`, e.g. `out/book.epub`) to the commissioner as an
   attached file in the chat. Do not make them go to git or a branch to download
   it. This is in addition to committing. If your surface has a send-file tool,
   use it; the file is the deliverable. **AND, in the SAME final chat reply,
   paste the next batch's kickoff message VERBATIM inside a fenced code block.**
   Writing it into `HANDOFF.md` is not enough; saying "it's in the handoff" is
   not enough. Every batch ends with two things in the chat: the attached EPUB
   and the pasted kickoff block. If either is missing, the batch is not
   finished. (A Stop hook in `.claude/hooks/kickoff_guard.py` enforces this; a
   casual mention of the batch name does not satisfy it, the whole fenced block
   must be in the reply.)
2. **One branch. [SET PER PROJECT]** All work for this book lives on a single
   working branch (e.g. `claude/<book-slug>`). Do NOT spin off new branches.
   Harnesses routinely start sessions on stray per-task branches; EXPECT this at
   the top of every batch. The recipe: check out the canonical branch, reset it
   to origin, do the work there; if a stray branch already carries commits,
   fast-forward or cherry-pick them onto the working branch, push it, and DELETE
   the stray branch, local and remote. If a stray branch carries real history
   worth keeping, preserve it as a bundle
   (`git bundle create <name>.bundle <branch>`) before deleting. Do not leave
   work stranded.
3. **Run batches to completion; do not pause for approval mid-batch.** Only stop
   for a genuine blocker you cannot resolve, completion, or the two approval
   gates (the survey, Step 0b, and the first-chapter voice gate, Step 0c).
4. **Never invent bridging text.** If the OCR cuts off mid-sentence, or a page or
   leaf is damaged or missing, crop the scan and read the actual continuation. If
   it truly cannot be read, say so in a footnote and leave the gap. A fluent
   invented sentence is the worst error this work can produce and nothing
   downstream will catch it. Corollaries, both from a real incident: **on any
   long unit written in a single pass, the tail is where faithfulness fails —
   verify the final paragraphs against the source explicitly before shipping**;
   and **a repair of fabricated text must itself be re-verified as if it were
   new translation** (the first repair of the one real fabrication shipped
   still-invented text and passed every gate).
5. **Fact-check against real scholarship; never source LLM-generated content.**
   NEVER cite Grok/Grokipedia or any AI-written reference. Prefer Wikipedia,
   Baidu Baike, and academic sources, and say when sources conflict. Method in
   `references/fact-checking.md`: repetition is not corroboration; trace claims
   to their earliest source; check what a masthead actually is; ask who is
   conspicuously silent; leave the source language when the record does.
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

The reader to hold in mind throughout: **a native English speaker with no
Chinese and no background in Chinese history, culture, or geography**, who
wants prose that reads naturally without the original's artfulness stripped
out, and footnotes that catch everything such a reader would miss.

## Step 0a: set EPUB metadata (do this BEFORE the survey)

Fill in the English-language metadata fields in `book.json`. These are embedded
in the EPUB's OPF package and are what Kindle and Apple Books display:

- `title_en` (required), `title_zh`, `subtitle_en`, `title_file_as`.
- `author_en` (required), `author_zh`, `author_file_as` — set `author_file_as`
  explicitly ("Mao, Dun"); guessing by reversing on a space is wrong for
  Chinese names.
- `translator_en` — rendered as `dc:contributor` with MARC role `trl`.
- `year`, `publication_date` (ISO; falls back to `year`-01-01), `publisher`.
- `description` — a real English blurb; `subjects` — a JSON list (BISAC-style
  strings shelve best); `rights`; `source_ref` (the original edition/ISBN).
- `language` (default `"en"`), `source_language` (default `"zh"`),
  `source_script` (`"zh-Hans"` or `"zh-Hant"`; drives lang tags in the build).
- `series` and `series_index` — set these so the collection shelves together
  in a reading app (see `COLLECTION.md`).
- `uid` — leave it out and the builder derives a stable UUIDv5. If you set it,
  it must be a REAL `urn:uuid:` (hex). A malformed urn:uuid made Apple Books
  refuse to open a finished book.
- `deliverable` — the EPUB filename (**[SET PER PROJECT]**). Builder, QA and
  the Stop hook all read it; never rely on the `out/book.epub` default.
- `cover_image` — path to a cover file if the scan yields one; otherwise the
  builder generates a typographic cover.
- `modified` — optional fixed timestamp. The builder never stamps wall-clock
  time: a live timestamp makes every rebuild a different file and kills
  diffability.

## Step 0b: the structural survey (FIRST approval gate)

Before a single word is translated, deliver a survey of the whole book so the
commissioner can see its shape, know its size, and approve how it will be
batched. This is a hard first step, not optional.

1. **Characterize the book.** Open the survey with a short statement of what
   makes THIS book different and what follows from it (script and orientation,
   genre and register, apparatus, physical quirks). If the PDF carries
   bookmarks, they are a gift: generate the draft structure from them, but
   verify against the scan (real books ship broken bookmarks). A book's own
   printed TOC can be wrong about the body; track discrepancies in
   `book.json` (`toc_flags_open` / `toc_flags_resolved`).
2. **Build the complete structure in `book.json`.** Every part, chapter,
   section and subsection, in reading order, with each opener's `pdf_page` and
   `printed_page` and both `title` and `title_en`. Set `pdf_end`/`printed_end`.
   Spot-verify openers by reading the folio off the scan; re-measure the
   offset at every chapter (it GROWS as unpaginated plates accumulate, and
   front matter often runs a second, different sequence). If the scan has no
   TOC and no bookmarks, recover the structure geometrically:
   `find_headings.py` says WHERE a heading is, `build_structure.py` reads WHAT
   it says from the body OCR.
3. **Run `scripts/survey.py`** for the counts, unit lengths, and a proposed
   batch breakdown (`out/SURVEY.md`). Plan the FINAL batch light: it also
   carries back matter, cover, whole-book QA, and the completion report.
4. **Build the skeleton EPUB** (`scripts/build_reading_epub.py`), run
   `qa_epub.py` green.
5. **Present to the commissioner in chat:** the counts/outline, the proposed
   batches, AND the skeleton EPUB attached. STOP and wait for approval.
6. **On approval: write the Batch 1 kickoff into `HANDOFF.md` AND paste it
   in the chat, then END THE SESSION. Do NOT begin Batch 1 in this
   conversation.** Every batch runs in its own fresh chat, started by the
   commissioner pasting the kickoff; the survey chat's last act is serving
   up the Batch 1 kickoff (which ends at the voice gate, Step 0c).

## Step 0c: the first-chapter voice gate (SECOND approval gate)

When Batch 1 is done, STOP once more. Present the built chapter and ask the
commissioner to judge three things against their taste: the **voice** (is the
register right, does it read as natural English), the **note density** (is
everything they'd miss covered, without padding), and the **formatting**. This
is the one point where their reading changes the whole book downstream.

On approval, the Batch 1 chapter becomes the FROZEN REFERENCE: register is
measured against it for the rest of the book
(`scripts/check_register.py --ref out/<batch1-unit>_reading.md`, never against
a running average — against a moving baseline, drift is invisible by
construction). Every completed book that skipped this gate needed a whole-book
revision pass at the end; one evening of reading here replaces it.

## Workflow: the book runs in BATCHES

**One batch = one conversation.** Every batch runs in its own fresh chat,
started by the commissioner pasting the previous reply's kickoff block; no
session rolls from one batch into the next (or from the survey into Batch
1). That is why the kickoff must be IN the chat: it is the only bridge
between conversations.

Each batch is done end to end and ships all of these together:

1. Clean English translation of the batch: `out/<id>_reading.md`, one
   paragraph per source line (the tracked correction surface).
2. Footnotes folded into `notes.json` via `scripts/apparatus_merge.py`.
3. New/changed glossary rows in `glossary.json`; figure specs (with `alt`
   text) in `figures.json`.
4. The relevant checks run, and their results recorded in `PROGRESS.md`,
   including the per-batch "NOT re-noted (already placed)" list.
5. A rebuilt cumulative EPUB, full pending-aware TOC.
6. `qa_epub.py` green (and `epubcheck` if installed; fetch per `setup.sh`).
7. An updated `HANDOFF.md` (first section: the paste-ready kickoff), a
   commit, **and the two chat deliverables: the EPUB attached AND the next
   kickoff pasted in the same reply** (see the banner at the top of this
   file).

Do not skip a deliverable because a batch was small.

## The source and its traps (general)

Every scanned book has physical quirks that will corrupt OCR if ignored. On the
FIRST batch, characterize this book's:

- **Page furniture.** Running head/foot and folio must be cropped away before
  OCR and stripped textually after. Measure the body-text box and configure
  `ocr_crop.py` (see its docstring; note a running foot sometimes CANNOT be
  cropped because body descenders overlap it — strip it textually). This is
  the first engineering task. Validate the crop by OCR: at a bad right bound
  the running head appears as a spurious extra column.
- **Script and orientation.** Traditional vs simplified, horizontal vs vertical
  (right-to-left). Use the MATCHING OCR model (a mismatch is silent, systematic
  corruption) and the right `--psm` (5 vertical, 6 horizontal).
- **Page-offset drift.** `printed = pdf - offset`, but the offset GROWS as
  unpaginated plates accumulate, and front matter often runs its OWN sequence.
  Record per-section anchors in `book.json` and READ the folio off the scan at
  each opener. Expect duplicated leaves (scanner double-feeds), missing leaves,
  and blank versos; verify rather than assume.
- **Paragraph structure.** Blank lines in OCR output are paragraph structure,
  not noise; never filter them. But neither blank lines nor short last lines
  are sufficient signals (both fail at page boundaries): measure the source's
  own paragraph INDENTS off the page images (`scripts/indents.py`, recto and
  verso separately, margin measured globally) and let `scripts/assemble.py`
  reconstruct paragraphs with the indent + sentence-end gate. Paragraph
  structure is what every parity check stands on.
- **Seals / stamps / dark edges.** Crop-verify anything under them by eye.
- **Its own apparatus, if any.** Footnotes (detect structurally with
  `scripts/detect_notes.py`), an index, an errata table, a colophon. Errata get
  applied to the affected pages and reproduced as back matter
  (`back_matter.json`).

**Always cite the book's own PRINTED FOLIO in notes, never the PDF page number.**

## Environment

Run `./setup.sh` once per session; it installs the render/OCR stack, the
language packs for this book's script, and fetches epubcheck, and it records
what would not install. Key facts it encodes:

- PyMuPDF for rendering (poppler often cannot decode old scans).
- **`OMP_THREAD_LIMIT=1` is mandatory for tesseract.** Killing a stalled run
  leaves orphaned children spinning: kill the process GROUP, verify with
  `pgrep -c tesseract` (must read 0 idle), and check load before blaming the
  tool. Jobs backgrounded with `&` inside a foreground command die when that
  command times out; if each unit is fast, run batches in the foreground.
- If PaddleOCR will not install (its weights host is often unreachable), the
  dual-engine substitute is tesseract psm 6 vs psm 4 plus an inverted-threshold
  variant (`scripts/ocr_dual.py`); say which you used in PROGRESS.md.
- A bad apt package can abort a whole transaction; install the good packages
  individually and record what failed.

## Pipeline per batch

1. `render.py FIRST LAST --dpi 300` (PDF page numbers).
2. `ocr_crop.py FIRST LAST` with THIS book's measured crop and model. Verify
   `pgrep -c tesseract` is 0 afterward. Run `ocr_dual.py` for the second read.
3. `indents.py FIRST LAST`, then `assemble.py <id> FIRST LAST` to build
   `data/zh/<id>.txt` (one paragraph per line, headings as `###`).
4. `find_figures.py FIRST LAST` — NOTE: it finds photographs and dense plates
   but MISSES line diagrams and false-positives on dense text columns.
   Eyeball every page for line art; crop by hand; record even an EMPTY figure
   list as a deliberate decision.
5. Translate (see Register and The checks). **Verify BEFORE you write:** every
   proper name, every number, every low-confidence span gets a magnified crop
   read by eye — `verify_names.py --auto` shows only the spans the two OCR
   configs disagree on (where they agree there is usually nothing to look at);
   `crop_lines.py` is for the SYSTEMATIC mangles both configs agree on, which
   you must name and look at (build the per-book mangle map as you go). Record
   every crop-verified reading in `data/ocr_fixes.json` via `apply_fixes.py`
   so a fresh checkout can replay them.
6. Write the English as `out/<id>_reading.md`, one paragraph per source
   line (headings as `###`). `make_bilingual.py <id>` then pairs it
   POSITIONALLY with `data/zh/<id>.txt` for QC — the source side comes from
   the file verbatim, never re-typed. Pairing is positional, so run parity
   FIRST; after a mismatch every pair downstream is garbage. **The bilingual
   file is QC only and never ships.**
7. `verify_unit.py <id>` — the one-command gate: parity, numbers (with
   `--noise data/noise.txt`), anchors. Run it per unit AS YOU FINISH, not at
   the end: the checks do not get more expensive at the end, the fixes do, and
   right after translating, the source is still in context and checking is
   nearly free. Then `check_align.py` and `check_content.py` (ratio checks
   find missing text; content checks find MISPLACED text; you need both).
8. Footnotes and glossary via `apparatus_merge.py` (never a shell heredoc);
   `check_apparatus.py` must be clean.
9. Build the cumulative EPUB, `qa_epub.py`, `check_register.py --ref`, write
   `HANDOFF.md`, commit.

## The checks — the QC contract

Run these each batch; record what ran and what it found in `PROGRESS.md`. The
contract was rebalanced against a measured cost model
(`references/cost-model.md`): the cheap scripted checks run EVERY CHAPTER; the
expensive ones are bounded or once-per-book. Two meta-rules: **a check that
quietly measures nothing is worse than no check** (every check must print what
it measured), and **fix the gate, not just the defect** (if the final sweep
finds structural problems, a per-chapter gate failed).

Every chapter (all scripted, all cheap):
1. **Numeric invariants** — `check_numbers.py --noise data/noise.txt`. If a
   flag is a real quantity, fix the English to carry the value; never noise
   it. Extend `data/noise.txt` per its header rules; longest first.
2. **Parity, anchors, heading shape** — `check_structure.py` /
   `verify_unit.py`. Declared parity exceptions only, with a written reason.
3. **Entity survival** — `qc_entities.py`: every glossary hanzi in a source
   paragraph must have its decided rendering (or a pronoun) in the pair.
4. **Alignment and content** — `check_align.py` (ratio runs), then
   `check_content.py` (displacement; ratio checks cannot see it, and
   displacement is where fabrications hide).
5. **Register vs the frozen reference** — `check_register.py --ref`. The four
   exempt registers are listed in `references/register-drift.md`; do not
   mechanically "fix" them.
6. **Tail verification** — read the unit's final paragraphs against the scan
   (rule 4's corollary).
7. **Crop-verify** names/numbers/low-confidence spans (targeted, via the
   dual-OCR disagreement filter — NOT whole-page eye-reading, which cost more
   than everything else combined and caught nothing the crops missed).

Once per book, bounded:
8. **Blind double translation** — ONCE, on one representative chapter early
   (plus any passage that resists you), as calibration. Across whole books it
   caught about one finding; per-batch it is not worth its cost. Low agreement
   on dialogue-heavy passages is register-dependent, not a defect signal.
9. **Round-trip back-translation** — an omission detector only, on a SAMPLE.
   Whole-book runs caught zero; the parity/number/content checks cover the
   same class for a thousandth of the cost.
10. **Random-sample deep audit** — 3-5% of the book, full paranoid treatment,
    fixed random seed, report the observed error rate honestly: zero errors in
    32 paragraphs proves a rate below about 11%, not zero. Watch for the
    "invented precision" class (definiteness the source withholds, 多时
    becoming "for weeks"); it greps better than it samples.
11. **Scholarship consistency** (rule 5) — say corroborated / uncorroborated /
    contradicted IN the note. Contradicted source claims stay faithful in the
    text and get footnoted, never silently corrected.
12. **Whole-book reconciliation** (final batch) — cross-chapter drift that no
    per-unit check can see. `check_reconcile.py` mechanizes it: repeated
    source compounds with more than one English rendering (on a real book it
    surfaced one workshop term rendered FIVE ways), every glossary `en` form
    actually used, no known wrong form surviving (variants map: wrong forms
    ONLY, never the canonical), one spelling locale (curated pairs). Its
    drift candidates are for a HUMAN read; some variation is legitimate.
    Still by hand: grep-count ~20 decided renderings; notes at FIRST
    appearance.

## Footnotes — what earns one (be generous; never invent)

Keyed by an exact anchor phrase, per unit: `notes.json` is
`{unit_id: [{anchor, note}]}`. Anchors must be verbatim substrings of the
English prose, verified at write time (`apparatus_merge.py` refuses otherwise;
the builder's refusal is the backstop, not the check). Anchors may sit on
section headings. Note bodies are XHTML: `<i>` for emphasis, NUMERIC character
references only (`&#160;`, `&#8212;`), never named entities.

**Density is a reader model, not a quota.** The reader is a Westerner with no
background in Chinese history, family structure, or custom; anything such a
reader would miss earns a note. Four coverage domains to sweep deliberately:
material culture (objects, food, clothing, money), social structure (kinship,
address, hierarchy), customs and belief, institutions and offices. Early
chapters typically want 8-15 notes; the count TAPERS naturally as the book's
furniture gets covered, and a late chapter with 0-2 new notes is healthy, not
starved. Do not pad to a number.

Four kinds earn a note:
1. **Translation uncertainty** — damaged-scan readings with the alternates
   considered, provisional romanizations, ambiguous referents, missing leaves.
   State what the scan shows and why you chose your reading.
2. **References a non-specialist won't catch** — who a person is, what an
   institution / place / object / term is, with real checked content and the
   verdict stated (corroborated / uncorroborated / contradicted). There is
   also a tier of minor low-stakes discrepancies deliberately left
   unfootnoted; name that tier in PROGRESS so you don't over-annotate.
3. **Texture lost in translation** — idioms with their literal image, classical
   allusions, register shifts, names whose meaning matters.
4. **The author as interested witness** — where the account is self-serving or
   shaped by its political moment, say so, with evidence.

Protocol: recurring subjects get their note at FIRST appearance in the book —
before adding one, grep `notes.json` and the earlier reading files; keep a
"NOT re-noted (already placed)" list per batch in PROGRESS.md; prefer
cross-referencing an existing note to re-noting. **The glossary is your
quarry:** every glossary row with a substantive note is a footnote candidate at
its first textual appearance, and the footnote should say MORE than the
glossary row. Numbering is continuous book-wide and assigned by the builder.

## Register — the style contract (general principles)

- **Clean, flowing English prose. All apparatus lives in the notes**, never
  inline: no bilingual interleave, no page numbers in the text, no [?]/[!]
  flags.
- **Keep the book's own voice.** The falsifiable test: could a good
  contemporary translator of, say, Mo Yan or Jin Yong have written this
  sentence? If it sounds like a Victorian rendering of Scripture, it goes. Do
  not import another register, another book's voice, or academic distance into
  a popular text.
- **Every major character gets a VOICE SHEET.** At first appearance, write
  a two-line register spec into HANDOFF's carry-forward section (educated or
  rough, terse or windy, verbal tics, formality toward whom) and consult it
  at every dialogue scene. "Characters must differ from each other" only
  happens when their differences are written down; the book that improvised
  this convention had the best dialogue on the shelf.
- **Merge sentences where English wants them merged.** Source information order
  is not sacred. Stiltedness is the failure mode to avoid. The recurring
  defect classes: idiom calques, transferred syntax, fake-antique verb forms,
  stilted inversion, wrong-register dialogue (characters must differ from each
  other), pronoun fog in action scenes, over-explained doubled renderings.
- **Idioms:** translate for effect; keep the vivid ones literal when they land,
  and footnote the ones whose flavor cannot survive.
- **Names:** pinyin (or the source language's standard romanization) except
  conventional English forms. One rendering per referent, DECIDED in
  `glossary.json` before you romanize anything. Consult `authority.json` (the
  cross-book name ledger) first so this book agrees with the shelf.
- Preserve period/technical vocabulary rather than modernizing it; gloss where
  a modern reader would miss the sense. Keep the author's own printed
  abbreviations and gloss them.
- For a genuinely hard passage, draft a literal first pass and keep it beside
  the polished version so the smoothing is visible and checkable.
- **The source's own errors stay visible.** Misprints, internal
  contradictions, inconsistent names: render as printed, note the fact, never
  repair the story. The one exception is a mechanical imprint typo in
  colophon-type matter, corrected with the discrepancy recorded in PROGRESS.
  OCR-era digitization glitches are different again: render to plain sense,
  LIST every one in PROGRESS.md, footnote only genuine reading uncertainty.

## Formatting the reading text

Set-off material is marked in the reading files and rendered by the builder:
`***` alone on a line is a scene break (centered asterism); `{v} ` opens a
vignette (italic block); `{d} ` a dateline (centered italic); `{g} ` a source
hour-gloss; `{p} ` verse (line breaks preserved). `check_structure.py` strips
the markers before parity. Translator-supplied datelines always carry a note
saying they were inferred and on what evidence.

**Emphasis (italic) in the reading text is written `*with asterisks*`**, which
the builder turns into `<i>`. Do NOT write a literal `<i>...</i>` tag in a
reading `.md` file: it is escaped and ships as VISIBLE `<i>Tewu</i>` text. This
shipped once; the builder now REFUSES a build whose reading files contain a
literal `<i>`/`</i>`. (Footnote and glossary bodies are XHTML and DO take
`<i>` directly, along with numeric character references only.)

## Glossary discipline

`glossary.json` is the single source of truth and the term ledger. Status per
entry: `attested` (form used in scholarship, with the citation), `provisional`
(your romanization, not found outside; the build marks these visibly),
`decided` (a project style call). One rendering per referent for the whole
book. Record per batch which existing rows were REUSED unchanged, not just
what was added; that is what keeps drift at zero. If you find a better
attested form mid-book, change the glossary AND grep every built unit for the
old form and rebuild. Flag the book's main cast with `"principal": true` (optional `cast`
one-liner and `cast_order`): the builder renders them as a front-matter
**Principal Characters** page, the standard courtesy of published Chinese
translations, because Western readers reliably lose track of Chinese names.
On completion, render the ledger as `out/term_ledger.md`
so someone who reads no Chinese can audit every rendering, and feed new
decisions back into `authority.json`.

## Build — the cumulative EPUB

- `scripts/build_reading_epub.py` builds one cumulative EPUB, driven entirely
  by `book.json` (deliverable name included). Every build ships a FULL,
  hyperlinked TOC, pending-aware until the book completes, then cleaned of
  scaffolding. The title page states honestly whether the build is complete.
- Cover: from `cover_image`, copied byte-identical (never through the figure
  pipeline), or a generated typographic cover. Declared for both EPUB3
  (`properties="cover-image"`) and legacy Kindle (`<meta name="cover">`).
- Straight quotes and `...` are typographized at the RENDER layer, so all
  source files stay plain ASCII and anchors never break.
- Footnote numbering is continuous; note markers sit after closing
  punctuation; `qa_epub.py` checks ref/body/backlink and sequential order.
  Markers carry `epub:type="noteref"` and bodies are `<aside
  epub:type="footnote">`, so Apple Books and Kindle show notes as POPUPS
  over the page; the endnotes page remains for readers that do not.
- The builder REFUSES to build on an unmatched note anchor or an unplaced
  figure spec (both were silent losses on real books: twelve notes once
  vanished for weeks; images silently dropped). Anchors are inserted BEFORE
  markup substitution, or the substitution eats them.
- Figures: per-unit specs in `figures.json` (file, `before` anchor in the
  FIRST ~80 chars of a paragraph, `alt` — a real screen-reader description —
  and caption). The caption's provenance is explicit: the labels are the
  source's, the caption is the translator's. If a caption is illegible,
  caption it neutrally; never invent an identification. A diagram worth
  keeping can also be transcribed in prose in its caption.
- Printed-page markers: if `data/pagemap/` exists, the builder emits
  `epub:type="pagebreak"` spans and a page-list nav, so folio citations in
  the notes are followable in the ebook.
- Optional back matter (errata, colophon) renders from `back_matter.json`;
  apply each erratum to the affected translation too, and say so.
- Run `qa_epub.py` after EVERY build; run epubcheck when available (it is
  what catches the store-blocking defects qa_epub cannot see). A failure
  stops the line until fixed.

## The revision pass (after completion, on commissioner feedback)

When the commissioner's read produces style/annotation feedback rather than
itemized corrections, run a structured whole-book pass: copy
`REVISION_PLAN.template.md` to `REVISION_PLAN.md`, fill it in from the
feedback, and follow it. Non-negotiables baked into the template: content is
frozen (a style pass, not a retranslation); expect most paragraphs to be LEFT
alone (both real revision passes over-predicted defect density by an order of
magnitude; a pass that edits every chapter is churning); edits go through
committed `edits/<id>_edits.md` lists applied by `scripts/apply_edits.py`;
read zh against en (the only real fidelity defects found in revision were
invisible to an English-only read); and NO subagent fan-out (a real attempt
burned the session budget re-reading shared context; sequential in-session
work was cheaper and more uniform).

## HANDOFF.md and the kickoff message

**HANDOFF.md stores the kickoff; the CHAT delivers it.** Every batch ends
with the kickoff pasted verbatim in the chat reply (top-of-file banner);
this section is about what the stored copy must contain.

Rewrite `HANDOFF.md` each batch so a fresh session with no memory can start
the next batch immediately. Required contents: the fenced kickoff message
FIRST (under `## Message to paste into the next chat`); what is DONE, one
line per batch, do not redo; tooling in place, with an explicit "do not
revert" list of accumulated script patches; renderings settled this batch and
the carry-forward list (including the per-character VOICE SHEETS); where the
story/argument stands; exact next-batch
scope with unit ids and page ranges; open traps and environment state.

The kickoff message's FIRST LINE is the project label and batch,
**[SET PER PROJECT]** e.g. `My Book B07`, then a blank line, then: read
`CLAUDE.md`, then `HANDOFF.md`, then `book.json`; do batch `<Bxx>` =
`<scope>` (PDF `<a-b>`, printed `<a-b>`) end to end per the pipeline;
BEFORE translating, read the final two pages of the previous unit's English
(HANDOFF describes the voice; the pages ARE the voice); cite
printed folios; never invent bridging text; do not pause for approval;
deliver the EPUB in chat and paste the next kickoff. Paste the current
kickoff verbatim at the end of your batch-completion reply too.

On the LAST batch: back matter, the whole-book reconciliation sweep (check
12), `COMPLETION.md` from the template instead of another handoff, commit the
final EPUB itself (`git add -f out/<deliverable>` — branches outlive
containers, chat attachments do not), and rewrite `HANDOFF.md` to say the
book is COMPLETE and further work is a corrections pass. Do not modify the
kickoff section afterward (the Stop hook would demand a block that no longer
exists).

## Corrections workflow

The commissioner reads the EPUB and files corrections in `CORRECTIONS.md` —
or, just as validly, pastes them in chat, in which case YOU transcribe them
into `CORRECTIONS.md` (the form in that file) before acting; the file is the
ledger, not a form the commissioner must fill. GLOBAL corrections (a
rendering, a register rule, a note policy) cascade via a glossary/style change
plus a grep-driven edit across ALL built units INCLUDING note and glossary
bodies, then rebuild and full QA; a global correction applied to only some
units is worse than not applying it. LOCAL corrections are a fix at one spot.
A corrections pass with zero items is still a clean-checkout regression run:
re-clone, regenerate, rebuild, re-verify, prune stray branches. After any
corrections batch: rebuild, `qa_epub`, list every file touched, dated entry in
`CHANGELOG.md` (tooling changes get entries too).

## If something goes wrong

- **Pushes fail (permissions):** keep committing locally, retry the push at
  every commit point, and surface the permission ask to the commissioner.
  Never let work sit uncommitted.
- **A model change mid-book:** the real risk is voice drift, not competence.
  Mitigate mechanically: `check_register.py --ref` every unit, record
  uncertain passages in PROGRESS as the final-pass worklist.
- **Content that should not be translated** (e.g. operational instructions
  for weapons in a historical manual): do not render it; hold the section
  slot with an editorial placeholder and a footnote stating the omission;
  record the standing decision in PROGRESS, HANDOFF and the completion
  report so no later session "completes" it. Surface the decision to the
  commissioner.
- **Session/API caps mid-check:** substitute the documented manual fallback,
  and SAY in PROGRESS.md which you did.

## Known traps (general)

- Wrong OCR script model (simplified vs Traditional) = silent corruption.
- Uncropped page furniture corrupts line ends and injects phantom numerals.
- Offset drift and second front-matter sequences; read folios off the scan.
- Scanner double-feeds duplicate a leaf; blank versos go uncounted.
- OpenMP/tesseract orphans (`OMP_THREAD_LIMIT=1`; kill the process group;
  `pgrep -c tesseract`).
- `find_figures.py` misses line art and false-positives on dense text.
- Folio detection must profile the SAME crop the OCR saw; a mismatch silently
  deleted the last line of 41% of a chapter's pages, invisible to parity.
- Insert note anchors BEFORE markup substitution in the builder.
- XHTML note bodies: numeric character references, never named entities.
- NEVER write CJK into JSON via a shell heredoc; use `apparatus_merge.py` or
  the Write tool, and re-read to verify (`check_apparatus.py`).
- When editing scripts, grep for the actual bytes first: a source file may
  hold `\u` escapes where the rendered string shows the character.
- Keep `mimetype` first and stored in the EPUB zip (the builder does).
- Numerals in unit designations (第37军) are load-bearing; always crop-verify.
- Tracked vs regenerable is DECIDED (see `.gitignore`'s reasons): track
  `source.pdf`, `out/*_reading.md`, all ledgers, derived
  geometry (`data/indent/`, `data/pagemap/`, `data/ocr_fixes.json`,
  `data/structure.json`, `data/headings.json`); ignore renders, raw OCR text
  and bilinguals.

## Definition of done (whole book)

- The EPUB: front matter + all chapters, full clean TOC, cover, figures with
  captions/alt or honest non-captions, footnotes at reader-model density,
  glossary and translator's note current, `qa_epub` PASS across the whole
  spine, epubcheck clean if available, back matter if the book has any, and
  the file itself committed.
- `out/<id>_reading.md` per unit (the correction surface),
  `out/term_ledger.md`, `out/deep_audit.md`.
- `notes.json`, `glossary.json`, `figures.json`, `book.json` current;
  `authority.json` updated with this book's decided renderings.
- `COMPLETION.md` written from the template, with the sampled error rate and
  the residual uncertainties a reader should know about.
- `PROGRESS.md` and `HANDOFF.md` written as you go, not at the end.
