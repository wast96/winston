# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

## The register pass is COMPLETE — there is no next batch

The whole-book register pass (the R-series, R01 to R08) is finished. This file no
longer carries a paste-ready kickoff, because the last batch writes a completion
report instead of another handoff. The register-pass completion is recorded in
`COMPLETION.md` (the "Register pass (the R-series)" section) and each batch has a
dated entry in `CHANGELOG.md` (R01 to R08) and a section in `PROGRESS.md`.

If new work is commissioned (e.g. reader corrections), follow the corrections
workflow in `CLAUDE.md`: file items in `CORRECTIONS.md`, apply GLOBAL fixes via a
glossary/style change plus a grep-driven edit across ALL built units, rebuild, run
`qa_epub.py`, run the straight-quote guard, and append a dated `CHANGELOG.md` entry.

## State of the project

- Translation COMPLETE (B01 to B13); register pass COMPLETE (R01 to R08). All 36
  units (ch00 to ch35) translated and register-revised, glossary 273 entries.
- Footnotes: **224**, continuous numbering, at the densified reference policy.
- Deliverable: `out/On a Hair Trigger.epub`, full hyperlinked TOC, Translator's
  Note, glossary. `qa_epub.py` PASS (48 files, 42 documents, 7,082 paragraphs,
  224 references = 224 bodies = 224 backlinks). Straight-quote guard clean on all
  36 reading files. No colophon (source has none; `back_matter.json` is inert).
- Edit lists for the whole pass committed under `edits/` (ch00 backfill, ch02 to
  ch35).

## Reference documents

- `COMPLETION.md` — whole-book completion report; its last section records the
  register pass and confirms the definition-of-done.
- `REGISTER_PASS.md` — the operating instruction for the register pass (done).
- `PROGRESS.md` — per-batch log, B01 through B13 and R01 through R08.
- `CHANGELOG.md` — dated record of corrections and revisions (newest first).
- `edits/` — committed per-chapter edit lists.

## Rebuilding from a clean checkout

`data/src`, `data/zh`, `out/*_en.txt`, and `out/*.epub` are gitignored. From a
fresh clone: `python3 scripts/ingest_epub.py source.epub` to rebuild `data/src`;
then, for each id ch00..ch35, `python3 scripts/split_bilingual.py
"out/<id>_bilingual.md" <id> "<zh title from book.json>"` to rebuild `data/zh` and
`out/<id>_reading.md`; then `python3 scripts/build_reading_epub.py
"out/On a Hair Trigger.epub"` and `python3 scripts/qa_epub.py
"out/On a Hair Trigger.epub"`.

## The single working branch

All work for this book lives on `claude/on-a-hair-trigger` (CLAUDE.md rule 2). A
session started on a per-batch branch folds its work onto `claude/on-a-hair-trigger`
and retires the stray branch, local and remote.
