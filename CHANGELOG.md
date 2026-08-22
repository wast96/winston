# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-22: Footnote densification pass (commissioner request)

The commissioner asked to greatly increase footnote density: explain the
terms, people, places, events, and references a non-specialist Western reader
would miss, without padding. Content stays FROZEN (a note-only pass; not one
word of the translation changed).

- APPARATUS: notes.json grew from 258 to 886 (+628). Per unit, new totals:
  ch00 7, ch01 86, ch02 110, ch03 126, ch04 31, ch05 68, ch06 101, ch07 66,
  ch08 22, ch09 54, ch10 56, ch11 93, ch12 54, ch13 12. Late chapters taper
  by design (their institutional furniture was introduced earlier and is
  cross-referenced, not re-noted).
- METHOD: one annotator per chapter, each reading the full book-wide
  notes.json and glossary.json so nothing already covered was re-noted;
  recurring subjects keep their note at first book-wide appearance. Every
  candidate was pre-validated (anchor a verbatim substring of the reading
  file, no builder-hazard characters, numeric character references only, no
  duplicate anchors) before apparatus_merge.
- FACT DISCIPLINE (CLAUDE.md rule 5): checkable claims verified against
  Wikipedia / Baidu Baike / academic sources, never AI-written references;
  substantive claims carry a corroborated / uncorroborated / contradicted
  verdict; uncertain external detail was hedged or omitted rather than
  invented. Notes were written not to contradict the frozen prose even where
  the source itself errs (e.g. the ch12 field-army command line).
- BUILD FIX: three same-paragraph anchor overlaps (ch02 Zhang Wentian/Li
  Fuchun, ch06 Xia Yan/Tian Han, ch12 Hou Baolin/Yiguandao) made the note
  numbering non-sequential; the earlier anchor of each pair was trimmed to a
  non-overlapping substring. Rebuilt: qa_epub PASS (886 notes), epubcheck
  5.1.0 clean (0/0/0/0), check_apparatus 0 failures.

## 2026-08-22: Corrections pass 1 (source-dependent faithfulness items + deliverable rename)

