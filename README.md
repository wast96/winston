# Scanned-book translation template

A reusable starter kit for turning an image-only scanned book into an annotated
English EPUB: OCR, verified translation, footnotes, glossary, and a cumulative
EPUB with a full linked table of contents.

**New here? Read [`START_HERE.md`](START_HERE.md).** It has the setup steps and
the paste-ready messages. The full operating manual is [`CLAUDE.md`](CLAUDE.md).

The very first step is a **structural survey**, before any translation: fill in
`book.json`, run `survey.py` for the counts/outline and a proposed batch plan,
and `build_reading_epub.py` to produce a skeleton EPUB whose table of contents is
already fully hyperlinked down to subsections. You approve the batch plan, then
translation begins.

## The pipeline in one glance

```
STEP 0  book.json ──survey.py──▶ out/SURVEY.md (counts + batch plan)
                  └─build_reading_epub.py──▶ skeleton out/book.epub (hyperlinked TOC) ─▶ qa_epub.py
                                                     │  (you approve the batch plan)
BATCHES ◀────────────────────────────────────────────┘
source.pdf ──render.py──▶ data/png ──ocr_crop.py──▶ data/txt
                                                       │
                        (read + verify against scan)   ▼
     out/<id>_bilingual.md ──split_bilingual.py──▶ out/<id>_reading.md + data/zh/<id>.txt
        │  │                                              │
        │  └── check_numbers.py                           └── check_structure.py --pairs
        ▼
   notes.json, glossary.json, figures.json, book.json
        │
        └── build_reading_epub.py ──▶ out/book.epub ──▶ qa_epub.py (must be green)
```

Survey first; then one batch at a time, each shipping a rebuilt EPUB and an
updated handoff. See `CLAUDE.md` for the rules and the checks.

## Scripts

| Script | Does |
|--------|------|
| `survey.py [--target N]` | **Run first.** Structure report (parts/chapters/sections/subsections, page counts, titles) + a proposed batch plan, from `book.json`. |
| `render.py FIRST LAST --dpi 300` | PDF pages to PNG (PyMuPDF). |
| `ocr_crop.py FIRST LAST ...` | Crop page furniture, OCR the body block. **Measure the crop per book** (see its docstring). |
| `find_figures.py FIRST LAST` | Detect photo/plate regions (misses line art; eyeball too). |
| `split_bilingual.py <bilingual> <id> "<zh title>"` | Split the QC bilingual into reading text + parity source. |
| `check_numbers.py <bilingual>` | Every numeral survives source to target. |
| `check_structure.py --pairs <zh> <reading>` / `--config <cfg>` | Paragraph parity, note anchors, heading shape, glossary drift. |
| `build_reading_epub.py [out.epub]` | Build the cumulative EPUB from `book.json`. |
| `qa_epub.py <epub>` | Validate the built EPUB (well-formedness, links, notes). |

## Requirements

```
pip install pymupdf pillow numpy opencv-python-headless
# plus tesseract + the language packs for the book's script (see CLAUDE.md)
```
