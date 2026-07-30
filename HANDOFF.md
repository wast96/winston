# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) COMPLETE and approved. The batch plan is
approved: 25 batches, one chapter per batch (B01=ch01 ... B24=ch24), plus
B25 = the two afterwords. Batch 1 has not started yet.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 is done and the 25-batch plan is
approved (one chapter per batch).

Do Batch 1 = ch01 (第一章 巳正 / "Chapter One. The Hour of the Snake, Second Half
(10 a.m.)") end to end. Read the batch's source from its text_file in book.json
(data/src/02_text00003.txt); the source is authoritative, quote it verbatim in
the bilingual QC file and render it faithfully and in full. Author one aligned
bilingual QC file out/ch01_bilingual.md (source '>' blockquote line, English
paragraph beneath; headings tagged), then generate out/ch01_reading.md and the
parity source with scripts/split_bilingual.py. Run scripts/check_numbers.py and
scripts/check_structure.py. Add footnotes to notes.json (verbatim English
anchors; XHTML bodies with numeric character references), glossary rows to
glossary.json (decide one rendering per referent BEFORE romanizing; Zhang
Xiaojing, Li Bi, Tianbao, Chang'an, the West Market, the shichen system, etc.),
and any figure specs to figures.json (reuse images already in data/figs/).
Rebuild with scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"
so the pending-aware TOC links ch01's content and every other chapter's skeleton,
then run scripts/qa_epub.py until green. Record the checks in PROGRESS.md, rewrite
HANDOFF.md with the Batch 2 (= ch02) kickoff message, commit, and push to branch
claude/the-longest-day-in-changan. Cite chapters/sections, never page numbers.
Never invent bridging text; footnote genuine ambiguity rather than smoothing it.
Do not pause for approval mid-batch. Deliver the rebuilt EPUB in chat as an
attached file.
```

## What is DONE (do not redo)

- Step 0 ingest: `scripts/ingest_epub.py source.epub` run; text in `data/src/`,
  images in `data/figs/`, `out/INGEST.md` and `book.draft.json` written.
- `book.json` authored: 24 numbered chapters (ch01-ch24), each MERGED from the
  source's numbered-heading file + time-marker body file, plus 2 afterwords
  (ch25, ch26). Five pirate-site ad interstitials dropped. English chapter
  titles gloss each traditional half-shichen with its modern clock time.
- Kindle/Apple-Books OPF metadata added to `scripts/build_reading_epub.py`
  (bilingual title/creator with file-as + MARC roles, languages, publisher,
  date, description, BISAC-style subjects, source ISBNs) and an embedded cover
  (`data/figs/Image00010.jpg`) via EPUB3 `cover-image` + legacy `<meta cover>`.
- `out/SURVEY.md` written; skeleton EPUB built; `qa_epub.py` PASS; committed and
  pushed. Batch plan approved (25 batches).

## What is NEXT

- Batch 1 = ch01 (第一章 巳正, ~19,105 source chars). Then B02=ch02 ...
  B24=ch24, B25=ch25+ch26. See the batches array in book.json.

## Open items for the read-through

- English chapter titles ("The Hour of the Snake, Second Half (10 a.m.)" etc.)
  are provisional; confirm the register once Batch 1 sets the house style.
- No glossary decided yet: the recurring names (张小敬 Zhang Xiaojing, 李泌 Li Bi,
  靖安司, 望楼, 大案牍术, 天宝三载, 上元节, the twelve shichen) must each get one
  decided rendering in glossary.json at first appearance in Batch 1.

## State / traps

- Source structure: each logical chapter is TWO source files (a `第X章` heading
  page then the body); book.json already merges them, so translate from each
  unit's `text_file` (the body). The heading files are just the chapter number.
- Every chapter body opens with the same recurring epigraph (the besieged-city
  image: 无数黑骑…狼烟正直直刺向昏黄的天空) followed by a dateline
  (天宝三载，元月十四日，<时辰> / 长安，长安县，<place>). Keep the epigraph and
  dateline; decide once how to render the shichen in the dateline.
- Working branch is `claude/the-longest-day-in-changan`. A duplicate remote ref
  `claude/the-longest-day-in-changan-lkw0ih` (same commit) could not be deleted
  from here (egress policy 403); it is harmless. Push only to the working branch.
- Bilingual QC file never ships. Note anchors must be verbatim English
  substrings or the build refuses. XHTML note bodies use numeric character
  references, never named entities.
