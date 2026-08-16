# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with the block below PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 5 (Chapter 4, sections 1–4, ch04s01–s04) is COMPLETE: translated,
annotated, built, all gates green (parity 142=142, numbers 0 unresolved, content
0 displaced, entities 0, align OK, register within tolerance, apparatus 0/0,
qa_epub PASS, epubcheck 0/0/0). The block below is the Batch 6 kickoff, ready to
paste.

## Message to paste into the next chat

```
Chen Yangshan B06

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset: printed = pdf - 11
(constant). Chapter 1 is the FROZEN register reference
(check_register.py --ref out/ch01_reading.md). Chapters 1, 2 and 3 are done, and
Chapter 4 sections 1-4 are done (out/ch04_reading.md + data/zh/ch04.txt already
exist and carry those four sections).

Do Batch 6 = Chapter 4, sections 5-8 (ch04s05-ch04s08), PDF 147-171, printed
136-160, end to end per the CLAUDE.md pipeline:
  - APPEND sections 5-8 to the EXISTING file out/ch04_reading.md (which currently
    ends section 4 with Wei Jian's escape and the deaths of Cui Shou'an and Lü
    Lashuang) and EXTEND the EXISTING data/zh/ch04.txt. Keep the two files
    structurally identical line-for-line (same "###" section headings with the
    English titles from book.json, same {v} markers on the same paragraphs, same
    body-paragraph count/order). The ch04 configs already exist
    (data/check_config.json has ch04; data/check_config.ch04.json is the scoped
    one) -- no config change needed. data/zh/*.txt are gitignored and gone on a
    fresh checkout, so re-run the parity/number/content/align/entity checks with
    the ch04-scoped config; build/qa/epubcheck/register run on the whole
    cumulative EPUB. Sections:
    5 = 沉着果断，潜入敌特内部窃取密电 (PDF 147; printed 136);
    6 = 深入敌后，大同情报工作的开展 (PDF 150; printed 139);
    7 = 敌中有我，机智的鲁南情报组织 (PDF 154; printed 143);
    8 = 历史一页，晋绥情报传奇故事 (PDF 160; printed 149).
    Section 8 runs to printed 160 (PDF 171); Chapter 5 opens at PDF 172. CHECK the
    tops of PDF 147 and each section opener for any lead paragraphs; render 147-171.
  - BEFORE translating, read the final two pages of out/ch04_reading.md (the end
    of the Wei Jian saga -- Chen Yangshan's plain, sincere voice and He Long's
    blunt earthy voice are the register for this chapter) and STYLE.local.md.
  - render 147-171; OCR with the SAME crop as ch01-ch04 (do-not-revert list
    below): ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985 --top
    0.08 --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945, VERSO
    (PDF odd) --bottom 0.915, run per-page so the parity-correct bottom applies.
    The per-page loop can exceed a 120s foreground timeout -- run ocr_crop and
    ocr_dual in the background or in page-range chunks; verify pgrep -c tesseract
    is 0 after.
  - WATCH THE SILENT OCR-LOSS (CONFIRMED every batch): tesseract drops an isolated
    paragraph-final SHORT line, AND a long single-paragraph tail can be dropped in
    the English on a first pass (B05 lost the chase/water-pit tail of one long
    paragraph until check_numbers' idiom flag surfaced it). VERIFY EVERY PAGE
    BOTTOM and every long paragraph's final sentences against the scan and restore
    them. data/zh is hand-assembled from corrected OCR + scans, one source
    paragraph per line. Keep portrait bio-boxes and photo captions OUT of data/zh
    (they are figure captions, translated into figures.json) so parity stays 1:1.
    Crop-verify EVERY name/number (verify_names.py --auto shows only the dual-OCR
    disagreements; crop the systematic mangles by eye).
  - eyeball EVERY page for figures; find_figures.py has matched the real plates
    every batch but MISSES line art and mis-detects on dense text (and flags the
    chapter-opener photos, which we SKIP) - verify each by eye, and crop clean
    images to data/figs/ (name p0NNN-f1.png; crop OUT the caption and any
    wraparound body text; find_figures boxes often include margin text). Photo/
    portrait captions go in figures.json (translated; who's-who labels are the
    source's, caption prose is yours). FIGURE ALT MUST CONTAIN NO STRAIGHT DOUBLE
    QUOTES (they break the alt="..." attribute -> epubcheck fatal); use single
    quotes.
  - Write English one paragraph per source line, and MIRROR the {v} markers and
    section "###" lines in BOTH data/zh/ch04.txt and out/ch04_reading.md so every
    positional check lines up. Use PLAIN ASCII in the reading file: straight quotes
    " ', literal em dash — ONLY for genuine interruption (the builder curls quotes
    and turns ... into an ellipsis at render; it does NOT make em dashes from --).
    NO dashed-in appositive glosses: a fact set off in a dash-pair belongs in
    parens, a comma clause, or its own sentence. Consult authority.json +
    glossary.json before romanising; ONE rendering per referent (the whole ch01-04
    cast is now in glossary.json -- He Long, Chen Yangshan, Li Kenong, Yan Xishan,
    Fu Zuoyi, Wei Jian, the Bureau of Confidential Investigation, etc. are decided).
    PUT THE DECIDED FULL NAME ONCE PER PARAGRAPH the referent appears in
    (check_content is strict; pronouns/short forms carry the rest).
    Cite PRINTED folios in notes. Never invent bridging text; verify the final
    paragraphs against the scan.
  - Footnotes via apparatus_merge.py (glossary rows carry a "section" field:
    people/organizations/places/events/terms). glossary.json + figures.json.
    HIGH NOTE DENSITY is a standing commissioner directive (STYLE.local.md):
    gloss EVERY named person/place/institution/event/period-term a non-specialist
    might not know, at first appearance, each note saying more than the name.
    grep notes.json + out/ch0[1234]_reading.md BEFORE re-noting a recurring subject
    (density TAPERS; Datong, the Bureau of Confidential Investigation, the
    Comradeship Association, Kenanpo etc. are already noted). Sections 5-8 continue
    the Jin-Sui intelligence war (Datong network, southern-Shandong network,
    legendary tales); fact-check the operational claims in the notes.
  - verify_unit.py ch04 (numbers via bilingual), check_structure.py/check_content.py
    --config data/check_config.ch04.json, make_bilingual.py ch04 then
    qc_entities.py out/ch04_bilingual.md, check_numbers.py out/ch04_bilingual.md
    --noise data/noise.txt, check_align.py ch04, check_apparatus.py,
    check_register.py out/ch04_reading.md --ref out/ch01_reading.md. Build the
    cumulative EPUB, qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar)
    0/0.
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
  reference.
- **B02 = Chapter 2, sections 1-3** (ch02s01-s03, PDF 39-68): 169 paragraphs,
  106 footnotes, 143 referents, 15 figures.
- **B03 = Chapter 2, sections 4-5** (ch02s04-s05, PDF 69-92): +142 lines (ch02
  complete). +24 footnotes; +83 glossary rows; +5 figures.
- **B04 = Chapter 3** (ch03, PDF 93-115): 125 paragraphs, 62 footnotes, +100
  glossary rows, 5 figures.
- **B05 = Chapter 4, sections 1-4** (ch04s01-s04, PDF 117-146, printed 106-135):
  142 paragraphs (S1=28, S2=34, S3=33, S4=47), +40 footnotes (book-wide 305),
  +91 glossary rows (417 referents), 5 figures. Chen Yangshan's Jin-Sui
  intelligence war under He Long: rebuilding the Investigation Bureau, the Gao
  Shuxun Movement, and Wei Jian's underground station inside Yan Xishan's Taiyuan
  (the top-secret letter and the Xieyiheng dim-sum-shop tragedy). All gates green.

## Tooling in place (DO NOT REVERT)

- **OCR crop** (measured for this book): `ocr_crop.py --lang chi_sim --psm 6
  --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`, recto/
  verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`, run per-page in a loop (background it or chunk it; a full
  chapter exceeds a 120s foreground timeout). ocr_crop.strip_runfoot patched for
  the verso book-title / pipe foot. indents.py/assemble.py UNUSED (data/zh is
  hand-assembled from corrected OCR + scans).
