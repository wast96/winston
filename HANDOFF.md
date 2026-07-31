# HANDOFF — The Whistling Wind (风萧萧) by Xu Xu

State: Batch B02 (ch09 through ch14: Chapters 9 to 14) is COMPLETE, checked, and
committed. The cumulative EPUB `out/The Whistling Wind.epub` has 15 of 60 chapters
translated (ch00 through ch14); the other 45 still link to their skeleton outlines
and the TOC stays fully navigable. Next up: Batch B03 = ch15 through ch17
(Chapters 15 to 17).

## Message to paste into the next chat

```
Whistling Wind B03 — Chapters 15 to 17 (ch15 through ch17).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Then do Batch B03 = units ch15 through ch17
(Chapters 15 to 17 of the novel; ~16,230 source chars) end to end, following the
per-batch pipeline in CLAUDE.md.

Concretely:
- The ingest is regenerable but NOT committed (data/src/ is gitignored). If
  data/src/ is missing in a fresh checkout, run scripts/ingest_epub.py source.epub
  once to repopulate it before you start.
- Read the batch's source text from data/src/ for each unit (ch15 =
  19_chapter17.txt, ch16 = 20_chapter18.txt, ch17 = 21_chapter19.txt). NOTE:
  ch15 is a long chapter (~10,004 source chars), the two others are short. Quote
  the source VERBATIM in the bilingual QC file; do not re-type or paraphrase it.
  A quick mechanical confirmation is the whitespace-stripped character comparison
  used in B01/B02 (strip the UTF-8 BOM and the two duplicated chapter-numeral
  heading lines the source repeats, then compare the joined '>' blockquotes to
  the joined source paragraphs).
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
  (pass the source chapter heading as the third argument, e.g. "十五").
- Run the checks and record them in PROGRESS.md: check_numbers.py --noise
  data/noise.txt on each bilingual file; check_structure.py --config over the
  batch (or --pairs per unit); blind double translation on the
  analytical/lyrical passages, sampled on plain narration; round-trip
  back-translation as an omission check; a 3 to 5 percent random deep audit with
  the observed error rate reported. Extend data/noise.txt whenever the number
  check flags a non-quantity numeral (write down what and why). The built-in
  check_numbers NOISE now strips clock times AND whole-hour "点钟" times, and its
  two bare-一 measure patterns carry a negative lookbehind so compound numbers
  like 十一个 survive (both added in B02); keep that in mind before "fixing" a
  flag by editing the script.
- Footnotes into notes.json (about 3 per chapter-equivalent; anchors must be
  verbatim substrings of the English prose, matched BEFORE markup — use ASCII
  apostrophes/quotes and the exact capitalisation of the prose; XHTML bodies use
  NUMERIC character references, never named entities). Numbering is continuous
  and assigned by the builder, so just append to each unit's list; B02 ended at
  note 28. Recurring subjects already have their note at first appearance in
  B01/B02 (Stephen, Bai Ping, Mei Yingzi, Helen, the Solitary Island, the
  Paramount, the narrator's name Xu (used since ch07, deliberately NOT noted),
  the Arcadia, West Lake landmarks, Geling, the National Academy of Art, etc.),
  so do NOT re-note them; footnote only genuinely new references.
- Glossary discipline: glossary.json (63 rows) already fixes the whole cast and
  the Shanghai/Hangzhou geography, dance halls, restaurants and the cheongsam
  (旗袍) rendering. REUSE those exact renderings; add a new row for every new
  proper noun / place / org / term with status (attested / provisional /
  decided) and attestation, deciding the one rendering before you romanize it.
  Fact-check any historical/real-world reference against real scholarship
  (Wikipedia / Baidu Baike / academic), never LLM-generated sources (never
  Grok/Grokipedia), and say corroborated / uncorroborated / contradicted.
- Rebuild the cumulative EPUB: python3 scripts/build_reading_epub.py
  "out/The Whistling Wind.epub" (the TOC stays pending-aware). Run
  python3 scripts/qa_epub.py "out/The Whistling Wind.epub" until green.
- Commit on the one working branch claude/the-whistling-wind. Rewrite HANDOFF.md
  so its first section is the paste-ready kickoff for Batch B04 = ch18 through ch21.
- Cite chapters, never page numbers. Do not pause for approval mid-batch.
- Deliver out/The Whistling Wind.epub to me as an attached file in the chat.
```

## Project facts a fresh session needs

- Deliverable filename: `out/The Whistling Wind.epub`. Working branch:
  `claude/the-whistling-wind` (one branch only; do not spin off others). If a
  session opens you on a different branch, move the work onto this one and delete
  the stray branch, per CLAUDE.md rule 2. (B01 and B02 were each started on a
  stray `claude/batch-...` branch and consolidated here; the stray branch is then
  deleted, local and remote.)
- Structure (see book.json): ch00 = About the Author (front matter);
  ch01..ch58 = the novel's 58 numbered chapters (源 一..五十八); ch59 =
  Impressions of Xu Xu (appendix). Units have no sub-sections.
- Pipeline artifacts that persist across batches: glossary.json (63 rows),
  notes.json (28 notes so far), data/noise.txt (project number-check noise),
  data/src/ (all source text, regenerated by the ingest; gitignored),
  data/zh/ (parity source, regenerated per unit by split_bilingual.py).
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
| B03 | ch15 to ch17 | 16,230 | next |
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
