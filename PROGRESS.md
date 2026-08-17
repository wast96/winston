# PROGRESS — China's Secret War (中国秘密战)

The running per-batch log. Written as we go. One section per batch: what was
translated (unit ids, PDF and printed ranges), which checks ran and what they
found, notes added, glossary rows added with status, figures, and anything
flagged for the commissioner's read-through.

## Setup / Survey (Step 0a + 0b)

- **Source:** `source.pdf`, 436 PDF pages, image-only scan, no text layer.
  Internet Archive (archive.org/details/zhongguomimizhan0000unse), scanned from
  a Contra Costa County Library copy. Book: 《中国秘密战：中共情报、保卫工作纪实》
  by 郝在今 (Hao Zaijin), 金城出版社 (Gold Wall Press), Beijing, 最新升级图文版
  (2nd ed., 2015-01). ISBN 978-7-5155-1071-2. 报告文学 (reportage). 330,000
  Chinese chars; 27 print sheets; 710×1000 1/16.
- **Script / orientation:** SIMPLIFIED Chinese, horizontal, left-to-right. Use
  `chi_sim` (psm 6). PaddleOCR not installed (weights host unreachable) — use
  the dual-tesseract substitute `scripts/ocr_dual.py`; note that in each batch.
- **Offset:** CONSTANT `printed = pdf - 36` across the whole body. Verified at
  four chapter openers spanning the book (ch2 46→PDF82, ch5 148→184,
  ch10 307→343, ch12 375→411). No interior plate drift — the 图文版 photos are
  inline on numbered pages, not separate unpaginated plate sequences. Section
  opener pdf pages in book.json are computed (printed+36); spot-verify each
  opener's folio at batch time (an inline full-page plate can nudge a single
  section opener by ±1).
- **Front matter:** cover + title + CIP/copyright (PDF 1–4); a photo-plate
  section INTERLEAVED with the printed 目录 (PDF 5–32, its own folio sequences);
  Preface 前言 探秘 (PDF 33–35, its own sequence, printed 1–3; PDF 36 blank).
- **Back matter:** the book carries its OWN apparatus — a section of source
  notes citing the author's interviews (e.g. "王芳：前国务委员、公安部长，2000年6月8日
  采访"), clustered around printed ~391–394 (PDF 427–430); then Afterword 后记
  (PDF 431–434, printed 395–398). PDF 435–436 are the library endpaper +
  Contra Costa County barcode (scan artifact, not book content). **TODO Batch 1
  / final batch:** run `detect_notes.py` to characterize whether the 注释 are
  per-page footnotes or a collected endnote section, and decide how to
  reproduce them.
- **Page furniture:** verso (even) pages print a VERTICAL running title
  （中国秘密战／——中共情报、保卫工作纪实）in the outer (left) margin; recto (odd)
  pages a vertical running head (章 title, or 目录 on the TOC pages). Folio sits
  in the bottom outer corner. Crop the outer-margin running title before OCR;
  measure the body box in Batch 1 and configure `ocr_crop.py`. First batch's
  first engineering task.
- **Structure:** 12 chapters, 86 numbered sections, + Preface + Afterword.
  Recovered from the printed 目录 (PDF 19–31), which is clean and reliable.
  Full structure and English titles in `book.json`; outline in `out/SURVEY.md`.
- **Environment (setup.sh):** tesseract + chi_sim/chi_tra (and -vert) packs
  installed; PyMuPDF/Pillow/numpy/opencv OK; epubcheck 5.1.0 fetched; checker
  regression tests GREEN. Only note: PaddleOCR absent (expected).
- **Skeleton EPUB:** built (14 units, full hyperlinked pending-aware TOC).
  `qa_epub.py` PASS (27 files, all links resolve). `epubcheck` clean
  (0 fatals / 0 errors / 0 warnings).
- **Branch hygiene:** consolidated onto the canonical book branch
  `claude/chinas-secret-war` (per CLAUDE.md rule 2). The harness's stray
  per-task branch `claude/pdf-source-document-kvueuz` carried no commits beyond
  the template baseline; deleted local, and removed from origin.

Structure and batch plan approved. Batch 1 done (below).

## Batch B01 — Preface (ch00) + Chapter 1 (ch01)

Scope: PDF 33-81; printed Preface 1-3, Chapter 1 printed 1-45. Simplified,
horizontal; chi_sim, psm 6. PaddleOCR absent, so the second read is the
dual-tesseract substitute (scripts/ocr_dual.py, psm 6 vs psm 4).

### Pipeline established (do not revert)
- **Page furniture / crop.** Mirror-margin book: the vertical running title
  sits in the OUTER margin (verso left, recto right). Measured crop, per
  parity: recto (odd PDF) [left 0.07, right 0.86], verso (even PDF)
  [left 0.17, right 0.94], shared top 0.045 / bottom 0.93. Validated by OCR
  (no phantom head column). ocr_crop.py gained per-parity overrides
  (--left-even/--right-even/...) and the geometric folio_present() that
  indents.py needs (it was referenced but missing).
- **assemble.py --blank-assist** (new, opt-in): layers tesseract's blank-line
  paragraph signal on top of the indent, gated by the sentence-end test. The
  indent flags desync from the OCR text on the many inline-photo pages, so the
  blank signal is needed; default behavior unchanged.
- **data/txt_fixes.json + apply_fixes.py --txt** (new): pre-assembly per-page
  OCR fixes for mangles that change paragraph structure. Five here: tesseract
  read the fullwidth exclamation as the digit 1, welding paragraphs; restored.
- Reproducible pipeline for ch01 zh: indents 37 81 (NOT 33-36; the preface has
  its own margins and assembles from the blank-line signal), apply_fixes --txt,
  assemble ch00 33 35 --offset 32, assemble ch01 37 81 --offset 36
  --blank-assist, apply_fixes ch00 ch01.

### Translated and checked
- **ch00 (Preface):** 28 body paragraphs. verify_unit CLEAN (parity 28/28,
  numbers 0 unresolved, 2 anchors ok); check_align OK.
- **ch01 (Chapter 1):** 9 sections + a translated "Principal Sources" section.
  299 English body paragraphs. The frozen VOICE REFERENCE is
  out/ch01_reading.md (check_register run: contractions 2.0/1k, em-dash 3.4/1k,
  rhythm CV 0.49).
- **Apparatus:** glossary.json +17 rows (12 flagged principal: Zhou Enlai, Mao
  Zedong, Chen Geng, Gu Shunzhang, Kang Sheng, Li Kenong, Qian Zhuangfei, Hu
  Di, Chiang Kai-shek, Dai Li, Zhu De, Zhang Xueliang; plus the key organs and
  the word tewu). notes.json: 2 for ch00, 19 for ch01 (reader-model density for
  a long 1927-1937 chapter). check_apparatus clean.
- **Build:** cumulative EPUB builds; qa_epub PASS (28 files, 21 notes, all
  links resolve); epubcheck 5.1.0 clean (0 fatals / 0 errors / 0 warnings).
- Builder patch: render_glossary now renders BOTH sectioned and flat glossary
  rows (apparatus_merge writes flat), so the build does not need a manual
  re-sectioning pass each batch.

### KNOWN ISSUE, top follow-up: ch01 zh parity
verify_unit ch01 FAILS parity: zh 269 vs en 299. The zh side is the OCR
reconstruction, and it under-segments on the figure-heavy pages, where the
inline photos defeat BOTH the indent flags and tesseract's blank lines. The
English is one paragraph per TRUE source paragraph (every page was read from
the scan while translating), so this gap is a defect of the zh QC scaffolding,
not a dropped or added translation paragraph. Because check_content and
qc_entities pair zh to en positionally, they are pending this reconciliation
and were not run clean. Reconcile by hand-splitting the merged zh paragraphs
on the figure pages to 299, recording the splits in ocr_fixes.json (\n
insertions) so a fresh checkout reproduces; then rerun verify_unit /
check_content / qc_entities. (data/zh is gitignored copyright text; the tracked
out/ch01_reading.md is the correction surface and is complete and correct.)

### Figures: DEFERRED (deliberate)
figures.json is empty this batch. The 图文版 carries many inline photos (one or
more per body page, captions often vertical in the outer margin) plus a
Shaan-Gan-Ning border-region MAP on printed 39 (PDF 75). Extracting and
cropping them was deferred to keep the voice gate focused on text, voice, and
note density. Recorded here as a deliberate decision, not an oversight; figure
extraction is a follow-up (and the standing approach for all 12 图文 chapters
needs a commissioner decision: reproduce every inline photo, or a curated
subset).

### FINDING: source notes are PER-CHAPTER
The survey expected the book's own source-note apparatus only at the book's end
(printed ~391-394). In fact EACH chapter ends with its own "主要资料"
(Principal Sources) section: ch01's runs printed 42-45 (PDF 78-81), ~42
interview and reference entries. Rendered this batch as a translated "Principal
Sources" section at the chapter's end. This changes the plan for later batches
and for B13's whole-book source-note handling; flag for the commissioner.

### Source errors rendered as printed and footnoted (verdicts stated)
- Jinggangshan base "across Jiangxi, Fujian, and Zhejiang" (printed 14/PDF 50):
  geographically wrong (Zhejiang not part; figures describe the Central Soviet
  Area). CONTRADICTED.
- Li Dazhao's execution dated 1928 (printed 36/PDF 72): actually April 1927.
  CONTRADICTED.
- Security badge letters "GBW" then called the Russian GPU (printed 16/PDF 52):
  the letters do not match GPU. Flagged.
- Contested history footnoted with verdicts: the "AB Corps" as a real
  conspiracy is CONTRADICTED (the CCP's own 2002 verdict, quoted by the author,
  is cited); the author's framing of Mao's role in the Futian purge is noted as
  partisan.
- Rendered-as-printed uncertain name: 曾固林 "Zeng Gulin" (printed 19/PDF 55),
  the 20th Red Army commander arrested at Futian; obscure, possibly a misprint.

### OCR-fix ledgers
- data/txt_fixes.json: 5 pre-assembly fixes (p37/38/64/76/80, ！->1).
- data/ocr_fixes.json: ch00 has 31 crop-verified char + 2 paragraph-split
  fixes; heading restored. ch01 char fixes are NOT yet fully laddered (to be
  done with the parity reconciliation above).

### Environment / checks
- OMP_THREAD_LIMIT=1 throughout; tesseract left 0 orphans (pgrep -c 0).
- setup.sh checker regression tests: one benign FAIL, "hook stands down on
  template stub." That sub-test asserts the Stop hook stands down when
  HANDOFF.md still holds the TEMPLATE placeholder; HANDOFF.md now holds a real
  batch kickoff, so the hook correctly demands it. Not a defect in the checkers
  or the hook; it will "fail" for the life of the project until completion.

### Batch ends at the voice gate (Step 0c)
B01 stops here for the commissioner to judge voice, note density, and
formatting on ch00 + ch01. Do NOT begin B02 until approved.

## Batch B02 — Chapter 2, sections 1-5 (ch02s01-ch02s05)

