# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat alongside the attached EPUB.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B04

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). NOT a translation: source.pdf (repo root, 409 pages) has a clean
born-digital text layer, so there is no OCR and nothing to translate. The work
is annotation and faithful resetting. Batches 1-3 (front matter + ch01-03) are
done and set the whole machinery; you are extending it, not inventing it.

Read, in order: CLAUDE.md, then HANDOFF.md (full source characterization and the
do-not-revert tooling list), then book.json, then STYLE.local.md (the whole
style contract; it carries the Batch 1, 2 AND 3 voice-gate rulings - follow
them). BEFORE writing any editorial notes, read a sample of ch02/ch03's
editorial notes in notes.json (they ARE the note voice to match) and the final
two pages of ch03's English (out/ch03_reading.md) - that prose IS the register
the notes sit against.

Do Batch 4 = ch04 "Canton: To Whom the Power?" (PDF 83-97, printed 60-74) and
ch05 "Canton: The Coup of March 20, 1926" (PDF 98-116, printed 75-93), end to
end per the pipeline ch01-03 established:

1. Extract each unit VERBATIM: `python3 scripts/extract_isaacs.py ch04` and
   `... ch05` (body offset is 23, from book.json; folios come out arabic 60..
   and 75..). The extractor now CAPTURES set-off block quotations automatically
   (Isaacs sets them in 9.0pt, indented; they emit with the `{q} ` prefix) - so
   review the printed de-hyphenation report AND eyeball for any real compound
   hyphen broken at a line end (war-weary class), which check_fidelity cannot
   catch because it strips hyphens; restore those by hand. Then run
   `python3 scripts/check_fidelity.py ch04 ch05` and confirm BOTH streams are
   IDENTICAL (the byte-for-byte rule-4 gate).
2. AUTHOR notes (arabic): `python3 scripts/dump_anchors.py ch04` lists every
   in-text reference mark (superscript digit or asterisk) in reading order;
   `python3 scripts/anchor_offsets.py ch04 ch05` resolves each to a unique
   verbatim anchor. Dump the endnote bodies with dump_endnotes.py (ch04 endnotes
   are on PDF 368-369, ch05 on PDF 369-370 - verify the headings) and the
   asterisk foot footnotes from the extract report; assemble on the
   build_ch0203_notes.py pattern (endnotes cleaned with clean_body; asterisk
   bodies transcribed by hand with <i> and de-hyphenation, in position order).
3. EDITORIAL notes (roman, "ed": true) on the build_ch0203_editorial.py pattern,
   per CLAUDE.md's generous density model AND the STYLE.local rulings (marker ON
   the term; verdict tag ONLY where a claim is weighed; one subject one note; a
   note is never vaguer than its text; test each note against the adjacent
   paragraphs, not just its sentence; consistent pinyin gloss; no re-noting a
   subject an earlier-reading unit already covers). GREP notes.json and the
   earlier reading files first; keep a "NOT re-noted (already placed)" list in
   PROGRESS. New first-appearance subjects to expect: the Northern Expedition
   preliminaries, Hu Han-min, the March 20 1926 Chung Shan (Zhongshan) gunboat
   incident and Chiang's coup, the Whampoa cadets in action, the strike
   committee, more warlords (Chang Tso-lin, Sun Chuan-fang, Feng Yu-hsiang), and
   Comintern figures (Bubnov, the "Sixth Plenum of the E.C.C.I."). Fact-check
   against real scholarship (rule 5), verdict where checkable. Cite ARABIC
   printed folios in body notes.
4. Glossary: add new people/terms DIRECTLY INTO THEIR SECTION with Write/Edit
   (NOT apparatus_merge - it flattens the sectioned glossary and breaks the
   build; see the trap note below). Consult authority.json for shelf agreement;
   flag genuine principals with "principal": true and a cast_order/cast (Sun 1,
   Chiang 2, Chen Tu-hsiu 3, Borodin 4 are set; Wang Ching-wei and Chiang are
   the ones to watch as the narrative turns to him).
5. Build (`scripts/build_reading_epub.py`); qa_epub AND epubcheck BOTH clean
   (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; refetch per setup.sh if the
   container is fresh), check_apparatus clean, check_fidelity green. Run the
   Step 0c blind-critique loop on at least one unit; evolve STYLE.local.md.
