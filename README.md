# EPUB translation template

A reusable starter kit for turning a digital **source EPUB** (real text, no
scanning) into an annotated English EPUB: verified translation, footnotes,
glossary, and a cumulative EPUB with a full hyperlinked table of contents.

**New here? Read [`START_HERE.md`](START_HERE.md).** It has the setup steps and
the paste-ready messages. The full operating manual is [`CLAUDE.md`](CLAUDE.md).

The first step is **ingest + a structural survey**, before any translation:
`ingest_epub.py` unpacks the source and extracts its text and structure;
`survey.py` reports the counts/outline and a proposed batch plan; and
`build_reading_epub.py` produces a skeleton EPUB whose table of contents is
already fully hyperlinked down to subsections. You approve the batch plan, then
translation begins.

> This is the sibling of the scanned-PDF template. Same batch process, same
> hyperlinked-TOC build; the OCR/scan/page machinery is replaced by EPUB ingest,
> and there are no page numbers (cite chapters and sections).

## The pipeline in one glance

```
STEP 0  source.epub ──ingest_epub.py──▶ data/src/*.txt + data/figs/* + book.draft.json + out/INGEST.md
                    (author book.json from the draft)
        book.json ──survey.py──▶ out/SURVEY.md (counts + batch plan)
                  └─build_reading_epub.py──▶ skeleton out/book.epub (hyperlinked TOC) ─▶ qa_epub.py
                                                     │  (you approve the batch plan)
BATCHES ◀────────────────────────────────────────────┘
data/src/<unit>.txt ──(translate)──▶ out/<id>_bilingual.md ──split_bilingual.py──▶ out/<id>_reading.md + data/zh/<id>.txt
        │  │                                              │
        │  └── check_numbers.py                           └── check_structure.py --pairs
        ▼
   notes.json, glossary.json, figures.json, book.json
        │
        └── build_reading_epub.py ──▶ out/book.epub ──▶ qa_epub.py (must be green)
```

Ingest + survey first; then one batch at a time, each shipping a rebuilt EPUB and
an updated handoff. See `CLAUDE.md` for the rules and the checks.

## Scripts

| Script | Does |
|--------|------|
| `ingest_epub.py [source.epub]` | **Run first.** Unpack the EPUB; extract each spine document's text + images; count source chars; write `out/INGEST.md` and `book.draft.json`. |
| `survey.py [--target N]` | Structure report (parts/chapters/sections/subsections, source-char sizes, titles) + a proposed batch plan, from `book.json`. |
| `split_bilingual.py <bilingual> <id> "<zh title>"` | Split the QC bilingual into reading text + parity source. |
| `check_numbers.py <bilingual>` | Every numeral survives source to target. |
| `check_structure.py --pairs <zh> <reading>` / `--config <cfg>` | Paragraph parity, note anchors, heading shape, glossary drift. |
| `build_reading_epub.py [out.epub]` | Build the cumulative EPUB (fully linked TOC) from `book.json`. |
| `qa_epub.py <epub>` | Validate the built EPUB (well-formedness, links, notes). |

## Requirements

```
pip install pillow        # optional, for figure images
# everything else is pure Python stdlib. No OCR engine or PDF renderer needed.
```
