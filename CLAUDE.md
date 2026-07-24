# CLAUDE.md — 中国暗杀王：王亚樵 full-book translation project

## What this project is

Translate Dou Yingtai's 中国暗杀王：王亚樵 (China's King of Assassins: Wang
Yaqiao, 2nd ed., Tuanjie Publishing House, Beijing 2007, ISBN
978-7-80130-758-3) from a scanned Chinese PDF into an annotated English
EPUB. Chapter 1 is already done and shipped; it is the quality bar and the
style contract. Everything in `reference/` is the standard to match.

**Scope: the ENTIRE remaining book — prologue (小引) and chapters 2
through 15 — processed end to end without stopping for review.** Winston
will read the finished product afterward and issue corrections that
cascade globally (see Corrections workflow below). Do not pause after each
chapter to ask if you should continue. Do not ask permission to proceed to
the next chapter. Only stop for: (a) a genuine blocker you cannot resolve,
(b) completion.

## The source

- `source.pdf` — 336 PDF pages, image-only scan, NO text layer. Mixed
  DCTDecode and JBIG2 streams.
- PDF page = printed page + 10. This offset is constant; verify it once on
  chapter 2's opener and then trust it.
- The book has NO footnotes, endnotes, bibliography, or index (verified
  structurally and by reading the back matter). Do not hunt for them.
- PDF page 336 is an Anna's Archive provenance page, not part of the book.
- Front matter: cover (p1), title/CIP (p2-5), TOC (p6-8), prologue 小引
  starts printed p1 (PDF 11).
- Chapter map (printed pages, from the TOC — re-OCR PDF 6-8 at the start
  to complete and confirm the middle chapters, the TOC scan is readable):
  小引/1, ch1/9, ch2/27, ch3/43, ch4/57 ... ch13/259, ch14/281, ch15/299.
  Book text ends printed p325.

## Environment setup (first run only)

```
sudo apt install tesseract-ocr tesseract-ocr-chi-sim poppler-utils   # poppler for pdfimages only
pip install pymupdf pdfplumber pillow opencv-python-headless numpy
```

CRITICAL: pdftoppm/poppler CANNOT render this PDF (its JBIG2 streams
throw "Unknown segment type"). All page rendering goes through PyMuPDF
(`scripts/render.py`). Do not waste time on poppler rendering paths.

If PaddleOCR installs cleanly in this environment, use it as the primary
OCR engine with tesseract as the diff partner in `ocr_dual.py` — it is
substantially better for Chinese and was unavailable in the environment
where these scripts were written. If it doesn't install in a few minutes,
move on with tesseract alone; do not burn an hour on it.

## Pipeline per chapter

1. `render.py FIRST LAST --dpi 300` (PDF page numbers).
2. `ocr_crop.py FIRST LAST` — margin-cropped psm 6. The book prints a
   vertical running title down the OUTER margin (recto right, verso left);
   the crop in this script removes it. Without the crop, margin glyphs
   corrupt line ends. Expected error rate after cropping: 4-5% of
   characters.
3. `find_figures.py FIRST LAST` — ink-density figure detection.
   **TRAP: this overwrites data/figs/manifest.json each run.** Fix it to
   merge before your first use, or run it once over the whole chapter
   range. It already filters recurring page furniture (the recto margin
   decoration).
4. Read the OCR text and translate (see Register). Verify BEFORE writing:
   every proper name, every number, every low-confidence span gets a
   magnified crop of the scan (PIL crop + resize, then tesseract on the
   crop, then look at it). OCR errors here are contextually plausible
   valid words, not gibberish — the dangerous ones read fluently.
5. `check_invariants.py` on a working bilingual draft (source blockquote
   above English paragraph — this format is for QC ONLY, never for the
   deliverable). It catches dropped/altered numbers. Extend its NOISE
   list as new measure-word false positives appear.
6. Write notes into `notes.json` (see Notes).
7. Build and QA (see Build).

Delete each chapter's rendered PNGs after its QA passes if disk gets
tight; keep the OCR text and figure crops forever.

## Register — the style contract (from Winston, non-negotiable)

- Clean flowing English prose. NO bilingual interleave, NO page numbers
  in the text, NO inline [?]/[!] flags. All apparatus lives in the notes.
- This is popular history in a novelistic key. Keep that voice — invented
  dialogue, interior thought, melodrama and all. Do not tighten it into
  academic English, do not camp it up further.
- Translate idioms for effect, keep the vivid ones literal when they land
  ("what medicine he was selling from that gourd"), and note the ones
  whose flavor can't survive.
- Merge sentences where English wants them merged. Chinese information
  order is not sacred. Fluency failures read as "stilted" — that word is
  Winston's, from rejecting the first draft. Read reference/ch1_reading.md
  until you can hear its register.
- Names: pinyin except conventional forms (Chiang Kai-shek, Sun Yat-sen).
  斧头帮 is "Hatchet Gang," never "Axe Gang" — decided, see glossary.
- NEVER invent bridging text. If the OCR cuts off mid-sentence, crop the
  scan and read the actual continuation. A fluent invented sentence is the
  worst error this project can produce; it happened once in ch1 and was
  caught only by luck.

## Notes — what earns one

Three kinds, per Winston's spec:
1. References a Western reader won't catch: who a person is, what an
   institution/object/place is (the flag, the Mauser, nü'erhong wine,
   Purple Mountain), with real historical content — check claims against
   scholarship via web search where the book intersects documented
   history, and SAY in the note when the book's claim is corroborated,
   uncorroborated, or contradicted.
