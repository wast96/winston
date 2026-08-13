# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B12

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B12 = ch12 「吉野天人」 (The Celestial Maiden of Yoshino), printed folios 397-424, end to end per the CLAUDE.md pipeline. OFFSET AT THE START IS STILL +2: folio = PDF render page minus 2 (PDF 399 = folio 397, the ch12 opener, CONFIRMED at the end of B11; PDF 400 = folio 398). BUT the +2 span is expected to END somewhere in folios 397-425 via a 1-leaf scan gap that re-maps the offset back to 0 (book.json says printed == PDF again from folio 425). DO NOT COMPUTE THE OFFSET — READ the folio off the running head of EVERY rendered page across this span, watch for a SKIPPED folio (that skip is the gap: from that page on the offset drops toward 0) or any further duplicate leaf, and re-map from the page where it changes. Build data/pagemap/ch12.json for the span (ch10.json / ch11.json are the format model: entries {printed, pdf, body_paragraph} where body_paragraph is the 0-based index into data/zh/ch12.txt body paragraphs, title excluded). Confirm the ch13 opener 水狗 (book.json: printed 425, pdf 425 — i.e. offset back to 0) and flag exactly where the offset changed.

ch12 body begins on folio 397 AFTER the 吉野天人 title with 文禄三年二月二十七日、太閤秀吉は、養子秀次、家康、利家と輿をつらねて吉野山に遊んだ。朝鮮ノ役の収拾は漸く思わしくなく畿内の人心に微妙な動揺が伝えられて… . ch11's tail SPILLS onto folio 397 BEFORE that title (7 paragraphs, source lines 225-231 of data/zh/ch11.txt: 呟きつつ…であろうか。 / 「お目覚めなさいました？」 / 「ふむ」 / 重蔵は、小萩のほうを… / 「あさげが、あちらに」 / 「頂く」 / 顔を洗うために、重蔵は庵を出て谷間へおりた。…重蔵は考えた。); those are DONE in ch11 — do NOT re-translate them. BEFORE translating, read the final two pages of ch11's English (the tail of out/ch11_reading.md) so the voice carries.

ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch12_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write (Jūzō blunt わし; Kuroami humble ござる; Kisaru dialect わし/じゃ and self-reference "Kisaru"; low-city voices) — do NOT leave "It is/I do not/you are" everywhere; keep the grave uncontracted line only for deliberately-formal registers (Kuroami's ござる, obsequious まする to a lord, quoted documents/scripture, a courtier's or Hideyoshi's formal speech). ch05/ch08 both needed a whole contraction pass afterward; ch06 ran formal-by-design at 0.74x and passed, ch09 ran 1.21x, ch10 (dialogue-heavy) ran 2.31x, ch11 ran 1.62x — a court/exposition chapter may sit below 1.0x, but 0.0x is a draft error, not "formal by design". NOTE: ch12 opens with a Hideyoshi court set-piece at Yoshino (the Taikō, Hidetsugu, Ieyasu, Toshiie; the Korea campaign faltering) — that framing exposition is formal-by-design; the ninja scenes are not.

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled). The pre-existing checker-regression FAIL "hook stands down on template stub" is unrelated; leave it.
2. OCR: render.py 399 427 --dpi 300 (folio 397 = PDF 399; render a few pages past the expected ch13 opener 425 to catch the offset re-map and the ch13 opener); then ocr_crop.py 399 427 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 399 427. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls). CHECK each rendered page's running-head folio: expected folio = PDF - 2 UNTIL the gap, then it steps toward printed == PDF. A folio that repeats the previous folio is a double-feed (skip it); a SKIPPED folio is the gap (re-map from there).
3. find_figures.py 399 427 AND eyeball every page for line art (ch01-ch11 were all text-only; if ch12 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by READING the rendered page images directly (data/png/p0NNNN.png) and hand-build data/zh/ch12.txt as a corrected, paragraph-aligned transcription (the parity surface). scratchpad/crop.py 6x-renders a page-fraction rectangle (crop.py PAGE x0 y0 x1 y1 [zoom]; PAGE 1-based; fractions of the full page; reads furigana AND faint running-head folios cleanly — the running heads are VERY faint, crop the top strip 0.0 0.02 1.0 0.075 at zoom 10 and autocontrast). Re-create crop.py if the container recycled (body in "Tooling in place" below). Interleaved narration/dialogue mis-orders from the full page — crop the columns and read right-to-left, top-to-bottom literally; a quote 「…」 that starts a column with と/narration after it is embedded, but treat each 「…」 line and each narration run as its own paragraph (dialogue lines are their own paragraphs). Force-add data/zh/ch12.txt (data/zh/ is gitignored). Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch13 opener folio and check whether ch12's tail spills onto it, and make sure B13 does not re-translate any spillover. COVERAGE cross-check after transcribing: extract every 3+-kanji compound from the raw data/txt OCR (over the ch12 PDF span, excluding any duplicate leaves) and confirm each appears in your HAND data/zh/ch12.txt — garbles are expected; a clean meaningful compound that is absent is a real drop to fix (the B11 script: python one-liner over data/txt with a Counter of [一-鿿]{3,}).
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Hidetsugu/Ieyasu/Toshiie/Kyoto/Yoshino/Tokugawa). Principal cast and majors are decided in glossary.json; reuse unchanged and record in PROGRESS which rows you reused. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans. Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False indent=2, or the Edit tool — the B04-B11 method, NOT apparatus_merge which flattens the glossary). AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter (B11 hit 甲斐々々しく matching the province key 甲斐 — a declared qc false positive). Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch12_reading.md, settle the English title at translation ('## The Celestial Maiden of Yoshino' unless a better reading emerges — 天人 is the Buddhist tennin/apsaras, a heavenly being; footnote at first body appearance if the title's sense is not obvious). Add a ch12 entry to data/checks.json (docs + sources). make_bilingual.py ch12 (parity FIRST). Then run: verify_unit.py ch12; check_structure.py --pairs data/zh/ch12.txt out/ch12_reading.md; check_align.py ch12; qc_entities.py out/ch12_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch12_reading.md. (qc/content want the rendered name once per paragraph the character appears in — do a name-survival pass over any pronoun-only paragraph, as in B10/B11; check_content is authoritative, qc_entities over-flags place-keys inside common words.)
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch11 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office (治部少輔)/太閤(Taikō) titles, Sakai the free-city, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu/Hideyori(お拾/O-Hiroi), Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours and 半刻/小半刻, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures (shaku/chō/koku/ri/ken/kin/tsubo/jō/kan/kanmon), rappa/shinobi/jōnin/genin, jizamurai/gōshi, くノ一/kunoichi, 忍び文字/shinobi-moji, Marishiten, the Udaifu/Naifu court titles, Yodo-dono(淀君)/Odani, Rokkaku/Sasaki Yoshikata (Hakkansai/Jōtei) & Kannon-ji 1568, the 1487 Magari campaign, the fifty-three houses of Kōga, Kōga Saburō, the Odawara campaign, Nagoya castle in Hizen, Hattori Hanzō, the Jurakudai, the go-bugyō, the Iga-goe, Miyamoto Musashi & the Yoshioka, Kashima/Katori & Bokuden, 陽忍/陰忍 open-way/shadow-way, the Bon send-off, shōchū, the Kyoto-to-Kōga escape route, AND the B11 first-appearances: the Buddhist precepts / Mahāsāṃghika Vinaya / Buddhabhadra, Empress Jitō's no-kill decree, 化生/keshō (shape-shifter), the Mochizuki house of Kōga, Ren (Kisaru's given name). Note only ch12's NEW first-appearances (likely candidates: 吉野/Yoshino & its cherry-blossom cult, the 天人/tennin, whatever new offices, places, and the Korea-campaign specifics come up). Anchor notes to BODY phrases (verbatim substrings), not heading-only text. Add via apparatus_merge.py (batch JSON file, numeric char refs OR literal chars in bodies — NEVER a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, the renderings reused/added), INCLUDING the confirmed folio-to-PDF map for this span, WHERE the +2 offset ends (the gap page), and the data/pagemap/ch12.json you built.

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B13 kickoff (ch13 「水狗」 The Water Dog, printed folios 425-455; offset should be 0 by then — printed == PDF — but READ folios to confirm the gap landed where you found it) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure in book.json; metadata set; skeleton EPUB built; page
  furniture measured (crop L0.035 R0.965 T0.075 B0.955; model jpn_vert psm5). Offset: 0 for
  folios 7-325; **+2 from folio 326 (PDF 328) through folio 397 (PDF 399), CONFIRMED unbroken
  by B09/B10/B11**; a 1-leaf gap somewhere in 397-425 re-maps back to 0 by folio 425 (B12/B13).
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
- **B11 = ch11 伊賀ノ山 / The Hills of Iga (373-396, tail on 397): COMPLETE.** 230 paragraphs,
  6 new notes (book total 87). All checks green (parity 230|230, numbers 0/230, check_content
  clean, apparatus clean, register 1.62x ref within tolerance, align median 11.43, qa_epub PASS,
  epubcheck 0/0/0/0). data/pagemap/ch11.json built (25 entries, folios 373-397). NO figures.
  Added glossary rows 淀君→Yodo-gimi, 秀頼→Hideyori. ch11's tail (7 paras) spills onto folio 397
  before the 吉野天人 title — B12 must not re-translate lines 225-231 of data/zh/ch11.txt.

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
  present (substring) and only uses `en` that are Capitalised, slash-free and >= 4 chars (so bare
  "Dōgen" satisfies qc where 摩利洞玄 appears, but check_content wants "Mari Dōgen" there — render
  the full form in 摩利洞玄 paragraphs). **check_content is the authoritative displacement check;
  qc_entities over-flags a place-key that sits inside a common word (B11: 甲斐 inside 甲斐々々しく
  "assiduously") — verify against the scan and DECLARE it in PROGRESS rather than mis-rendering.**
