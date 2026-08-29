# ASSESSMENT.md: retrofit assessment of *A Thousand Li of Rivers and Mountains*

Read-only retrofit inspection of the completed book against the CURRENT shelf
standard (template v2.4, 2026-08-29). No translation text was changed in this
session and no EPUB was built. The product is a commissioning decision: whether
the book earns a retrofit pass, of what kind, and at what size.

(Obeys CLAUDE.md rule 6: no em dashes in this file's prose.)

## 0. Toolkit upgraded before measuring; doctrine upgrade deferred to the pass

The measurement tools were brought current before any number was taken. This
session copied onto the branch, from `origin/claude/translation-template-epub-master`,
the shared assessment toolkit and committed it as "v2.4 toolkit for assessment":
`ASSESSMENT.template.md`, `authority.json`, `TEMPLATE_CHANGELOG.md`, and the
scripts `register_tics.py`, `check_register.py`, `anchor_check.py`,
`stamp_deliverable.py`. Every measured figure below was produced with those
current tools, not the older set the branch shipped.

The DOCTRINE upgrade (replacing the branch's `CLAUDE.md`, adding the `styles/`
layer system and a composed `STYLE.md`, and pulling the remaining current
scripts and templates) is deliberately NOT done here, because it would change
the operating manual and this session is read-only. It is step one of any
commissioned pass and is written into the R1 kickoff in section 6.

## 1. What the book predates

The book carried no `TEMPLATE_CHANGELOG.md`, no `styles/` directory, and none of
the register or apparatus scripts (`register_tics.py`, `check_register.py`,
`anchor_check.py`, `compose_style.py`, `voice_gate_critique.py`, `verify_unit.py`,
`check_align.py`, the `check_apparatus`/`apparatus_merge` set, `check_style_freshness.py`),
so it forked at roughly template v2.2 or earlier, before the changelog mechanism
existed. It therefore predates: the composed style-layer system and `STYLE.md`
(the branch still runs the monolithic `CLAUDE.md`); the voice gate; the v2.3
register tooling (`register_tics.py`, `check_register.py`, `anchor_check.py`);
the v2.4 shelf-wide `authority.json` adjudication; the v2.4 deliverable naming
policy; and, most consequentially, the current footnote-density directive. This
book's `CLAUDE.md` (line 206) still states the retired model, "about 3 notes per
chapter-equivalent is a fair calibration"; the current directive asks for roughly
40 to 60 notes per chapter-sized unit. The book was annotated to its own old
target and slightly exceeds it (about 6 notes per chapter), which places it an
order of magnitude under the standard it is now measured against.

Several of this book's own practices are already shelf canon and must NOT be
disturbed: the pending-aware full hyperlinked TOC, the cumulative single-spine
build, the verbatim-quote bilingual QC file split into reading and parity
sources, and the additive `check_numbers` lookbehind noise patches. One class of
its choices was later overruled: the concession-name renderings. The v2.4
`authority.json`, adjudicated 2026-08-29, records this book ("thousand-li") by
name as the deviating party on six concession-era terms and binds a different
`decided` form for each; the adjudication postdates the book, so those forms
stand in the file as recorded, tolerated deviations rather than as errors caught
in the act (see section 2 and Tier A).

## 2. Measured state (numbers before opinion; measured 2026-08-29)

- **Size.** 37 logical units (epigraph `ch01`, 34 titled chapters `ch02`–`ch35`,
  the unsigned letter `ch36`, the two-part appendix `ch37`). Source: 157,170
  characters. Reading text: about 132,000 English words, 2,768 paragraphs. Notes:
  **217**, continuously numbered, average note body about 67 words (real notes,
  not stubs). Deliverable `out/thousand-li.epub`; `qa_epub.py` re-run this session
  is **PASS** (37 documents, 2,768 paragraphs, 217 references = 217 bodies = 217
  backlinks, all links resolve).

- **Tic profile** (`register_tics.py --profile`, 37 units, 2026-08-29). Counts
  are candidates, not verdicts.

  ```
  battery                    total     where it clusters
  antique-fn-words              15     spread thin, <=2 per chapter
  trailing-besides              27     spread across the book
  could-only                    34     spread; the largest by-ear battery
  pivots                         0
  nominalization                12     ch34 x4 the only cluster
  deng-tag                       8
  one-after-another             10
  quote-tag-archaism             1
  narration-ellipsis            13
  in-the-end-question            6
  sentence-initial-numeral       1     ch01 epigraph date line
  day-month-date                11     ALL in ch37 appendix
  british-spelling               9     8 "theatre" + 1 "labour"
  litotes                       14
  narration-bang                 2     near zero
  long-sentence>90w              5     ch13/18/24/28/30, one each
  ```

  The profile is clean by shelf standards: zero pivots, near-zero reveal-bangs,
  a single archaic quote tag, nominalization confined to one chapter, and only
  five sentences over 90 words across the whole novel. The two batteries worth a
  by-ear sweep are `could-only` (34) and `trailing-besides` (27); the rest are
  small.

- **Register vs reference.** The book predates the voice gate and has NO frozen
  reference chapter (`reference/` is empty), so `ch01` is an epigraph and cannot
  serve; `ch02` ("Dice"), the first narrative chapter, was used as the baseline
  and every conclusion is relative to it. `check_register.py --ref out/ch02_reading.md`
  reports the baseline itself on the low-contraction end (dialogue 10.8 per 1,000,
  rhythm CV 0.61, zero antique narration words), with most chapters running ABOVE
  it (ch04 33.2, ch30 26.3, ch33 25.8), so the book's dialogue register is
  healthy and if anything generous. Two chapters fail the drift test against this
  baseline: `ch24` ("Backstage", 0 dialogue contractions) and `ch28`
  ("Xiaotaoyuan", 0.05x). `ch28`'s formality is deliberate characterization (a
  master-and-disciple exchange in a classical political register: "To resist the
  foreign, one must first pacify the domestic"), so it is a KEEP; `ch24` warrants
  one by-ear read. Apostrophe style is straight throughout (1,585 contractions,
  no curly strays), so there is no smart-quote inconsistency to fix.

- **Footnote density vs the directive.** Across the 34 titled chapters: 130,068
  words, 210 notes, mean **6.2 notes per chapter**, overall **619 words per note**.
  The directive benchmark is roughly **40 to 60 notes per chapter-sized unit**,
  with words-per-note swinging no more than about 2 to 3x across the book. This
  book is at about one-seventh to one-tenth of the note-count band, and its
  words-per-note swing is **7.6x** (277 in `ch37` to 2,118 in `ch35`), well past
  the 2-3x ceiling. Eleven chapters sit at four notes or fewer; the thinnest are
  `ch35` (2,118 words/note), `ch33` (2,020), `ch29` (1,809), `ch05` (1,223),
  `ch32` (1,033). This is the single largest gap between the book and the current
  standard, and the whole of the densification workstream (section 4, Tier C).

- **Consistency spot-checks.**
  - *Date format.* The body uses the shelf-default "Month Day" form ("August 7",
    "January 28", "March 20"). The `ch37` appendix uses the "Day Month Year" form
    for all 11 of its dates ("16 January 1933", "4 April 1933"). One internal
    split, confined to the appendix, 11 dates.
  - *Spelling locale.* Nine British-spelling hits, but eight are the real
    concession-era venue names the battery explicitly exempts (the Lyceum,
    Grand, Carlton and Lehua Theatres, whose period English WAS "Theatre") plus
    "Labour College" (a proper institution name). Only "a piece of theatre" (x2)
    is a genuine common-noun locale stray. Effectively 2 to 3 real hits, not 9.
  - *High-traffic decided renderings.* "the Shen Bao" appears 14 times against 4
    bare "Shen Bao" (the `decided` form is "the Shen Bao", article per sentence),
    a small internal-consistency nit, not an authority deviation. "the Bund",
    "the Whampoa Military Academy", "Chiang Kai-shek", "the Kuomintang" all match
    the shelf.
  - *authority.json deviations (status `decided`, binding).* Cross-checking every
    binding shelf term whose hanzi appears in this book's source (85 of them)
    surfaces six substantive deviations, EACH already recorded in `authority.json`
    against "thousand-li":

    | term | book uses | decided form | in reading text |
    |------|-----------|--------------|-----------------|
    | 海格路 | Haige Road | **Avenue Haig** | 1 (period name already glossed in a note) |
    | 老闸捕房 | the Laozha Police Station | **the Louza police station** | 1 |
    | 马斯南路 | Massenet Road | **Route Massenet** | 2 |
    | 大美晚报 | Da Mei Wan Bao | **the Shanghai Evening Post and Mercury** | 1 (masthead glossed in a note) |
    | 吴淞口 | the Wusong bar | **the mouth of the Wusong River** | 7 |
    | 反省院 | the Reflection Institute | **reflection institute** (case) | 1 |

    Plus 白区 "the White area" against decided "the White areas" (number). About
    13 occurrences in the reading text, six terms, all grep-locatable, all already
    recorded as this book's deviations. `黄埔军校` and `申报` differ from their
    decided forms only by the leading article and are effectively compliant.

## 3. What already meets the standard (do NOT "fix" these)

The register and fidelity apparatus are at or near target; the pass must not
churn them.

- **Translation fidelity is thoroughly evidenced.** Every unit's reading and
  parity texts split from one bilingual QC file that quotes the digital source
  verbatim; `check_numbers.py` clean across all 32 machine-checkable units (0
  unresolved numerals), `check_structure.py` paragraph-parity clean, 217 anchors
  resolve, glossary drift 0; blind double-translation and back-translation run
  per batch with the one caught omission (从上海) restored. Leave this alone.
- **Register is clean.** Tic profile near-zero on the dangerous batteries (0
  pivots, 2 narration bangs, 1 archaic quote tag, 5 long sentences book-wide);
  rhythm CV around 0.6; dialogue contraction rate generous relative to the ch02
  baseline. `ch28`'s formal dialogue is deliberate and is a KEEP. The concession
  venue names in period "Theatre" spelling are correct, not locale strays.
- **Note QUALITY is good where notes exist.** Average note body about 67 words,
  fact-checked against real scholarship with real-vs-fiction and
  corroborated/uncorroborated/invention verdicts (the 32nd Army, the 4 April 1933
  Longhua execution, the T. V. Soong inference, the provisional romanizations all
  honestly flagged). The densification adds notes; it does not rewrite these.
- **Build and structure are current canon.** Full pending-aware hyperlinked TOC,
  cumulative single-spine build, embedded cover, colophon with the publisher
  discrepancy resolved, scene typography; `qa_epub` PASS. No structural work is
  owed.

Every prior retrofit over-predicted defect density by an order of magnitude.
This section is deliberately long to keep the pass small: the ONLY large item
is footnote density.

## 4. Defect inventory, ranked by value per keystroke

- **Tier A: mechanical consistency** (near-zero risk, grep-locatable; a few hours).
  - Date format: normalize the 11 `ch37` appendix dates from "Day Month Year" to
    the body's "Month Day, Year". (11 edits, one file.)
  - Locale strays: "a piece of theatre" x2 to "theater"; decide "Labour College"
    as a proper name (likely keep). (2 to 3 edits.)
  - "Shen Bao" article consistency: the 4 bare forms to "the Shen Bao" where a
    sentence wants the article. (up to 4 edits.)
  - authority.json conformance (commissioner's call, since these are recorded
    tolerated deviations): the six terms above, about 13 reading-text occurrences,
    plus the 白区 number. Grep-driven, global, with the glossary updated in lockstep
    and the notes that gloss the period forms adjusted. If declined, they stay as
    recorded deviations and nothing breaks.
  - Deliverable naming: `book.json` has no `deliverable` field and the file is the
    slug `out/thousand-li.epub`; the v2.4 policy wants "A Thousand Li of Rivers and
    Mountains.epub" as the build target, with per-round chat copies stamped
    ("... R1.epub") by `stamp_deliverable.py`. A one-line `book.json` add plus a
    rename at the next build.

- **Tier B: kill-list sweep** (semi-mechanical, by-ear per hit; low risk). The
  two batteries with material counts, each with its carve-outs: `could-only` (34;
  plain the archaic "had to" cases, leave the idiomatic) and `trailing-besides`
  (27; "as well"/"too"/cut). Smaller sweeps if wanted: `litotes` (14),
  `narration-ellipsis` (13), `nominalization` (12, ch34 cluster),
  `one-after-another` (10), `antique-fn-words` (15). No battery is large; the
  whole Tier B is well under 150 candidate lines and most will pass the read-aloud
  test unchanged.

- **Tier C: judgment work.** Two small items and one large one.
  - Register by-ear: `ch24`'s zero-contraction dialogue (one read; `ch28` already
    ruled a KEEP). The five long sentences for the spine test.
  - **The FOOTNOTE DENSIFICATION workstream (the headline).** The book runs 6.2
    notes per chapter against a 40-to-60 directive, with a 7.6x words-per-note
    swing to flatten. Sized honestly against the standard:
    - to the directive FLOOR (40/ch): **+1,150 new notes** (total ~1,360);
    - to the directive band midpoint (~50/ch): **+1,500 new notes**;
    - a pragmatic MODERATE retrofit (~25/ch, roughly quadrupling density and
      pulling the swing under 2x): **+640 new notes** (total ~850);
    - an evenness-only floor (lift the 11 thin chapters and the tail to ~15/ch,
      closing the swing but not reaching the band): **+300 new notes**.
    The quarry already exists: `glossary.json` holds 370 adjudicated referents
    (151 places, 82 people, 52 organizations, 85 terms) and only ~210 notes sit on
    the 34 chapters, so roughly 250 to 300 first-appearance referents (concession
    geography, tradecraft, the real historical figures, the brands and dishes and
    theater bills) can each seed a note without new research risk, each carrying
    its real-vs-fiction and corroboration verdict per CLAUDE.md's four coverage
    domains, with the lost-in-translation (idiom/allusion) layer swept on top.
    As a chapters-by-notes program: **34 chapters at roughly 20 to 35 new notes
    each** for the moderate-to-band target, run thinnest-chapter-first
    (`ch35`, `ch33`, `ch29`, `ch05`, `ch32`, then the eight-remaining thin tail).

