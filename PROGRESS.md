# PROGRESS — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The running per-batch log. Written as work happens, not at the end.

## Batch 6. Chapter 4, sections 5–8 "Hard Fighting in the Jin-Sui Border Region" (ch04s05–s08; PDF 147–171, printed 136–160)

APPENDED sections 5–8 to the EXISTING out/ch04_reading.md (now 8 "###" sections +
4 "####" subsections; body 245 paras, headings 12). data/zh gitignored and gone
on this fresh checkout, so the whole ch04 Chinese source was rebuilt: sections
5–8 hand-assembled from corrected OCR + scans this batch, sections 1–4
reconstructed from OCR aligned to the frozen English (parity-locked). No
chapter-intro paragraphs; each section opens straight on its heading. PDF 147 top
verified — no lead paragraph before section 5.

### Content
- S5 (沉着果断，潜入敌特内部窃取密电, PDF 147): Zhang He (= Zhang Youxin) working
  three times into the enemy service at Guisui to steal ciphered cables; the 1943
  Li Wucai wireless attempt wrecked by Wu Bingzhou's defection; the 1947 penetration
  of the Suiyuan Investigation-and-Statistics office; Pei Zhouyu's cipher warning to
  Chen Yangshan; the Guisui/Jining connection roster.
- S6 (深入敌后，大同情报工作的开展, PDF 150): Wang Yanming (Fang Shaoming) building
  the Datong network from inside the Resource Investigation Society; disarming the
  mine-police band; buying the 38th Division's order of battle and city-defense maps
  (Han Buzhou's guard-officer Peng, the clerk Ma Zaiwu, the cipher clerk Liu
  Wenzhong); the May 1946 collapse and Chen Yangshan's own 1985 lesson-summary; a
  frank close on Wang's stumble and worth.
- S7 (敌中有我，机智的鲁南情报组织, PDF 154): the whole arc of Lu Nan (Zhao Xihong),
  Suide → the Ike Zhao League → Dongsheng (the 1941 arrest by Jia Gengfu) →
  Yan'an vetting → the 1946 penetration of the Suiyuan Special Conference
  Secretariat under Zhang Qing'en; He Long claiming the network for Jin-Sui; Lu
  Nan's death (Jan 1947, aged 33); Cui Jizhou and Wang Qi carrying it to the 1950
  destruction of the Suiyuan Investigation-and-Statistics organization.
- S8 (历史一页，晋绥情报传奇故事, PDF 160): four legendary tales — (1) Liu Zhen the
  book-buyer and the Mauser at the ford; (2) the Lanxian couriers (Li Yuanze, Zhao
  Guilong, the "strongbox" wives, the milk-copied plan retold); (3) Li Fang's raid
  to seize the Japanese quartermaster Nanqi (Nakamura Rijin); (4) Zheng Gui cracking
  the Bureau of Confidential Investigation's Suiyuan network — turning Xing Shaowen
  and Wu Yumei, the Pang Zhongxing/Yang Bingren feud, and the seized wireless sets.
