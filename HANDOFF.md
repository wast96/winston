# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with the block below PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 2 (Chapter 2, sections 1-3) is COMPLETE: translated, annotated, built,
all gates green (qa_epub PASS, epubcheck 0/0/0). The block below is the Batch 3
kickoff, ready to paste.

## Message to paste into the next chat

```
Chen Yangshan B03

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset: printed = pdf - 11
(constant). Chapter 1 is the FROZEN register reference
(check_register.py --ref out/ch01_reading.md). Chapters 1 and 2.1-2.3 are done.

Do Batch 3 = Chapter 2, sections 4-5 (ch02s04-ch02s05), PDF 69-92, printed
58-81, end to end per the CLAUDE.md pipeline:
  - THE UNIT IS THE WHOLE CHAPTER. The builder reads ONE file per chapter,
    out/ch02_reading.md, which already holds sections 1-3. APPEND sections 4-5
    to that SAME file (new "### 4. ..." and "### 5. ..." headings, English
    titles from book.json) and to data/zh/ch02.txt. Do NOT make a new per-section
    file. check_config already maps unit "ch02" to both files; the whole chapter
    is re-checked as one unit (verify_unit.py ch02, etc.).
  - BEFORE translating, read the final two pages of out/ch02_reading.md (the
    section-3 Tianjin ending; the voice IS those pages) and STYLE.local.md.
    Section 4 = 功不可没,"红队"的特殊任务 (the Red Squad's assassinations:
    the killings of 白鑫 Bai Xin, 何家兴 He Jiaxing, the rescue/【顾顺章】 fallout);
    section 5 = 重庆办社,"三陈"相伴战友情 (a Chongqing news agency; the "Three
    Chens").
  - render 69-92; OCR with the SAME crop as ch01/ch02 (do-not-revert list below):
    ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985 --top 0.08
    --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945, VERSO (PDF
    odd) --bottom 0.915. Run ocr_dual.py; verify pgrep -c tesseract is 0.
  - WATCH THE SILENT OCR-LOSS: tesseract drops an isolated paragraph-final SHORT
    line. Any OCR paragraph ending WITHOUT sentence-final punctuation before a
    blank is a dropped-tail suspect; verify against the scan and restore it.
    data/zh is hand-assembled from corrected OCR + scans, one source paragraph
    per line. Keep portrait bio-boxes and photo captions OUT of data/zh (they are
    figure captions, translated into figures.json) so parity stays 1:1.
  - eyeball EVERY page for figures; find_figures.py MISSES vertical/document
    plates and thin line art and mis-detects on dense text - verify each by eye,
    and crop clean images to data/figs/. Photo/portrait captions go in
    figures.json (translated). FIGURE ALT MUST CONTAIN NO STRAIGHT DOUBLE QUOTES
    (they break the alt="..." attribute -> epubcheck fatal); use single quotes.
  - Translate by APPENDING to out/ch02_reading.md, one paragraph per source line.
    Crop-verify EVERY name/number/low-confidence span. Consult authority.json +
    glossary.json before romanising; ONE rendering per referent (many recur:
    Chen Geng, Bao Junfu, Zhou Enlai, Kang Sheng, the Red Squad, etc. are already
    decided). Cite PRINTED folios in notes. Never invent bridging text; verify
    the final paragraphs against the scan.
  - Footnotes via apparatus_merge.py (glossary rows carry a "section" field:
    people/organizations/places/events/terms). glossary.json + figures.json.
    HIGH NOTE DENSITY is a standing commissioner directive (STYLE.local.md):
    gloss EVERY named person/place/institution/event/period-term a non-specialist
    might not know, at first appearance, each note saying more than the name.
    grep notes.json + out/ch02_reading.md BEFORE re-noting a recurring subject.
  - verify_unit.py ch02, check_structure.py/check_content.py --config
    data/check_config.json, qc_entities.py (make_bilingual.py ch02 first),
    check_numbers.py --noise data/noise.txt, check_align.py ch02,
    check_apparatus.py, check_register.py --ref out/ch01_reading.md. Build the
    cumulative EPUB, qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/
    epubcheck.jar) 0/0. NOTE: data/zh/ch01.txt and data/zh/ch02.txt are
    gitignored (raw book text); on a fresh checkout they must be regenerated, or
    run structural checks with a config scoped to the unit you rebuilt.
  - Record everything in PROGRESS.md. Run to completion; do not pause for
    approval mid-batch.

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
  169 paragraphs, 106 footnotes, +102 glossary rows (143 referents total), 15
  figures. All gates green: parity 169=169, numbers 0 unresolved, entities 0,
  content 0 displaced, align OK, apparatus 0/0, register within tolerance,
  qa_epub PASS, epubcheck 0/0/0. Continuous note total now 179.

## Tooling in place (DO NOT REVERT)

- **OCR crop** (measured for this book): `ocr_crop.py --lang chi_sim --psm 6
  --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`, recto/
  verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`. ocr_crop.strip_runfoot patched for the verso book-title /
  pipe foot. indents.py/assemble.py UNUSED (data/zh hand-assembled).
