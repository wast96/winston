# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-16 (ch01-ch16) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 17 (ch17). 8
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two
afterwords together).

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch
was `Chang'an B16`; the next is `Chang'an B17`). CLAUDE.md records the rule; the
kickoff block below opens with that name as its first line on purpose. Keep it
there.

## Message to paste into the next chat

```
Chang'an B17
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-16 (ch01-ch16) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 17 = ch17 (第十七章 丑正 / "Chapter Seventeen. The Hour of the Ox, Second
Half (2 a.m.)") end to end. It is ~13,753 source chars. NOTE: data/src/ and
data/figs/ are gitignored and rebuild from source.epub; if data/src/ is absent in
a fresh clone, run `python3 scripts/ingest_epub.py source.epub` first. Read the
batch's source from its text_file in book.json (data/src/37_text00035.txt); the
source is authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch17_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct, and translate a recurring vignette identically in both places;
the source's content-file time-marker heading line is absorbed into the H2 title,
as in ch01-ch16; render the source's per-chapter time-gloss final line as the
source's own italic note, prefixed '*[The source appends a note on the hour to
each chapter:]*'). Watch for the source's scene-break rules (Image00005.jpg): the
house style renders each scene shift as a plain paragraph break, no separator
glyph. Watch too for extractor-split paragraphs (a logical paragraph broken across
two data/src lines, the first ending on a comma or mid-phrase); merge such halves
into one bilingual pair (ch07-ch16 each merged the opening vignette's and the
dateline's split halves; a quick scan: flag any source line whose last char is not
in 。！？"）…— nor a colon). Then generate out/ch17_reading.md and the parity source
with `scripts/split_bilingual.py out/ch17_bilingual.md ch17 "第十七章　丑正"` (use the
exact full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch17_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail — if it is a real quantity, fix the ENGLISH
to carry the value rather than noising it; watch ORDERING, a new strip pattern must
precede any shorter built-in that would eat part of it first) and
`scripts/check_structure.py --pairs data/zh/ch17.txt out/ch17_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch17" (verbatim English anchors; XHTML bodies with numeric character
references for punctuation/accents, literal CJK for Chinese terms is fine and
builds — ch01/ch09-ch16 do it — never HTML named entities; ~3 per chapter,
recurring subjects get their note at first appearance across the whole book, so
skip anything already noted in ch01-ch16). Add any figure specs to figures.json
only if the chapter has a real content illustration in data/figs/ (the source's
footnote-marker glyph Image00004.jpg and the decorative scene-break rule
Image00005.jpg are NOT figures). Rebuild with
`scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"` so the
pending-aware TOC links ch01-ch17 content and every other chapter's skeleton, then
run `scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"` until green. Do a
blind double-translation of a literary sample and a round-trip back-translation of
a number-dense sample (separate contexts), and record the checks and the sample
error rate in PROGRESS.md. Rewrite HANDOFF.md with the Batch 18 (= ch18) kickoff
message (its fenced block opening with the line `Chang'an B18`), commit, and push
to branch claude/the-longest-day-in-changan. Cite chapters/sections, never page
numbers. Never invent bridging text; footnote genuine ambiguity rather than
smoothing it. Do not pause for approval mid-batch. Deliver the rebuilt EPUB in
chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 ingest + survey + skeleton EPUB, approved. 25-batch plan approved.
- Batch 1 = ch01, complete and committed: 12 notes, glossary seeded, qa PASS.
- Batch 2 = ch02, complete: 3 notes (15 total), EPUB metadata set for Kindle/Apple
  Books, qa PASS.
- Batch 3 = ch03, complete: 4 notes (19 total), noise.txt extended, qa PASS.
- Batch 4 = ch04, complete: 3 notes (22 total), noise.txt extended, qa PASS.
- Batch 5 = ch05, complete: 3 notes (25 total), noise.txt extended, qa PASS.
- Batch 6 = ch06, complete: 3 notes (28 total), noise.txt extended, qa PASS.
- Batch 7 = ch07, complete: 3 notes (31 total), noise.txt extended, qa PASS.
- Batch 8 = ch08, complete: 3 notes (34 total), glossary grown, noise.txt
  extended, qa PASS.
