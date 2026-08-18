# PROGRESS — The Sword Roars in the West Wind (剑吼西风：中央特科纪事)

The running per-batch log. Written as we go.

## B12 — Chapter Ten "开铺子做买卖 / Opening a Shop, Doing Trade" (ch10)

- **Scope.** PDF 236-247, printed 221-232. Two sections: s1 一、这个人不简单
  "No Ordinary Man" (opener PDF 237, folio 222) and s2 二、第一桶金 "The First Pot
  of Gold" (opener PDF 242, folio 227). Offset held a constant 15; folios read off
  the scan at each opener and confirmed on every text page (223-231). Chapter divider
  p0236 and the washed-out full-page painting p0247 (ch11 divider bleed) are design
  furniture, not figures. 39 body paragraphs. A change of key from the traitor-hunt
  chapters: the Party's COMMERCIAL fronts. s1 introduces Bo Gu (Qin Bangxian), the
  new "man in overall charge" from Sept 1931, and his lineage; s2 follows his younger
  brother Qin Bangli (alias Yang Lin) running the rice shop, furniture shop, and the
  Shantou drugstore courier station that fed the Central Soviet, ending on the firm
  that became China Resources (华润).
- **Source recovery.** data/zh/ch10.txt HAND-TRANSCRIBED off the 300-DPI page images
  (OCR chi_sim psm6, crop 0.06/0.95/0.11/0.955, kept as cross-check only — noisy on
  the names, e.g. 瞿秋白→惧秋白, 洛甫→洛南, the whole Qin genealogy mangled). Chapter
  title + both section heads marked `###` (parity gotcha). Parity exact: 39 = 39
  (check_structure --pairs). Crop-verified the uncertain names by eye: 拱危之 (Gong
  Weizhi, obscure, provisional), 陈友梅 (Chen Youmei, provisional), 张然和 (Zhang Ranhe,
  provisional), 严重 (Yan Zhong), 黄甦 (Huang Su); the geographic 邵阳 (Shaoyang, as
  printed in 陈云传 — flagged in a [—Trans.] note as a likely slip off the route);
  秦摩亚/杨琳/长林 on p0238 (Qin Moya = Bo Gu's daughter; uncle Yang Lin = Qin Bangli;
  "Changlin" = Bo Gu's childhood name, resolved in a note).
- **Register.** Drafted straight against the frozen doc (STYLE.local top sections):
  modern-neutral narration, ch08/ch09 sardonic source-criticism voice kept (the
  却不是…更非… comparison of 红色华润 vs 陈云传 on the furniture shop; the Chen Pannian ≠
  Pan Hannian argument; the deadpan quoting of the very source that makes the error),
  each source's own words preserved, verdicts in the notes. The four-part
  呼风唤雨/暴风骤雨/腥风血雨/凄风苦雨 wind-and-rain figure preserved and footnoted.
  Read the final two pages of ch09 first.
- **Checks, all green.** parity 39=39; verify_unit numbers 0 unresolved (a B12 noise
  block added: 二房东, 百货公司, 三河坝, 三洋坎, 李六如, 十字架 — all lexical numerals in
  names/set-phrases, no real quantity; every real count carried in the English:
  31st/14th generation, five ministries/two capitals, six men/six shops, two gold
  bars, fourteen years, several hundred comrades); check_align median 4.74 en/han,
  no pair > 2.2x; check_content 242 name occurrences all in the paired paragraph
  (ch10 added to data/content_config.json docs+sources; one initial displacement
  fixed — 凯丰 rendered "Kai Feng" to match the glossary, not "Kaifeng"); qc_entities
  0 misses; check_apparatus 0/0; anchors 15/15 resolve; build PASS (10/18 chapters,
  332 notes); qa_epub PASS (91 files, 332 refs/bodies/backlinks); epubcheck 5.1.0
  0/0/0/0; check_register --ref out/ch01_reading.md within tolerance (dialogue
  contraction noisy — this unit runs on memoir/document quotes; narratorial signals
  on-reference: em-dash 6.4/1k, sent median 25, rhythm CV 0.65).
- **The 华润 rendering decision.** 华润 legitimately wears two English faces: the
  transliteration "Huarun" (the Chinese name the book uses) and the official English
  name "China Resources," which the chapter itself introduces and discusses (use vs
  mention, para 32). Glossary `en` = **Huarun** (so qc/content anchor on it), glossed
  "China Resources" at first mention (para 21) and again in the naming passage; the
  book title 《红色华润》 rendered "Red Huarun" for consistency.
- **Tail verification (rule 4 corollary).** The close (p0246, paras 38-39: 政保/外贸
  fronts; the two Mao quotes) re-read against the scan; faithful, nothing invented.
  封锁几十年 kept as "decades" with the received "eight or ten years" in the note.
- **Footnotes: 15 new** (unit total 15; book 332), first-appearance, reader-model,
  verdicts in the note. Headline items: the four wind-and-rain idioms; the Central
  Soviet/Ruijin; the Qin genealogy (Qin Guan the Song poet; Qin Jin the Ming official
  + the Jichang Garden); 吃人礼教 as the May Fourth/Lu Xun trope; the Li Qingzhao
  声声慢 allusion; "Changlin" = Bo Gu + his April 8 1946 death ("4·8 martyrs");
  Qin Bangli/Huarun/China Resources; the Sino-French Drugstore; the courier-line
  roster as the future PRC leadership; the Shaoyang [—Trans.] slip; the Central
  Political Security Bureau (crux of the Chen Pannian argument); the two 1949 Mao
  slogans. New figures: 3.
- **NOT re-noted (already placed earlier) — cross-referenced, not re-noted:** Bo Gu /
  Qin Bangxian (ch09), Li De / Otto Braun (ch08), Wang Ming (ch05/ch08/ch09), Kang
  Sheng (ch02/ch03), Xu Enzeng (ch01/ch08), Gu Shunzhang (ch01), Pan Hannian (ch01),
  Chen Yun (ch02/ch09), Zhou Enlai (ch05), Deng Yingchao (ch01), Chen Duxiu
  (ch01/ch02), Qu Qiubai (ch01), Xiang Zhongfa (ch09), Chen Geng / Qian Zhuangfei /
  Hu Di (ch01/ch08), Deng Xiaoping (ch03), Ren Bishi (ch01), Nie Rongzhen (ch08),
  Dong Biwu (ch09), Zhu De (ch03); the Central Special Branch (ch01), the ACFTU/全总
  (ch07), the Communist University of the Toilers of the East (ch03), the White Terror
  (ch03), 铺保/打保单 "stand the surety" (ch05), the Fourth Plenum / 28 Bolsheviks
  (ch05/ch09).
- **Figures: 3** (`data/figs/ch10-01..03.png`, hand-cropped, printed captions excluded,
  translator's captions with source-label provenance, real alt text): the Bo Gu
  portrait (s1, p0237/folio 222); the Qin Bangli portrait (s1, p0239/folio 224); the
  1937 Qin Bangli family photo (s2, p0245/folio 230). find_figures not relied on;
  every page eyeballed.
- **Glossary: 101 new rows** (70 people, 26 places, 5 organizations), written into the
  sectioned ledger; 30 existing rows reused unchanged. `en` all ASCII. Recurring
  institutional terms flagged `recurring:true`: 华润 (Huarun), 中央政治保卫局 (the
  Central Political Security Bureau), 全总 (the ACFTU), 中央苏区 (the Central Soviet).
  No new concession streets (德辅道/太子行 are Hong Kong, not gazetteer). Consulted
  authority.json: 香港=Hong Kong, 广州=Guangzhou, 瑞金=Ruijin confirmed shelf-wide.

### Renderings settled this batch (also in glossary.json)
- 博古 = Bo Gu (real name 秦邦宪 Qin Bangxian, courtesy 则民 Zemin, pen name 上林
  Shanglin); 秦邦礼 = Qin Bangli (alias 杨琳 Yang Lin, HK name 杨廉安 Yang Lian'an);
  华润 = Huarun (English name China Resources); 张闻天 = Zhang Wentian (alias 洛甫 Luo
  Fu); 卢福坦 = Lu Futan, 李竹声 = Li Zhusheng (both "later turned traitor"); 严朴 =
  Yan Pu; 卓雄 = Zhuo Xiong; 陈潘年 = Chen Pannian ("Fat Chen", ≠ Pan Hannian);
  the Qin memoirists 秦红 Qin Hong, 秦摩亚 Qin Moya, 秦福铨 Qin Fuquan, 秦钢 Qin Gang,
  秦家骢 Qin Jiacong (Frank Ching); 戚元德 Qi Yuande, 吴德峰 Wu Defeng (reused), 卢伟良
  Lu Weiliang, 黄美娴 Huang Meixian; 严重 = Yan Zhong, 黄甦 = Huang Su, 拱危之 = Gong
  Weizhi.
- Places: 汕头 = Shantou, 大埔 = Dabu, 永定 = Yongding, 上杭 = Shanghang, 汀州 =
  Tingzhou, 三河坝 = Sanheba, 瑞金 = Ruijin, 中央苏区 = the Central Soviet, 红庙 =
  Hongmiao, 寄畅园 = the Jichang Garden, 德辅道 = Des Voeux Road, 太子行 = Prince's
  Building, 联合行 = Lianhehang, 联合公司 = the Lianhe Company, 天隆行 = Tianlonghang.
- Orgs: 中法药房 = the Sino-French Drugstore; 复元钱庄 = the Fuyuan money house;
  全总 = the All-China Federation of Trade Unions (reused, ch07).

## B11 — Chapter Nine "向忠发失踪之谜 / The Riddle of Xiang Zhongfa's Disappearance" (ch09)

- **Scope.** PDF 208-235, printed 193-220. Nine sections ch09s01-s09 (openers at
  PDF 209,210,214,216,220,225,229,231,233; folios read off the scan at each; offset
  held a constant 15). The chapter divider p0208 is design furniture. 194 body
  paragraphs. The direct sequel to ch08: how CCP General Secretary Xiang Zhongfa
  fell (seized at the Delle Motor Garage near Jing'an Temple, June 22, 1931) and
  whether he broke, weighed across a dozen contested sources; skeptical of the
  "secret cable."
- **Source recovery.** data/zh/ch09.txt HAND-TRANSCRIBED off the 300-DPI page
  images (OCR too noisy on the proper names — 向忠发/陈志皋/黄慕兰/探勒车行 all mangled,
  as the B10 kickoff warned); OCR (chi_sim psm6, crop 0.06/0.95/0.11/0.955) kept as
  the cross-check only. Chapter title marked `###` per the parity gotcha. Parity
  exact: 194 = 194 (check_structure --pairs).
- **Register.** Drafted straight against the frozen doc (STYLE.local top sections):
  modern-neutral narration, contractions by ear, no inversions, ch08's sardonic
  source-criticism voice kept, each source's own words preserved, verdicts in the
  notes. Read the final two pages of ch08 first. The author's three anaphoric
  "为什么…呢？" (Why…?) attacks on Pan Hannian/Mu Xin (s5) and his sardonic
  scare-quoting of the Huang Mulan memoir (s2) preserved as load-bearing voice.
- **Checks, all green.** parity 194=194; verify_unit numbers 0 unresolved (--noise;
  a B11 block appended: 百科全书, 一来二去, 四顾无人, 30年代, 八卦, 颠三倒四 as idiom/decade
  numerals, and the two idiomatic times 8时45分/9点3刻 whose exact value the English
  carries in words — "a quarter to nine/ten"; two real counts carried in the
  English instead of noised: 两人 "the two of them", and 8:45/9:45 preserved as
  clock times where the source gives 分); check_align median 4.55 en/han, no pair
  > 2.2x; check_content 493 name occurrences all in the paired paragraph (ch09
  added to data/content_config.json; three initial displacement flags fixed —
  named Huang Mulan in two pronoun-run paragraphs, and rendered 静安寺路底 "the
  Jing'an Temple end of Bubbling Well Road" so the 静安寺 substring resolves);
  qc_entities 0 misses; check_apparatus 0/0; anchors 27+5 all resolve; build PASS
  (9/18 chapters, 317 notes); qa_epub PASS (88 files); epubcheck 5.1.0 0/0/0/0;
  check_register --ref out/ch01_reading.md within tolerance (dialogue contraction
  1.5/1k / 4.88x is the reportage artifact — this chapter runs heavily on quoted
  memoir/confession/interview; narratorial signals on-reference: em-dash 4.7/1k,
  sent median 24, shall 0%).
- **Tail verification (rule 4 corollary).** The s9 close (the June 23 telegram in
  the Shilüe Gaoben, "这有点奇怪吗？我们觉得很正常", and the "示复密电"依然"存在" verdict)
  re-read against p0235; faithful, nothing invented. 向中（忠）发 rendered "Xiang
  Zhong[fa]" preserving the telegram's own typo-and-correction.
- **Footnotes: 27 new** (unit total 27; book 317), first-appearance, reader-model,
  verdicts in the note. The headline fact-checks: Xiang Zhongfa's identity and the
  defection question (standard accounts + the Party's own 1988 Deng Yingchao / Chen
  Yun verdict hold he confessed; the Zhang Ji'en "forgery" dissent noted;
  arrest+execution not in doubt, extent of betrayal contested); and the tail's
  "secret cable" (CORROBORATED — the author found Chiang's actual June 23 telegram
  in the Shilüe Gaoben). Plus first-appearance notes on Huang Mulan, Guan Xiangying,
  the Grand Theatre, Hua Mulan, the two great novels, Dong Biwu, Wan Xiyan, He Chang,
  Chen Zhigao, Aurora University, the North China Political Security Bureau, Moskvin
  (= Zhou's Comintern codename), the Metropole, the Yong'anli safe house, Bao Wenwei,
  He Xiangning/Liao Chengzhi, the Hanyeping Company, the Feb 7 1923 Jinghan strike,
  Luo Zhanglong, Pavel Mif, the Suguangcheng tailor-shop pun, Yang Hu, Mount Lu,
  *The Turn*/the Confession, Qin Bangxian (Bo Gu).
- **NOT re-noted (already placed earlier) — cross-referenced, not re-noted:** Gu
  Shunzhang, Zhou Enlai, Chen Yun, Kang Sheng, Pan Hannian, Chen Geng, Li Qiang,
  Xu Enzeng (ch01/ch08); Wang Ming, the Eyuwan Soviet (ch08); Xiong Shihui (ch07);
  Deng Yingchao, Tan Zhongyu (ch01); the Central Special Branch / Red Squad /
  dog-beating squad (ch01); the Zhongtong (ch04); the Mixed Court (ch03); Avenue
  Joffre (ch03/04); Jing'an Temple / Bubbling Well Road (ch07); May Thirtieth,
  Nanchang Uprising, the Nineteenth Route Army, the White Terror, Tan Sitong,
  the May Fourth Movement, Chiang Kai-shek / Wang Jingwei / Chen Duxiu / Sun
  Yat-sen / Mao Zedong / Zhang Guotao, Ren Bishi (ch01); the August 7 Conference
  (ch02); the Sixth Congress + Zvenigorod (ch01/ch06); the Fourth Plenum (ch05);
  the Mutual Aid Society / Red Aid (ch02); the All-China Federation of Trade Unions
  (ch07); Li Lisan the man (ch06/07); the Long March (ch07); the June 3 1932
  Comintern report (ch01, cited again here); *Lurk* / Yu Zecheng / Wang Cuiping
  (ch01, the note already forward-refs "invoked later in this chapter").
- **Figures: 5** (`data/figs/ch09-*.png`, hand-cropped, printed captions excluded,
  translator's captions with source-label provenance, real alt text): the Huang
  Mulan portrait (s2, p0211/folio 196); Zhou Huinian with Zhang Yuexia (s4, p0219);
  the *Bao Wenwei underground-work* manuscript facsimile (s5, p0221); the Bao
  Wenwei / Liang Zhifen 1935 wedding photo (s5, p0223); the 1927 Wuhan group photo
  with Xiang Zhongfa / Xu Baihao / Li Lisan (s6, p0226). find_figures not relied on;
  every page eyeballed. The B10 kickoff flagged only the Huang Mulan portrait; the
  other four were found by eye per CLAUDE.md.
- **Glossary: 95 new rows** (people/places/organizations), written straight into the
  sectioned ledger and re-read verified; 12 existing rows reused unchanged. `en`
  forms all ASCII (an initial curly-apostrophe slip in Hong'en/Yong'anli/Zhang
  Ji'en/Kuang Hui'an/Wan'an fired qc_entities/check_content and was fixed to
  straight `'`). 善钟路 = Rue de Sieyès flagged `gazetteer:true`+`today:"Changshu
  Road"` (joins the Street Gazetteer). Consistency canon: 徐家汇 rendered **Xujiahui**
  (pinyin) throughout, so 徐家汇天主教堂 = "the Xujiahui Cathedral" (an initial
  "Zikawei Cathedral" was corrected to match the B09 canon).

### Renderings settled this batch (also in glossary.json)
- 向忠发 = Xiang Zhongfa (alias 向仲发 rendered inline "written with a different middle
  character"); 黄慕兰 = Huang Mulan; 陈志皋 = Chen Zhigao; 探勒车行 = the Delle Motor
  Garage; 关向应 = Guan Xiangying; 宛希俨 = Wan Xiyan; 贺昌 = He Chang; 董必武 = Dong Biwu;
  鲍文蔚 = Bao Wenwei; 鲍文杰 = Bao Wenjie; 米夫 = Mif (note: Pavel Mif); 肖明 = Xiao Ming;
  王定南 = Wang Dingnan; 秦邦宪 = Qin Bangxian (Bo Gu); 杨秀贞 = Yang Xiuzhen; 杨虎 = Yang Hu.
- Places: 善钟路 = Rue de Sieyès (Changshu Road, gazetteer); 都城饭店 = the Metropole
  Hotel; 大光明 = the Grand Theatre; 庐山 = Mount Lu; 汉冶萍 = the Hanyeping Company;
  静安寺路 = Bubbling Well Road (reused); 静安寺 = Jing'an Temple (reused); 霞飞路 =
  Avenue Joffre (reused). Orgs: 中央特委 = the Central Special Work Committee;
  华北政治保卫局 = the North China Political Security Bureau (the Beiping Special Branch);
  红旗印刷所 = the Red Flag Press.
- The June 3 1932 Comintern report rendered in the CANONICAL consistency-canon form
  (Special Work Department of the Comintern Executive Committee; "Written Report on
  the State of Secret Work and Special-Service Work…") at all three of its ch09
  appearances; noted first in ch01, cross-referenced here.

## B10 — apparatus features + sweeps + spine pass; ch09 set up (2026-08-16)

Delivered the footnote-apparatus and spine work the B09 review specified; ch09
(the new-content chapter) is set up and deferred to its own batch per rule 4.

### Two new builder features (build_reading_epub.py)
- **Glossary of Recurring Terms** (the "back glossary"): a new back-matter page
  rendering every glossary row flagged `"recurring": true`, with its full note,
  so the recurring institutional/material furniture is glossed once in the text
  and carried here. 20 rows flagged (Central Special Branch, Red Squad, Zhongtong,
  Party Affairs Investigation Section, Green and Red Gangs, Municipal Council,
  French Municipal Council, shikumen, tingzijian, laohuzao, the White Terror, the
  Mixed Court, three-stripers, pidgin English, the Great World, second landlord,
  Mauser, the ten-li foreign quarter, dog-beating squad, the Racecourse).
- **Street Gazetteer**: a new back-matter table of concession streets, period
  name -> Chinese -> today's name, from place rows flagged `"gazetteer": true`
  with a `"today"` field. 24 streets (Avenue Joffre -> Huaihai Middle Road, etc.).
- Both are rendered only when their data exists, wired into spine + reader nav +
  ncx, and added to qa_epub's APPARATUS set. `render_recurring`, `render_gazetteer`,
  and the `_walk_flagged` helper are new; `.gaz` table CSS added. Do not revert.

### Footnote apparatus sweeps
- **Placement:** moved mid-phrase markers (after a bare word, the clause running
  on) to the end of the clause that holds the referent, via a conservative
  same-clause anchor extension (commas inside numbers guarded; anchors already at
  a comma/dash/sentence-end left as rule-permitted; markers before a parenthetical
  or dash-aside left in place). 29 moves ch02-ch08 + 5 ch01 survivors + 1 ch07.
  The scratchpad driver is `scratchpad/move_markers.py` (dry-run by default).
- **Density (ch01 thinned):** dropped 25 ch01 footnotes on passing-mention
  warlords/generals in the Yang Du and Chen Geng digressions (Lu Diping, Zhang
  Jingyao, Cheng Qian, Tang Shengzhi, Liao Zhongkai, Feng Yuxiang, Bai Chongxi,
  ...) and low-stakes institutional glosses (People's Daily, Cihai, Nanjing Road,
  Toa Dobun Shoin, Provisional Constitution, Hu Jintao at a commemoration, ...).
  Every dropped item keeps its glossary row; only the footnote goes. ch01
  116 -> 91 notes; density 138 -> 174 words/note (the egregious outlier fixed).
- **Density (ch07/ch08 backfilled):** +6 ch07 (the Long March, the 1911 Revolution,
  Hongkou as the Japanese quarter, the qipao, the birthday shou character, the
  Kongming/Jieting allusion), +6 ch08 (the Eyuwan Soviet, Li De = Otto Braun, the
  Nanshe and Beiping, Nanyang College, po-fu-chen-zhou, san-jiao-jiu-liu), +1 ch01
  (the War of Resistance against Japan). ch07 490 -> 377, ch08 807 -> 634 w/note.
  ch08 stays the sparsest because its references are largely noted at first
  appearance in earlier chapters and cross-referenced per protocol; padding to a
  count is against the method. Final densities: ch01 174, ch02 124, ch03 283,
  ch04 417, ch05 264, ch06 383, ch07 377, ch08 634. The ch01 outlier (was the
  dense end at 138) is corrected; the residual extremes are structural (short
  early ch02; long late ch08 whose furniture is pre-noted). 290 notes total.

### Spine-test pass
- Split four genuine multi-spine narration sentences by the spine test,
  front-loading the main clause and protecting the lists: ch08 the Chen Lifu
  propaganda sentence (purpose clause promoted) and the Dec 7 Nanchang sentence
  (buried verb "reached"; two dash-parenthetical title-strings moved to parens);
  ch01 the Zhou Enlai "come without a shadow" sentence (two "because" fronts
  promoted after the main clause); ch07 the Li Lisan uprising sentence (Liu
  Bocheng dash-bio un-nested). The remaining ~31 sentences over 90 words are
  exempt: quoted 1930s documents, quoted memoirs/interviews, the author's
  deliberate anaphora, and protected title/career lists. Worklist driver:
  `scratchpad/long_sentences.py`. Parity preserved (splits stay within paragraphs).

### ch09 set up, deferred (per rule 4)
- ch09 is a full-chapter, source-critical translation (PDF 208-235, printed
  193-220, 27 content pages, ~180 paragraphs, contested accounts of Xiang
  Zhongfa's capture and the "secret cable"). Rushing its tail in the same session
  as the apparatus work courts exactly the fabrication rule 4 forbids; B09
  deferred it for the same reason. Groundwork done this batch: pages 208-235
  rendered @300 DPI; OCR cross-check produced (confirmed too noisy on the proper
  names, so hand-transcription off the images is required, per B08); offset
  constant 15 verified at folios 195/196/197; a portrait of Huang Mulan on p0211
  identified as a figure; the 9-section structure is in book.json; the voice is
  ch08's sardonic source-criticism. The full recipe is in the HANDOFF kickoff.

### Checks
- Build PASS after every change; qa_epub PASS; epubcheck 5.1.0 0/0/0/0 on the
  final build. Consistency canon still clean.

## B09 review, round two — attribution, footnotes, spine method (2026-08-16)

Ran build (PASS, 302 notes) + qa_epub (PASS) + epubcheck (0/0/0). Fixed the ch08
attribution non sequitur in the text (front-loaded Zhang Guodong), the two
genuinely-missed round-one items (no-oil-lamp idiom, flagship inversion),
de-bundled the conjuring note and moved the pleasure-house/enforcer markers to
their list-ends, de-duplicated tingzijian, eliminated sentence-tail "besides"
book-wide, applied the Cixi spine-test split, and added the ch05 yawning/chill
TCM footnote (verified 呵欠/着凉 against the scan). Encoded the spine test, the
footnote mechanics (de-bundling, placement, gloss-boundary, density), and a
narration-contraction target in STYLE.local.md. Remaining mechanical sweeps
(marker placement book-wide, density rebalance, narration contractions, the
~100-sentence spine pass) are specified in the doc and carried in the kickoff.
Full itemization in CHANGELOG.md.

## B09 commissioner review — register rebaseline + corrections (2026-08-16)

Ran: build_reading_epub.py (PASS, 300 notes), qa_epub.py (PASS, 81 files, all
links resolve), epubcheck 5.1.0 (0 fatals / 0 errors / 0 warnings),
check_register.py --ref out/ch01_reading.md (informational; flags ch04 dialogue
as still formal, which is the whole-book register pass that remains).

Applied to ch01-ch08: the seven outright errors (all crop-verified against the
scan), the book-wide consistency sweeps, the named prose fixes, and the
apparatus additions. Full itemization in CHANGELOG.md (2026-08-16 B09 entry).
The pattern behind every note is now encoded in STYLE.local.md's new top
section, "THE REGISTER REBASELINE." Later notes were sided with over earlier
ones per the commissioner (modern-neutral default register).

NOT DONE (carried in the kickoff, governed by the frozen doc): the exhaustive
sentence-by-sentence register de-archaizing of all narration across ch01-ch08
(inversions, antique function words, narration contractions, doublets,
de-nominalization, fragment un-quoting, attribution front-loading, "and the
rest"/"and the others" variation). This is a whole-book pass one session could
not finish; the deterministic sweeps, the errors, the named examples, and the
apparatus are complete.

## Setup / Survey (this session)

- Source: image-only PDF scan, 350 pages, no text layer. `source.pdf` (73 MB).
  Front cover is an oil painting (kept as the ebook cover, `data/figs/cover.png`,
  extracted byte-identical from PDF p1). Back cover carries the blurb and
  ISBN 978-7-5155-2038-4. Publisher Gold Wall Press (金城出版社), Beijing;
  1st ed. 2021.6 (this scan is the 2022.3 6th printing). 390,000 characters,
  22 print sheets. CIP subject: CCP intelligence / security work, 1927–1935.
- Script/orientation: **simplified Chinese, horizontal** (verified by cover and
  OCR). OCR model: `chi_sim`, `--psm 6`. (chi_sim + chi_sim_vert packs installed.)
- **Page offset: constant 15 across the ENTIRE book (printed = pdf − 15).**
  Verified at every one of the 15 chapter openers plus References and Afterword
  by OCR-reading the folio band of all 335 body pages. No unpaginated plate
  inserts anywhere; no drift. This is an unusually clean scan. The preface runs
  a SEPARATE roman-numeral sequence (pdf 6–10 = i–v); the TOC is pdf 11–15.
- Front matter map: p1 front cover (painting), p2 back cover, p3 title page,
  p4 CIP/copyright, p5 epigraph (He Zhu 六州歌头, source of the title 剑吼西风),
  p6–10 preface (前言 历史不能被妖魔化), p11–15 table of contents.
- Structure: 15 chapters, two levels (chapter + numbered 一/二/… sections),
  86 sections total. Plus authorial Preface (front), and Works Cited (参考文献,
  printed 323) + Afterword (后记, printed 333) as back matter. Full structure,
  every opener's pdf_page/printed_page, in `book.json`. `pdf_end` 350,
  `printed_end` 335.
- Style contract composed: `STYLE.md` (zh + nonfiction layers), `STYLE.local.md`
  seeded. Voice target: first-rate popular narrative history for a general reader.
- Skeleton EPUB built: `out/sword-roars.epub`, full hyperlinked TOC (112 links,
  deep to every section), original cover embedded. `qa_epub.py` PASS;
  **epubcheck 5.1.0 clean (0 errors / 0 warnings)**.
- Figures: NOT yet detected. There may be inline photographs on numbered pages
  (offset is constant, so no separate plate section). Run `find_figures.py`
  per batch and eyeball for line art; the cover is handled.
- Survey delivered to the commissioner; awaiting approval of shape + batching
  before Batch 1 (Chapter One, the voice-gate frozen reference).

## B01 = Chapter One "不知掩饰，不知生存 / No Concealment, No Survival" (voice gate)

**Scope:** ch01, PDF 16–49, printed 1–34, four sections (ch01s01–s04). Done end
to end; held at the human voice / note-density / formatting gate (Step 0c).

### Pipeline
- Rendered 16–49 @300dpi. **Crop measured for THIS book:**
  `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955 --lang chi_sim --psm 6`
  (folio + running head are one TOP band; no running foot). No tesseract
  orphans (`pgrep -c tesseract` = 0 after each run). `ocr_dual.py` run for the
  name/number disagreement signal.
- **Tooling fixes this batch — DO NOT REVERT:**
  - `scripts/indents.py`: it called a non-existent `ocr_crop.folio_present` and
    assumed a *bottom* folio; this book's furniture is at the TOP. Rewrote
    `line_starts` to drop furniture bands by y-position (constants
    `FURNITURE_TOP=0.11`, `FURNITURE_BOTTOM=0.955` = the OCR crop).
  - `scripts/check_numbers.py`: added an **arabic+万 combiner** ("31万"=310,000,
    "2.6万"=26,000) that runs BEFORE the noise loop (the built-in `\d+[．.、]`
    list-marker rule was eating the "2." of "2.6万" → phantom 6万=60,000).
    Regression fixtures still green.
  - `scripts/check_content.py`: `name_map` now skips `_`-prefixed doc keys /
    non-dict sections (it choked on the glossary's `_about` string).
- **data/zh/ch01.txt is a HAND TRANSCRIPTION of the scans, not OCR output.**
  Character-level OCR was too noisy and `assemble.py`'s positional
  indent↔OCR-line zip breaks on this book's many figure pages and the
  decorative chapter opener (tesseract's line count diverges from the geometric
  band count there). The source side was read off the scans directly, one
  paragraph per line, parity-guaranteed, every name/number cross-checked
  against the dual OCR and (for hard cases) magnified crops.
  **Reproducibility caveat, raised at the gate:** `data/zh/` is gitignored
  (copyright), so the default regenerate-from-OCR path will NOT reproduce this
  file; the tracked deliverable (`out/ch01_reading.md`, apparatus, EPUB) is
  complete regardless. Decision on whether to track `data/zh` for this book is
  the commissioner's.

### Checks (all green)
- Parity 165 = 165 (`check_structure --pairs`, `verify_unit`).
- Numbers: `check_numbers --noise data/noise.txt` 0 unresolved / 165 pairs.
  `data/noise.txt` extended: event-date names read as one numeral (七一五, 五二〇,
  二七, 八七, 六一, 五四), numeral-bearing names (李立三, 张阿四, 肖阿四, 马万祺),
  decade labels (20世纪/20年代), idioms (百般, 四通八达, 万岁, 九腔十八调, 成百,
  风情万种, 海纳百川, 两手, 万恶, …). Every entry commented.
- `check_align` median 4.98 en/han, no pair > 2.2×. `check_content` 203 name
  occurrences 0 displaced. `qc_entities` 0 misses. `check_apparatus` clean.
  Builder anchor gate green (it caught 2 anchors orphaned by voice-gate edits;
  fixed).
- Tail verification: closing paragraphs of every section re-read against the
  scan. Crop-verified: Red Squad roster (谭忠余/张阿莲/张文虎/张文龙 p20), the
  南昌决裂 reading (as printed; footnoted), casualty figures 31万/2.6万 (p31),
  addresses 22号/679号.

### Apparatus
- **115 footnotes** (`notes.json`): first the 52-note base (figures, events,
  institutions, idioms, quotations a non-specialist needs, first-appearance
  anchored, fact-check verdicts where checkable: the 310,000 purge-deaths as the
  Party's own Sixth-Congress reckoning; Wakeman = 魏斐德; the Latin maxim = the
  chapter-title source); then **+63 notes for the commissioner's density
  request** (`data/ch01_notes2.json`, merged), closing every place / reference /
  minor-figure gap a reader with no China background would hit. The trigger was
  explicit: the six Shanghai pleasure-houses ("Tower-Beyond-the-Tower … the
  Great World") of which the reader knew two, now all glossed in one note. The
  new batch sweeps: the venues and the amusement-arcade world; classical
  conjuring (baixi, the Seven Sages); the department stores and Shen Bao; the
  Green Gang; the three Shanghai workers' uprisings; the concession/settlement
  geography that the whole book turns on; the warlords and revolutionaries named
  in passing (Lu Diping, Zhang Jingyao, Cheng Qian, Tang Shengzhi, Zhang Zuolin,
  Yuan Shikai, Li Yuanhong, Feng Yuxiang, Bai Chongxi …); the Party congresses
  (Third, Fifth, Sixth) and bodies (Youth League, Comintern, CPPCC/NPC, Southern
  Bureau); the 1927 Politburo roster; institutions (Tongmenghui, Tōa Dōbun
  Shoin, Naigai, Cihai, People's Daily); the White-Terror enforcers and the
  White/Soviet-areas vocabulary; allusions (Lord Chunshen, Zhuge Liang, Patrick
  Henry); and the shikumen/tingzijian/xiaokai material culture. All 63 anchors
  verified unique and non-nesting against the 52 already placed; numeric refs
  only; `check_apparatus` clean, builder anchor gate green, `qa_epub` PASS,
  epubcheck 0/0.
- **12 figures** (`figures.json`) with real alt text; `find_figures` MISSED the
  Shen Bao ad-clippings (dense newsprint) and the org chart (line art) — cropped
  by hand (`data/figs/ch01-*.png`). The faded photo behind the p16 chapter title
  is treated as design furniture, NOT a captioned figure.
- Glossary: principal cast + recurring names/orgs/terms; `authority.json` to be
  updated on completion.

### Voice gate (Step 0c) — blind-critique loop
- Round 1 (context-blind reader): ~40 findings; applied 33, kept the deliberate
  正面/背面 parallelism and the Mao/Lu Xun/couplet quotations (load-bearing, the
  blind reader couldn't see them). Six RULE/WHY/FIX/CHECK classes folded into
  `STYLE.local.md`.
- Round 2: opened "polished, high-accomplishment… mostly real English"; ~44
  further fixes (garbled-logic, remaining calques, doubled synonyms, purple);
  apparatus "read clean." Two more rules added to `STYLE.local.md`.
- Round 3: convergence check (running / done — see HANDOFF).
- On approval this chapter is the FROZEN register reference
  (`check_register.py --ref out/ch01_reading.md`).

### Setup-report note
- `tests/run_tests.py`: one FAIL, "hook stands down on template stub" — benign
  (the survey already put a real kickoff in HANDOFF.md, so the Stop hook
  correctly ENFORCES rather than standing down). Not a regression.

### NOT re-noted (already placed) — for later batches, cross-reference don't re-note
- Gu Shunzhang, Chen Geng, Zhou Enlai, the Central Special Branch, the Red
  Squad, Chiang Kai-shek, Yang Du, Pan Hannian, Li Dazhao, Du Yuesheng, the
  Whampoa Academy, the May Thirtieth Massacre, the Great Revolution / party
  purge, the "ten years of turmoil", Wakeman, Zhang Guotao, Xu Enzeng, Dong
  Jianwu, Qu Qiubai, Li Qiang, Mei Baoji, Mei Gongbin, the Nineteenth Route
  Army, Song Qingling — all first-noted in ch01.

## B02 = Chapter Two "清者自清，浊者自浊 / The Clean Stay Clean, the Foul Stay Foul"

**Scope:** ch02, PDF 50-59, printed 35-44, two sections (ch02s01 一、英雄阳刚 /
"A Hero's Mettle"; ch02s02 二、流氓无产者 / "The Lumpen Proletariat"). Done end
to end. 56 body paragraphs.

### Pipeline
- Rendered 50-59 @300dpi. Crop as B01:
  `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955 --lang chi_sim --psm 6`.
  `ocr_crop` + `ocr_dual` run; `pgrep -c tesseract` = 0 after each.
- **Folios verified off the scan at every page:** pdf 50 = chapter opener
  (decorative, faded photo behind the title, NO printed folio = printed 35);
  pdf 52-58 read 037-043; **offset holds at a constant 15, no drift** (matches
  book.json / B01).
- **data/zh/ch02.txt is a HAND TRANSCRIPTION** off the scans (same reason as
  B01: OCR too noisy, assemble misaligns on the figure-heavy pages 52-53 and
  the opener). Parity-guaranteed, one paragraph per line, every name/number
  cross-checked against dual OCR and magnified crops. (data/zh gitignored;
  reproducibility caveat as B01.)

### Crop-verified readings (names/numbers)
- **约翰·拜伦、罗伯特·帕克 = John Byron and Robert Pack** (NOT "Baolun/Park"):
  authors of *The Claws of the Dragon: Kang Sheng* (1992; Chinese tr. 1998).
  The crop caught 拜 (Byron) mis-first-read as 豹. Western scholars, own names.
- **史曜宾 (Shi Yaobin) and 史砚芬 (Shi Yanfen) are TWO DIFFERENT people**,
  both in the source: Shi Yaobin = the Yixing county-committee secretary
  (p51); Shi Yanfen = uprising vice-commander and the martyr executed at
  Yuhuatai 1928 (p52-53). Rendered as printed; footnoted the distinction.
- Verified: 宗孟平/宗益寿/宗颖/吴丹枫/宗文斌, 匡亚明/洁玉/匡世, 荆溪, 史曜宾,
  李旸谷, 宗盘林, 宗道章, 万益, 段炎华, 蒋三大, 严朴, 后塍, 英举, 赵和, 宗益茂,
  官林, 李凯, 罗青长, 薛岳, 蔡孟坚, 杨之华/杏花/文君/杜宁. Numbers:
  6支部/39党员, 502工会/82万会员/3000党员, 五十多万, 12时, 十三村镇 all crop-clean.
- **杜宁 (Du Ning) is Yang Zhihua's pen name** (the p58 citation uses it);
  footnoted so the reader does not take it for a separate authority.

### Checks (all green)
- Parity 56 = 56 (`check_structure --pairs`, `verify_unit`).
- Numbers: `check_numbers --noise data/noise.txt` 0 unresolved / 56 pairs.
  `data/noise.txt` extended (commented): idiom-numerals 十足 / 万能 / 两肋;
  the approximate quantity 五十多万 (= "over 500,000", rendered in full, listed
  so the generic 十多 rule does not fragment it and orphan 万=10000); and the
  name-numerals 万益 (surname 万) and 蒋三大 (三). 中午12时 rendered "twelve noon"
  so the 12 is carried.
- `check_align` median 5.10 en/han, no pair > 2.2x. `check_content` 45 name
  occurrences, all in the paired paragraph. `qc_entities` 0 misses (incl. the
  14 new glossary rows). `check_apparatus` clean.
- **Register vs frozen ch01** (`check_register --ref out/ch01_reading.md`):
  within tolerance. Dialogue-contraction metric QUIET (this chapter is quoted
  meeting-records + citations, little scene dialogue) — judged on the
  narratorial signals (em-dash 8.7/1k vs ref 8.2; rhythm CV 0.59 vs 0.67;
  sent median 23), all in range.
- Tail verification: closing paragraphs (p58, the 顾顺章 blood-and-iron coda)
  re-read against the scan; faithful, nothing invented.
- Build: cumulative EPUB rebuilt (2/18 chapters, 143 notes). `qa_epub` PASS
  (49 files, all links resolve). **epubcheck 5.1.0 clean (0/0).**

### Apparatus
- **28 footnotes** (`data/ch02_apparatus.json` -> notes.json). Coverage:
  the chapter-title proverb; the Aug 7 Conference and Autumn Harvest Uprising;
  Jiangnan geography; the 节孝祠 shrine; Shi Yanfen (martyr + the Shi Yaobin
  distinction); the Relief Society (济难会 / Red Aid); Chen Yun; the KMT 自首
  surrender policy; the Mencius three-cannots and the "受屈…知君子" maxim; Mao's
  1945 "On Coalition Government" line and his 1925 class-analysis essay; the
  five Shanghai leaders (Chen Duxiu, Peng Shuzhi, Luo Yinong, Zhao Shiyan,
  Wang Shouhua) with fates; the Shanghai Provisional Municipal Government; the
  Northern Expedition; "C.P."; the Shanghai General Labor Union; the lumpen-
  proletariat concept; the secret societies (Triads/Gelaohui/Big Sword/
  Zailihui/Green Gang); Nanyang Brothers Tobacco; Byron & Pack; Cai Mengjian;
  Yang Zhihua/Du Ning; Xue Yue; the Green Gang initiation hall. Fact-checks
  corroborated against Party and Western sources (Shi Yanfen, the Byron/Pack
  book, Cai Mengjian's 1931 capture of Gu, the Provisional Municipal Govt).
- **5 figures** (`figures.json`, hand-cropped from the scans, real alt text):
  portraits of Zong Mengping, Kuang Yaming, Yan Pu (p52) and Chen Yun (p53),
  and the group photo of Gu Shunzhang at the Provisional Municipal Government
  (p55). `find_figures` not relied on. The full-page faded painting on **pdf 59**
  (no folio, no caption) is treated as design furniture, NOT a captioned
  figure (as with the ch01 chapter-title photo).
- **14 new glossary rows** (people: Zong Mengping, Kuang Yaming, Shi Yanfen,
  Chen Yun, Chen Duxiu, Peng Shuzhi, Luo Yinong, Zhao Shiyan, Wang Shouhua,
  Cai Mengjian, Xue Yue, Yang Zhihua; orgs: Nanyang Brothers Tobacco, Shanghai
  General Labor Union). All `attested`. (apparatus_merge places rows at top
  level; MOVED into people/organizations sections by hand, else the builder's
  render_glossary chokes on a flat row — noted for next batch.)

### NOT re-noted (already placed in ch01) — cross-referenced, not re-noted
- Gu Shunzhang, Zhou Enlai, the Central Special Branch, the Red Squad, the
  "dog-beating"/"beating the dogs" usage, the Third/Action Section, Chiang
  Kai-shek, the May Thirtieth, the three Shanghai workers' uprisings, the
  soviet/White-areas vocabulary, Qu Qiubai, Du Yuesheng, the Green Gang
  (青帮; the initiation-hall custom is newly noted), Wakeman, Zhang Guotao,
  Xu Enzeng, the April 12 coup / party purge, the Comintern.

### Tooling notes (do not revert)
- `data/noise.txt`: see the ch02 block appended at the end (idiom/name/quantity
  numerals). Every entry commented; longest-literal-first respected.
- `apparatus_merge.py` writes glossary rows at the JSON top level; they must be
  moved into the correct section (people/organizations/...) or the builder
  fails at render_glossary. Figure `file` fields must be BASENAMES only
  (builder prepends data/figs and images/); a "data/figs/..." prefix breaks
  qa_epub with a missing-image path.
- `check_structure.py --config` cannot run a whole-book parity pass on a fresh
  checkout because data/zh/ch01.txt is gitignored/absent; per-unit
  `--pairs data/zh/ch02.txt out/ch02_reading.md` was run instead (OK).

## B03 = Chapter Three "谁是犹大 / Who Is Judas" (ch03)

- **Scope:** PDF 60-81, printed 45-66. Seven sections ch03s01-s07. Offset held
  at a constant 15 (folios 045-066 read off the scan at every opener; no drift).
  The chapter turns from the moral contrast of ch02 to the hunt for a traitor:
  the betrayal, arrest, and execution of Luo Yinong (罗亦农) in April 1928, and
  the Special Branch reprisal on the informers He Zhihua (贺稚华) and her husband
  He Jiaxing (何家兴).
- **Source recovery.** OCR (chi_sim, psm 6, crop 0.06/0.95/0.11/0.955) was noisy
  on the proper names as expected (夏禹奎 came out four different ways), so
  `data/zh/ch03.txt` was hand-transcribed from the page images and cross-checked
  against the dual-OCR read, exactly as for ch01-ch02. Parity is exact: **146
  source paragraphs = 146 translation paragraphs** (7 `###` section headings).
- **Translation:** `out/ch03_reading.md`, one paragraph per source line. Voice
  carried over from the end of ch02 (read first). Real scene dialogue this
  chapter (Luo/Li courtship, the He couple, quoted Deng Xiaoping); differentiated
  per the voice sheets in HANDOFF. The set-off Peng Shuzhi memoir block is a
  `{v}` vignette (one source paragraph, parity-locked).
- **Checks, all green:**
  - parity 146=146 (`check_structure --pairs`).
  - numbers: `check_numbers --noise` 0 unresolved. Caught one real error mid-draft
    (三千或五万 rendered "three or five thousand"; fixed to "three thousand or
    fifty thousand") and the dropped inline citation years, now all restored in
    the ch02 "(Author, YEAR)" style. Also carried 八人 "eight", 二楼 "second-floor",
    两家 "two households", 上海 "Shanghai" where first drafted loose.
  - align OK (median 4.46 en/han, no pair strays > 2.2x).
  - content displacement OK (370 name occurrences, all in the paired paragraph).
  - entities: `qc_entities` 0 misses (Li Zheshi named once in two grief
    paragraphs where pronouns had carried her; He Jiaxing named in the 何家兴夫妇
    paragraph).
  - register vs the FROZEN ch01 reference: within tolerance. The dialogue
    contraction rate is 6.0/1k against ch01's 0.3/1k (20x), but this is the
    expected signal, not drift: ch01 is nearly dialogue-free and ch03 carries
    real scene dialogue (the register-drift caveat for reportage). Narratorial
    signals (em-dash 0.0/1k, rhythm CV 0.68 vs 0.67, sentence median 20) sit on
    the reference. Metric noted as expected, not a flag.
  - `check_apparatus` 0/0; qa_epub PASS (176 refs/bodies/backlinks); epubcheck
    5.1.0 clean (0 fatals / 0 errors / 0 warnings).
- **Footnotes: 33 new** (unit total 33). Coverage swept across the four domains:
  people first-introduced (Luo Yinong, Zheng Chaolin, Zhu De, Zhu Min, Deng
  Xiaoping, Kang Sheng, Zhang Zuolin, Qian Dajun, Yang Dengying/Bao Junfu, Hu
  Jintao, Chen Yannian, Xia Minghan); institutions and places (KUTV, Longhua,
  the Great World, Hardoon Garden, the Mixed Court, the Green and Red Gangs, the
  White Terror, Bolshevik, Bubbling Well Road); material culture and allusion
  (Rue Bourgeat / concession streets, comprador, chaibaidang, Xiang embroidery,
  the Bai Juyi and Li Yu allusions, Lu Xun's Wandering); and the source-critical
  notes (the redacted "奉蒋××令" reproduced as printed; the 夏明翰/夏明瀚 misprint;
  the 贺稚华/贺治华 name variant against Zhu De's letter; the Monte Cristo maxim;
  the unresolved manner of He Zhihua's death, left as the author leaves it).
- **FACT-CHECK / interested-witness.** He Zhihua = the historical 贺治华, Zhu De's
  wife and mother of Zhu Min: corroborated, and footnoted at the Zhu De note.
  Luo Yinong's execution at Longhua (21 April 1928): corroborated. The identity
  of the traitor is contested in the sources the author himself quotes (Zheng
  Chaolin's letter version vs the informer-woman version vs the "who profits"
  reading); the translation renders all faithfully and the notes flag the
  disagreement rather than resolving it. Kang Sheng leading the killing squad:
  uncorroborated, one version only, footnoted as such.
- **Figures: 4** (basenames in `figures.json`, real alt text, translator's
  captions with source-label provenance stated):
  - `ch03-luo-yinong.png`, `ch03-li-zheshi.png` (paired portraits, pdf 63).
  - `ch03-he-zhihua-europe.png` (group photo, He Zhihua front row right-2, pdf 72).
  - `ch03-shanghai-map.png` (old street map locating 178 Rue Bourgeat, pdf 77).
  - The faded chapter-opener montage on pdf 60 (no folio, no caption) is treated
    as design furniture, NOT a captioned figure (as with ch01/ch02 openers).
    `find_figures` not relied on; every page eyeballed.
- **59 new glossary rows** (people, organizations, places, terms), added
  DIRECTLY into the correct sections by a one-shot script (re-read verified),
  not via apparatus_merge's flat top-level write. All `attested`/`decided`.
  李维汉 already present (reused). Key: 李哲时 = Li Zheshi (= 李文宜 Li Wenyi),
  贺稚华 = He Zhihua, 何家兴 = He Jiaxing, 朱德 = Zhu De, 郑超麟 = Zheng Chaolin,
  杨登瀛/鲍君甫 = Yang Dengying/Bao Junfu (the ch04 double agent).

### NOT re-noted (already placed in ch01/ch02) — cross-referenced, not re-noted
- The August 7 (八七) Conference (noted ch02), the Nanchang Uprising (ch01), the
  Green Gang (ch01; the Red Gang is folded into the new Green-and-Red note),
  the tingzijian (ch01), Chiang Kai-shek / Wang Jingwei (ch01), Zhang Tailei
  (ch01; his widow Wang Yizhi is glossed only), the Special Branch / Red Squad /
  "beating the dogs" (ch01), Gu Shunzhang / Chen Geng / Zhou Enlai / Qu Qiubai /
  Chen Duxiu (ch01-ch02).

### Tooling notes (do not revert)
- `data/noise.txt`: ch03 block appended (四川 Sichuan; 三教街 Sanjiao Street;
  化整为零; 一百二十四; 推三阻四; 万籁; 万般; 第二天). Every entry commented;
  longest-literal-first respected. These are place-names and idioms carrying a
  numeral that is not a quantity; no real dropped number was ever noised.
- `data/content_config.json` extended to include ch03 so the displacement check
  covers it (ch01+ch02+ch03).
- Glossary discipline: apparatus_merge STILL writes glossary rows at the JSON
  top level; this batch bypassed that by adding rows straight into the sections
  with a re-read-verified one-shot (deleted after use). Either path is fine;
  just never leave a flat top-level row, which breaks render_glossary.

## B04 = Chapter Four "喋血霞飞路 / Bloodshed on Avenue Joffre" (ch04)

- **Scope:** PDF 82-107, printed 67-92. Seven sections ch04s01-s07. Offset held
  at a constant 15 (folios 068-091 read off the scan at every opener; no drift).
  The double-agent chapter that ch03's ending set up: the arrests at Jingyuanli
  "as if foreknown" (Peng Pai, Yang Yin, Yan Changyi, Xing Shizhen + Zhang
  Jichun, 24 Aug 1929; four shot at Longhua 30 Aug), Yang Dengying/Bao Junfu the
  double agent run by Chen Geng, the failed Fenglin Bridge rescue, Bai Xin's
  betrayal exposed, and the Red Squad's killing of Bai Xin on Avenue Joffre
  (11 Nov 1929). Closes on Zhou Enlai sheltering Yang Dengying in Qincheng
  Prison during the Cultural Revolution.
- **Source recovery.** `data/zh/ch04.txt` hand-transcribed off the page images
  (OCR too noisy on the proper names, as before), cross-checked against the
  dual-OCR read and magnified crops. Parity is exact: **131 source paragraphs =
  131 translation paragraphs** (chapter title + 7 `###` section headings).
- **Translation:** `out/ch04_reading.md`, one paragraph per source line. Voice
  carried from the end of ch03 (read first). Section 7 carries a run of set-off
  block quotations and the **李强日记 (Li Qiang's Diary) 1968-69 entries**, all
  marked `{v}` vignettes (date + entry combined one-per-line; the source's
  abridging "……" kept as its own `{v} ...` line). The White-Russian-café
  set-piece (s03) is rendered at elevation as the author's own descriptive prose.
- **Checks, all green:**
  - parity 131=131 (`check_structure --pairs`, `verify_unit`).
  - numbers: `check_numbers --noise` 0 unresolved. Caught one real slip
    (五位负责人 first drafted "the other four leaders"; fixed to "the five
    leaders, Peng Pai among them"). noise.txt extended with ch04 proper-name
    numerals (百禄里, 五洲, 三民, 三轮车 = Popov's "Tricycle", 八仙桥).
  - align median 4.85 en/han, no pair > 2.2x. content displacement 174 name
    occurrences, all in the paired paragraph (content_config extended to ch04).
  - entities: `qc_entities` 0 misses (top: 杨登瀛 x60, 周恩来 x58, 陈赓 x27,
    董健吾 x14, 鲍君甫 x12).
  - register vs FROZEN ch01: the dialogue-contraction metric is QUIET/flagged
    "STILTED" (0.0/1k), the expected reportage signal for a chapter that is
    almost entirely quoted documents (Zhou Enlai's 1930 proclamation, the
    Comintern report, a memoir/biography stack, and the diary) with only a
    handful of scene-dialogue lines (the Bai Xin/Ke Lin exchange). Judged on the
    narratorial signals: rhythm CV 0.68 vs ref 0.67, sentence median 23, em-dash
    0.9/1k (low, consistent with ch03's 0.0) — all in range. Not real drift.
  - `check_apparatus` 0/0; qa_epub PASS (200 refs/bodies/backlinks); **epubcheck
    5.1.0 clean (0 fatals / 0 errors / 0 warnings).**
  - tail verification: the s07 closing paragraphs re-read against p0106 (printed
    091); faithful, nothing invented.
- **Footnotes: 24 new** (unit total 24). Coverage across the four domains:
  people first-introduced (Peng Pai, Yang Yin, Yan Changyi+Xing Shizhen, Zhang
  Jichun, Bai Xin, An E, Ke Lin, Huang Jinrong, Luo Qingchang; Dong Jianwu
  supplemented from ch01 with the Red-Pastor/Mao's-sons material); institutions
  and places (the Zhongtong lineage via the two Chens, Sun Yat-sen Univ. Moscow
  vs KUTV, St. Peter's vs Grace Church, Avenue Joffre, Qincheng, the Republican
  Daily, the Guangzhou Uprising); texture and reference (Lu Xun's censorship
  opening and "opening a skylight", the North China Daily News, the White
  Russian émigrés, the Internationale, Dusko Popov = "Tricycle"); and one
  source-critical note (the 12-vs-1015 Jingyuanli house-number discrepancy, as
  printed). Fact-checks corroborated against Wikipedia/Baidu/academic/official
  sources (the Peng-Yang-Yan-Xing arrest and execution and Bai Xin's betrayal;
  Popov = Tricycle, MI5/MI6, Bond inspiration — cited to Wikipedia/UK National
  Archives, NOT the Grokipedia hit; An E; Dong Jianwu; Ke Lin).
- **Figures: 10** (basenames in `figures.json`, real alt text, translator's
  captions with source-label provenance stated): four martyr portraits
  (`ch04-peng-pai.png`, `ch04-yang-yin.png`, `ch04-yan-changyi.png`,
  `ch04-xing-shizhen.png`, pdf 85-86), `ch04-yang-dengying.png` (pdf 87),
  `ch04-an-e.png` (pdf 89), `ch04-garrison.png` (the Songhu Garrison Command,
  pdf 92), `ch04-shanghai-map.png` (old street map locating Fenglin Bridge,
  pdf 93 — a full-page figure), `ch04-red-flag-daily.png` (Zhou Enlai's memorial
  front page, pdf 95), `ch04-yang-family.png` (1956 family photo, pdf 102). The
  faded full-page painting on pdf 107 (no folio, no caption) is design
  furniture, NOT a captioned figure (as with the ch01-ch03 openers/closers).
- **62 new glossary rows** (people, organizations, places, terms), added
  directly into the correct sections by a re-read-verified script (not via
  apparatus_merge's flat top-level write). Key: 彭湃=Peng Pai, 杨殷=Yang Yin,
  白鑫=Bai Xin, 安娥=An E, 柯麟=Ke Lin, 董健吾=Dong Jianwu (already present),
  中统=the Zhongtong, 霞飞路=Avenue Joffre, 秦城监狱=Qincheng Prison.

### Source oddities logged (per the typo policy)
- **p0089 (printed 074) prints "白行车" for "自行车" (bicycle).** An evident
  imprint typo (白 for 自); rendered to plain sense "a bicycle." Listed here,
  not footnoted (below the annotation threshold).
- The 静安区委党史研究室 (2016) quote gives "经远里1015号" where every other
  source gives "12号"; both reproduced as printed and the discrepancy footnoted.

### Tooling notes (do not revert)
- **Builder alt-attribute escaping (FIXED this batch):** `build_reading_epub.py`
  emitted `alt="%s"` through `esc()` (which is `html.escape(quote=False)`), so a
  double quote inside alt text (`'Wuhing Road'` was first written with real "")
  produced malformed XHTML and qa_epub/epubcheck reported the WHOLE chapter's
  ids as undefined. Changed that one call to `html.escape(..., quote=True)`.
  Keep it. Lesson: an alt string with a literal `"` is now safe, but prefer
  single quotes in alt text anyway.
- `data/noise.txt`: ch04 block appended (百禄里, 五洲, 三民, 三轮车, 八仙桥),
  every entry commented, longest-literal-first respected. All are proper-name
  numerals rendered romanized; none masks a real dropped quantity.
- `data/content_config.json` extended to include ch04.

### NOT re-noted (already placed in ch01-ch03) — cross-referenced, not re-noted
- The Central Special Branch / Red Squad / "beating the dogs" (ch01); Zhou Enlai,
  Chen Geng, Gu Shunzhang, Xu Enzeng, Kang Sheng (ch01/ch03); the Whampoa Academy
  (ch01); the Green Gang (ch01); Longhua (ch03); the Comintern / KUTV (ch01/ch03);
  the April 12 coup / Great Revolution / White Terror (ch01/ch03); Chiang
  Kai-shek / the Kuomintang (ch01); Nanchang Uprising (ch01); "Judas" (ch03
  title); Yang Dengying/Bao Junfu & Chen Yangshan (ch03); Li Qiang, Dong Jianwu
  (ch01, supplemented here); the tingzijian / shikumen (ch01).

## B05 = Chapter Five "真金库，假夫妻 / A Real Vault, a False Marriage" (ch05)

- **Scope:** PDF 108-123, printed 93-108. Three sections ch05s01-s03 (openers at
  PDF 109/115/120, folios 094/100/105). Offset held at a constant 15 (folios
  094-108 read off the scan; no drift, as promised through ch04). The chapter
  turns from the traitor-hunt to the Party's own machinery: how Xiong Jinding
  and Zhu Duanshou set up and guarded the Yunnan Road safe house (the "Fuxing"
  firm), the false marriage that covered it, and the couple's whole life
  together, closing on their deaths on the same calendar day 21 years apart.
- **Source recovery.** `data/zh/ch05.txt` hand-transcribed off the page images
  (OCR too noisy on the proper names, as before), cross-checked against the
  dual-OCR read and magnified crops of every poem, name, and number. Parity is
  exact: **66 source paragraphs = 66 translation paragraphs** (chapter title +
  3 `###` section headings; the source's chapter line marked `###` so the parity
  filter treats it like the section heads). Zhou Enlai's 1966 statement and Zhu
  Duanshou's autobiography passage are set off `{v}`; the statement's signature
  and date are their own `{v}` lines.
- **Translation:** `out/ch05_reading.md`, one paragraph per source line. Voice
  carried from the end of ch04 (read first). This is a dialogue-rich chapter
  (Zhu Duanshou's spirited country-girl speech; Zhou Enlai warm and big-brotherly
  here, distinct from his martyr-proclamation register), with a stack of quoted
  memoirs and biographies the author weighs against one another, and seven
  classical or old-style poems rendered at elevation (Xiong's couplets, Zhu's
  reply after Yuan Mei, the Wang Bo and Bai Juyi lines Xiong taught her, his
  deathbed couplet to Zhou, Zhu's ten-line inscription, and Xiong's closing
  "white hair, young companion" quatrain).
- **Checks, all green:**
  - parity 66=66 (`check_structure --pairs`, `verify_unit`).
  - numbers: `check_numbers --noise` 0 unresolved. Two real English fixes
    (两同志 "the two comrades", carried in both the testimonial and its re-quote;
    30多岁 rendered "thirty-odd years"). noise.txt extended with ch05 romanized
    proper-name numerals (四马路/三马路/朱葆三路/熊笑三, 零星 in Yuan Mei's line) and
    two approximate 几-quantities (几十万 "several hundred thousand", 几千里
    "thousands of li") that the digit parser cannot match in idiomatic English;
    the English carries the magnitude, so noising the source token cannot mask a
    real drop. Every entry commented, longest-literal-first.
  - align median 4.79 en/han; one expected short-line outlier (the "{v} January
    1, 1966" signature, 2.11x). content displacement 264 name occurrences, all
    in the paired paragraph (content_config extended to ch05).
  - entities: `qc_entities` 0 misses (top: 朱端绶 x75, 熊瑾玎 x66, 周恩来 x58,
    上海 x30, 熊畅苏 x22). Two initial misses fixed by naming Zhu Duanshou where
    the source names her (not a pronoun) and restoring the dropped book title
    《熊瑾玎》.
  - register vs FROZEN ch01: within tolerance. The dialogue-contraction metric
    reads HIGH here (13.0/1k vs ref 0.3), the OPPOSITE of ch04's quiet reportage
    signal and exactly right for a dialogue-heavy chapter; judged on the
    narratorial signals, which track the reference (em-dash 5.5/1k vs 8.2,
    rhythm CV 0.68 vs 0.67, sentence median 21).
  - `check_apparatus` 0/0; qa_epub PASS (227 refs/bodies/backlinks); **epubcheck
    5.1.0 clean (0 fatals / 0 errors / 0 warnings).** style layers FRESH.
  - tail verification: the s03 closing paragraphs (熊畅苏's three-mentors speech,
    Zhu's inscribed poem, Deng Yingchao's "Hold on, little sister!", and Xiong's
    closing quatrain) re-read against p0122-0123 (printed 107-108); the poems
    crop-verified; faithful, nothing invented.
- **Footnotes: 27 new** (unit total 27). Coverage across the four domains:
  material culture (the numbered "horse roads" / Sima Road, the Racecourse,
  laohuzao [rendered per ch03's inline gloss, NOT re-noted], the shikumen
  chamber-pot custom, alum-water secret writing, braised lion's-head meatballs,
  the Ten-Li Foreign Settlement); social/institutional (the "solid shop to stand
  surety" rental custom, Branch Life and the 直支/植枝 homophone codename, the
  Fourth Plenum dating); people (Xiong Jinding himself, Nan Hanchen, Xiong
  Xiaosan, Wu Jieping, Yuan Mei, Wang Bo, Bai Juyi); tradecraft and texture (the
  "frisking"/抄靶子 slang, Wuhao as Zhou Enlai's alias and the 1932 forged notice,
  the fish-and-water figure, ci tune-titles); and history/reference (the Gu
  Shunzhang defection that closed the house, cross-ref to Chapter Three's
  Luo Yinong betrayal, West Hunan-Hubei/Honghu, the Ma Day Incident, the Zhou
  Residence on Rue Massenet, the Gang of Four). Fact-checks corroborated against
  Wikipedia/Baidu/academic sources; the author's own skeptical source-criticism
  (debunking the romantic "found the house in the rain" story) preserved.
- **Figures: 5** (`data/figs/ch05-*.png`), all hand-cropped, printed captions
  excluded and re-captioned by the translator with the source-label provenance
  line, each with real alt text: the 447 Yunnan Road storefront (s01), Gong
  Yinbing's portrait (s01), the Xiong-Zhu couple portrait (s01), a detail of
  Zhou Enlai's 1966 handwritten statement (s01), and the Yan'an-era family
  photograph (s03). find_figures was not relied on; every page eyeballed. No
  line-art diagrams in this chapter; the faded portrait behind the chapter
  divider (p0108) is design furniture, not a captioned figure.
- **Glossary: 75 rows added** (42 people, 20 places, 5 organizations, 8 terms),
  written straight into the sectioned ledger (NOT via apparatus_merge, per the
  flat-row gotcha) and re-read verified. 老虎灶/石库门/亭子间/蒲石路/中央军委 reused
  unchanged from earlier batches; 老虎灶 kept as the decided "laohuzao" (I first
  drafted "tiger-stove", caught by qc_entities against the glossary decision and
  the ch03 first-use, and corrected).

### Renderings settled this batch (also in glossary.json)
- 熊瑾玎=Xiong Jinding, 朱端绶=Zhu Duanshou, 熊畅苏=Xiong Changsu, 龚饮冰=Gong
  Yinbing, 熊笑三=Xiong Xiaosan (Nationalist general), 南汉宸=Nan Hanchen; the
  descendants and biographers by standard pinyin.
- 福兴字号=the "Fuxing" firm; 云南路=Yunnan Road (today Yunnan Middle Road);
  天蟾舞台=Tianchan Stage; 生黎医院=Shengli Hospital; 跑马厅=the Racecourse;
  湘鄂西=West Hunan-Hubei; 洪湖=Honghu; 陶乐春=Taolechun.
- Concession/lane names: 巨籁达路=Rue Ratard, 马斯南路=Rue Massenet,
  慎成里=Shenchengli, 泰辰里=Taichenli, 眉寿里=Meishouli (里-compounds as -li per
  ch04's Jingyuanli). **康悌路 kept as pinyin "Kangti Road"** (French name
  uncertain; first drafted as "Rue du Consulat", corrected to pinyin per the
  book's uncertain-French rule).
- Terms: 抄靶子=frisking (chao bazi), 明矾水=alum water, 红烧狮子头=braised
  lion's-head meatballs, 伍豪=Wuhao, 十里洋场=the Ten-Li Foreign Settlement,
  四人帮=the Gang of Four, 词牌=tune-title.

### NOT re-noted (already placed earlier) — cross-referenced, not re-noted
- The Central Special Branch / Red Squad (ch01); Gu Shunzhang (ch01, the 1931
  defection named here and pointed forward); Luo Yinong and the He Jiaxing / He
  Zhihua betrayal (ch03, cross-ref in the surety note); the tingzijian and
  shikumen (ch01); laohuzao (ch03, inline gloss); the Sixth Congress (ch01); the
  August 7 Conference (ch02); He Long (ch01); the Huaihai Campaign (ch04); Avenue
  Joffre / the concessions (ch03/ch04); the Cultural Revolution / "ten years of
  turmoil" (ch01/ch03/ch04).

## B06 = Chapter Six "不是我，是风 / It Was Not Me, It Was the Wind" (ch06)

- **Scope.** PDF 124-149 (printed 109-134). A large chapter: ten sections
  ch06s01-s10, 26 pages. The chapter divider (p0124) and the full-bleed washed
  illustration on p0149 are design furniture, not captioned figures. The body
  text runs PDF 125-148; p0149 (printed 134) is a decorative plate only.
- **Offset held constant 15** (printed = pdf - 15). Folios read off the scan at
  every opener; no plate drift.
- **Source.** data/zh/ch06.txt hand-transcribed from the scans, one paragraph
  per line, chapter title and section heads as ###. 165 paragraphs. Three
  displayed block quotations carry the {v} marker in BOTH zh and en (the Chen
  Tan 1992 torture testimony, the Chen Tan 1992 morgue testimony, and the Guan
  Wenwei 1985 "three types of penitent"). All other quotations are inline.
- **Crop-verified names/numbers** (dual-OCR disagreement plus by-eye magnified
  crops): 谭献犹 Tan Xianyou, 刘希吾 Liu Xiwu; the 16-trainee roster (麦建屏,
  何世大, 冯一平, 王西雄, 高枕松 etc.); 任玑 Ren Ji (Su Gangda's real name);
  袁良 Yuan Liang; the Shen Bao list variants 冯敬三 / 何世夫; the Jiangyin
  martyrs 陈叔璇, 陈维吾, 茅学勤; the full Suzhou Reformatory roll-call on
  p0147 (彭康 子劼, 曹荻秋 张云卿, 李祚利, 章汉夫 谢启泰, 于寿康 刘松山, 夏之栩,
  张仃, 凌子风). The obscure locality 亳阳 (Su Gangda's peasant-rising site near
  Yixing) reads 亳阳 on the scan; romanized Boyang, glossed provisional.
- **Two source-internal name discrepancies rendered as printed and footnoted:**
  the school roster's 冯一平 / 何世大 appear in the next section's Shen Bao
  report as 冯敬三 / 何世夫. The divergence is in the sources (the paper worked
  from blotter names, themselves partly the prisoners' false confessions); left
  as printed with a note.
- **Caption/body road discrepancy:** the p0136 photo caption prints 郝德路
  where the body prints 赫德路 (Hart Road, today Changde Road). Body form used;
  the figure caption notes the misprint. 郝德路 is not a real Shanghai road.
- **Checks (all green).** parity 165 = 165; numbers 0 unresolved (--noise);
  qc_entities 0 misses; check_align median 4.58 en/han, no pair beyond 2.2x;
  check_content 390 name occurrences all in the paired paragraph, no
  displacement; anchors 28/28 resolve; check_apparatus 0/0; qa_epub PASS (255
  notes total, all refs/bodies/backlinks); epubcheck 0 fatals / 0 errors / 0
  warnings. Tail (final 8 paragraphs, p0148) verified against the scan; nothing
  invented.
- **Register vs the frozen ch01 reference:** within tolerance. The dialogue
  contraction rate reads 11.4/1k against ch01's 0.3/1k (a 38x ratio), but that
  is the dialogue-density artifact, not drift: ch01 is nearly dialogue-free
  while ch06 runs dialogue-heavy (arrest scenes, interrogations, Zhou/Li
  exchanges). Judged on the narratorial signals per references/register-drift.md,
  ch06 tracks the reference: em-dash 8.8/1k vs 8.2, rhythm CV 0.73 vs 0.67,
  shall-share 0% (no formal "shall" leaked into speech), sentence median 24.
- **Numbers / noise (do not revert).** A B06 block appended to data/noise.txt:
  romanized names with a numeral (四成里 Sicheng Li, where 四成 misreads as
  40%/0.4; 曾三 Zeng San; 零陵 Lingling; 万航渡路 Wanhangdu Road); idioms whose
  magnitude the English carries in words (零敲碎打, 零配件, 零件 all with 零 = "odd",
  十字路口 "crossroads", 六神无主, 千刀万剐, 千斤重担, 烽火万里, 百姓); and the
  event date-name 四一二 (the "4-12"). Every entry strips a SOURCE numeral that
  carries no cardinal quantity, so none can mask a real drop. Five genuine
  "keep the counted numeral" fixes were made to the English instead of noised:
  restored "Sixth" (六大会场), "four in all" (四人), "the two of them" (两人,
  both named), "the two characters" (两字), and "seventeen ... and three" (十七人
  / 三人) in the sentencing.
- **Notes: 28.** Fresh tradecraft and material culture (three-stripers /
  sandaotou, Yangjingbang pidgin, the Zikawei Observatory, the tiger bench and
  duckling's paddle, the Eight-Trigrams prison plan, the Hao cipher, the
  "electric-light news"); the Soviet apparatus (Sixth Congress in Moscow, KUTV,
  the Cheka, the Frunze school); people a Western reader needs (Yun Daiying and
  the "captive of Chu" allusion, Xia Yan, Zhou Libo, Liu Renjing, Cao Diqiu, Li
  Shaoshi / Liao Zhongkai, Granny Xia, Zhang Ding & Ling Zifeng, Xiang Zhongfa);
  New Youth, Lord Mengchang, the "4-12", the Three Principles, the National
  Labor University; and the two apparatus points above (the roster/Shen Bao name
  divergence, Su Gangda's coded four-character farewell that gives the section
  title). Reader-model density, tapering appropriately for a mid-book chapter
  whose recurring furniture is already placed.
- **Figures: 3** (`data/figs/ch06-*.png`), hand-cropped with the printed caption
  line excluded and re-captioned by the translator with the source-label
  provenance line, each with real alt text: Zhang Shenchuan in later years
  (placed at s05), the Zhou Enlai / Deng Yingchao couple portrait (s06), and the
  Central Military Prison corridor (s10). find_figures not relied on; every page
  eyeballed. No line-art diagrams.
- **Glossary: ~120 rows added** (people, organizations, places, terms), written
  straight into the sectioned ledger (NOT via apparatus_merge, per the flat-row
  gotcha) and re-read verified. Each new row's `en` set to the form actually
  rendered (the B05 qc_entities/check_content lesson). Reused unchanged from
  earlier batches: 巨籁达路 = Rue Ratard, 西摩路 = Seymour Road, the Central
  Special Branch, the Red Squad, the dog-beating squad, shikumen, the Great
  World, Li Qiang, Xu Enzeng, Chen Lifu, Deng Yingchao, Zhang Guotao, Xiang
  Zhongfa, Zhao Shiyan, Wu Zhihui.

### Renderings settled this batch (also in glossary.json)
- People (principals): 涂作潮 = Tu Zuochao (codename "Carpenter"), 张沈川 = Zhang
  Shenchuan, 苏刚达 = Su Gangda (real name 任玑 Ren Ji), 蔡叔厚 = Cai Shuhou,
  夏衍 = Xia Yan, 恽代英 = Yun Daiying, 李强 = Li Qiang (reused).
- Concession streets: 迈尔西爱路 = Route Cardinal Mercier (Maoming South Road),
  亚尔培路 = Avenue du Roi Albert (Shaanxi South Road), 极司非而路 = Jessfield
  Road (Wanhangdu Road), 大西路 = Great Western Road (Yan'an West Road), 福煦路 =
  Avenue Foch (Yan'an Middle Road), 古拔路 = Route Voisin (Fumin Road), 赫德路 =
  Hart Road (Changde Road), 康脑脱路 = Connaught Road (Kangding Road), 有恒路 =
  Youheng Road, 三马路 = Sanma Road (Third Horse Road, Hankou Road). Uncertain
  French names not invented; Chinese-named roads kept as pinyin.
- Places: 四成里 = Sicheng Li, 福康里 = Fukang Li, 福德坊 = Fudefang, 惠中旅馆 =
  the Huizhong Hotel, 徐家汇天文台 = the Zikawei Observatory; Soviet places
  伯力 = Khabarovsk, 符拉迪沃斯托克 = Vladivostok, 列宁格勒 = Leningrad,
  兹维尼果罗德 = Zvenigorod.
- Organizations: 福利电器公司 = the Welfare Electric Company (the frequency /
  flequency / fuli pun carried in the body), 绍敦电机公司 = the Shaodun Electric
  Company, 党务调查科 = the Party Affairs Investigation Section, 国立劳动大学 =
  the National Labor University, 中央军人监狱 = the Central Military Prison,
  苏州反省院 = the Suzhou Reformatory, 商务印书馆 = the Commercial Press.
- Terms: 木匠 = "Carpenter", 三道头 = three-stripers, 洋泾浜英文 = pidgin English,
  孟尝君 = Lord Mengchang, 豪密 = the Hao cipher, 老虎凳 = the tiger bench,
  八卦 = the Eight Trigrams, 铁窗大学 = iron-window university, 楚囚 = captive of
  Chu, 矽钢片 = silicon-steel laminations, 风语者 = windtalker.

### NOT re-noted (already placed earlier) — cross-referenced, not re-noted
- The Central Special Branch / Red Squad and the dog-beating squad (ch01/ch03);
  Zhou Enlai, Gu Shunzhang, Chen Lifu, Xu Enzeng (ch01/earlier); the Sixth
  Congress framing beyond the Moscow venue (ch01); Chen Duxiu (ch01); the
  Whampoa Military Academy (ch01); the White Terror (ch01/ch03); Wuhao =
  Zhou Enlai and Liming = Gu Shunzhang's alias (ch04/ch05); shikumen and
  tingzijian (ch01/ch03); the Sincere Company (ch01); the concession police and
  patrolmen (ch04/ch05); silver dollars and the concessions generally.

## B07 = Chapter Seven "大隐隐于市 / The Great Hermit Hides in the City" (ch07)

- **Scope.** PDF 150-171 (printed 135-156). Seven sections ch07s01-s07, 22
  pages. The chapter divider (p0150) is design furniture (washed-out full-bleed
  illustration + the section list), not a captioned figure. Body runs PDF
  151-171; p0159 (printed 144) is a FULL-PAGE old street map (a figure, caption
  only, no body text).
- **Offset held constant 15** (printed = pdf - 15). Folios read off the scan at
  every opener (137 on p0152, 139 p0154, ... 156 p0171); no plate drift.
- **Source.** data/zh/ch07.txt hand-transcribed from the scans, one paragraph
  per line, chapter title and section heads as ###. 99 paragraphs. All quoted
  matter (the Ding Ling and Mao Dun literary passages, and the Zhang Wenqiu /
  Li Yimang / Hong Yangsheng / Yi Hui / Xiao Ke / Ding Ling / Xia Yan memoirs)
  is inline quotation, no {v} blocks this chapter. Inline source citations
  render (Author, YEAR): (Li Yimang, 2001), (Zhang Wenqiu, 2002), (Lin Chengxi
  and Xu Rongsheng, 1996), (Yi Hui, 2002), (Xiao Ke, 1997), (People's
  Government of Meilong Township, Shanghai County, Shanghai, 1986).
- **Crop-verified names/numbers** (dual-OCR disagreement + by-eye magnified
  crops): 邹志淑 Zou Zhishu and her school 庄史高级中学 / 新塍读书会; the
  Southeast Hubei delegate roll 吴梓民, 曹大全, 易金波, 方步舟, 余海侠（徐泽）;
  钱泓 / 高崇民 / 高大会 / 艾思奇 / 李昕东 (Nanshagou children); 阚思俊 (Liu
  Ding's real name); the address numerals 690至696号, 张家宅36号 vs 36弄, 210所,
  第68号 / 第八十一号通告, 近15000字, 50万元, 10万大洋, 60两白银.
- **Character of this chapter.** It is source-CRITICISM-heavy: the author weighs
  half a dozen memoirs against one another over where the congress met (the
  "British Concession"/Hart Road claims vs Li Yimang's Park/Burkill Road), and
  over whether "Fang Lin" was Deng Fa. Kept his dry, skeptical edge; the
  martyrdom set-piece (Zhao Yiman's farewell letter to "Ning'er") kept at full
  temperature per the interested-witness rule.
- **Global correction (cascaded): 卡德路 = Carter Road, not "Cardan Road."**
  The glossary and ch04 carried "Cardan Road"; verified against scholarship
  (卡德路 = Carter Road, today Shimen No. 2 Road). Fixed glossary.json and the
  two occurrences in out/ch04_reading.md; ch04 rebuilt in the cumulative EPUB.
  Logged in CHANGELOG.md.
- **Source-internal date discrepancy rendered as printed and footnoted:** the
  author narrates the congress on May 5-7, 1930 (section 6-7) but quotes Zhang
  Wenqiu's May 20 (section 2); the accepted scholarly date is May 20-23, 1930.
  Rendered as printed each place; a note at "May 5, 1930" states the conflict.
- **Caption/photo discrepancy (kept, noted):** the p0161 photo captioned
  卡尔登大戏院 (Carlton Theatre) in fact shows the vertical GRAND THEATRE sign.
  Source caption rendered faithfully; the figure caption and alt note that the
  photo shows the Grand's sign. Not the translator's identification.
- **Figures (6).** ch07-li-yimang (p154 portrait), ch07-prep-office (p155
  building), ch07-old-map (p159 full-page street map, CARLTON THEATRE label
  visible upper right), ch07-carlton (p161 theatre photo), ch07-liu-ding (p162
  portrait), ch07-dingling-huyepin (p167 couple). Printed captions excluded from
  each crop; captions are the translator's, labels the source's, stated in each.
  find_figures would miss the line-art map; hand-cropped.
- **Checks (all green).** parity 99 = 99; numbers 0 unresolved (--noise, with a
  B07 block added: 一九三○, 三三五五, 四郊, 八秩, 千言万语, 瘪三, 两回事, 牌九,
  两白银, 几十两, 零食 — each strips a source numeral with no cardinal quantity);
  qc_entities 0 misses; check_align median 4.67 en/han, no pair beyond 2.2x;
  check_content 264 name occurrences all in the paired paragraph, no
  displacement (ch07 added to data/content_config.json); anchors 20/20 resolve;
  check_apparatus 0/0; qa_epub PASS (275 notes total); epubcheck 0 fatals /
  0 errors / 0 warnings; check_style_freshness all layers FRESH.
- **Register vs frozen ch01.** em-dash 9.0/1k (ref 8.2), rhythm CV 0.63 (ref
  0.67), sent median 25 — all within tolerance. The dialogue-contraction metric
  reads 0.0/1k and the tool prints "STILTED," but this chapter is almost
  entirely quoted memoir and quoted literary documents (exempt registers that
  keep their form); the dialogue metric is QUIET here and is not itself drift
  (per references/register-drift.md). Judged on the narratorial signals, which
  are on-reference. Two natural contractions added to the one genuinely
  colloquial exchange (Liu Bocheng).
- **20 footnotes.** The congress (identity + dating), Ding Ling's ×× censorship,
  Ding Ling, Xiong Shihui, Zhang Wenqiu/Sorge/Mao in-law, Deng Fa (the source
  verdict), the spear-and-shield (Han Feizi) and great-hermit allusions, the
  "British Concession" misnomer, "seventy-two tenants," Zhao Yiman, the Mauser,
  the two concession Municipal Councils, the Li Lisan line, Red May, the
  sickle-and-axe flag, Ozaki Hotsumi, the May 5/May 20 dating, the Lord
  Guan/Kongming allusions, and Rou Shi & Feng Keng (Left League martyrs).
  Density tapering as expected (ch01 115 → ch06 28 → ch07 20).
- **NOT re-noted (already placed earlier) — cross-referenced, not re-noted:**
  the Comintern / Communist International (ch01-04); the Whampoa Military
  Academy (ch01); April 12th / the White Terror (ch02/ch06); the Internationale
  (ch04); the League of Left-Wing Writers as an organ (ch01/ch06); the
  Racecourse (ch05); Bubbling Well Road (ch03); Mao Dun and Midnight (ch01);
  Qu Qiubai (ch01-03); the Central Special Branch / Red Squad; Zhou Enlai,
  Gu Shunzhang, Chen Geng, Li Lisan the man, Xiang Zhongfa; silver dollars,
  taels, and the concessions generally.

### Renderings settled this batch (also in glossary.json)
- People (new): 熊式辉 Xiong Shihui, 李薇薇 Li Weiwei, 李一氓 Li Yimang, 张文秋
  Zhang Wenqiu, 林育南 Lin Yunan, 邓发 Deng Fa (方林 Fang Lin his queried alias),
  刘鼎 Liu Ding (阚思俊 Kan Sijun), 易辉 Yi Hui, 洪扬生 Hong Yangsheng, 邹志淑
  Zou Zhishu (邹志英), 宋再生 Song Zaisheng (宋启荣), 蒋伯器 Jiang Boqi, 何长工
  He Changgong, 滕代远 Teng Daiyuan, 萧克 Xiao Ke, 熊寿祺 Xiong Shouqi, 胡也频
  Hu Yepin, 柔石 Rou Shi, 冯铿 Feng Keng, 丁玲 Ding Ling, 茅盾 Mao Dun, 尾崎秀实
  Ozaki Hotsumi, 左尔格 Sorge, 赵一曼 Zhao Yiman (李一超 Li Yichao / 李坤泰 Li
  Kuntai), 宁儿 Ning'er, 宋保苏 Song Baosu, 吴国麟 Wu Guolin, 钱壮飞 Qian
  Zhuangfei, 赵毅敏 Zhao Yimin, 刘思齐 Liu Siqi (松林 Songlin), 邵华 Shaohua.
- Concession geography: 卡尔登大戏院 = the Carlton Theatre (today Changjiang
  Theatre); 白克路 = Burkill Road (Fengyang Road); 派克路 = Park Road (Huanghe
  Road); 卡德路 = Carter Road (Shimen No. 2 Road, corrected); 爱文义路 = Avenue
  Road (Beijing West Road, reused); 赫德路 = Hart Road (Changde Road, reused);
  麦特赫斯脱路 = Medhurst Road (Taixing Road); 静安寺路 = Bubbling Well Road
  (reused); 静安寺 = Jing'an Temple; 跑马厅 = the Racecourse; 洋泾浜 = the
  Yangjingbang; 苏州河 = Suzhou Creek; 黄浦江 = the Huangpu River; 虹口 =
  Hongkou; 乍浦路 = Zhapu Road; 张家宅 = Zhangjiazhai; 南沙沟 = Nanshagou.
- Organizations: 中华全国总工会 = the All-China Federation of Trade Unions;
  中国左翼作家联盟 = the League of Left-Wing Writers (the "Left League"); 工部局
  = the Municipal Council; 公董局 = the French Municipal Council; 保定军官学校 =
  the Baoding Military Academy; 同盟会 = the Tongmenghui. Event names left OUT of
  the entity-checked glossary to avoid false displacement flags: 全国苏维埃区域
  代表大会 = the National Congress of Soviet Areas (short handle "the Congress"),
  苏准会 = the "Prep Committee," 苏维埃工农兵代表会议 = the soviet congress of
  workers, peasants, and soldiers.
- Terms: 驳壳枪 = Mauser (the "box cannon"); 镰刀斧头旗 = the sickle-and-axe flag;
  长衫 long gown, 马褂 riding jacket, 旗袍 qipao; 戥子 native/foreign scales;
  瘪三 biesan (glossed "street urchin" inline).

## B08 = Chapter Eight "金陵夜，十万火急 / A Nanjing Night, Deadly Urgent" (ch08)

### What was produced
- Full translation of ch08: 252 paragraphs across ten sections, `out/ch08_reading.md`.
  PDF 172-207, printed 158-192; offset constant 15, no plate drift, folios read
  off the scan at each opener.
- `data/zh/ch08.txt` hand-transcribed off the scans (OCR too noisy on the dense
  memoirist names); chapter title marked `###` per the parity gotcha.
- 21 footnotes; 4 figures; 43 new glossary rows.

### Checks run and results
- Parity 252=252 (check_structure --pairs OK). verify_unit: parity, numbers,
  anchors all clean.
- Numbers: check_numbers 0 unresolved after the B08 noise block (all flags were
  word-internal numerals in names/places, idioms, or rounded rhetoric the English
  already carries: 张万栋, 万状, 百昌, 千奇百怪, 百计/千计, 六安, 九旬, 接二连三,
  九江, 星期六, 垂涎三尺, 三四十年代, 万安). NONE was a real dropped quantity.
- qc_entities 0 misses; check_content 0 displaced across ALL units (416 glossary
  names now). One caught displacement fixed: 夏娘娘 was drafted "Auntie Xia",
  corrected to the decided "Granny Xia".
- check_align OK (median 4.78 en/han, no pair strays > 2.2x).
- Register vs frozen ch01: within tolerance. Narratorial signals close (em-dash
  5.0/1k vs ref 8.2; rhythm CV 0.69 vs 0.67; sent median 23; shall% 22 vs 20).
  Dialogue-contraction 1.3/1k (4.49x ref) is HIGH but expected: this chapter runs
  heavily on quoted family-interview speech (Qian Hong, Li Li, Li Lun, Nie Li,
  Dong Huifang, Li Lili), which is colloquial and contracts. Not drift.
- Tail verification: final paragraphs (the Ouyang Yi 1998 account of Qian
  Zhuangfei's death) read against p206 as translated. Clean.
- qa_epub PASS (296 refs/bodies/backlinks resolve); epubcheck 0/0.

### Notes placed (21) and NOT re-noted
- Placed at first ch08 appearance: the seventeenth year of the Republic (=1928);
  Carnegie Institute of Technology (source's 康奈杰工业大学, with the electrical-
  vs-business-management source split flagged); Zou Taofen; natural (unbound)
  feet; Qian Xuantong / Lu Xun's Madman's Diary; the Wuyue kings; Li Lili;
  Sun Tzu's five spies; the Three Heroes of Longtan (龙潭三杰, the emblem);
  the West Lake Exposition; Nie Rongzhen; the "assassinate Chiang" question
  (fact-check verdict, left open); the Central Plains War; the First Encirclement
  Campaign; Zhu/Mao/Peng/Huang; bang-bang chicken; the Horse King's three eyes;
  the Zeng Guofan book-code; the Wu River; how Qian Zhuangfei died (the three
  contested accounts, verdict in the note); the Western Route Army.
- **NOT re-noted (already placed earlier, cross-referenced):** Gu Shunzhang,
  Central Special Branch, Red Squad, Zhongtong, CC Clique / the two Chens,
  Borodin, Wakeman, the GPU, the Comintern, Zhang Guotao (ch01), Dong Jianwu
  (ch01/ch04), Song Qingling (ch01), Cai Mengjian (ch02, covers his arrest of
  Gu), Li Lisan (the man), Wang Ming, Zeng Guofan (partially), 化广奇/黎明 (Gu's
  stage name and alias), Zhou Enlai, Chen Geng, Chiang Kai-shek, silver dollars.

### Renderings settled this batch (also in glossary.json)
- Aliases previously undocumented in glossary, now added: 化广奇 = Hua Guangqi
  (Gu's stage name; the p193 archive file spells it 化光奇), 黎明 = Liming.
- Three Heroes of Longtan (龙潭三杰) = Qian Zhuangfei, Li Kenong, Hu Di.
  NOTE: 李克农 and 胡底 are deliberately NOT in the entity-checked glossary
  (as in B01-B07): both recur constantly with pronoun runs, and adding them would
  fire false check_content displacement across the whole book. Rendered
  consistently Li Kenong / Hu Di throughout.
- People (new rows): 钱江 Qian Jiang, 钱泓 Qian Hong (existed), 钱玄同 Qian
  Xuantong, 邹韬奋 Zou Taofen, 王思诚 Wang Sicheng, 李熙元 Li Xiyuan, 孟真 Meng
  Zhen, 张暹中 Zhang Xianzhong, 董惠芳 Dong Huifang, 盛岳 Sheng Yue, 聂荣臻 Nie
  Rongzhen, 聂力 Nie Li, 李力 Li Li, 李仑 Li Lun, 陈昌浩 Chen Changhao, 沈泽民
  Shen Zemin, 顾建中 Gu Jianzhong, 张冲 Zhang Chong, 吴德峰 Wu Defeng, 陈知建
  Chen Zhijian, 尤崇新 You Chongxin (本名游无魂 You Wuhun), 鲁涤平 Lu Diping,
  何成濬 He Chengjun, 王素卿 Wang Suqing ("Miss Wang"), 刘杞夫 Liu Qifu, 徐双英
  Xu Shuangying, 黄纲 Huang Gang, 潘虹 Pan Hong, 黎莉莉 Li Lili, 王智涛 Wang
  Zhitao, 欧阳毅 Ouyang Yi, 顾竹轩 Gu Zhuxuan, 常春恒 Chang Chunheng, 王明 Wang
  Ming, 王云程 Wang Yuncheng, 陈寿昌 Chen Shouchang, 宋庆龄 Song Qingling, 鲍罗廷
  Borodin, 魏斐德 Wakeman.
- Organizations: 正元实业社 = the Zhengyuan Industrial Company; 长江通讯社 = the
  Yangtze News Agency; 民智通讯社 = the Minzhi News Agency; 长城通讯社 = the Great
  Wall News Agency. Existing reused: 中统 the Zhongtong, 党务调查科 the Party
  Affairs Investigation Section (handle: the Investigation Section), 中央特科 the
  Central Special Branch, 红队 the Red Squad.
- Places kept as printed with source inconsistencies preserved: 康奈杰工业大学
  (Carnegie); 脚渡河 the Jiaodu River (crossed on the Long March, spring 1935);
  达智门/大智门 both rendered Dazhimen; 新市场游艺场 the New Market pleasure grounds
  vs 新世界游艺场 the New World pleasure grounds (source uses both; kept).
- The Internationale (S5): rendered as verse ({p}, one line per source line),
  faithful to the Chinese lyric, footnoted-adjacent to the martyr set-piece.
- Set-off block quotes rendered {v}: the Xu Enzeng memoir (S1), the Chen Yun
  biography (S8), the Wang Zhitao death account (S10). Two spring-scene white-space
  gaps on p192 kept as ordinary paragraph breaks (no `***`, consistent with
  B01-B07 which use none).

### Figures (4)
- ch08-xu-enzeng.png (p174 portrait), ch08-chen-lifu.png (p175 portrait),
  ch08-longtan-trio.png (p180, the three heroes), ch08-archive-caselist.png
  (p193 full-page handwritten case-list of the Wuhan detection section).
- p207 is a washed-out full-page chapter-divider illustration = design furniture,
  NOT a captioned figure (per the standing B07 trap note). Excluded deliberately.

### Standing decisions / traps confirmed
- The dual-OCR (ocr_dual.py) writes nothing consumable here; direct reading of the
  300-DPI page images was the reliable transcription method (names too mangled in
  OCR). data/zh is gitignored, so a fresh checkout cannot regenerate ch08.txt.

---

## B09 continuation: the register de-archaizing pass over ch01-ch08

Session picked up the B09 register rebaseline (STYLE.local "THE REGISTER
REBASELINE"). The itemized B09 review fixes were already in; this session ran the
systematic sentence-by-sentence register de-archaizing pass the rebaseline
specifies.

### Housekeeping
- Branch: the harness started on a stray `claude/sword-roars-register-pass-p7h1yb`
  that was identical to `origin/claude/the-sword-roars` (both at 4598fa3).
  Consolidated onto the canonical `claude/the-sword-roars`; deleted the stray
  (local; the remote ref was already gone, pruned).
- `tests/run_tests.py` "hook stands down on template stub" was FAILING on every
  active book because the stand-down subcase wrote back the real book HANDOFF
  (not a stub) and expected no block. Hardened it to stage an actual placeholder
  stub, then restore the real handoff. Regression suite now green on a live book;
  setup.sh no longer prints the spurious CHECKER REGRESSION TESTS FAILED line.

### Method for the register pass
- Fresh checkout has NO data/zh (gitignored, copyright) and no page renders. The
  register pass is English->English re-voicing of the gate-approved, B09-corrected
  translation, so fidelity is guaranteed by preserving the propositional content
  of every OLD in its NEW (no fact/name/number/date-value/claim change), verified
  by direct OLD/NEW comparison. No line was re-translated; nothing was invented.
  Source pages were not rendered for this pass (they are needed only for ch09
  drafting, which is deferred). This is the defensible reading of CLAUDE.md rule 4
  for a register-only pass over already-faithful text.
- Driver: `edits/chNN_edits.md` + `scripts/apply_edits.py` (safe single-match
  replace; NOTE-ANCHOR moves in the same pass). A tic-battery grep
  (`scripts/register_tics.sh`) drove targeted edits; ch01, ch02, ch03, ch05, ch06, ch07
  were read in full, ch04 and ch08 (the two largest) via context-grep on each hit.
- LESSON (cost a build failure): cross-check every OLD against BOTH notes.json AND
  figures.json anchors before applying (`scripts/anchor_check.py`). A ch05
  figure `before` anchor and three ch01 note anchors were broken by re-voicing and
  had to be moved.

### What the pass did, per chapter (all builds + qa_epub clean, 302 notes)
- ch01 (frozen reference, deepest pass): rhetorical questions -> declaratives
  (keeping the quoted Ho Chi Minh poem + Luo Qingchang quote), de-nominalized the
  flagged "the [gerund] of" chains, cut 即/也就是 and 不能不/could-only archaisms,
  modernized the Bo Yibo quote tag, trimmed a fronted-superlative doublet, added
  narration contractions. PLUS the day-month -> month-day date sweep the B09 STATE
  reported done but that had NOT actually been applied to ch01 (13 dates, incl.
  diary datelines inconsistent with the diary's own first entry).
- ch02: 3 date stragglers fixed; de-nominalization; "before long"->"soon"; the
  Yang Zhihua dash-parenthetical bio broken into its own sentences (a topology
  type-specimen the rebaseline names).
- ch03: kill-list "had no wish to"/"it was gone nine"; cut doubled "which was to
  say" and "namely" pivots; de-nominalized "the killing of"; one anchor moved.
- ch04: "before long"->"soon"; "still less could"->"nor could"; varied "and the
  rest"; contractions. Quoted documents (Lu Xun, Zhou Enlai, Li Qiang diary) left
  in register.
- ch05: "before long"->"soon" (narration only; quoted autobiography left);
  contraction; varied "and the rest"; one FIGURE anchor updated.
- ch06: "for all that"/"before long"/"had no wish to"; de-inverted a fronted
  "Still less did X imagine"; contraction; varied "and the rest".
- ch07: reviewed in full and found ALREADY at the target modern register (drafted
  in B07); one contraction only. ch07's real need is note-density backfill.
- ch08 (targeted): "for all that"/"thereupon" x2/"before long"; cut 不得不 "could
  not help admitting"; modernized an interviewee's "come what may"; varied "and
  the rest". The Qian Xuantong topology split was already in place.

### Checks
- qa_epub PASS after every chapter; epubcheck 5.1.0 clean (0 fatals/errors/
  warnings/infos) on the final build. 302 notes throughout (no notes added or
  moved except the anchor repairs above).
- check_register.py --ref out/ch01_reading.md (informational, per the kickoff):
  ch04 flags "STILTED", which is the reportage-caveat noise, not a defect: ch04 is
  memoir/document-heavy (Zhou Enlai, Li Qiang, Ke Lin, Zhang Guodong quotes), so a
  low dialogue-contraction rate is correct. The frozen ch01 ref itself sits at
  0.3 contractions/1k, so the "vs ref" multiples are inflated by a near-zero
  denominator. No action taken.
- Consistency-canon regression check (run because the date claim proved wrong):
  "Political Bureau", "Centre", lowercase "white terror", "Zikawei Observatory",
  "Idly Seeking", "Cardan" all return ZERO across reading files + notes.json. The
  other B09 consistency sweeps held; only the dates had slipped (now fixed).

### DEFERRED to the next batch (with specs in HANDOFF)
- Footnote sweeps: (a) placement (move mid-clause markers to clause/sentence end,
  ~88 of them) and (b) density (thin ch01, backfill ch07-ch08, and move recurring
  institutional glosses to a BACK GLOSSARY). The back glossary and the back-matter
  street gazetteer are NEW builder features that do not exist yet; they are the
  gating work.
- Spine-test pass: 52 narration-ish sentences over 90 words remain across ch01-08
  (ch01 13, ch08 16 the heaviest; some are exempt quoted-document or colon-list
  sentences). The flagship long sentences were already broken (Qian Xuantong;
  ch01 rhetorical ending; ch02 Yang Zhihua bio).
- ch09 draft ("The Riddle of Xiang Zhongfa's Disappearance", PDF 208-235, printed
  193-220). Deferred deliberately: it needs page-by-page hand-transcription off
  the 300-DPI scans (OCR too noisy on the proper names), which is high-cost and
  high fabrication-risk to rush; better done fresh with the full recipe (in
  HANDOFF and book.json already carries the 9-section structure).
