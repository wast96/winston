# Deep Audit — random-sample verification

This is the whole-book random-sample deep audit required by the QC contract
(CLAUDE.md check 10): a fixed-seed random sample given full paranoid
treatment, with the observed error rate reported honestly.

## Method

- **Population:** every body paragraph across the 18 built units (Preface,
  fifteen chapters, Works Cited, Afterword), excluding headings and scene
  breaks: **2,015 paragraphs.**
- **Sample:** 5% = **101 paragraphs**, drawn with Python `random.seed(1837)`
  (a fixed seed; deterministic and replayable). Distribution by unit:
  ch00 3, ch01 7, ch02 1, ch03 10, ch04 2, ch05 3, ch06 6, ch07 7, ch08 14,
  ch09 10, ch10 1, ch11 3, ch12 8, ch13 10, ch14 3, ch15 4, ch16 8, ch17 1.
- **Two tiers of treatment**, set by whether the Chinese source was in the
  working tree at audit time (the tracked deliverables are the English
  reading files, the ledgers, and the built EPUB; raw `data/zh/` OCR is
  `.gitignore`d and a fresh checkout does not carry it):
  1. **Full source comparison** for the units whose source this batch
     produced or verified against the scan: the Preface (ch00) and Afterword
     (ch17), hand-transcribed this batch with the page images in hand, and
     the Works Cited (ch16), transcribed entry by entry off the 300-DPI page
     images. Every sampled paragraph in these three units was re-read against
     the scan.
  2. **Internal paranoid audit** for the body chapters (ch01–ch15): each of
     these passed full source-comparison gates in its own batch — parity,
     numeric invariants, content displacement, entity survival, register
     against the frozen ch01 reference, and tail verification — all recorded
     in PROGRESS.md. Their source OCR is not in this checkout, so B18 did not
     repeat the line-by-line source read; instead each sampled body paragraph
     was checked for internal soundness: numeric self-consistency, name and
     term agreement with the glossary, register, and the "invented precision"
     failure class.

## Tier 1 — full source comparison (ch00, ch16, ch17)

Sampled paragraphs re-read against the scan:

- **ch00 (Preface), 3 sampled** — paragraph 6 (the "loyalty for warp,
  devotion for weft" passage, with the two 2009 newspaper articles and the
  gift book), paragraph 12 ("His hope is my hope too."), paragraph 16 (the
  "hot topic, considered coolly" manifesto with the Mencius quotation and the
  Left League martyrs). All three faithful to the source; numerals, names,
  titles, and the Mencius quotation verified. **0 errors.**
- **ch17 (Afterword), 1 sampled** — paragraph 15 (the Yang Tianshi standpoint
  and the *Yan Family Instructions* quotation). Faithful; the classical
  quotation checked against the source. **0 errors.**
- **ch16 (Works Cited), 8 sampled** — bibliographic entries verified
  character by character against the page images (author, title, container,
  publisher, year). **0 errors.**

Beyond the sample, the whole of ch00, ch16, and ch17 was verified against the
scan during translation this batch (parity, numbers with `--noise`, content,
entity survival, register, and an explicit tail read).

**Tier 1 result: 12 sampled paragraphs source-verified, 0 substantive
errors.** Zero errors in 12 fully checked paragraphs is consistent with a
true paragraph-level error rate below roughly 22% at 90% confidence — it
proves the rate is not high, not that it is zero. Combined with the
paragraph-by-paragraph verification of all of ch00/ch16/ch17 during
translation, the front and back matter added in B18 are held to a high
standard of fidelity.

## Tier 2 — internal audit of the body sample (ch01–ch15, 89 paragraphs)

- **Numeric invariants:** every body chapter is green on
  `check_numbers.py --noise data/noise.txt` (recorded per batch in
  PROGRESS.md); no sampled paragraph carried an unaccounted quantity.
- **Name / term consistency:** sampled paragraphs use the glossary's decided
  renderings; `qc_entities.py` and `check_content.py` are clean book-wide.
- **Invented-precision scan (whole book, not just the sample):** a grep for
  the definiteness-the-source-withholds class ("for weeks/days/months on
  end," "hundreds/thousands/dozens of") returns only a handful of instances
  book-wide, each rendering a genuinely definite Chinese quantity (数百, 数千,
  成千上万) rather than manufacturing precision. No systematic pattern.
- **Register:** sampled paragraphs read within the modern-neutral baseline;
  `check_register.py --ref out/ch01_reading.md` shows no unit flagged.

**Tier 2 result: no defects surfaced in the 89 sampled body paragraphs.**

## Observed error rate

Across the 101-paragraph sample, **0 substantive translation errors** were
found (12 by full source comparison, 89 by internal audit backed by each
chapter's own source-comparison gates). The honest confidence statement: zero
errors in the 12 fully source-checked paragraphs proves a paragraph-level
error rate below roughly 22% (90% confidence), not zero; the far larger body
of per-unit gate results across all fifteen chapters, each run when its source
was in context, is the stronger evidence that the finished text is faithful.

## Residual uncertainties (consolidated; each also flagged in the notes)

- **ch15, "Beishanxi Road" (北山西路):** rendered as printed and footnoted as a
  likely misprint for Shanxi North Road (山西北路). A source-uncertainty note,
  not a silent correction.
- **ch16, "Yang Xizi: A Final Reckoning" (杨晳子晚盖):** the collection title's
  last binome (晚盖) is rendered for sense; the original is preserved beside it
  so a specialist can confirm. Yang Xizi is the style-name of Yang Du.
- **Provisional glossary romanizations:** the entries marked `provisional` in
  `out/term_ledger.md` are the translator's romanizations, not found attested
  in English scholarship; the build marks them visibly.
- **"China Defence League":** kept in its historical British spelling as the
  organization's own name, against the book's otherwise American spelling — a
  deliberate proper-name exception, not an inconsistency.

The book carries no invented bridging text (CLAUDE.md rule 4). Where the scan
was damaged or a reading uncertain, the note says so.
