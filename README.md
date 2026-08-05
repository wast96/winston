# Scanned-book translation template

A reusable starter kit for turning an image-only scanned book into an annotated
English EPUB: OCR, verified translation, footnotes at reader-model density,
glossary, and a cumulative EPUB with a full linked table of contents, a cover,
and store-ready metadata. Distilled from nine completed books; the hard-won
lessons live in `CLAUDE.md` and the `scanned-book-translation` skill.

> This branch is UPSTREAM for the scripts shared with the sibling EPUB
> template (`translation-template-epub-master`): checkers, tests, hook,
> process templates, authority/collection files. Fix shared things here
> first, then sync them across, so a fix lands once, not twice.

**New here? Read [`START_HERE.md`](START_HERE.md).** It has the setup steps and
the paste-ready messages. The full operating manual is [`CLAUDE.md`](CLAUDE.md).
Template version: see [`TEMPLATE_CHANGELOG.md`](TEMPLATE_CHANGELOG.md).

Two approval gates, then batches: the **structural survey** (you approve the
batch plan against a navigable skeleton EPUB), and after Batch 1 the
**voice gate** (you approve the register, note density and formatting of one
real chapter, which then becomes the frozen register reference).

## The pipeline in one glance

```
STEP 0  book.json ──survey.py──▶ out/SURVEY.md (counts + batch plan)
                  └─build_reading_epub.py──▶ skeleton EPUB (full TOC) ─▶ qa_epub.py
                                                  │ (approve plan; later, voice gate)
BATCHES ◀─────────────────────────────────────────┘
source.pdf ─render.py─▶ data/png ─ocr_crop.py + ocr_dual.py─▶ data/txt
                        └─indents.py─▶ data/indent ─┐
                                                    ▼
                       assemble.py ──▶ data/zh/<id>.txt (one paragraph a line)
   (translate → out/<id>_reading.md; crop-verify names/numbers; apply_fixes.py)
                                                    ▼
   out/<id>_reading.md ─make_bilingual.py─▶ out/<id>_bilingual.md (QC only)
        │                                           │
        └── verify_unit.py (parity+numbers+anchors) ├── check_align.py
            check_register.py --ref                 └── check_content.py
        ▼
   notes.json / glossary.json / figures.json  (via apparatus_merge.py)
        │
        └── build_reading_epub.py ──▶ out/<deliverable> ──▶ qa_epub.py + epubcheck
```

## Scripts

| Script | Does |
|--------|------|
| `survey.py [--target N]` | **Run first.** Structure report + proposed batch plan, from `book.json`. |
| `render.py FIRST LAST --dpi 300` | PDF pages to PNG (PyMuPDF). |
| `ocr_crop.py FIRST LAST ...` | Crop page furniture, OCR the body block. **Measure the crop per book.** |
| `ocr_dual.py FIRST LAST` | Second independent OCR read (psm 6 / psm 4 / inverted); disagreements drive crop verification. |
| `indents.py FIRST LAST` | Measure paragraph indents off the page images (the reliable paragraph signal). |
| `assemble.py <id> FIRST LAST` | Per-page OCR → per-chapter source, indent + sentence-end gated. |
| `find_headings.py` / `build_structure.py` | Recover structure when the scan has no TOC/bookmarks (geometry says where, body OCR says what). |
| `detect_notes.py FIRST LAST` | Does a page carry a footnote apparatus? (line-pitch geometry, no reading) |
| `find_figures.py FIRST LAST` | Detect photo/plate regions (misses line art; eyeball too). |
| `verify_names.py --auto` | Show only the spans the two OCR reads disagree on; crop-verify those. |
| `crop_lines.py --spec p:term ...` | Stitched line crops for SYSTEMATIC mangles both engines agree on. |
| `apply_fixes.py` | Replayable ledger of crop-verified readings (`data/ocr_fixes.json`). |
| `make_bilingual.py <id>` | Pair `data/zh/<id>.txt` with the reading file positionally for QC (run parity first). |
| `split_bilingual.py <bilingual> <id> "<zh title>"` | Split a QC bilingual into reading text + parity source. |
| `verify_unit.py <id> ...` | **The per-unit gate:** parity + numbers + anchors in one command. |
| `check_numbers.py <bilingual> --noise data/noise.txt` | Every numeral survives source to target. |
| `check_structure.py --pairs/--config` | Parity, anchors, heading shape, glossary drift, declared exceptions. |
| `check_align.py` / `check_content.py` | Ratio runs find missing text; glossary-name content finds MISPLACED text. |
| `qc_entities.py` | Every glossary hanzi's decided rendering survives into the pair. |
| `check_register.py --ref <chapter>` | Voice drift vs the frozen Batch 1 reference. |
| `check_reconcile.py` | Whole-book sweep: repeated-compound rendering drift, glossary-forward usage, spelling locale. |
| `apparatus_merge.py <batch.json>` | Validated, idempotent merge into notes/glossary/figures (kills the heredoc trap). |
| `check_apparatus.py` | Mojibake / named-entity / double-escape / anchor scan of the ledgers. |
| `apply_edits.py <id>` | Mechanical, verifiable application of `edits/<id>_edits.md` (revision passes). |
| `smart_quotes.py` | Offset-preserving, anchor-safe typographic normalization (if not using the render-layer pass). |
| `reflow.py` | Re-flow a finished translation onto corrected source paragraphing. |
| `build_reading_epub.py [out.epub]` | Build the cumulative EPUB (cover, metadata, set-off classes, pagebreaks) from `book.json`. |
| `qa_epub.py <epub>` | Validate the built EPUB (structure, links, notes, pagination). |
| `tests/run_tests.py` | Regression harness for the checkers; extend it with every new trap, keep it green. |

## Requirements

```
./setup.sh   # installs the stack, language packs, epubcheck; records failures
```
