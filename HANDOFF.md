# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with the block below PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 9 (front + back matter: ch00 foreword, ch07 Appendix I, ch08 Appendix II,
ch09 Appendix III 年谱, ch10 References) is COMPLETE: translated, annotated, four
figures placed, built, all gates green (parity 6/14/38/76/42 exact; entities 0
misses; content aligned; numbers 0 unresolved incl. the numbers-dense 年谱;
apparatus 0/0; register within tolerance; qa_epub PASS; epubcheck 0/0/0). Only
ch11 (Afterword) and the whole-book close remain. The block below is the Batch 10
kickoff (the LIGHT final batch), ready to paste.

## Message to paste into the next chat

```
Chen Yangshan B10

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset for the BODY: printed = pdf
- 11 (constant). Chapter 1 is the FROZEN register reference
(check_register.py --ref out/ch01_reading.md). Chapters 1-6 and the front/back
matter (ch00, ch07-ch10) are DONE. This is the LIGHT final batch.

Do Batch 10 = ch11 Afterword + WHOLE-BOOK CLOSE, end to end per the CLAUDE.md
pipeline.
  - ch11 = 后记 "Afterword" (by the author Yao Huafei), PDF 241-242 (printed
    230-231). ~1.5 pages of running prose: how the book was made (two-plus years'
    research, interviews with the son 程建宇 Cheng Jianyu, 秦杰, 金楚宣; six drafts
    over ten years; the earlier 2006 edition 《隐蔽战线福将陈养山传奇》, China
    Friendship Publishing). Render one paragraph per source line; ch11 is running
    prose (no {v}). Author's own voice; keep it plain and warm, not inflated.
    Make out/ch11_reading.md + data/zh/ch11.txt and ADD ch11 to
    data/check_config.json AND a scoped data/check_config.ch11.json.
  - render 241-242 and OCR with the SAME body crop as ch01-ch06 (do-not-revert
    below): ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985
    --top 0.08 --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945,
    VERSO (PDF odd) --bottom 0.915, per-page. Background the loop; pgrep -c
    tesseract must read 0 after. WATCH the silent OCR loss on the page bottom and
    on any long paragraph's tail; verify the final paragraphs against the scan.
  - THEN THE WHOLE-BOOK CLOSE (check 12 and the definition of done):
    * Whole-book reconciliation sweep (check_reconcile.py + a HUMAN read of its
      drift candidates). THREE FLAGS ALREADY IDENTIFIED IN B09 (see PROGRESS
      "FLAGS FOR THE B10 WHOLE-BOOK RECONCILE"): (1) the 1988 letter is rendered
      twice, ch03s03 {v} vs ch08(二) running prose, wording diverges -- decide
      whether to harmonize; (2) Xiao Shouhuang (肖寿煌, appendix + ch03,
      crop-verified) vs Xiao Taihuang (肖太煌, ch06) is a SOURCE variant -- render
      each as printed, add ONE note flagging it, do not silently harmonize;
      (3) rehabilitation timeline (1978 vs 1983) already noted in ch07, confirm
      consistent. Also grep-count the ~20 decided renderings; confirm notes sit at
      first appearance.
    * Cover: decide whether to use the frontispiece portrait or keep the generated
      typographic cover (book.json cover_image is unset -> typographic). The colour
      cover is at PDF p1 if you want to try it.
    * out/term_ledger.md (render the glossary ledger); feed this book's decided
      renderings into authority.json (lists in each batch's PROGRESS "NEW decided
      renderings").
    * out/deep_audit.md: random-sample deep audit, 3-5% of the book, fixed seed,
      honest error rate. Watch the "invented precision" class.
    * COMPLETION.md from the template (sampled error rate + residual
      uncertainties). Rewrite HANDOFF.md to say the book is COMPLETE.
    * On the title page the build must read COMPLETE once ch11 exists (12 of 12).
    * COMMIT THE FINAL EPUB ITSELF: git add -f out/chen-yangshan.epub (branches
      outlive containers, chat attachments do not).
  - Per unit: verify_unit.py ch11, check_structure.py/check_content.py --config
    data/check_config.ch11.json, make_bilingual.py ch11 then qc_entities.py,
    check_numbers.py --noise data/noise.txt, check_align.py ch11,
    check_apparatus.py, check_register.py out/ch11_reading.md --ref
    out/ch01_reading.md. Build the cumulative EPUB, qa_epub.py green, epubcheck
    (/tmp/epubcheck-5.1.0/epubcheck.jar) 0/0.
  - Notes taper hard here: the afterword mostly re-treads noted ground
    (grep notes.json + out/ch0*_reading.md BEFORE re-noting). Cite PRINTED folios.
    Never invent bridging text; verify the final paragraphs.
  - Record everything in PROGRESS.md. Run to completion; do not pause for approval.

Deliver the EPUB in chat AND (since this is the final batch) present COMPLETION.md.
All work on branch claude/chen-yangshan.
```

