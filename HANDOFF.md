# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

```
Scales and Claws B06

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu
Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; 2019 Taipei reprint,
customs volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the
harness to start you on a stray branch and consolidate per rule 2 (check out the
canonical branch, reset it to origin, do the work there, delete the stray). This
book's PR history through B05 is already merged, so if the designated branch
carries only merged history, restart it from origin. Deliverable
out/scales-and-claws-of-shanghai.epub.

Do Batch B06 = ch071-ch090 (賊技 through 場面不可不繃; PDF 134-158, printed
folios 132-156) end to end per the CLAUDE.md pipeline: ./setup.sh; render 134
158 --dpi 300; OCR with the B01-B05 crop (ocr_crop.py --left 0.03 --right 0.97
--top 0.13 --bottom 0.95 --lang chi_tra_vert --psm 5, tighter --bottom on any
page carrying a reprint photo). tesseract on this vertical-Traditional reset is
only ~85% and too error-dense to trust: EYE-READ every page at magnification and
hand-transcribe data/zh against the scans, exactly as B01-B05 did. indents.py is
UNUSABLE here; assemble on the blank-line signal and finalize paragraph
structure BY HAND against the scan, using the short-line signal at the page
seams (and note that where a text band sits above a reprint photo there may be
NO internal short-column break, so the band can be a single paragraph, as ch063
was). pgrep -c tesseract must be 0 after OCR. Eyeball every page for
reprint-added photos: 大出喪 (The Grand Funerals, ch088, PDF 153-155, which
spans three pages and is a prime photo candidate) and 送喪馬車 (ch089) are the
likeliest; run each through the figure pipeline (crop to data/figs/, alt text,
caption translating any reprint label and stating 2019-editor provenance).

MULTI-PAGE UNITS in this batch: ch072 (PDF 135-136), ch075 (139-140), ch076
(141), ch088 (153-155, note the gap to ch089 at 156). Re-read the folio off the
scan at every opener; offset stays printed = pdf - 2 but VERIFY it.

BEFORE translating, read the final two pages of out/ch070_reading.md: HANDOFF
describes the voice, but those pages ARE the voice; the FROZEN reference is
still out/ch001_reading.md. Run check_register.py --ref out/ch001_reading.md on
every unit. Consult glossary.json and authority.json BEFORE romanizing any
name. THEMATIC NOTE: this cluster is the beggars-cheats-and-street-trades run
(賊技 thieves, 吃豆腐/吃盤子/吃百家飯 sponging rackets, 叫魂 soul-calling, 沖喜
luck-weddings, 拉洋人/小車/坐車子 the transport trades, 大出喪 the grand
funerals). Expect dense Wu-dialect slang and beggar/underworld cant: gloss it,
keep the flavour, footnote generously. Recurring furniture already noted,
cross-ref do not re-note: money policy (大洋/小洋/毛/角/分/文, ch001 & ch014),
弄堂 longtang (ch063), 老虎灶 (ch063), the little pawnshops (ch062), 花會
huahui (ch065), 遊戲場 amusement halls (glossed), 洋人/租界 furniture. Crop-verify
every name, number, price and low-confidence span, recording verified readings
in data/ocr_fixes.json. Fact-check any real person or institution against real
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
check_content.py --config check_config.json + qc_entities.py PER BILINGUAL FILE
(qc_entities.py out/<id>_bilingual.md — it reads ONE bilingual file, NOT the
config; loop over units). Rebuild the EPUB, qa_epub.py until green, epubcheck
(jar at /tmp/epubcheck-5.1.0/epubcheck.jar). Record every result in PROGRESS.md;
commit and push claude/scales-and-claws. Do not pause for approval mid-batch.

Deliver in chat: the built EPUB attached, AND the B07 kickoff pasted verbatim
in a fenced code block in the same reply.
```

If the commissioner instead sends corrections to B01-B05, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B06.

## What is DONE (do not redo)

- Survey (2026-08-10): source characterized, book.json complete, skeleton EPUB
  green, batch plan + 3 standing decisions approved, photos ruled IN.
- B01 (2026-08-11): ch000 (序) + ch001 (上海人的過年忙). Voice gate PASSED;
  ch001 is the FROZEN register reference. 25 notes, 22 glossary rows, 5 figures.
- B02 (2026-08-11): ch002-ch014 (宋案的回顧 through 跳舞). Press & politics.
  93 notes (book-wide 26-118), 25 glossary rows, 13 reprint figures.
- B03 (2026-08-12): ch015-ch034 (肉林秘聞 through 女相士). Shanghai demimonde.
  93 notes (book-wide 119-211), 32 glossary rows, no figures.
- B04 (2026-08-12): ch035-ch052 (一杯茶值五大元 through 味蒓園). Prices & trades.
  61 notes (212-272), 36 glossary rows, 2 reprint figures.