- `data/checks.json`: the {docs, sources} config. ch01-ch11 in.
- `data/noise.txt`: check_numbers noise. B10 added `三昧`; B09 added the roster/name numerals.
  Extend per its header, longest literal first, one comment line each; never noise a real
  quantity you dropped (fix the English to carry it). B11 added NOTHING.
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens glossary
  rows to the ROOT, so since B04 add glossary rows DIRECTLY into the sections (Edit tool, or json
  load/dump ensure_ascii=False indent=2). Notes and figures merge fine via apparatus_merge.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder refuses a
  heading-only anchor. Note bodies: literal Unicode is fine (em dash, macrons, curly quotes) OR
  numeric character references; only NAMED HTML entities (&nbsp; &mdash;) are rejected. Author
  the notes batch as a JSON FILE (Write tool) and run apparatus_merge.py on it — never a heredoc.
- **Substring trap for glossary keys:** do NOT add a bare-name row whose romanization is a
  substring of a fuller row in use (宗久⊂Imai Sōkyū). SAFE full+bare pairs (重蔵/葛籠重蔵,
  摩利洞玄/洞玄, 望月刑部左衛門/刑部左衛門, 淀君, 秀頼) are fine and used. When a place key collides
  as a substring of another word (山城 Yamashiro inside 釜山城 Pusan castle; 甲斐 Kai inside
  甲斐々々しく), prefer the longer key or DECLARE the false positive.
