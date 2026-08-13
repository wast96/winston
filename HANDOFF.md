# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B09

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana.

Do Batch B09 = ch09 「甲賀ノ摩利」 (Mari of Kōga), PDF pages 302-339 (printed folios 302-337), end to end per the CLAUDE.md pipeline. OFFSET: 0 through this whole chapter (printed folio == PDF render page for 302-337); the +2 drift only begins at ch10 (奇妙な事故, PDF 340 = printed 338). Still, READ folios off the scan near the end to confirm where the drift starts and build data/pagemap for the drift span as you approach it (B10-B13 need it). ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch09_reading.md and fix any drift. CAUTION (the recurring failure mode): dialogue first-drafts STILTED. Contract the casual dialogue as you write (Jūzō blunt わし, Kisaru, low-city voices) — do NOT leave "It is/I do not/you are" everywhere; keep the grave uncontracted line only for deliberately-formal registers (Kuroami's ござる, obsequious まする to a lord, quoted documents). ch05/ch08 both needed a whole contraction pass afterward; ch06 ran formal-by-design at 0.74x and passed, ch07 at 0.99x, ch08 at 0.89x — a court/dialogue chapter may sit below 1.0x, but 0.0x is a draft error, not "formal by design".

Environment / pipeline (batch engineering already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container recycled).
2. OCR: render.py 302 340 --dpi 300 (include 340 for the tail check into the ch10 opener); then ocr_crop.py 302 339 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 302 339. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls).
3. find_figures.py 302 339 AND eyeball every page for line art (ch01-ch08 were all text-only; if ch09 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: assemble.py WELDS paragraphs on this vertical Japanese AND OVERWRITES data/zh/chNN.txt — the B08 lesson, do not let it clobber your work. Translate by READING the rendered page images directly (data/png/p0NNNN.png) and hand-build data/zh/ch09.txt as a corrected, paragraph-aligned transcription (the parity surface). Force-add it (data/zh/ is gitignored). ch09 begins on folio 302 AFTER the 甲賀ノ摩利 title with しかし、前田玄以は風間五平が思ったほど甘い男ではなかった。 . ch08's tail ENDS on folio 302 BEFORE that title (…思わず陰湿な笑いが唇許にのぼった。); do NOT re-translate it. BEFORE translating, read the final two pages of ch08's English (the tail of out/ch08_reading.md) so the voice carries. Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); render the ch10 opener folio and check whether ch09's tail spills onto it, and make sure B10 does not re-translate any spillover. As a COVERAGE cross-check after transcribing: back up data/zh/ch09.txt, run assemble.py ch09 302 339 (it overwrites — restore from the backup afterward), and grep the raw data/txt OCR for distinctive 3+-kanji compounds absent from your transcription (in B08 this caught two real drops on the dense opener and on folio 286 — the grep is meaningless unless data/zh holds the HAND transcription).
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). Principal cast and the major historical/place names are decided in glossary.json; reuse them unchanged and record in PROGRESS which rows you reused. New here: title 甲賀ノ摩利 = "Mari of Kōga" (Kōga is the rival ninja province across the ridge from Iga, already glossaried; 摩利 Mari is likely a Kōga figure — possibly tied to Kohagi's hidden Kōga side, or to Marishiten). Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans; for tight crops the scratchpad crop.py 6x-renders a page-fraction rectangle (PAGE x0 y0 x1 y1 fractions; PAGE 1-based) and reads furigana cleanly — re-create it if the container recycled. Add glossary rows DIRECTLY into the sectioned people/places/terms (byte-preserving json load/dump with ensure_ascii=False, or the Edit tool — the B04-B08 method, no apparatus_merge glossary flatten), then re-run check_content/qc_entities. AVOID a bare-name row whose romanization is a substring of a fuller row in use, AND a hanzi key whose characters double as a counter/common word in the same chapter. Numerals inside names go in data/noise.txt (source side only, longest literal first, one comment line each) — B08 added 十郎左衛門/三法師/三成/一条/百地/億劫/二重/二階/一尺五寸. NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch09_reading.md, '## Mari of Kōga' as the h1 (settle the English title at translation). Add a ch09 entry to data/checks.json (docs + sources). make_bilingual.py ch09 (parity FIRST). Then run: verify_unit.py ch09; check_structure.py --pairs data/zh/ch09.txt out/ch09_reading.md; check_align.py ch09; qc_entities.py out/ch09_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch09_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch08 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku/Kōji dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōkyū, the Hōin/Kampaku/Ōkurakyō/Ishida-office titles, Sakai the free-city, the meibutsu tea cult, Tenka Fubu, Sekigahara, the Korea invasion & Konishi Yukinaga, Tsurumatsu/Hidetsugu, Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha, the zodiac double-hours and 半刻/小半刻, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures shaku/chō/koku/ri/ken/kin/tsubo/jō/kan, rappa/shinobi/jōnin/genin, jizamurai/gōshi, the B04 first-appearances (放下僧, Nyoigatake/Daimonji, Gion, Katō Kiyomasa, Maeda Gen'i & the Kyoto magistracy), the B05 first-appearances (羅刹/rakshasa, Sennyū-ji, Hattori Hanzō, the 金賦 gold largesse, the Jurakudai, the kōshin monkey), the B06 first-appearances (くノ一/kunoichi, 忍び文字/shinobi-moji, Kashima/Katori with Bokuden, Miyamoto Musashi & the Yoshioka, Kisshōten, the Chōsokabe), the B07 first-appearances (蓬莱/Hōrai, Konishi Yukinaga/Sŏnjo/Tenjiku, the 上り音曲・下り兵法 proverb), AND the B08 first-appearances: Makuzugahara, Ishida Mitsunari (石田治部少輔/三成), Yamazaki (the 1582 victory), the Toyotomi Five Commissioners (go-bugyō), Yanagimachi (the pleasure-quarter), and the "crossing of Iga" (Iga-goe). Note only ch09's NEW first-appearances. Anchor notes to BODY phrases (verbatim substrings), not heading-only text — the builder refuses a heading-only anchor. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B10 kickoff (ch10 「奇妙な事故」 A Strange Accident, PDF 340-374 / printed 338-373 — the +2 drift is IN this span: build data/pagemap by reading folios) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (top-only; crop L0.035 R0.965 T0.075 B0.955;
  model jpn_vert psm5); offset 0 for folios 7-337 and 425-660, drifts +2 across
  ~338-397 (B10+ must build data/pagemap by reading folios there).
