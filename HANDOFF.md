# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

```
Scales and Claws B09

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu
Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; 2019 Taipei reprint,
customs volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the
harness to start you on a stray branch and consolidate per rule 2 (check out the
canonical branch, reset it to origin, do the work there, delete the stray). This
book's PR history through B08 is already merged, so if the designated branch
carries only merged history, restart it from origin. Deliverable
out/scales-and-claws-of-shanghai.epub.

Do Batch B09 = ch130-ch155 (兜得轉與跑得開 through 兩個半滑頭; PDF 209-233, printed
folios 207-231) end to end per the CLAUDE.md pipeline: ./setup.sh; render 209 233
--dpi 300; OCR with the B01-B08 crop (ocr_crop.py --left 0.03 --right 0.97
--top 0.13 --bottom 0.95 --lang chi_tra_vert --psm 5, tighter --bottom on any
page carrying a reprint photo). tesseract on this vertical-Traditional reset is
only ~85% and too error-dense to trust: EYE-READ every page at magnification and
hand-transcribe data/zh against the scans, exactly as B01-B08 did. indents.py is
UNUSABLE here; assemble on the blank-line signal and finalize paragraph
structure BY HAND against the scan, using the short-line signal at the page
seams (and note that where a text band sits above a reprint photo there may be
NO internal short-column break, so the band can be a single paragraph, as ch063,
ch088, ch100 and ch114 were). pgrep -c tesseract must be 0 after OCR. Eyeball
every page for reprint-added photos and run each through the figure pipeline
(crop to data/figs/ with a BARE filename, not a data/figs/ path; alt text with
NO double quotes since it is inserted raw into an XML attribute; caption
translating any reprint label and stating 2019-editor provenance; exclude the
printed caption line from the crop).

TWO ESSAYS SHARE A PAGE (watch the parity split, the unit boundary is mid-page):
ch135 頂呱呱與硬繃繃 and ch136 拋頂宮 both on PDF 214; ch140 賣性照片 and ch141
賣冰 both on PDF 218. Also PDF 231 (printed 229) is SKIPPED in the numbering
between ch153 (pdf 230) and ch154 (pdf 232): check whether it is a blank, a
plate, or a mis-count, and read the folio off the scan. Offset stays printed =
pdf - 2 but VERIFY it at every opener.

BEFORE translating, read the final two pages of out/ch129_reading.md and, for the
voice, the last two pages of out/ch114_reading.md (the long narrative): HANDOFF
describes the voice, but those pages ARE the voice; the FROZEN reference is still
out/ch001_reading.md. Run check_register.py --ref out/ch001_reading.md on every
unit. Consult glossary.json and authority.json BEFORE romanizing any name.
THEMATIC NOTE: this cluster is the swindler/beggar/street-trade heart of the
book — kidnappers (綁匪), the hoodlum's wife (白相人嫂嫂, note the locked rendering
"hoodlum" for 白相人, and 嫂嫂), cricket-fighting (捉蟋蟀), the "three-lights gang"
(三光黨), Wu-slang tags 頂呱呱/硬繃繃, hat-snatching (拋頂宮), a long run of
selling-cons (買戶頭 buying a mark, 買爛東西, 賣長錠 fake ingots, 賣性照片, 賣冰
= selling "ice"/fake goods, 賣書畫, 賣經), rag-and-bone trades (撈錫箔灰, 拾荒),
two dialect-word essays (上海人的「老」字, 寧波人的「阿」字), fortune-telling
(算命), 還魂煙 (resurrection cigarettes = re-rolled butts), tattooing (刺花),
吃講茶 (settling disputes over teahouse "judgment tea"), 揩油 (skim — the decided
rendering, title of this ch152; glossary), 儲蓄騙 savings swindles, 孵豆芽, and
兩個半滑頭. Expect dense Wu-dialect cant; gloss it, keep the flavour, footnote
generously. Recurring furniture already noted, cross-ref do not re-note: money
policy (大洋/小洋/毛/角/分/文, ch001 & ch014), 白相人 hoodlum (decided "hoodlum",
locked by ch132's title 白相人嫂嫂; literal "man-about-town" sense noted ch072),
野雞 pheasant (ch012/ch043/ch093), 么二/長三 brothel grades (B03), 弄堂 (ch063),
洋盤 sucker (ch073), 掮客 broker (B06), 揩油 skim (ch098/B07, and ch152 is its own
essay), 綁票/拐子 kidnapping/kidnapper (B07 ch104), 癟三 biesan (ch123), 城隍廟
(ch001), 跑馬廳 the Racecourse (ch082/ch089), 洋涇浜 pidgin (ch018/ch078), 洋人/
租界 furniture. Crop-verify every name, number, price and low-confidence span,
recording verified readings in data/ocr_fixes.json. Fact-check any real person or
institution against real scholarship (Wikipedia / Baidu Baike / academic, NEVER
an LLM-written site such as Grok/Grokipedia); state the verdict in the note.
Never invent bridging text; verify each unit's tail against the scan.

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
quotes or numeric char refs, &#8211; for en-dashes in date ranges, &#8212; for em
dashes, <i> only, numeric char refs never named entities, and &#38; for any
literal ampersand; a figure "file" is a BARE filename and its "alt" must contain
NO double quotes), check_apparatus.py; regenerate check_config.json for the units
whose data/zh exists, then check_structure.py --config check_config.json +
check_content.py --config check_config.json + qc_entities.py PER BILINGUAL FILE
(qc_entities.py out/<id>_bilingual.md — it reads ONE bilingual file, NOT the
config; loop over units). WATCH qc_entities: an EXISTING glossary hanzi that
appears in your source (even as a substring, e.g. 么二 inside 么二三式) must have
its ledger rendering in your English, or use the ledger's word (B08 aligned
舞女=dance-girl, 堂倌=waiter, 拆字=character-splitting). Rebuild the EPUB, qa_epub.py
until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar). Record every
result in PROGRESS.md; commit and push claude/scales-and-claws. Do not pause for
approval mid-batch.

Deliver in chat: the built EPUB attached, AND the B10 kickoff pasted verbatim
in a fenced code block in the same reply.
```

