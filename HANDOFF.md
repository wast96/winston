# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B17

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B17 = ch17 「尾行」 (The Shadowing), printed folios 584-590, end to end per the CLAUDE.md pipeline. OFFSET IS 0: printed == PDF (folio 584 = PDF 584, CONFIRMED at the end of B16 by reading the running head of every page across PDF 566-585; no duplicate leaf, no gap). Do NOT assume — READ the folio off the running head of EVERY rendered page across this span to confirm printed == PDF holds, and watch for any further duplicate leaf or gap. The running heads are VERY faint: use scratchpad/topstrips.py FIRST LAST to stack the top strips of a page range into one image (top strip 0.0 0.015 1.0 0.072 at zoom ~9, autocontrast). book.json: ch18 opener 石田屋敷 (The Ishida Mansion) at printed 591 == PDF 591. Build data/pagemap/ch17.json for the span (ch15.json / ch16.json are the format model: entries {printed, pdf, body_paragraph} where body_paragraph is the 0-based index into data/zh/ch17.txt body paragraphs, title excluded; keep indices UNIQUE — the builder inverts the list to {body_paragraph: folio}, so two folios mapping to the same paragraph collide). Confirm the ch18 opener 石田屋敷 and flag whether ch17's tail spills onto it.

ch17 opens CLEAN on folio 584 (the 尾行 title sits at the left of 584 with the body starting on the SAME page; ch16's tail does NOT spill onto 584 — ch16 ended on 583). ch17 body begins with 夏も間近くなったある日の午後、祇園八坂神社の石段下に葭簀をかまえた掛け茶屋の床几の上で、午睡をむさぼっていた馬方のひとりが、むくむくと起きあがるなり、目を糸のように細めて、往来の一角をみつめた。（early summer, an afternoon at the Gion Yasaka shrine steps: a dozing horse-driver at a reed-screened tea-stall jerks awake and stares — he is Gohei in disguise, sunburnt, his moon-pate grown out, and since the Kiwano ambush by Sōkyū's people he cannot return to the magistrate's residence; now he himself is being shadowed by a Kōga assassin). BEFORE translating, read the final two pages of ch16's English (the tail of out/ch16_reading.md) so the voice carries — note ch16 ends on Kisaru (maimed at Kiwano, trudging home to Iga), but ch17 follows GOHEI in the capital.

ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch17_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write (Gohei's low-city horse-driver disguise, tea-stall banter, any street/inn exchange) — do NOT leave "It is/I do not/you are" everywhere; keep the grave uncontracted line only for deliberately-formal registers. ch05/ch08 both needed a whole contraction pass afterward; ch06 ran formal-by-design at 0.74x and passed, ch09 1.21x, ch10 2.31x, ch11 1.62x, ch12 1.86x, ch13 1.34x, ch14 1.54x, ch15 0.60x (court/interrogation chapter, formal by design), ch16 1.98x (Kiwano night-ambush action) — an action/suspense chapter should sit above 1.0x, but 0.0x is a draft error, not "formal by design". ch17 is a shadowing/suspense chapter (Gohei disguised, hunted through the capital) — expect narration-forward prose with contracted street dialogue.

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). ALSO: setup.sh installs pymupdf under a name the scripts import as `fitz`; if `import fitz` fails, run `pip install -q pymupdf numpy opencv-python-headless`. epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled). The pre-existing checker-regression FAIL "hook stands down on template stub" is unrelated; leave it.
2. OCR: render.py 584 592 --dpi 300 (folio 584 = PDF 584; render a few pages past the expected ch18 opener 591 to catch the ch18 opener and any drift); then ocr_crop.py 584 592 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 584 592. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls). CHECK each rendered page's running-head folio: expected folio == PDF. A folio that repeats the previous folio is a double-feed (skip it); a SKIPPED folio is a gap (re-map from there).
3. find_figures.py 584 592 AND eyeball every page for line art (ch01-ch16 were all text-only; if ch17 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by READING the rendered page images directly (data/png/p0NNNN.png — files are named p0584.png etc., 4-digit) and hand-build data/zh/ch17.txt as a corrected, paragraph-aligned transcription (the parity surface). scratchpad/crop.py 6x-renders a page-fraction rectangle (crop.py PAGE x0 y0 x1 y1 [zoom]; PAGE 1-based; fractions of the full page; reads furigana AND faint running-head folios cleanly). scratchpad/topstrips.py FIRST LAST stacks running-head strips of a page range into one image for fast folio reading. Re-create crop.py / topstrips.py if the container recycled (bodies in "Tooling in place" below). NOTE: the full-page images at 300dpi (~1112x1725) are LEGIBLE enough to transcribe directly, cropping columns only for interleaved dense pages and uncertain names/furigana (the B12-B16 method — far faster than half-page crops). Interleaved narration/dialogue mis-orders from the full page — crop the columns and read right-to-left, top-to-bottom literally (READING ORDER IS STRICT RTL COLUMN-BY-COLUMN; a dialogue attribution 「…」と… sits in its own column); treat each 「…」 line and each narration run as its own paragraph. On a DENSE page, cross-check column order against the RAW OCR (data/txt/p0NNN.txt) — it reads the page as a linear column flow and, garbles aside, disambiguates which sentence follows which (the B14 method). Force-add data/zh/ch17.txt (data/zh/ is gitignored). Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch18 opener folio and check whether ch17's tail spills onto it, and make sure B18 does not re-translate any spillover. COVERAGE cross-check after transcribing: extract every 3+-kanji compound from the raw data/txt OCR (over the ch17 PDF span, excluding any duplicate leaves) and confirm each appears in your HAND data/zh/ch17.txt — garbles are expected; a clean meaningful compound that is absent is a real drop to fix (python one-liner over data/txt with a Counter of [一-鿿]{3,}).
   WATCH THE NEWLINE TRAP (bit B13, B14, B15): when you complete a page-spanning paragraph with the Edit tool and its new_string ends with a FULL paragraph, END the new_string WITH a trailing newline, or the next cat-append welds onto that line and silently merges two source paragraphs. After transcribing, ALWAYS run a positional zh↔en alignment (zip the two body-line arrays) — check_structure counts LINES so a compensating merge+split passes parity while the middle is displaced; only the zip catches it. THE B15/B16 METHOD that worked cleanly: write each ~6-page chunk as scratchpad/zh/cNN.txt + scratchpad/en/cNN.txt (ONE paragraph per line, both sides), verify per-chunk line counts match, then assemble both files with a python script that asserts equal length and prints any quote-line alignment mismatch — this makes the zip-alignment automatic and sidesteps the weld trap entirely.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Ieyasu/Tokugawa/Kyoto/Yoshino). Principal cast and majors are decided in glossary.json; reuse unchanged and record in PROGRESS which rows you reused. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans. Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False indent=2, or the Edit tool — the B04-B16 method, NOT apparatus_merge which flattens the glossary). AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter. Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch17_reading.md, settle the English title at translation ('## The Shadowing' — 尾行 bikō = the act of tailing/following someone covertly; the shadower here is a Kōga assassin on Gohei's trail. Footnote it on a relevant BODY phrase if the sense needs it, per the ch13/14/15/16 title-note precedent). Add a ch17 entry to data/checks.json (docs + sources). make_bilingual.py ch17 (parity FIRST). Then run: verify_unit.py ch17; check_structure.py --pairs data/zh/ch17.txt out/ch17_reading.md; check_align.py ch17; qc_entities.py out/ch17_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch17_reading.md. (qc/content want the rendered name once per paragraph the character appears in — do a name-survival pass over any pronoun-only paragraph, as in B10-B16; check_content is authoritative, qc_entities over-flags place-keys inside common words, e.g. 甲斐/Kai inside 生き甲斐/甲斐がある.)
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch16 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku/Genki dating, the Iga Rebellion, Honnō-ji AND Akechi Mitsuhide(明智/惟任日向守) & the field of Yamazaki, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office(治部少輔)/太閤(Taikō)/内府・内大臣(Naifu/Inner Minister=Ieyasu)/右府 titles, Sakai the free-city & its merchant houses, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu/Hideyori(お拾), Nanban, the Nara Great Buddha(Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours & 半刻/小半刻/四半刻 & the night-watches(更/丑ノ刻/六ツ), Aizen Myō-ō, the wakō/bahan ships & Luzon(呂宋), the measures(shaku/chō/koku/ri/ken/kin/tsubo/jō/kan/kanmon), rappa/shinobi/jōnin/genin, jizamurai/gōshi, くノ一/kunoichi, 忍び文字/shinobi-moji, Marishiten, Yodo-gimi(淀君)/Odani, Rokkaku/Sasaki Yoshikata(Hakkansai/Jōtei) & the Sasaki of Ōmi & Kannon-ji 1568, the 1487 Magari campaign, the fifty-three houses of Kōga, Kōga Saburō, the Odawara campaign & the Hōjō, Nagoya castle in Hizen, Hattori Hanzō, the Jurakudai, the go-bugyō, the Iga-goe, Miyamoto Musashi & the Yoshioka, Kashima/Katori & Bokuden, 陽忍/陰忍, the Bon send-off, shōchū, the Kyoto-to-Kōga escape route, the Buddhist precepts / Mahāsāṃghika Vinaya / Buddhabhadra, Empress Jitō's no-kill decree, 化生/keshō, the Mochizuki house of Kōga, Ren (Kisaru's given name), Yoshino & its cherry cult, Maeda Toshiie, the 1595 Hidetsugu purge, the Zaō Hall/Kimpusen-ji, the Saigyō hermitage, Noh/takigi-nō/Kanze & 吉野天人, the owl-whistle(梟笛), the sasumata, Mimi of Nabari, the kozuka, the kuji/Samaya-mudra/mantra counter-spell, Fushimi Castle, the Genki era, Maeda Gen'i & the Kyoto magistracy(京都奉行), Hachisuka Masakatsu, Ise no Saburō Yoshimori & Kurō Hōgan/Yoshitsune, Benzaiten, 修羅/Shura(Carnage), the Nigatsu-dō folding stand, the Awataguchi sword school, the 五三ノ桐 paulownia crest, 百八/hundred-and-eight, クナイ/kunai, 末法/mappō, 般若/prajñā, Tenjiku=India; AND the B16 first-appearances: 甘南備/kannabi (the sacred hill), 木津川/the Kizu-gawa (the river), 八幡/Hachiman (the war-god & his shrine), 仮祝言/kari-shūgen (the provisional wedding). Note only ch17's NEW first-appearances (likely candidates: 祇園八坂神社/the Gion Yasaka shrine; 馬方/the horse-driver disguise if it needs a gloss; 月代/sakayaki the shaved pate; 鐚銭/bita-sen low-grade coin; any new office/person/place the shadowing route crosses). Anchor notes to BODY phrases (verbatim substrings), not heading-only text (the ch13-16 precedent). Add via apparatus_merge.py (batch JSON file with a top-level "notes" key, numeric char refs OR literal chars in bodies — NEVER a heredoc; ANCHORS must use LITERAL Unicode matching the reading text, e.g. ō/ā/ñ, NOT char refs). check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, the renderings reused/added), INCLUDING the confirmed folio-to-PDF map for this span (should be printed == PDF throughout — confirm), and the data/pagemap/ch17.json you built.

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B18 kickoff (ch18 「石田屋敷」 The Ishida Mansion, printed folios 591-607; offset should still be 0 — printed == PDF — but READ folios to confirm) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure in book.json; metadata set; skeleton EPUB built; page
  furniture measured (crop L0.035 R0.965 T0.075 B0.955; model jpn_vert psm5).
