# PROGRESS — 军统内幕 / Inside the Juntong

Working state. Updated as each unit lands.

## The book

Shen Zui (沈醉), 军统内幕, 3rd ed., Zhongguo Wenshi Chubanshe, Beijing 2001,
ISBN 978-7-5034-0755-0. 521-page image-only scan, no text layer, no bookmarks.
515 pages of book text, ~338,000 Han characters by OCR count (the CIP page
claims 418,000 字, which counts punctuation and front matter).

A memoir, not a narrative history: twenty-one free-standing chapters, most of
them written between 1962 and 1966 for the CPPCC's *Selected Historical
Materials* and collected here. The author was a Juntong major-general.

## Verified structure

- **Two page-number sequences.** Main text: printed = PDF − 19. Front matter
  (概况, 前言, 目录): printed = PDF − 5, running 1–14. Confirmed by eye on the
  magnified footers of PDF 200/250/450 → 181/231/431, and cross-checked against
  a dozen page references in the book's own contents pages. The front-matter
  sequence is why the first offset measurement (PDF − 5, taken on page 10) was
  wrong for the body of the book; anything citing pages before this was settled
  would have been off by fourteen.
- The scan's contents pages (PDF 16–19) exist but are **incomplete** — they
  omit several chapters they nonetheless paginate. The authoritative map is
  `data/structure.json`, recovered from heading geometry and confirmed against
  the contents pages where those do list an entry.
- 25 units: 2 front matter, 21 chapters, 2 back matter. See `book.json`.
- One chapter was missing from the geometric pass and found by probing the gap:
  保密局内幕 (Inside the Bureau of Secrets Preservation), printed 392.
- PDF 521 is the Anna's Archive provenance page.

## Pipeline state

Rendered: all 520 pages at 300 dpi. OCR'd: all 515 text pages. Both complete;
the per-chapter work from here is assemble → verify → translate → check.

## Environment findings worth keeping

- **`OMP_THREAD_LIMIT=1` on tesseract is mandatory.** Without it three
  concurrent processes each pinned a core at 130% and did not finish a single
  page in ten minutes — twice, once through a Python thread pool and once
  through xargs. Tesseract's OpenMP threads busy-wait; twelve of them on four
  cores starve each other rather than sharing. Pinned, with `xargs -P 4`, a
  page costs 0.93s and the whole book OCRs in about six minutes. This cost
  roughly an hour to diagnose and is the single most expensive trap here.
- Killing a stalled run **orphans the tesseract children**, which keep
  spinning and slow everything afterwards. Kill by PID and verify with
  `pgrep -c tesseract`.
- Blank lines in the OCR output are the **only** paragraph signal the file
  carries — tesseract drops the source's two-space indent. The first OCR pass
  filtered them as noise and had to be redone.
- Page folios cannot be cropped away: the last body line reaches 0.9117 of
  page height on some pages while the folio starts at 0.8890 on others, so the
  bands overlap globally. Filtered by shape in `ocr_crop.py:strip_folio`.

## Register baseline — NEEDS WINSTON'S SIGN-OFF

There is no approved reference chapter for this book yet, and the skill's whole
per-chapter drift check is measured against one. `fm01_gaikuang` is proposed as
that baseline: institutional prose, first person, plain and documentary, period
political idiom preserved rather than neutralised.

**This is the one thing worth reading before the rest of the book is
translated**, because everything after it is measured against it. If the voice
is wrong, it is wrong once here and twenty-four times later.

Specific choices made in it, all reversible:
- 军统 glossed once in full, then "the Juntong" throughout — the book's own usage.
- 重庆 as "Chungking", the period English form, not "Chongqing".
- 委员长 as "the Generalissimo".
- 臭招牌 kept literal as "stinking signboard", with a note on the register.
- Chapter title 军统概况 as "An Outline of the Juntong".

## Register baseline: the dialogue half is NOT yet set

`fm01_gaikuang` works as the baseline for the expository voice, but it contains
no dialogue at all, so its dialogue-contraction rate is 0.0/1k and measuring
anything against it is measuring nothing: the ratio comes out 1.00x whatever
the chapter does. The preface reads 13.2/1k against it and the check reports
"within tolerance," which is true and uninformative.

The dialogue baseline has to be reset from the first unit that has real
dialogue. Until then, treat the contraction column as unmeasured rather than
passing. The "shall" share is the usable signal in the meantime: it caught one
line in the preface where Zhou Enlai's warm, plain send-off had been given a
formal "I shall," which is exactly the drift the check exists for, and it is
now "I'll."

## Per-unit log

### fm01_gaikuang (军统概况 / An Outline of the Juntong) — DONE

- PDF 6–9, front-matter printed 1–4. 18 source paragraphs, 18 translated.
- **13 name mangles caught by crop verification**, every one of them a
  plausible-looking valid word rather than obvious garbage — the defect class
  the dual-OCR disagreement filter cannot see, because both psm configurations
  make the same mistake on the same glyphs:
  郑锡鹿→郑锡麟, 岂料→酆悌, 潘估强→潘佑强, 印开基→邱开基, 候志明→侯志明,
  徐因曾→徐恩曾, 贺友组→贺耀组, 钱大钓→钱大钧, 林幸→林蔚, 玫珈山→珞珈山,
  番戒委员会→惩戒委员会, 一九八年→一九八〇年, and 张国琳→**张国焘**.
  The last is the one that mattered: Zhang Guotao, a founder of the Chinese
  Communist Party, running a Juntong research office — OCR had turned him into
  a nobody, and nothing but the scan would have caught it.
- Checks: parity 18/18, anchors 12/12 resolve, headings consistent, numbers
  0 unresolved across 18 pairs.
- Notes: 12 (3.0 per printed page).
- Glossary: +32 entries (75 total).
- **Three real tool bugs found and fixed**, all of which would have produced
  false confidence rather than noise:
  1. `check_structure.check_parity` dropped a source line as the "chapter
     title" even when the title had already been removed as a heading, biasing
     every parity count by one — in the direction that hides a dropped
     paragraph, which is the defect the check exists to find.
  2. `check_numbers.cn_to_int` could not read 百/千/万, so 一千四百 fell apart
     into a stray 四 and reported a dropped number that was not dropped.
  3. A NOISE entry (`[一二三]十`) ate the first half of 二十九 and left a bare
     九 behind — the exact prefix-eating trap the script's own comment warns
     about, recurring with a different pair.

### fm02_qianyan (前言 / Preface) - DONE

- PDF 10-15, front-matter printed 5-10. 15 source paragraphs, 15 translated.
- Crop verification caught five more source errors, two of which the numeric
  check had already flagged from the other direction: 十和年 for 十八年
  (eighteen years) and 十别总理 for 辞别总理 (took leave of the Premier), both
  of which left a stray 十 that read as a dropped "10"; plus 黄效先生 for
  黄雍先生 (Huang Yong, a CPPCC member and one of the original Ten-Man Team),
  郑锡记 for 郑锡麟, and 周因来 for 周恩来.
- Checks: parity 15/15, anchors 14/14, numbers 0 unresolved, register within
  tolerance (but see the baseline caveat above).
- Notes: 14 (2.3 per printed page).
- EPUB built and QA PASS: 2 documents, 33 paragraphs, 26 notes, all references,
  bodies and backlinks matching.

### Two more tool fixes this unit

- `qa_epub.py` identified chapter documents by matching `prologue|chNN` in the
  filename, so it reported "0 documents, 0 paragraphs" for a spine made of
  front matter and did not notice it had measured nothing. It now derives
  content documents from the spine by excluding the known apparatus documents,
  so a unit named anything at all is still checked. This is the last gate
  before a build ships and it must not depend on a naming convention it does
  not itself enforce.
- `check_numbers.py`: a noise pattern beginning with a numeral could eat the
  TAIL of a longer numeral (一日 fired inside 二十一日 and left 二十, reported
  as a dropped "20"). All such patterns are now guarded with a lookbehind.
  Also added "a million" to the English reader.

### New in the pipeline: a correction ledger

`data/ocr_fixes.json` plus `scripts/apply_fixes.py`. Crop verification is the
most expensive step here and its results were the most perishable: `data/txt/`
and `data/zh/` are untracked, so a fresh checkout re-runs OCR and quietly
reinstates every mangle already paid for - 张国焘 reverts to 张国琳. Every
verified reading is now recorded with the page it was checked on and why, and
replayed by script. 18 entries so far.

### ch03 (抗战时期军统特务在重庆的罪行 / Juntong Crimes in Chungking during the War of Resistance) - DONE

- PDF 91-149, printed 72-130. 193 source paragraphs, 193 translated. 11 sections.
- **619 crop-verified OCR corrections**, by far the largest ledger of any unit so
  far. Names OCR had turned into non-names and the scan restored: 郭寄峤,
  张简斋, 陈逊斋, 肖茂如, 胡藻, 曹万道, 廖承志, 史良, 曹禺, 孔祥熙 (mangled
  five distinct ways), 孔令俊, 宋希濂, 唐毅, 酆裕昆, 魏大铭, 王瓒绪, 刘耀,
  蒲岗, 何成濬, 张炎元, 胡天秋, 韦贤, 王兴国, 曾泽, 祝宗梁, 周伯勋, 周景敦,
  刘之盘, 刘廷根, 邹陆夫, 陈昌熙, 龚仙舫, 任建鹏, 王芃生, 林可胜, 贝祖诒,
  谷正纲, 葛天璇, 陈韵娜, 陈雯, and 张国焘 twice more.
- Places restored: 红岩村, 渣滓洞, 白公馆, 鹅公岩, 寸滩, 海棠溪, 机房街,
  枣子岚垭, 赣江街.
- Checks: parity 193/193, alignment OK across every pair, register within
  tolerance of the ch01 reference, numeric check 6 residual flags, all
  adjudicated (see below).
