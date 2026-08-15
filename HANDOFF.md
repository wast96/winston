# HANDOFF — The Sword Roars in the West Wind (剑吼西风：中央特科纪事)

The baton. A fresh session reads this and starts immediately. This file is the
ARCHIVE of the kickoff; the kickoff is DELIVERED in the chat, pasted verbatim.

## Message to paste into the next chat

```
Sword Roars B01

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2). Run ./setup.sh first.

Do Batch 1 = Chapter One, "No Concealment, No Survival" (ch01), PDF 16-49,
printed 1-34, end to end per the pipeline in CLAUDE.md. It has four sections
(ch01s01..ch01s04); the source is simplified Chinese, horizontal, OCR with
chi_sim --psm 6, and the printed-to-PDF offset is a constant 15 (printed =
pdf - 15) with no plate drift — but still read each opener's folio off the scan.

This is the VOICE GATE chapter (Step 0c): after translating, run the
blind-critique evolution loop (up to 3 rounds), fold every lesson into
STYLE.local.md, then STOP and present the built chapter to the commissioner for
the voice / note-density / formatting gate. Do NOT continue to Batch 2. On
approval this chapter becomes the frozen register reference for the whole book.

Cite printed folios in notes, never PDF pages. Never invent bridging text: if
the OCR breaks mid-sentence or a leaf is damaged, crop the scan and read the
real continuation, or footnote the gap. Verify every name, number and
low-confidence span against a magnified crop before writing. Consult
authority.json for shelf-wide name renderings (Chiang Kai-shek, Zhou Enlai,
Gu Shunzhang, Chen Geng, "the Central Special Branch" are already set).

Deliver the built EPUB attached in the chat, and paste the Batch 2 kickoff
(or, for this batch, hold at the voice gate) verbatim in the same reply.
```

## What is DONE (do not redo)

- **Survey session.** Source characterized; `book.json` fully populated
  (18 units: Preface + 15 chapters/86 sections + Works Cited + Afterword);
  `STYLE.md`/`STYLE.local.md` composed; skeleton EPUB built, qa_epub PASS,
  epubcheck clean. Cover extracted (`data/figs/cover.png`) and embedded. No
  translation yet. See PROGRESS.md "Setup / Survey".

## Tooling in place (do not revert)

- OCR model decided: `chi_sim --psm 6` (simplified, horizontal). Second read:
  `ocr_dual.py` (PaddleOCR is not installed; expected). `OMP_THREAD_LIMIT=1`.
- Page offset: constant **15** (printed = pdf − 15) book-wide, no drift, no
  unpaginated plates. Verified on all 335 body pages.
- Crop box: NOT yet measured. First engineering task of Batch 1 — measure the
  body-text box and configure `ocr_crop.py` (running head is top, folio is the
  outer top corner; crop both away). Validate the crop by OCR.

## Renderings settled this batch / carry-forward

- From authority.json (shelf-wide, use as-is): 蒋介石 Chiang Kai-shek;
  周恩来 Zhou Enlai; 顾顺章 Gu Shunzhang; 陈赓 Chen Geng; 中央特科 the Central
  Special Branch.
- Provisional (decide in glossary at first appearance, then reuse): 钱壮飞
  Qian Zhuangfei, 李克农 Li Kenong, 胡底 Hu Di (the "Longtan Three Heroes"
  龙潭三杰); 徐恩曾 Xu Enzeng; 向忠发 Xiang Zhongfa; 陈云 Chen Yun; 白鑫 Bai Xin;
  贺稚华 He Zhihua; 沈琬 Shen Wan; 杨登瀛 Yang Dengying.
- Title 剑吼西风 = "The sword roars in the west wind", a line from He Zhu's ci
  六州歌头 (the p5 epigraph). Rendered "The Sword Roars in the West Wind".

## Voice sheets (one per major character)

- (none yet; write the first at Chapter One's first major character.)

## Where the book stands

- Nothing translated. Chapter One introduces the Central Special Branch's world
  and (per its section titles) a "man of a thousand faces" — likely Qian
  Zhuangfei or the conjuror motif that recurs (魔术 threads through chs 1 and 8).

## What is NEXT

- Batch 1 = Chapter One (ch01), PDF 16-49, printed 1-34. VOICE GATE — stop for
  approval; do not start Batch 2.

## Open items for the read-through

- Epigraph (He Zhu ci, p5) to be rendered as a front-matter verse page in the
  final batch (verse, {p}).
- Preface, Works Cited, Afterword scheduled for the final (light) batch with
  back matter, whole-book reconciliation, and COMPLETION.md.
- Confirm the proposed batch plan (see out/SURVEY.md and the reply) at the gate.

## Environment / traps state

- PyMuPDF/tesseract/chi_sim(+vert)/chi_tra(+vert) installed; epubcheck 5.1.0
  available (java present). PaddleOCR NOT installed (expected) — use ocr_dual.py.
- Branch: survey work committed on the harness's stray branch
  `claude/pdf-source-review-kehwvb`; canonical book branch per CLAUDE.md rule 2
  is `claude/the-sword-roars`. Consolidate onto the canonical branch (see reply).
- Clean scan, no seal, constant offset — the usual furniture traps are mild here,
  but the crop still must be measured and OCR-validated in Batch 1.
