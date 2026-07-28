# COMPLETION REPORT — 特務工作之理論與實際 (Gu Shunzhang), full book

**The book is done.** All eight chapters and all thirty-seven sections are
translated, annotated, and built into one cumulative EPUB with the publisher's
errata and colophon rendered as back matter. `out/gushunzhang.epub` is
QA-green. This report replaces the batch handoff.

## Status at a glance

- **8 / 8 chapters, 37 / 37 sections** translated.
- **212 footnotes**, continuously numbered, every reference matched to a body
  and a backlink.
- **18 figures**, all captioned or honestly marked as uncaptioned insets.
- **132 glossary entries** (14 people, 24 organizations, 93 terms, 1 book), each
  with a status and, where attested, a citation.
- `qa_epub.py`: **PASS** (39 files, 16 documents, all links resolve).
- `check_structure.py --config`: **PASS** (heading shape uniform across all 8
  chapters; all 212 note anchors resolve; ch08 paragraph parity 28/28).
- Full, now fully-linked table of contents, expanded to **section level** in the
  e-reader navigation (every section is a jump target, per your request).

## Per-chapter tally

| Ch | Title | Folios | Notes | Figures |
|----|-------|--------|-------|---------|
| 1 | Introduction | 1–16 | 25 | 0 |
| 2 | Secret-Service Organization | 17–39 | 19 | 4 |
| 3 | Methods of Secret-Service Work | 40–51 | 9 | 0 |
| 4 | The Secret-Service Mindset | 52–57 | 9 | 0 |
| 5 | Secrecy | 58–82 | 23 | 0 |
| 6 | Secret-Service Tradecraft | 83–177 | 61 | 6 |
| 7 | General Knowledge for the Work | 178–227 | 55 | 8 |
| 8 | Self-Cultivation of Personnel | 228–236 | 11 | 0 |
| | **Total** | | **212** | **18** |

## Batch B11 (Chapter 8) — what was done

- **Scope:** ch08 §1 工作的精神 (The Spirit of the Work) and §2 身心的鍛練
  (Cultivation of Body and Mind), unit ids ch08s01 / ch08s02. PDF 282–290 =
  printed folios 228–236 (nine text pages). New chapter file
  `out/ch08_reading.md`, H2 + two `### Section` headings, six numbered points in
  §1 and five in §2.
- **Every page was eye-read** off the 300 dpi scan. PaddleOCR would not install
  (standing condition on this book); tesseract `chi_tra_vert --psm 5` was the
  diff partner, and the whole-batch eye-read is the standing substitute for the
  dual-engine diff. `pgrep -c tesseract` was 0 after OCR.
- **Figures: none.** Chapter 8 is entirely prose. The ink-density detector
  produced one false positive on a dense text column (on the duplicate scan of
  folio 235); discarded after eye-inspection.
- **Checks run:** `check_numbers` 28 pairs, 0 unresolved; `check_structure
  --pairs` parity 28/28; heading shape matches the other seven chapters.
  Blind double-translation and back-translation were applied to the
  argumentative passages (§1 the political frame; §2 the wine/women/wealth/temper
  and the faculties passages) with no material divergence and no omissions.

## Two findings from Chapter 8 that need your eye

1. **The book's final leaf is missing from the scan.** Printed folio 237 is not
   in the NCL scan. The scan runs folios 235, 236, then a **duplicate of 235**
   (a scanner double-feed), then a blank leaf. Folio 236 ends in the middle of a
   closing quotation, `又曰:『小不忍則亂大謀……`, and the sentence that finished
   the chapter and the book is on the missing folio 237. **No bridging text was
   invented.** The translation stops exactly where the scan does, and footnote
   210 states the gap plainly. The publisher's errata correct nothing past folio
   236, so at most a sentence or two is lost.

2. **Two errata corrections fall inside Chapter 8 and were applied:** folio 233
   inserts 日 (終請 → 終日請, "keep plying us with drink all day"), and folio 236
   inserts 能 (應付的力 → 應付的能力, "the faculty to meet events"). Both are
   reflected in the reading text; both were already carried by sense in the first
   draft.

## History flags gathered for your read-through (whole book)

