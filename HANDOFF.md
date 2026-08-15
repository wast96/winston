# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B18

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B18 = ch18 「石田屋敷」 (The Ishida Mansion), printed folios 591-607, end to end per the CLAUDE.md pipeline. OFFSET IS 0: printed == PDF (folio 591 = PDF 591, CONFIRMED at the end of B17 by reading the running head of every page across PDF 584-592; no duplicate leaf, no gap). Do NOT assume — READ the folio off the running head of EVERY rendered page across this span to confirm printed == PDF holds, and watch for any further duplicate leaf or gap. The running heads are VERY faint: use scratchpad/topstrips.py FIRST LAST to stack the top strips of a page range into one image (top strip 0.0 0.015 1.0 0.072 at zoom ~9, autocontrast). book.json: ch19 opener 伏見城 (Fushimi Castle) at printed 608 == PDF 608. Build data/pagemap/ch18.json for the span (ch16.json / ch17.json are the format model: entries {printed, pdf, body_paragraph} where body_paragraph is the 0-based index into data/zh/ch18.txt body paragraphs, title excluded; keep indices UNIQUE — the builder inverts the list to {body_paragraph: folio}, so two folios mapping to the same paragraph collide).

ch18 opens MID-591: ch17 尾行's TAIL occupies the top of folio 591 (through the line 「前田屋敷の者じゃ。詮議の筋あって人を追うている。粗略にすまいぞ」, ALREADY translated in B17), then the 石田屋敷 title sits partway down 591, and ch18's BODY begins after it. DO NOT re-translate the ch17 spillover; START ch18 at その時刻より少し前、小萩は、わずかに芭蕉葉のみが茂る枯れ山水の中庭を前に小松谷寮の一室で、雲水毒潭と向いあっていた。「それで、重蔵さまはどう申されましたか」（a little before that hour, at the Komatsudani villa, Kohagi sits in a room over a dry-landscape garden where only a banana-plant leaf grows, facing the wandering monk Dokutan; she asks what Jūzō said）. In the ch18 pagemap OMIT folio 591 if the only ch18 body on it is the title line and the first body paragraph starts on 591 anyway — actually 591 DOES carry ch18 body (the opener paragraph), so map folio 591 to body_paragraph 0, and START ch18's first pagemap entry there. BEFORE translating, read the final two pages of ch17's English (the tail of out/ch17_reading.md) so the voice carries — note ch17 ends on GOHEI taking the inn room opposite Jūzō's, but ch18 cuts back to KOHAGI and Dokutan at Komatsudani "a little before that hour".

ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch18_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write; keep the grave uncontracted line only for deliberately-formal registers (Kohagi's courtly ございます/ませ; Dokutan's earthy discourse contracted). ch05/ch08 both needed a whole contraction pass afterward; ch06 formal-by-design 0.74x, ch09 1.21x, ch10 2.31x, ch11 1.62x, ch12 1.86x, ch13 1.34x, ch14 1.54x, ch15 0.60x (court/interrogation, formal by design), ch16 1.98x (night-ambush action), ch17 3.00x (contracted street/barker/inn dialogue). ch18 is a dialogue-and-intrigue chapter (Kohagi/Dokutan, then the Ishida mansion) — contract the natural speech, keep Kohagi's courtly poise; a mid register is expected.

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). ALSO: setup.sh installs pymupdf under a name the scripts import as `fitz`; if `import fitz` fails, run `pip install -q pymupdf numpy opencv-python-headless`. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled). The pre-existing checker-regression FAIL "hook stands down on template stub" is unrelated; leave it.
2. OCR: render.py 591 609 --dpi 300 (folio 591 = PDF 591; render a few pages past the expected ch19 opener 608 to catch the ch19 opener and any drift); then ocr_crop.py 591 609 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 591 609. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls). CHECK each rendered page's running-head folio: expected folio == PDF. A folio that repeats the previous folio is a double-feed (skip it); a SKIPPED folio is a gap (re-map from there).
3. find_figures.py 591 609 AND eyeball every page for line art (ch01-ch17 were all text-only; if ch18 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by READING the rendered page images directly (data/png/p0NNNN.png — files are named p0591.png etc., 4-digit) and hand-build data/zh/ch18.txt as a corrected, paragraph-aligned transcription (the parity surface). scratchpad/crop.py 6x-renders a page-fraction rectangle (crop.py PAGE x0 y0 x1 y1 [zoom]; PAGE 1-based; fractions of the full page; reads furigana AND faint running-head folios cleanly). scratchpad/topstrips.py FIRST LAST stacks running-head strips of a page range into one image for fast folio reading. Re-create crop.py / topstrips.py if the container recycled (bodies in "Tooling in place" below). NOTE: the full-page images at 300dpi (~1112x1725) are LEGIBLE enough to transcribe directly, cropping columns only for interleaved dense pages and uncertain names/furigana (the B12-B17 method — far faster than half-page crops). Interleaved narration/dialogue mis-orders from the full page — crop the columns and read right-to-left, top-to-bottom literally (READING ORDER IS STRICT RTL COLUMN-BY-COLUMN; a dialogue attribution 「…」と… sits in its own column); treat each 「…」 line and each narration run as its own paragraph. On a DENSE page, cross-check column order against the RAW OCR (data/txt/p0NNN.txt) — it reads the page as a linear column flow and, garbles aside, disambiguates which sentence follows which (the B14 method). Force-add data/zh/ch18.txt (data/zh/ is gitignored). The ch18 opener shares folio 591 with ch17's tail — START at その時刻より少し前 (right after the 石田屋敷 title line), NOT at the top of 591. Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch19 opener folio (608) and check whether ch18's tail spills onto it, and make sure B19 does not re-translate any spillover. COVERAGE cross-check after transcribing: extract every 3+-kanji compound from the raw data/txt OCR (over the ch18 PDF span, excluding any duplicate leaves and the ch17 tail on 591) and confirm each appears in your HAND data/zh/ch18.txt — garbles are expected; a clean meaningful compound that is absent is a real drop to fix (python one-liner over data/txt with a Counter of [一-鿿]{3,}).
   WATCH THE NEWLINE TRAP (bit B13-B16): when you complete a page-spanning paragraph with the Edit tool and its new_string ends with a FULL paragraph, END the new_string WITH a trailing newline, or the next cat-append welds onto that line and silently merges two source paragraphs. After transcribing, ALWAYS run a positional zh↔en alignment (zip the two body-line arrays) — check_structure counts LINES so a compensating merge+split passes parity while the middle is displaced; only the zip catches it. THE B15/B16/B17 METHOD that worked cleanly: write each ~6-page chunk as scratchpad/zh/cNN.txt + scratchpad/en/cNN.txt (ONE paragraph per line, both sides), verify per-chunk line counts match, then assemble both files with a python script that asserts equal length and prints any quote-line alignment mismatch — this makes the zip-alignment automatic and sidesteps the weld trap entirely.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Ieyasu/Tokugawa/Kyoto/Yoshino). Principal cast and majors are decided in glossary.json; reuse unchanged and record in PROGRESS which rows you reused. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans. Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False indent=2, or the Edit tool — the B04-B17 method, NOT apparatus_merge which flattens the glossary). AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter. Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch18_reading.md, settle the English title at translation ('## The Ishida Mansion' — 石田屋敷 = the residence of Ishida Mitsunari, 石田三成 the Jibu-no-shō, already glossaried). Footnote it on a relevant BODY phrase if the sense needs it, per the ch13-17 title-note precedent. Add a ch18 entry to data/checks.json (docs + sources). make_bilingual.py ch18 (parity FIRST). Then run: verify_unit.py ch18; check_structure.py --pairs data/zh/ch18.txt out/ch18_reading.md; check_align.py ch18; qc_entities.py out/ch18_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch18_reading.md. (qc/content want the rendered name once per paragraph the character appears in — do a name-survival pass over any pronoun-only paragraph, as in B10-B17; check_content is authoritative, qc_entities over-flags place-keys inside common words, e.g. 甲斐/Kai inside 生き甲斐/甲斐がある.)
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch17 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku/Genki dating, the Iga Rebellion, Honnō-ji AND Akechi Mitsuhide(明智/惟任日向守) & the field of Yamazaki, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office(治部少輔)/太閤(Taikō)/内府・内大臣(Naifu/Inner Minister=Ieyasu)/右府 titles, Sakai the free-city & its merchant houses, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu/Hideyori(お拾), Nanban, the Nara Great Buddha(Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours & 半刻/小半刻/四半刻 & the night-watches(更/丑ノ刻/六ツ), Aizen Myō-ō, the wakō/bahan ships & Luzon(呂宋), the measures(shaku/sun/chō/koku/ri/ken/kin/tsubo/jō/kan/kanmon), rappa/shinobi/jōnin/genin, jizamurai/gōshi, くノ一/kunoichi, 忍び文字/shinobi-moji, Marishiten, Yodo-gimi(淀君)/Odani, Rokkaku/Sasaki Yoshikata(Hakkansai/Jōtei) & the Sasaki of Ōmi & Kannon-ji 1568, the 1487 Magari campaign, the fifty-three houses of Kōga, Kōga Saburō, the Odawara campaign & the Hōjō, Nagoya castle in Hizen, Hattori Hanzō, the Jurakudai, the go-bugyō, the Iga-goe, Miyamoto Musashi & the Yoshioka, Kashima/Katori & Bokuden, 陽忍/陰忍, the Bon send-off, shōchū, the Kyoto-to-Kōga escape route, the Buddhist precepts / Mahāsāṃghika Vinaya / Buddhabhadra, Empress Jitō's no-kill decree, 化生/keshō, the Mochizuki house of Kōga, Ren (Kisaru's given name), Yoshino & its cherry cult, Maeda Toshiie, the 1595 Hidetsugu purge, the Zaō Hall/Kimpusen-ji, the Saigyō hermitage, Noh/takigi-nō/Kanze & 吉野天人, the owl-whistle(梟笛), the sasumata, Mimi of Nabari, the kozuka, the kuji/Samaya-mudra/mantra counter-spell, Fushimi Castle, the Genki era, Maeda Gen'i & the Kyoto magistracy(京都奉行), Hachisuka Masakatsu, Ise no Saburō Yoshimori & Kurō Hōgan/Yoshitsune, Benzaiten, 修羅/Shura(Carnage), the Nigatsu-dō folding stand, the Awataguchi sword school, the 五三ノ桐 paulownia crest, 百八/hundred-and-eight, クナイ/kunai, 末法/mappō, 般若/prajñā, Tenjiku=India; the B16 first-appearances 甘南備/kannabi, 木津川/the Kizu-gawa, 八幡/Hachiman, 仮祝言/kari-shūgen; the Gion district "below the Yasaka Shrine" (noted ch04, so the Gion Yasaka shrine is NOT re-noted); AND the B17 first-appearances: 月代/sakayaki (the shaved crown), 鐚銭/bita-sen (debased coin), 歌舞伎/kabukimono (flamboyant street swaggerer, NOT the theater), 永楽銭/Eiraku-sen (Ming Yongle cash, the good coin vs bita-sen), 鬼門/kimon (the demon-gate/unlucky NE), 尾行/bikō (the title, covert tailing). Note only ch18's NEW first-appearances (likely candidates: 石田三成/the Ishida mansion if the man/office wants a fresh gloss beyond the existing Ishida-office notes; 芭蕉/the banana-plant; 枯れ山水/the dry-landscape garden; 雲水/the wandering-monk status; any new person/place/office the Ishida intrigue crosses). Anchor notes to BODY phrases (verbatim substrings), not heading-only text. Add via apparatus_merge.py (batch JSON file with a top-level "notes" key, numeric char refs OR literal chars in bodies — NEVER a heredoc; ANCHORS must use LITERAL Unicode matching the reading text, e.g. ō/ā/ñ and STRAIGHT ASCII apostrophes/quotes as the reading files carry them, NOT char refs). check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, the renderings reused/added), INCLUDING the confirmed folio-to-PDF map for this span (should be printed == PDF throughout — confirm), and the data/pagemap/ch18.json you built.

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B19 kickoff (ch19 「伏見城」 Fushimi Castle, printed folios 608-652 — the FINAL novel chapter; ch20 解説 is a third-party afterword whose translation is the commissioner's separate call; offset should still be 0 — printed == PDF — but READ folios to confirm) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure in book.json; metadata set; skeleton EPUB built; page
  furniture measured (crop L0.035 R0.965 T0.075 B0.955; model jpn_vert psm5).
- **Offset history (READ folios, do not compute):** 0 for folios 7-325; **+2 from folio 326
  (PDF 328) through folio 403 (PDF 405)**; a **1-leaf scan gap dropped printed folios 404-405**
  (MISSING from the scan), re-mapping the offset back to **0 from folio 406 (PDF 406) onward**.
  **printed == PDF CONFIRMED unbroken through folio 592 (end of B17's rendered span).** It should
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
  paragraphs, 4 notes. ch16 opens mid-566 (ch15 tail + 甘南備山 title, no ch16 body on 566; body starts
  567) and ENDS on 583 — does NOT spill onto 584.
- **B17 = ch17 尾行 / The Shadowing (584-590, tail on 591): COMPLETE.** 44 body paragraphs, 6 new notes
  (book total 124). All checks green (parity 44|44, numbers 0/44 with noise +2 [八坂神社, 四明岳],
  check_content clean after 3 name-survival fixes, qc 0 misses, check_align 2 declared exceptions
  [short interior thoughts, ratio-inflated], register 3.00x contracted-street-dialogue within tolerance,
  check_apparatus clean, qa_epub PASS, epubcheck 0/0/0/0). Built data/pagemap/ch17.json (8 entries,
  printed==PDF 584-591). NO figures. NO new glossary rows (all reused). ch17 opens CLEAN at top of 584
  (尾行 title + body same page); its TAIL spills onto 591 (through 「前田屋敷の者じゃ…粗略にすまいぞ」) before
  the 石田屋敷 (ch18) title. Gohei, disguised as a horse-driver, tails Jūzō through the capital to a
  sideshow and on to an inn, and takes the room opposite to keep watch.

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
  "one hundred and twenty thousand", "five million". It does NOT parse bare compounds like "a hundred
  and eight" (108) — those go in noise with a comment (value verified present by eye). Fix a real
  quantity in the ENGLISH where a parseable spelled form exists; noise only the genuinely unparseable
  compounds and the numerals-inside-names.
- `data/checks.json`: the {docs, sources} config. ch01-ch17 in.
- `data/noise.txt`: check_numbers noise. B13 二十代; B14 八の字/四つ這い; B15 三千六百万/百八/三村/三角/八幡/
  五条; B17 八坂神社 (the Gion Yasaka shrine)/四明岳 (Shimeigatake, a peak of Mt Hiei). 四条/Shijō was
  already in from ch08. Extend per its header, longest literal first, one comment line each; never noise
  a real quantity you dropped.
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens glossary
  rows to the ROOT, so since B04 add glossary rows DIRECTLY into the sections (Edit tool, or json
  load/dump ensure_ascii=False indent=2). Notes and figures merge fine via apparatus_merge (batch
  file needs a top-level "notes"/"figures" key — {"notes": {"chNN": [...]}}).
- **Note anchors:** must be verbatim substrings of the BODY prose (a title-meaning note is anchored
  to a relevant body phrase — ch13 "Water Dog", ch14 "Carnage", ch15 "Paulownia Crest", ch16 title on a
  body phrase, ch17 title on "Gohei's shadowing had come off"). **ANCHORS use LITERAL Unicode**
  matching the reading text (ō, ā, ñ, AND straight ASCII apostrophes/quotes — the reading files stay
  plain ASCII, typographized only at render, so anchor an apostrophe as ' NOT &#8217;), NOT numeric
  char refs. Note BODIES: literal Unicode is fine (em dash, en dash, macrons, curly quotes) OR numeric
  character references; only NAMED HTML entities (&nbsp; &mdash;) are rejected. Author the notes batch
  as a JSON FILE (Write tool) and run apparatus_merge.py on it — never a heredoc.
- **Substring trap for glossary keys:** do NOT add a bare-name row whose romanization is a
  substring of a fuller row in use. SAFE full+bare pairs (重蔵/葛籠重蔵, 摩利洞玄/洞玄, 名張/名張ノ耳,
  淀君, 秀頼, 五平/風間五平, 玄以/前田玄以, 宗久/今井宗久, 三成/石田三成) are fine. When a place key
  collides as a substring of another word, prefer the longer key or DECLARE the false positive.
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
- **Method (the B12-B17 flow that works):** hand-transcribe from the FULL-PAGE images (300dpi
  ~1112x1725 is legible); crop columns only on dense interleaved pages and for uncertain
  names/furigana. READING ORDER IS STRICT RTL COLUMN-BY-COLUMN (a dialogue attribution "…と…" sits
  in its own column between quotes). Dialogue lines and each narration run are their own paragraphs.
  On a dense page, cross-check column order against the raw OCR data/txt/p0NNN.txt. Write each
  ~6-page chunk to scratchpad/zh/cNN.txt + scratchpad/en/cNN.txt (ONE paragraph per line, both
  sides), verify per-chunk line counts match, then assemble with a python script that asserts equal
  length and joins the EN with blank lines — the zip-alignment is then automatic. Track a
  folio→first-body-paragraph map as you go for the pagemap.
- **A set-off chant/cipher is ONE parity line marked {p}** (verse), between the narration lines that
  introduce and resume it. check_structure strips the marker before parity.
- **A silent dialogue line (「…………」 or 「————」)** transcribes verbatim on the zh side and renders as
  "……" / "——" on the en side (its own paragraph; pairs positionally; qc/content ignore it).
- **NEWLINE-WELD TRAP (B13-B16):** an Edit that completes a page-spanning paragraph and whose
  new_string ends WITHOUT a trailing newline will have the next cat-append welded onto it, silently
  merging two source paragraphs. End such Edits with `\n`. The chunk-file method above sidesteps it.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 / 五平; also Gero
Shōbei Yasuji), Shimotsuge Jirōzaemon (下柘植次郎左衛門 / 次郎左衛門), Kisaru (木さる / key 木猿; given
name 簾 Ren), Kuroami (黒阿弥, dead ch13). Kohagi (小萩) and Imai Sōkyū (今井宗久 → bare "Sōkyū") the
other leads. Mari Dōgen (摩利洞玄 / 洞玄; dead ch14), Mochizuki Gyōbuzaemon (望月刑部左衛門), Maeda Gen'i
(前田玄以 / 玄以; office 京都奉行 the Kyoto magistrate), Ishida Mitsunari (石田三成 / 石田治部少輔 →
"Ishida, the Jibu-no-shō"), Hakkansai (抜関斎 = Sasaki Yoshikata), Jōtei (承禎入道), Yodo-gimi (淀君),
Hideyori (秀頼; お拾 O-Hiroi), Maeda Toshiie (利家). Places: 阿弥陀ヶ峰 → **Amidagamine**, 吉野 Yoshino,
吉野山 Mount Yoshino, 方広寺 Hōkō-ji, 羅刹谷 Rakshasa Valley, 御斎峠 Otogi Pass, 伏見 Fushimi, 大坂/大坂城
Ōsaka/Ōsaka Castle (macron!), 小松谷 Komatsudani, 天竺 → **Tenjiku** (NOT "India"), and the province/city
rows (Iga/Kōga/Ōmi/Yamashiro/Sakai/Ōsaka/Nara/Gifu). Terms: Marishiten (摩利支天), Kōga Saburō (甲賀三郎),
rappa (乱波), Mimi of Nabari (名張ノ耳). NOT glossaried by design: bare 摩利 "Mari"; 化生 keshō; the
fictional drug かすり and 偸盗術; single-chapter names (Dokutan 毒潭 the wandering monk — REAPPEARS in
ch18 at Komatsudani, still rendered "Dokutan"; Keikyokusai 荊棘斎 Jūzō's painter alias; Kiheiji 川ノ端の
喜平次; Imai Sōkun 宗薫; Konishi Ryūsa/Yakurō; Hosokawa Tadaoki; Tsuda of the Tennōjiya; Shibatsuji
Riemon; Iba no Yokoashi 伊庭ノ横足); and the geography markers 甘南備(Mount Kannabi)/伎和野(Kiwano)/木津川
(Kizu-gawa) — kept consistent in ch16. Historical one-offs footnoted not glossaried: Akechi/惟任日向守,
蜂須賀正勝, 伊勢三郎義盛, 弁財天 Benzaiten, 粟田口 the sword school; B16's 甘南備/kannabi, 木津川/Kizu-gawa,
八幡/Hachiman, 仮祝言/kari-shūgen; B17's 月代/sakayaki, 鐚銭/bita-sen, 歌舞伎/kabukimono, 永楽銭/Eiraku-sen,
鬼門/kimon, 尾行/bikō, plus the Gion Yasaka shrine (cross-ref ch04's Gion note), 四条/Shijō, 叡山四明岳/
Shimeigatake of Mt Hiei, 貴船/Kifune — all rendered plainly or footnoted, not glossaried. Consult
glossary.json, do not re-derive.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō (葛籠重蔵 / 重蔵):** mid-30s, thick-shouldered, terse, blunt (わし); the book's centre.
  In ch17 he is in the capital in a gaudy scarlet-flecked kosode, moving on Hideyoshi's Fushimi; a
  master of disguise-swap (he shrinks himself crabwise through a fairground crowd and re-emerges as a
  plain sword-less painter with a scroll). Wry, cold nerve; a real softness he despises. His road still
  points at killing the Taikō. He is being tailed by Gohei without knowing the tail is Gohei.
- **Kazama Gohei (五平 / Gero Shōbei):** cold, clerkly, calculating, androgynous. In ch17 he is loose
  and hunted, sunburnt, disguised as a low-city horse-driver (rough tea-stall banter; superior わし/じゃ
  to the innkeeper), unable since Kiwano to return to the magistrate's residence. He tails Jūzō to build
  the proof (Jūzō means to enter Fushimi) that would confirm Sōkyū's plot to Ishida and vault his own
  Maeda standing; he savors the thousand-koku bounty and dismisses the (presumed-dead) Kisaru with pure
  ninja tool-logic ("death is the using-up of a tool"). Admires Jūzō's craft coldly. Takes the inn room
  opposite Jūzō's to keep watch, buying the host's silence with silver, posing as a Maeda man.
- **Kohagi (小萩):** Sōkyū's adopted daughter, a Mochizuki-of-Kōga shape-shifter planted on Sōkyū by
  Ishida; born a Sasaki(Rokkaku) daughter of Ōmi. Cool courtly poise (ございます/ませ; self-refers
  "Kohagi"). Defied Sōkyū's order to slaughter Gohei's band (ch15), meaning to take them alive to shield
  the wounded Jūzō; longs to quit the rappa life. In ch18 she is back at the Komatsudani villa facing
  the monk Dokutan and asking what Jūzō said — the intrigue turns toward the Ishida mansion.
- **Dokutan (毒潭):** the wandering Zen monk, earthy/booming/roguish/wise; loves Kohagi, was sent by her
  to shatter Jūzō's ambition and failed. REAPPEARS in ch18 at Komatsudani with Kohagi. His discourse
  (prajñā, mappō, the beast-realm) is grave but living; his banter contracted.
- **Kisaru (木さる / given name 簾 Ren):** Shimotsuge's daughter, spirited, blunt Iga dialect (じゃ/のじゃ,
  self-refers 木さる/わたくし). In ch16 Gohei sold her to the Kōga ambush as a decoy; she survived by her
  father's "take the cut" doctrine (lost her left hand), and at the Kizu-gawa renounced the world of the
  two men she loved and trudged home to Iga, maimed but carefree. Gohei believes her dead. Likely
  off-stage.
- **Imai Sōkyū (宗久):** the great Sakai merchant-magnate (Ōkurakyō Hōin); grave, sardonic, unhurried, a
  blade under the yawn. His plot (via Kohagi and Ishida) drives the endgame. Formal by design.
- **Maeda Gen'i (前田玄以):** the shrewd, life-clinging Kyoto magistrate; secretly tilting to the
  Tokugawa; lets Gohei run the Iga work his own way. Off-stage but Gohei still trades on the Maeda name.

## Where the story stands (end of ch17)
Bunroku 3 (1594), weeks after the Kiwano ambush; early summer in the capital. Three plot-lines run on.
(1) GOHEI has dropped the samurai disguise and the magistrate's residence (too exposed to the Kōga
hunting him) and works the streets in a rotation of disguises, presently a horse-driver. His aim: pin
down where Jūzō lodges and prove the man means to penetrate Hideyoshi's Fushimi stronghold — which would
confirm Sōkyū's plot to Ishida and vault Gohei's standing in the Maeda house. In ch17 he spots the
flashily-dressed Jūzō near the Gion steps, tails him toward Shijō and into a sideshow, watches Jūzō
sense the tail and swap his identity for a plain sword-less painter, re-acquires him on the road, trails
him a small half-hour to a small red-lattice inn, and takes the room opposite to keep watch. (2) JŪZŌ is
in the capital moving on Fushimi, master of the crowd-disguise, unaware the tail is Gohei. (3) KOHAGI /
the Ishida side: ch18 石田屋敷 / The Ishida Mansion (opens "a little before that hour" — 591, offset 0)
cuts back to Kohagi at the Komatsudani villa facing the monk Dokutan and asking what Jūzō said, the
intrigue turning toward Ishida Mitsunari's mansion.

## Next batch
B18 = ch18 石田屋敷 / The Ishida Mansion, printed folios 591-607 (opens MID-591 after ch17's tail + the
石田屋敷 title; offset 0, printed == PDF, CONFIRMED through 592 at end of B17). ch18 body begins
その時刻より少し前、小萩は…雲水毒潭と向いあっていた (Kohagi and Dokutan at Komatsudani). READ folios off the
running heads to confirm printed == PDF holds. Then B19 = ch19 伏見城 / Fushimi Castle, folios 608-652
(the FINAL novel chapter), and ch20 解説 is the third-party afterword (translate-or-not is the
commissioner's call).

## Open traps / environment
- **Offset is 0 (folio == PDF) and should stay so to the end.** READ folios off the running heads
  each batch (very faint — topstrips.py + autocontrast; even folios recto/right, odd verso/left); skip
  any duplicate leaf; re-map from any SKIPPED folio; build data/pagemap for the span.
- **The folios 404-405 scan gap is PERMANENT and already handled in ch12.** Do NOT try to bridge it.
- A chapter's tail can spill onto the next opener folio (most chapters did; ch16 did NOT, ch17 DID —
  onto 591 through 「…粗略にすまいぞ」). Render the next opener and verify; make sure the next batch does
  not re-translate the spillover. ch18 opens MID-591 sharing that folio with ch17's tail.
- **pagemap indices must be UNIQUE per body_paragraph.** The builder inverts the list to
  {body_paragraph: printed_folio}, so two folios mapping to the same paragraph collide. When a chapter
  opens mid-page on a title-only folio, OMIT that folio; but ch18 DOES carry body on its opener folio
  591, so map 591 to its first ch18 body paragraph.
- Furigana leakage and dropped clauses cluster on the DENSE opener and the TAIL. Re-read both against
  the scan and run the compound-coverage grep before shipping. On dense interleaved pages, read the
  columns RTL and cross-check order against the raw OCR (data/txt).
- **assemble.py OVERWRITES data/zh/chNN.txt AND welds paragraphs** — hand-transcribe from images via
  the chunk-file method (scratchpad/zh + scratchpad/en, one para per line, python-assembled).
- qc_entities / check_content want the rendered name once per paragraph the character appears in —
  do a name-survival pass over pronoun-only paragraphs (B17 fixed 3). Match the glossary `en` form
  exactly, macrons included; render 天竺 as "Tenjiku" not "India". check_content is authoritative;
  qc_entities over-flags place-keys inside common words (declare those, e.g. 甲斐/Kai).
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py (notes/figures) or the
  Write/Edit tool or a python json load/dump (glossary), then re-read to verify. (Plain-text
  data/noise.txt via a heredoc is fine — it's not JSON — but re-read to confirm.)
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words; place ⊂ compound).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution); if you run a
  post-hoc pass, watch clause-final over-contraction ("you're."/"there's." are ungrammatical). Keep
  grave uncontracted lines ONLY for deliberately-formal registers. ch17 ran 3.00x (contracted
  street/barker/inn dialogue, clean); ch18 is dialogue-and-intrigue — contract the natural speech,
  keep Kohagi's courtly poise.
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled. If `import fitz` fails, `pip install -q pymupdf`.
  Pre-existing checker-regression FAIL (hook stands down on template stub) is unrelated; leave it.
