# HANDOFF

## Message to paste into the next chat

```
The Stealthy Ones B09 (FINAL)

Read CLAUDE.md, then STYLE.md, then HANDOFF.md, then book.json.

This is the FINAL batch. Chapters 1-8 are COMPLETE: the whole novel body is
translated and the cumulative EPUB is 8 of 8 chapters, qa PASS and epubcheck clean.
out/ch01_reading.md is the FROZEN register reference. B09 carries the back matter
and the whole-book close-out. Do all of the following, end to end, per CLAUDE.md's
"Definition of done" and its final-batch instructions. Do not pause for approval.

1. AFTERWORD (解説) as back matter. Translate the afterword by Musashino Jiro,
   printed folios 529-534 (PDF 531-536; offset printed = pdf - 2), as CLEARLY
   ATTRIBUTED back matter, NOT as a chapter of the novel. It is a critic's essay
   about the book and its author: register-exempt (a formal modern critical essay),
   rendered in clean contemporary English. The OCR is a structural aid only:
   TRANSLATE BY READING THE PAGE IMAGES (render.py 531 536, then read
   data/png/p05NN.png), and crop-verify every name, title and date by eye with
   scripts/cropview.py. Add it through back_matter.json (see how the builder renders
   back matter) with a clear heading and an attribution line naming Musashino Jiro
   and stating it is the afterword to the 1987 Kobunsha bunko edition. House macron
   romanization; reading text stays plain ASCII apostrophes/quotes (typographized at
   render); o/u/a-macron and the em-dash are the only non-ASCII, plus the book's
   established loanword spellings (Lourenso with c-cedilla, irmao with a-tilde).

2. COVER. book.json cover_image is empty, so the builder makes a typographic cover.
   Look at the scan's colour cover (PDF p1) and decide whether it is worth
   extracting; if yes, set cover_image (copied byte-identical, never through the
   figure pipeline) and rebuild. Otherwise keep the generated cover and say so in
   COMPLETION.md.

3. WHOLE-BOOK RECONCILIATION SWEEP (check 12). Run scripts/check_reconcile.py and
   resolve the OPEN reconcile items at the end of PROGRESS.md's Batch 8 section:
   Koya-san vs Mount Koya (macron); Osaka vs Osaka-macron; Daito vs Daito-macron;
   Sasa vs Sassa Narimasa (standard Hepburn is Sassa); Kyushu vs Kyushu-macron.
   DECIDE one form for each, change the glossary, and grep-fix EVERY built unit
   (all out/*_reading.md, notes.json bodies, glossary.json) INCLUDING the wrong
   variant (variants map: wrong forms only, never the canonical), then rebuild and
   run full QA. A global fix applied to only some units is worse than none. The
   tool's drift candidates are for a HUMAN read; some variation is legitimate (see
   references/register-drift.md). Also grep-count the ~20 decided renderings and
   confirm each recurring subject's note sits at its first appearance book-wide.

4. LEDGERS. Render out/term_ledger.md from glossary.json so someone who reads no
   Japanese can audit every rendering, and feed this book's decided renderings back
   into authority.json (the cross-book name ledger).

5. DEEP AUDIT (check 10). Random-sample 3-5% of the book at a fixed seed, full
   paranoid treatment (read zh against en), and write out/deep_audit.md with the
   observed error rate reported honestly (zero errors in N paragraphs proves a rate
   below a bound, not zero). Watch the "invented precision" class (definiteness the
   source withholds).

6. COMPLETION.md from COMPLETION.template.md (NOT another handoff): the sampled
   error rate, the residual uncertainties a reader should know, and the standing
   decisions (the source inconsistencies rendered as read; the one illegible route
   waypoint at folio 509 left as motion, not invented; the Yamashina/Tokitsune diary
   slip footnoted at folio 522; the inverted cauldron legend at folio 528). Commit
   the final EPUB itself (git add -f out/the-stealthy-ones.epub; branches outlive
   containers, chat attachments do not). Rewrite HANDOFF.md to say the book is
   COMPLETE and further work is a corrections pass, and do NOT modify the kickoff
   section afterward (the Stop hook would then demand a block that no longer exists).

Build with build_reading_epub.py, then qa_epub.py and epubcheck (java -jar
/tmp/epubcheck-5.1.0/epubcheck.jar out/the-stealthy-ones.epub). One branch:
claude/the-stealthy-ones (CLAUDE.md rule 2 overrides any harness note naming a
different branch; expect a stray per-task branch, reset the canonical branch to
origin, do the work there, and delete the stray local and remote). Since this is the
last batch there is no next kickoff to paste: deliver the built EPUB in chat AND
deliver COMPLETION.md in chat.
```

