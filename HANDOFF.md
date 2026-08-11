# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

```
Scales and Claws B03

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu
Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; 2019 Taipei reprint,
customs volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the
harness to start you on a stray branch and consolidate per rule 2 (check out the
canonical branch, reset to origin, do the work there, delete the stray). This
book's PR history through B02 is already merged, so if the designated branch
carries only merged history, restart it from origin. Deliverable
out/scales-and-claws-of-shanghai.epub.

Do Batch B03 = ch015-ch034 (肉林秘聞 through 女相士; PDF 59-83, printed folios
57-81) end to end per the CLAUDE.md pipeline: ./setup.sh; render 59 83 --dpi 300;
OCR with the B01/B02 crop (ocr_crop.py --left 0.03 --right 0.97 --top 0.13
--lang chi_tra_vert --psm 5; set --bottom per page, tighter on any page that
carries a reprint photo so the photo band stays out of body OCR). tesseract on
this vertical-Traditional reset is only ~85% and too error-dense to trust:
EYE-READ every page at magnification and hand-transcribe data/zh against the
scans, exactly as B01/B02 did. indents.py is UNUSABLE here; assemble on the
blank-line signal and finalize paragraph structure BY HAND against the scan,
using the short-line signal at the page seams where the blank falls off the
page. pgrep -c tesseract must be 0 after OCR. Eyeball every page for
reprint-added photos and run each through the figure pipeline (crop to
data/figs/, alt text, caption translating the reprint label and stating
2019-editor provenance).

BEFORE translating, read the final two pages of out/ch014_reading.md: HANDOFF
describes the voice, but those pages ARE the voice; the FROZEN reference is
still out/ch001_reading.md. Run check_register.py --ref out/ch001_reading.md on
every unit. Consult glossary.json and authority.json BEFORE romanizing any
name. This cluster is the Shanghai demimonde: courtesan houses and their grades
(么二, 長三, 堂子), brothel slang and catchphrases, the tricks of the trade;
crop-verify every name, number, price and low-confidence span, recording
verified readings via apply_fixes.py. Fact-check any real person or institution
against real scholarship (Wikipedia / Baidu Baike / academic, NEVER an
LLM-written site); state the verdict in the note. Never invent bridging text;
verify each unit's tail against the scan.

NOTES: the commissioner wants them GENEROUS and dense, more rather than fewer.
Annotate freely wherever a non-specialist Western reader would miss anything
(what a courtesan grade or house-type is; a custom, a price in period money, a
piece of slang; texture lost in translation; the author as interested witness).
Recurring subjects get their note at FIRST appearance (grep notes.json and
earlier reading files first; keep the per-batch "NOT re-noted" list). Give 野雞
its full glossary decision here (its own chapters come later, but it recurs);
carry 舞女, 大洋, 小洋, 毛/角/分 per the settled money policy. Do not thin out
to hit a number.

Per unit: write out/<id>_reading.md (one paragraph per source line), then
make_bilingual.py, verify_unit.py, check_align.py; apparatus_merge.py for
notes/glossary/figures (glossary rows may now be SECTIONED in the batch file:
{"glossary": {"<zh>": {..., "section": "people|places|organizations|terms"}}} —
default section is terms; use &#38; for any literal ampersand in a note body),
check_apparatus.py; regenerate check_config.json for the units whose data/zh
exists, then check_structure.py + check_content.py + qc_entities.py. Rebuild the
EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar).
Record every result in PROGRESS.md; commit and push claude/scales-and-claws. Do
not pause for approval mid-batch.

Deliver in chat: the built EPUB attached, AND the B04 kickoff pasted verbatim
in a fenced code block in the same reply.
```

If the commissioner instead sends corrections to B01/B02, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B03.

## What is DONE (do not redo)

- Survey (2026-08-10): source characterized, book.json complete, skeleton EPUB
  green, batch plan + 3 standing decisions approved, photos ruled IN.
- B01 (2026-08-11): ch000 (序) + ch001 (上海人的過年忙). Voice gate PASSED;
  ch001 is the FROZEN register reference. 25 notes, 22 glossary rows, 5 figures.
- B02 (2026-08-11): ch002-ch014 (宋案的回顧 through 跳舞), PDF 34-58 /
  printed 32-56. Thirteen essays, the press-and-politics cluster. All checks
  green (verify_unit, check_numbers, check_align, check_content, qc_entities,
  check_structure, check_apparatus); qa_epub PASS; epubcheck 5.1.0 clean;
  check_register within tolerance on all 13. 93 notes (book-wide 26-118), 25
  glossary rows, 13 reprint figures. See PROGRESS.md for the full log,
  including the eight fact-check flags (Song's post, the Subao date, the
  crossed sobriquets, Kang's Guoshi Bao, etc.).

## Tooling in place (do not revert)

- OCR: tesseract chi_tra_vert --psm 5 only (PaddleOCR absent, ocr_dual.py
  NOT usable here — wrong script/orientation). ~85% accurate; every page is
  eye-read at magnification and data/zh hand-corrected against the scans.
- ocr_crop.py crop for this book: --left 0.03 --right 0.97 --top 0.13
  --bottom PAGE-TYPE dependent (full-text ~0.95; photo pages tighter).
- indents.py is HORIZONTAL-only and errors here; do NOT rely on it.
  assemble.py runs on the blank-line signal; paragraphs finalized by hand.
- scripts/check_content.py name_map PATCHED (B01) to skip '_'-prefixed keys
  and non-dict values. DO NOT REVERT.
- scripts/apparatus_merge.py PATCHED (B02): glossary merge is SECTION-AWARE.
  A batch glossary row carries an optional "section" (people/places/
  organizations/terms, default terms); it merges into that section, treats a
  zh present in ANY section as already-present, and keeps flat behavior for an
  un-sectioned ledger. The old flat merge crashed the builder. DO NOT REVERT.
- NOTE-BODY RULE (B02): note/glossary bodies are inserted RAW into XHTML. Use
  &#38; for a literal ampersand (a bare "&" slips past apparatus_merge and
  produces a FATAL epubcheck error that drops every later note body). Named
  entities are already refused; use numeric character references only.
