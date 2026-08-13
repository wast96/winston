# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

```
Scales and Claws B07

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu
Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; 2019 Taipei reprint,
customs volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the
harness to start you on a stray branch and consolidate per rule 2 (check out the
canonical branch, reset it to origin, do the work there, delete the stray). This
book's PR history through B06 is already merged, so if the designated branch
carries only merged history, restart it from origin. Deliverable
out/scales-and-claws-of-shanghai.epub.

Do Batch B07 = ch091-ch110 (假人參 through 尋人; PDF 159-183, printed folios
157-181) end to end per the CLAUDE.md pipeline: ./setup.sh; render 159 183
--dpi 300; OCR with the B01-B06 crop (ocr_crop.py --left 0.03 --right 0.97
--top 0.13 --bottom 0.95 --lang chi_tra_vert --psm 5, tighter --bottom on any
page carrying a reprint photo). tesseract on this vertical-Traditional reset is
only ~85% and too error-dense to trust: EYE-READ every page at magnification and
hand-transcribe data/zh against the scans, exactly as B01-B06 did. indents.py is
UNUSABLE here; assemble on the blank-line signal and finalize paragraph
structure BY HAND against the scan, using the short-line signal at the page
seams (and note that where a text band sits above a reprint photo there may be
NO internal short-column break, so the band can be a single paragraph, as ch063
and ch088 were). pgrep -c tesseract must be 0 after OCR. Eyeball every page for
reprint-added photos and run each through the figure pipeline (crop to
data/figs/ with a BARE filename, not a data/figs/ path; alt text with NO double
quotes since it is inserted raw into an XML attribute; caption translating any
reprint label and stating 2019-editor provenance).

MULTI-PAGE UNITS in this batch: ch091 (PDF 159-160), ch100 (170-171), ch105
(176-178, a likely spot for a photo of a refugee-relief scene or a named
charity boss). Re-read the folio off the scan at every opener; offset stays
printed = pdf - 2 but VERIFY it.

BEFORE translating, read the final two pages of out/ch090_reading.md: HANDOFF
describes the voice, but those pages ARE the voice; the FROZEN reference is
still out/ch001_reading.md. Run check_register.py --ref out/ch001_reading.md on
every unit. Consult glossary.json and authority.json BEFORE romanizing any
name. THEMATIC NOTE: this cluster is the cheap-eats, quack-doctors and
petty-price run (假人參 fake ginseng, 野雞 pheasant cabs/girls, 請醫生打保單 the
doctor's guarantee, 粥店/豆腐店/餛飩擔/客飯 the food stalls, 蘇廣成衣鋪 ready-made
clothiers, 冷攤 cold stalls, 日需房飯錢二百八十文 room-and-board at 280 cash,
小便三角大便一元 the privy toll, 靠災民發財的善棍 charity sharks, 廣告醫生
advertising doctors, 高等華人 "superior Chinese", 看鬼臉/十三點 street types,
尋人 missing persons). Expect Wu-dialect slang, food and price detail, and
quack-medicine cant: gloss it, keep the flavour, footnote generously. Recurring
furniture already noted, cross-ref do not re-note: money policy (大洋/小洋/毛/角/
分/文, ch001 & ch014), 白相人 hoodlum (glossed; decided rendering "hoodlum",
locked by the ch132 title), 洋盤 sucker (ch073), 野雞 pheasant (ch012/ch043),
弄堂 (ch063), 老虎灶 (ch063), the little pawnshops (ch062), 花會 huahui (ch065),
遊戲場 amusement halls (glossed), 跑馬廳 the Racecourse (ch082/ch089), 城隍廟
City God Temple (glossed), 洋人/租界 furniture. Crop-verify every name, number,
price and low-confidence span, recording verified readings in data/ocr_fixes.json.
Fact-check any real person or institution against real scholarship (Wikipedia /
Baidu Baike / academic, NEVER an LLM-written site such as Grok/Grokipedia);
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
ampersand; a figure "file" is a BARE filename and its "alt" must contain NO
double quotes), check_apparatus.py; regenerate check_config.json for the units
whose data/zh exists, then check_structure.py --config check_config.json +
check_content.py --config check_config.json + qc_entities.py PER BILINGUAL FILE
(qc_entities.py out/<id>_bilingual.md — it reads ONE bilingual file, NOT the
config; loop over units). Rebuild the EPUB, qa_epub.py until green, epubcheck
(jar at /tmp/epubcheck-5.1.0/epubcheck.jar). Record every result in PROGRESS.md;
commit and push claude/scales-and-claws. Do not pause for approval mid-batch.

Deliver in chat: the built EPUB attached, AND the B08 kickoff pasted verbatim
in a fenced code block in the same reply.
```

If the commissioner instead sends corrections to B01-B06, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B07.

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
  halls and street rackets. 87 notes (273-359), 47 glossary rows, 3 figures.
