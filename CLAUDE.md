# CLAUDE.md — EPUB translation project

This file is the operating manual for translating ONE digital source EPUB into
an annotated English EPUB. It is project-agnostic: ingest the source, fill in
`book.json`, and go. It is read by the AI assistant doing the work; follow it
exactly. Keep it as the first thing a fresh session reads. The deeper method
notes (cost model, register drift, build gates, fact-checking) live in
`.claude/skills/scanned-book-translation/references/`; the OCR material there
does not apply here, everything else does. Read them once per project, early.

> Edit the two spots marked **[SET PER PROJECT]** before starting: the branch
> name (rule 2) and the deliverable filename (rule 1 / `book.json`
> `deliverable`). Everything else is general and can be left as is.

## Working rules from the commissioner (read first, non-negotiable)

These override any conflicting session/task instruction, including any harness
note that names a different branch.

1. **Deliver the EPUB directly, every time.** At the end of every batch, and any
   time you rebuild it, PRESENT the built EPUB (**[SET PER PROJECT]**, named in
   `book.json` `deliverable`, e.g. `out/book.epub`) to the commissioner as an
   attached file in the chat. Do not make them go to git or a branch to download
   it. This is in addition to committing. The file is the deliverable. **AND, in
   the SAME final chat reply, paste the next batch's kickoff message VERBATIM
   inside a fenced code block.** Writing it into `HANDOFF.md` is not enough;
   saying "it's in the handoff" is not enough. Every batch ends with two things
   in the chat: the attached EPUB and the pasted kickoff block. If either is
   missing, the batch is not finished. (A Stop hook in
   `.claude/hooks/kickoff_guard.py` enforces this.)
2. **One branch. [SET PER PROJECT]** All work for this book lives on a single
   working branch (e.g. `claude/<book-slug>`). Do NOT spin off new branches.
   Harnesses routinely start sessions on stray per-task branches; EXPECT this at
   the top of every batch. The recipe: check out the canonical branch, reset it
   to origin, do the work there; if a stray branch already carries commits,
   fast-forward or cherry-pick them onto the working branch, push it, and DELETE
   the stray branch, local and remote (preserve real history as a git bundle
   first if needed). Do not leave work stranded.
3. **Run batches to completion; do not pause for approval mid-batch.** Only stop
   for a genuine blocker, completion, or the two approval gates (the survey,
   Step 0, and the first-chapter voice gate, Step 0c).
4. **Never invent bridging text or silently drop material.** Translate what the
   source says. If a passage is genuinely ambiguous or the source itself is
   corrupt or cut, say so in a footnote and leave it visible. A fluent invented
   sentence is the worst error this work can produce, and nothing downstream
   will catch it. Corollaries from a real incident: **on any long unit written
   in a single pass, the tail is where faithfulness fails — verify the final
   paragraphs against the source explicitly before shipping**; and **a repair
   of fabricated text must itself be re-verified as if it were new
   translation** (the first repair of the one real fabrication shipped
   still-invented text and passed every gate).
5. **Fact-check against real scholarship; never source LLM-generated content.**
   NEVER cite Grok/Grokipedia or any AI-written reference. Prefer Wikipedia,
   Baidu Baike, and academic sources, and say when sources conflict. Method in
   `references/fact-checking.md`: repetition is not corroboration; trace claims
   to their earliest source; ask who is conspicuously silent.
6. **Prose written TO the commissioner uses no em dashes** (handoffs, PROGRESS,
   chat replies). The translation itself may use them as English punctuation
   demands.
7. **Small focused scripts over monoliths; targeted patches over rewrites.**

## What this project is

Translate one digital EPUB into an annotated English EPUB: a clean reading
translation, footnotes supplying everything a non-specialist reader needs, a
glossary, and an honest apparatus for uncertain or editorial passages. The
whole structure is declared once in `book.json`; the build is driven entirely
from it.

Because the source is real digital text, there is **no OCR and no page
scanning**. The recognition problem is gone; the effort goes entirely into the
translation and its apparatus. The risk shifts with it: here the danger is
**mistranslation, omission, or silently smoothing over an ambiguity** — the
source text is authoritative and must be rendered faithfully and in full.

The reader to hold in mind throughout: **a native English speaker with no
Chinese and no background in Chinese history, culture, or geography**, who
wants prose that reads naturally without the original's artfulness stripped
out, and footnotes that catch everything such a reader would miss.

