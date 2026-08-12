# COMPLETION.md — The Stealthy Ones (Goemon Boiled in the Cauldron)

Whole-book completion report for the annotated English translation of Murayama
Tomoyoshi's *Shinobi no mono: Goemon kamairi* (村山知義『忍びの者〈五右衛門釜煎り〉』),
from an image-only scan of the 1987 Kobunsha bunko edition. Written on the final
batch instead of a handoff. The book is COMPLETE.

## Status at a glance

- **8 of 8 chapters translated**, plus the source edition's afterword rendered
  as attributed back matter. About **146,000 words** of English.
- **213 footnotes**, numbered continuously book-wide.
- **226 glossary rows**: 124 people, 3 organizations, 63 places, 36 terms.
- **0 figures** (a deliberate decision, recorded below: the source is a text-only
  novel with no plates or diagrams).
- **qa_epub: PASS** (23 files, 16 documents, 9 reading documents, 3,159
  paragraphs, 213/213/213 note refs/bodies/backlinks, 48/48 page markers, all
  links resolve).
- **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.**
- **check_apparatus: clean**; **check_reconcile --variants: clean** (no wrong
  form surviving; spelling locale 0 British / 194 American).
- Deliverable: **`out/The Stealthy Ones.epub`**, committed with `git add -f` on
  branch `claude/the-stealthy-ones` (see "Definition of done").

## What the finished edition contains

- **Cover:** the publisher's colour cover art (an illustration of the Nanzen-ji
  gate-tower, the setting of Goemon's famous kabuki rooftop scene), extracted
  byte-identical from the source PDF (`cover.jpg`) and copied byte-identical into
  the EPUB. The generated typographic cover is not used.
- **Front matter:** title page (honestly marked complete), a Principal
  Characters page (14 principals, the standard courtesy of published Chinese and
  Japanese translations), and a full hyperlinked table of contents.
- **The eight chapters**, clean reading English, with set-off conventions
  rendered by the builder: scene-break asterisms, italic vignettes and datelines,
  hour-glosses, and verse. Footnotes appear as pop-up asides (Apple Books /
  Kindle) with a full endnotes page as fallback.
- **Back matter — the afterword.** The *kaisetsu* by the literary critic
  Musashino Jirō, printed in the 1987 bunko edition (printed folios 529-534), is
  rendered as clearly attributed back matter, with an attribution line naming
  Musashino Jirō and stating it is the afterword to that edition. It is placed
  after the last chapter and before the Notes, so the source book's own critical
  essay is kept distinct from the translator's apparatus. Where it quotes the
  novel, it reuses this translation's exact wording.
- **Translator's note and a full glossary** (name/term ledger with status codes).
- **Deliberately NOT invented:** there is no errata table and no colophon,
  because the source novel prints neither; `back_matter.json` carries only the
  afterword and leaves the errata/colophon slots inert. No figures were
  fabricated; the book has no plates.

## Per-chapter tally

| Unit | Title | Printed folios | ~Words | Notes | Figures |
| --- | --- | --- | --- | --- | --- |
| ch01 | New Waves | 5-68 | 18,300 | 67 | 0 |
| ch02 | A Warm Current | 69-134 | 18,000 | 29 | 0 |
| ch03 | Surface and Underside | 135-198 | 17,800 | 34 | 0 |
| ch04 | War upon War | 199-256 | 16,100 | 20 | 0 |
| ch05 | The Two of Them | 257-358 | 28,000 | 24 | 0 |
| ch06 | Earth and Water | 359-412 | 15,900 | 9 | 0 |
| ch07 | Death, Death, Death | 413-457 | 11,800 | 13 | 0 |
| ch08 | Death Throes | 459-528 | 20,300 | 17 | 0 |
| — | Afterword (Musashino Jirō) | 529-534 | — | — | 0 |

