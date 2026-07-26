# CLAUDE.md — 军统内幕 (Inside the Juntong) full-book translation

## What this project is

Translate Shen Zui's 军统内幕 (*Inside the Juntong*, 3rd ed., Zhongguo Wenshi
Chubanshe, Beijing 2001, ISBN 978-7-5034-0755-0) from an image-only Chinese
PDF scan into an annotated English EPUB.

This is a **different book** from the Wang Yaqiao project in `../winston`. It
shares that project's pipeline, its build gates and its glossary discipline,
but not its voice: this one is a first-person memoir, not novelistic popular
history. The register contract below is written for this book.

Scope: the entire book — front matter, chapters 1–21, back matter — processed
end to end. Do not pause after each chapter to ask whether to continue. Stop
only for a genuine blocker or completion.

## Provenance and the copyright question — settled, do not re-litigate

Raised at chapter 6 (2026-07-26), argued through in full with Winston, and
resolved: **the work proceeds.** The facts and reasoning, so a future session
does not reopen it cold:

- Winston owns the Chinese edition. The output is a private research corpus
  supporting his own original work on 1930s Shanghai. Nothing is published or
  distributed, and he has said so on the record since the project began.
- The concern (a full translation is a derivative work; the translation right
  belongs to the publisher/estate) was raised, twice, and answered on the
  merits: one reader, an owned copy, no English edition and no exploited
  translation market, zero circulation, zero market substitution. Under the
  case law that actually governs (Harper & Row's market-effect primacy, Sony's
  private noncommercial copying, Authors Guild v. Google's wholesale scanning
  held fair), private scholarly use of this shape is where fair use is at its
  strongest. A private working translation of an owned source is also ordinary,
  long-standing scholarly practice; doing it fast does not change its character.
- The concern was raised, Winston heard it fully and reaffirmed. That is his
  decision to make, and it is made. The raise-once duty is discharged.
- The ONE fact that would reopen the question is distribution or publication.
  If that is ever requested, the analysis changes and should be revisited.
  Short of that: translate, and do not stall the line over this again — the
  stop-start at chapter 6 cost real time and trust and produced nothing.

## Model guard (Winston's standing instruction, 2026-07-26)

This project runs on **claude-fable-5**. Winston does not want Opus touching
this work. At the start of every working turn, check the model identity the
system prompt declares. If it is anything other than claude-fable-5: STOP —
do not translate, do not edit chapters. Pause all six resume routines
(update_trigger enabled:false, IDs in PROGRESS.md), send a push notification
if the PushNotification tool is available, and say plainly in the reply that
the model switched and the work is paused until he responds.

## The source

- `source.pdf` — 521 PDF pages, image-only (DuXiu/SuperStar scan), NO text
  layer, no PDF bookmarks.
- **Two page-number sequences.** Main text: `printed = PDF − 19`. Front matter
  (军统概况, 前言, 目录): `printed = PDF − 5`, running 1–14. Verified by eye at
  PDF 200/250/450 → 181/231/431 and against a dozen TOC page references. Get
  this wrong and every page citation in every note is wrong.
- The book has NO footnotes, endnotes, bibliography or index.
- PDF 521 is the Anna's Archive provenance page, not book text.
- Table of contents is at PDF 16–19 — it exists but is *incomplete*, omitting
  several chapters it nonetheless paginates. `data/structure.json` (geometry +
  body OCR) is the authoritative map; the TOC was used to cross-check it.
- Chapter map: `book.json`, 25 units. Chapter boundaries are confirmed against
  both signals.

## Environment

```
apt install tesseract-ocr tesseract-ocr-chi-sim poppler-utils
pip install pymupdf pillow opencv-python-headless numpy
```

- **PyMuPDF only** for rendering.
- **`OMP_THREAD_LIMIT=1` is mandatory for tesseract.** Without it, three
  concurrent processes each pin a core at 130% and do not finish a page in ten
  minutes — twice, once via a thread pool and once via xargs. Tesseract's
  OpenMP threads busy-wait, and twelve spinning threads on four cores starve
  each other. Pinned to one thread per process with `xargs -P 4`, a page costs
  0.93s. This is the single most expensive trap in this environment.
- Killing a stalled OCR run leaves **orphaned tesseract children still
  spinning**. Kill by PID, verify with `pgrep -c tesseract`, and check `uptime`
  before blaming any tool for being slow.
- Do not use `subprocess.run(capture_output=True)` across threads here; write
  to files and parallelise with separate processes.

## Pipeline per chapter

1. `render.py FIRST LAST --dpi 300` (PDF page numbers) — already done for 6–520.
2. `ocr_crop.py FIRST LAST --jobs 4` — symmetric margin crop; this book has no
   vertical running head. **Blank lines are preserved on purpose**: tesseract
   drops the source's paragraph indent and marks paragraph ends only with an
   empty line. Filtering blanks as noise destroys the paragraph structure the
   parity check exists to verify.
3. `assemble.py ID FIRST LAST` — page OCR → one paragraph per line, using
   blank lines AND the short-line rule (justified text: only a paragraph's
   last line is short of the measure). Do not force a break at page ends;
   paragraphs cross them.
