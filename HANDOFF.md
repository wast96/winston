# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-13 (ch01-ch13) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 14 (ch14). 11
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two
afterwords together).

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch
was `Chang'an B13`; the next is `Chang'an B14`). CLAUDE.md records the rule; the
kickoff block below opens with that name as its first line on purpose. Keep it
there.

## Message to paste into the next chat

```
Chang'an B14
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-13 (ch01-ch13) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 14 = ch14 (第十四章 子初 / "Chapter Fourteen. The Hour of the Rat, First
Half (11 p.m.)") end to end. It is ~17,484 source chars. NOTE: data/src/ and
data/figs/ are gitignored and rebuild from source.epub; if data/src/ is absent in
a fresh clone, run `python3 scripts/ingest_epub.py source.epub` first. Read the
batch's source from its text_file in book.json (data/src/30_text00029.txt); the
source is authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch14_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct, and translate a recurring vignette identically in both places;
the source's content-file time-marker heading line is absorbed into the H2 title,
as in ch01-ch13; render the source's per-chapter time-gloss final line as the
source's own italic note, prefixed '*[The source appends a note on the hour to
each chapter:]*'). Watch for the source's scene-break rules (Image00005.jpg): the
house style renders each scene shift as a plain paragraph break, no separator
glyph. Watch too for extractor-split paragraphs (a logical paragraph broken across
two data/src lines, the first ending on a comma or mid-phrase); merge such halves
into one bilingual pair (ch07-ch13 each merged the opening vignette's and the
dateline's split halves; a quick scan: flag any source line whose last char is not
in 。！？"）…— nor a colon). Then generate out/ch14_reading.md and the parity source
with `scripts/split_bilingual.py out/ch14_bilingual.md ch14 "第十四章　子初"` (use the
exact full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch14_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail — if it is a real quantity, fix the ENGLISH
to carry the value rather than noising it; watch ORDERING, a new strip pattern must
precede any shorter built-in that would eat part of it first) and
`scripts/check_structure.py --pairs data/zh/ch14.txt out/ch14_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch14" (verbatim English anchors; XHTML bodies with numeric character
references for punctuation/accents, literal CJK for Chinese terms is fine and
builds — ch01/ch09/ch10/ch11/ch12/ch13 do it — never HTML named entities; ~3 per
chapter, recurring subjects get their note at first appearance across the whole
book, so skip anything already noted in ch01-ch13). Add any figure specs to
figures.json only if the chapter has a real content illustration in data/figs/
(the source's footnote-marker glyph Image00004.jpg and the decorative scene-break
rule Image00005.jpg are NOT figures). Rebuild with
`scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"` so the
pending-aware TOC links ch01-ch14 content and every other chapter's skeleton, then
run `scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"` until green. Do a
blind double-translation of a literary sample and a round-trip back-translation of
a number-dense sample (separate contexts), and record the checks and the sample
error rate in PROGRESS.md. Rewrite HANDOFF.md with the Batch 15 (= ch15) kickoff
message (its fenced block opening with the line `Chang'an B15`), commit, and push
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
- Batch 13 = ch13, complete and committed: out/ch13_reading.md, data/zh/ch13.txt,
  3 notes (49 total: 地藏菩萨/the bodhisattva Ksitigarbha; 太真/Taizhen = Yang
  Yuhuan; 霓裳羽衣舞/the Rainbow-Feather Dance). glossary.json grown by 23 rows:
  people 张洛/Zhang Luo, 韦氏/Consort Wei, 太真/Taizhen; places 花萼相辉楼/the
  Hua'e Xianghui Tower, 拱月桥/the Arched-Moon Bridge, 兴庆坊/Xingqing Ward,
  永嘉坊/Yongjia Ward, 胜业坊/Shengye Ward, 道业坊/Daoye Ward, 太极宫/the Taiji
  Palace, 南内/the Southern Interior, 春名门/the Chunming Gate; terms 麻搭/fire-mop,
  推事厅/the Deliberation Hall, 架阁库/the records store, 设厅/the reception hall,
  婆罗门戏/a Brahman farce, 地藏菩萨/the bodhisattva Ksitigarbha, 景尊/the Luminous
  Lord, 霓裳羽衣舞/the Rainbow-Feather Dance, 黄狮子舞/the Yellow Lion Dance,
  通天冠/the tongtian crown, 放生池/mercy-release pond. noise.txt extended (两处,
  二不为, 万状, 八成 — all non-quantities; no real number noised). qa PASS (49
  notes). Verbatim-quote check 290/290 clean; blind double-translation (Zhang's
  Ksitigarbha epiphany) and back-translation (the Xingqing lantern-tower, numbers
  intact) both clean, 0 errors.

