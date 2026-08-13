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
ch15-ch20) is done. Next is B04, The Postman installments 7-11 (ch21-ch25).

## Message to paste into the next chat

```
The Rebel B04

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then STYLE.md (the prose contract), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, four Republican-era espionage novellas, into an annotated English EPUB. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub. Run ./setup.sh first; if data/src is empty, re-ingest with scripts/ingest_epub.py source.epub (it is gitignored and regenerable).

ch01 is FROZEN as the register reference (reference/ch01.md). This is a NORMAL batch: run it end to end and finish with the TWO chat deliverables (the built EPUB attached AND the next batch's kickoff pasted verbatim in a fenced block). Do NOT stop for a voice gate.

Do Batch B04 = The Postman installments 7-11 (units ch21 through ch25), source files data/src/24_part0022.txt .. 28_part0026.txt, per the CLAUDE.md pipeline and STYLE.md. This continues The Postman (邮差), the SAME novella and cast as B03 (ch15-ch20): its story and characters DO carry over now. Read the final two pages of ch20's English (out/ch20_reading.md) before you start, to catch the voice seam. The Postman voice sheets and settled renderings are in this HANDOFF; consult them. ch01 of The Rebel remains the frozen register reference for check_register (do not re-freeze).
1. Read ch21-ch25 from data/src/. Fix extractor-split paragraphs (a body line whose last char is not in 。！？"）…—); the source has a DOUBLED heading line per file, so make_bilingual runs with skip=2. Grep each unit for source note markers (\[\d+\]) and record "none present" in PROGRESS.md (the source has carried none so far; grep anyway).
2. Translate to STYLE.md: literary contemporary English, restrained third person; dialogue IN QUOTATION MARKS (the source runs it unmarked), natural and contracted, grave where the weight wants it; name each character once per paragraph and let pronouns carry the rest (this satisfies qc_entities and check_content — the latter wants the FULL glossary name). Consult glossary.json and authority.json BEFORE romanizing ANY name or term; carry forward the settled renderings and voice sheets in this HANDOFF.
3. Per unit, in order: write out/<id>_en.json (one English paragraph per source body line); make_bilingual.py <id> <src> <title_en> out/<id>_en.json 2 (title_en is the installment number 7..11 per book.json); split_bilingual.py out/<id>_bilingual.md <id> "<zh title>"; then verify_unit.py (parity + numbers, it uses data/noise.txt), check_align.py <id>, check_content.py --config review/content_config.json, qc_entities.py out/<id>_bilingual.md glossary.json, and check_register.py --ref reference/ch01.md out/<id>_reading.md. Verify each unit's TAIL against the source. Add non-quantitative numerals to data/noise.txt with a comment as they flag; NEVER noise a real quantity.
4. Footnotes per STYLE.md's apparatus doctrine — be generous, the commissioner loves them: cover history, institutions, money, geography, custom, and material culture, AND the nuances lost in translation (telling given-names, idioms/allusions/chengyu given with the hanzi and the literal image, symbolism, honorifics, loaded keywords). Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source), state the verdict in the note, flag any source conflict, and keep the source's own errors of fact visible and footnoted. Use apparatus_merge.py (never a shell heredoc); first-appearance discipline with the NOT-re-noted ledger in PROGRESS.md; new glossary rows carry a "category" (people / organizations / places / terms) and an attestation status. First-appearance discipline is BOOK-WIDE: check notes.json before re-noting anything already covered (e.g. the Tokkō, No. 76, the Battle of Shanghai, the 88th Division, Kempeitai, Wang Jingwei, the Paramount, Siming Apartments, Rue Ratard, cheongsam, rickshaw, Jintan, Fourth Avenue).
5. Rebuild the cumulative EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; record all check results in PROGRESS.md; keep the ORIGINAL cover (data/figs/cover00144.jpeg, reused byte-identical — commissioner's instruction); commit; push claude/the-rebel.
6. Finish with BOTH chat deliverables: the built EPUB attached, and the Batch B05 kickoff (The Postman 12-15 + Afterword, units ch26-ch30) pasted VERBATIM in a fenced code block. A Stop hook enforces the pasted kickoff.

Cite chapters and sections, never pages. Do not pause for approval mid-batch; only stop for a genuine blocker or completion.
```

## What is DONE (do not redo)

- Step 0 survey: source ingested, book.json authored (51 units, four parts),
  skeleton EPUB green, batch plan approved (9 batches).