- **SCANNER DOUBLE-FEED (found B09):** PDF 326/327 are re-scans of folios 324/325, so
  **folio = PDF - 2 from PDF 328 through PDF 399 (= folio 397), CONFIRMED unbroken by B11.**
  A 1-leaf gap somewhere in folios 397-425 re-maps to printed == PDF by folio 425. CHECK the
  folio on every rendered page in B12; a SKIPPED folio marks the gap (re-map from there).
- **scratchpad crop.py** (re-create if the container recycled): renders a fractional rectangle
  of a source.pdf page at high zoom so furigana AND the faint running-head folio are legible.
  Signature `crop.py PAGE x0 y0 x1 y1 [zoom]` (PAGE 1-based; fractions of the full page; default
  zoom 6). Uses `import fitz` (pymupdf), opens /home/user/winston/source.pdf, clips to the rect,
  saves scratchpad/_crop.png. Read the png to eyeball furigana; for running-head folios crop
  the top strip (e.g. 0.0 0.02 1.0 0.075 at zoom 10) and autocontrast with PIL (ImageOps.
  autocontrast cutoff=2) — the folios are very faint but readable enhanced (do NOT hard-threshold,
  it turns corner smudges into blobs).
- **Method:** hand-transcribe from the page images; use a top-strip crop to read running-head
  folios and paragraph INDENTS, since assemble.py mis-groups AND overwrites data/zh/chNN.txt.
  Dialogue lines are their own paragraphs; a paragraph is a new line only when the source column
  is INDENTed at its top (a non-indented column-top after a sentence-end is the SAME paragraph
  continuing). Interleaved narration/dialogue on dense pages mis-orders from the full page — crop
  columns and read right-to-left literally. Flush the transcription to a scratch build file per
  few pages so a context summary can't lose it, then cp to data/zh and force-add.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 / 五平),
Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木さる / key 木猿; given name 簾 Ren, footnoted
ch11), Kuroami (黒阿弥). Kohagi (小萩) and Imai Sōkyū (今井宗久 → bare "Sōkyū") are the other leads.
Mari Dōgen (摩利洞玄 / 洞玄; birth name 伴藤内 Ban Tōnai; byname 甲賀ノ摩利), Mochizuki Gyōbuzaemon
(望月刑部左衛門 / 刑部左衛門), the Mochizuki house of Kōga (望月家, prose), Maeda Gen'i (前田玄以 /
玄以; Kyoto magistrate; Dōgen lodges at his tenement), Ishida Mitsunari (石田三成 / 三成; office
石田治部少輔 → "Ishida, the Jibu-no-shō"), Hakkansai (抜関斎 = Rokkaku/Sasaki Yoshikata), Jōtei
(承禎入道). NEW in B11 glossary: 淀君 Yodo-gimi, 秀頼 Hideyori (infant name お拾 O-Hiroi, prose+note).
Terms: Marishiten (摩利支天), Kōga Saburō (甲賀三郎), rappa (乱波). NOT glossaried by design: bare
摩利 "Mari"; 化生 keshō ("shape-shifter", footnoted ch11, kept free in prose); Gen'i's aliases
徳善院/半夢斎 (prose only); ch10 route markers (Shibutani/Daigo/Uji river/Gō-no-kuchi/Matsubara);
ch11 single-appearance names (三条西家/岩倉/一乗寺, and the Jitō place-names Takashi-no-umi/
Muko-no-umi/Nagi-no/Mi-no, covered in the Jitō note). Earlier rows (Nobunaga, Hideyoshi, Ieyasu,
Gen'i, Sōkyū, Hattori Hanzō, Iga/Kōga/Ōmi/Yamashiro/Sakai/Ōsaka/Nara/Gifu, 方広寺 Hōkō-ji, おとぎ峠
Otogi Pass, the measures, etc.) are all in glossary.json — consult it, do not re-derive.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, terse, blunt (わし). Plays a long waiting game for
  the Toyotomi collapse; will NOT leave the capital or betray the work. In ch11: the great
  self-portrait speech (the ninja as a lodging-house of many selves, no fixed "I"); confesses he
  is genuinely smitten with Kohagi "as one rappa to another" but refuses to flee — "a man tires
  of the woman he loved, never of his work." The morning-after tenderness unnerves him more than
  any fight; he leaves to wash his face and never returns to the hermitage. Wry, dry.
