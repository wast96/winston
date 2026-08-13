# HANDOFF — The Rebel (叛逆者) / Bi Yu

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE
CHAT, alongside the attached EPUB. Writing it here alone does not count.**
Rewrite it at the end of every batch; always keep the paste-ready kickoff
below as its first section. When the book completes, replace it with the
completion notice and do not touch it afterward (the Stop hook keys off it).

Batch 1 passed the first-chapter voice gate. ch01 is FROZEN as the register
reference (`reference/ch01.md`); STYLE.md is the prose contract. From here on
every batch is a normal batch that ends at its next-batch kickoff. The Rebel
(ch01-ch14) is complete. The Postman is under way: B03 (installments 1-6,
ch15-ch20) and B04 (installments 7-11, ch21-ch25) are done. Next is B05, The
Postman installments 12-15 plus the Afterword (ch26-ch30), which COMPLETES The
Postman.

## Message to paste into the next chat

```
The Rebel B05

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then STYLE.md (the prose contract), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, four Republican-era espionage novellas, into an annotated English EPUB. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub. Run ./setup.sh first; if data/src is empty, re-ingest with scripts/ingest_epub.py source.epub (it is gitignored and regenerable).

ch01 is FROZEN as the register reference (reference/ch01.md). This is a NORMAL batch: run it end to end and finish with the TWO chat deliverables (the built EPUB attached AND the next batch's kickoff pasted verbatim in a fenced block). Do NOT stop for a voice gate.

Do Batch B05 = The Postman installments 12-15 + Afterword (units ch26 through ch30), source files data/src/29_part0027.txt .. 33_part0031.txt, per the CLAUDE.md pipeline and STYLE.md. This COMPLETES The Postman (邮差), the SAME novella and cast as B03/B04: its story and characters carry over. Read the final two pages of ch25's English (out/ch25_reading.md) before you start, to catch the voice seam. ch25 ends the assassination arc: Xiufen is dead, Qin Zhaokuan is revealed as a deep-cover Zhongtong (Nationalist) agent and dies, and Chen Taining is charged with getting Su Lina out of Shanghai. The Postman voice sheets and settled renderings are in this HANDOFF; consult them. ch01 of The Rebel remains the frozen register reference for check_register (do not re-freeze).
1. Read ch26-ch30 from data/src/. Fix extractor-split paragraphs (a body line whose last char is not in 。！？"）…—). For ch26-ch29 the source has a DOUBLED heading line per file, so make_bilingual runs with skip=2. ch30 is the 后记 (Afterword): INSPECT its source head first (`sed -n '1,4p'`), it may NOT carry the doubled heading line, so set skip to match (skip=1 if the title appears once, skip=2 if doubled). Grep each unit for source note markers (\[\d+\]) and record "none present" in PROGRESS.md (the source has carried none through the whole book so far; grep anyway).
2. Translate to STYLE.md: literary contemporary English, restrained third person; dialogue IN QUOTATION MARKS (the source runs it unmarked), natural and contracted, grave where the weight wants it; name each character once per paragraph and let pronouns carry the rest (this satisfies qc_entities and check_content — the latter wants the FULL glossary name, e.g. "St. Thérèse's Church" not bare "St. Thérèse's"). Consult glossary.json and authority.json BEFORE romanizing ANY name or term; carry forward the settled renderings and voice sheets in this HANDOFF. The Afterword (ch30) is the author's own reflective voice, not the narrative: translate it faithfully; check_register will likely flag it as off-reference (a different register), which is EXPECTED for an authorial afterword (an exempt register per references/register-drift.md) — record it, do not distort the prose to hit the number.
3. Per unit, in order: write out/<id>_en.json (one English paragraph per source body line); make_bilingual.py <id> <src> <title_en> out/<id>_en.json <skip> (title_en is the installment number 12..15 per book.json for ch26-ch29, and "Afterword" for ch30; skip is 2 for ch26-ch29, and whatever ch30's head requires); split_bilingual.py out/<id>_bilingual.md <id> "<zh title>"; then verify_unit.py (parity + numbers, it uses data/noise.txt), check_align.py <id>, check_content.py --config review/content_config.json, qc_entities.py out/<id>_bilingual.md glossary.json, and check_register.py --ref reference/ch01.md out/<id>_reading.md. Verify each unit's TAIL against the source. Add non-quantitative numerals to data/noise.txt with a comment as they flag; NEVER noise a real quantity.
4. Footnotes per STYLE.md's apparatus doctrine — be generous, the commissioner loves them: cover history, institutions, money, geography, custom, and material culture, AND the nuances lost in translation (telling given-names, idioms/allusions/chengyu given with the hanzi and the literal image, symbolism, honorifics, loaded keywords). Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source), state the verdict in the note, flag any source conflict, and keep the source's own errors of fact visible and footnoted. Use apparatus_merge.py (never a shell heredoc); give every new glossary row a "category" (people / organizations / places / terms), an attestation status, AND the Mandarin "pinyin" of the source hanzi (qc_entities crashes on a row with no pinyin field — even non-Chinese renderings like place names carry the source's pinyin). Watch for bare "&" in note bodies: use the numeric ref &#38; (a literal & breaks the XHTML build). First-appearance discipline with the NOT-re-noted ledger in PROGRESS.md; check notes.json BEFORE re-noting anything already covered book-wide (e.g. the Tokkō, No. 76, the Battle of Shanghai, the 88th Division, Kempeitai, Bridge House, Longhua camp, Kagoshima, Wang Jingwei, the Cathay Hotel, the ROC flag, reserve certificates, 中统/Zhongtong, shikumen, Seymour Road, cheongsam, rickshaw, Jintan, Fourth Avenue).
5. Rebuild the cumulative EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; record all check results in PROGRESS.md; keep the ORIGINAL cover (data/figs/cover00144.jpeg, reused byte-identical — commissioner's instruction); commit; push claude/the-rebel.
6. Finish with BOTH chat deliverables: the built EPUB attached, and the Batch B06 kickoff (Potassium Cyanide 1-5, units ch31-ch35, a NEW novella — read its opening cold, no cast carryover, and build fresh voice sheets) pasted VERBATIM in a fenced code block. A Stop hook enforces the pasted kickoff.

Cite chapters and sections, never pages. Do not pause for approval mid-batch; only stop for a genuine blocker or completion.
```

