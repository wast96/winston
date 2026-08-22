# COMPLETION.md — The Sword Roars in the West Wind

Written on the final batch (B18) in place of another handoff. This is the
document to read to know what the finished edition contains and how far to
trust it. (No em dashes, per the working rules.)

## Status at a glance

- **18 of 18 units translated:** the Preface, fifteen body chapters, the
  Works Cited, and the Afterword.
- **425 footnotes**, continuous book-wide.
- **77 figures**, every one hand-cropped, with real screen-reader alt text and
  a translator's caption whose provenance is stated.
- **Glossary: 1,140 rows** (people 757, organizations 115, places 227, terms
  41), rendered for a non-Chinese reader as `out/term_ledger.md`.
- **qa_epub: PASS** (111 files, 27 documents, 425 references / 425 bodies /
  425 backlinks, all links resolve).
- **epubcheck 5.1.0 (EPUB 3.3): 0 fatals / 0 errors / 0 warnings / 0 infos.**
- **Deliverable:** `out/The Sword Roars in the West Wind.epub`, committed to the
  branch `claude/the-sword-roars` (branches outlive containers, chat
  attachments do not). Renamed from `out/sword-roars.epub` in the 2026-08-22
  corrections pass to carry the book's full name; content unchanged.

## What the finished edition contains

- **Front matter:** typographic-free painted cover (the source's front-cover
  painting, embedded byte-identical); title page stating honestly that the
  build is complete; an expanded translator's note on conventions (pinyin
  romanization, the concession street-name policy, currency, li, and the
  crucial warning that "our Party," "reactionaries," and "running dogs" are
  the author's voice, preserved deliberately); a Principal Characters page; a
  full hyperlinked table of contents.
- **The Preface** ("History Must Not Be Made a Monster"): the author's frame
  for the whole book, the interested-witness voice at full volume, footnoted
  at reader-model density (the Double Hundred campaign, Li Bai the radio
  operator, the Three Heroes of Longtan, the Lurk pun, historical nihilism,
  the Mencius and Lu Xun references, and the rest).
- **Fifteen chapters** telling the hidden war of the Central Special Branch
  street by street, 1927 to 1935.
