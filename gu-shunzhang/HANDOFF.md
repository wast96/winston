# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

## THE BOOK IS COMPLETE — there is no next batch

All eight chapters (B01–B11) are translated, annotated, and built into
`out/gushunzhang.epub`, together with the publisher's errata and colophon as
back matter. There is no further content batch. The consolidated read-through
surface is **`COMPLETION_REPORT.md`** (open that first).

If Winston files corrections, follow the Corrections workflow in `CLAUDE.md`
(global corrections cascade via glossary/style + grep-driven edit across all
built units, then rebuild + full QA; append a dated entry to `CHANGELOG.md`).

## Final state

- **8 / 8 chapters, 37 / 37 sections.** `out/ch01_reading.md` … `out/ch08_reading.md`.
- **212 notes** (continuous 1–212), **18 figures**, **132 glossary entries**.
- `out/gushunzhang.epub`: full, fully-linked TOC (expanded to section level),
  errata + colophon back matter. `qa_epub.py` PASS (39 files, all links resolve).
  `check_structure.py --config` PASS.
- **One irreducible gap:** printed folio 237 (the book's last leaf) is missing
  from the NCL scan; the text stops where the scan does, footnoted (note 210),
  with no invented bridging text. See COMPLETION_REPORT.md.

## Standing safety item (unchanged)

Chapter 6 §5 破壞術: non-operational doctrine is in the edition; the technical
device-construction core (folios 121-133) remains **withheld** and was never
read or reproduced. Do not "complete" it.

## Environment notes for any future rebuild

- Traditional OCR only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- `apt-get install ... poppler-utils` 404s and aborts the whole run; install
  tesseract WITHOUT poppler; render via PyMuPDF. PaddleOCR does not install here.
- `pip install pymupdf pillow numpy opencv-python-headless` install cleanly.
- Build-trap: note bodies are XHTML — numeric character references (`&#160;`,
  `&#215;`), never HTML named entities.
- One branch: `claude/gu-shunzhang`. Stray per-batch branches are folded onto it
  and deleted.
