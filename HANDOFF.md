# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat alongside the attached EPUB.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B06

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). NOT a translation: source.pdf (repo root) has a clean born-digital
text layer, so there is no OCR and nothing to translate. The work is annotation
and faithful resetting. Batches 1-5 (front matter + ch01-08) are done and set
the whole machinery; you are extending it, not inventing it.

Read, in order: CLAUDE.md, then HANDOFF.md (full source characterization and the
do-not-revert tooling list), then book.json, then STYLE.local.md (the whole
style contract; it carries the Batch 1-5 voice-gate rulings - follow them).
BEFORE writing any editorial notes, read a sample of ch07/ch08's editorial notes
in notes.json (they ARE the note voice to match) and the final two pages of
ch08's English (out/ch08_reading.md) - that prose IS the register the notes sit
against.

Do Batch 6 = ch09 "The Conspiracy of Silence" (PDF 155-172, printed 132-149),
ch10 "The Coup of April 12, 1927" (PDF 173-182, printed 150-159), and ch11
"Wuhan: The Revolutionary Center" (PDF 183-196, printed 160-173), end to end per
the pipeline ch01-08 established:

1. FIRST run ./setup.sh, THEN `sudo apt-get install -y -qq wamerican wbritish`
   (setup.sh does NOT install the English wordlists extract_isaacs.py needs for
   de-hyphenation - it installs Chinese OCR packs the extractor never uses).
   Confirm /usr/share/dict/american-english exists. Expect a possible stray
   per-task branch and a stale working tree at the top: `git fetch origin
   claude/tragedy-of-the-chinese-revolution` and hard-reset onto it if HEAD is
   not at the real tip (B04 and B05 containers were both parked on
   template-master).
2. Extract each unit VERBATIM: `python3 scripts/extract_isaacs.py ch09` etc.
   (body offset 23; folios come out arabic 132.., 150.., 160..). REVIEW the
   de-hyphenation report AND eyeball for real compound hyphens broken at a line
   end (the "war-weary" class: a hyphen at a line break whose closed form is a
   non-word is a HARD hyphen - keep it; B05 restored breaking-point,
   liberal-reform, eighty-two this way), which check_fidelity cannot catch.
   Then `python3 scripts/check_fidelity.py ch09 ch10 ch11` and confirm BOTH
   streams IDENTICAL. Also scan each reading file for a paragraph ending
   mid-sentence OR with a full-width line before a body (not {q}) paragraph - a
   residual spurious split (a mid-sentence end that precedes a {q} block is a
   normal quote intro, fine) - and for born-digital glitches (stray
   hyphen/tilde; render to plain sense and LOG in PROGRESS).
3. AUTHOR notes (arabic): `dump_anchors.py`, `anchor_offsets.py`, then
   `dump_endnotes.py`. Endnote headings: "9. The Conspiracy of Silence" begins
   PDF 375, "10. The Coup of April 12, 1927" PDF 377; find the ch11 heading and
   the ranges (the next chapter heading closes each range). Assemble on the
   build_ch0608_notes.py pattern, which numbers author notes POSITIONALLY (by
   the in-text mark, not the printed back-matter label). WATCH for source quirks
   in the back matter like ch06's (endnote 14 printed "14" with no period - the
   label regex now tolerates a missing period; verify the parsed labels come out
   a perfectly sequential 1..N run). Isaacs's ** on a page = the SECOND foot
   footnote (anchor_offsets now collapses a run of asterisks into one mark - do
   not revert). Transcribe asterisk foot footnotes by hand with <i>, dropping
   any stray trailing glyph.
4. EDITORIAL notes (roman, "ed": true) on the build_ch0608_editorial.py pattern,
   per CLAUDE.md's generous density model AND the STYLE.local rulings (marker ON
   the term; verdict tag ONLY where a claim is weighed; one subject one note; a
   note is never vaguer than its text AND never restates the body or its irony;
   no competing translation of a term the body renders; a significance/"first"
   claim must be grammatical and scoped; identify a quoted eyewitness by
   placement and stop; consistent pinyin gloss; no re-noting a subject an
   earlier-reading unit already covers). GREP notes.json and the earlier reading
   files first; keep a "NOT re-noted" list in PROGRESS. New first-appearance
   subjects to expect: the April 12 1927 Shanghai coup and massacre and its
   machinery (the gangster "Workers' Trade Alliance," Chou En-lai's near-
   execution), the Wuhan "Left" government at work, T. V. Soong, Sun Fo, the
   split between Wuhan and Nanking, the Fifth CCP Congress (late April 1927),
   M. N. Roy, more Comintern figures (the Eighth ECCI Plenum, May 1927). Fact-
   check against real scholarship, verdict where checkable. NEVER cite
   Grok/Grokipedia. Cite ARABIC printed folios in body notes.
