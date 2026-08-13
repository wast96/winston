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
every batch is a normal batch that ends at its next-batch kickoff. B02 (the rest
of The Rebel, ch08-ch14) is done. Next is B03, the first six installments of the
second novella, The Postman.

## Message to paste into the next chat

```
The Rebel B03

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then STYLE.md (the prose contract), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, four Republican-era espionage novellas, into an annotated English EPUB. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub. Run ./setup.sh first; if data/src is empty, re-ingest with scripts/ingest_epub.py source.epub (it is gitignored and regenerable).

ch01 is FROZEN as the register reference (reference/ch01.md). This is a NORMAL batch: run it end to end and finish with the TWO chat deliverables (the built EPUB attached AND the next batch's kickoff pasted verbatim in a fenced block). Do NOT stop for a voice gate.

Do Batch B03 = The Postman installments 1-6 (units ch15 through ch20), source files data/src/18_part0016.txt .. 23_part0021.txt, per the CLAUDE.md pipeline and STYLE.md. NOTE: ch15 opens a NEW novella (邮差 / The Postman), a separate story with its own cast — The Rebel's characters do not carry over. There is NO voice seam to read back into; instead establish fresh two-line VOICE SHEETS for The Postman's principals at first appearance and write them into this HANDOFF. ch01 of The Rebel remains the frozen register reference for check_register (the register target is the same book-wide restrained third person; do not re-freeze).
1. Read ch15-ch20 from data/src/. Fix extractor-split paragraphs (a body line whose last char is not in 。！？"）…—); the source has a DOUBLED heading line per file, so make_bilingual runs with skip=2. Grep each unit for source note markers (\[\d+\]) and record "none present" in PROGRESS.md.
2. Translate to STYLE.md: literary contemporary English, restrained third person; dialogue IN QUOTATION MARKS (the source runs it unmarked), natural and contracted, grave where the weight wants it; name each character once per paragraph and let pronouns carry the rest (this satisfies qc_entities and check_content — the latter wants the FULL glossary name, not just a surname). Render idioms to natural English in the text and keep the literal image or allusion in a FOOTNOTE. Consult glossary.json and authority.json BEFORE romanizing ANY name or term; carry forward the settled renderings and voice sheets in this HANDOFF.
3. Per unit, in order: write out/<id>_en.json (one English paragraph per source body line); make_bilingual.py <id> <src> <title_en> out/<id>_en.json 2 (title_en is the installment number 1..6 per book.json); split_bilingual.py out/<id>_bilingual.md <id> "<zh title>"; then verify_unit.py (parity + numbers, it uses data/noise.txt), check_align.py, check_content.py --config review/content_config.json, qc_entities.py out/<id>_bilingual.md glossary.json, and check_register.py --ref reference/ch01.md out/<id>_reading.md. Verify each unit's TAIL against the source. Add non-quantitative numerals to data/noise.txt with a comment as they flag; NEVER noise a real quantity.
4. Footnotes per STYLE.md's apparatus doctrine — be generous, the commissioner loves them: cover history, institutions, money, geography, custom, and material culture, AND the nuances lost in translation (telling given-names, idioms/allusions/chengyu given with the hanzi and the literal image, symbolism, honorifics, loaded keywords). Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source), state the verdict in the note, flag any source conflict, and keep the source's own errors of fact visible and footnoted. Use apparatus_merge.py (never a shell heredoc); first-appearance discipline with the NOT-re-noted ledger in PROGRESS.md; new glossary rows carry a "category" (people / organizations / places / terms) and an attestation status. First-appearance discipline is BOOK-WIDE: check notes.json before re-noting anything already covered in The Rebel (e.g. the Juntong, No. 76, SACO, Wang Jingwei, the Tokko, cheongsam, rickshaw).
5. Rebuild the cumulative EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; record all check results in PROGRESS.md; keep the ORIGINAL cover (data/figs/cover00144.jpeg, reused byte-identical — commissioner's instruction); commit; push claude/the-rebel.
6. Finish with BOTH chat deliverables: the built EPUB attached, and the Batch B04 kickoff (The Postman 7-11, units ch21-ch25) pasted VERBATIM in a fenced code block. A Stop hook enforces the pasted kickoff.

Cite chapters and sections, never pages. Do not pause for approval mid-batch; only stop for a genuine blocker or completion.
```

