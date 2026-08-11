# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B02

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the new "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana; the offset is 0 in this range (printed folio == PDF render page).

Do Batch B02 = ch02 「濡れ大仏」 (The Rain-Soaked Buddha), PDF pages 64-89 (printed folios 64-89), end to end per the CLAUDE.md pipeline. ch01 is the FROZEN register reference now: run scripts/check_register.py --ref out/ch01_reading.md on ch02 and fix any drift.

Environment / pipeline (the batch-1 engineering is already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck is at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container was recycled).
2. OCR: render.py 64 89 --dpi 300; then ocr_crop.py 64 89 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 64 89 for the second read (already Japanese-adapted). Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls).
3. find_figures.py 64 89 AND eyeball every page for line art (ch01 was text-only; if ch02 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: the automated assemble.py welds paragraphs on vertical Japanese (the OCR mangles the sentence-final punctuation can_break() relies on). Translate by READING the rendered page images directly (data/png/p00NN.png), and build data/zh/ch02.txt as a hand-corrected, paragraph-aligned transcription read off the scan. That file IS the parity surface and the crop-verification record; force-add it (data/zh/ is gitignored). BEFORE translating, read the final two pages of ch01's English (the tail of out/ch01_reading.md) so the voice carries; the story resumes exactly where ch01 stopped.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). The principal cast and the major historical names/places are already decided in glossary.json; reuse them unchanged and record in PROGRESS which rows you reused. Add new names with a status; flag any new principal with principal:true. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation; verify the unit's FINAL paragraphs against the scan explicitly before shipping.
6. Write out/ch02_reading.md, '## The Rain-Soaked Buddha' as the h1, one paragraph per source paragraph. Add a ch02 entry to data/checks.json (docs + sources). make_bilingual.py ch02 (parity FIRST). Then run: verify_unit.py ch02 (numbers with --noise data/noise.txt); check_structure.py --pairs data/zh/ch02.txt out/ch02_reading.md; check_align.py; qc_entities.py out/ch02_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi, the Sakai tea-masters/Rikyū, the Hōkō-ji Great Buddha, and the measures shaku/chō/koku/ri/ken, rappa/shinobi, jizamurai/gōshi. Note only ch02's NEW first-appearances. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B03 kickoff (ch03 「白い法印」 The White Hōin, PDF/printed 90-123) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (top-only; crop L0.035 R0.965 T0.075 B0.955;
  model jpn_vert psm5); offset is 0 for folios 7-302 and 425-660, drifts +2 across
  ~338-397 (B09-B13 must build data/pagemap by reading folios there).
- **B01 = ch01 「おとぎ峠」 / Otogi Pass (folios 7-63): COMPLETE and approved at the
  voice gate.** 521 source paragraphs, ~11.9k words, 16 footnotes. All checks green
  (numbers 0 unresolved, parity 521|521, qc_entities/check_content/check_apparatus
  clean, qa_epub PASS, epubcheck 0/0/0/0). ch01 is the FROZEN register reference.
  Revised in place per the commissioner's voice-gate notes (see STYLE.md).

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana added to the despace class; `--no-furniture-strip` flag skips
  the Chinese strip_folio/strip_runfoot (they delete short Japanese dialogue lines
  ending in 。 and only match Chinese 第X章). Furniture here is top-only and cropped.
- `ocr_dual.py`: Japanese second read (crop the body box, jpn_vert psm5 on a
  grayscale and an Otsu-binarised variant). `--lang/--psm/--left/...` restore the
  Chinese behaviour on a Chinese book.
- `check_content.py`: skips `_`-prefixed / non-dict glossary sections; subsumes a
  shorter glossary key covered by a longer matched key at the same span
  (山城-inside-丸山城 collision class). `qc_entities.py`: same subsume fix.
- `data/checks.json`: the {docs, sources} config for check_content / check_structure.
  Add each new unit here.
- `data/noise.txt`: Japanese entries for check_numbers (names 五平/百地/千宗易/三河,
  idioms 四散/四囲/三脚/四半刻/十数/幾千億/百年松/零細, and carried-but-under-parsed
  forms 五、六十 / 八〇 / 一万二千). Extend per its header rules, longest literal first.

