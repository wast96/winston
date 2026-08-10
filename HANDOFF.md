# HANDOFF — The Gangs of Old Shanghai (旧上海的帮会)

The baton. A fresh session reads this and continues. **Voice gate PASSED** (the
commissioner approved the revised B01 voice on the second pass). ch03 is now the
FROZEN register reference: measure every later unit with
`check_register.py --ref out/ch03_reading.md`. The natural contemporary-English
voice of the revised B01 (see the voice-gate revision note in PROGRESS.md) is
the standard for the whole book. B02 is in progress.

## Message to paste into the next chat

```
Gangs of Old Shanghai B02

Read CLAUDE.md, then HANDOFF.md, then book.json. Do batch B02 = ch05 (青帮早期组织考略,
Li Shiyu) + ch06 (青帮的源流及其演变, Jiang Hao), PDF 38–76, printed 29–50 and 51–67,
end to end per the pipeline. This scan defeats geometric indent detection, so
assemble from the fallback and hand-build the zh files to match the English 1:1
(see B01). BEFORE translating, read the final two pages of ch04's English and skim
ch03 — that natural voice is the frozen reference; no stilted/period register,
digits for specific quantities. ch05 is a scholarly paper with the AUTHOR'S OWN
numbered footnotes/citations (captured at each page foot in the OCR): reproduce
them as author-attributed notes, distinct from translator notes. Green Gang lore
is dense (前三祖/后三祖, the 24-generation characters, 漕运 grain transport, 罗祖/罗教,
翁潘钱); consult authority.json before romanizing, keep 军统 unsettled until B08.
Cite printed folios; never invent bridging text; do not pause for approval;
deliver the EPUB in chat and paste the next kickoff.
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