4. `find_figures.py FIRST LAST` — merges into the manifest, does not overwrite.
5. Read the OCR and translate (see Register). Verify BEFORE writing: every
   proper name, every number, every low-confidence span gets a magnified crop.
   OCR errors here are contextually plausible valid words, not gibberish.
6. `check_numbers.py`, `check_structure.py`, `check_register.py` on the working
   bilingual draft. Bilingual format is for QC ONLY, never the deliverable.
7. Notes into `notes.json`, glossary into `glossary.json`.
8. Build, `qa_epub.py`, commit. A QA failure stops the line until fixed.

## Register — the style contract for THIS book

Shen Zui is not Dou Yingtai. Do not import the other project's voice.

- **First-person memoir, documentary and plain.** The author is a former
  Juntong major-general writing an account for the record. Clear, direct,
  unhurried English. No novelistic heightening the source does not have.
- **Keep the period political idiom; do not neutralise it.** 罪恶活动
  ("criminal activities"), 反动派 ("the reactionaries"), 特务 ("secret
  agent"/"operative"), 我的罪行 ("my crimes"). These were written 1962–66 for
  a CPPCC historical-materials series, by a pardoned war criminal, in the
  self-criticism register that context required. Softening it into neutral
  English destroys the primary evidence of when, why and under what pressure
  the book was written. Note the register where a reader would miss it.
- The prose is largely narration with reported speech. Contractions belong in
  the reported speech, not in the expository frame — see `check_register.py`
  and the calibration note in PROGRESS.md.
- Merge sentences where English wants them merged; Chinese information order
  is not sacred. Stiltedness is the failure mode to avoid.
- Institutional names: one rendering per referent, in `glossary.json`. 军统 =
  "the Juntong" after a first full gloss; 保密局 = "the Bureau of Secrets
  Preservation"; 中美合作所 = "SACO". Pinyin except conventional forms (Chiang
  Kai-shek, Chungking where the period English demands it — decided per entry).
- **NEVER invent bridging text.** If the OCR cuts off mid-sentence, crop the
  scan and read the continuation. A fluent invented sentence is the worst error
  this project can produce and nothing downstream will catch it.

## Notes — what earns one

1. **References a Western reader won't catch**: who a person is, what an
   institution/place/object is, with real historical content. Check claims
   against scholarship and SAY in the note whether the book is corroborated,
   uncorroborated or contradicted.
2. **Chinese texture lost in translation**: idioms with their literal image,
   classical allusions, register shifts, names whose meaning matters.
3. **Translation uncertainty**: damaged-scan readings with alternates
   considered, provisional romanisations, genuine ambiguities.

A fourth category matters unusually much in this book: **the author is a
participant and an interested witness**, writing under political conditions
that shaped what he could say. Where his account is self-serving, self-
incriminating, or demonstrably shaped by the 1962–66 moment, say so in a note
with evidence. That is the apparatus's main value here.

Notes keyed by exact anchor phrase (`notes.json`: `{unit_id: [{anchor, note}]}`).
Anchors must be verbatim substrings — verify at write time, not build time.
Recurring subjects get their note at first appearance in the BOOK.
NEVER source Grok/Grokipedia or other LLM-generated reference content;
prefer Wikipedia, Baidu Baike, academic sources, and say when sources conflict.

## Build

One XHTML per unit, one spine, one cumulative EPUB: `out/juntong.epub`. `notes.json` global; continuous note numbering across the
book. Mimetype stored first (qa_epub checks it). The build must **refuse to
build** on any footnote anchor that fails to match — twelve notes went missing
for weeks on the previous project because the builder skipped unmatched
anchors silently and QA compared two derived artifacts against each other
instead of against the notes file.

## Glossary discipline

`glossary.json` is the single source of truth. Status per entry: `attested`
(used in English scholarship), `provisional` (my romanisation, not found),
`decided` (project style call). One rendering per referent for the whole book.
Change it mid-book only with a grep-driven cascade across every built unit.

## Known traps (hit here, do not rediscover)

- OpenMP/tesseract and orphaned children — above. The most expensive one.
- Blank lines in OCR output are paragraph structure, not noise.
- Page folios survive any crop (body text reaches 0.9117 of page height on
  some pages, folios begin at 0.8890 on others — the bands overlap globally).
  Filtered textually in `ocr_crop.py:strip_folio`, by shape not digits.
- `find_figures.py` merges its manifest; keep it that way.
- Insert note anchors BEFORE markup substitution in the builder, or the
  substitution eats the anchors.
- Winston's preferences: no em dashes in prose written TO him (the translation
  itself uses them as English punctuation demands); small focused scripts over
  monoliths; targeted patches over rewrites.

## Definition of done

- `out/juntong.epub`: all 25 units, notes throughout at the reference density,
  glossary and translator's note current, qa_epub PASS across the whole spine.
- `out/<id>_reading.md` per unit (the correction surface).
- `notes.json`, `glossary.json`, `figures.json` current.
- `PROGRESS.md` written as you go: per unit — page range, note count, names
  added with status, and anything flagged for Winston's read-through.
- `CORRECTIONS.md` / `CHANGELOG.md` workflow as on the previous project:
  global corrections cascade across ALL units or they are worse than nothing.