- Batch 9 = ch09, complete: 3 notes (37 total), glossary grown, noise.txt
  extended, qa PASS.
- Batch 10 = ch10, complete: 3 notes (40 total), glossary grown by 46 rows,
  noise.txt extended, qa PASS.
- Batch 11 = ch11, complete: 3 notes (43 total), glossary grown by 20 rows,
  noise.txt extended, qa PASS.
- Batch 12 = ch12, complete: 3 notes (46 total), glossary grown by ~15 rows,
  noise.txt extended, qa PASS.
- Batch 13 = ch13, complete: 3 notes (49 total), glossary grown by 23 rows,
  noise.txt extended, qa PASS.
- Batch 14 = ch14, complete: 3 notes (52 total), glossary grown by 26 rows,
  noise.txt extended, qa PASS.
- Batch 15 = ch15, complete: 3 notes (55 total), glossary grown by 26 rows,
  noise.txt extended, qa PASS.
- Batch 16 = ch16, complete and committed: out/ch16_reading.md, data/zh/ch16.txt,
  3 notes (58 total: "Chen Xuanli, Grand General of the Longwu Army" = the palace
  general of the Mawei mutiny to come; "An Lushan, Commissioner An" = the future
  arch-rebel at his first in-text appearance, praised as "a good man, a man of
  honor"; "Duke Li of Wei and Jieli Khagan" = the Wuwei lantern-chamber tableau, Li
  Jing's 630 capture of Illig Qaghan in the Yin Mountains). glossary.json grown by
  19 rows: people 陈玄礼/Chen Xuanli, 安禄山/An Lushan, 颉利可汗/Jieli Khagan; places
  越州/Yuezhou, 营州/Yingzhou, 河北/Hebei, 林邑/Linyi, 青云观/the Qingyun Abbey,
  武威/Wuwei; orgs 左骁卫/the Left Xiao Guard, 千牛卫/the Qianniu Guard, 万骑/the
  Wanqi; terms 转机/the turning-gear, 水力宫/the Hydraulic Hall, 团结兵/tuanjie
  militia, 柱国/Pillar of State, 越骑/yueqi horseman, 丁防/frontier levy, 顶阁/the
  crown-loft. noise.txt extended (千牛 the Qianniu Guard; 万骑 the Wanqi — both unit
  names, not 1000/10000; 五成 the "fifty-fifty" probability idiom, cf. 十成/八成;
  千恩万谢 "thank a thousand times over," 万 non-quantitative — all non-quantities).
  ONE real quantity was fixed in ENGLISH not noised: 阴阳两界 → "between the two
  worlds of light and shade" so the 两 survives. qa PASS (58 notes). Verbatim-quote
  check: the concatenation of every source blockquote equals the source content
  character-for-character (16,287 chars); parity 289/289; blind double-translation
  (the lantern-tower-descent atmosphere passage, src line 167) and back-translation
  (the tower-waking machinery, src line 291) both clean, 0 errors. ch16's
  time-gloss is CORRECT (the Ox hour, 1–3 a.m.).

## What is NEXT

- Batch 17 = ch17 (第十七章 丑正, ~13,753 source chars, data/src/37_text00035.txt).
  Then B18=ch18 ... B24=ch24, B25=ch25+ch26. See book.json's structure/batches.

## House style set by Batches 1-16 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged. Keep the
  book's own coarseness where it is coarse (ch13 rendered Zhang's "我他妈" as
  "I didn't fucking say ..."; ch14 kept 贱婢 as "treacherous slut"; ch15 kept Xiao
  Gui's "你他妈的" as "Can't you fucking give it me first?").
- Openings: NOT every chapter has an epigraph. Each chapter's opening differs
  (flash-forward vignette, scene-setting description, or the dateline direct);
  translate whatever the source has, and translate a recurring vignette
  identically in both places (ch04 Qujiang; ch05 writing-case; ch06 kiln-duel;
  ch07 festival-crowd; ch08 plain-oil-fritters; ch09 ox-cart ambush; ch10
  Bureau-fire; ch11 Long-Bo's-pavilion; ch12 the golden-horsemen vignette; ch13
  Long-Bo-climbing-from-the-cellar; ch14 Taizhen-catching-Tanqi's-hands; ch15 the
  reversed-crossbow standoff; ch16 Li-Bi-crouched-in-the-water-channel each recur
  later and were translated identically). The content-file time-marker heading line
  (子正 etc.) is absorbed into the H2 chapter title, not made a paragraph. The
  source's per-chapter time-gloss (its own footnote on the dateline) is rendered as
  the SOURCE's own note, in italics, prefixed "*[The source appends a note on the
  hour to each chapter:]*", distinct from translator's notes. Its ordinary words
  are translated; only technical hour-names are romanized (e.g. ch16 "Chou, the
  hour of the Ox, also called the Crowing Cock").
- Scene breaks: the source divides multi-scene chapters with a decorative rule
  image (Image00005.jpg, alt="line"). House style renders each scene shift as a
  plain paragraph break with NO separator glyph (the rule image is not a figure),
  matching ch01-ch16. If visible scene breaks are ever wanted, that is a global
  change across all chapters at once, not a per-batch call.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. The cast/terms decided across
  ch01-ch16 that MUST be reused verbatim include: Zhang Xiaojing (张大头 = Zhang
  Big-Head), Li Bi (Changyuan) / Deputy Director Li, Director He / He Zhizhang (+
  sons He Dong, He Zeng), Yao Runeng, Cui Qi (Commander Cui), Cao Poyan, Xu Bin
  (Youde) / Recorder Xu, Tanqi, Wen Ran, Wen Wuji, Li Heng (heir apparent), Li
  Linfu (the Right Minister), Long Bo (= 萧规 Xiao Gui, his true name, revealed
  ch15), Old Ge, the Great Sabao, Tong'er, Wang Yunxiu, Ma Ge'er, Xiao Yi, Wang
  Zhongsi (military commissioner), Feng Dalun, Prince Yong / Li Lin, Yuan Zai (zi
  Gongfu), Jia Shiqi, Gan Shoucheng / General Gan, Adjutant Zhao / Zhao Qilang, Cen
  Shen (of Xianzhou), the Right Shad, Ozmish Khagan, Ashina, Yisi (deacon), Alopen,
  Mishihe, Registrar Pang, Puzhe, Ji Wen (Deputy Director / Vice-Duan), the
  cruel-official cluster (Lai Junchen, Zhou Xing, Zhou Lizhen, Huan Yanfan, Wu
  Sansi, Hao Xiangxian), Liu Shiqi (刘十七), Mojialuo (摩伽罗), Yuchang (鱼肠, the
  assassin), Peroz (卑路斯), Old Zhao (老赵), Guan Zhong (管仲), Lao Dan / Laozi
  (老聃/老子), Li the Swallow (燕子李), Zhang Luo (张洛, Recorder Zhang), Consort Wei
  (韦氏), Taizhen (太真 = Yang Yuhuan 杨玉环), Chao Fen (晁分), Chao Heng (晁衡 = Abe
  no Nakamaro), Mao Shun (毛顺, Director Mao), Mao Poluo (毛婆罗), Xu Hezi (许合子),
  Prince Shou (寿王) / Li Mao (李瑁), Empress Dowager Dou (窦太后), the Batch-15 cast
  (Xiao Gui 萧规, Gai Jiayun 盖嘉运 / Protector Gai, Zhao Xiao 赵孝, Zhao Li 赵礼,
  Duke Li of Wei 李卫公 = Li Jing, the Sage Confucius 孔圣), and the Batch-16 cast:
  Chen Xuanli (陈玄礼, Grand General of the Longwu Army), An Lushan (安禄山,
  Commissioner An of Pinglu), Jieli Khagan (颉利可汗 = Illig Qaghan). Orgs: the
  Jing'an Bureau, the Lüben Guards, the Jinwu Guard, the Longwu Army, the Right Xiao
  Guard + the Left Xiao Guard (左骁卫) / Leopard Cavalry / Sixteen Guards of the
  Southern Command, the Qianniu Guard (千牛卫), the Wanqi (万骑), the Right Awesome
  Guard, the Court of Judicial Review, the Censorate, the Ministry of
  Justice/Works/War (兵部 = the Ministry of War), the Forestry and Crafts Bureau,
  the Palace Domestic Service, the Jingzhao Prefecture, the Stores Section, the
  Secretariat / the Phoenix Pavilion, the Bureau of Sacrifices, the Shouzhuolang,
  the Eighth Company (第八团), the Assault-Resisting Garrison (折冲府). Places:
  Chang'an, Wannian/Chang'an County, the Vermilion Bird Avenue, the West/East
  Markets, the many wards (incl. Pingkang Ward + the Pingkang Quarter, Guangde,
  Changming, Xuanyang, Yongle, Changxing, Anren, Xingqing/Yongjia/Shengye/Daoye,
  Zhiye, Daozheng), the Xingqing Palace + the Qinzheng Wuben Tower + the Hua'e
  Xianghui Tower + the Taishang Xuanyuan Grand Lantern-Tower, the Taiji and Daming
  Palaces, the Cibei/Daqin/Persian Temples + the Guan Zhong shrine, the Longshou
  Canal + the Arched-Moon Bridge, the ten frontier commands, Balhuan, the
  beacon-fort (烽燧堡/烽燧城), the Protectorate of Anxi (安西都护府), Yanzhou,
  Tianzhu (=India), Kucha, Persia, the Arab lands, Izumo/Japan, the Duanmen Gate
  (Luoyang), the Batch-15 places (Guangwu, Lingwu, Lanzhou, the Yin Mountains,
  Hedong, Jiannan, Shayan, the Southern Mountains 南山), and the Batch-16 places:
  Yuezhou, Yingzhou, Hebei, Linyi (=Champa), the Qingyun Abbey, Pinglu (平卢), the
  Chunming Gate (春名门, an authorial slip for 春明门). Terms: shichen ("double-hour"),
  watchtower / great watchtower, constable (武侯), post-soldier (铺兵), squad leader
  (队正), buliang chief/men, county commandant, Wolf Guards, Türk, Türgesh (突骑施),
  the Sage, His Majesty, Your Highness, the Lantern Festival, the lantern-floats
  (拔灯), the Xi cart (奚车), barrier-knife, modao, pocket crossbow, smoke pellet,
  binding-cord, the art of the Great Archive, the Nine-Gate Drum, rock-oil,
  fierce-fire / fierce-fire thunder, the Que-le Huo-duo, "Zhang the Yama" / the Five
  Yamas (+ the sixth, "the Mad," ch14), the ch08 Nestorian cluster, the ch09-15
  clusters, and the ch16 cluster (the turning-gear 转机, the Hydraulic Hall 水力宫,
  the crown-loft 顶阁, the Wuwei lantern-chamber 武威, tuanjie militia 团结兵, Pillar
  of State 柱国, yueqi horseman 越骑, frontier levy 丁防). The lantern-tower's central
  天枢 pillar reuses "the Tianshu"; 天枢层 = "the Tianshu tier."
- Titles/address: 太子/东宫 = "heir apparent" / "the Eastern Palace"; 太子妃 =
  "Consort Wei"; 司丞 (Li Bi, and Ji Wen) = "Deputy Director" (李司丞 = "Deputy
  Director Li"); 贺监 (He) = "Director He"; 都尉 (Zhang) = "Commander"; 旅帅/崔尉
  (Cui) = "Commander"; 节度 / 节度使 (Wang, An Lushan) = "military commissioner";
  殿下 = "Your Highness"; 陛下 = "His Majesty"; 圣人 = "the Sage"; 郎君 = "young
  master" (李郎君 = "young Master Li"). OFFICE-TITLE renderings: 主事 = "recorder"
  (张主事 = "Recorder Zhang" = Zhang Luo); 录事 = "registrar"; 评事 = "Evaluator";
  参军 = "adjutant"; 将军 (Gan) = "General"; 大将军 (Chen Xuanli) = "Grand General";
  员外郎 (He Dong) = "vice-director"; 执事 = "deacon"; 大主教 = "archbishop"; 长老 =
  "elder"; 副队长 = "deputy squad-leader"; 队正 = "squad leader"; 永王 = "Prince
  Yong"; 寿王 = "Prince Shou"; 节级 = "warder"; 云麾将军 = "General of the Cloud
  Banner"; 右杀 = "the Right Shad"; 尚灯监 = "Director of Lanterns" (毛监 = "Director
  Mao"); 伍长 = "guard-corporal"; 校尉 = "commandant" (military); 都护 = "Protector"
  (盖都护 = "Protector Gai"); 火师 = "fire-master"; 行头 = "foreman (of the
  craftsmen's guild)"; 转运使 = "Transport Commissioner"; the censorial cluster
  殿中侍御史 = "Palace Censor", 侍御史 = "Attendant Censor", 左巡使 = "Commissioner of
  the Left Patrol", 端公 = "Duangong", 副端 = "Vice-Duan"; 京兆尹 = "the Prefect of
  Jingzhao", 中书令 = "the Secretariat Director". 工部/虞部/大理寺/御史台/刑部/内侍省/
  仓曹/中书省/祠部/右威卫/卫尉少卿/尚方丞/兵部/折冲府 per Hucker (see glossary).
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name, an idiom, a round number spelled out analytically,
  an "all-directions" 四X idiom incl. 四下, a swear-word, a myriad-idiom, a
  千古-type "through the ages," an organ idiom like 五脏六腑, a 零="drip" as in 涕零,
  a ranking-name, a list enumerator, a probability idiom like 八成/十成/五成, a
  classifier like 两处/两界, a cn_to_int mis-compound like 千百→1100 or 一两百→200, a
  character-COUNT like 四个字/六个字, a UNIT-NAME numeral like 千牛卫/万骑, an
  idiom like 千恩万谢), extend noise.txt (own-line comments) or WORD_NUM, and say so
  in PROGRESS. ORDERING is load-bearing: a new strip pattern must precede any
  shorter built-in/earlier entry that would eat part of it first. If a flag is a
  REAL quantity, fix the ENGLISH to carry the value instead of noising it (ch06
  一百步/十来个/三面; ch07 张小敬等三人; ch10 近百 → "fully a hundred"; ch11 十来个 →
  "ten-odd"; ch12 两边必须选一边; ch14 数以百计 → "a hundred and more"; ch15 一千多斤
  → "a thousand jin and more", 一两百骑 → "a hundred or two hundred more riders";
  ch16 阴阳两界 → "the two worlds of light and shade"). A genuinely dropped number
  must still fail. The 50/500/5000/50000 escalation of ch16 all carry ("fifty",
  "five hundred", "five thousand", "fifty thousand"). WATCH the checker's English
  parser: it reads cardinals and a FEW ordinals (eighth/fifth/…/seventeenth/
  twentieth) but NOT "eleventh"/"eighteenth" — ch15's Tangyun cipher decode had to
  use cardinals. When a name's numeral must be stripped only in ONE context (ch11
  十七违背 = "Shiqi"), noise the context-specific string. Extra-noise entries run
  BEFORE the built-in NOISE list.
