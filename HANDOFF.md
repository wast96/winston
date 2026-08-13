# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

```
Scales and Claws B08

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu
Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; 2019 Taipei reprint,
customs volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the
harness to start you on a stray branch and consolidate per rule 2 (check out the
canonical branch, reset it to origin, do the work there, delete the stray). This
book's PR history through B07 is already merged, so if the designated branch
carries only merged history, restart it from origin. Deliverable
out/scales-and-claws-of-shanghai.epub.

Do Batch B08 = ch111-ch129 (俞調、馬調 through 兜得轉與跑得開; PDF 184-208, printed
folios 182-206) end to end per the CLAUDE.md pipeline: ./setup.sh; render 184 208
--dpi 300; OCR with the B01-B07 crop (ocr_crop.py --left 0.03 --right 0.97
--top 0.13 --bottom 0.95 --lang chi_tra_vert --psm 5, tighter --bottom on any
page carrying a reprint photo). tesseract on this vertical-Traditional reset is
only ~85% and too error-dense to trust: EYE-READ every page at magnification and
hand-transcribe data/zh against the scans, exactly as B01-B07 did. indents.py is
UNUSABLE here; assemble on the blank-line signal and finalize paragraph
structure BY HAND against the scan, using the short-line signal at the page
seams (and note that where a text band sits above a reprint photo there may be
NO internal short-column break, so the band can be a single paragraph, as ch063,
ch088 and ch100 were; on a photo-only page like pdf 171 the unit's text finished
on the PREVIOUS page). pgrep -c tesseract must be 0 after OCR. Eyeball every page
for reprint-added photos and run each through the figure pipeline (crop to
data/figs/ with a BARE filename, not a data/figs/ path; alt text with NO double
quotes since it is inserted raw into an XML attribute; caption translating any
reprint label and stating 2019-editor provenance; exclude the printed caption
line from the crop).

MULTI-PAGE UNITS in this batch: ch112 (PDF 185-186), ch114 大少爺謀害妓女 (188-190,
a 3-page narrative and a likely spot for a courtesan/scandal photo), ch115
(191-192), ch118 (195-196), ch120 (198-199). Re-read the folio off the scan at
every opener; offset stays printed = pdf - 2 but VERIFY it.

BEFORE translating, read the final two pages of out/ch110_reading.md: HANDOFF
describes the voice, but those pages ARE the voice; the FROZEN reference is
still out/ch001_reading.md. Run check_register.py --ref out/ch001_reading.md on
every unit. Consult glossary.json and authority.json BEFORE romanizing any
name. THEMATIC NOTE: this cluster runs from tanci balladry and quack-medicine
cant into the con-and-beggar trades (俞調/馬調 the ballad tunes named for the
singers Yu Xiushan and Ma Rufei, 醫生的三嚇頭 the doctor's three scares, 開大炮
firing the big gun = brazen bluff, 大少爺謀害妓女 a rich young master murders a
courtesan, 燙頭髮 permanent waves, 跑狗癮 the greyhound-racing habit at the
Canidrome, 么二三式 the one-two-three brothel style, 捏腳 foot-pinching,
水門汀上告狀 petitions on the pavement, 專做外國生意的乞丐 beggars who work only
foreigners, 趕豬玀/殺豬玀 driving and slaughtering the "pigs" = fleecing country
marks, 拿開銷/講斤頭 taking the payoff and haggling the cut, 賞光券 patronage
tickets, 戤牌頭 trading on a big name, 兜得轉與跑得開 getting around and getting
away). Expect Wu-dialect swindler cant, brothel/entertainment furniture and a
long narrative piece (ch114). Gloss it, keep the flavour, footnote generously.
Recurring furniture already noted, cross-ref do not re-note: money policy
(大洋/小洋/毛/角/分/文, ch001 & ch014), 白相人 hoodlum (decided rendering
"hoodlum", locked by ch132), 野雞 pheasant (ch012/ch043/ch093), 么二 yao-er and
長三 changsan (ch019/ch003-era brothel grades, B03), 弄堂 (ch063), 洋盤 sucker
(ch073), 掮客 broker (B06), 揩油 skim (ch098/B07), 賞光券 patronage tickets
(introduced ch093/ch128), 城隍廟 City God Temple (ch001), 跑馬廳 the Racecourse
(ch082/ch089), 遊戲場 amusement halls, 洋人/租界 furniture. Crop-verify every
name, number, price and low-confidence span, recording verified readings in
data/ocr_fixes.json. Fact-check any real person or institution against real
scholarship (Wikipedia / Baidu Baike / academic, NEVER an LLM-written site such
as Grok/Grokipedia); state the verdict in the note. Never invent bridging text;
verify each unit's tail against the scan.

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

Deliver in chat: the built EPUB attached, AND the B09 kickoff pasted verbatim
in a fenced code block in the same reply.
```

If the commissioner instead sends corrections to B01-B07, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B08.

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
  beggars and the transport trades. 88 notes (360-447), 67 glossary rows,
  5 reprint figures.
