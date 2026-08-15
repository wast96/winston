# HANDOFF — China's Secret War (中国秘密战)

B02 (Chapter 2, sections 1-5) is translated, built, and QA-clean. The frozen
voice reference is still out/ch01_reading.md. The kickoff below is for B03
(Chapter 2, sections 6-8).

## Message to paste into the next chat

```
China's Secret War B03

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B03 = Chapter 2, sections 6-8 (ch02s06-ch02s08), end to end per the
CLAUDE.md pipeline. PDF pages 109-133; printed pages 73-97 (offset constant:
printed = pdf - 36; spot-verify each section opener's folio off the scan).
NOTE: book.json lists B03 pdf_range [104,133], but 104-108 is section 5, which
was completed in B02 (including section 5's four-paragraph tail on PDF 109,
printed 73, before the section-6 heading). B03's real scope is sections 6-8 =
PDF 109-133. Section 6 (知青进入特训班 / Educated Youth Enter the Special
Training Class) opens at PDF 109 / printed 73; section 7 (延安防线) at PDF 120 /
printed 84; section 8 (大布局) at PDF 124 / printed 88; Chapter 3 opens at PDF
134 / printed 98, which is your stop. Simplified Chinese, horizontal; chi_sim,
psm 6; PaddleOCR absent, use scripts/ocr_dual.py.

The pipeline is established (see PROGRESS "Pipeline established" in B01 and the
do-not-revert list below); reuse it, do not re-measure. Recipe:
render 109 133 --dpi 300 -> ocr_crop 109 133 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 109 133 ->
indents 109 133 -> add the section 6/7/8 heading strings (as the OCR reads
them) to data/structure.json -> assemble ch02b03 109 133 --offset 36
--blank-assist (use a SEPARATE zh scaffold id so you do not clobber
data/zh/ch02.txt, then reconcile against the section 6-8 span of
out/ch02_reading.md) -> find_figures (the 图文版 has many inline photos; see
the figures decision below) -> translate, APPENDING sections 6-8 to
out/ch02_reading.md after section 5 -> verify_unit / check_align / qc_entities
on the appended span (the whole-chapter zh scaffolding is figure-heavy and
under-segments; expect to re-segment as in B02, scripts/resegment_ch02.py is
the model) -> apparatus_merge for notes and glossary -> build EPUB -> qa_epub
(green) and epubcheck (clean) -> check_register --ref out/ch01_reading.md
out/ch02_reading.md (ch01 is the FROZEN reference; the dialogue metric is noise
in low-dialogue units, judge on the narratorial signals) -> write PROGRESS and
the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of section 5
(out/ch02_reading.md, the Zhou Xing / Zhao Cangbi / Li Qiming cadre portraits)
for the voice; consult the VOICE SHEETS and glossary in this HANDOFF. Cite the
book's PRINTED folios in notes, never PDF pages. Never invent bridging text: if
OCR cuts off, crop the scan and read the real continuation. WATCH THE SECTION
TAILS: a section's last paragraphs often straddle onto the NEXT section's
opening page before the heading (this bit twice in B02); read past each heading
to be sure you have the whole preceding section. Verify every name, number, and
unit designation by crop before writing; render load-bearing figures and unit
designations in DIGITS (the 24th Division, 518, 25,000 li) per STYLE. State
corroborated/uncorroborated/contradicted in notes; the partisan voice is
content, the counter-record goes in the footnote.

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
  ch01 is the FROZEN voice reference. Voice gate passed (B01 revision applied:
  "loyalty to effect, not texture").
- **B02 = Chapter 2, sections 1-5 (ch02s01-ch02s05).** 167 English body
  paragraphs. verify_unit parity 167/167, 18 notes, 10 glossary rows; qa_epub
  PASS; epubcheck 0/0/0. See PROGRESS "Batch B02" for the full record,
  including the batch-boundary correction (sections 1-5 = PDF 82-108 plus
  section 5's tail on PDF 109, NOT the "82-103" the B01 kickoff wrote).

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop overrides for mirror-margin books;
  measured box recto/odd [0.07, 0.86], verso/even [0.17, 0.94], top 0.045,
  bottom 0.93. chi_sim, psm 6.
- **scripts/assemble.py**: --blank-assist (blank-line signal layered on the
  indent, gated by sentence-end) for figure-heavy pages.
- **scripts/apply_fixes.py --txt + data/txt_fixes.json**: pre-assembly per-page
  OCR fixes affecting paragraph segmentation.
- **scripts/build_reading_epub.py**: render_glossary handles flat rows; and
  (B02) sec_nav omits a pending section from the nav of a PARTIALLY translated
  chapter (epubcheck NAV-011 / nav content-model fix). Chapter 2 is the first
  partially translated chapter, so this matters from B03 on too.
- **scripts/make_bilingual.py, scripts/check_align.py**: both now skip the
  '***' scene-break marker (B02), matching verify_unit / check_structure.
- **scripts/resegment_ch02.py**: the reproducible zh re-segmentation for the
  figure-heavy ch02 pages (B02). Model it for B03's sections 6-8.
- Do NOT re-measure the crop box; do NOT revert any of the above.

## Renderings settled and carry-forward

glossary.json now has 33 rows: the B01 cast/organs plus B02's additions (Pan
Hannian, Zhang Guotao, Hu Zongnan, Zhou Xing, Xu Enzeng, Chen Lifu, Wang Ming,
Kang Shichang; Central Social Affairs Department, Shaanxi-Gansu-Ningxia Border
Region Security Office). Consult glossary.json and authority.json BEFORE
romanizing any recurring name. Handles fixed this batch and to KEEP: the Social
Affairs Department (中社部, "Zhongshebu"); the Border Security (边保) for
陕甘宁边区保安处; the Central Intelligence Department (中情部); Zhao Rong =
Kang Sheng (reveal handled in s4); the garrison/security regiment (保安团);
the Garrison Corps (留守兵团). Kang Sheng's original name printed as 张旺 (used
张宗可 etc.), rendered "born Zhang Wang"; the glossary's ch01 note gives Zhang
Zongke, they are consistent (张宗可 is one of the used names). "Border Police"
(边警), "black dogs" (黑狗子 = KMT police), the "far country" (远方 = USSR /
Comintern) glossed inline. Chapter 2's subtitle folds into the chapter title_en
("Secret War: The Hidden Struggle Within a United Front"), so no separate
subtitle heading in the reading file.

VOICE SHEETS (start here; extend as characters speak in later sections):
- **Narrator (Hao Zaijin):** brisk narrative-nonfiction reportage; anaphora
  chains, one-line punch paragraphs, rhetorical questions kept sparingly,
  datebook chronology staccato, the inclusive "we." Runs HOT in the political
  set-pieces (the Kang Sheng portrait, "only Yan'an was pure ground for the
  nation") and turns SARDONIC on the enemy and on turncoats-become-officials;
  keep both. Partisan by design; counter-record lives in the footnotes.
  Exclamation rationed hard (period by default; keep only inside quoted speech
  and the rarest authorial outburst); most rhetorical questions converted to
  statements; the "so it turns out" reveal wrappers dropped.
- **Mao Zedong:** earthy, aphoristic ("old Mao," "Marshal Mao" as Xu Shiyou
  calls him). In s3 he charges Xu Shiyou warmly; in s4 his airport welcome
  ("immortals come down from the Kunlun Mountains") overflows. Keep the warmth.
- **Zhou Enlai:** measured, precise, terse when sharp ("You may be muddled.
  I'm not."). Little direct speech.
- **Chiang Kai-shek:** declarative, strategic, cold ("Japan is no more than a
  skin rash; the Communist Party is the disease in our vitals").
- **Xu Enzeng (memoir), Dimitrov (directive):** formal document register, kept
  formal.
- (Kang Sheng, gangster and provincial-cadre voices: not yet at length; build
  their sheets when they speak.)

## Where the story stands

Chapter 1 carried the CCP hidden front from 1927 to the eve of the war.
Chapter 2 ("暗战") opens the united-front years: Zhou Enlai's brush with death
at Laoshan and the tightening of Yan'an security (s1); the formal shaping of
Zhongtong and Juntong and Chiang's blockade of the Border Region, against the
CCP's three secret routes and its beacon-pull on the nation's youth (s2); the
defection incidents, Zhang Guotao's flight and the turncoats-become-Nationalist-
officials (s3); the founding of the Central Social Affairs Department under Kang
Sheng, with the Pan Hannian and Li Kenong portraits (s4); and the structure of
the Border Region Security Office ("Bianbao"), the Yan'an police, the security
regiment, and the three cadre types embodied by Zhou Xing, Zhao Cangbi, and Li
Qiming (s5). B03 continues: the "'38-style" educated youth entering the special
training classes (s6), the Yan'an defense line (s7), and the grand deployment
(s8).

## Open traps and environment

- **Section tails straddle pages.** Twice in B02 a section's closing paragraphs
  sat on the NEXT section's opening page before its heading (s1 -> printed 51,
  s4 -> printed 68). ALWAYS read past each section heading to confirm you have
  the whole preceding section. This is the "tail is where faithfulness fails"
  rule; the zh<->en parity audit is what catches it.
- **zh scaffolding under-segments on figure pages.** assemble.py merges
  paragraphs where inline photos desync the indent/blank signals. B02 gave 137
  vs 167; reconciled with scripts/resegment_ch02.py. Expect the same for s6-8
  and re-segment; keep the ch02 reading file the tracked correction surface.
- **ch01 zh parity still unresolved** (zh 269 vs en 299, KNOWN ISSUE from B01).
  The B02 re-segmentation approach (split merged paragraphs at anchors, record
  a reproducible script) is the model for closing it; commissioner's call
  whether to do it now or in a corrections pass.
- **Figures deferred** (figures.json empty). ~14 inline photo groups on the B02
  pages catalogued in PROGRESS. The standing decision for all 图文 chapters
  (every photo, or a curated subset) is pending for the commissioner. There is
  also a Shaan-Gan-Ning MAP on printed 39 (ch01) worth keeping.
- **Source notes are PER-CHAPTER** (a 主要资料 / Principal Sources section ends
  each chapter). Chapter 2's will fall at the end of section 8 (B03); render it
  as a translated "Principal Sources" section, same treatment as ch01.
- **Number check is noisy on this book** because the zh scaffolding is OCR-lossy
  (mangled digits, embedded caption numbers, name numerals) and English spells
  out numbers over thirteen. Verify quantities against the SCAN; use digits for
  load-bearing figures and unit designations per STYLE.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run
  via java -jar). The setup regression test "hook stands down on template stub"
  FAILS benignly now that HANDOFF holds a real kickoff (not a defect).

The kickoff message above is repeated verbatim at the end of the B02 completion
reply in chat, as CLAUDE.md requires.
