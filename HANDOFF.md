# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with the block below PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 3 (Chapter 2, sections 4-5) is COMPLETE: translated, annotated, built, all
gates green (parity 142=142, numbers 0 unresolved, content 0 displaced, entities
0, register within tolerance, qa_epub PASS, epubcheck 0/0/0). The block below is
the Batch 4 kickoff, ready to paste.

## Message to paste into the next chat

```
Chen Yangshan B04

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset: printed = pdf - 11
(constant). Chapter 1 is the FROZEN register reference
(check_register.py --ref out/ch01_reading.md). Chapters 1 and 2 are done.

Do Batch 4 = Chapter 3 (ch03), PDF 93-115, printed 82-104, end to end per the
CLAUDE.md pipeline:
  - THE UNIT IS THE WHOLE CHAPTER = a NEW file out/ch03_reading.md (three
    "### 1./2./3." section headings, English titles from book.json) and a new
    data/zh/ch03.txt. Add "ch03" to data/check_config.json (docs + sources) so
    verify_unit.py ch03, check_structure/check_content --config
    data/check_config.json, check_align.py ch03 all run on it. Sections:
    1 = 西安事变隐蔽战线高奏凯歌 (the Xi'an Incident on the hidden front; PDF 94);
    2 = 回到延安，整风学习为作战 (back in Yan'an, the Rectification study; PDF 103);
    3 = 三问康生，战友鲜血同志泪 (three questions for Kang Sheng; PDF 110). Chapter
    opener recto PDF 93 carries a photo above the heading — SKIP it (per ch01/ch02).
  - BEFORE translating, read the final two pages of out/ch02_reading.md (the 1987
    "New Sichuan News Agency" recollection closing Chapter 2; the voice IS those
    pages) and STYLE.local.md.
  - render 93-115; OCR with the SAME crop as ch01/ch02 (do-not-revert list below):
    ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985 --top 0.08
    --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945, VERSO (PDF
    odd) --bottom 0.915, run per-page so the parity-correct bottom applies. Run
    ocr_dual.py; verify pgrep -c tesseract is 0.
  - WATCH THE SILENT OCR-LOSS (CONFIRMED every batch): tesseract drops an isolated
    paragraph-final SHORT line. Any OCR paragraph ending WITHOUT sentence-final
    punctuation before a blank is a dropped-tail suspect; VERIFY EVERY PAGE BOTTOM
    against the scan and restore it. data/zh is hand-assembled from corrected OCR +
    scans, one source paragraph per line. Keep portrait bio-boxes and photo
    captions OUT of data/zh (they are figure captions, translated into
    figures.json) so parity stays 1:1.
  - eyeball EVERY page for figures; find_figures.py has matched the real plates
    every batch but MISSES line art and mis-detects on dense text - verify each by
    eye, and crop clean images to data/figs/. Photo/portrait captions go in
    figures.json (translated). FIGURE ALT MUST CONTAIN NO STRAIGHT DOUBLE QUOTES
    (they break the alt="..." attribute -> epubcheck fatal); use single quotes.
  - Write English one paragraph per source line. Use PLAIN ASCII in the reading
    file: straight quotes " ', literal em dash — ONLY for genuine interruption
    (the builder curls quotes and turns ... into an ellipsis at render; it does
    NOT make em dashes from --). NO dashed-in appositive glosses (failure mode #1):
    a fact set off in a dash-pair belongs in parens, a comma clause, or its own
    sentence. Crop-verify EVERY name/number/low-confidence span. Consult
    authority.json + glossary.json before romanising; ONE rendering per referent
    (Kang Sheng, Zhou Enlai, Chen Geng, Bao Junfu, Li Kenong, the Central Special
    Branch, etc. are decided). Cite PRINTED folios in notes. Never invent bridging
    text; verify the final paragraphs against the scan.
  - Footnotes via apparatus_merge.py (glossary rows carry a "section" field:
    people/organizations/places/events/terms). glossary.json + figures.json.
    HIGH NOTE DENSITY is a standing commissioner directive (STYLE.local.md):
    gloss EVERY named person/place/institution/event/period-term a non-specialist
    might not know, at first appearance, each note saying more than the name.
    grep notes.json + out/ch0[123]_reading.md BEFORE re-noting a recurring subject
    (density TAPERS as recurring figures get their one note). Chapter 3 opens the
    Xi'an Incident and the Yan'an Rectification, and section 3 is Kang Sheng and
    the persecution of comrades — render the partisan/indignant voice faithfully,
    fact-check the contested claims in the notes.
  - verify_unit.py ch03, check_structure.py/check_content.py --config
    data/check_config.json, qc_entities.py (make_bilingual.py ch03 first),
    check_numbers.py --noise data/noise.txt, check_align.py ch03,
    check_apparatus.py, check_register.py --ref out/ch01_reading.md. Build the
    cumulative EPUB, qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/
    epubcheck.jar) 0/0. NOTE: data/zh/*.txt are gitignored (raw book text); on a
    fresh checkout they must be regenerated, or run structural checks with a
    config scoped to the unit you rebuilt (see B03's data/check_config.b3.json).
  - Record everything in PROGRESS.md. Run to completion; do not pause for approval
    mid-batch.

Deliver the EPUB in chat AND paste the next kickoff verbatim in a fenced block.
All work on branch claude/chen-yangshan.
```

