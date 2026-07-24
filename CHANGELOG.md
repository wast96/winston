## 2026-07-24 - Datelines: only where the book supplies none

GLOBAL correction from Winston, clarifying the earlier dateline instruction:
"unless otherwise stated" means that where the book states the date itself,
the translator's guess should not appear at all.

Chapters one and two open with the date in the author's own first line. Both
were carrying a bracketed dateline as well, so the reader met the same date
twice in consecutive lines, once as apparatus and once as prose. Removed.

- book.json: dropped the "dateline" key from ch01 and ch02. The prologue and
  chapters three to six keep theirs; those are genuine inferences and each
  still carries its note saying so and giving the reasoning.
- notes.json: removed the two notes whose only content was "this dateline is
  the author's own." Re-anchoring that content onto the chapter's opening
  line turned out to be unnecessary in both cases - ch02 already had a
  stronger note on the same phrase making the same point (that March 1928 is
  a frame the author imposed over events documented to 1929 and 1930), and
  ch01's was explaining an edition-wide convention rather than a fact about
  the chapter. Note count 279 -> 277.
- scripts/build_reading_epub.py: the convention itself now lives in the
  translator's note, where it belongs - a bracketed opening line is mine, an
  absent one means the author dated his own chapter.

Caught by qa_epub, which failed the first rebuild with a note body that had
no reference: the re-anchored ch02 note could never match, because the
existing note on the same phrase had already inserted its marker into the
middle of the string. The checker earned its place again.

Rebuilt: 7 documents, 930 paragraphs, 277 notes, qa_epub PASS.
