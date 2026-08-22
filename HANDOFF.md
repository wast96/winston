# HANDOFF — Zhou Enlai: Commander of the Hidden Front

## Message to paste into the next chat

The book is COMPLETE; the REGISTER REVISION pass (`REVISION_PLAN.md`, five
batches R1-R5) is under way. **R1 and R2 are DONE.** R1: Tier A globals (95
dates, Politburo cascade, ledger residuals) + the ch15 exemplar. R2: the
Tier-B tic sweep of the front batch ch00-ch08 (11 English-surface edits;
ch00/ch03/ch05/ch08 came back clean; see PROGRESS.md / CHANGELOG.md). Where the
plan and this handoff disagree, the plan wins. Next is R3. The R3 kickoff:

```
Zhou Enlai R3 (revision)

Read CLAUDE.md, then REVISION_PLAN.md (it governs; where HANDOFF.md disagrees, the plan wins), then STYLE.md. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content FROZEN; edits only via edits/<id>_edits.md + scripts/apply_edits.py. Calibrate against the committed ch15 exemplar diff before writing the first edit list.

Do batch R3 = tic sweep of ch09-ch14 and ch17, plus the FULL treatment of ch16 (aligned zh-en read like ch15; it is the other elevated-antique biography chapter), per REVISION_PLAN.md sections 3-5. Source consulted at every non-mechanical site; KEEP list respected. If data/zh is missing, regenerate per scripts/recovery/README.md and verify_unit green before editing.

Per unit: apply, verify_unit, re-run register_tics.sh, defend survivors in PROGRESS.md, check_register vs out/ch01_reading.pre-R.md. Then rebuild, qa_epub (epubcheck if installed), 10% spot-audit (min 10), CHANGELOG, commit, push. Do not pause for approval. End with the rebuilt EPUB attached in chat AND the R4 kickoff from REVISION_PLAN.md section 9 pasted verbatim in a fenced block.
```

### R2 carry-forward for R3 (ch09-ch14, ch16, ch17)
- **Fresh container = regenerate data/zh first.** data/zh is untracked; R3's
  units come from recovery batches b06-b09 (ch09-ch16) and b10 (ch17). Run
  render + ocr_crop (recorded crop, chi_sim psm6) for the PDF ranges, then the
  b0N strip/assemble/surgery/apply_fixes per scripts/recovery/README.md, then
  verify_unit. ocr_dual is NOT needed (QC scaffold only; content frozen). After
  assemble, **revert data/pagemap/** — assemble's auto-output is stale after
  surgery and the committed hand-built pagemaps are authoritative.
- **check_register ref:** always `out/ch01_reading.pre-R.md`.
- **ch16 gets the FULL treatment** (aligned zh-en read, like ch15) — it is the
  other elevated-antique biography chapter. Everything else is the tic sweep.
- **Pinned benign zh artifact in range:** ch16 pair 2 `[0,5,6,7,8]` (OCR-garbled
  龙华兵工厂/1865). When an edited unit's verify_unit shows only its pinned
  artifact, it is clean.
- **Already edited in R1 within R3's range** (do not re-do): "in good time" in
  ch09 x3, ch11, ch12, ch16, ch17; any date/Politburo cascades. R3 is the TIER
  B tic sweep on top.
- **Calibration:** the ch15 exemplar diff (12 edits / 75 paras) and R2's edit
  lists (edits/ch0{1,2,4,6,7}_edits.md) are the restraint targets. Most flagged
  sites are LEFT; touch only genuine narration tics; quoted memoirs/documents
  are KEEP.
- **Anchor discipline:** any prose edit that breaks a notes.json anchor carries
  its NOTE-ANCHOR pair in the same edit list; date/term edits can also break
  figures.json `before` anchors (builder refuses; fix figures.json by hand).

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
