# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with the block below PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 4 (Chapter 3, ch03) is COMPLETE: translated, annotated, built, all gates
green (parity 125=125, numbers 0 unresolved, content 0 displaced, entities 0,
register within tolerance, qa_epub PASS, epubcheck 0/0/0). The block below is
the Batch 5 kickoff, ready to paste.

## Message to paste into the next chat

```
Chen Yangshan B05

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset: printed = pdf - 11
(constant). Chapter 1 is the FROZEN register reference
(check_register.py --ref out/ch01_reading.md). Chapters 1, 2 and 3 are done.

Do Batch 5 = Chapter 4, sections 1-4 (ch04s01-ch04s04), PDF 117-146, printed
106-135, end to end per the CLAUDE.md pipeline:
  - THE UNIT IS THE CHAPTER FILE = a NEW file out/ch04_reading.md carrying
    sections 1-4 only (four "### 1./2./3./4." section headings, English titles
    from book.json) and a new data/zh/ch04.txt. Batch 6 will APPEND sections 5-8
    to the same file. Add "ch04" to data/check_config.json (docs + sources) AND
    make a ch04-scoped config (copy data/check_config.ch03.json -> ch04) for the
    structural checks, since data/zh/*.txt are gitignored and ch01-ch03 zh will
    be gone on a fresh checkout. Sections:
    1 = 情报纪事，陈养山晋绥经历 (PDF 117; printed 106);
    2 = 再创佳绩，贺龙麾下立新功 (PDF 122; printed 111);
    3 = 依势利导，全力搜集战略情报 (PDF 130; printed 119);
    4 = 剑胆琴心，陈养山一封绝密信 (PDF 137; printed 126).
    RENDER 116-146: the chapter opener is recto PDF 116 (printed 105), title
    "第四章 在晋绥边区的奋战" with a photo above the heading -- SKIP the photo (per
    ch01/ch02/ch03). CHECK PDF 116 for any chapter-intro paragraphs before
    section 1 (ch02 had three such intro paragraphs above out/ch02_reading.md's
    first "###"; ch03 had none). If present they go at the TOP of the file,
    before "### 1.".
  - BEFORE translating, read the final two pages of out/ch03_reading.md (Chen
    Yangshan's 1988 letter to the Central Organization Department, closing the
    Kang Sheng section; the voice IS those pages) and STYLE.local.md.
  - render 116-146; OCR with the SAME crop as ch01/ch02/ch03 (do-not-revert list
    below): ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985 --top
    0.08 --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945, VERSO
    (PDF odd) --bottom 0.915, run per-page so the parity-correct bottom applies.
    Run ocr_dual.py; verify pgrep -c tesseract is 0.
  - WATCH THE SILENT OCR-LOSS (CONFIRMED every batch, incl. B04's mid-page
    "尖锐起来。"): tesseract drops an isolated paragraph-final SHORT line. Any OCR
    paragraph ending WITHOUT sentence-final punctuation before a blank is a
    dropped-tail suspect; VERIFY EVERY PAGE BOTTOM (and short mid-page final
    lines) against the scan and restore it. data/zh is hand-assembled from
    corrected OCR + scans, one source paragraph per line. Keep portrait bio-boxes
    and photo captions OUT of data/zh (they are figure captions, translated into
    figures.json) so parity stays 1:1. Crop-verify EVERY name/number.
  - eyeball EVERY page for figures; find_figures.py has matched the real plates
    every batch but MISSES line art and mis-detects on dense text - verify each by
    eye, and crop clean images to data/figs/ (name p0NNN-f1.png; crop OUT the
    caption and any wraparound body text). Photo/portrait captions go in
    figures.json (translated). FIGURE ALT MUST CONTAIN NO STRAIGHT DOUBLE QUOTES
    (they break the alt="..." attribute -> epubcheck fatal); use single quotes.
  - Write English one paragraph per source line, and MIRROR the {v} markers and
    section "###" lines in BOTH data/zh/ch04.txt and out/ch04_reading.md so every
    positional check (parity, content, align, entities) lines up. Use PLAIN ASCII
    in the reading file: straight quotes " ', literal em dash — ONLY for genuine
    interruption (the builder curls quotes and turns ... into an ellipsis at
    render; it does NOT make em dashes from --). NO dashed-in appositive glosses:
    a fact set off in a dash-pair belongs in parens, a comma clause, or its own
    sentence. Consult authority.json + glossary.json before romanising; ONE
    rendering per referent (He Long, Chen Yangshan, Zhang Suzhen, Li Kenong, Kang
    Sheng, the Central Special Branch, etc. are decided; the whole ch03 cast is now
    in glossary.json). PUT THE DECIDED FULL NAME ONCE PER PARAGRAPH the referent
    appears in (check_content is strict; pronouns/short forms carry the rest).
    Cite PRINTED folios in notes. Never invent bridging text; verify the final
    paragraphs against the scan.
  - Footnotes via apparatus_merge.py (glossary rows carry a "section" field:
    people/organizations/places/events/terms). glossary.json + figures.json.
    HIGH NOTE DENSITY is a standing commissioner directive (STYLE.local.md):
    gloss EVERY named person/place/institution/event/period-term a non-specialist
    might not know, at first appearance, each note saying more than the name.
    grep notes.json + out/ch0[123]_reading.md BEFORE re-noting a recurring subject
    (He Long, Li Kenong, the Special Branch, Kang Sheng, Juntong/Zhongtong etc.
    are already noted; density TAPERS). Chapter 4 is Chen Yangshan's Jin-Sui
    intelligence war under He Long -- render He Long's blunt, earthy voice (voice
    sheet below) and fact-check the operational claims in the notes.
  - verify_unit.py ch04, check_structure.py/check_content.py --config
    data/check_config.ch04.json, qc_entities.py out/ch04_bilingual.md
    (make_bilingual.py ch04 first), check_numbers.py --noise data/noise.txt (via
    verify_unit), check_align.py ch04, check_apparatus.py, check_register.py --ref
    out/ch01_reading.md. Build the cumulative EPUB, qa_epub.py green, epubcheck
    (/tmp/epubcheck-5.1.0/epubcheck.jar) 0/0.
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
  142 lines appended (ch02 complete). +24 footnotes; +83 glossary rows; +5
  figures. All gates green.
- **B04 = Chapter 3** (ch03, PDF 93-115, printed 82-104): 125 paragraphs (S1=40,
  S2=40, S3=45), 62 footnotes (book-wide 265), +100 glossary rows (326 referents),
  5 figures. The Xi'an Incident on the hidden front, the return to Yan'an and the
  Rectification, and the three questions to Kang Sheng over the comrades killed in
  the Soviet purge. All gates green: parity 125=125, numbers 0, content 0
  displaced, align OK, entities 0, register within tolerance, apparatus 0/0,
  qa_epub PASS, epubcheck 0/0/0.

## Tooling in place (DO NOT REVERT)

- **OCR crop** (measured for this book): `ocr_crop.py --lang chi_sim --psm 6
  --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`, recto/
  verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`, run per-page in a loop. ocr_crop.strip_runfoot patched for the
  verso book-title / pipe foot. indents.py/assemble.py UNUSED (data/zh is
  hand-assembled from corrected OCR + scans).
