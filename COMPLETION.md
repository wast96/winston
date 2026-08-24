# COMPLETION.md — *Zhou Enlai: Commander of the Hidden Front*

The book is COMPLETE. This report replaces the batch handoff: it is what the
commissioner reads to know what the finished edition contains and how far to
trust it.

## Status at a glance

- **28 of 28 units translated** (ch00 Preface through ch27 Afterword).
- **457 footnotes** (after the FN1&#8211;FN5 footnote-density pass; 339 at the
  register close); **36 figures** with captions and screen-reader alt text.
- **847 glossary rows**: 634 people, 70 organizations, 92 places, 44 works, 7 terms.
- **1,367 body paragraphs**, **496 printed-page markers** (folio-followable in the ebook).
- **qa_epub.py: PASS** (78 files, 35 documents, all links resolve; 457 note
  references / 457 bodies / 457 backlinks, all sequential).
- **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings** (EPUB 3.3 rules).
- Deliverable: **`out/zhou-enlai.epub`**, committed to the repository with
  `git add -f` on branch `claude/zhou-enlai` (the final B14 commit).

## What the finished edition contains

Front matter (title page stating the build is complete, a Principal
Characters page, and the translator's and source notes), all 28 chapters in
reading order, a full hyperlinked TOC, footnotes as pop-ups (with an endnotes
page for readers whose apps do not support pop-ups), a glossary, and a
generated-from-scan cover (`data/figs/cover.png`).

Set-off conventions used across the book: displayed documents (the forged Wu
Hao Notice, the Party's rebuttal notice, Mao's Central Government
Proclamation, Barrister Ba He's notice, and the memoir and testimony
passages) are rendered as plain paragraphs with no outer quotation marks, the
attribution intro leading in on a colon; inline dialogue keeps its quotation
marks; the author's source citations are reproduced as "Author's note." at the
marked passages.

**Back matter was left inert deliberately.** The scanned book carries no
errata table and no colophon (PDF page 582, after the Afterword, is blank), so
`book.json` `back_matter` is `[]` by decision, not by omission.

## Per-chapter tally

| Unit | Title | Printed p. | Paragraphs | Notes | Figures |
| --- | --- | --- | --- | --- | --- |
| ch00 | Preface | 1 | 6 | 19 | 0 |
| ch01 | The Birth of the Central Special Section | 1 | 38 | 41 | 2 |
| ch02 | The Special Section's Structure and Duties | 16 | 40 | 23 | 2 |
| ch03 | Intelligence Chief "Wang Yong" (Chen Geng) | 33 | 37 | 20 | 1 |
| ch04 | Heroes of the Intelligence Front | 51 | 62 | 35 | 3 |
| ch05 | The "Three Heroes of Longtan" | 79 | 41 | 21 | 2 |
| ch06 | The First Counter-Espionage Asset (Yang Dengying) | 96 | 40 | 11 | 0 |
| ch07 | Deep into the Tiger's Den | 110 | 54 | 20 | 0 |
| ch08 | Fengtian Military Academy Instructor | 129 | 54 | 16 | 0 |
| ch09 | The Action Section and the "Red Squad" | 154 | 53 | 21 | 1 |
| ch10 | The Red Squad Draws Its Sword | 174 | 34 | 13 | 1 |
| ch11 | Gunshots off Avenue Joffre (Part 1) | 187 | 39 | 14 | 1 |
| ch12 | Gunshots off Avenue Joffre (Part 2) | 203 | 42 | 9 | 3 |
| ch13 | Rescuing Ren Bishi and Guan Xiangying | 219 | 34 | 9 | 0 |
| ch14 | Opening a New Chapter (Part 1) | 232 | 44 | 22 | 1 |
| ch15 | Opening a New Chapter (Part 2) | 252 | 75 | 25 | 1 |
| ch16 | Opening a New Chapter (Part 3) | 277 | 42 | 9 | 1 |
| ch17 | Communications Chief "Zeng Peihong" (Li Qiang) | 289 | 74 | 14 | 5 |
| ch18 | The Red Airwaves That Never Die | 320 | 59 | 19 | 2 |
| ch19 | Averting a Catastrophe (Gu Shunzhang's Defection) | 345 | 42 | 10 | 0 |
| ch20 | Betrayal to the Last Scrap | 362 | 64 | 14 | 0 |
| ch21 | A Vicious Manhunt (Part 1) | 385 | 104 | 14 | 2 |
| ch22 | A Vicious Manhunt (Part 2) | 414 | 47 | 14 | 2 |
| ch23 | Concealment, Withdrawal, Relocation | 441 | 101 | 17 | 3 |
| ch24 | The Traitor Gu Shunzhang's Shameful End | 483 | 63 | 8 | 1 |
| ch25 | The "Wu Hao Notice": Its Fabrication and Its Collapse | 509 | 52 | 10 | 2 |
| ch26 | Conclusion | 526 | 19 | 8 | 0 |
| ch27 | Afterword | 535 | 7 | 1 | 0 |

The book runs to printed page 537 (PDF 553&#8211;581 for this final batch).

## Batching as executed

Fourteen batches, each run in its own conversation, plus the structural
survey. B01 = Preface + ch01 (the first-chapter voice gate; ch01 is the
frozen register reference). B02 through B13 carried ch02 through ch24, two
chapters to a batch as a rule. B14 (this batch) = ch25 + ch26 + ch27, plus
the whole-book completion tail. (The `out/SURVEY.md` batch numbering runs one
behind the working numbering, because B05 combined ch07 and ch08.) Exact
calendar dates per batch were not recorded and are not reconstructed here.

## Checks run book-wide, and what they found

- **Numeric invariants** (`check_numbers` via `verify_unit`, with
  `data/noise.txt`): clean on every unit. Every quantity in the English
  traces to a quantity in the source; the noise file carries the book's
  idioms and measures (extended this batch with 数万万, 亿万, 千百倍,
  日理万机, 万劫, 一百两, 伍豪二字).
- **Parity, anchors, heading shape** (`verify_unit` / `check_structure
  --pairs`): every unit at 1:1 source-to-translation parity; every footnote
  anchor resolves verbatim.
- **Entity survival** (`qc_entities`): 0 misses across ch25&#8211;ch27; the
  book-wide census is consistent. Two glossary hazards were cleaned this
  batch: 斗争 (removed as a works entry, since it false-matched the common
  word "struggle") and 罗斯 (removed, since it is a substring of 俄罗斯,
  "Russia"; "Ross" as a person survives only in ch12, already built).
- **Alignment and content** (`check_align`, `check_content --config`): ratio
  alignment within tolerance; 0 displacement (all decided renderings land in
  the paired paragraph).
- **Register** (`check_register --ref out/ch01_reading.md`): every unit
  within tolerance of the frozen reference; em-dash rate at or under the
  reference throughout.
- **Whole-book reconciliation** (`check_reconcile.py` + by-hand grep, QC
  check 12): glossary-forward 843/847 decided forms present (the 4 unused
  forms &#8212; Chen Zhifei, Zhao Minlin, Jiang Baili, Guangming Daily &#8212;
  are earlier-batch entries whose referents are carried by pronoun in the
  prose). Epithet-drift candidates were false positives (consistent
  renderings). Cross-book renderings checked by hand: Central Special Section
  (285, distinct from Central Special Committee, 10), Kuomintang (646),
  Zhongtong (69), Juntong (45), White Terror (52), Wu Hao (86) all uniform.
  **Spelling locale** was standardized to American: three generic British
  spellings were corrected (grey&#8594;gray, two travelled&#8594;traveled, one
  note theatre&#8594;theater). The nine remaining "Theatre" spellings are
  proper names of real Shanghai venues (Lido, Carlton, Peacock Oriental,
  Beijing Theatre) and correctly keep their spelling.
- **Apparatus** (`check_apparatus.py`): 0 failures, 0 warnings.

## Observed error rate

A random-sample deep audit (QC check 10) was run over the whole book: 41
paragraphs (3.0% of 1,367), fixed seed `20260822`. No substantive error was
found. This batch's own three units (ch25&#8211;ch27, 78 paragraphs) were
verified at 100% coverage against the page scans, not sampled; 0 fabrications
and 0 residual substantive errors survive there. Honest confidence: 0 errors
in 41 sampled paragraphs proves a book-wide substantive-error rate below about
7% at 95% confidence, not zero; the 100%-verified B14 text bounds its own rate
below about 4%. Full method and findings in `out/deep_audit.md`.

## Findings that need the commissioner's eye

- **The Wu Hao Notice affair (ch25) is a strong-corroboration episode and
  checks out.** The 1932 forgery was the work of Zhang Chong of the Kuomintang
  Investigation Section; Mao's 1932 proclamation and the 1967&#8211;1980 legal
  reckoning are well documented. One point of the author's framing is worth
  the reader's eye and is footnoted: Kang Sheng knew first-hand the notice was
  fake (he was himself named, as "Zhao Rong," in the 1931 bounty notice) yet
  stayed silent during the Cultural Revolution.
- **The Yan Baohang / Operation Barbarossa claim (ch26) is graded in the
  note.** That Yan Baohang obtained the German invasion date and that it
  reached Moscow through Zhou Enlai is attested; the further claim that it
  gave the Red Army a 24-hour head start and won Stalin's thanks is the
  Chinese account's and is not confirmed by Western scholarship. The note
  says so.
- **A source inconsistency in ch25 is footnoted:** Mu Xin introduces a memoir
  passage as Li Yimang's, but cites *The Blurred Screen*, which is Huang
  Mulan's memoir.

## Residual uncertainties a reader should know about

- Provisional glossary romanizations (marked `provisional` in
  `out/term_ledger.md`) are the translator's best readings, not forms found in
  scholarship; they are flagged where they occur.
- The graded historical verdicts above (corroborated / uncorroborated /
  contradicted) live in the footnotes; the translated prose always keeps Mu
  Xin's own telling, and the note carries the verdict.
- No damaged-scan gaps remain in this batch; the one OCR cut-off found in ch25
  (逸豪, p510) was read off the image and restored.

## Provenance and method

- **Source:** a scanned, image-only edition of Mu Xin, *隐蔽战线统帅周恩来*
  (`source.pdf`, 582 pages); body offset a constant 44 (printed = PDF minus
  44).
- **OCR:** tesseract (`chi_sim`, psm 6) with the measured crop (left 0.11,
  right 0.90, top 0.135, bottom 0.95) and the running head stripped; a second
  read via `scripts/ocr_dual.py` (PaddleOCR's weights host was unreachable, so
  the dual-tesseract substitute was used, as recorded in `PROGRESS.md`).
- **Pipeline as run for B14:** render &#8594; ocr_crop &#8594; the
  `scripts/recovery/b14_*` rebuild driver (strip furniture / structure /
  assemble / paragraph surgery / OCR fixes / apply / pagemap) &#8594;
  translate &#8594; apparatus &#8594; checks &#8594; build. Paragraph
  boundaries were determined by reading the page images (indent geometry is
  unreliable on this scan) and encoded as surgery markers.
- **Builder features that must not be reverted:** the pending-aware then
  cleaned full TOC; note pop-ups with an endnotes fallback; the refusal to
  build on an unmatched note anchor or unplaced figure; byte-identical cover
  copy; render-layer smart quotes so source files stay ASCII.
- **To rebuild from a clean checkout:** regenerate `data/zh/` with the
  `scripts/recovery/b*_rebuild.sh` drivers (raw-OCR backups under
  `data/txt_backup_b*`), then `python3 scripts/build_reading_epub.py`,
  `python3 scripts/qa_epub.py`, and `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar
  out/zhou-enlai.epub`.

## Register revision pass (R1-R5) — revision record, 2026-08-22

After the book was complete, a five-batch **register revision pass** ran over
the whole text (`REVISION_PLAN.md`), operationalizing the findings in
`review/REGISTER_PASS_ASSESSMENT.md`. It was a REGISTER pass, not a
retranslation: content frozen, no paragraph merged or split, no fact/name/
date/number/hedge changed. Every change is an English-surface edit at an
identified defect site.

**Whole-pass total: 192 word-level edits, 188 insertions / 188 deletions
across 25 of 28 reading files — zero paragraph-boundary changes anywhere.**
By tier:
- **Tier A globals (R1):** 95 day-month dates normalized to month-day; the
  政治局 cascade to "the Politburo" (~65 sites incl. notes/glossary/authority);
  ledger residuals ("in good time"->"in time/promptly" ×16; ch07 "driving
  into"->"planted inside").
- **Tier B tic sweep (R1 exemplar ch15, R2-R5):** ~40 narration edits total —
  litotes calques ("no little/no small/no few" -> considerable / a good
  deal / a good many), trailing/appositive "besides" (-> as well / apart
  from / also), 只好 "could only" -> "had no choice but to", 相继/先后 for
  people -> "in succession", antique stragglers (thereupon/whereupon/at
  length/"was given to" -> then / and then / at last / often did),
  fronted-infinitive de-inversions, redundant quote-tags. Most chapters came
  back nearly clean; ch26/ch27 fully clean. Restraint held: the ch15 exemplar
  was 12 edits / 75 paragraphs, and no later batch exceeded that density.
- **Reconciliation (R5):**
  - **叛徒 verdict:** "renegade" (29 occ., confined to batch B12 ch21/ch22 +
    ch24, all rendering 叛徒, co-occurring with "traitor") was **per-batch
    drift** and was collapsed to "traitor" (28 sites; 1 kept where the same
    sentence already used "traitor"). "turncoat" (11 occ.) is the
    STYLE-sanctioned variant and was **kept**.
  - **Killing-verb ledger:** 3 source-verified fixes where 镇压/除掉 of
    traitors by the Red Squad was softened to "put down"/"did away with" ->
    "eliminated" (ch09 ×2, ch16).
  - 破坏 -> "wreck*": reviewed book-wide and left as contextually appropriate
    (mass-arrest destruction = smash/wreck, not the covert-subversion
    "sabotage"); the abstract-noun calque the ledger flagged does not survive
    in the text. See PROGRESS.md for the site inventory if a uniform
    "sabotage" is ever wanted.

**Verification:** every edited unit with a reading-source verify_unit GREEN
(parity + numbers 0 unresolved + anchors); units edited without regenerated
data/zh verified by the zh-independent guard set. check_register within
tolerance of the frozen ch01 reference throughout. KEEP-list diff grep clean
(no quoted-document register change, no "Comrade" thinning, no em-dash swaps,
no contractions by quota). **Spot audit: 20+ edited paragraphs across R1-R5
re-verified against source — zero meaning drift.** Build 28/28, qa_epub PASS,
**epubcheck 5.1.0: 0 errors / 0 warnings** after the final rebuild.

The register pass is CLOSED. The commissioner's requested **footnote-density
pass** (`FOOTNOTE_PASS.md`) is now also CLOSED: FN1&#8211;FN5 carried the book
from 339 footnotes to **457**, sweeping every chapter for the people, places,
events, institutions, terms, and allusions a non-specialist Western reader
would miss, at first appearance book-wide, each with real checked content and a
fact-check verdict. FN5 (ch23&#8211;ch27 plus whole-book apparatus
reconciliation) added 16 notes and cleared the standing backlog: shikumen
(ch02), Sun Yat-sen University Moscow (moved to ch03), the Third Plenum of the
Eleventh CC (ch04), Sun Chuanfang (ch05), the Shen Bao (moved to ch10), the
China Mutual Aid Society / China Relief Society tie and Ta Kung Pao (ch14), the
E-Yu-Wan Soviet (moved to ch15), the Baoding Military Academy (ch16), and Li
Mingrui (ch17). Everything else on this book is now a corrections pass per
CLAUDE.md.

**Density record (footnotes at each pass close):** 339 (register close) &#8594;
385 (FN1, ch00&#8211;05) &#8594; 409 (FN2, ch06&#8211;11) &#8594; 427 (FN3,
ch12&#8211;17) &#8594; 441 (FN4, ch18&#8211;22) &#8594; **457 (FN5, ch23&#8211;27
+ whole-book reconciliation)**. The count tapers in the tail by design: the
later chapters reuse a cast already introduced, and a note is placed once, at
first appearance. No subject is double-noted; the Hu&#160;Yepin cluster
(ch09 the arrest, ch20 the Longhua Martyrs, ch22 his individual bio) was
confirmed complementary, not duplicative.

## Definition of done — met

- [x] The EPUB: front matter, all 28 chapters, full clean TOC, cover, figures
  with captions and alt text, footnotes at reader-model density, glossary and
  translator's note current, qa_epub PASS across the whole spine, epubcheck
  clean, back matter correctly inert, and the file itself committed
  (`git add -f out/zhou-enlai.epub`).
- [x] `out/<id>_reading.md` per unit (the correction surface),
  `out/term_ledger.md`, `out/deep_audit.md`.
- [x] `notes.json`, `glossary.json`, `figures.json`, `book.json` current;
  `authority.json` updated with this book's decided renderings.
- [x] `COMPLETION.md` written from the template, with the sampled error rate.
- [x] `PROGRESS.md` and `HANDOFF.md` current; `HANDOFF.md` rewritten to say
  the book is COMPLETE; `CHANGELOG.md` updated.

Further work on this book is a corrections pass, not new translation.
