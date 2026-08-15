# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with this block PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

## Message to paste into the next chat

```
Chen Yangshan B01

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018), a Party biography of a Central Special Branch intelligence officer;
modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is source.pdf
(image-only); run ./setup.sh first. Offset: printed = pdf - 11 (constant).

Do Batch 1 = Chapter 1 "Seeking the Truth, Turning to Revolution" (ch01, its
five sections ch01s01-ch01s05), PDF 12-37, printed 1-26, end to end per the
CLAUDE.md pipeline:
  - render 12-37; MEASURE the crop box and running head/foot with ocr_crop.py
    (position varies recto/verso - verify by OCR) and record it in HANDOFF's
    tooling list; OCR chi_sim --psm 6 + ocr_dual.py second read; verify
    pgrep -c tesseract is 0.
  - indents.py, assemble.py; eyeball every page for figures (chapter-opener
    photo on p12; line art find_figures misses) and record figures.json with alt.
  - Translate to out/ch01_reading.md, one paragraph per source line, headings
    as ###. Crop-verify EVERY name/number/low-confidence span BEFORE writing;
    log fixes via apply_fixes.py. Consult authority.json before romanising
    (Yun Daiying, He Long, Shanghai place names, etc.); decide each rendering in
    glossary.json first. Cite PRINTED folios in notes, never PDF pages. Never
    invent bridging text; verify the final paragraphs against the scan.
  - Footnotes via apparatus_merge.py (reader = Westerner with no China
    background: gloss May Thirtieth Movement, Yun Daiying, He Long, Shangyu/
    Baiguan, 特科, etc.); glossary.json + figures.json.
  - verify_unit.py ch01, check_align.py, check_content.py, check_apparatus.py,
    qc_entities.py, check_numbers.py --noise data/noise.txt. Build the cumulative
    EPUB, qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar).
  - Record everything in PROGRESS.md.

Then, BECAUSE THIS IS BATCH 1, run the Step 0c VOICE GATE: the blind-critique
evolution loop (voice_gate_critique.py prepare -> a fully context-blind fresh
reader -> apply fixes re-verified against the source -> evolve STYLE.local.md;
up to 3 rounds), then STOP and present Chapter 1 to the commissioner for the
human voice/notes/formatting gate. Do NOT proceed to Batch 2. Attach the EPUB
in chat and paste this same kickoff back at the end of your reply.

All work on branch claude/chen-yangshan.
```

## What is DONE (do not redo)

- **Survey session** (this one): full structure in book.json (6 chapters / 29
  sections + 3 appendices + references + afterword + series foreword);
  metadata (Step 0a) set; STYLE.md composed; skeleton EPUB built; qa_epub PASS;
  epubcheck 0/0. No chapters translated yet. Continuous note number: 0.

## Tooling in place (do not revert)

- setup.sh installs tesseract chi_sim/chi_tra (+ vert); PaddleOCR absent -> use
  ocr_dual.py. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar.
- Offset printed = pdf - 11 (constant; verified printed 2 / 27 / 231).
- Crop box: NOT yet measured — Batch 1's first engineering task (ocr_crop.py).

## Renderings settled this batch / carry-forward

- None decided yet. glossary.json is empty. Consult authority.json first for the
  shelf-standard forms (中央特科, 顾顺章, 周恩来, 李克农, 康生, 贺龙, 军统, Shanghai
  streets). Decide each in glossary.json BEFORE romanising.

## Voice sheets (one per major character)

- None yet. Chen Yangshan (陈养山, b. 程仰山/Cheng Yangshan) is the subject; write
  his voice sheet at his first substantial appearance in Chapter 1.

## Where the book stands

- Nothing translated. Chapter 1 opens in Shangyu, Zhejiang, with Chen's birth
  (1906) and boyhood, and his leaving home for Wuhan at thirteen.

## What is NEXT

- Batch B01 = Chapter 1 (ch01, ch01s01–ch01s05), PDF 12–37, printed 1–26.
  Ends at the Step 0c voice gate (do not start Batch 2).

## Open items for the read-through

- English title "Chen Yangshan: Hero of the Secret War" is provisional —
  commissioner may prefer another rendering of 秘战英雄 (metadata only, easily
  changed). Batch plan (10 batches) awaiting approval.

## Environment / traps state

- Front matter runs a SECOND folio sequence (foreword folios 1–2 at PDF 7–8).
- Chapter-opener rectos carry a photograph above the heading.
- PDF p243 is an Anna's Archive metadata leaf, not book content.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process group; pgrep -c tesseract.
