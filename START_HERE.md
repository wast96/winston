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
2. **Edit `book.json`:** title, author, year, and the full `structure` (every
   chapter and section, with the opener's `pdf_page`/`printed_page` anchors).
   If you have the chapter map from a table of contents or PDF bookmarks, put it
   all in now; the build shows the whole book's shape from day one.
3. **Set two names:** the working branch (rule 2 in `CLAUDE.md`) and the EPUB
   filename (rule 1 / Build). Search `CLAUDE.md` for `[SET PER PROJECT]`.
4. **Plan your batches** in `book.json` -> `batches` (a chapter, or a run of
   sections, per batch).
5. That is it. `notes.json`, `glossary.json`, `figures.json` start empty and fill
   as you go. `back_matter.json` stays inert until you enable it.

## Your intro message — paste this into a NEW Claude Code session

This is the message that kicks the whole thing off. Fill in the **`<...>`**
blanks from your `book.json`, paste it as your first message in a fresh session
pointed at the project, and let it run. Everything else it needs is in
`CLAUDE.md`.

> Copy the fenced block, fill the blanks, send it. Keep it for reuse: for each
> later batch you only change the batch line (or let the previous batch's HANDOFF
> hand you the next kickoff message ready-made).

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md if one exists. We are translating <BOOK TITLE (author, year)> from an image-only scan (source.pdf) into an annotated English EPUB, following CLAUDE.md exactly.

Work only on the branch <claude/my-book>; if the session starts you on another branch, move your work onto it and drop the stray branch. Build the deliverable as <out/my-book.epub>.

Do Batch <B01> = <scope, e.g. Chapter 1, sections ch01s01-ch01s03>, PDF pages <A-B> (printed folios <a-b>), end to end:

1. Set up the environment (PyMuPDF, pillow, numpy, opencv; tesseract with the <Traditional/simplified> + vertical language packs — <script/orientation of this book>). If PaddleOCR will not install quickly, fall back to a full eye-read and say so.
2. First engineering task: measure this book's page furniture on a dozen rendered pages and configure scripts/ocr_crop.py (crop box, --lang, --psm, --running-head). Render, then OCR with the measured crop; verify pgrep -c tesseract is 0 after.
3. Read every page off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Verify every name, number, and low-confidence span against a magnified crop before writing. Never invent bridging text — if the scan cuts off or is damaged, crop and read it, and if it truly can't be read, footnote the gap.
4. Author one aligned out/<id>_bilingual.md, generate the reading text and parity source with scripts/split_bilingual.py, then run scripts/check_numbers.py and scripts/check_structure.py --pairs. Run scripts/find_figures.py and also eyeball every page for line art (the detector misses charts); crop figures by hand into figures.json.
5. Do blind double-translation and back-translation on the argumentative passages; fact-check names/dates against real scholarship (never Grok/Grokipedia).
6. Add footnotes to notes.json (keyed by unit id, three kinds, ~3/printed page, XHTML bodies with numeric character references) and extend glossary.json with attestation.
7. Rebuild the EPUB with the full pending-aware TOC (nested to section level), run scripts/qa_epub.py until green.
8. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch.

Cite printed folios, never PDF pages. Don't pause for my approval; run the whole batch and report back when it's built and QA-green, and paste the next-batch kickoff message at the end of your reply.
```

## After the first batch

Each batch's `HANDOFF.md` will contain the next batch's kickoff message,
ready to paste. So after batch one you rarely write the intro by hand again:
open `HANDOFF.md`, copy its first section, start a fresh session, paste. On the
last batch, ask for the final back matter (errata/colophon if the book has them),
a whole-book QA pass, and a completion report instead of another handoff.

## What each file is

- `CLAUDE.md` — the operating manual. Read by the assistant every session.
- `book.json` — the whole book's structure; drives the build. You fill this in.
- `notes.json` / `glossary.json` / `figures.json` — apparatus, fill as you go.
- `back_matter.json` — optional errata/colophon; inert until enabled.
- `scripts/` — the pipeline (render, OCR-crop, figures, split-bilingual, the two
  checks, the EPUB builder, the EPUB QA). Each has a docstring.
- `out/` — deliverables: `<id>_reading.md` per unit and the built EPUB.
- `data/` — working files (renders, OCR text, crops); regenerable, git-ignored.
- `PROGRESS.md` / `HANDOFF.md` / `CORRECTIONS.md` / `CHANGELOG.md` — the log, the
  baton, the correction inbox, the change record.
