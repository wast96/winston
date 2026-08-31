# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat alongside the attached EPUB.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B07

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). NOT a translation: source.pdf (repo root) has a clean born-digital
text layer, so there is no OCR and nothing to translate. The work is annotation
and faithful resetting. Batches 1-6 (front matter + ch01-11) are done and set
the whole machinery; you are extending it, not inventing it.

Read, in order: CLAUDE.md, then HANDOFF.md (full source characterization and the
do-not-revert tooling list), then book.json, then STYLE.local.md (the whole
style contract; it carries the Batch 1-6 voice-gate rulings - follow them).
BEFORE writing any editorial notes, read a sample of ch09/ch10/ch11's editorial
notes in notes.json (they ARE the note voice to match) and the final two pages
of ch11's English (out/ch11_reading.md) - that prose IS the register the notes
sit against.

Do Batch 7 = ch12 "The 'Revolutionary Center' at Work" (PDF 197-215, printed
174-192), ch13 "The Struggle for the Land" (PDF 216-234, printed 193-211), and
ch14 "Moscow and Wuhan" (PDF 235-249, printed 212-226), end to end per the
pipeline ch01-11 established:

1. FIRST run ./setup.sh, THEN `sudo apt-get install -y -qq wamerican wbritish`
   (setup.sh does NOT install the English wordlists extract_isaacs.py needs for
   de-hyphenation - it installs Chinese OCR packs the extractor never uses).
   Confirm /usr/share/dict/american-english exists. Expect a possible stray
   per-task branch and a stale working tree at the top: `git fetch origin
   claude/tragedy-of-the-chinese-revolution` and hard-reset onto it if HEAD is
   not at the real tip (every container so far has been parked on
   template-master). Only the by-design test "hook stands down on template
   stub" fails; do not fix it.
2. Extract each unit VERBATIM: `python3 scripts/extract_isaacs.py ch12` etc.
   (body offset 23; folios come out arabic 174.., 193.., 212..). REVIEW the
   de-hyphenation report AND eyeball for real compound hyphens broken at a line
   end (the "war-weary" class: a hyphen at a line break whose closed form is a
   non-word is a HARD hyphen - keep it; B05/B06 restored breaking-point,
   liberal-reform, eighty-two, half-page, worn-out, semi-adulterated, and a
   "Chiang Kai-shek...and" whose hyphen was dropped because "...and" attached to
   the fragment). Then `python3 scripts/check_fidelity.py ch12 ch13 ch14` and
   confirm all green (it now keeps inline small-caps like "4:30 A.M." via a
   block-body-dominance gate - do not revert). Also scan each reading file for a
   paragraph ending mid-sentence OR starting mid-word (a residual spurious split;
   a mid-sentence end that precedes a {q} block is a normal quote intro, fine),
   and for born-digital glitches (stray hyphen/tilde, or a C0 control char like
   the NUL that hit ch10's back matter; render to plain sense and LOG in PROGRESS).
3. AUTHOR notes (arabic): `dump_anchors.py`, `anchor_offsets.py`, then
   `dump_endnotes.py`. Endnote heading "12. The 'Revolutionary Center' at Work"
   begins PDF 380; find the ch13 and ch14 headings and the ranges (the next
   chapter heading closes each range). Assemble on the build_ch0911_notes.py
   pattern, which numbers author notes POSITIONALLY (by in-text mark) and anchors
   ASTERISK footnotes EXPLICITLY (do NOT trust anchor_offsets to find every
   asterisk mark: B06 hit TWO asterisk footnotes whose in-text mark is absent
   from the born-digital text layer - one in ch09, and ch11's single note that
   prints as two foot paragraphs with no ** on the second). For each asterisk,
   crop-verify by eye where its mark sits (or, if absent, its unambiguous
   referent) and anchor it there; read the foot body programmatically and
   reduce-check it against the raw foot text. WATCH for source label quirks in
   the back matter; verify the parsed labels come out a sequential 1..N run.
   Isaacs's ** on a page = the SECOND foot footnote (anchor_offsets collapses a
   run of asterisks into one mark - do not revert). Transcribe asterisk foot
   footnotes with <i>, dropping any stray trailing glyph.
