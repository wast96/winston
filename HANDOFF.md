# HANDOFF — Zhou Enlai: Commander of the Hidden Front

## Message to paste into the next chat

The book is COMPLETE (see below); what follows next is the REGISTER REVISION
pass planned in `REVISION_PLAN.md` (2026-08-22, five batches R1-R5). Where
that plan and this handoff disagree, the plan wins. The R1 kickoff:

```
Zhou Enlai R1 (revision)

Read CLAUDE.md, then REVISION_PLAN.md (it governs this pass; where HANDOFF.md disagrees, the plan wins), then STYLE.md and review/REGISTER_PASS_ASSESSMENT.md. All work on branch claude/zhou-enlai only; if the session starts on a stray branch, fold it per CLAUDE.md rule 2. Content is FROZEN: English-surface edits at flagged sites only, no paragraph merged or split, no facts or hedges changed, edits only via edits/<id>_edits.md + scripts/apply_edits.py.

Do batch R1 end to end per REVISION_PLAN.md section 7: (a) setup.sh; regenerate data/zh for all 28 units per scripts/recovery/README.md and replay apply_fixes.py; verify_unit green on ALL units before any edit; pin known-benign warnings in the plan's section 2; snapshot out/ch01_reading.pre-R.md; (b) Tier A globals: normalize the 95 day-month dates to month-day, cascade the Politburo decision (plan section 3.2; default "the Politburo", record in glossary.json and authority.json), fix the "in good time" and "driving into" ledger residuals; (c) the ch15 exemplar: full tic sweep plus aligned zh-en read plus spine test, per plan sections 3-5; (d) rebuild, qa_epub, epubcheck, 10% spot-audit, PROGRESS and CHANGELOG entries, commit, push.

Do not pause for approval mid-batch. Cite printed folios in any new note text. Never invent bridging text. End the batch with the rebuilt EPUB attached in chat AND the R2 kickoff from REVISION_PLAN.md section 9 pasted verbatim in a fenced block.
```

## THE BOOK IS COMPLETE

All 28 units are translated (ch00 Preface through ch27 Afterword). B14, the
final batch, is done: ch25 (the Wu Hao Notice affair), ch26 (Conclusion), and
ch27 (Afterword), plus the whole-book completion tail. There is no next batch,
so this file no longer carries a paste-ready kickoff. The full completion
report is `COMPLETION.md`; read that first.

Further work on this book is a CORRECTIONS pass, not new translation. Follow
the corrections workflow in `CLAUDE.md`: the commissioner files items in
`CORRECTIONS.md` (or pastes them in chat, and you transcribe them there
first), global corrections cascade across all built units plus the note and
glossary bodies, then rebuild and full QA; a zero-item corrections pass is
still a clean-checkout regression run.

## Final state

- Deliverable: `out/zhou-enlai.epub`, committed with `git add -f` on branch
  `claude/zhou-enlai`. 28/28 chapters, 339 notes, 36 figures, 496 pagebreaks.
- `qa_epub.py`: PASS (all links resolve). `epubcheck` 5.1.0: 0 errors, 0 warnings.
- Ledgers current: `glossary.json` (847 rows), `notes.json`, `figures.json`,
  `book.json`; `authority.json` fed with this book's decided renderings;
  `out/term_ledger.md` and `out/deep_audit.md` written; `CHANGELOG.md` and
  `PROGRESS.md` current.

## Do not revert (accumulated tooling)

- `data/ocr_fixes.json`: crop/context-verified readings for ch00&#8211;ch27;
  replay with `apply_fixes.py` on any fresh regen.
- `scripts/recovery/`: the b02_* through **b14_*** strip/surgery/pagemap/
  addfixes/glossary scripts and the `b1X_rebuild.sh` drivers. The b14_* set
  rebuilds ch25&#8211;ch27 from `data/txt_backup_b14`.
- `data/noise.txt`: keep extending, never prune. B14 added 数万万, 亿万,
  千百倍, 日理万机, 万劫, 一百两, 伍豪二字.
- `data/check_config.json`: docs + sources for ch00&#8211;ch27.
- Builder invariants (full pending-aware then cleaned TOC; note pop-ups with
  endnotes fallback; refusal to build on an unmatched anchor or unplaced
  figure; byte-identical cover copy; render-layer smart quotes).

## How to rebuild from a clean checkout

1. `./setup.sh`
2. regenerate `data/zh/` with the `scripts/recovery/b*_rebuild.sh` drivers
   (raw-OCR backups are under `data/txt_backup_b*`).
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
