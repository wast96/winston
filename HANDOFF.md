# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B10

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B10 = ch10 「奇妙な事故」 (A Strange Accident), printed folios 338-372, end to end per the CLAUDE.md pipeline. OFFSET IS +2 ACROSS THIS WHOLE SPAN: folio = PDF render page minus 2 (PDF 340 = folio 338, the ch10 opener; PDF 374 = folio 372; ch11 開く at PDF 375 = folio 373). This is because a scanner DOUBLE-FEED duplicated folios 324-325 at PDF 326-327 (see the B09 note below and PROGRESS "CRITICAL"), so from PDF 328 on the folio runs two behind the PDF page. READ the folio off the running head of every opener and spot pages to CONFIRM, and BUILD data/pagemap/ch10.json for this span (B11-B13 need the mapping; ch08.json is the format model). Watch for another anomaly near folios 397-425 (a possible 1-leaf scan gap; that is B12-B13, but confirm as you go).

ch10 body begins on folio 338 AFTER the 奇妙な事故 title with 錯綜した関係にある京の忍者のあいだに、ひとつの真空地帯ができた。 . ch09's tail SPILLS onto folio 338 BEFORE that title (five paragraphs ending 「わるい虫じゃ」 / 黒阿弥は苦虫を嚙みつぶしたような顔を作った。); those are DONE in ch09 — do NOT re-translate them. BEFORE translating, read the final two pages of ch09's English (the tail of out/ch09_reading.md) so the voice carries.

ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch10_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write (Jūzō blunt わし; Kuroami humble ござる; Mari Dōgen folksy わし/じゃ/のう; low-city voices) — do NOT leave "It is/I do not/you are" everywhere; keep the grave uncontracted line only for deliberately-formal registers (Kuroami's ござる, obsequious まする to a lord, quoted documents/scripture). ch05/ch08 both needed a whole contraction pass afterward; ch06 ran formal-by-design at 0.74x and passed, ch09 (dialogue-heavy) ran at 1.21x — a court chapter may sit below 1.0x, but 0.0x is a draft error, not "formal by design".

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled). The pre-existing checker-regression FAIL "hook stands down on template stub" is unrelated; leave it.
2. OCR: render.py 340 376 --dpi 300 (folios 338-373 sit at PDF 340-375; render 376 too for the tail check into ch11); then ocr_crop.py 340 375 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 340 375. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls). CHECK each rendered page's running-head folio against the expected folio = PDF - 2; if any PDF page repeats the previous folio, it is another double-feed — skip it and re-map.
3. find_figures.py 340 375 AND eyeball every page for line art (ch01-ch09 were all text-only; if ch10 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by READING the rendered page images directly (data/png/p0NNNN.png) and hand-build data/zh/ch10.txt as a corrected, paragraph-aligned transcription (the parity surface); use a top-strip crop of each page (scratchpad crop.py) to read the paragraph INDENTS, since assemble mis-groups. Force-add data/zh/ch10.txt (data/zh/ is gitignored). Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch11 opener folio (PDF 375) and check whether ch10's tail spills onto it, and make sure B11 does not re-translate any spillover. COVERAGE cross-check after transcribing: extract every 3+-kanji compound from the raw data/txt OCR (over the ch10 PDF span, excluding any duplicate leaves) and confirm each appears in your HAND data/zh/ch10.txt — garbles are expected; a clean meaningful compound that is absent is a real drop to fix.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). Principal cast and majors are decided in glossary.json; reuse unchanged and record in PROGRESS which rows you reused. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans; the scratchpad crop.py 6x-renders a page-fraction rectangle (PAGE x0 y0 x1 y1 fractions; PAGE 1-based) and reads furigana cleanly — re-create it if the container recycled. Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False, or the Edit tool — the B04-B09 method, NOT apparatus_merge which flattens the glossary). AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter. Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch10_reading.md, '## A Strange Accident' as the h1 (settle the English title at translation). Add a ch10 entry to data/checks.json (docs + sources). make_bilingual.py ch10 (parity FIRST). Then run: verify_unit.py ch10; check_structure.py --pairs data/zh/ch10.txt out/ch10_reading.md; check_align.py ch10; qc_entities.py out/ch10_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch10_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch09 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office titles, Sakai the free-city, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu, Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours and 半刻/小半刻, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures (shaku/chō/koku/ri/ken/kin/tsubo/jō/kan/kanmon), rappa/shinobi/jōnin/genin, jizamurai/gōshi, the B04-B08 first-appearances (放下僧, Nyoigatake/Daimonji, Gion, Katō Kiyomasa, Maeda Gen'i & the Kyoto magistracy, 羅刹/rakshasa, Sennyū-ji, Hattori Hanzō, the Jurakudai, the kōshin monkey, くノ一/kunoichi, 忍び文字/shinobi-moji, Kashima/Katori & Bokuden, Miyamoto Musashi & the Yoshioka, Kisshōten, the Chōsokabe, 蓬莱/Hōrai, the 上り音曲・下り兵法 proverb, Makuzugahara, Ishida Mitsunari, Yamazaki 1582, the go-bugyō, Yanagimachi, the Iga-goe), AND the B09 first-appearances: Marishiten/Mārīcī, the Udaifu (右府=Nobunaga) and Naifu (内府=Ieyasu) court titles, Yodo-dono (小谷殿の娘) & Odani, Rokkaku/Sasaki Yoshikata (抜関斎/承禎/Hakkansai/Jōtei) & Kannon-ji castle 1568, the 1487 Magari campaign & shogun Yoshihisa, the fifty-three houses of Kōga, Kōga Saburō, Oiro Tayuya/Prince Shōtoku's spy, the Odawara campaign (1590), Nagoya castle in Hizen. Note only ch10's NEW first-appearances. Anchor notes to BODY phrases (verbatim substrings), not heading-only text. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added), INCLUDING the confirmed folio-to-PDF map for this span and the data/pagemap/ch10.json you built.

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B11 kickoff (ch11 「伊賀ノ山」 The Hills of Iga, printed folios 373-396; still in the +2 span, PDF 375-398 — read folios and extend data/pagemap) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (crop L0.035 R0.965 T0.075 B0.955; model
  jpn_vert psm5). Offset: 0 for folios 7-325; +2 from folio 326 (see the double-feed
  note under Tooling); an apparent 1-leaf gap near 397-425 still to confirm (B12-B13).
- **B01 = ch01 おとぎ峠 / Otogi Pass (folios 7-63): COMPLETE, approved at the voice
  gate.** ch01 is the FROZEN register reference. 523 paragraphs, 17 notes.
- **B02 = ch02 濡れ大仏 / The Rain-Soaked Buddha (64-89): COMPLETE.** 276 paras, 6 notes.
- **B03 = ch03 白い法印 / The White Hōin (90-123): COMPLETE.** 385 paras, 16 notes.
- **B04 = ch04 木さると五平 / Kisaru and Gohei (124-148): COMPLETE.** 286 paras, 5 notes.
- **B05 = ch05 羅刹谷 / Rakshasa Valley (149-166): COMPLETE.** 152 paras, 6 notes.
- **B06 = ch06 忍び文字 / The Ninja Cipher (167-206): COMPLETE.** 312 paras, 5 notes.
- **B07 = ch07 聚楽 / Juraku (207-236): COMPLETE.** 280 paras, 5 notes.
- **B08 = ch08 京の盗賊 / The Thief of the Capital (237-301, tail on 302): COMPLETE.**
  580 paras, 6 notes.
- **B09 = ch09 甲賀ノ摩利 / Mari of Kōga (302-337, tail on 338): COMPLETE.** 324 paragraphs,
  11 new notes (book total 77). All checks green (numbers 0/324, parity 324|324,
  qc/content/apparatus clean, register 1.21x ref, qa_epub PASS, epubcheck 0/0/0/0).
  Gen'i hires the old Kōga rappa Mari Dōgen to watch the "capital thief"; Kohagi is
  revealed as Rokkaku Yoshikata's daughter, Kōga-trained, planted on Sōkyū by Mitsunari;
  Dōgen and Jūzō recognise each other as the rival leaders; Hideyoshi leaves for the
  Korean war and the shadow-war goes quiet. A SCANNER DOUBLE-FEED was found and mapped
  (PDF 326/327 duplicate folios 324/325); no content lost.

## ch01 corrections made earlier (do NOT undo)
1. ch01's dropped final two paragraphs restored in B02; ch01 parity is 523 | 523.
2. ch01's Great Buddha note corrected in B02 to the NARA Tōdai-ji Vairocana (roofless
   since Matsunaga burned it 1567), not Hideyoshi's Hōkō-ji. In B03 Hideyoshi's OWN
   Great Buddha (方広寺大仏, Kyoto Hōkō-ji) appears and is footnoted as DISTINCT; ch05/ch08
   京の大仏/方広寺 is Hideyoshi's Hōkō-ji again (cross-ref).

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana in the despace class; `--no-furniture-strip` skips the Chinese
  strip_folio/strip_runfoot. Furniture here is top-only, cropped.