- **Offset history (READ folios, do not compute):** 0 for folios 7-325; **+2 from folio 326
  (PDF 328) through folio 403 (PDF 405)**; a **1-leaf scan gap dropped printed folios 404-405**
  (MISSING from the scan), re-mapping the offset back to **0 from folio 406 (PDF 406) onward**.
  **printed == PDF CONFIRMED unbroken through folio 585 (end of B16's rendered span).** It should
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
- **B15 = ch15 五三ノ桐 / The Paulownia Crest (508-565, tail on 566): COMPLETE.** 440 body paragraphs,
  5 new notes (book total 114). All checks green (parity 440|440, numbers 0/440, check_content clean,
  qc 2 misses = declared 甲斐/Kai false positive, register 0.60x formal-by-design within tolerance,
  qa_epub PASS, epubcheck 0/0/0/0). Built data/pagemap/ch15.json (59 entries, printed==PDF 508-566).
  NO figures. NO new glossary rows (all reused). noise +6 (三千六百万, 百八, 三村, 三角, 八幡, 五条).
  Gohei extorts Sōkyū for 2000 gold buried at Kiwano; Kohagi plots to take Gohei's band alive to save
  Jūzō; the monk Dokutan tells Jūzō that Kohagi loves him, but Jūzō holds to his death-road. ch15's
  tail (body para 439) spills onto folio 566 before the 甘南備山 title — B16 must not re-translate it.
- **B16 = ch16 甘南備山 / Mount Kannabi (566-583; opener mid-566, ends on 583): COMPLETE.** 132 body
  paragraphs, 4 new notes (book total 118). All checks green (parity 132|132, numbers 0/132 — 二丁→"two
  chō", 二人→"The two of them" carried, no noise added; check_content clean after 2 name-survival fixes;
  qc 0 misses; register 1.98x = livelier action register, within tolerance; check_apparatus clean;
  qa_epub PASS; epubcheck 0/0/0/0). Built data/pagemap/ch16.json (17 entries, folios 567-583; folio
  566 is title-only and omitted to keep body_paragraph indices unique). NO figures. NO new glossary
  rows (all reused). No noise added. ch16 opens mid-566 (ch15 tail + 甘南備山 title, no ch16 body on 566;
  body starts 567) and ENDS on 583 — does NOT spill onto 584 (ch17 尾行 opens clean on 584). The Kiwano
  night ambush: Gohei walks his band into Kohagi's Kōga trap at the ruined Hachiman shrine, throws his
  sword and then throws KISARU as decoys to escape; Kisaru survives by her father's "take the cut"
  doctrine (loses her left hand, kills a Kōga man with a right-hand shuriken), crawls to the Kizu-gawa,
  and resolves to vanish from the world of the two men she loved — trudges home to Iga, maimed.

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
  that sits inside a common word (B13 declared 甲斐/Kai inside 年甲斐; B15 again 甲斐 inside 生き甲斐/
  甲斐がある = "worth, purpose") — verify against the scan and DECLARE it in PROGRESS.**
- `check_numbers.py` (`--noise data/noise.txt`): parses English number-words including "a hundred",
  "one hundred and twenty thousand" (= 120,000), "five million"/"a hundred million". It does NOT
  parse the bare compounds "a hundred and eight" (108) or "thirty-six million" — those go in noise
  with a comment (value verified present in prose by eye). Fix a real quantity in the ENGLISH where
  a parseable spelled form exists (B15: "hundred and twenty thousand" → "one hundred and twenty
  thousand" so the parser read 120,000); noise only the genuinely unparseable compounds and the
  numerals-inside-names.
- `data/checks.json`: the {docs, sources} config. ch01-ch15 in.
- `data/noise.txt`: check_numbers noise. B13 added 二十代; B14 八の字/四つ這い; B15 三千六百万/百八/
  三村/三角/八幡/五条. Extend per its header, longest literal first, one comment line each; never
  noise a real quantity you dropped.
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens glossary
  rows to the ROOT, so since B04 add glossary rows DIRECTLY into the sections (Edit tool, or json
  load/dump ensure_ascii=False indent=2). Notes and figures merge fine via apparatus_merge (batch
  file needs a top-level "notes"/"figures" key — {"notes": {"chNN": [...]}}).
- **Note anchors:** must be verbatim substrings of the BODY prose (a title-meaning note is anchored
  to a relevant body phrase — ch13 "Water Dog", ch14 "Carnage", ch15 "Paulownia Crest" on the body
  phrase "kill the Taikō"). **ANCHORS use LITERAL Unicode** matching the reading text (ō, ā, ñ), NOT
  numeric char refs — a char-ref anchor will not match. Note BODIES: literal Unicode is fine (em
  dash, en dash, macrons, curly quotes) OR numeric character references; only NAMED HTML entities
  (&nbsp; &mdash;) are rejected. Author the notes batch as a JSON FILE (Write tool) and run
  apparatus_merge.py on it — never a heredoc.
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
  the whole span's faint folios in one or two Read calls.
- **fitz/pymupdf:** setup.sh's pip line can leave `import fitz` failing; if so, `pip install -q
  pymupdf numpy opencv-python-headless` before render.py/crop.py/topstrips.py.
- **Method (the B12-B15 flow that works):** hand-transcribe from the FULL-PAGE images (300dpi
  ~1112x1725 is legible); crop columns only on dense interleaved pages and for uncertain
  names/furigana. READING ORDER IS STRICT RTL COLUMN-BY-COLUMN (a dialogue attribution "…と…" sits
  in its own column between quotes). Dialogue lines and each narration run are their own paragraphs.
  On a dense page, cross-check column order against the raw OCR data/txt/p0NNN.txt. Write each
  ~6-page chunk to scratchpad/zh/cNN.txt + scratchpad/en/cNN.txt (ONE paragraph per line, both
  sides), verify per-chunk line counts match, then assemble with a python script that asserts equal
  length and joins the EN with blank lines — the zip-alignment is then automatic. Track a
  folio→first-body-paragraph map as you go for the pagemap.
- **A set-off chant/cipher is ONE parity line marked {p}** (verse), between the narration lines that
  introduce and resume it (ch06 cipher, ch13 mantra). check_structure strips the marker before parity.
- **A silent dialogue line (「…………」 or 「————」)** transcribes verbatim on the zh side and renders as
  "……" / "——" on the en side (its own paragraph; pairs positionally; qc/content ignore it).
- **NEWLINE-WELD TRAP (B13, B14, B15):** an Edit that completes a page-spanning paragraph and whose
  new_string ends WITHOUT a trailing newline will have the next cat-append welded onto it, silently
  merging two source paragraphs. End such Edits with `\n`. The chunk-file method above sidesteps it.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 / 五平; now Gero
Shōbei Yasuji), Shimotsuge Jirōzaemon (下柘植次郎左衛門 / 次郎左衛門), Kisaru (木さる / key 木猿; given
name 簾 Ren), Kuroami (黒阿弥, dead ch13). Kohagi (小萩) and Imai Sōkyū (今井宗久 → bare "Sōkyū") the
other leads. Mari Dōgen (摩利洞玄 / 洞玄; dead ch14; here referred to as 洞玄 "Dōgen"), Mochizuki
Gyōbuzaemon (望月刑部左衛門), Maeda Gen'i (前田玄以 / 玄以; office 京都奉行 the Kyoto magistrate), Ishida
Mitsunari (石田三成 / 石田治部少輔 → "Ishida, the Jibu-no-shō"), Hakkansai (抜関斎 = Sasaki Yoshikata),
Jōtei (承禎入道), Yodo-gimi (淀君), Hideyori (秀頼; お拾 O-Hiroi), Maeda Toshiie (利家). Places:
阿弥陀ヶ峰 → **Amidagamine** (do NOT drift to "Amida-ga-mine"), 吉野 Yoshino, 吉野山 Mount Yoshino,
方広寺 Hōkō-ji, 羅刹谷 Rakshasa Valley, 御斎峠 Otogi Pass, 伏見 Fushimi, 大坂/大坂城 Ōsaka/Ōsaka Castle
(macron!), 小松谷 Komatsudani, 天竺 → **Tenjiku** (per ch07; NOT "India"), and the province/city rows
(Iga/Kōga/Ōmi/Yamashiro/Sakai/Ōsaka/Nara/Gifu). Terms: Marishiten (摩利支天), Kōga Saburō (甲賀三郎),
rappa (乱波), Mimi of Nabari (名張ノ耳). NOT glossaried by design: bare 摩利 "Mari"; 化生 keshō; the
fictional drug かすり and 偸盗術; the single-chapter names — B15's Dokutan (毒潭 the wandering monk),
Keikyokusai (荊棘斎 Jūzō's painter alias), Kiheiji of Kawabata (川ノ端の喜平次), Imai Sōkun (宗薫),
Konishi Ryūsa/Yakurō, Hosokawa Tadaoki, Tsuda of the Tennōjiya, Shibatsuji Riemon; and the geography
markers 甘南備(Mount Kannabi)/伎和野(Kiwano)/木津川(Kizu-gawa) — used and kept CONSISTENT in ch16
(甘南備→Kannabi / 甘南備山→Mount Kannabi, 伎和野→Kiwano, 木津川→Kizu-gawa; 伊賀下柘植郷→"the Shimotsuge
district of Iga"); and B16's one-off genin name 伊庭ノ横足→Iba no Yokoashi. Historical one-offs footnoted
not glossaried: Akechi/惟任日向守, 蜂須賀正勝, 伊勢三郎義盛, 弁財天 Benzaiten, 粟田口 the sword school; and
B16's 甘南備/kannabi, 木津川/Kizu-gawa, 八幡/Hachiman, 仮祝言/kari-shūgen (all footnoted, not glossaried).
Consult glossary.json, do not re-derive.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, terse, blunt (わし); the book's centre. In ch15 he
  hides in a Gojō inn as the painter "Keikyokusai"; the wandering monk Dokutan (sent by Kohagi to
  break his ambition) sees through him. Their long duel of minds ends in a draw — Jūzō learns Kohagi
  has become human out of love for HIM, lets a single tear and a cold smile pass in feigned sleep,
  and holds to his road: "I am fond of hell, and so to hell I go." Wry, cold nerve; a real softness
  he despises. Bound for Kiwano/Fushimi.
- **Kazama Gohei (五平 / Gero Shōbei):** cold, clerkly, androgynous; in ch15 his real hunger turns to
  GOLD, not rank. Extorts Sōkyū for 2000 gold (buried at the Kiwano Hachiman torii), writes to Kisaru
  half in genuine longing (the first crack of love in him — "the edge going off me"), summons her
  with three Shimotsuge genin, promises marriage and a rich life. Superior わし/じゃ to inferiors;
  formal-cold to Gen'i/Sōkyū; teasing to Kisaru. In ch16 he leads the Kiwano rendezvous into Kohagi's
  ambush and shows his full ice: reading the trap from the silence, he throws his sword and then throws
  KISARU herself as decoys and slips away — "the shinobi reflex bred into his body; into it entered no
  honor, no human feeling, not even a will of his own." In ch17 he is loose, sunburnt and disguised as
  a horse-driver in the capital, unable to return to the magistrate's residence, and being shadowed.
- **Kohagi (小萩):** Sōkyū's adopted daughter, a Mochizuki-of-Kōga shape-shifter planted on Sōkyū by
  Ishida; born a Sasaki(Rokkaku) daughter of Ōmi. Cool courtly poise (ございます/ませ; self-refers
  "Kohagi"). In ch15 she DEFIES Sōkyū's order to slaughter Gohei's band: she means to take them alive,
  pin the capital's banditry on them, and expose Sōkyū to Ishida — all to keep the wounded Jūzō out
  of danger; she longs to quit the rappa life and be an ordinary woman. Weeps for a love she cannot
  name. In ch16 her twenty Kōga men (led by the old nurse) ambush at Kiwano.
- **The old nurse (嫗/楠 Kusu):** Kohagi's Kōga foster-mother; small, cold, sly, teasing, a freezing
  white-eyed stare. Formal-servile ございましょう with a blade under the smile; runs the Kiwano ambush
  in the field.
- **Kisaru (木さる / given name 簾 Ren):** Shimotsuge's daughter, spirited, blunt, Iga dialect
  (じゃ/のじゃ, self-refers 木さる/わたくし); still aching for Jūzō under the bravado. In ch15 she agrees
  to marry Gohei for her own advantage (citing old Kiheiji's worldly counsel) and brings the three
  genin to the Kiwano rendezvous. The chapter's warmest, most contracted voice. In ch16 Gohei sells
  her to the Kōga ambush as a decoy; she survives by her father's "take the cut" doctrine — sacrifices
  her left hand to plant a shuriken in a Kōga man's face, escapes maimed, and at the Kizu-gawa
  renounces the world of the two men she loved (Gohei's pain she can share, Jūzō's she never could),
  laughs carefree, and trudges home to Iga. Likely off-stage now.
- **Maeda Gen'i (前田玄以):** the shrewd, life-clinging Kyoto magistrate (opens ch15 polishing his 108
  walnuts); secretly tilting to the Tokugawa; lets Gohei run the Iga work his own way. Off-stage after
  the opening of ch15.
- **Imai Sōkyū (宗久):** the great Sakai merchant-magnate (Ōkurakyō Hōin); grave, sardonic, unhurried,
  a blade under the yawn. In ch15 Gohei breaks into his villa and extorts him; Sōkyū orders Kohagi to
  wipe out Gohei's band. Formal by design.
- **Dokutan (毒潭):** the wandering Zen monk (ch15 only, likely), earthy/booming/roguish/wise; loves
  Kohagi, sent by her to shatter Jūzō's ambition; fails, and Jūzō lets him go. His discourse (prajñā,
  mappō, the beast-realm) is grave but living; his banter contracted.

## Where the story stands (end of ch16)
Bunroku 3 (1594). The night of the Kiwano rendezvous. Gohei leads his band — Kisaru and three
Shimotsuge genin — up the ruined-village road below Mount Kannabi to the old Hachiman shrine where
Sōkyū's 2000 gold lies buried, and walks into the Kōga ambush Kohagi's people have laid. (Sōkyū had
ordered the band wiped out; Kohagi meant to take them alive to shield Jūzō, but in the field the old
nurse's men mean to kill.) Gohei reads the trap from the silence, throws his sword as a decoy and then
throws KISARU as a decoy — selling her to the pursuers to buy his own escape, purely on shinobi
reflex. Kisaru survives by her father's "take the cut" doctrine: she takes the downstroke on her
raised left arm, kills her attacker with a right-hand shuriken, and crawls away maimed. At the
Kizu-gawa she washes the stump, weeps, and reckons the difference between the two men — Jūzō would
make this agony a rapture offered to his god and would never understand her; Gohei would weep as she
weeps. She resolves to vanish from the world where she chased a man, and trudges home to Shimotsuge in
Iga. Gohei is loose and hunted; Jūzō's death-bound purpose still points at Fushimi. Three lines of the
plot now run on: Gohei's flight, Kohagi's failed rescue, Jūzō's road to the Taikō.
ch17 尾行 / The Shadowing (opener clean on folio 584, offset 0) opens weeks later, early summer, at the
Gion Yasaka shrine steps in the capital: Gohei, sunburnt and disguised as a horse-driver, unable since
Kiwano to return to the magistrate's residence, is himself now being shadowed by a Kōga assassin.

## Next batch
B17 = ch17 尾行 / The Shadowing, printed folios 584-590 (opener clean on folio 584 = PDF 584, offset 0 —
printed == PDF, CONFIRMED through 585 at end of B16; ch16 ended on 583 and does NOT spill onto 584).
ch17 body begins with 夏も間近くなったある日の午後、祇園八坂神社の石段下… (Gohei disguised as a horse-driver
at the Gion Yasaka steps, being shadowed). READ folios off the running heads to confirm printed == PDF
holds. Then B18 = ch18 石田屋敷 / The Ishida Mansion, folios 591-607.

## Open traps / environment
- **Offset is 0 (folio == PDF) and should stay so to the end.** READ folios off the running heads
  each batch (very faint — topstrips.py + autocontrast); skip any duplicate leaf; re-map from any
  SKIPPED folio; build data/pagemap for the span.
- **The folios 404-405 scan gap is PERMANENT and already handled in ch12.** Do NOT try to bridge it.
- A chapter's tail can spill onto the next opener folio (ch03/04/06/07/08/09/10/11/12/13/14/15 all
  did) — render the next opener and verify; make sure the next batch does not re-translate the
  spillover. NOTE: ch16 did NOT spill — it ended cleanly on folio 583, and ch17 尾行 opens fresh at the
  top of 584. Still render the ch18 opener (591) and check whether ch17 spills onto it.
- **pagemap indices must be UNIQUE per body_paragraph.** The builder inverts the list to
  {body_paragraph: printed_folio}, so two folios mapping to the same paragraph collide (ch15's map had
  a 508/509→0 collision that silently dropped 508). When a chapter opens mid-page on a title-only
  folio (ch16's 566), OMIT that folio from the pagemap and start at the first folio carrying body.
- Furigana leakage and dropped clauses cluster on the DENSE opener and the TAIL. Re-read both
  against the scan and run the compound-coverage grep before shipping. On dense interleaved pages,
  read the columns RTL and cross-check order against the raw OCR (data/txt).
- **assemble.py OVERWRITES data/zh/chNN.txt AND welds paragraphs** — hand-transcribe from images
  via the chunk-file method (scratchpad/zh + scratchpad/en, one para per line, python-assembled).
- qc_entities / check_content want the rendered name once per paragraph the character appears in
  — do a name-survival pass over pronoun-only paragraphs (B10 fixed 20, B11 8, B12 6, B13 8, B14 2,
  B15 16). Match the glossary `en` form exactly, macrons included (B15: "Osaka"→"Ōsaka" flagged;
  render 天竺 as "Tenjiku" not "India" to match the shelf). check_content is authoritative;
  qc_entities over-flags place-keys inside common words (declare those, e.g. 甲斐/Kai).
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py (notes/figures) or the
  Write/Edit tool or a python json load/dump (glossary), then re-read to verify. (Plain-text
  data/noise.txt via a heredoc is fine — it's not JSON — but re-read to confirm.)
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words; place ⊂ compound).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution); if you run
  a post-hoc pass, watch clause-final over-contraction ("you're."/"there's." are ungrammatical).
  Keep grave uncontracted lines ONLY for deliberately-formal registers. ch16 ran 1.98x (night-ambush
  action, contracted, clean); ch17 is shadowing/suspense — narration-forward with contracted street
  dialogue, expect above 1.0x.
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled. If `import fitz` fails, `pip install -q pymupdf`.
  Pre-existing checker-regression FAIL (hook stands down on template stub) is unrelated; leave it.
