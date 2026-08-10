# PROGRESS — The Gangs of Old Shanghai (旧上海的帮会)

Running per-batch log. Written as work happens, not at the end.

## Setup (session 1)

- **Source.** `source.pdf` = the uploaded scan, 391 pages, image-only (no text
  layer; producer FreePic2Pdf/Pdg2Pic). Simplified Chinese, horizontal.
  Cover carries a library seal and a signature (朱学范, the title inscription);
  title page carries accession no. 124054 and a Shandong Normal University
  library stamp. Copyright page (pdf 3): 上海人民出版社, printed 上海新华印刷厂,
  出版日期 1986年8月, 定价 2.90 元, 上海市报刊登记证第424号.
- **Attribution decided.** This is an ANTHOLOGY (26 memoir/study articles +
  editorial note + preface + 2 appendices), compiled by 中国人民政治协商会议上海市
  委员会文史资料工作委员会. Cataloged to that committee as corporate author/editor
  (`author_en`). Zhu Xuefan (vice-chairman, NPC Standing Committee) contributed
  the opening article and brushed the cover title; Wei Jianyou (history prof.,
  Shanghai Normal) wrote the preface. Individual contributors are named per
  article and carried as in-text bylines.
- **Page offset.** printed = pdf − 9, CONSTANT across the whole book (no
  accumulating plates). Verified at anchors: pdf 6=序言 folio 1; pdf 10=body
  folio 1; pdf 38=folio 29; pdf 204=folio 195; pdf 351=folio 342; pdf 376=folio
  367; pdf 378=folio 369; pdf 391=folio 382 (last page, member roll:
  "共三百二十四人"). Re-verify each opener's folio at its batch anyway.
- **Environment.** `setup.sh` green: tesseract 5 + chi-sim/chi-sim-vert/
  chi-tra/chi-tra-vert. PaddleOCR NOT installed (expected) → dual-engine
  substitute is `scripts/ocr_dual.py` (psm 6 / psm 4 / inverted). epubcheck
  5.1.0 available (java present). Checker regression tests: green.
  `OMP_THREAD_LIMIT=1` exported.
- **Front matter.** 编辑说明 pdf 4–5 (own folios 1–2, dated 1986年4月); 序言 by
  魏建猷 pdf 6–7 (own folios 1–…); 目录 pdf 8–9. Body pdf 10 onward.
- **Page furniture (to configure at B01).** Body text box + running foot/folio
  crop NOT yet measured; do it as the first engineering task of B01 and record
  the crop box here. Folio sits centered at the foot as `• N •`.

## Step 0 gates

- **0a metadata:** done in `book.json` (title, author/editor, translator
  "Winston", series "Winston Translations" #10, subjects, description,
  translator_note, source_ref, pdf_end/printed_end, modified fixed).
- **0b survey:** `out/SURVEY.md` generated; 28 units in 9 parts; skeleton EPUB
  built (`out/gangs-of-old-shanghai.epub`), `qa_epub` PASS, epubcheck 0/0.
  Refined 10-batch plan written to `book.json`. **Awaiting commissioner
  approval before Batch 1.**
- **0c voice gate:** pending (after B01).

## Glossary seeded (from authority.json)

Principal cast + core terms only, to make the skeleton's Principal Characters
page representative. Renderings taken from the cross-book ledger where present:
Du Yuesheng, Huang Jinrong, Zhang Xiaolin, Dai Li (attested); Gu Zhuxuan, Zhang
Renkui (provisional); Green Gang (青帮), the Hongmen (洪门, attested), Heng
Society (恒社), Ren Society (仁社), the gangs (帮会).

- **军统 is a live cross-shelf RECONCILE** (COLLECTION.md): three prior renderings
  (Military Statistics Bureau / the Juntong / Juntong). Seeded here as "the
  Juntong" but the binding decision + authority.json reconciliation is deferred
  to B08 (ch21, 杜月笙与戴笠及军统的关系), the article that leans on it.

## Batches

