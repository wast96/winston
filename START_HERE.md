# START HERE — spin up a new translation project from this template

This branch (`translation-template-master`) is a ready-to-clone starter kit for
translating one scanned book into an annotated English EPUB, using the same
process we built on nine real books. It carries the pipeline scripts, the
operating manual (`CLAUDE.md`), the enforcement layer (`.claude/`), the method
references (the `scanned-book-translation` skill), and empty data files. No
book is loaded in.

There are two ways to use it. Pick one.

## Option A — a new folder inside this repo (simplest)

```
git checkout translation-template-master
git checkout <your-main-branch>
git checkout -b claude/my-book
mkdir my-book && git archive translation-template-master | tar -x -C my-book
cp /path/to/scan.pdf my-book/source.pdf
```

Then all commands run from inside `my-book/`.

## Option B — a fresh branch that IS the project (cleanest history)

```
git checkout -b claude/my-book translation-template-master
cp /path/to/scan.pdf source.pdf
```

## One-time setup (either option)

1. **Drop the scan in as `source.pdf`.**
2. **Set the two [SET PER PROJECT] values:** the working branch (CLAUDE.md
   rule 2) and the deliverable filename (`book.json` `deliverable`). Also set
   the kickoff label (`My Book` in the messages below).
3. **Consult `authority.json`** (the cross-book name ledger) if this book
   shares people, places or institutions with earlier books on the shelf, so
   renderings agree across the collection; set `series`/`series_index` in
   `book.json` per `COLLECTION.md`.
4. That is it. You do NOT hand-enter the structure or plan the batches: the
   first session runs the survey, fills in `book.json`, proposes the batches,
   and shows you a navigable skeleton EPUB to approve.

## The flow: survey, then ONE chapter, then batches

1. **Survey** (message 1): structure, counts, proposed batches, skeleton EPUB
   with a fully hyperlinked TOC, attached in chat. The session stops.
2. **You approve the batch plan** (or adjust it).
3. **Batch 1 runs, then stops again — the voice gate.** You read the first
   chapter in the EPUB and judge three things: the voice, the footnote
   density (does it catch everything you'd miss), and the formatting. This is
   the cheapest moment to change the whole book; every completed book that
   skipped this gate needed a whole-book revision pass at the end. On your
   approval the chapter is frozen as the register reference.
4. **Batches** run to completion from then on, each ending with the EPUB
   attached and the next kickoff pasted in the same reply.

## Message 1 — the survey (paste into a NEW session first)

Fill the **`<...>`** blanks and send.

```
My Book SURVEY

Read CLAUDE.md in full (the working rules at the top are non-negotiable). We are translating <BOOK TITLE (author, year)> from an image-only scan (source.pdf) into an annotated English EPUB, following CLAUDE.md exactly. Work only on the branch <claude/my-book>; the deliverable is <out/my-book.epub> (set book.json "deliverable").

Do STEP 0 (a, b) and NOTHING past it yet:
1. Run ./setup.sh; record anything that failed in PROGRESS.md.
2. Fill in book.json metadata (Step 0a), including series/series_index per COLLECTION.md, and check authority.json for any recurring names.
3. Characterize the book (script, orientation, register, apparatus, quirks) and build the complete structure in book.json: every part/chapter/section/subsection with pdf_page and printed_page, titles in both languages. Use PDF bookmarks if present but verify against the scan; if there is no TOC and no bookmarks, use find_headings.py + build_structure.py. Read folios off the scan; the offset drifts.
4. Run scripts/survey.py; build the skeleton EPUB; run scripts/qa_epub.py until green.
5. Report: the characterization, the counts, every unit's title and length, the proposed batches (final batch light), AND attach the skeleton EPUB.
6. STOP and wait for approval. Once approved, write the Batch 1 kickoff into HANDOFF.md, ending it with the reminder that Batch 1 ends at the voice gate.

Cite printed folios, never PDF pages. Commit the survey.
```

## Message 2 — a translation batch (after approvals)

The survey session writes this into `HANDOFF.md`, already filled in; normally
you just copy it from there. Reproduced so you know its shape:

```
My Book B01

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating <BOOK TITLE> per CLAUDE.md. Work only on <claude/my-book>; expect the harness to start you on a stray branch and consolidate per rule 2. Deliverable <out/my-book.epub>.

Do Batch <B01> = <scope>, PDF pages <A-B> (printed folios <a-b>), end to end per the CLAUDE.md pipeline:
1. ./setup.sh; batch 1 only: measure the page furniture and configure ocr_crop.py (crop box, --lang, --psm); render; OCR (ocr_crop.py + ocr_dual.py); pgrep -c tesseract must be 0 after.
2. indents.py + assemble.py for paragraph structure; find_figures.py AND eyeball every page for line art.
3. Translate to the register contract, consulting glossary.json and authority.json BEFORE romanizing anything. Crop-verify every name, number, and low-confidence span (verify_names.py --auto for disagreements, crop_lines.py for systematic mangles); record verified readings via apply_fixes.py. Never invent bridging text; verify each unit's tail against the scan.
4. Write out/<id>_en.json, make_bilingual.py, then verify_unit.py per unit AS YOU GO; check_align.py + check_content.py; check_register.py --ref <frozen reference> (from B02 on).
5. Footnotes per the reader model in CLAUDE.md (coverage-driven; grep for first appearances; keep the NOT-re-noted list) via apparatus_merge.py; glossary rows with attestation; figures with alt text.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available; record all check results in PROGRESS.md; commit.
7. Attach the EPUB in this chat AND paste the next batch's kickoff message verbatim in a fenced block in the same reply (the Stop hook checks).

Cite printed folios. Do not pause for approval mid-batch.
```

Batch 1's kickoff differs in one way: it ends "then STOP at the voice gate:
present the chapter and ask for approval of voice, note density and
formatting before writing the B02 kickoff."

On the LAST batch, the kickoff instead asks for back matter, the whole-book
reconciliation sweep, COMPLETION.md from the template, the final EPUB
committed (git add -f), and the handoff rewritten to COMPLETE.

## What each file is

- `CLAUDE.md` — the operating manual; read by the assistant every session.
- `.claude/` — enforcement (Stop hook for the kickoff paste; permission
  allowlist) and the `scanned-book-translation` skill with the method
  references (cost model, register drift, build gates, fact-checking).
- `book.json` — structure + metadata; drives the whole build.
- `notes.json` / `glossary.json` / `figures.json` — apparatus ledgers, edited
  only via `scripts/apparatus_merge.py`.
- `authority.json` / `COLLECTION.md` — the cross-book name ledger and the
  collection conventions (series metadata, reading order).
- `back_matter.json` — optional errata/colophon; inert until enabled.
- `scripts/` — the pipeline; each has a docstring. `tests/run_tests.py` is
  the regression harness for the checkers; keep it green.
- `REVISION_PLAN.template.md` / `COMPLETION.template.md` / `review/` — the
  post-completion instruments.
- `out/` — deliverables; `data/` — working files (see `.gitignore` for what
  is tracked and why).
- `PROGRESS.md` / `HANDOFF.md` / `CORRECTIONS.md` / `CHANGELOG.md` — the log,
  the baton, the correction ledger, the change record.
