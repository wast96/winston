# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B07

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana; the offset is 0 in this range (printed folio == PDF render page).

Do Batch B07 = ch07 「聚楽」 (Juraku), PDF pages 207-236 (printed folios 207-236), end to end per the CLAUDE.md pipeline. ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch07_reading.md on ch07 and fix any drift (contract dialogue where natural; ch05 first-drafted STILTED and needed a contraction pass, ch06 ran formal-by-design at 0.74x of ref which passed — a heavy-dialogue court chapter can legitimately sit below 1.0x, but keep the contractions living).

Environment / pipeline (the batch engineering is already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck is at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container was recycled).
2. OCR: render.py 207 237 --dpi 300 (include 237 for the tail check); then ocr_crop.py 207 236 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 207 236 for the second read. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls).
3. find_figures.py 207 236 AND eyeball every page for line art (ch01-ch06 were text-only; if ch07 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: the automated assemble.py welds paragraphs on this vertical Japanese (the OCR mangles the sentence-final punctuation can_break() relies on). Translate by READING the rendered page images directly (data/png/p0NNNN.png), and build data/zh/ch07.txt as a hand-corrected, paragraph-aligned transcription read off the scan. That file IS the parity surface and the crop-verification record; force-add it (data/zh/ is gitignored). ch07 begins on folio 207 AFTER the 聚楽 title with 聚楽第は、京の内野にある… . ch06's tail OCCUPIES THE TOP OF FOLIO 207 (through 慧は総身からみるみる力がぬけて、足もとの大地がゆらぐ思いがした。); do NOT re-translate that spillover — ch07 starts at the 聚楽 title lower on 207. BEFORE translating, read the final two pages of ch06's English (the tail of out/ch06_reading.md) so the voice carries. Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); ch07's tail may spill onto folio 237 (the ch08 opener 京の盗賊 / The Thief of the Capital) — render it and check, and make sure B08 does not re-translate any spillover.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). Principal cast and the major historical/place names are decided in glossary.json; reuse them unchanged and record in PROGRESS which rows you reused. New here: likely more Jurakudai/court geography and Hideyoshi's household, possibly historical figures. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans; for tight crops a 6x PyMuPDF clip-render of a page-fraction region reads furigana cleanly (a small crop.py helper lives in the scratchpad; re-create it if the container was recycled — it takes PAGE x0 y0 x1 y1 fractions and 6x-renders that rectangle). Add glossary rows DIRECTLY into the sectioned people/places/terms with the Edit tool (the B04-B06 method — no apparatus_merge glossary flatten), then re-run check_content/qc_entities. AVOID adding a bare-name row whose romanization is a substring of a fuller row already in use (a bare 宗久→Sōkyū row tripped check_content in B05; in B06 a bare 慧→Satoru row was likewise avoided because "Satoru" ⊂ "Watanabe Satoru"). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation. (In B06 a whole clause was dropped at a column boundary and only caught by an OCR-coverage grep; after transcribing, grep the raw data/txt OCR for any distinctive compound you do not find in your transcription.)
6. Write out/ch07_reading.md, '## Juraku' as the h1 (settle the English title at translation; 聚楽 = the Jurakudai palace, already glossed — footnote it further only if the chapter turns on it, else cross-reference the B05 note). Add a ch07 entry to data/checks.json (docs + sources). make_bilingual.py ch07 (parity FIRST). Then run: verify_unit.py ch07 (it auto-uses data/noise.txt); check_structure.py --pairs data/zh/ch07.txt out/ch07_reading.md; check_align.py ch07; qc_entities.py out/ch07_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch07_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch06 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōgyū/Sōkyū, the Hōin/Hōgen ranks and Kampaku/Ōkurakyō offices, Sakai the free-city, the meibutsu tea cult and Matsushima caddy, Tenka Fubu, Sekigahara, the Korea invasion (唐入り/朝鮮出兵), Tsurumatsu/Hidetsugu, Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha (京の大仏), the zodiac double-hours, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures shaku/chō/koku/ri/ken/kin/tsubo, rappa/shinobi, jizamurai/gōshi, the B04 first-appearances (放下僧 juggler-priests, Nyoigatake/Daimonji, Gion, Katō Kiyomasa, Maeda Gen'i and the Kyoto magistracy), the B05 first-appearances (羅刹/rakshasa, Sennyū-ji and the imperial tombs, Hattori Hanzō, the 金賦 gold largesse, the Jurakudai, the kōshin monkey), AND the B06 first-appearances: くノ一/kunoichi, 忍び文字/shinobi-moji (the ninja cipher), the Kashima/Katori swordsmanship tradition (with Bokuden), Miyamoto Musashi and the Yoshioka of Kyoto, Kisshōten, the Chōsokabe house. Note only ch07's NEW first-appearances. Anchor notes to BODY phrases (verbatim substrings), not heading-only text — the builder refuses a heading-only anchor. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B08 kickoff (ch08 「京の盗賊」 The Thief of the Capital, PDF/printed 237-301) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (top-only; crop L0.035 R0.965 T0.075 B0.955;
  model jpn_vert psm5); offset 0 for folios 7-302 and 425-660, drifts +2 across
  ~338-397 (B09-B13 must build data/pagemap by reading folios there).
- **B01 = ch01 おとぎ峠 / Otogi Pass (folios 7-63): COMPLETE, approved at the voice
  gate.** ch01 is the FROZEN register reference. (523 source paragraphs, 17 notes.)
- **B02 = ch02 濡れ大仏 / The Rain-Soaked Buddha (folios 64-89): COMPLETE.** 276 paras,
  6 notes. Kisaru and Kohagi introduced; Matsukura killed, Kumobei conscripted.
- **B03 = ch03 白い法印 / The White Hōin (folios 90-123): COMPLETE.** 385 paras, 16 notes.
  Sōkyū's biography; the commission's motive (Hideyoshi's Korea war); Kohagi revealed
  as Sōkyū's adopted daughter and Jūzō's contact.
- **B04 = ch04 木さると五平 / Kisaru and Gohei (folios 124-148): COMPLETE.** 286 paras, 5
  notes. Gohei deserts Iga to serve Maeda Gen'i as Gero Shōbei Yasuji; rapes and
  recruits Kisaru; learns Jūzō is in the capital.
- **B05 = ch05 羅刹谷 / Rakshasa Valley (folios 149-166): COMPLETE.** 152 paras, 6 notes.
  Jūzō and Kuroami install a 20-man rappa band; Jūzō reads Sōkyū's design (Sakai's
  wealth behind Ieyasu, Hattori Hanzō the broker); Kohagi suspected a Kōga plant, to be
  killed on sight.
- **B06 = ch06 忍び文字 / The Ninja Cipher (folios 167-206, tail on 207): COMPLETE.** 312
  paras, 5 new notes (book total 55). All checks green (numbers 0/312, parity 312|312,
  qc_entities/check_content/check_apparatus clean, register 0.74x ref, qa_epub PASS,
  epubcheck 0/0/0/0). Kohagi sends Gohei a shinobi-cipher letter and engineers a
  Jūzō-Gohei rooftop meeting at the Jurakudai (ten days hence, hour of the ox); she
  bankrolls the fictional Kashima swordsman Watanabe Satoru with Sōkyū's gold and pits
  him against Jūzō as a test; Jūzō outwits the ambush (a thrown crimson haori as decoy)
  and spares Watanabe without drawing his blade, telling him to bring the name of who
  sent him. Kohagi's inner turmoil: she has begun to love Jūzō and half-plans to kill
  him to reclaim her rappa's heart ("a fierce kind of love").

## ch01 corrections made earlier (do NOT undo)
1. ch01's dropped final two paragraphs restored in B02; ch01 parity is 523 | 523.
2. ch01's Great Buddha note corrected in B02 to the NARA Tōdai-ji Vairocana (roofless
   since Matsunaga burned it 1567), not Hideyoshi's Hōkō-ji. In B03 Hideyoshi's OWN
   Great Buddha (方広寺大仏, the Kyoto Hōkō-ji) appears and is footnoted as DISTINCT from
   the Nara one. Keep the two straight. (ch05's 京の大仏 / 方広寺 is Hideyoshi's Hōkō-ji
   again — cross-referenced, not re-noted.)

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana in the despace class; `--no-furniture-strip` skips the Chinese
  strip_folio/strip_runfoot. Furniture here is top-only, cropped.