## What is NEXT

- Batch 14 = ch14 (第十四章 子初, ~17,484 source chars, data/src/30_text00029.txt).
  Then B15=ch15 ... B24=ch24, B25=ch25+ch26. See book.json's structure/batches.

## House style set by Batches 1-13 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged. Keep the
  book's own coarseness where it is coarse (ch13 rendered Zhang's "我他妈" as
  "I didn't fucking say ...").
- Openings: NOT every chapter has an epigraph. Each chapter's opening differs
  (flash-forward vignette, scene-setting description, or the dateline direct);
  translate whatever the source has, and translate a recurring vignette
  identically in both places (ch04 Qujiang; ch05 writing-case; ch06 kiln-duel;
  ch07 festival-crowd; ch08 plain-oil-fritters; ch09 ox-cart ambush; ch10
  Bureau-fire; ch11 Long-Bo's-pavilion; ch12 the golden-horsemen/four-windowed-
  carriage vignette; ch13 Long-Bo-climbing-from-the-cellar vignette each recur
  later and were translated identically). The content-file time-marker heading
  line (子初 etc.) is absorbed into the H2 chapter title, not made a paragraph.
  The source's per-chapter time-gloss (its own footnote on the dateline) is
  rendered as the SOURCE's own note, in italics, prefixed "*[The source appends a
  note on the hour to each chapter:]*", distinct from translator's notes. Its
  ordinary words are translated; only technical hour-names are romanized.
- Scene breaks: the source divides multi-scene chapters with a decorative rule
  image (Image00005.jpg, alt="line"). House style renders each scene shift as a
  plain paragraph break with NO separator glyph (the rule image is not a figure),
  matching ch01-ch13. If visible scene breaks are ever wanted, that is a global
  change across all chapters at once, not a per-batch call.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. The cast/terms decided across
  ch01-ch13 that MUST be reused verbatim include: Zhang Xiaojing, Li Bi
  (Changyuan) / Deputy Director Li, Director He / He Zhizhang (+ sons He Dong, He
  Zeng), Yao Runeng, Cui Qi (Commander Cui), Cao Poyan, Xu Bin (Youde) / Recorder
  Xu, Tanqi, Wen Ran, Wen Wuji, Li Heng (heir apparent), Li Linfu (the Right
  Minister), Long Bo, Old Ge, the Great Sabao, Tong'er, Wang Yunxiu, Ma Ge'er,
  Xiao Yi, Wang Zhongsi (military commissioner), Feng Dalun, Prince Yong / Li Lin,
  Yuan Zai (zi Gongfu), Jia Shiqi, Gan Shoucheng / General Gan, Adjutant Zhao /
  Zhao Qilang, Cen Shen (of Xianzhou), the Right Shad, Ozmish Khagan, Ashina, Yisi
  (deacon), Alopen, Mishihe, Registrar Pang, Puzhe, Ji Wen (Deputy Director /
  Vice-Duan), the cruel-official cluster (Lai Junchen, Zhou Xing, Zhou Lizhen,
  Huan Yanfan, Wu Sansi, Hao Xiangxian), Liu Shiqi (刘十七), Mojialuo (摩伽罗),
  Yuchang (鱼肠, the assassin), Peroz (卑路斯), Old Zhao (老赵), Guan Zhong (管仲),
  Lao Dan (老聃), Li the Swallow (燕子李), and the Batch-13 cast: Zhang Luo (张洛,
  the lantern-recorder), Consort Wei (韦氏, the heir's wife), Taizhen (太真 = Yang
  Yuhuan). Orgs: the Jing'an Bureau, the Lüben Guards, the Jinwu Guard, the Right
  Xiao Guard / Leopard Cavalry / Sixteen Guards of the Southern Command, the Right
  Awesome Guard (右威卫), the Court of Judicial Review, the Censorate, the Ministry
  of Justice/Works, the Forestry and Crafts Bureau, the Palace Domestic Service,
  the Jingzhao Prefecture, the Stores Section, the Secretariat / the Phoenix
  Pavilion, the Bureau of Sacrifices, and the Shouzhuolang. Places: Chang'an,
  Wannian/Chang'an County, the Vermilion Bird Avenue, the West/East Markets, the
  many wards (incl. Pingkang Ward + the Pingkang Quarter 平康里, Guangde, Changming,
  Xuanyang, Yongle, Changxing, Anren, and the Batch-13 Xingqing/Yongjia/Shengye/
  Daoye wards), the Xingqing Palace + the Qinzheng Wuben Tower + the Hua'e Xianghui
  Tower, the Taiji and Daming Palaces (the Southern Interior = Xingqing), the
  Cibei/Daqin/Persian Temples + the Guan Zhong shrine, the Longshou Canal + the
  Arched-Moon Bridge, the ten frontier commands, Balhuan, Yanzhou, Tianzhu
  (=India), Kucha, Persia (波斯), the Arab lands (大食). Terms: shichen
  ("double-hour"), watchtower / great watchtower, constable (武侯), post-soldier
  (铺兵), squad leader (队正), buliang chief/men, county commandant, Wolf Guards,
  Türk, the Sage, His Majesty, Your Highness, the Lantern Festival, the
  lantern-floats (拔灯), the Xi cart (奚车), barrier-knife, modao, pocket crossbow,
  smoke pellet, binding-cord, the art of the Great Archive, the Nine-Gate Drum,
  rock-oil, fierce-fire / fierce-fire thunder, the Que-le Huo-duo, "Zhang the
  Yama," the ch08 Nestorian cluster, the ch09 cluster (the Pifu, xiezhi, the
  Sogdian Whirl, ...), the ch10 cluster, the ch11 cluster, the ch12 cluster
  (green-vitriol oil 绿矾油, cave-running 跑窟, the four-windowed carriage 四望车, the
  Rosy-Cloud Fling 甩霞舞), and the ch13 cluster (the three-feather order 三羽令,
  fire-mop 麻搭, fire-proof cloth 火浣布 = asbestos, the Deliberation Hall 推事厅,
  the records store 架阁库, the reception hall 设厅, a Brahman farce 婆罗门戏, the
  Luminous Lord 景尊, the Yellow Lion Dance 黄狮子舞, the tongtian crown 通天冠,
  mercy-release pond 放生池).