- **B01 = ch01 おとぎ峠 / Otogi Pass (folios 7-63): COMPLETE, approved at the voice
  gate.** ch01 is the FROZEN register reference. (523 source paragraphs, 17 notes.)
- **B02 = ch02 濡れ大仏 / The Rain-Soaked Buddha (64-89): COMPLETE.** 276 paras, 6 notes.
- **B03 = ch03 白い法印 / The White Hōin (90-123): COMPLETE.** 385 paras, 16 notes.
- **B04 = ch04 木さると五平 / Kisaru and Gohei (124-148): COMPLETE.** 286 paras, 5 notes.
- **B05 = ch05 羅刹谷 / Rakshasa Valley (149-166): COMPLETE.** 152 paras, 6 notes.
- **B06 = ch06 忍び文字 / The Ninja Cipher (167-206, tail 207): COMPLETE.** 312 paras, 5 notes.
- **B07 = ch07 聚楽 / Juraku (207-236, tail 237): COMPLETE.** 280 paras, 5 notes.
- **B08 = ch08 京の盗賊 / The Thief of the Capital (237-301, tail on 302): COMPLETE.**
  580 source paragraphs, 6 new notes (book total 66). All checks green (numbers
  0/580, parity 580|580, qc_entities/check_content/check_apparatus clean, register
  0.89x ref, qa_epub PASS, epubcheck 0/0/0/0). Kuroami's band turns to low-city
  thieving; Kuroami fails to kill Gohei (Shijō fight); Jūzō learns Shimotsuge is
  alive in Kyoto as the mad monk "Gyōzan" and that Shimotsuge/Gohei/Kisaru are
  selling him; Jūzō refuses Gohei's collusion offer, kills the informer Haruzemi,
  escapes by smoke-bomb; the long Maeda Gen'i digression + Gohei's audience (Gen'i
  unmasks him, promotes him to 300 koku, sets him to hunt the thief while himself
  tilting Tokugawa). TWO OCR-read drops caught+fixed (opener 237-238; folio 286).

