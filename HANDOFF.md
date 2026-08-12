# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B08

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana; the offset is 0 in this range (printed folio == PDF render page).

Do Batch B08 = ch08 「京の盗賊」 (The Thief of the Capital), PDF pages 237-301 (printed folios 237-301), end to end per the CLAUDE.md pipeline. ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch08_reading.md on ch08 and fix any drift (contract dialogue where natural; ch05 first-drafted STILTED and needed a contraction pass, ch06 ran formal-by-design at 0.74x of ref which passed, ch07 landed at 0.99x — keep the contractions living, but a court/dialogue chapter may legitimately sit below 1.0x).

Environment / pipeline (the batch engineering is already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck is at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container was recycled).
2. OCR: render.py 237 302 --dpi 300 (include 302 for the tail check); then ocr_crop.py 237 301 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 237 301 for the second read. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls).
3. find_figures.py 237 301 AND eyeball every page for line art (ch01-ch07 were text-only; if ch08 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: the automated assemble.py welds paragraphs on this vertical Japanese (the OCR mangles the sentence-final punctuation can_break() relies on). Translate by READING the rendered page images directly (data/png/p0NNNN.png), and build data/zh/ch08.txt as a hand-corrected, paragraph-aligned transcription read off the scan. That file IS the parity surface and the crop-verification record; force-add it (data/zh/ is gitignored). ch08 begins on folio 237 AFTER the 京の盗賊 title with 真葛ヶ原の萩の花に露がおりた… . ch07's tail OCCUPIES THE TOP OF FOLIO 237 (through 重蔵は刀を捨てて、寮から消えた。); do NOT re-translate that spillover — ch08 starts at the 京の盗賊 title lower on 237. BEFORE translating, read the final two pages of ch07's English (the tail of out/ch07_reading.md) so the voice carries. Verify the unit's FINAL paragraphs against the scan explicitly before shipping (rule 4); ch08's tail may spill onto folio 302 (the ch09 opener 甲賀ノ摩利 / Mari of Kōga) — render it and check, and make sure B09 does not re-translate any spillover. As a coverage cross-check after transcribing, run assemble.py ch08 237 301 ONLY to catch a dropped paragraph (it welds, so use it for coverage, not text) and grep the raw data/txt OCR for any distinctive compound absent from your transcription (in B06 a whole clause was dropped at a column boundary; in B07 the paragraph 濠のふちから… was recovered exactly this way).
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). Principal cast and the major historical/place names are decided in glossary.json; reuse them unchanged and record in PROGRESS which rows you reused. New here: title 京の盗賊 = "The Thief of the Capital" (a thief-plot; likely new low-city geography, thieves'/pleasure-quarter cast, possibly Ishida Mitsunari's household reaching in — 石田治部少輔 appears on folio 237). Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. Tooling: verify_names.py --pdf source.pdf --page N --auto shows the dual-OCR disagreement spans; for tight crops a 6x PyMuPDF clip-render of a page-fraction region reads furigana cleanly (the small crop.py helper lives in the scratchpad; re-create it if the container was recycled — it takes PAGE x0 y0 x1 y1 fractions and 6x-renders that rectangle; PAGE is 1-based PDF page). Add glossary rows DIRECTLY into the sectioned people/places/terms (a byte-preserving json load/dump with ensure_ascii=False, or the Edit tool — the B04-B07 method, no apparatus_merge glossary flatten), then re-run check_content/qc_entities. AVOID adding a bare-name row whose romanization is a substring of a fuller row already in use, AND a hanzi key whose characters double as a counter/word elsewhere in the chapter (in B07, 一条 Ichijō was NOT added because 一条 also means "a single [rake]" on folio 209; 平 Hei was NOT added because 平 ⊂ 五平/平城). NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation.
6. Write out/ch08_reading.md, '## The Thief of the Capital' as the h1 (settle the English title at translation; the section titles are evocative — 京の盗賊 is literal enough). Add a ch08 entry to data/checks.json (docs + sources). make_bilingual.py ch08 (parity FIRST). Then run: verify_unit.py ch08 (it auto-uses data/noise.txt); check_structure.py --pairs data/zh/ch08.txt out/ch08_reading.md; check_align.py ch08; qc_entities.py out/ch08_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch08_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch07 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōgyū/Sōkyū, the Hōin/Hōgen ranks and Kampaku/Ōkurakyō/Ishida-office titles, Sakai the free-city, the meibutsu tea cult and Matsushima caddy, Tenka Fubu, Sekigahara, the Korea invasion (唐入り/朝鮮出兵) and Konishi Yukinaga, Tsurumatsu/Hidetsugu, Nanban, the Nara Great Buddha (Tōdai-ji) AND Hideyoshi's Hōkō-ji Great Buddha (京の大仏), the zodiac double-hours and 半刻/小半刻 durations, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures shaku/chō/koku/ri/ken/kin/tsubo/jō, rappa/shinobi, jizamurai/gōshi, the B04 first-appearances (放下僧, Nyoigatake/Daimonji, Gion, Katō Kiyomasa, Maeda Gen'i and the Kyoto magistracy), the B05 first-appearances (羅刹/rakshasa, Sennyū-ji, Hattori Hanzō, the 金賦 gold largesse, the Jurakudai, the kōshin monkey), the B06 first-appearances (くノ一/kunoichi, 忍び文字/shinobi-moji, the Kashima/Katori tradition with Bokuden, Miyamoto Musashi and the Yoshioka, Kisshōten, the Chōsokabe), AND the B07 first-appearances: 蓬莱/Hōrai, 小西行長/Konishi Yukinaga (弥九郎), 宣祖/Sŏnjo, 天竺/Tenjiku, and the 上り音曲・下り兵法 (east/Kamigata swordsmanship) proverb. Note only ch08's NEW first-appearances. Anchor notes to BODY phrases (verbatim substrings), not heading-only text — the builder refuses a heading-only anchor. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B09 kickoff (ch09 「甲賀ノ摩利」 Mari of Kōga, PDF 302-339 / printed 302-337 — offset 0 through folio 302, then WATCH for the +2 drift beginning ~folio 338/ch10; build data/pagemap by reading folios in the drift span) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (top-only; crop L0.035 R0.965 T0.075 B0.955;
  model jpn_vert psm5); offset 0 for folios 7-302 and 425-660, drifts +2 across
  ~338-397 (B09-B13 must build data/pagemap by reading folios there).
