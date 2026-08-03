# HANDOFF — The Whistling Wind (风萧萧) by Xu Xu

State: Batch B12 (ch53 through ch57: Chapters 53 to 57) is COMPLETE, checked, and
committed. The cumulative EPUB `out/The Whistling Wind.epub` has 58 of 60 chapters
translated (ch00 through ch57); the last 2 (ch58 and ch59) still link to their skeleton
outlines and the TOC stays fully navigable. Next up: Batch B13 = ch58 through ch59, the
LAST batch (back matter plus a whole-book QA pass and a completion report).

## Message to paste into the next chat

```
Whistling Wind B13 — Chapter 58 and Impressions of Xu Xu (ch58 through ch59). THE LAST BATCH.

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Then do Batch B13 = units ch58 and ch59 (Chapter 58 of the
novel plus the appendix "Impressions of Xu Xu"; ~15,635 source chars) end to end, following
the per-batch pipeline in CLAUDE.md, AND finish the book: render the deferred Colophon,
run a whole-book QA pass, and write a COMPLETION REPORT instead of another handoff.

Concretely:
- The ingest is regenerable but NOT committed (data/src/ is gitignored). If data/src/ is
  missing in a fresh checkout, run scripts/ingest_epub.py source.epub once to repopulate it
  before you start.
- Read the batch's source text from data/src/ for each unit (ch58 = 62_chapter60.txt,
  heading 五十八; ch59 = 63_chapter62.txt, the appendix 徐訏印象 "Impressions of Xu Xu", which
  is NOT a numbered chapter, so it has no duplicated numeral heading line to skip). Quote the
  source VERBATIM in the bilingual QC file; do not re-type or paraphrase it. The fastest safe
  way is scripts/_zip_bilingual.py for the numbered chapter (ch58): author an English-only file
  (one paragraph per line, in order) and it pairs your English with the VERBATIM source
  paragraphs, stripping the BOM and the two duplicated numeral heading lines, erroring on a
  count mismatch. NOTE: ch59 (徐訏印象) is an appendix, so its source does NOT repeat a numeral
  heading; _zip_bilingual.py asserts paras[0]==paras[1]==<head>, which will FAIL on ch59. For
  ch59 either author the bilingual file by hand (one "> " source line + one English paragraph
  per source paragraph, first line "## H2 Impressions of Xu Xu"), or copy _zip_bilingual.py to a
  scratch variant that skips only the ONE title line ch59 actually has. Confirm both with the
  whitespace-stripped char comparison of the joined '>' blockquotes vs the joined source
  paragraphs (used every batch).
- ch58 is the novel's penultimate chapter (Helen and the narrator; the resolve formed at the
  end of ch57); ch59 "Impressions of Xu Xu" (徐訏印象) is an appreciative APPENDIX ESSAY about
  the author, by another hand (like ch00 "About the Author" it is not Xu Xu's own narration, so
  render it as expository prose, not in the novel's first-person voice, and footnote any real
  people/works it names, checked against scholarship). Watch: ch59, being critical/biographical
  prose, will name writers, works, and places that earn glossary rows and notes.
- Translate to the register in CLAUDE.md: clean, flowing English; ch58 in the book's own
  first-person novelistic voice, ch59 in an expository register. All apparatus in the notes,
  never inline. Never invent bridging text and never silently drop material; if a passage is
  genuinely ambiguous or the source is cut/corrupt, footnote it and leave it visible. Render the
  recurring source digitization glitches to plain sense (and LIST them in PROGRESS), footnoting
  only genuine reading uncertainty. (B12 saw several: 年强力壮 for 身强力壮/年轻力壮; 硕命 for
  殒命; 相传 for 相信; 纯悉 for 纯熟; 一气张 for 一张; 之肘 for 之时; a mismatched guillemet
  『...『; a full-width variant period ．. All rendered to sense, none footnoted.)
- Author one aligned bilingual QC file out/<id>_bilingual.md per unit (first line "## H2 <title>"
  for the title, then per source paragraph a "> " blockquote line followed by one English
  paragraph; skip the duplicated chapter-number heading lines the source repeats on a numbered
  chapter; a lone source "──" divider is a lone "—" paragraph; verse kept line-by-line).
  Generate the reading text and parity source with scripts/split_bilingual.py (pass the source
  heading as the third argument, e.g. "五十八" for ch58, and the appendix title for ch59). WATCH
  the paragraph count: a mismatch means one English line merged two source paragraphs (common on
  tag-less dialogue where a paragraph ends "说：" and the quote is its own source paragraph), or
  (in a long essay) a whole paragraph was dropped. Also watch source dittography and
  multi-speaker paragraphs (render all quotes of one source paragraph on the one English line).
- Run the checks and record them in PROGRESS.md: check_numbers.py --noise data/noise.txt on each
  bilingual file; check_structure.py --config over the WHOLE book (all 60 translated units,
  ch00 through ch59; build the {docs,sources,notes,variants} config in scratch/, as B12 did in
  scratch/b12_check.json; scratch/ is gitignored, so regenerate it, and in the variants map put
  ONLY wrong forms in each value list, NEVER the canonical, or every correct occurrence is
  flagged as drift). Blind double translation on the analytical/lyrical passages (ch59's
  criticism especially), sampled on plain narration; round-trip back-translation as an omission
  check; a 3 to 5 percent random deep audit with the observed error rate reported. Extend
  data/noise.txt whenever the number check flags a non-quantity numeral (write down what and
  why).
- Number-check notes: the built-in NOISE strips clock times AND whole-hour "点钟" times; 两/兩
  are in the top clock/duration classes (两点四十分 / 两点钟 / 两分钟 strip whole). Bare-一 measure
  and 一-idiom patterns carry negative lookbehinds so date/time compounds survive (十一点钟 /
  十一日 / 十一时). NOTE clock caveat: "点半" (half past) and "时" times are NOT stripped (五点半 ->
  5, 十二点半 -> 12, 十一时 -> 11 survive as bare numerals and must appear in the English); bare
  十一点 / 十一点多 likewise survive as 11. WORD_NUM carries the ordinals through twentieth /
  twenty-third and MONTHS maps january..december to 1..12; add the next such ordinal the same way
  if an essay date needs it. Prefer noise/prose fixes over editing the script (write "three
  hundred and forty" as digits; 十来个 as "ten or so"). data/noise.txt already carries the whole
  B01-B12 accumulation, incl. the B12 additions: 零票 (loose notes, 零 not 0), 六安 (the Lu'an
  place name, 六 not 6), and the kinship titles 三叔 / 二婶 / 三妹 (the numeral ranks the kin, not
  a count). ch59, an essay, may cite years (positional forms like 一九XX年 are digit strings, not
  summed) and dates; render them faithfully and let the number check confirm.
- Footnotes into notes.json (about 3 per chapter-equivalent; anchors must be verbatim substrings
  of the English prose, matched BEFORE markup, so use ASCII apostrophes/quotes and the exact
  capitalisation of the prose; XHTML bodies use NUMERIC character references, never named
  entities, so escape every non-ASCII codepoint to &#dec;, reuse scratch/add_notes.py's esc()).
  Numbering is continuous and assigned by the BUILDER from anchor position in reading order, so
  just append to each unit's list. B12 ended at note 93. Recurring subjects already have their
  note at first appearance in B01-B12 (the whole cast and geography; the escape sequence's
  Cishan's Third Uncle / Xiao Heizi / Bingfu / the kinship numbering (note 84), Rue du Consulat
  (87), the Tao-residence label (88), the 1943 surrender dream (89), Third Sister (90), Bai
  Ping's keepsakes (91), the Hōdōbu press bureau (92), the Miko song-code (93)), so do NOT
  re-note them; footnote only genuinely new refs (ch59's essay will bring most of the new ones).
- Glossary discipline: glossary.json (150 rows) fixes the whole cast and geography, incl. the
  B12 additions (people: 丙福 Bingfu, 慈珊的三叔 Cishan's Third Uncle, 小黑子 Xiao Heizi; places:
  法大马路 Rue du Consulat, 六安旅社 the Lu'an Hotel, 戈登路 Gordon Road, 新世界 the New World,
  皇宫饭店 the Palace Hotel). REUSE those exact renderings; add a new row for every new proper
  noun / place / org / term with status (attested / provisional / decided) and attestation,
  deciding the one rendering before you romanize it. Fact-check any historical/real-world
  reference against real scholarship (Wikipedia / Baidu Baike / academic), never LLM-generated
  sources (never Grok/Grokipedia), and say corroborated / uncorroborated / contradicted.
- BACK MATTER (this batch only): render the deferred Colophon from the source's imprint page
  (data/src/*chapter61*; recorded in book.json _source_note). The builder renders a colophon
  ONLY when back_matter.json has a top-level "colophon" key: rename its "_colophon_schema" ->
  "colophon" and fill it from the imprint page (title_zh 風蕭蕭 / 风萧萧, author_zh 徐訏, and the
  publication note: 成都东方书店 1944 / 民国三十三年, and the 上海夜窗书屋 1949 edition; give a
  translated notice_en / date_en). The Translator's Note (book.json translator_note) and the
  glossary already render as back matter; confirm they read as final.
- Rebuild the cumulative EPUB: python3 scripts/build_reading_epub.py "out/The Whistling Wind.epub"
  (now all 60 chapters translated, plus the Colophon). Run python3 scripts/qa_epub.py
  "out/The Whistling Wind.epub" until green.
- WHOLE-BOOK QA (last batch): after the final build, do a whole-book pass per CLAUDE.md's
  "Definition of done": qa_epub PASS across the full spine; TOC nested and fully linked; every
  note ref has a body and backlink and numbering is sequential; glossary and Translator's Note
  current; the Colophon present. Spot-grep the built units for any stray old/variant renderings.
- Commit on the one working branch claude/the-whistling-wind. Instead of another handoff, write a
  COMPLETION REPORT (in HANDOFF.md or a COMPLETION.md): batches done, final counts (chapters,
  notes, glossary rows), checks run book-wide and their results, and any residual provisional
  readings a reader should know about.
- Cite chapters, never page numbers. Do not pause for approval mid-batch.
- Deliver out/The Whistling Wind.epub to me as an attached file in the chat.
```

