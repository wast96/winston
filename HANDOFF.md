# HANDOFF — The Whistling Wind (风萧萧) by Xu Xu

State: Batch B01 (ch00 through ch08: About the Author + Chapters 1 to 8) is
COMPLETE, checked, and committed. The cumulative EPUB
`out/The Whistling Wind.epub` has 9 of 60 chapters translated; the other 51
still link to their skeleton outlines and the TOC stays fully navigable. Next up:
Batch B02 = ch09 through ch14 (Chapters 9 to 14).

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Then do Batch B02 = units ch09 through ch14
(Chapters 9 to 14 of the novel; ~19,469 source chars) end to end, following the
per-batch pipeline in CLAUDE.md.

Concretely:
- Read the batch's source text from data/src/ for each unit (ch09 =
  13_chapter11.txt, ch10 = 14_chapter12.txt, ch11 = 15_chapter13.txt,
  ch12 = 16_chapter14.txt, ch13 = 17_chapter15.txt, ch14 = 18_chapter16.txt).
  Quote the source VERBATIM in the bilingual QC file; do not re-type or
  paraphrase it. (The ingest is already run; data/src/ is populated. A quick
  mechanical way to confirm verbatim quotation is the whitespace-stripped
  character comparison used in B01, recorded in PROGRESS.md.)
- Translate to the register in CLAUDE.md: clean, flowing English narrative
  prose in the book's own first-person voice; all apparatus lives in the notes,
  never inline. Never invent bridging text and never silently drop material; if
  a passage is genuinely ambiguous or the source is cut/corrupt, footnote it and
  leave it visible.
- Author one aligned bilingual QC file out/<id>_bilingual.md per unit (a first
  line "## H2 Chapter N" for the title, then, for each source paragraph, a "> "
  blockquote line followed by one English paragraph; skip the duplicated
  chapter-number heading lines the source repeats). Generate the reading text
  and parity source with scripts/split_bilingual.py (pass the source chapter
  heading as the third argument, e.g. "九"). The bilingual file is QC only and
  never ships.
- Run the checks and record them in PROGRESS.md: check_numbers.py --noise
  data/noise.txt on each bilingual file; check_structure.py --pairs on each
  unit (or one --config run over the batch); blind double translation on the
  analytical/lyrical passages, sampled on plain narration; round-trip
  back-translation as an omission check; a 3 to 5 percent random deep audit
  with the observed error rate reported. Extend data/noise.txt whenever the
  number check flags a non-quantity numeral (write down what and why); the
  built-in NOISE now also strips clock times and durations, added in B01.
- Footnotes into notes.json (about 3 per chapter-equivalent; anchors must be
  verbatim substrings of the English prose; XHTML bodies use NUMERIC character
  references, never named entities). Numbering is continuous and assigned by
  the builder, so just append to each unit's list; B01 ended at note 16.
  Recurring subjects already have their note at first appearance in B01 (Stephen,
  Bai Ping, Mei Yingzi, Helen, the Solitary Island, etc.), so do NOT re-note
  them; footnote only genuinely new references.
- Glossary discipline: glossary.json already fixes the narrator's circle
  (Stephen, Bai Ping = 白苹, Mei Yingzi = 梅瀛子, Helen Manfield = 海伦·曼斐儿,
  Mrs. Stephen, Dr. Philip = 费利普/菲利浦, Mr. Gao = 高, and the Shanghai places
  and dance halls). REUSE those exact renderings; add a new row for every new
  proper noun / place / org / term with status (attested / provisional /
  decided) and attestation, deciding the one rendering before you romanize it.
  Fact-check any historical/real-world reference against real scholarship
  (Wikipedia / Baidu Baike / academic), never LLM-generated sources, and say
  corroborated / uncorroborated / contradicted.
- Rebuild the cumulative EPUB: python3 scripts/build_reading_epub.py
  "out/The Whistling Wind.epub" (the TOC stays pending-aware). Run
  python3 scripts/qa_epub.py "out/The Whistling Wind.epub" until green.
- Commit on the one working branch claude/the-whistling-wind. Rewrite HANDOFF.md
  so its first section is the paste-ready kickoff for Batch B03 = ch15 through
  ch17.
- Cite chapters, never page numbers. Do not pause for approval mid-batch.
- Deliver out/The Whistling Wind.epub to me as an attached file in the chat.
```

## Project facts a fresh session needs

- Deliverable filename: `out/The Whistling Wind.epub`. Working branch:
  `claude/the-whistling-wind` (one branch only; do not spin off others). If a
  session opens you on a different branch, move the work onto this one and
  delete the stray branch, per CLAUDE.md rule 2. (B01 was started on a stray
  `claude/batch-...` branch and consolidated here.)
- Structure (see book.json): ch00 = About the Author (front matter);
  ch01..ch58 = the novel's 58 numbered chapters (源 一..五十八); ch59 =
  Impressions of Xu Xu (appendix). Units have no sub-sections.
- Pipeline artifacts that persist across batches: glossary.json (33 rows so
  far), notes.json (16 notes so far), data/noise.txt (project number-check
  noise), data/src/ (all source text, from the ingest), data/zh/ (parity
  source, regenerated per unit by split_bilingual.py).
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
| B02 | ch09 to ch14 | 19,469 | next |
| B03 | ch15 to ch17 | 16,230 | |
| B04 | ch18 to ch21 | 19,962 | |
| B05 | ch22 to ch25 | 18,788 | |
| B06 | ch26 to ch31 | 20,716 | |
| B07 | ch32 to ch36 | 18,411 | |
| B08 | ch37 to ch41 | 17,945 | |
| B09 | ch42 to ch45 | 14,344 | |
| B10 | ch46 to ch48 | 17,009 | |
| B11 | ch49 to ch52 | 17,733 | |
| B12 | ch53 to ch57 | 20,620 | |
| B13 | ch58 to ch59 | 15,635 | (last: back matter + whole-book QA) |