- B07 (2026-08-13): ch091-ch110 (假人參 through 尋人). Cheap-eats, quack-doctors
  and petty-price cluster. 42 notes (book-wide 448-489), 33 glossary rows,
  4 reprint figures (ch096 Feng Zikai wonton cartoon; ch098 Su-Guang clothier
  stall; ch099 City God Temple book market; ch100 theater boxes). All gates
  green (verify_unit, check_align, check_apparatus, check_structure,
  check_content, qc_entities); qa_epub PASS; epubcheck 5.1.0 clean (0/0/0);
  check_register within tolerance on all 20. Fact-checks in PROGRESS (Dangui
  First Stage/Xu Shaoqing, Lao Dafang's 48-shops name-dispute, Northeast
  Volunteer Army fund scandal, Feng Zikai all handled; the ch109 呆戀 misprint
  rendered to sense and footnoted).

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
- NOTE-BODY RULE (B02, reaffirmed B04-B07): note/glossary bodies are inserted
  RAW into XHTML. STRAIGHT quotes, &#8211; for en-dashes in date ranges, &#8212;
  or a literal em dash for em dashes, <i> only (no <b>), numeric char refs never
  named entities, &#38; for a literal ampersand. When writing CJK into the batch
  JSON, RE-READ every character (near-homoglyph typos).
- FIGURE RULES: (a) a figure's "before" anchor MUST fall within the first ~80
  chars of the target paragraph (B02); (b) the "file" field is a BARE filename
  (e.g. ch100_theatre_boxes.png), NOT a data/figs/ path (B06); (c) the "alt"
  text is inserted RAW into an XML attribute, so it must contain NO double quotes
  (B06); (d) crop OUT the reprint's own printed caption line — write your own
  caption stating 2019-editor provenance (B07).
- ANCHOR GOTCHA (B05/B07): note markers sit after the anchor; pick an anchor
  that does NOT end just before a closing quote or an em dash — choose a plain
  word-run inside the sentence.
- check_config.json (tracked): {docs,sources,notes,variants}. In a fresh
  container only the CURRENT batch's data/zh exists, so REGENERATE it each
  batch to the units whose data/zh EXISTS (glob data/zh/ch*.txt ->
  docs=out/<u>_reading.md, sources=data/zh/<u>.txt; keep notes/variants).
- verify_unit.py takes UNIT IDS ONLY and applies data/noise.txt itself; do NOT
  pass --noise. check_numbers.py DOES take --noise. check_structure/check_content
  take --config. qc_entities.py takes ONE BILINGUAL FILE (out/<id>_bilingual.md),
  NOT the config; loop over units. check_align.py takes ONE unit; loop. NOTE:
  when eyeballing verify_unit output over 20 units, GREP for FAIL — a plain
  tail truncates the early units (bit me once in B07).
- check_numbers quirks (running list): parses "a hundred" not "the/per hundred";
  reads a name's or idiom's digit as a numeral; reads an abbreviated X、Y tail as
  a numeral; 零 in 零落/有零 reads as 0; 萬 in 萬事 reads as 10000. Fix with a
  TARGETED noise, never a broad one (rule 4: a noise rule only REMOVES a source
  numeral, never masks a drop).
- data/noise.txt (longest-first): B03 added 北四川路, 十八、九, 長三, 么二, 老六.
  B04 added 黃楚九, 九畝地, 億定盤路, 萬民矚目, 十餘萬, 塵煙四起. B05 added 巨萬,
  零售, 百科, 十六浦, 十幾萬, (?<=十一)、二. B06 added 有零, 萬事, 零落, 丘八,
  朱葆三, 三、四十. B07 added 五方雜處, 四出, (?<=十五)、六, 五官.
- data/ocr_fixes.json: crop-verified readings ledger.

## Renderings settled / carry-forward

- Voice (frozen at the ch001 gate): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, the author
  stepping in to editorialize. Held B02-B07. The B07 run leans satirical and
  moralizing at the close (善棍, 高等華人, 尋人 each end on a wry or indignant
  editorial turn — the anti-collaboration bite of 高等華人/亡國奴 is period-real,
  keep it pointed not preachy).
- Money policy (recurs book-wide): 塊/元 = "dollar"; 大洋 = the standard silver
  dollar; 小洋 = "small silver"; 毛 = "*mao*"; 角 = "*jiao*"; 分 = "*fen*";
  文 = "cash" (period copper); 制錢 = "standard coin/cash"; 銅圓/銅板 = "copper".
  As an INTEREST rate, 分 = one per cent. Never flatten 毛/角 to "cents". 鈿 is
  Wu for money/cash; render by context (工鈿 = "labor cost"; 一百鈿 = the cash
  reckoning it is explicitly glossed as).
- Shelf-consistent names (authority.json): 南京路 Nanjing Road, 南市 Nanshi,
  捕房 police station, 霞飛路 Avenue Joffre, 靜安寺路 Bubbling Well Road,
  工部局 the Municipal Council, 公董局 the French Municipal Council. Author
  郁慕俠 = Yu Muxia; preface author 天虛我生 = Chen Diexian.