- book.json fix: ch04s07 title_en was a survey mistranslation ("Southern-Shandong
  Network"); 鲁南 is a PERSON's codename (Zhao Xihong), so retitled "Lu Nan's
  Ingenious Network". Noted in the Lu Nan footnote.

### Paragraph structure
- S5=9 body, S6=15, S7=24, S8=55 (across 4 "####" subsections) = 103 new body
  paras; +4 "###" + 4 "####" headings. data/zh and reading file structurally
  identical line-for-line (scoped ch04s58 parity 103=103; whole-chapter parity
  re-run after S1–4 reconstruction).
- Tail-verified every long paragraph's final sentences against the scan (rule 4):
  restored a DROPPED short final line on p158 (the reply-letter quote ended
  "…已与" in OCR; the scan shows "…已与崔谈过。").

### OCR / crop-verification (this batch)
- Same crop as ch01–ch05 (do-not-revert list unchanged). ocr_crop + ocr_dual run
  per-page in the background; pgrep -c tesseract 0 after.
- Crop-verified names against the scan (OCR garbled): 韩步洲 (38th Div cdr, NOT
  昔步洲); 龚国华; 冀述楷 (Guisui station head, distinct from 王树楷 Wang Shukai);
  龚震; 冀聘之; 贾耿夫; 李禾亭 (one man, inspection-chief AND Juntong agent);
  巴荣昌; 陈奇涵; 李启明 (distinct from 李甫山); 亢上池 (NOT 元上池); 胡全福 (NOT
  关全福); 郭长青; 米景铨; 张玉清/郭靖帮; 李鲲生/崔正春/田树梅/胡尚儒; 咎良;
  邢绍闻 (上尉编审); 何柱国; 武毓美 (consistent, NOT 武航美); 大台乡. Months/years
  verified: 同年7月 (Ba Rongchang), letter dated 1946年7月14日, 1947年1月8日 (Lu Nan
  death), 张庆恩's 同年7月/19人, 11人 fled, 1950年秋 roundup.

### Source errors rendered as printed + footnoted (do NOT "fix")
- 1912年 for 1942 (Zhang He's Zaoyuan training, printed 136) — chronologically
  impossible; rendered as printed, footnoted.
- 马汉山 / 马汉三 — the SAME Juntong chief spelled two ways (printed 145); both
  rendered as printed (Ma Hanshan / Ma Hansan), footnoted + cross-noted in glossary.
- "1945年1月上党战役后" (printed 153) — the Shangdang Campaign was fought Sept–Oct
  1945; rendered as printed, date-error footnoted.
- 周高明 / 田高明 — the same courier, two surnames (printed 152); both rendered,
  cross-noted in glossary.
- 右平县 (Youping County, printed 137) rendered as printed — no such standard county;
  obscure local name, left unfootnoted (per the ch04 minor-name tier).
- 田唆布 (printed 159) reading uncertain from the scan — glossary status provisional.
- 一奉烧鸡铺 (printed 138): the classifier/name is garbled in print; rendered
  functionally ("a roast-chicken shop").

### Figures (3; every page eyeballed)
- p0148-f1 (printed 137, Sui-Meng Public Security cadres group photo; Pei Zhouyu,
  Zhao Fang, Zhang Rugang labelled), p0160-f1 (printed 150, Qu Rixin + Li Jiankui),
  p0171-f1 (printed 160, Mao Zedong's Nov-1950 security-work inscription — line art
  find_figures MISSED, caught by eye). Captions crop-excluded; alt text has no
  straight double quotes; who's-who labels are the source's, caption prose the
  translator's. find_figures flagged only the two photos, as expected.

### Apparatus
- notes.json: +35 (ch04 now 75; book-wide 340). New glosses at first appearance:
  Guisui, the Investigation-and-Statistics (调统) system, the National Liberation
  Vanguard, the Anwubao class, the Sacrifice League, the 1912 misprint,
  good-citizen certificate, Houhehaote, the First Suiyuan Campaign, Jin-Cha-Ji,
  the Resource Investigation Society, Gao Kelin, Chu Xichun, the MSS, Lu Nan (with
  the codename etymology + the survey-title correction), He Shaonan, Chen Qihan,
  the Ike Zhao League, Ma Zhanshan, Kangda, Chen Changjie, Juntong vs Zhongtong,
  the Seventh Congress, Ma Hansan (with the spelling discrepancy), Ouyang Qin, Dong
  Qiwu (the source's own bio footnote, translated), the "Suiyuan formula", Zhou
  Fohai, Chen Gongbo, the Shangdang date error, He Zhuguo, Mao Renfeng, the
  gold-yuan, the Bandit-Suppression HQ, the Sept-19 uprising. Already-noted
  (Datong, the Bureau of Confidential Investigation, the Comradeship Association,
  Kenanpo, the Daqing Mts, the Gao Shuxun Movement, He Long, Pei Zhouyu, E Yousan,
  the milk-copied plan, Wei Gang's 320th-Div defection) cross-referenced, not re-noted.
- glossary.json: +159 rows (576 referents), sectioned people/organizations/places/
  events; ONE rendering per referent; the 鲁南=赵锡鸿=赵孚民, 方少明=王雁鸣,
  南奇=中村里仁, 马汉三/山, 周/田高明, 张新甫=Li Wenfang aliases cross-noted.
- figures.json: +3 (ch04 now 8).
- data/noise.txt: +10 (names 李五才/刘万春/马汉三/鄂友三, places 五寨/五原, phrase
  两党, idioms 万籁俱寂/惊恐万状, date 九一九) — all carried in English prose, none
  quantities.

### Checks (all green)
- The batch's new content (S5–8) was validated on a UNIT-SCOPED pairing
  (data/zh/ch04s58.txt vs out/ch04s58_reading.md, config
  data/check_config.ch04s58.json) — the same parity/number/content/entity/align
  checks the kickoff lists, run on exactly the new sections (S1–4 is frozen and
  was validated in B05): parity 103=103; check_numbers 0 unresolved (via bilingual
  + noise); qc_entities 0 misses (493 name occurrences, top 绥远 ×93, 鲁南 ×65, 归绥
  ×60); check_content all name occurrences in the paired paragraph; check_structure
  PASS (headings level-shape OK, ### + ####); check_align OK (median 4.90 en/han).
- Whole ch04 (no zh needed): check_apparatus 0/0; check_register within tolerance
  of ch01 ("shall" 14% is one formal quote — Zhao Siwu's "we shall come to
  grief…" — verified; em-dash 0.0/1k, rhythm 0.66); check_style_freshness all
  layers fresh. Build: 4 of 12 chapters, 340 notes; qa_epub PASS (54 files,
  340/340/340 notes resolve, all links resolve); epubcheck 5.1.0 = 0 fatals /
  0 errors / 0 warnings.
- Whole-chapter confirmation: with S1–4 zh reconstructed (from OCR aligned to the
  frozen English) and concatenated with S5–8, data/zh/ch04.txt = out/ch04_reading.md
  = 257 lines; verify_unit ch04 parity 245=245 OK, all 75 note anchors resolve;
  check_structure PASS; check_align OK (median 4.78 en/han). Four residual
  number/content flags all fall in the REGENERATED S1–4 zh and are artifacts, not
  defects in the new content: 张和 (Zhang He, a 2-char key) false-matches inside
  主张和平 "advocate peace"; and 绥蒙 appears in the reconstructed S1–4 zh where the
  frozen B05 English used "Jin-Sui"/"Suiyuan" — a 绥蒙-vs-晋绥 reading/rendering
  question on already-shipped S1–4 text, logged here as a candidate for the B10
  whole-book reconcile (check 12), not touched in this translation batch.
- NOTE: data/zh is gitignored and gone on a fresh checkout; the ch04 zh is
  hand-assembled/regenerated (committed nowhere), and the scoped pairing above is
  the validation of record for this batch's new content.

## Batch 5. Chapter 4, sections 1–4 "Hard Fighting in the Jin-Sui Border Region" (ch04s01–s04; PDF 117–146, printed 106–135)

NEW file out/ch04_reading.md carrying sections 1–4 only (four "###" section
headings, English titles from book.json) + data/zh/ch04.txt. Batch 6 appends
sections 5–8 to the same file. Added `ch04` to data/check_config.json and made a
scoped data/check_config.ch04.json for the structural checks (data/zh gitignored;
ch01–03 zh gone on a fresh checkout). PDF 116 (chapter opener recto, printed 105)
carries the title photo above the heading — SKIPPED per ch01/ch02/ch03 — and NO
chapter-intro paragraphs before section 1, so the file opens straight on "### 1.".

### Content
- S1 (情报纪事，陈养山晋绥经历, PDF 117): the Jin-Sui base area and its strategic
  role; Chen Yangshan sent in early 1945 to rebuild the Investigation Bureau;
  vetting, station-building, the Dec 1945 merger under Tan Zhengwen, He Long's and
  Li Kenong's 1947 talks, land reform, the 1948 takeover-prep, Linfen liberated.
- S2 (再创佳绩，贺龙麾下立新功, PDF 122): Luo Qingchang's record of He Long's
  esteem; the 1927–28 Shanghai backstory of why He Long asked for Chen by name;
  the vetting of Wang Shukai; Pei Zhouyu's recollections (source's own bio footnote
  reproduced); the book/press-collection task; exploits against enemy agents;
  Wang Shukai's martyrdom at Youyu.
- S3 (依势利导，全力搜集战略情报, PDF 130): the post-1945 pivot to watching the
  Nationalists; the Investigation Bureau / Public Security Bureau merger; the Gao
  Shuxun Movement (Gao's Handan defection, Pan Shuoduan at Haicheng, Liu Shanben's
  B-24); breaking up Yan's forces; five summarized lines of work; Suiyuan's
  peaceful liberation; Chen's four years praised by He Long and Li Kenong.
- S4 (剑胆琴心，陈养山一封绝密信, PDF 137): Chen Yangshan's Nov-20 top-secret
  letter (a {v} block) on the loss of "Xinfu"; then the whole saga of Wei Jian's
  underground station in Yan Xishan's Taiyuan — the Kenanpo years inside the
  "Comradeship Association," the "Fifth Miss" coup, the Xieyiheng dim-sum-shop
  cover, its Oct 1946 collapse, and the deaths of Zhang Xinfu (Li Wenfang), Cui
  Shou'an, Zhou Peiji, and Lü Lashuang.

### Paragraph structure (142 body paras: S1=28, S2=34, S3=33, S4=47)
- Section headings 4; `{v}` lines 8 (all in S4: the 7-line letter — salutation,
  three body paras, closing, signature, date — plus the newspaper missing-person
  notice). data/zh/ch04.txt and out/ch04_reading.md are structurally identical
  line-for-line, so every positional check aligns.
- CAUGHT one silent English drop on first pass: source line 143 (张若玲一回去…
  五花大绑) is ONE long paragraph including the chase, water pit, and Zhou Peiji's
  trussing; the first draft ended it early at "…district office." Restored the
  missing tail against the p146 scan (rule 4). Number check's [5] flag (五花大绑)
  is what surfaced it.

### OCR / silent-loss (crop-verified this batch)
- Same crop as ch01–ch03 (do-not-revert): --lang chi_sim --psm 6 --left 0.045
  --right 0.985 --top 0.08, running-head "秘战英雄陈养山", recto (PDF even)
  --bottom 0.945 / verso (PDF odd) --bottom 0.915, run per-page. ocr_dual.py run
  (backgrounded — it exceeds a 120s foreground timeout on a full chapter). pgrep
  -c tesseract 0 after.
- Crop-verified names/numbers: 罗青长 (printed 罗长青 at 106, a source
  transposition — one rendering "Luo Qingchang", noted); 周全 (dep. dir., NOT
  周仝); 崔耀南; 李甫山; 岚县 (mid-zoom lost the 山 radical and read 凤); 電陵桥;
  赵金鳌/赵精弟; 樊仰斌; 尉顺时; 魏×/李×× (source redacts given names, noted);
  吕拉双; 阎起鹅; 周佩玑 (玑, vs clansman 周佩瑶). The letter (p137) re-cropped
  clean and transcribed verbatim; para 3's "更不应该" corroborated by the p138
  quotation.

### Source errors rendered as printed + footnoted (do NOT "fix")
- 罗长青 for 罗青长 (Luo Qingchang) at printed 106 — name characters transposed.
- The April-13 intelligence speech printed TWICE with different years: 1948 at
  printed 109 (S1) and 1947 at printed 116 (S2), near-identical text — noted.
- 平律 for 平津 (Beiping-Tianjin) at printed 115 — misprint; sense followed, noted.
- 野板参三 for 野坂参三 (Nosaka Sanzo) — noted (Okano already glossed in ch03).
- 没谓 for 莫谓 in the Wang Shukai couplet — noted.
- 和清县 (Heqing County) and 二配区 rendered as printed (obscure local names).

### Figures (5; every page eyeballed)
- p0119-f1 (printed 108, re-cropped clean from the lower half), p0131-f1 (printed
  120), p0132-f1 (printed 121, ten named Taiyuan-station comrades), p0133-f1
  (printed 122, Gao Shuxun portrait), p0137-f1 (printed 126, Zheng Xiaoxian
  portrait). The chapter-opener photo (p116) SKIPPED per convention; find_figures
  flagged it and was ignored. All alt text single-quote-only (no straight
  doubles). Captions are the translator's; the who's-who labels are the source's.

### Apparatus
- notes.json: +40 (book-wide 305). New glosses: the Jin-Sui base area, Luo
  Qingchang, Stalingrad, the Daqing Mts base, the Gao Shuxun Movement + Gao
  himself, Pan Shuoduan, Liu Shanben, Li Jingquan, Tan Zhengwen, Ma Mingfang, Yan
  Xishan + Fu Zuoyi, the Bureau of Confidential Investigation, Pei Zhouyu (the
  source's own bio, translated), Zhao Jin'ao, the Kawasaki Mansion, the
  Book-and-Press Newsletter, the April-13 date discrepancy, Liang Shengyuan, the
  Assoc. for the Promotion of Democracy, E Yousan, Ma Hongkui + Dong Qiwu, the 平律
  misprint, the Wang Shukai couplet, the ×-redacted defectors, Sun Simiao's maxim,
  绵里藏针, the Comradeship Association, Kenanpo, Yan Huiqing, the Jiefang Daily,
  the Marshall three-man group, Chen Cheng, the (puppet) National Assembly, fabi,
  milk-as-invisible-ink, and the Rescue Movement. Already-noted subjects (He Long,
  Li Kenong, Special Branch, Kang Sheng, Juntong/Zhongtong, CC Clique, Rectification,
  Seventh Congress, Zaoyuan, Hu Zongnan, Nosaka/Okano, Wang Shiying, li, Nanchang,
  Central News Agency, Peng Zhen, Suiyuan) cross-referenced, not re-noted.
- glossary.json: +91 rows (417 referents). The whole ch04 cast added, sectioned
  people/organizations/places/events; ONE rendering per referent; Li Wenfang=Zhang
  Xinfu and Cui Shou'an=Wang Lianzhong cross-noted in their rows.
- data/noise.txt: +5 (百灵庙 place, 野板参三 name, 窘态百出 & 五花大绑 idioms, 40万
  arabic+万 magnitude split — all carried in English prose, none quantities).

### Checks (all green)
- parity 142=142; check_numbers 0 unresolved (via bilingual + noise); check_content
  0 displaced (352 name occurrences, all in the paired paragraph); check_align OK
  (median 4.69 en/han); qc_entities 0 misses; check_structure PASS; check_apparatus
  0/0; check_register within tolerance of ch01 (contr 1.4/1k, 0 em-dash, rhythm
  0.71); check_style_freshness all layers fresh. Build: 4 of 12 chapters, 305 notes;
  qa_epub PASS (51 files, all links resolve); epubcheck 0 fatals / 0 errors / 0
  warnings.

## Batch 4. Chapter 3 "From Enemy-Occupied Territory Back to Yan'an" (ch03; PDF 93–115, printed 82–104)

Whole chapter in one file: out/ch03_reading.md + data/zh/ch03.txt, three "###"
section headings from book.json. `ch03` mapped in data/check_config.json (docs +
sources). Because data/zh is gitignored and ch01/ch02 zh are gone on a fresh
checkout, the structural checks were scoped with data/check_config.ch03.json
(ch03 only); build/qa/epubcheck/register run on the whole cumulative EPUB.

### Content
- Section 1 (西安事变隐蔽战线高奏凯歌, PDF 94): the Xi'an Incident on the hidden
  front — Gao Fuyuan won over in captivity, Li Kenong's Luochuan talks with Zhang
  Xueliang and Wang Yizhe, Zhou Enlai's Yan'an meeting with Zhang, Wang Feng and
  Wang Shiying opening the channel to Yang Hucheng, and Chen Yangshan's Xi'an
  intelligence station (1936–40, cover name Chen Mingjun, via Song Qiyun).
- Section 2 (回到延安，整风学习为作战, PDF 103): the wallet-loss ruse escaping
  Xi'an, Chen at the Central Social Affairs Department under Kang Sheng, Zhang
  Suzhen's Party membership and nurseries, the Rectification at the Central Party
  School, Chen as Seventh-Branch secretary vetting cadres (Jiang Qing and Ye Qun
  among them), delegate to the "Seventh Congress," and Guan Fushan's recollection.
- Section 3 (三问康生，战友鲜血同志泪, PDF 110): the killing of four ex-Special
  Branch cadres (Wu Hujing, Xiao Shouhuang, Ouyang Xin, He Changzhi) in the Soviet
  purge, Chen's three questions to Kang Sheng, Kang's Yan'an "Rescue Movement" and
  Mao's counter-directives, and Chen's 1979 and 1988 letters exposing Kang.

### Paragraph structure (125 body paras: S1=40, S2=40, S3=45)
- Quoted documents/recollections set off with `{v}` (18 lines): Guan Fushan's
  3-para recollection; Mao's anti-traitor directive; Chen's two letters (the
  1979 exposé, 5 paras; and the appended 1988 letter to the Central Organization
  Department, title + salutation + body + closing). "附:" -> "Appended:" is a plain
  paragraph separating the two letter blocks. The 致/敬礼 closing merged to one
  line ("With respectful regards,") in both zh and en.

### OCR / silent-loss (crop-verified this batch)
- Same crop as ch01/ch02 (do-not-revert): --lang chi_sim --psm 6 --left 0.045
  --right 0.985 --top 0.08, running-head "秘战英雄陈养山", recto (PDF even)
  --bottom 0.945 / verso (PDF odd) --bottom 0.915, run per-page.
- **DROPPED TAIL restored:** PDF 94 mid-page "尖锐起来。" (the 4-char final line of
  the 张学良–蒋介石 paragraph) was silently dropped by tesseract; restored from the
  scan. Every page bottom verified; no other drops.
- **Crop-verified name corrections** (OCR wrong -> scan-correct): 戚元德 Qi Yuande
  (not 威), 塞先佛 Sai Xianfo (not 寒; base 土, flagged provisional), 劳山 Laoshan
  (not 序山), 瓦窑堡 Wayaobao, 彭德怀 Peng Dehuai, 李克农 Li Kenong, 阎揆要 Yan
  Kuiyao, 建宇 Jianyu (not 建字), 鄜县 Fu County.
- **Source inconsistency (rendered + footnoted):** PDF 94 prints 宗绮云 (Zong) at
  first mention; PDF 99 and the photo caption print 宋绮云 (Song Qiyun, the
  attested martyr). Rendered "Song Qiyun" throughout, variant noted.

### Figures (5; every page eyeballed)
- p0096-f1 Yang Hucheng portrait; p0098-f1 the Maoling group photo (Zhang/Yang/
  Chiang, Oct 1936); p0099-f1 Song Qiyun portrait; p0101-f1 Chen with family
  (1938); p0107-f1 the Seventh Congress hall. Captions translated into
  figures.json (alt uses single quotes only). Chapter-opener photo on PDF 93
  SKIPPED (per ch01/ch02). find_figures matched the plates; none are line art.
- **Source typo in a caption:** the Maoling caption prints 汉开帝墓; Maoling is the
  tomb of Emperor Wu of Han (汉武帝), rendered correctly in the translated caption.

### Fact-checks carried in the notes (interested-witness discipline)
- **Seventh Congress date:** source says 1943 (prep meeting and congress); the
  Seventh Congress in fact met 23 Apr–11 Jun 1945. Rendered as printed; footnoted
  that Mao's own "24-year course" (1921+24) and the 1.2M-member figure both point
  to 1945.
- **Kang Sheng's culpability:** the deaths of the four cadres in the 1937–38
  Soviet purge are well attested; how far Kang personally engineered particular
  cases rests on post-1980 testimony — said so in the note. Kang expelled
  posthumously 1980, ashes removed from Babaoshan.
- Loaded partisan voice (section 3) rendered faithfully; verdicts in the notes.

### Apparatus
- **62 footnotes** (book-wide 265), high density per the standing directive:
  glossed every non-obvious person/place/institution/event at first appearance,
  cross-referenced (not re-noted) figures already covered in ch01/ch02 (Chiang
  Kai-shek, the Central Special Branch, Whampoa, Zhou Enlai, Mao Zedong, He Long,
  Li Kenong, Kang Sheng, Pan Hannian, Li Lisan, the Long March, April 12 coup).
- **+100 glossary rows** (326 referents total): all decided pinyin except 塞先佛
  provisional. Reused decided forms (He Long, Zhou Enlai, Chiang Kai-shek, Kang
  Sheng, Li Kenong, Liu Ding, Mao Zedong, Wang Shiying, Chen Kehan, Luo Qingchang,
  Pan Hannian, Zhang Suzhen, Li Yimang). authority.json confirmed Zhang Xueliang,
  Hu Zongnan, He Long. NOT re-noted (already placed): the recurring figures above.

### Checks (all green)
- parity 125=125; verify_unit numbers 0 unresolved; check_content 340 name
  occurrences, 0 displaced; check_align OK (median 4.55 en/han, no stray);
  qc_entities 0 misses (census: 陈养山×69, 康生×63, 西安×51 …); check_apparatus
  0/0; check_register --ref ch01 within tolerance (em-dash 0.0/1k; dialogue-light,
  judged on narratorial signals).
- data/noise.txt extended: 一〇七 (107th Div numeral misparse), 七尺 (seven-foot
  idiom), 七贤庄 (Qixianzhuang), 一打二拉 (Wang-Ming idiom), 立三路线 (line label),
  120万 / 100万 / 1亿 (arabic+万/亿 magnitude splits, carried in English prose).
  The 四人 count (母子四人) was carried in English ("four in all"), not noised.
- Build: qa_epub PASS (265 refs/bodies/backlinks); **epubcheck 5.1.0 = 0/0/0.**

## Batch 3. Chapter 2, sections 4–5 (ch02s04–s05; PDF 69–92, printed 58–81)

The Red Squad's assassinations (Luo Yinong's informers He Jiaxing, the enemy
agent Dai Bingshi, the spy Chen Weinian, the traitors Bai Xin and Huang Dihong)
and the Chongqing news-agency episode of the "Three Chens."

- **Unit model.** Appended sections 4–5 (two `### ` titles + five `#### ` numbered
  case headings) to the SAME `out/ch02_reading.md`; the whole chapter is one
  builder unit. ch02 reading file now 321 lines; 142 new body/{v} parity lines.
- **data/zh regeneration.** `data/zh/ch02.txt` (sections 1–3) is gitignored and
  did NOT survive the fresh checkout, so whole-`ch02` parity via the default
  config can't be run without regenerating sections 1–3. Per HANDOFF, scoped the
  structural checks to the rebuilt unit: `data/zh/ch02s45.txt` (sections 4–5
  source) + `out/ch02s45_reading.md` (a slice of the appended English) + a scoped
  `data/check_config.b3.json` mapping unit `ch02s45`. The slice is verbatim the
  appended part of `out/ch02_reading.md`. Register/build/qa/epubcheck run on the
  WHOLE chapter file (no zh needed); apparatus anchors validated against the whole
  file.
- **OCR.** Rendered/cropped 69–92 with the ch01/ch02 crop, per-parity bottom
  (recto/even `--bottom 0.945`, verso/odd `--bottom 0.915`, `--running-head
  秘战英雄陈养山`); `ocr_dual.py` for the disagreement filter. `pgrep -c
  tesseract` = 0 after every run. data/zh hand-assembled from corrected OCR +
  every page image read by eye; portrait bio-boxes and photo captions kept OUT of
  data/zh (they are figure captions, in figures.json) so parity stays 1:1.
- **Dropped-tail trap CONFIRMED.** p80 (end of the Chen Weinian episode): OCR
  dropped the paragraph-final short line 冰棒"……; restored from the scan. Every
  page bottom checked against the image.
- **Crop-verified names/readings** (OCR form on the left was WRONG): 刘鼎 Liu Ding
  (OCR 刘易, the "Hart Road hospital" operation), 陈慰年 Chen Weinian (OCR 陈奈年
  throughout — confirmed 慰 on p80), 白鑫 Bai Xin (OCR 白侈/白佬/白奢/白夺/白钨),
  彭湃 Peng Pai (OCR 彭涯/彭涛), 谭余保 Tan Yubao, 红色恐怖队 (OCR 红色信怖队),
  恽代英 Yun Daiying (OCR 履代英), 镣铐 (OCR 镀铸), 袭击 (OCR 黎击), 五卅 (OCR 五州),
  温嗣翔/李鸿混 (given provisional — characters doubtful in the scan).
- **Figures (5; find_figures + eyeballed EVERY page).** find_figures found exactly
  the 5 real plates (p73 Luo Yinong portrait, p81 Peng Pai portrait, p82 the
  puppet Shanghai police HQ building, p89 Chen Yangshan & Chen Kehan, p90 Chen
  Kehan in the 1950s); no line art or document plates elsewhere (OCR ran clean and
  ungarbled on every other page). Portrait bio-boxes translated into the figure
  captions; alt text carries NO straight double quotes.
- **The book's own footnote.** p88 carries the author's numbered footnote ① on
  陈昌 (Chen Chang); reproduced as our translated footnote, attributed to the book.
- **Source errors rendered as printed + footnoted** (do NOT "fix"): the Peng
  Pai / Yang Yin arrest is printed "1928年8月24日" but fell on **24 Aug 1929**
  (execution at Longhua 30 Aug 1929; the book's own later "1929年9月14日" news item
  confirms 1929) — footnoted, corroborated against standard Party-history accounts
  and the Bai Xin-informer record; the "几千万" (tens of millions) slaughtered in
  the 1927–28 white terror is authorial hyperbole (actual toll in the hundreds of
  thousands; CCP membership then under 60,000) — rendered faithfully, footnoted.
- **Bai Xin killing corroborated**: shot by the Red Squad the night of 11 Nov 1929
  at Hehefang off Route Joffre (now Huaihai Middle Rd) — matches the account;
  footnoted.
- **Notes / glossary / figures.** +24 footnotes on ch02 (unit total 130; book-wide
  203). Most section-4/5 subjects (Luo Yinong, Peng Pai and the four martyrs, Bai
  Xin, Dai Bingshi, Chen Weinian, Huang Dihong, Yang Jianhong, Xu Enzeng, Tan
  Shaoliang, Whampoa, Wang Genying, Shen Bao, the Red Squad, the Special Branch,
  the Communist University of the Toilers of the East, the Songhu Garrison Command)
  were ALREADY noted at first appearance in earlier batches — cross-referenced,
  NOT re-noted. +83 glossary rows (226 referents total). NOT re-noted (already
  placed): the traitors as a group, the Special Branch, the Red Squad, Whampoa,
  Sun Yat-sen, the four-martyr group. Minor unfootnoted tier: bit-part bodyguards
  and patrolmen (Han Yunxiu, Lin Hanchen, Wang Baoyuan, Fan Zhengluo, Wang
  Rongchuan), the Red Squad member roll, one-off local officials (Yuan Jiapei,
  Huang Yingqian, Li Honghun, Li Jiemin) — glossary rows only.
- **Style: em-dash discipline.** First English draft over-used the dashed-in
  appositive gloss (failure mode #1: 36 em dashes). Rewrote 25 of them as parens /
  commas / colons / periods per the contract; only the interrupted-speech dash
  ("Ice po—") remains. em-dash rate now 0.1/1k, matching the frozen ch01 reference.
- **Checks (all green).**
  - Parity: ch02s45 142 source = 142 translation.
  - Numbers: `verify_unit.py ch02s45` 142 pairs, 0 unresolved (noise extended:
    10万, 百步穿杨, 百炼成钢, 三民照相馆, 万县, 一九三〇, 零乱; the "four martyrs"
    fixed in English, not noised).
  - Content (displacement): 359 name occurrences, all in the paired paragraph.
  - Alignment: median ratio 4.32 en/han, no pair strays > 2.2x.
  - Entities: `qc_entities` 0 misses.
  - Register vs ch01: within tolerance (contr 14.3/1k, em-dash 0.1/1k, rhythm 0.54).
  - Apparatus: `check_apparatus` 0 failures / 0 warnings (all 130 anchors resolve).
  - Build: qa_epub PASS (203 refs = 203 bodies = 203 backlinks); **epubcheck 5.1.0
    = 0 fatals / 0 errors / 0 warnings**.
- **Tail verified** against the scan (p92): the 1987 recollection closing the
  chapter (50多年前; Chen Kehan; Chen Chang tormented to death 1960, rehabilitated
  1981) reads faithfully.

## Batch 2. Chapter 2, sections 1–3 (ch02s01–s03; PDF 39–68, printed 28–57)

The heart of the book: the birth of the Central Special Branch, the Chen
Yangshan / Bao Junfu double-agent bond, and the Chen Geng / Chen Yangshan
Tianjin operation.

- **Unit model.** The builder reads ONE reading file per chapter
  (`out/ch02_reading.md`); ch02 is split across batches, so this file now holds
  sections 1–3 (three `### ` section titles from book.json) with the chapter's
  three intro paragraphs before section 1. B03 will append sections 4–5 to the
  SAME `out/ch02_reading.md` and `data/zh/ch02.txt`. check_config maps the unit
  id `ch02` to both. 169 source paragraphs, 169 translation paragraphs.
- **OCR.** Rendered/cropped 38–68 with the ch01 crop (recto `--bottom 0.945`,
  verso `--bottom 0.915`, `--running-head 秘战英雄陈养山`); `ocr_dual.py` for the
  disagreement filter. `pgrep -c tesseract` = 0 after every run. data/zh
  hand-assembled from corrected OCR + scans, portrait bio-boxes and photo
  captions kept OUT of data/zh (they are figure captions, translated into
  figures.json) so parity stays 1:1.
- **Crop-verified names/readings** (dual-OCR disagreement + eye on the scan;
  the OCR forms on the left were WRONG): 刘鼎 Liu Ding (OCR 刘易/刘里),
  徐恩曾 Xu Enzeng (徐恩兽/徐四曾), 钱大钧 Qian Dajun (钱大钩), 熊瑾玎 Xiong Jinding
  (能瑾末), 张克侠 Zhang Kexia (张殉侠) and 何基沣 He Jifeng (何基汗); the
  Northwest-Army pair, distinct from the traitor 张克云 Zhang Keyun (张开运),
  鞠华 Ju Hua (misprinted 葛华 once in the narrative; the letter and court address
  read 鞠), 胡鄂公 Hu Egong, 杨登瀛 Yang Dengying, 陈彭年 Chen Pengnian (our agent,
  died on the Long March) vs the traitor 陈慰年 Chen Weinian, 俞同良 Yu Tongliang,
  殷鉴 Yin Jian (曾 is the adverb "had", not part of the name), 周仲英 Zhou Zhongying,
  茅乃功/茅功 (one man, two printed forms). Also restored a silently-dropped tail
  ("于是陈赓让鲍君甫去英捕房活动。", p56) and read 一片荒凉 (not "salt", p64).
- **Source errors rendered as printed + footnoted** (never silently fixed):
  李一氓(又名李坤泰); 李坤泰 is actually the birth name of 李一超/赵一曼, not of
  Li Yimang; 武和景 for 武胡景 (Wu Hujing); Yang Jianhong's death given as suicide
  (自杀, p52) then as execution (被处死, p54); Bao Junfu's own 1951 deposition
  dates his Party tie to 1926 and claims Party membership, going beyond the
  narrative (which treats him throughout as a non-Party agent from 1928); the
  concession car "驶出国民党中央巡捕房" (the concession police were not in fact
  Nationalist-run). Each carries a note.
- **Figures: 15.** Zhou Enlai portrait (p40, missed by find_figures), Pan Hannian
  + Kang Sheng portraits (p41), the "Three Heroes of Longtan" triple photo (p44),
  Chen Shouchang (p45), Bao Junfu (p46), Chen Lifu (p47), the over-street-building
  photo (p51), Xu Enzeng (p52), Huang Molan (p57), the Gu Shunzhang defection
  record; a vertical traditional-character document table, MISSED by find_figures
  (p58), Chen Geng (p61), Wang Genying (p62), Liu Shaobai (p63), Yang Xianzhen
  (p65). Portrait bio-boxes translated as the figure caption. The chapter-opener
  frontispiece (p38, two soldiers) was SKIPPED, matching the ch01 decision to
  omit opener photos.
- **Notes: 106** (book-wide continuous total now 179). Matches the ch01 density
  directive: every non-obvious person/place/institution/event/period-term glossed
  at first appearance, each note saying more than the name, with fact-check
  verdicts where a claim is checkable (Kang Sheng's later persecutions, Pan
  Hannian's 1955 fall, the source errors above). Already-noted ch01 recurring
  subjects NOT re-noted: Zhou Enlai, Chen Geng, Bao Junfu, Gu Shunzhang, Ren
  Bishi, Li Weihan, Qu Qiubai, Li Lisan, Chiang Kai-shek, Wang Jingwei, the May
  Thirtieth / May Fourth movements, the August 7 Conference, the Nanchang
  Uprising, Whampoa, Zhang Zuolin, the Northern Expedition.
- **Glossary: +102 rows** (143 referents total), all with `section` fields.
  Decided renderings fed to authority.json at completion.
- **Checks, all green.** parity 169=169; check_numbers 0 unresolved (noise
  extended: 四川, 20世纪, `[0-9]0年代`, 十足, 涕零, 一二八, 九一八, 两家话, 第二天);
  qc_entities 0 misses; check_content 0 displaced (fixed 3 real/redundant drops:
  Shanghai ×2, Zhang Daofan; and renamed the colliding glossary key
  中国青年 → 《中国青年》 so it no longer matches inside 中国青年团); check_align OK
  (median 4.54 en/han, no strays); check_apparatus 0/0; check_register within
  tolerance of the frozen ch01 reference (em-dash 0.1/1k vs ref 0.6; dialogue
  contraction metric noisy per the reportage caveat); check_style_freshness all
  layers FRESH. verify_unit ch02 green. qa_epub PASS; **epubcheck 5.1.0 =
  0 fatals / 0 errors / 0 warnings.**
- **Builder patch (do-not-revert).** `build_reading_epub.sec_nav`: the EPUB nav
  now OMITS pending (untranslated) sections/subsections instead of linking them
  to the bare chapter file. A partially-translated chapter otherwise put a link
  to the top of the document AFTER a link to a later anchor in the same file
  (epubcheck NAV-011, toc not in reading order), and a `<span>` leaf is invalid
  in a toc nav (RSC-005). The contents.xhtml PAGE still shows the whole shape,
  pending entries and all. Exposed by ch02 being the first chapter translated a
  batch at a time.
- **Figure-alt hazard fixed in data, worth knowing:** a figure `alt` string is
  written into an `alt="..."` attribute with `esc(quote=False)`, so a straight
  double-quote inside alt text breaks the attribute and makes the XHTML
  unparseable (epubcheck RSC-016 fatal, then a cascade of phantom "missing
  anchor" reports). Keep figure `alt` free of `"` (use single quotes); caption
  text may keep double quotes (it is element content, typographized).

## Setup / Survey (this session)

- **Book.** 秘战英雄陈养山, by 姚华飞 (Yao Huafei). CCP Party History Press
  (中共党史出版社), Beijing, 2018.4. ISBN 978-7-5098-4587-5. CIP subject:
  陈养山 (1906–1991), biography. 227,000 characters; 15 print sheets; 33.00 RMB.
  Biography volume of the 隐蔽战线春秋书系 (Hidden Front Chronicles) series.
- **Source.** Image-only PDF (`source.pdf`, 99 MB, 243 PDF pages), DuXiu/SuperStar
  digitisation via Anna's Archive. No text layer. PDF p243 is an Anna's Archive
  metadata leaf, NOT book content (reports 231 main book pages). PyMuPDF renders
  fine; no bookmarks (`get_toc()` empty), so structure was recovered from the
  printed TOC (目录, PDF p9–11) and verified opener-by-opener against the scan.
- **Script / orientation.** Modern SIMPLIFIED Chinese, single column, horizontal
  (left-to-right). Clean digital typeface — OCR will be easy (chi_sim, --psm 6).
  This is NOT an old letterpress scan; most of CLAUDE.md's furniture/orientation
  traps are mild here.
- **Offset.** printed = pdf − 11 for the whole body. Verified at printed 2
  (=PDF 13), 27 (=PDF 38), 231 (=PDF 242). Constant — no unpaginated plates in
  the body, so no offset drift.
- **Front matter runs a SECOND sequence.** Cover p1; series-title verso p2 (lists
  the 10-volume 传记卷 set); title page p3; CIP/copyright p4; frontispiece portrait
  of Chen (陈养山 1906–1991) p5; jacket blurb (内容提要) p6; **series foreword
  (丛书前言) by 章百家 (Zhang Baijia)** pp.7–8 on its OWN folio sequence
  (folios 1–2); TOC (目录) pp.9–11. Body (Chapter 1, printed 1) begins at PDF p12.
- **Page furniture.** Running head/foot with folio + running title present; exact
  top/bottom position appears to vary recto vs verso (verso title+folio seen at
  BOTTOM on p13; a running head seen at TOP on p242). MEASURE precisely in Batch 1
  per `ocr_crop.py` and strip textually after OCR. Chapter-opener rectos carry a
  PHOTOGRAPH above the heading (e.g. p38 = Chapter 2) — capture as figures per batch.
- **Structure.** 6 chapters / 29 sections; back matter = Appendix I 陈养山生平 (214),
  II 陈养山遗作 (217), III 陈养山年谱 (223), 参考文献 References (228), 后记
  Afterword (230–231). All folios verified. Full structure in `book.json`.
  TOC discrepancy flagged: the series foreword is not in the printed TOC
  (see `book.json` toc_flags_open).
- **Metadata (Step 0a).** Set in `book.json`; series "Winston Translations",
  index 10. `compose_style.py` run → STYLE.md (zh / nonfiction / popular
  narrative-history voice); STYLE.local.md seeded.
- **Skeleton EPUB.** `build_reading_epub.py` → out/chen-yangshan.epub (0/12
  translated). `qa_epub.py` PASS. **epubcheck 5.1.0: 0 errors / 0 warnings.**
- **Environment.** tesseract chi_sim + chi_tra (sim/trad, incl. vert) installed.
  PaddleOCR NOT installed (expected) → dual-engine substitute is `ocr_dual.py`.
  epubcheck present at /tmp/epubcheck-5.1.0/epubcheck.jar. Java via setup.
- **Branch.** All work consolidated on `claude/chen-yangshan` per commissioner
  and CLAUDE.md rule 2. Stray harness branch `claude/pdf-source-review-ieeufv`
  left untouched (not deleted).

### Cross-book connections to watch (from COLLECTION.md / authority.json)

This book sits in the shelf's core world (中央特科 / the hidden front). Consult
`authority.json` BEFORE romanising: 周恩来 Zhou Enlai, 顾顺章 Gu Shunzhang
(author of shelf book 2), 中央特科 Central Special Branch/Teke, 李克农 Li Kenong,
康生 Kang Sheng, 贺龙 He Long, 恽代英 Yun Daiying, 鲍君甫 Bao Junfu, 军统 (reconcile
the three-way drift noted in COLLECTION.md before use).

## B01 = Chapter 1 "Seeking the Truth, Turning to Revolution" (ch01s01–s05), PDF 12–37, printed 1–26

Status: translated, apparatus complete, EPUB built green; voice gate in progress.

### OCR / page geometry (measured this batch — DO NOT REVERT)
- **Crop.** `ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985
  --top 0.08 --running-head "秘战英雄陈养山"`, with a **recto/verso split bottom**:
  RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd) `--bottom 0.915`.
- **Mirrored furniture.** RECTO (printed odd) carries the running head + folio at
  the TOP (cut by top=0.08); VERSO (printed even) carries folio + book-title foot
  at the BOTTOM. The verso foot band (~0.925–0.953) overlaps recto body text
  (~0.94), so recto is cropped generous and the verso foot is excluded
  geometrically (bottom 0.915; body ends by ~0.910).
- **strip_runfoot patched** (do-not-revert) to remove the verso book-title foot
  textually as a backstop: exact title-tail match, plus any LAST line containing
  a `|` (the ▶ marker + decorative rules OCR as pipe noise; this book's body
  prose never contains `|`).
- **SILENT OCR-LOSS class found and worked around.** tesseract psm6/psm4/psm11 on
  the full page-crop DROP an isolated paragraph-final SHORT line (both at page
  bottom above the foot AND mid-page). Confirmed losses recovered from the scan:
  p13 "逐渐衰败，生活贫寒。" and p15 "为恐慌。". A psm11 cross-pass over the whole
  batch confirmed these were the ONLY two dropped tails. Lesson for later batches:
  a paragraph whose OCR ends without sentence-final punctuation before a blank is
  a dropped-tail suspect; verify against the scan. `data/zh/ch01.txt` was
  hand-assembled from the corrected OCR + scans for this reason (a third of the
  pages carry photos with text wrap, which the indent/assemble geometry cannot
  handle here — `ocr_crop.folio_present` is also absent, so indents.py is unused
  this book).
- ocr_dual.py second read run (psm4 vs psm6); crop-verified readings recorded in
  `data/ocr_fixes_notes.md` (military-commission names, Chen Geng, the Zhou poem,
  the Longhua martyr, classical Cao E names).

### Figures (10; eyeballed every page — find_figures MISSED p16, false-negative on
line-thin calligraphy p18)
- p12/p19 portrait (same photo; placed ONCE, at the p19 clerk-portrait context,
  caption "…Hankou, 1924"); p16 《中国青年》; p17 Yun Daiying; p18 Zhou Enlai's
  1953 calligraphy of Yun's prison poem (hand-cropped; also rendered as {p} verse
  in the body); p24 Ren Bishi; p29 Shanghai Bund (source prose caption); p31 Wang
  Yifei; p32 Chen in Ningbo; p33 April-12 massacre (source prose caption); p34
  He Long. All with real `alt`. Source photo captions translated into figures.json;
  they are NOT body paragraphs (excluded from data/zh, so parity stays 1:1).

### Translation & apparatus
- `out/ch01_reading.md`: 141 body paragraphs + 5 section headings, one paragraph
  per source line. Block quotes as `{v}`; the prison poem as `{p}` verse.
- notes.json: 23 footnotes (reader = Westerner, no China background): geography,
  jinshi, 曹娥/水经注, 实业救国, May Fourth, 二七/li, 中国青年, Youth League,
  Ren Bishi, Lenin issue, 楚囚 allusion + poem-variant, May Thirtieth /
  International Settlement / SMC / McEuen, Northern Expedition, April 12 / white
  terror, Nanchang Uprising, silver dollars, Green Gang, Central Special Branch,
  Gu Shunzhang. Continuous, all anchors verbatim.
- glossary.json: 41 rows in sections people/organizations/places/events; 3
  principals (Chen, Yun, He Long) → Principal Characters front page. Reused
  authority.json agreed forms (He Long, Zhou Enlai, Chiang Kai-shek, Kuomintang,
  Central Special Branch, Wuhan/Hankou/Shanghai, Northern Expedition, etc.).

### Checks (all green)
- check_numbers --noise: **0 unresolved** (141 pairs). Real drops fixed to carry
  the value (三人, 6时, 3时45分, and large counts written as digits 200,000/50,000/
  250,000/100,000). Noise added for idioms/names/date-labels (三罢, 万岁, 百官,
  百姓, 李立三, 九江, 矢田七太郎, 四出, 一分为二, 二话, 百年, 四一二, and the
  X多万 magnitude approximations with English rendering noted).
- parity 141=141; anchors 23 ok; qc_entities 0 misses (census: 陈养山×131 …);
  check_content OK (281 name occurrences all in the paired paragraph);
  check_apparatus 0/0.
- **check_align: 1 expected flag** — pair 33, poem line 2 (故人生死各千秋。, 7
  hanzi) expands ~10x in English. High ratio = expansion, not missing text; a
  legitimate verse exception, not a defect.
- Build: qa_epub PASS; **epubcheck 5.1.0 = 0 errors / 0 warnings.**

### Tooling patches (do-not-revert)
- `ocr_crop.strip_runfoot`: verso book-title / pipe-foot removal (above).
- `apparatus_merge.py`: glossary now merges into SECTIONS (`"section"` field on a
  row, default terms) instead of flat top-level keys — the flat form crashed the
  builder's render_glossary and made qc_entities vacuous.
- `check_content.name_map`: skip `_`-prefixed metadata keys (e.g. `_about`),
  which are strings, not sections.

### Register reference
On voice-gate approval, ch01 becomes the FROZEN register reference
(`check_register.py --ref out/ch01_reading.md` for every later batch).

### Voice gate (Step 0c)
- **HUMAN GATE outcome:** commissioner approved the voice, and asked for much
  higher footnote density ("explain the names and places and all that... just in
  case there's a gap," but no padding). Applied: ch01 notes 24 -> **73** (glossed
  every non-obvious person/place/institution/event/term at first appearance,
  each saying more than the name). Recorded as a standing note-density RULE in
  STYLE.local.md for all future batches. Rebuilt: qa PASS, epubcheck 0/0, all
  73 anchors resolve. Awaiting confirmation, then freeze as register reference.
- **Blind-critique loop complete: 3 rounds, converging 30 -> 24 -> 14 findings**
  (round 3: "largely clean, reads as fluent English"). Each round: a fully
  context-blind FRESH reader (no source, no STYLE, no project) via
  voice_gate_critique.py; all fixes applied and re-verified against the source;
  all gates re-run green after each round. STYLE.local.md evolved with 8
  RULE/WHY/FIX/CHECK entries (heroic-formula rationing, 成语-as-calque,
  water/storm imagery, editorial-adjective/coinage, fronted-inversion, classical-
  tag framing, impression-formula + metaphor budget, no clefts/antique
  light-verbs) + a 7-item word-level ledger. Archived under review/voice_gate/.
  NEXT: human voice/notes/formatting gate, then freeze ch01 as register reference.
- Regression note: setup.sh "CHECKER REGRESSION TESTS FAILED" is a benign
  artifact — the kickoff_guard template-stand-down fixture expects a placeholder
  HANDOFF.md, but ours is a real book handoff, so the hook correctly refuses to
  stand down. All translation checkers (check_numbers, builder, compose_style)
  pass.

## Batch 7 — Chapter 5 (ch05, PDF 172-204, printed 161-193) — COMPLETE

**Scope.** Whole of Chapter 5, "Anecdotes from Around the Founding of New China,"
all four sections in one unit `ch05` (own reading file + `data/zh/ch05.txt`). Done
end to end. Post-1949 years: the Xi'an takeover and the first national public
security conference; the Nanjing years and the Huang Kai interrogation (the Wu Hao
forgery saga); the deep Li Kenong friendship and the 1961 Shanghai materials trip;
principle and frugality; and two appended 1961 letters (Li Kenong to the leadership,
Yang Shangkun's reply).

**Counts.** 180 body paragraphs (incl. 23 `{v}` set-off document lines + 1 `{p}`
verse line), 4 `###` sections + 3 `####` (附 appendix + the two letter titles),
47 footnotes (book-wide now 387), 101 new glossary rows (677 referents), 17 figures.

**Pipeline / gates — all green.**
- render 172-204; OCR ocr_crop (chi_sim, psm6, left .045/right .985/top .08,
  recto bottom .945 / verso .915 per page) + ocr_dual; `pgrep -c tesseract` = 0.
- parity 180=180; headings OK; `check_apparatus` 0/0; `check_content --config
  data/check_config.ch05.json` aligned (445 name occ, 0 displaced); `qc_entities`
  0 misses; `check_numbers --noise` 0 unresolved; `check_align` 1 benign ratio
  outlier (`布礼` -> "Bolshevik greetings," a 2-char formal closing); `verify_unit`
  numbers 0 / anchors 47; `check_register --ref out/ch01_reading.md` within
  tolerance (contr 4.1/1k, em-dash 2.9/1k, roster-heavy chapter, little dialogue).
- build cumulative EPUB (5/12 translated, 387 notes); `qa_epub` PASS; epubcheck
  0 fatals / 0 errors / 0 warnings.

**Silent OCR-loss caught (confirmed again).** p200 (printed 189): tesseract
dropped the paragraph-final "我贺龙" from He Long's quoted line "你们看不起他,就是
看不起我贺龙" — restored from the scan. Every page bottom and every long paragraph
tail verified against the scan; the two appended letters (chapter tail) verified
against p203-204.

**Source errors rendered as printed + footnoted (do NOT "fix").**
- printed 165: 中央直辖市**西安**部门 — an evident misprint for 公安 (public
  security); rendered as printed ("the Xi'an departments") with a footnote carrying
  the correction (the meeting was the national **public security** work conference).
- printed 189/190: the Huzhou Chinese-medicine relative is 堂兄 (paternal cousin)
  twice, then 妻兄 (wife's brother) once — rendered consistently as "his cousin"
  (also agreeing with the later 堂嫂 "cousin's wife"), with a footnote flagging the
  slip.
- 事务所法 大马路四十号六楼五号 (printed 172): garbled law-office letterhead;
  rendered "The Law Office. No. 40 Damalu, Sixth Floor, Room 5."

**Crop-verified oddities that ARE the source (not OCR).** printed 176
"一网打尽陈养山党中央机关" (rendered "net Chen Yangshan and the Party Central organs
in a single sweep"); printed 179 "为寻陈养山出路" (rendered "looking to Chen Yangshan
for a way out"). Both eyeballed at magnification; the author over-inserts the
subject's name.

**Fact-check verdicts placed in notes (not the text).** the CIA-declared-a-holiday
claim for Li Kenong's death is flagged as legend, not verifiable fact; the Wu Hao /
Zhou Shaoshan forgery-and-rebuttal is corroborated in outline; Shi Liangcai's
reluctance fits the record but the private exchanges cannot be confirmed.

**NOT re-noted (already placed in ch01-04; cross-referenced instead):** Li Kenong,
Zhou Enlai, He Long, Peng Dehuai, Mao Zedong, Kang Sheng, Chiang Kai-shek, Hu Zongnan,
Chen Geng, Pan Hannian, Gu Shunzhang, Qian Zhuangfei, Bao Junfu, Chen Lifu, Hu Di,
Chen Yun, Xu Enzeng, Ren Bishi, Deng Yingchao, Zhang Xueliang, Wang Jingwei, Wang Ming,
Central Special Branch, Central Intelligence Department, Social Affairs Department,
Xi'an Incident, Jin-Sui Border Region, Red Squad, Zhongtong/Central Statistics,
Zaoyuan, Seventh Congress, April 12 coup, August 7 Conference, Rectification,
Zhang Guotao, Longhua, Peng Pai, Cultural Revolution, Gang of Four, First Field Army,
Ningxia (the campaign/place noted; ch06 will carry the persecution).

**data/noise.txt** — added 8 rules (二三十年代, 20多岁, 四马路 Simalu, idioms
千头万绪 / 百忙 / 百出, enumerators 一则/二则, name 丁老二). None are quantities.

**Tooling — no reverts.** No script changes this batch; the ch01-04 crop, the
apparatus_merge section-field mechanism, and the {v}/### /#### mirroring all held.

## Batch 8 — Chapter 6 (ch06, PDF 205-224, printed 194-213) — COMPLETE

**Scope.** Whole of Chapter 6, "A Loyal Heart Revealed in a Time of Injustice,"
all four sections in one unit `ch06` (own reading file + `data/zh/ch06.txt`). Done
end to end. The persecution years: the 1958 "anti-Party clique" frame-up of the
Ministry of Justice Party group; twenty years of disgrace; ten years exiled in
Ningxia through the Cultural Revolution; full rehabilitation in 1983; and the last
working years, writings, and death (1991), closing with the book's peroration and
four calligraphic tributes. 67 body paragraphs, 4 `###` section headings.

**Pipeline / gates (all green).**
- render 205-224 (PyMuPDF 300 dpi); OCR per-page with the ch01-05 crop
  (`--lang chi_sim --psm 6 --left 0.045 --right 0.985 --top 0.08`, recto/verso
  split bottom 0.945/0.915), backgrounded; `pgrep -c tesseract` 0 after.
- Every page read by eye at magnification; `data/zh/ch06.txt` hand-assembled one
  source paragraph per line, portrait/photo captions kept OUT (into figures.json).
- parity 67 = 67 (`check_structure`), headings OK.
- numbers 0 unresolved (`check_numbers --noise`); 5 CJK/era magnitude idioms added
  to `data/noise.txt` (十余万 "more than a hundred thousand words", 100多万 "more
  than a million words", 三十年代 "the 1930s", 九旬 "close on ninety", 亿万
  "hundreds of millions") — all magnitudes carried in the English prose.
- content aligned, 155 name occurrences all in the paired paragraph
  (`check_content --config data/check_config.ch06.json`).
- entity survival 0 misses (`qc_entities` on the bilingual QC file).
- align OK, median 4.55 en/han, no pair strays > 2.2x (`check_align`).
- apparatus 0/0 (`check_apparatus`); 23 footnotes (book-wide 410); 40 new glossary
  rows (716 referents).
- 14 figures cropped to `data/figs/` (photos + the four end-of-chapter calligraphy
  tributes; find_figures misses calligraphy, cropped by eye); alt text carries no
  straight double quotes.
- build OK (6 of 12 chapters, 410 notes); `qa_epub` PASS (410 ref/body/backlink);
  `check_register --ref out/ch01_reading.md` within tolerance (little dialogue,
  narratorial signals only); epubcheck 0 fatals / 0 errors / 0 warnings.

**Source error rendered as printed + footnoted (do NOT "fix").** printed 202:
中共**十届**六中全会 (twice) — the Resolution on Party History was in fact adopted
at the Sixth Plenary Session of the **Eleventh** Central Committee (June 1981);
there was no such Tenth-CC plenum. Crop-verified both occurrences; rendered as
printed ("the Sixth Plenary Session of the Tenth Central Committee") with a
footnote, and the book's own later, correct "Third Plenary Session of the Eleventh
Central Committee" makes the slip plain.

**Two sons (consistent with ch05).** 长子建宇 = eldest son Chen Jianyu (already
decided); 幼子震宇 = youngest son Chen Zhenyu (glossary key 震宇 → "Zhenyu"), who
suffered a mental breakdown after the father's fall (printed 197).

**Fact-check verdicts placed in notes (not the text).** the 1931 Longhua arrests /
"24 comrades" — Chen's charge that the Wang Ming leadership deliberately let them
be taken is the survivors' bitter factional reading; historians link the arrests to
the internal fight over Wang Ming's line but do not all accept a deliberate
betrayal — flagged in the note. Dong Biwu's dissent from the "anti-Party clique"
finding corroborated. The Anti-Rightist over-extension, Seven Thousand Cadres
Conference, Reflection Institute, Wang Jingwei collaboration, Fan Zhongyan maxim,
Rou Shi martyrdom — all corroborated in the notes.

**NEW decided renderings (feed to authority.json at completion).** People: Zheng
Shaowen, Wang Huai'an, Wang Ruqi, Wang Yuechen, Liu Shangzhi, Tang Jinshi, Song
Zicheng, Luo Zhiguang, Dong Biwu, Kang Jianmin, Huo Shilian, Ma Xin, Ding Yimin,
Pei Zhouyu, Jin Zhaodian, Qu Rixin, Feng Jinchen, Zheng Xiaoxian, Gu Yizhi, Rou Shi,
He Mengxiong, Li Qiushi, Wu Huai'e, Xiao Taihuang, He Changzhi, He Zhihua, Hu Weihua,
Jiang An, Zhou Jianjie, Rong Xuan, Yu Ping, Huang Huoqing, Zhang Su, Li Yimang, Ling
Yun. Places: Ningxia, Yinchuan, Ninghai County, Mengzhou. Orgs/events: the Reflection
Institute, the College of Foreign Affairs, the Central Political-Legal Group, the
Production Command, the Revolutionary Committee, the Anti-Rightist Campaign, the Seven
Thousand Cadres Conference, the Five-Antis.

**NOT re-noted (already placed in ch01-05; cross-referenced instead):** Li Kenong,
Chen Geng, Zhou Enlai, Deng Xiaoping, Yang Shangkun, Peng Zhen, Kang Sheng, Jiang
Qing, Chen Yun, Wang Ming, Gu Shunzhang, Bao Junfu, Peng Pai, Luo Yinong, Bai Xin,
He Jiaxing, Wu Hujing, Li Qiang, Luo Qingchang, Yun Daiying, the Central Special
Branch, the Central Investigation Department, the Ministries of Public Security and
Justice, the Cultural Revolution, the Gang of Four, the "anti-Party clique" case,
Ningxia (place noted in ch05), the Three-Antis, the Eighth National Congress,
Longhua, the White Terror, "national salvation through industry."

**Tooling — no reverts.** No script changes this batch; the ch01-05 crop, the
apparatus_merge section-field mechanism, the {v}/### mirroring, and the data/zh
regeneration protocol all held. ch06 has NO {v}/{p} set-off blocks (the letter and
verdict quotations are inline within narrative paragraphs).

================================================================================
## Batch 9 (B09): FRONT + BACK MATTER (translation) — ch00, ch07, ch08, ch09, ch10

Five framing units translated end to end. All per-unit gates green; cumulative
EPUB rebuilt (11 of 12 units; only ch11 afterword pending), qa_epub PASS,
epubcheck 0/0/0, register within tolerance of the frozen ch01 reference for every
unit (all dialogue-quiet, judged on the narratorial signals, which held).

### Units
- **ch00 = 丛书前言 "Foreword to the Series"** (Zhang Baijia), PDF 7-8, front folios
  1-2. 6 paragraphs (byline + 4 body + signature), 4 notes. A signed editorial
  preface to the whole Hidden Front Chronicles series; the main NEW note targets
  were Zhang Baijia himself, the series, Xu Xiangqian, and the New Democratic
  Revolution.
- **ch07 = 附录一 陈养山生平 "Chen Yangshan: A Life"**, PDF 225-227 (printed 214-216).
  14 paragraphs, 6 notes. Chen's official obituary (悼词), rendered in a dignified
  natural-English obituary register with the heroic set-phrases rationed. Notes:
  the obituary genre; the rehabilitation-date discrepancy (obituary/年谱 date the
  full clearing to the 1978 Third Plenum, ch06 places the thorough reversal in
  1983); "one central task, two basic points"; the Four Cardinal Principles; the
  Ten-Year Program / Eighth Five-Year Plan; Jiang Zemin.
- **ch08 = 附录二 陈养山遗作 "Chen Yangshan's Posthumous Writings"**, PDF 228-233
  (printed 217-222). Four sub-parts rendered as running prose (the layout is
  ordinary body text, not set-off blocks), 38 paragraphs, 5 notes, 3 figures.
  (1) On Bao Junfu (Chen's plainer first-person retelling of the ch02 story);
  (2) his 1988 letter to the Central Organization Department and the Ministry of
  State Security, with typeset transcription and appended profiles of the four
  Special Branch comrades Kang Sheng framed; (3) the 36-item outline for the
  memoir he did not live to write, plus the son Cheng Jianyu's editorial note
  (rendered as reading text, not apparatus, to keep the footnotes translator-only);
  (4) his thirteen household precepts. Voice sheet honoured: Chen's own writing
  kept plain and dry.
- **ch09 = 附录三 陈养山年谱 "A Chronology of Chen Yangshan's Life"**, PDF 234-238
  (printed 223-227). 76 paragraphs (intro + one year-label line and one entry
  paragraph per year, multi-entry years kept as separate paragraphs), 2 notes.
  Numbers-dense: check_numbers ran clean at 76/76 with no unresolved; every year
  label carries its year and age, checked. Re-treads noted ground almost entirely
  (Feb 7 strike, Wang Yifei, College of Foreign Affairs all already noted), so
  notes taper to a heading orientation note and a cover-names note.
- **ch10 = 参考文献 "References"**, PDF 239-240 (printed 228-229). 42 citations,
  1 note. Each citation rendered as: author(s), romanized title in italics, an
  English gloss of the title in brackets, publisher (Englished) and year as
  printed. No bibliographic detail invented. The one note flags the author's own
  self-citations and the family/memorial sources.

### Checks run (per unit, unit-scoped configs)
verify_unit (parity + numbers + anchors), check_structure/check_content
(--config data/check_config.<id>.json), make_bilingual then qc_entities,
check_numbers --noise data/noise.txt, check_align, check_apparatus (whole
notes.json), check_register --ref out/ch01_reading.md. Parity: ch00 6=6, ch07
14=14, ch08 38=38, ch09 76=76, ch10 42=42. Entities 0 misses each; content
alignment OK each; align OK each; numbers 0 unresolved each. Book-wide notes now
428; glossary 718 referents.

### noise.txt additions (all name/lexical, no real quantity masked)
章百家 (Zhang Baijia, 百 a name component); 十万余 ("more than a hundred thousand
words", magnitude carried in English); 百花 (Baihua Press); 大百科全书 (Encyclopedia
of China Publishing House, 百科 lexical).

### Figures (4)
Frontispiece portrait p0005-f1.png -> ch07 (before the obituary's first line);
three handwriting facsimiles from Appendix II -> ch08, manuscript-first before
each typeset piece: the 1988 letter (p0230-f1.png), the memoir outline
(p0232-f1.png), the household precepts (p0233-f1.png). Captions note the source
provenance of dates; alt text carries no straight double quotes. Portrait
bio-boxes and captions kept out of data/zh so parity stayed 1:1.

### NEW decided renderings (feed to authority.json at completion)
People: Zhang Baijia; Cheng Jianyu (程建宇, eldest son, family's original surname
Cheng); Wu Huairang (武怀让, original name of Wu Hujing); Hou Zhi; He Changchi
(贺长炽, the appendix's primary form for the comrade the glossary fixes as He
Changzhi 贺昌之); Cao Yi'ou (Kang Sheng's wife); Liu Bowen; Wang Yifei; Zhang
Xiushan. Chen's underground cover names: Chen Yingzhou (陈英舟), Chen Deqing
(陈德清), Gao Junshi (高君实), Lao Wang (老王), with Chen Zhongying and Chen Mingjun
already decided. Bibliography authors were rendered in pinyin but NOT glossaried
(one-off, not narrative cast).

### FLAGS FOR THE B10 WHOLE-BOOK RECONCILE
1. **The 1988 letter appears twice.** ch03s03 quotes it as a {v} block ("Chen
   Yangshan's Letter to the Central Organization Department"); ch08 (二) reproduces
   it as the posthumous document. Both renderings are faithful to their own source
   layout (ch03 split the body into two paragraphs with an inline closing; the
   appendix on printed 220 prints one body paragraph and splits 致 / 敬礼！ onto two
   lines, which ch08 mirrors), but the wording diverges. A reconcile pass should
   decide whether to harmonize the two English renderings of the one document.
2. **Xiao Shouhuang vs Xiao Taihuang — a SOURCE variant, not an error.** The
   appendix (printed 220) and ch03 print 肖寿煌 (Xiao Shouhuang), crop-verified;
   ch06 prints 肖太煌 (Xiao Taihuang), the B08 decided form. The source itself names
   this murdered comrade two ways. Render each as printed; B10 should add a note at
   one appearance flagging the variant, rather than silently harmonizing.
3. **Rehabilitation timeline.** obituary + 年谱 date the full clearing to the 1978
   Third Plenum; ch06 (case papers) places the thorough reversal in 1983 (1978
   quashed the "anti-Party clique" verdict but left a residual "Right deviation"
   finding, negated only in 1983). Noted in ch07; consistent across the batch.

### Tail verification (rule 4 corollary)
Every unit's final paragraph read against the scan at transcription: ch00
signature line (printed 2), ch07 "lives forever in our hearts" (printed 216),
ch08 precept 13 (printed 222), ch09 the 1989 death entry (printed 227), ch10
citation 42 (printed 229). No dropped tails.

### Tooling — no reverts
No script changes. The ch01-06 OCR crop held for the back matter; the front-matter
pages (7-8) needed a different crop (no top running head, folios and running foot
below), handled per-page with --top 0.05 and --bottom 0.90-0.92. apparatus_merge
section-field mechanism, {v}/### mirroring, and the data/zh regeneration protocol
all held.

================================================================================
## Batch 10 (B10): AFTERWORD (ch11) + WHOLE-BOOK CLOSE -- BOOK COMPLETE

The light final batch. ch11 translated end to end; then the whole-book close
(reconcile sweep, cover, term ledger, authority.json, deep audit, COMPLETION).
The book is now COMPLETE: 12 of 12 units, 432 notes, 78 figures, 731 referents;
qa_epub PASS, epubcheck 0/0/0, title page reads COMPLETE.

### ch11 = 后记 "Afterword" (Yao Huafei), PDF 241-242 (printed 230-231)
- 11 body paragraphs (9 running-prose paras + 2 signature lines), no {v}. The
  author's own plain, warm voice (voice sheet honoured; heroic formulas
  rationed). Rendered one paragraph per source line; data/zh/ch11.txt +
  out/ch11_reading.md; added ch11 to data/check_config.json AND scoped
  data/check_config.ch11.json.
- render 241-242 @300dpi (PyMuPDF); the pages are a clean digital typeface. Read
  BOTH page images by eye and crop-verified every name against the scan at
  magnification: interviewees 程建宇 Cheng Jianyu / 秦杰 Qin Jie / 金楚宣 Jin Chuxuan;
  acknowledgements 凌云 Ling Yun, 刘复之 Liu Fuzhi, 《谍海瞭望》 Espionage Watch,
  董沪英 Dong Huying, 姜岸 Jiang An, 何岳隽 He Yuejun, 管志华 Guan Zhihua (People's
  Daily senior editor), wife 陈大文 Chen Dawen, twin granddaughters 妞妞/妮妮
  Niuniu/Nini (13). Numbers preserved: 16年, 2006年10月7日, 六易其稿, 13周岁,
  2017年6月18日. Tail (signature) verified against the scan.
- 2 notes (taper): the 2006 first edition 《隐蔽战线福将陈养山传奇》 (China Friendship
  Publishing, Chen's centenary) + 福将 gloss, anchored on "October 7, 2006"; and a
  name-gloss on Espionage Watch. 13 new glossary rows (Yao Huafei, the five new
  helpers/family, People's Daily, the two publishers/bureau, the 2006 title).
- Gates: parity 11=11; check_numbers 0 unresolved; check_content 28 name occ all
  placed; qc_entities 0 misses; check_align 4.68 en/han; check_apparatus 0/0;
  verify_unit anchors 2 ok; check_register within tolerance (dialogue-quiet;
  em-dash 0.0/1k, rhythm 0.47 vs ref 0.50).

### Whole-book reconciliation sweep (check 12)
- check_reconcile: **epithet drift 0**; 704/731 decided forms present in prose
  (the rest caption-/note-only or article-prefix artifacts, sampled and
  confirmed legitimate); spelling locale 0 British / 438 American.
- Decided-rendering grep (~20 core): no wrong forms surviving. "Canton" x2 =
  "a Cantonese" (demonym); "Teke" x1 = romanized book title (use-vs-mention);
  "Peking" x1 = "Peking Union Medical College Hospital" (institution name).
- THREE B09 FLAGS resolved:
  1. **1988 letter twice** (ch03s03 {v} vs ch08(二)): both faithful transcriptions
     of one manuscript (the ch08 facsimile confirms), differing only in wording +
     layout; NOT glossary/term drift. Decision: keep both (forcing them identical
     would edit frozen gate-passed chapters for no fidelity gain); added ONE
     cross-reference note at the ch08 appendix letter.
  2. **Xiao Shouhuang (肖寿煌) vs Xiao Taihuang (肖太煌)**: source variant for one
     murdered comrade (ch03/ch08 vs ch06). Added ONE note at the ch06 "Xiao
     Taihuang" occurrence flagging the variant; each left as printed.
  3. **Rehabilitation timeline (1978 vs 1983)**: CONSISTENT (1978 quashed the
     "anti-Party clique" verdict but left a residual "Right deviation" finding,
     negated only in 1983); explained in ch06, discrepancy noted in ch07. No change.
- **Cross-book authority reconcile (fed to authority.json):** of this book's
  glossary vs the 194-entry ledger, 44 agreed (chen-yangshan appended) + 1
  variant registered (巡捕房 "the concession police"). ONE wrong form found and
  FIXED: 霞飞路 "Route Joffre" -> shelf-agreed, historically correct **"Avenue
  Joffre"** (5 books, status agreed) -- corrected in ch02 prose (2x), the note
  anchor + body, and the glossary; rebuilt + re-validated. ONE homograph kept
  separate: 中原 = "Nakahara" (Japanese general's surname here), NOT the shelf's
  "Central Plains". authority.json now cites chen-yangshan on 45 entries.

### SILENT FIGURE LOSS found and fixed (figure integrity sweep)
- A crops-on-disk vs figures.json cross-check caught 15 MISSING ch02 figures
  (sections 1-3: Zhou Enlai p40, Pan Hannian/Kang Sheng p41, Three Heroes p44,
  Chen Shouchang p45, Bao Junfu p46, Chen Lifu p47, over-street p51, Xu Enzeng
  p52, Huang Molan p57, Gu Shunzhang doc p58, Chen Geng p61, Wang Genying p62,
  Liu Shaobai p63, Yang Xianzhen p65). ROOT CAUSE: apparatus_merge REPLACES a
  unit's figures wholesale; B03 (ch02 s4-5) overwrote B02's 15 (ch02 s1-3) with
  its 5. ch02 was the ONLY chapter split across batches, so the only casualty.
  The crops + original alt/captions were recovered from the B02 commit
  (8ea14e2:figures.json) and re-merged: ch02 5 -> 20; book 63 -> 78 figures. The
  build (which refuses an unplaced figure anchor) validated all 20 anchors.
  Post-fix sweep: 0 unreferenced crops, 0 missing files across all units.
  GATE NOTE for future split chapters: after appending sections to an existing
  unit, always re-include the prior batch's figures in the apparatus (or the
  wholesale replace drops them silently).

### Cover decision
- Kept the generated typographic ENGLISH cover (book.json cover_image unset).
  The colour cover (PDF p1) is a striking duotone portrait but entirely in
  Chinese; the builder copies a cover image byte-identical and cannot composite
  an English title, so a Chinese-only cover would be unreadable to the intended
  reader. The portrait is preserved as the ch07 frontispiece. Switching to it is
  a one-line book.json change; flagged to the commissioner.

### Deep audit (out/deep_audit.md)
- 1256 body paragraphs; 44 sampled (3.5%) at fixed seed 424242. Hand-read the
  pinnable sampled paragraphs against the scan (ch03 Kang interrogation incl.
  quoted speech; ch08 son's footnote, 13 precepts, 36-item outline; ch09
  chronology entries + all year/age labels): ~20 paragraph-equivalents, ZERO
  substantive errors. Whole-book invented-precision grep screen: benign.
- Term ledger rendered (out/term_ledger.md): 731 referents, 52 provisional (all
  minor bit-part names, doubtful scan characters; listed).

### Build / deliverable
- Cumulative EPUB rebuilt: 12 of 12, 432 notes, 78 figures; qa_epub PASS (104
  files, 432/432/432 notes resolve, all links resolve); epubcheck 5.1.0 =
  0 fatals / 0 errors / 0 warnings. Title page reads "the complete book: all 12
  chapters." COMPLETION.md written; HANDOFF.md rewritten to COMPLETE; CHANGELOG
  updated. Final EPUB committed with git add -f out/chen-yangshan.epub.

### Tooling -- no reverts
No script changes. ch11 used the ch01-06 body crop. The Route->Avenue Joffre fix
and the ch02 figure recovery are DATA corrections (glossary/notes/prose/figures),
not tooling changes.

================================================================================
## Revision R1 (R1): LEDGER UPDATE + ch02 EXEMPLAR -- scope TIER 1+2

The first editing batch of the post-completion register/style/apparatus pass
(REVISION_PLAN.md). Scope approved by the commissioner: TIER 1+2 only (tier 3,
the deeper topology/contraction rebaseline, was DECLINED). R0 was read-only
calibration; its census (defect classes + counts) lives in the R0 chat, and the
confirmed defect list was carried into the R1 kickoff. Content is FROZEN: this
is a style pass, not a retranslation; no source line touched, no boundary moved,
no number/name/fact changed.

### Ledger update (done first, per the kickoff)
Wrote the approved tier-1+2 rules into STYLE.local.md as a new section,
"Revision rebaseline (register/style/apparatus pass, R1+)", tagged #book/#promote,
provenance cited as REVISION_PLAN.md sec.3. Eight rules: Politburo, White Terror,
date format, litotes calque, the could-not-help formula, 等-tags, one-after-another,
and the X-ing-of nominalization. Each carries the anti-over-correction discipline
(most paragraphs LEAVE; synonym-shuffling is itself a defect) and the KEEP list.
STYLE.md and the styles/ layers were NOT touched (no mid-book recompose).

### ch02 exemplar -- 26 prose edits + 4 note-body date reformats
All edits in edits/ch02_edits.md (apply_edits.py grammar; OLD occurs exactly
once each), applied with `python3 scripts/apply_edits.py ch02`. Every edit is a
single-word or phrase substitution that cannot move a paragraph boundary.
Breakdown:
- TIER 1 Politburo: 10 edits collapsing all 政治局 ("Political Bureau" -> "Politburo",
  qualifier kept). Post-edit grep "Political Bureau" = 0.
- TIER 1 White Terror: 7 edits capitalizing all seven body hits of 白色恐怖 (all
  the specific definite terror -- Shanghai, Tianjin, Chongqing; none the generic
  "a white terror descended", so no carve-out applied). grep lowercase = 0.
- TIER 1 could-not-help: 1 edit (ch02:54 "could not help asking" -> "couldn't
  help asking", the plan's prescribed plain equivalent for THIS formula; this is
  a tier-1 fix, NOT the declined tier-3 narration-contraction program -- recorded
  in the STYLE.local rule so later batches do not over-read it).
- TIER 2 litotes: 1 edit (ch02:306 "no small convenience" -> "a great convenience").
  ch02:115 "no small contribution" was KEPT: it sits inside Chen Geng's {v} letter.
- TIER 2 nominalization: 1 edit (ch02:58 "the drawing of a double agent out" ->
  "drawing a double agent out"); the other ~10 "the X-ing of" hits were idiomatic
  ("the founding of ...", "the killing of ...", "the shooting of the four") and LEFT.
- TIER 2 one-after-another: 3 edits varied by sense ("in turn" / "one by one" /
  "a few at a time"), keeping ch02:293 as the retained instance.
- TIER 2 等-tags: 3 surgical edits (cut a redundant re-listing at ch02:20; vary to
  "among others" at ch02:36; cut "and so on" redundant with "many connections" at
  ch02:297). The tags in ch02 were already well varied (7/6/5/2), so only genuine
  tics were touched; any 等-tag sitting inside a note OR figure anchor was LEFT.

Apparatus (ch02 only this batch; other chapters' note dates go to R2/R3): 4
D-Month-YYYY dates reformatted to Month D, YYYY in note bodies 111 (three:
August 24/30, 1929; September 14, 1929) and 116 (November 11, 1929). Done
directly in notes.json via a json load/dump (ensure_ascii=False) because
apply_edits cannot edit a note body; only the day/month/year ordering changed,
never the values (note 111 still flags the source's wrong 1928 -> 1929 year).

### One collision caught by the build gate (recorded as a lesson)
Edit p036 first read "...and Yang Jianhong, among others...", which inserted "and"
into the figure `before` anchor "That March, Chen Lifu, Zhang Daofan, Yang Jianhong"
(p0047-f1.png) and the builder REFUSED the build. I had checked note anchors but
not FIGURE anchors. Fix: reworded p036 to vary the tag AFTER the names only
("Yang Jianhong, among others"), leaving the anchored name-list intact; reset the
reading file and re-applied. GATE NOTE for R2/R3: check every prose edit against
BOTH notes.json anchors AND figures.json `before` anchors before applying; do not
restructure anchored text for a mere tic.

### Verification (plan sec.2, mechanical-chapter path)
- Parity by construction: `git diff --stat out/ch02_reading.md` = 24 insertions /
  24 deletions, ZERO net line change (all in-place substitutions).
- Anchors: all 130 ch02 note anchors and all 20 ch02 figure anchors still present
  (dry-run check + the builder's refusal backstop, which fired once and was fixed).
- Numbers: grepped the edit list for digits; no numeral differs between any OLD
  and NEW. data/zh is gitignored (mechanical path), so no bilingual number run.
- Typography guard: every ADDED (+) line is pure ASCII; the pre-existing café /
  Pere Robert / one dialogue em dash were untouched. No curly quotes or ellipsis
  characters introduced.
- check_apparatus.py: 0 failures, 0 warnings.
- Build: 12/12, 432 notes; qa_epub PASS (104 files, 432/432/432 notes resolve);
  epubcheck 5.1.0 = 0 fatals / 0 errors / 0 warnings.
- EPUB 28 MiB (under the 30 MiB chat limit; MAX_FIG_WIDTH=1000 held).

### Spot-audit (plan sec.5 step 5)
Reviewed 100% of the 24 edited paragraphs (well over the 10% / min-10 bar) for
meaning preservation, reading each OLD->NEW in context. Every edit is a
terminology substitution (Politburo), a capitalization (White Terror), a
tic-variation (等 / one-after-another), one litotes flip, or one nominalization
recast -- none alters the translation's relationship to the source, so parity +
the semantic-equivalence review is the appropriate audit and a scan re-render was
not required (plan sec.2 mechanical-chapter path; data/zh gitignored). Zero
meaning drift found.

### KEEP-list sweep (plan sec.3.3)
Diff sweep confirms: no {v}/{p}/{d}/{g} line changed; the ch02:115 "no small
contribution" inside Chen Geng's letter is untouched; all four ch02 {v} blocks
(Chen Geng's 1951 letter, the note to Deshui, the order to Huang Dihong, and
Chen Yangshan's quoted recollections) are untouched; the author's institutional
first person ("our Party") and partisan epithets ("traitors", "running dogs")
are preserved; every decided glossary rendering (Avenue Joffre included) stands.

### Deliverables
edits/ch02_edits.md, out/ch02_reading.md (24 lines), notes.json (4 date
reformats), STYLE.local.md (rebaseline section), out/chen-yangshan.epub rebuilt.
The ch02 diff is the calibration target for R2/R3. NOT in scope for R1 (deferred
to R3 per the plan): Principal Characters growth, the translator's-note sentence,
and the other chapters' apparatus date reformats.

### Tooling -- no reverts
No script changes. The 4 note-date reformats were a one-off json edit (ASCII-only
date reordering, ensure_ascii=False preserves all CJK; 141 hanzi across note
bodies verified intact after write).

## Revision R2 (R2): SWEEP ch01, ch03, ch04 -- scope TIER 1+2

Second editing batch of the register/style/apparatus pass (REVISION_PLAN.md),
scope TIER 1+2. Calibration target: the R1 ch02 exemplar diff (most paragraphs
LEAVE; synonym-shuffling is itself a defect; when in doubt keep). Content FROZEN.
Totals: 23 prose edits + 2 note-anchor moves + 18 note-body date reformats across
the three chapters. Line counts unchanged (146/128/257); git diff --stat = 22
insertions / 22 deletions, ZERO net line change.

### ch01 -- 7 prose edits (no Politburo/litotes/could-not-help; no note dates)
- White Terror x3: capitalized the three DEFINITE named uses (ch01:120 Hangzhou,
  137 Shanghai, 138 Zhejiang). Read each hit: ch01:124 "lay under a white terror"
  and ch01:130 "so fierce a white terror" are INDEFINITE generic uses -> LEFT
  lowercase per the rule's carve-out; ch01:145 "steeped in white terror" sits in
  a {v} block -> LEFT frozen (KEEP list).
- one-after-another x4: 5 identical hits dominated the chapter; varied four
  (77 "in quick succession", 86 "in turn", 122 "one by one", 126 "in succession")
  and kept ch01:124 "one after another" as the retained instance. The ch01:126
  edit changed only "fell one after another"->"fell in succession"; the anchored
  name-list (Li Dazhao, Zhao Shiyan, Chen Yannian ...) earlier in the em-dash run
  is untouched.
- LEFT deliberately: nominalizations ("the founding of", "the making of", "the
  writing of", "the coming of" ...) all idiomatic; "threats and inducements"
  (威逼利诱, ch01:19) is a real coercion/enticement distinction, not a collapsible
  doublet; "heart and soul"/"safe and sound" idiomatic English.

### ch03 -- 6 prose edits + 2 anchor moves + 7 note-date reformats
- Politburo x1 (ch03:84, the CPSU Политбюро "Political Bureau"->"Politburo"). The
  note anchored on that clause CONTAINED "Political Bureau", so shipped a
  NOTE-ANCHOR pair (Kirov ... Political Bureau -> ... Politburo) in the same list.
  grep "Political Bureau" now 0.
- inversion recast x1 (ch03:88): "So answered, with one voice, several of the
  chief men Kang Sheng named: X, Y, Z." -> subject-first "Several of the chief men
  Kang Sheng named, X, Y, and Z, answered with one voice." The note on the three
  cadres was anchored on the old colon-list; re-anchored to "Xiao Shouhuang,
  Ouyang Xin, and He Changzhi" (NOTE-ANCHOR pair). No em-dash introduced (ch03
  has none in the file).
- could-not-but x2: ch03:98 "could not but have known"->"must have known";
  ch03:111 "could not but shake Mao Zedong"->"was bound to shake". ch03:5/15
  "had no wish to" read as natural reported speech and were LEFT (the tier-1
  target is the stiff "could not but" formula).
- litotes x2: ch03:67 "wronged not a few comrades"->"a good many comrades";
  ch03:99 "had had no few comrades killed"->"a good many". KEPT ch03:67 "which
  was no small thing" (idiomatic English).
- one-after-another: ch03:114 is inside a {v} block (LEFT); ch03:62 is the only
  editable instance and, with no domination, was LEFT.
- Note dates x7: reformatted D-Month-YYYY to Month D, YYYY in note bodies
  0,8,15,27,39,47,49 (e.g. "12 December 1936"->"December 12, 1936") AND normalized
  4 bare day-month forms (0 "25 December"->"December 25", 4 "12 December", 6
  "1 October", 39 "23 April"; note 39's range now reads "from April 23 to June 11,
  1945"). Values never changed (note 39 still flags the source's wrong 1943->1945;
  note 49's Kirov date December 1, 1934 preserved). Done via json load/dump,
  ensure_ascii=False.

### ch04 -- 10 prose edits + 7 note-date reformats (no Politburo)
- could-not-but x1 (ch04:209 "could not but carry a certain risk"->"was bound to").
- litotes x2: ch04:138 "gathered no little material"->"a good deal of material";
  ch04:199 "had no few legendary stories"->"a good many" (the figure `before`
  anchor earlier in that paragraph is untouched). KEPT ch04:18 "no small amount of
  work" (inside He Long's quoted speech).
- "Such was" x1: ch04:109 "Such was Chen Yangshan ..." PASSES the read-aloud test
  (deliberate summation after a quoted maxim) -> LEFT; ch04:151 "Such was the whole
  of Zhang He's first entry ..." fails -> recast "That was all that came of ...".
- one-after-another x6: 9 hits dominated the chapter; CUT three redundant with an
  explicit count (9 "a good many cadres", 11 "three ... stations", 196 "more than
  twenty connections" -- counts untouched), varied three (160 "in turn", 166 "in
  succession", 209 "a few at a time"), kept three natural instances (64, 151, 170).

### Verification (plan sec.2, mechanical-chapter path)
- Parity by construction: line counts unchanged; git diff --stat 22 ins / 22 del,
  zero net line change (all in-place substitutions or same-line phrase cuts).
- Anchors: pre-flight simulation applied all edits to a copy and confirmed every
  note anchor (after the 2 moves) and every figure `before` anchor still a verbatim
  substring; old anchors gone; the builder's refusal is the backstop (did not fire).
- Numbers: grepped every OLD/NEW pair for digits -- no numeral differs. The three
  one-after-another cuts drop only the sequence tag, never a count.
- Typography guard: every added line pure ASCII; no curly quotes/ellipsis
  introduced. (ch01 carries 4 PRE-EXISTING curly chars on lines 23/46/123, present
  in HEAD, NOT on any edited line and out of R2 scope -- flag for the R-final
  typography regression.)
- check_apparatus.py: 0 failures, 0 warnings.
- Build: 12/12, 432 notes, 0 pagebreaks; qa_epub PASS (104 files, 432/432/432
  notes resolve); epubcheck 5.1.0 = 0 fatals / 0 errors / 0 warnings.
- EPUB 28.6 MiB (under the 30 MiB chat limit; MAX_FIG_WIDTH=1000 held).

### Spot-audit (plan sec.5 step 5)
Reviewed 100% of the 23 edited paragraphs (well over the 10%/min-10 bar) OLD->NEW
in context: every edit is a terminology substitution (Politburo), a capitalization
(White Terror), a tic-variation/cut (等/one-after-another), a litotes flip, a
plain-auxiliary swap (could-not-but), or one inversion + one summary-formula
recast. None alters the translation's relationship to the source; parity + the
semantic-equivalence review is the appropriate audit (data/zh gitignored;
mechanical path). Zero meaning drift found.

### KEEP-list sweep (plan sec.3.3)
Diff sweep confirms: no {v}/{p}/{d}/{g}/*** line changed (grep of the changed
lines returns none); partisan epithets ("traitors", "agents", "butcher knife")
and the institutional first person ("our Party") preserved; the ch01:126 em-dash
name-list, ch04:18 quoted speech, and the ch03/ch04 {v} instance of
"one after another" all untouched; every decided glossary rendering stands.

### Deliverables
edits/ch01_edits.md, edits/ch03_edits.md, edits/ch04_edits.md; out/ch01_reading.md
(14 lines touched), out/ch03_reading.md (12), out/ch04_reading.md (18);
notes.json (2 anchor moves + 18 date reformats); out/chen-yangshan.epub rebuilt.
NOT in scope for R2 (deferred to R3): Principal Characters growth, the
translator's-note sentence, and ch00/ch05-ch11 note-date reformats.

### Tooling -- no reverts
No script changes. Date reformats were a one-off json load/dump (ASCII-only date
reordering, ensure_ascii=False preserves all CJK).

## Revision R3 (R3): SWEEP ch05-ch11 + APPARATUS -- scope TIER 1+2

Final editing batch of the register/style/apparatus pass (REVISION_PLAN.md),
scope TIER 1+2. Calibration target: the R1 ch02 / R2 ch01,ch03,ch04 diffs (most
paragraphs LEAVE; a rewrite that only shuffles synonyms is itself a defect; when
in doubt keep). Content FROZEN. This batch: 7 prose edits (all ch05) + 1
note-anchor move; 0 note-body date reformats needed (already compliant); 1
glossary date reformat; Principal Characters grown 3 -> 18; one translator's-note
sentence. git diff --stat out/ch05_reading.md = 7 insertions / 7 deletions, zero
net line change (187 = 187).

### ch05 -- 7 prose edits + 1 note-anchor move (the only R3 chapter with defects)
ch05 is the last big narrative chapter; ch06-ch11 are near-KEEP (obituary,
posthumous writings, chronology, references, afterword) and took zero prose
edits. All edits in edits/ch05_edits.md (apply_edits.py grammar; OLD occurs once
each).
- Politburo x2: ch05:42 "the Party's Central Political Bureau" -> "Politburo"
  (this clause is a NOTE ANCHOR, so a NOTE-ANCHOR pair shipped in the same list);
  ch05:45 "a provisional Central Political Bureau" -> "Politburo". grep
  "Political Bureau" now 0.
- White Terror x1: ch05:81 "in the days of the white terror" -> "White Terror"
  (the specific post-1927 Shanghai terror of the Gu Shunzhang-defection era;
  definite named use, not the generic carve-out). grep lowercase "white terror"
  now 0.
- litotes x1: ch05:53 "handled no small number of grave matters" -> "a good many
  grave matters" (narration, not a {v} block).
- ellipsis in narration x1: ch05:74 trailing "..." after "the War to Resist
  America and Aid Korea" -> period (plan sec.3.2: narration gets a period, "..."
  kept only inside quotations the source truncates; this is the career-sweep
  sentence before "Who was he?"). The note anchor "the Panmunjom talks during the
  War to Resist America and Aid Korea" is preserved verbatim.
- 等-tags x2: "and others" dominated ch05's list-closers (~10 hits); fronted two
  as "among them" appositives reusing the existing em dashes (ch05:17, ch05:26),
  both spans clear of note AND figure anchors. Other tags (already varied across
  "and others"/"and the others"/"and the rest") LEFT.
- LEFT deliberately in ch05: the two 1961 letters and quoted recollections ({v}),
  the {p} verse, the forged "Notice of Wu Hao and Others" (document title), the
  13 precepts (Chen's posthumous voice), the single non-dominating "one after the
  other"/"one by one" pair on ch05:45 (already varied phrasings), all idiomatic
  "the founding of"/"the gathering of"/"the handling of"/"the raising of"
  nominalizations, and the author's institutional first person and epithets.

### ch06-ch11 -- zero prose edits (walked the full grep battery; recorded here)
- ch06: White Terror already capitalized (line 68); "had no choice but to close"
  is inside a quoted 1988 letter (KEEP); the one litotes "the yield was not small"
  (line 19) is natural understatement, immediately quantified by "a good deal of
  ... material," LEFT; 等-tags varied and non-dominating. 0 edits.
- ch07: the whole obituary (悼词) is a HARD KEEP; both "White Terror" hits already
  capitalized. 0 edits.
- ch08: Chen's posthumous writings (13 precepts + 36-item outline + dry first
  person) are a HARD KEEP; the sentence-initial numerals are his numbered lists
  (structural). 0 edits.
- ch09: the chronology (年谱) is a structural table (year entries "1913 (age 7)");
  "White Terror" (line 16) already capitalized. 0 edits.
- ch10: References (bibliography); "White Terror" appears only inside a cited book
  title, already capitalized. 0 edits.
- ch11: the Afterword (author's own closing) reads as natural, warm English; the
  three "and others" are natural name-list closers / "others like him"; "the
  Writing of" (line 3) is a document title. 0 edits.

### Apparatus (plan sec.6)
- Note-date reformats (ch00, ch05-ch11): NONE required. Every month-bearing date
  in these chapters' note bodies is already Month D, YYYY or Month YYYY (e.g.
  "January 17, 1931", "February 7", "January 28, 1932", "October 7, 1906"); no
  D-Month-YYYY (day-first) or bare day-month forms remained. The R0 outliers were
  all in ch01-ch04, cleared in R1/R2. Verified by regex scan; logged as a no-op.
- Glossary date reformat x1: events/卢沟桥事变 note "The Marco Polo Bridge
  Incident, 7 July 1937." -> "..., July 7, 1937." Done by a targeted ASCII
  substring replace (not a heredoc; count-checked == 1); values unchanged, JSON
  re-validated. This was the one glossary D-Month-YYYY row the plan named.
- Principal Characters page grown 3 -> 18. Flagged the recurring cast in
  glossary.json with "principal": true + a one-line "cast" + "cast_order": Chen
  Yangshan (1), Zhou Enlai (2), Li Kenong (3), Chen Geng (4), He Long (5), Yun
  Daiying (6), Wang Shiying (7), Chen Kehan (8), Zhang Suzhen (9), Bao Junfu (10),
  Pan Hannian (11), Lu Nan (12), Wei Jian (13), Cheng Jianyu (14), Gu Shunzhang
  (15), Kang Sheng (16), Xu Enzeng (17), Chiang Kai-shek (18). Pure glossary edit;
  cast one-liners drawn from each row's existing note and the book, dates only
  where well established. The built characters.xhtml renders 18 castrows.
- Translator's-note sentence added (book.json translator_note para 2, mapped to
  translator_note_paragraphs by the builder): one sentence stating that the book's
  institutional first person ("our Party", "we") and its partisan epithets
  ("traitors", "running dogs", "reactionaries") are the author's own voice, kept
  deliberately rather than softened, with the historical verdicts left to the
  notes. Rendered (backmatter.xhtml) and typographized correctly.

### Verification (plan sec.2, mechanical-chapter path)
- Parity by construction: ch05 187 = 187 lines; git diff --stat 7 ins / 7 del,
  zero net line change (all in-place substitutions or same-line phrase recasts).
- Anchors: all 47 ch05 note anchors (after the 1 move) and all 17 ch05 figure
  before-anchors still verbatim substrings post-edit; the builder's anchor-refusal
  backstop passed (built 12/12, 432 notes). check_apparatus 0 failures / 0
  warnings.
- Numbers: no digit appears in any OLD/NEW in edits/ch05_edits.md, so no numeral
  can change; the glossary date reorder changed no value; data/zh gitignored
  (mechanical path), so no bilingual number run.
- Typography guard: ch05 non-ASCII inventory unchanged (U+2014 x41, U+00FC x1);
  no curly quote or ellipsis character introduced into any reading file; the two
  等 recasts reuse pre-existing em dashes and introduce none.
- Build: 12/12, 432 notes, 0 pagebreaks; qa_epub PASS (104 files, 19 documents,
  432/432/432 notes resolve, all links resolve); epubcheck 5.1.0 = 0 fatals / 0
  errors / 0 warnings.
- EPUB 28.6 MiB (under the 30 MiB chat limit; MAX_FIG_WIDTH=1000 held).
- Register: check_register out/ch05_reading.md --ref out/ch01_reading.md within
  tolerance (contr 4.1/1k, em-dash 2.9/1k, rhythm 0.62; roster-heavy chapter,
  little dialogue -- matches the B07 ch05 baseline).

### Spot-audit (plan sec.5 step 5)
Reviewed 100% of the 7 edited ch05 paragraphs OLD->NEW in context (well over the
10%/min-10 bar): two Politburo terminology substitutions, one White Terror
capitalization, one litotes flip, one narration ellipsis -> period, and two 等
appositive recasts that preserve every name and add/drop none. None alters the
translation's relationship to the source; parity + the semantic-equivalence
review is the appropriate audit (data/zh gitignored; mechanical path). Zero
meaning drift found.

### KEEP-list sweep (plan sec.3.3)
Diff sweep confirms: no {v}/{p}/{d}/{g}/*** line changed in ch05; ch07 obituary,
ch08 precepts/outline, and all verse untouched (0 prose edits in ch06-ch11); the
author's institutional first person and partisan epithets are preserved (the
translator's-note sentence names them as deliberately kept, not neutralized);
every decided glossary rendering stands.

### Deliverables
edits/ch05_edits.md; out/ch05_reading.md (7 lines touched); notes.json (1 anchor
move); glossary.json (1 date reformat + 18 principal flags); book.json
(translator's-note sentence); out/chen-yangshan.epub rebuilt (committed).
R3 completes the chapter sweep of the revision pass; all 12 units now swept
(R1 ch02, R2 ch01/ch03/ch04, R3 ch05 + the ch06-ch11 zero-edit walk) plus the
apparatus mechanics. Remaining: R-final (whole-book regression + reconcile +
register table + CHANGELOG + COMPLETION addendum + final EPUB commit).

### Tooling -- no reverts
No script changes. The glossary date reformat and principal flags were a
targeted string replace + a json load/dump (indent=2, ensure_ascii=False, CJK
preserved); the translator's-note sentence was a targeted book.json edit.