If the commissioner instead sends corrections to B01-B08, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B09.

## What is DONE (do not redo)

- Survey (2026-08-10): source characterized, book.json complete, skeleton EPUB
  green, batch plan + 3 standing decisions approved, photos ruled IN.
- B01 (2026-08-11): ch000 (序) + ch001 (上海人的過年忙). Voice gate PASSED;
  ch001 is the FROZEN register reference. 25 notes, 22 glossary rows, 5 figures.
- B02 (2026-08-11): ch002-ch014 (宋案的回顧 through 跳舞). 93 notes, 25 rows, 13 figs.
- B03 (2026-08-12): ch015-ch034 (肉林秘聞 through 女相士). 93 notes, 32 rows, 0 figs.
- B04 (2026-08-12): ch035-ch052 (一杯茶值五大元 through 味蒓園). 61 notes, 36 rows, 2 figs.
- B05 (2026-08-12): ch053-ch070 (新世界的隧道 through 裱畫店之換天頭). 87 notes, 47 rows, 3 figs.
- B06 (2026-08-13): ch071-ch090 (賊技 through 場面不可不繃). 88 notes, 67 rows, 5 figs.
- B07 (2026-08-13): ch091-ch110 (假人參 through 尋人). 42 notes, 33 rows, 4 figs.
- B08 (2026-08-13): ch111-ch129 (俞調、馬調 through 戤牌頭). Tanci/quack-medicine
  into the con-and-beggar trades. 66 notes (book-wide 490-555), 49 glossary rows,
  3 reprint figures (all ch114: the Yan-Wang portraits, the 1920 Shenbao ad, the
  New Stage playbill). book.json ch116 title_en corrected "The New Year Red
  Lantern" -> "Neon Lights" (the essay is about neon signs). All gates green;
  qa_epub PASS; epubcheck 5.1.0 clean (0/0/0); check_register within tolerance on
  all 19. Fact-checks in PROGRESS (Yan Ruisheng case date CONTRADICTED — 1920 not
  1922; He Fenglin, Yu Xiushan/Ma Rufei, Yan Duhe, the three dog-tracks, Twin
  Sisters, Aurora, 花國總理, New Life all corroborated).

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
- NOTE-BODY RULE: note/glossary bodies are inserted RAW into XHTML. STRAIGHT
  quotes or numeric char refs (B08 used &#8220;/&#8221;/&#8217; freely — both are
  fine), &#8211; for en-dashes, &#8212; for em dashes, <i> only (no <b>), numeric
  char refs never named entities, &#38; for a literal ampersand. When writing CJK
  into the batch JSON, RE-READ every character (near-homoglyph typos).