2. Chinese wordplay and prose texture lost in translation: idioms with
   their literal images, classical allusions (Jing Ke, Maicheng, Ouyang
   Xiu), register shifts, names whose meaning matters (九爷/九光).
3. Translation uncertainty: damaged-scan readings with the alternates
   considered, provisional romanizations, genuine ambiguities. State what
   the scan shows and why you chose your reading.

Notes are keyed by exact anchor phrase from the English text
(notes.json format: [{"anchor": "...", "note": "..."}]). Anchors must be
verbatim substrings of the prose. HTML allowed in note bodies (<i>).
Density calibration: ch1 ran ~3 notes per printed page. Don't pad; don't
starve. NEVER source Grok/Grokipedia or other LLM-generated reference
content when checking facts (Winston's standing rule); prefer Wikipedia,
Baidu Baike, academic sources, and note when sources conflict.

Do not re-note what ch1 already noted (the flag, the Mauser, 九爷) unless
the new context adds something. Recurring-character notes go at first
appearance per BOOK, not per chapter.

## Build

`scripts/build_reading_epub.py` is currently CHAPTER-1-SHAPED: single
spine document, hardcoded FIGURES dict, qa_epub checks "ch01.xhtml" by
name. **Your first engineering task is generalizing it:**
- One XHTML per chapter (ch01...ch15 + prologue), all in one spine, one
  cumulative EPUB: `out/wang-yaqiao.epub`.
- notes.json stays global; note numbering restarts per chapter or runs
  continuously — pick one, implement it in both builder and qa_epub, and
  keep qa_epub's checks (every ref has a body, every body a backlink,
  ordering sane) passing across ALL chapter docs.
- FIGURES dict → per-chapter figure specs (file, anchor phrase, caption).
  Figure captions in this book are often VERTICAL text in the margin
  beside the image: crop that zone and OCR with -l chi_sim (psm 6 catches
  short vertical runs) or chi_sim_vert. If no caption is legible, caption
  it neutrally as an uncaptioned inset — never invent an identification.
- Keep the existing back matter (translator's note + glossary rendered
  from glossary.json) and update the translator's note to describe the
  full book.
- Preserve mimetype-first-and-stored zip ordering; qa_epub checks it.

Run `qa_epub.py` after EVERY chapter build. A QA failure stops the line
until fixed. Commit to git after each chapter passes (init a repo at
start; commit message = chapter number + one line).

## Glossary discipline

`glossary.json` is the single source of truth for every rendering.
Before romanizing ANY name, check it. New names get added with status:
- "attested" — the form used in English scholarship (cite-checkable)
- "provisional" — your romanization, not found in outside sources
- "decided" — a project style decision (Hatchet Gang, Gate of China)
One rendering per referent for the whole book. If you discover a better
attested form mid-book, change the glossary AND grep every already-built
chapter for the old form. Consistency across 15 chapters is the point of
the file.

## Corrections workflow (this is why the whole book runs first)

Winston reads the finished EPUB and files corrections in
`CORRECTIONS.md` (template provided). Corrections come in two kinds:
- GLOBAL: a rendering, register rule, or note policy ("render X as Y
  everywhere", "stop noting every idiom", "this person is actually Z").
  Apply via glossary/style change + grep-driven edit across ALL chapter
  markdown + rebuild + full QA. These must cascade completely — a global
  correction applied to only some chapters is worse than not applying it.
- LOCAL: a fix at one spot. Apply, rebuild, QA.
After applying a corrections batch: rebuild the EPUB, run qa_epub, list
every file touched in the reply, and append a dated entry to
CHANGELOG.md summarizing what cascaded where.

## Known traps (all hit in ch1 — do not rediscover them)

- Poppler/JBIG2 as above. PyMuPDF only.
- find_figures manifest overwrite as above.
- OCR name mangles are systematic: 王亚樵→王亚榴/王亚权/王亚机/王亚檐,
  柏文蔚→柏文艺/柏文茸/柏文蔚 variants, 杜月笙→杜月笔, 斧头帮→佐头帮/
  径头帮/攻头帮/莽头帮/和头帮. Build a per-chapter mangle map as you go;
  it accelerates every subsequent page.
- 兼 (concurrently) OCRs as 莱. 咬 as 蛟. Numerals in titles (第37军)
  are load-bearing — always crop-verify unit numbers.
- The escaping order in the builder: insert note anchors BEFORE any
  markup substitutions, or the substitutions eat the anchors.
- str_replace-style edits on the builder failed once because the source
  file held \\u escapes where the rendered string had the character. When
  editing scripts, grep for the actual bytes first.
- Winston's preferences: no em dashes in prose you write TO him (the
  book translation itself may use them as English punctuation demands);
  small focused scripts over monoliths; targeted patches over rewrites.

## Definition of done

- `out/wang-yaqiao.epub`: prologue + chapters 1-15, all figures with
  captions or honest non-captions, notes throughout at ch1 density,
  glossary and translator's note updated, qa_epub PASS across the whole
  spine.
- `out/chNN_reading.md` per chapter (the correction surface).
- `notes.json`, `glossary.json` current.
- `PROGRESS.md`: per chapter — page range, figure count, note count,
  names added to glossary with status, anything flagged for Winston's
  read-through (uncertain readings, contradictions with history, choices
  you weren't sure about). This file is what makes his review fast; write
  it as you go, not at the end.
