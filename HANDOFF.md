# HANDOFF -- China's Secret War (中国秘密战)

B08 (Chapter 7, the whole chapter, plus Chapter 7's Principal Sources) is
translated, built, and QA-clean. Chapter 7 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B09 (Chapter 8,
the whole chapter). Chapter 7 ("锄奸" / "Rooting Out Traitors") laid out the
whole defensive war of counter-espionage; Chapter 8 ("延安反特第一案" / "Yan'an's
First Great Counter-espionage Case") turns to a single set-piece case, the
winning policy of "turning the enemy to serve us."

## Message to paste into the next chat

```
China's Secret War B09

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B09 = Chapter 8 (第八章 延安反特第一案 / "Yan'an's First Great
Counter-espionage Case"), the whole chapter, ch08s01-ch08s06, end to end per the
CLAUDE.md pipeline. PDF pages 282-304; printed pages 246-268 (offset constant:
printed = pdf - 36; spot-verify each section opener's folio off the scan).
Section openers: s1 军统有个"死间"特训班 (Juntong's Special Training Class for
"Expendable Agents") PDF 282 / printed 246; s2 放线与织网 (Casting the Line and
Weaving the Net) PDF 284 / printed 248; s3 大案惊天！(A Case to Shake the
Heavens!) PDF 288 / printed 252; s4 侦控特务联络员 (Tracking the Agents' Couriers)
PDF 291 / printed 255; s5 深挖独立小组 (Digging Out the Independent Cell) PDF 294 /
printed 258; s6 反用特务 (Turning Enemy Agents to Our Use) PDF 295 / printed 259.
Chapter 9 opens at PDF 305 / printed 269, which is your stop. Chapter 8 carries
its OWN chapter-end Principal Sources (参考资料 / 主要资料); render it as a
translated "### Principal Sources" section, same treatment as ch01-ch07.
Simplified Chinese, horizontal; chi_sim, psm 6; PaddleOCR absent, use
scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 282 304 --dpi 300 -> ocr_crop 282 304 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 282 304 ->
indents 282 304 -> add the chapter title, subtitle, and section 1-6 heading
strings (as the OCR reads them) to data/structure.json -> assemble ch08 282 304
--offset 36 --blank-assist -> find_figures (the 图文版 has many inline photos;
figures remain DEFERRED, see below) -> translate to out/ch08_reading.md, one
paragraph per TRUE source paragraph.

METHOD (proven B04-B08): read every page image (data/png/pNNNN.png) by eye,
transcribe each TRUE source paragraph, verify against BOTH OCR configs, and write
scripts/resegment_ch08.py that HARDCODES the verified ('h'|'b', text) item list
and rebuilds data/zh/ch08.txt wholesale (model: scripts/resegment_ch07.py /
resegment_ch06.py). NOTE from B06-B08: this book's STRAIGHT text pages OCR
cleanly, so assemble.py is a useful independent paragraph-BOUNDARY cross-check
(compare its body count to your resegment count; on ch07 assemble read 216 vs the
223 hand count, the +7 being one-line PUNCH paragraphs assemble merges) -- but the
plate and column-wrap pages STILL merge four-to-eight true paragraphs and inject
photo-caption and vertical-running-title bleed, so the hand-verified resegment
stays authoritative. Keep assemble in the pipeline for the pagemap/heading check.
Use indents.py to settle every page-break seam: a page top whose first line is
INDENTED starts a NEW paragraph, a non-indented top CONTINUES the previous
page's last paragraph (on ch07 only pdf 257 was indented). Any one-line PUNCH
paragraph is its own line/pair.

Then: make_bilingual ch08 -> verify_unit ch08 (parity + numbers + anchors; it
passes --noise data/noise.txt itself, do NOT add flags) -> check_align ch08 ->
qc_entities is vacuous on the flat glossary -- ensure entity survival BY HAND;
verify EVERY quantity against the SCAN. Number check is noisy: numerals inside
names/places/idioms/titles go in data/noise.txt (literal phrase, longest-first,
each commented with its value and the English phrase); a mixed Arabic+万 form
(e.g. 3万) the reader can't combine, so if the value is carried in English, noise
the literal form; a REAL dropped quantity is fixed in the English, never noised.
Prefer REWORDING to carry a number. Then apparatus_merge for notes+glossary ->
check_apparatus (0 failures; the 19 attestation-note warnings on old rows are
pre-existing, not yours) -> build_reading_epub -> qa_epub (green) and epubcheck
(java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub; clean)
-> check_register --ref out/ch01_reading.md out/ch08_reading.md (ch01 is the
FROZEN reference; the dialogue metric is noise in low-dialogue units -- Chapter 8
is a single case narrative, likely dialogue-light like ch07, so judge on the
narratorial signals and CONTRACT any genuine conversational speech, leave
documents/telegrams/oaths formal). Watch the em-dash rate: keep it near ch06/ch07
(~4.5/1k), convert appositive-gloss dashes to colons/commas. Then write PROGRESS
and the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of Chapter 7
(out/ch07_reading.md, section 6's close: the "reversal stratagem" cases, the
"divergence of wits", and the closing "can an agent's heart be turned toward the
Communists?" -- which sets up Chapter 8) for the voice; consult the VOICE SHEETS
and glossary in this HANDOFF. Cite the book's PRINTED folios in notes, never PDF
pages. Never invent bridging text: if OCR cuts off or a leaf is faded, crop the
scan and read the real continuation. Verify every name, number, and unit
designation by crop before writing (use verify_names.py --auto for the dual-OCR
disagreement filter, then magnified PIL crops for the dense rosters); render
load-bearing figures and unit designations in DIGITS per STYLE. Keep
anonymized-by-某 people anonymized. State corroborated / uncorroborated /
contradicted in notes; the partisan voice is content, the counter-record goes in
the footnote (fact-check hard against Wikipedia/Baidu/academic, never Grok or any
AI reference).

Do NOT pause for approval mid-batch. Deliver the EPUB in chat and paste the
next kickoff verbatim in the same reply.

Work on branch claude/chinas-secret-war only (CLAUDE.md rule 2); expect a
stray per-task branch at session start and consolidate onto the canonical
branch.
```

## What is DONE

- **Survey (Step 0a + 0b), approved.** book.json carries full metadata and the
  complete structure (12 chapters, 86 sections, + Preface + Afterword).
- **B01 = Preface (ch00) + Chapter 1 (ch01).** ch01 is the FROZEN voice
  reference. Voice gate passed.
- **B02 = Chapter 2, sections 1-5.**
- **B03 = Chapter 2, sections 6-8 + Chapter 2 Principal Sources.** Chapter 2 COMPLETE.
- **B04 = Chapter 3, the whole chapter + Principal Sources.** Chapter 3 COMPLETE.
- **B05 = Chapter 4, the whole chapter + Principal Sources.** Chapter 4 COMPLETE.
- **B06 = Chapter 5, the whole chapter + Principal Sources.** Chapter 5 COMPLETE.
- **B07 = Chapter 6, the whole chapter + Principal Sources.** Chapter 6 COMPLETE.
- **B08 = Chapter 7 (锄奸) + Principal Sources.** 223 English body paragraphs
  (1:1 parity). +27 notes (book total 161); +37 glossary rows (189 total).
  qa_epub PASS; epubcheck 0/0/0/0; register within tolerance; em-dash 4.7/1k.
  **Chapter 7 is COMPLETE.** See PROGRESS "Batch B08."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6. Do NOT re-measure.
- **scripts/assemble.py**: --blank-assist. On this book the straight text pages
  OCR cleanly, so assemble is a good paragraph-BOUNDARY cross-check; the plate/
  wrap pages still merge and must be hand-verified. NOTE: assemble OVERWRITES
  data/zh/chNN.txt, so re-run resegment_chNN.py AFTER assemble.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; sec_nav
  omits a pending section from the nav of a PARTIALLY translated chapter
  (epubcheck NAV-011 fix). Chapter 8 will again be partially translated during
  the batch, so this matters.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip '***'; markers
  {v}/{d}/{g}/{p} are stripped for parity (check_structure body_lines).
- **scripts/resegment_ch04.py ... resegment_ch07.py**: the model. When the OCR is
  too caption-corrupted to serve as a scaffold, rebuild data/zh/chNN.txt from a
  HARDCODED, hand-verified ('h'|'b', text) item list read off the scan. Model
  resegment_ch08.py on resegment_ch07.py.
- **scripts/verify_names.py --auto**: the dual-OCR disagreement filter; reads
  ONLY the spans the two configs disagree on. Follow with magnified PIL crops
  (PLAYWRIGHT-free, plain Pillow) for dense rosters and rare surnames.
- **data/noise.txt**: this book's number-check noise rules; extend it (longest-
  first, each commented with its value and the English phrase). B08 added the
  Arabic+万 grain/currency forms (140万, 60万, 4万, 1600万, 1000万, 800万, 600万,
  200万), place/name/idiom numerals (三交, 十字岭, 坂谷政三, 马汉三, 赵老五, 王八,
  万众), and ordinals/enumerators (第二年, 二是, 数十万, 20世纪80年代).
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args.
- **qc_entities.py is a VACUOUS PASS** on this project's flat glossary schema.
  Ensure entity survival BY HAND (consistency grep of the settled handles) during
  translation. Do not trust its "0 misses."
- **check_content.py / check_structure.py** need a --config with a `docs` map
  (whole-book tools); the per-unit contract is covered by verify_unit. Skip them
  per batch.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 189 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ
forever): Juntong; Zhongtong; the Eighth Route Army office / 八办; the Central
Social Affairs Department (中社部) / "the Social Affairs Department"; the Central
Intelligence Department (中情部); the Border Security (边保) = the full 陕甘宁边区
保安处 "Shaanxi-Gansu-Ningxia Border Region Security Office"; 保安处 standalone =
"the Security Office"; the Southern Bureau (南方局); the Special Branch (中央特科);
the dog-beating squad; the Military Commission's Second Bureau (军委二局); the
Shandong Column; No. 76; the Ume Kikan; the Iwai Kōkan; the Tokkō; the Kwantung
Army; Manchukuo.