- `ocr_dual.py`: Japanese second read (jpn_vert psm5 on grayscale + Otsu variant).
- `check_content.py` / `qc_entities.py`: skip non-dict glossary sections; subsume a
  shorter glossary key covered by a longer matched key at the same span. qc_entities is
  case-insensitive and accepts the first OR last word of a multi-word `en`; check_content
  needs the EXACT `en` present (substring) and only uses `en` that are Capitalised,
  slash-free and >= 4 chars (so bare "Dōgen" satisfies qc where 摩利洞玄 appears, but
  check_content wants "Mari Dōgen" there — render the full form in 摩利洞玄 paragraphs).
- `data/checks.json`: the {docs, sources} config. ch01-ch09 in.
- `data/noise.txt`: check_numbers noise. B09 added the roster/name numerals (四郎兵衛,
  十郎, 八郎, 七郎, 三郎, 五郎, 四方, 八田, 三雲, 三河, 六角, 三満多) and 十四、五. Extend per its
  header, longest literal first, one comment line each; never noise a real quantity you
  dropped (fix the English to carry it).
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens
  glossary rows to the ROOT, so since B04 add glossary rows DIRECTLY into the sections
  (Edit tool, or json load/dump ensure_ascii=False indent=2). Notes and figures merge
  fine via apparatus_merge as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder refuses a
  heading-only anchor. Note bodies: literal Unicode is fine (em dash, macrons, curly
  quotes); only NAMED HTML entities are rejected (use numeric refs or the literal char).