4. EDITORIAL notes (roman, "ed": true) on the build_ch0911_editorial.py pattern,
   per CLAUDE.md's generous density model AND the STYLE.local rulings (marker ON
   the term; verdict tag ONLY where a claim is weighed; one subject one note; a
   note never vaguer than its text AND never restates the body, the author's own
   citation, or its irony; no competing translation of a term the body renders;
   a significance/"first" claim grammatical and scoped; identify a quoted
   eyewitness by placement PLUS vantage, minus both duplications; a book-specific
   proper name takes the body's own capitalization; read each note's dash-tail
   as a standalone sentence; consistent pinyin gloss; no re-noting a subject an
   earlier-reading unit already covers). GREP notes.json and the earlier reading
   files first; keep a "NOT re-noted" list in PROGRESS. New first-appearance
   subjects to expect: the Wuhan "Left" government's actual conduct, the peasant
   revolt in Hunan and its suppression (the "Horse Day"/May 21 Changsha
   incident), T. V. Soong, the Fifth CCP Congress (late April 1927), M. N. Roy
   and Stalin's June 1927 telegram to Wuhan (Roy showed it to Wang Ching-wei),
   Feng Yu-hsiang's Chengchow and Hsuchow conferences and his defection, more
   Comintern figures. Fact-check against real scholarship, verdict where
   checkable. NEVER cite Grok/Grokipedia. Cite ARABIC printed folios in body notes.
5. Glossary: add new people/terms DIRECTLY INTO THEIR SECTION with a small
   script like add_ch0911_glossary.py (NOT apparatus_merge - it flattens the
   sectioned glossary). Consult authority.json for shelf agreement; principals
   are Sun 1, Chiang 2, Chen Tu-hsiu 3, Borodin 4, Wang Ching-wei 5, Chow En-lai
   6 - consider promoting Chiu Chiu-pei (Qu Qiubai) when he moves to center
   (he succeeds Chen in August 1927, ch16 region).
6. Build (build_reading_epub.py); qa_epub AND epubcheck BOTH clean (jar at
   /tmp/epubcheck-5.1.0/epubcheck.jar; refetch per setup.sh if the container is
   fresh), check_apparatus clean, check_fidelity green on ALL units. Run the
   Step 0c blind-critique loop on at least one unit; evolve STYLE.local.md.
7. Deliver the built EPUB in chat as an attached file (stamp a chat copy with
   `python3 scripts/stamp_deliverable.py B07`) and PASTE the next kickoff
   verbatim in the same reply. Update PROGRESS.md and HANDOFF.md; commit and push.