- `apparatus_merge.py`: glossary merges into SECTIONS via a `"section"` field on
  each row (default terms). figures.json `file` is a BARE filename (p0NNN-f1.png),
  NOT a path — the builder prepends data/figs/.
- `check_content.name_map`: skips `_`-prefixed metadata keys.
- `build_reading_epub.sec_nav`: the EPUB nav omits pending (untranslated)
  sections/subsections. ch04 sections 5-8 stay pending until B06.
- **data/zh gitignored, regeneration protocol.** `data/zh/*.txt` do NOT survive a
  fresh checkout. Run parity/number/content/align/entity checks with the
  UNIT-SCOPED config (data/check_config.ch04.json maps ONLY ch04); build/qa/
  epubcheck/register run on the WHOLE cumulative EPUB; check_apparatus validates
  anchors against the whole notes.json.
- **{v}/### mirroring:** data/zh/ch04.txt and out/ch04_reading.md are hand-
  assembled STRUCTURALLY IDENTICAL line-for-line. B06 APPENDS to both.
- `data/noise.txt`: extended in B05 with 百灵庙 (place), 野板参三 (name), 窘态百出
  and 五花大绑 (idioms), 40万 (arabic+万 magnitude split). All carried in English
  prose; none are quantities.
- setup.sh regression test "hook stands down on template stub: FAIL" is BENIGN
  (the fixture expects a placeholder HANDOFF; ours is real). All translation
  checkers pass.