## What is DONE (do not redo)

- Step 0 survey: source ingested, book.json authored (51 units, four parts),
  skeleton EPUB green, batch plan approved (9 batches).
- B01 = The Rebel 1-7 (ch01-ch07), 357 paragraphs. VOICE GATE PASSED. ch01
  frozen as the register reference. 50 footnotes, Principal Characters page.
- B02 = The Rebel 8-14 (ch08-ch14), 380 paragraphs. The Rebel novella COMPLETE.
- B03 = The Postman 1-6 (ch15-ch20), 231 paragraphs. 39 footnotes, 36 glossary
  rows. All checks green; qa_epub PASS; epubcheck clean.
- B04 = The Postman 7-11 (ch21-ch25), 216 paragraphs, translated end to end.
  22 footnotes added (book total 150 -> 172), 19 glossary rows added (book
  total 124 -> 143). Every historical claim fact-checked (Wikipedia / Baidu
  Baike / USNI / academic). All checks green (parity/numbers/anchors,
  alignment, content/displacement, entity survival, register, apparatus).
  qa_epub PASS; epubcheck 5.1.0 clean (0/0/0/0). 25 of 51 chapters translated.
  Committed and pushed to claude/the-rebel.
- STYLE.md is the project prose contract.

## Tooling in place (do NOT revert)

- STYLE.md — the PROSE CONTRACT. Read it every batch before translating.
- reference/ch01.md — the FROZEN register reference. Run
  check_register.py --ref reference/ch01.md on every new unit. Do not
  regenerate or overwrite it.
