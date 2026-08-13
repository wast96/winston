# HANDOFF — Nameless Heroes (英雄无名), Chen Gongshu

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the message below, not its delivery:
every batch ends with this file's paste-block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite
it at the end of every batch; always keep the paste-ready block below as its
first section. When the book completes, replace it with the completion notice
and do not touch it afterward.

## Message to paste into the next chat

```
Nameless Heroes B11

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14) and B10 (ch15) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B11 = ch16 (ONE unit, ~23,759 source chars): 第六章 奸伪卑劣 寿张为幻 "Chapter 6. Vile Treachery, Illusions Undone" - the sixth chapter of PART TWO ("Disgrace at Hanoi"), the reckoning-and-reflection chapter that FOLLOWS the failed assassination (ch15). Chen owns the failure, then turns to a documentary indictment of Wang Jingwei: the chapter reproduces AT LENGTH two of Wang's own texts - 「曾仲鸣先生行状」 (Wang's eulogy/biographical account of Zeng Zhongming, dated 二十八年四月六日 / 6 April 1939) and 「举一个例」 (Wang's public apologia of 9 April 1939, WITH the record of the 国防最高会议第五十四次常务委员会议 that ch15 said he doctored, including its attendee roster) - and Chen rebuts them point by point. Read the tail of ch15 English (out/ch15_reading.md sections (四)-(五)) and ch14 for register + story continuity: ch15 ended with 举一个例/吴稚晖 and the promise that "the work of sanctioning Wang did not stop at this... more sacrifices to make." Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch16 from data/src (17_index-split-000-0015.txt). drop=2 (running header 英雄无名-陈恭澍 from <title> + the <h2> chapter title; CONFIRM against data/src_epub/OEBPS/Text/index_split_000_0015.xhtml, which parses to 1 <h2> + 121 <p>, zero mismatches vs the extracted text). NO <br/>, NO images, NO set-off formatting (confirm). FOUR numbered-in-parens sub-headings (一)-(四) like ch12/ch13/ch15: (一)我们勇于承担失败的责任 [STANDALONE, its own <p>]; (二)曾仲鸣事汪以忠虽枉死应无怨尤 [GLUED onto the TAIL of a preceding <p>, cf. ch08 - split off as its own ### heading]; (三)强词夺理「举一个例」为乞降作辩解 [STANDALONE]; (四)原是个偷天换日媚辞取容的大奸佞 [STANDALONE]. Grep each candidate p-by-p against data/src_epub to confirm which are glued vs standalone. TWO long quoted Wang documents kept WHOLE as deliberate multi-<p> blocks: 「曾仲鸣先生行状」 (title line + body, ending "...所继述云尔。(二十八年四月六日)") and 「举一个例」 (title line + body), the latter enclosing the 国防最高会议 meeting record with a broken-across-lines ATTENDEE ROSTER (出席：于右任 居正 孔祥熙... / 翁文灏 邵力子 陈立夫 董显光... / 主席：汪... 秘书长：张群 秘书主任：曾仲鸣) - these roster lines are DELIBERATE document formatting, NOT extractor splits; keep them as separate <p> and do NOT merge (cf. ch12/ch13 quoted documents). An in-text "(第六章完)" coda near the end (cf. ch12/ch13). EXTRACTOR mid-phrase splits to MERGE: re-derive each against the XHTML (candidates include a "...何时" continuation and a "...何况现时" continuation - re-confirm the exact body-line pairs). GREP the source for note markers (\[\d+\]) and record "none present" in PROGRESS.md (none through B10).
2. Extend scripts/clean_batch.py with ch16's spec (drop=2; merges = the mid-phrase pairs, re-derived as body-line pairs; glued { (二) heading }; standalone = the (一),(三),(四) sub-heading lines). Run it (source-conservation check). Write out/ch16_reading.md (## chapter title from book.json = "Chapter 6. Vile Treachery, Illusions Undone"; ### for each (一)-(四) sub-heading; one English paragraph per source body line; the two quoted Wang documents and the meeting record as normal paragraphs - do NOT use {p} verse). Then run scripts/batch_artifacts.py ch16 (and, to keep checks.json complete, scripts/batch_artifacts.py with no args). NOTE the batch_artifacts.py workflow trap: running it with an ID writes checks.json with ONLY that unit; ALWAYS finish with a no-arg run so check_structure/check_content see all 16 units.
3. Translate to the FROZEN register (Chen's voice sheet + character voice sheets in HANDOFF). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled renderings (the Juntong; Dai Li / 老板 / 戴先生 "Mr. Dai" / 戴雨农 "Dai Yunong"; 汪精卫 Wang Jingwei / 汪逆 "the traitor Wang" / 汪某 "the man Wang"; 陈璧君 Chen Bijun; 制裁 "sanction" / 制裁令 "sanction order"; 曾仲鸣 Zeng Zhongming; 方君璧 Fang Junbi; 徐先生 Mr. Xu; 王鲁翘 Wang Luqiao; 余乐醒 Yu Lexing/Dr. Yu; 岑家焯 Cen Jiazhuo; 方炳西 Fang Bingxi; 唐英杰 Tang Yingjie; 余鉴声 Yu Jiansheng; 陈邦国 Chen Bangguo [see the name-trap note]; 张逢义 Zhang Fengyi; 陈步云 Chen Buyun; 魏春风 Wei Chunfeng; 高朗街 Gao Lang Street / Rue Colombert No. 27; 吴敬恒 Wu Jingheng [Zhihui]; 朱执信 Zhu Zhixin; the B06-B10 shelves). Part Two PRINCIPALS: Chen(1), Dai Li(2), Wang Jingwei(3), Zheng Jiemin(4), Wang Tianmu(5), Fan Xing(6), Fang Bingxi(7), Wang Luqiao(8). Render Republican years literally per the Part-Two convention ("the twenty-eighth year"; the checker matches the source numeral and the Gregorian if carried). NEW cast likely to add: the National Defense Council meeting attendees in the quoted record (于右任 Yu Youren, 居正 Ju Zheng, 孔祥熙 Kong Xiangxi, 翁文灏 Weng Wenhao, 邵力子 Shao Lizi, 陈立夫 Chen Lifu, 董显光 Dong Xianguang, 张群 Zhang Qun, and any others in the roster - MANY are famous, check authority.json/glossary for existing rows first; give pinyin fields). The two documents 「曾仲鸣先生行状」 and 「举一个例」 were both FOOTNOTED in ch15 (B10) at first mention - do NOT re-note them; here they are quoted in full, so add notes only for NEW references inside them.
   ⚠ Reuse the B10 resolution: 陈邦国 "Chen Bangguo" (the source spelled it 陈 in ch15 + the Dai biography, 郑 in ch13; glossary key is now 陈邦国, ch13 was updated to match, discrepancy footnoted in ch15). WATCH ch16's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): expect the same single-character-substitution classes as ch15 (先↔光, 卫→术, 鸣→呜, 汪→江, 文↔交, 声→聋, 其→共, 间→问, 便→遍, 是→走/遍, 这→违, 随→隧, 春→舂) plus the TITLE glyph 寿张为幻 (flagged as a stray/uncertain glyph - 寿张 may be a corruption; render the title from book.json's "Illusions Undone" and footnote the source uncertainty if the body clarifies it). NUMBER-DENSE quoted documents (the 行状 and the meeting record with its dates 二十八年四月六日, 四月九日, and the 第五十四次 session number, plus any attendee counts/vote tallies): carry real counts as DIGITS/explicit words; NOISE only elided-tens/approximate forms - add a commented B11 block to data/noise.txt as needed (the B10 block already covers 四、五百 / 四、五十 / 八、九百 / 五、六响 etc.; the B09+B10 elided-tens block is ordered longest-first - keep any new compound BEFORE the bare form it contains).
4. Checks (per unit): verify_unit.py ch16 (parity + numbers with --noise auto-found + anchors); check_align.py ch16; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch07 Zhanggu, ch08 Shunde, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen - these are diacritic/variant substring-match artifacts, NOT regressions; CONFIRM ch16 itself shows "all in the paired paragraph" / 0 displaced, and do NOT add book-TITLE glossary rows keyed on full hanzi, which cross-flag ch10/ch13/ch15); qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch16_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field); verify the TAIL against the source (the "(第六章完)" coda region 汪的工作则迄未放松。 and Chen's closing rebuttal). check_register.py --ref reference/B01_frozen.md out/ch16_reading.md ("shall" in Chen's narration is deliberate; the two long quoted Wang documents may push the ratio up like ch12/ch13/ch15 - read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md). This chapter earns NEW notes for its first-appearance material: the famous National Defense Council attendees a Western reader won't know (Yu Youren, Kong Xiangxi, etc. - be selective, note the 2-3 most load-bearing, not every name); the 行状 genre was NOTED in ch15 - do NOT re-note it, but Zeng's eulogy content may earn a fresh note; 举一个例 was NOTED in ch15 - do NOT re-note the piece itself, but the doctoring claim about the meeting record may earn one; any idioms that carry weight (be generous but do NOT pad; consult the NOT-re-noted list first). Merge notes via apparatus_merge.py (numeric character references only in note bodies - keep them ASCII where possible; anchors verbatim substrings of the reading.md, in body text not headings; keep anchors ASCII with NO em dash and NO quote character - the reading.md uses straight quotes and em dashes, so an anchor containing either is a substring trap; multi-occurrence anchors attach at first occurrence, which is the correct first-appearance placement). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes). Confirm ch16 carries no images.
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B12 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) +
  skeleton EPUB. See the survey section of PROGRESS.md.
- **Batch B01 (ch01-ch05), the front matter.** 67 notes. **VOICE GATE PASSED:**
  the B01 front matter is the FROZEN register reference (`reference/B01_frozen.md`)
  for `check_register.py --ref` from B02 on.
- **Batch B02 (ch06), Part One Section 1.** 322 paragraphs; 24 notes; 17 glossary rows.
  The once-per-book blind double-translation and back-translation samples were done here.
- **Batch B03 (ch07), Part One Section 2.** 362 paragraphs; the Zhang Jingyao case.
- **Batch B04 (ch08), Part One Section 3.** 461 paragraphs; the Ji Hongchang case,
  the Wang Zixiang poison death, the 9 Nov 1934 Guomin Hotel shooting.
- **Batch B05 (ch09), Part One Section 4.** 332 paragraphs; the Shi Yousan case.
  **Part One COMPLETE.**
- **Batch B06 (ch10 + ch11), Part Two opens.** ch10 = the Part Two Author's Preface;
  ch11 = "Bloodshed Against the Enemy". **Part Two title RESOLVED: "Disgrace at Hanoi."**
- **Batch B07 (ch12), Part Two Chapter 2.** "Unfathomable Hearts, Hidden Designs".
- **Batch B08 (ch13), Part Two Chapter 3.** "Treacherous Tides, a Gathering Storm"
  (262 body paragraphs, largest of Part Two). First use of `{p}` verse.
- **Batch B09 (ch14), Part Two Chapter 4.** "Beset on Three Sides, Ever Forward" - a
  very short (520-char) bridge chapter; 0 new notes.
- **Batch B10 (ch15), Part Two Chapter 5.** 第五章 博浪一击 误中副车 "A Blow at Bolang,
  the Wrong Carriage Struck" - the CLIMAX: the failed poison-bread "soft action" and
  gas device, the sanction order (19 March 1939), the botched Red River bridge chase,
  the night raid killing Zeng Zhongming by mistake, and the documentary section (五)
  quoting/correcting three real books. 225 body paragraphs; 11 new notes (185
  cumulative); ~13 glossary rows. **Name trap RESOLVED: 郑邦国 -> 陈邦国 "Chen Bangguo"**
  (glossary key renamed, ch13 built unit updated to match, discrepancy footnoted in
  ch15). All checks green; qa_epub PASS; epubcheck 0/0/0/0. EPUB now **15/43 chapters**.
  Detail in PROGRESS.md ("Batch B10").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch15. Merge logic FOLLOWS CHAINS (a `<p>` split into 3+ fragments is
  rejoined whole). **drop is variable:** most chapters drop=2; ch01 and ch10 drop=3.
- `scripts/batch_artifacts.py` - derives out/<id>_en.json FROM out/<id>_reading.md
  and writes checks.json. Author the reading.md; run this. **TRAP: running it with an
  ID writes checks.json with ONLY that unit; ALWAYS finish with a no-arg run** so
  check_structure/check_content see every unit. `body_lines` strips `#`-headings,
  `***`, and the `{vdgp}` set-off prefix.
