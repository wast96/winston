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
(ch01-ch14), The Postman (ch15-ch30), and Potassium Cyanide (ch31-ch40) are all
COMPLETE. **Rouge (胭脂) is now OPEN: installments 1-6 (ch41-ch46) are DONE.**
Next is B09, the FINAL batch, Rouge 7-11 (ch47-ch51), which COMPLETES the book.

## Message to paste into the next chat

```
The Rebel B09

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then STYLE.md (the prose contract), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, four Republican-era espionage novellas, into an annotated English EPUB. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub. Run ./setup.sh first; if data/src is empty, re-ingest with scripts/ingest_epub.py source.epub (it is gitignored and regenerable).

ch01 is FROZEN as the register reference (reference/ch01.md). This is the FINAL batch: it COMPLETES the book. ch41-ch46 of Rouge are DONE; ch01-ch40 (the first three novellas) are DONE. Run it end to end. Do NOT stop for a voice gate; ch01 stays the frozen reference. There is no B10: finish with the TWO chat deliverables (the built EPUB attached AND the COMPLETION summary pasted verbatim in a fenced code block, since there is no next-batch kickoff). The Stop hook stops demanding a kickoff once HANDOFF.md is rewritten to the completion notice.

Do Batch B09 = Rouge (胭脂) installments 7-11 (units ch47 through ch51), source files data/src/50_part0048.txt .. 54_part0052.txt, per the CLAUDE.md pipeline and STYLE.md. This COMPLETES the fourth novella (胭脂, ch41-ch51) and the whole book. Read the final two pages of out/ch46_reading.md before you start (the voice carries: cool, restrained, brutal). Consult glossary.json and authority.json BEFORE romanizing ANY name or term; the whole Rouge cast (胭脂 Yanzhi, 宝生 Baosheng, 秦树基 Qin Shuji, 老莫 Old Mo, 朱七 Zhu Qi [dead], 唐少爷 Young Master Tang, 刘麻子 Pockmarked Liu [dead], 林小姐 Miss Lin, 秦太太 Mrs. Qin, 白泰来 Bai Tailai, 阿四 Ah Si) and settings (祥符荡 the Xiangfu marsh, 斜塘镇 Xietang, 上海美专 the Shanghai Art Academy) are already in glossary.json — reuse them EXACTLY. From the ch47-ch51 heads: ch47 胭脂 becomes the most ruthless bandit chief of the marsh, letting her men rob but never touching it herself, sitting apart in a small boat with her daughter; ch48 秦树基 (Qin Shuji) reappears one misty morning as she steams her face in the cabin; ch49 she settles at 费家村 (Fei Family Village), ten li outside Xietang; ch50 除夕 (New Year's Eve) in a prison cell; ch51 she comes home to Fei Family Village near dusk in the snow, the first spring after the founding of New China (post-1949) — the close of the book.
1. Read ch47-ch51 from data/src/. Fix extractor-split paragraphs (a body line whose last char is not in 。！？"）…—). Each file has a DOUBLED heading line (skip=2); INSPECT each head with `sed -n '1,3p'` before trusting it. Grep each unit for source note markers (\[\d+\]) and record "none present" in PROGRESS.md (the source has carried none through the whole book; grep anyway).
2. Translate to STYLE.md: literary contemporary English, restrained third person; dialogue IN QUOTATION MARKS (the source runs it unmarked), natural and contracted, grave where the weight wants it; name each character once per paragraph and let pronouns carry the rest (this satisfies qc_entities and check_content — the latter wants the FULL glossary name as a substring of the paired paragraph). Consult glossary.json and authority.json BEFORE romanizing ANY name or term.
3. Per unit, in order: write out/<id>_en.json (one English paragraph per source body line); make_bilingual.py <id> <src> <title_en> out/<id>_en.json <skip> (title_en is the installment number 7..11 per book.json for ch47-ch51; skip is 2); split_bilingual.py out/<id>_bilingual.md <id> "<zh title>" (e.g. "胭脂（7）"); then verify_unit.py (parity + numbers, it uses data/noise.txt), check_align.py <id>, check_content.py --config review/content_config.json, qc_entities.py out/<id>_bilingual.md glossary.json, and check_register.py --ref reference/ch01.md out/<id>_reading.md. Verify each unit's TAIL against the source. Add non-quantitative numerals to data/noise.txt with a comment as they flag; NEVER noise a real quantity.
4. Footnotes per STYLE.md's apparatus doctrine — be generous, the commissioner loves them: history, institutions, money, geography, custom, material culture, AND the nuances lost in translation (telling names, idioms/allusions/chengyu given with the hanzi and the literal image, symbolism, honorifics, loaded keywords). Likely note targets: the founding of the PRC / New China, 土改 land reform and the 五亩地 (five-mu allotment), 除夕 New Year's Eve customs, 费家村 geography, and any late allusions. Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source — do NOT cite Grok/Grokipedia), state the verdict in the note, flag any source conflict, keep the source's own errors of fact visible and footnoted. Use apparatus_merge.py (never a shell heredoc); give every new glossary row a "category" (people / organizations / places / terms), an attestation status, AND the Mandarin "pinyin" of the source hanzi (qc_entities crashes on a row with no pinyin field). Watch for bare "&" in note bodies: use &#38; (a literal & breaks the XHTML build); and beware substring collisions when adding a short glossary rendering. First-appearance discipline with the NOT-re-noted ledger in PROGRESS.md; check notes.json BEFORE re-noting anything already covered book-wide (301 notes are in place across ch01-ch46 — e.g. cheongsam, rickshaw, the silver dollar/大洋, the ROC calendar, the Juntong/Zhongtong, the concessions, pingtan, the almanac 皇历, taijun 太君, the levirate custom, the Sincere Company, the Shanghai Art Academy, the puppet currencies 联银券/中储券).
5. FINAL-BATCH BACK MATTER + WHOLE-BOOK QA (this batch carries it): run check_reconcile.py (repeated-compound rendering drift, glossary-forward usage, spelling locale by curated pairs) plus by hand grep-count ~20 decided renderings and confirm notes-at-first-appearance; write out/term_ledger.md and out/deep_audit.md (3-5% random-sample deep audit, FIXED seed, honest error-rate statement, grep for the "invented precision" class); feed settled renderings back into authority.json; CLEAN the TOC (drop the pending-aware markers now that all 51 units are translated); write COMPLETION.md from the scanned template. Rebuild the cumulative EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; keep the ORIGINAL cover (data/figs/cover00144.jpeg, reused byte-identical — commissioner's instruction); `git add -f out/the_rebel.epub`; record all check results in PROGRESS.md; commit; push claude/the-rebel.
6. Rewrite HANDOFF.md to COMPLETE (the completion notice, no kickoff — the Stop hook stops demanding a block once the kickoff section is gone) and do not touch it afterward. Finish with BOTH chat deliverables: the built EPUB attached, and the COMPLETION summary pasted VERBATIM in a fenced code block (there is no next kickoff). A Stop hook enforces the pasted fenced block.

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
- B07 = Potassium Cyanide 6-10 (ch36-ch40), 234 paragraphs. COMPLETES the third
  novella (氰化钾, ch31-ch40). 30 footnotes.
- **B08 = Rouge 1-6 (ch41-ch46), 201 paragraphs. OPENS the fourth and final
  novella (胭脂). 34 footnotes added (book total 267 -> 301), 17 glossary rows
  added (book total 241 -> 258). Every historical claim fact-checked (Wikipedia /
  Baidu Baike / academic). ALL checks green (parity/numbers/anchors, alignment,
  content/displacement, entity survival, apparatus); register within tolerance
  for all six vs the frozen ch01. qa_epub PASS; epubcheck 5.1.0 clean (0/0/0/0).
  46 of 51 chapters translated. Committed and pushed to claude/the-rebel.**
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
  commented. B08 added: 百福楼, 两岸, 秋千, 阿四, 百货公司, 朱七, 五花大绑,
  十里港, 千百年. Extend as new number idioms surface; never noise a real quantity.
- scripts/apparatus_merge.py files each glossary row UNDER its "category" field
  and validates note anchors as verbatim substrings of the reading text; give
  every row a category, an attestation status, AND a pinyin field.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- No source-notes stream (the source carries none; grep each new batch anyway,
  record "none present").
- batch_apparatus_b02.json ... batch_apparatus_b08.json are the kept payloads
  for the record; author a new batch_apparatus file per batch, never edit the
  ledgers by hand.

## Voice sheets — Rouge cast (胭脂, ch41-ch51) — ESTABLISHED IN B08

- **胭脂 Yanzhi ("Rouge"), the protagonist.** Cool, still, opaque; says little,
  and what she says lands flat and hard ("Bullshit"; "Even if he's gone I still
  won't marry you"; "being alive is better than anything"). A passive surface
  over an iron will that surfaces, terribly, in ch45-ch46 (she commands, buys
  knives, stabs Pockmarked Liu to death). Never sentimental, never explains
  herself. Contractions in speech; grave, uncontracted where the weight wants it.
- **宝生 Baosheng (surname Hu; "Master Hu" / "Boss Hu").** The tailor: dutiful,
  timid, decent, self-effacing. Cannot meet her eyes. Speaks softly, plainly,
  apologetically ("Don't worry, I'll be good to you"). Contracted, humble.
- **秦树基 Qin Shuji.** The Shanghai oil-painter. Evasive, self-absorbed, cool;
  short deflections ("Now is not the time to come"; "I have to keep this
  household going"). A coward under the aesthete. (Reappears in ch48.)
- **朱七 Zhu Qi (DEAD, ch46).** The water-bandit chief. Rough, swaggering,
  lecherous but shrewd, knife-eyed; coarse oaths ("damn these Eastern-ocean
  turtles"), blunt appetite, then a startling tenderness at the end ("a pity I
  never had the luck to be your man").
- **老莫 Old Mo.** Boatman/bandit; weary, practical, fatalistic. Marsh-realist,
  plain speech ("Apart from robbing and smoking opium, there's nothing we can
  do"). Becomes Yanzhi's right hand.
- **唐少爷 Young Master Tang.** The collaborator heir. Ingratiating, self-
  justifying, oily, darkly comic; lusts after Yanzhi. Wheedling, rationalizing
  speech ("The old master's gone, I have to go on living, don't I?"). MUST be
  named "Young Master Tang" in full once per paragraph he appears (check_content).
- **刘麻子 Pockmarked Liu (DEAD, ch46), 白泰来 Bai Tailai (DEAD, ch41 flashback),
  秦太太 Mrs. Qin, 林小姐 Miss Lin, 阿四 Ah Si, 本良 Benliang (DEAD, ch44):**
  minor; register per glossary.json.

## Voice sheets (Potassium Cyanide / The Postman / The Rebel casts — ARCHIVED)

Kept as register calibration; novellas 1-3 COMPLETE. Potassium Cyanide: Jiang
Yongnan, Tang Ya, Yang Qun, Guo Bingyan, the Korean priest, Mr. Qi, Old Jin,
Jiang Yongzhu, Adjutant Yan. The Postman: Xu Zhongliang/仲良, Zhou San, Su Lina,
Mr. Pan/Yang Fugang, Xiufen, Qin Zhaokuan, Father Brown, Father Kruger, Itō
Kinji/You Kechang, Chen Taining, Zhou Chukang, Section Chief Chen. The Rebel:
Lin Nansheng, Gu Shenyan, Zhu Yizhen, Miss Lan, Old Pan, Meng Annan, Ji
Zhongyuan, Ding Mocun. (Full descriptions in git history / earlier HANDOFF revs.)

## Where the book stands (story)

- THE REBEL (novella 1) COMPLETE, ch01-ch14. THE POSTMAN (novella 2) COMPLETE,
  ch15-ch30. POTASSIUM CYANIDE (novella 3) COMPLETE, ch31-ch40.
- ROUGE (novella 4, ch41-ch51) — IN PROGRESS. ch41-ch46 done. Yanzhi comes home
  and is married off to the tailor Baosheng at her dying father's charge, though
  she loves the Shanghai painter Qin Shuji; she follows Qin to Shanghai, becomes
  his kept woman, is abandoned when he vanishes (his gallery and rooms sealed by
  the Garrison Command), and returns home. War comes: a Japanese bomb destroys
  the Tang soy-works; Young Master Tang turns collaborator headman. Zhu Qi's
  water bandits raid the town; the Japanese behead thirteen townsmen in reprisal.
  Baosheng is captured for ransom; Yanzhi ransoms him, is taken by Zhu Qi (who
  makes Baosheng sew her eighteen bridal cheongsams and means to wed her).
  Baosheng, freed, leads the Japanese to the marsh; in the reed-fire Zhu Qi is
  shot and dies on Yanzhi. She takes command of the survivors, marries down to
  Zhu Qi's sworn brother Pockmarked Liu by the levirate custom and stabs him
  dead in his bed, becomes the Big Sister-in-law (当家的), and a year later bears
  a daughter.
- ROUGE ch47-ch51 — NEXT and LAST (B09): Yanzhi the ruthless marsh chief; Qin
  Shuji's reappearance; retreat to 费家村 (Fei Family Village); a prison cell on
  New Year's Eve; and the close, the first spring after the founding of New
  China (post-1949).

## What is NEXT

- B09 = Rouge 7-11 (ch47-ch51) — the FINAL batch. COMPLETES the book and the
  whole project: back matter, whole-book reconciliation (check_reconcile.py,
  term_ledger.md, deep_audit.md), authority.json fed back, COMPLETION.md, TOC
  cleaned of pending markers, HANDOFF rewritten to COMPLETE.

## Settled renderings / carry-forward

- Rouge glossary (glossary.json, with category/status/pinyin) covers the whole
  ch41-ch46 cast, places, and terms; reuse them EXACTLY if any recur (they will:
  Yanzhi, Baosheng, Qin Shuji, Old Mo, Young Master Tang, the Xiangfu marsh,
  Xietang, the Shanghai Art Academy, taijun). Baosheng's surname is Hu (Master
  Hu / Boss Hu / 胡太太 Mrs. Hu / 师母 Shimu).
- Principals across the book stay the six Rebel principals on the cast page (The
  Postman, Potassium Cyanide, and Rouge characters were NOT flagged principal —
  keep that pattern unless the commissioner says otherwise).
- Shanghai and Jiangnan furniture is heavily glossaried and noted (concessions,
  roads, the silver dollar/大洋, cheongsam, rickshaw, pingtan, the Sincere
  Company, the almanac, taijun, the puppet currencies, the levirate custom);
  check glossary.json and notes.json BEFORE romanizing or re-noting anything.
- Dialogue is unmarked in the source; quote it in English. Chapter heading = the
  installment number under the part title (title_en is that number). One English
  paragraph per source line (parity machine-enforced; vary rhythm within the
  paragraph).
- COVER: keep the source's original, data/figs/cover00144.jpeg, reused
  byte-identical (commissioner's instruction). Do NOT replace.

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done every batch; expect it again). At B08 the
  stray (claude/the-rebel-b08-rouge-32a79h) was at the same commit as
  origin/claude/the-rebel with no stranded commits; deleted after consolidation.
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch — it was empty at the start of B08). data/zh,
  out/*_en.json, out/*_reading.md, reference/ch01.md, review/content_config.json,
  data/noise.txt and the ledgers are tracked; bilinguals are regenerable and not
  shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file (skip=2) for the
  numbered installments — held through ch46. Still, INSPECT each head with sed
  before trusting skip.
- APPARATUS TRAPS (still live): (1) every glossary row needs a "pinyin" field or
  qc_entities crashes. (2) a bare "&" in a note body breaks notes.xhtml; use
  &#38;. (3) check_content and qc_entities want the FULL glossary "en" as a
  substring of the paired English paragraph; name each character once per
  paragraph. check_content only ENFORCES glossary names whose "en" starts with
  an uppercase letter (so "the Xiangfu marsh" etc. are not enforced, but
  "Yanzhi", "Young Master Tang", "Jiahe County" are). (4) a short glossary
  rendering that is a SUBSTRING of an existing key (or vice versa) can retro-flag
  an EARLIER chapter — grep built chapters for the hanzi and pick a distinct
  rendering, or skip the row and footnote instead. (5) anchors are case-sensitive
  verbatim substrings of the reading md (watch straight vs curly apostrophes —
  anchor on a stretch without an apostrophe when in doubt).
- NUMBER-CHECK traps in Rouge: names/words containing digit characters must be
  noised (朱七/七, 阿四/四, 百福楼/百, 百货公司/百, 秋千/千, 十里港/十里,
  五花大绑/五, 千百年, 两岸). A real quantity is always fixed in the English,
  never noised (thirteen beheaded, eighteen cheongsams, four sabers, three days
  and three nights, thirty silver dollars).
- The setup.sh checker suite reports one FAILURE ("hook stands down on template
  stub"); it is a FALSE failure of project state (HANDOFF carries a real kickoff,
  not the template placeholder), not a real defect. Record it and move on.
