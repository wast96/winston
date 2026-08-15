# HANDOFF — China's Secret War (中国秘密战)

B01 (Preface + Chapter 1) is translated, built, and QA-clean, and is stopped
at the first-chapter VOICE GATE (CLAUDE.md Step 0c). The commissioner judges
voice, note density, and formatting on ch00 + ch01 before B02 begins. The
kickoff below is for B02, to paste AFTER the voice gate is approved.

## Message to paste into the next chat

```
China's Secret War B02

Read CLAUDE.md, then this HANDOFF.md, then book.json, then STYLE.md. Then do
batch B02 = Chapter 2, sections 1-5 (ch02s01-ch02s05), end to end per the
CLAUDE.md pipeline. PDF pages 82-103; printed pages 46-72 (offset constant:
printed = pdf - 36; spot-verify each section opener's folio off the scan).
Simplified Chinese, horizontal; chi_sim, psm 6; PaddleOCR absent, use
scripts/ocr_dual.py.

The pipeline is established (see PROGRESS "Pipeline established" and the
do-not-revert list below); reuse it, do not re-measure. Recipe:
render 82 103 --dpi 300 -> ocr_crop 82 103 with the MEASURED per-parity crop
(recto/odd [--left 0.07 --right 0.86], verso/even [--left-even 0.17
--right-even 0.94], shared --top 0.045 --bottom 0.93, --lang chi_sim --psm 6,
--running-head "中国秘密战——中共情报保卫工作纪实") -> ocr_dual 82 103 ->
indents 82 103 -> assemble ch02 82 103 --offset 36 --blank-assist -> then, if
sentence-ender OCR mangles (fullwidth ！/？ read as digits) merge paragraphs,
add them to data/txt_fixes.json and run apply_fixes.py --txt, re-assemble ->
find_figures (the 图文版 has many inline photos; see the figures decision
below) -> translate to out/ch02_reading.md (one English paragraph per TRUE
source paragraph, read every page off the scan) -> apply_fixes ch02 ->
verify_unit ch02 / check_align / check_content / qc_entities -> apparatus_merge
for notes and glossary -> build EPUB -> qa_epub (green) and epubcheck ->
check_register --ref out/ch01_reading.md out/ch02_reading.md (ch01 is the
FROZEN reference) -> write PROGRESS and the next HANDOFF/kickoff -> commit.

BEFORE translating, read the final two English pages of ch01
(out/ch01_reading.md) for the voice; consult the VOICE SHEETS and glossary in
this HANDOFF. Cite the book's PRINTED folios in notes, never PDF pages. Never
invent bridging text: if OCR cuts off, crop the scan and read the real
continuation. Verify every name, number, and unit designation by crop before
writing. State corroborated/uncorroborated/contradicted in notes; the
partisan voice is content, the counter-record goes in the footnote.

Also carry forward two OPEN ITEMS from B01 (do them or fold into a corrections
pass, commissioner's call): (1) reconcile ch01 zh parity (zh 269 vs en 299;
hand-split the figure-page merges in data/zh/ch01.txt to 299 and record the
splits in data/ocr_fixes.json, then rerun verify_unit/check_content/
qc_entities), and (2) the figures decision (whether to extract every inline
photo across the 图文 chapters or a curated subset).

Do NOT pause for approval mid-batch. Deliver the EPUB in chat and paste the
next kickoff verbatim in the same reply.

Work on branch claude/chinas-secret-war only (CLAUDE.md rule 2); expect a
stray per-task branch at session start and consolidate onto the canonical
branch.
```

## What is DONE

- **Survey (Step 0a + 0b), approved.** book.json carries full metadata and the
  complete structure (12 chapters, 86 sections, + Preface + Afterword).
- **B01 = Preface (ch00) + Chapter 1 (ch01).** Both translated. ch00 verify
  CLEAN. ch01 built with 19 notes + 17 glossary rows; qa_epub PASS; epubcheck
  0/0/0. ch01 is the FROZEN voice reference. One open item: ch01 zh parity
  (see PROGRESS "KNOWN ISSUE"). Stopped at the voice gate.

## Tooling in place (do NOT revert)

- **scripts/ocr_crop.py**: per-parity crop overrides (--left-even/--right-even/
  --top-even/--bottom-even) for mirror-margin books; folio_present() (geometric
  folio test that indents.py calls; it was referenced but missing).
