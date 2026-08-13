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
(ch01-ch14) is complete. **The Postman (ch15-ch30) is now COMPLETE** through
B03/B04/B05. Next is B06, the FIRST batch of a NEW novella, Potassium Cyanide
(氰化钾), installments 1-5 (ch31-ch35): a fresh story with a fresh cast, no
carryover from The Postman.

## Message to paste into the next chat

```
The Rebel B06

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then STYLE.md (the prose contract), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, four Republican-era espionage novellas, into an annotated English EPUB. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub. Run ./setup.sh first; if data/src is empty, re-ingest with scripts/ingest_epub.py source.epub (it is gitignored and regenerable).

ch01 is FROZEN as the register reference (reference/ch01.md). This is a NORMAL batch: run it end to end and finish with the TWO chat deliverables (the built EPUB attached AND the next batch's kickoff pasted verbatim in a fenced block). Do NOT stop for a voice gate.

Do Batch B06 = Potassium Cyanide (氰化钾) installments 1-5 (units ch31 through ch35), source files data/src/34_part0032.txt .. 38_part0036.txt, per the CLAUDE.md pipeline and STYLE.md. This BEGINS a NEW, THIRD novella: read its opening COLD. There is NO cast carryover from The Rebel or The Postman, so build FRESH voice sheets for its characters as they appear (write each into HANDOFF's carry-forward section at first appearance, two lines: educated or rough, terse or windy, tics, formality toward whom). The story opens with the arrest of one 姜泳男 (Jiang Yongnan) and is set partly in wartime Chongqing (the Chongqing local court's execution ground, a Japanese "中原" command HQ, a bar called "White Night", one 杨群/Yang Qun at a 保安处 security bureau). Consult glossary.json and authority.json BEFORE romanizing ANY name or term; several place/institution renderings from The Rebel (Chongqing, Mount Gele, the Jialing River, the Juntong, etc.) are already settled there. ch01 of The Rebel remains the frozen register reference for check_register (do not re-freeze).
1. Read ch31-ch35 from data/src/. Fix extractor-split paragraphs (a body line whose last char is not in 。！？"）…—). Each of ch31-ch35 has a DOUBLED heading line per file (confirmed at ingest), so make_bilingual runs with skip=2; INSPECT each head with `sed -n '1,3p'` before trusting it. Grep each unit for source note markers (\[\d+\]) and record "none present" in PROGRESS.md (the source has carried none through the whole book so far; grep anyway).
2. Translate to STYLE.md: literary contemporary English, restrained third person; dialogue IN QUOTATION MARKS (the source runs it unmarked), natural and contracted, grave where the weight wants it; name each character once per paragraph and let pronouns carry the rest (this satisfies qc_entities and check_content — the latter wants the FULL glossary name as a substring of the paired paragraph). Consult glossary.json and authority.json BEFORE romanizing ANY name or term.
3. Per unit, in order: write out/<id>_en.json (one English paragraph per source body line); make_bilingual.py <id> <src> <title_en> out/<id>_en.json <skip> (title_en is the installment number 1..5 per book.json for ch31-ch35; skip is 2); split_bilingual.py out/<id>_bilingual.md <id> "<zh title>"; then verify_unit.py (parity + numbers, it uses data/noise.txt), check_align.py <id>, check_content.py --config review/content_config.json, qc_entities.py out/<id>_bilingual.md glossary.json, and check_register.py --ref reference/ch01.md out/<id>_reading.md. Verify each unit's TAIL against the source. Add non-quantitative numerals to data/noise.txt with a comment as they flag; NEVER noise a real quantity.
4. Footnotes per STYLE.md's apparatus doctrine — be generous, the commissioner loves them: cover history, institutions, money, geography, custom, and material culture, AND the nuances lost in translation (telling given-names, idioms/allusions/chengyu given with the hanzi and the literal image, symbolism, honorifics, loaded keywords). Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source), state the verdict in the note, flag any source conflict, and keep the source's own errors of fact visible and footnoted. Use apparatus_merge.py (never a shell heredoc); give every new glossary row a "category" (people / organizations / places / terms), an attestation status, AND the Mandarin "pinyin" of the source hanzi (qc_entities crashes on a row with no pinyin field). Watch for bare "&" in note bodies: use the numeric ref &#38; (a literal & breaks the XHTML build); and beware substring collisions when adding a short glossary rendering (a new key that is a substring of an existing key, or vice versa, can retro-flag an earlier chapter in check_content — pick distinct renderings or skip the row). First-appearance discipline with the NOT-re-noted ledger in PROGRESS.md; check notes.json BEFORE re-noting anything already covered book-wide (e.g. Chongqing, the Juntong, Mount Gele, Dai Li, the Whampoa Academy, the Tokkō, No. 76, Wang Jingwei, the Battle of Shanghai, reserve certificates, the silver dollar/大洋, shikumen, cheongsam, rickshaw, Jintan).
5. Rebuild the cumulative EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; record all check results in PROGRESS.md; keep the ORIGINAL cover (data/figs/cover00144.jpeg, reused byte-identical — commissioner's instruction); commit; push claude/the-rebel.
6. Finish with BOTH chat deliverables: the built EPUB attached, and the Batch B07 kickoff (Potassium Cyanide 6-10, units ch36-ch40, completes 氰化钾) pasted VERBATIM in a fenced code block. A Stop hook enforces the pasted kickoff.

Cite chapters and sections, never pages. Do not pause for approval mid-batch; only stop for a genuine blocker or completion.
```

