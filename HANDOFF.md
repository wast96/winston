# HANDOFF -- China's Secret War (中国秘密战)

## Message to paste into the next chat

```
China's Secret War R04 (register pass, final)

Read CLAUDE.md, then HANDOFF.md, then REVISION_PLAN.md, then STYLE.md and
STYLE.local.md. Run ./setup.sh. Branch claude/chinas-secret-war only.

Do revision batch R04 = ch10 + ch11 + ch12 + ch13 per REVISION_PLAN.md §5
(read the R01 diff first), THEN the closing sweep per §7: apparatus checks
(§6), whole-book tic regression, check_register table, epubcheck, CHANGELOG
entry, COMPLETION.md addendum, and rewrite HANDOFF.md to post-pass state
(remove the kickoff section so the Stop hook stands down). Content frozen;
anchor_check before every apply; blind critique per unit; one commit per
unit. Deliver the final EPUB in chat with a summary of the whole pass
(edits per unit, classes, anything left for a corrections pass).
```

## R03 DONE (register pass, batch 3 of 4) — 2026-08-22

R03 = ch06 + ch07 + ch08 complete, one commit per unit, all pushed to
claude/chinas-secret-war (35/36/50 edits). These were the three heaviest
question-mark units; the docent questions were converted and the genuine ones
kept (free-indirect reveals, investigative and interior questions, section
cliffhangers, ventriloquized/quoted cries, the chapter-frame hooks). ch08's
five ungrammatical "How to X?" problem-headers were made grammatical rather
than flattened. Content frozen; R01's diff stayed the exemplar and the
restraint held (most paragraphs LEFT). Authorial reveal-bangs rationed
(ch07 11 exclamations to 3, ch08 to 0). epubcheck 0/0/0/0 at batch end;
check_register within tolerance. See PROGRESS.md "R03" for the full exit
checklist and the items logged for the corrections/R04 sweeps.

ONE-OFF CORRECTION MADE IN R03 (not register work): two OCR-corrupt hanzi in
the ch07 note on "the Anti-Traitor Department" were fixed in notes.json,
锂奶/汉奇 -> 除奸/汉奸 (the note's own romanizations chujian/hanjian confirm
the intended characters). Meaning unchanged; logged here so R04's apparatus
sweep does not re-flag it. Next: R04, the FINAL batch (kickoff above), which
also runs the whole-book closing sweep per REVISION_PLAN §7.

## R02 DONE (register pass, batch 2 of 4) — 2026-08-22

R02 = ch02 + ch03 + ch04 + ch05 complete, one commit per unit, all pushed to
claude/chinas-secret-war (34/19/19/26 edits). Content frozen; R01's diff was
the exemplar and the restraint held (most paragraphs LEFT). epubcheck 0/0/0/0
at batch end. See PROGRESS.md "R02" entry for the full exit checklist and the
items logged for the corrections/R04 sweeps. Next: R03 (kickoff above).

TRAP CONFIRMED IN R02 (for R03-R04): a FIGURE 'before' anchor can be LONGER
than an edit's OLD line, so `anchor_check.py` (which tests anchor-in-OLD) will
NOT flag it; the builder's refusal (exit 2, "BUILD FAILED: N figure(s) never
placed") is the real backstop. Trust the build's own exit code, never a piped
grep's. When it fires, update the figure's `before` in figures.json in the
SAME commit (as done for ch05 p0208-f1).

## R01 DONE (register pass, batch 1 of 4) — 2026-08-22

R01 = ch00 + ch01 + ch09 complete, one commit per unit, all pushed to
claude/chinas-secret-war. The REVISED out/ch01_reading.md is now the register
reference for R02-R04. R01's committed diff is the exemplar: most paragraphs
LEFT untouched; the edits are surgical and content-frozen. See PROGRESS.md
"R01" entry for the exit checklist.

## A VOICE/REGISTER REVISION PASS IS PLANNED (not yet started)

The commissioner ordered a whole-book voice/register pass (2026-08-22),
adapting the shelf's register-rebaseline learnings. Everything a session
needs is ON THIS BRANCH: the plan and batch kickoffs are `REVISION_PLAN.md`;
the target register is `STYLE.local.md` ("THE REGISTER REBASELINE"); the
composed contract is `STYLE.md` (build artifact of the new `styles/` layers;
never hand-edit); the machinery is `scripts/` (voice_gate_critique,
register_tics, anchor_check, apply_edits, compose_style,
check_style_freshness) and `review/PROTOCOL.md`. Four batches, R01-R04, one
conversation each; the R01 kickoff is above. Until R04 completes, the
shipped EPUB remains the pre-pass build.

Do not revert: the composable style system (styles/, composed STYLE.md,
STYLE.local.md ledger), book.json `genre: nonfiction`, the ported
tests/run_tests.py hook-test fix, and the figures-pass items listed further
down.

## THE BOOK IS COMPLETE

All 14 units are translated, built, and QA-clean: the Preface (ch00),
Chapters 1 through 12 (ch01-ch12), and the Afterword (ch13). There is no next
batch. The completion report is `COMPLETION.md`; read it first. This file no
longer carries a next-batch kickoff, by design (the last batch replaces the
kickoff with the completion notice; the Stop hook stands down when the kickoff
section is gone).