6. Deliver the built EPUB in chat as an attached file (stamp a chat copy with
   `python3 scripts/stamp_deliverable.py B04`) and PASTE the next kickoff
   verbatim in the same reply. Update PROGRESS.md and HANDOFF.md; commit and push.

Do not pause for approval mid-batch. Cite printed folios (arabic for the body).
One branch only: claude/tragedy-of-the-chinese-revolution - expect a possible
stray per-task branch at the top and reconcile onto the working branch (this
session found none; the working tree had been reset to origin).
```

## What is DONE (do not redo)

- Survey session: book.json filled, builder adapted for an annotated edition,
  skeleton EPUB, SURVEY.md, source.pdf committed.
- **B01 (ch01 "Seeds of Revolt"): COMPLETE.** 85 notes (32 author + 53
  editorial), glossary bootstrapped, Sun flagged principal. Step 0c ran 3 rounds.
- **B02 (front matter: ch00a Foreword + ch00b Trotsky Introduction): COMPLETE.**
  47 front-matter notes (ch00a 16 ed + 1 author; ch00b 30 ed). 6 glossary rows
  (Chiang principal, Mao, Deng, Jiang Qing, CCP, Comintern). check_fidelity.py
  introduced.
- **B03 (ch02 "Problems of the Chinese Revolution" + ch03 "The New Awakening"):
  COMPLETE.** ch02 48 notes (29 author arabic + 19 editorial roman), ch03 90
  notes (59 author + 31 editorial). 28 glossary rows (Chen Tu-hsiu and Borodin
  added as principals, cast_order 3 and 4). Block-quote extraction, the author-
  note anchor tooling, and the chapter-numeral fidelity fix all landed here (see
  Tooling). Step 0c ran 2 rounds on ch03. Full record in PROGRESS.md.
- Cumulative build: **5 of 22 chapters, 270 notes, 74 pagebreaks, 0.2 MB.**
- 15 chapters remain (ch04-ch20).

## Tooling in place (DO NOT REVERT)

- **scripts/extract_isaacs.py**: faithful-reset extractor; per-unit offset from
  book.json (23 body, 1 front matter); de-hyphenation by Isaacs's own usage +
  word lists; drop-cap fold; furniture strip; superscript-ref removal; asterisk-
  footnote capture; pagemap. **B03 addition: set-off BLOCK QUOTATIONS** (size
  8.6-9.2pt AND indent x0 63-110, the geometry that separates a 9.0pt quote from
  the 9.0pt running heads/folios), emitted with `{q} `, with per-kind indent
  thresholds and cross-page continuation. BLIND SPOTS to fix by hand and
  re-verify with check_fidelity: a drop cap with leading punctuation (the ch00a
  `"F`), a ZapfDingbats ornament in the foot band (a `***` scene break), and a
  real compound hyphen that breaks at a line end (war-weary/three-quarter -
  check_fidelity strips hyphens so it cannot catch these; read the de-hyphen
  report).
- **scripts/check_fidelity.py** (do not revert): whole-unit letters+digits
  fidelity gate. B03 additions: it now keeps the 9.0pt block-quote spans (same
  geometry gate as the extractor) AND excludes the 100pt chapter numeral (the
  big-glyph keep now requires a letter, so the drop cap survives but the numeral
  is dropped). Run on every chapter.
- **scripts/dump_anchors.py + scripts/anchor_offsets.py** (new in B03): resolve
  every in-text reference mark to a unique verbatim reading-file anchor by
  reducing both sides to a letters+digits stream and mapping the mark's position
  back, extending over the trailing punctuation the marks follow. Writes
  data/anchors/<id>.json.
- **scripts/build_ch0203_notes.py / build_ch0203_editorial.py /
  add_ch0203_glossary.py** (new in B03): the per-batch note and glossary
  generators; good per-chapter templates alongside build_ch01_notes.py.
- **scripts/build_reading_epub.py**: `edition_kind: "annotated"` chrome; the
  `{q} ` block-quote marker; TWO-STREAM per-chapter note numbering (author
  arabic n-<unit>-N / editorial roman en-<unit>-r, both restart each chapter);
  markers ordered by ANCHOR-END position, so array order in notes.json does not
  affect numbering, and an anchor may include `*` italic markers.
- **scripts/dump_endnotes.py**, build_ch01_notes.py, build_ch01_editorial.py:
  the ch01 endnote dumper + note generators (also good templates).
