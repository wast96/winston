# HANDOFF -- China's Secret War (中国秘密战)

B11 (Chapter 10, the whole chapter, plus Chapter 10's Principal Sources) is
translated, built, and QA-clean. Chapter 10 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B12 (Chapter 11,
the whole chapter). Chapter 10 ("阳谋" / "The Open Scheme") was the post-war pivot:
the Japanese surrender, the Chongqing negotiations played in earnest while both sides
raced for position, the "cold-storage spies" reactivated, the "Democratic Allied
Army" defections, the "Latter Three Heroes" in Hu Zongnan's HQ, and the Great
Withdrawal from Yan'an. Chapter 11 ("大策反" / "The Great Turning") is the highest art
of the secret war: electronic warfare on the Loess Plateau, the race to read Hu
Zongnan's battle orders, the "Five Martyrs of North China," subduing the enemy
without a fight, and the founding of the state.

## Message to paste into the next chat

```
China's Secret War B12

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B12 = Chapter 11 (第十一章 "大策反" / "The Great Turning"), the whole chapter,
ch11s01-ch11s07, end to end per the CLAUDE.md pipeline. PDF pages 384-410; printed
pages 348-374 (offset constant: printed = pdf - 36; spot-verify each section opener's
folio off the scan). Section openers: s1 黄土高原上演电子对抗 (Electronic Warfare on
the Loess Plateau) PDF 384 / printed 348; s2 谁先收到胡宗南的作战电报？(Who Received
Hu Zongnan's Battle Orders First?) PDF 388 / printed 352; s3 情报工作最成功的时期
(The Most Successful Period of Intelligence Work) PDF 392 / printed 356; s4 "华北五
烈士" (The "Five Martyrs of North China") PDF 393 / printed 357; s5 不战而屈人之兵
(Subduing the Enemy Without a Fight) PDF 396 / printed 360; s6 中将之死 (Death of a
Lieutenant General) PDF 403 / printed 367; s7 建国大业 (The Great Enterprise of
Founding the Nation) PDF 406 / printed 370. Chapter 12 opens at PDF 411 / printed 375,
which is your stop. Chapter 11 carries its OWN chapter-end Principal Sources (主要资料);
render it as a translated "### Principal Sources" section, same treatment as
ch01-ch10. Simplified Chinese, horizontal; chi_sim, psm 6; PaddleOCR absent, use
scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 384 410 --dpi 300 -> ocr_crop 384 410 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17 --right-even 0.94],
shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6, --running-head
"中国秘密战——中共情报保卫工作纪实") -> ocr_dual 384 410 -> indents 384 410 ->
assemble ch11 384 410 --offset 36 --blank-assist -> find_figures (the 图文版 has many
inline photos; figures remain DEFERRED, see below) -> translate to
out/ch11_reading.md, one paragraph per TRUE source paragraph.

METHOD (proven B04-B11): read every page image (data/png/pNNNN.png) by eye,
transcribe each TRUE source paragraph, verify against BOTH OCR configs, and write
scripts/resegment_ch11.py that HARDCODES the verified ('h'|'b', text) item list and
rebuilds data/zh/ch11.txt wholesale (model: scripts/resegment_ch10.py /
resegment_ch09.py). CRITICAL SEAM TRAP: indents.py MISREADS digit-/date-initial first
lines -- do NOT trust its page-top flags on digit-initial lines; settle every seam by
EYE + logic (a physically indented page top after sentence-final 。？！ = NEW
paragraph; a non-indented top, or one whose previous page ended mid-clause / on a cut
word / with ；, = continuation). assemble.py stays a useful paragraph-BOUNDARY
cross-check but merges the many one-line PUNCH paragraphs plus plate/column-wrap pages
(on ch10 assemble read 330 vs the 355 hand count). resegment_ch11.py ALSO rebuilds
data/pagemap/ch11.json from a hand-recorded PAGE_STARTS list (each printed page ->
the 0-based body-paragraph index of the first paragraph that STARTS on it); the script
validates it is strictly increasing. Any one-line PUNCH paragraph is its own line/pair.

Then: make_bilingual ch11 -> verify_unit ch11 (parity + numbers + anchors; it passes
--noise data/noise.txt itself, do NOT add flags) -> check_align ch11 -> qc_entities is
vacuous on the flat glossary -- ensure entity survival BY HAND; verify EVERY quantity
against the SCAN. Number check is noisy: numerals inside names/places/idioms/titles go
in data/noise.txt (literal phrase, longest-first, each commented with its value and
the English phrase). WATCH the "part-of-a-word / Arabic+万" false-positive class: e.g.
a mixed Arabic+万 form (like ch10's 14万) is mangled by the parser -- noise the literal
and carry the value in English digits; place-name numerals (五华山, 五原, 二十里铺) get
noised; idiom numerals (七七八八, 不远千里, 一失足成千古恨) get noised; a name's numeral
(祁三益) gets noised. A REAL dropped quantity is fixed in the English, never noised;
prefer REWORDING to carry a number, and carry English number WORDS (two/three/ten/first/
second) -- the check recognizes number words and ordinals. Then apparatus_merge for
notes+glossary -> check_apparatus (0 failures; the 19 attestation-note warnings on old
rows are pre-existing, not yours) -> build_reading_epub -> qa_epub (green) and
epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub;
clean) -> check_register --ref out/ch01_reading.md out/ch11_reading.md (ch01 is the
FROZEN reference; contract genuine conversational speech, leave documents/directives/
telegrams/slogans/oaths formal). Watch the em-dash rate: ch10 shipped 0.0/1k; keep it
low (convert appositive-gloss and list dashes to colons/commas). Then write PROGRESS
and the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of Chapter 10 (out/ch10_reading.md,
section 8's close: the security regiments becoming PLA main-force divisions, the recovery
of Yan'an on 22 Apr 1948, and the closing "the great Communist army was already a tiger
with wings ... China's secret war too would enter a new realm") for the voice; consult
the VOICE SHEETS and glossary in this HANDOFF. Cite the book's PRINTED folios in notes,
never PDF pages. Never invent bridging text: if OCR cuts off or a leaf is faded, crop
the scan and read the real continuation. Verify every name, number, and unit designation
by crop before writing (use verify_names.py --auto for the dual-OCR disagreement filter,
then magnified PIL crops for the dense rosters); render load-bearing figures and unit
designations in DIGITS per STYLE. Keep anonymized-by-某 people anonymized.

CHAPTER 11 is the crest of the intelligence war (大策反 "the great turning" / mass
turning of the enemy): the SIGINT/electronic-warfare duel on the Loess Plateau as
Peng Dehuai's outnumbered Northwest Field Army fights Hu Zongnan; the "後三杰"/熊向晖
thread continues as the CCP reads Hu Zongnan's operational telegrams before his own
generals do; the "Five Martyrs of North China" (华北五烈士 -- 谢士炎 Xie Shiyan, who
was INTRODUCED in ch10 sec 6, is one of them; crop-verify and footnote the five at
first use); Sun Tzu's 不战而屈人之兵 "to subdue the enemy without fighting" (use the
canonical English per STYLE) as generals are turned; the death of a lieutenant general
(中将之死); and 建国大业 the founding of the PRC. The interested-witness doctrine
stays central: render the partisan account faithfully in the TEXT, put the
counter-record and historians' verdict in the FOOTNOTES (corroborated / partly /
uncorroborated / contradicted), fact-checking HARD against Wikipedia/Baidu/academic --
never Grok/Grokipedia (they surface in results; refuse them per rule 5). 大策反 /
华北五烈士 / 不战而屈人之兵 are the terms to gloss/footnote at first use; render the
MEANING in plain English.

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
- **B04 = Chapter 3 + Principal Sources.** Chapter 3 COMPLETE.
- **B05 = Chapter 4 + Principal Sources.** Chapter 4 COMPLETE.
- **B06 = Chapter 5 + Principal Sources.** Chapter 5 COMPLETE.
- **B07 = Chapter 6 + Principal Sources.** Chapter 6 COMPLETE.
- **B08 = Chapter 7 (锄奸) + Principal Sources.** Chapter 7 COMPLETE.
- **B09 = Chapter 8 (延安反特第一案) + Principal Sources.** Chapter 8 COMPLETE.
- **B10 = Chapter 9 (抢救运动) + Principal Sources.** Chapter 9 COMPLETE.
- **B11 = Chapter 10 (阳谋) + Principal Sources.** Chapter 10 COMPLETE. 355 English
  body paragraphs (1:1 parity). +22 notes (book total 207); +15 glossary rows (234
  total). qa_epub PASS; epubcheck 0/0/0/0; register within tolerance (contr 7.6/1k);
  em-dash 0.0/1k. See PROGRESS "Batch B11."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6. Do NOT re-measure.
- **scripts/assemble.py**: --blank-assist. Good paragraph-BOUNDARY cross-check; the
  plate/wrap pages still merge and must be hand-verified. NOTE: assemble OVERWRITES
  data/zh/chNN.txt, so re-run resegment_chNN.py AFTER assemble.
- **indents.py is UNRELIABLE on digit-/date-initial first lines** (mis-flags an
  indented "1946年.../第二次..." new paragraph as a continuation). Settle page-break
  seams by EYE + logic, using indents.py only as a soft cross-check on prose-initial
  lines.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; sec_nav omits
  a pending section from the nav of a PARTIALLY translated chapter. The builder does
  NOT anchor a chapter-title H1 -- put any chapter-concept note on a BODY phrase, not
  the "## Chapter N. Title" line (cost a build on ch10). Chapter 11 will again be
  partially translated during the batch.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip '***'; markers
  {v}/{d}/{g}/{p} are stripped for parity (check_structure body_lines).
- **scripts/resegment_ch04.py ... resegment_ch10.py**: the model. Rebuild
  data/zh/chNN.txt from a HARDCODED, hand-verified ('h'|'b', text) item list read off
  the scan. resegment_ch10.py ALSO rebuilds data/pagemap/ch10.json from a PAGE_STARTS
  list of (printed, pdf, prefix) tuples (prefix = distinctive start of the first body
  paragraph on that page), validated strictly increasing. Model resegment_ch11.py on
  resegment_ch10.py.
- **scripts/verify_names.py --auto**: the dual-OCR disagreement filter; reads ONLY
  the spans the two configs disagree on. Follow with magnified PIL crops (plain
  Pillow, PLAYWRIGHT-free) for dense rosters and rare surnames.
- **data/noise.txt**: this book's number-check noise rules; extend it (longest-first,
  each commented with its value and the English phrase). B11 added: 14万,
  一失足成千古恨, 两眼一抹黑, 陈云、彭真二人, 不远千里, 二十里铺, 三十里铺, 七七八八,
  夫妻两人, 前一日, 零件, 五华山, 五原, 祁三益, 两区. **B11 tooling FIX (do not
  revert):** the old rule "4万" (intended for 4万石) was eating the "4万" inside "14万"
  and leaving a spurious "1"; it is now scoped to "4万石" per its own comment.
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args. check_numbers recognizes English
  number WORDS and ORDINALS (one..thirteen, first..thirteenth, fourteen..seventeen,
  twenty-first..); carry a count as a word/ordinal in the prose rather than noising it,
  and reserve noise for numerals inside names/places/idioms/designations.
- **qc_entities.py is a VACUOUS PASS** on this project's flat glossary schema.
  Ensure entity survival BY HAND (consistency grep of the settled handles).
- **check_content.py / check_structure.py** need a --config with a `docs` map
  (whole-book tools); the per-unit contract is covered by verify_unit. Skip them
  per batch.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 234 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ forever):
Juntong; Zhongtong; the Eighth Route Army office / 八办; the Central Social Affairs
Department (中社部) / "the Social Affairs Department"; the Central Intelligence
Department (中情部); the Border Security (边保) = the full 陕甘宁边区保安处; 保安处
standalone = "the Security Office"; the Special Branch (中央特科); the Military
Commission's Second Bureau (军委二局) and Third Bureau (军委三局); No. 76; the Tokkō;
the Kwantung Army; Manchukuo; the Hanzhong (training) class (汉训班); 死间 "expendable
agent"; the Rescue Campaign (抢救运动); cadre vetting (审干); screening (甄别); the
Rectification Movement (整风); the Red-Flag Party (红旗党).

Chapter 11 (大策反) will RE-USE HEAVILY: the Border Security, the Social Affairs
Department, Juntong/Zhongtong, Hu Zongnan (胡宗南), Peng Dehuai (彭德怀), Xi Zhongxun
(习仲勋), Li Kenong (李克农), Zhou Enlai, Mao Zedong, Chiang Kai-shek / old Chiang, and
the whole penetration apparatus. Terms SETTLED THIS BATCH (ch10) that recur: the Latter
Three Heroes (后三杰 = Xiong Xianghui 熊向晖, Chen Zhongjing 陈忠经, Shen Jian 申健);
"idle chessman" (闲棋冷子, ch03); the Longtan Trio / Three Heroes of Longtan (龙潭三杰,
ch01); the cold-storage / strategic spy; the Empty Fort Stratagem (空城计). NEW terms to
watch in ch11: 大策反 "the great turning" (mass turning of enemy forces); 华北五烈士
"the Five Martyrs of North China" (谢士炎 Xie Shiyan -- introduced ch10 sec 6 -- is one;
crop-verify the five, footnote at first use); 不战而屈人之兵 = Sun Tzu's "to subdue the
enemy without fighting" (use the CANONICAL English per STYLE); 电子对抗 "electronic
warfare / countermeasures." Render the MEANING in plain English; gloss/footnote at first
use.

CONSISTENCY LEDGER points (do not re-decide):
- 阳谋 = "the open scheme" (vs 阴谋 "plot"); 重庆谈判 = "the Chongqing negotiations";
  双十协定 = "the Double-Tenth Agreement"; 冷藏间谍 = "cold-storage spy" / 战略间谍 =
  "strategic spy"; 后三杰 = "the Latter Three Heroes"; 龙潭三杰 = "the Three Heroes of
  Longtan"; 民主联军 = "Democratic Allied Army"; 延安大撤退 = "the Great Withdrawal
  from Yan'an"; 跑反 = "fleeing the raid" (paofan); 高树勋运动 = "the Gao Shuxun
  Movement"; 还乡团 = "home-returning corps"; 生进死出 = "enter alive, leave only dead."
- 手筋 = "tesuji" (go term, glossed ch10); 空城计 = "the Empty Fort Stratagem" (ch10);
  鸿门宴 = "the Feast at Hongmen" (ch10).
- 边区 = "the Border Region"; 关中分区 = "the Guanzhong sub-district"; 陇东分区 =
  "the Longdong sub-district"; 三边 = "Sanbian"; 晋绥 = "Jin-Sui"; 晋察冀 = "Jin-Cha-Ji."
- 老蒋 = "old Chiang"; 蒋委员长/蒋总裁 = "Generalissimo Chiang" / "the Generalissimo";
  蒋中正 = Chiang Kai-shek; 蒋经国 = Chiang Ching-kuo.
- 汉奸 = "traitor / collaborator"; 特务 = "special agent / secret service"; 国特 =
  "Nationalist agent(s)". Loaded terms kept as the author uses them; loaded-term note
  placed early.
- Anonymized-by-某 people STAY anonymized. Do NOT let a later session "resolve" them.
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file. The reading uses a single '## Chapter N. Title:
  Subtitle' h1 that folds the subtitle; the zh scaffold keeps two '### ' heading lines
  (chapter + subtitle) -- body-line parity is what check_structure compares, so the
  heading COUNT differs by one and still passes.
- Book/journal/film/play TITLES in the reading file use *asterisks* (the builder turns
  them into <i>); NEVER a literal <i> tag in a reading .md (the builder refuses it).
  Footnote/glossary bodies ARE XHTML and take <i> + numeric character references
  directly.
- Source-internal name/spelling variants are the minor low-stakes tier: render
  consistently (one pinyin per referent), leave UNfootnoted unless load-bearing. ch10:
  刘戡/刘勘 (both "Liu Kan"), 章炳南 misprinted 张炳南 on the monument (kept as the
  author notes it).

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora chains,
  one-line PUNCH paragraphs (the 图文 OCR merges these -- split them back out),
  rhetorical questions kept sparingly, datebook chronology staccato, the inclusive
  "we." Runs HOT on the political set-pieces and SARDONIC on the enemy, on turncoats,
  and on Chiang's blunders. Partisan by design; counter-record in the footnotes.
  Exclamations rationed hard (period by default); most rhetorical questions converted
  to statements; "so it turns out" reveal wrappers dropped. Em dashes used ONLY as
  English punctuation demands; ch09 and ch10 shipped 0.0/1k. Ch10 leaned documentary
  (telegrams, negotiations, killing-directives) with real dialogue interspersed;
  contract only the genuine dialogue. Ch11 (SIGINT duel, telegram intercepts, turned
  generals) will lean documentary again -- keep the intercepts/telegrams formal,
  contract the genuine speech.
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts;
  didactic-and-folksy. Keep the warmth and the edge. (ch10: the "two directors
  sponsoring a third director into the Party" joke; to Hu Jingduo, "you got off Deng
  Baoshan's boat and onto Xi Zhongxun's"; his grief over Wang Shiwei, "give me back my
  Wang Shiwei," kept plain.)
- **Zhou Enlai:** measured, precise, terse when sharp; the talent-spotter and the
  handler (ch10: weighs whether to pull Xiong Xianghui after the notebook is lost on
  Marshall's plane; "worth several divisions").
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative, strategic,
  cold, and in ch10 repeatedly out-maneuvered. 老蒋 = "old Chiang"; 蒋委员长 =
  "Generalissimo Chiang."
- **Hu Zongnan:** ambitious, vain, self-important ("no mere man of arms ... political
  ambition to succeed Chiang"); sets great store by secrecy and is penetrated at every
  turn. Central in ch11 too.
- **Kang Sheng ("Boss Kang" for 康老板):** sharp, doctrinaire; menace under the
  reasonableness. In ch10 one of the three possible approvers of Wang Shiwei's
  execution.
- **Li Kenong:** measured, humane, quietly authoritative; the corrective figure. In
  ch10 takes responsibility for Wang Shiwei's death.
- **Xiong Xianghui (the "idle chessman"):** the cool, deep-cover penetration agent in
  Hu Zongnan's HQ; drafts Hu's own attack plan and copies it to Yan'an. CENTRAL to
  ch11's telegram-intercept thread.
- **Interviewees / memoirs / documents (Principal Sources register):** formal
  reminiscence, kept formal but never wooden.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the Yan'an
security state. Chapter 3 built the open Eighth Route Army offices and the
Chongqing/Xi'an webs. Chapter 4 ("拔钉子") pulled the Nationalist "nails" out of the
Border Region. Chapter 5 ("深入虎穴") turned to the offensive and closed on the world
race for Japan's intentions. Chapter 6 ("东方大谍") ran the Japanese "state-policy
school" front and Pan Hannian's penetration. Chapter 7 ("锄奸") laid out the defensive
war of counter-espionage. Chapter 8 ("延安反特第一案") answered whether an agent's
heart can be turned, with the Hanzhong "expendable-agent" case. Chapter 9 ("抢救运动")
was the purge that swept up the innocent, ending in Mao's apology. Chapter 10 ("阳谋")
is now COMPLETE: the post-war pivot -- the Japanese surrender and the international
receivings (Vietnam, Taiwan, the Long Yun ouster), the Chongqing negotiations played
in earnest while both sides raced for the Northeast, the "cold-storage spies" (Yan
Youwen, Shen Anna) reactivated, the wave of "democratic" defections (the Gao Shuxun
Movement, Hengshan), the "Latter Three Heroes" reading Hu Zongnan's plan to take
Yan'an, the Great Withdrawal of March 1947 (the execution of Wang Shiwei, the candid
2,296-killed reckoning, the Yihe criticism of Zhou Xing), and the Yan'an guerrillas
who became PLA main-force divisions -- closing on the recovery of Yan'an in April 1948
and the "tiger with wings." Chapter 11 ("大策反" / "The Great Turning") is the crest:
the electronic-warfare duel on the Loess Plateau, the reading of Hu Zongnan's battle
orders, the Five Martyrs of North China, subduing the enemy without a fight, and the
founding of the state.

## Open traps and environment

- **The 图文 OCR is UNUSABLE as a scaffold on plate/column-wrap pages.** Read every
  page image by eye, verify against both OCR configs, and rebuild data/zh via a
  hardcoded resegment_ch11.py. Resolve any faded leaf by magnified crop.
- **indents.py mis-reads digit-/date-initial page tops** -- settle every seam by eye +
  logic, NOT by the indent flag alone.
- **Section tails straddle pages AND one-line punch paragraphs hide on figure pages.**
  Read PAST each section heading and each plate.
- **assemble.py OVERWRITES data/zh/chNN.txt** -- run resegment AFTER assemble.
  resegment ALSO rebuilds data/pagemap/chNN.json.
- **Number check is noisy.** Run via verify_unit (it passes --noise data/noise.txt);
  extend noise.txt for numerals inside names/places/idioms/designations (each
  commented); prefer REWORDING or carrying an English number WORD/ordinal; carry REAL
  quantities as digits; noise Arabic+万 literals whose value you carry in English (the
  parser mangles them). The "4万" rule is now scoped to "4万石" -- do not un-scope it.
- **check_content / check_structure are per-batch N/A**; **qc_entities is vacuous** --
  entity survival by hand.
- **The builder does not anchor a chapter-title H1** -- put chapter-concept notes on a
  body phrase.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline photos;
  catalogued in PROGRESS as a deliberate decision. The standing question (every photo,
  or a curated subset) is still for the commissioner.
- **Source notes are PER-CHAPTER** (主要资料). Chapter 11's fall at the end of section
  7; render as a translated "### Principal Sources" section.
- **The interested-witness doctrine is central to this book.** Faithful partisan text,
  counter-record + verdict in the footnotes, fact-checked hard against real scholarship
  (Wikipedia/Baidu/academic -- NEVER Grok/Grokipedia, which surface in results and must
  be refused per rule 5).
- **Printed-page markers**: ch04-ch10 carry folio markers (their resegment rebuilds the
  pagemap). ch03 has NONE (a clean rebuild is a corrections-pass task). ch01 zh parity
  269/299 (from B01) also still open. No note cites a ch03 folio.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B11 completion
reply in chat, as CLAUDE.md requires.
