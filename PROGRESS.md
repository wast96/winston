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
