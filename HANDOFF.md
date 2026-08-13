# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B07

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 6 are DONE (ch01 to ch28). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 7 = ch29 through ch33 (憎まれ歳三 / Toshizō the Hated; 四条橋の雲 / Clouds over Shijō Bridge; 堀川の雨 / Rain on the Horikawa; お雪 / Oyuki; 紅白 / Red and White), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. This span carries YAMANAMI KEISUKE'S SEPPUKU (he deserted at the end of ch28; his forced death under the Code, with Okita as his second, falls early here — fact-check the date, 2nd month Keiō 1 / 1865, and Okita's role) and the FIRST ENTRANCE OF OYUKI (ch32 お雪), the heroine Shiba INVENTED (see book.json translator_note); handle her as fiction, no fact-check of her existence, but note in the apparatus at first appearance that Shiba flags her as invented. Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch29=33_part0031, ch30=34_part0032, ch31=35_part0033, ch32=36_part0034, ch33=37_part0035. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks with scripts/scene_map.py OEBPS/Text/partNNNN.xhtml (a run of TWO OR MORE consecutive <p><br/></p> in the body is a break; the single pair after the title is only the title/body separator; body-paragraph N maps to source line N+2). Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it caught Rokusha/Momonoi in B02, Yamanami-not-Sannan in B03, Toshima/Mikura/Akazawa/Kujō in B04, Matsubara-an/Yoshimaro/Mizuo/Tantora in B05, and in B06: 外島→とじま Tojima but glossary keeps Toshima, 蒔田→まきた Makita not Maita, 来島→きじま Kijima, 一橋慶喜→ひとつばしよしのぶ; note the source also uses EXPRESSIVE gikun furigana like 将軍→たいじゅ, 京→ここ, 近藤→せんせい, which are semantic glosses, NOT phonetic, and must not be romanized), and consult glossary.json (then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」 silence is its OWN source paragraph and needs its OWN reading line (B04, B05 AND B06 each dropped/merged lines in dialogue and narration seams — B06 had THREE misses in ch26 alone and one each in ch27/ch28; make_bilingual caught them all; ALWAYS re-check dense exchanges and run-on narration for count). OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch28's English before starting ch29 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field; the merge nests it and check_apparatus stays clean; render the glossary's DECIDED form verbatim, e.g. 旗本→"hatamoto", 武州多摩→"Bushū Tama", or qc_entities/check_content flag it; when the source shortens a name give the glossary a bare-surname en). A NOTE ANCHOR must be a verbatim substring of the reading file with LITERAL macrons (ō, not sh&#333;gi); note BODIES use numeric character references for &-entities. Any figure from data/figs/ with a translated caption and real alt text (ch24-28 had none).
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity; and use spelled forms the checker parses — "a hundred or so" / "a hundred and some", not "a good hundred").
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 8 kickoff PASTED VERBATIM in a fenced code block. Batch 8 = ch34 through ch38.

Cite chapters and sections, never pages.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey), committed. book.json: 68 novel chapters (ch01 to
  ch68) + 3 back-matter units.
- B01 = ch01 「女の夜市」 / "The Women's Night Market", COMPLETE and APPROVED at
  the voice gate. ch01 FROZEN as the register reference (reference/ch01_ref.md;
  em-dash baseline 12.7/1k, dialogue contractions 24.9/1k). Notes 1 to 15.
- B02 = ch02 to ch07, COMPLETE. Notes 16 to 55.
- B03 = ch08 to ch13, COMPLETE. Notes 56 to 100.
- B04 = ch14 to ch18, COMPLETE. Notes 101 to 143.
- B05 = ch19 to ch23, COMPLETE. Notes 144 to 180.
- B06 = ch24 to ch28, COMPLETE. ch24 京師の乱 / "Turmoil in the Capital", ch25
  長州軍乱入 / "The Chōshū Army Storms In", ch26 伊東甲子太郎 / "Itō Kashitarō",
  ch27 甲子太郎、京へ / "Kashitarō Comes to Kyoto", ch28 慶応元年正月 / "New Year,
  First Year of Keiō". Notes 181 to 208 (28 this batch). All checks green;
  qa_epub PASS (208/208/208); epubcheck 0/0/0/0. Continuous note number now 208.
  Glossary 237 rows. 28 of 71 chapters translated. See PROGRESS.md B06 for the
  full record: the three parity misses (ch26 x3 seams, ch27 line 166, ch28 line
  50), the four content displacements fixed, the four fact-check verdicts, and
  every settled rendering.

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time (single space,
  em-dash aware). Reading keeps one line per source paragraph, so parity /
  number / entity checks are untouched. All checks strip {j}.