- **Substring trap for glossary keys:** do NOT add a bare-name row whose romanization is a
  substring of a fuller row in use (宗久⊂Imai Sōkyū). SAFE full+bare pairs that mirror the
  重蔵/葛籠重蔵 precedent are fine and used: 摩利洞玄/洞玄, 望月刑部左衛門/刑部左衛門. When a
  place key collides as a substring of another word (山城 Yamashiro inside 釜山城 Pusan
  castle), add the longer key (釜山城) so it subsumes the shorter at that span.
- **SCANNER DOUBLE-FEED (found in B09):** PDF 326 and 327 are re-scans of folios 324 and
  325 (running heads read 324, 325; OCR identical). The real run resumes at PDF 328 =
  folio 326. So **folio = PDF - 2 from PDF 328 onward** through this middle span
  (PDF 340 = folio 338 = ch10, PDF 375 = folio 373 = ch11). CHECK the folio on every
  rendered page and skip any further duplicate leaf. Build data/pagemap for the span with
  this map. book.json's source_note still says the drift starts ~338; the true start is
  folio 326 (PDF 328).
- **Method:** hand-transcribe from the page images; use a top-strip crop (scratchpad
  crop.py, e.g. PAGE 0.05 0.07 0.95 0.20) to read paragraph INDENTS, since assemble.py
  mis-groups AND overwrites data/zh/chNN.txt. Dialogue lines are their own paragraphs;
  narration that ends in 、 and leads into a quote is kept as its own line (the quote is a
  separate line). Interleaved narration/dialogue on dense pages mis-orders from the full
  page — crop the columns and read right-to-left, top-to-bottom literally.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 /