## 5. Scores (relative to the genre's published English annotated-translation benchmark)

Scale 0 to 100; "now" is the shipped edition, projections are cumulative by tier.

- **Accessibility to a no-background reader: 68 now.** The prose is clean and
  self-explaining where it can be, but 6.2 notes per chapter under-serves a reader
  with no 1933-Shanghai background against a scholarly annotated benchmark: the
  concession streets, the underground tradecraft, the real figures behind the
  fictional ones go largely unglossed after first mention. After Tier A/B: ~70.
  After Tier C densification: **~90**.
- **Translation fidelity: 92 now.** Verbatim-quote QC, clean invariant checks,
  double and back translation, honest uncertainty flags. At the top of the
  benchmark. Tiers do not move it (the authority conformances are cosmetic to
  fidelity): **~92 throughout**.
- **Prose against native-authored peers: 86 now.** Clean tic profile, healthy
  rhythm, generous dialogue register, the book's own voice intact. After the Tier
  B sweep and the one `ch24` read: **~89**.
- **Overall: ~80 now.** After Tier A + B: ~82. After Tier C: **~90.**

The commissioner can buy the tiers separately; the accessibility axis is the only
one with real headroom, and densification is what moves it.

## 6. Verdict and commissioning proposal

**Recommended pass: DENSIFICATION (Tier C), with a cheap Tier A mechanical
ride-along and a light Tier B tic sweep. A full register rework is NOT
warranted:** the register and fidelity are already at standard, and the one real
gap against the current template is footnote density. This is a "densification"
pass in the section-4 taxonomy, not a "full register plus densification."