## Project facts a fresh session needs

- Deliverable filename: `out/The Whistling Wind.epub`. Working branch:
  `claude/the-whistling-wind` (one branch only; do not spin off others). If a session opens
  you on a different branch, move the work onto this one and delete the stray branch, per
  CLAUDE.md rule 2. (Every batch B01-B12 was started on a differently named branch and
  consolidated onto `claude/the-whistling-wind`; the stray branch is then deleted, local and
  remote.)
- Structure (see book.json): ch00 = About the Author (front matter); ch01..ch58 = the
  novel's 58 numbered chapters (源 一..五十八); ch59 = Impressions of Xu Xu (appendix). Units
  have no sub-sections.
- Pipeline artifacts that persist across batches: glossary.json (150 term rows), notes.json
  (93 notes so far), data/noise.txt (project number-check noise, B01-B12 accumulation),
  scripts/_zip_bilingual.py (the batch helper; asserts the two duplicated numeral heading
  lines, so an un-numbered appendix like ch59 needs a hand-built bilingual or a scratch variant),
  scripts/check_numbers.py, data/src/ (all source text, regenerated by the ingest; gitignored),
  data/zh/ (parity source, regenerated per unit by split_bilingual.py; gitignored), scratch/
  (gitignored; put the check_structure config and the add_notes/add_glossary helpers there).
