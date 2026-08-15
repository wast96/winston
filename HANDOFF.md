# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B19

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B19 = ch19 「伏見城」 (Fushimi Castle), printed folios 608-652 — the FINAL novel chapter (ch20 解説 is a third-party afterword whose translation is the commissioner's separate call). Do it end to end per the CLAUDE.md pipeline. OFFSET IS 0: printed == PDF (folio 608 = PDF 608, CONFIRMED at the end of B18 by reading the running head of every page across PDF 591-609; no duplicate leaf, no gap; offset has been 0 unbroken since folio 406). Do NOT assume — READ the folio off the running head of EVERY rendered page across this span to confirm printed == PDF holds, and watch for any duplicate leaf or gap. The running heads are VERY faint: use scratchpad/topstrips.py FIRST LAST to stack the top strips of a page range into one image (top strip 0.0 0.015 1.0 0.072 at zoom ~9, autocontrast). book.json: ch20 opener 解説（村松剛） (Afterword) at printed 653 == PDF 653. Build data/pagemap/ch19.json for the span (ch17.json / ch18.json are the format model: entries {printed, pdf, body_paragraph} where body_paragraph is the 0-based index into data/zh/ch19.txt body paragraphs, title excluded; keep indices UNIQUE — the builder inverts the list to {body_paragraph: folio}, so two folios mapping to the same paragraph collide).

ch19 opens MID-608: ch18 石田屋敷's TAIL occupies the top of folio 608 (paras through the line 「これは佳絶な檻であろうの。重蔵とやらは、武芸には秀でていても、ものの福を知らぬげな男であるわい」 and the closing narration と、はじめて、左近らしいつややかな好色の笑い声をあげた。, ALL translated in B18), then the 伏見城 title sits partway down 608, and ch19's BODY begins after it. DO NOT re-translate the ch18 spillover; START ch19 at 五平が、亭主に命じた二階の部屋と、重蔵が旅絵師の姿で潜伏している旅籠の部屋とは、狭い小路を隔てて、まむかいに庇を突きあわしている。（Gohei's second-floor room, which he ordered from the innkeeper, and the inn room where Jūzō lies hidden in a travelling-painter's guise, face each other eave to eave across a narrow lane — the ch17/ch18 threads converge: Gohei watching Jūzō's inn). Map folio 608 to ch19 body_paragraph 0 (the 五平が opener), and START ch19's first pagemap entry there. BEFORE translating, read the final two pages of ch18's English (the tail of out/ch18_reading.md) so the voice carries — ch18 ends on SHIMA SAKON's lecherous laugh after agreeing to help Kohagi "cage" or, failing that, kill Jūzō; ch19 cuts back to GOHEI staking out Jūzō's inn (the surveillance of ch17 resumed).

ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch19_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write; keep the grave uncontracted line only for deliberately-formal registers. Priors: ch05/ch08 both needed a whole contraction pass afterward; ch06 formal-by-design 0.74x, ch09 1.21x, ch10 2.31x, ch11 1.62x, ch12 1.86x, ch13 1.34x, ch14 1.54x, ch15 0.60x (court/interrogation, formal), ch16 1.98x (night-ambush action), ch17 3.00x (contracted street/inn dialogue), ch18 0.68x (court/intrigue, formal by design). ch19 is the CLIMAX (Gohei vs Jūzō, the move on Fushimi Castle, Kohagi) — action + confrontation; contract the natural speech, expect a mid-to-high register.

ch19 IS THE LAST NOVEL CHAPTER — follow the CLAUDE.md last-batch protocol IN ADDITION to the normal pipeline: (a) whole-book reconciliation sweep (check 12: check_reconcile.py for cross-chapter drift, grep-count ~20 decided renderings, notes at FIRST appearance); (b) any back matter the book has (there is none declared — book.json back_matter is []; the 解説 afterword is ch20, NOT back matter); (c) write COMPLETION.md from the template (sampled error rate, residual uncertainties) INSTEAD of another handoff; (d) commit the final EPUB itself (git add -f out/owls-castle.epub — branches outlive containers, chat attachments do not); (e) rewrite HANDOFF.md to say the novel is COMPLETE (18→19 chapters translated; ch20 解説 pending the commissioner's decision) and further work is a corrections pass; (f) feed ch19's decided renderings back into authority.json. FLAG the ch20 解説 decision to the commissioner in the final chat reply (translate the afterword, or ship the novel as-is?). The title-page/TOC "complete" state: build_reading_epub.py reports "19 of 20 chapters translated" — the novel proper is done; ch20 is the only untranslated section and it is an afterword.

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). ALSO: setup.sh installs pymupdf under a name the scripts import as `fitz`; if `import fitz` fails, run `pip install -q pymupdf numpy opencv-python-headless`. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled). The pre-existing checker-regression FAIL "hook stands down on template stub" is unrelated; leave it.
2. OCR: render.py 608 654 --dpi 300 (folio 608 = PDF 608; render a couple pages past the expected ch20 opener 653 to catch it and any drift); then ocr_crop.py 608 654 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 608 654. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls). CHECK each rendered page's running-head folio: expected folio == PDF. A folio that repeats the previous folio is a double-feed (skip it); a SKIPPED folio is a gap (re-map from there).
3. find_figures.py 608 654 AND eyeball every page for line art (ch01-ch18 were all text-only; if ch19 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by READING the rendered page images directly (data/png/p0NNNN.png — files are named p0608.png etc., 4-digit) and hand-build data/zh/ch19.txt as a corrected, paragraph-aligned transcription (the parity surface). scratchpad/crop.py 6x-renders a page-fraction rectangle (crop.py PAGE x0 y0 x1 y1 [zoom]; PAGE 1-based; fractions of the full page; reads furigana AND faint running-head folios cleanly). scratchpad/topstrips.py FIRST LAST stacks running-head strips of a page range into one image for fast folio reading. Re-create crop.py / topstrips.py if the container recycled (bodies in "Tooling in place" below). NOTE: the full-page images at 300dpi (~1112x1725) are LEGIBLE enough to transcribe directly, cropping columns only for interleaved dense pages and uncertain names/furigana (the B12-B18 method — far faster than half-page crops). Interleaved narration/dialogue mis-orders from the full page — crop the columns and read right-to-left, top-to-bottom literally (READING ORDER IS STRICT RTL COLUMN-BY-COLUMN; a dialogue attribution 「…」と… sits in its own column); treat each 「…」 line and each narration run as its own paragraph. On a DENSE page, cross-check column order against the RAW OCR (data/txt/p0NNN.txt) — it reads the page as a linear column flow and, garbles aside, disambiguates which sentence follows which (the B14 method). Force-add data/zh/ch19.txt (data/zh/ is gitignored). The ch19 opener shares folio 608 with ch18's tail — START at 五平が (right after the 伏見城 title line), NOT at the top of 608. Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch20 opener folio (653) and check whether ch19's tail spills onto it, and make sure the (possible) ch20 work does not re-translate any spillover. COVERAGE cross-check after transcribing: extract every 3+-kanji compound from the raw data/txt OCR (over the ch19 PDF span, excluding the ch18 tail on 608 and any ch20 spillover on 653+) and confirm each appears in your HAND data/zh/ch19.txt — garbles are expected; a clean meaningful compound that is absent is a real drop to fix (python one-liner over data/txt with a Counter of [一-鿿]{3,}).
   WATCH THE NEWLINE TRAP (bit B13-B16): the chunk-file method sidesteps it — write each ~6-page chunk as scratchpad/zh/cNN.txt + scratchpad/en/cNN.txt (ONE paragraph per line, both sides), verify per-chunk line counts match, then assemble both files with a python script that asserts equal length and prints any quote-line alignment mismatch (this makes the zip-alignment automatic). check_structure counts LINES so a compensating merge+split passes parity while the middle is displaced; only the zip catches it. ch19 is LONG (~44 folios) — expect 5-8 chunks.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Ieyasu/Tokugawa/Kyoto/Yoshino/Fushimi). Principal cast and majors are decided in glossary.json; reuse unchanged and record in PROGRESS which rows you reused. Shima Sakon (島左近/左近→Shima Sakon/Sakon; 勝猛→Katsutake) was ADDED in B18 — reuse it. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans. Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False indent=2, or the Edit tool — the B04-B18 method, NOT apparatus_merge which flattens the glossary). AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter. Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch19_reading.md, settle the English title at translation ('## Fushimi Castle' — 伏見城 = Hideyoshi's Fushimi stronghold, already glossaried/noted; Jūzō's target). Footnote it on a relevant BODY phrase if the sense needs it, per the ch13-18 title-note precedent. Add a ch19 entry to data/checks.json (docs + sources). make_bilingual.py ch19 (parity FIRST). Then run: verify_unit.py ch19; check_structure.py --pairs data/zh/ch19.txt out/ch19_reading.md; check_align.py ch19; qc_entities.py out/ch19_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch19_reading.md. (qc/content want the rendered name once per paragraph the character appears in — do a name-survival pass over any pronoun-only paragraph, as in B10-B18; check_content is authoritative, qc_entities over-flags place-keys inside common words, e.g. 甲斐/Kai inside 生き甲斐/甲斐がある.)
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch18 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku/Genki dating, the Iga Rebellion, Honnō-ji AND Akechi Mitsuhide & Yamazaki, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office(治部少輔)/太閤(Taikō)/内府(Naifu=Ieyasu)/右府 titles, Sakai the free-city, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu/Hideyori, Nanban, the Nara Great Buddha AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours & 半刻/小半刻/四半刻 & the night-watches, Aizen Myō-ō, the wakō/bahan ships & Luzon, the measures(shaku/sun/chō/koku/ri/ken/kin/tsubo/jō/kan/kanmon), rappa/shinobi/jōnin/genin, jizamurai/gōshi, くノ一/kunoichi, 忍び文字/shinobi-moji, Marishiten, Yodo-gimi/Odani, Rokkaku/Sasaki Yoshikata & the Sasaki of Ōmi & Kannon-ji 1568, the 1487 Magari campaign, the fifty-three houses of Kōga, Kōga Saburō, the Odawara campaign & the Hōjō, Nagoya castle in Hizen, Hattori Hanzō, the Jurakudai, the go-bugyō, the Iga-goe, Miyamoto Musashi & the Yoshioka, Kashima/Katori & Bokuden, 陽忍/陰忍, the Bon send-off, shōchū, the Kyoto-to-Kōga route, the Buddhist precepts / Mahāsāṃghika Vinaya / Buddhabhadra, Empress Jitō's no-kill decree, 化生/keshō, the Mochizuki house of Kōga, Ren (Kisaru's given name), Yoshino & its cherry cult, Maeda Toshiie, the 1595 Hidetsugu purge, the Zaō Hall/Kimpusen-ji, the Saigyō hermitage, Noh/takigi-nō/Kanze & 吉野天人, the owl-whistle(梟笛), the sasumata, Mimi of Nabari, the kozuka, the kuji/Samaya-mudra/mantra counter-spell, Fushimi Castle, the Genki era, Maeda Gen'i & the Kyoto magistracy, Hachisuka Masakatsu, Ise no Saburō Yoshimori & Yoshitsune, Benzaiten, 修羅/Shura, the Nigatsu-dō folding stand, the Awataguchi sword school, the 五三ノ桐 paulownia crest, 百八/hundred-and-eight, クナイ/kunai, 末法/mappō, 般若/prajñā, Tenjiku=India; B16's 甘南備/kannabi, 木津川/Kizu-gawa, 八幡/Hachiman, 仮祝言/kari-shūgen; the Gion Yasaka shrine (ch04); B17's 月代/sakayaki, 鐚銭/bita-sen, 歌舞伎/kabukimono, 永楽銭/Eiraku-sen, 鬼門/kimon, 尾行/bikō; AND the B18 first-appearances: 島左近/Shima Sakon (Mitsunari's chief retainer, 鬼左近, d. Sekigahara — glossaried AND footnoted), 枯れ山水/kare-sansui (the dry-landscape garden), and the "edible walls" siege-ration conceit (鰯/するめ in the wall-clay, cross-ref Katō Kiyomasa's Kumamoto). Note only ch19's NEW first-appearances (likely candidates: the specific architecture/defenses of 伏見城/Fushimi Castle if a fresh gloss beyond the existing Fushimi note is wanted; 旅絵師/travelling-painter or 放下師/hōkashi street-entertainer disguises; any new office/person/place the assault crosses; the ninja infiltration tools/techniques). Anchor notes to BODY phrases (verbatim substrings), not heading-only text. Add via apparatus_merge.py (batch JSON file with a top-level "notes" key, numeric char refs OR literal chars in bodies — NEVER a heredoc; ANCHORS must use LITERAL Unicode matching the reading text, e.g. ō/ā/ñ and STRAIGHT ASCII apostrophes/quotes as the reading files carry them, NOT char refs). check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, the renderings reused/added), INCLUDING the confirmed folio-to-PDF map for this span (should be printed == PDF throughout — confirm), and the data/pagemap/ch19.json you built. Then run the LAST-BATCH protocol (whole-book reconciliation, COMPLETION.md from the template, commit out/owls-castle.epub with git add -f, feed renderings into authority.json, rewrite HANDOFF to COMPLETE).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND (because this is the last novel chapter) paste the COMPLETION summary and FLAG the ch20 解説 (Afterword by Muramatsu Tsuyoshi, folios 653-660) translate-or-not decision to the commissioner. If the commissioner wants ch20, that becomes B20; otherwise the novel ships as-is. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 20-section structure in book.json; metadata set; skeleton EPUB built; page
  furniture measured (crop L0.035 R0.965 T0.075 B0.955; model jpn_vert psm5).
