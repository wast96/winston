# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

```
Scales and Claws B05

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu
Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; 2019 Taipei reprint,
customs volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the
harness to start you on a stray branch and consolidate per rule 2 (check out the
canonical branch, reset it to origin, do the work there, delete the stray). This
book's PR history through B04 is already merged, so if the designated branch
carries only merged history, restart it from origin. Deliverable
out/scales-and-claws-of-shanghai.epub.

Do Batch B05 = ch053-ch070 (新世界的隧道 through 裱畫店之換天頭; PDF 109-133,
printed folios 107-131) end to end per the CLAUDE.md pipeline: ./setup.sh;
render 109 133 --dpi 300; OCR with the B01-B04 crop (ocr_crop.py --left 0.03
--right 0.97 --top 0.13 --bottom 0.95 --lang chi_tra_vert --psm 5, tighter
--bottom on any page carrying a reprint photo). tesseract on this
vertical-Traditional reset is only ~85% and too error-dense to trust: EYE-READ
every page at magnification and hand-transcribe data/zh against the scans,
exactly as B01-B04 did. indents.py is UNUSABLE here; assemble on the blank-line
signal and finalize paragraph structure BY HAND against the scan, using the
short-line signal at the page seams. pgrep -c tesseract must be 0 after OCR.
Eyeball every page for reprint-added photos (Garden Bridge / 外白渡橋 ch056, the
gardens and landmarks are likely photo candidates) and run each through the
figure pipeline (crop to data/figs/, alt text, caption translating the reprint
label and stating 2019-editor provenance).

BEFORE translating, read the final two pages of out/ch052_reading.md: HANDOFF
describes the voice, but those pages ARE the voice; the FROZEN reference is
still out/ch001_reading.md. Run check_register.py --ref out/ch001_reading.md on
every unit. Consult glossary.json and authority.json BEFORE romanizing any
name. TWO TRAPS IN THIS CLUSTER: (1) 陸遜 at ch057 is the Three Kingdoms general
Lu Xun of Wu (183-245), NOT the writer Lu Xun 魯迅 — disambiguate explicitly in
a note. (2) 法國公園 (French Park, ch058) got only a brief pointer-note at ch052;
give it its full note here at its own chapter (Koukaza / French Park, now Fuxing
Park). Other recurring furniture already noted, cross-ref do not re-note: money
policy (大洋/小洋/毛/角/分/文, ch001 & ch014), 靜安寺路 Bubbling Well Road (ch017),
新世界 New World (glossed B04), 野雞 pheasant (ch012). Crop-verify every name,
number, price and low-confidence span, recording verified readings via
apply_fixes.py. Fact-check any real person or institution against real
scholarship (Wikipedia / Baidu Baike / academic, NEVER an LLM-written site);
state the verdict in the note. Never invent bridging text; verify each unit's
tail against the scan.

NOTES: the commissioner wants them GENEROUS and dense, more rather than fewer.
Annotate freely wherever a non-specialist Western reader would miss anything (a
price in period money, a custom, a piece of slang; who a person or landmark was;
texture lost in translation; the author as interested witness). Recurring
subjects get their note at FIRST appearance (grep notes.json and earlier reading
files first; keep the per-batch "NOT re-noted" list). Do not thin out to hit a
number.

Per unit: write out/<id>_reading.md (one paragraph per source line), then
make_bilingual.py, verify_unit.py (unit ids only — it applies data/noise.txt
itself; do NOT pass --noise), check_align.py; apparatus_merge.py for
notes/glossary/figures (glossary rows may be SECTIONED in the batch file:
{"glossary": {"<zh>": {..., "section": "people|places|organizations|terms"}}} —
default section is terms; note bodies inserted RAW into XHTML, so use straight
quotes, &#8211; for en-dashes in date ranges, &#8212; or a literal em dash, <i>
only, numeric char refs never named entities, and &#38; for any literal
ampersand), check_apparatus.py; regenerate check_config.json for the units whose
data/zh exists, then check_structure.py --config check_config.json +
check_content.py --config check_config.json + qc_entities.py check_config.json.
Rebuild the EPUB, qa_epub.py until green, epubcheck (jar at
/tmp/epubcheck-5.1.0/epubcheck.jar). Record every result in PROGRESS.md; commit
and push claude/scales-and-claws. Do not pause for approval mid-batch.

Deliver in chat: the built EPUB attached, AND the B06 kickoff pasted verbatim
in a fenced code block in the same reply.
```

If the commissioner instead sends corrections to B01-B04, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B05.

## What is DONE (do not redo)

- Survey (2026-08-10): source characterized, book.json complete, skeleton EPUB
  green, batch plan + 3 standing decisions approved, photos ruled IN.
- B01 (2026-08-11): ch000 (序) + ch001 (上海人的過年忙). Voice gate PASSED;
  ch001 is the FROZEN register reference. 25 notes, 22 glossary rows, 5 figures.
