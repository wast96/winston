# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat alongside the attached EPUB.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B05

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). NOT a translation: source.pdf (repo root) has a clean born-digital
text layer, so there is no OCR and nothing to translate. The work is annotation
and faithful resetting. Batches 1-4 (front matter + ch01-05) are done and set
the whole machinery; you are extending it, not inventing it.

Read, in order: CLAUDE.md, then HANDOFF.md (full source characterization and the
do-not-revert tooling list), then book.json, then STYLE.local.md (the whole
style contract; it carries the Batch 1-4 voice-gate rulings - follow them).
BEFORE writing any editorial notes, read a sample of ch04/ch05's editorial notes
in notes.json (they ARE the note voice to match) and the final two pages of
ch05's English (out/ch05_reading.md) - that prose IS the register the notes sit
against.

Do Batch 5 = ch06 "From Canton to the Yangtze" (PDF 117-132, printed 94-109),
ch07 "The Shanghai Insurrection" (PDF 133-142, printed 110-119), and ch08 "The
Prodigal's Return" (PDF 143-154, printed 120-131), end to end per the pipeline
ch01-05 established:

1. FIRST run ./setup.sh, THEN `sudo apt-get install -y -qq wamerican wbritish`
   (setup.sh does NOT install the English wordlists extract_isaacs.py needs for
   de-hyphenation - it installs Chinese OCR packs the extractor never uses).
   Confirm /usr/share/dict/american-english exists. Expect a possible stray
   per-task branch and a stale working tree at the top: `git fetch origin
   claude/tragedy-of-the-chinese-revolution` and hard-reset onto it if HEAD is
   not at the real tip (last session's tree was parked on template-master).
2. Extract each unit VERBATIM: `python3 scripts/extract_isaacs.py ch06` etc.
   (body offset 23; folios come out arabic 94.., 110.., 120..). The extractor
   now (a) captures set-off block quotations ({q} prefix) and (b) merges the
   spurious mid-page paragraph splits a superscript-at-a-line-end used to cause
   (gap-ratio rule; do not revert). REVIEW the de-hyphenation report AND eyeball
   for real compound hyphens broken at a line end (war-weary class), which
   check_fidelity cannot catch. Then `python3 scripts/check_fidelity.py ch06
   ch07 ch08` and confirm BOTH streams IDENTICAL. Also scan each reading file
   for a paragraph ending mid-sentence OR with a full-width line before a body
   (not {q}) paragraph - a residual spurious split - and for born-digital
   glitches (stray hyphen/tilde; render to plain sense and LOG in PROGRESS).
3. AUTHOR notes (arabic): `dump_anchors.py`, `anchor_offsets.py`, then
   `dump_endnotes.py` (ch06 endnotes begin PDF 370 "6. From Canton to Yangtze";
   verify the ch07/ch08 headings and ranges). Assemble on the
   build_ch0405_notes.py pattern, which numbers author notes POSITIONALLY (by
   the in-text mark, not the printed back-matter label) - ch05's 1938 endnotes
   were misnumbered "18, 18, 20", and ch06-08 may carry similar quirks; check.
   Transcribe asterisk foot footnotes by hand with <i>, dropping any stray
   trailing glyph.
4. EDITORIAL notes (roman, "ed": true) on the build_ch0405_editorial.py pattern,
   per CLAUDE.md's generous density model AND the STYLE.local rulings (marker ON
   the term; verdict tag ONLY where a claim is weighed; one subject one note; a
   note is never vaguer than its text AND never re-underlines the body's own
   point or irony; do not offer a competing translation of a term the body
   already renders; consistent pinyin gloss; no re-noting a subject an earlier-
   reading unit already covers). GREP notes.json and the earlier reading files
   first; keep a "NOT re-noted" list in PROGRESS. New first-appearance subjects
   to expect: the Northern Expedition's campaigns and its generals (Tang
   Sheng-chih, Ho Ying-chin, Pai Chung-hsi, Li Tsung-jen), the Shanghai
   uprisings of 1926-27 and the workers' pickets, Chou En-lai as insurrection
   organizer, Sun Chuan-fang, the Wuhan/Nanking split beginning, and more
   Comintern figures. Fact-check against real scholarship, verdict where
   checkable. Cite ARABIC printed folios in body notes.
5. Glossary: add new people/terms DIRECTLY INTO THEIR SECTION with Write/Edit
   (NOT apparatus_merge - it flattens the sectioned glossary; use a small script
   like add_ch0405_glossary.py). Consult authority.json for shelf agreement;
   principals are Sun 1, Chiang 2, Chen Tu-hsiu 3, Borodin 4 - consider
   promoting Wang Ching-wei (now central) to principal 5 if the narrative keeps
   turning on him, and watch for Chou En-lai.
