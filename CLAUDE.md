# CLAUDE.md — EPUB translation project

This file is the operating manual for translating ONE digital source EPUB into an
annotated English EPUB. It is project-agnostic: ingest the source, fill in
`book.json`, and go. It is read by the AI assistant doing the work; follow it
exactly. Keep it as the first thing a fresh session reads.

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
   committing. The file is the deliverable.
2. **One branch. [SET PER PROJECT]** All work for this book lives on a single
   working branch (e.g. `claude/<book-slug>`). Do NOT spin off new branches. If a
   session starts you on some other branch, or a stray branch gets created and
   worked on, move every commit and file onto the one working branch, push it,
   and DELETE the stray branch, both local and remote. Do not leave work
   stranded.
3. **Run batches to completion; do not pause for approval mid-batch.** Only stop
   for a genuine blocker, or completion, or the survey-approval gate (Step 0).
4. **Never invent bridging text or silently drop material.** Translate what the
   source says. If a passage is genuinely ambiguous or the source itself is
   corrupt or cut, say so in a footnote and leave it visible. A fluent invented
   sentence is the worst error this work can produce, and nothing downstream will
   catch it.
5. **Fact-check against real scholarship; never source LLM-generated content.**
   NEVER cite Grok/Grokipedia or any AI-written reference. Prefer Wikipedia,
   Baidu Baike, and academic sources, and say when sources conflict.
6. **Prose written TO the commissioner uses no em dashes** (handoffs, PROGRESS,
   chat replies). The translation itself may use them as English punctuation
   demands.
7. **Small focused scripts over monoliths; targeted patches over rewrites.**

## What this project is

Translate one digital EPUB into an annotated English EPUB: a clean reading
translation, footnotes supplying everything a non-specialist reader needs, a
glossary, and an honest apparatus for uncertain or editorial passages. The whole
structure is declared once in `book.json`; the build is driven entirely from it.

Because the source is real digital text, there is **no OCR and no page
scanning**. The recognition problem is gone; the effort goes entirely into the
translation and its apparatus. The corresponding risk also shifts: on a scan the
danger is misreading a character, but here the danger is **mistranslation,
omission, or silently smoothing over an ambiguity** — the source text is
authoritative and must be rendered faithfully and in full.

## Step 0: ingest and survey (do this FIRST, before any batch)

Before a single word is translated, ingest the source and deliver a survey of the
whole book, so the commissioner can see its shape, know its size, and approve how
it will be batched. Hard first step, not optional.

1. **Ingest the source EPUB:** `scripts/ingest_epub.py source.epub`. It unpacks
   the EPUB, reads the spine in reading order, extracts the plain text and
   headings of each document into `data/src/`, pulls out the images into
   `data/figs/`, counts the source characters, and writes `out/INGEST.md` (an
   outline report) and `book.draft.json` (a first-cut structure).
2. **Author `book.json` from the draft.** Refine titles, add English titles, and
   MERGE or SPLIT units where the source's file boundaries do not match its
   logical chapters (one spine file may hold several chapters, or one chapter may
   span several files). Add optional `part` labels and `subsections`. Keep each
   unit's `src` and `chars`.
3. **Run `scripts/survey.py`.** It reports the counts (parts / chapters /
   sections / subsections), every unit's title and size in source characters, and
   a proposed batch breakdown, and writes `out/SURVEY.md`.
4. **Build the skeleton EPUB:** `scripts/build_reading_epub.py`. With nothing
   translated yet it produces a fully navigable EPUB whose table of contents
   links every part, chapter, section and subsection (each to an outline page
   showing its source size). Run `qa_epub.py`; it must be green.
5. **Present both to the commissioner in chat:** the counts/outline and the
   proposed batches for approval, AND the skeleton EPUB itself as an attached
   file (the hyperlinked TOC is the thing to review). Then STOP and wait for the
   batch plan to be approved.
6. **Only after approval**, write the Batch 1 kickoff message into `HANDOFF.md`
   and begin.

## Workflow: the book runs in BATCHES

Once the survey is approved, do the book a **batch at a time** (a chapter, or a
run of sections, per the approved plan). Each batch ships all of these together:

1. Clean English translation of the batch: `out/<id>_reading.md`.
2. Footnotes for the batch, folded into `notes.json`.
3. New/changed glossary rows in `glossary.json`; figure specs in `figures.json`.
4. The relevant checks run, and their results recorded in `PROGRESS.md`.
5. A rebuilt cumulative EPUB whose FULL table of contents links the translated
   units and still links every not-yet-translated unit to its skeleton outline,
   so the whole book stays navigable.
6. `qa_epub.py` green.
7. An updated `HANDOFF.md`, whose first section is a **paste-ready kickoff
   message** for the next batch, and a commit.

