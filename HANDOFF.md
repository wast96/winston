# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with the block below PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 6 (Chapter 4, sections 5–8, ch04s05–s08) is COMPLETE: translated,
annotated, built, all gates green (S5–8 scoped parity 103=103, numbers 0,
entities 0, content aligned, align OK; whole-chapter apparatus 0/0, register
within tolerance; qa_epub PASS, epubcheck 0/0/0). Chapter 4 is now COMPLETE.
The block below is the Batch 7 kickoff, ready to paste.

## Message to paste into the next chat

```
Chen Yangshan B07

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset: printed = pdf - 11
(constant). Chapter 1 is the FROZEN register reference
(check_register.py --ref out/ch01_reading.md). Chapters 1, 2, 3 and 4 are done.

Do Batch 7 = Chapter 5 (ch05, all four sections), PDF 172-204, printed 161-193,
end to end per the CLAUDE.md pipeline:
  - NEW unit ch05 (its own out/ch05_reading.md + data/zh/ch05.txt), four "###"
    section headings with the English titles from book.json:
    1 = 奋发工作，还有许多战斗在后头 (PDF 173; printed 162);
    2 = 战友情深，李克农与陈养山 (PDF 186; printed 175);
    3 = 坚持原则，一身正气跟党走 (PDF 195; printed 184);
    4 = 艰苦朴素，高风亮节当公仆 (PDF 198; printed 187).
    Chapter 5 opens at PDF 172; the chapter-opener recto carries a photo above the
    heading -- SKIP it (per ch01-ch04). CHECK the top of PDF 173 and each section
    opener for lead paragraphs. Chapter 6 opens at PDF 205. 33 pp.: if it runs
    long, it is fine to do it in one batch, but you MAY split at ch05s02/ch05s03
    (note it in the kickoff if you do).
  - ADD ch05 to data/check_config.json AND make a scoped data/check_config.ch05.json
    (copy the ch04 one). data/zh/*.txt are gitignored and gone on a fresh checkout;
    ch01-04 zh will NOT be present -- run the parity/number/content/align/entity
    checks with the ch05-scoped config; build/qa/epubcheck/register run on the whole
    cumulative EPUB; check_apparatus validates anchors against the whole notes.json.
  - BEFORE translating, read the final two pages of out/ch04_reading.md (the Zheng
    Gui / Bureau-of-Confidential-Investigation saga) and STYLE.local.md. Chapter 5
    turns to the post-1949 years: Chen Yangshan's plain, modest first-person voice;
    Li Kenong's warm, precise senior register (voice sheets in HANDOFF).
  - render 172-204; OCR with the SAME crop as ch01-ch04 (do-not-revert list below):
    ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985 --top 0.08
    --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945, VERSO (PDF odd)
    --bottom 0.915, run per-page so the parity-correct bottom applies. The per-page
    loop and ocr_dual exceed a 120s foreground timeout -- run them in the background
    or in page-range chunks; verify pgrep -c tesseract is 0 after.
  - WATCH THE SILENT OCR-LOSS (CONFIRMED every batch, incl. B06 p158): tesseract
    drops an isolated paragraph-final SHORT line, AND a long single-paragraph tail
    can be dropped in the English on a first pass. VERIFY EVERY PAGE BOTTOM and every
    long paragraph's final sentences against the scan and restore them. data/zh is
    hand-assembled from corrected OCR + scans, one source paragraph per line. Keep
    portrait bio-boxes and photo captions OUT of data/zh (they are figure captions,
    into figures.json) so parity stays 1:1. Crop-verify EVERY name/number
    (verify_names.py --auto shows the dual-OCR disagreements; crop systematic mangles
    by eye).
  - eyeball EVERY page for figures; find_figures.py matches photographs but MISSES
    line art/calligraphy (B06: it missed the Mao inscription on p171) and flags the
    chapter-opener photo (SKIP it) - verify each by eye, crop clean images to
    data/figs/ (name p0NNN-f1.png; crop OUT the caption and wraparound body text).
    Photo/portrait captions go in figures.json (translated; who's-who labels are the
    source's, caption prose is yours). FIGURE ALT MUST CONTAIN NO STRAIGHT DOUBLE
    QUOTES (they break alt="..." -> epubcheck fatal); use single/curly quotes.
  - Write English one paragraph per source line, mirror {v}/### /#### markers in
    BOTH data/zh/ch05.txt and out/ch05_reading.md. Use PLAIN ASCII in the reading
    file (straight quotes, literal em dash — ONLY for genuine interruption; the
    builder curls quotes and makes ... an ellipsis at render, but does NOT make em
    dashes from --). NO dashed-in appositive glosses. Consult authority.json +
    glossary.json before romanising; ONE rendering per referent (the whole ch01-04
    cast is decided -- He Long, Chen Yangshan, Li Kenong, Zhou Enlai, Yan Xishan, Fu
    Zuoyi, etc.). PUT THE DECIDED FULL NAME ONCE PER PARAGRAPH the referent appears
    in (check_content is strict; pronouns/short forms carry the rest). Cite PRINTED
    folios in notes. Never invent bridging text; verify the final paragraphs.
  - Footnotes via apparatus_merge.py (glossary rows carry a "section" field). HIGH
    NOTE DENSITY is a standing commissioner directive (STYLE.local.md): gloss every
    named person/place/institution/event/period-term a non-specialist might not
    know, at first appearance, each note saying more than the name. grep notes.json
    + out/ch0[1234]_reading.md BEFORE re-noting a recurring subject (density TAPERS;
    Li Kenong, the Central Investigation Department, the Ministry of Public Security,
    the Special Branch, Zhou Enlai etc. are already noted). Fact-check the claims.
  - verify_unit.py ch05, check_structure.py/check_content.py --config
    data/check_config.ch05.json, make_bilingual.py ch05 then qc_entities.py
    out/ch05_bilingual.md, check_numbers.py out/ch05_bilingual.md --noise
    data/noise.txt, check_align.py ch05, check_apparatus.py, check_register.py
    out/ch05_reading.md --ref out/ch01_reading.md. Build the cumulative EPUB,
    qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) 0/0.
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
- **B03 = Chapter 2, sections 4-5** (ch02s04-s05, PDF 69-92): ch02 complete.
- **B04 = Chapter 3** (ch03, PDF 93-115): 125 paragraphs, 62 footnotes, 5 figures.
- **B05 = Chapter 4, sections 1-4** (ch04s01-s04, PDF 117-146): 142 paragraphs,
  40 footnotes, 91 glossary rows, 5 figures.
- **B06 = Chapter 4, sections 5-8** (ch04s05-s08, PDF 147-171, printed 136-160):
  +103 body paras (S5=9, S6=15, S7=24, S8=55 across 4 "####" subsections), +35
  footnotes (ch04 now 75, book-wide 340), +159 glossary rows (576 referents), +3
  figures (ch04 now 8). Chapter 4 COMPLETE. The rest of the Jin-Sui intelligence
  war: Zhang He stealing ciphers at Guisui; Wang Yanming's Datong network; Lu
  Nan's (Zhao Xihong's) Suiyuan network to its 1950 close; and four "legendary
  tales" (the book-buyer Liu Zhen, the Lanxian couriers, the seizure of the
  Japanese officer Nanqi, and Zheng Gui cracking the Bureau of Confidential
  Investigation's Suiyuan net). All gates green.

## Tooling in place (DO NOT REVERT)

- **OCR crop** (measured for this book): `ocr_crop.py --lang chi_sim --psm 6
  --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`, recto/
  verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`, run per-page in a loop (background it or chunk it; a full
  chapter exceeds a 120s foreground timeout). ocr_crop.strip_runfoot patched for
  the verso book-title / pipe foot. indents.py/assemble.py UNUSED (data/zh is
  hand-assembled from corrected OCR + scans).
