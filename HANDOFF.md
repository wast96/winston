# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-2 (ch01-ch02) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 3 (ch03). 23
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two afterwords
together).

## Message to paste into the next chat

```
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-2 (ch01-ch02) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 3 = ch03 (第三章 午正 / "Chapter Three. The Hour of the Horse, Second Half
(noon)") end to end. NOTE: data/src/ and data/figs/ are gitignored and rebuild
from source.epub; if data/src/ is absent in a fresh clone, run
`python3 scripts/ingest_epub.py source.epub` first. Read the batch's source from
its text_file in book.json (data/src/06_text00007.txt); the source is
authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch03_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <title>'; each chapter's opening differs: some have an epigraph, some open
directly with the dateline; render whatever the source has; render the source's
per-chapter time-gloss final line as the source's own note). Then generate
out/ch03_reading.md and the parity source with
`scripts/split_bilingual.py out/ch03_bilingual.md ch03 "第三章　午正"`.
Run `scripts/check_numbers.py out/ch03_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail) and
`scripts/check_structure.py --pairs data/zh/ch03.txt out/ch03_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch03" (verbatim English anchors; XHTML bodies with numeric character
references, never named entities; ~3 per chapter, recurring subjects get their
note at first appearance across the whole book, so skip anything already noted in
ch01-ch02). Add any figure specs to figures.json only if the chapter has an image
in data/figs/. Rebuild with `scripts/build_reading_epub.py "out/The Longest Day in
Chang'an.epub"` so the pending-aware TOC links ch01-ch03 content and every other
chapter's skeleton, then run `scripts/qa_epub.py "out/The Longest Day in
Chang'an.epub"` until green. Do a blind double-translation of a literary sample
and a round-trip back-translation of a number-dense sample (separate contexts),
and record the checks and the sample error rate in PROGRESS.md. Rewrite
HANDOFF.md with the Batch 4 (= ch04) kickoff message, commit, and push to branch
claude/the-longest-day-in-changan. Cite chapters/sections, never page numbers.
Never invent bridging text; footnote genuine ambiguity rather than smoothing it.
Do not pause for approval mid-batch. Deliver the rebuilt EPUB in chat as an
attached file.
```

## What is DONE (do not redo)

- Step 0 ingest + survey + skeleton EPUB, approved. 25-batch plan approved.
- Batch 1 = ch01, complete and committed: out/ch01_reading.md, data/zh/ch01.txt,
  12 notes in notes.json, glossary.json seeded, EPUB rebuilt, qa_epub PASS.
- Batch 2 = ch02, complete and committed: out/ch02_reading.md, data/zh/ch02.txt,
  3 notes in notes.json (15 total), glossary.json updated, EPUB rebuilt with
  metadata formatted for Kindle/Apple Books, qa_epub PASS.
- noise.txt authored for check_numbers (project names/idioms/round numbers); its
  loader does NOT strip trailing comments, so keep every note on its own line.
  External noise patterns fire BEFORE built-in patterns in check_numbers.py.
- check_numbers.py WORD_NUM extended with teen ordinals (thirteenth..sixteenth).
- 县尉 rendered "county commandant" (NOT "county magistrate"); decided and in
  glossary.

## What is NEXT

- Batch 3 = ch03 (第三章 午正, ~22,888 source chars, data/src/06_text00007.txt).
  Then B04=ch04 ... B24=ch24, B25=ch25+ch26. See book.json's structure/batches.

## House style set by Batches 1-2 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged.
- Epigraph: NOT every chapter has one. Each chapter's opening differs; some have a
  flash-forward vignette, some open directly with the dateline. Translate whatever
  the source has. The source's per-chapter time-gloss (e.g. "上午10时。巳，又名日禺…")
  is rendered as the SOURCE's own note, in italics, marked as the source's,
  distinct from translator's notes.
- Names: pinyin, one decided rendering per referent, all in glossary.json.
  Recurring items already decided in ch01-ch02 (Zhang Xiaojing, Li Bi, Yao
  Runeng, Wen Ran, Cao Poyan, the Right Shad, the Jing'an Bureau, the Lüben
  Guards, watchtowers, buliang, Wolf Guards, shichen, the West Market, Tianbao,
  barrier-knife, pocket crossbow, smoke pellet, the Xifu, etc.) must be reused
  verbatim; grep the glossary before romanizing anything new.
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
- Cite by chapter, never by page.
- The source text sometimes uses 中元 ("Ghost Festival") where it means 上元
  ("Lantern Festival"); when encountered, translate the intent, not the literal
  wrong festival name.