- review/content_config.json — docs/sources map for ALL 51 units (untranslated
  ones skipped automatically). Run check_content.py --config
  review/content_config.json.
- data/noise.txt — project entries for non-quantitative source numerals, each
  commented. B04 added: 百顺来, 胡说八道, 四面八方, 八格, 三教九流, 伊藤近二,
  丢三落四, 成千上万, 飘零. Extend as new number idioms surface; never noise a
  real quantity.
- scripts/apparatus_merge.py files each glossary row UNDER its "category" field
  and validates note anchors as verbatim substrings of the reading text; give
  every row a category, an attestation status, AND a pinyin field.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- No source-notes stream (the source carries none; grep each new batch anyway,
  record "none present").
- batch_apparatus_b02.json, batch_apparatus_b03_glossary.json,
  batch_apparatus_b03_notes.json, batch_apparatus_b04.json are the kept
  payloads for the record; author a new batch_apparatus file per batch, never
  edit the ledgers by hand.

## Voice sheets (The Postman cast — CARRY FORWARD into B05)

The Postman (ch15-ch30) is a separate novella. Its principals, as established:
- Xu Zhongliang / 仲良 (protagonist): a postman's son, aloof and proud, bookish
  (loves English, Shelley and Byron, copperplate calligraphy). Morally
  fastidious, near-silent under pressure; his father's murder hardens him into
  a cold, brooding operative who despises the trade even as he masters it. His
  hopeless love for Su Lina is the private wound. By B04 he has taken over
  Zhou San's work under the code name Catfish (鲶鱼), lost his post-office cover,
  runs a cigarette stall, and works the church channel (Kruger). Pinyin.
- Zhou San / 周三 (his first controller): the folksy, wry post-office doorman
  and Communist veteran, killer's flat eyes under jokes. In B04 he vanishes and
  is found drowned in the Huangpu; presumed murdered. "A number-name": 周三 =
  "Zhou Three". Pinyin.
- Su Lina / 苏丽娜 (the female agent): languid, cool, fatalistic; her hatred of
  the Japanese ("not dislike, hate") the one heat she shows. Cover as Qin
  Zhaokuan's kept woman and dance-hall queen; Zhongliang is her courier. By B04
  she is a "literary bluestocking" feeding out Qin's intelligence, and by
  ch25's end is a marked woman being spirited out of Shanghai. Pinyin.
- Mr. Pan / 潘先生 (the handler): the Communist officer over the network.
  Courteous, quiet, absolute about the mission. In B04 he orders Zhongliang to
  "go to ground" after a traitor breaks the network, then disappears. Pinyin.
  NOTE: distinct from The Rebel's Old Pan.