- **review/voice_gate_critic_prompt_annotation.md** + voice_gate_critique.py is
  edition-aware. epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/.
- **GLOSSARY IS SECTIONED (trap).** glossary.json has people/organizations/
  places/terms sections that the builder's render_glossary and Principal
  Characters page walk. `apparatus_merge.py` assumes a FLAT glossary and appends
  rows at the TOP LEVEL, which breaks the build. Add glossary rows STRAIGHT INTO
  their section (Write/Edit or a small script like add_ch0203_glossary.py).
  Notes and figures merge through apparatus_merge fine.

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles (or conventional English) forms STAY in the
  body; pinyin + hanzi go in the glossary and the first-appearance editorial
  note. One form per referent; check authority.json.
- Note architecture: author notes arabic, editorial roman, per-chapter restart,
  NO "Ed." prefix. ALL of Isaacs's own notes (numbered endnotes AND asterisks)
  go in the arabic stream, numbered by position.
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American
  English in editorial prose; dates "Month D, YYYY".
- Editorial-note voice (now with the B03 refinements in STYLE.local): concise,
  factual; who/what/when + why-it-matters-here; verdict tag ONLY on a weighed
  claim; marker lands ON the glossed term; a note is never vaguer than its text;
  test each note against the whole paragraph it sits in (not just its sentence);
  pinyin gloss applied consistently to named Chinese figures; no meta-filler
  ("central figure in Isaacs's account"), no feeling-management ("notoriously").
- Principals set (Principal Characters page): Sun Yat-sen (1), Chiang Kai-shek
  (2), Chen Tu-hsiu (3), Borodin (4). Borodin is keyed by his Chinese
  transliteration 鲍罗廷 so the page can carry a non-Chinese principal.

## Where the book stands

- Front matter frames the book; ch01 gives the 19th-c background; ch02 is
  Isaacs's theoretical chapter (why only the proletariat, led by a Communist
  party, could carry China's bourgeois-democratic revolution, and how Stalin's
  Comintern abandoned that line for a "bloc" with the bourgeoisie); ch03 opens
  the 1919-25 narrative (May Fourth, the CCP's founding, the "bloc within" entry
  into the Kuomintang, Sun's reorganization with Borodin and Whampoa, the labor
  and peasant upsurge, the May Thirtieth movement, the Canton-Hong Kong strike).
  ch04-05 turn to the struggle for power inside the Canton base and Chiang's
  March 20, 1926 coup - the point where Chiang moves to the center.

## What is NEXT (grouping calibrated on Batches 1-3)

- B04 = ch04-05. Then, tuned as later chapters prove lighter: B05 = ch06-07-08;
  B06 = ch09-10-11; B07 = ch12-13-14; B08 = ch15-16-17; B09 = ch18-19-20.
- The FINAL batch stays light on chapters: it builds the LINKED index from all
  the per-chapter pagemaps (book.json _index_decision), does the whole-book
  reconciliation sweep (check 12), renders out/term_ledger.md, writes
  COMPLETION.md, and commits the final EPUB itself.

## Open items / cross-unit overlaps for the final reconciliation sweep

- Body offset is 23 (printed = PDF page - 23); front matter was 1. Cite ARABIC
  folios in body-chapter notes.
- Cross-unit overlaps logged (deliberate first-appearance-per-context, the sweep
  confirms or trims): Kuomintang (ch00a phrase + ch00b + ch01), Sun Yat-sen
  (Principal Characters + ch00b + ch01), the Comintern (ch00a + used throughout).
  The blind critic keeps flagging these as "undefined" in later units - that is
  the documented cross-unit false positive, not a gap.
- Source discrepancy kept visible: the Feb 7 1923 massacre toll (Isaacs's
  "sixty" vs the ~30s of later estimates) is footnoted, not corrected.

## Environment / traps state

- Container is reprovisioned fresh each session: run setup.sh (pymupdf, pillow,
  wamerican/wbritish, epubcheck 5.1.0). No tesseract/OCR needed. Build is
  text-only + one generated cover, ~0.2 MB, well under the 30 MB cap.
- tests/run_tests.py "hook stands down on template stub" FAILS by design (the
  test restores a HANDOFF with a real kickoff, so the hook correctly fires). Do
  not "fix" the hook.
- Stray-branch check every batch (working branch
  claude/tragedy-of-the-chinese-revolution). This session found no stray branch;
  the working tree was reset to origin at the top.