## What is DONE (do not redo)

- Step 0 survey: source ingested, book.json authored (51 units, four parts),
  skeleton EPUB green, batch plan approved (9 batches).
- B01 = The Rebel 1-7 (ch01-ch07), 357 paragraphs. VOICE GATE PASSED. ch01
  frozen as the register reference. Principal Characters page.
- B02 = The Rebel 8-14 (ch08-ch14), 380 paragraphs. The Rebel novella COMPLETE.
- B03 = The Postman 1-6 (ch15-ch20), 231 paragraphs. 39 footnotes.
- B04 = The Postman 7-11 (ch21-ch25), 216 paragraphs. 22 footnotes.
- B05 = The Postman 12-15 + Afterword (ch26-ch30), 231 paragraphs. **The Postman
  novella COMPLETE (ch15-ch30).** 30 footnotes added (book total 172 -> 202),
  13 glossary rows added (book total 143 -> 156). Every historical claim
  fact-checked (Wikipedia / Britannica / Baidu Baike / zdic / academic). All
  checks green (parity/numbers/anchors, alignment, content/displacement, entity
  survival, apparatus); register within tolerance for ch26-ch29, ch30 Afterword
  off-reference as EXPECTED (exempt authorial register). qa_epub PASS; epubcheck
  5.1.0 clean (0/0/0/0). 30 of 51 chapters translated. Committed and pushed to
  claude/the-rebel.
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
  commented. B05 added: 四乡八里, 四个字, 二话没说, 老百姓. Extend as new number
  idioms surface; never noise a real quantity.
- scripts/apparatus_merge.py files each glossary row UNDER its "category" field
  and validates note anchors as verbatim substrings of the reading text; give
  every row a category, an attestation status, AND a pinyin field.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- No source-notes stream (the source carries none; grep each new batch anyway,
  record "none present").
- batch_apparatus_b02.json, ..._b03_*.json, ..._b04.json, ..._b05.json are the
  kept payloads for the record; author a new batch_apparatus file per batch,
  never edit the ledgers by hand.

## Voice sheets — NEW NOVELLA next (Potassium Cyanide, ch31-ch40)

B06 opens a fresh, third novella (氰化钾, Potassium Cyanide). NONE of the casts
below carry into it. Read its opening cold and build new voice sheets as its
characters appear (Jiang Yongnan / 姜泳男, Yang Qun / 杨群, and others), writing
each into this section at first appearance.

## Voice sheets (The Postman cast — ARCHIVED, novella COMPLETE)

