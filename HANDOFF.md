# HANDOFF — Scales and Claws of Shanghai (上海鱗爪, customs volume)

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery:
every ordinary batch ends with this file's kickoff block PASTED VERBATIM INTO
THE CHAT, alongside the attached EPUB. Writing it here alone does not count.

## Message to paste into the next chat

```
Scales and Claws B10 (FINAL BATCH)

Read CLAUDE.md in full, then HANDOFF.md, then book.json. We are translating Yu
Muxia's Scales and Claws of Shanghai (上海鱗爪, 1933; 2019 Taipei reprint, customs
volume) per CLAUDE.md. Work only on claude/scales-and-claws; expect the harness to
start you on a stray branch and consolidate per rule 2 (check out the canonical
branch, reset it to origin, do the work there, delete the stray). This book's PR
history through B09 is merged, so if the designated branch carries only merged
history, restart it from origin. Deliverable out/scales-and-claws-of-shanghai.epub.

This is the LAST batch: B10 = ch156-ch167 (點香燭 through 髦兒戲; PDF 234-247, printed
folios 232-245) end to end per the CLAUDE.md pipeline, PLUS the whole-book close-out
(back matter, reconciliation sweep, COMPLETION.md, commit the final EPUB). Plan it
light on translation, heavy on close-out.

Pipeline: ./setup.sh; render 234 247 --dpi 300; OCR with the B01-B09 crop (ocr_crop.py
--left 0.03 --right 0.97 --top 0.13 --bottom 0.95 --lang chi_tra_vert --psm 5, tighter
--bottom on any page carrying a reprint photo). tesseract on this vertical-Traditional
reset is only ~85% and too error-dense to trust: EYE-READ every page at magnification
and hand-transcribe data/zh against the scans, exactly as B01-B09 did. indents.py is
UNUSABLE here; assemble on the blank-line signal and finalize paragraph structure BY
HAND against the scan, using the short-line signal at the page seams (where a text band
sits above a reprint photo there may be NO internal short-column break, so the band can
be a single paragraph, as ch063/ch088/ch100/ch114 were). pgrep -c tesseract must be 0
after OCR. Eyeball every page for reprint-added photos and run each through the figure
pipeline (crop to data/figs/ with a BARE filename; alt text with NO double quotes;
caption translating any reprint label and stating 2019-editor provenance; exclude the
printed caption line from the crop). B01-B09 had photos only in the front matter and
ch114; expect few or none here, but LOOK, and record an empty figure list as a decision.

PAGE-STRUCTURE TRAPS to verify off the scan:
- NUMBERING GAP: ch161 空頭支票 is PDF 239, ch162 假鈔票 is PDF 242 (book.json). PDF
  240-241 are unaccounted between them. Check whether ch161 spans 239-241 (as ch153
  spanned 230-231 in B09), or whether 240-241 hold a plate or blanks. Read the folio
  off the scan and record what they are, exactly as B09 resolved the 231 gap.
- Offset holds printed = pdf - 2; VERIFY at every opener. Body ends at PDF 247
  (printed 245, ch167 髦兒戲, the last essay). PDF 248-249 blank, 250 CIP, 252 back cover.
- Watch for any two-essays-share-a-page splits (none flagged, but several titles are
  short: 叫火燭, 抄把子, 假客氣). Read each unit's start/end off the scan.

THEMATIC NOTE: B10 closes the book on the counterfeiting/fakery cluster and a few
last customs. 點香燭 (temple incense-and-candle sellers), 某國浪人 ("ronin of a certain
country" = Japanese toughs; ×× self-censorship likely, render as printed + footnote),
叫火燭 (the night fire-watch crier), 樹上開花 (a con, lit. "flowers on the tree"), 抄把子
(the frisk / shakedown), 空頭支票 (rubber/bad checks), then the four counterfeit essays
假鈔票/假銀幣/假輔幣 (fake banknotes, silver dollars, small coin) and 假書畫 (fake
paintings, pairs with ch142/ch165 and the earlier 裱畫店 ch070), 假客氣 (false
politeness), 髦兒戲 (the all-girl opera troupes). Expect money/counterfeiting detail:
carry every figure, cross-ref the money policy, footnote the coin and note types.
Recurring furniture already noted, cross-ref do not re-note: money policy (大洋/小洋/
毛/角/分/文/鈿, ch001/ch014/ch148); 白相人 hoodlum (decided "hoodlum"); 野雞 pheasant;
洋盤 sucker (ch073); 掮客 broker (B06); 揩油 skim (ch098/ch152); 拆白黨 peeling-white
gang (ch114/ch134); 拆字 character-splitting (ch037/ch121/ch155); 城隍廟 (ch001);
洋涇浜 pidgin (ch018/ch078); 弄堂 (ch063); 三百六十行 the 360 trades (ch133/ch145);
福州路/四馬路 Fuzhou Road; 捕房 police station; 洋人/租界 furniture.

BEFORE translating, read the final two pages of out/ch155_reading.md and, for the
voice, the last two pages of out/ch114_reading.md (the long narrative): HANDOFF
describes the voice, but those pages ARE the voice; the FROZEN reference is still
out/ch001_reading.md. Run check_register.py --ref out/ch001_reading.md on every unit.
Consult glossary.json and authority.json BEFORE romanizing any name. Crop-verify every
name, number, price and low-confidence span, recording verified readings in
data/ocr_fixes.json. Fact-check any real person or institution against real scholarship
(Wikipedia / Baidu Baike / academic, NEVER an LLM-written site such as Grok/Grokipedia);
state the verdict in the note. Never invent bridging text; verify each unit's tail
against the scan. NOTES stay GENEROUS: annotate wherever a non-specialist Western reader
would miss anything. Recurring subjects get their note at FIRST appearance (grep
notes.json and earlier reading files first; keep the per-batch "NOT re-noted" list).

Per unit: write out/<id>_reading.md (one paragraph per source line), then
make_bilingual.py, verify_unit.py (unit ids only, it applies data/noise.txt itself; do
NOT pass --noise), check_align.py; apparatus_merge.py for notes/glossary/figures
(glossary rows may be SECTIONED: {"glossary": {"<zh>": {..., "pinyin": ...,
"section": "people|places|organizations|terms"}}} - default section is terms; every
glossary rec MUST carry a "pinyin" key or qc_entities throws KeyError; note bodies
inserted RAW into XHTML, so straight quotes or numeric char refs, &#8211; en-dash,
&#8212; em dash, <i> only, numeric char refs never named entities, &#38; for a literal
ampersand; a figure "file" is a BARE filename and its "alt" must contain NO double
quotes), check_apparatus.py; regenerate check_config.json for the units whose data/zh
exists, then check_structure.py --config + check_content.py --config + qc_entities.py
PER BILINGUAL FILE (loop over units; watch existing-key SUBSTRING collisions, e.g. B09
hit 探捕 inside 警探捕 and 自來火 inside 自來火街, both aligned to the ledger word).

THEN, because this is the last batch, do the CLAUDE.md close-out:
- Back matter: check the colophon / any errata table at the book's end (PDF 247-250);
  if present, reproduce in back_matter.json and apply each erratum to the affected text.
- Whole-book reconciliation (check 12): run scripts/check_reconcile.py; hand-read its
  drift candidates; grep-count the ~20 decided renderings; confirm notes sit at FIRST
  appearance; one spelling locale.
- Render out/term_ledger.md and out/deep_audit.md (3-5% random-sample deep audit, fixed
  seed, honest error rate). Feed this book's decided renderings back into authority.json.
- Rebuild the cumulative EPUB (now COMPLETE: title page states so, TOC cleaned of
  pending scaffolding); qa_epub.py green; epubcheck (jar at /tmp/epubcheck-5.1.0/
  epubcheck.jar). Commit the final EPUB itself: git add -f out/scales-and-claws-of-
  shanghai.epub (branches outlive containers, chat attachments do not).
- Write COMPLETION.md from the template (sampled error rate, residual uncertainties).
  Rewrite HANDOFF.md to say the book is COMPLETE and further work is a corrections pass;
  do NOT leave a next-batch kickoff (there is none). Commit and push claude/scales-and-claws.

Deliver in chat: the final EPUB attached, AND a short completion report (counts, gates,
fact-check verdicts, residual uncertainties). Do not pause for approval mid-batch.
```

