# HANDOFF — Zhou Enlai: Commander of the Hidden Front

## Message to paste into the next chat

The book is COMPLETE; the REGISTER REVISION pass (`REVISION_PLAN.md`, five
batches R1-R5) is under way. **R1, R2, R3 and R4 are DONE.** R1: Tier A globals
(95 dates, Politburo cascade, ledger residuals) + the ch15 exemplar. R2: the
Tier-B tic sweep of the front batch ch00-ch08 (11 edits). R3: the tic sweep of
ch09-ch14 and ch17 + the full aligned read of ch16 (18 edits). R4: the tic
sweep of the back batch ch18-ch22 (19 edits; ch22 clean; see PROGRESS.md /
CHANGELOG.md). Where the plan and this handoff disagree, the plan wins. Next is
R5, the final register batch. The R5 kickoff:

```
Zhou Enlai R5 (revision, final)

Read CLAUDE.md, then REVISION_PLAN.md (it governs; where HANDOFF.md disagrees, the plan wins), then STYLE.md. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content FROZEN; edits only via edits/<id>_edits.md + scripts/apply_edits.py. Calibrate against the committed ch15 exemplar diff.

Do batch R5 = tic sweep of ch23-ch27, then the pass-closing sweep, per REVISION_PLAN.md sections 3-5 and 7: the 叛徒 variety check (plan section 3.2; sample against source, collapse only if it is drift, record the verdict); whole-book register_tics.sh re-run with every surviving hit defended; check_reconcile.py; grep the full pass diff for KEEP-list over-corrections; fresh 15-paragraph spot audit drawn from edited paragraphs book-wide. If data/zh is missing, regenerate per scripts/recovery/README.md and verify_unit green before editing.

Close out: rebuild, qa_epub, epubcheck; update COMPLETION.md with a dated revision record (edit counts per tier, spot-audit result, the 叛徒 verdict); commit the final EPUB with git add -f out/zhou-enlai.epub; restore HANDOFF.md to its completion state with NO kickoff section (the pass is over; further work is corrections per CLAUDE.md); CHANGELOG; commit, push. Do not pause for approval. End with the final EPUB attached in chat and a closing summary; there is no next kickoff.
```

> **Commissioner request (2026-08-22), AFTER R5:** once the register pass closes,
> run a dedicated **footnote-density pass** — greatly increase footnote coverage
> across the whole book (people, places, events, offices, terms, allusions:
> everything a non-specialist Western reader would miss), without padding. This
> is a NEW initiative beyond the register plan (which had footnotes out of scope,
> section 6); the commissioner's instruction takes precedence. The plan and
> kickoff live in `FOOTNOTE_PASS.md` (its `## Kickoff` block is paste-ready).
> Do R5 first; then that pass.

### R4 carry-forward for R5 (ch23-ch27 + close-out)
- **Fresh container = regenerate data/zh first.** data/zh is untracked. R5's
  units ch23-ch27 come from `data/txt_backup_b13` and `_b14` via
  `scripts/recovery/b13_rebuild.sh` and `b14_rebuild.sh` (deterministic; they
  copy the backup into data/txt, then strip/assemble/surgery/apply_fixes/
  pagemap). No re-OCR, no render needed for b10-b14 units. `mkdir -p data/txt
  data/zh` first if absent. A stray apply_fixes "not found" on a single char is
  benign tesseract-5.3.4 drift; verify_unit is the gate. In R4 the b1N drivers
  regenerated data/pagemap byte-identical to the committed maps (no revert
  needed); check `git status data/pagemap` and revert only if it drifts.
- **All 28 units verify_unit green on R4's regen; ch18-ch22 had no benign
  number-pair artifacts** (unlike ch04/ch15/ch16). If R5's regen throws one,
  pin it in PROGRESS and do NOT touch the English.
- **check_register ref:** always `out/ch01_reading.pre-R.md`.
- **Calibration:** the ch15 exemplar diff (12 edits/75 paras) and the R2/R3/R4
  edit lists are the restraint targets. R4 was 19 edits across 316 paras; ch22
  came back clean. Touch only genuine narration tics; quoted
  memoirs/documents/dialogue are KEEP.
- **KEEP-list guard is real:** R4 caught three in-quote hits and left them
  ("could only work hard to repay" ch18 Zhang Shenchuan memoir; "Presently"
  ch19 Cai Mengjian testimony; "could only make contact by telephone" ch20 Chen
  Yangshan testimony). Search the diff for over-corrections every batch.
- **Defended-survivor conventions (R2-R4, apply the same reasoning):**
  "before long"/"Before long" (不久) = modern, keep; "could not help" (不禁) =
  idiomatic, keep; "no small risk/part/feat" = idiomatic collocation, keep, but
  "no few"/"no little" = calque, fix; 除...外 noun-phrase "besides" -> "apart
  from"; trailing 并/还/又/还有/此外 "besides" -> "as well"/"also"; sentence-
  initial or +gerund "besides" = modern, keep; "one after another" kept only for
  genuine sequence (连续/相继/接连 where rhythm holds), else "in succession"
  (people) or recast for 纷纷 (distributive); "and the others"/"and the rest"
  kept as genuine varying-membership truncations, collapsed only on intra-
  chapter drift for one fixed referent; 只好 -> "had no choice but to";
  后来 -> "then/later" not "at length"; 便 -> "then" not "thereupon";
  fronted-infinitive subjects de-inverted per STYLE calibrated ruling 1;
  narration ellipses cut per STYLE ruling 8, quotation-abridgment ellipses kept;
  spine-split ONLY genuine multi-spine run-ons, never a colon-plus-list.
- **叛徒 variety check (R5 core task):** traitor 240 / renegade 29 / turncoat
  11. Sample ~15 sites per variant against source; if the variation tracks
  distinct source words (叛徒/变节分子/叛逆) keep it as deliberate, else collapse
  to "traitor". Also do ch21's 等-tag arrestee-group alternation via
  check_reconcile.py's human read.
- **Book-wide diction-ledger residuals for R5's whole-book cascade (do NOT do
  piecemeal):** 破坏 -> "wrecking" (ledger: **sabotage**), e.g. ch21:5,
  ch20:67; and 镇压/除掉 of traitors -> soft "put down"/"did away with"
  (killing-verb ledger: **eliminate/kill**). Grep-and-cascade across ALL built
  units, then rebuild.
- **Anchor discipline:** any prose edit that breaks a notes.json anchor carries
  its NOTE-ANCHOR pair in the same edit list. In R4 no anchor was touched
  (notes.json byte-unchanged, 339).

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