**Figures added (2026-08-21).** The illustrated edition's images, deferred
through every translation batch, are now all in the EPUB: 182 inline figures
across ch01–ch12, a 36-plate front-matter "Photographs" gallery (PDF 5–18 +
author photo), and the real scanned cover. figures.json (+ `_plates`) drives
them; crops live in `data/figs/*.png` (now tracked); the builder gained a
gallery page and JPEG figure output. qa_epub PASS, epubcheck clean, ~15 MB.
Do not revert: `data/figs/` un-ignored; `esc_attr` for the `alt` attribute;
`render_gallery`; `MAX_FIG_WIDTH=900` + JPEG figures. See CHANGELOG.

Further work on this book is a CORRECTIONS PASS, not a new batch. The
commissioner reads the EPUB and files corrections in `CORRECTIONS.md` (or
pastes them in chat, to be transcribed there). Global corrections cascade via a
glossary/style change plus a grep across all built units including note and
glossary bodies, then rebuild and full QA; local corrections are a fix at one
spot. A corrections pass with zero items is still a clean-checkout regression
run: re-clone, replay the resegment scripts, rebuild, re-verify, prune stray
branches.

## What is DONE

- **Survey (Step 0a + 0b), approved.** book.json carries full metadata and the
  complete structure (12 chapters + Preface + Afterword).
- **B01 = Preface + Chapter 1** (frozen voice reference; voice gate passed).
- **B02-B03 = Chapter 2.** **B04-B12 = Chapters 3 through 11**, one chapter per
  batch, each with its Principal Sources.
- **B13 = Chapter 12 (明暗易位) + the Afterword (后记) + whole-book completion.**
  14/14 units; 3,285 English body paragraphs; 251 notes; 284 glossary rows
  (187 attested, 91 decided, 6 provisional). qa_epub PASS; epubcheck 0/0/0/0.
  The final EPUB is committed (`git add -f out/chinas_secret_war.epub`).

## Deliverables on disk

- `out/chinas_secret_war.epub` -- the finished annotated edition (committed).
- `out/<id>_reading.md` per unit -- the correction surface (one paragraph per
  true source paragraph).
- `out/term_ledger.md` -- the auditable term ledger (284 rows).
- `out/deep_audit.md` -- the random-sample deep audit and honest error rate.
- `notes.json`, `glossary.json`, `figures.json` (empty by decision), `book.json`
  -- current. `authority.json` fed with this book's renderings under the slug
  `chinas-secret-war`.
- `COMPLETION.md`, `PROGRESS.md`, `CHANGELOG.md` -- current.

## Tooling in place (do NOT revert)

- **Per-parity OCR crop** (scripts/ocr_crop.py): recto/odd [0.07, 0.86],
  verso/even [0.17, 0.94], top 0.045, bottom 0.93, chi_sim psm 6. Do NOT
  re-measure. scripts/ocr_dual.py is the PaddleOCR substitute.
- **scripts/resegment_ch04.py ... resegment_ch13.py**: rebuild data/zh/chNN.txt
  and data/pagemap/chNN.json from a hardcoded, hand-verified item list read off
  the scan. resegment ch02/ch03 are in-place editors (need OCR inputs);
  ch00/ch01 have none. Run resegment AFTER assemble (assemble overwrites zh).
- **scripts/crop_band.py**: magnified horizontal-band crop for dense rosters /
  faded spans (used for the ch12 "Hundred-and-Eight" roster).
- **scripts/render_ledger.py**, **scripts/feed_authority.py**: the completion
  tools (term ledger; authority feedback).
- **data/noise.txt**: the number-check noise rules; extend longest-first with a
  commented literal for numerals inside names/places/idioms/designations. Never
  noise a real quantity; carry it (in digits where load-bearing).
- **Builder invariants**: flat-glossary renderer; the chapter-title H1 is not
  anchorable (chapter-concept notes sit on a body phrase); note bodies are XHTML
  with numeric character references only; the builder refuses an unmatched
  anchor or unplaced figure spec.

## Open items for a corrections pass (none block completion)

- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; the standing question (every photo / a curated subset / none) is the
  one open editorial choice, and it is the commissioner's.
- **ch01 zh parity** 269/299 (from B01) and **ch03 folio markers** (none) are
  the two known housekeeping gaps; neither touches a footnote or the reading
  text.
- Frozen voice reference remains `out/ch01_reading.md` for any register work.

## Environment

- `./setup.sh` once per session. `OMP_THREAD_LIMIT=1` mandatory for tesseract;
  kill the process GROUP, confirm `pgrep -c tesseract` reads 0. epubcheck at
  `/tmp/epubcheck-5.1.0/epubcheck.jar`. The setup regression test "hook stands
  down on template stub" fails benignly. PaddleOCR absent (expected).
- Rebuild from a clean checkout: `./setup.sh`; replay the resegment scripts;
  `python3 scripts/build_reading_epub.py`; `python3 scripts/qa_epub.py`;
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub`.
- Work on branch `claude/chinas-secret-war` only (CLAUDE.md rule 2); expect a
  stray per-task branch at session start and consolidate onto the canonical
  branch.
