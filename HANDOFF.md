# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with the block below PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 8 (Chapter 6, ch06, PDF 205–224, printed 194–213) is COMPLETE: translated,
annotated, built, all gates green (parity 67=67, apparatus 0/0, content aligned,
entities 0, numbers 0, align OK, register within tolerance; qa_epub PASS, epubcheck
0/0/0). Chapters 1–6 — the whole body of the book — are now COMPLETE. The block
below is the Batch 9 kickoff (front + back matter translation), ready to paste.

## Message to paste into the next chat

```
Chen Yangshan B09

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset for the BODY: printed = pdf
- 11 (constant). The FRONT MATTER runs its OWN folio sequence (blurb printed 6;
series foreword printed 1-2 on front folios). Chapter 1 is the FROZEN register
reference (check_register.py --ref out/ch01_reading.md). Chapters 1-6 are done.

Do Batch 9 = FRONT + BACK MATTER (translation), end to end per the CLAUDE.md
pipeline. FIVE new units:
  - ch00 = 丛书前言 "Foreword to the Series" (Zhang Baijia), PDF 7-8 (front folios
    1-2). A signed editorial foreword to the whole "Hidden Front Chronicles" series.
  - ch07 = 附录一 陈养山生平 "Appendix I. Chen Yangshan: A Life", PDF 225-227
    (printed 214-216). A prose life-summary.
  - ch08 = 附录二 陈养山遗作 "Appendix II. Chen Yangshan's Posthumous Writings",
    PDF 228-233 (printed 217-222). One or more essays BY Chen (first person);
    set-off document(s) -- decide {v} vs running prose from the layout, and mind
    Chen's own plain voice (voice sheet below).
  - ch09 = 附录三 陈养山年谱 "Appendix III. A Chronology of Chen Yangshan's Life",
    PDF 234-238 (printed 223-227). A year-by-year 年谱: one dated entry per source
    line; keep every date/number (crop-verify), render years/months in English
    convention. This is a numbers-dense unit -- run check_numbers hard.
  - ch10 = 参考文献 "References", PDF 239-240 (printed 228-229). A bibliography:
    one citation per line. Leave author/title romanization per the ledger; give an
    English gloss of each title in brackets or a note as fits the reading model.
    Do NOT invent bibliographic detail; render what is printed.
  (ch11 = 后记 Afterword and the whole-book close are B10, the LIGHT final batch.)
  - For EACH unit make its own out/<id>_reading.md + data/zh/<id>.txt and ADD it to
    data/check_config.json AND a scoped data/check_config.<id>.json (copy an existing
    one). data/zh/*.txt are gitignored and gone on a fresh checkout; ch01-06 zh will
    NOT be present -- run parity/number/content/align/entity with the unit-scoped
    configs; build/qa/epubcheck/register run on the whole cumulative EPUB;
    check_apparatus validates anchors against the whole notes.json.
  - render 7-8 and 225-240; OCR with the SAME crop as ch01-ch06 (do-not-revert list
    below): ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985 --top 0.08
    --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945, VERSO (PDF odd)
    --bottom 0.915, per-page. The FRONT-MATTER pages (7-8) have DIFFERENT running
    heads/furniture -- check the crop by OCR and adjust top/bottom for those two
    pages only if the folio or a series-title band intrudes. Background the loops;
    verify pgrep -c tesseract is 0 after.
  - WATCH THE SILENT OCR-LOSS (CONFIRMED every batch): tesseract drops an isolated
    paragraph-final SHORT line, AND a long single-paragraph tail can be dropped in
    the English on a first pass. VERIFY EVERY PAGE BOTTOM and every long paragraph's
    final sentences against the scan. In the 年谱 and References especially, verify
    the LAST entry on every page. Keep portrait bio-boxes and photo captions OUT of
    data/zh (into figures.json) so parity stays 1:1.
  - eyeball EVERY page for figures (photos, and the frontispiece portrait at PDF p5
    if you choose to place it -- optional); find_figures MISSES line art/calligraphy.
    Crop clean images to data/figs/ (name p0NNN-f1.png; crop OUT caption + bio-box +
    wraparound text). Photo captions go in figures.json (translated). FIGURE ALT MUST
    CONTAIN NO STRAIGHT DOUBLE QUOTES. A figure `before` anchor must be a substring
    of the FIRST ~80 chars of its paragraph.
  - Write English one paragraph per source line, mirror {v}/{p}/### /#### markers in
    BOTH data/zh and out/*_reading.md. Set-off documents (essays, letters, the
    chronology's dated lines if laid out as a table/list) as {v} where the layout is
    set off; a plain prose appendix stays running prose. Use PLAIN ASCII (straight
    quotes; literal em dash ONLY for real interruption/aside; NO dashed appositive
    glosses). Consult authority.json + glossary.json before romanising; ONE rendering
    per referent (the whole ch01-06 cast is decided). PUT THE DECIDED FULL NAME ONCE
    PER PARAGRAPH the referent appears in. Cite PRINTED folios in notes. Never invent
    bridging text; verify the final paragraphs.
  - Footnotes via apparatus_merge.py (glossary rows carry a "section" field; status
    attested/provisional/decided ONLY). HIGH NOTE DENSITY (STYLE.local.md): gloss
    every named person/place/institution/event/period-term a non-specialist might not
    know, at first appearance -- BUT grep notes.json + out/ch0[1-6]_reading.md BEFORE
    re-noting; the cast is heavily noted already, so back-matter notes should TAPER
    (the foreword's Zhang Baijia and the series itself are the main NEW note targets;
    the appendices mostly re-tread noted ground -- cross-reference). Fact-check;
    verdict in the note. The 年谱/生平 will surface a few NEW minor names/places --
    crop-verify and gloss those.
  - Per unit: verify_unit.py <id>, check_structure.py/check_content.py --config
    data/check_config.<id>.json, make_bilingual.py <id> then qc_entities.py
    out/<id>_bilingual.md, check_numbers.py out/<id>_bilingual.md --noise
    data/noise.txt, check_align.py <id>, check_apparatus.py, check_register.py
    out/<id>_reading.md --ref out/ch01_reading.md. Build the cumulative EPUB,
    qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) 0/0.
  - Record everything in PROGRESS.md. Run to completion; do not pause for approval
    mid-batch.

Deliver the EPUB in chat AND paste the next kickoff (B10) verbatim in a fenced block.
All work on branch claude/chen-yangshan.
```

