# HANDOFF — Zhou Enlai: Commander of the Hidden Front

## THE BOOK IS COMPLETE, AND THE REGISTER PASS IS CLOSED

All 28 units are translated (ch00 Preface through ch27 Afterword), and the
five-batch **register revision pass (R1-R5)** is now finished as well. There
is no next register batch, so this file no longer carries a paste-ready
kickoff section. Read `COMPLETION.md` first (its "Register revision pass
(R1-R5)" section is the revision record); `PROGRESS.md` and `CHANGELOG.md`
carry the per-batch detail.

Further work on this book is one of two things, in this order:

1. **The footnote-density pass the commissioner requested** — greatly increase
   footnote coverage across the whole book (people, places, events, offices,
   terms, allusions: everything a non-specialist Western reader would miss),
   without padding. This is a NEW initiative beyond the register pass. Its
   plan and its paste-ready per-batch kickoffs live in **`FOOTNOTE_PASS.md`**
   (start with its `## 9. Kickoff` block for FN1). Do this next.
2. **A corrections pass** (CLAUDE.md corrections workflow) for anything the
   commissioner files in `CORRECTIONS.md` or pastes in chat. A zero-item
   corrections pass is still a clean-checkout regression run.

## Final state

- Deliverable: `out/zhou-enlai.epub`, committed with `git add -f` on branch
  `claude/zhou-enlai`. 28/28 chapters, 339 notes, 36 figures, 496 pagebreaks.
- `qa_epub.py`: PASS (all links resolve). `epubcheck` 5.1.0: 0 errors, 0 warnings.
- Ledgers current: `glossary.json` (847 rows), `notes.json` (339),
  `figures.json`, `book.json`; `authority.json` fed with this book's decided
  renderings; `out/term_ledger.md` and `out/deep_audit.md` written;
  `CHANGELOG.md` and `PROGRESS.md` current.
- Register pass ledgers: `REVISION_PLAN.md` (the pass that governed R1-R5),
  `review/REGISTER_PASS_ASSESSMENT.md`, `out/ch01_reading.pre-R.md` (the frozen
  register reference), `STYLE.md` (the prose contract, with its calibrated
  rulings ledger).

## Register-pass residuals recorded for a future corrections pass

- **破坏 -> "wreck*"**: reviewed book-wide in R5 and left as contextually
  appropriate (mass-arrest destruction = smash/wreck/destroy, not the
  covert-subversion "sabotage"). If the commissioner ever wants a uniform
  "sabotage", PROGRESS.md's R5 section has the full site inventory; note that
  many sites sit inside quoted documents/memoirs (KEEP).
- **4 unused glossary forms** (Chen Zhifei, Zhao Minlin, Jiang Baili, Guangming
  Daily) are pre-existing and legitimate (referent rendered by given name or a
  variant); left as-is.

## Do not revert (accumulated tooling)

- `data/ocr_fixes.json`: crop/context-verified readings for ch00&#8211;ch27;
  replay with `apply_fixes.py` on any fresh regen.
- `scripts/recovery/`: the b01_* through b14_* strip/surgery/pagemap/addfixes/
  glossary scripts and the `b1X_rebuild.sh` drivers (b10&#8211;b14 rebuild
  ch17&#8211;ch27 from `data/txt_backup_b1*` with no re-OCR); plus
  `r5_collapse_renegade.py` (the 叛徒 reconciliation cascade) and
  `gen_date_edits.py` (R1's date-normalization edit-list generator).
- `data/noise.txt`: keep extending, never prune.
- `data/check_config.json`: docs + sources for ch00&#8211;ch27.
- Builder invariants (full pending-aware then cleaned TOC; note pop-ups with
  endnotes fallback; refusal to build on an unmatched anchor or unplaced
  figure; byte-identical cover copy; render-layer smart quotes).

## How to rebuild from a clean checkout

1. `./setup.sh`
2. regenerate `data/zh/` with the `scripts/recovery/b*_rebuild.sh` drivers for
   b10&#8211;b14 (ch17&#8211;ch27); b01&#8211;b09 re-OCR from `source.pdf` with
   the recorded crops per `scripts/recovery/README.md`.
3. `python3 scripts/build_reading_epub.py`
4. `python3 scripts/qa_epub.py`
5. `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/zhou-enlai.epub`

## Environment notes

- Body offset is a constant 44 (printed = PDF minus 44). PaddleOCR's weights
  host is usually unreachable; `scripts/ocr_dual.py` is the dual-tesseract
  substitute. `OMP_THREAD_LIMIT=1` for tesseract; check `pgrep -c tesseract`
  reads 0 after a run. There is one pre-existing failing regression test
  ("hook stands down on template stub"), template maintenance only, unrelated
  to the book.
