# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B13

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B13 = ch13 「水狗」 (The Water Dog), printed folios 425-455, end to end per the CLAUDE.md pipeline. OFFSET IS NOW 0: printed == PDF (folio 425 = PDF 425, CONFIRMED at the end of B12 — the +2 offset ended via a 1-leaf scan gap that dropped printed folios 404-405, re-mapping the offset to 0 from PDF 406 / folio 406). Do NOT assume — READ the folio off the running head of EVERY rendered page across this span to confirm printed == PDF holds, and watch for any further duplicate leaf or gap. The running heads are VERY faint: use scratchpad/topstrips.py FIRST LAST to stack the top strips of a page range into one image (top strip 0.0 0.02 1.0 0.075 at zoom ~9-10, autocontrast). book.json: ch14 opener 修羅 (Carnage) at printed 456 == PDF 456. Build data/pagemap/ch13.json for the span (ch11.json / ch12.json are the format model: entries {printed, pdf, body_paragraph} where body_paragraph is the 0-based index into data/zh/ch13.txt body paragraphs, title excluded). Confirm the ch14 opener 修羅 and flag whether ch13's tail spills onto it.

ch13 body begins on folio 425 AFTER the 水狗 title with 吉野から京へもどった黒阿弥は、方広寺裏の研店をにわかに畳むと、すぐその足で羅刹谷の荒れ寺に籠った。ひとり、ふたりと、一旦は飼い放した乱波を、丹念に呼び集めはじめたのである。 . ch12's tail SPILLS onto folio 425 BEFORE that title (5 paragraphs, source lines 209-213 of data/zh/ch12.txt: つと立ち去りかける重蔵の編笠の中へ… / 「京に戻れば、小萩を成敗…」 / 「そちはどうする」 / 「散った乱波どもを集めて…」 / 歯をむいて、天明の村道を歩きながら…); those are DONE in ch12 — do NOT re-translate them. BEFORE translating, read the final two pages of ch12's English (the tail of out/ch12_reading.md) so the voice carries.

ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch13_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write (Jūzō blunt わし; Kuroami humble ござる/申す; low-city rappa voices) — do NOT leave "It is/I do not/you are" everywhere; keep the grave uncontracted line only for deliberately-formal registers (Kuroami's ござる, obsequious まする to a lord, quoted documents/scripture, a courtier's or Hideyoshi's formal speech). ch05/ch08 both needed a whole contraction pass afterward; ch06 ran formal-by-design at 0.74x and passed, ch09 1.21x, ch10 (dialogue-heavy) 2.31x, ch11 1.62x, ch12 1.86x — a court/exposition chapter may sit below 1.0x, but 0.0x is a draft error, not "formal by design". NOTE: ch13 水狗 opens with Kuroami re-gathering the scattered rappa at the Rakshasa Valley ruin — a low-city thieves'/ninja register, not court.

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled). The pre-existing checker-regression FAIL "hook stands down on template stub" is unrelated; leave it.
2. OCR: render.py 425 457 --dpi 300 (folio 425 = PDF 425; render a few pages past the expected ch14 opener 456 to catch the ch14 opener and any drift); then ocr_crop.py 425 457 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 425 457. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls). CHECK each rendered page's running-head folio: expected folio == PDF. A folio that repeats the previous folio is a double-feed (skip it); a SKIPPED folio is a gap (re-map from there).
3. find_figures.py 425 457 AND eyeball every page for line art (ch01-ch12 were all text-only; if ch13 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by READING the rendered page images directly (data/png/p0NNNN.png — files are named p0425.png etc., 4-digit) and hand-build data/zh/ch13.txt as a corrected, paragraph-aligned transcription (the parity surface). scratchpad/crop.py 6x-renders a page-fraction rectangle (crop.py PAGE x0 y0 x1 y1 [zoom]; PAGE 1-based; fractions of the full page; reads furigana AND faint running-head folios cleanly). scratchpad/topstrips.py FIRST LAST stacks running-head strips of a page range into one image for fast folio reading. Re-create crop.py / topstrips.py if the container recycled (bodies in "Tooling in place" below). NOTE: the full-page images at 300dpi (~1112x1725) are LEGIBLE enough to transcribe directly, cropping columns only for interleaved dense pages and uncertain names/furigana (the B12 method — far faster than half-page crops). Interleaved narration/dialogue mis-orders from the full page — crop the columns and read right-to-left, top-to-bottom literally; treat each 「…」 line and each narration run as its own paragraph. Force-add data/zh/ch13.txt (data/zh/ is gitignored). Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch14 opener folio and check whether ch13's tail spills onto it, and make sure B14 does not re-translate any spillover. COVERAGE cross-check after transcribing: extract every 3+-kanji compound from the raw data/txt OCR (over the ch13 PDF span, excluding any duplicate leaves) and confirm each appears in your HAND data/zh/ch13.txt — garbles are expected; a clean meaningful compound that is absent is a real drop to fix (python one-liner over data/txt with a Counter of [一-鿿]{3,}).
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Ieyasu/Tokugawa/Kyoto/Yoshino). Principal cast and majors are decided in glossary.json; reuse unchanged and record in PROGRESS which rows you reused. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans. Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False indent=2, or the Edit tool — the B04-B12 method, NOT apparatus_merge which flattens the glossary). AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter. Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch13_reading.md, settle the English title at translation ('## The Water Dog' — 水狗 is literally "water-dog"; per book.json translator_note several section titles are evocative codenames or emblems rather than plain place-names — footnote at first body appearance if the sense is not obvious). Add a ch13 entry to data/checks.json (docs + sources). make_bilingual.py ch13 (parity FIRST). Then run: verify_unit.py ch13; check_structure.py --pairs data/zh/ch13.txt out/ch13_reading.md; check_align.py ch13; qc_entities.py out/ch13_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch13_reading.md. (qc/content want the rendered name once per paragraph the character appears in — do a name-survival pass over any pronoun-only paragraph, as in B10/B11/B12; check_content is authoritative, qc_entities over-flags place-keys inside common words.)
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch12 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office (治部少輔)/太閤(Taikō)/内府(Naifu) titles, Sakai the free-city, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu/Hideyori(お拾/O-Hiroi), Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours and 半刻/小半刻, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures (shaku/chō/koku/ri/ken/kin/tsubo/jō/kan/kanmon), rappa/shinobi/jōnin/genin, jizamurai/gōshi, くノ一/kunoichi, 忍び文字/shinobi-moji, Marishiten, the Udaifu/Naifu court titles, Yodo-gimi(淀君)/Odani, Rokkaku/Sasaki Yoshikata (Hakkansai/Jōtei) & Kannon-ji 1568, the 1487 Magari campaign, the fifty-three houses of Kōga, Kōga Saburō, the Odawara campaign, Nagoya castle in Hizen, Hattori Hanzō, the Jurakudai, the go-bugyō, the Iga-goe, Miyamoto Musashi & the Yoshioka, Kashima/Katori & Bokuden, 陽忍/陰忍 open-way/shadow-way, the Bon send-off, shōchū, the Kyoto-to-Kōga escape route, the Buddhist precepts / Mahāsāṃghika Vinaya / Buddhabhadra, Empress Jitō's no-kill decree, 化生/keshō (shape-shifter), the Mochizuki house of Kōga, Ren (Kisaru's given name), AND the B12 first-appearances: Yoshino & its cherry-blossom cult, Maeda Toshiie, the 1595 Hidetsugu purge (三条河原), the Zaō Hall/Kimpusen-ji, the Saigyō hermitage, Noh/takigi-nō/the Kanze school/shite-waki-wakizure, the Noh play 吉野天人 & the tennin/apsaras, the owl-whistle (梟笛), the sasumata. Note only ch13's NEW first-appearances (likely candidates: whatever the 水狗 codename means, new rappa/thieves' argot, the Rakshasa-Valley operation specifics, any new offices/places). Anchor notes to BODY phrases (verbatim substrings), not heading-only text. Add via apparatus_merge.py (batch JSON file with a top-level "notes" key, numeric char refs OR literal chars in bodies — NEVER a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, the renderings reused/added), INCLUDING the confirmed folio-to-PDF map for this span (should be printed == PDF throughout — confirm), and the data/pagemap/ch13.json you built.

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B14 kickoff (ch14 「修羅」 Carnage, printed folios 456-507; offset should still be 0 — printed == PDF — but READ folios to confirm) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure in book.json; metadata set; skeleton EPUB built; page
  furniture measured (crop L0.035 R0.965 T0.075 B0.955; model jpn_vert psm5).