- Notes: 81, i.e. 1.37 per printed page, against 1.6 in ch01 and 3.0 in fm01.
  Every anchor verified verbatim at write time; check_structure reports 152
  anchors across the book, 0 unresolved. Density is where the material earns
  it: this chapter, like ch01, carries long personnel rosters that need no
  glossing, and the notes concentrate on the historical figures, the prison
  system, the wordplay that cannot cross, and the places where the author is
  an interested witness.
- Glossary: +81 entries (198 total), including the two SACO prisons, the
  Chungking institutions, and the period idiom preserved rather than
  neutralized (美帝, 家法, 清水衙门).

### ch03 numeric adjudication - 27 flags, 0 real omissions

Every flag was one of four classes, none of them a dropped quantity:
- numerals inside NAMES (许忠五, 曹万道, 廖越万, 王四心, 三斗坪);
- numerals inside PLACE names (两湖会馆, 两路口, 万寿宫, 一品场);
- numerals inside IDIOMS (漏洞百出, 成千上万, 不三不四, 劲头十足, 百般,
  十有八九, 七折八扣, 数以百计);
- real numbers correctly translated that the checker could not read in English
  ("a hundred thousand dollars" for 十万元, "between a hundred and seventy and
  a hundred and eighty" for 一百七八十, "two or three hundred" for 二三百).

The classes are now in `data/noise.txt` and the parser reads "a hundred
thousand". The exercise was still worth it: it caught ONE real loss. The source
counts characters - 望龙门 is 三个字, 望龙门的 is 四个字 - and the translation
had flattened both to "the words". Restored as "the three characters" and
"those four characters".

### FOR WINSTON'S READ-THROUGH, ch03

- The book prints 卫成总司令部 throughout for what is unmistakably the
  重庆卫戍总司令部, the Chungking Garrison Command. 卫成 is not a word. Twelve
  occurrences, all reading 成 in the scan. Preserved as printed and to be noted,
  not silently corrected. JBIG2 glyph substitution and a printing error are both
  live possibilities and I cannot tell them apart at this resolution.
- 助桀为虐 where the common form is 助纣为虐. Crop-verified as printed.
- 王固盘 where scholarship gives 王固磐. Preserved as printed.
- 黄角垭 where the commoner form is 黄桷垭. Preserved as printed.
- Two passages need notes more than most: the hotel waiter's cry "Is Mr. Wang
  Sixin at home?", which is the character 憲 taken apart into 王/四/心 as a
  warning that the military police are at the door; and the action group the
  operatives themselves nicknamed the 锦衣卫 after the Ming secret police.
- The prison ladder - 小学 / 中学 / 大学 for the corps detention house,
  Baigongguan and the Xifeng camp - is the author's own reported usage.

### ch05 (囚禁期间的叶挺将军 / General Ye Ting in Confinement) - DONE

- PDF 157-162, printed 138-143. 14 source paragraphs, 14 translated.
- 70 crop-verified OCR corrections. Restored 江西上饶, 七星岩, 小歌乐山北麓,
  四川军阀白驹, 香山别墅, 渣滓洞, 廖承志, 挥着一柄大葵扇, 邵力子.
- Checks: parity 14/14, alignment OK, content alignment OK (63 name
  occurrences all in the paired paragraph), register within tolerance,
  numeric check 1 residual flag, adjudicated: the 五 inside the name 马法五.
- Notes: 20, i.e. 3.3 per printed page. Glossary +20 (218 total).
- CAUGHT BY PARITY: the chapter's final paragraph was not translated at all.
  I read paragraphs 11-13, translated them, and stopped without checking there
  was a 14th. Nothing in the English showed it -- the chapter ended on a
  perfectly good closing line. check_structure reported 14 source against 13
  translation immediately. The missing paragraph carried the March 1946
  exchange for Ma Fawu and Ye Ting's remark on cutting his hair at last, which
  is the chapter's resolution.

### ch06 (张学良将军被扣押时的情况 / General Zhang Xueliang under Detention) - DONE

- PDF 163-170, printed 144-151. 22 source paragraphs, 22 translated.
- 113 ledger entries, all crop-verified where the reading was in doubt.
  Restored among others: 雪窦寺 (OCR made the temple a village), 阿米茄表厂
  (Omega), 白面馍, 王陵基亲自, 荒凉, 朝廷, 草山温泉区, 鄂豫皖三省剿总, 击毙,
  劫走, 竭力, 握别, 老竹子, 拴住. One OCR error (说下去吧!” read as 说下去吧二)
  had swallowed the sentence-final punctuation and with it a real paragraph
  break; fixed in the page text and reassembled, 21 paragraphs became 22.
- PIPELINE TRAP FIXED: apply_fixes writes data/zh, assemble regenerates
  data/zh from data/txt. Run in the wrong order, assembly silently discards
  every correction — which is exactly what the first ch06 pass did. Order is
  assemble THEN apply_fixes, always.
- CHECK FIXED: check_structure's heading-shape comparison could never pass
  once sectionless chapters joined sectioned ones ((2,) vs (2,3)); it had
  been red since ch04 without stopping the line, and it ignored book.json's
  heading_depth key. Now compares level positions only where present, and
  honors the config.
- Checks: parity 22/22, alignment OK, content alignment OK (101 name
  occurrences all in the paired paragraph), register within tolerance,
  numeric check 1 residual flag adjudicated (百年纪念表 -> "centenary" carries
  the hundred; noise rule added with comment).
- Notes: 25 at 3.1 per printed page, plus two retro first-appearance notes
  the earlier chapters owed: the Xi'an Incident (ch02) and the joint
  identification of Zhang and Yang (ch03).
- Glossary +34 (252 total).
- Corroboration pass run against outside sources for this chapter's checkable
  claims: Zhang's 1936 tribunal and pardon-into-custody (corroborated), Yu
  Fengzhi's departure (contradicted: 1940, not Shen's 1943 -- noted), Liu
  Yiguang's Whampoa class (contradicted: fourth, not Shen's sixth -- noted),
  the watch anecdote (legend with incompatible variants -- noted as such),
  Caoshan renamed Yangmingshan 1950 (corroborated, completes the Wang
  Yangming programme Shen describes), Hu Die kept by Dai Li (corroborated,
  Wakeman -- explains the lunch scene Shen leaves unexplained).

### ch07 (杨虎城将军被惨杀的经过 / The Murder of General Yang Hucheng) - DONE

- PDF 171-182, printed 152-163. 27 source paragraphs + 4 section headings,
  27 translated. The chapter is the book's centrepiece atrocity narrative:
  Yang's return in 1937, Xifeng and Xuantian Cave, the 1949 knife murders of
  Yang, his son, his secretary Song Qiyun, Xu Linxia and the two children at
  the Dai Memorial Hall on Songlinpo.
- 173 ledger entries. THE SYSTEMATIC MANGLE OF THE CHAPTER: the guard
  captain 龚国彦, which OCR rendered ten different ways (黎/蓝/缆/绪/秦/复/
  鸡/故/克/裴); the print is crop-verified 龚. Also restored: 谢葆贞, 拯中,
  熊式辉, 阳朗坝, 车耀先, 张静甫 (twice-mangled into a phantom second medic
  张项青), 临澧, 张鹄, 白公馆, 渣滓洞, 革命人士, 龙蟠虎踞, 含矿质/泉水,
  镪水 (the nitric acid -- load-bearing, crop-verified), 李虎臣 (OCR 李虎城;
  my first ledger guess 杨虎臣 was wrong and is corrected -- the 1926 'two
  tigers' defence of Xi'an).
- Checks: parity 27/27, alignment OK, content OK after one glossary-drift
  cascade (Gele Mountain -> Geleshan, the established rendering), numbers 0
  after 3 noise adjudications (百花洲, 百科全书, 万有文库), register in
  tolerance.
