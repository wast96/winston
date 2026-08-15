# COMPLETION — The Rebel (叛逆者) / Bi Yu

The book is complete. This is the completion report; it and `HANDOFF.md` are the
last things written and are not touched again.

## The book

- **Title:** *The Rebel* (《叛逆者》), four novellas of the secret intelligence
  war in Republican-era China, by Bi Yu (畀愚).
- **Source:** the digital EPUB, People's Literature Publishing House, 2020.
- **Deliverable:** `out/the_rebel.epub` — an annotated English study edition with
  footnotes, a glossary, a Principal Characters page, and a Translator's Note.
- **Structure:** 51 translation units in four parts —
  *The Rebel* (叛逆者, ch01–ch14), *The Postman* (邮差, ch15–ch30, with the
  author's afterword as ch30), *Potassium Cyanide* (氰化钾, ch31–ch40), and
  *Rouge* (胭脂, ch41–ch51).

## What was produced

- **2,158 paragraphs** translated in full, one English paragraph per source
  paragraph, parity machine-enforced by `make_bilingual.py`.
- **329 translator footnotes** across the book (0 source notes — the source
  carries none; every batch was grepped for `[\d+]` and recorded "none present").
- **265 glossary rows**, one rendering per referent, each with
  category / attestation-status / pinyin; a Principal Characters cast page for
  the six principals of the title novella.
- Back matter: `out/term_ledger.md` (the auditable term ledger),
  `out/deep_audit.md` (the whole-book fidelity audit).
- The book's decided renderings fed back into the shelf `authority.json`
  (tagged `the-rebel`; 233 new terms recorded, 4 cross-book divergences flagged
  `reconcile` for the next book: 歌乐山, 兆丰公园, 百乐门, 珞珈山).

## Whole-book QA (final batch)

- **Per-chapter gates, all 51 units green:** verbatim quotation + paragraph
  parity (by construction); numeric invariants (`check_numbers.py`, 0
  unresolved book-wide); entity survival (`qc_entities.py`, 0 misses);
  alignment (`check_align.py`); content / displacement
  (`check_content.py --config`, all name occurrences in the paired paragraph);
  register vs the frozen ch01 reference (`check_register.py --ref`, all within
  tolerance).
- **Apparatus:** `check_apparatus.py` — 0 failures, 0 warnings; every one of the
  329 note anchors resolves as a verbatim substring of its reading text.
- **Reconciliation** (`check_reconcile.py`): glossary-forward 258/265 decided
  forms present in prose (the 7 absent are terms that occur only in notes or as
  alternates); epithet/compound drift produced 12 human-read candidates, all
  reviewed and judged acceptable variation (e.g. pitch-dark / pitch-black).
  Spelling locale cascaded to American: the mixed British forms (grey, labour,
  honour) were normalized (grey→gray ×4 in prose; labour/honour in notes). Two
  British spellings remain **by design**, both proper names in their attested
  form: **Victoria Harbour** (Hong Kong) and the **Longhua Civil Assembly
  Centre** (the historical Shanghai internment camp); the reconcile script still
  lists these as mixed-pair candidates, which is a known false positive on
  proper nouns.
- **Deep audit:** 86 paragraph pairs (4.0%), fixed seed `20260815`, read
  source-against-translation — **0 errors**; by the rule of three this bounds
  the paragraph-level error rate below ≈3.5% at ~95% confidence, not at zero.
  The invented-precision scan returned nothing.
- **Build:** `qa_epub.py` PASS (65 files, 58 documents, all links resolve; 329
  references = 329 bodies = 329 backlinks; 2,158 paragraphs; 51 documents).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
  The TOC carries no pending scaffolding (all 51 translated); the cover is the
  source's own, reused **byte-identical** to `data/figs/cover00144.jpeg`
  (sha256 `aafb7f2a…33f09f`).

## Definition of done — checklist

- [x] Complete EPUB with cover and clean TOC, committed (`git add -f`).
- [x] `qa_epub.py` + epubcheck green.
- [x] Per-unit `out/<id>_reading.md` and `out/<id>_en.json` for all 51 units.
- [x] `out/term_ledger.md` and `out/deep_audit.md` written.
- [x] Both note streams complete (translator's 329; source 0, none exist).
- [x] `authority.json` fed back with this book's renderings.
- [x] `COMPLETION.md` written; `PROGRESS.md` / `HANDOFF.md` maintained; HANDOFF
      rewritten to the completion notice.

## Notes for the shelf

- Reconcile the four flagged cross-book divergences before the next book uses
  those place names (歌乐山, 兆丰公园, 百乐门, 珞珈山).
- The one live glitch policy call kept visible and footnoted, not corrected:
  联银券 named in the Jiangnan setting (it properly circulated in North China).
- Register reference ch01 stayed frozen throughout; it was never regenerated.