- `apparatus_merge.py`: glossary merges into SECTIONS via a `"section"` field on
  each row (default terms). figures.json `file` is a BARE filename (p0NNN-f1.png).
- `check_content.name_map`: skips `_`-prefixed metadata keys.
- `build_reading_epub.sec_nav`: the EPUB nav omits pending (untranslated)
  sections/subsections. Chapter 4 is now fully translated; ch05-ch11 stay pending.
- **data/zh gitignored, regeneration protocol.** `data/zh/*.txt` do NOT survive a
  fresh checkout. Run parity/number/content/align/entity checks with the
  UNIT-SCOPED config; build/qa/epubcheck/register run on the WHOLE cumulative
  EPUB; check_apparatus validates anchors against the whole notes.json. B06 built a
  scoped data/check_config.ch04s58.json to validate the NEW sections independently
  of the frozen S1-4.
- **{v}/### /#### mirroring:** data/zh/<id>.txt and out/<id>_reading.md are
  hand-assembled STRUCTURALLY IDENTICAL line-for-line.
- `data/noise.txt`: B06 added 10 rules (names 李五才/刘万春/马汉三/鄂友三, places
  五寨/五原, phrase 两党, idioms 万籁俱寂/惊恐万状, date 九一九). All carried in
  English prose; none are quantities.
