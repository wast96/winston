# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

The baton. A fresh session with no memory reads this and starts immediately.
This book is an ANNOTATED ENGLISH EDITION, not a translation: the source is
already in English and the PDF has a clean text layer, so there is no OCR and
no translating. The kickoff below is the archive copy; every batch also PASTES
it into the chat alongside the attached EPUB. Writing it here alone does not
count.

## Message to paste into the next chat

```
Tragedy of the Chinese Revolution B09 (FINAL batch)

This is an ANNOTATED ENGLISH EDITION of Harold Isaacs, "The Tragedy of the
Chinese Revolution" (Haymarket 2009 reprint of the Secker & Warburg 1938 first
edition). NOT a translation: source.pdf (repo root) has a clean born-digital
text layer, so there is no OCR and nothing to translate. Batches 1-8 (front
matter + ch01-17, 1067 notes) are done and set the whole machinery; you are
finishing the book.

Read, in order: CLAUDE.md, then HANDOFF.md (full source characterization and the
do-not-revert tooling list), then book.json, then STYLE.local.md (the whole
style contract; it carries the Batch 1-8 voice-gate rulings - follow them).
BEFORE writing any editorial notes, read a sample of ch15/ch16/ch17's editorial
notes in notes.json (they ARE the note voice to match) and the final two pages
of ch17's English (out/ch17_reading.md).

This is the LAST batch: it stays light on chapters and carries the whole-book
close-out. Do the three remaining chapters AND the final-batch work.

1. SETUP: FIRST run ./setup.sh, THEN `sudo apt-get install -y -qq wamerican
   wbritish` (setup.sh installs Chinese OCR packs the extractor never uses, NOT
   the English wordlists extract_isaacs.py needs). Confirm
   /usr/share/dict/american-english exists. Expect a stray per-task branch / a
   stale tree parked on template-master df55427: `git fetch origin
   claude/tragedy-of-the-chinese-revolution` and hard-reset onto the real tip.
   Only the by-design test "hook stands down on template stub" fails; do not fix.
2. CHAPTERS: ch18 "Fruits of Defeat" (PDF 303-316, printed 280-293), ch19 "The
   Rise and Fall of 'Soviet China'" (PDF 317-338, printed 294-315), ch20 "The
   New 'National United Front'" (PDF 339-361, printed 316-338), end to end per
   the pipeline. `extract_isaacs.py ch18` etc. (offset 23; folios arabic 280..,
   294.., 316..). REVIEW the de-hyphenation report AND eyeball for the "war-weary"
   hard-hyphen class (a hyphen at a line break whose closed form is a non-word;
   B08 hit "midwifein-chief" -> "midwife-in-chief") and for born-digital glitches
   (a dropped hyphen in a WG NAME rendered closed mid-line; a stray '*' text-layer
   glyph that is NOT a footnote mark, like B08's "GPU*" -- crop-verify against the
   page image; a stray hyphen/tilde; a C0 control char). Then
   `check_fidelity.py ch18 ch19 ch20` green, and scan each reading file for a
   paragraph ending mid-sentence (a mid-sentence end before a {q} block is a
   normal quote intro) or starting mid-word.
3. AUTHOR notes (arabic): dump_anchors.py, anchor_offsets.py, dump_endnotes.py;
   assemble on the build_ch1517_notes.py pattern (positional numbering; AST_SKIP
   for a stray-glyph mark; per-unit AST_GROUP for multi-block asterisk footnotes;
   fix_italic_space for the space clean_body drops after "</i>"+word). The ch18-20
   endnote back-matter headings follow ch17's ("17. The Canton Commune" ended PDF
   390): find "18. Fruits of Defeat", "19. ...Soviet China", "20. ...United
   Front" (each range closed by the next heading; the index begins printed 374 /
   PDF ~397). WATCH numbered-mark vs back-matter-note counts (a source
   double-mark, like ch13's, is tolerated by the positional mapper); count actual
   footnotes (leading */**/***) vs foot blocks and crop-verify each asterisk's
   mark by eye.
4. EDITORIAL notes (roman, "ed": true) on the build_ch1517_editorial.py pattern,
   per CLAUDE.md's generous density AND the STYLE.local rulings. GREP notes.json
   for an actual EDITORIAL ("ed":true) note before treating a flagged subject as
   a cross-unit false positive. Keep a "NOT re-noted" list. Fact-check against
   real scholarship, verdict ONLY where a claim is weighed; NEVER Grok/Grokipedia.
   Cite ARABIC printed folios in body notes. Expect first-appearance subjects in
   the aftermath: the Kiangsi/Jiangxi soviets and the Chinese Soviet Republic
   (Juichin/Ruijin, 1931), the Long March, the Fukien/Fujian rebellion (1933-34),
   the Second United Front and the Sian Incident (Dec 1936, Chang Hsueh-liang
   already noted ch15), the Japanese invasion (Mukden 1931, the 1937 war).
5. GLOSSARY: add new people/terms DIRECTLY INTO THEIR SECTION with a small
   add_ch1820_glossary.py (NOT apparatus_merge - it flattens the sectioned
   glossary). Consult authority.json. Principals are Sun 1, Chiang 2, Chen Tu-hsiu
   3, Borodin 4, Wang Ching-wei 5, Chow En-lai 6, Chiu Chiu-pei 7 (no further
   promotion expected; Mao is noted ch00a but Isaacs's book, ending in 1938, never
   makes him its central figure - use judgement).
6. FINAL-BATCH CLOSE-OUT (the reason this batch is light on chapters):
   - The LINKED INDEX (book.json _index_decision): parse the printed index (printed
     374 to end) and render it as a back-matter Index page whose every folio
     reference links to the pg-<unit>-<folio> anchors the pagemaps emit; 'see/see
     also' cross-refs linked to the target entry. Needs anchors from ALL chapters.
   - Whole-book RECONCILIATION sweep (check 12): run check_reconcile.py; a HUMAN
     read of its drift candidates (some variation is legitimate). Confirm the
     "Hsu Chien"/"George Hsu-chien" bridge, the Wuhan tri-city gloss, one spelling
     locale, notes at FIRST appearance.
   - authority.json: add this book's NEW-TO-SHELF decided renderings -- 向忠发
     Xiang Zhongfa, 许克祥 Xu Kexiang, 何键 He Jian, 苏兆征 Su Zhaozheng, 朱培德 Zhu
     Peide (B07), 张太雷 Zhang Tailei (B08), plus any new ch18-20 names.
   - render out/term_ledger.md; out/deep_audit.md (the 3-5% random-sample audit,
     fixed seed, honest error rate); write COMPLETION.md from the template (NOT
     another handoff); do NOT modify the kickoff section afterward (the Stop hook
     would demand a block that no longer exists).
   - CORRECTIONS-PASS candidates to note in COMPLETION (latent, book-wide, do NOT
     retrofit into shipped units mid-close unless cheap): (a) the clean_body lost
     space after "</i>"+word in earlier batches' author-note citations
     ("News,</i>April 13") -- B08 fixed it for ch15-17 via fix_italic_space and
     logged the rest; (b) "mow" got a book-wide glossary terms row in B08 but no
     first-appearance ch02 note.
   - COMMIT THE FINAL EPUB ITSELF: `git add -f out/<deliverable>` (branches
     outlive containers, chat attachments do not).
7. Build (build_reading_epub.py, now cleaned of pending-TOC scaffolding since the
   book is complete); qa_epub AND epubcheck BOTH clean (jar at
   /tmp/epubcheck-5.1.0/epubcheck.jar; refetch per setup.sh if fresh),
   check_apparatus clean, check_fidelity green on ALL units. Run the Step 0c blind
   loop on at least one unit; evolve STYLE.local.md.
8. Deliver the built EPUB in chat as an attached file (stamp a chat copy with
   `python3 scripts/stamp_deliverable.py B09`). Since this is the last batch there
   is no next kickoff to paste; instead say the book is COMPLETE and point to
   COMPLETION.md. Commit and push.

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
- **B04 (ch04 + ch05): COMPLETE.** ch04 47, ch05 70 notes (with Fischer). 19 rows.
- **B05 (ch06 + ch07 + ch08): COMPLETE.** ch06 54, ch07 29, ch08 54 notes. 18
  glossary rows. Wang Ching-wei promoted to principal 5.
- **B06 (ch09 + ch10 + ch11): COMPLETE.** ch09 61, ch10 48, ch11 35 notes. 5
  glossary rows. Chow En-lai promoted to principal 6.
- **B07 (ch12 + ch13 + ch14): COMPLETE.** ch12 74, ch13 77, ch14 54 notes; +1
  ch05 Fischer. 8 glossary rows.
- **B08 (ch15 "The Wuhan Debacle" + ch16 "Autumn Harvest" + ch17 "The Canton
  Commune"): COMPLETE.** ch15 70 notes (63 author + 7 editorial), ch16 57 (49 +
  8), ch17 66 (62 + 4). 5 glossary people rows + 1 terms row (mow); Chiu Chiu-pei
  (Qu Qiubai) promoted to principal 7. Two note-tooling additions (AST_SKIP for a
  stray-glyph '*' mark; fix_italic_space). Step 0c ran 2 rounds on ch16,
  convergent. Full record in PROGRESS.md.
- Cumulative build: **19 of 22 chapters, 1067 notes, 290 pagebreaks, 0.5 MB.**
- 3 chapters remain (ch18-ch20) plus the final-batch close-out (linked index,
  reconciliation sweep, term_ledger, COMPLETION.md, authority.json, commit the
  final EPUB).

## Tooling in place (DO NOT REVERT)

- **scripts/extract_isaacs.py**: faithful-reset extractor; per-unit offset from
  book.json (23 body, 1 front matter); de-hyphenation; drop-cap fold; furniture
  strip; superscript-ref removal; asterisk-footnote capture; block-quote
  capture ({q}); gap-ratio merge of spurious mid-page paragraph splits (B04);
  pagemap. BLIND SPOTS still hand-fixed and re-verified with check_fidelity: a
  real compound hyphen broken at a line end (the "war-weary" class -- B08 hit
  "midwifein-chief"->"midwife-in-chief"); a born-digital dropped hyphen in a WG
  NAME printed closed mid-line; a stray-glyph or control-char glitch (render to
  plain sense, log it); a stray '*' text-layer glyph that is NOT a footnote mark
  (B08's "GPU*", crop-verified -> AST_SKIP in the notes builder).
- **scripts/check_fidelity.py**: whole-unit letters+digits fidelity gate. CANNOT
  see paragraph structure, hyphens, or stray punctuation - hence the hand checks.
- **scripts/dump_anchors.py + scripts/anchor_offsets.py**: resolve in-text marks
  to unique verbatim anchors (italic-run fallback; closing-`*` absorb; collapse a
  run of asterisks into ONE mark; skip a {q}/{v} block-marker letter).
- **scripts/build_ch1517_notes.py** (B08, the current author-note template):
  positional numbering that allows duplicate in-text mark values; per-unit
  AST_GROUP for multi-block asterisk footnotes; AST_SKIP to drop a stray '*'
  text-layer glyph that is not a footnote mark (ch16 "GPU"); fix_italic_space to
  restore the space clean_body drops after "</i>"+word; restore_hyphens maps
  "Kaishek"/"Chiupei" and strips C0 control chars. The earlier build_ch1214/
  ch0911/ch0608 notes builders remain valid templates.
- **scripts/build_reading_epub.py**: `edition_kind: "annotated"` chrome; `{q} `
  block quotes; TWO-STREAM per-chapter note numbering (author arabic / editorial
  roman); markers ordered by ANCHOR-END position; an anchor may include `*`.
  REFUSES a build on an unmatched note anchor or unplaced figure spec.
- **GLOSSARY IS SECTIONED (trap).** glossary.json has people/organizations/
  places/terms sections (each a dict keyed by hanzi). apparatus_merge FLATTENS it
  and breaks the build; add glossary rows STRAIGHT INTO their section (a small
  add_ch<...>_glossary.py). Notes and figures merge through apparatus_merge fine.
- **review/voice_gate_critic_prompt_annotation.md** + voice_gate_critique.py is
  edition-aware. epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/.

## Renderings settled / carry-forward

- Name policy: Isaacs's Wade-Giles (or conventional English) forms STAY in the
  body; pinyin + hanzi go in the glossary and the first-appearance editorial
  note. One form per referent; check authority.json. B08's body forms: "Feng
  Yu-hsiang", "Chang Hsueh-liang", "Chang Fah-kwei", "Li Li-san", "Ho Lung",
  "Chang Tai-lei", "Chen Shao-yu" (= Wang Min, per Isaacs's own author note),
  "Yeh-Ho" (Isaacs's hyphenated compound for the joint Yeh Ting / Ho Lung forces).
- Note architecture: author notes arabic, editorial roman, per-chapter restart,
  NO "Ed." prefix. ALL of Isaacs's own notes (numbered endnotes AND asterisks) go
  in the arabic stream, numbered by POSITION.
- Spelling: Isaacs's British 1938 spelling verbatim in the body; American
  English in editorial prose; dates "Month D, YYYY". A book-specific proper name
  takes the body's own capitalization in the notes.
- Editorial-note voice (with the B01-B08 refinements in STYLE.local): concise,
  factual; who/what/when + why-it-matters-here; verdict tag ONLY on a weighed
  claim; marker ON the glossed term; a note never restates the body, the adjacent
  author citation, or the body's own irony; a quoted eyewitness gets placement
  PLUS vantage; a place in a note matches the body's; NO repeated death year (the
  fate clause never restates the year already inside the opening "(1897-1935)").
- Principals (Principal Characters page): Sun Yat-sen (1), Chiang Kai-shek (2),
  Chen Tu-hsiu (3), Borodin (4), Wang Ching-wei (5), Chow En-lai (6), Chiu
  Chiu-pei (7, promoted B08 at the August 7 1927 conference). No further promotion
  expected in ch18-20; Mao is noted (ch00a) but Isaacs's 1938 book never centers
  on him.

## Where the book stands

- Front matter frames the book; ch01-03 background and 1919-25; ch04-05 the
  Canton power struggle and Chiang's March 20 1926 coup; ch06-08 the Northern
  Expedition and the Shanghai risings; ch09-11 the disarming of the Shanghai
  workers, Chiang's April 12 coup, and the opening of the Wuhan act; ch12-14 the
  Wuhan "revolutionary center" at work, the land question, Moscow's paralysis.
  ch15-17 (this batch): the Wuhan debacle -- Feng Yu-hsiang's defection (the June
  Chengchow/Hsuchow conferences), the July 15 1927 split and the end of the
  united front; then the turn to putschism ordered at the August 7 conference
  (Chiu Chiu-pei succeeding Chen), the Nanchang and Autumn Harvest risings; and
  the doomed Canton Commune of December 1927. ch18-20 (the final batch) turn to
  the aftermath: the fruits of defeat, the rise and fall of "Soviet China," and
  the new "national united front" of 1937 with which the book closes.

## What is NEXT

- B09 = ch18-19-20, the FINAL batch. It stays light on chapters and carries the
  close-out: the LINKED index from all the pagemaps (book.json _index_decision),
  the whole-book reconciliation sweep (check 12, check_reconcile.py), term_ledger,
  deep_audit, COMPLETION.md (from the template, NOT another handoff),
  authority.json updated with this book's decided renderings, and the final EPUB
  committed with `git add -f`.

## Open items / cross-unit overlaps for the final reconciliation sweep

- Body offset is 23 (printed = PDF page - 23); front matter was 1. Cite ARABIC
  folios in body-chapter notes.
- **NEW-TO-SHELF renderings to add to authority.json on the final batch:**
  向忠发 Xiang Zhongfa (Hsiang Chung-fah), 许克祥 Xu Kexiang (Hsu Keh-chang),
  何键 He Jian (Ho Chien), 苏兆征 Su Zhaozheng (Hsu Chao-jen), 朱培德 Zhu Peide
  (Chu Pei-teh) [B07], 张太雷 Zhang Tailei (Chang Tai-lei) [B08], plus new ch18-20
  names. (张学良/李立三/贺龙/张发奎 already agreed shelf-wide.)
- **CORRECTIONS-PASS candidates (latent, book-wide):** (a) the clean_body lost
  space after "</i>"+word in earlier batches' author-note citations
  ("North China Daily News,</i>April 13") -- B08 fixed it for ch15-17 via
  fix_italic_space; earlier units still carry it; (b) "mow" now has a book-wide
  glossary terms row (亩 mu) but no first-appearance ch02 note.
- **"Hsu Chien" vs "George Hsu-chien":** ch12 body uses "Hsu Chien"; ch11 noted
  him as "George Hsu-chien" (Xu Qian). Confirm the reader bridges them.
- **Wuhan as a tri-city:** confirm the reader learns early (ch06/ch11 region) that
  Wuhan = Wuchang + Hankow + Hanyang.
- Cross-unit overlaps the blind critic keeps flagging as "undefined" (Borodin,
  Chen Tu-hsiu, Roy, Anna Strong, Wang Ching-wei, Feng, Tang Sheng-chih, Yeh Ting,
  hsien, etc.): each noted at first appearance in an earlier-reading unit -- the
  documented false positive. Before skipping one, grep notes.json for an actual
  EDITORIAL note, not any mention.
- Source quirks kept visible (this batch): ch17's opening-style curly quote where
  a closing belongs ("in China look like? [U+201C]", cf. ch11); ch16's stray '*'
  glyph after "the GPU" (not a footnote, dropped via AST_SKIP); ch15 "The people
  [sic]" and ch16's "[!]"/"[?]" (Isaacs's own bracketed marks). Earlier quirks:
  ch13 duplicate "64", ch14 "[!]", ch05 misnumbered "18,18,20", ch06 endnote "14",
  Malraux "Man's Fate"/"Mans' Fate", ch10 "[sic]"/NUL, ch11 stray curly quote,
  ch14 "Tuhsiu"/"Chiupei", ch16 "midwifein-chief" hard-hyphen glitch.

## Environment / traps state

- Container is reprovisioned fresh each session. setup.sh installs pymupdf,
  pillow, epubcheck 5.1.0 AND (uselessly) Chinese tesseract packs, but NOT the
  English wordlists extract_isaacs.py needs - install wamerican/wbritish by hand
  (kickoff step 1). No OCR needed. Build is text-only, ~0.5 MB.
- tests/run_tests.py "hook stands down on template stub" FAILS by design; do not
  "fix" it.
- Stray-branch / stale-tree check every batch. B08's container was parked on
  template-master (df55427); fetched and hard-reset onto the real tip (364015c).