## Renderings settled B05 / carry-forward

- Decided NEW in B05 (feed to authority.json at completion): Luo Qingchang, Yan
  Xishan, Fu Zuoyi, Tan Zhengwen, Li Jingquan, Feng Jiping, Feng Jinchen, Liang
  Hanbing, Zhou Quan, Cui Yaonan, Zhang Shoude, Ma Mingfang, Li Fushan, Pei Zhouyu,
  Zhou Yi, Zou Dapeng, Nie Yuansu, Wang Shukai, Zhao Jin'ao, Zhao Jingdi, E Yousan,
  Ma Hongkui, Dong Qiwu, Liang Shengyuan, Wu Leiyuan, Fu Juemin, Cheng Dedi, Zhao
  Siwu, Gao Shuxun, Pan Shuoduan, Liu Shanben, Fan Yangbin, Wei Shunshi, Marshall,
  Zhang Zhizhong, Chen Cheng, Wei Jian, Cao Yanxing, Wu Peishen, Zhang Lixian, Kang
  Li, An Zifeng, Han Bin, Liang Yanwu, Yan Huiqing, Wang Jingguo, Liang Huazhi, Meng
  Jifeng, Bo Yuxiang, Lu Xueming, Wang Zhishi, Yang Aiyuan, Wu Zhezhi, Chai Zemin,
  Hao Binnan, Zhou Peiji, Zhou Peiyao, An Baozhi, Li Wenfang (=Zhang Xinfu), Cui
  Shou'an (=Wang Lianzhong), Zhou Jianmin, Zhu Chonglian, Zhang Ruoling, Xu Duan,
  Yang Zhenji, Liang Jiqing, Yan Handong, Wang Yudi, Liu Huamin, Ma Chen, Xue Bomin,
  He Jiong, Tian Shulan, Ren Zhiqing, Yan Qi'e, Lü Lashuang, Wang Qian, Zheng
  Xiaoxian, Wang Guohua, Zhang Peizhen. Orgs/places/events: the Jin-Sui Border
  Region / Military Region / Sub-bureau, the Comradeship Association, the National
  Revolution News Agency, the Bureau of Confidential Investigation, the Fuxing
  Daily, the Jiefang Daily, Kenanpo, the Gao Shuxun / Shangdang / Qingfengdian
  campaigns.