Do not pause for approval mid-batch. Cite printed folios (arabic for the body).
One branch only: claude/tragedy-of-the-chinese-revolution - reconcile any stray
branch onto it.
```

## What is DONE (do not redo)

- Survey session: book.json filled, builder adapted for an annotated edition,
  skeleton EPUB, SURVEY.md, source.pdf committed.
- **B01 (ch01): COMPLETE.** 85 notes (32 author + 53 editorial). Step 0c 3 rounds.
- **B02 (front matter ch00a + ch00b): COMPLETE.** 47 notes. check_fidelity.py.
- **B03 (ch02 + ch03): COMPLETE.** ch02 48, ch03 90 notes.
- **B04 (ch04 + ch05): COMPLETE.** ch04 47, ch05 69 notes. 19 glossary rows.
- **B05 (ch06 + ch07 + ch08): COMPLETE.** ch06 54, ch07 29, ch08 54 notes. 18
  glossary rows. Wang Ching-wei promoted to principal 5.
- **B06 (ch09 "The Conspiracy of Silence" + ch10 "The Coup of April 12, 1927" +
  ch11 "Wuhan: The Revolutionary Center"): COMPLETE.** ch09 61 notes (58 author
  + 3 editorial), ch10 48 (42 + 6), ch11 35 (29 + 6); 144 notes this batch. 5
  glossary rows. Chow En-lai promoted to principal 6. Three
  extractor/note-tooling fixes (small-caps fidelity gate; {q}-marker skip in
  anchor reduction; explicit asterisk anchoring + C0 control-char strip). Step
  0c ran 2 rounds on ch11, convergent. Full record in PROGRESS.md.
- Cumulative build: **13 of 22 chapters, 668 notes, 187 pagebreaks, 0.3 MB.**
- 9 chapters remain (ch12-ch20).

## Tooling in place (DO NOT REVERT)

- **scripts/extract_isaacs.py**: faithful-reset extractor; per-unit offset from
  book.json (23 body, 1 front matter); de-hyphenation; drop-cap fold; furniture
  strip; superscript-ref removal; asterisk-footnote capture; block-quote
  capture ({q}); gap-ratio merge of spurious mid-page paragraph splits (B04);
  pagemap. BLIND SPOTS still hand-fixed and re-verified with check_fidelity: a
  real compound hyphen broken at a line end (the "war-weary" class); a
  born-digital stray-glyph or control-char glitch (render to plain sense, log it).
- **scripts/check_fidelity.py**: whole-unit letters+digits fidelity gate. **B06
  addition (do not revert): a body-DOMINANT block emits all its spans, so an
  inline sub-body small-caps span survives** (ch10's "4:30 A.M." sets A and M at
  7.5pt, below the 9.3pt per-span floor; the extractor keeps them because it
  classifies the whole block as body). Verified all 13 units + front matter stay
  green. CANNOT see paragraph structure, hyphens, or stray punctuation - hence
  the hand checks above.
- **scripts/dump_anchors.py + scripts/anchor_offsets.py**: resolve in-text marks
  to unique verbatim anchors. B04: italic-run fallback + closing-`*` absorb. B05:
  collapse a run of consecutive asterisks into ONE mark (Isaacs's `**` is the
  SECOND page-foot footnote). **B06 addition (do not revert): skip the single
  letter of a "{q} "/"{v} " block marker when reducing the reading stream**, so a
  stray q/v/d/g/p is not injected; without it ch09's signature note 29 (after the
  one-line quote "{q} Chen.") would not resolve. Regenerating ch01-08 changed
  only ch03 note 47, for the better (marker now after the closing italic+period);
  the built book is unaffected (ch03's committed notes.json anchor is still a
  valid unique substring).
- **scripts/build_ch0911_notes.py**: author-note assembler with EXPLICIT asterisk
  anchoring (B06: two asterisk references have NO extractable in-text mark - a
  ch09 note whose mark is absent from text layer AND page image, and ch11's note
  that prints as two foot paragraphs with no `**`; anchor each by its
  crop-verified referent), programmatic foot-body reading with a reduce
  drift-check, "Kaishek" -> "Kai-shek" hard-hyphen restore, C0 control-char strip
  (ch10 endnote 9 carries a literal NUL in the text layer), and a per-anchor
  override (a cross-paragraph anchor the builder cannot insert per paragraph is
  remapped to the unique first line). build_ch0608_notes.py (positional; robust
  to Isaacs's misnumbered/period-less labels) remains the template for a batch
  whose asterisk marks all survive.
- **scripts/build_reading_epub.py**: `edition_kind: "annotated"` chrome; `{q} `
  block quotes; TWO-STREAM per-chapter note numbering (author arabic / editorial
  roman, both restart each chapter); markers ordered by ANCHOR-END position; an
  anchor may include `*` italic markers. REFUSES a build on an unmatched note
  anchor (this is why a cross-paragraph anchor must be overridden, not merged).
- **GLOSSARY IS SECTIONED (trap).** glossary.json has people/organizations/
  places/terms sections (each a dict keyed by hanzi). apparatus_merge flattens it
  and breaks the build; add glossary rows STRAIGHT INTO their section (a small
  script like add_ch0911_glossary.py). Notes and figures merge through
  apparatus_merge fine.
- **review/voice_gate_critic_prompt_annotation.md** + voice_gate_critique.py is
  edition-aware. epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/.

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles (or conventional English) forms STAY in the
  body; pinyin + hanzi go in the glossary and the first-appearance editorial
  note. One form per referent; check authority.json. Isaacs's own spellings this
  batch: "Sun Fo", "George Hsu-chien", "Ku Meng-yu", "Soong Ching-ling", "Yung
  Chung-chin", "Chow En-lai", "Chen Chuen", "Hsin Ting-yu", "Ku Chen-chung".
- Note architecture: author notes arabic, editorial roman, per-chapter restart,
  NO "Ed." prefix. ALL of Isaacs's own notes (numbered endnotes AND asterisks)
  go in the arabic stream, numbered by POSITION.
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American
  English in editorial prose; dates "Month D, YYYY". A book-specific proper name
  (e.g. "Left Kuomintang") takes the body's own capitalization in the notes.
- Editorial-note voice (with the B01-B06 refinements in STYLE.local): concise,
  factual; who/what/when + why-it-matters-here; verdict tag ONLY on a weighed
  claim; marker ON the glossed term; a note never vaguer than its text and never
  restating the body, the adjacent author citation, or the body's own irony; a
  quoted eyewitness gets placement PLUS vantage, no citation-duplication; a
  significance/"first" claim grammatical and scoped; each note's dash-tail reads
  as a standalone grammatical sentence; pinyin gloss applied consistently.
- Principals (Principal Characters page): Sun Yat-sen (1), Chiang Kai-shek (2),
  Chen Tu-hsiu (3), Borodin (4), Wang Ching-wei (5), Chow En-lai (6, promoted
  B06). Chiu Chiu-pei (Qu Qiubai) is the next candidate when he succeeds Chen at
  the party head in August 1927.

## Where the book stands

- Front matter frames the book; ch01-03 background and 1919-25; ch04-05 the
  Canton power struggle and Chiang's March 20 1926 coup; ch06-08 the Northern
  Expedition to the Yangtze and the two Shanghai risings; ch09-11 the "conspiracy
  of silence" that disarmed the Shanghai workers, Chiang's April 12 1927 coup and
  massacre (the gangster "Workers' Trade Alliance," Chou En-lai's escape), and
  the opening of the Wuhan act: Stalin's "revolutionary center" theses and
  Trotsky's rebuttal, and the petty-bourgeois Left-Kuomintang cast (Wang
  Ching-wei, Hsu-chien, Ku Meng-yu, Sun Fo, Soong Ching-ling, Teng Yen-ta) whom
  Borodin likened to a rabbit before an anaconda. ch12-14 turn to the Wuhan
  government AT WORK, the struggle for the land in Hunan and its suppression, and
  Moscow's and Wuhan's dealings as the "Left" bloc breaks down.

## What is NEXT (grouping calibrated on Batches 1-6)

- B07 = ch12-13-14. Then, tuned as later chapters prove lighter: B08 = ch15-16-17;
  B09 = ch18-19-20.
- The FINAL batch stays light on chapters: it builds the LINKED index from all
  the per-chapter pagemaps (book.json _index_decision), does the whole-book
  reconciliation sweep (check 12), renders out/term_ledger.md, writes
  COMPLETION.md, updates authority.json with this book's decided renderings (e.g.
  Xu Qian, new to the shelf this batch), and commits the final EPUB itself.

## Open items / cross-unit overlaps for the final reconciliation sweep

- Body offset is 23 (printed = PDF page - 23); front matter was 1. Cite ARABIC
  folios in body-chapter notes.
- Cross-unit overlaps the blind critic keeps flagging as "undefined" (Wang
  Ching-wei, Borodin, Chen Tu-hsiu, Eugene Chen, Teng Yen-ta, Liao Chung-kai,
  Feng Yu-hsiang, Tang Sheng-chih, Mif, the Kuomintang, the Comintern, the "bloc
  of four classes", and earlier: Voitinsky, Wu Pei-fu, Chang Tso-lin, May
  Thirtieth, hsien, compradore): each noted at first appearance in an
  earlier-reading unit. The documented false positive; the sweep confirms.
- Source quirks kept visible: the Feb 7 1923 massacre toll (ch03); ch04 "whole
  interests"; ch05 back-matter endnotes misnumbered "18, 18, 20"; ch06 endnote 14
  printed "14" (no period); Malraux both "Man's Fate" and "Mans' Fate" (ch07/ch09);
  ch09 two-line signature "Signed: Wang / Chen."; ch10 "the people [sic]" and
  "not accepting (?) battle" (Isaacs's own brackets); ch11 p193 a quotation
  closing with an opening-style curly quote (U+201C). Digitization glitches
  rendered to plain sense and logged: ch04 "in the- masses", ch05 "'overthrown'~",
  and ch10 endnote 9's NUL byte (rendered to a space).
- Green Gang bridge (ch04 note "Huang Chin-jung"/"Tu Yueh-sheng" vs the B05
  glossary body forms "Hwang Ching-yung"/"Tu Yueh-sen"): the sweep should confirm
  the reader can bridge these.

## Environment / traps state

- Container is reprovisioned fresh each session. setup.sh installs pymupdf,
  pillow, epubcheck 5.1.0 AND (uselessly) Chinese tesseract packs, but NOT the
  English wordlists extract_isaacs.py needs - install wamerican/wbritish by hand
  (kickoff step 1). No OCR needed. Build is text-only, ~0.3 MB.
- tests/run_tests.py "hook stands down on template stub" FAILS by design; do not
  "fix" it.
- Stray-branch / stale-tree check every batch (working branch
  claude/tragedy-of-the-chinese-revolution). B06's container had the tree parked
  on template-master (df55427); fetched and hard-reset onto the real tip.
