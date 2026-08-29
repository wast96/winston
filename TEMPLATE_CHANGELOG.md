# TEMPLATE_CHANGELOG — versions of the translation template itself

A project forked from this template should note here WHICH version it forked,
so a mid-book "template upgrade pass" knows what fixes it predates. Keep this
file when instantiating a project.

## v2.4 — 2026-08-29

The shelf-wide authority adjudication, the retrofit assessment template, and
the deliverable naming policy.

- AUTHORITY.JSON ADJUDICATED SHELF-WIDE. Every branch's copy (fourteen
  carried the file; each had drifted independently since 2026-08-05) merged
  into one 2,596-term file with full book provenance. All 72 real cross-book
  conflicts adjudicated: 64 carry a binding `decided` form (earlier books'
  other forms stand as recorded deviations), 8 are `context-dependent` with
  the rule in the note (a hanzi naming different things in different books
  or languages). Status vocabulary normalized (agreed / agreed-article-varies
  / single-book / decided / context-dependent / reconcile); adjudication
  rationale recorded per entry. Decisions follow the shelf's own canons:
  concession-era names keep period English forms (the Garden Bridge, Avenue
  Haig, Jessfield Park, Bubbling Well Road, the Louza station), pinyin is the
  default elsewhere (Chongqing, Guilin, Yan'an), conventional English forms
  for established figures (the Soong family set: T. V. Soong, Soong
  Ching-ling, Soong Mei-ling, H. H. Kung), one handle per organization
  (Juntong, the Baomiju, the Central Special Branch, the Renaissance
  Society).
- ASSESSMENT.template.md (new, shared): read-only retrofit inspection of a
  completed book against the CURRENT standard: template-version archaeology,
  measured tic profile and register state, footnote density vs the directive
  (benchmark: roughly 40-60 notes per chapter-sized unit; words-per-note
  swing under ~2-3x), authority.json deviation check, tiered defect
  inventory, and a commissioning verdict. Its step 0 (upgrade the branch's
  template files before measuring or editing) is mandatory for any pass on a
  pre-current-template book; CLAUDE.md's revision-pass section points here.
- DELIVERABLE NAMING POLICY (commissioner, 2026-08-29). The deliverable
  carries the book's FULL English title with any colon replaced by a comma
  ("Midnight, A Romance of China.epub"), and every per-round chat copy
  carries the round marker ("The Longest Day In Chang'an B5.epub"), made by
  scripts/stamp_deliverable.py (new, shared; also validates the name with
  --check). The canonical unstamped file remains the build target, the
  qa_epub target, and the file committed on completion. kickoff_guard now
  matches the deliverable STEM so stamped names still satisfy the wrap-up
  signal.

## v2.3 — 2026-08-29

The first promotion pass, plus the register-pass tooling the books built.
Harvested from the-sword-roars (the B09 commissioner register review),
chinas-secret-war (the review adopted and applied, with measured
calibration), chen-yangshan (voice-gate and revision rulings), the zhou-enlai
register assessment, and the fiction-side revision plans. Every promoted rule
carries a provenance comment in its layer.

- LAYERS PROMOTED. `_base.md`: the read-aloud and modern-writer tests; the
  keynote-register guard ("de-stiffen the machine, never the voice," from
  the-rebel); the spine test for long sentences; kill-inversions; the antique
  function-word kill list; scene-primed second meaning (moved from lang-ja,
  it is language-independent); no sentence-initial numerals; date-format and
  spelling-locale decided at setup; footnote shaping mechanics (one note =
  one referent, marker placement, one gloss mechanism, density balance).
  `lang-zh.md`: chengyu three-bin triage; de-nominalization; 等-tag and
  one-after-another variation; interrogative "in the end"; the could-only
  class; source-punctuation function (narration ellipses). `lang-ja.md`:
  proofread every inserted character. `genre-nonfiction.md`: the
  modern-neutral register baseline (three voices); the narration-contraction
  DIAL with its recorded conflict (adopted on two books, declined on a
  third); quotation attribution front-load and quote-tag variation; formula
  fatigue.
- PROMOTION MECHANICS. `styles/INDEX.md` defines `#adopted` (adoption is not
  corroboration; surviving application is validation), records commissioner
  declines against a rule, promotes contested rules as per-book DIALS, and
  gives the harvest a trigger: COMPLETION.md now requires a style ledger
  harvest section listing the book's `#promote` rules.
- TOOLING. `scripts/register_tics.py`: the greppable tic battery both real
  register passes had to build per-book, generalized (per-unit listing +
  `--profile` calibration table + `data/register_tics.local.json` per-book
  config), with a regression fixture in tests. `scripts/anchor_check.py`:
  pre-flight anchor-collision check for edit lists. `check_register.py`
  gains informational narration columns (contraction share, bangs/1k,
  antique-word count): the second drift campaign was narration-side and the
  dialogue metrics cannot see it (references/register-drift.md tells that
  story).
- FOOTNOTE DENSITY DIRECTIVE (commissioner, shelf-wide). Default to
  footnoting, not omitting: assume a reader with no background for the
  events, places, people, ideas, and items unique to the book's time and
  place, note every such reference at first appearance with real content and
  the fact-check verdict, and sweep the lost-in-translation layer (wordplay,
  idiom images, register shifts, meaningful names, forms of address) with the
  same generosity. The old "8-15 notes early" guide and the default
  unfootnoted-discrepancy tier are retired; an early chapter now runs dozens
  of notes (the directive's source book went 24 to 73 on chapter one at its
  gate). Padding is still forbidden: a note must say something beyond the
  name. Encoded in CLAUDE.md's footnote section and `_base.md`'s apparatus
  section.
- PROCESS. REVISION_PLAN.template: measured calibration baseline before any
  editing; per-unit blind critique as the one sanctioned context-free
  subagent; anchor_check before every apply; tics regression and KEEP-list
  diff sweep in the exit checklist; the mid-book sequencing rule (freeze the
  sheet, draft the back half congruous, sweep the front once); the optional
  ANALYZE/EXECUTE role split. STYLE.local.template gains the KEEP list and
  the consistency canon; the voice gate calibrates the register dials and the
  critic-prompt file documents the known blind-critic false positives.
  `tools/sync_shared.sh` now carries the new scripts, the register-drift
  reference, and itself (it runs on the EPUB master, which did not have it).

## v2.2 — 2026-08-15

The composable style system, plus the voice-gate auto-evolution loop.

- STYLE IS NOW COMPOSED, not hand-written per book. `scripts/compose_style.py`
  builds a book's `STYLE.md` from shelf-wide `styles/` layers (`_base` +
  `lang-<zh|ja>` + `genre-<fiction|nonfiction>`, selected mechanically from
  `book.json`), alongside `STYLE.local.md`, the book's own voice-gate ledger and
  the only style file a session edits. `styles/INDEX.md` documents selection and
  the between-books promotion rule; `check_style_freshness.py` flags when a layer
  has moved since a book was composed (informational; never recompose mid-book).
- VOICE-GATE AUTO-EVOLUTION (Step 0c): a context-blind critic (a fresh reader
  with no source, no `STYLE.md`, no project context, driven by
  `review/voice_gate_critic_prompt.md`) flags what reads wrong as English; the
  fixes are applied against the source and distilled into `STYLE.local.md` rules
  (general ones tagged `#promote`), up to three rounds, before the human gate.
  `voice_gate_critique.py` does the plumbing.
- `tools/sync_shared.sh` carries `styles/` and the new scripts so the scanned
  and EPUB masters stay identical. `tests/run_tests.py` covers layer selection,
  substitution, determinism, freshness, and the missing-VOICE_TARGET guard.

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