## What is DONE (do not redo)

- **Survey session:** full structure in book.json (6 chapters / 29 sections + 3
  appendices + references + afterword + series foreword); metadata; STYLE.md
  composed; skeleton EPUB.
- **B01 = Chapter 1** (ch01, PDF 12-37): 141 paragraphs, 73 footnotes, 41
  glossary rows, 10 figures. Voice-gate approved and FROZEN as the register
  reference. All gates green.
- **B02 = Chapter 2, sections 1-3** (ch02s01-s03, PDF 39-68, printed 28-57):
  169 paragraphs, 106 footnotes, 143 referents, 15 figures. All gates green.
- **B03 = Chapter 2, sections 4-5** (ch02s04-s05, PDF 69-92, printed 58-81):
  142 new body/{v} lines appended to out/ch02_reading.md (ch02 now complete: the
  Red Squad's five assassination cases + the Chongqing "Three Chens" news agency).
  +24 footnotes (ch02 total 130; book-wide 203), +83 glossary rows (226 referents
  total), +5 figures (ch02 total 20). All gates green: parity 142=142, numbers 0,
  content 0 displaced, align OK, entities 0, register within tolerance, apparatus
  0/0, qa_epub PASS, epubcheck 0/0/0.

## Tooling in place (DO NOT REVERT)

- **OCR crop** (measured for this book): `ocr_crop.py --lang chi_sim --psm 6
  --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`, recto/
  verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`. In B03 the crop was run per-page in a loop so each page got
  the parity-correct bottom. ocr_crop.strip_runfoot patched for the verso
  book-title / pipe foot. indents.py/assemble.py UNUSED (data/zh hand-assembled).
- `apparatus_merge.py`: glossary merges into SECTIONS via a `"section"` field on
  each row (default terms).
- `check_content.name_map`: skips `_`-prefixed metadata keys.
- `build_reading_epub.sec_nav`: the EPUB nav omits pending (untranslated)
  sections/subsections rather than linking them to the bare chapter file.
- **data/zh gitignored, regeneration protocol (B03).** `data/zh/*.txt` (raw book
  text) do NOT survive a fresh checkout. When APPENDING to an existing chapter
  file whose earlier sections' zh is gone, scope the parity/number/content/align/
  entity checks to the rebuilt slice: make `data/zh/<unit>s<NN>.txt`, a matching
  slice reading file `out/<unit>s<NN>_reading.md`, and a scoped
  `data/check_config.b3.json` (see B03). Build/qa/epubcheck/register run on the
  WHOLE chapter file; check_apparatus validates anchors against the whole file.
  For a NEW whole chapter (B04 = ch03) this is moot — just map `ch03` in
  data/check_config.json.
- `data/noise.txt`: extended in B03 with 10万, 百步穿杨, 百炼成钢, 三民照相馆,
  万县, 一九三〇, 零乱 (all idiom/name/date/myriad-split, not quantities; the
  "四人/四同志" four-martyr count was carried in English, not noised).
- setup.sh regression test "kickoff_guard template stand-down FAIL" is BENIGN
  (the fixture expects a placeholder HANDOFF; ours is real). Translation checkers
  all pass.

## Renderings settled this batch / carry-forward

- Reused decided forms throughout (Zhou Enlai, Chen Geng, Bao Junfu, Kang Sheng,
  Gu Shunzhang, Liu Ding, Ke Lin, Wang Genying, Yun Daiying, Xu Enzeng, Yang
  Jianhong, Tan Shaoliang, Chen Lifu, Chen Guofu, the Red Squad, the Central
  Special Branch, the Songhu Garrison Command, the Communist University of the
  Toilers of the East, Shen Bao, Whampoa, the May Thirtieth Movement, the April 12
  coup, Sichuan, Shanghai, Wuhan).
- Decided NEW in B03 (feed to authority.json at completion): the Red Terror Squad;
  the martyrs Yan Changyi, Xing Shizhen, Zhang Jichun; He Yihua (郝芝华 Hao Zhihua
  alias); Tan Yubao; Ye Ting; Bai Yunshen; Fan Zhengbo, Fan Zhengluo; Wang
  Rongchuan; Han Yunxiu; Lin Hanchen; Wang Baoyuan; Fan Mengju; Ke Dawen (=Ke Lin
  cover), He Cheng / He Yusheng; the Red Squad men Shao Dafu, Tan Zhongyu, Wang
  Deming, Zhao Yifan, Wu Lanfu, Chen Yongjia, Zuo Guangyu; Wang Songsheng;
  Yuxiang; Chen Chang (贾绍谊 Jia Shaoyi alias) and his wife Liu Qizhen; Chen Kehan;
  Chen Zhongying (=Chen Yangshan cover); Liu Hangchen; Liu Xiang; Kang Ze; Yuan
  Fulu; Wang Shiying; Qiu Jifu; Feng Xuefeng; Tao Jingzhi; Hou Zhenchang; Huang
  Yingqian; Yuan Jiapei; Li Jiemin; Sun Yat-sen. Orgs: the Wude Society, the
  Special-Operations Corps (别动队), the New Sichuan News Agency, the Nanhua News
  Agency, the Renaissance Society, Juntong, Zhongtong, the Chongqing field
  headquarters, the Political Training Department, the Central News Agency, the
  Republican Daily, the Shanghai/Commercial/New Shu Daily, the Dasheng Hospital,
  the Shanghai Provisional Central Bureau. Places: Hai-Lu-Feng, Route Joffre, the
  City God Temple, the Sincere Company, Suiyuan, Wanxian, Yangzhou, Zhabei,
  Pingliang/Hart/Carter/Weihaiwei/Xiaoshadu/Hubei Roads, Xi'an, Pudong. Terms/
  events: ruse of self-injury (苦肉计), the Long March, the National Congress of
  Soviets, the anti-Japanese national-salvation movement.
- Provisional / flagged: Wen Sixiang (温嗣翔, given-name character doubtful in the
  scan); Li Honghun (李鸿混, the 混 doubtful).
- Aliases decided: 德水 Deshui = Dai Bingshi cover; 陈仲英 Chen Zhongying = Chen
  Yangshan cover; 柯达文 Ke Dawen = Ke Lin; 贺雨生 He Yusheng = He Cheng; 贾绍谊 Jia
  Shaoyi = Chen Chang. Chen Yangshan writes 贺家兴 where standard accounts write
  何家兴 (both "He Jiaxing") — footnoted.
- Source errors rendered as printed + footnoted (do NOT "fix"): Peng Pai/Yang Yin
  arrest printed "1928" but fell 24 Aug 1929 (execution 30 Aug 1929); "几千万"
  (tens of millions) killed in the white terror is authorial hyperbole. Keep these
  faithful if they recur; Kang Sheng and the Yan'an persecutions in ch03 will need
  the same interested-witness discipline (render the slant, verdict in the note).

## Voice sheets (consult at every dialogue scene)

- **Chen Yangshan** (subject). Earnest, modest, understated; plain and sincere,
  deflects credit. Render his speech simply. His recollection passages (quoted at
  length in ch02) are plain first-person report, no ornament.
- **Zhou Enlai.** Measured, strategic, courteous; principled directives given
  quietly ("keep close watch... and the moment it is confirmed, execute him in
  secret"). Never bombast.
- **Chen Geng.** Warm, bold, decisive; a soldier's ease and quickness.
- **Bao Junfu.** Worldly, self-serving charm; smooth, slightly performing in
  dialogue, but keeps faith with the Party.
- **Kang Sheng** (comes to the fore in ch03 s3). Cold, sinuous, dangerous; the
  book's villain of the Yan'an chapters. Write him controlled and chilling, not
  cartoonish; keep the author's indignation in the facts, not in adjectives.
- **He Long** (ch01). Blunt, earthy, proud, short concrete declaratives.

## Where the book stands

- Chapter 2 is COMPLETE. Section 4 gave the Red Squad's five signature
  assassinations (He Jiaxing, Dai Bingshi, Chen Weinian, Bai Xin, Huang Dihong),
  each a self-contained case; section 5 followed Chen Yangshan to Chongqing in
  1935-37, where the "Three Chens" (Chen Chang, Chen Yangshan, Chen Kehan) ran the
  New Sichuan News Agency as intelligence cover until the agency was wound up and
  Chen Yangshan was sent to Xi'an in 1936.
- B04 = Chapter 3 opens the Xi'an Incident and the return to Yan'an: the hidden
  front's triumph, the Rectification study, and Chen Yangshan's three questions to
  Kang Sheng amid the persecution of comrades.

## What is NEXT

- B04 = Chapter 3 (ch03), PDF 93-115, printed 82-104. NEW file
  out/ch03_reading.md + data/zh/ch03.txt; add `ch03` to data/check_config.json.

## Open traps / environment state

- Offset printed = pdf - 11 (constant). Front matter runs a SECOND folio
  sequence. Chapter-opener rectos carry a photo above the heading (SKIP it). PDF
  p243 is an Anna's Archive metadata leaf.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process group; pgrep -c tesseract=0.
  ocr_dual.py can exceed a 120s foreground timeout on a full chapter — run it in
  the background or in page-range chunks.
- Reading files are PLAIN ASCII (straight quotes, literal em dash only for real
  interruption); the builder typographizes at render. NO dashed-in appositive
  glosses. Note bodies: numeric character references only (&#8211; &#8212;), never
  named entities; the builder typographizes note-body text too.
- Figure alt: NO straight double quotes (breaks alt="..." -> epubcheck fatal).
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup if the
  container is fresh).