Clean-checkout regression first: reset to origin, replayed the resegment
scripts, rebuilt, qa_epub PASS, epubcheck 0/0/0/0. (resegment_ch05..ch13
regenerate their zh scaffold + pagemap standalone and reproduced the tracked
pagemaps byte-identical; resegment_ch02..ch04 chain on the gitignored
data/zh/*.txt OCR scaffold and are not standalone-replayable on a bare
checkout, a known limitation, and those chapters were out of scope here.)

Then resolved the source-dependent faithfulness items logged in PROGRESS.md's
R04 entry, each crop-verified against source.pdf before any edit; where the
source is genuinely self-contradictory it is rendered as printed and
footnoted, never silently corrected (CLAUDE.md rule 4). Prose edits went
through committed edits/<id>_corrections.md lists applied by apply_edits.py,
with anchor_check run before each apply.

- LOCAL ch10 (folio 339): the monument line "'Zhang Bingnan' written by
  mistake for 'Zhang Bingnan'" was self-nullifying (both names romanize
  identically). The scan reads 章炳南 miscarved as 张炳南; the text now says
  the monument "carves the martyr Zhang Bingnan's surname with the wrong
  character," and a NOTE-ADD carries the two characters (章 correct, 张 as
  carved).
- LOCAL ch10 (folio 323): the "fifteen years" War-of-Resistance span
  footnoted as the source's own inconsistency (fourteen at the chapter head,
  eight elsewhere, fifteen here); rendered as printed, no number changed.
- LOCAL ch10 (folio 313): the three-vs-two liaison-officer count footnoted as
  the source's own slip (three posted, two named and followed); rendered as
  printed.
- LOCAL ch10 (folio 332): the Wang Shiwei note refined. The body text says
  only "put to death"; the "dry well" is the later documented record, now
  attributed ("by most later accounts") rather than stated as the book's.
- LOCAL ch11 (folio 358): the dangling "dead fish" given the fish antecedent
  the source implies ("a fish dish" for 下毒/死鱼); no fact added.
- LOCAL ch11 (folio 368): the Wu Shi / Baoding passage footnoted. The source
  both credits Baoding with "producing" Chiang and says his real schooling
  was the Japanese officers' school; Chiang passed through a 1906 Baoding
  preparatory class before Japan and is only loosely counted an alumnus,
  while Wu Shi and Bai Chongxi were full graduates. Rendered as printed.
- LOCAL ch11 (folio 370): Xiao Minghua's third-person "her" (就让她在台湾吧)
  footnoted as the source's own self-reference; faithful. Baidu Baike
  corroboration: executed Taipei 1950, remains returned to the mainland 1982.
- LOCAL ch12 (folio 381): Xi'an "six dynasties" footnoted (Xi'an is
  conventionally the capital of thirteen dynasties; 六朝古都 is Nanjing's
  epithet); rendered as printed.
- LOCAL ch12 (folio 390): the intelligence/security/safety/public-security
  quadruplet footnoted. The source lists four distinct terms
  (情报/保卫/安全/公安), so the English near-synonyms are not a redundant
  doubling; faithful.
- DELIVERABLE: renamed per the commissioner's chat request so the .epub
  carries the book's full name:
  "out/China's Secret War - A Documentary Record of the CCP's Intelligence
  and Security Work.epub" (book.json "deliverable" updated; the old
  out/chinas_secret_war.epub retired). Builder, qa_epub and the Stop hook all
  read the name from book.json, so nothing else needed changing.
- TOOLING: apply_edits.py gained --suffix and anchor_check.py an optional
  second arg, so a separate committed edits/<id>_corrections.md list applies
  without disturbing the R04 edits/<id>_edits.md audit trail. Default
  behavior (edits/<id>_edits.md) is unchanged.

Net: 7 notes added (book-wide 251 to 258), 2 prose fixes (ch10 monument,
ch11 fish), 1 note refined (ch10 Wang Shiwei). Rebuilt; qa_epub PASS (258
notes); epubcheck 5.1.0 clean (0/0/0/0). Files touched: book.json,
notes.json, out/ch10_reading.md, out/ch11_reading.md, scripts/apply_edits.py,
scripts/anchor_check.py, edits/ch10_corrections.md, edits/ch11_corrections.md,
edits/ch12_corrections.md, the renamed deliverable, CHANGELOG.md, PROGRESS.md,
HANDOFF.md, CORRECTIONS.md.

## 2026-08-22: Voice/register pass COMPLETE (R01–R04)

The commissioner-ordered whole-book voice/register/style pass is finished. It
was an English-to-English re-voicing with content FROZEN: every replacement
preserved its original's propositional content exactly (no fact, name, number,
date-value, or claim changed; no paragraph merged or split; no name
re-romanized; no note added or removed). Edits went through committed
`edits/<id>_edits.md` lists applied by `scripts/apply_edits.py`, with
`scripts/anchor_check.py` run before every apply so the 251 note anchors and
182 figure anchors stayed placed. One commit per unit; blind context-free
critiques archived under `review/voice_gate/`.

- R01 (calibration + exemplar): ch00, ch01, ch09. The REVISED
  `out/ch01_reading.md` became the register reference for the rest.
- R02: ch02, ch03, ch04, ch05.
- R03: ch06, ch07, ch08.
- R04 (final) + closing sweep: ch10, ch11, ch12, ch13 (66 edits: 10/9/14/33).
  The Afterword (ch13) drew the most edits — it is the author's own essay and
  the most translationese-dense unit. Closing sweep: book-wide apparatus checks
  (check_apparatus 0 failures; no bundled notes; density spread ~3.2x within
  tolerance), whole-book tic regression (near-zero batteries stayed near zero),
  the check_register table (R04 units within tolerance; the lone drift flag is
  pre-existing ch02), and epubcheck 5.1.0 clean (0/0/0/0).
- MOST paragraphs were LEFT untouched in the narrative chapters; the pass
  protected the author's deliberate register (partisan terms, "old Chiang," the
  vivid keep-idioms and 对仗 set-pieces, the footnoted allusions, the one-line
  punches, quoted-document shapes, the *tewu* italics). Source-dependent
  faithfulness flags the blind readers raised are logged in PROGRESS.md for a
  corrections pass, not touched here. No new STYLE.local rules were needed.
- The rebuilt EPUB is `out/chinas_secret_war.epub` (committed). qa_epub PASS,
  epubcheck 0/0/0/0. The book remains COMPLETE; further work is a corrections
  pass. HANDOFF.md rewritten to post-pass state (kickoff section removed).

## 2026-08-22: Register-pass setup — style system adopted, plan committed

No prose changed. Adopted the shelf's composable style system and planned
the commissioner-ordered voice/register pass so future sessions need only
this branch:

- Ported verbatim from the sibling book's branch (read-only): `styles/`
  (INDEX, _base, lang-zh, lang-ja, genre-fiction, genre-nonfiction,
  STYLE.local.template), `scripts/compose_style.py`,
  `scripts/check_style_freshness.py`, `scripts/voice_gate_critique.py`,
  `scripts/anchor_check.py`, `review/PROTOCOL.md`,
  `review/voice_gate_critic_prompt.md`, `tools/sync_shared.sh`,
  `tests/run_tests.py` (hook-test fix; kills the benign FAILED line
  setup.sh printed on every run).
- `book.json`: `genre: "nonfiction"`. `STYLE.md` recomposed from the layers
  (build artifact with manifest; the old standalone file, which the layers
  descend from, is in git history at edc98bf). `STYLE.local.md` written:
  voice sharpening, preserve list, the ADOPTED register rebaseline, the
  measured calibration baseline, decided renderings.
- `REVISION_PLAN.md` written (four batches R01-R04 with verbatim kickoffs);
  `scripts/register_tics.sh` adapted to this book's profile; HANDOFF carries
  the R01 kickoff.

## 2026-08-21: Figures pass — all 218 images/figures added; real cover

The 图文版's images were deferred through the whole translation (figures.json
was empty). This pass extracts, crops, captions and places EVERY figure in the
book, adds the front-matter portrait gallery, and sets the real scanned cover.

- **182 inline figures** placed across the 12 chapters (ch01 22, ch02 45,
  ch03 12, ch04 4, ch05 21, ch06 5, ch07 12, ch08 8, ch09 14, ch10 16,
  ch11 15, ch12 8) — photos, maps (the Shaan-Gan-Ning border-region map on
  printed 39; the ch02 checkpoint distribution map), and document facsimiles
  (Mao's manuscripts, handwritten letters, signature sheets). Each has a real
  screen-reader `alt` and a translated caption (labels are the source's).
- **36-plate front-matter gallery** (`figures.json` `_plates`): the portrait
  section on PDF 5–18 plus the author photo (PDF 2), rendered as a new
  "Photographs" page after Principal Characters.
- **Real cover**: the scanned front cover (PDF 1) set as `book.json`
  `cover_image` (`data/figs/cover_front.jpg`), replacing the generated cover.
- **Crop verification**: every crop was drawn on its page and eyeballed for
  clipping; `find_figures.py` misses (maps, line art, faint/light portraits,
  multi-photo pages, document facsimiles) were caught by a whole-book
  thumbnail sweep. Three crops that caught a caption/body-text sliver
  (p0046, p0162; the earlier map) were re-cropped tight.
- **Tooling**: `scripts/crop_fig.py` (explicit-coord/batch cropper),
  `scripts/draw_boxes.py` (box-on-page overlay for cutoff checks),
  `scripts/scan_pages.py` (thumbnail sweep), `scripts/montage.py` (crop QA
  sheet), `scripts/fig_anchor.py` (page→paragraph anchor), and
  `scripts/assemble_figures.py` (merges per-unit spec files into figures.json
  and validates that every `before` anchor is a unique substring within the
  first 80 chars of a reading-md paragraph).
- **Builder** (`scripts/build_reading_epub.py`): new `render_gallery` +
  spine/nav wiring for the Photographs page; interior figures now ship as
  greyscale JPEG (`MAX_FIG_WIDTH` 1100→900, q82) instead of greyscale PNG,
  cutting the EPUB from ~40 MB to ~15 MB with no visible loss; **fixed** a
  latent bug where an `alt` containing a double quote (e.g. a sign reading
  "WHITLEY HALL") broke the XHTML — `alt` now uses `esc_attr` (quote=True).
- **.gitignore**: `data/figs/` un-ignored so the committed figure crops and the
  cover source are tracked; only the figure scratch (`_scan/`, `_specs_*.json`,
  `_*.png`) stays ignored.
- Rebuilt: 219 images embedded, qa_epub PASS, epubcheck 0/0/0/0.

## 2026-08-21: B13 — Chapter 12 + Afterword; BOOK COMPLETE
- Translated ch12 (128 paras, +21 notes) and ch13/Afterword (32 paras, +4 notes);
  +42 glossary rows (284 total, 251 notes). EPUB now 14/14 units; qa_epub PASS,
  epubcheck 0/0/0/0. Final EPUB committed with `git add -f`.
- WHOLE-BOOK RECONCILIATION (deep-audit finding, applied as a global correction):
  GLOBAL: 西北公学 rendered "West China College" in ch08 (5 occurrences) corrected to
  "Northwest College" to match ch02/ch05/ch07 (西北 = Northwest); rebuilt, qa green.
  LOCAL: ch08 冀南行署 "Jinan Administrative Office" -> "South Hebei Administrative
  Office" (disambiguates from the city 济南).
- data/noise.txt: +7 entries (一百单八将, 二十多万, 七万三轮车, 金三角, 六里桥, 徐欣三, 十足).
- New tooling (do not revert): scripts/resegment_ch12.py, scripts/resegment_ch13.py,
  scripts/crop_band.py (magnified band crop), scripts/render_ledger.py (term ledger),
  scripts/feed_authority.py. Rendered out/term_ledger.md, out/deep_audit.md.
  authority.json fed with this book's renderings under slug "chinas-secret-war".
- COMPLETION.md written; HANDOFF.md rewritten to COMPLETE.

## 2026-08-15: B01 voice-gate revision (register recalibration)
- Commissioner feedback at the voice gate: the translation was loyal to the
  source's TEXTURE (baogao-wenxue exclamation, rhetorical questions, "so it
  turns out" reveals, anaphora, name repetition, calques) where it should be
  loyal to its EFFECT; the result read "goofy" in English.
- STYLE.md recalibrated: rewrote "The author's voice" section (keep stance and
  heat, render at English register); added the calque-sweep list and a
  pronoun-down rule; fixed failure-mode 10 (was "questions stay questions").
- ch00 (Preface) rewritten cold and plain: exclamations 0, anaphora thinned,
  mining metaphor pulled back, the "engineering the cultural gene" closer
  re-voiced. 28-paragraph structure preserved.
- ch01 swept: narration exclamations 79 -> 20 (kept only quoted speech and
  slogans, via a quote-aware pass); non-quote rhetorical questions -> 2;
  "so it turns out / it seems" reveals removed; calques fixed (thirds-of-a-
  month, 人枪 "men and guns", 工作网 "work net", 鹤立鸡群, 之至, trailing
  "indeed", domestic 侦察 -> investigation/surveillance while keeping military
  "technical reconnaissance"); name-repetition runs pronouned down (the Liu
  Zhidan letter scene, Yao Zijian). 299-paragraph structure preserved.
- Genuine snags fixed: "detection and banditry" -> "detection of bandit
  crime"; "hacked into being by the party in power" -> "cut into being by the
  terror of the ruling Nationalists" (removes the apparent contradiction with
  the CCP being outlawed); the smashed-radio anecdote's two tellings
  differentiated so they no longer read as an accidental duplication.
- Rebuilt: qa_epub PASS, epubcheck 0/0/0; ch00 verify clean; note anchors
  re-checked (fixed the Xi'an Incident anchor after its "!" was flattened).

## 2026-08-15: STYLE.md revision pass (commissioned, pre-translation)
- Rewrote STYLE.md against the actual source prose (preface + ch1 openers now
  read from the scan). Cut novel-inherited residue: trimmed provenance
  framing, removed fiction-latitude from the enrichment doctrine (nonfiction
  default: when in doubt, do not enrich), fixed the sheet's own em-dash
  violations in headings.
- Added what the book actually does: a signature-devices list (anaphora
  chains, one-line punch paragraphs, datebook chronology, recurring metaphor
  strands, the inclusive "we"), a Party-jargon abstraction-stack failure
  mode, and a Reader-ease conventions section (one handle per organization;
  use-vs-mention rule for terms discussed as words; canonical renderings for
  famous quotations; nickname policy; scare-quote budget of zero added;
  date/number/unit conventions with exact 万 conversion).
- Register-drift guard: added the low-dialogue caveat (contraction rate is
  noise in units with sparse quoted speech; judge narratorial signals and say
  so in PROGRESS).
- No translation exists yet, so nothing cascades. B01 translates under the
  revised sheet.