## What is DONE (do not redo)

- **Survey session:** full structure in book.json (6 chapters / 29 sections + 3
  appendices + references + afterword + series foreword); metadata; STYLE.md
  composed; skeleton EPUB.
- **B01 = Chapter 1** (ch01, PDF 12-37): 141 paragraphs, 73 footnotes. Voice-gate
  approved and FROZEN as the register reference.
- **B02 = Chapter 2, sections 1-3** (PDF 39-68). **B03 = Chapter 2, sections 4-5**
  (PDF 69-92): ch02 complete.
- **B04 = Chapter 3** (ch03, PDF 93-115): 125 paragraphs, 62 footnotes.
- **B05 = Chapter 4, sections 1-4** (PDF 117-146). **B06 = Chapter 4, sections 5-8**
  (PDF 147-171): ch04 complete (245 paras, 75 notes).
- **B07 = Chapter 5** (ch05, PDF 172-204, printed 161-193): 180 body paras, 47
  footnotes, 101 new glossary rows, 17 figures. Post-1949 to the Li Kenong death.
- **B08 = Chapter 6** (ch06, PDF 205-224, printed 194-213): 67 body paras (NO {v}
  blocks), 23 footnotes (book-wide 410), 40 new glossary rows (716 referents), 14
  figures (incl. the four end-of-chapter calligraphy tributes). The persecution and
  rehabilitation arc: the 1958 "anti-Party clique" case, twenty years' disgrace, ten
  years exiled in Ningxia through the Cultural Revolution, full rehabilitation 1983,
  the last working years and death (1991), the peroration. All gates green; qa PASS;
  epubcheck 0/0/0. **Chapters 1-6 (the whole body) COMPLETE.**