- `apparatus_merge.py`: glossary merges into SECTIONS via a `"section"` field on
  each row (default terms).
- `check_content.name_map`: skips `_`-prefixed metadata keys.
- **`build_reading_epub.sec_nav` (NEW this batch):** the EPUB nav omits pending
  (untranslated) sections/subsections rather than linking them to the bare
  chapter file. Fixes epubcheck NAV-011 (toc out of reading order) and RSC-005
  (span leaf) on a partially-translated chapter. contents.xhtml still shows the
  full pending shape.
- `data/check_config.json`: docs/sources now map ch01 AND ch02 to their reading
  and data/zh files.
- `data/noise.txt`: extended this batch with 四川, 20世纪, `[0-9]0年代`, 十足,
  涕零, 一二八, 九一八, 两家话, 第二天 (all idiom/name/date, not quantities).
- setup.sh regression test "kickoff_guard template stand-down FAIL" is BENIGN
  (the fixture expects a placeholder HANDOFF; ours is real). Translation checkers
  all pass.
- **data/zh/ch01.txt and data/zh/ch02.txt are gitignored** (raw book text). They
  do not survive a fresh checkout; regenerate from source.pdf, or scope
  structural checks to the rebuilt unit.

## Renderings settled this batch / carry-forward

- Reused ch01/authority.json forms: Zhou Enlai, Chen Geng, Bao Junfu, Gu
  Shunzhang, Ren Bishi, Li Weihan, Qu Qiubai, Li Lisan, Chiang Kai-shek, Wang
  Jingwei, the Central Special Branch, the Kuomintang, the May Thirtieth
  Movement, the Nanchang Uprising, Zhang Zuolin, the Northern Expedition,
  Shanghai, Wuhan, Hankou.
- Decided NEW (feed to authority.json at completion): Kang Sheng, Pan Hannian,
  Chen Yun, Li Kenong, Qian Zhuangfei, Hu Di, Li Qiang, Hong Yangsheng, Liu
  Ding, Ke Lin, Chen Shouchang, Liu Bocheng, Su Zhaozheng, Luo Yinong, Peng Pai,
  Deng Zhongxia, Deng Xiaoping, Guan Xiangying, He Jiaxing, Bai Xin, Chen Lifu,
  Chen Guofu, Zhang Daofan, Yang Jianhong, Xu Enzeng, Chen Pengnian, Lian
  Desheng, Qian Dajun, Xiong Shihui, Huang Molan, Yang Yin, Huang Dihong, Yang
  Dezhi, Wang Genying, Hu Egong, Yang Xianzhen, Liu Shaobai, Chen Yuandao, An
  Ziwen, Zhang Kexia, He Jifeng, Zhang Keyun, Shao Fumin, Xu Beihong, An E, Tian
  Han, Zhao Yiman, Li Yimang, Xiong Jinding, Zhu Duansui; the Red Squad, the
  Investigation Section / Central Statistics Bureau (Zhongtong), the Songhu
  Garrison Command, the concession police, the Green Gang, the Three Heroes of
  Longtan, the South China News Agency, the Tongmenghui, the Autumn Harvest
  Uprising, the January 28 / September 18 Incidents, the Campaign to Suppress
  Counterrevolutionaries; Beiping, the Shun-Zhi provincial committee, the
  Hubei-Henan-Anhui soviet area, Route Pichon, Bubbling Well Road.