- `ocr_dual.py`: Japanese second read (jpn_vert psm5 on grayscale + Otsu variant).
- `check_content.py` / `qc_entities.py`: skip non-dict glossary sections; subsume a
  shorter glossary key covered by a longer matched key at the same span. qc_entities is
  case-insensitive and accepts the first OR last word of a multi-word `en`; check_content
  needs the EXACT `en` string present, and only uses `en` that are Capitalised, slash-free
  and >= 4 chars (so lowercase common-noun terms like kunoichi are ignored by it).
- `data/checks.json`: the {docs, sources} config. ch01-ch06 in.
- `data/noise.txt`: check_numbers noise. B06 added 二条 (Nijō, covers 二条河原), 三方
  (sanbō offering-stand), 源九郎 (Kurō), 五官 (five senses). Extend per its header, longest
  literal first; never noise a real quantity you dropped. Hyphenated English numbers
  ("two-hundred-koku") do not parse — write them open ("two hundred koku").
- **apparatus_merge glossary gotcha:** it flattens glossary rows to the file ROOT, but
  glossary.json is sectioned. Since B04, add rows DIRECTLY into people/places/terms with
  the Edit tool (no flatten, cleaner); re-check content/entities after. Notes and figures
  merge fine as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder refuses a
  heading-only anchor. Pick a unique body phrase so the marker lands where you mean.
