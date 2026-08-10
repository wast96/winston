# HANDOFF — The Golden Roc Dynasty (陆小凤传奇·金鹏王朝, Gu Long)

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite it
at the end of every batch; always keep the paste-ready kickoff message below as
its first section. When the book completes, replace the kickoff with the
completion notice and do not touch it afterward (the Stop hook keys off it).

## Message to paste into the next chat

```
Lu Xiaofeng 1 B01

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 金鹏王朝 (The Golden Roc Dynasty), Volume 1 of Gu Long's Legend of Lu Xiaofeng, from a digital source EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/lu-xiaofeng-1; expect the harness to start you on a stray per-task branch and consolidate per rule 2 (check out claude/lu-xiaofeng-1, reset to origin, and if a stray branch carries commits, fast-forward or cherry-pick them on, push, and delete the stray). Deliverable out/lu-xiaofeng-1.epub.

Run ./setup.sh first and record any failure in PROGRESS.md. data/src and data/src_epub are gitignored and regenerable: if they are missing, run scripts/ingest_epub.py source.epub to recreate them (the survey already authored book.json, so do NOT overwrite book.json). This book has NO source-edition footnotes; re-grep this unit's source for \[\d+\] and record "none present" in PROGRESS.md.

Do Batch B01 = the Prologue (ch01, 楔子; ~6,069 source chars; four named vignettes that are book.json sections: Granny Xiong's Sugar-Roasted Chestnuts / The Honest Monk / Ximen Chuixue / Hua Manlou), end to end per the CLAUDE.md pipeline:
1. Read ch01 from data/src/06_part0000-split-004.txt. Fix extractor-split paragraphs (a line whose last char is not in 。！？"）…— continues the next). Recover set-off formatting with apply_format_markers.py where the source HTML encodes it: the four vignette titles render as ### section headings (they match book.json sections ch01s01..ch01s04 in order); any bare numeric divider renders as a *** scene break.
2. This is the REGISTER-SETTING chapter and it defines the frozen reference for the whole book, so get the voice right. Translate to the CLAUDE.md register contract: fast, spare, wry Gu Long, short paragraphs, abrupt line breaks; readable modern English, not fake-antique. Consult glossary.json and authority.json BEFORE romanizing anything (both are empty of wuxia terms, so you are DECIDING the shelf renderings here: Hanyu Pinyin without tone marks, e.g. Lu Xiaofeng, Ximen Chuixue, Hua Manlou). Write a two-line voice sheet into HANDOFF for every character who speaks (Ximen Chuixue and Hua Manlou both appear in the prologue). Never invent bridging text; render digitization glitches to plain sense and LIST each in PROGRESS.md; the source's own errors of fact stay visible and get a footnote. Verify the chapter's TAIL against the source explicitly before shipping.
3. Write out/ch01_en.json (a flat JSON array, one English paragraph per source line) and run make_bilingual.py ch01 ...; then verify_unit.py ch01 (parity + numbers with --noise data/noise.txt + anchors); check_align.py and check_content.py; qc_entities.py.
4. Footnotes per the reader model in CLAUDE.md (a Western reader with no Chinese background): the jianghu itself, 糖炒栗子 street food, Shaolin and the 老实和尚, and the standing reputations of Ximen Chuixue and Hua Manlou are the kind of thing that earns one; expect roughly 8-15. Use apparatus_merge.py (never a shell heredoc), first-appearance greps, and a NOT-re-noted list; check_apparatus.py clean. Flag the principal cast (Lu Xiaofeng, Ximen Chuixue, Hua Manlou) with "principal": true and a one-line cast blurb in glossary.json. No figures (the book has none).
5. Rebuild the EPUB, run qa_epub.py until green and epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) clean; record every check result in PROGRESS.md; update HANDOFF.md (voice sheets, settled renderings, story state); commit and push to claude/lu-xiaofeng-1.
6. STOP at the first-chapter voice gate (Step 0c). Do NOT begin Batch 2. Your final chat reply must (a) attach the built out/lu-xiaofeng-1.epub and (b) say this is the voice gate and ask the commissioner to read the Prologue and judge voice, footnote density, and formatting. Paste the reply's fenced block as the frozen-reference note / the B02 kickoff-in-waiting so the Stop hook is satisfied, but make clear B02 does not start until the voice is approved.

Cite chapters and sections, never pages. Do not pause for approval mid-batch; the only stop is the voice gate at the end.
```

## What is DONE (do not redo)

- Step 0 survey: ingested the source, authored book.json (13 units: prologue +
  12 chapters; prologue's 4 vignettes are sections; chapters 1-12 use ***
  scene breaks), built the skeleton EPUB, ran the survey. Committed and pushed
  to claude/lu-xiaofeng-1 (99521e0). No chapters translated yet.

## Tooling in place (do not revert)

- Nothing patched yet. Scripts are the template defaults. epubcheck lives at
  /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetched it).

## Renderings settled this batch / carry-forward

- None yet. glossary.json and authority.json hold no wuxia terms, so B01
  decides the first shelf renderings. Pinyin without tone marks. Names seen so
  far and awaiting a decided rendering: 陆小凤 (Lu Xiaofeng), 西门吹雪 (Ximen
  Chuixue), 花满楼 (Hua Manlou), 熊姥姥 (Granny Xiong / the villainess of the
  prologue), 上官丹凤 / 丹凤公主 (Princess Danfeng, appears from ch03), 金鹏王朝
  (The Golden Roc Dynasty), 峨嵋 (Emei). Provisional English chapter titles are
  in book.json and may change as the text is read.

## Voice sheets (one per major character, written at first appearance)

- (none yet; B01 writes the first ones for Ximen Chuixue and Hua Manlou)

## Where the book stands

- Nothing translated. The prologue opens the book with four vignettes that
  introduce the world and two of the principal swordsmen (Ximen Chuixue, Hua
  Manlou) before Lu Xiaofeng's own plot begins in Chapter 1.

## What is NEXT

- Batch B01 = the Prologue (ch01), ending at the voice gate. Then B02 = Ch 1,
  and the plan in book.json "batches" (B03 ch2-3, B04 ch4-5, B05 ch6-7, B06
  ch8-10, B07 ch11 the ~31k climax, B08 ch12 + back matter/reconciliation/
  completion).

## Open items for the read-through

- English chapter titles are provisional (set in the survey, not yet checked
  against the translated text).
- The rendering of 熊姥姥 (literal "Bear-Granny"; likely surname Xiong) is a
  first-batch call worth flagging.

## Environment / traps state

- epubcheck available (path above). qa_epub + epubcheck both clean on the
  skeleton.
- Source: a 2013 Henan Wenyi digital EPUB; simplified characters; NO source
  footnotes; NO story images (cover + 2 decorative endpapers only). The 18
  spine chunks map 1:1 to logical units; excluded front matter is listed in
  book.json _source_note.
- The source puts a full-width space inside chapter headings (第一章　...);
  cosmetic, collapses on extraction.
- data/src and data/src_epub are gitignored (regenerate with ingest_epub.py);
  data/figs images and source.epub ARE tracked, so the cover builds without
  re-ingesting.
- Stray-branch trap: the harness starts each session on a claude/new-session-*
  branch. The canonical, only branch for this book is claude/lu-xiaofeng-1
  (rule 2). Consolidate onto it every batch.