- FIGURE RULE (B02): a figure's "before" anchor MUST fall within the first
  ~80 chars of the target paragraph (the builder inserts the figure before
  that paragraph). Point it at a paragraph opening.
- check_config.json (tracked): {docs,sources,notes,variants} for
  check_structure/check_content, scoped to the units whose data/zh EXISTS in
  the container (ch000/ch001 data/zh is gitignored and not regenerable — B01
  reproducibility note — so the two checks cover the current batch's units;
  the builder's unmatched-anchor refusal is the whole-book backstop).
  REGENERATE it each batch (one-liner in PROGRESS).
- data/noise.txt: B02 added 十六開/四開/八開, 禮拜六, 九一八/一二八,
  瞎七搭八, 星期一、二、三、四、五, 萬丈深淵 (reasons in-file). Longest-first.
- data/ocr_fixes.json: crop-verified readings ledger (audit trail; NOT a full
  reconstruction — see the reproducibility note in PROGRESS).

## Renderings settled / carry-forward

- Voice (frozen at the ch001 gate): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, the author
  stepping in to editorialize. This held for the grave political essays of
  B02 too (no academic distance). Subsection topic-labels = ITALIC run-in
  leads (builder supports *italic* only; #### breaks the heading-shape gate).
- Money policy (recurs book-wide): 塊/元 = "dollar"; 大洋 = the standard
  silver dollar; 小洋 = "small silver"; 毛 = the period unit "*mao*", kept
  romanized; 角 = "*jiao*" and 分 = "*fen*" (glossed at ch014: jiao = a tenth,
  fen = a hundredth of a dollar). Do NOT flatten to "cents".
- Shelf-consistent names (authority.json + B01): 南京路 Nanjing Road, 南市
  Nanshi, 捕房 police station. Author 郁慕俠 = Yu Muxia (principal). Preface
  author 天虛我生 = Chen Diexian.
- Glossary DECIDED in B02 (reuse verbatim; grep before re-noting): people
  袁世凱 Yuan Shikai, 戴季陶 Dai Jitao, 周浩 Zhou Hao, 趙秉鈞 Zhao Bingjun,
  康有為 Kang Youwei, 梁啟超 Liang Qichao, 章太炎 Zhang Taiyan, 鄭正秋 Zheng
  Zhengqiu, 歐陽予倩 Ouyang Yuqian, 蘇石癡 Su Shichi, 顧無為 Gu Wuwei; papers
  民立報 Minli Bao, 民權報 Minquan Bao, 天鐸報 Tianduo Bao, 亞細亞報 Yaxiya
  Bao, 大晚報 Da Wanbao, 申報 Shenbao, 新聞報 Xinwenbao; places 福州路 Fuzhou
  Road, 望平街 Wangping Street, 棋盤街 Qipan Street; terms 新劇 new drama,
  遊戲場 amusement hall, 小報 tabloid, 號外 extra.
- Terms to DECIDE early in B03 (they recur): 野雞 (pheasant / unlicensed
  streetwalker — footnoted at ch012, glossary it here), 舞女 dance-girl,
  堂子 / 么二 / 長三 (courtesan-house grades), 姨太太 concubine, 娼 / 妓.
- No continuing cast (essay collection); no voice sheets needed. Recurring
  historical names are handled by the glossary, not sheets.

## Where the book stands

- Fifteen of 168 units done (preface + 14 essays). 153 essays remain. No plot
  to track; the register decisions in B01 govern everything downstream. The
  book's internal dating runs to ~1934-35 (Manchukuo, the "Year of the
  Magazine"), a few years past the 1933 imprint — flagged honestly, unresolved
  (this is a 2019 reset, no 1933 collation source).

## Next batch scope

- B03 = ch015-ch034, PDF 59-83, printed 57-81. The Shanghai demimonde:
  courtesan houses, their grades and rules, brothel slang and catchphrases,
  the swindles of the trade, a woman physiognomist. Expect period money,
  house-type vocabulary, and Wu-dialect slang needing glosses; few famous
  proper names, more custom and texture. Refine the provisional English
  titles against the essay bodies.

## Open traps and environment state

- This is the 2019 RESET, not the 1933 original: no collation source. Where the
  reprint is suspect, note it; do not guess the 1933 reading.
- Vertical RTL OCR column-order errors are silent; verify assemble output by
  eye. Photo-band OCR corrupts paragraphing; keep it out of the crop.
- Two essays share PDF 214 (ch135/ch136) and two share PDF 218 (ch140/ch141):
  unit boundaries mid-page (B08/B10), watch the parity split.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset
  printed = pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template
  stub") — HANDOFF carries a real kickoff, so the Stop hook correctly enters
  its enforcing path. Working as designed. See PROGRESS.
