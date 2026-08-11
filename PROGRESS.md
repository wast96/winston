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

## B04 DONE (ch09–ch12, printed 108–137)

- **Scope.** ch09 "张仁奎与仁社" (Zhang Renkui and the Ren Society, UNBYLINED memoir);
  ch10 "我的老师袁寒云" (My Teacher Yuan Hanyun), by **Chen Timin (陈惕敏)**, Yuan's
  Green Gang disciple; ch11 "先父徐朗西生平事略" (A Brief Life of My Late Father Xu
  Langxi), by his son **Xu Xiaogeng (徐晓耕)**, set down by Yang Shi (杨×实, middle
  graph spaced/illegible); ch12 "黄金荣事略" (A Brief Account of Huang Jinrong), byline
  **乡波 (Xiang Bo, a pen name)**, reprinted from 中华民国史资料丛稿·人物传记. PDF 117–146,
  printed 108–137.
- **Author footnotes:** ch09/ch10/ch11 carry NONE (page feet checked by eye). ch12
  carries ONE editors' note ① (李志清 absconding with Huang's valuables), reproduced as
  an "Editors' note." entry. ch11's "(Set down by Yang Shi.)" and ch12's source-line are
  in-text attributions, not foot-notes.
- **Checks, all green:** verify_unit parity 26/26 (ch09), 29/29 (ch10), 16/16 (ch11),
  26/26 (ch12); check_numbers 0 unresolved all four (noise extended, below);
  check_align OK (medians 5.22 / 4.68 / 5.10 / 4.95 en/han); check_content OK all units
  (docs/sources cfg regenerated in work/ to cover ch01–ch12); qc_entities 0 misses all
  four (and no glossary miss surfaced in ch01–ch08 against the enlarged glossary);
  check_structure ALL PASS (214 anchors 0 unresolved, headings OK); check_register vs
  the frozen ch03 reference within tolerance; check_apparatus 0/0; qa_epub PASS
  (214 ref/body/backlink); **epubcheck 0/0**.
- **Apparatus:** 54 notes (ch09 15, ch10 14, ch11 10, ch12 15); running total 214.
  Glossary +83 rows (178 total).
- **Figures:** NONE. All four are text-only (page images eyeballed). Recorded as a
  deliberate empty figure decision.