- `scripts/verify_unit.py <id>` - parity + numbers (auto-finds data/noise.txt; do NOT
  pass --noise, it is treated as a cid) + anchors. Run per unit.
- `scripts/build_reading_epub.py` - builds out/nameless-heroes.epub from book.json +
  the reading.md/en.json + notes.json + glossary.json + figures.json.
- `scripts/check_content.py` (patched) - name_map skips "_"-prefixed glossary
  categories/entries. It flags KNOWN PRE-EXISTING artifacts and exits NONZERO because
  of them: ch07 Zhanggu, ch08 Shunde, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen
  (diacritic/variant forms the substring matcher cannot align). These are NOT
  regressions; the pass criterion for a NEW batch is "the batch's own unit shows all
  name occurrences in the paired paragraph / 0 displaced." Do NOT add book-TITLE
  glossary rows keyed on the full hanzi title: a title entry cross-flags every other
  chapter that renders the same title slightly differently (this bit B10 - the three
  quoted books are handled by FOOTNOTES, not glossary rows).
- **Verse marker `{p}`** (first used in ch13): prefix a pure-verse body line with
  `{p} ` and the builder renders `<p class="verse">`; the checks strip it. ch15 used
  none.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** - `qc_entities.py` does `rec["pinyin"]` and KeyErrors
  otherwise. apparatus_merge's glossary path assumes a FLAT map and would corrupt the
  sectioned file; NOTES still go through apparatus_merge.py.
