# PROGRESS — The Golden Roc Dynasty (陆小凤传奇·金鹏王朝, Gu Long)

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, chapter/section scope), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup / Survey (Step 0)

- `./setup.sh`: green (pillow installed, epubcheck present at
  /tmp/epubcheck-5.1.0/epubcheck.jar, checker regression tests green). Nothing
  FAILED.
- Source EPUB: `陆小凤传奇·1·金鹏王朝`, 古龙 (Gu Long), Henan Literature & Art
  Publishing House, 2013 (古龙文集 collected-works line), ISBN 978-7-80765-772-9.
  Simplified characters. The novel was first serialised 1976-77.
- Ingest (out/INGEST.md): 18 spine documents, 3 images, 124,096 source chars.
- **Source's own notes: NONE.** Grep for `\[\d+\]` over every extracted unit
  returns zero matches. No `source_notes.json` stream needed for this book; re-grep
  each batch's source and record "none present" per CLAUDE.md.
- Structure: the source split its single text into 18 mechanical
  `part0000_split_NNN.html` chunks. These DO line up one-to-one with the logical
  units: each content chunk opens with a `<p class="x2" id="toc-anchor">`
  heading. Mapped to 13 logical units — the prologue (楔子) + 12 numbered
  chapters. No merge/split of content chunks was needed; only front matter was
  excluded (see book.json `_source_note`): 2 half-title stubs, the CIP colophon,
  the source TOC, and the titlepage (its cover.jpeg reused as the EPUB cover).
- **The prologue alone has named internal sections** — four vignettes (熊姥姥的糖炒栗子
  / 老实和尚 / 西门吹雪 / 花满楼), modelled as book.json sections and shown in the TOC.
  Chapters 1-12 divide themselves with bare numeric markers (01, 02, ...); these
  are scene breaks, to be recovered as `***` with apply_format_markers.py, not
  TOC sections.
- **Chapter 11 (第六根足趾, "The Sixth Toe") is the long climax at ~31,104 chars**
  — roughly 3x a normal chapter. Sized as its own batch.
- Images: `cover.jpeg` = the cover (reused byte-identical). `00001.jpeg`/`00002.jpeg`
  = decorative publisher endpapers (alt 知识小说环衬), no story content — NOT carried
  into figures.json. The book has no story images of its own.
- Digitization glitches: none audited yet (a per-batch task). Note the source
  uses a full-width space inside its chapter headings (第一章　...), collapsed in
  extraction — cosmetic only.
- Skeleton build: `qa_epub.py` PASS (26 files, 19 documents, all links resolve);
  `epubcheck` 3.3: 0 fatals / 0 errors / 0 warnings / 0 infos. Cover embedded.

## B01 = Prologue (ch01) — voice gate

- (pending commissioner approval of the survey; runs in its own chat)