## ch01 corrections made earlier (do NOT undo)
1. ch01's dropped final two paragraphs restored in B02; ch01 parity is 523 | 523.
2. ch01's Great Buddha note corrected in B02 to the NARA Tōdai-ji Vairocana (roofless
   since Matsunaga burned it 1567), not Hideyoshi's Hōkō-ji. In B03 Hideyoshi's OWN
   Great Buddha (方広寺大仏, the Kyoto Hōkō-ji) appears and is footnoted as DISTINCT from
   the Nara one; ch05/ch08 京の大仏/方広寺 is Hideyoshi's Hōkō-ji again (cross-ref).

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana in the despace class; `--no-furniture-strip` skips the Chinese
  strip_folio/strip_runfoot. Furniture here is top-only, cropped.
- `ocr_dual.py`: Japanese second read (jpn_vert psm5 on grayscale + Otsu variant).
- `check_content.py` / `qc_entities.py`: skip non-dict glossary sections; subsume a
  shorter glossary key covered by a longer matched key at the same span. qc_entities
  is case-insensitive and accepts the first OR last word of a multi-word `en`;
  check_content needs the EXACT `en` present (substring), and only uses `en` that are
  Capitalised, slash-free and >= 4 chars (so lowercase common-noun terms are ignored
  by it but still checked by qc).
- `data/checks.json`: the {docs, sources} config. ch01-ch08 in.
- `data/noise.txt`: check_numbers noise. B08 added the ch08 name/word numerals
  (十郎左衛門, 十郎左, 三法師, 三成, 一条, 百地, 億劫, 二重, 二階, 一尺五寸). Extend per its
  header, longest literal first, one comment line each; never noise a real quantity
  you dropped (fix the English to carry it — e.g. 千金 → "a thousand-gold steed").
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens
  rows to the file ROOT, so since B04 add glossary rows DIRECTLY into the sections
  (Edit tool, or json load/dump with ensure_ascii=False, indent=2). Notes and figures
  merge fine via apparatus_merge as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder refuses
  a heading-only anchor. Note bodies: literal Unicode is fine (em dash —, curly
  quotes); only NAMED HTML entities are rejected (use numeric refs or the literal char).
- **check_content / qc substring trap:** do NOT add a bare-name glossary row whose
  romanization is a substring of a fuller row in use (宗久⊂Imai Sōkyū; 平⊂五平/平城; 三成
  is safe, 石田三成 subsumes it), AND do NOT add a hanzi key that doubles as a counter or
  common word in the SAME chapter (一条 Ichijō ⊂ the counter 一条; kept out of glossary,
  noised for numbers only).
- **Set-off markers:** `{p}` verse, `{v}` vignette italic, `***` scene break, `{d}`
  dateline, `{g}` hour-gloss. check_structure strips them before parity. (ch07/ch08 used none.)