- 二楼/二层 rendered with an English number-word so its numeral survives ("the
  second floor", "two-story"); for approximate "ten-odd" (十余/十几/十来) render
  "ten-odd" (keeps 10), not "a dozen or so" (loses it). 尺 = "chi", 里 = "li", 丈 =
  "zhang", 抱 = "arm-span", 分 = "fen", 弹指 = "finger-snap(s)", 刻 = "mark/quarter".

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. B06-B16 were each started on
  a stray per-batch branch and all work was consolidated onto
  claude/the-longest-day-in-changan, the remote's canonical branch. B16
  specifically: the session opened on claude/changan-b16-ch16-9vuezd, whose HEAD
  equaled origin/claude/the-longest-day-in-changan; the canonical branch was
  checked out and reset to origin, the work done there, the stray local branch
  deleted, remote stray pruned.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships (and is not committed). Note anchors must be
  verbatim English substrings or the build refuses. XHTML note bodies: literal CJK
  is fine, numeric character references for typographic punctuation and accented
  Latin (&#8212; &#8216; &#8217; &#252; &#160; ...), never HTML named entities.
  The builder inserts note anchors BEFORE markup substitution.
- When editing the JSON ledgers, use a Python load/modify/dump (ensure_ascii=False,
  indent=2 for glossary.json AND notes.json) rather than hand-editing braces; then
  json.load to verify.
- Extractor artifacts: a logical paragraph is sometimes split across two (or three)
  lines in data/src (no sentence-ending punctuation on the first). Merge such
  halves into one bilingual pair (ch07-ch16 merged the opening vignette's and the
  dateline's split halves; ch13's and ch15's opening vignettes were THREE lines;
  ch16's opening vignette was THREE lines and its dateline was two). A quick way to
  find them: scan for source lines whose last char is not in 。！？"）…— nor a
  colon. (Multi-paragraph quotations stay separate.)
- Cite by chapter, never by page.
- Dating: the source advances the day at the Rat hour — ch13 (亥正) is 元月十四日,
  ch14 (子初) through ch16 (丑初) are 元月十五日 (Tianbao 3 = 744 CE). ch15 also
  carries a FLASHBACK dateline 开元二十三年 (735 CE) for the beacon-fort last stand.
  Render whatever the source's dateline says.
- The source sometimes uses 中元 ("Ghost Festival") where it means 上元 ("Lantern
  Festival"); translate the intent. (BUT ch06's 盂兰盆节 river-lanterns is a genuine
  Ghost-Festival reference; render it faithfully.)
- Watch for authorial slips (ch03 祆正-for-Sabao and a tutor date; ch04 麻格心 for
  麻格儿; ch05 doubled negative; ch06/ch07 time-gloss 日铺 for 日晡; ch07 五桶 where
  the math needs 十五桶; ch08 time-gloss 17是至19时; ch09 line 271 远怀坊 for 怀远坊;
  ch10 AND ch11 the time-gloss is MISMATCHED; ch13 春名门 for 春明门, which recurs in
  ch16). Render the intent for a mis-named established referent; render genuine
  source errors faithfully and visibly (rule 4) and flag them in PROGRESS. NOTE:
  ch12's, ch13's, ch14's, ch15's AND ch16's time-glosses are CORRECT; do not assume
  every hour-note is broken.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files. Already-noted
  or already-appeared-and-passed subjects to NOT re-note include: He Zhizhang,
  Yuan Zai, Prince Yong, Ozmish Khagan, the Right Shad, Sun Simiao, the Right Xiao
  Guard, the Censorate, Cen Shen, the Pifu, the xiezhi, the Sogdian Whirl, Lai
  Junchen, Ji Wen, the Shouzhuolang, the Self-Raining Pavilion, A Moonlit Night on
  the Spring River, storax, the Guan Zhong shrine, Yuchang, Peroz, Ksitigarbha,
  Taizhen (Yang Yuhuan), the Rainbow-Feather Dance, the tongtian crown, fire-proof
  cloth (asbestos), the mercy-release pond, Chao Heng, the Tianshu, Xu Hezi, the
  Tang Rhymes / Tangyun rhyme-code, Balhuan/the beacon-fort backstory, Gai Jiayun,
  the old charcoal-seller (Bai Juyi's 卖炭翁), 茱萸/the Double Ninth dogwood,
  投名状/the Water Margin blood-pledge, and the ch16 subjects Chen Xuanli, An Lushan,
  Jieli Khagan / Li Jing's Yin-Mountains campaign, and everything in notes.json
  ch01-ch16.
