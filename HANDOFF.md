# HANDOFF — The Rebel (叛逆者) / Bi Yu

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE
CHAT, alongside the attached EPUB. Writing it here alone does not count.**
Rewrite it at the end of every batch; always keep the paste-ready message
below as its first section. When the book completes, replace it with the
completion notice and do not touch it afterward (the Stop hook keys off it).

Batch 1 is a special case: it ends at the first-chapter VOICE GATE (CLAUDE.md
Step 0c), not at a normal batch handoff, so the message below is a voice-gate
decision prompt rather than a Batch 2 kickoff. Batch 2 does not start until the
gate is passed and ch01 is frozen as the register reference.

## Message to paste into the next chat

```
The Rebel — voice-gate decision (after Batch 1)

Batch 1 of The Rebel is done and waiting at the first-chapter voice gate (CLAUDE.md Step 0c). Read the built chapters (ch01 through ch07 of the title novella) in the attached EPUB and judge three things before ch01 becomes the FROZEN register reference for the rest of the book:

1. Voice. Literary contemporary English, restrained third person, dialogue set in quotation marks (the source runs dialogue unmarked). Is the register right for a serious espionage novel? Any drift toward pulp or toward stiffness?
2. Footnote density. This batch carries 35 notes (12 on the opening chapter, tapering), across history, institutions, material culture, and custom, for a reader with no background in modern China. Too many, too few, right?
3. Formatting. Chapter headings are the installment numbers under the part title "The Rebel"; a Principal Characters page and a four-section glossary sit in the back matter; footnotes pop up in Apple Books and Kindle.

If approved: freeze ch01 as check_register.py --ref, then run Batch B02 = The Rebel 8-14 (units ch08-ch14). If changes are wanted, name them and I will revise Batch 1 first (nothing downstream depends on it yet).
```

## What is DONE (do not redo)

- Step 0 survey: source ingested, book.json authored (51 units, four parts),
  skeleton EPUB green, batch plan approved (9 batches).
- Batch B01 = The Rebel 1-7 (ch01-ch07), 357 paragraphs, translated end to end.
  All checks green (parity, numbers, alignment, content/displacement, entity
  survival, anchors, apparatus). 35 footnotes, 51 glossary rows, Principal
  Characters page. EPUB rebuilt: qa_epub PASS, epubcheck 5.1.0 clean. Committed
  and pushed to claude/the-rebel. AWAITING THE VOICE GATE (Step 0c); ch01 is
  not yet frozen as the register reference.

## Tooling in place (do NOT revert)

- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched by setup.sh).
- data/noise.txt: project entries for non-quantitative source numerals
  (第二天, 一言不发, 一动不动, 十六铺, 八仙桥, 零星, 九宫, 三轮车), each commented.
  Extend as new number idioms surface; never noise a real quantity.