- B06 (2026-08-13): ch071-ch090 (賊技 through 場面不可不繃). Thieves, cheats,
  beggars and the transport trades. 88 notes (book-wide 360-447), 67 glossary
  rows, 5 reprint figures (ch072 Wu Zhihui + Rong Zongjing portraits; ch088
  Sheng Xuanhuai portrait, Zhu Baosan's tomb, Rue Chu-Pao-San). All gates green
  (verify_unit, check_align, check_apparatus, check_structure, check_content,
  qc_entities); qa_epub PASS; epubcheck 5.1.0 clean (0/0/0); check_register
  within tolerance on all 20. Fact-checks in PROGRESS (Wu Zhihui, Rong Zongjing
  & the 1934 Shenxin crisis, Chen Gongbo, the 1935 collective weddings, Beihai
  Road/1883, Sheng Xuanhuai's 1917 funeral, Zhu Baosan & Rue Chu-Pao-San, Huang
  Chujiu's 1931 death and dropped funeral all CORROBORATED; a Grokipedia hit
  DISREGARDED per rule 5).

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
- NOTE-BODY RULE (B02, reaffirmed B04/B05/B06): note/glossary bodies are inserted
  RAW into XHTML. STRAIGHT quotes, &#8211; for en-dashes in date ranges, &#8212;
  or a literal em dash for em dashes, <i> only (no <b>), numeric char refs never
  named entities, &#38; for a literal ampersand. When writing CJK into the batch
  JSON, RE-READ every character (near-homoglyph typos).
- FIGURE RULES: (a) a figure's "before" anchor MUST fall within the first ~80
  chars of the target paragraph (B02); (b) the "file" field is a BARE filename
  (e.g. ch088_shengxuanhuai.png), NOT a data/figs/ path, or the builder writes a
  broken images/data/figs/ src (B06); (c) the "alt" text is inserted RAW into an
  XML attribute, so it must contain NO double quotes (use single quotes) or the
  document is not well-formed and qa_epub fails (B06).
- ANCHOR GOTCHA (B05): note markers sit after closing punctuation; anchor on a
  phrase that does not straddle a closing quote.
- check_config.json (tracked): {docs,sources,notes,variants}. In a fresh
  container only the CURRENT batch's data/zh exists, so REGENERATE it each
  batch to the units whose data/zh EXISTS (glob data/zh/ch*.txt ->
  docs=out/<u>_reading.md, sources=data/zh/<u>.txt; keep notes/variants).
- verify_unit.py takes UNIT IDS ONLY and applies data/noise.txt itself; do NOT
  pass --noise. check_numbers.py DOES take --noise. check_structure/check_content
  take --config. qc_entities.py takes ONE BILINGUAL FILE (out/<id>_bilingual.md),
  NOT the config; loop over units. check_align.py takes ONE unit; loop.
- check_numbers quirks (running list): parses "a hundred" not "the/per hundred";
  reads a name's or idiom's digit as a numeral (朱葆三's 三, 丘八's 八); reads an
  abbreviated X、Y (三、四十) standalone tail as a numeral; 零 in 零落/有零 reads as
  0; 萬 in 萬事 reads as 10000. Fix with a TARGETED noise, never a broad one
  (rule 4: a noise rule only ever REMOVES a source numeral, never masks a drop).
- data/noise.txt: B03 added 北四川路, 十八、九, 長三, 么二, 老六. B04 added 黃楚九,
  九畝地, 億定盤路, 萬民矚目, 十餘萬, 塵煙四起. B05 added 巨萬, 零售, 百科, 十六浦,
  十幾萬, (?<=十一)、二. B06 added 有零, 萬事, 零落, 丘八, 朱葆三, 三、四十.
  Longest-first.
- data/ocr_fixes.json: crop-verified readings ledger. B06 added
  ch071/ch073/ch088/ch089 (pickpocket names, gold prices, Sheng/Zhu names,
  carriage counts).

## Renderings settled / carry-forward

- Voice (frozen at the ch001 gate): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, the author
  stepping in to editorialize. Held B02-B06. The B06 run is heavy on the author's
  moralizing close (叫魂, 大出喪, 場面不可不繃 each end on a wry editorial sigh);
  keep those closes pointed, not preachy.
- Money policy (recurs book-wide): 塊/元 = "dollar"; 大洋 = the standard silver
  dollar; 小洋 = "small silver"; 毛 = "*mao*"; 角 = "*jiao*"; 分 = "*fen*";
  文 = "cash" (period copper); 大錢 = "big cash"; 銅元/銅圓 = "copper". As an
  INTEREST rate, 分 = one per cent. Never flatten 毛/角 to "cents".
- Shelf-consistent names (authority.json): 南京路 Nanjing Road, 南市 Nanshi,
  捕房 police station, 霞飛路 Avenue Joffre, 靜安寺路 Bubbling Well Road,
  工部局 the Municipal Council, 公董局 the French Municipal Council. Author
  郁慕俠 = Yu Muxia; preface author 天虛我生 = Chen Diexian.
- B06 glossary DECIDED (reuse verbatim; grep before re-noting):
  People 楊金奎 Yang Jinkui, 韓才狗 Han Caigou, 吳稚暉 Wu Zhihui, 榮宗敬 Rong
  Zongjing, 陳公博 Chen Gongbo, 魯仲連 Lu Zhonglian, 盛宣懷/盛杏蓀 Sheng Xuanhuai,
  朱葆三 Zhu Baosan. Places 吳淞 Wusong, 虹口 Hongkou, 六馬路 Sixth Avenue (Beihai
  Road), 華界 the Chinese city, 江北 Jiangbei, 閘北 Zhabei. Orgs 龍飛(馬車行)
  Longfei, 雲飛汽車公司 Yunfei Motor Company, 龍園 Longyuan. Terms 扎兒手
  nimble-fingers, 失風 a job blew up, 吃豆腐 eating tofu, 標金 standard gold, 洋盤
  sucker, 吃盤子 eating the plate, 喜娘 wedding-matron, 二爺 second master,
  吃百家飯 eating from a hundred households, 集團結婚 group weddings, 叫魂
  soul-calling, 甲馬 spirit-paper, 麻衣債 mourning-cloth debt, 印子鈿 stamp-money,
  公子哥兒 young master, 興隆票 prosperity note, 阿羊哥 Brother Sheep, 屈死
  Wronged-to-Death, 麥克麥克 muchee-muchee, 水鬼 water ghost, 花柳 flower-and-willow,
  賣羊 selling sheep, 賣相 salable looks, 包探 detective, 掮客 broker, 沖鳥 flushing
  the birds, 小開 young boss, 沖喜 turning the luck, 大照會 big license, 黃包車
  rickshaw, 丘八 soldier, 漂亮人物 swell, 飛毛腿 flying legs, 小車 wheelbarrow,
  狗頭車 dog's-head cart, 東洋車 rickshaw, 大出喪 grand funeral, 送喪馬車 funeral
  carriage, 寓公 idle rich sojourner, 繃場面 keeping up appearances, 堂倌 waiter.
- 白相人 = "hoodlum" (glossed earlier, en corrected-in-use to fit): the decided
  rendering is "hoodlum", locked by the ch132 title "The Hoodlum's Missus". Its
  literal "man-about-town / idler" sense is footnoted once (ch072). Render it
  "hoodlum" wherever 白相人 appears, or qc_entities fails.
- Earlier-batch glossary (reuse verbatim): 袁世凱 Yuan Shikai, 黃楚九 Huang Chujiu,
  申報 Shenbao, 新聞報 Xinwenbao; 四馬路 Fourth Avenue (福州路), 北四川路 North
  Sichuan Road, 霞飛路 Avenue Joffre; numbered "Avenues" 大馬路=Nanjing,
  二馬路=Jiujiang, 三馬路=Hankou, 四馬路=Fuzhou, 五馬路=Guangdong, 六馬路=Beihai;
  新世界 New World; 大世界 Great World.
- No continuing cast (essay collection); recurring historical names handled by
  the glossary, not voice sheets.

## Where the book stands

- Ninety-one of 168 units done (preface + 90 essays). 77 essays remain. No plot
  to track; the register decisions in B01 govern everything downstream. Internal
  dating runs ~1856 (Wills Bridge) to the mid-1930s (1934 Shenxin crisis, 1935
  collective weddings surfaced in B06).

## Next batch scope

- B07 = ch091-ch110, PDF 159-183, printed 157-181. Fake ginseng, pheasant cabs
  and girls, the doctor's guarantee, the food-stall economy (congee, tofu,
  wontons, set meals, cold stalls), ready-made clothiers, room-and-board and
  privy tolls, charity sharks, advertising doctors, "superior Chinese", street
  types (十三點, 看鬼臉), and missing persons. The cheap-eats-and-quacks cluster:
  food and price detail, Wu slang, quack-medicine cant. Offset still printed =
  pdf - 2.