- `apparatus_merge.py`: glossary merges into SECTIONS via a `"section"` field on
  each row (default terms).
- `check_content.name_map`: skips `_`-prefixed metadata keys.
- `build_reading_epub.sec_nav`: the EPUB nav omits pending (untranslated)
  sections/subsections rather than linking them to the bare chapter file. (So a
  partial chapter -- ch04 sections 1-4 -- builds clean; sections 5-8 stay pending.)
- **data/zh gitignored, regeneration protocol.** `data/zh/*.txt` (raw book text)
  do NOT survive a fresh checkout. Run the parity/number/content/align/entity
  checks with a UNIT-SCOPED config (e.g. data/check_config.ch03.json for B04;
  make data/check_config.ch04.json for B05) that maps ONLY the unit you rebuilt.
  Build/qa/epubcheck/register run on the WHOLE cumulative EPUB; check_apparatus
  validates anchors against the whole notes.json.
- **{v}/### mirroring:** data/zh/<unit>.txt and out/<unit>_reading.md are
  hand-assembled to be STRUCTURALLY IDENTICAL line-for-line (same "###" headings,
  same `{v}` markers on the same paragraphs, same body-paragraph count/order), so
  every positional check aligns trivially. Quoted letters/recollections/documents
  use `{v}`; a plain paragraph between two `{v}` runs (e.g. "Appended:") separates
  distinct documents.