Chapter 8 (延安反特第一案: Juntong's "expendable-agent" (死间) training class, the
line-casting and net-weaving, the great case, tracking the couriers, the
independent cell, and turning enemy agents to our use) will RE-USE HEAVILY:
Juntong, Zhongtong, the Border Security, the Social Affairs Department, Kang
Sheng, Xi Zhongxun, Hu Zongnan, the Guanzhong / Longdong sub-districts, Bu Lu,
Qin Ping, and the "化敌为我服务" policy line -- all already in the glossary. Watch
for: 死间 (the "dead/expendable agent", Sun Tzu's fifth spy-type -- likely a
footnote, cross-ref the 反间/离间 notes); 反间计 already noted ch07; 双重间谍 /
双料特务 = "double agent" (established ch07).

CONSISTENCY LEDGER points (do not re-decide):
- 锄奸 = "rooting out traitors" (specific sense; noted ch07); 锄奸部 = "the
  Anti-Traitor Department"; 锄奸委员会 = "the Anti-Traitor Committee".
- 反间计 = "the counter-espionage stratagem" (turning the enemy's spies, ch07);
  离间计 = "the Stratagem of Sowing Discord" (ch06) -- KEEP DISTINCT.
- 汉奸 = "traitor / collaborator"; 特务 = "special agent / secret service";
  敌探/日探 = "enemy scout / Japanese scout"; 国特 = "Nationalist agent(s)"
  (gloss "guote" once, ch07). Loaded terms, kept as the author uses them.
- 边区 = "the Border Region"; 关中分区 = "the Guanzhong sub-district"; 陇东分区 =
  "the Longdong sub-district"; 囊形地带 = "the pouch"; 宝葫芦 = "treasure gourd".
- 布鲁 = Bu Lu = 陈泊 (Chen Bo, "the Red Sherlock Holmes"); 杜理卿 = 许建国 (Xu
  Jianguo); 陈焕章 = 陈涛 (Chen Tao). 马锡武 (as printed) = the judge 马锡五 (Ma
  Xiwu, same romanization, noted ch07).
- 皖南事变 = "the New Fourth Army Incident" (ch03); 九一八 = "the Mukden Incident"
  (ch05); 西安事变 = "the Xi'an Incident"; 整风 = "the Rectification Movement";
  空城计 = "the Empty City Stratagem" (ch05); 三十六计 = "the Thirty-Six
  Stratagems"; 身在曹营心在汉 = the Guan Yu idiom (noted ch07).
- Anonymized-by-某 people STAY anonymized (何某, 张某, 田某, 樊某, 肖某, 李科长,
  李秘书 ...). Do NOT let a later session "resolve" them.
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file (confirmed ch01-ch07). The reading uses a single
  '## Chapter N. Title: Subtitle' h1 that folds the subtitle; the zh scaffold
  keeps two '### ' heading lines (chapter + subtitle) -- body-line parity is what
  check_structure compares, so the heading COUNT may differ by one and still pass.

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line PUNCH paragraphs (the 图文 OCR merges these -- split them back
  out), rhetorical questions kept sparingly, datebook chronology staccato, the
  inclusive "we." Runs HOT on the political set-pieces and SARDONIC on the enemy
  and on turncoats. Partisan by design; counter-record in the footnotes.
  Exclamations rationed hard (period by default); most rhetorical questions
  converted to statements; "so it turns out" reveal wrappers dropped. Em dashes
  used only as English punctuation demands; ch07 shipped 4.7/1k after trimming
  appositive-gloss dashes -- cap one per sentence or one matched pair, convert
  gloss-dashes to colons/commas. ch07 was a case-story chapter but still
  dialogue-light (documents/directives/reports dominate); Chapter 8 is a single
  extended case, likely the same, so contract the few conversational lines and
  keep documents/oaths formal.
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts;
  didactic-and-folksy. Keep the warmth and the edge. (ch07: stopped the Thunder
  God investigation, "peasants do not curse for no reason.")
- **Zhou Enlai:** measured, precise, terse when sharp; the talent-spotter.
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative,
  strategic, cold. 老蒋 = "old Chiang"; 蒋委员长 = "Generalissimo Chiang."
- **Kang Sheng ("Boss Kang" for 康老板):** sharp, doctrinaire, worried about
  political optics; menace under the reasonableness. Likely central again in
  Chapter 8 (the great Yan'an counter-espionage case, on the road to the "Rescue
  Campaign" of Chapter 9).
- **Bu Lu (陈泊, "the Red Sherlock Holmes"):** the forensic detective; loves
  material evidence, quibbles over terms, coins the "scouting / counter-scouting"
  ladder; patient, methodical (ch04, ch07). Likely central in Chapter 8.
- **Pan Hannian:** cool, daring, epigrammatic (ch05-ch06).
- **The Japanese brothers of conscience (ch06):** earnest, principled, unshowy.
- **Interviewees / memoirs / documents (Principal Sources register):** formal
  reminiscence, kept formal but never wooden.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the
Yan'an security state. Chapter 3 built the open Eighth Route Army offices and the
Chongqing/Xi'an webs. Chapter 4 ("拔钉子") pulled the Nationalist "nails" out of
the Border Region. Chapter 5 ("深入虎穴") turned to the offensive and closed on
the world race for Japan's intentions. Chapter 6 ("东方大谍") ran the Japanese
"state-policy school" front, Pan Hannian's penetration of the enemy's three
agencies, and the foreign brothers who aided unto death. Chapter 7 ("锄奸" /
"Rooting Out Traitors") is now COMPLETE: the whole defensive war of
counter-espionage -- the "double agent" who tried to kill Zhu De and Yang
Qiqing's shrewd re-labelling of him; the "good devil" Mizuhara Kiyoshi at
Da'anzhuang; the Party branch Zhang Luping built inside Juntong's Chongqing radio
HQ (martyred at the SACO prisons); Li Maotang's capture of Zhongtong's Shaanxi
apparatus by riding the CC-Clique feud; the doctrine of "pulling out" vs
"planting in" and "turn the enemy to serve us"; the double-agent cases in
Guanzhong; the "why doesn't the Thunder God strike Mao?" affair that produced
"crack troops and simple administration" and the Great Production Campaign; Bu
Lu's forensic cracking of the Longdong money-theft frame; and the 反间计
set-pieces (Xu Jishen framed to death, the Luochuan takeover, the "divergence of
wits"). It ends on the question that opens Chapter 8: can an agent's heart be
turned toward the Communists? Chapter 8 ("延安反特第一案" / "Yan'an's First Great
Counter-espionage Case") answers it with a single extended case built on "化敌为
我服务" ("turning the enemy to serve us").

## Open traps and environment

- **The 图文 OCR is UNUSABLE as a scaffold on plate/column-wrap pages.** Read
  every page image by eye, verify against both OCR configs, and rebuild data/zh
  via a hardcoded resegment_ch08.py. Resolve any faded leaf by magnified crop and
  by cross-reading later pages / the Principal Sources.
- **Section tails straddle pages AND one-line punch paragraphs hide on figure
  pages.** Read PAST each section heading and each plate. Use indents.py per-page
  first-line flag to settle each page-break seam.
- **assemble.py OVERWRITES data/zh/chNN.txt** -- run resegment AFTER assemble.
- **Number check is noisy.** Run via verify_unit (it passes --noise
  data/noise.txt); extend noise.txt for numerals inside names/places/idioms/
  titles (each commented); prefer REWORDING to carry a real number; carry REAL
  quantities as digits; noise Arabic+万 literals whose value you carry in English.
- **check_content / check_structure are per-batch N/A**; **qc_entities is
  vacuous** -- entity survival by hand.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; catalog them in PROGRESS as a deliberate decision. The standing
  question (every photo, or a curated subset) is still for the commissioner.
- **Source notes are PER-CHAPTER** (参考资料 / 主要资料). Chapter 8's fall at the
  end of section 6; render as a translated "### Principal Sources" section.
- **Printed-page markers**: ch04-ch07 carry folio markers (their resegment
  rebuilds the pagemap). ch03 has NONE (a clean rebuild is a corrections-pass
  task). ch01 zh parity 269/299 (from B01) also still open. No note cites a ch03
  folio.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B08 completion
reply in chat, as CLAUDE.md requires.