- FIGURE RULES: (a) a figure's "before" anchor MUST fall within the first ~80
  chars of the target paragraph (B02) — MULTIPLE figures may share one paragraph's
  anchor and stack before it in list order (B08 put 2 figs before ch114 para1);
  (b) the "file" field is a BARE filename (B06); (c) the "alt" text is inserted
  into an XML attribute — keep it free of double quotes (B06); (d) crop OUT the
  reprint's own printed caption line — write your own caption stating 2019-editor
  provenance (B07).
- ANCHOR GOTCHA (B05/B07/B08): the note marker sits right after the anchor
  string. Pick an anchor that is a plain word-run INSIDE the sentence — NOT one
  ending just before a closing quote or an em dash (both collide). Ending before a
  comma/period/paren is fine. B08 systematically chose mid-sentence runs.
- QC_ENTITIES GOTCHA (B08): qc requires every glossary hanzi in a source
  paragraph to have its ledger rendering (full en, its pinyin, or the en's first
  OR last word) in the paired English. Watch (1) SUBSTRING collisions with
  existing keys (么二 inside 么二三式 forced "yao-er" into the ch119 rendering);
  (2) existing terms whose ledger word differs from your natural choice — align to
  the ledger (B08: 舞女=dance-girl, 堂倌=waiter, 拆字=character-splitting). Every
  glossary rec MUST carry a "pinyin" key or qc throws KeyError.
- check_config.json (tracked): {docs,sources,notes,variants}. In a fresh
  container only the CURRENT batch's data/zh exists, so REGENERATE it each batch
  to the units whose data/zh EXISTS (glob data/zh/ch*.txt -> docs=out/<u>_reading.md,
  sources=data/zh/<u>.txt; keep notes/variants).
- verify_unit.py takes UNIT IDS ONLY and applies data/noise.txt itself; do NOT
  pass --noise. check_numbers.py DOES take --noise. check_structure/check_content
  take --config. qc_entities.py takes ONE BILINGUAL FILE; loop over units.
  check_align.py takes ONE unit; loop. GREP verify_unit output for FAIL over many
  units (a plain tail truncates the early ones).
- check_numbers quirks (running list): parses "a hundred" not "the/per hundred";
  reads a name's or idiom's digit as a numeral; reads an abbreviated X、Y tail as
  a numeral; 零 in 零落/有零 reads as 0; 萬 in 萬事 reads as 10000; weekday numerals
  (禮拜三、六) read as 3/6. Fix with a TARGETED noise, never a broad one.
- data/noise.txt (longest-first): B03 added 北四川路, 十八、九, 長三, 么二, 老六.
  B04 added 黃楚九, 九畝地, 億定盤路, 萬民矚目, 十餘萬, 塵煙四起. B05 added 巨萬,
  零售, 百科, 十六浦, 十幾萬, (?<=十一)、二. B06 added 有零, 萬事, 零落, 丘八,
  朱葆三, 三、四十. B07 added 五方雜處, 四出, (?<=十五)、六, 五官. B08 added
  禮拜三、六 (Wed & Sat), 癟三 (biesan).