- Source errors rendered as printed + footnoted (do NOT "fix"): 罗长青 for 罗青长
  (Luo Qingchang) at printed 106; the April-13 speech dated 1948 (printed 109) AND
  1947 (printed 116); 平律 for 平津 (Beiping-Tianjin) at printed 115; 野板参三 for
  野坂参三 (Nosaka); 没谓 for 莫谓 in the Wang Shukai couplet; 魏×/李×× (given names
  redacted by the source); 和清县 / 二配区 (obscure local names, as printed).

## Voice sheets (consult at every dialogue scene)

- **Chen Yangshan** (subject). Earnest, modest, understated; plain and sincere,
  deflects credit. His letter and recollection passages are plain first-person
  report, no ornament (see ch03's 1979/1988 letters and ch04's Nov-20 letter).
- **He Long** (Chen's chief in the Jin-Sui chapter). Blunt, earthy, proud, short
  concrete declaratives. His register: the work is remarkable, this man Chen
  Yangshan is remarkable, worth any money spent.
- **Zhou Enlai.** Measured, strategic, courteous; principled directives quietly.
- **Li Kenong.** Senior, precise, warm to Chen; the intelligence chief's brief,
  practical instructions.
- **Kang Sheng** (ch03 villain). Cold, sinuous, dangerous; controlled, not
  cartoonish. Keep the author's indignation in the facts, not adjectives.
- **Chen Geng** (ch01-02). Warm, bold, decisive; a soldier's ease.
- **Bao Junfu** (ch02). Worldly, self-serving charm; keeps faith with the Party.

## Where the book stands

- Chapters 1-3 COMPLETE. Chapter 4 sections 1-4 COMPLETE (the Jin-Sui intelligence
  war under He Long, through the fall of Wei Jian's Taiyuan station in late 1946).
- B06 = Chapter 4, sections 5-8: the rest of the Jin-Sui intelligence saga
  (stealing enemy ciphers, the Datong network, the southern-Shandong network, and
  "legendary tales" of Jin-Sui intelligence).

## What is NEXT

- B06 = Chapter 4, sections 5-8 (ch04s05-ch04s08), PDF 147-171, printed 136-160.
  APPEND to the EXISTING out/ch04_reading.md + data/zh/ch04.txt (do NOT start a new
  file). ch04 is already mapped in both check configs. B07 = Chapter 5.

## Open traps / environment state

- Offset printed = pdf - 11 (constant). Front matter runs a SECOND folio sequence.
  Chapter-opener rectos carry a photo above the heading (SKIP it). PDF p243 is an
  Anna's Archive metadata leaf.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract=0.
  The per-page ocr loop and ocr_dual.py exceed a 120s foreground timeout on a full
  chapter -- background them or chunk the range.
- Reading files are PLAIN ASCII (straight quotes, literal em dash only for real
  interruption); the builder typographizes at render. NO dashed-in appositive
  glosses. Note bodies: numeric character references only (&#8211; &#8212; &#160;),
  never named entities; <i> is allowed.
- check_content is STRICT: the decided full glossary name must appear once in each
  paragraph the source names the referent (short forms/pronouns fail it).
- A long single paragraph's TAIL can be silently dropped in the English on a first
  pass (B05). Verify every long paragraph's final sentences against the scan.
- Figure alt: NO straight double quotes (breaks alt="..." -> epubcheck fatal).
  figures.json `file` is a BARE filename. Crop OUT captions and wraparound text.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup if the
  container is fresh).