5. Glossary: add new people/terms DIRECTLY INTO THEIR SECTION with a small
   script like add_ch0608_glossary.py (NOT apparatus_merge - it flattens the
   sectioned glossary). Consult authority.json for shelf agreement; principals
   are Sun 1, Chiang 2, Chen Tu-hsiu 3, Borodin 4, Wang Ching-wei 5 - consider
   promoting Chow En-lai (Zhou Enlai) or Chiu Chiu-pei (Qu Qiubai) if the
   narrative keeps turning on them.
6. Build (build_reading_epub.py); qa_epub AND epubcheck BOTH clean (jar at
   /tmp/epubcheck-5.1.0/epubcheck.jar; refetch per setup.sh if the container is
   fresh), check_apparatus clean, check_fidelity green on ALL units. Run the
   Step 0c blind-critique loop on at least one unit; evolve STYLE.local.md.
7. Deliver the built EPUB in chat as an attached file (stamp a chat copy with
   `python3 scripts/stamp_deliverable.py B06`) and PASTE the next kickoff
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
  extraction, author-note anchor tooling, the chapter-numeral fidelity fix.
- **B04 (ch04 + ch05): COMPLETE.** ch04 47, ch05 69 notes. 19 glossary rows.
  Fixed the spurious mid-page paragraph-split extractor bug.
- **B05 (ch06 "From Canton to the Yangtze" + ch07 "The Shanghai Insurrection" +
  ch08 "The Prodigal's Return"): COMPLETE.** ch06 54 notes (44 author + 10
  editorial), ch07 29 (21 + 8), ch08 54 (47 + 7); 137 notes this batch. 18
  glossary rows (16 people + 2 orgs). Wang Ching-wei promoted to principal 5.
  Two extractor/note-tooling fixes (consecutive-asterisk collapse; optional-
  period endnote label). Step 0c ran 2 rounds on ch06, convergent. Full record
  in PROGRESS.md.
- Cumulative build: **10 of 22 chapters, 524 notes, 146 pagebreaks, 0.3 MB.**
- 9 chapters remain (ch09-ch20).

## Tooling in place (DO NOT REVERT)

- **scripts/extract_isaacs.py**: faithful-reset extractor; per-unit offset from
  book.json (23 body, 1 front matter); de-hyphenation; drop-cap fold; furniture
  strip; superscript-ref removal; asterisk-footnote capture; block-quote
  capture ({q}); gap-ratio merge of spurious mid-page paragraph splits (B04);
  pagemap. BLIND SPOTS still hand-fixed and re-verified with check_fidelity: a
  real compound hyphen broken at a line end (the "war-weary" class -
  check_fidelity strips hyphens; a hyphen at a line break whose closed form is a
  non-word is a HARD hyphen and stays); a born-digital stray-glyph glitch
  (render to plain sense, log it).
- **scripts/check_fidelity.py**: whole-unit letters+digits fidelity gate; keeps
  block-quote spans, excludes the 100pt chapter numeral. Run on every chapter.
  CANNOT see paragraph structure, hyphens, or stray punctuation - hence the
  hand checks above.
- **scripts/dump_anchors.py + scripts/anchor_offsets.py**: resolve every in-text
  reference mark to a unique verbatim anchor. B04 additions: italic-run anchor
  fallback + closing-`*` absorb. **B05 addition (do not revert): collapse a run
  of consecutive asterisks into ONE mark** - Isaacs's `**` is the SECOND
  page-foot footnote symbol on a page (ch06 p.98 had `*`=Voitinsky and
  `**`=Mandalyan), and the old code counted `**` as two marks and the resolver
  died on the duplicate. Consecutive 'ast' marks with identical preceding prose
  are merged; two distinct footnotes always have intervening prose. Verified
  ch04/ch05 regenerate byte-identical.
- **scripts/build_ch0608_notes.py**: author-note assembler; numbers author notes
  POSITIONALLY (by in-text mark, not the printed back-matter label), robust to
  Isaacs's back-matter misnumbering. **B05 addition (do not revert): the note-
  label regex tolerates a MISSING trailing period** (ch06 endnote 14 is printed
  "14" with no period; every other label has one), plus a matching label
  pre-strip - verified the relaxed regex still yields a sequential 1..N run so
  no wrapped continuation is misread as a label. (build_ch0405_*, build_ch0203_*,
  build_ch01_* remain as templates.)
- **scripts/build_reading_epub.py**: `edition_kind: "annotated"` chrome; `{q} `
  block quotes; TWO-STREAM per-chapter note numbering (author arabic n-<unit>-N
  / editorial roman en-<unit>-r, both restart each chapter); markers ordered by
  ANCHOR-END position; an anchor may include `*` italic markers.
- **GLOSSARY IS SECTIONED (trap).** glossary.json has people/organizations/
  places/terms sections (each a dict keyed by hanzi). apparatus_merge.py
  flattens it and breaks the build; add glossary rows STRAIGHT INTO their
  section (a small script like add_ch0608_glossary.py). Notes and figures merge
  through apparatus_merge fine.