## What is DONE (one line per batch, do not redo)
- Batch 0 (survey): 8-chapter structure, metadata, skeleton EPUB, batching approved
  (8 chapter-batches; afterword as B09 back matter; typographic cover).
- Batch 1 (Chapter 1, "New Waves", folios 5-68): COMPLETE. VOICE GATE and FROZEN
  register reference. 328 paras, 67 notes, 13 principals.
- Batch 2 (Chapter 2, "A Warm Current", folios 69-134): COMPLETE. ~430 paras, 29
  notes, 24 glossary rows (Maki principal).
- Batch 3 (Chapter 3, "Surface and Underside", folios 135-198): COMPLETE. ~17,700
  words, 34 notes.
- Batch 4 (Chapter 4, "War upon War", folios 199-256): COMPLETE. ~16,140 words, 20
  notes.
- Batch 5 (Chapter 5, "The Two of Them", folios 257-358): COMPLETE. ~28,000 words,
  24 notes, 25 glossary rows.
- Batch 6 (Chapter 6, "Earth and Water", folios 359-412): COMPLETE. ~16,200 words,
  9 notes.
- Batch 7 (Chapter 7, "Death, Death, Death", folios 413-457): COMPLETE. ~11,800
  words, 13 notes. Maki dies; Kazue lost overseas.
- Batch 8 (Chapter 8, "Death Throes", folios 459-528): COMPLETE. ~20,270 words (the
  longest chapter), 441+ paras, 17 notes (book total 213), 13 glossary rows (5
  people, 5 places, 3 terms; no new principals), figures ch08 EMPTY. qa PASS
  (213/213/213), epubcheck 0/0/0/0, check_apparatus clean, register within
  documented tolerance. Goemon's road to the cauldron; father and son boiled
  together, Goemon turning the blind boy UNDER him to end his suffering (the
  traditional legend inverted). THE NOVEL BODY IS NOW FULLY TRANSLATED.

## Branch note (read this)
Working branch is `claude/the-stealthy-ones`. Harnesses routinely start a session on
a stray per-task branch. The recipe (CLAUDE.md rule 2, which overrides any harness
note naming a different branch): check out `claude/the-stealthy-ones`, reset it to
origin, do all work there, and DELETE the stray branch (local and remote). B08 was
started on `claude/ch08-death-throes-l6koae` (identical to origin/claude/the-stealthy-ones
at Batch 7); the canonical branch was reset to origin, all B08 work done and pushed
there, and the stray deleted.

## Tooling in place - do NOT revert
- `data/structure.json` from book.json. Offset printed = pdf - 2 (constant, no
  plates), verified at every opener AND at the afterword divider.
- `scripts/cropview.py`: fractional crop tool for eyeball verification.
- OCR structural aid: ocr_crop.py with `--left 0.06 --right 0.96 --top 0.09
  --bottom 0.935 --lang jpn_vert --psm 5`. For ch08 stage-3 DID write pages this
  time; if a later run writes 0, regenerate per-page by hand (tesseract loop into
  data/txt, jpn_vert, psm 5, OMP_THREAD_LIMIT=1, verify pgrep -c tesseract = 0).
  Translate from the page images, not the OCR.
- Glossary is edited directly as a SECTIONED, CJK-keyed file (json.load -> add keys
  -> json.dump ensure_ascii=False, or the Write tool); apparatus_merge is used for
  NOTES and FIGURES only (its glossary merge is flat and breaks the sectioned builder).
