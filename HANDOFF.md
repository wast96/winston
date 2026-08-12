# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

```
Scales and Claws B04

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu
Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; 2019 Taipei reprint,
customs volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the
harness to start you on a stray branch and consolidate per rule 2 (check out the
canonical branch, reset it to origin, do the work there, delete the stray). This
book's PR history through B03 is already merged, so if the designated branch
carries only merged history, restart it from origin. Deliverable
out/scales-and-claws-of-shanghai.epub.

Do Batch B04 = ch035-ch052 (一杯茶值五大元 through 味園; PDF 84-108, printed
folios 82-106) end to end per the CLAUDE.md pipeline: ./setup.sh; render 84 108
--dpi 300; OCR with the B01-B03 crop (ocr_crop.py --left 0.03 --right 0.97 --top
0.13 --bottom 0.95 --lang chi_tra_vert --psm 5, tighter --bottom on any page
carrying a reprint photo so the photo band stays out of body OCR). tesseract on
this vertical-Traditional reset is only ~85% and too error-dense to trust:
EYE-READ every page at magnification and hand-transcribe data/zh against the
scans, exactly as B01-B03 did. indents.py is UNUSABLE here; assemble on the
blank-line signal and finalize paragraph structure BY HAND against the scan,
using the short-line signal at the page seams where the blank falls off the
page. pgrep -c tesseract must be 0 after OCR. Eyeball every page for
reprint-added photos (B04 likely has some: 譚鑫培/小叫天 the opera master at
ch040, possibly Avenue Joffre / White Russian scenes at ch048-049) and run each
through the figure pipeline (crop to data/figs/, alt text, caption translating
the reprint label and stating 2019-editor provenance).

BEFORE translating, read the final two pages of out/ch034_reading.md: HANDOFF
describes the voice, but those pages ARE the voice; the FROZEN reference is
still out/ch001_reading.md. Run check_register.py --ref out/ch001_reading.md on
every unit. Consult glossary.json and authority.json BEFORE romanizing any
name. This cluster mixes period prices (tea/food/cash — carry the money policy:
大洋 silver dollar, 小洋 small silver, 毛/角/分 romanized; 文 = cash/wen), the
theatre (小叫天 = 譚鑫培, Tan Xinpei, the great Peking-opera master — fact-check;
翁梅倩 the street-singer ch038), education fakes (野雞大學 pheasant universities
ch043 — 野雞 is now the DECIDED glossary rendering "pheasant"; 鍍金博士 gilded
doctorates ch045), and the White Russian emigres of Avenue Joffre (ch048-049 —
霞飛路 Avenue Joffre is already noted at ch018; cross-ref, do not re-note the
street). Crop-verify every name, number, price and low-confidence span, recording
verified readings via apply_fixes.py. Fact-check any real person or institution
against real scholarship (Wikipedia / Baidu Baike / academic, NEVER an
LLM-written site); state the verdict in the note. Never invent bridging text;
verify each unit's tail against the scan.

NOTES: the commissioner wants them GENEROUS and dense, more rather than fewer.
Annotate freely wherever a non-specialist Western reader would miss anything (a
price in period money, a custom, a piece of slang; who a performer or
institution was; texture lost in translation; the author as interested witness).
Recurring subjects get their note at FIRST appearance (grep notes.json and
earlier reading files first; keep the per-batch "NOT re-noted" list). Do not
thin out to hit a number.

Per unit: write out/<id>_reading.md (one paragraph per source line), then
make_bilingual.py, verify_unit.py, check_align.py; apparatus_merge.py for
notes/glossary/figures (glossary rows may be SECTIONED in the batch file:
{"glossary": {"<zh>": {..., "section": "people|places|organizations|terms"}}} —
default section is terms; use &#38; for any literal ampersand in a note body),
check_apparatus.py; regenerate check_config.json for the units whose data/zh
exists, then check_structure.py + check_content.py + qc_entities.py. Rebuild the
EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar).
Record every result in PROGRESS.md; commit and push claude/scales-and-claws. Do
not pause for approval mid-batch.

Deliver in chat: the built EPUB attached, AND the B05 kickoff pasted verbatim
in a fenced code block in the same reply.
```

