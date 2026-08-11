# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B06

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana; the offset is 0 in this range (printed folio == PDF render page).

Do Batch B06 = ch06 「忍び文字」 (The Ninja Cipher), PDF pages 167-206 (printed folios 167-206), end to end per the CLAUDE.md pipeline. ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch06_reading.md on ch06 and fix any drift (contract inside Jūzō/Kuroami/Gohei dialogue where natural — ch05 first-drafted STILTED at 0.34x and needed one contraction pass to reach 1.06x; keep Kuroami's ござる weight on a few grave lines).

Environment / pipeline (the batch engineering is already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck is at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container was recycled).
2. OCR: render.py 167 206 --dpi 300; then ocr_crop.py 167 206 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 167 206 for the second read. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls).
3. find_figures.py 167 206 AND eyeball every page for line art (ch01-ch05 were text-only; if ch06 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: the automated assemble.py welds paragraphs on this vertical Japanese (the OCR mangles the sentence-final punctuation can_break() relies on). Translate by READING the rendered page images directly (data/png/p0NNNN.png), and build data/zh/ch06.txt as a hand-corrected, paragraph-aligned transcription read off the scan. That file IS the parity surface and the crop-verification record; force-add it (data/zh/ is gitignored). ch06 begins on folio 167 AFTER the 忍び文字 title with 珍皇院の藪を離れた風間五平は…; this is Gohei's thread, opening on a meditation on the くノ一 (kunoichi, the female ninja), picking up right after ch04's Chinnō-in scene. ch05 does NOT spill onto 167 (already confirmed in B05). BEFORE translating, read the final two pages of ch05's English (the tail of out/ch05_reading.md) so the voice carries. Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); ch06's tail may spill onto folio 207 (the ch07 opener 聚楽 / Juraku) — render it and check, and make sure B07 does not re-translate any spillover.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). Principal cast and the major historical/place names are decided in glossary.json; reuse them unchanged and record in PROGRESS which rows you reused. New here: くノ一/kunoichi terminology, likely more Kyoto geography, possibly historical figures. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans; for tight crops a 6x PyMuPDF clip-render of a page-fraction region reads furigana cleanly (B05 used a small crop.py helper in the scratchpad). Add glossary rows DIRECTLY into the sectioned people/places/terms with the Edit tool (the B04/B05 method — no apparatus_merge glossary flatten), then re-run check_content/qc_entities. AVOID adding a bare-name row whose romanization is a substring of a fuller row already in use: a bare 宗久→Sōkyū row retroactively tripped check_content on a pronoun-carried ch03 paragraph in B05 and had to be removed. NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch06_reading.md, '## The Ninja Cipher' as the h1 (settle the English title at translation; 忍び文字 = a ninja's secret writing/cipher — footnote it if the chapter turns on the device). Add a ch06 entry to data/checks.json (docs + sources). make_bilingual.py ch06 (parity FIRST). Then run: verify_unit.py ch06 (it auto-uses data/noise.txt); check_structure.py --pairs data/zh/ch06.txt out/ch06_reading.md; check_align.py ch06; qc_entities.py out/ch06_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch06_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch05 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōgyū/Sōkyū, the Hōin/Hōgen ranks and Kampaku office, Sakai the free-city, the meibutsu tea cult and Matsushima caddy, Tenka Fubu, Sekigahara, the Korea invasion (唐入り/朝鮮出兵), Tsurumatsu/Hidetsugu, Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha (京の大仏), the zodiac double-hours, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures shaku/chō/koku/ri/ken/kin, rappa/shinobi, jizamurai/gōshi, the B04 first-appearances (放下僧 juggler-priests, Nyoigatake/Daimonji, Gion, Katō Kiyomasa, Maeda Gen'i and the Kyoto magistracy), AND the B05 first-appearances: 羅刹/rakshasa, Sennyū-ji and the imperial tombs, Hattori Hanzō, the 金賦 gold largesse, the Jurakudai, the kōshin monkey. Note only ch06's NEW first-appearances (くノ一/kunoichi as a term of art; anything new historical/geographic). Anchor notes to BODY phrases (verbatim substrings), not heading-only text — the builder refuses a heading-only anchor. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B07 kickoff (ch07 「聚楽」 Juraku, PDF/printed 207-236) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (top-only; crop L0.035 R0.965 T0.075 B0.955;
  model jpn_vert psm5); offset 0 for folios 7-302 and 425-660, drifts +2 across
  ~338-397 (B09-B13 must build data/pagemap by reading folios there).
