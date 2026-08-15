# HANDOFF — China's Secret War (中国秘密战)

B04 (Chapter 3, the whole chapter, plus Chapter 3's Principal Sources) is
translated, built, and QA-clean. Chapter 3 is now COMPLETE. The frozen voice
reference is still out/ch01_reading.md. The kickoff below is for B05 (Chapter 4,
the whole chapter).

## Message to paste into the next chat

```
China's Secret War B05

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B05 = Chapter 4 (第四章 拔钉子 / "Pulling Out the Nails"), the whole
chapter, ch04s01-ch04s05, end to end per the CLAUDE.md pipeline. PDF pages
171-183; printed pages 135-147 (offset constant: printed = pdf - 36; spot-verify
each section opener's folio off the scan). Section openers: s1 "双重政权" (Dual
Regimes) PDF 171 / printed 135; s2 争抢"宝葫芦" (Fighting Over the "Treasure
Gourd") PDF 175 / printed 139; s3 "红色福尔摩斯"出招 (The "Red Sherlock Holmes"
Makes His Move) PDF 178 / printed 142; s4 反腐风暴 (The Anti-Corruption Storm)
PDF 179 / printed 143; s5 "护送出境" ("Escorted Out of the Territory") PDF 180 /
printed 144. Chapter 5 opens at PDF 184 / printed 148, which is your stop.
Chapter 4 carries its OWN chapter-end Principal Sources (主要资料); render it as a
translated "### Principal Sources" section, same treatment as ch01/ch02/ch03.
Simplified Chinese, horizontal; chi_sim, psm 6; PaddleOCR absent, use
scripts/ocr_dual.py.

The pipeline is established; reuse it, do not re-measure. Recipe:
render 171 183 --dpi 300 -> ocr_crop 171 183 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 171 183 ->
indents 171 183 -> add the chapter title, subtitle, and section 1-5 heading
strings (as the OCR reads them) to data/structure.json -> assemble ch04 171 183
--offset 36 --blank-assist -> find_figures (the 图文版 has many inline photos;
figures remain DEFERRED, see below) -> translate to out/ch04_reading.md, one
paragraph per TRUE source paragraph (read every page off the scan; the 图文
pages under-segment, so expect to re-segment the zh as in B02/B03/B04 —
scripts/resegment_ch03.py is the model; write scripts/resegment_ch04.py) ->
verify_unit ch04 / check_align ch04 / qc_entities on out/ch04_bilingual.md
(check_content is N/A to this project's schema; the number check is noisy on this
book, run via verify_unit which passes --noise data/noise.txt, and verify every
quantity against the SCAN) -> apparatus_merge for notes and glossary -> build
EPUB -> qa_epub (green) and epubcheck (clean) -> check_register
--ref out/ch01_reading.md out/ch04_reading.md (ch01 is the FROZEN reference; the
dialogue metric is noise in low-dialogue units, judge on the narratorial signals)
-> write PROGRESS and the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of Chapter 3
(out/ch03_reading.md, section 7's "making friends" close and the Principal
Sources) for the voice; consult the VOICE SHEETS and glossary in this HANDOFF.
Cite the book's PRINTED folios in notes, never PDF pages. Never invent bridging
text: if OCR cuts off, crop the scan and read the real continuation. WATCH THE
SECTION TAILS: a section's last paragraphs often straddle onto the NEXT section's
opening page before the heading, and the 图文 pages hide one-line PUNCH paragraphs
that the OCR merges (in B04 five of them had to be split back out) — read past
each heading and each plate. Verify every name, number, and unit designation by
crop before writing (B04 caught a dropped "22nd Army", a "14th"-for-"4th"
regiment, and a "dozen"-for-"twenty" — the number check flags these); render
load-bearing figures and unit designations in DIGITS (the 18th Group Army, the
38th Army, 300,000 rounds) per STYLE. State corroborated/uncorroborated/
contradicted in notes; the partisan voice is content, the counter-record goes in
the footnote.

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
- **B04 = Chapter 3, the whole chapter + Chapter 3 Principal Sources.** 305
  English body paragraphs (1:1 parity). +27 notes (book total 84); +21 glossary
  rows (70 total). qa_epub PASS; epubcheck 0/0/0. **Chapter 3 is COMPLETE.**
  See PROGRESS "Batch B04."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6.
- **scripts/assemble.py**: --blank-assist (blank-line signal layered on the
  indent, gated by sentence-end) for figure-heavy pages.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; sec_nav
  omits a pending section from the nav of a PARTIALLY translated chapter
  (epubcheck NAV-011 fix). Chapter 4 will again be partially translated during
  the batch, so this matters.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip the '***'
  scene-break marker, matching verify_unit / check_structure.
- **scripts/resegment_ch02.py, resegment_ch02b03.py, resegment_ch03.py**: the
  reproducible zh re-segmentation for the figure-heavy chapters. Model
  resegment_ch04.py on resegment_ch03.py: identify each OCR merge/split by a
  garbled-OCR anchor substring (grep the assembled data/zh/ch04.txt for the
  real bytes — 阎→间, 蒋→藉/薪, 共→其, 桂→佳, 薇→芍, 暗→瞳 are common OCR swaps),
  and rewrite the "主要资料:" body line as "### Principal Sources". It is NOT
  idempotent — re-run assemble before each run.
- **data/noise.txt**: carries this book's number-check noise rules; extend it
  (longest-first, each commented) as new idioms/place-names/name-numerals surface.
- **verify_unit.py** takes ONLY the unit id (it passes --noise data/noise.txt to
  check_numbers itself); do NOT pass extra args.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 70 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles to KEEP fixed (one handle per organ
forever): the Eighth Route Army office / 八办 ("ba-ban", glossed); the Social
Affairs Department (中社部); the Central Intelligence Department (中情部, new in
ch03); the Border Security (边保); the Southern Bureau (南方局); Juntong;
Zhongtong; the Special Branch (中央特科). Chapter 4 ("拔钉子" — pulling out
Nationalist agents inside the Border Region) will re-use the Border Security,
the Yan'an security organs, Kang Sheng, and the "'38-style" cadres heavily.

CONSISTENCY LEDGER points (do not re-decide):
- 杜理卿 (Du Liqing) = 许建国 (Xu Jianguo) are ONE man (glossary row records it).
- Kang Sheng's alias Zhao Rong; born Zhang Zongke / Zhang Wang (settled in B01).
- "black dogs" (黑狗子 = KMT police), the "far country" (远方 = USSR / Comintern),
  the "'38-style" cadre, "reform and opening" (改革开放, the author's recurring
  anachronistic motif — render consistently, noted once in ch02, do NOT re-note).
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file (confirmed ch01-ch03; do the same for ch04).
- Tan Kah Kee (陈嘉庚), Ho Chi Minh (胡志明/阮爱国), Aung San (昂山), Bethune
  (白求恩), Edgar Snow / Red Star Over China, Stilwell (史迪威) — conventional
  English forms, now glossary/noted (ch03).

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line PUNCH paragraphs (the 图文 OCR merges these — split them back
  out), rhetorical questions kept sparingly (only where they land in English),
  datebook chronology staccato, the inclusive "we." Runs HOT in the political
  set-pieces and SARDONIC on the enemy and on turncoats-become-officials; keep
  both. Partisan by design; counter-record lives in the footnotes. Exclamation
  rationed hard (period by default); most rhetorical questions converted to
  statements; "so it turns out" reveal wrappers dropped. Em dashes rationed to
  near-zero in the translation (ch03 shipped with zero; a parenthetical gloss
  year uses parentheses, not dashes).
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts.
  Keep the warmth and the edge. In ch03 the friend-making impresario ("two
  million friends"; seven days hosting Deng Baoshan).
- **Zhou Enlai:** measured, precise, terse when sharp; a man of "feeling and
  honor." The presiding figure of ch03 — the 八办 network, the Chongqing work,
  the idle-chessmen deep agents, "making friends widely." Warmth and tradecraft
  are the through-line.
- **Chiang Kai-shek ("the Generalissimo" / "old Chiang"):** declarative,
  strategic, cold, ruthless (orders Xuan Xiafu killed to keep his grip on Hu
  Zongnan). Render 老蒋 as "Chiang" / "the Generalissimo" to carry the register.
- **Xu Enzeng (memoir), Zhang Yanfo (confession-memoir), Dimitrov (directive),
  Zhuo Lin / interviewees (written recollection):** formal document/reminiscence
  register, kept formal but never wooden.
- **Deng Xiaoping (reflective aside, ch02):** warm, plain, unhurried.

## Where the story stands

Chapters 1-2 carried the CCP hidden front from 1927 through the shaping of the
Yan'an security state. Chapter 3 ("从'地下'到'地上'") is now COMPLETE: the Eighth
Route Army offices blossoming across Nationalist China as open cover for secret
intelligence, and Li Kenong building and then winding them up (s1); Xu Enzeng's
"contact chart" of Zhou Enlai's Chongqing web and the three-line open/underground/
intelligence design (s2); the "idle chessmen" and "strategic spies" — Xiong
Xianghui inside Hu Zongnan, the "Latter Three Heroes," Xie Hegeng and Liu
Zhongrong on Bai Chongxi, Shen Anna the stenographer (s3); the money problem and
the Party's "companies," Guangda Huaxing and the birth of China Resources (s4);
the "overseas work" — Tan Kah Kee, the South Seas resistance, the international
intelligence links to Stilwell's observer groups (s5); the great contest in
Xi'an over the Qixianzhuang office and the assassination of Xuan Xiafu (s6); and
Zhou Enlai's intelligence method — "making friends widely," Mao's own hand on the
38th Army (s7). Chapter 4 ("拔钉子" / "Pulling Out the Nails") turns to the covert
struggle to secure the Border Region itself: "dual regimes," the contest over
informers, the "Red Sherlock Holmes," the anti-corruption storm, and "escorting"
agents out.

## Open traps and environment

- **Section tails straddle pages AND one-line punch paragraphs hide on figure
  pages.** Read PAST each section heading and each plate; split the merged
  one-liners back out (bit us in B02-B04).
- **zh scaffolding under-segments on figure pages.** Re-segment with a scripted
  bridge (resegment_ch04.py, modeled on resegment_ch03.py) to reach 1:1 parity.
  NOT idempotent — re-run assemble before each resegment run.
- **Number check is noisy** (OCR-lossy zh; 八办/八路军/七贤庄, dates, decade
  labels, name numerals). Run via verify_unit (it passes --noise data/noise.txt),
  extend noise.txt, and verify every quantity against the SCAN. Digits for
  load-bearing figures and unit designations per STYLE. B04 caught a dropped
  "22nd Army", a "14th"-for-"4th" regiment, a "dozen"-for-"twenty" — the check
  earns its keep; read its real-quantity flags.
- **check_content is N/A** to this project's book.json schema. Rely on
  check_align + parity + the manual zh<->en read.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; catalog them in PROGRESS as a deliberate decision. The standing
  question (every photo, or a curated subset) is still for the commissioner.
- **Source notes are PER-CHAPTER** (主要资料). Chapter 4's fall at the end of
  section 5; render as a translated "Principal Sources" section.
- **Printed-page markers**: ch03 has NONE (pagemap deleted — stale post-resegment
  indices; see PROGRESS B04). A clean full-chapter pagemap rebuild is a
  corrections-pass task; do not let it block B05. ch01 zh parity 269/299 (from
  B01) also still open. No note cites a ch03 folio, so nothing depends on it.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B04 completion
reply in chat, as CLAUDE.md requires.