- Note anchors are LITERAL substrings of the reading file (o/u/a-macron and straight
  ASCII quotes allowed; no em-dashes), in BODY paragraphs; note BODIES use numeric
  character references, authored via a Python encoder (keep <i> tags literal), end
  "(Printed folio NNN.)". apparatus_merge validates anchors; the builder refuses a
  heading-only or unmatched anchor.
- Reading files use house MACRON romanization (o/u/a-macron) plus the em-dash, and
  the two established loanword spellings (Lourenso with c-cedilla, irmao with
  a-tilde). "Osaka", "Kyoto", "Daito" stay plain (pending the reconcile).

## Renderings settled through Batch 8 (in glossary.json; reuse unchanged)
All Batch 1-7 renderings stand. Added in Batch 8: people - Asahi-hime, Seyakuin
Zenso, Toyotomi Hideyori, Yi Sun-sin, So Yoshitomo. Places - the Jurakudai, Yodo
Castle, Fushimi Castle, Edo Castle, Nagoya (Hizen). Terms - the nightingale floor
(uguisubari), the plover incense-burner, the Bunroku-Keicho War. Reused unchanged:
Ishikawa Goemon, Ishikawa Kazumasa, Gaspar Coelho, the Lady Yodo (Ochacha), Hattori
Hanzo, Torii Moriichiro, Tamo/Kiara, Lourenso, Goichi, Maki, Kashii, the Shofuku-ji,
Mount Koya, the Negoro-ji, Toyotomi Hidetsugu, Takayama Ukon, Frois, Valignano,
Organtino, the Nanban-ji, Momochi/Fujibayashi, the Bansenshukai, Saeki Dennai. The
long ch08 "Rendered-as-read" list (Koga ninja codenames, the Korean toponyms, the
Kanto castles, Hideyoshi's other concubines, the cited playwrights and works) is in
PROGRESS.md.

## Where the story stands
The novel is FINISHED. Chapter 8 has carried Goemon to the cauldron: after ten years
farming at Nagao and raising the blind Goichi, he leaves the boy with Ryosai and Tamo
at the Shofuku-ji, infiltrates Yodo castle to kill the Taiko, and is caught in a trap
Hanzo built for him. Hanzo brings the blind child to the execution, and father and
son are boiled together, Goemon turning Goichi under to end his pain. The historical
frame (Kazumasa's defection, the 1587 expulsion edict, the Jurakudai, Odawara and the
founding of Edo, the Korea invasions and Yi Sun-sin, the Hidetsugu purge, the
Yamashina/Razan execution record) is all in place. Only the back matter, the
reconciliation sweep, and the close-out ledgers remain for B09.

## B09 scope (the FINAL batch)
The afterword (解説) by Musashino Jiro, printed folios 529-534 (PDF 531-536), as
clearly-attributed back matter via back_matter.json; the cover decision; the
whole-book reconciliation sweep (check 12) resolving the OPEN reconcile items;
out/term_ledger.md and the authority.json update; out/deep_audit.md (check 10); and
COMPLETION.md from the template, with the final EPUB committed. Leave nothing for a
"B10": B09 is the end. See the pasted kickoff above for the step-by-step.

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify with
  scripts/cropview.py.
- Glossary sectioned and CJK-keyed; apparatus_merge for notes+figures only.
- NARRATION em-dashes kept low (convert appositive dash-glosses); dialogue
  trailing/interruption em-dashes and quoted-document dashes are licensed. The
  register checker's "shall" and low-contraction flags on exposition-heavy chapters
  are documented deviations, not the ch01 defect.
- OPEN reconcile items for B09: Koya-san vs Mount Koya; Osaka vs Osaka-macron; Daito
  vs Daito-macron; Sasa vs Sassa Narimasa; Kyushu vs Kyushu-macron. Fix all +
  glossary + variant grep at the reconcile.
- OMP_THREAD_LIMIT=1 for tesseract; check pgrep -c tesseract = 0 after OCR.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (java present).
- No data/pagemap/ for ch02-ch08 (only ch01 emits in-text page markers); qa still
  PASSES and every note cites its printed folio in prose.
- One checker regression test ("hook stands down on template stub") fails; a template
  corner case that does not affect real batch replies.