- **B01 = ch01 おとぎ峠 / Otogi Pass (folios 7-63): COMPLETE, approved at the voice
  gate.** ch01 is the FROZEN register reference. (523 source paragraphs, 17 notes.)
- **B02 = ch02 濡れ大仏 / The Rain-Soaked Buddha (folios 64-89): COMPLETE.** 276
  source paragraphs, 6 notes. Kisaru and Kohagi introduced; Matsukura killed,
  Kumobei conscripted.
- **B03 = ch03 白い法印 / The White Hōin (folios 90-123): COMPLETE.** 385 source
  paragraphs, 16 notes. Sōkyū's biography and the tea-room confrontation; the
  commission's motive (Hideyoshi's Korea war) drawn out; Kohagi revealed as
  Sōkyū's adopted daughter and made Jūzō's contact.
- **B04 = ch04 木さると五平 / Kisaru and Gohei (folios 124-148, tail on 149): COMPLETE.**
  286 source paragraphs, 5 new notes. Gohei has deserted Iga to serve Maeda Gen'i
  (magistrate of Kyoto) as Gero Shōbei Yasuji; rapes and recruits Kisaru; learns Jūzō
  is in the capital.
- **B05 = ch05 羅刹谷 / Rakshasa Valley (folios 149-166): COMPLETE.** 152 source
  paragraphs, 6 new notes (book total 50). All checks green (numbers 0/152, parity
  152|152, qc_entities/check_content/check_apparatus clean, register 1.06x ref after a
  contraction pass, qa_epub PASS, epubcheck 0/0/0/0). Jūzō and Kuroami install a
  20-man rappa band at a ruined Yakushi hall to spread anti-Toyotomi rumour; a long
  Shiba digression on Hideyoshi's gold; Jūzō reads Sōkyū's design (Sakai's wealth
  behind Ieyasu, Hattori Hanzō the broker, Iga to rise again); Kohagi suspected a
  Kōga infiltrator, to be killed on sight.

## ch01 corrections made earlier (do NOT undo)
1. ch01's dropped final two paragraphs restored in B02 (Iseya Kahei shop
   instruction + "idle talk of the world"); ch01 parity is 523 | 523.