If the commissioner instead sends corrections to B01-B09, transcribe them into
CORRECTIONS.md and run the corrections workflow (rebuild, qa_epub, epubcheck,
CHANGELOG entry) before B10.

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
- B08 (2026-08-13): ch111-ch129 (俞調、馬調 through 戤牌頭). 66 notes, 49 rows, 3 figs.
- B09 (2026-08-13): ch130-ch155 (兜得轉與跑得開 through 兩個半滑頭). The swindler/beggar/
  street-trade heart. 62 notes (book-wide 556-617), 17 glossary rows, 0 figures (no
  reprint photos on any page 209-233). Resolved the numbering gap: PDF 231 is ch153's
  SECOND page (儲蓄騙 spans PDF 230-231), not a blank/plate. Two shared pages confirmed
  (ch135+ch136 on PDF 214; ch140+ch141 on PDF 218). Fact-checks: 萬國儲蓄會 International
  Savings Society CORROBORATED; 三山會館 Sanshan Guild Hall CORROBORATED; 嵊縣 real
  county (kidnapping repute per tradition); 瞿紹伊 uncorroborated, noted honestly. All
  gates green; qa_epub PASS; epubcheck 5.1.0 clean (0/0/0); check_register all within
  tolerance on all 26.

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
  quotes or numeric char refs (&#8220;/&#8221;/&#8217; all fine), &#8211; en-dash,
  &#8212; em dash, <i> only (no <b>), numeric char refs never named entities,
  &#38; for a literal ampersand. When writing CJK into the batch JSON, RE-READ every
  character (near-homoglyph typos).
- FIGURE RULES: (a) a figure's "before" anchor MUST fall within the first ~80 chars
  of the target paragraph; MULTIPLE figures may share one paragraph's anchor and
  stack in list order; (b) the "file" field is a BARE filename; (c) the "alt" text
  is inserted into an XML attribute, keep it free of double quotes; (d) crop OUT the
  reprint's own printed caption line and write your own caption stating provenance.
- ANCHOR GOTCHA: the note marker sits right after the anchor string. Pick an anchor
  that is a plain word-run INSIDE the sentence, NOT one ending just before a closing
  quote or an em dash (both collide). Ending before a comma/period/paren is fine.
- QC_ENTITIES GOTCHA: qc requires every glossary hanzi in a source paragraph to have
  its ledger rendering (full en, its pinyin, or the en's first OR last word) in the
  paired English. Watch (1) SUBSTRING collisions with existing keys (B09: 探捕 inside
  警探捕 -> "plain-clothes constable"; 自來火 inside 自來火街 -> keep "self-coming fire"
  in the sentence); (2) a term rendered two ways (heading vs cant-in-text) will fail
  if you glossary-ize it, so do NOT add such terms to the glossary (B09 kept 拋頂宮 and
  買戶頭 OUT for this reason). Every glossary rec MUST carry a "pinyin" key or KeyError.
- check_config.json (tracked): {docs,sources,notes,variants}. In a fresh container
  only the CURRENT batch's data/zh exists, so REGENERATE it each batch to the units
  whose data/zh EXISTS.
- verify_unit.py takes UNIT IDS ONLY and applies data/noise.txt itself; do NOT pass
  --noise. check_numbers.py DOES take --noise and takes the BILINGUAL FILE path (not a
  unit id). check_structure/check_content take --config. qc_entities.py takes ONE
  BILINGUAL FILE; loop over units. check_align.py takes ONE unit; loop. GREP output
  for FAIL over many units.
- check_numbers quirks (running list): parses "a hundred" not "the/per hundred"; reads
  a name's or idiom's digit as a numeral; reads an abbreviated X、Y tail as a numeral
  (二、三十); reads 兩 in a 十四兩天/三十兩夜 counter as 2; 零 in 零紙/零碎/零落/有零 reads
  as 0; 萬 in a name (萬國/萬事) or 巨萬 reads as 10000; 五色/五光十色/十足 read their
  digits. Fix with a TARGETED noise (lookbehind/lookahead), never a broad one. Only
  noises SOURCE numerals; a real number (ch151 效力等於零) is carried in the English.
- data/noise.txt (longest-first, each with a comment): current tail adds (B09) 五色,
  張三, 李四, (?<=十四)兩, 二(?=、三十), 三山, 五光十色, 十足, (?<=三十)兩(?=天|夜),
  零(?=紙), 零(?=碎), 萬國. Earlier: B03 北四川路/十八、九/長三/么二/老六; B04 黃楚九/
  九畝地/億定盤路/萬民矚目/十餘萬/塵煙四起; B05 巨萬/零售/百科/十六浦/十幾萬/(?<=十一)、二;
  B06 有零/萬事/零落/丘八/朱葆三/三、四十; B07 五方雜處/四出/(?<=十五)、六/五官; B08
  禮拜三、六/癟三.
- data/ocr_fixes.json: crop-verified readings ledger.

## Renderings settled / carry-forward

- Voice (frozen at the ch001 gate): preface = formal classical-period English;
  chapters = 1930s newspaperman's miscellany, quick/worldly/amused, the author
  stepping in to editorialize (呵呵！; the sardonic "worthy of all men's admiration").
  Held B02-B09.
- Money policy (recurs book-wide): 塊/元 = "dollar"; 大洋 = the standard silver
  dollar; 小洋 = "small silver"; 毛 = "*mao*"; 角 = "*jiao*"; 分 = "*fen*"; 文 =
  "cash"; 制錢 = "standard coin/cash"; 銅圓/銅板 = "copper". As an INTEREST rate,
  分 = one per cent. Never flatten 毛/角 to "cents". 鈿 is Wu for money (二百鈿 = two
  hundred cash). B10 will need the counterfeit-coin vocabulary; hold to this policy.
- Shelf-consistent names (authority.json): 南京路 Nanjing Road, 南市 Nanshi, 捕房
  police station, 霞飛路 Avenue Joffre, 靜安寺路 Bubbling Well Road, 工部局 the
  Municipal Council, 公董局 the French Municipal Council, 蘇州河 Suzhou Creek, 跑馬廳
  the Racecourse. Author 郁慕俠 = Yu Muxia; preface author 天虛我生 = Chen Diexian.
- 白相人 = "hoodlum" (locked by the ch132 title "The Hoodlum's Missus"); render it
  "hoodlum" wherever 白相人 appears, or qc_entities fails. Literal "man-about-town"
  sense footnoted (ch072); the author re-glosses it 即流氓 at ch127.
- B09 glossary DECIDED (reuse verbatim; grep before re-noting): Terms 捉蟋蟀 catching
  crickets, 滑頭 slicker, 老弟兄 old brothers, 老門檻 old hand, 長錠 long ingots, 三光黨
  the Three-Lights Gang, 還魂煙 resurrection cigarettes, 吃講茶 judgment tea, 孵豆芽
  hatching bean sprouts, 阿拉 a-la, 春宮 spring-palace pictures, 拾荒 scavenging,
  撈錫箔灰 dredging for tinfoil ash. Orgs 萬國儲蓄會 the International Savings Society.
  Places 三山會館 the Sanshan Guild Hall, 嵊縣 Shengxian, 漢口 Hankou.
- Earlier-batch glossary (reuse verbatim, a partial list): 城隍廟 City God Temple,
  野雞 pheasant, 揩油 skim, 拆白黨 peeling-white gang, 拆字 character-splitting, 探捕
  plain-clothes constable, 包探 detective, 老虎灶 tiger stove, 弄堂 lane, 洋盤 sucker,
  花會 huahui, 自來火 self-coming fire (gas), 么二/長三 brothel grades; numbered
  "Avenues" 大馬路=Nanjing, 二馬路=Jiujiang, 三馬路=Hankou, 四馬路=Fuzhou(福州路),
  五馬路=Guangdong, 六馬路=Beihai; 申報 Shenbao, 新聞報 Xinwenbao. Full ledger in
  glossary.json (319 rows, sectioned people/places/organizations/terms).
- No continuing cast (essay collection); recurring historical names handled by the
  glossary, not voice sheets.

## Where the book stands

- 156 of 168 units done (preface + 155 essays). 12 essays remain (B10 = ch156-ch167,
  the FINAL batch). No plot to track; the register decisions in B01 govern everything.
  Internal dating runs ~1856 to the mid-1930s.

## Next batch scope

- B10 = ch156-ch167, PDF 234-247, printed 232-245. Incense-and-candle sellers,
  foreign toughs, the fire-watch crier, cons and the frisk, rubber checks, the four
  counterfeit-money essays, fake paintings, false politeness, the all-girl troupes.
  Offset printed = pdf - 2. THIS IS THE LAST BATCH: after the units, do the close-out
  (back matter, reconciliation sweep, term_ledger, deep_audit, COMPLETION.md, commit
  the final EPUB, rewrite HANDOFF to COMPLETE). See the kickoff above.

## Open traps and environment state

- NUMBERING GAP B10: ch161 空頭支票 is PDF 239, ch162 假鈔票 is PDF 242; PDF 240-241 are
  unaccounted. Check whether ch161 spans 239-241 (as ch153 spanned 230-231 in B09) or
  240-241 hold a plate/blanks. Read the folio off the scan and record it.
- This is the 2019 RESET, not the 1933 original: no collation source. Where the reprint
  is suspect, note it; do not guess the 1933 reading. Reprint misprints seen so far:
  ch052 味蒓園 (TOC), ch053 經營三 for 經潤三, ch109 呆戀, ch116 年紅燈 title, ch122 橋塊
  for 橋堍. Render as printed, translate to the attested/plain-sense form, footnote.
- Source SELF-CENSORSHIP: the reprint blanks words as ×× (clinics, a steamship line,
  poetry societies, a film company in ch114). ch157 某國浪人 ("ronin of a certain
  country") likely carries ×× or the euphemism 某國 for Japan; render as printed,
  footnote. NOTE: in ch110 the ×× were the AUTHOR's own placeholders, not censorship.
- Vertical RTL OCR column-order errors are silent; verify assemble output by eye. A
  text band ABOVE a photo may have no internal short-column break (one paragraph). A
  photo-only page means the unit's text finished on the previous page; do not hunt for
  missing paragraphs.
- Magnified crops can clip a character's top strokes; when a digit or name is load-
  bearing, crop generously and re-zoom at 4-6x. Numerals in coin/note designations
  (B10's counterfeit essays) are load-bearing; always crop-verify.
- Blank/filler: pdf 4, 14, 248, 249, 251; CIP 250; back cover 252. Offset printed =
  pdf - 2 constant, but re-read the folio at every opener.
- 導讀 (pdf 5-11) stays untranslated (copyright); photos ARE included.
- Pagemap: only ch000/ch001 carry data/pagemap (B01); essays ship without followable
  page-list entries (consistent B02-B09). Notes cite printed folios.
- tests/run_tests.py shows one benign FAIL ("hook stands down on template stub") —
  HANDOFF carries a real kickoff, so the Stop hook correctly enters its enforcing path.
  Working as designed.
