# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B14

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B14 = ch14 「修羅」 (Carnage), printed folios 456-507, end to end per the CLAUDE.md pipeline. OFFSET IS 0: printed == PDF (folio 456 = PDF 456, CONFIRMED at the end of B13 by reading the running head of every page across PDF 425-457; no duplicate leaf, no gap). Do NOT assume — READ the folio off the running head of EVERY rendered page across this span to confirm printed == PDF holds, and watch for any further duplicate leaf or gap. The running heads are VERY faint: use scratchpad/topstrips.py FIRST LAST to stack the top strips of a page range into one image (top strip 0.0 0.02 1.0 0.075 at zoom ~9-10, autocontrast). book.json: ch15 opener 五三ノ桐 (The Paulownia Crest) at printed 508 == PDF 508. Build data/pagemap/ch14.json for the span (ch12.json / ch13.json are the format model: entries {printed, pdf, body_paragraph} where body_paragraph is the 0-based index into data/zh/ch14.txt body paragraphs, title excluded). Confirm the ch15 opener 五三ノ桐 and flag whether ch14's tail spills onto it.

ch14 opens MID-PAGE on folio 456 (the 修羅 title sits below ch13's 2-sentence tail). ch14 body begins AFTER the 修羅 title with それから数日たった午後、京都奉行前田玄以の屋敷へ、玄関を通らず裏門からすっと入ってきた深編笠の男がある。まだ陽も高い。… (a deep-hatted man slips in at the back gate of the Kyoto magistrate Maeda Gen'i's residence). ch13's tail SPILLS onto folio 456 BEFORE the 修羅 title (source line 246 = body paragraph 244 of data/zh/ch13.txt: 重蔵はうしろもみず、浅瀬を渡って山に入った。頂きにのぼればそのまま、むこう斜面は京の街につづいているはずであった。); that is DONE in ch13 — do NOT re-translate it. BEFORE translating, read the final two pages of ch13's English (the tail of out/ch13_reading.md) so the voice carries.

ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch14_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write (Jūzō blunt わし; Gero Shōbei/Gohei cold-clerkly; Gen'i the shrewd magistrate; low-city voices) — do NOT leave "It is/I do not/you are" everywhere; keep the grave uncontracted line only for deliberately-formal registers (obsequious まする to a lord, quoted documents/scripture, a courtier's or Hideyoshi's formal speech, a priest's invocation). ch05/ch08 both needed a whole contraction pass afterward; ch06 ran formal-by-design at 0.74x and passed, ch09 1.21x, ch10 2.31x, ch11 1.62x, ch12 1.86x, ch13 1.34x — a court/exposition chapter may sit below 1.0x, but 0.0x is a draft error, not "formal by design".

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled). The pre-existing checker-regression FAIL "hook stands down on template stub" is unrelated; leave it.
2. OCR: render.py 456 509 --dpi 300 (folio 456 = PDF 456; render a few pages past the expected ch15 opener 508 to catch the ch15 opener and any drift); then ocr_crop.py 456 509 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 456 509. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls). CHECK each rendered page's running-head folio: expected folio == PDF. A folio that repeats the previous folio is a double-feed (skip it); a SKIPPED folio is a gap (re-map from there).
3. find_figures.py 456 509 AND eyeball every page for line art (ch01-ch13 were all text-only; if ch14 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by READING the rendered page images directly (data/png/p0NNNN.png — files are named p0456.png etc., 4-digit) and hand-build data/zh/ch14.txt as a corrected, paragraph-aligned transcription (the parity surface). scratchpad/crop.py 6x-renders a page-fraction rectangle (crop.py PAGE x0 y0 x1 y1 [zoom]; PAGE 1-based; fractions of the full page; reads furigana AND faint running-head folios cleanly). scratchpad/topstrips.py FIRST LAST stacks running-head strips of a page range into one image for fast folio reading. Re-create crop.py / topstrips.py if the container recycled (bodies in "Tooling in place" below). NOTE: the full-page images at 300dpi (~1112x1725) are LEGIBLE enough to transcribe directly, cropping columns only for interleaved dense pages and uncertain names/furigana (the B12/B13 method — far faster than half-page crops). Interleaved narration/dialogue mis-orders from the full page — crop the columns and read right-to-left, top-to-bottom literally (READING ORDER IS STRICT RTL COLUMN-BY-COLUMN; a dialogue attribution 「…」と… sits in its own column); treat each 「…」 line and each narration run as its own paragraph. Force-add data/zh/ch14.txt (data/zh/ is gitignored). Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch15 opener folio and check whether ch14's tail spills onto it, and make sure B15 does not re-translate any spillover. COVERAGE cross-check after transcribing: extract every 3+-kanji compound from the raw data/txt OCR (over the ch14 PDF span, excluding any duplicate leaves) and confirm each appears in your HAND data/zh/ch14.txt — garbles are expected; a clean meaningful compound that is absent is a real drop to fix (python one-liner over data/txt with a Counter of [一-鿿]{3,}).
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Ieyasu/Tokugawa/Kyoto/Yoshino). Principal cast and majors are decided in glossary.json; reuse unchanged and record in PROGRESS which rows you reused. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans. Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False indent=2, or the Edit tool — the B04-B13 method, NOT apparatus_merge which flattens the glossary). AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter. Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch14_reading.md, settle the English title at translation ('## Carnage' — 修羅 is the Buddhist "shura/asura," a realm/state of ceaseless bloody strife; rendered "Carnage" in book.json. Footnote at first body appearance if the sense is not obvious). Add a ch14 entry to data/checks.json (docs + sources). make_bilingual.py ch14 (parity FIRST). Then run: verify_unit.py ch14; check_structure.py --pairs data/zh/ch14.txt out/ch14_reading.md; check_align.py ch14; qc_entities.py out/ch14_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch14_reading.md. (qc/content want the rendered name once per paragraph the character appears in — do a name-survival pass over any pronoun-only paragraph, as in B10/B11/B12/B13; check_content is authoritative, qc_entities over-flags place-keys inside common words.)
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch13 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku/Genki dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office (治部少輔)/太閤(Taikō)/内府(Naifu)/右府(Udaifu) titles, Sakai the free-city, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu/Hideyori(お拾/O-Hiroi), Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours and 半刻/小半刻, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures (shaku/chō/koku/ri/ken/kin/tsubo/jō/kan/kanmon), rappa/shinobi/jōnin/genin, jizamurai/gōshi, くノ一/kunoichi, 忍び文字/shinobi-moji, Marishiten, Yodo-gimi(淀君)/Odani, Rokkaku/Sasaki Yoshikata (Hakkansai/Jōtei) & Kannon-ji 1568, the 1487 Magari campaign, the fifty-three houses of Kōga, Kōga Saburō, the Odawara campaign, Nagoya castle in Hizen, Hattori Hanzō, the Jurakudai, the go-bugyō, the Iga-goe, Miyamoto Musashi & the Yoshioka, Kashima/Katori & Bokuden, 陽忍/陰忍 open-way/shadow-way, the Bon send-off, shōchū, the Kyoto-to-Kōga escape route, the Buddhist precepts / Mahāsāṃghika Vinaya / Buddhabhadra, Empress Jitō's no-kill decree, 化生/keshō (shape-shifter), the Mochizuki house of Kōga, Ren (Kisaru's given name), Yoshino & its cherry-blossom cult, Maeda Toshiie, the 1595 Hidetsugu purge, the Zaō Hall/Kimpusen-ji, the Saigyō hermitage, Noh/takigi-nō/the Kanze school, the Noh play 吉野天人 & the tennin, the owl-whistle (梟笛), the sasumata, AND the B13 first-appearances: Mimi of Nabari (the name = "ear"), the kozuka, the kuji/Samaya-mudra/mantra ninja counter-spell, Fushimi Castle, the Genki era. Note only ch14's NEW first-appearances (likely candidates: whatever the 修羅/shura realm means if not obvious, any new offices/places/persons introduced at Gen'i's residence, new tools/argot). Anchor notes to BODY phrases (verbatim substrings), not heading-only text. Add via apparatus_merge.py (batch JSON file with a top-level "notes" key, numeric char refs OR literal chars in bodies — NEVER a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, the renderings reused/added), INCLUDING the confirmed folio-to-PDF map for this span (should be printed == PDF throughout — confirm), and the data/pagemap/ch14.json you built.

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B15 kickoff (ch15 「五三ノ桐」 The Paulownia Crest, printed folios 508-565; offset should still be 0 — printed == PDF — but READ folios to confirm) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure in book.json; metadata set; skeleton EPUB built; page
  furniture measured (crop L0.035 R0.965 T0.075 B0.955; model jpn_vert psm5).
