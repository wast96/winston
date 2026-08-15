# HANDOFF -- China's Secret War (中国秘密战)

B07 (Chapter 6, the whole chapter, plus Chapter 6's Principal Sources) is
translated, built, and QA-clean. Chapter 6 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B08 (Chapter 7,
the whole chapter). Chapter 6 ("东方大谍" / "The Great Spies of the East") closed
the world race for Japan's intentions; Chapter 7 ("锄奸" / "Rooting Out Traitors")
turns inward, to the intricate war of counter-espionage.

## Message to paste into the next chat

```
China's Secret War B08

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B08 = Chapter 7 (第七章 锄奸 / "Rooting Out Traitors"), the whole chapter,
ch07s01-ch07s06, end to end per the CLAUDE.md pipeline. PDF pages 256-281;
printed pages 220-245 (offset constant: printed = pdf - 36; spot-verify each
section opener's folio off the scan). Section openers: s1 行刺总司令的"双料特务"
(The "Double Agent" Who Tried to Kill the Commander-in-Chief) PDF 256 / printed
220; s2 大安庄来了个"好鬼子" (A "Good Devil" Comes to Da'anzhuang) PDF 260 /
printed 224; s3 军统总台有个"党支部" (A "Party Branch" Inside Juntong's Main
Station) PDF 262 / printed 226; s4 关中有个"双重间谍" (A "Double Agent" in
Guanzhong) PDF 268 / printed 232; s5 "雷公咋不打毛泽东？" ("Why Doesn't the
Thunder God Strike Mao Zedong?") PDF 274 / printed 238; s6 反间计 (The
Counter-espionage Stratagem) PDF 277 / printed 241. Chapter 8 opens at PDF 282 /
printed 246, which is your stop. Chapter 7 carries its OWN chapter-end Principal
Sources (参考资料 / 主要资料); render it as a translated "### Principal Sources"
section, same treatment as ch01-ch06. Simplified Chinese, horizontal; chi_sim,
psm 6; PaddleOCR absent, use scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 256 281 --dpi 300 -> ocr_crop 256 281 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 256 281 ->
indents 256 281 -> add the chapter title, subtitle, and section 1-6 heading
strings (as the OCR reads them) to data/structure.json -> assemble ch07 256 281
--offset 36 --blank-assist -> find_figures (the 图文版 has many inline photos;
figures remain DEFERRED, see below) -> translate to out/ch07_reading.md, one
paragraph per TRUE source paragraph.

METHOD (proven B04-B07): read every page image (data/png/pNNNN.png) by eye,
transcribe each TRUE source paragraph, verify against BOTH OCR configs, and write
scripts/resegment_ch07.py that HARDCODES the verified ('h'|'b', text) item list
and rebuilds data/zh/ch07.txt wholesale (model: scripts/resegment_ch06.py /
resegment_ch05.py). NOTE from B06-B07: this book's STRAIGHT text pages OCR
cleanly, so assemble.py is a useful independent paragraph-BOUNDARY cross-check
(compare its body count to your resegment count) -- but the plate and column-wrap
pages STILL merge four-to-eight true paragraphs and inject photo-caption and
vertical-running-title bleed, AND faded leaves (B07 had one, pdf 251) return
near-garbage from both OCR configs, so the hand-verified resegment stays
authoritative. Keep assemble in the pipeline for the pagemap/heading check.
Any one-line PUNCH paragraph and any verse ({p}) is its own line/pair; verse
lines are emitted one {p} per source line (see the ch06 poem on pdf 253).

Then: make_bilingual ch07 -> verify_unit ch07 (parity + numbers + anchors; it
passes --noise data/noise.txt itself, do NOT add flags) -> check_align ch07 ->
qc_entities on out/ch07_bilingual.md (vacuous on the flat glossary -- ensure
entity survival BY HAND; verify EVERY quantity against the SCAN). Number check is
noisy: numerals inside names/places/idioms/titles go in data/noise.txt (literal
phrase, longest-first, each commented with its value and the English phrase); a
mixed Arabic+万 form (e.g. 3万) the reader can't combine, so if the value is
carried in English, noise the literal form (see 3万, 20万); a REAL dropped
quantity is fixed in the English, never noised. Prefer REWORDING to carry a
number (both/two/three-nation) over noising it. Then apparatus_merge for
notes+glossary -> check_apparatus (0 failures; the ~19 attestation-note warnings
on old rows are pre-existing, not yours) -> build_reading_epub -> qa_epub (green)
and epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar
out/chinas_secret_war.epub; clean) -> check_register --ref out/ch01_reading.md
out/ch07_reading.md (ch01 is the FROZEN reference; the dialogue metric is noise
in low-dialogue units, but Chapter 7 is a case-story chapter with real dialogue
-- CONTRACT the genuine conversational speech, leave documents/telegrams/oaths
formal) -> write PROGRESS and the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of Chapter 6
(out/ch06_reading.md, section 8's close: Nakanishi and Zheng Wendao, the verse,
the Laozi asterism, the "情报领先" question) for the voice; consult the VOICE
SHEETS and glossary in this HANDOFF. Cite the book's PRINTED folios in notes,
never PDF pages. Never invent bridging text: if OCR cuts off or a leaf is faded,
crop the scan and read the real continuation (B07's pdf 251 was resolved by
magnified crops, and one linchpin name 刘钊 by cross-reading pdf 252/255). Verify
every name, number, and unit designation by crop before writing; render
load-bearing figures and unit designations in DIGITS per STYLE. State
corroborated / uncorroborated / contradicted in notes; the partisan voice is
content, the counter-record goes in the footnote (fact-check hard against
Wikipedia/Baidu/academic, never Grok or any AI reference).

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
- **B07 = Chapter 6, the whole chapter + Principal Sources.** 341 English body
  paragraphs (1:1 parity). +12 notes (book total 134); +29 glossary rows (151
  total). qa_epub PASS; epubcheck 0/0/0/0; register within tolerance. **Chapter 6
  is COMPLETE.** See PROGRESS "Batch B07."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6. Do NOT re-measure.
- **scripts/assemble.py**: --blank-assist. On this book the straight text pages
  OCR cleanly, so assemble is a good paragraph-BOUNDARY cross-check; the plate/
  wrap/faded pages still merge and must be hand-verified. NOTE: assemble
  OVERWRITES data/zh/chNN.txt, so re-run resegment_chNN.py AFTER assemble.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; sec_nav
  omits a pending section from the nav of a PARTIALLY translated chapter
  (epubcheck NAV-011 fix). Chapter 7 will again be partially translated during the
  batch, so this matters. Verse ({p}) renders one italic line per source line.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip '***'; markers
  {v}/{d}/{g}/{p} are stripped for parity (check_structure body_lines).
- **scripts/resegment_ch04.py, resegment_ch05.py, resegment_ch06.py**: the model.
  When the OCR is too caption-corrupted or faded to serve as a scaffold, rebuild
  data/zh/chNN.txt from a HARDCODED, hand-verified ('h'|'b', text) item list read
  off the scan. Model resegment_ch07.py on these.
- **data/noise.txt**: this book's number-check noise rules; extend it (longest-
  first, each commented with its value and the English phrase). B07 added 石田七郎,
  郑百千, 岩桥竹二 (names), 3万 (=30,000, Arabic+万 not combinable, carried in
  English), 622 (the June-22 label), 第二天 (the next day).
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args.
- **qc_entities.py is a VACUOUS PASS** on this project's flat glossary schema.
  Ensure entity survival BY HAND (consistency grep of the settled handles) during
  translation. Do not trust its "0 misses."
- **check_structure.py** needs a --config with a `docs` map (whole-book heading/
  drift tool); the per-unit contract is covered by verify_unit. Skip it per batch.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 151 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ
forever): the Eighth Route Army office / 八办; the Social Affairs Department
(中社部); the Central Intelligence Department (中情部); the Central Investigation
and Study Bureau; the Border Security (边保); the Southern Bureau (南方局);
Juntong; Zhongtong; the Special Branch (中央特科); the South China Intelligence
Bureau. Enemy/foreign organs settled and reused: No. 76 (76号); the Ume Kikan
(梅机关); the Iwai Kōkan (岩井公馆, en field now corrected to the macron form);
the Tokkō (特高课); Manchukuo (满洲国); the National Defense Line; the dog-beating
squad; the South Manchuria Railway (满铁); the Kwantung Army; the Kōa-in (兴亚院);
the Kwantung Army Special Maneuvers / Kantokuen (关特演); Operation Kiri (桐工作).

Chapter 7 (锄奸 / counter-espionage: the "double agents," the "good devil" at
Da'anzhuang, the Party branch inside Juntong's main radio station, the Guanzhong
double agent, "why doesn't the Thunder God strike Mao," the 反间计) will RE-USE
HEAVILY: Juntong, Zhongtong, No. 76, the dog-beating squad, Kang Sheng, the
Guanzhong sub-district (关中分区), Xi Zhongxun (习仲勋), the锄奸 committee
(锄奸委员会), Bu Lu / Chen Bo -- all already in the glossary. 锄奸 = "rooting out
traitors" / counter-espionage (keep the specific sense; noted early). 反间计 =
the counter-espionage stratagem (turning the enemy's spies), distinct from 离间计
(sowing discord, noted ch06). "双料特务" / "双重间谍" = "double agent."

CONSISTENCY LEDGER points (do not re-decide):
- 中西功 = Nakanishi Kō; 尾崎秀实 = Ozaki Hotsumi; 尾崎庄太郎 = Ozaki Shōtarō (a
  DIFFERENT man from Hotsumi -- keep distinct); 郑文道 = Zheng Wendao; 方知达 =
  张明达 = Fang Zhida / Zhang Mingda (one man); 钱明 = 景若南 = Qian Ming (one man);
  刘钊 = Liu Zhao.
- 杜理卿 (Du Liqing) = 许建国 (Xu Jianguo) one man. 陈焕章 = 陈涛 (Chen Tao) one man.
  陈泊 = 布鲁 (Bu Lu, "the Red Sherlock Holmes"). 俞鸣九 = 肖炳实 = 肖项平 one man.
- 关中分区 = "Guanzhong sub-district"; 军分区 = "military sub-district"; 边区 =
  "Border Region"; 囊形地带 = "the pouch"; 宝葫芦 = "treasure gourd."
- 磨擦 = "friction" (ch04); 双重政权 = "dual regime" (ch04); 皖南事变 = "the New
  Fourth Army Incident" (noted ch03); 九一八 = "the Mukden Incident" (noted ch05);
  空城计 = "the Empty City Stratagem" (noted ch05); 离间计 = "the Stratagem of
  Sowing Discord" (ch06); 三十六计 = "the Thirty-Six Stratagems."
- The Barbarossa / Pearl Harbor / Moscow-defense credit claims are CONTESTED:
  keep the even-handed footnote posture (transfer/warnings real; the CCP-decisive
  attribution uncorroborated; Sorge/SIGINT usually credited). Chi Buzhou's Pearl
  Harbor decrypt claim is UNCORROBORATED (Chinese-origin).
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file (confirmed ch01-ch06).

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line PUNCH paragraphs (the 图文 OCR merges these -- split them back
  out), rhetorical questions kept sparingly, datebook chronology staccato, the
  inclusive "we." Runs HOT in the political set-pieces and SARDONIC on the enemy
  and on turncoats. Partisan by design; counter-record in the footnotes.
  Exclamations rationed hard (period by default); most rhetorical questions
  converted to statements; "so it turns out" reveal wrappers dropped. Em dashes
  used only as English punctuation demands (ch06 shipped 4.5/1k after trimming
  appositive-gloss dashes; watch pile-ups, cap one per sentence or one matched
  pair). ch06 was low-dialogue and document-heavy; Chapter 7 is a CASE-STORY
  chapter, so it will carry more real dialogue -- contract the conversational
  speech, keep documents/oaths formal.
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts;
  didactic-and-folksy. Keep the warmth and the edge.
- **Zhou Enlai:** measured, precise, terse when sharp; a man of feeling and honor;
  the talent-spotter who binds agents by a word of honor.
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative, strategic,
  cold. 老蒋 = "old Chiang"; 蒋委员长 = "Generalissimo Chiang." His diary voice
  (ch06) is clipped and contemptuous.
- **Kang Sheng ("Boss Kang" for 康老板):** sharp, doctrinaire, worried about
  political optics; menace under the reasonableness. Central again in Chapter 7.
- **Pan Hannian:** the master intelligencer of the Shanghai/Hong Kong theatre;
  cool, daring, epigrammatic. Central in ch05-ch06.
- **Nakanishi Kō / Ozaki Hotsumi / the Japanese brothers (ch06):** high
  intellectuals of conscience; earnest, principled, unshowy. Nakanishi speaks
  plainly and warmly of China; the parting-charge and Zheng Wendao's reply are
  contracted, heartfelt speech.
- **Interviewees / memoirs / documents (Principal Sources register):** formal
  reminiscence, kept formal but never wooden.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the
Yan'an security state. Chapter 3 built the open Eighth Route Army offices and the
Chongqing/Xi'an webs. Chapter 4 ("拔钉子") pulled the Nationalist "nails" out of
the Border Region. Chapter 5 ("深入虎穴") turned to the offensive and closed on the
world race for Japan's intentions. Chapter 6 ("东方大谍" / "The Great Spies of the
East") is now COMPLETE: the Japanese "state-policy school" front and the Communist
organization inside it; the agency-within-the-agency (the Ume Kikan, the Iwai
Kōkan, No. 76) and Pan Hannian's penetration of all three; Yan'an's Japanese
Workers' and Peasants' School; the deft离间计 that broke Operation Kiri; the road
from "Barbarossa" to the "Kwantung Army Special Maneuvers," and Nakanishi Kō's
reckoning of the Pearl Harbor date; the supreme-commander responsibility set-piece
(Stalin, Roosevelt, Chiang all misjudged; Mao the true intelligence master); and
the foreign brothers who aided unto death (Nakanishi Kō and the suicide of Zheng
Wendao). Chapter 7 ("锄奸" / "Rooting Out Traitors") turns to counter-espionage:
the double agents, the "good devil," the Party branch inside Juntong's radio
station, the Guanzhong double agent, the Thunder-God case, and the 反间计.

## Open traps and environment

- **The 图文 OCR is UNUSABLE as a scaffold on plate/column-wrap/faded pages.** Read
  every page image by eye, verify against both OCR configs, and rebuild data/zh via
  a hardcoded resegment_ch07.py. Faded leaves (B07 pdf 251) yield near-garbage;
  resolve by magnified crop and by cross-reading later pages (a name illegible in
  one place is often spelled out in the Principal Sources).
- **Section tails straddle pages AND one-line punch paragraphs hide on figure
  pages.** Read PAST each section heading and each plate.
- **assemble.py OVERWRITES data/zh/chNN.txt** -- run resegment AFTER assemble.
- **Number check is noisy.** Run via verify_unit (it passes --noise data/noise.txt);
  extend noise.txt for numerals inside names/places/idioms/titles (each commented);
  prefer REWORDING to carry a real number; carry REAL quantities as digits.
- **check_content is N/A**; **qc_entities is vacuous** -- entity survival by hand.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; catalog them in PROGRESS as a deliberate decision. The standing question
  (every photo, or a curated subset) is still for the commissioner.
- **Source notes are PER-CHAPTER** (参考资料 / 主要资料). Chapter 7's fall at the
  end of section 6; render as a translated "### Principal Sources" section.
- **Printed-page markers**: ch04, ch05, ch06 carry folio markers (their resegment
  rebuilds the pagemap). ch03 has NONE (a clean rebuild is a corrections-pass
  task). ch01 zh parity 269/299 (from B01) also still open. No note cites a ch03
  folio.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B07 completion
reply in chat, as CLAUDE.md requires.
