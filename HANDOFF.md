# HANDOFF — The Whistling Wind (风萧萧) by Xu Xu

State: Batch B06 (ch26 through ch31: Chapters 26 to 31) is COMPLETE, checked, and
committed. The cumulative EPUB `out/The Whistling Wind.epub` has 32 of 60 chapters
translated (ch00 through ch31); the other 28 still link to their skeleton outlines
and the TOC stays fully navigable. Next up: Batch B07 = ch32 through ch36
(Chapters 32 to 36).

## Message to paste into the next chat

```
Whistling Wind B07 — Chapters 32 to 36 (ch32 through ch36).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Then do Batch B07 = units ch32 through ch36
(Chapters 32 to 36 of the novel; ~18,411 source chars) end to end, following the
per-batch pipeline in CLAUDE.md.

Concretely:
- The ingest is regenerable but NOT committed (data/src/ is gitignored). If
  data/src/ is missing in a fresh checkout, run scripts/ingest_epub.py source.epub
  once to repopulate it before you start.
- Read the batch's source text from data/src/ for each unit (ch32 =
  36_chapter34.txt, ch33 = 37_chapter35.txt, ch34 = 38_chapter36.txt, ch35 =
  39_chapter37.txt, ch36 = 40_chapter38.txt). Quote the source VERBATIM in the
  bilingual QC file; do not re-type or paraphrase it. The fastest safe way is the
  batch helper scripts/_zip_bilingual.py: author an English-only file (one paragraph
  per line, in order), and it pairs your English with the VERBATIM source paragraphs
  copied from data/src (stripping the UTF-8 BOM and the two duplicated chapter-numeral
  heading lines the source repeats), erroring if the paragraph counts differ. Then
  confirm with the whitespace-stripped char comparison of the joined '>' blockquotes
  vs the joined source paragraphs (used every batch).
- Translate to the register in CLAUDE.md: clean, flowing English narrative prose
  in the book's own first-person voice; all apparatus lives in the notes, never
  inline. Never invent bridging text and never silently drop material; if a
  passage is genuinely ambiguous or the source is cut/corrupt, footnote it and
  leave it visible. Render the recurring source digitization glitches to plain
  sense (and list them in PROGRESS), footnoting only genuine reading uncertainty.
- Author one aligned bilingual QC file out/<id>_bilingual.md per unit (a first
  line "## H2 Chapter N" for the title, then, for each source paragraph, a "> "
  blockquote line followed by one English paragraph; skip the duplicated
  chapter-number heading lines the source repeats; a lone source "──" divider
  line is rendered as a lone "—" paragraph, and verse is kept line-by-line).
  Generate the reading text and parity source with scripts/split_bilingual.py
  (pass the source chapter heading as the third argument, e.g. "三十二"). WATCH the
  paragraph count: _zip_bilingual.py errors on a mismatch — if it does, one English
  line has merged two source paragraphs (a common slip on tag-less dialogue where a
  paragraph ends with a colon "说：" and the quote is a separate source paragraph).
- Run the checks and record them in PROGRESS.md: check_numbers.py --noise
  data/noise.txt on each bilingual file; check_structure.py --config over the batch
  (build a small {docs,sources,notes,variants} config over the translated units, as
  B06 did in scratch/b06_check.json; scratch/ is gitignored, so regenerate it — and
  in the variants map put ONLY wrong forms in each value list, NEVER the canonical
  itself, or every correct occurrence is flagged as drift). Blind double translation
  on the analytical/lyrical passages, sampled on plain narration; round-trip
  back-translation as an omission check; a 3 to 5 percent random deep audit with the
  observed error rate reported. Extend data/noise.txt whenever the number check flags
  a non-quantity numeral (write down what and why).
- Number-check notes: the built-in NOISE strips clock times AND whole-hour "点钟"
  times; its bare-一 measure patterns AND its two 一-idiom patterns all carry a
  negative lookbehind, so compound numbers like 十一个 / 十一点钟 / 十一日 / 十一时
  survive (B04). B06 added, at the TOP block, r"[一二三四五六七八九]十多" (mirroring the
  existing 四十几): the built-in r"[十几幾]多" was eating the "十多" out of 五十多
  ("fifty-odd") and orphaning a 五 read as 5. Prefer noise/prose fixes over editing
  the script (a spelled "three hundred and forty" parses to 3/40/300, so write such
  figures as digits; a hyphen-joined "twenty-fourmo" parses only to 20, so write
  "twenty-four-mo"). LIVE GOTCHAS: the bare-一 measure rule strips "一次" out of the
  idiom 一次两次 and orphans the 两 (B05) — reword the English to carry the count
  rather than masking a real "twice" globally. Reduplicated count-idioms like 两两三三
  ("in twos and threes", B06) are noise, not quantities. Tenths fractions (十分之七
  etc.) are stripped by the built-in fraction pattern and are NOT re-verified by the
  check, so render them faithfully in the prose yourself. data/noise.txt already
  carries: 两样, 十足, 光芒万丈, a numeral+丈 pattern (丈 -> feet), the 四十二四十三
  artifact; the B04 additions (二房东 / 飘零 / 二○号 / [一二三四五]更 / 六角 / 大千世界);
  the B05 additions 两[手膝] / 连三接四 / 零碎; and the B06 additions 万物 ("all things";
  万≠10000), 两两三三, 畸零 ("odd/isolated"; 零≠0), 万国 (万国公墓; 万≠10000).
- Footnotes into notes.json (about 3 per chapter-equivalent; anchors must be
  verbatim substrings of the English prose, matched BEFORE markup - use ASCII
  apostrophes/quotes and the exact capitalisation of the prose; XHTML bodies use
  NUMERIC character references, never named entities - escape every non-ASCII
  codepoint to &#dec;, reuse that pattern). Numbering is continuous and assigned
  by the builder, so just append to each unit's list; B06 ended at note 56.
  Recurring subjects already have their note at first appearance in B01-B06 (Stephen,
  Bai Ping, Mei Yingzi, Helen, Mrs. Manfield, Mrs. Stephen, Dr. Philip, the Solitary
  Island, the Paramount, Renji Hospital, the narrator's name Xu, the Arcadia, West
  Lake landmarks, Geling, the National Academy of Art, Mario Paci, Jessfield Park,
  DD's Café, Route Prosper Paris, Tao Yuanming, the Palace of the Moon, Wu Zetian /
  the Western Empress Dowager, the Pacific war outbreak, the Pudong internment, the
  July 7 Incident, Sai Jinhua, Shitao, Hongkou, the Benner Inn, the Standford, the
  Fuyuan native bank, the Hailin Broadcasting Station, the narrator's alias Chen Ji,
  the International Cemetery, Isadora Duncan, the "true gold fears no fire" proverb,
  the Great World, etc.), so do NOT re-note them; footnote only genuinely new refs.
- Glossary discipline: glossary.json (100 rows) already fixes the whole cast and the
  Shanghai/Hangzhou geography, dance halls, restaurants, the cheongsam (旗袍), and the
  B06 additions (Nomura 野村, Rear Admiral Umetake 梅武, Chen Ji 陈寂, Dr. Gaolang 高朗,
  the Hailin Broadcasting Station 海邻广播电台, Weihaiwei Road 威海卫路, the Racecourse
  跑马厅, the International Cemetery 万国公墓, Jing'an Temple 静安寺, Malang Road 马浪路 =
  the colloquial short of Rue Brenier de Montmorand, Beiping 北平, the Huimei Hotel
  汇美饭店, Gaoye Road 高叶路, the Gaolang Hospital 高朗医院, the Yuanyutai 源裕泰, the
  Great World 大世界). REUSE those exact renderings; add a new row for every new proper
  noun / place / org / term with status (attested / provisional / decided) and
  attestation, deciding the one rendering before you romanize it. Fact-check any
  historical/real-world reference against real scholarship (Wikipedia / Baidu Baike /
  academic), never LLM-generated sources (never Grok/Grokipedia), and say
  corroborated / uncorroborated / contradicted.
- Rebuild the cumulative EPUB: python3 scripts/build_reading_epub.py
  "out/The Whistling Wind.epub" (the TOC stays pending-aware). Run
  python3 scripts/qa_epub.py "out/The Whistling Wind.epub" until green.
- Commit on the one working branch claude/the-whistling-wind. Rewrite HANDOFF.md
  so its first section is the paste-ready kickoff for Batch B08 = ch37 through ch41.
- Cite chapters, never page numbers. Do not pause for approval mid-batch.
- Deliver out/The Whistling Wind.epub to me as an attached file in the chat.
```