- Xiufen / 秀芬 (Zhongliang's "woman"): the silent widow installed in his home
  by Zhou San; revealed in B04 to be a member of the anti-Japanese assassination
  squad. Cold, tearless, absolute. She kills a turncoat, then dies biting a
  cyanide wax pill in the Nanjing Road assassination of Nakamura Nobuo. DEAD as
  of ch24/ch25. Pinyin.
- Qin Zhaokuan / 秦兆宽 (the "collaborator"): suave, patient, elegant; courts
  Su Lina ("I'll wait"). B04's great reveal: he was a deep-cover Nationalist
  (中统 / Zhongtong) agent all along, feeding Su Lina his own intelligence
  knowingly. Shot in the Nakamura assassination, he dies in ch25 after arranging
  Su Lina's escape through Chen Taining. DEAD as of ch25. Pinyin.
- Father Brown / 布朗神父: the English priest of St. Thérèse's, the Far East
  intelligence contact. Interned at Bridge House after Pearl Harbor, he jumps to
  his death from the officers' bathhouse (ch23) rather than betray more. DEAD.
  布朗 = source's "Brown".
- Father Kruger / 克鲁格 (NEW, B04): the fair-haired German priest who succeeds
  Father Brown as the church channel. Eager, worldly, transactional ("I don't
  serve you for nothing"); dangles a passage to America. Alive, active. Source's
  transliteration of a German surname.
- Itō Kinji / 伊藤近二 (NEW, B04): the Japanese agent planted as postal
  inspector; twenty years in Shanghai, exiled to it for drunken defeatism, sunk
  in homesickness for Nagoya. A wry, defeated foil. Hepburn romanization.
- Chen Taining / 陈泰泞 (NEW, B04): the meek, mean-looking warehouse clerk at
  Shiliupu, secretly Qin Zhaokuan's man, charged with getting Su Lina out.
  Alive at ch25's end. Pinyin.
- Nakamura Nobuo / 仲村信夫: the Japanese intelligence officer, "Eagle of East
  Asia". Assassinated in ch24. DEAD.
- Zhou Chukang / 周楚康 (Su Lina's cover husband): NRA officer, reported still
  alive at the front with the 88th Division / 264th Brigade (ch22). Pinyin.

## Voice sheets (The Rebel cast — ARCHIVED, story complete)

Kept as the world's register calibration; do not expect them in The Postman.
Lin Nansheng (林楠笙), Gu Shenyan (顾慎言), Zhu Yizhen (朱怡贞), Miss Lan
(蓝小姐), Old Pan (老潘), Meng Annan (孟安南), Ji Zhongyuan (纪中原), Ding Mocun
(丁默邨). (Full descriptions in git history / earlier HANDOFF revisions.)

## Where the book stands (story)

- THE REBEL (novella 1) COMPLETE, ch01-ch14.
- THE POSTMAN (novella 2, ch15-ch30) through ch25: Xu Delin, a secret Communist
  courier and postman, is tortured to death by the Japanese. His proud, bookish
  son Zhongliang takes his place under the doorman-controller Zhou San, who
  trains him and installs the silent widow Xiufen in his home. Zhongliang loves
  Su Lina, a Communist agent married in cover to the patriot officer Zhou
  Chukang; ordered to ground, she becomes a dance-hall queen set to seduce the
  collaborator Qin Zhaokuan, and Zhongliang becomes her courier. THEN: after the
  New Fourth Army Incident, Xiufen is revealed as an assassination-squad member
  and kills a turncoat. Zhou San vanishes and is found drowned; Zhongliang takes
  over his work as "Catfish", the liaison to the Far East intelligence station
  through Father Brown. Pearl Harbor: the concessions are occupied, Brown is
  interned at Bridge House and jumps to his death; the German priest Kruger takes
  over the channel. A traitor breaks the network; Mr. Pan orders a freeze, then
  disappears. Zhongliang, dismissed from the post office by the Japanese agent
  Itō Kinji (warned first by his sympathetic Chinese postmaster), runs a
  cigarette stall; Su Lina feeds him a winter-pacification plan, and he reopens
  the church channel with Kruger on Kruger's transactional terms. Xiufen keeps
  the New Year early, sends Zhongliang away, and dies in the Nanjing Road
  assassination of Nakamura Nobuo, biting her cyanide pill. Qin Zhaokuan, shot in
  the same attack, is unmasked as a deep-cover Nationalist (Zhongtong) agent who
  fed Su Lina his own intelligence; dying, he arranges her escape through Chen
  Taining at Shiliupu. Su Lina, marked, refuses to leave without Zhongliang.
- Still to come in The Postman: ch26-ch29 (installments 12-15) + ch30 (the
  后记/Afterword). UNREAD.

## What is NEXT

- B05 = The Postman 12-15 + Afterword (ch26-ch30). Normal batch; ends at the B06
  kickoff. COMPLETES The Postman.
- Then B06-B07 Potassium Cyanide (ch31-ch40, a NEW novella — no cast carryover),
  B08-B09 Rouge (ch41-ch51 + back matter and whole-book QA).

## Settled renderings / carry-forward

- The Postman glossary (glossary.json, with category/status/pinyin): people —
  Xu Delin, Zhongliang (仲良), Xu-sao (徐嫂), Zhou San, Su Lina, Mr. Pan, Zhou
  Chukang, Qin Zhaokuan, Nakamura Nobuo, Xiufen, Father Brown, Father Kruger
  (克鲁格), Itō Kinji (伊藤近二), Chen Taining (陈泰泞), Mr. Harada (原田), Yu
  Hongjun, Chen Sunong, Huang Tingjian. organizations — the Dahua Trading
  Company, the 88th Division, the 264th Brigade (264旅), the anti-Japanese
  assassination squad (抗日除奸队), the Songjiang detachment, Tokyo Imperial
  University, the Wang Jingwei puppet government, the Shanghai Times. places —
  the Jing'an post office, St. Thérèse's Church, the International Funeral
  Parlor, the Siming Apartments, Hongkou, Hongkou Park (虹口公园), Fourth Avenue,
  Songjiang, Seymour Road (西摩路), Bridge House (桥楼), Kagoshima (鹿儿岛),
  Nagoya (名古屋), Shiliupu (十六铺), the Cathay Hotel (华懋饭店), the Customs
  House clock tower, Changsha, Nanjing, Wuhan. terms — the cuckoo is singing,
  queen of the dance, Jintan, Catfish (鲶鱼), reserve certificates (储备券),
  Three Castles (三炮台), the Blue Sky White Sun & Wholly Red Earth flag
  (青天白日满地红), rural pacification (清乡), shikumen (石库门), tatami (榻榻米).
- Reused shelf/earlier forms in use: Rue Ratard (巨籁达路), the Jing'an Temple
  (静安寺), Suzhou Creek, Yuyuan Road, the Paramount (百乐门), the Tokkō
  (特高课), No. 76 Jessfield Road, Wang Jingwei, The Young Companion (良友),
  cheongsam (旗袍), rickshaw (黄包车), the New Fourth Army (新四军), 中统
  Zhongtong (already in glossary; footnoted in B04), the traitor (汉奸).
- Dialogue is unmarked in the source; quote it in English. Chapter heading = the
  installment number under the part title (title_en is that number); the
  Afterword's title_en is "Afterword". One English paragraph per source line
  (parity machine-enforced; vary rhythm within the paragraph).
- COVER: keep the source's original, data/figs/cover00144.jpeg, reused
  byte-identical (commissioner's instruction). Do NOT replace.

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done every batch; expect it again). At B04 the
  stray branch was identical to origin/claude/the-rebel (no stranded work) and
  had no remote ref; deleting it locally was enough.
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch — it was empty at the start of B03 and B04).
  data/zh, out/*_en.json, out/*_reading.md, reference/ch01.md,
  review/content_config.json, data/noise.txt and the ledgers are tracked;
  bilinguals are regenerable and not shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file for the numbered
  installments (skip=2). The Afterword (ch30) may differ — inspect its head.
- B04 digitization glitches (rendered to sense, listed in PROGRESS, never
  footnoted as typos): 马牌橹子 for 马牌撸子 (ch21, the slang itself footnoted as
  texture); 她的女人 for 他的女人 (ch23); 大街大上 for 大街上 (ch23); 十六浦 for
  十六铺 Shiliupu (ch25, same glitch class as before). Watch for more.
- APPARATUS TRAPS learned in B04: (1) every glossary row needs a "pinyin" field
  or qc_entities crashes (KeyError) — even English/Japanese renderings carry the
  source hanzi's Mandarin pinyin. (2) A bare "&" in a note body (e.g. "W. D. &
  H. O. Wills") is an invalid XML token that breaks the whole notes.xhtml build;
  use the numeric ref &#38;. (3) check_content wants the FULL glossary name in
  the paired paragraph (e.g. "St. Thérèse's Church", not "St. Thérèse's"), and
  qc_entities wants the glossary "en" for 汉奸 = "traitor" to appear literally.
- The setup.sh checker suite reports one FAILURE ("hook stands down on template
  stub"); it is a FALSE failure of project state (HANDOFF carries a real
  kickoff, not the template placeholder), not a real defect. Record it and move
  on.