- Titles/address: 太子/东宫 = "heir apparent" / "the Eastern Palace"; 太子妃 =
  "Consort Wei"; 司丞 (Li Bi, and Ji Wen) = "Deputy Director"; 贺监 (He) =
  "Director He"; 都尉 (Zhang) = "Commander"; 旅帅/崔尉 (Cui) = "Commander"; 节度
  (Wang) = "military commissioner"; 殿下 = "Your Highness"; 陛下 = "His Majesty";
  圣人 = "the Sage". OFFICE-TITLE renderings: 主事 = "recorder"; 录事 = "registrar";
  评事 = "Evaluator"; 参军 = "adjutant"; 将军 (Gan) = "General"; 员外郎 (He Dong) =
  "vice-director"; 执事 = "deacon"; 大主教 = "archbishop"; 长老 = "elder"; 副队长 =
  "deputy squad-leader"; 队正 = "squad leader"; 永王 = "Prince Yong"; 节级 =
  "warder"; 云麾将军 = "General of the Cloud Banner"; 右杀 = "the Right Shad"; the
  censorial cluster 殿中侍御史 = "Palace Censor", 侍御史 = "Attendant Censor", 左巡使
  = "Commissioner of the Left Patrol", 端公 = "Duangong", 副端 = "Vice-Duan"; 京兆尹
  = "the Prefect of Jingzhao", 中书令 = "the Secretariat Director". 工部/虞部/大理寺/
  御史台/刑部/内侍省/仓曹/中书省/祠部/右威卫 per Hucker (see glossary).
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name, an idiom, a round number spelled out analytically,
  an "all-directions" 四X idiom, a swear-word, a myriad-idiom, a ranking-name, a
  list enumerator, a probability idiom like 八成/十成, a classifier like 两处, a
  list enumerator like 二不为, a character-COUNT like 四个字/六个字), extend noise.txt
  (own-line comments) or WORD_NUM, and say so in PROGRESS. ORDERING is load-bearing:
  a new strip pattern must precede any shorter built-in/earlier entry that would eat
  part of it first (ch10 placed 十几万 ABOVE the bare 十几 rule). If a flag is a REAL
  quantity, fix the ENGLISH to carry the value instead of noising it (ch06 一百步/
  十来个/三面; ch07 张小敬等三人; ch10 近百 → "fully a hundred"; ch11 十来个 → "ten-odd";
  ch12 两边必须选一边 → "of the two he had to choose one"). A genuinely dropped number
  must still fail. When a name's numeral must be stripped only in ONE context (ch11
  十七违背 = the name "Shiqi", while 第十七句 = "the seventeenth line" stays a real
  number), noise the context-specific string, not the bare numeral.
