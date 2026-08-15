# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

## THE NOVEL IS COMPLETE

All nineteen novel sections (ch01 through ch19) are translated, annotated, and
built into out/owls-castle.epub. The completion report is COMPLETION.md; read
that first. There is no next batch to kick off. Further work is a corrections
pass (see the corrections workflow in CLAUDE.md), or, if the commissioner
wants it, the one remaining untranslated section: ch20 解説, the afterword.

- Deliverable: out/owls-castle.epub, committed with git add -f on branch
  claude/owls-castle. qa_epub PASS, epubcheck 0/0/0/0.
- 19 of 20 sections translated; 130 notes; 0 figures (text-only throughout, a
  recorded decision); glossary 113 people / 113 places / 30 terms.
- The title page and TOC honestly report "19 of 20 sections translated." The
  only untranslated section is ch20, the third-party afterword.

## The one open decision: ch20 解説 (Afterword by Muramatsu Tsuyoshi)

Folios 653-660. It is a critical essay ABOUT the novel by the critic Muramatsu
Tsuyoshi, not Shiba's own text. Translating a third-party afterword is the
commissioner's call. If they want it, it becomes B20; the optional kickoff is
below. If not, the novel ships as it stands.

## If the commissioner wants ch20 (optional B20 kickoff)

```
Owl's Castle B20

Read CLAUDE.md, then COMPLETION.md, then this HANDOFF, then book.json and STYLE.md. The novel (ch01-ch19) is COMPLETE in out/owls-castle.epub. This batch adds ch20 解説（村松剛）/ Afterword by Muramatsu Tsuyoshi, folios 653-660 (== PDF; offset 0 holds to the end of the book, confirmed at end of B19). It is a third-party critical essay, so treat register accordingly: this is a modern critic writing appreciative literary criticism, not Shiba's period narrative. Do it end to end per the CLAUDE.md pipeline: render.py 653 660 --dpi 300; ocr_crop.py 653 660 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 653 660; hand-transcribe from the page images into data/zh/ch20.txt (chunk-file method, scratchpad/zh + scratchpad/en, python-assembled with the zip-alignment assert); crop-verify every name (the essay names other authors, works, and critics — Sarutobi Sasuke, Tachikawa Bunko, Murayama Tomoyoshi, etc.); glossary/authority for any recurring name; footnote the writers/works/critical terms a Western reader would miss; out/ch20_reading.md titled '## Afterword'. Then verify_unit ch20; check_structure --pairs; check_align; qc_entities; check_content; check_register --ref out/ch01_reading.md (expect a NON-fiction register, likely low contractions — an essay, formal by design, not a defect); apparatus_merge notes; build_reading_epub.py (it will then report 20 of 20); qa_epub green; epubcheck. Update the title page to "complete" (all 20 sections). Then it is a whole-book corrections pass from there. Cite printed folios. Deliver the EPUB in chat and paste the COMPLETION update.
```

## What is done (one line per batch, do not redo)

- Survey approved; 20-section structure in book.json; metadata set; skeleton EPUB.
- Offset history (READ folios, do not compute): 0 for folios 7-325; +2 from
  folio 326 (PDF 328) through 403 (PDF 405); a 1-leaf scan gap dropped printed
  404-405; back to 0 from folio 406 onward, unbroken to the end (confirmed
  through PDF 652 in B19).
- B01 ch01 おとぎ峠 / Otogi Pass (7-63): COMPLETE, approved at the voice gate.
  ch01 is the FROZEN register reference. 523 paras, 17 notes.
- B02 ch02 濡れ大仏 / The Rain-Soaked Buddha (64-89): 276 paras, 6 notes.
- B03 ch03 白い法印 / The White Hōin (90-123): 385 paras, 16 notes.
- B04 ch04 木さると五平 / Kisaru and Gohei (124-148): 286 paras, 5 notes.
- B05 ch05 羅刹谷 / Rakshasa Valley (149-166): 152 paras, 6 notes.
- B06 ch06 忍び文字 / The Ninja Cipher (167-206): 312 paras, 5 notes.
- B07 ch07 聚楽 / Juraku (207-236): 280 paras, 5 notes.
- B08 ch08 京の盗賊 / The Thief of the Capital (237-302): 580 paras, 6 notes.
- B09 ch09 甲賀ノ摩利 / Mari of Kōga (302-338): 324 paras, 11 notes.
- B10 ch10 奇妙な事故 / A Strange Accident (338-373): 312 paras, 4 notes.
- B11 ch11 伊賀ノ山 / The Hills of Iga (373-397): 230 paras, 6 notes.
- B12 ch12 吉野天人 / The Celestial Maiden of Yoshino (397-425): 212 paras, 10
  notes. Contains the permanent 404-405 scan gap, handled honestly, no bridging.