- setup.sh regression "hook stands down on template stub: FAIL" is BENIGN (the
  fixture expects a placeholder HANDOFF; ours is real). All translation checkers pass.

## Renderings settled B06 / carry-forward

- Decided NEW in B06 (feed to authority.json at completion): Zhang He (=Zhang
  Youxin), Li Wucai, Zhang Dazhi, Wu Bingzhou, Jia Tongfu, Wen Yuru, Gong Guohua,
  Jia Zicheng, Hao Ying, Xue Ying, Ji Shukai, Song Wenlin, Wen Jing, Xu Jun, Hou
  Weicheng, Zhang Pinshan, Zhao Liang, Zhou Ziyang, Yuan Maosheng, Yang Zengxiang,
  Lu Jingfu, Liu Wanchun, Ma Fengchen, Wei Gang, Zhao Fang, Zhang Rugang, Fang
  Shaoming (=Wang Yanming), Gao Kelin, Yang Wugong, Li Run, Zou Zonglu, Zou
  Zengqiao, Chu Xichun, Nakahara, Liu Wenzhong, Han Buzhou, Ma Zaiwu, He Dengyuan,
  Xie Yunguang, Peng Ling, Jin Zhaodian, Lu Nan (=Zhao Xihong / Zhao Fumin), Li
  Qiming, He Shaonan, Chen Qihan, Cui Jizhou, Gong Zhen, Zhang Lisheng, Wang
  Zhixiang, Zhang Yongchang, Ji Pinzhi, Ba Rongchang, Ma Zhanshan, Chen Changjie,
  Zhang Jingshi, Li Heting, Jia Gengfu, Lin Ruobing, Ma Hansan (source also Ma
  Hanshan), Ouyang Qin, Zhang Qing'en, Wang Qi, Guo Changqing, Mi Jingquan, Kang
  Shangchi, Chen Ziheng, Liu Guoqing, Hu Quanfu, Zhang Yuqing, Guo Jingbang, Cheng
  Deyan, Li Kunsheng, Cui Zhengchun, Tian Shumei, Hu Shangru, Qu Rixin, Li Jiankui,
  Liu Zhen, Ji Xizi, Zhou Fohai, Chen Gongbo, Li Yuanze, Zhao Guilong, Zhao Ruze,
  Niu Maolin, Cheng Rize, Zhou Gaoming (=Tian Gaoming), Liu Tongshan, Zhang Xinfu,
  Zhao Duan, Li Fang, Nanqi (=Nakamura Rijin), Ding Haoxin, Xing Shengzeng, Niu
  Youmu, Niu Chenglin, Cheng Xi, Li Jisheng, Niu Chengsen, Zhai Wenhua, Zheng Gui,
  Xing Shaowen, He Zhuguo, Li Bao, Jiu Liang, Chai Chuxiang, Li Mo, Pang Zhongxing,
  Yang Bingren, Mao Renfeng, Niu Xiyuan, Wu Yumei, Liu Xiaoji, Liu Zhenhuan, Wang
  Shaohua, Liu Xiaoxian, Zhang Hongbo, Tian Suobu (provisional), Gao Guangyao, Zhai
  Suiping, Huang Donglou, Li Qifeng, Wang Kemo, Zhang Fengxian, Zhu Hongliang, Wei
  Yong'an, Zhang Jie, Yun Long, Yun Hai, Liu Huanbo. Orgs/places/terms: Guisui,
  Sui-Meng, Jining, the Ike Zhao League, the Hetao, Shahukou, Kouquan, the
  Investigation and Statistics office (调统), the Special Conference Secretariat,
  the Resource Investigation Society, the Jin-Sui Intelligence General Bureau, the
  Sui-Meng Public Security Bureau, the Sacrifice League, the National Liberation
  Vanguard, the Cha-Sui Campaign, the Liaoshen Campaign, the Suiyuan peaceful
  uprising.