- B05 (2026-08-12): ch053-ch070 (新世界的隧道 through 裱畫店之換天頭). Amusement
  halls and street rackets. 87 notes (book-wide 273-359), 47 glossary rows,
  3 reprint figures (ch053 Huang Chujiu portrait, ch056 Garden Bridge/Bund
  aerial, ch063 tiger-stove photo). All gates green (verify_unit, check_align,
  check_apparatus, check_structure, check_content, qc_entities); qa_epub PASS;
  epubcheck 5.1.0 clean; check_register within tolerance on all 18. Fact-checks
  in PROGRESS (New World/Jing Runsan, the 1882 telephone & Zikawei observatory,
  R.W. Little & the 1882 electric company, the Wills Bridge/1873 buyout, French
  Park/Koukaza, Jessfield all CORROBORATED; the Bubbling Well Road "Lu Xun tomb"
  UNCORROBORATED/legend, flagged).

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
- NOTE-BODY RULE (B02, reaffirmed B04/B05): note/glossary bodies are inserted
  RAW into XHTML. STRAIGHT quotes, &#8211; for en-dashes in date ranges, &#8212;
  or a literal em dash for em dashes, <i> only (no <b>), numeric char refs never
  named entities, &#38; for a literal ampersand. When writing CJK into the batch
  JSON, RE-READ every character (near-homoglyph typos: 葫/葡, 潤/營, 儌, 韓/韋).
- ANCHOR GOTCHA (B05): note markers sit after closing punctuation, so a phrase
  ending a quoted term reads `ticket."` with the period INSIDE the quotes; an
  anchor ending `ticket"` will NOT match. Anchor on a phrase that does not
  straddle the closing quote, or drop the trailing quote from the anchor.
- FIGURE RULE (B02): a figure's "before" anchor MUST fall within the first
  ~80 chars of the target paragraph.
- check_config.json (tracked): {docs,sources,notes,variants}. In a fresh
  container only the CURRENT batch's data/zh exists, so REGENERATE it each
  batch to the units whose data/zh EXISTS (glob data/zh/ch*.txt ->
  docs=out/<u>_reading.md, sources=data/zh/<u>.txt; keep notes/variants).
- verify_unit.py takes UNIT IDS ONLY and applies data/noise.txt itself; do NOT
  pass --noise. check_numbers.py DOES take --noise. check_structure/check_content
  take --config. qc_entities.py takes ONE BILINGUAL FILE as its positional arg
  (out/<id>_bilingual.md), NOT the config; loop over units. (The old HANDOFF
  line saying it takes the config was WRONG; passing the config makes it a
  silent no-op that measures nothing.)
- check_numbers quirks learned (B05): it parses "a hundred"/"a thousand" but
  NOT "the hundred"/"per hundred" (use "a hundred"); it has no plain "hundred"
  word entry, only "a hundred" and "<one> hundred"; 零售 (retail) and 百科
  (encyclopaedia) and 巨萬 (a fortune) trip false numerals; an abbreviated
  X、Y like 十一、二 reads the standalone Y as a bare numeral. Fix with a
  TARGETED lookbehind noise, never a broad one (rule 4: noise never masks a
  drop).
- data/noise.txt: B03 added 北四川路, 十八、九, 長三, 么二, 老六. B04 added
  黃楚九, 九畝地, 億定盤路, 萬民矚目, 十餘萬, 塵煙四起. B05 added 巨萬, 零售,
  百科, 十六浦, 十幾萬, (?<=十一)、二. Longest-first. A noise rule only ever
  REMOVES a source numeral; never noise a value you failed to carry.
- data/ocr_fixes.json: crop-verified readings ledger. B05 added
  ch053/ch057/ch058/ch059/ch060/ch062/ch064.
- check_align.py takes ONE unit (no --config); loop over units.

## Renderings settled / carry-forward