## Method note (every batch)
`assemble.py` is unreliable on this vertical-Japanese OCR (welds paragraphs) AND it
OVERWRITES data/zh/chNN.txt — the B08 lesson. Translate by reading the rendered page
images directly and hand-build `data/zh/chNN.txt` (the parity surface). Use assemble
ONLY as a coverage cross-check: back up data/zh/chNN.txt, run assemble, RESTORE the
backup, then grep the raw data/txt OCR for distinctive 3+-kanji compounds absent from
your HAND transcription (the grep is worthless if data/zh holds the welded version).
**On any long single-pass unit the DENSE opener and the tail are where faithfulness
fails** — B08 dropped three clauses on the furigana-heavy chapter-opener and a whole
clause on an exposition page, and had let a non-source bridge creep in; all caught by
the compound grep + re-reading the scan. A chapter's last sentence can spill onto the
next opener folio (ch03/04/06/07 did; ch05/ch08 did NOT) — render the next folio's top
and verify before shipping. For crop-verification the fastest tool is the scratchpad
crop.py 6x clip-render (PAGE x0 y0 x1 y1 fractions); verify_names.py --auto surfaces the
dual-OCR disagreement spans. **Dialogue-dense pages mis-order easily from the full
page — crop the columns and read right-to-left, top-to-bottom literally.**

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 /
五平), Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木さる / 木猿), Kuroami (黒阿弥).
Kohagi (小萩) and Imai Sōkyū (今井宗久) are the other leads. B08 people added: Ishida
Mitsunari (石田三成 / 三成), Kiyomasa (清正), Masanori (正則), Maekawa Jūrōzaemon
(前川十郎左衛門 / 十郎左衛門), Fujimoto Yasubei (藤本安兵衛), Kanamori (金森), Haruzemi
(春蟬), Nobutada (信忠), Sanbōshi (三法師), Oda Hidenobu (織田秀信). B08 places added:
Makuzugahara (真葛ヶ原), Tōfuku-ji (東福寺), Tō-ji (東寺), Nijō castle (二条城), Gifu castle
(岐阜城), Owari (尾張), Kōfu (甲府), Nakamura (中村), Yamato-kōji (大和小路). B08 terms:
the Seven Forms (七方出 shichihōde). NOT glossaried by design: Gen'i's aliases 徳善院
Tokuzen'in / 半夢斎 Hanmusai (prose only; rendered consistently), 一条 Ichijō (substring
trap; noised only). Earlier rows (Nobunaga, Hideyoshi, Ieyasu, Gen'i, Sōkyū, Hattori
Hanzō, Iga/Kōga/Sakai/Ōsaka/Nara, the tea/Kyoto/geography rows, the measures, 楯岡ノ道順
Tateoka-no-Dōjun, 音羽ノ城戸 Otowa-no-Kido, 松原通 "Matsubara road", etc.) are all in
glossary.json.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, terse, blunt (わし). The age has turned:
  grudge cooled into the one "tremendous ninja's stage" of killing Hideyoshi; Gohei,
  Kohagi and even Kisaru are "play within this time of waiting." Reads the three's
  betrayal and laughs it off as the fool's role. Cannot kill a woman who comes to him
  (Kohagi, Kisaru) — but kills the informer courtesan Haruzemi without a flicker.
- **Kuroami:** Jūzō's aged genin (past fifty), under five shaku, boy's face; humble
  archaic ござる/ござろう, chides Jūzō like a father. Acts on his own to execute the
  traitor Gohei (the genin does the dirty work the jōnin is above); loses the Shijō
  fight to Gohei's nimbler art, comes home with a cut wrist and a rare bashful smile;
  rages at Jūzō's softness. Cold, practical, superstitious; fronts as the whetter
  "Iseya Kahei." Addresses/refers to Jūzō as "Master Jūzō".
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly, cruel. Superior わし/じゃ to
  inferiors, obsequious ます/です to a master. Deserted Iga for ambition; now Gero
  Shōbei Yasuji, raised to 300 koku and made a squad-leader by Gen'i, who has unmasked
  him. Proposes open collusion to Jūzō (both keep their roles, both profit; Jūzō
  refuses with a thrown kozuka); to Gen'i plays the ambitious samurai and reads his
  master's secret Tokugawa tilt. Claims Kazama = a branch of the Hattori, of Taira line.
- **Shimotsuge Jirōzaemon:** the disfigured old master — ALIVE and in Kyoto. Master of
  the 七方出, best at the monk-form; a decade as the mad "Gyōzan"/Saint of the Bamboo,
  crossing to Iga every ten days. Gruff, teasing, われ for "you", 〜じゃ/〜のう. Dotes on
  Kisaru (his daughter) enough to sell Jūzō for her marriage to Gohei — but a rappa's
  loyalty is provisional and Jūzō would cut him without mercy if he turned.
