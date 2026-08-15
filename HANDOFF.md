# HANDOFF — China's Secret War (中国秘密战)

Survey complete and approved. This hands off to Batch 1. A fresh session starts
each batch by pasting the kickoff below into a new chat.

## Message to paste into the next chat

```
China's Secret War B01

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B01 = Preface (ch00) + Chapter 1 (ch01), end to end per the CLAUDE.md
pipeline. PDF pages 33-81; printed pages: Preface 1-3 (its own front-matter
sequence, PDF 33-35), Chapter 1 printed 1-45 (PDF 37-81). Body offset is
constant: printed = pdf - 36 (verified). Simplified Chinese, horizontal;
chi_sim, psm 6; PaddleOCR absent, use scripts/ocr_dual.py and say so in
PROGRESS.

This is the FIRST content batch, so there is no previous unit's English to read
for the voice; instead your first engineering task is the page furniture:
measure the body text box and configure scripts/ocr_crop.py to crop the
vertical running title in the outer margin (verso: left; recto: right) and the
bottom folio before OCR. Validate the crop by OCR (a bad right/left bound makes
the running head appear as a spurious column). Then render -> ocr_crop ->
ocr_dual -> indents -> assemble -> find_figures (eyeball for line art; the
图文版 has many inline photos with vertical outer-margin captions, crop and OCR
those) -> translate to out/ch00_reading.md and out/ch01_reading.md (one
paragraph per source line) -> verify_unit / check_align / check_content ->
apparatus_merge for notes and glossary (this book has a partisan apparatus:
footnote the invisible logic and state corroborated/uncorroborated/contradicted;
seed the Principal Characters cast: Zhou Enlai, Chen Geng, Gu Shunzhang, Kang
Sheng, Chiang Kai-shek, Dai Li, and the "Longtan Three") -> build the cumulative
EPUB -> qa_epub (green) and epubcheck -> check_register (this unit BECOMES the
frozen reference) -> write PROGRESS and the next HANDOFF/kickoff -> commit.

Also: run scripts/detect_notes.py early to characterize the book's own source-
note apparatus (interview citations clustered near printed 391-394) so the plan
for reproducing it is set before later batches. Cite the book's PRINTED folios
in notes, never PDF pages. Never invent bridging text: if OCR cuts off, crop the
scan and read the real continuation. Verify every name, number, and unit
designation by crop before writing.

Do NOT pause for approval mid-batch. B01 is special: it ENDS at the first-chapter
voice gate (CLAUDE.md Step 0c). When B01 is done, STOP and present the built
chapter for the commissioner to judge voice, note density, and formatting; do
not begin B02. Deliver the EPUB in chat and paste the B02 kickoff verbatim in
the same reply.

Work on branch claude/chinas-secret-war only (CLAUDE.md rule 2); expect a stray
per-task branch at session start and consolidate onto the canonical branch.
```

## What is DONE

- **Survey (Step 0a + 0b), approved.** book.json carries full EPUB metadata and
  the complete structure: 12 chapters, 86 numbered sections, plus Preface
  (前言 探秘, ch00) and Afterword (后记, ch13). English chapter/section titles
  drafted (refine as you translate). Batch plan (13 batches) in book.json
  `batches`; outline in out/SURVEY.md.
- **Skeleton EPUB** builds green: qa_epub PASS, epubcheck 0 errors/0 warnings.
- **STYLE.md** written (the prose contract; read it every batch).
- **Branch** consolidated onto claude/chinas-secret-war; stray deleted.

## Tooling in place (do NOT revert)

- `scripts/gen_book_json.py` records the structure and the offset (printed =
  pdf - 36) with its four verification anchors. If the structure needs editing,
  prefer editing book.json directly now that it exists.
- Nothing else patched yet. ocr_crop.py still needs THIS book's crop box
  (Batch 1's first task). The dual-OCR substitute (ocr_dual.py) is the engine;
  PaddleOCR is absent.

## Renderings settled this batch

None yet. glossary.json is empty. Consult authority.json BEFORE romanizing any
name that the shelf may already have decided (Dai Li / 军统 / the Shanghai
institutions carry live cross-book renderings). Feed decisions back on
completion. Start the per-character VOICE SHEETS in the carry-forward section
below as characters first speak (Mao, Zhou Enlai, Kang Sheng, Chiang Kai-shek,
gangster and cadre voices will all recur).

## Where the story stands

Nothing translated yet. Chapter 1 opens with the 1927 Nationalist terror and the
birth of the CCP's first intelligence and security cells (the 军委特务工作科 and
then the 中央特科 under Zhou Enlai), the Gu Shunzhang defection and the "Longtan
Three," the State Political Security Bureau, the Soviet-area purges, and the road
to a foothold in northern Shaanxi. The Preface (探秘) is the author's framing
essay on why China's secret war is the deepest secret of all.

## Open traps and environment

- Page furniture: vertical running title in the OUTER margin (verso left, recto
  right); bottom-outer folio. Crop before OCR. First batch's first task.
- The 图文版 has many INLINE photos on numbered body pages (not separate plate
  sequences), which is WHY the offset stays constant at 36. Captions are often
  vertical in the outer margin: crop and OCR them; never invent an ID.
- The book has its OWN source-note apparatus (author's interview citations);
  characterize with detect_notes.py, decide reproduction before later batches.
- Contested-history book: partisan voice is content (see STYLE.md interested-
  witness doctrine); apparatus states corroborated/uncorroborated/contradicted;
  never source LLM-generated content (CLAUDE.md rule 5).
- Environment: tesseract chi_sim/chi_tra installed; epubcheck 5.1.0 fetched;
  regression tests green; OMP_THREAD_LIMIT=1 mandatory for tesseract (kill the
  process GROUP; pgrep -c tesseract must read 0).
- book.json section opener pdf pages are computed (printed+36); spot-verify each
  opener's folio off the scan at batch time (an inline full-page plate can nudge
  one by +-1).