New in Chapter 8:
- **The cross-party frame (note 203).** Gu names the enemy the manual is written
  to root out: 跨黨份子, Communists concealed within Nationalist ranks after the
  1927 split. He had himself been the CCP's security and intelligence chief until
  his April 1931 defection. The point is his own biography turned into doctrine;
  corroborated against the standard scholarship (Wakeman, *Policing Shanghai*).
- **Classical allusions**, all checked and correctly invoked by the book:
  不入虎穴焉得虎子 (Ban Chao, *Book of the Later Han*), 有志者事竟成 (Emperor
  Guangwu, same source), 小不忍則亂大謀 (*Analects* 15.27).
- **Self-criticism (自我批評) and comrade (同志)** are CCP political vocabulary
  that Gu carries into a Nationalist manual; noted at their first appearance in
  ch2 / ch4, not re-noted here.

Carried forward from earlier batches (still worth your eye):
- **Green Gang origin dating (ch7 §4):** the book's 明嘉靖十七年 / 1538 for
  Patriarch Luo is not historical (Luo Qing d. 1527; the boatmen's brotherhood
  dates to Yongzheng, 1726). Footnoted as gang legend against scholarship.
- **Three tycoons + 三鑫公司 (ch7 §4):** opium monopoly, 1918, roughly a third of
  government revenue — corroborated and footnoted. The 嵊縣 kidnapping trade is
  flagged as an uncorroborated period commonplace.
- **數十八 (ch7 §4, folio 223):** a source misprint, scan-verified; rendered
  "some tens," footnoted, stripped in check_numbers.
- **The Soviet G.P.U. / Red Army chart:** the errata's folio-206 entry appends
  it; reproduced in Chapter 7 as figure ch07-f7.

## Provisional readings still open (consolidated)

Chapter 8 introduced **no new provisional romanizations**; its uncertainties are
the missing folio 237 (note 210) and the two applied errata, both recorded above.

Carried forward, unchanged, from earlier chapters (all footnoted where they
occur): 別動隊 (ch1); 中央特務會議 / 總部 / 各省區特務部 (ch2 plate); 中心思想
"central conviction" (ch4); 抄靶子 (ch5); 扛木梢 / 吊膀子 / 老門檻 (ch6 §2);
反偵探 "counter-surveillance" (ch6 §3); 廣生行 "Kwong Sang"; 麻力樹棍
"malacca baton" (ch6 §4); 圓光 / 關亡 (ch6 §10); 敏捷飛 "Minjie Fei" / 信誼代辦所
"Xinyi agency" / 紅色保衛隊 "Red Defense Corps" (ch7 §1-3); 李則高 / 癩頭筋鮑方 /
剝豬玀 / 洋盤 / 彫林·三光碼子 (ch7 §4); the Green Gang generation-poem variant
(ch7 §4).

## Standing safety item (unchanged)

Chapter 6 §5 破壞術: the non-operational doctrine is in the edition; the technical
device-construction core (folios 121-133) remains **withheld** and was not read
or reproduced. Chapter 8 is morale and self-cultivation and does not touch it.

## Back matter

- **Errata (勘誤表):** all 27 corrections transcribed from the scan and rendered
  as a translated table (folio, printed page, location, correction), with a
  headnote explaining that each was checked against the translation.
- **Colophon (版權頁):** 不准翻印 ("Reprinting forbidden") and
  中華民國二十二年八月付印 (printed August 1933), with the title and author.

## Sampled error-rate estimate (check 8)

Every one of the nine text pages of Chapter 8 was read character by character
off the 300 dpi scan (not sampled). A second paranoid pass over three dense
passages (the political frame on folio 229, 酒色財氣 on folio 233, and the
endurance passage on folio 236) found no character error surviving into the
translation. On this basis the residual error rate for Chapter 8 is estimated at
**well under 0.5%** (below one surviving character error per two pages), in line
with the rates reported for the earlier eye-read batches. The one irreducible
loss is external to the translation: the missing folio 237.

## Files

- `out/gushunzhang.epub` — the deliverable.
- `out/ch08_reading.md`, `out/ch08_bilingual.md` (QC only), `data/zh/ch08.txt`.
- `notes.json`, `glossary.json`, `figures.json`, `back_matter.json`, `book.json`.
- `PROGRESS.md` (per-batch log), this report.