If the commissioner instead sends corrections to B01-B03, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B04.

## What is DONE (do not redo)

- Survey (2026-08-10): source characterized, book.json complete, skeleton EPUB
  green, batch plan + 3 standing decisions approved, photos ruled IN.
- B01 (2026-08-11): ch000 (序) + ch001 (上海人的過年忙). Voice gate PASSED;
  ch001 is the FROZEN register reference. 25 notes, 22 glossary rows, 5 figures.
- B02 (2026-08-11): ch002-ch014 (宋案的回顧 through 跳舞), PDF 34-58 /
  printed 32-56. The press-and-politics cluster. 93 notes (book-wide 26-118),
  25 glossary rows, 13 reprint figures. All gates green.
- B03 (2026-08-12): ch015-ch034 (肉林秘聞 through 女相士), PDF 59-83 /
  printed 57-81. The Shanghai demimonde cluster (courtesan-house grades,
  brothel slang, the swindles, a beauty-pageant, the woman physiognomists).
  93 notes (book-wide 119-211), 32 glossary rows, NO figures (text-only
  cluster, deliberate). All gates green (verify_unit, check_numbers,
  check_align, check_content, qc_entities, check_structure, check_apparatus);
  qa_epub PASS; epubcheck 5.1.0 clean; check_register within tolerance on all
  20. Fact-check flags in PROGRESS (1920 lottery abolition CORROBORATED; Gu
  Hongming, flower-elections, the two cigarette brands CORROBORATED; the
  candy company, 電光日報, the two procurers and the 聞鶯 murder as-reported).

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
- scripts/apparatus_merge.py PATCHED (B02): glossary merge is SECTION-AWARE
  (row's optional "section" -> people/places/organizations/terms, default
  terms; a zh present in ANY section counts as already-present; flat behavior
  preserved for an un-sectioned ledger). DO NOT REVERT.
- NOTE-BODY RULE (B02): note/glossary bodies are inserted RAW into XHTML. Use
  &#38; for a literal ampersand; numeric character references only, never
  named entities. Literal em dash (—) and straight quotes are fine (house
  style; B03 used them throughout).
- FIGURE RULE (B02): a figure's "before" anchor MUST fall within the first
  ~80 chars of the target paragraph.
- check_config.json (tracked): {docs,sources,notes,variants}. In a fresh
  container only the CURRENT batch's data/zh exists (earlier batches' data/zh
  is gitignored and not regenerable — B01 reproducibility note), so REGENERATE
  it each batch to the units whose data/zh EXISTS; the builder's
  unmatched-anchor refusal is the whole-book backstop. One-liner: glob
  data/zh/ch*.txt -> docs=out/<u>_reading.md, sources=data/zh/<u>.txt.
- data/noise.txt: B03 added 北四川路, 十八、九, 長三, 么二, 老六 (reasons
  in-file; romanized-name numerals and one elided age range). Longest-first.
- data/ocr_fixes.json: crop-verified readings ledger (audit trail; NOT a full
  reconstruction — see the reproducibility note in PROGRESS).
- check_align.py takes ONE unit (no --config); loop over units.

## Renderings settled / carry-forward

