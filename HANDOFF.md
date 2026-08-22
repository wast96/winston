# HANDOFF -- China's Secret War (中国秘密战)

## THE BOOK IS COMPLETE, AND THE VOICE/REGISTER PASS IS COMPLETE

There is no next batch, and this file no longer carries a kickoff message (by
design: the last batch removes the kickoff section, and the Stop hook
`kickoff_guard.py` stands down once the "Message to paste into the next chat"
section is gone). Read `COMPLETION.md` first; then `PROGRESS.md` (the R01-R04
entries) for the register pass; then `CHANGELOG.md`.

All 14 units are translated, built, and QA-clean: the Preface (ch00), Chapters
1 through 12 (ch01-ch12), and the Afterword (ch13). The illustrated edition's
figures are all in (182 inline + a 36-plate gallery + the real cover). The
finished, rebuilt deliverable is `out/chinas_secret_war.epub` (committed with
`git add -f`; chat attachments do not outlive the container, the branch does).
qa_epub PASS; epubcheck 5.1.0 clean (0/0/0/0).

## What the voice/register pass did (R01-R04, complete 2026-08-22)

The commissioner-ordered whole-book voice/register pass is finished. It was an
English-to-English re-voicing toward the modern-neutral register in
`STYLE.local.md` ("THE REGISTER REBASELINE"), with content FROZEN: every edit
preserved its original's propositional content exactly (no fact, name, number,
date-value, or claim changed; no paragraph merged or split; no name
re-romanized; no note added or removed). The machinery: committed
`edits/<id>_edits.md` lists applied by `scripts/apply_edits.py`,
`scripts/anchor_check.py` before every apply, per-unit blind context-free
critique via `scripts/voice_gate_critique.py` (archived under
`review/voice_gate/`), one commit per unit, build + qa_epub each.

- R01 (calibration + exemplar): ch00, ch01, ch09. The REVISED
  `out/ch01_reading.md` is the register reference.
- R02: ch02, ch03, ch04, ch05. R03: ch06, ch07, ch08.
- R04 (final) + closing sweep: ch10, ch11, ch12, ch13 (66 edits: 10/9/14/33).

MOST paragraphs in the narrative chapters were LEFT untouched; the book already
measured modern on the syntax-archaism axis. The pass protected the author's
deliberate register (the partisan "interested witness" voice, "old Chiang," the
vivid keep-idioms and 对仗 set-pieces, the footnoted allusions, the one-line
punches, quoted-document shapes, the *tewu* italics). The Afterword (ch13) drew
the most edits, being the author's own essay and the most translationese-dense
unit. No new STYLE.local rules were needed.

Closing sweep (all clean): book-wide apparatus checks (check_apparatus 0
failures; no bundled notes; density spread ~3.2x, within tolerance), whole-book
tic regression (near-zero batteries stayed near zero), the check_register table
(R04 units within tolerance; the lone drift flag is pre-existing ch02), and
epubcheck 0/0/0/0.

## Further work is a CORRECTIONS PASS, not a new batch

The commissioner reads the EPUB and files corrections in `CORRECTIONS.md` (or
pastes them in chat, to be transcribed there). GLOBAL corrections cascade via a
glossary/style change plus a grep across all built units INCLUDING note and
glossary bodies, then rebuild and full QA; LOCAL corrections are a fix at one
spot. A corrections pass with zero items is still a clean-checkout regression
run: re-clone, replay the resegment scripts, rebuild, re-verify, prune stray
branches.

PROGRESS.md's R04 entry logs the source-dependent faithfulness items the blind
readers raised, which a frozen register pass could not resolve without the
scan and which a corrections pass should look at:
- ch10: the "eight/fourteen/fifteen years" War-of-Resistance span; the "three
  vs two liaison officers" count; the "Zhang Bingnan written by mistake for
  Zhang Bingnan" romanization collision (two distinct source characters lost);
  the note-vs-text Wang Shiwei detail (well vs "put to death").
- ch11: the Baoding-vs-Chiang apparent contradiction (Wu Shi paragraph); the
  unreferenced "dead fish"; the third-person "her" in Xiao Minghua's testament.
- ch12: Xi'an "ancient capital of six dynasties" (usually thirteen); the
  "security, safety" near-synonym pair (possibly distinct 保卫/安全 terms).

## Environment / tooling (do NOT revert)

- `./setup.sh` once per session. `OMP_THREAD_LIMIT=1` mandatory for tesseract;
  kill the process GROUP, confirm `pgrep -c tesseract` reads 0. epubcheck at
  `/tmp/epubcheck-5.1.0/epubcheck.jar`. PaddleOCR absent (expected).
- Rebuild from a clean checkout: `./setup.sh`; replay the resegment scripts;
  `python3 scripts/build_reading_epub.py`; `python3 scripts/qa_epub.py`;
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub`.
- Do NOT revert: the composable style system (`styles/`, composed `STYLE.md`
  which is a BUILD ARTIFACT never hand-edited, `STYLE.local.md` ledger),
  `book.json` `genre: nonfiction`, the register-pass scripts
  (compose_style, check_style_freshness, voice_gate_critique, anchor_check,
  apply_edits, register_tics.sh), `review/PROTOCOL.md`, the per-parity OCR crop
  and the resegment_chNN.py scripts, and all figures-pass items.
- Work on branch `claude/chinas-secret-war` only (CLAUDE.md rule 2); expect a
  stray per-task branch at session start and consolidate onto the canonical
  branch.
- The setup regression "hook stands down on template stub" no longer applies:
  the kickoff section has been removed from this file, so the Stop hook stands
  down of its own accord.
