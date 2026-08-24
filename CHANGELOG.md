# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

## 2026-08-24 — FN5 footnote-density pass, ch23-ch27 + whole-book close-out (FOOTNOTE_PASS.md batch 5, LAST)
Final batch of the commissioner's footnote-density pass (the manhunt survivors and
the radio-line reconstruction; Gu Shunzhang's shameful end; the Wu Hao Notice affair;
the Conclusion and Afterword), plus whole-book apparatus reconciliation and close-out.
Content FROZEN: notes ADDED and reconciled only; no prose/number/name/date/paragraph
change (git diff touches only notes.json + data/fn5_notes.json + scripts/recovery/
fn5_*.py + docs + the rebuilt EPUB; no out/ch*_reading.md edited).
- **+16 footnotes. Book 441 -> 457.** Tail (ch23-27) +6: ch23 14->17 (State Political
  Security Bureau, Ma Haide, Dragon Boat Festival), ch25 8->10 (Shi Liangcai, Tao
  Xingzhi), ch26 7->8 (Shen Anna); ch24 and ch27 a genuine +0. Whole-book
  reconciliation +10, each at true first appearance: ch02 shikumen, ch03 Sun Yat-sen
  University Moscow, ch04 Third Plenary Session of the 11th CC, ch05 Sun Chuanfang,
  ch10 Shen Bao, ch14 China Mutual Aid Society + Ta Kung Pao, ch15 E-Yu-Wan Soviet,
  ch16 Baoding Military Academy, ch17 Li Mingrui.
- Reconciliations (first-appearance discipline): three pre-existing later notes
  trimmed to cross-references — Shen Bao (ch17 -> ch10), Sun Yat-sen University Moscow
  (ch18 -> ch03), E-Yu-Wan Soviet (ch19 -> ch15).
- 互济会 "rendering drift" resolved as a historical rename, not an error: 中国济难会 ->
  "China Relief Society" (1925) and 中国互济会 -> "China Mutual Aid Society" (1929
  rename) are two consistent glossary mappings; a bridging note at ch14 ties them. No
  glossary or prose change.
- Hu Yepin cluster (ch09/ch20/ch22) confirmed complementary, not double-noted.
- COMPLETION.md per-chapter Notes column rebuilt from notes.json (it had carried the
  stale translation-batch counts through FN1-FN4); density record added.
- Fact-check: every claim checked against real scholarship (Wikipedia, Baidu Baike,
  Cambridge China Quarterly, UH Press, SHINE/China Daily); verdict in each note. NO
  Grok/Grokipedia or AI-written reference used (surfaced for Ma Haide / Longzhou /
  assassinations queries and rejected).
- Hanzi: three org/work notes carry numeric character references generated from
  glossary strings (申报, 中国互济会, 大公报); all others use pinyin/English. 0 U+FFFD in
  the EPUB xhtml.
- QC: check_apparatus.py 0/0; build 28/28, 457 notes; qa_epub PASS; epubcheck 5.1.0
  0 fatals/0 errors/0 warnings. Tooling added: scripts/recovery/fn5_authorel.py
  (note authoring, glossary-driven hanzi) and scripts/recovery/fn5_trims.py (the
  reconciliation trims). **The footnote-density pass (FN1-FN5) is COMPLETE.**

## 2026-08-24 — FN4 footnote-density pass, ch18-ch22 (FOOTNOTE_PASS.md batch 4)
Fourth batch of the commissioner's footnote-density pass (the radio men and cipher
work; the Gu Shunzhang defection and its averting; the Yun Daiying, Cai Hesen, and
Xiang Zhongfa betrayals; the Chen Geng and Wang Genying manhunts; the Ding Ling
abduction and the Yang Xingfo assassination). Content FROZEN: notes ADDED and
reconciled only; no prose/number/name/date/paragraph change (git diff touches only
notes.json + data/fn4_notes.json + docs + the rebuilt EPUB; no out/ch*_reading.md
edited).
- **+14 footnotes. Book 427 -> 441; ch18-ch22 57 -> 71.** Per unit:
  ch18 15->19, ch19 9->10, ch20 12->14, ch21 11->14, ch22 10->14.
