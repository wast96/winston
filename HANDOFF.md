# HANDOFF -- The Gangs of Old Shanghai (旧上海的帮会)

**THE BOOK IS COMPLETE.** All 28 units are translated, annotated, reconciled, and built
into `out/gangs-of-old-shanghai.epub`, which passes qa_epub and epubcheck cleanly. There
is no next batch and no kickoff to paste. The full completion report is `COMPLETION.md`;
the batch-by-batch record is `PROGRESS.md`.

## What "complete" means here

- 28 / 28 units: front matter, 24 memoir/study chapters, and the two Heng Society
  appendices (charter and 1934 member roll).
- 409 footnotes at reader-model density; glossary 920 rows; 0 figures (an all-text
  anthology, honest empty set).
- qa_epub PASS (28 documents, 1213 paragraphs, all note refs/bodies/backlinks resolve);
  epubcheck 5.1.0 clean (0 fatals / 0 errors / 0 warnings / 0 infos).
- Book-wide checks green: check_content exit 0, check_apparatus 0/0, check_reconcile
  exit 0, qc_entities 0 misses, check_register within tolerance, check_align within
  tolerance.
- The final EPUB is committed to the branch with `git add -f` (chat attachments do not
  outlive the container; the branch does).

## If further work is requested, it is a CORRECTIONS pass

Follow the corrections workflow in CLAUDE.md, not a new batch:

- The commissioner reads the EPUB and files items in `CORRECTIONS.md` (or pastes them in
  chat, in which case transcribe them into `CORRECTIONS.md` first).
- GLOBAL corrections (a rendering, a register rule, a note policy) cascade via a
  glossary/style change plus a grep-driven edit across ALL built units including note and
  glossary bodies, then a full rebuild and QA.
- LOCAL corrections are a fix at one spot.
- A zero-item corrections pass is still a clean-checkout regression run: re-clone,
  `./setup.sh`, regenerate, rebuild, re-verify, prune any stray branch.
- After any corrections batch: rebuild, qa_epub, epubcheck, list every file touched, and
  add a dated entry to `CHANGELOG.md`.

## Standing decisions to keep (do NOT revert)

- CLAUDE.md's operating-guardrails section; the `check_numbers.py` million/billion patch;
  the `data/noise.txt` rule ordering (the `万千` rule must precede the bare-`万` rule) and
  its accumulated blocks; the builder's refusal on orphan anchors and unplaced figures.
- `back_matter.json` is inert by decision (the book has no errata; its colophon data is in
  `book.json` `source_ref`). Do not "complete" it.
- The 1934 member roll (ch28) is a DESCRIBED appendix by decision, not a 324-name
  transcription; a full romanized roster would need a dedicated name-by-name
  crop-verification pass and is not something a later session should silently attempt.
- Two-contributor disagreements (Gu Zhuxuan's name/master/rank across ch25-26; Zhang
  Xiaolin's birthplace across ch22-23) are rendered as printed and footnoted; do not
  reconcile them.

## Rebuild from a clean checkout

```
./setup.sh
python3 scripts/build_reading_epub.py
python3 scripts/qa_epub.py out/gangs-of-old-shanghai.epub
java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/gangs-of-old-shanghai.epub
# regenerate work/content_cfg.json (gitignored) over every unit before check_content
```

setup.sh reports one expected checker-test line ("hook stands down on template stub");
that path is not exercised now that HANDOFF carries no kickoff block, and the two
enforcing hook paths pass. Do not "fix" the hook.
