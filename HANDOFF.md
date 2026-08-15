# HANDOFF -- China's Secret War (中国秘密战)

B06 (Chapter 5, the whole chapter, plus Chapter 5's Principal Sources) is
translated, built, and QA-clean. Chapter 5 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B07 (Chapter 6,
the whole chapter). Chapter 6 picks up exactly where Chapter 5 ends -- the world
race for the strategic intelligence of Japan's intentions.

## Message to paste into the next chat

```
China's Secret War B07

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B07 = Chapter 6 (第六章 东方大谍 / "The Great Spies of the East"), the whole
chapter, ch06s01-ch06s08, end to end per the CLAUDE.md pipeline. PDF pages
223-255; printed pages 187-219 (offset constant: printed = pdf - 36; spot-verify
each section opener's folio off the scan). Section openers: s1 上海滩有个日本"国策
学校" (A Japanese "State-Policy School" on the Shanghai Bund) PDF 223 / printed
187; s2 "机关"中的机关 (The Agency Within the "Agency") PDF 227 / printed 191;
s3 延安也有个日本学校 (Yan'an Had a Japanese School Too) PDF 231 / printed 195;
s4 巧施离间计 (A Deft Stratagem to Sow Discord) PDF 234 / printed 198; s5 从"巴巴
罗萨"到"关特演" (From "Barbarossa" to the "Kwantung Army Special Maneuvers") PDF
236 / printed 200; s6 绝密情报深藏虎穴 (Top-Secret Intelligence Hidden Deep in the
Tiger's Den) PDF 240 / printed 204; s7 最高统帅的最高责任 (The Supreme Commander's
Supreme Responsibility) PDF 243 / printed 207; s8 异国兄弟，生死相助 (Brothers from
Foreign Lands, Aiding Unto Death) PDF 250 / printed 214. Chapter 7 opens at PDF
256 / printed 220, which is your stop. Chapter 6 carries its OWN chapter-end
Principal Sources (主要资料); render it as a translated "### Principal Sources"
section, same treatment as ch01-ch05. Simplified Chinese, horizontal; chi_sim,
psm 6; PaddleOCR absent, use scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 223 255 --dpi 300 -> ocr_crop 223 255 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 223 255 ->
indents 223 255 -> add the chapter title, subtitle, and section 1-8 heading
strings (as the OCR reads them) to data/structure.json -> assemble ch06 223 255
--offset 36 --blank-assist -> find_figures (the 图文版 has many inline photos;
figures remain DEFERRED, see below) -> translate to out/ch06_reading.md, one
paragraph per TRUE source paragraph.

METHOD (proven B05-B06): read every page image (data/png/pNNNN.png) by eye,
transcribe each TRUE source paragraph, verify against BOTH OCR configs, and write
scripts/resegment_ch06.py that HARDCODES the verified ('h'|'b', text) item list
and rebuilds data/zh/ch06.txt wholesale (model: scripts/resegment_ch05.py /
resegment_ch04.py, NOT the merge/split bridge of resegment_ch03.py). NOTE from
B06: this book's STRAIGHT text pages now OCR cleanly, so assemble.py is a useful
independent paragraph-BOUNDARY cross-check (compare its body count to your
resegment count) -- but the plate and column-wrap pages STILL merge four-to-eight
true paragraphs and inject photo-caption and vertical-running-title bleed, so the
hand-verified resegment stays authoritative. Keep assemble in the pipeline for
the pagemap/heading sanity check.

Then: make_bilingual ch06 -> verify_unit ch06 (parity + numbers + anchors; it
passes --noise data/noise.txt itself, do NOT add flags) -> check_align ch06 ->
qc_entities on out/ch06_bilingual.md (vacuous on the flat glossary -- ensure
entity survival BY HAND; verify EVERY quantity against the SCAN). Number check is
noisy: numerals inside names/places/idioms/titles go in data/noise.txt (literal
phrase, longest-first, each commented with its value and the English phrase; if a
name ending in a numeral precedes an idiom, noise the NAME too so the idiom rule's
lookbehind can fire -- see 岩井英一 before 千方百计 in B06); a REAL dropped quantity
is fixed in the English, never noised. Then apparatus_merge for notes+glossary ->
check_apparatus (0 failures; pre-existing attestation-note warnings are not yours)
-> build_reading_epub -> qa_epub (green) and epubcheck (java -jar
/tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub; clean) ->
check_register --ref out/ch01_reading.md out/ch06_reading.md (ch01 is the FROZEN
reference; dialogue metric is noise in low-dialogue units, judge on the
narratorial signals) -> write PROGRESS and the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of Chapter 5
(out/ch05_reading.md, section 8's close: the Sun Tzu / Cao Cao passages and the
"super-spy" cliffhanger that Chapter 6 answers) for the voice; consult the VOICE
SHEETS and glossary in this HANDOFF. Cite the book's PRINTED folios in notes,
never PDF pages. Never invent bridging text: if OCR cuts off, crop the scan and
read the real continuation. WATCH THE SECTION TAILS: a section's last paragraphs
often straddle onto the NEXT section's opening page before the heading, and the
图文 pages hide one-line PUNCH paragraphs that the OCR merges -- read past each
heading and each plate. Verify every name, number, and unit designation by crop
before writing (B06 caught 上万裕 mis-OCR'd 王万裕, 单不移 as 单不和, and the
referent-correct 蹇先佛 where the print/OCR was ambiguous). Render load-bearing
figures and unit designations in DIGITS per STYLE. State corroborated /
uncorroborated / contradicted in notes; the partisan voice is content, the
counter-record goes in the footnote (in B06 the "who warned Stalin" claim got a
CONTESTED note; Chapter 6, the Sorge ring / Barbarossa / 关特演 material, will
need the same honesty -- the Sorge story is heavily documented in Western and
Japanese scholarship, so fact-check hard, prefer Wikipedia/Baidu/academic, never
source Grok or any AI-written reference).

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
- **B03 = Chapter 2, sections 6-8 + Chapter 2 Principal Sources.** Chapter 2
  COMPLETE.
- **B04 = Chapter 3, the whole chapter + Principal Sources.** Chapter 3 COMPLETE.
- **B05 = Chapter 4, the whole chapter + Principal Sources.** Chapter 4 COMPLETE.
- **B06 = Chapter 5, the whole chapter + Principal Sources.** 330 English body
  paragraphs (1:1 parity). +24 notes (book total 122); +22 glossary rows (123
  total). qa_epub PASS; epubcheck 0/0/0/0. **Chapter 5 is COMPLETE.** See PROGRESS
  "Batch B06."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6. Do NOT re-measure.
- **scripts/assemble.py**: --blank-assist. On this book the straight text pages
  OCR cleanly, so assemble is a good paragraph-BOUNDARY cross-check; the plate/
  wrap pages still merge and must be hand-verified.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; sec_nav
  omits a pending section from the nav of a PARTIALLY translated chapter
  (epubcheck NAV-011 fix). Chapter 6 will again be partially translated during the
  batch, so this matters.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip the '***'
  scene-break marker.
- **scripts/resegment_ch04.py, resegment_ch05.py**: the model. When the OCR is too
  caption-corrupted to serve as a scaffold, rebuild data/zh/chNN.txt from a
  HARDCODED, hand-verified ('h'|'b', text) item list read off the scan. Model
  resegment_ch06.py on these (NOT on resegment_ch03.py). The earlier
  resegment_ch02/ch02b03/ch03 are the merge/split-on-garbled-anchor variants.
- **data/noise.txt**: this book's number-check noise rules; extend it (longest-
  first, each commented with its value and the English phrase). If a name ending
  in a numeral abuts an idiom, noise the NAME too so the idiom rule's auto-guard
  lookbehind can fire (see 岩井英一 immediately before 千方百计).
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args.
- **qc_entities.py is a VACUOUS PASS** on this project's flat glossary schema.
  Ensure entity survival BY HAND during translation. Do not trust its "0 misses."
- **check_structure.py** needs a --config with a `docs` map (whole-book heading/
  drift tool); the per-unit contract is covered by verify_unit. Skip it per batch.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 123 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ
forever): the Eighth Route Army office / 八办; the Social Affairs Department
(中社部); the Central Intelligence Department (中情部) / Central Investigation and
Study Bureau; the Border Security (边保); the Southern Bureau (南方局); Juntong;
Zhongtong; the Special Branch (中央特科); the South China Intelligence Bureau
(华南情报局). Enemy/foreign organs now settled and reused: No. 76 (76号); the Ume
Kikan (梅机关); the Iwai Kōkan (岩井公馆); the Tokkō (特高课); Manchukuo (满洲国);
the National Defense Line (国防线); the dog-beating squad (打狗队). Chapter 6 (the
Sorge ring, the Japanese "state-policy school" front on the Shanghai Bund, the
Yan'an Japanese-workers school, the离间计, "Barbarossa"→"关特演", the foreign
brothers) will re-use HEAVILY: Sorge, Pan Hannian, Iwai Eiichi, the Ume Kikan /
No. 76, Yuan Shu, Yan Baohang, Manchukuo, and Kagesa Sadaaki -- all now in the
glossary.

CONSISTENCY LEDGER points (do not re-decide):
- 杜理卿 (Du Liqing) = 许建国 (Xu Jianguo) are ONE man. 陈焕章 = 陈涛 (Chen Tao) one
  man. 陈泊 = 布鲁 (Bu Lu, "the Red Sherlock Holmes"). 俞鸣九 = 肖炳实 = 肖项平 one
  man (the Lanzhou/Sorge-linked cadre).
- 关中分区 = "Guanzhong sub-district" (分区 = sub-district, 军分区 = "military
  sub-district", 边区 = "Border Region"); 囊形地带 = "the pouch" (Hu Zongnan's term)
  / 宝葫芦 = "treasure gourd" (the popular name).
- 磨擦 = "friction" (noted ch04); 双重政权 = "dual regime" (noted ch04); 皖南事变 =
  "the New Fourth Army Incident" (noted ch03, do NOT re-note); 九一八 = "the Mukden
  Incident" (noted ch05); 空城计 = "the Empty City Stratagem" (noted ch05).
- The "who warned Stalin"/Barbarossa material is CONTESTED: Yan Baohang's warning
  and his 1995 Russian decoration are corroborated; the decisive-effect claim is
  not. Chapter 6 revisits Barbarossa (从"巴巴罗萨"到"关特演") -- keep the same
  even-handed footnote posture; the Sorge ring is well documented, fact-check it.
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file (confirmed ch01-ch05).
- Sun Tzu's Art of War "Use of Spies" and Cao Cao's "周公吐哺，天下归心" both noted
  in ch05; if they recur, cross-reference, do not re-note.

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line PUNCH paragraphs (the 图文 OCR merges these -- split them back
  out), rhetorical questions kept sparingly (only where they land in English),
  datebook chronology staccato, the inclusive "we." Runs HOT in the political
  set-pieces and SARDONIC on the enemy and on turncoats-become-officials. Partisan
  by design; counter-record in the footnotes. Exclamations rationed hard (period
  by default); most rhetorical questions converted to statements; "so it turns
  out" reveal wrappers dropped. Em dashes used only as English punctuation demands
  (ch05 shipped 4.3/1k, within tolerance of ch01's 3.4). Chapter 5 ends on a
  super-spy cliffhanger the Sun Tzu / Cao Cao passages set up; Chapter 6 answers
  "who wins the Japan-intentions prize" -- keep that competitive momentum.
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts;
  didactic-and-folksy in the ch05 "investigation and study" set piece. Keep the
  warmth and the edge.
- **Zhou Enlai:** measured, precise, terse when sharp; a man of "feeling and
  honor." In ch05 the talent-spotter who binds agents by a word of honor.
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative,
  strategic, cold. 老蒋 = "old Chiang"; 蒋委员长 = "Generalissimo Chiang."
- **Kang Sheng ("Boss Kang" for 康老板):** sharp, doctrinaire, worried about
  political optics; menace under the reasonableness.
- **Pan Hannian:** the master intelligencer of the Shanghai/Hong Kong theatre;
  cool, daring, epigrammatic ("to give up one's life is not the hard thing; harder
  is to destroy one's own good name"). Central in Chapter 6.
- **Interviewees / memoirs / documents (Principal Sources register):** formal
  reminiscence, kept formal but never wooden.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the
Yan'an security state. Chapter 3 built the open Eighth Route Army offices and the
Chongqing/Xi'an webs. Chapter 4 ("拔钉子") pulled the Nationalist "nails" out of
the Border Region. Chapter 5 ("深入虎穴" / "Into the Tiger's Den") is now COMPLETE:
CCP intelligence turning to the offensive -- the "Great Darkness in the East" and
Mao's open-stratagem exposure of the surrender talks; the Soviet-trained agents
and the Lanzhou/Yan'an Soviet groups; the warning to Stalin of the German invasion
(Yan Baohang); Mao's "investigation and study" method and the 1941 creation of the
Central Intelligence Department; the offensive nets at Yan'an, Xi'an (Xiong
Xianghui inside Hu Zongnan), and the front (Chen Geng and the Linfen/Hanlüe
coups, the Jin-Cha-Ji and Northeast nets breaking the "National Defense Line");
and Pan Hannian's penetration of No. 76, the Ume Kikan, and the Iwai Kōkan, closing
on the world race for Japan's intentions. Chapter 6 ("东方大谍" / "The Great Spies
of the East") takes up that race: the Japanese "state-policy school" front, the
agency within the agency, Yan'an's own Japanese school, the离间计, the road from
"Barbarossa" to the "Kwantung Army Special Maneuvers," and the foreign brothers who
aided unto death.

## Open traps and environment

- **The 图文 OCR is UNUSABLE as a scaffold on plate/column-wrap pages.** Read every
  page image by eye, verify against both OCR configs, and rebuild data/zh via a
  hardcoded resegment_ch06.py (model: resegment_ch05.py). The straight text pages
  DO OCR cleanly now -- use assemble's body count as a boundary cross-check, but
  the resegment (which WRITES the file wholesale) is authoritative.
- **Section tails straddle pages AND one-line punch paragraphs hide on figure
  pages.** Read PAST each section heading and each plate.
- **Number check is noisy.** Run via verify_unit (it passes --noise data/noise.txt);
  extend noise.txt for numerals inside names/places/idioms/titles/decades (each
  commented); carry REAL quantities in the English as digits, never noise them.
- **check_content is N/A**; **qc_entities is vacuous** -- entity survival by hand.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; catalog them in PROGRESS as a deliberate decision. The standing question
  (every photo, or a curated subset) is still for the commissioner.
- **Source notes are PER-CHAPTER** (主要资料). Chapter 6's fall at the end of
  section 8; render as a translated "Principal Sources" section.
- **Printed-page markers**: ch04 and ch05 carry folio markers (their resegment
  rebuilds the pagemap). ch03 has NONE (stale post-resegment indices; a clean
  rebuild is a corrections-pass task). ch01 zh parity 269/299 (from B01) also still
  open. No note cites a ch03 folio.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B06 completion
reply in chat, as CLAUDE.md requires.
