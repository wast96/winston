# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat alongside the attached EPUB.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B03

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). NOT a translation: source.pdf (repo root, 409 pages) has a clean
born-digital text layer, so there is no OCR and nothing to translate. The work
is annotation and faithful resetting. Batches 1 (ch01) and 2 (front matter) are
done and set the whole machinery; you are extending it, not inventing it.

Read, in order: CLAUDE.md, then HANDOFF.md (full source characterization and the
do-not-revert tooling list), then book.json, then STYLE.local.md (the whole
style contract; it now carries the Batch 1 AND Batch 2 voice-gate rulings —
follow them). BEFORE writing any editorial notes, read ch01's editorial notes in
notes.json and a few of the front-matter notes (ch00a/ch00b): they ARE the note
voice to match. Then read the final two pages of ch01's English
(out/ch01_reading.md) — that prose IS the register the notes sit against.

Do Batch 3 = ch02 "Problems of the Chinese Revolution" (PDF 42-62, printed
19-39) and ch03 "The New Awakening" (PDF 63-82, printed 40-59), end to end per
the pipeline ch01/the front matter established:

1. Extract each unit VERBATIM: `python3 scripts/extract_isaacs.py ch02` and
   `... ch03` (body offset is 23, read from book.json; folios come out arabic
   19.. and 40..). REVIEW the printed de-hyphenation report, then run
   `python3 scripts/check_fidelity.py ch02 ch03` and confirm BOTH streams are
   IDENTICAL (this is the byte-for-byte rule-4 gate; it excludes running heads,
   folios, the chapter title, the 8pt footnotes, superscripts and any ornament,
   and strips ***/{q}/markdown before comparing). Eyeball the report for any
   drop-cap or ornament the size classifier mishandles (the front matter had a
   `"F` drop cap and a ZapfDingbats scene break the extractor missed — fix such
   cases by hand and let check_fidelity confirm). ch02/ch03 are theory-and-
   narrative chapters and WILL quote documents/speeches at length: mark real
   block quotations with the `{q} ` line prefix so the builder sets them off.
2. CHARACTERIZE each unit's apparatus: Isaacs's own numbered endnotes (printed
   340-373) for these chapters PLUS any asterisked page-foot footnotes. Convert
   ALL of them to the ARABIC author stream, numbered by position, exactly as
   ch01 did (scripts/dump_endnotes.py for the endnote bodies + the
   build_ch01_notes.py pattern; anchors resolved against the reading file).
3. Editorial notes (ROMAN stream, "ed": true) per CLAUDE.md's generous density
   model AND the STYLE.local.md rulings (marker lands ON the glossed term; no
   "Pinyin:" trailer; verdict tag ONLY where an author claim is weighed; one
   subject one note; don't gloss ordinary English; no editorial-policy or
   body-restating filler; map the old romanizations). MOST of the 19th/early-20th
   cast AND the Comintern/Bolshevik cast are already noted (ch01 + the front
   matter): GREP notes.json and the earlier reading files before adding a note,
   cross-reference instead of re-noting, and keep a "NOT re-noted (already
   placed)" list in PROGRESS. New first-appearance subjects to expect in ch02-03:
   the May Fourth movement, the May Thirtieth incident, Borodin, Chen Tu-hsiu,
   the Third International congresses, the CCP's founding, Sun's reorganization of
   the KMT (1923-24), the Whampoa Academy, Comintern agents (Maring/Voitinsky),
   the "two-stage"/"bloc within" line. Fact-check against real scholarship (rule
   5), verdict where checkable. Body folios are ARABIC now (cite the printed
   folio, e.g. 27, not the PDF page).
4. Glossary: add new people/terms DIRECTLY INTO THEIR SECTION
   (people/organizations/places/terms) with the Write/Edit tool, key=hanzi,
   en=the form Isaacs uses, pinyin, note. DO NOT rely on apparatus_merge for the
   glossary — it flattens rows to the top level and breaks the build (see the
   trap note in HANDOFF). Consult authority.json for shelf agreement; flag
   genuine principals with "principal": true (Chiang and Sun are already flagged;
   Borodin and Chen Tu-hsiu are likely principals — add cast_order/cast).
5. Build (`scripts/build_reading_epub.py`); qa_epub AND epubcheck BOTH clean
   (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; refetch per setup.sh if the
   container is fresh), check_apparatus clean. Run the Step 0c blind-critique
   loop (annotation variant is automatic) on at least one unit; evolve
   STYLE.local.md with anything new.