- B02 (2026-08-11): ch002-ch014 (宋案的回顧 through 跳舞), PDF 34-58 /
  printed 32-56. Press-and-politics cluster. 93 notes (book-wide 26-118),
  25 glossary rows, 13 reprint figures. All gates green.
- B03 (2026-08-12): ch015-ch034 (肉林秘聞 through 女相士), PDF 59-83 /
  printed 57-81. Shanghai demimonde cluster. 93 notes (book-wide 119-211),
  32 glossary rows, NO figures. All gates green.
- B04 (2026-08-12): ch035-ch052 (一杯茶值五大元 through 味蒓園), PDF 84-108 /
  printed 82-106. Prices-and-trades cluster (teahouse waitresses, the theatre
  master Tan Xinpei, education fakes, the White Russians of Avenue Joffre,
  Zhang's Garden). 61 notes (book-wide 212-272), 36 glossary rows, 2 reprint
  figures (ch037 character-stall, ch052 Arcadia Hall). All gates green
  (verify_unit, check_numbers, check_align, check_content, qc_entities,
  check_structure, check_apparatus); qa_epub PASS; epubcheck 5.1.0 clean;
  check_register within tolerance on all 18. book.json ch052 title corrected
  味園 -> 味蒓園. Fact-checks in PROGRESS (Tan Xinpei, Huang Chujiu, the Xia
  brothers incl. the son-in-law tie, Lin Daiyu, Joffre, Zhang's Garden, the
  department stores, 性史/肉蒲團, the GPO all CORROBORATED; the Tan-Sai Jinhua
  cohabitation UNCORROBORATED/apocryphal, flagged as gossip).

## Tooling in place (do not revert)

- OCR: tesseract chi_tra_vert --psm 5 only (PaddleOCR absent, ocr_dual.py NOT
  usable here). ~85% accurate; every page eye-read at magnification and data/zh
  hand-corrected against the scans.
- ocr_crop.py crop for this book: --left 0.03 --right 0.97 --top 0.13
  --bottom PAGE-TYPE dependent (full-text ~0.95; photo pages tighter).
- indents.py is HORIZONTAL-only and errors here; do NOT rely on it.
- scripts/check_content.py name_map PATCHED (B01) to skip '_'-prefixed keys
  and non-dict values. DO NOT REVERT.
- scripts/apparatus_merge.py PATCHED (B02): glossary merge is SECTION-AWARE.
  DO NOT REVERT.
- NOTE-BODY RULE (B02, reaffirmed B04): note/glossary bodies are inserted RAW
  into XHTML. STRAIGHT quotes (not curly), &#8211; for en-dashes in date
  ranges, &#8212; or a literal em dash for em dashes, <i> only (no <b>),
  numeric char refs never named entities, &#38; for a literal ampersand. When
  writing CJK into the batch JSON, RE-READ every character (B04 caught a
  half-dozen near-homoglyph typos before merge: 葫/葡, 髦/髛, 鹹/鵹, 鍍/鏀,
  巴/巷, 蒓/蕾, 塏/塺, 競/竞).
- FIGURE RULE (B02): a figure's "before" anchor MUST fall within the first
  ~80 chars of the target paragraph.
- check_config.json (tracked): {docs,sources,notes,variants}. In a fresh
  container only the CURRENT batch's data/zh exists, so REGENERATE it each
  batch to the units whose data/zh EXISTS (glob data/zh/ch*.txt ->
  docs=out/<u>_reading.md, sources=data/zh/<u>.txt; keep notes/variants).
- verify_unit.py takes UNIT IDS ONLY and applies data/noise.txt itself; do NOT
  pass --noise (it treats extra args as more units and crashes). check_numbers.py
  DOES take --noise. check_structure/check_content take --config; qc_entities
  takes the config path as a positional arg.
- data/noise.txt: B03 added 北四川路, 十八、九, 長三, 么二, 老六. B04 added
  黃楚九, 九畝地, 億定盤路, 萬民矚目, 十餘萬, 塵煙四起 (name/idiom numerals).
  Longest-first. A noise rule only ever REMOVES a source numeral; never noise a
  value you failed to carry.
- data/ocr_fixes.json: crop-verified readings ledger (audit trail; B04 added
  ch035/ch037/ch044/ch049/ch052).
- check_align.py takes ONE unit (no --config); loop over units.

## Renderings settled / carry-forward

- Voice (frozen at the ch001 gate): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, the author
  stepping in to editorialize. Held through B02-B04.
  Subsection topic-labels = ITALIC run-in leads (builder supports *italic*
  only; #### breaks the heading-shape gate). (No subsections arose in B04 —
  all 18 units are single-run essays.)
- Money policy (recurs book-wide): 塊/元 = "dollar"; 大洋 = the standard silver
  dollar; 小洋 = "small silver"; 毛 = "*mao*"; 角 = "*jiao*"; 分 = "*fen*";
  文 = "cash" (period copper). Never flatten 毛/角 to "cents". Notes at ch001
  and ch014; carried, not re-noted. (B04: 二元二角 = "two dollars and two jiao".)
- Shelf-consistent names (authority.json): 南京路 Nanjing Road, 南市 Nanshi,
  捕房 police station, 霞飛路 Avenue Joffre, 永安 Wing On, 先施 Sincere. Author
  郁慕俠 = Yu Muxia; preface author 天虛我生 = Chen Diexian.
- B04 glossary DECIDED (reuse verbatim; grep before re-noting):
  People 譚鑫培 Tan Xinpei / 小叫天 Xiao Jiaotian, 黃楚九 Huang Chujiu, 賽金花
  Sai Jinhua, 夏月潤 Xia Yuerun, 夏月珊 Xia Yueshan, 邱治雲 Qiu Zhiyun, 林黛玉
  Lin Daiyu, 翁梅倩 Weng Meiqian, 嚴芙孫 Yan Fusun. Places 張園 Zhang's Garden,
  味蒓園 the Weiyuan, 愚園 Yu Garden, 徐園 Xu Garden, 半淞園 Bansong Garden,
  安塏第 Arcadia Hall, 康腦脫路 Connaught Road, 億定盤路 Edinburgh Road, 北蘇州路
  North Suzhou Road, 寶昌路 Avenue Paul Brunat, 九畝地 Jiumudi, 法國公園 French
  Park, 北福建路 North Fujian Road, 唐家弄 Tang Family Lane, 安康里 Ankang Li.
  Orgs 永安公司 Wing On, 先施公司 Sincere, 新新公司 Sun Sun, 新舞臺 New Stage,
  醒舞臺 Awakening Stage, 新世界 New World, 群仙 Qunxian. Terms 髦兒戲 all-girl
  opera, 鬚生 bearded-male role (laosheng), 拆字 character-splitting, 白俄 White
  Russians, 野雞大學 pheasant university.
- B02/B03 glossary (reuse verbatim): people 袁世凱 Yuan Shikai, 戴季陶 Dai Jitao,
  周浩 Zhou Hao, 康有為 Kang Youwei, 章太炎 Zhang Taiyan, 鄭正秋 Zheng Zhengqiu,
  辜鴻銘 Gu Hongming; papers 申報 Shenbao, 新聞報 Xinwenbao; house grades 長三
  changsan, 么二 yao-er, 堂子 house, 野雞 pheasant, 鹹肉莊 salt-meat house,
  花煙間 flower-smoke room; places 四馬路 Fourth Avenue (= 福州路 Fuzhou Road),
  靜安寺路 Bubbling Well Road, 北四川路 North Sichuan Road. Numbered "Avenues":
  大馬路=Nanjing, 二馬路=Jiujiang, 三馬路=Hankou, 四馬路=Fuzhou.
- No continuing cast (essay collection); no voice sheets needed. Recurring
  historical names are handled by the glossary, not sheets.

## Where the book stands

- Fifty-three of 168 units done (preface + 52 essays). 115 essays remain. No
  plot to track; the register decisions in B01 govern everything downstream.
  Internal dating runs ~1900 (Boxer, Tan Xinpei) to the mid-1930s.

## Next batch scope

- B05 = ch053-ch070, PDF 109-133, printed 107-131. The New World tunnel,
  posters over the piss-pit, roof-top eight-trigrams, Garden Bridge, the tomb
  of Lu Xun (the Wu general 陸遜, NOT the writer), the French Park, fire under
  the ground, the telephone, Confucius, little pawnshops, tiger stoves, poem
  riddles, the lavish "great works", ring-toss and ticket-toss carnival games,
  the picture-mounter's heaven-head swap. Offset still printed = pdf - 2.

## Open traps and environment state

- 陸遜 (ch057) = the Three Kingdoms statesman-general Lu Xun of Wu (183-245),
  NOT the writer Lu Xun 魯迅. Disambiguate in a note (the English title "The
  Site of Lu Xun's Tomb" will otherwise mislead).
- 法國公園 French Park: brief pointer-note only at ch052; its FULL note is due
  at ch058 (its own chapter).
- This is the 2019 RESET, not the 1933 original: no collation source. Where the
  reprint is suspect, note it; do not guess the 1933 reading.
- Source SELF-CENSORSHIP: the reprint blanks words as ×× (e.g. ch031). Render
  as printed, footnote.
- Vertical RTL OCR column-order errors are silent; verify assemble output by
  eye. Photo-band OCR corrupts paragraphing; keep it out of the crop.
- Two essays share PDF 214 (ch135/ch136) and two share PDF 218 (ch140/ch141):
  unit boundaries mid-page (B08/B10), watch the parity split.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset
  printed = pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- Pagemap: only ch000/ch001 carry data/pagemap (B01); essays ship without
  followable page-list entries (consistent across B02-B04). Notes cite printed
  folios in prose.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template
  stub") — HANDOFF carries a real kickoff, so the Stop hook correctly enters
  its enforcing path. Working as designed.
