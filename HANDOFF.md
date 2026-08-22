# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

## THE BOOK IS COMPLETE

All 12 units are translated, annotated, built, and verified. There is no next
batch. The full completion report is in `COMPLETION.md`; read that first. This
file is now only a pointer.

## A REVISION PASS IS PLANNED (2026-08-22): read REVISION_PLAN.md

The commissioner has commissioned a register/style/apparatus pass over the
completed book. `REVISION_PLAN.md` is the operating document and it is
SELF-CONTAINED: every imported rule is reproduced there in full. **Do NOT
fetch, read, or pull anything from `claude/the-sword-roars` or any other
branch; all work stays on `claude/chen-yangshan`.** The pass starts with the
R0 kickoff in the plan's §9 and is gated on the commissioner's tier decision.
Where this file and the plan disagree, the plan wins.

Any further work is a **corrections pass**, not a batch: the commissioner reads
the EPUB and files items in `CORRECTIONS.md` (or pastes them in chat, and you
transcribe them there first). Follow the corrections workflow in CLAUDE.md —
global corrections cascade via a glossary/style change plus a grep-driven edit
across ALL built units including note and glossary bodies, then rebuild and full
QA; local corrections are a single-spot fix. A zero-item corrections pass is
still a clean-checkout regression run.

## Final state

- **12 of 12 units** (ch00 foreword; ch01-ch06; ch07-ch09 appendices I-III;
  ch10 references; ch11 afterword). 1,256 body paragraphs.
- **432 footnotes**, **78 figures**, **731 glossary referents** (52 provisional,
  all minor bit-part names).
- **Deliverable:** `out/chen-yangshan.epub` (committed with `git add -f`).
  qa_epub PASS (104 files, 432/432/432 notes resolve); epubcheck 5.1.0 0/0/0.
  Title page reads COMPLETE.
- **Ledgers current:** `notes.json`, `glossary.json`, `figures.json`, `book.json`,
  `authority.json` (fed this book's decided renderings). `out/term_ledger.md` and
  `out/deep_audit.md` rendered. `COMPLETION.md`, `PROGRESS.md`, `CHANGELOG.md`
  current.
- **Branch:** all work on `claude/chen-yangshan`.

## Do-not-revert (accumulated tooling, still in force)

- OCR body crop: `ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985
  --top 0.08 --running-head "秘战英雄陈养山"`, recto (PDF even) `--bottom 0.945`,
  verso (PDF odd) `--bottom 0.915`. Front-matter pages 7-8 use a different crop.
- Builder: section-nav omits pending sections; refuses on an unmatched note anchor
  or unplaced figure; figure `alt` carries no straight double quotes;
  `strip_runfoot` removes the verso book-title foot.
- `apparatus_merge` merges glossary rows into sections; **REPLACES a unit's
  figures wholesale** — for a chapter split across batches, always re-include the
  prior batch's figures or they are dropped silently (this bit ch02; recovered in
  B10). `data/zh` is gitignored and regenerated per unit; run per-unit checks with
  the scoped `data/check_config.<id>.json`.

## Environment notes for a future rebuild

- `./setup.sh` once; epubcheck at `/tmp/epubcheck-5.1.0/epubcheck.jar` (setup
  re-fetches on a fresh container). `OMP_THREAD_LIMIT=1` for tesseract.
- Rebuild: `python3 scripts/build_reading_epub.py`, `python3 scripts/qa_epub.py`,
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chen-yangshan.epub`.
- The setup.sh regression "hook stands down on template stub: FAIL" is benign
  (the fixture expects a placeholder HANDOFF; this one is a real/complete handoff).