2. ch01's Great Buddha note corrected in B02 to the NARA Tōdai-ji Vairocana
   (roofless since Matsunaga burned it 1567), not Hideyoshi's Hōkō-ji. In B03,
   Hideyoshi's OWN Great Buddha (方広寺大仏, the Kyoto Hōkō-ji) appears and is
   footnoted as DISTINCT from the Nara one. Keep the two straight. (ch05's 京の大仏 /
   方広寺 is Hideyoshi's Hōkō-ji again — cross-referenced, not re-noted.)

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana in the despace class; `--no-furniture-strip` skips the
  Chinese strip_folio/strip_runfoot. Furniture here is top-only, cropped.
- `ocr_dual.py`: Japanese second read (jpn_vert psm5 on grayscale + Otsu variant).
- `check_content.py` / `qc_entities.py`: skip non-dict glossary sections; subsume a
  shorter glossary key covered by a longer matched key at the same span.
- `data/checks.json`: the {docs, sources} config. ch01-ch05 in.
- `data/noise.txt`: check_numbers noise. B03 added 惣五郎, 千利休, 九州, 三宅, 巨万,
  五体, 四肢, 二千二百 / 千二百. B04 added 四条, 三条, 六波羅. B05 added 百姓, 何百年
  (百 not a count) and 二百五十五万 / 三十万五千 / 二万六千 / 百十 (real quantities the
  English carries but the parser cannot compose from words; noise the SOURCE side, per
  the B03 二千二百 precedent). Extend per its header, longest literal first; never
  noise a real quantity you dropped.
- **apparatus_merge glossary gotcha:** it flattens glossary rows to the file ROOT, but
  glossary.json is sectioned. Since B04, add rows DIRECTLY into people/places/terms
  with the Edit tool (no flatten, cleaner); re-check content/entities after. Notes and
  figures merge fine as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder refuses
  a heading-only anchor. Pick a unique body phrase so the marker lands where you mean.
- **check_content substring trap (B05):** do NOT add a bare-name glossary row whose
  romanization is a substring of a fuller row in use (bare 宗久→Sōkyū collided with
  "Imai Sōkyū" and retroactively failed a pronoun-carried ch03 paragraph). Keep such
  bare names consistent in prose but out of the glossary.

## Method note (every batch)
`assemble.py` is unreliable on this vertical-Japanese OCR (welds paragraphs). The
working method: translate by reading the rendered page images directly, and
hand-build `data/zh/chNN.txt` as a corrected, paragraph-aligned transcription (the
parity surface and crop-verification record). Force-add it (data/zh is gitignored).
**A chapter's last sentence can run onto the next chapter's opener folio** — ch03's,
ch04's did; ch05's did NOT (folio 167 is entirely the ch06 opener). Always render the
next folio's top to recover/deny the tail before shipping (rule 4), and make sure the
NEXT batch does not re-translate any spillover. For crop-verification the fastest tool
is a 6x PyMuPDF clip-render of a page-fraction rectangle (reads furigana cleanly);
verify_names.py --auto surfaces the dual-OCR disagreement spans worth cropping.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei
(風間五平 / 五平), Shimotsuge Jirōzaemon (下柘植次郎左衛門 / 次郎左衛門), Kisaru
(木猿; written 木さる in ch04-05), Kuroami (黒阿弥). Kohagi (小萩) and Imai Sōkyū
(今井宗久) are the other leads. B05 people added: Hattori Hanzō (服部半蔵),
Iwami-no-kami (石見守), Mitsuhide (光秀, bare surname-reading; see 明智光秀), Katsuie
(勝家, bare given name; see 柴田勝家), Natsumi-no-Mimiji (夏見ノ耳次, provisional).
B05 places added: Rakshasa Valley (羅刹谷), Senzan (泉山, provisional), Sennyū-ji
(泉涌寺), the Otonashi-gawa (音無川), the Ukiyo-bashi (浮世橋), Shimogyō (下京), the
Hōkō-ji (方広寺), Sado (佐渡), Ikuno (生野), the Jurakudai (聚楽第), Edo (江戸), the
Kantō (関東), Korea (朝鮮), the Ming (大明), Shikoku (四国), the Chūgoku provinces
(中国), Kishū (紀州), the Five Home Provinces (五畿内). B05 terms added: rakshasa
(羅刹), Kunihiro (国広), kōshin (庚申). Earlier rows (Nobunaga, Hideyoshi, Ieyasu,
Sōkyū, Iga, Kōga, Sakai, Ōsaka, Nara, Tōdai-ji, rappa, Tenshō, the measures, the B03
Sakai/tea rows, the B04 Kyoto geography, etc.) are all in glossary.json.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, tall for a ninja; terse, guarded, blunt
  (わし). A raw hunger for revenge under a monk-like idleness; a merchant's cold eye on
  the age ("not a breath of moisture" in the rappa's view). Drawn to Kohagi against his
  creed — in ch05 he will not kill her himself but consents to Kuroami doing it. The
  revenge-hunger now hardens into a will to "throw himself, body and life" into the
  work for Iga's restoration.
- **Kuroami:** Jūzō's aged genin (past fifty), under five shaku, near-silent boy's
  face; the shinobi art made flesh. Humble-archaic ござる/ござろう servant register to
  Jūzō, whom he has known "since swaddling-clothes" and chides like a father. Cold,
  practical, superstitious in his creed (no women inside a ninja's 結界); can snuff out
  his own presence mid-sentence. Fronts as the whetter "Iseya Kahei" beside the Hōkō-ji;
  runs the muster and installs the unseen Jūzō as chief. Was Jūzō's contact/shopkeeper.
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly, cruel; a "mean little
  shadow at the corner of the mouth" when he smiles. Superior/intimate わし・じゃ to
  inferiors, polite ます・です to a master. Deserted Iga for ambition; serves Maeda Gen'i
  as a spy-catcher under the alias Gero Shōbei Yasuji. ch06 is his thread again.
- **Shimotsuge Jirōzaemon:** the disfigured old master; gruff, archaic, teasing, wry,
  secretly tender toward Jūzō. Creed: be as earth, stone, wind. Old dialect (〜じゃ,
  〜のう), われ for "you". Has a daughter now coming up to Kyoto (mentioned ch05).
- **Kisaru (木さる/木猿):** the crowd-illusion virtuoso turned broken ninja-daughter;
  by ch04's end "parted from Iga for good," half-believing she loves Gohei, tempted by
  a thousand-koku future, still secretly holding Jūzō. Volunteered to kill Gohei (Jūzō
  notes this in ch05; Kuroami distrusts a woman for it).
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter, born a princess of a fallen house;
  his agent and Jūzō's contact. Cool, unbreakable poise; a smoky half-smile. Polite
  ます/でございます. In ch05 Jūzō names her as a suspected Kōga infiltrator whom Kuroami
  means to kill on sight — a thread now hanging over her.
- **Imai Sōkyū (今井宗久):** the White Hōin; frail, tiny, urbane old arms-merchant;
  cold irony over a war-profiteer's pride. ch05 reveals (through Jūzō's reasoning) his
  design: put Sakai's wealth behind Ieyasu so the Toyotomi fall.

## Where the story stands (end of ch05)
Two threads. THREAD A (Jūzō): hired to kill Hideyoshi, paid by Sōkyū of Sakai, with
Kohagi as contact; now in the capital, he has taken command (unseen) of a 20-man rappa
band and grasped the larger design — Sōkyū is steering Sakai's gold behind Ieyasu, and
Iga's restoration rides on Hideyoshi's death; but he suspects Kohagi is a Kōga plant.
THREAD B (Gohei): deserted to Maeda Gen'i, turned Kisaru into his creature, hunts Jūzō
for the reward. ch06 「忍び文字」 (The Ninja Cipher) returns to Gohei's thread and the
kunoichi.

## Next batch
B06 = ch06 「忍び文字」 / The Ninja Cipher, PDF/printed 167-206 (40 pages), offset 0.
ch06's body begins AFTER the 忍び文字 title on folio 167 (珍皇院の藪を離れた風間五平は…),
Gohei's thread. Then B07 = ch07 「聚楽」 / Juraku, 207-236.

## Open traps / environment
- Furigana leakage clusters on chapter-opener pages; body pages OCR cleanly.
- Offset stays 0 through folio 302; do not assume it later (see the survey note).
- A chapter's tail can spill onto the next opener folio — render it and verify; make
  sure the next batch does not re-translate the spillover.
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py or the
  Write/Edit tool, then re-read to verify.
- Numerals inside place-names / big spelled numbers the English carries but the parser
  cannot compose go in data/noise.txt (source side only), longest literal first.
- Pre-existing checker-regression FAIL (`hook stands down on template stub`) is
  unrelated to this book; leave it for a template-tooling session.