- **Back matter:** the Street Gazetteer (old and period names to today's);
  the Glossary of Recurring Terms; a bilingual **Works Cited** (books,
  periodicals, newspapers, 178 entries, each with an English rendering and the
  Chinese original so a scholar can trace it); the **Afterword** ("Keep to
  Poverty, Endure the Silence"); and the continuous Notes page (notes also
  render as pop-ups over the text in Apple Books and Kindle).
- **Set-off conventions used:** none of the vignette, dateline, hour-gloss, or
  verse markers were needed in the front or back matter; cited memoir and
  document passages read as normal paragraphs with a colon lead-in or a
  "(Name, year)" attribution, as in the body chapters.
- **Deliberately NOT invented to fill a slot:** `back_matter.json` remains
  inert (no errata table, no colophon) because the book has neither; the Works
  Cited is rendered as its own reading unit (ch16) rather than through the
  errata/colophon machinery. No bridging text was invented anywhere
  (CLAUDE.md rule 4).

## Per-chapter tally

| Unit | Title | Paragraphs | Notes | Figures |
| --- | --- | --- | --- | --- |
| ch00 | Preface: History Must Not Be Made a Monster | 24 | 15 | 0 |
| ch01 | No Concealment, No Survival | 165 | 92 | 12 |
| ch02 | The Clean Stay Clean, the Foul Stay Foul | 56 | 28 | 5 |
| ch03 | Who Is Judas | 146 | 34 | 4 |
| ch04 | Bloodshed on Avenue Joffre | 131 | 24 | 10 |
| ch05 | A Real Vault, a False Marriage | 66 | 28 | 5 |
| ch06 | It Was Not Me, It Was the Wind | 165 | 30 | 3 |
| ch07 | The Great Hermit Hides in the City | 99 | 26 | 6 |
| ch08 | A Nanjing Night, Deadly Urgent | 252 | 28 | 4 |
| ch09 | The Riddle of Xiang Zhongfa's Disappearance | 194 | 27 | 5 |
| ch10 | Opening a Shop, Doing Trade | 39 | 15 | 3 |
| ch11 | The Wild Swan | 82 | 19 | 3 |
| ch12 | A Purge in the Red-Light District | 139 | 15 | 2 |
| ch13 | Twin Lotus on One Stem | 139 | 17 | 4 |
| ch14 | "Secret Number One" | 66 | 12 | 7 |
| ch15 | The Last Effort | 55 | 10 | 4 |
| ch16 | Works Cited | 179 | 0 | 0 |
| ch17 | Afterword: Keep to Poverty, Endure the Silence | 18 | 5 | 0 |
| | **Total** | **2,015** | **425** | **77** |

## Batching as executed

- Survey (structure, offsets, style contract, skeleton EPUB).
- B01 = ch01 (voice gate); B02 = ch02; B03 = ch03; B04 = ch04; B05 = ch05;
  B06 = ch06; B07 = ch07; B08 = ch08.
- B09: commissioner register review, a whole-book register rebaseline written
  into STYLE.local, itemized corrections and a de-archaizing pass over
  ch01-ch08; dates set to month-day-year book-wide.
- B10: two builder features (Glossary of Recurring Terms, Street Gazetteer);
  footnote-placement sweep; ch01 thinned; ch07/ch08 backfilled.
- B11 = ch09; B12 = ch10; B13 = ch11; B14 = ch12; B15 = ch13; B16 = ch14;
  B17 = ch15 (the last body chapter).
- B18 (this batch): the Preface (ch00), the Works Cited (ch16), the Afterword
  (ch17); the whole-book reconciliation sweep; cover confirmation; and this
  completion report. No deviation from the approved batch plan.

## Checks run book-wide, and what they found

- **Numeric invariants** (`check_numbers.py --noise data/noise.txt`): green on
  every unit; the noise file carries per-batch blocks (longest literal first),
  including the B18 additions for 双百 / 老百姓 (ch00) and the ch17 idioms
  (千变万化, 一不买二不看, 两无声), none of which is a quantity.
- **Parity, anchors, heading shape**: 24=24 (ch00), 18=18 (ch17); Works Cited
  is a bibliography, not parity-checked prose.
- **Entity survival** (`qc_entities.py`) and **content displacement**
  (`check_content.py`): clean across all pairing units.
- **Alignment** (`check_align.py`): every unit within tolerance.
- **Register** (`check_register.py --ref out/ch01_reading.md`): ch00 and ch17
  within tolerance of the frozen ch01 reference; no unit flagged stilted.
- **Apparatus** (`check_apparatus.py`): 0 failures, 0 warnings, after the
  title-italics anchor updates.
- **Whole-book reconciliation** (`check_reconcile.py`): epithet drift 0
  candidates; 1,120 of 1,140 decided forms present in the text (the 20 unused
  are recurring terms that surface only in notes, or short-form variants the
  prose uses instead, all legitimate). Resolved this batch:
  - "Soong Ching-ling" to **Song Qingling** (the decided form; the T.V. Soong
    / Soong Ai-ling / Soong Mei-ling conventional names are unchanged).
  - "Dapu" already clean; **Dabu** stands book-wide.
  - ch01 Yang Du note birth year 1875 to **1874**.
  - ch09 "Fourth Avenue" to **Sima Road** for 四马路 (matching the gazetteer).
  - **Title italics unified:** book and periodical titles in ch10-ch13, which
    had been plain, are now italic like the rest of the book; four note
    anchors that quoted a title were updated in step.
  - **Spelling locale:** "Grand Theatre" to **Grand Theater** (American,
    matching the book's 27 "theater" against the lone "theatre"). The three
    "China Defence League" instances keep the organization's own historical
    British spelling, a deliberate proper-name exception.
  - **Latent caption bug fixed book-wide:** figure captions and alt text that
    stored numeric character references (&#8217; and the like) were
    double-escaped by the builder's HTML-escape step and would have rendered
    as literal entity text; all 16 affected caption/alt fields (ch02, ch13,
    ch14) were converted to plain ASCII quotes, which the render layer curls
    correctly. Verified in the built EPUB.
- **Scholarship consistency** (rule 5): notes state corroborated /
  uncorroborated / contradicted; no source cites Grok or any AI-written
  reference.

## Observed error rate

See `out/deep_audit.md`. A fixed-seed (1837) random 5% sample of 101
paragraphs was drawn across all 18 units. The units whose source is in the
working tree (the B18 Preface and Afterword, plus the Works Cited checked
against the page images) were given full source comparison: 12 sampled
paragraphs, 0 substantive errors, on top of the paragraph-by-paragraph
verification of all of ch00/ch16/ch17 during translation. The body chapters,
whose OCR source is not carried in a fresh checkout, each passed full
source-comparison gates in their own batch; their sampled paragraphs were
audited internally (numbers, name and term consistency, register, and an
invented-precision scan that found no systematic problem). Honest confidence:
zero errors in the 12 fully source-checked paragraphs proves a paragraph-level
error rate below roughly 22% at 90% confidence, not zero; the far larger body
of per-unit gate results is the stronger evidence of fidelity.

## Findings that need the commissioner's eye

- **The book is an interested witness, deliberately preserved.** It speaks
  from inside the Party's own tradition and celebrates its subjects; footnotes
  mark where the celebration outruns the record or the account is self-serving,
  but the framing itself is the author's and is kept.
- **Cross-book naming for a later reconciliation pass** (recorded in
  authority.json as `reconcile`): this book renders 三马路 "Sanma Road", 四马路
  "Sima Road", 伍豪 "Wuhao", and 马斯南路 "Rue Massenet", which differ from some
  other shelf books' choices. These are per-book decisions, correct within
  this book; the shelf can reconcile them between books.

## Residual uncertainties a reader should know about

- **ch15, "Beishanxi Road" (北山西路):** rendered as printed and footnoted as a
  likely misprint for Shanxi North Road; a reading-uncertainty note, not a
  silent correction.
- **ch16, "Yang Xizi: A Final Reckoning" (杨晳子晚盖):** the title's last binome
  is rendered for sense with the original preserved beside it; Yang Xizi is the
  style-name of Yang Du.
- **Provisional glossary romanizations:** the entries marked `provisional` in
  `out/term_ledger.md` are the translator's romanizations, not found attested
  in English scholarship; the build marks them visibly.
- No damaged-scan gaps were left unread and no bridging text was invented.

## Provenance and method

- **Source:** 剑吼西风：中央特科纪事 by Ye Xiaoshen (叶孝慎), Gold Wall Press
  (Jincheng Chubanshe), Beijing, 1st ed. 2021.6, ISBN 978-7-5155-2038-4. An
  image-only PDF scan, 350 pages, no text layer. Printed-to-PDF offset a
  constant 15 (printed = pdf - 15); the Preface runs its own roman-numeral
  sequence.
- **Pipeline:** PyMuPDF render at 300 DPI; tesseract (chi_sim, psm 6) with a
  measured crop (--left 0.06 --right 0.95 --top 0.11 --bottom 0.955) as a
  cross-check only; the proper names and dense passages were hand-transcribed
  off the 300-DPI page images, which OCR could not be trusted on. Translation
  verified per unit (parity, numbers, content, entities, register, tail read)
  and built into one cumulative EPUB driven entirely by book.json.
- **Deliverables:** `out/<id>_reading.md` per unit (the correction surface),
  `out/term_ledger.md`, `out/deep_audit.md`, `notes.json`, `glossary.json`,
  `figures.json`, `book.json`; `authority.json` updated with this book's
  decided renderings; the built `out/The Sword Roars in the West Wind.epub`
  committed.

## Further work

The book is complete. Any further work is a **corrections pass**: the
commissioner reads the EPUB and files items in `CORRECTIONS.md` (or pastes
them in chat for transcription). A corrections pass with zero items is still a
clean-checkout regression run. Global corrections cascade through a
glossary/style change plus a grep-driven edit across all built units, then a
rebuild and full QA; local corrections are a fix at one spot. After any
corrections batch: rebuild, qa_epub, list every file touched, and add a dated
entry to CHANGELOG.md.
