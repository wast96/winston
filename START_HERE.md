# START HERE — translate a Chinese EPUB into an annotated English EPUB

This branch (`translation-template-epub-master`) is a ready-to-clone starter kit
for translating one **digital source EPUB** (real text, no scanning) into an
annotated English EPUB, using the same batch process and hyperlinked-TOC build as
the scanned-book template, but with the OCR/scan machinery replaced by EPUB
ingest. No book is loaded in.

There are two ways to use it. Pick one.

## Option A — a new folder inside a repo (simplest)

```
git checkout -b claude/my-book translation-template-epub-master
# or, to keep it in an existing repo, copy the template into a new folder:
mkdir my-book && git archive translation-template-epub-master | tar -x -C my-book
cp /path/to/source.epub my-book/source.epub
```

## Option B — a fresh branch that IS the project

```
git checkout -b claude/my-book translation-template-epub-master
cp /path/to/source.epub source.epub
```

## One-time setup

1. **Drop the source EPUB in as `source.epub`.**
2. **Set two names:** the working branch (rule 2 in `CLAUDE.md`) and the output
   EPUB filename (rule 1 / Build). Search `CLAUDE.md` for `[SET PER PROJECT]`.
3. That is it for you. You do NOT hand-enter the structure or plan the batches:
   the first session ingests the EPUB, drafts `book.json`, proposes the batches,
   and shows you a navigable skeleton EPUB to approve.

## The flow: ingest + survey first, then batches

1. **Survey** (message 1): the session runs `ingest_epub.py` on your EPUB,
   authors `book.json` from the draft, and hands you back the counts (parts,
   chapters, sections, subsections), each unit's title and size in source
   characters, a proposed batch breakdown, and a **skeleton EPUB with a fully
   hyperlinked table of contents** attached in chat. It then stops.
2. **You approve** the batch plan (or adjust it).
3. **Batches** (message 2): the session runs Batch 1 end to end, and from then on
   each batch's `HANDOFF.md` hands you the next batch's kickoff message.

## Message 1 — ingest and survey (paste into a NEW session first)

Fill the **`<...>`** blanks and send. This produces the structure report and the
hyperlinked-TOC EPUB for your approval; it does not translate anything yet.

```
We're translating a Chinese-language EPUB into an annotated English EPUB, using the translation-template-epub-master starter kit. Set it up and run the ingest + structural survey only — no translation yet.

Setup:
1. Create the working branch <claude/my-book> from translation-template-epub-master, and copy the template's files into the project (CLAUDE.md, book.json, scripts/, etc.).
2. Put my source EPUB at source.epub. <say how it reaches the session, or that it's already in the repo.>
3. Read CLAUDE.md in full — the working rules at the top are non-negotiable. Build the deliverable as <out/my-book.epub>.

This book: <BOOK TITLE (author, year)>.

Now do STEP 0, ingest + survey, and NOTHING past it:
1. Run scripts/ingest_epub.py source.epub. It unpacks the EPUB, extracts each spine document's text into data/src/, pulls images into data/figs/, counts source characters, and writes out/INGEST.md and book.draft.json.
2. Author book.json from book.draft.json: real chapter/section titles plus English titles, optional parts and subsections, and — importantly — MERGE or SPLIT units where the EPUB's file boundaries do not match the book's logical chapters. Keep each unit's src and chars.
3. Run scripts/survey.py, then build the skeleton EPUB with scripts/build_reading_epub.py, and run scripts/qa_epub.py until green.
4. Report back with: the counts (parts / chapters / sections / subsections), every unit's title and size in source characters, and a proposed batch breakdown — and attach the skeleton EPUB (the hyperlinked table of contents) to the chat so I can navigate it.
5. STOP and wait for me to approve the batch plan. Do not start translating. Once I approve, write the Batch 1 kickoff message into HANDOFF.md and paste it to me.

Cite chapters and sections, never page numbers (an EPUB has none). Commit the survey (book.json + out/SURVEY.md).
```

## Message 2 — a translation batch (after you approve the plan)

The survey session writes this into `HANDOFF.md`, already filled in; it is shown
here so you know what it looks like. Normally you just copy it from `HANDOFF.md`.

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating <BOOK TITLE> into an annotated English EPUB per CLAUDE.md. Work only on <claude/my-book>; build <out/my-book.epub>.

Do Batch <B01> = <scope, e.g. Chapter 1, sections ch01s01-ch01s03>, end to end:
1. Read the batch's source text from data/src/ (already extracted at ingest). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file — copy, do not re-type. Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible. Preserve the source's own notes/markup (render its notes as text, distinct from your translator's notes).
2. Author one aligned out/<id>_bilingual.md, generate the reading text and parity source with scripts/split_bilingual.py, then run scripts/check_numbers.py and scripts/check_structure.py --pairs.
3. Blind double-translation and back-translation on the argumentative/literary passages; fact-check names/dates against real scholarship (never Grok/Grokipedia).
4. Add footnotes to notes.json (keyed by unit id, three kinds, ~3 per chapter-equivalent, XHTML bodies with numeric character references) and extend glossary.json with attestation. Place any images from this unit via figures.json.
5. Rebuild the EPUB (the TOC stays fully linked, nested to subsection level), run scripts/qa_epub.py until green.
6. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch.

Cite chapters and sections, never pages. Don't pause for my approval; run the whole batch and report back when it's built and QA-green, and paste the next-batch kickoff message at the end of your reply.
```

On the last batch, ask for any back matter (a translated colophon if the source
has one), a whole-book QA pass, and a completion report instead of a handoff.

## What each file is

- `CLAUDE.md` — the operating manual. Read by the assistant every session.
- `book.json` — the whole book's structure; drives the build. Authored from the
  ingest draft.
- `notes.json` / `glossary.json` / `figures.json` — apparatus, fill as you go.
- `back_matter.json` — optional colophon; inert until enabled.
- `scripts/` — the pipeline (ingest, survey, split-bilingual, the two checks, the
  EPUB builder, the EPUB QA). Each has a docstring.
- `out/` — deliverables: `INGEST.md`, `SURVEY.md`, `<id>_reading.md` per unit,
  and the built EPUB.
- `data/` — working files (unpacked source, extracted text, images);
  regenerable, git-ignored.
- `PROGRESS.md` / `HANDOFF.md` / `CORRECTIONS.md` / `CHANGELOG.md` — the log, the
  baton, the correction inbox, the change record.