6. Deliver the built EPUB in chat as an attached file (stamp a chat copy with
   `python3 scripts/stamp_deliverable.py B03`) and PASTE the next kickoff
   verbatim in the same reply. Update PROGRESS.md and HANDOFF.md; commit.

Do not pause for approval mid-batch. Cite printed folios (arabic for the body).
One branch only: claude/tragedy-of-the-chinese-revolution — expect a stray
per-task branch at the top and reconcile onto the working branch.
```

## What is DONE (do not redo)

- Survey session: book.json filled, builder adapted for an annotated edition,
  skeleton EPUB built, SURVEY.md written, source.pdf committed.
- **Batch 1 (ch01 "Seeds of Revolt"): COMPLETE.** out/ch01_reading.md (verbatim,
  fidelity-verified), data/pagemap/ch01.json, 85 notes (32 author arabic + 53
  editorial roman), glossary bootstrapped, Sun Yat-sen flagged principal. Builder
  features (block-quote, two-stream notes) implemented and gated green. Step 0c
  ran 3 rounds; STYLE.local.md carries the Batch 1 rulings.
- **Batch 2 (front matter: ch00a Foreword + ch00b Trotsky Introduction):
  COMPLETE.** out/ch00a_reading.md (11 paras; drop cap and a ZapfDingbats scene
  break restored by hand; `***` scene break; signature split) and
  out/ch00b_reading.md (33 paras), both fidelity-verified byte-for-byte with the
  new check_fidelity.py. 47 front-matter notes: ch00a 16 editorial + 1 author
  (Arnold's Kuomintang-spelling footnote); ch00b 30 editorial, 0 author (Trotsky
  carries no apparatus of his own). 6 glossary rows added (Chiang principal, Mao,
  Deng, Jiang Qing, CCP, Comintern). Step 0c blind loop ran on both units (2
  rounds on ch00b). qa_epub + epubcheck + check_apparatus all green. Full record
  in PROGRESS.md.
- Cumulative build: 3 of 22 chapters, 132 notes, 33 pagebreaks, 0.1 MB.
- 17 chapters remain (ch04-ch20). Provisional grouping below.

## Tooling in place (DO NOT REVERT)

- **scripts/extract_isaacs.py**: faithful-reset extractor; offset per-unit from
  book.json (23 body, 1 front matter); de-hyphenation by Isaacs's own usage +
  word lists; drop-cap fold; furniture strip; superscript-ref removal; asterisk-
  footnote capture; writes reading md + pagemap; prints a review report. NOTE its
  blind spots (fix by hand, then re-verify with check_fidelity): a drop cap that
  includes leading punctuation (`"F`) fails the single-letter test; a
  ZapfDingbats/ornament scene break in the 7.6-8.4pt band is mis-captured as a
  footnote (it is a `***` scene break).
- **scripts/check_fidelity.py** (NEW in B02, do not revert): whole-unit
  letters+digits fidelity check — reduces the reading body and the PDF prose
  spans to a lowercase [a-z0-9] stream and asserts identical; run it on every
  chapter as the rule-4 gate.
- **scripts/build_reading_epub.py**: `edition_kind: "annotated"` chrome; the
  `{q} ` block-quote marker; TWO-STREAM per-chapter note numbering (author arabic
  n-<unit>-N / editorial roman en-<unit>-r, both restart each chapter); the
  builder orders note markers by ANCHOR-END position, so array order in
  notes.json does not affect numbering, and an anchor may include the `*` italic
  markers (used to land a marker on an italicized term).
- **scripts/qa_epub.py**: note check for the two per-chapter streams. **dump_endnotes.py**,
  build_ch01_notes.py, build_ch01_editorial.py: endnote dumper + the ch01 note
  generators (good per-chapter templates).
- **review/voice_gate_critic_prompt_annotation.md** + voice_gate_critique.py is
  edition-aware. epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/.
- **GLOSSARY IS SECTIONED (trap).** glossary.json has people/organizations/places/
  terms sections; the builder's render_glossary and Principal Characters page
  walk those sections. `apparatus_merge.py` assumes a FLAT glossary and will
  append rows at the TOP LEVEL, which breaks the build. Add glossary rows STRAIGHT
  INTO their section (Write/Edit), or move them after a merge. Notes and figures
  merge through apparatus_merge fine.

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles (or conventional English) forms STAY in the
  body; pinyin + hanzi go in the glossary and the first-appearance editorial
  note. One form per referent; check authority.json.
- Note architecture: author notes arabic, editorial roman, per-chapter restart,
  NO "Ed." prefix. ALL of Isaacs's own notes (numbered endnotes AND asterisked
  footnotes) go in the arabic stream, numbered by position.
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American English
  in editorial prose; dates "Month D, YYYY".