## What is DONE (do not redo)

- **Survey session:** full structure in book.json; metadata; STYLE.md composed;
  skeleton EPUB.
- **B01 = Chapter 1** (ch01, PDF 12-37): voice-gate approved; FROZEN register
  reference. **B02-B03 = Chapter 2** (PDF 39-92). **B04 = Chapter 3** (PDF 93-115).
  **B05-B06 = Chapter 4** (PDF 117-171). **B07 = Chapter 5** (PDF 172-204).
  **B08 = Chapter 6** (PDF 205-224). Chapters 1-6 (the whole narrative body)
  COMPLETE.
- **B09 = front + back matter** (this batch): ch00 foreword (PDF 7-8, 6 paras,
  4 notes); ch07 Appendix I obituary (PDF 225-227, 14 paras, 6 notes); ch08
  Appendix II Chen's posthumous writings (PDF 228-233, 38 paras, 5 notes, 3
  facsimile figures); ch09 Appendix III 年谱 (PDF 234-238, 76 paras, 2 notes,
  numbers 76/76 clean); ch10 References (PDF 239-240, 42 citations, 1 note). Plus
  the frontispiece portrait placed at ch07. Book-wide 428 notes, glossary 718
  referents. All gates green; qa PASS; epubcheck 0/0/0.

## Tooling in place (DO NOT REVERT)

- **OCR crop (body, ch01-06 and back matter):** `ocr_crop.py --lang chi_sim
  --psm 6 --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`,
  recto/verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`, per-page. **Front-matter pages (7-8) used a DIFFERENT crop**
  (no top running head; folios and a running foot below): `--top 0.05 --bottom
  0.90-0.92`, no running-head match. ocr_dual.py for the disagreement filter.
  indents.py/assemble.py UNUSED (data/zh is hand-assembled from corrected OCR +
  scans).
- `apparatus_merge.py`: glossary merges into SECTIONS via a `"section"` field;
  `status` MUST be attested/provisional/decided. figures.json `file` is a BARE
  filename (p0NNN-f1.png); a figure `before` anchor must be a substring of the
  FIRST ~80 chars of its paragraph. Figures render BEFORE the anchor paragraph.
- `check_content` STRICT: the decided full glossary name must appear once in each
  paragraph the source names the referent (short forms/pronouns fail it). B09
  hits fixed: 中国青年 -> "China Youth" (not "Chinese Youth"); 陈赓大将 -> "General
  Chen Geng"; a 年谱 entry needed "Chen Yangshan" spelled out.
- **No-section units (ch00, ch07, ch09, ch10)** lead with a single `### ` heading
  (renders h2, dropped from parity); **ch08** leads with `### ` chapter title then
  `#### ` sub-part headings. All heading levels stay consistent with ch01-06
  (position-0 level 3); shape checks run per-unit and pass trivially.
- **data/zh gitignored, regeneration protocol.** `data/zh/*.txt` do NOT survive a
  fresh checkout. Run parity/number/content/align/entity with the UNIT-SCOPED
  config (`data/check_config.<id>.json`); build/qa/epubcheck/register on the WHOLE
  cumulative EPUB; check_apparatus against the whole notes.json. The MAIN
  check_config.json now lists ch00-ch10 but CANNOT be run whole on a fresh
  checkout (ch01-06 zh absent) -- use the scoped configs.