- scripts/scene_map.py (B02): reports scene breaks from data/src_epub XHTML
  (runs of two or more <p><br/></p> in the body). Body-paragraph N = source
  line N+2. Run per chapter. Needs data/src_epub (re-run ingest if empty).
- scripts/reading_to_en.py (B02): derives out/<id>_en.json from the authored
  out/<id>_reading.md so the flat parity array cannot drift.
- scripts/check_chapter.sh (B02): the per-chapter QC battery in one call.
- scripts/apparatus_merge.py (B02): glossary rows REQUIRE a "section" field and
  are nested into people/places/organizations/terms. Note ANCHORS must be
  verbatim substrings of the reading (LITERAL macrons); note BODIES use numeric
  character references for &-entities.
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys (zh
  length < 2), matching check_content. DO NOT REVERT.
- scripts/check_numbers.py (B04 PATCH, target-side only): spelled_numbers reads
  "a/one hundred and <ten..nineteen>" (110-119). It does NOT parse a bare
  "hundred": write "a hundred" / "one hundred" / "a hundred or so" so it maps to
  100. DO NOT REVERT.
- scripts/build_zh.py (B04): mechanical data/zh/<id>.txt builder from data/src.
- data/noise.txt (B01 to B06): Japanese name/idiom/place numeral rules, each
  commented. Add more as numbered names / teen-elisions / place-names appear.
  Never noise a real quantity. B06 added: 三々五々, 三田尻 (ch24); 五月人形,
  弥十郎, 忠三郎 (ch25); 三樹三郎 (ch26); 七子, 七五三之助, 二郎, 三村, 三田台町
  (ch27).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B06.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.
- GLOSSARY en for shortened names: when the source drops to a bare surname, set
  the glossary "en" to that bare form (古高 -> "Furutaka") so check_content
  matches every paragraph. Do NOT add a bare given-name row that is a SUBSTRING
  of an existing honorific key. SUBSTRING-COLLISION also runs the other way: in
  B06, 福田理兵衛 contains the pre-existing bare 理兵衛 -> "Rihei" (a different
  man, the Fuda innkeeper); rendered "Fukuda Rihei" so both keys are satisfied,
  and added the specific 福田理兵衛 row.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside ("by the way," "come
  to think of it") and the forward glance to events years ahead. Long descriptive
  sentences alternating with very short flat ones. Period texture, never
  antiquarian. KEEPS Shiba's own modern parentheticals (Western dates; "the
  present Crown Prince"; the national-railway station; quoted real letters,
  diaries, and memoirs like Nagakura's; the Ono Keijirō exam-book digression of
  ch26): KEEP them all.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 22 to 30 across the book. Rough Bushū
  farm dialect off guard, contracted and blunt. Cool, laconic, a dandy, a
  natural tactician. Class-obsessed. The cold ENGINE of the corps. His cruelty is
  matter-of-fact; his one soft spot is his SECRET HAIKU (pen-name Hōgyoku), which
  only Okita knows. In B06 he calls himself a "craftsman" (職人) who wants no
  rank and no fief, only to raise the corps into the first fighting-band under
  heaven; will help Kondō until Kondō himself quits the corps. He reads Itō as
  the real danger and Yamanami's defection as betrayal. Now "the hated" (ch29
  title).
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; slow to surprise,
  generous, believes in 気組. Supreme commander in name; learning his letters;
  weeps easily; calls Toshizō "Toshi." Bushū dialect. In B06 grown VAIN after
  Edo: lobbied the rōjū, plays the daimyō, parades Horikawa with thirty men,
  dreams of an "expel-the-barbarian daimyō" title, sits powdered white for the
  hotogara photograph sent by Yoshinobu. Outshone by Itō; holding rank over the
  corps to compensate. His sword is the Kotetsu; formal name Kondō Isami
  Masayoshi.
