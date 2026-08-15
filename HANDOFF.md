# HANDOFF — China's Secret War (中国秘密战)

B05 (Chapter 4, the whole chapter, plus Chapter 4's Principal Sources) is
translated, built, and QA-clean. Chapter 4 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B06 (Chapter 5,
the whole chapter).

## Message to paste into the next chat

```
China's Secret War B06

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B06 = Chapter 5 (第五章 深入虎穴 / "Into the Tiger's Den"), the whole
chapter, ch05s01-ch05s08, end to end per the CLAUDE.md pipeline. PDF pages
184-222; printed pages 148-186 (offset constant: printed = pdf - 36; spot-verify
each section opener's folio off the scan). Section openers: s1 "东方大黑暗"！
(The Great Darkness in the East) PDF 184 / printed 148; s2 是谁向斯大林通报德国
侵苏情报？(Who Warned Stalin of Germany's Invasion of the USSR?) PDF 187 /
printed 151; s3 毛泽东的情报分析方式——调查研究 (Mao Zedong's Method of
Intelligence Analysis: Investigation and Study) PDF 193 / printed 157; s4 延安
出击 (Yan'an Strikes Out) PDF 197 / printed 161; s5 西安织网 (Weaving the Net in
Xi'an) PDF 200 / printed 164; s6 战地军情急 (Urgent Military Intelligence at the
Front) PDF 203 / printed 167; s7 突破"国防线"！(Breaking Through the "National
Defense Line") PDF 207 / printed 171; s8 挑战情报强国 (Challenging the
Intelligence Powers) PDF 211 / printed 175. Chapter 6 opens at PDF 223 / printed
187, which is your stop. Chapter 5 carries its OWN chapter-end Principal Sources
(主要资料); render it as a translated "### Principal Sources" section, same
treatment as ch01-ch04. Simplified Chinese, horizontal; chi_sim, psm 6;
PaddleOCR absent, use scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 184 222 --dpi 300 -> ocr_crop 184 222 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 184 222 ->
indents 184 222 -> add the chapter title, subtitle, and section 1-8 heading
strings (as the OCR reads them) to data/structure.json -> assemble ch05 184 222
--offset 36 --blank-assist -> find_figures (the 图文版 has many inline photos;
figures remain DEFERRED, see below) -> translate to out/ch05_reading.md, one
paragraph per TRUE source paragraph.

IMPORTANT LESSON FROM B05: on the figure-dense 图文 pages the OCR (both psm6/psm4
AND ocr_dual) merges four-to-eight true paragraphs per plate and injects photo-
caption and vertical-running-title bleed as pure garbage mid-line. In B05 the
whole chapter had to be read off the scan by eye, page by page, because the
assembled scaffold was unusable on the worst pages. EXPECT the same for
Chapter 5 (it is a big, plate-heavy chapter). The reliable method proved to be:
read every page image (data/png/pNNNN.png) directly, transcribe and verify each
true paragraph against BOTH OCR configs, then write a scripts/resegment_ch05.py
that HARDCODES the verified paragraph list and rebuilds data/zh/ch05.txt from it
(model it on scripts/resegment_ch04.py -- an ('h'|'b', text) item list, NOT the
merge/split-on-garbled-anchor bridge of resegment_ch03.py, which cannot land its
markers on this level of corruption). Then verify_unit ch05 / check_align ch05 /
qc_entities on out/ch05_bilingual.md (check_content is N/A to this project's
schema; qc_entities is a vacuous pass on the flat glossary -- ensure entity
survival by hand; the number check is noisy, run via verify_unit which passes
--noise data/noise.txt, and verify EVERY quantity against the SCAN) -> apparatus_
merge for notes and glossary -> build EPUB -> qa_epub (green) and epubcheck
(clean) -> check_register --ref out/ch01_reading.md out/ch05_reading.md (ch01 is
the FROZEN reference; the dialogue metric is noise in low-dialogue units, judge on
the narratorial signals) -> write PROGRESS and the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of Chapter 4
(out/ch04_reading.md, section 5's "escorted out" close and the Principal Sources)
for the voice; consult the VOICE SHEETS and glossary in this HANDOFF. Cite the
book's PRINTED folios in notes, never PDF pages. Never invent bridging text: if
OCR cuts off, crop the scan and read the real continuation. WATCH THE SECTION
TAILS: a section's last paragraphs often straddle onto the NEXT section's opening
page before the heading (in B05 section 1's closing punch line sat on top of the
section-2 page), and the 图文 pages hide one-line PUNCH paragraphs that the OCR
merges -- read past each heading and each plate. Verify every name, number, and
unit designation by crop before writing (B05 caught 张中堂 mis-OCR'd three ways,
蒋龙涎, 马豫章 garbled four ways, and 万里迢迢 that is NOT a person). Render load-
bearing figures and unit designations in DIGITS (the 359th Brigade, 200,000
troops, 4,500 killed) per STYLE. State corroborated/uncorroborated/contradicted
in notes; the partisan voice is content, the counter-record goes in the footnote.

Do NOT pause for approval mid-batch. Deliver the EPUB in chat and paste the
next kickoff verbatim in the same reply.

Work on branch claude/chinas-secret-war only (CLAUDE.md rule 2); expect a
stray per-task branch at session start and consolidate onto the canonical
branch.
```

## What is DONE

- **Survey (Step 0a + 0b), approved.** book.json carries full metadata and the
  complete structure (12 chapters, 86 sections, + Preface + Afterword).
- **B01 = Preface (ch00) + Chapter 1 (ch01).** Translated, built, QA-clean.
  ch01 is the FROZEN voice reference. Voice gate passed.
- **B02 = Chapter 2, sections 1-5.** See PROGRESS "Batch B02."
- **B03 = Chapter 2, sections 6-8 + Chapter 2 Principal Sources.** Chapter 2
  COMPLETE. See PROGRESS "Batch B03."
- **B04 = Chapter 3, the whole chapter + Chapter 3 Principal Sources.** Chapter 3
  COMPLETE. See PROGRESS "Batch B04."
- **B05 = Chapter 4, the whole chapter + Chapter 4 Principal Sources.** 119
  English body paragraphs (1:1 parity). +14 notes (book total 98); +25 glossary
  rows (101 total). qa_epub PASS; epubcheck 0/0/0/0. **Chapter 4 is COMPLETE.**
  See PROGRESS "Batch B05."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6.
- **scripts/assemble.py**: --blank-assist (blank-line signal layered on the
  indent, gated by sentence-end) for figure-heavy pages.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; sec_nav
  omits a pending section from the nav of a PARTIALLY translated chapter
  (epubcheck NAV-011 fix). Chapter 5 will again be partially translated during
  the batch, so this matters.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip the '***'
  scene-break marker, matching verify_unit / check_structure.
- **scripts/resegment_ch02.py, resegment_ch02b03.py, resegment_ch03.py**: the
  merge/split-on-garbled-anchor re-segmentation for the earlier figure-heavy
  chapters.
- **scripts/resegment_ch04.py**: NEW and the model for Chapter 5. When the OCR is
  too caption-corrupted to serve even as a merge/split scaffold, this rebuilds
  data/zh/chNN.txt from a HARDCODED, hand-verified ('h'|'b', text) item list read
  off the scan. Model resegment_ch05.py on it (NOT on resegment_ch03.py).
- **data/noise.txt**: carries this book's number-check noise rules; extend it
  (longest-first, each commented with its value and the English phrase) as new
  idioms/place-names/name-numerals/arabic-万 artifacts surface.
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args.
- **qc_entities.py is a VACUOUS PASS** on this project's flat glossary schema (zh
  keyed at top level, not nested sections). It reports 0 misses because it finds
  no entities. Ensure entity survival BY HAND during translation (render every
  glossary hanzi). Do not trust its "0 misses" as coverage.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 101 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ
forever): the Eighth Route Army office / 八办 ("ba-ban", glossed); the Social
Affairs Department (中社部); the Central Intelligence Department (中情部); the
Border Security (边保); the Southern Bureau (南方局); Juntong; Zhongtong; the
Special Branch (中央特科). Chapter 5 ("深入虎穴" -- CCP intelligence goes on the
offensive into Japanese-occupied and Nationalist territory, the Sorge/Barbarossa
material, Mao's "investigation and study" method, the Xi'an and front-line nets)
will re-use Kang Sheng, the Border Security, Xiong Xianghui and the Xi'an station,
Hu Zongnan, and the Yan'an security organs heavily. NEW from B05 to reuse: the
Border Region "friction" vocabulary (磨擦 = friction), 双重政权, Xi Zhongxun,
Wang Zhen (359th Brigade), Bu Lu / Chen Bo, 关中/陇东/绥德 sub-districts.

CONSISTENCY LEDGER points (do not re-decide):
- 杜理卿 (Du Liqing) = 许建国 (Xu Jianguo) are ONE man (glossary row records it).
- Kang Sheng's alias Zhao Rong; born Zhang Zongke / Zhang Wang (settled in B01).
- "black dogs" (黑狗子 = KMT police), the "far country" (远方 = USSR / Comintern),
  the "'38-style" cadre, "reform and opening" (改革开放, the author's recurring
  anachronistic motif -- render consistently, noted once in ch02, do NOT re-note).
- 磨擦 = "friction" (noted ch04); 双重政权 = "dual regime" (noted ch04);
  锄奸 = "rooting out traitors"/chujian (glossed ch04, points to Chapter 7);
  皖南事变 = "the New Fourth Army Incident" (noted ch03, do NOT re-note).
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file (confirmed ch01-ch04; do the same for ch05).
- Tan Kah Kee (陈嘉庚), Ho Chi Minh, Aung San, Bethune, Edgar Snow / Red Star Over
  China, Stilwell (史迪威) -- conventional English forms, already glossary/noted.
