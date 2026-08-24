# HANDOFF — Zhou Enlai: Commander of the Hidden Front

**The book is COMPLETE, and the footnote-density pass (FN1-FN5) is now also
CLOSED.** There is no next batch. Further work on this book is a corrections
pass per CLAUDE.md (`CORRECTIONS.md` is the ledger), not new translation and not
another footnote batch. This file no longer carries a paste-ready kickoff,
because there is nothing left to kick off.

## Where the book stands

- Translation of all 28 units (ch00-ch27); register pass R1-R5 (see COMPLETION.md).
- **Footnote-density pass complete: 339 -> 457 footnotes** across FN1-FN5.
  - FN1 ch00-ch05: 339 -> 385. FN2 ch06-ch11: 385 -> 409. FN3 ch12-ch17: 409 ->
    427. FN4 ch18-ch22: 427 -> 441. **FN5 ch23-ch27 + whole-book reconciliation:
    441 -> 457.** Per-batch detail, "NOT re-noted" lists, fact-check verdicts, and
    reconciliations are in PROGRESS.md's FN1-FN5 sections. FN5 merged via
    `data/fn5_notes.json` (authored by `scripts/recovery/fn5_authorel.py`) and the
    three reconciliation trims applied by `scripts/recovery/fn5_trims.py`.
- **All FN5 backlog cleared** (the FN3/FN4 "Items flagged for FN5" lists):
  shikumen (ch02), Sun Yat-sen University Moscow (moved to ch03), the Third Plenum
  of the Eleventh CC (ch04), Sun Chuanfang (ch05), Shen Bao (moved to ch10), the
  China Mutual Aid Society / China Relief Society tie + Ta Kung Pao (ch14), the
  E-Yu-Wan Soviet (moved to ch15), the Baoding Military Academy (ch16, corrected
  from the mis-flagged ch03 which is Baoding Road), Li Mingrui (ch17). The 互济会
  "rendering drift" was resolved as a historical rename, not an error (see PROGRESS
  FN5). Hu Yepin's ch09/ch20/ch22 cluster confirmed complementary, not
  double-noted.

## Deliverable / state

- `out/zhou-enlai.epub` (committed with `git add -f`). 28/28 chapters, **457
  notes**, 36 figures, 496 pagebreaks. qa_epub PASS (457 refs/bodies/backlinks);
  epubcheck 5.1.0 0/0/0 (EPUB 3.3).
- Ledgers: `glossary.json` (847 rows, unchanged by FN5), `notes.json` (457),
  `figures.json`, `book.json`, `authority.json`; `out/term_ledger.md` current
  (unchanged — FN5 added no glossary rows) and `out/deep_audit.md` from the
  register close.
- Branch: all work on `claude/zhou-enlai`. Body offset constant 44 (printed =
  PDF - 44). `data/zh` is absent on a fresh checkout (regenerable parity scaffold,
  not needed for a notes-only pass). `OMP_THREAD_LIMIT=1` for tesseract.

## Rebuild from a clean checkout

1. `./setup.sh`
2. `python3 scripts/build_reading_epub.py`
3. `python3 scripts/qa_epub.py`
4. `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/zhou-enlai.epub`

## Do not revert (accumulated tooling)

- `scripts/fa_check.py` (first-appearance grep) and `scripts/gloss_hanzi.py`
  (glossary hanzi reverse-lookup); `scripts/recovery/fn5_authorel.py` and
  `scripts/recovery/fn5_trims.py` (FN5 authoring + reconciliation).
- `data/ocr_fixes.json`; `scripts/recovery/` (b01-b14 + r5/date generators);
  `data/noise.txt` (extend, never prune); `data/check_config.json`; builder
  invariants (pending-aware then cleaned TOC; note pop-ups with endnotes fallback;
  refusal to build on an unmatched anchor or unplaced figure; byte-identical cover
  copy; render-layer smart quotes).

## If the commissioner files corrections

Follow the corrections workflow in CLAUDE.md: transcribe into `CORRECTIONS.md`,
apply GLOBAL changes with a glossary/style change plus a grep-driven cascade
across ALL built units including note and glossary bodies, then rebuild and full
QA; LOCAL changes are a single-spot fix. Every corrections batch ends with a
rebuild, `qa_epub`, and a dated `CHANGELOG.md` entry.