- **review/voice_gate_critic_prompt_annotation.md** + voice_gate_critique.py is
  edition-aware. epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/.

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles (or conventional English) forms STAY in the
  body; pinyin + hanzi go in the glossary and the first-appearance editorial
  note. One form per referent; check authority.json. Isaacs's own spellings
  this batch: "Chow En-lai" (not Chou), "Chiu Chiu-pei", "Sun Chuang-fang" (not
  Chuan-fang), "Tang Ping-shan", "Chang Tsung-chang", "Pai Chung-hsi", "Ho
  Ying-chin", "Tsai Yuan-pei", "Tu Yueh-sen", "Hwang Ching-yung".
- Note architecture: author notes arabic, editorial roman, per-chapter restart,
  NO "Ed." prefix. ALL of Isaacs's own notes (numbered endnotes AND asterisks)
  go in the arabic stream, numbered by POSITION.
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American
  English in editorial prose; dates "Month D, YYYY".
- Editorial-note voice (with the B01-B05 refinements in STYLE.local): concise,
  factual; who/what/when + why-it-matters-here; verdict tag ONLY on a weighed
  claim; marker ON the glossed term; a note never vaguer than its text and never
  restating the body's own point/irony; no competing translation of a term the
  body renders; a significance/"first" claim grammatical and scoped; a quoted
  eyewitness identified by placement, no trivia; pinyin gloss applied
  consistently; no meta-filler.
- Principals (Principal Characters page): Sun Yat-sen (1), Chiang Kai-shek (2),
  Chen Tu-hsiu (3), Borodin (4), Wang Ching-wei (5, promoted B05). Chow En-lai
  (Zhou Enlai) and Chiu Chiu-pei (Qu Qiubai) are the next candidates as the
  Shanghai insurrection and its aftermath move to the center.

## Where the book stands

- Front matter frames the book; ch01-03 give the background and 1919-25
  narrative; ch04-05 the Canton power struggle and Chiang's March 20, 1926 coup.
  ch06-08 carry the Northern Expedition north to the Yangtze (July 1926 on),
  the Comintern's Seventh-Plenum policy of binding the Communists to the
  Kuomintang, the two Shanghai risings (the failed February 1927 rising and the
  victorious March 21 insurrection led by Chou En-lai), and Chiang's arrival at
  Shanghai in late March 1927 - the prodigal back among the Green Gang bosses
  and Chekiang bankers, buying time, financing, and gangster "unions" for the
  purge now one chapter away. ch09-11 turn to the "conspiracy of silence" that
  disarmed the workers, the April 12 coup and massacre, and the Wuhan "Left"
  government.

## What is NEXT (grouping calibrated on Batches 1-5)

- B06 = ch09-10-11. Then, tuned as later chapters prove lighter: B07 = ch12-13-14;
  B08 = ch15-16-17; B09 = ch18-19-20.
- The FINAL batch stays light on chapters: it builds the LINKED index from all
  the per-chapter pagemaps (book.json _index_decision), does the whole-book
  reconciliation sweep (check 12), renders out/term_ledger.md, writes
  COMPLETION.md, and commits the final EPUB itself.

## Open items / cross-unit overlaps for the final reconciliation sweep

- Body offset is 23 (printed = PDF page - 23); front matter was 1. Cite ARABIC
  folios in body-chapter notes.
- Cross-unit overlaps the blind critic keeps flagging as "undefined" (Borodin,
  Voitinsky, Wu Pei-fu, Chen Tu-hsiu, Chang Tso-lin, Sun Yat-sen, the
  Kuomintang, the Comintern, Wang Ching-wei, May Thirtieth, hsien, compradore,
  the Washington Conference): the documented false positive, noted at first
  appearance in an earlier-reading unit. The sweep confirms or trims.
- Source misprints kept visible: the Feb 7 1923 massacre toll (ch03); ch04
  "whole interests"; ch05 back-matter endnotes misnumbered "18, 18, 20"; ch06
  back-matter endnote 14 printed "14" (no period). Malraux's novel spelled both
  "Man's Fate" (ch07 endnote) and "Mans' Fate" (ch07 asterisk footnote), kept as
  printed. Digitization glitches (ch04 "in the- masses", ch05 "'overthrown'~")
  rendered to plain sense and logged; none this batch.
- Green Gang: the ch04 note glosses the bosses as "Huang Chin-jung" / "Tu
  Yueh-sheng"; the B05 glossary rows use Isaacs's body forms "Hwang Ching-yung"
  / "Tu Yueh-sen" with pinyin Huang Jinrong / Du Yuesheng. The reconciliation
  sweep should confirm the reader can bridge these.

## Environment / traps state

- Container is reprovisioned fresh each session. setup.sh installs pymupdf,
  pillow, epubcheck 5.1.0 AND (uselessly) Chinese tesseract packs, but NOT the
  English wordlists extract_isaacs.py needs - install wamerican/wbritish by hand
  (kickoff step 1). No OCR needed. Build is text-only, ~0.3 MB.
- tests/run_tests.py "hook stands down on template stub" FAILS by design; do not
  "fix" it.
- Stray-branch / stale-tree check every batch (working branch
  claude/tragedy-of-the-chinese-revolution). B05's container had the tree parked
  on template-master (df55427); fetched and hard-reset onto the real tip.
