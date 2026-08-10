# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE
CHAT, alongside the attached EPUB. Writing it here alone does not count.**
Rewrite it at the end of every batch; always keep the paste-ready kickoff
message below as its first section. When the book completes, replace the
kickoff with the completion notice and do not touch it afterward (the Stop
hook keys off it).

## Message to paste into the next chat

```
Scales and Claws B01

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; scanned source is the 2019 Taipei reprint, customs volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the harness to start you on a stray branch and consolidate per rule 2. Deliverable out/scales-and-claws-of-shanghai.epub.

Do Batch B01 = ch000 (author's preface) + ch001 (上海人的過年忙 The New Year Rush), PDF pages 12-13 and 23-33 (printed folios 10-11 and 21-31; PDF 14-22 are a blank verso and the printed TOC, skip them), end to end per the CLAUDE.md pipeline:
1. ./setup.sh; batch 1 only: measure the page furniture and configure ocr_crop.py (crop box, --lang chi_tra_vert, --psm 5; running heads and the stacked folio digits sit at the top of the page, body block below); render; OCR (ocr_crop.py + ocr_dual.py); pgrep -c tesseract must be 0 after.
2. indents.py + assemble.py for paragraph structure (vertical RTL: verify column order comes out right on a page you read by eye); find_figures.py AND eyeball every page for the reprint-added photographs; the commissioner has ruled the photos IN: crop each one, figures.json spec with alt text and a caption that translates the reprint's label and states provenance (2019 editor's addition, not a figure of the 1933 book).
3. This is the FIRST translated unit, so there is no previous voice to splice onto; set the voice per the register contract in CLAUDE.md (1930s newspaperman's miscellany: quick, worldly, amused, never academic; the preface ch000 is classical in register and should read as formal period prose). Consult glossary.json and authority.json BEFORE romanizing anything (Shanghai street names and institutions are on the shelf ledger); crop-verify every name, number, and low-confidence span (verify_names.py --auto, crop_lines.py); record verified readings via apply_fixes.py. Never invent bridging text; verify each unit's tail against the scan.
4. Write out/ch000_reading.md and out/ch001_reading.md (one paragraph per source line), make_bilingual.py per unit, verify_unit.py per unit AS YOU GO; check_align.py + check_content.py.
5. Footnotes per the reader model in CLAUDE.md via apparatus_merge.py (this opening batch will be note-dense: lunar/solar calendar politics, New Year customs, money and shop practice); glossary rows with attestation; flag recurring cast principal: true as they appear.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar, else fetch per setup.sh); record all check results in PROGRESS.md; commit.
7. Then STOP at the voice gate: attach the EPUB and present the first chapter; ask the commissioner to judge voice, note density, and formatting. Do NOT write or paste a B02 kickoff, and do not start B02; on approval this chapter freezes as the register reference for the whole book.

Cite printed folios, never PDF pages. Do not pause for approval mid-batch before the gate.
```

## What is DONE (do not redo)

- Survey (2026-08-10): source characterized, book.json complete (metadata,
  168-chapter structure from verified bookmarks, 10 batches), skeleton EPUB
  green (qa_epub PASS; epubcheck 5.1.0 clean), out/SURVEY.md written,
  committed on claude/scales-and-claws. Batch plan and the three standing
  decisions approved by the commissioner; photos ruled IN (see PROGRESS
  Setup/Survey section).
- No translation yet. B01 is next and ends at the voice gate.

## Tooling in place (do not revert)

- Template scripts as shipped; no project patches yet. setup.sh runs clean;
  PaddleOCR absent (use ocr_dual.py); epubcheck at
  /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetched by setup.sh if the container
  is fresh).

## Renderings settled / carry-forward

- Title: Scales and Claws of Shanghai; author Yu Muxia (郁慕俠); preface
  author: Chen Diexian, pen name 天虛我生 Tianxuwosheng (ch000 signature
  reads 癸酉七夕天虛我生識於西湖息養社).
- English essay titles in book.json are PROVISIONAL, drafted at survey from
  the titles alone; each batch should refine its titles against the essay
  content and update book.json in the same commit (several are slang whose
  sense must come from the body: 沖鳥, 阿羊哥, 年紅燈, 桂花, 么二三式,
  大廠, 拉一把, 抄把子 among others).
- No voice sheets yet (essay collection, no continuing cast so far; the
  author's own voice IS the register, frozen at the B01 gate).
- Consult authority.json before romanizing: Shanghai streets/institutions
  (Avenue Joffre, Garden Bridge, the concessions' police and parks) recur
  across the shelf.

## Where the book stands

- Nothing translated. The book is 167 independent short sketches plus a
  2-page classical preface; there is no plot to track. Register decisions in
  B01 govern everything downstream.

## Next batch scope

- B01 = ch000 + ch001, PDF 12-13 and 23-33, printed 10-11 and 21-31, ending
  at the voice gate (no B02 kickoff from B01).
- B02 (after gate approval) = ch002-ch014, PDF 34-58, printed 32-56.

## Open traps and environment state

- The scan is the 2019 RESET, not the 1933 original: no access to the 1933
  text for collation; where the reprint is suspect (typos, modern
  punctuation choices), note it, do not guess at the 1933 reading.
- Vertical RTL OCR: column order errors are silent; verify assemble.py output
  by eye against one full page in B01 before trusting the pipeline.
- Two essays share PDF page 214 (頂呱呱與硬繃繃, 拋頂宮) and two share 218
  (賣性照片, 賣冰): unit boundaries mid-page, watch the parity split there
  (B09 and B10).
- Blank/filler pages: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252.
- Offset printed = pdf - 2 constant, but re-read the folio at every opener
  anyway (rule).
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included per
  commissioner.
