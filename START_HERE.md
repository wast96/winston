# START HERE — spin up a new translation project from this template

This branch (`translation-template-master`) is a ready-to-clone starter kit for
translating one scanned book into an annotated English EPUB, using the same
process we built on real books. It carries the pipeline scripts, the operating
manual (`CLAUDE.md`), and empty data files. No book is loaded in.

There are two ways to use it. Pick one.

## Option A — a new folder inside this repo (simplest)

Good when you want all your translation projects living side by side in one repo.

```
# from the repo root, on the template branch:
git checkout translation-template-master
# copy the template into a new project folder named after the book:
mkdir -p ../my-book && git archive translation-template-master | tar -x -C ../my-book
# actually keep it in-repo:
git checkout <your-main-branch>
git checkout -b claude/my-book
mkdir my-book && git archive translation-template-master | tar -x -C my-book
# drop the scan in and start editing:
cp /path/to/scan.pdf my-book/source.pdf
```

Then all commands run from inside `my-book/` and paths in `book.json` stay
relative to it (the scripts locate the project root themselves).

## Option B — a fresh branch that IS the project (cleanest history)

Good when you want one book per branch with nothing else in it.

```
git checkout -b claude/my-book translation-template-master
cp /path/to/scan.pdf source.pdf
```

Now the branch root IS the project.

## One-time setup (either option)

1. **Drop the scan in as `source.pdf`.**
2. **Set two names in `book.json`/`CLAUDE.md`:** the working branch (rule 2) and
   the EPUB filename (rule 1 / Build). Search `CLAUDE.md` for `[SET PER PROJECT]`.
3. That is it for you. You do NOT hand-enter the structure or plan the batches:
   the first session does the survey (below), fills in `book.json`, proposes the
   batches, and shows you a navigable skeleton EPUB to approve. `notes.json`,
   `glossary.json`, `figures.json` start empty; `back_matter.json` is inert until
   enabled.

## The flow: survey first, then batches

1. **Survey** (message 1, below): the session reads the book's table of contents
   / bookmarks, fills in the whole structure, and hands you back the counts (how
   many parts, chapters, sections, subsections), each unit's title and page
   length, a proposed batch breakdown, and a **skeleton EPUB with a fully
   hyperlinked table of contents** attached in chat. It then stops.
2. **You approve** the batch plan (or adjust it).
3. **Batches** (message 2, below): the session runs Batch 1 end to end and, from
   then on, each batch's `HANDOFF.md` hands you the next batch's kickoff message
   ready to paste.

## Message 1 — the survey (paste into a NEW session first)

Fill the **`<...>`** blanks and send. This produces the structure report and the
hyperlinked-TOC EPUB for your approval; it does not translate anything yet.

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable). We are translating <BOOK TITLE (author, year)> from an image-only scan (source.pdf) into an annotated English EPUB, following CLAUDE.md exactly. Work only on the branch <claude/my-book>; build the deliverable as <out/my-book.epub>.

Do STEP 0, the structural survey, and NOTHING past it yet:
1. Set up the environment (PyMuPDF, pillow, numpy, opencv). Render the front matter / table of contents pages and read the book's own contents; if the PDF has bookmarks, use them too.
2. Fill in book.json completely: every part, chapter, section and subsection in reading order, with each opener's pdf_page and printed_page and both the source title and an English title, plus pdf_end/printed_end. Spot-verify openers by reading the printed folio off the scan (the offset drifts; never assume a constant).
3. Run scripts/survey.py and build the skeleton EPUB with scripts/build_reading_epub.py; run scripts/qa_epub.py until green.
4. Report back to me with: the counts (parts / chapters / sections / subsections), every unit's title and page length, and a proposed batch breakdown — and attach the skeleton EPUB (the hyperlinked table of contents) to the chat so I can navigate it.
5. STOP and wait for me to approve the batch plan. Do not start translating. Once I approve, write the Batch 1 kickoff message into HANDOFF.md.

Cite printed folios, never PDF pages. Commit the survey (book.json + SURVEY.md).
```

## Message 2 — a translation batch (after you approve the plan)

The survey session writes this into `HANDOFF.md` for you, already filled in. It
is reproduced here so you know what it looks like; normally you just copy it from
`HANDOFF.md`.

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating <BOOK TITLE> into an annotated English EPUB per CLAUDE.md. Work only on <claude/my-book>; build <out/my-book.epub>.

Do Batch <B01> = <scope, e.g. Chapter 1, sections ch01s01-ch01s03>, PDF pages <A-B> (printed folios <a-b>), end to end:
1. Environment: tesseract with the <Traditional/simplified> + vertical language packs (<script/orientation of this book>). If PaddleOCR will not install quickly, fall back to a full eye-read and say so.
2. First engineering task (batch 1 only): measure this book's page furniture on a dozen rendered pages and configure scripts/ocr_crop.py (crop box, --lang, --psm, --running-head). Render, then OCR; verify pgrep -c tesseract is 0 after.
3. Read every page off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Verify every name, number, and low-confidence span against a magnified crop before writing. Never invent bridging text — if the scan cuts off or is damaged, crop and read it, and if it truly can't be read, footnote the gap.
4. Author one aligned out/<id>_bilingual.md, generate the reading text and parity source with scripts/split_bilingual.py, then run scripts/check_numbers.py and scripts/check_structure.py --pairs. Run scripts/find_figures.py and also eyeball every page for line art (the detector misses charts); crop figures by hand into figures.json.
5. Blind double-translation and back-translation on the argumentative passages; fact-check names/dates against real scholarship (never Grok/Grokipedia).
6. Add footnotes to notes.json (keyed by unit id, three kinds, ~3/printed page, XHTML bodies with numeric character references) and extend glossary.json with attestation.
7. Rebuild the EPUB (the TOC stays fully linked, nested to subsection level), run scripts/qa_epub.py until green.
8. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch.

Cite printed folios, never PDF pages. Don't pause for my approval; run the whole batch and report back when it's built and QA-green, and paste the next-batch kickoff message at the end of your reply.
```

On the last batch, ask for the final back matter (errata/colophon if the book has
them), a whole-book QA pass, and a completion report instead of another handoff.

## What each file is

- `CLAUDE.md` — the operating manual. Read by the assistant every session.
- `book.json` — the whole book's structure; drives the build. You fill this in.
- `notes.json` / `glossary.json` / `figures.json` — apparatus, fill as you go.
- `back_matter.json` — optional errata/colophon; inert until enabled.
- `scripts/` — the pipeline (survey, render, OCR-crop, figures, split-bilingual,
  the two checks, the EPUB builder, the EPUB QA). Each has a docstring.
- `out/` — deliverables: `SURVEY.md`, `<id>_reading.md` per unit, and the EPUB.
- `data/` — working files (renders, OCR text, crops); regenerable, git-ignored.
- `PROGRESS.md` / `HANDOFF.md` / `CORRECTIONS.md` / `CHANGELOG.md` — the log, the
  baton, the correction inbox, the change record.
