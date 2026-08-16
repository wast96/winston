# HANDOFF -- China's Secret War (中国秘密战)

B10 (Chapter 9, the whole chapter, plus Chapter 9's Principal Sources) is
translated, built, and QA-clean. Chapter 9 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B11 (Chapter 10,
the whole chapter). Chapter 9 ("抢救运动" / "The Rescue Campaign") was the book's
most contested chapter: how the hunt for agents, riding the Rectification,
broadened into a purge that swept up the innocent -- 逼供信, "agents as thick as
hemp," Kang Sheng at the center, the fabricated "Red-Flag Party" -- and ended in
Mao's apology. Chapter 10 ("阳谋" / "The Open Scheme") turns to the post-war secret
contest between peace and war: the Chongqing negotiations played in earnest, the
race for the initiative, the "cold-storage spies" reactivated, and the great
withdrawal from Yan'an.

## Message to paste into the next chat

```
China's Secret War B11

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B11 = Chapter 10 (第十章 "阳谋" / "The Open Scheme"), the whole chapter,
ch10s01-ch10s08, end to end per the CLAUDE.md pipeline. PDF pages 343-383; printed
pages 307-347 (offset constant: printed = pdf - 36; spot-verify each section
opener's folio off the scan). Section openers: s1 秘密战线提前较劲 (The Secret Front
Locks Horns Early) PDF 343 / printed 307; s2 假戏真做的重庆谈判 (The Chongqing
Negotiations: A Play Performed in Earnest) PDF 347 / printed 311; s3 是谁错过了历史
机遇？(Who Missed the Historic Opportunity?) PDF 351 / printed 315; s4 激活"冷藏间谍"
(Activating the "Cold-Storage Spies") PDF 356 / printed 320; s5 中国还有"民主联军"
(China Also Had a "Democratic Allied Army") PDF 359 / printed 323; s6 中共情报界的
"后三杰" (The "Latter Three Heroes" of CCP Intelligence) PDF 361 / printed 325; s7
延安大撤退 (The Great Withdrawal from Yan'an) PDF 364 / printed 328; s8 延安游击队
(The Yan'an Guerrillas) PDF 372 / printed 336. Chapter 11 opens at PDF 384 /
printed 348, which is your stop. Chapter 10 carries its OWN chapter-end Principal
Sources (参考资料 / 主要资料); render it as a translated "### Principal Sources"
section, same treatment as ch01-ch09. Simplified Chinese, horizontal; chi_sim,
psm 6; PaddleOCR absent, use scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 343 383 --dpi 300 -> ocr_crop 343 383 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 343 383 ->
indents 343 383 -> assemble ch10 343 383 --offset 36 --blank-assist ->
find_figures (the 图文版 has many inline photos; figures remain DEFERRED, see
below) -> translate to out/ch10_reading.md, one paragraph per TRUE source
paragraph.

METHOD (proven B04-B10): read every page image (data/png/pNNNN.png) by eye,
transcribe each TRUE source paragraph, verify against BOTH OCR configs, and write
scripts/resegment_ch10.py that HARDCODES the verified ('h'|'b', text) item list
and rebuilds data/zh/ch10.txt wholesale (model: scripts/resegment_ch09.py /
resegment_ch08.py). CRITICAL SEAM TRAP (cost real time on ch09): indents.py
MISREADS digit-/date-initial first lines -- it flagged several indented new
"1943年..." paragraph tops as continuations. DO NOT trust indents.py page-top
flags on digit-initial lines; settle every seam by EYE + logic (a physically
indented page top after sentence-final 。？！ = NEW paragraph; a non-indented top,
or one whose previous page ended mid-clause / on a cut word / with ；, =
continuation). assemble.py stays a useful paragraph-BOUNDARY cross-check (on ch09
assemble read 330 vs the 368 hand count, the +38 being the many one-line PUNCH
paragraphs assemble merges plus the short Principal-Sources entries), but the
plate/column-wrap pages STILL merge four-to-eight true paragraphs and inject
photo-caption and vertical-running-title bleed, so the hand resegment stays
authoritative. resegment_ch09.py ALSO rebuilds data/pagemap/ch10.json from a
hand-recorded PAGE_STARTS list -- do the same for ch10 (assemble's own pagemap is
keyed to its merged segmentation, drifts against the reading, and on ch09 even
skipped a folio); each printed page maps to the 0-based body-paragraph index of
the first paragraph that STARTS on it. Any one-line PUNCH paragraph is its own
line/pair.

Then: make_bilingual ch10 -> verify_unit ch10 (parity + numbers + anchors; it
passes --noise data/noise.txt itself, do NOT add flags) -> check_align ch10 ->
qc_entities is vacuous on the flat glossary -- ensure entity survival BY HAND;
verify EVERY quantity against the SCAN. Number check is noisy: numerals inside
names/places/idioms/titles go in data/noise.txt (literal phrase, longest-first,
each commented with its value and the English phrase); a mixed Arabic+万 form the
reader can't combine, so if the value is carried in English, noise the literal
form; a REAL dropped quantity is fixed in the English, never noised. Prefer
REWORDING to carry a number, and carry English number WORDS (two/three/ten): the
check recognizes them. WATCH for the 百合-in-野百合花 / 七大 class of false
positives (a 百/七 that is part of a word or a fixed designation, not a quantity);
noise the literal. Then apparatus_merge for notes+glossary -> check_apparatus
(0 failures; the 19 attestation-note warnings on old rows are pre-existing, not
yours) -> build_reading_epub -> qa_epub (green) and epubcheck (java -jar
/tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub; clean) ->
check_register --ref out/ch01_reading.md out/ch10_reading.md (ch01 is the FROZEN
reference; contract genuine conversational speech, leave documents/directives/
telegrams/slogans formal; both "shall" on ch09 were inside a quoted 1941 policy
document, a legitimate exempt register). Watch the em-dash rate: ch09 shipped
0.0/1k (all appositive-gloss/list dashes converted to colons/commas); keep it low.
Then write PROGRESS and the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of Chapter 9
(out/ch09_reading.md, section 8's close: the cadres sent "to the front to draw
their own conclusions," the 99% freed, and the closing verdict likening the
"Rescue Campaign" to the "Cultural Revolution" -- "the same leader... the same
'strategist,' Kang Sheng") for the voice; consult the VOICE SHEETS and glossary in
this HANDOFF. Cite the book's PRINTED folios in notes, never PDF pages. Never
invent bridging text: if OCR cuts off or a leaf is faded, crop the scan and read
the real continuation. Verify every name, number, and unit designation by crop
before writing (use verify_names.py --auto for the dual-OCR disagreement filter,
then magnified PIL crops for the dense rosters); render load-bearing figures and
unit designations in DIGITS per STYLE. Keep anonymized-by-某 people anonymized.

CHAPTER 10 is the post-war pivot (阳谋 "the open scheme"): the Japanese surrender,
the Chongqing negotiations (重庆谈判) staged while both sides raced for position,
Mao's flight to Chongqing, the "cold-storage spies" (冷藏间谍) reactivated for the
coming civil war, the "Democratic Allied Army," the "Latter Three Heroes" of CCP
intelligence (后三杰 -- likely Xiong Xianghui 熊向晖, Shen Jian 申健, Chen Zhongjing
陈忠经, the Hu Zongnan penetration trio; crop-verify and footnote at first use), and
the Great Withdrawal from Yan'an (延安大撤退, March 1947) + the Yan'an guerrillas.
The interested-witness doctrine (STYLE) stays central: render the partisan account
faithfully in the TEXT, put the counter-record and historians' verdict in the
FOOTNOTES (corroborated / partly / uncorroborated / contradicted), fact-checking
HARD against Wikipedia/Baidu/academic -- never Grok/Grokipedia (they surface in
results; refuse them per rule 5). 阳谋/重庆谈判/双十协定/冷藏间谍/后三杰 are the
terms to gloss/footnote at first use; render the MEANING in plain English.

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
- **B09 = Chapter 8 (延安反特第一案) + Principal Sources.** Chapter 8 COMPLETE.
- **B10 = Chapter 9 (抢救运动) + Principal Sources.** Chapter 9 COMPLETE. 368 English
  body paragraphs (1:1 parity). +16 notes (book total 185); +10 glossary rows (219
  total). qa_epub PASS; epubcheck 0/0/0/0; register within tolerance; em-dash
  0.0/1k. See PROGRESS "Batch B10."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6. Do NOT re-measure.
- **scripts/assemble.py**: --blank-assist. Good paragraph-BOUNDARY cross-check; the
  plate/wrap pages still merge and must be hand-verified. NOTE: assemble OVERWRITES
  data/zh/chNN.txt, so re-run resegment_chNN.py AFTER assemble.
- **indents.py is UNRELIABLE on digit-/date-initial first lines** (mis-flags an
  indented "1943年..." new paragraph as a continuation). Settle page-break seams by
  EYE + logic, using indents.py only as a soft cross-check on prose-initial lines.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; sec_nav
  omits a pending section from the nav of a PARTIALLY translated chapter
  (epubcheck NAV-011 fix). Chapter 10 will again be partially translated during
  the batch, so this matters.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip '***'; markers
  {v}/{d}/{g}/{p} are stripped for parity (check_structure body_lines).
- **scripts/resegment_ch04.py ... resegment_ch09.py**: the model. Rebuild
  data/zh/chNN.txt from a HARDCODED, hand-verified ('h'|'b', text) item list read
  off the scan. resegment_ch09.py ALSO rebuilds data/pagemap/ch09.json from a
  PAGE_STARTS list (each printed page -> the 0-based body index of its first
  starting paragraph); do the same for ch10 (assemble's pagemap drifts and can skip
  a folio). Model resegment_ch10.py on resegment_ch09.py.
- **scripts/verify_names.py --auto**: the dual-OCR disagreement filter; reads
  ONLY the spans the two configs disagree on. Follow with magnified PIL crops
  (plain Pillow, PLAYWRIGHT-free) for dense rosters and rare surnames.
- **data/noise.txt**: this book's number-check noise rules; extend it (longest-
  first, each commented with its value and the English phrase). B10 added: 五花大绑,
  一而再、再而三, 十几万字, 七大, 百忙之中, 两千二百多, 野百合花 (the last is 百合
  "lily", not a numeral -- watch the "part-of-a-word 百/七" false-positive class).
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args.
- **qc_entities.py is a VACUOUS PASS** on this project's flat glossary schema.
  Ensure entity survival BY HAND (consistency grep of the settled handles).
- **check_content.py / check_structure.py** need a --config with a `docs` map
  (whole-book tools); the per-unit contract is covered by verify_unit. Skip them
  per batch.
- The number check recognizes English number WORDS (two, three, second, ten), not
  only digits: carry a count as a word in the prose rather than noising it, and
  reserve noise for numerals inside names/places/idioms/designations.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 219 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ
forever): Juntong; Zhongtong; the Eighth Route Army office / 八办; the Central
Social Affairs Department (中社部) / "the Social Affairs Department"; the Central
Intelligence Department (中情部); the Border Security (边保) = the full 陕甘宁边区
保安处 "Shaanxi-Gansu-Ningxia Border Region Security Office"; 保安处 standalone =
"the Security Office"; the Southern Bureau (南方局); the Southern Committee (南委);
the Special Branch (中央特科); the dog-beating squad; the Military Commission's
Second Bureau (军委二局); the Shandong Column; No. 76; the Ume Kikan; the Iwai
Kōkan; the Tokkō; the Kwantung Army; Manchukuo; the Hanzhong (training) class
(汉训班); the "Dai case" (戴案); the Northwest Special Reconnaissance Station
(西北特侦站); 死间 "expendable agent"; 海底 haidi; Kangda; Shaanbei College; SACO;
Baigongguan; the Rescue Campaign (抢救运动); cadre vetting (审干); screening (甄别);
the Red-Flag Party (红旗党); the Fuxingshe (复兴社); the CC Clique (CC); the Three
People's Principles Youth League (三青团).

Chapter 10 (阳谋: the open scheme) will RE-USE HEAVILY: Juntong/Zhongtong, the
Social Affairs Department, the Border Security, Kang Sheng, Li Kenong, Mao Zedong,
Zhou Enlai, Chiang Kai-shek / old Chiang, Hu Zongnan (胡宗南), Pan Hannian, and the
whole post-war intelligence apparatus. Watch for NEW terms: 阳谋 "the open scheme"
(vs 阴谋 "plot"); 重庆谈判 "the Chongqing negotiations"; 双十协定 "the Double-Tenth
Agreement"; 冷藏间谍 "cold-storage spy" (a sleeper held in reserve); 后三杰 "the
Latter Three Heroes" (the Hu Zongnan penetration trio -- likely 熊向晖 Xiong
Xianghui, 申健 Shen Jian, 陈忠经 Chen Zhongjing; crop-verify, footnote at first
use); 民主联军 "Democratic Allied Army"; 延安大撤退 "the Great Withdrawal from
Yan'an" (March 1947). Render the MEANING in plain English; gloss/footnote the term
at first use (STYLE rule 11).

CONSISTENCY LEDGER points (do not re-decide):
- 抢救运动 = "the Rescue Campaign"; 审干 = "cadre vetting"; 甄别 = "screening";
  整风 = "the Rectification Movement" (all noted/glossed in ch09/earlier).
- 逼供信 = "coerce, confess, believe" (noted ch01, glossed ch09); 红旗党 = "the
  Red-Flag Party"; 特务如麻 = "agents as thick as hemp"; 南委 = "the Southern
  Committee" (wrecked 1942, noted ch09).
- 锄奸 = "rooting out traitors" (ch07); 反间计 = "the counter-espionage stratagem"
  (ch07); 离间计 = "the Stratagem of Sowing Discord" (ch06) -- KEEP DISTINCT.
  反用/逆用 = "counter-use" / "turning the use" (ch08); 死间 = "expendable agent"
  (ch08).
- 汉奸 = "traitor / collaborator" (rendered "traitor" throughout ch09); 特务 =
  "special agent / secret service"; 敌探/日探 = "enemy scout / Japanese scout";
  国特 = "Nationalist agent(s)". Loaded terms, kept as the author uses them;
  loaded-term note placed early.
- 边区 = "the Border Region"; 关中分区 = "the Guanzhong sub-district"; 陇东分区 =
  "the Longdong sub-district"; 三边 = "Sanbian" (the Dingbian/Anbian/Jingbian area).
- 布鲁 = Bu Lu = 陈泊 (Chen Bo, "the Red Sherlock Holmes"); 杜理卿 = 许建国 (Xu
  Jianguo); 马锡武 (as printed) = the judge 马锡五 (Ma Xiwu = Ma Qingtian, noted ch07).
- 皖南事变 = "the New Fourth Army Incident" (ch03); 九一八 = "the Mukden Incident"
  (ch05); 西安事变 = "the Xi'an Incident"; 整风 = "the Rectification Movement";
  抢救运动 = "the Rescue Campaign" (ch09).
- Anonymized-by-某 people STAY anonymized. Do NOT let a later session "resolve" them.
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file. The reading uses a single '## Chapter N. Title:
  Subtitle' h1 that folds the subtitle; the zh scaffold keeps two '### ' heading
  lines (chapter + subtitle) -- body-line parity is what check_structure compares,
  so the heading COUNT differs by one and still passes.
- Book/journal/film/play TITLES in the reading file use *asterisks* (the builder
  turns them into <i>); NEVER a literal <i> tag in a reading .md (the builder
  refuses it). Footnote/glossary bodies ARE XHTML and take <i> + numeric character
  references directly.
- Source-internal name/spelling variants are the minor low-stakes tier: render as
  printed on each page, leave UNfootnoted unless load-bearing (ch09: 熊大正 for the
  physicist 熊大缜 was footnoted because the note names the real figure; a bare
  print variant would not be).

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line PUNCH paragraphs (the 图文 OCR merges these -- split them back
  out), rhetorical questions kept sparingly, datebook chronology staccato, the
  inclusive "we." Runs HOT on the political set-pieces and SARDONIC on the enemy,
  on turncoats, and (in ch09) on Kang Sheng's self-serving maneuvers. Partisan by
  design; counter-record in the footnotes. Exclamations rationed hard (period by
  default); most rhetorical questions converted to statements; "so it turns out"
  reveal wrappers dropped. Em dashes used ONLY as English punctuation demands;
  ch09 shipped 0.0/1k -- convert appositive-gloss and list dashes to colons/commas.
  ch09 carried MORE quoted speech than ch07-ch08 (interrogations, Mao's speeches,
  Liu Qiao'er, Kang Sheng); the conversational lines were contracted, the
  documents/directives/slogans/oaths kept formal. Chapter 10 (negotiations,
  telegrams, penetration cases) will lean documentary again -- contract only the
  genuine dialogue.
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts;
  didactic-and-folksy. Keep the warmth and the edge. (ch08: "we need men like Bu
  Lu; ten or so would do us fine." ch09, sending un-screened cadres to the front:
  "A Communist will stay in the Communist Party; a Nationalist, let him run off to
  the Nationalists, what is there to fear!") In ch09 he APOLOGIZES for the
  campaign's excesses -- kept plain. In ch10 he flies to the Chongqing talks.
- **Zhou Enlai:** measured, precise, terse when sharp; the talent-spotter. In ch09,
  under strain over the Southern Committee, his father's death: kept restrained.
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative,
  strategic, cold. 老蒋 = "old Chiang"; 蒋委员长 = "Generalissimo Chiang."
- **Kang Sheng ("Boss Kang" for 康老板):** sharp, doctrinaire, worried about
  political optics; menace under the reasonableness. CENTRAL in Chapter 9 -- his
  ant/flood metaphors, his "analyze the agent" logic, his self-serving 7th-Congress
  defense ("excesses, not a line error"); rendered faithfully in the text, the
  historians' verdict in the footnote.
- **Li Kenong:** the corrective figure in ch09 -- saw the errors early, reported to
  Mao, questioned Huang Gang kindly. Measured, humane, quietly authoritative.
- **Bu Lu (陈泊, "the Red Sherlock Holmes"):** the forensic detective; in ch09 he
  cracks the Suide "stone case" by re-enacting the self-injury -- exonerating, the
  antithesis of the coercion machine. Patient, methodical.
- **Pan Hannian:** cool, daring, epigrammatic (ch05-ch06); in ch09 pulled back to
  Rectification and criticized. His 1955 fate footnoted.
- **Interviewees / memoirs / documents (Principal Sources register):** formal
  reminiscence, kept formal but never wooden.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the
Yan'an security state. Chapter 3 built the open Eighth Route Army offices and the
Chongqing/Xi'an webs. Chapter 4 ("拔钉子") pulled the Nationalist "nails" out of
the Border Region. Chapter 5 ("深入虎穴") turned to the offensive and closed on the
world race for Japan's intentions. Chapter 6 ("东方大谍") ran the Japanese
"state-policy school" front and Pan Hannian's penetration of the enemy's three
agencies. Chapter 7 ("锄奸") laid out the whole defensive war of counter-espionage.
Chapter 8 ("延安反特第一案") answered whether an agent's heart can be turned, with
the great Juntong Hanzhong "expendable-agent" case and the winning policy of
"化敌为我服务," and tied that case to the Rescue Campaign. Chapter 9 ("抢救运动") is
now COMPLETE: the turn where the hunt for agents, riding the Rectification,
broadened into a purge that swept up the innocent -- the "old-case" suspects and
the Huxi anti-Trotskyist purge, the "four great agents" and the Southern Committee
wreck, the April 1943 mass arrests, Kang Sheng's "Rescue the Fallen" speech and
逼供信, Mao's apology and the screening, the "Liu Qiao'er"/Ma Xiwu counterpoint,
and cadres sent "to the front to draw their own conclusions" -- closing by likening
the campaign to the Cultural Revolution. Chapter 10 ("阳谋" / "The Open Scheme") is
the post-war pivot: the Japanese surrender, the Chongqing negotiations played in
earnest while both sides race for the initiative, the "cold-storage spies"
reactivated for the coming civil war, the "Latter Three Heroes," and the great
withdrawal from Yan'an in March 1947.

## Open traps and environment

- **The 图文 OCR is UNUSABLE as a scaffold on plate/column-wrap pages.** Read
  every page image by eye, verify against both OCR configs, and rebuild data/zh
  via a hardcoded resegment_ch10.py. Resolve any faded leaf by magnified crop.
- **indents.py mis-reads digit-/date-initial page tops** -- settle every seam by
  eye + logic, NOT by the indent flag alone (cost real time on ch09).
- **Section tails straddle pages AND one-line punch paragraphs hide on figure
  pages.** Read PAST each section heading and each plate.
- **assemble.py OVERWRITES data/zh/chNN.txt** -- run resegment AFTER assemble.
  resegment ALSO rebuilds data/pagemap/chNN.json (assemble's pagemap drifts against
  the reading and can skip a folio).
- **Number check is noisy.** Run via verify_unit (it passes --noise
  data/noise.txt); extend noise.txt for numerals inside names/places/idioms/
  designations (each commented); WATCH the "part-of-a-word 百/七" false-positive
  class (百合 "lily", 七大 "Seventh Congress"); prefer REWORDING or carrying an
  English number WORD; carry REAL quantities as digits; noise Arabic+万 literals
  whose value you carry in English.
- **check_content / check_structure are per-batch N/A**; **qc_entities is
  vacuous** -- entity survival by hand.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; catalog them in PROGRESS as a deliberate decision. The standing
  question (every photo, or a curated subset) is still for the commissioner.
- **Source notes are PER-CHAPTER** (参考资料 / 主要资料). Chapter 10's fall at the
  end of section 8; render as a translated "### Principal Sources" section.
- **The interested-witness doctrine is central to this book.** Faithful partisan
  text, counter-record + verdict in the footnotes, fact-checked hard against real
  scholarship (Wikipedia/Baidu/academic -- NEVER Grok/Grokipedia, which surface in
  results and must be refused per rule 5).
- **Printed-page markers**: ch04-ch09 carry folio markers (their resegment rebuilds
  the pagemap). ch03 has NONE (a clean rebuild is a corrections-pass task). ch01 zh
  parity 269/299 (from B01) also still open. No note cites a ch03 folio.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B10 completion
reply in chat, as CLAUDE.md requires.
