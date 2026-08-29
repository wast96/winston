# PROGRESS — The Tragedy of the Chinese Revolution (annotated edition)

Per-batch log. Written as the work happens, not at the end.

## Setup / survey (this session)

- Source: born-digital PDF, Haymarket Books 2009 reprint of the Secker &
  Warburg 1938 first edition of Harold Isaacs, "The Tragedy of the Chinese
  Revolution". 409 pages, clean embedded text layer (QuarkXPress/Quartz), zero
  page images on text pages. No OCR and no translation needed. Committed as
  source.pdf.
- This is an ANNOTATED ENGLISH EDITION, not a translation. Pipeline adapted:
  the reading files hold Isaacs's own text verbatim; the apparatus is his own
  endnotes (converted to footnotes) plus a new editorial footnote layer, a
  glossary, and a Principal Characters page.
- Page furniture: no cropping needed (text layer is clean). Running heads
  ("TRAGEDY OF THE CHINESE REVOLUTION" / chapter title) and folios strip
  textually during extraction. In-text reference marks are 5.5pt superscript
  digits, per-chapter numbering.
- Offset: front matter roman i-xxii; body restarts arabic 1; body offset a
  constant 23 (printed = PDF-page-1indexed - 23), verified at all 20 chapter
  openers. Recorded per unit in book.json.
- Structure: 20 chapters + Foreword (Arnold R. Isaacs, 2009) + Introduction
  (Leon Trotsky); no titled sections within chapters. Full structure in
  book.json, spot-verified against the scan and the printed TOC. 4 TOC-vs-opener
  title discrepancies flagged (ch08/09/10/16); opener forms used.
- book.json metadata (Step 0a) complete: title, author, publisher (Haymarket),
  1938 date, subjects (BISAC), rights (honest copyright note, not public
  domain), source_ref, edition_kind "annotated", note_heading "A Note on This
  Edition".
- Builder adapted for edition_kind "annotated" (see HANDOFF "Tooling in place").
- Checks run this session: skeleton EPUB build OK; qa_epub PASS (22 documents,
  all links resolve, cover generated, 0.1 MB); epubcheck 5.1.0 clean (0 errors /
  0 warnings, EPUB 3.3). SURVEY.md written to out/.
- Flagged for the read-through / gate: omit the printed index (dead page refs);
  confirm single note stream with "Ed." marks; confirm the 2009 Foreword is
  kept.
- STOP: survey presented for approval; Batch 1 kickoff served (ch01). No chapter
  prepared yet.

## B01 = ch01 "Seeds of Revolt" (pending)

- (fill in per the batch)