- Classes swept per FOOTNOTE_PASS.md 2-6: people (Gu Zhenghong, Deng Zhongxia,
  Qiu Jin, Agnes Smedley, Zhang Wentian, Yang Shangkun); places/institutions (the
  Naigai Cotton Mill, Wayaobao, Academia Sinica); orgs (the Comintern's Far Eastern
  Bureau, the Young China Association); units/offices (the 19th Route Army, the
  Eighth Route Army, the Executive Yuan). Cross-references placed to existing notes
  (May Thirtieth ch01, Canton-Hong Kong strike ch10, Noulens ch21, Jan 28 Incident
  ch20, New Fourth Army ch04).
- Reconciliation (first-appearance discipline, mandated by the FN4 kickoff): the
  Agnes Smedley ID note trimmed at ch23 to a cross-ref to chapter 22 (her first
  appearance).
- Fact-check: every claim checked against real scholarship (Wikipedia, Cambridge/
  academic histories, official CCP-history and PRC-foreign-ministry sources); verdict
  stated in each note. NO Grok/Grokipedia or AI-written reference used (Grokipedia
  surfaced in result lists and was rejected each time).
- QC: check_apparatus.py 0/0; build 28/28, 441 notes; qa_epub PASS; epubcheck
  5.1.0 0 fatals/0 errors/0 warnings.

## 2026-08-24 — FN3 footnote-density pass, ch12-ch17 (FOOTNOTE_PASS.md batch 3)
Third batch of the commissioner's footnote-density pass (the Bai Xin manhunt and
Avenue Joffre gunfight aftermath; the Ren Bishi and Guan Xiangying rescues; the
Yang Du / Du Yuesheng "new chapter" trio; the Liu Shaobai, pastor, and lawyer
connections; the Songhu Garrison Command and Song Zaisheng; Li Qiang and the
radio branch). Content FROZEN: notes ADDED and reconciled only; no
prose/number/name/date/paragraph change (git diff touches only notes.json +
data/fn3_notes.json + docs + the rebuilt EPUB; no out/ch*_reading.md edited).
- **+18 footnotes. Book 409 -> 427; ch12-ch17 65 -> 83.** Per unit:
  ch12 8->9, ch13 8->9, ch14 11->20, ch15 19->24, ch16 8->8 (already dense),
  ch17 11->13.
