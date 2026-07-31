# HANDOFF — The Whistling Wind (风萧萧) by Xu Xu

State: Step 0 (ingest + survey) complete and APPROVED. Batch plan is the 13
batches in `book.json` "batches" (each <= 21,000 source chars). No chapter is
translated yet. Next up: Batch 1.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Then do Batch B01 = units ch00 through ch08
(About the Author + Chapters 1 to 8 of the novel; ~18,512 source chars) end to
end, following the per-batch pipeline in CLAUDE.md.

Concretely:
- Read the batch's source text from data/src/ for each unit (ch00 =
  03_chapter2.txt, ch01 = 05_chapter3.txt, ch02 = 06_chapter4.txt,
  ch03 = 07_chapter5.txt, ch04 = 08_chapter6.txt, ch05 = 09_chapter7.txt,
  ch06 = 10_chapter8.txt, ch07 = 11_chapter9.txt, ch08 = 12_chapter10.txt).
  Quote the source VERBATIM in the bilingual QC file; do not re-type or
  paraphrase it.
- Translate to the register in CLAUDE.md: clean, flowing English narrative
  prose in the book's own first-person voice; all apparatus lives in the notes,
  never inline. Never invent bridging text and never silently drop material; if
  a passage is genuinely ambiguous or the source is cut/corrupt, footnote it and
  leave it visible.
- Author one aligned bilingual QC file out/<id>_bilingual.md per unit (source
  '>' blockquote line, English paragraph beneath), and generate the reading text
  and parity source with scripts/split_bilingual.py. The bilingual file is QC
  only and never ships.
- Run the checks and record them in PROGRESS.md: check_numbers.py on each
  bilingual file, check_structure.py --pairs on each unit; blind double
  translation on the analytical/lyrical passages, sampled on plain narration;
  round-trip back-translation as an omission check; a 3 to 5 percent random deep
  audit with the observed error rate reported.
- Footnotes into notes.json (~3 per chapter-equivalent; anchors must be verbatim
  substrings of the English prose; XHTML bodies use NUMERIC character
  references, never named entities). Recurring subjects get their note at first
  appearance. Glossary rows into glossary.json for every proper noun / place /
  org / term, with status (attested / provisional / decided) and attestation;
  DECIDE each recurring name's one rendering before romanizing it. The narrator,
  Bai Ping (白苹), Mei Yingzi (梅瀛子), Helen (海伦), and Stephen all appear early
  in Chapter 1 (the party invitation) and Chapter 2 onward: fix them in the
  glossary first. Fact-check any historical/real-world reference against real
  scholarship (Wikipedia / Baidu Baike / academic), never LLM-generated
  sources, and say corroborated / uncorroborated / contradicted.
- Rebuild the cumulative EPUB: python3 scripts/build_reading_epub.py
  "out/The Whistling Wind.epub" (the TOC stays pending-aware: it links the
  translated units and still links every not-yet-translated unit to its
  skeleton outline). Run python3 scripts/qa_epub.py "out/The Whistling Wind.epub"
  until green.
- Commit. Rewrite HANDOFF.md so its first section is the paste-ready kickoff for
  Batch B02 = ch09 through ch14.
- Cite chapters, never page numbers. Do not pause for approval mid-batch.
- Deliver out/The Whistling Wind.epub to me as an attached file in the chat.
```

## Project facts a fresh session needs

- Deliverable filename: `out/The Whistling Wind.epub`. Working branch:
  `claude/the-whistling-wind` (one branch only; do not spin off others).
- Structure (see book.json): ch00 = About the Author (front matter);
  ch01..ch58 = the novel's 58 numbered chapters (源 一..五十八); ch59 =
  Impressions of Xu Xu (appendix). Units have no sub-sections.
- Metadata is already authored in book.json and emitted by the builder
  (Kindle / Apple Books: file-as sort keys, MARC aut role, subjects,
  description, color cover). Leave `translator` blank unless the commissioner
  supplies a name.
- Deferred source material to handle later, NOT dropped: `chapter61.html`
  (edition/imprint note) becomes the translated Colophon on the LAST batch via
  back_matter.json; `coverpage.html` abstract and `chapter1.html` (source TOC)
  are intentionally not body chapters (recorded in book.json `_source_note`).
- Title note for the glossary/translator's note: 风萧萧 echoes 风萧萧兮易水寒,
  the parting song for the assassin Jing Ke; keep that note of doomed sacrifice
  audible.

## Batch plan (approved)

| Batch | Units | Chars |
|---|---|---|
| B01 | ch00 to ch08 | 18,512 |
| B02 | ch09 to ch14 | 19,469 |
| B03 | ch15 to ch17 | 16,230 |
| B04 | ch18 to ch21 | 19,962 |
| B05 | ch22 to ch25 | 18,788 |
| B06 | ch26 to ch31 | 20,716 |
| B07 | ch32 to ch36 | 18,411 |
| B08 | ch37 to ch41 | 17,945 |
| B09 | ch42 to ch45 | 14,344 |
| B10 | ch46 to ch48 | 17,009 |
| B11 | ch49 to ch52 | 17,733 |
| B12 | ch53 to ch57 | 20,620 |
| B13 | ch58 to ch59 | 15,635 |
