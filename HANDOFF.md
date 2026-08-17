# HANDOFF -- China's Secret War (中国秘密战)

B12 (Chapter 11, the whole chapter, plus Chapter 11's Principal Sources) is
translated, built, and QA-clean. Chapter 11 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B13, the FINAL
batch: Chapter 12 (明暗易位) + the Afterword (后记) + back matter + the whole-book
reconciliation sweep + COMPLETION.md. Chapter 11 ("大策反" / "The Great Turning")
was the crest of the intelligence war: the SIGINT duel on the Loess Plateau (Mao's
sub-1,000-man Ninth Detachment vs Hu Zongnan's 230,000), Lü Chu's radio group
reading Hu Zongnan's battle orders before his own generals, the Wang Shijian network
collapse and the Five Martyrs of North China, "subduing the enemy without fighting"
(861.7M enemy eliminated, 1.89M / 21% by turning), the Wu Shi case and the Taiwan
martyrs, and the founding of the PRC.

## Message to paste into the next chat

```
China's Secret War B13

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B13 = the FINAL batch: Chapter 12 (第十二章 "明暗易位" / "Light and Dark
Change Places"), the whole chapter, ch12s01-ch12s06, AND the Afterword (后记),
end to end per the CLAUDE.md pipeline. PDF pages 411-434; printed pages 375-398
(offset constant: printed = pdf - 36; spot-verify each section opener's folio off
the scan). Section openers: s1 中国公安"一百单八将" (China's Public Security
"Hundred-and-Eight Heroes") PDF 411 / printed 375; s2 向西！向南！(West! South!)
PDF 415 / printed 379; s3 哪个国家最先反恐？(Which Country Fought Terror First?)
PDF 420 / printed 384; s4 连公安局长也被镇压 (Even the Police Chiefs Were Purged)
PDF 423 / printed 387; s5 "砸烂公检法！" ("Smash the Police, Procuratorate, and
Courts!") PDF 424 / printed 388; s6 挖掘文化基因 (Excavating the Cultural Gene)
PDF 426 / printed 390. Chapter 12 runs PDF 411-430. The Afterword (后记) is PDF
431-434 / printed 395-398, and PDF 434 is the LAST page of the book -- your stop.
Chapter 12 carries its OWN chapter-end Principal Sources (主要资料) near PDF 430;
render it as a translated "### Principal Sources" section, same treatment as
ch01-ch11. Render the Afterword as its own unit (ch13, matter:back; a "## Afterword"
h1, no section headings). WATCH for the book's own back matter after the afterword
(an index, errata table, or colophon on the final leaves) -- if present, render it
via back_matter.json and apply any erratum to the affected translation. Simplified
Chinese, horizontal; chi_sim, psm 6; PaddleOCR absent, use scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 411 434 --dpi 300 -> ocr_crop 411 434 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17 --right-even
0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6, --running-head
"中国秘密战——中共情报保卫工作纪实") -> ocr_dual 411 434 -> indents 411 434 ->
assemble ch12 411 430 --offset 36 --blank-assist (and a separate assemble for the
afterword span) -> find_figures (the 图文版 has many inline photos; figures remain
DEFERRED, see below) -> translate to out/ch12_reading.md and out/ch13_reading.md,
one paragraph per TRUE source paragraph.

METHOD (proven B04-B12): read every page image (data/png/pNNNN.png) by eye,
transcribe each TRUE source paragraph, verify against BOTH OCR configs, and write
scripts/resegment_ch12.py (and resegment_ch13.py for the afterword) that HARDCODE
the verified ('h'|'b', text) item list and rebuild data/zh/ch12.txt / ch13.txt
wholesale (model: scripts/resegment_ch11.py / resegment_ch10.py). CRITICAL SEAM
TRAP: indents.py MISREADS digit-/date-initial first lines -- do NOT trust its
page-top flags on digit-initial lines; settle every seam by EYE + logic (a
physically indented page top after sentence-final 。？！ = NEW paragraph; a
non-indented top, or one whose previous page ended mid-clause / on a cut word /
with ；, = continuation). assemble.py stays a useful paragraph-BOUNDARY cross-check
but merges the many one-line PUNCH paragraphs plus plate/column-wrap pages (on ch11
assemble read 197 vs the 236 hand count). resegment_ch12.py ALSO rebuilds
data/pagemap/ch12.json from a hand-recorded PAGE_STARTS list (each printed page ->
the 0-based body-paragraph index of the first paragraph that STARTS on it); the
script validates it is strictly increasing. Any one-line PUNCH paragraph is its own
line/pair. NOTE: a section heading may sit MID-PAGE, AFTER the previous section's
tail (as "6.中将之死" did on ch11 p403) -- place headings by where they actually fall.

Then: make_bilingual ch12 (and ch13) -> verify_unit ch12 (parity + numbers +
anchors; it passes --noise data/noise.txt itself, do NOT add flags) -> check_align
ch12 -> qc_entities is vacuous on the flat glossary -- ensure entity survival BY
HAND; verify EVERY quantity against the SCAN. Number check is noisy: numerals inside
names/places/idioms/titles go in data/noise.txt (literal phrase, longest-first, each
commented with its value and the English phrase). WATCH the "part-of-a-word /
Arabic+万 / Arabic+量词" false-positive class (like ch11's 861.7万, 189万, 40两) --
noise the literal and carry the value in English digits; place-name numerals get
noised; idiom numerals (一百单八将, 三头六臂, etc.) get noised; a name's numeral gets
noised. NOTE: 一百单八将 "the Hundred-and-Eight Heroes" (the Water Margin allusion in
s1) will need noising AND a footnote. A REAL dropped quantity is fixed in the
English, never noised; prefer REWORDING to carry a number, and carry English number
WORDS (two/three/ten/first/second). Then apparatus_merge for notes+glossary ->
check_apparatus (0 failures; the 19 attestation-note warnings on old rows are
pre-existing, not yours) -> build_reading_epub -> qa_epub (green) and epubcheck
(java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub; clean) ->
check_register --ref out/ch01_reading.md out/ch12_reading.md out/ch13_reading.md
(ch01 is the FROZEN reference; contract genuine conversational speech, leave
documents/directives/slogans formal; the "砸烂公检法" slogans in s5 stay as slogans,
glossed). Watch the em-dash rate: ch11 shipped 2.0/1k; keep it low (convert
appositive-gloss and list dashes to colons/commas).

THEN, because this is the LAST batch (CLAUDE.md "Definition of done" + last-batch
protocol): run the WHOLE-BOOK RECONCILIATION sweep (check 12) --
scripts/check_reconcile.py for repeated source compounds with more than one English
rendering, every glossary `en` form actually used, no known wrong form surviving,
one spelling locale; its drift candidates are for a HUMAN read. Render the term
ledger as out/term_ledger.md, write out/deep_audit.md (3-5% random-sample deep
audit, fixed seed, honest error rate), feed this book's decided renderings back into
authority.json, write COMPLETION.md from COMPLETION.template.md (with the sampled
error rate and residual uncertainties), commit the final EPUB itself
(git add -f out/chinas_secret_war.epub -- branches outlive containers, chat
attachments do not), and rewrite HANDOFF.md to say the book is COMPLETE and further
work is a corrections pass. Do NOT modify the kickoff section of HANDOFF afterward
(the Stop hook would demand a block that no longer exists) -- on the final batch,
COMPLETION.md replaces the next-batch kickoff; keep a minimal valid fenced block in
HANDOFF if the hook needs one, per CLAUDE.md.

BEFORE translating, read the final two English pages of Chapter 11 (out/ch11_reading.md,
section 7's close: the democratic figures spirited out of Hong Kong and Shanghai to
the new PCC, the "country bumpkins" who will govern, and the Principal Sources) for
the voice; consult the VOICE SHEETS and glossary in this HANDOFF. Cite the book's
PRINTED folios in notes, never PDF pages. Never invent bridging text: if OCR cuts off
or a leaf is faded, crop the scan and read the real continuation. Verify every name,
number, and unit designation by crop before writing; render load-bearing figures and
unit designations in DIGITS per STYLE. Keep anonymized-by-某 people anonymized.

CHAPTER 12 (明暗易位 "light and dark change places") is the resolution: the hidden
front comes into the open as the new state's public-security apparatus is built --
the "Hundred-and-Eight Heroes" (Water Margin allusion) staffing the new organs; the
push West and South to take over the whole country; the counter-terror / anti-agent
chapter ("which country fought terror first?"); then the DARK turn -- the security
men themselves purged (连公安局长也被镇压, and the Cultural Revolution slogan 砸烂
公检法 "smash the police, procuratorate, and courts"); closing on 挖掘文化基因
"excavating the cultural gene," the author's reflective coda that the preface's mining
metaphor answers. The AFTERWORD (后记) is the author's personal close. The
interested-witness doctrine stays central and is at its SHARPEST here (the apparatus
purging itself, the Cultural Revolution): render the partisan account faithfully in
the TEXT, put the counter-record and historians' verdict in the FOOTNOTES
(corroborated / partly / uncorroborated / contradicted), fact-checking HARD against
Wikipedia/Baidu/academic -- never Grok/Grokipedia (they surface in results; refuse
them per rule 5). 一百单八将 / 明暗易位 / 砸烂公检法 / 挖掘文化基因 are the terms to
gloss/footnote at first use; render the MEANING in plain English.

Do NOT pause for approval mid-batch. Deliver the EPUB in chat and (this being the
final batch) paste the COMPLETION summary in the same reply; there is no next kickoff.

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
- **B11 = Chapter 10 (阳谋) + Principal Sources.** Chapter 10 COMPLETE.
- **B12 = Chapter 11 (大策反) + Principal Sources.** Chapter 11 COMPLETE. 236 English
  body paragraphs (1:1 parity). +19 notes (book total 226); +15 glossary rows (249
  total). qa_epub PASS; epubcheck 0/0/0/0; register within tolerance (contr noise,
  little dialogue); em-dash 2.0/1k. See PROGRESS "Batch B12."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6. Do NOT re-measure.
- **scripts/ocr_dual.py**: the dual-engine substitute (PaddleOCR absent). Its wrapper
  can time out at 2m on a long span AFTER it has printed every page (the work is done);
  kill the process GROUP (pkill -g), confirm data/txt/ and data/ocr/ both have all
  pages, and pgrep -c tesseract reads 0.
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
  the "## Chapter N. Title" line. Chapter 12 will again be partially translated during
  the batch.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip '***'; markers
  {v}/{d}/{g}/{p} are stripped for parity (check_structure body_lines).
- **scripts/resegment_ch04.py ... resegment_ch11.py**: the model. Rebuild
  data/zh/chNN.txt from a HARDCODED, hand-verified ('h'|'b', text) item list read off
  the scan. resegment_ch11.py ALSO rebuilds data/pagemap/ch11.json from a PAGE_STARTS
  list of (printed, pdf, prefix) tuples (prefix = distinctive start of the first body
  paragraph on that page), validated strictly increasing. Model resegment_ch12.py on
  resegment_ch11.py.
- **scripts/verify_names.py --auto**: the dual-OCR disagreement filter; reads ONLY
  the spans the two configs disagree on. Follow with magnified PIL crops (plain
  Pillow, PLAYWRIGHT-free) for dense rosters and rare surnames.
- **data/noise.txt**: this book's number-check noise rules; extend it (longest-first,
  each commented with its value and the English phrase). B12 added: 千忙万忙,
  十万火急, 二万五千里长征, 四平战役, 861.7万, 189万, 40两, 名垂千古. The B11 "4万"
  fix (scoped to "4万石") stands -- do not un-scope it.
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args. check_numbers recognizes English
  number WORDS and ORDINALS; carry a count as a word/ordinal in the prose rather than
  noising it, and reserve noise for numerals inside names/places/idioms/designations.
- **qc_entities.py is a VACUOUS PASS** on this project's flat glossary schema.
  Ensure entity survival BY HAND (consistency grep of the settled handles).
- **check_content.py / check_structure.py** need a --config with a `docs` map
  (whole-book tools); the per-unit contract is covered by verify_unit. Skip them
  per batch. FOR B13 (final): run the whole-book tools -- check_reconcile.py (check
  12) and the deep audit -- as the CLAUDE.md "Definition of done" requires.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 249 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ forever):
Juntong; Zhongtong; the Eighth Route Army office / 八办; the Central Social Affairs
Department (中社部) / "the Social Affairs Department"; the Central Intelligence
Department (中情部); the Border Security (边保) = the full 陕甘宁边区保安处; 保安处
standalone = "the Security Office"; the Special Branch (中央特科); the Military
Commission's Second Bureau (军委二局) and Third Bureau (军委三局); No. 76; the Tokkō;
the Kwantung Army; Manchukuo; the Hanzhong (training) class (汉训班); the Bureau of
Confidential Investigation (保密局); the Liaison Department (联络部); "turning"
(策反); the Empty Fort Stratagem (空城计); SACO / the Sino-American Cooperative
Organization (中美特种技术合作所).

Chapter 12 (明暗易位, the new public-security apparatus) will RE-USE HEAVILY: the
Social Affairs Department, the Border Security, Juntong/Zhongtong, Li Kenong (李克农),
Luo Ruiqing (罗瑞卿, likely central to the new 公安部), Zhou Enlai, Mao Zedong, Kang
Sheng, and the whole security lineage. NEW terms to watch in ch12: 一百单八将 "the
Hundred-and-Eight Heroes" (Water Margin allusion, gloss/footnote at first use);
明暗易位 "light and dark change places" (the chapter concept -- put its note on a body
phrase); 砸烂公检法 "smash the police, procuratorate, and courts" (the Cultural
Revolution slogan -- keep as a slogan, gloss); 挖掘文化基因 "excavating the cultural
gene" (the author's closing metaphor, which answers the preface's mining figure --
render concretely, do not amplify; STYLE warns the mining strand runs to preciousness).

CONSISTENCY LEDGER points settled in ch11 (do not re-decide):
- 大策反 = "the great turning"; 策反 = "turning" (work); 华北五烈士 = "the Five Martyrs
  of North China"; 不战而屈人之兵 = "to subdue the enemy without fighting" (Sun Tzu
  canonical); 电子对抗 = "electronic warfare"; 保密局 = "the Bureau of Confidential
  Investigation"; 联络部 = "the Liaison Department"; 九支队 = "the Ninth Detachment";
  绥署二处 = "the Second Section" (of the Northwest Pacification HQ); 军调部 = "the
  Military Mediation office"; 剿总 = "the Pacification Command"; 三大战役 = "the three
  great campaigns"; 辽沈/淮海/平津 = "the Liaoshen / Huaihai / Pingjin campaign(s)";
  西柏坡 = "Xibaipo"; 五一口号 = "the May Day Slogans"; 政治协商会议 = "the Political
  Consultative Conference".
- Battle/place: 青化砭 = "Qinghuabian"; 蟠龙 = "Panlong"; 扶眉 = "Fumei"; 秦岭 =
  "Qinling"; 马场町 = "Machangding"; 城南庄 = "Chengnanzhuang"; 中原 = "the Central
  Plains".
- Person handles fixed this batch: Hu Zongnan, Peng Dehuai, Xi Zhongxun, Fu Zuoyi,
  Chen Mingren, Zeng Zesheng, Guo Ruguai, Wei Lihuang (contested -- see the note),
  Han Liancheng, Wang Shijian, Wu Shi, Yan Youwen, Li Kenong. Distinct near-namesakes:
  刘光国 Liu Guangguo vs 刘光典 Liu Guangdian; 甘陵 Ganling is a PERSON.
- 老蒋 = "old Chiang"; 蒋委员长/蒋总裁 = "Generalissimo Chiang" / "the Generalissimo";
  蒋中正 = Chiang Kai-shek; 蒋经国 = Chiang Ching-kuo.
- 汉奸 = "traitor / collaborator"; 特务 = "special agent / secret service"; 国特 =
  "Nationalist agent(s)". Loaded terms kept as the author uses them.
- Anonymized-by-某 people STAY anonymized. Do NOT let a later session "resolve" them.
- Chapter titles' subtitles fold into title_en in book.json; the reading uses a single
  '## Chapter N. Title: Subtitle' h1 that folds the subtitle; the zh scaffold keeps two
  '### ' heading lines -- body-line parity is what check_structure compares, so the
  heading COUNT differs by one and still passes.
- Book/journal/film/play TITLES in the reading file use *asterisks* (the builder turns
  them into <i>); NEVER a literal <i> tag in a reading .md (the builder refuses it).
  Footnote/glossary bodies ARE XHTML and take <i> + numeric character references only.
- Source-internal name/spelling variants are the minor low-stakes tier: render
  consistently (one pinyin per referent), leave UNfootnoted unless load-bearing. ch11:
  刘进昌 printed for BOTH the Baoding station chief and the recruited deserter (apparent
  source slip; footnoted); 府西分区/分州 kept as printed.

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora chains,
  one-line PUNCH paragraphs (the 图文 OCR merges these -- split them back out),
  rhetorical questions kept sparingly, datebook chronology staccato, the inclusive
  "we." Runs HOT on the political set-pieces and SARDONIC on the enemy, on turncoats,
  and on Chiang's blunders. Partisan by design; counter-record in the footnotes.
  Exclamations rationed hard (period by default); most rhetorical questions converted
  to statements; "so it turns out" reveal wrappers dropped. Em dashes ONLY as English
  punctuation demands (ch11 shipped 2.0/1k). Ch11 leaned documentary (telegrams,
  intercepts, turned generals) with the genuine speech contracted. Ch12 will lean
  documentary AND reflective (the founding of the apparatus, then its self-purge and
  the author's coda) -- keep documents/slogans formal, contract genuine speech, and
  pull the closing "cultural gene" metaphor back rather than amplify it (STYLE).
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts;
  didactic-and-folksy. Keep the warmth and the edge.
- **Zhou Enlai:** measured, precise, terse when sharp; the talent-spotter and handler.
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative, strategic,
  cold, repeatedly out-maneuvered. 老蒋 = "old Chiang".
- **Hu Zongnan:** ambitious, vain, self-important; sets great store by secrecy and is
  penetrated at every turn. Central to ch11.
- **Li Kenong:** measured, humane, quietly authoritative; the corrective figure; the
  Communists' finest intelligence expert. Likely present in ch12's apparatus-building.
- **Kang Sheng ("Boss Kang" for 康老板):** sharp, doctrinaire; menace under the
  reasonableness. Watch for him in ch12's darker turn.
- **Interviewees / memoirs / documents (Principal Sources register):** formal
  reminiscence, kept formal but never wooden.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the Yan'an
security state. Chapter 3 built the open Eighth Route Army offices and the
Chongqing/Xi'an webs. Chapter 4 pulled the Nationalist "nails" out of the Border
Region. Chapter 5 turned to the offensive and the world race for Japan's intentions.
Chapter 6 ran the Japanese "state-policy school" front and Pan Hannian's penetration.
Chapter 7 laid out the defensive war of counter-espionage. Chapter 8 answered whether
an agent's heart can be turned. Chapter 9 was the Rescue Campaign purge that swept up
the innocent. Chapter 10 was the post-war pivot (阳谋). Chapter 11 ("大策反") is now
COMPLETE: the crest of the intelligence war -- the SIGINT duel on the Loess Plateau,
Lü Chu's group reading Hu Zongnan's orders, the Wang Shijian collapse and the Five
Martyrs, the mass turning of enemy generals, the Wu Shi case and the Taiwan martyrs,
and the founding of the state. Chapter 12 ("明暗易位" / "Light and Dark Change
Places") is the FINAL chapter and the resolution: the hidden front comes into the
open as the new state's public-security apparatus is built, is pushed West and South
across the country, fights the early counter-terror war -- and is then purged in its
turn (the police chiefs repressed, "smash the police, procuratorate, and courts"),
closing on "excavating the cultural gene." Then the Afterword.

## Open traps and environment

- **The 图文 OCR is UNUSABLE as a scaffold on plate/column-wrap pages.** Read every
  page image by eye, verify against both OCR configs, and rebuild data/zh via a
  hardcoded resegment_ch12.py (+ resegment_ch13.py for the afterword). Resolve any
  faded leaf by magnified crop.
- **indents.py mis-reads digit-/date-initial page tops** -- settle every seam by eye +
  logic, NOT by the indent flag alone. A section heading can sit MID-PAGE after the
  previous section's tail.
- **Section tails straddle pages AND one-line punch paragraphs hide on figure pages.**
  Read PAST each section heading and each plate.
- **assemble.py OVERWRITES data/zh/chNN.txt** -- run resegment AFTER assemble.
  resegment ALSO rebuilds data/pagemap/chNN.json.
- **Number check is noisy.** Run via verify_unit (it passes --noise data/noise.txt);
  extend noise.txt for numerals inside names/places/idioms/designations (each
  commented; watch 一百单八将 in s1); prefer REWORDING or carrying an English number
  WORD/ordinal; carry REAL quantities as digits; noise Arabic+万 / Arabic+量词 literals
  whose value you carry in English.
- **check_content / check_structure are per-batch N/A**; **qc_entities is vacuous** --
  entity survival by hand. FOR B13 run the whole-book reconciliation (check 12) and
  deep audit as part of the completion requirement.
- **The builder does not anchor a chapter-title H1** -- put chapter-concept notes on a
  body phrase.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline photos;
  catalogued in PROGRESS as a deliberate decision. The standing question (every photo,
  or a curated subset) is still for the commissioner -- flag it in COMPLETION.
- **Source notes are PER-CHAPTER** (主要资料). Chapter 12's fall at the end of section
  6 (~PDF 430); render as a translated "### Principal Sources" section. The Afterword
  is a separate unit.
- **The interested-witness doctrine is central and at its SHARPEST in ch12** (the
  apparatus purging itself, the Cultural Revolution). Faithful partisan text,
  counter-record + verdict in the footnotes, fact-checked hard against real scholarship
  (Wikipedia/Baidu/academic -- NEVER Grok/Grokipedia, refuse per rule 5).
- **Printed-page markers**: ch04-ch11 carry folio markers (their resegment rebuilds the
  pagemap). ch03 has NONE (a clean rebuild is a corrections-pass task). ch01 zh parity
  269/299 (from B01) also still open. No note cites a ch03 folio.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B12 completion
reply in chat, as CLAUDE.md requires.
