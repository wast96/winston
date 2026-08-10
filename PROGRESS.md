# PROGRESS — The Gangs of Old Shanghai (旧上海的帮会)

Running per-batch log. Written as work happens, not at the end.

## Setup (session 1)

- **Source.** `source.pdf` = the uploaded scan, 391 pages, image-only (no text
  layer; producer FreePic2Pdf/Pdg2Pic). Simplified Chinese, horizontal.
  Cover carries a library seal and a signature (朱学范, the title inscription);
  title page carries accession no. 124054 and a Shandong Normal University
  library stamp. Copyright page (pdf 3): 上海人民出版社, printed 上海新华印刷厂,
  出版日期 1986年8月, 定价 2.90 元, 上海市报刊登记证第424号.
- **Attribution decided.** This is an ANTHOLOGY (26 memoir/study articles +
  editorial note + preface + 2 appendices), compiled by 中国人民政治协商会议上海市
  委员会文史资料工作委员会. Cataloged to that committee as corporate author/editor
  (`author_en`). Zhu Xuefan (vice-chairman, NPC Standing Committee) contributed
  the opening article and brushed the cover title; Wei Jianyou (history prof.,
  Shanghai Normal) wrote the preface. Individual contributors are named per
  article and carried as in-text bylines.
- **Page offset.** printed = pdf − 9, CONSTANT across the whole book (no
  accumulating plates). Verified at anchors: pdf 6=序言 folio 1; pdf 10=body
  folio 1; pdf 38=folio 29; pdf 204=folio 195; pdf 351=folio 342; pdf 376=folio
  367; pdf 378=folio 369; pdf 391=folio 382 (last page, member roll:
  "共三百二十四人"). Re-verify each opener's folio at its batch anyway.
- **Environment.** `setup.sh` green: tesseract 5 + chi-sim/chi-sim-vert/
  chi-tra/chi-tra-vert. PaddleOCR NOT installed (expected) → dual-engine
  substitute is `scripts/ocr_dual.py` (psm 6 / psm 4 / inverted). epubcheck
  5.1.0 available (java present). Checker regression tests: green.
  `OMP_THREAD_LIMIT=1` exported.
- **Front matter.** 编辑说明 pdf 4–5 (own folios 1–2, dated 1986年4月); 序言 by
  魏建猷 pdf 6–7 (own folios 1–…); 目录 pdf 8–9. Body pdf 10 onward.
- **Page furniture (to configure at B01).** Body text box + running foot/folio
  crop NOT yet measured; do it as the first engineering task of B01 and record
  the crop box here. Folio sits centered at the foot as `• N •`.

## Step 0 gates

- **0a metadata:** done in `book.json` (title, author/editor, translator
  "Winston", series "Winston Translations" #10, subjects, description,
  translator_note, source_ref, pdf_end/printed_end, modified fixed).
- **0b survey:** `out/SURVEY.md` generated; 28 units in 9 parts; skeleton EPUB
  built (`out/gangs-of-old-shanghai.epub`), `qa_epub` PASS, epubcheck 0/0.
  Refined 10-batch plan written to `book.json`. **Awaiting commissioner
  approval before Batch 1.**
- **0c voice gate:** pending (after B01).

## Glossary seeded (from authority.json)

Principal cast + core terms only, to make the skeleton's Principal Characters
page representative. Renderings taken from the cross-book ledger where present:
Du Yuesheng, Huang Jinrong, Zhang Xiaolin, Dai Li (attested); Gu Zhuxuan, Zhang
Renkui (provisional); Green Gang (青帮), the Hongmen (洪门, attested), Heng
Society (恒社), Ren Society (仁社), the gangs (帮会).

- **军统 is a live cross-shelf RECONCILE** (COLLECTION.md): three prior renderings
  (Military Statistics Bureau / the Juntong / Juntong). Seeded here as "the
  Juntong" but the binding decision + authority.json reconciliation is deferred
  to B08 (ch21, 杜月笙与戴笠及军统的关系), the article that leans on it.

## Batches