- Aliases decided: 杨登瀛 Yang Dengying = Bao Junfu (KMT-service name);
  王庸 Wang Yong = Chen Geng; 罗迈 Luo Mai = Li Weihan; 吴南湖 Wu Nanhu = Hu Egong.
- Provisional / flagged: Lampson (兰普逊, Western original uncertain); Yin Jian
  (殷鉴); Wu Hejing (武和景, printed for 武胡景).
- Source errors rendered as printed + footnoted (do NOT "fix"): 李坤泰 wrongly
  attached to Li Yimang; 武和景 for Wu Hujing; Yang Jianhong suicide vs execution;
  Bao's 1951 deposition (1926 + Party membership) beyond the narrative; "国民党
  中央巡捕房". Keep these consistent if they recur.
- Two Chens / naming: many "陈" figures (Chen Geng, Chen Yangshan, Chen Yun, Chen
  Lifu, Chen Guofu, Chen Shouchang, Chen Pengnian, Chen Weinian, Chen Yuandao,
  Chen Zhigao, Chen Qishou). Keep full names on new beats to kill pronoun fog.
- Institutional first person KEPT ("our Party," "we," "the enemy"): deliberate
  partisan-source voice; do not launder to neutral third person.

## Voice sheets (consult at every dialogue scene)

- **Chen Yangshan** (subject). Earnest, modest, understated; plain and sincere,
  deflects credit. Render his speech simply.
- **Zhou Enlai.** Measured, strategic, courteous. Principled directives given
  quietly ("a man like Bao Junfu is not very reliable politically, but... can be
  put entirely to our use"). Never bombast.
- **Chen Geng.** Warm, bold, decisive, humorous. Grips hands, calls Bao "Brother
  Junfu," jokes on the boat about "lucky we brought a doctor." A soldier's ease
  and quickness; the book's most vivid presence after He Long.
- **Bao Junfu.** Worldly, self-serving charm, jocular and theatrical; a survivor
  who nonetheless keeps faith ("up the mountain of knives and down into the
  cauldron of oil"). Keep his smooth, slightly performing register in dialogue.
- **Zhang Daofan.** Vain hypocrite; effusive when grateful ("your prospects are
  boundless"). Let the flattery sound hollow.
- **Deng Xiaoping.** Plain, factual first-person recollection (the 1978 quote).
- **He Long** (ch01). Blunt, earthy, proud, short concrete declaratives.

## Where the book stands

- Chapter 2 opens the hidden-front core. Section 1: the founding of the Central
  Special Branch under Zhou Enlai (Nov 1927), its three (then four) sections, and
  its method of planting agents. Section 2: Chen Yangshan draws the KMT
  investigator Bao Junfu into becoming the Party's first double agent, the whole
  arc through Bao's rise, the rescues of Ren Bishi and Guan Xiangying, Gu
  Shunzhang's 1931 defection, Bao's imprisonment, and his 1950s rehabilitation
  with Chen Yangshan's help. Section 3: Chen Geng and Chen Yangshan's 1931 Tianjin
  mission (rescue, traitor-hunting), ending with Chen Geng transferred to the
  soviet and Chen Yangshan told to stay in Shanghai. Sections 4-5 (B03) cover the
  Red Squad's special missions and a Chongqing news agency.

## What is NEXT

- B03 = Chapter 2, sections 4-5 (ch02s04-ch02s05), PDF 69-92, printed 58-81.
  APPEND to out/ch02_reading.md and data/zh/ch02.txt (unit stays "ch02").

## Open traps / environment state

- Offset printed = pdf - 11 (constant). Front matter runs a SECOND folio
  sequence. Chapter-opener rectos carry a photo above the heading (SKIP it, per
  ch01/ch02). PDF p243 is an Anna's Archive metadata leaf.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process group; pgrep -c tesseract=0.
- Figure alt: NO straight double quotes (breaks alt="..." -> epubcheck fatal).
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup if the
  container is fresh).
