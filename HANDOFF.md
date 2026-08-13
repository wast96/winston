# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B05

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1, 2, 3 and 4 are DONE (ch01 to ch18). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 5 = ch19 through ch23 (再会 / Reunion; 二帖半敷町の辻 / The Crossroads at Nijōhanjiki-chō; 局中法度書 / The Code of the Corps; 池田屋 / The Ikedaya; 断章・池田屋 / Ikedaya: A Coda), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. ch22-23 are the Ikedaya Incident (June 1864), the book's set-piece; fact-check it carefully. Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks with scripts/scene_map.py OEBPS/Text/partNNNN.xhtml (a run of TWO OR MORE consecutive <p><br/></p> in the body is a break; the single pair after the title is only the title/body separator; body-paragraph N maps to source line N+2). Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it caught Rokusha/Momonoi in B02, Yamanami-not-Sannan in B03, Toshima Kihee / Mikura Isetake / Akazawa Morito / Kujō Hisatada in B04; note the source also uses EXPRESSIVE gikun furigana like 将軍→たいじゅ, 京→ここ, 近藤→せんせい, which are semantic glosses, NOT phonetic, and must not be romanized), and consult glossary.json (then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」 silence is its OWN source paragraph and needs its OWN reading line (B04 dropped two lines in a dialogue seam and make_bilingual caught it; verify the count). OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch18's English before starting ch19 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field; the merge nests it and check_apparatus stays clean; render the glossary's DECIDED form verbatim, e.g. 旗本→"hatamoto" not "bannermen", or qc_entities/check_content flag it). Any figure from data/figs/ with a translated caption and real alt text.
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 6 kickoff PASTED VERBATIM in a fenced code block. Batch 6 = ch24 through ch28.

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
- B04 = ch14 to ch18, COMPLETE. ch14 ついに誕生 / "Born at Last", ch15 四条大橋 /
  "Shijō Great Bridge", ch16 高瀬川 / "The Takase River", ch17 祇園「山の尾」/
  "The Yamanoo in Gion", ch18 士道 / "The Warrior's Code". Notes 101 to 143 (43
  this batch). All checks green; qa_epub PASS; epubcheck 0/0/0/0. Continuous
  note number so far: 143. See PROGRESS.md B04 for the full record, the six
  fact-check verdicts, the one caught omission, and every settled rendering.

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
  line N+2. Run per chapter.
- scripts/reading_to_en.py (B02): derives out/<id>_en.json from the authored
  out/<id>_reading.md so the flat parity array cannot drift.
- scripts/check_chapter.sh (B02): the per-chapter QC battery in one call.
- scripts/apparatus_merge.py (B02): glossary rows REQUIRE a "section" field and
  are nested into people/places/organizations/terms.
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys (zh
  length < 2), matching check_content. DO NOT REVERT.
- scripts/check_numbers.py (B04 PATCH, target-side only): spelled_numbers now
  reads "a/one hundred and <ten..nineteen>" and "<one..nine> hundred and <teen>"
  (values 110 to 119, e.g. 百十). Reaches the teens the old rules skipped between
  hundreds-plus-tens (120+). Target-side, so it can only ADD a translation
  number, never mask a dropped source quantity. Regression suite still green
  (pass-fixture OK, fail-fixture 5/5). DO NOT REVERT.
- scripts/build_zh.py (B04 NEW): mechanical data/zh/<id>.txt builder from
  data/src (title line then one body line per non-empty paragraph, skip 2
  headers). File-to-file copy, no authoring.