- Voice (frozen at the ch001 gate): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, the author
  stepping in to editorialize. Held through the grave B02 essays and the
  risqué B03 demimonde alike (no academic distance; period contempt on ch027
  male prostitution rendered as printed, terms footnoted neutrally).
  Subsection topic-labels = ITALIC run-in leads (builder supports *italic*
  only; #### breaks the heading-shape gate).
- Money policy (recurs book-wide): 塊/元 = "dollar"; 大洋 = the standard
  silver dollar; 小洋 = "small silver"; 毛 = "*mao*"; 角 = "*jiao*", 分 =
  "*fen*" (glossed at ch014); 文 = "cash" (period copper). Do NOT flatten to
  "cents". Notes at ch001 and ch014; carried, not re-noted.
- Shelf-consistent names (authority.json + B01): 南京路 Nanjing Road, 南市
  Nanshi, 捕房 police station. Author 郁慕俠 = Yu Muxia. Preface author
  天虛我生 = Chen Diexian.
- DEMIMONDE glossary DECIDED in B03 (reuse verbatim; grep before re-noting):
  house grades 長三 changsan, 么二 yao-er, 堂子 house, 野雞 pheasant (DECIDED
  here), 鹹肉莊 salt-meat house / 鹹肉 salt-meat, 花煙間 flower-smoke room,
  煙妓 smoke-girl, 淌白 streetwalker, 小先生 little master, 姨太太 concubine,
  舞女 dance-girl, 白相人 hoodlum, 包客 keeper, 三寸金蓮 three-inch golden
  lotus. People 辜鴻銘 Gu Hongming, 薛大塊頭 Xue the Big Fellow, 寄生姆媽
  Parasite Mama, 聞鶯 Wenying, 菱清 Lingqing, 張桐花 Zhang Tonghua, 吳書箴
  Wu Shuzhen. Places 四馬路 Fourth Avenue (= 福州路 Fuzhou Road), 靜安寺路
  Bubbling Well Road, 北四川路 North Sichuan Road, 霞飛路 Avenue Joffre,
  靶子路 Range Road, 漕涇 Caojing, 三馬路 Third Avenue (= Hankou Road).
  Orgs 永安公司 Wing On Company, 電光日報 Dianguang Ribao. Numbered "Avenues":
  大馬路=Nanjing, 二馬路=Jiujiang, 三馬路=Hankou, 四馬路=Fuzhou.
- B02 glossary (reuse verbatim): people 袁世凱 Yuan Shikai, 戴季陶 Dai Jitao,
  周浩 Zhou Hao, 康有為 Kang Youwei, 章太炎 Zhang Taiyan, 鄭正秋 Zheng
  Zhengqiu, etc.; papers 申報 Shenbao, 新聞報 Xinwenbao, etc.; places 福州路
  Fuzhou Road, 望平街 Wangping Street, 棋盤街 Qipan Street; terms 新劇 new
  drama, 遊戲場 amusement hall, 小報 tabloid.
- No continuing cast (essay collection); no voice sheets needed. Recurring
  historical names are handled by the glossary, not sheets.

## Where the book stands

- Thirty-five of 168 units done (preface + 34 essays). 133 essays remain. No
  plot to track; the register decisions in B01 govern everything downstream.
  Internal dating runs ~1920 (the flower-election) to ~1934-35 (Manchukuo,
  the "Year of the Magazine"), a few years past the 1933 imprint — flagged
  honestly, unresolved (2019 reset, no 1933 collation source).

## Next batch scope

- B04 = ch035-ch052, PDF 84-108, printed 82-106. Prices and food (tea, a
  three-hundred-dollar dinner, sixty-cash characters), street singing
  (翁梅倩), obscene books, the opera master 小叫天/譚鑫培, seamstresses and
  mending-women, the "pheasant universities" and gilded doctorates, the
  booked room and the flower-vase, Avenue Joffre gone Russian and the White
  Russian drifters, the post-office coolies and parcel companies, the Weiyuan.
  Expect period money throughout, one big theatre fact-check (Tan Xinpei),
  the education-fraud cluster, and the White Russian emigre material
  (cross-ref 霞飛路 at ch018).

## Open traps and environment state

- This is the 2019 RESET, not the 1933 original: no collation source. Where the
  reprint is suspect, note it; do not guess the 1933 reading. (B03: 楊 printed
  for 榻 at ch015 p59, rendered to sense, logged in PROGRESS.)
- Source SELF-CENSORSHIP: the reprint blanks words as ×× (e.g. ch031 "a
  colony of the ×× people" = Japanese). Render as printed, footnote.
- Vertical RTL OCR column-order errors are silent; verify assemble output by
  eye. Photo-band OCR corrupts paragraphing; keep it out of the crop.
- Two essays share PDF 214 (ch135/ch136) and two share PDF 218 (ch140/ch141):
  unit boundaries mid-page (B08/B10), watch the parity split.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset
  printed = pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- Pagemap: only ch000/ch001 carry data/pagemap (B01); the geometry tooling is
  unusable for this book, so essays ship without followable page-list entries
  — consistent across B02/B03, not a defect. Notes cite printed folios in
  prose.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template
  stub") — HANDOFF carries a real kickoff, so the Stop hook correctly enters
  its enforcing path. Working as designed. See PROGRESS.
