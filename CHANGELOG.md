# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

## 2026-08-04 — revision batch R2: register polish + footnote expansion (ch14–ch26) + whole-book close
- RECONCILIATIONS (2 global, R1-flagged): 投名状 unified on "oath-token of blood"
  (glossary-decided, first appearance ch03) — changed ch15 rendering "a pledge of
  blood-guilt" → "an oath-token of blood", moved the note from ch15 to ch03 (first
  appearance) and rewrote its close for the ch03 scene. 双陆 unified on "double-sixes"
  (first appearance ch04) — changed ch23 rendering "shuanglu" → "double-sixes", moved
  the note from ch23 to ch04, updated glossary.json 双陆 en → "double-sixes". ch04's
  unrelated 杀孽 "blood-guilt" left as-is. Grep-confirmed 2 occurrences each, no drift.
  Files: out/ch15, ch23 _reading.md; notes.json; glossary.json.
- REGISTER (16 edits, 7 chapters): removed archaic/fake-antique diction and stilted
  inversions per §3.2 — "upon the air"→"in the air" (ch15, ch22), "presently"(archaic),
  "verily", "well-nigh"/"nigh", "scarce"(adverb), "not a whit", "was/were become"→
  "had become", "there could be seen X"→"stood X", "Broad and high it spread"→
  un-inverted, "in a twinkling"→"in an instant". ch24 carried the exact §3.2 examples
  (8 edits). Files: out/ch15, ch18, ch19, ch20, ch22, ch23, ch24 _reading.md.
  ch14/ch16/ch17/ch21/ch25/ch26 swept, already clean.
- LOCAL fidelity: 0 new fixes; the strong prior baseline held across ch14–ch26.
- FOOTNOTES: +40 net (141 → 181) across ch14–ch26 per §4, plus the 2 relocated
  first-appearance notes (into ch03, ch04). Every new note fact-checked; the
  glossary rows were the quarry (§4.3). Files: notes.json.
- VERSE: none added; the two candidate couplets (Ode to the Willow ch24; the
  Everlasting-Sorrow lines ch21) are quoted inline in prose and stay prose, per §5.
- Whole-book close: verify_unit.py on ALL 26 units (green, exit 0); smart_quotes.py
  (idempotent; only the 5 known benign continuation-line warnings); ~20-term glossary
  consistency grep (all consistent, no drift); rebuilt
  out/"The Longest Day in Chang'an.epub"; qa_epub PASS (181 refs = bodies = backlinks,
  38 files, all links resolve). Files: PROGRESS.md (R2 entry), CHANGELOG.md,
  COMPLETION.md (note count + revision addendum). HANDOFF.md untouched by design.
- Observation (not a defect): ch22 source {g} hour-gloss carries an internal
  clock-time error ("Five o'clock ... Mao" for the 7 a.m. Dragon hour), same class as
  the ch10/ch11 {g} quirks; left verbatim per house style.

## 2026-08-04 — revision batch R1: register polish + footnote expansion (ch01–ch13)
- REGISTER (15 edits, 6 chapters): removed archaic/fake-antique diction and one
  calque per REVISION_PLAN §3.2 — "presently"(archaic), "not a whit", "whereupon",
  "yonder", "hither and yon", 不由得="could not help but". Files: out/ch01, ch02,
  ch05, ch07, ch10, ch11 _reading.md. ch03/ch04/ch06/ch08/ch09/ch12/ch13 swept,
  already clean.
- LOCAL fidelity (2, ch07): rendered raw untranslated CJK 花钿 in the English body
  at two spots into English, consistent with ch04's decided 绞银翠钿 rendering.
  Files: out/ch07_reading.md.
- FOOTNOTES: +55 net (86 → 141) across ch01–ch13, per REVISION_PLAN §4. Includes
  2 retroactive first-appearance notes into ch01 (Qujiang Pool, Wang Zhongsi) and
  relocation of the 胡旋舞 note from ch09 to its first appearance in ch04. Files:
  notes.json.
- Ran verify_unit.py on all 13 units (green), smart_quotes.py (idempotent; 5 known
  benign continuation-line warnings), rebuilt out/book.epub, qa_epub PASS (141
  refs = bodies = backlinks). Files: PROGRESS.md (R1 entry), CHANGELOG.md.
- Logged for R2: 投名状 and 双陆 rendering + first-appearance mismatches across the
  book; ch10/ch11 source {g} hour-gloss quirk left faithfully as-is.

## 2026-08-04 — revision pass 1: formatting, typography, plan for register pass
- GLOBAL: recovered the source EPUB's set-off formatting into all 24 chapter
  reading files (110 scene breaks as `***`, opening vignettes `{v}`, datelines
  `{d}`, the source's hour-notes `{g}`), rendered distinctly by the builder;
  new scripts/apply_format_markers.py. Files: out/ch01–ch24_reading.md,
  scripts/build_reading_epub.py (new CSS classes, centered chapter titles,
  cleaner Contents page, corrected Notes-page preamble), scripts/check_structure.py.
- GLOBAL: typographic quotes across all 26 units + notes.json anchors/bodies +
  glossary/book.json display strings; new scripts/smart_quotes.py (idempotent).
- LOCAL fidelity: ch03 removed a speaker tag not in the source (zh+en);
  ch09 restored a dropped closing quote.
- LOCAL: partial register polish of ch01, ch04–ch07 (first tranche; full sweep
  planned). noise.txt: lookbehind fixes for 十一 and 六个字 (residual-orphan trap).
- New scripts/verify_unit.py (per-unit parity+numbers+anchors gate); all 26
  units verified; rebuilt; qa_epub PASS.
- Wrote REVISION_PLAN.md: the full register-polish + footnote-expansion plan
  (batches R1/R2), for execution in follow-up sessions.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->