- **Crop-verified against the scan (systematic mangles both OCR configs shared / that I
  named):** ch09 — 张仁奎 (dozens of variants), 赵子超 (=Zhao Dan's father, ✓超 not 起),
  张詧字退庵, 徐静仁, 陈光甫, 高鑫宝, 蒋鼎文/朱绍良, 韦敬周, 盛昇颐 (not 盛异虞), 周象贤,
  袁良 (not 者良), 吴启鼎, 张竹平/葛福田, 葛光庭/宋哲元/韩复榘, 大生第八纺织公司, 76th
  brigade, 二十四颗当. ch10 — byline 陈惕敏, 袁家嘏/家彰/家骝 (老三=Yuan Jialiu the
  physicist), 步章五(号林屋山人), 褚玉璞, seal "上第二子", 段祺瑞小站. ch11 — byline 徐晓耕,
  郑弼臣, 头山满/宫崎寅藏, 峪云山, 唐继尧/姚以价/徐永昌/阎志远, 陈树藩/于右任, 程克祥/彭盛木/
  彭寿, 张国威, recorder 杨×实. ch12 — 字锦镛, 黄炳泉/邹氏女/余姚, 聚宝茶楼 (not 又宝),
  樊尔谛+樊菊丽, 太保阿书/猪猡阿美, 周荫人/杨知候, 俞叶封, 苏州唯亭乡 (not 叭亭), 张镜湖,
  杨虎/陈群/王柏龄/白崇禧, 王文奎 (not 王文计), 龚天健 (not 裴天健), 郝鹏举 (not 骆股举),
  鲁锦臣 (not 伍锦臣), 邱子善 (not 骆子善), 黄源焘, 李志清, 徐林诚/陶雪生/颜秀吾/田铁夫/
  丁聚堂/沈靖华/韦长镇/杨士杰/周阿福, 3,500,000 银元 + 60 余亩. Tails read against the
  p123/p134/p139/p146 scans (rule 4): faithful, no invented bridging.
- **Source claims footnoted honestly:** Xu Baoshan's curio-bomb killing dated to 24 May
  1913 (the text frames it "during the 1911 Revolution" — hedged as CONTRADICTED); the
  Xingzhonghui "organized in Tokyo" is CONTRADICTED (Honolulu 1894 / Hong Kong 1895; the
  Tongmenghui was the Tokyo body) — Sun's Hongmen membership itself corroborated (Chee
  Kung Tong, 1904). Memoir-tier / uncorroborated, footnoted as such: the Zuo Zongtang
  "Dragon Head" legend, Ge Guangting's Jiaoji-Railway identity, Zhang Zongchang making
  Yuan Kewen "Advance Army commander," the "National Nine-Dragons Conference," the Lake
  Tai consul-clerk rescue, Huang Yuantao as a Zhongtong agent, and — with its outline
  plausible but unverified — Xu Langxi's introduction of three named Juntong agents to
  Zhou Fohai (Zhou's own Dai Li/Chongqing channel IS documented). ch11's pro-CCP framing
  (a son's 1986 memoir) is flagged as an interested witness. CORROBORATED and noted:
  Zhang Xiaoruo's 1935 assassination, Zhao Dan's father, Yuan Jialiu = the physicist,
  the April-12 agents (Yang Hu/Chen Qun/Wang Bailing/Bai Chongxi), Ding Mocun/Mei Siping,
  Hao Pengju, Huang's 1951 self-confession and 1953 death.
- **Source's own inconsistency (left as printed, footnoted):** Zhang Renkui's hao given
  as 锦湖 (Jinhu) in ch08/ch09 but 镜湖 (Jinghu) in ch12 — rendered as printed in each,
  cross-referenced in the ch12 note.
- **Cross-shelf reconciliation done this batch:** 宋子文 → **"T. V. Soong"** (ch07 already
  used it; my ch09 draft "Song Ziwen" corrected; authority.json agrees). 孔祥熙 →
  **"H. H. Kung"** (authority.json marks it a reconcile; picked the conventional form to
  parallel Soong; 孔祥熙 is new to this book). 晶报 → **"The Crystal"** (ch06 had rendered
  it "Jing Bao"; updated ch06 to match ch10 — one rendering per referent). glossary +
  ch06/ch09 readings updated, rebuilt, re-verified.
- **noise.txt extended (each entry commented, longest-literal-first; 一二八五 relocated
  ABOVE 一二八 so the Jan-28 rule can't orphan its 五):** 红十字, 一二八五, 不知其二, 四明,
  李征五, 化整为零, 两腿, 第二天, 上万, 二字, 三字, 三原, 两系, 十二万分, 三轮车, 万岁,
  三牌楼, 一百零八将, 三鑫, 两手空空, 巨万, 数以千计, 牌九. Genuine quantities carried as
  digits in the English (100,000 yuan; 20,000 silver yuan; 3,500,000 銀元; 100 yuan/day).
- **NOT re-noted (already placed):** Zhang Renkui bio (ch08), the 24 generation-
  characters / Da-Tong-Wu ranks (ch05), the April 12 coup (ch02), Chen Qimei / 陈英士
  (ch07), Xu Langxi bio (ch04, ch07), the Juntong (ch06), Du Yuesheng / Huang Jinrong /
  Zhang Xiaolin as the three bosses (B01–B02), Kawashima Yoshiko (ch06), Yang Hu / Gu
  Zhuxuan (ch08). Wang Shouhua gets his first dedicated note here (ch09), cross-referenced
  from ch12.
- **Voice sheets (dialogue begins here).** YUAN HANYUN (ch10 speaker): a cultured,
  relaxed, faintly ironic aristocrat-aesthete; opium-couch ease, literary allusion,
  gang-kinship banter ("your Grandfather Zhang"); contractions in his speech but not
  street-colloquial. CHEN TIMIN (ch10 narrator): deferential, precise, self-deprecating.
  ch10 is the FIRST genuinely dialogue-bearing chapter (2.8 contractions/1k — right for
  cultured reminiscence, not the gangster register to come); it can serve as a dialogue
  reference for later cultured-memoir speech, while the boastful Huang/Du household voices
  (B05+) will want their own, higher-contraction baseline.
- **Provisional / left as printed (for the B10 reconciliation):** ch09 single-appearance
  Nantong figures (蒋暇堂, 韩奉持, 赵汉生, 许泽初, 赵鸿祠), 盛昇颐; ch10 黄伯炮, 俞佩文,
  浦应仙, 吴桐渊, and the seal 上第二子; ch11 徐晓耕, 郑弼臣, 张国威, 峪云山 romanization,
  中华艺术专科学校 (sources give 新华艺专/上海美专), recorder 杨×实; ch12 樊尔谛, 龚天健,
  王文奎, 鲁锦臣, 邱子善, 李志清, 黄源焘, and the puppet-army/-county roster (徐林诚,
  陶雪生, 颜秀吾, 田铁夫, 丁聚堂, 沈靖华, 韦长镇, 杨士杰, 周阿福), plus the bandit
  nicknames 太保阿书 / 猪猡阿美.
- **Tooling:** no script logic changes. work/structure_cfg.json + work/content_cfg.json
  regenerated to cover ch01–ch12 (heading_depth 1). A note-ordering trap fixed at build
  time, NOT in code: two ch10 notes ended at the same character ("...the second son of
  Yuan Shikai"), one anchor a suffix of the other, so their markers tied and inverted
  (qa_epub "not sequential"); re-anchored the Yuan Kewen note to end earlier ("Yuan
  Hanyun, whose given name was Kewen"). Lesson for later batches: never give two notes
  anchors that END at the same point.

## B05 (ch13-ch14, printed 138-194): Huang Jinrong's steward and insider memoirs

Finished from the mid-flight resume: the two long Huang Jinrong memoirs, ch13
(Cheng Xiwen, the steward) and ch14 (Huang Zhenshi, the insider), had their
English drafted and pushed by the prior session; this batch built the zh
sources, the apparatus, the glossary, and the EPUB.

- **zh sources rebuilt from OCR, not from the candidate.** build_zh_candidate's
  output was misaligned (embedded section markers, offset boundaries), usable
  only as raw OCR. Both files were reconstructed paragraph by paragraph against
  the English: data/zh/ch13.txt (69 body lines) and data/zh/ch14.txt (87 body
  lines), force-added because data/zh/ is gitignored. Sections I-III of ch13
  came from the prior session's hand-verified partial.
- **Checks ran, all clean.** verify_unit (parity + numbers) 69/69 and 87/87,
  0 unresolved numbers each; qc_entities 0 misses both; check_align OK
  (median 4.92 and 5.06 en/han); check_content OK (215 and 233 name
  occurrences, all in the paired paragraph); check_register within tolerance
  of the ch03 reference (ch13 17.5 contr/1k, ch14 11.4, both 1.00x); qa_epub
  PASS (238 refs/bodies/backlinks); epubcheck 0 errors 0 warnings.
- **Crop-verified names (dual-OCR flagged or English-source disagreement).**
  The recurring secretary is 龚天健 = Gong Tianjian (one man across both
  chapters; the English "Fei Tianjian" and the resume note's 费天健 were both
  wrong, corrected in ch14 zh and en). Also read off the scan and corrected:
  马鸿魁 = Ma Hongkui (not 奎), 龚兆熊 = Gong Zhaoxiong (English had "Pei
  Zhaoneng"), 徐笠衫 = Xu Lishan (English had "Xu Dashan"), 胡憨珠 = Hu Hanzhu
  (English had "Hu Shuzhu"/"Hu Bingzhu"), 李云生 = Li Yunsheng (English had "Li
  Yunbi"), 郑慕周, and 蒋恒祥 = Jiang Hengxiang (ch13 OCR 蒋重祥 was a mangle).
  三菱洋行 (Mitsubishi) and 傅筱庵 (Fu Xiaoan) confirmed on the same pass.
- **Cross-chapter ledger fixes.** 金廷荪 was carried in glossary and in
  ch03/ch06/ch08 as the typo "Jin Tingsu"; corrected to Jin Tingsun everywhere
  (correct pinyin, 荪 = sun). 王柏龄 conformed to the glossary form Wang
  Bailing in ch13/ch14 (ch12 already used it). These are book-wide corrections,
  applied now rather than deferred.
- **Numbers: noise vs digits.** Extended data/noise.txt with this batch's
  numeral-bearing proper nouns and idioms (八仙桥, 六国饭店, 三菱洋行, 王八妹,
  成千成万, 呼幺喝六, 三分, 一两万, 二三千-class, 九一八, 黄楚九, 万荣, 万墨林,
  阿三/阿四/阿六, etc.). Genuine specific quantities were carried as digits in
  the English per the book's convention (100,000 yuan; 50,000; 9,600 cash;
  150 li), correcting a few word-form amounts the prior session had left
  spelled out.
- **NO figures in B05, deliberate.** The two long household memoirs carry no
  plates in the source; figures.json has no ch13/ch14 entries by decision.
- **24 footnotes (12 per chapter).** The source's own apparatus reproduced:
  the ch13 author's note defining the "Five-Sheng Party" (p138), and the two
  ch14 editors' notes at p167 (the two-sisters correction pointing to Cheng
  Xiwen's account, and the Ye/Lin Guisheng variant). Two claims fact-checked
  against scholarship and footnoted as printed: the "Bishop Yao" rescue
  (conflates/contradicts the 1923 Lincheng Outrage, Sun Meiyao's bandits on
  the Blue Express, no French bishop in the record) and the Rong Desheng
  kidnapping (the real case was 1946, extorted 600,000+ USD by Nationalist
  officials, not Huang's early-career doing). Huang's aid to Sun Yat-sen
  footnoted as uncorroborated self-report. Plus reader-model glosses (bairen /
  men about town, Annamese constables, share-parties, gudao "solitary
  island", January 28 and August 13, the Anqing Gang generations, girl-show
  troupes, reasoning-tea, red-and-white rice, Wing On, Su Yu, pingtan).
- **NOT re-noted (already placed):** the April 12 coup (ch02), the Green Gang
  generation-poem and Da/Tong ranks (ch05), the Sanxin opium combine and No.
  76 Jessfield Road (both well covered in ch05-ch12; No. 76 has eleven prior
  notes), Lu Lanchun (ch12, cross-referenced from the ch13 An Shuyuan note),
  the Rong and Heng Societies (ch12/earlier), Dai Li and the Juntong, Yang Hu,
  Gu Zhuxuan, Chen Shichang. The ch13/ch14 recurrences cross-reference these
  rather than repeat them.
- **Ye/Lin Guisheng kept as printed:** ch13 (steward) names Huang's first wife
  Lin Guisheng, ch14 (insider) names her Ye Guisheng; the source's own editors
  flag the variant and later scholarship favours Lin. Rendered as each narrator
  prints, with the editors' note reproduced and a translator's cross-reference.
- **Provisional / left as printed (for the B10 reconciliation):** the
  single-appearance City God Temple circle (黄玉斋, 陈涵秦 as native-place
  witnesses; 王两般 for "Wang Liangchen"; 席德才 for the English "Xi Delin";
  藤曲三郎 for the Japanese ronin; 燃石八仙 for the "carved-stone Eight
  Immortals"); the long ch14 disciple rosters carry many nicknames rendered
  as printed. 潘七分/潘子欣 (Pan Qifen / Pan Zixin) kept as the source's two
  spellings of one man. 黄源焘/黄元涛 both kept (the source writes Huang
  Yuantao two ways).
- **Voice sheets (Huang household, in use from here).** HUANG JINRONG in
  dialogue: swaggering, boastful, colloquial, contractions throughout, "hmph,"
  boasts of his honour and his services to Sun and Chiang, the "bend when you
  must, stretch when you may" refrain. CHENG XIWEN (ch13): the steward, plain
  and matter-of-fact, non-editorial. HUANG ZHENSHI (ch14): the insider,
  openly contemptuous, "grand hoodlum," reflective and judgmental, with the
  1980s wenshi-ziliao political vocabulary (footnoted once).
- **Tooling:** no script changes. work/content_cfg.json regenerated for
  ch13-ch14 (it is gitignored). The zh files were hand-corrected against the
  OCR rather than replayed through data/ocr_fixes.json, since data/zh/ is
  tracked (force-added) and a fresh checkout carries the corrected files
  directly.

## B06a (ch15 first half, printed 195-221): Fan Shaozeng on Du Yuesheng

- **Scope.** First half of ch15, "On Du Yuesheng" (关于杜月笙), narrated by the
  Sichuan warlord and Du sworn-brother Fan Shaozeng, set down by the Juntong
  memoirist Shen Zui. PDF 204-230 / printed 195-221. Sections 一 (Early
  Activities), 二 (The Special Power Built on Anti-Communism), and the opening
  of 三 (through the first two paragraphs). 119 body paragraphs. B06b continues
  the SAME out/ch15_reading.md and data/zh/ch15.txt from PDF 231 (筹备工作...).
- **Checks, all clean.** verify_unit (parity 119=119, numbers 0 unresolved,
  41 anchors ok), check_align (median 4.79, no pair >2.2x), check_content
  (199 name occurrences, all placed), qc_entities (0 misses), check_register
  (within tolerance of the frozen ch03 ref), check_apparatus (0/0), qa_epub
  PASS, epubcheck 0 errors 0 warnings.
- **TWO content drops caught and fixed before shipping** (rule 4 corollary --
  the tail of a long single-pass paragraph is where faithfulness fails). Pair
  42 (the 1930 strike background) had dropped the whole second half (the
  lockout, the 8-yuan / abolish-fines demand, the KMT-mediation refusal, the
  White Russian strikebreakers); pair 55 (Zhang Yishu) had dropped its whole
  second half (Zhang bailing out Du's disciples by phone/name-card and doing
  his bribery). Both restored and re-verified. Caught by an en/han ratio scan
  plus a zh-vs-en sentence-count scan over every pair; the surviving low-ratio
  pairs (59, 119, 26, 12, 108, 118) were checked by eye and are complete
  (name-dense or terse, not drops). Lesson for B06b: run the ratio + sentence
  scans on the long paragraphs BEFORE the first build, not after.
- **+41 notes** (running total 279). Dense, as planned for the first Du
  chapter; will taper across ch16-21. New this batch: Fan Shaozeng and Shen
  Zui (byline, with the interested-witness framing); the Paoge and gengtie
  birth-cards; He Long; hat-snatching (抛顶宫) and biesan; the Great World
  founder discrepancy (Huang Chujiu, not Huang Jinrong -- factual); Zhuge
  Liang, Song Jiang / "Timely Rain", Lord Chunshen / Lord Mengchang; Zhang
  Jinghu = Zhang Renkui cross-ref (the 镜湖/锦湖 hao); the Chou'an Society "Six
  Gentlemen"; the Four Great Families; the April-12 fullest-account +
  witness-stance note (cross-ref ch02); the July 21 / 1930 tramway strike;
  comprador, Vietnamese constables, White Russians; Li Shizeng; the 1948
  vice-president election; Aviation-to-save-the-nation; Saionji (boast, flagged
  uncorroborated and improbable); the Lytton Commission; the "sixteenth year"
  Central Daily eulogy register; Chiang's first (1927) resignation; Dai Ji vs
  Dai Li; the Sun Sun Company; wahua / paijiu, "big swindle", the Champions'
  sweepstakes, the fabi; the Tongshang Bank (Commercial Bank of China), China
  Merchants, the Jiangyin scuttling; the Heng Society (1932, cross-ref ch03,
  Qing/Chang sub-fraternities); "taking an old man"; Yao Yulan / Meng Xiaodong
  / Mei Lanfang; Huang Tianba / Dou Erdun. Chiang-as-Green-Gang-disciple
  flagged as gang lore, not fact.
- **Chiang-as-disciple, Saionji, Great World founder** are the three
  interested-witness / factual-correction notes (rule 5): rendered as printed,
  the discrepancy stated in the note, never silently corrected.
- **NOT re-noted (already placed):** the April 12 coup mechanics (ch02; here
  cross-referenced with the witness-stance note), Wang Shouhua's murder (ch09),
  the Three Big Bosses (ch06), master-disciple 门生 initiation (ch03), the
  generation-rank system (ch05), the Sanxin opium combine (ch05/ch13), the
  Juntong (ch06), Yang Du's double life (ch04), the Heng Society name-pun on
  Du (ch03), jai alai (ch08), T. V. Soong / H. H. Kung as decided shelf forms.
- **+54 glossary rows** (people; total 262). Added the byline pair and the
  large ch15 cast: Gu Jiatang (顾嘉棠 -- a major recurring enforcer that had
  been MISSING from the ledger through ch12-14; now attested "Gu Jiatang"),
  Ma Shiqi, Ma Xiangsheng, Yang Sen, Liu Xiang, He Long, Chen Kunyuan, Xiang
  Chuanyi, He Beiheng, Wu Guozhen, Yan Huiqing, Zhang Yishu, Saionji, Liu
  Hangchen, the Du children (Weifan/Weiping/Weixin), Yao Yulan, Meng Xiaodong,
  Sun Chuanfang, Wei Daoming, Wu Zhongxin, Li Jishen, Chen Duxiu, Zhou Fengqi,
  Dai Ji, Sun Ke, Li Zongren, Chen Lifu, Wang Zhaohuai, Jin Jiulin, Ji
  Yunqing, Xu Maotang/Maochang, Zeng Kuoqing, Liu Gongyun, Li Shizeng, Jin
  Shaoshan, and others (see work/batch_gloss_ch15.json). 张镜湖 was NOT added
  as a separate row (it is Zhang Renkui's hao; handled by footnote cross-ref).
- **Reused unchanged:** Du Yuesheng, Huang Jinrong, Zhang Xiaolin, Jin
  Tingsun, Chen Qun, Yang Hu, Dai Li, Lu Jingshi, Chen Shichang, Zhang Renkui,
  Wei Tingrong, Lu Liankui, Yang Du, Qian Xinzhi, Zhang Shizhao, Bai Chongxi,
  Han Fuju, Qi Xieyuan, Lu Yongxiang, Gao Xinbao, Wang Jingwei, Yuan Shikai,
  Mei Lanfang, T. V. Soong, H. H. Kung; the Green Gang, Ren/Heng/Rong
  Societies, Sanxin Company, Juntong.
- **noise.txt** grew a ch15 block: 万县, 二三两, (?<=多)两, 四乡, 成千上万,
  成千, 两面三刀, 七二一, 零食, 三山会馆, 金九林, 推三推四, 三(?=、四),
  两银行, 四角 -- all placenames / idioms / measure-word 两 (tael) / date-names
  the extractor read as digits. Every entry commented per the file's rules.
- **Two real quantities carried, not noised:** the 20,000/19,000 USD loan and
  the "over a thousand silver dollars" small-game stake are rendered in digits
  so the number check catches them (the extractor cannot parse "nineteen
  thousand").
- **Provisional / left as printed (for B10 reconciliation):** the foreign
  concession-commanders 巴而雪/邓坎/白多楼 (Ba'erxue / Dengkan / Baiduolou,
  transliterated, unidentified) rendered as printed and NOT glossaried; the
  single-appearance functionaries 唐嘉鹏, 芮庆荣, 彭伯威, 祝绍周, 伍文渊, 斯烈,
  顾苗根, 朱如山, 徐士浩, 吴启鼎, 康心之/康心如, 陆根泉, 张克昌, 张君生,
  甘格霖/费沃礼/沈叔眉 (French consul, police chief, comprador) -- most now in
  the glossary, a few (the foreign commanders) left as printed. 张镜湖/张锦湖
  hao split still open for check_reconcile.
- **Voice.** Fan Shaozeng narrates plain, worldly, first-person, often
  self-implicating (his own black-market fortunes, gambling cuts, warehouse
  killing); Du's dialogue kept to the boastful-boss baseline (the chest-thump
  "what kind of men would we be if we did not help!", the "spend one cash, get
  the effect of ten" maxim). No em dashes in prose to the commissioner; the
  translation uses them as English punctuation.
- **Tooling:** no script changes. Added work/asm_ch15a.py (one-off ch15
  assembler, gitignored under work/) and scripts/band.py (crop a page band by
  OCR line number -- the crop_lines row-mapping is unreliable on this book).
  data/zh/ch15.txt is force-added (tracked) like the earlier zh files; the
  97/98 paragraph split (深明大义 / 识时务) was merged by hand to match the scan,
  and the 106-line drug-income paragraph was restored to the reading.

## B06b (ch15 second half, printed 222-247): Fan Shaozeng / Shen Zui on Du Yuesheng, part 2

- **Scope done.** PDF 231-256, printed 222-247, appended to out/ch15_reading.md
  and data/zh/ch15.txt. Continued section 三 (the ancestral-shrine dedication
  and the sixtieth birthday) and added sections 四 (the first to make a fortune
  from the national calamity and the takeover) and 五 (the downward road), then
  the source colophon. ch15 is now COMPLETE: 217 zh lines, 211 translation
  pairs after headings, 51 notes.
- **All checks green.** check_numbers 0 unresolved (with data/noise.txt);
  check_structure parity 211|211; check_align OK (median 4.83, no strays);
  check_content OK (406 name occurrences, all in the paired paragraph);
  qc_entities 0 misses; check_register within tolerance of ch03; check_apparatus
  0/0; qa_epub PASS (289 notes, 22 pagebreaks); epubcheck 0 fatals/0 errors/0
  warnings.
- **Tail-drop scans (the B06a lesson) run clean.** en/han ratio scan flagged no
  B06b pair below 0.75x the chapter median; zh-vs-en sentence-count scan flagged
  only high-ratio pairs where the English merged clauses. The four longest
  paragraphs (the Zhang Xiaolin assassination, han 556; Wan Molin, 388; the
  price-control saga, 372; the National Assembly election, 318) were each tail-
  verified against the zh: all end on the source's last clause. No drops.
- **Crop-verified readings (19 new, all in data/ocr_fixes.json, v:1).** The
  shrine committee 虞洽卿 (was OCR 嵌洽师) / 庞京周 (须京周) / 袁履登 (媳履登);
  the sedan-pole magistrate 李祖夔 (李祖间); the consul 甘格霖 (甘格震) and police
  chief 毛鼎 (毛紧); the opera stars 尚小云 (肖小云), 龚云甫 (族云南), 王又宸
  (王又宕), 言菊朋 / 肖长华 (言莫朋 / 首长华); 熊式辉 / 段祺瑞 / 刘峙 (能式交 /
  眉凡瑞 / 刘蛙); 俞飞鹏 (俞飞有聘); 通商银行 (通离银行); 张嘉璈 (张嘉琉);
  叶焯山 (叶灶山); 吴绍澍 (吴绍潮). Also crop-verified as printed: 金荣小学,
  两丈见方 flags, 万民伞, the couplet (烟花十万 / 乌履三千 / 以杜甫自况), 三百多人
  at the eve party (not 三十), the money figures (米价三十多万/五十多万一石,
  义演二十多亿, 寿仪三十多亿, 卖房一百七十根金条 / 四十五万美元 / 遗产二十五万
  美元), and folios 222 and 246 (offset 9 confirmed both ends).
- **noise.txt grew a B06b block.** 五体投地, 接二连三 (idioms); 胡叙五, 万昌米行,
  and the bare surname 万(?=[是来留不]) = Wan Molin; the 多/几-split myriad
  compounds 三千多万 / 三十多万 / 五十多万 / 二十多亿 / 三十多亿 / 十几万 / 几万名
  / 几十万 (English carries "more than thirty million", "three hundred thousand",
  etc.); 万民伞; and a SECOND 四川 pass after 几十万 (the early guarded 四川 rule
  skips 四川 when it follows 万 in 几十万四川, so it needs a second unguarded-
  position pass). Every entry commented per the file's rules. Three real
  quantities were fixed in the English instead of noised: 十万 blossoms (was
  "ten thousand"), the 2,800 Yong'an shares, and the 170 gold bars, all now in
  digits so the check catches them.
- **Renderings settled this batch.** Two puns footnoted: 武库世家 (Wu Peifu's
  plaque casting Du as the general Du Yu, "Du of the Arsenal") is glossed inline
  by the source; the flatterers' essay "以杜甫自况" (a second Du Fu) gets a note.
  吴敬恒 = 吴稚晖 = Wu Zhihui (the same man; the birthday-essay signer 吴敬恒 was
  rendered "Wu Jinghen" at first, corrected to Wu Zhihui so there is one
  referent, one rendering). 梅乐斯 rendered "Miles" in prose (glossary en set to
  Miles to match). CC clique written "CC" in the zh where the OCR read "O CQ".
- **Glossary +46 rows (now 308).** Seven organizations (益社, 港济公司, 通济公司,
  忠义救国军, 中美合作所, 扬子公司, 保密局) and the new political / military /
  operatic cast (蒋经国, 孔令侃, 宋美龄, 胡宗南, 顾祝同, 唐绍仪, 高宗武, 陈布雷,
  虞洽卿, 张嘉璈, 毛人凤, 吴开先, 杨杰, 黄琪翔, 章伯钧, 吴绍澍, 王新衡, 杜维屏,
  杜维垣, and the rest). Reused unchanged: Du Yuesheng, Dai Li, Gu Jiatang,
  Yang Hu, H. H. Kung, T. V. Soong, Qian Xinzhi, Lu Jingshi, Xu Caicheng, Wan
  Molin, Yao Yulan, Meng Xiaodong, Zhang Xiaolin, Chen Gongbo, Wang Jingwei,
  the Heng Society, the Sanxin Company, the Juntong.
- **+10 notes (ch15 now 51, book 289).** ten-thousand-citizen umbrellas (万民伞);
  the shrine plaque "Filial thoughts unfailing" (孝思不匮); the Du Fu surname pun;
  Guo Ziyi as the byword for a complete life; the gold yuan certificate (1948
  reform and collapse); the Sino-American Cooperation Organization (SACO / Miles);
  the Baomiju (renamed Juntong) with the note that Shen Zui, the recorder, here
  steps into his own account; the shangfang "imperial sword"; the Loyal and
  Patriotic Army; and "a first-rank commoner" (一品老百姓). NOT re-noted (already
  placed): the April 12 coup (ch02), the Juntong (ch06), the Heng Society and
  Lord Chunshen and Shen Zui and Fan Shaozeng (ch15 first half), the Sanxin
  Company and Chiang Ching-kuo's tiger-beating (ch13), fabi and the New Fourth
  Army and the Marco Polo / July 7 incident (earlier). Cross-referenced, not
  re-noted.
- **Figures.** None. find_figures 231-256 flagged nothing; the chapter is
  continuous memoir prose. Empty figure list is a deliberate decision, as in
  B06a.
- **Voice.** Unchanged from B06a: Fan Shaozeng plain, worldly, first-person,
  self-implicating (the opium-delivery cut, the grenade in Cheng Yanqiu's
  theater, the six votes bought at the National Assembly); Du's dialogue on the
  boastful-boss baseline ("I have held Chiang Kai-shek up all these years, and
  it has come to this"). No em dashes in prose to the commissioner.
- **Tooling:** no script changes. work/asm_ch15a.py reused as a starting point;
  the second half was reconstructed paragraph by paragraph from data/txt against
  the English and crop-verified. data/zh/ch15.txt force-added (tracked).

## B07a — ch16 (杜门话旧, "Reminiscences of the Du Household") — DONE

- **Scope:** ch16, PDF 257-276 / printed 248-267. A NEW chapter in new files
  (out/ch16_reading.md, data/zh/ch16.txt), 58 paragraphs, 4 numbered sections
  (一-四; the source marks them (一)-(四) with no titles, rendered ### I-IV).
- **Narrator / byline:** 黄国栋口述　罗醴泉整理 — Huang Guodong (Du's household
  chief accountant, entered at 24), taken down by Luo Liquan. Byline confirmed
  by crop. This is the household-insider's view of Du: the two mansions, the
  wives and children, the whole hired establishment and its cost, Du's gang
  rise, the wartime Hong Kong years, and the strange last months before
  liberation.
- **Pipeline:** render 257-276 --dpi 300; ocr_crop 257-276 --left 0.06 --right
  0.91 --top 0.09 --bottom 0.89 --lang chi_sim --psm 6 (pgrep -c tesseract = 0
  after); ocr_dual for the second read. zh reconstructed paragraph by paragraph
  from data/txt against the English, 1:1, headings ###; build_zh_candidate NOT
  used (mis-aligns, guardrail c). data/zh/ch16.txt force-added.
- **Checks (all green):** verify_unit (58 pairs, numbers 0 unresolved, 17
  anchors ok); check_align (median 4.82 en/han, no stray > 2.2x); check_content
  (317 name occurrences, all in the paired paragraph — after fixing the drift
  below); qc_entities (0 misses; census 杜月笙 x43, 黄金荣 x19, 万墨林 x18);
  check_register --ref out/ch03_reading.md (within tolerance); zh-vs-en
  sentence-count tail scan (no long-paragraph clause drops); check_apparatus
  (0 failures). Built cumulative EPUB (16/28, 306 notes), qa_epub PASS,
  epubcheck 0/0.
- **Cross-chapter drift caught and fixed:** 叶焯山 was rendered "Ye Zhuoshan" in
  ch15 (焯 = zhuō); I had written "Ye Chuoshan". Corrected the glossary row and
  ch16 to "Ye Zhuoshan" — ch15 now passes check_content too. (Adding a glossary
  row makes check_content re-check every prior chapter for that name; a mismatch
  surfaces immediately. Worth remembering.)
- **Register / digits:** house rule "digits for specific quantities" — the
  salaries, the 600,000-dollar house, the debt figures (5,700,000 / 2,400,000 /
  300,000 / 2,000,000), the flower-basket sums, Room 705, No. 181, and the
  120-odd telephone numbers are all digits; small counts (six weddings, three
  horses, nine at dinner) stay words.
- **+113 glossary rows (total 421).** The chapter is a who's-who; nearly every
  hired hand, guest, and gang figure is named. New principal-cast-adjacent:
  黄国栋, 罗醴泉, 黄文祥, 杨渔笙, 陈帼英, 孙佩豪, 万墨林, 万兆棠. The household staff
  (翁佐卿, 邱访陌, 王幼棠, 胡叙五, 陆桂才, 陈秦鹤, 陈继藩, 高怀礼, 王宝钰, 郁访熏);
  the gang gallery (谢葆生, 杨顺铨, 范开泰, 范回春, 范恒德, 徐德胜, 袁宝珊, 叶焯山,
  戴步祥, 江肇铭, 浦贤元, 樊良伯, 夏连良, 陈荣生); the wartime cast (蒋伯诚, 汪曼云,
  傅品圭, 傅筱庵, 徐庆云, 邵得度, 唐生明, 唐生智, 袁履登, 林康侯, 金鼎勋, 丁如松,
  蔡庆其, 张慰如, 张锦寿); and the liberation-eve figures (周恩霆, 宋霭龄, 盛丕华,
  潘汉年, 张澜, 史良, 沙千里, 廖承志). Reused unchanged from prior batches: Du
  Yuesheng, Huang Jinrong, Zhang Xiaolin, Jin Tingsun, Gu Jiatang, Chen Qun,
  Qian Xinzhi, Zhang Shizhao, Yao Yulan, Meng Xiaodong, Du Weiping, Du Weifan,
  Chiang Ching-kuo, Kong Lingkan, Song Meiling, Xu Caicheng, Lu Jingshi, Zhu
  Xuefan, Rui Qingrong, Ma Xiangsheng, Gu Zhuxuan, Lu Yongxiang, He Fenglin, Wu
  Shibao, Wu Kaixian, Zhang Yishu, Lu Lanchun, Wei Tingrong, Ding Yongchang,
  Tang Jiapeng, Gao Xinbao, Fan Kaitai, Huang Zhenshi, Xu Maotang, Wen Lanting,
  Wang Xiaolai, Liu Hongsheng, Pan Gongzhan, Xu Jiqing.
- **+17 notes (ch16), book total 306.** Zhonghui Bank; Shiliupu; the aviation
  lottery; Meng Xiaodong; the Four Guardians; pingtan; Yang Du (the monarchist
  who was secretly a CCP member); the Hardoon Garden; the January 28 (1932)
  incident; Fu Xiao'an (the assassinated puppet mayor); the Dadao puppet city
  government; the "three notables of Shanghai"; Meng Linghui (= Meng Xiaodong);
  Zhang Lan; Liao Chengzhi; Pan Hannian; and Zhou Enting (this last reproduces
  the source's own footnote and flags the uncorroborated "Zhou Enlai's cousin"
  claim). NOT re-noted (already placed): 老头子 and Chen Shichang as Du's Green
  Gang master (ch15); the Du family shrine at Gaoqiao (ch15); Huileli (ch15);
  the Lu Lanchun / Huang-Jinrong-arrest / He-Fenglin rescue (ch08); No. 76
  Jessfield Road puppet secret service (ch04, ch06); the "solitary island"
  (ch03, ch14); fabi and the gold yuan certificate (ch08, ch15); Du Weiping's
  arrest / the 1948 buying panic / Kong Lingkan / Song Meiling (ch15, from the
  other witness). Cross-referenced, not re-noted.
- **Figures.** None. find_figures 257-276 flagged nothing; continuous memoir
  prose. Empty figure list is a deliberate decision.
- **Crop-verified readings (29) recorded in data/ocr_fixes.json under "ch16".**
  Key catches: 陈志昌→陈世昌 (Du's Green Gang master); 傅彼攻→傅筱庵; 金策肌→金鼎勋;
  周恩赴→周恩霆; 座承志→廖承志; 砧否华→盛丕华; 茉证街→菜市街; 徐犯党→徐懋棠;
  高效宝→高鑫宝; 谢医生→谢葆生; 吉宝组→袁宝珊; 江药铝→江肇铭; 美良信→樊良伯;
  维得→维翰, plus the Yao Yulan children (维善、维嵩、美如、美霞). Because data/zh
  is tracked and already corrected, apply_fixes replays as a no-op; the ledger
  is the audit trail.
- **Minor low-stakes tier left at best OCR reading (named so as not to
  over-verify):** the defunct fruit-firm and shop names in §1 and §3; the
  Cai Qingqi opera-amateur names (张中原, 孙兰亭, 改剑飞, 张拓生, 孙钧时); 郭兰世
  (provisional) and 蒯德珍 (provisional); the jailbreak plotters (刘绍奎, 陆大公,
  刘俊卿). None recur or bear weight.
- **noise.txt additions (ch16 block):** 五百七十余万, 二百数十万, 二十余万,
  三十多万, 五百多万 (all split by 余/多 before 万); a guarded surname-万 rule
  (万墨林/万木林/万兆棠/bare 万, never the 10,000 multiplier); a guarded tael
  rule ((?<=[余多])两, the unit 两 orphaned by 余/多 else reads as 2); 顾七
  (七 = name), 零用钱 (零 = spare), 沙千里 (千 = name), 中百一店 (百一 ≠ 101).
  Do NOT remove; extend as the number check flags new ones, longest literal
  first.
- **Voice sheet — HUANG GUODONG (ch16 narrator):** the household chief
  accountant. Plain, precise, ledger-minded — inventories the mansions, the
  wives and children, the whole staff and its salaries down to the yuan. Loyal
  insider but a watchful one; survived three wartime arrests and frames himself
  as an anti-Japanese resister working under Du's cover. Reticent before what
  he cannot explain ("I never did make out"), and pointed about the
  liberation-eve mysteries (the sham monk, the Zhou disciple, the Zhang Lan
  dinner, the three letters to Liao/Sheng/Pan) that hint Du leaned toward the
  Communists. 1980s CPPCC vocabulary (汉奸, 伪, 解放). No em dashes in prose to
  the commissioner.
- **Tooling:** no script changes. work/content_cfg.json regenerated with a ch16
  docs/sources entry (work/ is gitignored).

## B07b (ch17-ch18) COMPLETE

**ch17 (我所知道的杜月笙, "The Du Yuesheng I Knew"), Yu Yongfu (郁咏馥), printed 268-283, PDF 277-292.** 62 pairs, 11 notes, +38 glossary rows. The narrator is Du's opium-pipe attendant of some twenty years; six titled sections (origins; life and family; extravagance; where the money came from; friends and retainers; character and tastes). Two of its notes reproduce the SOURCE's own footnotes: the byline compilation note (a pre-Cultural-Revolution CPPCC office piece from Yu's oral accounts) and the Yang Du / Gu Ao note (per Pang Jingzhou, neither was really a secretary).

**ch18 (杜月笙打进大达轮船公司经过, "How Du Yuesheng Broke into the Dada Steamship Company"), Huang Yongyan (黄永言), printed 284-292, PDF 293-301.** 22 body paragraphs (23 pairs with the byline), 8 notes, +74 glossary rows (glossary 533 total after B07b; book 325 notes). A business-and-politics chronicle: the three-Yang pun; Yang Guanbei steering Du into the Zhang brothers' Dada line; the wharf brawl and the social-bureau petition; the shipping rivalries (Datong, Ping'an, Daxing/Sanbei); and the Huang Zhendong sugar-boycott squeeze, which is where the Yuebao launch of ch17 came from.

**Checks (both units):** parity 62/62 and 23/23; check_numbers 0 unresolved; check_align no outliers (the long ch18 paragraphs tail-verified against the scan); check_content clean for ch17 and ch18 across the whole book; qc_entities 0 misses; check_register within tolerance of ch03. qa_epub PASS (28 documents, 1002 paragraphs, 325 notes all resolving); epubcheck 5.1.0 clean (0 fatals, 0 errors, 0 warnings).

**Crop-verified readings (data/ocr_fixes.json, ch17 and ch18 keys).** ch17: 郁咏馥 (byline, not the OCR 郁咏敌/郁咏禾); 城厢长生桥 (not 长生帮); 杜三十岁生日 (not 三嫂); 亨利路 = Route Paul Henry; 张翼枢 (the Concession's Chinese councillor); 汤玉麟 of 热河; the Sanxin middle-six 顾嘉棠/金廷荪/叶焯山/芮庆荣; 高鑫宝; 江肇铭; 顾鳌 (not 丘鳌); 维仁 (source variant); 城隍庙 five sedan-chairs 抬送高桥. ch18: 黄永言; 三阳开泰; the capital figures 23,537 / 527,500 / 1,655,734 taels (digit-for-digit); 张謇/张詧 brothers; 蒋敬堂; 张慰慈 (张詧's grandson); 沈燕谋/沈敬夫; 徐陶菴/徐揭和; 张孝若 (张謇's son, 謇 confirmed against 詧); 蔡劲军 (police chief); 郑锡棠; 李耀庭; 吴颙 (航政局长); 杨在田 (盐贩, the Datong boss); 陆伯鸿/朱志尧.

**noise.txt additions.** ch17: 二百多万, 四十多万 (split-万); 两角 (a twenty-cent coin); 老四, 老五 (wife by-names). ch18: a general tael-unit rule, (?<=[numeral])两, that strips the unit 两 (liang) after any numeral. This fixes a real parser bug: because 两 sits in the numeral class, the tokenizer fused it onto the preceding number and mis-valued it (五百两 read as 502, 二万三千五百三十七两 as 23532). The rule is book-wide and safe (两 meaning "two", as in 两艘/两个, is never numeral-preceded). Also 垂涎三尺, 百分比, 三北, 沈荣三, 谢葆三. Do NOT remove.

**Cross-chapter reconciliations (glossary aligned to the earlier form, per the known trap).** ch17 places: 八仙桥 = Baxianqiao, 金陵东路 = East Jinling Road, 小东门 = the Small East Gate, 郑家木桥 = Zhengjia Wooden Bridge, 敏体尼荫路 = Rue Montauban (see below). ch18: 苏北 = "northern Jiangsu" (per ch09/12/13/15; ch18 text changed from "Subei" throughout); 怡和洋行 = "Jardine Matheson" (per ch07; ch03's one-off "Jardine's" changed to match, a single-word global edit; ch18 changed from "Jardine, Matheson").

**Open for B10 (whole-book reconciliation).** (1) 敏体尼荫路 is rendered "Rue Montauban" to match ch08, but the road is historically Route Montigny (敏体尼 = Montigny); both give today's Xizang South Road. A scholarship call. (2) Pre-existing content-check flags NOT caused by B07b (latent because earlier batches content-checked only their own unit): ch03 p29 (吴绍澍/Wu Shaoshu), ch13 p39-41 (福煦路/Avenue Foch across three gambling-house paragraphs), ch13 p58 (傅筱庵/Fu Xiao'an). A human read should confirm pronoun false-positive versus real omission. (3) Source discrepancies kept as printed and footnoted: ch17's 维仁 (Yu's son-list differs from ch16's); ch17's Madam gloss; ch18's May-Third-Incident year (1927 for 1928) and its "Zhu was the bishop of Haimen" (Zhu Zhiyao was a layman; the bishop was his kinsman Zhu Kaimin).

**NOT re-noted in B07b (placed earlier, cross-referenced instead):** the Battle of Shanghai/八一三 (ch14); the gang "old man"/老头子 (ch15); the Green Gang generation ranks 通/悟 (ch05); the Sanxin Company (ch13); the aviation lottery (ch16); Yang Du's Chou'an Society/Hongxian context (ch15); Meng Xiaodong (ch15/16); the "yellow" unions (ch03); the Heng Society (ch15); "men of mark"/闻人 (ch05/16); Avenue Foch and the No. 181 gambling house (ch08/13); Rue Wagner, Route Doumer and the Eighteen-Story Building (ch16); Yu Qiaqing, Zhang Shizhao, H. H. Kung, T. V. Soong, Dai Li, Yang Hu, Chen Qun (all earlier).

**Voice sheets (new).** YU YONGFU (ch17): Du's opium-pipe attendant for twenty-odd years, the view from the smoking-couch. Plain and humble; matter-of-fact even about blindings and gambling ruin; wry about his own perks ("I was the exception"); reticent about what he could not see. 1980s CPPCC framing. HUANG YONGYAN (ch18): a shipping-world chronicler. Analytical and documentary, plainly hostile to Du's methods (巧取豪夺, 敲竹杠), dense with company names, dates and figures, almost no dialogue.

**Tooling:** no script changes. work/content_cfg.json regenerated with every unit's docs/sources so the new glossary rows were re-checked against all earlier chapters (work/ is gitignored).

## B08a (ch19) COMPLETE

**ch19 (杜月笙出任上海面粉交易所理事长的经过, "How Du Yuesheng Became Chairman of the Shanghai Flour Exchange"), Huang Bingquan (黄炳权), printed 293-299, PDF 302-308.** 9 body paragraphs (11 pairs with heading and byline), 6 notes, +32 glossary rows (glossary 567 after the two generic rows were pulled, see below; book 331 notes). A first-person operator's account: the narrator, an electric-power man in Nanhui and Chuansha who doubled as the exchange's warehouse director, engineers a "fight poison with poison" bear raid in Du's name (500,000 then 800,000 sacks dumped to force a limit-down halt, 1,300,000 short in all), backstops the halt with a Bureau of Social Affairs proclamation obtained on Du's letter, settles the corner, and then rigs the August 1936 shareholders' election so that Du unseats the longtime chairman Wang Yiting and takes the chair. The chapter is the book's clearest set-piece on how Du's clout, an underling's cunning and a friendly official converted a market panic into a boardroom takeover.

**Checks.** parity 10/10; check_numbers 0 unresolved (the number-dense margin paragraph carries every figure as digits: 500,000 / 800,000 / 1,300,000 sacks, 3.4 and 3.2 yuan, 200/0.2 and 100/0.1 yuan margins, the 0.2-yuan halt trigger, the three-day limit, the 60-pound bushel, 5 US cents, 80 percent of shares); check_align no outliers (median 5.10 en/han; the two long paragraphs, the discount-system background and the election, tail-verified against the scan); check_content clean for ch19 across the whole book; qc_entities 0 misses; check_register within tolerance of ch03. qa_epub PASS (28 documents, 1011 paragraphs, 331 notes all resolving); epubcheck 5.1.0 clean (0 fatals, 0 errors, 0 warnings).

**No source footnotes in ch19** (all seven pages checked; no asterisk or circled-numeral small print at the page feet).

**Crop-verified readings (data/ocr_fixes.json, ch19 key, 25 entries).** byline 黄炳权 (not 黄柄权); 骎骎乎 (居于, the horse-radical literary adverb, not the OCR 恒蝶乎); the four brokers 杨镜澄/王忠良/张松春/顾竹年 (顾竹年, not the OCR 顾人竹年); 朱如山 (not 朱如出) and 钟可澄; 华格臬路 (Rue Wagner, not the OCR 华将泉路); 兼职厚禄 (not 摩禄); 踌躇了一下 (not 跨踏); 草草不恭 (not 草草不堆); 攸关民食 and 应著该交易所 (the proclamation wording, not 依关/应著访); 诸广成 and 徐咏棠 (棠, not 党); 卞筱卿 (the Nanjing Datong manager, not 卞征师); 荣宗敬, 王禹卿; the Fufeng directors 宁钰亭 then 吕玉荪 (not 日玉苏) then 孙仲立 (not 孙伸立); 顾馨一 (馨, not the OCR 顾志一/顾殴一); 忌嫉 (not 鼠恋); 慷交易所之慨 (the idiom "generous at another's expense," not the OCR 惧...之慨); 曩年 (not 攻年); 胡筠庄 (not 胡针庄); 佯为推辞, 恳切力劝, 曲蟮（即蚯蚓）, 沽名钓誉.

**noise.txt addition (ch19 block).** 再四 (再三再四, "again and again"; 四 is the idiom, not the count 4). Nothing else in the chapter flagged.

**Glossary discipline / a cascade caught and undone.** The batch added 34 rows, then two were pulled after check_content (run over every unit) surfaced pre-existing book-wide inconsistency they would have retro-flagged: 社会局 (rendered "Social Affairs Bureau" in ch03/ch13 but lowercase "social-affairs bureau" in ch14) and 宁海西路 (rendered "Ninghai West Road" in ch16/ch17). 社会局 was removed from the glossary and left for the B10 reconciliation; 宁海西路 was kept but aligned to the earlier "Ninghai West Road" (ch19's prose changed from "West Ninghai Road" to match). 大同面粉厂's en was capitalized to "Datong Flour Mill" to match the prose. Net glossary rows after the pull: 32 new (567 total). The two big attested figures are new: 荣宗敬 = Rong Zongjing (the "Flour King," 1873-1938) and 王禹卿 = Wang Yuqing; 王一亭 = Wang Yiting (1867-1938, the painter-philanthropist and longtime chairman) had a single passing, unnoted mention in ch13 (as a Mitsubishi/Nisshin comprador) and is footnoted here at his substantive appearance.

**NOT re-noted in B08a (placed earlier or glossed inline, cross-referenced instead):** Rue Wagner / the Du mansion (ch16; and glossed inline here as "Ninghai West Road, formerly Rue Wagner"); Rong Desheng (ch13, the kidnapping note; his elder brother Rong Zongjing is noted here); the April 12 coup, the Sanxin Company, the Heng Society, Yu Qiaqing, H. H. Kung, T. V. Soong, Dai Li (all earlier).

**Voice sheet (new). HUANG BINGQUAN (ch19 narrator):** an electric-power businessman of Nanhui and Chuansha who was also the Flour Exchange's warehouse director. A practical, self-aware operator who plainly relishes his own market cunning (the whole "fight poison with poison" corner is his design) and is candid about the manipulation and about his self-interested motives (currying favor with Du, checking a rival standing director). Deploys exchange jargon precisely; dryly cynical about Du's theatrics and the "no salary" pose at the close. 1980s CPPCC framing (解放, 帮会, 流氓).

**Open for B10.** 社会局 rendering is inconsistent book-wide (Social Affairs Bureau vs social-affairs bureau) and was left unglossaried; reconcile in the whole-book pass. The B07b latents (ch03 p29 Wu Shaoshu; ch13 p39-41 Avenue Foch; ch13 p58 Fu Xiao'an; the Montauban/Montigny call) remain.

**Tooling:** no script changes. work/content_cfg.json regenerated over all 19 translated units (work/ is gitignored).
