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
(ch01-ch14), The Postman (ch15-ch30), and **Potassium Cyanide (ch31-ch40) are
all COMPLETE.** Next is B08, which OPENS the fourth and final novella, Rouge
(胭脂), with installments 1-6 (ch41-ch46).

## Message to paste into the next chat

```
The Rebel B08

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then STYLE.md (the prose contract), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, four Republican-era espionage novellas, into an annotated English EPUB. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub. Run ./setup.sh first; if data/src is empty, re-ingest with scripts/ingest_epub.py source.epub (it is gitignored and regenerable).

ch01 is FROZEN as the register reference (reference/ch01.md). This is a NORMAL batch: run it end to end and finish with the TWO chat deliverables (the built EPUB attached AND the next batch's kickoff pasted verbatim in a fenced block). Do NOT stop for a voice gate; ch01 stays the frozen reference (do not re-freeze).

Do Batch B08 = Rouge (胭脂) installments 1-6 (units ch41 through ch46), source files data/src/44_part0042.txt .. 49_part0047.txt, per the CLAUDE.md pipeline and STYLE.md. This OPENS the FOURTH and FINAL novella (胭脂, ch41-ch51). It is a fresh cast and a fresh setting: the Chongqing/Wuhan/Ganzhou world of Potassium Cyanide is closed. Rouge is a Jiangnan water-country tale. Because it opens a novella, this is like a new book's first batch: ESTABLISH a voice sheet for each major character at first appearance and write it into HANDOFF's carry-forward section, and consult glossary.json and authority.json BEFORE romanizing ANY name or term. Read the final two pages of out/ch40_reading.md before you start — not for cast continuity (the cast changes) but for the author's overall voice, cool and restrained, which carries across the novellas. From the ch41-ch46 heads: ch41 一个叫胭脂 (Yanzhi/"Rouge") marries 宝生 (Baosheng) three days after coming home; ch42 at 上海师专 (the Shanghai Normal College) she meets 秦树基 (Qin Shuji), the man she would risk everything for; ch43 married life, her Shanghai habits kept; ch44 winter fog and the water bandits of 祥符荡 (the Xiangfu marsh); ch45 老莫 (Old Mo) ferries Yanzhi across the marsh; ch46 the reed-marsh fire burns three days and three nights, and 朱七 (Zhu Qi) dies in it. Consult glossary.json and authority.json BEFORE romanizing ANY name or term; a few Shanghai/Jiangnan places may already be settled there from earlier novellas (check first).
1. Read ch41-ch46 from data/src/. Fix extractor-split paragraphs (a body line whose last char is not in 。！？"）…—). Each file has a DOUBLED heading line (ch41 confirmed at ingest; the pattern has held for every numbered installment in this book), so make_bilingual runs with skip=2; INSPECT each head with `sed -n '1,3p'` before trusting it. Grep each unit for source note markers (\[\d+\]) and record "none present" in PROGRESS.md (the source has carried none through the whole book; grep anyway).
2. Translate to STYLE.md: literary contemporary English, restrained third person; dialogue IN QUOTATION MARKS (the source runs it unmarked), natural and contracted, grave where the weight wants it; name each character once per paragraph and let pronouns carry the rest (this satisfies qc_entities and check_content — the latter wants the FULL glossary name as a substring of the paired paragraph). Consult glossary.json and authority.json BEFORE romanizing ANY name or term.
3. Per unit, in order: write out/<id>_en.json (one English paragraph per source body line); make_bilingual.py <id> <src> <title_en> out/<id>_en.json <skip> (title_en is the installment number 1..6 per book.json for ch41-ch46; skip is 2); split_bilingual.py out/<id>_bilingual.md <id> "<zh title>" (e.g. "胭脂（1）"); then verify_unit.py (parity + numbers, it uses data/noise.txt), check_align.py <id>, check_content.py --config review/content_config.json, qc_entities.py out/<id>_bilingual.md glossary.json, and check_register.py --ref reference/ch01.md out/<id>_reading.md. Verify each unit's TAIL against the source. Add non-quantitative numerals to data/noise.txt with a comment as they flag; NEVER noise a real quantity.
4. Footnotes per STYLE.md's apparatus doctrine — be generous, the commissioner loves them: cover history, institutions, money, geography, custom, and material culture, AND the nuances lost in translation (telling given-names — 胭脂 "rouge/cosmetic" is itself a loaded, telling name worth a note — idioms/allusions/chengyu given with the hanzi and the literal image, symbolism, honorifics, loaded keywords). Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source), state the verdict in the note, flag any source conflict, keep the source's own errors of fact visible and footnoted. Use apparatus_merge.py (never a shell heredoc); give every new glossary row a "category" (people / organizations / places / terms), an attestation status, AND the Mandarin "pinyin" of the source hanzi (qc_entities crashes on a row with no pinyin field). Watch for bare "&" in note bodies: use the numeric ref &#38; (a literal & breaks the XHTML build); and beware substring collisions when adding a short glossary rendering (a new key that is a substring of an existing key, or vice versa, can retro-flag an earlier chapter in check_content — pick distinct renderings or skip the row). First-appearance discipline with the NOT-re-noted ledger in PROGRESS.md; check notes.json BEFORE re-noting anything already covered book-wide (267 notes are already in place across ch01-ch40 — e.g. cheongsam, rickshaw, the silver dollar/大洋, the ROC calendar, the Juntong, the Zhongtong, the concessions, and much of the Shanghai furniture from The Rebel and The Postman).
5. Rebuild the cumulative EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; record all check results in PROGRESS.md; keep the ORIGINAL cover (data/figs/cover00144.jpeg, reused byte-identical — commissioner's instruction); commit; push claude/the-rebel.
6. Finish with BOTH chat deliverables: the built EPUB attached, and the Batch B09 kickoff (Rouge / 胭脂 7-11, units ch47-ch51 — the FINAL batch, which COMPLETES the book and carries the back matter, whole-book reconciliation / term_ledger / deep_audit, and COMPLETION.md) pasted VERBATIM in a fenced code block. A Stop hook enforces the pasted kickoff.

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
- B05 = The Postman 12-15 + Afterword (ch26-ch30), 231 paragraphs. The Postman
  novella COMPLETE (ch15-ch30).
- B06 = Potassium Cyanide 1-5 (ch31-ch35), 252 paragraphs. Opened the third
  novella. 35 footnotes, 50 glossary rows.
- **B07 = Potassium Cyanide 6-10 (ch36-ch40), 234 paragraphs. COMPLETES the
  third novella (氰化钾, ch31-ch40).** 30 footnotes added (book total 237 -> 267),
  35 glossary rows added (book total 206 -> 241). Every historical claim
  fact-checked (Wikipedia / Baidu Baike / academic). ALL checks green
  (parity/numbers/anchors, alignment, content/displacement, entity survival,
  apparatus); register within tolerance for all five vs the frozen ch01. qa_epub
  PASS; epubcheck 5.1.0 clean (0/0/0/0). 40 of 51 chapters translated. Committed
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
  commented. B07 added: 三青团, 四起, 四顾, 八仙桌, 四溅, 千山万水, 九龙坡,
  五光十色. Extend as new number idioms surface; never noise a real quantity.
- scripts/apparatus_merge.py files each glossary row UNDER its "category" field
  and validates note anchors as verbatim substrings of the reading text; give
  every row a category, an attestation status, AND a pinyin field.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- No source-notes stream (the source carries none; grep each new batch anyway,
  record "none present").
- batch_apparatus_b02.json ... batch_apparatus_b07.json are the kept payloads
  for the record; author a new batch_apparatus file per batch, never edit the
  ledgers by hand.

## Voice sheets — Rouge cast (胭脂, ch41-ch51) — TO ESTABLISH IN B08

Rouge is UNREAD beyond the chapter heads. Establish a two-line register spec
for each principal AT FIRST APPEARANCE and write it here. From the heads, the
emerging cast is: 胭脂 (Yanzhi / "Rouge", the protagonist), 宝生 (Baosheng, whom
she marries), 秦树基 (Qin Shuji, the Shanghai man she cannot resist), 老莫 (Old
Mo, a boatman/ferry across the Xiangfu marsh), 朱七 (Zhu Qi, a water-bandit who
dies in the reed fire). Setting: the Jiangnan water country — the 祥符荡 (Xiangfu
marsh), Shanghai, the 上海师专 (Shanghai Normal College). Consult glossary.json
and authority.json before romanizing any of these; decide renderings once.

## Voice sheets (Potassium Cyanide cast — ARCHIVED, novella COMPLETE)

Kept as register calibration; do NOT expect them in Rouge.
Jiang Yongnan / 姜泳男 (the Korean surgeon-agent), Tang Ya / 唐雅 (the
bailiff-executioner), Yang Qun / 杨群 (the security chief), Guo Bingyan / 郭炳炎
(the Zhongtong "Grand Executioner"), the Korean priest / 神父, Mr. Qi / 祁先生,
Old Jin / 老金, Jiang Yongzhu / 姜泳洙 (the brother), Adjutant Yan / 严副官. (Full
descriptions in git history / earlier HANDOFF revisions.)

## Voice sheets (The Postman cast — ARCHIVED, novella COMPLETE)

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
- POTASSIUM CYANIDE (novella 3) COMPLETE, ch31-ch40. Jiang Yongnan, a Korean
  surgeon turned Zhongtong agent, is sent back through occupied Hankou to kill a
  Japanese colonel; the Korean priest dies covering his escape. Exiled to a
  youth-cadre camp in Gannan, he marries Shen Jinzhu, then gives her back to her
  first husband, returned from the dead. After victory he returns to Chongqing,
  is received by the Generalissimo, finds his brother Jiang Yongzhu, and is
  cornered by Guo Bingyan, who hands him a last assignment (kill Yang Qun) and,
  when he refuses, has him arrested. Yang Qun, before his own sniper-killing by
  Adjutant Yan, shows Jiang the Anderson safe house and the Taiping-Society list
  and begs him to take Tang Ya away. Jiang is caught, condemned; the executioners'
  fake-execution ruse (a blank round, "fall at the shot") fails when Guo's sniper
  kills Jiang for real. Tang Ya kills the informer Old Jin, then, months later,
  poisons Guo Bingyan with the cyanide coin at Qixia Temple and carries Jiang's
  ashes home to Jeju. The recurring cocktail "potassium cyanide" was always
  missing one thing: a pinch of salt.
- ROUGE (novella 4, ch41-ch51) — NEXT, and the last. UNREAD. A Jiangnan
  water-country tale: 胭脂 (Yanzhi/Rouge), her marriage to 宝生 (Baosheng), the
  Shanghai man 秦树基 (Qin Shuji), the 祥符荡 (Xiangfu marsh) and its water
  bandits.

## What is NEXT

- B08 = Rouge 1-6 (ch41-ch46). OPENS 胭脂. New cast, new setting; establish
  voice sheets at first appearance; normal batch; ends at the B09 kickoff.
- B09 = Rouge 7-11 (ch47-ch51) — the FINAL batch. COMPLETES the book and the
  whole project: back matter, whole-book reconciliation (check_reconcile.py,
  term_ledger.md, deep_audit.md), authority.json fed back, COMPLETION.md, TOC
  cleaned, HANDOFF rewritten to COMPLETE.

## Settled renderings / carry-forward

- Potassium Cyanide glossary (glossary.json, with category/status/pinyin) covers
  the whole ch31-ch40 cast, places, and terms; reuse them exactly if any recur.
  Principals across the book stay the six Rebel principals on the cast page (The
  Postman and Potassium Cyanide characters were NOT flagged principal — keep that
  pattern for Rouge too unless the commissioner says otherwise).
- Shanghai and Jiangnan furniture is heavily glossaried from The Rebel and The
  Postman (concessions, roads, the silver dollar/大洋, cheongsam, rickshaw, the
  Juntong, the Zhongtong, etc.); check glossary.json and notes.json BEFORE
  romanizing or re-noting anything in Rouge.
- Dialogue is unmarked in the source; quote it in English. Chapter heading = the
  installment number under the part title (title_en is that number). One English
  paragraph per source line (parity machine-enforced; vary rhythm within the
  paragraph).
- COVER: keep the source's original, data/figs/cover00144.jpeg, reused
  byte-identical (commissioner's instruction). Do NOT replace.

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done every batch; expect it again). At B07 the
  stray (claude/the-rebel-b07-zhnzr2) was identical to origin/claude/the-rebel
  with no stranded commits; deleted after consolidation.
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch — it was empty at the start of B07). data/zh,
  out/*_en.json, out/*_reading.md, reference/ch01.md, review/content_config.json,
  data/noise.txt and the ledgers are tracked; bilinguals are regenerable and not
  shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file (skip=2) for the
  numbered installments — confirmed at ingest through ch41. Still, INSPECT each
  head with sed before trusting skip.
- B07 digitization glitches (rendered to sense, not footnoted — mechanical
  typos): ch37 沈近珠 for 沈近朱 (Shen Jinzhu); ch37 岩田 for the settled 岩井
  (Iwai) Hankou clinic; ch36 两楼 for 二楼 (second floor). Expect similar in Rouge.
- APPARATUS TRAPS (still live): (1) every glossary row needs a "pinyin" field or
  qc_entities crashes. (2) a bare "&" in a note body breaks notes.xhtml; use
  &#38;. (3) check_content and qc_entities want the FULL glossary "en" as a
  substring of the paired English paragraph; name each character once per
  paragraph. (4) a short glossary rendering that is a SUBSTRING of an existing
  key (or vice versa) will retro-flag an EARLIER chapter in check_content — grep
  built chapters for the hanzi and pick a distinct rendering, or skip the row and
  footnote instead. Set glossary "en" WITHOUT a leading article when the text
  varies the article (e.g. "207th Division", "Yamazaki", "Third Air Group") so
  the substring match holds across "the/his/their". (5) anchors are
  case-sensitive verbatim substrings of the reading md.
- The setup.sh checker suite reports one FAILURE ("hook stands down on template
  stub"); it is a FALSE failure of project state (HANDOFF carries a real kickoff,
  not the template placeholder), not a real defect. Record it and move on.