- B13 ch13 水狗 / The Water Dog (425-456): 245 paras, 6 notes.
- B14 ch14 修羅 / Carnage (456-508): 446 paras, 6 notes.
- B15 ch15 五三ノ桐 / The Paulownia Crest (508-566): 440 paras, 5 notes.
- B16 ch16 甘南備山 / Mount Kannabi (566-583): 132 paras, 4 notes.
- B17 ch17 尾行 / The Shadowing (584-591): 44 paras, 6 notes.
- B18 ch18 石田屋敷 / The Ishida Mansion (591-608): 122 paras, 3 notes.
- B19 ch19 伏見城 / Fushimi Castle (608-652): 310 paras, 3 notes. FINAL chapter.
  All checks green; whole-book completion protocol run (see COMPLETION.md).

## Tooling and conventions in place (do NOT revert)

- Sectioned glossary (people/places/terms): add rows directly (Edit or json
  load/dump ensure_ascii=False indent=2), NOT via apparatus_merge (which
  flattens). Notes/figures merge fine via apparatus_merge.
- ocr_crop.py has kana in the despace class and --no-furniture-strip; ocr_dual.py
  is the Japanese second read; check_content/qc_entities skip non-dict glossary
  sections and subsume shorter-key spans. check_content is the authoritative
  displacement check; qc_entities over-flags place-keys inside common words.
- data/noise.txt: name/idiom numerals, longest-literal-first, one comment each.
  B19 added 五右衛門, 三太夫, 五山桐, 十重二十重, 千載一遇, 何百, 八釜, 十王, 三黄.
- Note anchors: verbatim BODY-prose substrings, LITERAL Unicode (ō, ā, straight
  ASCII quotes/apostrophes); note bodies use numeric char refs or literal Unicode,
  never named HTML entities. Author the batch as a JSON file, run apparatus_merge.
- Method: hand-transcribe from the 300dpi full-page images (assemble.py WELDS and
  OVERWRITES on this vertical text, so it is NOT used); chunk-file zip-alignment
  (scratchpad/zh + scratchpad/en, python-assembled with an equal-length assert
  and a quote-line check). scratchpad/crop.py and topstrips.py read furigana and
  faint running-head folios (re-create from COMPLETION/PROGRESS if the container
  recycled).
- Spelling locale is AMERICAN (ch01, the approved reference, is American). B19's
  completion sweep cascaded all drifted British forms to American book-wide; the
  ledger reads 0 British / 130 American. Keep it American in any corrections.
- Pre-existing checker-regression FAIL "hook stands down on template stub" is
  unrelated; leave it. setup.sh omits the Japanese tesseract packs; install
  jpn + jpn_vert manually. Re-fetch epubcheck if the container recycled.

## Residual items for a corrections pass (none blocking)

- 治部少輔 for Ishida Mitsunari appears as both "Jibu-no-shō" and "Jibu-no-shōyū"
  across earlier chapters; harmonize to one if the commissioner prefers.
- Unused glossary form "Imai Sōkun" (今井宗薫) never appears in prose; prune if
  wanted.
- These are cosmetic; the EPUB is store-ready as it stands.

## Where the story ends (ch19)

Jūzō penetrates Hideyoshi's Fushimi residence and stands over the sleeping
Taikō, but cannot kill a helpless old man; he wakes him, they talk, and Jūzō,
disgusted by Hideyoshi's arrogance, beats him and leaves without killing. Gohei,
following, is caught in the residence, gives the false name Ishikawa Goemon, and
is executed under it. Shiba's closing device identifies the invented spy with
the historical Goemon boiled at Sanjōgawara in 1594. Jūzō retires to a hermitage
on Otogi Pass with Kohagi, selling wild herbs, and slowly dissolves back into
the mountains as the age of Sekigahara passes him by. The novel ends where it
began, at Otogi Pass.
