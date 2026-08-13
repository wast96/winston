# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

## THE BOOK IS COMPLETE

All 168 units are translated (preface + 167 essays). The final batch (B10,
ch156–ch167) and the whole-book close-out are done. **There is no next batch
and no kickoff message.** Any further work is a corrections pass, not a batch —
see `## Corrections workflow` in `CLAUDE.md`.

The completion report is `COMPLETION.md` (read that first): status at a glance,
per-chapter tally, book-wide check results, fact-check verdicts, the deep-audit
error rate, and the residual uncertainties a reader should know about.

## What the finished edition is

- **Deliverable:** `out/scales-and-claws-of-shanghai.epub` — committed to the
  branch `claude/scales-and-claws` (`git add -f`, since `out/` is otherwise
  gitignored). Branches outlive containers; the file is in git.
- 168/168 units · 643 footnotes · 35 figures · 339 glossary rows
  (people 68 / places 66 / organizations 45 / terms 160).
- Title page states the edition is **complete**; the TOC is clean of pending
  scaffolding.
- **qa_epub: PASS** (643/643/643, all links resolve). **epubcheck 5.1.0:
  clean** (0/0/0/0, EPUB 3.3).

## State of the ledgers and tooling (do not revert)

- `out/*_reading.md` — the correction surface, one paragraph per source line.
- `out/term_ledger.md` — the whole ledger, human-auditable.
- `out/deep_audit.md` — the final random-sample audit (fixed seed 42).
- `notes.json`, `glossary.json`, `figures.json`, `book.json` — current.
- `data/ocr_fixes.json` — crop-verified readings, replayable.
- `authority.json` — fed this book's renderings under slug `scales-and-claws`.
- **Spelling locale: British** (cascaded whole-book at completion; the frozen
  reference ch001 uses "honour"). If a future correction adds prose, keep
  British curated forms (colour/honour/theatre/centre/defence/…). The
  reconcile checker prints a residual MIXED flag from two locale-neutral words
  ("laborious", "vigorous") caught by its prefix heuristic — a **false
  positive**, not a real American form; do not "fix" it by misspelling them.
- Accumulated script patches from earlier batches remain in force (do not
  revert): `check_content.py` name_map skips `_`-prefixed keys and non-dict
  values (B01); `apparatus_merge.py` glossary merge is section-aware (B02);
  `data/noise.txt` targeted rules (through B10: 萬狀, 絲毫無二/毫髮無二, 四馬路).
- `back_matter.json` is deliberately INERT: the book has no errata table, and
  its final leaves are the 2019 reprint's modern imprint page + CIP record
  (bibliographic data already in `book.json` metadata), not a historical
  colophon. The builder's colophon template is for an original copyright leaf
  and would mislabel a reprint imprint. Recorded in `COMPLETION.md` / PROGRESS.

## If the commissioner files corrections

Follow `## Corrections workflow` in `CLAUDE.md`: transcribe items into
`CORRECTIONS.md` (the ledger), apply GLOBAL corrections by a glossary/style
change plus a grep-driven cascade across ALL built units including note and
glossary bodies, LOCAL corrections at the single spot; then rebuild,
`qa_epub`, `epubcheck`, and a dated `CHANGELOG.md` entry. A zero-item
corrections pass is still a clean-checkout regression run (re-clone,
regenerate `data/zh`, rebuild, re-verify, prune stray branches).

## Notes for a fresh session

- Run `./setup.sh` once. PyMuPDF may import only as `pymupdf`/`fitz`; if
  `render.py` says `No module named 'fitz'`, `pip install pymupdf`.
- `tests/run_tests.py` shows one benign FAIL ("hook stands down on template
  stub"): with no kickoff block in HANDOFF.md the Stop hook correctly stands
  down, which the stub test reads as a fail. Working as designed now that the
  book is complete.
- OCR here is tesseract `chi_tra_vert --psm 5` only (~85%); `data/zh` was
  produced by full eye-transcription and crop-verification, not OCR replay.
  Regenerate renders/OCR from `source.pdf` as needed; the tracked ledgers and
  `out/*_reading.md` are the source of truth.