- **Offset history (READ folios, do not compute):** 0 for folios 7-325; **+2 from folio 326
  (PDF 328) through folio 403 (PDF 405), CONFIRMED unbroken by B09/B10/B11/B12**; a **1-leaf scan
  gap dropped printed folios 404-405** (MISSING from the scan), re-mapping the offset back to
  **0 from folio 406 (PDF 406) onward, CONFIRMED through folio 425 = PDF 425**. printed == PDF
  should hold for the rest of the book — confirm by reading running heads each batch.
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
  COMPLETE.** 212 body paragraphs (incl. one scan-gap marker), 10 new notes (book total 97). All
  checks green (parity 212|212, numbers 0/212, check_content clean, qc 0 misses, apparatus clean,
  register 1.86x ref within tolerance, align median 9.50, qa_epub PASS, epubcheck 0/0/0/0). Built
  data/pagemap/ch12.json (27 entries). NO figures. **1-LEAF SCAN GAP: printed folios 404-405 are
  MISSING** (confirmed by content across the boundary); left as an honest gap (body para 37
  truncated, body 38 an editorial marker + footnote, body 39 resumes mid-scene — NO bridging text
  invented). Added glossary rows 利家→Toshiie, 吉野→Yoshino, 吉野山→Mount Yoshino; noise +4
  (万燈会/万余/千本/五節). ch12's tail (5 paras) spills onto folio 425 before the 水狗 title —
  B13 must not re-translate source lines 209-213 of data/zh/ch12.txt.

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
  that sits inside a common word — verify against the scan and DECLARE it in PROGRESS.**
