# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B01

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). It is NOT a translation: the source is already English and source.pdf
(committed at the repo root, 409 pages) has a clean born-digital text layer, so
there is no OCR and nothing to translate. The work is annotation and faithful
resetting.

Read, in order: CLAUDE.md, then HANDOFF.md (it carries the full source
characterization and the do-not-revert tooling list), then book.json, then
STYLE.local.md (the whole style contract for this book; there is no composed
STYLE.md here).

Do Batch 1 = ch01 "Seeds of Revolt" (PDF pages 24-41, printed folios 1-18) end
to end:

1. Extract Isaacs's text VERBATIM into out/ch01_reading.md, one paragraph per
   line, with "## 1. Seeds of Revolt" as the h1. Mechanical fixes only: rejoin
   hyphenated line-breaks, fold the drop-cap initial into its word, strip
   running heads and folios, and remove the in-text superscript reference
   digits from the prose (they become footnote anchors). Preserve paragraph
   breaks and Isaacs's own British 1938 spelling. Mark his block quotations.
   Never paraphrase or invent: this is his prose (rule 4 binds; verify the tail
   against source.pdf before shipping).
2. Add a block-quote marker to the builder (proposed prefix "{q} ", an indented
   block) since Isaacs quotes documents at length; qa_epub and epubcheck must
   stay clean after.
3. Convert Isaacs's own chapter-1 endnotes (printed 340+, numbered per chapter)
   into anchored popup footnotes in notes.json: detect the 5.5pt superscript
   digits, anchor each to the phrase it follows, note body = his endnote text
   verbatim. Leave these UNMARKED (author's notes).
4. Add the editorial footnote layer per CLAUDE.md's generous density model, each
   note opening with "<i>Ed.</i>&#160;": who/what/when for every 1920s name,
   place, institution, office, and party or Comintern term a non-specialist
   would miss, with the fact-check verdict where checkable (real scholarship
   only, never AI sources, rule 5).
5. Bootstrap glossary.json (key = hanzi; en = Isaacs's Wade-Giles form; pinyin =
   modern pinyin; note = identification); flag principals with "principal": true
   for the Principal Characters page.
6. Build, run qa_epub AND epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar,
   refetch per setup.sh if the container is fresh), both clean. Then run the
   Step 0c gate: the blind-critique loop adapted for ANNOTATION (density, voice
   of the notes, formatting; there is no translation register to grade), evolve
   STYLE.local.md, and PRESENT ch01 to the commissioner for the format and
   note-density gate. STOP there.

Batch 1 is also the CALIBRATION for batch sizing: in your wrap-up, report
roughly how much of the context window this one fully-annotated chapter
consumed (extraction + endnote conversion + editorial notes + research), so
the following batches can be grouped to fill (not exceed) ~65%. Chapters 2+
are lighter because the cast is front-loaded (most names get their note at
first appearance here and are not re-noted), so later batches will group
2-4 chapters. Propose the concrete grouping in your next kickoff.

Cite printed folios (arabic). Deliver the EPUB in chat as an attached file and
paste the next kickoff verbatim in the same reply.
```

## What is DONE (do not redo)

- Survey session: book.json filled (Step 0a metadata + full verified structure),
  builder adapted for an annotated (non-translation) edition, skeleton EPUB
  built and validated (qa_epub PASS, epubcheck 5.1.0 clean), SURVEY.md written,
  source.pdf committed. No chapters prepared yet (0 of 22 units).

## Tooling in place (do not revert)

- **scripts/build_reading_epub.py**: added `edition_kind` support. When
  book.json `"edition_kind": "annotated"`, the builder drops translation chrome:
  title page reads "Annotated edition" and omits the empty source-title line;
  the notes page says editorial notes are marked "Ed." and the rest are the
  author's own; coverage/skeleton wording says "prepared", not "translated";
  the back-matter heading comes from book.json `note_heading` ("A Note on This
  Edition"); the generated cover tagline is "Annotated Edition". All gated on
  `_annotated()`, so the translation path is unchanged when the key is absent.
- epubcheck 5.1.0 fetched to /tmp/epubcheck-5.1.0/ (java present at /usr/bin/java).
- Pillow installed (typographic cover generates; Liberation fonts present).

## Source characterization (verified against the scan)

- Born-digital PDF (QuarkXPress/Quartz), clean text layer, ZERO page images on
  text pages. No OCR needed. Bookmarks present and accurate (25 entries).
- Fonts: body ACaslon-Regular ~10pt; chapter number 100pt, chapter title 21pt,
  drop-cap 44pt; in-text reference marks are 5.5pt superscript ACaslon digits,
  numbered PER CHAPTER (restart at 1 each chapter).
- Offset: front matter runs roman i-xxii; the body restarts at arabic 1. Body
  offset is CONSTANT 23: printed = (PDF page, 1-indexed) - 23, confirmed at all
  20 chapter openers via bottom folios. Front-matter offset is 1 (roman).
- No titled sections inside chapters; each chapter is one continuous unit.
  Chapters DO carry internal white-space breaks (render as "***" where clear).
- Body = chapters 1-20, PDF 24-362, printed 1-339. Endnotes printed 340-373;
  index printed 374 to end (recommended OMITTED, see book.json / SURVEY.md).
- TOC discrepancies flagged in book.json toc_flags_open (ch08/09/10/16 printed
  TOC titles differ from the chapter openers; the opener forms are used).

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles forms STAY in the body; pinyin + hanzi go in
  the glossary and the first-appearance editorial note. One form per referent;
  check authority.json before deciding.
- Note architecture: author's notes (his endnotes) unmarked; editorial notes
  prefixed "Ed."; single continuous builder numbering.
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American
  English in editorial prose; dates "Month D, YYYY".

## Voice sheets

- Not applicable (no dialogue to voice; this is a documented history). The
  "voice" to protect is the register of the EDITORIAL notes: concise, factual,
  non-partisan; set at the Batch 1 gate.

## Where the book stands

- Nothing prepared yet. Batch 1 sets the annotation style, the endnote-conversion
  mechanism, and the block-quote rendering, then holds the format/density gate.

## What is NEXT

- Batch 1 = ch01 "Seeds of Revolt" (PDF 24-41, printed 1-18). Ends at the Step
  0c gate, and also calibrates batch size. Proposed order after, GROUPED to fill
  ~65% of context (target ~8-10 batches total, not one per chapter): B02 = ch00a
  + ch00b (Foreword + Trotsky's Introduction); then ch02-ch20 in groups of about
  2-4 (front-loaded cast makes later chapters lighter), the exact grouping set
  from Batch 1's measured cost. A provisional grouping: ch02-03, ch04-05,
  ch06-07-08, ch09-10-11, ch12-13-14, ch15-16-17, ch18-19-20.

## Open items for the read-through

- Confirm at the gate: index omitted; single note stream with "Ed." marks; the
  2009 Foreword kept as front matter (its copyright is separate from the 1938
  text). Copyright: the 1938 text is very likely still protected; treated as a
  derivative for private study.

## Environment / traps state

- pymupdf, Pillow available; java + epubcheck 5.1.0 ready. No tesseract/OCR
  needed. Build target under 30 MB is trivial (text-only + one small cover).
- Batches capped at ~65% of the context window (commissioner directive): one
  chapter per batch keeps inside it.
- Stray-branch check every batch per CLAUDE.md rule 2 (working branch
  claude/tragedy-of-the-chinese-revolution).