- Notes: 27 at 2.3 per printed page (the chapter runs long and narrative;
  density deliberately below ch06's biography-dense 3.1), plus a retro li
  unit note at its true first appearance (ch04).
- Glossary +42 (294 total).
- Corroboration: the murder date (record: 6 Sept 1949) sits inside Shen's
  'end of August or beginning of September'; 森森 confirmed as the pet name
  of Song Zhenzhong (小萝卜头), youngest recognized martyr; Luo Shiwen /
  Che Yaoxian executions (Aug 1946, under Li Jiajie) corroborated; Zhang
  Luping radio-case seven corroborated -- Shen lists them without mentioning
  they had penetrated his own service, noted; Qilin Cave held Zhang Xueliang
  1941-42 per standard accounts, which Shen's ch06 chronology contradicts --
  flagged in the note; Xu Linxia arrested with an eight-month-old son, not
  delivered in prison as Shen has it -- noted.

### ch20 (保密局内幕 / Inside the Bureau of Secrets Preservation) - SOURCE PREP + SYSTEMATIC LEDGER, TRANSLATION PENDING

- PDF 411-469, printed 392-450. 163 body paragraphs + 7 detected ### headings,
  ~40,000 CJK chars. THE BIGGEST CHAPTER IN THE BOOK. Multi-turn unit -- do NOT
  write a partial reading.md. Offset confirmed (PDF 411 -> printed 392).
- DONE this turn: render 411-469, ocr_crop, assemble (163 paras, 7 headings),
  apply_fixes. 43-entry systematic ledger, 103 replacements applied. Residue
  scan clean for all principals.
- SECTION STRUCTURE for the translation turn. 7 headings were detected as ###:
  调整组织，更疯狂地反共反人民 / 从屠杀到利用 / 用叛徒做耳目 / 特务们是怎样观察、
  诱骗被捕的革命人士的 / 错综复杂的种种斗争 / 郑、毛、唐三派的明争暗斗 /
  真假保密局的鬼把戏. In ADDITION, THREE subtitles were OCR-merged into body
  paragraphs (like ch19's "After the Victory") and MUST be split into ### +
  body para to keep parity, all three crop-verified this turn:
    * para 2  : 改头换面，汰弱留强 ("A Change of Face; Cull the Weak, Keep the Strong")
    * para 53 : 血腥毒辣的罪恶活动 ("Bloody, Vicious Criminal Activities")
    * para 107: 对叛徒的运用 ("The Use of Traitors")
  Confirm the merged/split parity math carefully -- these three shift the count.
- LEDGER (systematic, whole-book manglings, all high-confidence): Dai Li
  (戴竺/戴符/戴等->戴笠, but NOT 戴仅 = 戴+仅 "Dai only", left alone); Chiang
  (菏/薪/戎/藉/东/萝介石->蒋介石); Mao Renfeng (毛人风/毛人反); Juntong
  (车/衬/盏/御统); 郑介昆->郑介民. PRISONS (historically critical, every
  occurrence was mangled): 渣滓洞 <- 渣滋润/酒淳润/酒浮润/渣入洞/洼注洞;
  白公馆 <- 日公馆/昌公馆 (昌园路, a road, left untouched). 江竹筠 (Sister
  Jiang) <- 江竹移. 潜伏 <- 淤伏/湾伏/淤估.
- 和军统 IS NOT A BLIND REPLACE. Of 11 occurrences, several are legitimate:
  和...一样 ("same as the Juntong period"), 戴笠和军统特务 ("Dai Li and the
  agents"), 邹陆夫和军统...胡屏翰 (a conjunction), and 打和军统 = 打入军统
  ("infiltrate"). Only the clearly-spurious 和 were removed per-occurrence
  (7 targeted entries). Watch this at translation time.
- TRANSLATION-TURN VERIFICATION WORKLIST (crop-verify BEFORE writing, per
  pipeline step 5 -- these are the load-bearing, high-error-risk items NOT yet
  done): (a) the ~80-name national station-chief roster in para 36 (dozens of
  provinces, many obscure names, unit numbers); (b) the massacre martyr rosters
  in paras 59 (重庆大坪/渣滓洞, incl. 江竹筠), 80 (上海, Mao Sen), 86-91 (the
  11-27 Chongqing massacre: 杨虎城, 黄显声, 黎剑霜 and infant, the 白公馆/渣滓洞
  killings) -- these names must be exact and cross-checked against the
  documented 红岩/歌乐山 record; (c) the 三有公司 enterprise list (para 8-9);
  (d) personnel/troop numbers throughout (para 13, 17, 30, 73-74).
- GLOSSARY/NOTES to prepare: 保密局 = "Bureau of Secrets Preservation" (already
  decided); the 三有公司 ("Three-Haves Company") pun (有势/有钱/有人); 顾顺章
  (Gu Shunzhang) turncoat episode (para 109-111, cross-ref the famous 1931
  case); 江竹筠/江姐 (Sister Jiang, the 红岩 martyr); the 白公馆/渣滓洞 prisons
  and 中美所 (SACO) already glossed; the 苦肉计 ("self-injury ruse") stratagem;
  真假保密局 (the "real vs fake Bureau" ruse for Li Zongren). Shen is a direct
  participant here (总务处长, then 云南站长) -- category-4 self-implication notes
  matter especially (his own role storing weapons in coffins, para 79; being
  ordered to assassinate Yang Jie, cross-ref ch17).

### ch19 (唐纵其人 / Tang Zong) - DONE

- Translation done (148/148 parity first pass). All 5 gates green, qa PASS
  (21 documents, 520 notes, 393 page markers). Notes: 12. Glossary +32 (the
  large new cast).
- PARITY: the OCR-merged heading 抗战胜利后的情况 (para line 39) was split into
  a ### heading + body para as planned; 警察总署/保安局 title rendered as one ###.
  Both give 148/148.
- CONTENT check caught 6 short-form renderings where the source used the FULL
  name (唐纵/蒋介石) or a dropped place (昆明); fixed all six to the full form.
  Adding the new cast then surfaced 乐干: I had rendered it "Le Gan" in BOTH
  ch13 and ch19, so the glossary was set to "Le Gan" (provisional; surname 乐
  also reads "Yue") to match the built text rather than editing two chapters.
- NUMBERS: 2 residual flags both adjudicated PASS -- para 61 十余人 rendered
  "a dozen" (correct, no digit), para 126 an OCR "了！"->"了1" artifact. Noise
  list extended with the ch19 idioms/name-numerals (三令五申/三令五中, 十拿九稳,
  笑话百出, 一不做二不休/体, 杀人以万计, 一帆风顺, 这一手, 三顾茅访, 一五一十,
  零星, 誓不两立, 万人凤 [OCR of 毛人凤], 二反共, 四川/四州).
- REGISTER: within tolerance vs ch01; "shall" elevated (22%) but deliberate --
  Shen's formal expository frame ("I shall not repeat here"); contractions are
  in the quoted speech only. VOICE-DRIFT FLAG (fable pass): confirm the
  quoted-speech contractions in the outraged-agents passage (para 126) read
  right and that the long expository stretches did not pick up Opus cadence.
- SOURCE editorial note: the edition inserts "本书付印前唐已在台湾死去" mid-
  sentence in para 3; moved out of the sentence into a footnote per the
  no-inline-flags rule (Tang died in Taipei 26 Oct 1981).
- Corroboration (no Grok): Tang Zong 1905-1981, his captured diary 《在蒋介石
  身边八年》 (pub. 1991); 金都血案 27-29 Jul 1947 (standard count 11 dead, close
  to but not matching Shen's figures -- noted); 《中国之命运》 ghostwritten by
  Tao Xisheng 1943; Wei Lihuang/Lihuang County (Jinjiazhai, reverted to
  Jinzhai) precedent for Hu Zongnan's failed "Zongnan County" vanity.
- Notes texture: 智多星 (Wu Yong/Water Margin), 以柔克刚, 三顾茅庐, the German-
  fascist model and the self-incriminating candour about it, the child-flesh
  atrocity flagged as Shen's uncorroborated testimony in the 1962-66 register.

- PDF 369-410, printed 350-391. 148 body paragraphs, ~27,700 CJK chars.
  The biggest chapter; multi-turn unit -- do NOT write a partial reading.md.
- LEDGER COMPLETE (36 entries, every name crop-verified against the scan):
  recurring manglings (戴笠/蒋介石 7 variants/毛人凤); section headings; and the
  full cast: 乃建 (Tang's zi, 帮健), 酃县 (hometown, 圭县), 曹圣芬 (草圣分),
  鄂裕坤 (岂容坤/峙裕坤/部裕坤), 汪弼 (汪弹/汪纲/汪绚), 李寨 (李塞), 俞叔平
  (价叔平/俞杰平), 酆悌 (attaché, 召悦), 冯文尧 (冯文用), 蒋镇南 (菏镇南),
  翁文灏 (翁文溉), 邱吉尔 (苑吉尔), 乐干 (乐于), 张衮甫 (张窒甫). Clean-OCR
  names trusted (谷正伦/韩文焕/黄珍吾/秦德纯/宣铁吾/陶一珊/罗国新/卫立煌/
  蒋纬国/曾扩情/刘健群/张镇/唐角/李叶/王芝禄/刘本钦/李哲/徐恩平/石仁宠/
  徐昭骏/赵世瑞/林桓/吴适宪/陈菊英/陈希曾/竺培基 + the province-chief lists).
  Residue scan clean; source is fully prepped for translation.
- PARITY TRAP for the translation turn: the section heading 抗战胜利后的情况
  (After the Victory) is OCR-MERGED into the body at para line 39
  ("抗战胜利后的情况抗战胜利后，唐纵大走鸿运"); split it into a ### heading + the
  body para -- source counts line 39 as 1 body para, so translation must be
  1 heading (uncounted) + 1 body para to keep 148/148. The 警察总署/保安局 title
  is 2 ### lines in source (50-51) -> render as one ### heading (both excluded
  from body counts, so parity is unaffected).
- 8 sections to render: (intro); Before the War; During the War; After the
  Victory (the merged one); Director of the Police Directorate-General and the
  Defence Ministry's Public-Security Affairs Bureau; An Endless Stream of
  Headaches; Reactionary Measures as Director; The Open and Hidden Struggle
  with Li Shizhen; A Lament Before Fleeing to Taiwan.
- Texture to note: 唐's "智多星"(Wisdom Star) epithet; 和柔能克刚; 三顾茅庐; the
  German-fascist model for the secret police; 制敌机先; the 立煌县->宗南县 vanity
  episode (Hu Zongnan). Corroborate: Cairo Conference photo, 《中国之命运》, the
  金都血案. Already glossed: 邱开基/李毓桢/李肖白/王新衡/胡宗南/汤恩伯/叶霞翟/毛森/
  李士珍/潘其武/俞济时/汪精卫/胡适(add?).

### ch18 (军统特务头子戴笠的继承人毛人凤 / Mao Renfeng, Dai Li's Successor) - DONE

- Translation done this turn (89/89 parity first pass). 5 gates green, qa PASS
  (20 documents, 508 notes). Notes: 12. Glossary +30 (the large new cast).
- Extra ledger fixes found during translation (all crop- or context-verified):
  亲万→亲信 (Chen Cheng's confidant, 信→万), 感激阐零→涕零, 陈减/跌诚→陈诚,
  李钥村/李毓相→李毓桢, 户→卢 (Lu Han), 笑汝耕→殷汝耕 (Yin Rugeng, crop p361).
- Numbers 0 after noise for names/companies/idioms with numerals: 马汉三,
  三有公司, 十八集团军, 低三下四, 一丈五, 三分, 涕零, 五原, 三轮.
- GLOSSARY CASCADE: added 宋子文 and hit a book-wide rendering split — earlier
  chapters use "T.V. Soong" at first mention then bare "Soong". Set the glossary
  anchor to "Soong" (note records the full "T. V. Soong"), which validates
  ch02/03/06/07/13/18 uniformly; ch18 renders "T.V. Soong" first, "Soong" after.
- Corroboration (no Grok): Ma Hansan executed 27 Sep 1948, factional cause as
  Shen gives; the Kawashima Yoshiko / Nine-Dragon-Sword backstory noted as the
  popular account that Shen pointedly omits. Zhang Guotao (defected 1938) and
  Huang Xiansheng (martyr) already noted earlier; Yin Rugeng, Yu Lexing glossed.
- VOICE-DRIFT FLAG (fable pass): contr/1k 18.6; the chapter is nearly all
  exposition with little dialogue -- confirm Opus didn't over-contract.
- NOTES for the read-through: the 忍/等/狠 organizing pun, the 宋子文/刘纪文
  gambling pun, the flag-superstition, and the 王佐断臂 self-injury allusion
  (Mao telling Shen to stay behind as a planted agent) are the texture highlights.

- PDF 342-368, printed 323-349. 89 body paragraphs, ~18,000 CJK chars, 7 heading
  lines (chapter title split over 2 lines + 5 section headings). The largest
  remaining chapter; a multi-turn unit like ch13 -- do NOT write a partial
  reading.md that fails parity.
- DONE this turn: render/ocr/assemble, and a 27-entry crop-verified ledger
  (95 replacements) covering the recurring-name manglings (戴笠, 蒋介石, 毛人凤,
  王蒲臣) and the new cast, all crop-checked against the scan:
  杨宣诚 (声宣诚), 张严佛/毅夫 (雪夫), 邓文仪, 郭子良, 何龙庆, 周伟龙, 张炎元,
  张师, 张业, 王兆槐, 马汉三, 王蒲臣, 乔家才, 刘玉珠, 李希成, 潘其武, 毛森,
  黄显声, 陈为诚, 俞济时, 邱开基 (=ch14), 瞿梦秋, 张国焘 (张国奏), 东方白 (东方折),
  陈世贤, 毛惕园, 余素秋, 马连良, 吕世琨, 董士立, 钱午林, 李士珍, 张振国.
  黄×× is redacted in the SOURCE itself (a turncoat's given name).
- The 5 sections: 忍/等/狠 (Endure, Wait, Strike Hard); 取信于蒋介石的方法
  (winning Chiang's trust); 对权贵的拉拢和运用 (cultivating the powerful);
  对待叛徒的手段 (methods with turncoats); 和毛人凤的生活片断 (life fragments).
- NEXT TURN: crop-verify numbers during translation, translate all 89 paras,
  run the 5 gates, notes + glossary (many new: 张严佛/邓文仪/杨宣诚/马汉三/毛森/
  俞济时/黄显声/瞿梦秋/余乐醒/王凌云-no/etc.; 张国焘 attested), build, qa, commit.
  Watch for consistency: 邱开基/李毓桢/周伯先/何绍周/叶翔之 already glossed.
  The 忍等狠 pun and the gambling pun (宋子文/刘纪文 = 送几文/留几文) need notes;
  王佐断臂 allusion (line "学一学王佐") needs a note.

### ch17 (我受命暗杀杨杰将军的经过 / How I Was Ordered to Assassinate General Yang Jie) - DONE

- PDF 338-341, printed 319-322. 13 body paragraphs (last is the byline
  沈美娟记录整理). Full pipeline. Shen's confession of the order to kill Yang Jie,
  his mother's intervention (the "my mother's words" episode ch14 alludes to),
  and Yang Jie's eventual HK assassination.
- Ledger 6 fixes, crop-verified: title 腊杀/将盏 -> 暗杀/将军, 严燮成 (tuo-tea
  king, NOT 严楼成/严赤成), 韩世昌 (agent, NOT 韩址昌), 叶羯之 -> 叶翔之.
- TWO cross-chapter catches into ch14 (re-ran ch14 gates green, re-committed):
  (1) ch14's tuo-tea king was 严肖成/"Yan Xiaocheng" — crop of p284 shows
  严燮成 (Yan Xiecheng); corrected in ch14 text + glossary. (2) 李宗理 appears
  in BOTH ch14 (para77) and ch17 as the friend whose handwriting the assassins
  forged — it is Li Zongli, NOT the acting president Li Zongren. I first
  "corrected" ch17 to Li Zongren, then a corroborating source (and ch14's own
  context) confirmed 李宗理 = Li Zongli; reverted, and fixed ch14 para77 too.
- Address inconsistency in the SOURCE: Shen's Kunming home is 靖园新村 in ch14
  and 靖国新村 here; rendered uniformly "Jingyuan New Village" with a glossary
  note recording the variant.
- Checks: parity 13/13, align OK, content OK, numbers 0, register in tolerance.
- Notes: 5. Glossary +6 (严燮成/龙泽汇/韩世昌/朱健飞/沈美娟 + place 靖园新村).
- Corroboration (no Grok): Yang Jie assassinated 19 Sep 1949 at Wu Jicheng's
  flat on Hennessy Road, en route to the first CPPCC; martyr; Ye Xiangzhi's
  team did it -- corroborated (Wikipedia, rmzxw, 163). Discrepancy noted: Shen
  names the agent Han Shichang, the record names the shooter as Chen Jiaqing.
- VOICE-DRIFT FLAG (fable pass): the mother's speech is the chapter's one big
  block of reported dialogue -- contractions are concentrated there by design;
  confirm the expository frame stays clean. shall% 25% (mother's "shall").

### ch16 (阴谋诬陷中共的一个例证 / A Case of Framing the Communists) - DONE

- PDF 334-337, printed 315-318. 12 body paragraphs + a ### subtitle
  (李公朴、闻一多被暗杀案侧记). Full pipeline from scratch. A side-record on the
  1946 Li Gongpu / Wen Yiduo assassinations: the plot to plant false confessors
  implicating the CCP, and the double-impersonation of the two men publicly shot.
- Ledger 16 entries, ALL crop-verified. The culprit 霍揆彰 (Huo Kuizhang) was
  OCR-scattered (霍把彰/霍抄彰/雹扎彰/替搂彰 -> 霍揆彰); also 刘一戈 (not 刘一龙),
  龚少侠 (not 奢少侠), 王巍 (station chief, not 王狗/王寿), 李毓桢, 酃县 (hometown),
  洞庭湖 (Huo's wartime post), and the two prisons 白公馆/渣滓洞 (OCR
  电公馆/洼淳洞) -- I had first translated those literally as "Dianzi mansion /
  Wachundong"; caught by crop.
- Checks: parity 12/12, align OK, content OK (after Shenxiandong glossary match
  + restoring 三个人/三老板 counts), numbers 0, register in tolerance.
- Notes: 7. Glossary +13 (霍揆彰/王凌云 attested; the rest provisional; 无为寺/
  神仙洞/嵩庄 places). Prisons 白公馆/渣滓洞, Tang Zong, SACO all noted earlier.
- FLAG FOR WINSTON / GLOBAL CASCADE: glossary renders 渣滓洞 as "the Bath Cave
  (Zhazidong)" (status: decided), but its own glossary note says the name means
  'dross pit' -- "Bath" looks like an error for "dross/dregs". Used the decided
  form here for consistency (5+ chapters use it); recommend a global correction
  to e.g. "the Dregs Cave (Zhazidong)" cascaded across ch03/ch05/ch07/ch13/ch16.
- CONSISTENCY: the same Wang Wei (王巍) is Yunnan station chief here (1946),
  station chief again later, and Kunming police chief by 1948 (ch14/15) -- one
  referent, one glossary entry; the ch14 "Wang Zhi" error was corrected.

### ch15 (昆明七一五 / The Kunming Fifteenth of July) - DONE

- PDF 325-333, printed 306-314. 29 body paragraphs, ~5,600 CJK chars, 1 section
  heading. Rendered / OCR'd / assembled fresh this session. The 15 July 1948
  suppression of the Kunming student movement (the siege of Huize Hall).
- Ledger 13 entries, all crop-verified against the scan. The Kunming police
  chief was OCR-scattered across eight garbles (王猎/王帮/王岗/王狗/王几/王并/
  王效/王狠) -> all 王巍 (Wang Wei); also 能庆来->熊庆来 (Xiong Qinglai),
  朱景上院->朱景暄, 李航想->李毓桢, 周介先->周伯先, and the title 屁明->昆明.
- CROSS-CHAPTER FIX: crop of ch14 p280 showed the same police chief is 王巍,
  not 王峙 -- ch14 had shipped "Wang Zhi". Corrected ch14 ledger + reading
  (Wang Zhi -> Wang Wei) and re-ran ch14 gates (still green). Also closed a
  glossary-coverage gap: 何绍周/谢崇文/杨文清/周伯先/杨文智 were never in the
  glossary though they appear in ch14; added now, so content-check validates
  them across both chapters (ch14 name occurrences rose 412 -> 443).
- Checks: parity 29/29, alignment OK, content OK, numbers 0 (no noise additions
  needed), register in tolerance (contr/1k 23.8, shall 33% -- He Shaozhou's
  reported speech; flagged for the fable pass).
- Notes: 11. Glossary +29 (people + 会泽院/南菁中学 places). 熊庆来 and 何绍周
  attested; the rest of the local cast provisional. Students named as victims
  (温宗江、白明顺、王友珍、傅金德、董德平、金维和) all crop-verified and glossed.
- Corroboration (no Grok): the 云南七一五运动 and the 会泽院守卫战 -- corroborated
  (Wikipedia, Yunnan University history); the June 1948 反美扶日 march to the US
  consulate with a protest to Truman -- corroborated. TWO undercounts flagged
  as memoir-vs-record notes: Shen says 300+ arrested / 3 months, the record says
  ~1000 / ~half a year; Shen says the march was 30,000+, the record says ~10,000.
- VOICE-DRIFT FLAGS for the fable pass: shall% 33% is high (He Shaozhou's lines
  -- "you shall", "I shall"); confirm the expository frame stays contraction-
  light. Idioms rendered literal with notes (釜底抽薪, 猛张飞/诸葛亮, 救救孩子).

### ch14 (云南解放前夕军统在昆明的特务活动 / Juntong Operations in Kunming on the Eve of Yunnan's Liberation) - DONE

- PDF 276-324, printed 257-305. 135 body paragraphs, ~33,500 CJK chars,
  8 section headings. The largest chapter after ch13; the Yunnan/Kunming
  chapter, ending in Lu Han's 9 Dec 1949 uprising.
- Ledger 322 entries. IMPORTANT: fixed a prior-session ledger bug -- entry
  {户 -> 卢(context)} had the literal placeholder "(context)" in its `right`,
  which corrupted 31 spots (all "卢(context)") AND over-converted 暴发户
  (nouveau riche) to 暴发卢. Corrected `right` to 卢, restored 暴发户, realigned
  the 卢千不住->卢靠不住 workaround. Also removed two gutter-garbage strings
  (`se 300 ae`, the `(context)` token) and two real single-char OCR errors:
  百趋->直趋 (直趋四川) and 虎黄->虎贲 (the 57th Div. code name, same 虎贲 as
  the novel title in the same sentence -- I had first translated the OCR error
  literally as "Tiger-Yellow"; corrected to "Tiger Braves").
- Checks: parity 135/135, alignment OK, content OK (after fixing 5 displaced:
  Ye Xiazhai->Ye Xiadi to match glossary, "Chiang clique"->"Chiang Kai-shek
  clique" x2, and two dropped Kunming place-names). Numbers 0 after adjudicating
  34 flags: dominant false positive was 余程万 (Yu Chengwan, 万->10000) and
  五华 (Wuhua, 五->5); added to noise with 一本万利/万岁/万状/敖万华/两手/
  两回事/两天/三节桥/十两黄金/一百二十个不愿意/三百八十. Seven real quantities
  reworded to checker-parseable English (hundred-odd->over a hundred; 十万->
  a hundred thousand ...strong; 三个室/科->"three offices/sections"; 四十四人->
  "forty-four people led by"; 三个人->"the three of us"; 十余弹->"over ten
  bullets"). Register in tolerance.
- Notes: 24. Glossary +12 people (Li Mi, Yu Chengwan, Long Yun, Chiang
  Ching-kuo, Huang Shaohong attested; Shi Butian, Shen Yanshi, Li Chufan,
  Tong Helian, An Enpu, Chen Fuguang, Ma Bo'an provisional). Lu Han / Ye Xiadi
  / Xi'an Incident already noted earlier -- not re-noted.
- Corroboration (no Grok/Grokipedia): Li Gongpu (11 Jul 1946) & Wen Yiduo
  (15 Jul 1946) assassinations by the Bureau's Kunming station -- corroborated
  (people.cn, chinanews, Baidu Baike; gunman Cai Yunqi executed 1958);
  September 9 affair (九九整肃, ~400 arrested, Lu Han stalled and released) --
  corroborated; Huang Shaohong Hong Kong declaration, 44 signatories incl. Long
  Yun, Aug 1949 -- corroborated; 虎贲万岁 (Zhang Henshui, 1945, on Yu Chengwan's
  Changde defence) -- corroborated; Lu Han's 9 Dec 1949 uprising (~40,000
  troops, the seven commanders detained at Wuhuashan) -- corroborated in
  outline. Shen appears in the sources as a 九九 planner and one of the seven
  detained, exactly as the memoir has it.
- SELF-SERVING (category-4 note, anchored "my mother's words"): the chapter's
  spine is Shen's account of delaying three assassination orders (Yang Jie,
  who reached Hong Kong; An Enpu / Xie Chongwen / Long Zehui). He supplies
  motives -- fear of capture, a lost cause, his mother's reproach -- for acts
  he otherwise admits. Noted so the read-through weighs the framing against the
  deeds.
- VOICE-DRIFT FLAGS for the final fable-5 pass (this chapter was done on Opus
  after the model-guard was lifted -- see CLAUDE.md): register gate passed
  (contr/1k 15.4, 1.00x vs ch01) but Opus may over-contract the expository
  frame; spot-check contraction placement in narration vs reported speech.
  The seven reworded number-phrases (above) traded a little idiom for
  checker-parseability -- confirm none reads flat.
- Harmless stale ledger no-ops (prior OCR variance, permanently "not found",
  do not affect output): 童稚莲 p297, 滥事污芒共产党 p285, 一序年龄 p319,
  《虎资万岁》 p289.

### ch13 (中美特种技术合作所内幕 / Inside SACO) - DONE

- PDF 229-275, printed 210-256. 126 body paragraphs + preamble, 10 section
  headings (the 美帝海军与陆军 / 争夺对中美所的领导权 title spans two source
  lines, merged into one in English). THE LARGEST CHAPTER IN THE BOOK, done.
- ~380 ledger entries. Every American and Chinese name crop-verified: Miles,
  Xiao Bo, Guo Dequan, Depass, Knox, Luce, Donovan, Cooke, Wedemeyer,
  Marshall, Nimitz, Kotrla, White; 李崇诗, 沈维翰, 徐人骥, 龚仙舫, 王芃生,
  周至柔, 林可胜 (=Robert Lim), 顾祝同, 费巩, 竺可桢, 皮宗阚, and the author
  in his own roster (沈醉). Two embedded page-number junk strings and three
  real single-char OCR errors caught by check_numbers (士兵/埋葬/天雨).
- TRAP AVOIDED then HIT: wrote to a WIP path per plan, but the parity check
  caught that I had skipped the opening preamble paragraph (SACO's English
  name) AND misplaced the first section heading -- fixed, 126/126.
- GLOSSARY CASCADE: 林可胜 set to the attested 'Robert Lim' (cascaded to ch03
  + its note anchor); 贝乐利->Bei Leli and 桂林->Kweilin unified across ch13.
- Checks: parity 126/126, alignment OK, content OK (after Bei Leli/Kweilin/
  Robert Lim/Chungking-Xifeng reconciliations), numbers 0 after adjudicating
  ~24 flags (names/places/idioms/counters to noise; 3 real OCR fixes; a few
  compound numbers reworded to digits), register in tolerance.
- Notes: 27. Glossary +55 (457 total).
- THE KEY FINDING for the read-through: the Fei Gong passage. Fei Gong was
  abducted and murdered by SACO agents (body destroyed in nitric acid,
  5 March 1945; martyr 1978), and Shen -- who ran the two-month 'search' --
  calls it 'a mystery.' The note lays out the documented truth against Shen's
  silence; this is the book's sharpest case of the gap between the page and
  the record, exactly what the apparatus exists to mark. Corroboration also
  run on SACO's structure and Miles (Wakeman's Spymaster; Miles's own memoir)
  -- Shen's account is broadly borne out. Miles's seven-star-flag origin
  story is flagged as almost certainly Juntong lore.
- NO Grok/Grokipedia used (a Grokipedia SACO page surfaced in search and was
  ignored per standing rule).

- PDF 229-275, printed 210-256. THE LARGEST CHAPTER IN THE BOOK: 126 body
  paragraphs, ~32,000 CJK chars, 11 section headings -- roughly 3x a normal
  chapter. Rendered, OCR'd, indents measured, assembled.
- Section titles crop-verified and in the ledger: 中美特种技术合作所内幕,
  成立经过, 前后三次签订的合同概要, 组织、人事及活动情况, 美帝特务的活动情况,
  梅乐斯的罪恶活动, 美帝海军与陆军争夺对中美所的领导权 (ONE title split over
  two source heading lines -- blocks 109+110; merge into one ## in English),
  为求美特欢心举行的几次盛大宴会, 蒋介石最欣赏美国刑具, 任务未完先行结束.
- WHEN RESUMING: this chapter carries three contract texts and a large cast of
  American names to crop-verify -- Miles (梅乐斯), Xiao Bo (肖勃), Guo Dequan
  (郭德权), Depass/迪帕斯, Knox (诺克斯), Luce (鲁斯 = Henry Luce of Life),
  Bergholz (贝乐利), plus the SACO org roster (李崇诗/李崇许?, 何芝园, 沈维翰,
  徐人骥, etc. -- all need crop-verify). Budget it as a multi-session unit;
  do NOT write a partial ch13_reading.md that fails parity.

### ch12 (旧社会里的鸡鸣狗盗和侦缉人员 / Thieves and Detectives in the Old Society) - DONE

- PDF 212-228, printed 193-208. 51 body paragraphs, 51 translated. The
  longest chapter so far. A folkloric-turned-savage account of the Shanghai
  underworld and the detective police who fed off it: gang geography, thieves'
  argot, the master-thief Wang Huzi, the honey-trap and post-office cases,
  and then the private-torture / 'living teaching material' passages that turn
  the chapter from color into indictment.
- 196 ledger entries -- the heaviest yet, because the chapter is dense with
  argot the OCR shredded and with two embedded page-number junk strings
  (205, TO606) sitting INSIDE words, which check_numbers caught as phantom
  quantities. Both stripped. Crop-verified: 王鹤 (Wang Huzi's real name),
  杨虎 (garrison commander / gang boss), 吴乃宪, 饶伯泽, 李连福, 许忠五,
  李筱宝, 黄加持, 车重光, 胡葆文, 哥伦比亚路二十二号, 卢英, 顾纪生, 李虎臣
  (a detective -- NOT the general of ch07; same characters, noted).
- REGISTER: this chapter lives on its slang. The argot terms (吃硬钱/吃洋火钱,
  撕露水/收灯油/掀帘子, 亮相, 吃讲茶, 拆白党, 替罪羊, 活教材) are translated
  for sense with the literal image kept, and each carries a note -- the notes
  ARE the register apparatus here (42 notes, the densest in the book).
- Checks: parity 51/51, alignment OK, content OK, numbers 0 after adjudicating
  ordinals/counters/a-name to noise (第二步/三角架/四乡/周百先/四十多万) and
  the two junk strings, register in tolerance.
- Glossary +23 (410 total).
- CORRELATION note for the read-through: the '活教材' and tiger-bench passages
  are the clearest self-incrimination in the book -- Shen recording torture as
  pedagogy in a flat procedural voice. That flatness is the evidence; the
  notes flag it rather than let the English round it off.

### ch11 (胡宗南和戴笠、毛人凤的关系 / Hu Zongnan's Relations with Dai Li and Mao Renfeng) - DONE

- PDF 199-211, printed 180-192. 40 body paragraphs, 40 translated. The Dai
  Li / Hu Zongnan partnership from the inside: the 1937 hospital meeting, the
  mutual puffery, the gift-diplomacy, Hu's wife Ye Xiadi, the shared carve-up
  fantasy, and the 1947 discovery of Communists in Hu's own secretariat.
- 160 ledger entries. THE CHAPTER'S SYSTEMATIC MANGLE: the name/pronoun for
  Hu (胡) was OCR'd as 明/妆/衣/硼/阴/朝/大 in scattered places, and Chiang
  (蒋) as 头/萝/送/戎/藉 -- every one context-checked before replacement
  (衣/头/大 are real words). Crop-verified: 陈质平, 曹圣芬, 熊斌, 祝绍周,
  俞作柏, 叶霞弟, 魏大铭, 杜逵, 陈洁如, 蒋纬国, 范长江, 平凉, 董钊, 狂嫖滥赌,
  当着胡的面 (x2), Hu's parting line 多辛苦点.
- REGISTER: kept 另一个老婆 ('Chiang's other wife') for Chen Jieru as Shen
  wrote it -- my draft had softened it to '前妻/former wife'; reverted against
  the scan and noted. The flat designation is evidence.
- Checks: parity 40/40, alignment OK, content OK after fixing two anchors
  (para 3 needed 'Dai Li' spelled out; 延安->Yenan), numbers 0 after noise
  adjudications (万能/千方百计/万分/千万), register in tolerance.
- Notes: 23. Glossary +45 (387 total).
- Corroboration: Ye Xiazhai/叶霞翟 (book prints 叶霞弟) -- Dai Li's Hangzhou
  student, Guanghua, Wisconsin PhD, married Hu 1947: corroborated; her family
  disputes the intelligence-work and mistress colourings, noted. The 1947
  Communists-in-Hu's-secretariat passage matches the Xiong Xianghui (熊向晖)
  network -- Zhou Enlai's mole, Hu's confidential secretary, leaked the 1943
  anti-Border-Region plan; the network left for study abroad ~May 1947, none
  caught, so Shen's autumn-1947 'discovery' is the service finding traces
  after the birds had flown. Documented and noted in full.

### ch10 (军统对陕甘宁边区的罪恶活动 / The Juntong against the Shaan-Gan-Ning Border Region) - DONE

- PDF 189-198, printed 170-179. 33 body paragraphs (4 sections), 33
  translated. The Juntong's decade-long, mostly-failed campaign to penetrate
  Yenan: early Xi'an training classes, Zhang Guotao's research office, the
  infiltration doctrine, and the assassination teams sent after the CCP
  leadership.
- 137 ledger entries -- the heaviest name load in the book so far. THE BIG
  ONE: 张国焘 = Zhang Guotao, CCP founder and Mao's rival, defected 1938;
  OCR had mangled him to 张国春/张国森 throughout. The personnel chief 龚仙舫
  was mangled five different ways (黎/获/缆/约/奢仙盘). All crop-verified:
  薛志祥, 黄逸公, 程慕颐, 耀县, 于斌, 袁寄滨, 枣子岚垭/漱庐 (guest house;
  my provisional 罗家湾/激庐 corrected against the scan), 娄剑如, instructors
  为教官.
- Checks: parity 33/33, alignment OK, content OK after a glossary cascade
  (see below), numbers 0 after noise adjudications (李友三/四川/中四路/乐山),
  register in tolerance.
- GLOSSARY CASCADE: my ch10 draft wrote 延安 as 'Yan'an' and 汉中 as
  'Hanzhong'; the established renderings are 'Yenan' (ch01/ch03 period form)
  and 'Hanchung' (ch03). Both cascaded to match. 延安 and 汉中 pinned in the
  glossary as decided.
- Corroboration: Zhang Guotao's 1938 defection, forced admission to the
  Juntong at Chiang's insistence, major-general headship of the Special
  Political Problems Research Office, and Dai Li's treatment of him as a
  display piece -- all corroborated. Shen Zhiyue's Yenan infiltration (Kangda,
  Party membership, central organs, return 1941) corroborated; Shen Zui's
  studied vagueness about a fellow-Shen he envied is noted. Xu Foguan = the
  later New Confucian philosopher Xu Fuguan, corroborated. The assassination
  programme is Shen's uncorroborable inside testimony, flagged as such.
- Notes: 21 at ~2/printed page. Glossary +36 (354 total, after the two
  reconciliations).

### KNOWN DEBT for the final consistency pass (found during ch10)

The book is internally inconsistent on province/city romanization, inherited
from the early chapters: Szechwan (8) vs Sichuan (21), Kweichow (2) vs
Guizhou (15), Chengtu (period, 5) vs none, Peiping (5) vs Peking (5). The
deliberate period forms are Chungking/Nanking/Peiping/Yenan/Chengtu; the rest
should probably go pinyin. This is a global correction to run in one grep-
driven cascade at the end, NOT chapter by chapter. Left as-is for now so the
line keeps moving; recorded here so the final pass catches it.

### ch09 (交通警察总队是一支什么样的反动部队 / The Traffic Police Corps) - DONE

- PDF 187-188, printed 168-169. 5 body paragraphs (title spans two source
  heading lines), 5 translated. An institutional primer written explicitly
  as a gloss on the Selected Works of Mao Zedong, vol. 4 -- noted as the
  clearest dating marker in the book so far.
- 26 ledger entries. Crop-verified: 歙县雄村 (OCR 庚县), 陶一珊 (OCR 陶一副),
  临汝风穴寺 (OCR 临改风灾村 -- a temple turned into a disaster village),
  建瓯, and the whole corps-commander roster: 张国梁, 彭自强, 汤毅生, 朱赓扬,
  李骧. Weapons list: the scan prints roman 'UD' (UD M42 submachine gun);
  OCR read 0UD. 曲尺 rendered 'automatic pistols' (service slang, carpenter's
  square silhouette), not Mausers.
- Checks: parity 5/5, alignment OK, content OK, numbers 0 unresolved on
  first run, register in tolerance.
- Notes: 8 at 4/printed page (short chapter, dense referents).
  Glossary +26 (328 total).

### ch08 (蒋介石阴谋暗杀李宗仁的内幕 / Chiang's Plot to Assassinate Li Zongren) - DONE

- PDF 183-186, printed 164-167. 8 source paragraphs (1 heading), 7 body
  paragraphs translated. Short chapter: Shen's first-person account of the
  1948-49 assassination plot he personally led against acting-president Li
  Zongren, and its coda when Li, returned from the US in 1965, read Shen's
  own published account of it over lunch.
- 34 ledger entries, all applied. Crop-verified: 和蔼, 装出, 飞鸟, 寝室,
  爬墙, 蒋贼/蒋匪 (the epithets Shen gives Li Zongren -- load-bearing for the
  chapter's register, crop-verified), 留下...捣乱. Names restored: 潘其武
  (Pan Qiwu, OCR 讨其武), 郭德洁, 尹冰彦.
- Checks: parity 8/8, alignment OK, content OK, numbers 0 after one noise
  adjudication (万万想不到 parsed as 20000), register in tolerance.
- Notes: 15 at 3.75 per printed page (dense: the chapter is short and every
  name is a principal). Glossary +12 (306 total).
- REGISTER NOTE for the read-through: this is the fullest confession of a
  directed political murder in the book, and it is the one that failed. Shen
  tells it completely precisely because no one died -- the professional
  killer's competence is displayed as pride even inside the self-criticism
  frame. The 1965 coda, ending by adopting Li's 'Chiang the bandit,' is the
  1962-66 moment doing its work through reported speech; noted as such.
- The 美龄号 plane-as-bait story is Guo Dejie's account via Shen and is
  uncorroborated outside these memoirs; Shen's own testimony establishes the
  plan to down Li's plane but not that the Meiling was the lure. Noted.

### FOR WINSTON'S READ-THROUGH, ch07

- 杨氏佳城 / 龙蟠虎踞: the tomb passage turns on all three characters of
  Yang Hucheng's name standing in the stone. Untranslatable; the note
  explains it. Check whether the note carries it clearly enough.
- The onomatopoeia of the warning shot (OCR gave 只) is unreadable at
  available resolution; rendered as plain 'the crack of a shot'.
- 张严佛-style uncertain identifications this chapter: 杨光 (common name),
  邓匡元/徐羽仪/陈国祯 (Xifeng magistrates), 陈宝琪 -- all provisional in
  the glossary.

### FOR WINSTON'S READ-THROUGH, ch06

- 李仲桢 for the Xiuwen county magistrate is provisional: the scan prints an
  OCR-resistant name (machine read 李和久桢), not confirmable at available
  resolution, and no outside source for the appointment was found.
- Shen's "sixth Whampoa class" for Liu Yiguang and "1943" for Yu Fengzhi's
  departure are both contradicted by outside accounts; both kept as written
  and noted, per the register contract (his errors are evidence).
- 南京总台指定专机日夜不停地收听 -- 专机 crop-verified as printed; read as a
  dedicated radio set at the Nanking head station, not an aircraft. If you
  read it otherwise, say so.

### FOR WINSTON'S READ-THROUGH, ch05

- Two provisional readings not confirmed against the scan: 悻悻地走了 and
  悻悻走了 for Chen Cheng's departures (OCR gave 缴幻/缴缴). The sense is clear
  from context but the characters were not legible at the resolution I had.
- The chapter is the strongest material in the book so far and the least
  self-serving. Shen Zui's errand throughout is to soften Ye Ting by comforts
  and bring him over to Chiang Kai-shek; he reports its failure, Ye Ting's
  refusal to cut his hair, and Dai Li's closing remark, without mitigating any
  of it. His admission that he understood nothing of what Ye Ting meant by
  asking to have his Party membership restored is doing the work the 1962-66
  framing required, and is also, on the evidence, probably true.

### FOR WINSTON'S READ-THROUGH, fm01

- The scholarship pass is **not yet run** for this unit. The twelve notes rest
  on general knowledge of the period and are written to be checkable; claims
  that need external verification (the Lixingshe founding roster, Feng Ti's
  execution, the Dai Hill crash site) are flagged as such in the note text
  rather than asserted flatly. Per the skill's cost model, research is batched
  across several chapters rather than run per chapter — that pass is pending.
- The book prints 戴山 for the hill Dai Li's aircraft struck, where other
  sources give 岱山. Preserved as printed and noted; not silently corrected.

### ch01 (军统培训特务的内幕 / Inside the Juntong's Training of Agents) - DONE

- PDF 20-47, printed 1-28. 97 source paragraphs, 92 translated (declared -5:
  see the song appendix below). 5 sections.
- Crop verification caught 13 more source errors, including **the author's own
  name**: 沈醉 was OCR'd 沈醇 in the one paragraph where he lists himself among
  the staff. Also 王尝五→王崇五, 薪镇南/菏镇南→蒋镇南, 严杰/严你→严燮 (the
  student beaten to death in a training bout), 喜铭易→袁铭鼎, and 正是需要二部
  →正是需要干部.
- Checks: parity OK with the declared exception, anchors 45/45, numbers
  0 unresolved across 92 pairs, headings consistent, register within tolerance.
- Notes: 45, i.e. 1.6 per printed page, against 3.0 in fm01 and 2.3 in fm02.
  Deliberately not padded: a third of this chapter is personnel rosters -
  ninety-odd names of company commanders and platoon leaders - which need no
  glossing and would not be improved by it. The density is where the material
  earns it, and this is the justification on record.
- Glossary: +42 entries (117 total).
- EPUB rebuilt: 3 documents, 125 paragraphs, 71 notes, qa_epub PASS.

### THE SONG APPENDIX - a decision Winston should confirm

The chapter ends its second section by printing the full lyric of the class
song, which became the Juntong's own anthem. That lyric is characterised in one
editorial block rather than set out line by line; the two lines Shen Zui himself
singles out, and on which his whole argument rests - the leader's safety before
the state's territory - are quoted in the body where he makes the point. The
departure is declared in `book.json` as a parity exception with a written
reason, printed on every run of the structural check, and the QC file folds the
same run so the numeric check stays aligned. Say if you want the lyric rendered
in full instead; it is four lines of conventional period exhortation and
nothing in the argument turns on it.

### The numeric check earned its keep this chapter

17 flags on first run, all adjudicated: 3 were OCR errors in the source, TWO
WERE REAL OMISSIONS IN MY TRANSLATION - a dropped "four rounds" from Tao
Yishan's mahjong remark, and a dropped "two" from "the two specialities of
telecommunications and accounting" - and the other 12 were names containing
numerals (王崇五, 王百刚, 周万尝) and period idioms. Fixes made:
- English ordinals now resolve, so 十六兵团 as "Sixteenth Army Group" and
  第二十六军 as "Twenty-Sixth Army" stop reading as dropped unit numbers. Unit
  numbers are load-bearing and must not be silenced as noise.
- Project noise moved to `data/noise.txt` and applied BEFORE the built-in list,
  not after. The generic 两[三边] was eating the front of the project's 两三百
  and leaving a bare 百 - the same prefix-eating trap as inside NOISE, one
  level up.

### ch02 (抗战前军统特务在上海的罪恶活动) - TRANSLATED, checks incomplete

- PDF 48-90, printed 29-71. 117 source paragraphs, 117 translated, parity OK.
- 30 source OCR errors recorded and replayed, including six separate manglings
  of one name (吴乃宪) and four of another (程慕熙). Crop-verified: 唐腴庐,
  车耀先, 邹韬奋, 高巩白, 吴乃宪. The Cui Wanqiu passage - Zhang Chunqiao
  writing as Di Ke against Lu Xun, and Lan Ping at Cui's house - reads as
  printed; it is the most historically loaded claim in the chapter and it was
  checked against the scan rather than trusted to OCR.
- STILL TO DO on this chapter: the numeric check has 46 flags outstanding,
  unadjudicated (the count rose with the corrected segmentation, which
  restored text the folio bug had removed). On ch01 the same first pass was 17 flags of which two were
  real omissions in the translation, so these must be worked through, not
  waved past. Notes not yet written. Not yet built into the EPUB.

## A pipeline defect that cost the afternoon, and what it changed

`strip_folio` decided whether a page's last line was the printed page number
by looking at the TEXT: short, at most one Han character, dot-delimited. That
rule deleted a real line - a paragraph whose final line was 写。 - and with it
the paragraph break that followed, silently merging two paragraphs of the
book. It was found only because chapter 2's parity came out one over and the
scan was consulted to see why.

Silent deletion of text is the worst defect this pipeline can produce after
invented text, so the guess was replaced by a measurement: a folio sits below
a gap 1.35x the leading and is a few glyphs wide against a full measure.
Sampled over the book it finds a folio on 71 of 72 pages, and where it is
unsure it KEEPS the line, which is the right direction to fail in.

Restoring those lines then exposed a second problem. The short-last-line rule
for paragraph ends is right inside a page and wrong at the foot of one, since
a page's final line is short whenever the text block ends there. So paragraph
segmentation now uses the printed INDENT, measured off the page image by
`scripts/indents.py` - the mark the typesetter actually made. Two things had
to be got right for it to work, and both were got wrong first:
- the flush-left margin is measured GLOBALLY rather than per page, because
  twenty-odd lines are too few to locate it and a skewed page produces a
  second cluster;
- it is measured SEPARATELY for recto and verso, because the gutter mirrors.
  A single margin sat between the two and read one side as all-indented.
- at the top of a page the indent is not trusted at all; there the previous
  page's short last line decides.

Chapter 2's source came out at 117 paragraphs under this scheme - the exact
count the translation had independently reached from reading the scan, after
the earlier segmentation said 116. That agreement is the reason to believe it.

### CONSEQUENCE FOR THE THREE FINISHED UNITS - work outstanding

fm01, fm02 and ch01 were translated against the OLD segmentation, which was
missing the lines the folio bug had eaten. Their prose is unaffected and every
other check on them still passes, but their paragraph COUNTS no longer match
the corrected source: fm01 19 against 18, fm02 18 against 15, ch01 95 against
92. In each case the book splits a paragraph where the translation runs two
together. The fix is to insert paragraph breaks at those points - checking
each against the scan, not against the count - and to recompute ch01's
declared song-appendix exception, which was written against the old numbering.
This is bookkeeping, not retranslation, but it is not done.

## SEGMENTATION: RESOLVED, and the root cause

The previous session recorded that this had not converged and warned against
tuning thresholds. Following that note, the detector was validated against the
pages themselves before anything else was touched -- and it was exact: six
indents of six on one sample page, three of three on another, no false
positives. The detector was never the problem.

THE ROOT CAUSE was that the indent was being measured off the page image in
one pass and the text produced in another, then matched BY LINE INDEX.
Tesseract's line grouping is not the printed line banding -- it merges and
splits lines of its own accord -- so the two disagreed on 140 of 515 pages,
and each disagreement slid every paragraph mark below it one line out of
place. That, not any threshold, is what made the counts wander for hours.

THE FIX: take the indent from the same tesseract pass that produces the text.
`--psm 6 txt tsv` yields a bounding box per word and so a left edge per OCR
line, and the reference margin is the mode of the line starts on that page.
Same pass, same lines, no alignment step to get wrong. Misaligned pages went
from 140 to 0. No global margin, no recto/verso calibration, no page-top
special case, no short-line fallback -- all of those were scaffolding for a
problem that no longer exists.

Two further defects fell out of it:
- Folio-derived pseudo-headings. `find_headings` had recorded two page numbers
  as section titles ('.5，' and '到'); assemble was injecting them into the
  source as '### ' lines, which both split a paragraph mid-sentence and put
  junk in the text. Dropped: a heading has at least two Han characters.
- Every break is still gated on sentence-final punctuation, which is what
  makes the result safe by construction rather than merely correct today.

RECONCILIATION DONE. All four translated units now match the corrected source
exactly: fm01 18/18, fm02 16/16, ch01 91/91, ch02 115/115. The adjustments
were paragraph joins and one split in the ENGLISH, plus removal of ch01's
song-appendix parity exception, which was an artefact of the old segmentation
-- the book sets that lyric as a single paragraph, which is how the
translation renders it. No prose was rewritten. There are now no parity
exceptions anywhere in the book.

## THE FOLIO FILTER WAS STILL DELETING TEXT, AND IT REACHED CHAPTERS 1-4

Found while assembling chapter 3, by chasing a single stray character. The
source read "...与处相等的室、人。" where 人 made no sense. The scan showed the
book prints a whole line there that the OCR did not have:

    区、组，还有几个委员会，内勤达到一千多人，外勤增至五万多

A line carrying two of the Juntong's strength figures, silently gone.

THE MECHANISM. `strip_folio` popped a page's last OCR line whenever
`folio_present` said the page had a printed folio. But `folio_present`
profiled the WHOLE page while the text it judged came from the CROPPED image.
Where the crop bottom (0.905) fell above the folio, the crop had already
removed the page number, tesseract's output ended on real prose, and the pop
deleted that prose. In chapter 3 the folio falls outside the crop on 24 of 59
pages: 41% of pages lost their last line.

WHY NOTHING CAUGHT IT. A line deleted from the middle of a paragraph changes
no paragraph count, so parity passed. The previous session's reconciliation
("all four translated units now match the corrected source exactly") was
matching the translation against an already-damaged source. Two derived
artifacts agreeing with each other, again.

THE FIX. Deletion now requires the geometric AND the textual signal to agree,
and where they disagree the line is KEPT. Neither signal is sound alone: the
geometry is what ate the line above, and the text-only rule is what once ate
写。. A full folio carries digits; a folio the crop clipped keeps its dot
delimiters, and Chinese typesetting forbids a line opening on sentence-final
punctuation, so a short line starting with 。 is not prose either.

REJECTED: widening the crop to 0.970 to swallow the folio whole. It does fix
the folio, and body text (max 0.9173) and folios (from 0.8868) genuinely
overlap so no crop line separates them -- but a taller image regroups psm 6's
lines, which broke heading matching (chapter 4's title merged into its first
paragraph) and moved settled paragraph counts. Reverted to 0.905.

CONSEQUENCE FOR THE FINISHED UNITS - now resolved. Corrected source counts
came out fm01 18, fm02 16, ch01 93, ch02 116, ch04 20, against translations
of 18/16/92/115/19. Every shortfall was a paragraph BOUNDARY, not lost prose:
the eaten line carried the indent that marked the break, so two paragraphs ran
together. `reflow.py` re-laid ch01, ch02 and ch04 onto the corrected
boundaries. No prose was rewritten and none was found missing.

State after the repair: parity OK on all five units, and check_align reports
no pair straying from the median on any of them.

## A TRUNCATION BUG IN MY OWN READING, AND WHAT CAUGHT IT

Reading assembled source with `cut -c1-700` to keep chunks manageable. `cut -c`
counts BYTES, not characters, so on UTF-8 Chinese the window was really about
233 characters. Twenty-one of chapter 3's first 96 paragraphs were translated
only as far as that cut, losing the second half of each -- including the whole
middle of the Inspectorate's staffing paragraph (the three recalled deputy
inspectors-general), the wireless-registration and interception passage, the
Kong Lingjun confrontation, Liao Gongshao's traitor relations, and the entire
close of the chapter's detective-brigade section.

Nothing in the prose showed it: every truncated paragraph ended on a complete
English sentence. `check_align.py` caught it, because the ratio of English
characters to Han characters collapsed on exactly those pairs. That check was
written for a different failure (source and translation slipping past one
another) and found this one for free. It is the reason to keep ratio checks
even when parity passes.

All twenty-one repaired against the full source, with the OCR in the recovered
tails crop-verified like the rest. ch03 now reports "alignment OK: no pair
strays more than 2.2x from the median" across all 96 translated paragraphs.

Reading the source in fixed-size chunks is now done by paragraph index in
Python, never by `cut`.

## THE SENTENCE-END GATE DID NOT KNOW ASCII PUNCTUATION

`assemble.py` gates every proposed paragraph break on the text ending in
sentence-final punctuation, with SENT_END = "。！？…" -- all fullwidth. But
tesseract reads the printed ！ and ？ as ASCII "!" and "?" often enough that
the gate refused real breaks: six across the book, each welding two source
paragraphs into one. The typesetter's own indent said "new paragraph" and was
overruled by a punctuation list that did not contain the mark on the page.

Found while translating ch03 p133, where "...真是不知道怎么办才好!" ran
straight into the start of the counter-espionage section. The indent flag for
that line was True; the break was suppressed anyway.

Fixed by admitting the ASCII forms (they are the same marks) and the colon.
The colon is safe here because a break still requires the measured indent as
well, so a false split would need a colon and a typesetter's indent together;
it recovers the ordinary enumerating case, "...分述于下:" followed by an
indented list entry.

Consequence: ch02 source 116 -> 119, ch03 source 190 -> 193. ch02's finished
English re-laid onto the corrected boundaries with reflow.py and passes parity
and alignment at 119/119. ch03's in-progress English split by hand at the two
points that fall inside the translated range, verified by matching content
markers independently in the Chinese and the English.

## THE DISPLACEMENT CLASS, AND THE GATE THAT NOW CATCHES IT - RESOLVED

Found while clearing ch02's inherited numeric debt. The 46 flags had already
fallen to 8 once ch03's noise classes and the "a hundred thousand" parser fix
were in. Four of those were numerals inside names or a weekday. The other four
were real quantities absent from the paragraph paired with them - and they
proved not to be missing but ONE PARAGRAPH LATE. A proper-name probe confirmed
it across roughly ch02 48-78.

CAUSE. reflow.py assigns the translation's sentences to source paragraphs by
dynamic programming, with length as the cost and NUMERALS as content anchors.
The stretch that drifted is narrative - the assassinations, the Lu Haifang
episode - and carries almost no numbers. With no anchors the DP had only
length, and length decides how MUCH English a paragraph gets, never WHICH.

FIX, in three parts.
1. reflow.py now also anchors on GLOSSARY PROPER NAMES. The glossary is
   already a hanzi-to-English key maintained one-rendering-per-referent, so it
   is exactly the cross-lingual fixed point needed. Generic renderings are
   excluded: 特务 -> "secret agent / operative" never appears literally and
   would report a phantom miss on nearly every paragraph.
2. The name penalty is charged BOTH WAYS. A one-sided penalty asks only
   whether a paragraph got the names its source has; it is free to be given
   names its source does not have, which is what a boundary one sentence out
   looks like from the other side. Adding the stray-name charge fixed the last
   residual slips, which sat between adjacent paragraphs naming the same man.
3. `scripts/check_content.py`, a new gate. For every source paragraph it
   requires the paired translation to contain the glossary names the source
   carries. One-directional on purpose: English may use a pronoun where the
   Chinese repeats a name, so an extra occurrence is not a fault. The author's
   own name is excluded - Shen Zui names himself in the third person in his own
   instructor roster and the only correct English is "me".

WHY THIS GATE HAD TO EXIST. check_align compares English-to-Han character
ratios. It is the right check for text that has gone MISSING and is
structurally blind to text that has been MISPLACED, because a displacement
preserves every ratio. It passed ch03's skipped paragraph, ch03's one-place
offset, and ch02's forty-paragraph drift. Ratio checks find missing text;
content checks find misplaced text; the pipeline needed both and had only one.

STATE. All six units re-laid and hand-nudged where the DP still left a
boundary a sentence out (ch02 110, ch01 41 and the two Dai Li paragraphs).
check_content now reports 710 name occurrences across the six units, every one
in its paired paragraph. Parity 18/16/93/119/193/20 all OK, 152 note anchors
all resolve, alignment OK on every unit, register within tolerance.

Also cascaded: 延安 was rendered "Yan'an" in ch01 and "Yenan" in ch03. The
project's decided style is period English (Chungking, Peiping, Szechwan,
Kweichow, Whampoa), so Yenan wins; glossary updated to "decided", prose
cascaded, and the two ch01 note anchors that carried the old form updated with
it. That the note anchors needed updating too is the cascade discipline
CLAUDE.md warns about, and check_structure caught the omission immediately.

## CH02'S SECTION HEADINGS WERE IN THE WRONG PLACES

Found while starting ch02's notes: three headings stacked at the top of the
chapter with no text between them, and every section of the reading text
sitting under the wrong name.

CAUSE. This book sets a long chapter title over two printed lines, and the
assembler records each line as its own heading -- ch02's source opens with
抗战前军统特务在上海的 / 罪恶活动. reflow.py re-inserted headings by walking
the source blocks and consuming one English heading per source heading, so
the title's continuation line ate a section heading's slot and everything
after shifted one place earlier.

Nothing in the prose showed it. The prose was correct; only the headings had
moved. Parity, alignment and the anchor check all passed throughout.

FIX. The title's length cannot be found by looking for a run of consecutive
headings, because ch02's first SECTION heading follows the title with no
paragraph between it -- a run-based rule swallows it, and the guard I added
caught exactly that on the first attempt. It is counted instead: the English
carries one title plus one heading per section, so the leftover source
heading blocks are the title's lines. reflow now also refuses to write if the
two counts cannot be reconciled.

VERIFIED NUMERICALLY rather than by eye. Source and English heading positions,
expressed as the number of body paragraphs preceding each, now agree exactly:
ch02 [47, 50, 57, 64, 80, 93, 100, 104], ch01 [1, 11, 36, 69, 84]. My first
reading of the repaired text was that the sections still looked wrong; the
numbers say otherwise, and the numbers are right -- Chinese section boundaries
do not always open on a topic sentence the way an English reader expects.

WORKFLOW TRAP. Re-running reflow discards hand-nudged boundaries. The four
nudges at ch01 41/50/58 and ch02 110 had to be re-applied after this re-lay.
If reflow is run again on a finished unit, check_content must be re-run and
the nudges restored.

## Wake-up routines

Four routines fire into this session on the hour, offset to give a roughly
15-minute cadence (the server enforces a one-hour minimum per routine, so the
cadence is built from four of them rather than one quarter-hourly schedule):

  trig_013MTXGfGeLaHnWYNch9WSyF  resume (:04, server-anchored)
  trig_019kYNxyeLBKiH997uEguYAJ  resume (:10)
  trig_0143bPgBXSMYZyqtCdnNjF1v  resume (:20)
  trig_017UGgcXSTJKbAmLaWY8usfA  resume (:30)
  trig_015NZK9u2DoznUUWut8Z5mjW  resume (:40)
  trig_017aetyoMaUkaKbdg6BZZErE  resume (:50)

ALL SIX must be deleted once every unit is done and qa_epub passes. The old
four routines no longer appear in list_triggers and are presumed gone; these
six replaced them 2026-07-26 at Winston's request (every ten minutes). They
store no MCP connectors, so the sessions they wake cannot delete them: that
has to happen from a session holding the tool, or from the routines UI.

## Pending decisions

- **Chapter 1 contains an appendix printing the full lyrics of the training
  class song** (附录:班歌歌词全文, printed p.40). Intention is to characterise
  and summarise it — what it says, what register it is in, what it tells you
  about the institution — rather than set out a complete lyric translation.
  Say if you want it rendered in full instead.
- Note numbering runs continuously across the book (decided; implemented in
  neither builder nor QA yet — the builder is the next engineering task).

## Next steps, in order

1. Generalise `build_reading_epub.py` and `qa_epub.py` from the previous
   project's chapter-1 shape to this book's 25 units, with the anchor gate that
   refuses to build on an unmatched anchor.
2. fm02_qianyan (前言), PDF 10–15 — source already assembled.
3. Chapters 1–21 in order, per the pipeline in CLAUDE.md.
4. Batched scholarship pass, covering several chapters at a time.
5. Final sweep per the skill: re-run every script, register across the whole
   spine, historical pattern analysis, random-sample deep audit.
