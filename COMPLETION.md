# COMPLETION REPORT — The Whistling Wind (风萧萧) by Xu Xu

The annotated English translation of Xu Xu's 1943 novel 风萧萧 (*The Whistling
Wind*) is **complete**. All thirteen approved batches are done; the cumulative
EPUB `out/The Whistling Wind.epub` contains the whole book, its apparatus, and
the back matter, and passes QA across the full spine.

## Final counts

- **60 units translated**, ch00–ch59: front matter (ch00, *About the Author*)
  + the novel's **58 numbered chapters** (一..五十八, ch01–ch58) + the appendix
  (ch59, *Impressions of Xu Xu*, 徐訏印象).
- **~236,000 source characters** rendered in full.
- **103 footnotes** (continuous numbering, every reference with a body and a
  backlink, sequential in reading order).
- **209 glossary rows** across book / people / organizations / places / terms
  (one decided rendering per referent for the whole book).
- Back matter: **Translator's Note**, **Glossary of Names and Terms**, and the
  translated **Colophon** (from the source's imprint leaf).
- EPUB: cover, title page, fully hyperlinked nested TOC (part → chapter →
  section), 60 chapter documents, Notes, back matter, Colophon — 73 files,
  66 spine items.

## Batches

| Batch | Units | Chars | Status |
|---|---|---|---|
| B01 | ch00–ch08 | 18,512 | DONE |
| B02 | ch09–ch14 | 19,469 | DONE |
| B03 | ch15–ch17 | 16,230 | DONE |
| B04 | ch18–ch21 | 19,962 | DONE |
| B05 | ch22–ch25 | 18,788 | DONE |
| B06 | ch26–ch31 | 20,716 | DONE |
| B07 | ch32–ch36 | 18,411 | DONE |
| B08 | ch37–ch41 | 17,945 | DONE |
| B09 | ch42–ch45 | 14,344 | DONE |
| B10 | ch46–ch48 | 17,009 | DONE |
| B11 | ch49–ch52 | 17,733 | DONE |
| B12 | ch53–ch57 | 20,620 | DONE |
| B13 | ch58–ch59 | 15,635 | DONE (+ Colophon + whole-book QA) |

## Whole-book QA (final pass)

- `qa_epub.py "out/The Whistling Wind.epub"`: **PASS** — 73 files, 67 documents,
  103 references / 103 bodies / 103 backlinks, all links resolve.
- `check_structure.py --config` over all 60 units: **ALL STRUCTURAL CHECKS PASS**
  — paragraph parity OK on every unit; 103 note anchors resolve, 0 unresolved;
  heading shape uniform (1 distinct shape); glossary drift 0.
- Verbatim quotation confirmed batch by batch (joined source blockquotes ==
  joined source paragraphs, whitespace-stripped) — no source paragraph dropped
  or paraphrased anywhere.
- `check_numbers.py --noise data/noise.txt`: every unit clean (0 unresolved) as
  built; `data/noise.txt` carries the full B01–B13 project noise accumulation.
- TOC fully linked (0 "pending" markers); notes 1..103 sequential; Colophon
  present in spine and navigation.

## Method (per CLAUDE.md)

Translated from the digital source EPUB (no OCR). Each batch: an aligned
bilingual QC file quoting the source **verbatim**, from which the reading text
and the parity source were mechanically derived; the invariant checks
(`check_numbers`, `check_structure`) run every batch; footnotes at reference
density keyed to verbatim anchors; a term ledger (`glossary.json`) fixing one
rendering per referent; sampled blind double-translation and back-translation on
argumentative/lyrical passages; and a 3–5% random deep audit per batch. Real-
world references were checked against Wikipedia / Baidu Baike / academic sources
(never LLM-generated references). Genuine ambiguities and source corruptions
were footnoted or normalized to sense and **listed** in `PROGRESS.md`, never
silently smoothed; no bridging text was invented.

## Residual provisional readings a reader should know about

These are flagged `provisional` in the glossary (romanizations not found
attested in English scholarship) or are otherwise worth a reader's awareness:

- **The three principal women's names are project style calls** (`decided`):
  **Bai Ping** (白苹), **Mei Yingzi** (梅瀛子), **Helen** (海伦, an American). The
  narrator is unnamed throughout.
- **Provisional romanizations**: **Manfield** (曼斐儿, the German-American mother
  and daughter; an anglicization, not an attested spelling), **Dr. Philip**
  (费利普), **Cishan** (慈珊), and the boat-family names introduced late (**Bingfu**
  丙福, **Xiao Heizi** 小黑子). Japanese names carried Anglo/Hepburn forms where the
  source's kana were not recoverable from the Chinese (e.g. **Miko**, **Miyama
  Yoshiko**, the **Hōdōbu** press bureau).
- **Appendix (ch59) minor figures** flagged `provisional`: **Liu Bo** (刘波),
  **Xiao Tong** (萧铜), **Ge Fucan** (葛福灿), **Ge Yuan** (葛原) — pinyin, no widely
  used English form located. Major figures use their attested English names
  (C. T. Hsia, Lin Yutang, Lu Xun, Eileen Chang, Jin Yong / Louis Cha, Chip
  Tsao, Joseph S. M. Lau, King Hu, Xiao Si / Lo Wai-luen).
- **One preserved-and-corrected factual error** in the source (not the
  translation): the ch59 essayist calls Keynes a "Jewish economist" and the
  1950s framer of British policy; note 103 records that this is **contradicted**
  by scholarship (Keynes was Congregationalist/agnostic and died in 1946). Kept
  visible and corrected, per the no-smoothing rule.
- **Colophon date**: the source imprint prints "1944年（民国三十一年）", but 民国三十一年
  is 1942; 1944 = 民国三十三年. The colophon gives the corrected 民国三十三年（一九四四年）;
  the discrepancy is recorded in `PROGRESS.md` (B13).
- **Recurring digitization glitches** in the simplified-character source (wrong-
  but-adjacent characters, stray inserted glyphs, mismatched guillemets) were
  rendered to plain sense throughout and are itemized per batch in `PROGRESS.md`;
  only genuine reading *uncertainty* (never a mechanical typo) was footnoted.

## Files of record

- `out/The Whistling Wind.epub` — the deliverable.
- `out/<id>_reading.md` (ch00–ch59) — the per-unit correction surface.
- `book.json`, `notes.json` (103), `glossary.json` (209), `back_matter.json`
  (colophon), `figures.json` — all current.
- `PROGRESS.md` — the batch-by-batch QC record (checks run and what they found).
- `data/noise.txt` — the project number-check noise (B01–B13).