- **Offset history (READ folios, do not compute):** 0 for folios 7-325; **+2 from folio 326
  (PDF 328) through folio 403 (PDF 405)**; a **1-leaf scan gap dropped printed folios 404-405**
  (MISSING from the scan), re-mapping the offset back to **0 from folio 406 (PDF 406) onward**.
  **printed == PDF CONFIRMED unbroken through folio 457 (end of B13's rendered span).** It should
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
- **B13 = ch13 水狗 / The Water Dog (425-455, tail on 456): COMPLETE.** 245 body paragraphs, 6 new
  notes (book total 103). All checks green (parity 245|245, numbers 0/245, check_content clean, qc
  1 declared false positive, register 1.34x within tolerance, align median 9.47, qa_epub PASS,
  epubcheck 0/0/0/0). Built data/pagemap/ch13.json (32 entries, printed==PDF 425-456). NO figures.
  Added glossary row 名張ノ耳 → Mimi of Nabari; noise +1 (二十代). Kuroami is KILLED this chapter.
  ch13's tail (body para 244) spills onto folio 456 before the 修羅 title — B14 must not re-translate it.

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
- `data/checks.json`: the {docs, sources} config. ch01-ch13 in.
- `data/noise.txt`: check_numbers noise. B13 added 二十代 ("in their twenties"). Extend per its
  header, longest literal first, one comment line each; never noise a real quantity you dropped.
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens glossary
  rows to the ROOT, so since B04 add glossary rows DIRECTLY into the sections (Edit tool, or json
  load/dump ensure_ascii=False indent=2). Notes and figures merge fine via apparatus_merge (batch
  file needs a top-level "notes"/"figures" key — {"notes": {"chNN": [...]}}).
- **Note anchors:** must be verbatim substrings of the BODY prose (NOT the heading). Note bodies:
  literal Unicode is fine (em dash, en dash, macrons, curly quotes) OR numeric character
  references; only NAMED HTML entities (&nbsp; &mdash;) are rejected. Author the notes batch as a
  JSON FILE (Write tool) and run apparatus_merge.py on it — never a heredoc.
- **Substring trap for glossary keys:** do NOT add a bare-name row whose romanization is a
  substring of a fuller row in use. SAFE full+bare pairs (重蔵/葛籠重蔵, 摩利洞玄/洞玄, 名張/名張ノ耳,
  淀君, 秀頼, 五平/風間五平) are fine. When a place key collides as a substring of another word,
  prefer the longer key or DECLARE the false positive (B13 declared 甲斐/Kai inside 年甲斐).
- **scratchpad crop.py** (re-create if the container recycled): renders a fractional rectangle of a
  source.pdf page at high zoom so furigana AND the faint running-head folio are legible. Signature
  `crop.py PAGE x0 y0 x1 y1 [zoom]` (PAGE 1-based; fractions of the full page; default zoom 6).
  Uses `import fitz` (pymupdf), opens /home/user/winston/source.pdf, clips to the rect, autocontrasts
  (PIL ImageOps.autocontrast cutoff=2 — do NOT hard-threshold), saves scratchpad/_crop.png.
- **scratchpad topstrips.py** (re-create if recycled): `topstrips.py FIRST LAST` renders the top
  running-head strip (x 0.0-1.0, y 0.015-0.072) of every page in the range at zoom ~9, autocontrasts,
  labels each with "PDF N", and stacks them vertically into scratchpad/_strips_FIRST_LAST.png — read
  the whole span's faint folios in one or two Read calls.
- **Method:** hand-transcribe from the FULL-PAGE images (300dpi ~1112x1725 is legible); crop columns
  only on dense interleaved pages and for uncertain names/furigana. READING ORDER IS STRICT RTL
  COLUMN-BY-COLUMN (a dialogue attribution "…と…" sits in its own column between quotes). Dialogue
  lines and each narration run are their own paragraphs. Flush the transcription to
  scratchpad/chNN_build.txt per few pages (edit-in-place to complete a page-spanning paragraph),
  then cp to data/zh and force-add. Track a folio→first-body-paragraph map as you go for the pagemap.
- **A set-off chant/cipher is ONE parity line marked {p}** (verse), between the narration lines that
  introduce and resume it (ch06 cipher, ch13 mantra). check_structure strips the marker before parity.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 / 五平),
Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木さる / key 木猿; given name 簾 Ren), Kuroami
(黒阿弥, KILLED in ch13). Kohagi (小萩) and Imai Sōkyū (今井宗久 → bare "Sōkyū") the other leads.
Mari Dōgen (摩利洞玄 / 洞玄; birth name 伴藤内 Ban Tōnai; byname 甲賀ノ摩利), Mochizuki Gyōbuzaemon
(望月刑部左衛門 / 刑部左衛門), Maeda Gen'i (前田玄以 / 玄以; aliases 徳善院/半夢斎), Ishida Mitsunari
(石田三成 / 三成; office 石田治部少輔 → "Ishida, the Jibu-no-shō"), Hakkansai (抜関斎 = Rokkaku/Sasaki
Yoshikata), Jōtei (承禎入道), Yodo-gimi (淀君), Hideyori (秀頼; infant name お拾 O-Hiroi), Maeda
Toshiie (利家). NEW in B13 glossary: 名張ノ耳 → Mimi of Nabari (people). Places: 阿弥陀ヶ峰 →
**Amidagamine** (glossary form; do NOT drift to "Amida-ga-mine"), 吉野 Yoshino, 吉野山 Mount Yoshino,
方広寺 Hōkō-ji, 羅刹谷 Rakshasa Valley, 御斎峠 Otogi Pass, and the province/city rows (Iga/Kōga/Ōmi/
Yamashiro/Sakai/Ōsaka/Nara/Gifu). Terms: Marishiten (摩利支天), Kōga Saburō (甲賀三郎), rappa (乱波).
NOT glossaried by design: bare 摩利 "Mari"; 化生 keshō; the ch12/ch13 single-chapter names (Oda
Urakusai, Furuta Oribe-no-shō, Kanze Otojirō; the Yoshino sub-temples; the route markers; ch13's
柘植義宗 Tsuge Yoshimune, the Iga roll-call 大呂源左衛門/上野ノ鹿次/平川ノたひょうえ/上塚道願 Uezuka
Dōgan/上柘植ノ佐吉, and the places 珠宝院 Shuhō-in / 射庭川 Iba-gawa / 山科 Yamashina / 渋谷越 the
Shibutani pass / 浮世橋 Ukiyo-bashi / 東山 Higashiyama / 伏見 Fushimi (footnoted) / 遠州 Enshū).
Consult glossary.json, do not re-derive.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, terse, blunt (わし). Plays a long waiting game for
  the Toyotomi collapse. In ch13 (close only) he finds Kuroami's body at the Iba-gawa ford and
  resolves on revenge — whoever did it, "no matter"; pays a farmer for the crows' requiem
  ("Say I'm one of the crows' own kin") and crosses into the mountains for the capital. Wry, cold nerve.
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly. Now Gero Shōbei Yasuji, raised to 300
  koku by Gen'i, working for Ishida Mitsunari; the Iga art of measure-and-concealment (測隠術).
  Superior わし/じゃ; mocking, calculating. (Enters ch14 at Gen'i's residence — verify who the
  back-gate man is.)
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter; a Mochizuki-of-Kōga shape-shifter planted on
  Sōkyū by Ishida Mitsunari. Cool courtly poise (ございます/ませぬ; self-refers "Kohagi"). She LED the
  Kōga night-attack in ch12. May command the Kōga band that killed Kuroami.