- **Note-anchor gotchas:** (B06) American-style punctuation puts the period INSIDE the
  closing quote, so an anchor ending on a quoted phrase fails - anchor on an interior
  phrase. (B08) the reading.md uses STRAIGHT quotes/apostrophes; a curly-quote anchor
  will not match - keep anchors ASCII, WITHOUT any quote character AND without an em
  dash (the reading.md uses U+2014 em dashes freely; an anchor containing one is a
  substring trap). Multi-occurrence anchors attach at the FIRST occurrence (correct
  first-appearance placement); check_structure reports "attach at first of several".
- data/noise.txt carries the B01-B10 project noise rules (each with a comment line).
  Republican years are rendered literally in Part Two ("the twenty-eighth year"); the
  checker matches the source numeral directly. **The elided-tens block (B09+B10) is
  ordered LONGEST-FIRST:** a compound like 四、五百 MUST precede the bare 四、五, or the
  short rule fires first and orphans the leftover 百/十 (100/10). Fullwidth-zero
  years/refs (一九○五 / 二○三, ○ = U+25CB) must be noised - the checker cannot compose
  them - and the value carried in the English. Greedy-match traps get their own noise
  line (五百一张 read as 501).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run
  per session). setup.sh's ONE failing regression test ("hook stands down on template
  stub") is a KNOWN false alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss";
  戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (原名 汪兆铭 "Wang Zhaoming";
  汪逆 "the traitor Wang"; 汪某 "the man Wang"); 陈璧君 Chen Bijun. 制裁 "sanction"; 制裁令
  "sanction order". Chiang's titles: 校长 "the Commandant", 领袖 "the Leader", 委员长 "the
  Generalissimo", 总裁 "the Director-General" (Wang = 副总裁 "Vice-Director-General").
  总理 = "the Party Leader" / 国父 = "the Father of the Nation" = Sun Yat-sen. Floors:
  二楼/三楼 = "second/third floor". Republican years literal in Part Two. 督察 "inspector"
  (rendered "inspectorate" for Fang Bingxi's oversight role in ch15). 为虎作伥 "playing
  the tiger's cat's-paw".
- **B03-B08 shelves (reuse; in glossary.json):** the Juntong internal units,
  Tianjin/Beiping/Hong Kong/Hanoi geography, the Mauser "box-cannon", the Green Gang,
  the Kwantung Army, Manchukuo, the "Yan Telegram", the Three Principles of Peace,
  Konoe's "New Order in East Asia", 支那 = "Shina", the Kōain, the Tanaka Memorial, the
  Hanoi team as "the Eighteen Arhats"; people: Cen Jiazhuo, Yu Lexing, Zhou Fohai, Chen
  Gongbo, Gao Zongwu, Mei Siping, Kagesa Sadaaki, Konoe, Long Yun, Zeng Zhongming, etc.
- **B08 shelf.** Hanoi operation: 徐先生 "Mr. Xu"; 曾先生 "Mr. Zeng"; 魏春风 Wei Chunfeng;
  阮小姐 Miss Nguyen; 曹师昂 Cao Shi'ang; 谭天堑 Tan Tianqian; 张逢义 Zhang Fengyi; 陈步云
  Chen Buyun; the Continental Hotel; 高朗街 "Gao Lang Street" (Rue Colombert, No. 27);
  海防 Haiphong; 息烽 Xifeng. Wang-essay history names (Zaifeng, the Tongmenghui, the
  Min Bao, Zhang Taiyan, Liang Qichao, Huang Xing, Song Jiaoren, Zhu Zhixin, etc.).
- **B10 shelf (ch15; reuse; in glossary.json).** 陈邦国 Chen Bangguo (the resolved
  spelling - see the name trap below); 唐英杰 Tang Yingjie; 余鉴声 Yu Jiansheng (DISTINCT
  from 余乐醒 Yu Lexing); household/witnesses from the quoted essay: 方君璧 Fang Junbi
  (Zeng's wife), 朱媺 Zhu Mei, 何文杰 He Wenjie, 汪文惺 Wang Wenxing, 陈国琦 Chen Guoqi,
  戴芸生 Dai Yunsheng, 何就 He Jiu, 陈国星 Chen Guoxing, 汪圯 Wang Yi; 平沼骐一郎 Hiranuma
  Kiichirō; 金雄白 Jin Xiongbai / pen name 朱子家 Zhu Zijia; 吴敬恒 Wu Jingheng (courtesy
  稚晖 Zhihui); 红河大桥 the Red River bridge (the Pont Doumer / Long Bien); 打叻 Da Le
  (the biography's 丹道镇 "Dan Dao" / the essay's 三桃山 "San Tao Shan", unreconciled);
  东方汇理银行 the Banque de l'Indochine. Books handled by FOOTNOTE (not glossary):
  蒋总统秘录 "The Secret Records of President Chiang", 戴雨农先生传 "The Biography of Mr.
  Dai Yunong", 汪政权的开场与收场 "The Rise and Fall of the Wang Regime" - all real,
  semi-official/journalistic, corroborating in the main.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 (B08) and 陈邦国 in ch15
(B10, 16x) plus the quoted Biography of Dai Yunong (陈). This is ONE man (one of the
three captured). RESOLVED to **Chen Bangguo (陈邦国)**, the better-attested/semi-official
form: glossary key renamed 郑邦国 -> 陈邦国; the BUILT ch13 unit updated (Zheng Bangguo ->
Chen Bangguo, 4x; re-verified green); the discrepancy footnoted at the first ch15
occurrence. Wikipedia's "陈邦国" is a different modern PRC official; the 十八罗汉 secondary
rosters vary (often 郑), so the romanization stays `provisional`. Use Chen Bangguo
consistently in all remaining batches.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but
  not stilted. Long semicolon-joined clauses; four-character idiom and classical
  allusion used freely and footnoted when they carry weight. Refers to himself as
  笔者 "the writer" and 我 "I". His narrating "shall" is DELIBERATE - do not
  de-formalize it; check_register flags it informationally (B06 33%, B08 29%, B10 9%,
  verified deliberate).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his
  blunders; tender toward dead comrades, bitter and scornful toward the enemy;
  rhetorical questions and exclamations for emphasis. In ch16 (the reckoning after the
  failure) the stance turns from raw remorse (ch15) to a cold documentary indictment:
  he quotes Wang's own 行状 eulogy and 举一个例 apologia AT LENGTH and rebuts them line by
  line. Keep the quoted-Wang register (formal, literary, self-pitying/self-justifying)
  DISTINCT from Chen's own dry, scornful first person.
- Ratio ~4.55-4.76 en/han in narrative; prefaces denser (~5.2); document-/essay-heavy
  chapters run higher (ch12 4.84, ch13 4.79, ch15 4.60 despite two long quotes). ch16's
  two long Wang documents will pull its ratio up.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** Off-stage in ch16 (Chen was recalled to
  Chongqing at the end of ch15). Warm off duty, abrupt on business, grave at Hanoi.
- **WANG LUQIAO (王鲁翘 / Luqiao).** Part Two principal (cast 8). The trigger-man who shot
  Zeng in error; bluff, bold, loyal ("没关系，咱们再干！"). Shares Chen's northern tastes.
- **FANG BINGXI (方炳西 / Brother Bingxi).** Part Two principal (cast 7). The advance man;
  cipher-holder; carried the sanction order in by night; likely a "supervisory
  (inspectorate)" role. Survives the operation.
- **YU LEXING (余乐醒 / Brother Lexing / Brother Yu Lexing / Dr. Yu).** France-trained
  chemist, chief of staff; brooding, thin-skinned ("开不得玩笑…自尊心特别强"). Championed the
  failed poison-bread "soft action" and gas device in ch15. NOTE the rendering split:
  余乐醒 (full name) = "Brother Yu Lexing"; 乐醒兄 (given only) = "Brother Lexing".
- **CEN JIAZHUO (岑家焯 / Brother Jiazhuo).** Chen's Whampoa senior; silent, steady;
  volunteered for the "second-line deployment" in ch15.
- **MR. XU (徐先生).** The unnamed "special personage"; embedded with Hanoi's overseas
  Chinese and the French police; delivered the two shattering dawn phone calls in ch15
  ("你们搞错了…受伤的是曾仲鸣" and "有三个人被逮去了"). Never writes a word down.
- **WEI CHUNFENG (魏春风).** The brilliant young overseas-Chinese guide (four tongues);
  bribed the two Annamese detectives (4,500) to clear the raid; pure of motive.
- **CHEN BANGGUO (陈邦国 - see the name trap).** The big, powerful "open-road vanguard"
  of the raid; impetuous ("我说冲上去就干"); one of the three captured (seven years).
- **YU JIANSHENG (余鉴声).** Wang Luqiao's second in the raid, DISTINCT from Yu Lexing;
  cool-headed (restrained the hot Chen Bangguo); one of the three captured.
- **TANG YINGJIE (唐英杰).** The reconnaissance specialist who scaled the roof and led the
  raiders over the wall; nimble but with "几段不切实的往事" that made Chen watch him.
- **ZHENG JIEMIN / WANG TIANMU / FAN XING.** Part Two principals (4, 5, 6), off-stage in
  B06-B10; render straight when they recur (Wang Tianmu's loyalty is tested later).
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11); and ZENG
  ZHONGMING 曾仲鸣, killed at Hanoi in Wang's place (the 误中副车 of the ch15 title). In
  ch16, Wang Jingwei's own eulogy 「曾仲鸣先生行状」 for Zeng is quoted and rebutted.

## Where the book stands

- Part One (北国锄奸) is COMPLETE (B01-B05).
- **Part Two - "Disgrace at Hanoi" (河内辱命)** is UNDERWAY: B06 = Preface (ch10) +
  Chapter 1 (ch11); B07 = Ch2 (ch12); B08 = Ch3 (ch13); B09 = Ch4 (ch14); B10 = Ch5
  (ch15, the CLIMAX). The assassination has FAILED (Zeng killed, three captured, Chen
  recalled to Chongqing).
- **NEXT: B11 = ch16** 第六章 奸伪卑劣 寿张为幻 "Vile Treachery, Illusions Undone" - the
  reckoning-and-indictment chapter: Chen owns the failure, then quotes and demolishes
  Wang's own 行状 eulogy and 举一个例 apologia (with the National Defense Council meeting
  record). ~23,759 chars, four (一)-(四) sub-sections (one glued), two long quoted
  documents, a "(第六章完)" coda.

## What is NEXT

- Batch B11 = ch16 (Part Two, Chapter 6). Kickoff is the paste-block at the top. Runs
  to completion (no gate); ends by pasting the B12 kickoff.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at
  4.55-4.76 en/han; document-/essay-heavy chapters run higher; ch16's quoted Wang
  documents will lift it. Read the note, do not reset.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/ch16 numbered-in-parens
  (一)/(二)…; ch08/ch16 have a GLUED sub-heading (on a paragraph tail); ch13's inner
  enumerated list 一、-六、 rendered `####`. Grep each new chapter.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character
  phrases, terminal-」 name-splits, the in-text "(第N章完)" coda pattern (ch12/ch13/ch16),
  fullwidth-zero (U+25CB) years/refs, and single-character substitutions. Re-grep each
  batch's source for `\[\d+\]` note markers (none present through B10).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the
  full B02-B10 historical-name set (Part One; the B06-B07 Japanese/negotiator/elder
  names; the B08 Wang-essay set; the B10 additions - Chen Bangguo, the Zeng household,
  Hiranuma Kiichirō, Wu Jingheng, Jin Xiongbai, Fang Junbi, etc.).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二,
  坂垣征四郎, 近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤, 伊藤芳男; 大屋久寿雄 "Ōya Kusuo";
  平沼骐一郎 "Hiranuma Kiichirō" - added B10).
- Identify 剑秋 "Jianqiu" (a 1932 Nanjing "elder brother" of Chen) when sources allow.
- Stray source glyphs still to resolve in later batches: 寿张为幻 in the ch16 title
  (B11 - flag the source uncertainty); trailing 杀 on the ch22 title; 毛酋 in a ch36
  section title.
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows,
  incl. the B10 additions: Tang Yingjie, Yu Jiansheng, Chen Bangguo, the Zeng household).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B10 builds (0/0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical
  typos). B01-B10 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 (from the `<title>`) opens all 43 content files: drop
  it. drop count is variable - most drop=2; ch01 and ch10 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/roster lines, and verse lines in the
  source are DELIBERATE separate `<p>` - do NOT merge them; only genuine mid-phrase
  splits (last char not terminal, OR a source `<p>` boundary that severs one sentence)
  merge, and those can CHAIN across 3+ fragments. `<br/>` inside one `<p>` splits into
  extra extracted lines - decide per case. ALWAYS confirm the extracted body count
  p-by-p against data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters (ch14 and ch24); ch09 printed
  §五 before §四; ch13 restarts its (一)-(五) numbering for the appended essay. Preserve
  and, where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