## Method note (important for every batch)
The automated `assemble.py` is unreliable on this vertical-Japanese OCR (it welds
paragraphs where the OCR mangled sentence-final punctuation). The working method
that produced ch01: translate by reading the rendered page images directly, and
hand-build `data/zh/chNN.txt` as a corrected, paragraph-aligned transcription. That
transcription is both the parity surface and the crop-verification record (no
separate ocr_fixes replay). Force-add it (data/zh/ is gitignored).

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵), Kazama Gohei (風間五平),
Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木猿), Kuroami (黒阿弥).
Historical: Oda Nobunaga, Toyotomi/Hashiba Hideyoshi, Tokugawa Ieyasu, Akechi
Mitsuhide (惟任日向守光秀 = Koretō Hyūga-no-kami Mitsuhide), Niwa Nagahide, Takigawa
Kazumasu, Gamō Katahide, Asano Nagamasa, Tsutsui Junkei, Oda Nobukatsu, Shibata
Katsuie, Tsuge Kiyohiro, Momochi Shinnojō, Tateoka-no-Dōjun, Tsuzura Tarōbei, Imai
Sōkyū, Tsuda Sōgyū, Sen no Sōeki (Rikyū), Otowa-no-Kido, Yoshitsune. Places and
terms (Iga, Kōga, Otogi Pass, Sakai, the Honnō-ji, the Aekuni Shrine, rappa, the
Iga Rebellion, Tenshō, tōyaku, etc.) are in glossary.json too.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, unusually tall for a ninja; terse,
  guarded, minimal. Since his family's murder he runs on a raw human hunger for
  revenge; purposeless and monk-like at the pass, but a coiled force everyone feels.
  Plain samurai forms (わし), not uneducated.
- **Shimotsuge Jirōzaemon:** the disfigured old master; gruff, archaic, teasing, wry
  (あはは), commanding but secretly tender toward Jūzō. Creed: "be as earth, stone,
  wind; hold no human heart." Old dialect endings (〜じゃ, 〜のう, 出い, 居申したわ),
  uses われ for "you". A creature of pure flux.
- **Kazama Gohei:** beautiful, almost androgynous ("like a shrine-maiden girl");
  cool, clever, detached, the clerkly killer. Nihilist in a colder key than Jūzō;
  wants "the pleasures of the human world". Polite ます/です to his master, but
  distrustful.
- **Kuroami:** Jūzō's aged genin, under five shaku, past fifty, a face like a boy's;
  near-silent, flatly loyal, answers with 「左様か」 ("Is that so").
- **Kisaru:** Jirōzaemon's fierce, unreadable daughter, Gohei's betrothed; vows to
  run Gohei through herself if he betrayed Iga. Barely onstage yet (a lead later).

## Where the story stands (end of ch01)
Nine years after Iga was destroyed, Hideyoshi now rules Japan. The purposeless
hermit-ninja Jūzō is visited at his grandfather's hermitage on Otogi Pass by his
old master Jirōzaemon, who brings a commission from the Sakai tea-merchant Imai
Sōkyū: assassinate Hideyoshi. Jūzō, soft from years of idleness, accepts. The
rendezvous is set for the Hour of the Ox two nights hence, at the foot of the
Great Buddha (Hōkō-ji) in the capital; a messenger will come. Jūzō tells the old
genin Kuroami they leave tomorrow. Meanwhile Gohei (betrothed to Kisaru, sent to
the capital years ago) is reported dead or a traitor there. ch02 「濡れ大仏」 opens
on the Great Buddha rendezvous.

## Next batch
B02 = ch02 「濡れ大仏」 / The Rain-Soaked Buddha, PDF/printed 64-89 (26 pages),
offset 0. Then B03 = ch03 「白い法印」 / The White Hōin, 90-123.

## Open traps / environment
- Furigana leakage clusters on chapter-opener pages; body pages OCR cleanly.
- Offset stays 0 through folio 302; do not assume it later (see the survey note).
- Section English titles beyond ch01 are provisional (drafted for the skeleton);
  settle each at translation time. ch02 = "The Rain-Soaked Buddha".
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not translate CJK into JSON via a shell heredoc; use apparatus_merge.py or the
  Write tool, then re-read to verify.