6. Build (build_reading_epub.py); qa_epub AND epubcheck BOTH clean (jar at
   /tmp/epubcheck-5.1.0/epubcheck.jar; refetch per setup.sh if the container is
   fresh), check_apparatus clean, check_fidelity green on ALL units. Run the
   Step 0c blind-critique loop on at least one unit; evolve STYLE.local.md.
7. Deliver the built EPUB in chat as an attached file (stamp a chat copy with
   `python3 scripts/stamp_deliverable.py B05`) and PASTE the next kickoff
   verbatim in the same reply. Update PROGRESS.md and HANDOFF.md; commit and push.

Do not pause for approval mid-batch. Cite printed folios (arabic for the body).
One branch only: claude/tragedy-of-the-chinese-revolution - reconcile any stray
branch onto it.
```

## What is DONE (do not redo)

- Survey session: book.json filled, builder adapted for an annotated edition,
  skeleton EPUB, SURVEY.md, source.pdf committed.
- **B01 (ch01 "Seeds of Revolt"): COMPLETE.** 85 notes (32 author + 53
  editorial). Step 0c ran 3 rounds.
- **B02 (front matter: ch00a Foreword + ch00b Trotsky Introduction): COMPLETE.**
  47 notes. check_fidelity.py introduced.
- **B03 (ch02 + ch03): COMPLETE.** ch02 48 notes, ch03 90 notes. Block-quote
  extraction, the author-note anchor tooling, the chapter-numeral fidelity fix.
- **B04 (ch04 "Canton: To Whom the Power?" + ch05 "Canton: The Coup of March 20,
  1926"): COMPLETE.** ch04 47 notes (32 author + 16 editorial), ch05 69 notes
  (63 author + 6 editorial). 19 glossary rows. Fixed a latent extractor bug
  (spurious mid-page paragraph splits) that had shipped in ch01-03; re-extracted
  and corrected those (words byte-identical, 4 paragraph merges only). Step 0c
  ran 2 rounds on ch04. Full record in PROGRESS.md.
- Cumulative build: **7 of 22 chapters, 387 notes, 108 pagebreaks, 0.2 MB.**
- 12 chapters remain (ch06-ch20).

## Tooling in place (DO NOT REVERT)

- **scripts/extract_isaacs.py**: faithful-reset extractor; per-unit offset from
  book.json (23 body, 1 front matter); de-hyphenation; drop-cap fold; furniture
  strip; superscript-ref removal; asterisk-footnote capture; block-quote
  capture ({q}); pagemap. **B04 addition: gap-ratio merge of spurious mid-page
  paragraph splits** - a superscript mark at a line end makes PyMuPDF split one
  paragraph into two blocks; the extractor now merges a flush-left same-kind
  block into the previous paragraph when it starts a page OR follows at the
  normal line rhythm (vertical gap <= 1.35x the body line height). Real
  flush-left new paragraphs (after a scene-break ornament, or with extra
  leading) sit >=1.4x and stay separate. BLIND SPOTS still hand-fixed and
  re-verified with check_fidelity: a drop cap with leading punctuation; a
  ZapfDingbats ornament scene break; a real compound hyphen broken at a line end
  (check_fidelity strips hyphens); a born-digital stray-glyph glitch (render to
  plain sense, log it).
- **scripts/check_fidelity.py**: whole-unit letters+digits fidelity gate; keeps
  block-quote spans, excludes the 100pt chapter numeral. Run on every chapter.
  CANNOT see paragraph structure, hyphens, or stray punctuation - hence the
  hand checks above.
- **scripts/dump_anchors.py + scripts/anchor_offsets.py**: resolve every in-text
  reference mark to a unique verbatim anchor. **B04 additions (do not revert):**
  a fallback that accepts a unique anchor containing complete `*...*` italic
  runs, and a trailing-punctuation absorb that steps over a closing `*`, so a
  mark right after an italicized term lands after "*term*." not inside it.
- **scripts/build_ch0405_notes.py**: author-note assembler; **numbers author
  notes POSITIONALLY** (by in-text mark, not the printed back-matter label),
  which survives Isaacs's own back-matter misnumbering (ch05: "18, 18, 20").
  build_ch0405_editorial.py / add_ch0405_glossary.py: the per-batch editorial
  and glossary generators. (build_ch0203_* and build_ch01_* remain as templates.)
- **scripts/build_reading_epub.py**: `edition_kind: "annotated"` chrome; `{q} `
  block quotes; TWO-STREAM per-chapter note numbering (author arabic n-<unit>-N /
  editorial roman en-<unit>-r, both restart each chapter); markers ordered by
  ANCHOR-END position; an anchor may include `*` italic markers.
- **GLOSSARY IS SECTIONED (trap).** glossary.json has people/organizations/
  places/terms sections. apparatus_merge.py flattens it and breaks the build;
  add glossary rows STRAIGHT INTO their section (Write/Edit or add_ch0405_
  glossary.py). Notes and figures merge through apparatus_merge fine.
- **review/voice_gate_critic_prompt_annotation.md** + voice_gate_critique.py is
  edition-aware. epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/.

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles (or conventional English) forms STAY in the
  body; pinyin + hanzi go in the glossary and the first-appearance editorial
  note. One form per referent; check authority.json.
- Note architecture: author notes arabic, editorial roman, per-chapter restart,
  NO "Ed." prefix. ALL of Isaacs's own notes (numbered endnotes AND asterisks)
  go in the arabic stream, numbered by POSITION (not his printed labels).
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American
  English in editorial prose; dates "Month D, YYYY".
- Editorial-note voice (with the B04 refinements in STYLE.local): concise,
  factual; who/what/when + why-it-matters-here; verdict tag ONLY on a weighed
  claim; marker ON the glossed term; a note never vaguer than its text and never
  re-underlining the body's own point/irony; no competing translation of a term
  the body already renders; pinyin gloss applied consistently; no meta-filler.
- Principals set (Principal Characters page): Sun Yat-sen (1), Chiang Kai-shek
  (2), Chen Tu-hsiu (3), Borodin (4, keyed by 鲍罗廷). Wang Ching-wei is the
  next candidate (now head of party/government); promote when a batch confirms.

## Where the book stands

- Front matter frames the book; ch01 the 19th-c background; ch02 the theory;
  ch03 the 1919-25 narrative (May Fourth, CCP founding, the "bloc within," the
  labor/peasant upsurge, May Thirtieth, the Canton-Hong Kong strike). ch04-05
  turn to the struggle for power inside the Canton base: Chiang's rise through
  Whampoa and the Shanghai gangster-banker milieu, and his bloodless March 20,
  1926 coup (the Chung-shan gunboat incident) that put bourgeois hegemony over
  the mass movement while the Communists, under Comintern orders, capitulated
  and covered it up. ch06-08 move north with the Northern Expedition (July 1926
  on), across the Yangtze to the Shanghai insurrections and the eve of the
  April 1927 rupture.

## What is NEXT (grouping calibrated on Batches 1-4)

- B05 = ch06-07-08. Then, tuned as later chapters prove lighter: B06 = ch09-10-11;
  B07 = ch12-13-14; B08 = ch15-16-17; B09 = ch18-19-20.
- The FINAL batch stays light on chapters: it builds the LINKED index from all
  the per-chapter pagemaps (book.json _index_decision), does the whole-book
  reconciliation sweep (check 12), renders out/term_ledger.md, writes
  COMPLETION.md, and commits the final EPUB itself.

## Open items / cross-unit overlaps for the final reconciliation sweep

- Body offset is 23 (printed = PDF page - 23); front matter was 1. Cite ARABIC
  folios in body-chapter notes.
- Cross-unit overlaps the blind critic keeps flagging as "undefined" (Borodin,
  Sun Yat-sen, the Kuomintang, the Comintern, Wang Ching-wei, May Thirtieth,
  hsien, the Washington Conference): the documented false positive, noted at
  first appearance in an earlier-reading unit. The sweep confirms or trims.
- Source misprints kept visible: the Feb 7 1923 massacre toll (ch03);
  ch04 "whole interests" (for "whose"); ch05 back-matter endnotes misnumbered
  "18, 18, 20" (edition renumbers author notes by position). Digitization
  glitches rendered to plain sense and logged: ch04 "in the- masses", ch05
  "'overthrown'~".

## Environment / traps state

- Container is reprovisioned fresh each session. setup.sh installs pymupdf,
  pillow, epubcheck 5.1.0 AND (uselessly) Chinese tesseract packs, but NOT the
  English wordlists extract_isaacs.py needs - install wamerican/wbritish by hand
  (see kickoff step 1). No OCR needed. Build is text-only, ~0.2 MB.
- tests/run_tests.py "hook stands down on template stub" FAILS by design; do not
  "fix" it.
- Stray-branch / stale-tree check every batch (working branch
  claude/tragedy-of-the-chinese-revolution). B04's container had the tree parked
  on template-master; fetched and hard-reset onto the real tip.