- **Kuroami:** Jūzō's aged genin (past fifty), under five shaku, boy's face; humble archaic
  ござる/申す, superstitious and fearful, practical. Fronts as the whetter "Iseya Kahei." In ch11
  brings word of Hideyori's birth and fixes the killing for next year's seventh month, shivering
  with fearful glee. Refers to Jūzō as "Master Jūzō".
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter; in fact a Mochizuki-of-Kōga shape-shifter
  planted on Sōkyū by Ishida Mitsunari to expose the plot (Jūzō names it in ch11; she does not
  deny it). Cool unbreakable courtly poise (ございます/ませぬ; self-refers as "Kohagi"), but openly
  in love with Jūzō — asks him to flee and abandon the plot, grants him one night, warns her own
  work may be to kill him, cooks him a devoted morning meal. The love AND the danger are real.
- **Kisaru (木さる / given name 簾 Ren):** Shimotsuge Jirōzaemon's daughter, a full lead. Spirited,
  blunt, dialect (わし/じゃ; self-reference "Kisaru"), moods change with violence. In ch11's
  Komatsudani flashback she is caught breaking into Kohagi's lodging (fearless, jealous of Kohagi
  over Jūzō, wants Dōgen's whereabouts to avenge her father and "win" Jūzō); Kohagi jails her in
  the storehouse cell (jealousy + intelligence). Wounded, growing up fast.
- **Mari Dōgen (甲賀ノ摩利洞玄):** the aged Kōga rappa (past fifty, robust); folksy, blunt, wry,
  self-mocking (わし/じゃ/のう/そこもと/おぬし). Lost his left hand to Jūzō in ch10, escaped; now
  lodges at Maeda Gen'i's Kyoto tenement (per ch11). Off-stage in ch11.
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly. Now Gero Shōbei Yasuji, raised to
  300 koku by Gen'i. Superior わし/じゃ to inferiors, obsequious ます/です to a master. Off-stage
  in ch11 (last seen ch10 discarding Kisaru).