- 二楼/二层 rendered with an English number-word so its numeral survives ("the
  second floor", "two-story"); for approximate "ten-odd" (十余/十几/十来) render
  "ten-odd" (keeps 10), not "a dozen or so" (loses it). 尺 = "chi", 里 = "li", 丈 =
  "zhang", 抱 = "arm-span", 分 = "fen".

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. B06-B13 were each started on
  a stray per-batch branch and all work was consolidated onto
  claude/the-longest-day-in-changan, the remote's canonical branch. B13
  specifically: the session opened on claude/changan-b13-ch13-81mvtm; its HEAD
  equaled origin canonical (Batch 12), so the canonical branch was checked out and
  reset to origin, the work was done there, and the stray local branch was
  deleted; the stray remote 81mvtm was deleted too.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships (and is not committed). Note anchors must be
  verbatim English substrings or the build refuses. XHTML note bodies: literal CJK
  is fine (ch01/ch09/ch10/ch11/ch12/ch13), numeric character references for
  typographic punctuation and accented Latin (&#8212; &#8216; &#8217; &#252; &#160;
  ...), never HTML named entities. The builder inserts note anchors BEFORE markup
  substitution.
- When editing the JSON ledgers, use a Python load/modify/dump (ensure_ascii=False,
  indent=2 for glossary.json AND notes.json — matching their on-disk 2-space
  indent) rather than hand-editing braces; then json.load to verify. Always
  `python3 -c "import json; json.load(open('glossary.json'))"` (and notes.json)
  after editing.
- Extractor artifacts: a logical paragraph is sometimes split across two (or
  three) lines in data/src (no sentence-ending punctuation on the first). Merge
  such halves into one bilingual pair (ch07-ch13 merged the opening vignette's and
  the dateline's split halves; ch13's opening vignette was THREE lines, and its
  dateline carried a 。。 double-period artifact collapsed to 。). A quick way to
  find them: scan for source lines whose last char is not in 。！？"）…— nor a colon.
  (Multi-paragraph quotations, where a speech runs across several source lines each
  a complete sentence, stay separate.)
- Cite by chapter, never by page.
- The source sometimes uses 中元 ("Ghost Festival") where it means 上元 ("Lantern
  Festival"); translate the intent. (BUT ch06's 盂兰盆节 river-lanterns is a genuine
  Ghost-Festival reference; render it faithfully.)
- Watch for authorial slips (ch03 祆正-for-Sabao and a tutor date; ch04 麻格心 for
  麻格儿; ch05 doubled negative; ch06/ch07 time-gloss 日铺 for 日晡; ch07 五桶 where
  the math needs 十五桶; ch08 time-gloss 17是至19时; ch09 line 271 远怀坊 for 怀远坊;
  ch10 AND ch11 the time-gloss is MISMATCHED — both label the hour 戌 but gloss it
  with pre-dawn 卯 content; ch13 春名门 for 春明门, same reading). Render the intent
  for a mis-named established referent; render genuine source errors faithfully and
  visibly (rule 4) and flag them in PROGRESS. NOTE: ch12's AND ch13's time-glosses
  are CORRECT (亥 glossed with "21时至23时"); do not assume every hour-note is broken.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files. Already-noted
  or already-appeared-and-passed subjects to NOT re-note include: He Zhizhang,
  Yuan Zai, Prince Yong, Ozmish Khagan, the Right Shad, Sun Simiao, the Right Xiao
  Guard, the Censorate, Cen Shen (of Xianzhou), the Pifu, the xiezhi, the Sogdian
  Whirl, Lai Junchen, Ji Wen, the Shouzhuolang, the Self-Raining Pavilion,
  A Moonlit Night on the Spring River, storax, the Guan Zhong shrine, Yuchang,
  Peroz, Ksitigarbha, Taizhen (Yang Yuhuan), the Rainbow-Feather Dance,
  fire-proof cloth (asbestos, glossary-noted, first ch06), the mercy-release pond
  (ch07), and everything in notes.json ch01-ch13.