- 白相人 = "hoodlum" (locked by the ch132 title "The Hoodlum's Missus"); render
  it "hoodlum" wherever 白相人 appears, or qc_entities fails. Its literal
  "man-about-town" sense footnoted once (ch072).
- B07 glossary DECIDED (reuse verbatim; grep before re-noting):
  People 許少卿 Xu Shaoqing, 豐子愷 Feng Zikai. Places 吉林 Jilin, 營口 Yingkou,
  老北門 Old North Gate. Orgs 丹桂第一台 Dangui First Stage, 東北義勇軍 Northeast
  Volunteer Army, 老大房 Lao Dafang, 稻香村 Daoxiangcun, 野荸薺 Yebiqi, 天祿 Tianlu
  (provisional), 致美樓 Zhimei Lou, 煙兌店 opium-and-exchange shop. Terms 人參
  ginseng, 虛頭 empty trick, 客飯 set meal, 冷攤 cold stall, 善棍 charity shark,
  高等華人 superior Chinese, 起碼華人 common Chinese, 十三點 Thirteen O'Clock,
  鬼臉 ghost-face, 保單 guarantee, 綁票 kidnapping, 拐子 kidnapper, 制錢 standard
  coin, 客棧 guest-lodge, 茶房 tea-boy, 燻魚 smoked fish, 酥糖 crisp candy, 餛飩
  wonton, 買辦 comprador, 揩油 skim (title of ch152).
- Earlier-batch glossary (reuse verbatim): 城隍廟 City God Temple, 野雞 pheasant,
  麥克麥克 muchee-muchee, 寓公 idle rich sojourner, 錢莊 native bank, 探捕
  plain-clothes constable, 包探 detective, 老虎灶 tiger stove, 弄堂 lane, 洋盤
  sucker, 花會 huahui, 么二/長三 brothel grades (B03); numbered "Avenues"
  大馬路=Nanjing, 二馬路=Jiujiang, 三馬路=Hankou, 四馬路=Fuzhou(福州路),
  五馬路=Guangdong, 六馬路=Beihai; 申報 Shenbao, 新聞報 Xinwenbao.
- No continuing cast (essay collection); recurring historical names handled by
  the glossary, not voice sheets.

## Where the book stands

- 111 of 168 units done (preface + 110 essays). 57 essays remain. No plot to
  track; the register decisions in B01 govern everything downstream. Internal
  dating runs ~1856 (Wills Bridge) to the mid-1930s; B07 adds the ~1933
  Northeast Volunteer Army fund scandal (ch105) and the early-1930s anti-Japanese
  anxiety of 高等華人 (ch107).

## Next batch scope

- B08 = ch111-ch129, PDF 184-208, printed 182-206. Tanci ballad tunes, the
  doctor's three scares and "firing the big gun", a young master's murder of a
  courtesan (ch114, a 3-page narrative), permanent waves, greyhound racing,
  brothel styles, foot-pinching, pavement petitions, foreigner-working beggars,
  the "driving/slaughtering the pigs" con games, payoffs and cuts, patronage
  tickets, trading on a big name. Offset still printed = pdf - 2.

## Open traps and environment state

- MULTI-PAGE UNITS B08: ch112 (185-186), ch114 (188-190, 3pp), ch115 (191-192),
  ch118 (195-196), ch120 (198-199). Watch the folio at every opener; eyeball
  every page for reprint photos (ch114 is a likely spot).
- This is the 2019 RESET, not the 1933 original: no collation source. Where the
  reprint is suspect, note it; do not guess the 1933 reading. Reprint misprints
  seen so far: ch052 味蒓園 (TOC), ch053 經營三 for 經潤三, ch109 呆戀 (probable
  reset error for 呆戇, rendered to sense + footnoted). Render as printed,
  translate to the attested/plain-sense form, footnote the discrepancy.
- Source SELF-CENSORSHIP: the reprint blanks words as ×× (clinics, a steamship
  line, poetry societies). Render as printed, footnote. NOTE: in ch110 the ××
  are the AUTHOR's own "such-and-such" placeholders in a specimen notice, not
  censorship — read by context.
- Vertical RTL OCR column-order errors are silent; verify assemble output by
  eye. A text band ABOVE a photo may have no internal short-column break (one
  paragraph): ch063, ch088, ch100 were. A photo-only page (pdf 171) means the
  unit's text finished on the previous page — do not hunt for missing paragraphs.
- Magnified crops can clip a character's top strokes and misread it; when a
  digit or name is load-bearing, crop generously top and bottom (and re-zoom at
  4-6x, as done for ch103 拆洋濫污 and the ch109 呆戀 glyph).
- Two essays share PDF 214 (ch135/ch136) and two share PDF 218 (ch140/ch141):
  unit boundaries mid-page (B09/B10), watch the parity split.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset
  printed = pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- Pagemap: only ch000/ch001 carry data/pagemap (B01); essays ship without
  followable page-list entries (consistent B02-B07). Notes cite printed folios.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template
  stub") — HANDOFF carries a real kickoff, so the Stop hook correctly enters
  its enforcing path. Working as designed.