- Deferred source material still to handle on B13, NOT dropped: `chapter61.html` (the 45-char
  edition/imprint note) becomes the translated Colophon back-matter via back_matter.json.
  `coverpage.html` abstract and `chapter1.html` (source TOC) are intentionally not body chapters
  (recorded in book.json `_source_note`).
- Title note (in the Translator's Note already): 风萧萧 echoes 风萧萧兮易水寒, the parting song
  for the assassin Jing Ke; keep that note of doomed sacrifice audible.

## Batch plan (approved)

| Batch | Units | Chars | Status |
|---|---|---|---|
| B01 | ch00 to ch08 | 18,512 | DONE |
| B02 | ch09 to ch14 | 19,469 | DONE |
| B03 | ch15 to ch17 | 16,230 | DONE |
| B04 | ch18 to ch21 | 19,962 | DONE |
| B05 | ch22 to ch25 | 18,788 | DONE |
| B06 | ch26 to ch31 | 20,716 | DONE |
| B07 | ch32 to ch36 | 18,411 | DONE |
| B08 | ch37 to ch41 | 17,945 | DONE |
| B09 | ch42 to ch45 | 14,344 | DONE |
| B10 | ch46 to ch48 | 17,009 | DONE |
| B11 | ch49 to ch52 | 17,733 | DONE |
| B12 | ch53 to ch57 | 20,620 | DONE |
| B13 | ch58 to ch59 | 15,635 | next (last: back matter + whole-book QA + completion report) |
