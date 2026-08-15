# HANDOFF — The Rebel (叛逆者) / Bi Yu — COMPLETE

**The book is finished.** All 51 units of *The Rebel* (four novellas by Bi Yu)
are translated, annotated, built, and checked. There is no next batch and no
kickoff to paste; this file is now the completion notice and is not touched
again. The full completion report is in `COMPLETION.md`.

## Status: COMPLETE

- **Deliverable:** `out/the_rebel.epub` — 51 of 51 chapters, four parts
  (*The Rebel* ch01–ch14, *The Postman* ch15–ch30, *Potassium Cyanide*
  ch31–ch40, *Rouge* ch41–ch51), 2,158 paragraphs, 329 footnotes, 0 source
  notes, 265 glossary rows, Principal Characters page, Translator's Note.
- **Build gates green:** `qa_epub.py` PASS (329 refs = 329 bodies = 329
  backlinks; all links resolve); **epubcheck 5.1.0 clean (0/0/0/0)**, EPUB 3.3.
  TOC auto-cleaned of pending scaffolding. Cover reused **byte-identical** to
  `data/figs/cover00144.jpeg`.
- **Whole-book QA:** every per-chapter gate green across all 51 units (parity,
  numbers, entities, alignment, content/displacement, register vs the frozen
  ch01). `check_apparatus.py` 0/0. `check_reconcile.py` run; spelling cascaded
  to American (two proper-name British spellings kept by design: Victoria
  Harbour, Longhua Civil Assembly Centre). Deep audit: 86-pair sample (4.0%,
  fixed seed 20260815), 0 errors, honest rule-of-three bound stated.
- **Back matter written:** `out/term_ledger.md`, `out/deep_audit.md`,
  `COMPLETION.md`. `authority.json` fed back (slug `the-rebel`; 4 cross-book
  divergences flagged `reconcile` for the next book).

## Do not

- Do not reopen the kickoff cycle; there is no B10.
- Do not regenerate `reference/ch01.md` (the frozen register reference).
- Do not replace the cover (commissioner's standing instruction: the source's
  own cover, byte-identical).
- Do not touch this file again.

## Provenance

The per-batch record (B01–B09) is in `PROGRESS.md`; the prose contract is
`STYLE.md`; the operating manual is `CLAUDE.md`. All work lives on branch
`claude/the-rebel`.
