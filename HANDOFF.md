# HANDOFF — Zhou Enlai: Commander of the Hidden Front

## Message to paste into the next chat

The book is COMPLETE; the REGISTER REVISION pass (`REVISION_PLAN.md`, five
batches R1-R5) is under way. **R1 is DONE** (Tier A globals: 95 dates
normalized, Politburo cascaded, ledger residuals fixed; ch15 exemplar applied
as the calibration target; build/qa/epubcheck clean; see PROGRESS.md and
CHANGELOG.md). Where the plan and this handoff disagree, the plan wins. Next is
R2. The R2 kickoff:

```
Zhou Enlai R2 (revision)

Read CLAUDE.md, then REVISION_PLAN.md (it governs; where HANDOFF.md disagrees, the plan wins), then STYLE.md. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content FROZEN; edits only via edits/<id>_edits.md + scripts/apply_edits.py. Before editing, read the committed R1 exemplar diff for ch15: every edit list in this batch must match its restraint.

Do batch R2 = tic sweep of ch00-ch08 per REVISION_PLAN.md sections 3-5: register_tics.sh plus the section 3.2 greps per unit, source consulted at every non-mechanical site, LEAVE/TOUCH/RECAST verdicts, spine test on the flagged long sentences, KEEP list respected (quoted documents and memoirs untouched). ch01 carries 28 note anchors; pair every broken anchor in the same edit list, and run check_register against out/ch01_reading.pre-R.md. If data/zh is missing (fresh container), regenerate per scripts/recovery/README.md and verify_unit green before editing.

Per unit: apply, verify_unit, re-run tics, defend survivors in PROGRESS.md. Then rebuild, qa_epub (epubcheck if installed), 10% spot-audit (min 10), CHANGELOG, commit, push. Do not pause for approval. End with the rebuilt EPUB attached in chat AND the R3 kickoff from REVISION_PLAN.md section 9 pasted verbatim in a fenced block.
```

### R1 carry-forward for R2 (ch00-ch08)
- **data/zh parity limits (pinned, plan section 2):** ch01 (zh 32 vs en 38, 6
  OCR welds; §3 ambiguous, not force-split) and ch03 (zh 38 vs en 37, p83
  photo displacement) are NOT reproducible under this container's tesseract
  5.3.4. ch00 and ch02 were recovered (b01_surgery.py; b02_surgery.py made
  skip-and-warn). For ch01/ch03 use the zh-independent guard set (apply_edits +
  notes.json anchor grep + builder anchor refusal + direct number/typography
  grep + check_register). ch04 has one benign zh number artifact (pair 37).
- **check_register ref:** always `out/ch01_reading.pre-R.md` (ch01 is being
  edited; do not use its live state as the ref).
- **Already edited in R1 within the ch00-ch08 range** (do not re-do): all dates
  in ch00-ch05; Politburo in ch00,ch01,ch02,ch04; "in good time" in ch03,ch04,
  ch07; ch07 "driving into"->"planted inside". R2 is the TIER B tic sweep on
  top of these.
- **Anchor discipline lesson from R1:** date/term edits can break BOTH
  notes.json anchors (handle via NOTE-ANCHOR in the edit list) AND figures.json
  `before` anchors (the builder refuses; fix figures.json by hand). Check both.

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