## Open traps and environment state

- MULTI-PAGE UNITS B07: ch091 (159-160), ch100 (170-171), ch105 (176-178).
  Watch the folio at every opener; eyeball every page for reprint photos.
- This is the 2019 RESET, not the 1933 original: no collation source. Where the
  reprint is suspect, note it; do not guess the 1933 reading. Reprint misprints
  seen so far: ch052 味蒓園 (TOC), ch053 經營三 for 經潤三. Render as printed,
  translate to the attested form where one exists, footnote the discrepancy.
- Source SELF-CENSORSHIP: the reprint blanks words as ×× (clinics, a steamship
  line, poetry societies). Render as printed, footnote.
- Vertical RTL OCR column-order errors are silent; verify assemble output by
  eye. A text band ABOVE a photo may have no internal short-column break (one
  paragraph): ch063 and ch088 were.
- Magnified crops can clip a character's top strokes and misread it (三 read as
  一 at ch057; 奎 read as 大 at ch071); when a digit or name is load-bearing,
  crop generously top and bottom.
- Two essays share PDF 214 (ch135/ch136) and two share PDF 218 (ch140/ch141):
  unit boundaries mid-page (B08/B10), watch the parity split.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset
  printed = pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- Pagemap: only ch000/ch001 carry data/pagemap (B01); essays ship without
  followable page-list entries (consistent B02-B06). Notes cite printed folios.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template
  stub") — HANDOFF carries a real kickoff, so the Stop hook correctly enters
  its enforcing path. Working as designed.