- **Maeda Gen'i (徳善院/半夢斎):** the shrewd Kyoto magistrate, a "true villain" who keeps a debt
  more faithfully than any good man; secretly tilting to the Tokugawa. Off-stage in ch11.

## Where the story stands (end of ch11)
Kuroami brings word that Yodo-gimi has borne Hideyoshi a son (O-Hiroi / the future Hideyori,
Bunroku 2 = 1593); the plotters fix the killing for the seventh month of the coming year, to
fall as the Taikō's death-anniversary. Kohagi comes to Otogi Pass with Sōkyū's money and the
story of catching and jailing Kisaru at Komatsudani. Through the night Jūzō names her a
Mochizuki-of-Kōga shape-shifter, planted on Sōkyū by Ishida Mitsunari to expose the plot, and
tells her that, left as they are, she and he must end as sworn enemies. She begs him to flee
with her; he refuses (the work outweighs the woman) but confesses he is truly smitten and grants
her one night. In the morning her tenderness so shakes his discipline that he leaves to wash his
face and never returns, taking the ridge road toward Yamashiro. ch12 吉野天人 / The Celestial
Maiden of Yoshino (opener on folio 397) turns to Hideyoshi's court: on Bunroku 3/2/27 (1594) the
Taikō, with Hidetsugu, Ieyasu and Toshiie, makes his famous cherry-blossom progress to Mount
Yoshino, while the Korea campaign falters and the capital region grows uneasy.

## Next batch
B12 = ch12 吉野天人 / The Celestial Maiden of Yoshino, printed folios 397-424 (opener PDF 399 =
folio 397, offset +2 CONFIRMED at start). ch12 body begins AFTER the 吉野天人 title on folio 397
(文禄三年二月二十七日、太閤秀吉は、養子秀次、家康、利家と輿をつらねて吉野山に遊んだ…); ch11's tail
(7 paras before the title, lines 225-231) is done. THE +2 OFFSET ENDS SOMEWHERE IN 397-425 via a
1-leaf gap — READ folios off every running head, do not compute; re-map from the skipped folio.
Then B13 = ch13 水狗 / The Water Dog, folios 425-455 (book.json: printed 425 == PDF 425, i.e.
offset back to 0 by then).

## Open traps / environment
- **Offset is +2 at the start of B12 (folio 397 = PDF 399) but ENDS in 397-425 via a 1-leaf gap.**
  READ folios off the running heads (very faint — top-strip crop + autocontrast); skip any
  duplicate leaf; re-map from any SKIPPED folio; build data/pagemap for the span; confirm
  ch13 opener 水狗 at printed 425 (== PDF 425).
- A chapter's tail can spill onto the next opener folio (ch03/04/06/07/08/09/10/11 all did) —
  render the next opener and verify; make sure the next batch does not re-translate the spillover.
  ch11's tail (7 paras) is on folio 397; ch12 body starts after the 吉野天人 title.
- Furigana leakage and dropped clauses cluster on the DENSE opener and the TAIL. Re-read both
  against the scan and run the compound-coverage grep before shipping.
- **assemble.py OVERWRITES data/zh/chNN.txt AND welds paragraphs** — hand-transcribe from the
  images; use a top-strip crop to read indents (indent = new paragraph; non-indented column-top
  after a sentence-end = same paragraph continuing).
- qc_entities / check_content want the rendered name once per paragraph the character appears in
  — do a name-survival pass over pronoun-only paragraphs (B10 fixed 20, B11 fixed 8). Match the
  glossary `en` form exactly. check_content is authoritative; qc_entities over-flags place-keys
  inside common words (declare those).
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py (notes/figures, from a
  JSON file) or the Write/Edit tool or a python json load/dump (glossary), then re-read to verify.
  (Plain-text data/noise.txt via a heredoc is fine — it's not JSON — but re-read to confirm.)
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words; place ⊂ compound).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution); if you run
  a post-hoc pass, watch clause-final over-contraction ("you're."/"there's." are ungrammatical).
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled. Pre-existing checker-regression FAIL (hook stands
  down on template stub) is unrelated to this book; leave it.
