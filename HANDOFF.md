# HANDOFF — Zhou Enlai: Commander of the Hidden Front

The book is COMPLETE and the register pass (R1-R5) is CLOSED. We are now in the
**footnote-density pass** (FOOTNOTE_PASS.md). FN1 (ch00-ch05) and **FN2
(ch06-ch11) are done; FN3 (ch12-ch17) is next.** One batch = one fresh chat,
started by pasting the block below. (FN1 stopped at a light annotation-depth
gate; FN2 onward runs straight through, no gate.)

## Message to paste into the next chat

```
Zhou Enlai FN3 (footnote-density pass)

Read CLAUDE.md, then FOOTNOTE_PASS.md (it governs this pass), then STYLE.md ("Apparatus" and the partisan-source discipline), then this HANDOFF and PROGRESS.md's FN1/FN2 sections. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content is FROZEN: this pass ADDS and enriches footnotes only, no prose/number/name/paragraph change. Notes are authored as a JSON file and merged with scripts/apparatus_merge.py (never a heredoc); anchors are verbatim UNIQUE substrings of out/<id>_reading.md; note bodies are XHTML with numeric character references only; people notes carry no hanzi, term/place/event notes carry glossary-verified hanzi decoded and checked; cite printed folios where a note cites a page; never invent; fact-check every claim against real scholarship (Wikipedia/Baidu Baike/academic, NEVER Grok/Grokipedia/AI) with the verdict stated in the note. Use scripts/fa_check.py (first-appearance grep across notes.json + reading files) before every note and scripts/gloss_hanzi.py for hanzi. data/zh is a parity scaffold not needed for a notes-only pass; do not regenerate it unless a check requires it.

Do batch FN3 = greatly increase footnote density on ch12-ch17 (the manhunt aftermath, the Ren Bishi rescue, the "new chapter" trio, the radio and communications chiefs) per FOOTNOTE_PASS.md sections 2-6: sweep every chapter for people, places, events, institutions/offices/ranks/units, terms and period vocabulary, and allusions/idioms/quotations, and annotate every instance a non-specialist Western reader would miss AT ITS FIRST appearance book-wide. Density is coverage, not quota: every note carries real checked content and answers a real reader question; add nothing just to add it. Run the first-appearance check before every note and keep the "NOT re-noted" list in PROGRESS. RECONCILE any pre-existing later-chapter note whose subject first appears in ch12-ch17 by trimming the later note to a cross-reference at the first appearance (check each with fa_check). Then rebuild, check_apparatus.py, qa_epub (epubcheck if installed), PROGRESS + CHANGELOG, commit, push.

End with the rebuilt EPUB attached in chat AND the FN4 kickoff pasted verbatim in a fenced block (same form as this one, ch18-ch22). Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- Translation of all 28 units (ch00-ch27); register pass R1-R5 (see COMPLETION.md).
- **FN1 footnote-density pass, ch00-ch05: +46 notes (339 -> 385).** Details in
  PROGRESS.md's FN1 section. Merged via `data/fn1_notes_a.json` (ch00-01) and
  `data/fn1_notes_b.json` (ch02-05).
- **FN2 footnote-density pass, ch06-ch11: +24 notes (385 -> 409; ch06-ch11
  70 -> 94).** Per-unit counts, the full "NOT re-noted" list, fact-check
  verdicts, and reconciliations are in PROGRESS.md's FN2 section. Merged via
  `data/fn2_notes.json`. FN2 also did three reconciliations (below).

## Carry-forward for the footnote pass

- **First-appearance discipline is the main guard against redundancy.** Before
  every note run `python3 scripts/fa_check.py "Subject"`: it lists which reading
  files mention it (in order) and any notes.json anchor/body that already covers
  it. Note at the FIRST appearance book-wide; cross-reference, never re-note.
- **Reconciliations already done (do NOT redo):** Liu Bocheng ch07 -> cross-ref
  ch01 (the FN1-logged item); Qian Dajun ch10 -> cross-ref ch03; the
  Canton-Hong Kong Strike note moved from ch11 to its ch10 first appearance
  (ch11 now a cross-ref).
- **For FN3 (ch12-ch17):** check each pre-existing later-chapter note whose
  subject first appears in ch12-ch17 with fa_check and trim it to a cross-ref at
  the first appearance. Known figures who recur from here whose full notes may
  sit later: Du Yuesheng (full note at ch14 — first substantive appearance is
  ch14, so it is correctly placed; the Green Gang is now noted at ch09); Ren
  Bishi (noted at ch02 arrest + ch13 bio — if ch12/ch13 is his first substantive
  treatment, keep ch13 and cross-ref, per what fa_check shows). Verify with
  fa_check, do not assume.
- **Hanzi:** people notes carry none. Term/org/place/event notes carry hanzi as
  numeric character references, taken verbatim from `glossary.json` (use
  `scripts/gloss_hanzi.py`) and generated programmatically from the glossary
  string, never hand-typed; where the glossary lacks the term, prefer pinyin over
  a hand-typed glyph. Merge validates for U+FFFD and named entities.
- **Voice of the notes:** concise, one referent per note; dates; role in the
  period AND later fate; verdict "(Corroborated.)" or a graded claim. Match the
  existing note bodies (see ch00-ch11 for the model).

## Do not revert (accumulated tooling)

- `scripts/fa_check.py` (first-appearance grep) and `scripts/gloss_hanzi.py`
  (glossary hanzi reverse-lookup) — added in FN1; keep for every FN batch.
- `data/ocr_fixes.json`; `scripts/recovery/` (b01-b14 + r5/date generators);
  `data/noise.txt` (extend, never prune); `data/check_config.json`; builder
  invariants (pending-aware then cleaned TOC; note pop-ups with endnotes
  fallback; refusal to build on an unmatched anchor or unplaced figure;
  byte-identical cover copy; render-layer smart quotes).

## State / environment

- Deliverable: `out/zhou-enlai.epub` (committed with `git add -f`). 28/28
  chapters, **409 notes**, 36 figures, 496 pagebreaks. qa_epub PASS; epubcheck
  5.1.0 0/0/0.
- Ledgers: `glossary.json` (847 rows), `notes.json` (409), `figures.json`,
  `book.json`, `authority.json`; `out/term_ledger.md` and `out/deep_audit.md`
  are from the register close (refresh term_ledger only at FN5).
- `data/zh` is absent on a fresh checkout (untracked/regenerable) and was NOT
  regenerated for FN1/FN2 (parity scaffold, not needed for a notes-only pass).
  Regenerate per `scripts/recovery/README.md` only if a later batch needs
  qc_entities/parity.
- Body offset constant 44 (printed = PDF - 44). `OMP_THREAD_LIMIT=1` for
  tesseract; `pgrep -c tesseract` must read 0 after a run. One pre-existing
  failing regression test ("hook stands down on template stub"), template
  maintenance only, unrelated to the book.

## Environment / rebuild from clean checkout

1. `./setup.sh`
2. `python3 scripts/build_reading_epub.py`
3. `python3 scripts/qa_epub.py`
4. `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/zhou-enlai.epub`
(A notes-only FN batch does not need `data/zh`; regenerate it only if a check
that reads the source requires it.)
