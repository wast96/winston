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
every batch is a normal batch that ends at its next-batch kickoff.

## Message to paste into the next chat

```
The Rebel B02

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then STYLE.md (the prose contract), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, four Republican-era espionage novellas, into an annotated English EPUB. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub. Run ./setup.sh first; if data/src is empty, re-ingest with scripts/ingest_epub.py source.epub (it is gitignored and regenerable).

Batch 1 passed the voice gate; ch01 is FROZEN as the register reference (reference/ch01.md). This is a NORMAL batch: run it end to end and finish with the TWO chat deliverables (the built EPUB attached AND the next batch's kickoff pasted verbatim in a fenced block). Do NOT stop for a voice gate.

Do Batch B02 = The Rebel installments 8-14 (units ch08 through ch14), source files data/src/11_part0009.txt .. 17_part0015.txt, per the CLAUDE.md pipeline and STYLE.md:
1. Read ch08-ch14 from data/src/. Fix extractor-split paragraphs (a body line whose last char is not in 。！？"）…—); the source has a DOUBLED heading line per file, so make_bilingual runs with skip=2. Grep each unit for source note markers (\[\d+\]) and record "none present" in PROGRESS.md.
2. Translate to STYLE.md: literary contemporary English, restrained third person, Lin Nansheng's cool analytical register; dialogue IN QUOTATION MARKS (the source runs it unmarked), natural and contracted, grave where the weight wants it; name each character once per paragraph and let pronouns carry the rest (this satisfies qc_entities and check_content — the latter wants the FULL glossary name, not just a surname). Render idioms to natural English in the text and keep the literal image or allusion in a FOOTNOTE. Consult glossary.json and authority.json BEFORE romanizing ANY name or term; carry forward the settled renderings and the voice sheets in this HANDOFF. Read the last two pages of ch07's English first, for the voice at the seam.
3. Per unit, in order: write out/<id>_en.json (one English paragraph per source body line); make_bilingual.py <id> <src> <title_en> out/<id>_en.json 2; split_bilingual.py; then verify_unit.py (parity + numbers, it uses data/noise.txt), check_align.py, check_content.py --config review/content_config.json, qc_entities.py out/<id>_bilingual.md glossary.json, and check_register.py --ref reference/ch01.md out/<id>_reading.md (drift is now live — keep dialogue contractions near the reference). Verify each unit's TAIL against the source. Add non-quantitative numerals to data/noise.txt with a comment as they flag; NEVER noise a real quantity.
4. Footnotes per STYLE.md's apparatus doctrine — be generous, the commissioner loves them: cover history, institutions, money, geography, custom, and material culture, AND the nuances lost in translation (telling given-names, idioms/allusions/chengyu given with the hanzi and the literal image, symbolism, honorifics, loaded keywords of the 叛逆者/叛徒 kind). Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source), state the verdict in the note, flag any source conflict, and keep the source's own errors of fact visible and footnoted. Use apparatus_merge.py (never a shell heredoc); first-appearance discipline with the NOT-re-noted ledger in PROGRESS.md; new glossary rows carry a "category" (people / organizations / places / terms) and an attestation status.
5. Rebuild the cumulative EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; record all check results in PROGRESS.md; keep the ORIGINAL cover (data/figs/cover00144.jpeg, reused byte-identical — commissioner's instruction); commit; push claude/the-rebel.
6. Finish with BOTH chat deliverables: the built EPUB attached, and the Batch B03 kickoff (The Postman 1-6, units ch15-ch20) pasted VERBATIM in a fenced code block. A Stop hook enforces the pasted kickoff.

Cite chapters and sections, never pages. Do not pause for approval mid-batch; only stop for a genuine blocker or completion.
```

## What is DONE (do not redo)

- Step 0 survey: source ingested, book.json authored (51 units, four parts),
  skeleton EPUB green, batch plan approved (9 batches).
- Batch B01 = The Rebel 1-7 (ch01-ch07), 357 paragraphs, translated end to end.
  VOICE GATE PASSED. ch01 frozen as the register reference (reference/ch01.md).
  50 footnotes, 51 glossary rows, Principal Characters page. All checks green
  (parity/numbers/anchors, alignment, content/displacement, entity survival,
  register, apparatus); qa_epub PASS, epubcheck 5.1.0 clean. Committed and
  pushed to claude/the-rebel.
- STYLE.md written and adopted as the project prose contract.

## Tooling in place (do NOT revert)

- STYLE.md — the project PROSE CONTRACT (general rules and reasoning, no book
  specifics). Read it every batch, before translating. It encodes the
  voice-gate calibrations: preserve the source's register while de-stiffening
  the machine, dialogue quoting, once-per-paragraph naming, natural-idiom-in-
  text with the literal image in a footnote, and the generous-but-honest
  footnote doctrine. Do not delete or narrow it.
- reference/ch01.md — the FROZEN register reference. Run
  check_register.py --ref reference/ch01.md on every new unit. Do not
  regenerate or overwrite it (if ch01's wording is ever corrected, update the
  reference deliberately, noting it).
- review/content_config.json — docs/sources map for ALL 51 units (untranslated
  ones are skipped automatically). Run check_content.py --config
  review/content_config.json.
- data/noise.txt — project entries for non-quantitative source numerals, each
  commented. Extend as new number idioms surface; never noise a real quantity.