- `data/noise.txt`: B09 added 章百家, 十万余, 百花, 大百科全书 (all name/lexical;
  no real quantity masked).
- setup.sh regression "hook stands down on template stub: FAIL" is BENIGN (the
  fixture expects a placeholder HANDOFF; ours is real).

## Carry-forward / renderings settled B09

- **Cheng Jianyu** (程建宇), Chen's eldest son, signs the appendix note and is
  thanked in the afterword; he uses the family's ORIGINAL surname Cheng (程), which
  Chen changed to Chen (陈) for underground work. The glossary's 陈建宇 -> "Chen
  Jianyu" is the SAME person under the assumed surname; render 程建宇 as printed
  ("Cheng Jianyu"), noted.
- Chen's underground cover names (from the 年谱 intro): Chen Yingzhou (陈英舟),
  Chen Deqing (陈德清), Gao Junshi (高君实), Lao Wang (老王), Chen Zhongying,
  Chen Mingjun.
- The four Special Branch comrades Kang Sheng framed (already noted in ch03/ch06):
  Wu Hujing (武胡景, orig. 武怀让 Wu Huairang; wife Hou Zhi), Xiao Shouhuang
  (肖寿煌; SEE B10 flag on the ch06 variant Xiao Taihuang), He Changzhi (贺昌之,
  the appendix's primary form 贺长炽 He Changchi), Ouyang Xin. Cao Yi'ou = Kang
  Sheng's wife; her sister Su Mei was Xiao Shouhuang's wife.
- Zhang Baijia (章百家), foreword author, party historian. Xu Xiangqian, Wang
  Yifei, Zhang Xiushan, Liu Bowen, Liu Fuzhi already handled.

## Voice sheets (consult at every dialogue scene)

- **Chen Yangshan** (subject). Earnest, modest, understated; deflects credit. In
  his own posthumous writing (ch08) the FIRST-PERSON is plain and dry: he reports
  rather than emotes. In the afterword the voice is the AUTHOR's, not Chen's.
- **Yao Huafei (author).** Admiring Party-biography reportage; warm, reverent
  toward the martyrs, dense with dates and offices. In the afterword he speaks in
  his own person about how the book was made; keep it plain and warm, not inflated.
- Li Kenong, He Long, Zhou Enlai, Kang Sheng, Chen Geng: see earlier handoffs.

## Where the book stands

- Chapters 1-6 (narrative body) COMPLETE; front + back matter (foreword,
  appendices I-III, references) COMPLETE. Remaining: the Afterword (ch11) and the
  whole-book close.

## What is NEXT

- **B10 = ch11 Afterword (PDF 241-242) + whole-book close.** The LIGHT final
  batch: afterword, reconcile sweep (act on the three flags in PROGRESS), cover
  decision, term ledger, deep audit, COMPLETION.md, and commit the final EPUB
  (git add -f out/chen-yangshan.epub).

## Open traps / environment state

- BODY offset printed = pdf - 11. FRONT MATTER ran a second folio sequence
  (foreword printed 1-2 at PDF 7-8). PDF p243 is an Anna's Archive metadata leaf;
  frontispiece portrait at PDF p5 (now placed at ch07), colour cover at p1.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract=0.
  The per-page ocr loop exceeds a 120s foreground timeout on a full chapter; for
  the 2-page afterword it is trivial.
- Reading files are PLAIN ASCII with straight quotes and a literal em dash only
  for real interruption or a bracketed aside; NO dashed appositive glosses. Note
  bodies: numeric character references only (&#8211; &#8212; &#160;), never named
  entities; hanzi inline are fine; <i> allowed. Note ANCHORS must be verbatim ASCII
  substrings of the reading file.
- Figure alt: NO straight double quotes. figures.json `file` is a BARE filename;
  the `before` anchor must be within the first ~80 chars of its paragraph.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup if the
  container is fresh; setup.sh does this, but it did NOT run in B09's container and
  was fetched by hand).
