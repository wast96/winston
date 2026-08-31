# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat alongside the attached EPUB. Writing it here alone does not
count.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B08

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). NOT a translation: source.pdf (repo root) has a clean born-digital
text layer, so there is no OCR and nothing to translate. The work is annotation
and faithful resetting. Batches 1-7 (front matter + ch01-14) are done and set
the whole machinery; you are extending it, not inventing it.

Read, in order: CLAUDE.md, then HANDOFF.md (full source characterization and the
do-not-revert tooling list), then book.json, then STYLE.local.md (the whole
style contract; it carries the Batch 1-7 voice-gate rulings - follow them).
BEFORE writing any editorial notes, read a sample of ch12/ch13/ch14's editorial
notes in notes.json (they ARE the note voice to match) and the final two pages
of ch14's English (out/ch14_reading.md) - that prose IS the register the notes
sit against.

Do Batch 8 = ch15 "The Wuhan Debacle" (PDF 250-268, printed 227-245), ch16
"Autumn Harvest" (PDF 269-283, printed 246-260), and ch17 "The Canton Commune"
(PDF 284-302, printed 261-279), end to end per the pipeline ch01-14 established:

1. FIRST run ./setup.sh, THEN `sudo apt-get install -y -qq wamerican wbritish`
   (setup.sh does NOT install the English wordlists extract_isaacs.py needs for
   de-hyphenation - it installs Chinese OCR packs the extractor never uses).
   Confirm /usr/share/dict/american-english exists. Expect a stray per-task
   branch and a stale working tree at the top: `git fetch origin
   claude/tragedy-of-the-chinese-revolution` and hard-reset onto it if HEAD is
   not at the real tip (every container so far has been parked on
   template-master df55427). Only the by-design test "hook stands down on
   template stub" fails; do not fix it.
2. Extract each unit VERBATIM: `python3 scripts/extract_isaacs.py ch15` etc.
   (body offset 23; folios come out arabic 227.., 246.., 261..). REVIEW the
   de-hyphenation report AND eyeball for real compound hyphens broken at a line
   end (the "war-weary" class: a hyphen at a line break whose closed form is a
   non-word is a HARD hyphen - keep it). Then `python3 scripts/check_fidelity.py
   ch15 ch16 ch17` and confirm all green. Also scan each reading file for a
   paragraph ending mid-sentence OR starting mid-word (a residual spurious split;
   a mid-sentence end that precedes a {q} block is a normal quote intro, fine),
   and for born-digital glitches (a dropped hyphen in a WG NAME rendered closed
   mid-line, like B07's "Tuhsiu"/"Chiupei"; a stray hyphen/tilde; a C0 control
   char like the NUL that hit ch10). Render name-hyphen glitches to plain sense
   and LOG in PROGRESS; restore_hyphens in the notes builder already maps the
   known ones (Kaishek, Chiupei).
3. AUTHOR notes (arabic): `dump_anchors.py`, `anchor_offsets.py`, then
   `dump_endnotes.py`. Endnote back-matter headings begin: "15. Wuhan: The
   Debacle" PDF 385, "16. Autumn Harvest" PDF 387, "17. The Canton Commune" PDF
   389 (the next chapter heading closes each range: ch15 385-387, ch16 387-389,
   ch17 389-390). Assemble on the build_ch1214_notes.py pattern, which numbers
   author notes POSITIONALLY. WATCH the numbered-mark vs back-matter-note count:
   B07's ch13 had a SOURCE error (65 in-text marks, 64 notes -- the same "64"
   superscript printed twice on one Min Kuo Jih Pao passage), and the positional
   mapper now ALLOWS duplicate mark values as long as every body index 1..N is
   covered -- do not revert. WATCH multi-block asterisk footnotes: a long
   page-foot note that wraps a page turn or carries "Again:" quotations is ONE
   note across several foot blocks (ch14 grouped [6,1,1,5] via AST_GROUP); count
   the actual footnotes (leading */**/***) vs the foot blocks. For each
   asterisk, crop-verify by eye where its mark sits (B06 hit two whose in-text
   mark is absent from the text layer); read the foot body programmatically and
   reduce-check it against the raw foot text. Isaacs's ** on a page = the SECOND
   foot footnote (anchor_offsets collapses a run of asterisks into one mark - do
   not revert). Transcribe asterisk foot footnotes with <i>.