Kept as register calibration; do NOT expect them in Potassium Cyanide.
Xu Zhongliang / 仲良 (protagonist: a postman's son, bookish, proud, cold under
pressure; loved Su Lina; died an old man at Xietang). Zhou San / 周三 (folksy
Communist controller, drowned). Su Lina / 苏丽娜 (languid, fatalistic agent;
cover wife, dance-hall queen; broke under torture, cleared no name, died in the
Cultural Revolution). Mr. Pan / 潘先生 = Yang Fugang / 杨复纲 (the handler,
killed 1942). Xiufen / 秀芬 (assassination-squad widow, died biting cyanide).
Qin Zhaokuan / 秦兆宽 (deep-cover Nationalist, died arranging Su Lina's escape).
Father Brown / 布朗神父 and Father Kruger / 克鲁格 (the church channel). Itō
Kinji / 伊藤近二 = You Kechang / 尤可常 (Japanese agent, survived as doorman).
Chen Taining / 陈泰泞 (Qin's man; later spared Su Lina). Zhou Chukang / 周楚康
(Su Lina's cover husband; PLA deputy division commander, died in Korea).
Section Chief Chen / 陈科长 (postwar public-security interrogator).

## Voice sheets (The Rebel cast — ARCHIVED, novella complete)

Lin Nansheng (林楠笙), Gu Shenyan (顾慎言), Zhu Yizhen (朱怡贞), Miss Lan
(蓝小姐), Old Pan (老潘), Meng Annan (孟安南), Ji Zhongyuan (纪中原), Ding Mocun
(丁默邨). (Full descriptions in git history / earlier HANDOFF revisions.)

## Where the book stands (story)

- THE REBEL (novella 1) COMPLETE, ch01-ch14.
- THE POSTMAN (novella 2) COMPLETE, ch15-ch30. Xu Delin, a Communist courier and
  postman, is tortured to death by the Japanese; his proud, bookish son
  Zhongliang takes his place under the doorman Zhou San, loves the agent Su Lina,
  and works the church channel as "Catfish." Xiufen (the widow installed in his
  home) dies in the Nanjing Road assassination of Nakamura Nobuo; Qin Zhaokuan,
  unmasked as a deep-cover Nationalist, dies arranging Su Lina's escape. In B05:
  Su Lina and Zhongliang flee upriver and marry in his mother's town of Xietang
  (his mother Xu-sao and the old bamboo-worker die in the fire that destroys the
  town in the civil war); they return to Shanghai; the city is liberated (1949).
  Su Lina is seized by Chen Taining, tortured, condemned, spared by him at the
  last, and released only after months, her name unclearable. Zhongliang's
  letters to Pan Hannian, Chen Yi, and Luo Ruiqing go unanswered. Zhou Chukang
  returns once, a PLA deputy division commander, and later dies in Korea. In the
  Afterword: twenty years on (the Cultural Revolution) Su Lina, head shaved,
  drowns in Suzhou Creek; another ten years and Zhongliang retires, buries her
  ashes at Xietang, and each Qingming burns her a letter in fly's-head script.
- NEXT: POTASSIUM CYANIDE (novella 3, ch31-ch40), then ROUGE (novella 4,
  ch41-ch51 + back matter and whole-book QA). Both UNREAD.

## What is NEXT

- B06 = Potassium Cyanide 1-5 (ch31-ch35). NEW novella, fresh cast, read cold;
  normal batch; ends at the B07 kickoff.
- Then B07 Potassium Cyanide 6-10 (ch36-ch40, completes 氰化钾), B08-B09 Rouge
  (ch41-ch51 + back matter and whole-book QA).

## Settled renderings / carry-forward

- The Postman glossary (glossary.json, with category/status/pinyin) is complete
  for that novella. B05 additions of book-wide use going forward: Pan Hannian
  (潘汉年), Chen Yi (陈毅), Luo Ruiqing (罗瑞卿), the Fourth Field Army (四野),
  the silver dollar (大洋/银元, footnoted ch26), the Waibaidu / Garden Bridge,
  Tilanqiao Prison / Ward Road Gaol, shilin cloth (士林布, Indanthrene).
- Reused shelf/earlier forms still in force (many relevant to a Chongqing-set
  novella): Chongqing (重庆), Mount Gele (歌乐山), the Jialing River (嘉陵江),
  the Juntong (军统), the Zhongtong (中统), Dai Li (戴笠), the Whampoa Military
  Academy, the Blue Shirts (蓝衣社) / Lixingshe (力行社), the Loyal and Patriotic
  Army (忠义救国军), the Baomiju (保密局), the Sino-American Cooperative
  Organization (中美合作所), the Tokkō (特高课), No. 76, Wang Jingwei, reserve
  certificates (储备券), shikumen (石库门), cheongsam (旗袍), rickshaw (黄包车),
  Jintan (人丹), the traitor (汉奸).
- Dialogue is unmarked in the source; quote it in English. Chapter heading = the
  installment number under the part title (title_en is that number). One English
  paragraph per source line (parity machine-enforced; vary rhythm within the
  paragraph).
- COVER: keep the source's original, data/figs/cover00144.jpeg, reused
  byte-identical (commissioner's instruction). Do NOT replace.

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done every batch; expect it again). At B05 the
  stray (claude/the-rebel-b05-11mrk0) was identical to origin/claude/the-rebel
  with no stranded commits; deleted after push.
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch — it was empty at the start of B03/B04/B05).
  data/zh, out/*_en.json, out/*_reading.md, reference/ch01.md,
  review/content_config.json, data/noise.txt and the ledgers are tracked;
  bilinguals are regenerable and not shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file (skip=2) for the
  numbered installments — including the 后记/Afterword (ch30) and, confirmed at
  ingest, ch31-ch35. Still, INSPECT each head with sed before trusting skip.
- B05 saw NO digitization glitches (ch26-ch30 clean).
- APPARATUS TRAPS (still live): (1) every glossary row needs a "pinyin" field or
  qc_entities crashes. (2) a bare "&" in a note body breaks notes.xhtml; use
  &#38;. (3) check_content and qc_entities want the FULL glossary "en" as a
  substring of the paired English paragraph. (4) NEW in B05 — a short glossary
  rendering that is a SUBSTRING of an existing key (or vice versa) will
  retro-flag an EARLIER chapter in check_content: a 布谷鸟 -> "Cuckoo" row
  collided with the existing signal 布谷鸟在歌唱 and flagged ch20; dropped it.
  When adding a row, grep built chapters for the hanzi and pick a distinct
  rendering, or skip the row and footnote instead.
- The setup.sh checker suite reports one FAILURE ("hook stands down on template
  stub"); it is a FALSE failure of project state (HANDOFF carries a real
  kickoff, not the template placeholder), not a real defect. Record it and move
  on.