- data/ocr_fixes.json: crop-verified readings ledger.

## Renderings settled / carry-forward

- Voice (frozen at the ch001 gate): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, the author
  stepping in to editorialize. Held B02-B08. B08 adds a marquee narrative piece
  (ch114, the Yan Ruisheng murder) handled as reportage, and a run of short,
  wry sketches of the swindler/beggar trades closing on the author's sardonic
  asides (呵呵！; "is that not detestable?"; the "duck-piss" idiom).
- Money policy (recurs book-wide): 塊/元 = "dollar"; 大洋 = the standard silver
  dollar; 小洋 = "small silver"; 毛 = "*mao*"; 角 = "*jiao*"; 分 = "*fen*";
  文 = "cash"; 制錢 = "standard coin/cash"; 銅圓/銅板 = "copper". As an INTEREST
  rate, 分 = one per cent. Never flatten 毛/角 to "cents". 鈿 is Wu for money
  (大洋鈿 = the silver-dollar cash, rendered "silver dollars").
- Shelf-consistent names (authority.json): 南京路 Nanjing Road, 南市 Nanshi,
  捕房 police station, 霞飛路 Avenue Joffre, 靜安寺路 Bubbling Well Road, 工部局
  the Municipal Council, 公董局 the French Municipal Council, 蘇州河 Suzhou Creek,
  跑馬廳 the Racecourse. Author 郁慕俠 = Yu Muxia; preface author 天虛我生 = Chen
  Diexian.
- 白相人 = "hoodlum" (locked by the ch132 title "The Hoodlum's Missus"); render it
  "hoodlum" wherever 白相人 appears, or qc_entities fails. Literal "man-about-town"
  sense footnoted once (ch072); the author re-glosses it 即流氓 at ch127.
- B08 glossary DECIDED (reuse verbatim; grep before re-noting):
  People 俞秀山 Yu Xiushan, 馬如飛 Ma Rufei, 閻瑞生 Yan Ruisheng, 王蓮英 Wang
  Lianying, 何豐林 He Fenglin, 吳春芳 Wu Chunfang, 朱稚嘉 Zhu Zhijia, 朱葆三 Zhu
  Baosan, 趙君玉 Zhao Junyu, 汪優遊 Wang Youyou, 嚴獨鶴 Yan Duhe, 浦驚鴻 Pu
  Jinghong. Places 福祥里 Fuxiang Li, 徐州 Xuzhou, 九畝地 Jiumudi, 震旦大學 Aurora
  University, 亞爾倍路 Avenue du Roi Albert, 華德路 Ward Road, 延平路 Yanping Road.
  Orgs 新舞臺 the New Stage, 淞滬護軍使 the Songhu Defence Commissioner, 逸園 the
  Canidrome, 明園 the Mingyuan, 申園 the Shenyuan. Terms 開篇 prelude-song, 彈詞
  tanci, 三嚇頭 the three scares, 脈案 pulse-record, 嗎啡 morphine, 白麵 white flour,
  開大炮 firing the big gun, 紅白丸 red-and-white pills, 花國總理 Premier of the
  Flower Kingdom, 拆白黨 peeling-white gang, 新生活 New Life, 年紅燈 year-red lamp,
  霓紅燈 neon lamp, 桂花 sweet osmanthus, 跑狗 dog racing, 回力球 jai alai, 水門汀
  cement, 蟹行文字 crab-crawling script, 癟三 biesan, 釘巴 limpet, 趕豬玀 driving the
  pigs, 殺豬玀 slaughtering the pigs, 拿開銷 taking the payoff, 講斤頭 haggling the
  cut, 賞光券 patronage ticket, 打抽風 squeeze, 戤牌頭 trading on a big name, 案目
  seat-agent. Also aligned to ledger this batch: 舞女 dance-girl, 堂倌 waiter,
  拆字 character-splitting.