- **Kisaru (木さる):** Shimotsuge's daughter; the crowd-illusion virtuoso. Wants Gohei
  as husband and begged her father to arrange it (which set the sale of Jūzō going);
  loves Jūzō too and cannot untangle her own heart (renjutsu from age three, "a
  guileless apparition"). Asks Jūzō to take her, then won't pledge; pushes him off in
  tears. Now warns him off ("trouble yourself no more with our affairs").
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter, born a princess of a fallen house;
  his agent and Jūzō's contact. Cool unbreakable poise, a smoky half-smile, a wet
  throaty laugh. In ch07 won the kill-threat duel (Jūzō spared her with the thigh-
  thrust). Her true master still hidden — Sōkyū's agent, a suspected Kōga plant; ch09
  甲賀ノ摩利 / Mari of Kōga likely turns to that side.
- **Imai Sōkyū (今井宗久):** the White Hōin; frail, tiny, urbane old arms-merchant; cold
  irony over a war-profiteer's pride. His design: Sakai's wealth behind Ieyasu so the
  Toyotomi fall.
- **Maeda Gen'i (徳善院/半夢斎):** the shrewd, tangled Kyoto magistrate — a former Owari
  abbot risen by wit; the ox-cart tyrant who cowed the capital; secretly tilting to the
  Tokugawa (historically the first to warn Ieyasu of the Ishida rising). Heavy-lidded,
  lordly, formal; sets Gohei to "probe, not seize."
- **Kumobei (雲兵衛):** the timid ex-wakō sailor spared in ch02; clownish, over-grateful
  (ございます); set as an ear at the Iseya. Now among Kuroami's ~30 rappa agents.

## Where the story stands (end of ch08)
The three-way trap has hardened: Shimotsuge + Gohei + Kisaru are selling Jūzō to the
Maeda/magistracy for Gohei's rise; Gen'i, tilting Tokugawa, wants the affair watched,
not closed. Jūzō — now a stranger and enemy to all of them — holds to the one strike on
Hideyoshi and waits for the perfect moment; Kuroami runs the low-city rumour-and-theft
war and wants Gohei and Kohagi dead now. Kohagi's true Kōga allegiance is still hidden.

## Next batch
B09 = ch09 甲賀ノ摩利 / Mari of Kōga, PDF/printed 302-337 (offset 0 throughout). ch09's
body begins AFTER the 甲賀ノ摩利 title on folio 302 (しかし、前田玄以は風間五平が思ったほど
甘い男ではなかった。); ch08's tail ends on 302 before that title — do NOT re-translate it.
Then B10 = ch10 奇妙な事故 / A Strange Accident, PDF 340-374 (printed 338-373) — the +2
offset drift is IN that span; build data/pagemap by reading folios.

## Open traps / environment
- Furigana leakage clusters on chapter-opener pages; the dense opener is where drops
  happen (B08 lost three clauses on folio 237-238). Re-read the opener + tail against
  the scan and run the compound-coverage grep before shipping.
- **assemble.py OVERWRITES data/zh/chNN.txt** — back up or redirect; restore before
  the coverage grep (the grep needs the HAND transcription).
- Offset stays 0 through folio 337; the +2 drift begins at ch10 (~338). READ folios
  off the scan as you approach it; build data/pagemap for the drift span.
- A chapter's tail can spill onto the next opener folio — render it and verify; make
  sure the next batch does not re-translate the spillover.
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py or the
  Write/Edit tool, or a python json load/dump, then re-read to verify.
- Substring trap for glossary keys (bare ⊂ full; hanzi ⊂ counters/common words).
- **Dialogue first-drafts STILTED — contract as you write** (see the kickoff caution);
  don't rely on a post-hoc pass, but if you run one, watch clause-final over-contraction
  ("you're."/"there's."/"how it's" are ungrammatical — revert those).
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually.
  epubcheck must be re-fetched if the container recycled.
- Pre-existing checker-regression FAIL (`hook stands down on template stub`) is
  unrelated to this book; leave it for a template-tooling session.