- `data/noise.txt`: extended in B04 with 一〇七, 七尺, 七贤庄, 一打二拉, 立三路线,
  120万, 100万, 1亿 (unit-designation numeral, idioms, place/line names, and
  arabic+万/亿 magnitude splits -- all carried in English prose, none are
  quantities). 李立三 was already present. The 四人 count was carried in English,
  not noised.
- setup.sh regression test "kickoff_guard template stand-down FAIL" is BENIGN
  (the fixture expects a placeholder HANDOFF; ours is real). Translation checkers
  all pass.

## Renderings settled B04 / carry-forward

- Decided NEW in B04 (feed to authority.json at completion): Zhang Xueliang, Yang
  Hucheng, Song Qiyun, Gao Fuyuan, Wang Yizhe, Peng Dehuai, Wang Feng, Wang
  Shiying, Nan Hanchen, Du Binchen, Zhao Shoushan, Kong Congzhou, Shen Bochun,
  Feng Qinzai, Yan Kuiyao, Wu Xiru, Ding Ling, Xu Pingyu, Chen Bo (Bulu), Li
  Yimang, Hu Zongnan, Wu Defeng, Qi Yuande, Tao Shiyong, Sai Xianfo (provisional),
  Cheng Ziping, Yu Zhongyou, Xiao Fuxian, Chen Mingjun (Chen Yangshan cover),
  Xuan Xiafu, Xu Binru, Jiang Ziming, Li Furen, Gao Chongmin, Yang Mingxuan, Han
  Zhuoru, Che Xiangchen, Xu Zhongquan, Qiu Jin (cadre, not the 1907 martyr), Deng
  Yingchao, Zhenyu (Chen Zhenyu), Song Shilun, Wang Heshou, Xiang Zhonghua, Lei
  Renmin, Fu Yutian, Jia Zheng, Gao Langshan, Bai Xiangyin, Li Guohua, Wang
  Shiwei, Fan Shiren, Lin Yixin, Mo Wenhua, Zeng Zhi, Kang Keqing, Jiang Qing,
  Ye Qun, Peng Zhen, Ren Bishi, Zhu De, Liu Shaoqi, Lin Boqu, Okano Susumu
  (=Nosaka Sanzo), Chen Yun, Guan Fushan, Chen Jianyu, Chen Guobao, Yuan Renyuan,
  Wang Ming, Xiao Shouhuang, Ouyang Xin, He Changzhi, Wu Hujing (=Wu Huairang),
  Hou Zhi, Su Mei, Lin Biao, Kirov. Orgs: the Northeastern/Northwestern/Seventeenth
  Route Army, the Anti-Japanese Comrades' Association, the Cultural Weekly, the Red
  China News Agency, Xinhua, the Central Social Affairs Department, the Central
  Party School, the Three People's Principles Youth Corps, the Comintern, the
  Jin-Sui Military Region, the Central Intelligence Department, the Ministry of
  State Security. Places: the Huaqing Pool, Lintong, Luochuan, Wayaobao, the
  Shaan-Gan-Ning Border Region, Zaoyuan, Baoji, Qixianzhuang. Events: the Xi'an
  Incident, the Lugou Bridge Incident, the Rectification Movement, the Great
  Cultural Revolution, the August First Declaration.
