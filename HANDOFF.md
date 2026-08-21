# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-13 are COMPLETE (ch00-ch24). Next is
B14 = ch25 + ch26 + ch27, the FINAL batch (back matter, cover, whole-book
reconciliation, COMPLETION.md, commit the EPUB).

## Message to paste into the next chat

```
Zhou Enlai B14 (FINAL BATCH)

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 14 =
ch25 (《伍豪启事》的出笼与破灭 / The "Wu Hao Notice": Its Fabrication and Its
Collapse, PDF 553-569, printed 509-525; THREE sections ch25s01-03: 伪造的《伍豪
启事》出笼 / 临时中央为周恩来辟谣 / 斩断江青射出的毒箭) AND ch26 (结束语 /
Conclusion, PDF 570-578, printed 526-534) AND ch27 (后记 / Afterword, PDF 579-581,
printed 535-537), end to end per the CLAUDE.md pipeline. This is the LAST batch:
after the three units also do the BACK MATTER, the COVER, the whole-book
reconciliation sweep (check 12, check_reconcile.py + the by-hand grep of ~20
decided renderings), write out/term_ledger.md and out/deep_audit.md, feed decided
renderings into authority.json, write COMPLETION.md from the template (with the
sampled error rate), commit the EPUB itself (git add -f out/zhou-enlai.epub), and
rewrite HANDOFF.md to say the book is COMPLETE. Do NOT modify the kickoff section
of HANDOFF afterward (the Stop hook would demand a block that no longer exists).

Work on branch claude/zhou-enlai; expect a stray per-task branch and consolidate
onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai, reset --hard to origin,
do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch24 in out/ch24_reading.md
(Mu Xin's verdict on the traitor's inevitable end) so the voice carries over. ch25
is the《伍豪启事》(Wu Hao Notice) affair: the Kuomintang's Feb 1932 forged press
notice purporting to be Zhou Enlai (伍豪) renouncing Communism, the Provisional
Central Committee's rebuttal, and the 1967-80 legal reckoning after Jiang Qing and
the Gang of Four weaponized the forgery against Zhou during the Cultural
Revolution. STRONG corroboration target: the Wu Hao Notice is one of the
best-documented episodes in the book (already noted several times earlier —
grep notes.json before re-noting; the note is placed, cross-reference it). ch26 is
Mu Xin's Conclusion (exposition/argument — the highest-risk zone for stilted prose;
break the walls) and ch27 his Afterword (author's-voice; acknowledgements, sources,
how the book was made). Register: the same confident narrative-history voice; ch01
is the FROZEN reference; run check_register.py --ref out/ch01_reading.md on
every unit.

Pipeline notes specific to THIS book (all proven in B01-B13, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch25 opens PDF 553 = printed 509; ch26 PDF 570 = 526; ch27 PDF 579
  = 535. Book ends PDF 581 = printed 537.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. ocr_dual.py FIRST LAST is SLOW — run it in the BACKGROUND.
  Back up data/txt for the batch pages before the FIRST strip (mkdir
  data/txt_backup_b14).
- ASSEMBLY: USE THE B13 MODEL (scripts/recovery/b13_*.py are the newest;
  b13_rebuild.sh is the deterministic strip→structure→assemble→surgery→addfixes→
  apply_fixes→pagemap driver — copy it to b14 and edit the page range, backup
  dir, and unit ids/ranges). Key pieces, all current:
  (1) b13_strip_furniture.py: normalize garbled section/chapter headings to the
  EXACT book.json titles (byte-exact, incl. 《》). Section headings often sit
  MID-PAGE — grep the raw OCR to locate them. The foot-citation peeler is now
  LINE-BASED (is_citation) and handles citations glued to the last body line with
  no blank; it writes the stripped citations to data/b14_footnotes.txt for the
  Author's-note reproduction. Figure captions that OCR'd INTO the body: REMOVE_UNTIL
  (caption at page top) or TRUNCATE_AFTER (caption at page foot); find_figures
  MISSES line-art diagrams (B13 had one on p543), so eyeball every page.
  (2) b13_structure.py: pulls chapter+section rows from book.json into
  data/structure.json (idempotent) BEFORE assemble.
  (3) indents.py FIRST LAST (data/indent TRACKED). Indent geometry is UNRELIABLE
  here (the crop left-aligns, so no leading-space signal either) — determine
  paragraph boundaries by READING the page images. This is the labor: view each
  page, mark the 2-em indents, write one surgery marker per paragraph opening.
  (4) b13_surgery.py is the ROBUST re-segmenter (normalized-match, no snap). Write
  markers in CLEAN text; the DEMANGLE map de-mangles same-length name garbles for
  MATCHING only (it does NOT alter the text). Each marker must be the EXACT
  paragraph OPENING and unique after normalization. If a marker fails, the opening
  has a non-name OCR garble: put the GARBLED chars in the marker (it just has to
  match the raw blob). DIALOGUE turns are each their own paragraph. VERSE is ONE
  {p} line with " / " between verse-lines. DISPLAYED block quotes (memoir,
  newspaper, statements, the forged Notice, the rebuttal) render as PLAIN
  paragraphs, no outer quotes; an attribution intro ending in a colon is its OWN
  paragraph; inline dialogue keeps quote marks.
  (5) b13_addfixes.py builds data/ocr_fixes.json rows (name + numeral garbles),
  applied AFTER surgery. NAMES are PER-UNIT (a fold that is right in one chapter
  can be wrong in another — e.g. 张国栋 = 张国焘 in ch23 but the real person Zhang
  Guodong in ch24). (6) b13_pagemap.py regenerates data/pagemap.
  (7) b13_glossary.py adds glossary rows nested into people/places/works so
  qc_entities can reach them; every row needs en + pinyin + status.
- Name-mangle survey FIRST (Python Counter). Watch the homograph/fold traps that
  bit B13: do NOT fold a mangle that also spells a real name (陈庆斋, 刘杞夫,
  陈云/陈立/陈果/陈康-was-actually-Chen-Geng); do NOT add a glossary row for a
  place/person homograph (黄平 the county vs Huang Ping the man — removed).
- check_numbers phantoms (all seen before): note-ref circled-1 OCR'd as a trailing
  digit at a quote end (.0 / 9 / 7); 《 OCR'd as 4; a fraction 1/10 OCR'd 1710; a
  garbled year (193$/193S); idioms/measures go to data/noise.txt (九牛二虎, 千瓦,
  一再, 化整为零, 濮备九, [0-9]+年代, parenthesized CJK ordinals, 1个多月, 最后一期,
  十多万, arabic+万 composites). Longest first; comment every entry.
- Checks (all must pass): verify_unit UNIT_ID (parity+numbers+anchors, no --noise);
  make_bilingual UNIT_ID then qc_entities out/<id>_bilingual.md (accepts the en's
  FIRST or LAST word); ADD ch25/ch26/ch27 to data/check_config.json (docs+sources)
  then check_content --config (wants the EXACT glossary en form in the paired
  paragraph — align your EN to the SHELF form: 伍豪 = Wu Hao, 中央特科 = Central
  Special Section, 顺直省委 = Shun-Zhi provincial committee, 东方大学 = Communist
  University of the Toilers of the East, 绍敦电机公司 = Shaodun Electrical Company,
  改组派 = Kuomintang Reorganizationists, 蔡麻子 = Pockmarked Cai; and BEWARE short
  keys that grep as phrases); check_align UNIT_ID; check_structure --pairs SRC TGT;
  check_register --ref out/ch01_reading.md.
- Glossary: GREP glossary.json FIRST — 周恩来, 伍豪, 江青, 王明, 博古, 陈立夫,
  徐恩曾, 戴笠 all on the shelf. Consult authority.json for shelf agreement.
- Footnotes at reader-model density (a LATE chapter tapers; the recurring furniture
  is already noted — keep a "NOT re-noted" list). Author footnotes reproduced as
  "Author's note." at the ① anchor for QUOTED passages. Note anchors are verbatim
  ASCII substrings of the reading .md (straight ' and "); bodies use numeric char
  refs only (&#8212; &#8211; &#160; &#8220; &#8221; &#8217; &#8216;). Fact-check
  the Wu Hao Notice and the Jiang Qing / Cultural Revolution reckoning against real
  scholarship (WebSearch Wikipedia/academic; NEVER Grokipedia).
- Merge apparatus via apparatus_merge.py (plain JSON file, Write tool, then merge);
  check_apparatus.py must be clean. Build the cumulative EPUB, qa_epub green,
  epubcheck (/tmp/epubcheck-5.1.0).
- Then the FINAL-BATCH tail: back_matter.json (errata/colophon if the book has
  any), the whole-book reconciliation sweep (check 12), out/term_ledger.md,
  out/deep_audit.md, authority.json update, COMPLETION.md from the template, commit
  the EPUB with git add -f, rewrite HANDOFF.md to COMPLETE. Update PROGRESS.md;
  commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND (since this is the last batch)
the COMPLETION report summary in place of a next kickoff — the CLAUDE.md banner
still expects the fenced block, so paste the COMPLETION.md "book is COMPLETE"
message verbatim in a fenced code block.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02+ch03)** through **B12 (ch21+ch22):** complete.
- **B13 (ch23 Concealment/Withdrawal/Relocation + ch24 The Traitor Gu Shunzhang's
  Shameful End):** complete. ch23 = 101 body paras, 6 sections, 14 notes, 3
  figures: the reshuffle of the Special Committee and reorganization of the Special
  Section under Chen Yun; Chen Geng and Chen Yangshan's Tianjin mission and
  withdrawal; Li Qiang barred by Wang Ming from KUTV, made a Soviet radio expert;
  the "Three Heroes of Longtan" to the Central Soviet (Qian Zhuangfei lost on the
  Long March 1935; Hu Di murdered by Zhang Guotao 1936; Li Kenong); Liu Ding's
  arrest, escape, and route through Smedley and Rewi Alley to Xi'an; Zhou Enlai's
  own route to Ruijin, late 1931. ch24 = 63 body paras, 4 sections, 8 notes, 1
  figure: Gu Shunzhang hunted (Mao's 1931 wanted-order); the surrender policy and
  spy-training classes; the fawning book he ghost-wrote betraying the Special
  Section's structure; his execution by Xu Enzeng ~1935 at Suzhou, told through
  four conflicting agent memoirs. All checks green; details in PROGRESS.md B13.
- **EPUB:** out/zhou-enlai.epub = 25 of 28 chapters (ch00-ch24), 323 notes, 470
  pagebreaks; qa_epub PASS, epubcheck 0/0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop/context-verified readings for ch00-ch24; replay with
  apply_fixes.py on any fresh regen. B13 added ch23 + ch24 rows (name + numeral
  garbles), per-unit NAMES maps.
- scripts/recovery/ (tracked): b02_* through **b13_*** strip/surgery/pagemap/addfixes/
  glossary scripts + the b1X_rebuild.sh drivers. The **b13_* set is the CURRENT
  model**: robust LINE-BASED foot-citation peeler, per-unit fold maps, structure
  builder, glossary builder. Do not delete.
- data/noise.txt: keep extending, never prune. B13 added 九牛二虎, 五角形, 曾传六,
  一再, 千瓦, 濮备九, 化整为零, 一同, 最后一期, 1个多月, 十多万, 十亚不赦, 1/10,
  [0-9]+年代, and the parenthesized-CJK-ordinal pattern.
- data/check_config.json: docs+sources for ch00-ch24; ADD ch25/ch26/ch27 next batch.
- data/pagemap/ch23.json, ch24.json: regenerated post-surgery (b13_pagemap.py).
- data/txt_backup_b13/: raw OCR for PDF 485-552 (the rebuild driver's source).
- data/figs/: ch23_smedley.png, ch23_alley.png, ch23_ruijin_office.png,
  ch24_network.png (Gu's hand-drawn Second-Branch chart, cropped by hand from p543).
- KNOWN HAZARD: apply_fixes.py + surgery are NOT idempotent. Always clean-regen
  (b13_rebuild.sh) before apply_fixes; keep the raw data/txt backup for the batch.
- KNOWN HAZARD: qc_entities.py KeyErrors if a glossary row lacks "pinyin" — every
  row needs "en" + "pinyin". Accepts the en's first OR last word.
- KNOWN HAZARD: check_content wants the EXACT glossary en form; align your EN to the
  shelf form, or a short glossary key can FALSE-MATCH. Do NOT add a glossary row for
  a place/person homograph (removed 黄平 the county vs Huang Ping the man).
- KNOWN HAZARD: a per-unit fold map (b13_addfixes NAMES) exists because a name
  mangle that is right in one chapter can be a real different name in another
  (张国栋 = Zhang Guotao in ch23, the real Zhang Guodong in ch24; 陈庆 = Chen Geng
  in ch23 but part of Chen Qingzhai 陈庆斋 in ch24).
- Assembly: indents.py IS run but geometry is UNRELIABLE and the crop strips
  leading spaces; boundaries come from READING the page images and are encoded as
  surgery markers.

## Renderings settled (glossary.json is the ledger)

- Held terms carried from earlier: 巡捕房 concession police, 中央特科 Central Special
  Section, 红队 Red Squad, 打狗队 Dog-Beating Squad, 白色恐怖 White Terror, 中统
  Zhongtong, 军统 Juntong, 复兴社/蓝衣社 Renaissance Society/Blue Shirts, 国民党
  Kuomintang, 大公报 Ta Kung Pao, 申报 Shen Bao, 反省院 reformatory, 宋庆龄 Song
  Qingling (authority.json).
- B13 people added (nested rows, en+pinyin+status): 陈云 Chen Yun, 方志敏 Fang
  Zhimin, 李杜 Li Du, 史沫特莱 Smedley, 黄平 was REMOVED (homograph with Huangping
  county), 张国栋 Zhang Guodong (ch24, distinct from Zhang Guotao), 陈养山 Chen
  Yangshan, plus the Tianjin/Shunzhi/Moscow/Longtan/Liu-Ding/Ruijin cast and the
  ch24 Zhongtong-agent cast (Cai Mengjian, Huang Kai, Gu Jianzhong, Lin Jinsheng,
  Zhang Changgeng, Wang Yixin, Meng Zhen, Chen Weiru, Lin Chengyin, Pu Mengjiu, ...).
  陈康 was NOT a person (= Chen Geng); its stray row was removed.
- Shelf forms to MATCH in check_content: 顺直省委 Shun-Zhi provincial committee,
  东方大学 Communist University of the Toilers of the East, 绍敦电机公司 Shaodun
  Electrical Company, 改组派 Kuomintang Reorganizationists, 蔡麻子 Pockmarked Cai,
  特务工作之理论与实际 The Theory and Practice of Secret Service Work.
- Feed decided renderings into authority.json at book's end (out/term_ledger.md).

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. Break potted
  biographies and exposition into short confident statements, no dash-glosses. B13
  em-dash rate 4.8 (ch23) / 6.1 (ch24) per 1k vs the ch01 reference's 6.0; keep at
  or under. ch26 (Conclusion) is pure exposition — apply the anti-stilt rules
  hardest there.
- **Zhou Enlai** (the book's subject; the ch25 Wu Hao Notice is about him):
  measured, analytic, unflappable; the forgery is aimed at him and the rebuttal
  defends him. **Jiang Qing** (ch25s03): render the Cultural-Revolution weaponizing
  of the forgery cold, let the facts damn it, verdict in the note.
- **Reproduced material:** DISPLAYED blocks (the forged Notice, the Provisional
  Central Committee's rebuttal, telegrams, memoir, statements) render as PLAIN
  paragraphs, no outer quotes; INLINE dialogue keeps quote marks; an attribution
  intro ending in a colon is its OWN paragraph; VERSE takes {p} as ONE paragraph
  with " / " line breaks. Author source-citations reproduced as "Author's note."
  at the ① anchor (QUOTED passages only).

## Where the story stands

The clandestine arms are all drawn (ch04-18); the central catastrophe (Gu
Shunzhang's April 1931 defection, ch19-20); the manhunt (Chen Geng, Ding Ling,
Yang Xingfo, ch21-22); the orderly RETREAT of the apparatus and the END of the
traitor Gu Shunzhang (ch23-24). B14 (ch25-27) closes the book: the Wu Hao Notice
forgery and its 1930s fabrication and its 1960s-80s Cultural-Revolution afterlife
(ch25), Mu Xin's Conclusion (ch26), and his Afterword (ch27).

## Exact next-batch scope

- **B14 (FINAL)** = ch25 (PDF 553-569, printed 509-525, ch25s01-03) + ch26 结束语
  Conclusion (PDF 570-578, printed 526-534) + ch27 后记 Afterword (PDF 579-581,
  printed 535-537). Then the whole-book completion tail: back matter, cover,
  reconciliation sweep (check 12), term_ledger.md, deep_audit.md, authority.json,
  COMPLETION.md, commit the EPUB, mark the book COMPLETE.
  (out/SURVEY.md's batch numbering runs one behind, since B05 combined ch07+ch08.)

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY: b13_rebuild.sh is the model; markers need EXACT-opening unique openings;
  put non-name OCR garbles literally into the marker; extend the DEMANGLE map for
  same-length NAME garbles a marker needs; DRY-RUN until paragraph counts match.
- Per-unit fold maps: never fold a mangle that spells a real name in the other unit.
- Surgery + apply_fixes are NOT idempotent (use the rebuild driver).
- data/indent is TRACKED — git checkout it if you rm -rf'd it before re-running.
- qc_entities needs "pinyin" on every glossary row; check_content wants the EXACT
  shelf en form; both read the bilingual PATH.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract must
  read 0 after a run. ocr_dual is slow — background it.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
