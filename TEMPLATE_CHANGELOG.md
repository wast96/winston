# TEMPLATE_CHANGELOG — versions of the translation template itself

A project forked from this template should note here WHICH version it forked,
so a mid-book "template upgrade pass" knows what fixes it predates. Keep this
file when instantiating a project.

## v2.1 — 2026-08-05

The reader-experience pass, plus conformance hardening.

- POPUP FOOTNOTES: markers carry epub:type="noteref" and bodies are <aside
  epub:type="footnote">, so Apple Books and Kindle show notes (both streams,
  on the EPUB template) as popups over the page; the endnotes page remains
  as fallback.
- PRINCIPAL CHARACTERS page rendered from glossary rows flagged
  principal:true (optional cast one-liner, cast_order).
- Per-character VOICE SHEETS in HANDOFF (register spec at first appearance,
  consulted at every dialogue scene) and the batch-seam splice (read the
  previous unit's final two pages before translating).
- check_register gains an informational sentence-rhythm CV column (the
  droning class nothing else measures).
- check_reconcile.py mechanizes the whole-book reconciliation sweep
  (compound rendering drift, glossary-forward usage, spelling locale).
- Conformance: TOC sub-lists nest inside their parent li; nav entries for
  pending sections link instead of sitting as bare text; reserved marc
  prefix dropped; skeleton and fixture builds check 0/0/0 in epubcheck.
- The kickoff Stop hook stands down when HANDOFF.md still carries the
  template placeholder; the test harness covers both hook paths and the
  builder round trip. verify_unit reads data/noise.txt; check_content
  refuses to measure nothing; authority.json disagreements adjudicated.

## v2.0 — 2026-08-05

The nine-book harvest. Everything below was learned on gu-shunzhang, wang-
yaqiao, juntong, huang-mulan, the-whistling-wind, midnight, thousand-li,
on-a-hair-trigger, and the-longest-day-in-changan.

- Two approval gates: the survey and the new first-chapter VOICE GATE (the
  frozen register reference).
- QC contract rebalanced against the measured cost model: cheap scripted
  checks every chapter (verify_unit one-command gate); blind double
  translation demoted to once-per-book calibration; round-trip
  back-translation demoted to sample-only; whole-page eye-reads replaced by
  dual-OCR-filtered crop verification.
- New checks: check_content (displacement), check_align, qc_entities,
  check_register (frozen reference), check_apparatus, tail verification,
  whole-book reconciliation sweep (epithet drift, rendering counts,
  first-appearance).
- check_numbers: auto-guarded noise (lookbehind), extra-noise-before-builtins,
  decomma, positional hanzi years, full ordinals, composite
  hundreds-of-thousands, cn_to_int 百/千/万; regression fixtures in tests/.
- check_structure: declared parity exceptions, positional heading-shape,
  config heading_depth, set-off marker stripping. qa_epub: META-INF
  exemption, apparatus-set doc detection, page-list gate.
- Paragraph structure from measured indents (indents.py + assemble.py);
  structure recovery without TOC (find_headings.py + build_structure.py);
  replayable crop-verification ledger (apply_fixes.py).
- Builder: covers (supplied or generated, EPUB3+legacy declarations), full
  store-ready OPF with unified field vocabulary, valid deterministic UUIDv5,
  deterministic dcterms:modified, render-layer typographize, note markers
  after punctuation, figure-placement guard + alt text, set-off classes
  (*** / {v} {d} {g} {p}), printed-page markers + page-list, pending-only
  spans and all_done TOC cleanup, glossary escape fix, series metadata.
- Apparatus by tool, not hand: apparatus_merge.py (validated, idempotent,
  re-read verified) replaces heredocs; apply_edits.py + edits/ grammar for
  revision passes.
- Footnote density is a reader model (coverage domains, first-appearance
  protocol, NOT-re-noted ledger, glossary-as-quarry), not a 3-per-page quota.
- Docs: CLAUDE.md rewritten; REVISION_PLAN and COMPLETION templates;
  review/PROTOCOL.md; upgraded CORRECTIONS form (chat input is first-class);
  setup.sh; reasons-carrying .gitignore; kickoff label + paste rule.
- Enforcement layer: .claude/settings.json allowlist + Stop hook
  (kickoff_guard.py, self-configuring, fail-open, capped); the
  scanned-book-translation skill with its four reference docs.
- Collection layer: authority.json (cross-book renderings) and COLLECTION.md
  (series metadata, reading order); final EPUB committed on completion.

## v1.x — 2026-07-28..31

Initial extraction from the wang-yaqiao project: survey-first workflow,
skeleton EPUB with full hyperlinked TOC, generalized ocr_crop, basic
Kindle/Apple metadata.
