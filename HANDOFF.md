# HANDOFF -- China's Secret War (中国秘密战)

B09 (Chapter 8, the whole chapter, plus Chapter 8's Principal Sources) is
translated, built, and QA-clean. Chapter 8 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B10 (Chapter 9,
the whole chapter). Chapter 8 ("延安反特第一案") answered whether an agent's heart
can be turned, with the great Hanzhong "expendable-agent" case and the winning
policy of "化敌为我服务"; it ends by tying that case to the Rescue Campaign.
Chapter 9 ("抢救运动" / "The Rescue Campaign") is the turn: how the hunt for
agents, riding the Rectification, broadened into a purge that swept up the
innocent -- the book's most contested episode, ending in Mao's apology.

## Message to paste into the next chat

```
China's Secret War B10

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B10 = Chapter 9 (第九章 "抢救运动" / "The Rescue Campaign"), the whole
chapter, ch09s01-ch09s08, end to end per the CLAUDE.md pipeline. PDF pages
305-342; printed pages 269-306 (offset constant: printed = pdf - 36; spot-verify
each section opener's folio off the scan). Section openers: s1 "侦破"与"运动"同步
("Case-Cracking" in Step with the "Campaign") PDF 305 / printed 269; s2 从"老号疑犯"
到"山东肃托" (From the "Old-Case Suspects" to the "Shandong Anti-Trotskyist Purge")
PDF 309 / printed 273; s3 "四大特务"和"红旗党" (The "Four Great Agents" and the
"Red-Flag Party") PDF 312 / printed 276; s4 "外来知识分子"中"特务如麻"？(Were the
"Outside Intellectuals" "Riddled with Agents"?) PDF 317 / printed 281; s5
"群众运动"加"逼、供、信" ("Mass Campaigns" Plus "Coerce, Confess, Believe") PDF 319 /
printed 283; s6 毛泽东道歉 (Mao Zedong Apologizes) PDF 324 / printed 288; s7
《刘巧儿告状》 ("Liu Qiao'er Brings Suit") PDF 331 / printed 295; s8 到前线去自己
做结论！(Go to the Front and Draw Your Own Conclusions!) PDF 335 / printed 299.
Chapter 10 opens at PDF 343 / printed 307, which is your stop. Chapter 9 carries
its OWN chapter-end Principal Sources (参考资料 / 主要资料); render it as a
translated "### Principal Sources" section, same treatment as ch01-ch08.
Simplified Chinese, horizontal; chi_sim, psm 6; PaddleOCR absent, use
scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 305 342 --dpi 300 -> ocr_crop 305 342 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 305 342 ->
indents 305 342 -> add the chapter title, subtitle, and section 1-8 heading
strings (as the OCR reads them) to data/structure.json -> assemble ch09 305 342
--offset 36 --blank-assist -> find_figures (the 图文版 has many inline photos;
figures remain DEFERRED, see below) -> translate to out/ch09_reading.md, one
paragraph per TRUE source paragraph.

METHOD (proven B04-B09): read every page image (data/png/pNNNN.png) by eye,
transcribe each TRUE source paragraph, verify against BOTH OCR configs, and write
scripts/resegment_ch09.py that HARDCODES the verified ('h'|'b', text) item list
and rebuilds data/zh/ch09.txt wholesale (model: scripts/resegment_ch08.py /
resegment_ch07.py). NOTE from B06-B09: this book's STRAIGHT text pages OCR
cleanly, so assemble.py is a useful independent paragraph-BOUNDARY cross-check
(compare its body count to your resegment count; on ch08 assemble read 160 vs the
182 hand count, the +22 being the many one-line PUNCH paragraphs assemble merges
plus the short Principal-Sources entries) -- but the plate and column-wrap pages
STILL merge four-to-eight true paragraphs and inject photo-caption and vertical-
running-title bleed, so the hand-verified resegment stays authoritative. Keep
assemble in the pipeline for the pagemap/heading check. Use indents.py to settle
every page-break seam: a page top whose first line is INDENTED starts a NEW
paragraph, a non-indented top CONTINUES the previous page's last paragraph. Any
one-line PUNCH paragraph is its own line/pair.

Then: make_bilingual ch09 -> verify_unit ch09 (parity + numbers + anchors; it
passes --noise data/noise.txt itself, do NOT add flags) -> check_align ch09 ->
qc_entities is vacuous on the flat glossary -- ensure entity survival BY HAND;
verify EVERY quantity against the SCAN. Number check is noisy: numerals inside
names/places/idioms/titles go in data/noise.txt (literal phrase, longest-first,
each commented with its value and the English phrase); a mixed Arabic+万 form the
reader can't combine, so if the value is carried in English, noise the literal
form; a REAL dropped quantity is fixed in the English, never noised. Prefer
REWORDING to carry a number, and carry English number WORDS (two/three/ten): the
check recognizes them. Then apparatus_merge for notes+glossary -> check_apparatus
(0 failures; the 19 attestation-note warnings on old rows are pre-existing, not
yours) -> build_reading_epub -> qa_epub (green) and epubcheck (java -jar
/tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub; clean) ->
check_register --ref out/ch01_reading.md out/ch09_reading.md (ch01 is the FROZEN
reference; the dialogue metric is noise in low-dialogue units, but Chapter 9 has
MORE quoted speech than ch07-ch08 -- the interrogations, Mao's speeches, Liu
Qiao'er -- so watch the contraction rate more here and CONTRACT genuine
conversational speech, leaving documents/directives/slogans formal). Watch the
em-dash rate: keep it near ch06-ch08 (~4.5/1k), convert appositive-gloss and
list dashes to colons/commas. Then write PROGRESS and the next HANDOFF/kickoff ->
commit.

BEFORE translating, read the final two English pages of Chapter 8
(out/ch08_reading.md, section 6's close: the "turncoat" who is the man neither
side will own, the counter-espionage that reaches into the 1960s, and the closing
lines where the case breeds the审干 phase and the "Rescue Campaign" -- which OPENS
Chapter 9) for the voice; consult the VOICE SHEETS and glossary in this HANDOFF.
Cite the book's PRINTED folios in notes, never PDF pages. Never invent bridging
text: if OCR cuts off or a leaf is faded, crop the scan and read the real
continuation. Verify every name, number, and unit designation by crop before
writing (use verify_names.py --auto for the dual-OCR disagreement filter, then
magnified PIL crops for the dense rosters); render load-bearing figures and unit
designations in DIGITS per STYLE. Keep anonymized-by-某 people anonymized.

CHAPTER 9 IS THE MOST CONTESTED CHAPTER SO FAR. It is the "Rescue Campaign"
(抢救运动): the purge excesses, 逼供信 ("coerce, confess, believe"), the
"agents as thick as hemp" hysteria, Kang Sheng's central role, and Mao's apology.
The interested-witness doctrine (STYLE) is CENTRAL here, not occasional: render
the author's partisan account faithfully in the TEXT (he is sympathetic to the
Party and treats its own excesses more gently than the enemy's), and put the
counter-record and the historians' verdict in the FOOTNOTES (corroborated /
partly / uncorroborated / contradicted), fact-checking HARD against
Wikipedia/Baidu/academic -- never Grok or any AI reference. Kang Sheng's role in
driving the campaign is the single most scrutinized fact; footnote it with the
scholarly verdict. 抢救运动/审干/整风/逼供信/一元化领导 are Party-campaign terms:
render the MEANING in plain English and gloss/footnote the term at first use.

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
- **B08 = Chapter 7 (锄奸) + Principal Sources.** Chapter 7 COMPLETE.
- **B09 = Chapter 8 (延安反特第一案) + Principal Sources.** 182 English body
  paragraphs (1:1 parity). +8 notes (book total 169); +20 glossary rows (209
  total). qa_epub PASS; epubcheck 0/0/0/0; register within tolerance; em-dash
  4.4/1k. **Chapter 8 is COMPLETE.** See PROGRESS "Batch B09."

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
  (epubcheck NAV-011 fix). Chapter 9 will again be partially translated during
  the batch, so this matters.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip '***'; markers
  {v}/{d}/{g}/{p} are stripped for parity (check_structure body_lines).
- **scripts/resegment_ch04.py ... resegment_ch08.py**: the model. When the OCR is
  too caption-corrupted to serve as a scaffold, rebuild data/zh/chNN.txt from a
  HARDCODED, hand-verified ('h'|'b', text) item list read off the scan. Model
  resegment_ch09.py on resegment_ch08.py.
- **scripts/verify_names.py --auto**: the dual-OCR disagreement filter; reads
  ONLY the spans the two configs disagree on. Follow with magnified PIL crops
  (plain Pillow, PLAYWRIGHT-free) for dense rosters and rare surnames.
- **data/noise.txt**: this book's number-check noise rules; extend it (longest-
  first, each commented with its value and the English phrase). B09 added: 祁三益
  (Qi Sanyi, name), 一江山岛 (Yijiangshan Island), 势不两立 (idiom), 五台 (Wutai).
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args.
- **qc_entities.py is a VACUOUS PASS** on this project's flat glossary schema.
  Ensure entity survival BY HAND (consistency grep of the settled handles).
- **check_content.py / check_structure.py** need a --config with a `docs` map
  (whole-book tools); the per-unit contract is covered by verify_unit. Skip them
  per batch.
- The number check recognizes English number WORDS (two, three, second, ten), not
  only digits: carry a count as a word in the prose rather than noising it, and
  reserve noise for numerals inside names/places/idioms.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 209 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ
forever): Juntong; Zhongtong; the Eighth Route Army office / 八办; the Central
Social Affairs Department (中社部) / "the Social Affairs Department"; the Central
Intelligence Department (中情部); the Border Security (边保) = the full 陕甘宁边区
保安处 "Shaanxi-Gansu-Ningxia Border Region Security Office"; 保安处 standalone =
"the Security Office"; the Southern Bureau (南方局); the Special Branch (中央特科);
the dog-beating squad; the Military Commission's Second Bureau (军委二局); the
Shandong Column; No. 76; the Ume Kikan; the Iwai Kōkan; the Tokkō; the Kwantung
Army; Manchukuo; the Hanzhong (training) class (汉训班); the "Dai case" (戴案);
the Northwest Special Reconnaissance Station (西北特侦站); 死间 "expendable agent";
海底 haidi; Kangda; Shaanbei College; SACO; Baigongguan.

Chapter 9 (抢救运动: the Rescue Campaign) will RE-USE HEAVILY: the Border Security,
the Social Affairs Department, Kang Sheng, Li Kenong, Mao Zedong, the Rectification
Movement (整风), 审干 (cadre-vetting), 化敌为我服务, 特务/国特/汉奸, and likely the
Hanzhong-class "confessors" who became "model" figures (they set up ch09). Watch
for NEW campaign terms: 抢救运动 "the Rescue Campaign"; 逼供信 "coerce, confess,
believe" (slogan, keep + gloss); 特务如麻 "agents as thick as hemp"; 红旗党
"Red-Flag Party"; 山东肃托 "Shandong anti-Trotskyist purge"; 一元化领导 "unified
leadership". Render the MEANING in plain English; gloss/footnote the term at first
use (STYLE rule 11). 刘巧儿告状 is the "Liu Qiao'er" opera (cross-ref 马青天/马锡五,
noted ch07).

CONSISTENCY LEDGER points (do not re-decide):
- 锄奸 = "rooting out traitors" (specific sense; noted ch07); 反间计 = "the
  counter-espionage stratagem" (ch07); 离间计 = "the Stratagem of Sowing Discord"
  (ch06) -- KEEP DISTINCT. 反用/逆用 = "counter-use" / "turning the use" (≈ Sun
  Tzu's 反间 "turned spy", ch08); 死间 = "expendable agent" (ch08).
- 汉奸 = "traitor / collaborator"; 特务 = "special agent / secret service";
  敌探/日探 = "enemy scout / Japanese scout"; 国特 = "Nationalist agent(s)".
  Loaded terms, kept as the author uses them; loaded-term note placed early.
- 边区 = "the Border Region"; 关中分区 = "the Guanzhong sub-district"; 陇东分区 =
  "the Longdong sub-district".
- 布鲁 = Bu Lu = 陈泊 (Chen Bo, "the Red Sherlock Holmes"); 杜理卿 = 许建国 (Xu
  Jianguo); 马锡武 (as printed) = the judge 马锡五 (Ma Xiwu, noted ch07).
- 皖南事变 = "the New Fourth Army Incident" (ch03); 九一八 = "the Mukden Incident"
  (ch05); 西安事变 = "the Xi'an Incident"; 整风 = "the Rectification Movement";
  抢救运动 = "the Rescue Campaign" (subject of ch09).
- Anonymized-by-某 people STAY anonymized (秦某, 周某/张某夫妇, 李某/吕某/陈某,
  何某, 张某, 田某, 樊某, 肖某, 李科长, 李秘书 ...). Do NOT let a later session
  "resolve" them.
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file. The reading uses a single '## Chapter N. Title:
  Subtitle' h1 that folds the subtitle; the zh scaffold keeps two '### ' heading
  lines (chapter + subtitle) -- body-line parity is what check_structure compares,
  so the heading COUNT differs by one and still passes.
- Source-internal name/spelling variants are the minor low-stakes tier: render as
  printed on each page, leave UNfootnoted unless load-bearing (ch08: 郑崇义/郑崇文,
  冯平波/冯平舟, 郭继武/郭力群, 张秉均/张秉钧 all left unfootnoted).

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line PUNCH paragraphs (the 图文 OCR merges these -- split them back
  out), rhetorical questions kept sparingly, datebook chronology staccato, the
  inclusive "we." Runs HOT on the political set-pieces and SARDONIC on the enemy
  and on turncoats. Partisan by design; counter-record in the footnotes.
  Exclamations rationed hard (period by default); most rhetorical questions
  converted to statements; "so it turns out" reveal wrappers dropped. Em dashes
  used only as English punctuation demands; ch08 shipped 4.4/1k after trimming
  appositive/list dashes to colons/commas -- cap one per sentence or one matched
  pair. ch08 was a case-story chapter but still dialogue-light (documents/
  directives/reports dominate); Chapter 9 (Rescue Campaign) carries MORE quoted
  speech -- interrogations, Mao's speeches, the Liu Qiao'er opera -- so contract
  the conversational lines and keep documents/slogans/oaths formal.
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts;
  didactic-and-folksy. Keep the warmth and the edge. (ch07: "peasants do not
  curse for no reason"; ch08: "we need men like Bu Lu; ten or so would do us
  fine.") In ch09 he APOLOGIZES for the campaign's excesses -- keep the plainness.
- **Zhou Enlai:** measured, precise, terse when sharp; the talent-spotter.
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative,
  strategic, cold. 老蒋 = "old Chiang"; 蒋委员长 = "Generalissimo Chiang."
- **Kang Sheng ("Boss Kang" for 康老板):** sharp, doctrinaire, worried about
  political optics; menace under the reasonableness. CENTRAL in Chapter 9 (he
  drove the Rescue Campaign) -- render his voice faithfully in the text and put
  the historians' verdict on his role in the footnote.
- **Bu Lu (陈泊, "the Red Sherlock Holmes"):** the forensic detective; loves
  material evidence, quibbles over terms, coins the "scouting / counter-scouting"
  ladder and "化敌为我"; patient, methodical (ch04, ch07, ch08).
- **Pan Hannian:** cool, daring, epigrammatic (ch05-ch06).
- **Interviewees / memoirs / documents (Principal Sources register):** formal
  reminiscence, kept formal but never wooden.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the
Yan'an security state. Chapter 3 built the open Eighth Route Army offices and the
Chongqing/Xi'an webs. Chapter 4 ("拔钉子") pulled the Nationalist "nails" out of
the Border Region. Chapter 5 ("深入虎穴") turned to the offensive and closed on
the world race for Japan's intentions. Chapter 6 ("东方大谍") ran the Japanese
"state-policy school" front and Pan Hannian's penetration of the enemy's three
agencies. Chapter 7 ("锄奸") laid out the whole defensive war of counter-
espionage and ended on the question whether an agent's heart can be turned.
Chapter 8 ("延安反特第一案") is now COMPLETE: it answers that question with the
great Juntong Hanzhong "expendable-agent" case -- Wu Nanshan's confession at
Qingyang, the line-casting and net-weaving, the tracking of the couriers, the
independent cell burrowed into the Military Commission's Second Bureau, and the
turning of the captured agents under the winning policy of "化敌为我服务." 32
agents netted in Yan'an, all counter-used but one; the case reached into the
1960s and, by the author's own account, fed the cadre-vetting that grew into the
"Rescue Campaign." Chapter 9 ("抢救运动" / "The Rescue Campaign") is that turn:
how the hunt for agents, riding the Rectification, broadened into a purge that
swept up the innocent --逼供信, "agents as thick as hemp," Kang Sheng at the
center -- and ended in Mao's apology.

## Open traps and environment

- **The 图文 OCR is UNUSABLE as a scaffold on plate/column-wrap pages.** Read
  every page image by eye, verify against both OCR configs, and rebuild data/zh
  via a hardcoded resegment_ch09.py. Resolve any faded leaf by magnified crop.
- **Section tails straddle pages AND one-line punch paragraphs hide on figure
  pages.** Read PAST each section heading and each plate. Use indents.py per-page
  first-line flag to settle each page-break seam.
- **assemble.py OVERWRITES data/zh/chNN.txt** -- run resegment AFTER assemble.
- **Number check is noisy.** Run via verify_unit (it passes --noise
  data/noise.txt); extend noise.txt for numerals inside names/places/idioms/
  titles (each commented); prefer REWORDING or carrying an English number WORD to
  carry a real number; carry REAL quantities as digits; noise Arabic+万 literals
  whose value you carry in English.
- **check_content / check_structure are per-batch N/A**; **qc_entities is
  vacuous** -- entity survival by hand.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; catalog them in PROGRESS as a deliberate decision. The standing
  question (every photo, or a curated subset) is still for the commissioner.
- **Source notes are PER-CHAPTER** (参考资料 / 主要资料). Chapter 9's fall at the
  end of section 8; render as a translated "### Principal Sources" section.
- **Chapter 9 is the contested one.** The interested-witness doctrine is central:
  faithful partisan text, counter-record + verdict in the footnotes, fact-checked
  hard against real scholarship (never Grok/AI). Kang Sheng's role is the most
  scrutinized fact -- footnote it.
- **Printed-page markers**: ch04-ch08 carry folio markers (their resegment
  rebuilds the pagemap). ch03 has NONE (a clean rebuild is a corrections-pass
  task). ch01 zh parity 269/299 (from B01) also still open. No note cites a ch03
  folio.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B09 completion
reply in chat, as CLAUDE.md requires.
