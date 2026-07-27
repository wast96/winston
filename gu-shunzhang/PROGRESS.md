# PROGRESS — 特務工作之理論與實際 (Gu Shunzhang)

Read this first. Written as work happens, not at the end.

## Status: Batch B01 (Chapter 1) DONE, built and QA-green.

Branch `claude/chapter-1-ocr-qc-pf39oq`. One of eight chapters translated.
`out/theory-practice.epub` builds with a full pending-aware TOC; `qa_epub.py`
PASS. Next batch is B02 (Chapter 2); see `HANDOFF.md`.

## Source facts established at setup (unchanged)

- 298-page image-only PDF, National Central Library (Taiwan) copy. No text
  layer. Vertical, right-to-left, Traditional characters. Running head down the
  outer margin, chapter title as running foot, folio at the bottom outer
  corner. Round NCL library seal stamped across the centre of many pages.
- Page offset drifts; use `book.json` per-section anchors. Chapter 1 opens at
  PDF 27 = printed 1 (confirmed by eye against folio 一).

## Batch B01 — Chapter 1 (緒論 / Introduction), printed folios 1-16 (PDF 27-42)

Three sections: §1 The Nature of Secret-Service Work (printed 1-6), §2 The
Importance of Secret-Service Work (printed 7-11), §3 The Scope of Secret-Service
Work (printed 12-16). 60 body paragraphs, 25 footnotes. No figures in this
chapter (pure text; confirmed by reading all 16 pages).

### Environment
- Installed: tesseract 5.3.4 with `chi_tra` and `chi_tra_vert`; pymupdf,
  pillow, numpy. `poppler-utils` present but unused for rendering.
- PaddleOCR NOT installed: its model weights download from a host outside the
  sandbox allowlist (as the sibling `ocr_dual.py` note already recorded), so
  check 1's dual engine is tesseract `chi_tra_vert` versus a direct eye-read of
  the 300 dpi scans, which for this chapter is the stronger of the two. Record
  this for later batches; retry Paddle only if the allowlist changes.
- `cv2` (opencv) NOT installed; `find_figures.py` needs it. Not required for
  Chapter 1 (no plates). Install before the first batch that has figures
  (Chapter 2 onward may have plates).

### Deliverables produced
- `out/ch01_reading.md` — clean English, the correction surface.
- `out/ch01_bilingual.md` — QC-only source-above-English draft (gitignored).
- `data/zh/ch01.txt` — verified source transcription for the parity check
  (gitignored; rebuilds from `out/ch01_bilingual.md`).
- `notes.json` — 25 notes keyed `ch01`. `glossary.json` — ledger extended.
- `out/theory-practice.epub` — cumulative EPUB, full TOC, ch1 linked, ch2-8
  pending.

### The eight checks — what ran and what it found
1. **Dual-engine OCR diff.** Tesseract `chi_tra_vert --psm 5` (the measured
   crop) versus a direct character-by-character eye-read of every one of the 16
   rendered pages. The seal and the vertical type make tesseract noisy;
   systematic mangles seen: 緒論→繕論, 暗殺→唔殺, 特務→畫務/岩務, 偵緝→偵繩,
   格伯武 read cleanly. Every disagreement was resolved off the scan. The
   eye-read is the authority for this chapter.
2. **Blind double translation.** The seven argumentative/analytical passages
   (definition + GPU; the negative/positive-aspect argument; 防患未然; the
   履霜堅冰 / 百發百中 passage; the budget-figures passage; the 1927/C.P. history;
   the WWII-Pacific forecast) were retranslated in a separate context with no
   sight of the first pass and diffed. Close agreement throughout; the one
   substantive note was that 利害 in the history passage is 厲害 ("formidable"),
   which the finished text already reflects. Descriptive/list filler was
   sampled, not fully doubled.
3. **Round-trip back-translation.** Seven finished English passages (incl. all
   the numbers) were back-translated in a fresh context and diffed against the
   source: no omissions and no additions detected. It flagged the 履霜堅冰
   simile as possibly expanded, but the source carries both 履霜堅冰 and
   其來也漸, so the fuller English is faithful.
4. **Automated invariants.** `check_numbers.py` on the bilingual draft: 60
   pairs, 0 unaccounted numbers. `check_structure.py`: paragraph parity 60/60,
   heading shape consistent, glossary drift 0, all 25 note anchors resolve.
   (check_numbers was extended for this book: Traditional 萬/億, X分之Y
   fractions, English "million"/"billion", and several numeral-idioms.)
5. **Term ledger.** `glossary.json` extended with pinyin + attestation for the
   recurring referents (中國國民黨, 三民主義, 國民革命, 中央特科, 格伯武/GPU,
   別動隊, 一黨專政, 土豪劣紳, 巡捕房, 交通部, 偵察, 情報, 非常). Statuses set;
   GPU, KMT, Three Principles, National Revolution, Central Special Branch now
   attested with citations.
6. **Annotate not smooth.** Low-confidence and idiom spans became footnotes
   rather than smoothed away; no bracketed tags survive into the clean prose.
7. **External scholarship.** Checked and cited: Gu Shunzhang's biography and
   1931 defection; GPU/OGPU (1922-34); the 1927 KMT-CCP split; the Zhou and
   Qin-Han offices 司隸/司稽/鄉亭/游徼; the WWII-Pacific forecast (corroborated by
   1941). Sourced to Wikipedia / Baidu Baike / a CIA study; Grok/Grokipedia
   results appeared in searches and were NOT used (standing rule).
8. **Deep audit.** Coverage was 100 percent (every page eye-read), so the
   audit is the whole batch rather than a 3-5 percent sample. Spans given the
   full crop-and-zoom treatment: 河溝/山丘 (p41), 司隸/司稽/鄉亭/游徼 (p36),
   格伯武 (p28), 五百萬金磅 (p35), 百戰百勝 (p35). Estimated residual error rate:
   under 0.5 percent; no dropped numbers, no omissions.

### Flagged for Winston's read-through
- The budget figures on printed p9 (British "secret" fund ~£5,000,000/yr; Japan's
  military = half the budget, its "secret" fund = a third of that) are the
  author's 1933 rhetoric, uncorroborated. Noted as such.
- 別動隊 rendered "special-operations corps" (provisional; not found attested).
- Chapter 1 uses 格伯武 for GPU; Chapter 7 is expected to use 格伯烏. Both are
  glossed to the same referent "the GPU"; confirm the ch7 spelling in that batch.
- The self-referential irony (Gu praising the C.P. apparatus he himself built
  and then betrayed) is footnoted at "it began with the C.P."

## Engineering state (for later batches)
- `scripts/build_reading_epub.py` REWRITTEN for this book: driven by
  `book.json` structure (dict), one XHTML per translated chapter, full
  8-chapter/37-section pending-aware TOC (translated sections deep-linked),
  continuous footnote numbering, refuses to build on any unmatched anchor.
- `scripts/split_bilingual.py` NEW: derives `out/<id>_reading.md` and
  `data/zh/<id>.txt` from one `out/<id>_bilingual.md`, so the shipped prose and
  the parity source cannot drift.
- `scripts/check_numbers.py` extended (see check 4 above).
- `scripts/ocr_crop.py` crop geometry is correct for this book; just run it.