- Editorial-note voice: concise, factual, modern American English; who/what/when
  + why-it-matters-here; verdict tag ONLY where a claim is weighed; the marker
  lands ON the glossed term; no "Pinyin:" trailer, no editorial-policy or
  body-restating filler, no bare print-folio parentheticals, one subject one note.
  Full rulings in STYLE.local.md (Batch 1 + Batch 2 sections).
- Reading order is ch00a → ch00b → ch01 → ch02 → ...: the FRONT MATTER reads
  before ch01, so the shared cast (Chiang, KMT, Comintern, Bolsheviks, Sun) first
  appears there. A blind per-unit critic flags these as "undefined" in a later
  unit — cross-unit false positive when already noted in an earlier-reading unit.

## Cast / voice reference (for the notes)

- Already noted (do NOT re-note; cross-reference): the whole ch01 19th/early-20th
  cast (Sun Yat-sen, the Manchus, Taiping/Hung, Tseng Kuo-fan, Li Hung-chang,
  Kang/Liang, Cixi, Yuan Shih-kai, Puyi, the Boxers, the Triads, the reform and
  1911 events, the treaty-port furniture) AND the front-matter cast (Harold &
  Arnold Isaacs, Trotsky, Lenin, Stalin, Bukharin, Plekhanov, the
  Bolsheviks/Mensheviks/SRs/Narodniks, Mao, Deng, Jiang Qing, the Comintern, CCP,
  Kuomintang, permanent revolution, the bloc of four classes, historical
  materialism, the dialectic, semi-colonial/bourgeois/proletariat, the Popular
  Front, defeatism, the three Russian revolutions, the April Theses, Sun's Three
  Principles).
- Cross-unit overlaps logged for the final reconciliation sweep: Kuomintang
  (ch00a phrase + ch00b note + ch01 full) and Sun Yat-sen (Principal Characters +
  ch00b + ch01) are noted more than once by design; the final sweep confirms or
  trims.

## Where the book stands

- The front matter frames the book (Arnold's memoir of his father; Trotsky's
  polemic staking the "permanent revolution" reading). ch01 gives the 19th-c
  background. ch02 ("Problems of the Chinese Revolution") is Isaacs's own
  theoretical chapter; ch03 ("The New Awakening") begins the 1919-25 narrative
  (May Fourth, the CCP's founding, the KMT-Communist alliance). The 1925-27
  principals proper (Borodin, Chen Tu-hsiu, and Chiang in action) arrive here and
  in ch04+.

## What is NEXT (grouping calibrated on Batches 1-2)

- B03 = ch02-03 (theory + the awakening; keep to 2, they are dense). Then, tuned
  as later chapters prove lighter: B04 = ch04-05; B05 = ch06-07-08; B06 =
  ch09-10-11; B07 = ch12-13-14; B08 = ch15-16-17; B09 = ch18-19-20.
- The FINAL batch stays light on chapters: it also builds the LINKED index from
  all the per-chapter pagemaps (book.json _index_decision), does the whole-book
  reconciliation sweep (check 12; the Kuomintang/Sun overlaps above are on its
  worklist), and writes COMPLETION.md.

## Commissioner decisions (settled)

- LINKED index (final batch, from per-chapter pagemaps). Two note layers told
  apart by NUMERAL SYSTEM (author arabic, editorial roman, per-chapter, no "Ed."
  prefix). 2009 Foreword KEPT as front matter.

## Open items / traps for the next session

- Body offset is 23 (printed = PDF page - 23); front matter was 1. Cite ARABIC
  folios in body-chapter notes.
- Watch for BLOCK QUOTES from ch02 on (Isaacs quotes resolutions, speeches,
  documents): mark them `{q} ` per line; check_fidelity strips the marker before
  comparing, so a real quote block still verifies.
- Glossary sectioning trap (above): do not add glossary rows via apparatus_merge.
- Known non-issue: tests/run_tests.py "hook stands down on template stub" FAILS
  by design (the test restores a HANDOFF with a real kickoff, so the hook
  correctly fires). Do not "fix" the hook.

## Environment / traps state

- Container is reprovisioned fresh each session: run setup.sh (pymupdf, pillow,
  wamerican/wbritish, epubcheck 5.1.0). No tesseract/OCR needed. Build is
  text-only + one generated cover, ~0.1 MB, well under the 30 MB cap.
- Stray-branch check every batch per CLAUDE.md rule 2 (working branch
  claude/tragedy-of-the-chinese-revolution).