- `data/checks.json`: the {docs, sources} config. ch01-ch12 in.
- `data/noise.txt`: check_numbers noise. B12 added 万燈会/万余/千本/五節 (number-words carried in
  English prose / proper names). Extend per its header, longest literal first, one comment line
  each; never noise a real quantity you dropped (fix the English to carry it).
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens glossary
  rows to the ROOT, so since B04 add glossary rows DIRECTLY into the sections (Edit tool, or json
  load/dump ensure_ascii=False indent=2). Notes and figures merge fine via apparatus_merge (batch
  file needs a top-level "notes"/"figures" key — {"notes": {"chNN": [...]}}).
- **Note anchors:** must be verbatim substrings of the BODY prose. Note bodies: literal Unicode is
  fine (em dash, macrons, curly quotes) OR numeric character references; only NAMED HTML entities
  (&nbsp; &mdash;) are rejected. Author the notes batch as a JSON FILE (Write tool) and run
  apparatus_merge.py on it — never a heredoc.
- **Substring trap for glossary keys:** do NOT add a bare-name row whose romanization is a
  substring of a fuller row in use. SAFE full+bare pairs (重蔵/葛籠重蔵, 摩利洞玄/洞玄,
  望月刑部左衛門/刑部左衛門, 淀君, 秀頼, 五平/風間五平) are fine. When a place key collides as a
  substring of another word, prefer the longer key or DECLARE the false positive. 吉野→Yoshino is
  safe because 吉野山/吉野天人/吉野川/吉野観桜 all render with "Yoshino".
- **scratchpad crop.py** (re-create if the container recycled): renders a fractional rectangle of a
  source.pdf page at high zoom so furigana AND the faint running-head folio are legible. Signature
  `crop.py PAGE x0 y0 x1 y1 [zoom]` (PAGE 1-based; fractions of the full page; default zoom 6).
  Uses `import fitz` (pymupdf), opens /home/user/winston/source.pdf, clips to the rect, autocontrasts
  (PIL ImageOps.autocontrast cutoff=2 — do NOT hard-threshold), saves scratchpad/_crop.png.
- **scratchpad topstrips.py** (re-create if recycled): `topstrips.py FIRST LAST` renders the top
  running-head strip (x 0.0-1.0, y 0.015-0.072) of every page in the range at zoom ~9, autocontrasts,
  labels each with "PDF N", and stacks them vertically into scratchpad/_strips_FIRST_LAST.png — read
  the whole span's faint folios in one or two Read calls. This is how the B12 offset gap was found.