- **scripts/assemble.py**: --blank-assist (blank-line paragraph signal layered
  on the indent, gated by sentence-end), for the figure-heavy pages.
- **scripts/apply_fixes.py**: --txt mode + data/txt_fixes.json, pre-assembly
  per-page OCR fixes that affect paragraph segmentation.
- **scripts/build_reading_epub.py**: render_glossary handles BOTH sectioned and
  FLAT glossary rows (apparatus_merge writes flat), so no manual re-sectioning
  each batch.
- Measured crop box (do not re-measure): recto/odd [0.07, 0.86], verso/even
  [0.17, 0.94], top 0.045, bottom 0.93. chi_sim, psm 6.

## Renderings settled this batch (glossary) and carry-forward

glossary.json now has the principal cast and the core organs/terms; consult it
and authority.json BEFORE romanizing any recurring name. Settled: Zhou Enlai,
Mao Zedong, Zhu De, Chen Geng, Gu Shunzhang, Kang Sheng (alias Zhao Rong), Li
Kenong / Qian Zhuangfei / Hu Di (the Longtan Three), Chiang Kai-shek, Dai Li,
Zhang Xueliang; Central Special Branch (中央特科), State Political Security
Bureau (国家政治保卫局), Zhongtong (中统), Juntong (军统), tewu (特务, rendered
by sense; kept as tewu where discussed as a word). "Special Work Section"
(特务工作科), "Red Squad" / dog-beating squad (红队/打狗队), "Border Region"
(边区), suppression (肃反), "coerce, confess, believe" (逼供信).

VOICE SHEETS (start here; extend as characters speak in later chapters):
- **Narrator (Hao Zaijin):** brisk, buttonholing reportage. Anaphora chains
  ("Who knew... Who imagined..."), one-line punch paragraphs with exclamation,
  rhetorical questions kept as questions, datebook chronology kept staccato,
  the inclusive "we," recurring treasure/deep-water/wuxia-manual metaphors.
  Runs hot in the political asides; keep the heat. Partisan by design (special
  agent = enemy; our side = ours); the counter-record lives in the footnotes.
- **Mao Zedong:** earthy, aphoristic, vivid images ("chives grow back, a head
  does not"; "betting in a glass cup"; "thousand-li eye and downwind ear").
  Confident, didactic when teaching. Canonical quotes use the received English.
- **Zhou Enlai:** measured, precise, the organizer; little direct speech so far.
- (Kang Sheng, Chiang Kai-shek, gangster and cadre voices: not yet spoken at
  length; build their sheets when they do.)

## Where the story stands

Chapter 1 has carried the CCP hidden front from its birth in the 1927 terror
(the Special Work Section, then the Central Special Branch under Zhou Enlai in
Shanghai) through the Gu Shunzhang defection and the Longtan Three, the State
Political Security Bureau of the Jiangxi Soviet, the Soviet-area purges (AB
Corps, Futian), the Long March SIGINT "trump card," the arrival in northern
Shaanxi and the halting of the Shaanbei purge, the secret channel to the
Second United Front and the Xi'an Incident, and the founding of the Border
Region Security Office at Yan'an on the eve of the war with Japan. Chapter 2
("暗战", the hidden struggle within the united front) opens with Zhou Enlai in
danger and the formal shaping of Zhongtong and Juntong.

## Open traps and environment

- **ch01 zh parity is unresolved** (zh 269 vs en 299). Top follow-up; see
  PROGRESS. Do not mistake it for a dropped-translation defect.
- **Figures deferred** (figures.json empty). Decision pending on scope for the
  图文 chapters. There is a Shaan-Gan-Ning MAP on printed 39 worth keeping.
- **Source notes are PER-CHAPTER** (a 主要资料 section ends each chapter), not
  only at the book's end as the survey assumed. Rendered as a translated
  "Principal Sources" section; keep this treatment consistent.
- **Source errors** stay as printed with a footnote stating the verdict (see
  PROGRESS list). Contested episodes: partisan text, counter-record in notes.
- Environment: OMP_THREAD_LIMIT=1 mandatory; kill the process GROUP, pgrep -c
  tesseract must read 0. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (run
  via java -jar). The setup regression test "hook stands down on template
  stub" FAILS benignly now that HANDOFF holds a real kickoff (not a defect).
- book.json B02 printed_range shows [46,72] while the s05 opener computes to
  printed 68; verify section openers off the scan at batch time.