五平), Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木さる / 木猿), Kuroami (黒阿弥).
Kohagi (小萩) and Imai Sōkyū (今井宗久) are the other leads. B09 people added: Mari Dōgen
(摩利洞玄 / 洞玄; birth name 伴藤内 Ban Tōnai; byname 甲賀ノ摩利 "Mari of Kōga"), Mochizuki
Gyōbuzaemon (望月刑部左衛門 / 刑部左衛門; given name 重久 Shigehisa), Hakkansai (抜関斎 =
Rokkaku/Sasaki Yoshikata), Jōtei (承禎入道, Yoshikata's later name). B09 terms: Marishiten
(摩利支天), Kōga Saburō (甲賀三郎), Kōga letter (甲賀文, fictional). B09 places: Pusan castle
(釜山城). NOT glossaried by design: bare 摩利 "Mari" (substring of 摩利洞玄 and 摩利支天; rendered
in prose), Gen'i's aliases 徳善院 Tokuzen'in / 半夢斎 Hanmusai (prose only). Earlier rows
(Nobunaga, Hideyoshi, Ieyasu, Gen'i, Sōkyū, Hattori Hanzō, Ishida Mitsunari, Iga/Kōga/Ōmi/
Sakai/Ōsaka/Nara/Gifu, 方広寺 Hōkō-ji, 伊勢屋嘉兵衛 Iseya Kahei, おとぎ峠 Otogi Pass, the
measures, etc.) are all in glossary.json.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, terse, blunt (わし). The grudge has cooled
  into the one "tremendous ninja's stage" of killing Hideyoshi; he plays a long waiting
  game. In ch09 he learns Mari Dōgen of Kōga is set against him, resolves to cut him "when
  an opening comes," but "since I idled ten years at Otogi Pass I've come to pity anything
  that lives and moves — the ferocity's left my heart." Waits for the Toyotomi collapse;
  will NOT leave the capital (won't cut the thread to it). Wry with Kuroami.
- **Kuroami:** Jūzō's aged genin (past fifty), under five shaku, boy's face; humble archaic
  ござる/申す, chides Jūzō like a father, superstitious and openly fearful (teeth chatter),
  practical. Fronts as the whetter "Iseya Kahei." Trembles at the Kōga threat; proposes
  retreating to Otogi Pass. Addresses/refers to Jūzō as "Master Jūzō".
- **Mari Dōgen (甲賀ノ摩利洞玄):** the aged Kōga rappa (past fifty but robust, coarse-haired,
  eats dried boar's gall). Folksy, blunt, wry, self-mocking; わし/じゃ/のう/おぬし; the "owl"
  philosophy ("a ninja lives in the hollows of men, alone"). Once carried Gen'i and the
  infant Sanbōshi out of the Honnō-ji trap; holds Gen'i to a fifty-kanmon-a-year debt.
  Calls Gen'i "Tokuzen'in-dono," teases him ("too good-hearted for an inquisitor"). Sizes
  Jūzō up as a "stripling" but privately wary ("a trial of skill between Kōga and Iga").
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly. Now Gero Shōbei Yasuji, raised to
  300 koku by Gen'i, who has unmasked him and set him to hunt the thief. Superior わし/じゃ to
  inferiors, obsequious ます/です to a master. (Off-stage in ch09; will return.)
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter; REVEALED in ch09 as the natural daughter
  of Rokkaku Yoshikata (Hakkansai/Jōtei), left with Mochizuki Gyōbuzaemon in Kōga, taught
  the full Kōga arts (holds the Kōga license), then placed on Sōkyū by Ishida Mitsunari.
  Cool unbreakable poise, a smoky half-smile. Dōgen has left her a Kōga calling-card.
- **Maeda Gen'i (徳善院/半夢斎):** the shrewd Kyoto magistrate, a former Owari abbot risen by
  wit; a "true villain" who keeps a debt more faithfully than any good man; secretly tilting
  to the Tokugawa. Heavy-lidded, lordly, formal; hunts the thief under pressure from Hideyoshi.

## Where the story stands (end of ch09)
The Kōga side is on the board. Gen'i, hunting the "capital thief" under Hideyoshi's pressure,
recalls his old life-debt and hires Mari Dōgen of Kōga. Kohagi's secret is out: she is Rokkaku
Yoshikata's daughter, Kōga-trained, planted on Imai Sōkyū by Ishida Mitsunari. Dōgen and Jūzō
each learn the other leads the rival side and size each other up. Then Hideyoshi departs for the
Korean war (Bunroku 1 / 1592) and the capital's shadow-war goes quiet: Jūzō lies low, waiting for
the Toyotomi collapse but refusing to leave the capital; Dōgen, uneasy at the silence, stays on in
Gen'i's grounds disguised as a shrine-keeper, having already glimpsed the sleeping Kohagi and left
a Kōga card. ch10 奇妙な事故 / A Strange Accident (opener already on folio 338) opens on the "vacuum"
this quiet has left among the tangled ninja of the capital.

## Next batch
B10 = ch10 奇妙な事故 / A Strange Accident, printed folios 338-372 (PDF 340-374; OFFSET +2, folio =
PDF - 2). ch10 body begins AFTER the 奇妙な事故 title on folio 338 (錯綜した関係にある京の忍者のあいだに、
ひとつの真空地帯ができた。); ch09's tail (before the title) is done. Then B11 = ch11 伊賀ノ山 / The Hills
of Iga, folios 373-396 (PDF 375-398), still in the +2 span.

## Open traps / environment
- **Offset is +2 across this whole middle span** because of the PDF 326/327 double-feed:
  folio = PDF - 2 from PDF 328 on. READ folios off the running heads; skip any further
  duplicate leaf; build data/pagemap for the span. Watch for a possible 1-leaf gap near 397-425.
- A chapter's tail can spill onto the next opener folio (ch03/04/06/07/08/09 did) — render the
  next opener and verify; make sure the next batch does not re-translate the spillover.
- Furigana leakage and dropped clauses cluster on the DENSE opener and the TAIL. Re-read both
  against the scan and run the compound-coverage grep before shipping.
- **assemble.py OVERWRITES data/zh/chNN.txt AND welds paragraphs** — hand-transcribe from the
  images; use a top-strip crop to read indents; if you run assemble as a coverage aid, back up
  data/zh first and restore before the grep.
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py (notes/figures) or the
  Write/Edit tool or a python json load/dump (glossary), then re-read to verify.
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words; place ⊂ compound).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution); if you run
  a post-hoc pass, watch clause-final over-contraction ("you're."/"there's." are ungrammatical).
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled. Pre-existing checker-regression FAIL
  (hook stands down on template stub) is unrelated to this book; leave it.
