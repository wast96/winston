# PROGRESS

## Batch 1 = Chapter 1, "New Waves" (PDF 7-70, printed folios 5-68) — COMPLETE

The chapter is a bridging prologue to Murayama's Goemon saga: it sets the stage
of 1582 (the Honno-ji Incident, the fall of the Takeda, the ninja's turn to the
Tokugawa after the Tarao crossing, the Christian mission at the Nanban-ji and
the seminaries) and ends by turning time back a year to rejoin the hero,
Ishikawa Goemon, whose story proper starts in Chapter 2. Goemon himself is only
named here, not yet on stage.

### Deliverables shipped
- `out/ch01_reading.md`: full clean translation, 328 body paragraphs, 4 scene
  breaks, one chapter heading. 18,700 words. The correction surface.
- 67 footnotes in `notes.json` (folio-cited throughout), glossary rows in
  `glossary.json` (13 principals flagged for the Principal Characters page),
  page map for folio citations.
- `out/the-stealthy-ones.epub`: cumulative build, full pending-aware TOC.

### Checks run and results
- `qa_epub.py`: PASS (8 documents, 67 refs / 67 bodies / 67 backlinks all
  resolve, 48 pagebreak markers, all links resolve).
- `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos (store-clean).
- `check_apparatus.py`: 0 failures, 0 warnings.
- `check_register.py`: baseline recorded (this is the FROZEN REFERENCE), taken
  AFTER the voice-gate re-voice (see below): dialogue contractions 8.8/1k,
  shall-share 0%, em-dash 0.3/1k, rhythm CV 0.63, sentence median 17.

### Voice-gate revision (commissioner feedback)
The first build was judged too stilted. The commissioner rewrote the opening
paragraphs to model the target voice; from that comparison a prose contract was
written to `STYLE.md` (approved), and the WHOLE chapter was re-voiced to it.
The fix was structural, not lexical: kill the dashed-in appositive gloss, break
long periodic sentences into short varied ones, break dense paragraphs at each
shift of focus, trim doubled synonyms, de-translationese, prefer active verbs,
hold understatement in narration while keeping the author's heat where the
source has it. The register numbers show the change: em-dash use fell from
16.3/1k to 0.3/1k (the four survivors are all interrupted/trailing dialogue),
sentence median from 23 words to 17. All 67 footnote anchors were reconciled to
the new prose (12 re-pointed in notes.json; all resolve). Content fidelity
verified: 47 critical name/number tokens all present, 18,321 words (tighter than
the first draft's 18,693, from trimming, not cutting). `STYLE.md` now governs
every remaining chapter.

### OCR and fidelity method (important, book-specific)
- OCR: tesseract `jpn_vert`, psm 5, crop left 0.06 / right 0.96 / top 0.09 /
  bottom 0.935 (as specified; drops the top-corner folio, keeps all body text).
  Verified `pgrep -c tesseract` = 0 after each run.
- `ocr_dual.py` was NOT used: it is hard-wired to `chi_sim` and horizontal psm
  4/6, wrong for vertical Japanese. `indents.py` likewise measures a horizontal
  indent axis and calls a `folio_present` helper that does not exist in
  `ocr_crop.py`; it does not apply to vertical text and was not run. These are
  Chinese-template scripts not yet adapted to this book.
- Because vertical-Japanese OCR with heavy furigana bleed is too corrupt to
  translate from directly (e.g. 洛中 read as 潜中, 乞食 as 包食, 鴨川 as 嶋川),
  the chapter was translated by reading every page image (PDF 8-70) directly,
  with the primary OCR used only as a structural aid. This is the skill's
  high-value method (targeted crop-verification against the scan), applied
  wholesale for a literary text.
- Crop-verified spans (recorded here so a fresh checkout knows what was
  eye-read): the Nobutada vs Hideyoshi monogamy attribution (folio 10); the
  fortress-burning verb in Tamo's backstory (folio 13); the ten-member
  wood/earth/man escape lists (folio 17); the Koichi / Higashi-Yubune identity
  (folio 49). Every proper name, unit number, and date was read off the image.

### Parity / number checks (declared exception, with reason)
- `data/zh/` and `data/txt/` are gitignored (copyrighted source, never shipped).
  The assembled `data/zh/ch01.txt` is raw vertical-JP OCR whose paragraph
  segmentation (blank-line based) over-splits at furigana artifacts and page
  boundaries: 423 OCR "paragraphs" against 328 true print paragraphs read from
  the images. Positional bilingual pairing and `check_numbers` against this OCR
  side are therefore NOT meaningful and were not used as a gate. Fidelity was
  instead guaranteed by direct image reading plus targeted crop-verification of
  every name, number, and date. This is the honest posture for this book; if a
  later batch adapts the OCR pipeline for vertical Japanese, revisit.

### Figures
- None. This chapter's scan carries no photographs, plates, or line diagrams
  (it is unbroken body text). Recorded here as a deliberate empty figure list.

### Source inconsistencies noted, NOT harmonized (rendered as printed)
- Hattori Hanzo's age: folio 29 gives 42 ("going on forty-two"), folio 32 gives
  41. Rendered as printed at each spot; a one-year slip, left visible, not
  footnoted (the minor-discrepancy tier).
- "Padre Francisco Frois" (folio 25): the chronicler is usually Luis Frois. The
  differing given name is footnoted, not corrected.
- "Dutch pirates" in the arms trade (folio 67): an anachronism or loose usage;
  in 1582 the sea-traders were Portuguese and Spanish. Footnoted, not corrected.

### Note-density and the "NOT re-noted (already placed)" list
Density is front-loaded on the reference-heavy opening (the 1582 political frame
and the ninja-history digressions) and tapers naturally through the
character/comedy stretches (Etegi, Hatsuko, Karasumaru), which is healthy for
this material. Recurring subjects were noted at first appearance and
cross-referenced, not re-noted, thereafter: Nobunaga, Hideyoshi, Ieyasu, the
Ikko sect / Ishiyama war, the Tensho Iga War (placed on the Momochi-fort note),
Kashii, the jonin/chunin/genin ranks, the traditional units (shaku/sun/ri/cho/
ryo on one note; kan on another), and the author-as-interested-witness lens
(placed on the "first seize the soul" note, revisited only where the author's
intrusions are themselves the subject: the Special Higher Police line, the
socialist-Japan aside, the woman-in-bondage aside).

### Environment note
`setup.sh` installed the render/OCR stack and the jpn + jpn-vert packs cleanly.
One checker regression test fails: "hook stands down on template stub"
(kickoff_guard placeholder stand-down). It is a template-maintenance corner
case; the two cases that matter for a real batch reply both pass ("hook blocks
kickoff-less wrap-up", "hook passes compliant wrap-up"). PaddleOCR not installed
(expected).
