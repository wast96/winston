# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

B01 has STOPPED at the first-chapter voice gate (Step 0c) and is awaiting the
commissioner's judgement of voice, note density, and formatting. Per the
workflow there is deliberately NO next-batch kickoff yet: the B02 kickoff is
written only AFTER the commissioner approves the voice, at which point ch001
freezes as the register reference for the whole book
(check_register.py --ref out/ch001_reading.md) and B02 begins in a fresh chat.

On approval, the B02 kickoff to write here (and paste into the next chat) is:
Scales and Claws B02, do ch002-ch014 (PDF 34-58, printed 32-56) end to end
per the CLAUDE.md pipeline; BEFORE translating, read the final two pages of
out/ch001_reading.md (the frozen voice); run check_register.py --ref
out/ch001_reading.md every unit; cite printed folios; never invent bridging
text; deliver the EPUB in chat and paste the following batch's kickoff.

If the commissioner instead sends corrections to B01, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B02.

## What is DONE (do not redo)

- Survey (2026-08-10): source characterized, book.json complete, skeleton EPUB
  green, batch plan + 3 standing decisions approved, photos ruled IN.
- B01 (2026-08-11): ch000 (序, Author's Preface) + ch001 (上海人的過年忙, The
  New Year Rush) translated end to end. All checks green (verify_unit,
  check_numbers, check_align, check_content, qc_entities, check_structure,
  check_apparatus); qa_epub PASS; epubcheck 5.1.0 clean. 25 notes (7+18),
  22 glossary rows, 5 figures. See PROGRESS.md for the full log. AWAITING the
  voice-gate decision — do not start B02 until it is given.

## Tooling in place (do not revert)

- OCR: tesseract chi_tra_vert --psm 5 only (PaddleOCR absent). ocr_dual.py is
  NOT usable on this book (hardwired chi_sim + horizontal psm 6/4 = wrong
  script/orientation); do not run it expecting a signal. On this
  vertical-Traditional reset tesseract is ~85% accurate, so B01 was fully
  eye-read at magnification and data/zh hand-corrected against the scans.
- ocr_crop.py crop for this book: --left 0.03 --right 0.97 --top 0.13
  --lang chi_tra_vert --psm 5; --bottom is PAGE-TYPE dependent (full-text
  pages ~0.95; photo pages ~0.51-0.56 to exclude the reprint photo band).
- indents.py is HORIZONTAL-only and errors on this vertical book
  (ocr_crop.folio_present missing); do NOT rely on it. assemble.py runs on the
  blank-line signal; paragraph structure is finalized by hand. data/indent/
  intentionally empty for this book.
- scripts/check_content.py name_map PATCHED to skip '_'-prefixed keys and
  non-dict values (crashed on glossary "_about"). DO NOT REVERT.
- check_config.json (tracked): {docs,sources,notes,variants} for
  check_structure/check_content, filtered to BUILT units; REGENERATE it as
  each batch adds units (see the one-liner in PROGRESS B01).
- data/noise.txt: 萬事如意, 百貨 added (idiom/compound; reasons in-file).
- data/ocr_fixes.json: crop-verified readings ledger (audit trail; NOT a full
  reconstruction — see the reproducibility note in PROGRESS).

## Renderings settled / carry-forward

- Voice (freezes at gate approval): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, author
  editorializing. Subsection topic-labels = ITALIC run-in leads (builder
  supports *italic* only, not bold; #### would break the heading-shape gate).
- Money policy (shelf-relevant, recurs book-wide): 塊/元 = "dollar"; 毛 = the
  period unit "*mao*" kept romanized (preserves the numeral for check_numbers;
  footnoted once at first appearance); 小洋 = "small silver"; 大洋 = the big
  standard dollar. Do NOT flatten 毛 to "cents".
- Shelf-consistent names (from authority.json): 南京路 Nanjing Road, 南市
  Nanshi, 捕房 police station. Author 郁慕俠 = Yu Muxia (principal). Preface
  author 天虛我生 = Chen Diexian (1879-1940).
- Glossary decided this batch: 財神 God of Wealth, 接路頭 Welcoming the God of
  Wealth, 元宵 Lantern Festival, 元旦 New Year's Day (lunar), 錢莊 native bank,
  租界 the Settlement, 城隍廟 City God Temple, 虹廟 Hong Temple, 菩薩 the
  Bodhisattva, 元寶茶 Ingot Tea, 壓歲錢 lucky money. Reuse verbatim; grep
  before re-noting (recurring subjects get their note at FIRST appearance).
- No continuing cast yet (essay collection); no voice sheets needed.

## Where the book stands

- Two units translated (preface + one essay). 166 essays remain. No plot to
  track; register decisions in B01 govern everything downstream.

## Next batch scope

- B02 (after gate approval) = ch002-ch014, PDF 34-58, printed 32-56. These are
  the "press/politics" cluster (宋案, 戴季陶, 章太炎, 康有為, newspapers,
  文化街, 新劇, 跳舞); expect proper names and 1910s-20s politics needing
  fact-checks. Refine the provisional English titles against the essay bodies.

## Open traps and environment state

- This is the 2019 RESET, not the 1933 original: no collation source. Where the
  reprint is suspect, note it; do not guess at the 1933 reading. ch001's
  internal dating (~1935-36) already runs ahead of the 1933 imprint — footnoted
  honestly, unresolved.
- Vertical RTL OCR column-order errors are silent; verify assemble output by
  eye. Photo-band OCR corrupts paragraphing; keep it out of the crop.
- Two essays share PDF 214 (ch135/ch136) and two share PDF 218 (ch140/ch141):
  unit boundaries mid-page (B08/B10), watch the parity split.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset
  printed = pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template
  stub") — a template-only fixture assumption now that HANDOFF carries a real
  kickoff; the hook is working as designed. See PROGRESS.
