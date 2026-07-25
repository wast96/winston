# PROGRESS — 军统内幕 / Inside the Juntong

Working state. Updated as each unit lands.

## The book

Shen Zui (沈醉), 军统内幕, 3rd ed., Zhongguo Wenshi Chubanshe, Beijing 2001,
ISBN 978-7-5034-0755-0. 521-page image-only scan, no text layer, no bookmarks.
515 pages of book text, ~338,000 Han characters by OCR count (the CIP page
claims 418,000 字, which counts punctuation and front matter).

A memoir, not a narrative history: twenty-one free-standing chapters, most of
them written between 1962 and 1966 for the CPPCC's *Selected Historical
Materials* and collected here. The author was a Juntong major-general.

## Verified structure

- **Two page-number sequences.** Main text: printed = PDF − 19. Front matter
  (概况, 前言, 目录): printed = PDF − 5, running 1–14. Confirmed by eye on the
  magnified footers of PDF 200/250/450 → 181/231/431, and cross-checked against
  a dozen page references in the book's own contents pages. The front-matter
  sequence is why the first offset measurement (PDF − 5, taken on page 10) was
  wrong for the body of the book; anything citing pages before this was settled
  would have been off by fourteen.
- The scan's contents pages (PDF 16–19) exist but are **incomplete** — they
  omit several chapters they nonetheless paginate. The authoritative map is
  `data/structure.json`, recovered from heading geometry and confirmed against
  the contents pages where those do list an entry.
- 25 units: 2 front matter, 21 chapters, 2 back matter. See `book.json`.
- One chapter was missing from the geometric pass and found by probing the gap:
  保密局内幕 (Inside the Bureau of Secrets Preservation), printed 392.
- PDF 521 is the Anna's Archive provenance page.

## Pipeline state

Rendered: all 520 pages at 300 dpi. OCR'd: all 515 text pages. Both complete;
the per-chapter work from here is assemble → verify → translate → check.

## Environment findings worth keeping

- **`OMP_THREAD_LIMIT=1` on tesseract is mandatory.** Without it three
  concurrent processes each pinned a core at 130% and did not finish a single
  page in ten minutes — twice, once through a Python thread pool and once
  through xargs. Tesseract's OpenMP threads busy-wait; twelve of them on four
  cores starve each other rather than sharing. Pinned, with `xargs -P 4`, a
  page costs 0.93s and the whole book OCRs in about six minutes. This cost
  roughly an hour to diagnose and is the single most expensive trap here.
- Killing a stalled run **orphans the tesseract children**, which keep
  spinning and slow everything afterwards. Kill by PID and verify with
  `pgrep -c tesseract`.
- Blank lines in the OCR output are the **only** paragraph signal the file
  carries — tesseract drops the source's two-space indent. The first OCR pass
  filtered them as noise and had to be redone.
- Page folios cannot be cropped away: the last body line reaches 0.9117 of
  page height on some pages while the folio starts at 0.8890 on others, so the
  bands overlap globally. Filtered by shape in `ocr_crop.py:strip_folio`.

## Register baseline — NEEDS WINSTON'S SIGN-OFF

There is no approved reference chapter for this book yet, and the skill's whole
per-chapter drift check is measured against one. `fm01_gaikuang` is proposed as
that baseline: institutional prose, first person, plain and documentary, period
political idiom preserved rather than neutralised.

**This is the one thing worth reading before the rest of the book is
translated**, because everything after it is measured against it. If the voice
is wrong, it is wrong once here and twenty-four times later.

Specific choices made in it, all reversible:
- 军统 glossed once in full, then "the Juntong" throughout — the book's own usage.
- 重庆 as "Chungking", the period English form, not "Chongqing".
- 委员长 as "the Generalissimo".
- 臭招牌 kept literal as "stinking signboard", with a note on the register.
- Chapter title 军统概况 as "An Outline of the Juntong".

## Register baseline: the dialogue half is NOT yet set

`fm01_gaikuang` works as the baseline for the expository voice, but it contains
no dialogue at all, so its dialogue-contraction rate is 0.0/1k and measuring
anything against it is measuring nothing: the ratio comes out 1.00x whatever
the chapter does. The preface reads 13.2/1k against it and the check reports
"within tolerance," which is true and uninformative.

The dialogue baseline has to be reset from the first unit that has real
dialogue. Until then, treat the contraction column as unmeasured rather than
passing. The "shall" share is the usable signal in the meantime: it caught one
line in the preface where Zhou Enlai's warm, plain send-off had been given a
formal "I shall," which is exactly the drift the check exists for, and it is
now "I'll."

## Per-unit log

### fm01_gaikuang (军统概况 / An Outline of the Juntong) — DONE