## What is DONE (do not redo)

- Step 0 survey: source ingested, book.json authored (51 units, four parts),
  skeleton EPUB green, batch plan approved (9 batches).
- Batch B01 = The Rebel 1-7 (ch01-ch07), 357 paragraphs. VOICE GATE PASSED.
  ch01 frozen as the register reference (reference/ch01.md). 50 footnotes,
  51 glossary rows, Principal Characters page. All checks green; qa_epub PASS,
  epubcheck 5.1.0 clean.
- Batch B02 = The Rebel 8-14 (ch08-ch14), 380 paragraphs, translated end to
  end. 61 footnotes added (book total 111), 37 glossary rows added (book total
  88). Every historical claim fact-checked against Wikipedia/academic sources.
  All checks green (parity/numbers/anchors, alignment, content/displacement,
  entity survival, register, apparatus); qa_epub PASS, epubcheck 5.1.0 clean.
  The Rebel novella is now COMPLETE. Committed and pushed to claude/the-rebel.
- STYLE.md written and adopted as the project prose contract.

## Tooling in place (do NOT revert)

- STYLE.md — the project PROSE CONTRACT. Read it every batch, before
  translating. Do not delete or narrow it.
- reference/ch01.md — the FROZEN register reference. Run
  check_register.py --ref reference/ch01.md on every new unit. Do not
  regenerate or overwrite it.
- review/content_config.json — docs/sources map for ALL 51 units (untranslated
  ones skipped automatically). Run check_content.py --config
  review/content_config.json.
- data/noise.txt — project entries for non-quantitative source numerals, each
  commented. B02 added: 四下, 第二年, 十六浦, 八角厅, 礼拜[一二三四五六],
  星期[一二三四五六], 百乐门. Extend as new number idioms surface; never noise a
  real quantity.
- scripts/apparatus_merge.py — glossary rows file UNDER their "category"
  (default "terms"); give every row a category. scripts/check_content.py —
  skips non-dict / "_"-prefixed glossary sections. Keep both fixes.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- No source-notes stream (the source carries none; grep each new batch anyway).
- batch_apparatus_b02.json is the B02 apparatus payload (kept for the record);
  author a new batch_apparatus_bNN.json per batch, never edit the ledgers by
  hand.

## Voice sheets (The Rebel cast — archived; do not expect them in The Postman)

The Postman (ch15+) is a SEPARATE novella with its own cast. Write fresh voice
sheets for its principals at first appearance. The Rebel sheets below are kept
as the world's register calibration:
- Lin Nansheng (林楠笙): the Rebel's protagonist. Educated, controlled,
  near-silent under pressure; short flat sentences, hard truths stated plainly;
  dry self-directed irony; colder and blacker after his wound (cannot feel
  pain, a motif to the end). Pinyin.
- Gu Shenyan (顾慎言): Lin's spymaster. The cultivated aesthete (go, cigars,
  Baudelaire); measured aphorism and indirection, warm on the surface, testing
  underneath. His given name means "guard your words." Died in ch08. Pinyin.
- Zhu Yizhen (朱怡贞): the Communist agent, Lin's love. Proud, stubborn,
  wounded; cold formality broken by sudden fractures; silence and needlework
  carry what she won't say. Endearment 贞贞 = Zhenzhen. Pinyin.
- Miss Lan (蓝小姐): the fallen socialite-agent; brittle, fatalistic, blunt in
  speech, tender only in the dark. Dies at the Paramount (ch12). Pinyin surname.
- Old Pan (老潘): the Communist controller; wry, patient, absolute about the
  primacy of the mission over life or name. Sacrifices himself (ch12). Pinyin.
- Meng Annan (孟安南): Vietnamese-born deep-cover agent, Gu's foster son (real
  name Nguyen Chi Trung); quiet, procedural, doctrinaire; "trust is a strange
  thing." Pinyin cover name.
- Ji Zhongyuan (纪中原): Zhu's controller and cover-husband; quiet, patient,
  absolute about the work; fakes his death and returns as a public-security
  cadre. Pinyin.
- Ding Mocun (丁默邨): the historical turncoat, director of No. 76. Historical;
  pinyin.

## Where the book stands (story)