- Voice (frozen at the ch001 gate): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, the author
  stepping in to editorialize. Held through B02-B05. ch060 shows the "按" form
  (an editor's note 劍公按 answered by 作者又按): render both, they are part of
  the printed piece.
- Money policy (recurs book-wide): 塊/元 = "dollar"; 大洋 = the standard silver
  dollar; 小洋 = "small silver"; 毛 = "*mao*"; 角 = "*jiao*"; 分 = "*fen*";
  文 = "cash" (period copper); 大錢 = "big cash". As an INTEREST rate, 分 = one
  per cent (noted ch062). Never flatten 毛/角 to "cents". Notes at ch001/ch014.
- Shelf-consistent names (authority.json): 南京路 Nanjing Road, 南市 Nanshi,
  捕房 police station, 霞飛路 Avenue Joffre, 靜安寺路 Bubbling Well Road,
  工部局 the Municipal Council, 公董局 the French Municipal Council. Author
  郁慕俠 = Yu Muxia; preface author 天虛我生 = Chen Diexian.
- B05 glossary DECIDED (reuse verbatim; grep before re-noting):
  People 經營三 Jing Runsan (source misprint for 經潤三), 陸遜 Lu Xun of Wu,
  周瑜 Zhou Yu, 皮曉浦 Pi Xiaopu, 能慕谷 Neng Mugu, 立德 Lide (R.W. Little),
  黃式權 Huang Shiquan, 孔夫子 Confucius, 左宗棠 Zuo Zongtang. Places 泥城橋
  Nicheng Bridge, 跑馬廳 the Racecourse, 外白渡橋 the Garden Bridge, 蘇州河
  Suzhou Creek, 馬霍路 Mohawk Road, 顧家宅 Koukaza, 兆豐公園 Jessfield Park,
  松江 Songjiang, 愛多亞路 Avenue Édouard VII, 十六浦 Shiliupu, 徐家匯
  Xujiahui, 寧紹 Ningbo and Shaoxing. Orgs 樓外樓 Tower-Beyond-the-Tower, 大世界
  Great World, 冠雲詩社 Guanyun Poetry Society, 水爐公所 Water-Stove Guild,
  大廠 the Great Works. Terms 八卦 Eight Trigrams, 風水 fengshui, 翁仲 guardian
  figures, 自來火 self-coming fire (gaslight), 地火 earth-fire, 德律風 delüfeng,
  詩謎 poem-riddle, 大洋盤 big silver sucker, 老虎灶 tiger stove, 弄堂 lane,
  小押當 little pawnshop, 餉押 pay-pawn, 後門貨 back-door goods, 丟圈 ring toss,
  丟票 dropped ticket, 花會 huahui, 快馬 fast horses, 裱畫店 picture-mounting
  shop, 換天頭 changing the heaven-head.
- Earlier-batch glossary (reuse verbatim): people 袁世凱 Yuan Shikai, 戴季陶
  Dai Jitao, 康有為 Kang Youwei, 章太炎 Zhang Taiyan, 鄭正秋 Zheng Zhengqiu,
  譚鑫培 Tan Xinpei, 黃楚九 Huang Chujiu, 賽金花 Sai Jinhua, 林黛玉 Lin Daiyu;
  papers 申報 Shenbao, 新聞報 Xinwenbao; house grades 長三 changsan, 么二 yao-er,
  野雞 pheasant, 鹹肉莊 salt-meat house; places 四馬路 Fourth Avenue (福州路),
  北四川路 North Sichuan Road, 張園 Zhang's Garden, 霞飛路 Avenue Joffre.
  Numbered "Avenues": 大馬路=Nanjing, 二馬路=Jiujiang, 三馬路=Hankou,
  四馬路=Fuzhou. 新世界 New World (organizations).
- No continuing cast (essay collection); recurring historical names handled by
  the glossary, not voice sheets.

## Where the book stands

- Seventy-one of 168 units done (preface + 70 essays). 97 essays remain. No plot
  to track; the register decisions in B01 govern everything downstream. Internal
  dating runs ~1856 (Wills Bridge) to the mid-1930s.

## Next batch scope

- B06 = ch071-ch090, PDF 134-158, printed 132-156. Thieves' tricks, the
  tofu/plate/hundred-households sponging rackets, soul-calling, mourning-cloth
  debts, prosperity notes, Brother Sheep, water ghosts, selling sheep, salable
  looks, flushing birds, luck-weddings, the big license, hauling foreigners,
  riding without settling the fare, the wheelbarrows, the grand funerals,
  funeral carriages, keeping up appearances. The beggars-cheats-and-transport
  cluster: heavy Wu slang and underworld cant. Offset still printed = pdf - 2.

## Open traps and environment state

- MULTI-PAGE UNITS B06: ch072 (135-136), ch075 (139-140), ch088 (153-155).
  ch088 大出喪 spans three PDF pages with a gap before ch089 at 156: a prime
  photo candidate (funeral processions). Watch the folio at every opener.
- This is the 2019 RESET, not the 1933 original: no collation source. Where the
  reprint is suspect, note it; do not guess the 1933 reading. Reprint misprints
  seen so far: ch052 味蒓園 (TOC), ch053 經營三 for 經潤三. Render as printed,
  translate to the attested form where one exists, footnote the discrepancy.
- Source SELF-CENSORSHIP: the reprint blanks words as ×× (clinics, a steamship
  line, poetry societies). Render as printed, footnote.
- Vertical RTL OCR column-order errors are silent; verify assemble output by
  eye. Photo-band OCR corrupts paragraphing; keep it out of the crop. A text
  band ABOVE a photo may have no internal short-column break (one paragraph).
- Magnified crops can clip a character's top strokes and misread it (三 read as
  一 at ch057); when a digit is load-bearing, crop generously top and bottom.
- Two essays share PDF 214 (ch135/ch136) and two share PDF 218 (ch140/ch141):
  unit boundaries mid-page (B08/B10), watch the parity split.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset
  printed = pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- Pagemap: only ch000/ch001 carry data/pagemap (B01); essays ship without
  followable page-list entries (consistent B02-B05). Notes cite printed folios
  in prose.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template
  stub") — HANDOFF carries a real kickoff, so the Stop hook correctly enters
  its enforcing path. Working as designed.
