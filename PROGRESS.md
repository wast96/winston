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