- **check_content / qc substring trap (B05, B06):** do NOT add a bare-name glossary row
  whose romanization is a substring of a fuller row in use (bare 宗久→Sōkyū collided with
  "Imai Sōkyū"; bare 慧→Satoru would collide with "Watanabe Satoru"). Add the base form or
  the full form, not both, and keep such names consistent in prose but out of the glossary.
- **Set-off markers:** `{p}` verse block (used for the ch06 cipher glyphs), `{v}` vignette
  italic block (used for the ch06 decoded message), `***` scene break, `{d}` dateline,
  `{g}` hour-gloss. check_structure strips them before parity.

## Method note (every batch)
`assemble.py` is unreliable on this vertical-Japanese OCR (welds paragraphs). The working
method: translate by reading the rendered page images directly, and hand-build
`data/zh/chNN.txt` as a corrected, paragraph-aligned transcription (the parity surface and
crop-verification record). Force-add it (data/zh is gitignored). **A chapter's last
sentence can run onto the next chapter's opener folio** — ch03's, ch04's, and ch06's did
(ch06 ends on 207, before the 聚楽 title); ch05's did NOT. Always render the next folio's
top to recover/deny the tail before shipping (rule 4), and make sure the NEXT batch does
not re-translate any spillover. For crop-verification the fastest tool is a 6x PyMuPDF
clip-render of a page-fraction rectangle (reads furigana cleanly); verify_names.py --auto
surfaces the dual-OCR disagreement spans worth cropping. **Dialogue-dense pages (a quick
「」-vs-narration exchange with narration tags interleaved) mis-order easily from the full
page — crop the columns and read the order literally (this bit hard on ch06 p181).**
**After transcribing, grep the raw data/txt OCR for distinctive compounds absent from your
transcription; a whole clause (吉祥天女に似た顔の) was dropped at a column boundary in B06
and only that catch found it — check_align cannot see a small mid-paragraph drop.**

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 /
五平), Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木猿; 木さる in ch04-05), Kuroami
(黒阿弥). Kohagi (小萩) and Imai Sōkyū (今井宗久) are the other leads. B06 people added:
Watanabe Satoru (渡辺慧, provisional — 慧 unglossed, narration uses bare 慧; NO bare-name
row), Sakakibara Yasumasa (榊原康政), Tsukahara Bokuden (塚原卜伝), Matsubayashi Samanosuke
(松林左馬助, prov.), Ashikaga Yoshiteru (足利義輝), Miyamoto Musashi (宮本武蔵), Taira no
Shigemori (平重盛), Yoshinaka (義仲), Myōbei (妙兵衛), Sunetsugi (すね次, prov.), Chōsokabe
(長曾我部). B06 places added: Nijō (二条 / 二条河原), Amidagamine (阿弥陀ヶ峰), Komatsudani
(小松谷), Hitachi (常陸), Kashima (鹿島), Katori (香取), Bandō (坂東), Ōsaka Castle (大坂城),
Yanagimachi (柳町), Wakasaya (若狭屋), Nakagyō (中京), Konoe (近衛), Marutamachi (丸太町),
Sakaimachi (堺町). B06 terms added: kunoichi (くノ一), ninja cipher / shinobi-moji (忍び文字),
Kisshōten (吉祥天女). Earlier rows (Nobunaga, Hideyoshi, Ieyasu, Sōkyū, Iga, Kōga, Sakai,
Ōsaka, Nara, Tōdai-ji, rappa, Tenshō, the measures, the B03 Sakai/tea rows, the B04-B05
Kyoto geography and cast, etc.) are all in glossary.json.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, tall for a ninja; terse, guarded, blunt
  (わし). A raw hunger for revenge under a monk-like idleness; a merchant's cold eye on the
  age. Drawn to Kohagi against his creed; will not kill her himself. In ch06 he sees
  through his own heart (went to "nail" her scheme but really to see her) and feels shabby
  for it; sets the rooftop-of-the-Jurakudai duel as pure ninja theatre, and spares
  Watanabe without drawing.
