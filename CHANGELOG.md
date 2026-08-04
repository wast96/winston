# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

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
