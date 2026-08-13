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
(ch01-ch14) and The Postman (ch15-ch30) are COMPLETE. **Potassium Cyanide
(氰化钾) is now under way: B06 translated installments 1-5 (ch31-ch35).** Next
is B07, which completes the novella with installments 6-10 (ch36-ch40).

## Message to paste into the next chat

```
The Rebel B07

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then STYLE.md (the prose contract), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, four Republican-era espionage novellas, into an annotated English EPUB. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub. Run ./setup.sh first; if data/src is empty, re-ingest with scripts/ingest_epub.py source.epub (it is gitignored and regenerable).

ch01 is FROZEN as the register reference (reference/ch01.md). This is a NORMAL batch: run it end to end and finish with the TWO chat deliverables (the built EPUB attached AND the next batch's kickoff pasted verbatim in a fenced block). Do NOT stop for a voice gate.

Do Batch B07 = Potassium Cyanide (氰化钾) installments 6-10 (units ch36 through ch40), source files data/src/39_part0037.txt .. 43_part0041.txt, per the CLAUDE.md pipeline and STYLE.md. This COMPLETES the third novella (氰化钾, ch31-ch40). It CONTINUES from B06: the cast and voice sheets are in HANDOFF (Jiang Yongnan / 姜泳男, Tang Ya / 唐雅, Yang Qun / 杨群, Guo Bingyan / 郭炳炎, the Korean priest, Mr. Qi / 祁先生, Old Jin / 老金). Read the final two pages of out/ch35_reading.md before you start (the HANDOFF describes the voice; the pages ARE it). B06 ended on a cliffhanger: Tang Ya, taken back overnight by Yang Qun, comes to a teahouse expecting Jiang and finds Guo Bingyan instead, who says "I am the one who gave the order to have you silenced." From the ch36-ch40 heads: ch36 Jiang slips back through occupied Hankou disguised as a Japanese returnee; ch37 a Jiangxi "youth-cadre" (青干班) training camp at Liyuan village near Ganzhou; ch38 Jiang returns to Chongqing after the victory and is received by the Generalissimo as a representative of the Youth Army's 207th Division; ch39 Tang Ya finds Yang Qun's corpse in the Central Hospital morgue; ch40 (short, 588 chars) the 5 May 1946 "return to the capital" ceremony at the Sun Yat-sen Mausoleum in Nanjing, with Guo at Qixia Temple. Consult glossary.json and authority.json BEFORE romanizing ANY name or term; the Potassium Cyanide cast and its Chongqing/Wuhan places are already settled there from B06 (Jiang Yongnan, Tang Ya, Yang Qun, Guo Bingyan, Hankou, Wuchang, the Zhongyuan Command, the Central Police Academy, etc.). ch01 of The Rebel remains the frozen register reference for check_register (do not re-freeze).
1. Read ch36-ch40 from data/src/. Fix extractor-split paragraphs (a body line whose last char is not in 。！？"）…—). Each of ch36-ch40 has a DOUBLED heading line per file (confirmed at ingest), so make_bilingual runs with skip=2; INSPECT each head with `sed -n '1,3p'` before trusting it. Grep each unit for source note markers (\[\d+\]) and record "none present" in PROGRESS.md (the source has carried none through the whole book so far; grep anyway).
2. Translate to STYLE.md: literary contemporary English, restrained third person; dialogue IN QUOTATION MARKS (the source runs it unmarked), natural and contracted, grave where the weight wants it; name each character once per paragraph and let pronouns carry the rest (this satisfies qc_entities and check_content — the latter wants the FULL glossary name as a substring of the paired paragraph). Consult glossary.json and authority.json BEFORE romanizing ANY name or term.
3. Per unit, in order: write out/<id>_en.json (one English paragraph per source body line); make_bilingual.py <id> <src> <title_en> out/<id>_en.json <skip> (title_en is the installment number 6..10 per book.json for ch36-ch40; skip is 2); split_bilingual.py out/<id>_bilingual.md <id> "<zh title>"; then verify_unit.py (parity + numbers, it uses data/noise.txt), check_align.py <id>, check_content.py --config review/content_config.json, qc_entities.py out/<id>_bilingual.md glossary.json, and check_register.py --ref reference/ch01.md out/<id>_reading.md. Verify each unit's TAIL against the source. Add non-quantitative numerals to data/noise.txt with a comment as they flag; NEVER noise a real quantity (dates like 1946年5月5日 and the 207 in 第207师 are real and stay in the English).
4. Footnotes per STYLE.md's apparatus doctrine — be generous, the commissioner loves them: cover history, institutions, money, geography, custom, and material culture, AND the nuances lost in translation (telling given-names, idioms/allusions/chengyu given with the hanzi and the literal image, symbolism, honorifics, loaded keywords). Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source), state the verdict in the note, flag any source conflict, and keep the source's own errors of fact visible and footnoted. Likely new note candidates: the 膏药旗 (Rising-Sun / "plaster flag"), the 三八式 (Type 38 Arisaka rifle), the 青干班 / Youth-Cadre training and 世外桃源 (the Peach-Blossom-Spring allusion), 青年军 the Youth Army and its 207th Division, 委员长 the Generalissimo (Chiang Kai-shek), 军委会 the Military Affairs Commission, the 1946 还都 return of the capital to Nanjing and the 中山陵 Sun Yat-sen Mausoleum, 栖霞寺 Qixia Temple, 沙弥 (novice monk). Use apparatus_merge.py (never a shell heredoc); give every new glossary row a "category" (people / organizations / places / terms), an attestation status, AND the Mandarin "pinyin" of the source hanzi (qc_entities crashes on a row with no pinyin field). Watch for bare "&" in note bodies: use the numeric ref &#38; (a literal & breaks the XHTML build); and beware substring collisions when adding a short glossary rendering (a new key that is a substring of an existing key, or vice versa, can retro-flag an earlier chapter in check_content — pick distinct renderings or skip the row). First-appearance discipline with the NOT-re-noted ledger in PROGRESS.md; check notes.json BEFORE re-noting anything already covered book-wide (e.g. Chongqing, the Juntong, the Zhongtong, Mount Gele, Dai Li, the Battle of Wuhan, the Central Police Academy, the Hump, Kyoto Imperial University, "Shina", the Co-Prosperity Sphere, the silver dollar/大洋, potassium cyanide, cheongsam, rickshaw, the ROC calendar — all noted in ch31-ch35).
5. Rebuild the cumulative EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; record all check results in PROGRESS.md; keep the ORIGINAL cover (data/figs/cover00144.jpeg, reused byte-identical — commissioner's instruction); commit; push claude/the-rebel.
6. Finish with BOTH chat deliverables: the built EPUB attached, and the Batch B08 kickoff (Rouge / 胭脂 1-6, units ch41-ch46, opens the FOURTH and final novella) pasted VERBATIM in a fenced code block. A Stop hook enforces the pasted kickoff.

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
  novella COMPLETE (ch15-ch30).** Book totals after B05: 202 footnotes, 156
  glossary rows.
- **B06 = Potassium Cyanide 1-5 (ch31-ch35), 252 paragraphs. OPENS the third
  novella (氰化钾).** 35 footnotes added (book total 202 -> 237), 50 glossary
  rows added (book total 156 -> 206). Every historical claim fact-checked
  (Wikipedia / Baidu Baike / Cambridge Core / CGTN / academic). ALL checks green
  (parity/numbers/anchors, alignment, content/displacement, entity survival,
  apparatus); register within tolerance for all five vs the frozen ch01. qa_epub
  PASS; epubcheck 5.1.0 clean (0/0/0/0). 35 of 51 chapters translated. Committed
  and pushed to claude/the-rebel.
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
  commented. B06 added: 四杂街, 金九, 百感交集, 一了百了, 三水湾. Extend as new
  number idioms surface; never noise a real quantity.
- scripts/apparatus_merge.py files each glossary row UNDER its "category" field
  and validates note anchors as verbatim substrings of the reading text; give
  every row a category, an attestation status, AND a pinyin field.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- No source-notes stream (the source carries none; grep each new batch anyway,
  record "none present").
- batch_apparatus_b02.json ... _b05.json and now batch_apparatus_b06.json are
  the kept payloads for the record; author a new batch_apparatus file per batch,
  never edit the ledgers by hand.

## Voice sheets — Potassium Cyanide cast (ACTIVE for B07)

- Jiang Yongnan / 姜泳男 (protagonist): educated, a Kyoto-trained surgeon; Korean.
  Terse, dry, self-mocking under pressure (gallows wit: "Only the dead know the
  taste of poison"); a doctor first, principled to the edge of self-destruction;
  speaks fluent Japanese and Korean. Formal and clipped upward ("Yes."; "Sir")
  to Mr. Qi and Guo Bingyan. Surgeon's calm even in violence.
- Tang Ya / 唐雅: once a Chinese-literature student, now a Chongqing bailiff and
  executioner. Fatalistic, reckless, seductive, sardonic; dark, provocative wit;
  careless of her own life; loathes Yang Qun's fatherly manner and needles him.
  "I have no family, and I have no enemies."
- Yang Qun / 杨群: security-bureau chief, thirty years a policeman; smooth, a
  gentleman in uniform, controlling and unshakeable. Transactional creed ("life
  is nothing but one transaction after another"); calls Tang Ya "Xiao Ya";
  patient to the point of cruelty.
- Guo Bingyan / 郭炳炎: a Nationalist colonel, later revealed a powerful Zhongtong
  figure. Buddhist affectations (sutras, a rattan couch); worldly, genial and
  ruthless at once; speaks in chengyu and aphorism (亡羊补牢, 守株待兔, 漏网之鱼,
  刀头舔血, "a needle at the bottom of the sea"). Ceremonious, unhurried, reads
  a man's whole file before he sits.
- The priest / 神父 (Korean, unnamed): Jiang's countryman and a secret agent of
  the Korean independence cause behind his cassock. Consoles with Chinese
  proverbs; calm, patient, iron-willed. "To live in the wolves' den, be more
  wolf than the wolves."
- Mr. Qi / 祁先生: the Nationalist handler who first turns Jiang. Grave,
  reluctant, terse. "We too act only because we must."
- Old Jin / 老金: the veteran bailiff who oversees the executions and half-fathers
  Tang Ya. Gruff, Sichuanese oaths ("Little bastard"), weary tenderness beneath.

## Voice sheets (The Postman cast — ARCHIVED, novella COMPLETE)

Kept as register calibration; do NOT expect them in Potassium Cyanide.
Xu Zhongliang / 仲良, Zhou San / 周三, Su Lina / 苏丽娜, Mr. Pan / 潘先生 =
Yang Fugang / 杨复纲, Xiufen / 秀芬, Qin Zhaokuan / 秦兆宽, Father Brown / 布朗神父,
Father Kruger / 克鲁格, Itō Kinji / 伊藤近二 = You Kechang / 尤可常, Chen Taining /
陈泰泞, Zhou Chukang / 周楚康, Section Chief Chen / 陈科长. (Full descriptions in
git history / earlier HANDOFF revisions.)

## Voice sheets (The Rebel cast — ARCHIVED, novella complete)

Lin Nansheng (林楠笙), Gu Shenyan (顾慎言), Zhu Yizhen (朱怡贞), Miss Lan
(蓝小姐), Old Pan (老潘), Meng Annan (孟安南), Ji Zhongyuan (纪中原), Ding Mocun
(丁默邨). (Full descriptions in git history / earlier HANDOFF revisions.)

## Where the book stands (story)

- THE REBEL (novella 1) COMPLETE, ch01-ch14.
- THE POSTMAN (novella 2) COMPLETE, ch15-ch30.
- POTASSIUM CYANIDE (novella 3), ch31-ch40, IN PROGRESS. Through B06 (ch31-ch35):
  Jiang Yongnan, a Korean surgeon, is pressed into the Japanese army after Wuhan
  falls in 1938. His Korean priest (a secret independence agent) and the
  Nationalist handler Mr. Qi turn him. Ordered to pass a captured Nationalist
  colonel, Guo Bingyan, a cyanide coin for suicide, Jiang instead plants escape
  tools and gets him out, and so becomes Guo's man. Years on, in wartime
  Chongqing, Jiang kills the American traitor-attaché Anderson at the White Night
  bar. The witness is Tang Ya, the Hankou girl he once saved and claimed as his
  fiancée to shield her from the Japanese, now a bailiff-executioner and the
  cast-off mistress of security chief Yang Qun. Guo orders Jiang to silence her
  (she is a Central Police Academy graduate, possibly a Juntong plant). Jiang
  cannot; they draw together in an air-raid shelter; Yang Qun's men take Jiang,
  and Tang Ya trades herself to Yang Qun to free him. Guo, unveiled as a powerful
  Zhongtong man, cows Yang Qun with a terrifying signature and a gift of
  intelligence, and quietly releases Jiang, telling him to flee Chongqing and
  take Tang Ya with him. But Tang Ya, held overnight by Yang Qun, comes to a
  teahouse expecting Jiang and finds Guo instead: "I am the one who gave the
  order to have you silenced." (Cliffhanger into B07.)
- NEXT after B07: ROUGE (novella 4, ch41-ch51 + back matter and whole-book QA).
  UNREAD.

## What is NEXT

- B07 = Potassium Cyanide 6-10 (ch36-ch40). COMPLETES 氰化钾. Continues from B06;
  cast/voice sheets above; normal batch; ends at the B08 kickoff (Rouge 1-6).
- Then B08 Rouge 1-6 (ch41-ch46), B09 Rouge 7-11 (ch47-ch51) + back matter and
  whole-book QA.

## Settled renderings / carry-forward

- Potassium Cyanide glossary (glossary.json, with category/status/pinyin) covers
  the ch31-ch35 cast, places, and terms; reuse them exactly. Principals across
  the book: the six Rebel principals stay the cast page (The Postman and
  Potassium Cyanide characters were NOT flagged principal — keep that pattern).
- Reused shelf/earlier forms still in force for a Chongqing/wartime novella:
  Chongqing (重庆), Mount Gele (歌乐山), the Jialing River (嘉陵江), the Juntong
  (军统), the Zhongtong (中统), Dai Li (戴笠), the Whampoa Academy, the Baomiju,
  the Tokko (特高课), Wang Jingwei, the silver dollar (大洋), cheongsam (旗袍),
  rickshaw (黄包车), the traitor (汉奸), Hongkou (虹口). B06 added and now settled:
  Hankou, Wuchang, Mount Luojia, Sizajie, East Lake, the Yangtze, Shapingba, the
  Chaotianmen Wharf, Anxi, the Zhongyuan Command, the Central Police Academy, the
  Police Administration Department, the security bureau, the Expeditionary Army,
  the Hanyang Arsenal, the Ordnance Department, bailiff (法警), potassium cyanide
  (氰化钾), the Hump (驼峰), Tieguanyin, the ban on entertainment.
- The source writes 都邮街 for Chongqing's 督邮街 (Duyou Street, glossaried from
  The Rebel); render "Duyou Street" consistently (not re-added, to avoid a
  duplicate same-en row).
- Dialogue is unmarked in the source; quote it in English. Chapter heading = the
  installment number under the part title (title_en is that number). One English
  paragraph per source line (parity machine-enforced; vary rhythm within the
  paragraph).
- COVER: keep the source's original, data/figs/cover00144.jpeg, reused
  byte-identical (commissioner's instruction). Do NOT replace.

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done every batch; expect it again). At B06 the
  stray (claude/the-rebel-b06-izg4qu) was identical to origin/claude/the-rebel
  with no stranded commits; deleted after consolidation.
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch — it was empty at the start of B06). data/zh,
  out/*_en.json, out/*_reading.md, reference/ch01.md, review/content_config.json,
  data/noise.txt and the ledgers are tracked; bilinguals are regenerable and not
  shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file (skip=2) for the
  numbered installments — confirmed at ingest for ch31-ch40. Still, INSPECT each
  head with sed before trusting skip.
- B06 saw ONE digitization glitch: 祁先先 for 祁先生 (Mr. Qi) in ch32 body para
  44; rendered to sense, not footnoted (mechanical typo). No others in ch31-ch35.
- APPARATUS TRAPS (still live): (1) every glossary row needs a "pinyin" field or
  qc_entities crashes. (2) a bare "&" in a note body breaks notes.xhtml; use
  &#38;. (3) check_content and qc_entities want the FULL glossary "en" as a
  substring of the paired English paragraph; name each character once per
  paragraph. (4) a short glossary rendering that is a SUBSTRING of an existing
  key (or vice versa) will retro-flag an EARLIER chapter in check_content — grep
  built chapters for the hanzi and pick a distinct rendering, or skip the row and
  footnote instead. (5) anchors are case-sensitive verbatim substrings of the
  reading md — "the plum-rain season" failed until re-anchored "plum-rain
  season" (the text has "The" at a sentence start).
- The setup.sh checker suite reports one FAILURE ("hook stands down on template
  stub"); it is a FALSE failure of project state (HANDOFF carries a real
  kickoff, not the template placeholder), not a real defect. Record it and move
  on.