Scope: Chapter 2 "暗战 / Secret War," sections 1-5. PDF 82-108 plus section 5's
tail on PDF 109 (printed 46 through 72, ending mid-p73 where section 6 opens).
Simplified, horizontal; chi_sim, psm 6; PaddleOCR absent, dual read via
scripts/ocr_dual.py. Offset constant printed = pdf - 36, re-verified at every
section opener off the scan (s1 p82/46, s2 p87/51, s3 p94/58, s4 p98/62,
s5 p104/68, and s6 opener p109/73 confirmed as the batch's stop).

### Batch-boundary correction (recorded so B03 inherits it cleanly)
The B01 kickoff wrote "PDF 82-103," which is inconsistent with its own stated
printed range 46-72 and the sections-1-5 scope (offset 36 makes printed 72 =
PDF 108, and section 5 runs to the top of PDF 109). The authoritative boundary
is SECTIONS 1-5 = PDF 82-108 plus section 5's four closing paragraphs on PDF
109. book.json's B03 pdf_range [104,133] likewise overlaps section 5; B03's
real scope is sections 6-8 = PDF 109-133 (section 6 opens at PDF 109 / printed
73). The next kickoff states this.

### Translated and checked
- ch02: chapter intro (3 paras) + 5 sections, 167 English body paragraphs in
  out/ch02_reading.md (one paragraph per TRUE source paragraph; every page read
  off the scan). Sections: 1 Zhou Enlai in Danger (34), 2 Zhongtong and Juntong
  Take Formal Shape (44), 3 The Defection Incident! (24), 4 The CCP Central
  Social Affairs Department (35), 5 The Shaanxi-Gansu-Ningxia Border Region
  Security Office (27).
- verify_unit ch02: parity 167 zh / 167 en CLEAN; anchors 18/18 resolve. The
  number invariant's residual flags were all adjudicated to OCR-scaffolding
  artifacts (mangled digits: 战士->战七=7, 518->S18, 八十一->八十=80; embedded
  photo-caption years 1937/1949; place-name numerals 二十里铺; name numerals
  李韶九) and English spelled-out numbers the checker does not parse (words over
  thirteen). Every source quantity was verified against the SCAN while
  translating; none dropped. Load-bearing figures and unit designations were set
  in digits per STYLE (518 blockhouses, 25,000 li, 500,000 men, 329 officers,
  2,288 youth, the Red 15th/25th/26th/81st, etc.).
- check_align ch02: 167/167, median 4.84 en/han; one out-of-line pair (s5-13),
  explained by an inline photo caption garbling that zh scaffolding paragraph
  (the English is correct). qc_entities: 0 misses (its census is thin because
  the OCR mangles many names in the zh scaffolding). check_content is not wired
  to this project's book.json schema (it expects docs/sources, we use structure).
- Register vs frozen ch01: dialogue-contraction metric is QUIET (0.0/1k) and is
  noise here, exactly the reportage caveat in STYLE and references/register-
  drift.md: Chapter 2 is institutional/documentary with little quoted speech,
  and what speech there is runs formal by design (Xu Enzeng's memoir, Dimitrov's
  directive, Chiang's declaration, Zhang Guotao's ceremonial self-deprecation).
  Judged on the narratorial signals instead: rhythm CV 0.51 tracks the ref's
  0.49, sentence median 23, exclamation and rhetorical-question retention held
  to English norms (rationed hard per STYLE). Not stilted narration.

### The two omissions the parity reconciliation caught (rule 4 corollary)
The zh<->en paragraph audit surfaced two section tails that straddle a page
into the NEXT section's opening page and had been missed on the first pass:
(1) section 1's conclusion of the Laoshan bandit story, three paragraphs on
printed 51 (PDF 87) before section 2's heading; (2) section 4's final paragraph
naming the other Social Affairs Department deputy heads, on printed 68 (PDF 104)
before section 5's heading. Both were re-read off the scan and translated. This
is the "tail is where faithfulness fails" rule; the per-section boundary check
is the gate that caught it. B03 must watch the same straddle at s6/s7/s8.

### zh scaffolding parity (method, reproducible)
The figure-heavy body pages defeat both the indent flags and tesseract's blank
lines, so assemble.py under-segments (137 vs 167). Reconciled by a scripted
re-segmentation, scripts/resegment_ch02.py (splits the merged paragraphs at
distinctive anchors and appends section 5's PDF-109 tail), run after
assemble.py. data/zh is gitignored; that script is the reproducible bridge and
must not be reverted. A complete manual zh<->en 1:1 correspondence audit was
performed (this is the real displacement check); no displacement found beyond
the two omissions above.

### Apparatus
- notes.json: +18 for ch02 (feather-dispatch; the Laoshan Incident with its
  date/decoy/site discrepancies; "Deng, Mao, Xie, and Gu"; the Elder Brothers
  Society; the Blue Shirts / Vigorous Action Society; Chiang's skin-rash /
  vitals metaphor; the three-in-one alignment; Hu Zongnan; the opera At the
  Crossroads; the "reform and opening" anachronism; Xu Shiyou's loaded gun; the
  Yellow Emperor's Mausoleum sacrifice; Zhang Guotao; the white-terror slogan /
  surrender law / repentance houses; the Kang Sheng portrait; the Five Elders of
  Yan'an; the Pan Hannian 1955 case; Mao's poem "Snow"). check_apparatus clean.
- glossary.json: +10 rows (Pan Hannian, Zhang Guotao, Hu Zongnan, Zhou Xing, Xu
  Enzeng, Chen Lifu, Wang Ming, Kang Shichang [attested]; Central Social Affairs
  Department, Shaanxi-Gansu-Ningxia Border Region Security Office [decided]).
  REUSED unchanged from ch01: Zhou Enlai, Mao Zedong, Kang Sheng (alias Zhao
  Rong), Li Kenong, Chiang Kai-shek, Dai Li, Zhu De, Zhang Xueliang, Central
  Special Branch, State Political Security Bureau, Zhongtong, Juntong, tewu.

### NOT re-noted (already placed in ch01, cross-referenced or relied on)
Xi'an Incident (ch01); the GPU model behind the security service ("GBW"/GPU
note, ch01); the Longtan Three (ch01); Li Shaojiu and the Futian purge (ch01,
relied on at his mention in s5); Zhongtong/Juntong first gloss (ch01 glossary).

### Source errors / contested claims rendered as printed and footnoted
- Laoshan Incident: text dates it 25 April, the photo caption 24 April; footnote
  states the internal discrepancy (25 April is the attested date). The source
  also twice writes the ambush site "沿湫山" (Yanqiushan) while naming the affair
  after Laoshan; harmonized to Laoshan in the text with the variant noted.
- "改革开放" (reform and opening), printed 58: a real anachronism in the source,
  the author borrowing the post-1978 slogan for the united-front thaw; kept
  visible in scare quotes and footnoted as his own flourish, not a 1930s term.
- Jiang Dingwen is "Xi'an field headquarters director" on printed 53 and
  "Tianshui field headquarters director" on printed 59; rendered as printed both
  places (a source inconsistency, low stakes, not footnoted).
- The interested-witness set: the author's unusually harsh Kang Sheng portrait,
  the sympathetic Pan Hannian and Zhang Guotao treatments, and the partisan
  "only Yan'an was pure ground for the nation" set-piece are rendered faithfully;
  the counter-record and later verdicts live in the footnotes.

### Names crop-verified this batch
Ran verify_names --auto across 82-108 and read the dual-OCR disagreement crops;
plus every page was read off the scan (reading IS crop-verification here). Spot
crops confirmed: 沿湫山 (water radical, not 劳), "改革开放" (both engines +
eye), "用其才，不信其听" (听, not 人). No name corrections needed beyond fixing
"Liang Jishu" -> "Liang Ji" in s1 (由梁济书写起诉书 = "Liang Ji wrote the
indictment"; 梁济 is the known Yan'an-born cadre, confirmed again on printed 69).

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json remains empty. Chapter 2's B02 pages carry ~14 inline photo groups
(Laoshan + Chen Youcai p47; Chen Fusheng p48; Wu Tailiang + Liu Lanting p50;
Zhou/Zhang Yunyi/Kong Shiquan p51; Zhu Jiahua/Xu Enzeng/Chen Lifu/Dai Li p52;
blockhouse p54; Wu Defeng p55; Deng Baoshan/Xu Fanting/Nan Hanchen p56;
Mao + Zhang Guotao p59; Wu Kejian p60; Kang Sheng/Pan Hannian/Li Kenong p63;
Chen Yun p64; 中社部旧址 + 边保 buildings p68; Zhou Xing + deputy heads p71).
The standing question for ALL 图文 chapters (extract every inline photo, or a
curated subset) is still for the commissioner.

### Tooling touched (do NOT revert)
- scripts/build_reading_epub.py: sec_nav now omits a PENDING section from the
  EPUB nav of a PARTIALLY translated chapter. A pending section has no anchor;
  a bare link back to the chapter file lands at the document top and reads as
  out-of-order once earlier sections link to anchors further down (epubcheck
  NAV-011), and the nav content model forbids an unlinked <span> leaf. Fully
  pending chapters still list all sections as bare links. This first bit with
  ch02 (the first partially translated chapter).
- scripts/make_bilingual.py and scripts/check_align.py: both now skip the '***'
  scene-break marker, consistent with check_structure and verify_unit (which
  already did). Without it the en side counted 8 extra "paragraphs" and parity
  looked broken in those two tools only.
- scripts/resegment_ch02.py: new; the reproducible zh re-segmentation (above).
- data/structure.json: +7 ch02 heading rows (chapter title, subtitle, sections
  1-5), matched to the OCR strings so assemble.py marks them.

### Build / environment
- EPUB rebuilt: 3 of 14 chapters (ch00, ch01, ch02), 39 notes, 74 pagebreaks.
  qa_epub PASS (28 files, all links resolve). epubcheck 5.1.0 clean
  (0 fatals / 0 errors / 0 warnings).
- OMP_THREAD_LIMIT=1 throughout; pgrep -c tesseract read 0 after every OCR run.
- Branch consolidated onto claude/chinas-secret-war at session start (the
  harness stray branch claude/chinas-secret-war-b02-zsrbvw was at the same
  commit; deleted local, remote pruned at push).

## Batch B03 — Chapter 2, sections 6-8 + chapter-end Principal Sources (ch02s06-ch02s08)

Scope: Chapter 2 "暗战 / Secret War," sections 6 (知青进入特训班 / Educated Youth
Enter the Special Training Class), 7 (延安防线 / The Yan'an Defense Line), 8 (大布局
/ The Grand Deployment), plus the chapter's 主要资料 / Principal Sources apparatus.
PDF 109-133, printed 73-97. Offset constant printed = pdf - 36, re-verified at
each opener off the scan (s6 p109/73, s7 p120/84, s8 p124/88) and at the stop
(Chapter 3 opens p134/98). Simplified, horizontal; chi_sim, psm 6; PaddleOCR
absent, dual read via scripts/ocr_dual.py. This completes Chapter 2.

### Translated and checked
- ch02_reading.md now carries the whole chapter: 339 English body paragraphs
  (167 from B02 + 172 new). New sections: 6 (63), 7 (29), 8 (44), Principal
  Sources (34). One paragraph per TRUE source paragraph; every page read off the
  scan.
- Verified as a self-contained QC unit "ch02b03" (a SEPARATE zh scaffold so
  data/zh/ch02.txt was not clobbered), then folded into ch02_reading.md:
  - verify_unit ch02b03: parity 172 zh / 172 en CLEAN.
  - check_align: 172/172, median 4.80 en/han; one out-of-line pair, the s8
    photo-caption (许建国 Jin-Cha-Ji group, printed 93) embedded in that OCR
    paragraph; the English is correct (caption is a deferred figure).
  - qc_entities: 0 misses.
  - check_content: still N/A to this project's schema (as in B02).
  - The number invariant's residual flags were all adjudicated to OCR-scaffold
    garble and to idioms/place-names the checker reads as quantities: 老百姓/百姓
    ("hundred surnames" = the common people), 七里铺/三十里铺 (Qilipu / Sanshilipu,
    the training-camp li-names), 万岁 ("long live"), 三仙园 (a restaurant), 二字
    ("the two characters 人民" = the word "people"), the OCR-mangled month in
    "第八期于1941年10月" (tesseract read 1月; the SCAN reads 10月, and the English
    carries October), and OCR digit garble in the figure-heavy regions. These
    were added to data/noise.txt (longest-first, each commented). Every source
    quantity was verified against the SCAN while translating; load-bearing
    figures/unit designations set in digits per STYLE (the 22nd Army; more than
    two hundred organs; over sixty thousand people; 8:40 a.m.; six planes; the
    25,000-li Long March; two hundred trained cadres).
- ONE real drop the number check caught: 四渡赤水 had been rendered "the crossings
  of the Chishui" (the "four" lost); fixed to "the Four Crossings of the Chishui"
  (the named campaign). Re-verified.
- Register vs frozen ch01: dialogue-contraction metric QUIET (0.4/1k), noise
  again for this low-dialogue documentary unit (the reportage caveat in STYLE /
  references/register-drift.md). Judged on narratorial signals: em-dash 0.0/1k
  (rationed hard, well under the ref's 3.4), rhythm CV 0.56 (healthy spread vs
  ref 0.49), sentence median 22. The quoted speech present (the moon joke, Mao's
  "first in China," Huang Kegong's shout, Zhuo Lin's written recollection, Deng's
  reflection on Mao) is either contracted where natural or formal by design.
  Not stilted narration.

### Section tails (rule 4 corollary) — checked
Each s6/s7/s8 tail was read PAST the next heading to confirm the whole preceding
section: section 6's close ("outside cadres from everywhere," the peasant-rising
aside, the two "young students / value talent" codas) sits on printed 84 above
the section-7 heading; section 7's close (the air-raid story, Mao's "first in
China," the "model base / embryo of a new China" line) sits on printed 88 above
the section-8 heading. Both fully captured.

### zh scaffolding parity (method, reproducible)
Same figure-page defeat of indent/blank signals as B02 (many true paragraphs
merged into one OCR line by inline photos, plus a few split across a page). New
script scripts/resegment_ch02b03.py: drops the section-5 tail carried on PDF 109
(already in B02's section 5), applies the merges/splits that bring the OCR to
1:1 with the English, and inserts the Principal Sources heading. Split markers
are drawn verbatim from the garbled OCR. data/zh is gitignored; the script is
the reproducible bridge. The QC unit files (out/ch02b03_reading.md and its
bilingual) were removed after verification so ch02_reading.md is the single
source of truth; re-verification re-extracts the span.

### Apparatus
- notes.json: +18 for ch02 (ch02 unit total 36; book total 57). New: the Arisaka
  Type-38 / "'38-style" pun; the Whampoa Academy analogy; the Three People's
  Principles Youth League; Wang Dongxing; Ling Yun (first Minister of State
  Security); the Yan'an Rectification (cross-ref Chapter 9); Deng Xiaoping;
  Li De / Otto Braun; Zhuo Lin; Jiang Qing; the Huang Kegong case + Mao's letter
  (CORROBORATED, also propaganda from the first); China's Destiny; Li Zicheng
  (brief cross-ref to ch01); the Zunyi Conference; "political power grows out of
  the barrel of a gun" + the knife-haft coinage; the Wang Jingwei puppet regime;
  the Battle of Tai'erzhuang; Deng's "merits outweigh faults" (echoes the 1981
  verdict). check_apparatus clean.
- glossary.json: +22 rows (55 total). People (attested): Deng Xiaoping, Zhuo Lin,
  Luo Qingchang, Wang Dongxing, Xu Jianguo (= born Du Liqing), Tan Zhengwen,
  Zhao Cangbi, Chen Long, Ling Yun, He Long, Lin Biao, Jiang Qing, Nie Rongzhen,
  Li Zongren, Dong Biwu, Ye Jianying, Li De. People (decided, pinyin call for
  lesser cadres): Li Qiming, Bu Lu, Wang Yantang. Terms: 三青团 (Three People's
  Principles Youth League, attested), 整风 (the Rectification Movement, attested).
  CONSISTENCY NOTE: 杜理卿 (Du Liqing), section 5's early Border Security deputy
  head, and 许建国 (Xu Jianguo), the Jin-Cha-Ji Social Affairs head of section 8,
  are ONE man; the glossary row records the name change and both renderings are
  kept (Du Liqing where the book uses the original name).

### NOT re-noted (already placed / relied on)
Kang Sheng and the Rescue Campaign (ch02 s4 + ch01); Whampoa officers / Blue
Shirts (ch02 s2, distinct from the new Whampoa-Academy note); Hu Zongnan (ch02
s2); Zhang Guotao (ch02 s3, his fate enlarged only in the source note here);
the Long March and the 25,000 li (ch01); Sun Tzu's maxim is explained inline by
the author, not footnoted.

### Interested-witness set (rendered as printed, counter-record in the notes)
- The Huang Kegong case is told as a triumph of impartial Yan'an justice; the
  note states it is genuinely well documented AND was put to propaganda use.
- The air-raid set-piece (the police holding their posts, nothing looted, Mao's
  "Yan'an's police... first in China") is a self-celebrating anecdote, rendered
  faithfully with its heat kept; no note needed beyond the naming.
- The Laoshan "no political background" verdict appears in Luo Qingchang's own
  source note, which lays out the dispute honestly; rendered as the source gives
  it.

### Names crop-verified this batch (every page read off the scan)
Confirmed against the scan, correcting OCR: 艾丁 (Ai Ding, not OCR "区三"), 吕瑛
(Lü Ying), 慕丰韵 (Mu Fengyun, not "莫丰韵"), 邓杰 (Deng Jie), 赵去非 (Zhao Qufei,
not "赵去自"), 丁尚柏 (Ding Shangbai, not "丁尚林"), 刘茜 (Liu Qian), 王曦 (Wang Xi),
蔡诚 (Cai Cheng), 曲及新 (Qu Jixin), 郑柱国/穆广林 (Zheng Zhuguo / Mu Guanglin),
余海宇 (Yu Haiyu), 马兆祥 (Ma Zhaoxiang), 谢甫生 (Xie Fusheng), 缪庄林 (Miao
Zhuanglin), 裴周玉 (Pei Zhouyu, consistent with ch01). Number fix: 第八期于1941年
10月 (October, OCR had 1月); 机关单位二百多个 (over two hundred, OCR dropped 二).

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json remains empty. Sections 6-8 carry many inline plates: the Li Qiming
family + author (p73); Wu Cheng (p75); Li Kenong / Luo Qingchang / Wang Yantang
group (p76); the 1992 Qilipu-first-class Beijing reunion (p78); Xiao Chi (p79);
the Deng Xiaoping & Zhuo Lin / Kong Yuan & Xu Ming wedding pair (p80); Yili's
1949 Xi'an-takeover group (p81); Hao Su & Su Ping (p82); Mao Renfeng (p83); the
Border-Security travel-checkpoint MAP 1937-1947 + Laoshan-checkpoint cadres
(p85 — worth keeping, like the ch01 Shaan-Gan-Ning map); Mao Zedong's letter to
Lei Jingtian, facsimile (p86); the three Yan'an municipal police chiefs Liu
Huping / Wang Zhuochao / Hao Su (p87); the young Dong Biwu (p94); the Xu Jianguo
Jin-Cha-Ji leadership group (p93). Standing question (every 图文 photo, or a
curated subset) still for the commissioner.

### KNOWN LIMITATION carried forward
- Printed-page markers (the EPUB page-list) cover s1-5 (printed 46-72) only.
  Sections 6-8 (printed 73-97) have no folio markers this batch: the pagemap
  generator keys to pre-resegment zh indices, and the s5/s6 boundary is tangled
  because section 5's tail straddles onto printed 73. No s6-8 note cites a folio,
  so nothing depends on it. A clean full-chapter pagemap rebuild is a corrections-
  pass task. (ch01 zh parity 269/299, from B01, also still open.)

### Tooling touched (do NOT revert)
- scripts/resegment_ch02b03.py: new; the reproducible zh re-segmentation for the
  B03 span (analogue of resegment_ch02.py).
- data/structure.json: +3 rows (section 6/7/8 headings, matched to OCR strings).
- data/noise.txt: +7 entries (老百姓, 百姓, 七里铺, 三十里铺, 二字, 万岁, 三仙园),
  each commented.

### Build / environment
- EPUB rebuilt: 3 of 14 chapters (ch00, ch01, ch02), 57 notes, 74 pagebreaks.
  qa_epub PASS (28 files, all links resolve). epubcheck 5.1.0 clean
  (0 fatals / 0 errors / 0 warnings).
- OMP_THREAD_LIMIT=1 throughout; pgrep -c tesseract read 0 after every OCR run.
- Branch consolidated onto claude/chinas-secret-war at session start (the harness
  stray branch claude/china-secret-war-b03-vax76y was at the same commit as
  origin/claude/chinas-secret-war; deleted local, remote already pruned).
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff, not the template stub).

## Batch B04 — Chapter 3, the whole chapter + chapter-end Principal Sources (ch03s01-ch03s07)

Chapter 3 ("从'地下'到'地上'" / "From 'Underground' to 'Aboveground'") is
translated, built, and QA-clean. **Chapter 3 is COMPLETE.** ch01 remains the
FROZEN voice reference.

### Pipeline run (reused B01-B03, nothing re-measured)
- render 134-170 --dpi 300; ocr_crop 134-170 with the measured per-parity crop
  (recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93,
  chi_sim, psm 6, running head "中国秘密战——中共情报保卫工作纪实"); ocr_dual
  134-170; indents 134-170. OMP_THREAD_LIMIT=1 throughout; pgrep -c tesseract
  read 0 after every OCR run.
- structure.json: +10 rows (ch03 chapter title, subtitle, section 1-7 headings,
  matched to the OCR strings).
- assemble ch03 134-170 --offset 36 --blank-assist → 268 body paras (figure
  pages under-segment). resegment_ch03.py (new; the B04 analogue of
  resegment_ch02b03.py) brings it to 305 by 2 page/figure merges + ~30 splits
  and rewrites the "主要资料:" line as a "### Principal Sources" heading.
- Folios spot-verified off the scan at every section opener: s1 p134/98, s2
  p141/105, s3 p144/108, s4 p150/114, s5 p154/118, s6 p158/122, s7 p164/128;
  Principal Sources p168-170/132-134; chapter ends p170/134 (ch04 opens p171/135).

### The checks
- **verify_unit ch03**: parity 305 zh / 305 en (1:1, no declared exceptions).
  27 note anchors all resolve.
- **check_align ch03**: 305/305, median 4.77 en/han, no pair strays > 2.2x.
- **qc_entities** on out/ch03_bilingual.md: 0 misses.
- **check_content**: N/A to this book's book.json schema (confirmed again).
- **Number check** (via verify_unit, --noise data/noise.txt): 55 residual flags,
  ALL verified as noise — OCR garble on figure-heavy lines (乃→万, 拿→千, 五十号→
  五于, 一万四千→10004, embedded photo-caption years), name numerals (师印三,
  野坂参三, 李锡九), idiom/decade labels now in noise.txt. Four REAL number issues
  found and FIXED against the scan:
    * 国民党二十二军 (opium pack train, p116/152) — the "22nd Army" designation had
      been dropped; restored.
    * 二十几个小铺子 (p115/151) — was "a dozen-odd", corrected to "twenty-odd".
    * 上百副担子 (p115/151) — was "hundreds of", corrected to "over a hundred".
    * 战干四团 (p125/161) — was "the Fourteenth", corrected to "the Fourth War
      Cadre Regiment" (crop-verified 四, not 十四).
- **Tail verification** (rule 4): section 7's close and all 30 Principal-Sources
  entries read against the scan (interview dates, book titles, publishers) — clean.
- **check_register --ref out/ch01_reading.md**: within tolerance (contr 2.9/1k =
  1.43x ref; em-dash 0.1/1k; rhythm CV 0.49 = ref; sent median 22). Dialogue
  metric flagged noisy (low-dialogue unit, as expected for a mostly-narratorial
  chapter — judged on the narratorial signals per STYLE).
- **data/noise.txt**: +13 entries (一百八十度, 二十世纪, 四通八达, decade labels
  三十/四十/五十/六十/七十/八十年代, 七贤庄, 八路军, 八办, 李锡九), each commented.

### Apparatus (via apparatus_merge.py; check_apparatus 0/0)
- **+21 glossary rows** (70 total): 熊向晖, 沈安娜, 白崇禧, 傅作义, 阎锡山, 卢绪章,
  陈嘉庚 (Tan Kah Kee), 王世英, 吴德峰, 宣侠父, 蒋鼎文, 卫立煌, 邓宝珊, 赵寿山,
  高崇民, 广大华行, 华润公司, 八办, 皖南事变, 韩练成, 阎又文.
- **+27 footnotes** (book total 84). Coverage: the 八办 arrangement and why the
  offices could exist openly; the Zhongshan suit; Pingxingguan; the Mengjiang
  puppet government; the "Latter Three Heroes" (cross-ref Longtan); the weiqi
  "idle chessman" metaphor; the tiger's-lair proverb; Shen Anna; China Resources;
  Bao Yugang (Y.K. Pao); Tan Kah Kee; Zengjiayan No. 50 / Hongyan; the Changsha
  fire; the New Fourth Army Incident; the Yellow River Cantata; Bethune; Ho Chi
  Minh; Nosaka Sanzo; Edgar Snow / Red Star Over China; the Barrett/"Ou Daiyi"
  observer groups; Yan Baohang's Barbarossa claim (UNCORROBORATED, stated in note);
  the 89-POW rescue; the Xuan Xiafu assassination (author-as-interested-witness:
  Chiang's order CORROBORATED by Zhang Yanfo's memoir, the "turn Hu Zongnan"
  motive flagged as the Communist interpretation); Lihuang County; the Executive
  Headquarters; the three-thirds system.

### "NOT re-noted" (already placed earlier; cross-referenced, not repeated)
- "the far country" (远方 = USSR/Comintern) — glossed B01/B02; a one-line
  cross-reference note repeats the gloss where 远方 first appears in ch03.
- "reform and opening" (改革开放, the author's recurring anachronistic motif) —
  noted in ch02; ch03 uses it 4x, rendered consistently, NOT re-noted.
- "Three Heroes of Longtan" (龙潭三杰) — noted ch01; the ch03 "Latter Three Heroes"
  note cross-references it.
- Whampoa Academy, the Comintern, the Rectification Movement — all noted ch01/ch02.
- Xu Enzeng, Hu Zongnan, Zhou Enlai, Li Kenong, Dong Biwu, Ye Jianying, Deng
  Xiaoping/Zhuo Lin, etc. — existing glossary rows, reused unchanged.

### Names crop-verified this batch
Section openers' folios; 国民党二十二军 (22nd Army, p152); 战干四团 (Fourth, not
14th, p161); the three-organ layout on p158 (confirmed 3 separate paragraphs);
the Ejin banquet one-line punch (p138, confirmed a separate paragraph); the Wang
Shiying portrait split (p138). Reading-side punch-line splits added to match the
source's isolated one-liners: the Ejin killing; the radio-hunt / "now a museum"
break (p161/162); the Juntong-reward / Chiang's-confession break (p163); "两军
如何交流? / 交上两百万个朋友" (p164); 卫立煌 thanks / 三十万发子弹 (p169).

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json remains empty. Chapter 3 is the most plate-dense chapter so far:
Ye Jianying/Bogu/Tong Xiaopeng Nanjing-office group (p100); Wang Shiying portrait
(p102); the "Latter Three Heroes" trio Chen Zhongjing/Xiong Xianghui/Shen Jian
(p110); Xie Hegeng & Wang Ying wedding (p111); Deng Yingchao with the Shen Anna
couple, and Hua Mingzhi & Shen Anna (p113); Shen Anna stenographing beside Chiang
Kai-shek (p112); the young Nan Hanchen (p116); Lu Xuzhang with the Guangda Huaxing
partners in Chongqing + the drug-plant founders' facsimile signatures incl. Chen
Guofu and Bao Yugang (p117); Xu Xiangqian/Xuan Xiafu/Zuo Quan/Chen Geng in Xi'an
1937 (p126). The Xi'an checkpoint/office material has no map this chapter. Standing
question (every 图文 photo, or a curated subset) still for the commissioner.

### KNOWN LIMITATION carried forward
- **ch03 has NO printed-page (folio) markers.** assemble.py writes the pagemap
  keyed to PRE-resegment paragraph indices; after resegmentation (268→305) those
  indices are stale, so data/pagemap/ch03.json was DELETED rather than ship
  misplaced markers (wrong markers are worse than an honest gap). No ch03 note
  cites a followable folio, so nothing depends on it. A clean full-chapter
  pagemap rebuild (compute page→paragraph against the resegmented file) is a
  corrections-pass task, same as the ch02 s6-8 gap. (ch01 zh parity 269/299,
  from B01, also still open.)
- The number check leaves 55 residual flags on ch03; all are catalogued as noise
  above and were verified against the scan. 13亿/11亿 render as "1.3 billion"/
  "1.1 billion" (correct 亿→100M conversion; the checker cannot parse "billion").

### Tooling touched (do NOT revert)
- scripts/resegment_ch03.py: new; the reproducible zh re-segmentation for B04
  (merges王世英/阎又文 photo-splits, ~30 splits, inserts Principal Sources heading).
- data/structure.json: +10 rows (ch03 headings, matched to OCR strings).
- data/noise.txt: +13 entries (see above), each commented.
- data/apparatus_ch03.json: the B04 apparatus merge file.

### Build / environment
- EPUB rebuilt: 4 of 14 chapters (ch00, ch01, ch02, ch03), 84 notes, 74
  pagebreaks (ch03 folio markers intentionally absent, see above). qa_epub PASS
  (28 files, all links resolve). epubcheck 5.1.0 clean (0 fatals/0 errors/0 warnings).
- Reading text: 0 literal <i> tags, 0 em dashes (the one parenthetical gloss year
  rendered with parentheses, not dashes).
- Branch consolidated onto claude/chinas-secret-war at session start (the harness
  stray branch claude/china-secret-war-b04-ch03-3dr47i sat at the same commit as
  origin/claude/chinas-secret-war; the local canonical branch was reset to origin).
- setup.sh regression "hook stands down on template stub" still FAILS benignly.

## Batch B05 — Chapter 4, the whole chapter + chapter-end Principal Sources (ch04s01-ch04s05)

**Scope.** Chapter 4 第四章 拔钉子 ("Pulling Out the Nails"), PDF 171-183, printed
135-147. All five sections plus the chapter intro and the chapter-end Principal
Sources. Offset constant printed = pdf - 36, spot-verified at every section opener
off the scan: s1 双重政权 p135; s2 争抢"宝葫芦" p139; s3 "红色福尔摩斯"出招 p142;
s4 反腐风暴 p143; s5 "护送出境" p144; Principal Sources close p146-147. Chapter 5
opens p148 (PDF 184), the stop.

**Result.** 119 English body paragraphs, 1:1 parity with the source. 5 section
headings + chapter title/subtitle + Principal Sources. +14 notes (book total 98).
+25 glossary rows (101 total). ch04 is the FROZEN reference's fourth measured unit.
Chapter 4 is COMPLETE.

### Source read entirely off the scan (the OCR was not usable as a scaffold)
Chapter 4 is the most caption-corrupted span so far. The 图文版 sets photo plates
INTO the body column on pdf 172-174, 177, 179-180, and the verso vertical running
title bleeds in as well; both tesseract configs (psm6/psm4) and ocr_dual merged
four-to-eight true paragraphs per figure page and injected caption fragments and
pure garbage mid-line (assembled ch04.txt paras 10-13 and 57 were almost entirely
unusable). So every one of the 13 pages was read by eye and every paragraph
transcribed and verified against BOTH OCR configs. scripts/resegment_ch04.py holds
the verified paragraph list and rebuilds data/zh/ch04.txt from it (the reproducible
record; data/zh is gitignored). This is the documented limit case the
resegment_ch03 docstring anticipated: not merge/split-on-garbled-anchor but a full
hand transcription.

### Crop-verified names/numbers (the number check earns its keep again)
- Xunyi KMT magistrate 张中堂 (Zhang Zhongtang): the OCR gave 张中符 / 张中笃 /
  张中党 across three occurrences; the scan is 张中堂. Crop-verified.
- Fu county KMT magistrate 蒋龙涎 (Jiang Longxian): OCR 蒋龙洗 / 薪龙族; scan 蒋龙涎.
  Crop-verified (p137, p145). Kuang Yumin 匡裕民 (artillery battalion cdr) confirmed.
- 郭相堂 (not 郭相党), 李养之, 慕青 (not 区青), 龚震 (not 獒震), 张振声 (not 张振志),
  鲁南 (not 售南), 陈奇涵, 赵苍璧, 汪锋, 于桑 all crop/scan-verified.
- 马豫章 (Ma Yuzhang): OCR gave 马耶章 / 马弛章 / 马蚤 / 马鸳章; the photo caption and
  body on p138/p147 are unambiguous 马豫章.
- 邹瑜's "随同长兄万里迢迢奔赴延安" is 长兄 (elder brother) + 万里迢迢 (a great
  distance), NOT a person named Wan Li; rendered "with his elder brother... the
  long road." Noised 万里迢迢.
