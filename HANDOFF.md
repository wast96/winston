# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B02

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). NOT a translation: source.pdf (repo root, 409 pages) has a clean
born-digital text layer, so there is no OCR and nothing to translate. The work
is annotation and faithful resetting. Batch 1 (ch01) is done and set the whole
machinery; you are extending it, not inventing it.

Read, in order: CLAUDE.md, then HANDOFF.md (full source characterization and
the do-not-revert tooling list), then book.json, then STYLE.local.md (the whole
style contract; it now carries the Batch 1 voice-gate rulings — follow them).
BEFORE writing any editorial notes, read out/ch01_reading.md's notes and a few
of ch01's editorial notes in notes.json: they ARE the note voice to match.

Do Batch 2 = the FRONT MATTER, ch00a "Foreword, by Arnold R. Isaacs" (PDF 8-11,
printed vii-x) and ch00b "Introduction, by Leon Trotsky" (PDF 12-23, printed
xi-xxii), end to end per the pipeline ch01 established:

1. Extract each unit VERBATIM with `python3 scripts/extract_isaacs.py ch00a`
   and `... ch00b` (it is now offset-aware: front matter offset is 1, read from
   book.json, so folios come out as their roman equivalents 7..22 = vii..xxii).
   REVIEW the printed de-hyphenation report and the char-stream fidelity check
   (the ch01 method: reduce both the extracted body and the PDF's own body spans
   to a whitespace/hyphen/quote-stripped stream and confirm they are IDENTICAL).
   The Foreword is Arnold Isaacs's 2009 prose; the Introduction is Trotsky's
   1938 text. Keep each verbatim; never invent bridging text (rule 4).
2. CHARACTERIZE the front matter's own apparatus first: does the Foreword or
   Trotsky's Introduction carry its own footnotes/endnotes? (ch01's were 5.5pt
   superscript digits + 8pt asterisk foot-notes; check whether the front matter
   uses the same, and whether Trotsky's intro has back-of-book notes.) Convert
   any author notes to the ARABIC stream exactly as in ch01 (scripts/
   dump_endnotes.py + build pattern); if there are none, say so explicitly.
