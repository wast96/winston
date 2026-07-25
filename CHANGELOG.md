## 2026-07-25 - Final sweep: accuracy and stylistic unity

Whole-book pass over the translated text (prologue + ch1-6).

TWELVE FOOTNOTES WERE NOT IN THE BOOK. 289 written, 277 shipping. Anchors that
no longer matched the prose - mostly capitalisation slips - were skipped
silently, and qa_epub stayed green because refs and bodies still agreed with
each other. All twelve restored. The builder now REFUSES to build when an
anchor fails to match, and that check caught two more during this sweep.

CHAPTER SIX WAS SHIPPING WITHOUT ITS TITLE. Its file used a single # where the
others use the two-level convention; the builder treats # as the book title
and skips it, so the chapter heading, subtitle and dateline were all dropped.
Fixed.

STYLISTIC DRIFT MEASURED AND CORRECTED. Contractions inside dialogue had
fallen from 16.2/1k in ch1 to 0.37/1k in ch6 - two contractions in 136 places
that wanted one. "Shall" had risen from 0% of shall+will to 25%. Both are
formality markers and both moved together; this is the stiltedness the first
draft was rejected for, arriving quietly. Corrected to 11.0/1k in ch6 and
20.1/1k in ch5, with three registers deliberately left formal: the Japanese
officers (a period convention the Chinese observes), quoted documents, and
classical tags. Two oaths and a proverb had to be put back after the first
pass over-corrected them.

RESIDUAL LEFT ALONE: em-dashes still range 4.3 to 17.9 per 1k against ch1's
12.2. The dense paragraphs use them for dialogue interruption and appositive
work, so flattening them mechanically would damage prose that reads well.
Reported rather than faked.

Also swept for the invented-precision defect the deep audit found. Four
candidates, all false positives - the definiteness was in the source each
time. That error was isolated, not systematic.

All checks re-run after the edits: invariants 0 unresolved across 793 pairs,
paragraph parity exact, zero glossary drift, entity misses all pronoun
substitution. Rebuilt: 7 documents, 931 paragraphs, 289 notes, qa_epub PASS.