- **B01 DONE (ch01–ch04, printed 1–28)** — pending the voice-gate approval.
  - Units: ch01 Editorial Note (5 paras), ch02 Preface / Wei Jianyou (8), ch03
    Zhu Xuefan, "A Few Notes on the Shanghai Workers' Movement and the Gangs"
    (42, three parts + five subsections), ch04 Wu Chengfang, "Fragmentary
    Materials..." (18).
  - Notes: 43 (ch01 2, ch02 6, ch03 19, ch04 16). Continuous book-wide numbering
    by the builder. Glossary: 33 rows (people 24, orgs 8, terms 1).
  - Checks all green: parity 5/8/42/18 = OK; check_numbers 0 unresolved (see the
    noise + digit notes below); check_apparatus 0/0; qc_entities 0 misses;
    check_align OK (ch02's short "April 1986" dateline is the one expected
    short-pair flag); check_content OK; qa_epub PASS (43 ref/body/backlink);
    epubcheck 0/0.
  - **Register:** ch03/ch04 are expository memoir with almost no dialogue
    (0.0 contractions/1k), so the dialogue-contraction metric is not meaningful
    yet. The dialogue-register REFERENCE should be set from the first
    dialogue-heavy chapter (a Huang Jinrong / Du Yuesheng memoir, B04+), not
    from B01. Noted so drift-checking measures against a real dialogue baseline.
  - **Paragraph structure:** built by hand from the OCR + scan, because this
    scan defeats the geometric indent detector (see Setup). zh source files in
    data/zh are reconstructed clean (numbers verified) and segmented to match
    the English 1:1.
  - **Number-check accounting:** event/movement date-names (八一三 一二八 一二九
    四一二 五卅 七七), the pricing idiom 八折, decade labels, and numeral-bearing
    proper names (李立三 万邦和 王懂百 九江路 万里浪 王震百) are in data/noise.txt.
    Genuine large quantities are written as digits in the English so the check
    can verify them.
  - **Tail-verified** (rule 4 corollary): ch04's true last line is "…很有帮助的。"
    — strip_folio had eaten the one-character line "的。" as if it were a folio;
    restored. Watch short one-glyph closing lines each batch.

## Voice-gate revision (round 1)