**Batch plan.** Run the densification on the book's own approved 12-batch spine
(B01 to B12, about 13k source characters each) as revision rounds R1 to R12, two
to five chapters per round, thinnest-chapter-first WITHIN the reading order so
the worst-served chapters lift earliest. Target the directive band; if the
commissioner buys the moderate tier instead, target about 25 notes per chapter.
Each round: source first-appearance candidates from `glossary.json` and the four
coverage domains, fact-check every new note against real scholarship (never an
AI-written source), verify every anchor is a verbatim substring with
`anchor_check.py` before applying, fold the Tier A conformances that fall in the
round's chapters, rebuild the cumulative EPUB, run the full check battery and
`qa_epub` to green, deliver the stamped EPUB in chat with the next kickoff, and
commit. Roughly +1,150 to +1,830 new notes to the band, or +640 at the moderate
target, over the twelve rounds.

**Explicitly out of scope:** rewriting any existing note; re-translating any
paragraph (the reading text is FROZEN except the Tier A conformances, which
change named renderings only, not sense); touching the build, TOC, cover,
colophon, or scene typography; re-opening the fidelity QC. Content is frozen and
most paragraphs LEAVE untouched: a densification pass adds apparatus, it does not
churn prose.

**Standing cautions.** The pass runs under `REVISION_PLAN.template.md` with
`anchor_check.py` before every apply. The FIRST act of the pass is the section-0
doctrine upgrade this read-only session deferred: replace the branch's
`CLAUDE.md`, `styles/`, shared scripts and templates with the current masters'
versions, compose `STYLE.md`, and set `book.json`'s `deliverable`, so the pass
follows current doctrine and the current (not the retired 3-notes) density model.
All work stays on `claude/thousand-li`.