- B01 = The Rebel 1-7 (ch01-ch07), 357 paragraphs. VOICE GATE PASSED. ch01
  frozen as the register reference. 50 footnotes, Principal Characters page.
- B02 = The Rebel 8-14 (ch08-ch14), 380 paragraphs. The Rebel novella COMPLETE.
- B03 = The Postman 1-6 (ch15-ch20), 231 paragraphs, translated end to end.
  39 footnotes added (book total 111 -> 150), 36 glossary rows added (book total
  88 -> 124). Every historical claim fact-checked (Wikipedia / Baidu Baike /
  academic). All checks green (parity/numbers/anchors, alignment, content/
  displacement, entity survival, register, apparatus). qa_epub PASS; epubcheck
  5.1.0 clean (0/0/0/0). 20 of 51 chapters translated. Committed and pushed to
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
  commented. B03 added: 十字架, 十字, 周三, 万国, 四明, 百无聊赖, 四散, 两盅,
  两手, 两人. Extend as new number idioms surface; never noise a real quantity.
- scripts/apparatus_merge.py files each glossary row UNDER its "category" field;
  give every row a category. Anchors are validated as verbatim substrings of the
  reading text at merge time.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- No source-notes stream (the source carries none; grep each new batch anyway,
  record "none present").
- batch_apparatus_b02.json, batch_apparatus_b03_glossary.json,
  batch_apparatus_b03_notes.json are the kept payloads for the record; author a
  new batch_apparatus file per batch, never edit the ledgers by hand.

## Voice sheets (The Postman cast — CARRY FORWARD into B04+)

The Postman (ch15+) is a separate novella. Its principals, written at first
appearance:
- Xu Zhongliang / 仲良 (protagonist): a postman's son, aloof and proud, bookish
  (loves English, Shelley and Byron, copperplate calligraphy). Morally
  fastidious, near-silent under pressure; his father's murder hardens him into a
  cold, brooding operative who despises the trade even as he masters it. His
  hopeless love for Su Lina is the private wound. Pinyin.
- Zhou San / 周三 (his controller): doorman of the Jing'an post office, a
  Communist veteran. Folksy, wry, patient, hiding a killer's flat dead eyes and
  absolute discipline under jokes about dreams, lottery tickets, and chess
  (xiangqi). Teacher of tradecraft; "wherever you stand, you have to look like
  you belong there." Pinyin. (A "number-name": 周三 = "Zhou Three".)
- Su Lina / 苏丽娜 (the female agent): married in cover to an army officer, then
  a dance-hall queen sent to seduce the collaborator Qin Zhaokuan. Languid,
  cool, fatalistic; masks grief and resentment under indifference; her hatred of
  the Japanese ("not dislike, hate") is the one heat she shows. Pinyin.