- **Offset history (READ folios, do not compute):** 0 for folios 7-325; **+2 from folio 326
  (PDF 328) through folio 403 (PDF 405)**; a **1-leaf scan gap dropped printed folios 404-405**
  (MISSING from the scan), re-mapping the offset back to **0 from folio 406 (PDF 406) onward**.
  **printed == PDF CONFIRMED unbroken through folio 609 (end of B18's rendered span).** It should
  hold to the end of the book — confirm by reading running heads each batch.
- **B01 = ch01 おとぎ峠 / Otogi Pass (folios 7-63): COMPLETE, approved at the voice gate.**
  ch01 is the FROZEN register reference. 523 paragraphs, 17 notes.
- **B02 = ch02 濡れ大仏 / The Rain-Soaked Buddha (64-89): COMPLETE.** 276 paras, 6 notes.
- **B03 = ch03 白い法印 / The White Hōin (90-123): COMPLETE.** 385 paras, 16 notes.
- **B04 = ch04 木さると五平 / Kisaru and Gohei (124-148): COMPLETE.** 286 paras, 5 notes.
- **B05 = ch05 羅刹谷 / Rakshasa Valley (149-166): COMPLETE.** 152 paras, 6 notes.
- **B06 = ch06 忍び文字 / The Ninja Cipher (167-206): COMPLETE.** 312 paras, 5 notes.
- **B07 = ch07 聚楽 / Juraku (207-236): COMPLETE.** 280 paras, 5 notes.
- **B08 = ch08 京の盗賊 / The Thief of the Capital (237-301, tail on 302): COMPLETE.** 580 paras, 6 notes.
- **B09 = ch09 甲賀ノ摩利 / Mari of Kōga (302-337, tail on 338): COMPLETE.** 324 paras, 11 notes.
- **B10 = ch10 奇妙な事故 / A Strange Accident (338-372, tail on 373): COMPLETE.** 312 paras, 4 notes.
- **B11 = ch11 伊賀ノ山 / The Hills of Iga (373-396, tail on 397): COMPLETE.** 230 paras, 6 notes.
- **B12 = ch12 吉野天人 / The Celestial Maiden of Yoshino (397-403 + 406-424, tail on 425):
  COMPLETE.** 212 body paragraphs (incl. one scan-gap marker), 10 notes. 1-LEAF SCAN GAP: printed
  folios 404-405 are MISSING (honest gap, no bridging invented).
- **B13 = ch13 水狗 / The Water Dog (425-455, tail on 456): COMPLETE.** 245 body paragraphs, 6 notes.
- **B14 = ch14 修羅 / Carnage (456-507, tail on 508): COMPLETE.** 445 body paragraphs, 6 notes.
- **B15 = ch15 五三ノ桐 / The Paulownia Crest (508-565, tail on 566): COMPLETE.** 440 body paragraphs, 5 notes.
- **B16 = ch16 甘南備山 / Mount Kannabi (566-583; opener mid-566, ends on 583): COMPLETE.** 132 body
  paragraphs, 4 notes.
- **B17 = ch17 尾行 / The Shadowing (584-590, tail on 591): COMPLETE.** 44 body paragraphs, 6 notes.
- **B18 = ch18 石田屋敷 / The Ishida Mansion (591-607, tail spills onto 608): COMPLETE.** 122 body
  paragraphs, 3 new notes (book total 127). All checks green (parity 122|122, numbers 0 unresolved with
  noise +2 [一万五千, 劫億] and two English fixes [194000 spelled form, 零→"close to zero"], check_content
  clean after 7 name-survival fixes, qc 0 misses, check_align 5 declared ratio-inflated exceptions,
  register 0.68x court/intrigue formal-by-design within tolerance, check_apparatus clean, qa_epub PASS,
  epubcheck 0/0/0/0). Built data/pagemap/ch18.json (18 entries, printed==PDF 591-608). NO figures. THREE
  new glossary rows: 島左近/Shima Sakon, 左近/Sakon, 勝猛/Katsutake. ch18 opens MID-591 (its own opener
  その時刻より少し前… after the ch17 tail + 石田屋敷 title) and its TAIL spills onto 608 (through
  「…好色の笑い声をあげた。」) before the 伏見城 (ch19) title. Kohagi returns to Komatsudani and dismisses
  Dokutan, then infiltrates the Ishida mansion at night and wins Shima Sakon's aid: she will try to "cage"
  Jūzō (with Sakon's men as beaters), but if he nears Hideyoshi she kills him herself.

## ch01 corrections made earlier (do NOT undo)
1. ch01's dropped final two paragraphs restored in B02; ch01 parity is 523 | 523.
2. ch01's Great Buddha note corrected in B02 to the NARA Tōdai-ji Vairocana (roofless since
   Matsunaga burned it 1567), not Hideyoshi's Hōkō-ji. In B03 Hideyoshi's OWN Great Buddha
   (方広寺大仏, Kyoto Hōkō-ji) appears and is footnoted as DISTINCT; ch05/ch08 京の大仏/方広寺
   is Hideyoshi's Hōkō-ji again (cross-ref).

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana in the despace class; `--no-furniture-strip` skips the Chinese
  strip_folio/strip_runfoot. Furniture here is top-only, cropped.
- `ocr_dual.py`: Japanese second read (jpn_vert psm5 on grayscale + Otsu variant).
- `check_content.py` / `qc_entities.py`: skip non-dict glossary sections; subsume a shorter
  glossary key covered by a longer matched key at the same span. qc_entities is case-insensitive
  and accepts the first OR last word of a multi-word `en`; check_content needs the EXACT `en`
  present (substring) and only uses `en` that are Capitalised, slash-free and >= 4 chars.
  **check_content is the authoritative displacement check; qc_entities over-flags a place-key
  that sits inside a common word (B13 甲斐/Kai inside 年甲斐; B15 甲斐 inside 生き甲斐/甲斐がある).**
- `check_numbers.py` (`--noise data/noise.txt`): parses English number-words including "a hundred",
  "one hundred and twenty thousand", "forty thousand", "five million". It does NOT compose a
  TEENS+thousand spelled form ("fifteen thousand" parses to 15, not 15000 — noise the source 一万五千
  and keep the English), nor bare compounds like "a hundred and eight" (108). Note "a hundred and X
  thousand" fails but "one hundred and X thousand" parses (use the "one hundred" form, matching the
  ch08 house style). Fix a real quantity in the ENGLISH where a parseable spelled form exists; noise
  only the genuinely unparseable compounds and the numerals-inside-names.