- **B01 DONE (ch01–ch04, printed 1–28)** — pending the voice-gate approval.
  - Units: ch01 Editorial Note (5 paras), ch02 Preface / Wei Jianyou (8), ch03
    Zhu Xuefan, "A Few Notes on the Shanghai Workers' Movement and the Gangs"
    (42, three parts + five subsections), ch04 Wu Chengfang, "Fragmentary
    Materials..." (18).
  - Notes: 43 (ch01 2, ch02 6, ch03 19, ch04 16). Continuous book-wide numbering
    by the builder. Glossary: 33 rows (people 24, orgs 8, terms 1).
  - Checks all green: parity 5/8/42/18 = OK; check_numbers 0 unresolved (see the
    noise + digit notes below); check_apparatus 0/0; qc_entities 0 misses;
    check_align OK (ch02's short "April 1986" dateline is the one expected
    short-pair flag); check_content OK; qa_epub PASS (43 ref/body/backlink);
    epubcheck 0/0.
  - **Register:** ch03/ch04 are expository memoir with almost no dialogue
    (0.0 contractions/1k), so the dialogue-contraction metric is not meaningful
    yet. The dialogue-register REFERENCE should be set from the first
    dialogue-heavy chapter (a Huang Jinrong / Du Yuesheng memoir, B04+), not
    from B01. Noted so drift-checking measures against a real dialogue baseline.
  - **Paragraph structure:** built by hand from the OCR + scan, because this
    scan defeats the geometric indent detector (see Setup). zh source files in
    data/zh are reconstructed clean (numbers verified) and segmented to match
    the English 1:1.
  - **Number-check accounting:** event/movement date-names (八一三 一二八 一二九
    四一二 五卅 七七), the pricing idiom 八折, decade labels, and numeral-bearing
    proper names (李立三 万邦和 王懂百 九江路 万里浪 王震百) are in data/noise.txt.
    Genuine large quantities are written as digits in the English so the check
    can verify them.
  - **Tail-verified** (rule 4 corollary): ch04's true last line is "…很有帮助的。"
    — strip_folio had eaten the one-character line "的。" as if it were a folio;
    restored. Watch short one-glyph closing lines each batch.

## Voice-gate revision (round 1)

Commissioner read to printed p.12 and rejected the prose as clunky and stilted:
faux-period formality, inversions (&#8220;needed all the more someone&#8230;&#8221;), calque
idioms (&#8220;lay hands on that pension,&#8221; &#8220;have a voice put in for them&#8221;), and
inconsistent number styling (&#8220;sixty-eight&#8221; beside &#8220;2,400&#8221;). RECALIBRATED the
whole batch to natural contemporary English: removed inversions and archaisms,
broke run-ons, fixed the flagged phrasings, dropped the confusing &#8220;twenty-fourth
part,&#8221; and adopted ONE number rule &#8212; digits for specific quantities (counts,
ages, years of service, sums, percentages), words only for rounded/rhetorical
ones. ch03 and ch04 rewritten in full; ch02 preface lightly de-flowered (its
scholarly register kept); ch01 already clean. Note anchors re-pointed to the
new prose (7 anchors updated); all checks re-run green. This natural register
is the standard for the rest of the book.

## Tooling patches this project (do NOT revert)

- `ocr_crop.py`: added `folio_present()` (was referenced by indents.py but never
  defined — crashed every book). Geometric folio test; kept in lock-step with
  `indents.line_starts`.
- `indents.py`: documented that geometric indent detection is bypassed on this
  scan (speckle + tight lines break band↔OCR-line alignment); assembly uses the
  blank/short-line fallback.
- `check_numbers.py`: added 〇 (ideographic zero, U+3007) to CN_DIGIT and the
  extraction class, so years like 一九四〇 read as 1940; guarded the built-in
  `一一` ("one by one") rule with a lookahead so it no longer eats the head of a
  compound like 一一七 (117 → orphan 7).
- `apparatus_merge.py`: made the glossary merge SECTION-aware (rows carry an
  optional `section`, default `terms`; dup-check spans all sections). It had
  merged rows flat at the top level, which broke render_glossary and duplicated
  戴笠.
- `check_content.py`: skip `_`-prefixed / non-dict glossary keys in name_map
  (it crashed on the `_about` string).
- **Measured OCR crop** (this book): `--left 0.06 --right 0.91 --top 0.09
  --bottom 0.89 --lang chi_sim --psm 6`. Folio at the foot centre (`• N •`),
  cropped out. No running head.