- Mr. Pan / 潘先生 (the handler): the Communist officer over Zhou San and Su
  Lina. Courteous, quiet, absolute about the mission over the person ("first of
  all you are a soldier"). Pinyin. NOTE: distinct from The Rebel's Old Pan.
- Xu-sao / 徐嫂 (the mother): Xu Delin's widow. Endures for her son, then leaves
  to remarry; bitter, hard, controlled, tearless. Address-form 嫂 kept. Pinyin.
- Qin Zhaokuan / 秦兆宽 (the target): collaborator, Dahua Trading manager, Wang
  regime liaison, frequenter of No. 76. Suave, patient, elegant (cigars), coolly
  persistent in courting Su Lina; "I'll wait." Pinyin.
- Zhou Chukang / 周楚康 (Su Lina's husband): NRA lieutenant colonel, ardent
  patriot, goes to the 88th Division at the front. Passionate, doomed. Pinyin.
- Xiufen / 秀芬: widow of a killed guerrilla commissar, brought to keep house for
  Zhongliang; silent, cold, a body "cold as a corpse". Pinyin.
- Father Brown / 布朗神父: the English priest of St. Thérèse's, thirty years in
  China, speaks Tianjin dialect not Wu; kind, blunt. 布朗 = source's "Brown".

## Voice sheets (The Rebel cast — ARCHIVED, story complete)

Kept as the world's register calibration; do not expect them in The Postman.
Lin Nansheng (林楠笙), Gu Shenyan (顾慎言), Zhu Yizhen (朱怡贞), Miss Lan
(蓝小姐), Old Pan (老潘), Meng Annan (孟安南), Ji Zhongyuan (纪中原), Ding Mocun
(丁默邨). (Full descriptions in git history / earlier HANDOFF revisions.)

## Where the book stands (story)

- THE REBEL (novella 1) COMPLETE, ch01-ch14.
- THE POSTMAN (novella 2, ch15-ch30) in progress. Through ch20: In 1930s
  Shanghai the postman Xu Delin, a secret Communist courier, is tortured to
  death by the Japanese and dies rather than talk. His proud, bookish son
  Zhongliang, refusing his mother's plan to make him a bamboo-weaver, takes his
  father's place under the post-office doorman and controller Zhou San, who
  trains him in tradecraft. Zhongliang falls hopelessly in love with Su Lina, a
  Communist agent married in cover to the patriot officer Zhou Chukang (who goes
  to the front with the 88th Division and is lost). Ordered to "go to ground,"
  Su Lina becomes a dance-hall queen and, on the handler Mr. Pan's orders, is
  set to seduce the collaborator Qin Zhaokuan, general manager of the Dahua
  Trading Company and a Japanese liaison. Zhongliang becomes her courier;
  Qin proposes marriage ("I'll wait"). Meanwhile Zhou San has installed the
  silent widow Xiufen in Zhongliang's home as his "woman".
- Still to come in The Postman: ch21-ch29 (installments 7-15) + ch30 (a short
  后记/afterword coda). UNREAD.

## What is NEXT

- B04 = The Postman 7-11 (ch21-ch25). Normal batch; ends at the B05 kickoff.
- Then B05 The Postman 12-15 + Afterword (ch26-ch30), B06-B07 Potassium Cyanide
  (ch31-ch40), B08-B09 Rouge (ch41-ch51 + back matter and whole-book QA).

## Settled renderings / carry-forward

- The Postman glossary rows (glossary.json, category/status): people — Xu Delin,
  Zhongliang (仲良), Xu-sao (徐嫂), Zhou San, Su Lina, Mr. Pan, Zhou Chukang,
  Qin Zhaokuan, Nakamura Nobuo, Xiufen, Father Brown, Yu Hongjun (attested;
  source 俞鸿均 -> attested 俞鸿钧), Chen Sunong (attested), Huang Tingjian
  (attested). organizations — the Dahua Trading Company, the 88th Division, the
  Songjiang detachment (provisional), Tokyo Imperial University, the Wang Jingwei
  puppet government, the Shanghai Times. places — the Jing'an post office, St.
  Thérèse's Church, the International Funeral Parlor, the Siming Apartments,
  Hongkou, Fourth Avenue (= Sima Road / Fuzhou Road), Songjiang, the East Asia
  Hotel (provisional), the Taishun tea shop (provisional), the Customs House
  clock tower, Changsha, Nanjing, Wuhan. terms — the cuckoo is singing (code
  signal), queen of the dance (舞林皇后), Jintan (人丹).
- Reused shelf/earlier forms in use: Rue Ratard (巨籁达路), the Jing'an Temple
  (静安寺), Suzhou Creek, Yuyuan Road, the Paramount (百乐门), the Tokkō
  (特高课), No. 76 Jessfield Road, Wang Jingwei, The Young Companion (良友),
  cheongsam (旗袍), rickshaw (黄包车).
- Dialogue is unmarked in the source; quote it in English. Chapter heading = the
  installment number under the part title (title_en is that number). One English
  paragraph per source line (parity machine-enforced; vary rhythm within the
  paragraph).
- COVER: keep the source's original, data/figs/cover00144.jpeg, reused
  byte-identical (commissioner's instruction). Do NOT replace.

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done every batch; expect it again).
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch — it was empty at the start of B03). data/zh,
  out/*_en.json, out/*_reading.md, reference/ch01.md, review/content_config.json,
  data/noise.txt and the ledgers are tracked; bilinguals are regenerable and not
  shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file (skip=2).
- B03 digitization glitches (rendered to sense, listed in PROGRESS, never
  footnoted as typos): 飞住 for 飞往 (ch17); 巨籁路 short variant of 巨籁达路
  (ch18); 十六浦 for 十六铺 Shiliupu (ch16, same as B02). Plus one real name
  mis-keyed: 俞鸿均 for 俞鸿钧 Yu Hongjun (ch17), corrected to the attested form
  and the correction recorded in the footnote. Watch for more in The Postman.
- The setup.sh checker suite reports one FAILURE ("hook stands down on template
  stub"); it is a FALSE failure of project state (HANDOFF carries a real
  kickoff, not the template placeholder), not a real defect. Record it and move
  on.
