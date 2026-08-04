# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

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
