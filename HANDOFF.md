# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs to start Batch 1 cold.

## Message to paste into the next chat

```
Zhou Enlai B01

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 1 =
前言 (ch00) + 中央特科的诞生 (ch01), PDF 35-37 and 44-58, printed: 前言 pp.1-3
(its own sequence) and ch01 pp.1-15. Work on branch claude/zhou-enlai; expect a
stray per-task branch and consolidate onto it (CLAUDE.md rule 2).

This is Batch 1, so it is ALSO the first-chapter voice gate (Step 0c): there is
no previous unit to read for the voice — ch01 SETS the reference voice for the
whole book. Translate it to the standard in STYLE.md, then STOP at the voice
gate and present it for approval; do NOT roll on to Batch 2.

Run the pipeline end to end per CLAUDE.md:
- FIRST engineering task: measure this book's body-text box and configure
  ocr_crop.py, then validate by OCR that no running-head column bleeds into the
  text (running head is the book title / chapter title centred at the top;
  folio in the bottom outer corner). Model chi_sim, psm 6 (simplified,
  horizontal). Second read via ocr_dual.py.
- Verify ch01's opener folio (printed 1 = PDF 44) and each section folio against
  the scan before translating. Body offset is a constant printed = pdf - 43;
  the preface runs its own sequence (printed 1 = PDF 35). The TOC (PDF 38-43)
  sits between preface and body and is NOT translated.
- Crop-verify every name, number, alias, and low-confidence span BEFORE writing
  (verify_names.py --auto for the OCR-disagreement spans; build the per-book
  mangle map). Record fixes via apply_fixes.py.
- Write out/ch00_reading.md and out/ch01_reading.md, one paragraph per source
  line, headings as ###. Fold the front-matter photo-plate captions relevant to
  ch01 into figures.json with real alt text.
- verify_unit.py per unit; check_align.py, check_content.py; footnotes and
  glossary via apparatus_merge.py (check_apparatus.py clean); numbers with
  --noise data/noise.txt.
- Footnotes at reader-model density (a Westerner with no background in the
  Republican-era Chinese underground): the Special Section and its branches,
  the White Terror, the Concessions and their police, 四一二/九一八, and every
  person at first appearance. Put fact-check verdicts in the note; never source
  LLM content.
- Cite the book's own PRINTED FOLIO in notes, never the PDF page.
- NEVER invent bridging text; if OCR cuts off, crop the scan and read the real
  continuation. Verify the final paragraphs of each unit against the scan.
- Build the cumulative EPUB, qa_epub.py green (epubcheck at /tmp/epubcheck-5.1.0
  if still present), check_register.py sets the frozen reference from ch01.
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey session (Step 0a/0b): complete and APPROVED.** Metadata + full
  28-unit / 92-section structure in book.json, recovered from the printed 目录
  and verified folio by folio. Skeleton EPUB builds; qa_epub PASS; epubcheck
  5.1.0 clean. Batching approved as proposed (18 batches; see out/SURVEY.md).
- **STYLE.md written** (the prose contract; read it every batch). Adapted from
  the collection's fiction style sheets to this Chinese partisan nonfiction:
  Chinese-specific translationese tells, enrichment OFF, partisan-source
  discipline (render the slant faithfully; fact-check verdicts go in the note),
  quoted-document handling.
- **Environment:** setup.sh run; chi_sim installed; PaddleOCR absent
  (ocr_dual.py substitute); epubcheck fetched to /tmp/epubcheck-5.1.0.

## Tooling in place / do not revert

- book.json drives the whole build. Deliverable is out/zhou-enlai.epub.
- data/figs/cover.png is the book's own front cover (byte-copied by the
  builder; do not run it through the figure pipeline).
- Nothing else patched yet. The OCR crop box is NOT yet configured — that is
  the first task of Batch 1.

## Renderings settled so far (checked against authority.json)

- 周恩来 Zhou Enlai · 陈赓 Chen Geng · 顾顺章 Gu Shunzhang · 蒋介石 Chiang
  Kai-shek (all confirmed against the shelf). 中央特科 = the Central Special
  Section. Aliases to keep straight: 王庸 = Chen Geng, 伍豪 = Zhou Enlai,
  曾培鸿 = Li Qiang, 化广奇 = Gu Shunzhang, 鲍君甫 = 杨登瀛 Yang Dengying.
- Everything else is decided in glossary.json as it comes up, one rendering per
  referent; feed new decisions back into authority.json at the end.

## Voice sheets (carry-forward; fill as characters first speak)

- _(none yet — Batch 1 establishes the principal voices: Zhou Enlai, Chen Geng,
  Li Kenong, Gu Shunzhang, and Mu Xin's own authorial voice.)_

## Where the story stands

Nothing translated yet. The book opens (ch01) with the political rationale for
Party intelligence work (the White Terror after 1927, 知己知彼 from 孙子兵法) and
the founding of the Central Special Section in Shanghai.

## Exact next-batch scope

- **B01** = ch00 (前言, PDF 35-37) + ch01 (中央特科的诞生, PDF 44-58, printed
  1-15), with sections ch01s01-ch01s03. Ends at the Step 0c voice gate.
- Then B02 = ch02-ch03, per out/SURVEY.md.

## Open traps / environment state

- OCR crop box unmeasured (first B01 task); validate the crop by OCR.
- Running foot may not exist; running head is the title line at top. Folio in
  bottom outer corner — profile the SAME crop the OCR sees, or the last body
  line can be silently deleted.
- Body offset constant 43; do not assume drift, but read the folio at each
  opener anyway.
- Front-matter plate captions (PDF 3-34) are figure material; pull the ones
  tied to ch01 people as those people first appear.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract
  must read 0 after a run.
