# HANDOFF — Owl's Castle (梟の城, Shiba Ryōtarō)

## THE BOOK IS COMPLETE

All twenty sections — the nineteen novel chapters (ch01–ch19) and the critical
afterword (ch20 解説) — are translated, annotated, and built into
out/owls-castle.epub. The completion report is **COMPLETION.md**; read that
first. There is no next batch to kick off. Further work is a corrections pass
only (see the corrections workflow in CLAUDE.md).

- Deliverable: out/owls-castle.epub, committed with git add -f on branch
  claude/owls-castle. qa_epub PASS (34 files, 27 documents); epubcheck 5.1.0
  0/0/0/0.
- 20 of 20 sections translated; 149 notes; 0 figures (text-only throughout, a
  recorded decision); glossary 113 people / 113 places / 30 terms.
- The title page and TOC report the book as COMPLETE — no pending markers.

## What B20 added (the afterword)

- ch20 解説 / Afterword, folios 653–660, 26 paragraphs, 19 notes. A third-party
  critical essay by the critic **Muramatsu Takeshi** (村松剛), rendered as
  modern appreciative literary criticism, not Shiba's period narrative.
- Fact-check correction carried into book.json and the EPUB: the critic's name
  reads Muramatsu **Takeshi**, not "Tsuyoshi" as the survey had it.
- All per-chapter checks green; noise.txt gained the Shōwa era-year dates
  (rendered as Gregorian years) and the name numerals in 道三 / 歳三;
  data/checks.json now registers ch20 for check_content.

## Do-not-revert list (accumulated script/config state)

- data/noise.txt entries (each carries a comment); the B20 additions included.
- data/checks.json docs+sources map (all 20 units, ch20 included).
- Builder features: sectioned glossary (add rows directly, not via
  apparatus_merge); note-anchor and figure-spec refusal gates; the (now fully
  resolved) TOC; pagebreak/page-list emission from data/pagemap/.
- The measured OCR crop for this book: jpn_vert psm 5, L0.035 R0.965 T0.075
  B0.955, --no-furniture-strip. Offset 0 (printed == PDF) holds unbroken from
  folio 406 through the afterword (653–660).

## If a corrections pass is opened

The commissioner files corrections in CORRECTIONS.md (or pastes them in chat, in
which case transcribe them there first). Global corrections cascade via a
glossary/style change plus a grep-driven edit across ALL built units including
note and glossary bodies, then rebuild and full QA. A zero-item corrections
batch is still a clean-checkout regression run. Open items noted in
COMPLETION.md for a human eye: the Jibu-no-shō / Jibu-no-shōyū court-title
variance, and the unused glossary form Imai Sōkun.
