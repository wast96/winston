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