- `data/checks.json`: the {docs, sources} config. ch01-ch18 in.
- `data/noise.txt`: check_numbers noise. B13 二十代; B14 八の字/四つ這い; B15 三千六百万/百八/三村/三角/八幡/
  五条; B17 八坂神社/四明岳; **B18 一万五千 (15,000 koku, Sakon's stipend — teens+thousand unparseable) /
  劫億 (gō-oku, Buddhist boundless-time, 億 idiomatic).** 四条/Shijō was already in from ch08. Extend per
  its header, longest literal first, one comment line each; never noise a real quantity you dropped.
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens glossary
  rows to the ROOT, so since B04 add glossary rows DIRECTLY into the sections (Edit tool, or json
  load/dump ensure_ascii=False indent=2). Notes and figures merge fine via apparatus_merge (batch
  file needs a top-level "notes"/"figures" key — {"notes": {"chNN": [...]}}).
- **Note anchors:** must be verbatim substrings of the BODY prose (a title-meaning note is anchored
  to a relevant body phrase — ch13-17, and ch18's Shima-Sakon/garden/edible-wall notes are on body
  phrases). **ANCHORS use LITERAL Unicode** matching the reading text (ō, ā, ñ, AND straight ASCII
  apostrophes/quotes — the reading files stay plain ASCII, typographized only at render, so anchor an
  apostrophe as ' NOT &#8217;), NOT numeric char refs. Note BODIES: literal Unicode is fine OR numeric
  character references; only NAMED HTML entities (&nbsp; &mdash;) are rejected. Author the notes batch
  as a JSON FILE (Write tool) and run apparatus_merge.py on it — never a heredoc.
- **Substring trap for glossary keys:** do NOT add a bare-name row whose romanization is a
  substring of a fuller row in use. SAFE full+bare pairs (重蔵/葛籠重蔵, 摩利洞玄/洞玄, 名張/名張ノ耳,
  淀君, 秀頼, 五平/風間五平, 玄以/前田玄以, 宗久/今井宗久, 三成/石田三成, **左近/島左近**) are fine.
  When a place key collides as a substring of another word, prefer the longer key or DECLARE the false
  positive.
- **scratchpad crop.py** (re-create if the container recycled): renders a fractional rectangle of a
  source.pdf page at high zoom so furigana AND the faint running-head folio are legible. Signature
  `crop.py PAGE x0 y0 x1 y1 [zoom]` (PAGE 1-based; fractions of the full page; default zoom 6).
  Uses `import fitz` (pymupdf), opens /home/user/winston/source.pdf, clips to the rect, autocontrasts
  (PIL ImageOps.autocontrast cutoff=2 — do NOT hard-threshold), saves scratchpad/_crop.png.
- **scratchpad topstrips.py** (re-create if recycled): `topstrips.py FIRST LAST` renders the top
  running-head strip (x 0.0-1.0, y 0.015-0.072) of every page in the range at zoom ~9, autocontrasts,
  labels each with "PDF N", and stacks them vertically into scratchpad/_strips_FIRST_LAST.png — read
  the whole span's faint folios in one or two Read calls. (Even folios sit recto/right, odd verso/left.)
- **fitz/pymupdf:** setup.sh's pip line can leave `import fitz` failing; if so, `pip install -q
  pymupdf numpy opencv-python-headless` before render.py/crop.py/topstrips.py.
- **Method (the B12-B18 flow that works):** hand-transcribe from the FULL-PAGE images (300dpi
  ~1112x1725 is legible); crop columns only on dense interleaved pages and for uncertain
  names/furigana. READING ORDER IS STRICT RTL COLUMN-BY-COLUMN (a dialogue attribution "…と…" sits
  in its own column between quotes). Dialogue lines and each narration run are their own paragraphs.
  On a dense page, cross-check column order against the raw OCR data/txt/p0NNN.txt. Write each
  ~6-page chunk to scratchpad/zh/cNN.txt + scratchpad/en/cNN.txt (ONE paragraph per line, both
  sides), verify per-chunk line counts match, then assemble with a python script that asserts equal
  length, joins EN with blank lines, and prints any quote-line mismatch — the zip-alignment is then
  automatic. Track a folio→first-body-paragraph map as you go for the pagemap.
- **A set-off chant/cipher is ONE parity line marked {p}** (verse), between the narration lines that
  introduce and resume it. check_structure strips the marker before parity.
- **A silent dialogue line (「…………」 or 「————」)** transcribes verbatim on the zh side and renders as
  "……" / "——" on the en side (its own paragraph; pairs positionally; qc/content ignore it). ch18 had
  two silent lines (「………………」).
- **NEWLINE-WELD TRAP (B13-B16):** an Edit/append that completes a page-spanning paragraph and whose
  new_string ends WITHOUT a trailing newline gets the next append welded onto it, silently merging two
  source paragraphs. The chunk-file method above sidesteps it (each chunk is a complete Write).

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 / 五平; also Gero
Shōbei Yasuji), Shimotsuge Jirōzaemon (下柘植次郎左衛門 / 次郎左衛門), Kisaru (木さる / key 木猿; given
name 簾 Ren), Kuroami (黒阿弥, dead ch13). Kohagi (小萩) and Imai Sōkyū (今井宗久 → bare "Sōkyū") the
other leads. Mari Dōgen (摩利洞玄 / 洞玄; dead ch14), Mochizuki Gyōbuzaemon (望月刑部左衛門), Maeda Gen'i
(前田玄以 / 玄以; office 京都奉行 the Kyoto magistrate), Ishida Mitsunari (石田三成 / 石田治部少輔 →
"Ishida, the Jibu-no-shō"), **Shima Sakon (島左近 / 左近 → Shima Sakon / Sakon; given name 勝猛 →
Katsutake; ADDED B18: Mitsunari's chief retainer, governs Fushimi in his absence, dies at Sekigahara)**,
Hakkansai (抜関斎 = Sasaki Yoshikata), Jōtei (承禎入道), Yodo-gimi (淀君), Hideyori (秀頼; お拾 O-Hiroi),
Maeda Toshiie (利家). Places: 阿弥陀ヶ峰 → **Amidagamine**, 吉野 Yoshino, 吉野山 Mount Yoshino, 方広寺
Hōkō-ji, 羅刹谷 Rakshasa Valley, 御斎峠 Otogi Pass, 伏見 Fushimi, 大坂/大坂城 Ōsaka/Ōsaka Castle (macron!),
小松谷 Komatsudani, 天竺 → **Tenjiku** (NOT "India"), and the province/city rows (Iga/Kōga/Ōmi/Yamashiro/
Sakai/Ōsaka/Nara/Gifu). Terms: Marishiten (摩利支天), Kōga Saburō (甲賀三郎), rappa (乱波), Mimi of Nabari
(名張ノ耳). NOT glossaried by design: bare 摩利 "Mari"; 化生 keshō; the fictional drug かすり and 偸盗術;
single-chapter names (Dokutan 毒潭 the wandering monk — appeared through ch18, still "Dokutan";
Keikyokusai 荊棘斎 Jūzō's painter alias; and the B18 one-offs 佐々木/Sasaki [rendered "Sasaki", cross-ref
ch09 Rokkaku note], 筒井/Tsutsui, 佐和山/Sawayama, 犬上川/Inukami-gawa, 高宮/Takamiya); and the geography
markers 甘南備(Mount Kannabi)/伎和野(Kiwano)/木津川(Kizu-gawa). Historical one-offs footnoted not
glossaried: Akechi/惟任日向守, 蜂須賀正勝, 伊勢三郎義盛, 弁財天 Benzaiten, 粟田口 the sword school; B16's
甘南備/kannabi, 木津川/Kizu-gawa, 八幡/Hachiman, 仮祝言/kari-shūgen; B17's 月代/sakayaki, 鐚銭/bita-sen,
歌舞伎/kabukimono, 永楽銭/Eiraku-sen, 鬼門/kimon, 尾行/bikō, the Gion Yasaka shrine (cross-ref ch04),
四条/Shijō, 叡山四明岳/Shimeigatake, 貴船/Kifune; B18's 枯れ山水/kare-sansui (dry-landscape garden) and
the "edible walls" siege-ration conceit. Consult glossary.json, do not re-derive.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō (葛籠重蔵 / 重蔵):** mid-30s, thick-shouldered, terse, blunt (わし); the book's centre.
  In the capital moving on Hideyoshi's Fushimi; master of disguise-swap. In ch18 he is off-stage but
  central: Sōkyū's plot hangs on him; calm, all preparations complete, ready to strike (per Dokutan and
  Sakon). Being tailed by Gohei (ch17/19) and loved by Kohagi (ch18). His road still points at killing
  the Taikō. In ch19 he lies hidden in a travelling-painter's guise at the inn Gohei is watching.
- **Kazama Gohei (五平 / Gero Shōbei):** cold, clerkly, calculating, androgynous. Disguised as a low-city
  horse-driver, hunted by the Kōga, unable to return to the Maeda magistrate's residence. Tails Jūzō to
  prove the plot and vault his Maeda standing; savors the thousand-koku bounty. In ch19 he takes a
  second-floor room facing Jūzō's inn to watch (the ch17 surveillance resumed).
- **Kohagi (小萩):** Sōkyū's adopted daughter, a Mochizuki-of-Kōga shape-shifter planted on Sōkyū by
  Ishida; born a Sasaki(Rokkaku) daughter of Ōmi. Cool courtly poise (ございます/ませ; self-refers
  "Kohagi"). In ch18 she LOVES Jūzō and defies the plot's logic: rather than let him be killed, she wins
  Shima Sakon's aid to "cage" him (turn/take him alive) — but accepts that if he nears Hideyoshi she
  must kill him herself. Longs to quit the rappa life.
- **Shima Sakon (島左近 / 左近; given name 勝猛 Katsutake):** ADDED B18. Small-built, past middle age,
  Mitsunari's celebrated chief retainer (鬼左近), governing the Fushimi mansion while Mitsunari is at
  Nagoya. Grave, shrewd, warm under the surface; speaks in measured strategic prose (the tiger-of-the-
  realm metaphor) and rough self-reference (わし; self-names 左近/勝猛), with a sudden lecherous laugh.
  A man who lives to die for a lord who knows him (foreshadowed: he falls at Sekigahara). Off-stage after
  ch18 unless ch19 returns to the Ishida side.
- **Dokutan (毒潭):** the wandering Zen monk, earthy/booming/roguish/wise; loves Kohagi, failed to break
  Jūzō. His ch18 discourse (the wind, prajñā, kalpas, the beast-realm) is grave but living; his banter
  contracted. Dismissed by Kohagi at the end of the Komatsudani scene; likely off-stage now.
- **Imai Sōkyū (宗久):** the great Sakai merchant-magnate (Ōkurakyō Hōin); grave, sardonic, unhurried.
  His plot (via Kohagi and Ishida) drives the endgame; Sakon calls him the hilt whose hidden dagger is
  Jūzō. Formal by design. Off-stage in ch18.

## Where the story stands (end of ch18)
Bunroku 3 (1594), early summer in the capital. Three threads converge on Fushimi. (1) JŪZŌ lies hidden
in a travelling-painter's guise at a small inn, calm and fully prepared to penetrate Hideyoshi's Fushimi
Castle and kill the Taikō. (2) GOHEI, in horse-driver disguise, watches that inn from the room opposite
(ch17), building the proof of Jūzō's intent that would confirm Sōkyū's plot to Ishida and vault his own
Maeda standing. (3) The ISHIDA/KOHAGI side (ch18, "a little before that hour"): Kohagi, who loves Jūzō,
returns to the Komatsudani villa, hears from the monk DOKUTAN that Jūzō cannot be turned, and resolves to
change him by "a woman's truth." That night she infiltrates the Ishida mansion at Fushimi (Mitsunari away
at Nagoya on Korea-campaign business) and wins the aid of SHIMA SAKON, Mitsunari's chief retainer:
rather than simply kill Jūzō (Sakon's cold logic — Jūzō is the only proof, the realm a sleeping tiger not
to be provoked), Sakon lends her men as beaters to help her "cage" the hunter, on one condition — if Jūzō
breaks through and nears Hideyoshi, Sakon (or Kohagi's own hand) will cut him down. The realm's safety
trumps love. Next: B19 = ch19 伏見城 / Fushimi Castle (folios 608-652), the FINAL novel chapter and the
climax, opening 五平が、亭主に命じた二階の部屋と… (Gohei watching Jūzō's inn).

## Next batch
B19 = ch19 伏見城 / Fushimi Castle, printed folios 608-652 (the FINAL novel chapter; ~44 folios, the
longest remaining — expect 5-8 chunks). Opens MID-608 after ch18's tail (paras through
「…好色の笑い声をあげた。」) + the 伏見城 title; offset 0, printed == PDF, CONFIRMED through 609 at end of
B18. ch19 body begins 五平が、亭主に命じた二階の部屋と、重蔵が旅絵師の姿で潜伏している旅籠の部屋とは…
(Gohei staking out Jūzō's inn). READ folios off the running heads to confirm printed == PDF holds. Run the
LAST-BATCH protocol (whole-book reconciliation, COMPLETION.md, commit the final EPUB, authority.json,
HANDOFF→COMPLETE). ch20 解説（村松剛）/ Afterword (folios 653-660) is a third-party critical essay —
translate-or-not is the commissioner's call; FLAG it in the final chat reply.

## Open traps / environment
- **Offset is 0 (folio == PDF) and should stay so to the end.** READ folios off the running heads
  each batch (very faint — topstrips.py + autocontrast; even folios recto/right, odd verso/left); skip
  any duplicate leaf; re-map from any SKIPPED folio; build data/pagemap for the span.
- **The folios 404-405 scan gap is PERMANENT and already handled in ch12.** Do NOT try to bridge it.
- A chapter's tail can spill onto the next opener folio (most chapters did; ch16 did NOT; ch17 spilled
  onto 591; **ch18 spilled onto 608 through 「…好色の笑い声をあげた。」**). Render the next opener and
  verify; make sure the next batch does not re-translate the spillover. ch19 opens MID-608 sharing that
  folio with ch18's tail — START at 五平が (after the 伏見城 title).
- **pagemap indices must be UNIQUE per body_paragraph.** The builder inverts the list to
  {body_paragraph: printed_folio}, so two folios mapping to the same paragraph collide. When a chapter
  opens mid-page on a title-only folio, OMIT that folio; but if the opener folio carries body (ch18's
  608 carries ch18 TAIL, not ch19 body — ch19 body starts on 608 too, so map 608→ch19 para 0).
- Furigana leakage and dropped clauses cluster on the DENSE opener and the TAIL. Re-read both against
  the scan and run the compound-coverage grep before shipping. On dense interleaved pages, read the
  columns RTL and cross-check order against the raw OCR (data/txt).
- **assemble.py OVERWRITES data/zh/chNN.txt AND welds paragraphs** — hand-transcribe from images via
  the chunk-file method (scratchpad/zh + scratchpad/en, one para per line, python-assembled).
- qc_entities / check_content want the rendered name once per paragraph the character appears in —
  do a name-survival pass over pronoun-only paragraphs (B18 fixed 7). Match the glossary `en` form
  exactly, macrons included; render 天竺 as "Tenjiku" not "India". check_content is authoritative;
  qc_entities over-flags place-keys inside common words (declare those, e.g. 甲斐/Kai).
- **check_numbers:** "fifteen thousand" (teens+thousand) parses to 15, NOT 15000 — noise the source
  一万五千 and keep the English spelled form. "a hundred and X thousand" fails; "one hundred and X
  thousand" parses. Fix the English where a parseable spelled form exists; noise the genuinely
  unparseable. Never noise a real quantity you dropped.
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py (notes/figures) or the
  Write/Edit tool or a python json load/dump (glossary), then re-read to verify. (Plain-text
  data/noise.txt via a heredoc is fine — it's not JSON — but re-read to confirm.)
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words; place ⊂ compound).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution); if you run a
  post-hoc pass, watch clause-final over-contraction ("you're."/"there's." are ungrammatical). Keep
  grave uncontracted lines ONLY for deliberately-formal registers. ch18 ran 0.68x (court/intrigue,
  formal by design, clean); ch19 is the climax (action + confrontation) — contract the natural speech.
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled. If `import fitz` fails, `pip install -q pymupdf`.
  Pre-existing checker-regression FAIL (hook stands down on template stub) is unrelated; leave it.
- **ch19 is the LAST novel chapter** — after the normal pipeline, run the CLAUDE.md last-batch protocol
  (whole-book reconciliation check_reconcile.py, COMPLETION.md from template, commit out/owls-castle.epub
  with git add -f, feed renderings to authority.json, rewrite HANDOFF to COMPLETE) and FLAG the ch20
  解説 translate-or-not decision to the commissioner.