- data/noise.txt (B01 to B04): Japanese name/idiom/place numeral rules, each
  commented. Add more as numbered names / teen-elisions / place-names appear.
  Never noise a real quantity.
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside ("or so the story
  goes," "incidentally") and the forward glance to events years ahead. Long
  descriptive sentences alternating with very short flat ones. Period texture,
  never antiquarian. Keeps Shiba's own modern parentheticals (forerunner of
  Tokyo University; the Western calendar dates; "half past twelve"): KEEP them.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 22 to 28 across the book. Rough Bushū
  farm dialect off guard, contracted and blunt. Cool, laconic, a dandy, a
  natural tactician. Class-obsessed. In Kyoto he is now the cold ENGINE of the
  corps: the vice-commander who by design runs the jokin and inspectors and
  leaves Kondō the title. He conceives shidō as the corps's lord and enforces it
  by death (Niimi, Serizawa). Insists on "Hijikata," not "Toshi," among the men.
  His cruelty is matter-of-fact; his care for his blades (Kanesada, Kunihiro)
  and his organization is a craftsman's.
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; slow to surprise,
  generous, believes in 気組. Now supreme commander in name; learning his letters
  (imitating Rai San'yō), aspiring to the scholar-gentleman. Weeps easily; calls
  Toshizō "Toshi." Bushū dialect. Toshizō props him up and works him from below.
- OKITA SŌJI: 20 to 21, Edo-born, the corps' finest blade. Bright, boyish, glib,
  teasing, needles Toshizō, clowns near danger, cool as ice in a fight. Quick
  Edo tongue, contracts freely. From ch16 his CONSUMPTION shows (the recurring
  cough); the smile and the cough are his two recurring beats.
- YAMANAMI KEISUKE: the eldest ex-Shieikan man, learned Sendai adept; educated,
  controlled, faintly stiff and formulaic, a sincere expel-the-barbarian
  idealist who praises everything of Kyoto. Toshizō despises him. Now general
  secretary of the corps. His gentleness will destroy him (seppuku, 1865). His
  stiffness is DELIBERATE register, not drift.
- HARADA SANOSUKE: hot-blooded Iyo spearman, risen from chūgen (footman) stock,
  a belly-scar from an old half-botched suicide; rough, animal-loyal to Kondō,
  quick to tears and to a fight, close-mouthed. Laughs a dry cackle. To Toshizō
  he is almost the living example of the corps's shidō.
- SHICHIRI KENNOSUKE: the early antagonist, an iai master of the Araki-ryū,
  fleshy jowls, cold mocking eyes. Has come up to Kyoto and frequents the Chōshū
  residence on Kawaramachi (ch15); one of his Kōgen Ittō-ryū men escaped Toshizō
  at Kiyamachi (ch16), vowing revenge. WATCH FOR HIS RETURN (ch19 再会?).
- SERIZAWA KAMO and NIIMI NISHIKI: BOTH DEAD (ch18). Serizawa, the huge violent
  Mito co-commander, and his lieutenant Niimi, purged by the Kondō faction in
  the ninth month of 1863. Their faction (Noguchi, Hirayama, Hirama) is
  destroyed. Do not bring them back as living voices.
- KIYOKAWA HACHIRŌ: DEAD (assassinated at Akabanebashi, ch14). The Rōshigumi
  founder; gone from the living cast.
- OSEN, SATŌ HIKOGORŌ / ONOBU, KATSURA KOGORŌ: as in prior sheets (Hikogorō the
  Hino brother-in-law still funds the corps by courier).

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json. Enforced by check_content
  (proper names) and qc_entities (all keys length >= 2). RENDER THE DECIDED FORM
  VERBATIM: e.g. 旗本 → "hatamoto" (NOT "bannermen"), or the checks flag it.
- B04 settled forms: 新選組 "the Shinsengumi"; 新徴組 "the Shinchōgumi"; 学習院
  "the Gakushūin"; 所司代 "the Shoshidai"; corps ranks 局長 "commander" (kyokuchō),
  副長 "vice-commander" (fukuchō), 助勤 "jokin", 監察 "inspector" (kansatsu);
  士道 "the warrior's code" (shidō); 士道不覚悟 "unpreparedness in the warrior's
  code". Places: 先斗町 "Pontochō", 木屋町 "Kiyamachi", 高瀬川 "the Takase River",
  島原 "Shimabara", 角屋 "the Sumiya", 本能寺 "the Honnō-ji", 黒谷/金戒光明寺
  "Kurodani / the Konkai Kōmyō-ji". People: 外島機兵衛 "Toshima Kihee", 島津久光
  "Shimazu Hisamitsu", 佐々木唯三郎 "Sasaki Tadasaburō", 九条尚忠 "Kujō Hisatada",
  島田左近 "Shimada Sakon", 谷三十郎 "Tani Sanjūrō", 広沢富次郎 "Hirosawa
  Tomijirō", 久坂玄瑞 "Kusaka Genzui", 山崎烝 "Yamazaki Susumu", 赤沢守人
  "Akazawa Morito". 鴻池 "the Kōnoike". Era-year form kept with the numeral
  (e.g. "the third year of Bunkyū"); Shiba's own modern intrusions KEPT.
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags now: Hijikata (1), Kondō (2), Okita (3),
  Inoue (4), Nagakura (5), Shichiri (6), Harada (7), Katsura (8), Yamanami (9),
  Serizawa (10), Saitō Hajime (11). (Serizawa dead but a principal of the arc.)

## Where the book stands (story)

- ch01 to ch07 (B01 to B02): the Tama-country prologue. Toshizō the rakish
  farmer's son; the Rokusha killing and the Shichiri feud; the core cast
  assembles at the Edo dōjō.
- ch08 to ch13 (B03): Katsura outfences Shichiri; the Hachiōji raid; the 1862
  epidemic ruins the dōjō and drives the company into the shogunate's Rōshigumi;
  Toshizō buys his Kanesada; in Kyoto at Mibu, Kiyokawa reveals the corps's
  secret imperial purpose, and Toshizō resolves to break away and found a new
  party, allying with Serizawa Kamo.
- ch14 to ch18 (B04): the founding. The Kiyokawa assassination is botched;
  Kiyokawa returns to Edo (renamed Shinchōgumi) and is himself killed. Through
  Serizawa's Aizu-connected brother and the liaison officer Toshima Kihee, the
  Mibu band gets Aizu patronage, money, and the name SHINSENGUMI (spring 1863).
  Toshizō organizes it on Western company lines (three commanders, two
  vice-commanders, jokin and inspectors) and keeps the working power as
  vice-commander. He builds the corps's martial name in Kyoto by night killings
  (the Shijō bridge, the Kiyamachi fight). Then he purges the Serizawa half: on
  the shidō argument he forces Niimi's seppuku, and in a night raid the Kondō
  faction kills Serizawa, Hirayama, and Serizawa's mistress Oume (Sept 1863).
  Kondō is now sole head; Toshizō the cold engine beneath him.

## What is NEXT

- B05 = ch19 to ch23 (kickoff above): the corps consolidates; the written CODE
  of the corps (局中法度書, ch21); and the IKEDAYA INCIDENT (ch22-23, June 1864),
  the book's great set-piece. Then B06 ch24-28, B07 ch29-33, B08 ch34-38, B09
  ch39-43, B10 ch44-48, B11 ch49-53, B12 ch54-58, B13 ch59-63, B14 ch64-68,
  B15 ch69-71 back matter + whole-book reconciliation + COMPLETION.

## Open items for the read-through

- ch19 再会 ("Reunion"): confirm WHO is reunited. Watch for Shichiri Kennosuke's
  return (his man swore revenge in ch16) and/or the reappearance of a Tama
  figure. Consult the furigana for any new Kyoto/Chōshū name.
- ch21 局中法度書 ("The Code of the Corps"): the famous written Shinsengumi law,
  the formal descendant of the shidō doctrine argued in ch18. Render its clauses
  carefully; fact-check the code's text and provenance (it is historically
  attested but its exact wording is debated).