Do not skip a deliverable because a batch was small.

## The source: a digital EPUB

- The extracted text in `data/src/` is authoritative — translate from it, and
  quote it exactly in the bilingual QC file. Do not re-type or paraphrase the
  source; copy it.
- **Watch where the source's own structure and its logical structure differ.**
  A single spine file can contain several chapters; a chapter can be split across
  files; front matter, a table of contents, and colophon pages sit in the spine
  too. `book.json` reflects the LOGICAL structure; map it to the source via each
  unit's `src`.
- **The source may carry its own apparatus** — the author's or editor's
  footnotes/endnotes, italics, block quotes, poems. Preserve these: render the
  source's own notes as part of the text (marked as the source's, distinct from
  your translator's notes), and keep quoted/verse formatting.
- **Encoding and punctuation.** The source is Unicode; keep full-width
  punctuation meaning intact, and normalize only into clean English typography in
  the translation, never in the quoted source.
- **Cite by chapter and section**, not by page — an EPUB has no fixed pages.

## Environment

```
pip install pillow                 # image handling for figures (optional)
# ingest_epub.py, the checks, the builder and QA are pure Python stdlib.
```

No OCR engine, no PDF renderer, no page-image tooling is needed.

## Pipeline per batch

1. The source text is already extracted (Step 0). Read the batch's units from
   `data/src/`.
2. Translate to the register (see Register and The checks). The source is
   authoritative: quote it verbatim in the bilingual QC file; render it faithfully
   and in full into English.
3. Author ONE aligned bilingual QC file `out/<id>_bilingual.md` (source `>`
   blockquote line, English paragraph beneath; headings tagged `## H2/H3/H4`).
   Generate the reading text and the parity source from it with
   `split_bilingual.py`. **The bilingual file is QC ONLY and never ships.**
4. Run `check_numbers.py out/<id>_bilingual.md` and
   `check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md`.
5. Footnotes into `notes.json`; glossary into `glossary.json`; figures into
   `figures.json` (re-use images pulled from the source into `data/figs/`).
6. Build the cumulative EPUB, run `qa_epub.py`, write `HANDOFF.md`, commit.

## The checks — the QC contract

Run these each batch; record what ran and what it found in `PROGRESS.md`.

1. **Faithful, complete quotation of the source.** Because the source is digital,
   there is no OCR step — but confirm the bilingual QC file quotes the source
   VERBATIM (copy, do not re-type) and that no sentence or paragraph of the
   source is dropped. Paragraph parity (check 4) is the mechanical backstop.
2. **Blind double translation.** Translate the batch twice in separate contexts
   and diff. Apply to ALL argumentative/analytical/literary passages; sample the
   plain narration. Divergence means the source is ambiguous or hard.
3. **Round-trip back-translation.** Translate the English back to the source
   language in a fresh context and diff against the source. An omission detector,
   not a correctness detector.
4. **Automated invariant checks.** `check_numbers.py` (every numeral, date, year
   survives source to target) and `check_structure.py` (paragraph parity; note
   anchors resolve; heading shape uniform; glossary drift). Extend the
   `check_numbers` NOISE list (or a `--noise` file) whenever a non-quantity
   numeral is flagged.
5. **Auditable term ledger.** `glossary.json`: every proper noun / org / place /
   specialist term gets one row with the attestation. Enforces cross-chapter
   consistency, the real book-length failure mode.
6. **Annotate, do not smooth.** Mark genuinely ambiguous or hard spans in the
   working draft with a reason; each becomes a footnote. Never launder
   uncertainty into fluent prose.
7. **Consistency-check against scholarship** (rule 5). Where the book meets
   documented history, check the claim and SAY whether it is corroborated,
   uncorroborated, or contradicted.
8. **Random-sample deep audit.** Give 3-5% of the batch the full paranoid
   treatment (verbatim-quote check, double translation, back-translation) and
   report the observed error rate in the handoff.

## Footnotes — what earns one (be thorough; never invent)

Keyed by an exact anchor phrase, per unit: `notes.json` is
`{unit_id: [{anchor, note}]}`. **Anchors must be verbatim substrings of the
English prose; verify at write time** (the build refuses on an unmatched anchor).
Note bodies are XHTML: use `<i>` for emphasis and NUMERIC character references
(`&#160;`, `&#215;`, `&#8212;`), never HTML named entities.

Three kinds earn a note:
1. **Translation uncertainty** — genuinely ambiguous passages with the readings
   considered, provisional romanizations, ambiguous referents. Keep the source's
   OWN notes separate (render those as part of the text).
2. **References a non-specialist won't catch** — who a person is, what an
   institution / place / object / term is, with real historical content, checked
   against scholarship (say corroborated / uncorroborated / contradicted).
