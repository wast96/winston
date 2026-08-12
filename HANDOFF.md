# HANDOFF — The Stealthy Ones

## THE BOOK IS COMPLETE

All eight chapters are translated, the source edition's afterword is rendered as
attributed back matter, and the cumulative EPUB is finished: front matter, 8/8
chapters, afterword, glossary, translator's note, extracted colour cover.
`qa_epub` PASS, `epubcheck` 0/0/0/0, `check_apparatus` clean,
`check_reconcile.py --variants data/variants.json` clean.

There is no next batch and no kickoff to paste. The whole-book completion report
is **`COMPLETION.md`** (written from the template instead of another handoff);
read that for the full state, the sampled error rate, the residual uncertainties,
and the standing editorial decisions.

**Further work is a corrections pass only.** The commissioner reads the EPUB and
files corrections in `CORRECTIONS.md` (or pastes them in chat, to be transcribed
there); then follow the corrections workflow in `CLAUDE.md` (global corrections
cascade via a glossary/style change plus a grep-driven edit across every built
unit including note and glossary bodies, then rebuild and full QA; local
corrections are a fix at one spot). A corrections pass with zero items is still a
clean-checkout regression run. Do NOT stack new chapters or reopen the
translation; the content is frozen.

## Deliverable and rebuild

- Deliverable: `out/the-stealthy-ones.epub` (committed with `git add -f`;
  branches outlive containers).
- One branch: `claude/the-stealthy-ones`.
- Rebuild from a clean checkout:
  - `./setup.sh`
  - `python3 scripts/render_term_ledger.py`
  - `python3 scripts/build_reading_epub.py`
  - `python3 scripts/qa_epub.py`
  - `python3 scripts/check_reconcile.py --variants data/variants.json`
  - `python3 scripts/check_apparatus.py`
  - `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/the-stealthy-ones.epub`

## What is DONE (one line per batch, do not redo)
- Batch 0 (survey): structure, metadata, skeleton EPUB, batching approved.
- Batch 1 (Chapter 1, "New Waves", folios 5-68): COMPLETE. Voice gate; frozen
  register reference (`out/ch01_reading.md`). 67 notes, 13 principals.
- Batch 2 (Chapter 2, "A Warm Current", folios 69-134): COMPLETE. 29 notes.
- Batch 3 (Chapter 3, "Surface and Underside", folios 135-198): COMPLETE. 34 notes.
- Batch 4 (Chapter 4, "War upon War", folios 199-256): COMPLETE. 20 notes.
- Batch 5 (Chapter 5, "The Two of Them", folios 257-358): COMPLETE. 24 notes.
- Batch 6 (Chapter 6, "Earth and Water", folios 359-412): COMPLETE. 9 notes.
- Batch 7 (Chapter 7, "Death, Death, Death", folios 413-457): COMPLETE. 13 notes.
- Batch 8 (Chapter 8, "Death Throes", folios 459-528): COMPLETE. 17 notes. The
  novel body fully translated.
- Batch 9 (FINAL): afterword (Musashino Jiro, folios 529-534) as attributed back
  matter; colour cover extracted byte-identical; whole-book reconciliation sweep
  (check 12) with `data/variants.json`; `out/term_ledger.md` + `authority.json`
  fed back; deep audit (check 10, `out/deep_audit.md`, zero errors in ~54
  paragraphs); COMPLETION.md; final EPUB committed.

## Tooling in place — do NOT revert
- `render_afterword` in `scripts/build_reading_epub.py`, driven by the
  `afterword` block in `back_matter.json`; placed after the last chapter and
  before the Notes.
- `scripts/render_term_ledger.py` renders `out/term_ledger.md` from the glossary.
- `data/variants.json`: the reconciliation variants map (wrong forms only),
  consumed by `check_reconcile.py --variants`.
- `cover.jpg`: the publisher colour cover, extracted byte-identical from
  `source.pdf`; `book.json` `cover_image` points at it; the builder copies it
  byte-identical.
- Glossary is a sectioned, CJK-keyed file edited directly (apparatus_merge is for
  notes and figures only). Note anchors are literal substrings of the reading
  files; note bodies use numeric character references. Reading files use house
  macron romanization plus the em-dash and the established loanword spellings
  (Lourenso with c-cedilla, irmao with a-tilde).
- Reconciled canonical forms: Mount Kōya, Osaka (plain), Daitō, Sassa Narimasa,
  Kyūshū, Hattori Hanzō, Taikō kenchi, daimyo/shogun (plain), American spelling.

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify with
  `scripts/cropview.py`. `OMP_THREAD_LIMIT=1` for tesseract; check
  `pgrep -c tesseract` is 0 after OCR.
- `epubcheck` at `/tmp/epubcheck-5.1.0/epubcheck.jar`.
- No `data/pagemap/` for ch02-ch08 (only ch01 emits in-text page markers); qa
  still PASSES and every note cites its printed folio in prose.
- One checker self-test ("hook stands down on template stub") fails on a template
  corner case that does not affect real batch replies.