Note density tapers naturally from 67 in Chapter 1 (which sets up the whole
book's furniture) to single digits late on, exactly as a reader-model, not a
quota, predicts.

## Batching as executed

- **Batch 0 (survey):** 8-chapter structure, EPUB metadata, skeleton EPUB;
  batching approved (eight chapter-batches; the afterword as B09 back matter; a
  typographic cover, later replaced by the extracted colour cover).
- **Batches 1-8:** one chapter each, in order, each shipped end to end (reading
  text, notes, glossary, checks, cumulative EPUB, handoff). Batch 1 passed the
  first-chapter voice gate and became the frozen register reference.
- **Batch 9 (this batch, final):** afterword, cover decision, whole-book
  reconciliation sweep, ledgers, deep audit, completion report. No deviation from
  the approved plan; the afterword was carried here as agreed rather than treated
  as a ninth chapter.

## Checks run book-wide, and what they found

- **Numeric invariants, parity, anchors, entity survival, alignment, content,
  register** were run every chapter and recorded in `PROGRESS.md`; all passed
  within documented tolerances. The register checker's "shall"/low-contraction
  flags on exposition-heavy chapters are documented deviations, not the ch01
  defect.
- **Tail verification** (the final paragraphs of each unit read against the scan)
  was done per chapter, per the standing rule that the tail is where faithfulness
  fails.
- **Whole-book reconciliation (check 12):** the five open items were decided and
  cascaded across every unit, `notes.json`, and `glossary.json`, with the wrong
  forms folded into `data/variants.json` (wrong forms only):
  - **Mount Kōya** (macron; native short forms "Kōya-san"/"Kōya" kept),
    **Osaka** (plain, conventional English), **Daitō** (macron), **Sassa
    Narimasa / Sassa** (standard Hepburn), **Kyūshū** (macron).
  - Two further drifts the pass surfaced were fixed: **Hattori Hanzō** (the
    antagonist had about thirteen macron-less strays against 300-plus correct)
    and **Taikō kenchi**; and the spelling locale was unified to American
    (gray, theater, story, mold).
  - The deep audit surfaced one more: **daimyo / shogun** were split with and
    without macrons; standardized to the plain naturalized English forms.
  - The ~20 decided renderings were grep-counted book-wide and are each
    single-form. Recurring subjects' notes sit at first substantive appearance;
    Negoro-ji (a glancing childhood dialogue mention) and the Jurakudai (a
    one-word list item) keep their substantive notes downstream, with the
    glossary carrying the gloss meanwhile.
- **Scholarship consistency (check 11):** each substantive note states its
  verdict (corroborated / uncorroborated / contradicted) inline. This is
  historical fiction, so no separate reliability map is written; the apparatus
  carries the adjudication, and flags where the author writes as an interested
  witness of his own century (his materialist reading of Hideyoshi, the
  Chollima/politics asides).

## Observed error rate

Random-sample deep audit (check 10), full detail in **`out/deep_audit.md`**:

- Population 3,134 body paragraphs; fixed seed `19870824`; 18 windows drawn
  (3.4%), then read against the source page images, with **at least one full
  source page verified in every one of the eight chapters** (~54 paragraphs
  read zh-against-en).
- **Zero mistranslation errors.** By the rule of three, zero errors in 54
  paragraphs bounds the paragraph-level rate **below about 5.6% at 95%
  confidence — a bound, not a proof of zero.**
- The invented-precision class was scanned whole-book and spot-checked: no
  vague-source-to-false-specific conversions; the two riskiest physical
  definiteness cases are grounded in the source's own explicit description.
- One finding (daimyo/shogun spelling) was fixed during the audit; see above.

## Findings that need the commissioner's eye

None outstanding. Every machine check is green and the deep audit found no
mistranslation. The remaining items below are things a reader should simply be
aware of, not open questions.

## Residual uncertainties and standing decisions a reader should know about

Each of these is already flagged in the notes at its place; consolidated here:

- **The source's own inconsistencies are rendered as read**, never silently
  harmonized. The clearest instance is the medicine-peddler's patter at printed
  folio ~81 that his wares came "from Ming China" although famed "since the Nara
  capital" (Nara predates Ming): the source says 明国渡来, so the anachronism is
  the author's and is kept, not corrected. Internal name and detail
  inconsistencies elsewhere are handled the same way.
- **One illegible route waypoint (printed folio ~509)** on Goemon's road into
  Iga could not be read on the scan and is rendered as motion ("out from Gojō")
  rather than inventing a place name. The legible waypoints around it are all
  carried. This is an honest gap, per the no-invented-bridging-text rule.
- **The Yamashina/Tokitsune diary slip (printed folio ~522):** where the novel
  attributes the execution record, the footnote records the discrepancy rather
  than repairing the text.
- **The inverted cauldron legend (printed folio ~528):** the novel inverts the
  traditional legend (Goemon turning the blind child under himself to end its
  suffering, rather than holding it up); the note flags that this is the author's
  deliberate inversion of the received story.
- **Provisional romanizations** (glossary `status: provisional`) are marked
  visibly in the build; they are readings not attested outside this translation
  and should be treated as best-effort.
- **No in-text printed-page markers for ch02-ch08** (only ch01 emits them); every
  note nonetheless cites the printed folio in its prose, so citations remain
  followable.

## Provenance and method

- **Source:** image-only PDF, 537 pages, no text layer; 1987 Kobunsha
  jidai-shosetsu bunko edition. Vertical Japanese, right-to-left, dense furigana.
  PDF-to-printed offset a constant +2 (printed = pdf - 2), verified at every
  opener and at the afterword.
- **OCR was a structural aid only; the translation was made by reading the page
  images.** Vertical-Japanese OCR (tesseract `jpn_vert`, psm 5, with the dual
  psm-6/inverted substitute) is furigana-corrupted, so every proper name, number,
  and low-confidence span was crop-verified by eye (`scripts/cropview.py`) before
  translation; crop-verified readings are replayable via `data/ocr_fixes.json`.
- **Builder features that must not be reverted:** the sectioned CJK-keyed
  glossary edited directly (apparatus_merge is for notes and figures only); note
  bodies authored with numeric character references; the afterword renderer
  (`render_afterword`, driven by `back_matter.json`'s `afterword` block) placed
  after the chapters and before the Notes; the byte-identical cover copy; the
  reconciliation variants map at `data/variants.json`.
- **Rebuild from a clean checkout:**
  - `./setup.sh`
  - `python3 scripts/render_term_ledger.py`
  - `python3 scripts/build_reading_epub.py`
  - `python3 scripts/qa_epub.py`
  - `python3 scripts/check_reconcile.py --variants data/variants.json`
  - `python3 scripts/check_apparatus.py`
  - `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar "out/The Stealthy Ones.epub"`
- **Environment note:** `OMP_THREAD_LIMIT=1` is mandatory for tesseract; check
  `pgrep -c tesseract` is 0 after any OCR run. One checker self-test ("hook stands
  down on template stub") fails on a template corner case that does not affect
  real batch replies.

## Definition of done — met

- **The EPUB:** front matter + all 8 chapters + afterword, full clean hyperlinked
  TOC, extracted colour cover, footnotes at reader-model density, glossary and
  translator's note current, no figures (honest, the book has none), no errata /
  colophon (the book prints none). `qa_epub` PASS across the whole spine;
  epubcheck clean. **The file itself is committed (`git add -f
  "out/The Stealthy Ones.epub"`).**
- `out/<id>_reading.md` per unit (the correction surface), **`out/term_ledger.md`**,
  **`out/deep_audit.md`** all present.
- `notes.json`, `glossary.json`, `figures.json`, `book.json`, `back_matter.json`
  current; **`authority.json` updated** with this book's 226 decided renderings
  under slug `the-stealthy-ones`.
- `PROGRESS.md` and `CHANGELOG.md` current; **`HANDOFF.md` rewritten to say the
  book is COMPLETE** and that further work is a corrections pass.

The book is finished. Any further work is a corrections pass driven by the
commissioner's read (see `CORRECTIONS.md` / the corrections workflow in
`CLAUDE.md`).