- **Mari Dōgen (甲賀ノ摩利洞玄):** the aged Kōga rappa master; folksy, blunt, wry, cruel, self-mocking.
  Lost his left hand to Jūzō in ch10. In ch13 he runs Kuroami down, annihilates the Iga at
  Amidagamine, kicks Kuroami's corpse, and leaves the Iga dead for the crows. Lodges at Gen'i's
  Kyoto tenement.
- **Maeda Gen'i (前田玄以 / 徳善院/半夢斎):** the shrewd Kyoto magistrate (京都奉行); secretly tilting
  to the Tokugawa. His residence opens ch14.
- **Kuroami (dead):** was Jūzō's aged genin, humble-archaic ござる/申す, a professional's creed
  ("a ninja never betrays the man who hired him"). Died in ch13 by his own hand, vowing Jūzō's revenge.
- **Kisaru (木さる / given name 簾 Ren):** Shimotsuge's daughter, spirited, blunt, dialect (わし/じゃ).
  Off-stage since ch11 (jailed by Kohagi).

## Where the story stands (end of ch13)
Bunroku 3 (1594), after the Yoshino progress. Back in the capital, Kuroami re-gathers his scattered
rappa at the Rakshasa Valley ruin and sets them to watch Hideyoshi (now building Fushimi Castle,
lodging at the Jurakudai). But Nabari no Mimi, a broken Iga survivor Kuroami turned away, sells the
Iga hideout to Mari Dōgen of Kōga. Dōgen runs Kuroami down; at Amidagamine Kuroami's dozen aged Iga
men (13 with him) face 50 young Kōga. In a running fight down to the Iba-gawa riverbed the Iga die
as death-troops, Uezuka Dōgan last; Kuroami, offered his life to betray the plot, refuses and cuts
his own throat, vowing Jūzō will avenge him. At dawn Jūzō, coming from Otogi Pass by the Shibutani
pass, finds the black-clad dead in the shallows, knows Kuroami, and swears to make the Kōga bleed
before he kills the Taikō. ch14 修羅 / Carnage (opener mid-folio 456, offset 0) opens some days
later with a deep-hatted man slipping in at the back gate of the magistrate Maeda Gen'i's residence.