- Bu Lu / Chen Bo, Xi Zhongxun, Du Bincheng, Wang Zhen, Ma Hongkui, He Shaonan,
  Pingjiang Massacre -- all noted in ch04; reuse the glossary rows, do NOT re-note.

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line PUNCH paragraphs (the 图文 OCR merges these -- split them back
  out), rhetorical questions kept sparingly (only where they land in English),
  datebook chronology staccato, the inclusive "we." Runs HOT in the political
  set-pieces and SARDONIC on the enemy and on turncoats-become-officials; keep
  both. Partisan by design; counter-record lives in the footnotes. Exclamation
  rationed hard (period by default); most rhetorical questions converted to
  statements; "so it turns out" reveal wrappers dropped. Em dashes rationed to
  near-zero in the translation (ch03 and ch04 both shipped with ZERO). Chapter 4's
  close is a run of one-line rhetorical questions turning toward Chapter 5 ("Could
  a green red spy outfight the seasoned Japanese agent?") -- keep that momentum.
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts.
  Keep the warmth and the edge. In ch04 the coiner of "friction" and the drafter,
  in his own hand, of the courtly-classical ultimatum telegram. Chapter 5 gives
  him the "investigation and study" intelligence-method set piece -- expect him
  didactic and folksy at once.
- **Zhou Enlai:** measured, precise, terse when sharp; a man of "feeling and
  honor." The presiding figure of ch03.
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative,
  strategic, cold, ruthless. Render 老蒋 as "old Chiang" / 蒋委员长 as "Generalissimo
  Chiang." In ch04 the cynical delegator who "would not wear the hat himself."
- **Kang Sheng ("Boss Kang" for 康老板):** in ch04 the political scold who dresses
  Bu Lu down for a "tactical victory, strategic defeat." Sharp, doctrinaire,
  worried about the political optics. Keep the menace under the reasonableness.
- **Xu Enzeng (memoir), Zhang Yanfo (confession-memoir), Dimitrov (directive),
  interviewees (written recollection):** formal document/reminiscence register,
  kept formal but never wooden. The Principal Sources entries are this register.
- **Deng Xiaoping (reflective aside, ch02):** warm, plain, unhurried.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the
Yan'an security state. Chapter 3 built the open Eighth Route Army offices and the
Chongqing/Xi'an intelligence webs. Chapter 4 ("拔钉子" / "Pulling Out the Nails")
is now COMPLETE: the "dual regimes" of the Border Region (both Nationalists and
Communists appointing rival county governments); the threats to Mao's own safety
in Yan'an; the contest over the Guanzhong "treasure gourd" salient and Xi
Zhongxun's restraint against Hu Zongnan's friction; the "Red Sherlock Holmes"
(Bu Lu / Chen Bo) running disguise operations inside the Nationalist county
branches; the anti-corruption storm that broke "Commissioner Friction" He Shaonan
at Suide; and the "escorting out of the territory" of the last Nationalist organs
by the spring of 1941, closing with the Border Security turning from defense to
offense -- issuing the order to send "red spies" into enemy territory. Chapter 5
("深入虎穴" / "Into the Tiger's Den") takes up that offensive: CCP intelligence
officers going on the attack, the "Great Darkness in the East," the warning to
Stalin of the German invasion, Mao's investigation-and-study method, and the nets
woven at Yan'an, Xi'an, and the front.

## Open traps and environment

- **The 图文 OCR is UNUSABLE as a scaffold on plate-dense pages.** This bit every
  batch and was worst in B05 (whole chapter read off the scan). Read every page
  image by eye, verify against both OCR configs, and rebuild data/zh via a
  hardcoded resegment_ch05.py (model: resegment_ch04.py). NOT idempotent versus
  assemble -- resegment WRITES the file wholesale, so it does not need assemble
  re-run first, but keep assemble's run in the pipeline for the pagemap/heading
  detection sanity check.
- **Section tails straddle pages AND one-line punch paragraphs hide on figure
  pages.** Read PAST each section heading and each plate.
- **Number check is noisy** (OCR-lossy zh; unit designations, dates, decade
  labels, name numerals, arabic-万 artifacts). Run via verify_unit (it passes
  --noise data/noise.txt), extend noise.txt (each entry commented with its value
  and the English phrase), and verify every quantity against the SCAN. Digits for
  load-bearing figures and unit designations per STYLE. Arabic-万 ("20万") and
  X多万 ("十多万") tokenize to an orphan 万=10000 the checker can't join; noise the
  specific literal and carry the value in the English as digits (see the B05
  entries at the tail of noise.txt for the pattern).
- **check_content is N/A** to this project's book.json schema. Rely on
  check_align + parity + the manual zh<->en read.
- **qc_entities is vacuous** on the flat glossary (see Tooling). Ensure entity
  survival by hand.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; catalog them in PROGRESS as a deliberate decision. The standing
  question (every photo, or a curated subset) is still for the commissioner.
- **Source notes are PER-CHAPTER** (主要资料). Chapter 5's fall at the end of
  section 8; render as a translated "Principal Sources" section.
- **Printed-page markers**: ch04 HAS folio markers (resegment_ch04 rebuilds the
  pagemap cleanly). ch03 has NONE (stale post-resegment indices; a clean rebuild
  is a corrections-pass task). ch01 zh parity 269/299 (from B01) also still open.
  No note cites a ch03 folio, so nothing depends on it.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B05 completion
reply in chat, as CLAUDE.md requires.