### Drafted R1 kickoff

```
Read CLAUDE.md, then ASSESSMENT.md, then HANDOFF.md, then book.json. This is
densification round R1 of the retrofit commissioned in ASSESSMENT.md section 6.
Work only on branch claude/thousand-li; deliver the EPUB in chat at the end.

STEP 0 (doctrine upgrade, mandatory, before any note): from
origin/claude/translation-template-epub-master copy the current CLAUDE.md,
the whole styles/ directory, REVISION_PLAN.template.md, and every shared
script the branch still lacks (compose_style.py, apply_edits.py,
check_align.py, check_apparatus.py, apparatus_merge.py, verify_unit.py,
voice_gate_critique.py, check_style_freshness.py, qc_entities.py, reflow.py,
smart_quotes.py, apply_format_markers.py, check_content.py, check_reconcile.py).
Compose STYLE.md with compose_style.py. Add "deliverable":
"A Thousand Li of Rivers and Mountains.epub" to book.json. Commit as
"R1 step 0: doctrine upgrade to v2.4". Do NOT touch reading text in this step.

THEN R1 = B01 = ch02 Dice, ch03 Longhua, ch04 Miss Tao, ch05 Xuanwu Lake.
Densify to the directive band (aim ~30-40 notes per chapter; ch05 is thinnest
at 3 notes and gets the most). Source first-appearance candidates from
glossary.json (its 370 referents are the quarry) and CLAUDE.md's four coverage
domains, plus the lost-in-translation idiom/allusion layer. Every new note:
fact-checked against real scholarship (Wikipedia, Baidu Baike, academic and
museum sources; NEVER Grok/Grokipedia or any AI-written source), with its
real-vs-fiction and corroborated/uncorroborated/invention verdict; anchor a
verbatim substring of the English prose, verified with anchor_check.py before
apply_edits.py runs; note bodies XHTML with numeric character references.

Fold the Tier A conformances that fall in ch02-ch05: normalize any date to
"Month Day, Year"; conform authority.json decided names appearing here
(e.g. Massenet Road -> Route Massenet in ch04/ch05 if present, Da Mei Wan Bao
-> the Shanghai Evening Post and Mercury, the Wusong bar -> the mouth of the
Wusong River) with glossary.json updated in lockstep; leave every other
paragraph's sense untouched (content is frozen).

Run check_numbers.py, check_structure.py, register_tics.py, anchor_check.py,
then rebuild the cumulative EPUB and run qa_epub.py until green. Do not invent
bridging text; do not pause for approval mid-round. Commit. Rewrite HANDOFF.md
with the R2 kickoff as its first section. Deliver the stamped EPUB
"A Thousand Li of Rivers and Mountains R1.epub" (stamp_deliverable.py R1) as an
attached file in chat, and paste the R2 kickoff verbatim in the same reply.
```