- Classes swept per FOOTNOTE_PASS.md 2-6: people (Chen Yun, Kang Youwei, Song
  Meiling, Ji Yun/Xiaolan, Zhang Shizhao, Huang Jinrong, Lu Xun, Cai Yuanpei, Tan
  Sitong+Tang Caichang, Eugene Chen, Bo Gu, Long Yun); places (Tilanqiao Prison);
  events/orgs (the Four Great Families, the Renaissance Society/Blue Shirts, the
  Red China News Agency -> Xinhua, the Ningdu Uprising / 26th Route Army); source-
  accuracy (the Civil Rights League postdates Yang Du's death; the Song Meiling
  morphine-plant charge graded as the author's uncorroborated assertion).
- Reconciliations (first-appearance discipline, both mandated by the FN3 kickoff):
  Chen Yun ch23 note trimmed to a cross-ref to chapter 12 (his first appearance);
  the Renaissance Society ch21 note trimmed to a cross-ref to chapter 15.
- Fact-check: every claim checked against real scholarship (Wikipedia, China Daily,
  academic sources); verdict stated in each note. NO Grok/Grokipedia or AI-written
  reference used (both surfaced in result lists and were rejected).
- QC: check_apparatus.py 0/0; build 28/28, 427 notes; qa_epub PASS; epubcheck
  5.1.0 0 fatals/0 errors/0 warnings.

## 2026-08-24 — FN2 footnote-density pass, ch06-ch11 (FOOTNOTE_PASS.md batch 2)
Second batch of the commissioner's footnote-density pass. Content FROZEN: notes
ADDED and reconciled only; no prose/number/name/date/paragraph change (git diff
touches only notes.json + data/fn2_notes.json + docs; no out/ch*_reading.md
edited).
- **+24 footnotes. Book 385 -> 409; ch06-ch11 70 -> 94.** Per unit:
  ch06 7->11, ch07 14->20, ch08 13->16, ch09 16->21, ch10 9->12, ch11 11->14.
- Classes swept per FOOTNOTE_PASS.md 2-6: people (Zhang Daofan, Sun Ke, Li
  Zongren, Liang Qichao, Yang Yuting, Wu Zhihui, Chen Yi, Yang Zhihua/Du Ning);
  places/events/orgs (Fengtian city+clique, Nanyang College, Central Military
  Academy, Green Gang, Sixth National Congress, League of Left-Wing Writers,
  Northeast Anti-Japanese United Army, Hailufeng soviet, Canton-Hong Kong Strike);
  terms (Sun Yat-sen tunic, Four Cardinal Principles, the 1927 vs 1966 "Red
  Guards" caution); allusions/quotations/works (the Mao 1935 report source, Su
  Shi's "true face of Mount Lu," Water Margin & Romance of the Three Kingdoms,
  Zeng Guofan's Family Letters).
- Reconciliations (first-appearance discipline): Liu Bocheng ch07 note trimmed to
  a cross-ref to chapter 1 (mandated); Qian Dajun ch10 note trimmed to a cross-ref
  to chapter 3; the Canton-Hong Kong Strike note moved from ch11 to its ch10 first
  appearance, ch11 trimmed to a cross-ref.
- Fact-check: every claim checked against real scholarship (Wikipedia/Baidu/
  Britannica/academic/primary texts); verdict in each note; NO AI-sourced
  references (Grok/Grokipedia results rejected). Flags: Yang Zhihua 1900/1901;
  Fengtian naming history; Green Gang police-penetration stated to scholarship.
- Hanzi: only 奉天 and 中国左翼作家联盟, both from glossary.json, emitted as numeric
  refs generated from the glossary string (never hand-typed); people notes carry
  none.
- check_apparatus clean; build 409 notes / 496 pagebreaks; qa_epub PASS;
  epubcheck 5.1.0 0/0/0.

## 2026-08-24 — FN1 footnote-density pass, ch00-ch05 (FOOTNOTE_PASS.md batch 1)
First batch of the commissioner's footnote-density pass. Content FROZEN: notes
ADDED only; no prose/number/name/date/paragraph change (git diff touches only
notes.json + the two merge files + docs; no out/ch*_reading.md edited).
- **+46 footnotes. Book 339 -> 385; ch00-ch05 109 -> 155.** Per unit:
  ch00 12->19, ch01 28->41, ch02 16->22, ch03 13->19, ch04 24->34, ch05 16->20.
- Classes swept per FOOTNOTE_PASS.md 2-6: people (largest class — the fast-
  turning early cast: Zhu De, He Long, Liu Bocheng, Qu Qiubai, Li Lisan-line,
  Zhao Shiyan, Chen Yannian, Zhang Tailei, Li Weihan, Su Zhaozheng, Liu Shaoqi,
  Xiang Ying, He Mengxiong, Li Dazhao, Cai Hesen, Deng Yanda, Sun Bingwen, Yang
  Yin, He Yingqin, Tang Shengzhi, Ye Jianying, Zhou Yiqun, Kong Xiangxi, Li
  Fuchun, Chen Diaoyuan, Yuan Shikai, Sun Yat-sen, Borodin, Deng Yingchao, Li
  Qiang, Zhou Enlai, Chiang Kai-shek); places/events (Great Revolution, Northern
  Expedition, Eastern Expeditions, Guangzhou/three-Shanghai-uprisings, May Fourth,
  Xi'an Incident, Zhang Xun's 1917 restoration, Fifth Congress, Nov-1927 enlarged
  Politburo, "July 15" split, Central Soviet); institutions/terms (Comintern,
  Tongmenghui, Reorganizationists, China Relief Society/MOPR).
- Filled a dangling cross-reference: the ch00 Wang Jingwei note pointed to a
  "July 15" note "in the next chapter" that did not exist; now added at ch01.
- Accuracy/partisan-source notes (verdict in the note): Chen Diaoyuan (20-million
  -yuan plunder = author's, uncorroborated; ticket-bandit nickname = 1923 Lincheng
  case); Reorganizationists ("under Hu Hanmin" loose — looked to Wang Jingwei);
  Xiang Ying birth year 1895/1898 flagged.
- Fact-checked against real scholarship only (Wikipedia EN/ZH, Baidu Baike,
  Britannica, Maitron, CCP-history sites); no Grok/Grokipedia/AI sources.
- Every hanzi inserted as a numeric character reference, decoded and cross-checked
  against glossary.json / standard forms; people notes carry no hanzi.
- Merged via scripts/apparatus_merge.py (data/fn1_notes_a.json = ch00-01,
  data/fn1_notes_b.json = ch02-05). check_apparatus clean; qa_epub PASS;
  epubcheck 5.1.0 0/0/0. New helper scripts: scripts/fa_check.py (first-appearance
  grep) and scripts/gloss_hanzi.py (glossary hanzi reverse-lookup).
- data/zh not regenerated (parity scaffold, not needed for a notes-only pass;
  rationale in PROGRESS.md FN1).
- One cross-chapter reconciliation logged for FN2 (Liu Bocheng ch01 first-appearance
  ID vs existing ch07 bio); see PROGRESS.md FN1.

## 2026-08-22 — R5 register pass: tail tic sweep, reconciliation, CLOSE (ch23-ch27 + whole book)
Final register batch: tail tic sweep of ch23-ch27, then the whole-book
reconciliation and close-out. Content frozen (no para merged/split, no fact/
number/name/date/hedge changed). Reading text edited via edits/<id>_edits.md +
apply_edits.py, except the 叛徒 collapse (a global rendering fix done grep-driven
per the CLAUDE.md corrections workflow).
- **Tail tic sweep, 6 edits** across ch23(3)/ch24(1)/ch25(2): 相继/先后 people ->
  "in succession"; 出力不小 litotes -> "a great deal"; 除…外 "besides" ->
  "apart from". **ch26 and ch27 came back clean** (0 edits).
- **叛徒 variety check -> renegade collapsed.** "renegade" (29 occ., confined to
  batch B12 ch21/ch22 + ch24, all rendering 叛徒, co-occurring with "traitor")
  was per-batch drift; collapsed renegade -> traitor at 28 sites
  (scripts/recovery/r5_collapse_renegade.py; anchor-safe), 1 kept where the same
  sentence already used "traitor" (ch21 Chen Weiru). "turncoat" (11 occ.) kept
  as the STYLE-sanctioned variant. CASCADE SCOPE: out/ch21,ch22,ch24_reading.md;
  no notes/glossary body contained "renegade".
- **Killing-verb ledger, 3 source-verified edits:** 镇压/除掉 of traitors by the
  Red Squad softened to "put down"/"did away with" -> "eliminated"
  (ch09 x2, ch16 x1). Borderline/quoted/idiom/movement-suppression uses KEPT.
- **Whole-book antique-straggler sweep, 2 edits** the per-chapter gates missed:
  ch12 "whereupon" -> "and then"; ch22 "at length" (终于, in the 1984 org-dept
  notice) -> "at last".
- **破坏 -> "wreck*" reviewed and LEFT** as contextually appropriate (mass-arrest
  destruction = smash/wreck, not covert "sabotage"); the abstract-noun calque
  the ledger flagged does not survive. Site inventory recorded in PROGRESS.md if
  a uniform "sabotage" is ever wanted.
- check_reconcile.py: epithet-drift candidates all hyphenation noise; glossary
  forward 845/849 (4 pre-existing legitimate unused forms); theatre/theater is
  the recorded venue-proper-name split, not drift.
- Whole-pass (R1-R5) diff audit: 192 word-level edits, 188/188 balanced, zero
  paragraph-boundary changes; KEEP-list grep clean. Spot audit 20+ paragraphs,
  zero meaning drift.
- Pre-flight: stray branch claude/modest-archimedes-7h5vbz folded into
  claude/zhou-enlai; data/zh regenerated for ch17-ch27 (b10-b14 drivers);
  ch09/ch10/ch16 pages re-OCR'd for killing-verb source.
- Files touched: out/ch09,ch12,ch16,ch21,ch22,ch23,ch24,ch25_reading.md;
  edits/ch09,ch12,ch16,ch22,ch23,ch24,ch25_edits.md;
  scripts/recovery/r5_collapse_renegade.py; PROGRESS.md; COMPLETION.md;
  HANDOFF.md; out/zhou-enlai.epub (rebuilt). notes.json byte-unchanged (339).
- Build: 28/28, 339 notes, 496 pagebreaks. qa_epub PASS. epubcheck 5.1.0:
  0 errors / 0 warnings. **The register revision pass (R1-R5) is CLOSED.**

## 2026-08-22 — R4 register pass: tic sweep, back batch (ch18–ch22)
Tier-B tic sweep of the back batch (ch18–ch22), including the spine test on
ch19's five and ch21's two flagged long sentences. Reading text edited via
edits/<id>_edits.md + apply_edits.py; content frozen (no para merged/split, no
fact/number/name/date/hedge changed, no quoted material touched).
- **19 English-surface edits** across ch18(4)/ch19(6)/ch20(4)/ch21(5)/ch22(0):
  trailing 此外/并且/又/还/还有 "besides" → "also"/"as well"; 除…外 "besides X"
  → "apart from X"; 先后 "one after another" → "in succession" (people) and
  接连 reordered for rhythm; 只好 "could only" → "had no choice but to"; 便
  "thereupon" → "then"; 后来 "At length" → "Later"; inverted antique "let slip
  no chance" → "missed no chance"; de-nominalized "the teaching of the …";
  **one calibrated-ruling-1 de-inversion** (ch19 L79 fronted-infinitive subject);
  **one spine split** (ch21 L201 run-on cut at the hall).
- **ch22 came back clean** (0 edits): a testimony-saturated chapter (the prison
  hypnotism memoir, the Shen Bao report, Shen Zui's assassination account, the
  Organization Department statement) — every tic is KEEP-listed. ch20 likewise
  KEPT every in-quote litotes/could-only/besides (Chen Yangshan / Bao Junfu /
  Chen Geng's reply letter).
- Long-sentence spine test: only ch21 L201 split; all others pass (single-spine
  biographies, colon-plus-list measure enumerations, rhetorical how-lists that
  keep the author's heat, semicolon-balanced deliberations, quoted documents).
- KEEP-list guard caught and left three in-quote hits: "could only work hard to
  repay" (ch18, Zhang Shenchuan memoir), "Presently Chiang Kai-shek came" (ch19,
  Cai Mengjian testimony), "could only make contact by telephone" (ch20, Chen
  Yangshan testimony).
- ch21's 18 等-tags ("and the rest"/"and the others") LEFT as genuine
  varying-membership truncations; the mild arrestee-group alternation is flagged
  for R5's whole-book check_reconcile.py (the plan's place for it).
- Pre-flight: regenerated data/zh for ch18–ch22 from data/txt_backup_b1* via the
  b1N_rebuild.sh drivers; all five verify_unit green before any edit.
- Files touched: out/ch18,ch19,ch20,ch21_reading.md;
  edits/ch18,ch19,ch20,ch21,ch22_edits.md; PROGRESS.md; rebuilt
  out/zhou-enlai.epub. notes.json unchanged (339; no anchor moved).
- verify_unit green on all five; check_register within tolerance vs
  ch01_reading.pre-R.md (em-dash 1.00×); typography guard clean (0 curly quotes,
  0 new ellipses); qa_epub PASS; **epubcheck 5.1.0: 0 errors, 0 warnings.**

## 2026-08-22 — R3 register pass: tic sweep, middle batch (ch09–ch14, ch16, ch17)
Tier-B tic sweep of ch09–ch14 and ch17, plus the FULL aligned zh-en read of
ch16. Reading text edited via edits/<id>_edits.md + apply_edits.py; content
frozen (no para merged/split, no facts/numbers/names/hedges changed).
- **18 English-surface edits** across ch09(5)/ch11(4)/ch13(1)/ch14(5)/ch16(2)/
  ch17(1): litotes 不少/不小 ("no few/no little" -> "a good many / quite a few /
  a good deal of"); 除...外 "besides" -> "apart from"; trailing 并/还 "besides"
  -> "as well"; 纷纷 -> "each" (distributive) and 相继 -> "in succession"; the
  ch11 martyr-group 等-list drift collapsed to "and the others"; two narration
  ellipses cut per STYLE ruling 8 (ch14); 只得 -> "had no choice but to" (ch16).
- **ch16 got the full aligned read** (42 paras, 2 edits): it is largely
  operational, not elevated-antique like ch15, so it correctly yields few
  register edits — no padding to a number.
- **ch10 & ch12 came back clean** (0 edits): quoted memoirs/letters/dialogue and
  meaningful "and the others"/"and the rest" distinctions, respected per KEEP.
- Long-sentence spine test on the >90-word narration sentences: no split (single-
  spine colon-lists, em-dash action beats, or splitter artifacts across in-quote
  periods).
- KEEP-list guard caught two mechanical over-corrections and left them: "let
  slip not a moment" (ch11, Zhou Enlai's quoted essay) and "whereupon" (ch12,
  quoted newspaper).
- Files touched: out/ch09,ch11,ch13,ch14,ch16,ch17_reading.md;
  edits/ch09,ch11,ch13,ch14,ch16,ch17_edits.md; rebuilt out/zhou-enlai.epub.
  notes.json unchanged (339; no anchor moved).
- verify_unit green (ch16 shows only its pinned pair-2 zh artifact);
  check_register within tolerance vs ch01_reading.pre-R.md; typography guard
  clean (zero new smart punct); spot-audit of all 18 sites vs source = zero
  meaning drift.
- Build 28/28, 339 notes; qa_epub PASS; **epubcheck 5.1.0: 0 errors, 0 warnings.**
- Noted for R5 (book-wide diction ledger, not fixed piecemeal): 破坏 ->
  "wrecking" (ledger: sabotage) and 镇压/除掉 -> soft "put down"/"did away with"
  (killing-verb ledger: eliminate/kill); these need a whole-book cascade.

## 2026-08-22 — R2 register pass: tic sweep, front batch (ch00–ch08)
Tier-B tic sweep of the front chapters. Reading text edited via
edits/<id>_edits.md + apply_edits.py; content frozen (no para merged/split,
no facts/numbers/names/hedges changed).
- **11 English-surface edits** across ch01(2)/ch02(1)/ch04(1)/ch06(6)/ch07(1):
  相继/陆续/先后 "one after another" calques, 不少/不小 litotes ("no little/no
  small" -> "a good deal of/considerable/sizable"), trailing/appositive
  "besides" (-> "also/as well/other"), 不得不 "could not but" -> "had to".
- **ch00/ch03/ch05/ch08 came back clean** (0 edits): quoted memoirs and
  idioms, respected per the KEEP list. ch08's whole body is Zhao Weigang's
  memoir; all its tic hits are KEEP-list.
- Long-sentence spine test on the >90-word narration sentences: no split (all
  single-spine list/cumulative constructions).
- Files touched: out/ch01_reading.md, out/ch02_reading.md, out/ch04_reading.md,
  out/ch06_reading.md, out/ch07_reading.md; edits/ch0{1,2,4,6,7}_edits.md;
  rebuilt out/zhou-enlai.epub. notes.json unchanged (339; no anchor moved).
- verify_unit matches §2 pins; check_register within tolerance vs
  ch01_reading.pre-R.md; typography guard clean (zero new smart punct);
  spot-audit of all 11 sites vs source = zero meaning drift.
- Build 28/28, 339 notes; qa_epub PASS. epubcheck not available in this
  container (fetch network-restricted); qa_epub is the gate.

## 2026-08-22 — R1 register pass: Tier A globals + ch15 exemplar
Reading text edited via edits/<id>_edits.md + apply_edits.py; Politburo via a
global cascade (CLAUDE.md). Content frozen (no para merged/split, no facts or
hedges changed).
- **Dates:** 95 day-month dates -> month-day (ch00-ch05, ch09-ch12). Cascaded
  to 5 note anchors (ch00, ch02 x3, ch12) and 3 figures.json `before` anchors
  (ch01, ch02, ch11).
- **Politburo:** 政治局/中央政治局 -> "the Politburo" book-wide (51 reading + 3
  note bodies); recorded in glossary.json and authority.json.
- **Ledger residuals:** "in good time" -> "in time/promptly" (14 narration
  sites); ch07 "driving into the heart of the enemy" -> "planted inside..."
  (打入). Three quoted "in good time" in ch15 kept (quoted testimony).
- **ch15 exemplar:** 12 narration edits (litotes calques, trailing "besides",
  "given to startling acts", "in his lifetime", 只好, a calqued "one after
  another"); quoted material untouched; the R2-R5 calibration target.
- Build 28/28, 339 notes, 496 pagebreaks; qa_epub PASS; epubcheck 5.1.0 clean;
  10% spot-audit (15 paras) vs source: zero meaning drift.

## 2026-08-22 — R1 pre-flight: data/zh regeneration + recovery tooling (no reading text changed)
- Regenerated `data/zh/` for all 28 units; verify_unit GREEN on 26/28.
- TOOLING (do not revert): added `scripts/recovery/b01_surgery.py` (ch00
  Preface: assemble range 36-38, strip furniture + 2 boundary repairs -> 6
  paras, GREEN); patched `scripts/recovery/b02_surgery.py` to skip-and-warn on
  a missing OCR anchor instead of a fatal SystemExit (ch02 -> 40/40 GREEN
  under tesseract 5.3.4).
- Documented in `scripts/recovery/README.md` the B01 recipe and the two
  parity limits (ch01, ch03) this container's tesseract 5.3.4 cannot
  reproduce; pinned the known-benign warnings in `REVISION_PLAN.md` section 2.
- Snapshotted `out/ch01_reading.pre-R.md` as the frozen register reference.

## 2026-08-22 — revision pass planned (no text changed)
- Added `REVISION_PLAN.md` from the template: five batches (R1 foundation +
  globals + ch15 exemplar; R2-R4 tic sweeps front/middle/back; R5 tail +
  reconciliation + close), filled with live examples, KEEP list, and verbatim
  kickoffs for every batch.
- `HANDOFF.md` again carries a paste-ready kickoff (R1) as its first section;
  the completion notice stands below it.
- Still no reading text, apparatus, or EPUB content modified.

## 2026-08-22 — register-pass assessment (no text changed)
- Added `review/REGISTER_PASS_ASSESSMENT.md`: a measured survey of the built
  book against the register rebaseline and style machinery on
  `claude/the-sword-roars` (commit 8431573), with a ranked defect inventory,
  prose quality score, and a recommendation for a bounded tic-sweep pass.
- TOOLING: imported `scripts/register_tics.sh` (the sword branch's grep
  battery for the rebaseline kill list; runs against this repo unmodified).
- No reading text, apparatus, or EPUB content was modified.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-22 — B14 (final batch) + book completion
- Translated ch25 (Wu Hao Notice), ch26 (Conclusion), ch27 (Afterword); book now 28/28 complete.
- GLOBAL: spelling locale standardized to American across all units (out/ch10 grey->gray; out/ch13, out/ch14 travelled->traveled; notes.json theatre->theater). Proper-noun "Theatre" venue names kept.
- GLOSSARY: added B14 rows (people/places/works); removed 斗争 (works; false-matched "struggle") and 罗斯 (substring of 俄罗斯).
- Ledgers: authority.json fed with decided renderings (slug zhou-enlai); out/term_ledger.md and out/deep_audit.md written; COMPLETION.md written; HANDOFF.md -> COMPLETE.
- Rebuilt: qa_epub PASS, epubcheck 0/0/0. EPUB committed with git add -f.
