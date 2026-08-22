# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

## THE BOOK IS COMPLETE; a REVISION PASS is now IN PROGRESS

All 12 units are translated, annotated, built, and verified (COMPLETION.md is
the report). A post-completion register/style/apparatus pass (REVISION_PLAN.md)
is now running, scope **TIER 1+2** (tier 3 declined). Done so far: **R0**
(read-only calibration) and **R1** (STYLE.local rebaseline rules + the ch02
exemplar, 26 prose edits + 4 note-date reformats; see PROGRESS.md). The ch02
diff is the calibration target. Next: **R2** (sweep ch01, ch03, ch04).

## Message to paste into the next chat

```
Chen Yangshan REVISION R2 (sweep ch01, ch03, ch04)

Read: CLAUDE.md, REVISION_PLAN.md (self-contained; never read or pull from any
other branch), STYLE.local.md (now carries the approved TIER 1+2 rebaseline
rules), PROGRESS.md (the R1 ch02 exemplar diff is the calibration target). All
work on claude/chen-yangshan. Approved scope: TIER 1+2 ONLY.

Sweep ch01, ch03, ch04 end to end per plan sec.5 with the sec.2 verification,
honouring the sec.3.3 KEEP list, at the ch02 touch-rate (most paragraphs LEAVE;
a rewrite that only shuffles synonyms is itself a defect). Apply the STYLE.local
rebaseline rules: Politburo (ch03 has 1 body hit); White Terror; date reformats
in these chapters' note bodies (json load/dump, ensure_ascii=False -- apply_edits
cannot touch a note body); litotes calques; the could-not-help formula (ch03:98);
"Such was" at ch04:109 and ch04:151 (recast ONLY if the read-aloud test fails,
else leave); the inversion at ch03:88; 等-tags (vary, no tag dominating, not
zero); one-after-another; the awkward "the X-ing of" nominalizations (leave the
idiomatic ones); doubled synonyms. Edits via edits/<id>_edits.md + apply_edits.py,
OLD occurring exactly once. R1 LESSON: before applying, check every edit's OLD
against BOTH notes.json anchors AND figures.json `before` anchors, and ship a
NOTE-ANCHOR pair for any note anchor an edit breaks; never restructure anchored
text for a mere tic. Verify per plan sec.2: git diff --stat shows NO net line
change on mechanical chapters, grep the edit lists for digits (no numeral may
change), typography guard (no curly quotes/ellipsis introduced), check_apparatus
clean, and let the builder's anchor refusal backstop it. Spot-audit 10% (min 10)
of edited paragraphs; KEEP-list diff sweep. Rebuild (build_reading_epub.py),
qa_epub.py, epubcheck 0/0/0, commit, push. Deliver the EPUB in chat and paste
the R3 kickoff (R3 = ch05-ch11 + the apparatus mechanics of plan sec.6:
Principal Characters growth, the translator's-note sentence, and the remaining
chapters' note-date reformats). Do not pause for approval mid-batch.
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