3. Editorial notes (ROMAN stream, "ed": true) per CLAUDE.md's generous density
   model AND the STYLE.local.md rulings from Batch 1 (no "Pinyin:" trailers;
   verdict tag ONLY where an author claim is actually weighed; one subject one
   note; don't gloss ordinary English; map old romanizations). Trotsky's
   Introduction is dense Comintern/Bolshevik polemic — expect many first-
   appearance notes (Stalin, Bukharin, the Comintern, "permanent revolution,"
   the 1926-27 events he foreshadows). Fact-check against real scholarship only
   (rule 5), verdict where checkable. NOTE: for the front matter, cite the ROMAN
   folio (vii, xi, ...) in note prose, not arabic.
4. Glossary: add new people/terms (key=hanzi where one exists; en=the form the
   text uses; pinyin; note). Flag any genuine principal with "principal": true.
5. Build (`scripts/build_reading_epub.py`), qa_epub AND epubcheck BOTH clean
   (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; refetch per setup.sh if the
   container is fresh), check_apparatus clean. Run the Step 0c blind-critique
   loop (annotation variant is automatic) on ch00b at least; evolve
   STYLE.local.md with anything new.
6. Deliver the built EPUB in chat as an attached file (stamp a chat copy with
   `python3 scripts/stamp_deliverable.py B02`) and PASTE the next kickoff
   verbatim in the same reply. Update PROGRESS.md and HANDOFF.md; commit.

Do not pause for approval mid-batch. Cite printed folios (roman for the front
matter). One branch only: claude/tragedy-of-the-chinese-revolution — expect a
stray per-task branch at the top and reconcile onto the working branch.
```

## What is DONE (do not redo)

- Survey session: book.json filled, builder adapted for an annotated edition,
  skeleton EPUB built and validated, SURVEY.md written, source.pdf committed.
- **Batch 1 (ch01 "Seeds of Revolt"): COMPLETE.** out/ch01_reading.md (verbatim,
  fidelity-verified byte-for-byte), data/pagemap/ch01.json, 85 notes (32 author
  arabic + 53 editorial roman), glossary bootstrapped with the ch01 cast +
  terms + places, Sun Yat-sen flagged principal. Builder features (block-quote,
  two-stream notes) implemented, tested, and gated green (qa_epub + epubcheck +
  check_apparatus). Step 0c blind-critique loop ran 3 rounds; STYLE.local.md
  carries the distilled rulings. See PROGRESS.md for the full record.
- 0 of 22 units remain besides the 21 not-yet-prepared (ch00a, ch00b, ch02-20).

## Tooling in place (DO NOT REVERT)

- **scripts/build_reading_epub.py**: `edition_kind: "annotated"` chrome (from the
  survey), PLUS Batch 1: (a) the `{q} ` block-quote marker — consecutive `{q}`
  lines group into one `<blockquote class="quote">`, each its own `<p>`; (b)
  TWO-STREAM per-chapter note numbering — author notes arabic (ids n-<unit>-N /
  ref-n-<unit>-N), editorial notes ("ed": true) lowercase roman (ids
  en-<unit>-r / ref-en-<unit>-r), both restart each chapter; `to_roman()` helper;
  render_notes_page groups author-then-editorial per chapter.
- **scripts/qa_epub.py**: note check REWRITTEN for the two per-chapter streams
  (parses ref-n-/ref-en- ids, checks refs=bodies=backlinks and per-(unit,stream)
  1..k sequence, roman decoded).
- **scripts/extract_isaacs.py** (NEW): faithful-reset extractor. De-hyphenation
  by Isaacs's own dominant usage + system word lists; drop-cap fold; furniture
  strip; superscript-ref removal with space repair; asterisk-footnote capture;
  offset read per-unit from book.json (23 body, 1 front matter); writes reading
  md + pagemap; prints a review report. USE IT for every chapter.
- **scripts/dump_endnotes.py**, **build_ch01_notes.py**, **build_ch01_editorial.py**
  (NEW): endnote-text dumper and the ch01 author/editorial note generators
  (anchors resolved against reading.md, checked unique + non-colliding). The
  editorial one is a good template to copy per chapter.
- **review/voice_gate_critic_prompt_annotation.md** (NEW) + voice_gate_critique.py
  is edition-aware (auto-selects the annotation prompt, labels notes
  author/editorial). tests/run_tests.py has `annotation_test` covering {q} and
  the two streams. check_structure/verify_unit/check_reconcile/voice_gate marker
  regexes now include `q`.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/; Pillow + wamerican/wbritish word
  lists installed by setup.sh + apt.

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles (or conventional English) forms STAY in the
  body; pinyin + hanzi go in the glossary and the first-appearance editorial
  note. One form per referent; check authority.json (孙中山→Sun Yat-sen,
  国民党→Kuomintang confirmed shelf-wide).
- Note architecture: author notes arabic, editorial roman, per-chapter restart,
  NO "Ed." prefix. All of Isaacs's own notes (numbered endnotes AND asterisked
  footnotes) go in the arabic stream, numbered by position — so the arabic
  numbers are the edition's sequence, not his printed endnote numbers.
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American
  English in editorial prose; dates "Month D, YYYY".
- Editorial-note voice (the "voice" this book protects; set at the ch01 gate):
  concise, factual, modern American English; who/what/when + why-it-matters-here;
  verdict tag ONLY where an author claim is weighed; no padding, no "Pinyin:"
  trailer, one subject one note. Full rulings in STYLE.local.md.

## Where the book stands

- ch01 establishes the machinery and the note voice. The cast is front-loaded:
  most 19th/early-20th-c. figures got their note in ch01 and are NOT re-noted
  (grep notes.json + earlier reading files before adding a note; keep a "NOT
  re-noted" list per batch). The 1925-27 principals (Chiang, Borodin, Chen
  Tu-hsiu, Stalin, Trotsky, Mao, Wang Ching-wei) mostly arrive in ch02+ /
  Trotsky's Introduction.

## What is NEXT (grouping calibrated on Batch 1)

- B02 = front matter (ch00a Foreword + ch00b Trotsky Introduction). Front matter
  is roman-foliated (offset 1) and Trotsky's intro is annotation-heavy; sized as
  ~one batch.
- Then the body, GROUPED to fill (not exceed) ~65% of context. ch01 (front-
  loaded, 53 first-appearance editorial notes, 3 critique rounds) was about one
  full working-context's worth; later chapters inherit the cast and run lighter.
  Provisional: B03 = ch02-03 (theory-heavy, keep to 2); B04 = ch04-05; B05 =
  ch06-07-08; B06 = ch09-10-11; B07 = ch12-13-14; B08 = ch15-16-17; B09 =
  ch18-19-20. Adjust as later chapters prove lighter.
- The FINAL batch stays light on chapters: it also builds the LINKED index from
  all the per-chapter pagemaps (see book.json _index_decision), does the
  whole-book reconciliation sweep (check 12), and writes COMPLETION.md.

## Commissioner decisions (settled; no longer open)

- LINKED index (not omitted): built in the FINAL batch from per-chapter
  pagemaps; each folio reference links to its pagebreak anchor.
- Two note layers told apart by NUMERAL SYSTEM: author arabic, editorial roman,
  per-chapter; no "Ed." prefix.
- 2009 Foreword KEPT as front matter (ch00a). Treated as a derivative edition
  for private study (see book.json rights).

## Open items / traps for the next session

- Front matter offset is 1, not 23 (extractor handles it from book.json). Cite
  ROMAN folios (vii..xxii) in front-matter note prose.
- CHARACTERIZE the front matter's own note apparatus before converting: it may
  differ from ch01's (Trotsky's intro may carry footnotes and/or its own
  numbered notes).
- The pagemap "printed" field is arabic; for the front matter it holds the
  arabic equivalents (7..22). If you want roman page-list labels in the built
  nav, that is a builder tweak to consider at the linked-index (final) batch;
  ch01's arabic pagemap is unaffected.
- Known non-issue: `tests/run_tests.py` "hook stands down on template stub"
  FAILS because the test restores the real HANDOFF (with a live kickoff) and
  then asserts the hook does NOT fire — with a real kickoff it correctly does.
  The hook works; the test's premise lapsed when the kickoff was filled in. Do
  not "fix" the hook.

## Environment / traps state

- pymupdf, Pillow, java + epubcheck 5.1.0, wamerican/wbritish word lists ready.
  No tesseract/OCR needed. Build is text-only + one small generated cover, well
  under the 30 MB cap (0.1 MB).
- Stray-branch check every batch per CLAUDE.md rule 2 (working branch
  claude/tragedy-of-the-chinese-revolution).