- Numbers all verified against the scan: 23 counties; 200,000 troops (20万);
  4,500 (张荫梧); 400 (Shen county); 300 killed + twelve fled (Huan county);
  4 seats/5 districts/40+ townships and 5 seats/6 districts/43 townships;
  17 disabled men; nine representatives; 385th / 165th / 359th Brigades,
  27th Group Army, 2nd Cavalry Division; 100,000+ yuan embezzled; 27 reports /
  100,000 words. 十二人 is genuinely twelve (contrast the B04 dozen/twenty trap).

### The checks
- Parity 119/119 (check_structure --pairs). Alignment OK, median 5.17 en/han, no
  pair strays >2.2x (check_align). qc_entities 0 misses (note: qc_entities is a
  vacuous pass on this project's FLAT glossary schema, keyed by zh at top level,
  not nested sections as the script expects; entity survival was ensured by hand
  during translation, every glossary hanzi rendered). verify_unit: numbers 0
  unresolved, anchors 14 ok.
- Number check: 6 new noise entries (万里迢迢, 四肢, 两当, 三边, 千百件, 四川, plus
  the two arabic-万 artifacts 20万 and 十多万 whose value is carried in the English
  as digits; 四川 had only ever been a comment example, now a real entry). Every
  entry commented with its value and the phrase the English uses.
- Register vs the FROZEN ch01 reference: within tolerance. Dialogue-contraction
  metric is noise here (ch04 is almost pure narration; its only quoted speech is
  Kang Sheng's document-register dressing-down and the Mao/telegram set pieces,
  kept formal by design). Narratorial signals: em-dash 0.0/1k (zero em dashes,
  as ch03), rhythm CV 0.46 vs ref 0.49, sentence median 22. Judged on those.
- Tail verification (rule 4 corollary): the Principal Sources close (p146-147) and
  the section-5 turn toward Chapter 5 (p182) read against the scan; faithful.