4. EDITORIAL notes (roman, "ed": true) on the build_ch1214_editorial.py pattern,
   per CLAUDE.md's generous density model AND the STYLE.local rulings (marker ON
   the term; verdict tag ONLY where a claim is weighed; one subject one note; a
   note never vaguer than its text AND never restating the body, the author's
   own citation, or its irony; no competing translation of a term the body
   renders; a significance/"first" claim grammatical and scoped; identify a
   quoted eyewitness by placement PLUS vantage, minus both duplications; a
   book-specific proper name takes the body's own capitalization; a note that
   gives the "correct" form of a quotation the body prints in a variant must
   ACKNOWLEDGE the variance not silently contradict; a place named in a note
   must match the body's or be reconciled; read each note's dash-tail as a
   standalone sentence; consistent pinyin gloss; no re-noting a subject an
   earlier-reading unit already covers). GREP notes.json for an actual EDITORIAL
   ("ed":true) note before treating a flagged subject as a cross-unit false
   positive -- a figure who appears only in author-note CITATIONS is NOT placed
   (B07 found Louis Fischer had been wrongly listed as "placed" for four
   batches; his note was added at his first appearance, ch05). Keep a "NOT
   re-noted" list in PROGRESS. New first-appearance subjects to expect: Feng
   Yu-hsiang's Chengchow (June 10-12) and Hsuchow (Xuzhou, June 19-21)
   conferences and his defection/ultimatum to Wuhan; the July 15 1927 Wuhan
   split (Wang Ching-wei's final break with the Communists); the August 7
   Emergency Conference (the "August 7 Letter" cited in ch13's notes) at which
   Chiu Chiu-pei succeeds Chen Tu-hsiu; the Nanchang uprising (Aug 1 1927); the
   Autumn Harvest uprising (Mao); the Canton Commune (Dec 11-13 1927) and its
   cast (Heinz Neumann, Chang Tai-lei, Yeh Ting and Yeh Ting's/Ho Lung's forces,
   Vissarion Lominadze). Fact-check against real scholarship, verdict where
   checkable. NEVER cite Grok/Grokipedia. Cite ARABIC printed folios in body notes.
5. Glossary: add new people/terms DIRECTLY INTO THEIR SECTION with a small
   script like add_ch1214_glossary.py (NOT apparatus_merge - it flattens the
   sectioned glossary). Consult authority.json for shelf agreement; principals
   are Sun 1, Chiang 2, Chen Tu-hsiu 3, Borodin 4, Wang Ching-wei 5, Chow En-lai
   6. PROMOTE Chiu Chiu-pei (Qu Qiubai) to principal (cast_order 7) in ch16
   region: he succeeds Chen Tu-hsiu at the head of the party at the August 7
   1927 conference (his glossary row 瞿秋白 already records this; set principal:
   true, cast, cast_order 7).
6. Build (build_reading_epub.py); qa_epub AND epubcheck BOTH clean (jar at
   /tmp/epubcheck-5.1.0/epubcheck.jar; refetch per setup.sh if the container is
   fresh), check_apparatus clean, check_fidelity green on ALL units. Run the
   Step 0c blind-critique loop on at least one unit; evolve STYLE.local.md.
7. Deliver the built EPUB in chat as an attached file (stamp a chat copy with
   `python3 scripts/stamp_deliverable.py B08`) and PASTE the next kickoff
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
- **B04 (ch04 + ch05): COMPLETE.** ch04 47, ch05 69 notes (now 70, +Fischer). 19
  glossary rows.
- **B05 (ch06 + ch07 + ch08): COMPLETE.** ch06 54, ch07 29, ch08 54 notes. 18
  glossary rows. Wang Ching-wei promoted to principal 5.
- **B06 (ch09 + ch10 + ch11): COMPLETE.** ch09 61, ch10 48, ch11 35 notes. 5
  glossary rows. Chow En-lai promoted to principal 6.
- **B07 (ch12 "The 'Revolutionary Center' at Work" + ch13 "The Struggle for the
  Land" + ch14 "Moscow and Wuhan"): COMPLETE.** ch12 74 notes (63 author + 11
  editorial), ch13 77 (71 + 6), ch14 54 (49 + 5); plus 1 gap-fix editorial note
  in ch05 (Louis Fischer). 8 glossary rows. Three note-tooling additions (dup
  mark-value tolerance for ch13's double "64"; AST_GROUP multi-block asterisk
  grouping for ch14; Chiupei hyphen restore). Step 0c ran 2 rounds on ch12,
  convergent. Full record in PROGRESS.md.
- Cumulative build: **16 of 22 chapters, 874 notes, 238 pagebreaks, 0.4 MB.**
- 6 chapters remain (ch15-ch20).

## Tooling in place (DO NOT REVERT)

- **scripts/extract_isaacs.py**: faithful-reset extractor; per-unit offset from
  book.json (23 body, 1 front matter); de-hyphenation; drop-cap fold; furniture
  strip; superscript-ref removal; asterisk-footnote capture; block-quote
  capture ({q}); gap-ratio merge of spurious mid-page paragraph splits (B04);
  pagemap. BLIND SPOTS still hand-fixed and re-verified with check_fidelity: a
  real compound hyphen broken at a line end (the "war-weary" class); a
  born-digital dropped hyphen in a WG NAME printed closed mid-line (B07's
  "Tuhsiu"->"Tu-hsiu"); a stray-glyph or control-char glitch (render to plain
  sense, log it).
- **scripts/check_fidelity.py**: whole-unit letters+digits fidelity gate. B06
  addition (do not revert): a body-DOMINANT block emits all its spans, so an
  inline sub-body small-caps span survives. CANNOT see paragraph structure,
  hyphens, or stray punctuation - hence the hand checks above.
- **scripts/dump_anchors.py + scripts/anchor_offsets.py**: resolve in-text marks
  to unique verbatim anchors. B04: italic-run fallback + closing-`*` absorb. B05:
  collapse a run of consecutive asterisks into ONE mark (`**` = the SECOND
  page-foot footnote). B06: skip the single letter of a "{q} "/"{v} " block
  marker when reducing the reading stream.
- **scripts/build_ch1214_notes.py** (B07, the current author-note template):
  positional numbering that ALLOWS duplicate in-text mark values (ch13's double
  "64" -- asserts only that every back-matter body index 1..N is cited);
  per-unit AST_GROUP grouping for multi-block asterisk footnotes (a long note
  that wraps a page turn or carries the author's own "Again:" quotations is ONE
  note across several foot blocks; ch14 = [6,1,1,5]); programmatic foot-body
  reading with a reduce drift-check; restore_hyphens maps "Kaishek"->"Kai-shek"
  AND "Chiupei"->"Chiu-pei" and strips C0 control chars. The earlier
  build_ch0911_notes.py / build_ch0608_notes.py remain valid templates for a
  batch whose marks all survive and are 1-per-body.
- **scripts/build_reading_epub.py**: `edition_kind: "annotated"` chrome; `{q} `
  block quotes; TWO-STREAM per-chapter note numbering (author arabic / editorial
  roman, both restart each chapter); markers ordered by ANCHOR-END position; an
  anchor may include `*` italic markers. REFUSES a build on an unmatched note
  anchor or unplaced figure spec.
- **GLOSSARY IS SECTIONED (trap).** glossary.json has people/organizations/
  places/terms sections (each a dict keyed by hanzi). apparatus_merge flattens
  it and breaks the build; add glossary rows STRAIGHT INTO their section (a
  small script like add_ch1214_glossary.py). Notes and figures merge through
  apparatus_merge fine.
- **review/voice_gate_critic_prompt_annotation.md** + voice_gate_critique.py is
  edition-aware. epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/.

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles (or conventional English) forms STAY in the
  body; pinyin + hanzi go in the glossary and the first-appearance editorial
  note. One form per referent; check authority.json. Isaacs's own spellings this
  batch: "Tan Yen-kai", "Yen Hsi-shan", "Hsiang Chung-fah", "Yeh Ting", "Hsu
  Keh-chang", "Ho Chien", "Hsu Chao-jen", "Chu Pei-teh", and "Hsu Chien" (=
  George Hsu-chien / Xu Qian, noted ch11 -- the final sweep should confirm the
  reader bridges "Hsu Chien" to "George Hsu-chien").
- Note architecture: author notes arabic, editorial roman, per-chapter restart,
  NO "Ed." prefix. ALL of Isaacs's own notes (numbered endnotes AND asterisks)
  go in the arabic stream, numbered by POSITION -- so the edition's arabic
  numbers are its OWN sequence, and a source double-numbering (ch13's two "64"
  marks) simply becomes two consecutive edition markers on the same body.
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American
  English in editorial prose; dates "Month D, YYYY". A book-specific proper name
  takes the body's own capitalization in the notes.
- Editorial-note voice (with the B01-B07 refinements in STYLE.local): concise,
  factual; who/what/when + why-it-matters-here; verdict tag ONLY on a weighed
  claim; marker ON the glossed term; a note never vaguer than its text and never
  restating the body, the adjacent author citation, or the body's own irony; a
  quoted eyewitness gets placement PLUS vantage; a significance/"first" claim
  grammatical and scoped; a note's version of a quotation the body gives loosely
  is framed as "echoes"/"remembered as," never a silent correction; a place in
  a note matches the body's place; each note's dash-tail reads as a standalone
  grammatical sentence; pinyin gloss applied consistently.
- Principals (Principal Characters page): Sun Yat-sen (1), Chiang Kai-shek (2),
  Chen Tu-hsiu (3), Borodin (4), Wang Ching-wei (5), Chow En-lai (6). Chiu
  Chiu-pei (Qu Qiubai) is DUE for promotion to principal 7 in B08/ch16, when he
  succeeds Chen at the August 7 1927 conference (his glossary row already
  records the succession).

## Where the book stands

- Front matter frames the book; ch01-03 background and 1919-25; ch04-05 the
  Canton power struggle and Chiang's March 20 1926 coup; ch06-08 the Northern
  Expedition to the Yangtze and the two Shanghai risings; ch09-11 the disarming
  of the Shanghai workers, Chiang's April 12 coup, and the opening of the Wuhan
  act. ch12-14 (this batch): the Wuhan "revolutionary center" AT WORK -- its
  capitulation to the bourgeoisie and the imperialist powers after Chiang's
  coup, the Fifth CCP Congress's evasion of the land question; the peasant
  revolt in Hunan/Hupeh and its bloody suppression (the May 21 Horse Day
  Incident at Changsha, Hsu Keh-chang, Ho Chien); and the Eighth ECCI Plenum in
  Moscow (Stalin vs. Trotsky on soviets), Stalin's June 1 telegram (which Roy
  showed Wang Ching-wei), and the Communists' paralysis -- ending as the
  Comintern's last "possibility" narrows to Feng Yu-hsiang. ch15-17 turn to the
  Wuhan debacle (Feng's defection, the July 15 split), the August 7 conference
  and the Autumn Harvest risings, and the Canton Commune.

## What is NEXT (grouping calibrated on Batches 1-7)

- B08 = ch15-16-17. Then B09 = ch18-19-20 (the final batch).
- The FINAL batch (B09) stays light on chapters: it builds the LINKED index from
  all the per-chapter pagemaps (book.json _index_decision), does the whole-book
  reconciliation sweep (check 12), renders out/term_ledger.md, writes
  COMPLETION.md, updates authority.json with this book's decided renderings, and
  commits the final EPUB itself (`git add -f`).

## Open items / cross-unit overlaps for the final reconciliation sweep

- Body offset is 23 (printed = PDF page - 23); front matter was 1. Cite ARABIC
  folios in body-chapter notes.
- **NEW-TO-SHELF renderings to add to authority.json on the final batch:**
  向忠发 Xiang Zhongfa (Hsiang Chung-fah), 许克祥 Xu Kexiang (Hsu Keh-chang),
  何键 He Jian (Ho Chien), 苏兆征 Su Zhaozheng (Hsu Chao-jen), 朱培德 Zhu Peide
  (Chu Pei-teh). (谭延闿/阎锡山/叶挺 were already "agreed"; ch09-11's 徐谦 Xu Qian
  was flagged for the same.)
- **Louis Fischer** now has his editorial note at first appearance (ch05); the
  sweep should confirm no later unit needs a duplicate. His name appears
  ch05/ch11/ch12.
- **Wuhan as a tri-city:** the Fifth Congress note (ch12) folds in "Hankow, one
  of the three cities that make up Wuhan," but the sweep should confirm the
  reader learns early (ch06/ch11 region) that Wuhan = Wuchang + Hankow + Hanyang;
  it may want a dedicated first-appearance gloss.
- **"Hsu Chien" vs "George Hsu-chien":** ch12 body uses "Hsu Chien"; ch11 noted
  him as "George Hsu-chien" (Xu Qian). Confirm the reader bridges them.
- Cross-unit overlaps the blind critic keeps flagging as "undefined" (Fischer,
  Mif, Browder, Chiu Chiu-pei, Wang Ching-wei, Borodin, Feng Yu-hsiang, etc.):
  each noted at first appearance in an earlier-reading unit -- the documented
  false positive. Fischer was the exception (a real gap, now fixed). Before
  skipping one, grep notes.json for an actual EDITORIAL note, not any mention.
- Source quirks kept visible (this batch): ch13's duplicate in-text "64"
  (rendered as edition markers 64 and 65, both citing Min Kuo Jih Pao); ch14
  "against the people[!]" (Isaacs's own bracketed exclamation in a quoted
  telegram). Earlier quirks: ch05 misnumbered "18,18,20"; ch06 endnote "14" (no
  period); Malraux both "Man's Fate"/"Mans' Fate"; ch09 two-line signature; ch10
  "[sic]"/NUL byte; ch11 stray opening curly quote. Digitization name-hyphen
  glitches rendered to plain sense and logged: ch14 "Tuhsiu"->"Tu-hsiu",
  "Chiupei"->"Chiu-pei".

## Environment / traps state

- Container is reprovisioned fresh each session. setup.sh installs pymupdf,
  pillow, epubcheck 5.1.0 AND (uselessly) Chinese tesseract packs, but NOT the
  English wordlists extract_isaacs.py needs - install wamerican/wbritish by hand
  (kickoff step 1). No OCR needed. Build is text-only, ~0.4 MB.
- tests/run_tests.py "hook stands down on template stub" FAILS by design; do not
  "fix" it.
- Stray-branch / stale-tree check every batch (working branch
  claude/tragedy-of-the-chinese-revolution). B07's container was parked on
  template-master (df55427); fetched and hard-reset onto the real tip (1b9760c).
