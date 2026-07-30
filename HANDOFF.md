# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batch 1 (ch01) COMPLETE: translated, checked,
footnoted, built, QA green, committed. Next is Batch 2 (ch02). 24 chapters plus
2 afterwords remain, one chapter per batch (B25 = the two afterwords together).

## Message to paste into the next chat

```
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batch 1 (ch01) are done; the
25-batch plan (one chapter per batch) is approved.

Do Batch 2 = ch02 (第二章 午初 / "Chapter Two. The Hour of the Horse, First Half
(11 a.m.)") end to end. NOTE: data/src/ and data/figs/ are gitignored and rebuild
from source.epub; if data/src/ is absent in a fresh clone, run
`python3 scripts/ingest_epub.py source.epub` first. Read the batch's source from
its text_file in book.json (data/src/04_text00005.txt); the source is
authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch02_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <title>'; combine the recurring opening epigraph into one pair and the
dateline into one pair as ch01 did; render the source's per-chapter time-gloss
final line as the source's own note). Then generate out/ch02_reading.md and the
parity source with `scripts/split_bilingual.py out/ch02_bilingual.md ch02 "第二章　午初"`.
Run `scripts/check_numbers.py out/ch02_bilingual.md --noise noise.txt` (extend
noise.txt or WORD_NUM in check_numbers.py when a NON-quantity numeral is flagged,
and record what you add and why; a real dropped number must still fail) and
`scripts/check_structure.py --pairs data/zh/ch02.txt out/ch02_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch02" (verbatim English anchors; XHTML bodies with numeric character
references, never named entities; ~3 per chapter, recurring subjects get their
note at first appearance across the whole book, so skip anything already noted in
ch01). Add any figure specs to figures.json only if the chapter has an image in
data/figs/. Rebuild with `scripts/build_reading_epub.py "out/The Longest Day in
Chang'an.epub"` so the pending-aware TOC links ch01 and ch02 content and every
other chapter's skeleton, then run `scripts/qa_epub.py "out/The Longest Day in
Chang'an.epub"` until green. Do a blind double-translation of a literary sample
and a round-trip back-translation of a number-dense sample (separate contexts),
and record the checks and the sample error rate in PROGRESS.md. Rewrite
HANDOFF.md with the Batch 3 (= ch03) kickoff message, commit, and push to branch
claude/the-longest-day-in-changan. Cite chapters/sections, never page numbers.
Never invent bridging text; footnote genuine ambiguity rather than smoothing it.
Do not pause for approval mid-batch. Deliver the rebuilt EPUB in chat as an
attached file.
```

## What is DONE (do not redo)

- Step 0 ingest + survey + skeleton EPUB, approved. 25-batch plan approved.
- Batch 1 = ch01, complete and committed: out/ch01_reading.md, data/zh/ch01.txt,
  12 notes in notes.json, glossary.json seeded, EPUB rebuilt, qa_epub PASS.
- noise.txt authored for check_numbers (project names/idioms/round numbers); its
  loader does NOT strip trailing comments, so keep every note on its own line.
- check_numbers.py WORD_NUM extended with teen ordinals (thirteenth..sixteenth).

## What is NEXT

- Batch 2 = ch02 (第二章 午初, ~16,686 source chars, data/src/04_text00005.txt).
  Then B03=ch03 ... B24=ch24, B25=ch25+ch26. See book.json's structure/batches.

## House style set by Batch 1 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged.
- Epigraph and dateline: one bilingual pair each. The source's per-chapter
  time-gloss (e.g. "上午10时。巳，又名日禺…") is rendered as the SOURCE's own note,
  in italics, marked as the source's, distinct from translator's notes.
- Names: pinyin, one decided rendering per referent, all in glossary.json.
  Recurring items already decided in ch01 (Zhang Xiaojing, Li Bi, the Jing'an
  Bureau, the Lüben Guards, watchtowers, buliang, Wolf Guards, shichen, the West
  Market, Tianbao, etc.) must be reused verbatim; grep the glossary before
  romanizing anything new.
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name, an idiom, a round number spelled out in English),
  extend noise.txt (own-line comments) or WORD_NUM, and say so in PROGRESS.

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches; if a session starts on another branch, move the work
  onto this one. (A harness note may name a different branch; CLAUDE.md rule 2
  and the commissioner override it.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships. Note anchors must be verbatim English
  substrings or the build refuses. XHTML note bodies use numeric character
  references, never named entities. The builder inserts note anchors BEFORE
  markup substitution.
- Every source chapter body opens with the same besieged-city epigraph and a
  dateline; keep both. Cite by chapter, never by page.
