# HANDOFF — Midnight (子夜), Mao Dun — BOOK COMPLETE

This book is finished. There is no next batch. This file is no longer a baton;
it records the final state. The whole-book summary is in `COMPLETION_REPORT.md`.

## Status

- **All 20 units translated** (Chapters One–Nineteen + the Afterword 后记),
  243,113 source characters. Deliverable: `out/Midnight.epub`.
- **B18 (final batch)** closed the book: ch18, ch19, ch20. See `PROGRESS.md`
  for the per-batch record and `COMPLETION_REPORT.md` for the whole-book report.

## Final checks (all green)

- Verbatim source quotation: 0 mismatches (B18 verified mechanically, 286/286
  paragraphs); paragraph parity OK on every unit.
- `check_numbers.py --noise data/noise_zh.txt`: 0 unresolved on every unit.
- `check_structure.py --pairs`: parity OK on every unit.
- `qa_epub.py out/Midnight.epub`: PASS — 32 files, 26 documents, 109 note
  references / 109 bodies / 109 backlinks, all links resolve.
- `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings.
- Random-sample deep audit (~5% of B18): 0 substantive errors.

## Counts

- Translator footnotes: **109** (builder-numbered 1–109, continuous).
- Author (source) endnotes: **9**, placed and frozen (`source_notes.json`):
  ch01 [1][2], ch02 [3], ch05 [4], ch06 [5][6][7], ch11 [8][9].
- Glossary: **384 entries** (people 118, organizations 50, places 115, terms 101).

## If corrections come

The commissioner reads the EPUB and files corrections in `CORRECTIONS.md`. Follow
the corrections workflow in `CLAUDE.md`: GLOBAL corrections cascade via a glossary/
style change plus a grep-driven edit across ALL built units, then rebuild and full
QA; LOCAL corrections are a one-spot fix. After any corrections batch: rebuild
`out/Midnight.epub`, run `qa_epub.py out/Midnight.epub` and `epubcheck`, list every
file touched, and append a dated entry to `CHANGELOG.md`.

## Rebuild reminders (unchanged)

- Deliverable filename is `out/Midnight.epub`; the builder and qa default to
  `out/book.epub`, so pass `out/Midnight.epub` explicitly on every build and qa run.
- `data/src/` is git-ignored and regenerable: `scripts/ingest_epub.py source.epub`.
- epubcheck 5.1.0 jar: `/tmp/epubcheck-5.1.0/epubcheck.jar` (re-fetch from the
  w3c/epubcheck GitHub release if a fresh container lacks it).
- One branch only: `claude/midnight`.
