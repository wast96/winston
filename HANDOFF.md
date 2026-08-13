# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B11

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B11 = ch11 「伊賀ノ山」 (The Hills of Iga), printed folios 373-396, end to end per the CLAUDE.md pipeline. OFFSET IS STILL +2 ACROSS THIS SPAN: folio = PDF render page minus 2 (PDF 375 = folio 373, the ch11 opener; PDF 398 = folio 396; ch12 吉野天人 開く at PDF 399 = folio 397). This is the same +2 caused by the PDF 326/327 double-feed (see B09/B10 notes). READ the folio off the running head of every opener and spot pages to CONFIRM, and BUILD data/pagemap/ch11.json for this span (ch08.json / ch10.json are the format model). WATCH for the possible 1-leaf scan gap near folios 397-425 that may bring the offset back to 0 (that is mainly B12-B13, but confirm the offset holds through folio 396 and flag any anomaly at the tail).

ch11 body begins on folio 373 AFTER the 伊賀ノ山 title with 天正伊賀ノ乱から数えてこの年は十三年目になる。京からおとぎ峠へもどった葛籠重蔵のうえに、ふたたび無為の日月が流れた。 . ch10's tail SPILLS onto folio 373 BEFORE that title (three paragraphs: 「当てにするのではないぞ。わしに命があればじゃな」 / 重蔵のわるい癖で… / 「それなら、おとなしゅう下柘植へ帰る。重蔵様の約束ならきっと確かじゃ」); those are DONE in ch10 — do NOT re-translate them. BEFORE translating, read the final two pages of ch10's English (the tail of out/ch10_reading.md) so the voice carries.

ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch11_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write (Jūzō blunt わし; Kuroami humble ござる; Kisaru dialect わし/じゃ and self-reference "Kisaru"; low-city voices) — do NOT leave "It is/I do not/you are" everywhere; keep the grave uncontracted line only for deliberately-formal registers (Kuroami's ござる, obsequious まする to a lord, quoted documents/scripture). ch05/ch08 both needed a whole contraction pass afterward; ch06 ran formal-by-design at 0.74x and passed, ch09 ran 1.21x, ch10 (dialogue-heavy) ran 2.31x — a court chapter may sit below 1.0x, but 0.0x is a draft error, not "formal by design".

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled). The pre-existing checker-regression FAIL "hook stands down on template stub" is unrelated; leave it.
2. OCR: render.py 375 400 --dpi 300 (folios 373-396 sit at PDF 375-398; render 399-400 too for the tail check into ch12); then ocr_crop.py 375 399 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 375 399. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls). CHECK each rendered page's running-head folio against the expected folio = PDF - 2; if any PDF page repeats the previous folio it is another double-feed (skip it) — and if a folio is SKIPPED, that is the 1-leaf gap re-mapping the offset; re-map from that page.
3. find_figures.py 375 399 AND eyeball every page for line art (ch01-ch10 were all text-only; if ch11 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by READING the rendered page images directly (data/png/p0NNNN.png) and hand-build data/zh/ch11.txt as a corrected, paragraph-aligned transcription (the parity surface); use a top-strip crop of each page (scratchpad crop.py) to read the paragraph INDENTS, since assemble mis-groups. Force-add data/zh/ch11.txt (data/zh/ is gitignored). Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch12 opener folio (PDF 399) and check whether ch11's tail spills onto it, and make sure B12 does not re-translate any spillover. COVERAGE cross-check after transcribing: extract every 3+-kanji compound from the raw data/txt OCR (over the ch11 PDF span, excluding any duplicate leaves) and confirm each appears in your HAND data/zh/ch11.txt — garbles are expected; a clean meaningful compound that is absent is a real drop to fix.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). Principal cast and majors are decided in glossary.json; reuse unchanged and record in PROGRESS which rows you reused. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans; the scratchpad crop.py 6x-renders a page-fraction rectangle (PAGE x0 y0 x1 y1 fractions; PAGE 1-based) and reads furigana cleanly — re-create it if the container recycled (see "Tooling in place" below for its body). Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False, or the Edit tool — the B04-B10 method, NOT apparatus_merge which flattens the glossary). AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter. Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch11_reading.md, '## The Hills of Iga' as the h1 (settle the English title at translation). Add a ch11 entry to data/checks.json (docs + sources). make_bilingual.py ch11 (parity FIRST). Then run: verify_unit.py ch11; check_structure.py --pairs data/zh/ch11.txt out/ch11_reading.md; check_align.py ch11; qc_entities.py out/ch11_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch11_reading.md. (qc/content want the rendered name once per paragraph the character appears in — do a name-survival pass over any pronoun-only paragraph, as in B10.)
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch10 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku dating, the Iga Rebellion (天正伊賀ノ乱), Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office (治部少輔) titles, Sakai the free-city, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu, Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours and 半刻/小半刻, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures (shaku/chō/koku/ri/ken/kin/tsubo/jō/kan/kanmon), rappa/shinobi/jōnin/genin, jizamurai/gōshi, くノ一/kunoichi, 忍び文字/shinobi-moji, Marishiten, the Udaifu/Naifu court titles, Yodo-dono & Odani, Rokkaku/Sasaki Yoshikata (Hakkansai/Jōtei) & Kannon-ji 1568, the 1487 Magari campaign, the fifty-three houses of Kōga, Kōga Saburō, the Odawara campaign, Nagoya castle in Hizen, Hattori Hanzō, the Jurakudai, the go-bugyō, the Iga-goe, Miyamoto Musashi & the Yoshioka, Kashima/Katori & Bokuden, AND the B10 first-appearances: the open way / shadow way (陽忍/陰忍) of ninja infiltration, the Bon spirit send-off (中元), shōchū, the Kyoto-to-Kōga escape route (Higashiyama/Shibutani/Daigo/Uji river). Note only ch11's NEW first-appearances. Anchor notes to BODY phrases (verbatim substrings), not heading-only text. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added), INCLUDING the confirmed folio-to-PDF map for this span and the data/pagemap/ch11.json you built.

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B12 kickoff (ch12 「吉野天人」 The Celestial Maiden of Yoshino, printed folios 397-424; the +2 span likely ENDS somewhere in 397-425 via a 1-leaf gap — read folios and extend data/pagemap, do not compute the offset) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (crop L0.035 R0.965 T0.075 B0.955; model
  jpn_vert psm5). Offset: 0 for folios 7-325; +2 from folio 326 (PDF 328) onward through
  the middle span (see the double-feed note under Tooling); an apparent 1-leaf gap near
  397-425 still to confirm (B12-B13).
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
- **B09 = ch09 甲賀ノ摩利 / Mari of Kōga (302-337, tail on 338): COMPLETE.** 324 paras, 11 notes.
- **B10 = ch10 奇妙な事故 / A Strange Accident (338-372, tail on 373): COMPLETE.** 312 paragraphs,
  4 new notes (book total 81). All checks green (numbers 0/312, parity 312|312, qc/content/
  apparatus clean, register 2.31x ref within tolerance, align median 9.70, qa_epub PASS,
  epubcheck 0/0/0/0). Gohei goads Jirōzaemon to his death at Dōgen's spear; Gohei rapes and
  casts off Kisaru (Jirōzaemon's daughter) and tells her Dōgen killed her father; Dōgen
  interrogates Kohagi at Komatsudani and is ambushed by Jūzō (who has come courting her);
  Jūzō takes Dōgen's hand, Dōgen escapes; Kisaru attaches herself to Jūzō, who sends her home
  to Shimotsuge to kill Dōgen herself. data/pagemap/ch10.json built (36 entries). NO figures.

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
- `data/checks.json`: the {docs, sources} config. ch01-ch10 in.
- `data/noise.txt`: check_numbers noise. B10 added `三昧` (zanmai / 刃物三昧). B09 added the
  roster/name numerals. Extend per its header, longest literal first, one comment line each;
  never noise a real quantity you dropped (fix the English to carry it).
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens
  glossary rows to the ROOT, so since B04 add glossary rows DIRECTLY into the sections
  (Edit tool, or json load/dump ensure_ascii=False indent=2). Notes and figures merge
  fine via apparatus_merge as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder refuses a
  heading-only anchor. Note bodies: literal Unicode is fine (em dash, macrons, curly
  quotes); only NAMED HTML entities are rejected (use numeric refs or the literal char).
- **Substring trap for glossary keys:** do NOT add a bare-name row whose romanization is a
  substring of a fuller row in use (宗久⊂Imai Sōkyū). SAFE full+bare pairs (重蔵/葛籠重蔵,
  摩利洞玄/洞玄, 望月刑部左衛門/刑部左衛門) are fine and used. When a place key collides as a
  substring of another word (山城 Yamashiro inside 釜山城 Pusan castle), add the longer key.
- **SCANNER DOUBLE-FEED (found B09):** PDF 326/327 are re-scans of folios 324/325. So
  **folio = PDF - 2 from PDF 328 onward** through the middle span (PDF 375 = folio 373 =
  ch11; PDF 399 = folio 397 = ch12). CHECK the folio on every rendered page; skip any further
  duplicate leaf. A SKIPPED folio marks the 397-425 1-leaf gap that re-maps the offset — watch
  for it near the end of B11/into B12.
- **scratchpad crop.py** (re-create if the container recycled): renders a fractional
  rectangle of a source.pdf page at high zoom so furigana is legible. Signature
  `crop.py PAGE x0 y0 x1 y1 [zoom]` (PAGE 1-based; fractions of the full page; default zoom 6).
  Uses pymupdf (`import fitz`/pymupdf), opens /home/user/winston/source.pdf, clips to the
  rect, saves scratchpad/_crop.png. Read the png to eyeball furigana / running-head folios.
- **Method:** hand-transcribe from the page images; use a top-strip crop (e.g. PAGE
  0.0 0.0 1.0 0.09) to read running-head folios and (0.05 0.07 0.95 0.20) for paragraph
  INDENTS, since assemble.py mis-groups AND overwrites data/zh/chNN.txt. Dialogue lines are
  their own paragraphs; narration that ends in 、 and leads into a quote is its own line (the
  quote is a separate line). Interleaved narration/dialogue on dense pages mis-orders from the
  full page — crop the columns and read right-to-left, top-to-bottom literally. Flush the
  transcription to a scratch build file per few pages so a context summary can't lose it.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 /
五平), Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木さる / key 木猿), Kuroami (黒阿弥).
Kohagi (小萩) and Imai Sōkyū (今井宗久) are the other leads. Mari Dōgen (摩利洞玄 / 洞玄; birth
name 伴藤内 Ban Tōnai; byname 甲賀ノ摩利 "Mari of Kōga"), Mochizuki Gyōbuzaemon (望月刑部左衛門 /
刑部左衛門; given name 重久 Shigehisa), Hakkansai (抜関斎 = Rokkaku/Sasaki Yoshikata), Jōtei
(承禎入道). Terms: Marishiten (摩利支天), Kōga Saburō (甲賀三郎), 竹ノ上人 "the Bamboo Saint"
(Jirōzaemon's disguise). Places used in ch10 (all pre-existing): Chinnō-in (珍皇院), Komatsudani
(小松谷), Amidagamine (阿弥陀ヶ峰), Higashiyama (東山). NOT glossaried by design: bare 摩利 "Mari";
Gen'i's aliases 徳善院 Tokuzen'in / 半夢斎 Hanmusai (prose only); ch10's single-appearance route
markers 渋谷 Shibutani, 醍醐 Daigo, 宇治川 Uji river, 郷之口 Gō-no-kuchi, 松原 Matsubara, 治部少輔
Jibu-no-shō. Earlier rows (Nobunaga, Hideyoshi, Ieyasu, Gen'i, Sōkyū, Hattori Hanzō, Ishida
Mitsunari, Iga/Kōga/Ōmi/Sakai/Ōsaka/Nara/Gifu, 方広寺 Hōkō-ji, 伊勢屋嘉兵衛 Iseya Kahei, おとぎ峠
Otogi Pass, the measures, etc.) are all in glossary.json.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, terse, blunt (わし). Plays a long waiting game
  for the Toyotomi collapse; will NOT leave the capital. In ch10 he cuts off Dōgen's hand,
  courts Kohagi (admits a "bond of the flesh" and, guardedly, fondness), and sends Kisaru home
  to kill Dōgen herself, half-promising marriage "if I'm still alive" — a bad habit of treating
  her as a child. Wry, dry.
- **Kuroami:** Jūzō's aged genin (past fifty), under five shaku, boy's face; humble archaic
  ござる/申す, chides Jūzō like a father, superstitious and fearful, practical. Fronts as the
  whetter "Iseya Kahei." Addresses/refers to Jūzō as "Master Jūzō". (Off-stage in ch10.)
- **Mari Dōgen (甲賀ノ摩利洞玄):** the aged Kōga rappa (past fifty, robust, eats dried boar's
  gall). Folksy, blunt, wry, self-mocking; わし/じゃ/のう/そこもと/おぬし. In ch10 he spears
  Jirōzaemon, interrogates Kohagi (blade to the eye, then finds the Iga scar), loses his left
  hand to Jūzō but escapes over the roof ("We'll settle it another day").
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly. Now Gero Shōbei Yasuji, raised to
  300 koku by Gen'i. Superior わし/じゃ to inferiors, obsequious ます/です to a master. In ch10:
  goads Jirōzaemon (his own old master) to death, then rapes and discards Kisaru, cold to the last.
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter; the natural daughter of Rokkaku Yoshikata,
  Kōga-trained (holds the Kōga license), planted on Sōkyū by Mitsunari. Cool unbreakable poise —
  holds even under Dōgen's blade; refers to herself formally as "Kohagi"; keeps her chastity
  "for one to whom I must keep it" (Jūzō, who once stabbed her; there is a bond of the flesh).
- **Kisaru (木さる):** Shimotsuge Jirōzaemon's daughter; now a full lead. Spirited, blunt, dialect
  (わし/じゃ; self-reference "Kisaru"). In ch10 Gohei rapes and casts her off and reveals Dōgen
  killed her father; she swears to kill Dōgen and Gohei, then attaches herself fiercely to Jūzō
  (loves him openly, was jealousy-paralysed watching him with Kohagi). Wounded, growing up fast.
- **Maeda Gen'i (徳善院/半夢斎):** the shrewd Kyoto magistrate, a "true villain" who keeps a debt
  more faithfully than any good man; secretly tilting to the Tokugawa. (Off-stage in ch10.)

## Where the story stands (end of ch10)
Jūzō's long silence has bred "strange accidents" among the capital's ninja. Gohei goaded his own
old master Shimotsuge Jirōzaemon into raiding the Maeda mansion, where Dōgen speared him through
the floor and Jirōzaemon fired a face-destroying charge rather than be taken. Freed of his master,
Gohei raped and discarded Kisaru (Jirōzaemon's daughter), telling her Dōgen was the killer.
Kisaru swore vengeance. Dōgen, interrogating Kohagi at Komatsudani, was ambushed by Jūzō (come
courting Kohagi); Jūzō took Dōgen's left hand but he escaped over the roof. Jūzō and Kohagi rode
for Kōga; Kisaru intercepted, and on the dawn ridge Jūzō sent her home to Shimotsuge to kill
Dōgen herself, half-promising marriage. ch11 伊賀ノ山 / The Hills of Iga (opener on folio 373)
opens thirteen years after the Tenshō Iga Rebellion, with Jūzō back at Otogi Pass and idle days
flowing over him again.

## Next batch
B11 = ch11 伊賀ノ山 / The Hills of Iga, printed folios 373-396 (PDF 375-398; OFFSET +2, folio =
PDF - 2). ch11 body begins AFTER the 伊賀ノ山 title on folio 373 (天正伊賀ノ乱から数えてこの年は
十三年目になる。京からおとぎ峠へもどった葛籠重蔵…); ch10's tail (three paras before the title) is
done. Then B12 = ch12 吉野天人 / The Celestial Maiden of Yoshino, folios 397-424 — where the +2
offset likely ENDS via a 1-leaf gap; read folios, do not compute.

## Open traps / environment
- **Offset is +2 across this middle span** because of the PDF 326/327 double-feed: folio = PDF - 2
  from PDF 328 on. READ folios off the running heads; skip any further duplicate leaf; build
  data/pagemap for the span. Watch for the possible 1-leaf gap near 397-425 that re-maps to 0.
- A chapter's tail can spill onto the next opener folio (ch03/04/06/07/08/09/10 all did) — render
  the next opener and verify; make sure the next batch does not re-translate the spillover.
- Furigana leakage and dropped clauses cluster on the DENSE opener and the TAIL. Re-read both
  against the scan and run the compound-coverage grep before shipping.
- **assemble.py OVERWRITES data/zh/chNN.txt AND welds paragraphs** — hand-transcribe from the
  images; use a top-strip crop to read indents.
- qc_entities / check_content want the rendered name once per paragraph the character appears in
  — do a name-survival pass over pronoun-only paragraphs (B10 fixed 20 such). Match the glossary
  `en` form exactly (e.g. "Ōkurakyō", not "Ōkura-kyō").
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py (notes/figures) or the
  Write/Edit tool or a python json load/dump (glossary), then re-read to verify. (Plain-text
  data/noise.txt via a heredoc is fine — it's not JSON — but re-read to confirm.)
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words; place ⊂ compound).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution); if you run
  a post-hoc pass, watch clause-final over-contraction ("you're."/"there's." are ungrammatical).
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled. Pre-existing checker-regression FAIL
  (hook stands down on template stub) is unrelated to this book; leave it.
