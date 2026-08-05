# START HERE — translate a Chinese EPUB into an annotated English EPUB

This branch (`translation-template-epub-master`) is a ready-to-clone starter
kit for translating one **digital source EPUB** (real text, no scanning) into
an annotated English EPUB, using the same batch process, enforcement layer and
hyperlinked-TOC build as the scanned-book template, with the OCR machinery
replaced by EPUB ingest. No book is loaded in.

## Setup (pick one option)

Option A, a folder in an existing repo:
```
mkdir my-book && git archive translation-template-epub-master | tar -x -C my-book
cp /path/to/source.epub my-book/source.epub
```
Option B, a fresh branch that IS the project:
```
git checkout -b claude/my-book translation-template-epub-master
cp /path/to/source.epub source.epub
```

Then: set the two **[SET PER PROJECT]** values (working branch in `CLAUDE.md`
rule 2; deliverable filename in `book.json`), the kickoff label (`My Book`
below), and check `authority.json`/`COLLECTION.md` for shelf conventions
(series metadata, renderings this book must agree with). Everything else the
first session does itself.

## The flow: ingest + survey, then ONE chapter, then batches

1. **Survey** (message 1): ingest, `book.json`, counts, proposed batches, and
   a skeleton EPUB with a fully hyperlinked TOC, attached in chat. Stops.
2. **You approve the batch plan.** The survey session replies with the
   Batch 1 kickoff pasted in the chat and ends. It does NOT start
   translating.
3. **You paste that kickoff into a NEW chat.** Every batch gets its own
   conversation; the pasted kickoff is always how the next one starts.
   **Batch 1 runs, then stops at the voice gate.** You read the first chapter
   and judge voice, footnote density, and formatting. On approval it becomes
   the frozen register reference. (Every book that skipped this gate needed a
   whole-book revision pass at the end.)
4. **Batches** run to completion, each ending with the EPUB attached and the
   next kickoff pasted in the same reply (a Stop hook enforces it).

## Message 1 — ingest and survey (paste into a NEW session first)

```
My Book SURVEY

Read CLAUDE.md in full (the working rules at the top are non-negotiable). We are translating <BOOK TITLE (author, year)> from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work only on the branch <claude/my-book>; the deliverable is <out/my-book.epub> (set book.json "deliverable").

Do STEP 0, ingest + survey, and NOTHING past it:
1. Run ./setup.sh; record anything that failed in PROGRESS.md.
2. Run scripts/ingest_epub.py source.epub. GREP the extracted text for the source's own note markers before anything else; if the book carries its own notes, open the source_notes.json stream per CLAUDE.md.
3. Author book.json from book.draft.json: real titles plus English titles, MERGE or SPLIT units where file boundaries do not match logical chapters, record excluded spine documents in _source_note, and fill in the full metadata block (Step 0 list in CLAUDE.md), including series/series_index per COLLECTION.md and the source's own cover as cover_image. Check authority.json for any name a previous book has already decided.
4. Run scripts/survey.py (final batch light), build the skeleton EPUB, run scripts/qa_epub.py until green.
5. Report: the counts, every unit's title and size, the proposed batches, AND attach the skeleton EPUB.
6. STOP and wait for approval. Once approved: write the Batch 1 kickoff into HANDOFF.md AND paste it in the chat, then end the session. Do NOT start Batch 1 in this conversation; I will paste the kickoff into a new chat. (The Batch 1 kickoff ends at the voice gate.)

Cite chapters and sections, never pages. Commit the survey.
```

## Message 2 — a translation batch (after approvals)

Written into `HANDOFF.md` by the survey session; reproduced so you know its
shape:

```
My Book B01

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating <BOOK TITLE> per CLAUDE.md. Work only on <claude/my-book>; expect the harness to start you on a stray branch and consolidate per rule 2. Deliverable <out/my-book.epub>.

Do Batch <B01> = <scope>, end to end per the CLAUDE.md pipeline:
1. Read the batch's units from data/src/. Fix extractor-split paragraphs; recover set-off formatting with apply_format_markers.py where the source HTML encodes it.
2. FIRST read the final two pages of the previous unit's English and the HANDOFF voice sheets (splice onto the actual voice, not a description of it). Then translate to the register contract, consulting glossary.json and authority.json BEFORE romanizing anything; keep the voice sheets current and flag main-cast glossary rows principal: true. Never invent bridging text; digitization glitches render to plain sense and are LISTED in PROGRESS.md; the source's own errors stay visible and footnoted.
3. Write out/<id>_en.json (one English paragraph per source line) and run make_bilingual.py; then verify_unit.py per unit AS YOU GO; check_align.py + check_content.py; verify each unit's tail against the source; check_register.py --ref <frozen reference> (from B02 on).
4. Footnotes per the reader model in CLAUDE.md (coverage-driven, first-appearance greps, NOT-re-noted list) via apparatus_merge.py; glossary rows with attestation; source's-own notes into source_notes.json; figures with translated captions and alt text.
5. Rebuild the EPUB, qa_epub.py until green, epubcheck if available; record all check results in PROGRESS.md; commit.
6. Attach the EPUB in this chat AND paste the next batch's kickoff message verbatim in a fenced block in the same reply (the Stop hook checks).

Cite chapters and sections. Do not pause for approval mid-batch.
```

Batch 1's kickoff ends instead at the voice gate. On the LAST batch, the
kickoff asks for back matter (a translated colophon if the source has one),
the whole-book reconciliation sweep, COMPLETION.md from the template, the
final EPUB committed (git add -f), and the handoff rewritten to COMPLETE.

## What each file is

- `CLAUDE.md` — the operating manual; read every session.
- `.claude/` — the Stop hook, permission allowlist, and the method-reference
  skill (cost model, register drift, build gates, fact-checking).
- `book.json` — structure + metadata; drives the build. Authored from the
  ingest draft.
- `notes.json` / `source_notes.json` / `glossary.json` / `figures.json` —
  the apparatus ledgers (translator's notes and the SOURCE's own notes are
  separate streams), edited via `scripts/apparatus_merge.py`.
- `authority.json` / `COLLECTION.md` — the cross-book ledger and shelf
  conventions.
- `back_matter.json` — optional colophon; inert until enabled.
- `scripts/` — the pipeline; each has a docstring. Shared checker scripts are
  maintained on `translation-template-master` first and synced here; fix them
  there. `tests/run_tests.py` must stay green.
- `REVISION_PLAN.template.md` / `COMPLETION.template.md` / `review/` — the
  post-completion instruments.
- `out/`, `data/` — deliverables and working files (see `.gitignore` for what
  is tracked and why).
- `PROGRESS.md` / `HANDOFF.md` / `CORRECTIONS.md` / `CHANGELOG.md` — the log,
  the baton, the correction ledger, the change record.