- ch22-23 池田屋 / 断章・池田屋 ("The Ikedaya" and a coda): the Ikedaya Incident
  of the fifth month of 1864 (5 July 1864), the raid that made the Shinsengumi
  famous. Fact-check the date, the casualties, Miyabe Teizō / Yoshida Toshimaro,
  and Kondō's small party; expect Shiba to dramatize. Watch Okita's consumption
  (he collapses coughing at the Ikedaya in the received story).

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene_map.py needs data/src_epub, so re-run ingest before it if empty.
- Scene-break convention: two or more consecutive blank <p><br/></p> inside the
  body = a break; the single pair after the title is only the title/body
  separator. Body-paragraph N (scene_map) = source line N+2. Use scene_map.py.
- PARITY trap, PROVEN in B04: the source sets every quote, every attribution
  (と…いった), and every silence (「………」) as its own paragraph, and a whole
  reply can hide in a fast dialogue seam. ch18 dropped two lines there;
  make_bilingual's count refused, reading_to_en + an index scan located it.
  Always re-read a dense exchange against the source for count.
- NUMBER-CHECK traps: teen-elisions (十二、三) and tens-elisions (三、四十) take a
  noise rule; names and PLACE NAMES with numerals take a noise rule (四条, 二条,
  三条, 千本, 三本木, 五郎, 唯三郎 added in B04); four-char idioms with 万/十
  (万、まちがい, 万能, 十手, 五体) take a noise rule; a hundred-plus-teens value
  (百十) now reads from the word-form "a hundred and ten" thanks to the
  check_numbers patch. Real koku/troop/date figures stay in the English.
- CONTENT/ENTITY trap: render the glossary's decided form verbatim in a
  paragraph that names a glossaried referent (write "Toshima Kihee", "Akazawa
  Morito", "hatamoto" in full), or check_content / qc_entities reports it.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (it only passes on the template placeholder kickoff). Not
  a translation gate. All other tests pass.
- All work is on branch claude/burn-o-sword.
