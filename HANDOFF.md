# HANDOFF — The Gangs of Old Shanghai (旧上海的帮会)

The baton. A fresh session reads this and continues. **At the voice gate right
now:** Batch 1 is built and delivered; the project is STOPPED for the
commissioner to judge voice, note density, and formatting before the rest of
the book follows. Do not start Batch 2 until that approval comes; on approval,
ch03 becomes the FROZEN register reference and the real Batch 2 kickoff gets
written into the block below.

## Message to paste into the next chat

```
(First line: the project label and batch, e.g. "Gangs of Old Shanghai B02",
then a blank line. Then the kickoff body per CLAUDE.md: read CLAUDE.md,
HANDOFF.md, book.json; do batch B02 = ch05–ch06 (Green Gang origins: Li Shiyu
+ Jiang Hao), PDF 38–76, printed 29–67, end to end per the pipeline; BEFORE
translating, read the final two pages of ch04's English (the voice); cite
printed folios; never invent bridging text; do not pause for approval; deliver
the EPUB in chat and paste the next kickoff. — Written only AFTER the voice
gate is approved.)
```

## What is DONE (do not redo)

- Step 0a metadata + 0b survey: book.json full 28-unit structure, 10-batch plan,
  skeleton EPUB, SURVEY.md. Approved.
- **B01 (ch01–ch04, printed 1–28):** editorial note, preface (Wei Jianyou),
  Zhu Xuefan's workers'-movement memoir, Wu Chengfang's underground-work memoir.
  43 notes (running total 43), 33 glossary rows. All checks green, qa_epub PASS,
  epubcheck 0/0. See PROGRESS.md for the per-check detail.

## Tooling in place (do not revert) — see PROGRESS.md for the full list

- ocr_crop `folio_present()` added; measured crop `--left 0.06 --right 0.91
  --top 0.09 --bottom 0.89 --lang chi_sim --psm 6`.
- Geometric indent detection is BYPASSED on this scan (speckle); assembly uses
  the fallback and paragraphs are fixed by reading. zh files are hand-built to
  match the English 1:1.
- check_numbers: 〇 zero added; `一一` compound-guard added.
- apparatus_merge: glossary merge is section-aware (rows carry `section`).
- check_content: skips `_`-prefixed glossary keys.
- data/noise.txt carries this book's event-names, idioms, numeral-bearing names.

## Renderings settled this batch / carry-forward

- Shelf-agreed (authority.json): Du Yuesheng, Huang Jinrong, Zhang Xiaolin,
  Dai Li, Chiang Kai-shek, Zhou Enlai, the Green Gang (青帮), the Hongmen (洪门).
- Decided this batch (in glossary.json): Zhu Xuefan, Lu Jingshi, Li Lisan, Yang
  Du, Li Dazhao, Zhao Puchu, Wang Jingwei, Feng Yuxiang, Xiang Haiqian
  (= Xiang Songpo), Zhang Kechang, Jin Tingsu, Zhang Shizhao, Wen Lanting,
  Wu Chengfang, Hu Egong, Weng Wenhao; the Yi Society (毅社), the Chang Society
  (畅社), the Heng Society (恒社), the Ming Society (铭社), the Special
  Operations Corps (别动队).
- **军统 still UNSETTLED shelf-wide** (Military Statistics Bureau / the Juntong).
  Seeded "the Juntong"; the binding decision + authority.json reconcile happen
  at B08 (ch21). Do not use 军统 in prose before then without deciding.
- Provisional readings flagged in notes: Dai Xiaodong (戴晓东, the 互济会 head),
  Qiu Zipei (邱子佩), Chen Junyi (陈君毅). Re-check if better sources surface.
- Event-name renderings: the May Thirtieth Movement (五卅), the January
  Twenty-Eighth Incident (一二八), the Battle/resistance of August Thirteenth
  (八一三), the April 12 coup (四一二), the December Ninth student movement (一二九),
  the July Seventh war (七七), the "solitary island" (孤岛).

## Voice sheets

- **Narrators are the register.** B01 is expository memoir, not dialogue.
  ZHU XUEFAN (ch03): an educated union organizer looking back from inside the
  establishment; measured, factual, quietly candid about the transactional use
  of the gangs; long marshalled sentences, dates and figures exact. WU CHENGFANG
  (ch04): a Party underground worker; drier, more clipped, catalogues names and
  operations. Keep both plain and unstilted; no antique diction. The preface
  (Wei Jianyou) is a scholar's register — dignified, a shade more formal — and
  is legitimately distinct.
- Dialogue voices will be written when the first dialogue-heavy memoir arrives.

## Where the book stands

- The two framing memoirs are done: how a Nationalist labour boss (Zhu) and the
  Communist underground (Wu) each USED the gangs. Du Yuesheng is established as
  the pivot both depend on. Next the book turns to the gangs' own history
  (Green Gang / Hongmen origins), then to the big bosses.

## What is NEXT

- After voice-gate approval: B02 = ch05–ch06, PDF 38–76, printed 29–67.

## Open items for the read-through

- Provisional name readings above. The ch03 open letter (Chang Society) names
  "one Shen and one Dai" (沈某、戴某) — left as the source has them.
- Liu Shanben's defection: book says 1947, standard accounts say June 1946 —
  footnoted as a likely memory slip.

## Environment / traps state

- setup.sh green; PaddleOCR absent (dual-tesseract used); epubcheck available.
- OMP_THREAD_LIMIT=1. Watch one-glyph closing lines (strip_folio can eat them).
- Stray per-task branch expected at each batch start; canonical branch is
  claude/gangs-of-old-shanghai.
