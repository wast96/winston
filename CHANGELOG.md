# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

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