- Source errors rendered as printed + footnoted (do NOT "fix"): 1912 for 1942
  (printed 136); 马汉山/马汉三 the same man two ways (printed 145); "1945年1月上党战役"
  (Shangdang was Sept-Oct 1945, printed 153); 周高明/田高明 the same courier two ways
  (printed 152); 右平县 (Youping, obscure local name, as printed); 一奉烧鸡铺 (garbled
  classifier, rendered "a roast-chicken shop"); 田唆布 (reading uncertain, provisional).

## Voice sheets (consult at every dialogue scene)

- **Chen Yangshan** (subject). Earnest, modest, understated; plain and sincere,
  deflects credit. First-person report passages are plain, no ornament.
- **Li Kenong** (Chen's intelligence chief; CENTRAL to Chapter 5, section 2).
  Senior, precise, warm to Chen; brief, practical instructions; the intelligence
  chief who trusts his people.
- **He Long** (Chen's chief in the Jin-Sui chapter). Blunt, earthy, proud, short
  concrete declaratives; the work and the man are remarkable, worth any money.
- **Zhou Enlai.** Measured, strategic, courteous; principled directives quietly.
- **Kang Sheng** (ch03 villain). Cold, sinuous, dangerous; controlled, not
  cartoonish. Keep the author's indignation in the facts, not adjectives.
- **Chen Geng** (ch01-02). Warm, bold, decisive; a soldier's ease.
- Minor B06 voices: Zheng Gui (glib, worldly cover-talk, plays the opium trader);
  He Long's admiration; Zhang He's blunt field judgment ("The fellow came to it
  late... his strong point is that he is bold and brave").

## Where the book stands

- Chapters 1-4 COMPLETE. Chapter 4 (the whole Jin-Sui intelligence war under He
  Long, 1945-1950) is done: rebuilding the Bureau, the Gao Shuxun Movement, Wei
  Jian's Taiyuan station, Zhang He's ciphers, the Datong and Lu Nan networks, and
  the legendary tales.
- B07 = Chapter 5 "Anecdotes from Around the Founding of New China": the post-1949
  years, the deep Li Kenong friendship, principle, and frugality.

## What is NEXT

- B07 = Chapter 5 (ch05, PDF 172-204, printed 161-193, four sections). NEW unit
  (own reading file + zh). Add ch05 to both check configs. B08 = Chapter 6; B09 =
  front + back matter; B10 = afterword + whole-book close.

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
  never named entities; <i> is allowed. (Curly quotes/dashes inside note bodies and
  figure captions are fine; only ANCHORS must be verbatim ASCII substrings of the
  reading file.)
- check_content is STRICT: the decided full glossary name must appear once in each
  paragraph the source names the referent (short forms/pronouns fail it).
- A long single paragraph's TAIL, and an isolated short final line at a page
  bottom, can be silently dropped (B05, B06). Verify against the scan.
- Figure alt: NO straight double quotes. figures.json `file` is a BARE filename.
  Crop OUT captions and wraparound text. find_figures MISSES line art/calligraphy.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup if the
  container is fresh).