## Tooling in place (DO NOT REVERT)

- **OCR crop** (measured for this book): `ocr_crop.py --lang chi_sim --psm 6
  --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`, recto/
  verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`, run per-page in a loop (background it or chunk it). ocr_dual.py
  for the disagreement filter. indents.py/assemble.py UNUSED (data/zh is
  hand-assembled from corrected OCR + scans).
- `apparatus_merge.py`: glossary merges into SECTIONS via a `"section"` field on
  each row; `status` MUST be attested/provisional/decided. figures.json `file` is a
  BARE filename (p0NNN-f1.png); a figure `before` anchor must be a substring of the
  FIRST ~80 chars of its paragraph. Figures render BEFORE the anchor paragraph;
  several figures may share one anchor and render in list order (used for the four
  end-of-ch06 tributes, all anchored to the final obituary paragraph).
- `check_content` STRICT: the decided full glossary name must appear once in each
  paragraph the source names the referent (short forms/pronouns fail it). Do NOT
  glossary a title/word whose English collides with a common word.
- `build_reading_epub.sec_nav`: the EPUB nav omits pending (untranslated) sections.
  Chapters 1-6 fully translated; the front matter (ch00), appendices (ch07-ch09),
  references (ch10) and afterword (ch11) stay pending until B09/B10.
- **data/zh gitignored, regeneration protocol.** `data/zh/*.txt` do NOT survive a
  fresh checkout. Run parity/number/content/align/entity with the UNIT-SCOPED config
  (`data/check_config.<id>.json`); build/qa/epubcheck/register on the WHOLE
  cumulative EPUB; check_apparatus against the whole notes.json.
- **{v}/{p}/### /#### mirroring:** data/zh/<id>.txt and out/<id>_reading.md are
  hand-assembled STRUCTURALLY IDENTICAL line-for-line. Headings (`#`-prefixed) are
  dropped by the parity check; `{v}`/`{p}` prefixes are stripped before comparison.
- `data/noise.txt`: B08 added 5 rules (十余万 "more than a hundred thousand words",
  100多万 "more than a million words", 三十年代 "the 1930s", 九旬 "close on ninety",
  亿万 "hundreds of millions"). All magnitudes carried in the English; none masked.
- setup.sh regression "hook stands down on template stub: FAIL" is BENIGN (the
  fixture expects a placeholder HANDOFF; ours is real). All translation checkers pass.

## Renderings settled B08 / carry-forward

- Decided NEW in B08 (feed to authority.json at completion): Zheng Shaowen, Wang
  Huai'an, Wang Ruqi, Wang Yuechen, Liu Shangzhi, Tang Jinshi, Song Zicheng, Luo
  Zhiguang, Dong Biwu, Kang Jianmin, Huo Shilian, Ma Xin, Ding Yimin, Pei Zhouyu, Jin
  Zhaodian, Qu Rixin, Feng Jinchen, Zheng Xiaoxian, Gu Yizhi, Rou Shi, He Mengxiong,
  Li Qiushi, Wu Huai'e, Xiao Taihuang, He Changzhi, He Zhihua, Hu Weihua, Jiang An,
  Zhou Jianjie, Rong Xuan, Yu Ping, Huang Huoqing, Zhang Su, Li Yimang, Ling Yun.
  Places: Ningxia, Yinchuan, Ninghai County, Mengzhou. Orgs/events: the Reflection
  Institute, the College of Foreign Affairs, the Central Political-Legal Group, the
  Production Command, the Revolutionary Committee, the Anti-Rightist Campaign, the
  Seven Thousand Cadres Conference, the Five-Antis. Two sons decided earlier: Chen
  Jianyu (eldest, 建宇) and Chen Zhenyu (youngest, 震宇 → glossary en "Zhenyu").
  Consistent handles held: the Great Cultural Revolution (文化大革命, glossary en),
  the Campaign to Suppress Counterrevolutionaries, the Rectification Movement.
- Source error rendered as printed + footnoted (do NOT "fix"): 十届六中全会 (×2,
  printed 202) for what was in fact the Eleventh CC's Sixth Plenum (the 1981
  Resolution on Party History); crop-verified both, footnoted.
- ch06 has NO {v}/{p} set-off blocks: the letter and verdict quotations are inline
  within narrative paragraphs (introduced by "in the letter he said," etc.).

## Voice sheets (consult at every dialogue scene)

- **Chen Yangshan** (subject). Earnest, modest, understated; plain and sincere,
  deflects credit. In the persecution chapter (ch06) he is steady and uncomplaining;
  the indignation is the author's, carried in the facts, not adjectives. In Appendix
  II (ch08, his own posthumous writing) keep the FIRST-PERSON plain and dry: no
  ornament, no heroics; he reports rather than emotes.
- **Li Kenong** (Chen's intelligence chief). Senior, precise, warm to Chen; brief
  practical instructions; unassuming; the donkey-and-load saying.
- **He Long.** Blunt, earthy, proud, short concrete declaratives.
- **Zhou Enlai.** Measured, strategic, courteous; principled directives quietly.
- **Kang Sheng.** Cold, sinuous, dangerous; controlled, not cartoonish.
- **Chen Geng.** Warm, bold, decisive; a soldier's ease.

## Where the book stands

- Chapters 1-6 COMPLETE: the whole narrative body, from the poor Huzhou boyhood
  through the underground, the Special Branch, Yan'an, the Jin-Sui intelligence war,
  the post-1949 heights, and the persecution-and-rehabilitation arc to Chen's death
  in 1991 and the closing tributes.
- Remaining: the FRAMING matter. B09 = front + back matter translation (series
  foreword ch00 + appendices I-III ch07-ch09 + references ch10). B10 = afterword
  ch11 + whole-book close (reconcile sweep, cover, term ledger, deep audit,
  COMPLETION.md, commit the final EPUB).

## What is NEXT

- **B09 = front + back matter** (ch00 foreword PDF 7-8; ch07 Appendix I PDF 225-227;
  ch08 Appendix II PDF 228-233; ch09 Appendix III 年谱 PDF 234-238; ch10 References
  PDF 239-240). FIVE new units; add each to both check configs. The 年谱 (ch09) is
  numbers-dense — run check_numbers hard and verify the last entry on every page.
- **B10 = afterword + whole-book close** (ch11 afterword PDF 241-242; then reconcile,
  cover, term ledger, deep audit, COMPLETION.md, commit final EPUB).

## Open traps / environment state

- BODY offset printed = pdf - 11 (constant). FRONT MATTER runs a SECOND folio
  sequence (foreword printed 1-2 at PDF 7-8). Chapter-opener rectos carry a photo
  above the heading (SKIP it; ch06's opener photo is the SAME image as the captioned
  in-text figure on PDF 214, which IS included). PDF p243 is an Anna's Archive
  metadata leaf; frontispiece portrait at PDF p5, colour cover at p1.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract=0.
  The per-page ocr loop and ocr_dual.py exceed a 120s foreground timeout on a full
  chapter -- background them or chunk the range.
- Reading files are PLAIN ASCII (straight quotes, literal em dash only for real
  interruption or a bracketed aside; NO dashed appositive glosses). Note bodies:
  numeric character references only (&#8211; &#8212; &#160; &#8220; &#8221;), never
  named entities; <i> is allowed. Note ANCHORS must be verbatim ASCII substrings of
  the reading file (straight quotes, not &quot;).
- check_content is STRICT (full name once per paragraph); watch capitalization of
  glossary handles (B08: "Ninghai County" vs "Ninghai county" tripped it once).
- A long single paragraph's TAIL, and an isolated short final line at a page bottom,
  can be silently dropped by OCR. Verify against the scan.
- Figure alt: NO straight double quotes. figures.json `file` is a BARE filename; the
  `before` anchor must be within the first ~80 chars of its paragraph. Crop OUT
  captions AND bio-box text. find_figures MISSES line art/calligraphy (ch06's four
  tribute inscriptions were cropped and transcribed-in-caption by hand).
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup if the
  container is fresh).