### Notes added (14; book total 98)
dual regime (双重政权, the united-front arrangement); the Fifth Plenum "restrict
alien-party activities" policy (Jan 1939); friction 磨擦 (the 1939-43 term); Xi
Zhongxun (bio, Xi Jinping's father, CORROBORATED); Du Bincheng (executed by Hu
Zongnan Oct 1947, CORROBORATED); baojia (gloss); the Pingjiang Massacre (Jun 12
1939, Yang Sen's 27th Group Army, six killed incl. Tu Zhengkun & Luo Ziming,
CORROBORATED); Ma Yuzhang (the secret-Communist magistrate, family testimony,
thinly documented elsewhere); He Shaonan / "Commissioner Friction" (the Wang Zhen
anti-corruption campaign, CORROBORATED in outline); Wang Zhen (359th Brigade,
later PRC vice-president, CORROBORATED); Ma Hongkui (Ningxia Ma-clique warlord);
Bu Lu / Chen Bo the "Red Sherlock Holmes" (the interested-witness counter-record:
arrested 1951 in the "two Chens case," died 1972 in labor reform, cleared 1980,
CORROBORATED); the classical telegram flourish 盖亦仁之至义之尽也 (Mencian idiom
dressing an ultimatum); chujian 锄奸 / the Anti-Traitor Committee (gloss, points
to Chapter 7). Fact-checks via Wikipedia / Baidu Baike / People's Daily 党史 /
Guangzhou Party-history office; no LLM-sourced content.

### NOT re-noted (already placed earlier in the book)
- 皖南事变 (New Fourth Army Incident): noted at ch03 (anchor "engineered the New
  Fourth Army Incident"). Appears here in s5; not re-noted, glossary row already
  present.
- 特务 / tewu, 汉奸, 中统 (Zhongtong), 军统 (Juntong): loaded-term notes placed at
  ch01. Hu Zongnan (ch02), Kang Sheng (ch02), the "reform and opening" motif (ch02),
  the Rescue/Rectification campaign (ch02) all already noted; used, not re-noted.
- 边保 / Border Security, 中社部 / Social Affairs Department, 八办: glossed earlier;
  reused unchanged.

### Renderings settled / reused
Reused unchanged: 边保 (the Border Security), 中社部 (the Social Affairs Department),
八办, 中统/军统, 特务, 康生 (Kang Sheng / "Boss Kang" for 康老板), 胡宗南, 周恩来,
毛泽东, 蒋介石 ("old Chiang" for 老蒋), 王明, 许建国 (Xu Jianguo, = 杜理卿),
罗青长, 李启明, 布鲁, 赵苍璧, 皖南事变. New this batch (see glossary): 双重政权 "dual
regime", 磨擦 "friction", 宝葫芦 "treasure gourd" / 囊形地带 "the pouch", 护送出境
"escorted out of the territory", 关中/陇东分区 "Guanzhong/Longdong sub-district",
抗敌后援会 "Resist-the-Enemy Support Association", 锄奸委员会 "Anti-Traitor Committee",
肤施县 "Fushi County", and the new cast (习仲勋, 杜斌丞, 马豫章, 何绍南, 王震, 萧劲光,
程潜, 刘伯承, 陈奇涵, 邹瑜, 陈泊, 马鸿逵, 杨森, 张荫梧, 汪锋, 于桑).

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json still empty. Chapter 4's inline plates catalogued for a later
figures pass: the Yan'an panorama by Liang Ji (p136); the double-life magistrate
Ma Yuzhang portrait (p138); a Longdong group photo (p141); Xi Zhongxun 1932 doing
army-work, left-one (p141); Bu Lu at Yan'an (p143). Standing question (every 图文
photo, or a curated subset) still for the commissioner.

### Build / environment
- EPUB rebuilt: 5 of 14 chapters (ch00, ch01, ch02, ch03, ch04), 98 notes, 87
  pagebreaks. qa_epub PASS (28 files, 21 documents, all links resolve). epubcheck
  5.1.0 clean (0 fatals / 0 errors / 0 warnings / 0 infos).
- ch04 DOES carry printed-page (folio) markers (resegment_ch04 rebuilds the
  pagemap from the verified paragraph list; unlike ch03, no stale-index problem).
- Reading text: 0 literal <i> tags, 0 em dashes.
- Branch consolidated onto claude/chinas-secret-war at session start (the harness
  stray branch claude/china-secret-war-ch04-1pds62 sat at the same commit as
  origin/claude/chinas-secret-war = 696786f; local canonical was reset to origin,
  stray local deleted).
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff, so the stub-detection test trips). All other
  checker regression tests green.

### Tooling touched (do NOT revert)
- scripts/resegment_ch04.py: new; rebuilds data/zh/ch04.txt from the hand-verified
  paragraph list (the OCR was too caption-corrupted to use as a scaffold).
- data/structure.json: +7 rows (ch04 chapter title, subtitle, 5 section headings,
  matched to the OCR strings).
- data/noise.txt: +8 entries (万里迢迢, 四肢, 两当, 三边, 千百件, 四川, 20万, 十多万),
  each commented with its value and the English phrase.
- data/apparatus_ch04.json: the B05 apparatus merge file.

---

## Batch B06 -- Chapter 5 (第五章 深入虎穴 / "Into the Tiger's Den"), whole chapter + Principal Sources

**Scope.** ch05s01–ch05s08 plus the chapter-end 主要资料, PDF 184–222 / printed
148–186 (offset printed = pdf − 36, spot-verified at every section opener; Ch. 6
opens PDF 223 / printed 187). Chapter 5 is COMPLETE. 330 English body paragraphs,
1:1 parity with data/zh/ch05.txt (330). ch01 remains the frozen voice reference.

**Method.** Every page image read by eye and transcribed to true source
paragraphs; scripts/resegment_ch05.py HARDCODES the verified ('h'|'b') list and
writes data/zh/ch05.txt wholesale (model: resegment_ch04.py). Unlike B05, this
chapter's straight text pages OCR'd cleanly, so assemble.py (289 paras) served as
an independent boundary cross-check; but the plate/column-wrap pages (pdf
189–192, 199–208, 210, 220) merged four-to-eight true paragraphs and injected
caption/running-title bleed exactly as warned, so the hand-verified resegment is
authoritative. assemble.py kept in the pipeline for the pagemap/heading sanity
check only.

**Crop-verified names/numbers (against the scan).** 上万裕 Shang Wanyu (OCR gave
王万裕), 单不移 Shan Buyi (OCR 单不和), 徐晃 Xu Huang, 冉苹 Ran Ping, 陈本身 Chen
Benshen, 蒲随昌/蒲又杰 Pu Suichang/Pu Youjie, 万里浪 Wan Lilang (a person; cf. the
B05 trap where 万里迢迢 was NOT), 陆海涛 Lu Haitao (split across the 212/213 page
break), 秦老太/秦妈妈 "Old Lady Qin/Mama Qin" (a genuine female cover figure,
distinct from 老太爷 Zhang Weiyi). 蹇先佛 rendered "Jian Xianfo": the referent is
unambiguously Xiao Ke's wife; the printed glyph is the common 塞/蹇 variant and
OCR garbled it (宕/宣) -- rendered to the correct referent, logged here.

**Source-error footnotes (rendered as printed, verdict in the note).** (1) 诺门罕
之战 dated "1937" -- Nomonhan/Khalkhin Gol was 1939; CONTRADICTED. (2) 东亚同文书院
founded "1905" -- the Tōa Dōbun Shoin dates to c. 1900–01; CONTRADICTED on the
date. Both left as printed in the text.

**Interested-witness counter-record.** The "who warned Stalin" claim (§2) carries
a note: Yan Baohang's obtaining the June 22 date and Russia's 1995 posthumous
decoration of him are CORROBORATED (Chinese state sources; the decoration is
real), but Stalin received and discounted many warnings (Sorge, British
intercepts) and the USSR was caught unprepared, so the decisive-effect claim and
the thank-you telegram rest on Chinese accounts and are UNCORROBORATED/CONTESTED
in the Soviet record. The author is himself relatively honest here ("one day
early… suffered a grave defeat all the same").

**Checks run.**
- verify_unit ch05: parity 330=330; numbers checked 330 pairs, **0 unresolved**;
  anchors **24 ok**.
- check_align ch05: 330/330, median ratio 4.97 en/han, no pair strays >2.2×.
- qc_entities: 0 misses (vacuous pass on the flat glossary; entity survival done
  by hand -- every recurring handle reconciled against glossary/authority).
- check_register --ref out/ch01_reading.md: within tolerance. Dialogue metric
  noisy (low-dialogue reportage, flagged as such); narratorial signals close to
  ref -- contr 7.5/1k (ref 2.0), em-dash 4.3/1k (ref 3.4), rhythm CV 0.50 (ref
  0.49), sentence median 22.
- check_apparatus: 0 failures (19 warnings are all PRE-EXISTING rows from earlier
  batches lacking attestation notes; all 22 new B06 rows carry notes).
- qa_epub: PASS (28 files, 21 documents; 122 refs / 122 bodies / 122 backlinks).
- epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.
- Reading text: 0 literal <i> tags, 0 em-dash violations (translation uses em
  dashes as English punctuation demands, rationed).

**Number-check noise added (data/noise.txt, +20, longest-first, each commented).**
Name-numerals 九一八, 杜汉三, 曾三, 张怀三, 陈炳三, 陈三百, 三木, 坂垣征四郎, 上万裕,
万里浪, 岩井英一 (added so the following 千方百计 rule can fire past the name's
trailing 一); org/place/title 三青团, 五台山, 十字街头; decade 二十年代; idioms
王老五, 两栖, 文武两手, 三教九流, 千方百计, 千里迢迢. Four genuine small counts were
carried in the English instead of noised (两人 "the two of them", 两家 "the two
[offices]", 二三十 "twenty or thirty", 三国 "three-nation pact").

**Apparatus.** +24 notes (book total 122); +22 glossary rows (123 total). New
glossary handles to KEEP: the Central Intelligence Department (中情部) / Central
Investigation and Study Bureau; No. 76; the Ume Kikan; the Iwai Kōkan; the Tokkō;
Manchukuo; the National Defense Line; the dog-beating squad; the South China
Intelligence Bureau; and people Yan Baohang, Guan Lu, Li Shiqun, Ding Mocun, Iwai
Eiichi, Yuan Shu, Zhang Weiyi ("the Old Master"), Chen Huanzhang/Chen Tao, Sorge,
Kawashima Yoshiko, Kagesa Sadaaki, Wang Chaobei.

**Reconciliation note.** 关中分区 fixed to "Guanzhong **sub**-district" to match
the ch04 glossary (an initial draft drift to "district" was corrected across all
occurrences; 军分区 → "military sub-district" likewise). 囊形地带关中分区 rendered
"the pouch-shaped Guanzhong sub-district" (Hu Zongnan's term per the 宝葫芦 gloss).

**Reused unchanged (glossary rows):** 边保, 中社部, 八办, 中统/军统, 特务, 康生,
胡宗南, 周恩来, 毛泽东, 蒋介石, 王明, 许建国 (=杜理卿), 罗青长, 李启明, 布鲁, 熊向晖,
陈赓, 戴笠, 三青团, 潘汉年, 皖南事变, 沈安娜, 白崇禧, 阎锡山, 邓宝珊, 萧劲光, 陈奇涵.

**NOT re-noted (already placed in ch01–ch04):** 皖南事变 (New Fourth Army Incident,
ch03); the Marco Polo Bridge Incident (ch-earlier); the Special Branch / 中央特科;
Kang Sheng; Dai Li; Whampoa; the Long March; Xi Zhongxun; the Comintern. First-
appearance notes in B06 only for the genuinely new furniture.

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json still empty. Chapter 5's inline plates catalogued for a later pass:
Liu Hekong in Dihua 1938 (p189) and his family in Shanghai (p190); portraits of
Liu Shaowen (p191), Yan Baohang / "the Yan family's old shop" (p192), Yang
Hongchao (p199), Cheng Yonghe 1950 and Mao Peichun (p200), Guan Lu (p215), Yuan
Shu with Iwai Eiichi (p217), Hua Kezhi (p218); Mao speaking at Yan'an (p194);
Zhang Jiping at Ganzhou 1949 (p198); Wu Defeng with Wu Yunfu 1938 (p201); Lin Yi
and Teng Daiyuan 1947 (p204); Chen Tao and wife at Linfen 1941 (p205); Jiang Tao
1950 (p208); Li Shiyu's family (p209); Zhang Mengshi and wife (p210); Wang Jingwei
hearing Li Shiqun's "qingxiang" report 1942 (p212); Li Zhengwen (p219). Standing
question (every 图文 photo, or a curated subset) still for the commissioner.

### Build / environment (B06)
- EPUB rebuilt: 6 of 14 chapters (ch00–ch05), 122 notes, 125 pagebreaks.
  out/chinas_secret_war.epub. qa_epub PASS; epubcheck 0/0/0/0.
- data/structure.json: +10 rows (ch05 chapter title, subtitle, 8 section headings,
  matched to the OCR strings).
- scripts/resegment_ch05.py: new; the hand-verified paragraph rebuild for ch05.
- ch05 carries printed-page (folio) markers (resegment rebuilds the pagemap).
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff).


## Batch B07 -- Chapter 6 (第六章 东方大谍 / "The Great Spies of the East"), whole chapter + Principal Sources

ch06s01-ch06s08 + the chapter-end 参考资料 (rendered "### Principal Sources").
PDF 223-255, printed 187-219 (offset constant printed = pdf - 36, spot-verified
at every section opener off the folio). 341 English body paragraphs, 1:1 parity
with the hand-verified zh source. Chapter 6 answers Chapter 5's "super-spy"
cliffhanger: the world race for Japan's intentions, won by the CCP twice over
(Barbarossa, then Pearl Harbor).

### Source read entirely off the scan (OCR unusable as a scaffold on the 图文 pages)
Every page image (data/png/p0223-0255.png) was read by eye and every true source
paragraph transcribed and verified against both OCR configs. scripts/resegment_ch06.py
HARDCODES the verified ('h'|'b', text) item list and writes data/zh/ch06.txt
wholesale (model: resegment_ch05.py). assemble.py's body count (302, 4 headings)
under-counted by ~39 as expected -- it merged the many one-line PUNCH paragraphs
and the plate/faded pages; the hand resegment (341 body) is authoritative.
p251 is a badly FADED leaf: both OCR configs returned near-garbage; the linchpin
paragraph and the three-portrait caption were read by magnified crop.

### Crop-verified names / numbers / source errors (rendered faithfully, footnoted)
- 荒尾精 Arao Sei (OCR gave 荡尾精); 梅宝玑 Mei Baoji (uncle); 显玗 Xianyu.
- 高崇武: the source PRINTS 高崇武, but the man is the documented 高宗武 Gao Zongwu
  of the Jan 1940 Gao-Tao incident. Rendered "Gao Chongwu" + footnote. (崇 for 宗.)
- 南冠湾: the source PRINTS 南冠湾 for 单冠湾 (Hitokappu Bay, the Pearl Harbor fleet
  anchorage off Etorofu). Rendered "Hitokappu Bay off Etorofu Island"; zh scaffold
  keeps the printed 南冠湾. (An earlier draft wrongly "corrected" the zh to 单; fixed.)
- 川岛芳子's father printed 耆善 (Prince Su's name is 善耆, Shanqi -- characters
  reversed). Rendered "the Qing dynasty's Prince Su" (title carries it); the
  reversal is a minor low-stakes discrepancy left UNfootnoted (Kawashima already
  noted ch05).
- 大音无声: the source prints 无声 for Laozi's 大音希声 (Daodejing 41); footnoted.
- Cross-page / cross-book identities resolved off the scan: 刘钊 Liu Zhao (Zheng
  Wendao's Party sponsor; p251 illegible, resolved from p252 + p255); 方知达 =
  张明达 (p255); 钱明 = 景若南 (p255).
- The US Army Observation Group photo caption (p249) is dated 1943; the Dixie
  Mission actually reached Yan'an in July 1944. Figure DEFERRED, so not rendered;
  noted here.

### The checks
- verify_unit ch06: parity 341/341; numbers checked 341 pairs, 0 unresolved;
  anchors 12 ok.
- check_align ch06: 341/341, median 4.80 en/han, no pair strays > 2.2x. OK.
- qc_entities: vacuous PASS (flat glossary); entity survival ensured BY HAND and
  by consistency grep (Nakanishi Kō x95, Ozaki Hotsumi x27, Pan Hannian x32, Ume
  Kikan / No. 76 / Iwai Kōkan / Tokkō all uniform, macrons consistent).
- data/noise.txt extended (each commented): 石田七郎, 郑百千, 岩桥竹二 (names with
  numerals); 3万 (=30,000 Katyn officers; Arabic+万 the reader can't combine, value
  carried in English as "30,000"); 622 (the "six-two-two" June-22 label); 第二天
  (the next day). Four number-carrying pairs were REWORDED to carry the count
  ("both"/"two"/"three-nation") rather than noised. No real quantity was noised.
- check_register --ref out/ch01_reading.md: within tolerance (contractions 4.2/1k,
  em-dash 4.5/1k, rhythm CV 0.53, sentence median 21). ch06 is a LOW-DIALOGUE,
  document-heavy unit: most quoted material is telegrams, directives, a treaty
  outline, a diary entry, inscriptions, oaths, the TASS/Golikov statements (all
  exempt registers). The genuine conversational lines (the American taunt, Zheng
  Wendao's reply, Nakanishi's parting charge, his inner monologue) were contracted;
  a first pass had left them formal and tripped the metric.
- Tail verified against the scan (s8 close: Nakanishi's verse, the Laozi asterism,
  the "情报领先" question); Principal Sources (30 entries) verified against p253-255.
- Fixed a stray untranslated CJK word ("The综合 judgment" -> "The overall judgment").

### Notes added (12; book total 134)
Fact-checked against Wikipedia / Baidu / academic sources (no AI references):
1. Japanese Workers' and Peasants' School (Yan'an, opened 15 May 1941; Nosaka
   Sanzō). CORROBORATED.
2. The Tanaka Memorial: authenticity CONTRADICTED (forgery per scholarly
   consensus, no Japanese original); the Yan Baohang / 1929 Kyoto IPR circulation
   CORROBORATED.
3. 支那 / Shina: the derogatory Japanese exonym in the report title and 支那派遣军 /
   支那事变; rendered "China."
4. Operation Kiri / Song Ziliang: PARTLY CORROBORATED. Song Ziliang was a REAL
   Soong-family name but the negotiator was an impostor (a Dai Li / Juntong agent);
   Pan Hannian exposed him to Iwai with ACCURATE intel (not "disinformation"); the
   book's dramatized framing and the credit it gives Pan are Chinese accounts.
5. Gao Chongwu source error (documented Gao Zongwu / Gao-Tao incident).
6. Kantokuen (关特演): CORROBORATED (July 1941, ~750,000-850,000 troops, cancelled).
7. The Moscow-defense claim (Stalin moved 200,000 west and won Moscow on CCP
   intel): transfer real but CCP-attribution UNCORROBORATED; usually credited to
   Sorge / SIGINT; cross-ref ch05.
8. The Dec-7 Pearl Harbor prediction (Nakanishi/Ozaki): PARTLY CORROBORATED
   (southward strike attested; the exact date rests on later Chinese accounts).
9. Chi Buzhou's Pearl Harbor decrypt + the Xiao Bo warning: UNCORROBORATED
   (Chinese-origin, absent from Western records).
10. Yue Fei ("the Yue Fei of Japan").
11. Zhuge Liang "pacifying the Five Routes" allusion (cross-ref the ch05 Empty
    City note).
12. Laozi's 大音希声 (Daodejing 41) and the source's 无声 variant.

### NOT re-noted (already placed earlier in the book; cross-referenced)
Sorge (ch05), the East Asia Common Culture Academy + its 1905/1901 date already
CONTRADICTED in ch05 (ch06 correctly says 1901), the Ume Kikan, No. 76, the Iwai
Kōkan, Kagesa Sadaaki, the Tokkō, Yuan Shu, Guan Lu, Li Shiqun, Ding Mocun, Zhang
Weiyi, Yan Baohang + the Barbarossa warning (ch03/ch05), Kawashima Yoshiko (ch05),
Sun Tzu's Use of Spies (ch05), the Empty City Stratagem / Zhuge Liang (ch05), the
Mukden Incident (ch05), the New Fourth Army Incident (ch03), the Wang Jingwei
puppet regime (ch02), the Comintern (ch02/03/05), 特务 / 汉奸 loaded terms (ch01).

### Renderings settled / reused
+29 glossary rows (book total 151): the Japanese network (Nakanishi Kō, Ozaki
Hotsumi, Ozaki Shōtarō [distinct from Hotsumi], Nishizato Tatsuo, Kawai Teikichi,
Imai Takeo, Tōjō Hideki), Wang Xuewen, Zheng Wendao, Wu Chengfang, Wang Jinyuan,
Chi Buzhou, Arao Sei, Nezu Hajime, Gao Chongwu, Song Ziliang, Li Desen, Qian Ming,
Liu Zhao, Zhang Mingda; and the organs/terms the South Manchuria Railway (满铁),
the Kwantung Army, the East Asia Common Culture Academy / Society, the Institute
of Pacific Relations, the Kōa-in, the Kwantung Army Special Maneuvers (Kantokuen),
Operation Kiri, the Ramsay group. FIXED (deliberate, cascade grep clean): the
岩井公馆 en field "the Iwai Kokan" -> "the Iwai Kōkan" to match the shipped text.
Reused from ch05 unchanged: Pan Hannian, Sorge, Iwai Eiichi, the Ume Kikan, No. 76,
the Iwai Kōkan, Kagesa Sadaaki, Kawashima Yoshiko, Manchukuo, the Tokkō, the South
China Intelligence Bureau, the Central Intelligence Department, the Central
Investigation and Study Bureau, Yan Baohang, Guan Lu, Li Shiqun, Ding Mocun,
Zhang Weiyi, Yuan Shu, Wang Ming.

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json still empty. Chapter 6's inline plates catalogued for a later pass:
the Sorge memorial in Moscow (p226); the US Army Observation Group with Eighth
Route Army weather staff at Yan'an (p249, caption dated 1943; the Dixie Mission
actually arrived July 1944); a three-portrait plate (p251) of Nakanishi Kō with
Ozaki Shōtarō and (per the faded caption) Ozaki Hotsumi in Shanghai, Wang Xuewen,
and Zheng Wendao. Standing question (every 图文 photo, or a curated subset) still
for the commissioner.

### Build / environment (B07)
- EPUB rebuilt: 7 of 14 chapters (ch00-ch06), 134 notes, 158 pagebreaks.
  out/chinas_secret_war.epub. qa_epub PASS; epubcheck 0/0/0/0.
- data/structure.json: +10 rows (ch06 chapter title, subtitle, 8 section headings,
  matched to the OCR strings).
- scripts/resegment_ch06.py: new; the hand-verified paragraph rebuild for ch06.
- ch06 carries printed-page (folio) markers (resegment rebuilds the pagemap).
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff).