## Next batch
B14 = ch14 修羅 / Carnage, printed folios 456-507 (opener mid-folio 456 = PDF 456, offset 0 —
printed == PDF, CONFIRMED through 457 at end of B13). ch14 body begins AFTER the 修羅 title
(それから数日たった午後、京都奉行前田玄以の屋敷へ…); ch13's tail (body para 244) sits on folio 456
before the title and is done. READ folios off the running heads to confirm printed == PDF holds.
Then B15 = ch15 五三ノ桐 / The Paulownia Crest, folios 508-565.

## Open traps / environment
- **Offset is 0 (folio == PDF) and should stay so to the end.** READ folios off the running heads
  each batch (very faint — topstrips.py + autocontrast); skip any duplicate leaf; re-map from any
  SKIPPED folio; build data/pagemap for the span.
- **The folios 404-405 scan gap is PERMANENT and already handled in ch12.** Do NOT try to bridge it.
- A chapter's tail can spill onto the next opener folio (ch03/04/06/07/08/09/10/11/12/13 all did) —
  render the next opener and verify; make sure the next batch does not re-translate the spillover.
  ch13's tail (body para 244) is on folio 456 before the 修羅 title; ch14 body starts after the title.
- Furigana leakage and dropped clauses cluster on the DENSE opener and the TAIL. Re-read both
  against the scan and run the compound-coverage grep before shipping. (B13 caught a merged
  dialogue pair + a dropped 「心得申した」 reply this way — parity is the tripwire.)
- **assemble.py OVERWRITES data/zh/chNN.txt AND welds paragraphs** — hand-transcribe from images.
- qc_entities / check_content want the rendered name once per paragraph the character appears in
  — do a name-survival pass over pronoun-only paragraphs (B10 fixed 20, B11 fixed 8, B12 fixed 6,
  B13 fixed 8 + surfaced "rappa"). Match the glossary `en` form exactly. check_content is
  authoritative; qc_entities over-flags place-keys inside common words (declare those).
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py (notes/figures) or the
  Write/Edit tool or a python json load/dump (glossary), then re-read to verify. (Plain-text
  data/noise.txt via a heredoc is fine — it's not JSON — but re-read to confirm.)
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words; place ⊂ compound).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution); if you run
  a post-hoc pass, watch clause-final over-contraction ("you're."/"there's." are ungrammatical).
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled. Pre-existing checker-regression FAIL (hook stands
  down on template stub) is unrelated to this book; leave it.