- PDF 6–9, front-matter printed 1–4. 18 source paragraphs, 18 translated.
- **13 name mangles caught by crop verification**, every one of them a
  plausible-looking valid word rather than obvious garbage — the defect class
  the dual-OCR disagreement filter cannot see, because both psm configurations
  make the same mistake on the same glyphs:
  郑锡鹿→郑锡麟, 岂料→酆悌, 潘估强→潘佑强, 印开基→邱开基, 候志明→侯志明,
  徐因曾→徐恩曾, 贺友组→贺耀组, 钱大钓→钱大钧, 林幸→林蔚, 玫珈山→珞珈山,
  番戒委员会→惩戒委员会, 一九八年→一九八〇年, and 张国琳→**张国焘**.
  The last is the one that mattered: Zhang Guotao, a founder of the Chinese
  Communist Party, running a Juntong research office — OCR had turned him into
  a nobody, and nothing but the scan would have caught it.
- Checks: parity 18/18, anchors 12/12 resolve, headings consistent, numbers
  0 unresolved across 18 pairs.
- Notes: 12 (3.0 per printed page).
- Glossary: +32 entries (75 total).
- **Three real tool bugs found and fixed**, all of which would have produced
  false confidence rather than noise:
  1. `check_structure.check_parity` dropped a source line as the "chapter
     title" even when the title had already been removed as a heading, biasing
     every parity count by one — in the direction that hides a dropped
     paragraph, which is the defect the check exists to find.
  2. `check_numbers.cn_to_int` could not read 百/千/万, so 一千四百 fell apart
     into a stray 四 and reported a dropped number that was not dropped.
  3. A NOISE entry (`[一二三]十`) ate the first half of 二十九 and left a bare
     九 behind — the exact prefix-eating trap the script's own comment warns
     about, recurring with a different pair.

### fm02_qianyan (前言 / Preface) - DONE

- PDF 10-15, front-matter printed 5-10. 15 source paragraphs, 15 translated.
- Crop verification caught five more source errors, two of which the numeric
  check had already flagged from the other direction: 十和年 for 十八年
  (eighteen years) and 十别总理 for 辞别总理 (took leave of the Premier), both
  of which left a stray 十 that read as a dropped "10"; plus 黄效先生 for
  黄雍先生 (Huang Yong, a CPPCC member and one of the original Ten-Man Team),
  郑锡记 for 郑锡麟, and 周因来 for 周恩来.
- Checks: parity 15/15, anchors 14/14, numbers 0 unresolved, register within
  tolerance (but see the baseline caveat above).
- Notes: 14 (2.3 per printed page).
- EPUB built and QA PASS: 2 documents, 33 paragraphs, 26 notes, all references,
  bodies and backlinks matching.

### Two more tool fixes this unit

- `qa_epub.py` identified chapter documents by matching `prologue|chNN` in the
  filename, so it reported "0 documents, 0 paragraphs" for a spine made of
  front matter and did not notice it had measured nothing. It now derives
  content documents from the spine by excluding the known apparatus documents,
  so a unit named anything at all is still checked. This is the last gate
  before a build ships and it must not depend on a naming convention it does
  not itself enforce.
- `check_numbers.py`: a noise pattern beginning with a numeral could eat the
  TAIL of a longer numeral (一日 fired inside 二十一日 and left 二十, reported
  as a dropped "20"). All such patterns are now guarded with a lookbehind.
  Also added "a million" to the English reader.

### New in the pipeline: a correction ledger

`data/ocr_fixes.json` plus `scripts/apply_fixes.py`. Crop verification is the
most expensive step here and its results were the most perishable: `data/txt/`
and `data/zh/` are untracked, so a fresh checkout re-runs OCR and quietly
reinstates every mangle already paid for - 张国焘 reverts to 张国琳. Every
verified reading is now recorded with the page it was checked on and why, and
replayed by script. 18 entries so far.

### FOR WINSTON'S READ-THROUGH, fm01

- The scholarship pass is **not yet run** for this unit. The twelve notes rest
  on general knowledge of the period and are written to be checkable; claims
  that need external verification (the Lixingshe founding roster, Feng Ti's
  execution, the Dai Hill crash site) are flagged as such in the note text
  rather than asserted flatly. Per the skill's cost model, research is batched
  across several chapters rather than run per chapter — that pass is pending.
- The book prints 戴山 for the hill Dai Li's aircraft struck, where other
  sources give 岱山. Preserved as printed and noted; not silently corrected.

## Pending decisions

- **Chapter 1 contains an appendix printing the full lyrics of the training
  class song** (附录:班歌歌词全文, printed p.40). Intention is to characterise
  and summarise it — what it says, what register it is in, what it tells you
  about the institution — rather than set out a complete lyric translation.
  Say if you want it rendered in full instead.
- Note numbering runs continuously across the book (decided; implemented in
  neither builder nor QA yet — the builder is the next engineering task).

## Next steps, in order

1. Generalise `build_reading_epub.py` and `qa_epub.py` from the previous
   project's chapter-1 shape to this book's 25 units, with the anchor gate that
   refuses to build on an unmatched anchor.
2. fm02_qianyan (前言), PDF 10–15 — source already assembled.
3. Chapters 1–21 in order, per the pipeline in CLAUDE.md.
4. Batched scholarship pass, covering several chapters at a time.
5. Final sweep per the skill: re-run every script, register across the whole
   spine, historical pattern analysis, random-sample deep audit.
