# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

## The book is COMPLETE. There is no next batch.

All thirteen batches are done. The Prologue and all 35 chapters (36 units,
ch00 to ch35) are translated, annotated, and built into the cumulative EPUB
`out/On a Hair Trigger.epub`, with a full hyperlinked table of contents, 114
footnotes, a glossary of 273 entries, and the Translator's Note. Every check is
green book-wide (verbatim parity zero diffs; `check_structure` parity OK and
`check_numbers` 0 unresolved on all 36 units; `qa_epub.py` PASS, 114 references =
114 bodies = 114 backlinks).

Because this was the last batch, a completion report was written INSTEAD of a new
kickoff message. See:

- `COMPLETION.md` — the whole-book completion report (what was produced, the
  checks run book-wide and their results, known anachronisms and annotations,
  and rebuild-from-clean-checkout instructions).
- `PROGRESS.md` — the per-batch log, B01 through B13.
- `CHANGELOG.md` — dated record; corrections go here going forward.

## If the commissioner files corrections

Read `CLAUDE.md` "Corrections workflow." In brief: GLOBAL corrections (a
rendering, a register rule, a note policy) cascade via a glossary/style change
plus a grep-driven edit across ALL built units, then a rebuild and full QA; LOCAL
corrections are a single-spot fix. After any corrections batch: rebuild
`out/On a Hair Trigger.epub`, run `qa_epub.py` until green, list every file
touched, and append a dated entry to `CHANGELOG.md`. Deliver the rebuilt EPUB in
chat.

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