- **Method:** hand-transcribe from the FULL-PAGE images (300dpi ~1112x1725 is legible); crop columns
  only on dense interleaved pages and for uncertain names/furigana. Dialogue lines and each narration
  run are their own paragraphs; a paragraph is a new line only when the source column is INDENTed at
  its top. Flush the transcription to scratchpad/chNN_build.txt per few pages (edit-in-place to
  complete a page-spanning paragraph), then cp to data/zh and force-add. Track a folio→first-body-
  paragraph map as you go (scratchpad/pagemap_notes.txt) for the pagemap JSON.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 / 五平),
Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木さる / key 木猿; given name 簾 Ren, footnoted
ch11), Kuroami (黒阿弥). Kohagi (小萩) and Imai Sōkyū (今井宗久 → bare "Sōkyū") are the other leads.
Mari Dōgen (摩利洞玄 / 洞玄; birth name 伴藤内 Ban Tōnai; byname 甲賀ノ摩利), Mochizuki Gyōbuzaemon
(望月刑部左衛門 / 刑部左衛門), the Mochizuki house of Kōga (望月家, prose), Maeda Gen'i (前田玄以 /
玄以), Ishida Mitsunari (石田三成 / 三成; office 石田治部少輔 → "Ishida, the Jibu-no-shō"), Hakkansai
(抜関斎 = Rokkaku/Sasaki Yoshikata), Jōtei (承禎入道), Yodo-gimi (淀君), Hideyori (秀頼; infant name
お拾 O-Hiroi). NEW in B12 glossary: 利家 Toshiie (Maeda Toshiie), 吉野 Yoshino, 吉野山 Mount Yoshino.
Terms: Marishiten (摩利支天), Kōga Saburō (甲賀三郎), rappa (乱波). NOT glossaried by design: bare
摩利 "Mari"; 化生 keshō ("keshō"/"a thing of no human birth", footnoted ch11, kept free in prose,
NOT re-noted in ch12); Gen'i's aliases 徳善院/半夢斎; the ch12 single-appearance names (Oda Urakusai,
Furuta Oribe-no-shō, Yamaoka Dōami, Kanze Otojirō, Mikajirō; the Yoshino sub-temples Shikan-in /
Hōzen-in / Kissui-in; the route markers Sanade / Takatori / Takada / Shimoichi / Shimogawara);
ch12 fictional ninja tools rendered descriptively (忍び車 "throwing-wheel", 測隠術 "the Iga art of
measure-and-concealment"). Earlier rows (Nobunaga, Hideyoshi, Ieyasu, Gen'i, Sōkyū, Hattori Hanzō,
Iga/Kōga/Ōmi/Yamashiro/Sakai/Ōsaka/Nara/Gifu, 方広寺 Hōkō-ji, 羅刹谷 Rakshasa Valley, おとぎ峠 Otogi
Pass, the measures) are all in glossary.json — consult it, do not re-derive.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, terse, blunt (わし). Plays a long waiting game for
  the Toyotomi collapse; will NOT leave the capital or betray the work. In ch11 he refuses to flee
  with Kohagi ("a man tires of the woman he loved, never of his work") and leaves the hermitage. In
  ch12 he infiltrates the Yoshino torchlight Noh to see Hideyoshi's face, duels Gohei to a wounding
  draw, breaks a Kōga ambush, and reflects that he commits himself into the keshō of the ninja
  rather than the woman — Kohagi is "the last true ninja." Wry, dry, a professional's cold nerve.