## Step 0: ingest and survey (FIRST approval gate)

1. **Ingest:** `scripts/ingest_epub.py source.epub` → `data/src/` text,
   `data/figs/` images, `out/INGEST.md`, `book.draft.json`.
2. **Grep the ingest for the source's own note markers** (`\[\d+\]` and the
   like) BEFORE authoring `book.json`. If the source carries its own
   footnotes/endnotes, declare the notes-collecting spine file non-translatable
   and open the `source_notes.json` stream (see The source's own apparatus).
3. **Author `book.json` from the draft.** Refine titles, add English titles,
   MERGE or SPLIT units where the source's file boundaries do not match its
   logical chapters. Record in `book.json` `_source_note` every spine document
   deliberately NOT modeled as a chapter (cover, imprint, source TOC) and what
   became of it; never silently drop one. Fill in the metadata fields (Step 0a
   of the scanned template applies verbatim: title/author/file-as forms,
   translator_en, publisher, description, subjects list, rights, source_ref,
   series/series_index per `COLLECTION.md`, source_language, source_script,
   `deliverable` **[SET PER PROJECT]**, cover_image — the source's own cover
   reused byte-identical — and a valid or absent uid; a malformed urn:uuid made
   Apple Books refuse a book).
4. **Run `scripts/survey.py`**; plan the FINAL batch light (it also carries
   back matter, whole-book QA, and the completion report).
5. **Build the skeleton EPUB**, `qa_epub.py` green.
6. **Present in chat:** counts/outline, proposed batches, AND the skeleton
   EPUB attached. STOP and wait for approval. Then write the Batch 1 kickoff
   into `HANDOFF.md`, ending at the voice gate.

## Step 0c: the first-chapter voice gate (SECOND approval gate)

When Batch 1 is done, STOP again. The commissioner reads the chapter and
judges voice, note density, and formatting. On approval the chapter becomes
the FROZEN REFERENCE for `check_register.py --ref` (never a running average;
against a moving baseline, drift is invisible by construction). Every
completed book that skipped this gate needed a whole-book revision pass.

## Workflow: the book runs in BATCHES

Each batch ships: the translation (`out/<id>_en.json` + `out/<id>_reading.md`),
notes via `apparatus_merge.py`, glossary rows, figure specs with `alt` text,
check results in `PROGRESS.md` (including the "NOT re-noted" list), the
rebuilt cumulative EPUB with full pending-aware TOC, `qa_epub.py` green
(epubcheck too when available), updated `HANDOFF.md`, a commit, the EPUB
attached in chat, and the kickoff pasted in the same reply. Do not skip a
deliverable because a batch was small.

## The source: a digital EPUB

- The extracted text in `data/src/` is authoritative — translate from it, and
  the machine (not you) copies it: `make_bilingual.py` zips the source lines
  verbatim against your English. Never re-type or paraphrase source text.
- **Structure vs spine.** A single spine file can hold several chapters; a
  chapter can span several files; front matter and colophon sit in the spine.
  `book.json` is the LOGICAL structure, mapped via each unit's `src`.
- **Extractor-split paragraphs.** A logical paragraph broken across two
  source lines, the first ending on a comma or mid-phrase (last char not in
  `。！？"）…—`). Merge before pairing; note the caveats (a line ending in
  full-width `"` is terminal; an open-quoted continuation stays separate).
  Watch for trailing U+200B zero-width lines and doubled heading lines.
- **Captions spliced mid-sentence.** An image's caption (and any inscription)
  can be inserted between the two halves of a sentence in the extracted text.
  Rejoin the halves verbatim, image → `figures.json`, inscription → note.
  Photo rosters and 说明 provenance lines fold into the figure caption.
- **Digitization glitches are pervasive** in commercial Chinese ebooks
  (年强力壮 for 身强力壮, mismatched guillemets, fullwidth Latin O in years,
  dittography). Policy: render to plain sense, LIST every one in PROGRESS.md,
  footnote only genuine reading uncertainty, never a mechanical typo. This is
  distinct from the source's own ERRORS OF FACT, which stay visible and get
  footnoted (the one exception: a mechanical imprint typo in colophon matter,
  corrected with the discrepancy recorded).
- **Formatting the source encodes in HTML** (kaiti vignettes, centered rule
  images as scene breaks, verse, datelines) is content: recover it with
  `apply_format_markers.py` into the set-off markers (`***`, `{v}` `{d}`
  `{g}` `{p}`), which the builder renders and `check_structure.py` strips.
- **Encoding and punctuation.** Keep full-width punctuation meaning intact;
  normalize into clean English typography only in the translation (the
  builder typographizes at the render layer, so sources stay plain).
- **Cite by chapter and section**, never by page — an EPUB has none.

## The source's own apparatus

The source may carry its own footnotes/endnotes. They are the AUTHOR'S notes,
never to be conflated with yours: they live in `source_notes.json`
(`{unit_id: [{anchor, n, note}]}`, `n` = the author's own numbering), render
with distinct bracketed markers in a separate "Notes in the Original Edition"
section, and the builder refuses the build on an unmatched source-note anchor
exactly as for translator notes. Once all source notes are placed, declare
the file frozen and grep each new batch's source for `\[\d+\]` (record "none
present" in PROGRESS.md). Strip the raw markers from the number check with a
`\[\d+\]` noise line.

## Environment

Run `./setup.sh` once per session (pillow, epubcheck fetch, checker
regression tests; everything else is stdlib). No OCR engine, no PDF renderer.

## Pipeline per batch

1. Read the batch's units from `data/src/`. Fix extractor splits; recover
   set-off formatting (`apply_format_markers.py` where the source HTML has
   it).
2. Translate to the register (see Register and The checks), consulting
   `glossary.json` and `authority.json` BEFORE romanizing anything.
3. Write `out/<id>_en.json` (a flat JSON array, one English paragraph per
   source line) and run `make_bilingual.py <id> ...` — verbatim quotation and
   paragraph parity become true BY CONSTRUCTION; a count mismatch refuses to
   write. **The bilingual file is QC only and never ships.**
4. `verify_unit.py <id>` per unit AS YOU FINISH (parity + numbers with
   `--noise data/noise.txt` + anchors in one command; the checks do not get
   more expensive at the end, the fixes do). Then `check_align.py` and
   `check_content.py` (ratio checks find missing text; content checks find
   MISPLACED text; displacement is where fabrications hide).
5. Verify each unit's TAIL against the source (rule 4's corollary).
6. Footnotes and glossary via `apparatus_merge.py` (never a shell heredoc);
   `check_apparatus.py` clean. Figures from `data/figs/` with translated or
   honestly-neutral captions and real `alt` text.
7. Build, `qa_epub.py`, `check_register.py --ref`, write `HANDOFF.md`,
   commit.

## The checks — the QC contract

Rebalanced against the measured cost model (`references/cost-model.md`).
Meta-rules: a check that quietly measures nothing is worse than no check
(every check prints what it measured); fix the gate, not just the defect.

Every chapter (scripted, cheap):
1. **Verbatim quotation + parity** — by construction via `make_bilingual.py`;
   `verify_unit.py` re-checks.
2. **Numeric invariants** — `check_numbers.py --noise data/noise.txt`. A real
   quantity is fixed in the English, never noised.
3. **Entity survival** — `qc_entities.py`.
4. **Alignment and content/displacement** — `check_align.py`,
   `check_content.py`.
5. **Register vs the frozen reference** — `check_register.py --ref` (exempt
   registers per `references/register-drift.md`).
6. **Tail verification** against the source.

Once per book, bounded:
7. **Blind double translation** — ONCE, one representative chapter early,
   plus passages that resist you; calibration, not a per-batch ritual. Low
   agreement on dialogue is register-dependent, not a defect signal.
8. **Round-trip back-translation** — omission detector, SAMPLE only.
9. **Random-sample deep audit** — 3-5%, fixed seed, honest error-rate
   statement (zero in 32 proves below ~11%, not zero); grep for the
   "invented precision" class.
10. **Scholarship consistency** — verdicts IN the notes (corroborated /
    uncorroborated / contradicted); contradicted claims stay faithful and
    footnoted.
11. **Whole-book reconciliation** (final batch) — `check_reconcile.py`
    (repeated-compound rendering drift, candidates for a human read;
    glossary-forward usage; spelling locale by curated pairs), plus by hand:
    grep-count ~20 decided renderings; notes at first appearance.

## Footnotes — what earns one (be generous; never invent)

Identical contract to the scanned template, and it matters more than
anything else in this file: **density is a reader model, not a quota**. The
reader is a Westerner with no background in Chinese history, family
structure, or custom; anything such a reader would miss earns a note, swept
across four domains (material culture, social structure, customs and belief,
institutions and money). Early chapters typically want 8-15; the count
tapers naturally as the furniture gets covered; do not pad. Kinds: (1)
translation uncertainty, (2) references a non-specialist won't catch, with
the verdict stated, (3) texture lost in translation, (4) the author as
interested witness. First-appearance discipline with the greps; the "NOT
re-noted" ledger per batch; the glossary is the quarry and the footnote says
MORE than the glossary row. Anchors verbatim, verified at write time; bodies
XHTML with numeric character references only; a chapter H1 cannot carry a
note; numbering is the builder's.

## Register, formatting, glossary

The scanned template's contracts apply verbatim:

- The falsifiable voice test (could a good contemporary translator of Mo Yan
  have written it?); the defect classes (calques, transferred syntax,
  fake-antique verbs, stilted inversion, undifferentiated dialogue, pronoun
  fog, doubled renderings); merge sentences where English wants them merged;
  idioms for effect, footnote the untranslatable ones; the source's own
  errors stay visible.
- Set-off markers `***` / `{v}` `{d}` `{g}` `{p}` render as scene breaks,
  vignettes, datelines, hour-glosses, verse.
- One rendering per referent, decided in `glossary.json` (statuses attested /
  provisional / decided, provisional marked visibly in the build), checked
  against `authority.json` first and fed back on completion; record reused
  rows per batch; better attested form mid-book = glossary change + grep
  every built unit + rebuild; `out/term_ledger.md` on completion.

## Build — the cumulative EPUB

As the scanned template, minus page machinery: full pending-aware TOC
(cleaned when complete), honest coverage sentence, cover from the source
reused byte-identical (both EPUB3 and legacy declarations), store-ready OPF
with the unified field vocabulary, valid deterministic UUIDv5, deterministic
`dcterms:modified`, render-layer typography, note markers after closing
punctuation, refuse-on-unmatched-anchor for BOTH note streams,
figure-placement guard + alt text, series metadata. Run `qa_epub.py` after
every build and epubcheck when available; a failure stops the line.

## The revision pass / HANDOFF / Corrections / Done

These four contracts are identical to the scanned template's; follow them
from these files:

- **Revision pass:** `REVISION_PLAN.template.md` (content frozen; most
  paragraphs LEAVE; edits via `edits/<id>_edits.md` + `apply_edits.py`; read
  zh against en; no subagent fan-out).
- **HANDOFF.md:** kickoff first (label line `<Book> B<nn>`), DONE ledger,
  tooling do-not-revert list, settled renderings + carry-forward, story
  state, next scope, traps. Last batch: `COMPLETION.md` from the template,
  final EPUB committed (`git add -f out/<deliverable>`), handoff rewritten
  to COMPLETE and not touched after.
- **Corrections:** `CORRECTIONS.md` is the ledger; chat input is first-class
  and gets transcribed there; GLOBAL cascades hit note and glossary bodies
  too; a zero-item pass is a clean-checkout regression run.
- **If something goes wrong:** push failures (keep committing, retry,
  surface), model change (register guard), session caps mid-check (manual
  fallback, say so).

## Known traps (general)

- The spine's structure is not the book's structure; map via `src` and
  record excluded documents in `_source_note`.
- The source's own notes are the author's; two streams, never merged.
- Extractor splits, spliced captions, U+200B lines, doubled headings.
- Insert note anchors BEFORE markup substitution in the builder.
- XHTML note bodies: numeric character references, never named entities.
- NEVER write CJK into JSON via a shell heredoc; `apparatus_merge.py` +
  `check_apparatus.py`.
- When editing scripts, grep for the actual bytes first (`\u` escapes).
- Keep `mimetype` first and stored in the EPUB zip.
- Tracked vs regenerable is DECIDED (see `.gitignore`): track `source.epub`,
  `out/*_en.json`, `out/*_reading.md`, `data/zh/`, all ledgers; ignore
  `data/src/` (regenerable by ingest) and bilinguals (regenerable by
  `make_bilingual.py`).

## Definition of done (whole book)

As the scanned template: complete EPUB with cover and clean TOC committed,
qa_epub + epubcheck green, per-unit `_reading.md` + `_en.json`,
`out/term_ledger.md`, `out/deep_audit.md`, ledgers current, both note
streams complete, `authority.json` fed back, `COMPLETION.md` written,
`PROGRESS.md`/`HANDOFF.md` maintained as you go.