- Provisional / flagged: Sai Xianfo (塞先佛, uncommon surname, crop-verified 塞).
- Source errors rendered as printed + footnoted (do NOT "fix"): the Seventh
  Congress dated 1943 (was 1945; noted via Mao's own "24-year course" + the 1.2M
  figure); 宗绮云/宋绮云 (Song Qiyun, one referent, variant noted); the Maoling
  caption's 汉开帝墓 (Emperor Wu of Han's tomb, rendered correctly in the caption);
  the letter's 大浦 for 大埔 (Dabu), noted.

## Voice sheets (consult at every dialogue scene)

- **Chen Yangshan** (subject). Earnest, modest, understated; plain and sincere,
  deflects credit. His recollection/letter passages are plain first-person report,
  no ornament (see ch03's 1979/1988 letters).
- **Zhou Enlai.** Measured, strategic, courteous; principled directives given
  quietly. Never bombast.
- **He Long** (returns as Chen's chief in ch04 Jin-Sui). Blunt, earthy, proud,
  short concrete declaratives. His ch01 line -- the work is remarkable, this man
  Chen Yangshan is remarkable, worth any money spent -- is the register.
- **Kang Sheng** (ch03 villain). Cold, sinuous, dangerous; controlled and
  chilling, not cartoonish ("I say you have problems in your history, so you have
  problems in your history"). Keep the author's indignation in the facts, not in
  adjectives.
- **Chen Geng** (ch01-02). Warm, bold, decisive; a soldier's ease.
- **Bao Junfu** (ch02). Worldly, self-serving charm; keeps faith with the Party.

## Where the book stands

- Chapters 1-3 COMPLETE. Ch03 closed the Yan'an chapter: Chen Yangshan back from
  the enemy areas, through the Rectification, and pressing Kang Sheng three times
  over the comrades killed in the USSR; the chapter ends on his 1979 and 1988
  letters demanding the murdered cadres' rehabilitation. At the end of 1944 (last
  line of ch03) He Long has Chen sent to head the Jin-Sui Military Region's
  investigation bureau -- which is exactly where Chapter 4 opens.
- B05 = Chapter 4, sections 1-4 (ch04s01-s04): Chen Yangshan's intelligence war in
  the Jin-Sui border region under He Long.

## What is NEXT

- B05 = Chapter 4, sections 1-4 (ch04s01-ch04s04), PDF 117-146 (render 116-146 for
  the opener), printed 106-135. NEW file out/ch04_reading.md (sections 1-4) +
  data/zh/ch04.txt; add `ch04` to data/check_config.json + a scoped
  data/check_config.ch04.json. B06 appends sections 5-8.

## Open traps / environment state

- Offset printed = pdf - 11 (constant). Front matter runs a SECOND folio
  sequence. Chapter-opener rectos carry a photo above the heading (SKIP it). PDF
  p243 is an Anna's Archive metadata leaf.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process group; pgrep -c tesseract=0.
  ocr_dual.py can exceed a 120s foreground timeout on a full chapter -- run it in
  the background or in page-range chunks.
- Reading files are PLAIN ASCII (straight quotes, literal em dash only for real
  interruption); the builder typographizes at render. NO dashed-in appositive
  glosses. Note bodies: numeric character references only (&#8211; &#8212;), never
  named entities; the builder typographizes note-body text too. <i> is allowed in
  note bodies.
- check_content is STRICT: the decided full glossary name must appear once in each
  paragraph the source names the referent (short forms/pronouns fail it). Put the
  full name once per paragraph, pronouns after.
- Figure alt: NO straight double quotes (breaks alt="..." -> epubcheck fatal).
  Crop OUT captions and wraparound body text from figure images.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup if the
  container is fresh).