## Batch B08 -- Chapter 7 (第七章 锄奸 / "Rooting Out Traitors"), whole chapter + Principal Sources

Scope: ch07s01-ch07s06 (PDF 256-281, printed 220-245), plus the chapter-end
主要资料 rendered as "### Principal Sources". Offset constant printed = pdf - 36,
spot-verified at every section opener off the folio. Chapter 7 is COMPLETE.

### Pipeline run (reused, not re-measured)
- render 256 281 --dpi 300; ocr_crop 256 281 with the MEASURED per-parity crop
  (recto [0.07,0.86], verso [0.17,0.94], top 0.045, bottom 0.93, chi_sim psm 6,
  running-head filter). pgrep -c tesseract = 0 after each run.
- ocr_dual 256 281 (PaddleOCR absent, dual-engine substitute).
- indents 256 281: only p257 line 1 is indented (a NEW paragraph); every other
  page top 258-281 is a continuation, which fixed all page-break seams.
- data/structure.json: +8 rows (ch07 chapter title, subtitle, 6 section headings).
- assemble ch07 256 281 --offset 36 --blank-assist: 216-paragraph boundary
  cross-check (my hand resegment gives 223 body -- the +7 is one-line PUNCH
  paragraphs assemble merges: "延安也公审汉奸了。", "杨宏超策反周崇德？", etc.).
- scripts/resegment_ch07.py: new; HARDCODES the hand-verified ('h'|'b') item list
  read off every page image, rebuilds data/zh/ch07.txt wholesale. 223 body, 9
  headings. This is the authoritative source rebuild (data/zh is gitignored).

### Checks run and results
- verify_unit ch07: parity 223 = 223 OK; numbers checked 223 pairs, 0 unresolved;
  anchors 27 ok.
- check_align ch07: 223/223, median 5.05 en/han, no pair strays > 2.2x. OK.
- check_content: N/A (whole-book tool, needs a docs config). qc_entities: vacuous
  on the flat glossary -- entity survival ensured BY HAND (settled handles reused;
  see below).
- check_apparatus: 0 failures, 19 warnings -- ALL 19 on pre-existing rows (关中分区,
  陇东分区, 绥德, 习仲勋, 何绍南, 于桑, 王震, ...); every NEW ch07 row carries a note.