- THE REBEL (novella 1) COMPLETE, ch01-ch14. After the Hong Kong hospital
  (B01), Lin is recalled to Chongqing to instruct at SACO. B02: he is set to
  watch his old teacher Gu Shenyan under house arrest; Gu, protector of hidden
  agents and of Ho Chi Minh, poisons himself rather than be broken, leaving Lin
  the go-manual cipher. Lin takes in the ruined agent Miss Lan; after victory he
  returns to occupied-then-liberated Shanghai, rises in the Baomiju, and finds
  Zhu Yizhen alive (married in cover to Meng Annan). The controller Old Pan lets
  himself be "turned" and killed to pass Lin into the Communist net; Miss Lan
  dies covering the hit and Lin's own assassination of Old Pan. Lin passes the
  Liaoshen/Changchun battle plan through Zhu, learns Meng is Gu's foster son,
  and is nearly killed crossing the lines. He hides as a village schoolteacher
  (alias Lin Qiuming, his dead friend Zuo Qiuming's name) until Ji Zhongyuan,
  now a public-security officer, brings him back. Dying and numb, Lin is reunited
  at his deathbed with Zhu Yizhen: "Still — I got to see you after all."
- THE POSTMAN (novella 2, ch15-ch30) is NEXT and UNREAD. New cast, same world
  of Republican/wartime Shanghai espionage. ch30 is a short 后记/afterword coda.

## What is NEXT

- B03 = The Postman 1-6 (ch15-ch20). Normal batch; ends at the B04 kickoff.
- Then B04 The Postman 7-11 (ch21-ch25), B05 The Postman 12-15 + Afterword
  (ch26-ch30), B06-B07 Potassium Cyanide (ch31-ch40), B08-B09 Rouge
  (ch41-ch51 + back matter and whole-book QA). Nine batches total; three done
  after B02 counts B01+B02 (B01 done, B02 done).

## Settled renderings / carry-forward

- Cross-shelf (authority.json) forms in use: Wang Jingwei, Dai Li, the Juntong,
  the Cathay Hotel, Avenue Joffre, Suzhou Creek, Yuyuan Road, Nanjing Road,
  rickshaw, cheongsam, Chongqing. From B01: Ding Mocun, No. 76 / Jessfield Road,
  the Zhongtong, the Peace Army, SACO, the Tokko, Rue Ratard, the Zhonghua Ribao,
  The Young Companion, Ta Kung Pao, the Central Reserve Bank, the Red House
  (红房子, NOT "Chez Louis").
- New this batch (glossary.json): Ho Chi Minh, the Baomiju (postwar Juntong),
  the Loyal and Patriotic Army, the Lixingshe, the Central Bank (Nationalist,
  distinct from the Central Reserve Bank), the East China Bureau, the Nineteenth
  Route Army, the Chinese Youth Communist Party in Europe, the Third Field Army,
  the Volunteer Army, Mount Gele, the Jialing River, Yan'an, Xietang, the Jing'an
  Temple, Zhaofeng Park (= Jessfield Park), the Paramount Ballroom, the Dangui
  Theater, Xibaipo, Avenue Foch, the Metropol Theater, the Wangyou Qingle Ji,
  汉奸 (traitor/collaborator), and the full B02 cast.
- Dialogue is unmarked in the source; quote it in English. Chapter heading =
  the installment number under the part title (title_en is that number). One
  English paragraph per source line (parity machine-enforced; vary rhythm
  within the paragraph).
- COVER: keep the source's original, data/figs/cover00144.jpeg, reused
  byte-identical (commissioner's instruction; md5 84b0d189...). Do NOT replace.

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done every batch; expect it again).
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch — it was empty at the start of B02). data/zh,
  out/*_en.json, out/*_reading.md, reference/ch01.md, review/content_config.json
  and the ledgers are tracked; bilinguals are regenerable and not shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file (skip=2). One
  digitization glitch in B02: 十六浦 for 十六铺 (Shiliupu docks, ch10), rendered
  to sense and noised. Watch for more in The Postman.
- The setup.sh checker suite reports one FAILURE ("hook stands down on template
  stub"); it is a FALSE failure of project state (HANDOFF carries a real
  kickoff, not the template placeholder), not a real defect. Record it and move
  on.
