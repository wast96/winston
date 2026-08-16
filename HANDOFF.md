# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-9 are COMPLETE (ch00-ch16). Next is
B10 = ch17 + ch18.

## Message to paste into the next chat

```
Zhou Enlai B10

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 10 =
ch17 (电讯科长"曾培鸿"——李强 / Communications Chief "Zeng Peihong" — Li Qiang,
PDF 333-363, printed 289-319; five sections ch17s01-05: 党的电讯事业创始人李强 /
为党造出第一部收发报机 / 到香港建立电台 / 培训党的第一代报务员 /
"划时代的通信革命") AND ch18 (永不消逝的红色电波 / The Red Airwaves That Never
Die, PDF 364-388, printed 320-344; four sections ch18s01-04: 留日电机专家蔡叔厚 /
党的第一个报务员张沈川 / 留苏专家毛齐华 / "木匠"涂作潮), end to end per the
CLAUDE.md pipeline. Work on branch claude/zhou-enlai; expect a stray per-task
branch and consolidate onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai,
reset --hard to origin, do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch16 in out/ch16_reading.md
(the summary of the turn from terror to political struggle, crediting Chen Geng,
Li Qiang, and Liu Ding) so the voice carries over. ch17/ch18 open a NEW arc: the
Party's clandestine RADIO / communications work — 李强 Li Qiang (alias 曾培鸿
Zeng Peihong, already in the glossary) builds the first transmitter, sets up the
Hong Kong station, trains the first operators; ch18 profiles the radio men
(蔡叔厚, 张沈川, 毛齐华, 涂作潮). This is the book's most TECHNICAL register
(radio engineering, callsigns, frequencies) laid over portrait-biography — apply
STYLE.md's "exposition and political framing" rules hardest, keep the technical
nouns precise, break run-ons into short confident statements. ch01 is the FROZEN
reference; run check_register.py --ref out/ch01_reading.md on every unit.

Pipeline notes specific to THIS book (all proven in B01-B09, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch17 opens PDF 333 = printed 289; ch18 opens PDF 364 = printed 320.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. ocr_dual.py only if names resist crop-verify.
- ASSEMBLY IS THE HARD PART and mutates per batch. USE THE B09 MODEL
  (scripts/recovery/b09_*.py are the newest, most complete; they follow b08):
  (1) b0X_strip_furniture.py: normalize garbled section headings to the EXACT
  book.json titles (pull by id, per-target guard len(good)+4); RESTORE stray
  footnote-marker chars (① OCR'd as 出/中/G/./0 etc.) AND every OCR-mangled
  SENTENCE-END that would weld two paragraphs or defeat the surgery boundary-snap.
  THE B09 LESSON: the surgery boundary-snap needs a BREAK char (。！？…：) right
  before a paragraph start; when OCR renders a ！/。 as a non-break glyph (！->
  上/性/伍/习; 。-> 、 or ascii '.'; 《-> 4; 口 -> 11; a digit doubled 1949->19495)
  the split lands in the wrong place. Grep the ASSEMBLED zh for such glyphs at
  paragraph seams and RESTORE them in the strip (verify exact bytes on the scan;
  the RESTORE quote char is ascii " 0x22 in this OCR, curly “ ” are 201C/201D;
  a blank-line seam may be \n\n so match it). EMPTY any full-page image page (it
  sits mid-paragraph; the spanning paragraph rejoins across the gap).
  (2) Add data/structure.json rows for the chapters + all sections BEFORE assemble
  (pull exact title bytes from book.json; a fancy-quote title like ch16s02 must be
  byte-exact).
  (3) git checkout -- data/indent/ if you rm -rf'd it (it is TRACKED); indents.py
  FIRST LAST; assemble.py <id> FIRST LAST --offset 44 (BOTH units before surgery —
  surgery is NOT idempotent).
  (4) b0X_surgery.py --apply. markers[i] starts piece i+1; a blob of N paragraphs
  needs N-1 markers. markers are RAW-OCR substrings (apply_fixes runs AFTER). DRY-
  RUN first (verifies each marker occurs exactly once, in order). Build the marker
  list by EYEBALLING every content page. DIALOGUE paragraphs that OPEN on a quote:
  put the marker a few chars INTO the quote and let the boundary-snap prepend the
  opening “ (verified in ch16); a paragraph that opens on a NAME after a mangled
  ！ needs the ！ restored (step 1) or a marker AT the paragraph start. LETTERS:
  split salutation | body | closing | signature (the closing "!" makes the snap
  pull the signature forward, so the signature needs its OWN marker). BLOCK QUOTES
  (碑文, 辞海, memoir, Snow/李一氓/陈养山 quotes): each indented sub-paragraph is
  its own paragraph; an attribution intro ending in : is its own paragraph. A 七律
  is ONE {p} line, couplets joined by " / ". Verify each ZH paragraph ENDS in
  sentence-final punct (letter signatures / standalone dialogue exclamations are
  the only OK exceptions) and EN paragraph count == ZH count (per SECTION —
  check_structure --pairs, and align the bilingual to catch a split/merged pair
  that leaves the count right but the CONTENT shifted, which happened twice in B09).
  (5) apply_fixes.py <id> AFTER surgery (NOT idempotent — clean-regen before every
  apply_fixes; keep a backup of the raw data/txt for the batch pages before the
  FIRST strip).
  (6) b0X_pagemap.py regenerates data/pagemap/<unit>.json (edit the two build()
  calls to the new unit ids/ranges).
- Crop-verify every name/number/alias/date/CALLSIGN BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. check_numbers catches phantom numerals
  from glyph garbles ($=5, 《=4, 口=11, S=5, doubled digits) and dropped digits; fix
  real garbles in the ZH, carry real values in the English (use figures for 100+
  per STYLE), noise ONLY genuine non-quantities (place/idiom/name numerals: add to
  data/noise.txt, longest-first). radio频率/callsigns are load-bearing numbers.
- Checks: verify_unit reads unit ids (parity + check_numbers with data/noise.txt +
  anchors); qc_entities reads out/<id>_bilingual.md (glossary rows need BOTH "en"
  AND "pinyin" or it KeyErrors; watch for FALSE-POSITIVE substring hits like a name
  X三 inside 曾三去 — document, don't fabricate); check_align reads a unit id;
  check_content --config data/check_config.json (ADD ch17, ch18 to docs AND
  sources; it wants each glossary EN form present in the paired paragraph, and it
  flags a name pronoun'd in a paragraph the source names — fix by NAMING, which
  STYLE prefers when ambiguous). check_structure --pairs SRC TGT for one unit.
  check_register --ref out/ch01_reading.md.
- Glossary: add rows DIRECTLY nested into people/organizations/places/works/terms
  (NOT via apparatus_merge, which drops them at top level where qc_entities can't
  reach); give every row "en" + "pinyin" + "status". Decide the PROSE rendering as
  the glossary `en`, keep the formal expansion in the NOTE. REUSE decided
  renderings: 李强 Li Qiang (曾培鸿 Zeng Peihong), 周恩来, 陈赓, 顾顺章, 淞沪警备司令部
  all recur. SHELF DRIFT to hold the glossary line on: 晋绥 Shanxi-Suiyuan (not
  Jin-Sui), 军统 Juntong (not Military Statistics Bureau), 同盟会 Tongmenghui.
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/Baidu/academic; NEVER Grokipedia; block
  grokipedia.com). Author footnotes (source citations, content notes) reproduced
  as translator notes tagged "Author's note." at the ① anchor. Note at FIRST
  appearance book-wide (grep notes.json and earlier reading files first). Note
  anchors must be verbatim ASCII substrings of the reading .md (straight quotes,
  match the exact quote style — single vs double — that you actually wrote; note
  BODIES use numeric char refs only, e.g. &#8212; &#8211; &#160; &#8220; &#8221;).
  Figure `alt` must NOT contain a double quote; figure `file` is a BARE basename in
  data/figs/. Merge apparatus via apparatus_merge.py (a plain JSON file, Write tool
  not heredoc); then check_apparatus.py must be clean.
- Cite the book's PRINTED FOLIO in notes, never the PDF page.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02 + ch03 Chen Geng)** through **B07 (ch11 + ch12):** complete.
- **B08 (ch13 Rescuing Ren Bishi + ch14 Opening a New Chapter Part 1):** complete.
- **B09 (ch15 Opening a New Chapter Part 2 + ch16 Part 3):** complete. ch15 = 75
  body paras, 3 sections, 19 notes, 1 figure (Mao's reply-letter facsimile): Liu
  Shaobai's whole biography (tribute scholar to secret Party member, the Mao and
  Zhou letters), then the pastors (Dong Jianwu / "Pastor Wang" of Snow's account,
  Pu Huaren) and lawyers (Chen Zhigao and the Wu Hao Notice affair), then the
  push into the press (Chen Yangshan, the news agencies). ch16 = 42 body paras,
  3 sections, 8 notes, 1 figure (Longhua garrison photo): penetrating the enemy's
  own organs — the Songhu Garrison Command and its Longhua execution ground, Song
  Zaisheng as "Political Investigator No. 4" (the magic-wine trap dialogue), the
  British/French concession police. All checks green (one documented 曾三 false
  positive). Details in PROGRESS.md.
- **EPUB:** out/zhou-enlai.epub = 17 of 28 chapters (ch00-ch16), 233 notes, 266
  pagebreaks; qa_epub PASS, epubcheck 0/0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch16; replay with
  apply_fixes.py on any fresh regen. B09 added ch15 + ch16.
- scripts/recovery/ (tracked): b02_* through **b09_*** strip/surgery/pagemap
  scripts + README. The b09_* set is the CURRENT model (follows b08; adds
  image-page emptying, letter salutation/body/closing/signature splitting, the
  dialogue-quote boundary-snap technique, and the mangled-sentence-end RESTORE for
  seams that defeat the surgery snap). Do not delete.
- ocr_crop.py patches, check_content.py '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B09 added 三一八, 五原, 三教九流,
  十足, 千里香, 三友实业社, 百里, 50年代.
- data/check_config.json: docs+sources for ch00-ch16; ADD ch17, ch18 next batch.
- data/pagemap/ch15.json, ch16.json: regenerated post-surgery (b09_pagemap.py).
- data/figs/ch15_mao_letter.png, ch16_longhua.png: cropped figure images (tracked).
- Assembly: indents.py IS used (data/indent is TRACKED — git checkout it if rm'd);
  the fix is RE-SEGMENTATION (b09_surgery.py).
- KNOWN HAZARD: apply_fixes.py is not idempotent. Always clean-regen before it.
- KNOWN HAZARD: qc_entities.py KeyErrors if a glossary row lacks "pinyin" — every
  row you add (people AND orgs/places/works) needs "en" + "pinyin".
- KNOWN HAZARD: surgery boundary-snap needs a BREAK char at a paragraph seam;
  OCR-mangled ！/。/《/口/doubled-digit at a seam must be RESTORE'd in the strip.

## Renderings settled (glossary.json is the ledger)

- Held terms: 中央特科 Central Special Section, 红队 Red Squad, 淞沪警备司令部 Songhu
  Garrison Command, 巡捕房 concession police, 租界 the Concessions, 白色恐怖 White
  Terror, 军统 Juntong, 同盟会 Tongmenghui, 晋绥 Shanxi-Suiyuan (hold the glossary
  line; earlier chapters drift — reconcile at book's end).
- B09 people (glossary): 董健吾 Dong Jianwu, 浦化人 Pu Huaren, 宋再生 Song Zaisheng
  (宋启荣 Song Qirong / 宋启华 Song Qihua), 熊式辉 Xiong Shihui, 钱大钧 Qian Dajun,
  蒋方震 Jiang Fangzhen (蒋百里 Jiang Baili), 陈志皋 Chen Zhigao, 黄定慧 Huang
  Dinghui (黄慕兰 Huang Mulan), 傅作义 Fu Zuoyi, 王若飞 Wang Ruofei, 潘汉年 Pan
  Hannian, 范广珍 Fan Guangzhen, 刘亚雄 Liu Yaxiong, 蔡麻子 Pockmarked Cai, 巴和
  Baihe, plus the Longhua martyr roster. Works: 西行漫记 Red Star Over China. See
  PROGRESS.md B09 for the full list.
- **刘鼎 Liu Ding** (NOT "刘易 Liu Yi" — B08 handoff was imprecise): the 情报科
  副科长, crop-verified.
- Killing verbs (STYLE ledger): 镇压/制裁 of a traitor = eliminate/kill; 处决 =
  execute; 除掉 = kill; 镇压 of a movement = crush.
- Feed decided renderings into authority.json at book's end (out/term_ledger.md).

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. His exposition
  and potted biography (Liu Shaobai's life, the martyr roster, the garrison
  commanders' service records) is the highest-risk zone for stiltedness — break
  it into short confident statements, no dash-glosses. In B09 the em-dash rate
  came in at 0.4-0.8/1k (vs the ch01 reference's 6.0); hold that.
- **Zhou Enlai:** measured, analytic, unshowy; his letter to Liu Shaobai (ch15)
  is warm and terse. **Chen Geng:** quick, cool, the operational hand — in ch16
  he plays the "Kuomintang chief of staff" in the magic-wine sting, dry and
  commanding. **Li Qiang** (the B10 lead): the technical man, the Party's radio
  pioneer, alias 曾培鸿; write his engineering work precise and unfussy.
- **Reproduced material** (碑文 inscriptions, Mao's and Zhou's LETTERS, memoir
  quotes, the Snow/西行漫记 passage, 冯玉祥's 我的生活, 陈养山's and 李一氓's memoir
  quotes): rendered as PLAIN paragraphs, no outer quotes on block quotes; an
  attribution intro ending in a colon is its OWN paragraph. A LETTER = salutation /
  body / closing / signature, each its own paragraph. INLINE quotes (intro + quote
  in one source paragraph) keep their quote marks inline. Author source-citations
  and content notes reproduced as "Author's note." at the ① anchor.
- **Dialogue** (heavy in ch16, and expected in ch17/ch18 training scenes):
  natural and contracted, differentiated by speaker; a gangster/informer, a Party
  officer, and a technician do not talk alike. The magic-wine sting (ch16s02) is
  the model for a multi-turn exchange.

## Where the story stands

The Special Section's arms are drawn (intelligence ch04-08; Action/Red Squad
ch09-12; the rescue and political turn ch13-14). B09 completed the political-
penetration arc: ch15 recruited eminent outsiders (Liu Shaobai; the pastors Dong
Jianwu and Pu Huaren; the lawyer Chen Zhigao, who fronted the Wu Hao counter-
notice; the press networks under Chen Yangshan) and ch16 turned the tables on the
enemy's own organs (the Songhu Garrison Command, the concession police), closing
on the verdict that Zhou Enlai's line — away from pure terror, toward political
struggle — had succeeded. B10 (ch17-18) opens the NEW arc of the Party's secret
RADIO and communications work under Li Qiang.

## Exact next-batch scope

- **B10** = ch17 (PDF 333-363, printed 289-319, ch17s01-05) + ch18 (PDF 364-388,
  printed 320-344, ch18s01-04). Then B11 = ch19 (opens PDF 389) + ch20.
  (out/SURVEY.md's batch numbering runs one behind, since B05 combined ch07+ch08.)

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY: OCR-mangled sentence-ends at paragraph seams defeat the surgery
  boundary-snap; RESTORE them in the strip. EMPTY full-page image pages. Verify
  per-SECTION EN==ZH AND align the bilingual (a split/merged pair can keep the
  count right while shifting content — caught twice in B09).
- Surgery is NOT idempotent (re-assemble both units first); DRY-RUN before --apply.
  apply_fixes is NOT idempotent (clean-regen; keep a raw data/txt backup).
- data/indent is TRACKED — git checkout it if you rm -rf'd it before re-running.
- qc_entities needs "pinyin" on every glossary row; check_content wants the
  glossary EN form present in the paired paragraph (fix a flag by NAMING the
  figure); both can throw a substring FALSE POSITIVE (a name X三 inside 曾三去) —
  document, never fabricate.
- Figure `alt` must not contain a double quote; `file` is a bare basename in
  data/figs/. Note anchors verbatim ASCII substrings (match your exact quote
  style); note bodies numeric char refs only.
- ocr_dual.py is slow; run in the background. OMP_THREAD_LIMIT=1 for tesseract;
  kill the process GROUP; pgrep -c tesseract must read 0 after a run.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