- Earlier-batch glossary (reuse verbatim): 城隍廟 City God Temple, 野雞 pheasant,
  麥克麥克 muchee-muchee, 寓公 idle rich sojourner, 錢莊 native bank, 探捕
  plain-clothes constable, 包探 detective, 老虎灶 tiger stove, 弄堂 lane, 洋盤
  sucker, 花會 huahui, 么二/長三 brothel grades; numbered "Avenues" 大馬路=Nanjing,
  二馬路=Jiujiang, 三馬路=Hankou, 四馬路=Fuzhou(福州路), 五馬路=Guangdong,
  六馬路=Beihai; 申報 Shenbao, 新聞報 Xinwenbao.
- No continuing cast (essay collection); recurring historical names handled by
  the glossary, not voice sheets.

## Where the book stands

- 130 of 168 units done (preface + 129 essays). 38 essays remain (B09 = 26,
  B10 = 12). No plot to track; the register decisions in B01 govern everything
  downstream. Internal dating runs ~1856 to the mid-1930s; B08 pins several
  essays to 1934 (Twin Sisters "this spring", ch114; the New Life perm ban,
  ch115) and revisits the 1920 Yan Ruisheng case (ch114).

## Next batch scope

- B09 = ch130-ch155, PDF 209-233, printed 207-231. Kidnappers, the hoodlum's
  wife, cricket-fighting, the three-lights gang, a long run of selling-cons and
  rag trades, two dialect-word essays, fortune-telling, resurrection cigarettes,
  tattooing, judgment tea, skimming, savings swindles. Offset printed = pdf - 2.

## Open traps and environment state

- SHARED PAGES B09 (unit boundary mid-page — watch the parity split): ch135
  頂呱呱與硬繃繃 & ch136 拋頂宮 both on PDF 214; ch140 賣性照片 & ch141 賣冰 both
  on PDF 218. Read each unit's start/end off the scan.
- NUMBERING GAP B09: PDF 231 (printed 229) is skipped between ch153 (pdf 230)
  and ch154 (pdf 232). Check whether it is a blank verso, a full-page plate, or
  a mis-count; read the folio off the scan and record what it is.
- This is the 2019 RESET, not the 1933 original: no collation source. Where the
  reprint is suspect, note it; do not guess the 1933 reading. Reprint misprints
  seen so far: ch052 味蒓園 (TOC), ch053 經營三 for 經潤三, ch109 呆戀, ch116
  年紅燈 title mistranslation (fixed), ch122 橋塊 for 橋堍. Render as printed,
  translate to the attested/plain-sense form, footnote the discrepancy.
- Source SELF-CENSORSHIP: the reprint blanks words as ×× (clinics, a steamship
  line, poetry societies; a film company in ch114). Render as printed, footnote.
  NOTE: in ch110 the ×× were the AUTHOR's own "such-and-such" placeholders, not
  censorship — read by context.
- Vertical RTL OCR column-order errors are silent; verify assemble output by eye.
  A text band ABOVE a photo may have no internal short-column break (one
  paragraph): ch063, ch088, ch100, ch114. A photo-only page means the unit's
  text finished on the previous page (ch100 p171; ch114 p190) — do not hunt for
  missing paragraphs.
- Magnified crops can clip a character's top strokes; when a digit or name is
  load-bearing, crop generously and re-zoom at 4-6x.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset
  printed = pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- Pagemap: only ch000/ch001 carry data/pagemap (B01); essays ship without
  followable page-list entries (consistent B02-B08). Notes cite printed folios.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template stub")
  — HANDOFF carries a real kickoff, so the Stop hook correctly enters its
  enforcing path. Working as designed.
