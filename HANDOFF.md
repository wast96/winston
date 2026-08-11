# HANDOFF — Owl's Castle (梟の城, Shiba Ryōtarō)

Baton for a fresh session. Read this, then `book.json`, then `STYLE.md`.

## Message to paste into the next chat

```
Owl's Castle B01

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md. We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. This is a VERTICAL, right-to-left Japanese book with furigana; it is book #10 on a Chinese-Republican shelf, so authority.json has no names for it yet.

Do Batch B01 = ch01 「おとぎ峠」 (Otogi Pass), PDF pages 7-63 (printed folios 7-63; offset is 0 in this range, folio == render page), end to end per the CLAUDE.md pipeline. This is BATCH 1: it sets the voice and ends at the voice gate.

Setup and OCR (batch-1 engineering):
1. ./setup.sh, THEN install the Japanese OCR packs setup.sh omits: apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert. epubcheck is at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container was recycled).
2. Page furniture is ALREADY measured (see PROGRESS.md): all furniture (running head 梟の城 + arabic folio) is at the TOP; body crop left 0.035 right 0.965 top 0.075 bottom 0.955; model jpn_vert --psm 5. BEFORE OCR, patch scripts/ocr_crop.py for Japanese: (a) despace() must also strip spaces adjacent to kana (hiragana U+3040-309F, katakana U+30A0-30FF), not only Han; (b) do NOT apply strip_folio()/strip_runfoot() (they delete short Japanese dialogue lines ending in 。 and match Chinese 第X章 only; furniture is top-only and cropped, so they are unneeded). scripts/ocr_survey.py already does the correct crop+model and can be a reference.
3. render.py 7 63 --dpi 300; ocr_crop.py 7 63 with the crop/model above; ocr_dual.py for the second read. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process group if a run stalls).
4. indents.py 7 63; assemble.py ch01 7 63 to build data/zh/ch01.txt. find_figures.py 7 63 AND eyeball every page for line art (this novel is text-only so far; record an empty figure list as a deliberate decision).

Translate:
5. Read STYLE.md and the CLAUDE.md register section. Translate to that contract: swift narrative, character-marked dialogue, and Shiba's fourth-wall historical asides each in their own register. Consult glossary.json and authority.json BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi, Nobunaga, Kyoto, Tokugawa). As the major cast appears, write a two-line VOICE SHEET per character into HANDOFF's carry-forward and flag them principal:true in glossary (expected here: 葛籠重蔵 Tsuzura Jūzō, 風間五平 Kazama Gohei, 下柘植次郎左衛門, the disfigured old man of Iga, and any others). Crop-verify every proper name, number, unit designation, and low-confidence span (verify_names.py --auto for OCR disagreements; crop_lines.py for systematic mangles; record every verified reading via apply_fixes.py into data/ocr_fixes.json). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation; verify the unit's FINAL paragraphs against the scan explicitly before shipping.
6. Write out/ch01_reading.md, one paragraph per source line, '## Otogi Pass' as the h1. make_bilingual.py ch01 (positional pairing; run parity FIRST). verify_unit.py ch01 (parity, numbers with --noise data/noise.txt, anchors); check_align.py; check_content.py.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history): early chapters want ~8-15. Likely notes here: Iga and Kōga (the ninja provinces), 天正十九年 = 1591, the Kasagi / Yamashiro-Ōmi border geography and 御斎峠 (Otodo/Otogi Pass), the 伊賀ノ乱 (Nobunaga's 1581 invasion of Iga) and Oda Nobunaga, 樵/杣人 (woodcutters), and any ninja-art term at first appearance. Add via apparatus_merge.py (never a heredoc); glossary rows with status; check_apparatus.py clean.
8. Rebuild the EPUB; qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md.

THEN STOP at the VOICE GATE (do not start B02). Present the built ch01 and ask the commissioner to judge three things: the voice/register, the footnote density (does it catch everything they'd miss, without padding), and the formatting. Attach the EPUB in the chat. On approval, ch01 becomes the FROZEN register reference (check_register.py --ref out/ch01_reading.md from B02 on), and you write the B02 kickoff. Cite printed folios; do not pause for approval mid-batch before the gate.
```

## What is DONE

- **Survey (this session):** whole-book structure recovered and approved.
  book.json carries full English metadata and all 20 units (19 novel sections
  ch01-ch19 + the 解説 afterword ch20, which the commissioner asked to INCLUDE).
  Title approved as **Owl's Castle**. Skeleton EPUB builds; qa_epub PASS;
  epubcheck 5.1.0 clean. Batch plan approved AS-IS (one section per batch, 19
  batches; ch16+ch17 combined; see out/SURVEY.md).
- Nothing translated yet. B01 (おとぎ峠) is next and runs the voice gate.

## Tooling in place (do NOT revert)

- `scripts/find_headings_vert.py` — vertical-text heading detector (columns, not
  rows; furigana filtered by glyph width).
- `scripts/ocr_survey.py` — survey OCR runner (crop + jpn_vert, keeps paragraph
  blanks, no Chinese folio/runfoot strips). Reference for the correct crop/model.
- `STYLE.md` — the prose contract (adapted from the claude/the-stealthy-ones
  contract, with the comma-density/read-aloud test, names-vs-pronouns rule,
  measured-contractions and footnote heuristics folded in from
  claude/lu-xiaofeng-1, tuned to Shiba). Read it every batch.
- Body OCR for the whole book already exists at data/txt_survey/ (jpn_vert,
  survey quality) — useful for structure/search, but batches re-OCR at 300 dpi
  for translation.

## Do-not-revert / must-do for batches

- **setup.sh gap:** it installs only Chinese tesseract packs. Every batch must
  add tesseract-ocr-jpn + tesseract-ocr-jpn-vert.
- **ocr_crop.py needs Japanese patches** before first use (kana despace; skip
  the Chinese strip_folio/strip_runfoot). See the kickoff.

## Renderings settled / carry-forward

- Names: Hepburn + macrons; conventional English forms for well-known figures
  (Hideyoshi, Nobunaga, Kyoto, Tokugawa, Ishida Mitsunari). glossary.json is
  empty; authority.json has no Japanese entries (first Japanese book on the
  shelf). Decide each name in glossary before romanizing; feed decisions back
  into authority.json on completion.
- **Voice sheets:** none yet. B01 must create them for the major cast as they
  appear.
- Provisional English section titles are in book.json; settle them at/after the
  voice gate.

## Where the story stands

Not started. Opening (ch01, おとぎ峠): Iga, spring of 天正十九年 (1591); a
disfigured old man of Iga and a woodcutter on a mountain pass. The novel's two
poles are 葛籠重蔵 (Tsuzura Jūzō), the Iga ninja bent on assassinating Hideyoshi,
and 風間五平 (Kazama Gohei), his fellow disciple who quit the shadow arts.

## Next-batch scope

- **B01 = ch01 おとぎ峠 / Otogi Pass**, PDF 7-63, printed folios 7-63 (57 pp.).
  Offset 0 here. Ends at the voice gate.

## Open traps and environment

- **Page-offset wrinkle** (does not affect B01): folio == render page for
  folios 7-302 and 425-660, but +2 render pages across folios ~338-397. The
  batches crossing that span (B09-B13) must read folios off the scan and build
  data/pagemap/ accordingly; watch for a possibly missing leaf around folios
  397-425.
- **The scan's first TOC leaf is missing**; structure was rebuilt from the body
  (already done, in book.json).
- OMP_THREAD_LIMIT=1 mandatory for tesseract; verify pgrep -c tesseract == 0.
- Container is ephemeral: commit and push to claude/owls-castle at every point.