- check_register --ref out/ch01_reading.md: within tolerance. Dialogue contraction
  0.9/1k (0.46x ref) flagged "little dialogue -- noisy": Chapter 7's quoted matter
  is mostly documents/directives/reports and the author's rhetorical questions;
  genuine conversational speech is a handful of short lines (the "good devil" cry,
  the peasant's curse "why doesn't the Thunder God strike Mao dead?", the county
  head's terse "This is the security section's business"), which ARE contracted.
  Judged on narratorial signals per STYLE: sentence median 21, rhythm CV 0.54.
- Em-dash discipline: first build shipped 6.0/1k; trimmed appositive-gloss dashes
  (STYLE failure mode #1) to colons/commas, down to 4.7/1k (ch06 shipped 4.5).
- Tail verification (rule 4 corollary): the section-6 close (p280, "这反间谍工作...
  能不能让间谍也心向共产党呢？") and the last source entry (Zhao Cangbi, p281) read
  against the scan -- faithful, no drift or invention.
- qa_epub PASS (28 files, 161 notes ref/body/backlink, 184 pagebreaks); epubcheck
  0/0/0/0 (EPUB 3.3).

### OCR / crop-verification (names, numbers, unit designations)
Every proper name crop-verified: high-res eye-read of each page image, cross-read
against BOTH ocr configs via verify_names.py --auto (disagreement filter), and
historical cross-check for notable figures. Settled dense rosters:
- p258 dispatched-agents roster (magnified crop): 拜明耀、宋昌龄、罗鸿沟、蔡长庚、
  撖玉书 (扌+敢, surname Hàn, not 木; crop-confirmed)、李田心、李巨川、高子文、王芝生;
  and 李永茂, 三千元 (3,000 yuan), 73件.
- p268 军统电台 party branch (magnified crop): 张露萍 (书记, 年方二十)、张蔚林、冯传庆、
  赵力耕、杨洸、陈国柱、王席珍.
- p279 NW generals cross-checked against the record: 邓宝珊、高桂滋 (滋, not 汶)、高双成.
- OCR-garble corrections confirmed by context + the disagreement filter: 张严佛
  (not 张玫佛), 高继铨 (not 高继锭), 李茂堂 (not 李茂党), 许继慎 (not 许继司), 朱蕴山
  (not 朱草山), 赵苍璧 (per glossary; book prints 苍壁/璧, same romanization Zhao Cangbi).

### Number-check noise added (data/noise.txt, B08 block)
All flags classified as noise (numeral inside a name/place/idiom/ordinal, or an
Arabic+万 form whose VALUE is carried in English); NONE was a real dropped quantity
(verified). Arabic+万 carried in English and the literal noised: 140万 (1.4 million
people), 60万/4万石 (600,000 / 40,000 dan), 1600万/1000万斤 (16 million / 10 million
jin), 800万/600万/200万 (border currency). Numeral-in-token noised: 三交 (Sanjiao,
place), 十字岭 (Shiziling), 坂谷政三/马汉三 (三 in names), 赵老五 (五 in bandit name),
王八 (八 in idiom), 万众 (万 in idiom), 第二年 (ordinal), 二是 (enumerator),
数十万 (kept vague), 20世纪80年代 (the 1980s).

### Notes added (27; book total 161)
锄奸/汉奸 (loaded terms, first ch07 use); the Special Branch "dog-beating squad";
Puyi + Wang Kemin (puppet rulers); Zuo Quan (Shiziling, highest CCP officer lost,
CORROBORATED, book styles him chief-of-staff vs actual deputy); the "three links";
the Second Revolutionary Civil War; Shen Zhiyue (infiltrated Yan'an, later Taiwan
Investigation Bureau -- CORROBORATED; the "Mao's secretary" claim UNCORROBORATED,
book calls it bragging); 身在曹营心在汉 (Guan Yu); "On Tactics Against Japanese
Imperialism" (Wayaobao, Dec 1935); the CC Clique vs the Zhu faction; 苦肉计 +
蒋干盗书 (36 Stratagems / Three Kingdoms, tied to the reverse-frame that killed Xu
Jishen); 天人感应; 精兵简政 + Li Dingming (CORROBORATED); the Great Production
Campaign; dan/jin measures; 边币 border currency; the Cheka; Ma Xiwu "Ma the Blue
Sky" (the 锡武/锡五 print variant, the adjudication method, links to 刘巧儿 ch09,
CORROBORATED); Xu Jishen (framed via a KMT counter-espionage ruse, executed 1931,
CORROBORATED; book's 1932 founding date noted); SACO / 中美合作所 (Zhang Luping group
held/killed at the Geleshan prisons); Zhang Luping + the Juntong-radio branch
martyrs (CORROBORATED, surfaced only in the 1980s); Deng Yanda; 反间计 (36
Stratagems, distinct from 离间计 ch06); 智异 (Zhao Cangbi's coinage; he became PRC
Minister of Public Security 1977-83).

### NOT re-noted (already placed earlier; cross-referenced in the note bodies)
特务 / 汉奸 loaded terms (ch01/first-use gloss folded into the new 锄奸 note),
Wang Jingwei puppet regime (ch02), Dai Li / Juntong / Zhongtong (ch01), Hu Zongnan
(ch02), Kang Sheng (ch02), the Xi'an Incident (ch01), the Rectification Movement
(ch02), the New Fourth Army Incident (ch03), Gu Shunzhang / Xu Enzeng / the "Three
Heroes of Longtan" (ch01), Zhang Guotao + the Long March (ch02), Whampoa (ch02),
Kawashima Yoshiko (ch05), Li Zicheng (ch01, re-invoked here), Zengjiayan / Red Crag
(ch03), Sorge (ch05), the 离间计 (ch06, cross-referenced by the new 反间计 note).

### Renderings settled / reused
+37 glossary rows (book total 189). New principal referents (all with notes):
Yang Qiqing, Mizuhara Kiyoshi (provisional; reconstructed Japanese reading),
He Qingyu, Zhang Luping, Zhang Weilin, Feng Chuanqing, Li Maotang, Qin Ping, Zhao
Qufei, Ren Yuan, Shan Buyi, Shen Zhiyue, Xu Jishen, Ma Hansan, Li Dingming, Ma Xiwu
(马锡武, book variant of 锡五), Zuo Quan, Wang Jingwei, Puyi, Wang Kemin, Li Zicheng,
Deng Yanda, Zhu Yunshan, Shi Zhe, Gu Zhengding, Zhu Jiahua, Chen Guofu, Cheng
Yiming, Zhang Yanfo; and the organs/terms 锄奸 / 锄奸部 (rooting out traitors /
Anti-Traitor Department, parallel to the Anti-Traitor Committee), 边保 (the Border
Security), the Shandong Column, the Military Commission's Second Bureau, the
Sacrifice League (牺盟会), SACO (中美合作所), 智异 (the divergence of wits).
Reused UNCHANGED from the ledger: Juntong, Zhongtong, the Eighth Route Army office,
Xi Zhongxun, Ye Jianying, Kang Sheng, Dai Li, Hu Zongnan, Zhu De, Zhou Enlai, Mao
Zedong, Chiang Kai-shek, Bu Lu (布鲁=陈泊), Chen Long, Xu Jianguo, Xu Enzeng, Gu
Shunzhang, Zhang Guotao, Yan Xishan, the Rectification Movement, the Anti-Traitor
Committee, the dog-beating squad, Wang Chaobei, Li Qiming, He Shaonan, Yu Sang,
Zhao Cangbi (glossary 赵苍璧), Deng Baoshan, Suide, Longdong sub-district, Guanzhong
sub-district, the New Fourth Army Incident, the Central Social Affairs Department,
the Central Intelligence Department.

### CONSISTENCY / interested-witness posture
- Partisan voice kept in the text (汉奸 "traitor/collaborator", 特务 for the enemy's
  agents, "our side"); the counter-record lives in the footnotes.
- Anonymized-by-某 people kept anonymized in English (何某, 张某, 田某, 樊某, 肖某,
  梅某, plus 李科长/李秘书 by title): the source withholds the name, so does the
  English. NOT to be "resolved" by a later session.
- 反间计 (counter-espionage stratagem, turning the enemy's spies) kept DISTINCT from
  离间计 (sowing discord, ch06); 锄奸 kept in its specific sense (not generic).
- Source-internal variant rendered faithfully + footnoted: 马锡武 for the documented
  judge 马锡五 (same romanization).

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json still empty. Chapter 7's inline plates catalogued for a later pass:
Yang Qiqing with Deng Xiaoping/Yang Shangkun/Lu Dingyi/Luo Ronghuan at the ERA
front HQ, 1937 (p257); the Yan'an public-trial group and the "children's corps with
red-tasseled spears checking road passes" (p259, p261); the 6th-Plenum presidium
group portrait (p259); Zhu Guifang of the Border Security mail-inspection station
(p263); "Zhang Luping's red secret branch fighting at Juntong's nerve center"
(p268); Mu Fengyun with the author (p269); Wang Chaobei + Li Maotang with the Xi'an
intelligence office, 1949 (p270); Wang Jinxiang + Chen Long at Yan'an (p272); the
Border Security field-team heads, 1945 (p273); Ren Yuan interviewed by the author
(p274); Yu Sang with the "carry-on-to-victory" pumpkin (p276); Zhao Qufei at
Ganquan/Fuxian (p279). Standing question (every 图文 photo, or a curated subset)
still for the commissioner.

### Build / environment (B08)
- EPUB rebuilt: 8 of 14 chapters (ch00-ch07), 161 notes, 184 pagebreaks.
  out/chinas_secret_war.epub. qa_epub PASS; epubcheck 0/0/0/0.
- data/structure.json: +8 rows (ch07 chapter title, subtitle, 6 section headings).
- data/noise.txt: +B08 block (see above).
- ch07 carries printed-page (folio) markers (resegment rebuilds the pagemap).
- Branch consolidation: session started on stray branch
  claude/ch07-rooting-out-traitors-byhq8x (identical to origin canonical at
  e2969f4); reset local claude/chinas-secret-war to origin, deleted the stray
  (local; the remote ref never existed, pruned the stale tracking ref).
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff); all other checker regression tests green.

## Batch B09 -- Chapter 8 (第八章 延安反特第一案 / "Yan'an's First Great Counter-espionage Case"), whole chapter + Principal Sources

Chapter 8 is COMPLETE. One extended case built on "化敌为我服务" (turning the enemy
to serve us): Juntong's Hanzhong "expendable-agent" (死间) training class, Wu
Nanshan's voluntary confession at Qingyang, the line-casting and net-weaving, the
great case, the tracking of the couriers, the independent cell in the Military
Commission's Second Bureau, and the turning of the captured agents. 182 English
body paragraphs (1:1 parity). Ends by setting up Chapter 9's "Rescue Campaign."

### Pipeline run (reused, not re-measured)
- render 282 304 --dpi 300; ocr_crop 282 304 (recto/odd [0.07,0.86], verso/even
  [0.17,0.94], top 0.045, bottom 0.93, chi_sim psm6, running-head stripped);
  ocr_dual 282 304; indents 282 304. tesseract idle 0 after each (pgrep -c = 0).
- data/structure.json: +8 rows (ch08 chapter title, subtitle, 6 section headings).
- assemble ch08 282 304 --offset 36 --blank-assist = 160 body paragraphs (boundary
  cross-check only); scripts/resegment_ch08.py is AUTHORITATIVE (182 body, 9
  headings), a hardcoded hand-verified ('h'|'b') item list read off every page
  image. The +22 gap is the usual: assemble merges the many one-line PUNCH
  paragraphs (section 6 is punch-heavy) and the 18 short Principal-Sources entries.
  Run resegment AFTER assemble (assemble overwrites data/zh/ch08.txt).

### Source read entirely off the scan (every page image read by eye)
Straight text pages OCR cleanly; the plate/roster pages (285-295, 302-304) merge
four-to-eight true paragraphs and inject caption + vertical-running-title bleed, so
the hand resegment stays authoritative. Page-break seams settled with indents.py.

### Crop-verified readings (magnified PIL crops; scratchpad/crops)
- p282 兴隆寺 Xinglong Temple (the class site outside Hanzhong).
- p289 固林 as printed (the Border Region county 固临 romanizes identically, Gulin;
  no reader-facing difference, not footnoted).
- p290 "老三班" the Social Affairs Dept's West China College class; 王珺 Wang Jun
  confirmed by the p291 photo caption "王珺（左）与本书作者".
- p294 "查遍抗陕公、女大、青训班、行政学院" -- 抗陕公 as printed, read as a compression
  of 抗大 (Kangda) + 陕公 (Shaanbei College); the next clause re-focuses on 抗大, so
  the English names both. 抗大二大队九队.
- p295 独立小组 leader 胡士渊 (aliases 胡思瑗、胡耀南、胡有连); 杨效卫（杨子才）;
  夏秉塾（夏珍卿）; cell code name 化名"南卫塾" (romanized "Nanweishu"); 王恕 (not
  上恕), 杨荫唐, 苟振生, 王锦堂.
- Numbers verified by eye: 32 = 主动交代1 + 侦察发现20 + 供出11, 物证7件; 6 fled; the
  1955/603 tallies 320 / 40多下落不明 / 670 (Cheng Muyi's captured report) / 631
  (九期, 教官37) / 55 (Yan'an period) / 160 (newly found); 40多/200多/600多 (final
  source). All rendered in DIGITS per STYLE; the differing scopes footnoted.

### Source-internal variants (rendered faithfully as printed; NOT to be "harmonized")
- 郑崇义 (p285) vs 郑崇文 (p290) for the man whose alias is 陈明 Chen Ming.
- 冯平波 (p290) vs 冯平舟 (p295) for the informant on 朱浪舟/金光.
- 郭继武 (p289 roster, p295 arrest list) vs 郭力群 (p295 situational summary).
- 张秉均 (p292/293/295) vs 张秉钧 (p298) -- identical romanization Zhang Bingjun.
These are the minor low-stakes-discrepancy tier: rendered as printed, left
UNfootnoted (over-noting a roster spelling helps no reader). Anonymized-by-某 people
kept anonymized (秦某; 周某、张某(女)夫妇; 李某、吕某; 陈某).

### The checks (all green)
- verify_unit ch08: parity 182/182; numbers 0 unresolved (--noise data/noise.txt);
  anchors 8 ok.
- check_align ch08: 182/182, median ratio 4.71 en/han, no pair strays > 2.2x.
- check_apparatus: 0 failures (the 19 attestation-note warnings are pre-existing
  rows from earlier chapters, not ch08's -- every ch08 glossary row carries a note).
- qa_epub: PASS (28 files, 21 documents, all links resolve; 169 refs/bodies/
  backlinks). epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.
- check_register --ref out/ch01_reading.md: within tolerance. Dialogue-contraction
  metric is 0.0 and flagged "little dialogue -- noisy": this is a single extended
  case narrative dominated by documents, directives, oaths, and reports (like ch07),
  so the contraction metric is legitimately quiet; judged on narratorial signals.
  em-dash 4.4/1k (trimmed from a 6.4 first draft toward the ch06/ch07 ~4.5 target by
  converting appositive/list-gloss dashes to colons/commas); sentence median 21;
  rhythm CV 0.56. The few conversational lines contracted; documents/oaths/telegrams
  and Kang Sheng's / Dai Li's / Li Kenong's set-piece speeches kept formal.
- Tail verification (rule 4 corollary): the Principal Sources (the tail) read against
  p302-304; final source (Wang Yantang) numbers 40多/200多/600多 carried.

### Number-check noise added (data/noise.txt, B09 block)
祁三益 (Qi Sanyi, 三=San in the name, ~30 occurrences -- the big one); 一江山岛
(Yijiangshan Island, 一=1); 势不两立 (idiom, 两); 五台 (Wutai place, 五=5, one of the
18 special-investigation-group sites). Genuine enumerators (两人/两个/三人/三个/十来个/
一…二…) carried in the English, not noised.

### Notes added (8; book total 169)
1. 死间 "expendable agents" -- Sun Tzu's fifth spy-type (the doomed/dead agent),
   Juntong's term for base-area burrowers (anchor "training class for expendable
   agents"; cross-ref the Sun Tzu spy note ch05, 反间计 ch07).
2. 海底 haidi -- the Juntong secret personal dossier (names/addresses/contacts/
   cipher/oath), the master file keying all clandestine contact.
3. 复兴社 the Renaissance Society -- outer organ of the "Blue Shirts" (cross-ref the
   力行社 Vigorous Action Society note, ch02).
4. 任卓宣（叶青）Ren Zhuoxuan / Ye Qing -- early Communist turned Nationalist
   propaganda theorist; Kang Sheng's model of a usable turncoat (corroborated).
5. The numbers tally -- why 32 vs 40多 vs 55 vs 631 vs 670 vs 320 vs 160 differ
   (single case vs whole Yan'an period vs whole class vs all base areas).
6. 一江山岛 Yijiangshan Island -- the Jan 1955 PLA amphibious assault that captured
   Cheng Muyi's report (corroborated).
7. 保密局 the Bureau of Confidential Investigation -- the postwar (1946) successor to
   Juntong.
8. 白公馆 Baigongguan -- the Juntong Chongqing prison/site, part of SACO (cross-ref
   ch07).

### NOT re-noted (already placed earlier; cross-referenced in the note bodies)
顾顺章 Gu Shunzhang (ch01); 许继慎 Xu Jishen (ch07); the New Fourth Army Incident /
皖南事变 (ch03/ch04); 苦肉计 self-injury ruse (ch07); SACO 中美合作所 (ch07); Sun Tzu's
spies (ch05); the Rescue Campaign / Rectification (ch02); 张国焘 Zhang Guotao,
沈之岳 Shen Zhiyue (earlier chapters); 军委二局 Second Bureau (ch07 glossary).

### Renderings settled / reused (consult glossary.json; 209 rows now, +20 this batch)
- REUSED unchanged: Juntong, Zhongtong, the Border Security (边保) / the Security
  Office (保安处), the Central Social Affairs Department (中社部), the Military
  Commission's Second Bureau (军委二局), Kang Sheng, Li Kenong, Dai Li, Bu Lu (陈泊),
  Zhao Cangbi, Chiang Kai-shek / Generalissimo Chiang, Mao Zedong, the Guanzhong /
  Longdong sub-districts, the Border Region, 特务/国特/汉奸 (loaded, kept), 反间计,
  化敌为我服务, the Renaissance Society (复兴社 = 力行社 apparatus), Kangda,
  Shaanbei College, SACO, Deng Baoshan.
- NEW this batch: the Hanzhong (training) class (汉中特训班/汉训班); the "Dai case"
  (戴案); the Northwest Special Reconnaissance Station (西北特侦站); 死间 "expendable
  agent"; 海底 haidi; principals Wu Nanshan, Cheng Muyi (alias Cheng Yi), Qi Sanyi,
  Li Chunmao, Zhao Xiu, Wang Xingwen, Hu Shiyuan; Ma Wenrui, Li Fushan, Wang Jun,
  Zhou Xing, Ouyang Yi, Qian Yimin. One handle per referent, book-wide.
- 反用/逆用 = "counter-use" / "turning the use" (近似 Sun Tzu's 反间 = the "turned
  spy"); kept distinct from 反间计 (counter-espionage stratagem).
- The p292 quatrain rendered as a quoted inline verse within its paragraph (kept 1:1
  parity; no {p} block, since it is embedded mid-paragraph in the source).

### CONSISTENCY / interested-witness posture
- Partisan voice kept in the text (特务 for the enemy's agents, 汉奸 traitor,
  "匪区"/"奸党" as the Nationalists' own scare-quoted usage); counter-record and
  verdicts (corroborated) live in the footnotes.
- The chapter is sympathetic to the "turn the enemy" policy and closes by tying the
  case to the Rescue Campaign; that framing is the author's, rendered faithfully.

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json still empty. Chapter 8's inline plates catalogued for a later pass:
portrait of Wu Nanshan (p283); portrait of Li Fushan, Longdong security-section
chief (p284); portrait of Zhao Cangbi (p285); a facsimile of Zhou Xing's handwritten
letter to Bu Lu on continuing the investigation (p289); the Yan'an New Market street
scene (p292); portrait of Li Chunmao (p293); Wang Jun (left) with the author (p291);
a facsimile of Chen Long's handwritten letter to Bu Lu on Zhang Zhigang's flight
(p297). Standing question (every 图文 photo, or a curated subset) still for the
commissioner.

### Build / environment (B09)
- EPUB rebuilt: 9 of 14 chapters (ch00-ch08), 169 notes, 206 pagebreaks.
  out/chinas_secret_war.epub. qa_epub PASS; epubcheck 0/0/0/0.
- ch08 carries printed-page (folio) markers (resegment rebuilds the pagemap,
  printed 246-268).
- Branch consolidation: session started on stray branch
  claude/china-secret-war-ch08-96v4kk (identical to origin/claude/chinas-secret-war
  at 704a9b3); reset local canonical to origin, deleted the stray (local + the remote
  ref existed and is removed at push time). All work on claude/chinas-secret-war.
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff); all other checker regression tests green. PaddleOCR
  absent (expected); used scripts/ocr_dual.py.

## Batch B10 -- Chapter 9 (第九章 "抢救运动" / "The Rescue Campaign"), whole chapter + Principal Sources

Chapter 9 is COMPLETE. The book's most contested chapter: how the hunt for agents,
riding the Rectification, broadened into a purge (审干 -> 抢救运动) that swept up the
innocent -- 逼供信 ("coerce, confess, believe"), "agents as thick as hemp," Kang
Sheng's central role, the fabricated "Red-Flag Party," and Mao's apology. Eight
sections: the "case-cracking in step with the campaign" timeline; the "old-case"
suspects and the Shandong/Huxi anti-Trotskyist purge; the "four great agents" and
the Southern Committee wreck; the April 1943 mass arrests; Kang Sheng's "Rescue the
Fallen" speech and the torture catalogue; Mao's apology and the screening; the "Liu
Qiao'er"/Ma Xiwu counterpoint; and "go to the front and draw your own conclusions,"
closing by likening the campaign to the Cultural Revolution. 368 English body
paragraphs (1:1 parity).

### Pipeline run (reused, not re-measured)
- render 305 342 --dpi 300; ocr_crop 305 342 (recto/odd [0.07,0.86], verso/even
  [0.17,0.94], top 0.045, bottom 0.93, chi_sim psm6, running-head stripped);
  ocr_dual 305 342; indents 305 342. tesseract idle 0 after each (pgrep -c = 0).
- assemble ch09 305 342 --offset 36 --blank-assist = 330 body paragraphs (boundary
  cross-check only); scripts/resegment_ch09.py is AUTHORITATIVE (368 body, 11
  headings), a hardcoded hand-verified ('h'|'b') item list read off every page
  image (pp. 305-342 all read by eye, cross-checked vs psm6 + ocr_dual psm4). The
  +38 gap is the usual: assemble merges the many one-line PUNCH paragraphs (this
  chapter is punch-heavy -- the "analyze the agent" set-pieces, the slogan quotes)
  and the short Principal-Sources entries.
- resegment_ch09.py ALSO rebuilds data/pagemap/ch09.json (38 folios, printed
  269-306) from a hand-recorded PAGE_STARTS list, because assemble's pagemap is
  keyed to its 330-paragraph segmentation (drifts against the 368 reading) AND
  skipped folio 278. The hand pagemap is accurate to the reading file.

### Page-seam method (indents.py is UNRELIABLE on digit-initial lines)
Every page-break seam settled by eye + logic, NOT by indents.py alone: indents.py
mis-flagged p306/p318/p328 tops (all digit- or date-initial "1939年.../1943年...")
as continuations when they are indented new paragraphs. Rule applied: a physically
indented page top that follows sentence-final 。？！ starts a NEW paragraph; a
non-indented top, or one whose previous page ended mid-clause (；, a cut word), is a
continuation.

### Crop-verifications (magnified PIL crops)
- p318 (printed 282): the Ren Bishi quote prints "这些一是被迫误入歧途的青年" --
  crop-verified 是 (not 时). "一是" does not parse as a word; an OCR-era/print
  artifact for 一时 ("for a time"). Rendered to plain sense ("coerced for a time
  onto the wrong road"). Logged here per the OCR-glitch rule.
- p310 (printed 274): "还给后三科的女干部带孩子" -- 后三科 confirmed (a Border
  Security section); rendered "the rear third section."
- p338 (printed 302): "219个特务中其中165个" -- 219/165 confirmed (Arabic in source).
- p310/p340: 何圭人 (He Guiren) confirmed via Lin Lifu's document title on p340
  (《党应为何圭人和方今同志平反昭雪...》); not footnoted as a variant.

### Numbers (verify_unit clean: 368 pairs, 0 unresolved)
Real quantities carried as digits/words: 五人 -> "five"; 1400多 -> "over 1,400";
两个 -> "two"; 两千二百多 -> "2,200"; 908, 25, 500多, 219/165, 544/208/752/49/2,
2475, 60%/30%, 99%, 91万/19块/近一亿 all carried. data/noise.txt += 六 entries
(numerals inside idioms/designations, each commented): 五花大绑 (5), 一而再、再而三
(3), 十几万字 (Arabic+万, value in English), 七大 (7, the Seventh Congress
designation), 百忙之中 (100), 两千二百多 (百 decomposition artifact; value carried),
野百合花 ("Wild Lily", 百 is part of 百合 "lily", NOT a numeral).

### Apparatus (check_apparatus 0 failures)
- notes.json: +16 notes (book total 185). Interested-witness counter-records with
  stated verdicts (fact-checked against Wikipedia / Baidu Baike / Gao Hua's *How the
  Red Sun Rose* / Dai Qing on Wang Shiwei / the Pan Hannian scholarship -- NEVER
  Grok/Grokipedia, which appeared in results and was refused per rule 5):
  the Rescue Campaign (~30,000 swept up; CORROBORATED); Kang Sheng's central role
  (cross-ref ch02; Cao Yi'ou ran Yan'an county; CORROBORATED); Wang Shiwei
  (CONTRADICTED: shown alive in 1944, but secretly killed 1 July 1947, rehabilitated
  Feb 1991); the Huxi purge (CORROBORATED); Kang Sheng's 1938 Chen Duxiu smear; the
  "Red-Flag Party" fabrication (1981 rehabilitation; CORROBORATED); Pan Hannian's
  1955 fate (Wang Jingwei charge, rehab 1982; CORROBORATED); Mao's apology
  (CORROBORATED); plus reader-model glosses (Kawashima Yoshiko, Wang Kemin, the
  Southern Committee, Dou E / "snow in June," the Comintern dissolution, Jiang
  Nanxiang, Liu Qiao'er / Feng Zhiqin, Xiong Dazhen).
- glossary.json: +10 rows (219 total): 抢救运动, 审干, 逼供信, 甄别, 南委, 红旗党,
  山东肃托, 复兴社, 特务如麻, 老号. REUSED unchanged: 整风, 康生, 潘汉年, 三青团,
  戴案, 马锡武 (= the judge Ma Xiwu, noted ch07), 边保, 中社部, 保安处, Juntong,
  Zhongtong. Cross-referenced (not re-noted): Kang Sheng (ch02), Rectification
  (ch02), 逼供信 (ch01), Xi Zhongxun (ch04), Ma Xiwu / Ma Qingtian (ch07).
- Loaded terms 特务/汉奸/国特 kept as the author uses them (traitor / agent / secret
  service); loaded-term note already placed early in the book.

### CONSISTENCY / interested-witness posture
- The partisan account is rendered faithfully in the TEXT (the campaign's absurd
  charges, Wang Shiwei "living well" in 1944, Kang Sheng's self-serving 7th-Congress
  defense), with the counter-record and historians' verdict in the FOOTNOTES. The
  author is himself markedly critical here -- he pins the blame on Kang Sheng, calls
  the "analyze the agent" logic "past all imagining," and closes by likening the
  Rescue Campaign to the Cultural Revolution ("the same leader... the same
  'strategist,' Kang Sheng"). That verdict is his; rendered as printed.
- 汉奸 rendered "traitor" throughout (40x, consistent). 边保 = "Border Security" (54x),
  保安处 standalone = "the Security Office" (15x) -- kept distinct.

### Register (check_register --ref out/ch01_reading.md)
Within tolerance. contr 1.4/1k (0.66x ref, above the 0.5x floor); em-dash 0.0/1k
(all appositive-gloss/list dashes converted to colons/commas -- well under the
~4.5/1k target); shall% 100% is deliberate: both "shall" instances are inside the
quoted 1941 anti-traitor policy DOCUMENT (an exempt formal register). Conversational
quoted speech contracted (Li Kenong, Wang Zunji, Mao); documents/directives/slogans/
oaths kept formal.

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json still empty. Chapter 9's inline plates catalogued for a later pass:
Central Party School auditorium (p307); portrait of Lin Lifu (p310); "one of the
four great agents" Wang Zunji (p314); the Rescue-rally photo (p320); portrait of Yu
Bingran in Chongqing (p323); facsimile of Mao's "not one to be killed" instruction
(p325); Shi Zhe in Moscow (p327); portrait of Wang Shiwei (p330); portrait of Yuan
Jing (p332); a scene from the opera (p333); Li Rui and Hu Sha, each with the author
(p334); 7th-Congress delegates entering the hall (p337). Standing question (every
图文 photo, or a curated subset) still for the commissioner.

### Build / environment (B10)
- EPUB rebuilt: 10 of 14 chapters (ch00-ch09), 185 notes, 244 pagebreaks.
  out/chinas_secret_war.epub. qa_epub PASS; epubcheck 0/0/0/0.
- ch09 carries printed-page (folio) markers (resegment rebuilds the pagemap,
  printed 269-306). ch01 zh parity 269/299 and ch03 folio markers still open
  (corrections-pass tasks; no note cites a ch03 folio).
- Branch consolidation: session started on stray per-task branch
  claude/ch09-rescue-campaign-wl9tnm (identical to origin/claude/chinas-secret-war
  at b1bfd45); reset local canonical to origin, deleted the stray (local + stale
  remote-tracking ref pruned). All work on claude/chinas-secret-war.
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff); all other checker regression tests green. PaddleOCR
  absent (expected); used scripts/ocr_dual.py.

## Batch B11 -- Chapter 10 (第十章 "阳谋" / "The Open Scheme"), whole chapter + Principal Sources

Chapter 10 is COMPLETE. The post-war pivot: the Japanese surrender, the Chongqing
negotiations "played in earnest" while both sides race for position, the "cold-storage
spies" reactivated for the coming civil war, the "Democratic Allied Army" wave of
defections, the "Latter Three Heroes" (Xiong Xianghui / Chen Zhongjing / Shen Jian in
Hu Zongnan's HQ), the Great Withdrawal from Yan'an (March 1947), and the Yan'an
guerrillas. Eight sections. 355 English body paragraphs (1:1 parity). The chapter is
unusually candid for this book: it quotes the internal reckoning that 2,296 people
were killed in the Border Region in 1947, over half of them wrongly, and gives the
execution of Wang Shiwei plainly.

### Pipeline run (reused, not re-measured)
- render 343 383 --dpi 300; ocr_crop 343 383 (recto/odd [0.07,0.86], verso/even
  [0.17,0.94], top 0.045, bottom 0.93, chi_sim psm6, running-head stripped);
  ocr_dual 343 383; indents 343 383. tesseract idle 0 after each (pgrep -c = 0; the
  ocr_crop background job's "exit 1" was only `pgrep -c tesseract` returning nonzero
  on a zero count, i.e. success).
- assemble ch10 343 383 --offset 36 --blank-assist = 330 body paragraphs (boundary
  cross-check only); scripts/resegment_ch10.py is AUTHORITATIVE (355 body, 11
  headings), a hardcoded hand-verified ('h'|'b') item list read off every page image
  (pp. 343-383 all read by eye, cross-checked vs psm6 + ocr_dual psm4). The +25 gap
  is the usual: assemble merges the many one-line PUNCH paragraphs (this chapter is
  punch-heavy) and the short Principal-Sources entries, and merges four-to-eight true
  paragraphs on the plate/column-wrap pages.
- resegment_ch10.py ALSO rebuilds data/pagemap/ch10.json (41 folios, printed 307-347)
  from a hand-recorded PAGE_STARTS list (each printed page -> the 0-based body index
  of its first STARTING paragraph); strictly increasing, verified by the script.

### Page-seam method (indents.py unreliable on digit-initial lines)
Every seam settled by eye + logic. Digit-/date-initial page tops (e.g. p344 top
"第二次淳化事件爆发！" after a sentence-final period = NEW; the many "8月.../1946年..."
tops) resolved by the rule: indented top after 。？！ = NEW; non-indented top, or one
whose previous page ended mid-clause / on a cut word, = continuation. Several
paragraphs legitimately span a page break (e.g. b14 苗乐山 p344->345; b25 陈汝杰
p346->347; b285 祁三益 roster p375->376).

### Crop-verifications (magnified PIL crops; verify_names --auto + Pillow)
- p315 "1945年9月5日，日本投降" -- crop-verified the digit is 5 (not 2/9). This is a
  SOURCE ANOMALY: the surrender was Aug 15 (announcement) / Sept 2 (Missouri) / Sept 9
  (China-theater, which the book gives correctly two paragraphs below). Rendered as
  printed ("September 5, 1945") and FOOTNOTED.
- p317 "陇耀师长" -- crop-verified 陇耀 (Long Yao), a Yunnan-army division commander.
- p323 vs p338: the Nationalist general is printed 刘戡 (Liu Kan) on printed 323 and
  刘勘 on printed 338 -- an internal PRINT VARIANT of the same person. Rendered "Liu
  Kan" throughout; NOT footnoted (invisible in pinyin, not load-bearing; minor tier).
- p337 "不留后路是老擤" -- crop-verified 擤 (扌+鼻); a Shaanbei dialect word for
  foolishness. Rendered for sense ("plain foolishness"); no note (minor tier).
- p337 "蛮婆" -- crop-verified; rendered "country crone" (an agent's fortune-teller
  disguise).
- p342 "五丈五云梯" -- crop-verified; a scaling ladder 5.5 zhang tall.
- p339 "章炳南误写为张炳南" -- the source itself notes the martyrs' monument misprints
  the name; rendered as printed (the misprint kept), the author's own observation.
- Dense figure rosters cross-checked against BOTH ocr configs (agree): p337
  7663/4592/15挺/114次/614/1281; p334 2296 killed; p311 374%; p329 3.37:1; p336
  113->2. All carried in the English as digits.

### Numbers (verify_unit / check_numbers --noise data/noise.txt): 0 unresolved
Reworded 5 pairs to carry values the parser recognizes: the 四类 list -> "first/
second/third/fourth"; 十二万 -> "120,000"; 四国外长 -> "the four powers"; 左右两个兵团
-> "the two corps, left and right"; 两人逃亡 -> "only two ... fled". Extended
data/noise.txt (B11 block): 14万 (Arabic+万 the parser mangles to a spurious 1;
carried as "140,000"), 一失足成千古恨, 两眼一抹黑, 陈云、彭真二人, 不远千里,
二十里铺, 三十里铺, 七七八八, 夫妻两人, 前一日, 零件 (零=spare, not 0), 五华山, 五原,
祁三益 (三 in the name), 两区. TOOLING FIX (do not revert): the pre-existing noise
rule "4万" (intended for 4万石) was greedily eating the "4万" inside "14万" and leaving
a spurious "1"; scoped it to "4万石" per its own comment. 野百合花 and 七大 (already in
noise) also cover this chapter's 《王实味与野百合花》 and 七大.

### Apparatus
- notes.json: +22 ch10 notes (book total 207). New this chapter: 阳谋 (open scheme,
  anchored on the "kicking each other under the table" line, NOT the H1 -- the builder
  does not anchor chapter-title headings); Chongqing negotiations; Feast at Hongmen;
  Jiang Gan / Zhou Yu (Three Kingdoms); the Sept-5 surrender-date anomaly; the 16th-
  parallel Potsdam arrangement; Long Yun's ouster; Bao Dai; the Diaoyu aside (interested-
  witness); cold-storage / strategic spy; Yan Youwen (identity secret to 1993,
  corroborated via his daughter + Luo Qingchang); the Latter Three Heroes + Longtan
  parallel (KEY; Xiong Xianghui's memoir the principal source); tesuji (go term);
  Empty Fort Stratagem; Gao Shuxun revolt / movement; the "democratic army" framing
  (interested-witness); Li Bai the radio operator; paofan; Wang Shiwei's execution +
  1991 rehabilitation (cross-ref ch09); Juntong's "enter alive, leave only dead";
  huanxiangtuan; Wu Manyou the model laborer's fall.
- CROSS-REFERENCED, not re-noted (already placed): Longtan Trio / 龙潭三杰 (ch01);
  Kawashima Yoshiko + her brother Xiandong/宪东 (ch05); Shen Anna (ch03); Puyi (ch07);
  Xi Zhongxun (ch04); Wang Shiwei's "Wild Lily" and full execution/rehab account
  (ch09); Kang Sheng, Rectification (ch02); Juntong/Zhongtong, Central Special Branch,
  the Social Affairs Department, the Border Security (earlier chapters).
- glossary.json: +15 rows (234 total): 阳谋, 重庆谈判, 双十协定, 冷藏间谍, 战略间谍,
  后三杰, 民主联军, 延安大撤退, 跑反, 高树勋运动, 还乡团, 冈村宁次, 傅作义, 阎又文,
  熊向晖, 龙云, 卢汉, 高树勋, 习仲勋 (4 of these already present -> left untouched).
  REUSED unchanged: 边保, 中社部, 中情部, 保安处, Juntong, Zhongtong, 胡宗南, 康生,
  李克农, 毛泽东, 周恩来, 蒋介石/老蒋, 潘汉年, 闲棋冷子 (ch03), 汉训班, 三边, 关中分区,
  陇东. check_apparatus: 0 failures (the 19 attestation-note warnings are all on
  pre-existing OLD rows, not this batch's).

### Consistency / interested-witness posture
- The partisan account is rendered faithfully in the TEXT (the Chongqing talks as
  Chiang's "sham play," the "democratic" uprisings, the Diaoyu aside, the wry
  "this place will yield oil someday" over the buried executed). The counter-record
  and verdicts are in the FOOTNOTES. Notably the author is himself candid here about
  the wartime killings (2,296, over half wrong) and about Wang Shiwei's death.
- Handles held fixed: Border Security (56x), Social Affairs Department (17x), Juntong
  (12x)/Zhongtong (11x), Hu Zongnan (36x), old Chiang (5x)/Chiang Kai-shek (26x),
  Guanzhong sub-district. No slips (grep for Hu Tsung-nan/Chungking/Yenan/secret
  police = 0). Anonymized-by-某: none new. No literal <i> in the reading (builder-safe).

### Register (check_register --ref out/ch01_reading.md)
Within tolerance. contr 7.6/1k (3.7x ref -- healthy; the chapter carries real
conversational speech: Mao's jokes to Hu Jingduo and about the "two directors," Su
Ping's "your mule goes to fight," Hao Su's "never mind these pots and jars," Long
Yao's outburst -- all contracted). em-dash 0.0/1k (appositive-gloss and list dashes
converted to colons/commas). shall% 0. Documents/directives/telegrams (the two 1947-48
Northwest Bureau killing directives, the Truman quote) kept formal.

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json still empty. Chapter 10's inline plates catalogued for a later pass:
Bu Lu directing Miao Leshan, 1944 (printed 309); Li Maotang (310); Mao's party at the
Yan'an airfield before the Chongqing flight, w/ Zhang Zhizhong/Hurley/Wang Ruofei/Hu
Qiaomu/Chen Long (313); Yang Huanglin and Huang Bin, codebook copyists (314); Li
Shiying (319); Yan Youwen (left) and Wang Yu (right) (321); Shen Anna's handwriting
(322); Xi Zhongxun at NW Field Army HQ (337); the reporters' tour of Yan'an, Aug 1947
(330); Luo Fei with the author (331); the Yan'an PSB building (338); the grove where
Liu Wu's group was killed, outside Yuxiang Gate, Xi'an (340); the Yihezhen/Yanjiaqu
cave dwellings (335); the recapture of Yan'an, 22 Apr 1948, Border Security gate (343).
Standing question (every 图文 photo, or a curated subset) still for the commissioner.

### Build / environment (B11)
- EPUB rebuilt: 11 of 14 chapters (ch00-ch10), 207 notes, 285 pagebreaks.
  out/chinas_secret_war.epub. qa_epub PASS; epubcheck 0/0/0/0.
- ch10 carries printed-page (folio) markers (resegment rebuilds the pagemap, printed
  307-347). ch01 zh parity 269/299 and ch03 folio markers still open (corrections-pass
  tasks; no note cites a ch03 folio).
- Branch consolidation: session started on stray per-task branch
  claude/china-secret-war-ch10-3asnf9 (0 commits ahead of, 24 behind
  origin/claude/chinas-secret-war). Reset local canonical to origin (b92d035),
  deleted the stray local branch and pruned the stale remote-tracking ref. All work on
  claude/chinas-secret-war.
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff); all other checker regression tests green. PaddleOCR
  absent (expected); used scripts/ocr_dual.py.

## Batch B12 -- Chapter 11 (第十一章 大策反 / "The Great Turning"), whole chapter + Principal Sources

Chapter 11 is COMPLETE. The crest of the intelligence war. Seven sections. 236 English
body paragraphs (1:1 parity with 236 zh body lines; 10 zh heading lines vs 9 en, the
usual chapter-subtitle fold). The SIGINT/radio-direction-finding duel on the Loess
Plateau as Mao's <1,000-man Ninth Detachment plays cat-and-mouse with Hu Zongnan's
230,000; Lü Chu's seven-man radio group reading Hu Zongnan's battle orders before his
own generals (Fumei 43,000, Qinling 13,000); the Wang Shijian network collapse and the
Five Martyrs of North China; Sun Tzu's "subdue the enemy without fighting" as generals
are turned (861.7M enemy eliminated, 1.89M / 21% by turning); the Wu Shi case and the
Taiwan martyrs (中将之死); and the founding of the PRC (建国大业).

### Pipeline run (reused, not re-measured)
- render 384 410 --dpi 300; ocr_crop 384 410 (recto/odd [0.07,0.86], verso/even
  [0.17,0.94], top 0.045, bottom 0.93, chi_sim psm6, running-head stripped);
  ocr_dual 384 410; indents 384 410. tesseract idle 0 after each (pkill -g + pgrep -c
  = 0). ocr_dual's wrapper timed out at 2m after printing p410 (work finished; killed
  the group, confirmed both dirs have all 27 pages).
- assemble ch11 384 410 --offset 36 --blank-assist read 197 paragraphs / 0 headings
  (merged the many one-line PUNCH paragraphs and the plate/wrap pages, as expected).
- METHOD: read every page image (data/png/p0384..p0410) by eye, transcribed each TRUE
  source paragraph, verified against BOTH ocr configs. scripts/resegment_ch11.py
  HARDCODES the verified ('h'|'b', text) list -> data/zh/ch11.txt (246 items: 236 body,
  10 heading) and rebuilds data/pagemap/ch11.json from PAGE_STARTS (27 folios 348-374,
  validated strictly increasing). Section heading "6.中将之死" sits mid-p403, AFTER the
  Hao Pengju / Zhou Gao tail of section 5 -- placed accordingly.

### Crop-verified this batch (magnified PIL crops, dual-OCR disagreement)
- p384 "二十三万大军" (Hu Zongnan 230,000; faded, both configs mangle) -- read by crop.
- p389 "府西分区"/"分州" as PRINTED (both configs + eye agree 分州, not 邠州); "刘丕清"
  Liu Piqing; "吕出" Lü Chu (aged 15).
- p390 seven-man roster 薛浩然/徐学章/李福泳/高健/王冠洲/赵继勋 (+Lü Chu = 7); psm4
  matched the eye read exactly.
- p392 FIVE MARTYRS roster + ranks crop-verified across two lines (少将作战处长谢士炎 /
  少将军法处副处长丁行 / 少校参谋石淳 / 代理作战科长朱建国 / 空军第二军区参谋赵良璋);
  re-confirmed p394 (main + caption) and p403 (martyr roll).
- p394 段云鹏 (cat-burglar), 李政宣 (traitor clerk), 京兆东街24号.
- p399 caption roster (50th Army: 白肇学/148, 徐文烈 commissar, 曾泽生 cmdr, 陇耀/149,
  刘惠之 propaganda, 李佐/150) crop-verified.
- p402 chapter statistics 861.7万 / 320起189万 / 21% -- triple agreement (eye+psm6+psm4).
- p404 Taiwan martyrs 吴石/朱枫/陈宝仓/聂曦; 何遂.
- p409 张鼎中 entry prints "刘进昌" for BOTH the Baoding station chief AND the recruited
  deserter -- an apparent source slip; rendered faithfully + footnoted.
- p410 author names 杨喆 (喆 = twin 吉, "Yang Zhe"), 韩兢 (Han Liancheng's daughter).

### The checks (all run; results)
- verify_unit ch11: parity 236/236, numbers 0 unresolved, anchors 19 ok. check_align:
  236/236, median 4.99 en/han, no pair strays >2.2x.
- Number check noise added (data/noise.txt, Batch B12 block): 千忙万忙, 十万火急,
  二万五千里长征, 四平战役, 861.7万, 189万, 40两, 名垂千古 (numerals inside
  idioms/names/Arabic+量词; each carries its value in the English). REAL quantities
  carried as digits/words: 150 li, "five agents in all" (谢士炎等五人), 500,000
  swallowed 500,000, 43,000, 13,000, 230,000, 8.617 million, 1.89 million, 21%, 40
  taels, 34 days, 40 days, twelve hours, six days.
- Entity survival BY HAND (qc_entities vacuous): Juntong 11x, Border Security 11x, Hu
  Zongnan single form, Xibaipo 8x, Wu Shi 35x -- no drift; 保密局 unified to "Bureau of
  Confidential Investigation" (matched ch08). Distinct near-namesakes kept apart: 刘光国
  Liu Guangguo (11th-War-Zone clerk) vs 刘光典 Liu Guangdian (courier, held out 4 yrs,
  killed 1959). 甘陵 (Ganling) is a PERSON, not a place.
- Tail verification: Principal Sources (p409-410) transcribed and name-verified
  entry-by-entry against the scan; last entries (何嘉, 郝在今 -- the author's own
  《协商民主》 self-cited) read against the folios.

### Apparatus
- notes.json: +19 notes (ch11), book total 226. Interested-witness verdicts stated in
  the note: 卫立煌 (CONTESTED -- historians divided on whether he colluded or merely
  preserved his forces; no documents released); 郭汝瑰 (corroborated, posthumously
  confirmed); Five Martyrs (corroborated; executed 1948, Nanjing/Yuhuatai per the
  record); Dai Li death 16/17 Mar 1946; 羊马河 vs 瓦窑堡 (the 135th Bde was annihilated
  at Yangmahe, 14 Apr 1947, near Wayaobao -- book names the general area); Hu Zongnan
  230k (low end of the 230-250k range); Wu Shi case (corroborated; shot Machangding
  10 Jun 1950); 阎又文 ghostwriter (well documented); Shen Chong incident; Li Bai (the
  radio martyr, "永不消逝的电波"); Jing Ke's Yi-River farewell; Chen Lin/Luo Binwang
  manifestos; 不战而屈人之兵 + 止戈为武 gloss; 电子对抗 gloss; the 刘进昌 source slip.
- glossary.json: +15 rows (249 total): 大策反, 策反, 华北五烈士, 不战而屈人之兵,
  电子对抗, 保密局, 联络部, 王石坚, 吴石, 陈明仁, 郭汝瑰, 曾泽生, 李白, 沈崇, 五一口号.
  REUSED unchanged: 边保, 中社部, 中情部, Juntong, Zhongtong, 胡宗南, 傅作义, 阎又文,
  卫立煌, 韩练成, 康生, 李克农, 毛泽东, 周恩来, 蒋介石/老蒋, 潘汉年, 熊向晖, 后三杰,
  空城计, 龙潭三杰, 二万五千里长征, 中美特种技术合作所 (SACO). check_apparatus: 0
  failures (the 19 attestation-note warnings are all pre-existing OLD rows).

### NOT re-noted (already placed earlier in the book)
- Empty Fort Stratagem / Zhuge Liang (ch05, ch06, ch10) -- referenced, not re-noted.
- Shen Anna (ch03); Latter Three Heroes / Longtan Trio (ch03, ch10); the Long March
  (ch02); Juntong (ch01); Zhongtong; Whampoa (ch02, ch07); SACO / Sino-American
  Cooperative Organization (ch07, ch08); the Bureau of Confidential Investigation
  (ch08); the Border Security; the Social Affairs Department.

### Register (check_register --ref out/ch01_reading.md)
Within tolerance. contr 0.0/1k (little quoted dialogue -- the chapter is documentary:
telegrams, directives, the Chiang review批示, Fu Zuoyi's open telegram, Mao's three
principles, all kept formal; the metric is noise here, judged on narratorial signals).
em-dash 2.0/1k (below the ch01 ref 3.4; appositive-gloss and list dashes converted to
colons/commas). shall% 0. Sentence median 22, rhythm CV 0.63.

### Figures: still DEFERRED (deliberate; commissioner decision pending)
figures.json still empty. Chapter 11's inline plates catalogued for a later pass: Mao
(front right) on the trek across N. Shaanxi, 1947 (printed 349); Tong Xiaopeng (350);
Fumei surrender + 1st FA 18th Corps planting the flag on the Qinling (355); Liu Xiao
and Zhang Zhiyi, Beijing 1954 (356); the five martyrs + Zhao Wei, 6 portraits (358);
Ganling and Liu Guangguo (360); Zhang Kexia (left) and He Jifeng (362); the 50th Army
leaders after the Changchun revolt (363); Xu Chuguang (366); Chiang Kai-shek with Jia
Yibin at Lushan (365); Zhou Gao, CCP agent / Juntong major general (367); the five
martyrs again (358); Xiao Minghua (369); Nie Xi (369); the 1947 student "Anti-Hunger,
Anti-Civil-War, Anti-Persecution" march (371). Standing question (every 图文 photo, or
a curated subset) still for the commissioner.

### Build / environment (B12)
- EPUB rebuilt: 12 of 14 chapters (ch00-ch11), 226 notes, 312 pagebreaks.
  out/chinas_secret_war.epub. qa_epub PASS; epubcheck 0/0/0/0.
- ch11 carries printed-page (folio) markers (resegment rebuilds the pagemap, printed
  348-374). ch01 zh parity 269/299 and ch03 folio markers still open (corrections-pass
  tasks; no note cites a ch03 folio).
- Branch consolidation: session started on stray per-task branch
  claude/ch11-batch-b12-nw45qb (at 32517ab, same as origin/claude/chinas-secret-war,
  0 commits ahead). Reset local canonical to origin, did all work on
  claude/chinas-secret-war; stray branch to be deleted (local + remote) at push.
- setup.sh regression "hook stands down on template stub" still FAILS benignly
  (HANDOFF holds a real kickoff); all other checker regression tests green. PaddleOCR
  absent (expected); used scripts/ocr_dual.py.