## Project facts a fresh session needs

- Deliverable filename: `out/The Whistling Wind.epub`. Working branch:
  `claude/the-whistling-wind` (one branch only; do not spin off others). If a
  session opens you on a different branch, move the work onto this one and delete
  the stray branch, per CLAUDE.md rule 2. (B01-B06 were each started on a stray
  branch and consolidated here; the stray branch is then deleted, local and
  remote.)
- Structure (see book.json): ch00 = About the Author (front matter);
  ch01..ch58 = the novel's 58 numbered chapters (源 一..五十八); ch59 =
  Impressions of Xu Xu (appendix). Units have no sub-sections.
- Pipeline artifacts that persist across batches: glossary.json (100 rows),
  notes.json (56 notes so far), data/noise.txt (project number-check noise),
  scripts/_zip_bilingual.py (the batch helper), scripts/check_numbers.py (its
  1-idiom and measure patterns carry negative lookbehinds so date/time compounds
  survive; B06 added r"[一二三四五六七八九]十多" at the top so 五十多 survives; see the
  B05 一次两次 gotcha above), data/src/ (all source text, regenerated by the ingest;
  gitignored), data/zh/ (parity source, regenerated per unit by split_bilingual.py),
  scratch/ (gitignored; put the check_structure config here, e.g. b06_check.json).
- Deferred source material to handle later, NOT dropped: `chapter61.html`
  (edition/imprint note) becomes the translated Colophon on the LAST batch via
  back_matter.json; `coverpage.html` abstract and `chapter1.html` (source TOC)
  are intentionally not body chapters (recorded in book.json `_source_note`).
- Title note (in the translator's note already): 风萧萧 echoes 风萧萧兮易水寒,
  the parting song for the assassin Jing Ke; keep that note of doomed sacrifice
  audible.

## Batch plan (approved)

| Batch | Units | Chars | Status |
|---|---|---|---|
| B01 | ch00 to ch08 | 18,512 | DONE |
| B02 | ch09 to ch14 | 19,469 | DONE |
| B03 | ch15 to ch17 | 16,230 | DONE |
| B04 | ch18 to ch21 | 19,962 | DONE |
| B05 | ch22 to ch25 | 18,788 | DONE |
| B06 | ch26 to ch31 | 20,716 | DONE |
| B07 | ch32 to ch36 | 18,411 | next |
| B08 | ch37 to ch41 | 17,945 | |
| B09 | ch42 to ch45 | 14,344 | |
| B10 | ch46 to ch48 | 17,009 | |
| B11 | ch49 to ch52 | 17,733 | |
| B12 | ch53 to ch57 | 20,620 | |
| B13 | ch58 to ch59 | 15,635 | (last: back matter + whole-book QA) |
