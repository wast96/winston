# The Theory and Practice of Secret Service Work — translation package

Gu Shunzhang (顧順章), 特務工作之理論與實際 (Nanjing, 1933). Annotated English
translation from an image-only scan (National Central Library, Taiwan copy).

This book is translated in **batches**, each with a full eight-check QC pass,
its footnotes, an updated cumulative EPUB, and a handoff file for the next
instance. It is not run unattended end to end.

Setup:
1. `source.pdf` is already in this folder (committed to the branch).
2. Open this folder in Claude Code and say: "Read CLAUDE.md, then translate
   the next batch" (or name the chapter/sections you want).

Each batch produces:
- `out/<id>_reading.md` — the clean English for the batch (the correction surface).
- Footnotes folded into `notes.json`.
- The eight checks run, results in `PROGRESS.md`.
- A rebuilt `out/theory-practice.epub` whose TOC covers the whole book, with
  translated units linked and the rest shown as pending.
- An updated `HANDOFF.md` telling the next instance exactly where to start.

When Winston has read a batch: write corrections into `CORRECTIONS.md`, then say
"Apply CORRECTIONS.md." Global corrections cascade across every built unit.

Contents:
- `CLAUDE.md`     — the playbook (source facts, pipeline, the eight checks, register)
- `book.json`     — the 8-chapter / 37-section map with page anchors and English titles
- `glossary.json` — every rendering decided so far, with status and attestation
- `notes.json`    — the footnote apparatus, keyed by unit
- `PROGRESS.md`   — working state; read this first
- `HANDOFF.md`    — the baton for the next instance
- `CORRECTIONS.md`— Winston's review surface
- `reference/`    — the translated table of contents, and other reference material
- `scripts/`      — the pipeline (inherited from the sibling projects; see CLAUDE.md
                    for what needs re-measuring for this book's vertical layout)
- `out/`          — reading markdown per unit, and the EPUB