- OKITA SŌJI: 20 to 22, Edo-born, the corps' finest blade. Bright, boyish, glib,
  teasing, needles Toshizō, clowns near danger, cool as ice in a fight. Quick Edo
  tongue, contracts freely. The ONE person who knows Toshizō's haiku and his true
  heart; a fierce picky eater (won't touch raw things). His CONSUMPTION shows from
  ch16 (the cough); watch it. Will be Yamanami's second at the seppuku (B07).
- YAMANAMI KEISUKE: the eldest ex-Shieikan man, learned Sendai adept; educated,
  controlled, faintly stiff and formulaic, a sincere expel-the-barbarian
  idealist. Toshizō despises him. Shelved as GENERAL SECRETARY (総長, a grand
  empty title with no command). In B06 he draws close to Itō, resents Kondō's
  daimyō airs, and at the end of ch28 DESERTS THE CORPS. His forced seppuku under
  the Code (Okita his second) falls in B07 (early 1865). Do NOT write him as a
  living voice past that point.
- ITŌ KASHITARŌ: NEW in B06. Born Suzuki Daizō in Hitachi; pale, handsome, "of
  the clever quick-witted stamp," dressed like a great hatamoto. A fluent
  National-Learning (Kokugaku) scholar and Hokushin Ittō-ryū master; a
  topple-the-shogunate ideologue who joined the corps (late 1864) MEANING to
  capture it from within — poison Kondō thinks he can use as medicine. Refined,
  courteous, self-assured to a fault (Shinohara warns him he leans on his own
  cleverness). Educated Edo speech; addresses comrades as "-kun." His faction —
  Shinohara Tainoshin, Hattori Takeo, Kanō Michinosuke, Sano Shimenosuke,
  Nakanishi Noboru, Utsumi Jirō, plus his brother Suzuki Mikisaburō — shadow him
  and shun Western things (they will not look at the camera). Watch for the
  Kōdai-ji split and the Aburanokōji killing (1867).
- HARADA SANOSUKE: hot-blooded Iyo spearman, risen from chūgen stock, a
  belly-scar from an old half-botched suicide; rough, animal-loyal to Kondō,
  quick to tears and to a fight, close-mouthed, a dry cackle.
- SHICHIRI KENNOSUKE: the early antagonist, an iai master, cold mocking eyes, a
  RUSTY voice; Chōshū ties. Fought Toshizō at Nijōhanjiki-chō (B05) and ESCAPED
  AGAIN. STILL AT LARGE. Watch for his return.
- OSAE (佐絵 / お佐絵): the Fuchū shrine-daughter Toshizō loved in Bushū, revealed
  in B05 as a loyalist go-between in Kyoto. Her tie to Shichiri and the plotters
  is live; she may recur.
- KATSURA KOGORŌ (= Kido Takayoshi): the Chōshū Kyoto resident-agent, cool,
  lucky past belief. A recurring survivor; his diary is quoted as real.
- SERIZAWA KAMO, NIIMI NISHIKI, KIYOKAWA HACHIRŌ: all DEAD. Do not revive as
  living voices.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (237 rows). Enforced by
  check_content (people/places proper names) and qc_entities (all keys length
  >= 2). RENDER THE DECIDED FORM VERBATIM or the checks flag it: e.g. 旗本 ->
  "hatamoto", 武州多摩 -> "Bushū Tama", 京都守護職 -> "the Kyoto Protector", 所司代
  -> "the Shoshidai", 見廻組 -> "the Mimawarigumi", 公用方 -> "liaison office",
  助勤 -> "jokin", 監察 -> "inspector", 総長 -> "general secretary" (not a
  glossary key, but the fixed rendering).
- B06 settled forms. People: Matsudaira Sadaaki, Jinbō Kuranosuke, Maki
  Izumi-no-kami, Fukuhara Echigo, Kijima Matabee (来島 read Kijima), Kunishi
  Shinano, Fukuda Rihei, Takeda Kanryūsai, Yamazaki Susumu, Makita
  Sagami-no-kami Hirotaka (蒔田 read Makita), Toda Uneme-no-shō Ujiakira, Ohara
  Jinbee, Ōta Ichinoshin, Masuda Etchū, Kodama Minbu, Terashima Chūzaburō,
  Tsubaki Yajūrō, Itō Kashitarō, Ogata Shuntarō, Suzuki Mikisaburō, Shinohara
  Tainoshin, Kanō Michinosuke, Hattori Takeo, Sano Shimenosuke, Nakanishi
  Noboru, Utsumi Jirō, Matsumae Izu-no-kami, Hitotsubashi Yoshinobu, Ueno
  Hikoma, Matsumoto Ryōjun. Places: the Tenryū-ji, the Hamaguri Gate, Tennōzan,
  Kurodani, Mitajiri, the Gōō Shrine, the Sujikai Bridge, Fujinomori, the
  Takatsukasa mansion, the Kōshō-ji. Era-year form kept with the numeral ("the
  first year of Keiō"). Shiba's own modern intrusions KEPT.
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags (unchanged): Hijikata (1), Kondō (2), Okita
  (3), Inoue (4), Nagakura (5), Shichiri (6), Harada (7), Katsura (8), Yamanami
  (9), Serizawa (10), Saitō Hajime (11).

## Where the book stands (story)

- ch01 to ch07 (B01 to B02): the Tama-country prologue; the core cast assembles.
- ch08 to ch13 (B03): the dōjō ruined by epidemic; the Rōshigumi; Kyoto at Mibu.
- ch14 to ch18 (B04): the founding; the name SHINSENGUMI (1863); the Serizawa
  purge. Kondō sole head; Toshizō the cold engine.
- ch19 to ch23 (B05): the CODE OF THE CORPS; the IKEDAYA INCIDENT (8 July 1864);
  the corps made famous across the realm.
- ch24 to ch28 (B06): the aftermath. The KINMON / HAMAGURI GATE INCIDENT (Chōshū's
  July-1864 attack on the palace and its defeat; Kijima, Kusaka, Maki Izumi die;
  the Dondon-yaki fire). Kondō swells with vanity and plays the daimyō. ITŌ
  KASHITARŌ recruited (late 1864) — a topple-the-shogunate ideologue meaning to
  take the corps from within, his faction shadowing him. YAMANAMI KEISUKE, drawn
  to Itō and sick of Kondō's airs, DESERTS at the New Year of Keiō 1 (1865).

## What is NEXT

- B07 = ch29 to ch33 (kickoff above): 憎まれ歳三 (Toshizō the hated); 四条橋の雲;
  堀川の雨; お雪 (OYUKI, the invented heroine's entrance); 紅白. Carries YAMANAMI'S
  SEPPUKU (Okita his second) and OYUKI's first appearance. Then B08 ch34-38, B09
  ch39-43, B10 ch44-48, B11 ch49-53, B12 ch54-58, B13 ch59-63, B14 ch64-68, B15
  ch69-71 back matter + whole-book reconciliation + COMPLETION.

## Open items for the read-through

- ch29 憎まれ歳三 ("Toshizō the Hated"): the fallout of Yamanami's desertion and
  seppuku; Toshizō's growing unpopularity as the corps's hard enforcer. Fact-check
  Yamanami's death (2nd month Keiō 1 = early 1865; Okita as kaishaku).
- ch30-31 四条橋の雲 / 堀川の雨: watch the Itō faction's maneuvering and the corps's
  move (the Nishi-Honganji billeting comes around here historically).
- ch32 お雪 ("Oyuki"): the INVENTED heroine enters. Shiba himself flags her as
  fiction (translator_note). Note it in the apparatus at first appearance; do NOT
  fact-check her existence. Watch her register (she is Shiba's device for
  Toshizō's private self).
- ch33 紅白 ("Red and White"): follow whatever set-piece it names.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene_map.py needs data/src_epub, so re-run ingest before it if empty.
- Scene-break convention: two or more consecutive blank <p><br/></p> inside the
  body = a break; the single pair after the title is only the title/body
  separator. Body-paragraph N (scene_map) = source line N+2. Use scene_map.py.
- PARITY trap, PROVEN AGAIN in B06 (four misses): the source sets every quote,
  attribution (と…いった), and silence (「………」) as its own paragraph, AND a
  long narration or a lead-in ending in 、 can hide a line. B06 misses: ch26
  merged 「平助が悩んでいる」/91, dropped と洩らした/98, merged 酒になった/席上;
  ch27 dropped 「なにがおかしい」/166; ch28 dropped になるしかしかたがない/50.
  make_bilingual's count refused each; a positional re-read against the source
  located them. ALWAYS re-check dense exchanges AND run-on narration for count.
- NUMBER-CHECK traps: name/place/fabric numerals (三田尻, 五月人形, 七子, 弥十郎,
  三樹三郎, 七五三之助, 二郎, 三村, 三田台町) each take a commented noise rule; and
  the parser does NOT read a bare "hundred" — write "a hundred" / "a hundred or
  so" / "a hundred and some", and use "thirty to fifty" not "thirties to
  fifties." Real koku/troop/date/age figures stay in the English word-forms.
- CONTENT/ENTITY trap: render the glossary's decided form verbatim (旗本 ->
  "hatamoto", 武州多摩 -> "Bushū Tama"); a dropped parenthetical gloss counts as
  displacement (ch24 (松平容保) restored). SUBSTRING COLLISION both ways (see
  Tooling: 福田理兵衛 vs bare 理兵衛).
- NOTE-ANCHOR trap: the anchor must be a verbatim substring of the reading with
  LITERAL macrons; a numeric ref in an anchor (sh&#333;gi) will NOT match. Note
  bodies use numeric refs for &-entities only.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (it only passes on the template placeholder kickoff). Not a
  translation gate. All other tests pass.
- All work is on branch claude/burn-o-sword.
