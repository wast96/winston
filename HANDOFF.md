# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

## Message to paste into the next chat

```
Hair Trigger R01

Read CLAUDE.md, then REGISTER_PASS.md (in full; it is the operating
instruction for this pass), then HANDOFF.md, then book.json. The translation
is complete (B01 to B13); this is the REGISTER PASS: a style-only revision of
the English, per the commissioner's readability feedback. ch00 and ch01 are
already revised and are the exemplar; study `git show 895d19c` before
starting.

The pass has TWO workstreams, run together: (1) the style revision, and
(2) footnote densification to the new policy (REGISTER_PASS.md, "The
annotation gap"): the reader is a Westerner with no background in Chinese
history, family structure, or custom; anything such a reader would miss earns
a note at first occurrence, roughly 8 to 15 per chapter.

Do batch R01 = ch02, ch03, ch04, ch05, ch06, end to end, PLUS the
note-densification backfill of ch00 (ch00/ch01 prose is done; ch01's notes
are already densified to 15 and are the model). ANALYZE each chapter against the
source in out/<id>_bilingual.md and commit the edit lists to
edits/<id>_edits.md in the format REGISTER_PASS.md specifies (TOUCH/RECAST
blocks, NOTE-ANCHOR items, NOTE-ADD blocks), then EXECUTE them exactly
(exact-match replacement, count == 1, via Python). Style only: never touch a
source line, never merge or split paragraphs, nothing invented, nothing
dropped, names per glossary.json, note anchors kept in step with notes.json,
new-note anchors verified as verbatim substrings BEFORE building. After
editing: regenerate with split_bilingual.py, run check_structure --pairs and
check_numbers --noise per chapter, run the straight-quote typography guard,
rebuild "out/On a Hair Trigger.epub", run qa_epub.py until green. Spot-audit
10% of edited paragraphs against the source for meaning drift. Record
everything in PROGRESS.md, append a dated CHANGELOG.md entry, rewrite
HANDOFF.md's kickoff for R02 (ch07 to ch11), commit and push to
claude/on-a-hair-trigger (the ONLY branch). Do not pause for approval
mid-batch. Deliver the rebuilt EPUB in chat, and end the reply with the R02
kickoff verbatim in a fenced block.
```

## State of the project

- Translation COMPLETE: B01 to B13 done, all 36 units (ch00 to ch35)
  translated, annotated (117 footnotes), glossary 273 entries, EPUB
  `out/On a Hair Trigger.epub` with full TOC, qa green book-wide.
- 2026-08-03 whole-book QC read-through: done, minor fixes applied (see
  CHANGELOG.md).
- Typography normalized book-wide (uniform curly quotes, apostrophes,
  ellipses); a straight quote in prose is now a regression.
- REGISTER PASS in progress: the commissioner found the English at many points
  too literal (calqued idioms, scene cards as body copy, transferred syntax).
  `REGISTER_PASS.md` defines the whole pass: taxonomy, triage, two-phase
  ANALYZE/EXECUTE workflow, hard constraints, batch plan R01 to R08, and the
  definition of done. ch00 + ch01 revised as the exemplar (commit `895d19c`).
  Next batch: R01 (ch02 to ch06, plus the ch00 note backfill).

## Reference documents

- `REGISTER_PASS.md` — the operating instruction for the register pass.
- `COMPLETION.md` — whole-book completion report for the translation itself.
- `PROGRESS.md` — per-batch log, B01 through B13 (R-batches append here).
- `CHANGELOG.md` — dated record of corrections and revisions.

## Rebuilding from a clean checkout

`data/src`, `data/zh`, `out/*_en.txt`, and `out/*.epub` are gitignored. From a
fresh clone: `python3 scripts/ingest_epub.py source.epub` to rebuild `data/src`;
then, for each id ch00..ch35, `python3 scripts/split_bilingual.py
"out/<id>_bilingual.md" <id> "<zh title from book.json>"` to rebuild `data/zh`
and `out/<id>_reading.md`; then `python3 scripts/build_reading_epub.py
"out/On a Hair Trigger.epub"` and `python3 scripts/qa_epub.py
"out/On a Hair Trigger.epub"`.

## The single working branch

All work for this book lives on `claude/on-a-hair-trigger` (CLAUDE.md rule 2). A
session started on a per-batch branch folds its work onto `claude/on-a-hair-trigger`
and retires the stray branch, local and remote.
