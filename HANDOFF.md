# HANDOFF — Zhou Enlai: Commander of the Hidden Front

## Message to paste into the next chat

The book is COMPLETE; the REGISTER REVISION pass (`REVISION_PLAN.md`, five
batches R1-R5) is under way. **R1, R2 and R3 are DONE.** R1: Tier A globals (95
dates, Politburo cascade, ledger residuals) + the ch15 exemplar. R2: the
Tier-B tic sweep of the front batch ch00-ch08 (11 edits; ch00/ch03/ch05/ch08
clean). R3: the tic sweep of ch09-ch14 and ch17 + the full aligned read of ch16
(18 edits; ch10/ch12 clean; see PROGRESS.md / CHANGELOG.md). Where the plan and
this handoff disagree, the plan wins. Next is R4. The R4 kickoff:

```
Zhou Enlai R4 (revision)

Read CLAUDE.md, then REVISION_PLAN.md (it governs; where HANDOFF.md disagrees, the plan wins), then STYLE.md. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content FROZEN; edits only via edits/<id>_edits.md + scripts/apply_edits.py. Calibrate against the committed ch15 exemplar diff.

Do batch R4 = tic sweep of ch18-ch22 per REVISION_PLAN.md sections 3-5, including the spine test on ch19's five and ch21's two flagged long sentences. ch19-ch20 already carry the Politburo form from R1; do not re-decide it. Source consulted at every non-mechanical site; KEEP list respected (ch20-ch22 are dense with quoted testimony; abridgment ellipses and document register stay). If data/zh is missing, regenerate per scripts/recovery/README.md and verify_unit green before editing.

Per unit: apply, verify_unit, re-run register_tics.sh, defend survivors in PROGRESS.md, check_register vs out/ch01_reading.pre-R.md. Then rebuild, qa_epub (epubcheck if installed), 10% spot-audit (min 10), CHANGELOG, commit, push. Do not pause for approval. End with the rebuilt EPUB attached in chat AND the R5 kickoff from REVISION_PLAN.md section 9 pasted verbatim in a fenced block.
```

### R3 carry-forward for R4 (ch18-ch22)
- **Fresh container = regenerate data/zh first.** data/zh is untracked. R4's
  units: ch18 comes from `scripts/recovery/b10_rebuild.sh` (txt_backup_b10, with
  ch17); ch19-ch22 come from b11/b12 — run render + ocr_crop (recorded crop
  0.11/0.90/0.135/0.95, chi_sim psm6, running-head "隐蔽战线统帅周恩来") for the
  PDF ranges, then the b1N strip/assemble/surgery/apply_fixes per
  scripts/recovery/README.md and the b1N_rebuild.sh drivers where present, then
  `apply_fixes.py`, then **revert data/pagemap/** (assemble's auto-output is
  stale after surgery; the committed hand-built pagemaps are authoritative).
  `pgrep -c tesseract` must read 0 after every OCR run. ocr_dual NOT needed.
- **The regen recipe that worked in R3** (fresh container, tesseract 5.3.4):
  render the whole PDF span once, ocr_crop once with the recorded crop, then run
  each batch's strip -> assemble (per-unit, --offset 44) -> surgery --apply ->
  apply_fixes; b10-b14 have `b1N_rebuild.sh` drivers that do this from
  txt_backup. A stray "not found" from apply_fixes on a single char is benign
  tesseract-5.3.4 drift; verify_unit is the gate.
- **check_register ref:** always `out/ch01_reading.pre-R.md`.
- **Everything in R4's range is the tic sweep** (no full-read chapter; ch15/ch16
  were the two biography chapters and are done).
- **Calibration:** the ch15 exemplar diff (12 edits/75 paras) and R2/R3 edit
  lists are the restraint targets. Most flagged sites are LEFT; touch only
  genuine narration tics; quoted memoirs/documents/dialogue are KEEP. The
  KEEP-list guard is real: in R3 it caught "let slip not a moment" and
  "whereupon" sitting inside quotes — search the diff for over-corrections.
- **Defended-survivor conventions established R2-R3** (apply the same reasoning):
  "before long"/"Before long" (不久) = modern, keep; "could not help" (不禁) =
  idiomatic, keep; "no small risk/part/feat" = idiomatic collocation, keep, but
  "no few"/"no little" = calque, fix; 除...外 noun-phrase "besides" -> "apart
  from"; trailing 并/还 "besides" -> "as well"; sentence-initial or +gerund
  "besides" = modern, keep; "one after another" kept only for genuine sequence
  (连续/相继 where rhythm holds), else "in succession" (people) or recast for
  纷纷 (distributive); "and the others"/"and the rest" kept where a good form or
  a meaningful distinction (martyrs vs traitors), collapsed only on intra-
  chapter drift for one referent; narration "。……" ellipses cut per STYLE
  ruling 8, quotation-abridgment ellipses kept.
- **Pinned benign zh artifacts in/near range:** none new for ch18-ch22 recorded
  yet; if verify_unit flags a single number-pair that is zh-side OCR garble with
  the English correct, pin it in PROGRESS (do not "fix" the English).
- **Anchor discipline:** any prose edit that breaks a notes.json anchor carries
  its NOTE-ANCHOR pair in the same edit list; date/term edits can also break
  figures.json `before` anchors (builder refuses; fix figures.json by hand). In
  R3 no anchor was touched (notes.json byte-unchanged, 339).
- **For R5 (do not do in R4):** two book-wide diction-ledger residuals were
  observed and deliberately left for R5's whole-book cascade — 破坏 -> "wrecking"
  (ledger: sabotage) and 镇压/除掉 of traitors -> soft "put down"/"did away with"
  (killing-verb ledger: eliminate/kill). Fixing them piecemeal would drift.

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