- scripts/apparatus_merge.py: patched so glossary rows are filed under their
  section (the row's "category" field, default "terms"), matching the nested
  {section:{hanzi:row}} shape glossary.json documents and that render_glossary,
  render_characters and check_content all read. Give every glossary row a
  "category" in the batch apparatus file (people / organizations / places /
  terms). The old flat-key behaviour broke the build; keep the fix.
- scripts/check_content.py: patched so name_map skips non-dict / "_"-prefixed
  top-level sections (e.g. _about). Run it with a docs/sources config:
  {"docs":{id:"out/<id>_reading.md"}, "sources":{id:"data/zh/<id>.txt"}}.
- No source-notes stream (the source carries none).

## Voice sheets (one per major character, written at first appearance)

- Lin Nansheng (林楠笙): the protagonist. Educated, controlled, near-silent
  under pressure; speaks in short flat sentences, states hard truths plainly
  ("The trouble is I have never killed anyone"). Interiority carried by
  narration, not speech; irony is dry and self-directed. After his wound he
  goes colder and blacker. Pinyin.
- Gu Shenyan (顾慎言): Lin's spymaster and former training-class director.
  The cultivated aesthete (symphonies, Peking opera, go, Baudelaire in French);
  speaks in measured aphorism and indirection ("we dance on the point of a
  knife"; "to forget is the finest remembrance"), warm on the surface, testing
  underneath. Never raises his voice. Pinyin.
- Zuo Qiuming (左秋明): Lin's fellow trainee, now a Juntong liaison officer.
  Brief, warm, professional; the mild traveler's smile over a hard core. Few
  lines, but the batch turns on his suicide rather than break under
  interrogation. Pinyin.
- Ding Mocun (丁默邨): the historical turncoat, director of No. 76, later a
  minister of the Wang regime. Cold, ironic, unhurried; enjoys the upper hand
  and needles his visitor ("at bottom you are still a Communist"). Speaks as a
  man who has already chosen his side and feels no need to justify it.
  Historical; pinyin (standard form).
- Zhu Yizhen (朱怡贞): the Communist agent, Lin's former student and lover.
  Proud, stubborn, wounded; alternates cold formality ("Please let go of my
  hand") with sudden breaks (the scream that ends ch02, the cut embroidery).
  Silence and needlework carry what she will not say. Endearment 贞贞 = Zhenzhen.
  Pinyin.
- Ji Zhongyuan (纪中原): Zhu's controller and cover-husband, a Communist
  professional posing as a seal-engraver. Quiet, patient, absolute about the
  primacy of the work ("intelligence comes before all else"); jealousy shows
  only as a dryness in the voice. Fakes his own death and returns. Pinyin.

## Where the book stands (story)

- The Rebel, installments 1-7. Lin Nansheng, a Juntong agent in occupied
  Shanghai, is shot in an ambush and smuggled to a Japanese army hospital in
  Hong Kong, his spine wound leaving him unable to feel pain. The narrative
  flashes back: his handler Gu Shenyan; the assassination of the collaborator
  Tong Zizhong at the Cathay Hotel; his re-entangled love with Zhu Yizhen, a
  Communist agent married in cover to her controller Ji Zhongyuan; their flight
  from No. 76's dragnet; the killing of the consul Kobayashi; the ambush at the
  City God Temple that leaves Zhu apparently dead and Lin crippled; Gu's night
  bargain with Ding Mocun to pull Lin out of Japanese hands. In Hong Kong Lin
  learns Ji Zhongyuan faked his death; his friend Zuo Qiuming is captured and
  takes his own life rather than talk; Ji hints Zhu may be alive (two coffins
  left the hospital). Lin is recalled to Chongqing to instruct at SACO; Ji
  gives him a poem-cipher for contact. Whether Zhu lives is the open thread.

## What is NEXT

- On voice-gate approval: freeze ch01 (check_register.py --ref), then
  B02 = The Rebel 8-14 (ch08-ch14). Do NOT start B02 before the gate.
- Batch plan after that: B03-B05 The Postman, B06-B07 Potassium Cyanide,
  B08-B09 Rouge (+ back matter and whole-book QA). Nine batches total.

## Settled renderings / carry-forward

- Cross-shelf (authority.json) forms in use: Wang Jingwei, Dai Li, the Juntong,
  the Cathay Hotel, Avenue Joffre, Suzhou Creek, Yuyuan Road, Nanjing Road,
  rickshaw, cheongsam, Chongqing. New this book: Ding Mocun, No. 76 / Jessfield
  Road, the Zhongtong, the Peace Army, SACO, the Tokko, Rue Ratard, the
  Zhonghua Ribao, The Young Companion, Ta Kung Pao. All in glossary.json.
- 贞贞 = Zhenzhen; Japanese speakers address Lin as "Pang-san" / "Lin-san"
  (庞桑 / 林桑) under his cover name Pang Jiajun. Kobayashi = 小林大介.
- Dialogue is unmarked in the source; set it in quotation marks in English.
  Chapter heading = installment number under the part title.
- COVER: keep the source's original cover (commissioner's instruction, B01).
  It is data/figs/cover00144.jpeg, reused byte-identical by the builder
  (verified: same SHA in the built EPUB). Do NOT replace or regenerate it.

## Open items for the read-through

- Confirm footnote density on the opening chapter feels right before it becomes
  the frozen reference (ch01 carries 12).
- The fur-store attribution note (ch01): confirm the Zhongtong-over-Juntong
  framing reads as intended (the source is defensible; the note says so).

## Environment / traps state

- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done again this session; expect it every batch).
- data/src is gitignored and regenerable by ingest_epub.py (run it if data/src
  is empty at the top of a batch). data/zh, out/*_en.json, out/*_reading.md and
  the ledgers are tracked; bilinguals are regenerable and not shipped.
- Source is clean simplified-Chinese digital text; no OCR, no set-off HTML
  formatting, no source notes. Doubled heading line per file (skip=2).
