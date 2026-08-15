# HANDOFF — China's Secret War (中国秘密战)

B03 (Chapter 2, sections 6-8, plus Chapter 2's Principal Sources) is translated,
built, and QA-clean. Chapter 2 is now COMPLETE. The frozen voice reference is
still out/ch01_reading.md. The kickoff below is for B04 (Chapter 3, the whole
chapter).

## Message to paste into the next chat

```
China's Secret War B04

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B04 = Chapter 3 (第三章 从"地下"到"地上" / From "Underground" to
"Aboveground"), the whole chapter, ch03s01-ch03s07, end to end per the CLAUDE.md
pipeline. PDF pages 134-170; printed pages 98-134 (offset constant: printed =
pdf - 36; spot-verify each section opener's folio off the scan). Section openers:
s1 遍地开花的"八办" (The "Eighth Route Army Offices" Blossom Everywhere) PDF 134 /
printed 98; s2 绝密的"重庆联络图" PDF 141 / printed 105; s3 "闲棋冷子"与"战略间谍"
PDF 144 / printed 108; s4 为党赚钱的"公司" PDF 150 / printed 114; s5 遥远的"海外
工作" PDF 154 / printed 118; s6 西安大斗法的谜底 PDF 158 / printed 122; s7 周恩来
的情报搜集方式——广交朋友 PDF 164 / printed 128. Chapter 4 opens at PDF 171 /
printed 135, which is your stop. Chapter 3 carries its OWN chapter-end Principal
Sources (主要资料); render it as a translated "### Principal Sources" section, same
treatment as ch01 and ch02. Simplified Chinese, horizontal; chi_sim, psm 6;
PaddleOCR absent, use scripts/ocr_dual.py.

The pipeline is established (see PROGRESS "Pipeline established" in B01 and the
do-not-revert list below); reuse it, do not re-measure. Recipe:
render 134 170 --dpi 300 -> ocr_crop 134 170 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 134 170 ->
indents 134 170 -> add the chapter title, subtitle, and section 1-7 heading
strings (as the OCR reads them) to data/structure.json -> assemble ch03 134 170
--offset 36 --blank-assist -> find_figures (the 图文版 has many inline photos;
figures remain DEFERRED, see below) -> translate to out/ch03_reading.md, one
paragraph per TRUE source paragraph (read every page off the scan; the 图文
pages under-segment, so expect to re-segment the zh as in B02/B03 —
scripts/resegment_ch02b03.py is the model; write scripts/resegment_ch03.py) ->
verify_unit ch03 / check_align ch03 / qc_entities on out/ch03_bilingual.md
(check_content is N/A to this project's schema; the number check is noisy on this
book, run with --noise data/noise.txt and verify quantities against the SCAN) ->
apparatus_merge for notes and glossary -> build EPUB -> qa_epub (green) and
epubcheck (clean) -> check_register --ref out/ch01_reading.md out/ch03_reading.md
(ch01 is the FROZEN reference; the dialogue metric is noise in low-dialogue
units, judge on the narratorial signals) -> write PROGRESS and the next
HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of Chapter 2
(out/ch02_reading.md, section 8's "grand deployment" close and the Principal
Sources) for the voice; consult the VOICE SHEETS and glossary in this HANDOFF.
Cite the book's PRINTED folios in notes, never PDF pages. Never invent bridging
text: if OCR cuts off, crop the scan and read the real continuation. WATCH THE
SECTION TAILS: a section's last paragraphs often straddle onto the NEXT section's
opening page before the heading (this bit in B02 and B03; read past each heading
to be sure you have the whole preceding section). Verify every name, number, and
unit designation by crop before writing; render load-bearing figures and unit
designations in DIGITS (the 18th Group Army, the 24th Division, 25,000 li) per
STYLE. State corroborated/uncorroborated/contradicted in notes; the partisan
voice is content, the counter-record goes in the footnote.

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
- **B02 = Chapter 2, sections 1-5.** 167 English body paragraphs. See PROGRESS
  "Batch B02."
- **B03 = Chapter 2, sections 6-8 + Chapter 2 Principal Sources.** +172 English
  body paragraphs (ch02 now 339 total). verify_unit parity 172/172; +18 notes
  (ch02 total 36, book total 57); +22 glossary rows (55 total); qa_epub PASS;
  epubcheck 0/0/0. **Chapter 2 is COMPLETE.** See PROGRESS "Batch B03."

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop for mirror-margin books; measured box
  recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045, bottom 0.93.
  chi_sim, psm 6.
- **scripts/assemble.py**: --blank-assist (blank-line signal layered on the
  indent, gated by sentence-end) for figure-heavy pages.
- **scripts/apply_fixes.py --txt + data/txt_fixes.json**: pre-assembly per-page
  OCR fixes affecting paragraph segmentation.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; sec_nav
  omits a pending section from the nav of a PARTIALLY translated chapter
  (epubcheck NAV-011 fix). Chapter 3 will again be partially translated during
  the batch, so this matters.
- **scripts/make_bilingual.py, scripts/check_align.py**: both skip the '***'
  scene-break marker, matching verify_unit / check_structure.
- **scripts/resegment_ch02.py, scripts/resegment_ch02b03.py**: the reproducible
  zh re-segmentation for the figure-heavy ch02 pages. Model resegment_ch03.py on
  the B03 one (drop-nothing this time, since ch03 is a fresh chapter with no
  carried-in tail; splits/merges by garbled-OCR anchors; insert the Principal
  Sources heading).
- **data/noise.txt**: carries this book's number-check noise rules; extend it
  (longest-first, each commented) as new idioms/place-names surface.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 55 rows. Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Chapter 3 will re-use many existing rows heavily:
Zhou Enlai, Li Kenong, Pan Hannian, Ye Jianying, Dong Biwu, Wu Kejian (in
glossary? Wu Kejian is NOT yet a row — add if he recurs), Zhang Xueliang,
Chiang Kai-shek, Dai Li, Zhongtong, Juntong, the Social Affairs Department,
the Border Security. Handles to KEEP fixed: the Social Affairs Department (中社部,
"Zhongshebu"); the Border Security (边保) for 陕甘宁边区保安处; the Eighth Route
Army Office / "八办" (gloss the abbreviation at first use in ch03); one handle per
organ forever.

CONSISTENCY LEDGER points (do not re-decide):
- 杜理卿 (Du Liqing) = 许建国 (Xu Jianguo) are ONE man; render "Du Liqing" where
  the book uses the original name, "Xu Jianguo" otherwise (glossary row records
  it).
- Kang Sheng's alias Zhao Rong; born Zhang Zongke / Zhang Wang (settled in B01).
- "black dogs" (黑狗子 = KMT police), the "far country" (远方 = USSR / Comintern),
  the "'38-style" cadre, "living at the station" (住机关) — all glossed already.
- Chapter titles' subtitles fold into title_en in book.json; no separate subtitle
  heading in the reading file (confirmed for ch01, ch02; do the same for ch03).

VOICE SHEETS (start here; extend as characters speak):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line punch paragraphs, rhetorical questions kept sparingly (only
  where they land in English), datebook chronology staccato, the inclusive "we."
  Runs HOT in the political set-pieces and SARDONIC on the enemy and on
  turncoats-become-officials; keep both. Partisan by design; counter-record lives
  in the footnotes. Exclamation rationed hard (period by default); most
  rhetorical questions converted to statements; "so it turns out" reveal wrappers
  dropped. Em dashes rationed to near-zero in the translation.
- **Mao Zedong:** earthy, aphoristic, warm; pleased with himself when he boasts
  ("Yan'an's police... first in China"). Keep the warmth and the edge.
- **Zhou Enlai:** measured, precise, terse when sharp. Little direct speech.
  Chapter 3 is heavily Zhou-centered (the "八办" network, the Chongqing work,
  "making friends widely") — his tradecraft and warmth are the through-line.
- **Chiang Kai-shek:** declarative, strategic, cold.
- **Xu Enzeng (memoir), Dimitrov (directive), Zhuo Lin (written recollection):**
  formal document/reminiscence register, kept formal but never wooden.
- **Deng Xiaoping (reflective aside):** warm, plain, unhurried ("Chairman Mao...
  always protected me... his merits always outweighed his faults").

## Where the story stands

Chapter 1 carried the CCP hidden front from 1927 to the eve of the war. Chapter 2
("暗战") is now COMPLETE: Zhou Enlai's brush with death at Laoshan and the
tightening of Yan'an security (s1); the shaping of Zhongtong and Juntong and
Chiang's blockade (s2); the defection incidents and Zhang Guotao's flight (s3);
the founding of the Central Social Affairs Department under Kang Sheng (s4); the
Border Region Security Office, the Yan'an police, and the three cadre types
(s5); the "'38-style" educated youth entering the special training classes, with
the Deng Xiaoping / Zhuo Lin match, the Whampoa-of-security camp at Qilipu, and
the Huang Kegong case (s6); the Yan'an defense line of checkpoints, cover points,
and the plainclothes squad, capped by the model people's-police story (s7); and
the "grand deployment" — Mao's one long talk on security work, the shift from
Soviet vertical command to Party collective leadership, and the intelligence
system spreading to Jin-Sui, Jin-Cha-Ji, Chongqing, and the occupied cities (s8).
Chapter 3 ("从'地下'到'地上'") turns to the open-and-secret method: the Eighth
Route Army Offices blossoming across the country as cover for intelligence work,
the Chongqing network, strategic spies, the Party's money-making "companies,"
overseas work, the Xi'an contest, and Zhou Enlai's friendship-based tradecraft.

## Open traps and environment

- **Section tails straddle pages.** Read PAST each section heading to confirm you
  have the whole preceding section (bit us in B02 and B03).
- **zh scaffolding under-segments on figure pages.** assemble.py merges
  paragraphs where inline photos desync the indent/blank signals; giant merged
  OCR lines appear at every plate. Re-segment with a scripted bridge
  (resegment_ch03.py, modeled on resegment_ch02b03.py) to reach 1:1 parity.
- **Number check is noisy** (OCR-lossy zh; li-names like 八办/七里铺, idioms like
  老百姓/万岁 read as quantities). Run with --noise data/noise.txt, extend it,
  and verify every quantity against the SCAN. Use digits for load-bearing
  figures and unit designations per STYLE.
- **check_content is N/A** to this project's book.json schema (it expects a
  docs/sources layout; we use `structure`). Rely on check_align + parity + the
  manual zh<->en read.
- **Figures DEFERRED** (figures.json empty). Every 图文 chapter carries inline
  photos; catalog them in PROGRESS as a deliberate decision. The standing
  question (every photo, or a curated subset) is still for the commissioner.
  Maps are worth keeping (ch01 Shaan-Gan-Ning map, the ch02 checkpoint map).
- **Source notes are PER-CHAPTER** (主要资料). Chapter 3's fall at the end of
  section 7; render as a translated "Principal Sources" section.
- **ch01 zh parity still open** (zh 269 vs en 299, KNOWN from B01). B02/B03's
  re-segmentation approach is the model to close it; commissioner's call whether
  now or in a corrections pass.
- **Printed-page markers** cover only printed 46-72 for ch02 (s6-8, printed
  73-97, lack folio markers; the s5/s6 tail-straddle tangles the pagemap). No
  note cites those folios. A clean full-chapter pagemap rebuild is a corrections-
  pass task; do not let it block B04.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run via
  java -jar; setup.sh fetches it). The setup regression test "hook stands down on
  template stub" FAILS benignly now that HANDOFF holds a real kickoff.

The kickoff message above is repeated verbatim at the end of the B03 completion
reply in chat, as CLAUDE.md requires.
