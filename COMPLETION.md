# COMPLETION — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

The book is done. This report closes out the project in place of another
HANDOFF kickoff: Batch 25 was the last of the approved 25-batch plan, and the
whole annotated English EPUB now ships.

Deliverable: `out/The Longest Day in Chang'an.epub` (also attached in chat).

## What the book is

An annotated English translation of Ma Boyong's historical thriller 长安十二时辰,
made from the digital source EPUB (湖南文艺出版社, 2017). The novel runs in real
time across the twenty-four half-shichen of one day during the Lantern Festival
of Tianbao 3 (744 CE): the condemned buliang chief Zhang Xiaojing is given one
day to stop a plot to burn Chang'an. The edition adds footnotes, a glossary, a
translator's note, and an honest apparatus for uncertain and editorial passages.

## Scope completed

- **26 documents translated end to end:** 24 numbered chapters (ch01–ch24, the
  24 half-shichen of the day) plus 2 authorial afterwords (ch25 后记一, ch26
  后记二). ~407,000 source characters.
- **86 footnotes**, numbered continuously in reading order, at reference density
  (~3 per chapter-equivalent): translation uncertainties, historical references
  checked against scholarship, and texture lost in translation. The afterwords
  added 4 (the Nestorian Stele; the Changxin/Zhaoyang allusion; the real Tang
  text 《安禄山事迹》 that names a Zhang Xiaojing; Assassin's Creed / Zhihu).
- **Glossary: 656 rows** (150 people, 37 organizations, 213 places, 256 terms),
  the single term ledger — one decided rendering per referent, with status and
  attestation on each.
- **Front matter + translator's note** render from book.json (verbatim). No
  colophon: the source carries no imprint/奥付 page worth translating, so
  back_matter.json is left inert by design (a real colophon renders only when a
  top-level "colophon" key is present). No imprint page was invented.
- **Figures: none.** The source carries no content illustration (only a
  footnote-marker glyph and a scene-break rule, neither a figure); figures.json
  is empty by intent.

## Every check that ran, and its final result

Run per batch and recorded in PROGRESS.md; the whole-book state at completion:

1. **Faithful, complete quotation of the source (verbatim).** Every unit was
   built by a per-unit generator (scripts/gen_chNN_bilingual.py) that reads the
   source lines from data/src and ASSERTS the concatenation of every `>`
   blockquote equals the source content character-for-character before the
   checks. PASS for all 26 units.
2. **Blind double-translation** of argumentative/literary passages in fresh
   contexts, diffed against the shipped text. Divergences were stylistic only;
   no content divergence survived. Last sample (后记二's Chang'an-as-dream
   passage): clean.
3. **Round-trip back-translation** of number-dense passages in fresh contexts,
   as an omission detector. No omissions found. Last sample (后记一's Tianbao-3
   epilogue): every name, number, and date preserved.
4. **Automated invariant checks.** `check_numbers.py --noise noise.txt`: 0
   unresolved across every unit (each numeral, date, and year survives source →
   target; real quantities carried in words, non-quantity idiom numerals noised
   with the reason recorded). `check_structure.py`: paragraph parity EQUAL for
   every unit; note anchors resolve; heading shape uniform.
5. **Auditable term ledger.** glossary.json enforced one rendering per referent
   across all 26 units; greps against the built text kept cross-chapter
   consistency.
6. **Annotate, don't smooth.** Genuine ambiguities and source variants were
   footnoted or flagged in PROGRESS.md (e.g. ch24's 营山/营州 slip), never
   laundered into fluent prose.
7. **Consistency-check against scholarship.** Historical claims marked
   corroborated / uncorroborated / contradicted; the afterword's epilogue
   (He Zhizhang's death, the Türk collapse, An Lushan's rise, Li Bi's four
   reigns, Yisi and the 781 Nestorian Stele, the Mawei mutiny, the
   《安禄山事迹》 Zhang-Xiaojing notice) checked against the Tang record.
8. **Random-sample deep audit.** 3–5%+ of each batch given the full paranoid
   treatment; observed content-error rate at completion: 0.
9. **`qa_epub.py`: PASS** on the final EPUB — 26 documents (full spine), 7,417
   paragraphs, 86 references == 86 bodies == 86 backlinks, numbering sequential
   in reading order, all links resolve, 26 of 26 chapters translated (no
   skeleton pages), full hyperlinked TOC nesting part → chapter, with the two
   afterwords grouped under the "Afterword" part.

## Definition of done (CLAUDE.md) — checklist

- [x] The EPUB: front matter + all 24 chapters + 2 afterwords, full hyperlinked
      TOC, footnotes throughout at reference density, glossary and translator's
      note current, `qa_epub` PASS across the whole 26-document spine.
- [x] Figures with captions — N/A (the book has no content illustrations).
- [x] Colophon — N/A (the source has no imprint page; back_matter.json left
      inert, not invented).
- [x] `out/<id>_reading.md` present for every unit (the correction surface): 26
      files.
- [x] `notes.json`, `glossary.json`, `figures.json`, `book.json` current.
- [x] `PROGRESS.md` written as the work went; `HANDOFF.md` left as the final
      baton (no next kickoff on the last batch); this `COMPLETION.md` closes the
      project.

## Reading and corrections

The reading surface for corrections is `out/<id>_reading.md` per unit; the
commissioner files corrections in `CORRECTIONS.md`, and a corrections batch
rebuilds, re-runs `qa_epub`, lists every file touched, and appends a dated entry
to `CHANGELOG.md`. Global renderings cascade via a glossary/style change plus a
grep-driven edit across all built units, then a full rebuild and QA.