- scripts/apparatus_merge.py — patched so glossary rows file UNDER their
  section (the row's "category", default "terms"); give every glossary row a
  category. scripts/check_content.py — patched to skip non-dict / "_"-prefixed
  glossary sections. Keep both fixes.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- No source-notes stream (the source carries none).

## Voice sheets (one per major character, written at first appearance)

- Lin Nansheng (林楠笙): the protagonist. Educated, controlled, near-silent
  under pressure; short flat sentences, hard truths stated plainly. Interiority
  carried by narration, not speech; dry, self-directed irony. Colder and
  blacker after his wound. Pinyin.
- Gu Shenyan (顾慎言): Lin's spymaster and former training-class director. The
  cultivated aesthete (symphonies, Peking opera, go, Baudelaire); measured
  aphorism and indirection, warm on the surface and testing underneath, never
  loud. His given name means "guard your words." Pinyin.
- Zuo Qiuming (左秋明): Lin's fellow trainee, a Juntong liaison officer. Brief,
  warm, professional; the mild traveler's smile over a hard core. The batch
  turns on his suicide under interrogation. Pinyin.
- Ding Mocun (丁默邨): the historical turncoat, director of No. 76. Cold,
  ironic, unhurried; enjoys the upper hand and needles his visitor. A man who
  has chosen his side and feels no need to justify it. Historical; pinyin.
- Zhu Yizhen (朱怡贞): the Communist agent, Lin's former student and lover.
  Proud, stubborn, wounded; cold formality broken by sudden fractures (the
  scream ending ch02, the cut embroidery). Silence and needlework carry what
  she won't say. Endearment 贞贞 = Zhenzhen. Pinyin.
- Ji Zhongyuan (纪中原): Zhu's controller and cover-husband, posing as a
  seal-engraver. Quiet, patient, absolute about the primacy of the work;
  jealousy shows only as dryness in the voice. Fakes his death and returns.
  Pinyin.

## Where the book stands (story)

- The Rebel, installments 1-7 done. Lin Nansheng, a Juntong agent in occupied
  Shanghai, is shot in an ambush and smuggled to a Japanese army hospital in
  Hong Kong, his spine wound leaving him unable to feel pain. Flashbacks: his
  handler Gu Shenyan; the assassination of the collaborator Tong Zizhong at the
  Cathay Hotel; his re-entangled love with Zhu Yizhen, a Communist agent
  married in cover to her controller Ji Zhongyuan; their flight from No. 76's
  dragnet; the killing of the consul Kobayashi; the ambush at the City God
  Temple that leaves Zhu apparently dead and Lin crippled; Gu's night bargain
  with Ding Mocun to pull Lin out of Japanese hands. In Hong Kong, Lin learns
  Ji faked his death; his friend Zuo Qiuming is captured and takes his own life
  rather than talk; Ji hints Zhu may be alive (two coffins left the hospital).
  Lin is recalled to Chongqing to instruct at SACO; Ji gives him a poem-cipher
  ("Ode to the Plum Blossom," signed Huang Shanyun) for contact. Whether Zhu
  lives is the open thread going into ch08.

## What is NEXT

- B02 = The Rebel 8-14 (ch08-ch14). Normal batch; ends at the B03 kickoff.
- Then B03-B05 The Postman (ch15-ch30, incl. the 后记/afterword ch30),
  B06-B07 Potassium Cyanide (ch31-ch40), B08-B09 Rouge (ch41-ch51 + back
  matter and whole-book QA). Nine batches total.

## Settled renderings / carry-forward

- Cross-shelf (authority.json) forms in use: Wang Jingwei, Dai Li, the Juntong,
  the Cathay Hotel, Avenue Joffre, Suzhou Creek, Yuyuan Road, Nanjing Road,
  rickshaw, cheongsam, Chongqing. New this book (in glossary.json): Ding Mocun,
  No. 76 / Jessfield Road, the Zhongtong, the Peace Army, SACO, the Tokkō, Rue
  Ratard, the Zhonghua Ribao, The Young Companion, Ta Kung Pao, the Central
  Reserve Bank, and the full cast.
- 贞贞 = Zhenzhen; Japanese speakers address Lin as "Pang-san" / "Lin-san"
  (庞桑 / 林桑) under his cover name Pang Jiajun; Kobayashi = 小林大介.
- Dialogue is unmarked in the source; quote it in English. Chapter heading =
  the installment number under the part title. One English paragraph per source
  line (parity is machine-enforced; vary rhythm within the paragraph).
- COVER: keep the source's original, data/figs/cover00144.jpeg, reused
  byte-identical (commissioner's instruction). Do NOT replace or regenerate it.

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done twice this session; expect it again).
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch). data/zh, out/*_en.json, out/*_reading.md,
  reference/ch01.md, review/content_config.json and the ledgers are tracked;
  bilinguals are regenerable and not shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file (skip=2). Watch
  for the pervasive commercial-ebook glitches CLAUDE.md lists; none seen in
  ch01-ch07.
- The setup.sh checker suite reports one FAILURE ("hook stands down on template
  stub"); it is a FALSE failure of project state (HANDOFF carries a real
  kickoff, not the template placeholder), not a real defect. Record it and move
  on.
