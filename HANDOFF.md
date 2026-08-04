# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

## Message to paste into the next chat

```
Hair Trigger R06

Read CLAUDE.md, then REGISTER_PASS.md (in full; it is the operating
instruction for this pass), then HANDOFF.md, then book.json. The translation
is complete (B01 to B13); this is the REGISTER PASS: a style-only revision of
the English, per the commissioner's readability feedback. ch00 and ch01 are
the revised exemplar; R01 (ch02 to ch06, plus the ch00 note backfill), R02
(ch07 to ch11), R03 (ch12 to ch15), R04 (ch16 to ch19), and R05 (ch20 to ch23)
are done and committed. Study `git show 895d19c` and the R01 to R05 edit lists
in edits/ before starting.

The pass has TWO workstreams, run together: (1) the style revision, and
(2) footnote densification to the new policy (REGISTER_PASS.md, "The
annotation gap"): the reader is a Westerner with no background in Chinese
history, family structure, or custom; anything such a reader would miss earns
a note at first occurrence, roughly 8 to 15 per chapter, coverage-driven and
never padded (check notes.json across ALL units for earlier coverage first;
recurring subjects are noted once, at first appearance in the book). By ch24
the book's cultural furniture is largely already covered, so expect the new
notes per chapter to run low and be coverage-driven, not forced to a quota.

Do batch R06 = ch24, ch25, ch26, ch27, end to end. ANALYZE each chapter
against the source in out/<id>_bilingual.md and commit the edit lists to
edits/<id>_edits.md in the format REGISTER_PASS.md specifies (TOUCH/RECAST
blocks, NOTE-ANCHOR items, NOTE-ADD blocks), then EXECUTE them exactly
(exact-match replacement, count == 1, via Python; a stamp line that recurs is
one count == N replace). Style only: never touch a source line, never merge or
split paragraphs, nothing invented, nothing dropped, names per glossary.json,
note anchors kept in step with notes.json, new-note anchors verified as
verbatim substrings BEFORE building. Triage conservatively: these are ordinary
chapters like ch01, so most paragraphs LEAVE; do not churn prose that already
reads well. Set the source's bare place/time/transition stamps as italic scene
cards (T2). Watch the source oddities that are already footnoted and must stay
(the Tang Shaoli/Shaoqi slip, the Yang Muci/Muchu twin-name misprints, the
Ronghua/Huamei bookstore inconsistency). After editing: regenerate with
split_bilingual.py, run check_structure --pairs and check_numbers --noise
per chapter (noise.txt's B09 block already covers ch22-ch24; extend it only if
a new non-quantity numeral is flagged), run the straight-quote typography
guard, rebuild "out/On a Hair Trigger.epub", run qa_epub.py until green.
Spot-audit 10% of edited paragraphs (minimum 10) against the source for
meaning drift. Record everything in PROGRESS.md, append a dated CHANGELOG.md
entry, rewrite HANDOFF.md's kickoff for R07 (ch28 to ch31), commit and push to
claude/on-a-hair-trigger (the ONLY branch). Do not pause for approval
mid-batch. Deliver the rebuilt EPUB in chat, and end the reply with the R07
kickoff verbatim in a fenced block.
```

## State of the project

- Translation COMPLETE: B01 to B13 done, all 36 units (ch00 to ch35)
  translated, glossary 273 entries, EPUB `out/On a Hair Trigger.epub` with full
  TOC, qa green book-wide.
- Typography normalized book-wide (uniform curly quotes, apostrophes,
  ellipses); a straight quote in prose is a regression (guard: `grep -n
  "[\"']" out/<id>_reading.md` must print nothing).
- REGISTER PASS in progress. `REGISTER_PASS.md` defines the whole pass:
  taxonomy, triage, two-phase ANALYZE/EXECUTE workflow, hard constraints, batch
  plan R01 to R08, and the definition of done. ch00 + ch01 are the exemplar
  (commit 895d19c).
  - R01 (ch02 to ch06, plus the ch00 note backfill) is DONE: 6 prose touches,
    20 notes added.
  - R02 (ch07 to ch11) is DONE: 3 prose touches, 21 notes added.
  - R03 (ch12 to ch15) is DONE: 1 prose touch, 21 notes added.
  - R04 (ch16 to ch19) is DONE: 15 prose touches (ch16 T4 scare-quote
    de-cluttering), 15 notes added.
  - R05 (ch20 to ch23) is DONE: 14 prose touches (13 T2 scene cards + 1 T3
    image), 7 notes added. Book-wide notes now 213.
  - Next batch: R06 (ch24 to ch27).
- Batch plan (REGISTER_PASS.md): R06 ch24-ch27, R07 ch28-ch31, R08 ch32-ch35.

## Reference documents

- `REGISTER_PASS.md` — the operating instruction for the register pass.
- `edits/` — committed per-chapter edit lists (ch00, ch02 to ch23 so far).
- `COMPLETION.md` — whole-book completion report for the translation itself.
- `PROGRESS.md` — per-batch log, B01 through B13 and R01 through R05 (R-batches append here).
- `CHANGELOG.md` — dated record of corrections and revisions (newest first).

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