Commissioner read to printed p.12 and rejected the prose as clunky and stilted:
faux-period formality, inversions (&#8220;needed all the more someone&#8230;&#8221;), calque
idioms (&#8220;lay hands on that pension,&#8221; &#8220;have a voice put in for them&#8221;), and
inconsistent number styling (&#8220;sixty-eight&#8221; beside &#8220;2,400&#8221;). RECALIBRATED the
whole batch to natural contemporary English: removed inversions and archaisms,
broke run-ons, fixed the flagged phrasings, dropped the confusing &#8220;twenty-fourth
part,&#8221; and adopted ONE number rule &#8212; digits for specific quantities (counts,
ages, years of service, sums, percentages), words only for rounded/rhetorical
ones. ch03 and ch04 rewritten in full; ch02 preface lightly de-flowered (its
scholarly register kept); ch01 already clean. Note anchors re-pointed to the
new prose (7 anchors updated); all checks re-run green. This natural register
is the standard for the rest of the book.

## Tooling patches this project (do NOT revert)

- `ocr_crop.py`: added `folio_present()` (was referenced by indents.py but never
  defined — crashed every book). Geometric folio test; kept in lock-step with
  `indents.line_starts`.
- `indents.py`: documented that geometric indent detection is bypassed on this
  scan (speckle + tight lines break band↔OCR-line alignment); assembly uses the
  blank/short-line fallback.
- `check_numbers.py`: added 〇 (ideographic zero, U+3007) to CN_DIGIT and the
  extraction class, so years like 一九四〇 read as 1940; guarded the built-in
  `一一` ("one by one") rule with a lookahead so it no longer eats the head of a
  compound like 一一七 (117 → orphan 7).
- `apparatus_merge.py`: made the glossary merge SECTION-aware (rows carry an
  optional `section`, default `terms`; dup-check spans all sections). It had
  merged rows flat at the top level, which broke render_glossary and duplicated
  戴笠.
- `check_content.py`: skip `_`-prefixed / non-dict glossary keys in name_map
  (it crashed on the `_about` string).
- **Measured OCR crop** (this book): `--left 0.06 --right 0.91 --top 0.09
  --bottom 0.89 --lang chi_sim --psm 6`. Folio at the foot centre (`• N •`),
  cropped out. No running head.

## B02 DONE (ch05–ch06, printed 29–67)

- **Units:** ch05 Li Shiyu, "A Brief Study of the Early Organization of the
  Green Gang" (79 paras, 3 sections + conclusion; a scholarly paper);
  ch06 Jiang Hao, "The Origins and Evolution of the Green Gang" (103 paras,
  6 sections; memoir-study with a long who's-who of the Shanghai gang).
- **Notes:** 77 this batch (ch05 65, ch06 12); running total 120. ch05 carries
  the AUTHOR'S OWN citation footnotes reproduced in full and marked "Author's
  note." (57 of them), plus one "Editors' note." and 7 translator notes; ch06
  is translator notes only (no source footnotes in it).
- **Glossary:** +21 rows (people 12, orgs 7, terms 3 → after the 罗祖 removal,
  net 21 added this batch; 54 total). Removed the standalone 罗祖 anchor
  (it is a substring of 罗祖教 and appears in tablet-list short form; Patriarch
  Luo stays consistent in prose and is covered by its note). 军统 rendered
  "the Juntong" (still shelf-UNSETTLED; binding decision deferred to B08).
- **Checks all green:** parity 79/79 and 103/103; check_numbers 0 unresolved
  (see noise notes below); check_apparatus 0/0; qc_entities 0 misses;
  check_align (ch05 the one expected short "15 August 1984" dateline flag;
  ch06 OK); check_content 0 displaced; qa_epub PASS (120 ref/body/backlink);
  epubcheck 0/0; check_register within tolerance of the ch03 reference
  (both units near-zero dialogue, so the contraction metric is not meaningful).
- **Number-check accounting (data/noise.txt additions):** official titles and
  name/place/idiom numerals were added as noise, each with a comment —
  千总 (battalion officer), 王七/何二/步章五/庄铸九/金九龄/孙百群 (names),
  四川/百姓/十六铺/五台山/五行山/两狼山/百龄 (places/lodges/restaurant),
  零星/千百成群/千百万/十万八千里/万历/万象/万恶/千秋/两面派/三青团 (idioms
  and proper terms), 四百多万 (the "over 4 million" compound the 多 splits),
  and a general tael rule `(?<=[十百千万萬])两` so e.g. 五六百两 reads 600,
  not 602 (两 as the measure "tael", not the digit 2). Genuine quantities are
  carried as digits/spelled ordinals in the English so the check verifies them.
- **Classical block quotes:** ch05 quotes some three dozen Qing memorials and
  gang texts; each is rendered inline (not set off), keeping the source's own
  paragraph structure, and each carries the author's citation as an
  author-note. Three gang doggerel verses on p.48 use the {p} verse marker.
- **Tail-verified** (rule 4 corollary): ch05's true last lines ("…重要工具。"
  + the 一九八四年八月十五日 dateline) and ch06's last paragraph ("…直到解放后
  才肃清。") read against the p50 and p67 scans; faithful, no invented tail.
- **Source discrepancies noted (rendered as printed):** the gang's legendary
  genealogy in ch06 (前三祖/后三祖) is unhistorical and is footnoted as such,
  cross-referencing Li Shiyu's archival account in ch05; the two studies also
  give the 24 generation-characters in slightly different characters (元明兴理
  vs 圆明行理; 临持康泰 vs 临持广泰), footnoted. 樊瑾成 (p60) / 樊瑾丞 (p64)
  are printed with different third characters but both romanize "Fan Jincheng",
  so no reader-visible discrepancy. 曹志功 (p60 Ren Society roll) vs 曹立功
  (p62 own entry) left as printed.
- **Yi Society homophony:** 毅社 (B01, Zhu Xuefan) / 逸社 (Xu Yimin) / 怡社
  (Sun Yixiang) all romanize "the Yi Society"; distinct bodies, footnoted once
  at ch06. Flag for the B10 whole-book reconciliation (check_reconcile will
  surface "the Yi Society" against three hanzi — legitimate).
- **NOT re-noted (already placed in B01):** Du Yuesheng, Huang Jinrong, Zhang
  Xiaolin, Dai Li, Chiang Kai-shek, the Green Gang, the Hongmen, the April 12
  coup, the August Thirteenth resistance, the yellow unions, No.76's parent
  regime — the Green Gang/Hongmen themselves were introduced in B01. New notes
  here are for the gang's own history and its early-modern cast.
- **Tooling:** qc_entities.py made tolerant of a glossary row without a
  `pinyin` field (it crashed the whole check before); org/term rows given
  pinyin for consistency. No other script changes.

## B03 DONE (ch07–ch08, printed 68–107)

- **Scope.** ch07 "洪门历史初探" (A Preliminary Inquiry into the History of the
  Hongmen), by Jiang Hao (姜豪, same author as ch06); ch08 "我接触过的上海帮会
  人物" (Shanghai Gang Figures I Have Known), by **Xue Gengshen (薛耕莘**, byline
  printed with the variant graph 畊 for 耕), the French Concession police's most
  senior Chinese detective. PDF 77–116, printed 68–107.
- **Author footnotes:** NEITHER ch07 nor ch08 carries the author's own numbered
  page-foot notes (checked the page feet by eye; ch05 had them, ch06–ch08 do
  not). The `*`/`%`/`?` glyphs the OCR scattered are mis-read closing quotation
  marks, not note markers. So no "Author's note." entries this batch.
- **Checks, all green:** verify_unit parity 54/54 (ch07), 76/76 (ch08);
  check_numbers 0 unresolved both (noise extended, below); check_align OK
  (median 5.50 / 5.11 en/han); check_content OK (docs/sources cfg in
  work/content_cfg.json — regenerated for ch07/ch08); qc_entities 0 misses both
  (and ch01–ch06 re-checked 0 against the enlarged glossary); check_register vs
  the frozen ch03 within tolerance (both expository/memoir with little dialogue,
  flagged noisy not failed); check_apparatus 0/0; check_structure ALL PASS
  (anchors 160/0 unresolved, headings OK); qa_epub PASS; **epubcheck 0/0**.
- **Apparatus:** 40 notes (ch07 15, ch08 25); +41 glossary rows (95 total).
  Running note total 160.
- **Figures:** NONE. Both chapters are text-only (page images eyeballed; the two
  mountain-lodge grids in ch07 are tabular text, rendered as prose lists, not
  images). Recorded as a deliberate empty figure decision.
- **Crop-verified against the scan (dual-OCR mangles both configs shared or that
  I named):** byline 薛畊莘; the French romanizations the source itself glosses —
  夏才立/夏才拉 (Chazel), 费沃利上尉 (Capitaine Fiori), 谭斯脱 (Destes), 《真理报》
  (La Vérité), 葛格霖 (Koeclin, consul-general), 法伯尔中校 (L. Fabrer), 饶伯泽
  (Jobez), 马莫雅 (Marmorat), 范浪打 (Yolenti); both ch07 mountain-lodge tables
  (44 + post-1911 rows) — OCR mangled most founder names, corrected by eye;
  key body-text catches — 魏廷荣 (OCR 魏延荣/犁廷荣), 高鑫宝 (高读宝), 虞洽卿
  (广/处洽卿), 汪禹丞 = Wang Yucheng (汪珊丕/汪台丞), 徐逸民 (徐揭民), 留美西医
  (not 留德), 肇和兵舰起义 (侯和), 李咸池 (李威池), 山东泰安 (秦安), 三合会三千人
  (三和于人), 叔嫂相敬 (rule 7), 筑青山 (锁青山), 先烈祠 (忠烈祠), and the author's
  father 薛仲江 (OCR garbled to 龚/巷仲江 — same surname as the author). Tails of
  both chapters read against the p95/p116 scans (rule 4 corollary): ch07 ends
  "上述决议案也没有实现。" + the closing note; ch08 ends "常玉清被处决。" No
  invented bridging text.
- **noise.txt extended (each entry commented, longest-literal-first by hand):**
  ch07 — 三汊河, 九连山, 万云, 万寿, 万福, 万宝, 三星, 五方, 五圣, 十龙, 九华,
  九龙 (names/lodges/idioms carrying a numeral glyph the romanization drops).
  ch08 — a CJK list-enumerator rule `（[一二…十]）` (the source's （一）（二）…
  sub-heads, like the built-in "1." rule), 顾四, 饶老四, 九亩地, 潘三省, 三友,
  百货, 两帮, 二季, 瘪三, 朱葆三, 阿五, 零售. Genuine quantities carried as digits
  in the English (register: digits for specific quantities), incl. the large
  money amounts (100,000 yuan; 8,000–10,000 francs; 10,000–12,000 yuan).
- **Source claims footnoted honestly (corroborated / uncorroborated):** the
  Hongmen founding legend (Shaolin, Five Ancestors, the Red Flower Pavilion) is
  footnoted as myth, not history — the Tiandihui traces to mid-18th-c Fujian;
  Sun Yat-sen's Hongmen initiation is corroborated; the Tongmenghui passage
  conflates the 1905 Tokyo founding with the 1911 Hankou central bureau (noted).
  ch08's Song-family drowning anecdote and the 支那十勇士 episode rest on the
  author's word alone and are footnoted as uncorroborated; Lu Bohong's 1937
  assassination is corroborated but the attribution to Chen Mo / Chang Yuqing is
  the author's. The source's own inconsistency 夏才立/夏才拉 (Chazel) kept as
  printed; the printed Latin glosses (L. Fabrer, La Vérité) reproduced as the
  author gave them.
- **NOT re-noted (already placed):** the April 12 coup (ch02), Kawashima
  Yoshiko (ch06), Lu Liankui (ch03), the "ten years of turmoil" (ch02), the
  Green/Hong Gang names (ch01), the Small Sword Society's 1853 rising (ch02,
  cross-referenced), the generation-characters / 通字辈 (ch05), the Juntong
  (ch06), Xiang Songpo (ch03), Water Margin / Liangshan (ch06; Shi Qian gets a
  fresh pickpocket-specific note), Zhang Xiaolin as one of the Three Big Bosses
  (ch06; his assassination cross-referenced from ch06).
