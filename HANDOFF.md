# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

## THE BOOK IS COMPLETE; a REVISION PASS is now IN PROGRESS

All 12 units are translated, annotated, built, and verified (COMPLETION.md is
the report). A post-completion register/style/apparatus pass (REVISION_PLAN.md)
is now running, scope **TIER 1+2** (tier 3 declined). Done so far: **R0**
(read-only calibration), **R1** (STYLE.local rebaseline rules + the ch02
exemplar, 26 prose edits + 4 note-date reformats), **R2** (sweep ch01, ch03,
ch04: 23 prose edits + 2 anchor moves + 18 note-date reformats), and **R3**
(sweep ch05-ch11 + apparatus: 7 prose edits + 1 anchor move on ch05, ch06-ch11
zero edits, 1 glossary date reformat, Principal Characters grown 3 -> 18, the
translator's-note author-voice sentence; see PROGRESS.md). The chapter sweep is
COMPLETE. Next and last: **R-final** (whole-book regression + reconcile sweep +
register table + CHANGELOG + COMPLETION addendum + final EPUB commit).

## Message to paste into the next chat

```
Chen Yangshan REVISION R-final (whole-book regression + close)

Read: CLAUDE.md, REVISION_PLAN.md (self-contained; never read or pull from any
other branch), STYLE.local.md, PROGRESS.md. All work on claude/chen-yangshan;
never read other branches. Scope: TIER 1+2 (the whole pass). The chapter sweep
is done (R1 ch02, R2 ch01/ch03/ch04, R3 ch05 + the ch06-ch11 zero-edit walk +
apparatus); this batch does NOT edit prose, it regresses and closes.

Re-run the full battery across the spine per plan sec.2 and sec.8:
  - structure/apparatus: check_apparatus clean; the builder's anchor-refusal
    backstop passes on a clean build.
  - build + QA: build_reading_epub.py; qa_epub.py PASS; epubcheck
    /tmp/epubcheck-5.1.0/epubcheck.jar out/Chen Yangshan - Hero of the Secret War.epub = 0/0/0. Keep the
    EPUB under 30 MiB (MAX_FIG_WIDTH=1000 must hold; it is ~12.2 MiB now after the R3 JPEG re-encode).
  - reconcile sweep: check_reconcile.py for cross-chapter drift (repeated
    compounds with >1 English rendering, every glossary en form used, one
    spelling locale). NOTE a known metadata locale slip to resolve or record:
    the translator's note / source_note in book.json use British spelling
    ("honour", "organisations") while the body is American; decide one locale
    and either fix or record it in COMPLETION.
  - register table across the spine: check_register.py each unit --ref
    out/ch01_reading.md (ch01 is the frozen reference; tier 3 was declined, so
    it was NOT re-frozen).
  - typography regression: no curly quote / ellipsis char in out/*_reading.md
    EXCEPT the 4 PRE-EXISTING curly chars on ch01 lines 23/46/123 (flagged in
    R2, present in HEAD, out of the mechanical scope) -- decide fix-or-keep.
  - whole-revision KEEP-list sweep: obituary, {v} blocks, precepts, verse,
    partisan register, decided renderings all untouched across R1-R3.

Then close: dated CHANGELOG.md entry; COMPLETION.md addendum recording the pass
and final counts (12 units swept, edit totals per batch, 18 principals, dates
normalized, translator-note sentence); commit the final EPUB
(git add -f out/Chen Yangshan - Hero of the Secret War.epub); push. Deliver the EPUB and the addendum in
chat. HANDOFF.md returns to "COMPLETE; further work is a corrections pass." Do
not pause for approval mid-batch.
```

## Revision-pass provenance (do not violate)

`REVISION_PLAN.md` is the operating document and it is SELF-CONTAINED: every
imported rule is reproduced there in full. **Do NOT fetch, read, or pull
anything from `claude/the-sword-roars` or any other branch; all work stays on
`claude/chen-yangshan`.** Where this file and the plan disagree, the plan wins.

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
- **Deliverable:** `out/Chen Yangshan - Hero of the Secret War.epub` (committed with `git add -f`).
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
- Builder figure encoder `emit_figure`: greyscale + cap at MAX_FIG_WIDTH,
  then write each figure as whichever of PNG or JPEG (q90) is smaller (JPEG for
  photos, PNG for line art). Cut the EPUB 28.6 -> 12.2 MiB with no visible loss;
  do not revert to PNG-only. figures.json keeps .png source names; emitted names
  (often .jpg) are a build-time detail.
- `apparatus_merge` merges glossary rows into sections; **REPLACES a unit's
  figures wholesale** — for a chapter split across batches, always re-include the
  prior batch's figures or they are dropped silently (this bit ch02; recovered in
  B10). `data/zh` is gitignored and regenerated per unit; run per-unit checks with
  the scoped `data/check_config.<id>.json`.

## Environment notes for a future rebuild

- `./setup.sh` once; epubcheck at `/tmp/epubcheck-5.1.0/epubcheck.jar` (setup
  re-fetches on a fresh container). `OMP_THREAD_LIMIT=1` for tesseract.
- Rebuild: `python3 scripts/build_reading_epub.py`, `python3 scripts/qa_epub.py`,
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/Chen Yangshan - Hero of the Secret War.epub`.
- The setup.sh regression "hook stands down on template stub: FAIL" is benign
  (the fixture expects a placeholder HANDOFF; this one is a real/complete handoff).