- **Kuroami:** Jūzō's aged genin (past fifty), under five shaku, near-silent boy's face;
  the shinobi art made flesh. Humble-archaic ござる/ござろう servant register to Jūzō, whom
  he has known "since swaddling-clothes" and chides like a father. Cold, practical,
  superstitious (no women inside a ninja's 結界); can snuff out his own presence
  mid-sentence. Fronts as the whetter "Iseya Kahei" beside the Hōkō-ji. Addresses/refers
  to Jūzō as "Master Jūzō".
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly, cruel; a "mean little shadow at
  the corner of the mouth" when he smiles. Superior/intimate わし・じゃ to inferiors, polite
  ます・です to a master. Deserted Iga for ambition; serves Maeda Gen'i as Gero Shōbei Yasuji
  at 200 koku. In ch06 the cipher letter unnerves him (a rappa lets fear stand, does not
  master it); he slices the letter-box in four.
- **Shimotsuge Jirōzaemon:** the disfigured old master; gruff, archaic, teasing, wry,
  secretly tender toward Jūzō. Creed: be as earth, stone, wind. Old dialect (〜じゃ, 〜のう),
  われ for "you". Has a daughter coming up to Kyoto (mentioned ch05).
- **Kisaru (木さる/木猿):** the crowd-illusion virtuoso turned broken ninja-daughter; by
  ch04's end "parted from Iga for good," half-believing she loves Gohei; still secretly
  holding Jūzō. Volunteered to kill Gohei.
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter, born a princess of a fallen house; his
  agent and Jūzō's contact. Cool, unbreakable poise; a smoky half-smile; a Noh-mask calm
  over a rappa's ruthlessness. Polite ます/でございます. In ch06 the psychological centre:
  she engineers the Jūzō-Gohei meeting, runs a net of rappa (Myōbei, Sunetsugi), bankrolls
  Watanabe with Sōkyū's gold, and — having begun to love Jūzō — half-plans to kill him to
  prove her own ruthlessness ("a fierce kind of love"); crumbles for one instant and hates
  herself for it. Still under Jūzō and Kuroami's kill-on-sight suspicion from ch05.
- **Imai Sōkyū (今井宗久):** the White Hōin; frail, tiny, urbane old arms-merchant; cold
  irony over a war-profiteer's pride. His design: put Sakai's wealth behind Ieyasu so the
  Toyotomi fall (drawn out in ch05; the Sakakibara/Watanabe thread in ch06 is Ieyasu's
  side reaching into his household).
- **Watanabe Satoru (渡辺慧, ch06; dead/spared):** fictional Kashima-school rōnin, 28-29,
  broad-shouldered, a mad blue light in his eye; earnest, boastful, innocent of money and
  so enslaved by it. Rough eastern register, contracts freely. Not expected to recur.

## Where the story stands (end of ch06)
Two threads converging on the Jurakudai. THREAD A (Jūzō): commands (unseen) a 20-man rappa
band; has grasped Sōkyū's design (Sakai's gold behind Ieyasu, Iga's restoration riding on
Hideyoshi's death); suspects Kohagi. He has now set a rooftop duel with Gohei at the
Jurakudai, ten days hence, hour of the ox. THREAD B (Gohei): Maeda Gen'i's spy-catcher,
hunting Jūzō; the cipher letter has drawn him toward the same rendezvous. THREAD C (Kohagi):
Sōkyū's/Ieyasu's agent, orchestrating both men while falling for Jūzō; her test of Watanabe
against Jūzō failed (Jūzō spared him). ch07 「聚楽」 / Juraku moves to the Jurakudai itself.

## Next batch
B07 = ch07 「聚楽」 / Juraku, PDF/printed 207-236 (30 pages), offset 0. ch07's body begins
AFTER the 聚楽 title on folio 207 (聚楽第は、京の内野にある…); ch06's tail occupies the top of
207 — do NOT re-translate it. Then B08 = ch08 「京の盗賊」 / The Thief of the Capital, 237-301.

## Open traps / environment
- Furigana leakage clusters on chapter-opener pages; body pages OCR cleanly.
- Offset stays 0 through folio 302; do not assume it later (see the survey note).
- A chapter's tail can spill onto the next opener folio — render it and verify; make sure
  the next batch does not re-translate the spillover.
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py or the Write/Edit
  tool, then re-read to verify.
- Numerals inside place-names / big spelled numbers the English carries but the parser
  cannot compose go in data/noise.txt (source side only), longest literal first.
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually
  (a setup.sh gap for Japanese books). epubcheck must be re-fetched if the container recycled.
- Pre-existing checker-regression FAIL (`hook stands down on template stub`) is unrelated to
  this book; leave it for a template-tooling session.