3. **Texture lost in translation** — idioms with their literal image, classical
   allusions, register shifts, names whose meaning matters.

Density: about 3 notes per chapter-equivalent is a fair calibration; do not pad,
do not starve. Recurring subjects get their note at FIRST appearance in the book.
Numbering is continuous across the book and assigned by the builder from note
order; you just append to the unit's list.

## Register — the style contract (general principles)

- **Clean, flowing English prose. All apparatus lives in the notes**, never
  inline: no bilingual interleave, no [?]/[!] flags.
- **Keep the book's own voice.** Narrative fiction/history stays in its own
  register (novelistic, plain, lyrical — whatever the source is); an expository
  work stays expository. Do not import a different register or academicize a
  popular voice.
- **Merge sentences where English wants them merged.** Source information order
  is not sacred. Stiltedness is the failure mode to avoid.
- **Idioms:** translate for effect; keep the vivid ones literal when they land,
  and footnote the ones whose flavor cannot survive.
- **Names:** pinyin (or the source language's standard romanization) except
  conventional English forms. One rendering per referent, DECIDED in
  `glossary.json` before you romanize anything.

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
  outline with its source size. So the TOC is navigable from the first (survey)
  build, and stays fully linked as chapters fill in (a partly-translated chapter
  links only the sections it has). It never links an anchor that does not exist
  (which `qa_epub.py` would reject).
- Footnote numbering is continuous; `qa_epub.py` checks every ref has a body and
  every body a backlink, and that numbering is sequential in reading order.
- The builder REFUSES to build on an unmatched note anchor. Anchors are inserted
  BEFORE markup substitution, or the substitution eats them.
- Figures: per-unit specs in `figures.json` (file — reuse an image pulled into
  `data/figs/` — a `before` anchor phrase in the FIRST ~80 chars of a paragraph,
  and a caption). If the source captions the image, translate that caption; if
  not, caption it neutrally.
- Optional back matter (a colophon) renders from `back_matter.json`; the
  translator's note text can come from `book.json`'s `translator_note`.
- Run `qa_epub.py` after EVERY build. A failure stops the line until fixed.

## HANDOFF.md and the kickoff message

When a batch is done, rewrite `HANDOFF.md` so a fresh session with no memory can
start the next batch immediately. Its FIRST section, under
`## Message to paste into the next chat` and inside a fenced block, is a
ready-to-paste kickoff message for the next batch. **Every kickoff message MUST
begin with `Midnight B<nn>` as its first line** (e.g. `Midnight B03`, the batch
it kicks off), then a blank line, then the body. The body is: read `CLAUDE.md`,
then
`HANDOFF.md`, then `book.json`; do batch `<Bxx>` = `<scope>` end to end; read the
batch's source text from `data/src/`, translate to the register, run the checks,
footnote, rebuild the EPUB with the pending-aware TOC, run `qa_epub.py` until
green, commit, rewrite `HANDOFF.md`; cite chapters/sections; never invent bridging
text; do not pause for approval; deliver the EPUB in chat. Paste that message
verbatim at the end of your chat reply too. On the LAST batch, the message says
to do any back matter and a whole-book QA pass and write a completion report
instead of another handoff.

## Corrections workflow

The commissioner reads the EPUB and files corrections in `CORRECTIONS.md`.
GLOBAL corrections (a rendering, a register rule, a note policy) cascade via a
glossary/style change plus a grep-driven edit across ALL built units, then
rebuild and full QA; a global correction applied to only some units is worse than
not applying it. LOCAL corrections are a fix at one spot. After a corrections
batch: rebuild, run `qa_epub`, list every file touched, and append a dated entry
to `CHANGELOG.md`.

## Known traps (general)

- The source's own file/spine structure often differs from its logical chapter
  structure; `book.json` is the logical structure, mapped via `src`.
- The source may carry its own footnotes/endnotes and inline markup; preserve
  them (render the source's notes as text, distinct from your translator's notes).
- Quote the source VERBATIM in the bilingual file; do not re-type or paraphrase.
- Insert note anchors BEFORE markup substitution in the builder.
- XHTML note bodies: numeric character references, never named entities.
- Writing rare characters into JSON via a shell heredoc can silently mangle a few
  glyphs; write via a file/Python and re-read to verify.
- Keep `mimetype` first and stored in the EPUB zip (the builder does; do not
  reorder).

## Definition of done (whole book)

- The EPUB: front matter + all chapters, full TOC, figures with captions,
  footnotes throughout at reference density, glossary and translator's note
  current, `qa_epub` PASS across the whole spine, colophon if the book has one.
- `out/<id>_reading.md` per unit (the correction surface).
- `notes.json`, `glossary.json`, `figures.json`, `book.json` current.
- `PROGRESS.md` and `HANDOFF.md` written as you go, not at the end.