- **B01 = ch01 おとぎ峠 / Otogi Pass (folios 7-63): COMPLETE, approved at the voice
  gate.** ch01 is the FROZEN register reference. (523 source paragraphs, 17 notes.)
- **B02 = ch02 濡れ大仏 / The Rain-Soaked Buddha (folios 64-89): COMPLETE.** 276 paras, 6 notes.
- **B03 = ch03 白い法印 / The White Hōin (folios 90-123): COMPLETE.** 385 paras, 16 notes.
- **B04 = ch04 木さると五平 / Kisaru and Gohei (folios 124-148): COMPLETE.** 286 paras, 5 notes.
- **B05 = ch05 羅刹谷 / Rakshasa Valley (folios 149-166): COMPLETE.** 152 paras, 6 notes.
- **B06 = ch06 忍び文字 / The Ninja Cipher (folios 167-206, tail on 207): COMPLETE.** 312 paras, 5 notes.
- **B07 = ch07 聚楽 / Juraku (folios 207-236, tail on 237): COMPLETE.** 280 source
  paragraphs, 5 new notes (book total 60). All checks green (numbers 0/280, parity
  280|280, qc_entities/check_content/check_apparatus clean, register 0.99x ref,
  qa_epub PASS, epubcheck 0/0/0/0). Jūzō infiltrates the Jurakudai and meets Gohei
  on the tower roof (Gohei now Gen'i's spy-catcher, fires the palace as a diversion,
  lets Jūzō pass "this once"); Jūzō walks the town, re-engages the spared Kumobei,
  reads the anti-Toyotomi rumours (Konishi Yukinaga and the dreaded Korea war); at
  Komatsudani he confronts Kohagi, cannot kill her, falls into "a fierce rush of
  love," and in anger at his own weakness drives his blade through her thigh (sparing
  her) and vanishes.

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
  needs the EXACT `en` string present (substring match), and only uses `en` that are
  Capitalised, slash-free and >= 4 chars (so lowercase common-noun terms like kunoichi,
  "leather water-spider" are ignored by it).
- `data/checks.json`: the {docs, sources} config. ch01-ch07 in.
- `data/noise.txt`: check_numbers noise. B07 added 弥九郎 (Yakurō, the 九 a name), 三和土
  (tataki, the 三 part of the word). Extend per its header, longest literal first; never
  noise a real quantity you dropped. Hyphenated English numbers ("three-hundred") do not
  parse — write them open ("three hundred"), and a bare "three" won't carry a source 三百
  ("swells to three hundred").
- **Glossary is SECTIONED (people/places/terms), NOT flat.** apparatus_merge flattens
  rows to the file ROOT, so since B04 add rows DIRECTLY into the sections — either the
  Edit tool, or a json load/dump with ensure_ascii=False, indent=2 (B07 used the latter;
  git diff was insertions only, no reformat of existing rows). Notes and figures merge
  fine via apparatus_merge as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder refuses a
  heading-only anchor. Note bodies: literal Unicode is fine (em dash —, curly quotes);
  only NAMED HTML entities are rejected (use numeric refs or the literal char).