- **Kuroami:** Jūzō's aged genin (past fifty), under five shaku, boy's face; humble archaic
  ござる/申す, superstitious ("a sense like a shrine medium's"), practical, physically timid. Fronts
  as the whetter "Iseya Kahei." In ch12 openly terrified of Gohei; dry ironist ("hardly a lovers'
  quarrel"); returns to save Jūzō, sweeps the caltrops, names Kohagi as the attack's leader and
  Mitsunari's ninja, and urges Jūzō to make an end of Kohagi/Dōgen/Gohei. Ends ch12 with a bleak
  white laugh on the dawn road, a weariness of years in it. Refers to Jūzō as "Master Jūzō".
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter; a Mochizuki-of-Kōga shape-shifter planted on
  Sōkyū by Ishida Mitsunari. In ch11 she asks Jūzō to flee together and grants him a night; in ch12
  the truth is out — she LED the Kōga night-attack at the Saigyō peak, in ninja garb, giving orders,
  meaning to take Jūzō alive as living proof of the plot. Cool courtly poise (ございます/ませぬ;
  self-refers as "Kohagi"); her tender plea to flee (ましょう) is real AND the danger is real.
- **Kisaru (木さる / given name 簾 Ren):** Shimotsuge Jirōzaemon's daughter, a full lead. Spirited,
  blunt, dialect (わし/じゃ; self-reference "Kisaru"). Off-stage in ch12 (last in ch11's Komatsudani
  flashback, jailed by Kohagi).
- **Mari Dōgen (甲賀ノ摩利洞玄):** the aged Kōga rappa; folksy, blunt, wry, self-mocking. Lost his
  left hand to Jūzō in ch10; lodges at Gen'i's Kyoto tenement. Off-stage in ch12 (only named).
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly. Now Gero Shōbei Yasuji, raised to 300
  koku by Gen'i, and now working for Ishida Mitsunari. In ch12 he tails Jūzō from Yoshino and
  duels him — cold, mocking, calculating ("either way there's nothing in it for me"); the Iga art
  of measure-and-concealment (測隠術). Wounded and vanishes rather than fight fair. Superior わし/じゃ.
- **Maeda Gen'i (徳善院/半夢斎):** the shrewd Kyoto magistrate; secretly tilting to the Tokugawa.
  Off-stage in ch12.

## Where the story stands (end of ch12)
Bunroku 3/2/27 (1594): Hideyoshi's Yoshino cherry-blossom progress (with Hidetsugu, Ieyasu,
Toshiie; the Korea war faltering). Jūzō infiltrates the torchlight Noh 吉野天人 as a performer to
study Hideyoshi's face, but the Shikan-in seat is too dark and he aborts. Fleeing, he is tailed by
Gohei — now Mitsunari's man — and fights him to a wounding draw on the mountain, then is swarmed by
a dozen Kōga ninja amid owl-whistles: an ambush LED by Kohagi, who means to take him alive as proof
that Sōkyū's plot is Tokugawa-backed, to push Hideyoshi to destroy the Tokugawa. Jūzō breaks free
(Kuroami returns to help); Kuroami names Kohagi and warns him to make an end of her, Dōgen and Gohei
back in the capital — the day to kill the Taikō is near. They part at Sanade. ch13 水狗 / The Water
Dog (opener on folio 425, offset 0) opens with Kuroami, back from Yoshino to Kyoto, abruptly closing
the whetstone shop behind Hōkō-ji and holing up in the Rakshasa Valley ruin to re-gather the
scattered rappa.

## Next batch
B13 = ch13 水狗 / The Water Dog, printed folios 425-455 (opener PDF 425 = folio 425, offset 0 —
printed == PDF, CONFIRMED at end of B12). ch13 body begins AFTER the 水狗 title on folio 425
(吉野から京へもどった黒阿弥は…); ch12's tail (5 paras before the title, source lines 209-213) is done.
READ folios off the running heads to confirm printed == PDF holds. Then B14 = ch14 修羅 / Carnage,
folios 456-507.

## Open traps / environment
- **Offset is 0 at the start of B13 (folio 425 = PDF 425) and should stay printed == PDF to the end.**
  The +2 span ENDED via the 1-leaf gap that dropped printed folios 404-405. READ folios off the
  running heads each batch (very faint — topstrips.py + autocontrast); skip any duplicate leaf;
  re-map from any SKIPPED folio; build data/pagemap for the span.
- **The folios 404-405 scan gap is PERMANENT and already handled in ch12** (body para 37 truncated,
  38 editorial marker + footnote, 39 resumes). Do NOT try to "recover" or bridge it.
- A chapter's tail can spill onto the next opener folio (ch03/04/06/07/08/09/10/11/12 all did) —
  render the next opener and verify; make sure the next batch does not re-translate the spillover.
  ch12's tail (5 paras) is on folio 425 before the 水狗 title; ch13 body starts after the title.
- Furigana leakage and dropped clauses cluster on the DENSE opener and the TAIL. Re-read both
  against the scan and run the compound-coverage grep before shipping.
- **assemble.py OVERWRITES data/zh/chNN.txt AND welds paragraphs** — hand-transcribe from the
  images; use a top-strip crop to read indents (indent = new paragraph; non-indented column-top
  after a sentence-end = same paragraph continuing).
- qc_entities / check_content want the rendered name once per paragraph the character appears in
  — do a name-survival pass over pronoun-only paragraphs (B10 fixed 20, B11 fixed 8, B12 fixed 6).
  Match the glossary `en` form exactly. check_content is authoritative; qc_entities over-flags
  place-keys inside common words (declare those).
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py (notes/figures, from a
  JSON file with a top-level "notes"/"figures" key) or the Write/Edit tool or a python json
  load/dump (glossary), then re-read to verify. (Plain-text data/noise.txt via a heredoc is fine —
  it's not JSON — but re-read to confirm.)
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words; place ⊂ compound).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution); if you run
  a post-hoc pass, watch clause-final over-contraction ("you're."/"there's." are ungrammatical).
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled. Pre-existing checker-regression FAIL (hook stands
  down on template stub) is unrelated to this book; leave it.
