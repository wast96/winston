# EPUB translation template

A reusable starter kit for turning a digital **source EPUB** (real text, no
scanning) into an annotated English EPUB: verified translation, footnotes at
reader-model density, glossary, both the translator's and the source's own
note streams, and a cumulative EPUB with a full hyperlinked table of
contents, a cover, and store-ready metadata. Distilled from six completed
EPUB-source books (and the scanned-book siblings).

**New here? Read [`START_HERE.md`](START_HERE.md).** The full operating manual
is [`CLAUDE.md`](CLAUDE.md). Template version:
[`TEMPLATE_CHANGELOG.md`](TEMPLATE_CHANGELOG.md).

> Sibling of the scanned-PDF template (`translation-template-master`). Same
> batch process, gates, checks and build; the OCR machinery is replaced by
> EPUB ingest, and there are no page numbers (cite chapters and sections).
> The shared checker scripts are maintained on the scanned template FIRST and
> synced here, so a fix lands once, not twice.

Two approval gates, then batches: the **ingest + survey** (you approve the
batch plan against a navigable skeleton EPUB), then after Batch 1 the
**voice gate** (you approve voice, note density and formatting of one real
chapter, which becomes the frozen register reference).

## The pipeline in one glance

```
STEP 0  source.epub ─ingest_epub.py─▶ data/src/ + data/figs/ + book.draft.json
                     (grep for the source's own note markers; author book.json)
        book.json ──survey.py──▶ out/SURVEY.md (counts + batch plan)
                  └─build_reading_epub.py──▶ skeleton EPUB ─▶ qa_epub.py
                                       │ (approve plan; later, voice gate)
BATCHES ◀──────────────────────────────┘
data/src/<unit> ─(translate)─▶ out/<id>_en.json ─make_bilingual.py─▶ bilingual (QC only)
        │                                  │
        └ verify_unit.py (parity+numbers+anchors)   ├ check_align.py / check_content.py
          check_register.py --ref                   └ tail verification vs source
        ▼
 notes.json / source_notes.json / glossary.json / figures.json (apparatus_merge.py)
        │
        └── build_reading_epub.py ──▶ out/<deliverable> ──▶ qa_epub.py + epubcheck
```

## Scripts

| Script | Does |
|--------|------|
| `ingest_epub.py [source.epub]` | **Run first.** Unpack; extract text + images; count chars; write `out/INGEST.md`, `book.draft.json`. |
| `survey.py [--target N]` | Structure report + proposed batch plan, from `book.json`. |
| `apply_format_markers.py` | Recover set-off text (vignettes, scene breaks, datelines, verse) from the source HTML into the `***`/`{v}{d}{g}{p}` markers. |
| `make_bilingual.py <id> <src> <title> <en.json>` | Zip verbatim source lines with your English array; refuses on count mismatch. |
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
| `apply_edits.py <id>` | Mechanical application of `edits/<id>_edits.md` (revision passes). |
| `smart_quotes.py` / `reflow.py` | Offset-preserving typography; re-flow onto corrected paragraphing. |
| `build_reading_epub.py [out.epub]` | Build the cumulative EPUB (cover, metadata, set-off classes, two note streams) from `book.json`. |
| `qa_epub.py [epub]` | Validate the built EPUB (structure, links, notes; reads `book.json` `deliverable`). |
| `tests/run_tests.py` | Regression harness for the checkers; extend with every new trap, keep green. |

## Requirements

```
./setup.sh   # pillow + epubcheck + regression tests; everything else stdlib
```