- **check_content / qc substring trap (B05, B06, B07):** do NOT add a bare-name glossary
  row whose romanization is a substring of a fuller row in use (宗久⊂Imai Sōkyū; 慧⊂Watanabe
  Satoru; 平⊂五平/平城), AND do NOT add a hanzi key whose characters double as a counter or
  common word elsewhere in the SAME chapter (一条 Ichijō ⊂ the counter 一条 "a single [rake]"
  on folio 209 — kept in prose, out of the glossary).
- **Set-off markers:** `{p}` verse block, `{v}` vignette italic block, `***` scene break,
  `{d}` dateline, `{g}` hour-gloss. check_structure strips them before parity. (ch07 used none.)

## Method note (every batch)
`assemble.py` is unreliable on this vertical-Japanese OCR (welds paragraphs) — but it is a
good COVERAGE cross-check: run it after hand-transcribing to catch a dropped paragraph (in
B07 it flagged 濠のふちから… on folio 209, which the page-level read had compressed; restored).
The working method: translate by reading the rendered page images directly, and hand-build
`data/zh/chNN.txt` as a corrected, paragraph-aligned transcription (the parity surface and
crop-verification record). Force-add it (data/zh is gitignored). **A chapter's last sentence
can run onto the next chapter's opener folio** — ch03/ch04/ch06/ch07 did (ch07 ends on 237,
before the 京の盗賊 title); ch05's did NOT. Always render the next folio's top to recover/deny
the tail before shipping (rule 4), and make sure the NEXT batch does not re-translate any
spillover. For crop-verification the fastest tool is a 6x PyMuPDF clip-render of a
page-fraction rectangle (reads furigana cleanly; scratchpad crop.py PAGE x0 y0 x1 y1);
verify_names.py --auto surfaces the dual-OCR disagreement spans worth cropping. **Dialogue-dense
pages mis-order easily from the full page — crop the columns and read right-to-left,
top-to-bottom literally (this bit on ch06 p181 and ch07 p218/p228; re-crop and confirm).**
**After transcribing, grep the raw data/txt OCR for distinctive compounds absent from your
transcription; check_align cannot see a small mid-paragraph drop.**

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵 / 重蔵), Kazama Gohei (風間五平 / 五平),
Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木猿; 木さる in ch04-05), Kuroami (黒阿弥).
Kohagi (小萩) and Imai Sōkyū (今井宗久) are the other leads. B07 people added: Yakurō (弥九郎,
= Konishi Yukinaga's common name), Mōri (毛利), Hosokawa (細川), Tokugawa (徳川, house),
Sŏnjo (宣祖). B07 places added: the Uchino (内野), Ōmiya (大宮), the Jōfuku-ji (浄福寺),
Shimochōjamachi (下長者町), Tenjiku (天竺), Uto (宇土), Awata (粟田), Korea (高麗, older name),
Hōrai (蓬莱). B07 terms added: leather water-spider (革水蜘蛛), shinobi rake (忍び熊手).
Earlier rows (Nobunaga, Hideyoshi, Ieyasu, Sōkyū, Iga, Kōga, Sakai, Ōsaka, Nara, Tōdai-ji,
rappa, Tenshō, the measures, the B03 Sakai/tea rows, the B04-B06 Kyoto geography and cast,
Konishi Yukinaga/Ryūsa, Watanabe Satoru, Maeda Gen'i, Kumobei, etc.) are all in glossary.json.
NOT in the glossary by design: 一条 Ichijō and 平 Hei (substring traps — see the tooling note).

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, tall for a ninja; terse, guarded, blunt (わし).
  A raw hunger for revenge under a monk-like idleness; a merchant's cold eye on the age. On the
  Jurakudai roof he tastes the rappa's solitude at its height (alone, face to face with the
  master of the realm). Bound by Iga's law to kill the deserter Gohei, he cannot, and borrows a
  bantering tone because his heart won't rise to it. With Kohagi (ch07 climax) he goes to force
  the truth, is disarmed, cannot kill her, kicks her down, is beaten by "a fierce rush of love,"
  and in anger at his own weakness drives the blade through her thigh (sparing her) and vanishes.
- **Kuroami:** Jūzō's aged genin (past fifty), under five shaku, near-silent boy's face; the
  shinobi art made flesh. Humble-archaic ござる/ござろう servant register to Jūzō, whom he chides
  like a father. Cold, practical, superstitious; can snuff out his own presence mid-sentence.
  Fronts as the whetter "Iseya Kahei" beside the Hōkō-ji. Sees the fire's opening at once and
  moves the rumour-net. Addresses/refers to Jūzō as "Master Jūzō".
- **Kazama Gohei:** beautiful, androgynous, cold, clerkly, cruel; a "mean little shadow at the
  corner of the mouth". Superior/intimate わし・じゃ to inferiors, polite ます・です to a master.
  Deserted Iga for ambition; serves Maeda Gen'i as the spy-catcher Gero Shōbei Yasuji at 200 koku.
  In ch07 the assured hunter: likens himself to a vanishing star, fires the Juraku as a diversion
  and kills without hesitation, lets Jūzō pass "this once" but vows to hunt him "to Tenjiku and
  Luzon" from tomorrow.
- **Shimotsuge Jirōzaemon:** the disfigured old master; gruff, archaic, teasing, wry, secretly
  tender toward Jūzō. Creed: be as earth, stone, wind. Old dialect (〜じゃ, 〜のう), われ for "you".
  (Offstage since ch05; named by both men on the roof — "the master of Shimotsuge" — as well.)
- **Kisaru (木さる/木猿):** the crowd-illusion virtuoso turned broken ninja-daughter; by ch04's
  end "parted from Iga for good," half-believing she loves Gohei; still secretly holding Jūzō.
  Gohei denies having met her in ch07 (Jūzō does not believe him).
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter, born a princess of a fallen house; his agent
  and Jūzō's contact. Cool, unbreakable poise; a smoky half-smile that will not freeze even under
  the blade; a wet, throaty laugh. Polite ます/でございます. In ch07: wanted "to see the colour of
  his blood," watched the Watanabe duel from the shadows, offers herself as a courtesan; under
  Jūzō's kill-threat she is drunk on her own strange desire and wins (the point sinks). Her true
  master still hidden — Sōkyū's agent, a suspected Kōga plant; Jūzō still under kill-on-sight
  suspicion of her from ch05.
- **Imai Sōkyū (今井宗久):** the White Hōin; frail, tiny, urbane old arms-merchant; cold irony
  over a war-profiteer's pride. His design: put Sakai's wealth behind Ieyasu so the Toyotomi fall.
- **Kumobei (雲兵衛):** the timid ex-wakō sailor spared in ch02; clownish, over-grateful,
  deferential (ございます). In ch07 re-met at Shijō, begs to attend Jūzō, and is set as an ear at
  the Iseya (told to dress as a tradesman's man). A recurring low-city thread — likely useful in
  ch08 ("The Thief of the Capital").

## Where the story stands (end of ch07)
Two ninja converging, and a woman between them. THREAD A (Jūzō): commands (unseen) a 20-man
rappa band sowing anti-Toyotomi rumour; has cased the Jurakudai for the final strike on Hideyoshi;
has now met Gohei face to face and been let pass "once." THREAD B (Gohei): Maeda Gen'i's
spy-catcher, will hunt Jūzō and the Iga band from tomorrow to build the case for his own rise.
THREAD C (Kohagi): Sōkyū's/Ieyasu's agent, orchestrating and falling for Jūzō; he has now spared
her a second time (the thigh-thrust), unable to kill. ch08 「京の盗賊」 / The Thief of the Capital
turns (title) to a thief-plot of the low city; 石田治部少輔 (Ishida Mitsunari) appears on folio 237.

## Next batch
B08 = ch08 京の盗賊 / The Thief of the Capital, PDF/printed 237-301 (65 pages), offset 0. ch08's
body begins AFTER the 京の盗賊 title on folio 237 (真葛ヶ原の萩の花に露がおりた…); ch07's tail
occupies the top of 237 — do NOT re-translate it. Then B09 = ch09 甲賀ノ摩利 / Mari of Kōga,
PDF 302-339 (printed 302-337) — offset 0 through 302, then the +2 drift begins ~338 (ch10).

## Open traps / environment
- Furigana leakage clusters on chapter-opener pages; body pages OCR cleanly.
- Offset stays 0 through folio 302; do not assume it later (see the survey note — +2 across ~338-397).
- A chapter's tail can spill onto the next opener folio — render it and verify; make sure the next
  batch does not re-translate the spillover.
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py or the Write/Edit tool,
  or a python json load/dump, then re-read to verify.
- Numerals inside place-names / big spelled numbers the English carries but the parser cannot
  compose go in data/noise.txt (source side only), longest literal first.
- Substring trap for glossary keys — see the tooling note (bare names ⊂ full names; hanzi keys ⊂
  counters/common words in the same chapter, e.g. 一条).
- setup.sh installs only the Chinese tesseract packs; install jpn + jpn_vert manually. epubcheck
  must be re-fetched if the container recycled.
- Pre-existing checker-regression FAIL (`hook stands down on template stub`) is unrelated to this
  book; leave it for a template-tooling session.