- **Renderings settled B03 (in glossary; reuse):** the Three Harmonies Society
  (三合会, the Triads), the Elder Brothers Society (哥老会), the Chee Kung Tong
  (致公堂), the Small Sword Society (小刀会), the Hanliu (汉留, provisional), the
  Revive China Society (兴中会), the Revolutionary Alliance / Tongmenghui, the
  Revive Han Society (兴汉会), the Hongxing Association (洪兴协会), the Wusheng
  Mountain (五圣山), the "Seabed" (海底), the Red Flower Pavilion (红花亭), the
  Yellow Way Society (黄道会); Hong Ying, Chen Jinnan, Zheng Chenggong (Koxinga),
  Wan Yunlong, Su Hongguang, Sun Yat-sen, Huang Xing, Song Jiaoren, Situ
  Meitang, Xu Langxi, Wang Yucheng (汪禹丞), Xiang Songpo, Zheng Ziliang, Xue
  Gengshen, Yu Qiaqing, Cheng Ziqing, Jin Jiuling, Chang Yuqing, Lu Liankui,
  Gao Xinbao, Xu Caicheng, Wei Tingrong, Lu Lanchun, Chen Qimei, Kawashima
  Yoshiko. Kept 军统 = "the Juntong" (unsettled until B08).
- **Provisional / left as printed (for the B10 reconciliation):** the Hanliu
  romanization; the lodge founder names in the ch07 tables (many single-
  appearance, OCR-corrected but unattested); 荩忠山 (Guo Yongtai's lodge, the
  top graph faint on the scan); 福建霞宁县 (Guo Yongtai's county, uncertain
  reading); 和丛亮（又名徐为彬） and 杨庆/杨庆山 in the ch07 Juntong-committee
  list (garbled, rendered as best-read); 赵志游 (ch08, distinct from Du's
  disciple 赵志英); 张法党 (Zhang Xiaolin's son, as printed).
